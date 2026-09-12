import urllib.request,json,pathlib,hashlib,datetime,concurrent.futures
p=pathlib.Path(__file__).resolve().parent;out=p/'samples';out.mkdir(exist_ok=True)
jobs=[]
for k,name in [('complex','ComplexFuncBench.jsonl'),('tiny','testing_data.json')]:
 r=json.loads((p/'additional'/f'{k}_hf_meta.raw').read_text());jobs.extend([(k+'_data',f"https://huggingface.co/datasets/{r['id']}/resolve/{r['sha']}/{name}"),(k+'_card',f"https://huggingface.co/datasets/{r['id']}/resolve/{r['sha']}/README.md")])
jobs.append(('lost_commit','https://api.github.com/repos/microsoft/lost_in_conversation/commits/main'))
def run(pair):
 k,u=pair;r={'key':k,'url':u,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(u,timeout=25) as f:b=f.read(20000001)
  if len(b)>20000000:raise ValueError('bounded 20MB limit reached; not a full snapshot')
  (out/(k+'.raw')).write_bytes(b);r.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
 except Exception as e:r['error']=str(e)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:r=list(pool.map(run,jobs))
(out/'manifest.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
