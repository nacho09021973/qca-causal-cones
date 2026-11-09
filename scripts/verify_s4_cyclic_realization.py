"""Exact author checks for S4_CYCLIC_REALIZATION_ATTEMPT.md.

Run: python3 -B scripts/verify_s4_cyclic_realization.py
Physical Fourier coefficients are stored as sqrt(2)*A_h below.
No floating point tests or parameter search.
"""
import itertools
import sympy as s

checks = []


def zero(label, value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    if any(s.simplify(x) != 0 for x in entries):
        raise AssertionError(label)
    checks.append(label)


I, J = s.eye(2), s.eye(4)
pauli = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
kron = s.kronecker_product
G = [kron(p, p) for p in pauli]
R = [kron(p, I) for p in pauli]
n_tau = sum(pauli, s.zeros(2))/s.sqrt(3)
N = kron(I, n_tau)
Wraw = J-s.I*N
P, Q = (J+N)/2, (J-N)/2
V = kron(pauli[1], pauli[1])
t = (I-s.I*sum(pauli, s.zeros(2)))/2
S = kron(t, t)
zero('W unitary with normalization', Wraw.H*Wraw-2*J)
zero('cyclic representation unitary', S.H*S-J)
zero('cyclic representation cubed', S**3-J)
zero('C square +I', V*V.conjugate()-J)
zero('C exchanges nodal projectors', V*P.conjugate()*V.H-Q)
zero('S preserves W', S*Wraw*S.H-Wraw)
zero('S compatible with C', V*S.conjugate()*V.H-S)
for i in range(3):
    zero(f'G{i} Hermitian', G[i].H-G[i])
    zero(f'G{i} involution', G[i]**2-J)
    zero(f'S cycles G{i}', S*G[i]*S.H-G[(i+1) % 3])
    zero(f'S cycles R{i}', S*R[i]*S.H-R[(i+1) % 3])
    for j in range(3):
        zero(f'G{i} commutes G{j}', G[i]*G[j]-G[j]*G[i])
zero('triple product', G[0]*G[1]*G[2]+J)
coeffs = {}
for h in itertools.product((-1, 1), repeat=3):
    projector = J
    for i in range(3):
        projector = projector*(J+h[i]*G[i])/2
    A = (Wraw*projector).applyfunc(s.simplify)
    if A != s.zeros(4):
        coeffs[h] = A
        zero(f'projector rank one {h}', s.trace(projector)-1)
    else:
        zero(f'cancelled parity {h}', h[0]*h[1]*h[2]-1)
assert set(coeffs) == {h for h in itertools.product((-1, 1), repeat=3)
                       if h[0]*h[1]*h[2] == -1}
checks.append('exact four-point negative-parity support')
zero('origin coefficient sum', sum(coeffs.values(), s.zeros(4))-Wraw)
differences = {tuple(y[i]-x[i] for i in range(3))
               for x in coeffs for y in coeffs}
for d in sorted(differences):
    pairs = [(A, B) for x, A in coeffs.items() for y, B in coeffs.items()
             if tuple(y[i]-x[i] for i in range(3)) == d]
    target = 2*J if d == (0, 0, 0) else s.zeros(4)
    zero(f'Laurent Udagger U {d}',
         sum((A.H*B for A, B in pairs), s.zeros(4))-target)
    zero(f'Laurent U Udagger {d}',
         sum((A*B.H for A, B in pairs), s.zeros(4))-target)
for h, A in coeffs.items():
    zero(f'C coefficient {h}', V*A.conjugate()*V.H-A)
    rho = (h[2], h[0], h[1])
    zero(f'cyclic coefficient {h}', S*A*S.H-coeffs[rho])
    for i in range(3):
        gh = tuple(x if i == j else -x for j, x in enumerate(h))
        zero(f'D2 coefficient {i} {h}', R[i]*A*R[i].H-coeffs[gh])
for label, proj, sign in [('P', P, 1), ('Q', Q, -1)]:
    zero(label+' projector', proj**2-proj)
    zero(label+' rank two', s.trace(proj)-2)
    zero(label+' node phase', Wraw*proj-(1-sign*s.I)*proj)
    for i in range(3):
        # Physical derivative J_i = G_i/sqrt(3).
        zero(f'{label} compression {i}',
             proj*G[i]*proj/s.sqrt(3)-sign*R[i]*proj/3)
for i in range(3):
    zero(f'Fourier moment {i}',
         sum((h[i]*A for h, A in coeffs.items()), s.zeros(4))-Wraw*G[i])
q = s.symbols('qx qy qz', real=True)
lam = s.symbols('lambda')
H = sum((qi*pi for qi, pi in zip(q, pauli)), s.zeros(2))/3
zero('untilted effective cone', s.trace(H))
zero('isotropic cone polynomial',
     H.charpoly(lam).as_expr()-lam**2+sum(qi**2 for qi in q)/9)
# Independent axial route: diagonalize sigma_i, leaving a 2x2 SU(2) block.
x = s.symbols('x', real=True)
wtau = (I-s.I*n_tau)/s.sqrt(2)
for i in range(3):
    for eps in (-1, 1):
        block = wtau*(s.cos(x)*I-s.I*eps*s.sin(x)*pauli[i])
        f = (s.cos(x)-eps*s.sin(x)/s.sqrt(3))/s.sqrt(2)
        zero(f'axis half trace {i} {eps}', s.trace(block)/2-f)
        zero(f'axis determinant {i} {eps}', s.trigsimp(block.det())-1)
        zero(f'axis physical phase slope {i} {eps}',
             s.diff(s.acos(f), x).subs(x, 0)/s.sqrt(3)-eps/3)
# Direct coefficient commutant, not merely the linearized Hamiltonian.
basis = []
for j in range(16):
    E = s.zeros(4)
    E[j//4, j % 4] = 1
    basis.append(E)
constraints = s.Matrix.hstack(*[
    s.Matrix([v for A in coeffs.values() for v in E*A-A*E]) for E in basis])
rank = constraints.rank()
zero('full coefficient commutant rank 15', rank-15)
# Geometry: regular unit-circumradius tetrahedron, facets opposite vertices.
vertices = [s.Matrix(h)/s.sqrt(3) for h in coeffs]
for i, v in enumerate(vertices):
    zero(f'vertex radius {i}', v.dot(v)-1)
    for j, w in enumerate(vertices):
        zero(f'vertex dot {i} {j}', v.dot(w)-(1 if i == j else -s.Rational(1, 3)))
zero('tetrahedron centroid', sum(vertices, s.zeros(3, 1)))
# All raw vertices lie in equal-parity lattice, which has index four.
# Three of these generators already have determinant of magnitude four.
for h in coeffs:
    assert (h[0]-h[1]) % 2 == 0 and (h[0]-h[2]) % 2 == 0
zero('translation lattice index four',
     abs(s.Matrix.hstack(*[s.Matrix(h) for h in list(coeffs)[:3]]).det())-4)
print('SymPy', s.__version__)
for label in checks:
    print('PASS', label)
print(f'{len(checks)}/{len(checks)} exact checks PASS')
print('Actual raw support:', sorted(coeffs))
print('Physical support = raw/sqrt(3); cP=cQ=1/3; r_in=1/3')
print('Coefficient commutant dimension:', 16-rank)
print('Verdict: REALIZED_WITH_ACTUAL_SUPPORT; PRELIMINARY, author checks only')
