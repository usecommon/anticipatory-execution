"""Offline artifact integrity and causal input-boundary checks; no inference."""
import ast,collections,hashlib,json,re
from pathlib import Path
p=Path(__file__).resolve().parent
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
for inventory in ['INPUT_FREEZE.json','PROPOSAL_FREEZE.json','REVIEW_INPUT_FREEZE.json','RATINGS_FREEZE.json','JUDGE_INPUT_FREEZE.json','HASHES.json']:
 for f,h in json.loads((p/inventory).read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,(inventory,f)
ctx=read(p/'EVALUATOR_CONTEXT.jsonl');by={r['item_id']:r for r in ctx};assert len(by)==len(ctx)==200
expected=[]
for r in ctx:
 words=list(re.finditer(r'\S+',r['full_instruction']));assert r['prefix']==r['full_instruction'][:words[5].end()] and len(words)>6
 expected.extend({'item_id':r['item_id'],'word_index':i,'prefix':r['full_instruction'][:m.end()]} for i,m in enumerate(words,1))
assert expected==read(p/'ALL_WORD_PREFIXES.jsonl')
seen=[]
for n in [1,2]:
 mp={r['blind_id']:r['item_id'] for r in read(p/f'PROPOSER_{n}_MAPPING.jsonl')};rs=read(p/f'PROPOSER_{n}_INPUT.jsonl');assert len(rs)==100 and {r['item_id'] for r in rs}==set(mp)
 for r in rs:assert set(r)=={'item_id','prefix'} and r['prefix']==by[mp[r['item_id']]]['prefix'];seen.append(mp[r['item_id']])
assert len(seen)==len(set(seen))==200 and set(seen)==set(by)
full=read(p/'results/ALL_ITEMS.jsonl');assert len(full)==200 and {r['item_id'] for r in full}==set(by)
parts=[read(p/'results'/f) for f in ['REUSABLE.jsonl','NON_REUSABLE.jsonl','UNRESOLVED.jsonl','ABSTENTIONS.jsonl']];ids=[r['item_id'] for part in parts for r in part];assert len(ids)==len(set(ids))==200 and set(ids)==set(by)
for r in full:
 if r['proposal_status']=='abstain':assert all(r[k] is None for k in ['candidate_action','work_product','execution_class','rater_A','rater_B','adjudication'])
 else:assert r['adjudication'] is not None
for f in p.glob('*.py'):ast.parse(f.read_text())
print('PASS: frozen hashes; 200 exact opportunities; all literal prefixes; prefix-only proposer boundary; four exhaustive disjoint dispositions; abstentions unlabeled; syntax.')
