# G1 readiness assessment v0.1

Prepared September 11, 2026.

## Decision

**Gate: G1 Label Validity**

**Status: BLOCKED before annotation.**

Do not send the current combined workbook to annotators. Its 200 source records are structurally complete, but the package has three blocking validity defects: the recorded intermediate text is usually not a literal prefix of the recorded final instruction, the workbook exposes material that should be separated for blinding, and the adjudication formulas can report PASS on an untouched workbook.

This assessment does not change the frozen thesis, hypotheses, endpoints, labels, splits, numerical contract, or G0 status. It does not use the owner gold key as annotation evidence. No annotation, adjudication, development extraction, confirmatory extraction, GPU job, or Modal operation occurred.

## Repository and gate checkpoint

- Repository: `usecommon/anticipatory-execution` (private)
- Audited branch: `main`
- Audited HEAD: `523540c43c28e762c2626e90db88debafa887c04`
- G0: `PASS_SCOPED`
- Contract ID: `95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0`
- Successful G0 runs: `closure_a_20260911T175740Z`, `closure_c_20260911T180932Z`
- Preserved rejected run: `closure_b_20260911T180521Z`
- G1: `PENDING`
- Stage 1: `BLOCKED`
- Development extraction: false
- Confirmatory extraction: false

The audit used the GitHub connector because this Work session did not have a mounted checkout. Direct `git ls-remote` was unauthenticated. Therefore `python3 scripts/verify_import.py`, `git rev-parse HEAD`, and `git status --short` were not executed in a checkout. The connector verified the private repository, permissions, branch, and commit, and three G1 files were downloaded without the gold key; their SHA256 values matched `provenance/IMPORTED_FILES.json`:

- `handoff/aeb_g1_annotation_pilot_200.xlsx`: `63f2031293d21623abac89009d180bc0bf9f9b668d4e2b0cbfe554becf9d62ee`
- `handoff/aeb_g1_annotation_rubric_v0_1.docx`: `cfb4ece4644c9209f8a49381fe8a52b48a4f95cfdc97e5bee894c98f366dccc8`
- `handoff/anticipatory_execution_preregistered_protocol_v0_1.docx`: `06b66080f6a8e2a745d78e7d884189cf93c8881becc9381aad1d086c160f00a7`

The owner-only item-level gold key was not opened or downloaded.

## Evidence accessibility

The Git repository inventories 227 imported files totaling 10,630,294 bytes. It contains source, reports, JSON/JSONL, logs, the frozen documents, and the G1 workbook. It does not contain a complete raw-data backup.

`provenance/EXTERNAL_ARTIFACTS.json` inventories 112 excluded artifacts totaling 1,937,034,397 bytes (about 1.804 GiB):

| Evidence family | Excluded bytes |
|---|---:|
| g0_evidence_v0_1 | 234,730,196 |
| g0_rca_v0_2 | 972,721,808 |
| g0_fix_v0_3 | 85,318,257 |
| g0_closure_v0_5 | 644,264,136 |

These require the original local evidence archive or the named Modal volumes. In addition, 115 per-prefix pipeline tensor files for each successful v0.5 run remain remote-only. The model weights are not in Git. Modal authentication, volume access, runtime networking, account balance, and billing were not tested in this audit.

## Package checks that passed

The annotation source table contains:

- 200 unique item IDs
- 50 unique task IDs, exactly four items per task
- 12 domains
- no missing values in the nine source fields
- valid JSON in all 200 `proposed_arguments` cells
- identical source columns in the A and B sheets
- execution classes: 52 Prepare, 80 Speculate, 64 Stage, and 4 Commit
- blank annotation fields in both annotator sheets

The rubric consistently defines the primary label as whether candidate work remains reusable without material re-execution, rather than whether the candidate is the most likely final intent.

## Issue registry

