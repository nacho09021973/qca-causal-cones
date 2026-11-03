# SUBSTRATE_SATURATION (phase 0) — draft contract, revision 2

**Status: DRAFT, revision 2. Not frozen, not committed, nothing executed.**
Drafted by Claude Code (Claude Opus 5.5) on 2026-11-03 at the user's
instruction («Autorizo redactar la carta de la fase 0, pero no congelarla
ni ejecutar todavía ninguna comprobación»). Revision 1 was reviewed by Grok
(`grok-4.7`, REPAIR_REQUIRED, six mandatory repairs;
`debates/2026-11-03--substrate-saturation-phase0-draft-review-grok/`).
Revision 2 applies, by the user's decision of 2026-11-03 («aceptar las seis
reparaciones de Grok, adoptar "hipercubo" como predicado provisional y
convertir la fase 0 en una auditoría de definiciones, sin valor
confirmatorio»), all six repairs, the terminology change
parallelotope → parallelepiped, and the zonotope reading (PS′) without any
equivalence claim. Freezing needs a separate approval; reports would then
cite the commit that adds this file as the preregistration commit.
**Initial scientific status: OPEN.** The conjecture below is `[UNVERIFIED]`;
it was formulated by an AI from the promoted table and has no evidence
level of its own.
**Does not alter:** step 4 of the work plan (hexagonal-ceiling prior-art
check, `NOT_FOUND_IN_SCOPED_SEARCH`, `6114b9d`), M1 (`86573ca`,
Amendment 1 `208e1b1`) or any promoted row.

## 0. Nature of this gate and pre-step check (rule of 2026-11-02)

**Phase 0 is a definitional audit with no confirmatory value.** The
conjecture of Sec. 1 was read off the same table this gate would audit
(Grok, repair 6). Its purpose is to fix definitions, normalizations,
traceability and the domain of the statement. Its conclusion is never
"the conjecture survives"; at best it is "the statement is defined well
enough to be tested for refutation". A test that can fail needs a separate
contract with a shape not in the table (Sec. 7).

- **Known.** Promoted rows (CS Secs. 4, 5, 8, 11, 12, 14; c-across-lattices
  report Sec. 4; c-across-substrates answer Sec. 1): the ceiling
  `c_0 = r_in(C_micro)` is attained by some declared `s = 2` walk on the
  line (L1), the square (L2, L6e), BCC (L3, L5a) and the cube (L4); their
  `C_micro` are a segment, squares and cubes, i.e. hypercubes up to scale
  and isometry. On the hexagon no declared walk attains it; `sup c_0/r_in
  = sqrt3/2` in the `n = 3` antipodal subclass; no s=2 walk in `W_hex^sym`
  with `F` within S7, S13 or S19 attains it; the whole hexagonal class is
  OPEN. The table contains no parallelepiped that is not a hypercube, so it
  cannot distinguish the two notions (Grok, repair 1).
- **Question.** Is the statement of Sec. 1 defined without ambiguity on the
  promoted rows (definitions, units, single source per row, levels of
  claim), and is there an exact counterexample to it among those rows?
- **Result that ends this formulation.** One exact counterexample in the
  promoted rows (Sec. 4): the formulation of Sec. 1 is dropped at once,
  with no repair attempted in this gate.

## 1. Statement under audit

> **(PH) [UNVERIFIED], provisional predicate.** For `s = 2`, `d <= 3`,
> within the declared classes of Sec. 2 and only for models with an
> admissible isotropic untilted node: the ceiling is attained on a
> substrate, in the sense of Sec. 2.1, if and only if its `C_micro` is a
> hypercube up to scale and isometry.

Two directions are kept apart:

- **(PH⇐)** `C_micro` a hypercube up to scale and isometry ⇒ there exists
  an admissible walk on that substrate with `c_0 = r_in`.
- **(PH⇒)** `C_micro` not a hypercube up to scale and isometry ⇒ every
  admissible walk on that substrate has `c_0 < r_in`.

A body with no admissible isotropic untilted node in the declared class is
outside the statement: it is on neither side of the biconditional and is
recorded as `OUTSIDE_DEFINITIONS` (Sec. 3.4).

**The predicate is a geometric classification suggested by the existing
cases, not a physical explanation.** Whether saturation is controlled by
this geometry, or by algebraic and isotropy constraints that coincide with
it on the present table, is the open question (user decision,
2026-11-03).

This contract states only (PH) on the promoted rows. No general statement
about hypercubes or parallelepipeds outside those rows is written here
(Grok, repair 3).

