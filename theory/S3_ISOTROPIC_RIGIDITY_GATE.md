# S=3 ISOTROPIC RIGIDITY GATE

**Status: DRAFT v1 (2026-10-29), not frozen, not reviewed.** Requested by the user: "prepara el
charter para s=3". Nothing here is authorized for execution. The charter is frozen only by an
explicit user instruction after a different-family review; that commit becomes the
preregistration commit. This draft records no computation, candidate or theorem.

**Authority:** [CURRENT_STATE](../state/CURRENT_STATE.md) Sec. 4 (`B_infty^*`) and the entries
of 2026-10-29:
- `s=2`, families P and F of the minimal charter: only `(V4, tetrahedron, Pauli)` is nonempty
  (Step 4b-1, ESTABLISHED IN THE DECLARED FAMILIES). There Step 4b-2 gives
  `RIGIDITY_PROVED_FOR_FROZEN_CLASS` at `1/sqrt(3)` (**PRELIMINARY**, review pending).
- `s=4`: strong `B_infty^*` REJECTED IN THE DECLARED s=4 CLASS
  ([`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md)).
- `s=3` with an irreducible `R` under `T` or `O` (classes T3, O3): EMPTY_CLASS, ESTABLISHED IN
  THE DECLARED CLASSES ([`IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`](IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md)).
- Every other `s=3` isotropy class on `N_3` is OPEN and unchartered.

**Predecessors, inherited unless amended below:**
- [`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](MASSLESS_INRADIUS_RIGIDITY_GATE.md): Sec. 0
  definitions (`S_n`, `h_infty`, `c_strict^iso`, `rho_micro`, rigidity (i), saturation (ii)),
  the erratum on the vertex lemma, Sec. 3 admission checks, Sec. 5 vocabulary.
- [`MINIMAL_S2_RIGIDITY_GATE.md`](MINIMAL_S2_RIGIDITY_GATE.md) (`785565c`): units and lattice
  (Sec. 1), families P and F, covariance, class identification and Eq. (2) reading (Sec. 2), the
  4b-1/4b-2 encodings (Sec. 3), stop rules (Sec. 4), outcome vocabulary (Sec. 5), review
  (Sec. 6). Everything there that says `s = 2` reads `s = 3` here unless stated.
- The general ceiling `c_0 <= c_strict^iso`
  ([`STRICT_CONE_CEILING_N3_GATE.md`](STRICT_CONE_CEILING_N3_GATE.md),
  PROVED_UNDER_FROZEN_CONTRACT). Its frozen class allows any fixed `s >= 2`, `D2` covariance,
  node `k_star = 0`, sector rank `2 <= r <= s`, and other slopes in the same eigenspace.

## 0. Why this gate, and what is already anticipated

`s=2` is rigid in the only nonempty class; `s=4` is not rigid. `s=3` is the only internal
dimension between them. The gate asks whether the break happens already at `s=3`, or whether
`s=3` is rigid, or whether it is vacuous. **All three outcomes have equal standing.** A vacuous
`s=3` (every class `EMPTY_CLASS`) is a first-class result: it would mean the minimal isotropic
non-rigid dimension on `N_3` is 4.

**Anticipations (not results).** Written by Claude before any computation under this charter,
`[UNVERIFIED]`. Step 0 verifies or refutes each one.
- B1. **Every 3-dimensional projective representation of a subgroup `G ⊂ O` is equivalent to a
  linear one.** Sketch: for a cocycle `ω` of `R`, `det` gives `ω^3` a coboundary. The Schur
  multiplier of every subgroup of `O` has exponent at most 2, so `ω` is a coboundary. The spin
  (Pauli-type) projective classes used at `s=2` therefore do not exist at `s=3`.
- B2. **Rank bound.** The shift `2h` has the single pair `(−h, h)`, so `T_{−h}^† T_h = 0` and
  `T_h T_{−h}^† = 0`. Then `rank T_h + rank T_{−h} <= 3`. Every antipodal pair has ranks
  `(1, 1)`, `(1, 2)` or `(2, 1)`. (At `s=2` this forced rank one, A8.)
- B3. **Scalar kernel.** If `R` is scalar on a subgroup transitive on each half `S_±`, the A1
  argument of the minimal charter applies unchanged (it uses no dimension): `EMPTY_CLASS`. For
  `V4`, any `R = χ ⊕ χ ⊕ χ` is of this kind.
- B4. **No block-diagonal symbols.** For `R = R_2 ⊕ χ` and a symbol that preserves the blocks,
  the 1-dimensional block `t_h` is `G`-invariant. If it is nonzero somewhere, it is nonzero on a
  whole orbit of at least four vertices, and a unimodular scalar Laurent polynomial is a
  monomial (A3 of the minimal charter): contradiction. So `t ≡ 0` and the symbol is not unitary.
  Every unitary symbol of a reducible class, if any, mixes the blocks. In particular the `s=2`
  Weyl symbol plus a spectator does not embed as a direct sum.
- B5. **Determinant.** `det U` is a unimodular Laurent polynomial, hence `ζ e^{-ik·m}`.
  Covariance gives `det U(gk) = det U(k)`, so `g m = m` for every `g ∈ G`. For every `G`
  containing `V4`, `m = 0` and `det U` is constant.
- B6. **Ceiling scope.** Every class whose group contains the axial `D2` (`V4`, `T`, `D4`, `O`)
  is inside the ceiling's frozen class at node `k_star = 0`, so only `c_0 <= c_strict^iso` can
  occur there. The `C4` face class is not covered.
- B7. **Possibly vacuous.** B2–B5 together suggest, without proof, that many or all `s=3` classes
  may be empty. No outcome is expected or preferred.

## 1. Question

Units, lattice, Brillouin torus and the main quantified statement are those of the minimal
charter, Sec. 1, with `s = 3`:

\[
\forall \mathcal C,\ \forall U \in \mathcal C,\ \forall (k_\star,\omega_\star,P)\ \text{admissible}:\quad
c_0(U,k_\star,P) = c_{\rm strict}^{\rm iso}(U)\ ?
\]

- `𝒞` ranges over the classes of Sec. 2, excluding T3 and O3 (already EMPTY_CLASS, reused, not
  recomputed).
- **Sector (new at `s=3`).** `P` is the full spectral projector of `U(k_star)` at
  `e^{-iω_star}`, of rank `r ∈ {2, 3}`, isolated from the other eigenvalues at the node.
  - `r = 2`: the sector is a two-band cone; the third band is a spectator.
  - `r = 3`: `U(k_star) = aI`. The cone is admitted if, in every direction `q`, the linearized
    branches include `+c_0|q|` and `−c_0|q|` with the same `c_0 > 0`, untilted. A third branch
    may have another slope, including `0` (a flat branch, as for a spin-1 node). It is recorded,
    never mistaken for a cone.
  - This follows the ceiling gate's "Other slopes" row. **D1 (user, 2026-10-29): both ranks.**
- A counterexample is one admissible tuple with `c_0 != c_strict^iso`; its direction is
  recorded. Where the ceiling applies (B6), only `c_0 < c_strict^iso` is possible.
- **Saturation** (`c_strict^iso = rho_micro`) is a separate question, as at `s=2`.

Subsidiary question:
- **Q-a3.** On symbols with an admissible node, does P17's Eq. (2) hold, read as
  `T_{gh} != T_h` whenever `g h != h`? (Same predicate as Q-a, with the same family-dependent
  domain `D_𝒞`.)

There is no Q-b: no `s=3` certificate exists to transport.

## 2. Frozen class declaration

| Item | Declaration |
| --- | --- |
| Geometry | d=3; `N_3`, all eight `T_h != 0`; no on-site term; one complete update per time unit; `U(k) = Σ_h e^{-ik·h} T_h` |
| Internal dimension | `s = 3` only. No statement about any other `s` |
| Families | P and F exactly as in the minimal charter, Sec. 2. The geometric pairs are those of its reviewed stage (a): family P = `(V4, tetrahedron)`, `(T, tetrahedron)`, `(C4, face)`; family F = `D4`, `O`. This enumeration does not depend on `s` and is reused, not redone |
| Representations | **Every** 3-dimensional projective unitary `R` of `G`, irreducible or reducible, up to projective equivalence. By B1, if verified, these are linear up to equivalence. Irreducible `R` under `T` or `O` is T3 or O3 and is excluded as already decided |
| Fidelity | Not assumed. `ker_proj R` is recorded. B3 decides classes whose kernel contains a subgroup transitive on `S_±` (P) or on `N_3` (F) |
| Covariance | `T_{gh} = R_g T_h R_g^†` for every `g ∈ G`. No reflections, parity or antiunitaries required |
| Eq. (2) | Not assumed; recorded (Q-a3) |
| Node and sector | Sec. 1: every admissible node, rank `r ∈ {2, 3}` (D1), local branch |
| Coefficient domain | Real variables for real and imaginary parts, over all reals |
| Group arithmetic | Exact canonical forms, as in the minimal charter |

## 3. Sequence

**Step 0′ — representations.** For each of the five geometric classes:
1. List every 3-dimensional linear representation up to equivalence: sums of irreducibles of
   total dimension 3 (for abelian `G`, triples of characters up to permutation).
2. Prove B1, or list the projective classes that survive it.
3. Record `ker_proj R`, and the class identification under conjugation in `O` (minimal charter,
   Sec. 2), including the normalizer action that permutes characters.
4. Give a written exhaustiveness proof and an exact script. The list is reviewed (Sec. 6) before
   later steps use it as their universe.

**Step 0 — anticipations.** Verify or refute B1–B6 with exact certificates or written proofs,
and close every class that B3 or B4 empties. Controls:
- Positive: the `s=2` witness `e^{-iq_x σ_x} e^{-iq_y σ_y} e^{-iq_z σ_z}` satisfies the B2 and
  B5 identities at `s=2`.
- Negative: a block-diagonal `s=3` candidate built from the `s=2` witness plus any scalar block
  must fail unitarity or covariance, as B4 states.

**Step 1 — exact class derivation** (as 4b-1 in the minimal charter). For each class not closed in
Step 0: covariant parametrization, unitarity identities in real variables, Groebner basis over an
exact field, active support by `y Π_h ||T_h||_F^2 = 1` where needed. `EMPTY_CLASS` by a unit
ideal, or by a real infeasibility certificate; `UNITARY_SYMBOLS_EXIST` only with an explicit
certified real point. An ideal other than `(1)` is not existence. A class too large for the
budget stops as `OPEN_AFTER_CLASS_DERIVATION`. Reductions that lower the variable count (for
example B2's rank structure, or B5) are allowed only after they are certified in Step 0.

**Step 2 — sectors, strict body, comparison** (as 4b-2). For each nonempty class: the
description of the class as far as it is determined exactly; every admissible node for both
ranks (D1); `c_0` exactly; `c_strict^iso` by the vertex lemma when every vertex
coefficient is non-nilpotent, otherwise by exact computation (rank two `T_h` can be nilpotent in
new ways at `s=3`; this is checked, not assumed); Q-a3; saturation.

**Literature step** (before any outcome is described beyond its class). Local: `biblioteca/`
has no entry on `s=3` QCA on BCC (checked 2026-10-29 with `grep -i "s=3\|s = 3\|spin-1\|qutrit"`
on `INDICE.md`). External search for `s=3` or spin-1 quantum walk classifications sends text to
third parties and needs separate permission.

## 4. Admission, budget and stop rules

Inherited from the minimal charter, Sec. 4, with:
- **Stage authorizations,** each requested separately and reported before the next:
  (a) Steps 0′ and 0; (b) Step 1; (c) Step 2.
- **Budget** fixed by the user at each authorization (wall time, scope, deliverable, closure).
- **Explicit stops:** 0′ exhaustiveness not completed; Step 1 not tractable →
  `OPEN_AFTER_CLASS_DERIVATION`; Step 2 strict body not determinable → `OPEN_AFTER_STRICT_BODY`.
- No rigidity from a finite scan, a numerical search or local isolation.

## 5. Outcomes by question

The vocabulary of the minimal charter, Sec. 5, per class, with Q-a3 for Q-a and no Q-b row. In
addition, over the union of classes:

| Question | Outcomes | Closes |
| --- | --- | --- |
| Union | `S3_VACUOUS_IN_DECLARED_FAMILIES` (every class `EMPTY_CLASS`); `S3_RIGID_IN_DECLARED_FAMILIES` (every nonempty class `RIGIDITY_PROVED_FOR_FROZEN_CLASS`); `S3_COUNTEREXAMPLE_IN_DECLARED_FAMILIES` (some class has a verified counterexample); `OPEN` | Step 2 |

Reading rules: the minimal charter's, plus:
- The sector rank of every counterexample or rigidity statement is stated (`r = 2` or `r = 3`).
- A flat branch at an `r = 3` node is reported, never counted as a cone.

**Ceilings:** no statement about `s != 3`, other supports, on-site terms, reflections or
antiunitaries as symmetries, masses, interactions, species universality (A), the absolute scale
or nature. A result over these classes is not general QCA rigidity. Novelty: OPEN; no
classification wording until the literature step is done. `v_max` is never written unqualified.

## 6. Review

As in the minimal charter, Sec. 6. The draft itself gets a different-family review before it is
frozen. Astra was unavailable on 2026-10-29 (provider usage limit); the user chose Grok (D3).

## 7. User decisions (2026-10-29: "D1 ambos rangos, D2 mantener F, D3 Grok, commit")

- **D1.** Sector ranks: both `r = 2` and `r = 3`.
- **D2.** Family F is kept at `s=3`.
- **D3.** Reviewer of this draft: Grok (xAI family).
