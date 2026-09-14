# PROJECT_INSTRUCTIONS

## 1. Scope

This repository studies finite-range quantum cellular automata (QCA), their microscopic causal geometry, spectral propagation speeds, and relativistic low-energy limits.

The central scientific question is not whether locality gives a finite propagation bound; that is background. The live questions are:

- **A — IR universality:** why different low-energy species would share one relativistic causal cone;
- **B* — inradius matching:** whether, and under what conditions, the relativistic massless/continuum speed is selected by the inradius of the microscopic causal body.

Do not silently broaden the project to causal sets, random lattices, interacting QCA, quantum gravity, or other substrate classes before the current gate is closed.

## 2. Canonical authority

`state/CURRENT_STATE.md` is the single source of truth for project status.

If another file conflicts with it, `CURRENT_STATE.md` wins until explicitly revised by a new commit that records the reason.

## 3. Mandatory distinctions

Never use `v_max` without qualification. Keep distinct:

- `C_micro`: microscopic causal body fixed by locality;
- `V_causal^max`: maximum directional support of `C_micro`;
- `V_grp^max`: maximum group velocity actually realized by a QCA spectrum;
- `c_IR`: relativistic speed parameter of the low-energy effective theory.

For finite-range lattice QCA in more than one spatial dimension, treat `C_micro` as a convex body, not as a scalar speed.

## 4. Evidence levels

Every nontrivial claim must be tagged mentally as one of:

- **ESTABLISHED:** proved in-repo or directly supported by a checked primary source;
- **SUPPORTED:** consistent with checked examples but not established generally;
- **PRELIMINARY:** derivation or calculation not yet independently rechecked;
- **OPEN:** live conjecture/question;
- **REJECTED:** contradicted by proof, geometry, or explicit counterexample.

Do not promote PRELIMINARY to ESTABLISHED because it supports the narrative.

## 5. Method

Prefer exact algebra and geometry before numerical fitting.

For any candidate equality involving propagation speeds:

1. define the microscopic neighborhood and its normalization;
2. compute `C_micro = conv(N)` with physical scale restored only after the dimensionless geometry is clear;
3. compute its support function and inradius;
4. compute the exact Bloch unitary and eigenphases;
5. derive the appropriate low-energy Hamiltonian or dispersion expansion;
6. compare quantities only after checking that their definitions match.

For massive sectors, do not identify `c_IR` with `|∇ω(0)|`. At finite lattice mass, also do not assume that the coefficient extracted from `ω^2` is automatically identical to the coefficient of the linear spatial term in the interpolating Hamiltonian; lattice corrections can spoil that equivalence.

## 6. Novelty discipline

The scalar/trigonometric Bernstein derivative bound and its classical equality theory are prior art. Do not claim them as novel.

Potential novelty, if any, must lie in QCA-specific structural statements, causal-body geometry, exact matching/non-matching results, or new classification theorems that survive prior-art search.

## 7. Current gate

No new substrate class or model search until the frozen Weyl/Dirac battery is completed:

- dimensions `d = 1, 2, 3` where the Pavia family is defined;
- massless Weyl geometry and `c_IR`;
- massive Dirac extension;
- explicit comparison of `r_in(C_micro)`, the Hamiltonian spatial coefficient, and the coefficient inferred from `ω^2`;
- exact statement of which equalities hold, fail, or only emerge in the continuum/small-mass limit.

Negative results are valid project outcomes.