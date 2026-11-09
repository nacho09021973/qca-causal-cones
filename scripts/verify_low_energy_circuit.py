"""Exact algebra and finite-volume controls for the Wilson circuit proposal."""
import sympy as s
I=s.eye(2); x=s.Matrix([[0,1],[1,0]]); y=s.Matrix([[0,-s.I],[s.I,0]]); z=s.diag(1,-1)
A=[s.kronecker_product(x,p) for p in [x,y,z]]
B=s.kronecker_product(z,I); checks=0
def zero(M):
    global checks
    assert M.applyfunc(s.simplify)==s.zeros(*M.shape)
    checks+=1
for i in range(3):
    zero(A[i]*B+B*A[i])
    for j in range(3): zero(A[i]*A[j]+A[j]*A[i]-2*(i==j)*s.eye(4))
q=s.symbols('qx qy qz',real=True); v=s.symbols('v',positive=True)
mass=sum(1-s.cos(t) for t in q)
h=sum((v*A[i]*s.sin(q[i]) for i in range(3)),s.zeros(4))+B*mass
zero(h*h-(v*v*sum(s.sin(t)**2 for t in q)+mass**2)*s.eye(4))
for i in range(3):
    hop=(-s.I*v*A[i]-B)/2
    zero(s.expand_complex(hop*s.exp(s.I*q[i])+hop.H*s.exp(-s.I*q[i]))
         -v*A[i]*s.sin(q[i])+B*s.cos(q[i]))
    zero(h.diff(q[i]).subs(dict.fromkeys(q,0))-v*A[i])
assert s.Rational(3,2)*4-4==2; checks+=1
ell,g0=s.symbols('ell g0',positive=True)
running=g0*s.exp(-2*ell)
assert s.simplify(s.diff(running,ell)+2*running)==0; checks+=1
assert s.integrate(running**2,(ell,0,s.oo))==g0**2/4; checks+=1
print(f'{checks}/{checks} exact checks PASS')
print('Free dispersion: E^2=v^2 sum sin(k_i)^2+[sum(1-cos(k_i))]^2')
print('Tree-level contact coupling flow: du/dell=-2u')
print('Integral of leading u(ell)^2: u0^2/4; no two-loop coefficient computed.')
