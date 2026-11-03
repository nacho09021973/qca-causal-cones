# HEX_SUPREMUM (M1): the 19-point support (M1-B19)

**Date:** 2026-11-03. **Branch:** `research/schur-stability-audit`.
**Contract:** [`HEX_SUPREMUM_GATE.md`](../theory/HEX_SUPREMUM_GATE.md),
preregistration commit `86573ca`; M1-B19 authorized 2026-11-03 («Autorizar
M1-B19 ... empezando exclusivamente por la reducción estructural»), after
the promotion of M1-B13 (`677bec0`). Builds on
[Stage A](2026-11-03--hex-supremum.md) (promoted for S13).
**Author:** Claude Code (Claude Opus 5.5). **Verifier:**
`scripts/verify_hex_supremum_b19.py`, 17/17 (fail-closed, exact, 10 min 44 s;
SHA-256 `244bb106…`);
certificate data `scripts/data/hex_s19_certificate.json` (SHA-256
`548988f7…`). Exploratory scripts (no verdict):
`scripts/explore_hex_s19_reduced.py`, `scripts/explore_hex_s19_certificate.py`.
**Amendment:** [`HEX_SUPREMUM_GATE_AMENDMENT_1.md`](../theory/HEX_SUPREMUM_GATE_AMENDMENT_1.md)
(`208e1b1`, approved 2026-11-03): the certificate is assessed under
contract Sec. 4 (i); literal deviations declared there.
**Review:** Grok (`grok-4.7`), REPAIR_REQUIRED with one mandatory repair
(the amendment) and two clarifications, all applied in this revision
(`debates/2026-11-03--hex-supremum-b19-review-grok/`, record `f80c075`,
reviewed version `6302328`). Gemini: no report (402, no credits).
**Status: PRELIMINARY; one of the two requested independent reviews.**

**Pre-step check.** Known: S19 has facet-normal layers 3, 4, 5, 4, 3, so
lemma A1 forces only layer sums; the full system (56 free real parameters,
Gröbner over `C`) did not finish in 900 s in the parent gate. Question: do
further consequences of saturation reduce the unknowns before any solver?
Abandonment: if nothing beyond the layer sums is forced, no rerun of the
same system; budgeted solver on a reduced system or `OPEN_AFTER_<analysis>`.

## 1. Two further linear consequences of saturation

Notation of the Stage A report. Suppose `c_0 = r_in = r`. Fix a facet
normal `n`, the edge direction `e = Rot90(n)`, and `x_+`, `x_-` the unit
eigenvectors of `n.sigma` (eigenvalues `+1`, `-1`). On the facet line,
`U(t n) = D(t) = e^{-irt} P_+ + e^{irt} P_-` (rigidity). Levels `lambda`
are the projections `h.n`.

**Lemma A3 (first moments).** For every layer `lambda` and both signs,
`sum_{h in lambda} (h.e) <x_±, A_h x_±> = 0`.

*Proof (sign +).* `f(z; s) = e^{irt} <x_+, U(t n + s e) x_+>` is, for fixed
real `s`, an analytic polynomial in `z = e^{i delta t}` (the exponents
`r - h.n` are `>= 0` multiples of `delta`), with `|f| <= 1` on `|z| = 1`
(unitarity) and `f(z; 0) = 1` (rigidity). Let `g(z) = d f/ds (z; 0)`, again an
analytic polynomial. From `|f|^2 = 1 + 2 s Re g + O(s^2) <= 1` for both
signs of `s`, `Re g = 0` on the circle, so `g` is an imaginary constant.
At `z = 1` (`t = 0`), `g = -i <x_+, A(e) x_+> = -i r (e.n) = 0`. Hence
`g = 0`; its Fourier coefficients are `-i sum_{h in lambda} (h.e) <x_+, A_h x_+>`.
The sign `-` is the same with `e^{-irt}` and `z̄`. ∎

**Lemma A4 (off-diagonal first order).** For every layer `lambda`,
`sum_{h in lambda} (h.e) <x_+, A_h x_-> = sum_{h in -lambda} (h.e) conj<x_-, A_h x_+>`.

*Proof.* Differentiating `U^dag U = I` along `e` on the facet line gives
that `K(t) = D(t)^dag d_e U(t n)` is anti-Hermitian. With
`d_e U = -i sum_h (h.e) A_h e^{-it h.n}`, `K_{+-} = -i sum_h (h.e) <x_+, A_h x_->
e^{it(r - h.n)}` and `conj K_{-+} = i sum_h (h.e) conj<x_-, A_h x_+>
e^{it(r + h.n)}`. `K_{+-} + conj K_{-+} = 0` for all `t`; matching the
frequency `r - lambda = r + lambda'` gives `lambda' = -lambda` and the
stated identity. (The diagonal of `K` gives `Re g = 0` only; A3 is
stronger because it uses analyticity.) ∎

A3 and A4 are consequences of unitarity, rigidity and the normal form
`A(v) = r v.sigma` (hex-ceiling report Sec. 3, Step 2; A3 uses it at
`z = 1`); they are not new assumptions. Their use is that they are linear.

## 2. Reduction on S19 (verifier)

Unknowns: 19 complex 2×2 coefficients, 152 real parameters; normal form
`A(n) = r n.sigma`, `|vertex| = 1`.

