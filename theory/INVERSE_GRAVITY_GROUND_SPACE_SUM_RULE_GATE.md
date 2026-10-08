# IG-S2 — true-ground-space sum-rule audit

Date: 2026-10-08

Branch: `research/inverse-gravity-design`.
Authorization: user instruction to use information from the true ground space.
Parent: fixed `INVERSE_GRAVITY_CURVATURE_PROBE_GATE.md`.
Initial status: `OPEN`; freeze before auxiliary computation.

## 1. Fixed scope

Keep the full q=3 N-type H_L, positive comparable couplings independent of L,
even periodic L>=4, and exactly the B_+/B_cross curvature pair already fixed.
No new model, trial vacuum or replacement of H_N by H_U is permitted.
P_0 denotes the complete minimum-energy projector of H_L and
rho_0=P_0/Tr(P_0). Existence in finite dimension does not imply knowledge of
its rank, matrix elements or correlations.

## 2. Mathematical questions

1. Derive the consequences of exact realness of H_L in the momentum basis for
   F and D evaluated in rho_0. Determine whether D=2F is valid and distinguish
   it from statements about an arbitrary pure ground vector.
2. Use translation invariance and support of H_J to express axial D(p) through
   five finite-range coefficient matrices C_n(L), n=-2,-1,0,1,2.
   Derive exact polynomial and quantitative finite-volume conditions sufficient
   for a vacuum p^4 bound. Do not substitute tangent coefficients for C_n.
3. Express the zero-envelope-momentum first spectral moment using the complete
   P_0 and determine what it would mean for it to vanish.
4. Audit whether a rank-two matrix averaged over a degenerate ground space
   alone implies two distinct physical excited states.

All scalar/vector constraints and source conventions remain unchanged.
No claim about a limiting vacuum is allowed without a convergence argument.
Only expectations in an actual H_L ground density satisfy the ground-state
identities; no explicit value for an unknown expectation may be invented.

## 3. Permanent auxiliary checks

Add `scripts/verify_inverse_gravity_ground_sum_rules.py` after this file is
committed. Check only:

- support geometry giving axial double-commutator degree at most two;
- the exact five-coefficient p^4 polynomial identity and its uniqueness;
- D=2F and the averaged-rank counterexample in a declared auxiliary three-level
  real Hamiltonian. This is a check of the general identity and logical
  inference, not a substitute Hamiltonian or N-type ground calculation.

No mass diagonalization, variational scan or provider review is admitted.
Retain exact output after all checks pass; failed attempts must be preserved.
Analytic proofs, not finite extrapolations, support all-L statements.

## 4. Verdicts

`GROUND_SPACE_SUM_RULE_ANALYTIC_PASS_AUTHOR_SIDE` for the stated identities.
`AVERAGED_RANK_TWO_MODE_INFERENCE_FAIL` if the three-level example refutes
the inference without degeneracy control.
`NTYPE_GROUND_MOMENTS_UNKNOWN / TENSOR_SPECTRAL_GATE_OPEN` unless actual
uniform bounds for the true N-type expectations are proved.
No publication or scientific promotion follows automatically.
