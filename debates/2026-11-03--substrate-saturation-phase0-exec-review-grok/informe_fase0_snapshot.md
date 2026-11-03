# Substrate saturation, phase 0 — definitional audit

**Date:** 2026-11-03. **Branch:** `research/schur-stability-audit`.
**Contract:** [`SUBSTRATE_SATURATION_PHASE0_GATE.md`](../theory/SUBSTRATE_SATURATION_PHASE0_GATE.md),
preregistration commit `9bf3019`; registered in CS Sec. 15 (`6851d92`).
**Authorization to execute:** user instruction, 2026-11-03 («EJECUTAMOS
FASE 0»).
**Author:** Claude Code (Claude Opus 5.5). Documentary only: no verifier
run, written or edited; no walk built; no numerics.
**Nature:** a definitional audit with **no confirmatory value** (contract
Sec. 0). **Status: PRELIMINARY, not independently reviewed.**

**Pre-step check.** Known: the contract fixes (PH), its domain (`s = 2`,
`d <= 3`, admissible models), one source per row, three separate fields,
and the outcomes. Question: is (PH) defined without ambiguity on the
promoted rows, and is there an exact counterexample among them? Ends this
formulation: one exact counterexample (contract Sec. 4).

## 1. Rows considered (contract Sec. 3.1)

