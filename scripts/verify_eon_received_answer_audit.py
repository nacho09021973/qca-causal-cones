"""Exact algebra controls for the response supplied by the user on 2026-10-27.

Pre-execution scope: audit two proposed shortcuts, NOT construct an alternative
physical vacuum after STOP_THIS_CANDIDATE. (1) Fixed integer E=0 requires
sharp local N=2. Check local fluctuations of a negative-quasienergy Slater
projector for a FOUR-SITE ONE-DIRECTIONAL FREE SLICE of Eon's one-body walk.
This is an algebraic control, NOT the interacting 3D gauge QCA. (2) Test
principal-log selection on two independent modes with known additive energy.
(3) Test the inference that small one-step occupation error controls long time
on a mass-only rotation, NOT on the full Eon circuit. No loop or fitting.
"""

import argparse
import json
from pathlib import Path

import sympy as sp

from certificate_utils import assert_sym_equal


def clean(matrix):
    return matrix.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))


def band_gauss_checks():
    ident = sp.eye(4)
    y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    z = sp.diag(1, -1)
    gamma0 = sp.kronecker_product(y, sp.eye(2))
    gammak = sp.kronecker_product(z, z)
    t = sp.pi/4
    mass = sp.cos(t)*ident - sp.I*sp.sin(t)*gamma0
    qs = [0, sp.pi/2, sp.pi, 3*sp.pi/2]
    omegas = [sp.pi/4, sp.pi/2, 3*sp.pi/4, sp.pi/2]
    projectors, walks = [], []
    for q, omega in zip(qs, omegas):
        walk = clean(mass*(sp.cos(q)*ident + sp.I*sp.sin(q)*gammak))
        hhat = clean((walk.H-walk)/(2*sp.I*sp.sin(omega)))
        p = clean((ident-hhat)/2)  # W=e^{-i omega hhat}; fill energy -omega.
        assert_sym_equal(walk.H*walk, ident, 'slice unitarity')
        assert_sym_equal(p.H, p, 'band Hermiticity')
        assert_sym_equal(p*p, p, 'band projection')
        assert_sym_equal(sp.trace(p), 2, 'two filled modes per momentum')
        eigenphase = sp.cos(omega)+sp.I*sp.sin(omega)
        assert_sym_equal(walk*p, eigenphase*p, 'negative band phase')
        projectors.append(p)
        walks.append(walk)
    pfull = sp.zeros(16)
    wfull = sp.zeros(16)
    for x in range(4):
        for xpos in range(4):
            pblock = sp.zeros(4)
            wblock = sp.zeros(4)
            for q, p, walk in zip(qs, projectors, walks):
                phase = sp.exp(sp.I*q*(x-xpos))/4
                pblock += phase*p
                wblock += phase*walk
            pfull[4*x:4*x+4, 4*xpos:4*xpos+4] = clean(pblock)
            wfull[4*x:4*x+4, 4*xpos:4*xpos+4] = clean(wblock)
    assert_sym_equal(pfull*pfull, pfull, 'full Slater projector')
    assert_sym_equal(wfull*pfull*wfull.H, pfull, 'free slice stationarity')
    records = []
    for x in range(4):
        local = pfull[4*x:4*x+4, 4*x:4*x+4]
        mean = sp.trace(local)
        variance = sp.trace(local-local*local)
        offsite = sum((sp.trace(pfull[4*x:4*x+4, 4*j:4*j+4]
                               *pfull[4*j:4*j+4, 4*x:4*x+4])
                       for j in range(4) if j != x), sp.S.Zero)
        assert_sym_equal(local, ident/2, 'local block')
        assert_sym_equal(mean, 2, 'mean does not enforce Gauss')
        assert_sym_equal(variance, 1, 'nonzero local Gauss variance at E=0')
        assert_sym_equal(offsite, variance, 'projector identity second route')
        variable = sp.symbols('z')
        distribution = sp.Poly((ident-local+variable*local).det(), variable)
        assert_sym_equal(distribution.nth(2), sp.Rational(3, 8), 'sharp N=2 probability')
        records.append(dict(site=x, mean_N=2, variance_N=1,
                            expectation_G_squared_at_E_zero=1,
                            probability_N_equals_2='3/8'))
    # At zero mass, a NONDEGENERATE momentum already differs from local filling.
    pzero = (ident+gammak)/2  # q=pi/2, t=0: W=i gamma_k, omega=pi/2.
    pocc = sp.diag(0, 0, 1, 1)
    mismatch = sp.trace((pzero-pocc).H*(pzero-pocc))
    assert_sym_equal(mismatch, 2, 'small mass does not imply same occupied band')
    # Positive control: sharp on-site two-mode filling satisfies the variance test.
    assert_sym_equal(sp.trace(pocc-pocc*pocc), 0, 'sharp local filling control')
    return dict(scope='four-site one-direction free slice; NOT interacting 3D QCA',
                stationary_free_Slater=True, E_zero_Gauss_pass=False,
                local_records=records, zero_mass_projector_mismatch_squared=2)


