"""Exact fixed-point verifier for TWO_CONES_DOUBLE_SHIFT_ATTEMPT.md."""
import itertools
import sympy as s

checks = []


def zero(label, value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    if any(s.simplify(x) != 0 for x in entries):
        raise AssertionError(label)
    checks.append(label)


I = s.eye(2)
J = s.eye(4)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)
paulis = [sx, sy, sz]
a, b = s.Rational(3, 5), s.Rational(4, 5)
P = s.kronecker_product(I, (I+sz)/2)
Q = J-P
Wraw = (1-s.I)*P+(1+s.I)*Q
W = Wraw/s.sqrt(2)
zero('W unitary', W.H*W-J)
zero('nodal P phase', W*P-(1-s.I)*P/s.sqrt(2))
zero('nodal Q phase', W*Q-(1+s.I)*Q/s.sqrt(2))
zero('P rank two', s.trace(P)-2)
zero('Q rank two', s.trace(Q)-2)
Ts = [b*sx+a*sz, b*sy+a*sz, -b*sx+a*sz]
Gs = [s.kronecker_product(v, t) for v, t in zip(paulis, Ts)]
Ls = [s.kronecker_product(v, I) for v in paulis]
Ks = [g+l for g, l in zip(Gs, Ls)]
factors = []
for i, (g, l) in enumerate(zip(Gs, Ls)):
    for name, v in [('G', g), ('L', l)]:
        zero(f'{name}{i} Hermitian', v-v.H)
        zero(f'{name}{i} involution', v*v-J)
    F = {h: s.zeros(4) for h in (-2, 0, 2)}
    for r, t in itertools.product((-1, 1), repeat=2):
        F[r+t] += (J+r*g)*(J+t*l)/4
    # Each coordinate factor is unitary as a Laurent polynomial.
    for h in (-4, -2, 0, 2, 4):
        residue = sum((A.H*B for x, A in F.items() for y, B in F.items()
                       if y-x == h), s.zeros(4))
        zero(f'axis {i} Laurent unitarity {h}', residue-(J if h == 0 else s.zeros(4)))
    zero(f'axis {i} origin', sum(F.values(), s.zeros(4))-J)
    zero(f'axis {i} derivative', sum((h*A for h, A in F.items()), s.zeros(4))-Ks[i])
    factors.append(F)
coeffs = {}
for h in itertools.product((-2, 0, 2), repeat=3):
    M = Wraw
    for i, shift in enumerate(h):
        M = M*factors[i][shift]
    M = M.applyfunc(s.simplify)
    if M != s.zeros(4):
        coeffs[h] = M  # physical coefficient is M/sqrt(2)
zero('27 nonzero coefficients', len(coeffs)-27)
zero('coefficient sum', sum(coeffs.values(), s.zeros(4))-Wraw)
for i in range(3):
    zero(f'coefficient moment {i}',
         sum((h[i]*M for h, M in coeffs.items()), s.zeros(4))-Wraw*Ks[i])
    R = Ls[i]
    for h, M in coeffs.items():
        transformed = tuple(x if j == i else -x for j, x in enumerate(h))
        zero(f'D2 coefficient {i} {h}', R*M*R-coeffs[transformed])
    zero(f'P compression {i}', P*Ks[i]*P-(1+a)*Ls[i]*P)
    zero(f'Q compression {i}', Q*Ks[i]*Q-(1-a)*Ls[i]*Q)
q = s.symbols('qx qy qz', real=True)
lam = s.symbols('lambda')
# Second route: exact eigenphase equations along each coordinate axis.
t = s.symbols('t', real=True)
wtau = ((1-s.I)*(I+sz)+(1+s.I)*(I-sz))/(2*s.sqrt(2))
for i, Ti in enumerate(Ts):
    for eps in (-1, 1):
        stripped = wtau*(s.cos(t)*I-s.I*eps*s.sin(t)*Ti)
        f = (s.cos(t)-eps*a*s.sin(t))/s.sqrt(2)
        zero(f'axis {i} sign {eps} exact half trace', s.trace(stripped)/2-f)
        zero(f'axis {i} sign {eps} determinant', s.trigsimp(stripped.det())-1)
        phi = s.acos(f)
        zero(f'axis {i} sign {eps} P phase slope',
             eps+s.diff(phi, t).subs(t, 0)-eps*(1+a))
        zero(f'axis {i} sign {eps} Q phase slope',
             eps-s.diff(phi, t).subs(t, 0)-eps*(1-a))
for label, scale in [('P', 1+a), ('Q', 1-a)]:
    H = scale*sum((x*v for x, v in zip(q, paulis)), s.zeros(2))
    zero(f'{label} untilted', s.trace(H))
    zero(f'{label} isotropic characteristic polynomial',
         H.charpoly(lam).as_expr()-lam**2+scale**2*sum(x*x for x in q))
# Any common Fourier-coefficient commutant commutes with Wraw and Ks,
# by the sum and moment identities above and invertibility of Wraw.
basis = []
for i in range(16):
    E = s.zeros(4)
    E[i//4, i % 4] = 1
    basis.append(E)
constraints = s.Matrix.hstack(*[
    s.Matrix([entry for M in [Wraw]+Ks for entry in E*M-M*E]) for E in basis
])
rank = constraints.rank()
zero('commutant constraint rank 15', rank-15)
zero('max raw step squared 12', max(sum(x*x for x in h) for h in coeffs)-12)
# Axis steps and even coordinates establish generated group exactly 2Z^3.
for i in range(3):
    if tuple(2 if j == i else 0 for j in range(3)) not in coeffs:
        raise AssertionError('missing group generator')
    checks.append(f'group generator 2e{i}')
cP, cQ = (1+a)/(2*s.sqrt(3)), (1-a)/(2*s.sqrt(3))
zero('speed ratio four', cP/cQ-4)
if not (cP > cQ > 0):
    raise AssertionError('speed positivity and separation')
checks.append('positive unequal speeds')
for label in checks:
    print('PASS', label)
print(f'{len(checks)}/{len(checks)} exact checks PASS')
print('Raw support: {-2,0,2}^3; translation group: 2Z^3')
print('Normalized cP =', cP, '; cQ =', cQ, '; ratio =', cP/cQ)
print('Verdict: TWO_UNEQUAL_CONES (fixed model, author verification only)')
