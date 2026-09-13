"""Independent structural/provenance check of returned validation evidence."""
import ast,hashlib,json
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p in O.glob('*.py'):ast.parse(p.read_text())
for kind,pin in json.loads((O/'PINNED_INPUTS.json').read_text()).items():assert sha(R/pin['path'])==pin['sha256'],kind
success=[]
for run in O.glob('validation_*'):
 if not run.is_dir() or not (run/'GPU_RESULT.json').exists():continue
 cpu=json.loads((run/'CPU_RESULT.json').read_text());gpu=json.loads((run/'GPU_RESULT.json').read_text())
 if gpu['result']['status']!='PASS':continue
 for p,h in json.loads((run/'SOURCE_FREEZE.json').read_text()).items():assert sha(R/p)==h,p
 assert cpu['status']=='PASS' and cpu['synthetic_tensors_only'] and all(c['pass'] for c in cpu['checks'])
 names={c['name']:c for c in cpu['checks']}
 assert names['full_preflight_before_forward']['token_calls']==4013
 assert names['partial_failure_preserved']['forward_calls']==2
 assert names['late_overlength']['forward_calls']==0
 assert names['partition_confirmatory']['forward_calls']==0
 d=gpu['result'];assert d['actual_forward_count']==24 and not d['research_extraction']
 assert len(d['comparisons'])==12 and all(x['all_fields_bitwise_equal'] for x in d['comparisons'])
 assert d['confirmatory_rejection_zero_forwards'] and d['human_G1']=='PENDING_DEFERRED'
 assert d['contract_id']=='95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0'
 artifacts=gpu['artifacts'];hashes=json.loads(artifacts['HASHES.json'])
 for name,text in artifacts.items():
  if name!='HASHES.json':assert hashlib.sha256(text.encode()).hexdigest()==hashes[name],name
 old=json.loads(artifacts['original/manifest.json']);new=json.loads(artifacts['new/manifest.json'])
 assert old['partition']=='qa' and new['partition']=='instrumentation_validation'
 assert len(old['items'])==len(new['items'])==12
 for a,b in zip(old['items'],new['items']):
  for field in ['id','prefix_sha256','token_ids','active_length','contract_id']:assert a[field]==b[field]
 assert json.loads(artifacts['confirmatory_rejection/failure.json'])['completed_items']==0
 assert len([k for k in hashes if k.endswith('.pt')])==24
 success.append(run.name)
assert success,'No successful GPU validation evidence'
print('PASS: pinned files, source syntax/freeze, software rejection checks, full-input preflight, partial failure preservation, 12 GPU bitwise comparisons, zero-forward confirmatory rejection, returned artifact hashes. Raw tensors remain on Modal; equality was measured in worker.')