**Zonotope reading (PS′) [UNVERIFIED], product class only, not equivalent
to (PH).** For a walk that is a product of `n` coin–partial-shift factors,
each partial shift moving by `±a_i`, the composite step set is
`F = {sum_i ε_i a_i}` and `C_micro = conv F` is the zonotope
`sum_i [-a_i, a_i]` (convex hull of a Minkowski sum is the Minkowski sum
of the hulls). It is a parallelepiped exactly when the reduced generators
(`a_i` up to sign and positive scale, parallel ones merged) are `d`
linearly independent vectors. (PS′) reads: in the product class, the
ceiling is attained iff the generators reduce to `d` independent
directions. **(PS′) is not equivalent to (PH):** `d` independent
generators need not be orthogonal or of equal length, so a parallelepiped
need not be a hypercube (e.g. a 60° rhombus in `d = 2`). No equivalence is
claimed until proved. Examples in the promoted rows: square (two
generators), BCC/cube (three orthogonal generators), `W_hex` (three
generators at 120°, `d = 2`: the hexagon). The zonotope facts it would use
(e.g. the space-tiling criterion of Shephard 1974 and McMullen 1975) are
cited by Moriyama–Otozawa (arXiv:2411.09141v1) and have not been read
here. Phase 0 records the reduced generators of each product-class row
and gives no verdict on (PS′) beyond the counterexample test of Sec. 4.

## 2. Quantifiers, domain and normalization

1. **Quantifiers.** "The ceiling is attained on a substrate" means: there
   exists at least one admissible walk `W` on that substrate with
   `c_0(W) = r_in(C_W)`. It does not mean that every walk saturates. A
   non-saturating walk on a substrate where another walk saturates is not
   a counterexample to (PH⇐) (e.g. L3s4 on BCC, which in any case has
   `s = 4` and is outside the domain).
2. **Domain.** `s = 2`, `d <= 3`, models with an admissible isotropic
   untilted node, and only the classes already declared in the frozen
   contracts the promoted rows cite (C_ACROSS_LATTICES_GATE,
   HEX_CEILING_GATE, HEX_SUPREMUM_GATE and the row contracts). Rows with
   `s != 2` are recorded and are outside the domain: L5b and L3s4
   (`s = 4`, c-across-lattices report Sec. 4 table); L6b (`s = 6`, CS l. 94
   and l. 106: «`s = 6`, not the parent's `s = 2`», fixed by the promoted
   L6B_TRIANGULAR_ROW gate, which supersedes the parent contract's
   declaration). No extrapolation to other `s`, `d`, lattices or classes.
3. **Substrate.** As in C_ACROSS_LATTICES_GATE Sec. 2: the translation group
   generated by one complete update together with its composite step set.
   Here `N := F`, the composite step set of one complete update (all sums
   of one displacement per partial shift), not the displacement set of a
   single partial shift. `0 ∈ N` does not change `C_micro`, `r_in` or the
   longest step when it is interior.
4. **Normalization and single source per row.** Every row is compared with
   the same frozen definitions (CS Sec. 2): `C_micro := conv(N)`; `h_C`;
   `r_in(C_micro) := min h_C`; `c_0` the isotropic untilted cone speed at
   the massless node (`{T_a, T_b} = 2 c_0^2 delta_ab`, as certified per row
   in the c-across-lattices report Sec. 4); units: longest step 1, one
   update per time unit. **For each row the pair `(r_in, c_0)` is taken
   from exactly one source, in these units.** For L4 that source is the
   c-across-lattices report Sec. 4 table (`r_in = c_0 = 1/sqrt3`); the CS
   Sec. 8 pair (`C_micro = [-1,1]^3`, `r_in = 1`, `c_IR = 1`) is in other
   units and must not be crossed with it (Grok, repair 4). A numerical
   coincidence of speeds, or a value from a different normalization, is
   not a comparison. "Hypercube up to scale and isometry" and
   "parallelepiped" (Minkowski sum of `d` linearly independent segments)
   are checked exactly from the vertices of `C_micro`.
   **Terminology.** Revision 1 said "parallelotope"; in standard use a
   parallelotope is any polytope that tiles space by translations
   (Moriyama–Otozawa, arXiv:2411.09141v1, Sec. 2.2, p. 11), and the
   regular hexagon is one. That word is not used for the predicate.
5. **Pointwise against uniform gap.** (PH⇒) is pointwise:
   `for all W, c_0(W) < r_in(C_W)`. It does not imply a uniform gap
   `sup_W c_0(W)/r_in(C_W) < 1` over a class. Phase 0 makes no claim about
   a uniform gap. T1 (`sqrt3/2`) is a uniform statement for the `n = 3`
   antipodal subclass only; M1-B13 and M1-B19 are qualitative gaps with no
   bound below `r_in`.
6. **Background bound.** `c_0 <= r_in` (L0, Bernstein) holds on the
   declared classes; a row with `c_0 > r_in` would contradict L0, not (PH).
   No such row exists.

## 3. Method (no computation)

Documentary only. No verifier is run, written or edited; no new walk is
built; no numerics.

