# Public and synthetic data under a shared proposal policy

Completed a new development pilot using the same six-word checkpoint, prefix-only proposal instructions, preparation-sufficiency rule and AI review workflow on both sources. **300 task opportunities produced 87 work products: 58 reusable, 25 non-reusable and 4 unresolved. The remaining 213 opportunities abstained.** All 87 products were judged substantive. No negatives or failures were discarded; previous versions remain unchanged.

## Results

| Measure | BFCL public-source tasks | Synthetic task variants |
| --- | ---: | ---: |
| Task opportunities | 200 | 100 |
| Distinct six-word prefixes | 199 | 59 |
| Prefixes with proposals | 21 | 41 |
| Task opportunities with proposals | 21 (10.5%) | 66 (66.0%) |
| Abstentions | 179 | 34 |
| Reusable work | 15 | 43 |
| Non-reusable work | 4 | 21 |
| Unresolved reuse | 2 | 2 |
| Reusable / all opportunities | 7.5% | 43.0% |
| Reusable / proposed products | 71.4% | 65.2% |
| Ambiguity flags, overlapping labels | 9/21 | 21/66 |

The largest descriptive difference is proposal coverage at six words. Conditional on a proposal, the public sample does not show a lower reusable share. These are AI judgments of authored artifacts, not predictive accuracy, statistical source-effect estimates or evidence for the internal-state hypothesis. A sample with many abstentions can have high conditional reuse while offering few useful opportunities.

The policy produced one artifact per unique exact prefix. Thus 62 unique proposals expanded into 87 task-level work products; those 87 are not independent observations. Synthetic paired continuations can legitimately give different survival labels to the same prefix and work. No policy can identify an unseen branch from identical input alone. Synthetic branch frequencies and template structure are authored, not measured user behavior.

## What changed

The [versioned clarification](POLICY.md) asks first whether there is substantive work to evaluate, then whether it survives. An empty table, copied entity, intent restatement, generic checklist or list of unknown slots alone is insufficient. A concrete operation, calculation, operational query, parameterized algorithm with substantive logic, or meaningful draft can qualify without being a complete answer or executed result.

Absent meaningful work is a separate invalid-candidate disposition, not a negative survival label. Uncertain sufficiency is also separate. Neither occurred among these 87 proposed artifacts; the new proposal instructions screened out many lightweight preparations before review. This does not empirically validate every boundary case of the sufficiency rule. The original rubric is preserved, and a new human validation remains required.

Fresh proposer sessions received source-blinded prefix-only inputs. Fresh raters independently received separately shuffled products and full instructions, without source metadata or prior ratings. All 87 then received adjudication with both frozen ratings. A/B agreed on sufficiency 87/87 and full dispositions 82/87. Of 84 complete substantive binary pairs, 81 agreed (κ=0.9136); three pairs were outside that denominator. This is dependent-row AI agreement, not human G1. No repeated exact full-context products were adjudicated, so the empty exact-context inconsistency list does not demonstrate replicated consistency. Thirty final judgments retain ambiguity flags, including 26 resolved decisions, so four unresolved cases must not be interpreted as only four questionable cases.

Compared with the preceding BFCL pilot, the proposed-product count fell from 59 to 21 and unresolved judgments from 28 to 2 on public tasks. Both proposal selection and the measurement rule changed. These are not neutral remeasurements of the same 59 products, and the reduction cannot establish improved annotation reliability or predictive performance.

## What remains unmatched

The same checkpoint and proposal/review policy address the previous procedural mismatch. Domain weights, task distribution, semantic completeness at six words, source construction, model-session variation and template dependence remain different. [Proposer-session strata](PROPOSER_STRATA.json) preserve assignment-specific coverage and outcomes; session and batch-context variation remain possible despite identical instructions. Both sources are exposed development material, not unseen holdouts; public-source pretraining exposure is unknown. Proposers saw batches of 129 prefixes, so this is not a validated deterministic per-example policy.

