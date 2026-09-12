import argparse,hashlib,json,random,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--submissions',type=Path,required=True);a=ap.parse_args()
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
def valid(r):
 b=r['binary_usefulness_0_or_1'];f=r['fractional_utility_0_to_1'];c=r['confidence_1_to_5']
 assert b is None or type(b) is int and b in [0,1]
 assert f is None or type(f) in [int,float] and 0<=f<=1
 assert type(c) is int and 1<=c<=5 and r['ambiguity_flag_Y_N'] in ['Y','N'] and r['annotator_rationale'].strip()
 if b is None:assert r['ambiguity_flag_Y_N']=='Y'
for f,h in json.loads((p/'REVIEW_INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
ratings={};hashes={}
for n in ['A','B']:
 f=a.submissions/f'bfcl_rater_{n}.jsonl';rs=read(f);mp={r['blind_id']:r['item_id'] for r in read(p/f'RATER_{n}_MAPPING.jsonl')}
 assert len(rs)==len(mp) and {r['item_id'] for r in rs}==set(mp)
 ratings[n]={}
 for r in rs:valid(r);k=mp[r['item_id']];ratings[n][k]={**r,'item_id':k,'blind_id':r['item_id']}
 assert not (p/f.name).exists();shutil.copyfile(f,p/f.name);hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
(p/'RATINGS_FREEZE.json').write_text(json.dumps(hashes,indent=2)+'\n')
items=read(p/'PROPOSED_ITEMS.jsonl');random.Random(81203).shuffle(items);out=[];mp=[]
for i,r in enumerate(items,1):
 bid=f'J{i:03d}';mp.append({'blind_id':bid,'item_id':r['item_id']});rr={}
 for n in ['A','B']:rr[n]={k:v for k,v in ratings[n][r['item_id']].items() if k not in ['item_id','blind_id']}
 out.append({'item_id':bid,**{k:r[k] for k in ['prefix','candidate_action','execution_class','work_product','full_instruction','fixture_contract']},'rater_A':rr['A'],'rater_B':rr['B']})
for name,rows in [('JUDGE_INPUT.jsonl',out),('JUDGE_MAPPING.jsonl',mp)]:
 f=p/name;assert not f.exists();f.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
(p/'JUDGE_INPUT_FREEZE.json').write_text(json.dumps({n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ['JUDGE_INPUT.jsonl','JUDGE_MAPPING.jsonl']},indent=2)+'\n');print('Prepared',len(out),'adjudications')
