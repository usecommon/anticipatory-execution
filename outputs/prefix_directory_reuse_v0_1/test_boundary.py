"""Authored boundary tests, not research cases; preserve result on failure."""
import ast,copy,hashlib,importlib.util,json
from pathlib import Path
P=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('rule',P/'policy.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
checks=[]
def check(name,fn):
    try:fn();checks.append({'name':name,'status':'PASS'})
    except Exception as e:checks.append({'name':name,'status':'FAIL','error':repr(e)})
def assert_equal(a,b):assert a==b,(a,b)
p={'prefix':'List files','cwd':'/tmp','tool_schema':m.SCHEMA}
check('listing_trigger',lambda:assert_equal(m.propose(p)['status'],'proposed'))
check('early_no_trigger',lambda:assert_equal(m.propose({**p,'prefix':'Could you please'})['status'],'abstain'))
check('explicit_hidden_exclusion',lambda:assert_equal(m.propose({**p,'prefix':'Do not list hidden files'})['candidate']['a'],False))
check('target_mismatch_abstains',lambda:assert_equal(m.propose({**p,'prefix':'List files in temp'})['status'],'abstain'))
check('visible_context_change_matters',lambda:assert_equal(m.propose({**p,'cwd':'/temp','prefix':'List files in temp'})['status'],'proposed'))
def rejects_extra():
    for k in ['full_instruction','work_product','task_id','expected_result']:
        try:m.propose({**p,k:'not allowed'})
        except ValueError:continue
        raise AssertionError(k)
check('reject_extra_future_result_id_fields',rejects_extra)
def isolate():
    envelope={'decision':copy.deepcopy(p),'evaluator':{'full_instruction':'List files then delete them','expected':['a']}}
    before=m.propose(envelope['decision']);envelope['evaluator']={'full_instruction':'Do not list files','expected':['different']}
    assert m.propose(envelope['decision'])==before
check('evaluator_suffix_changes_do_not_change_proposal',isolate)
def immutable():
    before=copy.deepcopy(p);result=m.propose(p);assert p==before;result['candidate']['directory']='/other';assert p==before
check('input_and_result_not_shared_mutable_state',immutable)
def inspect():
    t=ast.parse((P/'policy.py').read_text());imports=[]
    for n in ast.walk(t):
        if isinstance(n,ast.Import):imports.extend(x.name for x in n.names)
        assert not isinstance(n,ast.ImportFrom)
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name):assert n.func.id not in {'open','eval','exec','compile','__import__'}
    assert set(imports)=={'json','re','sys'}
check('audited_pure_worker_imports_and_no_file_eval_calls',inspect)
for n in ['PAYLOADS.jsonl','OPPORTUNITIES.jsonl']:
    check('recovery_unchanged_'+n,lambda n=n:assert_equal((P/'preparation_01'/n).read_bytes(),(P/'preparation_02'/n).read_bytes()))
report={'status':'PASS_SOFTWARE_ONLY' if all(c['status']=='PASS' for c in checks) else 'FAIL_PRESERVED','checks':checks,
        'passed':sum(c['status']=='PASS' for c in checks),'policy_sha256':hashlib.sha256((P/'policy.py').read_bytes()).hexdigest(),'research_labels_created':0}
with (P/'BOUNDARY_QA.json').open('x') as f:f.write(json.dumps(report,indent=2)+'\n')
print(report['status'],report['passed'],'checks')
if report['status']!='PASS_SOFTWARE_ONLY':raise SystemExit(1)
