"""Build a synthetic development stress set; no model, tool execution or gold-key access."""
import argparse,hashlib,json,random,re
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
here=Path(__file__).resolve().parent;repo=here.parents[1];dest=args.output
if dest.exists() and any(dest.iterdir()):raise SystemExit('Refusing to overwrite nonempty output directory')
dest.mkdir(parents=True,exist_ok=True)
def read(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def write(name,r):
 (dest/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in r))
old=read(repo/'outputs/g1_team_v0_1/PROVISIONAL_LABELS.jsonl');owner=read(repo/'outputs/g1_owner_review_combined_v0_1/OWNER_BINARY_DECISIONS.jsonl');old={x['item_id']:x for x in old};owner={x['item_id']:x for x in owner}
specs=json.loads((here/'SCENARIO_SPECS.json').read_text());rows=[];tasks=[];prefixes=[];links=[];expect=[]
for n,s in enumerate(specs,1):
 anchor,prefix,keep,change,act1,out1,act2,out2=s
 assert owner[anchor]['binary_usefulness_0_or_1']==1
 family=f'SX1-F{n:03d}'
 for branch,suffix in [('K',keep),('R',change)]:
  task=f'{family}-{branch}';full=prefix+suffix
  tasks.append({'task_id':task,'family_id':family,'full_instruction':full,'domain':old[anchor]['domain'],'source_type':'AI_authored_synthetic','fixture_contract':'All named entities, prices, state and tool outputs are fictional frozen fixtures. Outputs are stipulated artifacts, not evidence of executed tools. No unmentioned capabilities or records may be inferred.'})
  for w,m in enumerate(re.finditer(r'\S+',full),1):prefixes.append({'observation_id':f'{task}-w{w:03d}','task_id':task,'prefix':full[:m.end()]})
  for j,(act,output) in enumerate([(act1,out1),(act2,out2)],1):
   item=f'{task}-A{j}';cl=3 if act.startswith(('Stage','Draft')) else 1 if act.startswith('Prepare') else 2
   row={'item_id':item,'task_id':task,'family_id':family,'domain':old[anchor]['domain'],'prefix':prefix,'candidate_action':act,'execution_class':cl,'work_product':output,'full_instruction':full,'fixture_contract':tasks[-1]['fixture_contract'],'provenance':'AI-authored expansion inspired by one accepted pilot action; no inherited label; no live lookup, model inference or tool execution.'}
   rows.append(row);links.append({'item_id':item,'accepted_style_anchor':anchor,'anchor_label_transferred':False})
   expect.append({'item_id':item,'binary_usefulness_0_or_1':0 if branch=='R' and j==1 else 1,'source':'Author construction expectation; coarse branch-based heuristic, not independent annotation or ground truth','rationale':'Expected target-specific work to fail after revision; expected retained and supporting work to survive. Must be checked against each actual artifact.'})
write('ITEMS.jsonl',rows);write('TASKS_EVALUATOR_ONLY.jsonl',tasks);write('ALL_WORD_PREFIXES.jsonl',prefixes);write('STYLE_LINEAGE.jsonl',links);write('AUTHOR_EXPECTATIONS.jsonl',expect)
write('CANDIDATE_POLICY_INPUTS.jsonl',[{'item_id':r['item_id'],'prefix':r['prefix'],'candidate_action':r['candidate_action'],'execution_class':r['execution_class']} for r in rows])
# Opaque IDs and independent ordering hide construction branches and expectations from reviewers.
for k,seed in [('A',2609121),('B',2609122)]:
 order=list(rows);random.Random(seed).shuffle(order);mapping=[];blind=[]
 for i,r in enumerate(order,1):
  oid=f'{k}{i:03d}';mapping.append({'blind_id':oid,'item_id':r['item_id']});blind.append({'item_id':oid,**{key:r[key] for key in ['prefix','candidate_action','execution_class','work_product','full_instruction','fixture_contract']}})
 write(f'RATER_{k}_INPUT.jsonl',blind);write(f'RATER_{k}_MAPPING.jsonl',mapping)
qa={'items':len(rows),'tasks':len(tasks),'families':len(specs),'all_word_observations':len(prefixes),'distinct_anchor_ids':len({x[0] for x in specs}),'old_labels_transferred':0,'all_prefixes_literal':all(r['full_instruction'].startswith(r['prefix']) for r in rows),'all_input_actions_identical_across_future_branches':all(rows[i]['prefix']==rows[i+2]['prefix'] and rows[i]['candidate_action']==rows[i+2]['candidate_action'] and rows[i]['work_product']==rows[i+2]['work_product'] for i in range(0,len(rows),4)),'source_hashes':{str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [repo/'outputs/g1_team_v0_1/PROVISIONAL_LABELS.jsonl',repo/'outputs/g1_owner_review_combined_v0_1/OWNER_BINARY_DECISIONS.jsonl']}}
(dest/'STRUCTURE_QA.json').write_text(json.dumps(qa,indent=2)+'\n');print(json.dumps(qa))
