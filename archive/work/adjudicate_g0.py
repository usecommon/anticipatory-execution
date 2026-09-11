import json,hashlib,tarfile
from pathlib import Path
from collections import Counter
root=Path('outputs/g0_evidence_v0_1')
a=root/'modal_run_01.tar.gz'
with tarfile.open(a) as t:t.extractall(root,filter='data')
run=next(root.glob('run_*'))
checksums=json.loads((run/'SHA256SUMS.json').read_text())
verification={k:hashlib.sha256((run/k).read_bytes()).hexdigest()==v for k,v in checksums.items()}
# Worker log remains open during checksum generation; only finalized artifacts are stable.
verification.pop('worker.log',None)
(root/'download_verification.json').write_text(json.dumps(verification,indent=2))
original=json.loads((run/'original_harness_report.json').read_text()) if (run/'original_harness_report.json').exists() else None
length=json.loads((run/'length_reproduction.json').read_text()) if (run/'length_reproduction.json').exists() else None
checks=json.loads((run/'checks_incremental.json').read_text()) if (run/'checks_incremental.json').exists() else []
execution=json.loads((run/'execution.json').read_text())
summary={'gate':'G0','status':'FAIL' if (original and original['status']=='FAIL') or any(x['status']=='FAIL' for x in checks) else 'BLOCKED','original_harness_status':original['status'] if original else 'NOT_COMPLETED','original_counts':dict(Counter(x['status'] for x in original['checks'])) if original else {},'length_outside_tolerance':length['outside_tolerance'] if length else None,'length_total':length['total'] if length else None,'supplemental_counts':dict(Counter(x['status'] for x in checks if not x['name'].startswith('length_'))),'worker_failure':(run/'worker_failure.txt').read_text() if (run/'worker_failure.txt').exists() else None,'execution':execution,'exact_historical_replay':False,'confirmatory_extraction':False,'all_finalized_artifact_checksums_verified':all(verification.values())}
(root/'adjudication.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
