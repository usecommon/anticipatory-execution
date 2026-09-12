"""Read-only recomputation from archived AI ratings; run with Python 3 stdlib."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib,json
root=Path(__file__).resolve().parent
ratings={}
for role in 'ABC':
    rows=[json.loads(l) for l in (root/f'RATER_{role}.jsonl').read_text().splitlines()]
    ratings[role]={r['item_id']:r['binary_usefulness_0_or_1'] for r in rows}
    assert len(rows)==len(ratings[role])==200
    assert all(type(x) is int and x in (0,1) for x in ratings[role].values())
assert set(ratings['A'])==set(ratings['B'])==set(ratings['C'])
saved=json.loads((root/'AGREEMENT_SUMMARY.json').read_text())
result={}
for a,b in [('A','B'),('A','C'),('B','C')]:
    c=Counter((ratings[a][k],ratings[b][k]) for k in ratings[a]);n=200
    po=Fraction(c[0,0]+c[1,1],n)
    pa=Fraction(sum(ratings[a].values()),n);pb=Fraction(sum(ratings[b].values()),n)
    pe=pa*pb+(1-pa)*(1-pb);kappa=float((po-pe)/(1-pe))
    assert abs(kappa-saved['pairwise'][a+b]['kappa'])<1e-12
    result[a+b]={'kappa':kappa,'agreement':float(po)}
votes=[sum(ratings[r][k] for r in 'ABC') for k in ratings['A']]
p=Fraction(sum(votes),600);pe=p*p+(1-p)*(1-p)
po=sum(Fraction(n*(n-1)+(3-n)*(2-n),6) for n in votes)/200
fleiss=float((po-pe)/(1-pe));assert abs(fleiss-saved['fleiss_kappa'])<1e-12
manifest=json.loads((root/'FREEZE_MANIFEST.json').read_text())
for role,files in manifest['files'].items():
    for name,digest in files.items():
        assert hashlib.sha256((root/'frozen_submissions'/role/name).read_bytes()).hexdigest()==digest
print(json.dumps({'verification':'PASS','pairwise':result,'fleiss_kappa':fleiss,'G1':'PENDING'},indent=2))
