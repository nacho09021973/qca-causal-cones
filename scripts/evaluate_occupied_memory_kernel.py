"""Finite-delay infinite-lattice force correlations, not a pole estimate.

Run from repo root: python scripts/evaluate_occupied_memory_kernel.py
Outputs retain complex matrices as [real,imag] pairs.
"""
import json
from pathlib import Path
import numpy as np

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.diag([1,-1]); eye=np.eye(4)
ps=[sx,sy,sz]
W=np.kron(np.eye(2),np.diag(np.exp(-1j*np.pi/4*np.array([1,-1]))))

def generators(a):
    b=np.sqrt(1-a*a)
    return [np.kron(p,T) for p,T in zip(ps,[b*sx+a*sz,b*sy+a*sz,-b*sx+a*sz])]

def evaluate(L, max_delay=8):
    assert L > 2*max_delay
    qs=np.meshgrid(*([2*np.pi*np.arange(L)/L]*3),indexing='ij')
    symbols=[]
    for a in [1/3,2/3]:
        U=np.broadcast_to(W,(L,L,L,4,4)).copy()
        for q,G in zip(qs,generators(a)):
            U=U@(np.cos(q)[...,None,None]*eye-1j*np.sin(q)[...,None,None]*G)
        symbols.append(U)
    powers=[np.broadcast_to(eye,U.shape).copy() for U in symbols]
    coords=np.meshgrid(*([np.fft.fftfreq(L)*L]*3),indexing='ij')
    rows=[]
    for r in range(1,max_delay+1):
        props=[]
        for a in range(2):
            powers[a]=powers[a]@symbols[a]
            prop=np.fft.ifftn(powers[a],axes=(0,1,2))
            assert abs(np.sum(abs(prop)**2)-4)<1e-10
            props.append(prop)
        for a in range(2):
            density=np.sum(abs(props[1-a])**2,axis=(-2,-1))/4
            product=props[a]*density[...,None,None]
            F=np.sum(product,axis=(0,1,2))
            dq=[np.sum(-1j*x[...,None,None]*product,axis=(0,1,2)) for x in coords]
            # Independent r=1 evaluation from eight ordered projector coefficients.
            if r==1:
                import itertools
                direct=np.zeros((4,4),complex)
                for h in itertools.product([-1,1],repeat=3):
                    coeff=[]
                    for aa in [1/3,2/3]:
                        A=W.copy()
                        for sign,G in zip(h,generators(aa)):
                            A=A@(eye+sign*G)/2
                        coeff.append(A)
                    direct+=coeff[a]*np.sum(abs(coeff[1-a])**2)/4
                assert np.max(abs(F-direct))<1e-12
            # Response matrix convention L c_j=sum_i U_ji c_i.
            # Transposing the abstract coefficient map gives -F_r(q) U_a(q).
            K=-F@W
            dK=[-(d@W+F@(-1j*W@G)) / np.sqrt(3)
                for G,d in zip(generators([1/3,2/3][a]),dq)]
            rows.append(dict(r=r,species=a+1,F=F,K=K,dK_dk=np.array(dK),
                             density_return=float(density[0,0,0]),
                             F_norm=float(np.linalg.norm(F))))
    return rows

def encode(value):
    if isinstance(value,np.ndarray):
        return np.stack([value.real,value.imag],axis=-1).tolist()
    raise TypeError(type(value).__name__)

if __name__=='__main__':
    rows=evaluate(24)
    other=evaluate(20)
    error=max(float(np.max(abs(row[key]-alt[key])))
              for row,alt in zip(rows,other) for key in ['F','K','dK_dk'])
    assert error<1e-11
    out=Path('reports/2026-11-06--occupied-memory-kernel.json')
    out.write_text(json.dumps(dict(parameters=dict(a=[1/3,2/3],p=[.5,.5],
        theta=float(np.pi/4),max_delay=8,grids=[24,20]),
        cross_grid_max_error=error,rows=rows),default=encode,indent=2)+'\n')
    print('Cross-grid maximum absolute difference:',error)
    for row in rows:
        print('r=%d species=%d ||F||=%.12g density_return=%.12g'%(
            row['r'],row['species'],row['F_norm'],row['density_return']))
    print('PASS: propagator normalization, direct first lag, two alias-free grids.')
    print('No memory-tail bound or long-time pole inferred.')
