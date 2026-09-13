import modal
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1] if modal.is_local() else Path('/')
app=modal.App('aeb-exploratory-verification-tail-v0-1')
base=modal.Image.debian_slim(python_version='3.11').pip_install('torch==2.5.1','transformers==4.45.2','accelerate==0.34.2','numpy==1.26.4','huggingface_hub==0.25.2')
if modal.is_local():
 import json
 freeze=json.loads((O/'FREEZE.json').read_text())
 for name in ['research.jsonl','preflight.json']:base=base.add_local_file(R/freeze['local_files'][name],'/src/'+name)
evidence=modal.Volume.from_name('aeb-exploratory-extraction-v0-1')
@app.function(image=base,cpu=2,memory=8192,timeout=600,retries=0,max_containers=4,volumes={'/evidence':evidence.with_mount_options(read_only=True)})
def verify_shard(label,start_index,end_index):
 import json,hashlib,time,os,torch,io
 torch.set_num_threads(2);start=time.time();root=Path('/evidence')/label
 def sha(p):
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
  return h.hexdigest()
 manifest=json.loads((root/'extraction/manifest.json').read_text());inputs=[json.loads(x) for x in Path('/src/research.jsonl').read_text().splitlines()]
 preflight={r['id']:r for r in json.loads(Path('/src/preflight.json').read_text())['rows']}
 assert manifest['status']=='PASS' and manifest['partition']=='exploratory' and manifest['confirmatory'] is False
 assert len(inputs)==len(manifest['items'])==4013
 contract=manifest['contract_id'];assert contract=='95dd7686f82fc1380c02539ec14fc73ab3073fc8be7b7ca015e40fd6e4fac1b0'
 hashes=json.loads((root/'HASHES.json').read_text());bytes_total=0;checked=[]
 assert type(start_index) is int and type(end_index) is int and 0<=start_index<end_index<=4013
 for r,inp in zip(manifest['items'][start_index:end_index],inputs[start_index:end_index]):
  path=root/'extraction'/r['file'];blob=path.read_bytes();actual=hashlib.sha256(blob).hexdigest()
  assert actual==r['sha256']==hashes['extraction/'+r['file']]
  assert r['id']==inp['id'] and r['prefix_sha256']==hashlib.sha256(inp['prefix'].encode()).hexdigest()
  assert r['token_ids']==preflight[r['id']]['token_ids'] and r['contract_id']==contract
  d=torch.load(io.BytesIO(blob),map_location='cpu',weights_only=True);n=r['active_length']
  assert set(d)=={'contract_id','input_ids','attention_mask','position_ids','active_length','hidden_last','logits_last'}
  assert d['contract_id']==contract and d['active_length']==n
  assert d['hidden_last'].shape==(29,3584) and d['logits_last'].shape==(152064,)
  assert d['hidden_last'].dtype==d['logits_last'].dtype==torch.float32
  assert torch.isfinite(d['hidden_last']).all() and torch.isfinite(d['logits_last']).all()
  assert d['input_ids'].shape==(1,128) and d['input_ids'][0,:n].tolist()==r['token_ids']
  assert (d['input_ids'][0,n:]==151643).all()
  assert d['attention_mask'].shape==(1,128) and d['attention_mask'][0,:n].all() and not d['attention_mask'][0,n:].any()
  assert torch.equal(d['position_ids'],torch.arange(128).unsqueeze(0))
  bytes_total+=path.stat().st_size;checked.append({'id':r['id'],'sha256':actual})
  if len(checked)%250==0:print(f'Shard {start_index}:{end_index}: {len(checked)} checked',flush=True)
 assert len(list((root/'extraction').glob('*.pt')))==4013
 audit=json.loads((root/'forward_audit.json').read_text());assert len(audit)==4013
 assert all(x['contract_id']==contract and x['shape']==[1,128] and x['mask_shape']==[1,1,128,128] and x['cache'] is False for x in audit)
 for name,h in hashes.items():
  if not name.endswith('.pt'):assert sha(root/name)==h
 return {'status':'PASS','checked_tensors':len(checked),'start_index':start_index,'end_index':end_index,'tensor_bytes':bytes_total,'seconds':time.time()-start,'container_id':os.getenv('MODAL_TASK_ID'),'independent_CPU_worker':True,'all_hashes_shapes_tokens_masks_positions_finite_pass':True,'checked':checked,'contract_id':contract,'manifest_sha256':sha(root/'extraction/manifest.json')}
@app.local_entrypoint()
def main():
 import json,datetime,hashlib,traceback,concurrent.futures,shutil
 target='run_20260913T003027625834Z';prior=O/'verification_recovery_20260913T011036317129Z'
 out=O/('verification_tail_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));out.mkdir()
 ranges=[(3012,3263),(3263,3514),(3514,3765),(3765,4013)]
 retained=[];sources={}
 for a,b in [(0,1004),(1004,2008),(2008,3012)]:
  p=prior/f'shard_{a}_{b}.json';d=json.loads(p.read_text());assert d['status']=='PASS' and d['checked_tensors']==b-a
  sources[str(p.relative_to(O))]=hashlib.sha256(p.read_bytes()).hexdigest();shutil.copyfile(p,out/p.name);retained.append(d)
 (out/'REQUEST.json').write_text(json.dumps({'target':target,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'retained_sources':sources,'ranges':ranges,'GPU':False,'timeout_seconds_per_shard':600,'max_containers':4},indent=2))
 try:
  def one(bounds):
   a,b=bounds;v=verify_shard.remote(target,a,b);(out/f'tail_{a}_{b}.json').write_text(json.dumps(v,indent=2));return v
  with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:tails=list(pool.map(one,ranges))
  results=retained+tails;results.sort(key=lambda r:r['start_index']);checked=[x for r in results for x in r['checked']]
  assert len(checked)==len({r['id'] for r in checked})==4013
  assert all(r['status']=='PASS' and r['checked_tensors']==r['end_index']-r['start_index'] for r in results)
  assert len({r['manifest_sha256'] for r in results})==1 and len({r['contract_id'] for r in results})==1
  merged={'status':'PASS','checked_tensors':4013,'tensor_bytes':sum(r['tensor_bytes'] for r in results),'seconds':max(r['seconds'] for r in tails),'container_id':'multiple_CPU_workers','container_ids':sorted({r['container_id'] for r in results}),'independent_CPU_worker':True,'all_hashes_shapes_tokens_masks_positions_finite_pass':True,'checked':checked,'contract_id':results[0]['contract_id'],'manifest_sha256':results[0]['manifest_sha256'],'verification_kind':'bounded_parallel_tail_recovery','recovery_source':'modal_verify_tail.py','recovery_evidence':out.name}
  dest=O/target/'VERIFICATION.json'
  if dest.exists():raise FileExistsError(dest)
  dest.write_text(json.dumps(merged,indent=2));(out/'SUMMARY.json').write_text(json.dumps({k:v for k,v in merged.items() if k!='checked'},indent=2));print({k:v for k,v in merged.items() if k!='checked'},flush=True)
 except BaseException:
  (out/'FAILURE.txt').write_text(traceback.format_exc());raise
