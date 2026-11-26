# Dispersive-horizon asymptotic channels: execution of C1–C5

Date: 2026-11-26. Branch: `research/dispersive-horizon-channels`.

| Item | Reference |
| --- | --- |
| Charter | `theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md`, frozen at `7a63529` |
| Verifier | `scripts/verify_dispersive_horizon_channels.py`, committed at `a5b9be3` before the recorded execution; SHA256 `08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc` |
| Recorded run | `reports/2026-11-26--dispersive-horizon-channels-run.txt`: 53/53 channel checks, after the 61/61 reviewed transfer-matrix checks; exit 0; Python 3.12.3, SymPy 1.14.0 |
| Review | `reports/2026-11-26--dispersive-horizon-channels-astra-review.md`: `gpt-6.2-astra` REPAIR_REQUIRED (missing charter deliverables; no claim refuted) |
| [A1] Amendment 1 verifier | `scripts/verify_dispersive_horizon_channels_amendment1.py`, committed at `ea3067a` before its recorded run; SHA256 `37aacbb5a3680fa3de3c74660b2fccfcd507e7b04c7f91b1b2b105c3416ebdd6` |
| [A1] Recorded run | `reports/2026-11-26--dispersive-horizon-channels-amendment1-run.txt`: 63/63, after 61/61 and 53/53; exit 0; first and only run |
| [A1] Review | `reports/2026-11-26--dispersive-horizon-channels-amendment1-astra-review.md`: `gpt-6.2-astra` PASS; editorial corrections applied |

**Author verdict: `CHANNELS_CLASSIFIED` (PRELIMINARY; not promoted).**
TRANSMISSION = OPEN. NOVELTY = OPEN.

**[A1] Amendment 1 (2026-11-26).** The Astra review found that the report did
not deliver everything the charter requires:
- the C2 count between thresholds;
- the per-root outputs of C3–C5;
- assertions of the published values and of the imported hashes.

As first delivered, the state was therefore `OPEN_AFTER_CHANNEL_ANALYSIS`.
Amendment 1 supplies these items, marked [A1] below, with a new verifier. The
verifier was committed before its only recorded run, and the earlier
verifiers' bytes are unchanged. After Amendment 1 the author candidate is
again `CHANNELS_CLASSIFIED`. Astra (`gpt-6.2-astra`) reviewed Amendment 1:
PASS, with editorial corrections that are applied.

## Authorization and process

- **Authorization:** user «autorizo las dos cosas» (2026-11-26), meaning push
  the research branch and execute C1–C5.
- **Order of work:**
  1. a numerical inspection of the band landscape, used for orientation only,
     with nothing retained;
  2. one development run of the verifier, which passed;
  3. the verifier commit `a5b9be3`;
  4. the recorded execution.
- **Deviation:** the charter asks for the verifier to be committed before
  execution. The development run preceded the commit and is disclosed here.
  No run failed.

**Conventions,** as in the charter:

- U = L₋W² with W = S C(θ) S C(θ) S C(−2θ);
- z = e^{iω}, λ = e^{−ik}, v = ∂ₖΩ;
- interior t = 5/16 as x → −∞, exterior t = 7/16 as x → +∞;
- A = t(2t − 1), f = A cos 3k + (1 − A) cos k = g(cos k), with
  g(C) = 4AC³ + (1 − 4A)C.

## C1. Flux form: ESTABLISHED (author; verifier C1)

The probability crossing the cut between x and x+1 during one period, summed
over the six conditional shifts and L₋, is conserved for every solution of
Uψ = zψ with |z| = 1. The reason is that each site's population returns to
itself (|zψ|² = |ψ|²) and the coins conserve probability locally.

In transfer variables the cut flux is Y_x^H G_x Y_x with

G_x = M_x^H D M_x − E₇₇,  D = diag(0,1,1,1,1,1,−1,−1,−1,−1,−1,−1).

The verifier checks:

- **Identity.** M_x^H G_{x+1} M_x = G_x for general independent angles at
  x, x+1, x+2 and |z| = 1, decided exactly modulo c² + s² = 1.
