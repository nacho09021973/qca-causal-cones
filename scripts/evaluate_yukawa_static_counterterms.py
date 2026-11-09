"""Static one-loop candidate counterterms, not a critical-surface proof."""
import json
from pathlib import Path
import numpy as np
import sympy as s
w,d,m=s.symbols('w d m',positive=True)
E=s.sqrt(d+(w+m)**2)
assert s.simplify(E.diff(m).subs(m,0)-w/s.sqrt(d+w*w))==0
assert s.simplify(E.diff(m,2).subs(m,0)-d/(d+w*w)**s.Rational(3,2))==0
rows=[]
for L in [24,48,96]:
    q=np.meshgrid(*([2*np.pi*(np.arange(L)+.5)/L]*3),indexing='ij')
    W=sum(1-np.cos(t) for t in q); S=sum(np.sin(t)**2 for t in q)
    omega=np.sqrt(2*W)
    species=[]
    for v in [1/3,2/3]:
        e=np.sqrt(v*v*S+W*W)
        species.append(dict(v=v,tadpole_counterterm_per_y=float(2*np.mean(W/e)),
                            mass2_counterterm_per_y2=float(2*np.mean(v*v*S/e**3))))
    rows.append(dict(L=L,species=species,
        scalar_mass2_counterterm_per_lambda=float(-np.mean(1/omega)/4)))
Path('reports/2026-11-06--yukawa-static-counterterms.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows: print(json.dumps(row))
print('PASS: exact first/second mass derivatives; numerical midpoint grids only.')
print('No rigorous quadrature error, fermion mass tuning, or full critical surface.')
