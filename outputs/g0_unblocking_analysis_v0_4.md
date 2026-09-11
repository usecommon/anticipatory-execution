# Analysis of G0 unblocking — v0.4

**Decision today: keep G0 blocked, but close it against a validated extraction contract rather than requiring universal kernel invariance.** No additional GPU experiments or research extraction were run for this analysis. Existing results and implementation were reviewed.

The v0.3 supported-path result is credible progress: 4,929 assertions passed, including 4,922 bitwise-equal numerical checks and 75 completed-word prefixes. The 54 unrestricted failures remain real. They need not permanently block a different, explicitly restricted implementation that cannot use those failing modes.

This corrects an overbroad implication in the earlier status language: G0 should establish reliable measurement in the actual research pipeline, not certify every execution mode offered by PyTorch. The restrictions must be explicit, enforced and tested, with a versioned instrumentation amendment. This is not a waiver of a supported failing test or a tolerance increase.

## Evidence already sufficient to retain

- The original failure type was reproduced before remediation; historical 24/80 and subsequent experiments remain distinct.
- RCA isolated a shape-dependent Q-projection discrepancy on identical inputs and matched it to captured full-model activations.
- Strict determinism alone did not fix the discrepancy; attention variants and FP32 did not make unrestricted execution universally pass.
- The canonical fixed-layout implementation passes the tested repeat, reload, masked-content, causal-suffix, token-alignment, serialization and batch-interface checks.
- Independent local audits verified original tensor hashes and representative canonical causal/masking invariants.

Repeating these same eight short fixtures again is unlikely to close the remaining gaps. Their full-text token lengths are **9, 10, 11, 13, 13, 9, 11, 9**. Large assertion counts across layers should not be confused with broad input coverage.

## Actual blockers and closure criteria

| Issue | Current evidence or gap | Specific closure condition |
|---|---|---|
| Declared active-length range | API accepts 1–128 active tokens; positive cases are short. Rejecting 129 tokens does not establish correct behavior at 128. | Predetermine fixtures at 1, 2, 63, 64, 65, 95, 96, 97, 127 and 128 active tokens. Verify all active hidden-state entries/logits, masks and positions; compare nested token prefixes against the same fixed-width full fixture. Keep an explicit overflow rejection at 129. |
| Content/tokenization coverage | Eight tasks, 75 word prefixes; all happened to align with corresponding full-text token prefixes. | Add held-out QA-only natural texts with punctuation, whitespace, numbers, code/URLs, Unicode and late revisions. Tokenize each observed word prefix independently. Apply causal-equality checks only when token IDs actually align; log alignment differences and handle them correctly in the pipeline. |
| Runtime enforcement | The worker configures the correct environment. The extractor constructor checks FP32 and eager attention but does not enforce all declared settings. | Enforce eval/frozen state, device/model/tokenizer identity, physical shape, explicit mask/positions, deterministic flags, TF32 setting and cache prohibition through the supported factory/entrypoint. Fail closed on a mismatch. Verify the actual forwards, not merely saved metadata. |
| Input validation | `encode()` casts to integer dtype and flattens before validation; the direct forward helper assumes well-formed canonical input. | Reject unintended ranks and non-integer IDs/masks before coercion; prevent a physical batch from being flattened into one sequence. Validate the canonical forward boundary too, or make it a controlled internal helper. Retain normal valid-input behavior and explicit overflow errors. |
| Pipeline integration | QA calls the extractor directly. There is no validated end-to-end research extraction route yet. | Run a small synthetic QA-only pipeline rehearsal through the exact public entrypoint. Verify every call uses `[1,128]`, no cache, correct prefix IDs/length, and the same state-to-logit alignment. Exercise order changes, a fresh process and a fresh container on the same declared hardware class. Verify outputs/manifests, not just process exit codes. |
| Overlength coverage | Inputs beyond 128 are rejected, but handling at dataset/job level is not established. | On development material only, determine whether 128 supports the intended benchmark. If not, choose a larger global width and revalidate before extraction. Otherwise document the scope prospectively. Overflow must visibly block the affected job/stage; do not silently truncate or discard long, potentially late-revising tasks. Do not inspect confirmatory data for this decision. |
| Gate interpretation | Original documents mix required batch/cache/length controls with diagnostics. v0.3 deliberately left full closure unresolved. | Publish an explicit versioned mapping from each G0 requirement to the supported API and test. Batch-interface equivalence remains required; physical batching is unavailable. Cache requests are rejected; raw cache failures remain FAIL outside the supported contract. No fallback to native variable-width/batched/cache paths. |

