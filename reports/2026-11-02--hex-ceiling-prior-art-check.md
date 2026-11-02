# Hexagonal ceiling: targeted prior-art check

**Date:** 2026-11-02. **Branch:** `research/schur-stability-audit`.
**Nature:** literature check of the hexagonal-ceiling results (CS Sec. 12,
promoted). No computation, no gate, no `investigacion-gemini`. alphaXiv
discovery and web search used only to locate papers. Written by Claude
Code (Claude Opus 5.5); unreviewed.

**Pre-step check.** Known (CS Sec. 12): L0 `c_0 <= r_in` on `W_hex`
(classical Bernstein, prior art); T1 `sup c_0/r_in = sqrt3/2` in the
`n = 3` antipodal subclass, attained iff the coin Bloch vectors are
coplanar at 120° (`g = -1/2`); T2 no minimal-support walk reaches `r_in`,
whole class OPEN; per-walk speeds come from ADMP and JDW, and JDW L6d
already sits at the supremum. Question: does a primary source contain
(i) a bound on the Dirac/Weyl speed of triangular/hexagonal walks below
the lattice causal bound, (ii) the 120° optimum or its overlap form, or
(iii) the statement that no walk in such a class reaches `r_in`?
Abandonment: any of (i)–(iii) with the same scope.

## 1. What was read

| Source | Passage | Finding |
| --- | --- | --- |
| D'Ariano, Erba, Perinotti (P17), arXiv:1708.00826v2, `sources/` | Abstract; Fig. 1 caption, PDF p. 6 | For `s = 2`, the "unique graphs admitting isotropic QWs in dimensions d = 1, 2, 3" are the integer lattice, the simple square lattice and BCC. In P17's sense of isotropy, no isotropic `s = 2` walk exists on the triangular lattice. |
| Arrighi, Di Molfetta, Márquez-Martín, Pérez (ADMP), arXiv:1803.01015v2, `sources/` | Introduction, PDF p. 1–2 | Cites P17 as implying "only the square lattice supports the Dirac equation" and says ADMP "circumvents this no-go theorem" by putting the two-component spinors on the edges shared by adjacent triangles. No statement on the speed relative to the lattice bound. |
| Jay, Debbasch, Wang (JDW), arXiv:1803.01304v1, `sources/` | Full text searched for speed, light, causal, coplanar, ratio | Four walks with Dirac continuum limits and their dispersion relations; no bound of the emergent speed against the lattice causal speed and no optimality statement. |
| Di Molfetta, *Quantum walks, limits and transport equations* (HDR), arXiv:2112.11828 | Ch. 6 (triangular QW), searched | Collects the triangular-lattice walks and continuum limits; no ceiling or optimality statement found. |
| Beenakker, Sánchez Fernán, Tworzydło, arXiv:2607.05112 (2026) | Sec. II | Square-lattice Dirac walks; notes that `v_eff` "may or may not differ" from `a/tau` (Ho–Chalker `v_eff = 2^{-1/2} a/tau`). Not hexagonal; no ceiling. |

## 2. Verdict on the candidacy

- (i), (ii), (iii): **not found** in what was read. The abandonment
  condition is not met.
- Context that bounds the weight of the result:
  - P17 rules out isotropic `s = 2` walks on the triangular lattice in its
    covariance sense; hexagonal walks exist only outside that class
    (ADMP's edge spinors; the composite-step class `W_hex` here). The
    ceiling question is therefore about a class P17 does not cover, and
    which P17 hypothesis each L6 row violates is still OPEN (CS Sec. 11).
  - L0 is Bernstein (prior art). T1 reduces to the Gram matrix of three
    unit vectors (`g >= -1/2`) once isotropy forces equal overlaps:
    exact and probably not recorded, but elementary.
  - T2 (minimal support, exact polynomial system without real solution)
    is the least elementary part, and it is restricted; the whole class
    is OPEN.
- **Status:** candidacy not refuted; `NOVELTY = OPEN`; weight low unless
  T2 is decided in the whole class.

## 3. Not done

Forward-citation search of ADMP, JDW and P17 for later triangular or
hexagonal walks with speed bounds; reading Arrighi et al.'s curved-
spacetime honeycomb paper (arXiv:1812.02601) located by the search.
