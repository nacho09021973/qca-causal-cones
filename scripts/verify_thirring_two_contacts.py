#!/usr/bin/env python3
"""Exact Gaussian-integer two-contact calculation and full Fock-space contrast."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"reports/2026-11-08--thirring-two-contacts"
CHECKS=[]


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def normsq(a): return a[0]**2+a[1]**2


def check(name,error,tol=2e-12):
    error=float(error)
    CHECKS.append(dict(name=name,error=error,passed=bool(np.isfinite(error) and error<tol)))


def exact_free(state,s):
    out={}
    for (x,y),a in state.items():
        px=(x+s*(-1)**x)%8
        py=(y-s*(-1)**y)%8
        for dest,weight in (((px,py),(16,0)),((px,y),(0,-12)),
                            ((x,py),(0,-12)),((x,y),(-9,0))):
            out[dest]=add(out.get(dest,(0,0)),mul(weight,a))
    return {k:v for k,v in out.items() if v!=(0,0)}


def exact_contact(state):
    return {k:mul((0,1),v) if k[0]==k[1] else v for k,v in state.items()}


def inner(a,b):
    out=(0,0)
    for k,v in a.items(): out=add(out,mul(conj(v),b.get(k,(0,0))))
    return out


def physical(mu,chi):
    nu=np.sqrt(1-mu*mu)
    L=8
    d=2*L
    A=np.zeros((d,2),complex)
    B=np.zeros((d,2),complex)
    A[4,0]=A[7,1]=B[6,0]=B[5,1]=1
    state=np.array([(np.outer(A[:,a],B[:,b])-np.outer(B[:,b],A[:,a]))/np.sqrt(2)
                    for a in range(2) for b in range(2)])
    W=np.zeros((d,d),complex)
    for x in range(L):
        W[2*((x+1)%L),2*x]=nu
        W[2*((x-1)%L)+1,2*x+1]=nu
        W[2*x+1,2*x]=W[2*x,2*x+1]=-1j*mu
    idx=np.arange(d)
    C=((idx[:,None]//2==idx[None,:]//2)&(idx[:,None]%2!=idx[None,:]%2))
    actual=state.copy()
    free=state.copy()
    rows=[]
    z=np.exp(1j*chi)
    D=np.diag([1,z,z,1])
    X=np.array([[0,1],[1,0]],complex)
    S=nu*X-1j*mu*np.eye(2)
    P0=S.conj().T@np.diag([1,0])@S
    P1=S.conj().T@np.diag([0,1])@S
    P=np.kron(P1,np.diag([1,0]))+np.kron(P0,np.diag([0,1]))
    for T in (1,2):
        actual=W@(np.where(C,z,1)*actual)@W.T
        free=W@free@W.T
        Bout=free.reshape(4,-1).T
        V=actual.reshape(4,-1).T
        K=Bout.conj().T@V
        expected=D if T==1 else (np.eye(4)+(z-1)*mu*mu*P)@D
        leak=float(np.linalg.norm(V-Bout@K,ord=2)**2)
        target=0. if T==1 else 2*mu*mu*nu*nu*(1-np.cos(chi))
        check(f"full-map:mu={mu}:chi={chi}:T={T}",np.linalg.norm(K-expected))
        check(f"leakage:mu={mu}:chi={chi}:T={T}",abs(leak-target))
        check(f"norm:mu={mu}:chi={chi}:T={T}",np.linalg.norm(V.conj().T@V-np.eye(4)))
        if T==2 and mu==.6 and chi==np.pi/2:
            witness=np.array([4,0,3,0])/5
            witness_leak=np.linalg.norm((V-Bout@K)@witness)**2
            check("maximizing-witness",abs(witness_leak-288/625))
        rows.append(dict(mu=mu,nu=nu,chi=chi,T=T,worst_leakage=leak,
                         singular_values=np.linalg.svd(K,compute_uv=False).tolist(),
                         K_real=K.real.tolist(),K_imag=K.imag.tolist()))
    return rows


def main():
    basis=[{(2+a,3-b):(1,0)} for a in range(2) for b in range(2)]
    free1=[exact_free(v,1) for v in basis]
    actual1=[exact_free(exact_contact(v),1) for v in basis]
    free2=[exact_free(v,-1) for v in free1]
    actual2=[exact_free(exact_contact(v),-1) for v in actual1]
    kraw=[[inner(a,b) for b in actual2] for a in free2]
    Knum=[[(v[0]//625,v[1]//625) for v in row] for row in kraw]
    check("exact-compression-denominator",0 if all(v[0]%625==0 and v[1]%625==0 for row in kraw for v in row) else 1)
    for states,label in ((free2,"free"),(actual2,"actual")):
        check(f"exact-gram-{label}",0 if all(inner(states[a],states[b])==((390625,0) if a==b else (0,0))
                                              for a in range(4) for b in range(4)) else 1)
        check(f"exact-no-wrap-{label}",0 if all(0<=x<=5 and 0<=y<=5 for v in states for x,y in v) else 1)
    column_norm=sum(normsq(Knum[k][0]) for k in range(4))
    check("exact-column-norm",abs(column_norm-275425))
    rows=[]
    for mu in (0.,.6,1.):
        for chi in (0.,np.pi/2): rows.extend(physical(mu,chi))
    chosen=[r for r in rows if r["mu"]==.6 and r["chi"]==np.pi/2 and r["T"]==2][0]
    check("integer-map-vs-full-Fock",np.linalg.norm(np.array(chosen["K_real"])+1j*np.array(chosen["K_imag"])-
          np.array([[complex(*v)/625 for v in row] for row in Knum])))
    paths=("scripts/verify_thirring_two_contacts.py","formal/thirring-two-contact/ThirringTwoContact/Challenge.lean",
           "formal/thirring-two-contact/ThirringTwoContact/Solution.lean","theory/THIRRING_TWO_CONTACT_COMPOSITION_GATE.md")
    result=dict(checks=CHECKS,K2_integer_numerator=Knum,K2_denominator=625,
                exact_column_defect=str(Fraction(390625-column_norm,390625)),
                exact_worst_leakage="288/625",physical_cases=rows,
                provenance={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    passed=sum(c["passed"] for c in CHECKS)
    lines=[f"Author exact/numerical checks: {passed}/{len(CHECKS)}",f"K2 numerator /625: {Knum}",
           f"Input 00 leakage: {result['exact_column_defect']}; worst leakage: 288/625 = {288/625}",
           "Lean separately checks exact reduced finite algebra; Fock identification is a modelling bridge."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}: {c['error']:.5g}" for c in CHECKS]
    OUT.with_suffix(".txt").write_text("\n".join(lines)+"\n")
    print("\n".join(lines[:4]))
    if passed!=len(CHECKS): raise SystemExit(1)


if __name__=="__main__": main()
