import argparse,hashlib,json,random,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--submissions',type=Path,required=True);a=ap.parse_args()
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
def write(n,rs):
 f=p/n;assert not f.exists(),f;f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
for n,h in json.loads((p/'INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h
props={};hashes={}
for n in [1,2]:
 f=a.submissions/f'shared_proposer_{n}.jsonl';rs=read(f);inp=read(p/f'PROPOSER_{n}_INPUT.jsonl');assert len(rs)==len(inp) and {x['item_id'] for x in rs}=={x['item_id'] for x in inp}
 for r in rs:
  assert r['proposal_status'] in ['proposed','abstain'] and r['prefix_support'].strip()
  if r['proposal_status']=='abstain':assert all(r[k] is None for k in ['candidate_action','execution_class','work_product'])
  else:assert type(r['execution_class']) is int and r['execution_class'] in [1,2,3] and r['candidate_action'].strip() and r['work_product'].strip()
  assert r['item_id'] not in props;props[r['item_id']]=r
 assert not (p/f.name).exists();shutil.copyfile(f,p/f.name);hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
(p/'PROPOSAL_FREEZE.json').write_text(json.dumps(hashes,indent=2)+'\n')
allrows=[]
for r in read(p/'EVALUATOR_CONTEXT.jsonl'):
 prop=props[r['prefix_group']];allrows.append({**r,**{k:v for k,v in prop.items() if k!='item_id'},'fixture_contract':'Local AI-authored prefix-only preparation, not executed/retrieved output. No unmentioned source state or tool capabilities may be assumed.'})
write('ALL_OPPORTUNITIES.jsonl',allrows);proposed=[r for r in allrows if r['proposal_status']=='proposed'];write('PROPOSED_ITEMS.jsonl',proposed)
for n,seed in [('A',260912303),('B',260912304)]:
 order=list(proposed);random.Random(seed).shuffle(order);rs=[];mp=[]
 for i,r in enumerate(order,1):
  bid=f'{n}{i:03d}';mp.append({'blind_id':bid,'item_id':r['item_id']});rs.append({'item_id':bid,**{k:r[k] for k in ['prefix','candidate_action','work_product','execution_class','full_instruction','fixture_contract']}})
 write(f'RATER_{n}_INPUT.jsonl',rs);write(f'RATER_{n}_MAPPING.jsonl',mp)
(p/'REVIEW_FREEZE.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.iterdir()) if f.name.startswith('RATER_') or f.name in ['REVIEWER_INSTRUCTIONS.txt','ALL_OPPORTUNITIES.jsonl','PROPOSED_ITEMS.jsonl']},indent=2)+'\n')
print(json.dumps({'opportunities':len(allrows),'proposed_items':len(proposed),'unique_prefix_proposals':sum(r['proposal_status']=='proposed' for r in props.values())}))
