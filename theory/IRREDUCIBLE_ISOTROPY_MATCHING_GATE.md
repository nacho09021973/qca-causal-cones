# IRREDUCIBLE ISOTROPY MATCHING GATE

**Status: OPEN — charter written 2026-10-28; execution NOT authorized.** Only the
user authorizes execution, and the authorization is recorded in
[CURRENT_STATE](../state/CURRENT_STATE.md). This charter records no computation,
candidate or theorem.

Authority: [CURRENT_STATE](../state/CURRENT_STATE.md) Sec. 4 (`B_infty^*`, row
"irreducible internal symmetry representation `R` for `s>2`: OPEN").
Predecessor: [`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](MASSLESS_INRADIUS_RIGIDITY_GATE.md),
completed by counterexample in the declared s=4 class
([`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md)). Its Sec. 0 (definitions of
`S_n`, `h_infty`, `c_strict^iso`, `rho_micro`, and the split into rigidity (i) and
saturation (ii)), Sec. 3 (exact admission checks) and Sec. 5 (outcome vocabulary) are
inherited unchanged unless amended below.
User instruction: "prepara la carta para la hipótesis 3" (2026-10-28).

## 0. Why this gate, and a fact that fixes its shape

The s=4 counterexample keeps `C_infty^strict = C_micro`, `c_strict^iso = 1/sqrt(3)`, and
has `c_0(a) = a/sqrt(3)`. Its declared isotropy is the group `D2` of half-turns, with
`R_i = sigma_i (x) I_2`, which is **reducible** (two copies of the Pauli projective class).
The question is whether requiring an **irreducible** internal representation restores
`c_0 = c_strict^iso`.

Checked before writing this charter (an inspection command, not a certificate): with
`N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`,

- `D2` (order 4) splits `N_3` into two orbits of size 4;
- the tetrahedral rotation group `T` (order 12) also splits it into two orbits of size 4;
- the cube rotation group `O` (order 24) acts transitively (one orbit of size 8), and the
  stabilizer of a vertex has order 3.

`D2` is abelian, so its projective irreducible representations have dimension at most 2.
Under `D2`, "irreducible `R` with `s > 2`" is an empty requirement, and the hypothesis would
reduce to the open `s = 2` rows. The isotropy group must therefore be enlarged. Two
enlargements are declared, as separate classes:

- `T`, the tetrahedral rotation group (order 12). Like `D2`, it is transitive on each of the
  two tetrahedra `S_+` and `S_- = -S_+`. That is the transitivity used in the P17
  classification (transitivity on `S_+`; source audit
  [`2026-09-14--massless-rigidity-source-audit.md`](../reports/2026-09-14--massless-rigidity-source-audit.md)).
  Its projective irreducible representations (linear representations of the binary
  tetrahedral group `2T`, order 24) have dimensions 1, 1, 1, 3 (linear) and 2, 2, 2
  (spinorial). So `s = 3` is possible and `s = 4` is not.
- `O`, the cube rotation group (order 24), the smallest of the groups checked that is
  transitive on all of `N_3`. Its projective irreducible representations (linear
  representations of the binary octahedral group `2O`, order 48) have dimensions
  1, 1, 2, 3, 3 (linear) and 2, 2, 4 (spinorial). So `s = 3` and `s = 4` are possible.

These dimensions are standard and pass the sum-of-squares check (12+12 = 24, 24+24 = 48).
Their check against a primary source or an explicit character table is an item of Step 0.

Changing the group from `D2` to `T` or `O` is an additional hypothesis. A result for one
group does not speak to another, and none speaks to `D2`-isotropic classes.

## 1. Question

In d=3, with the cubic baseline geometry, does every admissible massless symbol whose
internal representation of `O` is irreducible satisfy rigidity (i):

\[
c_0 = c_{\rm strict}^{\rm iso}
\]

for its own strict asymptotic body? Or is there an admissible symbol with
`0 < c_0 < c_strict^iso`?

