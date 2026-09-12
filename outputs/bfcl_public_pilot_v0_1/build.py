"""Frozen prefix boundary adapter. No tool execution or model features."""
import argparse,hashlib,json,random,re,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--license',type=Path,required=True);a=ap.parse_args()
expected='1a21a995d06fd6f20ba55de7bced30ef953ec35e998f502ec2ecf4d66ef1c43a'
assert hashlib.sha256(a.source.read_bytes()).hexdigest()==expected
assert hashlib.sha256(a.license.read_bytes()).hexdigest()=='c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4'
rows=[json.loads(x) for x in a.source.read_text().splitlines()];assert len(rows)==200
out=[];prefixes=[]
for r in rows:
 q=r['question'][0];assert len(q)==1 and q[0]['role']=='user'
 full=q[0]['content'];w=list(re.finditer(r'\S+',full));assert len(w)>6
 item_id='BP1-'+r['id'];prefix=full[:w[5].end()]
 out.append({'item_id':item_id,'source_id':r['id'],'source_turn':0,'source_commit':'6ea57973c7a6097fd7c5915698c54c17c5b1b6c8','prefix':prefix,'full_instruction':full,'checkpoint_words':6,'source_word_count':len(w),'source_kind':'public_source_adaptation','candidate_origin':'pending_prefix_only_AI','family_group':r['id'],'family_group_limitation':'source conversation grouping only; template dependence across conversations not ruled out','future_dialogue_used':False,'initial_state_used':False,'reference_paths_used':False})
 for i,m in enumerate(w,1):prefixes.append({'item_id':item_id,'word_index':i,'prefix':full[:m.end()]})
def write(name,data):
 f=p/name
 if f.exists():raise RuntimeError('Refuse overwrite '+str(f))
 f.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data))
write('EVALUATOR_CONTEXT.jsonl',out);write('ALL_WORD_PREFIXES.jsonl',prefixes)
order=list(out);random.Random(260912200).shuffle(order)
for n in [1,2]:
 subset=order[n-1::2];mapping=[];blind=[]
 for i,r in enumerate(subset,1):
  bid=f'P{n}-{i:03d}';mapping.append({'blind_id':bid,'item_id':r['item_id']});blind.append({'item_id':bid,'prefix':r['prefix']})
 write(f'PROPOSER_{n}_INPUT.jsonl',blind);write(f'PROPOSER_{n}_MAPPING.jsonl',mapping)
shutil.copyfile(a.license,p/'SOURCE_LICENSE.txt')
(p/'SOURCE_MANIFEST.json').write_text(json.dumps({'source_url':'https://raw.githubusercontent.com/ShishirPatil/gorilla/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard/bfcl_eval/data/BFCL_v4_multi_turn_base.json','source_sha256':expected,'source_rows':len(rows),'license_url':'https://raw.githubusercontent.com/ShishirPatil/gorilla/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/LICENSE','license_sha256':hashlib.sha256(a.license.read_bytes()).hexdigest(),'license_record':'Pinned repository Apache-2.0 declaration; preserved notice, no new blanket license.','changes':'Only first user turn retained, literal six-word prefix derived; later dialogue, initial states, credentials in initial states, tool paths and references omitted. Prefix-only proposals and reuse labels are new AI annotations, not official BFCL labels.','copyright_notice':'Source: ShishirPatil/gorilla, Berkeley Function Calling Leaderboard; see preserved license and source URL.'},indent=2)+'\n')
print(f'Built {len(out)} contexts and {len(prefixes)} word-prefix observations')
