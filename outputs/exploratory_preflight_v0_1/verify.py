"""Verify source identity, split boundaries, trajectory alignment and preflight."""
import hashlib,json,re,tempfile,subprocess,shutil
from collections import defaultdict
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jl(p):return [json.loads(x) for x in p.read_text().splitlines()]
for p,h in json.loads((O/'SOURCE_HASHES.json').read_text()).items():assert sha(R/p)==h,p
for p,h in json.loads((O/'INPUT_FREEZE.json').read_text()).items():assert sha(O/p)==h,p
inputs=jl(O/'EXTRACTION_INPUT.jsonl');im={r['id']:r for r in inputs}
assert len(inputs)==len(im) and all(set(r)=={'id','prefix'} for r in inputs)
source=jl(R/'outputs/checkpoint_human_pilot_v0_1/ALL_CHECKPOINTS.jsonl');sm={r['item_id']:r for r in source};tasks={r['task_id']:r for r in source}
opps=jl(O/'OPPORTUNITIES.jsonl');assert set(r['item_id'] for r in opps)==set(sm)
groups={};bytask={};byprefix=defaultdict(set)
for r in opps:
 s=sm[r['item_id']];assert r['checkpoint_status']==s['checkpoint_status'] and r['proposal_status']==s['proposal_status']
 bytask.setdefault(r['task_id'],r['split']);assert bytask[r['task_id']]==r['split']
 k=(r['source'],r['template_group']);groups.setdefault(k,r['split']);assert groups[k]==r['split']
 if 'input_id' in r:
  assert im[r['input_id']]['prefix']==s['prefix'];byprefix[r['input_id']].add(r['split'])
assert all(len(v)==1 for v in byprefix.values())
for r in jl(O/'TRAJECTORY_MAPPING.jsonl'):
 s=tasks[r['task_id']]['full_instruction'];end=list(re.finditer(r'\S+',s))[r['checkpoint_words']-1].end()
 assert im[r['input_id']]['prefix']==s[:end] and r['split']==bytask[r['task_id']]
labels=jl(O/'LABELS_COORDINATOR_ONLY.jsonl');orig={r['item_id']:r for r in jl(R/'outputs/checkpoint_ai_judge_v0_1/results/MAIN_200.jsonl')}
assert len(labels)==200 and set(r['item_id'] for r in labels)==set(orig)
for r in labels:
 assert r['binary_usefulness']==orig[r['item_id']]['judge']['binary_usefulness_0_or_1']
 assert r['ambiguity']==orig[r['item_id']]['judge']['ambiguity_flag_Y_N']
# Replay frozen manifest construction, then perturb labels to show split independence.
with tempfile.TemporaryDirectory() as td:
 tr=Path(td);to=tr/'outputs'/O.name;to.mkdir(parents=True)
 shutil.copy(O/'prepare.py',to/'prepare.py')
 for rel in json.loads((O/'SOURCE_HASHES.json').read_text()):
  dest=tr/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy(R/rel,dest)
 subprocess.run(['python3',str(to/'prepare.py')],check=True)
 compared=[]
 for p in O.iterdir():
  if p.name in ['INPUT_FREEZE.json','SOURCE_HASHES.json','PLAN.json','MANIFEST.json'] or p.suffix=='.jsonl':
   assert p.read_bytes()==(to/p.name).read_bytes(),p.name;compared.append(p.name)
 labelpath=tr/'outputs/checkpoint_ai_judge_v0_1/results/MAIN_200.jsonl'
 changed=jl(labelpath)
 for r in changed:r['disposition']='perturbed';r['judge']['binary_usefulness_0_or_1']=None
 labelpath.write_text(''.join(json.dumps(r)+'\n' for r in changed))
 for p in list(to.iterdir()):
  if p.name!='prepare.py':p.unlink()
 subprocess.run(['python3',str(to/'prepare.py')],check=True)
 for name in ['COMPONENTS.jsonl','GROUP_EDGES.jsonl','EXTRACTION_INPUT.jsonl','TRAJECTORY_MAPPING.jsonl','OPPORTUNITIES.jsonl']:
  assert (O/name).read_bytes()==(to/name).read_bytes(),name
results=sorted(O.glob('run_*/RESULT.json'));assert results,'No completed preflight'
for p in results:
 d=json.loads(p.read_text());request=json.loads(p.with_name('REQUEST.json').read_text())
 assert request['input_sha256']==sha(O/'EXTRACTION_INPUT.jsonl')
 assert d['status']=='PASS' and not d['model_loaded'] and not d['extraction'] and not d['gpu']
 rr={r['id']:r for r in d['rows']};assert set(rr)==set(im)
 for k,r in rr.items():
  assert r['prefix_sha256']==hashlib.sha256(im[k]['prefix'].encode()).hexdigest()
  assert r['active_length']==len(r['token_ids']) and r['fits_128'] and 1<=r['active_length']<=128
 assert d['tokenizer_backend_sha256']==json.loads((R/'outputs/g0_closure_v0_5/closure_c_20260911T180932Z/contract.json').read_text())['tokenizer_hash']
print('PASS: frozen sources, complete denominators, grouped splits, prefix-only payload, dense alignment, original labels, byte-identical replay, label-perturbation independence, exact tokenizer preflight.')
