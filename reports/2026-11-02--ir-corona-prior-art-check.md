# IR-corona theorem: targeted prior-art check

**Date:** 2026-11-02. **Branch:** `research/schur-stability-audit`.
**Nature:** literature check of the novelty sentence of
`papers/ir-corona/ir-corona.tex` ("Relation to the literature"). No
computation, no gate, no `investigacion-gemini` (declined by the user).
Search tools: alphaXiv discovery and web search, used only to locate
papers; every statement below is from the primary text named. Written by
Claude Code (Claude Opus 5.5); unreviewed.

**Pre-step check.** Known: the paper claims, "to our knowledge", that its
Theorem is the first prefactor-level asymptotic, with an oscillatory
leading coefficient certified non-vanishing, for an infrared-controlled
operational response strictly outside the propagation region of a 3D
multi-component walk; it cites Sunada–Tate and Carteret–Richmond–Temme
(1D), Baryshnikov–Brady–Bressler–Pemantle (2D), ACSV, Lieb–Robinson and
CJWW; only CJWW was in `sources/`. Question: does a primary source give
such asymptotics, or a transfer theorem that yields them directly for
the CJWW walk? Abandonment: (a) prefactor-level asymptotics with a
non-vanishing coefficient outside the propagation region for a
multi-component walk in `d >= 2`, after which only the operational/IR
wrapper would be ours; or (b) a theorem whose hypotheses the CJWW walk
satisfies and which yields the result directly.

## 1. What was read

| Source | Passage | Finding |
| --- | --- | --- |
| Cedzich, Joye, Werner, Werner, arXiv:2408.02108v1 (Ann. Henri Poincaré 2025), `sources/2408.02108v1.pdf` | Sec. 5.1, PDF p. 13 | "To our best knowledge, only two studies [8, 23] have been made of the asymptotics outside of the propagation region. In these studies a detailed stationary phase analysis was carried out ... this also gives the prefactors." [8] = Carteret–Richmond–Temme 2005, [23] = Sunada–Tate 2012, both one-dimensional. Independent authors, 2024. |
| Baryshnikov, Brady, Bressler, Pemantle, arXiv:0810.5495 (J. Stat. Phys. 2011) | Introduction; Sec. 4 | Proves uniform exponential decay outside the image of the logarithmic Gauss map and amplitudes inside it; says formulae "inside and outside of the feasible set may be obtained" but that they differ by instance and states no omnibus theorem. Read via alphaXiv full text, not from a versioned PDF. |
| Hinrichs, Mittenbühler, arXiv:2511.13409 (2025), citing CJWW | Abstract, Sec. 1 | Berry–Esseen rate `n^{-1/3}` for 1D walks; refers to CJWW for exponential decay outside the propagation region; no outside-region prefactors, no `d >= 2`. |
| Citing work located but not read: light-cone bounds for Markov open systems (Lett. Math. Phys. 2026, doi:10.1007/s11005-026-02086-4) | — | Located by web search as citing CJWW for an effective light cone with exponentially small spill-over in Lindblad dynamics; not read, so no claim is made about it. |

## 2. Verdict on the candidacy

- (a) **Not met in what was read.** The most recent independent statement
  (CJWW 2024, p. 13) restricts outside-region prefactor asymptotics to
  two 1D studies. BBBP (2D) prove decay, not prefactor asymptotics,
  outside the feasible set.
- (b) **Not decided.** Smooth-point ACSV gives `n^{-(d-1)/2}`-type
  prefactors at non-degenerate critical points; the paper's leader has
  power `13/2`, two discrete normal directions and a flat tangential
  direction confined only by the profiles, so a standard smooth-point
  transfer does not apply as stated. Degenerate/non-minimal ACSV theory
  (Pemantle–Wilson–Melczer, 2nd ed.; Baryshnikov–Pemantle) was **not
  read**; the paper itself says it does not claim these methods cannot
  reproduce the result.
- **Status:** the candidacy stands, `NOVELTY = OPEN`, claim unchanged and
  narrow (the conjunction of prefactor level, certified non-vanishing
  coefficient, operational IR-admissible response, outside region, 3D,
  multi-component).

