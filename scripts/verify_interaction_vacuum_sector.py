"""Exact occupation-basis check; universal sector argument is in report."""
checks = 0
for occupation in range(256):
    n1 = (occupation & 15).bit_count()
    n2 = (occupation >> 4).bit_count()
    interaction = n1*n2
    if n1+n2 <= 1:
        assert interaction == 0
        checks += 1
    assert interaction >= 0
    checks += 1
assert (1 & 15).bit_count() * (16 >> 4).bit_count() == 1
checks += 1
print(f'{checks}/{checks} exact checks PASS')
print('Vacuum and one-particle interaction generator vanish.')
print('One particle of each species at a cell has interaction eigenvalue 1.')
print('Global argument uses number conservation; no finite-density verdict.')
