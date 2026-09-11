# G1 readiness audit — September 11, 2026

**G1 PENDING. Zero completed independent label pairs in the checked-in pilot.** G0 remains PASS_SCOPED; no development or confirmatory extraction was run. Latest Cloud setup commits were incorporated through 0419f3c before this audit.

## What was inspected

The original workbook contains 200 unique items, 50 tasks and 12 domains on each of Annotator_A and Annotator_B. All 200 primary labels are blank on both sheets. Secondary labels are also unfilled. The original rubric and relevant protocol provisions were read; the separate owner gold key was not read for this audit and was not used to supply labels. No workbook bytes were modified.

## Original workbook formula risks

Adjudication!D2:E201 directly references the label cells, for example `=Annotator_A!J2`. In Excel, a reference to an empty cell can produce numeric zero. The paired-count formula at K2 uses `>=0`, so it does not independently require explicit binary labels. The kappa formula at K7 contains `IF(K6=1,1,...)`, setting kappa to one when expected agreement equals one. K9 can consequently return PASS for blank/degenerate sheets under those evaluation semantics. Positional row references also assume that neither sheet was reordered independently.

These are formula-inspection findings. Excel itself was not opened or recalculated during this audit; no cached display is presented as an observed Excel result. Do not use the original workbook's gate cell alone to authorize progression. The original is preserved as historical evidence.

## Independent checker

`scripts/g1_check.py` reads explicit cell values with formulas unevaluated. It checks the exact 200 reference IDs and unchanged annotation context, aligns sheets by ID, rejects formulas/invalid labels/duplicates, and distinguishes blanks from zeros. It requires every pair before computing Cohen's kappa, retains secondary-field incompleteness and reports degenerate rater prevalence. The threshold remains 0.70. Exact rational arithmetic avoids rounding the threshold boundary into a pass or fail.

The checker reports the binary statistic separately from G1. Even a threshold-meeting statistic does not certify annotator independence, third-party adjudication or the full gate. It never authorizes extraction or updates the frozen status automatically.

Read-only dependency: openpyxl 3.1.5. Synthetic logic tests use the standard library and do not require model access:

```sh
python3 -m unittest discover -s tests -v
```

Ten tests passed: blanks, complete nondegenerate agreement, degenerate agreement, exactly 0.70, below 0.70, one missing label, invalid labels/formulas, duplicate IDs, changed item context, and missing secondary fields. The complete-agreement test also checks reordered rows. These are software tests, not new scientific evidence or independent annotations.

When completed files exist:

```sh
python3 scripts/g1_check.py \
  --a /path/to/annotator_A.xlsx \
  --b /path/to/annotator_B.xlsx \
  --output outputs/g1_readiness_v0_1/new_unique_check.json
```

Use --sheet-a/--sheet-b if sheet names differ. Each completed sheet must retain the reference headers, IDs and item content. The output path must be new; prior checks are not overwritten. SHA256 records identify input workbooks.

## Next valid thesis-testing sequence

1. Obtain both independent annotations under the frozen rubric. Keep the owner key and the other annotator's work inaccessible. Do not distribute repository access to annotators, since the repository contains the owner key. Preserve original independent submissions before adjudication.
2. Run the checker, inspect completeness, prevalence and kappa, then complete the prescribed third-party disagreement adjudication. A checker threshold result is not a substitute for the process evidence.
3. If kappa is below 0.70, revise the development rubric/ontology and run a new pilot, preserving failures. Do not selectively remove difficult items to chase agreement.
4. After G1 is validly closed and development work is authorized, preflight the complete development benchmark against the 128-token limit. No truncation or selective exclusion. An outcome-independent larger global width needs new G0 validation.
5. Test H1 against naive baselines, H2 with matched B1 versus M, and H3 with matched B2 versus M under the frozen protocol. Regenerate affected features and refit development-only components using one extraction configuration. Do not reuse historical BF16 features as numerically neutral.
6. Keep product latency/waste evaluation separate from internal-state incremental value. Preserve negative results. Confirmatory extraction remains prohibited in this continuation.

No GPU or external annotation outreach was performed. This audit does not fix the incomplete GitHub raw-artifact transfer, which remains a separate storage issue and does not change the recorded G0 result.
