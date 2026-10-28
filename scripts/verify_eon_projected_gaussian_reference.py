"""Permanent algebra controls for a Gauss-projected Gaussian reference.

Fixed specification: theory/A_INT_EON_PROJECTED_GAUSSIAN_REFERENCE.md.
This does NOT diagonalize the full interacting QCA, compute its vacuum or
approximate its rotor by a finite cyclic group. The projected state is given
analytically; an author-written Fourier/Jensen lemma tests stationarity.
These checks validate ingredients, NOT an independent proof of that lemma.
"""

import argparse
import collections
import json
from pathlib import Path

import sympy as sp

from certificate_utils import assert_sym_equal
from verify_eon_reference_state import initial_state, neighbor, gauss_residuals, plaquette_flow


def dirac_seed_checks():
    x = sp.Matrix([[0, 1], [1, 0]])
    y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    z = sp.diag(1, -1)
    ident = sp.eye(4)
    gamma0 = sp.kronecker_product(y, sp.eye(2))
    gammas = [sp.kronecker_product(z, y), sp.kronecker_product(z, x),
              sp.kronecker_product(z, z)]
    mass = sp.symbols('m', positive=True)
    sines = sp.symbols('s0:3', real=True)
    h = mass*gamma0 - sum((s*g for s, g in zip(sines, gammas)), sp.zeros(4))
    energy2 = mass**2 + sum(s*s for s in sines)
    assert_sym_equal(h.H, h, 'auxiliary Dirac Hermiticity')
    assert_sym_equal(h*h, energy2*ident, 'auxiliary gapped spectrum')
    energy = sp.sqrt(energy2)
    p = (ident-h/energy)/2
    assert_sym_equal(p*p, p, 'negative energy projection')
    assert_sym_equal(p.H, p, 'projection Hermiticity')
    assert_sym_equal(sp.trace(p), 2, 'rank two per momentum')
    assert_sym_equal(h*p, -energy*p, 'negative additive energy selection')
    # At L=3 there are nonzero momenta: this seed is not local fixed filling.
    p0 = p.subs(dict(zip(sines, (0, 0, 0))))
    p1 = p.subs(dict(zip(sines, (sp.sqrt(3)/2, 0, 0))))
    assert_sym_equal(sp.trace(gammas[0]*p0), 0, 'zero-momentum seed component')
    assert_sym_equal(sp.trace(gammas[0]*p1),
                     sp.sqrt(3)/sp.sqrt(mass**2+sp.Rational(3, 4)),
                     'nonconstant occupied subspace')
    return dict(criterion='auxiliary additive Dirac Hamiltonian; NOT log(U)',
                rank_per_momentum=2, number_of_filled_modes='2*V',
                gapped_for_positive_mass=True, nonconstant_projector=True)


def tree_flow(length, charge):
    """Integer solution div E=charge on a connected periodic graph."""
    sites, _, flux = initial_state(length)
    assert sum(charge.values()) == 0
    root = sites[0]
    parent = {root: None}
    order = [root]
    for site in order:
        for axis in range(3):
            for sign in (1, -1):
                dest = neighbor(site, axis, sign, length)
                if dest not in parent:
                    parent[dest] = (site, axis, sign)
                    order.append(dest)
    subtotal = dict(charge)
    for child in reversed(order[1:]):
        par, axis, sign = parent[child]
        current = subtotal[child]
        if sign == 1:  # parent -> child is the positive canonical edge.
            flux[par, axis] -= current
        else:
            flux[child, axis] += current
        subtotal[par] += current
    assert subtotal[root] == 0
    return flux


def divergence(flux, sites, length):
    return {site: sum(flux[site, a]-flux[neighbor(site, a, -1, length), a]
                      for a in range(3)) for site in sites}


def gauss_solvability_checks():
    records = []
    for length in (3, 4):
        sites, _, _ = initial_state(length)
        configs = []
        unit_pair = {x: 0 for x in sites}
        unit_pair[sites[0]] = 1
        unit_pair[sites[-1]] = -1
        configs.append(unit_pair)
        extreme = {x: 0 for x in sites}
        half = len(sites)//2
        for site in sites[:half]:
            extreme[site] = 2
        for site in sites[half:2*half]:
            extreme[site] = -2
        configs.append(extreme)
        for charge in configs:
            flow = tree_flow(length, charge)
            assert divergence(flow, sites, length) == charge
            qplus = sum(max(q, 0) for q in charge.values())
            assert max(abs(e) for e in flow.values()) <= qplus
            records.append(dict(L=length, transported_positive_charge=qplus,
                                exact_divergence_match=True))
    return records


