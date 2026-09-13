# Council recommendations implemented — development contract v0.1

The user accepted the council recommendations. This package makes the next evaluation design concrete without changing the frozen thesis, rubric, old labels, check split or negative diagnostic.

- [Decision-time/reuse contract](CONTRACT.md): before-execution inputs exclude candidate results; after-preparation scoring remains a separate stage. Task correctness, consumption, contribution and reuse-capacity judgments stay separate.
- [Public adapter specification](ADAPTER_SPEC.md): narrowly scoped directory enumeration, independent task requirements, provenance and complete screening denominator. Actual BFCL environment/tool replay remains pending.
- [Comparison requirements](COMPARISON_SPEC.md): strong observable signals, stage-matched context, fair action interactions, snapshot controls and the original temporal controls. Interfaces are specified; full B1 is not implemented.
- [Seven fixed counterexample intents](COUNTEREXAMPLES.json): authored construct/software cases, not a new efficacy dataset.
- [Strict envelope and task-check software](contract.py): rejects empty/mismatched evidence; validates structure only, never public admission or binary usefulness.

## Observed development results

The deterministic screen retained all 200 source records (199 instruction groups). Its fixed lexical rule selected 9 records in 8 groups; no replacement or label-based filtering occurred. [Semantic scope triage](SEMANTIC_TRIAGE.jsonl) found 4 records in 3 groups potentially within simple enumeration, pending original context. Five selected records require unsupported composite/search/filter behavior. **None is admitted, executed or newly labeled.** Lexical selection and scope review are developmental, not representative sampling or claims of 9 independent tasks. The retained first-turn source lacks original environment data; an invented replacement must be named as an adaptation.

[Software attempt 02](software_attempt_02/QA.json): **25 checks passed, zero research cases validated.** [Attempt 01](software_attempt_01/QA.json) had 24 passes and one failure: payload metadata shared a mutable reference with the source decision. Recovery deep-copies the projected payload. Original code, failed check/traceback and unchanged expectations are preserved in [FAILURES.md](FAILURES.md). This was a software defect in the new package; it did not affect existing model results or labels.

The directory checker tests explicit authored task requirements independently of candidate-selected targets; it does not implement natural-language BFCL semantics. Preparation/draft materiality remains an explicit rubric-review question. Trace validation checks linkage and declarations, not whether a declared contribution is causally necessary.

## Reproduce

Use new output paths; existing attempt directories are never overwritten:

```sh
python3 outputs/evaluation_contract_v0_1/test_contract.py --out /tmp/aeb-contract-qa-new
python3 outputs/evaluation_contract_v0_1/screen.py --out /tmp/aeb-contract-screen-new
```

Source identity and initial specification/code freeze are retained. Screening reads only the existing first-turn evaluator records, never prior judgments or the owner key. Tests are stdlib-only; no GPU, public task execution, probe fitting, new AI reuse judging or confirmatory extraction ran.

Next: restore and verify original source environment/tool semantics for the fixed selected records, retain unsupported/missing cases, and establish independent task specifications before a bounded adapter execution. Review resulting evidence against the rubric before more probes. Full-B1 implementation and later human G1 remain outstanding. Confirmatory extraction remains prohibited.
