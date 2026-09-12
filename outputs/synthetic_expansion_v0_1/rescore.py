"""Rescore frozen AI labels. Agreement is not predictive efficacy or human G1."""
import argparse,collections,hashlib,json,shutil
from pathlib import Path
p=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--judge',type=Path,required=True);args=parser.parse_args();out=p/'results'
if out.exists() and any(out.iterdir()):raise SystemExit('Refusing to overwrite prior results')
def read(f):return [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
def write(f,r):f.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in r))
for name,digest in json.loads((p/'INPUT_FREEZE.json').read_text()).items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==digest, name
for name,digest in json.loads((p/'review/RATER_FREEZE.json').read_text()).items():assert hashlib.sha256((p/'review'/name).read_bytes()).hexdigest()==digest,name
raw=read(args.judge);mapping={x['judge_id']:x['item_id'] for x in read(p/'review/JUDGE_MAPPING.jsonl')};assert len(raw)==200 and len({x['item_id'] for x in raw})==200 and {x['item_id'] for x in raw}==set(mapping)
for x in raw:
 assert x['binary_usefulness_0_or_1'] is None or type(x['binary_usefulness_0_or_1']) is int and x['binary_usefulness_0_or_1'] in [0,1]
 assert x['fractional_utility_0_to_1'] is None or type(x['fractional_utility_0_to_1']) in [int,float] and 0<=x['fractional_utility_0_to_1']<=1
 assert type(x['confidence_1_to_5']) is int and 1<=x['confidence_1_to_5']<=5
 assert x['ambiguity_flag_Y_N'] in ['Y','N'] and x['annotator_rationale'].strip() and x['decision_reason'].strip()
out.mkdir(parents=True,exist_ok=True);shutil.copy2(args.judge,out/'JUDGE_RAW.jsonl')
notes=args.judge.with_name('JUDGE_NOTES.md')
if notes.exists():shutil.copy2(notes,out/notes.name)
items=read(p/'dataset/ITEMS.jsonl');d={k:{x['item_id']:x for x in read(p/f'review/RATER_{k}_MAPPED.jsonl')} for k in ['A','B']};d['judge']={mapping[x['item_id']]:{**x,'item_id':mapping[x['item_id']],'judge_blind_id':x['item_id']} for x in raw};expect={x['item_id']:x for x in read(p/'dataset/AUTHOR_EXPECTATIONS.jsonl')}
def counts(records):
 c=collections.Counter(x['binary_usefulness_0_or_1'] for x in records);return {'reusable':c[1],'non_reusable':c[0],'unresolved':c[None],'ambiguity_flags':sum(x.get('ambiguity_flag_Y_N')=='Y' for x in records)}
def agreement(left,right):
 pairs=[(left[k]['binary_usefulness_0_or_1'],right[k]['binary_usefulness_0_or_1']) for k in left];complete=[x for x in pairs if None not in x];n=len(complete)
 if not n:return {'total':len(pairs),'complete_binary_pairs':0,'kappa':None}
 po=sum(x==y for x,y in complete)/n;px=sum(x for x,y in complete)/n;py=sum(y for x,y in complete)/n;pe=px*py+(1-px)*(1-py)
 return {'total':len(pairs),'complete_binary_pairs':n,'unresolved_pairs':len(pairs)-n,'binary_agreements':sum(x==y for x,y in complete),'binary_disagreements':sum(x!=y for x,y in complete),'observed_agreement':po,'kappa':None if pe==1 else (po-pe)/(1-pe),'degenerate_kappa':pe==1,'denominator_policy':'Only pairs with two binary labels; unresolved count retained explicitly.'}
joined=[];attention=[];changed=[]
for r in items:
 k=r['item_id'];j=d['judge'][k];rr={**r,'author_expectation':expect[k]['binary_usefulness_0_or_1'],'rater_A':d['A'][k],'rater_B':d['B'][k],'adjudication':j,'label_status':'AI_provisional_not_human_gold'};joined.append(rr)
 if j['binary_usefulness_0_or_1']!=expect[k]['binary_usefulness_0_or_1']:changed.append(rr)
 if j['binary_usefulness_0_or_1'] is None or j['ambiguity_flag_Y_N']=='Y' or d['A'][k]['binary_usefulness_0_or_1']!=d['B'][k]['binary_usefulness_0_or_1']:attention.append(rr)
write(out/'JUDGED_ITEMS.jsonl',joined);write(out/'CHANGED_FROM_AUTHOR_EXPECTATIONS.jsonl',changed);write(out/'REVIEW_ATTENTION.jsonl',attention)
bydomain={domain:counts([d['judge'][r['item_id']] for r in items if r['domain']==domain]) for domain in sorted({r['domain'] for r in items})}
status={'state':'SYNTHETIC_DEVELOPMENT_AI_REVIEW_ONLY','items':200,'tasks':100,'families':50,'word_observations':1677,'source_pool_owner_accepted_items':125,'style_anchors_used':50,'old_owner_labels_changed':0,'author_expectations':counts(list(expect.values())),'rater_A':counts(list(d['A'].values())),'rater_B':counts(list(d['B'].values())),'judge':counts(list(d['judge'].values())),'rater_agreement':agreement(d['A'],d['B']),'author_vs_judge_consistency':agreement(expect,d['judge']),'changed_or_unresolved_from_author':len(changed),'review_attention_items':len(attention),'by_domain':bydomain,'G0':'PASS_SCOPED_UNCHANGED','G1':'PENDING','independent_human_pairs':0,'model_inference':False,'development_extraction':False,'confirmatory_extraction':False,'public_release_status':'PRIVATE_REPO_ONLY_NOT_PUBLICLY_RELEASED','scientific_predictive_accuracy_measured':False,'judge_raw_sha256':hashlib.sha256(args.judge.read_bytes()).hexdigest()}
(out/'SCORES.json').write_text(json.dumps(status,indent=2)+'\n')
def label(v):return 'unresolved' if v is None else 'reusable' if v else 'non-reusable'
text=['# All 200 synthetic items and adjudicated labels','', 'AI-provisional judgments on fictional, unexecuted artifacts. This is not human gold or evidence of predictive efficacy. Original owner labels are unchanged.','']
for r in joined:
 j=r['adjudication'];text.extend([f"## {r['item_id']}",'',f"**{r['domain']} · {label(j['binary_usefulness_0_or_1'])} · fraction {j['fractional_utility_0_to_1']} · confidence {j['confidence_1_to_5']}/5 · ambiguity {j['ambiguity_flag_Y_N']}" ,'',f"**Observed prefix:** {r['prefix']}",'',f"**Candidate:** {r['candidate_action']}",'','**Concrete work product:**','', '```text',r['work_product'],'```','',f"**Full instruction:** {r['full_instruction']}",'',f"**Judge:** {j['annotator_rationale']}",'',f"**Author expectation / rater A / rater B:** {label(r['author_expectation'])} / {label(r['rater_A']['binary_usefulness_0_or_1'])} / {label(r['rater_B']['binary_usefulness_0_or_1'])}",''])
(out/'ALL_ITEMS_REVIEW.md').write_text('\n'.join(text))
print(json.dumps({k:v for k,v in status.items() if k!='by_domain'},indent=2))
