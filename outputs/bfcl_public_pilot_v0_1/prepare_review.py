import argparse,hashlib,json,random,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--submissions',type=Path,required=True);a=ap.parse_args()
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
def write(n,rs):
 f=p/n
 if f.exists():raise RuntimeError('Refuse overwrite '+n)
 f.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rs))
for f,h in json.loads((p/'INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
contexts={r['item_id']:r for r in read(p/'EVALUATOR_CONTEXT.jsonl')};props={};hashes={}
for n in [1,2]:
 f=a.submissions/f'bfcl_proposer_{n}.jsonl';rs=read(f);mp={r['blind_id']:r['item_id'] for r in read(p/f'PROPOSER_{n}_MAPPING.jsonl')}
 assert len(rs)==len(mp)==100 and {r['item_id'] for r in rs}==set(mp)
 for r in rs:
  assert set(r)=={'item_id','proposal_status','candidate_action','execution_class','work_product','prefix_support'}
  assert r['proposal_status'] in ['proposed','abstain'] and r['prefix_support'].strip()
  if r['proposal_status']=='abstain':assert all(r[k] is None for k in ['candidate_action','execution_class','work_product'])
  else:assert r['execution_class'] in [1,2,3] and r['candidate_action'].strip() and r['work_product'].strip()
  k=mp[r['item_id']];assert k not in props;props[k]={**r,'item_id':k,'proposer_blind_id':r['item_id'],'proposer':n}
 hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
 # Raw proposals copied before evaluator join.
 assert not (p/f.name).exists();shutil.copyfile(f,p/f.name)
assert set(props)==set(contexts)
(p/'PROPOSAL_FREEZE.json').write_text(json.dumps(hashes,indent=2)+'\n')
allrows=[{**r,**props[k],'candidate_origin':'prefix_only_AI_authored_policy','fixture_contract':'Artifact is local prefix-only AI-authored preparation, not an executed BFCL tool result. No unmentioned tool/state facts may be inferred. Full instruction is first public user turn only.'} for k,r in contexts.items()]
write('ALL_OPPORTUNITIES.jsonl',allrows)
proposed=[r for r in allrows if r['proposal_status']=='proposed'];write('PROPOSED_ITEMS.jsonl',proposed);write('ABSTENTIONS.jsonl',[r for r in allrows if r['proposal_status']=='abstain'])
for n,seed in [('A',81201),('B',81202)]:
 order=list(proposed);random.Random(seed).shuffle(order);rs=[];mp=[]
 for i,r in enumerate(order,1):
  bid=f'{n}{i:03d}';mp.append({'blind_id':bid,'item_id':r['item_id']});rs.append({'item_id':bid,**{k:r[k] for k in ['prefix','candidate_action','execution_class','work_product','full_instruction','fixture_contract']}})
 write(f'RATER_{n}_INPUT.jsonl',rs);write(f'RATER_{n}_MAPPING.jsonl',mp)
(p/'REVIEW_INPUT_FREEZE.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.glob('RATER_*'))},indent=2)+'\n')
print(json.dumps({'opportunities':len(allrows),'proposed':len(proposed),'abstained':len(allrows)-len(proposed)}))
