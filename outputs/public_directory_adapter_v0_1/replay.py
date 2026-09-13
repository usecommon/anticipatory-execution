"""Bounded final-task directory replay, never speculative or model evaluation."""
import argparse,copy,hashlib,json,sys,traceback
from pathlib import Path
P=Path(__file__).resolve().parent

def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def from_source_node(name,node):
    if node['type']=='file':return {'name':name,'type':'file','content':node['content']}
    if node['type']!='directory':raise ValueError('unsupported source node')
    return {'name':name,'type':'directory','contents':{k:from_source_node(k,v) for k,v in node['contents'].items()}}

def source_expectation(row,spec):
    roots=row['filesystem_config']['root'];root_name=next(iter(roots))
    if spec['target_root_name']!=root_name:raise ValueError('target not initial source root; navigation unsupported')
    if spec['recursive'] or not spec['include_files'] or not spec['include_directories']:raise ValueError('unsupported task requirement')
    tree=from_source_node(root_name,roots[root_name])
    entries=sorted(x for x in roots[root_name]['contents'] if spec['include_hidden'] or not x.startswith('.'))
    return {'directory':'/'+root_name,'entries':entries,'snapshot':{'tree':tree,'cwd':'/'+root_name}}

def task_check(expected,actual,before,after):
    return {'correct_entry_set':actual['directory']==expected['directory'] and sorted(actual['entries'])==expected['entries'],
            'source_environment_matches':before==expected['snapshot'],
            'no_mutation':before==after}

def passed(check):return all(check.values())

def run(out):
    out.mkdir(parents=True,exist_ok=False)
    freeze=json.loads((P/'PRE_REPLAY_FREEZE.json').read_text())
    for rel,h in freeze.items():
        if hashlib.sha256((P/rel).read_bytes()).hexdigest()!=h:raise ValueError('Pre-replay input/source changed: '+rel)
    sys.path.insert(0,str(P/'vendor'))
    from bfcl_eval.eval_checker.multi_turn_eval.func_source_code.gorilla_file_system import GorillaFileSystem,Directory,File
    def snapshot(fs):
        def node(x):
            if isinstance(x,File):return {'name':x.name,'type':'file','content':x.content}
            if not isinstance(x,Directory):raise ValueError('unknown runtime node')
            return {'name':x.name,'type':'directory','contents':{k:node(v) for k,v in x.contents.items()}}
        return {'tree':node(fs.root),'cwd':fs.pwd()['current_working_directory']}
    records=[json.loads(x) for x in (P/'restoration_attempt_01/SOURCE_PROJECTION.jsonl').read_text().splitlines()]
    specs={x['item_id']:x for x in [json.loads(s) for s in (P/'restoration_attempt_01/TASK_SPECS.jsonl').read_text().splitlines()]}
    results=[]
    for row in records:
        if row['item_id'] not in specs:
            results.append({'item_id':row['item_id'],'status':'NOT_RUN_OUTSIDE_CURRENT_CHECKER','scope_assessment':row['scope_assessment'],'binary_usefulness':None})
            continue
        try:
            spec=specs[row['item_id']];expected=source_expectation(row,spec)
            assert 'ls' not in row['excluded_functions']
            fs=GorillaFileSystem();fs._load_scenario(copy.deepcopy(row['filesystem_config']),long_context=False)
            before=snapshot(fs);output=fs.ls(a=True);after=snapshot(fs)
            actual={'directory':after['cwd'],'entries':output['current_directory_content']}
            check=task_check(expected,actual,before,after)
            wrong_target={**actual,'directory':actual['directory']+'/WRONG_TARGET'}
            omitted={**actual,'entries':actual['entries'][1:]}
            fabricated={**actual,'entries':actual['entries']+['__invented_entry__']}
            changed=copy.deepcopy(after);changed['cwd']='/changed'
            controls={'wrong_target_rejected':not passed(task_check(expected,wrong_target,before,after)),
                      'omission_rejected':not passed(task_check(expected,omitted,before,after)),
                      'fabricated_entry_rejected':not passed(task_check(expected,fabricated,before,after)),
                      'mutation_rejected':not passed(task_check(expected,actual,before,changed))}
            if not actual['entries']:raise ValueError('Omission control undefined for empty directory')
            visible=fs.ls(a=False);visible_after=snapshot(fs)
            hidden=[x for x in actual['entries'] if x.startswith('.')]
            controls['visible_query_nonmutating']=visible_after==after
            controls['visible_filter_matches_source']=sorted(visible['current_directory_content'])==sorted(x for x in expected['entries'] if not x.startswith('.'))
            results.append({'item_id':row['item_id'],'status':'PASS_FINAL_TASK_REPLAY' if passed(check) and all(controls.values()) else 'FAIL_PRESERVED',
                            'decision_origin':'Evaluator-selected final-task command, not prefix-only candidate',
                            'command':{'operation':'GorillaFileSystem.ls','a':True},'source_environment_sha256':digest(row['filesystem_config']),
                            'task_spec_sha256':digest(spec),'actual':actual,'expected':expected,'checks':check,'counterchecks':controls,
                            'receipt':{'before_snapshot_sha256':digest(before),'after_snapshot_sha256':digest(after),'result_sha256':digest(output),'output':output},
                            'hidden_entries_in_original_target':hidden,'visible_only_result':visible,
                            'hidden_flag_observationally_equivalent':visible==output,
                            'binary_usefulness':None,'speculative_reuse_measured':False})
        except Exception:
            results.append({'item_id':row['item_id'],'status':'FAIL_PRESERVED','traceback':traceback.format_exc(),'binary_usefulness':None})
        (out/'PARTIAL.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in results))
    summary={'status':'PASS_SCOPED_FINAL_TASK_REPLAY' if all(x['status']!='FAIL_PRESERVED' for x in results) else 'FAIL_PRESERVED',
             'selected_records_retained':len(results),'final_task_replays_passed':sum(x['status']=='PASS_FINAL_TASK_REPLAY' for x in results),
             'unsupported_not_run':sum(x['status']=='NOT_RUN_OUTSIDE_CURRENT_CHECKER' for x in results),
             'failed_records':sum(x['status']=='FAIL_PRESERVED' for x in results),
             'speculative_reuse_labels_created':0,'prefix_generated_candidates':0,'model_forwards':0,
             'interpretation':'First-turn directory entry-set correctness with original filesystem context, not official BFCL evaluation or thesis evidence'}
    (out/'RESULTS.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in results));(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    if summary['failed_records']:raise SystemExit(1)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    try:run(a.out)
    except Exception:
        if a.out.exists():(a.out/'FAILURE.txt').write_text(traceback.format_exc())
        raise
