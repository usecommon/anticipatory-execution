"""Audit complete extraction and independent CPU verification without loading weights."""
import ast,hashlib,json
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
freeze=json.loads((O/'FREEZE.json').read_text())
for name,rel in freeze['local_files'].items():assert sha(R/rel)==freeze['remote_files'][name],name
for p in O.glob('*.py'):ast.parse(p.read_text())
success=[]
for run in sorted(O.glob('run_*')):
 if not (run/'VERIFICATION.json').exists():continue
 request=json.loads((run/'REQUEST.json').read_text());ex=json.loads((run/'EXTRACTION_RESULT.json').read_text());v=json.loads((run/'VERIFICATION.json').read_text())
 assert request['freeze_sha256']==sha(O/'FREEZE.json') and request['launcher_sha256']==sha(O/'modal_extract.py') and request['plan_sha256']==sha(O/'RUN_PLAN.json')
 assert ex['execution']['status']=='PASS' and ex['execution']['exit']==0
 texts=ex['artifacts'];hashes=json.loads(texts['HASHES.json'])
 for name,text in texts.items():
  if name=='worker.log':
   assert sha(run/'worker_raw.log')==hashes[name] and (run/'worker_raw.log').read_text()==text
  elif name!='HASHES.json':assert hashlib.sha256(text.encode()).hexdigest()==hashes[name],name
 m=json.loads(texts['extraction/manifest.json']);w=json.loads(texts['WORKER_RESULT.json']);audit=json.loads(texts['forward_audit.json'])
 assert m['partition']=='exploratory' and m['status']=='PASS' and not m['confirmatory']
 assert m['entrypoint_sha256']==freeze['remote_files']['entrypoint.py'] and m['input_sha256']==freeze['remote_files']['research.jsonl']
 assert w['items']==w['actual_forwards']==len(audit)==len(m['items'])==4013 and w['probe_fitting'] is False
 assert v['status']=='PASS' and v['checked_tensors']==4013 and v['independent_CPU_worker']
 assert v['all_hashes_shapes_tokens_masks_positions_finite_pass']
 hw=json.loads(texts['hardware.json']);assert hw['container_id']!=v['container_id']
 if v.get('verification_kind','').startswith('bounded_parallel'):
  recovery=O/v['recovery_evidence'];rr=json.loads((recovery/'REQUEST.json').read_text())
  assert rr['source_sha256']==sha(O/v.get('recovery_source','modal_verify_recovery.py'))
  for path,h in rr.get('retained_sources',{}).items():
   assert sha(O/path)==h and (O/path).read_bytes()==(recovery/Path(path).name).read_bytes()
  shards=[json.loads(p.read_text()) for p in [*recovery.glob('shard_*.json'),*recovery.glob('tail_*.json')]]
  shards.sort(key=lambda x:x['start_index'])
  ranges=[(0,1004),(1004,2008),(2008,3012),(3012,4013)]
  if v['verification_kind']=='bounded_parallel_tail_recovery':ranges=[(0,1004),(1004,2008),(2008,3012),(3012,3263),(3263,3514),(3514,3765),(3765,4013)]
  assert [(x['start_index'],x['end_index']) for x in shards]==ranges
  assert all(x['status']=='PASS' and x['checked_tensors']==x['end_index']-x['start_index'] and x['container_id']!=hw['container_id'] for x in shards)
  assert [row for x in shards for row in x['checked']]==v['checked']
  assert sum(x['tensor_bytes'] for x in shards)==v['tensor_bytes']
 assert 'NVIDIA A100-SXM4-40GB' in hw['stdout']
 expected=[json.loads(x) for x in (R/freeze['local_files']['research.jsonl']).read_text().splitlines()]
 verified={x['id']:x['sha256'] for x in v['checked']};assert len(verified)==4013
 preflight={r['id']:r for r in json.loads((R/freeze['local_files']['preflight.json']).read_text())['rows']}
 assert len([k for k in hashes if k.endswith('.pt')])==4013
 for r,inp,a in zip(m['items'],expected,audit):
  assert r['id']==inp['id'] and r['prefix_sha256']==hashlib.sha256(inp['prefix'].encode()).hexdigest()
  assert r['sha256']==verified[r['id']]==hashes['extraction/'+r['file']]
  assert r['token_ids']==preflight[r['id']]['token_ids'] and r['active_length']==len(r['token_ids'])
  assert a['active_length']==r['active_length'] and a['shape']==[1,128] and a['mask_shape']==[1,1,128,128] and a['cache'] is False
  assert a['contract_id']==r['contract_id']==m['contract_id']==v['contract_id']==w['contract_id']=='95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0'
 progress=[json.loads(x) for x in texts['extraction/progress.jsonl'].splitlines()];assert progress==m['items']
 assert v['manifest_sha256']==hashes['extraction/manifest.json']
 success.append(run.name)
assert len(success)==1,success
print('PASS: 4013 exact input/manifest/forward/progress records; all tensor hashes independently verified on Modal CPU; source freeze and contract match; distinct GPU/CPU containers; no confirmatory extraction or probe fitting.')
