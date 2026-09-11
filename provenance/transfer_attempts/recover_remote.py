from pathlib import Path
import hashlib,json,concurrent.futures,time,modal
base=Path.cwd();root=base/'work/github_complete/verified_remote';volume=modal.Volume.from_name('aeb-g0-closure-v0-5');jobs=[];records=[]
for r in root.iterdir():
 manifest=json.loads((base/'outputs/g0_closure_v0_5'/r.name/'final_manifest.json').read_text())
 for rel,expected in manifest.items():
  if not rel.startswith('pipeline_job/'):continue
  p=r/rel
  if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==expected:
   records.append({'run':r.name,'path':rel,'status':'PASS','already_valid':True});continue
  jobs.append((r.name,rel,expected,p))
def get(job):
 run,rel,expected,p=job
 for attempt in range(1,4):
  tmp=p.with_suffix(p.suffix+'.download')
  try:
   with tmp.open('wb') as f:
    for chunk in volume.read_file(run+'/'+rel):f.write(chunk)
   if hashlib.sha256(tmp.read_bytes()).hexdigest()!=expected:raise ValueError('Checksum mismatch')
   tmp.replace(p);return {'run':run,'path':rel,'status':'PASS','attempt':attempt}
  except Exception as e:
   print(json.dumps({'run':run,'path':rel,'attempt':attempt,'error_type':type(e).__name__}),flush=True)
   if attempt==3:return {'run':run,'path':rel,'status':'FAIL','error_type':type(e).__name__}
print('Files needing recovery: '+str(len(jobs)),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for result in pool.map(get,jobs):
  records.append(result)
  if len(records)%20==0:print('Verified/reported '+str(len(records)),flush=True)
report={'status':'PASS' if all(x['status']=='PASS' for x in records) else 'BLOCKED','checks':records}
(base/'work/github_complete/REMOTE_RECOVERY_VERIFICATION.json').write_text(json.dumps(report,indent=2));print(report['status'],len(records),flush=True)
if report['status']!='PASS':raise SystemExit(1)
