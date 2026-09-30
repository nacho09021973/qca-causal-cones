"""Exact SymPy execution certificate for frozen W12 (commit 2ff88b2).

Run from repository root:
    python3 -B scripts/verify_w12_four_species_metric_universality.py

The contract is not modified. Ranks are taken on the coefficient of g at
first order in species momentum, with z_ar independent real controls. The
four +I nodes decide universality; -I nodes are reported only as diagnostics.
"""

from itertools import product

import sympy as sp

from verify_directional_saturation import PAULI, P1, P2, P3, walk2

PS = (P1, P2, P3)
I2 = sp.eye(2)
I3 = sp.eye(3)
G = sp.symbols('g')
ZV = sp.symbols('z11:14 z21:24 z31:34', real=True)
Z = sp.Matrix(3, 3, ZV)
D = sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]])  # rows are d1,d2,d3, as in W6
DR = [sp.Matrix([1, 0, 0]), sp.Matrix([1, 1, 0]), sp.Matrix([1, 1, 1])]
COMPONENTS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
BITS_PLUS = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
BITS_ALL = list(product((0, 1), repeat=3))


def simp_matrix(m):
    return m.applyfunc(lambda x: sp.trigsimp(sp.expand(x)))


def pauli_symbol(v):
    return sum((v[a] * PAULI[a] for a in range(3)), sp.zeros(2))


def node_subs(bits):
    return dict(zip(PS, [sp.pi * b for b in bits]))


def signs(bits):
    return tuple((-1) ** b for b in bits)


def node_sign(bits):
    return (-1) ** sum(bits)


def frame_from_walk(W, bits):
    s = node_sign(bits)
    at = node_subs(bits)
    assert simp_matrix(W.subs(at) - s * I2) == sp.zeros(2)
    E = sp.zeros(3)
    for i, p in enumerate(PS):
        deriv = s * sp.diff(W, p).subs(at)
        for a in range(3):
            E[a, i] = sp.simplify(sp.trace(deriv * PAULI[a]) / (2 * sp.I))
    E = E.applyfunc(sp.simplify)
    assert E.det() in (sp.S.One, sp.S.NegativeOne)
    return E


def gate_symbol():
    J = sp.zeros(2)
    for a in range(3):
        for r, d in enumerate(DR):
            phase = sum(PS[i] * d[i] for i in range(3))
            J += 2 * Z[a, r] * sp.sin(phase) * PAULI[a]
    return J


def extract_delta_e(W, J, bits, right_order=True):
    """Extract coefficient of g*k from s W0 (1-igJ) or s (1-igJ) W0."""
    s, at = node_sign(bits), node_subs(bits)
    perturb = -sp.I * (W * J if right_order else J * W)
    dE = sp.zeros(3)
    for i, p in enumerate(PS):
        deriv = s * sp.diff(perturb, p).subs(at)
        for a in range(3):
            dE[a, i] = sp.simplify(sp.trace(deriv * PAULI[a]) / (2 * sp.I))
    return dE.applyfunc(sp.simplify)


def metric_coefficient(E, dE):
    # dE already denotes the coefficient of g in delta E.
    return simp_matrix(E.T * dE + dE.T * E)


def vec6(M):
    return sp.Matrix([sp.simplify(M[i, j]) for i, j in COMPONENTS])


def linear_map(rows):
    return sp.Matrix.vstack(*rows)


def kernel_basis(A):
    return A.nullspace()


