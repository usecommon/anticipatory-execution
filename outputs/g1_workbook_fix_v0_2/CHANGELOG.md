# G1 workbook v0.2 — reliability calculation correction

Use aeb_g1_annotation_pilot_200_v0_2.xlsx for subsequent pilot labeling. The original workbook is unchanged and remains in handoff/.

- Blank labels stay missing rather than becoming numeric zero. All 200 explicit binary pairs are required before kappa is calculated.
- Labels are joined by unique item ID, so independent row reordering does not mispair judgments. Missing/duplicate IDs and nonbinary numeric/text/boolean values produce INVALID.
- Degenerate rater prevalence produces DEGENERATE and leaves kappa blank. Undefined kappa is never replaced with one.
- The 0.70 threshold is unchanged. The former automatic PASS is now a binary reliability result (MEETS THRESHOLD or BELOW THRESHOLD), not G1 approval. Independent annotation, secondary fields, unchanged item context, and third-party adjudication still require verification.
- Workbook formulas evaluate numeric cell values; a numeric formula can therefore satisfy the workbook's statistical check. The independent scripts/g1_check.py additionally rejects formula labels and must be used before gate review. Enter labels as numeric constants as the instructions require.

Twelve dynamic scenarios passed in artifact-tool, including blank, all-zero, perfect balanced agreement, exact threshold, below threshold, one missing label, invalid numeric/boolean labels, numeric-formula limitation, row reordering, duplicate IDs, and final restoration to blank. No formula-error strings were found in the final workbook. The summary and modified instructions were rendered and visually checked. Saved-file auditing verified unchanged annotation/item content, all 400 primary-label cells blank, and preserved styles, validations, widths, merges and freeze settings on every sheet. Changed cells are limited to the reliability calculations and three directly related instruction cells.

Excel itself was not launched. These are artifact-tool calculation and XLSX preservation checks, not a claim of native Excel execution. The independent Python checker on the saved workbook reports zero completed pairs and G1 PENDING. No labels were supplied, no scientific hypothesis was tested, and no extraction gate was advanced.
