# Fresh AI judge input audit

Status: PASS for exact case selection, opaque-ID mapping, input projection, deterministic shuffle, and frozen-byte preservation. This is a structural audit, not new case judging or independent human annotation.

## Exposure and evidence boundary

This reused auditor session has prior BFCL/shared-policy diagnostic and human-package structural exposure. That exposure is disclosed; it is not the fresh case-judge session. The audit read the new plan, preparation script, judge instructions, input and mapping, input/source manifests, and the permitted human-pilot selected main/control files and package freeze. Package files and ZIPs were read as bytes for hash verification. No work/checkpoint_case_judge file, new judge output, old rating, gold, or owner key was accessed.

The preparation script was inspected, not executed. Independent read-only assertions reconstructed the shuffle and projection. No input, package, candidate, or dataset was changed; only this report was authored. No candidate or fixture was executed, and no external service was contacted.

## Exact case correspondence

The new input contains exactly the frozen 200 main cases and 20 separately tracked boundary cases used in the human packages. The coordinator case set has 220 unique IDs. No case is added, dropped, duplicated, or selected from the 60 other review-pool products. The main cases retain their 100-public/100-synthetic selection; the 20 boundary cases remain coordinator-side diagnostics, not extra main observations.

All 220 judge records and mapping rows are unique. Their IDs are J001 through J220. Every mapping row points to the correct selected/control case, with correct review_kind, source, task, checkpoint, and template lineage. Every input prefix, action, work product, execution class, and complete instruction equals its mapped source field exactly. The fixture contract is the same explicit unexecuted-artifact contract used in the human packages.

The documented seed 260913220 reproduces the judge order from the main-plus-boundary list exactly. This permutation differs from both human-package permutations reconstructed with their documented seeds. Opaque IDs contain no task/source/control lineage. Deterministic shuffling establishes the input order; it does not control model sampling or independently prove a fresh runtime context.

## Judge input boundary

Each input row has exactly seven fields: item_id, prefix, candidate_action, work_product, execution_class, full_instruction, and fixture_contract. No source/domain field, coordinator ID, checkpoint lineage, task/template identifier, review-kind/control marker, expected boundary decision, proposal-generation rationale, previous rating, or prior adjudication is present. Targeted checks found no coordinator IDs or source/control/rating data markers embedded in the projected input.

Judge instructions permit only the assigned input, original rubric, and sufficiency clarification. They explicitly prohibit mappings, sources, previous judgments, owner key, external information, and executing artifacts. They identify this as one AI rating per case, not adjudication of supplied ratings, and require a separate decision reason. The frozen plan retains all dispositions and prohibits converting no-material work to negative reuse or editing labels/artifacts to improve results.

Omission of explicit metadata does not eliminate linguistic source inference, recognition of deliberately minimal artifacts, visible prefix lengths, remembered public content, or cross-case context effects in a 220-case batch. The instructions and prepared payload are verified, but live-session isolation and actual read behavior are outside this audit's evidence.

## Hashes and human-package preservation

All 7 entries in the new INPUT_FREEZE.json and all 4 SOURCE_HASHES.json entries match current bytes. The copied original rubric matches its previously frozen hash, `95a21c324668f010475d2d2f550f8b22bd3011173c76b36276d529929321e11e`.

All 16 entries in the human pilot's REVIEW_INPUT_FREEZE.json still match. Its PACKAGE_MANIFEST.json separately verifies all eight package files and both ZIP hashes. Therefore the existing human packages, selected cases, controls, and coordinator mappings remain byte-preserved. They have not acquired new AI labels. These checks were repeated after authoring this report.

Manifest equality verifies present byte consistency, not independent timestamping or provenance authentication. The current manifests do not alone establish dispatch timing, model snapshot, or proof against coordinated file/manifest replacement. This later audit is outside the earlier input freeze.

## Interpretation and remaining work

No structural input defect was found. This stage supplies no judge output, human response, agreement result, or gate pass. A single AI judge cannot supply paired-rater Cohen kappa. Any later comparison with older six-word judgments must occur only after preserving the new raw output and must be reported as judgment sensitivity, not independent human reliability or model efficacy. This audit does not inspect those older ratings.

The 200 main and 20 boundary denominators must remain separate. Boundary artifacts are authored diagnostics, not independently verified ground truth. Selected-case source/checkpoint results are not representative prevalence estimates, and task/template dependence remains. Actual human reviewers must remain unaware of these case-level AI judgments; human G1 and source-release admission remain pending.
