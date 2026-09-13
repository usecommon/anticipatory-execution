> Latest: [first AI-labeled diagnostic comparison](../outputs/exploratory_comparison_v0_1/README.md) is complete. Tested dynamics did not outperform available output signals; full B1/H2/H3 remain unimplemented/untested. The public check slice has zero negatives. Preserve the result and read its measurement/label limitations before further work; this reaches the planned human-review revisit checkpoint.

> Latest execution (2026-09-12 local start): [4,013-prefix exploratory extraction and independent verification passed](../outputs/exploratory_extraction_v0_1/README.md). Raw tensors remain on the named Modal volume. Verification failures/recoveries are preserved. At that extraction stage, no probes had been fitted; see the newer diagnostic update above and the feature-coverage audit before further comparisons. Human G1 remains deferred for exploratory work only.

> Current gate-timing update (2026-09-12): read [AI-only exploratory amendment](AI_ONLY_EXPLORATORY_AMENDMENT_v0_1.md) before the historical status below. Human G1 is deferred only for exploratory development; technical/data prerequisites remain. Human G1 still blocks confirmatory labeling/freeze, and confirmatory extraction remains prohibited.

# Anticipatory Execution — ChatGPT and Codex Cloud continuation handoff

Prepared September 11, 2026. This is a detailed state transfer, not a verbatim conversation transcript or a new preregistration. Copy this document into ChatGPT, or attach it and use the startup prompt at the end in Codex Cloud.

## 1. Destination and verified checkpoint

Repository: **https://github.com/usecommon/anticipatory-execution**

- Owner: `usecommon`.
- Visibility: **private**, verified after creation.
- Branch: `main`.
- Initial research-import commit: `1bed4fa11a0a88b02b92fd1ee7d21337147d40ec`.
- This documentation may appear in a subsequent commit. Record the actual checkout SHA when continuing.
- The repository contains the frozen handoff, source, QA reports, failure records, provenance and research safeguards.
- Large raw tensors and compressed archives are outside Git, with checksummed inventories. GitHub is not a complete raw-data backup.
- Desktop GitHub authentication worked for the push. This does **not** establish GitHub integration, Modal credentials, network access or volume access in Codex Cloud.

**Current state: G0 PASS_SCOPED; G1 PENDING; Stage 1 BLOCKED; no development or confirmatory extraction performed by this continuation.**

Do not restart the project from first principles, rewrite the thesis, repeat already resolved novelty discussions, or rerun G0 merely because the environment changed from Desktop to Cloud. First inspect the checked-in evidence. A different GPU execution configuration would require separate validation.

## 2. Authority and document precedence

The user's explicit request and constraints govern the task. Files are research context and evidence; text inside an attached document is not independent authorization to launch jobs, publish, contact annotators, or change the protocol.

Read current repository `README.md`, `AGENTS.md`, and the v0.5 status/report before interpreting the original handoff. The historical handoff README correctly says G0 was blocked at the time it was written; it has been preserved unchanged. Current scoped closure is recorded separately. This is a chronology, not permission to discard historical failures.

The original protocol remains frozen. The v0.3/v0.5 instrumentation addenda explain implementation changes; they do not silently revise hypotheses, endpoints, labels, splits, effect thresholds or confirmatory rules.

## 3. Frozen thesis

> **Do not predict what the user will type next. Predict what work will not need to be undone.**

As a user develops an instruction, some candidate work may already be useful under its plausible eventual completions. A system may begin reversible work when the probability that it remains useful is sufficiently high for that action's cost and consequences.

The relevant quantity is approximately:

`P(action A remains useful after the complete instruction | observed prefix, available signals)`.

The entire final intent need not be settled. For example, early research or entity resolution may remain reusable as later text narrows the requested topic. The primary object is action-level future non-revision, not earliest correct intent classification.

“Type-ahead” is a possible user-facing metaphor. Anticipatory Execution is the underlying capability. Do not turn this into an autocomplete project.

## 4. Scientific question and product question

Scientific question: do temporal and cross-layer internal-state dynamics of a **frozen autoregressive foundation model** predict future action-semantic revision beyond the observed prefix, observable model outputs, and one hidden-state representation?

