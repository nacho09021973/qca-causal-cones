# Minimal s=2 rigidity gate: stage (a), Steps 0′ and 0 — 2026-10-29

## Provenance

- **Charter:** [`MINIMAL_S2_RIGIDITY_GATE.md`](../theory/MINIMAL_S2_RIGIDITY_GATE.md), preregistration
  commit `785565c`.
- **Authorization:** stage (a) recorded in `ef0ed24` ("autorizo la etapa a"). The user reduced the
  budget to 1 hour ("reduce el presupuesto a 1 hora y a ver que pasa").
- **Timing:** started 11:09 UTC. The certificate was written and passing by 11:11 UTC; the full
  sweep ran after that.
- **Certificate:** `scripts/verify_minimal_s2_step00.py`, SHA-256 `d6bf4189357f62fa…`. 16/16
  exact checks, under 1 s, Python 3.12.3, SymPy 1.14.0.
- **Full sweep:** 48/48 verifiers pass at base `3c7a98c` plus these uncommitted files
  ([record](2026-10-29--minimal-s2-step00-run_all.tsv)). The stage ended at 11:24 UTC, about
  15 minutes of the 1-hour budget.
- **Evidence level:** **PRELIMINARY**. Author-side computation. Charter Sec. 6 requires a
  different-family review of the Step 0′ enumeration before any later stage uses it.
- **Grok review, 2026-10-29**, of the bytes in `dc4a6f7`. Verdict: mathematically correct, not
  promotable as written, three repairs
  ([review and author reading](../debates/2026-10-29--minimal-s2-step00-review-grok/verificacion_autor.md)).
  The repairs are applied here:
  - G-S0-01: `E` is now built in the certificate.
  - G-S0-02: proof of 2-generation added below.
  - G-S0-03: class counts and survivors are now required.

  That repaired certificate had SHA-256 `a2abbe32a98ac005…` and passed 22/22 exact checks, with
  a full sweep of 48/48 ([record](2026-10-29--minimal-s2-step00-repair-run_all.tsv)).
- **Grok round 2**, of the bytes in `3bcf7b6`
  ([review](../debates/2026-10-29--minimal-s2-step00-review-grok-r2/verificacion_autor.md)).
  - Accepted G-S0-01 and G-S0-03.
  - Found the G-S0-02 proof incomplete.
  - Raised three new points: the trace of `ρ_E` on `D4`, the wording «single tuple», and that
    `Q8` is not computed.

  All were repaired. The current certificate has SHA-256 `adeb8afc4d4be5ed…` and passes 23/23,
  with a full sweep of 48/48 ([record](2026-10-29--minimal-s2-step00-repair2-run_all.tsv)).
- **Grok round 3**, of the bytes in `ebebca7`
  ([review](../debates/2026-10-29--minimal-s2-step00-review-grok-r3/verificacion_autor.md)).
  - No mandatory objection open.
  - The 2-generation proof is complete.
  - The `D4` check uses the trace of `ρ_E`.
  - The wording repairs suffice.
  - The only remark was this duplicated provenance sentence, now fixed.

## Result