| ID | Severity | Evidence | Why it blocks or weakens G1 | Required remediation |
|---|---|---|---|---|
| G1-001 | Critical | Only 54/200 `prefix` values are normalized literal starts of `full_instruction`; 88 are later substrings and 58 are not contained. No task has four literal prefixes; 46/50 tasks contain at least one state absent from the final text. | The frozen protocol defines the primary unit as completed-word prefixes `x₁:ₜ`. The current rows appear to mix literal prefixes, later fragments, and counterfactual or edited states. Agreement on these rows would not establish reliability for the preregistered prefix construct. | Before annotation, either rebuild the pilot with true cumulative prefixes of a preserved final instruction, including explicit correction language in that instruction, or make a separately versioned protocol change defining observed edit states and their transition history. The first option preserves the frozen protocol and is recommended. |
| G1-002 | Critical | `Adjudication!D2:E201` directly reference blank source cells. Excel evaluates a reference to a blank cell as 0. The untouched workbook consequently shows 200 completed pairs, A prevalence 0, B prevalence 0, kappa 1, and gate status PASS. | The gate can pass without annotations. | Preserve blanks explicitly in the links, require exactly 200 valid paired labels, and test untouched, partially complete, balanced, imbalanced, and invalid-input cases before release. |
| G1-003 | Critical | The kappa formula returns 1 when expected agreement `Pe=1`, and the gate formula checks only `kappa >= 0.70`. | Kappa is undefined under degenerate one-class labeling. The protocol also requires non-degenerate prevalence. | Return `UNDEFINED` or `DEGENERATE` when `Pe=1`; fail or hold the gate. Freeze an outcome-independent non-degeneracy rule before labels are collected. |
| G1-004 | High | One workbook contains `Annotator_A`, `Annotator_B`, `Adjudication`, and `Pilot_Composition`. The composition sheet includes owner-derived aggregate label counts. | The package relies on annotators voluntarily avoiding the other sheet and exposes owner-derived prevalence information that can bias labels. | Generate separate A and B packets containing only instructions, ontology, and that annotator's rows. Exclude the other annotator, adjudication, owner-derived prevalence, gold key, and repository access. |
| G1-005 | High | The completed-pair metric checks binary labels only. It does not require fractional utility, confidence, ambiguity flag, or rationale. | The workbook can report a gate result while required annotation fields remain incomplete. | Validate every required field on all 200 rows before computing the gate; report missing/invalid cells and block aggregation. |
| G1-006 | High | The combined workbook permits adjudicated labels on all rows and does not enforce that independent sheets are complete before adjudication. It does not construct one final label from agreement-or-third-review logic. | Early or over-broad adjudication can contaminate independence, and the final label provenance is unclear. | Lock independent returns first, compute kappa before adjudication, create a disagreement-only third-annotator packet, then calculate final labels as agreed A/B labels or the third label for disagreements. Preserve all raw labels. |
| G1-007 | Medium | Data validation exists for binary label, fractional utility, confidence, ambiguity, and adjudicated label, but the source columns are not protected and rationale has no completeness control. | Accidental edits to stimulus text or IDs could break alignment; validation alone does not force completion. | Protect source columns, leave response cells editable, validate rationales as nonblank during collection, and compare returned source hashes/IDs to the frozen packet manifest. |
| G1-008 | Medium | The rubric gives three worked examples, but no pre-label comprehension check or recorded attestation is defined. | Annotators may misunderstand the difference between intent correctness and work-product reuse despite reading the rubric. | Add an unscored, fixed comprehension exercise and independence attestation before the 200 items. Keep it outside the scored pilot and version it before use. |

## Synthetic agreement checks

A reference calculation produced the expected results:

| Case | Paired n | Observed agreement | Expected agreement | Kappa | Required interpretation |
|---|---:|---:|---:|---:|---|
| Perfect balanced agreement | 4 | 1.00 | 0.50 | 1.00 | Defined |
| Balanced chance agreement | 4 | 0.50 | 0.50 | 0.00 | Defined |
| Both annotators label every item 0 | 4 | 1.00 | 1.00 | Undefined | Degenerate; never PASS |
| One pair missing | 3 | 0.667 | 0.444 | 0.40 | Incomplete for a 200-item gate |

The current workbook fails the untouched and degenerate cases.

## Recommended blinded G1 workflow

### 1. Resolve the stimulus construct

Use true cumulative text prefixes to remain within the frozen protocol. For intended reversals, preserve the earlier text and the correction in the full instruction, for example: “Find economy fares; actually make that business class.” Do not use a cleaned final instruction that erases the observed earlier state.

Version the corrected item package as a successor. Preserve v0.1 unchanged and record a row-level change manifest. Recheck unique IDs, task grouping, domains, source completeness, JSON validity, prefix continuity, and absence of future-information leakage.

### 2. Freeze independent packets

Create two byte-distinct, content-equivalent annotator packets with stable `item_id` keys:

