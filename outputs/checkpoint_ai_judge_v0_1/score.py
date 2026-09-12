import argparse,collections,hashlib,json,math,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
ap=argparse.ArgumentParser();ap.add_argument('--submission',type=Path,required=True);a=ap.parse_args()
for f,h in json.loads((p/'INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
for f,h in json.loads((p/'SOURCE_HASHES.json').read_text()).items():assert hashlib.sha256((p.parent/f).read_bytes()).hexdigest()==h
raw=p/'JUDGE_RAW.jsonl';assert not raw.exists();shutil.copyfile(a.submission,raw)
(p/'RAW_FREEZE.json').write_text(json.dumps({'JUDGE_RAW.jsonl':hashlib.sha256(raw.read_bytes()).hexdigest()},indent=2)+'\n')
rs=read(raw);inputs={r['item_id']:r for r in read(p/'JUDGE_INPUT.jsonl')};maps={r['blind_id']:r for r in read(p/'JUDGE_MAPPING.jsonl')};assert len(rs)==220 and {r['item_id'] for r in rs}==set(inputs)==set(maps)
fields={'item_id','artifact_sufficiency','sufficiency_rationale','binary_usefulness_0_or_1','fractional_utility_0_to_1','confidence_1_to_5','ambiguity_flag_Y_N','annotator_rationale','decision_reason'}
for r in rs:
 assert set(r)==fields
 s=r['artifact_sufficiency'];b=r['binary_usefulness_0_or_1'];f=r['fractional_utility_0_to_1'];c=r['confidence_1_to_5'];flag=r['ambiguity_flag_Y_N']
 assert s in ['substantive','no_material_work','uncertain'] and flag in ['Y','N']
 assert b is None or type(b) is int and b in [0,1]
 assert f is None or type(f) in [int,float] and 0<=f<=1 and math.isfinite(f)
 assert type(c) is int and 1<=c<=5
 assert all(isinstance(r[k],str) and r[k].strip() for k in ['sufficiency_rationale','annotator_rationale','decision_reason'])
 if s!='substantive':assert b is None and f is None
 if s=='uncertain' or s=='substantive' and b is None:assert flag=='Y'
def disposition(r):
 if r['artifact_sufficiency']=='no_material_work':return 'invalid_candidate'
 if r['artifact_sufficiency']=='uncertain':return 'uncertain_candidate'
 return {1:'reusable',0:'non_reusable',None:'unresolved_reuse'}[r['binary_usefulness_0_or_1']]
full=[]
for r in rs:
 k=r['item_id'];full.append({**inputs[k],**maps[k],'item_id':maps[k]['coordinator_item_id'],'judge':r,'disposition':disposition(r),'label_status':'single_AI_judge_not_human_gold'})
def summarize(rows):
 c=collections.Counter(r['disposition'] for r in rows);n=len(rows);return {'items':n,'dispositions':{k:c[k] for k in ['reusable','non_reusable','unresolved_reuse','invalid_candidate','uncertain_candidate']},'ambiguity_flags':sum(r['judge']['ambiguity_flag_Y_N']=='Y' for r in rows),'reusable_per_selected_item':c['reusable']/n if n else None}
main=[r for r in full if r['review_kind']=='main'];boundary=[r for r in full if r['review_kind']=='boundary'];assert len(main)==200 and len(boundary)==20
# Only now inspect previous ratings: the new raw output is already preserved/frozen.
oldfile=p.parent/'shared_policy_pilot_v0_1/results/ALL_ITEMS.jsonl';old={r['item_id']:r for r in read(oldfile)};overlap=[]
for r in main:
 if r['checkpoint_words']!=6:continue
 o=old[r['task_id']]
 for k in ['prefix','candidate_action','work_product','execution_class','full_instruction']:assert r[k]==o[k]
 before=o['adjudication'];assert before is not None;overlap.append({'item_id':r['item_id'],'prior_item_id':o['item_id'],'prior_disposition':o['disposition'],'new_disposition':r['disposition'],'changed_disposition':o['disposition']!=r['disposition'],'prior_judgment':before,'new_judgment':r['judge']})
by_source={s:summarize([r for r in main if r['source']==s]) for s in ['public_bfcl','synthetic']}
stats={'main':summarize(main),'by_source':by_source,'by_source_checkpoint':{f'{s}:{k}':summarize([r for r in main if r['source']==s and r['checkpoint_words']==k]) for s in ['public_bfcl','synthetic'] for k in [6,12,18]},'boundary':summarize(boundary),'prior_six_word_comparison':{'exact_artifact_overlaps':len(overlap),'changed_dispositions':sum(r['changed_disposition'] for r in overlap),'transitions':dict(collections.Counter(r['prior_disposition']+' -> '+r['new_disposition'] for r in overlap)),'prior_source_sha256':hashlib.sha256(oldfile.read_bytes()).hexdigest(),'interpretation':'One new judge versus earlier AI adjudication, not independent truth, efficacy or neutral rescoring.'},'judges_per_case':1,'inter_rater_kappa':None,'human_submissions_received':0,'G1':'PENDING','human_packages_modified':False,'source_effect_established':False,'confirmatory_extraction':False,'research_model_inference':False,'fixture_execution':False,'unselected_pool_items_not_evaluated':60}
out=p/'results';assert not out.exists();out.mkdir()
def write(n,rows):(out/n).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
write('ALL_220.jsonl',full);write('MAIN_200.jsonl',main);write('BOUNDARY_20.jsonl',boundary);write('PRIOR_COMPARISON.jsonl',overlap)
for s in ['reusable','non_reusable','unresolved_reuse','invalid_candidate','uncertain_candidate']:write('MAIN_'+s.upper()+'.jsonl',[r for r in main if r['disposition']==s])
write('REVIEW_ATTENTION.jsonl',[r for r in full if r['disposition']!='reusable' or r['judge']['ambiguity_flag_Y_N']=='Y'])
(out/'SCORES.json').write_text(json.dumps(stats,indent=2)+'\n')
lines=['# AI judge review of 220 frozen cases','','Keep away from independent human annotators. One AI rating per case; main and boundary cases separated below.','']
for group,label in [(main,'Main review cases'),(boundary,'Boundary diagnostics')]:
 lines.extend([f'# {label}',''])
 for r in group:
  j=r['judge'];lines.extend([f"## {r['item_id']}",'',f"**Source:** {r['source']} · **Words:** {r['checkpoint_words']} · **Disposition:** {r['disposition']}",'',f"**Prefix:** {r['prefix']}",'',f"**Action:** {r['candidate_action']}",'','```text',r['work_product'],'```','',f"**Full instruction:** {r['full_instruction']}",'',f"**Sufficiency:** {j['artifact_sufficiency']} — {j['sufficiency_rationale']}",'',f"**Ambiguity:** {j['ambiguity_flag_Y_N']}",'',j['annotator_rationale'],'',j['decision_reason'],''])
(out/'REVIEW.md').write_text('\n'.join(lines));print(json.dumps(stats,indent=2))
