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

## 3. Not done (on 2026-11-02; done in Sec. 4)

Forward-citation search of ADMP, JDW and P17 for later triangular or
hexagonal walks with speed bounds; reading Arrighi et al.'s curved-
spacetime honeycomb paper (arXiv:1812.02601) located by the search.

## 4. Remaining sources (step 4 of the work plan, 2026-11-03)

User instruction (2026-11-03): «Autorizo el paso 4, con el alcance cerrado
que establece el plan del 2 de noviembre», limited to the forward citations
of ADMP, JDW and P17 and to arXiv:1812.02601; search only for antecedents
of (i) the speed bound, (ii) the 120° optimum, (iii) non-attainment of the
ceiling; on a match, check original text, page or equation, and
equivalence of hypotheses (class of walks, normalization, definition of
`c_0`); otherwise close as `NOT_FOUND_IN_SCOPED_SEARCH`, without widening
the search and without claiming originality. A bound on group velocity or
maximal propagation is not by itself a bound on `c_0`.

Pre-step check. Known: Secs. 1–3 above, and since then M1-B13 and M1-B19
promoted (CS Sec. 14: no s=2 walk with support in the 13- or 19-point
hexagon reaches `r_in`, in `W_hex^sym`). Question: does any source in the
scoped list state (i), (ii) or (iii) with equivalent hypotheses?
Abandonment: one that does, read in the original, which drops the
candidacy. Not a closure criterion of the work plan (Sec. 4 there).

**Citation lists (located only).** OpenAlex, retrieved 2026-11-03,
`/works?filter=cites:<id>`: ADMP (`W2791046739`, 45 citing records), JDW
(`W2794174953`, 16), P17 (`W2743063817`, 17). Semantic Scholar refused
(HTTP 429). Records screened by title and, where OpenAlex has it, abstract.
Kept for reading: those on triangular, hexagonal or honeycomb walks, or on
2D Dirac walks that could compare the continuum speed with the lattice
bound. Set aside by title/abstract: quantum algorithms and search on other
graphs, particle-physics and machine-learning applications, 1D walks,
square/cubic/hypercubic walks (e.g. 1802.03910, 2006.08927, 2408.04493),
noise and diffusion models, lattice Boltzmann, reviews. Citation indexes
are incomplete; this sweep is targeted, not exhaustive.

**Read** (all via alphaXiv full text, not versioned PDFs).

