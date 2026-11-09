#!/usr/bin/env python3
"""Permanent author checks for the fixed-rule massive Thirring preflight.

Finite cases corroborate exact algebra and bounded-duration bounds in report.
No long-time scattering scan, parameter optimization, or external controls.
"""
import hashlib
import json
import platform
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-08--thirring-massive-preflight"
X = np.array([[0, 1], [1, 0]], complex)
I = np.eye(2, dtype=complex)
MU, NU, CHI = 3/5, 4/5, np.pi/2
CHECKS = []


def check(name, error, tol=3e-12):
    error = float(error)
    CHECKS.append(dict(name=name, error=error, tolerance=tol,
                       passed=bool(np.isfinite(error) and error < tol)))


def wedge_basis(A, B):
    return np.array([(np.outer(A[:, i], B[:, j])-np.outer(B[:, j], A[:, i]))/np.sqrt(2)
                     for i in range(2) for j in range(2)])


def compress(output, evolved):
    B = output.reshape(len(output), -1).T
    V = evolved.reshape(len(evolved), -1).T
    K = B.conj().T@V
    leak = float(np.linalg.norm(V-B@K, ord=2)**2)
    return K, leak


def setup(M):
    L = 2*M+16
    d = 2*L
    f = np.zeros(L)
    sites = 6+2*np.arange(M)
    f[sites] = 1/np.sqrt(M)
    g = np.roll(f, 1)
    plus, minus = np.zeros((d, 2), complex), np.zeros((d, 2), complex)
    plus[::2, 0], plus[1::2, 1] = f, g
    minus[::2, 0], minus[1::2, 1] = g, f
    W = np.zeros((d, d), complex)
    for s in range(L):
        W[2*((s+1) % L), 2*s] = NU
        W[2*((s-1) % L)+1, 2*s+1] = NU
        W[2*s+1, 2*s] = W[2*s, 2*s+1] = -1j*MU
    modes = np.arange(d)
    contact = ((modes[:, None]//2 == modes[None, :]//2) &
               (modes[:, None] % 2 != modes[None, :] % 2))
    Gamma = np.diag(np.repeat((-1.)**np.arange(L), 2)*np.tile([1., -1.], L))
    return L, plus, minus, W, contact, Gamma


def main():
    rows = []
    R = NU*I-1j*MU*X
    z = np.exp(1j*CHI)
    for M in (1, 2, 4, 8, 16):
        L, plus, minus, W, contact, Gamma = setup(M)
        check(f"Gamma-anticommutation:M={M}", np.linalg.norm(W@Gamma+Gamma@W))
        check(f"plus-charge:M={M}", np.linalg.norm(Gamma@plus-plus))
        check(f"minus-charge:M={M}", np.linalg.norm(Gamma@minus+minus))
        check(f"plus-step-exact-rotation:M={M}", np.linalg.norm(W@plus-minus@R, ord=2))
        r = (M-1)/M
        Kminus = plus.conj().T@W@minus
        expected_minus = NU*r*I-1j*MU*X
        check(f"minus-compression:M={M}", np.linalg.norm(Kminus-expected_minus))
        residual_minus = W@minus-plus@Kminus
        check(f"minus-leak-exact:M={M}", abs(np.linalg.norm(residual_minus, ord=2)**2-NU**2*(1-r*r)))
        delta = NU*np.sqrt(2/M)
        check(f"minus-error-to-rotation:M={M}", abs(np.linalg.norm(W@minus-plus@R, ord=2)-delta))
        Ktwo = plus.conj().T@W@W@plus
        expected_two = (NU*NU*r-MU*MU)*I-1j*MU*NU*(1+r)*X
        check(f"two-step-logical-matrix:M={M}", np.linalg.norm(Ktwo-expected_two))
        B = wedge_basis(plus, minus)
        check(f"two-qubit-gram:M={M}", np.linalg.norm(B.reshape(4,-1).conj()@B.reshape(4,-1).T-np.eye(4)))
        phase = np.where(contact, z, 1.)
        J_B = phase*B
        KJ, leakJ = compress(B, J_B)
        c = 1+(z-1)/M
        D = np.diag([1, c, c, 1])
        check(f"contact-compression:M={M}", np.linalg.norm(KJ-D))
        check(f"contact-leakage:M={M}", abs(leakJ-2*(M-1)/M**2*(1-np.cos(CHI))))
        contact_norm = np.linalg.norm((contact*B).reshape(4,-1).T, ord=2)
        check(f"contact-projector-norm:M={M}", abs(contact_norm-1/np.sqrt(M)))
        # Matrix ordering and contraction give two independent formulas here:
        # logical D from counting; FJ is propagated on the full lattice.
        comm = np.linalg.norm(np.kron(R,R)@D-D@np.kron(R,R), ord=2)
        for T in (1, 2):
            free, actual = B.copy(), B.copy()
            for _ in range(T):
                free = W@free@W.T
                actual = W@(phase*actual)@W.T
            target_basis = wedge_basis(minus, plus) if T % 2 else B
            Kfree, leakfree = compress(target_basis, free)
            KU, leakU = compress(target_basis, actual)
            RT = np.linalg.matrix_power(R,T)
            local = np.kron(RT, RT)
            Vtarget = (target_basis.reshape(4,-1).T@local)
            free_error = np.linalg.norm(free.reshape(4,-1).T-Vtarget, ord=2)
            actual_error = np.linalg.norm(actual.reshape(4,-1).T-Vtarget, ord=2)
            interaction_error = np.linalg.norm((actual-free).reshape(4,-1).T, ord=2)
            free_bound = 2*T*delta
            interaction_bound = abs(z-1)*(T/np.sqrt(M)+delta*T*(T-1))
            check(f"free-error-bound:M={M}:T={T}", max(0.,free_error-free_bound))
            check(f"interaction-error-bound:M={M}:T={T}", max(0.,interaction_error-interaction_bound))
            check(f"actual-error-bound:M={M}:T={T}", max(0.,actual_error-free_bound-interaction_bound))
            # Initial |00>: two R orbitals, alternating positions. The rightmost
            # occupied mode can reach xmax+T only on an all-right path, no contact.
            final_site = 6+2*M-1+T
            assert final_site < L  # all positions reached before T<=2 avoid wrap
            extreme_occupation = 2*np.sum(abs(actual[0, 2*final_site, :])**2)
            extreme_expected = NU**(2*T)/M
            check(f"ballistic-boundary-occupation:M={M}:T={T}", abs(extreme_occupation-extreme_expected))
            check(f"leakage-positive-bound:M={M}:T={T}", max(0.,extreme_expected-leakU))
            check(f"charge-zero-preserved:M={M}:T={T}", np.linalg.norm(
                Gamma@actual+actual@Gamma.T))
            if T == 1:
                expected_free = np.kron(R,expected_minus)
                check(f"free-pair-factorization:M={M}", np.linalg.norm(Kfree-expected_free))
            rows.append(dict(M=M,T=T,free_error=float(free_error),
                             interaction_error=float(interaction_error), actual_error=float(actual_error),
                             free_leakage=leakfree, actual_leakage=leakU,
                             contact_leakage=leakJ, contact_c_real=float(c.real),contact_c_imag=float(c.imag),
                             abstract_commutator=float(comm),
                             extreme_occupation=float(extreme_occupation),
                             extreme_expected=float(extreme_expected),
                             free_bound=float(free_bound),interaction_bound=float(interaction_bound)))
        # Same-sign Gamma sector: any antisymmetric two-particle wavefunction
        # has zero contact. Test two orthogonal code orbitals, plus all of W's
        # next two iterates; algebra in report covers the entire sector.
        same = (np.outer(plus[:,0],plus[:,1])-np.outer(plus[:,1],plus[:,0]))/np.sqrt(2)
        for T in range(3):
            check(f"same-charge-contact-zero:M={M}:T={T}", np.linalg.norm(contact*same))
            same = W@same@W.T
    paths = ("scripts/verify_thirring_massive_preflight.py", "theory/THIRRING_MASSIVE_ALGEBRA_PREFLIGHT.md",
             "sources/1711.03920v1.pdf","sources/1804.08508v1.pdf")
    result = dict(parameters=dict(mu=MU,nu=NU,chi=CHI),python=platform.python_version(),
                  numpy=np.__version__,random_seed=None,checks=CHECKS,rows=rows,
                  provenance={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Author checks: {passed}/{len(CHECKS)}; no independent review.",
             "Fixed rule: mu=3/5,nu=4/5,chi=pi/2. Only T=1,2; no long-time scan.",
             "M T free_error interaction_error actual_leakage contact_leakage"]
    lines += [f"{r['M']} {r['T']} {r['free_error']:.9g} {r['interaction_error']:.9g} {r['actual_leakage']:.9g} {r['contact_leakage']:.9g}" for r in rows]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}: {c['error']:.6g}" for c in CHECKS]
    OUT.with_suffix(".txt").write_text("\n".join(lines)+"\n")
    print("\n".join(lines[:13]))
    if passed != len(CHECKS):
        print([c for c in CHECKS if not c["passed"]])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
