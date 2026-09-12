import argparse,collections,hashlib,json,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--submissions',type=Path,required=True);a=ap.parse_args()
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
def write(n,rs):
 f=p/n;assert not f.exists(),f;f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
for f,h in json.loads((p/'INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
for f,h in json.loads((p/'SOURCE_HASHES.json').read_text()).items():assert hashlib.sha256((p.parent/f).read_bytes()).hexdigest()==h
props={};hashes={}
for n in [1,2]:
 f=a.submissions/f'checkpoint_proposer_{n}.jsonl';rs=read(f);ids={r['item_id'] for r in read(p/f'PROPOSER_{n}_INPUT.jsonl')};assert len(rs)==len(ids) and {r['item_id'] for r in rs}==ids
 for r in rs:
  assert set(r)=={'item_id','proposal_status','candidate_action','execution_class','work_product','prefix_support'}
  assert r['proposal_status'] in ['proposed','abstain'] and r['prefix_support'].strip()
  if r['proposal_status']=='abstain':assert all(r[k] is None for k in ['candidate_action','execution_class','work_product'])
  else:assert type(r['execution_class']) is int and r['execution_class'] in [1,2,3] and r['candidate_action'].strip() and r['work_product'].strip()
  assert r['item_id'] not in props;props[r['item_id']]=r
 assert not (p/f.name).exists();shutil.copyfile(f,p/f.name);hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
(p/'PROPOSAL_FREEZE.json').write_text(json.dumps(hashes,indent=2)+'\n')
rows=[]
for r in read(p/'SCHEDULED_OPPORTUNITIES.jsonl'):
 if r['checkpoint_status']=='eligible':r={**r,**{k:v for k,v in props[r['prefix_group']].items() if k!='item_id'}}
 else:r={**r,'proposal_status':'not_eligible','candidate_action':None,'execution_class':None,'work_product':None,'prefix_support':None}
 rows.append(r)
write('LATER_OPPORTUNITIES.jsonl',rows)
old=read(p.parent/'shared_policy_pilot_v0_1/ALL_OPPORTUNITIES.jsonl')
for r in old:
 rows.append({'item_id':f'CP1-{r["item_id"]}-W6','task_id':r['item_id'],**{k:r[k] for k in ['source','source_task_id','template_group','domain','full_instruction','checkpoint_words','prefix','prefix_group','proposal_status','candidate_action','execution_class','work_product','prefix_support']},'checkpoint_status':'eligible','proposal_version':'frozen_shared_policy_v0_1'})
assert len(rows)==900;write('ALL_CHECKPOINTS.jsonl',rows)
pool=[r for r in rows if r['proposal_status']=='proposed'];write('REVIEW_POOL.jsonl',pool)
def rank(r,salt):return hashlib.sha256((salt+'|'+r['item_id']).encode()).hexdigest()
def ordered_candidates(source):
 candidates=sorted([r for r in pool if r['source']==source],key=lambda r:rank(r,'human-main-v1'));seen=set();first=[];extra=[]
 for r in candidates:
  if r['task_id'] in seen:extra.append(r)
  else:seen.add(r['task_id']);first.append(r)
 return first+extra
sources=['public_bfcl','synthetic'];ordered={s:ordered_candidates(s) for s in sources};selected=[]
for s in sources:selected.extend(ordered[s][:100])
used={r['item_id'] for r in selected};rest=sorted([r for r in pool if r['item_id'] not in used],key=lambda r:rank(r,'human-fill-v1'));selected.extend(rest[:max(0,200-len(selected))])
write('SELECTED_MAIN.jsonl',selected)
controls=[]
for i,r in enumerate(sorted(selected,key=lambda r:rank(r,'human-boundary-v1'))[:20]):
 typ=i%4
 action=['Copy the observed instruction into a note.','Prepare an empty results table.','List unresolved fields for later filling.','Write a generic task checklist.'][typ]
 product=[r['prefix'],'| Item | Result |\n|---|---|\n| | |','{"target":null,"operation":null,"arguments":null,"result":null}','1. Identify the task.\n2. Collect missing details.\n3. Complete the task.'][typ]
 controls.append({**r,'item_id':f'BOUNDARY-{i+1:03d}','parent_review_item_id':r['item_id'],'candidate_action':action,'work_product':product,'execution_class':1,'control_type':['copied_prefix','empty_table','unknown_slots','generic_checklist'][typ],'prefix_support':'Authored boundary diagnostic, not prefix-proposer output.'})
write('BOUNDARY_CONTROLS.jsonl',controls)
counts={f'{s}:{k}':dict(collections.Counter(r['proposal_status'] if r['checkpoint_status']=='eligible' else r['checkpoint_status'] for r in rows if r['source']==s and r['checkpoint_words']==k)) for s in sources for k in [6,12,18]}
status={'scheduled_opportunities':900,'later_scheduled':600,'later_unique_prefixes':len(props),'later_unique_proposals':sum(r['proposal_status']=='proposed' for r in props.values()),'review_pool':len(pool),'main_selected':len(selected),'main_shortfall':max(0,200-len(selected)),'boundary_controls':len(controls),'source_checkpoint_counts':counts,'selection_source_counts':dict(collections.Counter(r['source'] for r in selected)),'selection_checkpoint_counts':dict(collections.Counter(r['checkpoint_words'] for r in selected)),'selection_distinct_tasks':len({r['task_id'] for r in selected}),'selection_distinct_template_groups':len({(r['source'],r['template_group']) for r in selected}),'human_submissions_received':0,'G1':'PENDING','new_reuse_labels':0,'confirmatory_extraction':False,'research_model_inference':False,'fixture_execution':False}
(p/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n');print(json.dumps(status,indent=2))
