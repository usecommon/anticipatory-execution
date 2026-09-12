"""Preserve and check actual independent human exports. Never closes G1."""
import argparse,collections,hashlib,json,math,shutil
from pathlib import Path
P=Path(__file__).resolve().parent
REQUIRED={'artifact_sufficiency','sufficiency_rationale','binary_usefulness_0_or_1','fractional_utility_0_to_1','confidence_1_to_5','ambiguity_flag_Y_N','annotator_rationale'}
def validate_response(r):
 errors=[];missing=REQUIRED-set(r)
 if missing:return ['missing fields: '+','.join(sorted(missing))]
 s=r['artifact_sufficiency'];b=r['binary_usefulness_0_or_1'];f=r['fractional_utility_0_to_1'];c=r['confidence_1_to_5'];flag=r['ambiguity_flag_Y_N']
 if s not in ['substantive','no_material_work','uncertain']:errors.append('invalid sufficiency')
 if b is not None and not(type(b) is int and b in [0,1]):errors.append('invalid binary')
 if f is not None and not(type(f) in [int,float] and math.isfinite(f) and 0<=f<=1):errors.append('invalid fraction')
 if type(c) is not int or not 1<=c<=5:errors.append('invalid confidence')
 if flag not in ['Y','N']:errors.append('invalid ambiguity flag')
 for k in ['sufficiency_rationale','annotator_rationale']:
  if not isinstance(r[k],str) or not r[k].strip():errors.append('missing '+k)
 if s in ['no_material_work','uncertain'] and (b is not None or f is not None):errors.append('non-substantive work cannot have reuse/fraction label')
 if (s=='uncertain' or s=='substantive' and b is None) and flag!='Y':errors.append('uncertainty requires ambiguity Y')
 return errors

def disposition(r):
 s=r['artifact_sufficiency']
 return 'invalid_candidate' if s=='no_material_work' else 'uncertain_candidate' if s=='uncertain' else {1:'reusable',0:'non_reusable',None:'unresolved_reuse'}[r['binary_usefulness_0_or_1']]

def agreement(a,b,ids):
 pairs=[(a[k]['binary_usefulness_0_or_1'],b[k]['binary_usefulness_0_or_1']) for k in ids if a[k]['artifact_sufficiency']==b[k]['artifact_sufficiency']=='substantive' and a[k]['binary_usefulness_0_or_1'] is not None and b[k]['binary_usefulness_0_or_1'] is not None];n=len(pairs);same=sum(x==y for x,y in pairs);kappa=None
 ca=collections.Counter(x for x,y in pairs);cb=collections.Counter(y for x,y in pairs)
 if n:
  pe=sum(ca[z]*cb[z] for z in [0,1])/n**2
  if pe!=1:kappa=(same/n-pe)/(1-pe)
 return {'items':len(ids),'sufficiency_agreements':sum(a[k]['artifact_sufficiency']==b[k]['artifact_sufficiency'] for k in ids),'disposition_agreements':sum(disposition(a[k])==disposition(b[k]) for k in ids),'complete_binary_pairs':n,'outside_binary_denominator':len(ids)-n,'binary_agreements':same,'kappa':kappa,'A_binary_counts':dict(ca),'B_binary_counts':dict(cb),'nondegenerate_in_each_rater':all(ca[z]>0 and cb[z]>0 for z in [0,1])}

