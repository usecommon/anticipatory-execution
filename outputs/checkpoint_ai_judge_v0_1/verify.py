import ast,collections,hashlib,json
from pathlib import Path
p=Path(__file__).resolve().parent
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
for inv in ['INPUT_FREEZE.json','RAW_FREEZE.json','HASHES.json']:
 for f,h in json.loads((p/inv).read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,(inv,f)
for f,h in json.loads((p/'SOURCE_HASHES.json').read_text()).items():assert hashlib.sha256((p.parent/f).read_bytes()).hexdigest()==h
human=p.parent/'checkpoint_human_pilot_v0_1'
for f,h in json.loads((human/'REVIEW_INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((human/f).read_bytes()).hexdigest()==h
full=read(p/'results/ALL_220.jsonl');main=read(p/'results/MAIN_200.jsonl');boundary=read(p/'results/BOUNDARY_20.jsonl');assert len(full)==220 and len(main)==200 and len(boundary)==20;assert len({r['item_id'] for r in full})==220
assert {r['item_id'] for r in main}.isdisjoint({r['item_id'] for r in boundary}) and {r['item_id'] for r in full}=={r['item_id'] for r in main+boundary}
stats=json.loads((p/'results/SCORES.json').read_text());ids=[]
for d,n in stats['main']['dispositions'].items():
 rs=read(p/'results'/('MAIN_'+d.upper()+'.jsonl'));assert len(rs)==n and all(r['disposition']==d for r in rs);ids.extend(r['item_id'] for r in rs)
assert len(ids)==len(set(ids))==200
for source,ss in stats['by_source'].items():
 rs=[r for r in main if r['source']==source];assert len(rs)==ss['items']==100
 for d,n in ss['dispositions'].items():assert sum(r['disposition']==d for r in rs)==n
for r in full:
 j=r['judge']
 if j['artifact_sufficiency']!='substantive':assert j['binary_usefulness_0_or_1'] is None and j['fractional_utility_0_to_1'] is None and r['disposition'] in ['invalid_candidate','uncertain_candidate']
assert stats['G1']=='PENDING' and stats['human_submissions_received']==0 and stats['judges_per_case']==1 and stats['inter_rater_kappa'] is None
for f in p.glob('*.py'):ast.parse(f.read_text())
print('PASS frozen inputs/raw judgments,220exact cases,main/control separation,sourcecounts,nullhandling,unchangedhumanpackages,single-judge limitations,gates,syntax')
