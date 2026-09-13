"""Prefix projection, separate pure worker, static-environment reuse witness audit."""
import argparse,copy,hashlib,importlib.util,json,re,subprocess,sys,traceback
from pathlib import Path
P=Path(__file__).resolve().parent;OLD=P.parent/'public_directory_adapter_v0_1'
SCHEMA='ls(a: bool = false) -> current_directory_content; operates only on cwd'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def jl(p):return [json.loads(x) for x in p.read_text().splitlines()]
def save(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
def load_tool():
    sys.path.insert(0,str(OLD/'vendor'))
    from bfcl_eval.eval_checker.multi_turn_eval.func_source_code.gorilla_file_system import GorillaFileSystem,Directory,File
    return GorillaFileSystem,Directory,File

def prepare(out):
    out=out.resolve()
    out.mkdir(parents=True,exist_ok=False)
    for name,h in json.loads((P/'POLICY_FREEZE.json').read_text()).items():assert sha(P/name)==h
    old_freeze=json.loads((OLD/'PRE_REPLAY_FREEZE.json').read_text())
    for rel,h in old_freeze.items():assert sha(OLD/rel)==h,rel
    G,_,_=load_tool();rows=jl(OLD/'restoration_attempt_01/SOURCE_PROJECTION.jsonl');opps=[];payloads=[]
    for r in rows:
        fs=G();fs._load_scenario(copy.deepcopy(r['filesystem_config']),long_context=False);cwd=fs.pwd()['current_working_directory']
        full=r['question'][0][0]['content'];words=list(re.finditer(r'\S+',full))
        for k in [6,12,18]:
            state='eligible' if len(words)>k else 'complete' if len(words)==k else 'not_reached'
            prefix=full[:words[k-1].end()] if len(words)>=k else None
            index=None
            if state=='eligible':
                index=len(payloads);payloads.append({'prefix':prefix,'cwd':cwd,'tool_schema':SCHEMA})
            opps.append({'opportunity_id':r['item_id']+'-W'+str(k),'item_id':r['item_id'],'instruction_group':r['instruction_group'],
                         'checkpoint_words':k,'status':state,'payload_index':index})
    assert len(opps)==27
    for n,rs in [('OPPORTUNITIES.jsonl',opps),('PAYLOADS.jsonl',payloads)]:
        (out/n).write_text(''.join(json.dumps(x)+'\n' for x in rs))
    sourcefiles=[OLD/'restoration_attempt_01/SOURCE_PROJECTION.jsonl',OLD/'restoration_attempt_01/TASK_SPECS.jsonl',P/'policy.py',P/'PLAN.md',P/'run.py']
    sourcefiles += [OLD/rel for rel in old_freeze]
    frozen={str(f.relative_to(P.parent)):sha(f) for f in sourcefiles}
    frozen.update({str((out/n).relative_to(P.parent)):sha(out/n) for n in ['OPPORTUNITIES.jsonl','PAYLOADS.jsonl']})
    save(out/'FREEZE.json',frozen)
    save(out/'SUMMARY.json',{'scheduled':27,'eligible':len(payloads),'source_records':9,'metadata_setup_pwd_calls':9,
                            'payload_fields':['prefix','cwd','tool_schema'],'outcomes_consulted':False})
    print('Prepared',len(payloads),'eligible payloads from 27 scheduled opportunities; no proposals generated')

def worker(payloads):
    data=''.join(json.dumps(p)+'\n' for p in payloads)
    r=subprocess.run([sys.executable,'-I',str(P/'policy.py')],input=data,text=True,capture_output=True,timeout=30)
    if r.returncode:raise RuntimeError('worker failed: '+r.stderr)
    return [json.loads(x) for x in r.stdout.splitlines()],r.stdout,r.stderr

def run(prepared,out):
    out.mkdir(parents=True,exist_ok=False)
    for rel,h in json.loads((prepared/'FREEZE.json').read_text()).items():assert sha(P.parent/rel)==h,rel
    payloads=jl(prepared/'PAYLOADS.jsonl');opps=jl(prepared/'OPPORTUNITIES.jsonl')
    proposals,raw,stderr=worker(payloads)
    (out/'WORKER_RAW.jsonl').write_text(raw);(out/'WORKER_STDERR.txt').write_text(stderr)
    assert len(proposals)==len(payloads)
    # Same frozen payloads, reordered and duplicated, cannot acquire task-ID or batch-state dependence.
    reverse,_,_=worker(list(reversed(payloads)));assert reverse==list(reversed(proposals))
    twice,_,_=worker(payloads+payloads);assert twice==proposals+proposals
    G,D,F=load_tool()
    specmod=importlib.util.spec_from_file_location('prior_directory_checker',OLD/'replay.py');m=importlib.util.module_from_spec(specmod);specmod.loader.exec_module(m)
    def snapshot(fs):
        def node(x):
            if isinstance(x,F):return {'name':x.name,'type':'file','content':x.content}
            assert isinstance(x,D)
            return {'name':x.name,'type':'directory','contents':{k:node(v) for k,v in x.contents.items()}}
        names=[];cur=fs._current_dir
        while cur is not None:names.append(cur.name);cur=cur.parent
        return {'tree':node(fs.root),'cwd':'/'+'/'.join(reversed(names))}
    def init(row):
        fs=G();fs._load_scenario(copy.deepcopy(row['filesystem_config']),long_context=False);return fs
    rows={r['item_id']:r for r in jl(OLD/'restoration_attempt_01/SOURCE_PROJECTION.jsonl')}
    specs={r['item_id']:r for r in jl(OLD/'restoration_attempt_01/TASK_SPECS.jsonl')}
    results=[]
    for op in opps:
        result={**op,'binary_usefulness':None,'fractional_utility':None,'reuse_witness':None}
        if op['status']!='eligible':result['outcome']='NOT_ELIGIBLE';results.append(result);continue
        row=rows[op['item_id']];payload=payloads[op['payload_index']];proposal=proposals[op['payload_index']]
        result.update(proposal=proposal,payload_sha256=digest(payload),counts={'early_ls':0,'final_fresh_ls':0,'reference_ls':0,'execution_setup_pwd':1})
        try:
            fs=init(row);assert fs.pwd()['current_working_directory']==payload['cwd'];before=snapshot(fs);receipt=None
            if proposal['status']=='proposed':
                c=proposal['candidate'];assert c['operation']=='ls' and c['directory']==payload['cwd'] and type(c['a']) is bool
                output=fs.ls(a=c['a']);after=snapshot(fs);assert before==after
                receipt={'candidate_sha256':digest(c),'environment_sha256':digest(before),'output':output,
                         'output_sha256':digest(output),'decision_event':1,'execution_event':2,'before_after_equal':True}
                result['counts']['early_ls']=1;result['receipt']=receipt
            if op['item_id'] not in specs:
                result['outcome']='FINAL_CHECKER_UNSUPPORTED';result['receipt_observed_but_not_judged']=receipt is not None
            else:
                spec=specs[op['item_id']];expected=m.source_expectation(row,spec)
                baseline=init(row);reference=baseline.ls(a=spec['include_hidden']);result['counts']['reference_ls']=1
                # Evaluator-only static-state witness test; never passed to the candidate worker.
                reuse=receipt is not None and proposal['candidate']['directory']==expected['directory'] and receipt['environment_sha256']==digest(snapshot(fs)) and (proposal['candidate']['a'] or not spec['include_hidden'])
                if reuse:
                    entries=receipt['output']['current_directory_content'];origin='early_receipt'
                else:
                    entries=fs.ls(a=spec['include_hidden'])['current_directory_content'];origin='fresh_final_lookup';result['counts']['final_fresh_ls']=1
                actual={'directory':snapshot(fs)['cwd'],'entries':entries};checks=m.task_check(expected,actual,before,snapshot(fs))
                correct=all(checks.values()) and sorted(reference['current_directory_content'])==expected['entries']
                if not correct:raise AssertionError('Independent final task or reference failed')
                result.update(outcome='SUPPORTED_FINAL_TASK_CORRECT',final_task_checks=checks,final_output=actual,
                              reuse_witness=bool(reuse),trace={'origin':origin,'receipt_sha256':digest(receipt) if reuse else None,
                               'contributing_entries':entries if reuse else []},
                              observed_consumed_fraction=len(entries)/len(receipt['output']['current_directory_content']) if reuse and receipt['output']['current_directory_content'] else None,
                              freshness_basis='evaluator-only full static snapshot; not deployable freshness validation')
            results.append(result)
        except Exception:
            result.update(outcome='FAIL_PRESERVED',traceback=traceback.format_exc());results.append(result)
        (out/'PARTIAL.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in results))
    assert len(results)==27
    summary={'scheduled':27,'eligible':len(payloads),'proposed':sum(p['status']=='proposed' for p in proposals),
             'abstained':sum(p['status']=='abstain' for p in proposals),'supported_final_checks':sum(r['outcome']=='SUPPORTED_FINAL_TASK_CORRECT' for r in results),
             'unsupported_final_checks':sum(r['outcome']=='FINAL_CHECKER_UNSUPPORTED' for r in results),
             'positive_execution_witnesses':sum(r['reuse_witness'] is True for r in results),
             'failed':sum(r['outcome']=='FAIL_PRESERVED' for r in results),
             'operation_counts':{k:sum(r.get('counts',{}).get(k,0) for r in results) for k in ['early_ls','final_fresh_ls','reference_ls','execution_setup_pwd']},
             'count_scope':'symbolic operation counts; excludes simulator construction/checker overhead, not latency or compute',
             'metadata_setup_pwd_calls':9,'research_binary_labels_created':0,'model_forwards':0,'human_G1':'PENDING',
             'interpretation':'Authored prefix-rule and privileged static-environment reuse witnesses on selected exposed tasks; no H2/H3/S1 inference'}
    save(out/'SUMMARY.json',summary);save(out/'WORKER_CHECKS.json',{'reverse_order_equal':True,'duplicate_payloads_equal':True,'worker_uses_only_stdin':True,'not_an_OS_sandbox':True})
    (out/'RESULTS.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in results));print(json.dumps(summary,indent=2))
    if summary['failed']:raise SystemExit(1)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['prepare','run']);ap.add_argument('--prepared',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    try:
        if a.mode=='prepare':prepare(a.out)
        else:run(a.prepared,a.out)
    except Exception:
        if a.out.exists():(a.out/'FAILURE.txt').write_text(traceback.format_exc())
        raise
