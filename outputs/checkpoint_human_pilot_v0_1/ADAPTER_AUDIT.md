# Later-checkpoint adapter audit

Status: PASS for scheduled-opportunity accounting, checkpoint eligibility, literal prefix construction, proposer projection, and frozen-byte consistency. This is a structural audit, not proposal review or new human labeling.

## Exposure, timing, and scope

This reused auditor session previously adjudicated the older BFCL AI diagnostic and inspected source-visible shared-policy outputs. That exposure is disclosed and is appropriate only for this structural/provenance role, not a claim of fresh blinded labeling. This audit read PLAN.md, build.py, the input/source manifests, scheduled opportunities, prefix groups, proposer inputs/instructions, build QA, and the allowed evaluator source. The allowed old six-word opportunity file was read as bytes for hash verification, without inspecting its products. No work/checkpoint_proposer file, new proposal, prior rating, human response, gold file, or owner key was inspected for this audit.

The plan explicitly chooses 12- and 18-word checkpoints after the six-word coverage diagnostic and before new candidate generation/labels. This is a development amendment informed by prior results, not independent preregistration or evidence of a label-independent choice made before the six-word study. Its frozen bytes are verified; the manifest alone cannot independently timestamp planning or prove generation chronology. This audit does not use new labels to evaluate the plan.

The builder was inspected, not executed. Independent read-only assertions recomputed eligibility, all prefix strings, source correspondence, grouping, deterministic assignment, and manifest hashes. No source or pipeline input was modified; this report is the sole authored output. No fixture or candidate action ran and no external service was contacted.

## Scheduled opportunities and endpoint eligibility

The source retains all 300 task records: 200 public BFCL first-turn records and 100 synthetic task variants. Exactly one scheduled row exists for every task at each of 12 and 18 words, giving 600 unique opportunity IDs. Source/task identity, family, domain, and complete instruction match the allowed evaluator source exactly.

| Source | Checkpoint words | Scheduled | Eligible | Complete at checkpoint | Checkpoint not reached |
| --- | ---: | ---: | ---: | ---: | ---: |
| Public BFCL | 12 | 200 | 191 | 2 | 7 |
| Public BFCL | 18 | 200 | 166 | 4 | 30 |
| Synthetic | 12 | 100 | 86 | 7 | 7 |
| Synthetic | 18 | 100 | 33 | 6 | 61 |
| Total | — | 600 | 476 | 19 | 105 |

Thus 124 scheduled opportunities are ineligible: 19 messages end exactly at the checkpoint, and 105 end before it. All are preserved in SCHEDULED_OPPORTUNITIES.jsonl; none is replaced with an earlier prefix, sent for speculative proposal, or silently removed from scheduled counts.

Eligibility was recomputed using whitespace-delimited words independently of the stored status: eligible iff instruction length is strictly greater than k; complete_at_checkpoint iff equal to k; checkpoint_not_reached iff below k. All 476 eligible prefixes are literal initial substrings ending at the kth word, contain exactly k words, and are strictly shorter than their instructions. The 19 completed messages retain their literal k-word substring but have no prefix group and are not dispatched. The 105 unreached checkpoints have null prefix and null group.

## Exact-prefix groups and proposer inputs

The 476 eligible opportunities yield 473 distinct exact prefixes: 355 public and 118 synthetic. Group multiplicities are 470 singletons plus three pairs, accounting for all 476 eligible rows. Each eligible opportunity appears exactly once in its matching prefix group, and no ineligible opportunity appears in any group.

The two proposer shards contain 237 and 236 records. Their opaque IDs are disjoint, cover all 473 groups exactly once, and use the N### format. Each record has exactly two fields, item_id and prefix. Every prefix matches its group and source substring; every grouping opportunity list is exact. Independently reconstructing sorted prefixes, the documented shuffle seed 260913120, numbering, and alternating shard assignment reproduces the input files and mappings exactly. This is deterministic input assignment, not control of model sampling.

The proposer payload contains no explicit source, checkpoint number, source multiplicity, future continuation, total instruction length, task/family ID, state, reference path, old product, or prior label. The instructions prohibit other files and future context and retain the substantive-preparation requirement. The checkpoint-specific wording is adapted to observed instruction prefix. Unknown values may remain placeholders only where substantive work already exists.

Omission of a checkpoint-number field does not conceal the visible prefix word count: a proposer can count 12 or 18 words. Likewise, wording can suggest source or task type. All dispatched records are eligible, so eligibility is implicit in batch membership. The prepared input boundary is verified; actual live-session isolation or receipt cannot be established from these files alone. This audit does not inspect proposal outputs or verify later one-proposal-per-prefix output reuse.

## Frozen source availability and six-word preservation

Both allowed local source files are available and match SOURCE_HASHES.json. Their hashes also equal the values recorded during the earlier shared-policy audit:

- EVALUATOR_CONTEXT.jsonl: `08285eb9ac91974ce18317b78d553a6c853b46f365355d83ffa7151af4d7db8f`
- ALL_OPPORTUNITIES.jsonl: `a242f15fff08acf0d4e6b64b2f6fe2d5a63b2e2ad88fc2a50d3f8b45712ae4ef`

This establishes that the task source and frozen six-word opportunity/proposal baseline used by this adapter are unchanged from the prior audit. It is not a fresh comprehensive check of every older result or label file, which this audit did not inspect.

All ten entries in INPUT_FREEZE.json match current bytes, including the plan, builder, instructions, original rubric, scheduled rows, proposer shards, grouping, source manifest, and build QA. All twelve input/source manifest checks still pass after writing this report. The audit itself is outside the earlier freeze. Manifest equality establishes current byte consistency, not independent timestamping or authenticated provenance.

Availability here means the pinned local task snapshots are readable. It does not establish current upstream retrievability, licensing admission, public adaptation release, a complete future-dialogue fixture, or research-experiment eligibility. The public portion remains first-turn BFCL material; synthetic continuations retain their authored/private provenance. The plan correctly leaves public adaptation admission and research gates pending.

## Censoring and interpretation

Eligible opportunities fall from 277/300 at 12 words to 199/300 at 18 words. This change is source-dependent: public eligibility falls from 191/200 to 166/200, while synthetic eligibility falls from 86/100 to 33/100. Across both new checkpoints, eligibility is 357/400 public and 119/200 synthetic. Later-checkpoint samples therefore condition on instruction length and change the mix of available tasks before any proposal policy acts.

A complete or unreached endpoint is neither a proposer abstention nor evidence of non-reusable work. Scheduled, eligible, proposed, substantive, and resolved-label denominators must remain distinct in later reporting. Changes from six to twelve to eighteen words cannot by themselves isolate an information-timing benefit: they also change which instructions remain unfinished. Multiple checkpoints of a task and synthetic family members are dependent, and descriptive source/domain stratification does not remove that dependence or equalize available continuations.

The planned 200-case human sample, distinct-human collection, 20 separate boundary controls, package privacy, and downstream validation are future steps, not certified by this adapter check. No new human labels or G1 completion is established here.
