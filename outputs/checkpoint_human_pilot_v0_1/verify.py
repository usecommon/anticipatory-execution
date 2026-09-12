"""Offline integrity checks. Does not generate or certify human labels."""
import ast,collections,hashlib,json,re,zipfile
from pathlib import Path
p=Path(__file__).resolve().parent
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
for inv in ['INPUT_FREEZE.json','PROPOSAL_FREEZE.json','REVIEW_INPUT_FREEZE.json','HASHES.json']:
 for f,h in json.loads((p/inv).read_text()).items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,(inv,f)
for f,h in json.loads((p/'SOURCE_HASHES.json').read_text()).items():assert hashlib.sha256((p.parent/f).read_bytes()).hexdigest()==h
rows=read(p/'ALL_CHECKPOINTS.jsonl');assert len(rows)==len({r['item_id'] for r in rows})==900
for r in rows:
 words=list(re.finditer(r'\S+',r['full_instruction']));k=r['checkpoint_words'];expected='eligible' if len(words)>k else 'complete_at_checkpoint' if len(words)==k else 'checkpoint_not_reached';assert r['checkpoint_status']==expected
 if expected=='eligible':assert r['prefix']==r['full_instruction'][:words[k-1].end()] and r['proposal_status'] in ['proposed','abstain']
 else:assert r['proposal_status']=='not_eligible' and r['candidate_action'] is None and r['work_product'] is None
pool=read(p/'REVIEW_POOL.jsonl');assert {r['item_id'] for r in pool}=={r['item_id'] for r in rows if r['proposal_status']=='proposed'} and len(pool)==260
main=read(p/'SELECTED_MAIN.jsonl');controls=read(p/'BOUNDARY_CONTROLS.jsonl');assert len(main)==200 and len(controls)==20
assert collections.Counter(r['source'] for r in main)=={'public_bfcl':100,'synthetic':100}
joined={r['item_id']:r for r in main+controls};role_sets=[]
for role in ['A','B']:
 folder=p/'human_packages'/f'Annotator_{role}';package=json.loads((folder/'ITEMS.json').read_text());mp={r['blind_id']:r['coordinator_item_id'] for r in read(p/f'ANNOTATOR_{role}_MAPPING.jsonl')};items=package['items'];assert len(items)==len(mp)==220 and {r['item_id'] for r in items}==set(mp)
 for r in items:
  assert set(r)=={'item_id','prefix','candidate_action','work_product','execution_class','full_instruction','fixture_contract'};source=joined[mp[r['item_id']]]
  for k in ['prefix','candidate_action','work_product','execution_class','full_instruction']:assert r[k]==source[k]
 role_sets.append(set(mp.values()))
 html=(folder/'REVIEW.html').read_text();payload=json.loads(re.search(r'<script id="payload" type="application/json">(.*?)</script>',html,re.S).group(1));assert payload==package and '__PAYLOAD__' not in html
 assert not re.search(r'<script[^>]+src=',html,re.I)
 with zipfile.ZipFile(p/'human_packages'/f'Annotator_{role}.zip') as z:
  assert {Path(x).name for x in z.namelist()}=={'REVIEW.html','ITEMS.json','ORIGINAL_RUBRIC.txt','START_HERE.md'} and len(z.namelist())==4
  for name in z.namelist():assert z.read(name)==(folder/Path(name).name).read_bytes()
assert role_sets[0]==role_sets[1]==set(joined)
status=json.loads((p/'STATUS.json').read_text());assert status['human_submissions_received']==0 and status['G1']=='PENDING' and status['new_reuse_labels']==0
for f in p.glob('*.py'):ast.parse(f.read_text())
print('PASS frozen hashes,900opportunity inventory,260pool,200main+20boundary,symmetric blind packages,ZIP allowlists,no generated human labels,source syntax')
