# MINIMAL S=2 RIGIDITY GATE (DRAFT v2)

**Status: DRAFT v2 — not committed, not chartered, nothing authorized.**
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

*Prospective:* everything in Secs. 3–5.

## 1. Question

Units and lattice:
- `N_3 = {ε/sqrt(3) : ε ∈ {±1}^3}` (normalized, as in the predecessors). Displacements are
  labelled by their `ε` differences.
- The generated lattice is BCC (`ε`-coordinates `x_1 ≡ x_2 ≡ x_3 mod 2`), with Brillouin torus
  the dual cell.
- In these units the Pavia baseline value is `1/sqrt(3)`. With unnormalized `ε` both velocities
  scale by `sqrt(3)` and the baseline becomes `1`; the equality is unaffected (A-R1-02).

Main question:

\[
\forall (\mathcal F, G, S_\pm, [R]),\ \forall U,\ \forall (k_\star,\omega_\star)\ \text{admissible}:\quad
c_0(U,k_\star) = c_{\rm strict}^{\rm iso}(U)\ ?
\]

- `𝓕` is the isotropy family of Sec. 2.
- `(k_star, ω_star)` ranges over **every** admissible node and eigenphase of `U`. The sector is
  the full two-band space, and the local quasienergy branch is the one fixed by the predecessor's
  Sec. 3.
- One admissible tuple violating the equality is a counterexample.

Subsidiary questions:
- **Q-a.** Does every admissible member of a class satisfy P17 Eq. (2)?
- **Q-b.** Does the `A±,B±` certificate transport along every listed P17 equivalence?

## 2. Frozen class declaration

| Item | Declaration |
| --- | --- |
| Geometry | d=3; `N_3` as in Sec. 1, all eight `T_h != 0`; no on-site term; one complete update per time unit; `U(k) = sum_h e^{-i k.h} T_h` |
| Internal dimension | `s = 2` (main); `s = 1` only in Step 0 |
| Family P (partitioned) | `G ⊂ O`, proper rotations of the cube by their 3x3 matrices. `S_+ ⊂ N_3` with `|S_+| = 4` and `S_+ ∩ (−S_+) = ∅`. `G` permutes `S_+` transitively. This is a restriction of P17's setting: proper cube rotations and an oriented four-generator presentation, without Eq. (2). It is **not** "P17 minus Eq. (2)" (A-R1-03) |
| Family F (full) | `G ⊂ O` acting transitively on all eight vertices of `N_3`, with no partition. Contains `O` |
| Covariance | `T_{gh} = R_g T_h R_g^†` for all `g ∈ G`, with `R` a projective unitary representation; equivalently `U(gk) = R_g U(k) R_g^†`. No reflections, parity or antiunitaries are required as symmetries |
| Representations | **Every** 2-dimensional projective unitary `R`, irreducible or reducible, up to projective equivalence `R'_g = c_g W R_g W^†` (`|c_g| = 1`, `W` unitary). The multiplier class alone does not identify `R` (A-R1-07) |
| Fidelity | Not assumed. The projective kernel `ker_proj R = {g : R_g scalar}` is recorded. A `g ≠ e` in it that moves a generator forces equal coefficients and violates Eq. (2) |
| Class identification | `(G, S_±, R) ~ (QGQ^{-1}, QS_±, R∘Ad_{Q^{-1}})` for `Q ∈ O`; classes are counted up to this conjugation |
| Eq. (2) | Not assumed; recorded per candidate (Q-a) |
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
2. Family F. Enumerate the subgroups of `O` transitive on the eight vertices. `O` is one;
   `D4` about a coordinate axis is anticipated `[UNVERIFIED]`.
3. For each group, enumerate every 2-dimensional projective unitary `R` up to the equivalence of
   Sec. 2, and record `ker_proj R`.
4. Give a written proof that the enumeration is exhaustive, plus an exact script. **The
   enumeration and its conventions are reviewed (Sec. 6) before Steps 0, 4a and 4b use it as
   their universe.**

**Step 0 — verify or refute the anticipations (A-R1-06).**
1. A1 for every class from Step 0′ in which `R` is scalar on a subgroup transitive on each half
   (family P) or on all eight vertices (family F). Record the displacement and the pairs used.
   Family F with `R` scalar on a vertex-transitive subgroup forces all `T_h` equal. Whether that
   is empty is to be checked; it is not assumed.
   - Negative control: the `V4`/Q8 Pauli class must not become empty.
   - Positive control: `A±,B±` satisfy the identities.
2. A2 as a statement about `E` restricted to the groups of Step 0′. Rows are stated under their
   own group: `E` under `O` (family F), and its restriction to `D4` if `D4` occurs.
3. A3: in-repo analytic proof for s=1 (extremal-exponent argument), with P17 p.4 [24] cited as
   context. Meyer (1996) is not in the repo and stays `[UNVERIFIED]`.
4. Ceiling scope (A-R1-11): check whether the general ceiling covers every node and unit used
   here. The ceiling is stated at `k_star = 0`, so other nodes must be reached by a transport
   that keeps covariance. If it does not cover them, record that and drop any use of the
   ceiling for those nodes.

Each item has the outcomes VERIFIED, REFUTED (with witness) or INCONCLUSIVE.

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
- Q-a is recorded per class.

**Step 4b-2 — sectors, strict body, comparison.**
- Find every admissible node.
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
acceptance; none is expected or preferred. A1–A4 are not results.

| Question | Outcomes (per class) | Closes |
| --- | --- | --- |
| Classification | `EMPTY_CLASS` (no unitary symbol); `NO_ADMISSIBLE_SECTOR` (unitary symbols exist, no admissible cone); `NONEMPTY_WITH_ADMISSIBLE_SECTORS`; `OPEN_AFTER_CLASS_DERIVATION` | 4b-1 for that class |
| Main (rigidity) | `COUNTEREXAMPLE_VERIFIED` (one admissible tuple with `0 < c_0 < c_strict^iso`); `RIGIDITY_PROVED_FOR_FROZEN_CLASS` (equality for every admissible tuple); `RIGIDITY_HOLDS_SATURATION_FAILS` (equality holds but `c_strict^iso < rho_micro`; renamed from the predecessor's `INADMISSIBLE_SATURATION`); `VACUOUS` (class empty or without admissible sector); `OPEN_AFTER_STRICT_BODY` / `INCONCLUSIVE` | 4b-2 for that class |
| Q-a | `DISTINGUISHABILITY_IMPLIED_IN_CLASS`; `DISTINGUISHABILITY_REFUTED_BY_WITNESS`; `OPEN` | 4b-1 |
| Q-b | `TRANSFER_CERTIFIED_FOR_LISTED_EQUIVALENCES`; `CONDITIONAL` (with the unlisted operations named) | 4a |
| Anticipations | VERIFIED / REFUTED / INCONCLUSIVE per item | Step 0 |

`INADMISSIBLE_CANDIDATE` concerns a single candidate and never decides a class.

**Ceilings:** no statement about `s > 2`, other supports or on-site terms, reflections or
antiunitaries as symmetries, masses, interactions, species universality (A), the absolute scale,
or nature. `RIGIDITY_PROVED_FOR_FROZEN_CLASS` is not a general QCA law. No novelty wording: the
`s=2` classification with Eq. (2) is P17's. Any statement without Eq. (2) is "not located in the
sources checked", and those sources are named. `v_max` is never written unqualified.

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
  - the user's authorization for sending text externally.
- A review is an additional check, not a substitute for the exact certificate.
