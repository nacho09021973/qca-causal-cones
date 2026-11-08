"""Scaling identities and cutoff boundary controls; assumptions in report."""
import sympy as s
L=s.symbols('L',positive=True)
M=L**2; delta=L**-12; T=L; volume=L**3
normscale=volume*M**2
assert s.simplify(T*delta**2*normscale**3)==L**-2
assert s.simplify(delta*normscale)==L**-5
assert s.simplify(volume/M**2)==L**-1
assert s.simplify((M+1)/M**2-L**-2-L**-4)==0
assert s.limit(T*delta**2*normscale**3,L,s.oo)==0
assert s.limit(volume/M**2,L,s.oo)==0
# A bounded first moment alone does not force the CCR boundary defect to zero.
N=s.symbols('N',positive=True,integer=True)
prob=1/(N+1)
assert s.simplify((N+1)*prob)==1
assert s.limit(N*prob,N,s.oo)==1
print('8/8 exact scaling and boundary identities PASS')
print('Conditional schedule T=L, M=L^2, delta=L^-12: Strang O(L^-2).')
print('Uniform second occupation moment -> global cutoff probability O(L^-1).')
print('Bounded first moment alone does not suppress the CCR boundary defect.')
print('No moment uniformity, critical tuning or fixed-QCA infrared theorem proved.')
