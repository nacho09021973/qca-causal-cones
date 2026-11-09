#!/usr/bin/env python3
"""Growing-time fixed-rule Thirring experiment, with exact free output code.

Reduced opposite-Gamma representation is checked against full antisymmetric
two-fermion propagation. Fixed schedules, strict light-cone margins, no fitting.
"""
import hashlib
import json
import platform
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-08--thirring-growing-time"
MU, NU, CHI = .6, .8, np.pi/2
CHECKS = []


def check(name, error, tol=2e-11):
    error = float(error)
    CHECKS.append(dict(name=name,error=error,tolerance=tol,
                       passed=bool(np.isfinite(error) and error < tol)))


def matrix_json(a):
    return dict(real=a.real.tolist(),imag=a.imag.tolist())


def pair_code(A,B):
    return np.array([np.outer(a,b) for a in A for b in B])


def perms(L,s):
    x = np.arange(L)
    return (x+s*(-1)**x) % L


def step(psi,s):
    moved = NU*psi[:,perms(psi.shape[1],s),:]-1j*MU*psi
    return NU*moved[:,:,perms(psi.shape[2],-s)]-1j*MU*moved


def embed(psi,s):
    """Isometry from ordered opposite-Gamma positions to wedge^2 H."""
    L = psi.shape[1]
    x = np.arange(L)
    ma = 2*x+(1-s*(-1)**x)//2
    mb = 2*x+(1+s*(-1)**x)//2
    out = np.zeros((len(psi),2*L,2*L),complex)
    out[:,ma[:,None],mb[None,:]] = psi/np.sqrt(2)
    out[:,mb[None,:],ma[:,None]] = -psi/np.sqrt(2)
    return out


def diagnostics(actual,free,label):
    A = actual.reshape(4,-1).T
    B = free.reshape(4,-1).T
    K = B.conj().T@A
    check(f"norm:{label}",np.linalg.norm(A.conj().T@A-np.eye(4)))
    check(f"free-gram:{label}",np.linalg.norm(B.conj().T@B-np.eye(4)))
    left,sv,right = np.linalg.svd(K)
    Q = left@right
    smin = float(sv.min())
    leak = max(0.,1-smin*smin)
    leak_direct = float(np.linalg.norm(A-B@K,ord=2)**2)
    check(f"leakage-identity:{label}",abs(leak-leak_direct))
    error = float(np.linalg.norm(A-B@Q,ord=2))
    error_formula = float(np.sqrt(max(0.,2*(1-smin))))
    # Compare the squared identity: sqrt(1-smin) is ill-conditioned when
    # smin=1 to floating precision, even for an exactly closed unitary code.
    check(f"squared-polar-error-identity:{label}",abs(error*error-max(0.,2*(1-smin))))
    check(f"polar-unitarity:{label}",np.linalg.norm(Q.conj().T@Q-np.eye(4)))
    # These 16 products are witnesses only, not maximization over all inputs.
    probes = (np.array([1.,0.]),np.array([0.,1.]),
              np.array([1.,1.])/np.sqrt(2),np.array([1.,1j])/np.sqrt(2))
    concurrences = []
    for a in probes:
        for b in probes:
            v = Q@np.kron(a,b)
            concurrences.append(float(2*abs(v[0]*v[3]-v[1]*v[2])))
    identity_distance = float(np.sqrt(max(0.,8-2*abs(np.trace(Q)))))
    return dict(K=matrix_json(K),polar=matrix_json(Q),singular_values=sv.tolist(),
                min_singular_value=smin,polar_unique=bool(smin>1e-10),
                worst_leakage=leak,direct_worst_leakage=leak_direct,
                full_polar_error=error,polar_error_formula=error_formula,
                full_identity_error=float(np.linalg.norm(A-B,ord=2)),
                polar_phase_aligned_frobenius_to_identity=identity_distance,
                product_probe_concurrences=concurrences,
                largest_probe_concurrence=max(concurrences))


