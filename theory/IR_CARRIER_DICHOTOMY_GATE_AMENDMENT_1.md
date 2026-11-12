# Amendment 1 to the carrier dichotomy charter — DRAFT

2026-11-12. Drafted by Claude (claude-opus-5-5). **Status: DRAFT; not in
force until approved by the user.** The frozen charter
(`IR_CARRIER_DICHOTOMY_GATE.md`, `36adaa1`) is not edited.

## Reason

The charter (Sec. 2) requires the R1 analogues of H6, H9 and H10 to be
stated in Stage A before use and frozen by amendment. Stage A
(`reports/2026-11-12--ir-carrier-stage-a.md`, Secs. 5–6) shows that the
positivity used under H9(ii) at zero momentum is lost at `eta_k != 0`, so
H9_k must contain a non-vanishing condition.

## Hypotheses for R1, at a chosen dominant point `eta_k != 0` with character trivial on the planes

- **H6_k.** The left dominant eigenvector `f_k` is not in the complex span
  of the left dominant eigenvectors at the other dominant points with
  trivial character.
- **H9_k.** Either H9(i) (`1, u.w_A, u.w_B` rationally independent), or
  H9(ii) (`theta^A_N = theta^B_N`, `u.w_A` irrational) together with
  `mu_k != 0`, where
  `mu_k = sum_n int exp(-zeta^T S_{C_k} zeta/2) g^A(2 pi n; sigma) g^B(-2 pi n; sigma) d^m zeta`,
  `sigma = kappa + i phi`, as defined in Stage A, Sec. 5.
- **H10_k.** `e_k` is not a complex multiple of `R~ = R_0(w_B)` (with
  H6_k, `M_B` then rotates the coefficient `c_k`).

Together with H1–H3, H5, H7, H8 and H2 at the dominant set.

## Effect

Stage A's conclusion becomes `PROVED_UNDER_FROZEN_CONTRACT` (as amended).
`mu_k` is a finite, computable quantity; its numerical value for the R1
walks of the diagnostic is reported separately as a diagnostic, not as a
verification of the hypothesis.
