# Later checkpoints and blinded human-review packages

The 12- and 18-word proposal run is complete. It adds **173 task-level work products from 170 unique prefix proposals** to the frozen six-word pool, giving 260 reviewable products across 900 scheduled task/checkpoint opportunities. No new reuse labels were assigned. Two independent human-review packages are ready, each with **200 main cases plus 20 separate boundary checks**.

## Human review: the next action

Give each of two independent human reviewers only their assigned ZIP, not access to this repository:

- [Annotator A package](human_packages/Annotator_A.zip)
- [Annotator B package](human_packages/Annotator_B.zip)

Each reviewer extracts their ZIP, opens REVIEW.html in a browser, labels independently and exports their answers as JSON. They can save and reload draft exports. The packages contain no AI ratings, expected boundary labels, source metadata or coordinator mappings. Reviewers should not have seen prior item-level AI decisions. Source style can still suggest provenance; metadata blinding does not eliminate that possibility.

Both reviewers receive the same 220 cases in different orders. The main sample contains 100 public-source and 100 synthetic items from 169 distinct tasks; it is not 200 independent task families. Selection used a declared deterministic hash ranking, preferring distinct tasks and never consulting reuse labels. The 20 boundary checks are deliberately minimal authored artifacts and stay outside the main agreement denominator. Human labels remain blank; software QA fixtures are not human submissions.

The original 200-item G1 criterion applies to the main review set, not the 220-case package total. The clarified sufficiency rule is a developmental measurement change requiring human validation; this collection does not itself close G1 or replace the required independence/process review and third-party adjudication. See [coordinator instructions](COORDINATOR.md).

## Proposal coverage by checkpoint

| Source | Words observed | Eligible before completion | Work products proposed | Proposed / eligible |
| --- | ---: | ---: | ---: | ---: |
| BFCL | 6 | 200 | 21 | 10.5% |
| BFCL | 12 | 191 | 37 | 19.4% |
| BFCL | 18 | 166 | 66 | 39.8% |
| Synthetic | 6 | 100 | 66 | 66.0% |
| Synthetic | 12 | 86 | 45 | 52.3% |
| Synthetic | 18 | 33 | 25 | 75.8% |

Among the 600 later scheduled opportunities, 476 are before completion, 19 occur on the final word and 105 are never reached. All remain explicit. Across all 900 scheduled opportunities, 260 have proposals, 516 are abstentions and 124 are complete/unreached. Completed or unreached checkpoints are neither negative reuse labels nor policy abstentions.

BFCL shows more proposal coverage at the later checkpoints in this run. The synthetic pattern is not monotonic, and many synthetic instructions finish before 18 words. Eligibility uses eventual length only for evaluator-side bookkeeping; a deployed prefix-time policy cannot consult future length. Reported eligible-set rates do not describe the same population at every checkpoint. The six-word proposals are frozen from a previous batch, while later proposals were newly sampled; batch/session variability, domain mix and semantic completeness remain confounded with checkpoint comparisons. These are proposal-coverage measurements, not reusable-work rates, latency saved or scientific efficacy.

## Selection and blinding

The proposal pool contains 260 products. The deterministic 200-main-case selection is 100/source, with 65 cases at six words, 55 at 12 and 80 at 18. It represents 86 distinct public tasks and 83 distinct synthetic task variants, with repeated checkpoints where needed. All source/task/template/checkpoint lineage is retained in coordinator-only files. Related families and repeated contexts remain dependent; do not treat the 220 human judgments as 220 independent research observations.

Twenty boundary controls were created from a separate hash-ranked subset of the main cases: five copied prefixes, five empty tables, five unknown-slot lists and five generic checklists. They probe the new preparation-sufficiency boundary. They are not naturally proposed work, adversarial outcome labels or a way to inflate the negative prevalence. Their identities/types are coordinator-only; no expected labels are included in the reviewer packages.

The package payload allowlist is opaque item ID, prefix, candidate action, work product, declared execution class, completed instruction and unexecuted-fixture contract. Each ZIP contains only REVIEW.html, ITEMS.json, ORIGINAL_RUBRIC.txt and START_HERE.md. No owner gold key was accessed. Do not send the whole research repository to annotators.

## Verification and limitations

Independent [adapter](ADAPTER_AUDIT.md), [selection/package](COLLECTION_AUDIT.md) and [collector](COLLECTOR_REVIEW.md) reviews passed. Rebuilding reproduced six adapter files and fourteen package/mapping files byte-for-byte. Frozen inputs, raw proposals, selections, mappings and ZIP hashes are retained. Source and AI-generation qualifications are recorded in [AI_PROVENANCE.json](AI_PROVENANCE.json). Exact model sampling is not reproducible from the available configuration; deterministic transformations and saved-output handling are reproducible.

**Real-browser rendering remains unverified in this environment.** Chromium was blocked by the sandbox before loading the page. Actual form JavaScript passed a minimal DOM harness for blank initialization, disabled reuse on insufficient artifacts, stale-label clearing, uncertainty handling, export/import, draft persistence and navigation. This does not verify native browser downloads, real local-storage behavior or visual layout. Keep manual JSON exports as backups. Browser failures and the alternative test scope are preserved under software_qa.

The collection checker preserves originals before parsing, rejects invalid or incomplete exports, separates unknowns and sufficiency failures from negative labels, and keeps the 20 controls out of the main kappa. Two malformed-input crashes were found and fixed; earlier versions and fix logs are retained. All tests used clearly synthetic software fixtures, never genuine human submissions. Even a complete, nondegenerate main kappa>=0.70 leaves G1 pending until actual independence, all fields, adjudication and the process are reviewed.

Run offline integrity checks:

```sh
python3 outputs/checkpoint_human_pilot_v0_1/verify.py
```

No completed human responses are present. No new AI reuse adjudication, model training, research-model inference, fixture execution, development/confirmatory extraction or latency measurement occurred. G0 remains scoped and G1 remains pending. Public-source admission and a separate safe public release remain incomplete; the adapted data and synthetic material are still private. The frozen thesis and H2/H3 endpoints are unchanged.
