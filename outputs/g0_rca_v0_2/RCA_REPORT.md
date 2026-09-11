# G0 failure root-cause analysis — v0.2

**Gate: G0. Status: FAIL; progression BLOCKED. RCA experiments completed.**

The demonstrated mechanism is **shape-dependent numerical computation in BF16 linear projections, followed by differences through the transformer**. Identical active inputs first diverge in the first Q/K/V projections, before attention masking. An isolated Q projection reproduces the full-model discrepancy when only the number of matrix rows changes. Strict determinism does not remove it. FP32 sharply reduces the error but does not pass the unchanged tolerance across the model.

This is an instrumentation failure, not evidence against or for the frozen scientific thesis. The thesis, weights, protocol source, and `atol=rtol=1e-5` remain unchanged. No confirmatory extraction or training occurred.

## Evidence establishing the mechanism

1. **The original evidence is intact.** An independent local reader verified 160 state checksums from the A10 length experiment. Active token IDs match across tensor lengths. The observed final-layer relative L2 differences range from 1.02% to 1.64% of the reference vector norm. This does not quantify their effect on future temporal features.
2. **The first divergence is upstream of attention.** In the new A100 baseline, embeddings and the first RMSNorm outputs are bitwise identical for the matched prefix. The first Q projection differs at 33 of 32,256 active coordinates, with maximum absolute difference 0.015625. K and V also differ. The trace localizes both length and batch discrepancies to these projections before attention consumes the mask.
3. **The isolated operation reproduces the model.** With the same normalized input, Q-projection weights and bias, appending independent zero rows changes native BF16 projection results. The isolated outputs exactly match the respective captured full-model Q outputs for both shapes. Attention, position IDs, cache state, and later layers are absent from this experiment.
4. **The missing determinism setting is not a sufficient explanation.** `CUBLAS_WORKSPACE_CONFIG=:4096:8` plus strict deterministic algorithms removes the two CuBLAS warnings. It leaves the measured comparison metrics unchanged from the A100 baseline. A raw-state audit also finds exact equality between baseline and strict states for the inspected forward pass. Repeats are exact in every configuration.
5. **Precision is a major contributor, but not a complete fix.** The isolated FP32 Q projection passes the existing tolerance; its maximum shape difference is approximately 1.53e-5 in the BF16-input microtest. PASS uses both absolute and relative terms, not the maximum absolute value alone. The full FP32 eager model reduces the maximum length difference from 16 under BF16 eager to 0.00018692, yet 8/10 length comparisons still fail. These are paired configurations on the same GPU and checkpoint.

The direct projection experiment proves a numerical shape effect independent of attention logic. The exact cuBLAS kernel, accumulation order, and rounding operation responsible were not profiled. “Floating-point/GEMM path sensitivity” is supported; attributing it to one particular GPU instruction or claiming it is merely final BF16 rounding would exceed the evidence. Native BF16 outputs also differ from simply rounding the separately computed FP32 reference at some coordinates.

## Controlled comparison matrix

All six cases ran sequentially in fresh processes on the same NVIDIA A100-SXM4-40GB. Two predetermined QA texts × five probe layers give ten length comparisons and ten batch comparisons per case. One cache test contributes five hidden-state and one logits comparison. Values below are maximum absolute differences over the relevant comparisons; cache maxima combine hidden states and logits and are not a common physical scale.

| Configuration | Length failures | Max length difference | Batch failures | Cache failures | Max cache difference |
|---|---:|---:|---:|---:|---:|
| BF16 SDPA baseline | 10/10 | 2 | 10/10 | 6/6 | 3.4375 |
| BF16 SDPA + strict determinism | 10/10 | 2 | 10/10 | 6/6 | 3.4375 |
| BF16 eager + strict determinism | 10/10 | 16 | 10/10 | 6/6 | 13.5 |
| BF16 forced SDPA math + strict determinism | 10/10 | 4.5 | 10/10 | 6/6 | 1.75 |
| BF16 SDPA, reduced-precision reduction off + strict determinism | 10/10 | 1 | 10/10 | 6/6 | 3.5 |
| FP32 eager + strict determinism | 8/10 | 0.0001869202 | 8/10 | 3/6 | 0.0001983643 |

All six cases pass all five repeat and five fixed-shape masked-content controls exactly. Changing attention implementation affects the magnitude substantially but does not eliminate the upstream projection discrepancy. Disabling reduced-precision BF16 GEMM accumulation also leaves the isolated Q-projection discrepancy and all gate-style BF16 failures.

FP32 residual errors remain shape-dependent. Its final-layer length relative L2 differences are approximately 1.75e-6 and 1.97e-6 on the two texts. These much smaller vector-level errors can still exceed the elementwise tolerance on some coordinates. Neither this observation nor the precision improvement authorizes changing tolerance.

The batch and length results in this diagnostic design are not independent replications: both can change the effective row count of linear operations from 64 to 128. Their identical measurements are consistent with a common matrix-shape mechanism, not additional independent statistical evidence.

## Contributing process defects

