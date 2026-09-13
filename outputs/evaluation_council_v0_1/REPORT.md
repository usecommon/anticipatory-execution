# Fresh-eyes evaluation council — v0.1

**Verdict: continue measurement development; the present evidence does not yet constitute a thesis evaluation. Preserve the negative diagnostic. Before building the public-source adapter, define the decision time and how execution evidence relates to the frozen usefulness rubric.**

The council found no demonstrated arithmetic error, split leakage or label corruption in the inspected material. This is a limited review finding, not certification that none exists. The major findings concern what the current evaluation can establish and what the next design must make explicit. Many limitations were already disclosed correctly; the review does not recast them as undisclosed failures.

Reviewed commit: `9eaea40990db6f6fdecf8067917189f3bfbd3448`. Three AI reviewers received separate fresh contexts for statistics, measurement validity and thesis identification. The coordinator independently inspected the cited code and reconciled their findings. A second-round challenge tested the proposed next step. These are separate AI reviews, not independent human validation, a diverse-model replication, blinded outcome review or human G1. Reviewers were allowed to see prior negative results. No owner gold key, human submissions or confirmatory data were accessed. No extraction, fitting, new judging or dataset execution occurred.

## Prioritized findings

| ID | Priority and classification | Finding | Consequence |
|---|---|---|---|
| F1 | P1 — confirmed scope limitation | Predictors receive the already-produced work product. | Specify pre-action versus post-preparation prediction before interpreting scores as a decision to start work. |
| F2 | P1 — unresolved measurement design | Observed consumption does not equal the capacity for useful reuse. | Receipts supplement the rubric; they do not automatically create binary labels. |
| F3 | P1 — confirmed scope limitation | The toy fresh reference is independent of the cache, not independent of supplied task keys. | A real task checker must detect shared target/constraint mistakes. |
| F4 | P1 — confirmed identification limitation | Strong B1 is incomplete; the additive probe lacks action–dynamics interactions and mixes temporal/current geometry. | The negative diagnostic remains informative only for its tested features and learner. |
| F5 | P1 for risk claims; P2 for development — sampling limitation | Scoring conditions on proposals, review selection and resolved judgments; public check has zero negatives. | No opportunity-level risk, natural source effect or deployment claim follows. |
| F6 | P2 — uncertainty/provenance limitation | Bootstrap holds trained models and judgments fixed; known groups do not exhaust semantic/session dependence. | Report conditional uncertainty and preserve generation provenance in the next batch. |
| F7 | P2 — prospective validity risk | Restoring omitted public-task context or choosing only easy executable operations can change the task. | Explicitly distinguish original evidence, adaptations and adapter-supported scope. |
| F8 | P2 before admission; P3 today — inventory limitation | Empty dictionaries satisfy current field-presence checks. | The structural inventory must not become a schema/admission validator. |
| F9 | P3 — continuation documentation ambiguity | Historical status fields are still labeled current in some continuation pointers. | Add a versioned consolidated status in later maintenance; preserve historical evidence. |

P1 here means resolve before the corresponding broader inference, not that exploratory software development must stop. No new gate or protocol amendment is enacted by this report.

### F1. Fix the decision-time definition first

[prepare.py line 15](../exploratory_comparison_v0_1/prepare.py) constructs candidate text from both the candidate action and its work product. All learned models share those features. This is fair within the comparison and is not evidence of future-suffix leakage. It can evaluate whether an already-generated preparation remains useful. It cannot automatically support a claim that the policy predicted whether to begin producing that preparation.

**Required clarification for the next design:** record what has already executed at the prediction timestamp and which artifact fields exist then. If preparation has already happened, name that decision stage and count preparation cost. If the decision is before execution, later receipts/results remain evaluator-only; do not silently delete historical work-product features or relabel the old study. System instructions, tool schemas and environment facts need explicit availability provenance. The current extraction used plain prefixes, while proposers had no task-specific schemas/state ([preflight README lines 7 and 29](../exploratory_preflight_v0_1/README.md), [shared-policy README line 50](../shared_policy_pilot_v0_1/README.md)).

**Counterargument retained:** inexpensive preparation may legitimately precede a more expensive action. The remedy is stage-specific accounting, not a blanket prohibition on work-product features.

### F2–F3. Validate the construct as well as the mechanics

