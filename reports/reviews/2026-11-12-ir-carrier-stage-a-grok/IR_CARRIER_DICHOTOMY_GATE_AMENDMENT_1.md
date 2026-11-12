# Amendment 1 to the carrier dichotomy charter

2026-11-12. Drafted by Claude (claude-opus-5-5). **Status: APPROVED by the
user 2026-11-12 (choice «Aprobar y mandar a Grok», on the revised text);
in force from this commit.** The frozen charter
(`IR_CARRIER_DICHOTOMY_GATE.md`, `36adaa1`) is not edited.

## Reason

The charter (Sec. 2) requires the R1 analogues of H6, H9 and H10 to be
stated in Stage A before use and frozen by amendment. Stage A
(`reports/2026-11-12--ir-carrier-stage-a.md`, Secs. 5–6) shows that the
positivity used under H9(ii) at zero momentum is lost at `eta_k != 0`, so
H9_k must contain a non-vanishing condition.

## Hypotheses for R1, at a chosen dominant point `eta_k != 0` with character trivial on the planes

- **H6_k (isolation or carrier group).** Either (i) the left dominant
  eigenvector `f_k` is not in the complex span of the left dominant
  eigenvectors at the other trivial-character dominant points; or (ii) for
  the group `G` of trivial-character dominant points whose contributions
  cannot be separated from that of `eta_k`, and every pair `i != j` in `G`,
  the numbers `1`, `u.w_A` and `(psi_i - psi_j)/(2 pi)` are rationally
  independent (the other trivial points being isolated as in (i)).
- **H9_k.** Either H9(i) (`1, u.w_A, u.w_B` rationally independent), or
  H9(ii) (`theta^A_N = theta^B_N`, `u.w_A` irrational) together with
  `mu_j != 0` for `j = k` (case (i) of H6_k) or for every `j in G`
  (case (ii)), where
  `mu_j = sum_n int exp(-zeta^T S_{C_j} zeta/2) g^A(2 pi n; sigma_j) g^B(-2 pi n; sigma_j) d^m zeta`,
  `sigma_j = kappa + i phi_j`, as defined in Stage A, Sec. 5.
- **H10_k.** `e_k` is not a complex multiple of `R~ = R_0(w_B)` (so that
  `M_B` rotates the coefficient).

Together with H1–H3, H5, H7, H8 and H2 at the dominant set.

## Effect

Stage A's conclusion becomes `PROVED_UNDER_FROZEN_CONTRACT` (as amended).
Case (ii) of H6_k was added after the R1 diagnostic showed that in the
three R1 walks the two dominant carriers have dependent eigenvectors on
both sides (`reports/2026-11-12--ir-carrier-r1-diagnostic.json`); it is
declared as written after that output.
`mu_k` is a finite, computable quantity; its numerical value for the R1
walks of the diagnostic is reported separately as a diagnostic, not as a
verification of the hypothesis.
