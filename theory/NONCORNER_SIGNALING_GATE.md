# NONCORNER_SIGNALING_ONE_STEP — contract frozen before solving

**Date:** 2026-09-16. **Scope:** branch-local,
`research/b-infinity-post-s4-gate`, at `e03d19f`.
**Authorization:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` (2026-09-16), to
freeze this contract only. **No step of this gate has been executed.**

This contract is frozen **before** any new calculation. It records no result,
no proof, no counterexample and no novelty claim. It does not reopen the
optimal-D gate, the axial gate, `GATE_COMPLETITUD_AXIAL_N3`, or any frozen
witness, and it changes no dynamics.

**Ratified by the user, 2026-09-16**, with one nomenclature correction
adopted here: the negative verdict carries its temporal scope in its own name
(Sec. 8). Ratified as frozen: the four-point domain, the refusal to presume
symmetries, the completeness criterion `M(y)`, `Delta T = 1`, the exclusion of
the earlier `SUPPORTED` sampled results, and the claim ceiling.

**Initial evidence status: OPEN.**

## 1. Gate name

`NONCORNER_SIGNALING_ONE_STEP`

"One step" is not decoration: the readout time is fixed at one step after the
encoding event by the frozen protocol, and the gate's conclusions are bounded
by that (Sec. 9, Sec. 11.3).

## 2. Question

One physical question, with every other element held at its frozen value:

> In the protocol of
> [`ALICE_LOCAL_PREPARATION_WITNESS.md`](ALICE_LOCAL_PREPARATION_WITNESS.md),
> with **only Bob's site `y` varying**, does there exist a `y` that is
> (a) strictly outside the emergent relativistic cone of the encoding event,
> (b) inside the exact microscopic causal support of that event, and
> (c) not a vertex of `C_micro`, such that Bob's two reduced states differ,
> `rho_B^(0)(y) != rho_B^(1)(y)`?

Equivalently: is the locally-prepared signalling mechanism exclusive to the
`l_inf` vs `l_2` corner discrepancy, or does it survive in a
microscopically accessible non-corner direction?

**Frozen and not varied:** the CAR lift of CJWW (5.15); `c_IR = 1` and
`C_micro = [-1,1]^3` in lattice-step units; the convention
`K_t(x,z) = (W^t)_{x,z}` with one-particle evolution by `S = W^dagger`;
the initial resource `|0,down>` at `T = 0`; two preparation steps of free
dynamics, identical for both messages; the encoding event `A = (T=2, x=0)`
with `U_0 = I`, `U_1 = exp(i pi n_0)`; the readout time `T = 3`, i.e.
`Delta T = 1`. Varying any of these is a different gate.

## 3. Domain — the minimal class of Bob sites

Fix `Delta T = 1`. Write, for a candidate site `y`,

```
a(y) = (S P chi)_y ,      r(y) = (S Q chi)_y ,      v_b(y) = (-1)^b a(y) + r(y)
```

with `chi = S^2|0,down>` the frozen prepared state, `P = P_0` the
one-particle projector at Alice's site and `Q = I - P`. These are exactly the
objects the existing certification already builds.

A site `y` is **admissible** iff

- **(D1) outside the emergent cone of the encoding event:**
  `||y||_2 > c_IR * Delta T = 1` (strict; see Sec. 11.2);
- **(D2) inside the exact microscopic causal support in one step:**
  `K_1(0,y) != 0`;
- **(D3) non-vertex:** `y` has strictly fewer than three nonzero coordinates.

**Declared reduction.** Reading the frozen symbol entry by entry,

```
W_11 = c1 c2 z3      -> displacements (+-1,+-1,+1)
W_22 = c1 c2 z3^-1   -> displacements (+-1,+-1,-1)
W_12 = -c1 s2 + i s1 -> displacements (+-1,+-1,0) and (+-1,0,0)
W_21 =  c1 s2 + i s1 -> displacements (+-1,+-1,0) and (+-1,0,0)
```

so the one-step support is the 14 displacements
`{(+-1,+-1,+-1)} U {(+-1,+-1,0)} U {(+-1,0,0)}`. Applying (D1) removes
`(+-1,0,0)` (norm exactly `1`, null-separated, not outside); applying (D3)
removes the eight vertices. Therefore

> **Open class: the four sites `(+-1,+-1,0)`.**

Everything else in `Z^3` is excluded by an exact criterion, not by a search:

| Class | Excluded by |
| --- | --- |
| `\|\|y\|\|_inf >= 2` (includes the frozen control `(2,0,0)`) | (D2): `K_1 = 0` |
| `(+-1,0,+-1)` and `(0,+-1,+-1)` | (D2): `K_1 = 0` — a zero in coordinate 1 or 2 is reachable in one step only through `W_12`/`W_21`, whose `z3` exponent is `0` |
| `(+-1,0,0)` | (D1): `\|\|y\|\|_2 = 1`, on the emergent cone |
| `(0,+-1,0)`, `(0,0,+-1)` | (D1) and (D2) |
| `(+-1,+-1,+-1)` | (D3): vertex — already resolved, Sec. 7 |
| `y = 0` | Alice's own site |

The domain is therefore **finite, of size 4, and requires no search**. The
support decomposition above is a reading of the frozen symbol, **not** a
proved statement of this repository: it is re-certified exactly as execution
step 0 (Sec. 10), and if certification fails the domain is recomputed from the
certified support before any physical conclusion is drawn.

## 4. Symmetries

**No symmetry of the full protocol has been certified in this repository for
this walk.** The symbol is not invariant under permuting coordinates: `p3`
enters only the diagonal entries, `p1` enters `W_12`/`W_21` through `s1` and
`p2` through `c1 s2`. The initial spin `down` and the origin gate break
further structure.

Accordingly this contract **presumes no symmetry**. Any claimed equivalence
among the four admissible sites — for instance `(1,1,0)` with `(-1,-1,0)`,
`(1,-1,0)` or `(-1,1,0)` — must be certified as an exact unitary conjugation
carrying the **entire** protocol (initial state, preparation, encoding gate,
readout site and effect) to itself before it is used to skip a site. Absent
such a certificate, **all four sites are examined exhaustively**; the cost is
four exact evaluations. Any equivalence that is certified is recorded as a
by-product, never assumed in advance.

## 5. Positive criterion

`NONCORNER_SIGNALING_CONSTRUCTED` requires, for at least one admissible `y`,
**all three** of:

1. **(P1) Exact state inequality.** `M(y) != 0`, where

   ```
   M(y) := a(y) r(y)^dagger + r(y) a(y)^dagger        (Hermitian 2x2)
   ```

   with every entry exact (rational or exact algebraic). See Sec. 6 for why
   `M` is the complete invariant.
2. **(P2) An explicit operational witness.** A local effect `E` on Bob's
   two-mode Fock space with `0 <= E <= I`, exhibited explicitly, and an exact

   ```
   delta = |Tr(E (rho_B^(1) - rho_B^(0)))| > 0 ,   hence  D >= delta .
   ```

   This is required **even when `Tr M(y) = 0`**; in that case `E` cannot be
   the non-vacuum projection and must be given in an internal basis. No
   optimization of `E` is performed or claimed.
3. **(P3) Re-certified admissibility.** `y` satisfies (D1), (D2), (D3) under
   the frozen conventions, with `K_1(0,y)` exhibited.

One admissible `y` suffices. A positive result **adds** points; it does not
amend, weaken or reopen the frozen vertex witness.

## 6. Negative criterion

Because the protocol keeps one particle and Bob's site carries two modes,
fermion parity superselection forbids vacuum/one-particle coherence and
Bob's reduced state is exactly

```
rho_B^(b)(y) = (1 - ||v_b||^2) |vac><vac|  +  v_b v_b^dagger ,
```

with zero two-particle block. Hence

```
v_0 v_0^dagger - v_1 v_1^dagger = 2 M(y) ,
p_0 - p_1 = Tr(2 M(y)) = 2 Tr M(y) ,
```

and therefore

> `rho_B^(0)(y) = rho_B^(1)(y)`  **if and only if**  `M(y) = 0`.

`M(y)` is thus a **complete** invariant for this question, and the occupation
witness sees only its trace:

```
Delta p_B(y) = |p_1 - p_0| = 2 |Tr M(y)| .
```

A Hermitian `M != 0` with `Tr M = 0` gives `D > 0` with an exactly vanishing
occupation response. **Occupation nullity is therefore not evidence of
equality, and a null occupation response must never be reported as the
negative outcome.** (Consistency check with the frozen witness: at
`y = (1,1,1)`, `a = -3 down/16`, `r = -down/32`, so
`M = (3/256)|down><down|`, `Tr M = 3/256` and `Delta p_B = 3/128`.)

`CORNER_ONLY_AT_DT1_WITHIN_FROZEN_PROTOCOL` requires **all** of:

1. **(N1)** `M(y) = 0` exactly, as an identity in exact arithmetic, for
   **every** admissible `y` — all four, or all not excluded by a certified
   symmetry under Sec. 4.
2. **(N2)** An explicit statement of the algebraic obstruction producing each
   zero (for example `a(y) = 0`, or `r(y) = 0`, or `a` and `r` collinear with
   purely imaginary ratio), so the result is a structural statement and not a
   coincidence of four evaluations.
3. **(N3)** No appeal, anywhere in the record, to a null occupation response,
   to a floating-point evaluation, or to a sampled result.

## 7. Cases already resolved, and cases only sampled

**Vertex — POSITIVE, PROVED and INDEPENDENTLY REVIEWED.** At `y = (1,1,1)`:
`K_1(0,y) = diag(0,1/4) != 0`, `||y||_2 = sqrt(3) > 1`,
`M = (3/256)|down><down| != 0`, `Delta p_B = 3/128 > 0`, `D >= 3/128`.
Frozen in [`ALICE_LOCAL_PREPARATION_WITNESS.md`](ALICE_LOCAL_PREPARATION_WITNESS.md),
`CURRENT_STATE` Sec. 8.13. The other seven vertices are **not** individually
certified; they are vertices and so lie outside this gate's question.

**Axis — NEGATIVE, PROVED by exact obstruction.** At `y_ax = (2,0,0)` with
`Delta T = 1`, `K_1(0,y_ax) = 0` exactly, so Bob's evolved local algebra has
no Alice component and commutes with any even local Alice unitary. Hence
`rho_B^(0) = rho_B^(1)` there for **every** initial state and either choice.
Frozen; this is a statement about the microscopic support, not an occupation
null.

**Axis at unit distance — EXCLUDED BY DEFINITION, not by computation.** The
sites `(+-1,0,0)` are microscopically accessible in one step but satisfy
`||y||_2 = 1 = c_IR Delta T`: they are null-separated from the encoding
event, hence not outside the emergent cone. No axis direction can be both
micro-accessible in one step and strictly outside the emergent cone. This is
an exact structural fact about `Delta T = 1`, and it is the precise sense in
which "the axis is negative".

**Intermediate directions — NOT RESOLVED, AND NOT EVEN PARTIALLY ADDRESSED.**
The `SUPPORTED` check *"coupling map: sampled off-vertex local occupation
response vanishes"* in `verify_directional_saturation.py` contributes
**nothing** to this gate, for four independent reasons:

1. it belongs to the **coupling-map protocol** (pre-existing Alice–Bob
   coherence), not to the locally-prepared protocol frozen here;
2. it is evaluated at `t = 2, 3, 4` steps from the choice, never at
   `Delta T = 1`;
3. it is **floating point** with randomly sampled local rotations and a
   `1e-12` tolerance — not exact arithmetic;
4. it tests invariance of `K_0y K_0y^dagger` under local rotations, an
   occupation-response property, and its own recorded text already states
   that this *"does not imply equality of Bob's full reduced states"*.

It must not be cited as partial evidence for either outcome of this gate, and
no `SUPPORTED` item is promoted by this contract.

## 8. Possible outcomes

| Outcome | Condition |
| --- | --- |
| `NONCORNER_SIGNALING_CONSTRUCTED` | Sec. 5 met at one or more admissible sites. Each site's status is recorded separately. |
| `CORNER_ONLY_AT_DT1_WITHIN_FROZEN_PROTOCOL` | Sec. 6 met at **every** admissible site. |
| `OPEN_AFTER_EXACT_BOUNDED_ANALYSIS` | The step-0 support certification fails, or any admissible site cannot be settled exactly, or a mixture is found that Sec. 5 and Sec. 6 do not jointly classify. |

A mixed result — some admissible sites with `M != 0`, others with `M = 0` —
is `NONCORNER_SIGNALING_CONSTRUCTED` **with the per-site table recorded**, not
a partial negative. No outcome is forced into a binary.

**Why only the negative verdict carries `AT_DT1`.** The positive verdict is an
existence claim: a witness exhibited at `Delta T = 1` stays literally true
whatever a larger `Delta T` later shows, so its name needs no temporal tag.
The negative verdict is a non-existence claim over a domain that `Delta T`
fixes. Should a successor gate find signalling at, say, `(2,2,0)` with
`Delta T = 2`, today's verdict must remain literally true and require no
reinterpretation. The scope therefore lives in the name, not only in Sec. 9.

## 9. Claim ceiling

Binding on every outcome.

- **A negative result is not universal.** `CORNER_ONLY_AT_DT1_WITHIN_FROZEN_PROTOCOL`
  would say only: *within this frozen protocol* — initial `|0,down>` at
  Alice, two free preparation steps, the origin gate `exp(i pi n_0)`, one
  readout step — the effect vanishes at every micro-accessible non-vertex
  site strictly outside the emergent cone of the encoding event. It would say
  nothing about other interventions (other local unitaries, POVMs, multi-site
  or multi-particle operations), other preparation or readout times, other
  initial spins or sectors, other walks or substrate classes, optimized
  protocols, asymptotics, channel capacity, experimental feasibility, or our
  universe.
- **A negative result would not establish a mechanism.** It would establish
  corner-exclusivity *inside the frozen class*; it would not prove that the
  `l_inf`/`l_2` discrepancy *is* the mechanism, nor that no non-corner
  mechanism exists in any wider class.
- **A positive result is equally bounded.** It would exhibit one further
  finite witness at a non-vertex site, with its own exact `delta`. It would
  not establish optimality, minimality, scaling, capacity, feasibility, or
  any claim about our universe, and would not enlarge the frozen witness.
- **Neither outcome touches microcausality.** Every admissible site lies
  inside the exact microscopic causal support; no outcome can be reported as
  a violation of the model's microscopic causality.
- **Neither outcome reopens** the optimal-D gate (still `PARTIAL`, H1 `OPEN`,
  H3/H4 `NOT REACHED`), the axial gate, `GATE_COMPLETITUD_AXIAL_N3` (still
  `ABORTED_OR_INCOMPLETE`, unauthorized), or the experimental question
  (still unopened, by instruction).

## 10. Execution plan — approved contract only, not executed here

Minimal exact computation, in order:

0. **Certify the one-step support** exactly from the frozen symbol: exhibit
   `supp K_1` and check it equals the 14 displacements of Sec. 3. Recompute
   the admissible set from the certified support. On mismatch, stop at
   `OPEN_AFTER_EXACT_BOUNDED_ANALYSIS`.
1. **Reuse `chi`.** The prepared state `chi = S^2|0,down>`, its origin
   component `P chi = -3 down/4` and the remainder `Q chi` are already built
   by the existing `--local-preparation-only` path. Do not recompute them by
   another route and do not alter them.
2. **Evaluate the four sites.** For each admissible `y`, obtain `a(y)` and
   `r(y)` with the existing `evolve` / `exact_blocks` helpers, unmodified,
   and form `M(y)` exactly.
3. **Record per site:** `K_1(0,y)`, `a(y)`, `r(y)`, `M(y)`, `Tr M(y)`,
   `Delta p_B(y) = 2|Tr M(y)|`, and the boolean `M(y) = 0`.
4. **If any `M(y) != 0`:** exhibit `E` and the exact `delta` of (P2), and
   state explicitly whether `Tr M(y) = 0`, i.e. whether the occupation
   witness is blind at that site. *(Structural note, to be certified rather
   than assumed: at `(+-1,+-1,0)` the one-step block comes only from the
   off-diagonal symbol entries, so `a(y)` is expected to be spin-flipped
   relative to `down`. If so, part of `M(y)` sits off-diagonal, where the
   occupation witness cannot see it. This is stated as the reason the
   occupation criterion is inadequate — **not** as a prediction of the
   outcome, which is not computed here.)*
5. **Classify** per Sec. 8, write the report, freeze, and seek one
   independent review before any promotion of `CURRENT_STATE`.

**Implementation discipline.** No new script. One isolated function plus one
new CLI flag in `scripts/verify_directional_saturation.py`, under the same
isolation already reviewed for `--local-preparation-only`: the default
`main()` path unchanged in behaviour, new helper imports inside the function,
frozen witnesses and `verify_signaling_witness.py` untouched. Exact
arithmetic only — no floating point, no sampling, no parameter search, no
optimization, no asymptotics.

## 11. Declared ambiguities

These are recorded rather than silently resolved.

1. **"Not equivalent by symmetry to the vertex."** No protocol symmetry is
   certified for this walk, so that phrase has no operative meaning here. It
   is replaced by the exact geometric criterion (D3), *fewer than three
   nonzero coordinates*. If a different equivalence is intended, the domain
   must be restated before execution.
2. **Strict versus non-strict emergent-cone test.** The frozen witness uses
   the strict `||y||_2 > c_IR Delta T`, which excludes the null-separated
   sites `(+-1,0,0)`. This contract keeps the strict form, because signalling
   to a null-separated point is relativistically unremarkable. If "not
   strictly inside" were intended instead, those two sites would enter the
   domain and this contract would have to be re-frozen.
3. **`Delta T` is fixed at `1` by the frozen protocol.** This is the gate's
   principal scope limitation: a negative outcome is about one readout step.
   Larger `Delta T` enlarges the admissible set (at `Delta T = 2`, sites such
   as `(2,2,0)` and `(2,1,0)` satisfy both (D1) and (D2)) and is **not** part
   of this gate.

   **Resolved by explicit user decision, 2026-09-16: `Delta T = 1` is
   retained.** Widening to `Delta T = 2` now would mix a second causal
   geometry, a second spatial domain and possibly a second mechanism into one
   verdict. If this gate returns
   `CORNER_ONLY_AT_DT1_WITHIN_FROZEN_PROTOCOL`, then `Delta T = 2` is the
   natural successor gate, chartered separately — never an extension of this
   one, and never a reinterpretation of its verdict.
