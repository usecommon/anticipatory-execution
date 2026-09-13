"""Independent stored outcome/provenance audit; does not call the reuse implementation."""
import hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
for filename in ['CASE_FREEZE.json','RUN_FREEZE.json']:
    for n,h in json.loads((P/filename).read_text()).items():assert hashlib.sha256((P/n).read_bytes()).hexdigest()==h,n
cases=json.loads((P/'CASES.json').read_text());results=[json.loads(x) for x in (P/'attempt_01/RESULTS.jsonl').read_text().splitlines()]
assert len(cases)==len(results)==14 and [c['id'] for c in cases]==[r['id'] for r in results]
for c,r in zip(cases,results):
    assert c['origin']==r['origin']=='authored_software_fixture'
    assert all(r[k]==v for k,v in c['expected_mechanics'].items())
    assert r['binary_usefulness'] is None and r['fractional_utility'] is None
    target=c['task']['directory'];state=c['final'].get(target)
    if state is None:assert r['final_task_correct'] is None and r['offline_witness'] is None
    else:
        required=sorted(n for n in state['entries'] if c['task']['include_hidden'] or not n.startswith('.'))
        assert r['oracle_expected_entries']==required and r['final_task_correct']==(r['actual_entries']==required)
    assert r['contributing_units']<=r['read_units']
lookup={r['id']:r for r in results}
assert lookup['provider_breaks_revision_contract']['reused'] and not lookup['provider_breaks_revision_contract']['final_task_correct']
assert lookup['useful_receipt_deliberately_ignored']['offline_witness'] and lookup['useful_receipt_deliberately_ignored']['read_units']==0
assert lookup['irrelevant_receipt_read_not_contributed']['read_units']>0 and lookup['irrelevant_receipt_read_not_contributed']['contributing_units']==0
assert lookup['missing_revision_metadata']['offline_witness'] and not lookup['missing_revision_metadata']['reused']
counts={str(v):sum(r['final_task_correct'] is v for r in results) for v in [True,False,None]}
assert counts=={'True':12,'False':1,'None':1}
report={'status':'PASS_STORED_EVIDENCE','case_and_run_freezes_verified':True,'authored_cases_verified':14,
        'final_task_outcomes':counts,'broken_provider_failure_retained':True,'research_labels_created':0,
        'interpretation':'Mechanical expectations and task outcomes distinguished; no risk-rate or rubric-validity inference'}
with (P/'VERIFICATION.json').open('x') as f:f.write(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