The [original rubric](../checkpoint_ai_judge_v0_1/ORIGINAL_RUBRIC.txt), lines 4–12, asks whether work **can** be reused without material re-execution. The [fixture](../measurement_quality_v0_1/measure.py), lines 27–41, measures the execution path chosen by its cache policy. A useful result can be ignored; reading a result need not make it necessary; broad work can partially survive narrowing. The existing plan correctly acknowledges these distinctions and creates no research labels.

The fresh lookup reference uses the same supplied `final_keys` and final dictionary as the execution path. It detects stale/corrupt cache values but cannot expose a shared wrong-target or missing-constraint interpretation. This is acceptable for its declared unit-fixture role, not independent task-semantic validation.

**Next acceptance evidence:** separate final correctness, verified consumption, reuse-capacity judgment and material re-execution. Derive final required behavior from a separately specified task contract/environment, not from candidate-selected keys or executor output. Include wrong target, omitted constraint and internally consistent but incorrect fresh output. Preserve a difference between policy failure to reuse and evidence that work cannot be reused. An execution witness may support a positive reuse judgment; failure to observe reuse does not alone prove a negative.

### F4. Preserve the narrow negative result; specify fair action-conditioned controls

The [comparison README](../exploratory_comparison_v0_1/README.md), lines 53–61, correctly disclaims full B1/H2/H3. Action probabilities, semantic completeness and full surprisal remain missing. Fixed projected snapshots and three word-boundary positions also limit sensitivity.

[fit.py lines 21–38](../exploratory_comparison_v0_1/fit.py) concatenates candidate/text/numeric features in logistic regression. [features.py lines 12–22](../exploratory_comparison_v0_1/features.py) derives dynamics from prefix-only states. At one identical prefix, the internal-feature contribution to log-odds is identical across candidate actions. Candidate main effects can differ, and joint refitting can change them, but the model has no explicit candidate-by-dynamics interaction. The internal feature block therefore cannot express an action-specific response to a trajectory.

D-dynamics also adds temporal features and current cross-layer cosines together. A hypothetical gain would not isolate temporal ordering. The preserved protocol already includes within-utterance order shuffling and residualization against prefix length/B1 observables (original protocol DOCX, paragraphs 278–279, counting all `w:p` elements in document order). These controls remain future work, not a newly imposed endpoint.

**Next design:** specify comparable action-conditioning capacity, strong observable/context inputs, snapshot controls and search budgets before new scores. A single global regularization parameter can change shrinkage of existing and added feature blocks; more dimensions are not an exhaustive test of representations. Do not search retrospectively for a positive result. “Beyond prefix” should be interpreted as incremental predictive utility under defined baselines/learners/resource conditions. Fixed deterministic states are functions of their exact input/context; no information-theoretic novelty beyond that complete input is established. This clarifies interpretation without changing the thesis or endpoints.

### F5–F6. Name the denominator and the uncertainty

The [selection code](../checkpoint_human_pilot_v0_1/assemble.py), lines 31–42, balances the reviewed sources and prefers distinct tasks before extra checkpoints. The [metric](../exploratory_comparison_v0_1/fit.py), lines 9–15, averages resolved scored checkpoints within each task, then tasks equally. The result is selected-proposal, reviewed, resolved-label, task-weighted loss; it is not the expected utility of all scheduled opportunities or a natural source mixture.

There are 900 scheduled opportunities, 260 proposals and 200 current judgments. The scored check sample has 32 cases, 28 tasks and 22 groups, with 30 positives and two negatives; all 16 public cases are positive. Abstentions, ineligible checkpoints, unjudged products and unresolved judgments stay separate. Later word checkpoints condition on instruction length and alter source composition. No reroll of the old split is warranted.

[fit.py lines 50–59](../exploratory_comparison_v0_1/fit.py) bootstraps check groups while keeping models, tuning, labels and representations fixed. These intervals capture conditional check-group sampling variability, not all uncertainty in the method. The unresolved-zero/one sensitivities do not change check labels. Known exact/template grouping is useful but does not certify absence of semantic overlap, source memorization or shared generation-session effects; the existing reports acknowledge these limits.

**Next design:** state the conditioning events and target population, freeze source universe/support/sampling/groups before scoring, and size at the independent-family level using explicit prevalence, unresolved-rate and precision assumptions. Keep representative sampling separate from controlled challenge cases. Log scheduled, eligible, proposed, executable, resolved and successful counts, plus generation session/model/sampling provenance. Never replace failures until coverage looks favorable. This council does not adopt a new sample size or numerical acceptance threshold.