A fresh-process/container check is not a demand for arbitrary cross-GPU bitwise equality. It validates reload/redeployment within the declared hardware/software contract. Any broader hardware or precision claim requires its own evidence.

## Proposed G0 acceptance rule

Before the next closure run, freeze its cases and implementation/configuration hashes. Maintain `atol=rtol=1e-5`; keep bitwise equality as the observed result, not a selectively changed threshold.

Declare **G0 PASS for canonical extraction vX, specified hardware/software, and the validated active-length range** only if:

1. All supported-path numerical tests pass; expected error/rejection behavior is separately classified and passes.
2. Prefix construction, token alignment, masks, positions, output alignment, serialization, reload and boundary cases are validated through the actual entrypoint.
3. Invalid configurations, overlength inputs and excluded modes fail closed without silent data loss or fallback.
4. The gate-requirement mapping and implementation restriction are documented, and every historical/native failure stays intact with its original status.
5. The evidence manifest, code/configuration hashes and a fresh-process/container repeat are verified.

Any failure on the supported path blocks this scope. An unsupported native control can remain FAIL without implying the supported contract failed, provided the path cannot be reached by research extraction and the protocol explicitly reflects that restriction. This is a gate-definition clarification before further testing, not post-hoc relabeling to chase a pass.

The current eight-text result alone does not satisfy these closure conditions. There is no basis to promote G0 today.

## Scientific validity implications

The constrained path does not change the thesis: action-level future non-revision and incremental value beyond prefix, outputs and a single hidden state remain the targets. It controls a measurement confound by keeping the numerical execution layout fixed.

For the eventual scientific comparison, B1 observable features and B2/M internal features should come from the same pinned forward configuration. Comparing B1 outputs from BF16/cached execution against M states from FP32/canonical execution would introduce a configuration confound. This does not require every eventual product implementation to use the same inefficient instrumentation path; it requires a clean scientific comparison and separately measured systems costs.

The fixed width is independent of unseen suffixes. Changing width based on final utterance length would violate that boundary. Varying width across prefixes within one trajectory would also reintroduce the shape issue. A future bucketed or faster implementation needs separate validation.

Runtime/memory overhead should be measured during closure and later included in matched-compute systems evaluation. S1 profitability is not a prerequisite for instrumentation correctness. A numerically valid scientific pipeline can still fail the latency/compute product hypothesis.

## What does not block this G0 scope

- Repairing every native BF16, physical batching or KV-cache mode.
- Proving universal invariance across GPUs, precisions, versions or arbitrary lengths.
- Establishing H1–H4 or product latency benefits before collecting valid measurements.
- Reopening the narrowed novelty claim or changing the frozen thesis.

Attention/KV-derived research features remain exploratory/unvalidated where they depend on excluded extraction modes. Do not silently promote them because hidden-state QA passes.

## Stage progression remains separate

After the restricted G0 contract is actually cleared, **G1 still must pass**: two independent annotations, the required agreement threshold, and adjudication. The owner gold key does not substitute for independent annotation. The handoff requires both gates before Stage 1.

Confirmatory extraction remains prohibited. Neither this analysis nor a later scoped G0 pass authorizes opening the confirmatory set or skipping the development/freeze stages.

## Recommended next execution

One versioned hardening change and one predeclared closure suite addressing the gaps above. Reuse the pinned Modal checkpoint and hardware/software configuration; preserve the old native controls as failure evidence. Run the closure suite and a clean-container repeat without feature fitting or hypothesis evaluation. Broaden only if a specific failure demands it.

No new GPU cost was incurred by this analysis. Prior run costs remain in their respective reports. No new job, monitor or automation was scheduled.

## Evidence reviewed

- `g0_fix_v0_3/source/canonical_g0_v0_3.py`: canonical input/forward implementation.
- `g0_fix_v0_3/PROTOCOL_ADDENDUM_v0_3.md`: declared constraints and unclosed gate scope.
- `g0_fix_v0_3/fix_20260911T171625Z/checks.json` and `environment.json`: recorded checks and execution settings.
- `g0_fix_v0_3/independent_audit.json`: independent representative raw-tensor audit.
- Original runbook, README and preregistered protocol already reviewed in this task; earlier G0/RCA evidence remains unchanged.
