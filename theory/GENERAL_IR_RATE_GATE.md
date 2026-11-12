# General infrared operational rate: charter

2026-11-12. User: «lo damos por bueno, vamos a intentar hacer el teorema
general»; frozen unchanged by user choice «Congelar tal cual» the same day.
**Status: OPEN; frozen; execution of Stages 0–2 authorized within the
budget of Sec. 6.** Drafted by Claude (claude-opus-5-5).

## 1. Known, question, abandonment

**Known.**

- K1. Upper rate, general. For any translation-invariant finite-range walk
  `W` on `Z^d (x) C^s` and any initial state of compact support,
  `limsup (1/t) log p_t(M) <= -inf_M I_CJWW`, with `I_CJWW` the Legendre
  transform of `R(lambda) = sup_p sup{log|u|^2 : u in spec W(p+i lambda/2)}`
  (CJWW, `sources/2408.02108v1.pdf`, Thm. 2.1, PDF p. 3). The rate is for
  probabilities. Write `I = I_CJWW/2` for the amplitude rate. `I = 0` on
  `conv Gamma` and `I = +inf` outside `conv F` (same source, PDF pp. 9–10,
  Lemma 4.1). Prior art.
- K2. CJWW do not prove lower bounds: «since these would be state
  dependent, we do not consider them here» (PDF p. 3).
- K3. Non-ballistic corona, one walk. For CJWW Eq. (5.15) and the fixed
  protocol of `papers/ir-corona/ir-corona.tex` (tag `ir-corona-v3`):
  `delta(N) = |C(theta_N)| N^(-13/2) e^(-K_* N)(1 + O(N^(-1/2)))`,
  `K_* = inf_{V_reg} I`. PRELIMINARY; one sealed review per version
  (Grok 2026-11-12: A–C PASS, D exposition repairs applied); accepted by the
  user as the working version 2026-11-12.
- K4. Ballistic corona, one walk. For the tetrahedral s=4 walk and its fixed
  protocol, `c N^(-5) <= L_N <= C N^(-5)`: polynomial, carried by the
  admissibility leakage to non-zero momentum and transported ballistically
  by branches with speed above `c_IR`
  (`reports/2026-11-10--tetrahedral-fable-local-audit.md`, verdict
  `AUDIT_PASS_WITH_LOCAL_DERIVATION`, PRELIMINARY, Grok review never
  returned).
- K5. In K3 the leading coefficient is a real-linear functional of the
  encoder generator `M = aI + b.sigma` (manuscript, Methodology remark).

**Conjectured picture (not established).** For infrared-admissible
operations the regional exponential rate is the CJWW amplitude rate:
exponential decay with rate `K_* = inf_{B-A} I` when `K_* > 0` (K3), and
sub-exponential decay when the regional velocities meet the region where
`I = 0` (K4). K1 gives the upper half for free; nothing in the literature
read gives the lower half.

**Question (single).** Under explicit structural hypotheses, is the CJWW
rate sharp for infrared-admissible operational signals between two regions
in the non-ballistic corona? That is, does

    limsup_{N->inf} (1/N) log delta(N) = -K_*                    (T)

hold for at least one protocol of the declared family, for every walk of
the declared class that satisfies the hypotheses?

**Result that ends the line** (stated for the line, separately from the
per-target verdicts of Sec. 5):

- (a) a walk in the declared class satisfying H1–H5 for which every
  protocol of the family has `limsup (1/N) log delta(N) < -K_*`. This is a
  first-class negative result; it closes the line as stated.
- (b) a published theorem whose hypotheses the class satisfies and which
  yields (T) directly, with the operational step trivial. The line then
  closes as a corollary of prior art.
- (c) the budget of Sec. 6 exhausted without a proof of Stage 2. The line
  stops as `OPEN_AFTER_<analysis>`, with the missing step named.

## 2. Declared class

Frozen before any calculation; every conclusion keeps these quantifiers.

- Lattice `Z^d`, `d in {2, 3}`; internal space `C^s`, `s >= 2`; one-step
  unitary `S` with Laurent-polynomial symbol `S(p)`, finite support `F`,
  translation invariant. No interaction, no disorder, no time dependence.
- Infrared node: `p = 0` is an isolated point where two eigenphases meet
  with an isotropic, untilted linear cone of speed `c_IR > 0`; the
  resource's internal vector lies in that two-dimensional nodal space.
  No other condition on the rest of the spectrum.
- Regions: `A_N = N A cap Z^d`, `B_N = N B cap Z^d`, with `A`, `B` closed
  Euclidean balls; `K_* := inf_{v in B - A} I(v)`, required `> 0`
  (non-ballistic corona). `B - A` lies outside `B(c_IR)` and inside
  `conv F`.
