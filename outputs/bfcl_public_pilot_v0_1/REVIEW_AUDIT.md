# Independent proposal and A/B review audit

Audited 2026-09-12, initially before final adjudication and then extended with the final-output checks below. **All enumerated arithmetic, schema, mapping, content-preservation and frozen-file hash checks passed.** This audit recomputed results directly from preserved submissions and their mappings, rather than relying on a summary or joining rows by position. The extension read preserved `results/JUDGE_RAW.jsonl` and final outputs; no `work/bfcl_judge` content or owner gold was read, and no existing data was modified.

## Proposal accounting and preservation

All 200 opportunities have distinct IDs exactly covering evaluator context. There are **59 proposed candidates (29.5%) and 141 abstentions (70.5%)**. Proposer 1 contributes 29 proposals and 71 abstentions; proposer 2 contributes 30 and 70. The 59 proposals contain 58 execution-class-1 entries and one class-2 entry; none are class 3. These classes describe submitted preparations, not evidence of executed tools.

Both raw proposer files contain exactly the required fields: `item_id`, `proposal_status`, `candidate_action`, `execution_class`, `work_product`, and `prefix_support`. Every abstention has null action, class and work product; every proposal has a nonempty action/work product and valid integer class. All rows have nonempty prefix support. The proposed and abstention subsets exactly reproduce the corresponding rows of `ALL_OPPORTUNITIES.jsonl`, with no missing or overlapping IDs.

Every raw proposal field is unchanged after mapping its opaque ID into joined evaluator output. Every joined prefix equals both its corresponding raw proposer-input prefix and evaluator-context prefix. All 59 artifacts were inspected alongside these six-word prefixes: supplied concrete names or numeric values are visible in the prefixes, while generated scaffold choices and unresolved fields remain preparation rather than retrieved results. No observed artifact incorporates a completed-instruction-specific tool catalog or hidden result. This semantic inspection is a bounded leakage check, not proof of absence of memorization, a work-product quality judgment, or validation of actual execution. Generic scaffolds may add assumptions or have little surviving value; the review labels preserve uncertainty about such cases.

## Reviewer input boundary

Each reviewer input and mapping contains exactly 59 unique IDs covering all proposals and no abstentions. Each input row contains only `item_id`, `prefix`, `candidate_action`, `execution_class`, `work_product`, `full_instruction`, and `fixture_contract`; each content field exactly matches the corresponding joined proposal. The input files do not contain proposer identities, prefix-support rationales, source IDs, source domains, other-rater judgments, or expected labels. A and B have different opaque IDs and shuffled orders; only two positions happen to refer to the same source item across the two sequences.

These are evaluator inputs, so the full first-turn instruction is intentionally visible to reviewers. File-content blinding does not establish that two AI judgments are independent humans or prove isolation of every external agent context. The proposer boundary remains stricter: proposer input files contain only opaque ID and prefix. Mappings and evaluator files must stay out of proposer context.

Both raw rating files have exactly the expected six fields, valid binary/null values, valid fractional/null values, integer confidence 1–5, Y/N ambiguity flags, and nonempty rationale. Every binary null is paired with a fractional null and ambiguity Y; the converse binary/fractional null correspondence also holds. No null was converted into a negative or discarded from the saved data.

## Independently recomputed A/B counts

| Measure | Rater A | Rater B |
|---|---:|---:|
| Reusable / binary 1 | 32 | 32 |
| Non-reusable / binary 0 | 7 | 7 |
| Binary unresolved | 20 | 20 |
| Fractional utility null | 20 | 20 |
| Ambiguity Y | 29 | 33 |
| Total | 59 | 59 |

Identical marginal totals conceal different item-level decisions. After joining by true item ID:

| A decision | B decision | Count |
|---|---|---:|
| 1 | 1 | 30 |
| 0 | 0 | 7 |
| null | null | 18 |
| null | 1 | 2 |
| 1 | null | 2 |

Complete binary pairs number **37**, of which **37 agree (100%)**. On this selected complete-pair subset, each rater has 30 positives and 7 negatives. Expected chance agreement is `(30² + 7²) / 37² = 0.6932067202`; Cohen's kappa is **1.0**. The other **22/59 pairs (37.29%)** have at least one null and are excluded from this binary statistic. There are no opposing 0-versus-1 pairs, but four resolved-versus-unresolved differences. Treating null as its own status gives descriptive exact agreement **55/59 (93.22%)**; that is a different measure, not binary reliability.

Ambiguity flags overlap on 27 items and occur on **35 distinct items** in either review. Of the complete binary pairs, 13 still have an ambiguity flag from at least one rater. Exact numeric fractional ratings agree on 24 complete pairs and differ on 13; 18 pairs have two fractional nulls and four have one fractional null. Binary agreement therefore does not imply equal utility judgments or absence of uncertainty.

For compact identification below, each number expands to `BP1-multi_turn_base_<number>`.

