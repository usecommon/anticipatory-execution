"""Development-only evidence structure and authored directory-task checks.
No source admission, factual provenance certification, or usefulness labeling.
"""
import copy
import hashlib
import json


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def _object(value, keys, name):
    if type(value) is not dict or set(value) != set(keys):
        raise ValueError(name + ': exact nonempty schema required')


def _text(value, name):
    if type(value) is not str or not value.strip():
        raise ValueError(name + ': nonempty string required')


def _hash(value, name):
    if type(value) is not str or len(value) != 64 or any(c not in '0123456789abcdef' for c in value):
        raise ValueError(name + ': SHA256 required')


def _event(value):
    if type(value) is not int or value < 0:
        raise ValueError('event: nonnegative integer required')


def validate_decision(d):
    _object(d, ['schema', 'stage', 'event', 'prefix', 'context', 'candidate'], 'decision')
    if d['schema'] != 'aeb-decision-1' or d['stage'] != 'before_execution':
        raise ValueError('only versioned before_execution decisions supported')
    _event(d['event']); _text(d['prefix'], 'prefix')
    _object(d['context'], ['system', 'tool_schema', 'environment_metadata', 'provenance_ref'], 'context')
    for k in ['system', 'tool_schema', 'provenance_ref']:
        _text(d['context'][k], k)
    if type(d['context']['environment_metadata']) is not dict:
        raise ValueError('environment metadata must be an explicit dictionary')
    c = d['candidate']
    _object(c, ['operation', 'directory', 'include_hidden', 'proposal_event'], 'candidate')
    if c['operation'] != 'enumerate_directory' or type(c['include_hidden']) is not bool:
        raise ValueError('unsupported operation or hidden flag')
    _text(c['directory'], 'candidate directory'); _event(c['proposal_event'])
    if c['proposal_event'] > d['event']:
        raise ValueError('proposal must precede decision')
    return True


def predictor_payload(d):
    """Opaque event/provenance IDs are deliberately excluded from model features."""
    validate_decision(d)
    return copy.deepcopy({'prefix': d['prefix'],
            'context': {k: d['context'][k] for k in ['system', 'tool_schema', 'environment_metadata']},
            'candidate': {k: d['candidate'][k] for k in ['operation', 'directory', 'include_hidden']}})


def validate_evidence(e):
    _object(e, ['schema', 'decision', 'source', 'environment', 'receipt', 'trace', 'task_check'], 'evidence')
    if e['schema'] != 'aeb-evidence-1':
        raise ValueError('unsupported evidence schema')
    validate_decision(e['decision'])
    _object(e['source'], ['artifact_sha256', 'task_id', 'transformation_ref', 'origin'], 'source')
    _hash(e['source']['artifact_sha256'], 'source hash')
    for k in ['task_id', 'transformation_ref']: _text(e['source'][k], k)
    if e['source']['origin'] not in ['public_original', 'public_derived', 'synthetic_fixture']:
        raise ValueError('explicit source origin required')
    _object(e['environment'], ['decision_sha256', 'final_sha256', 'provenance_ref'], 'environment')
    for k in ['decision_sha256', 'final_sha256']: _hash(e['environment'][k], k)
    _text(e['environment']['provenance_ref'], 'environment provenance')
    q = e['receipt']
    _object(q, ['request_sha256', 'environment_sha256', 'execution_event', 'result', 'result_sha256'], 'receipt')
    _event(q['execution_event'])
    if q['execution_event'] <= e['decision']['event']:
        raise ValueError('execution must follow before_execution decision')
    if q['request_sha256'] != digest(e['decision']['candidate']):
        raise ValueError('receipt candidate mismatch')
    if q['environment_sha256'] != e['environment']['decision_sha256']:
        raise ValueError('receipt environment mismatch')
    if type(q['result']) is not list or any(type(x) is not str or not x for x in q['result']):
        raise ValueError('result must be entry-name list; empty directory allowed')
    if len(set(q['result'])) != len(q['result']) or q['result_sha256'] != digest(q['result']):
        raise ValueError('duplicate entries or result digest mismatch')
    _object(e['trace'], ['receipt_sha256', 'read_units', 'contributing_units'], 'trace')
    if e['trace']['receipt_sha256'] != digest(q): raise ValueError('trace receipt mismatch')
    for k in ['read_units', 'contributing_units']:
        v=e['trace'][k]
        if type(v) is not list or any(type(x) is not str for x in v) or len(set(v)) != len(v):
            raise ValueError('trace unit list invalid')
    if not set(e['trace']['contributing_units']) <= set(e['trace']['read_units']) <= set(q['result']):
        raise ValueError('trace units not linked to receipt')
    t=e['task_check']
    _object(t, ['checker_sha256', 'spec_sha256', 'final_environment_sha256', 'correct'], 'task check')
    for k in ['checker_sha256', 'spec_sha256', 'final_environment_sha256']: _hash(t[k], k)
    if type(t['correct']) is not bool or t['final_environment_sha256'] != e['environment']['final_sha256']:
        raise ValueError('task check type or environment mismatch')
    return {'status': 'STRUCTURE_VALIDATED_ONLY', 'public_admission': False, 'binary_usefulness': None}


def check_directory_task(spec, environment, actual):
    """Independent of candidate request/cache; task spec remains a trusted input.
    Authored flat-directory fixtures only; does not interpret BFCL instructions.
    """
    _object(spec, ['directory', 'include_hidden'], 'task spec')
    _text(spec['directory'], 'task directory')
    if type(spec['include_hidden']) is not bool: raise ValueError('task hidden flag')
    if type(environment) is not dict or spec['directory'] not in environment:
        raise ValueError('missing task environment')
    entries=environment[spec['directory']]
    if type(entries) is not list or any(type(x) is not str or not x for x in entries) or len(set(entries)) != len(entries):
        raise ValueError('invalid directory environment')
    _object(actual, ['directory', 'entries'], 'actual output')
    if type(actual['entries']) is not list or any(type(x) is not str for x in actual['entries']):
        raise ValueError('invalid actual entries')
    expected=sorted(x for x in entries if spec['include_hidden'] or not x.startswith('.'))
    correct=actual['directory']==spec['directory'] and sorted(actual['entries'])==expected
    return {'final_task_correct': correct, 'expected_entries': expected, 'binary_usefulness': None,
            'scope': 'authored flat-directory software fixture; supplied task semantics'}