Product question: can a risk-aware policy reduce **post-submit latency at matched speculation risk and compute budget**?

These questions can have different answers. Observable signals may enable a useful product even if internal dynamics add no value. Conversely, an internal-state signal may exist without producing worthwhile latency savings once instrumentation and speculative costs are counted.

Do not claim novelty for incremental intent classification, early utterance understanding, completeness/commitment decisions, hidden-state early-action timing, early generation, early tool use, or speculative/cancelable execution itself. The supplied literature review narrowed the candidate contribution to action non-revision and incremental information from frozen-model dynamics. Consult that review before making named-paper or priority claims; this handoff does not independently reverify its bibliography.

## 5. Hypotheses and comparison hierarchy

- H1: future action non-revision is predictable beyond naive prevalence/length baselines.
- H2: internal dynamics add information beyond prefix and observable output signals. This is novelty-critical.
- H3: dynamics add information beyond a single hidden-state snapshot.
- H4: generalization beyond the development distribution and directional replication in another frozen model family.
- S1: a risk-aware policy saves post-submit latency at matched speculation risk and compute budget.

| Model | Inputs/purpose |
|---|---|
| Naive | Prevalence and prefix length |
| B0 | Prefix text/embedding, length and completeness cues |
| B1 | B0 plus observable final-layer probabilities, entropy, margins, surprisal, persistence and argument completeness |
| B2 | B1 plus one frozen hidden-state representation |
| M | B2 plus temporal/cross-layer internal dynamics |

The original README specifies the primary scientific endpoint as `DeltaNLL(B1→M) = NLL(B1) − NLL(M)`. H2 requires the locked confirmatory 95% utterance-cluster-bootstrap interval entirely above zero and at least 1.0% relative NLL improvement. H3 applies the corresponding rule to B2 versus M. Read the original protocol for the complete operational definition; this summary does not replace it or authorize confirmatory execution.

Keep all prefixes of an utterance in the same split and group near-duplicate/template families. No suffix leakage or confirmatory feature/layer/threshold selection. No model-weight training. Future probes and calibrators are development-only until the protocol permits otherwise.

## 6. Action classes and evaluation

| Class | Meaning | Examples |
|---|---|---|
| 0 — Observe | Maintain hypotheses | Intent/entity inference |
| 1 — Prepare | Cheap reversible preparation | Context loading, query construction, tool warmup |
| 2 — Speculate | Bounded disposable/reusable work | Search, retrieval, read-only calls, calculations |
| 3 — Stage | Prepare without committing | Drafts, proposed patches, prepared transactions |
| 4 — Commit | Consequential external execution | Sending, purchasing, booking, publishing |

Primary experiments do not autonomously execute Class 4 actions. Consequential behavior is simulated. Thresholds depend on reversibility, compute cost, visibility and consequences. Count wasted work and wrong visible actions; earliest correct intent is not the main product metric.

## 7. Historical evidence and original blocker

The supplied background reports an earlier frozen Qwen2.5-7B-Instruct pilot with eight intents, 240 training examples, 40 selection examples, 80 evaluation examples and 3,228 prefixes. Approximate block accuracies were 86.25% at block 7, 93.75% at block 14 and 91.25% at block 21. These are historical reported results, not new verified efficacy results from this continuation. They did not show a clean monotonic intermediate-layer advantage.

Subsequent historical QA reported 499 suffix-invariance failures over 100 utterances/388 prefixes, then a bounded 24/80 sequence-length-extension failure result. Repeats, reloads and fixed-shape controls were reportedly stable. The full original diagnostic configuration and raw evidence were not supplied, so exact reproduction of the historical 24/80 count remains unavailable.

The user required reproduction of the failure type before attempting mitigation, preservation of all failures, and no confirmatory extraction. That order was followed.

## 8. Work completed in this continuation

### v0.1 — Failure reconstruction

The A10 BF16 SDPA reconstruction failed **80/80** length comparisons at the unchanged tolerance. The original harness had 20 batch failures; supplemental QA also found native batch/cache failures. Repeats and fixed-shape controls passed. These results reconstructed the failure type; they are not an exact replay of the original 24/80 experiment.

