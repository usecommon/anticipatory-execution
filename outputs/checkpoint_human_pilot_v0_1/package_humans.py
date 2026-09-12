import hashlib,json,random,shutil,zipfile
from pathlib import Path
p=Path(__file__).resolve().parent
read=lambda f:[json.loads(x) for x in f.read_text().splitlines()]
main=read(p/'SELECTED_MAIN.jsonl');controls=read(p/'BOUNDARY_CONTROLS.jsonl');allrows=[{**r,'review_kind':'main'} for r in main]+[{**r,'review_kind':'boundary'} for r in controls]
root=p/'human_packages';assert not root.exists();root.mkdir();manifest={}
for role,seed in [('A',260913201),('B',260913202)]:
 out=root/f'Annotator_{role}';out.mkdir();order=list(allrows);random.Random(seed).shuffle(order);items=[];mapping=[]
 for i,r in enumerate(order,1):
  bid=f'{role}{i:03d}';items.append({'item_id':bid,**{k:r[k] for k in ['prefix','candidate_action','work_product','execution_class','full_instruction']},'fixture_contract':'Local authored preparation. No displayed command or tool output has been executed or verified. Do not infer unmentioned environment facts.'});mapping.append({'blind_id':bid,'coordinator_item_id':r['item_id'],'review_kind':r['review_kind'],'source':r['source'],'task_id':r['task_id'],'checkpoint_words':r['checkpoint_words']})
 canonical=json.dumps(items,ensure_ascii=False,sort_keys=True,separators=(',',':'));package_id='CPH1-'+role+'-'+hashlib.sha256(canonical.encode()).hexdigest()[:20];payload={'package_id':package_id,'reviewer_role':'Annotator_'+role,'items':items}
 (out/'ITEMS.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 safe=json.dumps(payload,ensure_ascii=False).replace('&','\\u0026').replace('<','\\u003c').replace('>','\\u003e');(out/'REVIEW.html').write_text((p/'review_template.html').read_text().replace('__PAYLOAD__',safe));shutil.copyfile(p/'ORIGINAL_RUBRIC.txt',out/'ORIGINAL_RUBRIC.txt')
 (out/'START_HERE.md').write_text(f'''# Independent reviewer {role}

Open REVIEW.html in a browser. This package contains {len(items)} cases. Work alone, read the on-page clarification and original rubric, then label the actual artifact against the completed instruction. Do not rewrite instructions, repair artifacts, execute commands or use external information. All displayed work is unexecuted authored preparation.

Do not inspect any other reviewer’s answers, old AI judgments, or the research repository. Use only your assigned package. Some work may be insufficient to constitute a meaningful work unit; judge this before survival. No material work is not a negative reuse label. Missing facts remain unresolved. The fractions concern artifact content, not probability or elapsed time.

Enter your human reviewer name or stable pseudonym. Check independence and prior-label-exposure statements only if true; contact the coordinator if you have seen labels. Save drafts by exporting JSON regularly. Browser-local storage is only a convenience and may be unavailable. Load your exported JSON to resume, in this same role’s package.

A final export is marked SUBMITTED_FOR_REVIEW only when every case is filled and the attestations are checked; that is not validation or a research-gate pass. Return your JSON to the coordinator privately. There is no automatic upload or messaging. Do not exchange labels or discuss disagreements until both original submissions are frozen. A separate adjudicator will review disagreements afterward.

Package ID: {package_id}
''')
 (p/f'ANNOTATOR_{role}_MAPPING.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in mapping));manifest[role]={'package_id':package_id,'reviewer_role':'Annotator_'+role,'items':len(items),'main_items':len(main),'boundary_items':len(controls),'files':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(out.iterdir())}}
 z=root/f'Annotator_{role}.zip'
 with zipfile.ZipFile(z,'w',compression=zipfile.ZIP_DEFLATED) as archive:
  for f in sorted(out.iterdir()):
   info=zipfile.ZipInfo(f'Annotator_{role}/{f.name}',date_time=(2026,9,12,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;archive.writestr(info,f.read_bytes())
 manifest[role]['zip_sha256']=hashlib.sha256(z.read_bytes()).hexdigest()
(p/'PACKAGE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(p/'REVIEW_INPUT_FREEZE.json').write_text(json.dumps({str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.rglob('*')) if f.is_file() and ('human_packages' in f.parts or f.name in ['SELECTED_MAIN.jsonl','BOUNDARY_CONTROLS.jsonl','ANNOTATOR_A_MAPPING.jsonl','ANNOTATOR_B_MAPPING.jsonl','PACKAGE_MANIFEST.json','review_template.html'])},indent=2)+'\n');print('Prepared two blind packages:',len(items),'items each; no human labels generated')
