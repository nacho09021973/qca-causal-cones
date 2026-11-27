# Dispersive-horizon asymptotic channels gate

2026-11-26. Author: Claude Code (Claude Opus 5.5). Initial status **OPEN**.
Frozen by the commit that adds this file on branch
`research/dispersive-horizon-channels`, from `b1c6d75`, before any execution.

## Authorization and budget

User message, 2026-11-26: «Yo seguiría con un contrato acotado para clasificar
los canales asintóticos y normalizarlos por flujo … El siguiente paso que
autorizaría es redactar el contrato de canales, con la revisión de la Enmienda 2
como encargo separado.» That message authorized drafting.

User decision, 2026-11-26: «Autorizo conceptualmente Q-a, Q-b y Q-d, y Q-c con
la modificación indicada», with the order «1. Congelar el contrato de canales.
2. Resolver C1–C5. 3. Revisar independientemente los resultados. 4. Solo
entonces abordar la transmisión». The modification and the branch were then
chosen explicitly: Q-c "Add uniqueness stop"; Q-b "New research branch". See
"User decisions" below.

Freezing is authorized. Each of the following still needs its own user
authorization:

- execution of C1–C5;
- independent review;
- promotion;
- any transmission charter.

The review of Amendment 2 is a separate brief. It is not part of this
contract.

**Scope note, for the user's decision before freezing.**
`PROJECT_INSTRUCTIONS.md` §1 frames the project as the coexistence question
(Thirring) plus inherited lines A and B∞*. This walk is a one-particle quantum
walk with an imposed spatial profile. It is not the homogeneous interacting
rule of the main objective (`README.md` at `8fd37a5` calls it a separate
exploratory line). `state/CURRENT_STATE.md` has no entry for it. Freezing this
charter therefore also means accepting it as a separately chartered
exploratory line, recorded in `CURRENT_STATE.md` on the branch where it is
frozen. The user accepted this (Q-a).

One contract. A balance is mandatory on closure. No further contract follows
automatically: transmission needs its own charter.

## Known, question, abandonment

**Known** (read or certified this session, with source):

- **Operator and conventions.** `reports/2026-11-26--dispersive-horizon-three-step-transfer.md`
  §2, §4 (`8e5b540`) defines:
  - U = L₋W² and W = S C(θ) S C(θ) S C(−2θ);
  - the profile t_L(x) = 3/8 + tanh(x/L)/16, so t → 5/16 as x → −∞
    (interior) and t → 7/16 as x → +∞ (exterior);
  - Floquet eigenvalue e^{iΩ}, v = ∂ₖΩ, λ = e^{−ik}.
- **Transfer matrix.** The 12×12 matrix M_x(z) of that report, §6, gives a
  linear bijection between solutions of Uψ = zψ on ℤ and orbits of M
  (audit `reports/2026-11-26--dispersive-horizon-transfer-matrix-audit.md`).
  - Its entries are PASS under Astra's review.
  - The audit is amended twice. Amendment 2 is not yet reviewed.
  - Certified by `verify_dispersive_horizon_transfer_matrix.py` T2/T3.
- **Determinant and characteristic polynomial** (T4, T5).
  - det M_x = cot θ_x / cot θ_{x+1}, z-free.
  - In a homogeneous medium, det(λ − M) · (−zA²) = z²λ⁵ − zλ⁶(4f² − 2) + λ⁷,
    with A = t(2t − 1).
- **Bands.** Ω_± = −k ± 2E with cos E = A cos 3k + (1 − A) cos k.
  - The outgoing infrared velocity is 8t − 3: −1/2 in the interior and
    +1/2 in the exterior.
  - v_UV,out(π/2) = 1 − 8A: 31/16 in the interior and 23/16 in the exterior.
  - Certified by T8.
