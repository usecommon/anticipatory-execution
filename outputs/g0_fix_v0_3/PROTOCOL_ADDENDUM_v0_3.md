# G0 instrumentation amendment v0.3 — candidate validation only

Frozen thesis: Do not predict what the user will type next. Predict what work will not need to be undone.

The original protocol is preserved unchanged. This versioned implementation amendment investigates a constrained extraction path, motivated by the reproduced v0.1 failures and v0.2 RCA. It changes no scientific hypothesis, endpoint, data split, feature selection or numerical tolerance. No confirmatory extraction is allowed.

## Candidate contract

One NVIDIA A100-40GB; PyTorch 2.5.1; Transformers 4.45.2; pinned Qwen2.5-7B-Instruct model/tokenizer revision a09a35458c702b33eeacc393d103063234e8bc28. Frozen model in FP32 eager attention. Seed 1729, TF32 off, strict deterministic algorithms and CUBLAS_WORKSPACE_CONFIG=:4096:8. Physical input shape always [1,128]. Explicit arange positions and 4D additive causal/padding mask. No KV cache or reuse. Batch requests are implemented as ordered single-prefix calls.

The width is a global instrumentation constant, never derived from the full instruction or future suffix. Only contiguous right-padded inputs with 1..128 active tokens are supported. Oversize, empty, holey/left-padded, and cached requests raise errors; no silent truncation or fallback. Raw backend operations remain available only to the QA script, not through this extraction contract.

## Validation

Eight original QA texts. All 29 hidden-state tuple entries and all active-token logits checked for repeat, same-prefix input padding lengths, actual masked-content perturbation at model input, real causal suffix extensions, batch-interface ordering, serialization, reload, and completed-word prefix/full-token alignment. Mask/position/token alignment and finite-state checks included. Invalid-input rejection and active-input sensitivity guards included. Independent word-prefix tokenizations that do not align to the full sequence are logged as DIAGNOSTIC rather than falsely imposing equality.

Retain native physical length extension 8×2×5 = 80 comparisons, native batch-vs-singleton and actual cached-vs-full comparisons as separately reported real controls. Their failures are not reclassified as passes or hidden by the canonical adapter. The adapter's batch and input-padding checks validate normalization/contract enforcement; they do not prove physical batching or arbitrary-width kernels stable.

Original atol=rtol=1e-5 throughout; no tolerance relaxation. Canonical-path validation and the overall G0 gate are reported separately. A supported-contract PASS alone does not waive outstanding unrestricted/cache failures or constitute a complete research-stage authorization. G1 remains independent and unpassed.

## Evidence and bounds

One GPU job, no retries, 1,080-second worker and 1,200-second function limits. Reuse the existing pinned checkpoint volume. Every result and raw activation snapshot retained in new volume aeb-g0-fix-v0-3. Download a manifest, all metrics/logs, and representative raw tensors; remaining raw tensors stay in the volume and are addressable by manifest. No monetary cap supplied. No model training, automatic extraction or deployed service.
