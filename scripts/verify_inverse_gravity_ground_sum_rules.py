#!/usr/bin/env python3
"""Auxiliary exact controls for true-ground sum-rule audit, frozen at f57b0e6.

No N-type ground projector or ground-state expectation is computed.
"""

import argparse
from pathlib import Path

import sympy as sp

from verify_inverse_gravity_local_gates import real_r
from verify_inverse_gravity_curvature_probes import real_rxy


def comm(a, b):
    return a * b - b * a


def hj_support_keys(stencil, centre):
    keys = set()
    for species, offsets in enumerate(stencil):
        for offset in offsets:
            site = tuple(c + o for c, o in zip(centre, offset))
            keys.add(("register", species, site))
            if species < 3:
                keys.add(("trace", -1, site))
    return keys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lines = []

    def note(message):
        print(message, flush=True)
        lines.append(message)

    supports = [
        hj_support_keys(real_r(0), (0, 0, 0))
        | hj_support_keys(real_r(1), (0, 0, 0)),
        hj_support_keys(real_rxy(), (1, 1, 0)),
    ]
    for alpha in range(2):
        for beta in range(2):
            displacements = set()
            for kind_a, species_a, site_a in supports[alpha]:
                for kind_b, species_b, site_b in supports[beta]:
                    if (kind_a, species_a) != (kind_b, species_b):
                        continue
                    delta = tuple(a - b for a, b in zip(site_a, site_b))
                    assert all(d % 2 == 0 for d in delta)
                    displacements.add(delta[2] // 2)
            assert max(abs(d) for d in displacements) <= 2
            if alpha != beta:
                assert max(abs(d) for d in displacements) <= 1
            note(f"PASS axial H_J support, indices {alpha},{beta}: {sorted(displacements)}")

    ns = list(range(-2, 3))
    moments = sp.Matrix([[n**j for n in ns] for j in range(4)])
    null = moments.nullspace()
    expected = sp.Matrix([1, -4, 6, -4, 1])
    assert len(null) == 1 and null[0] == expected
    x = sp.symbols("x", nonzero=True)
    lhs = sum(c * x**n for c, n in zip(expected, ns))
    assert sp.expand(lhs - (2 - x - 1 / x)**2) == 0
    note("PASS unique degree-2 Fourier polynomial with fourth-order zero: (1,-4,6,-4,1)")

    # Explicit auxiliary ground-space example, not a N-type Hamiltonian.
    h = sp.diag(0, 0, 1)
    p0 = sp.diag(1, 1, 0)
    q0 = sp.eye(3) - p0
    rho = p0 / 2
    a = sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]])
    b = sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]])
    probes = [a, b]

    def matrices(probe_list):
        g = sp.Matrix(2, 2, lambda i, j: sp.trace(rho * probe_list[i].H * q0 * probe_list[j]))
        f = sp.Matrix(2, 2, lambda i, j: sp.trace(rho * probe_list[i].H * h * probe_list[j]))
        d = sp.Matrix(2, 2, lambda i, j: sp.trace(rho * comm(probe_list[i].H, comm(h, probe_list[j]))))
        return tuple(m.applyfunc(sp.expand) for m in (g, f, d))

    g, f, d = matrices(probes)
    assert g == f == sp.eye(2) / 2
    assert d == 2 * f == sp.eye(2)
    _, complex_f, complex_d = matrices([(1 + sp.I) * a, (1 - 2 * sp.I) * (a + b)])
    assert complex_d == 2 * complex_f
    note("PASS canonical real-ground D=2F controls, including complex mixed probes")
    assert g.rank() == 2 and q0.rank() == 1
    omega = sp.Matrix([1, 1, 0]) / sp.sqrt(2)
    pure_g = sp.Matrix(2, 2, lambda i, j: (omega.H * probes[i].H * q0 * probes[j] * omega)[0])
    assert pure_g == sp.ones(2) / 2 and pure_g.rank() == 1
    note("FINITE_PASS averaged-rank counterexample: averaged G rank 2, physical excited space rank 1")

    # Zeroth spectral moment is an exact ground-space Hilbert-Schmidt square.
    for probe in probes:
        d0 = sp.trace(rho * comm(probe, comm(h, probe)))
        hs = 2 * sp.trace((probe * p0).H * h * (probe * p0)) / sp.trace(p0)
        assert sp.expand(d0 - hs) == 0
    note("PASS zeroth-moment Hilbert-Schmidt identity on the auxiliary ground space")
    note(f"Environment: SymPy {sp.__version__}")
    note("VERDICT: GROUND_SUM_RULE_AUXILIARY_CONTROLS_PASS")
    note("Scope: support geometry, polynomial identity and three-level logical controls.")
    note("N-type ground moments, degeneracy and tensor spectral gate remain OPEN.")
    if args.output:
        args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
