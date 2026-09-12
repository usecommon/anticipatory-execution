# Human collector logic review

Status: PASS for the reviewed collector after two reproduced malformed-input bugs were fixed by the coordinating agent. No unresolved blocking collector defect was found in the bounded checks. This is software review, not validation of actual human judgments or a real-browser rendering assessment.

## Reviewed versions and evidence

- Final collect_humans.py SHA-256: `6cc0b93ac68209be97b14039da36fb33693fd282682b9c64cf32086ae64a54a9`
- Frozen review_template.html SHA-256: `aac497c8ec35113465897050dc79ee3de930636e3b9df36086022eaff35ca6f1`

The auditor has prior BFCL and shared-policy diagnostic exposure. This review is restricted to software behavior and provenance, not new blind annotation. No actual human submissions exist or were assessed. Tests constructed explicitly marked SYNTHETIC SOFTWARE TEST objects in temporary directories, then removed those directories; these do not constitute human annotations or gate evidence. The provided SOFTWARE_QA_DRAFT.json is likewise explicitly an incomplete software fixture, not a human response.

The reviewer did not modify source code or dataset/package files. The coordinating agent applied the two fixes below and preserved each earlier version with its fix log. The auditor independently reproduced failures against preserved versions and verified the corrected rejection behavior against the current collector. The frozen input, proposal, and review-input hashes still match after these collector-only fixes; package HTML/template bytes did not change.

## Bugs found and resolved

### Top-level non-object JSON escaped rejection reporting

The original collector stored parsed JSON in submissions before ensuring it was an object. A list or null caused the guarded role loop to record a malformed-submission error, then the later same-identity check called .get on that stored value outside the try block. The collector raised AttributeError and failed to write COLLECTION_REPORT.json.

A synthetic list input reproduced the crash against software_qa/collect_humans_before_top_level_fix.py. Both exact originals and RAW_HASHES.json had already been preserved. The fixed collector rejects non-object JSON before adding it to submissions and writes REJECTED_OR_INCOMPLETE_PRESERVED with an explicit object-type error. The earlier version and hashes are preserved in COLLECTOR_FIX.json; the auditor verified the fixed report and original bytes.

### Extremely large numeric fraction overflowed before range rejection

The intermediate collector evaluated math.isfinite before the 0-to-1 range check. A syntactically valid JSON integer of 10**1000 raised OverflowError during float conversion, again leaving preserved originals but no COLLECTION_REPORT.json.

The failure reproduced against software_qa/collect_humans_before_numeric_fix.py. The final code checks the permitted numeric range before isfinite, so the same input produces an invalid-fraction rejection with original bytes and a completed rejection report preserved. The prior version and fix hashes are recorded in COLLECTOR_NUMERIC_FIX.json. This was a software robustness test, not an annotation value supplied by a human.

## Preservation and rejection behavior

For readable input files, collect creates a new output directory, refuses to reuse an existing one, copies both input files exactly, and writes their SHA-256 hashes before parsing submissions or checking review-input hashes. Thus rejected submissions are retained rather than repaired or overwritten. File-copy, inaccessible-path, or other filesystem failures remain ordinary operational errors; the program does not promise a completed report when inputs cannot be read or output storage fails.

Synthetic tests confirmed readable rejection reports and unchanged originals for draft status, wrong package, same identity after whitespace/case normalization, Boolean binary, Boolean confidence, string fraction, unresolved binary without ambiguity Y, incomplete item IDs, non-object top-level JSON after its fix, and oversized fraction after its fix. Review-input hash mismatches are added as rejection errors before any agreement result is accepted.

Package ID and role must match the coordinator manifest. The submitted response set must contain all expected opaque IDs with matching count; duplicates or unknown IDs cannot satisfy these combined checks. Required annotation fields, exact integer binary/confidence types, finite bounded fractions, nonempty rationales, sufficiency enumeration, and ambiguity enumeration are checked. Unknown fractional utility may be explicitly null; it is not silently treated as zero.

## Null handling and agreement denominators