- **Degenerate points on the profile values** (audit A1/A2; repairs verifier
  R2/R3; amendment-2 verifier G1–G4).
  - (z, λ) = (±1, ±1): multiplicity 2 and semisimple at t = 5/16 and
    t = 7/16; multiplicity 4, geometric multiplicity 2, at t = 3/8.
  - (z, λ) = (i, −i): double and semisimple at the three profile values
    (T6).
  - Ω₊ has exactly one zero-velocity point in (0, π/2) at t = 5/16 and none
    at t = 7/16 (G4).
- **Local branch** [author and AI arguments; partly certified]. Report §5,
  with Astra's written compactness step, argues for an ω* < π/2 near π/2
  and a nondegenerate branch k₊(t) with ∂ₖΩ₊ > 0 for all t on the profile.
  Only its ingredients are certified (T8): 0 ≤ f < 1 on (0, π/2] and
  v_UV > 0. Astra's argument is an AI argument, not a source.

**Not known:**

- the full root structure (all twelve λ) at fixed |z| = 1 in either limit;
- which roots are propagating or evanescent and in which direction;
- the conserved flux form of M_x;
- the threshold set (critical values of Ω_±) in either limit.

Author remark to be derived, not a premise [UNVERIFIED]: det U(k) = e^{−2ik},
so the windings of the bands sum to −2. At every regular ω this would force
#(propagating roots with v > 0) − #(with v < 0) = −2 in each medium.

**Question.** Fix the tanh profile and its two limits t = 5/16 (interior) and
t = 7/16 (exterior). Is the interval I declared below nonempty, and on I:

- does the interior medium have at least one propagating right-moving
  (v > 0) channel, the candidate incident channel, and
- does the exterior medium have at least one propagating right-moving
  channel, the candidate transmitted channel?

The full classification of all twelve roots in both media, with flux signs
and unit-flux normalization, is the deliverable either way.

**Abandonment of this route** (transmission through the declared window):
verdict `NO_COMMON_CHANNEL_INTERVAL` or `INCIDENT_CHANNEL_NOT_UNIQUE`. Neither
is a no-go for other windows, profiles or rules.

**Weakness of the falsifier, recorded before freezing.** Report §5 already
argues that a right-moving Ω₊ branch exists near π/2 in every medium of the
profile. `NO_COMMON_CHANNEL_INTERVAL` is therefore unlikely on I. For that
reason the user added a uniqueness stop (Q-c): `INCIDENT_CHANNEL_NOT_UNIQUE`.

## Frozen data

- **Rule:** U = L₋W² of report §2, §4, unchanged.
- **Media:** homogeneous t_int = 5/16 and t_ext = 7/16. The intermediate
  profile enters only through C1, the x-dependence of the flux form. The
  scattering problem is not posed here.
- **Variables:** z = e^{iω}, |z| = 1, λ = e^{−ik}, Y_x as in report §6.
- **Window.** Let C_t be the set of critical values of ω ↦ Ω_±(k; t) mod 2π.
  These are the quasienergies at which two roots λ on the unit circle
  collide. I is the connected component of
  S¹ \ (C_{5/16} ∪ C_{7/16} ∪ {π/2}) whose closure contains π/2 from below.
  - This fixes I before computing: no window is chosen after seeing results.
  - π/2 is excluded because the two bands cross there (z = i) in every
    medium.
  - If π/2 ∈ C_t, then I is the component adjacent to π/2 from below.

## Tasks

- **C1 (flux form).** Derive from the unitarity of U a sesquilinear form
  G_x (12×12, Hermitian) such that M_x(z)^† G_{x+1} M_x(z) = G_x for all
  |z| = 1 and all admissible site angles.
  - Physically, G_x is the probability current through the cut between x
    and x+1.
  - Verify it exactly for general independent angles.
  - Check consistency with |det M_x|.
  - Second route: on a homogeneous medium, the flux of a propagating Bloch
    mode must be proportional, with a fixed positive factor, to its group
    velocity ∂ₖΩ.
- **C2 (root structure).** For |z| = 1, show that the twelve roots are closed
  under λ ↦ 1/λ̄, or refute this.
  - Derive or refute the winding count of the author remark.
  - Count the roots on the unit circle as a function of ω between
    thresholds.
