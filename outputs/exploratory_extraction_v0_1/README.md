# First bounded exploratory extraction — v0.1

Status: **PASS_SCOPED — complete extraction and independent saved-tensor verification passed.** Scope: private, AI-labeled exploratory diagnostic inputs only. Human G1 remains pending/deferred; confirmatory extraction is prohibited. This run extracts frozen model states, not evidence of H2/H3 or product benefit.

## Frozen run

All 4,013 distinct prefixes from the outcome-independent manifest are processed through the byte-identical validated exploratory entrypoint and canonical-v0.5 extractor. They represent 4,656 task-word observations across 300 tasks; the coordinator preserves all 900 scheduled opportunities separately. No source identity, task metadata, labels, full instruction, candidate artifact or split assignment is passed as a model input. Model weights are frozen. Each prefix is independently tokenized and checked against the pinned CPU preflight before the first forward.

The numerical contract remains 95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0: exact A100-SXM4-40GB, FP32/eager, physical [1,128], serial prefixes, explicit positions/masks, no cache, TF32 or autocast. The manifest maximum active length is 52. No truncation, exclusions, width changes or precision changes are permitted.

The saved data include 29 last-position hidden vectors (embedding/layer output entries), complete final next-token logits, input token IDs, padding mask, position IDs, active length and contract identity. These are shared numerical source material for later B1/B2/M work. This is not yet a complete implementation of the strong B1 baseline or trajectory feature suite. In particular, last-position logits at completed-word checkpoints do not provide every token-position surprisal, argument-completeness signal or action-conditioned observable. Do not claim H2 against a weakened baseline using only whichever outputs are convenient.

## Bounded resources and evidence

One A100-40GB GPU worker, two CPUs, 48 GiB host memory, no retries. The subprocess deadline is 2,100 seconds (35 minutes), with a 2,400-second outer function cap for final evidence preservation. A read-only, separate CPU verifier uses two CPUs, 8 GiB and a 1,200-second cap. Model volume is read-only. Raw tensor files remain in Modal volume aeb-exploratory-extraction-v0-1 under the unique run label. No large tensors or model weights are added to Git. Actual billing is not yet queried; configured bounds and elapsed times are reported separately from dollar cost.

Every completed prefix has a tensor SHA256 and a progress record. The success manifest appears only after the whole job completes. Failed runs retain partial tensors, progress, subprocess logs, failure/exit records and hashes; a failed partial run must never be used as a completed dataset. Each launcher invocation creates a new unique run directory. A process timeout remains a failure, never a reason to silently reduce the dataset.

The separate CPU worker checks every tensor SHA256, key set, shape, float32 dtype, finiteness, token IDs, canonical padding mask and position IDs against the pinned manifest/preflight. It also checks full coverage and forward audit records. This verifies stored artifacts, not fresh model reproducibility; G0 and the prior entrypoint bridge supply the scoped numerical regression evidence.

## Scientific and data limitations

Labels remain the single AI judge's 171 reusable, 21 non-reusable and 8 unresolved judgments for 200 main cases, with 53 ambiguity flags; the remaining 60 proposed artifacts have no fresh judge labels. All negatives, unknowns, abstentions and controls remain in their original records. No label or case is removed by extracting deduplicated prefixes. The exploratory check split has only two negative labels and does not support a reliable low-risk speculation estimate.

Public source versions were recorded earlier, but adaptation/label redistribution and synthetic release admission remain pending. These are private diagnostic inputs, not a certified publicly reproducible thesis benchmark. Human agreement would not by itself establish validity; actual reuse evidence and sensitivity to disputed labels remain necessary. Outcomes may change or reverse after measurement changes.

No probe is fitted, no threshold selected and no hypothesis tested in this extraction. The next step after verification is to freeze a bounded feature/comparison and label-sensitivity plan that preserves the strong B1 and B2 comparisons, uses fit-only transformations and keeps scientific claims exploratory. Human review must be revisited after the first bounded comparison/sensitivity report, before confirmatory labeling/freeze.