| Item | Outcome |
| --- | --- |
| Step 0′, family P | Three classes up to conjugation in `O`: `(V4, tetrahedron)`, `(T, tetrahedron)` and `(C4, face)`. `C4` does not contain the axial `V4`. |
| Step 0′, family F | `{D4, O}` up to conjugation; both contain the axial `V4`. |
| Step 0′, representations | Projective classes of 2-dimensional `R` per group: `V4`: 5; `T`: 3; `C4` (face): 3; `D4`: 6; `O`: 4. These count characters of the fixed representative group, not orbits of tuples `(G, S, R)`. In `(V4, tetrahedron)` the three characters with kernel of order 2 form a single orbit (of three tuples) under the stabilizer `T`. Survivors are unaffected (G-S0-03). |
| Step 0, kernel lemma | Every class with a nontrivial projective kernel is `EMPTY_CLASS`. Each certificate is a single shift whose pairs stay inside kernel orbits. The certificates do not depend on `s`. |
| Survivors (to Step 4b, not authorized) | Exactly one class per group: the faithful `ρ` (trivial projective kernel). These are `(V4, tet, Pauli)`, `(T, tet, image A4)`, `(C4, face, image C4, reducible)`, `(D4, image D4)` and `(O, image O)`. |
| A1 (tetrahedron and face) | VERIFIED |
| A2 / A7 (`E` of `2O`) | VERIFIED after repair G-S0-01. The certificate builds `E` as the standard representation of `S3` composed with the axis permutation `O → S3`. Its projective kernel is exactly the axial `V4`, and it is the unique `O` class with that kernel, the one emptied. Its restriction to `D4` has projective kernel containing `V4`, so it is also emptied. Round-2 repair: the restriction is checked with the trace of `ρ_E: O → SO(3)` (3, −1, 0 by the order of the axis permutation), giving `ρ_E|D4 = 1 ⊕ α ⊕ α`, where `α` is the sign of `D4/V4`. v2 had summed the character of the 2-dim irrep instead, which coincides here but not in general (for example on `C3`). The preimage `Q8` of `V4` in `2O`, mentioned in the charter's A2, is **not** computed. The original v1 certificate (`d6bf4189…`) did not build `E`. |
| A3 (s = 1) | VERIFIED |
| A4 (`C4` on a face, without `V4`) | VERIFIED |
| A5 (F = `{D4, O}`) | VERIFIED |
| A6 (kernel transitive on `N_3`) | VERIFIED |
| A8 (rank one; non-nilpotent iff `tr T_h != 0`) | VERIFIED |
| Step 0.4 (ceiling scope) | The general ceiling's `D2` hypothesis holds for the `V4`, `T`, `D4` and `O` classes. It does **not** hold for `(C4, face)`. Node transport is not examined at this stage, since no nodes are computed yet. |

**What this changes:** the open row "`s=2` without Eq. (2)" is reduced to five classes, all with
a faithful projective action. Every non-faithful class in the declared families is empty. That
includes the linear `E` of `2O` at `s=2`, an open row of CURRENT_STATE Sec. 4.

**What it does not change:** nothing is said about `c_0`, `c_strict^iso`, Q-a or Q-b. The
equality question is untouched.

## Method

**Group.**
- `O` is the set of 24 proper signed permutation matrices. All arithmetic is with integers.
- Every subgroup of `S4 ≅ O` is generated by at most two elements, so closing all ordered pairs
  gives every subgroup. The closure of a pair is the subgroup it generates: in a finite group,
  `g^{-1} = g^{n-1}` when `g^n = 1`, so the generated monoid is a subgroup. The proof is by order
  (G-S0-02, completed after the Grok round-2 review, which supplied the arguments). By Lagrange a
  subgroup has order 1, 2, 3, 4, 6, 8, 12 or 24. Element orders in `S4` are 1, 2 (transpositions,
  double transpositions), 3 (3-cycles) and 4 (4-cycles).
  - **No `C2³`.** The 6 transpositions form one class, so the centralizer of `(12)` has order
    `24/6 = 4`: it is `{1, (12), (34), (12)(34)}`. An elementary abelian 2-subgroup containing a
    transposition therefore has order ≤ 4. One without transpositions lies in
    `{1} ∪ {double transpositions}`, which is the normal `V4`, of order 4.
  - **Orders 1–4:** cyclic or `C2×C2`, both 2-generated.
  - **Order 6:** a group of order 6 is `C6` or `S3`. There is no element of order 6, so it is
    `S3 = ⟨(12),(13)⟩`, since `(12)(13)(12) = (23)`.
  - **Order 8:** it is a 2-Sylow. The 2-Sylows are conjugate, and one of them is the dihedral
    `⟨r, s⟩` (`r⁴ = s² = 1`, `srs = r⁻¹`), which is 2-generated. Equivalently: of the five groups
    of order 8, only `C2³` is not 2-generated, and it is excluded above.
  - **Order 12:** index 2, hence normal. The only index-2 subgroup is the kernel of the sign,
    `A4`. Conjugating `(124)` by `(123)` gives `(234)`; further conjugations give all eight
    3-cycles, which generate `A4`. So `A4 = ⟨(123),(124)⟩`.
  - **Order 24:** with `b = (1234)` and `a = (12)`, `bab⁻¹ = (23)` and `b(23)b⁻¹ = (34)`. The
    transpositions `(12), (23), (34)` generate `S4`, so `S4 = ⟨(12),(1234)⟩`.

  The certificate finds 30 subgroups. That number is a cross-check, not the proof.

