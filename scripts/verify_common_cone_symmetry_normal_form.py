"""Check the complete Hermitian Pauli basis for the fixed D2/PHS action.

Run: python3 -B scripts/verify_common_cone_symmetry_normal_form.py
This is a local necessary-form check, not Laurent-model existence.
"""
import sympy as s

I = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)
ps = [I, sx, sy, sz]
V = s.kronecker_product(sy, sy)
Rs = [s.kronecker_product(x, I) for x in ps[1:]]
basis = {(a, b): s.kronecker_product(A, B)
         for a, A in enumerate(ps) for b, B in enumerate(ps)}
checks = 0


def zero(value):
    global checks
    if any(s.simplify(x) != 0 for x in value):
        raise AssertionError(value)
    checks += 1


nodal = []
for ab, M in basis.items():
    if all(R*M*R == M for R in Rs):
        nodal.append(ab)
assert nodal == [(0, b) for b in range(4)]
checks += 1
print('D2 nodal commutant basis:', nodal)
for i in range(3):
    allowed_d2, allowed_both = [], []
    for ab, M in basis.items():
        if all(R*M*R == (1 if j == i else -1)*M for j, R in enumerate(Rs)):
            allowed_d2.append(ab)
            if V*M.conjugate()*V.H == M:
                allowed_both.append(ab)
    assert allowed_d2 == [(i+1, b) for b in range(4)]
    assert allowed_both == [(i+1, b) for b in range(1, 4)]
    checks += 2
    print('J', i, 'D2:', allowed_d2, '; D2+PHS:', allowed_both)
    zero(V*basis[i+1, 0].conjugate()*V.H+basis[i+1, 0])
    for b in range(1, 4):
        zero(V*basis[i+1, b].conjugate()*V.H-basis[i+1, b])
# The basis is trace-orthogonal and spans all Hermitian 4x4 matrices.
for ab, A in basis.items():
    for cd, B in basis.items():
        zero(s.Matrix([[s.trace(A*B)-(4 if ab == cd else 0)]]))
v = s.symbols('vx vy vz', real=True)
q = s.symbols('qx qy qz', real=True)
d = s.symbols('dx dy dz', real=True)
lam = s.symbols('lambda')
for sign in (-1, 1):
    H = sum((q[i]*(d[i]+sign*v[i])*ps[i+1] for i in range(3)), s.zeros(2))
    zero(s.Matrix([[s.trace(H)]]))
    zero(s.Matrix([[H.charpoly(lam).as_expr()-lam**2+
                    sum(q[i]**2*(d[i]+sign*v[i])**2 for i in range(3))]]))
print(f'{checks}/{checks} exact checks PASS')
print('No proof of isotropy, exact factorization, or novelty follows from this count.')
