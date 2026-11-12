"""Exact algebra for TETRAHEDRAL_IR_FABLE_AUDIT_GATE.md.

Known: frozen U(k) and Fable's candidate. Question: spectral/Fourier inputs?
Stop acceptance on any failed identity. Does not certify analytic Lemmas A-D.
No numerical samples, external calls, reviewed helper mutations or fitting.
"""
import itertools
import sympy as s

checks = 0


def zero(label, value):
    global checks
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    if any(s.simplify(s.expand(v)) != 0 for v in entries):
        raise AssertionError(label)
    checks += 1
    print('PASS', label, flush=True)


def truth(label, condition):
    global checks
    if condition != True:
        raise AssertionError(label)
    checks += 1
    print('PASS', label, flush=True)


def main():
    I, J = s.eye(2), s.eye(4)
    pauli = [s.Matrix([[0, 1], [1, 0]]),
             s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    G = [s.kronecker_product(p, p) for p in pauli]
    R = [s.kronecker_product(p, I) for p in pauli]
    W = s.kronecker_product(I, (I-s.I*sum(pauli, s.zeros(2))/s.sqrt(3))/s.sqrt(2))
    Nop = s.kronecker_product(I, sum(pauli, s.zeros(2))/s.sqrt(3))
    plus, minus = (J+Nop)/2, (J-Nop)/2
    singlet = s.Matrix([0, 1, -1, 0])/s.sqrt(2)
    hset = [h for h in itertools.product((-1, 1), repeat=3) if s.prod(h) == -1]
    projectors = {}
    zero('coin unitary', W.H*W-J)
    zero('coin determinant', W.det()-1)
    for h in hset:
        E = J
        for j in range(3):
            E = E*(J+h[j]*G[j])/2
        E = s.simplify(E)
        projectors[h] = E
        zero(f'joint projector trace {h}', s.trace(E)-1)
        truth(f'colour increment {h}', sum(h)%4 == 1)
    zero('projector resolution', sum(projectors.values(), s.zeros(4))-J)
    for h, k in itertools.combinations(hset, 2):
        zero(f'orthogonal channels {h},{k}', projectors[h]*projectors[k])
    zero('singlet channel', projectors[(-1, -1, -1)]-singlet*singlet.H)
    z = s.symbols('z1:4', nonzero=True)
    U = sum((W*E*s.prod(z[j]**(-h[j]) for j in range(3))
             for h,E in projectors.items()), s.zeros(4))
    C = s.prod((w+1/w)/2 for w in z)
    S = s.prod((w-1/w)/(2*s.I) for w in z)
    zero('general Laurent trace', s.trace(U)-2*s.sqrt(2)*(C-s.I*S))
    c2 = (s.trace(U)**2-s.trace(U*U))/2
    zero('general Laurent second coefficient', c2-s.Rational(2, 3)*sum(w*w+w**-2 for w in z))
    c3 = sum(U.extract(ids, ids).det() for ids in itertools.combinations(range(4), 3))
    zero('general Laurent third coefficient', c3-2*s.sqrt(2)*(C+s.I*S))
    zero('shift determinant', s.prod(s.prod(z[j]**(-h[j]) for j in range(3)) for h in hset)-1)
    for j in range(3):
        zero(f'local cluster derivative {j}', plus*G[j]*plus/s.sqrt(3)-R[j]*plus/3)
        zero(f'negative cluster derivative {j}', minus*G[j]*minus/s.sqrt(3)+R[j]*minus/3)
    q = s.symbols('q', nonzero=True)
    diagonal = W*(q**-1*(J+(q**4-1)*singlet*singlet.H))
    lam = s.symbols('lambda')
    expected = ((lam**2-s.sqrt(2)*lam/q+q**-2)
                *(lam**2-(q**3+q**-1)*lam/s.sqrt(2)+q*q))
    zero('axis characteristic factorisation', diagonal.charpoly(lam).as_expr()-expected)
    axial_point = U.subs({z[0]:s.I,z[1]:1,z[2]:1})
    axial_polynomial = axial_point.charpoly(lam).as_expr()
    zero('simple-spectrum witness polynomial', axial_polynomial-lam**4-s.Rational(4,3)*lam**2-1)
    truth('characteristic discriminant not identically zero', s.discriminant(axial_polynomial,lam) != 0)
    uplus, uminus = s.sqrt(2)*plus*singlet, s.sqrt(2)*minus*singlet
    T = s.Matrix.hstack(uplus, uminus)
    zero('active basis orthonormal', T.H*T-I)
    zero('active subspace invariant', diagonal*T-T*(T.H*diagonal*T))
    active = T.H*diagonal*T
    zero('active block trace', s.trace(active)-(q**3+q**-1)/s.sqrt(2))
    zero('active block determinant', active.det()-q*q)
    zero('active off-diagonal coupling', active[0,1]-(1-s.I)*(q**3-q**-1)/(2*s.sqrt(2)))
    # Crossing a flat eigenvalue with the active block forces sin(2s)=0.
    flat = (1-s.I)/(s.sqrt(2)*q)
    zero('flat/active crossing residual',
         (flat**2-(q**3+q**-1)*flat/s.sqrt(2)+q*q)
         -(1+s.I)*(q**4-1)/(2*q*q))
    eta = s.Matrix([s.sqrt(3)+1, 1+s.I])/s.sqrt(6+2*s.sqrt(3))
    chi = s.kronecker_product(s.Matrix([1, 0]), eta)
    M = s.kronecker_product(pauli[1], I)
    zero('resource spin normalised', (chi.H*chi)[0]-1)
    zero('resource in positive cluster', plus*chi-chi)
    zero('encoder stays in positive cluster', minus*M*chi)
    overlap = (singlet.H*M*chi)[0]
    zero('singlet overlap weight', s.conjugate(overlap)*overlap-(1+1/s.sqrt(3))/4)
    u = s.symbols('u', real=True)
    aprime = 2*u/s.sqrt(1+u*u)
    for label, target, target_slope in [
        ('centre', -5/s.sqrt(39), -s.Rational(5, 4)),
        ('lower-bound patch', -43/s.sqrt(2247), -s.Rational(43, 32))]:
        zero(label+' phase slope', aprime.subs(u, target)-target_slope)
        truth(label+' strictly interior sine', 0 < target**2 < 1)
    zero('centre group velocity', (1+s.Rational(5, 4))/3-s.Rational(3, 4))
    zero('patch group velocity', (1+s.Rational(43, 32))/3-s.Rational(25, 32))
    zero('patch arrival at Bob', s.Rational(25, 32)-s.Rational(1, 32)-s.Rational(3, 4))
    zero('centre nonzero second derivative',
         (4*s.sqrt(1-u*u)/(1+u*u)**s.Rational(3, 2)).subs(u, -5/s.sqrt(39))-39*s.sqrt(14)/128)
    # Two exact Fourier formulations for the unit-ball quadratic profile.
    r,t = s.symbols('r t', positive=True)
    radial = 4*s.pi/t*s.integrate(r*(1-r*r)**2*s.sin(t*r), (r,0,1))
    sections = 2*s.pi/3*s.integrate((1-r*r)**3*s.cos(t*r), (r,0,1))
    closed = 32*s.pi*((15-6*t*t)*s.sin(t)+(t**3-15*t)*s.cos(t))/t**7
    zero('radial Fourier closed form', radial-closed)
    zero('cross-section Fourier closed form', sections-closed)
    rho, d = s.symbols('rho d', positive=True)
    profile = (1-(rho-d)**2/rho**2)**2
    zero('profile second normal derivative', s.diff(profile,d,2).subs(d,0)-8/rho**2)
    zero('encoder second normal derivative',
         s.diff(s.sin(s.pi*profile/2),d,2).subs(d,0)-4*s.pi/rho**2)
    zero('encoder boundary coefficient', (2*s.pi*rho*4*s.pi/rho**2).subs(rho,s.Rational(1,32))-256*s.pi**2)
    zero('detector boundary coefficient', (2*s.pi*rho*8/rho**2).subs(rho,s.Rational(1,32))-512*s.pi)
    print(f'{checks}/{checks} exact checks passed')
    print('ALGEBRA_ONLY: analytic low-frequency, uniform Poisson, interference and transport bounds require the audit report.')


if __name__ == '__main__':
    main()
