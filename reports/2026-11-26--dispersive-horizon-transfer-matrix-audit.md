# Audit of the 12×12 spatial transfer matrix (dispersive-horizon walk)

Date: 2026-11-26. Branch: `review/dispersive-horizon-transfer-audit`, from
`main` at `8fd37a5`.
Reviewed candidate: `reports/2026-11-26--dispersive-horizon-three-step-transfer.md`,
written at `8e5b540` and unchanged at `8fd37a5`, SHA256
`7e372669d0155b26c26b50e464c33a4c7d6612dcf2d5e791b01d57cda90d63b6`.
Verifier: `scripts/verify_dispersive_horizon_transfer_matrix.py`, 61/61 exact
checks, about 45 s, SHA256
`98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2`.
No gate charter exists for this line. This audit records a review of the
author derivation and does not authorize anything.

**Status: PASS in the algebraic scope below. TRANSMISSION = OPEN.
NOVELTY = not assessed. Not promoted.**

**Amendment 1 (2026-11-26), after the Astra review**
(`2026-11-26--dispersive-horizon-transfer-matrix-astra-review.md`). Astra
returned REPAIR_REQUIRED on three statements of this audit, not on the matrix.
All three are repaired below and marked "[A1]":

- the T3 site count, which is 21, not 22;
- the general claim about roots at points of zero velocity;
- "all θ", which now reads "all admissible θ".

The new results are certified by
`scripts/verify_dispersive_horizon_transfer_repairs.py` (8 checks, run after
the 61 reviewed ones). The bytes of the reviewed verifier are unchanged.

**Amendment 2 (2026-11-26), after the Grok review of Amendment 1**
(`2026-11-26--dispersive-horizon-amendment1-grok-review.md`). Grok confirmed
every figure in Amendment 1 and returned REPAIR_REQUIRED on three points:

- the k³ expansion was attributed to R2/R3, which certify only multiplicities;
- the twin degeneracy at (z, λ) = (−1, −1) was missing;
- the semisimplicity at the profile endpoints and the ordinary band edge in
  the interior were not stated.

The repairs are marked "[A2]" below. They are certified by
`scripts/verify_dispersive_horizon_transfer_amendment2.py` (39 checks, run
after the 61 + 8 earlier ones). The earlier verifiers' bytes are unchanged.