### F7. A public-source adapter must not become a different benchmark silently

The [BFCL audit line 29](../bfcl_public_pilot_v0_1/ADAPTER_AUDIT.md) explains that first-turn text omits original state and later dialogue. Supplying authored state would test a public-derived adaptation, not restore an official task merely by using its wording. A lookup-only adapter may also select disproportionately tractable or reusable tasks.

**Next design:** retain original-versus-authored provenance per environment field; pin the evaluator and source; declare supported operations and screen the full frozen denominator. Task-specific facts may enter early execution only if they would actually be available then. A suffix-isolation check must hold prefix-time environment/context fixed; deliberately changing available environment facts is allowed to change early behavior. Unsupported tasks remain visible and unscored/unresolved as appropriate, not negative or replaced.

### F8–F9. Small process issues, with bounded implications

[audit.py lines 7–11](../measurement_quality_v0_1/audit.py) only checks whether each evidence field is a dictionary; `{}` qualifies. This does not change today's zero-ready result, but its readiness field name is stronger than its validation. A later admission validator should require schema version, typed content, provenance and valid linked receipts, and reject empty containers. The original inventory remains preserved.

The root README calls the G0 closure status machine-readable current status, while that historical file says development extraction is false. The cloud handoff still contains a bold “Current state” sentence saying no development extraction occurred, below newer updates that correctly report it. This is a navigation ambiguity, not evidence that runs were concealed. Recommended maintenance: a consolidated current status linking immutable phase reports, with historical prose clearly labeled by phase. No historical status was rewritten during this review.

## Council disagreement and resolution

**Strongest objection to measurement-first implementation:** an excellent cache adapter could become the research target by convenience, excluding conditional preparation, parameterized drafts and other work central to the thesis. More instrumentation alone would then validate a narrower construct.

**Resolution:** before code, write a short decision-time/construct contract. Use one small adapter to test that contract's limited domain, not to replace the thesis, certify the 200 labels or create a new efficacy benchmark. Specify the full-B1 interface in parallel. The council does not recommend another AI rejudging round, a larger synthetic batch, tuning the old probe, or immediate full-scale human labeling as a way to improve scores.

Human review remains useful for rubric reproducibility and executable-evidence alignment; it does not guarantee truth or favorable results. The formal human G1 gate remains pending under the existing amendment. This AI council cannot satisfy it.

## Recommended next bounded deliverable

1. **Decision-time and construct contract:** stage being predicted; already-paid work; permitted features/context; action identity; interpretation of material re-execution under the existing rubric. Open judgments stay explicit rather than being silently operationalized.
2. **One public-source adapter specification:** source/environment provenance, independently specified final-task checker, supported domain, full screened denominator and candidate/receipt isolation.
3. **Discriminating development cases selected before new scores:** useful work deliberately ignored; consumed-but-unnecessary work; partial narrowing; wrong entity with equal output; stale dependencies; target-specific preparation requiring revision; shared wrong-target/omitted-constraint checker errors. Keep software counterexamples separate from sampled research cases.
4. **Observable/snapshot comparison specification:** real surprisal capture and G0 bridge plan, action probability/completeness/persistence, stage-matched feature access, fair interaction capacity and already-prescribed temporal controls. Do not call software formula checks full-B1 readiness.
5. **Predeclared review decision:** assess evidence completeness and rubric disagreements before additional probes. Preserve all old versions and negative outcomes. Later S1 needs its own matched-risk/budget study including applicable feature, proposal, early-work, wasted-work and runtime overhead; symbolic lookup savings are not measured latency.

These are review recommendations for the next development package. No implementation change, new label, experiment, protocol amendment or confirmatory authorization is enacted here.

## Review record

[Reviewer summaries and second-round challenge](REVIEWER_RECORD.md) distinguish first-pass conclusions from coordinator synthesis. [STATUS.json](STATUS.json) records scope; [SOURCE_HASHES.json](SOURCE_HASHES.json) pins the main reviewed artifacts. Citations refer to the reviewed commit; line numbers are stated in prose because Git-relative Markdown links do not consistently support line anchors. No external literature or current-product claims were needed for this repository audit.
