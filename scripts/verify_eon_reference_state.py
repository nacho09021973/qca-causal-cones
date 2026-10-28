"""Exact checks of ONE occupation-product candidate in Eon arXiv:2205.03148v4.

Specification: theory/A_INT_EON_REFERENCE_CHECK.md. No rotor truncation,
full gauge simulation, vacuum construction, IR limit or loop calculation.
The transport routine tracks ONLY deterministic occupations and fluxes on
the specified input. JW phases cannot change these; B is separately checked
to preserve that input ray. Mass amplitudes use exact fermionic gates and an
independent exterior-power construction. The full-step conclusions also use
the analytic occupation-conservation and Taylor-bound arguments in the report.
"""

import argparse
import itertools
import json
from pathlib import Path

import sympy as sp

from certificate_utils import assert_sym_equal


def neighbor(x, axis, amount, length):
    y = list(x)
    y[axis] = (y[axis] + amount) % length
    return tuple(y)


def initial_state(length):
    sites = list(itertools.product(range(length), repeat=3))
    occ = {x: [0, 0, 1, 1] for x in sites}
    flux = {(x, axis): 0 for x in sites for axis in range(3)}
    return sites, occ, flux


def gauss_residuals(occ, flux, length):
    return [sum(occ[x]) - 2 + sum(
        flux[x, a] - flux[neighbor(x, a, -1, length), a]
        for a in range(3)) for x in occ]


def swap_on_site(occ, x, j, k):
    occ[x][j], occ[x][k] = occ[x][k], occ[x][j]


def dressed_swap(occ, flux, x, axis, length, flux_sign=1):
    """Eq.(18) occupation/flux action, j=3 and neighbor k=0.

    Leaving x raises its outgoing E. All omitted K/JW factors are phases
    on this deterministic input. They are NOT discarded in mass amplitudes.
    """
    y = neighbor(x, axis, 1, length)
    leaving, entering = occ[x][3], occ[y][0]
    flux[x, axis] += flux_sign * (leaving - entering)
    occ[x][3], occ[y][0] = entering, leaving


def transport_layer(length, axis, omit_second_swap=False):
    sites, occ, flux = initial_state(length)
    checks = 0
    for x in sites:  # S1, rightmost gate first, Eq.(34).
        swap_on_site(occ, x, 0, 1)
        swap_on_site(occ, x, 1, 2)
    for x in sites:  # Each four-mode bond block in Eq.(27) / Fig.7.
        y = neighbor(x, axis, 1, length)
        dressed_swap(occ, flux, x, axis, length)
        assert not any(gauss_residuals(occ, flux, length))
        swap_on_site(occ, x, 2, 3)
        swap_on_site(occ, y, 0, 1)
        if not omit_second_swap:
            dressed_swap(occ, flux, x, axis, length)
        assert not any(gauss_residuals(occ, flux, length))
        checks += 2
    for x in sites:  # S2.
        swap_on_site(occ, x, 1, 2)
        swap_on_site(occ, x, 2, 3)
    return occ, flux, checks


def transport_checks():
    records = []
    for length in (3, 4):
        for axis in (2, 1, 0):  # kappa, nu, mu: temporal order of Eq.(34).
            occ, flux, checks = transport_layer(length, axis)
            assert all(bits == [0, 0, 1, 1] for bits in occ.values())
            assert all(e == 0 for e in flux.values())
            records.append(dict(L=length, axis=axis, gauss_gate_checks=checks,
                                restored_occupations=True, restored_flux=True))
    # Mutation controls: MUST detect missing transport or wrong flux sign.
    occ, flux, _ = transport_layer(3, 0, omit_second_swap=True)
    assert (any(bits != [0, 0, 1, 1] for bits in occ.values())
            or any(flux.values()))
    _, occ, flux = initial_state(3)
    dressed_swap(occ, flux, (0, 0, 0), 0, 3, flux_sign=-1)
    assert any(gauss_residuals(occ, flux, 3))
    return records


def fock_lift(one_body):
    """Exterior powers with ascending mode order; vacuum amplitude 1."""
    modes = one_body.rows
    result = sp.zeros(2**modes)
    for row in range(2**modes):
        out_modes = [j for j in range(modes) if row & (1 << j)]
        for col in range(2**modes):
            in_modes = [j for j in range(modes) if col & (1 << j)]
            if len(out_modes) == len(in_modes):
                result[row, col] = (one_body.extract(out_modes, in_modes).det()
                                    if out_modes else 1)
    return result


