# Decision-time and reuse contract — development v0.1

User authorization: acceptance of the fresh-eyes council recommendations. This implements the next bounded development specification; it does not amend the frozen thesis, primary binary rubric, H2/H3 endpoints, effect thresholds or human G1. Existing results retain their original target and inputs.

## Decision stages

| Stage | What exists at prediction | Eligible predictor input | Evaluator-only evidence |
|---|---|---|---|
| before_execution (primary stage for the next adapter) | Observed prefix, independently available context and a proposed typed action; that action has not executed | Prefix, prefix-time system/tool schema, declared observable environment metadata, typed action and arguments | Candidate execution result, receipt, future input/state, final-task specification, reference answer, usefulness judgment |
| after_preparation (separate diagnostic stage) | A specified preparation has finished; a subsequent decision is pending | Above plus that preparation's actual available product, with recorded production cost | Future input, later execution receipts/results, final-task specification and labels |

A cheap proposal is not the proposed action's execution result. Proposal construction and any prior preparation cost are already paid at decision time and must be retained. For before_execution, candidate outcomes must not enter any predictor, including B0/B1/B2/M. Every nested model has the same available context, candidate and stage; internal models add only their declared state features. Explicit content projection, not a field blacklist, defines the payload. Content provenance also needs audit: correct field names cannot establish that a suffix was never seen.

The existing diagnostic includes candidate_action plus work_product. Preserve it as reuse scoring of already-produced preparation. Do not remove its work-product input, refit it, or reinterpret it as a pre-execution decision experiment.

Record logical event order (proposal <= decision < candidate execution for before_execution), byte hashes, model/session/sampling provenance, and the preparation/candidate identity. Clock values alone do not prove causality. Context hashes refer to the exact available input serialization. Legitimately observable state may change early behavior; suffix-isolation checks hold that state and prefix fixed.

## Usefulness and execution evidence

The frozen binary target asks whether the action output can be reused in the final correct task without material re-execution. Keep these separate:

- final_task_correct: satisfaction of independently specified final requirements;
- observed_consumption: receipt units read by the final executor;
- verified_contribution: units with traceable contribution to a correct output;
- reuse_witness: a valid completion using early work with the required provenance/freshness;
- material_reexecution: what target-specific work had to be discarded/recomputed, including why;
- binary_usefulness / fractional_utility: rubric judgments, never computed directly from consumed fraction.

A positive execution witness can support reuse capacity; lack of a witness is not proof of non-usefulness. Reading an irrelevant artifact is not contribution. Useful work deliberately ignored is a policy failure, not automatic label 0. Narrowing can preserve a subset of broad retrieval. A changed parameter can invalidate a result while leaving some preparation useful.

Do not invent a universal percentage or time threshold for “material.” Keep unresolved judgments about parameter substitutions, drafts and generic procedures explicit for rubric alignment. The existing rubric remains authoritative; no software checker closes these ambiguities. Class 1 preparation, conditional work and Class 3 drafts remain in scope conceptually even where the first adapter cannot execute them. No Class 4 external commits.

## Field and evidence contract

contract.py implements a strict software receipt envelope for before_execution fixtures. Its accepted status is STRUCTURE_VALIDATED_ONLY, never dataset admission or a usefulness label. Required fields have exact types, schema version, nonempty values, content digests, and matching receipt links. Empty dictionaries fail. The provenance source, environment and task references are declarations whose factual validity still requires independent verification.

Separate environment-at-decision, final environment, decision-visible context, candidate request, execution receipt, consumption trace, final-task specification and task-check result. Derived public tasks record authored transformations; original source identity alone does not validate an adaptation. The envelope's timestamp/order and hash checks do not prove semantic equivalence, public licensing, human independence or source truth.

## Costs and estimands

The next engineering adapter assesses contract violations and evidence completeness within its declared supported operation, not population utility. Record screened -> eligible -> selected -> proposed -> executable -> resolved -> successful counts without collapsing abstentions or missingness into negatives.

A later evaluation must freeze its target population, task/family weighting, independent-family sample-size/precision assumptions, risk threshold/calibration and reporting before scoring. Conditional check-group bootstrap intervals keep fitted models/labels fixed; they do not cover training/proposer/measurement variation. Representative and challenge collections remain separate. All old check partitions remain unchanged.

S1 needs separate measurements of post-submit latency and applicable proposal, preparation, prefix processing, probe, execution, wasted-work and fallback costs. Offline reference/oracle costs are recorded separately; runtime validation needed by the deployed policy counts toward that policy's budget.

## Review before more probes

First review independent task semantics, provenance/isolation failures and rubric-versus-execution disagreements on the bounded adapter. Passing software checks is insufficient. Full B1, fair action conditioning and temporal controls must be specified and validated before a full comparison. Human G1 remains deferred for exploratory work and required before confirmatory labeling/final freeze. Confirmatory extraction is prohibited. Preserve all failed attempts and old labels alongside any new evidence.