| Source | Passage | Finding |
| --- | --- | --- |
| Arrighi, Di Molfetta, Márquez-Martín, Pérez, *From curved spacetime to spacetime-dependent local unitaries over the honeycomb and triangular quantum walks*, arXiv:1812.02601v1 (Sci. Rep. 9, 2019) | Sec. III, Eq. (22), p. 4; Secs. V–VI, Eqs. (34)–(49), pp. 5–7; Sec. VII | Units `ħ = c = 1` (p. 2). The flat Dirac walk is the ADMP walk, `H_D = π_i τ^i + m σ_z` with three directions at 120°; curvature is absorbed into position-dependent `β_i = n_i·σ`. Uses the linear dependence of the three lattice directions; no speed bound, no comparison of the Dirac speed with the lattice causal bound, no optimum, no non-attainment statement. |
| Jay, Debbasch, Wang, *A new method to building Dirac quantum walks coupled to electromagnetic fields*, arXiv:1812.06729v1 (QIP 19, 422, 2020) | Abstract; "Equilateral Triangle Lattice (changing the t step size)", Eqs. (26)–(36), pp. 4–6; Conclusion, p. 8 | Closest statement found. Within its construction (first-order Trotter factorization of the Dirac Hamiltonian into directional shifts conjugated by unitaries, spinor on the vertices), the equilateral triangular walk requires the time step `Δt = (3/2) ε` (Eq. (32): "α must equal 3/2"), and these are "the only DQWs that can be defined with spinors living on the vertices of these lattices". This fixes the normalization of one construction; it is a uniqueness statement inside that method, not a bound of `c_0` against `r_in(C_micro)` over a class of walks, not the 120° optimum, and not non-attainment. Hypotheses differ: its class is the method's output, not `W_hex`; its `c` is set to 1 by choosing `Δt`, whereas `c_0` here is measured in lattice units of the fixed step set. Not equivalent. |
| Di Molfetta, Deng, *Geodesic quantum walks*, arXiv:2202.10235v2 | Sec. I, Thm I.1, Eqs. (8)–(20), pp. 2–3; Fig. 2 caption, p. 3 | Edge-based triangular walk (ADMP type) with `∂_t Ψ = (σ_x ∂_x + σ_y ∂_y) Ψ` for `Δ = Δt = ε`, `Δ` half an edge; simulations show propagation "isotropically at unit speed". A single walk's speed in its own units; no bound, optimum or non-attainment. |
| D'Ariano, Erba, Perinotti, *Chirality from quantum walks without quantum coin*, arXiv:1902.10227v2 | Sec. II A, Def. 6 and Eqs. (12)–(14), p. 4; Remark 1, p. 3 | Restates P17: for isotropic `s = 2` walks on lattices, the graph is unique (integer lattice, square, BCC for `d ≤ 3`); no-go for isotropic scalar walks. No speed bound on triangular/hexagonal walks. |
| Chagas, Portugal, Boettcher, Segawa, *Staggered quantum walk on hexagonal lattices*, arXiv:1806.10249v1 | Sec. IV, Figs. 4–5, p. 4 | Staggered (coinless) walk; numerical spreading rate `σ(t)/t` maximal at `θ = π/3`. An optimum of a spreading rate in a one-parameter family found numerically, not the 120° Bloch-vector optimum of `c_0`, not a bound against `r_in`. Different class (staggered, no internal Dirac limit stated). |
| Schaefer, *Dynamical localization and transport properties of quantum walks on the hexagonal lattice*, arXiv:2503.09421v1 | Sec. 2 (model), Thm 1, p. 4; Secs. 3, 5 | Three-state coined walk on the honeycomb lattice; localization under disorder and a topological index for transport. No speeds. |
| Aristote, Eon, Di Molfetta, *Dynamical triangulation induced by quantum walk*, arXiv:1907.10717v5 | Sec. 3.5, p. 9; Sec. 5, p. 14 | Triangular walk on a Pachner-move dynamical grid; variance exponent only ("never hyperbalistic in the intermediate and long run", sic). No speed bound. |
| Brun, Mlodinow, *Quantum cellular automata and quantum field theory in two spatial dimensions*, arXiv:2010.09104v1 | Sec. IV, Eqs. (48)–(79), pp. 7–10 | Square-lattice walk, `c ≡ Δx/Δt` by definition (Eq. (76)). Not hexagonal; no bound. |
| Yamagishi, Hatano, Imura, Obuse, *Multi-dimensional quantum walks*, arXiv:2212.13044v3 | Secs. I–II | Square lattice, extended 4-component Dirac walk. Not hexagonal; no bound. |

**Located, not read** (theses or records without accessible full text in
the tools used; screened by abstract where available): *Quantum walks:
background geometry and gauge invariance* (thesis, 2019, `W7148750845`),
*Marches quantiques sous champ magnétique et cages d'Aharonov-Bohm*
(thesis, 2021, `W7149512831`), *Gauge invariance in classical and quantum
cellular automata* (thesis, 2022, `W7151265526`), *Discrete Dirac
Dynamics* (thesis, 2021, `W3196275696`), *Dirac quantum walks with
conserved angular momentum* (2021, `W3199180021`; polar grid by its
abstract record). No claim is made about them.

**Verdict on step 4: `NOT_FOUND_IN_SCOPED_SEARCH`.** In the sources read,
none states (i) a bound of `c_0` (in the sense of CS Sec. 12) below the
lattice bound for triangular/hexagonal walks, (ii) the 120° coplanar
optimum, or (iii) that no walk in a declared hexagonal class reaches
`r_in`. The closest statement (JDW 2018/2020) fixes the time-step
normalization of one construction method and is not equivalent. This does
not show the results are original: the search was scoped, citation
indexes are incomplete, and five records were not read. By the stop rule,
step 4 ends here and the search is not widened. Unreviewed; written by
Claude Code (Claude Opus 5.5). Candidacy status unchanged: not refuted,
`NOVELTY = OPEN`, weight low (L0 Bernstein, T1 elementary; T2 now also
proved for S13 and S19, whole class OPEN).
