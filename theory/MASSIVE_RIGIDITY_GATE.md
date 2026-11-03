# MASSIVE RIGIDITY GATE

**Status: DRAFT v2 (2026-10-29), not frozen.** Requested by the user ("si, prepara el borrador
del charter con masa"; v2: "si a ambas"). Nothing here is authorized for execution. The charter is
frozen only by an explicit user instruction; that commit becomes the preregistration commit.
This draft records no computation, candidate or theorem.

Drafting history:
- **v1** (`afc2b64`) was reviewed blind by Astra (OpenAI family): **NOT READY**, thirteen repairs
  A-M-01..13, plus an explicit family that would decide several questions
  ([review and author reading](../debates/2026-10-29--massive-charter-draft-review-astra/verificacion_autor.md)).
- **v2** applies A-M-01..13 and builds Stage (a) around that family as candidates to certify.
- User decisions (v1, kept): D1 only class M4; D2 every admissible massive node; D3 after the
  `s=3` charter; D4 reviewer Grok for the draft (v1 was reviewed by Astra at the user's request).

**Authority:** [CURRENT_STATE](../state/CURRENT_STATE.md):
- Exact finite-mass `B*` REJECTED IN STANDARD DIRAC FAMILY (Sec. 5): for `0 < m < 1`,
  `M = arcsin m`, `F = M cot M`: `c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`, compared with
  `r_in(C_micro)`. Small-mass matching VERIFIED FOR STANDARD DIRAC COUPLINGS.
- Massless `s=2` `(V4, Pauli)`: `c_0 = c_strict^iso = 1/sqrt(3)`, ESTABLISHED IN THE DECLARED
  CLASS; every symbol gapless at every node.
- Massless `s=4` Pauli `D2` class: strong `B_infty^*` REJECTED
  ([`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md), `c_0(a) = a/sqrt(3)`).
- [`THREE_VELOCITIES.md`](THREE_VELOCITIES.md) Sec. 3: for a massive sector `c_IR` is not
  `|∇ω(0)|`; `c_H` and `c_{ω^2}` are never interchanged.
- The ceiling of [`STRICT_CONE_CEILING_N3_GATE.md`](STRICT_CONE_CEILING_N3_GATE.md) is for massless
  cones only. Nothing here is a consequence of it.

**Predecessors, inherited unless amended:**
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](MASSLESS_INRADIUS_RIGIDITY_GATE.md) (`S_n`, `h_infty`,
`c_strict^iso`, `rho_micro`, vertex-lemma erratum, Sec. 3 checks);
[`MINIMAL_S2_RIGIDITY_GATE.md`](MINIMAL_S2_RIGIDITY_GATE.md) (units, lattice, covariance, stop
rules, review); the Weyl/Dirac gate contract (`reports/2026-09-14--weyl-dirac-gate-contract.md`).

## 0. Question, and what is anticipated

**Scope of the question (A-M-13).** How two specified local coefficients of massive sectors,
`c_H` and `c_{ω^2}`, depend on the symbol across class M4, with explicit units and an explicit
causal comparator. Comparisons are between different dynamics, not between species coexisting in
one dynamics. The results may inform question A (species universality) but do not decide it; A
is not chartered here.

**Anticipations (not results),** `[UNVERIFIED]` until certified; C1–C4 incorporate the reviewer's
hand derivations, which are not certificates.
- C1 (A-M-04). The standard Dirac coupling's mass term is on-site (support `N_3 ∪ {0}`). An
  on-site term is not necessary: `U_{0,M}` below has `T_0 = 0` and a massive node.
- C2 (A-M-05). **Schur at invariant nodes.** If `g k_* − k_* ∈ Λ^*` for every `g ∈ G`, then
  `[U(k_*), R_g] = 0`. If `R` is projectively irreducible, `U(k_*)` is scalar, and the pair of
  distinct eigenvalues of a massive sector (Sec. 1) does not exist there. For `R_i = σ_i ⊗ I_2`
  the commutant is `I_2 ⊗ M_2(C)` (the isotypic multiplicity space), which allows it. Nothing is
  said about non-invariant nodes.
- C3 (A-M-06). **Standard family, strict body.** The coefficients are
  `T_h = n diag(A_h, A_{−h}^†)`, `T_0 = [[0, imI], [imI, 0]]`. Each `A_h` has a nonzero
  eigenvalue, so for `n > 0` each corner coefficient is non-nilpotent. A path through the on-site
  step cannot reach `n h` in `n` steps for an extreme vertex `h`, so `(U^n)_{nh} = T_h^n != 0`, and
  `c_strict^iso = 1/sqrt(3)` for `0 < m < 1` (vertex lemma). `m = 1` excluded.
- C4 (A-M-07). **Explicit family.** Let `A(k) = u I − i v·σ` be a standard Weyl symbol
  (`u = 1 − |k|^2/6 + O(|k|^3)`, `v = Lk + O(|k|^2)`, `L^T L = I/3`) and
  `D_η(k) = [[cos η A, i sin η I], [i sin η I, cos η A^†]]`. With
  `U_{η,t} = (e^{itτ_x} ⊗ I_2) D_η` (multiplicity ⊗ spin order; a constant permutation gives the
  `σ ⊗ τ` order of M4), `0 < M < π/2`, `0 <= η <= M`, `t = M − η`:
  - `U_{η,t}(0) = e^{iMτ_x} ⊗ I_2`, half-gap `M`, multiplicities `2 + 2`;
  - `cos ω(k) = cos η cos t · u(k) − sin η sin t`;
  - `c_{ω^2}^2 = (1/3) M cos η cos t / sin M` (rechecked by hand by the author);
  - `c_H = (1/sqrt(3)) M cos η / sin M`, with full Clifford relations;
  - `tr T_h = 2 cos η cos t γ_h != 0` at every corner, so `c_strict^iso = 1/sqrt(3)`.
  Consequences if certified: QM-0 decided; `c_H(U_{0,M}) = M/(sqrt(3) sin M) > 1/sqrt(3)`
  (QM-1 fails for `H`); the pair `(η, t) = (M, 0)`, `(M/2, M/2)` at `M = π/3` decides QM-2a and
  QM-2b for both extractions.
- C4′. In this family `cos η cos(M − η) <= (1 + cos M)/2`, so
  `c_{ω^2}^2 <= (1/3)(M/2) cot(M/2) < 1/3`: `c_{ω^2} < c_strict^iso` there. Says nothing in
  general.
- C5. **Hypothesis:** in these classes, the multiplicity that makes mass possible is the same that
  makes the coefficients adjustable. Coexistence in M4 would not prove it.

## 1. Definitions

Units, lattice and Brillouin torus as in the minimal charter, Sec. 1. Every quantity belongs to a
**tuple** `(U, k_*, ω_*, P)`, not to `U` alone (A-M-01).

**Massive admissible tuple (A-M-01).**
- `P = P_+ + P_−`, with `P_±` the **full** spectral projectors of `U(k_*)` at `e^{-i(ω_* ± M)}`,
  `0 < M < π/2`, `rank P_+ = rank P_− = r/2`. So `r` is even: `r ∈ {2, 4}` in M4, `r = s` allowed
  (empty complement). The two eigenvalues are isolated from the rest of the spectrum at `k_*`.
- `P(k)` is the local continuation of the joint projector; no joint analytic parametrization of
  individual branches is assumed.
- **Uniform expansion:** for every branch `a` of the sector,
  `(ω_a(k_* + p) − ω_*)^2 = M^2 + c_{ω^2}^2 |p|^2 + O(|p|^3)` uniformly in the direction of `p`,
  with one `c_{ω^2} > 0`. This excludes every linear term and forces a common radial curvature.
- `M` is the quasienergy half-gap in lattice units, with the declared branch. It is not an
  inertial or physical mass.

**`c_{ω^2}`** is the coefficient above (non-negative root).

**`c_H` (A-M-02, A-M-03).** Fixed microscopic basis; no `k`-dependent basis change.
- `H_P(k) = P(k) · i log(e^{iω_*} U(k)) · P(k)`, logarithm branch with values near `±M` on the
  sector; `β = P_+ − P_−` up to the sign fixed by the phase convention `e^{-iω}`, stated in
  Stage (a).
- `α_j = P_* ∂_j H_P(k_*) P_*`, `∂_j = ∂/∂k_j`.
- **Dirac form:** `{α_j, β} = 0` and `{α_j, α_l} = 2 c_H^2 δ_jl P_*`, `c_H >= 0`. If either fails, the
  tuple is `NO_DIRAC_FORM` and has no `c_H`. The trace condition `(1/r) tr(α_j α_l) ∝ δ_jl` alone
  is not used (it does not imply the Clifford relations).
- `c_H` is a coefficient of the effective Hamiltonian, not a signal speed. A causal bound on it is
  not expected (C4).

**Causal comparator:** `c_strict^iso(U)` of the full symbol. The convex hull of
`N_3 ∪ {0}` is `C_micro = [−1/sqrt(3), 1/sqrt(3)]^3`, but `S_n`, `h_infty` and `c_strict^iso` are
computed for the actual symbol, never inherited from the support. Positivity `c_strict^iso > 0`
is checked per tuple before any quotient is formed (A-M-10).

**Admissible family (A-M-11).** `U_μ`, `μ ∈ [0, μ_0)`, with fixed support and coefficients
continuous in `μ` (polynomial or analytic in the cases certified), such that for `μ > 0` there is
a massive admissible tuple `(U_μ, k_*(μ), ω_*(μ), P_μ)` with `k_*`, `ω_*`, `P_μ` continuous,
`M(μ) → 0`, the joint sector isolated from its complement uniformly in `μ`, and
`(U_0, k_*(0), ω_*(0), P_0)` an admissible **massless** tuple in the sense of the predecessor's
Sec. 3, with slope `c_0`.

## 2. Frozen class declaration

| Item | Declaration |
| --- | --- |
| Geometry | d=3; **allowed** support `N_3 ∪ {0}`; the eight corners active (`T_h != 0`, `h ∈ N_3`); effective support recorded per symbol (it is `N_3` if `T_0 = 0`); one complete update per time unit |
| Internal dimension | `s = 4` |
| Class M4 (D1: only this) | axial `V4 = D2`, `R_i = σ_i ⊗ I_2`; `T_{gh} = R_g T_h R_g^†` for `h ∈ N_3 ∪ {0}`, so `T_0 ∈ I_2 ⊗ M_2(C)`, subject to unitarity (A-M-08) |
| Dynamical irreducibility | Not required; recorded |
| Control class | `s = 2`, allowed support `N_3 ∪ {0}`, `(V4, Pauli)`, `T_0` scalar: C2 at invariant nodes only |
| Control family | standard Dirac family, `0 < m < 1` |
| Nodes (D2) | every massive admissible tuple |
| Coefficient domain | real variables over all reals; exact algebra |

## 3. Questions and outcomes (per class M4, per extraction `X ∈ {H, ω^2}`)

| Question | Outcomes |
| --- | --- |
| QM-0 Existence | `NO_MASSIVE_SECTOR`; `MASSIVE_SECTORS_EXIST` (certified explicit tuple); `OPEN` |
| QM-1 Causal bound | `MASSIVE_BOUND_PROVED_IN_CLASS` (`c_X <= c_strict^iso` for every tuple with `c_X` defined); `MASSIVE_BOUND_VIOLATION_WITNESS`; `OPEN`. Decided separately for `H` and for `ω^2` (A-M-09) |
| QM-2a Normalized dependence | `NORMALIZED_DEFICIT_FORCED_IN_CLASS` (`c_X / c_strict^iso = f_X(M)` for every tuple, `f_X` exhibited); `NORMALIZED_DEFICIT_NOT_DETERMINED_BY_M_WITNESS` (two tuples with equal `M` and different quotients); `OPEN` |
| QM-2b Adjustability at equal causal body | `ADJUSTABLE_AT_EQUAL_STRICT_BODY_WITNESS` (two tuples with equal `M`, **equal full strict body** `C_∞^strict`, different `c_X`); `NOT_ADJUSTABLE_PROVED_IN_CLASS`; `OPEN` |
| QM-3 Massless recovery | per family: `RECOVERY_PROVED_FOR_FAMILY` (`lim c_X(U_μ) = c_0(U_0)`), `RECOVERY_FAILURE_WITNESS`; class-wide: `RECOVERY_PROVED_IN_CLASS` (every admissible family) or `OPEN` |

Reading rules:
- Every outcome names its extraction. `NO_DIRAC_FORM` tuples enter only through `ω^2`.
- A witness (QM-1 violation, QM-2a, QM-2b, QM-3 failure) needs explicit exact symbols with every
  requirement certified. A class-wide proof needs the whole class; a failed search proves nothing.
- QM-2b implies QM-2a's witness outcome; not conversely.
- QM-3 compares with `c_0(U_0)`, not with `c_strict^iso`: they differ already at `M = 0` in M4.
- Equality of `c_strict^iso` (a scalar) is not equality of strict bodies.

## 4. Methods, sequence, budget and stops

**Methods (A-M-12).** Groebner bases decide polynomial identities only (unitarity, covariance,
Clifford relations, exact coefficient identities). Spectral statements (isolation, branch
expansions, logarithm branch, real inequalities, strict body) are decided by explicit analytic
proofs or exact closed forms, checked symbolically where possible. No complete decision procedure
for the class is promised.

- **Stage (a): controls and candidates.** Exact verifier and report for:
  - the standard family: reproduce `c_H = r_in F`, `c_{ω^2} = r_in sqrt(F)`; C3 (strict body);
  - C2 in the control class at invariant nodes; C1;
  - the family `U_{η,t}` of C4: unitarity, covariance, support, node, spectrum, `c_{ω^2}`, `c_H`
    with Clifford relations, strict body; at `M = π/3` the two members of the QM-2 pair.
  - Decides, if all pass: QM-0; QM-1 for `H` (violation witness); QM-2a and QM-2b witnesses for
    both extractions; QM-3 for this family.
- **Stage (b): QM-1 for `ω^2`.** A proof (new argument relating curvature to the exact support)
  or an explicit violation witness. Stop: `OPEN`.
- **Stage (c): QM-3 class-wide.** Proof over all admissible families, or a failure witness (for
  example a massive deformation of the `s=4` counterexample family, whose massless slope is
  `a/sqrt(3) < c_strict^iso`). Stop: `OPEN`.
- Each stage is authorized separately, with its budget (wall time, scope, deliverable, closure).
- No floating point in a certified quantity; no fitted tolerances; no rigidity from scans.

## 5. Ceilings

No statement about interactions, `s != 4`, other symmetry classes, other supports, reflections or
antiunitaries as symmetries, the absolute scale, or nature. No definition of species and no claim
about question A. `c_H` and `c_{ω^2}` are never called "the speed of light" of the sector without
naming the extraction. `v_max` is never written unqualified. Novelty: OPEN; local `biblioteca/`
first, external search needs separate permission.

## 6. Review

As in the minimal charter, Sec. 6. The draft gets a different-family review before freezing.
Stage (a)'s certificate and outcomes are reviewed before entering `CURRENT_STATE` as more than
PRELIMINARY.
