"""Exact auxiliary identities for S4_GENERAL_COIN_VIABILITY.md.

Run: python3 -B scripts/verify_s4_general_coin_viability.py
The universal argument is in the report; no search over coins is used.
"""
import itertools
import sympy as s

checks = []


def zero(label, value):
    values = list(value) if isinstance(value, s.MatrixBase) else [value]
    if any(s.simplify(s.expand(x)) != 0 for x in values):
        raise AssertionError(label)
    checks.append(label)


I, J = s.eye(2), s.eye(4)
pauli = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
G = [s.kronecker_product(p, p) for p in pauli]
F = [h for h in itertools.product((-1, 1), repeat=3) if h[0]*h[1]*h[2] == -1]
E = {}
for h in F:
    e = J
    for i in range(3):
        e = e*(J+h[i]*G[i])/2
    E[h] = e
    zero(f'projector {h}', e*e-e)
    zero(f'Hermitian {h}', e.H-e)
    zero(f'rank-one via trace {h}', s.trace(e)-1)
    zero(f'inverse tetrahedron transform {h}',
         e-(J+sum((h[i]*G[i] for i in range(3)), s.zeros(4)))/4)
zero('sum projectors', sum(E.values(), s.zeros(4))-J)
for i in range(3):
    zero(f'first moment {i}', sum((h[i]*E[h] for h in F), s.zeros(4))-G[i])
    zero(f'vertex first sum {i}', sum(h[i] for h in F))
    for j in range(3):
        zero(f'vertex second sum {i} {j}', sum(h[i]*h[j] for h in F)-4*(i == j))

# An arbitrary traceless Hermitian linear effective Hamiltonian.
x = s.symbols('x0:9', real=True)
H = [sum((x[3*i+j]*pauli[j] for j in range(3)), s.zeros(2)) for i in range(3)]
M = s.Matrix(3, 3, lambda i, j: s.trace(H[i]*H[j])/2)
B = {h: (I+s.sqrt(3)*sum((h[i]*H[i] for i in range(3)), s.zeros(2)))/4 for h in F}
zero('compressed completeness', sum(B.values(), s.zeros(2))-I)
for i in range(3):
    zero(f'compressed moment {i}',
         sum((h[i]*B[h] for h in F), s.zeros(2))/s.sqrt(3)-H[i])
for h in F:
    hv = s.Matrix(h)
    zero(f'untilted effect trace {h}', s.trace(B[h])-s.Rational(1, 2))
    zero(f'general effect determinant {h}', B[h].det()-(1-3*(hv.T*M*hv)[0])/16)
    zero(f'2x2 trace determinant identity {h}',
         s.trace(B[h]**2)-s.trace(B[h])**2+2*B[h].det())
zero('independent purity sum',
     sum(s.trace(b*b) for b in B.values())-s.Rational(1, 2)-s.Rational(3, 2)*s.trace(M))
c = s.symbols('c', positive=True)
for h in F:
    hv = s.Matrix(h)
    zero(f'isotropic rank obstruction {h}',
         (1-3*(hv.T*(c*c*s.eye(3))*hv)[0])/16-(1-9*c*c)/16)
zero('purity obstruction agrees with determinant',
     (s.Rational(1, 2)+s.Rational(9, 2)*c*c-1)+(1-9*c*c)/2)
solutions = s.solve(1-9*c*c, c)
assert solutions == [s.Rational(1, 3)], solutions
checks.append('unique positive isotropic speed 1/3')
print('SymPy', s.__version__)
for check in checks:
    print('PASS', check)
print(f'{len(checks)}/{len(checks)} exact auxiliary checks PASS')
print('Verdict: NO_DIFFERENT_UNTILTED_ISOTROPIC_SPEED_AT_ORIGIN_FOR_GENERAL_U4_COIN')
print('Author algebra only; no external review, novelty or general-QCA claim.')
