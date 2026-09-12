# Collection assembly and package privacy audit

Status: PASS for arithmetic, deterministic selection, artifact preservation, package payload projection, ZIP membership, and frozen hashes. No human labels were created or assessed.

## Scope and auditor exposure

This reused auditor session has prior BFCL adjudication and shared-policy source/AI-result exposure. This role is structural arithmetic and artifact privacy auditing, not a new independent human annotator. The audit inspected the new checkpoint folder's assembly/package scripts, frozen inputs and proposals, assembled opportunities, selection/control files, coordinator mappings, package files, and manifests. The sole older task/product source inspected was the allowed shared-policy ALL_OPPORTUNITIES.jsonl; no older ratings, gold, or owner key was accessed for this audit.

Independent read-only Python assertions reconstructed the joins, selection, group reuse, package projection, and hashes. The assembly and packaging programs were read but not executed or imported. No fixture or candidate ran, no external service was contacted, and no invitation or human response was sent. Only this report was authored. User-facing UI interaction testing and any later submission-collector review are outside this report.

## Opportunity and review-pool accounting

| Opportunity set | Scheduled | Proposed task rows | Eligible abstentions | Complete/unreached |
| --- | ---: | ---: | ---: | ---: |
| Frozen six-word baseline | 300 | 87 | 213 | 0 |
| New 12/18-word checkpoints | 600 | 173 | 303 | 124 |
| Combined | 900 | 260 | 516 | 124 |

All 900 IDs are unique, and every original task has exactly one scheduled opportunity at each of 6, 12, and 18 words. The 600 later rows preserve the scheduled context exactly. Their 476 eligible opportunities use the exact raw proposal assigned to their prefix group; their 124 ineligible opportunities retain null action/class/product/rationale and not_eligible status. No endpoint case is converted into a proposer abstention or a reuse label.

All 473 raw later-prefix outputs appear exactly once across their assigned shards. Of these, 170 are proposed artifacts and 303 are abstentions. Reuse across repeated exact prefixes expands the 170 distinct proposal records to 173 proposed task rows, with no product rewriting. The 300 six-word rows retain every selected source/proposal field exactly from the old ALL_OPPORTUNITIES source and add only the declared checkpoint lineage fields. No old rating is joined.

REVIEW_POOL.jsonl is exactly the ordered proposed-status subset of the combined file: 260 rows, comprising 124 public and 136 synthetic candidates. The 516 abstentions and 124 ineligible rows remain in the complete scheduled accounting, outside the proposed-work review pool. Raw proposal schemas, nonempty rationales, integer classes 1/2/3, and abstention null requirements pass.

## Deterministic main selection

The 200 selected rows exactly match independent reconstruction of the declared algorithm: per-source SHA-256 ranking using human-main-v1 and item ID, then first encountered candidate per distinct task before additional checkpoints, an initial cap of 100 per source, and human-fill-v1 ranking only for any remaining total shortfall. Selection uses no AI label, ambiguity, sufficiency result, or expected reuse. Both sources have at least 100 candidates, so no cross-source fill or total shortfall occurs.

| Source | Pool candidates | Distinct available tasks | Selected main cases | Selected distinct tasks | Extra checkpoint rows |
| --- | ---: | ---: | ---: | ---: | ---: |
| Public BFCL | 124 | 86 | 100 | 86 | 14 |
| Synthetic | 136 | 83 | 100 | 83 | 17 |
| Total | 260 | 169 | 200 | 169 | 31 |

The selected checkpoint counts are 65 at six words, 55 at twelve words, and 80 at eighteen words. There are 169 distinct tasks and 131 source-qualified template groups. These counts and every source/checkpoint count in STATUS.json were recomputed. The source balance is a review-sample design choice, not preservation of the original 200/100 task mix or a population prevalence estimate. Related checkpoints and families remain dependent.

## Separate boundary controls

