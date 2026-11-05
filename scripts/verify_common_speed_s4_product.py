"""Exact algebra checks for COMMON_SPEED_S4_PRODUCT_ATTEMPT.md.

The universal argument is in the report; these checks do not certify
stability outside the declared product architecture or establish novelty.
Run: python3 -B scripts/verify_common_speed_s4_product.py
"""
import itertools
import sympy as s

checks = []


def zero(label, expression):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    if any(s.simplify(x) != 0 for x in entries):
        raise AssertionError(label)
    checks.append(label)


I2 = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)
pauli = [sx, sy, sz]
av = s.symbols('a0:4', real=True)
dv = s.symbols('d0:4', real=True)
br = s.symbols('br0:4', real=True)
bi = s.symbols('bi0:4', real=True)
A = av[0]*I2 + sum((av[j+1]*pauli[j] for j in range(3)), s.zeros(2))
D = dv[0]*I2 + sum((dv[j+1]*pauli[j] for j in range(3)), s.zeros(2))
B = s.Matrix(2, 2, [br[j]+s.I*bi[j] for j in range(4)])
G = s.BlockMatrix([[A, B], [B.H, D]]).as_explicit()
G2 = G*G
zero('upper block square', G2[:2, :2] - A*A-B*B.H)
zero('lower block square', G2[2:, 2:] - D*D-B.H*B)
zero('off-diagonal trace cancellation', s.trace(B*B.H)-s.trace(B.H*B))
zero('block trace difference identity',
     s.trace(G2[:2, :2])-s.trace(G2[2:, 2:])-s.trace(A*A)+s.trace(D*D))
zero('Pauli squared trace', s.trace(A*A)-2*sum(x*x for x in av))
# Independent determinant formulation for traceless 2x2 blocks.
A0 = A.subs(av[0], 0)
D0 = D.subs(dv[0], 0)
zero('determinant formulation',
     s.trace(A0*A0)-s.trace(D0*D0)+2*(A0.det()-D0.det()))
# Boundary: involution alone does not identify cone widths with tilted blocks.
tilted = s.diag(1, -1, 1, 1)
zero('tilted boundary involution', tilted*tilted-s.eye(4))
if list(tilted[:2, :2].eigenvals()) == list(tilted[2:, 2:].eigenvals()):
    raise AssertionError('tilted boundary must have different spectra')
checks.append('tilted boundary spectra differ')
# Nonempty admitted class: exact base a=3/5, b=4/5, theta=pi/4.
a, b = s.Rational(3, 5), s.Rational(4, 5)
T = [b*sx+a*sz, b*sy+a*sz, -b*sx+a*sz]
gammas = [s.kronecker_product(pauli[j], T[j]) for j in range(3)]
P = s.kronecker_product(I2, (I2+sz)/2)
Q = s.eye(4)-P
W = ((1-s.I)*P+(1+s.I)*Q)/s.sqrt(2)
for j, gamma in enumerate(gammas):
    zero(f'base involution {j}', gamma*gamma-s.eye(4))
    zero(f'base P compression {j}', P*gamma*P-a*s.kronecker_product(pauli[j], I2)*P)
    zero(f'base Q compression {j}', Q*gamma*Q+a*s.kronecker_product(pauli[j], I2)*Q)
    R = s.kronecker_product(pauli[j], I2)
    for k, other in enumerate(gammas):
        zero(f'base D2 {j},{k}', R*other*R-(1 if j == k else -1)*other)
for signs in itertools.product((-1, 1), repeat=3):
    coeff = W
    for sign, gamma in zip(signs, gammas):
        coeff = coeff*(s.eye(4)+sign*gamma)/2
    if all(s.simplify(x) == 0 for x in coeff):
        raise AssertionError(f'base missing vertex {signs}')
    checks.append(f'base nonzero vertex {signs}')
for label in checks:
    print('PASS', label)
print(f'{len(checks)}/{len(checks)} exact checks PASS')
print('Scope: block identities and one admitted base; universal proof in report.')