Promoted rows with `d <= 3` and an exact `c_0` or an exact class statement.
Primary row source: the massless table of
[`reports/2026-11-01--c-across-lattices.md`](2026-11-01--c-across-lattices.md)
(l. 140–152; promoted in the declared rows, CS Sec. 11), in units of
longest step 1, one update per time unit. Composite step sets from the same
report, Sec. 3 (l. 106–113), and for L1–L3 from CS l. 484–496
(`N_d = {(±1,...,±1)/sqrt(d)}`, `C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,
`c_0 = r_in = 1/sqrt(d)`). Every computed row of that table carries the
certificate «Hermitian linear generators, zero tilt, an isotropic untilted
cone (`{T_a, T_b} = 2 c_0^2 delta_ab`), the exact facets and vertices of
`C_micro`» (report l. 154–156).

**Outside the domain (`s != 2`), recorded only:**

| Row | `s` | Source | Note |
| --- | --- | --- | --- |
| L5b (BCC) | 4 | c-across-lattices l. 145 | saturates; cannot confirm or refute (PH) |
| L3s4 (BCC) | 4 | c-across-lattices l. 146; CS Sec. 4.1 | `c_0 = a/sqrt3 < r_in` |
| L6b (triangular) | 6 | L6b report l. 24, l. 70–71; CS l. 88–94, l. 106 | the parent table (l. 152) still lists `s = 2`, OPEN, not encoded; not amended |

## 2. Row table, domain `s = 2` (contract Secs. 3.2–3.3)

Shapes are read from the certified vertices of `C_micro` in the units
above. "Hypercube" means up to scale and isometry; "parallelepiped" means a
Minkowski sum of `d` independent segments. "Zonotope directions" are the
edge directions of `C_micro` (every polytope listed here is a zonotope;
its generators are read from its edges, not from the walk's factor
structure — see Sec. 4, finding F2).

| Row | Substrate (group, `N`) | `C_micro` vertices | Hypercube | Parallelepiped | Zonotope directions | `r_in` | `c_0` | Single source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1 | line, `N = {±1}` | `±1` | yes (segment) | yes | 1 | 1 | 1 | c-across-lattices l. 140 |
| L2 | square, `N_2` | `(±1,±1)/sqrt2` | yes (square) | yes | 2, orthogonal | `1/sqrt2` | `1/sqrt2` | l. 141; CS l. 484–496 |
| L6e | square, same as L2 (l. 111) | `(±1,±1)/sqrt2` | yes | yes | 2, orthogonal | `1/sqrt2` | `1/sqrt2` | l. 142 |
| L3 | BCC, `N_3` | `(±1,±1,±1)/sqrt3` | yes (cube) | yes | 3, orthogonal | `1/sqrt3` | `1/sqrt3` | l. 143; CS l. 484–496 |
| L5a | BCC, same as L3 (l. 106) | `(±1,±1,±1)/sqrt3` | yes | yes | 3, orthogonal | `1/sqrt3` | `1/sqrt3` | l. 144 |
| L4 | cube (CJWW (5.12), (5.15)) | cube of longest step 1 (label `[-1,1]^3` is in CS Sec. 8 units; not combined with the rescaled radius) | yes | yes | 3, orthogonal | `1/sqrt3` | `1/sqrt3` | l. 147 only (CS Sec. 8 pair not crossed) |
| L6a | triangular lattice, `F = {0} ∪ {±2u_i}` (l. 108) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `1/2` | l. 148 |
| L6d | identical to L6a (l. 110) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `3/4` | l. 150 |
| L6f | triangular lattice, hexagon of radius `sqrt3` rotated 30° (l. 112) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `3/4` | l. 151 |
| L6c | finer triangular group, 19-point hexagonal ball (l. 109) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `3/4` | l. 149 |

**Three fields per row, kept apart (contract Sec. 3.3).**

| Row | (a) this walk | (b) promoted class statement, with its scope | (c) substrate, existential |
| --- | --- | --- | --- |
| L1 | `c_0 = r_in` | — | yes: L1 |
| L2, L6e | `c_0 = r_in` | — | yes: L2, L6e |
| L3, L5a | `c_0 = r_in` | — | yes: L3, L5a |
| L4 | `c_0 = r_in` | — | yes: L4 |
| L6a | `c_0 < r_in` (`1/sqrt3`) | T1: `sup c_0/r_in = sqrt3/2` on the `n = 3` antipodal subclass only (hex-ceiling report l. 125, CS Sec. 12); L6a is in it, `g = 1/3` (l. 138–139). T2: no s=2 walk with `F within {0} U vert(H)` reaches `r_in` (CS Sec. 12; contains L6a, L6d, L6f, hex-ceiling l. 152–156). M1-B13, M1-B19: no s=2 walk in `W_hex^sym` with `F` within S13 or S19 reaches `r_in` (CS Sec. 14), qualitative gaps. Whole hexagonal class OPEN. | no promoted saturating walk; **not** "no walk saturates" |
| L6d, L6f | `c_0 < r_in` (`sqrt3/2`) | as for L6a (L6d at the T1 maximum, `g = -1/2`) | as for L6a |
| L6c | `c_0 < r_in` (`sqrt3/2`) | not in the minimal-support subclass (hex-ceiling l. 156); its 19-point support is S19, covered by M1-B19 in `W_hex^sym` (B19 report Sec. 3) | as for L6a, on its own (finer) substrate |

**`OUTSIDE_DEFINITIONS` (contract Sec. 3.4): none.** Every row in the domain
has the isotropic untilted node: computed rows by the certificate of
report l. 154–156; L1–L3 also by CS l. 484–496. **L4 is the weakest traced
row:** it is re-tabulated, not computed, in that report (l. 147, «CURRENT_STATE
Sec. 8»), so its certificate does not cover it. Its node is traced to CS
Sec. 8.1 (l. 764–769, «the emergent isotropic IR light cone» `B(c_IR)` for
CJWW (5.12) and (5.15)) and Sec. 8.2 (l. 784–789: `S(n̂) = h_{B(c_IR)}(n̂) /
h_{C_micro}(n̂) = 1/||n̂||_1` for every unit `n̂`, i.e. `h_{B(c_IR)} ≡ c_IR`,
a ball centred at the origin, hence no tilt). Isotropy and zero tilt are
thus stated in promoted text, but not through the same certificate as the
other rows; recorded, not flagged.

## 3. Counterexample check (contract Sec. 4)

- **Against (PH⇒)** — a non-hypercube substrate in the domain with a
  promoted walk at `c_0 = r_in`: none. The only non-hypercube shape is the
  regular hexagon (L6a, L6c, L6d, L6f), and every promoted hexagonal walk
  has `c_0 < r_in`.
- **Against (PH⇐)** — a hypercube substrate in the domain on which a
  promoted exact result shows that no admissible walk saturates: none.
  Each hypercube substrate (line, square, BCC, cube) has a promoted walk
  with `c_0 = r_in`.

## 4. Audit findings

- **F1 (contract Sec. 3.5).** The table contains no parallelepiped that is
  not a hypercube, and no non-hypercube body with a promoted saturating
  walk. It therefore cannot separate (PH) from (PS′), nor from any other
  predicate that agrees on segments, squares, cubes and the regular
  hexagon (for example "fewer than `d+1` zonotope directions", or "the
  facet normals come in `d` orthogonal pairs"). The shapes present are
  three hypercubes (segment, square, cube) and one non-hypercube (the
  regular hexagon).
- **F2 (on (PS′), recorded, no verdict).** The contract's identity
  `conv F = sum_i [-a_i, a_i]` presupposes that every sign pattern
  `sum_i ε_i a_i` of the partial shifts appears in `F` with nonzero
  amplitude. That is not recorded per row in the promoted data (the factor
  structure is tabulated only for the `n = 3` antipodal subclass, T1), and
  it can fail if a coin entry vanishes. The "zonotope directions" column
  above is read from the edges of `C_micro`, which are certified; whether
  they coincide with the factor shifts of each walk is not established
  here. (PS′) as written therefore needs that hypothesis made explicit
  before any test.
- **F3 (substrate counts).** Grouped by shape and translation group, the
  domain has five substrates (line; square, L2 = L6e; BCC, L3 = L5a; cube,
  L4; hexagon on the triangular lattice, L6a = L6d, with L6f the same shape
  up to rotation and scale) plus the finer-group hexagon of L6c. By shape
  alone: four (segment, square, cube, hexagon).

## 5. Outcomes (contract Sec. 5)

**Definitional outcome: `DEFINITIONS_CLOSED`.** Every row in the domain has
one traced source in the units of contract Sec. 2.4 (L4 from l. 147 only),
all fields of Secs. 3.2–3.3 are filled from promoted exact data (the
zonotope-direction field from the certified vertices, with the caveat of
F2), and the `OUTSIDE_DEFINITIONS` list is explicit (empty). This means
only that (PH) is defined well enough to be tested for refutation.

**Counterexample check:** (PH⇐) `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`; (PH⇒)
`NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`. **This is not independent evidence
for (PH):** the statement was read off this table, which has three
hypercube shapes and one non-hypercube shape and no parallelepiped that is
not a hypercube (F1). Never `CONFIRMED`.

**No outcome of this gate authorizes any later phase** (contract Sec. 5).
A test that can fail needs its own contract with a shape or support not in
the table (contract Sec. 7).

## 6. What this does not establish

No evidence for (PH) or (PS′); no statement about parallelepipeds that are
not hypercubes, about hexagonal walks beyond the promoted results, about
`s != 2` or `d > 3`; no uniform gap; no physical explanation of the
predicate; no novelty claim.
