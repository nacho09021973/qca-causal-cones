"""One-loop velocity linearization and truncated scalar algebra checks."""
import sympy as s
c,y,f,b=s.symbols('c y f b',positive=True)
bf=y*y*(f-b)/(6*s.pi**2*b*(f+b)**2)
bb=y*y*(b*b-f*f)/(8*s.pi**2*b*f**3)
at={f:c,b:c}; checks=0
def eq(a,b):
    global checks
    assert s.simplify(a-b)==0; checks+=1
scale=y*y/(24*s.pi**2*c**3)
eq(s.diff(bf,f).subs(at),scale)
eq(s.diff(bf,b).subs(at),-scale)
eq(s.diff(bb,b).subs(at),6*scale)
eq(s.diff(bb,f).subs(at),-6*scale)
M=s.Matrix([[1,0,-1],[0,1,-1],[-6,-6,12]])
assert M.eigenvals()=={0:1,1:1,13:1}; checks+=1
assert (s.Matrix([[6,6,1]])*M)==s.zeros(1,3); checks+=1
assert s.Matrix([[1,-1,0]])*M==s.Matrix([[1,-1,0]]); checks+=1
assert s.Matrix([[s.Rational(1,2),s.Rational(1,2),-1]])*M==13*s.Matrix([[s.Rational(1,2),s.Rational(1,2),-1]]); checks+=1
q1,q2=s.symbols('q1 q2',positive=True)
N=s.Matrix([[q1,0,-q1],[0,q2,-q2],[-6*q1,-6*q2,6*(q1+q2)]])
D=s.diag(6,6,1)
assert D*N==(D*N).T; checks+=1
t1,t2,tb=s.symbols('t1 t2 tb',real=True)
v=s.Matrix([t1,t2,tb])
eq((v.T*D*N*v)[0],6*q1*(t1-tb)**2+6*q2*(t2-tb)**2)
# Finite oscillator: Hermiticity exact, CCR has a boundary defect.
for cutoff in [2,3,4]:
    a=s.zeros(cutoff+1)
    for n in range(1,cutoff+1): a[n-1,n]=s.sqrt(n)
    phi=(a+a.H)/s.sqrt(2); pi=(a-a.H)/(s.I*s.sqrt(2))
    assert phi==phi.H and pi==pi.H; checks+=1
    edge=s.zeros(cutoff+1); edge[cutoff,cutoff]=cutoff+1
    assert (phi*pi-pi*phi-s.I*(s.eye(cutoff+1)-edge)).applyfunc(s.simplify)==s.zeros(cutoff+1)
    checks+=1
print(f'{checks}/{checks} exact checks PASS')
print('IR velocity generator: -y^2/(24 pi^2 c^3) M; eigenvalues M: 0,1,13.')
print('Weighted dissipation =6 q1(v1-vb)^2+6 q2(v2-vb)^2.')
print('Scalar cutoff preserves Hermiticity, not exact canonical commutation.')
print('No microscopic critical matching or cutoff convergence certified.')
