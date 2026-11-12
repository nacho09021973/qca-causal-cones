# Amendment 5 to the general infrared operational rate charter

2026-11-12. Drafted by Claude (claude-opus-5-5) on the user's instruction
(«si a las dos», answering the proposal to draft an amendment clarifying
H2). **Status: DRAFT; not in force until the user approves it.** The
frozen charter (`aa6c5f6`) and Amendments 1–4 are not edited.

## Reason

The sealed Codex review of the Bravais Stage 1
(`reports/reviews/2026-11-12-bravais-stage1-astra/informe_astra.md`,
notes on B1) observes that H2 as written asks for a "non-degenerate
Hessian of `log lambda`", while the proofs use more: that

    Q = Hess_xi log|lambda_0|   is positive definite at the dominant point.

With `log lambda` holomorphic in `p = eta - i xi` and `H` its complex
Hessian, `Hess_eta log|lambda| = Re H` and `Hess_xi log|lambda| = -Re H`.
A non-degenerate `H` does not make `Re H` negative definite; maximality in
`eta` gives only semidefiniteness. The reviewer's one-variable germ
`f(t) = f(0) + i v t - i t^2 - t^4` has a strict maximum of `Re f` at `0`
and `f''(0) = -2i != 0`, but no quadratic Gaussian decay. The Grok review
of Stages 1–2 did not raise this.

Where the stronger property is used:

- Stage 0(i) (`reports/2026-11-12--general-ir-rate-stages-0-1.md`): K3's
  `I` is differentiable at `v_*` because `Hess Phi(xi_*) = Q` is positive
  definite (manuscript Lemma 7.1(d)).
- Stage 2 progress, Sec. 3.1: "`Q = Hess_xi log|lambda_0|` positive
  definite (H2, pluriharmonicity …)" — the inference this amendment
  repairs.
- Stage 2 leading term, Sec. 5: the Gaussian `e^(-N eta^T C eta/2)` with
  `C = Q + i Q'` accretive and `|rho_3| <= (1/4) eta^T Q eta`.
- Carrier Stage A, Secs. 1 and 4: `C_k` accretive at the carriers.

Stage 1 (upper bound) does not use it.

The intent of H2 was the stronger property: H2 names itself "the analogue
of manuscript Lemma 7.1(d)", which gives `Q` positive definite. The
hypothesis diagnostics already tested that reading: their H2 column
requires the Hessian in momentum of `log|lambda|` at fixed `xi_*` to be
negative definite (`scripts/diagnose_general_ir_rate_polyhedra.py:291-300`,
`scripts/diagnose_general_ir_rate_round2.py:152,162`), which by the
identity above is `Q > 0`.

## Change

In H2, "non-degenerate Hessian of `log lambda`" is replaced by:

> **H2′.** … each with a simple dominant eigenvalue `lambda_0`, and the
> real Hessian `Hess_eta log|lambda_0(eta - i xi_*)|` at `eta_0` negative
> definite; equivalently `Q = Hess_xi log|lambda_0|` positive definite
> there.

`Q > 0` implies that the complex Hessian `-(Q + i Q')` is non-degenerate,
so H2′ is stronger than H2 as written and contains it.

## Effect

- No proof changes: Stages 1–2 already use exactly H2′. The amendment
  corrects the statement of the hypothesis so that it matches its use.
- K3 satisfies H2′ (manuscript Lemma 7.1(d), as cited in Stage 0(i)).
- The H2 columns of the hypothesis diagnostics are columns of H2′; no
  label changes.
- H2 enters by reference in the carrier charter (`IR_CARRIER_DICHOTOMY_GATE.md`
  Sec. 2, "H2 at the dominant set") and in the Bravais charter
  (`GENERAL_IR_RATE_BRAVAIS_GATE.md` Sec. 2, "same hypotheses"); once in
  force, H2′ is read there too.
- Status of the verdicts is unchanged: Stages 1–2
  `PROVED_UNDER_FROZEN_CONTRACT` (author, PRELIMINARY), now under the
  charter as amended by Amendments 1–5, with this amendment not reviewed.