def principal_log_checks():
    n1 = sp.diag(0, 1, 0, 1)
    n2 = sp.diag(0, 0, 1, 1)
    h_add = 3*sp.pi*(n1+n2)/4
    h_principal = h_add-2*sp.pi*n1*n2
    u_add = sp.diag(*[sp.exp(-sp.I*h_add[i, i]) for i in range(4)])
    u_principal = sp.diag(*[sp.exp(-sp.I*h_principal[i, i]) for i in range(4)])
    assert_sym_equal(u_add, u_principal, 'same exact unitary')
    assert all(-sp.pi < h_principal[i, i] < sp.pi for i in range(4))
    assert h_add[0, 0] == 0 and all(h_add[i, i] > 0 for i in (1, 2, 3))
    assert h_principal[3, 3] < h_principal[0, 0]
    assert_sym_equal(h_principal[3, 3]-h_principal[1, 1]-h_principal[2, 2],
                     -2*sp.pi, 'principal log not additive')
    # The same four states can encode one fermion in two orbitals at each
    # of two sites. n1,n2 then count HIGH ORBITAL excitation, not charge.
    # Thus the ordering failure also occurs within one sharp Gauss sector.
    encoded_basis = (5, 6, 9, 10)  # (01,01), (10,01), (01,10), (10,10).
    charge1 = sp.diag(*[(mask & 3).bit_count() for mask in range(16)])
    charge2 = sp.diag(*[(mask >> 2).bit_count() for mask in range(16)])
    embedding = sp.zeros(16, 4)
    for col, mask in enumerate(encoded_basis):
        embedding[mask, col] = 1
    assert_sym_equal(embedding.H*embedding, sp.eye(4), 'fixed-charge encoding isometry')
    assert_sym_equal(charge1*embedding, embedding, 'sharp local charge site 1')
    assert_sym_equal(charge2*embedding, embedding, 'sharp local charge site 2')
    return dict(additive_energies_in_pi_units=['0', '3/4', '3/4', '3/2'],
                principal_energies_in_pi_units=['0', '3/4', '3/4', '-1/2'],
                same_unitary=True, same_ground_state=False,
                admits_same_sharp_local_charge_encoding=True,
                induced_cross_term='-2*pi*n1*n2')


def long_time_control():
    a, b = sp.symbols('a b', real=True)
    def rotation(angle):
        return sp.Matrix([[sp.cos(angle), -sp.sin(angle)],
                          [sp.sin(angle), sp.cos(angle)]])
    assert_sym_equal(rotation(a)*rotation(b), rotation(a+b), 'rotation composition')
    records = []
    for steps in (8, 16, 32):
        t = sp.pi/(2*steps)
        occupation_after_n_steps = 2*sp.sin(steps*t)**2
        assert_sym_equal(occupation_after_n_steps, 2, 'finite long-time change')
        records.append(dict(steps=steps, angle=f'pi/{2*steps}',
                            one_step_occupation=f'2*sin(pi/{2*steps})**2',
                            occupation_after_n_steps=2))
    return dict(scope='mass-only control, not full Eon evolution', records=records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = dict(status='RECEIVED_VACUUM_SHORTCUTS_NOT_VALIDATED',
                  slater_gauss=band_gauss_checks(), principal_log=principal_log_checks(),
                  long_time=long_time_control(), evidence='AUTHOR_CHECKED_ONLY')
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('PASS: exact audit controls; no gauge-invariant vacuum construction established.')


if __name__ == '__main__':
    main()
