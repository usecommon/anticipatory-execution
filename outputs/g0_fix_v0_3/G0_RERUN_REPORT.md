# Fixed-layout G0 rerun — v0.3

**Candidate extraction path: PASS on the QA set. Overall G0: BLOCKED. Original unrestricted execution: FAIL.**

The new extraction path removes shape variation from permitted calls and passes all 4,929 supported-path checks. The old variable-shape/batched/cached backend paths still fail 54 of 106 numerical controls. This is a validated constrained workaround on the stated QA set, not a general repair of PyTorch/Qwen kernels and not an unrestricted G0 pass.

## What changed

The candidate always executes one prefix in a physical tensor of shape `[1,128]`, with FP32 eager attention, explicit position IDs, an explicit 4D causal/padding mask, strict deterministic algorithms and `CUBLAS_WORKSPACE_CONFIG=:4096:8`. Batch-interface requests are serialized through that same path. KV-cache reuse is rejected. Model weights are frozen; no training occurred.

The 128-token width is predetermined and does not use the unseen suffix or final instruction length. Empty, overlength, left-padded, holey-mask and cache requests raise errors. There is no truncation or automatic fallback. Eight original QA texts were used; the current positive tests cover their short prefixes and explicit short suffix extensions. Although the API permits up to 128 active tokens, this run did not exhaustively validate long active sequences near that limit.

This change fixes the operational trigger identified by the RCA—changing the numerical computation layout—inside the constrained API. It does not make native variable-shape matrix multiplication invariant. The original harness and every prior evidence bundle are unchanged. The implementation amendment is in `PROTOCOL_ADDENDUM_v0_3.md`.

## Results

Original tolerance retained: `atol=rtol=1e-5`. The supported path had 4,922 numerical equality checks, all bitwise equal, plus one active-content sensitivity check and six rejection checks. No supported-path failures occurred.

| Supported-path check | Passed | Coverage |
|---|---:|---|
| Repeat | 240/240 | 8 texts × 29 hidden-state entries plus logits |
| Input padding normalization | 960/960 | Unpadded, 64, 96, 128 serialized input widths; physical execution always 128 |
| Actual masked-token content perturbation | 240/240 | Changed masked IDs at the model input, bypassing normalization |
| Actual unmasked suffix extension | 240/240 | Earlier active states/logits compared after adding real future tokens |
| Serialization equality | 240/240 | Saved and restored active states/logits |
| Batch interface and order | 480/480 | Forward and reversed input order; single-prefix physical execution |
| Completed-word prefix invariance | 2,250/2,250 | 75 prefixes × 29 hidden-state entries plus logits |
| Model reload | 240/240 | All eight texts after a fresh model load |
| Token/mask/position alignment | 24/24 | Eight texts |
| Finite hidden states | 8/8 | All stored hidden-state entries |
| Active-content sensitivity | 1/1 | Different observed input produces different final states |
| Invalid/unsupported request rejection | 6/6 | Empty, overflow, holey/left masks, cache and past state |

All 75 independently tokenized completed-word prefixes aligned with the corresponding full-utterance token prefixes in this fixture set; no token-boundary comparison was omitted. The checks are correlated instrumentation assertions, not 4,929 independent scientific observations.

The following real native controls were also rerun without the canonical adapter, in FP32 eager mode. Their failures remain FAIL:

| Unrestricted backend control | Failed | Max absolute difference |
|---|---:|---:|
| Sequence-length extension | 40/80 | 0.0003890991 |
| Physical batch vs singleton | 11/20 | 0.0005645752 |
| Actual KV-cache vs full forward | 3/6 | 0.0001983643 |

These new FP32/eager counts must not replace or be pooled with the historical 24/80 report, the v0.1 BF16 80/80 reconstruction, or the v0.2 two-text RCA.

## Independent verification

A separate local reader verified the representative saved tensors: physical shape `[1,128]`, mask shape `[1,1,128,128]`, all 29 hidden-state entries present, and exact equality of earlier active states and logits after both masked-content perturbation and a three-token real suffix extension. See `independent_audit.json`.

All downloaded artifacts listed in the remote manifest passed checksum verification. The other raw tensors remain preserved remotely with their recorded hashes; they were not all downloaded and are not described as independently verified locally.

## Gate impact and next allowed action

The candidate passes the stated supported-path QA set. It does **not** clear the original unrestricted G0 requirements: native shape/batch/cache discrepancies remain, and the restriction to a canonical path changes the permitted extraction contract. No failure has been waived through a tolerance increase or relabeling.

Next allowed work is to complete G0 closure for the restricted contract: validate long active sequences and declared boundaries, independently audit enforcement of that path end to end, and explicitly resolve the protocol coverage of excluded physical batching and KV reuse. Do not expose those modes as validated or use arbitrary-width extraction as a fallback. A short-fixture supported-path PASS alone is insufficient to authorize research extraction.

G0 remains BLOCKED; unrestricted controls remain FAIL. G1 remains an independent, pending annotation gate. The frozen thesis and scientific endpoints are unchanged. No Stage 1 feature extraction, confirmatory extraction, probe training or consequential action ran.

## Exact evidence and environment

Run: `fix_20260911T171625Z`, [Modal application](https://modal.com/apps/jeff-34667/main/ap-CM5rdNP91pidOjba2DIbNx).

Pinned model/tokenizer: Qwen2.5-7B-Instruct, commit `a09a35458c702b33eeacc393d103063234e8bc28`. One A100-40GB; PyTorch 2.5.1+cu124; Transformers 4.45.2; FP32 eager; seed 1729; TF32 disabled; cache off. Complete GPU inventory and dependency freeze are in the run directory.

The evidence directory includes source code and hashes, the versioned implementation amendment, all 5,035 check records, incremental records, summary and environment JSON, logs, a complete remote manifest, and four representative raw tensor files. All 100 raw tensor files are retained in Modal volume `aeb-g0-fix-v0-3`, under `/fix_20260911T171625Z`. The downloaded archive intentionally contains representative tensors rather than duplicating every activation snapshot.

## Cost and execution limits

One job, zero retries, worker exit 0. Worker wrapper wall time: 70.21 seconds; local app completion was approximately 97 seconds after GPU-function start. At the previously verified [Modal A100-40GB rate](https://modal.com/pricing) of $0.000583/second, this corresponds to approximately **$0.041–$0.057 GPU-only**, depending on whether packaging/transfer time is included. These are runtime-based estimates, not invoice totals; CPU, memory, storage and billing adjustments are excluded. No monetary cap was supplied, and account credits were not queried. The 1,080-second worker and 1,200-second function limits were not reached. The job has completed; no follow-on job is scheduled.
