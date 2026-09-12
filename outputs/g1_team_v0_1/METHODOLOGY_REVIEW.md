# B methodological review of the frozen AI study

The results support high reproducibility of these three AI annotators' binary judgments on this particular constructed set. They do not establish human label reliability, label accuracy, or the efficacy of anticipatory execution. Item construction does not support interpreting P1–P4 as cumulative observations of a user instruction.

## Scope

Reviewed only `RATER_A.jsonl`, `RATER_B.jsonl`, `RATER_C.jsonl`, `STUDY_PLAN.json`, and `AGREEMENT_SUMMARY.json` in `outputs/anticipatory-execution/outputs/g1_team_v0_1`, together with my existing B rubric and methods. All three frozen rater files were parsed with Python standard-library code for descriptive calculations. No owner key, prior trial, external sources, other files, candidate execution, new labels, or label revisions were used. This review is AI-generated; I am one of the original raters and therefore not an independent external auditor.

## What the agreement establishes

The primary A–B comparison reports 198/200 agreement (99%) and Cohen's kappa 0.9743. A–C kappa is 0.9487; B–C is 0.9740; three-rater Fleiss kappa is 0.9656. There are 196 unanimous items. Positive prevalence is 146/200 for A and 148/200 each for B and C, so both binary classes occur in meaningful numbers. These figures are comfortably above the numerical 0.70 reference point.

That is evidence of within-study AI judgment reproducibility, conditional on the shared rubric, model, and item construction. The study plan correctly leaves human G1 pending: there are zero independent human pairs. Same configured model, unpinned service revision, shared instruction framing, and isolation by workflow rather than access controls limit stronger independence claims. Agreement cannot reveal errors the models share. The corpus contains 50 repeated task families with four related rows each; treating all 200 rows as independent observations for inferential uncertainty would overstate information. Any interval or generalization analysis should resample at least at task level and explicitly define its target population.

The union of ambiguity flags contains 44 items, including 40 with unanimous binary labels. High agreement therefore does not eliminate uncertainty about the decision boundary. Fractional-utility mean absolute differences are 0.0332 for A–B, 0.0345 for A–C, and 0.0480 for B–C, matched by item ID. These are descriptive proximity measures, not calibrated survival estimates or validated utility reliability coefficients. Confidence ratings also lack an external correctness target.

## The prefix construction does not test cumulative anticipation

Using exact, case-sensitive `full_instruction.startswith(prefix)` with no normalization, 54/200 rows (27%) are literal prefixes. Another 88/200 (44%) are substrings elsewhere in the instruction but not initial prefixes. The remaining 58/200 (29%) are not exact substrings. Zero of the 50 task families has all four rows as nested literal prefixes of its complete instruction.

| Nominal position | Items | Literal prefixes | A positive | B positive | C positive |
|---|---:|---:|---:|---:|---:|
| P1 | 50 | 41 | 47 | 49 | 49 |
| P2 | 50 | 10 | 47 | 47 | 48 |
| P3 | 50 | 1 | 2 | 2 | 1 |
| P4 | 50 | 2 | 50 | 50 | 50 |

Position-label Cramer's V, calculated from the 4-by-2 tables, is 0.8990 for A, 0.9227 for B, and 0.9482 for C. A retrospective diagnostic rule assigning 0 to P3 and 1 elsewhere agrees with 96%, 97%, and 98% of the respective AI labels. This rule was calculated only after freezing labels; it was not used to annotate. These percentages measure agreement with AI judgments, not ground-truth accuracy, and no significance test is needed to see the construction imbalance. Role-specific opaque IDs and shuffled presentation reduce direct position access during rating; they do not remove this corpus-level semantic pattern.

For example, T001-P3's economy wording is incompatible with the complete business-class instruction: it cannot be an earlier literal prefix of that string. T009-P3 says “Exclude distributors,” whereas the final instruction includes distributors. T040-P4 presents the trailing temperature condition alone, not everything the user had said up to that point. Such rows can serve as counterfactual compatibility probes, but cannot be treated as sequential input snapshots. Genuine corrections, such as the coffee-shop-to-bakery instruction at T006, should retain the entire earlier text in every later cumulative prefix.

