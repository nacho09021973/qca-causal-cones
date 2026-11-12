# General infrared operational rate: Stages 0 and 1, Stage 2 reduction

2026-11-12. Claude (claude-opus-5-5). Charter
`theory/GENERAL_IR_RATE_GATE.md`, preregistration commit `aa6c5f6`.
Author derivation, **PRELIMINARY, not reviewed**. No computation, no
verifier, no external transmission.

Pre-step record. Known: charter Sec. 1 (K1–K5). Question: Stage 0 —
is the statement consistent with K3, K4, and does a published theorem
already give (T)? Stage 1 — the upper bound. Stop: outcome (b) of the
charter if a theorem yields (T) directly.

## Stage 0

### 0(i) The two known cases

- **K3 (CJWW Eq. (5.15)), inside the class, H1–H5 hold**, each from the
  manuscript (`papers/ir-corona/ir-corona.tex`, tag `ir-corona-v3`):
  `d = 3`, `s = 2`, isotropic untilted node `c_IR = 1`, balls, `K_* > 0`
  (Thm 4.3). H1: unique minimiser `v_*` (Thm 4.3(b)); `I` is
  differentiable at `v_*` because `Hess Phi(xi_*) = Q` is positive
  definite (Lemma 7.1(d)), so `xi_* = grad I(v_*)`. H2: the maximum of
  `rho(S(eta - i xi_*))` is attained exactly on `Sigma = {0, pi}^3`
  (Lemma 5.2, all `xi_j != 0`), with a simple dominant eigenvalue (gap
  `e^(2 Phi_*)`) and non-degenerate Hessian at `0`, transported to the
  other seven points by Lemma 7.1(b). H3: `xi_* || (1,1,1)`. H4: `0` and
  `pi u` are trivial on the planes (Lemma 7.1(c)). H5: `I_0 > 0`, so
  `R_0(w_*) != 0` (Lemma 7.2). The manuscript's `Phi` equals the `Phi` of
  Sec. 1 below (Lemma 5.2), so its `K_*` is the `K_*` of the charter.
- **K4 (tetrahedral s=4) is outside the class.** Its audit's transport
  limit localises the leading response at velocities equal to the region
  displacement `beta` (`reports/2026-11-10--tetrahedral-fable-local-audit.md`,
  Sec. 5), so that displacement is reached ballistically and `I = 0` on
  part of `B - A`; then `K_* = 0`. This is an inference from the audit, not
  re-derived here. The charter's picture (sub-exponential when `K_* = 0`)
  is consistent with the observed `N^(-5)`.

### 0(ii) ACSV smooth-point theorems — hypothesis match

Source read in the PDF: Pemantle, Wilson, Melczer, *Analytic Combinatorics
in Several Variables*, expanded 2nd ed. manuscript, downloaded again
2026-11-12, SHA256 `b9529cd7…5c02b` (equal to the copy recorded on
2026-11-02 and 2026-11-10). Thm 9.5 (printed pp. 264–265, PDF p. 258) and
Thm 9.12 (printed pp. 266–267, PDF p. 260).

- What they give: for `F = P/Q` with a convergent Laurent expansion,
  `a_r` is asymptotic to the sum of the contributions of the smooth,
  minimal, non-degenerate contributing points on the torus of `w(r^)`,
  uniformly for `r^` in a compact direction set. For a walk, the natural
  `F` is an entry of `(I - w S(z))^(-1)`, `Q = det(I - w S(z))`, direction
  `(v_*, 1)`. Smooth points correspond to a simple eigenvalue and the
  finite set of points on the torus to H2. The remaining obligations
  (Laurent domain, numerator cancellation, minimality) are those already
  listed on 2026-11-10 and are not discharged here.
- What they do not give: (1) **non-vanishing**. The asymptotic is a sum of
  contributions that can cancel; the book's own Example 9.14 (Chebyshev,
  printed p. 268) has `a_rs = 0` for `r + s` odd. (2) The **operational
  sum** over two regions with `N`-dependent, finitely smooth profiles,
  which is where lattice planes, characters (H3, H4) and the free tail
  (H5) enter.
