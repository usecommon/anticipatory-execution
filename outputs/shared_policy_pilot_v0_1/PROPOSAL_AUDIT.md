# Frozen proposal and reviewer-input audit

Status: PASS for proposal accounting, exact reuse, source projection, and manifest consistency. This is a structural/provenance audit, not artifact-sufficiency or survival labeling.

## Exposure and evidence boundary

This reused agent session previously adjudicated the 59 older BFCL public proposals using both frozen AI ratings and then audited this shared-policy adapter with source visibility. That exposure is explicit; this report is not a new blind annotation or an independent human G1 assessment.

The present check read the two frozen raw proposer outputs, their assigned inputs, evaluator context, prefix groups, ALL_OPPORTUNITIES.jsonl, PROPOSED_ITEMS.jsonl, both reviewer input files and mappings, reviewer instructions, and SOURCE_HASHES.json, INPUT_FREEZE.json, PROPOSAL_FREEZE.json, and REVIEW_FREEZE.json. Files named by these manifests were read as bytes to verify hashes. No work/shared_rater files, future judge outputs, owner gold, or external sources were accessed. No candidate, fixture, or pipeline builder was executed. Separate read-only assertions checked existing artifacts; only this report was authored.

## Proposal accounting

| Measure | Verified count |
| --- | ---: |
| Opportunities | 300 |
| Unique exact-prefix groups | 258 |
| Raw proposer records | 258, split 129 / 129 |
| Unique proposed artifacts | 62 |
| Unique-prefix abstentions | 196 |
| Proposed task rows | 87 |
| Abstained task rows | 213 |
| Reviewer rows per reviewer | 87 |

| Source | Opportunities | Proposed task rows | Abstained task rows | Unique proposed prefix groups |
| --- | ---: | ---: | ---: | ---: |
| Public BFCL | 200 | 21 | 179 | 21 |
| Synthetic | 100 | 66 | 34 | 41 |
| Total | 300 | 87 | 213 | 62 |

Task-opportunity proposal coverage is 29.0% overall, 10.5% public, and 66.0% synthetic. Unique-prefix proposal coverage is 62/258, approximately 24.0%. These are proposal coverage counts, not accepted substantive artifacts, usefulness results, or independent-sample success rates.

The 62 proposed artifacts comprise 38 class-1, 23 class-2, and one class-3 declaration. After reuse across opportunities, the 87 task rows comprise 49 class-1, 37 class-2, and one class-3 declaration. No class-4 declaration occurs. This validates declared values, not semantic correctness of the class assignment or evidence that any action was executed.

## Exact reuse and schema checks

Each raw proposer file contains every assigned opaque prefix ID exactly once, with no additional or missing IDs. The two sets are disjoint and together cover all 258 groups. Each row has exactly the required six fields: item_id, proposal_status, candidate_action, execution_class, work_product, and prefix_support. Status is proposed or abstain, and every rationale is nonempty. Abstentions have null action, class, and product. Proposed records have nonempty action and product strings and an integer class in 1, 2, or 3.

All 300 opportunity rows preserve their evaluator-context fields exactly. Every status, action, class, work product, and prefix-support rationale equals the single raw proposal assigned by that opportunity's prefix_group. Thus related opportunities sharing an exact prefix reuse the identical frozen output, including abstentions; no artifact repair, source-dependent substitution, or second proposal appears in this expansion. Every opportunity occurs once in its matching prefix group.

PROPOSED_ITEMS.jsonl equals the ordered proposed-status subset of ALL_OPPORTUNITIES.jsonl exactly. It contains all 87 proposed task rows and no abstentions. Its 62 unique prefix groups match the 62 raw proposed records. Abstentions remain in the full 300-row accounting rather than becoming negative survival labels or being silently dropped from coverage denominators.

## Reviewer input boundary

Both reviewer mappings are bijections from 87 opaque reviewer IDs to the same 87 proposed task IDs. Their orderings differ. Every reviewer input record matches its mapped proposal exactly on prefix, candidate action, work product, execution class, full instruction, and fixture contract.

Each reviewer row has exactly those six content fields plus item_id. It has no source, domain, source-task ID, family, original opportunity ID, prefix-group ID, multiplicity, prefix-support rationale, old label, or another reviewer's rating. The IDs use reviewer-specific opaque A### and B### formats. Reviewer instructions permit only the assigned input, original rubric, and instructions, and prohibit mappings, source files, prior outputs, other ratings, web, and owner keys.

This establishes omission of explicit source metadata from the prepared reviewer payloads. It does not prove that source cannot be inferred from wording, that duplicated artifacts are unrecognizable, or that a live session received only those inputs. Reviewer-session transcripts and isolation enforcement are outside this audit's evidence. No claim of independent model families, independent human raters, or completed blinded-label validation follows from differently ordered payloads.

## Frozen-byte verification

All 3 source-manifest entries, all 10 input-freeze entries, both raw-proposal-freeze entries, and all 7 review-freeze entries match their current SHA-256 values. The input freeze still matches after report creation. No mismatch or structural accounting defect was found.

Manifest equality attests to present byte consistency with the recorded manifests. It does not independently authenticate origin, timestamp the freeze, or exclude coordinated replacement of a manifest and its files. This later report is not a member of the earlier frozen input manifests.

## Remaining boundary

Artifact sufficiency, future survival, ambiguity, paired rating denominators, and adjudicated dispositions remain for the labeling and final arithmetic stages. This report intentionally makes no claim about those results. All prior source-exposure limitations and unchanged research gates remain applicable.
