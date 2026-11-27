# Dispersive-horizon transmission: execution of T0–T4 (sharp profile)

Date: 2026-11-26. Branch: `research/dispersive-horizon-channels`.

| Item | Reference |
| --- | --- |
| Charter | `theory/DISPERSIVE_HORIZON_TRANSMISSION_GATE.md`, frozen at `8eb8be5` |
| Verifier | `scripts/verify_dispersive_horizon_transmission.py`, SHA256 `29ee9f12…316ea`, commit `0959251` (before its recorded run) |
| Run 1 (interrupted) | `reports/2026-11-26--dispersive-horizon-transmission-run-1.txt`, verifier `5f0cea2`. The fully symbolic closure-row test exhausted memory (about 11 GB after about 15 min). It was stopped and the log kept. |
| Run 2 (recorded) | `reports/2026-11-26--dispersive-horizon-transmission-run-2.txt`: 33/33 after 61/61 and 53/53; exit 0; about 25 min; Python 3.12.3, SymPy 1.14.0 |

**Author verdicts (PRELIMINARY; independent review pending; not promoted).**
- z₀ = (3+4i)/5: `TRANSMISSION_NONZERO_CERTIFIED`, T0 = CONNECTED.
- z₁ = (2499+100i)/2501: `TRANSMISSION_NONZERO_CERTIFIED`.

Both are for the sharp profile only. NOVELTY = OPEN.

**[A1] Review and Amendment 1 (2026-11-27).** Astra 6.2 returned
REPAIR_REQUIRED (`reports/2026-11-27--dispersive-horizon-transmission-astra-review.md`).
Points 1–5 are PASS: both verdicts and T0 = CONNECTED stand. Points 6–7
asked for repairs to the z₁ interpretation and to the documentation. They
are applied below and marked [A1]. They are editorial and have not been
re-reviewed. The verifier is unchanged.

## Authorization and process

- **Authorization:** user «SI, LO AUTORIZO» (2026-11-26), meaning execute
  T0–T4 under the frozen charter. The charter's scope came from the user
  decisions «lo segundo, limite brusco y revision por Astra 6.2».
- **Order of work:** the verifier was committed before each run.
  - Run 1 was interrupted during one check.
  - That check was replaced by a weaker exact test (see "Process deviation").
  - The verifier was recommitted, then run 2 was recorded.
- **No development runs.** Only `py_compile` syntax checks were made before
  each commit.

**Profile.** t(x) = 5/16 for x < 0, 3/8 at x = 0, 7/16 for x > 0. This is
the L → 0⁺ limit of t_L = 3/8 + tanh(x/L)/16, since t_L(0) = 3/8 for every L.
- M_x uses the coins at x and the sixth coin at x + 1, so M_x is homogeneous
  for x ≤ −2 and x ≥ 1.
- Y_1 = M_0 M_{−1} Y_{−1}.

## Method (what is certified, and how)

- **Exact identities** (verifier S), homogeneous medium, with cos θ and sin θ
  rationally parametrized:
  - P(λ, z) = λ⁵ det(U(λ) − z);
  - the Bloch vector Y(λ) built by stages satisfies rows 1–10 of
    (M − λ)Y = 0 identically.
