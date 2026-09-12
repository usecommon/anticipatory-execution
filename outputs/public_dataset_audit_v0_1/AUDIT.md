# Public dataset audit — September 11, 2026

**Public datasets can reduce task construction and annotation work. None of the inspected releases supplies a verified, ready-to-use replacement for this project's prefix–candidate-action–final-instruction reusability labels.** This is a bounded audit, not a claim that no such dataset exists anywhere.

The frozen thesis remains: **Do not predict what the user will type next. Predict what work will not need to be undone.** G0 remains PASS_SCOPED, G1 remains PENDING, and confirmatory extraction remains prohibited. No model inference, benchmark execution, annotation, or protocol amendment was performed.

## Findings

| Dataset | Existing supervision or evaluator | Appropriate role | Missing for our target |
|---|---|---|---|
| inCLINC | Human intent judgments on full and partial utterances | Incremental-intent sanity check; reuse existing intent annotations | Candidate actions and whether their outputs remain reusable |
| BFCL, inspected v4 multi-turn base | Initial state, user turns, reference calls; state and execution-response checking | First candidate for a restricted executable reusability adapter | Within-utterance prefixes, prefix-only proposals, action-level reuse attribution and waste |
| ToolSandbox | Stateful scenarios, milestone constraints, forbidden-state checks | Complementary adapter for dependencies and invalid early actions | Prefix-level non-revision labels; proof that a successful trajectory actually reused a particular result |
| ComplexFuncBench | Reference function-calling tasks; rule, response and model-assisted comparisons | Later complex-action robustness work | Stable replay, reusability labels and validated context-length coverage |
| τ-bench family | Interactive tool-agent-user task evaluation | Later interactive systems evaluation | Fixed future instruction and action-level reuse labels; current release needs separate source audit |

### inCLINC: existing annotations are useful, but answer a different question

