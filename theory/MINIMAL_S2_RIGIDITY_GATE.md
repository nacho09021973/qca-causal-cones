# MINIMAL S=2 RIGIDITY GATE (DRAFT v3)

**Status: DRAFT v3 — not chartered, nothing authorized.**
- **v3** applies the round-2 Astra repairs A-R2-01..06, which found v2 NOT_READY:
  [review and author reading](../debates/2026-10-29--minimal-s2-charter-draft-v2-review-astra/verificacion_autor.md).
  It also applies two user decisions of 2026-10-29: keep the `C4` face class, and let Q-a range
  over symbols with an admissible cone.
- **v1** (sha256 `8541cf72…`) was drafted on 2026-10-29 from the committee recommendation
  [`comite_decision_002`](../reports/comite/comite_decision_002_siguiente-charter-tras-cola.md).
  It was reviewed blind by Astra (OpenAI family), which returned **NOT_READY** with 14 repairs
  (A-R1-01..14):
  [review and author reading](../debates/2026-10-29--minimal-s2-charter-draft-review-astra/verificacion_autor.md).
- **v2** applies those repairs. It also adds a second isotropy family (Sec. 2, family F) by user
  decision («Ampliar la definición», 2026-10-29).
- The charter is frozen only when the user approves it, commits it with status `OPEN`, and the
  authorization is recorded in [CURRENT_STATE](../state/CURRENT_STATE.md).
- This draft records no computation, candidate or theorem.

**Authority:** [CURRENT_STATE](../state/CURRENT_STATE.md) Sec. 4 (`B_infty^*`):
- the P17 minimal `s=2` class with its Eq. (2) is NOT REFUTED, and rigidity there is OPEN as an
  in-repo claim;
- `s=2` without Eq. (2) is OPEN;
- the linear `2O` irrep `E` at `s=2` is OPEN and unchartered;
- Sec. 7.1 leaves open whether Eq. (2) is derivable.