## Reviewer and independence

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`) in Claude Code. The user
  asked for the audit with a pasted brief: derive the matrix from the
  operator, check every block, the determinant, the homogeneous dispersion and
  the extra checks, give one round and one verdict, and do not compute
  transmission.
- **Independence:** the author's model family is not recorded in the
  candidate. If it was written with Claude, this is an author-side audit and
  not independent verification (`CLAUDE.md`, "No autophagy"). Independence
  still needs a cross-family review (`revision-ciega` / `sanedrin`) or a
  person.
- **Tools:** no `~/herramientas` or `sanedrin` tool was used.
- **How the audit ran:** the derivation was first redone by hand. Exploratory
  SymPy checks were run in a scratchpad and are superseded by the versioned
  verifier, which is the only provenance for the results below.

## Conventions (§1 of the brief): PASS

In coordinates:

- (Sψ)↑(x) = ψ↑(x−1)
- (Sψ)↓(x) = ψ↓(x+1)
- (L₋f)(x) = f(x+1)
- C(β) = exp(−iβσ_y), verified (T1).

**Coin order.** W = S C(θ) S C(θ) S C(−2θ) acts right to left, so the coin
order of W² is (−2θ, θ, θ, −2θ, θ, θ). The verifier reads this off the word
of W (T1).

**Stationary equation.** With q₁ = ψ and q_{j+1} = S C(β_j) q_j, we have
q₇ = W²ψ and (Uψ)(x) = q₇(x+1). So Uψ = zψ is equivalent to
q₇(x+1) = z q₁(x).

**Fourier symbol.** On ψ ∝ e^{−ikx}: S(k) = diag(e^{ik}, e^{−ik}) and
L₋(k) = e^{−ik}. With Floquet eigenvalues e^{iΩ}, the stationary phase gives
x = (∂ₖΩ) t, so the sign of v = ∂ₖΩ is correct.

## Matrix and equivalence (§2): PASS

**Stage relations.** With the coin at site x and then the shift:

- (i) a_{j+1}(x+1) = c_j(x) a_j(x) − s_j(x) b_j(x)
- (ii) b_{j+1}(x−1) = s_j(x) a_j(x) + c_j(x) b_j(x)

Solving (ii) for b_j(x) and substituting into (i), using c² + s² = 1, gives
the report's ten rows.

**Closures.**

- Up closure: a₇(x+1) = z a₁(x) with (i) at j = 6 gives the b₆(x) row.
- Down closure: it cannot be imposed at x, because b₇(x−1) = z b₁(x−2) lies
  outside Y_x. It is imposed at site x+1. There, (i) and (ii) for j = 6 give
  z a₁(x+1) = (a₆(x+1) − s₊ b₇(x)) / c₊, with b₇(x) = z b₁(x−1). The result
  is the report's a₁(x+1) row, with c₊ and s₊ evaluated at x+1.

**Entries.** All 144 entries agree with the report's P, Q, R and H. Of these,
25 are structurally nonzero: P 6, Q 7, R 7, H 5.

The verifier checks this without the report's combined forms (T2):

- It solves the raw 13-equation system: (i) and (ii) for j ≤ 5, the up
  closure at x, and stage 6 at x+1, with b₆(x+1) as an auxiliary unknown.
- The angles are free and independent: c_j, s_j at x, and c₆, s₆ at x+1.
- The system's determinant is −c₁c₂c₃c₄c₅ · c₆(x+1) · s₆(x) · z.
- Each difference from the report's entries is decided exactly by reducing
  its numerator modulo c² + s² − 1.
- Negative controls: a single sign flip, and the closure coefficients taken
  at x instead of x+1, are both detected.

**Second route (T3).**

- Iterate the report's M with site-dependent rational coins and
  z = (3+4i)/5.
- Rebuild ψ, apply U from its definition, and check Uψ = zψ exactly at 21
  interior sites (6..26) [A1; the original text said 22].
- The intermediate stage vectors match the components of Y in 280
  comparisons.

**Equivalence, written argument.** Assume c_j(x) ≠ 0 for j ≤ 6, s₆(x) ≠ 0 and
z ≠ 0 at every site.

- **From the operator to the recurrence.** A solution ψ determines all q_j.
  The 13-equation system has a unique solution, so Y_{x+1} = M_x Y_x.
- **From the recurrence to the operator.**
  - For j ≤ 5, each pair of rows is an invertible transformation of (i)/(ii).
  - Define q₇ := S C(β₆) q₆. The b₆ row at x gives a₇(x+1) = z a₁(x).
  - The b₆ row at x+1 combined with the a₁ row gives
    b₇(x) = s₊ a₆(x+1) + c₊ (c₊ a₆(x+1) − z a₁(x+1)) / s₊ = z b₁(x−1).
    The verifier checks the algebraic core of this step (T2, auxiliary
    b₆(x+1)).
- **Inverse map.** ψ is recovered as q₁(x) = (Y_x[1], Y_{x+1}[7]).

So solutions of Uψ = zψ on ℤ, with no ℓ² condition, correspond one to one and
linearly to orbits of M. The solution space has dimension 12, and there are no
spurious solutions.

Caveat for finite segments: the down closure at the last site uses one more
step, which matters when imposing boundary data.

## Determinant (§3): PASS

**Proof.**

- Stages 1–5 map disjoint pairs (a_j, b_{j+1}) → (a_{j+1}′, b_j′) with
  matrix (1/c)[[1, −s], [−s, 1]]. Its determinant is (1 − s²)/c² = 1.
- The two closures are triangular with respect to variables already
  produced. Their diagonal factors are c₆/s₆ and −s₊/c₊.
- The slot assignment is one 12-cycle, 1→2→…→6→12→11→…→7→1, with sign −1.

Result: det M_x = cot β₆(x) / cot β₆(x+1), which equals
cot θ_x / cot θ_{x+1} under the rule.

**Verifier (T4):** the identity holds for general angles, with no z
dependence.

**Consequences.** The determinant is positive for θ ∈ (0, π/2), has no extra
factors, holds for a variable profile, and equals 1 in a homogeneous medium.

## Homogeneous dispersion (§4): PASS

**Relation of dispersion (T5).** tr W/2 = A cos 3k + (1−A) cos k with
A = t(2t − 1) and t = cos²θ, and det W = 1. Hence

det(z − λW²) = z² − zλ(4f² − 2) + λ²,

which times λ⁵ is the report's polynomial. Here λ = e^{−ik}, and f is
symmetric under λ ↔ 1/λ.

**Characteristic polynomial (T5).** charpoly(M_hom) · (−zA²) equals the
report's polynomial for symbolic admissible θ (all denominators nonzero, z ≠ 0)
[A1], with the same coefficients and therefore
the same multiplicities. The polynomial has degree 12, with leading and
constant coefficient both −zA², nonzero for A ≠ 0.

**Bloch correspondence.** Through the bijection above, eigenvalues λ of M
correspond to Bloch modes with complex k.

**Floquet degeneracy (T6).**

- W(π/2)² = −I for every θ, so U(π/2) = iI.
- At t = 5/16, 3/8 and 7/16, with z = i and λ = −i:
  - two explicit, independent Bloch vectors are eigenvectors of M;
  - (λ + i)² divides the characteristic polynomial and (λ + i)³ does not.
- The root is therefore double and semisimple.

The nonzero tests use exact minimal polynomials, not simplification.

**Points of zero group velocity [A1, A2].** The original text said that band
edges (∂ₖΩ = 0) give double roots of the usual non-semisimple kind. That holds
only at a nondegenerate quadratic extremum (Ω″ ≠ 0) of a simple band. On this
profile the degenerate points are:

- **Horizon, t = 3/8.** The outgoing infrared velocity vanishes.
  - E = k/2 + (35/64)k³ + O(k⁵), so Ω₊ = (35/32)k³ + O(k⁵) (amendment-2
    verifier G3). This confirms the coefficient Astra and Grok derived.
  - (z, λ) = (1, 1) is a root of algebraic multiplicity 4 and geometric
    multiplicity 2 (repairs verifier R2).
  - So is its twin (z, λ) = (−1, −1), at k = π (G1) [A2].
  - The contact orders 3 + 1 give a Jordan partition 3 + 1 [UNVERIFIED: Grok's
    argument, not machine-checked].
- **Endpoints, t = 5/16 and t = 7/16.** At both (1, 1) and (−1, −1) the root
  has algebraic multiplicity 2 and geometric multiplicity 2. It is semisimple
  and is not a band edge (repairs verifier R3; G2) [A2].
- **Interior, ordinary band edge [A2].** Write u = cos²k and C = cos k. On
  (0, π/2), v₊ = 0 is equivalent to 4(1 − u)g′(C)² = 1 − g(C)². This
  equivalence is a written step: −f′ = sin k · g′(C) > 0 and sin E > 0 there.
  The resulting polynomial in u factors as (u − 1) × a quadratic.
  - At t = 5/16, the quadratic is proportional to 2625w² + 5w − 16 with
    w = u − 1. Its discriminant 168025 is nonzero, and it has exactly one root
    u ∈ (0, 1): one zero-velocity point of the outgoing branch in (0, π/2)
    (G4).
  - At t = 3/8, the factor is (u − 1)², the k³ contact, with no root in
    (0, 1).
  - At t = 7/16, there is no root in [0, 1].
  - So the interior medium has an ordinary band extremum of Ω₊ and the
    exterior medium does not. Whether the double root there is non-semisimple
    requires Ω″ ≠ 0 at that point, which is [UNVERIFIED]. A choice of ω* at
    the extremum's quasienergy must treat it.

The channel analysis must treat these degeneracies separately.

## Additional checks (§5)

**Support [−7, 5]: PASS (T7).** Six shifts of ±1 plus L₋ bound the support.
For one site-dependent coin configuration, U δ_{x0,↑} has a nonzero ↑
amplitude at x0+5, and U δ_{x0,↓} has a nonzero ↓ amplitude at x0−7. In
general, the extreme amplitude is a product of coin cosines, which is nonzero
on the profile.

**Denominators: PASS (T8).** For t ∈ [5/16, 7/16]: cos θ = √t,
sin θ = √(1−t), and cos 2θ = 2t − 1 ∈ [−3/8, −1/8].

**Velocities: PASS (T8).**

- 1 + 8A = (4t − 1)².
- f = 1 − (1 + 8A) k²/2 + O(k⁴), which gives v_IR,out = 8t − 3 = −1/2, 0, 1/2.
- f(π/2) = 0, and −f′(π/2) = 1 − 4A, which gives v_UV = 1 − 8A = 31/16, 7/4,
  23/16.
- The step E′ = −f′/sin E and the relation v = −1 + 2E′ are analytic and not
  certified by the script.

**Branch continuity: proved here, ingredients certified (T8).** This is a
claim of the candidate's §5 that the brief left as interpretation.

- Write f = g(cos k) with g(C) = 4AC³ + (1 − 4A)C, so g(0) = 0 and g(1) = 1.
- A < 0 on the profile, so g′(C) = 12AC² + 1 − 4A ≥ g′(1) = (4t − 1)² > 0
  on [0, 1].
- Hence 0 ≤ f < 1 on (0, π/2], and E = arccos f is smooth there.

So Ω₊ runs continuously from the infrared node to π/2.

**Not proved here:** the compactness step that gives ω* and k₊(t). It is
standard, but written only in the candidate.

## Interpretation, separate from the algebra

- Whether the branch near k = π/2 is the same field as the infrared mode, or
  an extra Floquet species, remains open, as the candidate says.
- At z = i the degeneracy occurs in every medium at once, because
  Ω₊(π/2) = π/2 for every t. The candidate's ω* < π/2 avoids that point. A
  choice of ω* close to π/2 must watch it.
- "Outgoing" and "incoming" are kinematic labels on group velocities. They
  do not establish physical channels.

## Verdict

| Section | Verdict |
| --- | --- |
| 1 Conventions | PASS |
| 2 Matrix, 144 entries, equivalence, no spurious solutions | PASS |
| 3 Determinant | PASS |
| 4 Homogeneous dispersion, multiplicities, z = i degeneracy | PASS |
| 5 Support, denominators, velocity values | PASS |
| 5 ω*, k₊(t) compactness step | UNVERIFIED (author argument only) |
| Global | **PASS** (algebraic scope) |

**Can the published M_x(z) be used as a reliable mathematical starting point
for the stationary transmission problem through the tanh profile?**

Yes, under these conditions:

- t_x ∈ (0, 1) and t_x ≠ 1/2 at every site, which the tanh profile
  satisfies;
- |z| = 1.

**Validated:**

- every entry of M_x;
- the bijection with Uψ = zψ;
- the determinant;
- the homogeneous characteristic polynomial for all admissible θ, with z ≠ 0 [A1];
- the multiplicities at (z, λ) = (±1, ±1) on the three profile values, and the
  k³ coefficient at the horizon [A1, A2];
- the location of the ordinary band edge of Ω₊ at t = 5/16 and its absence at
  t = 7/16 [A2];
- the structure at z = i on the profile values;
- the support, the denominators and the velocity values.

**Still open:**

- classification of propagating and evanescent modes in both limits;
- flux normalisation;
- treatment of band-edge Jordan blocks;
- 𝒯_L(ω*) > 0;
- the Floquet-species interpretation;
- cross-family independence of this review.

Nothing in `state/CURRENT_STATE.md` or `README.md` changes with this report.
Promotion is a separate decision for the user.
