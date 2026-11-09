"""Generate the fixed five-row exact table; no floating-point fits.

Run from repo root: python3 -B scripts/verify_two_cones_parameter_table.py
"""
import csv
import itertools
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
I, J = s.eye(2), s.eye(4)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)
ps = [sx, sy, sz]
P = s.kronecker_product(I, (I+sz)/2)
Q = J-P
W = (1-s.I)*P+(1+s.I)*Q  # physical W/sqrt(2)
Ls = [s.kronecker_product(v, I) for v in ps]
checks = 0


def zero(v):
    global checks
    vals = list(v) if isinstance(v, s.MatrixBase) else [v]
    if any(s.simplify(x) != 0 for x in vals):
        raise AssertionError(v)
    checks += 1


rows = []
for a in map(s.Rational, ['1/5', '1/3', '1/2', '3/5', '4/5']):
    b = s.sqrt(1-a*a)
    Ts = [b*sx+a*sz, b*sy+a*sz, -b*sx+a*sz]
    Gs = [s.kronecker_product(v, t) for v, t in zip(ps, Ts)]
    Ks = [g+l for g, l in zip(Gs, Ls)]
    factors = []
    for i, g in enumerate(Gs):
        zero(g-g.H)
        zero(g*g-J)
        F = {h: s.zeros(4) for h in (-2, 0, 2)}
        for r, t in itertools.product((-1, 1), repeat=2):
            F[r+t] += (J+r*g)*(J+t*Ls[i])/4
        for h in (-4, -2, 0, 2, 4):
            zero(sum((A.H*B for x, A in F.items() for y, B in F.items()
                      if y-x == h), s.zeros(4))-(J if h == 0 else s.zeros(4)))
        zero(sum(F.values(), s.zeros(4))-J)
        zero(sum((h*A for h, A in F.items()), s.zeros(4))-Ks[i])
        zero(P*Ks[i]*P-(1+a)*Ls[i]*P)
        zero(Q*Ks[i]*Q-(1-a)*Ls[i]*Q)
        for j, R in enumerate(Ls):
            zero(R*g*R-(1 if i == j else -1)*g)
            zero(R*Ls[i]*R-(1 if i == j else -1)*Ls[i])
        factors.append(F)
    coeffs = {}
    for h in itertools.product((-2, 0, 2), repeat=3):
        M = W
        for i, x in enumerate(h):
            M = M*factors[i][x]
        M = M.applyfunc(s.simplify)
        if M != s.zeros(4):
            coeffs[h] = M
    zero(len(coeffs)-27)
    zero(sum(coeffs.values(), s.zeros(4))-W)
    for i in range(3):
        zero(sum((h[i]*M for h, M in coeffs.items()), s.zeros(4))-W*Ks[i])
    basis = []
    for j in range(16):
        E = s.zeros(4)
        E[j//4, j % 4] = 1
        basis.append(E)
    constraints = s.Matrix.hstack(*[s.Matrix([
        x for M in [W]+Ks for x in E*M-M*E]) for E in basis])
    zero(constraints.rank()-15)
    for R in (P, Q):
        for i, k in enumerate(Ks):
            zero(s.trace(R*k*R))
            for j, l in enumerate(Ks):
                scale = 1+a if R == P else 1-a
                zero(R*k*R*l*R+R*l*R*k*R-
                     (2*scale**2*R if i == j else s.zeros(4)))
    cP, cQ = (1+a)/(2*s.sqrt(3)), (1-a)/(2*s.sqrt(3))
    zero(cP+cQ-1/s.sqrt(3))
    zero((cP-cQ)/(cP+cQ)-a)
    rows.append(dict(a=str(a), b=str(b), c_P=str(s.simplify(cP)),
                     c_Q=str(s.simplify(cQ)), ratio=str(s.cancel(cP/cQ)),
                     sum=str(s.simplify(cP+cQ)), support_size=27,
                     commutant_dimension=1))
    print('PASS a=', a, 'cP=', s.simplify(cP), 'cQ=', s.simplify(cQ),
          'ratio=', s.cancel(cP/cQ))
target = ROOT/'reports/2026-11-05--two-cones-parameter-table.csv'
with target.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print(f'{checks}/{checks} exact checks PASS; five rows written to {target.name}')
