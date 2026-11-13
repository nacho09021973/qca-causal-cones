"""Exact certificates for IR_CARRIER_W6_EXACT_EXAMPLE_GATE Stage 1.

No project imports, floats, scans or old-verifier execution. The report
supplies the global axial envelope bound, symmetry/minimizer implication
and interpretation of the rational relation. This script checks their
finite algebraic identities, not the unexecuted hypothesis ledger.
"""
import itertools
import platform

import sympy as sp


def main():
    checks = []

    def zero(label, value):
        entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
        if any(sp.simplify(sp.expand_complex(x)) != 0 for x in entries):
            raise AssertionError(label)
        checks.append(label)
        print(f"PASS {len(checks):02d}: {label}", flush=True)

    I2, I4 = sp.eye(2), sp.eye(4)
    pauli = [sp.Matrix([[0, 1], [1, 0]]),
             sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1)]
    G = [sp.kronecker_product(s, s) for s in pauli]
    N0 = sp.kronecker_product(I2, sum(pauli, sp.zeros(2)) / sp.sqrt(3))
    P = (I4 + N0) / 2
    W = (I4 - sp.I * N0) / sp.sqrt(2)
    zero("N0 Hermitian involution", N0**2 - I4)
    zero("W unitary", W.H * W - I4)
    zero("P projector", P**2 - P)
    zero("P rank two", sp.trace(P) - 2)
    zero("P nodal phase", W * P - (1-sp.I) / sp.sqrt(2) * P)
    e1 = I4[:, 0]
    norm2 = sp.simplify((e1.H * P * e1)[0])
    zero("resource denominator exact", norm2 - (1 + 1/sp.sqrt(3))/2)
    chi = P * e1 / sp.sqrt(norm2)
    zero("resource unit norm", (chi.H * chi)[0] - 1)
    zero("resource nodal membership", P * chi - chi)
    for j in range(3):
        for k in range(j):
            zero(f"G commute {j},{k}", G[j]*G[k]-G[k]*G[j])

    coeffs, projectors = {}, {}
    for h in itertools.product((-1, 1), repeat=3):
        proj = I4
        for j in range(3):
            proj = proj * (I4 + h[j]*G[j]) / 2
        proj = proj.applyfunc(sp.simplify)
        if h[0]*h[1]*h[2] == 1:
            zero(f"absent parity {h}", proj)
        else:
            zero(f"rank-one support {h}", sp.trace(proj)-1)
            projectors[h] = proj
            coeffs[h] = W * proj
    zero("support partition", sum(projectors.values(), sp.zeros(4))-I4)
    differences = {tuple(y[j]-x[j] for j in range(3))
                   for x in coeffs for y in coeffs}
    for delta in sorted(differences):
        pairs = [(A, C) for x, A in coeffs.items() for y, C in coeffs.items()
                 if tuple(y[j]-x[j] for j in range(3)) == delta]
        target = I4 if delta == (0, 0, 0) else sp.zeros(4)
        zero(f"Laurent S* S {delta}", sum((A.H*C for A, C in pairs), sp.zeros(4))-target)
        zero(f"Laurent S S* {delta}", sum((A*C.H for A, C in pairs), sp.zeros(4))-target)
    zero("physical isotropic node square", sum(
        (sp.Symbol(f"q{j}", real=True) * P*G[j]*P/sp.sqrt(3) for j in range(3)),
        sp.zeros(4))**2 - sum(sp.Symbol(f"q{j}", real=True)**2 for j in range(3))*P/9)
    for j in range(3):
        zero(f"node untilted {j}", sp.trace(P*G[j]*P))

    Braw = sp.Matrix([[1, 2, 0], [1, 0, 2], [1, 0, 0]])
    B = Braw / sp.sqrt(3)
    zero("lattice raw determinant", Braw.det()-4)
    for h in coeffs:
        coords = Braw.inv()*sp.Matrix(h)
        if not all(x.is_integer is True for x in coords):
            raise AssertionError(f"noninteger support coordinates {h}")
        zero(f"basis contains support {h}", Braw*coords-sp.Matrix(h))
    raw_a = sp.Matrix([1, -1, 1])
    raw_b = sp.Matrix([1, 1, -1])
    raw_c = sp.Matrix([-1, 1, 1])
    zero("basis from support b1", Braw[:, 0] + sp.Matrix([-1, -1, -1]))
    zero("basis from support b2", Braw[:, 1]-raw_a-raw_b)
    zero("basis from support b3", Braw[:, 2]-raw_c-raw_b)
    u = sp.sqrt(3)*raw_a
    V = raw_a/sp.sqrt(3)
    zero("primitive dual coordinates", B.T*u-sp.Matrix([1, 2, -2]))
    zero("primitive witness u.b1", (u.T*B[:, 0])[0]-1)
    zero("u norm squared", (u.T*u)[0]-9)
    zero("u.V", (u.T*V)[0]-3)
    zero("reciprocal duality", B.T*B.inv().T-I4[:3, :3])
    for h in coeffs:
        a = sp.Matrix(h)/sp.sqrt(3)
        zero(f"scalar character shift {h}", sp.exp(sp.I*sp.pi*(u.dot(a))/2)+sp.I)

    T0 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    F = sp.diag(-1, 1, -1)
    T = F*T0*F
    t = (I2-sp.I*sum(pauli, sp.zeros(2)))/2
    R2 = sp.kronecker_product(pauli[1], I2)
    U = R2*sp.kronecker_product(t, t)*R2.H
    zero("axis symmetry fixed V", T*V-V)
    zero("axis symmetry order three", T**3-sp.eye(3))
    zero("axis symmetry fixed space", sp.trace(T))
    zero("unitary axis representation", U.H*U-I4)
    for h, A in coeffs.items():
        th = tuple(T*sp.Matrix(h))
        zero(f"axis coefficient covariance {h}", U*A*U.H-coeffs[th])

    proj = projectors[(1, -1, 1)]
    zero("Bell-vector mean N0 zero", proj*N0*proj)
    zero("two-plane complement dimension", sp.trace(proj+N0*proj*N0)-2)
    for h in coeffs:
        a = sp.Matrix(h)/sp.sqrt(3)
        target = -1 if h == (1, -1, 1) else 1
        zero(f"attaining phase {h}", sp.exp(-sp.I*sp.pi*u.dot(a)/4)-sp.exp(sp.I*sp.pi/4)*target)
    a, b, z = sp.symbols("a b z", positive=True)
    c = 1/sp.sqrt(2)
    block = sp.Matrix([[-b, -sp.I*a], [sp.I*b, a]])/sp.sqrt(2)
    zero("attaining characteristic polynomial",
         (z*sp.eye(2)-block).det()-(z**2+c*(b-a)*z-a*b))
    first = z**2-c*(b-a)*z-a*b
    second = z**2-c*(b+a)*z+a*b
    zero("global envelope bound factorization",
         (z-b*c)**2*(z**2-a**2)-a**2*(1-c**2)*(b**2-z**2)-first*second)
    x = sp.symbols("x", real=True)
    zero("hyperbolic derivative denominator", 2+sp.sinh(x)**2-(1+sp.cosh(x)**2))
    alpha = sp.symbols("alpha", real=True)
    k, m = sp.symbols("k m", integer=True)
    uv = 3-2*alpha
    delta = -sp.Rational(1, 4)-(sp.Rational(1, 4)-k)*uv+m
    zero("branch-corrected phase relation", 2*delta-(1-4*k)*alpha-2*(m+3*k-1))
    zero("principal no-wrap phase relation", delta.subs({k: 0, m: 0})+1-alpha/2)
    print(f"Checks: {len(checks)}/{len(checks)}; exact algebra only")
    print(f"Python {platform.python_version()}; SymPy {sp.__version__}")
    print("Hypothesis-instance verdict belongs to the analytic report; no global ledger PASS here.")


if __name__ == "__main__":
    main()
