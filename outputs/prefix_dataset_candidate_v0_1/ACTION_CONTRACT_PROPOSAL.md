# Candidate action and output specification — proposal only

The next construction step is to make each candidate's work sufficiently concrete to judge reuse. This document proposes recording requirements; it does not silently amend the frozen rubric, choose a new materiality threshold, generate labels, or authorize execution.

## Prefix-only proposal record

Record observation ID, policy version/hash, exact observed text hash, action type, explicit arguments, dependencies known at that point, execution class, expected work product and missing required inputs. Future instruction, domain inferred from future text, owner labels, historical gold labels, total instruction length and future checkpoints are not proposer inputs.

When required information is missing, record the exact missing fields and abstain or propose a smaller valid preparation action. Do not invent a destination, company, time, document contents, or other unavailable context. Distinguish completing a partial work product from replacing already-produced work.

## Execution or fixture record

Where safe and authorized, record concrete output, output hash, environment state/version, tool implementation, timestamps/freshness window, time and compute cost, failures and side effects. For synthetic fixtures, declare the fixture as synthetic and retain its complete initial state; do not report fixture output as an observed live API result. Class 4 remains unexecuted or simulated according to the primary-experiment constraints.

For retrieval, identify the query, result budget, source snapshot and actual returned records. For drafts or code, retain the exact artifact rather than merely “draft email” or “write function.” For a ranking, retain the candidate set, ranking rule and resulting order. These details let a reviewer distinguish possible overlap from demonstrated reusable work.

## Evaluator-only judgment

The evaluator may see the full final instruction and concrete candidate work product. Apply the existing binary target: reuse without material re-execution. Keep fractional utility secondary. Record what survives, what must be redone and why. An unmet final requirement does not automatically invalidate an intermediate result; conversely, a successful final task does not prove every early action was useful.

The pilot exposed unresolved definitions for “material” revision, the denominator of fractional utility, freshness and soft preferences. Any operational choices need a prospective rubric addendum with examples before a new reliability pilot. Preserve unresolved cases and do not force a binary decision merely to complete a file. Owner bulk acceptance of earlier labels does not resolve these definitions for different examples.

## Illustrative scope reduction, not a labeled experiment

At the observed text `Find flights from Boston`, a proposer could extract the explicitly stated origin into a structured field, with the output `{"origin_text":"Boston"}`. It cannot infer Tokyo, a date, cabin, award availability or an airport code not established by its inputs. This is a narrowly defined preparation artifact, distinct from an unspecified flight search. The example demonstrates how to state work precisely; no usefulness label or performance result is assigned here.

Keep preparation, retrieval, drafting, abstention and costs visible. A policy that only performs trivial safe preparation may have high reuse but little latency benefit; that is an empirical outcome, not a reason to manufacture riskier candidates or broaden the thesis.
