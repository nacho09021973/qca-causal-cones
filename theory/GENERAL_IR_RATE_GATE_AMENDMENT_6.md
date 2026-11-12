# Amendment 6 to the general infrared operational rate charter

2026-11-12. Drafted by Claude (claude-opus-5-5) after the second sealed
Codex round (`reports/reviews/2026-11-12-bravais-stage1-astra-r2/`), which
gave REPAIR_REQUIRED to Amendment 5. **Status: APPROVED by the user
2026-11-12 («si»); in force from this commit.** The frozen charter (`aa6c5f6`) and Amendments 1–5
are not edited.

## Reason

H2 (as amended by Amendment 5) asks for "a simple dominant eigenvalue".
A simple eigenvalue can share the maximal modulus with another, distinct
eigenvalue. The proofs (Stage 2 leading term, Sec. 5; carrier Stage A,
Secs. 1 and 4) keep one branch at each dominant point and treat the other
eigenvalues as exponentially smaller after normalising by `e^(N Phi_*)`.
The reviewer's example `S_0(p) (+) e^(i beta) S_0(p)`, `beta notin pi Z`,
built from K3's symbol, has at each dominant point two simple eigenvalues
of modulus `e^(Phi_*)` with the same Hessian; the second block is not
small. It is not a counterexample to (T), but it shows that H2′ as
written does not justify discarding the other branches.

The intended reading was strict dominance: the manuscript gives the gap
`e^(2 Phi_*)` for K3 (cited in Stage 0(i)); the diagnostics require
`|lambda_2|/|lambda_1| < 1 - 10^-6` at every dominant point
(`scripts/diagnose_general_ir_rate_polyhedra.py:218-219`,
`scripts/diagnose_general_ir_rate_round2.py:162`).

## Change

H2′ is restated as:

> **H2″.** `rho(S(eta - i xi_*))` attains its maximum `e^(Phi(xi_*))` over
> the torus at finitely many `eta_0`. At each of them exactly one
> eigenvalue `lambda_0` of `S(eta_0 - i xi_*)` has modulus `e^(Phi(xi_*))`;
> it is algebraically simple; and the real Hessian
> `Hess_eta log|lambda_0(eta - i xi_*)|` of that local branch at `eta_0`
> is negative definite (equivalently `Q = Hess_xi log|lambda_0|` positive
> definite there).

Two statements of Amendment 5 are corrected in reading:

- "No proof changes" means: the Gaussian computation is unchanged and its
  declared hypothesis is strengthened to what it uses; the bounds on the
  other branches presuppose the strict dominance stated here. No proof
  under H2 as originally written is claimed.
- H2″ does not identify `Q` with `Hess Phi(xi_*)` in general (when the
  local maximiser moves with `xi`, the local envelope has Hessian
  `Q + Q' Q^(-1) Q'`); that identification is used only for K3, where it
  holds by its structure. H2″ does not replace H8.

## Effect

- K3 satisfies H2″: the second eigenvalue has modulus `e^(-Phi_*)`, and
  `q_t, q_n > 0` by manuscript Lemma 7.1(d) (rederived by the reviewer).
- The H2 columns of the diagnostics are columns of H2″; no label changes.
- Read by reference in the carrier and Bravais charters, as for
  Amendment 5.
- Verdicts unchanged: Stages 1–2 `PROVED_UNDER_FROZEN_CONTRACT` (author,
  PRELIMINARY) under the charter as amended by Amendments 1–6.
