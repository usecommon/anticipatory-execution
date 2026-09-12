import urllib.request,urllib.parse,json,pathlib,hashlib,datetime,concurrent.futures
out=pathlib.Path(__file__).resolve().parent/'additional';out.mkdir(exist_ok=True)
def get(u):return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'AEB-dataset-audit'}),timeout=20).read()
jobs=[]
base='https://raw.githubusercontent.com/ShishirPatil/gorilla/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/'
for key,p in [('bfcl_answers','data/possible_answer/BFCL_v4_multi_turn_base.json'),('bfcl_checker','eval_checker/multi_turn_eval/multi_turn_checker.py'),('bfcl_math','eval_checker/multi_turn_eval/func_source_code/math_api.py')]:jobs.append((key,base+p))
for k,repo in [('complex','zai-org/ComplexFuncBench'),('tiny','squeeze-ai-lab/TinyAgent-dataset')]:jobs.append((k+'_hf_meta','https://huggingface.co/api/datasets/'+repo))
jobs.append(('inclinc_page','https://fordatis.fraunhofer.de/handle/fordatis/213?locale=en'))
def run(pair):
 k,u=pair;r={'key':k,'url':u,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  b=get(u);(out/(k+'.raw')).write_bytes(b);r.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
 except Exception as e:r['error']=str(e)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:r=list(pool.map(run,jobs))
(out/'manifest.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
