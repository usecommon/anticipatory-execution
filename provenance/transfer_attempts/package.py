from pathlib import Path
import zipfile,hashlib,json,re
base=Path.cwd();dest=base/'outputs/github_complete_release';records=[]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def package(name,items):
 rows=[]
 with zipfile.ZipFile(dest/name,'w',zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
  for p,rel in sorted(items,key=lambda x:x[1]):
   if p.suffix in ('.py','.json','.log','.txt','.md','.jsonl'):
    s=p.read_text(errors='ignore')
    for pat in [r'gh[pousr]_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{30,}',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----']:
     if re.search(pat,s):raise RuntimeError('Credential pattern in '+str(p))
   z.write(p,rel);rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
 rec={'asset':name,'bytes':(dest/name).stat().st_size,'sha256':sha(dest/name),'files':rows};records.append(rec);print(name,rec['bytes'],len(rows),flush=True)
for name in ['g0_evidence_v0_1','g0_rca_v0_2','g0_fix_v0_3','g0_closure_v0_5']:
 package(name+'_complete.zip',[(p,str(p.relative_to(base))) for p in (base/'outputs'/name).rglob('*') if p.is_file()])
package('original_work_and_handoff.zip',[(p,str(p.relative_to(base))) for p in (base/'work').rglob('*') if p.is_file() and '__pycache__' not in p.parts and 'github_complete' not in p.parts])
items=[(p,'outputs/'+p.name) for p in (base/'outputs').iterdir() if p.is_file()]
p=Path('/Users/jeffkim/Downloads/anticipatory_execution_codex_handoff_v0_1.zip')
if p.exists():items.append((p,'original_attachment/'+p.name))
package('original_deliverables_and_attachment.zip',items)
(dest/'ASSET_MANIFEST_BASE.json').write_text(json.dumps({'release':'research-state-2026-09-11','assets':records,'excluded':'Python caches and credential/runtime configuration are not research artifacts; repository itself is separately tracked in Git.'},indent=2))
