"""Replay stored counts, payload isolation and witness provenance without tool execution."""
import hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parent;OLD=P.parent/'public_directory_adapter_v0_1'
def jl(p):return [json.loads(x) for x in p.read_text().splitlines()]
def dig(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
for rel,h in json.loads((P/'preparation_02/FREEZE.json').read_text()).items():assert hashlib.sha256((P.parent/rel).read_bytes()).hexdigest()==h,rel
rows={r['item_id']:r for r in jl(OLD/'restoration_attempt_01/SOURCE_PROJECTION.jsonl')}
specs={r['item_id']:r for r in jl(OLD/'restoration_attempt_01/TASK_SPECS.jsonl')}
opps=jl(P/'preparation_02/OPPORTUNITIES.jsonl');payloads=jl(P/'preparation_02/PAYLOADS.jsonl');props=jl(P/'execution_01/WORKER_RAW.jsonl');results=jl(P/'execution_01/RESULTS.jsonl')
assert len(opps)==len(payloads)==len(props)==len(results)==27
assert [r['opportunity_id'] for r in results]==[r['opportunity_id'] for r in opps]
witnesses=[];unsupported_proposals=0
for op,res in zip(opps,results):
    row=rows[op['item_id']];payload=payloads[op['payload_index']];words=list(re.finditer(r'\S+',row['question'][0][0]['content']))
    assert len(words)>op['checkpoint_words']
    assert payload['prefix']==row['question'][0][0]['content'][:words[op['checkpoint_words']-1].end()]
    assert set(payload)=={'prefix','cwd','tool_schema'} and payload['cwd']=='/'+next(iter(row['filesystem_config']['root']))
    assert dig(payload)==res['payload_sha256'] and res['proposal']==props[op['payload_index']]
    assert res['binary_usefulness'] is None and res['fractional_utility'] is None
    if res['proposal']['status']=='proposed':
        q=res['receipt'];assert q['candidate_sha256']==dig(res['proposal']['candidate']) and q['output_sha256']==dig(q['output'])
        assert q['decision_event']<q['execution_event'] and q['before_after_equal']
    if op['item_id'] not in specs:
        assert res['outcome']=='FINAL_CHECKER_UNSUPPORTED' and res['reuse_witness'] is None
        unsupported_proposals+=res['proposal']['status']=='proposed';continue
    root=specs[op['item_id']]['target_root_name'];expected=sorted(row['filesystem_config']['root'][root]['contents'])
    assert res['final_output']['directory']=='/'+root and sorted(res['final_output']['entries'])==expected
    assert all(res['final_task_checks'].values())
    if res['reuse_witness']:
        assert res['counts']['final_fresh_ls']==0 and res['trace']['origin']=='early_receipt'
        assert res['trace']['receipt_sha256']==dig(res['receipt'])
        assert res['trace']['contributing_entries']==res['receipt']['output']['current_directory_content']
        witnesses.append(res)
    else:assert res['proposal']['status']=='abstain' and res['counts']['final_fresh_ls']==1
assert len(witnesses)==8 and len({r['item_id'] for r in witnesses})==4 and len({r['instruction_group'] for r in witnesses})==3
assert unsupported_proposals==4
summary=json.loads((P/'execution_01/SUMMARY.json').read_text())
assert summary['proposed']==12 and summary['abstained']==15 and summary['failed']==0
for k in ['early_ls','final_fresh_ls','reference_ls','execution_setup_pwd']:assert summary['operation_counts'][k]==sum(r['counts'][k] for r in results)
report={'status':'PASS_STORED_EVIDENCE','scheduled_verified':27,'payload_fields_and_literal_prefixes_verified':True,'receipt_trace_links_verified':True,
        'positive_execution_witnesses':8,'witness_source_records':4,'witness_instruction_groups':3,'unsupported_early_proposals':4,
        'research_usefulness_labels_created':0,'scope':'Stored evidence/provenance verification; not validation of rubric labels or deployment utility'}
with (P/'VERIFICATION.json').open('x') as f:f.write(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