- README with the labeling task and independence rules
- execution ontology
- one annotator sheet only
- response fields for binary label, fractional utility, confidence, ambiguity, and rationale
- data validation and protected stimulus columns
- an unscored comprehension exercise using examples outside the 200 scored items
- packet version, generation commit, and SHA256 manifest

Do not include the other annotator sheet, adjudication metrics, owner prevalence, the gold key, or repository access. Do not reveal aggregate owner labels.

### 3. Collect independent annotations

Each annotator completes all 200 items without discussing them with the other. Record only a pseudonymous annotator ID, packet hash, start/finish timestamps, rubric version, and an independence attestation. Do not begin adjudication until both immutable returns pass structural validation.

### 4. Validate returns

For each return:

- packet/source IDs and stimulus hashes match the frozen manifest
- exactly 200 unique items are present
- binary labels are integers in {0,1}
- fractional utility is numeric in [0,1]
- confidence is an integer in [1,5]
- ambiguity is Y or N
- rationale is nonblank
- no stimulus field changed

Block the gate if any requirement fails. Preserve the original returns and perform corrections through a logged query process rather than overwriting raw responses.

### 5. Compute pre-adjudication reliability

Join by `item_id`, never row position. Require 200 complete pairs. Report the 2x2 agreement table, observed agreement, expected agreement, Cohen's kappa, each annotator's prevalence, overall disagreement count, and results by domain and execution class as descriptive diagnostics.

G1 cannot pass when kappa is undefined, prevalence is degenerate, paired n is below 200, or required fields are incomplete. Fix the exact non-degeneracy rule before collection. A pilot-specific minimum minority-class count is preferable to the weak rule “both classes appear,” but adopting a numeric threshold requires a versioned owner decision before labels are seen.

### 6. Adjudicate disagreements

After the independent gate calculation, create a third-annotator packet containing only disagreement items and the source fields needed for a de novo judgment. The adjudicator should assign a label before seeing A/B identities or the owner key. Preserve the third label and rationale.

Construct the final pilot label as:

- the agreed A/B label when A and B agree
- the third annotator's label when A and B disagree

Kappa remains the pre-adjudication A-versus-B statistic. Adjudication must not overwrite it.

### 7. Gate and archive

G1 passes only when all of the following are true:

- corrected, protocol-conformant stimulus package frozen before labeling
- two complete independent returns
- Cohen's kappa is defined and at least 0.70
- the predeclared non-degeneracy condition passes
- every A/B disagreement has a third label and rationale
- source integrity and item alignment checks pass

Archive the rubric, packets, manifests, untouched returns, calculation output, disagreement packet, adjudicator return, final-label table, and a signed gate report. Keep the owner key separate and do not use it to fill, repair, or replace independent labels.

## Owner inputs required

1. Confirm the stimulus interpretation. Recommended: keep the frozen completed-word-prefix definition and rebuild the 200-item pilot with literal cumulative prefixes. The alternative—edited intermediate states—requires a separately versioned protocol definition and transition data.
2. Approve a precise non-degenerate-prevalence rule before annotation. Recommended for discussion: at least 20 labels in each class per annotator for this 200-item pilot; do not adopt this silently.
3. Name or authorize selection of two independent annotators and one third adjudicator. No one has been contacted.
4. Choose the secure delivery/return channel, compensation, deadline, and whether annotator identities remain outside the repository.
5. Decide whether the adjudicator labels disagreements de novo before receiving anonymized A/B rationales. De novo first is recommended to limit anchoring.
6. Authorize a versioned v0.2 package repair after the preceding choices. The existing v0.1 files should remain untouched.
7. Separately decide whether and how a future runner will authenticate to Modal. No Modal work is needed for G1 and no GPU authorization follows from this assessment.

## Resource and protocol impact

- New GPU cost: $0
- Modal jobs: none
- Annotation cost: $0
- Confirmatory data accessed: no
- Gold key used as independent evidence: no
- G0 status changed: no
- Frozen scientific endpoints changed: no
- Numerical configuration changed: no

## Next allowed action

Obtain the owner's decisions above, then create and validate a versioned G1 v0.2 pilot package on a review branch. Do not distribute it until the prefix construct, non-degeneracy rule, packet contents, and adjudication procedure are fixed in advance. Stage 1 remains blocked until G1 passes and the later development-length preflight is complete.
