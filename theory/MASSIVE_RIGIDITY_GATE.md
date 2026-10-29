# MASSIVE RIGIDITY GATE

**Status: DRAFT v1 (2026-10-29), not frozen, not reviewed.** Requested by the user: "si, prepara
el borrador del charter con masa". Nothing here is authorized for execution. The charter is
frozen only by an explicit user instruction after a different-family review; that commit becomes
the preregistration commit. This draft records no computation, candidate or theorem.

**Authority:** [CURRENT_STATE](../state/CURRENT_STATE.md):
- Exact finite-mass `B*` is **REJECTED IN STANDARD DIRAC FAMILY** (Sec. 5): for every lattice mass
  `0 < m < 1`, with `M = arcsin m` and `F = M cot M`,
  `c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`. The comparison there is against
  `r_in(C_micro)`, not against `c_strict^iso`.
- Small-mass matching, `lim_{m→0} c_H = lim_{m→0} c_{ω^2} = r_in`, is **VERIFIED FOR STANDARD DIRAC
  COUPLINGS**.
- Massless `s=2`, minimal charter, class `(V4, tetrahedron, Pauli)`: `c_0 = c_strict^iso =
  rho_micro = 1/sqrt(3)`, ESTABLISHED IN THE DECLARED CLASS. Every symbol of that class is gapless
  at every node.
