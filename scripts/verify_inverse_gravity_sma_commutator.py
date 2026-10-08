#!/usr/bin/env python3
"""Local exact controls for the IG-S2/M3 frozen compact probes.

Contract: theory/INVERSE_GRAVITY_SMA_TENSOR_PREFLIGHT_GATE.md (737e2a6).
Source: Gu-Wen arXiv:0907.1203v3, PDF pp.13-14,18,20.
No many-body spectrum or ground-state correlations are computed.
"""

import argparse
from itertools import product
from pathlib import Path

import sympy as sp

from verify_inverse_gravity_constraint_module import (
    COMPONENTS,
    real_vector_stencils,
)


def comm(a, b):
    return a * b - b * a


def equal(a, b):
    if isinstance(a, sp.MatrixBase):
        assert a.shape == b.shape
        assert all(sp.expand(entry) == 0 for entry in a - b)
    else:
        assert sp.expand(a - b) == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = []

    def note(message):
        record.append(message)
        print(message, flush=True)

    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    eye = sp.eye(3)
    x = sp.zeros(3)
    for n in range(3):
        x[(n + 1) % 3, n] = 1
    z = sp.diag(1, omega, sp.expand(omega**2))
    sine = (x - x.H) / (2 * sp.I)
    equal(z * x, omega * x * z)
    equal(x**3, eye)
    equal(sine, sine.H)
    note("PASS q=3 clock orientation and Hermitian compact sine")

    # General identity on two registers, including coincident r=s:
    # [X_r^-eps,[Z^d,X_s^eta]]
    # = (omega^(eta*d_s)-1)(1-omega^(-eps*d_r))
    #   X_s^eta X_r^-eps Z^d.
    xs = (sp.kronecker_product(x, eye), sp.kronecker_product(eye, x))
    checks = 0
    for charges in ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)):
        word = sp.kronecker_product(z**charges[0], z**charges[1])
        for r, s in product(range(2), repeat=2):
            for eps, eta in product((-1, 1), repeat=2):
                coeff = (omega ** ((eta * charges[s]) % 3) - 1) * (
                    1 - omega ** ((-eps * charges[r]) % 3)
                )
                rhs = coeff * xs[s] ** (eta % 3) * xs[r] ** ((-eps) % 3) * word
                lhs = comm(xs[r] ** ((-eps) % 3), comm(word, xs[s] ** (eta % 3)))
                equal(lhs, rhs)
                checks += 1
        # Independent direct expansion of sine commutators.
        ss = tuple((xx - xx.H) / (2 * sp.I) for xx in xs)
        for r, s in product(range(2), repeat=2):
            rhs = sp.zeros(9)
            for eps, eta in product((-1, 1), repeat=2):
                coeff = sp.Rational(eps * eta, 4)
                phase = (omega ** ((eta * charges[s]) % 3) - 1) * (
                    1 - omega ** ((-eps * charges[r]) % 3)
                )
                rhs += coeff * phase * xs[s] ** (eta % 3) * xs[r] ** ((-eps) % 3) * word
            equal(comm(ss[r], comm(word, ss[s])), rhs)
            checks += 1
    note(f"PASS {checks} exact 9x9 nested-Weyl and sine identities")

    def f(momentum):
        return sp.Rational(3, 2) if momentum % 3 else sp.S.Zero

    # Full printed vertex including cos(sum_a L^aa), not sum_a cos(L^aa).
    j, u1 = sp.symbols("J U1", positive=True)
    triples = list(product(range(3), repeat=3))
    energies = [
        3 * j * (sum(f(n) for n in ns) - sp.Rational(1, 2) * f(sum(ns)))
        for ns in triples
    ]
    hj_vertex = sp.diag(*energies)
    equal(energies[0], 0)
    equal(energies[triples.index((1, 0, 0))], sp.Rational(9, 4) * j)
    assert all(sp.expand(e / j) >= 0 for e in energies)
    local_plus = (
        sp.kronecker_product(sine, eye, eye)
        - sp.kronecker_product(eye, sine, eye)
    ) / sp.sqrt(2)
    d_plus_j = sp.expand(comm(local_plus, comm(hj_vertex, local_plus))[0, 0])
    equal(d_plus_j, sp.Rational(9, 4) * j)
    local_cross = -sine / sp.sqrt(2)
    hj_face = sp.diag(*[6 * j * f(n) for n in range(3)])
    d_cross_j = sp.expand(comm(local_cross, comm(hj_face, local_cross))[0, 0])
    equal(d_cross_j, sp.Rational(9, 2) * j)
    note("PASS full 27-state diagonal vertex and J witness coefficients 9/4, 9/2")

    # Single clock shift touches 2 diagonal links or 4 face links.
    incidences = [
        sum(len(real_vector_stencils(a)[component]) for a in range(3))
        for component in range(len(COMPONENTS))
    ]
    assert incidences == [2, 2, 2, 4, 4, 4]
    h_link = sp.diag(*[3 * u1 * f(n) for n in range(3)])
    d_link = sp.expand(comm(sine, comm(h_link, sine))[0, 0])
    equal(d_link, sp.Rational(9, 2) * u1)
    d_plus_u = d_link * (incidences[0] + incidences[1]) / 2
    d_cross_u = d_link * incidences[3] / 2
    equal(d_plus_u, 9 * u1)
    equal(d_cross_u, 9 * u1)
    witness = sp.diag(d_plus_j + d_plus_u, d_cross_j + d_cross_u)
    equal(witness, sp.diag(9 * u1 + sp.Rational(9, 4) * j,
                          9 * u1 + sp.Rational(9, 2) * j))
    note("PASS vector-link incidences: diagonal=2, face=4")
    note("PASS |0_L> witness: diag(9 U1+9 J/4, 9 U1+9 J/2), independent of p")

    # Independent arithmetic accounting for the all-volume norm bound.
    max_link_registers = max(
        sum(len(stencil) for stencil in real_vector_stencils(a))
        for a in range(3)
    )
    assert max_link_registers == 6
    u_bound = 4 * sp.Rational(9, 2) * u1 * max_link_registers * 2
    j_plus_bound = 4 * (sp.Rational(9, 2) * j + sp.Rational(9, 4) * j * 2)
    j_cross_bound = 4 * 9 * j / 2
    equal(u_bound, 216 * u1)
    equal(j_plus_bound, 36 * j)
    equal(j_cross_bound, 18 * j)
    note("PASS support-count constants for C_*=216 U1+36 J (analytic norm proof in report)")

    e_plus = sp.diag(1, -1, 0) / sp.sqrt(2)
    e_cross = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / sp.sqrt(2)
    pz = sp.Matrix([0, 0, 1])
    for tensor in (e_plus, e_cross):
        equal(sp.trace(tensor), 0)
        equal(tensor * pz, sp.zeros(3, 1))
        equal(sp.trace(tensor.T * tensor), 1)
    equal(sp.trace(e_plus.T * e_cross), 0)
    equal(2 * e_cross[0, 1] * (-sp.Rational(1, 2)), -1 / sp.sqrt(2))
    note("PASS transverse-traceless coefficient tensors and source off-diagonal factor")
    note(f"Environment: SymPy {sp.__version__}")
    note("VERDICT: LOCAL_SMA_COMMUTATOR_CONTROLS_PASS")
    note("Scope: local algebra/witness coefficients only; all-L results require analytic proof.")
    note("No true-ground Gram matrix, mode count, dispersion, QCA or gravity certified.")
    if args.output:
        args.output.write_text("\n".join(record) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