Three separate quantified classes, each judged on its own:

- **Class T3:** group `T`, `s = 3`, `R` the irreducible 3-dimensional linear
  representation of `T`.
- **Class O3:** group `O`, `s = 3`, `R` an irreducible 3-dimensional linear representation
  of `O` (either of the two, declared).
- **Class O4:** group `O`, `s = 4`, `R` the irreducible 4-dimensional spinorial (projective)
  representation of `O`.

A result in one class says nothing about the others. Since `T` is a subgroup of `O` and
the 3-dimensional irreducible representations of `O` restrict to the one of `T`, every O3
symbol is also a T3 symbol. A T3 counterexample therefore does not transfer to O3, while an
O3 counterexample is also one for T3.

## 2. Frozen class declaration (all classes)

| Item | Declaration |
| --- | --- |
| Geometry | d=3; `N_3` as above, all eight displacements active (`T_h != 0` for every `h` in `N_3`); no on-site term; one complete update per time unit; Fourier convention `U(k) = sum_h e^{-i k.h} T_h`, as in the predecessor |
| Isotropy | The declared group `G` in {`T`, `O`} acting on `N_3` and on `k` by its defining 3x3 matrices; covariance `T_{gh} = R_g T_h R_g^dagger` for every `g` in `G`, equivalently `U(gk) = R_g U(k) R_g^dagger`. No reflections, parity or antiunitary symmetry are required or assumed |
| Internal symmetry | `R` fixed per class as in Sec. 1, irreducible, up to unitary equivalence; projective phases are allowed in O4 and must be declared explicitly |
| Dynamics irreducibility | Recorded, not assumed: the joint commutant of `{T_h}` is computed for every candidate. Irreducible `R` implies it, by Schur's lemma, only for `O`-commuting operators; the record keeps the two notions apart |
| Gapless sector | Node `k_star`, quasienergy origin, sector dimension and isolation declared per candidate. The node must be `O`-invariant or its orbit must be declared; an isotropic, untilted, linear cone in every direction is required (predecessor Sec. 3) |
| Coverage | Declared per step: the full `O`-covariant coefficient class, or an explicit ansatz with its coverage ceiling |
| Equivalences | Constant basis changes commuting with `R` up to the declared projective class, global phases, node relabelings within an orbit |

Consequences of the declaration, to be derived exactly in Step 1 and not assumed. Under
`O`, which is transitive on `N_3`, the eight coefficients are fixed by one `T_{h0}`. Under
`T`, they are fixed by one coefficient on each tetrahedron, `T_{h0}` and `T_{-h0}`. In both
cases each fixed coefficient must commute with `R` restricted to the order-3 stabilizer of
its vertex.

## 3. Sequence

**Step 0 — sources and controls (no new scientific claim).**

1. Read the isotropy definitions and classification assumptions in the primary sources
   already used for the Pavia baseline. These include D'Ariano–Erba–Perinotti,
   arXiv:1708.00826 (local copy in `biblioteca/`), and the source of the "P17
   classification" cited in CURRENT_STATE Sec. 4. Record which group, which `s` and which
   representation they quantify over. Check whether the question of Sec. 1 is already
   answered there. Unread items stay `[UNVERIFIED]`.
2. Verify the irreducible dimensions of `2T` and `2O` from a primary source or from an
   exact character-table computation kept in `scripts/`.
3. **Control A:** determine exactly whether the standard Pavia `s=2` Weyl symbols are `T`-
   and `O`-covariant with a 2-dimensional spinorial irreducible representation. This is a
   consistency control of the classes, not a result.