- **Verdict: outcome (b) not triggered.** ACSV can supply the pointwise
  kernel input to Stage 2 under H2; it does not yield (T).

### 0(iii) Search for lower bounds

CJWW leave lower bounds out explicitly (`sources/2408.02108v1.pdf`,
PDF p. 3). One alphaXiv discovery search (lower bounds / sharpness of
large-deviation rates for quantum walks in `d >= 2`), screened by title
only, returned no candidate; the closest items are 1D or upper bounds.
Targeted, not exhaustive. Novelty stays OPEN.

**Stage 0 outcome:** consistent with K3 and K4; (b) not triggered;
proceed.

## Stage 1 — upper bound in the class

Notation. `G_N(d) = int e^(-i p.d) S(p)^N dmu(p)` (manuscript
convention). For `xi in R^d` put

    Phi(xi) = max_{eta in T^d} log rho(S(eta - i xi)),
    I(v)    = sup_xi [xi.v - Phi(xi)].

`Phi` is finite: `det S(p)` of a unitary Laurent symbol is a monomial
`c e^(i p.d_0)`, so `|det S(eta - i xi)| = e^(xi.d_0) > 0` and the
spectral radius is positive.

**Lemma 1.1 (convexity).** `Phi` is convex and continuous on `R^d`.

*Proof.* `Phi(xi) = log rho(A(xi))`, with `A(xi)` the multiplication
operator by `S(. - i xi)` on `L^2(T^d; C^s)`: the spectrum of a continuous
matrix multiplication operator is the union of the pointwise spectra. So
`Phi = lim_n n^(-1) log ||A(xi)^n||`. Fix `n`, a point `xi_0` and a
direction `e`; `F(t) = A(xi_0 + t e)^n` extends to an entire
operator-valued function of `t in C`, and
`A(xi_0 + (a + ib) e)` is `A(xi_0 + a e)` conjugated by the unitary
translation `eta -> eta + b e`, so `||F(a + ib)|| = ||F(a)||`.
`log ||F||` is subharmonic and independent of `b`, hence convex in `a`.
A pointwise limit of convex functions is convex; finite convex functions
on `R^d` are continuous. ∎

**Lemma 1.2 (powers).** With `beta(xi) = sup_eta ||S(eta - i xi)||`,
`||S(eta - i xi)^N|| <= sum_{k=0}^{s-1} binom(N,k) (2 beta)^k e^((N-k) Phi(xi))`.

*Proof.* Unitary Schur form `T = V(D + U)V*`, `|D_jj| <= e^(Phi)`,
`U` strictly upper triangular, `||U|| <= ||T|| + ||D|| <= 2 beta`. In the
expansion of `(D + U)^N`, words with `s` or more factors `U` vanish, and
there are `binom(N,k)` words with `k` factors. ∎ (For `s = 2` this is
manuscript Lemma 5.3 with `2 beta` in place of `beta`.)

**Theorem 1.3 (upper bound).** Assume H1 and `K_* > 0`. There is `C` such
that for every `N >= 1`, every unitary acting as the identity outside
`A_N (x) C^s`, every one-particle state and every effect supported in
`B_N`,

    delta <= D_B <= 4 T_N <= C N^(d+s-1) e^(-K_* N).

*Proof.* `Phi` is finite, convex and continuous (Lemma 1.1), so `I` is
proper, convex and lower semicontinuous with `I* = Phi`. By H1,
`xi_* = grad I(v_*)`; Fenchel–Young equality gives
`I(v_*) = xi_*.v_* - Phi(xi_*)`. `v_*` minimises the convex `I` over the
convex set `B - A`, so `xi_*.(v - v_*) >= 0` for `v in B - A`. For
`x in A_N`, `y in B_N`, `(y - x)/N in B - A`, hence
`xi_*.(y - x) >= N xi_*.v_*`. The contour shift (manuscript Eq. (11),
valid for any entire periodic integrand) and Lemma 1.2 give
`||G_N(y - x)|| <= C N^(s-1) e^(N Phi(xi_*) - xi_*.(y - x)) <= C N^(s-1) e^(-K_* N)`.
The Schur test with `|A_N|, |B_N| <= C N^d` bounds `T_N`; the last two
inequalities are manuscript Thm 4.1's argument, which uses neither the
dimension nor the walk. ∎

