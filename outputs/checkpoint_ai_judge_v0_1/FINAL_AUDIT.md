# Frozen AI judge result audit

Status: PASS. Independently reconstructed records, dispositions, selected-source/checkpoint summaries, prior-comparison transitions, and frozen hashes match the delivered results. No raw rating or data was edited.

## Auditor and evidence boundary

This reused structural auditor has prior BFCL/shared-policy diagnostic exposure; it is not the fresh case judge or a human annotator. The audit checked the new raw judge freeze before opening the now-authorized prior shared-policy ALL_ITEMS.jsonl. It then joined the raw output through the frozen judge mapping independently of score.py. The scoring script was inspected but not imported or executed. No owner gold, actual human labels, candidate execution, or external action was used. Only this report was authored.

## Complete current accounting

| Group | Cases | Reusable | Non-reusable | Unresolved reuse | No material work | Uncertain sufficiency | Ambiguity Y |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Main: public BFCL | 100 | 87 | 5 | 8 | 0 | 0 | 25 |
| Main: synthetic | 100 | 84 | 16 | 0 | 0 | 0 | 28 |
| All main | 200 | 171 | 21 | 8 | 0 | 0 | 53 |
| Boundary controls | 20 | 0 | 0 | 0 | 20 | 0 | 0 |

All 200 main cases are recorded as substantive. Their 171 reusable, 21 non-reusable, and 8 unresolved rows form an exact disjoint 200-ID partition. The separate 20 controls are all recorded as no_material_work, with null reuse and fraction; they are not 20 negative reuse examples. Together the main and boundary files reproduce all 220 unique mapped raw judgments exactly. All eight unresolved main cases have ambiguity Y; 53 main cases have that flag in total. These statements verify the recorded labels, not their semantic truth.

Every raw row has the required schema, valid sufficiency/ambiguity values, strict integer binary/confidence fields, bounded finite numeric fraction or null, and nonempty rationales/decision reason. Null rules pass. Every embedded judge object equals its frozen raw record, and all retained input/mapping fields match. Each disposition subset is the exact ordered subset of the reconstructed main file. REVIEW_ATTENTION.jsonl exactly contains all non-reusable dispositions or ambiguity-flagged cases (86 rows); this is an attention filter, not a second judgment.

## Selected source/checkpoint denominators

| Source | Words | Selected cases | Reusable | Non-reusable | Unresolved | Ambiguity Y |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| public_bfcl | 6 | 16 | 11 | 2 | 3 | 6 |
| public_bfcl | 12 | 25 | 22 | 0 | 3 | 5 |
| public_bfcl | 18 | 59 | 54 | 3 | 2 | 14 |
| synthetic | 6 | 49 | 33 | 16 | 0 | 16 |
| synthetic | 12 | 30 | 30 | 0 | 0 | 5 |
| synthetic | 18 | 21 | 21 | 0 | 0 | 7 |

The main selected-case reuse fraction is 171/200 = 85.5%; public is 87/100 and synthetic is 84/100. At six words, 44/65 selected cases are reusable; at twelve words, 52/55; at eighteen words, 75/80. All published fractions and counts were independently recomputed. These denominators are selected proposed artifacts, not all 900 scheduled opportunities, all eligible prefixes, or the full 260-product pool. The 60 unselected products are outside this judge request.

## Exact six-word sensitivity comparison

All 65 main cases at six words have an exact prior match on prefix, action, work product, declared execution class, and full instruction. Each prior embedded adjudication and current embedded raw judgment in PRIOR_COMPARISON.jsonl matches its source. Six dispositions changed and 59 remained the same.

| Prior disposition | New disposition | Cases |
| --- | --- | ---: |
| non_reusable | non_reusable | 17 |
| non_reusable | reusable | 3 |
| non_reusable | unresolved_reuse | 1 |
| reusable | non_reusable | 1 |
| reusable | reusable | 41 |
| reusable | unresolved_reuse | 1 |
| unresolved_reuse | unresolved_reuse | 1 |

Changed case IDs and directions:

| Coordinator item | Prior | New |
| --- | --- | --- |
| CP1-SP1-S-SX1-F001-R-W6 | non_reusable | reusable |
| CP1-SP1-S-SX1-F049-K-W6 | reusable | non_reusable |
| CP1-SP1-P-multi_turn_base_30-W6 | reusable | unresolved_reuse |
| CP1-SP1-S-SX1-F010-R-W6 | non_reusable | reusable |
| CP1-SP1-S-SX1-F042-R-W6 | non_reusable | reusable |
| CP1-SP1-P-multi_turn_base_106-W6 | non_reusable | unresolved_reuse |

Prior source SHA-256: `2b49edd4eaa8408be5e67d2b55fe1c67bcb3ce9d3d2b13a9f189b33e6a6bf468`. The changed flag refers to disposition, not every fractional utility, confidence, wording, or ambiguity difference. The comparison uses one new AI judge versus an earlier adjudicator that saw two frozen AI ratings. It is a context/reviewer sensitivity diagnostic, not paired independent human agreement, neutral rescoring, independent ground truth, or a change in model efficacy. The new raw output was preserved/frozen before the permitted prior source join; current manifest consistency and code order are verified, without claiming independent timestamp authentication.

## Hash and human-package preservation

All 7 input-freeze entries, 4 source-hash entries, and the raw-judge entry match. All 16 human REVIEW_INPUT_FREEZE entries still match, and PACKAGE_MANIFEST separately verifies all eight package files and both ZIPs. The human packages remain unchanged and contain no new AI judgments. Raw judge SHA-256: `baa5d51ba3f7bc0d04856eb2677411675e8a76bc7f583ede1a9c03818ee37391`. Checks were repeated after report creation.

Current results are validated by full record reconstruction, exact partitions, and independently recomputed scores. Hash equality establishes present byte agreement, not proof against coordinated manifest/file replacement or verified model sampling provenance. This report is outside the preceding freeze.

## Interpretation limits

There is one new AI rating per case, so inter-rater kappa is correctly null. No actual human submission or human G1 completion is established. Boundary artifacts are deliberately designed sufficiency diagnostics; all 20 receiving no-material-work labels is not independently established accuracy. Main cases remain correlated across checkpoints/tasks/templates.

High selected reuse at later checkpoints cannot establish a causal source or instruction-length effect. Eligibility censors instructions that have already ended, source availability differs, selected artifacts and task mixtures differ, and the hash/distinct-task-first sample is not a matched randomized comparison. Labels judge semantic artifact survival and do not measure saved time, computation, model accuracy, or latency. Human G1, actual independence and adjudication, and public adaptation admission remain pending. Item-level AI results must remain separate from human packages and unseen by the intended independent human annotators.
