import json,hashlib,random,re
from pathlib import Path
p=Path(__file__).resolve().parent;repo=p.parents[1];src=repo/'outputs/synthetic_expansion_v0_1/dataset/ITEMS.jsonl'
rows=[json.loads(x) for x in src.read_text().splitlines()];out=[]
styles=['Please {p}','I need you to {p}','For this request, {p}','Help me {p}','For now, {p}']
# New surface variants; template lineage is retained rather than claimed independent.
for vi,style in enumerate(styles,1):
 for r in rows:
  prefix=style.format(p=r['prefix'][0].lower()+r['prefix'][1:]);suffix=r['full_instruction'][len(r['prefix']):]
  row={k:v for k,v in r.items() if k not in ['item_id','task_id','family_id','prefix','full_instruction','provenance']}
  row.update(item_id=f'SC1-V{vi}-{r["item_id"]}',task_id=f'SC1-V{vi}-{r["task_id"]}',family_id=f'SC1-V{vi}-{r["family_id"]}',template_group=r['family_id'],parent_item_id=r['item_id'],prefix=prefix,full_instruction=prefix+suffix,provenance='AI-authored synthetic surface expansion of existing fixture; new judgment required; labels not inherited.',variant_type='request_framing_paraphrase',surface_variant=vi)
  out.append(row)
assert len(out)==1000 and len({(r['prefix'],r['candidate_action'],r['full_instruction']) for r in out})==1000
p.mkdir(exist_ok=True)
def write(name,rs):
 f=p/name
 if f.exists():raise SystemExit('refuse overwrite '+str(f))
 f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs))
write('ALL_CANDIDATES.jsonl',out)
order=list(out);random.Random(2609121000).shuffle(order)
for k in range(3):
 subset=order[k::3];blind=[];mapping=[]
 for i,r in enumerate(subset,1):
  bid=f'R{k+1}-{i+1:04d}';mapping.append({'blind_id':bid,'item_id':r['item_id']});blind.append({'item_id':bid,**{f:r[f] for f in ['prefix','candidate_action','execution_class','work_product','full_instruction','fixture_contract']}})
 write(f'JUDGE_{k+1}_INPUT.jsonl',blind);write(f'JUDGE_{k+1}_MAPPING.jsonl',mapping)
qa={'items':1000,'task_variants':500,'scenario_variants':250,'independent_template_groups':50,'domains':len({r['domain'] for r in out}),'all_literal_prefixes':all(r['full_instruction'].startswith(r['prefix']) for r in out),'labels_transferred':0,'variation':'Five request-framing paraphrases per prior item; work products and semantic conditions retained. Not 1000 independent tasks.','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()};(p/'BUILD_QA.json').write_text(json.dumps(qa,indent=2)+'\n');print(qa)
