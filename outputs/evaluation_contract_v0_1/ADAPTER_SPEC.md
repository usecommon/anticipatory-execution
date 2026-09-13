# Public-source adapter specification — directory enumeration v0.1

Status: specification and structural development screening only. Actual original BFCL environment/tool replay is not implemented or admitted. Local software counterexamples are authored fixtures, not public benchmark outcomes.

## Source and boundary

Use the already pinned BFCL v4 multi-turn-base source at commit 6ea57973c7a6097fd7c5915698c54c17c5b1b6c8, original file SHA-256 1a21a995d06fd6f20ba55de7bced30ef953ec35e998f502ec2ecf4d66ef1c43a. The retained EVALUATOR_CONTEXT.jsonl contains all 200 first-turn adaptations, with initial_state_used and future_dialogue_used false. Do not infer a live filesystem from this text or expose credential-bearing source states. Follow the existing source/license manifest; public adaptation release/admission remains pending.

Chosen engineering operation: read-only directory entry enumeration. This choice is informed by existing development exposure and is not independent research preregistration. Exact directory identity, recursion, hidden-entry inclusion, type constraints, symlink rules and environment provenance must be explicit. No shell execution, host-filesystem inspection, network tool, or natural-language eval is permitted in the adapter.

## Frozen engineering selection rule

Screen all 200 retained first-turn records, without reading AI judgments or model predictions. A lexical candidate contains a token list/listing and a token file/files/directory/directories. This is triage, not proof of task support. Group identical whitespace-normalized full instructions; sort groups by SHA256 of "directory-contract-v1|" plus normalized instruction, select the first at most 8 groups, retain every member of selected groups. Eight is a bounded engineering capacity limit, not a powered efficacy sample. Preserve all screened rows, reasons and duplicates; never replace unsupported selections.

Selected rows require semantic review of the full instruction by the evaluator only. Composite tasks and missing original state remain visibly unresolved/not admitted. The first-turn full instruction stays fixed; later dialogue is neither silently appended nor ignored when claiming an original multi-turn task. Retain original dialogue as evaluator evidence when reconstructing that task. Authoring substitute state creates an explicitly public-derived adaptation with its own version and cannot validate the original record.

For later candidate generation: use the same literal 6/12/18-word schedule, recording complete/not-reached opportunities. Only prefix-time schemas/state actually available in the proposed deployment enter the candidate context. No candidate generation or new reuse scoring is performed by screening.

## Independent final-task semantics

The evaluator records a task requirement separately from the candidate and executor: directory identity, required entries/types/visibility/recursion, permitted alternatives and final environment snapshot. Requirements must be traceable to the fixed final instruction and supported environment, with unresolved interpretations explicit. The executor must not supply its own required target list to the checker.

The checker derives the acceptable final entry set from those requirements and the pinned environment. It checks target identity as well as outputs, catches omitted hidden entries and rejects plausible wrong values. A matching output from a different directory does not establish target-specific work survival. Public task semantics require an independent specification/provenance review beyond matching this envelope.

Record each early operation's request/environment digest, result, dependency versions and execution event. Trace actual reads separately from dependencies that contribute to the required result. Compare fresh-reference task completion with an early-result-assisted completion under the same declared environment. Preserve policy refusal to reuse, stale dependencies, failed execution, missing evidence and disagreement with prior labels separately.

## Acceptance cases

COUNTEREXAMPLES.json fixes seven authored test intents before execution: useful-but-ignored, consumed-but-unnecessary, partial narrowing, wrong entity/equal output, stale dependency, target-specific preparation revision, and shared wrong-target/missing-constraint errors. They demonstrate distinctions, not research prevalence or oracle accuracy. The bounded software checks instantiate enumeration mechanics and payload isolation; draft/parameter-revision semantics remain review questions rather than silently being reduced to cached values.

A usable public development adapter still requires recovery and provenance review of selected original environments/tool semantics, a separately validated task-spec mapping, and the receipts/traces outlined above. No new probe follows merely because lexical screening or fixture tests pass.
