# qca-causal-cones

Finite-range quantum cellular automata, microscopic causal bodies, Bernstein bounds, and the emergence of relativistic propagation speeds.

## Project question

The project asks whether a relativistic low-energy propagation speed can be derived from the causal geometry of an underlying finite-range QCA, while keeping distinct three objects that must not be conflated:

1. the microscopic causal body `C_micro`, fixed by locality;
2. the spectral group-velocity envelope `V_grp^max`, fixed by the bands of a specific automaton;
3. the relativistic low-energy speed `c_IR`, fixed by the effective field theory.

The original strong identification `c_IR = maximum microscopic substrate speed` does **not** survive generically in finite-range lattice QCAs for spatial dimension `d >= 2`. The current live question is whether the massless/continuum relativistic speed is instead tied to the inradius of the microscopic causal body.

## Canonical state

Read [`state/CURRENT_STATE.md`](state/CURRENT_STATE.md) before doing new work. It is the single source of truth for project status, gates, rejected claims, and the next allowed calculation.

## Method rule

No result is promoted from exploratory to canonical merely because it fits the current narrative. Every claimed identity must be checked against the exact QCA geometry, exact unitary spectrum, and the appropriate low-energy expansion.

## Verified standard Weyl/Dirac gate

The [execution contract](reports/2026-09-14--weyl-dirac-gate-contract.md),
[exact derivation](reports/2026-09-14--weyl-dirac-exact-gate.md), and
[reproducible verification](reports/2026-09-14--weyl-dirac-verification.md)
cover the seven declared standard symbols in d=1,2,3 and their Dirac couplings.
**STANDARD WEYL/DIRAC EXACT GATE: PASS.** The evidence baseline is `2c7c2c9`;
the [promotion record](reports/2026-09-14--standard-gate-promotion.md) explains
the canonical status change. The original reports retain their historical
pre-promotion wording and provenance.

Massless and continuum inradius matching are verified for the declared
standard family; exact finite-mass matching is rejected for both `c_H` and
`c_{ω^2}`. Generality and inter-species universality remain open. The seven
symbols share three dimension-specific geometries.

## Only next front

[MASSLESS INRADIUS RIGIDITY GATE](theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md):
seek `0 < c_0 < r_in` at fixed neighborhood, causal body, normalization,
unitarity, homogeneity and discrete isotropy. Freeze the admissible class
before solving; a failed search does not establish rigidity.