Evidence: `outputs/g0_evidence_v0_1/`.

### v0.2 — Root-cause analysis

Six configurations were compared on the same A100-SXM4-40GB. Matched active inputs first diverged in Q/K/V linear projections before attention. An isolated Q projection reproduced the shape-dependent discrepancy. This demonstrated a numerical matrix-shape effect independent of attention masking in the tested cases.

| Configuration | Length failures | Batch failures | Cache failures |
|---|---:|---:|---:|
| BF16 SDPA | 10/10 | 10/10 | 6/6 |
| BF16 SDPA + strict determinism | 10/10 | 10/10 | 6/6 |
| BF16 eager + strict determinism | 10/10 | 10/10 | 6/6 |
| BF16 SDPA forced math | 10/10 | 10/10 | 6/6 |
| BF16 SDPA, reduced-precision reduction off | 10/10 | 10/10 | 6/6 |
| FP32 eager + strict determinism | 8/10 | 8/10 | 3/6 |

Strict determinism removed warnings but did not remove the discrepancies. FP32 reduced them substantially but did not make native variable shapes pass. The exact low-level kernel/accumulation order was not profiled; do not claim a uniquely proven instruction-level cause or extend the projection result to every cache failure.

Evidence: `outputs/g0_rca_v0_2/RCA_REPORT.md` and associated raw comparison metadata.

### v0.3 — Initial canonical candidate

A fixed physical [1,128], FP32 eager, serial-prefix, no-cache path passed 4,929 supported checks with exact numerical equality. Native controls still failed 54/106 comparisons. This was a candidate-contract pass, not yet sufficient to close G0. It needed stronger boundary, enforcement, pipeline and independent-container coverage.

Evidence: `outputs/g0_fix_v0_3/`.

### v0.4 — Unblocking analysis

The analysis established a defensible scoped gate: unsupported native execution modes need not be repaired if they remain visibly failed and the supported extractor enforces their exclusion. The fix cannot silently redefine supported failures, increase tolerance, truncate examples or hide coverage limits.

Evidence: `outputs/g0_unblocking_analysis_v0_4.md`.

### v0.5 — Hardened implementation and closure

The factory pins/verifies checkpoint identity and the numerical configuration. Input validation happens before coercion, whole-job preflight rejects invalid/overlength jobs before inference, and the public pipeline permits QA only. Actual-forward hooks check physical shapes, masks, positions and cache settings.

Two completed fresh-container runs each passed **8,427 checks**: 8,394 supported assertions plus 33 expected-rejection assertions. Each contains 8,276 numerical comparisons with maximum absolute difference zero. Each made 410 actual forwards, testing 115 independently tokenized word prefixes from 12 new natural texts, two synthetic families across ten boundary lengths, serialization, runtime rejection and prior-canonical regression continuity.

Independent local adjudication passed **1,092 checks**, including **155 cross-container cases** with identical contracts, aligned inputs, bitwise-equal last states/logits and equal full-active-state digests. Assertion counts are not independent scientific samples or effect estimates. Natural fixtures reach 25 tokens; longer boundary coverage uses synthetic token families.

Successful runs:

- `closure_a_20260911T175740Z`
- `closure_c_20260911T180932Z`

Preserved failed attempts:

- Initial launcher import-path failure in CPU orchestration, before GPU QA.
- `closure_b_20260911T180521Z`: unvalidated GPU guard rejected the allocation before numerical extraction. The actual rejected GPU subtype was not captured, so its identity remains unknown.
- An import-only launcher correction and later pre-worker allocation logging are versioned. The replacement used unchanged extraction source, fixtures, tolerances and required hardware. No guard was relaxed.

Current evidence: `outputs/g0_closure_v0_5/G0_CLOSURE_REPORT.md`, `STATUS.json`, `closure_adjudication.json` and the preserved attempt records.

## 9. Exact validated extraction contract

