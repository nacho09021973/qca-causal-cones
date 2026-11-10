"""Exact axial witness under POLYHEDRAL_CORONA_TETRA_PREFLIGHT_GATE.md.

Known: fixed s=4 axial blocks, local c_IR=1/3 (2026-11-06 report).
Question: does the same walk satisfy the global IR group-velocity ball bound?
Abandon direct CJWW non-ballistic-corona transfer on a simple faster branch.
No scan, wavepacket/operational proof, or maximum-group-speed calculation.
"""
import itertools
import sympy as s

x = s.symbols('x', real=True)
I = s.eye(2)
pauli = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
W = (I-s.I*sum(pauli, s.zeros(2))/s.sqrt(3))/s.sqrt(2)
checks = 0


def zero(label, value):
    global checks
    result = s.simplify(s.trigsimp(value))
    if result != 0:
        raise AssertionError(f'{label}: residual {result}')
    checks += 1
    print(f'PASS {label}')


def truth(label, value):
    global checks
    if value is not True and value != s.true:
        raise AssertionError(f'{label}: {value}')
    checks += 1
    print(f'PASS {label}')


def main():
    eigenvalues = []
    for eps in (-1, 1):
        # Restrict sigma_x in the first tensor factor to eigenvalue eps.
        block = W*(s.cos(x)*I-s.I*eps*s.sin(x)*pauli[0])
        f = (s.cos(x)-eps*s.sin(x)/s.sqrt(3))/s.sqrt(2)
        zero(f'determinant eps={eps}', block.det()-1)
        zero(f'semitrace eps={eps}', s.trace(block)/2-f)
        slope = -s.diff(f, x)/(s.sqrt(3)*s.sqrt(1-f*f))
        zero(f'physical local slope eps={eps}', slope.subs(x, 0)-s.Rational(eps, 3))
        zero(f'physical witness slope eps={eps}', slope.subs(x, s.pi/2)-1/s.sqrt(5))
        lam = f-s.I*s.sqrt(1-f*f)
        zero(f'characteristic equation eps={eps}', lam*lam-2*f*lam+1)
        zero(f'eigenvalue derivative cross-check eps={eps}',
             (s.I*s.diff(lam, x)/(s.sqrt(3)*lam)).subs(x, s.pi/2)-1/s.sqrt(5))
        f0 = f.subs(x, s.pi/2)
        for sign in (-1, 1):
            value = f0+sign*s.I*s.sqrt(1-f0*f0)
            eigenvalues.append(value)
            target = block.subs(x, s.pi/2)
            zero(f'witness eigenvalue eps={eps},sign={sign}', (target-value*I).det())
    for i, j in itertools.combinations(range(4), 2):
        truth(f'simple eigenvalues {i},{j}', s.simplify(eigenvalues[i]-eigenvalues[j]) != 0)
    # A squared comparison suffices because both speeds are positive.
    truth('strictly faster than c_IR', s.Rational(1, 5) > s.Rational(1, 9))
    # The witness directional component is below the body's axial support.
    truth('directional component below axial causal ceiling', s.Rational(1, 5) < s.Rational(1, 3))
    print(f'{checks}/{checks} exact author checks passed')
    print('GLOBAL_IR_BALL_BOUND_REFUTED_BY_AXIAL_WITNESS')
    print('V_grp^max >= 1/sqrt(5) > c_IR=1/3; no global maximum or operational signal certified.')


if __name__ == '__main__':
    main()
