"""Exact single-step response; does not estimate a long-time linewidth."""
import sympy as s
p, chi = s.symbols('p chi', real=True)
z = s.symbols('z')
K = (1-p+p*z)**4
enum = sum(p**mask.bit_count()*(1-p)**(4-mask.bit_count())*z**mask.bit_count()
           for mask in range(16))
assert s.expand(K-enum) == 0
f = K.subs(z,s.exp(-s.I*chi))
assert s.simplify(f.subs(chi,0)-1) == 0
assert s.simplify(s.diff(f,chi).subs(chi,0)+4*s.I*p) == 0
assert s.simplify(s.diff(f,chi,2).subs(chi,0)+16*p*p+4*p*(1-p)) == 0
center = s.exp(4*s.I*p*chi)*f
assert s.simplify(s.diff(center,chi).subs(chi,0)) == 0
assert s.simplify(s.diff(center,chi,2).subs(chi,0)+4*p*(1-p)) == 0
half = s.exp(-2*s.I*chi)*s.cos(chi/2)**4
assert s.simplify(s.expand(f.subs(p,s.Rational(1,2))-half.rewrite(s.exp))) == 0
assert s.simplify(f.subs(p,0)-1) == 0
assert s.simplify(f.subs(p,1)-s.exp(-4*s.I*chi)) == 0
print('9/9 exact identities PASS')
print('K(chi,p)=(1-p+p exp(-i chi))^4')
print('Centered K=1-2p(1-p)chi^2+O(chi^3)')
print('p=1/2: K=exp(-2i chi)cos(chi/2)^4')
print('No long-time pole, linewidth, or velocity correction inferred.')