| Setting | Validated value |
|---|---|
| Model | Qwen/Qwen2.5-7B-Instruct, frozen |
| Model/tokenizer revision | `a09a35458c702b33eeacc393d103063234e8bc28` |
| GPU | `NVIDIA A100-SXM4-40GB` |
| PyTorch | `2.5.1+cu124` |
| Transformers | `4.45.2` |
| Precision/backend | FP32, eager attention |
| Physical input shape | One prefix, `[1,128]` |
| Supported active lengths | 1 through 128 tokens |
| Batching | Serialized through the same single-prefix numerical path |
| Positions/mask | Explicit positions and 4D additive causal/padding mask |
| Cache | Disabled; cache requests rejected |
| Determinism | Strict, seed 1729, `CUBLAS_WORKSPACE_CONFIG=:4096:8` before CUDA initialization |
| TF32/autocast | Disabled |
| Numerical tolerance | `atol=rtol=1e-5`, unchanged |

Contract ID:

`95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0`

G0 passes only for this enforced scope. Native variable widths, native batches, KV reuse, alternative hardware/precision/backends and active lengths above 128 remain unsupported. Driver/runtime changes also require revalidation. This is a validated measurement policy, not a repair of native GPU arithmetic or proof across arbitrary text distributions.

## 10. Numerical non-neutrality is a mandatory consideration

The user explicitly required the fix to preserve the thesis while recognizing that numerical results may change.

Precision, attention implementation, physical shape and cache policy can change hidden states, logits, temporal features, layer rankings, probe fits, calibration and measured incremental value. Correcting shape artifacts may reduce, eliminate or reverse an apparent internal-state advantage. That is a valid result, not a reason to tune the pipeline back toward historical accuracy.

Required rules:

1. Preserve all historical versions and unfavorable outcomes.
2. Do not pool BF16/historical features with canonical FP32 features as though they were equivalent.
3. Do not reuse affected old probes or calibrators without reanalysis/refitting.
4. Once permitted, regenerate affected B1/B2/M features using the same forward configuration and refit affected development-only components together.
5. Do not select numerical settings, layers, thresholds or exclusions based on confirmatory outcomes.
6. A v0.3-to-v0.5 bridge pass establishes limited canonical FP32 continuity, not equivalence to earlier BF16 results.
7. Keep H2/H3 conclusions separate from product viability.
8. Count fixed padding, FP32, serial execution, no-cache overhead and wasted work in later S1 comparisons.

The development benchmark's length distribution is unknown. Preflight it before any future authorized development extraction. If 128 tokens is insufficient, use an outcome-independent larger global width and rerun G0. Do not silently truncate or drop long/late-revising instructions, or infer width from unseen final text.

Full policy: `outputs/g0_closure_v0_5/RESEARCH_SAFEGUARDS.md`.

## 11. G1 is the next substantive research gate

The original pilot contains 200 items, 50 tasks and 12 domains. G1 requires two independent annotators, Cohen's kappa at least 0.70, and the prescribed disagreement-adjudication process. It has **not** passed.

The label concerns whether a candidate action's work is reusable in the final correct task without material re-execution. It is not simply whether an intent guess is correct.

The owner gold key is not independent annotation evidence. Do not use it to fill annotator sheets, fabricate agreement, or supply the missing independent labels. Keep annotators blind to the key and each other. Give annotators only the appropriate blind materials; do not give them access to this repository, which contains the key.

Useful preparatory work can include auditing workbook/rubric structure, preparing blinded exports and a collection workflow, and checking agreement-calculation logic with synthetic labels. Preparation does not equal G1 passage. Actual independent annotations remain required. Do not contact anyone or transmit annotation material without user authorization.

After both G0 and G1 pass, separately authorized Stage 1 development can proceed under the frozen protocol. This handoff does not authorize that extraction, and confirmatory extraction remains prohibited.

## 12. Repository reading order and code location

Read these in order:

1. `README.md` and `AGENTS.md`.
2. `outputs/g0_closure_v0_5/STATUS.json`.
3. `outputs/g0_closure_v0_5/G0_CLOSURE_REPORT.md`.
4. `outputs/g0_closure_v0_5/RESEARCH_SAFEGUARDS.md`.
5. `outputs/g0_closure_v0_5/RUNBOOK.md` and `CLOSURE_PLAN_FROZEN.md`.
6. `provenance/ARTIFACT_STORAGE.md`, `IMPORTED_FILES.json`, `EXTERNAL_ARTIFACTS.json`.
7. Original preregistered protocol and annotation rubric in `handoff/`.
8. Earlier reports/source when needed to understand specific failures.

