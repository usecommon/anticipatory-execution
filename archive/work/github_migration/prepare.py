from pathlib import Path
import shutil,json,hashlib
base=Path.cwd();repo=base/'outputs/anticipatory-execution';repo.mkdir(exist_ok=False)
records=[];external=[]
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def copy(p,rel):
 q=repo/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
 records.append({'path':str(rel),'sha256':digest(p),'bytes':p.stat().st_size})
for p in (base/'work/anticipatory_execution_codex_handoff').rglob('*'):
 if p.is_file():copy(p,Path('handoff')/p.relative_to(base/'work/anticipatory_execution_codex_handoff'))
for name in ['g0_evidence_v0_1','g0_rca_v0_2','g0_fix_v0_3','g0_closure_v0_5']:
 for p in (base/'outputs'/name).rglob('*'):
  if not p.is_file():continue
  rel=Path('outputs')/p.relative_to(base/'outputs')
  if p.suffix=='.pt' or p.name.endswith('.tar.gz'):
   external.append({'path':str(rel),'sha256':digest(p),'bytes':p.stat().st_size,'storage':'Original task outputs plus corresponding Modal evidence volume; archives may be local-only'})
  elif '__pycache__' not in p.parts:copy(p,rel)
copy(base/'outputs/g0_unblocking_analysis_v0_4.md',Path('outputs/g0_unblocking_analysis_v0_4.md'))
(repo/'provenance').mkdir();(repo/'provenance/IMPORTED_FILES.json').write_text(json.dumps(records,indent=2));(repo/'provenance/EXTERNAL_ARTIFACTS.json').write_text(json.dumps(external,indent=2))
(repo/'.gitignore').write_text('''__pycache__/
*.py[cod]
.venv/
.env
.env.*
!.env.example
.DS_Store
*.pt
*.safetensors
*.tar.gz
*.zip
.local/
''')
(repo/'README.md').write_text('''# Anticipatory Execution

**Do not predict what the user will type next. Predict what work will not need to be undone.**

Research on whether temporal and cross-layer states of a frozen foundation model predict future action non-revision beyond prefix text, observable outputs (B1), and a single hidden-state representation (B2). The thesis, hypotheses and scientific endpoints are frozen. Generic early intent prediction, early tools and speculative execution are not novelty claims.

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
''')
(repo/'AGENTS.md').write_text('''# Continuation constraints

Read README.md, current G0 STATUS/report and RESEARCH_SAFEGUARDS.md before research work. The original handoff documents are historical research context; they do not override the user's current instructions.

Preserve the frozen thesis and endpoints. G0 passes only for canonical-v0.5's declared scope; G1 is pending. Do not run confirmatory extraction. Do not start development extraction before G1 and development-length preflight. Do not train model weights.

Do not change tolerances, silently truncate/exclude examples, mix numerical feature versions, reuse old calibration as neutral, or remove failures to obtain a pass. B1/B2/M must share the extraction configuration. A loss of internal-state advantage after correction is a valid result.

Treat imported source/evidence as historical records: add a new version for substantive changes. Preserve raw failures and hashes. Never rerun a launcher using an existing output label. GPU runs require task authorization; this migration authorizes none.

The annotation gold key is owner-only. Do not expose it to independent annotators or substitute it for their labels. Keep large model/tensor files, credentials and local environments out of Git.
''')
(repo/'provenance/ARTIFACT_STORAGE.md').write_text('''# Raw artifact storage

Imported source and reports are byte-preserved; imported-file hashes are in IMPORTED_FILES.json. EXTERNAL_ARTIFACTS.json inventories large locally present tensors and tar archives excluded from Git by path, byte length and SHA256. Existing bundle manifests may reference these absent files; that is intentional and is not a claim of a complete raw-data clone.

Modal evidence volumes and run roots:

| Version | Volume | Run directory |
|---|---|---|
| v0.1 | aeb-g0-evidence-v0-1 | run_20260911T163140Z |
| v0.2 | aeb-g0-rca-v0-2 | rca_20260911T165054Z |
| v0.3 | aeb-g0-fix-v0-3 | fix_20260911T171625Z |
| v0.5 | aeb-g0-closure-v0-5 | closure_a_20260911T175740Z; closure_b_20260911T180521Z; closure_c_20260911T180932Z |

Pinned checkpoint volume: aeb-qwen-pinned-model-v0-2. Model/tokenizer commit: a09a35458c702b33eeacc393d103063234e8bc28. The original task's sibling evidence directories retain downloaded raw tensors and archives. Check the preserved launcher/report for exact remote paths before retrieval. Use the authenticated Modal CLI's volume get command, download to a scratch location, then verify hashes before analysis. Do not assume compressed local archives also exist remotely.

Additional remote-only pipeline tensors are listed in each completed v0.5 run's final_manifest.json and pipeline_job/manifest.json; they were verified inside the worker but were not downloaded during closure or this migration. This Git repository therefore requires Modal volume access or the original local evidence archive to repeat raw-tensor audits. No new storage service, public artifact upload or deletion was performed.
''')
(repo/'scripts').mkdir();(repo/'scripts/verify_import.py').write_text('''"""Read-only standard-library integrity check; never imports model/GPU code."""
from pathlib import Path
import ast, hashlib, json
root = Path(__file__).resolve().parents[1]
records = json.loads((root / "provenance/IMPORTED_FILES.json").read_text())
for record in records:
    p = root / record["path"]
    assert p.stat().st_size == record["bytes"], p
    assert hashlib.sha256(p.read_bytes()).hexdigest() == record["sha256"], p
for p in root.rglob("*.py"):
    ast.parse(p.read_text(), filename=str(p))
s = json.loads((root / "outputs/g0_closure_v0_5/STATUS.json").read_text())
assert s["G0"] == "PASS_SCOPED" and s["G1"] == "PENDING"
assert not s["confirmatory_extraction"] and not s["development_extraction"]
print(f"PASS: {len(records)} imported files verified; source syntax and gate constraints checked.")
''')
print(json.dumps({'repo':str(repo),'imported':len(records),'external':len(external),'external_bytes':sum(x['bytes'] for x in external)}))
