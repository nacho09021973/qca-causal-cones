"""Occupation identities supporting the report, not a long-time pole fit."""
import sympy as s
p = s.symbols('p', real=True)
weights = [s.binomial(4,n)*p**n*(1-p)**(4-n) for n in range(5)]
assert s.simplify(sum(weights)-1) == 0
assert s.simplify(sum(n*weights[n] for n in range(5))-4*p) == 0
assert s.simplify(sum((n-4*p)**2*weights[n] for n in range(5))-4*p*(1-p)) == 0
checks = 3
for state in range(256):
    n1, n2 = (state & 15).bit_count(), (state >> 4).bit_count()
    for mode in range(8):
        if state & (1 << mode):
            after = state ^ (1 << mode)
            m1, m2 = (after & 15).bit_count(), (after >> 4).bit_count()
            assert m1*m2-n1*n2 == -(n2 if mode < 4 else n1)
            checks += 1
print(f'{checks}/{checks} exact checks PASS')
print('Mean opposite-species cell density: 4p; variance: 4p(1-p).')
print('Collision annihilator phase: exp(-i chi N_other).')
print('Stationarity uses global number conservation, proved in report.')
