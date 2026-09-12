import argparse,hashlib,json,random,shutil
from common import P as p,read,mapped
ap=argparse.ArgumentParser();ap.add_argument('--submissions',required=True);a=ap.parse_args()
from pathlib import Path
for f,h in json.loads((p/'REVIEW_FREEZE.json').read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
ratings={};hashes={}
for n in ['A','B']:
 f=Path(a.submissions)/f'shared_rater_{n}.jsonl';ratings[n]=mapped(f,p/f'RATER_{n}_MAPPING.jsonl');assert not (p/f.name).exists();shutil.copyfile(f,p/f.name);hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
(p/'RATINGS_FREEZE.json').write_text(json.dumps(hashes,indent=2)+'\n')
rows=read(p/'PROPOSED_ITEMS.jsonl');random.Random(260912305).shuffle(rows);out=[];mp=[]
for i,r in enumerate(rows,1):
 bid=f'J{i:03d}';mp.append({'blind_id':bid,'item_id':r['item_id']});out.append({'item_id':bid,**{k:r[k] for k in ['prefix','candidate_action','work_product','execution_class','full_instruction','fixture_contract']},**{f'rater_{n}':{k:v for k,v in ratings[n][r['item_id']].items() if k not in ['item_id','blind_id']} for n in ['A','B']}})
for name,rs in [('JUDGE_INPUT.jsonl',out),('JUDGE_MAPPING.jsonl',mp)]:
 f=p/name;assert not f.exists();f.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rs))
(p/'JUDGE_FREEZE.json').write_text(json.dumps({f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in ['JUDGE_INPUT.jsonl','JUDGE_MAPPING.jsonl']},indent=2)+'\n');print('Adjudication items',len(out))
