# Anticipatory Execution

**Do not predict what the user will type next. Predict what work will not need to be undone.**

Research on whether temporal and cross-layer states of a frozen foundation model predict future action non-revision beyond prefix text, observable outputs (B1), and a single hidden-state representation (B2). The thesis, hypotheses and scientific endpoints are frozen. Generic early intent prediction, early tools and speculative execution are not novelty claims.

For ChatGPT or Codex Cloud continuation, use the [detailed handoff and copy-ready startup prompt](docs/CHATGPT_CODEX_CLOUD_HANDOFF.md).

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
