"""Exact finite certificate for theory/COUPLING_MAP_SIGNALING_WITNESS.md.

Run: python3 scripts/verify_signaling_witness.py
No floating point, fitted scaling, state search or optimization of trace distance.
The declared walk symbol is reused; Laurent extraction and convolution below
use SymPy exact arithmetic rather than the older complex-number kernel helper.
"""

import sympy as sp

from verify_directional_saturation import Z, laurent, walk2


ORIGIN = (0, 0, 0)
BOB = (2, 2, 2)
AXIAL = (3, 0, 0)
DOWN = sp.Matrix([0, 1])
CHECKS = 0


def verify(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1
    print(f"[PASS] {message}")


def exact_blocks():
    blocks = {}
    symbol = walk2()
    shift = sp.prod(Z)
    for i in range(2):
        for j in range(2):
            poly = sp.Poly(sp.expand(laurent(symbol[i, j]) * shift), *Z)
            for powers, coefficient in poly.terms():
                if coefficient == 0:
                    continue
                displacement = tuple(power - 1 for power in powers)
                blocks.setdefault(displacement, sp.zeros(2))[i, j] = coefficient
    return blocks


def square_kernel(blocks):
    result = {}
    for x, left in blocks.items():
        for z, right in blocks.items():
            displacement = tuple(a + b for a, b in zip(x, z))
            result[displacement] = result.get(displacement, sp.zeros(2)) + left * right
    return {x: matrix.applyfunc(sp.simplify) for x, matrix in result.items()
            if matrix != sp.zeros(2)}


def phase_choice(state):
    return {x: (-vector if x == ORIGIN else vector) for x, vector in state.items()}


def evolve(state, kernel):
    # alpha_t(P_y) = W^t P_y W^{t dagger}; states evolve by W^{t dagger}.
    output = {}
    for x, vector in state.items():
        for displacement, matrix in kernel.items():
            b = tuple(a - d for a, d in zip(x, displacement))
            output[b] = output.get(b, sp.zeros(2, 1)) + matrix.H * vector
    return {x: vector.applyfunc(sp.simplify) for x, vector in output.items()
            if vector != sp.zeros(2, 1)}


def norm_squared(state):
    return sp.simplify(sum((vector.H * vector)[0] for vector in state.values()))


def reduced_state(state, site):
    # Basis: vacuum, up, down, up-down. Global particle number is exactly one.
    vector = state.get(site, sp.zeros(2, 1))
    probability = sp.simplify((vector.H * vector)[0])
    rho = sp.zeros(4)
    rho[0, 0] = 1 - probability
    rho[1:3, 1:3] = vector * vector.H
    return rho.applyfunc(sp.simplify)


def main():
    blocks = exact_blocks()
    kernel = square_kernel(blocks)
    verify(all(not entry.has(sp.Float) for matrix in kernel.values() for entry in matrix),
           "all two-step kernel entries are exact")
    k_alice = kernel[tuple(-v for v in BOB)]
    k_bob = kernel[ORIGIN]
    verify(k_alice == sp.diag(0, sp.Rational(1, 16)),
           "K_2(0,y) = diag(0,1/16)")
    verify(k_bob == -sp.Rational(3, 4) * sp.eye(2),
           "K_2(y,y) = -3 I/4")
    verify(sum(v * v for v in BOB) > 2**2
           and max(abs(v) for v in BOB) == 2 and k_alice != sp.zeros(2),
           "Bob is outside the emergent ball and on the populated microscopic boundary")

    psi = {ORIGIN: DOWN / sp.sqrt(2), BOB: DOWN / sp.sqrt(2)}
    verify(norm_squared(psi) == 1, "common pre-choice state is normalized")
    # Alice's full two-mode Fock gate and Bob's full Fock measurement.
    gate = sp.diag(1, -1, -1, 1)
    parity = sp.diag(1, -1, -1, 1)
    effect = sp.diag(0, 1, 1, 1)
    verify(gate.H * gate == sp.eye(4) and gate * parity == parity * gate,
           "Alice gate is unitary and even on the full local Fock space")
    verify(effect**2 == effect and effect.H == effect and effect * parity == parity * effect,
           "Bob non-vacuum event is an even projection (norm one)")

    outputs = [evolve(psi, kernel), evolve(phase_choice(psi), kernel)]
    verify(all(norm_squared(state) == 1 for state in outputs),
           "both evolved global states have exact unit norm")
    amplitudes = [state[BOB] for state in outputs]
    verify(amplitudes == [-11 * DOWN / (16 * sp.sqrt(2)),
                          -13 * DOWN / (16 * sp.sqrt(2))],
           "Bob amplitudes are -11 down/(16 sqrt(2)) and -13 down/(16 sqrt(2))")
    rhos = [reduced_state(state, BOB) for state in outputs]
    probabilities = [sp.trace(effect * rho) for rho in rhos]
    verify(probabilities == [sp.Rational(121, 512), sp.Rational(169, 512)],
           "p_0 = 121/512; p_1 = 169/512")
    verify(all(sp.trace(rho) == 1 and rho.H == rho
               and all(eigenvalue >= 0 for eigenvalue in rho.eigenvals()) for rho in rhos),
           "Bob reduced states are normalized positive density matrices")
    witness = abs(probabilities[1] - probabilities[0])
    verify(witness == sp.Rational(3, 32) and witness > 0,
           "Delta p_B = 3/32 > 0, hence D >= 3/32 by the effect bound")
    cross = (DOWN.H * k_alice * k_bob.H * DOWN)[0]
    verify(cross == -sp.Rational(3, 64) and witness == 2 * abs(sp.re(cross)),
           "witness agrees with the exact interference cross term")

    localized = {ORIGIN: DOWN}
    local_outputs = [evolve(localized, kernel), evolve(phase_choice(localized), kernel)]
    verify(local_outputs[1] == {x: -v for x, v in local_outputs[0].items()},
           "Alice-localized control changes only a global phase: no observable can signal")
    # Dephasing the initial spatial superposition is the equal mixture of these
    # two localized preparations. Each density matrix is invariant under U_1.
    dephased_rhos = []
    for apply_phase in (False, True):
        mixture = sp.zeros(4)
        for site in (ORIGIN, BOB):
            component = {site: DOWN}
            if apply_phase:
                component = phase_choice(component)
            mixture += reduced_state(evolve(component, kernel), BOB) / 2
        dephased_rhos.append(mixture)
    verify(dephased_rhos[0] == dephased_rhos[1],
           "removing spatial coherence gives identical Bob states for this phase protocol")
    verify(kernel.get(tuple(-v for v in AXIAL), sp.zeros(2)) == sp.zeros(2),
           "axial K_2(0,(3,0,0)) is exactly zero")
    verify(reduced_state(outputs[0], AXIAL) == reduced_state(outputs[1], AXIAL),
           "axial control: full reduced states coincide for this preparation")
    print(f"\n{CHECKS}/{CHECKS} exact checks passed. Existence witness only; no optimum or asymptotic claim.")


if __name__ == "__main__":
    main()
