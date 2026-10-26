"""Permanent operator derivations shared by the W3/W5/W6 certificates.

Scope: first g-jet of the transport substep on a separable uniform background,
not the complete Floquet logarithm or an entangled-background closure.
"""

import sympy as sp

from certificate_utils import assert_sym_equal
from verify_directional_saturation import PAULI, P1, P2, P3, walk2

DIRECTIONS = ((1, 0, 0), (1, 1, 0), (1, 1, 1))
MOMENTA = (P1, P2, P3)
ZERO = dict.fromkeys(MOMENTA, 0)
X, Y, Z = PAULI


def current_symbol(a, r):
    """Fourier transform of i(|x+d><x|-|x><x+d|) tensor sigma_a."""
    phase = sum(p*d for p, d in zip(MOMENTA, DIRECTIONS[r]))
    forward = sp.exp(-sp.I*phase)
    backward = sp.conjugate(forward)
    return sp.I*(forward-backward)*PAULI[a]


def transport_jet(weights, g):
    """Differentiate each local exponential at g=0, then sum the layer jets.

    Matching parities partition all edges. The derivative of any ordered
    product of identity-valued gates at zero is the sum of their derivatives.
    Thus the first jet is translation invariant even though each parity layer
    separately has a doubled cell. weights maps (Pauli row, direction) to mean Z.
    """
    generator = sp.zeros(2)
    for (a, r), weight in weights.items():
        generator += weight*current_symbol(a, r)
    interaction = sp.eye(2)-sp.I*g*generator
    step = interaction*walk2()
    # Extract Pauli coefficients from the differentiated STEP, not a defined E.
    E = sp.Matrix(3, 3, lambda a, i: sp.simplify(
        -sp.I*sp.trace(PAULI[a]*sp.diff(step, MOMENTA[i]).subs(ZERO))/2))
    H_transport = sp.I*sp.diff(interaction, g).subs(g, 0)*g
    return E, H_transport


def edge_current(a):
    """Two endpoints plus a spectator: J^2=A, including the zero eigenspace."""
    hop = sp.zeros(3)
    hop[1, 0], hop[0, 1] = 1, 0
    spatial = sp.I*(hop-hop.H)
    projector = sp.diag(1, 1, 0)
    return (sp.kronecker_product(spatial, PAULI[a]),
            sp.kronecker_product(projector, sp.eye(2)))


def current_kick_checks(a, eta):
    """Derive the exact local gate from J^3=J; return its Heisenberg slope."""
    J, A = edge_current(a)
    Im, Ig = sp.eye(J.rows), sp.eye(2)
    assert_sym_equal(J.H, J, "current Hermiticity")
    assert_sym_equal(J*J, A, "J^2=A including spectator")
    assert_sym_equal(J*A, J, "J^3=J")
    # Exact exponential of Y tensor J using its eigenvalues 0,+1,-1.
    R = sp.kronecker_product(Ig, Im+(sp.cos(eta)-1)*A) \
        -sp.I*sp.sin(eta)*sp.kronecker_product(Y, J)
    assert_sym_equal(R.H*R, sp.eye(R.rows), "kick unitarity")
    assert_sym_equal(R.subs(eta, 0), sp.eye(R.rows), "zero kick")
    assert_sym_equal(sp.diff(R, eta).subs(eta, 0),
                     -sp.I*sp.kronecker_product(Y, J), "kick generator")
    obs = sp.kronecker_product(Z, Im)
    rotated = R.H*obs*R
    expected = sp.kronecker_product(Z, Im+(sp.cos(2*eta)-1)*A) \
        -sp.sin(2*eta)*sp.kronecker_product(X, J)
    assert_sym_equal(rotated, expected, "full current-conditioned Z rotation")
    slope = sp.diff(rotated, eta).subs(eta, 0)
    assert_sym_equal(slope, -2*sp.kronecker_product(X, J), "source slope")
    return J, A, R, slope