Validated source is intentionally retained in `outputs/g0_closure_v0_5/source/`:

- `extractor.py`: contract-enforced frozen-model factory and extraction.
- `pipeline.py`: QA-only job entrypoint and preserved-text word prefixes.
- `worker.py`: predeclared closure suite.
- `fixtures.json`: fixed QA fixtures.
- `modal_closure_v0_5_2.py`: latest preserved orchestration example, including allocation logging.
- Earlier launcher versions: retained to preserve failures and changes.
- `analyze_closure_ac.py` and `audit_saved_tensors.py`: independent downloaded-evidence audit.

Do not refactor or reformat this imported implementation merely to make the directory layout prettier. Its code hashes are part of provenance. A substantive successor should be versioned, reviewed and validated.

The existing launchers reuse historical output filenames if run unchanged. Do **not** invoke them casually. Any later authorized QA run requires a new versioned launcher, fresh unique labels/output locations and preserved pre-run hashes. No automatic fallback or repeated numerical sampling until a pass.

## 13. Raw artifacts and Modal access

The migration imported 227 byte-verified files; the initial commit tracks 234 files including repository documentation and verification tooling. It inventoried 112 large local artifacts, totaling approximately 1.94 GB, outside Git. Counts describe the initial import, not subsequent documentation commits.

| Evidence | Modal volume | Principal run root(s) |
|---|---|---|
| v0.1 failure reconstruction | `aeb-g0-evidence-v0-1` | `run_20260911T163140Z` |
| v0.2 RCA | `aeb-g0-rca-v0-2` | `rca_20260911T165054Z` |
| v0.3 candidate | `aeb-g0-fix-v0-3` | `fix_20260911T171625Z` |
| v0.5 closure | `aeb-g0-closure-v0-5` | closure_a, closure_b, closure_c timestamps above |
| Pinned checkpoint | `aeb-qwen-pinned-model-v0-2` | Consult preserved launcher |

Desktop used authenticated Modal profile `jeff-34667` and Modal CLI 1.5.5. Cloud does not inherit that profile or its credentials. Do not copy credentials into a prompt, Git, logs or this document.

The individual 115 pipeline tensor files per successful v0.5 suite remain remote with recorded hashes and in-worker round-trip checks. They were not independently downloaded. Some compressed local archives may not exist remotely. Use the storage document, original launcher and exact manifests to locate/retrieve evidence; verify hashes after retrieval.

Run reports contain measured runtime and limited GPU-only cost estimates, not invoices. Account balance and actual total bill were not retrieved. No standing monetary cap, automated continuation or blanket future GPU authorization was established by migration.

## 14. Codex Cloud setup — owner actions and first task

The repository is ready for Cloud inspection, but no Cloud environment has been created or verified in this conversation.

