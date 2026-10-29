# S=3 ISOTROPIC RIGIDITY GATE

**Status: OPEN — charter frozen 2026-10-29 from draft v3, by user instruction ("si a ambas", in
answer to "¿congelo el v3 y autorizo la etapa (a)?"). This commit is the preregistration
commit.** Execution is authorized stage by stage only, each authorization recorded in
[CURRENT_STATE](../state/CURRENT_STATE.md) with its budget (Sec. 4). The body below is the v3
text, unchanged. It records no computation, candidate or theorem.

Drafting history:
- **v1** (`5fe04ae`) was reviewed blind by Grok (xAI family), which returned **NOT_READY** with ten
  repairs G-S3-01..10
  ([review and author reading](../debates/2026-10-29--s3-charter-draft-review-grok/verificacion_autor.md)).
- **v2** applies G-S3-01..05 and 07..10. G-S3-06 is rejected (the explicit `s=2` witness is
  supported on `N_3`, as the 4b-1 certificate checks); its control is replaced anyway.
- **v3** applies the round-2 Grok objections G-S3-R2-01..04 (wording; round 2 found every
  round-1 repair resolved except G-S3-08, partial, and confirmed the G-S3-06 rejection)
  ([review and author reading](../debates/2026-10-29--s3-charter-draft-v2-review-grok/verificacion_autor.md)).
- User decisions recorded in v1 and kept: D1 both sector ranks; D2 keep family F; D3 Grok as
  reviewer.

**Authority:** [CURRENT_STATE](../state/CURRENT_STATE.md), Sec. 4 and the entries of 2026-10-29:
- `s=2`, families P and F of the minimal charter: only `(V4, tetrahedron, Pauli)` is nonempty
  (Step 4b-1), and there `c_0 = c_strict^iso = rho_micro = 1/sqrt(3)` at every node (Step 4b-2).
  Both ESTABLISHED IN THE DECLARED FAMILIES/CLASS (`014753e`, `ea3f401`).