1. List every promoted row in `state/CURRENT_STATE.md` and the reports it
   cites with `d <= 3`, with its source (`file:line` or section), its
   declared class and its `s`. Rows with `s != 2` are listed and marked
   outside the domain with the citation of Sec. 2.2.
2. For each row in the domain, record from the single source of Sec. 2.4:
   the vertices of `C_micro`; whether it is a hypercube up to scale and
   isometry; whether it is a parallelepiped; for product-class rows, the
   reduced generators (for (PS′)); `r_in`; `c_0`.
3. **Three separate fields per row, never merged** (Grok, repair 5):
   (a) *this walk*: `c_0 = r_in` or `c_0 < r_in`, exact;
   (b) *promoted statement on a class*, quoted with its own quantifier and
   scope (e.g. T1 on the `n = 3` antipodal subclass; M1-B13/B19 on `W_hex^sym`
   with `F` within S13/S19; the whole hexagonal class OPEN);
   (c) *existential reading per substrate*: "some promoted walk on this
   substrate has `c_0 = r_in`" (yes / no promoted witness). A gap on a
   subclass or a bounded support is entered in (b) and is never read as
   (c) "no walk on the substrate saturates".
4. Flag, without resolving, every row where a definition of Sec. 2 does not
   apply as frozen (for example a body whose declared class has no
   admissible isotropic untilted node). Such a row is
   `OUTSIDE_DEFINITIONS`: not a counterexample and not support.
5. Record, as a finding of the audit, that the table contains no
   parallelepiped that is not a hypercube and no non-hypercube body with
   a promoted saturating walk, so it cannot separate (PH) from (PS′) or
   from other predicates that agree on segments, squares, cubes and the
   regular hexagon.

## 4. Counterexample criterion

An exact counterexample among the promoted rows is any of:

- (against PH⇒) a substrate in the domain whose `C_micro` is not a
  hypercube up to scale and isometry, with a promoted walk with
  `c_0 = r_in` exactly;
- (against PH⇐) a substrate in the domain whose `C_micro` is a hypercube up
  to scale and isometry, on which a promoted exact result shows that no
  admissible walk of the declared class attains `c_0 = r_in`.

A failed search, a non-saturating single walk, a gap on a subclass or a
bounded support, or a row outside the domain or the definitions is not a
counterexample.

## 5. Outcomes

Two separate outcomes, reported together.

**Definitional outcome.**

- `DEFINITIONS_CLOSED`: every row in the domain has a single traced source
  in the units of Sec. 2.4, all fields of Sec. 3.2–3.3 are filled from
  promoted exact data, and the `OUTSIDE_DEFINITIONS` list is explicit.
  Meaning: the statement is defined well enough to be tested for
  refutation. Nothing more.
- `OPEN_AFTER_ROW_SURVEY`: some needed quantity is missing, not exact, or
  has no single source; the list of gaps is reported.

**Counterexample check** (per direction, PH⇐ and PH⇒):

- `REFUTED_BY_ROW_<row>`: one exact counterexample (Sec. 4). The
  formulation of Sec. 1 stops at once.
- `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`: no counterexample among the promoted
  rows. **This is not independent evidence for (PH)**: the statement was
  read off this table, which has three hypercube shapes and one
  non-hypercube shape (the regular hexagon), and no parallelepiped that is
  not a hypercube. The verdict is never `CONFIRMED`, and it must be
  reported in the same sentence as this caveat.

**No outcome of this gate authorizes any later phase.** In particular,
`NO_COUNTEREXAMPLE_IN_SOURCE_TABLE` is not a condition for, nor a reason
to start, any test of refutation; each later phase is chartered on its
own (Grok, repair 6).

## 6. Exclusions

`s != 2`, `d > 3`, bodies without an admissible isotropic untilted node,
new lattices, new walks, masses, `V_grp^max`, inhomogeneous or encoded
walks, uniform gaps, general QCA laws, claims about our universe, any
physical explanation of the predicate. No novelty claim. No computation of
any kind in this gate.

## 7. After this gate (not authorized here)

A test that can fail needs its own contract, with a shape or support not
in the source table. The user's stated first choice (2026-11-03) is the
hexagon: look for an admissible hexagonal family with exactly
`c_0 = r_in(C_micro)`. Finding one would refute (PH⇒); not finding one
would not prove (PH). The user prefers it to the rhombus because the
hexagonal substrate is already studied and a rhombus without an admissible
isotropic node would be outside the domain. Its exact scope (larger
support at `s = 2`, larger `s`, or both) is to be fixed in that contract.

## 8. Deliverables

A report `reports/YYYY-MM-DD--substrate-saturation-phase0.md` with the row
table of Sec. 3, each entry traced to its single source, the
`OUTSIDE_DEFINITIONS` list, the audit finding of Sec. 3.5 and the outcomes
of Sec. 5. Then independent cross-family review (user permission needed to
send), then a separate promotion decision.
