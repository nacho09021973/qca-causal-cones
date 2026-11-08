#!/usr/bin/env python3
"""Bounded audit of reviewer claims, not a successor universality experiment."""
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-08--thirring-claude-check"
checks = []


def check(name, residual, tol=2e-12):
    residual = float(residual)
    checks.append(dict(name=name, residual=residual, tolerance=tol,
                       passed=bool(np.isfinite(residual) and residual < tol)))


def collision(M, starts, steps, chi):
    x, y = np.meshgrid(np.arange(starts[0], starts[0]+2*M),
                       np.arange(starts[1], starts[1]+2*M), indexing="ij")
    phase = np.ones(x.shape, complex)
    for t in range(steps):
        phase[x+t == y-t] *= np.exp(1j*chi)
    B = np.column_stack([(np.power(-1., a*x+b*y)/(2*M)).ravel()
                         for a in (0, 1) for b in (0, 1)])
    evolved = phase.ravel()[:, None]*B
    K = B.conj().T@evolved
    leakage = float(np.linalg.norm(evolved-B@K, ord=2)**2)
    # Independent exact contact counting in each initial parity block.
    counts = {}
    for a in (0, 1):
        for b in (0, 1):
            coords = [(i, j) for i in range(starts[0], starts[0]+2*M)
                      for j in range(starts[1], starts[1]+2*M)
                      if i % 2 == a and j % 2 == b]
            hits = sum(any(i+t == j-t for t in range(steps)) for i, j in coords)
            q = Fraction(hits, len(coords))
            counts[str((a, b))] = str(q)
    q_values = [Fraction(v) for v in counts.values()]
    expected = max(2*float(q*(1-q))*(1-np.cos(chi)) for q in q_values)
    check(f"contact-count-vs-propagation:{starts}:{steps}:{chi}", abs(leakage-expected))
    return dict(starts=starts, steps=steps, chi=chi, parity_contact_fractions=counts,
                leakage=leakage, leakage_from_exact_counts=float(expected), K=K)


def main():
    rows = []
    for starts, times in (((0, 0), (0, 1, 4, 17)), ((-16, 16), (0, 17, 21))):
        for steps in times:
            r = collision(4, starts, steps, np.pi/2)
            r.pop("K")
            rows.append(r)
    # Counterexamples to the reviewer's literal 'for every T'.
    check("overlap-T0-zero-not-15/32", rows[0]["leakage"])
    check("overlap-T1-is-3/8", abs(rows[1]["leakage"]-3/8))
    check("overlap-T4-is-15/32", abs(rows[2]["leakage"]-15/32))
    transfer = []
    for chi in (0., .7, np.pi/2, np.pi):
        r = collision(4, (-16, 16), 21, chi)
        p = float(abs(r["K"][3, 0])**2)
        check(f"modal-node-transfer:{chi}", abs(p-np.sin(chi/2)**2))
        transfer.append(dict(chi=chi, node_11_probability=p,
                             concurrence=float(2*abs(r["K"][0, 0]*r["K"][3, 0]))))

    # Diagonal Fock observables: exhaustive eight-mode (four-site) occupation
    # configurations. U's contact phases cancel in conjugation of any density.
    L = 4
    bits = ((np.arange(2**(2*L))[:, None] >> np.arange(2*L)) & 1)
    dest = np.array([2*((i//2+(1 if i % 2 == 0 else -1)) % L)+i % 2
                     for i in range(2*L)])
    after = np.zeros_like(bits)
    after[:, dest] = bits
    S, Snext = (0, 1), (1, 2)
    n = bits[:, [2*x for x in S]].sum(axis=1)
    g0 = (-1.)**sum(x*bits[:, 2*x] for x in S)
    g1 = (-1.)**sum(x*after[:, 2*x] for x in Snext)
    check("Fock-region-identity-with-number-factor", np.max(abs(g1-g0*(-1.)**n)))
    check("Fock-region-minus-sign-on-N1-sector", np.max(abs((g1+g0)[n == 1])))
    failure_all_fock = float(np.max(abs(g1+g0)))
    check("unqualified-minus-sign-fails-on-full-Fock", abs(failure_all_fock-2))

    # Massive single-particle algebra only; no massive gate construction.
    L = 8
    Pi = np.diag(np.repeat((-1.)**np.arange(L), 2))
    Gamma = Pi@np.diag(np.tile([1., -1.], L))
    massive = []
    for mu in (0., .2, .6):
        W = np.zeros((2*L, 2*L), complex)
        nu = np.sqrt(1-mu*mu)
        for x in range(L):
            W[2*((x+1) % L), 2*x] = nu
            W[2*((x-1) % L)+1, 2*x+1] = nu
            W[2*x+1, 2*x] = W[2*x, 2*x+1] = -1j*mu
        gr = np.linalg.norm(W.conj().T@Gamma@W+Gamma, ord=2)
        pr = np.linalg.norm(W.conj().T@Pi@W+Pi, ord=2)
        check(f"massive-Gamma-flips:{mu}", gr)
        check(f"plain-Pi-flip-fails-by-2mu:{mu}", abs(pr-2*mu))
        massive.append(dict(mu=mu, Gamma_flip_residual=float(gr),
                            plain_Pi_flip_residual=float(pr)))

    old = json.loads((ROOT/"reports/2026-11-08--thirring-two-node.json").read_text())
    names = [r["name"] for r in old["checks"]]
    grams = [n for n in names if n.startswith("gram:")]
    counts = dict(total=len(names), gram_calls=len(grams), unique_grams=len(set(grams)),
                  gram_duplicates=len(grams)-len(set(grams)),
                  structural_18=sum(n.startswith(("fermionic-antisymmetry:",
                                 "Fourier-node-shift:", "two-node-quasienergy-shift")) for n in names))
    check("review-counts-228-49-9-40-18", 0 if list(counts.values()) == [228,49,9,40,18] else 1)
    categories = Counter()
    for name in names:
        if name.startswith(("two-packet-map:", "fermionic-map:", "three-packet-composition:")):
            category = "independent_propagator_vs_formula"
        elif name.startswith(("two-packet-leak:", "fermionic-leak:", "three-packet-leak:")):
            category = "leakage"
        elif name.startswith(("gram:", "fermionic-antisymmetry:", "Fourier-node-shift:", "two-node-quasienergy-shift")):
            category = "structural_consistency_including_repeated_grams"
        elif name.startswith(("overgrant-", "H-witness-", "ancilla-", "chi-pi-")):
            category = "illustration"
        else:
            category = "derived_diagnostic"
        categories[category] += 1
    paths = ("scripts/check_thirring_claude_objections.py", "theory/THIRRING_CLAUDE_OBJECTIONS_AUDIT.md",
             "sources/1711.03920v1.pdf", "sources/1804.08508v1.pdf",
             "reports/2026-11-08--thirring-two-node.json")
    result = dict(checks=checks, contact_cases=rows, node_transfer=transfer,
                  fock_full_space_unqualified_sign_failure=failure_all_fock,
                  massive_identity=massive, old_counts=counts, reclassified=dict(categories),
                  provenance={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    passed = sum(c["passed"] for c in checks)
    log = f"Author audit: {passed}/{len(checks)}\n"+"\n".join(
        f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}: {c['residual']:.17g}" for c in checks)+"\n"
    OUT.with_suffix(".txt").write_text(log)
    print(log)
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