The 20 controls exactly match the first 20 main cases ranked with human-boundary-v1. Their coordinator IDs are distinct from main IDs; each points to its correct selected parent. The four constructions rotate exactly five times each: copied prefix, empty table, unknown-slot list, and generic checklist. All retain the parent's context and use the declared replacement artifact and class 1.

Controls are separately tracked coordinator-side and are not part of the 200 main cases, the 260 naturally proposed review-pool rows, or the 900 scheduled opportunities. Their inclusion produces 220 package cases per reviewer. Their authored nature and expected boundary purpose do not create a human label or a valid additional G1 observation.

## Package projection and archive contents

Both packages contain precisely the same 200 main and 20 control cases, with independently ordered A### and B### IDs. Coordinator mappings are 220-case bijections; each packaged prefix, candidate action, work product, declared execution class, and full instruction matches its mapped selected or control record exactly. The documented random seeds reproduce both permutations, and the two orders differ.

Every ITEMS.json document has exactly package_id, reviewer_role, and items at top level. Every item has exactly item_id, prefix, candidate_action, work_product, execution_class, full_instruction, and fixture_contract. Canonical payload hashing reproduces each package ID. The embedded JSON in REVIEW.html equals ITEMS.json exactly, and the rest of each HTML file equals the declared template. Candidate text is inserted as JSON-escaped content and displayed through textContent; it is not treated as executable candidate code.

Each package directory and corresponding ZIP contains only:

- REVIEW.html
- ITEMS.json
- ORIGINAL_RUBRIC.txt
- START_HERE.md

Each ZIP has exactly four unique members under its expected Annotator_A or Annotator_B directory, with no extra file, directory record, mapping, parent path, or archive comment. Every archived member is byte-identical to its corresponding package file. The two rubric copies equal the frozen original rubric.

No explicit source field, task/family/checkpoint lineage field, coordinator ID, mapping, proposal-generation rationale, review-kind/control-type marker, parent-control reference, prior AI rating, prefilled response, or expected control label is included in the item payloads. Targeted scans across all four package files found no coordinator IDs or data markers. General rubric examples contain illustrative labels and discuss adjudication; those required instructions are not case-specific AI ratings or leaked control answers. An initial broad scan matched that ordinary rubric word; the check was narrowed to actual identifiers and data keys, and found no package leak.

The UI's response state starts empty. Its generic label choices and validation code are not prefilled decisions. The package instructions tell the reviewer to use only the assigned package, work independently, and return JSON privately. Static template inspection found no network endpoint or automatic upload; the page's content-security policy disables connections. Runtime rendering, import/export behavior, and complete UI validation are being tested separately and are not certified by this static audit.

This is metadata omission and controlled packaging, not a guarantee that provenance or controls are unrecognizable. Prefix word counts remain visible; source wording can reveal provenance; minimal controls can be recognized from their content; a reviewer may notice a parent/control pair. Package access alone does not establish actual human independence or lack of prior exposure. No declaration or package script proves a person's identity.

## Frozen hashes

All 2 source entries, 10 input-freeze entries, 2 raw-proposal entries, and 16 review-input-freeze entries match current SHA-256 values: 30 frozen entries in total. PACKAGE_MANIFEST.json additionally matches all eight package files and both ZIP hashes; package IDs independently reproduce from canonical item payloads. All frozen checks passed again after report creation.

The old six-word ALL_OPPORTUNITIES source still matches its previously audited hash. The later audit did not reopen old label/result files. Hash consistency is not independent timestamping, provenance authentication, or proof against coordinated replacement of files and manifests. This report is not part of the earlier freeze.

## Collection boundary

No arithmetic, selection, preservation, or explicit package-metadata privacy defect was found. No genuine human submission was inspected or created. The current packages support collecting two independent human submissions but do not establish such independence, completed judgments, sufficient resolved denominators, a third adjudicator, or G1 completion. Endpoint censoring and task/family dependence remain as documented in ADAPTER_AUDIT.md. The proposed human collection and boundary diagnostics remain separate from measured efficacy or latency claims.
