# Anticipatory Execution — Codex Handoff

## Frozen thesis
**Do not predict what the user will type next. Predict what work will not need to be undone.**

Anticipatory Execution tests whether an agent can identify work inferred from incomplete user input that will remain useful after the full instruction arrives, and safely begin reversible work before submission.

## Scientific question
Do temporal and cross-layer internal-state dynamics of a **frozen autoregressive foundation model** predict future action-semantic non-revision beyond:
1. the observed prefix,
2. observable output signals, and
3. a single hidden-state representation?

Do not claim novelty for incremental intent prediction, pre-end-of-turn understanding, hidden-state early decisions, early generation/tool use, or speculative execution. The candidate contribution is **action-level future non-revision + frozen foundation-model dynamics + incremental-value testing + risk-aware execution**.

## Current state
- Prior-art review: `anticipatory_intent_literature_review_v0_3.docx`
- Protocol: `anticipatory_execution_preregistered_protocol_v0_1.docx`
- G0 instrumentation: **BLOCKED in originating ChatGPT environment; not passed**
- G1 pilot package: **BUILT; not passed until two independent annotators achieve Cohen's kappa >= 0.70**
- Confirmatory execution: **DO NOT RUN YET**

## Model hierarchy
- Naive — prevalence / prefix length
- B0 — prefix text/embedding + length/completeness
- B1 — B0 + final-layer probabilities, entropy, margins, surprisal, persistence, argument completeness
- B2 — B1 + one frozen hidden-state representation
- M — B2 + temporal/cross-layer internal dynamics

Primary scientific endpoint:
`DeltaNLL(B1->M) = NLL(B1) - NLL(M)`

H2 requires the locked confirmatory 95% utterance-cluster-bootstrap CI to be entirely above zero **and** >=1.0% relative NLL improvement. H3 applies the same rule to B2 vs M.

## Immediate Codex objective
Complete **G0** and **G1**. Only then begin Stage 1 development work.

# G0 — Qwen instrumentation QA

Primary model: **Qwen2.5-7B-Instruct**, frozen.

Read first:
- `aeb_g0_runbook.md`
- `aeb_g0_qwen_qa_harness.py`
- `aeb_g0_requirements.txt`
- `aeb_execution_status_g0_g1.md`

### Historical blocker
Previous Qwen experiments found sequence-length sensitivity/suffix-invariance failures. Repeats, reloads, fixed-shape content changes and mask controls were stable; a later diagnostic found **24/80 sequence-length-extension comparisons outside tolerance**. Do not hide, waive, or tolerance-away this issue.

### First actions
1. Inspect the existing environment and repository before changing anything.
2. Check for existing Modal configuration/profile and reuse it if authenticated.
3. Record exact model/tokenizer revisions, PyTorch/Transformers versions, GPU, dtype, attention implementation, padding side, position IDs, cache settings and seeds.
4. Reproduce the historical sequence-length issue.
5. Run the complete deterministic QA harness.
6. Save raw outputs, logs, checksums and environment metadata.
7. Classify every test PASS / FAIL / DIAGNOSTIC.
8. If modifying the harness, version it and write a change log. Never weaken a failing test just to obtain PASS.

Required checks include exact repeat, reload equivalence, batch-vs-singleton, fixed-shape masked padding, token alignment, masks, position IDs, cache/no-cache where mathematically expected, sequence-length extension, hidden-state consistency and saved-state/checksum equality.

**G0 PASS:** all deterministic QA tests pass or deviations have a principled, documented numerical tolerance that does not invalidate cross-prefix comparisons.

## Modal
Prefer Modal because the earlier pilot ran there. Inspect installed Modal tooling/skills before inventing commands. Authenticate the existing profile if possible. Start with a small GPU QA job; do not scale extraction until G0 passes.

# G1 — Annotation validity

Files:
- `aeb_g1_annotation_pilot_200.xlsx`
- `aeb_g1_annotation_rubric_v0_1.docx`
- `aeb_g1_pilot_gold_key.jsonl`

Pilot design: **200 items / 50 tasks / 12 domains / two independent annotators / third adjudicator for disagreements.**

Primary label:
`C_i,t = 1` iff candidate action A_i inferred at prefix t produces work reusable in the final correct task **without material re-execution**.

This is NOT “did we guess the final intent?”

Procedure:
1. Keep both annotators blind to the gold key and each other.
2. Complete Annotator_A and Annotator_B independently.
3. Use workbook adjudication sheet to compute Cohen's kappa.
4. Require **kappa >= 0.70**.
5. Adjudicate only after independent labeling.
6. If kappa < 0.70, revise the rubric/ontology and run another development pilot.
7. Do not change the rubric after confirmatory labeling begins.

The gold key is an owner/development reference only and cannot substitute for independent annotation.

# After G0 + G1 PASS

## Stage 1A — Controlled sanity benchmark
Reproduce incremental-understanding behavior on CLINC/inCLINC-style completed-word prefixes. This is a sanity check, not the primary endpoint.

## Stage 1B — Anticipatory Execution development benchmark
Implement:
- completed-word prefix generation;
- candidate-action generation with strict no-future-information boundaries;
- canonical action graphs;
- B0/B1/B2/M extraction;
- development-only regularized probes;
- calibration;
- per-utterance paired loss analysis;
- simulation-based power analysis;
- compute/runtime estimates.

Prespecified internal features include hidden-state displacement, cosine change, velocity, acceleration, curvature, rolling stability, trajectory extrapolation residual, cross-layer agreement, pairwise JS divergence, entropy slope, late-layer convergence, prototype geometry and lens-derived entropy/stability.

Attention/KV features remain exploratory unless G0 validates them before protocol freeze.

# Hard constraints
1. Model weights remain frozen.
2. Lightweight probes/calibrators train only on development data.
3. All prefixes of one utterance remain in one split.
4. Near-duplicate/template families remain grouped.
5. No suffix/final-instruction leakage to prefix-time predictors.
6. No feature/layer/threshold selection on confirmatory data.
7. No confirmatory reruns to chase significance.
8. No hypothesis-favorable exclusions.
9. Consequential actions are simulated only.
10. Preserve negative results.

# Interpretation
- B1 ~ naive: benchmark/label may not expose predictable non-revision.
- B1 strong; M ~ B1: product may work; internal-dynamics thesis unsupported.
- M > B1; M ~ B2: internal representations help; trajectory novelty unsupported.
- M > B2 but fails replication: model/dataset-specific.
- M > B2 and replicates: supports central scientific thesis.
- Prediction works but latency advantage vanishes at matched compute: scientific result without operational value.
- Benefit only at unsafe speculation rates: restrict to cheap/reversible work.

# Product objective
Do **not** optimize for earliest final-intent prediction.

Optimize **useful pre-execution / post-submit latency saved**, subject to bounded future revision, wasted compute, wrong visible actions and consequential error.

The user may initially perceive the experience as type-ahead. The underlying capability is anticipatory execution.

# Required Codex status format
For every major run report:
1. Gate
2. Status: PASS / FAIL / BLOCKED
3. Exact evidence/artifacts
4. Unexpected findings
5. Protocol impact
6. Cost incurred / remaining cap if applicable
7. Next allowed action

# First instruction to Codex
> Read this README, the preregistered protocol, G0 runbook, and execution-status file. Continue from G0 instrumentation QA. Use Modal if authenticated access exists. Reproduce the historical sequence-length issue before trying to resolve it. Do not run confirmatory extraction. Preserve every failure and create a versioned evidence bundle. Keep G1 as a separate labeling-validity workstream; the supplied gold key is not independent annotation evidence.
