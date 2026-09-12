# Literal-prefix dataset candidate

Prepared after the owner completed binary decisions for the original pilot. This is **dataset preparation only**, not a new labeled benchmark or a completed research gate.

The 50 original full instructions now produce **703 literal completed-word observations** (666 distinct text strings). Every task's observations grow strictly by appending text, and the final observation equals its full instruction. There are no literal-prefix or sequence-nesting failures. Original instructions, 200 historical items, AI judgments and owner decisions are unchanged.

## Construction

The frozen protocol calls for all completed-word prefixes, not four outcome-selected checkpoints. This candidate uses every whitespace-delimited word boundary, beginning immediately after the first action verb. Every source instruction begins with an action verb; that convention is checked explicitly. Punctuation and internal whitespace are retained. These are text observations, not measured typing times or model-token boundaries.

For example, T001 begins `Find`, `Find flights`, `Find flights from`, `Find flights from Boston`, and continues through the unchanged full business-class instruction. The old economy-cabin counterfactual is not inserted into this cumulative sequence. T003 retains the full earlier JFK request when its later Newark correction arrives; its last prefix is not just the trailing correction fragment.

No reviewed label was used to choose boundaries, omit tasks or invent a target balance. All 50 already-exposed pilot tasks are retained. Their template distribution, realism, absent external context and pretraining contamination risks are not repaired by making prefixes literal. This does not replace the protocol's 3,000-task benchmark or satisfy its public-data composition requirements.

## Files and information boundaries

- `PREFIX_INPUTS.jsonl`: observation ID and observed prefix only. Only the prefix text may be passed to the model or candidate proposer. IDs are bookkeeping, not predictive features.
- `EVALUATOR_TASKS.jsonl`: unchanged final instruction, domain and links to historical item IDs. Evaluator-only information; never expose it to prefix-time proposal or feature extraction.
- `OBSERVATION_MAPPING.jsonl`: task links, observed word counts and exclusive Unicode-code-point offsets for audit. No future length or completion fraction is included in prefix-time inputs.
- `STRUCTURE_QA.json`: every task's structural checks.
- `STATUS.json` and `HASHES.json`: scope, missing work and file provenance.

Separate files make the boundary inspectable; they do not establish access-control isolation. The future runner must enforce its input allowlist. Identical text shared across tasks is preserved rather than silently deduplicated across evaluation units.

## What is still missing

**Candidate actions:** generate them from observed text alone under a fixed, versioned policy. Do not reuse a historical action that was written for a different snippet or infer the candidate from the final instruction. Permit an explicit no-action/insufficient-input outcome; do not turn abstention into a negative usefulness label or select only easy actionable prefixes without reporting coverage.

**Specified work products:** the repeated unresolved judgments arose because a generic “search” or “draft” can produce very different work. Record the actual result or a sufficiently narrow deterministic output contract before judging whether it survives. The accompanying action-contract proposal describes the needed information; it is not a new frozen labeling rule.

**New labels:** the owner's 125 reusable and 75 non-reusable decisions belong to the old prefix–action pairs. The new 703 observations have no candidate actions and no transferred labels. They must not inherit labels merely through shared task IDs or approximate prefix position.

**Research gates:** human G1 remains pending under the existing protocol. Model-token coverage for the complete eventual input is unknown. After G1 permits development work, preflight all intended inputs; if the validated 128-token scope is insufficient, select a global width independently of outcomes and rerun G0. No truncation, exclusions selected for favorable results, or numerical-contract mixing.

## Reproduction and use

Run `python3 outputs/prefix_dataset_candidate_v0_1/build.py --output /path/to/new-directory` with openpyxl available. The builder reads the unchanged blank pilot workbook and refuses to overwrite output files. It does not call a model or execute an action.

This candidate does not change the frozen thesis, H2/H3 comparisons, tolerances, endpoints or protocol gates. It is not authorized for confirmatory extraction, and no development or confirmatory extraction was run.