The official record describes 121 distinct utterances, 538 complete/partial stimuli, 37 intent categories plus out-of-scope, and six to nine coders per stimulus. These labels can be reused for intent analysis without relabeling the same target. They cannot directly answer whether a particular early search, calculation or prepared artifact survives the completed request. The repository links CC BY 4.0. Raw README/CSV web downloads failed in this audit, so column-level compatibility was not verified. [Official dataset record](https://fordatis.fraunhofer.de/handle/fordatis/213?locale=en).

### BFCL: strongest first adapter candidate, with an important limitation

At pinned commit `6ea57973c7a6097fd7c5915698c54c17c5b1b6c8`, both the inspected base file and its reference-answer file parse as 200 JSONL records. The first record has user turns, initial configuration, available-path information, involved classes and excluded functions; its reference supplies calls grouped by turn. This is public benchmark inspection, not AEB confirmatory extraction. [Pinned data](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json).

The checker compares state after nonempty-reference turns and checks whether accumulated model execution results contain the current reference results. It explicitly accommodates calls made in earlier turns. Thus describing BFCL as only a final-state check would be incorrect. Still, passing does not identify which extra early action was useful, measure wasted work, or supply within-utterance labels. An absent reference call is not automatically a negative reuse label. The checked repository license is Apache 2.0. [Pinned evaluator](https://github.com/ShishirPatil/gorilla/blob/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/multi_turn_checker.py).

### ToolSandbox: useful dependency and failure machinery

Pinned source exposes milestone snapshot constraints and guardrails against unintended state changes. Minefields describe forbidden trajectory states. Inspected scenarios include checking and changing cellular settings, with distinct state and response expectations. These are useful components for testing premature actions, but trajectory success does not by itself label each early result's reusability. The license is Apple's supplied software license, not assumed Apache/MIT. [Pinned evaluation source](https://github.com/apple-aiml-research/ToolSandbox/blob/c8571d7854316d2e1c5f288e59fe1e34e53f6dd1/tool_sandbox/common/evaluation.py), [license](https://github.com/apple-aiml-research/ToolSandbox/blob/c8571d7854316d2e1c5f288e59fe1e34e53f6dd1/LICENSE).

The standard setup includes a model-based user simulator; search scenarios require RapidAPI. An offline deterministic subset would need explicit boundaries and replay validation. [Official README](https://github.com/apple-aiml-research/ToolSandbox).

### ComplexFuncBench: useful, but not the shortest route through the present gates

The authors describe 1,000 complex tasks, long parameters and long contexts. Response-based evaluation can require a Booking API subscription. The pinned comparison code combines rule checks, response checks and a GPT-based fallback; this must not be presented as a purely deterministic oracle. [Official repository](https://github.com/zai-org/ComplexFuncBench), [pinned comparison code](https://github.com/zai-org/ComplexFuncBench/blob/c37b284e2f2e03ee456115b7c4b7e537f534be37/utils/compare_method.py).

The dataset card declares Apache 2.0, but its viewer currently reports mixed string/array content parsing failure. Its statistics table's total also conflicts with its narrative count. Neither observation proves raw data are unusable; they require explicit parsing/count verification before adoption. This audit did not download the full dataset or resolve those discrepancies. [Dataset card](https://huggingface.co/datasets/zai-org/ComplexFuncBench).

### τ-bench: avoid silently adopting the legacy release

The legacy repository warns that its airline/retail tasks are outdated and directs users to the successor repository, now described there as τ³-bench. This audit followed that link but did not inspect the successor's task schemas/evaluator. The interactive setup uses a simulated user. If early actions alter subsequent user messages, the outcome is an interactive-policy effect rather than prediction against one fixed eventual instruction; those studies must be distinguished. [Legacy notice](https://github.com/sierra-research/tau-bench), [successor repository](https://github.com/sierra-research/tau2-bench).

## What an executable reuse label must establish

This is a proposed adapter design, not an implemented or validated oracle:

1. Freeze an initial environment, full instruction and prefix schedule. Generate each candidate from only the information available at that prefix. Reference calls and future text are evaluator-only data.
2. Execute an allowed early action in an isolated copy. Record arguments, dependencies, result, cost and any state changes. Keep Class 4 external commitments outside the primary experiment.
3. Under the full instruction, test whether that recorded result can serve its intended role without material re-execution. Check dependencies and freshness; identical strings alone do not prove semantic equivalence.
4. Distinguish fully reusable, partial reuse, unusable and unresolved cases. Keep partial reuse secondary under the frozen rubric. Do not convert unresolved failures into negative labels or discard them silently.
5. Validate with known reusable cases and controlled changes to entities, units, destinations, constraints and environment state. Include harmless-but-unused work: a task can succeed despite wasting that work.
6. Compare with independent human judgments on an outcome-independent sample. Exact call matching can miss alternative valid implementations; a permissive task-success checker can accept irrelevant extra calls. Quantify both error directions.

This can automate a restricted subset after validation. It cannot yet waive the current human reliability gate. Simulator replay, API fixtures, judge versions and adapter hashes need provenance just as model features do.

## Recommendation and effect on the thesis

Keep the existing 200-item G1 pilot and the user-approved Numbers interface. Obtain the two independent submissions, preserve them, export separate XLSX files for `scripts/g1_check.py`, and complete adjudication. Visual approval of the Numbers workbook is not evidence that labels are complete or that Numbers export preserves the calculation behavior. The independent checker, explicit values and process evidence remain necessary. Do not share the owner-only key or one annotator's labels with the other.

For reducing later annotation effort, prioritize a **development-only BFCL adapter**, with ToolSandbox as a complementary source. Reusing public task text, environments and reference traces avoids building everything from scratch. Restricting the target to automatically checkable actions changes coverage and can change prevalence, difficulty and H2/H3 results; it is not a neutral substitution. Record any sampling or labeling change in a prospective protocol amendment before adopting it. This audit makes no such amendment and does not replace the pilot.

Maintain the frozen comparisons B1 versus M and B2 versus M. Lock task/utterance-level splits before prefix expansion, isolate inspected public cases from any future untouched holdout, and prevent full-instruction reference calls from leaking into candidate construction or features. Public data may have been seen during foundation-model training; availability does not establish uncontaminated generalization. Multi-turn clarification and within-utterance anticipation should be reported separately.

Before development extraction, preflight the actual complete model inputs using the frozen tokenizer, including whatever context the design exposes. No token coverage was measured here. G0's 128-token scope cannot be assumed to cover tool schemas or dialogue histories. Overlength inputs require an outcome-independent scope revision and renewed G0 validation, not truncation or convenient exclusions. B1/B2/M must use the same validated numerical contract; corrections and dataset changes may erase an apparent internal advantage.

## Evidence and limitations

`source_manifest.json` records nine downloaded files with commit-pinned URLs, byte counts and SHA256 hashes. Source code was inspected as text and never imported or executed. The two BFCL JSONL files were parsed and the first record's content inspected; ToolSandbox scenario/evaluator definitions and ComplexFuncBench comparator were inspected. No runtime success, oracle accuracy, annotation savings percentage or dataset-wide action coverage is claimed.

Web-only observations were accessed September 11, 2026. Failures retained in `AUDIT_STATUS.json`: inCLINC README/CSV fetch failures, Creative Commons page timeout, and ComplexFuncBench's displayed viewer failure/count discrepancy. Original G0 failures and historical workbook are unchanged. No owner gold key was used. The existing incomplete raw-evidence GitHub transfer remains a separate unresolved storage issue.
