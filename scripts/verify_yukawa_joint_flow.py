"""Solve the frozen one-loop effective system, not the microscopic QCA."""
import sympy as s
u,r,ell,u0=s.symbols('u r ell u0',positive=True)
P=16*s.pi**2
bu=-14*u*u/P
bl=-(3*(r*u)**2+16*u*r*u-96*u*u)/P
br=s.factor(bl/u-r*bu/u)
assert s.simplify(br+u*(3*r*r+2*r-96)/P)==0
assert s.factor(3*r*r+2*r-96)==(r+6)*(3*r-16)
us=u0/(1+14*u0*ell/P)
assert s.simplify(s.diff(us,ell)+14*us**2/P)==0
ratio=s.Rational(16,3)
assert s.simplify(br.subs(r,ratio))==0
for exponent,rate in [(s.Rational(1,21),1),(s.Rational(13,21),13)]:
    mode=(1+14*u0*ell/P)**(-exponent)
    assert s.simplify(s.diff(mode,ell)+rate*us/(24*s.pi**2)*mode)==0
    assert s.limit(mode,ell,s.oo)==0
    assert mode.subs(ell,0)==1
assert s.limit(s.integrate(us,(ell,0,ell)),ell,s.oo)==s.oo
print('Exact identities and limits PASS')
print('u=y^2; du/dell=-14u^2/(16pi^2)')
print('lambda/u -> 16/3 for positive initial ratio, within frozen ODE.')
print('Velocity modes decay as [1+14u0 ell/(16pi^2)]^(-1/21), ^(-13/21).')
print('Effective one-loop result only; no uniform microscopic matching proof.')
