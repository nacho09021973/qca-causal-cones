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

## Local Weyl/Dirac gate artifacts

The [execution contract](reports/2026-09-14--weyl-dirac-gate-contract.md),
[exact derivation](reports/2026-09-14--weyl-dirac-exact-gate.md), and
[reproducible verification](reports/2026-09-14--weyl-dirac-verification.md)
cover the seven declared standard symbols in d=1,2,3 and their Dirac couplings.
These supply evidence for review; canonical promotion remains a separate
reason-recording commit under `PROJECT_INSTRUCTIONS.md`.