- `s=4`: strong `B_infty^*` REJECTED IN THE DECLARED s=4 CLASS
  ([`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md)).
- `s=3` with an irreducible `R` under `T` or `O` (classes T3, O3): EMPTY_CLASS, promoted to
  ESTABLISHED IN THE DECLARED CLASSES in `CURRENT_STATE` (`5424771`, Gemini ACCEPT, Grok
  ACCEPT_WITH_REPAIRS). The header of
  [`IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`](IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md) still says
  PRELIMINARY; `CURRENT_STATE` prevails. Reused here, not recomputed.
- Every other `s=3` isotropy class on `N_3` is OPEN and unchartered.

**Predecessors, inherited unless amended below:**
- [`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](MASSLESS_INRADIUS_RIGIDITY_GATE.md): Sec. 0
  definitions, vertex-lemma erratum, Sec. 3 admission checks, Sec. 5 vocabulary.
- [`MINIMAL_S2_RIGIDITY_GATE.md`](MINIMAL_S2_RIGIDITY_GATE.md) (`785565c`): units and lattice
  (Sec. 1), families P and F, covariance, class identification under conjugation in `O`
  (Sec. 2), the 4b-1 encoding of class derivation (Sec. 3), stop rules (Sec. 4), outcome
  vocabulary (Sec. 5), review (Sec. 6). **Not inherited:** the 4b-2 sector encoding, A8, the
  `PU(2) ≅ SO(3)` method and the representation counts of stage (a), all specific to `s=2`.
- The general ceiling `c_0 <= c_strict^iso`
  ([`STRICT_CONE_CEILING_N3_GATE.md`](STRICT_CONE_CEILING_N3_GATE.md),
  PROVED_UNDER_FROZEN_CONTRACT): any fixed `s >= 2`, `D2` covariance, node `k_star = 0`, sector
  rank `2 <= r <= s`, rows "Selected cone" and "Other slopes".

## 0. Why this gate, and what is already anticipated

`s=2` is rigid in its only nonempty declared class; the declared `s=4` class is not rigid. This
gate asks what happens at `s=3` in families P and F: vacuous, rigid, or with a counterexample.
**All outcomes have equal standing.** A vacuous result concerns these families only. It would
not say which internal dimension is the smallest non-rigid one on `N_3` in general.

**Anticipations (not results).** Written by Claude, reviewed once by Grok, `[UNVERIFIED]` until
certified in Step 0.
- B5 (main; corrected by G-S3-01). **Determinant parity.** Every term of `det U` is a product of
  three coefficients, so its frequency is a sum of three vectors of `{±1}^3` (in `ε`
  coordinates): every coordinate is odd, never 0. A3 of the minimal charter makes the unimodular
  Laurent polynomial `det U` a single monomial `ζ e^{-ik·m}`, with `m` in that odd coset.
  Covariance, with linear or projective `R`, gives `det U(gk) = det U(k)`, so `g^T m = m` for every
  `g ∈ G`. `V4` (contained in `V4`, `T`, `D4`, `O`) fixes only `0`; the face `C4` fixes only its
  axis, whose vectors have two zero coordinates. **If certified, all five classes are
  `EMPTY_CLASS`, uniformly in `R`.** The argument uses `s` odd and no on-site term.
- B1. **Projective classes in dimension 3.** For a cocycle `ω` of `R`, `det` gives `[ω]^3 = 1`.
  If the exponent of `[ω]` in the Schur multiplier of `G` is prime to 3, `[ω] = 1`. Step 0′ (only
  if Step 0 does not close) checks the multiplier exponent per subgroup type of `O` (cyclic, `V4`, `S3`, `D4`, `A4`, `S4`); the
  exponent is that of the cohomology class, not of a representative cocycle.
- B2. **Rank bound.** The shift `2h` has the single pair `(−h, h)`, so `T_{−h}^† T_h = 0` and
  `T_h T_{−h}^† = 0`; hence `rank T_h + rank T_{−h} <= 3`, with pairs `(1,1)`, `(1,2)`, `(2,1)`.
  The criterion `tr T_h != 0` for non-nilpotency holds only at rank one.
- B3. **Scalar kernel.** If `ker_proj R` contains a subgroup transitive on each half `S_±` (P) or
  on `N_3` (F), A1 of the minimal charter applies unchanged (face case with the tangential shift
  `(0,2,2)`): `EMPTY_CLASS`. Examples: `χ ⊕ χ ⊕ χ` on `V4`; `ρ_2 ⊕ χ` of `O` with `χ` trivial on
  `V4`.
- B4. **No block-diagonal symbols.** For `R = R_2 ⊕ χ`, a block-preserving unitary covariant
  symbol is impossible (the scalar block is constant on orbits of size >= 4, and A3 forbids it).
  **B4 empties no class:** mixed symbols remain for Step 1.
- B6. **Ceiling scope.** At `k_star = 0`, every class whose group contains the axial `D2` (`V4`,
  `T`, `D4`, `O`) is inside the ceiling's frozen class. At `k_star != 0` only through the node
  transport of the minimal charter (`g^{-1} k_star − k_star ∈ Λ^*` for every `g ∈ D2`). The face
  `C4` class is not covered as a class, but a symbol of it that is also `D2`-covariant is.

**Outside this charter:** B5's argument, if correct, applies to every odd `s` on `N_3` without
on-site term under these groups. Any such statement needs its own charter.

## 1. Question

Units, lattice and Brillouin torus as in the minimal charter, Sec. 1, with `s = 3`:

\[
\forall \mathcal C,\ \forall U \in \mathcal C,\ \forall (k_\star,\omega_\star,P)\ \text{admissible}:\quad
c_0(U,k_\star,P) = c_{\rm strict}^{\rm iso}(U)\ ?
\]

`𝒞` ranges over the classes of Sec. 2, excluding T3 and O3 (reused as empty).

**Sector encodings (G-S3-02), one per rank (D1: both):**
- `r = 2`: `P` is the spectral projector of `U(k_star)` onto an isolated eigenvalue
  `e^{-iω_star}` of multiplicity 2. In every unit direction `q̂`, the two branches emerging from
  `P` have phases `ω_star ± c_0 |q| + o(|q|)` along `q = |q| q̂`, with the same `c_0 > 0`,
  untilted. The third (spectator) eigenvalue is isolated at the node; it is outside `P`, and its
  slope is not constrained.
- `r = 3`: `U(k_star) = aI`, `|a| = 1`. In every unit direction `q̂`, the branches include phases
  `ω_star ± c_0 |q| + o(|q|)`, with the same `c_0 > 0`, untilted. The third slope is a function of the
  direction, recorded, never counted as a cone (it may be 0, a flat branch).
- These follow the ceiling's rows "Selected cone" and "Other slopes". The 4b-2 identities
  `tr H_j = 0`, `½ tr(H_j H_l) = c_0^2 δ_jl` are **not** used as definitions.

Counterexample direction (G-S3-07):
- Where the ceiling covers the tuple (B6), only `c_0 < c_strict^iso` is a counterexample.
- A witness with `c_0 > c_strict^iso` in a covered tuple is a **conflict** with the ceiling. It is
  reviewed before any other outcome.
- Elsewhere both directions are admitted; a witness above must show that its tuple does not meet
  the ceiling's hypotheses on its own.

Saturation (`c_strict^iso = rho_micro`) is a separate question.

**Q-a3.** On symbols with an admissible node: `T_{gh} != T_h` for every `g ∈ G` and `h ∈ D_𝒞`
with `g h != h`, where `D_𝒞 = S_+` in family P and `D_𝒞 = N_3` in family F.

There is no Q-b: no `s=3` certificate exists to transport. Hence Step 2 must cover the whole real
solution set of each class; a certified point never authorizes a universal statement.

## 2. Frozen class declaration

| Item | Declaration |
| --- | --- |
| Geometry | d=3; `N_3`, all eight `T_h != 0`; no on-site term; one complete update per time unit; `U(k) = Σ_h e^{-ik·h} T_h` |
| Internal dimension | `s = 3` only |
| Families | P and F as in the minimal charter. Only the five geometric pairs of its reviewed stage (a) are reused: family P = `(V4, tetrahedron)`, `(T, tetrahedron)`, `(C4, face)`; family F = `D4`, `O`. Its representation counts are not reused |
| Representations (G-S3-03) | Every 3-dimensional projective unitary `R`, up to **projective** equivalence: `R'_g = c_g W R_g W^†`. Covariance depends on `R` only through `Ad R`, so classes are counted modulo tensoring by a 1-dimensional character, and then modulo conjugation by the normalizer in `O`. Known collisions: in `O`, `ρ_2 ⊕ 1 ~ ρ_2 ⊕ sgn` and `1 ⊕ 1 ⊕ sgn ~ 1 ⊕ sgn ⊕ sgn`; in abelian groups, `(χ_i) ~ (ψ χ_i)`. In `C4`, `χ` and `χ̄` are identified only if an element of `O` normalizing `C4` inverts it (no antiunitaries). Irreducible `R` under `T` or `O` is T3/O3 and is excluded |
| Fidelity | `ker_proj R` recorded per class before Step 1; B3 applies where it contains a transitive subgroup |
| Covariance | `T_{gh} = R_g T_h R_g^†` for every `g ∈ G`; no reflections, parity or antiunitaries |
| Eq. (2) | Not assumed; recorded (Q-a3) |
| Node and sector | Sec. 1: every admissible node, ranks 2 and 3 |
| Coefficient domain | Real variables over all reals; exact algebra |

## 3. Sequence

**Step 0 — parity lemma first.** Exact certificate and written proof of B5:
1. every monomial of `det U` for a generic `3x3` symbol on `N_3` has all coordinates odd
   (symbolic expansion with generic coefficients, and the parity argument);
2. A3 (a unimodular Laurent polynomial on the torus is a monomial), reused from the minimal
   charter's stage (a);
3. for each of the five groups, the **common** fixed space `{m : g^T m = m for every g ∈ G}`
   meets the odd coset trivially (the intersection over the whole group, not element by element:
   a 3-fold rotation of `T` or `O` alone fixes the odd vector `(1,1,1)`);
4. negative control: the same computation at `s = 2` and `s = 4` does produce the constant
   frequency (where unitary symbols exist);
5. positive control: the certified Pavia symbols (`s=2`) satisfy `det U = const` in their class.

If Step 0 closes, the union outcome is `S3_VACUOUS_IN_DECLARED_FAMILIES` at Step 0, uniformly in
`R`, and Steps 0′, 1 and 2 have no object. The Step 0 review (Sec. 6) is still required.

**Step 0′ — representations** (only if Step 0 does not close). For each class: every
3-dimensional projective `R` up to the equivalence of Sec. 2, B1 per subgroup type, `ker_proj R`,
a written exhaustiveness proof and an exact script; reviewed before later steps use it. If 0′
stops on exhaustiveness, no class is closed.

**Step 0″ — remaining anticipations** (only if needed): B2, B3 closures, B4 as a restriction of the
ansatz-free class (not a closure), B6.

**Step 1 — exact class derivation** (as 4b-1 in the minimal charter): covariant parametrization,
unitarity identities in real variables, Groebner over an exact field, active support by
`y Π_h ||T_h||_F^2 = 1`; B2 enters only as the identities `T_{−h}^† T_h = 0`, `T_h T_{−h}^† = 0`.
`EMPTY_CLASS` by a unit ideal or a real infeasibility certificate; `UNITARY_SYMBOLS_EXIST` only
with an explicit certified real point. Stop: `OPEN_AFTER_CLASS_DERIVATION`.

**Step 2 — sectors, strict body, comparison** over the whole real solution set: every admissible
node for both ranks with the encodings of Sec. 1; `c_0` exactly; `c_strict^iso` by the vertex
lemma when every vertex coefficient is non-nilpotent (checked, not inferred from the trace at
rank 2), otherwise by exact computation; Q-a3; saturation.

**Literature step.** Local `biblioteca/` has no entry on `s=3` QCA on BCC (checked 2026-10-29
with `grep -i "s=3\|s = 3\|spin-1\|qutrit"` on `INDICE.md`). External search needs separate
permission. It conditions novelty and any "classification" wording, not the mathematical outcome
inside the declared families.

## 4. Admission, budget and stop rules

Inherited from the minimal charter, Sec. 4, with stage authorizations (a) Step 0 (and 0′, 0″ if
needed), (b) Step 1, (c) Step 2, each with its budget fixed by the user. Explicit stops: Step 0
lemma not certified → proceed to 0′ only with a new authorization; 0′ exhaustiveness not
completed; Step 1 → `OPEN_AFTER_CLASS_DERIVATION`; Step 2 → `OPEN_AFTER_STRICT_BODY`. No rigidity
from a scan, a numerical search or local isolation.

## 5. Outcomes

Per class: the minimal charter's vocabulary, with Q-a3 for Q-a and no Q-b row. Over the union
(G-S3-08), closing at whichever step decides it:

| Union outcome | Meaning |
| --- | --- |
| `S3_CONFLICT_UNDER_REVIEW` | some covered tuple has `c_0 > c_strict^iso` (Sec. 1); takes precedence over every other row until reviewed |
| `S3_COUNTEREXAMPLE_IN_DECLARED_FAMILIES` | some class has a verified counterexample (rank and direction stated); takes precedence over `OPEN`, since one counterexample decides the universal question |
| `S3_VACUOUS_IN_DECLARED_FAMILIES` | every class `EMPTY_CLASS` (may close at Step 0) |
| `S3_NO_ADMISSIBLE_SECTOR_IN_DECLARED_FAMILIES` | every class decided; at least one has unitary symbols; none has an admissible sector |
| `S3_RIGID_IN_DECLARED_FAMILIES` | every class decided, each `EMPTY_CLASS`, without admissible sector (the per-class `VACUOUS` of the minimal charter, not `S3_VACUOUS`) or `RIGIDITY_PROVED_FOR_FROZEN_CLASS`, and at least one rigid |
| `OPEN` | no row above applies (some class undecided and no counterexample or conflict) |

The rows are checked in this order and the first that applies is the union outcome; the
per-class outcomes are always recorded as well.

Reading rules: the minimal charter's, plus: every rigidity or counterexample statement names its
sector rank; if a class has a counterexample in one rank and equality in the other, both are
recorded; a flat branch is never a cone.

**Ceilings:** no statement about `s != 3`, other supports, on-site terms, reflections or
antiunitaries as symmetries, masses, interactions, species universality (A), the absolute scale
or nature. No statement on the smallest non-rigid internal dimension in general. A result over
these classes is not general QCA rigidity. Novelty: OPEN. `v_max` is never written unqualified.

## 6. Review

As in the minimal charter, Sec. 6. Step 0's certificate and its terminal outcome are reviewed by
a different family before entering `CURRENT_STATE` as more than PRELIMINARY.
