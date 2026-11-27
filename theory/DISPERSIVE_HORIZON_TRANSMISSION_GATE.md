# Dispersive-horizon transmission gate

2026-11-26. Author: Claude Code (Claude Opus 5.5). Initial status **OPEN**.
Frozen by the commit that adds this file on branch
`research/dispersive-horizon-channels`, before any execution.

## Authorization and budget

- **Drafting.** User message, 2026-11-26: «1 y 2, luego con las comprobaciones
  3», where 3 was "draft the transmission charter".
- **Freezing.** User decisions, 2026-11-26: «lo segundo, limite brusco y
  revision por Astra 6.2». See "User decisions" below.
- **Not authorized:** execution and promotion. Each needs a separate user
  decision. The review model is fixed (Q4) but sending still needs the
  user's go-ahead.
- **Budget:** one contract. A balance is mandatory on closure. No further
  contract follows automatically.

## Known, question, abandonment

**Known** (with source):

- **Channels on I, reviewed.** `reports/2026-11-26--dispersive-horizon-channels.md`
  with Amendment 1, reviewed by Astra 6.2 (PASS), gives on
  I = (arg z_c*, π/2):
  - in each medium, 4 propagating channels (1 right, 3 left) and 4 + 4
    evanescent;
  - a conserved flux form G_x;
  - unit-flux modes at z₀ = (3+4i)/5.
- **Channels below the threshold arc.** The same report gives, at regular
  levels, 6 interior propagating roots (2 right, 4 left) for
  0 < dist(ω, πℤ) < arg z_c* ≈ 0.089, and 4 (1 right, 3 left) in the exterior.
- **Profile.** `reports/2026-11-26--dispersive-horizon-three-step-transfer.md`
  (`8e5b540`): t_L(x) = 3/8 + tanh(x/L)/16, with L > 0 free and t_L(0) = 3/8
  for every L.
- **Low-k branch (author remark, from Ω₊ = −k + 2E with E ≈ (4t − 1)|k|).**
  v(k → 0) = −1 + 2(4t − 1). This is −1/2 in the interior (left-mover) and
  +1/2 in the exterior (right-mover), and it vanishes at t = 3/8. So the
  horizon proper, a sign change of the low-k velocity, lives near ω ≡ 0
  (mod π).
- **Prior art** (`investigaciones/2026-11-26-dispersive-horizon-prior-art/comprobacion.md`,
  checked in the originals):
  - Maertens–Bultinck–Van Acoleyen 2204.06583: local evolution followed by a
    translation gives a horizon with doublers and partial transmission.
  - Sabsovich et al. 2106.14553: a stationary lattice S-matrix in which one
    band is transparent (T ≈ 1) and mixing with the doublers has probability
    1/(1 + e^{2πω/α}).
  - Tarasinski–Asbóth–Dahlhaus 1401.2673, Sec. VI: winding forces perfectly
    transmitting unidirectional channels.
  - Richard–Suzuki–Tiedra de Aldecoa 1801.02779: existence and completeness of
    wave operators for one-step U = SC with different asymptotic coins.

**Caveat to be decided before freezing (author, not computed).** On I the
incident interior right-mover is a high-wavenumber branch (k ≈ 1.23). Suppose
z₀ stays a regular value for every intermediate medium t ∈ [5/16, 7/16]. Then
that branch connects continuously to the exterior right-mover (k ≈ 1.11), and
for slowly varying profiles (L ≫ 1) one expects T → 1 by adiabatic continuity
`[UNVERIFIED]`.

That would be the transparent-band case of Sabsovich et al., not escape
across the horizon. A nonzero T on I would then answer "does any channel
connect inside and outside?" (yes) without saying anything about the horizon.
The horizon-relevant regime is the arc near ω ≡ 0, where the interior has two
right-movers and the window rule of the channels charter does not apply.

**Question.** For the declared profiles and quasienergies, is the
interior-to-exterior right-moving transmission T = |t|² nonzero? Is the
incident channel adiabatically connected to the transmitted one, or does it
cross the horizon branch?

