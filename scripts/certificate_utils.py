"""Shared helpers for exact symbolic certificates.

Structural equality (`a == b`) on SymPy expressions compares syntax trees, not
mathematical values: `simplify` may return an algebraically equal but
differently written form. Two certificates (W2, W5) failed under the pinned
SymPy 1.14.0 for this reason (reports/2026-10-22--escape-corruption-audit.md).
Use `sym_zero` / `assert_sym_equal` for value identities.
"""

import sympy as sp


def sym_zero(expr):
    """True iff expr simplifies to exactly zero (trig/exp forms normalized)."""
    if isinstance(expr, sp.MatrixBase):
        return all(sym_zero(e) for e in expr)
    e = sp.expand(sp.sympify(expr).rewrite(sp.exp))
    return sp.simplify(e) == 0


def assert_sym_equal(a, b, what=""):
    """Assert a and b are equal as values; report the residual on failure."""
    residual = (sp.Matrix(a) - sp.Matrix(b)) if isinstance(a, sp.MatrixBase) \
        else sp.sympify(a) - sp.sympify(b)
    assert sym_zero(residual), f"{what}: nonzero residual {sp.simplify(residual)}"