| Constraints | Free real parameters |
| --- | --- |
| L1: layer sums on the three facet normals | 56 (as in the parent gate) |
| + L2: A3 | 28 |
| + L3: A4 | 18 |

All three systems are consistent (exact rank over `QQ(sqrt3)`). The
remaining unitarity equations `sum_{h-h'=d} A_h A_{h'}^dag = delta_{d0} I`,
`sum A_{h'}^dag A_h = delta_{d0} I`, restricted to the 18-parameter affine
family, are 730 distinct real quadratics; they span a space of dimension 56
(floating-point rank, used only to guide).

**Controls.** The saturating square walk `exp(-ik_x s_x) exp(-ik_y s_y)`
satisfies L1, L2 and L3. The whole pipeline (L1 + L2 + L3, exact
parametrization, unitarity equations) on the 3×3 square support, which
like S19 has edge-interior and interior points, keeps that walk in its
13-parameter family, and all 298 reduced equations vanish there: the
reductions do not exclude a known saturating walk. On S7, L1 + L2 + L3
leave 1 free parameter, consistent with the parent T2 (the contradiction
there is in one real coordinate). The counts «13-parameter», «298
equations» and S7's «1 free parameter» are printed output, not checks:
the verifier requires only membership and vanishing for the square
controls, and its S7 record is informational (always passes).

## 3. Exact infeasibility certificate

**Exploration (no verdict).** Least squares on the 730 equations from 100
random starts converge to the same positive minimum (`5.056e-3`), which
suggests no real solution. A search over the 56-dimensional span for a
combination whose Gram matrix in the basis `(1, t)` is positive definite
(maximising `lambda_min` at trace 1, SLSQP, 20 starts) found
`lambda_min ≈ 3.8e-4 > 0` in every start. The best combination was rounded
to rational multipliers `c_i` (denominators `<= 10^9`) and stored in
`scripts/data/hex_s19_certificate.json`.

**Certificate (verifier, exact).** `p = sum_i c_i f_i` is formed exactly;
its unique Gram matrix `G` in the basis `(1, t)` satisfies
`p = (1,t) G (1,t)^T` identically, and exact Gaussian elimination over
`QQ(sqrt3)` gives 19 positive pivots, so `G` is positive definite. Then
`p(t) > 0` for every `t in R^18`, while at any solution every `f_i`, hence
`p`, vanishes. **Contract form: Sec. 4 (i)** (Amendment 1, Sec. 1): an
ideal element with explicit rational cofactors `c_i`, whose absence of real
zeros is certified exactly by `G > 0` (Gram identity plus 19 positive
pivots in `QQ(sqrt3)`). It is not claimed as a form (ii) certificate.
As a corollary only (not built or checked by the verifier): for
`0 < mu <= 1/(G^{-1})_00`, `G - mu e_0 e_0^T = L D L^T` with `D >= 0`, so
`-1 = sum_j (d_j/mu) l_j(t)^2 + sum_i (-c_i/mu) f_i(t)`, with coefficients
in `QQ(sqrt3)`. The system's own coefficients lie in `QQ(sqrt3)` (normal
form and hexagon geometry); the multipliers `c_i` are rational. The
docstring of `check_certificate` still says «contract Sec. 4 (ii)»; the
amendment supersedes it, and the verifier's bytes are unchanged.

**Verdict.** M1-B19 `PROVED_FOR_S19`: no s=2 walk with `F within S19`
(in `W_hex^sym`, hence in `W_hex`) reaches `c_0 = r_in`. This includes the
support of JDW L6c. HX2 `CONFIRMED_FOR_S19` (and S7, S13). The gap is
qualitative; no bound below `r_in` is claimed.

## 4. Budget and runs

- Gröbner or other exact nonlinear solver runs on S19: none (0 s of the
  3600 s). Counting the exploratory numerics below as solver time too:
  1294 s < 3600 s (Amendment 1, Sec. 2).
- Exact certificate check: inside the verifier, about 10 min of its 11.
- A first version of the linear reduction with symbolic `rank(simplify=True)`
  was stopped after more than 600 s; replaced by exact `DomainMatrix` rank
  over `QQ(sqrt3)` (seconds). No result came from the stopped run.
- Exploratory numerics: 558 s (least squares), 2 × 368 s (certificate
  search; the second run wrote the stored multipliers, seed 0, 20 starts).

## 5. Status of M1 and what is not established

- M1-A stays `OPEN_AFTER_SINGLETON_LAYER_ANALYSIS`: A1–A4 are proved for
  every support, but no gap proof for `W_hex^sym`.
- The contract's ordered bounded stages (S13, S19) both end with a gap.
  No witness was found, so result (a) of Sec. 0 is not met and the line is
  not closed; no gap proof for the whole class, so it is not settled
  either. Larger hexagons are not in the contract's stages (the next one,
  `v = 2 g_1 + g_2`, has 25 lattice points by Pick's theorem: area 21
  cells, 6 boundary points; not checked by any verifier); continuing would
  need a user decision.
- Nothing for `s > 2`, other lattices, masses.
- No novelty claim: A1–A4 are direct uses of unitarity and the Bernstein
  equality case (prior art); positive-definite Gram certificates are
  standard real algebraic geometry.

## 6. Next step

Second independent cross-family review (Gemini when it has credits, or
another family the user authorizes), then a separate promotion; any
extension beyond S19 is a separate user decision (S25 not authorized).
