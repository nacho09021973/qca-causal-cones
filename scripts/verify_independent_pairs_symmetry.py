"""Local algebra only; no finite-range QW counterexample is asserted.

Run with SymPy: python -B scripts/verify_independent_pairs_symmetry.py
Contract: theory/INDEPENDENT_PAIRS_SYMMETRY_PREFLIGHT.md
"""
import sympy as s

I = s.eye(2)
px = s.Matrix([[0, 1], [1, 0]])
py = s.Matrix([[0, -s.I], [s.I, 0]])
pz = s.diag(1, -1)
paulis = [I, px, py, pz]
K = s.kronecker_product
checks = []


def zero(label, M):
    if M.applyfunc(s.simplify) != s.zeros(*M.shape):
        raise AssertionError(label)
    checks.append(label)


def require(label, value):
    if not value:
        raise AssertionError(label)
    checks.append(label)


# Exhaust all four complex Pauli basis directions of the flavor algebra.
comm_x = [i for i, A in enumerate(paulis) if A*px == px*A]
comm_xz = [i for i in comm_x if paulis[i]*pz == pz*paulis[i]]
require('exchange commutant I,rho_x', comm_x == [0, 1])
require('two-generator commutant scalar', comm_xz == [0])
# Independent arbitrary-entry derivation of the same constraints.
v = s.symbols('v0:4')
B = s.Matrix(2, 2, v)
eqx, _ = s.linear_eq_to_matrix(list(B*px-px*B), v)
eqxz, _ = s.linear_eq_to_matrix(list(B*px-px*B)+list(B*pz-pz*B), v)
require('exchange arbitrary complex kernel dimension two', 4-eqx.rank() == 2)
require('both arbitrary complex kernel dimension one', 4-eqxz.rank() == 1)

c, delta = s.symbols('c delta', real=True)
k = s.symbols('kx ky kz', real=True)
flavor = c*I+delta*px
J = [K(paulis[i+1], pz, flavor) for i in range(3)]
F, Z = K(I, I, px), K(I, I, pz)
V = K(py, py, I)
for i in range(3):
    zero(f'J Hermitian {i}', J[i].H-J[i])
    zero(f'PHS derivative {i}', V*J[i].conjugate()*V.H-J[i])
    zero(f'exchange allowed {i}', F*J[i]-J[i]*F)
    for j in range(3):
        R = K(paulis[j+1], I, I)
        zero(f'D2 derivative {i},{j}', R*J[i]*R.H-(1 if i == j else -1)*J[i])
require('second generator forbids splitting term',
        (Z*J[0]-J[0]*Z).subs(delta, 1) != s.zeros(8))

Pplus, Pminus = (I+px)/2, (I-px)/2
for eta, P in [(1, Pplus), (-1, Pminus)]:
    zero(f'flavor eigenvalue {eta}', flavor*P-(c+eta*delta)*P)
    H = (c+eta*delta)*sum((k[i]*paulis[i+1] for i in range(3)), s.zeros(2))
    zero(f'cone square {eta}', H*H-(c+eta*delta)**2*sum(x*x for x in k)*I)
    lam = s.symbols('lambda')
    zero(f'cone characteristic polynomial {eta}', s.Matrix([[
        H.charpoly(lam).as_expr()-lam**2+(c+eta*delta)**2*sum(x*x for x in k)]]))
    zero(f'flavor projector conserved {eta}', P*flavor-flavor*P)

# Hadamard rotation exhibits actual normal modes and distinct slopes.
Had = s.Matrix([[1, 1], [1, -1]])/s.sqrt(2)
zero('exchange eigenbasis', Had.H*flavor*Had-s.diag(c+delta, c-delta))
require('rational local slopes differ and positive',
        (c+delta).subs({c:s.Rational(1,3), delta:s.Rational(1,12)}) == s.Rational(5,12)
        and (c-delta).subs({c:s.Rational(1,3), delta:s.Rational(1,12)}) == s.Rational(1,4))

# Two distinct phase pairs cannot be interchanged by this fixed F.
w1 = (I-s.I*pz)/s.sqrt(2)  # theta_1=pi/4
w2 = (I-s.I*s.sqrt(3)*pz)/2  # theta_2=pi/3
Wdistinct = K(I, w1, (I+pz)/2)+K(I, w2, (I-pz)/2)
require('exchange fails for distinct phase centers',
        (F*Wdistinct-Wdistinct*F).applyfunc(s.simplify) != s.zeros(8))
W = K(I, w1, I)
zero('coincident centers permit exchange', F*W-W*F)
zero('PHS nodal matrix', V*W.conjugate()*V.H-W)

# Conserved original flavor labels plus exchange imply identical blocks.
Aentries, Dentries = s.symbols('a0:4'), s.symbols('d0:4')
A, D = s.Matrix(2, 2, Aentries), s.Matrix(2, 2, Dentries)
Ublock = K(A, (I+pz)/2)+K(D, (I-pz)/2)
zero('conserved-label exchange difference identity',
     K(I, px)*Ublock*K(I, px)-Ublock-K(D-A, pz))
print('Flavor commutants:', comm_x, comm_xz)
print('Exchange-compatible local slopes at c=1/3, delta=1/12: 5/12 and 1/4')
print(f'{len(checks)}/{len(checks)} exact checks PASS')
print('LOCAL_EXCHANGE_INSUFFICIENT; TWO_GENERATORS_FORCE_IDENTICAL_COPIES')
print('No Laurent realization, normalized causal speed, or general no-go certified.')
