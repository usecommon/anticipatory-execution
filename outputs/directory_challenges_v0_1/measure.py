"""Authored in-memory provider and scoped reuse measurement; no research labeling."""
import copy,hashlib,json

def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def seal(body):return {**copy.deepcopy(body),'sha256':digest(body)}
def intact(receipt):return receipt['sha256']==digest({k:v for k,v in receipt.items() if k!='sha256'})

def guard(receipt,task,metadata):
    """No final directory entries or evaluator fields are accepted here."""
    if metadata is not None and set(metadata)!={'directory','incarnation','revision'}:raise ValueError('metadata allowlist violation')
    if set(task)!={'directory','include_hidden'}:raise ValueError('task allowlist violation')
    if not intact(receipt):return 'integrity_failure'
    if receipt['directory']!=task['directory']:return 'target_changed'
    if metadata is None or metadata['incarnation'] is None or metadata['revision'] is None:return 'metadata_unavailable'
    if metadata['directory']!=task['directory']:raise ValueError('provider target mismatch')
    if receipt['incarnation']!=metadata['incarnation']:return 'incarnation_changed'
    if receipt['revision']!=metadata['revision']:return 'revision_changed'
    if task['include_hidden'] and not receipt['include_hidden']:return 'insufficient_request_coverage'
    return 'eligible'

def required_names(task,final):
    """Independent task oracle. Does not consume the receipt or policy metadata."""
    if task['directory'] not in final:return None
    return sorted(name for name in final[task['directory']]['entries'] if task['include_hidden'] or not name.startswith('.'))

def run_case(c):
    initial=c['initial'];final=c['final'];candidate=c['candidate'];task=c['task'];state=initial[candidate['directory']]
    receipt=seal({'directory':candidate['directory'],'incarnation':state['incarnation'],'revision':state['revision'],
                  'include_hidden':candidate['include_hidden'],
                  'entries':[n for n in state['entries'] if candidate['include_hidden'] or not n.startswith('.')]})
    original_receipt=copy.deepcopy(receipt)
    if c['tamper_receipt']:receipt['entries'][0]='CORRUPTED'
    final_node=final.get(task['directory'])
    metadata=None if final_node is None else {'directory':task['directory'],'incarnation':final_node['incarnation'],'revision':final_node['revision']}
    decision=guard(receipt,task,metadata);reuse=decision=='eligible' and c['executor_mode']!='ignore'
    read_units=len(receipt['entries']) if reuse or c['executor_mode']=='read_irrelevant' else 0
    expected=required_names(task,final)
    counts={'early_listing':1,'metadata_query':1,'fresh_final_listing':0,'offline_oracle_name_reads':int(expected is not None)}
    if expected is None:
        actual=None;correct=None;reuse=False;contribution=0;witness=None
    else:
        if reuse:
            actual=sorted(n for n in receipt['entries'] if task['include_hidden'] or not n.startswith('.'))
        else:
            actual=sorted(n for n in final_node['entries'] if task['include_hidden'] or not n.startswith('.'))
            counts['fresh_final_listing']=1
        correct=actual==expected
        contribution=len(actual) if reuse and correct else 0
        # Offline witness can exist when metadata is unavailable or the executor ignores work.
        witness=intact(receipt) and receipt['directory']==task['directory'] and receipt['incarnation']==final_node['incarnation'] and sorted(n for n in receipt['entries'] if task['include_hidden'] or not n.startswith('.'))==expected
    return {'id':c['id'],'origin':'authored_software_fixture','decision_reason':decision,'reused':reuse,
            'final_task_correct':correct,'offline_witness':witness,'read_units':read_units,'contributing_units':contribution,
            'original_receipt':original_receipt,'presented_receipt':receipt,'metadata_view':metadata,
            'actual_entries':actual,'oracle_expected_entries':expected,'operation_counts':counts,
            'binary_usefulness':None,'fractional_utility':None,
            'scope':'Mock provider with declared revision contract; offline witness is not a deployed freshness guarantee'}
