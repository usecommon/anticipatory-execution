"""Independent stored-evidence verification; no upstream tool execution."""
import argparse,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent

def jl(p):return [json.loads(x) for x in p.read_text().splitlines()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def verify(source=None):
    freeze=json.loads((P/'PRE_REPLAY_FREEZE.json').read_text())
    for path,h in freeze.items():assert sha(P/path)==h,path
    manifest=json.loads((P/'SOURCE_MANIFEST.json').read_text())
    for name,entry in manifest['code'].items():
        assert sha(P/'vendor/bfcl_eval/eval_checker/multi_turn_eval/func_source_code'/name)==entry['sha256']
    rows=jl(P/'restoration_attempt_01/SOURCE_PROJECTION.jsonl');specs={x['item_id']:x for x in jl(P/'restoration_attempt_01/TASK_SPECS.jsonl')}
    assert len(rows)==9 and len(specs)==4
    if source is not None:
        assert sha(source)==manifest['dataset']['sha256']
        original={x['id']:x for x in jl(source)}
        for x in rows:
            r=original[x['source_id']]
            assert x['filesystem_config']==r['initial_config']['GorillaFileSystem']
            assert x['question']==r['question'] and x['reference_path']==r['path']
            assert set(x['omitted_initial_state_classes'])==set(r['initial_config'])-{'GorillaFileSystem'}
    results=jl(P/'replay_attempt_01/RESULTS.jsonl');lookup={x['item_id']:x for x in rows}
    assert {x['item_id'] for x in results}==set(lookup)
    passes=0;skips=0;counterchecks=0;equivalent=0
    for result in results:
        key=result['item_id']
        assert result['binary_usefulness'] is None
        if key not in specs:
            assert result['status']=='NOT_RUN_OUTSIDE_CURRENT_CHECKER';skips+=1;continue
        row=lookup[key];s=specs[key];roots=row['filesystem_config']['root'];root=list(roots)[0]
        assert root==s['target_root_name'] and s['include_hidden'] is True
        names=sorted(roots[root]['contents'])
        assert result['actual']=={'directory':'/'+root,'entries':list(roots[root]['contents'])}
        assert result['expected']['entries']==names and result['expected']['directory']=='/'+root
        assert result['status']=='PASS_FINAL_TASK_REPLAY' and all(result['checks'].values())
        assert all(result['counterchecks'].values()) and len(result['counterchecks'])==6
        assert result['receipt']['before_snapshot_sha256']==result['receipt']['after_snapshot_sha256']
        assert not any(x.startswith('.') for x in names)
        assert result['hidden_flag_observationally_equivalent'] is True
        passes+=1;counterchecks+=6;equivalent+=1
    assert (passes,skips,counterchecks,equivalent)==(4,5,24,4)
    summary=json.loads((P/'replay_attempt_01/SUMMARY.json').read_text())
    assert summary['final_task_replays_passed']==passes and summary['unsupported_not_run']==skips and summary['failed_records']==0
    return {'status':'PASS_STORED_EVIDENCE','frozen_inputs_verified':len(freeze),'original_full_source_checked':source is not None,
            'restored_records':9,'final_task_replays_passed':passes,'unsupported_retained':skips,'counterchecks_passed':counterchecks,
            'original_hidden_flag_equivalence_cases':equivalent,'research_usefulness_labels_created':0,
            'scope':'Source projection, stored replay and checker accounting; not semantic-ground-truth or speculative validation'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path);ap.add_argument('--report',type=Path);a=ap.parse_args()
    result=verify(a.source)
    if a.report:
        with a.report.open('x') as f:f.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