4. **Control B (decisive first test for O4):** determine exactly whether the s=4 family
   `A_a` admits `O`-covariance for some `R` and, if so, whether that `R` can be the
   irreducible 4-dimensional one.
   - If yes for some `0 < a < 1`, with all O4 admission checks passing and the existing
     `c_strict^iso` certificate applying unchanged, the outcome is
     `COUNTEREXAMPLE_VERIFIED` for class O4 and the gate stops for O4.
   - If `A_a` is not `O`-covariant with that `R`, record `S4_FAMILY_OUTSIDE_O4` and
     continue. This is not evidence for rigidity.
   - The family has `s = 4` and is therefore outside T3 and O3 by definition.

**Step 1 — exact class derivation.** For each class, derive the constraints on `T_{h0}`
from stabilizer covariance and the unitarity identities of the predecessor's Sec. 3, before
choosing any ansatz. Record the dimension and connected components of the solution set if
they can be determined exactly. If the class is empty, the outcome is `EMPTY_CLASS` for
that class.

**Step 2 — massless sectors.** Within the derived class, find the admissible gapless
sectors and their linear slopes `c_0`, exactly.

**Step 3 — strict body and comparison.** For each admissible candidate, certify
`c_strict^iso` exactly. Use the vertex lemma when every vertex coefficient is
non-nilpotent; otherwise compute it, because vertex nilpotency alone decides nothing
(predecessor erratum). Then compare it with `c_0`.

## 4. Admission, stop rules and budget

- Admission checks are those of the predecessor's Sec. 3, with `O` and the declared
  irreducible `R`. The first failed check makes a candidate `INADMISSIBLE_CANDIDATE`, and its
  certification stops there.
- Exact algebra only. A finite scan or a numerical search may suggest candidates but
  certifies nothing. Every retained computation is a versioned script in `scripts/`, run
  through `run_all_verifiers.py` before commit.
- Stop for a class at its first terminal outcome (Sec. 5).
- Budget: Steps 0–1 for the three classes are one authorization. Steps 2–3 need a separate
  user authorization after Step 1 is reported, because their cost depends on the dimension
  of the class found there.
- If Step 1 shows the constraint system is not tractable exactly within that
  authorization, stop with `OPEN_AFTER_CLASS_DERIVATION` and report what was derived.

## 5. Outcomes and claim ceilings (per class)

| Outcome | Meaning |
| --- | --- |
| `COUNTEREXAMPLE_VERIFIED` | An admissible symbol in the class with `0 < c_0 < c_strict^iso`, exactly certified. Irreducibility under `O` does not force matching for that `s`. |
| `RIGIDITY_PROVED_FOR_FROZEN_CLASS` | `c_0 = c_strict^iso` proved for every admissible member, with every restriction retained. Says nothing about other `s`, other groups or reducible `R`. |
| `EMPTY_CLASS` | No symbol satisfies the class constraints. The hypothesis is vacuous for that `s`, which is a first-class negative result. |
| `INADMISSIBLE_SATURATION` | As in the predecessor: (i) holds but `c_strict^iso < rho_micro`. Not a rigidity counterexample. |
| `S4_FAMILY_OUTSIDE_O4` | Control B only: the known s=4 family is not `O`-covariant with the irreducible 4-dimensional `R`. It decides nothing by itself. |
| `OPEN_AFTER_CLASS_DERIVATION` / `INCONCLUSIVE` | No certified counterexample, no exhaustive proof. |

Ceilings retained: no result here establishes A (species universality), matching under
`D2`, or any statement about nature. A rigidity result would mean that, under the declared
group and irreducible `R` at that `s`, `c_0` is fixed by the strict causal geometry. It would not
derive the numerical value of `c`, since the absolute scale is not derivable
(`NO_ABSOLUTE_SCALE_DERIVABLE`, Sec. 8.21). Novelty requires a separate source comparison.
No causal sets, random lattices, interactions, anisotropic detours or new substrate classes
are authorized by this charter.

## 6. Review

Any terminal outcome is reviewed by a model of a different family (`sanedrin` or
`revision-ciega`) before it enters CURRENT_STATE as more than PRELIMINARY. The review
record cites the SHA-256 of the reviewed report and the base commit.
