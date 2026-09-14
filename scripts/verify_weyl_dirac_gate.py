"""Exact, fail-closed checks for the frozen standard Pavia Weyl/Dirac gate."""

import argparse
import hashlib
import itertools
from pathlib import Path
import platform
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "reports/2026-09-14--weyl-dirac-gate-contract.md"
SOURCE = ROOT / "sources/1601.04832v1.pdf"
SOURCE_SHA256 = "0dbf0a0bea497701e0408ce410d62ca0183a4aa14b4116254d029ff6602f1367"
IDENTITY = sp.eye(2)
PAULI = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.diag(1, -1),
)
MASS, HOP = sp.symbols("m n", positive=True)
CHECKS = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def residual(expression):
    return sp.cancel(sp.expand(expression).subs(HOP**2, 1 - MASS**2))


def check_zero(label, expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    for entry in entries:
        remaining = residual(entry)
        if remaining != 0:
            raise ValueError(f"{label}: nonzero or unresolved residual {remaining}")
    CHECKS.append(label)


def check_equal(label, actual, expected):
    if actual != expected:
        raise ValueError(f"{label}: {actual!r} != {expected!r}")
    CHECKS.append(label)


def laurent_adjoint(matrix, variables):
    return matrix.H.subs({variable: 1 / variable for variable in variables}, simultaneous=True)


def published_symbol(dimension, chirality, variables):
    cosines = [(variable + 1 / variable) / 2 for variable in variables]
    sines = [(variable - 1 / variable) / (2 * sp.I) for variable in variables]
    if dimension == 1:
        scalar = cosines[0]
        vector = (0, 0, sines[0])
    elif dimension == 2:
        cos_x, cos_y = cosines
        sin_x, sin_y = sines
        scalar = cos_x * cos_y
        vector = (sin_x * cos_y, cos_x * sin_y, sin_x * sin_y)
    else:
        cos_x, cos_y, cos_z = cosines
        sin_x, sin_y, sin_z = sines
        scalar = cos_x * cos_y * cos_z + chirality * sin_x * sin_y * sin_z
        vector = (
            sin_x * cos_y * cos_z - chirality * cos_x * sin_y * sin_z,
            -chirality * cos_x * sin_y * cos_z - sin_x * cos_y * sin_z,
            cos_x * cos_y * sin_z - chirality * sin_x * sin_y * cos_z,
        )
    matrix = scalar * IDENTITY
    for component, pauli in zip(vector, PAULI):
        matrix -= sp.I * component * pauli
    return matrix.applyfunc(sp.expand), sp.expand(scalar)


def rotation_product(dimension, chirality, variables):
    axes = (2,) if dimension == 1 else tuple(range(dimension))
    signs = (1, -chirality, 1) if dimension == 3 else (1,) * dimension
    matrix = IDENTITY
    for variable, axis, sign in zip(variables, axes, signs):
        positive = (IDENTITY - sign * PAULI[axis]) / 2
        negative = (IDENTITY + sign * PAULI[axis]) / 2
        matrix = matrix * (variable * positive + negative / variable)
    return matrix.applyfunc(sp.expand)


def fourier_support(matrix, variables):
    shift = sp.prod(variables)
    coefficients = {}
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            polynomial = sp.Poly(sp.expand(shift * matrix[row, column]), *variables)
            for powers, coefficient in polynomial.terms():
                displacement = tuple(1 - power for power in powers)
                coefficients.setdefault(displacement, sp.zeros(matrix.rows, matrix.cols))
                coefficients[displacement][row, column] += coefficient
    return {
        displacement: coefficient
        for displacement, coefficient in coefficients.items()
        if any(sp.expand(entry) != 0 for entry in coefficient)
    }


def hull_geometry(support, dimension):
    vertices = [sp.Matrix(displacement) / sp.sqrt(dimension) for displacement in support]
    facets = set()
    for selected in itertools.combinations(vertices, dimension):
        differences = sp.Matrix(dimension - 1, dimension, lambda row, column:
                                selected[row + 1][column] - selected[0][column])
        normals = differences.nullspace()
        if len(normals) != 1:
            continue
        normal = normals[0]
        offset = normal.dot(selected[0])
        if offset == 0:
            continue
        normalized = normal / offset
        distances = [sp.simplify(normalized.dot(vertex) - 1) for vertex in vertices]
        if all(distance <= 0 for distance in distances):
            facets.add(tuple(normalized))
    if not facets:
        raise ValueError("Hull has no certified facets")
    inradius = min(sp.simplify(1 / sp.sqrt(sum(value**2 for value in facet)))
                   for facet in facets)
    maximum = max(sp.sqrt(vertex.dot(vertex)) for vertex in vertices)
    return inradius, maximum, len(facets)


def spatial_derivative(expression, variable, dimension):
    return sp.I * variable * sp.diff(expression, variable) / sp.sqrt(dimension)


def verify_case(dimension, chirality, transpose):
    suffix = ("+" if chirality == 1 else "-") if dimension == 3 else ""
    name = f"d={dimension} {'B' if transpose else 'A'}{suffix}"
    variables = sp.symbols(f"z0:{dimension}", real=True, nonzero=True)
    matrix, scalar = published_symbol(dimension, chirality, variables)
    product = rotation_product(dimension, chirality, variables)
    if transpose:
        matrix, product = matrix.T, product.T
    check_zero(f"{name}: published vs product", matrix - product)
    adjoint = laurent_adjoint(matrix, variables)
    check_zero(f"{name}: Weyl unitarity", matrix * adjoint - IDENTITY)
    check_zero(f"{name}: Weyl quadratic", matrix**2 - 2 * scalar * matrix + IDENTITY)
    check_zero(f"{name}: scalar trace", sp.trace(matrix) - 2 * scalar)
    support = fourier_support(matrix, variables)
    corners = set(itertools.product((-1, 1), repeat=dimension))
    check_equal(f"{name}: active support", set(support), corners)
    inradius, maximum, facets = hull_geometry(support, dimension)
    check_zero(f"{name}: inradius", inradius - 1 / sp.sqrt(dimension))
    check_zero(f"{name}: maximum support", maximum - 1)
    check_equal(f"{name}: facets", facets, 2 * dimension)
    origin = dict.fromkeys(variables, 1)
    check_zero(f"{name}: zero node", matrix.subs(origin) - IDENTITY)
    spatial = [sp.I * spatial_derivative(matrix, variable, dimension).subs(origin)
               for variable in variables]
    for first, first_variable in enumerate(variables):
        check_zero(f"{name}: scalar gradient {first}",
                   spatial_derivative(scalar, first_variable, dimension).subs(origin))
        for second, second_variable in enumerate(variables):
            expected = sp.Rational(int(first == second), dimension)
            check_zero(f"{name}: Clifford {first},{second}",
                       spatial[first] * spatial[second] + spatial[second] * spatial[first]
                       - 2 * expected * IDENTITY)
            hessian = spatial_derivative(
                spatial_derivative(scalar, first_variable, dimension), second_variable, dimension)
            check_zero(f"{name}: Hessian {first},{second}", hessian.subs(origin) + expected)
    speed = sp.sqrt(sp.simplify(sp.trace(spatial[0]**2) / 2))
    check_zero(f"{name}: massless matching", speed - inradius)
    dirac = sp.BlockMatrix([[HOP * matrix, sp.I * MASS * IDENTITY],
                           [sp.I * MASS * IDENTITY, HOP * adjoint]]).as_explicit()
    if dimension == 1:
        permutation = (0, 2, 3, 1)
        reduced = sp.Matrix([[HOP / variables[0], sp.I * MASS],
                             [sp.I * MASS, HOP * variables[0]]])
        check_zero(f"{name}: minimal Dirac blocks",
                   dirac.extract(permutation, permutation) - sp.diag(reduced, reduced))
    dirac_adjoint = laurent_adjoint(dirac, variables)
    check_zero(f"{name}: Dirac unitarity", dirac * dirac_adjoint - sp.eye(4))
    check_zero(f"{name}: Dirac quadratic", dirac**2 - 2 * HOP * scalar * dirac + sp.eye(4))
    check_zero(f"{name}: Dirac trace", sp.trace(dirac) - 4 * HOP * scalar)
    sine_part = sp.I * (dirac - dirac_adjoint) / 2
    check_zero(f"{name}: logarithm algebra",
               sine_part**2 - (1 - HOP**2 * scalar**2) * sp.eye(4))
    check_equal(f"{name}: massive support", set(fourier_support(dirac, variables)),
                corners | {(0,) * dimension})
    check_equal(f"{name}: massless Dirac support",
                set(fourier_support(dirac.subs({MASS: 0, HOP: 1}), variables)), corners)
    check_equal(f"{name}: decoupled support",
                set(fourier_support(dirac.subs({MASS: 1, HOP: 0}), variables)), {(0,) * dimension})
    return name, len(support), facets, sp.sstr(inradius), sp.sstr(maximum), sp.sstr(speed)


def verify_mass_coefficients():
    scalar_argument = sp.Symbol("u", real=True)
    gap = sp.Symbol("M", positive=True)
    phase = sp.acos(HOP * scalar_argument)
    prefactor = phase / sp.sqrt(1 - HOP**2 * scalar_argument**2)

    def at_origin(expression):
        expression = expression.subs(scalar_argument, 1).subs(HOP, sp.sqrt(1 - MASS**2))
        expression = sp.simplify(expression)
        return expression.subs(sp.acos(sp.sqrt(1 - MASS**2)), gap)

    hopping = sp.sqrt(1 - MASS**2)
    ratio = gap * hopping / MASS
    check_zero("fixed-mass logarithm prefactor", at_origin(prefactor) - gap / MASS)
    for dimension in (1, 2, 3):
        speed_squared = sp.Rational(1, dimension)
        phase_coefficient = at_origin(sp.diff(phase**2, scalar_argument)) * (-speed_squared / 2)
        check_zero(f"d={dimension}: phase curvature", phase_coefficient - speed_squared * ratio)
        mass_curvature = MASS * at_origin(sp.diff(prefactor, scalar_argument)) * (-speed_squared / 2)
        expected_curvature = speed_squared * hopping * (1 - ratio) / (2 * MASS)
        check_zero(f"d={dimension}: quadratic mass term", mass_curvature - expected_curvature)
        check_zero(f"d={dimension}: independent H-squared curvature",
                   speed_squared * ratio**2 + 2 * gap * mass_curvature - phase_coefficient)
    mass_ratio = ratio.subs(gap, sp.asin(MASS))
    check_zero("c_H small-mass series", sp.series(mass_ratio, MASS, 0, 6).removeO()
               - (1 - MASS**2 / 3 - 2 * MASS**4 / 15))
    check_zero("c_omega2 small-mass series", sp.series(sp.sqrt(mass_ratio), MASS, 0, 6).removeO()
               - (1 - MASS**2 / 6 - 29 * MASS**4 / 360))
    check_zero("small-mass ratio limit", sp.limit(mass_ratio, MASS, 0, dir="+") - 1)
    angle = sp.Symbol("angle", real=True)
    check_zero("strict-bound derivative identity",
               sp.diff(sp.sin(angle) - angle * sp.cos(angle), angle) - angle * sp.sin(angle))
    check_zero("strict-bound zero endpoint", (sp.sin(angle) - angle * sp.cos(angle)).subs(angle, 0))


def verify_negative_controls():
    weyl = sp.diag(-sp.I, sp.I)
    bad_dirac = sp.BlockMatrix([[sp.Rational(4, 5) * weyl, sp.I * sp.Rational(3, 5) * IDENTITY],
                               [sp.I * sp.Rational(3, 5) * IDENTITY, sp.Rational(4, 5) * weyl]]).as_explicit()
    check_equal("negative control: missing dagger detected",
                bad_dirac * bad_dirac.H != sp.eye(4), True)
    variables = sp.symbols("z0:3", real=True, nonzero=True)
    matrix, scalar = published_symbol(3, 1, variables)
    wrong_scalar = published_symbol(3, -1, variables)[1]
    check_equal("negative control: reversed phase sign detected",
                residual(sp.trace(matrix) / 2 - wrong_scalar) != 0, True)
    momentum = sp.Symbol("momentum", real=True)
    phase = sp.acos(sp.cos(momentum) / sp.sqrt(2))
    dispersion_coefficient = sp.simplify(sp.diff(phase**2, momentum, 2).subs(momentum, 0) / 2)
    hamiltonian_coefficient = sp.simplify((phase / sp.sin(phase)).subs(momentum, 0) / sp.sqrt(2))
    discrepancy = sp.simplify(dispersion_coefficient - hamiltonian_coefficient**2)
    check_zero("negative control: exact finite-mass discrepancy",
               discrepancy - sp.pi * (4 - sp.pi) / 16)
    check_equal("negative control: missing quadratic mass term detected", discrepancy != 0, True)


def run():
    CHECKS.clear()
    check_equal("source PDF SHA256", digest(SOURCE), SOURCE_SHA256)
    rows = []
    for dimension in (1, 2, 3):
        chiralities = (1, -1) if dimension == 3 else (0,)
        transposes = (False,) if dimension == 1 else (False, True)
        for chirality, transpose in itertools.product(chiralities, transposes):
            rows.append(verify_case(dimension, chirality, transpose))
    verify_mass_coefficients()
    verify_negative_controls()
    lines = [
        "# Weyl/Dirac exact verification record", "",
        f"Result: PASS — {len(CHECKS)} exact checks; zero tolerance; seven Weyl symbols and their Dirac couplings.",
        "", "This is a local verification record, not a canonical status update.", "",
        f"Python: {platform.python_version()}; SymPy: {sp.__version__}.", "",
        "| Case | Weyl neighbors | Facets | r_in | V_causal^max | c_0 |",
        "| --- | ---: | ---: | --- | --- | --- |",
    ]
    lines.extend("| " + " | ".join(map(str, row)) + " |" for row in rows)
    lines.extend([
        "", "For each row and 0<m<1: M=asin(m), F=M*sqrt(1-m^2)/m;",
        "c_H=c_0*F and c_omega2=c_0*sqrt(F). Analytically 0<F<1.",
        "At m=0 both equal r_in (EXACT); at fixed 0<m<1 both equalities",
        "with r_in are FALSE; matching as m tends to zero is ASYMPTOTIC.",
        "", "At m=1 active support is {0}; all spatial coefficients and its inradius",
        "are zero. The limiting ratio to the nonzero-mass substrate inradius is not",
        "an inradius ratio for that collapsed active body.", "",
        "Negative controls: missing dagger, reversed phase sign, omitted quadratic mass term detected.",
        "Interval proof, continuum scaling and convention limits: see the analytic report.", "",
        "## Provenance", "",
        f"- Script SHA256: `{digest(Path(__file__))}`",
        f"- Contract SHA256: `{digest(CONTRACT)}`",
        f"- 1601.04832v1 PDF SHA256: `{digest(SOURCE)}`",
        "- Weyl input: https://arxiv.org/abs/1601.04832v1, equations (15)-(17).",
        "- Dirac dagger cross-check: https://arxiv.org/html/1601.04842v1#S2.E9.",
        "- Baseline: 44ad178; fixed cases and semantics are specified by the contract.",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the record only after all checks pass.")
    arguments = parser.parse_args()
    try:
        record = run()
    except (ValueError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if arguments.output:
        arguments.output.write_text(record, encoding="utf-8")
        print(f"PASS: {len(CHECKS)} exact checks; wrote {arguments.output}")
    else:
        print(record, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
