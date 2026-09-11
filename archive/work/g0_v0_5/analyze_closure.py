"""Independent local audit of downloaded closure evidence. No GPU calls."""
import json,tarfile,hashlib,sys,collections
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_saved_tensors import load
root=Path('outputs/g0_closure_v0_5');runs=[];checks=[]
for label in ['closure_a','closure_b']:
 with tarfile.open(root/(label+'.tar.gz')) as t:t.extractall(root,filter='data')
 r=next(p for p in root.glob(label+'_*') if p.is_dir());runs.append(r)
 manifest=json.loads((r/'final_manifest.json').read_text())
 verify={k:hashlib.sha256((r/k).read_bytes()).hexdigest()==v for k,v in manifest.items() if (r/k).is_file()}
 checks.append({'name':label+'_download_hashes','status':'PASS' if all(verify.values()) else 'FAIL','verified':len(verify),'remote_only':len(manifest)-len(verify)})
 if not (r/'summary.json').exists():
  checks.append({'name':label+'_completion','status':'FAIL','detail':(r/'failure.txt').read_text() if (r/'failure.txt').exists() else 'No summary'})
  continue
 summary=json.loads((r/'summary.json').read_text());checks.append({'name':label+'_suite','status':summary['status'],'summary':summary})
if not all((r/'summary.json').exists() for r in runs):
 (root/'closure_adjudication.json').write_text(json.dumps({'gate':'G0','status':'BLOCKED','checks':checks},indent=2));print(json.dumps(checks,indent=2));sys.exit(2)
a,b=[load(r/'comparison_states.pt') for r in runs]
ca,cb=[json.loads((r/'contract.json').read_text()) for r in runs]
ea,eb=[json.loads((r/'environment.json').read_text()) for r in runs]
checks.append({'name':'identical_contract','status':'PASS' if ca==cb else 'FAIL'})
id_a=ea.get('container_id') or ea.get('hostname');id_b=eb.get('container_id') or eb.get('hostname')
checks.append({'name':'distinct_containers','status':'PASS' if id_a and id_b and id_a!=id_b else 'FAIL','container_a':id_a,'container_b':id_b})
checks.append({'name':'identical_case_set','status':'PASS' if a.keys()==b.keys() else 'FAIL','cases':len(a)})
for key in a.keys() & b.keys():
 for field in ['hidden_last','logits_last']:
  x,y=a[key][field],b[key][field];finite=np.isfinite(x).all() and np.isfinite(y).all();ok=finite and np.allclose(x,y,atol=1e-5,rtol=1e-5)
  checks.append({'name':key+'_'+field,'status':'PASS' if ok else 'FAIL','bitwise_equal':bool(np.array_equal(x,y)),'max_abs':float(np.max(np.abs(x-y)))})
 for field in ['hidden_all_sha','logits_all_sha']:
  same=a[key][field]==b[key][field]
  checks.append({'name':key+'_'+field,'status':'PASS' if same else 'FAIL','detail':'Full active-state digest equality. If unequal, do not infer allclose from last-state equality; full comparison remains required.'})
 # Independently validate token and position alignment in the actual saved snapshots.
 for field in ['input_ids','attention_mask','position_ids']:
  checks.append({'name':key+'_'+field,'status':'PASS' if np.array_equal(a[key][field],b[key][field]) else 'FAIL'})
status='PASS' if all(c['status']=='PASS' for c in checks) else 'BLOCKED'
report={'gate':'G0','status':status,'scope':'canonical-v0.5 only; active length 1..128; frozen Qwen commit and exact A100/FP32/eager configuration','checks':checks,'cross_container_case_count':len(a),'failures':sum(c['status']=='FAIL' for c in checks),'G1':'PENDING','research_extraction_enabled':False,'numerical_neutrality_claim':False}
(root/'closure_adjudication.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
