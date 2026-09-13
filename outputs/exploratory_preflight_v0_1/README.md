# Exploratory input and exact-tokenizer preflight — v0.1

Gate: exploratory input/length readiness. Status: **PASS for these frozen prefix inputs only**. Human G1 remains PENDING/DEFERRED under the temporary amendment. Model feature extraction has not run; confirmatory extraction remains prohibited. This is private AI-labeled diagnostic material, not a publicly admitted efficacy benchmark.

## Observed result

A CPU-only Modal worker tokenized all 4,013 distinct observed prefixes using the pinned Qwen2.5-7B-Instruct revision a09a35458c702b33eeacc393d103063234e8bc28, Transformers 4.45.2 and tokenizers 0.20.3. All fit the canonical 128-token width; maximum active length was **52**, overlength count **0**. The five tokenizer/config file hashes and serialized fast-tokenizer backend match the preserved G0 identity/contract. No truncation, whitespace normalization of extraction text, chat template, model load, GPU allocation or feature extraction occurred. This does not validate longer inputs, added candidate prompts or a new extraction entrypoint.

[Raw CPU result](run_20260913T000004720678Z/RESULT.json) and [Modal log](modal_attempt_01.log) preserve the run. Tokenizer work took approximately 1.99 seconds inside the worker, excluding image build/startup/transport. Resource limits: one CPU, 2 GiB memory, 300-second worker timeout, zero retries, one container. GPU cost is zero; CPU/build/other billed cost was not queried. No worker failures occurred. Initial web retrieval of Modal markdown documentation failed; the official HTML documentation was used successfully instead.

## Frozen coverage and partitions

The manifest retains all **900 scheduled opportunities** across **300 tasks**: 776 eligible (260 proposals and 516 abstentions), 19 already complete and 105 checkpoint-not-reached. It includes 4,656 task-word prefix observations through each task's last eligible 6/12/18-word checkpoint, deduplicated to 4,013 exact text inputs. Dense earlier prefixes support future temporal feature construction; no utility labels are invented for those positions.

The existing 200 main judgments remain unchanged: 171 reusable, 21 non-reusable, 8 unresolved. The other 60 proposed products remain unjudged by this fresh judge. All 20 boundary diagnostics stay in their original bundle, outside binary reuse targets. Neither abstentions nor missing labels are converted to negatives.

| Exploratory partition | Tasks | Reusable labels | Non-reusable labels | Unresolved labels |
|---|---:|---:|---:|---:|
| Fit | 194 | 105 | 15 | 7 |
| Tune | 53 | 36 | 4 | 1 |
| Check | 53 | 30 | 2 | 0 |

Assignment uses a fixed SHA256 rule without consulting labels. Connected components join source-qualified templates, normalized identical full instructions and identical eligible checkpoint prefixes. There are 249 components, largest size two tasks. All known task/family groups stay in one partition; scheduled checkpoint prefix overlap across partitions is zero. Exact/declared grouping does not certify the absence of all semantic near-duplicates.

There are 63 shared short-history input texts across partitions. These are label-free prefix states, not shared labeled prediction checkpoints; retain and disclose them. Any fitted transformation must use fit data only. This is an exploratory split of already exposed development material, not an untouched confirmatory test. With only two negative check labels, it cannot establish reliable low-risk speculation performance; no split was rerolled to improve its label distribution.

## Future-information and data boundaries

[EXTRACTION_INPUT.jsonl](EXTRACTION_INPUT.jsonl) contains only opaque content IDs and exact observed prefixes. It is the only text payload sent for tokenization. Full instructions, source metadata, split assignments, task mappings and all labels remain coordinator-side. Source full text is used to construct literal prefix boundaries and avoid duplicate-task split leakage, never as model input. Predictors must not use IDs as features.

[OPPORTUNITIES.jsonl](OPPORTUNITIES.jsonl) retains every denominator; [TRAJECTORY_MAPPING.jsonl](TRAJECTORY_MAPPING.jsonl) reconstructs ordered histories. [LABELS_COORDINATOR_ONLY.jsonl](LABELS_COORDINATOR_ONLY.jsonl) is a separate AI-label join. Candidate artifacts remain in the original frozen pool; this manifest defines prefix-state input, not a new action-generation or action-feature policy.

Public BFCL source identity was pinned in the earlier source pilot; adaptation/label redistribution and the synthetic release are still pending. This preflight does not waive the owner's public reproducibility requirement. Do not present the current public-versus-synthetic counts as a causal source comparison, drop negative cases, or treat these provisional labels as ground truth. Outcomes may change after human review or executable reuse checks.

## Verification and next boundary

`python3 outputs/exploratory_preflight_v0_1/verify.py` passed: source/input hash identity, complete opportunity coverage, group separation, exact literal trajectory alignment, prefix-only payload, unchanged labels, byte-identical manifest replay, split independence under label perturbation and completed exact-tokenizer preflight.

The frozen thesis, binary usefulness definition, H2/H3 endpoints and numerical contract remain unchanged. The preserved extractor is still QA-only. **Next: build and validate a versioned exploratory entrypoint that preserves the canonical forward path, rejects confirmatory inputs and checks this entire frozen input manifest before inference.** Do not relabel research inputs as QA to bypass the old guard. Any bounded GPU run needs a recorded run manifest/resource limit and technical readiness. Feature/probe comparisons remain exploratory, and human review is revisited after the first bounded comparison/sensitivity report, before confirmatory labeling or final protocol freeze.
