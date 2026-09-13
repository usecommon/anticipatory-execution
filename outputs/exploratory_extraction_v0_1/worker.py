"""Full frozen exploratory prefix extraction; no labels, probes or weights training."""
import json,sys,time,traceback
from pathlib import Path
import torch
from extractor import load_extractor,file_hash
from entrypoint import run_job,CONTRACT
root=Path(sys.argv[1]);start=time.time()
try:
 pins=json.loads(Path('/src/FREEZE.json').read_text())
 for name,sha in pins['remote_files'].items():
  if file_hash('/src/'+name)!=sha:raise ValueError('Source/input mismatch: '+name)
 identity=json.loads(Path('/src/identity.json').read_text())
 e=load_extractor('/model',identity)
 if e.contract_id!=CONTRACT:raise ValueError('Contract mismatch')
 (root/'contract.json').write_text(json.dumps(e.contract,indent=2))
 print('Identity and canonical contract verified; beginning whole-job preflight.',flush=True)
 manifest=run_job(e,'/src/research.jsonl',root/'extraction',partition='exploratory',preflight_file='/src/preflight.json')
 if len(manifest['items'])!=4013 or len(e.audit)!=4013:raise ValueError('Incomplete forward coverage')
 (root/'forward_audit.json').write_text(json.dumps(e.audit,indent=2))
 result={'status':'PASS','items':4013,'actual_forwards':len(e.audit),'contract_id':e.contract_id,'seconds':time.time()-start,'peak_cuda_bytes':torch.cuda.max_memory_allocated(),'partition':'exploratory','human_G1':'PENDING_DEFERRED','confirmatory':False,'probe_fitting':False}
 (root/'WORKER_RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
except BaseException:
 (root/'WORKER_FAILURE.json').write_text(json.dumps({'status':'BLOCKED','traceback':traceback.format_exc(),'seconds':time.time()-start},indent=2));raise
