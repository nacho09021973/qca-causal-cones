# CURRENT_STATE

**Date:** 2026-09-15  
**Status:** STANDARD WEYL/DIRAC EXACT GATE: PASS; strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS (branch-local)

**Branch-local state.** This file is reconciled on
`research/b-infinity-post-s4-gate` only, so that it agrees with all evidence
merged on this branch. It is **not** a canonical promotion: `main` is
unchanged, and promotion requires a separate explicit decision.

**Repository:** `nacho09021973/qca-causal-cones`

**Evidence baseline:** `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.
Canonical promotion is recorded in
[`2026-09-14--standard-gate-promotion.md`](../reports/2026-09-14--standard-gate-promotion.md).
**No successor scientific gate is currently chartered** (Sec. 7).

**Correction (2026-09-14):** `B*` as a comparison against the one-step
inradius `r_in(C_micro)` is superseded by `B_infty^*`, a comparison against
the strict asymptotic isotropic speed `c_strict^iso`. See
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) and
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0. New baseline-specific certificate: for the
standard Pavia Weyl family in d=3, `C_infty^strict = C_micro` exactly, so
`c_strict^iso = r_in(C_micro) = 1/sqrt(3)`; see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
This baseline-specific certificate did not by itself close the gate; the
later s=4 counterexample completed it for the declared s=4 class.

**Integration (2026-09-15, branch-local):** an explicit irreducible `s=4`
family on the same `N_3`, with the same `D2` action, has
`C_infty^strict = C_micro` and `c_strict^iso = 1/sqrt(3)`, but
`c_0(a) = a/sqrt(3)` for every `0 < a < 1`. This is `COUNTEREXAMPLE_VERIFIED`
in the sense of the
[gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) Sec. 5 for the
declared `s=4` class (Sec. 4.1 below). It does not refute the standard Pavia
`s=2` certificate above. Evidence:
[analytic note](../theory/S4_STRICT_CONE_COUNTEREXAMPLE.md) and
[freeze record](../reports/2026-09-15--s4-strict-cone-counterexample-freeze.md)
(`1dae941`), [independent review](../reports/2026-09-15--s4-independent-review.md)
(`aeec462`), [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md)
(`f74018f`). **NOVELTY = OPEN.**

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.
- In the verified standard Dirac couplings they differ for every `0 < m < 1`.
  Name the extraction `c_H` or `c_{ω^2}`; do not use an unspecified finite-lattice
  `c_IR` as though those coefficients were interchangeable.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Canonical hypothesis status

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

### B_infty^* — strict asymptotic matching (supersedes B* / inradius matching)

Candidate:

`c_0 = c_strict^iso`, `c_strict^iso = min_{n̂} h_infty(n̂)`,

with `h_infty` the strict asymptotic support function of
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md) Sec. 6.
Interpretation: `c` would match the exact long-run isotropic propagation
speed of the same dynamics, not necessarily the inradius of the one-step
body `C_micro` — the two satisfy `c_strict^iso <= r_in(C_micro)` in general,
with equality only where separately certified (see the d=3 row below).

| Claim | Status and scope |
| --- | --- |
| A — IR universality | **OPEN** |
| B_max | **REJECTED** under isotropic containment in an anisotropic causal body, d >= 2 |
| B_full | **REJECTED / GEOMETRICALLY IMPOSSIBLE** for a nondegenerate isotropic ball equaling a finite lattice polytope, d >= 2 |
| Exact finite-mass B* | **REJECTED IN STANDARD DIRAC FAMILY**, for both specified extractions, every 0 < m < 1 (comparison against `r_in(C_micro)`, unaffected by the B_infty^* correction) |
| B*_0 (linear order, `c_0=r_in`) | **VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN** |
| B*_cont | **VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN** |
| B_infty^*, d=3 Pavia baseline (`C_infty^strict=C_micro`, full nonlinear order) | **CERTIFIED for the standard Weyl family `A+,B+,A-,B-`** (`s=2`): `c_0 = c_strict^iso = 1/sqrt(3)`; d=1,2 not checked; unaffected by the s=4 result |
| Strong B_infty^* (`c_0 = c_strict^iso` forced by locality, unitarity, homogeneity and D2 covariance at fixed `N_3`) | **REJECTED IN DECLARED s=4 CLASS** — explicit counterexample, Sec. 4.1; false for any class containing that family |
| B_infty^* in the published minimal `s=2` class (P17, including its Eq. (2)) | **NOT REFUTED by the s=4 result; rigidity OPEN as an in-repo claim.** Origin-node inradius matching there is a conditional application of P17's classification plus the standard certificate, not a new theorem. The strict-body certificate is recorded for `A+,B+,A-,B-`; its transfer across all of P17's equivalences is not separately checked |
| B_infty^* for `s=2` without P17 Eq. (2), or with an irreducible internal symmetry representation `R` for `s>2` | **OPEN** |
| Novelty of the s=4 family and its strict-support statement | **OPEN** — no equivalent found in eleven checked primary sources; not a novelty certificate |

The restricted statements are established for the declared cases below.
There is no general rigidity theorem, proof of A, or novelty claim.

### 4.1 Declared s=4 counterexample class

**Status: COUNTEREXAMPLE_VERIFIED for this class; independent review PASS;
NOVELTY = OPEN.**

| Item | Declaration |
| --- | --- |
| Geometry | d=3, `N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`, all eight modes active, no on-site coefficient, one complete update per time unit, phase `exp(-i k.h)` |
| Internal space | `s=4 = C^2_sigma (x) C^2_tau`; parameter `0<a<1`, `b=sqrt(1-a^2)` |
| Symbol | `A_a(k) = W exp(-i q_x Gamma_x) exp(-i q_y Gamma_y) exp(-i q_z Gamma_z)`, `q_i=k_i/sqrt(3)`, `W = I (x) exp(-i pi tau_z/4)` |
| Isotropy | D2 half-turns acting on `N_3`; `R_i = sigma_i (x) I_2` — two copies of the Pauli projective class, hence a **reducible** representation; full cubic symmetry not assumed |
| Irreducibility | Dynamics irreducible: scalar joint commutant of all eight Fourier coefficients |
| Gapless sector | `k=0`; two isolated rank-two clusters at quasienergies `+/-theta`, `theta=pi/4`; isotropic, untilted cones measured from each cluster's node |
| Result | `C_infty^strict = C_micro` exactly (all vertex traces nonzero, so no vertex coefficient is nilpotent); `c_strict^iso = 1/sqrt(3)`; `c_0(a) = a/sqrt(3)` |
| Coverage | One particular product ansatz, not a classification of four-component walks |

Scope limits, all retained:

- **Procedure.** The class table above was written at the freeze and review,
  after the construction, not before solving as charter Sec. 2 requires. This
  limits which classes the example speaks to; it does not affect the
  mathematical validity of the certified inequality.
- **Strict means exact support.** Vertex amplitudes may decay exponentially.
  No ballistic, essential or Lieb-Robinson front statement is made.
- **Floquet-shifted nodes.** `A(0) = W` is not a global phase.
- **Family identity only.** For `0<theta<pi/2`,
  `c_0^2 + 2 sin^2(Delta eps/2) g_ii(0) = 1/3`, where `Delta eps = 2 theta`
  and `g` is the projector quantum metric. It comes from the
  intra/inter-sector split `a^2 + b^2 = 1` of the involutions `Gamma_i`.
  Equating `1/3` with `(c_strict^iso)^2` additionally needs vertex survival,
  which is certified at `theta=pi/4`, or, for fixed `a`, on an open
  neighbourhood where all vertex traces remain nonzero. This is not a
  general QCA theorem.
- **Prior art.** Product-of-projector walks (MB18, BM25), four-component Weyl
  mixing (BB94), shifted Floquet Weyl nodes, adjustable continuum velocity,
  and involution block completion (AF16/17) are antecedents and must be
  attributed. Raynal's explicit s=4 Dirac family is excluded as an
  identification. The most useful open equivalence check is AF16/17's
  homogeneous paired-walk specialization.
- **Certificates.** `scripts/cert_Aa_s4_counterexample.py` and
  `scripts/review_Aa_s4_exact.py` both return PASS (SymPy 1.14.0, zero
  tolerance), and `scripts/verify_weyl_dirac_gate.py` still returns PASS
  (375 checks), on this branch.

## 5. Completed standard Weyl/Dirac exact gate

**Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**

Evidence is the committed
[contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
[analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
[verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
[permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
Source provenance and the published sign/dagger issues are recorded there.
The analytic proof establishes the open mass interval and continuum scaling;
the check count alone is not their justification or a formal proof certificate.

### Declared family and coordinates

The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
the minimal two-component blocks. The seven symbols are not seven independent
geometries: transposes/chiralities within a dimension share support, inradius
and linear speed. There are three dimension-specific geometries in this battery.

Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
complete update per time unit:

`N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,

