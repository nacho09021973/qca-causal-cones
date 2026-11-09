"""Exact local antiunitary symmetry test for two fixed s=4 models.

Run: python3 -B scripts/verify_local_particle_hole_two_cones.py
All coefficient equations are linear in V (not in its conjugate).
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
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)
a, b = s.Rational(3, 5), s.Rational(4, 5)
P = s.kronecker_product(I, (I+sz)/2)
Q = J-P
W = (1-s.I)*P+(1+s.I)*Q  # all physical coefficients divided by sqrt(2)
G = [s.kronecker_product(v, t) for v, t in zip(
    [sx, sy, sz], [b*sx+a*sz, b*sy+a*sz, -b*sx+a*sz])]
L = [s.kronecker_product(v, I) for v in [sx, sy, sz]]
V = s.kronecker_product(sy, sy)
zero('candidate unitary', V*V.H-J)
zero('antiunitary square +I', V*V.conjugate()-J)
zero('doublet exchange', V*P.conjugate()*V.H-Q)
zero('W conjugation', V*W.conjugate()*V.H-W)
for i, g in enumerate(G):
    zero(f'G{i} conjugation', V*g.conjugate()*V.H-g)
    zero(f'L{i} sign reversal', V*L[i].conjugate()*V.H+L[i])


def coefficients(double):
    axes = []
    for g, l in zip(G, L):
        if not double:
            axes.append({r: (J+r*g)/2 for r in (-1, 1)})
        else:
            F = {h: s.zeros(4) for h in (-2, 0, 2)}
            for r, t in itertools.product((-1, 1), repeat=2):
                F[r+t] += (J+r*g)*(J+t*l)/4
            axes.append(F)
    out = {}
    for h in itertools.product(*[list(F) for F in axes]):
        M = W
        for i, x in enumerate(h):
            M = M*axes[i][x]
        M = M.applyfunc(s.simplify)
        if M != s.zeros(4):
            out[h] = M
    return out


basis = []
for j in range(16):
    E = s.zeros(4)
    E[j//4, j % 4] = 1
    basis.append(E)
for label, double, expected_rank in [('original', False, 15), ('double_shift', True, 16)]:
    coeffs = coefficients(double)
    zero(label+' support size', len(coeffs)-(27 if double else 8))
    M = s.Matrix.hstack(*[s.Matrix([
        x for A in coeffs.values() for x in E*A.conjugate()-A*E]) for E in basis])
    rank = M.rank()
    zero(label+' intertwiner rank', rank-expected_rank)
    if not double:
        for h, A in coeffs.items():
            zero('original coefficient '+str(h), V*A.conjugate()-A*V)
    print(label, ': rank =', rank, '; kernel dimension =', 16-rank)
    print('verdict =', 'NO_LOCAL_PHS' if rank == 16 else 'LOCAL_PHS_FOUND')
for label in checks:
    print('PASS', label)
print(f'{len(checks)}/{len(checks)} exact checks PASS')
print('No statement about physical charge or momentum-dependent transformations.')
