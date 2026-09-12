# AI annotation trial — 200 items

The user requested that Codex try the annotation. One Codex session assigned all 200 binary labels, fractional-utility estimates, confidence values, ambiguity flags and rationales. These are AI judgments, not human observations or validated ground truth. **G1 remains PENDING.**

## Results

| Measure | Result |
|---|---:|
| Complete AI-labeled items | 200 |
| Judged reusable | 148 |
| Judged non-reusable | 52 |
| Flagged ambiguous | 86 |
| Confidence 1 / 2 / 3 / 4 / 5 | 0 / 19 / 32 / 36 / 113 |
| Independent human label pairs | 0 |
| Cohen's kappa | Not computed |

All judgments are explicit authored entries, not outputs of a position-based labeling rule. The validation script only parses and checks the authored entries. `AI_LABELS.jsonl` preserves each item, judgment and AI provenance. The workbook places this single trial in Annotator_A for compatibility and leaves Annotator_B blank; its README explicitly identifies the AI trial. It must not be submitted as a human rating set.

The owner-only key was not read or used. The model had project context and rubric worked examples, including examples overlapping these items. Task groups were read with prefix, action, arguments and full instruction visible together; the prescribed prefix-first staged presentation was not reproduced. This is therefore a contextualized AI trial, not a blind rater experiment. Fractional utility values are coarse subjective estimates, not measured proportions or calibrated probabilities.

## Findings that matter before thesis testing

**Prefix structure:** only 54/200 fields are literal initial substrings of their final instructions; case-insensitive checking gives the same count. Of all 200 fields, 142 appear somewhere verbatim in the final instruction and 58 do not. `PREFIX_STRUCTURE.json` records the checks per item. No text was normalized or repaired. These counts describe string structure, not the truth of an annotation.

For example, T001-P3 contains an economy-cabin request absent from its business-class final instruction. T003-P4 is a trailing switch-to-Newark fragment, rather than the complete input observed up to that point. Such items can test semantic revision judgments, but they do not establish a growing within-utterance trajectory. Genuine editing or spoken corrections would require an explicit history representation and policy; silently treating these fields as cumulative prefixes would change the experiment.

**Position artifact:** P1 has 46 positive judgments, P2 has 48, P3 has 4, and P4 has 50. A post hoc rule assigning zero to P3 and one elsewhere agrees with 190/200 trial judgments (95%). This is descriptive agreement with one AI label set, not held-out accuracy or evidence for H1. The pattern suggests strong construction artifacts; it does not establish agreement with the unread owner key or eventual human labels. Position and IDs must not become shortcuts for a claimed internal-dynamics effect.

**Unspecified outputs:** generic searches, drafts and rankings do not define the actual work product or retrieval coverage. Judgments such as broad hotel search reuse depend on whether relevant results were retrieved. The rubric's broad-retrieval example supports possible reuse, but cannot establish every concrete output's usefulness. Several generic drafts were judged tentatively reusable while others were judged likely to require material revision; this unresolved boundary is a reason for the ambiguity flags, not a basis for silently changing the rubric.

**Preferences and conditions:** T014-P3's Monday invite may be a fallback under a Tuesday preference. T025-P3's federal research may survive as permitted context despite the wrong primary emphasis. T026-P3's vendor claims may support independent verification while remaining ineligible as unverified evidence. These were flagged rather than automatically treated as negatives. Some candidate descriptions and arguments also differ in strength: ranking shorter documentaries versus imposing a maximum runtime, for example.

**Action scope:** four items describe Class 4 actions. They were judged as written; none was executed. Their presence in a semantic labeling pilot does not authorize external commitments in the primary experiment.

## What this changes

This trial supplies concrete rubric-review material. It does not close G1, validate annotation accuracy, amend the frozen protocol, establish H1–H4, or authorize development/confirmatory extraction. Original workbooks and human collection packages remain unchanged.

Keep this AI-labeled file away from prospective independent annotators until their submissions are preserved. Exposure can anchor their judgments and compromise independence. Complete the original G1 process with independent human submissions, the unchanged reliability criterion and prescribed third-party adjudication. Retain disagreement rather than editing toward this trial's answers.

Separately, before a thesis-testing dataset is adopted, document an outcome-independent construction plan for actual cumulative input histories and sufficiently specified candidate work products. Preserve this pilot as a historical semantic-rubric pilot; do not silently rewrite its items or use the position pattern as scientific evidence. Any change belongs in an explicit prospective addendum. Frozen thesis, numerical contract and extraction restrictions remain unchanged.

## Verification

All 200 AI entries satisfy field types, ranges, required rationales and original item/context identity. The second rater remains blank and the independent checker reports zero completed pairs, no kappa and G1 pending. Workbook formula inspection/recalculation reports no formula errors and PENDING reliability. The changed annotation, README and gate views were rendered for review. Exported cells are checked against the JSONL judgments. Native Numbers import/export was not tested in this trial.
