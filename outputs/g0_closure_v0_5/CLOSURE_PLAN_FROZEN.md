# Predeclared G0 closure plan v0.5

Scope: canonical-v0.5, one-prefix physical shape [1,128], active length 1..128, FP32 eager Qwen2.5-7B-Instruct revision a09a35458c702b33eeacc393d103063234e8bc28, torch 2.5.1+cu124, Transformers 4.45.2, NVIDIA A100-SXM4-40GB, seed 1729, explicit positions and additive 4D mask, strict determinism, TF32/autocast/cache off. Tolerances remain atol=rtol=1e-5. Tests/cases/code are hashed before launch. No outcome-based test removal or tolerance changes.

## Planned tests

1. Verify pinned model/tokenizer cache bytes against the named Hugging Face commit's LFS SHA256/git-blob identities. Verify the resulting SHA256 manifest again on each container before load.
2. Bridge all eight original QA cases against preserved v0.3 canonical activations, all 29 hidden-state entries and active logits. Any unexpected regression is retained and blocks this closure.
3. Two predeclared synthetic token fixtures (repeated tokens and seeded mixed natural-fixture tokens), 128 tokens each. Test nested prefixes at 1,2,63,64,65,95,96,97,127,128, all active states/logits and masks/IDs. Test repeats.
4. Twelve additional QA-only natural texts in fixtures.json: punctuation, preserved whitespace, code, URL, numbers, Unicode, and late revisions. Test every independently tokenized completed-word prefix, repeat it, and compare to the full token sequence only when alignment permits. Retain every extraction even when tokenization makes a causal-equality assertion inapplicable.
5. Real masked-content perturbation at the model input; serialized input-padding widths including 256 with <=128 active tokens; canonical shape never varies.
6. Fail-closed invalid input, invalid mask, cache/past, unsafe constructor and runtime-contract tests. No malformed-input coercion or rank flattening. Runtime mutations must be rejected before a forward; no parameter value is changed.
7. QA-only public job entrypoint, all-or-nothing preflight for overlength inputs, forbidden development/confirmatory partitions and unexpected future-information fields, output contract/item/token alignment and serialization. Reverse batch-interface order and active-content sensitivity.
8. Independently observe actual model-call tensor/mask/position/cache settings via a QA hook. Compare the written pipeline output to independently obtained per-prefix results.
9. Execute the complete suite in two single-use Modal containers, each launching a fresh Python worker. Verify distinct container identities, identical extraction contracts and cross-container states/digests at the original tolerances. Retain raw differences if any.

## Acceptance and scope mapping

A supported numerical or enforcement failure, exception, missing evidence or contract mismatch blocks G0 closure. All successful numerical checks must also be finite. Expected rejected requests are recorded separately as enforcement tests, not treated as extraction success.

G0 requirements map to the actual supported implementation: repeat/reload -> within-run repetitions, prior-canonical bridge and fresh-container comparison; batch-vs-singleton -> ordered serialized batch interface and pipeline output identity; masked padding -> real physical masked-content perturbation plus input-normalization checks; sequence length/suffix -> fixed-width nested token/text prefixes through the boundary; alignment/positions/masks -> actual-forward hook and written IDs; hidden-state integrity/logits -> all 29 entries, active logits, finiteness, serialization, checksums; cache -> explicit rejection and preservation of old native cache FAIL results, not a claim of cache equivalence.

Excluded modes remain visibly unvalidated/failed: native variable physical widths, native batching, KV reuse, other hardware/dtypes/backends, active length >128. Historical failures are not rerun merely to change their labels. No supported failed case is removed to create a pass.

If all closure criteria pass, mark G0 PASS only for this exact contract and active-length scope. G1 remains pending; the executable stays QA-only. Full development benchmark length coverage is unknown and must be checked before any future research job; overflow blocks the job rather than changing the experimental population.

## Evidence and resource limits

Read-only mounts for checkpoint and prior evidence. New append-only run directories in Modal volume aeb-g0-closure-v0-5. Preserve all metrics, logs, provenance, comparison states and any numerical failures. Download complete JSON/log evidence, comparison snapshots and failure tensors; per-item pipeline tensor files remain in the remote volume with hashes.

Two sequential, single-use A100-40GB containers, zero retries. Each worker has a 1,080-second timeout; each function has a 1,200-second timeout. CPU-only identity verification has a 600-second limit. No monetary cap supplied; report measured runtime and resource-cost estimates, not an invoice. No scheduled follow-on work.