## 3. Closure of (b) — ACSV degenerate-point theory (2026-11-02, same day)

User instruction: «cierra (b) con la teoría ACSV de puntos degenerados».
Pre-step check: known, (b) undecided, leader `N^{-13/2}` with a flat
tangential direction; question, does a degenerate-point ACSV theorem,
with hypotheses our problem satisfies, yield the Theorem directly;
abandonment, finding one.

**Form of the hypotheses (read).**

| Source | Passage | Finding |
| --- | --- | --- |
| Baryshnikov, Pemantle, *Asymptotics of multivariate sequences, part III: quadratic points*, arXiv:0810.4898v3 (alphaXiv full text) | Theorem 3.7 and the quadratic-point hypotheses 3.1; Sec. 4.3 (two-dimensional quantum random walk); Introduction | The degenerate (quadratic/cone) point theorem gives asymptotics of the coefficients `a_r` of a fixed `F = P/Q^s`, "uniformly over `r in K*`", `K*` a compact subcone of the interior of `N*`. Outside `N*` the stated result is only "exponentially small"; no prefactor is given there. Sec. 4.3 applies the theory to pointwise amplitudes of the 2D Hadamard walk from its space-time generating function. |
| Baryshnikov, Melczer, Pemantle, *Stationary points at infinity for analytic combinatorics*, arXiv:1905.05250v3 (alphaXiv full text) | Sec. 1.1; Example 1 | ACSV "studies coefficients of multivariate generating functions", `a_r` given by a Cauchy integral of a fixed `F(z)`, as `r` varies over a cone; quantum walks enter through the coefficients of their space-time generating function. |

**Form of our quantity (read).** In `papers/ir-corona/ir-corona.tex`,
Sec. "Protocol and infrared admissibility", the signal
`delta_{M,M_B}(N) = |<psi_1,E psi_1> - <psi_0,E psi_0>|` is a bilinear sum
over `O(N^3)` sites of amplitudes weighted by N-dependent data: the
resource `g(Np)` (`g(q) = (1-|q|^2)_+^2`), Alice's profile
`F_N(x) = (1-16|x|^2/N^2)_+^2` inside `exp(i pi/2 F_N M)`, and Bob's
profile `h_N`. These profiles are compactly supported, only finitely
differentiable at the spheres, and rescale with `N`. Remark "Counting
the power" attributes the exponent `13/2` to the resource (`3/2 + 3/2`),
the profiles (`2 + 2`), the in-plane areas (`-2`), one normal Gaussian
(`1/2`) and the tangential rescaling (`1`); the flat tangential
direction is confined by the profiles; the quasi-periodic `C(theta_N)`
comes from lattice planes against the spheres bounding the regions.

**Verdict on (b): `NOT_MET`.** The ACSV theorems read concern single
coefficients of a fixed rational function, uniformly over compact
direction cones; `delta(N)` is not such a coefficient, its weights depend
on `N` and are non-analytic, and the features that fix the leader (the
`13/2`, the flat direction confined by profiles, `C(theta_N)`) come from
that summation, which none of the theorems read addresses. In the
exponentially small regime, the quadratic-point paper states only
exponential smallness. No theorem read yields the result directly.

**What ACSV plausibly does supply, not claimed as checked:** pointwise
amplitude asymptotics of the walk's space-time generating function, which
could replace part of the paper's own saddle-point input. That would
shorten a proof, not anticipate the result.

**Not read:** the monograph Pemantle–Wilson–Melczer, *Analytic
Combinatorics in Several Variables*, 2nd ed. (2024), and its chapters on
cone points and on quantum walks `[UNVERIFIED]`; a theorem there on
weighted sums with N-dependent non-analytic profiles would reopen (b).

## 4. Status after (a) and (b)

Both abandonment conditions are not met in what was read. The candidacy
stands with `NOVELTY = OPEN` and the paper's narrow claim unchanged. The
search is targeted, not exhaustive, and this report is unreviewed.
