"""Outcome-independent development manifest; labels joined only after splits."""
import hashlib,json,re
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SEED='aeb-exploratory-v0.1-20260912'
def sha(b):return hashlib.sha256(b).hexdigest()
def write(name,value):
 p=OUT/name
 if p.exists():raise FileExistsError(p)
 p.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')
def lines(name,rows):
 p=OUT/name
 if p.exists():raise FileExistsError(p)
 p.write_text(''.join(json.dumps(r,sort_keys=True)+'\n' for r in rows))
def read(rel):return [json.loads(x) for x in (ROOT/rel).read_text().splitlines()]
def main():
 src='outputs/checkpoint_human_pilot_v0_1/ALL_CHECKPOINTS.jsonl'
 labelsrc='outputs/checkpoint_ai_judge_v0_1/results/MAIN_200.jsonl'
 rows=read(src);tasks={r['task_id']:r for r in rows};parent={t:t for t in tasks}
 def find(t):
  while parent[t]!=t:parent[t]=parent[parent[t]];t=parent[t]
  return t
 def union(a,b):
  a,b=find(a),find(b)
  if a!=b:parent[max(a,b)]=min(a,b)
 keys={};edges=[]
 for r in sorted(rows,key=lambda r:r['item_id']):
  matchkeys=[('family',r['source']+':'+r['template_group']),('instruction',' '.join(r['full_instruction'].casefold().split()))]
  if r['checkpoint_status']=='eligible':matchkeys.append(('observed_prefix',' '.join(r['prefix'].casefold().split())))
  for kind,key in matchkeys:
   k=(kind,key)
   if k in keys and keys[k]!=r['task_id']:
    union(keys[k],r['task_id']);edges.append({'reason':kind,'a':keys[k],'b':r['task_id'],'key_sha256':sha(key.encode())})
   else:keys[k]=r['task_id']
 groups=defaultdict(list)
 for t in sorted(tasks):groups[find(t)].append(t)
 assignments={};components=[]
 for members in sorted(groups.values()):
  group=sha('\n'.join(members).encode());bucket=int(sha((SEED+group).encode()),16)%100
  split='exploratory_fit' if bucket<70 else ('exploratory_tune' if bucket<85 else 'exploratory_check')
  components.append({'group_id':group,'tasks':members,'split':split})
  for t in members:assignments[t]={'group_id':group,'split':split}
 # Freeze grouping before any label read. Never search for a split with desirable labels.
 lines('COMPONENTS.jsonl',components);lines('GROUP_EDGES.jsonl',edges)
 inputs={};coordinator=[];opps=[]
 for t,r in sorted(tasks.items()):
  eligible=[x for x in rows if x['task_id']==t and x['checkpoint_status']=='eligible']
  maxwords=max(x['checkpoint_words'] for x in eligible)
  spans=list(re.finditer(r'\S+',r['full_instruction']))
  for n in range(1,maxwords+1):
   prefix=r['full_instruction'][:spans[n-1].end()];pid='X'+sha(prefix.encode())
   inputs[pid]={'id':pid,'prefix':prefix}
   coordinator.append({'task_id':t,'checkpoint_words':n,'input_id':pid,**assignments[t]})
 for r in sorted(rows,key=lambda r:r['item_id']):
  entry={k:r[k] for k in ['item_id','task_id','source','template_group','checkpoint_words','checkpoint_status','proposal_status']}
  entry.update(assignments[r['task_id']])
  if r['checkpoint_status']=='eligible':
   entry['input_id']='X'+sha(r['prefix'].encode())
   assert entry['input_id'] in inputs
  opps.append(entry)
 # Exact duplicate extraction text cannot cross splits, including dense history.
 byinput=defaultdict(set)
 for r in coordinator:byinput[r['input_id']].add(r['split'])
 # Earlier short prefixes inevitably overlap. They are label-free states; report
 # overlaps explicitly. Scheduled prediction checkpoints must be group-separated.
 checkpoint_splits=defaultdict(set)
 for r in opps:
  if 'input_id' in r:checkpoint_splits[r['input_id']].add(r['split'])
 assert all(len(v)==1 for v in checkpoint_splits.values())
 lines('EXTRACTION_INPUT.jsonl',[inputs[k] for k in sorted(inputs)])
 lines('TRAJECTORY_MAPPING.jsonl',coordinator);lines('OPPORTUNITIES.jsonl',opps)
 labels=read(labelsrc);opmap={r['item_id']:r for r in opps};joined=[]
 for r in labels:
  o=opmap[r['item_id']];assert o['proposal_status']=='proposed'
  joined.append({'item_id':r['item_id'],'task_id':r['task_id'],'source':r['source'],'input_id':o['input_id'],**assignments[r['task_id']], 'binary_usefulness':r['judge']['binary_usefulness_0_or_1'],'fractional_utility':r['judge']['fractional_utility_0_to_1'],'ambiguity':r['judge']['ambiguity_flag_Y_N'],'disposition':r['disposition'],'label_source':'single_AI_judge_not_human_gold'})
 lines('LABELS_COORDINATOR_ONLY.jsonl',joined)
 counts={s:dict(Counter(r['disposition'] for r in joined if r['split']==s)) for s in sorted(set(assignments[t]['split'] for t in tasks))}
 write('PLAN.json',{'seed':SEED,'label_use':'joined after fixed split; no label balancing or rerolls','split_rule':'SHA256(seed + component hash) modulo100: fit<70,tune<85,check otherwise','grouping':['source-qualified template','normalized identical full instruction','normalized identical eligible checkpoint prefix'],'scope':'private AI-labeled exploratory diagnostic only; not confirmatory; source/adaptation release eligibility pending','tokenization':'exact observed prefix, add_special_tokens=True, no chat template; dense word history through last eligible 6/12/18 checkpoint','inputs':'EXTRACTION_INPUT.jsonl only; no suffix, label, source, split or candidate artifact in tokenizer payload','resource_limit':{'gpu':0,'cpu':1,'memory_mib':2048,'timeout_seconds':300,'retries':0,'max_containers':1},'human_G1':'PENDING_DEFERRED','confirmatory_extraction':False})
 write('MANIFEST.json',{'tasks':len(tasks),'components':len(components),'largest_component_tasks':max(len(x['tasks']) for x in components),'scheduled_opportunities':len(rows),'eligible_opportunities':sum(r['checkpoint_status']=='eligible' for r in rows),'unique_dense_prefixes':len(inputs),'task_word_prefixes':len(coordinator),'shared_early_history_inputs_across_splits':sum(len(v)>1 for v in byinput.values()),'scheduled_checkpoint_overlap_across_splits':0,'split_task_counts':dict(Counter(x['split'] for x in assignments.values())),'split_label_counts':counts,'main_judgments':len(labels),'unjudged_proposed':sum(r['proposal_status']=='proposed' for r in rows)-len(labels),'boundary_controls':'20 retained in original judge bundle; not prediction targets','limitations':['Group mapping catches declared templates/exact normalized duplicates, not all semantic near-duplicates.','Shared early histories are label-free prefix states; report overlap and never fit transformations on tune/check labels.','All cases have prior development exposure; exploratory_check is not untouched confirmatory data.','Single AI labels, few negatives and selected proposal pool do not establish false-speculation risk or causal public/synthetic effects.']})
 sources=[src,labelsrc,'outputs/g0_closure_v0_5/checkpoint_identity.json','outputs/g0_closure_v0_5/closure_c_20260911T180932Z/contract.json']
 write('SOURCE_HASHES.json',{p:sha((ROOT/p).read_bytes()) for p in sources})
 write('INPUT_FREEZE.json',{p.name:sha(p.read_bytes()) for p in sorted(OUT.iterdir()) if p.suffix in ['.json','.jsonl','.py']})
if __name__=='__main__':main()
