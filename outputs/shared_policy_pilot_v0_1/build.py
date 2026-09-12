import collections,hashlib,json,random,re
from pathlib import Path
p=Path(__file__).resolve().parent;root=p.parent
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
sources=[root/'bfcl_public_pilot_v0_1/EVALUATOR_CONTEXT.jsonl',root/'bfcl_public_pilot_v0_1/DOMAIN_TAGS.jsonl',root/'synthetic_expansion_v0_1/dataset/ITEMS.jsonl']
dom={r['item_id']:r['domain'] for r in read(sources[1])};out=[]
for r in read(sources[0]):out.append({'item_id':'SP1-P-'+r['source_id'],'source':'public_bfcl','source_task_id':r['source_id'],'template_group':r['source_id'],'domain':dom[r['item_id']],'full_instruction':r['full_instruction']})
syn={}
for r in read(sources[2]):
 k=r['task_id'];v={'item_id':'SP1-S-'+k,'source':'synthetic','source_task_id':k,'template_group':r['family_id'],'domain':r['domain'],'full_instruction':r['full_instruction']}
 assert k not in syn or syn[k]==v;syn[k]=v
out.extend(syn.values());assert len(out)==300
for r in out:
 w=list(re.finditer(r'\S+',r['full_instruction']));assert len(w)>6;r['prefix']=r['full_instruction'][:w[5].end()];r['checkpoint_words']=6;r['exact_instruction_group']=hashlib.sha256(r['full_instruction'].encode()).hexdigest()
prefixes=sorted({r['prefix'] for r in out});random.Random(260912302).shuffle(prefixes);lookup={x:f'U{i:03d}' for i,x in enumerate(prefixes,1)}
for r in out:r['prefix_group']=lookup[r['prefix']]
def write(name,rs):
 f=p/name;assert not f.exists(),f;f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
write('EVALUATOR_CONTEXT.jsonl',out)
for n in [1,2]:write(f'PROPOSER_{n}_INPUT.jsonl',[{'item_id':lookup[x],'prefix':x} for x in prefixes[n-1::2]])
write('PREFIX_GROUPS.jsonl',[{'item_id':lookup[x],'prefix':x,'opportunity_ids':[r['item_id'] for r in out if r['prefix']==x]} for x in prefixes])
(p/'SOURCE_HASHES.json').write_text(json.dumps({str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sources},indent=2)+'\n')
(p/'BUILD_QA.json').write_text(json.dumps({'opportunities':300,'public_tasks':200,'synthetic_tasks':100,'unique_prefixes':len(prefixes),'proper_six_word_prefixes':True,'prefix_reuse_policy':'One generated proposal per exact prefix across all contexts; no source or multiplicity sent to proposer.'},indent=2)+'\n');print((p/'BUILD_QA.json').read_text())
