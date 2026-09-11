# G0 closure and research safeguards — v0.5

**G0 PASS only for the enforced canonical-v0.5 contract. G1 remains pending; Stage 1 and confirmatory extraction remain blocked.**

Implemented the hardened extractor and QA-only pipeline, then validated them in two independent Modal containers. The frozen thesis remains: **Do not predict what the user will type next. Predict what work will not need to be undone.** This is a versioned instrumentation correction. It is not evidence for the scientific hypotheses, a claim of product benefit, or a repair of the underlying native GPU kernels.

## Evidence and decision

| Run | Outcome | Checks | Actual forwards |
|---|---|---:|---:|
| closure_a_20260911T175740Z | PASS | 8,427 | 410 |
| closure_b_20260911T180521Z | BLOCKED: unvalidated hardware, before extraction | No numerical tests | 0 |
| closure_c_20260911T180932Z | PASS | 8,427 | 410 |

Each successful suite has 8,394 supported checks and 33 expected-rejection checks; 8,276 numerical comparisons are bitwise equal with maximum absolute difference zero. Tests cover 115 independently tokenized word prefixes from 12 new natural QA texts, two synthetic token families at ten lengths through 128, all 29 hidden-state entries and active logits, masked-content perturbations, serialized batch order, actual-call masks/positions/cache, the public saved-output pipeline, and the eight-case bridge to preserved v0.3 canonical states. Counts are QA assertions, not independent statistical samples or scientific effect estimates. Natural fixtures reach 25 tokens; long-boundary evidence comes from the two synthetic families, not broad long-form natural text coverage.

Independent local adjudication passed 1,092 checks with zero failures across 155 saved cases. Container IDs are distinct, contract IDs match, saved last states/logits are bitwise equal, and full active-state hidden/logit digests match. Downloaded evidence hashes verify. Actual runtime and source hashes are recorded; the source matches the pre-run manifest. The 115 individual pipeline tensor files per successful run remain on the Modal evidence volume, with recorded hashes and in-container serialization checks; they were not independently downloaded. Numerical tolerance remains atol=rtol=1e-5.

## What was fixed

The prior RCA demonstrated shape-dependent numerical differences starting in Q/K/V linear projections. FP32 alone did not make native variable shapes pass. The corrected path keeps physical shape [1,128] constant and processes prefixes serially using FP32 eager attention, explicit positions and causal/padding masks, no KV cache, TF32 or autocast, and strict deterministic settings. Model and tokenizer files are checked against a pinned upstream commit and rehashed on load. Parameters remain frozen.

The factory and entrypoint enforce this execution scope, reject malformed input before coercion, reject unsupported runtime settings, and preflight an entire job before inference. Overlength examples block the job without truncation, silent exclusion or a different execution fallback. Only QA partitions are enabled. Expected rejection tests pass when invalid requests produce no model forward.

Supported hardware is exactly NVIDIA A100-SXM4-40GB, torch 2.5.1+cu124 and Transformers 4.45.2. The contract ID is `95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0`. Other hardware, drivers/software changes, precision, attention backends, native batches, native variable widths, cache reuse and active lengths above 128 need separate validation. Historical native-mode failures retain their FAIL status.

## Preserved failures and scope of reproduction

The historical failure type was reproduced before mitigation: the v0.1 A10 reconstruction failed 80/80 length comparisons. This is not an exact replay of the reported historical 24/80 result, whose complete configuration/raw evidence was absent. The v0.2 RCA and v0.3 native controls remain intact, including residual FP32 native failures. No old failure was erased, relabeled or removed from the supported test set to manufacture a pass.

Closure attempt 01 failed in CPU orchestration because extractor was not on the remote import path; the import-only launcher correction is versioned. Attempt 02 closure_b rejected hardware before numerical extraction. Its exact allocated device was not captured, so its subtype/cause remains unknown. Attempt 03 added pre-worker allocation logging and ran one bounded replacement on the unchanged requested hardware and unchanged numerical source/fixtures. The guard was not relaxed. Both failed attempts, logs, original launchers and the earlier blocked adjudication are preserved. A successful Modal transport exit is not treated as scientific success.

## Numerical results may change

Changing precision, backend and execution shape can alter hidden states, logits, trajectory features, probe fits, calibration, layer rankings and the measured incremental benefit of internal dynamics. The QA bridge to v0.3 demonstrates local FP32 regression continuity; it does not establish BF16 equivalence or neutrality of downstream outcomes. Removing shape artifacts may reduce, eliminate or reverse an apparent advantage. Such a result must be reported, not tuned away.

Keep extraction versions separate. Once G0 and G1 permit authorized development work, regenerate affected B1/B2/M features under the same pinned configuration and refit affected development-only probes/calibrators. Do not pool incompatible features, reuse old calibration as if unchanged, compare different numerical configurations as an internal-information test, or tune to recover historical accuracy. H2, H3, endpoints, labels, splits and the frozen thesis stay unchanged. Product viability remains a separate question from internal-state scientific value.

Fixed-width FP32, serialized execution and no cache may worsen latency, compute and memory. Those costs must count in future matched-risk, matched-budget S1 comparisons. Current QA runtime is not a product latency measurement. See RESEARCH_SAFEGUARDS.md for the full policy.

## Next authorized boundary

No development or confirmatory extraction occurred. The executable remains QA-only. G1 requires independent annotation and its prescribed agreement/adjudication gate. Development benchmark length coverage remains unknown; before any later authorized development extraction, preflight all lengths. If 128 is insufficient, choose a new global width without outcome consultation and rerun G0 rather than selectively dropping long cases. No follow-on job is scheduled.

## Resource and evidence record

Successful worker times: 357.34s and 358.33s; maximum CUDA allocated memory: 28.67 GiB. Combined recorded subprocess intervals, including the rejected allocation, total 735.71s. Applying the requested A100-40GB rate of $0.000583/s gives roughly $0.429 GPU-only for those intervals; this is not metered billing and excludes startup, packaging, CPU, memory, upstream verification, storage and transfer. Actual total and account balance were not queried. Pricing source: https://modal.com/pricing .

Full remote evidence: Modal volume aeb-g0-closure-v0-5. Local run directories, archives, pre-run hashes, source, allocation metadata, checks and final adjudication are retained alongside this report. RUNBOOK.md explains the contract and reproduction procedure. The compact ZIP contains source and text/JSON evidence; large tensors and tar archives remain separate in this output directory and the Modal volume.
