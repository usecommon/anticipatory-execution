"""Offline structural and outcome-integrity checks, no model/task execution."""
import ast,collections,copy,hashlib,json,re
from common import P as p,read,validate,disposition
for inv in ['INPUT_FREEZE.json','PROPOSAL_FREEZE.json','REVIEW_FREEZE.json','RATINGS_FREEZE.json','JUDGE_FREEZE.json','HASHES.json']:
 for f,h in json.loads((p/inv).read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,(inv,f)
for f,h in json.loads((p/'SOURCE_HASHES.json').read_text()).items():assert hashlib.sha256((p.parent/f).read_bytes()).hexdigest()==h
contexts=read(p/'EVALUATOR_CONTEXT.jsonl');assert len(contexts)==len({r['item_id'] for r in contexts})==300
prefixes={};seen=[]
for n in [1,2]:
 for r in read(p/f'PROPOSER_{n}_INPUT.jsonl'):assert set(r)=={'item_id','prefix'};assert r['item_id'] not in prefixes;prefixes[r['item_id']]=r['prefix']
assert len(prefixes)==258
for r in contexts:
 w=list(re.finditer(r'\S+',r['full_instruction']));assert len(w)>6 and r['prefix']==r['full_instruction'][:w[5].end()];assert prefixes[r['prefix_group']]==r['prefix']
rows=read(p/'results/ALL_ITEMS.jsonl');assert len(rows)==300 and {r['item_id'] for r in rows}=={r['item_id'] for r in contexts}
groups=collections.defaultdict(set)
for r in rows:
 groups[r['prefix_group']].add(tuple(r[k] for k in ['proposal_status','candidate_action','work_product','execution_class','prefix_support']))
 j=r['adjudication'];assert r['disposition']==disposition(j)
 if j:validate(j)
 else:assert r['proposal_status']=='abstain' and all(r[k] is None for k in ['work_product','candidate_action','execution_class','rater_A','rater_B'])
assert len(groups)==258 and all(len(v)==1 for v in groups.values())
parts=['REUSABLE','NON_REUSABLE','UNRESOLVED_REUSE','INVALID_CANDIDATE','UNCERTAIN_CANDIDATE','ABSTENTION'];ids=[]
for part in parts:
 rs=read(p/'results'/f'{part}.jsonl');assert all(r['disposition']==part.lower() for r in rs);ids.extend(r['item_id'] for r in rs)
assert len(ids)==len(set(ids))==300
scores=json.loads((p/'results/SCORES.json').read_text())
for source,ss in scores['by_source'].items():
 rs=[r for r in rows if r['source']==source];assert ss['opportunities']==len(rs);assert ss['proposed']==sum(r['proposal_status']=='proposed' for r in rs)
 for state,count in ss['dispositions'].items():assert count==sum(r['disposition']==state for r in rs)
# Meaningful negative tests: prevent validity exclusions being recoded as binary outcomes.
base={'artifact_sufficiency':'no_material_work','sufficiency_rationale':'No work unit','binary_usefulness_0_or_1':None,'fractional_utility_0_to_1':None,'confidence_1_to_5':4,'ambiguity_flag_Y_N':'N','annotator_rationale':'Copied inputs only'};validate(base)
for changes in [{'binary_usefulness_0_or_1':0},{'binary_usefulness_0_or_1':1},{'artifact_sufficiency':'uncertain'},{'artifact_sufficiency':'substantive'},{'fractional_utility_0_to_1':float('nan')}]:
 bad={**base,**changes}
 try:validate(bad)
 except AssertionError:pass
 else:raise AssertionError('Invalid label accepted: '+str(changes))
for f in p.glob('*.py'):ast.parse(f.read_text())
print('PASS: all freezes/source hashes; 300 literal prefixes; 258 identical-prefix proposal groups; six disjoint exhaustive dispositions; source counts; invalid-label rejection; source syntax.')