**Family P.**
- All 30 subgroups are crossed with all 16 choices of `S_+`, keeping the pairs where `G`
  stabilizes `S_+` and is transitive on it.
- Classes are taken up to `O`-conjugation of the pair.
- The 16 choices of `S_+` are 2 tetrahedra, 6 faces and 8 "vertex plus three neighbours" sets.

**Family F.** The subgroups transitive on all eight vertices, up to conjugation.

**Representations.**
- A 2-dimensional projective unitary `R`, up to projective equivalence `R' = c W R W^†`, is a
  homomorphism `ρ: G → PU(2) ≅ SO(3)` up to `SO(3)` conjugation. Covariance
  `T_{gh} = R_g T_h R_g^†` depends only on `ρ`.
- Every image type that occurs (1, `C2`, `C3`, `C4`, `V4`, `D3`, `D4`, `A4`, `S4`) is
  `SO(3)`-conjugate to a subgroup of `O`, so enumerating homomorphisms into `O` is exhaustive.
  For these five domains the counts do not need the general classification of finite subgroups
  of `SO(3)`:
  - the images are quotients of the domain;
  - the trace of a rotation is fixed by its order: 3, −1, 0, 1 for orders 1, 2, 3, 4.

  This enumerates the possible characters directly; the Grok review carries it out group by
  group.
- Two classes are identified iff their 3-dimensional characters agree. Equal real characters
  give orthogonal equivalence, and replacing `M` by `−M` makes it `SO(3)`.
- `R` is reducible iff the trivial multiplicity of `ρ` is at least 1, meaning a fixed axis.
- The projective kernel of `R` is `ker ρ`.

**Kernel lemma (A1, A6, A7).**
- If `R` is scalar on `K = ker ρ`, then `T` is constant on `K`-orbits.
- Take a shift `ℓ != 0` whose pairs `(h, h+ℓ)` all lie inside `K`-orbits. Its unitarity identity
  `Σ T_h^† T_{h+ℓ} = 0` becomes a sum of positive semidefinite terms `T_h^† T_h`.
- So every `T_h` that appears vanishes, which contradicts `T_h != 0`.
- The certificate prints the shift and the pairs for every emptied class.

**A3, A8.**
- The shift `(2,2,2)` has the single pair `((−1,−1,−1), (1,1,1))`.
- Each shift `2h` has the single pair `(−h, h)`. With `T_{−h}^† T_h = 0` and both nonzero, both
  have rank one.
- Cayley–Hamilton, `T^2 = tr(T) T − det(T) I`, is checked symbolically.

**Controls.**
- Negative: the Pauli class `(V4, tetrahedron, faithful)` gets no certificate.
- Positive: both Pavia chiralities satisfy all unitarity identities with all eight `T_h != 0`.
  This reuses the step-01 extraction read-only.

## Cross-reference, not a result of this stage

Two survivors coincide, as projective classes, with **controls** of the reviewed irreducible
isotropy certificate:
- `(T, tetrahedron, faithful)` is the step-01 `T2s` control (spin 1/2 under `T`).
- `(O, faithful)` is the step-01 `O2s` control.

Both gave unit Groebner ideals there
([report](2026-10-28--irreducible-isotropy-step01.md)). They were controls, not declared classes.
The charter does not let them settle anything here. They are recorded as **anticipations for
Step 4b-1**, `[UNVERIFIED in this charter]`.

The genuinely new survivors are:
- `(V4, tet, Pauli)` without Eq. (2), the class that contains Pavia;
- `(C4, face)`, which the ceiling does not cover;
- `(D4, image D4)`.

## Scope and limits

- **Frozen classes only:** d=3, `N_3` with all eight `T_h != 0`, no on-site term, proper cube
  rotations, the families of the charter. Emptiness results hold for any internal dimension `s`,
  but this charter states them at `s=2` and `s=1`.
- **Exhaustiveness of Step 0′** rests on the 2-generation of the subgroups of `S4`, proved above
  by order, and on the order/trace argument for the characters. The exact enumeration covers the
  rest. Grok reviewed the enumeration (first round). The repaired certificate needs a second
  review before Steps 4a and 4b use it.
- **Not done:** nodes, `c_0`, `c_strict^iso`, Q-a, Q-b, and the transport of the ceiling to
  nonzero nodes.
- **No novelty claim.**
