"""Separate real-space construction and Z-observable checks for W4.

Finite rings are exact regression witnesses, not a finite-size extrapolation.
The Bloch comparison imports the other certificate: it is an author-side
cross-check, not an independent review, and can share convention errors.
General Bloch/branch arguments are in verify_w4_long_wavelength_spectrum.py
and reports/2026-10-26--w4-spectrum-audit.md. All arithmetic is exact SymPy.
"""

import sympy as sp

from certificate_utils import assert_sym_equal, sym_zero
from verify_w4_long_wavelength_spectrum import bloch_step


def swap_sites(length, first, second):
    """Full 2**length qubit permutation; site n is bit n (little-endian)."""
    entries = {}
    for state in range(2**length):
        target = state
        if ((state >> first) & 1) != ((state >> second) & 1):
            target ^= (1 << first) | (1 << second)
        entries[target, state] = 1
    return sp.SparseMatrix(2**length, 2**length, entries)


def ring_step(length, kap, second_sign):
    """Build from full qubit swaps, never from the proposed 2x2 symbol."""
    assert length >= 4 and length % 2 == 0
    assert second_sign in (-1, 1)
    identity = sp.SparseMatrix(sp.eye(2**length))
    step = identity
    for parity, angle in ((0, kap), (1, second_sign*kap)):
        stay = sp.simplify(sp.expand_complex(sp.exp(-sp.I*angle)*sp.cos(angle)))
        hop = sp.simplify(sp.expand_complex(sp.I*sp.exp(-sp.I*angle)*sp.sin(angle)))
        for n in range(parity, length, 2):
            gate = stay*identity+hop*swap_sites(length, n, (n+1) % length)
            # Keep the exact Gaussian-rational entries expanded before passing
            # them to the shared trig/exp identity normalizer.
            step = (gate*step).applyfunc(sp.expand)
    return step


def one_defect_embedding(length):
    return sp.SparseMatrix(2**length, length, {(1 << n, n): 1 for n in range(length)})