**Abandonment of the line.** If T = 0 identically on the declared set, by a
structural argument (for example a symmetry forcing t = 0), the escape
question closes negatively for this rule and profile family. This is a
first-class result.

## Tasks

- **T0. Branch continuity at z₀** (decides the caveat).
  - For every t ∈ [5/16, 7/16], decide whether z₀ is a regular value: no
    critical value and no collision equal to z₀.
  - Count the right-movers at z₀ as a function of t.
  - Exact: discriminant in t, Sturm. Output: CONNECTED (no turning point on
    the incident branch) or TURNING_POINT_AT t*.
- **T1. Existence and unitarity of the S-matrix** for profiles constant
  outside a finite window.
  - Incoming amplitudes must determine the outgoing ones uniquely. This needs
    an exactly certified nonsingular matching matrix at the chosen z, which
    also excludes bound states.
  - Unitarity in the unit-flux basis of C5, from M^H G M = G.
  - Consistency check: Tarasinski's count predicts at least 2 perfectly
    transmitted left-moving channels, exterior to interior.
- **T2. Sharp limit L → 0⁺.** The profile is 5/16 for x < 0, 3/8 at x = 0 and
  7/16 for x > 0, a finite product of transfer matrices. Compute t at z₀
  exactly (algebraic, or a rational interval enclosure) and decide t ≠ 0.
- **T3. Finite L: out of scope** (user Q3). It needs a new charter.
- **T4. Horizon arc** (in scope, user Q1). At z₁ = (2499 + 100i)/2501, where
  0 < arg z₁ < arg z_c*, for the sharp profile of T2:
  - use the 2-incident-channel interior;
  - compute T1 there (existence and unitarity);
  - compute the 2 × 1 block, from the two interior right-movers to the
    exterior right-mover, and its singular value;
  - decide whether it is nonzero.

## Admission criteria

- Exact algebra, or rational interval arithmetic, for every certified number.
  Floating point only for orientation, labelled as such.
- A permanent verifier in `scripts/`, committed before its recorded run.
  Failed runs are retained. The reviewed verifiers are imported read-only,
  with SHA256 checks.
- Every claim at a named profile, L, N and z. No extrapolation in L or z
  without proof.

## Verdicts (per profile and z)

- `TRANSMISSION_NONZERO_CERTIFIED`: an enclosure of T excludes 0. If T0 gave
  CONNECTED, the report states that this is adiabatic continuity and not
  horizon crossing.
- `TRANSMISSION_ZERO_PROVED`: t = 0 exactly, with the structural reason.
- `S_MATRIX_NOT_ESTABLISHED`: the matching matrix is singular at z (a bound
  state or threshold). Retry only at points predeclared in Q2.
- `OPEN_AFTER_TRANSMISSION_ANALYSIS`: otherwise, with the open obligation.

## Not claimed (in any case)

- A Hawking or thermal statement, or a physical horizon.
- Anything about the tanh profile at finite L (only its sharp limit L → 0⁺ is treated).
- Anything outside the declared z.
- Novelty (OPEN).

## User decisions (2026-11-26)

- **Q1 = (b):** T0–T4, except T3 (see Q3).
- **Q2:** z₀ = (3+4i)/5 and z₁ = (2499 + 100i)/2501, as proposed, with no
  objection.
- **Q3:** the sharp limit only (T2, and T4 at the sharp profile). Finite L
  and tail bounds are out of scope.
- **Q4:** independent review by Astra 6.2 (`gpt-6.2-astra`).

## Original questions as posed

- **Q1. Scope.**
  - (a) I only: T0–T3.
  - (b) I plus the horizon arc: T0–T4.

  Recommendation: (b). The caveat suggests that I alone may not address the
  horizon.
- **Q2. Points.** z₀ = (3+4i)/5 on I. For the horizon arc,
  z₁ = (2499 + 100i)/2501, already certified to lie in (0, arg z_c*) with
  regular counts.
- **Q3. Profiles.**
  - T2, sharp limit: recommended.
  - T3: which L (for example L = 1, 4, 16) and truncation N.
  - The rigorous tail bound: yes or no. No means the result is stated for the
    truncated profiles.
- **Q4. Review** after execution: model or models.
