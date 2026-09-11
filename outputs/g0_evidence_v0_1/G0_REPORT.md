# G0 instrumentation QA — v0.1 evidence report

**Gate: G0. Status: FAIL; progression BLOCKED.** The bounded Modal job completed. The frozen thesis and supplied protocol are unchanged. No confirmatory extraction, probe training, consequential action, or mitigation run occurred.

> Do not predict what the user will type next. Predict what work will not need to be undone.

## Evidence and results

Run: `run_20260911T163140Z`, [Modal application](https://modal.com/apps/jeff-34667/main/ap-UVuGxBXNlzIFx2IZZnLQwV). The first numerical experiment was sequence-length sensitivity, followed by the unmodified supplied harness and additive controls. All comparisons retained `atol=rtol=1e-5`.

| Check | Result | Maximum absolute difference |
|---|---|---:|
| Reconstructed length sensitivity | DIAGNOSTIC: 80/80 outside tolerance | 2.5 |
| Original exact repeat | PASS: 5/5 | 0 |
| Original batch vs singleton | FAIL: 20/20 | 3.0 |
| Original masked-token content change at fixed shape | PASS: 5/5 | 0 |
| Original model reload | PASS: 5/5 | 0 |
| Explicit vs implicit position IDs | PASS: 5/5 | 0 |
| Saved-state roundtrip | PASS: 5/5 | 0 |
| Finite hidden states | PASS: 5/5 | 0 |
| Tested causal suffix comparison | PASS: 5/5 | 0 |
| Incremental cache vs full-forward hidden states | FAIL: 5/5 | 2.0 |
| Incremental cache vs full-forward logits | FAIL: 1/1 | 0.25 |
| Fixed-width batch vs singleton | FAIL: 20/20 | 2.5 |
| Token alignment and right-padding masks | PASS: 4/4 items | n/a |

The original harness separately records five length checks as INFO. Their original classification is preserved. The wrapper records its 80 length checks as DIAGNOSTIC with explicit tolerance outcomes. Original harness exit code: 2; 15 PASS, 20 FAIL, 5 INFO. Supplemental numerical controls: 20 PASS, 26 FAIL; alignment checks are recorded separately. The Modal transport completed successfully, which does **not** mean G0 passed.

## Historical reproduction limits

The supplied README reports 24/80 historical length-extension failures but the ZIP contains no historical script, raw tensors, exact revisions, tolerance, GPU, or comparison grid. This run reproduces the **presence of sequence-length sensitivity**, not the exact historical experiment or failure rate. Its prospectively defined reconstruction uses eight supplied QA texts, lengths 64→96 and 64→128, and hidden-state tuple indices 1, 7, 14, 21, 28. The 80/80 result must not replace or be pooled with the reported 24/80.

## Unexpected findings and interpretation

Fixing sequence width to 96 did not eliminate batch-vs-singleton differences. Batch size still differs, so this is not a fully identical tensor-shape control. Cached incremental execution also differs from full-forward execution. These observations prevent attributing all discrepancies to padding content or assuming a fixed-width mitigation is sufficient.

PyTorch emitted CuBLAS determinism warnings: the inherited harness uses warn-only deterministic algorithms and does not set `CUBLAS_WORKSPACE_CONFIG`. The warnings are preserved in the logs. Passing repeat tests does not establish general determinism. The warning identifies a follow-up control, not a proven cause of the observed shape-dependent discrepancies. No tolerance has been widened and no claim is made that these errors are harmless to temporal features.

Controls are limited to eight synthetic QA texts and five probe layers; some supplemental controls use one utterance. The causal-suffix PASS applies to that tested construction only. This is instrumentation evidence, not a hypothesis test or comprehensive validation of all layers, suffixes, padding modes, kernels, or devices.

## Exact environment

- Model and tokenizer: `Qwen/Qwen2.5-7B-Instruct`, commit `a09a35458c702b33eeacc393d103063234e8bc28`.
- GPU: NVIDIA A10; BF16; SDPA; right padding; seed 1729; TF32 off.
- Python 3.11.12; PyTorch 2.5.1+cu124; Transformers 4.45.2; NumPy 1.26.4. Full dependency freeze and NVIDIA driver inventory are saved.
- Baseline cache disabled; supplemental incremental-cache test explicitly enabled. Implicit arange position IDs agree exactly with explicit positions in the tested batch.
- Wrapper model parameters require no gradients, model is in evaluation mode; original harness uses inference mode. No weights were updated.

## Preserved artifacts

`source/` contains the original harness, README, runbook, protocol, requirements, manifest, and wrapper code. All 11 source-package hashes matched the handoff manifest. `run_20260911T163140Z/` contains 32 tensor files plus raw logs, JSON reports, token IDs/masks/positions, checksums, resolved revision, and environment metadata. `modal_run_01.tar.gz` preserves the returned raw evidence archive. The remote volume `aeb-g0-evidence-v0-1` retains the run too.

The worker hashes finalized artifacts before closing its log; the live log is therefore excluded from that comparison. The final local manifest covers the completed log and the complete delivered bundle. Original harness comparisons retain the original JSON metrics and logs; raw tensors are retained for reconstructed length and supplemental forward passes, not every internal forward call of the unmodified harness.

Local sandbox authentication timeouts and an initial container-inspection CLI syntax error are preserved. Network-enabled authentication succeeded using the existing profile. These operational failures are distinct from numerical QA failures.

## Protocol impact and next allowed action

G0 is failed. G1 remains pending two independent annotations and subsequent adjudication; the owner gold key is not independent evidence and was not read as labels. Stage 1 and confirmatory execution remain blocked. The source protocol and thesis were not edited.

Next allowed work is a versioned G0 numerical investigation: recover the historical script/configuration if available; separately control the missing CuBLAS workspace setting, attention backend, precision and batch shape; rerun the same cases and retain every failed baseline. Changes must be isolated and documented before any claim of resolution. A pass requires complete required QA and evidence that residual numerical errors do not invalidate cross-prefix comparisons, not merely relaxing tolerances.

## Cost

One A10 container, no retries. Worker subprocess wall time: 399.22 seconds; observed container/app interval approximately 491 seconds including evidence packaging and return. At the [published Modal A10 rate](https://modal.com/pricing) of $0.000306/second, the latter corresponds to approximately **$0.15 GPU-only**. This is an estimate, not invoiced cost; CPU, memory, image build, storage, and billing adjustments are excluded. The actual billed total and account credit balance were not retrieved. No monetary cap was supplied. The job had a 1,650-second subprocess limit and 1,800-second function limit; it has completed and no further job is scheduled.
