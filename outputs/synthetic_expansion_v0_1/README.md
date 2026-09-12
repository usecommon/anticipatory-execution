# Synthetic expansion review results

The 200 new items received two separately ordered AI ratings and an all-item AI adjudication. The final provisional distribution is **136 reusable, 59 non-reusable and 5 unresolved**. Nineteen items retain ambiguity flags. These are judgments of fictional stipulated artifacts, not measured predictions by the frozen research model.

## Dataset and source plan

The expansion contains 100 full-instruction variants in 50 related families across 12 domains, with 1,677 completed-word observations. Two candidate work products at one shared prefix per variant supply the 200 review items. It extends the style of 50 selected actions from the 125 accepted-positive anchor pool. Original owner decisions are unchanged.

The [public-plus-synthetic plan](STUDY_PLAN.md) targets at least 1,500 public-source tasks within the unchanged 3,000-task benchmark. BFCL is the first executable adapter, SGD supplies breadth, and ToolSandbox supplies dependency stress cases. Exact source quotas and splits remain unimplemented. All descendants of a task/template—including synthetic variants inspired by it—must stay grouped. These exposed 50 families cannot become an untouched confirmatory holdout.

## Rescoring

| Stage | Reusable | Non-reusable | Unresolved |
|---|---:|---:|---:|
| Author construction expectations | 150 | 50 | 0 |
| AI rater A | 138 | 61 | 1 |
| AI rater B | 139 | 60 | 1 |
| AI adjudication | 136 | 59 | 5 |

A/B agree on 198 of 199 complete binary pairs (99.50%; Cohen’s κ = 0.9881). One pair is unresolved by both and is explicitly outside the binary denominator. High agreement does not establish independent-human reliability or a human G1 pass. The judge saw both ratings and is not an independent third rater.

The final judge differs from 13 of 195 resolved author expectations and leaves five others unresolved. Eleven expected positives became non-reusable, and two expected negatives became reusable. The 182/195 consistency rate is a comparison to an authored branch heuristic, not predictive accuracy. No model performance improvement or internal-state advantage has been measured.

## Cases still unresolved

| Item | Candidate | Why unresolved |
|---|---|---|
| [SX1-F024-K-A2](results/ALL_ITEMS_REVIEW.md#sx1-f024-k-a2) | Calculate Acme revenue growth | The growth result is excluded, and this item does not establish the operands as company-stated actual revenue with units and year mapping; neither their reportability nor salvage materiality is settled. |
| [SX1-F031-K-A1](results/ALL_ITEMS_REVIEW.md#sx1-f031-k-a1) | Stage an ERROR-counting function | The item supplies no log format establishing that ERROR lines start with ERROR plus a space, so correctness and required predicate revision remain unresolved. |
| [SX1-F032-K-A2](results/ALL_ITEMS_REVIEW.md#sx1-f032-k-a2) | Stage a ten-second timeout patch | The patch contains the old five-second constant but no location metadata; the rubric does not settle whether salvaging that observation while discarding the edit avoids material reexecution. |
| [SX1-F040-K-A1](results/ALL_ITEMS_REVIEW.md#sx1-f040-k-a1) | Stage the 70 F setting | The current thermostat setting is absent from this item, so the condition permitting any 70 F plan is unresolved and surviving utility cannot be quantified. |
| [SX1-F041-K-A2](results/ALL_ITEMS_REVIEW.md#sx1-f041-k-a2) | Stage a departure trigger definition | The departure trigger content fits, but no prior sensor check is supplied; compliance with checking before staging anything and the resulting need to redo staging remain unresolved. |

The judge also retains ambiguity on some ancillary preparation and materiality decisions that received binary labels. [Review all 200 items](results/ALL_ITEMS_REVIEW.md), including exact prefix, full instruction, work product and each rating. Machine-readable subsets: [review attention](results/REVIEW_ATTENTION.jsonl) and [changes from author expectations](results/CHANGED_FROM_AUTHOR_EXPECTATIONS.jsonl).

## What the review found

Concrete work products make many decisions clearer, but do not remove the need to specify conditional state, permitted workflow and the unit of reuse. Five cases need a prospective rubric or fixture clarification before a firm label is justified. Do not fill missing facts from neighboring items or silently treat unresolved as non-reusable.

Some early assumptions were deliberately preserved: an event on the wrong day, a patch when inspection was requested, and scope-specific templates under later changes. These are candidate-quality issues distinct from whether their work survives. The two initially negative cases that became reusable show that a goal change need not destroy a useful observation or comparison.

Fractional utility is a qualitative annotation of surviving content. It is not a measured fraction of compute, latency saved, probability of correctness or an experimentally calibrated quantity. Small textual edits can change substantive semantics; the materiality rule still requires independent-human validation.

## Scope and limitations

This is a controlled, AI-authored development stress set with many explicit exclusions and synthetic branch cues. Paired futures share identical prefixes and actions; a deterministic frozen model cannot know which unseen branch is chosen. Branch probabilities are construction choices rather than measured user behavior. Treating all 200 rows as independent observations would overstate the sample size.

Only the anchor positions have candidate work products; the remaining word positions are unannotated, not automatic negatives or abstentions. No executable proposer, retrieval coverage, actual artifact generation, output oracle, typing-time model or latency measurement has been validated. Source diversity and changed label specificity can change or reverse later results.

G0 remains scoped. G1 remains pending with zero independent-human pairs. No frozen research-model inference, development extraction or confirmatory extraction ran. AI annotation and adjudication were performed. No old annotation, source file, tolerance or hypothesis was overwritten.

This material has been saved to the existing private repository. **It is not publicly released or experiment-eligible under the public-data requirement.** A separate public dataset release must exclude the owner gold key and respect the human annotation blinding process. The public source adapters and complete benchmark remain future work.

## Files and reproduction

- [Input freeze](INPUT_FREEZE.json), [structural QA](INDEPENDENT_STRUCTURE_CHECK.json) and [scores](results/SCORES.json) record this release.
- [Construction failures](CONSTRUCTION_FAILURES.md) and PRESERVED_CONSTRUCTION_DRAFTS.zip retain the failed JSON and superseded prefix version.
- dataset/ITEMS.jsonl contains the 200 new items; dataset/STYLE_LINEAGE.jsonl records private style-anchor links without transferring labels.
- review/ retains both raw frozen submissions, mappings and the judge input; results/ retains the judge submission and final decisions.
- build.py rebuilds into a new empty directory; prepare_judging.py freezes two submissions; rescore.py checks frozen inputs and writes into a new results directory. Existing outputs are not overwritten.

Builder reproduction produced byte-identical generated files. Character-walk verification independently checked all 100 word-prefix sequences and both actions across all 50 matched future pairs. Every reviewed anchor appears in the all-word schedule. Field/ID validation and an independent arithmetic audit are recorded separately.