- Both binary-null: 11, 28, 36, 46, 56, 58, 67, 89, 93, 105, 116, 131, 157, 163, 174, 175, 179, 194.
- A null / B 1: 18, 183.
- A 1 / B null: 30, 45.
- A ambiguity Y: 11, 18, 28, 30, 36, 41, 45, 46, 56, 57, 58, 67, 85, 89, 93, 105, 107, 116, 131, 157, 163, 171, 174, 175, 176, 179, 183, 189, 194.
- B ambiguity Y: 11, 18, 24, 28, 30, 36, 41, 44, 45, 46, 56, 58, 67, 86, 89, 93, 103, 105, 107, 116, 131, 133, 135, 157, 163, 171, 174, 175, 176, 179, 183, 189, 194.

Confidence counts are A: 2 at confidence 2, 23 at 3, 24 at 4, 10 at 5; B: 1 at 2, 26 at 3, 19 at 4, 13 at 5. Neither has confidence 1. Confidence and fractional utility are AI annotations, not empirical calibration or measured compute savings.

## Freezes, correction and domains

Every file listed in `INPUT_FREEZE.json`, `PROPOSAL_FREEZE.json`, `REVIEW_INPUT_FREEZE.json`, and `RATINGS_FREEZE.json` matches its recorded SHA-256. `METADATA_CORRECTION.json` accurately records the three joined-output after-hashes. Replacing only their corrected `candidate_origin` value with the former pending value and reproducing the original JSONL serialization reconstructs **all three recorded before-hashes exactly**. This independently substantiates the stated metadata-only change. Raw submissions, original pending evaluator context, reviewer inputs and labels remain frozen.

The separate `REBUILD_CHECK.json` reports eight adapter files reproduced byte-identically from a fresh pinned-source build. This audit read that report and verified applicable current freezes; it did not perform another adapter rebuild.

The domain file independently revalidates 200 unique IDs with exact context coverage. Primary counts remain Travel 63, Device/Home Control 30, Other/Unclear 26, Document Work 25, Finance-like Read-only Analysis 24, Information Retrieval 18, General Productivity 11, Communication 3. These are evaluator-only descriptive AI tags; ontology and unit-comparison caveats in `DOMAIN_NOTES.md` continue to apply.

## Interpretation limits

Abstentions are unproposed opportunities, not reuse negatives. The 59 reviewed artifacts are policy-selected preparations at one six-word checkpoint per conversation, not a random sample of all 7,415 word positions. All source and cross-conversation dependence limitations in `ADAPTER_AUDIT.md` remain. High selected-subset AI agreement does not establish independent-human reliability, a human G1 pass, frozen-model prediction accuracy, latency savings, or improvement over the earlier synthetic review set. Final adjudication remains provisional AI review, with arithmetic and preservation checked below rather than substantive rejudging.

## Final adjudication extension

The final `ALL_ITEMS.jsonl` contains all 200 opportunities exactly once and preserves every original joined field and every domain annotation. All 59 proposed items retain their A/B ratings exactly after ID mapping and receive one mapped final judgment. All 141 abstentions have null A, B and adjudication records. The preserved judge submission contains 59 unique opaque IDs exactly matching its mapping; its SHA-256 matches `SCORES.json`. Both files in `JUDGE_INPUT_FREEZE.json` match their hashes. Every judge-input artifact/context field matches the original proposal and both attached rating payloads match the respective raw submissions. The judge therefore sees both ratings and is an adjudicator, not a blinded independent third rater.

Raw final judgment fields and types pass schema checks. All 28 final binary nulls also have fractional null and ambiguity Y. Final categories recompute to **24 reusable, 7 non-reusable, 28 unresolved, and 141 abstentions**; the four saved result subsets exactly reproduce their respective rows and form a disjoint exhaustive partition of all 200 opportunities. There are **39 final ambiguity flags**: 28 unresolved judgments plus 11 resolved judgments. Survival-mechanism counts and primary-domain opportunity/proposal counts also match the saved score summary.

Score denominators independently verify as:

| Reported quantity | Exact denominator | Value |
|---|---|---:|
| Proposal coverage | 59 / 200 opportunities | 29.50% |
| Reusable per opportunity | 24 / 200 opportunities | 12.00% |
| Reusable per proposed candidate | 24 / 59 proposals | 40.68% |
| Reusable among resolved adjudications | 24 / 31 resolved proposals | 77.42% |

These quantities are not interchangeable. The last omits 28 unresolved proposals and all abstentions; none estimates frozen-model accuracy. `RATING_DISAGREEMENTS.jsonl` correctly contains IDs 18, 30, 45 and 183. These are **positive-versus-null differences**, not opposing positive-versus-negative judgments. Any prose calling them four “binary disagreements” is imprecise; the numerical score correctly records zero opposing binary disagreements on 37 complete pairs.

The synthetic comparator's **136 reusable, 59 non-reusable, 5 unresolved, 19 ambiguity flags** matches the earlier synthetic README already inspected. Its corresponding reusable proportions are 136/200 = 68.00% of candidate-review items and 136/195 = 69.74% of resolved items. Its candidate opportunity coverage was not measured under this prefix-only proposer and cannot be treated as 100%. The comparator's task/family units and domain-row counts are consistent with that README and the permitted domain-field inspection. This audit did not independently re-audit underlying synthetic ratings, action-class totals or checkpoint statistics; those extra comparator fields in `SCORES.json` are outside the independently verified scope here.

No failures were found in the enumerated checks; unresolved and ambiguous review findings remain preserved above.