- Protocol family: as in the manuscript, with the obvious changes of
  dimension: band-limited resource `g(Np) chi`, `g(q) = (1-|q|^2)_+^2`;
  encoders `exp(i (pi/2) F_N(x) M)`, `M` in a fixed basis of Hermitian
  `s x s` matrices; effects `h_N(y) (x) M_B`, `M_B` in a fixed finite set of
  projectors spanning the Hermitian matrices; profiles vanishing
  quadratically on the spheres. Admissibility in the sense of manuscript
  Definition 3.1.

## 3. Hypotheses (named; each conclusion lists the ones it uses)

- H1 (unique minimiser). `I` attains `K_*` on `B - A` at a unique `v_*`,
  with `I` differentiable there; `xi_* = grad I(v_*)`.
- H2 (finitely many dominant points). `rho(S(eta - i xi_*))` attains its
  maximum `e^(Phi(xi_*))` over the torus at finitely many `eta_0`, each with
  a simple dominant eigenvalue and non-degenerate Hessian of
  `log lambda` (the analogue of manuscript Lemma 7.1(d)).
- H3 (rational normal). `xi_*` is parallel to a primitive integer vector,
  so the planes orthogonal to it are lattice planes. (Needed for the layer
  decomposition used in K3; dropping it is a separate question.)
- H4 (trivial character). At least one dominant `eta_0` has a character
  trivial on the lattice planes orthogonal to `xi_*`.
- H5 (non-zero tail). The free tail of the resource at the facing point of
  `B` is non-zero: `R_0(w_*) != 0` in the notation of manuscript Lemma 7.2.

## 4. Stages

- **Stage 0 (documentary; one session).** (i) Check that K3 satisfies
  H1–H5 and K4 violates `K_* > 0`, so the statement is consistent with both
  cases. (ii) Read, in the PDF, the ACSV smooth-point theorems already
  cited (PWM expanded 2nd ed., Thms. 9.5, 9.12) and decide whether they
  give the pointwise kernel asymptotic at `N v_*` under H1–H2; record the
  hypothesis match line by line. (iii) Targeted search for lower
  large-deviation bounds for quantum walks in `d >= 2`. Outcome may
  trigger (b).
- **Stage 1 (upper bound).** `delta(N) <= C_eps e^(-N(K_* - eps))` for every
  protocol in the family and every `eps > 0`, from K1 adapted to amplitudes
  between regions (Schur test). Expected to be a short adaptation of prior
  art; recorded as such.
- **Stage 2 (lower bound, the target).** Under H1–H5, prove (T) for at
  least one pair `(M, M_B)` of the family. Route named in advance:
  layer decomposition along `xi_*` (H3), leading term from the dominant
  points with trivial character (H2, H4), non-vanishing of the
  vector-valued leading term (H5 and K5, which reduces the existence of a
  good pair to the non-vanishing of one vector), uniformity in the
  fractional part of the depth. Limsup form only: non-vanishing along
  infinitely many `N` suffices; no prefactor, no power, no `liminf`.
- **Stage 3 (not in this charter).** Prefactor and power; dropping H3 or
  H4; the ballistic corona (K4 regime); `liminf`. Each needs its own
  charter.

## 5. Verdicts

Per target: `PROVED_UNDER_FROZEN_CONTRACT` / `COUNTEREXAMPLE_VERIFIED` /
`OPEN_AFTER_<analysis>` / `REDUCED_TO_PRIOR_ART_<source>`. Line:
(a), (b), (c) of Sec. 1. A proof uses exact algebra and written analysis;
floating-point evaluation may guide but never enters a verdict. Any check
of an example (Stage 0 (i)) that needs computation goes in a versioned
verifier in `scripts/`. Reviewed verifiers are imported read-only.

## 6. Budget and stop rules

Stage 0: one session. Stages 1–2: two sessions in total. Stop at the end of
the budget with the outcome reached. No search over walks for a
counterexample beyond the two cases of K3, K4 without a new decision. No
change of class, hypotheses or protocol after freezing; a needed change is
an amendment recorded before use. No external transmission without a
separate user instruction. No promotion from a passing script.

## 7. What a positive outcome would and would not say

Would say: in the declared class and under H1–H5, infrared admissibility
does not change the exponential rate of operational influence outside the
emergent light cone; the CJWW upper rate is attained by an explicit local
protocol. Would not say: anything about the power or prefactor, walks
violating H3–H4, interacting automata, the ballistic corona, nature, or
novelty (`NOVELTY = OPEN` until Stage 0 (ii)–(iii) and an outside reader).
