# First exploratory diagnostic comparison — v0.1

**Result: the tested internal-state features did not improve on the available-output diagnostic. Text plus candidate features had the lowest check loss under current labels.** This is a preserved negative diagnostic result, not a rejection or confirmation of H2/H3. The full strong B1 baseline is incomplete, the sample is small and AI-labeled, and the check split has just two negative cases.

The [plan](PLAN.md) and code were frozen before feature construction/fitting. Foundation-model extraction and weights were unchanged; only CPU feature derivation and lightweight diagnostic probes ran. Human G1 remains pending/deferred. Public release/adaptation admission remains pending. No confirmatory extraction or evaluation occurred.

## Current-label results

Lower task-averaged NLL and Brier are better. The check set has 32 cases, 28 tasks and 22 connected template groups: 30 reusable, 2 non-reusable. Fit uses 120 resolved cases (105 positive/15 negative); tune uses 40 (36/4). Eight unresolved cases are preserved and receive predictions but are not fitted/scored in this scenario.

| Diagnostic model | Check NLL | Check Brier | Selected C |
|---|---:|---:|---:|
| Prevalence | 0.27495 | 0.06973 | — |
| Text + candidate | 0.20553 | 0.06418 | 10.0 |
| + available output signals | 0.24177 | 0.06683 | 1.0 |
| + one snapshot | 0.32524 | 0.09255 | 0.1 |
| + multiple snapshots | 0.33079 | 0.09498 | 0.1 |
| + temporal/layer geometry | 0.32225 | 0.09246 | 0.1 |

The output-to-dynamics NLL gain is negative: the dynamics model is worse. Adding temporal/layer geometry to the multiple-snapshot control gives a small gain, but its exploratory interval spans zero. No layer, projection, feature set or split was changed after observing this result.

| Paired comparison (positive gain favors added signals) | Task-mean NLL gain | Exploratory 95% group-bootstrap interval |
|---|---:|---:|
| D_text->D_output | -0.03624 | [-0.07592, 0.00148] |
| D_output->D_dynamics | -0.08049 | [-0.15253, -0.01450] |
| D_multisnapshot->D_dynamics | 0.00853 | [-0.00328, 0.02106] |

These 2,000-replicate group-cluster intervals are the predeclared diagnostic summary, not the frozen confirmatory endpoint or a corrected family of hypothesis tests. They do not overcome the small, selected and AI-labeled sample.

## Label sensitivity

Each scenario is independently refitted with the same frozen feature definitions and C grid. Original labels remain unchanged. Positive output→dynamics gain would favor internal features; every scenario here has a negative gain. Text versus output ordering changes with label assumptions, and the small multisnapshot→dynamics gain reverses when ambiguous cases are excluded. These scenarios are not independent replications.

| Label scenario | Fit/tune/check cases | Text NLL | Output NLL | Dynamics NLL | Output→dynamics gain |
|---|---:|---:|---:|---:|---:|
| current_resolved | 120/40/32 | 0.20553 | 0.24177 | 0.32225 | -0.08049 |
| prior_overlap_replaced | 122/40/32 | 0.22134 | 0.21728 | 0.33967 | -0.12238 |
| ambiguity_excluded | 96/26/25 | 0.15363 | 0.14988 | 0.28001 | -0.13013 |
| unresolved_zero | 127/41/32 | 0.24039 | 0.27444 | 0.35700 | -0.08256 |
| unresolved_one | 127/41/32 | 0.20329 | 0.24048 | 0.32038 | -0.07991 |

The prior-label scenario replaces only the 65 exact overlapping earlier judgments. Ambiguity exclusion is explicitly a selected-subset sensitivity, not a preferred cleaned dataset. The unresolved-zero/one cases are stress assumptions, not new judgments. The check labels remain the same in those two extremes; their prediction changes arise from altered fit/tune labels.

## Public and synthetic coverage

**All 16 public check cases are positive. Both negative check cases are synthetic.** The public check slice cannot measure detection of non-reusable work or a false-speculation rate. Source differences below are descriptive and confounded by source/task composition and labels; they are not a causal public-versus-synthetic experiment.

| Source | Check labels (+/−) | Text NLL | Output NLL | Dynamics NLL |
|---|---:|---:|---:|---:|
| public_bfcl | 16/0 | 0.01900 | 0.08898 | 0.19024 |
| synthetic | 14/2 | 0.39206 | 0.39455 | 0.45427 |

## What was and was not tested

D-output uses vocabulary entropy, probabilities/margins, short-window persistence, Jensen–Shannon divergence and entropy change. It lacks action probabilities, validated argument completeness and full token surprisal. TF-IDF text features and lexical cues are not a validated semantic-completeness model. It must not be renamed full B1.

Snapshots use 64 fixed random projections per layer; temporal geometry uses only the last three completed-word prefixes. These diagnostics do not exhaust raw-state information, temporal horizons, action-conditioned interactions or the protocol's projected-action/lens feature families. The small fit sample and feature dimension may affect generalization. They are limitations of this negative result, not grounds to tune until an advantage appears. All learned models include the same prefix-known candidate text and shared lexical/class features.

This diagnostic uses L2 liblinear logistic regression, as prospectively recorded, rather than the protocol's primary elastic-net classifier. Fit-only TF-IDF/scaling and equal total training weight per task precede tune-only C selection; there is no check-based fitting or threshold selection. No matched-risk/compute policy or systems experiment was attempted. All cases have prior development exposure and none may be relabeled as untouched confirmatory data.

## Verification and preserved failure

All 200 case feature rows passed, derived from 548 unique, hash-verified saved tensors. All six analytic formula checks passed. Feature/plan/source hashes were frozen before fitting. All candidate fits converged without warnings. Changing check labels left fitted models, vectorizers, selected C and predictions exactly unchanged. An independent standard-library verifier reproduced every reported overall and source-slice task-mean NLL/Brier and verified the label scenarios, tune selections and coverage.

The first attempt failed only when serializing a NumPy int64 to JSON after fitting. Its log and traceback remain preserved. Recovery reused the exact feature table and unchanged fitting function; NumPy-to-Python scalar conversion paths are recorded. No definitions or labels changed to recover a pass. See [FAILURES.md](FAILURES.md) and [RECOVERY_AUDIT.json](RECOVERY_AUDIT.json). CPU resource bounds and package versions are in the plan/raw result; no new GPU run occurred, and no metered billing total was queried.

[Raw predictions, fitted parameters, grid and metrics](run_20260913T013948081119Z/RESULT.json) · [Feature table](run_20260913T013948081119Z/FEATURES.json) · [Pre-fit freeze](run_20260913T013948081119Z/PRE_FIT_FREEZE.json).

## Next research decision

This completes the first bounded comparison and sensitivity report, reaching the amendment's planned point to revisit human review and measurement validity. Human G1 is not passed, and remains a hard gate before confirmatory labeling/freeze. Further AI-only exploratory work remains distinct under the amendment.

Before broader hypothesis testing, resolve the missing strong-B1 signals and the lack of public negative-case coverage using a prospective, versioned development design. Do not reroll this check split or relabel cases to improve internal-model results. Keep the original negative results, uncertainty and publicly reproducible source requirements visible. The frozen thesis remains unchanged.
