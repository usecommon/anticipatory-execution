import urllib.request,json,pathlib,hashlib,datetime,concurrent.futures
out=pathlib.Path(__file__).resolve().parent
repos={'bfcl':('ShishirPatil/gorilla','main'),'sgd':('google-research-datasets/dstc8-schema-guided-dialogue','master'),'toolsandbox':('apple-aiml-research/ToolSandbox','main'),'smcalflow':('microsoft/task_oriented_dialogue_as_dataflow_synthesis','master'),'evolving':('microsoft/evolving-intent','main'),'lost':('microsoft/lost_in_conversation','main'),'tau':('sierra-research/tau2-bench','main'),'multiwoz':('budzianowski/multiwoz','master')}
def get(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AEB-public-dataset-research'}),timeout=40).read()
def run(pair):
 key,(repo,branch)=pair; log={'key':key,'repo':repo,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[],'errors':[]}; d=out/key;d.mkdir(exist_ok=True)
 try:
  meta=json.loads(get(f'https://api.github.com/repos/{repo}/commits/{branch}'));sha=meta['sha'];log['revision']=sha
  tree=json.loads(get(f'https://api.github.com/repos/{repo}/git/trees/{sha}?recursive=1'));(d/'tree.json').write_text(json.dumps(tree));log['tree_truncated']=tree.get('truncated')
  paths=[e['path'] for e in tree['tree'] if e['type']=='blob'];(d/'paths.txt').write_text('\n'.join(paths))
  selected=[p for p in paths if p.lower() in ['readme.md','license','license.txt','license-code','datasets/license']]
  extra={'bfcl':['berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json','berkeley-function-call-leaderboard/bfcl_eval/possible_answer/BFCL_v4_multi_turn_base.json','berkeley-function-call-leaderboard/bfcl_eval/eval_checker/multi_turn_eval/multi_turn_checker.py'],'sgd':['train/dialogues_001.json','train/schema.json'],'lost':['data/sharded_instructions_600.json'],'multiwoz':['data/MultiWOZ_2.2/README.md'],'smcalflow':['README-SEMANTICS.md']}.get(key,[])
  selected+=extra
  for p in selected:
   url=f'https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(p)}'
   try:
    raw=get(url);dest=d/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw);log['files'].append({'path':p,'url':url,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
   except Exception as e:log['errors'].append({'url':url,'error':str(e)})
 except Exception as e:log['errors'].append({'error':str(e)})
 (d/'manifest.json').write_text(json.dumps(log,indent=2));return {'key':key,'revision':log.get('revision'),'files':len(log['files']),'errors':log['errors']}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for r in pool.map(run,repos.items()):print(json.dumps(r),flush=True)
