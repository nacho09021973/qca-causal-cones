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

- t ∈ −0.67825096333601940651 − 0.73191185779097809583 i (enclosure width
  10⁻²⁰).
- **T = |t|² ∈ [0.99571933684127928475, 0.99571933684127928476].**

Verdict: `TRANSMISSION_NONZERO_CERTIFIED`, sharp profile.

**Interpretation.** Together with T0 = CONNECTED, this is the transparent-band
case. The incident high-wavenumber branch passes from one medium to the other
without a turning point, and even a sharp step reflects only 0.43 %. It says
nothing about the horizon. The low-k branch, whose velocity changes sign at
t = 3/8, is not involved at z₀.

## T4. z₁ = (2499+100i)/2501 (horizon arc, 0 < arg z₁ < arg z_c*)

**Propagating modes.** Values of k = −arg λ are orientation only, read from
the certified boxes.

| Medium | Right-movers (flux +) | Left-movers (flux −) |
| --- | --- | --- |
| interior t = 5/16 | k ≈ 0.596, k ≈ −0.476 | k ≈ −0.027, −0.083 (low-k branch), and two with \|k\| ≈ 2 |
| exterior t = 7/16 | **k ≈ 0.080 (low-k branch)** | k ≈ −0.016, and two with \|k\| ≈ 2 |

The low-k branch moves left in the interior and right in the exterior, as the
author remark v(k → 0) = −1 + 2(4t − 1) predicts. That branch is the horizon.
The two interior right-movers are lattice "doublers" at finite k.

**Transmission into the exterior low-k right-mover:**
- t₁ ∈ 0.68522716166… − 0.36571035127… i, so |t₁|² ∈ [0.60328032410923785982, …983];
- t₂ ∈ −0.58832037108… − 0.10554696416… i, so |t₂|² ∈ [0.35726102067870325215, …216];
- **σ² = |t₁|² + |t₂|² ∈ [0.96054134478794111197, 0.96054134478794111198].**

Verdict: `TRANSMISSION_NONZERO_CERTIFIED`, sharp profile.

**Interpretation.**
- At z₁, 96.05 % of the outgoing flux in the exterior low-k right-mover comes
  from the two interior right-moving doublers. The remaining 3.95 % comes
  from exterior left-movers. This uses unitarity of that row of S.
- Flux from inside the horizon reaches the exterior through the mode that
  carries the horizon. The channel is lattice doublers scattering through the
  interface. This is the mechanism found numerically by Sabsovich et al.
  (2106.14553, attenuation) and Maertens et al. (2204.06583, local model,
  «leakage»).
- Here it is certified exactly, for this walk, at this point, for the sharp
  profile.

## Answer to the user's question, within scope

For the sharp profile, at two exact quasienergies, the rule connects interior
and exterior propagating modes with conserved flux, through a certified
unitary S-matrix.
- **z₀:** the connection is adiabatic continuity of one branch (T ≈ 0.996).
- **z₁ (horizon arc):** interior right-moving doublers feed the exterior
  low-k mode whose velocity sign flips across t = 3/8 (σ² ≈ 0.961).

## Process deviation

- Run 1 was interrupted, and its log is kept.
- The symbolic divisibility test of the closure rows was replaced by a test
  at 9 exact sample points. This is weaker than what run 1 attempted. The
  general statement rests on the reviewed bijection (written step).

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
