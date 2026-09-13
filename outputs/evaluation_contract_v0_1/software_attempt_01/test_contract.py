"""Preserves every check result, including failures; software fixtures only."""
import argparse,copy,hashlib,json,traceback
from pathlib import Path
from contract import digest,predictor_payload,validate_evidence,check_directory_task

P=Path(__file__).resolve().parent

def fixture():
    d={'schema':'aeb-decision-1','stage':'before_execution','event':2,'prefix':'List files',
       'context':{'system':'Read-only fixture','tool_schema':'enumerate_directory(directory, include_hidden)',
                  'environment_metadata':{'cwd':'A'},'provenance_ref':'authored-fixture-context'},
       'candidate':{'operation':'enumerate_directory','directory':'A','include_hidden':True,'proposal_event':1}}
    env=digest({'A':['.hidden','a','b']})
    receipt={'request_sha256':digest(d['candidate']),'environment_sha256':env,'execution_event':3,
             'result':['.hidden','a','b'],'result_sha256':digest(['.hidden','a','b'])}
    return {'schema':'aeb-evidence-1','decision':d,
            'source':{'artifact_sha256':digest('authored'),'task_id':'fixture','transformation_ref':'none-authored', 'origin':'synthetic_fixture'},
            'environment':{'decision_sha256':env,'final_sha256':env,'provenance_ref':'authored-static'},
            'receipt':receipt,'trace':{'receipt_sha256':digest(receipt),'read_units':['a','b'],'contributing_units':['a','b']},
            'task_check':{'checker_sha256':digest('fixture-checker'),'spec_sha256':digest({'directory':'A','include_hidden':False}),
                          'final_environment_sha256':env,'correct':True}}


def main(out):
    out.mkdir(parents=True,exist_ok=False);checks=[]
    def run(name,fn):
        try:fn();checks.append({'name':name,'status':'PASS'})
        except Exception:checks.append({'name':name,'status':'FAIL','traceback':traceback.format_exc()})
    def accepts(e):
        result=validate_evidence(e)
        assert result=={'status':'STRUCTURE_VALIDATED_ONLY','public_admission':False,'binary_usefulness':None}
    def rejects(mut):
        e=fixture();mut(e)
        try:validate_evidence(e)
        except ValueError:return
        raise AssertionError('invalid evidence accepted')
    run('valid_envelope_is_not_research_admission',lambda:accepts(fixture()))
    for field in ['decision','source','environment','receipt','trace','task_check']:
        run('reject_empty_'+field,lambda f=field:rejects(lambda e:e.__setitem__(f,{})))
    run('reject_pre_action_work_product',lambda:rejects(lambda e:e['decision'].__setitem__('work_product','future result')))
    run('reject_same_event_execution',lambda:rejects(lambda e:e['receipt'].__setitem__('execution_event',2)))
    run('reject_candidate_digest_mismatch',lambda:rejects(lambda e:e['decision']['candidate'].__setitem__('directory','B')))
    run('reject_environment_mismatch',lambda:rejects(lambda e:e['receipt'].__setitem__('environment_sha256',digest('other'))))
    run('reject_corrupt_result',lambda:rejects(lambda e:e['receipt']['result'].append('wrong')))
    run('reject_unlinked_trace',lambda:rejects(lambda e:e['trace'].__setitem__('receipt_sha256',digest('other'))))
    run('reject_unread_contribution',lambda:rejects(lambda e:e['trace'].__setitem__('read_units',[])))
    run('reject_nonboolean_correctness',lambda:rejects(lambda e:e['task_check'].__setitem__('correct',1)))
    def isolation():
        e=fixture();before=predictor_payload(e['decision']);e['task_check']['spec_sha256']=digest('different future instruction');e['receipt']['result']=['other']
        assert predictor_payload(e['decision'])==before
        e['decision']['context']['environment_metadata']['cwd']='B'
        assert predictor_payload(e['decision'])!=before
    run('evaluator_change_isolated_observable_context_change_visible',isolation)
    def trace_only(read,contribution):
        e=fixture();e['trace']['read_units']=read;e['trace']['contributing_units']=contribution;accepts(e)
    run('useful_ignored_does_not_create_negative_label',lambda:trace_only([],[]))
    run('read_unnecessary_is_distinct_from_contribution',lambda:trace_only(['.hidden'],[]))
    run('partial_narrowing_does_not_create_binary_label',lambda:trace_only(['a','b'],['a','b']))
    env={'A':['a','.hidden'],'B':['a','.hidden']};spec={'directory':'A','include_hidden':True}
    def task(actual,correct):
        result=check_directory_task(spec,env,actual)
        assert result['final_task_correct'] is correct and result['binary_usefulness'] is None
    run('independent_target_correct',lambda:task({'directory':'A','entries':['.hidden','a']},True))
    run('wrong_entity_identical_output_rejected',lambda:task({'directory':'B','entries':['a','.hidden']},False))
    run('omitted_hidden_constraint_rejected',lambda:task({'directory':'A','entries':['a']},False))
    run('plausible_wrong_fresh_output_rejected',lambda:task({'directory':'A','entries':['a','.wrong']},False))
    run('duplicate_output_rejected',lambda:task({'directory':'A','entries':['a','a','.hidden']},False))
    def screen_replay():
        from screen import build
        a,sa=build();b,sb=build();assert a==b and sa==sb and len(a)==200
        groups={}
        for row in a:groups.setdefault(row['group_sha256'],set()).add(row['selected_for_semantic_review'])
        assert all(len(v)==1 for v in groups.values())
        assert all(x['binary_usefulness'] is None for x in a)
    run('screen_replay_full_denominator_and_duplicate_grouping',screen_replay)
    report={'status':'PASS_SOFTWARE_ONLY' if all(c['status']=='PASS' for c in checks) else 'FAIL_PRESERVED',
            'checks':checks,'passed':sum(c['status']=='PASS' for c in checks),'failed':sum(c['status']=='FAIL' for c in checks),
            'research_cases_validated':0,'research_labels_created':0,'semantic_rubric_validated':False,
            'limitations':['Envelope checks declared structure, not actual source truth or execution',
                          'Supplied task spec is trusted; no BFCL language-to-task-spec mapper implemented',
                          'Draft/parameter materiality remains an explicit review question'],
            'source_sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['contract.py','test_contract.py','screen.py']}}
    (out/'QA.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','passed','failed','research_cases_validated']},indent=2))
    if report['failed']:raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args();main(args.out)