Disposition logic keeps no_material_work as invalid_candidate, uncertain sufficiency as uncertain_candidate, and substantive null binary as unresolved_reuse. None is converted to non-reusable. Non-substantive judgments require null binary and fraction. Uncertain sufficiency and substantive unresolved reuse require ambiguity Y.

The frozen coordinator mappings separate the 200 main cases from the 20 boundary controls. Main agreement includes only main cases; binary kappa includes only cases for which both raters record substantive work and resolve binary usefulness. It reports the complete-pair count and excluded count explicitly, alongside sufficiency and full-disposition agreement. The 20 controls have separate per-rater diagnostic disposition counts and never enter the primary main kappa denominator.

Empirical marginal binary counts determine expected agreement and Cohen kappa. Degenerate marginals produce a false nondegeneracy condition; all-one agreement has undefined kappa, not a pass. The numerical criterion requires exactly 200 main cases and 200 complete binary pairs, both labels present in each rater, kappa at least 0.70, and all main fractional-utility fields resolved. That full-denominator and secondary-field condition is stricter than merely reporting kappa on whatever subset remains.

| Explicitly synthetic scenario | Main binary pairs | Kappa | Numerical criterion only | G1 |
| --- | ---: | ---: | --- | --- |
| Balanced identical binary vectors | 200 | 1.0 | true | PENDING |
| All-one main vectors | 200 | null | false | PENDING |
| One unresolved main case in each rater | 199 | 1.0 | false | PENDING |
| One no-material main case in each rater | 199 | 1.0 | false | PENDING |
| One unknown main fraction in each rater | 200 | 1.0 | false | PENDING |
| Opposite main binary vectors | 200 | -1.0 | false | PENDING |

All six integration tests retained boundary_items = 20 and main items = 200. These test vectors validate arithmetic and exclusion logic only; none is a human dataset or agreement result.

## Human identity, independence, and adjudication

The collector requires a nonempty identity/pseudonym, rejects the same normalized identity across roles, and requires literal true independence and false prior-AI-label-exposure declarations. Distinct text strings do not establish distinct actual people, and declarations do not prove independence. The report correctly keeps human_process_verified false, explains that coordinator review is required, and never upgrades attestation into verified human provenance.

Even when the numerical criterion is true, validation remains VALIDATED_EXPORTS_PROCESS_PENDING and G1 remains PENDING. third_adjudication_received is false. The program writes blank adjudication fields for disposition disagreements or ambiguity-flagged cases; it does not fabricate a third adjudicator's decisions or identity. It neither checks a completed third-adjudicator submission nor closes the research gate. The flagging file is an attention queue, not evidence that adjudication occurred. Actual process review and preserved third-party decisions remain outstanding.

## UI correspondence and browser limits

Static review of the frozen template confirms blank initial responses and unchecked attestations, separate sufficiency and survival controls, null assignment for non-substantive work, ambiguity validation for unresolved judgments, and clearing of stale reuse/fraction fields when sufficiency changes. Export status is SUBMITTED_FOR_REVIEW only when all cases pass the local field checks and identity/attestations are entered; otherwise it is DRAFT. This status is a request for coordinator validation, not evidence of human provenance or a gate pass. The collector independently validates exports rather than trusting that UI status.

The recorded DOM_QA.json reports execution of the actual embedded JavaScript in a Node VM with a minimal DOM, local-storage, and download harness. Its listed checks cover blank state, 220 IDs, disabling/resetting controls, uncertainty, draft export, reload/import, navigation, and wrong-role rejection. These are software checks, not a native-browser or visual-layout test.

BROWSER_BLOCKED.json records Chromium terminating before page load because MachPortRendezvousServer bootstrap permission was denied, with SIGTRAP. Therefore no real-browser rendering, native file download/import interaction, browser storage behavior, or visual verification may be claimed from this attempt. The minimal-DOM success does not remove that limitation. No package or human input was changed to bypass it.

## Remaining interpretation

The reviewed software preserves failures, separates uncertainty from negatives and controls from main observations, and does not automatically close G1. Actual human collection, identities and independence assessment, complete appropriate annotations, and distinct third adjudication remain pending. Endpoint censoring, repeated-task dependence, and private source-admission limits from the preceding audits remain unchanged.