## Coverage audit for the next comparison

[FEATURE_COVERAGE.md](FEATURE_COVERAGE.md) maps the frozen B0/B1/B2/M requirements to these saved outputs. It records missing observables and leakage restrictions before any fitted comparison. Complete extraction is not equivalent to a complete strong baseline or a tested scientific hypothesis.

## Verification recovery and transport findings

The initial serial CPU audit was stopped incomplete after roughly 14 minutes and a 2,000-file milestone because it projected beyond its configured bound. Modal restarted that verifier invocation; the client/app was then interrupted and confirmed aborted. The subsequent 500-file milestone is not counted as a completed audit. GPU extraction had already completed and was not rerun.

A separately recorded recovery plan partitions the unchanged tensor manifest into four disjoint ranges, with up to four CPU containers (two CPUs and 8 GiB each, 600-second limits, no user-code retries). Each file is read once into bytes, hashed, then loaded from those same bytes with weights_only=True. All 19 original assertion expressions remain present, with an additional shard-bound check. [Criteria audit](RECOVERY_CRITERIA_AUDIT.json) and [recovery plan](VERIFICATION_RECOVERY_PLAN.json) preserve the change. Completion requires all four ranges and exact coverage of 4,013 unique IDs. Unclosed SDK connection warnings are retained in the recovery log; they do not replace the required completed results.

The returned text copy of worker.log normalized progress carriage returns and therefore differed from its original byte hash. The exact raw log was separately downloaded, matched to the original inventory, and shown to normalize to the initially returned copy. Both copies and the transport check are preserved. Tensor and JSON evidence were unchanged. See [failure/transport record](FAILURES.md).

## Completed result

- 4,013 saved outputs and exactly 4,013 model forwards, all under the same canonical-v0.5 contract. No missing or extra prefix outputs.
- 4,129,834,482 raw tensor bytes (about 4.13 GB decimal), kept on Modal rather than Git.
- Every tensor passed independent hash, shape, dtype, finiteness, token, mask and position checks. Seven completed disjoint CPU ranges cover the entire manifest; incomplete or timed-out attempts contribute no accepted coverage.
- GPU subprocess elapsed 1,399.10 seconds (about 23.3 minutes); worker-recorded interval 1,394.99 seconds. Peak CUDA allocated memory 30,783,937,024 bytes. These intervals exclude outer image startup/final volume commit and CPU verification; they are not product latency or billed cost.
- The final tail recovery's longest successful worker interval was 56.54 seconds, excluding the earlier completed ranges and all failed/interrupted verification work. All attempts and configured limits remain reported; no metered dollar total was queried.
- The local verifier passed exact source/input pins, full input/manifest/progress/audit coverage, returned JSON hashes, raw-log identity, retained-report hashes and merged CPU evidence. Original imported research files still pass the 227-file integrity check.

[Extraction evidence](run_20260913T003027625834Z/EXTRACTION_RESULT.json) · [Merged independent verification](run_20260913T003027625834Z/VERIFICATION.json) · [Exact raw log](run_20260913T003027625834Z/worker_raw.log).

Remote raw tensors: volume `aeb-exploratory-extraction-v0-1`, path `run_20260913T003027625834Z/extraction/`. All tensors were reread and checked by separate CPU containers; only the raw log and text/JSON evidence were downloaded locally. This is storage integrity and scoped instrumentation evidence, not an independent rerun of the model or support for H2/H3.

**Next allowed step:** freeze the observable/snapshot/dynamics feature and label-sensitivity plan, resolve the strong-B1 coverage gaps documented above, and then perform a bounded exploratory probe comparison using the existing grouped development partitions. Keep human G1 pending/deferred and public release/adaptation admission pending. Confirmatory extraction remains prohibited.
