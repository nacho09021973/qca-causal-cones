#!/usr/bin/env python3
"""Exact unbounded-lattice ray checks for the arbitrary-time recovery proof.

Selected times validate formulas, not a search or proof by extrapolation.
Gaussian-integer numerators have common denominator 25**T.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"reports/2026-11-08--thirring-exact-recovery"
TIMES=(1,2,3,4,6,8,12)
CHECKS=[]


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def normsq(a): return a[0]*a[0]+a[1]*a[1]
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def parity(x): return 1 if x%2==0 else -1


def check(name,value,tol=2e-12):
    error=float(value)
    CHECKS.append(dict(name=name,error=error,passed=bool(np.isfinite(error) and error<tol)))


def exact(name,condition): check(name,0 if condition else 1)


def contact(v):
    return {xy:mul((0,1),a) if xy[0]==xy[1] else a for xy,a in v.items()}


def free(v,s):
    out={}
    for (x,y),a in v.items():
        px=x+s*parity(x)
        py=y-s*parity(y)
        for xy,c in (((px,py),(16,0)),((px,y),(0,-12)),((x,py),(0,-12)),((x,y),(-9,0))):
            out[xy]=add(out.get(xy,(0,0)),mul(c,a))
    return {xy:a for xy,a in out.items() if a!=(0,0)}


def inner(a,b):
    z=(0,0)
    for xy,v in a.items(): z=add(z,mul(conj(v),b.get(xy,(0,0))))
    return z


def embed(states,T,L,offset):
    out=np.zeros((4,2*L,2*L),complex)
    s=parity(T)
    for j,state in enumerate(states):
        for (x,y),v in state.items():
            a=2*(x+offset)+(0 if s*parity(x)==1 else 1)
            b=2*(y+offset)+(0 if -s*parity(y)==1 else 1)
            assert 0<=a<2*L and 0<=b<2*L
            z=complex(*v)/(25**T*np.sqrt(2))
            out[j,a,b]+=z
            out[j,b,a]-=z
    return out


def full_reference(saved):
    L,offset=20,6
    W=np.zeros((2*L,2*L),complex)
    for x in range(L):
        W[2*((x+1)%L),2*x]=.8
        W[2*((x-1)%L)+1,2*x+1]=.8
        W[2*x+1,2*x]=W[2*x,2*x+1]=-.6j
    A=np.zeros((2*L,2),complex)
    B=np.zeros_like(A)
    A[2*offset,0]=A[2*(offset+1)+1,1]=1
    B[2*(offset+1),0]=B[2*offset+1,1]=1
    actual=np.array([(np.outer(A[:,a],B[:,b])-np.outer(B[:,b],A[:,a]))/np.sqrt(2)
                     for a in range(2) for b in range(2)])
    reference=actual.copy()
    modes=np.arange(2*L)
    mask=((modes[:,None]//2==modes[None,:]//2)&(modes[:,None]%2!=modes[None,:]%2))
    for T in range(1,5):
        actual=W@(np.where(mask,1j,1)*actual)@W.T
        reference=W@reference@W.T
        exact_actual,exact_free=saved[T]
        check(f"full-Fock-vs-exact-actual:T={T}",np.linalg.norm(actual-embed(exact_actual,T,L,offset)))
        check(f"full-Fock-vs-exact-free:T={T}",np.linalg.norm(reference-embed(exact_free,T,L,offset)))
        row=reference.reshape(4,-1).conj()@actual.reshape(4,-1).T
        p=1-sum(abs(row[:,1])**2)
        kraw=[inner(v,exact_actual[1]) for v in exact_free]
        pexact=1-Fraction(sum(normsq(z) for z in kraw),25**(4*T))
        check(f"full-Fock-input01-projection:T={T}",abs(p-float(pexact)))


def main():
    actual=[{(a,1-b):(1,0)} for a in range(2) for b in range(2)]
    reference=[dict(v) for v in actual]
    phases=((1,0),(0,1),(0,1),(1,0))
    G=[[(4,0),(0,0),(0,-3),(0,0)],[(0,-3),(0,0),(4,0),(0,0)],
       [(0,0),(4,0),(0,0),(0,-3)],[(0,0),(0,-3),(0,0),(4,0)]]
    rows=[]
    saved={}
    for T in range(1,max(TIMES)+1):
        s=parity(T-1)
        actual=[free(contact(v),s) for v in actual]
        reference=[free(v,s) for v in reference]
        if T not in TIMES: continue
        coords=((T,T+1),(1-T,T+1),(T,-T),(1-T,-T))
        R=[[v.get(xy,(0,0)) for v in reference] for xy in coords]
        Urows=[[v.get(xy,(0,0)) for v in actual] for xy in coords]
        factor=4**(2*T-1)
        expected=[[(factor*a,factor*b) for a,b in row] for row in G]
        exact(f"four-free-edge-rows:T={T}",R==expected)
        exact(f"four-actual-edge-rows-first-phase-only:T={T}",
              Urows==[[mul(a,phases[j]) for j,a in enumerate(row)] for row in expected])
        gram=[[sum((mul(conj(R[k][a]),R[k][b]))[0] for k in range(4))
               for b in range(4)] for a in range(4)]
        # Also check imaginary Gram components explicitly.
        exact(f"edge-extractor-invertible-real-Gram:T={T}",
              gram==[[25*factor*factor if a==b else 0 for b in range(4)] for a in range(4)])
        exact(f"edge-extractor-zero-imaginary-Gram:T={T}",
              all(sum(mul(conj(R[k][a]),R[k][b])[1] for k in range(4))==0
                  for a in range(4) for b in range(4)))
        exact(f"free-basis-Gram:T={T}",all(inner(reference[a],reference[b])==
              ((25**(2*T),0) if a==b else (0,0)) for a in range(4) for b in range(4)))
        exact(f"actual-basis-Gram:T={T}",all(inner(actual[a],actual[b])==
              ((25**(2*T),0) if a==b else (0,0)) for a in range(4) for b in range(4)))
        exact(f"finite-cone-support:T={T}",all(-T<=x<=T+1 and -T<=y<=T+1
              for v in actual+reference for x,y in v))
        k01=[inner(v,actual[1]) for v in reference]
        p01=1-Fraction(sum(normsq(z) for z in k01),25**(4*T))
        r=dict(T=T,raw_denominator=25**T,free_edge_rows=R,actual_edge_rows=Urows,
               edge_raw_factor=factor,input01_leakage_exact=str(p01),input01_leakage=float(p01))
        if T>=2:
            xy=(1-T,T-1)
            diff=sub(actual[1].get(xy,(0,0)),mul(reference[1].get(xy,(0,0)),(0,1)))
            predicted=(9*4**(2*T-2),9*4**(2*T-2))
            exact(f"earliest-emission-unrepaired:T={T}",diff==predicted)
            exact(f"persistent-positive-input01-leakage:T={T}",p01>0)
            rho=Fraction(4,5)**(2*T-1)
            lower=2*Fraction(3,5)**4*Fraction(4,5)**(8*T-6)/(1+rho)**2
            exact(f"quantitative-ray-lower-bound:T={T}",0<lower<=p01)
            r.update(emission_coordinate=xy,emission_difference_raw=diff,
                     emission_difference_expected_raw=predicted,
                     lower_bound_exact=str(lower),lower_bound=float(lower))
        else:
            exact("first-step-remains-exact",p01==0 and
                  all(actual[j]=={xy:mul(z,phases[j]) for xy,z in reference[j].items()}
                      for j in range(4)))
        rows.append(r)
        if T<=4: saved[T]=([dict(v) for v in actual],[dict(v) for v in reference])
    full_reference(saved)
    paths=("scripts/verify_thirring_exact_recovery.py","theory/THIRRING_EXACT_RECOVERY_GATE.md",
           "sources/1804.08508v1.pdf")
    data=dict(parameters=dict(mu="3/5",nu="4/5",phase="i",M=1),times=TIMES,
              rows=rows,checks=CHECKS,provenance={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(data,indent=2)+"\n")
    passed=sum(c["passed"] for c in CHECKS)
    lines=[f"Author checks: {passed}/{len(CHECKS)}; finite tests corroborate the all-time ray proof.",
           "Exact propagation on Z; Gaussian-integer numerators, no periodic boundary.",
           "T input01_leakage rigorous_lower_bound_from_written_ray_argument"]
    lines += [f"{r['T']} {r['input01_leakage']:.12g} {r.get('lower_bound',0):.12g}" for r in rows]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}: {c['error']:.6g}" for c in CHECKS]
    OUT.with_suffix(".txt").write_text("\n".join(lines)+"\n")
    print("\n".join(lines[:10]))
    if passed!=len(CHECKS):
        print([c for c in CHECKS if not c["passed"]])
        raise SystemExit(1)


if __name__=="__main__": main()