`C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,

`r_in = 1/sqrt(d)`, `V_causal^max = 1`.

### Massless equality

For d=1,2,3 in this family, at the declared zero node,

`m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.

This is equality of the linear IR coefficient, not exact finite-momentum
relativistic dispersion or a theorem about every admissible symbol.

### Fixed nonzero lattice mass

For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
`0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
continuous from the identity near the massless zero node. Then

`cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,

`F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.

Exact finite-mass B* is refuted in the standard family under either extraction.
This result is no longer PRELIMINARY.

The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
expansions: `b = r_in^2 n (1-F)/(2m)` and
`c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
not a failure of the exact spectrum or an inconsistent calculation.

The endpoint m=1 is separate: actual hopping vanishes, active support becomes
`{0}`, and its inradius and spatial coefficients are zero. It is not covered
by the strict inequalities for `0 < m < 1`.

### Small-mass / continuum matching

For each standard coupling in d=1,2,3,

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
the equality of the limits is established analytically. The joint scaling
of momentum, dimensionless mass, neighbor length and time step is specified
in the report. Its continuum statement is local at fixed rescaled momentum
and mass, not a full propagator convergence theorem on arbitrary states.

## 6. Current scientific interpretation

The live idea is no longer:

`c = maximum microscopic speed`,

nor, unqualified, `c_massless = r_in(C_micro)`. The corrected comparison is
`B_infty^*`: `c_0 = c_strict^iso`, the exact strict asymptotic isotropic
speed of the same dynamics (Sec. 4). Its strong form is rejected in the
declared s=4 class (update below). `r_in(C_micro)` remains a provable
upper bound (`c_strict^iso <= r_in(C_micro)`), and is known to be exactly
attained — `c_strict^iso = r_in(C_micro)` — for the standard Pavia Weyl
family in d=3, by an explicit vertex non-nilpotency certificate, not merely
by the linear-order Taylor coefficient.