- The supplied harness enables deterministic algorithms with `warn_only=True` while leaving the CuBLAS workspace setting unset. This permits known determinism warnings to continue. Correcting that configuration is appropriate, but was experimentally insufficient to resolve the observed failures.
- Repeatability at a fixed shape was being treated as potentially sufficient for cross-prefix comparability. The results distinguish these properties: exact repeats coexist with shape-dependent states.
- The original harness treats length deviations as INFO and omits several required controls. Its PASS alone would not establish the stronger G0 requirement in the README/protocol. The original run already failed batch equivalence; no original result has been relabeled as a pass.

These are instrumentation/validation issues. The evidence does not establish suffix leakage, a token-indexing bug, model training, or corrupted serialization as the cause of the demonstrated projection discrepancy. The tested controls narrow those explanations; they do not rule out every unrelated implementation bug in untested cases.

## Next allowed action

Develop and validate a versioned canonical extraction path: fixed batch size, a predetermined padded width independent of the unseen suffix, explicit position IDs, strict determinism, and no incremental-cache substitution. If batching is offered at the interface, evaluate routing requests through the same canonical numerical path rather than changing matrix shapes. Use FP32 as a comparison reference, not as a declared cure.

Then rerun the complete G0 suite, including the preserved failure cases, and assess whether numerical differences can confound the planned temporal/cross-layer measurements. Predetermined width must not use final instruction length or truncate unlogged cases. Any extraction-policy change needs documented versioning and validated operational limits. These are proposed remediations; this RCA did not implement or validate them.

G0 remains FAIL. G1 remains a separate pending independent-annotation gate. Stage 1 and confirmatory extraction remain blocked. The historical 24/80 experiment still cannot be replayed exactly because its code/configuration and raw evidence were not supplied; v0.1 reproduced the failure type before v0.2 interventions.

## Reproducibility and evidence

Run `rca_20260911T165054Z`, [Modal application](https://modal.com/apps/jeff-34667/main/ap-9MReGpOBkBqsflun45Ztqi).

Model/tokenizer revision: `a09a35458c702b33eeacc393d103063234e8bc28`. PyTorch 2.5.1+cu124, Transformers 4.45.2, seed 1729, TF32 disabled. Driver 580.95.05; GPU NVIDIA A100-SXM4-40GB. The inspected first checkpoint shard declares BF16 tensors. Model configuration, full installed dependency listing, each case's environment, exact Qwen implementation source, activation snapshots, and all failed comparisons are saved.

Files alongside this report:

- `comparison_summary.json` and `all_comparisons.json`: per-configuration results and every individual measurement.
- `independent_rca_audit.json`: raw-data checks proving identical inputs and that the isolated projection reproduces the in-model outputs.
- `baseline_tensor_audit.json`: original A10 checksum and relative-error audit.
- `rca_20260911T165054Z/`: complete raw outputs, tensors, environment records, logs and hashes.
- `rca_run_01.tar.gz`: downloaded raw evidence archive.
- `source/` and `INVESTIGATION_PLAN.md`: versioned code and pre-result comparison plan.

All files in the remote run's final manifest verified after download. Raw evidence remains in Modal volume `aeb-g0-rca-v0-2`; the pinned checkpoint cache remains in `aeb-qwen-pinned-model-v0-2`. A late read-only packaging inspection found the GPU container already finished; that operational diagnostic is preserved and is not a numerical failure.

This is a bounded two-text RCA on one A100, not a complete G0 rerun or exact A10 reproduction. Hardware was held constant across the six interventions. The earlier A10 result is reported separately. The root-cause mechanism is established for the tested length/batch projection cases; no claim is made that it uniquely accounts for every later-layer or cache discrepancy.

## Cost

All six processes completed without retries or execution exceptions. Experiment phase: 191.76 seconds, including case transitions and evidence commits. At the [published Modal A100-40GB rate](https://modal.com/pricing) of $0.000583/second, that phase corresponds to approximately $0.112 GPU-only. Using the entire 422-second interval from GPU-function start to local completion gives a conservative approximately $0.246 GPU-only estimate; this interval includes packaging and transfer and is not a metered billing record. CPU, 48-GiB memory allocation, checkpoint preparation, storage and other billing adjustments are excluded. Actual invoice total and account credit balance were not retrieved. No monetary cap was supplied. The 1,500-second GPU-function limit was not reached; no further job is scheduled.

## Primary technical sources

The observations above come from saved experiments. The following version-matched primary sources explain why strict repeatability does not imply shape invariance and identify the controls tested:

- [PyTorch 2.5.1 numerical accuracy](https://raw.githubusercontent.com/pytorch/pytorch/v2.5.1/docs/source/notes/numerical_accuracy.rst): floating-point computation can differ across batching/slicing; BF16 accumulation and SDPA backends have distinct numerical behavior.
- [PyTorch 2.5.1 reproducibility](https://raw.githubusercontent.com/pytorch/pytorch/v2.5.1/docs/source/notes/randomness.rst): deterministic-algorithm controls and the CuBLAS workspace requirement.
- [Transformers 4.45.2 Qwen implementation](https://raw.githubusercontent.com/huggingface/transformers/v4.45.2/src/transformers/models/qwen2/modeling_qwen2.py): inspected projection, attention, normalization, cache and position computations. The executed source is also captured in each case directory.
