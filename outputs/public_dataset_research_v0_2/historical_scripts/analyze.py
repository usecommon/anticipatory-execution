import pathlib,json,hashlib,collections
p=pathlib.Path(__file__).resolve().parent
out=p.parents[1]/'outputs/anticipatory-execution/outputs/public_dataset_research_v0_2'
checks={}
f=p/'bfcl/berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json';r=[json.loads(x) for x in f.read_text().split('\n') if x.strip()];a=[json.loads(x) for x in (p/'additional/bfcl_answers.raw').read_text().splitlines()]
checks['bfcl']={'records':len(r),'unique_ids':len({x['id'] for x in r}),'reference_records':len(a),'ids_match':{x['id'] for x in r}=={x['id'] for x in a},'record_fields':list(r[0]),'content_inspected_ids':[r[0]['id']],'runtime_evaluator_checks':0}
f=p/'sgd/train/dialogues_001.json';r=json.loads(f.read_text());checks['sgd']={'file_dialogues':len(r),'unique_ids':len({x['dialogue_id'] for x in r}),'service_call_frames':sum('service_call' in f for d in r for t in d['turns'] for f in t['frames']),'service_results_frames':sum('service_results' in f for d in r for t in d['turns'] for f in t['frames']),'content_inspected_ids':[r[0]['dialogue_id']],'full_corpus_count_measured':False}
f=p/'lost/data/sharded_instructions_600.json';r=json.loads(f.read_text());checks['lost']={'records':len(r),'unique_ids':len({x['task_id'] for x in r}),'task_counts':dict(collections.Counter(x['task'] for x in r)),'claimed_filename_count':600,'count_discrepancy_preserved':len(r)!=600,'content_inspected_ids':[r[0]['task_id']],'record_fields':list(r[0])}
for k in ['complex','tiny']:
 f=p/'samples'/f'{k}_data.raw'
 if f.exists():
  raw=f.read_bytes(); result={'downloaded_bytes':len(raw),'downloaded_sha256':hashlib.sha256(raw).hexdigest(),'content_inspected_ids':[],'semantic_quality_validated':False}
  try:
   r=json.loads(raw);result.update(parse_complete=True,records=len(r),container_type=type(r).__name__)
  except json.JSONDecodeError as e:
   if k=='complex':
    valid=0;errors=[]
    for n,line in enumerate(raw.split(b'\n'),1):
     if not line.strip():continue
     try:json.loads(line);valid+=1
     except json.JSONDecodeError as er:errors.append({'line':n,'error':str(er)})
    result.update(parse_complete=not errors,valid_jsonl_records_in_download=valid,parse_errors=errors)
   else:result.update(parse_complete=False,parse_error=str(e))
   result['admission']='HOLD: received bytes end mid-string; incomplete transfer suspected, upstream malformedness not established; do not drop rows or infer complete-corpus size.'
  checks[k]=result
checks['scope']={'model_inference':False,'new_labels':0,'confirmatory_extraction':False,'development_extraction':False,'tokenizer_preflight':False,'G1':'PENDING','G0':'PASS_SCOPED_UNCHANGED','sampling':'File metadata/schema checks; tiny convenience content samples, not a prevalence estimate or representative quality audit.'}
(out/'FILE_AUDIT.json').write_text(json.dumps(checks,indent=2)+'\n')
manifest=[]
for f in sorted(p.glob('*/manifest.json')):
 r=json.loads(f.read_text());manifest.append({'evidence_group':f.parent.name,'result':r})
(out/'SOURCE_FETCH_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(out/'FETCH_FAILURES.json').write_text(json.dumps({'initial_sandbox':'DNS unavailable; no source bytes obtained','system_python_tls_failures':{f.stem:json.loads(f.read_text()) for f in (p/'fetch_failure_1').glob('*.json')},'web_failures':['inCLINC CSV and README returned Internal Error','TinyAgent dataset viewer exceeded web tool response size; data availability assessed separately','Two initially guessed TinyAgent dataset URLs were not retrievable; corrected to the publisher-linked squeeze-ai-lab/TinyAgent-dataset'],'subsequent_errors':'See SOURCE_FETCH_MANIFEST.json; failed attempts preserved even when later fetch succeeded.'},indent=2)+'\n')
print(json.dumps(checks,indent=2))
