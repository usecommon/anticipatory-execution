import argparse,collections,hashlib,json,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--submissions',type=Path,required=True);args=parser.parse_args()
out=p/'results'
if out.exists():raise SystemExit('Refusing to overwrite results')
def read(f):return [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
rows=read(p/'ALL_CANDIDATES.jsonl');by={r['item_id']:r for r in rows};assert len(by)==len(rows)==1000
for f,h in json.loads((p/'INPUT_HASHES.json').read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,f
judgments={};raws=[]
for n in [1,2,3]:
 f=args.submissions/f'curation_judge_{n}.jsonl';r=read(f);mapping={m['blind_id']:m['item_id'] for m in read(p/f'JUDGE_{n}_MAPPING.jsonl')}
 assert len(r)==len(mapping) and {x['item_id'] for x in r}==set(mapping)
 for x in r:
  assert x['binary_usefulness_0_or_1'] is None or type(x['binary_usefulness_0_or_1']) is int and x['binary_usefulness_0_or_1'] in [0,1]
  assert x['ambiguity_flag_Y_N'] in ['Y','N'] and x['rationale'].strip()
  k=mapping[x['item_id']];assert k not in judgments
  judgments[k]={**x,'blind_id':x['item_id'],'item_id':k,'judge':f'AI_{n}','human_gold':False}
 raws.append(f)
assert set(judgments)==set(by)
groups=collections.defaultdict(list)
for r in rows:groups[r['parent_item_id']].append(judgments[r['item_id']])
active=[];excluded=[];quarantine=[];audit=[]
for r in rows:
 j=judgments[r['item_id']];siblings=groups[r['parent_item_id']];labels={s['binary_usefulness_0_or_1'] for s in siblings};flags=any(s['ambiguity_flag_Y_N']=='Y' for s in siblings);item={**r,'judgment':j}
 if j['binary_usefulness_0_or_1']==0:bucket='excluded_non_reusable';reason='AI judgment 0; discarded from active set';excluded.append(item)
 elif j['binary_usefulness_0_or_1'] is None:bucket='quarantine';reason='Unresolved judgment';quarantine.append(item)
 elif labels!={1} or flags:bucket='quarantine';reason='Ambiguity or label inconsistency among semantically matched wording variants';quarantine.append(item)
 else:bucket='active_reusable';reason='All five matched variants judged reusable without ambiguity';active.append(item)
 audit.append({'item_id':r['item_id'],'parent_item_id':r['parent_item_id'],'bucket':bucket,'reason':reason,'raw_binary':j['binary_usefulness_0_or_1']})
assert len(active)+len(excluded)+len(quarantine)==1000
assert all(r['judgment']['binary_usefulness_0_or_1']==1 and r['judgment']['ambiguity_flag_Y_N']=='N' for r in active)
out.mkdir()
def write(name,rs): (out/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rs))
for name,rs in [('ACTIVE_REUSABLE.jsonl',active),('EXCLUDED_NON_REUSABLE.jsonl',excluded),('QUARANTINE.jsonl',quarantine),('DISPOSITION.jsonl',audit),('ALL_JUDGMENTS.jsonl',list(judgments.values()))]:write(name,rs)
for f in raws:shutil.copy2(f,out/f.name)
c=collections.Counter(j['binary_usefulness_0_or_1'] for j in judgments.values());stats={'candidate_items':1000,'active_reusable':len(active),'excluded_non_reusable':len(excluded),'quarantined':len(quarantine),'raw_AI_labels':{'reusable':c[1],'non_reusable':c[0],'unresolved':c[None],'ambiguous':sum(j['ambiguity_flag_Y_N']=='Y' for j in judgments.values())},'active_parent_items':len({r['parent_item_id'] for r in active}),'active_template_groups':len({r['template_group'] for r in active}),'total_template_groups':50,'judgments_per_item':1,'AI_judges':3,'inter_rater_kappa':None,'human_G1':'PENDING','positive_only_research_validity':'NOT_A_VALID_STANDALONE_NON_REVISION_EVALUATION','public_release':False,'research_model_inference':False,'confirmatory_extraction':False,'old_labels_changed':False,'raw_submission_hashes':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in raws}}
(out/'STATUS.json').write_text(json.dumps(stats,indent=2)+'\n')
lines=['# Active reusable synthetic items','','Only clear positive AI judgments retained. Related wording variants share 50 source templates; this is not independent-human gold.','']
for r in active:
 lines.extend([f"## {r['item_id']}",'',f"**Prefix:** {r['prefix']}",'',f"**Action:** {r['candidate_action']}",'','```text',r['work_product'],'```','',f"**Full instruction:** {r['full_instruction']}",'',f"**Rationale:** {r['judgment']['rationale']}",''])
(out/'ACTIVE_REVIEW.md').write_text('\n'.join(lines));print(json.dumps(stats,indent=2))
