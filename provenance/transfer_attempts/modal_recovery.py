from pathlib import Path
import modal,json
app=modal.App('aeb-github-evidence-recovery')
image=modal.Image.debian_slim(python_version='3.11')
for run in ['closure_a_20260911T175740Z','closure_c_20260911T180932Z']:
 image=image.add_local_file(Path('outputs/g0_closure_v0_5')/run/'final_manifest.json','/expected/'+run+'.json')
source=modal.Volume.from_name('aeb-g0-closure-v0-5')
transfer=modal.Volume.from_name('aeb-g0-github-transfer',create_if_missing=True)
@app.function(image=image,cpu=1,memory=1024,timeout=600,retries=0,volumes={'/evidence':source.with_mount_options(read_only=True),'/transfer':transfer})
def pack():
 import hashlib,zipfile,json
 from pathlib import Path
 rows=[];dst=Path('/transfer/pipeline_verified.zip')
 with zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED,compresslevel=1) as z:
  for run in ['closure_a_20260911T175740Z','closure_c_20260911T180932Z']:
   expected=json.loads((Path('/expected')/(run+'.json')).read_text())
   for rel,h in expected.items():
    if not rel.startswith('pipeline_job/'):continue
    p=Path('/evidence')/run/rel;b=p.read_bytes()
    if hashlib.sha256(b).hexdigest()!=h:raise RuntimeError('Original checksum mismatch: '+run+'/'+rel)
    name='outputs/g0_closure_v0_5/'+run+'/'+rel;z.writestr(name,b);rows.append({'path':name,'sha256':h,'bytes':len(b)})
 transfer.commit()
 return {'asset':'modal_pipeline_tensors_verified.zip','bytes':dst.stat().st_size,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'files':rows}
@app.function(image=image,cpu=0.25,memory=256,timeout=120,retries=0,max_containers=4,volumes={'/transfer':transfer.with_mount_options(read_only=True)})
def chunk(index):
 with open('/transfer/pipeline_verified.zip','rb') as f:
  f.seek(index*512*1024);return f.read(512*1024)
@app.local_entrypoint()
def main():
 import hashlib,math,json
 out=Path('outputs/github_complete_release');meta=pack.remote();(out/'REMOTE_ASSET.json').write_text(json.dumps(meta,indent=2));print('Remote files verified:',len(meta['files']),flush=True)
 dst=out/meta['asset']
 with dst.open('wb') as f:
  for i,b in enumerate(chunk.map(range(math.ceil(meta['bytes']/(512*1024))))):
   f.write(b)
   if i%32==0:print('Chunks received',i+1,flush=True)
 if hashlib.sha256(dst.read_bytes()).hexdigest()!=meta['sha256']:raise RuntimeError('Archive transport mismatch')
 print('PASS remote archive',meta['bytes'],flush=True)
