"""Exact checks for CYCLIC_COMMON_CONE_REALIZATION_ATTEMPT.md.

Run: python3 -B scripts/verify_cyclic_common_cone_realization.py
The expected scientific outcome is a failed cyclic covariance, not a
successful realization. Assertions certify both positive checks and defect.
"""
import itertools
import sympy as s

checks = []
I2, I4 = s.eye(2), s.eye(4)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)
pauli = [sx, sy, sz]
kron = s.kronecker_product


def clean(M):
    return M.applyfunc(s.simplify)


def zero(label, M):
    if clean(M) != s.zeros(*M.shape):
        raise AssertionError(label)
    checks.append(label)


def require(label, condition):
    if not condition:
        raise AssertionError(label)
    checks.append(label)


a, b = s.Rational(3, 5), s.Rational(4, 5)
T = b*sx + a*sz
G = [kron(p, T) for p in pauli]
P, Q = kron(I2, (I2+sz)/2), kron(I2, (I2-sz)/2)
W = ((1-s.I)*P+(1+s.I)*Q)/s.sqrt(2)
V = kron(sy, sy)
S = kron((I2-s.I*(sx+sy+sz))/2, I2)
R = [kron(p, I2) for p in pauli]
zero('W unitary', W.H*W-I4)
zero('W nodal phases', W-s.expand_complex(
    s.exp(-s.I*s.pi/4)*P+s.exp(s.I*s.pi/4)*Q))
require('two rank-two separated nodes', P.rank() == Q.rank() == 2
        and s.exp(-s.I*s.pi/4) != s.exp(s.I*s.pi/4))
zero('C square plus identity', V*V.conjugate()-I4)
zero('S unitary', S*S.H-I4)
zero('S projective order three', S**3+I4)
zero('S preserves W', S*W*S.H-W)
zero('S commutes with C as antiunitary', V*S.conjugate()*V.H-S)
for i in range(3):
    zero(f'G{i} Hermitian', G[i].H-G[i])
    zero(f'G{i} involution', G[i]*G[i]-I4)
    zero(f'cyclic first derivative {i}', S*G[i]*S.H-G[(i+1)%3])
    zero(f'P compression {i}', P*G[i]*P-a*R[i]*P)
    zero(f'Q compression {i}', Q*G[i]*Q+a*R[i]*Q)

# All eight exact coefficients in exp(-i sum h_i q_i), raw h_i=+-1.
coeff = {}
for h in itertools.product((-1, 1), repeat=3):
    A = W
    for i in range(3):
        A = A*(I4+h[i]*G[i])/2
    coeff[h] = clean(A)
    require(f'nonzero support {h}', coeff[h] != s.zeros(4))
    zero(f'PHS coefficient {h}', V*coeff[h].conjugate()*V.H-coeff[h])
    for j in range(3):
        rotated = tuple(h[i] if i == j else -h[i] for i in range(3))
        # Read the transformed coefficient directly, avoiding iteration order.
        B = W
        for i in range(3):
            B = B*(I4+rotated[i]*G[i])/2
        zero(f'D2 coefficient {j},{h}', R[j]*A*R[j].H-B)
zero('coefficient sum is W', sum(coeff.values(), s.zeros(4))-W)
for i in range(3):
    zero(f'first Fourier moment {i}',
         sum((h[i]*A for h, A in coeff.items()), s.zeros(4))-W*G[i])

# Laurent unitarity, both orders, all 27 possible displacements.
for delta in itertools.product((-2, 0, 2), repeat=3):
    left, right = s.zeros(4), s.zeros(4)
    for h, A in coeff.items():
        g = tuple(h[i]-delta[i] for i in range(3))
        if g in coeff:
            left += A.H*coeff[g]
            right += A*coeff[g].H
    target = I4 if delta == (0, 0, 0) else s.zeros(4)
    zero(f'Laurent Udagger U {delta}', left-target)
    zero(f'Laurent U Udagger {delta}', right-target)

# Exact full-update cyclic test: r(hx,hy,hz)=(hz,hx,hy).
failed = []
for h, A in coeff.items():
    rh = (h[2], h[0], h[1])
    if clean(S*A*S.H-coeff[rh]) != s.zeros(4):
        failed.append(h)
require('cyclic coefficient covariance fails', len(failed) > 0)
print('Cyclic coefficient failures:', failed)

# Independent exact section q=(pi/2,0,pi/2), rq=(pi/2,pi/2,0).
def E(i, q):
    return s.cos(q)*I4-s.I*s.sin(q)*G[i]


def U(q):
    return W*E(0, q[0])*E(1, q[1])*E(2, q[2])


t = s.pi/2
defect = clean(S*U((t, 0, t))*S.H-U((t, t, 0)))
zero('independent exact section defect', defect-2*s.I*W*R[2])
require('section defect nonzero', defect != s.zeros(4))
zero('mixed-order defect', W*(G[0]*G[1]-G[1]*G[0])-2*s.I*W*R[2])

# Nodal isotropy by square identity and independent axial eigenphase trace.
k = s.symbols('kx ky kz', real=True)
H = a/s.sqrt(3)*sum((k[i]*pauli[i] for i in range(3)), s.zeros(2))
zero('nodal cone squared', H*H-a*a/3*sum(x*x for x in k)*I2)
q = s.symbols('q', real=True)
for eps in (-1, 1):
    block = (I2-s.I*sz)/s.sqrt(2)*(s.cos(q)*I2-s.I*eps*s.sin(q)*T)
    f = (s.cos(q)-eps*a*s.sin(q))/s.sqrt(2)
    zero(f'axial semitrace eps={eps}', s.Matrix([[s.trace(block)/2-f]]))
    zero(f'axial phase derivative eps={eps}',
         s.Matrix([[s.diff(s.acos(f), q).subs(q, 0)-eps*a]]))

# Scalar commutant: Fourier moments imply [X,W]=[X,G_i]=0.
# Removing sqrt2 from W makes this rank calculation rational complex.
x = s.symbols('x0:16')
X = s.Matrix(4, 4, x)
equations = [entry for M in [s.sqrt(2)*W]+G for entry in X*M-M*X]
system, _ = s.linear_eq_to_matrix(equations, x)
rank = system.rank()
require('commutant constraint rank 15', rank == 15)
print('Commutant rank:', rank, '; dimension:', 16-rank)
for A in coeff.values():
    zero('identity in coefficient commutant', I4*A-A*I4)

print('Normalized support: (+-1,+-1,+-1)/sqrt(3); r_in=1/sqrt(3)')
print('Both nodal speeds:', a/s.sqrt(3))
print(f'{len(checks)}/{len(checks)} exact checks PASS')
print('VERDICT: CANDIDATE_FAILS_CYCLIC_COVARIANCE')
print('No impossibility theorem for arbitrary Laurent symbols follows.')