Check against K3: `d = 3`, `s = 2` gives `N^4`, the power of manuscript
Thm 4.3(d). **Stage 1: `PROVED_UNDER_FROZEN_CONTRACT`, author derivation,
recorded as an adaptation of prior art** (CJWW Thm 2.1's tilt argument,
here for amplitudes between regions with a polynomial prefactor). The
identification of this `I` with half of CJWW's probability rate, up to
sign conventions, is not used and not checked.

## Stage 2 — reduction of non-vanishing (partial)

The lower bound has two parts. **(A)** the general leading-term lemma,
the analogue of manuscript Sec. 7 in the class: the linear interference
term has the form

    Z_N(M, M_B) = e^(-K_* N) N^(-p) [ sum_{k in D} e^(i N alpha_k)
                   Gamma_k(theta_N) (R~^dagger M_B e_k)(f_k^dagger M chi) + o(1) ],

with `D` the dominant points with trivial character (H4), `e_k`, `f_k`
the right and left dominant eigenvectors (rank one by H2), `R~` the tail
spinor (H5), `Gamma_k` the depth-sum factors and `alpha_k` real phases.
**Not proved here**; it is the analytic core of Stage 2. **(B)** given
(A), the existence of a protocol in the family with
`limsup |Z_N| e^(K_* N) N^p > 0`. Two facts reduce (B) to linear algebra:

- `L_N` is exactly linear in the effect, and its leading term is
  real-linear in the encoder generator (K5). If the leading coefficient
  vanished for every pair of the declared basis, it would vanish for every
  Hermitian `M`, `M_B` in their span.
- `{M chi : M Hermitian} = {v : <chi, v> real}`, and Hermitian `M_B`
  separate vectors, so the scalars `f_k^dagger M chi` and
  `R~^dagger M_B e_k` can be prescribed independently at one point `k_0`
  provided `f_{k_0}` (or `e_{k_0}`) is not in the complex span of the
  other `f_k` (or `e_k`).

Two gaps found, neither covered by H1–H5:

1. **Independence.** If several trivial dominant points have linearly
   dependent dominant eigenvectors, the contributions can cancel for every
   pair in the family. Nothing in H1–H5 excludes this. In K3 it does not
   happen: `P` is not a real matrix, so `e` and `e-bar` are independent.
2. **Sign of the depth factor.** `Gamma_k` is a positive integral only
   when the character on the depth index is `+1`, that is at `eta = 0`
   (as `Gamma_+` in manuscript Lemma 7.3). For other trivial points the
   factor is an integral of a square of a complex depth sum and may
   vanish at the values taken by `theta_N`, which are finitely many when
   `theta_N` is periodic. H4 asks for a trivial point, not for `eta = 0`.

With `eta = 0` dominant and its eigenvector independent of the others,
(B) follows: choose `M` with `f_0^dagger M chi != 0` and
`f_k^dagger M chi = 0` for the other `k`, `M_B` with
`R~^dagger M_B e_0 != 0`; then the bracket is
`Gamma_0(theta_N) c + o(1)`, `Gamma_0 > 0`, `c != 0`, and a real-linear
functional of it is non-zero for some pair (rotating `c` by the choice of
`M_B`). `L_N != 0` then also gives `Delta_M != 0`, so the
admissibility denominators are non-zero.

Both gaps change the hypotheses, which the charter allows only by an
amendment recorded before use. **Draft Amendment 1**
(`theory/GENERAL_IR_RATE_GATE_AMENDMENT_1.md`) replaces H4 by H4′ and adds
H6; it is not in force until the user approves it.

## Status

- Stage 0: done; consistent; (b) not triggered.
- Stage 1: `PROVED_UNDER_FROZEN_CONTRACT` (author, PRELIMINARY), prior-art
  adaptation.
- Stage 2: (B) reduced to linear algebra under the draft amendment; (A)
  not started. Budget: Stages 1–2 share two sessions; this session used
  part of the first.
