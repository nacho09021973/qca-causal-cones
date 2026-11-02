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

## 3. What would close (b), not done

Read the degenerate-point chapters of the ACSV monograph and check whether
a stated theorem covers a flat tangential direction with lattice-plane
sums in the normal directions; and a forward-citation search of CRT,
Sunada–Tate and BBBP for `d >= 2` outside-region results.
