"""Exact checks for the scoped irreducible-D2 application of P17.

Run from the repository root:
  python -B scripts/verify_irreducible_d2_pavia.py --output \
    reports/2026-09-23--irreducible-d2-pavia-verification.md

No sampling, fits, or numerical tolerances. The analytic completeness and
all-time support arguments live in the companion report, not in this script.
"""

import argparse
import hashlib
import itertools
from pathlib import Path
import platform

import sympy as sp

from verify_weyl_dirac_gate import fourier_support, published_symbol


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/1708.00826v2.pdf"
SOURCE_HASH = "dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81"
REPORT = ROOT / "reports/2026-09-23--irreducible-d2-pavia-checks.md"
BASELINE_SCRIPT = ROOT / "scripts/verify_weyl_dirac_gate.py"
I2 = sp.eye(2)
PAULI = (sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
POSITIVE = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
CORNERS = tuple(itertools.product((-1, 1), repeat=3))
CHECKS = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zero(label, expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    residuals = [sp.simplify(sp.expand(entry)) for entry in entries]
    if any(entry != 0 for entry in residuals):
        raise ValueError(f"{label}: nonzero or unresolved residual {residuals}")
    CHECKS.append(label)


def equal(label, actual, expected):
    if actual != expected:
        raise ValueError(f"{label}: {actual!r} != {expected!r}")
    CHECKS.append(label)


def neg(h):
    return tuple(-v for v in h)


def difference(h, j):
    return tuple(a - b for a, b in zip(h, j))


def pair_index():
    result = {}
    for h, j in itertools.product(CORNERS, repeat=2):
        result.setdefault(difference(h, j), []).append((h, j))
    return result


def verify_geometry(pairs):
    for h in CORNERS:
        equal(f"unique opposite difference {h}",
              set(pairs[tuple(2 * v for v in h)]), {(h, neg(h))})
        for j in CORNERS:
            if h == j or sp.prod(h) != sp.prod(j):
                continue
            equal(f"two-pair tetrahedral difference {h},{j}",
                  set(pairs[difference(h, j)]), {(h, j), (neg(j), neg(h))})
    for permutation in itertools.permutations(range(4)):
        # Integer tetrahedron has sum v_i v_i^T = 4 I_3.
        q = sum((sp.Matrix(POSITIVE[permutation[i]]) * sp.Matrix(POSITIVE[i]).T
                 for i in range(4)), sp.zeros(3)) / 4
        zero(f"tetrahedron permutation {permutation}: orthogonal", q.T * q - sp.eye(3))
        for i in range(4):
            zero(f"tetrahedron permutation {permutation}: image {i}",
                 q * sp.Matrix(POSITIVE[i]) - sp.Matrix(POSITIVE[permutation[i]]))


def p17_coefficients(epsilon):
    """Direct transcription of Proposition 5(c), arXiv PDF p. 7."""
    eta = (1 + epsilon * sp.I) / 4
    mu = sp.conjugate(eta)
    plus = (sp.Matrix([[1, 0], [1, 0]]), sp.Matrix([[0, 1], [0, 1]]),
            sp.Matrix([[0, -1], [0, 1]]), sp.Matrix([[1, 0], [-1, 0]]))
    minus = (sp.Matrix([[0, -1], [0, 1]]), sp.Matrix([[1, 0], [-1, 0]]),
             sp.Matrix([[1, 0], [1, 0]]), sp.Matrix([[0, 1], [0, 1]]))
    result = {h: eta * a for h, a in zip(POSITIVE, plus)}
    result.update({neg(h): mu * a for h, a in zip(POSITIVE, minus)})
    return result


def verify_form(epsilon, pairs):
    coefficients = p17_coefficients(epsilon)
    label = f"P17 epsilon={epsilon}"
    equal(f"{label}: full support", set(coefficients), set(CORNERS))
    zero(f"{label}: origin", sum(coefficients.values(), sp.zeros(2)) - I2)
    for d, decompositions in pairs.items():
        target = I2 if d == (0, 0, 0) else sp.zeros(2)
        zero(f"{label}: U Udag coefficient {d}",
             sum((coefficients[h] * coefficients[j].H for h, j in decompositions),
                 sp.zeros(2)) - target)
        zero(f"{label}: Udag U coefficient {d}",
             sum((coefficients[j].H * coefficients[h] for h, j in decompositions),
                 sp.zeros(2)) - target)
    for h, a in coefficients.items():
        equal(f"{label}: nonzero {h}", a == sp.zeros(2), False)
        for axis, r in enumerate(PAULI):
            gh = tuple(v if i == axis else -v for i, v in enumerate(h))
            zero(f"{label}: covariance axis {axis}, {h}", coefficients[gh] - r * a * r.H)
            commutator = (r * a - a * r).applyfunc(sp.simplify)
            equal(f"{label}: Eq2 axis {axis}, {h}", commutator == sp.zeros(2), False)
        alpha = (1 + epsilon * sp.I * sp.prod(h)) / 4
        zero(f"{label}: vertex determinant {h}", a.det())
        zero(f"{label}: vertex trace {h}", sp.trace(a) - alpha)
        zero(f"{label}: vertex square {h}", a * a - alpha * a)
        equal(f"{label}: nonzero vertex eigenvalue {h}", alpha == 0, False)
    moments = [sum((h[i] * a for h, a in coefficients.items()), sp.zeros(2)) / sp.sqrt(3)
               for i in range(3)]
    for i, moment in enumerate(moments):
        expected = PAULI[i] * (epsilon if i == 1 else 1) / sp.sqrt(3)
        zero(f"{label}: first moment {i}", moment - expected)
        zero(f"{label}: moment Hermitian {i}", moment - moment.H)
        zero(f"{label}: scalar first derivative {i}", sp.trace(moment))
        for j in range(3):
            delta = int(i == j)
            zero(f"{label}: Clifford {i},{j}",
                 moment * moments[j] + moments[j] * moment - 2 * delta * I2 / 3)
            hessian = -sum(h[i] * h[j] * sp.trace(a) for h, a in coefficients.items()) / 6
            zero(f"{label}: scalar Hessian {i},{j}", hessian + sp.Rational(delta, 3))
    z = sp.symbols("z0:3", nonzero=True)
    # z_i=exp(+i k_i/sqrt(3)); our negative Fourier exponent is z_i^(-h_i).
    matrix = sum((sp.prod(z[i] ** (-h[i]) for i in range(3)) * a
                  for h, a in coefficients.items()), sp.zeros(2))
    zero(f"{label}: determinant of full symbol", matrix.det() - 1)
    repo, _ = published_symbol(3, -epsilon, z)
    repo_coefficients = fourier_support(repo, z)
    equal(f"{label}: repository dictionary support", set(repo_coefficients), set(coefficients))
    for h in CORNERS:
        zero(f"{label}: repository dictionary coefficient {h}", repo_coefficients[h] - coefficients[h])
    zero(f"{label}: repository dictionary full symbol", repo - matrix)
    # Conventions cross-check: reversing all Fourier exponents inverts support.
    reflected = matrix.subs({v: 1 / v for v in z}, simultaneous=True)
    zero(f"{label}: Fourier convention inversion",
         reflected - sum((sp.prod(z[i] ** (-h[i]) for i in range(3)) * coefficients[neg(h)]
                          for h in CORNERS), sp.zeros(2)))


def run():
    CHECKS.clear()
    equal("primary source SHA256", digest(SOURCE), SOURCE_HASH)
    pairs = pair_index()
    verify_geometry(pairs)
    for epsilon in (1, -1):
        verify_form(epsilon, pairs)
    lines = ["# Irreducible D2 / P17: exact verification record", "",
             f"Result: PASS — {len(CHECKS)} exact checks; zero tolerance.", "",
             "Evidence: same-author computational checks; independent review pending.",
             "No canonical promotion. Published classification completeness is an input.", "",
             f"Python: {platform.python_version()}; SymPy: {sp.__version__}.", "",
             "Both P17 forms: c_0=1/sqrt(3); every vertex has a nonzero eigenvalue.",
             "The analytic all-n strict-support argument is in the companion report.",
             "The geometry checks verify the pair enumeration used to derive condition (2).", "",
             "## Provenance", "",
             f"- Source SHA256: `{digest(SOURCE)}`",
             f"- Checker SHA256: `{digest(Path(__file__))}`",
             f"- Analytic report SHA256: `{digest(REPORT)}`",
             f"- Imported baseline checker SHA256: `{digest(BASELINE_SCRIPT)}`", "",
             "## Checks", ""]
    lines.extend(f"- {label}" for label in CHECKS)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = run()
    if args.output:
        args.output.write_text(record, encoding="utf-8")
        print(f"PASS: {len(CHECKS)} exact checks; wrote {args.output}")
    else:
        print(record)


if __name__ == "__main__":
    main()