def infinite_loop_control():
    """Two charge patterns and an infinite loop coordinate: algebra control.

    NOT the complete 3D Slater-projected state. Partial sums have rigorous
    tails; no cutoff is substituted into the QCA evolution.
    """
    length = 3
    sites, occ, flux = initial_state(length)
    source = sites[0]
    sink = neighbor(source, 0, 1, length)
    loop = plaquette_flow(source, 0, 1, length, list(flux))
    assert divergence(loop, sites, length) == {x: 0 for x in sites}
    for sign in (1, -1):
        bits = {site: list(n) for site, n in occ.items()}
        if sign == 1:
            bits[source][3] = 0
            bits[sink][0] = 1
        else:
            bits[source][0] = 1
            bits[sink][3] = 0
        base = dict(flux)
        base[source, 0] = sign
        assert not any(gauss_residuals(bits, base, length))
        n = sp.symbols('n', integer=True)
        energy = sum((base[e]+n*loop[e])**2 for e in flux)
        assert_sym_equal(energy, 4*n**2+2*sign*n+1, 'loop electric energy')
    records = []
    for cutoff in (0, 1, 2):
        partial_plus = sum((sp.Rational(1, 4)**(4*n*n+2*n+1)
                            for n in range(-cutoff, cutoff+1)), sp.S.Zero)
        partial_minus = sum((sp.Rational(1, 4)**(4*n*n-2*n+1)
                             for n in range(-cutoff, cutoff+1)), sp.S.Zero)
        assert_sym_equal(partial_plus, partial_minus, 'opposite-charge norm equality')
        assert partial_plus >= sp.Rational(1, 4)
        # E(n)>=2*n^2+1 for |n|>=1; ratios of 16^(-n^2) bound each tail.
        tail = sp.Rational(1, 2)*sp.Rational(1, 16)**((cutoff+1)**2) / (
            1-sp.Rational(1, 16)**(2*cutoff+3))
        records.append(dict(cutoff=cutoff, unnormalized_norm_lower=str(partial_plus),
                            unnormalized_tail_upper=str(tail),
                            normalized_tail_probability_upper=str(tail/partial_plus)))
    return dict(scope='two-configuration, one-loop control; not full projected 3D state',
                beta='log(2)', Gauss_all_integer_loop_numbers=True,
                matter_reduced_purity='1/2', partial_sum_controls=records)


def fourier_obstruction_ingredients():
    beta = sp.symbols('beta', positive=True)
    number, logradius = sp.symbols('n s', real=True)
    assert_sym_equal(-beta*number**2+logradius*number,
                     -beta*(number-logradius/(2*beta))**2+logradius**2/(4*beta),
                     'Gaussian generating-function growth')
    counts = []
    for length in (3, 4):
        sites, _, flux = initial_state(length)
        edge = (sites[0], 0)
        harmonics = collections.Counter()
        for site in sites:
            for a, b in ((0, 1), (0, 2), (1, 2)):
                flow = plaquette_flow(site, a, b, length, list(flux))
                harmonics[flow[edge]] += 1
                harmonics[-flow[edge]] += 1
        assert harmonics[1] == 4 and harmonics[-1] == 4
        counts.append(dict(L=length, z_coefficient_at_other_angles_zero=4,
                           inverse_z_coefficient_at_other_angles_zero=4))
    # Finite-Laurent special case, checked independently of the analytic
    # Jensen argument: the polynomial identity has incompatible top degrees.
    zvar = sp.symbols('z', nonzero=True)
    a, theta = sp.symbols('a theta', nonzero=True)
    for p, q in ((0, 0), (2, 3), (-2, -1), (-3, 4)):
        f = zvar**p
        g = zvar**q
        residual = f*sp.diff(g, zvar)-g*sp.diff(f, zvar)-sp.I*theta*(a-zvar**-2)*f*g
        shifted = sp.expand(residual*zvar**(-p-q))
        assert_sym_equal(shifted.coeff(zvar, 0), -sp.I*theta*a,
                         'uncancellable leading Laurent coefficient')
    # A control outside the Gaussian-tail growth class can cancel the kick.
    # This is an inverse-kick wavefunction identity, NOT a QCA eigenstate.
    h = zvar+1/zvar
    f = sp.exp(-sp.I*theta*h)
    assert_sym_equal(-sp.diff(f, zvar)-sp.I*theta*sp.diff(h, zvar)*f, 0,
                     'inverse-kick identity outside the growth hypothesis')
    radius = sp.symbols('R', positive=True)
    assert_sym_equal((-sp.I*h).subs(zvar, sp.I*radius), radius-1/radius,
                     'inverse kick has linear-radius logarithmic growth')
    return dict(Gaussian_growth_identity=True, magnetic_harmonic_counts=counts,
                universal_stationarity_obstruction='author-written Fourier/Jensen proof in report',
                outside_Gaussian_class_inverse_kick_control=True,
                not_a_numerical_proof_of_complex_analysis=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = dict(
        status='PROJECTED_GAUSSIAN_GAUSS_PASS_STATIONARITY_FAIL',
        accepted_physical_vacuum=False,
        construction='P_G (FS_D tensor electric heat kernels), normalized; beta=log(2)',
        model='Eon v4 original U, exact magnetic exponential, untruncated integer rotors',
        seed=dirac_seed_checks(), integer_Gauss=gauss_solvability_checks(),
        infinite_support_control=infinite_loop_control(),
        obstruction_ingredients=fourier_obstruction_ingredients(),
        scope='finite volume L>=3; magnetic angle nonzero; Gaussian electric tails',
        evidence='AUTHOR_ANALYTIC_PROOF_AND_EXACT_INGREDIENT_CHECKS / INDEPENDENT_REVIEW_PENDING')
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('PASS: construction ingredients; projected Gaussian reference FAILS stationarity by stated analytic lemma.')


if __name__ == '__main__':
    main()