- **Closure rows 0 and 11.** They vanish modulo det(U − z) at 9 exact sample
  points (w, λ), with z symbolic.
  - *Written step:* in general, Y is an eigenvector because a Bloch solution
    of Uψ = zψ is an orbit of M. This is the bijection certified by the
    reviewed matrix verifier, T2.
  - The sample check, and an interval residual M Y − λY ∋ 0 at every root,
    are consistency checks.
  - [A1] What the **program** checks for rows 0 and 11 is only the 9 sample
    specializations. The general statement is a written argument. The
    stage variables of a Bloch solution are
    Y_x = λ^x(a₁,…,a₆, b₁/λ,…,b₆/λ)ᵀ. They satisfy the stage and closure
    equations whose unique solution is Y_{x+1} = M Y_x (reviewed T2), and
    also Y_{x+1} = λY_x. This covers evanescent modes too. (The argument is
    the reviewer's; the author checked it against the reviewed T2 bijection.)
    The verifier header does not make this distinction, and its bytes are
    left as reviewed.
- **Roots.** In each medium and at each z, the 12 roots of P(·, z) are
  certified in pairwise disjoint boxes of radius 10⁻⁵⁰ by a complex Krawczyk
  test. Numpy and mpmath only supply the guesses. The boxes are classified as
  |λ| < 1, |λ| > 1 or on the circle, against the exact Sturm count.
- **Normalization.** Propagating modes are normalized to |Y^H G Y| = 1. The
  sign of the flux is the direction: + means right-moving.
- **Matching.** The unknowns are:
  - interior outgoing (left-movers) plus interior evanescent with |μ| > 1;
  - exterior outgoing (right-movers) plus exterior evanescent with |ν| < 1.

  The 12 × 12 matching matrix is certified invertible by
  ‖I − RA‖_∞ ≤ 10⁻⁶ < 1. R is a floating-point preconditioner, used only as a
  guess; the bound is exact interval arithmetic. The solution is enclosed by
  the standard residual bound.
- **Unitarity.** It follows from flux conservation (C1, reviewed): written
  argument with a certified ingredient. It is checked as S^H S ∋ I, with
  width < 10⁻²⁰.

## T0. Branch continuity at z₀: CONNECTED

- The leading coefficient in τ of H_A(τ) at z₀ is 8/5, constant in A.
- The discriminant of H_A in τ has degree 28 in A and **no root** in
  [A(5/16), A(7/16)] = [−15/128, −7/128].

So z₀ is a regular value of every intermediate medium t ∈ [5/16, 7/16].

*Written step:* the propagating roots stay simple and move continuously, and
their velocities stay nonzero. The unique interior right-mover (k ≈ 1.231)
therefore continues, with no turning point, into the unique exterior
right-mover (k ≈ 1.107).

## T1. Existence and unitarity

At both points, the following are certified:
- the matching matrix is invertible, so the S-matrix exists and there is no
  bound state;
- S^H S encloses I (4 × 4 at z₀, 5 × 5 at z₁).

At z₀, tr(t′^H t′) − 2 − T encloses 0. This is Tarasinski's count: the 1 × 3
block r′ forces at least two perfectly transmitted left-moving channels,
exterior to interior.

## T2. z₀ = (3+4i)/5 (window I)

- [A1] t ∈ [−0.67825096333601940651, −0.67825096333601940650]
  + i [−0.73191185779097809583, −0.73191185779097809582] (run-2 log).
- **T = |t|² ∈ [0.99571933684127928475, 0.99571933684127928476].**

Verdict: `TRANSMISSION_NONZERO_CERTIFIED`, sharp profile.

**Interpretation.** Together with T0 = CONNECTED, this is the transparent-band
case. The incident high-wavenumber branch passes from one medium to the other
without a turning point, and even a sharp step reflects only 0.43 %.
[A1] "Continuity" is proved for the family of homogeneous media
t ∈ [5/16, 7/16]; the certified T is that of the sharp step. It says
nothing about the horizon. The low-k branch, whose velocity changes sign at
t = 3/8, is not involved at z₀.

## T4. z₁ = (2499+100i)/2501 (horizon arc, 0 < arg z₁ < arg z_c*)

**Propagating modes.** Values of k = −arg λ are orientation only, read from
the certified boxes.

[A1] Channels by medium. The flux sign is certified; λ is the centre of the
logged box (width 10⁻¹²); k = −arg λ is orientation only. "Sheet" is the
sign of Im(z₁λ̄), explained below; it is given only for |k| < π/2.

| Medium | λ (centre) | k ≈ | Flux | Im(z₁λ̄) |
| --- | --- | --- | --- | --- |
| interior 5/16 | 0.8278 − 0.5611i | 0.596 | + | |
| interior 5/16 | 0.8889 + 0.4580i | −0.476 | + | |
| interior 5/16 | 0.99965 + 0.02662i | −0.027 | − | + |
| interior 5/16 | 0.99655 + 0.08304i | −0.083 | − | − |
| interior 5/16 | −0.3845 − 0.9231i, −0.4040 + 0.9147i | ≈ ±2 | − | |
| exterior 7/16 | 0.99684 − 0.07949i | 0.080 | + | + |
| exterior 7/16 | 0.99987 + 0.01600i | −0.016 | − | |
| exterior 7/16 | −0.4582 + 0.8888i, −0.4365 − 0.8997i | ≈ ±2 | − | |

[A1] **Sheet argument** (written; suggested by the reviewer, signs computed
by hand by the author from the logged boxes).
- Near k = 0 the sheet with slope −1 + 2(4t − 1) is
  ω = −k + 2 sgn(k) E(k), where E = arccos f and E ≈ (4t − 1)|k| (author
  remark of the transmission charter).
- On that sheet, ω + k = 2 sgn(k) E with 0 < E < π/2, so
  sgn sin(ω₁ + k) = sgn k. Also sin(ω₁ + k) = Im(z₁λ̄), because λ = e^{−ik}.
- Exterior k ≈ 0.080: sign + = sgn k, so the mode is on the sheet. With
  t = 7/16 the sheet velocity at k → 0 is +1/2, which matches its + flux.
- Interior k ≈ −0.083: sign − = sgn k, so the mode is on the sheet. With
  t = 5/16 the sheet velocity at k → 0 is −1/2, which matches its − flux.
- Interior k ≈ −0.027: sign +, while sgn k is −, so the mode is on the
  other sheet.
- The margins are about 0.04 and 0.01, far above the box widths.

So the low-k sheet whose velocity changes sign at t = 3/8 contains the
exterior right-mover k ≈ 0.080 and the interior left-mover k ≈ −0.083. The
original table placed "low-k branch" next to both −0.027 and −0.083; the
correct one is −0.083.

The two incident interior right-movers (k ≈ 0.596 and −0.476) are additional
propagating channels at finite k. Calling them lattice "doublers" is an
interpretation; it is not certified.

**Transmission into the exterior right-mover k ≈ 0.080.** [A1] The block is
the 1 × 2 row B = (t₁, t₂) of S, from the two interior right-movers.
- t₁ ∈ [0.68522716166118497943, 0.68522716166118497944]
  + i [−0.36571035127679135149, −0.36571035127679135148], so
  |t₁|² ∈ [0.60328032410923785982, 0.60328032410923785983];
- t₂ ∈ [−0.58832037108490174467, −0.58832037108490174466]
  + i [−0.10554696416869013529, −0.10554696416869013528], so
  |t₂|² ∈ [0.35726102067870325215, 0.35726102067870325216];
- **σ² = BBᴴ = |t₁|² + |t₂|² ∈ [0.96054134478794111197, 0.96054134478794111198].**
  The singular value σ of B is the positive square root.

Verdict: `TRANSMISSION_NONZERO_CERTIFIED`, sharp profile, for the block B.

**Interpretation.** [A1, replaces the original text]
- σ² ≈ 0.96054 is the **maximal** flux transmitted into the exterior
  right-mover k ≈ 0.080 from a unit-flux superposition of the two interior
  right-movers, reached at incidence ∝ Bᴴ. Incidence ∝ (t₂, −t₁)ᵀ transmits
  **zero**. So the transmitted fraction depends on the interior state.
- By unitarity of the row, σ² is also the interior weight of that row, and
  1 − σ² ≈ 0.0395 its exterior weight. Read as "96 % of the outgoing flux in
  that mode comes from the interior", this holds only for an incoherent
  preparation with equal flux in every incoming channel.
- What is certified is this scattering block for the sharp profile at z₁.
  The rest is interpretation: that the exterior mode "carries the horizon"
  (supported by the sheet argument above), and that the incident channels
  are "doublers".
- The qualitative picture (partial transmission and leakage through extra
  lattice channels) matches what Sabsovich et al. (2106.14553) and Maertens
  et al. (2204.06583) report for other lattice models. It is an analogy, not
  a comparison of numbers.

## Answer to the user's question, within scope

For the sharp profile, at two exact quasienergies, the rule connects interior
and exterior propagating modes with conserved flux, through a certified
unitary S-matrix.
- **z₀:** the incident branch continues within the family of homogeneous
  media (T0); the sharp step transmits T ≈ 0.996.
- **z₁ (horizon arc):** [A1] a suitable unit-flux superposition of the two
  interior right-movers sends up to σ² ≈ 0.961 of its flux into the exterior
  right-mover on the low-k sheet, whose velocity sign flips across t = 3/8.
  Another superposition sends none.

## Process deviation

- Run 1 was interrupted, and its log is kept.
- The symbolic divisibility test of the closure rows was replaced by a test
  at 9 exact sample points. This is weaker than what run 1 attempted. The
  general statement rests on the reviewed bijection (written step).
- [A1] The reviewer judges that the written step covers the mathematical
  obligation and that the substitution does not change either verdict.
  The decision lines of run 2 must be read: the program can also record an
  `OPEN` outcome through `ok(…, True)`. In run 2 both decision lines say
  `TRANSMISSION_NONZERO_CERTIFIED`.

## Not claimed

- Anything at finite L, or for the smooth tanh profile. In particular, the
  adiabatic limit L → ∞, where z₁-type transmission might be exponentially
  suppressed (cf. X = 1/(1 + e^{2πω/α}) in Sabsovich et al.).
- Anything at other quasienergies.
- A Hawking, thermal or physical-horizon statement.
- Novelty: OPEN. The mechanism is known from tight-binding and Floquet
  analogues (`investigaciones/2026-11-26-dispersive-horizon-prior-art/comprobacion.md`).
- Anything about many-body, interacting or quantum-field versions.

## Next steps (each needs user authorization)

1. Independent review by Astra 6.2 (fixed by the charter; sending needs the
   go-ahead).
2. A finite-L charter (T3), the one that bears on horizon physics proper.
