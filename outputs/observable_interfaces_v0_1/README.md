# Observable interfaces and provider-scope resolution — v0.1

The pinned BFCL filesystem has no revision/incarnation metadata operation. Its public method inventory is recorded in PROVIDER_AUDIT.json. We therefore retain BFCL as an **offline static-snapshot measurement fixture**, not a deployed freshness provider. Missing trustworthy freshness requires fresh work/unresolved handling in a live policy; mock revision tokens are not promoted to real guarantees. This limits S1 claims, not preparation for a controlled offline H2 comparison. No new provider or benchmark has been silently substituted.

## Implemented components

- `observable.py`: streaming row-wise full-prefix NLL; one-token response-code probabilities with both raw support mass and conditional probabilities; typed ls action identity and temporal persistence with missing observations explicit.
- `capture.py`: a separate read-only extractor proxy that measures full active logits before the unchanged existing entrypoint discards all but the last position. It returns the same state object and writes ordinal/hash-linked JSON sidecars. Existing entrypoint owns input allowlists, whole-job preflight, partition rejection and tensor saving. The proxy is not a standalone authorized launcher.
- `test_interfaces.py`: analytic alignment/probability/persistence checks and a proxy test double. This validates software behavior only; it does not execute PyTorch or a foundation model.

Full-prefix NLL scores each observed token after the first using the preceding logits row. It preserves count/sum/mean, with null mean for a singleton. This version uses CPU binary64 and fsum reductions; do not assume exact equality with prior sum/NumPy reductions. Legacy FP32 tensors remain unchanged. Row-wise conversion avoids materializing all vocabulary rows as Python lists at once, but CPU cost still needs measurement.

## What the action probabilities mean

The interface supports a future code-choice measurement for `list_current_all`, `list_current_visible`, and `abstain`. It measures probability of declared single-token response codes, with raw outside-support mass retained. Renormalized probabilities are explicitly conditional on those codes; high conditional confidence at near-zero support mass must not be presented as high model confidence. They are not calibrated usefulness probabilities.

No actual response prompt, token-ID mapping or model outputs are supplied in this package. These require a separately frozen prefix-only prompt, pinned-tokenizer checks that codes are distinct single tokens in the actual context, and full-input preflight. A one-token interface must reject unsupported multi-token encodings rather than silently change the event. The restricted directory action support is not a general action ontology.

Typed execution-argument completeness is not semantic completeness of the user's request. We implement canonical identity/persistence, not a claim that a fully populated ls call establishes stable target/constraints. Prefix-known slot evidence, ambiguity and semantic argument-completeness remain pending. Missing candidates yield missing transitions rather than false persistence.

## Required real-model bridge before using capture

Use the existing 12 instrumentation-validation inputs under the exact canonical-v0.5 contract, one bounded run with paired unwrapped/wrapped forwards (24 QA forwards). Compare every legacy saved state/logit/mask/position/ID field bitwise; verify sidecar count/token hashes and independently compute shifted token NLL from full active logits. Confirm overlength/malformed/confirmatory requests fail before forwarding through the existing entrypoint. Record CPU summary time and GPU/runtime provenance. Retain failures without widening tolerance. This package does not launch that run or enable new input hashes.

Sidecars emitted before a later tensor-save failure are orphan evidence, not successful research records. Join only to the corresponding successful manifest row with matching ordinal, token hash and contract; a sidecar directory alone is not a complete extraction. Future integration must retain partial failures and emit an explicit successful combined manifest. Existing 4,013 saved last-position tensors cannot recover these measurements retrospectively.

## Current boundary

Software components exist; **full B1 is still incomplete**. Real tensor/entrypoint integration, numerical bridge, action prompting/capture, semantic completeness, fair interactions and temporal controls remain necessary before full model comparisons. New context/schema prompts must be shared across B0/B1/B2/M and preflighted; old plain-prefix states cannot be mixed into a new contextual comparison.

No model forwards, probes, new labels, public data changes, G1 completion or confirmatory extraction occurred. The frozen thesis and negative diagnostic remain unchanged. Next is the bounded canonical capture bridge, followed by a frozen action-response prompt/tokenizer preflight—not another toy challenge expansion.
