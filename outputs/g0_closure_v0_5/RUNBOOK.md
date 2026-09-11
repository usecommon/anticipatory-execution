# Canonical G0 instrumentation v0.5 runbook

This is the QA-only research measurement path. See RESEARCH_SAFEGUARDS.md before using its outputs. Frozen thesis and protocol are unchanged; execution configuration is versioned and numerical neutrality is not claimed.

## Supported contract

Qwen/Qwen2.5-7B-Instruct commit a09a35458c702b33eeacc393d103063234e8bc28; NVIDIA A100-SXM4-40GB; torch 2.5.1+cu124; Transformers 4.45.2; FP32 eager; one-prefix physical shape [1,128]; active length 1..128; explicit positions and causal/padding mask; no cache, TF32 or autocast; strict deterministic algorithms; CUBLAS_WORKSPACE_CONFIG=:4096:8 before CUDA initialization. All files and extraction contract are hashed. The actual driver/runtime is recorded in each successful run; software or driver changes require revalidation rather than an assumed equivalence.

## Invocation and preservation

Use source/modal_closure_v0_5_2.py as the latest orchestration example. It mounts the checkpoint and prior evidence read-only and runs a new single-use container with allocation logging. Its default closure_c label has already been reserved for this task: before a future authorized QA run, create a versioned launcher with a new label and output location, hash it and document the change. Do not overwrite existing archives or rerun research partitions. The supplied launchers resolve source files relative to themselves and output paths relative to the task working directory.

The latest launcher reads outputs/g0_closure_v0_5/checkpoint_identity.json, whose 11 files were verified against upstream commit identities. Every extractor load hashes the actual checkpoint/tokenizer files against it again. Upstream identity-verification code is retained in the launcher. CPU image/dependency setup and authenticated Modal CLI are required.

The only supported public construction is load_extractor(model_dir, manifest); use pipeline.run_prefix_job for QA jobs with item fields id and prefix only. Independently observed prefixes are supplied without future instructions. The factory guard is an engineering interface restriction, not a security sandbox against hostile Python callers accessing private fields.

## Gate handling

Missing evidence, supported numerical failure, runtime mismatch or unsupported GPU blocks the run. Preserve the failure and allocation metadata. Never relax guards or tolerances merely to accept a cloud allocation. An unexpected allocation may be retried in a new bounded, documented run under the same predeclared hardware requirement; every attempt remains in the ledger. Numeric failures require investigation rather than repeated sampling until a pass.

The executable rejects development and confirmatory partitions. A scoped G0 pass does not bypass G1. Before any later authorized development extraction, complete G1 and preflight development lengths. Any overflow blocks the complete job; a larger fixed width needs a new G0 validation. Regenerate affected B1/B2/M features and refit development-only models together under one configuration; never pool incompatible versions. Confirmatory extraction remains prohibited.

## Evidence

Full remote evidence is in Modal volume aeb-g0-closure-v0-5, one timestamped directory per run. Downloaded archives include logs, checks, provenance, comparison tensors and representative original tensors. The 115 per-prefix pipeline PT files in each completed suite remain remote, with file hashes and in-container round-trip equality checks. Local subset hash verification does not constitute an independent download audit of those remote-only PT files.

analyze_closure_ac.py independently checks downloaded hashes, distinct containers, equal contracts, aligned IDs/masks/positions, saved last states/logits and full-active-state digest equality. It requires numpy and audit_saved_tensors.py; it does not run inference. Raw remote files and earlier failure bundles are preserved separately. Gate status must be read from the final report and adjudication, not inferred from a successful Modal transport exit.