Official setup is to sign into Codex Cloud, connect GitHub with access to the chosen repository, create a repository environment, and start a task in it. Select `usecommon/anticipatory-execution`; keep repository access limited to intended users. Desktop `gh` login is separate from this connection. [Official Codex Cloud setup](https://learn.chatgpt.com/docs/cloud).

For the **first task**, use CPU-only repository inspection. From the repository root:

```sh
python3 scripts/verify_import.py
git rev-parse HEAD
git status --short
```

The verification script uses the Python standard library, verifies imported-file bytes/hashes, parses Python source and checks recorded gate constraints. It does not import the model, call Modal, perform annotation, or rerun G0. No special GPU setup is needed for this inspection. If Python is absent, configure it before this check.

Cloud environments have setup scripts and configurable internet access. Current official documentation says environment secrets are available to setup scripts and removed before the agent phase; agent internet is off by default and outbound access uses a proxy. Therefore, placing a Modal token in setup-only secrets does **not**, by itself, establish that a later agent-issued Modal command will authenticate. [Official environment configuration](https://learn.chatgpt.com/docs/environments/cloud-environment).

For later Modal execution, separately validate a supported credential and network arrangement, with the user, before launching paid work. Do not convert secret values to ordinary environment variables or persist credentials merely to bypass phase restrictions. If runtime authentication or proxy compatibility is unavailable, Cloud can still handle code/review and evidence analysis while an authorized Desktop/other runner executes Modal jobs and returns versioned artifacts. That is a proposed workflow, not an already configured integration.

Do not assume the Cloud container has the validated A100 or silently run Qwen on CPU/another device as equivalent G0 evidence. Keep actual GPU measurement in the pinned Modal execution environment unless a new contract is explicitly validated.

## 15. Recommended next bounded task

First establish a reliable Cloud continuation point:

1. Verify the actual repository/branch/SHA and imported-file checks.
2. Read the current status, safeguards and original protocol/rubric.
3. Report which evidence is accessible locally and which requires Modal; do not claim to audit tensors that are absent.
4. Confirm G0 remains scoped and G1 remains pending.
5. Prepare a concrete G1 readiness assessment and blinded annotation workflow, without reading or exposing the gold key for independent labeling, filling real labels, contacting annotators or claiming agreement.
6. Identify owner inputs needed for independent annotation and any future Modal credential setup.
7. Commit proposed code/document changes on a reviewable branch or provide a PR according to the task's configured workflow. Preserve historical evidence and do not merge policy changes implicitly.

Do not broaden this into a fresh literature review, large benchmark build, Stage 1 feature extraction or confirmatory run unless the user explicitly changes the task and the relevant gates allow it.

## 16. Reporting requirements for future work

Every major research report should state the gate and scoped status, exact commit/contract/run IDs, evidence locations and accessibility limits, preserved failures, protocol/numerical impact, measured resource use and remaining budget if one is set, and the next allowed action.

Separate observed results from hypotheses and proposed work. Do not equate a command exit code with scientific success. Do not claim the missing historical experiment was exactly reproduced, G0 proved H2/H3, G1 is complete, or Cloud/Modal access works without verifying it.

## 17. Copy-ready startup prompt for ChatGPT or Codex Cloud

```text
Continue the Anticipatory Execution project from the existing research state.

Repository: https://github.com/usecommon/anticipatory-execution (private).
Branch: main. Initial research import: 1bed4fa11a0a88b02b92fd1ee7d21337147d40ec.
Read docs/CHATGPT_CODEX_CLOUD_HANDOFF.md, README.md, AGENTS.md, the current v0.5 STATUS/report, RESEARCH_SAFEGUARDS.md, and the original protocol/rubric before proposing research changes. Record the actual checkout SHA.

Frozen thesis: “Do not predict what the user will type next. Predict what work will not need to be undone.”

Current state: G0 PASS only for canonical-v0.5's enforced Qwen/A100-SXM4-40GB/FP32/eager/[1,128]/serial/no-cache contract. Two Modal containers passed 8,427 checks each and all 155 cross-container cases matched bitwise. Native shape/cache failures remain preserved. G1 is pending; Stage 1 remains blocked. No confirmatory extraction is authorized.

Do not restart the project, broaden its novelty claims, weaken tolerance, silently truncate/exclude examples, mix numerical feature versions, reuse affected old calibration as neutral, or alter frozen endpoints. The fix may change or eliminate the measured internal-state advantage; report that honestly. B1/B2/M must later use matched extraction settings.

First run python3 scripts/verify_import.py and inspect current state. This is a CPU-only continuation audit, not authorization for GPU jobs or research extraction. Determine which raw artifacts are absent from Git and require Modal. Desktop credentials are not inherited by Cloud.

Then prepare a concrete G1 readiness assessment and blinded annotation workflow under the frozen rubric. Do not fabricate or complete independent annotations, use the owner gold key as labeling evidence, expose it to annotators, contact anyone, or claim G1 passed. List the owner inputs needed to obtain valid independent annotations.

Preserve the existing code/evidence hashes and all failed attempts. Version future changes. Report completed work, evidence, uncertainties, blockers, numerical/protocol implications and the next allowed action. If this is a ChatGPT conversation without repository access, use the attached handoff as context and state that limitation; do not claim to have inspected the private repo or launch a Cloud task without the user's request.
```
