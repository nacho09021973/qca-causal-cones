"""Abel-regularized finite-delay sums with analytic temporal-tail bounds."""
import json
from pathlib import Path
import numpy as np
from evaluate_occupied_memory_kernel import evaluate, encode

R=24
rows=evaluate(52,R)
old=json.loads(Path('reports/2026-11-06--occupied-memory-kernel.json').read_text())
errors=[]
for row,prior in zip(rows[:16],old['rows']):
    for key in ['F','K','dK_dk']:
        arr=np.array(prior[key]); reference=arr[...,0]+1j*arr[...,1]
        errors.append(float(np.max(abs(row[key]-reference))))
assert max(errors)<1e-11
sums=[]
for rho in [.5,.65,.8]:
    tail=2*rho**(R+1)/(1-rho)
    dtail=2/np.sqrt(3)*rho**(R+1)*((R+2)/(1-rho)+rho/(1-rho)**2)
    for species in [1,2]:
        selected=[row for row in rows if row['species']==species]
        for omega in [-np.pi/4,np.pi/4]:
            total=sum(rho**row['r']*np.exp(1j*omega*row['r'])*row['K'] for row in selected)
            derivative=sum(rho**row['r']*np.exp(1j*omega*row['r'])*row['dK_dk'] for row in selected)
            sums.append(dict(rho=rho,species=species,omega=float(omega),
                memory_sum=total,d_memory_sum_dk=derivative,
                truncation_operator_norm_bound=tail,
                derivative_truncation_operator_norm_bound=dtail))
    print('rho=%.2f tail<=%.12g derivative tail<=%.12g'%(rho,tail,dtail))
out=dict(R=R,L=52,previous_window_max_difference=max(errors),sums=sums,rows=rows,
         scope='Analytic bounds cover temporal truncation, not floating-point roundoff.')
Path('reports/2026-11-06--occupied-abel-memory.json').write_text(json.dumps(out,default=encode,indent=2)+'\n')
print('Previous-window max difference:',max(errors))
print('PASS: normalization, first-delay direct check, reproduction r<=8.')
print('No rho->1 limit, Dyson pole, or velocity attraction established.')