**Update (2026-09-15, branch-local).** Locality, unitarity, homogeneity and
D2 covariance at fixed `N_3` do **not** force `c_0 = c_strict^iso` once the
internal dimension is enlarged. The s=4 family (Sec. 4.1) keeps the whole
strict body, `C_infty^strict = C_micro`, while its Weyl slope varies
continuously below `1/sqrt(3)`. The strict causal body alone therefore does
not fix the Weyl speed. In this family the missing speed is exactly
accounted for by the inter-sector part of the involutions (the family
identity in Sec. 4.1). Whether that is a structural principle or a feature of
this ansatz is **OPEN**.

What remains unknown is which additional hypotheses restore matching: `s=2`
minimality with or without P17 Eq. (2), irreducibility of the internal
symmetry representation, a whole-symbol common cone, or something else.
Whether `c_strict^iso` saturates `r_in(C_micro)` for every admissible symbol
(saturation, charter Sec. 0(ii)) is a separate question and also remains
open.

At finite mass the two natural extraction procedures differ exactly. A common
relativistic coefficient is recovered in the specified continuum limit.
Additional equivalent representatives cannot resolve the open generality issue;
any successor gate must examine structural freedom under fixed causal geometry
and discrete isotropy.

## 7. GATE STATUS — no calculation currently authorized