The study provides action descriptions and final instructions to annotators. It does not test a policy selecting an action from a prefix alone, actual prefix timestamps or token boundaries, time saved, extra computation, redo work, action success, rollback cost, or consequences. My method also notes that prefix and final text were co-visible; sequential attention was not an enforced reveal procedure. Full text is appropriate for retrospective survival labeling, but cannot stand in for a blinded prospective action choice. No model accuracy or anticipatory-execution efficacy conclusion follows from kappa here.

## Main rubric weaknesses, with examples

1. **The candidate work product is unspecified.** T031-P1 (“Draft Python function”), T019-P1 (“Draft Slack message”), and T021-P1 (“Draft customer reply”) invite raters to imagine reusable scaffolds or substantial invented bodies. A description is not an observed output. At T037-P2, A and B imagine substantive pricing that must be replaced; C imagines a reusable section containing TBD. All are plausible readings. Specify the actual artifact or tightly define what an underspecified action produces.

2. **“Material” revision has no operational threshold.** T048-P1's morning plan and T050-P1's task ranking account for the two A–B disagreements. Moving an appointment buffer or pinning a client deadline could be a small edit or a wholesale schedule change. A binary label cannot be anchored by intuition about a hypothetical output alone. Predefine a work-unit or cost-based revision threshold, distinguish extending an unfinished artifact from redoing completed work, and give borderline examples.

3. **Broad retrieval survival is assumed without result coverage.** T009-P1 follows the rubric's broad-manufacturer example, but arbitrary bounded retrieval can omit every relevant actuator manufacturer. T001-P1 may produce route data, current fares, or nothing executable without destination and dates. T006-P1's coffee-shop results might already include the needed bakery. Fix the query, result budget, cache contents, and temporal validity before deciding what can actually be reused.

4. **Evidence collection versus admissible final evidence is unresolved.** At T026-P3, A and B permit collecting vendor claims then checking reproduction; C treats the vendor-only evidence as insufficient. Clarify whether additional independent verification is completion of the final task or material re-execution of the candidate action. Insufficiency of an intermediate output is not automatically invalidation.

5. **Soft preferences and unsupported narrowing are not the same as hard contradiction.** T014-P3 stages Monday despite a Tuesday preference, which may remain a valid fallback. T007-P3's pool filter and T011-P3's hood filter impose unnecessary constraints but do not logically preclude day-pass gyms or stand collars. State whether survival means at least one acceptable candidate, preserved recall, optimality, or compliance with explicit constraints; these yield different answers.

6. **Staging, commitment, condition evaluation, and freshness need separate treatment.** T032-P3 prepares a retry-setting increase even though changes must await diagnosis; whether speculative preparation survives is distinct from whether applying it is authorized. T040-P4's temperature reading may need repeating tonight even if useful now. The corpus has 52 prepare-class, 80 speculate-class, 64 stage-class, and only 4 commit-class rows, with no observe-class rows. It provides little basis for reliability across execution-risk classes. Use explicit state and timing fixtures and separate work reuse from authorization and harm.

7. **Fractional utility lacks a denominator.** Is it the fraction of existing content retained, computation not repeated, final task completed, or economic value saved? A nearly empty reusable skeleton can receive low utility despite all of its tiny output surviving, while a mostly retained ranking can be binary 0. T031-P1, T036-P2, and T050-P1 expose this problem. Define the denominator, handling of empty work, and relationship—if any—between the fractional score and binary threshold.

## Appropriate next use

Keep the frozen results as an AI compatibility-annotation pilot and retain all original disagreements and ambiguity flags. Resolve operational definitions before a new reliability sample, using independent human annotators if human G1 is the intended gate. A cumulative-prefix study needs real nested prefixes with recorded boundaries, prefix-only candidate selection separated from full-instruction evaluation, task-level held-out splits, balanced counterexamples without position-linked label roles, concrete execution traces, and preregistered measures of reuse and saved versus wasted work. This critique recommends a subsequent study; it neither relabels this one nor declares G1 passed.
