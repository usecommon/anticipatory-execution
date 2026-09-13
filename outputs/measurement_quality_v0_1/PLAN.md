# Measurement-first work package — v0.1

Authorization: the user agreed to prioritize measurement after the first negative AI-labeled diagnostic. Success means a more credible measurement process, whether scores rise, fall or stay unchanged. The frozen thesis, action-usefulness definition, scientific endpoints and original negative result remain unchanged. This is a prospective development work package, not a revised confirmatory protocol or waiver of human G1. No further probe search is launched by this package.

## Priority 1: define and capture missing observable measurements

| Gap | Concrete implementation requirement | Acceptance evidence before using the full-B1 name |
|---|---|---|
| Token surprisal | For independently tokenized observed prefix IDs z[0:n], score z[i] from active logits[i-1] for i=1..n-1. Preserve count, sum and mean NLL; first token unscored; n=1 mean is null. | Analytic shift/shape checks, a versioned capture that retains these summaries from full active logits, and a bridge showing unchanged legacy hidden/logit outputs under the same G0 contract. Current saved last-position logits are insufficient; do not reconstruct by pretending word-boundary tokenizations are nested. |
| Action probabilities | Freeze the action vocabulary, argument normalization, prefix-only candidate policy and probability measurement interface. Specify exactly what event each probability estimates. | Blind prefix replay, valid normalized probabilities over the declared support, observed-output provenance and no use of utility labels/final instruction to construct the feature. Vocabulary next-token probabilities cannot be renamed action probabilities. This design decision remains open; no substitute is silently adopted. |
| Argument completeness | A typed, prefix-known action schema with required/optional slots and present/unknown/ambiguous states. | Counterexamples in which a missing or ambiguous slot is not treated as complete; suffix-only slot values remain unavailable. Lexical endings and punctuation alone do not satisfy this requirement. |
| Persistence | Track the same canonical action/argument hypotheses across declared checkpoints; distinguish equivalent forms, revisions and unavailable observations. | Tests of equivalent aliases, changed targets, missing hypotheses and parser version changes. Short-window top-token persistence remains a separate diagnostic. |

The surprisal formula is implemented and software-tested in this package; it has not been applied to fresh foundation-model outputs. Other interfaces are specified, not implemented or certified. Before new model runs, preflight the complete actual inputs. New prompts/schemas may exceed 128 tokens and require a new outcome-independent width plus G0 validation. Never truncate to fit. B1/B2/M must share the same numerical configuration and any new observable inputs. Full-B1 readiness requires all declared components and their QA, not an improved score.

## Priority 2: executable reuse evidence

Do not execute free-text candidate scripts directly. Admit a narrowly supported typed operation only after its adapter, environment snapshot, source version and public reproduction terms are established. Use read-only or simulated work; no external Class 4 commits.

For each admitted case, retain: source/task identity and fixed full instruction (evaluator only); exact observed prefix; typed candidate/arguments and their prefix provenance; initial/final environment versions; early execution receipt with result and units/cost; final task checker; actual consumption trace; fresh-reference execution; freshness/dependency checks; failures and unresolved evidence.

Measure separately: final task correctness, verified consumption of early work, disposable/unused work, required re-execution, and observed costs. A final answer can be correct after discarding all early work. Equal outputs can concern different entities. A broad retrieval may remain useful after narrowing even when only part of it is consumed. Observed consumption is also not proof that unused work could never have been useful. These distinctions are required by the original rubric.

The new in-memory lookup harness is **software QA only**. It creates no research binary labels and does not run BFCL tasks. It records symbolic lookup counts, not latency or real compute, and excludes reference-check overhead from those counts explicitly. Its conservative version-token rule is a fixture assumption, not a general freshness oracle. A measured consumed fraction does not replace the rubric's secondary fractional utility or determine its binary label.

Current inventory: all 200 frozen case records lack the proposed structured receipt/environment/trace fields. Their textual work products remain preserved and retain their current labels. This is a readiness gap, not 200 failures or negatives. A real adapter must attach missing evidence explicitly; a synthetic environment must never be presented as the original public environment.

## Priority 3: prospective coverage and reproducibility

Preserve the existing 32-case check partition and its result. Do not move currently negative cases into it, reroll its seed, or rename exposed cases as unseen/confirmatory. The public check slice has 16 positives and zero negatives; it cannot assess non-reusable-action detection. Both sources require outcome-independent task/family grouping and visible uncertainty/missingness.

Before scoring a new development batch, freeze: pinned publicly obtainable sources and licenses/attribution, eligible task universe, fixed sampling rule/seed and batch size, family/duplicate grouping, prefix schedule, candidate policy, measurement contract, supported operation strata, and a reporting/precision plan. Determine sample size from prespecified precision/power assumptions, not model results; no new quota or numerical threshold is adopted in this package.

Use one fixed batch to audit positive/negative/unresolved coverage by source and task family. A deficient batch stays deficient and reported. Do not repeatedly sample until a desired model result or favorable label balance appears. Any subsequent design revision gets a new version and retains the full earlier denominator.

Two distinct collections may be useful: a representative public-source development sample for prevalence/generalization questions, and a controlled challenge set for known target/constraint/freshness changes. Public-derived controlled variants must be labeled as adaptations, and authored variants as synthetic. Challenge-set frequencies cannot estimate natural false-speculation rates; do not pool the two without an explicitly justified weighting/estimand. Actual reuse checks, not the mere presence of a changed intent, determine whether the intervention invalidates work.

## Human-review timing and outcome neutrality

The first comparison reached the planned human-review revisit point. The user now prioritizes measurement development; human G1 remains deferred for this exploratory track, not passed or removed. Once a concrete measurement adapter exists, use a representative sample plus disputed cases to assess rubric/oracle alignment, distinguishing reliability from truth. Under the retained protocol, human G1 remains a hard gate before confirmatory labeling or final freeze. Confirmatory extraction remains prohibited regardless of later G1 status.

Keep the five diagnostic label scenarios, fitted parameters, errors and negative internal-feature results unchanged. New measurements may change labels, prevalence, effects or rankings in either direction. Record disagreements between new executable evidence and old AI judgments; never silently overwrite old labels or treat an improved score as the criterion for a better measurement.

## Next bounded deliverable

Specify one typed public-source adapter and attach a versioned environment/receipt/consumption interface to a small development-only set selected before new scoring. Validate the adapter against correctness/reuse counterexamples and independently inspect its relation to the original rubric. In parallel, prepare the versioned full-prefix surprisal capture/bridge; no new GPU run or confirmatory extraction is launched here. Keep action-probability and semantic-completeness design decisions explicit before claiming full B1.
