"""Validate and freeze two AI submissions; build all-item judge input without author labels."""
import argparse,hashlib,json,random,shutil
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--submissions',type=Path,required=True);args=parser.parse_args()
p=Path(__file__).resolve().parent;out=p/'review';out.mkdir(exist_ok=True)
def read(f):return [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
def write(f,r):f.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in r))
def validate(r,ids):
 assert len(r)==len(ids) and {x['item_id'] for x in r}==ids and len({x['item_id'] for x in r})==len(r)
 for x in r:
  assert x['binary_usefulness_0_or_1'] is None or type(x['binary_usefulness_0_or_1']) is int and x['binary_usefulness_0_or_1'] in [0,1]
  assert x['fractional_utility_0_to_1'] is None or type(x['fractional_utility_0_to_1']) in [float,int] and 0<=x['fractional_utility_0_to_1']<=1
  assert type(x['confidence_1_to_5']) is int and 1<=x['confidence_1_to_5']<=5
  assert x['ambiguity_flag_Y_N'] in ['Y','N'] and x['annotator_rationale'].strip()
rows=read(p/'dataset/ITEMS.jsonl');ratings={};hashes={}
for role in ['A','B']:
 raw=args.submissions/f'RATER_{role}.jsonl';frozen=out/raw.name
 if frozen.exists():raise SystemExit('Refusing to overwrite frozen submissions')
 mapping={r['blind_id']:r['item_id'] for r in read(p/f'dataset/RATER_{role}_MAPPING.jsonl')};r=read(raw);validate(r,set(mapping));shutil.copy2(raw,frozen);hashes[raw.name]=hashlib.sha256(frozen.read_bytes()).hexdigest();ratings[role]={mapping[x['item_id']]:{**x,'original_blind_id':x['item_id'],'item_id':mapping[x['item_id']]} for x in r};write(out/f'RATER_{role}_MAPPED.jsonl',list(ratings[role].values()))
 notes=args.submissions/f'RATER_{role}_NOTES.md'
 if notes.exists():shutil.copy2(notes,out/notes.name)
(out/'RATER_FREEZE.json').write_text(json.dumps(hashes,indent=2)+'\n')
order=list(rows);random.Random(2609123).shuffle(order);judge=[];mapping=[]
for i,r in enumerate(order,1):
 jid=f'J{i:03d}';mapping.append({'judge_id':jid,'item_id':r['item_id']});judge.append({'item_id':jid,**{k:r[k] for k in ['prefix','candidate_action','execution_class','work_product','full_instruction','fixture_contract']},'ratings':{k:{f:v for f,v in ratings[k][r['item_id']].items() if f not in ['item_id','original_blind_id']} for k in ['A','B']}})
write(out/'JUDGE_INPUT.jsonl',judge);write(out/'JUDGE_MAPPING.jsonl',mapping)
(out/'JUDGE_INPUT_HASH.json').write_text(json.dumps({'sha256':hashlib.sha256((out/'JUDGE_INPUT.jsonl').read_bytes()).hexdigest(),'items':len(judge),'author_expectations_included':False},indent=2)+'\n');print('Validated and froze A/B; all 200 items prepared for adjudication.')