def local_amplitude_checks():
    t = sp.symbols('t', real=True)
    c, s = sp.cos(t), sp.sin(t)
    identity = sp.eye(2)
    fswap = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                       [0, 1, 0, 0], [0, 0, 0, -1]])
    c2 = sp.Matrix([[1, 0, 0, 0], [0, c, -s, 0],
                   [0, s, c, 0], [0, 0, 0, 1]])
    middle = sp.kronecker_product(identity, fswap, identity)
    circuit = middle * sp.kronecker_product(c2, c2) * middle
    # Eq.(31) in ordered one-particle basis 0,1,2,3.
    one_body = sp.Matrix([[c, 0, -s, 0], [0, c, 0, -s],
                          [s, 0, c, 0], [0, s, 0, c]])
    independent = fock_lift(one_body)
    assert_sym_equal(circuit, independent, 'mass circuit vs all exterior powers')
    assert_sym_equal(circuit.H * circuit, sp.eye(16), 'mass unitarity')
    n_total = sp.diag(*[i.bit_count() for i in range(16)])
    assert_sym_equal(circuit * n_total, n_total * circuit, 'mass local Gauss')
    state = circuit[:, 12]  # |1100>_(3,2,1,0).
    norm = sum(sp.conjugate(a) * a for a in state)
    occupation = sum((int(bool(i & 1)) + int(bool(i & 2)))
                     * sp.conjugate(a) * a for i, a in enumerate(state))
    survival = sp.conjugate(state[12]) * state[12]
    assert_sym_equal(norm, 1, 'mass output norm')
    assert_sym_equal(occupation, 2 * s**2, 'low-mode occupation after full DF')
    assert_sym_equal(survival, c**4, 'probability of original local pattern')
    assert_sym_equal(occupation.subs(t, sp.pi/4), 1, 'massive witness')
    assert_sym_equal(survival.subs(t, sp.pi/4), sp.Rational(1, 4), 'survival witness')
    assert_sym_equal(state.subs(t, 0), sp.eye(16)[:, 12], 'zero-mass control')
    # Eq.(33): B has no mixing on a pair which is empty or full.
    p = sp.exp(-sp.I * sp.pi/12)
    q = sp.exp(-sp.I * 7 * sp.pi/12)
    b2 = sp.Matrix([[1, 0, 0, 0],
                    [0, p/sp.sqrt(2), sp.I*q/sp.sqrt(2), 0],
                    [0, sp.I*p/sp.sqrt(2), q/sp.sqrt(2), 0],
                    [0, 0, 0, sp.exp(-2*sp.I*sp.pi/3)]])
    assert_sym_equal(b2.H*b2, sp.eye(4), 'B unitarity')
    b4 = sp.kronecker_product(b2, b2)
    basis = sp.eye(16)[:, 12]
    assert_sym_equal(b4*basis, sp.exp(-2*sp.I*sp.pi/3)*basis, 'B candidate ray')
    return dict(occupation_per_site='2*sin(t)**2',
                original_local_pattern_probability='cos(t)**4',
                t_pi_over_4_occupation_per_site=1,
                t_pi_over_4_original_local_pattern_probability='1/4',
                all_sector_mass_matrix_agreement=True)


def plaquette_flow(x, a, b, length, edges):
    """Oriented boundary of an elementary a,b plaquette, Eq.(12)/(15)."""
    flow = {edge: 0 for edge in edges}
    flow[x, a] += 1
    flow[neighbor(x, a, 1, length), b] += 1
    flow[neighbor(x, b, 1, length), a] -= 1
    flow[x, b] -= 1
    return flow


def magnetic_checks():
    records = []
    for length in (3, 4):
        sites, occ, flux = initial_state(length)
        edges = list(flux)
        targets = set()
        for x in sites:
            for a, b in ((0, 1), (0, 2), (1, 2)):
                loop = plaquette_flow(x, a, b, length, edges)
                for sign in (1, -1):
                    signed = {edge: sign*e for edge, e in loop.items()}
                    assert not any(gauss_residuals(occ, signed, length))
                    key = tuple(signed[edge] for edge in edges)
                    assert any(key) and key not in targets
                    targets.add(key)
        np = 3 * length**3
        assert len(targets) == 2*np
        # Analytic bound: ||D_M''(theta)|| <= (2*N_p)^2, also for
        # ordered noncommuting factors. Taylor remainder <= 2*N_p^2*theta^2.
        theta = sp.Rational(1, 8*np**2)
        remainder = 2 * np**2 * theta**2
        amplitude_lower = theta - remainder
        assert_sym_equal(amplitude_lower, 3*theta/4, 'full magnetic remainder')
        assert amplitude_lower > 0
        assert_sym_equal((sp.Rational(1, 1)/(2*theta))/2 * theta,
                         sp.Rational(1, 4), 'epsilon=1 coupling product')
        records.append(dict(L=length, N_plaquettes=np,
                            orthogonal_one_loop_targets=len(targets),
                            theta=str(theta),
                            target_amplitude_lower_bound=str(amplitude_lower),
                            reference_leakage_probability_lower_bound=str(amplitude_lower**2)))
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = dict(
        candidate='Omega_occ: modes 2,3 filled; integer E=0; f=2',
        status='CANDIDATE_REJECTED_AS_STATIONARY_REFERENCE',
        scope='Eon v4 exact exponential magnetism; periodic L>=3; no rotor truncation',
        transport=transport_checks(), mass=local_amplitude_checks(),
        massless_magnetic=magnetic_checks(),
        exclusions=['not a proof that every Eon vacuum fails',
                    'not a full gauge circuit simulator',
                    'massless failure only in the declared small-angle interval',
                    'no continuum, thermodynamic-spectrum or radiative-speed result'])
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('PASS: Gauss and exact witness checks; candidate FAILS stationarity in declared cases.')


if __name__ == '__main__':
    main()