- **C3 (thresholds).** Compute C_{5/16} and C_{7/16} exactly, as algebraic
  numbers, including zero-velocity points such as the G4 edge.
  - Give certified rational enclosures. Floating point is not admitted as
    evidence.
  - Determine I exactly.
- **C4 (classification on I).** Root counts are constant on I. Certify them
  at one exact point z₀ ∈ I with rational coordinates on the unit circle,
  together with the exclusion of thresholds from I. In each medium, give:
  - every root λ, propagating (|λ| = 1, with the sign of v and of the flux)
    or evanescent (|λ| < 1 or > 1, with its decay direction);
  - the counts.
- **C5 (normalization).** For each propagating root, give the eigenvector
  of M_hom(z₀) normalized to Y^† G Y = ±1.
  - State the pairing of evanescent modes under G.
  - State the dimension of the incoming and outgoing channel spaces of the
    full-line problem: interior right-movers plus exterior left-movers in;
    exterior right-movers plus interior left-movers out. The two must be
    equal.

Any computation needs a permanent verifier in `scripts/`, committed before
execution. Failed runs are retained, and exact command entries go into
`.claude/settings.json`. The reviewed verifiers (transfer matrix, repairs,
amendment 2) are reused read-only.

## Verdicts

- `CHANNELS_CLASSIFIED`: C1–C5 succeed, I is nonempty, and on I the
  interior has exactly one right-mover and the exterior at least one
  right-mover. The counts and normalizations are recorded.
- `NO_COMMON_CHANNEL_INTERVAL`: I is empty, or on I one of the two media has
  no right-moving propagating root. This route is closed for this window.
- `INCIDENT_CHANNEL_NOT_UNIQUE`: I is nonempty and both media have at least
  one right-mover, but on I the interior has more than one right-moving
  propagating channel, so "the" incident channel is not unique. The
  classification and normalization (C1–C5) are still recorded. This route is
  closed for this window.
- `FLUX_FORM_NOT_ESTABLISHED`: C1 fails. Stop; no classification is claimed.
- `OPEN_AFTER_CHANNEL_ANALYSIS`: otherwise, with the open obligation stated.

All verdicts are author PRELIMINARY pending independent review, which needs
separate permission.

## Not claimed by any verdict

The following stay outside every verdict:

- existence or uniqueness of the scattering matrix for the tanh profile,
  Jost-type asymptotics, or the convergence rate of the profile;
- 𝒯_L > 0 or its L → ∞ limit;
- the Jordan structure at thresholds (outside I by construction);
- the interpretation of Floquet species;
- any physical horizon or Hawking statement;
- other windows, profiles or rules.

NOVELTY = OPEN. Transfer-matrix channel analysis for quantum walks is prior
art; see the references of report §8, read in the original before any
citation.

## Execution bound

One working session. No search over windows, profiles or parameters. Stop on
a proved verdict.

## User decisions (2026-11-26)

- **Q-a (scope):** accepted. This is a separately chartered exploratory line,
  recorded in `state/CURRENT_STATE.md` on `research/dispersive-horizon-channels`.
- **Q-b (branch):** new research branch `research/dispersive-horizon-channels`,
  from `review/dispersive-horizon-transfer-audit` at `b1c6d75`.
- **Q-c (stop rule):** keep `NO_COMMON_CHANNEL_INTERVAL` and add
  `INCIDENT_CHANNEL_NOT_UNIQUE` (more than one interior right-mover on I).
- **Q-d (window):** I as defined in "Frozen data", adjacent to π/2 from below.

The user's stated interest, recorded as motivation and not as a criterion:
whether the rule admits a dynamical connection between interior and exterior
modes compatible with a conserved flux. A positive interior group velocity is
a possibility of escape; a nonzero transmission amplitude would show that it
is realized. That second question belongs to a later transmission charter.

## Before freezing

No computation has been run for this contract. The facts under "Known" come
from the audited report and the three verifiers already in the repository.
