import json,hashlib
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
def jl(p):return [json.loads(x) for x in (R/p).read_text().splitlines()]
def save(name,value):
 p=O/name
 if p.exists():raise FileExistsError(p)
 p.write_text(json.dumps(value,indent=2)+'\n')
labels=jl('outputs/exploratory_preflight_v0_1/LABELS_COORDINATOR_ONLY.jsonl')
original={r['item_id']:r for r in jl('outputs/checkpoint_ai_judge_v0_1/results/MAIN_200.jsonl')}
traj=jl('outputs/exploratory_preflight_v0_1/TRAJECTORY_MAPPING.jsonl');history={(r['task_id'],r['checkpoint_words']):r['input_id'] for r in traj}
cases=[]
for r in labels:
 d=original[r['item_id']];n=d['checkpoint_words']
 cases.append({'item_id':r['item_id'],'prefix':d['prefix'],'candidate_text':d['candidate_action']+'\n'+d['work_product'],'execution_class':d['execution_class'],'input_ids':[history[(r['task_id'],i)] for i in range(n-2,n+1)]})
save('CASES.json',sorted(cases,key=lambda r:r['item_id']))
save('LABELS.json',labels)
save('PRIOR_LABELS.json',jl('outputs/checkpoint_ai_judge_v0_1/results/PRIOR_COMPARISON.jsonl'))
run='outputs/exploratory_extraction_v0_1/run_20260913T003027625834Z'
e=json.loads((R/run/'EXTRACTION_RESULT.json').read_text());save('TENSOR_MANIFEST.json',json.loads(e['artifacts']['extraction/manifest.json']))
sources=['outputs/exploratory_preflight_v0_1/LABELS_COORDINATOR_ONLY.jsonl','outputs/exploratory_preflight_v0_1/TRAJECTORY_MAPPING.jsonl','outputs/checkpoint_ai_judge_v0_1/results/MAIN_200.jsonl','outputs/checkpoint_ai_judge_v0_1/results/PRIOR_COMPARISON.jsonl',run+'/VERIFICATION.json',run+'/EXTRACTION_RESULT.json']
save('SOURCE_HASHES.json',{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in sources})
print('Prepared',len(cases),'cases; last three prefixes each;',len({i for r in cases for i in r['input_ids']}),'unique tensor inputs')