**MASSLESS INRADIUS RIGIDITY GATE — COUNTEREXAMPLE_VERIFIED IN DECLARED s=4
CLASS (branch-local); s=2 and irreducible-R classes OPEN; successor gate NOT
YET CHARTERED.**
(Charter name kept for continuity; its comparison target is corrected, see
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0.) Where the charter or
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) still describe the
gate as having no counterexample, this section overrides them
(`PROJECT_INSTRUCTIONS.md` Sec. 2).

### 7.1 Superseded operative plan

The 2026-09-14 deliberation
([`debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md`](../debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md))
predates the s=4 result. It recommended freezing an `s=2` contract on `N_3`,
filtering candidates by non-nilpotent vertices, and escalating to `s>2` only
after exhausting that class. That order was not followed, and its
"rigidity vs saturation" framing cannot continue as written. It is kept as
historical decision material, not as a current plan. Its open point about
whether P17 Eq. (2) is derivable from the charter's identities still matters
for the `s=2` question.

### 7.2 Successor gate — to be chartered before any calculation

No successor calculation is authorized until a charter is committed. Its
question should be narrower than the refuted strong form. Candidate
directions, none of them frozen yet:

1. **Surviving bounds.** Which inequalities between `c_0`, `c_strict^iso`
   and `r_in(C_micro)` hold for every admissible symbol? Currently
   `c_strict^iso <= r_in(C_micro)` is established. `c_IR <= r_in(C_micro)`
   is established only under the isotropic-containment premise of Sec. 3.3.
   `c_0 <= c_strict^iso` is not established in general.
2. **Restoring hypotheses.** Which explicitly stated extra assumptions (for
   example `s=2` minimality with or without Eq. (2), or an irreducible `R`)
   give `c_0 = c_strict^iso` for a whole declared class?
3. **Intra/inter rule.** Does the s=4 family identity reflect a general
   structure that accounts for the missing speed, or is it specific to this
   ansatz?

Every class must keep the quantifiers of charter Sec. 2 and be declared
**before** solving.

### 7.3 Original gate question (answered for the declared s=4 class)

The original question was whether another admissible massless symbol can have
`0 < c_0 < c_strict^iso` for its own strict asymptotic body, while preserving
the same `N`, `C_micro`, embedding, unitarity, homogeneity and discrete
isotropy as its selected standard baseline. A candidate whose `c_0 < r_in(C_micro)`
only because its own strict body already falls short of `r_in(C_micro)` for a
combinatorial reason (a nilpotent one-step coefficient) is not this
counterexample; see the charter's Sec. 0 for the (i)/(ii) split.

The [gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) requires the
internal dimension, isotropy group/action and representation, node/sector,
and any irreducibility assumptions to be explicit before solving. Do not
silently introduce minimality or weaken the symmetry when interpreting a result.

- One exact admissible counterexample refutes B_infty^* for a class containing
  it (realized for the declared s=4 class, Sec. 4.1).
- A rigidity claim requires an exhaustive analytic argument for an explicitly
  quantified class; failure to find a deformation is not such an argument.
- The absence of a continuous deformation alone does not exclude disconnected
  admissible symbols. A restricted proof leaves wider generality open.
- Prior-art classification assumptions must be checked before any novelty claim.

### Stop rule

Until a successor gate is chartered and closed:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO anisotropic-QCA detour**;
- **NO change of support, embedding, time normalization or discrete isotropy
  within a declared rigidity comparison**;
- **NO novelty claim for B*, B_infty^* or the s=4 family (NOVELTY = OPEN)**;
- **NO use of a scalar `v_max` without definition**;
- **NO promotion of the s=4 family identity to a general QCA law**.

A certified falsification within the frozen admissible class is a successful
gate outcome. The s=4 counterexample is such an outcome for its declared
class only. This branch-local reconciliation does not promote anything to
`main` and does not charter the successor gate.