def main():
    W = walk2()
    J = gate_symbol()
    # U6: first-order gate vanishes at g=0, recovering exactly the input walk.
    Wg0 = W * (I2 - G * sp.I * J)
    assert simp_matrix(Wg0.subs(G, 0) - W) == sp.zeros(2)
    print('[PASS] U6 flat recovery: W_g|_(g=0) = walk2() exactly', flush=True)

    # U1: derive all node frames from the walk, not from a hard-coded table.
    frames = {}
    for bits in BITS_ALL:
        frames[bits] = frame_from_walk(W, bits)
        sig = signs(bits)
        expected = sp.diag(sig[1] * sig[2], -sig[2], 1)
        assert frames[bits] == expected
        print(f'[U1] node {bits}: s={node_sign(bits):+d}, E={tuple(frames[bits].diagonal())}', flush=True)
    print('[PASS] U1 all eight frames match the W11 expression', flush=True)

    # U2: first-order g,k coefficient, derived from the two product orders.
    dEs, dhs = {}, {}
    tau_rows = {}
    for bits in BITS_ALL:
        right = extract_delta_e(W, J, bits, right_order=True)
        reverse = extract_delta_e(W, J, bits, right_order=False)
        assert simp_matrix(right - reverse) == sp.zeros(3)
        # Independently factor the expected node-dependent sign of sin(p*.d_r).
        sig = signs(bits)
        tau = tuple(sp.prod(sig[j] for j, c in enumerate(d) if c) for d in DR)
        tau_rows[bits] = tau
        expected_dE = -2 * Z * sp.diag(*tau) * D
        assert simp_matrix(right - expected_dE) == sp.zeros(3)
        dEs[bits] = right
        dhs[bits] = metric_coefficient(frames[bits], right)
        print(f'[U2] node {bits}: tau_r={tau}; deltaE/g={right}', flush=True)
    print('[PASS] U2 product orders agree at O(g k) at all eight nodes', flush=True)

    # U3: the universality map is the exact 18 x 9 coefficient matrix.
    ref = BITS_PLUS[0]
    phi_rows = []
    for bits in BITS_PLUS[1:]:
        phi_rows.extend(list(vec6(dhs[bits] - dhs[ref])))
    Phi = linear_map([sp.Matrix([sp.diff(x, z) for z in ZV]).T for x in phi_rows])
    assert Phi.shape == (18, 9)
    phi_rank = Phi.rank()
    U_basis = kernel_basis(Phi)
    assert len(U_basis) == 9 - phi_rank
    expected_U = {(1, 0, 0, 0, 0, 0, 0, 0, 0),
                  (0, 0, 0, 0, 1, 0, 0, 0, 0),
                  (0, 0, 0, 0, 0, 0, 0, 0, 1)}
    assert {tuple(v) for v in U_basis} == expected_U
    U_matrix = sp.Matrix.hstack(*U_basis) if U_basis else sp.zeros(9, 0)
    print(f'[U3] rank(Phi)={phi_rank}; dim(U)={len(U_basis)}', flush=True)
    print('[U3] universal control basis (column vectors in z11,...,z33 order):')
    for b in U_basis:
        print(' ', tuple(b), flush=True)

    # U4: metric map of reference species restricted to U.
    Href_rows = [sp.Matrix([sp.diff(x, z) for z in ZV]).T for x in vec6(dhs[ref])]
    Href = linear_map(Href_rows)
    restricted = Href * U_matrix
    metric_rank = restricted.rank()
    assert restricted == sp.Matrix([[-4, 0, 0], [0, 4, 0], [0, 0, -4],
                                    [0, 2, 0], [0, 0, -2], [0, 0, -2]])
    assert 0 <= metric_rank <= 6
    metric_names = ('h11', 'h22', 'h33', 'h12', 'h13', 'h23')
    annihilator = kernel_basis(restricted.T)
    assert len(annihilator) == 6 - metric_rank
    missing_relations = []
    for relation in annihilator:
        terms = [f'({sp.sstr(sp.simplify(c))})*{metric_names[i]}'
                 for i, c in enumerate(relation) if c != 0]
        missing_relations.append(' + '.join(terms) + ' = 0')
    print(f'[U4] rank(metric map restricted to U)={metric_rank}/6', flush=True)
    print('[U4] independent metric constraints (missing directions in Sym^2):', flush=True)
    for relation in missing_relations:
        print(' ', relation, flush=True)
    print('[U4] restricted metric matrix:')
    print(restricted, flush=True)

    # U5: frame rotations are precisely the kernel of the common metric map.
    all_metric = linear_map([sp.Matrix([sp.diff(x, z) for z in ZV]).T
                             for bits in BITS_PLUS for x in vec6(dhs[bits])])
    rotation_basis = kernel_basis(all_metric)
    assert not rotation_basis
    assert all(Phi * b == sp.zeros(Phi.rows, 1) for b in rotation_basis)
    rotation_matrix = sp.Matrix.hstack(*rotation_basis) if rotation_basis else sp.zeros(9, 0)
    assert all_metric * rotation_matrix == sp.zeros(all_metric.rows, rotation_matrix.cols)
    print(f'[U5] common metric-null (frame-rotation) dimension={len(rotation_basis)}', flush=True)
    print('[U5] frame-rotation basis:')
    for b in rotation_basis:
        print(' ', tuple(b), flush=True)

    # Terminal state, as defined in the frozen contract.
    if phi_rank == 0 and metric_rank == 6:
        verdict = 'METRIC_UNIVERSAL_FULL'
    elif phi_rank != 0 and metric_rank == 6:
        verdict = 'UNIVERSAL_SUBFAMILY_FULL_RANK'
    elif metric_rank == 0:
        verdict = 'NON_UNIVERSAL'
    else:
        verdict = 'UNIVERSAL_SUBFAMILY_DEFICIENT'
    assert metric_rank == 6 or bool(missing_relations)
    print(f'VERDICT: {verdict}', flush=True)
    print('Scope: exact first order in g and k; W6 controls and one-particle CJWW (5.15) only.', flush=True)
    print('No claim: emergent gravity, higher orders, -I universality, or dynamics/backreaction of Z.', flush=True)


if __name__ == '__main__':
    main()
