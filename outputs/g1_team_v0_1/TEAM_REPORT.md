# AI team annotation and judgment — v0.1

Three fresh AI agents labeled all 200 original items. Their initial submissions were frozen before comparisons or adjudication. A separate review phase used rater C as the judge; rater A independently checked the arithmetic and rater B assessed methodological validity. **Human G1 remains PENDING. No extraction ran.**

## Original label agreement

| Rater | Reusable | Non-reusable | Ambiguous |
|---|---:|---:|---:|
| A | 146 | 54 | 37 |
| B | 148 | 52 | 34 |
| C | 148 | 52 | 32 |

| Pair | Observed agreement | Cohen κ |
|---|---:|---:|
| A / B | 99.0% | 0.974333 |
| A / C | 98.0% | 0.948665 |
| B / C | 99.0% | 0.974012 |

The primary comparison was A versus B, specified before labels. Three-rater Fleiss κ was **0.965634**. All three agreed on **196/200** binary judgments. The four nonunanimous items were T026-P3, T037-P2, T048-P1 and T050-P1. These are descriptive AI agreement statistics, not accuracy against gold labels, human reliability, or evidence for H1–H4.

## Judgment results

The judge reviewed **62 items**, selected by the frozen rule: any binary disagreement, any rater ambiguity flag, or one of 20 controls chosen before labeling. The decisions were: **23 reusable, 13 non-reusable and 26 unresolved**. Across the full dataset, provisional labels are **125 reusable, 49 non-reusable and 26 unresolved**. Unresolved cases remain explicitly missing rather than being coerced into zero.

The judge changed the original C binary judgment on 1 reviewed items with a resolved outcome. Unresolved cases are a separate outcome, not included in that change count. Original A/B/C submissions and pre-adjudication statistics remain intact. Unselected unanimous items retain a provisional consensus label and are explicitly marked as not individually adjudicated. See JUDGE_REPORT.md for reasoning and PROVISIONAL_LABELS.jsonl for every item.

## What the team learned

The original semantic examples are easy for these same-model raters to agree on, but that does not establish a valid trajectory benchmark. Only 54/200 fields are literal prefixes of the final instruction; 88 are internal substrings and 58 are absent verbatim. No task has all four fields as literal cumulative prefixes. The internal snippets and counterfactual alternatives must not be silently treated as successive observed input states.

The third position is predominantly negative and the fourth is always positive across these label sets. This is a construction artifact worth testing explicitly, not a useful scientific result. Hide IDs and position metadata from downstream predictors, but also address the underlying templated semantic cues: hiding IDs alone cannot remove content-level shortcuts. Do not select or rewrite items to obtain favorable model comparisons.

The rubric also leaves broad retrieval coverage, unspecified draft content, the extent of material rewriting, soft preferences and conditional actions underdetermined. The judge reviewed uncertain agreements as well as disagreements so unanimity would not automatically become a resolved answer. Actual work products or more precise action semantics are needed to resolve some cases without inventing details. See METHODOLOGY_REVIEW.md for the independent critique.

## Isolation and limitations

All raters started with no conversation-history fork, received only the frozen rubric and separately shuffled inputs, and saw role-specific opaque IDs rather than original task/position IDs. Each was instructed not to inspect other results, the previous AI trial, mappings or owner key. Their methods state those boundaries were followed. This was workflow isolation on a shared filesystem, not a security-enforced access boundary. The coordinator had prior project context and earlier trial results, which were not passed to raters. Worked examples in the rubric remained visible.

Agents inherited the same configured model. Shared model biases and training data can produce correlated errors; distinct sessions do not establish independent human judgment or cross-model replication. Model service revisions were not independently pinned. Full instructions were co-visible in record displays, rather than mechanically revealed after prefix review. Rater C reports that compact recovery displays for C041–C150 omitted domain and execution_class; this deviation is preserved and limits comparisons. The later adjudication input included those fields but does not retroactively repair the initial procedure.

C first labeled blindly and then judged after seeing A/B/C rationales. It is separate from primary raters A/B but is not a fourth untouched adjudicator. Do not treat the judge as independent of its initial opinions or calculate post-adjudication agreement as if labels remained independent. Fractional utility and confidence are subjective judgments, not calibrated or measured outcomes. On unresolved adjudications, the judge confidence expresses confidence that evidence is insufficient, not confidence in a binary label. No owner-key comparison or human label comparison was performed.

## Gate decision and next step

The numerical 0.70 criterion is exceeded descriptively by each AI pair, but this does not satisfy the frozen human G1 process. No gate, thesis, endpoint, tolerance or model configuration was changed. These outputs are an AI annotation/review study. Keep them inaccessible to prospective blind human annotators before their submissions are preserved.

For the original gate, obtain independent human submissions and prescribed adjudication. Separately, use the team critique to prepare an explicit prospective construction/rubric addendum for genuinely cumulative input histories and sufficiently specified reusable work. Preserve the current pilot and all unresolved judgments. Do not silently replace the original items, waive G1, or authorize development/confirmatory extraction from these statistics.

## Evidence and checks

STUDY_PLAN.json fixes comparison and review rules before labels. FREEZE_MANIFEST.json hashes raw submissions, assigned inputs and rubric copies. INPUT_VALIDATION.json verifies all 600 assigned records against the original context and plan hashes. RATER_A/B/C.jsonl contain mapped labels; BLIND_ID_MAPPING.json permits auditing the mapping. No source context was rewritten.

ARITHMETIC_AUDIT.json independently verifies all pairwise and Fleiss calculations. It preserves two schema warnings: the existing two-rater checker uses A/B as generic slot names even in AC/BC results. PAIR_SLOT_MAPPING.json explicitly maps those slots to actual raters; numerical values are unchanged. Finalization checks every frozen raw file hash again.

The workbook is a review artifact: Items retains original context, Ratings preserves all 600 initial ratings, Judgments separates provisional decisions from initial votes, and Summary calculates counts and pairwise κ from those rows. Unresolved labels remain explicit. Native Numbers behavior is not independently validated by this export.

Recompute the archived agreement without model access or dependencies: `python3 outputs/g1_team_v0_1/recompute_agreement.py`. This read-only check also verifies raw frozen file hashes.
