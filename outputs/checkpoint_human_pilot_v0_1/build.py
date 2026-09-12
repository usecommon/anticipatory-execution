import collections,hashlib,json,random,re
from pathlib import Path
p=Path(__file__).resolve().parent;source=p.parent/'shared_policy_pilot_v0_1/EVALUATOR_CONTEXT.jsonl';old=p.parent/'shared_policy_pilot_v0_1/ALL_OPPORTUNITIES.jsonl'
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
rows=read(source);assert len(rows)==300;out=[]
for r in rows:
 words=list(re.finditer(r'\S+',r['full_instruction']))
 for k in [12,18]:
  state='eligible' if len(words)>k else 'complete_at_checkpoint' if len(words)==k else 'checkpoint_not_reached'
  out.append({'item_id':f'CP1-{r["item_id"]}-W{k}','task_id':r['item_id'],'source':r['source'],'source_task_id':r['source_task_id'],'template_group':r['template_group'],'domain':r['domain'],'full_instruction':r['full_instruction'],'checkpoint_words':k,'checkpoint_status':state,'prefix':r['full_instruction'][:words[k-1].end()] if len(words)>=k else None})
prefixes=sorted({r['prefix'] for r in out if r['checkpoint_status']=='eligible'});random.Random(260913120).shuffle(prefixes);lookup={v:f'N{i:03d}' for i,v in enumerate(prefixes,1)}
for r in out:r['prefix_group']=lookup.get(r['prefix']) if r['checkpoint_status']=='eligible' else None
# The frozen instruction file says six-word prefix. Only replace that checkpoint-specific phrase before dispatch.
f=p/'PROPOSER_INSTRUCTIONS.txt';s=f.read_text().replace('six-word prefix','observed instruction prefix');f.write_text(s)
def write(n,rs):
 f=p/n;assert not f.exists(),f;f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
write('SCHEDULED_OPPORTUNITIES.jsonl',out)
for n in [1,2]:write(f'PROPOSER_{n}_INPUT.jsonl',[{'item_id':lookup[v],'prefix':v} for v in prefixes[n-1::2]])
write('PREFIX_GROUPS.jsonl',[{'item_id':lookup[v],'prefix':v,'opportunity_ids':[r['item_id'] for r in out if r['checkpoint_status']=='eligible' and r['prefix']==v]} for v in prefixes])
manifest={str(f.relative_to(p.parent)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [source,old]};(p/'SOURCE_HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n')
status={'scheduled':600,'unique_eligible_prefixes':len(prefixes),'by_source_checkpoint':{f'{s}:{k}':dict(collections.Counter(r['checkpoint_status'] for r in out if r['source']==s and r['checkpoint_words']==k)) for s in ['public_bfcl','synthetic'] for k in [12,18]},'six_word_baseline':'Frozen and unchanged; later joined without old labels'};(p/'BUILD_QA.json').write_text(json.dumps(status,indent=2)+'\n');print(json.dumps(status,indent=2))
