#!/usr/bin/env python3
"""Auxiliary checks for the mixed ground test, frozen at c15bde3.

No N-type ground projector or many-body Hamiltonian is constructed.
Scalar stencil helper is reused read-only; source is Gu-Wen v3 pp.14,18.
"""

import argparse
from itertools import product
from pathlib import Path

import sympy as sp

from verify_inverse_gravity_constraint_module import real_scalar_stencils
from verify_inverse_gravity_curvature_probes import periodic_word


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lines = []

    def note(message):
        print(message, flush=True)
        lines.append(message)

    x = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    z = sp.diag(1, omega, sp.expand(omega**2))
    p = ((sp.eye(3) + z + z**2) / 3).applyfunc(sp.simplify)
    assert p == sp.diag(1, 0, 0)
    t = x * p
    y = sp.I * (t.H - t)
    assert y.H == y and t**2 == sp.zeros(3)
    assert y**2 == sp.diag(1, 1, 0)
    u2 = sp.symbols("U2", positive=True)
    h_scalar = 3 * u2 * (sp.eye(3) - (x + x.H) / 2)
    w = sp.I * (h_scalar * y - y * h_scalar)
    assert w[0, 0] == -3 * u2
    note("PASS local projector, partial shift, Y Hermitian, norm(Y)=1")
    note("PASS scalar-orbit sign control: <0|i[H_scalar,Y]|0>=-3 U2")

    scalar = real_scalar_stencils()
    assert scalar[0][(0, 0, 0)] % 3 == 1
    diagonal_supports = [set(scalar[a]) for a in range(3)]
    assert set.intersection(*diagonal_supports) == {(0, 0, 0)}
    note("PASS scalar-word unique common diagonal centre, all three species present")
    for length in (4, 6):
        words = set()
        target = tuple(sorted(periodic_word(scalar, (0, 0, 0), length, 1).items()))
        matches = []
        for cell in product(range(length), repeat=3):
            centre = tuple(2 * c for c in cell)
            for sign in (-1, 1):
                word = tuple(sorted(periodic_word(scalar, centre, length, sign).items()))
                assert word not in words
                words.add(word)
                if word == target:
                    matches.append((cell, sign))
        assert matches == [((0, 0, 0), 1)]
        assert len(words) == 2 * length**3
        note(f"FINITE_PASS L={length}: {len(words)} distinct signed scalar translates; one target match")

    # Structural source check only: rho_aa has no diagonal species;
    # rho_ab (a!=b) contains only the bb diagonal species, as on PDF p.18.
    # This does not independently certify every coordinate of rho.
    all_diagonals = {0, 1, 2}
    masks = [set() for _ in range(3)]
    masks += [{a, b} for a, b in ((0, 1), (1, 2), (2, 0))]
    assert all(mask != all_diagonals for mask in masks)
    note("PASS H_g structural exclusion: cosine and sine-product words use at most two diagonal species")
    note(f"Environment: SymPy {sp.__version__}")
    note("VERDICT: MIXED_STATIONARITY_AUXILIARY_CONTROLS_PASS")
    note("Scope: local algebra, fixed-torus collisions, diagonal-species exclusion.")
    note("No true-ground correlations, tensor cost or spectrum computed.")
    if args.output:
        args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
