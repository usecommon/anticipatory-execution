import argparse,hashlib,json,traceback
from pathlib import Path
from measure import run_case,guard
P=Path(__file__).resolve().parent

def run(out):
    out.mkdir(parents=True,exist_ok=False)
    for name,h in json.loads((P/'RUN_FREEZE.json').read_text()).items():
        assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h,name
    cases=json.loads((P/'CASES.json').read_text());results=[]
    for c in cases:
        try:
            r=run_case(c);matches={k:r[k]==v for k,v in c['expected_mechanics'].items()}
            r.update(expected_mechanics=c['expected_mechanics'],expectation_checks=matches,
                     challenge_check='PASS_EXPECTED_MECHANICS' if all(matches.values()) else 'FAIL_PRESERVED')
        except Exception:r={'id':c['id'],'challenge_check':'FAIL_PRESERVED','traceback':traceback.format_exc()}
        results.append(r)
        (out/'PARTIAL.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in results))
    # Explicit metadata boundary check, separate from fixture task outcomes.
    q=results[0]['presented_receipt'];task=cases[0]['task'];metadata=results[0]['metadata_view'];boundary=False
    try:guard(q,task,{**metadata,'final_entries':['leaked']})
    except ValueError:boundary=True
    summary={'status':'PASS_CHALLENGE_CHECKS' if boundary and all(r['challenge_check']=='PASS_EXPECTED_MECHANICS' for r in results) else 'FAIL_PRESERVED',
             'authored_cases':len(results),'expected_mechanics_passed':sum(r['challenge_check']=='PASS_EXPECTED_MECHANICS' for r in results),
             'correct_final_tasks':sum(r.get('final_task_correct') is True for r in results),
             'incorrect_final_tasks_preserved':sum(r.get('final_task_correct') is False for r in results),
             'unresolved_final_tasks':sum(r.get('final_task_correct') is None for r in results),
             'metadata_extra_field_rejected':boundary,'research_labels_created':0,'public_records_changed':0,
             'interpretation':'Expected-failure detection is a challenge-check pass, NOT a successful final task or empirical speculation-risk result'}
    (out/'RESULTS.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in results));(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
    if summary['status']!='PASS_CHALLENGE_CHECKS':raise SystemExit(1)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    try:run(a.out)
    except Exception:
        if a.out.exists():(a.out/'FAILURE.txt').write_text(traceback.format_exc())
        raise
