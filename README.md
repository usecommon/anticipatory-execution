# Anticipatory Execution

**Do not predict what the user will type next. Predict what work will not need to be undone.**

Research on whether temporal and cross-layer states of a frozen foundation model predict future action non-revision beyond prefix text, observable outputs (B1), and a single hidden-state representation (B2). The thesis, hypotheses and scientific endpoints are frozen. Generic early intent prediction, early tools and speculative execution are not novelty claims.

For ChatGPT or Codex Cloud continuation, use the [detailed handoff and copy-ready startup prompt](docs/CHATGPT_CODEX_CLOUD_HANDOFF.md).

The additional full raw-evidence upload is currently **incomplete**; see [transfer status and recovery instructions](docs/GITHUB_EVIDENCE_RESTORE.md). All source/report material is available in Git, including `archive/work/`.

Use the [corrected G1 annotation workbook](outputs/g1_workbook_fix_v0_2/aeb_g1_annotation_pilot_200_v0_2.xlsx) for labeling; see its [calculation changes and validation](outputs/g1_workbook_fix_v0_2/CHANGELOG.md). The original workbook remains preserved.

The [public dataset audit](outputs/public_dataset_audit_v0_1/AUDIT.md) identifies reusable task sources and potential executable supervision; it does not waive G1 or change the protocol.

The [detailed public-dataset suitability research](outputs/public_dataset_research_v0_2/REPORT.md) recommends a BFCL development adapter with SGD for breadth, records pinned source checks and failures, and explains why new action-reuse validation is still needed.

The owner's [public-data and result-sensitivity requirement](docs/PUBLIC_DATA_AND_RESULT_SENSITIVITY.md) requires exact public source versions, traceable transformations and reproducible evaluation artifacts. Dataset changes may alter or reverse results. The current 50-task pilot candidate has unverified public provenance and remains diagnostic only.

The [200-item AI annotation trial](outputs/g1_ai_trial_v0_1/TRIAL_REPORT.md) is rubric-diagnostic work only. It does not close G1; keep its labels away from independent annotators until their submissions are preserved.

The [three-agent annotation and judgment study](outputs/g1_team_v0_1/TEAM_REPORT.md) preserves 600 AI ratings, original agreement and 26 unresolved judgments. High AI agreement does not close human G1 or establish dataset validity.

The [literal-prefix dataset candidate](outputs/prefix_dataset_candidate_v0_1/README.md) reconstructs 703 word-boundary observations from the 50 exposed pilot tasks. It has no new actions or labels and does not change the research gates.

The [public-plus-synthetic plan and 200-item expansion](outputs/synthetic_expansion_v0_1/README.md) preserves the original owner labels and records fresh AI adjudication: 136 reusable, 59 non-reusable and 5 unresolved. It remains private development material; public release, source adapters and human G1 are pending.

The [1,000-item synthetic curation](outputs/synthetic_curation_1000_v0_1/README.md) retains 665 reusable wording variants, archives 305 non-reusable items and quarantines 30. These derive from 50 substantive templates and have one AI judgment each; the positive-only subset is not a thesis evaluation dataset.

The [BFCL public-source pilot and synthetic comparison](outputs/bfcl_public_pilot_v0_1/README.md) covers 200 six-word proposal opportunities: 59 proposed artifacts, 141 abstentions; AI adjudication yields 24 reusable, 7 non-reusable and 28 unresolved. Differences from synthetic construction are confounded; no matched source-effect or model-efficacy result is claimed.

The [shared-policy public/synthetic pilot](outputs/shared_policy_pilot_v0_1/README.md) now uses the same six-word checkpoint and proposal/rating policy on 200 public and 100 synthetic tasks: 87 proposed products, 58 reusable, 25 non-reusable, 4 unresolved and 213 abstentions. Source/domain differences and dependent variants remain; human G1 and model efficacy testing are still pending.

## Current state

- **G0 PASS, scoped:** canonical-v0.5, frozen Qwen2.5-7B-Instruct, NVIDIA A100-SXM4-40GB, FP32 eager, physical shape [1,128], active length 1..128, serial prefixes, explicit positions/masks, cache off. Two fresh Modal containers passed 8,427 checks each; 155 cross-container cases matched bitwise.
- **G1 PENDING:** two independent annotators and prescribed agreement/adjudication are still required.
- **Stage 1 BLOCKED. No confirmatory extraction.** The executable permits QA only.
- Corrections are **not presumed numerically neutral**. Historical failures remain failures. Changes may reduce or eliminate the apparent internal-state advantage.

Start with [closure report](outputs/g0_closure_v0_5/G0_CLOSURE_REPORT.md), [research safeguards](outputs/g0_closure_v0_5/RESEARCH_SAFEGUARDS.md), and [runbook](outputs/g0_closure_v0_5/RUNBOOK.md). Machine-readable current status: [STATUS.json](outputs/g0_closure_v0_5/STATUS.json).

## Repository contents

- `handoff/`: byte-preserved original handoff, protocol, literature review, annotation package and originating status. Historical status documents describe their own time, not the current gate.
- `outputs/g0_evidence_v0_1/`: reconstructed sequence-length failure before mitigation.
- `outputs/g0_rca_v0_2/`: projection-level RCA and preserved unsuccessful interventions.
- `outputs/g0_fix_v0_3/`: initial canonical candidate and native failures.
- `outputs/g0_unblocking_analysis_v0_4.md`: scoped gate analysis.
- `outputs/g0_closure_v0_5/`: validated source, frozen plans, safeguards, all closure attempts and adjudication.
- `provenance/`: imported-file hashes and inventory of large external artifacts.

Validated code stays at its original relative layout to avoid modifying the hashed implementation merely for repository organization. No GPU job, annotation, development extraction or confirmatory run is triggered by this migration. No Actions workflow launches paid computation.

## Verify the migration locally

```sh
python3 scripts/verify_import.py
```

This uses only the standard library and verifies every imported file against its migration checksum, parses Python source, and checks the recorded gate state. It does not substitute for G0 or rerun inference.

For a later authorized QA rerun, read the runbook and create a versioned launcher with a unique run label/output path; retained launchers have already-used filenames and must not overwrite evidence. Modal authentication and access to the named private volumes are required. Dependencies are pinned in the preserved Modal image definitions. Model weights are not in Git.

## Evidence and annotation access

Large tensors and duplicate compressed archives remain outside Git with SHA256 inventories; see [artifact storage](provenance/ARTIFACT_STORAGE.md). This is a source/report repository, not a self-contained copy of all raw tensors. Original local evidence is unchanged.

Keep this repository private. The owner-only gold key in `handoff/aeb_g1_pilot_gold_key.jsonl` must remain inaccessible to independent annotators; give annotators only their blind workbooks/rubric, not repository access. The key does not constitute independent annotation. No open-source license or public release is implied by this migration.
