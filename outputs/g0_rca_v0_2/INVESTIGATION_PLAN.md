# G0 root-cause investigation v0.2

Scope: instrument QA failures only. The frozen thesis, protocol source, seed, model/tokenizer revision and 1e-5 absolute/relative tolerances remain unchanged. No confirmatory extraction or training. v0.1 failure evidence remains intact.

The historical failure type was reproduced before this investigation. Exact historical 24/80 replay remains unavailable.

## Competing explanations and interventions

1. Missing CuBLAS determinism configuration: compare baseline against CUBLAS_WORKSPACE_CONFIG=:4096:8 with strict deterministic algorithms in a fresh process. This intervention fixes the determinism configuration as a pair; it does not isolate the workspace flag from warn-only policy.
2. Attention backend numerics: compare strict BF16 SDPA against strict BF16 eager and forced SDPA math separately.
3. BF16 reduced-precision GEMM accumulation: compare strict BF16 SDPA with that reduction disabled; retain all other settings.
4. Precision-related amplification: compare strict BF16 eager against strict FP32 eager on the same GPU. FP32 uses the same checkpoint, without training.
5. Mask, token, or serialization errors: baseline controls remain relevant; repeat and masked-content controls recur here. Trace embedding, first RMSNorm, Q/K/V projections, attention output, post-attention RMSNorm, MLP, first-block output and final norm for matched active tokens.
6. Isolated projection test: same first normalized input and Q-projection parameters, change only GEMM row count from 64 to 128; compare native dtype and FP32. This can establish a shape effect upstream of attention if observed.

## Design

One A100-40GB supports both BF16 and FP32. All six comparisons run sequentially in that same container, in fresh processes. The A100 baseline is a new hardware stratum; do not attribute an A10-to-A100 change to another flag. Model revision: a09a35458c702b33eeacc393d103063234e8bc28. Torch 2.5.1, Transformers 4.45.2, seed 1729, TF32 off. Two predetermined QA texts, padded 64 vs 128, singleton vs two-item batch at width 64, one predetermined incremental-cache case. Five original probe layers. These bounded diagnostic cases do not constitute a complete G0 rerun.

Cases: baseline; workspace_strict; bf16_eager; bf16_math; bf16_no_reduced; fp32_eager.

Failure localization uses all active positions; gate-style length/batch comparisons use last-active hidden states. Absolute, relative-L2 and unequal-element counts are recorded. Same-input repeat and fixed-shape masked-content controls test whether differences depend on shape rather than randomness or masked content. Hooks read tensors and do not modify outputs. Numerical controls with no feature/hypothesis evaluation.

## Evidence and compute

CPU job downloads the pinned public checkpoint to reusable Modal volume aeb-qwen-pinned-model-v0-2. One GPU container, no retries; each case capped at 200 seconds, total function capped at 1,500 seconds. All case failures, logs, activation snapshots, exact source and hashes are retained in aeb-g0-rca-v0-2 and downloaded. No monetary cap supplied; runtime and estimated resource costs will be reported, not represented as an invoice. No automatic subsequent extraction or deployed service.

## Interpretation rules

A warning disappearing is not proof of root-cause resolution. A configuration passing a few cases does not pass G0. Differences beginning before attention weaken a mask/attention-only explanation. Reduced errors in FP32 support a numerical mechanism but do not justify tolerance changes. Exact kernel/accumulation mechanisms require evidence beyond a high-level configuration switch.
