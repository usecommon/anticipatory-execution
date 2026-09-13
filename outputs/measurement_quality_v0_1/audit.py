"""Structural readiness inventory; never assigns or revises usefulness labels."""
import json,hashlib
from collections import Counter
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
p=R/'outputs/checkpoint_ai_judge_v0_1/results/MAIN_200.jsonl';cases=[json.loads(x) for x in p.read_text().splitlines()]
required=['pinned_environment','typed_candidate','execution_receipt','reuse_trace','independent_task_check']
rows=[{'item_id':r['item_id'],'source':r['source'],'missing_structured_evidence':[k for k in required if not isinstance(r.get(k),dict)],'artifact_is_text':isinstance(r.get('work_product'),str),'readiness_scope':'Fields in frozen case record only; not a semantic usefulness judgment'} for r in cases]
(O/'CASE_READINESS.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rows))
comp=R/'outputs/exploratory_comparison_v0_1/run_20260913T013948081119Z/RESULT.json';result=json.loads(comp.read_text());slices=result['scenarios']['current_resolved']['check_source_slices']['D_text']
report={'status':'AUDIT_COMPLETE','case_records':len(rows),'source_counts':dict(Counter(r['source'] for r in rows)),'records_ready_for_proposed_execution_receipt_contract':sum(not r['missing_structured_evidence'] for r in rows),'missing_field_counts':{k:sum(k in r['missing_structured_evidence'] for r in rows) for k in required},'check_source_coverage':{k:{x:v[x] for x in ['cases','tasks','positive','negative']} for k,v in slices.items()},'interpretation':'Existing case text cannot be automatically admitted to this proposed execution-receipt interface. This does not mark cases non-reusable or prove no useful work exists. No real artifact was executed.','source_hashes':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest(),str(comp.relative_to(R)):hashlib.sha256(comp.read_bytes()).hexdigest()}}
(O/'READINESS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['source_hashes','interpretation']},indent=2))