- Massless `s=4`, Pauli `D2` class: strong `B_infty^*` REJECTED; the family of
  [`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md) has `c_0(a) = a/sqrt(3)`,
  `0 < a < 1`, at fixed `c_strict^iso = 1/sqrt(3)`.
- [`THREE_VELOCITIES.md`](THREE_VELOCITIES.md) Sec. 3 and the hard rule of `CLAUDE.md`: for a
  massive sector `c_IR` is not `|∇ω(0)|`, and `c_H`, `c_{ω^2}` are never interchanged.

**Predecessors, inherited unless amended:**
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](MASSLESS_INRADIUS_RIGIDITY_GATE.md) (definitions of `S_n`,
`h_infty`, `c_strict^iso`, `rho_micro`, the vertex-lemma erratum, Sec. 3 admission checks);
[`MINIMAL_S2_RIGIDITY_GATE.md`](MINIMAL_S2_RIGIDITY_GATE.md) (units, lattice, covariance, stop
rules, review); the Weyl/Dirac gate contract
(`reports/2026-09-14--weyl-dirac-gate-contract.md`) for the standard Dirac family.

## 0. Why this gate, and what is already anticipated

Physical question: for a massive species, is its effective light speed forced by the structure
(a function of its mass alone, the same for every admissible dynamics), or adjustable (two
dynamics with the same mass and the same causal limit give different speeds)? And is the
massless value recovered as the mass goes to zero in every admissible family? The answers bear
on species universality (question A) without deciding it: A is not chartered here.

**Anticipations (not results),** written by Claude before any computation, `[UNVERIFIED]`:
- C1. **The mass term is on-site.** In the standard Dirac family the mass coupling is
  `k`-independent, so the support is `N_3 ∪ {0}` (checked in
  `scripts/verify_weyl_dirac_gate.py`, "massive support"). A massive class on `N_3` without
  on-site term is not excluded by this, but none is known.
- C2. **Mass needs internal multiplicity (Schur).** If `k_*` is `G`-invariant
  (`g k_* − k_* ∈ Λ^*` for every `g ∈ G`), covariance gives `R_g U(k_*) R_g^† = U(k_*)`. If `R` is
  projectively irreducible, `U(k_*)` is scalar and no gap opens at `k_*`. So a gapped sector at an
  invariant node needs a reducible `R` with a nontrivial commutant. For the `s=2` Pauli class
  this rules out mass at invariant nodes, with or without an on-site term. For `s=4` with
  `R_i = σ_i ⊗ I_2` the commutant is `I ⊗ M_2`, so mass is possible.
- C3. **Standard family against the strict body.** If every vertex coefficient of the massive
  standard symbol is non-nilpotent, the vertex lemma gives `c_strict^iso = r_in`, and the
  established inequalities become `c_H < c_{ω^2} < c_strict^iso`. Not checked.
- C4. **Likely adjustable in the `s=4` Pauli class.** The massless slope already varies there at
  fixed `c_strict^iso` (`c_0(a) = a/sqrt(3)`). If a mass term can be added to that family
  admissibly, continuity suggests `c_X` varies at fixed `M`. Not checked; an explicit exact
  witness is required.
- C5. **Tension.** C2 and C4 together suggest that, in these classes, the multiplicity that makes
  mass possible is the same that makes the speed adjustable. This is a hypothesis to test, not a
  result.

## 1. Definitions

Units, lattice and Brillouin torus as in the minimal charter, Sec. 1.

**Massive admissible node.** A momentum `k_*` and a reference phase `ω_*` such that:
- the sector `P` is the spectral projector of `U(k_*)` onto the eigenvalues `e^{-i(ω_* ± M)}`,
  `0 < M < π/2`, of rank `r` (each sign with multiplicity `r/2`), isolated from the rest of the
  spectrum at `k_*`;
- for every unit direction `n̂`, every branch emerging from `P` satisfies
  `(ω(k_* + p n̂) − ω_*)^2 = M^2 + c_{ω^2}^2 p^2 + O(p^3)`, with the same `c_{ω^2} > 0` for all
  branches and directions (isotropic, untilted: no term linear in `p`);
- local unwrapped phases, as in the predecessor's Sec. 3.

**Two extractions, always reported separately:**
- `c_{ω^2}`, defined above.
- `c_H`: with `H(k) = i log(e^{iω_*} U(k))` on the sector, branch continuous from `k_*`, write
  `H(k_* + p) = M β + Σ_j p_j α_j + O(p^2)`. `c_H` is defined only if `β^2 = I_P`,
  `{α_j, β} = 0` and `(1/r) tr(α_j α_l) = c_H^2 δ_jl`. Otherwise the outcome for that node is
  `NO_DIRAC_FORM`, recorded, not repaired.

**Comparison targets:** `c_strict^iso(U)` of the full symbol (support `N_3 ∪ {0}` has the same
convex hull as `N_3`); and, for a one-parameter family `U_μ` with an admissible massless limit
`U_0`, the massless slope `c_0(U_0)`.

**Mass parameter:** `M`, the half-gap of eigenphases at the node, in lattice units. The hopping or
coupling parameters of particular families are not used to compare symbols.

## 2. Frozen class declaration

| Item | Declaration |
| --- | --- |
| Geometry | d=3; support `N_3 ∪ {0}`; all eight `T_h != 0` for `h ∈ N_3`; `T_0` free (possibly zero); one complete update per time unit |
| Internal dimension | `s = 4` |
| Symmetry (main class M4) | the axial `V4 = D2`, `R_i = σ_i ⊗ I_2` (the declared `s=4` class of the massless counterexample); `T_{gh} = R_g T_h R_g^†`, including `h = 0`. **User decision D1** on enlargements (families P and F with every 4-dimensional projective `R`) |
| Control class C2 | `s = 2`, support `N_3 ∪ {0}`, `(V4, Pauli)`: used only to check C2 |
| Control family | the standard Dirac family of the Weyl/Dirac gate: reproduce `c_H = r_in F`, `c_{ω^2} = r_in sqrt(F)` |
| Nodes | **User decision D2**: `G`-invariant nodes only, or every admissible node |
| Coefficient domain | real variables over all reals; exact algebra |

## 3. Questions and outcomes (per class)

| Question | Outcomes |
| --- | --- |
| QM-0 Existence | `NO_MASSIVE_SECTOR` (no admissible massive node); `MASSIVE_SECTORS_EXIST` (certified explicit symbol); `OPEN` |
| QM-1 Ceiling | `MASSIVE_CEILING_PROVED_IN_CLASS` (`c_X <= c_strict^iso` for every admissible tuple, per extraction `X`); `MASSIVE_CEILING_VIOLATION_WITNESS`; `OPEN` |
| QM-2 Forced or adjustable (central) | `MASS_DEFICIT_FORCED_IN_CLASS` (`c_X(U)/c_strict^iso(U) = f_X(M(U))` for every admissible `U`, with `f_X` exhibited); `MASS_DEFICIT_ADJUSTABLE_WITNESS` (two exact admissible symbols with equal `M`, equal `c_strict^iso` and different `c_X`); `OPEN` |
| QM-3 Massless recovery | `RECOVERY_PROVED_IN_CLASS` (`lim_{M→0} c_X(U_μ) = c_0(U_0)` for every admissible family); `RECOVERY_FAILURE_WITNESS`; `OPEN` |

Reading rules:
- Each outcome names its extraction `X ∈ {H, ω^2}`. A result for one extraction says nothing
  about the other.
- An adjustable witness needs only explicit exact symbols. A forced or ceiling outcome needs a
  proof over the whole class; a failed search proves nothing.
- QM-3 compares with `c_0(U_0)`, not with `c_strict^iso`: in the `s=4` class they differ already
  at `M = 0`.
- `NO_DIRAC_FORM` nodes enter QM-2 and QM-3 only through `c_{ω^2}`.

## 4. Sequence, budget and stops

- **Stage (a): definitions and controls.** Exact verifier for: the standard-family values
  (positive control); C2 in the control class (no gap at invariant nodes); C1; C3. Report.
- **Stage (b): QM-0 and QM-2 by explicit construction in M4.** Exact admissible massive symbols,
  for example a mass coupling added to the counterexample family if admissible. A witness
  decides `MASS_DEFICIT_ADJUSTABLE_WITNESS`; failing to build one decides nothing.
- **Stage (c): class derivation** for QM-1, and for QM-2 if (b) finds no witness. Exact
  parametrization and Groebner as in the minimal charter; likely large. Stop:
  `OPEN_AFTER_CLASS_DERIVATION`.
- Each stage is authorized separately with its budget (wall time, scope, deliverable, closure).
- No floating point in a certified quantity; no fitted tolerances; no rigidity from scans.

## 5. Ceilings

No statement about interactions, `s != 4` (unless D1 enlarges), other supports, reflections or
antiunitaries as symmetries, the absolute scale, or nature. No definition of species and no
claim about question A; results may be cited in the A preflight note only with this ceiling.
`v_max` is never written unqualified. Novelty: OPEN. The literature step of the minimal charter
applies: local `biblioteca/` first; external search needs separate permission.

## 6. Review

As in the minimal charter, Sec. 6. The draft gets a different-family review before freezing.

## 7. Decisions for the user before freezing

- **D1.** Symmetry: only M4 (`V4`, `σ_i ⊗ I_2`), or also families P and F with every
  4-dimensional projective `R`.
- **D2.** Nodes: `G`-invariant only, or every admissible node.
- **D3.** Order with the `s=3` charter: run this one after `s=3` (so that a nonempty reducible
  `s=3` class can be added as a successor), or in parallel.
- **D4.** Reviewer of this draft (Grok, DeepSeek or Gemini; not Claude).