def bloch_embedding(length, k):
    entries = {(2*m+sub, sub): sp.expand_complex(sp.exp(sp.I*k*m))
               for m in range(length//2) for sub in (0, 1)}
    return sp.SparseMatrix(length, 2, entries)


def z_operator(length, site):
    return sp.SparseMatrix(2**length, 2**length,
                          {(state, state): 1-2*((state >> site) & 1)
                           for state in range(2**length)})


def main():
    cases = 0
    for length in (4, 6):
        embedding = one_defect_embedding(length)
        vacuum = sp.SparseMatrix(2**length, 1, {(0, 0): 1})
        uniform = embedding*sp.ones(length, 1)
        for kap in (0, sp.pi/4, sp.pi/2):
            for sign in (1, -1):
                step = ring_step(length, kap, sign)
                assert_sym_equal(step.H*step, sp.eye(2**length), "full-qubit unitarity")
                assert_sym_equal(step*vacuum, vacuum, "fixed vacuum")
                assert_sym_equal(step*uniform, uniform, "fixed uniform defect")
                restricted = embedding.H*step*embedding
                assert_sym_equal(step*embedding, embedding*restricted, "sector closure")
                for mode in range(length//2):
                    k = 2*sp.pi*mode/(length//2)
                    plane = bloch_embedding(length, k)
                    expected = bloch_step(k, kap, sign).applyfunc(sp.expand_complex)
                    assert_sym_equal((restricted*plane).applyfunc(sp.expand),
                                     (plane*expected).applyfunc(sp.expand),
                                     "real-space/Bloch agreement")
                if kap == sp.pi/2:
                    for n in range(length):
                        target = (n+(2 if n % 2 == 0 else -2)) % length
                        assert_sym_equal(restricted[:, n], sp.eye(length)[:, target],
                                         "two-register transfer per full step")
                cases += 1
        print(f"[PASS] L={length}: full-qubit circuit, vacuum, sector, all Bloch momenta and SWAP displacement")
    assert cases == 12

    # Project the actual many-qubit Z onto vacuum plus one defect.
    length = 4
    embedding = one_defect_embedding(length)
    vacuum = sp.SparseMatrix(2**length, 1, {(0, 0): 1})
    restricted_basis = vacuum.row_join(embedding)
    amps = sp.Matrix(sp.symbols("b0:5", complex=True))
    norm = (amps.H*amps)[0]
    for n in range(length):
        actual = restricted_basis.H*z_operator(length, n)*restricted_basis
        expected = sp.eye(length+1)
        expected[n+1, n+1] = -1
        assert_sym_equal(actual, expected)
        assert_sym_equal((amps.H*actual*amps)[0], norm-2*sp.conjugate(amps[n+1])*amps[n+1])
    print("[PASS] arbitrary vacuum+one-defect state: <Z_n>=1-2|b_(n+1)|^2/||b||^2")

    # A momentum pi phase by CELL leaves site probabilities unchanged.
    plain = sp.ones(length, 1)/sp.sqrt(length)
    staggered = sp.Matrix([(-1)**(n//2) for n in range(length)])/sp.sqrt(length)
    assert_sym_equal(plain.H*staggered, sp.zeros(1, 1), "distinct orthogonal amplitudes")
    for n in range(length):
        z = embedding.H*z_operator(length, n)*embedding
        assert_sym_equal((plain.H*z*plain)[0], sp.Rational(1, 2))
        assert_sym_equal((staggered.H*z*staggered)[0], sp.Rational(1, 2))
    # The cell-pi state is an eigenstate for both signs at this angle.
    for sign in (1, -1):
        state = embedding*staggered
        eigenvalue = sp.exp(-2*sp.I*sp.pi/4) if sign == 1 else sp.exp(2*sp.I*sp.pi/4)
        assert_sym_equal(ring_step(length, sp.pi/4, sign)*state, eigenvalue*state)
    print("[PASS] k=pi defect phases can have uniform, stationary Z; no forced staggering")

    epsilon = sp.symbols("epsilon", real=True)
    evolved = ring_step(length, sp.pi/4, 1)*embedding[:, 0]
    state = (vacuum+epsilon*evolved)/sp.sqrt(1+epsilon**2)
    for n in range(length):
        z_value = (state.H*z_operator(length, n)*state)[0]
        assert_sym_equal(sp.diff(z_value, epsilon).subs(epsilon, 0), 0)
        assert_sym_equal(z_value,
                         1-2*epsilon**2*sp.conjugate(evolved[1 << n])*evolved[1 << n]/(1+epsilon**2))
    print("[PASS] vacuum+epsilon*defect: Z response starts at order epsilon^2, including after evolution")

    # Equal initial Z profiles can have different next Z: density is not closed.
    plus = sp.Matrix([1, sp.I])/sp.sqrt(2)
    minus = sp.Matrix([1, -sp.I])/sp.sqrt(2)
    z = sp.diag(1, -1)
    full_bond = (1-sp.I)/2*sp.eye(4)+(1+sp.I)/2*swap_sites(2, 0, 1)
    bond = full_bond.extract([1, 2], [1, 2])
    assert_sym_equal((plus.H*z*plus)[0], (minus.H*z*minus)[0])
    after_plus = (plus.H*bond.H*z*bond*plus)[0]
    after_minus = (minus.H*bond.H*z*bond*minus)[0]
    assert not sym_zero(after_plus-after_minus)
    assert_sym_equal(after_plus, -1)
    assert_sym_equal(after_minus, 1)
    # The obstruction also survives the complete two-layer step, not only a bond.
    initial_plus = embedding[:, :2]*plus
    initial_minus = embedding[:, :2]*minus
    step = ring_step(length, sp.pi/4, 1)
    output_plus, output_minus = step*initial_plus, step*initial_minus
    for n, (z_plus, z_minus) in enumerate(zip((1, 0, 0, 1), (0, 1, 1, 0))):
        local_z = z_operator(length, n)
        assert_sym_equal((initial_plus.H*local_z*initial_plus)[0],
                         (initial_minus.H*local_z*initial_minus)[0])
        assert_sym_equal((output_plus.H*local_z*output_plus)[0], z_plus)
        assert_sym_equal((output_minus.H*local_z*output_minus)[0], z_minus)
    print("[PASS] same initial Z, different next Z after a bond AND full step: density is not closed")
    print("\nVERDICT: 12 exact finite-ring controls and Z-observable identities pass; "
          "one-defect amplitude spectrum alone does not establish a linear metric wave.")


if __name__ == "__main__":
    main()