- **Hermitian.** G_x is Hermitian.
- **Second route.** On two exact solutions with site-dependent rational
  coins, the operational flux read off the word of U is constant in x and
  equals Y^H G Y. The check covers all four sesquilinear pairings and every
  interior site.
- **Determinant.** In a homogeneous medium, det G = −cot²θ (−5/11 and −7/9
  in the two media), so the form is nondegenerate.

Consistency with det M_x = cot θ_x / cot θ_{x+1}: det G_x = |det M_x|² det
G_{x+1} reproduces −cot²θ_x by telescoping.

**[A1] det G_x = −cot²β₆(x) for a varying profile.**
- **Proof** (Astra's written argument, checked by hand). The unitarity of the
  first five coins rewrites the cut flux as
  Σ_{j≤5}|a_j(x)|² − Σ_{j≤6}|b_j(x−1)|² − |(c₆a₆ − za₁)/s₆|².
  Changing a₆ for the last modulus argument has a determinant of modulus
  |cot β₆(x)|. The resulting diagonal form has signature (5, 7).
- **Check.** Verifier G confirms it exactly on the rational site-dependent
  profile of C1 at six sites.

## C2. Root structure: ESTABLISHED (verifier C2), winding remark proved

- **Symmetry.** λ¹² P(1/λ, 1/z) = z⁻² P(λ, z). For |z| = 1 the twelve roots
  are therefore closed under λ ↦ 1/λ̄, and roots off the circle come in
  pairs, inside and outside.
- **Reduction to one real function.** P = zλ⁶Φ, and on the circle
  Φ = −2h(k) with h = 2f² − 1 − cos(ω + k). Hence the roots on the circle,
  with their multiplicities, are the real zeros of h.
- **Winding.** Ω₊ + Ω₋ = −2k, because det U(k) = e^{−2ik}. At every regular
  ω, the signed count of propagating roots, Σ sign(v), equals the degree of
  k ↦ det U(k), which is −2. So #right − #left = −2 in every medium and at
  every regular ω. This was the author remark of the charter; it is now a
  written argument, checked against the counts in C4.

**[A1] Count between thresholds.** The charter asks for the count of roots on
the circle as a function of ω between thresholds.
- **Cuts.** The circle is cut by the four interior critical values
  {z_c*, z̄_c*, −z_c*, −z̄_c*} (the set is closed under conjugation and
  negation; verifier Z) and by the collision points ±1, ±i. That gives eight
  arcs.
- **Sampling.** Verifier K counts at one exact rational point in each arc, in
  both media, and checks that each point is regular. The points are
  (2499 + 100i)/2501, of argument 2 atan(1/50) < arg z_c*, and z₀, together
  with their images under conjugation and negation.

With δ = arg z_c* and d_π(ω) = dist(ω, πℤ), at regular levels only (the rows exclude the
collision points ±1, ±i and the critical values) [A1, editorial after review]:

| Medium and arc | Propagating | Right (v > 0) | Left (v < 0) |
| --- | ---: | ---: | ---: |
| interior, 0 < d_π(ω) < δ | 6 | 2 | 4 |
| interior, d_π(ω) > δ | 4 | 1 | 3 |
| exterior, every regular arc | 4 | 1 | 3 |

This confirms Astra's table.
- **Within each arc** the count is constant: this is the written argument of
  C4, applied per arc.
- **Across a collision point** the count is unchanged. The two crossing
  branches have nonzero slopes −1 ± 2(4t − 1) at z = ±1 and −1 ± 2(1 − 4A)
  at z = ±i (verifier K). The equal counts on both sides of each collision
  point confirm this.
- **Across the interior critical values** two propagating roots appear or
  disappear, one moving each way. This is the fold at the band maximum δ.

The window rule of the charter selects the arc (δ, π/2). Below δ the interior
has two right-movers, so the uniqueness of the incident channel holds on I
and not near ω ≡ 0 (mod π).

## C3. Thresholds and window: ESTABLISHED (verifier C3, written step noted)

**Where two propagating roots can collide.** A double root on the circle
needs h = ∂ₖh = 0.

- If ∂_ω h = sin(ω + k) ≠ 0, then v = 0, and eliminating ω gives
  f²(4f′² − (1 − f²)) = 0 (an identity checked by the verifier).
- If sin(ω + k) = 0, then f ∈ {0, ±1}, the collision points.
- On the profile A < 0, so g(C) = C(1 − 4A(1 − C²)) vanishes only at
  C = 0, and g′ ≥ (4t − 1)² > 0 makes f = ±1 occur only at k = 0, π.
- The collision points are therefore z ∈ {1, i, −1, −i}. They are band
  crossings and nodes, not critical values.

**Critical values.** These are the k with 4f′² = 1 − f² and f ≠ 0. In
u = cos²k the threshold polynomial is (u − 1) × a quadratic. Its root u = 1
corresponds to the nodes and is not critical, since v ≠ 0 there for
t ≠ 3/8.

- **Interior.** The quadratic is proportional to 2625u² − 5245u + 2604. It
  has exactly one root in (0, 1) (Sturm count),
  u* = (5245 − √168025)/5250.
  - This gives four critical points (cos k = ±√u*, sin k = ±√(1 − u*)).
  - Their critical values are
    z_c = e^{−ik}(2f² − 1 − 4iff′), with f′ = −sin k · g′(cos k).
- **Exterior.** The quadratic has no root in [0, 1], so there are no
  critical values at t = 7/16. Its only root on [0, 1] is u = 1, the nodes.

**Window.** Rational interval arithmetic (200-bit integer square roots, no
floating point) shows the following.

- Exactly one interior critical value lies in the open first quadrant. It is
  z_c*, with cos k = +√u* and sin k = −√(1 − u*).
- The other three have Im < 0 or Re < 0.
- Re z_c* is the algebraic number with minimal polynomial
  316240512000000000X⁴ − 664624285099139500X² + 348107462168643891,
  certified inside one isolating interval.
- Re z_c* > 3/5 = Re z₀.

Hence I = (arg z_c*, π/2) is nonempty and contains z₀ = (3+4i)/5. It also
excludes all four collision points. For orientation only (a numerical value,
not a certified quantity): arg z_c* ≈ 0.0894 and arg z₀ ≈ 0.9273.

**[A1] Certified enclosures** (verifier Z; printed outward-rounded):

z_c* ∈ [0.996006471094483079484232973570, 0.996006471094483079484232973571]
+ i [0.089281070434413149785007027183, 0.089281070434413149785007027184].

The other three critical values are z̄_c* and −z_c*, −z̄_c*, each with the
corresponding enclosure. The four enclosures are disjoint.

Verifier V checks the following:
- z_c* lies in the coarse box (9/10, 1) × (1/20, 1/8), given by Astra by hand;
- the primitive minimal polynomial computed equals the quartic printed
  above;
- the exterior quotient is proportional to 343u² − 1211u + 1012.

The charter glosses C_t as "the quasienergies at which two roots on the
unit circle collide". That gloss would also include the collision points.
Since none of them lies in (arg z_c*, π/2), the two readings give the same I.

## C4. Classification on I: ESTABLISHED at z₀; constancy on I by written argument

At z₀, in each medium, the verifier certifies:

- P(·, z₀) has degree 12, P(0) ≠ 0, and is squarefree. So the twelve roots
  are distinct and M_hom(z₀) is diagonalizable.
- With τ = tan(k/2), H(τ) = (1 + τ²)⁶ h has degree 12, so there is no root
  at k = π. It is squarefree, and gcd(H, N) = 1, where N is the
  group-velocity numerator. So there is no zero velocity and no collision at
  z₀.
- The real roots of H are counted by Sturm. The sign of
  v = −(4ff′ + sin(ω + k))/sin(ω + k) at each root is decided exactly, by
  isolating it away from the roots of N.

| Medium | Propagating | Right-moving (v > 0) | Left-moving (v < 0) | Evanescent, \|λ\| < 1 (decays as x → +∞) | Evanescent, \|λ\| > 1 (decays as x → −∞) |
| --- | --- | --- | --- | --- | --- |
| interior t = 5/16 | 4 | **1** | 3 | 4 | 4 |
| exterior t = 7/16 | 4 | **1** | 3 | 4 | 4 |

Numerically, for orientation only: the interior right-mover is at k ≈ 1.231
with v ≈ 1.81, the exterior one at k ≈ 1.107 with v ≈ 1.29. These are the
high-wavenumber Ω₊ branches of report §5.

**[A1] Every root at z₀** (verifier E). Each medium has 24 isolating
rational boxes, of width below 10⁻²⁵, for the roots of
P(·, z₀)P(·, z̄₀) ∈ ℚ[λ]. Each box is assigned to exactly one factor by
exact interval evaluation, and 12 belong to P(·, z₀).
- 4 lie inside the unit disk and 4 outside. For each inside box, the
  enclosure of its image under 1/λ̄ meets exactly one outside box. By the
  C2 symmetry, that box contains the partner root.
- 4 lie on the circle and are matched one-to-one with the Sturm roots.
- The signs of v in increasing k are −, −, +, − in both media, as Astra
  derived by hand.
- The mode Y ∝ λ^x decays as x → +∞ when |λ| < 1.

Values rounded to 3 decimals; the 12-digit enclosures are in the run log. The k values, k = 2 atan τ, are for orientation only:

| Medium | \|λ\| < 1 (decays as x → +∞) | \|λ\| > 1 (decays as x → −∞) | \|λ\| = 1 (propagating, increasing k; v sign) |
| --- | --- | --- | --- |
| interior | −0.344+0.065i, −0.275−0.027i, 0.257−0.011i, 0.475+0.124i | −3.600−0.359i, −2.805+0.533i, 1.970+0.513i, 3.881−0.160i | k ≈ −2.233 (−), −0.482 (−), 1.231 (+), 1.735 (−) |
| exterior | −0.239+0.047i, −0.198−0.021i, 0.187−0.008i, 0.306+0.068i | −4.985−0.539i, −4.029+0.793i, 3.114+0.695i, 5.334−0.241i | k ≈ −2.326 (−), −0.363 (−), 1.107 (+), 1.758 (−) |

**Constancy on I** (written argument). On I there is no critical value (C3)
and no collision point, so h has only simple real zeros. By the implicit
function theorem these zeros move continuously, with v continuous and
nonzero. By the 1/λ̄ symmetry a root can leave the circle only through a
double root on the circle, which is excluded. So the counts and signs at z₀
hold on all of I.

**Full-line channel count.**

- Incoming: interior right-movers (1) plus exterior left-movers (3), a total
  of 4.
- Outgoing: exterior right-movers (1) plus interior left-movers (3), a total
  of 4.

The counts are equal, as flux conservation requires.

## C5. Normalization: ESTABLISHED (verifier C5, with the written steps marked)

**Each propagating root.** Take the Bloch eigenvector: a kernel vector v of
U(k) − z₀, with stages q_{j+1} = S(k)C(β_j)q_j and Y = (a_j, b_j/λ). Exact
rational interval arithmetic on a 10⁻⁴⁵-wide isolating interval of the root
shows:

- F = Y^H G Y ≠ 0, and its sign is that of the group velocity, at all 8
  propagating roots;
- Im F is enclosed around 0;
- F/(v‖q₁‖²) is enclosed around 1 with width below 10⁻²⁰.

So N = Y/√|F| satisfies N^H G N = sign(v) = ±1. The enclosure of F is the
certified normalization factor.

**[A1] Per-mode normalization** (verifier N).
- **Inputs.** For each propagating root the run log records the τ interval
  (refined internally to tolerance 10⁻⁴⁵, printed outward-rounded to 20
  decimals), the sign of v, and the kernel row of U(k) − z₀ used. In
  all eight modes it is row 1, (U₁₂, z₀ − U₁₁).
- **Outputs.** It records enclosures of F, of 1/√|F|, and of the twelve
  components of N.
- **Checks.** The real part of N^H G N encloses sign(v), with width
  < 10⁻¹⁰, and its imaginary part encloses 0. F coincides with the C5
  computation re-run in the same import.

Values rounded to 6 significant digits:

| Medium | mode (increasing k) | sign v | F = Y^H G Y | 1/√\|F\| |
| --- | --- | --- | --- | --- |
| interior | 1 | − | −8.03313 | 0.352823 |
| interior | 2 | − | −0.952931 | 1.02440 |
| interior | 3 | + | 1.63931 | 0.781032 |
| interior | 4 | − | −2.27711 | 0.662686 |
| exterior | 1 | − | −6.08619 | 0.405347 |
| exterior | 2 | − | −1.38571 | 0.849500 |
| exterior | 3 | + | 1.88320 | 0.728706 |
| exterior | 4 | − | −1.47908 | 0.822252 |

F depends on the choice of kernel vector; the normalized N does so only up to
a phase.

**Exact identity F = (∂ₖΩ)‖q₁‖²** (written argument with a certified
ingredient).

- For a Bloch vector, Y^H G Y equals Σ_j (|(C q_j)↑|² − |(C q_j)↓|²) −
  ‖q₁‖². This is the stage form of G, obtained by direct expansion.
- The verifier certifies −iU^H ∂ₖU = Σ_j R_j^H σ_z R_j − I, with R_j the
  partial products.
- Hellmann–Feynman gives ∂ₖΩ‖v‖² = v^H(−iU^H ∂ₖU)v. Hence F = (∂ₖΩ)‖q₁‖²
  exactly.

The interval ratio is a consistency check of this identity at the 8 roots,
not its proof.

**Evanescent modes** (written argument). From C1, Y_μ^H G Y_ν =
μ̄ν Y_μ^H G Y_ν, so Y_μ^H G Y_ν = 0 unless μ̄ν = 1.

- The twelve eigenvectors form a basis, because the eigenvalues are
  distinct.
- G is nondegenerate.
- So each evanescent mode pairs nontrivially only with its mirror 1/μ̄.
  Evanescent modes carry no flux individually; flux appears only in
  cross-terms between mirror pairs.

## Verdict

**`CHANNELS_CLASSIFIED`** (author PRELIMINARY):

- C1–C5 succeed;
- I = (arg z_c*, π/2) is nonempty;
- on I the interior has exactly one right-moving propagating channel, so
  `INCIDENT_CHANNEL_NOT_UNIQUE` does not apply;
- the exterior has one right-moving channel.

Neither stop rule fires.

The full-line scattering problem on I has 4 incoming and 4 outgoing
channels. The candidate incident channel, the interior right-mover, is
unique. The candidate transmitted channel, the exterior right-mover, is
unique. Three left-moving channels in each medium are also open.

## Not claimed

- 𝒯_L > 0, or any statement about the coupling between channels across the
  profile.
- Existence or uniqueness of the scattering matrix for the tanh profile, or
  Jost-type asymptotics.
- [A1] Outside I, only the C2 counts per arc and the threshold enclosures are
  claimed. Not claimed there: the classification, normalization or
  incident-channel uniqueness, or the Jordan structure at the thresholds z_c
  and at the collision points.
- Any statement about the intermediate frozen media 5/16 < t < 7/16. They
  include the horizon t = 3/8, where (±1, ±1) are quadruple roots (audit
  A1/A2).
- A physical horizon or Hawking statement.
- Novelty.

The user's question (does the rule connect interior and exterior modes
dynamically, with conserved flux) is now posed on a defined 4 × 4 channel
space with a certified flux form. Answering it is the task of a separate
transmission charter.

## Next steps (each needs user authorization)

1. Promotion of `CHANNELS_CLASSIFIED` (user decision).
2. A transmission charter on I.