A descriptive stratum restricted to the seven shared named domains contains 174 public tasks and 58 synthetic variants. It produces 20 and 32 candidate work products respectively, with 15 and 20 judged reusable. This retains the coverage difference, but does not equalize domain weights or semantic difficulty. The other 26 public and 42 synthetic opportunities remain in the full results; they are not silently excluded. Detailed domain counts are in SCORES.json. Broader public coverage and template-group admission remain pending.

## Files

- [Review all 300 opportunities and exact work products](results/REVIEW.md)
- [All machine-readable results](results/ALL_ITEMS.jsonl) and [source/domain scores](results/SCORES.json)
- [Reusable](results/REUSABLE.jsonl), [non-reusable](results/NON_REUSABLE.jsonl), [unresolved reuse](results/UNRESOLVED_REUSE.jsonl), [abstentions](results/ABSTENTION.jsonl)
- [Independent adapter audit](ADAPTER_AUDIT.md), [proposal audit](PROPOSAL_AUDIT.md), [final audit](FINAL_AUDIT.md)
- [Policy](POLICY.md), [proposer instructions](PROPOSER_INSTRUCTIONS.txt), [reviewer instructions](REVIEWER_INSTRUCTIONS.txt), [original rubric](ORIGINAL_RUBRIC.txt)
- [Generation provenance and limitations](AI_PROVENANCE.json), [failures](FAILURES.md), [rebuild check](REBUILD_CHECK.json)

Source hashes link all 200 public first-turn records and 100 synthetic tasks to the prior immutable versions. Original synthetic products and labels were not supplied to proposers or copied into the new labels. Source metadata, later text, tool inventories, reference paths and initial states remain outside proposer inputs. Reviewer metadata blinding cannot hide linguistic clues about provenance or prove absence of model memorization.

BFCL remains pinned at 6ea57973c7a6097fd7c5915698c54c17c5b1b6c8; [source attribution and license notice](../bfcl_public_pilot_v0_1/SOURCE_MANIFEST.json) and [admission qualifications](../bfcl_public_pilot_v0_1/SOURCE_ADMISSION.json) are inherited. The original source is publicly retrievable; the adapted research package is private, not a public release, and complete redistribution admission remains pending. Synthetic instructions are also private diagnostic material. Do not publish the repository wholesale or expose the owner gold key.

The builder reproduced six output files byte-for-byte in a fresh directory. Frozen inputs, raw proposals, raw ratings, mappings and final output hashes are preserved. Software transformations and saved-output scoring are reproducible; exact AI sampling reproduction is not established. Structural and final arithmetic audits used a prior BFCL adjudicator session after agent-capacity failures, with its prior exposure disclosed. It did not provide the new blind ratings.

Run offline integrity checks:

```sh
python3 outputs/shared_policy_pilot_v0_1/verify.py
```

To rebuild, use a fresh sibling-layout copy with sources listed in SOURCE_HASHES.json; build.py refuses existing outputs. prepare_review.py consumes the two preserved proposer submissions, prepare_adjudication.py the two preserved rater submissions, and finalize.py the preserved judge submission. Never overwrite this version's evidence. Hash inventories exclude Python bytecode caches.

## Next research step

Validate the preparation boundary with independent humans, including deliberately insufficient artifacts and flagged cases. Extend a prospectively declared common checkpoint schedule to both sources to assess when substantive opportunities emerge, retaining every checkpoint's abstentions and failures. Executable frozen tool fixtures are still needed before claiming actual saved work or latency. Dataset eligibility, template grouping, complete human G1 and development-length preflight remain pending.

The frozen thesis remains: **Do not predict what the user will type next. Predict what work will not need to be undone.** G0 is unchanged and scoped. No research-model inference, training, fixture execution, development/confirmatory extraction, internal-state comparison or latency-benefit measurement occurred. New data and labeling rules may change or reverse future results; no scientific endpoint was relaxed to obtain a favorable finding.