def collect(a_path,b_path,out):
 assert not out.exists(),'Refuse overwrite collection';out.mkdir(parents=True)
 # Preserve exact originals before any parsing or validation, including failed submissions.
 raw={};hashes={}
 for role,f in [('A',a_path),('B',b_path)]:
  dst=out/f'ORIGINAL_{role}.json';shutil.copyfile(f,dst);hashes[role]=hashlib.sha256(dst.read_bytes()).hexdigest();raw[role]=dst
 (out/'RAW_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n')
 errors=[];mapped={};submissions={};kinds={};package_manifest=json.loads((P/'PACKAGE_MANIFEST.json').read_text())
 for name,h in json.loads((P/'REVIEW_INPUT_FREEZE.json').read_text()).items():
  if hashlib.sha256((P/name).read_bytes()).hexdigest()!=h:errors.append('frozen review input changed: '+name)
 for role in ['A','B']:
  try:
   d=json.loads(raw[role].read_text());submissions[role]=d
   if d.get('package_id')!=package_manifest[role]['package_id'] or d.get('reviewer_role')!=package_manifest[role]['reviewer_role']:errors.append(role+': wrong package or role')
   if d.get('status')!='SUBMITTED_FOR_REVIEW':errors.append(role+': draft/not submitted')
   if not isinstance(d.get('human_identity'),str) or not d['human_identity'].strip():errors.append(role+': missing actual human identity/pseudonym')
   if d.get('independent_attestation') is not True or d.get('prior_ai_labels_seen') is not False:errors.append(role+': independence/exposure declaration not satisfied')
   mapping=[json.loads(x) for x in (P/f'ANNOTATOR_{role}_MAPPING.jsonl').read_text().splitlines()];mp={r['blind_id']:r for r in mapping};rs=d.get('responses')
   if not isinstance(rs,list) or len(rs)!=len(mp) or any(not isinstance(r,dict) for r in rs) or {r.get('item_id') for r in rs}!=set(mp):errors.append(role+': incomplete/duplicate/unknown item IDs');continue
   mapped[role]={}
   for r in rs:
    errs=validate_response(r)
    if errs:errors.append(role+': '+r['item_id']+': '+ '; '.join(errs))
    item=mp[r['item_id']];k=item['coordinator_item_id'];mapped[role][k]=r;kinds[k]=item['review_kind']
  except (ValueError,KeyError,TypeError,AttributeError) as e:errors.append(role+': malformed submission: '+str(e))
 if all(role in submissions for role in ['A','B']):
  aa=str(submissions['A'].get('human_identity','')).strip().casefold();bb=str(submissions['B'].get('human_identity','')).strip().casefold()
  if aa==bb:errors.append('Two distinct actual humans required; same/empty identity supplied')
 report={'G1':'PENDING','human_process_verified':False,'independence_evidence':'Self-attestations require coordinator review; software does not establish human identity or independence','errors':errors,'raw_hashes':hashes,'third_adjudication_received':False,'confirmatory_extraction':False}
 if not errors:
  ids=[k for k,v in kinds.items() if v=='main'];boundary=[k for k,v in kinds.items() if v=='boundary'];stats=agreement(mapped['A'],mapped['B'],ids)
  secondary_complete=all(mapped[role][k]['fractional_utility_0_to_1'] is not None for role in ['A','B'] for k in ids)
  report.update(validation='VALIDATED_EXPORTS_PROCESS_PENDING',main_agreement=stats,boundary_diagnostics={role:dict(collections.Counter(disposition(mapped[role][k]) for k in boundary)) for role in ['A','B']},boundary_items=len(boundary),main_secondary_fraction_fields_complete=secondary_complete,numerical_criterion_only_met=len(ids)==200 and stats['complete_binary_pairs']==200 and stats['nondegenerate_in_each_rater'] and stats['kappa'] is not None and stats['kappa']>=.70 and secondary_complete)
  attention=[{'coordinator_item_id':k,'review_kind':kinds[k],'A':mapped['A'][k],'B':mapped['B'][k],'adjudicated_sufficiency':None,'adjudicated_binary':None,'adjudication_reason':None} for k in kinds if disposition(mapped['A'][k])!=disposition(mapped['B'][k]) or mapped['A'][k]['ambiguity_flag_Y_N']=='Y' or mapped['B'][k]['ambiguity_flag_Y_N']=='Y']
  (out/'ADJUDICATION_PENDING.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in attention))
 else:report['validation']='REJECTED_OR_INCOMPLETE_PRESERVED'
 (out/'COLLECTION_REPORT.json').write_text(json.dumps(report,indent=2)+'\n');return report

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--a',type=Path,required=True);ap.add_argument('--b',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();report=collect(args.a,args.b,args.out);print(json.dumps(report,indent=2))