**Predecessors:**
- [`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](MASSLESS_INRADIUS_RIGIDITY_GATE.md). Its Sec. 0
  definitions (`S_n`, `h_infty`, `c_strict^iso`, `rho_micro`, rigidity (i), saturation (ii)),
  Sec. 3 admission checks and Sec. 5 vocabulary are inherited unless amended below.
- [`IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`](IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md), closed for
  T3/O3/O4 and not amended here.
- The general ceiling `c_0 <= c_strict^iso`:
  [`STRICT_CONE_CEILING_N3_GATE.md`](STRICT_CONE_CEILING_N3_GATE.md) and
  [report](../reports/2026-09-16--point-3-strict-cone-ceiling.md), PROVED_UNDER_FROZEN_CONTRACT.
  Its frozen scope uses normalized `N_3`, node `k_star = 0`, any fixed eigenphase, a local
  unwrapped phase, and rank `2 <= r <= s` (contract lines 30–36). Whether it covers every node
  of this charter is checked in Step 0 (A-R1-11).

**Primary source:** P17 = D'Ariano–Erba–Perinotti, PRA 96, 062101 (2017), inspected as
`biblioteca/1708.00826v2.pdf`. All pages below refer to that arXiv v2 PDF. They must not be mixed
with the published-page coordinates of `reports/2026-09-14--massless-rigidity-source-audit.md`.
Locations confirmed by the Astra review:
- Definition 1 and Eq. (2), p.2. Distinguishability, supplemented by note [23] (p.15, published
  in the paper), which refers to ref. [31] (p.16, "Unpublished").
- s=1 "trivial", p.4, citing [24].
- Eqs. (12)–(13), p.4: rank one for nonzero transitions at `s=2`.
- Pauli isotropy image: Fig. 1(c) caption p.6, and Sec. V pp.5–6.
- Prop. 5, p.7, including (c) `A_e = 0` for d=3.
- The exchange `h_1 ↔ h_4`, used by P17 on p.7.

## 0. Why this gate, and what is already anticipated

Only one equality is certified: `c_0 = c_strict^iso` for the Pavia symbols `A±,B±`. In P17's
class, matching is a conditional application of P17's classification plus that certificate.
Without Eq. (2), no classification is held in the repo or was found in the local literature.

**Anticipations (not results).** These were stated before any computation under this charter.
None is certified. Step 0 must verify or refute each one.

*Retrospective, from the committee of 2026-10-29 (all members Claude):*
- A1. Suppose `R` is scalar on a subgroup transitive on each half `S_±`. Then covariance makes
  `T_h = A` on `S_+` and `B` on `−S_+`. The zero-shift identity gives `4(A^†A + B^†B) = I`. A
  displacement whose only pairs are one inside `S_+` and one inside `−S_+` gives
  `A^†A + B^†B = 0`, a contradiction.
- A2. The linear irrep `E` of `2O` is trivial on the axial half-turns: their image in
  `O ≅ S4` is the `V4` kernel of `S4 → S3`, and in `2O` the corresponding kernel is the
  preimage `Q8`.
- A3. A unimodular scalar Laurent polynomial on the torus is a monomial, so s=1 with eight active
  coefficients is empty.
- A4. Without Eq. (2), `S_+` can be a face, and `C4` acts transitively on it without containing
  `V4`.

*Corrections from the Astra review (2026-10-29):*
- A1 holds for the tetrahedron with `ε-shift (0,2,2)`.
- For a face, the displacement must be **tangential** to the face. Example: for
  `S_+ = {ε_x = +1}`, use `(0,2,2)`. The normal shift `(2,0,0)` only gives `4 B^†A = 0`; the v1
  note was wrong here.
- A2 is correct with the `Q8` precision.
- A3 is correct, with the extremal-exponent proof.
- A4 is correct as a geometric pair only. It says nothing yet about unitary symbols.

*From the Astra round-2 review (2026-10-29), reviewer derivations, `[UNVERIFIED]`:*
- A5. Family F, up to conjugation in `O`, is exactly `{D4, O}`: a transitive subgroup has order 8
  or 24.
- A6. If `R` is scalar on a subgroup transitive on all eight vertices, all `T_h` equal one `A`.
  The shift `ε = (2,2,2)` has a single pair and gives `A^†A = 0`, against `8A^†A = I`. The class
  is empty.
- A7. `E` under `O` or `D4` is scalar on `V4`. `V4` has two tetrahedral orbits, so A1 on the
  tetrahedron decides it.
- A8. Without Eq. (2), `s=2` coefficients have rank one: the shift `2h` has a single antipodal
  pair. Non-nilpotency of `T_h` is then equivalent to `tr T_h != 0`.

*Prospective:* everything in Secs. 3–5.

## 1. Question

Units and lattice:
- `N_3 = {ε/sqrt(3) : ε ∈ {±1}^3}` (normalized, as in the predecessors). Displacements are
  labelled by their `ε` differences.
- The generated lattice is BCC, `Λ = (1/sqrt(3)) {m ∈ Z^3 : m_1 ≡ m_2 ≡ m_3 mod 2}`.
- With the convention `e^{-ik.h}`, its reciprocal lattice is
  `Λ^* = π sqrt(3) {m ∈ Z^3 : m_1 + m_2 + m_3 even}`, and the Brillouin torus is `R^3 / Λ^*`.
- In these units the Pavia baseline value is `1/sqrt(3)`. With unnormalized `ε` both velocities
  scale by `sqrt(3)` and the baseline becomes `1`; the equality is unaffected (A-R1-02).

Main question:

\[
\forall \mathcal C,\ \forall U \in \mathcal C,\ \forall (k_\star,\omega_\star)\ \text{admissible}:\quad
c_0(U,k_\star) = c_{\rm strict}^{\rm iso}(U)\ ?
\]

- A class `𝒞` is a tuple `(P, G, S_±, [R])` in family P, or `(F, G, [R])` in family F. Family F
  has no partition (A-R2-01).
- `(k_star, ω_star)` ranges over **every** admissible node and eigenphase of `U`. The sector is
  the full two-band space, and the local quasienergy branch is the one fixed by the predecessor's
  Sec. 3.
- One admissible tuple with `c_0 != c_strict^iso` is a counterexample. Its direction is recorded
  (A-R2-04).
  - Where the general ceiling is certified for that class and node (Step 0.4), only
    `c_0 < c_strict^iso` is possible.
  - Where it is not certified, for example in the `C4` face class, both directions are admitted.
  - A `c_0 > c_strict^iso` witness inside a certified class would contradict the ceiling. It is
    recorded as a conflict and reviewed before anything else.

Subsidiary questions:
- **Q-a.** Does every symbol of a class **with at least one admissible node** satisfy P17
  Eq. (2)? User decision, A-R2-05. In family F, Eq. (2) is interpreted with `h ∈ N_3`
  (`S_+ = S_− = N_3` for this purpose only, as in P17 p.3).
- **Q-b.** Does the `A±,B±` certificate transport along every listed P17 equivalence?

## 2. Frozen class declaration

| Item | Declaration |
| --- | --- |
| Geometry | d=3; `N_3` as in Sec. 1, all eight `T_h != 0`; no on-site term; one complete update per time unit; `U(k) = sum_h e^{-i k.h} T_h` |
| Internal dimension | `s = 2` (main); `s = 1` only in Step 0 |
| Family P (partitioned) | `G ⊂ O`, proper rotations of the cube by their 3x3 matrices. `S_+ ⊂ N_3` with `|S_+| = 4` and `S_+ ∩ (−S_+) = ∅`. `G` permutes `S_+` transitively. This is a restriction of P17's setting: proper cube rotations and an oriented four-generator presentation, without Eq. (2). It is **not** "P17 minus Eq. (2)" (A-R1-03) |
| Family F (full) | `G ⊂ O` acting transitively on all eight vertices of `N_3`, with no partition. Classes are `(F, G, [R])`. Contains `O` |
| Overlap of P and F (A-R2-02) | Every `G` in F contains the axial `V4`, so every F-symbol, restricted to `V4`, belongs to a tetrahedral P class. A `D4`-covariant symbol also restricts to the `C4` face class. F adds stronger declared symmetry, not new symbols. Results transfer from a P class to its F subclasses (universal proofs) and from F to P (counterexamples), never the reverse. The same symbol appearing in several rows is not independent evidence. Reports count declared classes and distinct symbols separately |
| Covariance | `T_{gh} = R_g T_h R_g^†` for all `g ∈ G`, with `R` a projective unitary representation; equivalently `U(gk) = R_g U(k) R_g^†`. No reflections, parity or antiunitaries are required as symmetries |
| Representations | **Every** 2-dimensional projective unitary `R`, irreducible or reducible, up to projective equivalence `R'_g = c_g W R_g W^†` (`|c_g| = 1`, `W` unitary). The multiplier class alone does not identify `R` (A-R1-07) |
| Fidelity | Not assumed. The projective kernel `ker_proj R = {g : R_g scalar}` is recorded. A `g ≠ e` in it that moves a generator forces equal coefficients and violates Eq. (2) |
| Class identification | For `Q ∈ O`: in P, `(G, S_±, R) ~ (QGQ^{-1}, QS_±, R∘Ad_{Q^{-1}})`; in F, `(G, R) ~ (QGQ^{-1}, R∘Ad_{Q^{-1}})`. Classes are counted up to this conjugation |
| Eq. (2) | Not assumed; recorded per candidate. In F it is read with `h ∈ N_3` (Q-a) |
| Node and sector | All admissible nodes, full two-band sector, local branch (Sec. 1) |
| Coefficient domain | Real variables for the real and imaginary parts of the coefficients, ranging over all reals. "Exact algebra" is a method, not a restriction to algebraic points (A-R1-01, A-R1-09) |
| Group arithmetic | Exact canonical form. No numerical identification such as `nsimplify` |

## 3. Sequence

**Step 0′ — enumeration of isotropy classes.**
1. Family P. Enumerate the `2^4 = 16` choices of `S_+` (one vertex per antipodal pair):
   - two tetrahedra;
   - six faces;
   - eight "vertex plus its three neighbours" sets.

   For each choice, determine the transitive subgroups of its rotation stabilizer. The review
   anticipates three geometric pairs up to conjugation, `(V4, tetrahedron)`,
   `(T, tetrahedron)` and `(C4, face)` `[UNVERIFIED]`.
2. Family F. Enumerate the subgroups of `O` transitive on the eight vertices. A5 anticipates
   `{D4, O}`; the step verifies or refutes it.
3. For each group, enumerate every 2-dimensional projective unitary `R` up to the equivalence of
   Sec. 2, and record `ker_proj R`.
4. Give a written proof that the enumeration is exhaustive, plus an exact script. **The
   enumeration and its conventions are reviewed (Sec. 6) before Steps 0, 4a and 4b use it as
   their universe.**

**Step 0 — verify or refute the anticipations (A-R1-06).**
1. A1 for every class from Step 0′ in which `R` is scalar on a subgroup transitive on each half
   (family P) or on all eight vertices (family F; A6). Record the displacement and the pairs used.
   - Negative control: the `V4`/Q8 Pauli class must not become empty.
   - Positive control: `A±,B±` satisfy the identities.
2. A2 and A7 as statements about `E` restricted to the groups of Step 0′. Rows are stated under
   their own group: `E` under `O` (family F), and `E` restricted to `D4` (`≃ 1 ⊕ χ`, reducible).
3. A3: in-repo analytic proof for s=1 (extremal-exponent argument), with P17 p.4 [24] cited as
   context. Meyer (1996) is not in the repo and stays `[UNVERIFIED]`.
4. Ceiling scope (A-R1-11, A-R2-03). The general ceiling's frozen class
   (`STRICT_CONE_CEILING_N3_GATE.md`, lines 30–36) requires:
   - normalized `N_3`;
   - covariance under the Cartesian half-turn `D2` (= the axial `V4`);
   - node `k_star = 0`.

   Record per class and node whether the ceiling applies:
   - **Groups.** `V4` and `T` (tetrahedron) and `D4` and `O` (F) contain `D2`. The `C4` face
     class does not, so the ceiling does not cover it unless a `D2` covariance is proved for
     its symbols.
   - **Nodes.** A node `k_star != 0` is moved to `0` by `T'_h = e^{-i k_star.h} T_h`. This
     preserves `S_n`, the strict body and the slope. It keeps covariance with the same `R` on
     `D2` iff `g^{-1} k_star − k_star ∈ Λ^*` for every `g ∈ D2`.
   - The ceiling's proof is not re-read here. Any wider scope it might support is
     `[UNVERIFIED]` and is not used.

Each item has the outcomes VERIFIED, REFUTED (with witness) or INCONCLUSIVE. An anticipation that
ends INCONCLUSIVE does not remove its class from the later steps.

**Step 4a — transport within P17's class (A-R1-08).** Use transport laws, not literal
invariance. For each listed operation, state its effect on `S_n` and `c_0`, and re-verify
covariance and admission afterwards:
- constant unitary conjugation compatible with `R`: preserves `S_n`;
- global phase: preserves `S_n`;
- momentum shift: preserves `S_n`. It moves the node, and covariance with the same `R` must be
  re-checked;
- spatial inversion `h -> −h`: `S_n -> −S_n`;
- rotation `Q`: `S_n -> Q S_n`. The spherical minimum of the support function is preserved;
- complex conjugation of coefficients, `T_h -> T̄_h` (i.e. `U(k) -> conj(U(−k))`);
- P17's exchange `h_1 ↔ h_4` (p.7), with its geometric realization identified. Allowing a
  reflection as an equivalence between models is distinct from requiring it as a symmetry.

Left multiplication by a uniform local unitary is **excluded**. Astra's witness
`U = diag(e^{-ik}, e^{ik})`, `V = σ_x`, `(VU)^2 = I` shows it changes the strict velocity.
Unlisted or excluded operations leave Q-b `CONDITIONAL`.

**Step 4b-1 — exact class derivation (A-R1-09).**
- For each class from Step 0′ not emptied in Step 0: real variables, the unitarity identities
  split into real and imaginary parts, and active-support conditions `T_h != 0`.
- Groebner or primary decomposition over an exact field.
- Separately, a **real existence certificate**: an explicit real point, or a real
  infeasibility certificate such as a Positivstellensatz or SOS certificate.
- An ideal other than `(1)` is not existence.
- Complex algebraic components are kept distinct from components of the real admissible set.
- Admissible encodings, each to be verified exactly:
  - active support by an extra variable `y` with `y ∏_h ||T_h||_F^2 − 1 = 0`;
  - real emptiness by an identity `−1 = Σ a_i f_i + Σ b_j^2`.
  A bounded SOS search that fails is not existence, and a numerical approximation is not a
  certificate.
- 4b-1 decides only `EMPTY_CLASS` versus the existence of unitary symbols. Sectors are decided
  in 4b-2 (A-R2-05).

**Step 4b-2 — sectors, strict body, comparison.**
- Find every admissible node. One admissible encoding: `U(k_star) = aI`, `|a| = 1`,
  `H_j = i ā ∂_j U(k_star)`, `tr H_j = 0`, `½ tr(H_j H_l) = c_0^2 δ_jl`, `c_0 > 0`.
- Decide `NO_ADMISSIBLE_SECTOR` versus admissible sectors, and Q-a on the symbols that have one.
- Compute `c_0` exactly.
- Determine `c_strict^iso`: by the vertex lemma when every vertex coefficient is
  non-nilpotent (rank one `T_h = |u><v|` with `<v|u> != 0`), otherwise by an exact computation.
- If the strict body cannot be determined exactly within budget, stop with
  `OPEN_AFTER_STRICT_BODY` for that class.

## 4. Admission, budget and stop rules (A-R1-13)

- **Admission:** the predecessor's Sec. 3 checks, re-run after every transport in 4a. The first
  failure gives `INADMISSIBLE_CANDIDATE`.
- **Methods:** exact algebra only. A finite scan, a parameter sweep or a least-squares search
  certifies nothing (NO_RIGIDITY_FROM_FINITE_SCAN). Every retained computation is a versioned
  script in `scripts/`, run through `run_all_verifiers.py`.
- **Stage authorizations,** each requested separately and reported before the next:
  (a) Steps 0′ and 0; (b) 4a; (c) 4b-1; (d) 4b-2.
- **Before each stage runs,** its authorization fixes: a wall-time and resource budget, the
  scope (which classes), the deliverable, and the closure condition.
- **Explicit stops:**
  - 0′: exhaustiveness proof not completed.
  - 4a: an operation whose transport law cannot be established.
  - 4b-1: system not tractable → `OPEN_AFTER_CLASS_DERIVATION`.
  - 4b-2: strict body not determinable → `OPEN_AFTER_STRICT_BODY`.
- **Exhausted budget:** gives a partial or OPEN result, never rigidity.
- **Literature:** before any Q-a outcome is described beyond its class, search externally for
  P17 [31] and later work citing P17. That search sends text to third parties and needs
  separate permission.

## 5. Outcomes by question (A-R1-10)

Outcomes answer different questions and may coexist. "Equal standing" means equal editorial
acceptance; none is expected or preferred. A1–A8 are not results.

| Question | Outcomes (per class) | Closes |
| --- | --- | --- |
| Unitary symbols | `EMPTY_CLASS` (no unitary symbol); `UNITARY_SYMBOLS_EXIST` (certified real point); `OPEN_AFTER_CLASS_DERIVATION` | 4b-1 |
| Sectors | `NO_ADMISSIBLE_SECTOR` (unitary symbols exist, none has an admissible cone); `ADMISSIBLE_SECTORS_EXIST`; `OPEN` | 4b-2 |
| Main (rigidity, ∀ tuples) | `COUNTEREXAMPLE_VERIFIED_BELOW` (an admissible tuple with `0 < c_0 < c_strict^iso`); `COUNTEREXAMPLE_VERIFIED_ABOVE` (`c_0 > c_strict^iso`, only where the ceiling is not certified; inside a certified class it is a conflict, Sec. 1); `RIGIDITY_PROVED_FOR_FROZEN_CLASS` (equality for every admissible tuple); `VACUOUS` (class empty or without admissible sector); `OPEN_AFTER_STRICT_BODY` / `INCONCLUSIVE` | 4b-2 |
| Saturation (separate, A-R2-06) | `SATURATION_PROVED_FOR_CLASS` (∀ admissible `U`: `c_strict^iso(U) = rho_micro`); `SATURATION_FAILURE_WITNESS` (∃ admissible `U` with `c_strict^iso(U) < rho_micro`); `OPEN`. This replaces the predecessor's `INADMISSIBLE_SATURATION` and v2's `RIGIDITY_HOLDS_SATURATION_FAILS` | 4b-2 |
| Q-a (symbols with an admissible node) | `DISTINGUISHABILITY_IMPLIED_IN_CLASS`; `DISTINGUISHABILITY_REFUTED_BY_WITNESS` (the witness must have an admissible node); `OPEN` | 4b-2 |
| Q-b | `TRANSFER_CERTIFIED_FOR_LISTED_EQUIVALENCES`; `CONDITIONAL` (with the unlisted operations named) | 4a |
| Anticipations | VERIFIED / REFUTED / INCONCLUSIVE per item | Step 0 |

`INADMISSIBLE_CANDIDATE` concerns a single candidate and never decides a class.

**Ceilings:** no statement about `s > 2`, other supports or on-site terms, reflections or
antiunitaries as symmetries, masses, interactions, species universality (A), the absolute scale,
or nature. `RIGIDITY_PROVED_FOR_FROZEN_CLASS` is not a general QCA law. No novelty wording: the
`s=2` classification with Eq. (2) is P17's. Any statement without Eq. (2) is "not located in the
sources checked", and those sources are named. `v_max` is never written unqualified. A result
over this union of `s=2` classes is not general QCA rigidity, in titles and summaries as well as
in the body. A symbol counted under both P and F is one symbol.

## 6. Review (A-R1-14)

- The Step 0′ enumeration, with its exhaustiveness proof and conventions, is reviewed by a model
  of a different family before it is used as the classification universe.
- Every Step 0 certificate and every terminal outcome is reviewed the same way before entering
  CURRENT_STATE as more than PRELIMINARY.
- Each review gets one sealed round and one operational retry if transport fails.
- Open mandatory objections block promotion.
- Any change to certified content after review needs a new review of the changed files.
- Every review record cites:
  - the SHA-256 of the reviewed report and certificate;
  - the base commit;
  - the `~/herramientas` commit;
  - the user's authorization for sending text externally;
  - the model family that wrote the reviewed content, so that independence can be checked.
- A review is an additional check, not a substitute for the exact certificate.
