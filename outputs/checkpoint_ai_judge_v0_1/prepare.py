import hashlib,json,random,shutil
from pathlib import Path
p=Path(__file__).resolve().parent;s=p.parent/'checkpoint_human_pilot_v0_1';read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
for f,h in json.loads((s/'REVIEW_INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((s/f).read_bytes()).hexdigest()==h
main=read(s/'SELECTED_MAIN.jsonl');boundary=read(s/'BOUNDARY_CONTROLS.jsonl');rows=[{**r,'review_kind':'main'} for r in main]+[{**r,'review_kind':'boundary'} for r in boundary];assert len(rows)==220
random.Random(260913220).shuffle(rows);inputs=[];mapping=[]
for i,r in enumerate(rows,1):
 bid=f'J{i:03d}';inputs.append({'item_id':bid,**{k:r[k] for k in ['prefix','candidate_action','work_product','execution_class','full_instruction']},'fixture_contract':'Local authored preparation. No displayed command or tool output has been executed or verified. Do not infer unmentioned environment facts.'});mapping.append({'blind_id':bid,'coordinator_item_id':r['item_id'],'review_kind':r['review_kind'],'source':r['source'],'checkpoint_words':r['checkpoint_words'],'task_id':r['task_id'],'template_group':r['template_group']})
for name,rs in [('JUDGE_INPUT.jsonl',inputs),('JUDGE_MAPPING.jsonl',mapping)]:
 f=p/name;assert not f.exists();f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
shutil.copyfile(s/'ORIGINAL_RUBRIC.txt',p/'ORIGINAL_RUBRIC.txt')
f=p.parent/'shared_policy_pilot_v0_1/REVIEWER_INSTRUCTIONS.txt';(p/'JUDGE_INSTRUCTIONS.txt').write_text(f.read_text().replace('assigned RATER input','assigned JUDGE input')+'\nThis is one fresh AI judge, not an adjudication of supplied ratings. Provide decision_reason in addition to required fields. Do not infer hidden task state, run artifacts, or inspect any previous judgments.\n')
(p/'SOURCE_HASHES.json').write_text(json.dumps({str((s/f).relative_to(p.parent)):hashlib.sha256((s/f).read_bytes()).hexdigest() for f in ['SELECTED_MAIN.jsonl','BOUNDARY_CONTROLS.jsonl','REVIEW_INPUT_FREEZE.json','PACKAGE_MANIFEST.json']},indent=2)+'\n')