def full_reference(M,L,offset,times,reduced):
    # Independent full spatial W, same fixed rule, antisymmetric amplitudes.
    f = np.zeros(L)
    f[offset+2*np.arange(M)] = 1/np.sqrt(M)
    g = np.roll(f,1)
    plus,minus = np.zeros((2*L,2),complex),np.zeros((2*L,2),complex)
    plus[::2,0],plus[1::2,1] = f,g
    minus[::2,0],minus[1::2,1] = g,f
    actual = np.array([(np.outer(plus[:,i],minus[:,j])-np.outer(minus[:,j],plus[:,i]))/np.sqrt(2)
                       for i in range(2) for j in range(2)])
    free = actual.copy()
    W = np.zeros((2*L,2*L),complex)
    for x in range(L):
        W[2*((x+1)%L),2*x] = NU
        W[2*((x-1)%L)+1,2*x+1] = NU
        W[2*x+1,2*x] = W[2*x,2*x+1] = -1j*MU
    idx = np.arange(2*L)
    contact = ((idx[:,None]//2 == idx[None,:]//2)&(idx[:,None]%2 != idx[None,:]%2))
    for t in range(1,max(times)+1):
        actual = W@(np.where(contact,np.exp(1j*CHI),1)*actual)@W.T
        free = W@free@W.T
        if t in times:
            ra,rf = reduced[t]
            check(f"full-vs-reduced-actual:M={M}:T={t}",np.linalg.norm(actual-embed(ra,(-1)**t)))
            check(f"full-vs-reduced-free:M={M}:T={t}",np.linalg.norm(free-embed(rf,(-1)**t)))
            ref = diagnostics(actual,free,f"full:M={M}:T={t}")
            K = free.reshape(4,-1).conj()@actual.reshape(4,-1).T
            Kr = rf.reshape(4,-1).conj()@ra.reshape(4,-1).T
            check(f"full-vs-reduced-K:M={M}:T={t}",np.linalg.norm(K-Kr))


def run(M):
    maximum = M*M
    times = sorted(set((1,M,maximum)))
    L = 2*M+2*maximum+12
    offset = 2*((maximum+5)//2)
    assert offset-maximum>=4 and offset+2*M-1+maximum<L-4
    f = np.zeros(L,complex)
    f[offset+2*np.arange(M)] = 1/np.sqrt(M)
    A = np.array([f,np.roll(f,1)])
    B = np.array([np.roll(f,1),f])
    actual = pair_code(A,B)
    reduced = {}
    rows = []
    for t in range(1,maximum+1):
        s = (-1)**(t-1)
        idx = np.arange(L)
        actual[:,idx,idx] *= np.exp(1j*CHI)
        actual = step(actual,s)
        A = NU*A[:,perms(L,s)]-1j*MU*A
        B = NU*B[:,perms(L,-s)]-1j*MU*B
        if t in times:
            free = pair_code(A,B)
            label = f"M={M}:T={t}"
            data = diagnostics(actual,free,label)
            # Strict light cone: zero amplitudes in a two-site boundary strip.
            edge = max(np.max(abs(actual[:,:2,:])),np.max(abs(actual[:,-2:,:])),
                       np.max(abs(actual[:,:,:2])),np.max(abs(actual[:,:,-2:])))
            check(f"no-boundary-contact:{label}",edge)
            dchi = abs(np.exp(1j*CHI)-1)
            bound = dchi*(t/np.sqrt(M)+NU*np.sqrt(2/M)*t*(t-1))
            check(f"previous-algebra-bound:{label}",max(0.,data["full_identity_error"]-bound))
            data.update(M=M,T=t,L=L,offset=offset,schedules=(["linear"] if t==M else [])+
                        (["quadratic"] if t==M*M else [])+(["one_step"] if t==1 else []),
                        boundary_max_amplitude=float(edge),previous_interaction_bound=float(bound))
            rows.append(data)
            if M<=2:
                reduced[t]=(actual.copy(),free.copy())
            print(f"M={M} T={t}: leakage={data['worst_leakage']:.8g}, "
                  f"error={data['full_polar_error']:.8g}, Cprobe={data['largest_probe_concurrence']:.8g}",flush=True)
    if M<=2:
        full_reference(M,L,offset,times,reduced)
    return rows


def main():
    rows = []
    for M in (1,2,4,8,16):
        rows.extend(run(M))
    convergence = []
    for schedule in ("linear","quadratic"):
        chosen = [r for r in rows if schedule in r["schedules"]]
        for a,b in zip(chosen,chosen[1:]):
            Qa = np.array(a["polar"]["real"])+1j*np.array(a["polar"]["imag"])
            Qb = np.array(b["polar"]["real"])+1j*np.array(b["polar"]["imag"])
            distance = np.sqrt(max(0.,8-2*abs(np.trace(Qa.conj().T@Qb))))
            convergence.append(dict(schedule=schedule,M_previous=a["M"],M=b["M"],
                                    phase_aligned_polar_frobenius_difference=float(distance)))
    paths=("scripts/evaluate_thirring_growing_time.py","theory/THIRRING_GROWING_TIME_FREE_OUTPUT_GATE.md",
           "sources/1711.03920v1.pdf","sources/1804.08508v1.pdf")
    result=dict(parameters=dict(mu=MU,nu=NU,chi=CHI),python=platform.python_version(),numpy=np.__version__,
                seed=None,rows=rows,polar_sequence_diagnostics=convergence,checks=CHECKS,
                provenance={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    passed=sum(c["passed"] for c in CHECKS)
    lines=[f"Author checks: {passed}/{len(CHECKS)}; no independent review or limit certificate.",
           "Fixed mu=3/5,nu=4/5,chi=pi/2. Exact free output; strict light-cone margins.",
           "M T leakage full_polar_error min_singular_value largest_probe_concurrence"]
    lines += [f"{r['M']} {r['T']} {r['worst_leakage']:.12g} {r['full_polar_error']:.12g} "
              f"{r['min_singular_value']:.12g} {r['largest_probe_concurrence']:.12g}" for r in rows]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}: {c['error']:.6g}" for c in CHECKS]
    OUT.with_suffix(".txt").write_text("\n".join(lines)+"\n")
    print(lines[0],flush=True)
    if passed!=len(CHECKS):
        print([c for c in CHECKS if not c["passed"]])
        raise SystemExit(1)


if __name__=="__main__":
    main()
