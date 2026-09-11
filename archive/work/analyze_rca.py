import json,hashlib,tarfile,collections
from pathlib import Path
root=Path('outputs/g0_rca_v0_2')
with tarfile.open(root/'rca_run_01.tar.gz') as t:t.extractall(root,filter='data')
run=next(p for p in root.glob('rca_*') if p.is_dir())
manifest=json.loads((run/'sha256.json').read_text());valid={k:hashlib.sha256((run/k).read_bytes()).hexdigest()==v for k,v in manifest.items()}
assert all(valid.values());(root/'download_verification.json').write_text(json.dumps(valid,indent=2))
allrows=[];summary={}
for case in ['baseline','workspace_strict','bf16_eager','bf16_math','bf16_no_reduced','fp32_eager']:
 p=run/case
 if not (p/'checks.json').exists():summary[case]={'error':(p/'failure.txt').read_text() if (p/'failure.txt').exists() else 'not completed'};continue
 rows=json.loads((p/'checks.json').read_text());groups={}
 for family in ['length_','batch_','cache_','repeat_','masked_content_','isolated_']:
  r=[x for x in rows if x['name'].startswith(family)]
  groups[family]={'count':len(r),'fail':sum(x['status']=='FAIL' for x in r),'max_abs':max((x['max_abs'] for x in r),default=None),'max_relative_l2':max((x['relative_l2'] for x in r),default=None)}
 groups['first_nonzero_length0']=next((x for x in rows if x['name'].startswith('localize_length_0_') and x['unequal_elements']),None)
 groups['first_nonzero_batch0']=next((x for x in rows if x['name'].startswith('localize_batch_0_') and x['unequal_elements']),None)
 groups['isolated_projection']=[x for x in rows if x['name'].startswith('isolated_')]
 groups['complete']=(p/'summary.json').exists()
 summary[case]=groups
 allrows += [dict(case=case,**x) for x in rows]
(root/'comparison_summary.json').write_text(json.dumps(summary,indent=2));(root/'all_comparisons.json').write_text(json.dumps(allrows,indent=2))
print(json.dumps(summary,indent=2))
