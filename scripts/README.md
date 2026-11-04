# Scripts

## Small fixed Gaussian profile algebra (2026-10-31)

`verify_small_gaussian_profile_algebra.py` accompanies the preregistered
[small Gaussian gate](../theory/H1_SMALL_GAUSSIAN_PROFILE_GATE.md) and its
[execution](../reports/2026-10-31--h1-small-gaussian-profile.md). It runs
21 exact SymPy 1.14.0 checks: Gaussian Fourier moments, resource L1
normalization, channel parity, one abstract noncommuting three-step
quadratic expansion with the single-coin contribution, positive Hessian
factorization, geometric moments and power bookkeeping. This is not a
lattice simulation or finite-N signal scan. The analytic kernel estimate,
general-N remainder and signal survival remain report proofs pending review;
the checks do not certify them. The corrected contract is pinned by SHA256.

```sh
/home/adnac/venvs/torch-gpu/bin/python -B scripts/verify_small_gaussian_profile_algebra.py
```

No scientific script was present at the initial freeze (`44ad178`).

## IR projection leakage algebra (2026-09-22)

`verify_ir_projection_leakage.py` checks exact algebra for the
[projection and conditioning derivation](../reports/2026-09-22--ir-projection-leakage-and-conditioning.md):
rank-two trace norm, conditioning correction, the four original encoders'
boundary coefficients, radial Fourier constants and the sharp-cutoff kernel.
Run `python3 -B scripts/verify_ir_projection_leakage.py` (SymPy 1.14.0).
Fourier/Poisson error estimates remain written, independently unreviewed
arguments; the script does not certify the asymptotics of the PP observable.

## Exact standard Weyl/Dirac battery

`verify_weyl_dirac_gate.py` implements the
[pre-execution contract](../reports/2026-09-14--weyl-dirac-gate-contract.md).
It checks seven standard symbols and their Dirac couplings using exact
SymPy arithmetic, with no scans or fitted tolerances.

Requirements: Python 3.12 and `sympy==1.14.0` (see `requirements.txt`).
Run from the repository root:

```sh
python3 scripts/verify_weyl_dirac_gate.py
python3 scripts/verify_weyl_dirac_gate.py --output reports/2026-09-14--weyl-dirac-verification.md
```

The first command prints the record. The second writes it only after all
checks pass; a failed check exits nonzero and does not replace any earlier
record. Check hashes before treating an existing record as current.

The retained script is the provenance for the generated comparison table.
Interval inequalities and continuum scaling are derived separately in the
[analytic report](../reports/2026-09-14--weyl-dirac-exact-gate.md).
Neither artifact changes the canonical project state automatically.

## Initial scope (historical)

The initial freeze required the first code to implement only the standard
Weyl/Dirac battery. That gate is now PASS for its declared cases.

Its tasks were:

- exact causal-body geometry from a declared neighbor set;
- support function / inradius calculation;
- symbolic or high-precision verification of Bloch eigenphases;
- low-`k` expansion with branch conventions made explicit;
- comparison table for `r_in`, Hamiltonian spatial coefficient, and `ω^2` coefficient.

## Directional causal saturation (2026-09-16)

`verify_directional_saturation.py` is the traced evidence for the
[directional saturation report](../reports/2026-09-16--directional-causal-saturation.md),
covering the two 3D walks of CJWW `sources/2408.02108v1.pdf`, Eqs. (5.12) and (5.15).
It is a verification of a chartered report, not a new gate calculation, and it
changes no canonical state.

Requirements: Python 3.12, `sympy==1.14.0` and `numpy==1.26.4`; numpy is
imported at module level (see `requirements.txt`). Run from the repository root:

```sh
python3 scripts/verify_directional_saturation.py
```

Fourteen of the fifteen checks are exact. The one numerical check — whether the
group-velocity sets fill the tricylinder and the ball — is tagged
`SUPPORTED (numerical)` in its own output and must not be cited as ESTABLISHED.
The script fails closed: any exception counts as a failed check and the exit
status is nonzero.

It also carries the four checks of the `LDP_RADIAL_INTERPRETATION` gate
([contract](../theory/OPERATIONAL_INVISIBILITY_GATE.md)): CJWW Eq. (5.21) at
their stated maximizer, its two slopes `1` and `sqrt(3)`, the three regimes of
the dual transform with their quoted control value, and the declared limitation
that the radial rate function is coarse on the axes. Nineteen checks in total.

Two refinements of the printed source were found while writing it and are
recorded in the report: the trace of the literal product (5.12) is
`ccc + sss`, not the `ccc - sss` printed in (5.13) (the two differ by `p -> -p`);
and for (5.15) the equality set of `|grad omega| = 1` is the full axial lines
through the conical points, not only the tips.

## Narrow-band signalling gate certificate (2026-09-17)

`verify_narrow_band_gate.py` is the exact certificate for the
[narrow-band signalling gate report](../reports/2026-09-17--narrow-band-signaling-gate.md),
which executes the contract
[`NARROW_BAND_SIGNALING_GATE.md`](../theory/NARROW_BAND_SIGNALING_GATE.md)
(preregistered at `817050d`). It was frozen at `778a44a` with its
[independent review](../reports/2026-09-17--narrow-band-signaling-gate-independent-review.md);
see `state/CURRENT_STATE.md` Sec. 8.16. The verdict is
`NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS`.

It covers steps 0-2 of the contract only: class, chart, pre-choice IR control
and the Sec. 7 encoded-difference test. That test triggers the stop rule, so
no Bob state and no `D_B` is constructed. It reuses the frozen symbol `walk2()`
and the Laurent equality test from `verify_directional_saturation.py`
read-only, and does not modify that reviewed file.

Requirements: Python 3.12, `sympy==1.14.0` and `numpy==1.26.4`, both pinned
in `requirements.txt`. The certificate itself does not use numpy, but
`verify_directional_saturation.py` imports it at module level; without numpy
the import fails before any check runs. Run from the repository root:

```sh
python3 scripts/verify_narrow_band_gate.py
```

It runs 34 exact SymPy checks, with no floating point in any computed quantity,
no quadrature, no lattice truncation and no `Lambda` scan. It fails closed: any
failed check or exception exits nonzero. The count certifies only the
identities and limits marked [V] in the report. The analytic steps listed in
report Sec. 12 are not encoded as checks; the independent review verified them
by hand. These steps are the chart lemma, the flat-spectrum lemma and the
reduction to three dimensions, the two-sided bounds on `s`, the sign
conditions, the upper half of the squeeze, the `R_W` constants and the
`kappa(pi/4)` link.

## Scaled IR signalling gate certificate (2026-09-17)

`verify_scaled_ir_gate.py` is the exact certificate for the
[scaled IR signalling gate report](../reports/2026-09-17--scaled-ir-signaling-gate.md),
which executes the contract
[`SCALED_IR_SIGNALING_GATE.md`](../theory/SCALED_IR_SIGNALING_GATE.md)
(preregistered at `31b5797`). See `state/CURRENT_STATE.md` Sec. 8.17. The
verdict is `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`.

It checks identities supporting geometry, chart, operation algebra, the
ellipse-product polynomials, contour constants, Laurent-block norms and the
sixteen response functionals. It does **not** compute signals, certify
positivity, or encode the analytic steps for `J`, `T_N` or `D_B`. Those were
re-derived in the
[independent review](../reports/2026-09-17--scaled-ir-signaling-gate-independent-review.md).
It reuses `walk2()`, `is_zero`, `PAULI`, `PS` and `exact_blocks` read-only.

Requirements: Python 3.12, `sympy==1.14.0` and `numpy==1.26.4`, both pinned
in `requirements.txt`. The certificate itself does not use numpy, but
`verify_directional_saturation.py` imports it at module level. Run from the
repository root:

```sh
python3 -B scripts/verify_scaled_ir_gate.py
```

It runs 53 exact SymPy checks, with no floating point in any computed
quantity, no quadrature, no lattice truncation and no `N` scan. It fails
closed: any failed check or exception exits nonzero.

## Lower-bound / no-cancellation certificate (2026-09-17)

`verify_lower_bound_no_cancellation_gate.py` is the exact certificate for
the [cancellation-gate report](../reports/2026-09-17--lower-bound-no-cancellation-gate.md),
executing
[`LOWER_BOUND_NO_CANCELLATION_GATE.md`](../theory/LOWER_BOUND_NO_CANCELLATION_GATE.md)
(preregistered at `1717d5e`). See `state/CURRENT_STATE.md` Sec. 8.18. The
verdict is `OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`.

It checks unique-path identities, facing-point geometry, the vanishing of
the profiles on the Euclidean spheres, and the Taylor orders of `c_N` and
`s_N`. It does **not** identify a leading amplitude, classify `A`, or
certify vanishing. Those are analytic and remain open. Run from the
repository root:

```sh
python3 -B scripts/verify_lower_bound_no_cancellation_gate.py
```

## Regional directional-asymptotics certificate (2026-09-17)

`verify_regional_directional_asymptotics_gate.py` is the exact certificate
for the
[regional-asymptotics report](../reports/2026-09-17--regional-directional-asymptotics-gate.md),
executing
[`REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md`](../theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md)
(preregistered at `08613d0`). See `state/CURRENT_STATE.md` Sec. 8.19. The
verdict is `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`.

It checks the holomorphic trace identity, facing-point algebra, the
`log 2` tilt bound above `J`, tilted mixing `sinh t`, profile Taylor
orders, and the one-dimensional layer critical point. It does **not**
certify `C`, `β`, or remainder control. Run from the repository root:

```sh
python3 -B scripts/verify_regional_directional_asymptotics_gate.py
```

## Regional Laplace-coefficient certificate (2026-09-17)

`verify_regional_laplace_coefficient_gate.py` is the exact certificate
for the
[Laplace-coefficient report](../reports/2026-09-17--regional-laplace-coefficient-gate.md),
executing
[`REGIONAL_LAPLACE_COEFFICIENT_GATE.md`](../theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md)
(preregistered at `6f520ad`, blob `18d1f65`). See
`state/CURRENT_STATE.md` Sec. 8.20. The verdict is
`PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`.

It checks hermiticity of `S(-i ξ)`, half-period Laurent symmetries,
triviality of plane characters, the closed forms of `P`, `C_*^2`,
`q_n`, `q_t`, the Weyl tail of `r`, the Laplace/Poisson identities of
the discrete layer, the prefactor `\mathcal K`, the algebraic power
count `β = 13/2`, and interval enclosures of the sixteen complete
coefficients `C_{M,M_B}(θ)` (uniform sign in `θ`). It does **not**
certify the analytic remainder lemmas (`N_*`, `C'`). `--diagnostics`
is `SUPPORTED` only and is never used for `β`, `C` or the terminal
state. Run from the repository root:

```sh
python3 -B scripts/verify_regional_laplace_coefficient_gate.py
```

## Current scope

Project status, the active line and any authorized next calculation are
recorded only in [`state/CURRENT_STATE.md`](../state/CURRENT_STATE.md), which
is branch-local on `research/b-infinity-post-s4-gate`. This file does not
restate them. The
[massless rigidity gate](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md), which
this section previously named as the only next calculation, is historical: it
was completed by counterexample for the declared `s=4` class (see
[`PROJECT_INSTRUCTIONS.md`](../PROJECT_INSTRUCTIONS.md) Sec. 7).

Rules for any new scientific script:

- Freeze its contract before adding scientific code.
- Preserve completed verifiers and their evidence records.
- Do not change the bytes of an independently reviewed verifier without a new
  review of that file.
- No broad scans, anisotropic detours or new substrate classes.
- Every retained scientific result must have permanent, traced generating
  code; no ephemeral scripts may supply evidence.

## Exploratory IR spectral attribution (2026-09-22)

`ir_precision_N24.py` preserves the original fixed-N record. `ir_cancellation.py`
accepts N (default 24) and optional `--direct --scripts-dir scripts`.
The optional check imports the existing exact blocks and evolves the compact
perturbation in a nonperiodic box. No frozen verifier is modified.
See the [audit and reproduction commands](../reports/2026-09-22--ir-spectral-attribution-audit.md).
These are empirical finite-N diagnostics, not certificates or asymptotic gates.

## c across lattices gate (2026-11-01)

Repaired after the 2026-11-01 reviews: every tabulated value (step sets,
group indices, `r_in`, `c_0`, vertex counts, Gram matrices, `K`) is now
asserted by an exact `record`; 135/135 checks. A negative test that
alters one expected value in memory makes it exit 1. The Part 3 comment
now states the Duhamel identity with its unitary factor.

`verify_c_across_lattices_gate.py` certifies the
[`C_ACROSS_LATTICES`](../theory/C_ACROSS_LATTICES_GATE.md) contract,
preregistered at `30672ba`. Run from the repository root; fail-closed.

Part 1 (22 exact checks): for rows L5a, L5b, L6a, L6c–L6f it builds the
exact Bloch symbol of one complete update from the source equations,
checks unitarity on the unit torus, checks the source identities it uses
(ADMP Eq. (5) C1–C2, JDW printed inverses, the Mlodinow–Brun Clifford
relations for the chosen representation) and prints the composite step set
F with its lattice index. Two ADMP sign issues are certified as recorded
issues (Eq. (8) holds for `alpha=-arccos(sqrt5/3)`; the printed `S` orders
the `tau_i` backwards, `S^{-1}` restores Eq. (7) = Eq. (10)). Row L6b is
reported as not encoded, with its reason.

Part 2 (46 further checks, 68 total): massless node at `k=0` for L1, L2
(from the reviewed `published_symbol`/`fourier_support`, imported
read-only) and the seven new rows: `U(0)=I`, Hermitian linear generators,
no tilt, isotropic cone `{T_a,T_b}=2c_0^2 delta_ab`, exact `C_micro` facets
and vertices, `r_in`, `c_0`, and non-nilpotency of every vertex coefficient
(hence `C_infty^strict = C_micro`, `c_strict^iso = r_in`). Prints Ha/Hb/Hc
per row and asserts Hc where decided.

Part 3 (35 further checks, 103 total): massive rows L5b, L6c–L6f with
mass parameter `theta` (quasienergy gap at `k=0`). Uses the exact identity
`i dU U(0)^dag = X_par + (sin theta/theta) X_perp` for `U(0)=exp(-i theta Q)`
to obtain the linear term of `H = i log U` without a matrix-log series, and
`G=(U+U^dag)/2` for the `omega^2` curvature. It certifies, per row, the
scalar Gram matrix of the linear term (`c_H(n)`), and the exact
decomposition `Hess cos(omega)(0) = -c_0^2 cos(theta) I + sin(theta) K`
with `theta`-independent `K`; isotropy is printed, not assumed. Positive
control: reproduces the reviewed 1D Dirac block (`c_H = c_0 M cot M`,
`K=0`). ADMP's mass (inside `W`) is not encoded (OPEN).

What it does **not** certify: the step-set identifications are printed,
not asserted, except for L5a/L5b (`{±1}^3`); `V_grp^max` is not computed;
the ADMP massive row is not computed; signs of nonzero radicals use SymPy's exact
relational evaluation; the
reading of the source conventions (phase, product order, read-from-
neighbour routing) is a declared choice documented in the script header,
not a theorem. Not independently reviewed.

## Hexagonal ceiling gate (2026-11-01, in progress)

`verify_hex_ceiling_gate.py` certifies part of
[`HEX_CEILING`](../theory/HEX_CEILING_GATE.md), preregistered at `8c56ced`.
18 exact checks: the lattice-grid step of L0 (facet-normal frequencies on
a uniform grid), the T1 algebra symbolic in the pairwise overlaps
(isotropy iff equal overlaps, `c_0^2 = (3/2) l^2 (1-g)`, PSD iff
`g >= -1/2`, hence `c_0/r_in <= sqrt3/2`), an exactly certified walk
attaining `sqrt3/2`, and the ADMP overlaps `g = 1/3` reproducing
`c_0 = 1/2`. Reuses read-only helpers of `verify_c_across_lattices_gate.py`.

T2 minimal support (6 further checks, 24 total): layer structure along
the three facet normals, the layer equations forcing `A_0 = -I/2`, and a
lex Gröbner basis of the unitarity system containing a real quadratic of
discriminant `-1/12` (no real solution); positive control on the square
substrate (consistent system, solved by the known saturating walk).

Does **not** certify: the Bernstein step of L0 and the Bernstein-equality /
Julia step of T2 (prior art, applied in the report), the normal-form
reduction, the reduction of a general `n = 3` antipodal walk to product
form, or T2 beyond minimal support. Not independently reviewed.

`explore_hex_saturation_support.py` is **exploratory, not a certificate**:
it builds the same saturation system for a given support and runs a
grevlex Gröbner basis over `C`. Its docstring records the runs (minimal:
consistent over `C`, 0.5 s; 19-point ball: not finished in 900 s). It
supports no verdict.

## Hexagonal supremum gate, M1 (2026-11-03)

`verify_hex_supremum_gate.py` certifies Stage A and M1-B13 of
[`HEX_SUPREMUM`](../theory/HEX_SUPREMUM_GATE.md), preregistered at
`86573ca`. 12 exact checks: lattice-point counts of the closed hexagons
S7, S13, S19 (7, 13, 19); in S13 the facet-normal layers lie on the grid
`r_in/3` and the layers `+-2 delta` are singletons that together are the
inner ring; a second route (generic coefficients on all 13 points, exact
solve of the layer equations) forcing every inner-ring coefficient to 0;
the surviving `{0} U vert` similar to the T2 configuration; in S19 layer
sizes 3,4,5,4,3 with no intermediate singleton; and a read-only rerun of
`check_T2_minimal` of the reviewed `verify_hex_ceiling_gate.py` (4/4).
Does **not** certify: facet-line rigidity and the normal form (hex-ceiling
report Sec. 3, Steps 1-2), or that the T2 proof is lattice-free (report).
Nothing for S19 or larger supports. Reviewed 2026-11-03: Grok PASS,
Gemini PASS (verifier SHA-256 `ef4b0114…`).

`verify_hex_supremum_b19.py` certifies M1-B19 of the same gate (S19).
Exact: the linear reductions L1 (layer sums, 56 free real parameters),
L2 (first moments, lemma A3, 28) and L3 (off-diagonal first order, lemma
A4, 18), all consistent over `QQ(sqrt3)`; controls (the saturating square
walk satisfies L1-L3, the whole pipeline on the 3x3 square support keeps
it and all reduced equations vanish; unitarity_equations detects a
non-unitary perturbation); the reduced system (18 parameters, 730
quadratics) and an exact infeasibility certificate: rational multipliers
from `data/hex_s19_certificate.json`, Gram matrix of their combination
positive definite by exact elimination (19 positive pivots). About 11
minutes. Does **not** certify the analytic proofs of rigidity, A3, A4 or
the normal form (report). Not independently reviewed.

`explore_hex_s19_reduced.py` (least squares on the reduced system) and
`explore_hex_s19_certificate.py` (search for a positive-definite
combination; wrote `data/hex_s19_certificate.json`) are **exploratory,
not certificates**; runs recorded in `reports/2026-11-03--hex-supremum-b19.md`.

## Dispersion corrections gate (2026-11-02)

`verify_dispersion_corrections_gate.py` certifies
[`DISPERSION_CORRECTIONS_ACROSS_LATTICES`](../theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md),
preregistered at `a7ff5b7`, for the
[execution report](../reports/2026-11-02--dispersion-corrections-across-lattices.md).
81 exact checks, about 11 minutes (79 at the reviewed version; two
added by the review repairs, see the report Sec. 5). Run it with an interpreter that has
`sympy==1.14.0` (here `/home/adnac/venvs/torch-gpu/bin/python -B`). It
imports the thirteen massless symbols read-only from
`verify_weyl_dirac_gate.py`, `verify_c_across_lattices_gate.py`,
`verify_directional_saturation.py`, `cert_Aa_s4_counterexample.py` and
`verify_l6b_triangular_row_gate.py`; those files are unchanged. Importing
them reruns the parent row constructors' own checks, which the script
requires to pass.

Certified per row: the exact Taylor coefficients of the node branch
through relative order `t^4` (`d <= 2`) or `t^2` (`d = 3`), `c_0` against
the parent table, the absence of a linear phase, the walk's symmetry group
by Laurent identities of power traces, the harmonic decomposition, and the
sign of `alpha_0` (for L3s4 symbolic in `a`, with the exact root in
`0 < a < 1`). Cross-checks: L1 exactly linear, L6b equal to L6a scaled by
2/3, 2, 4 and rotated 60°, hand closed forms for L2, L6e, L3, L5a, L5b, L4
and L6a, and the Newton-identity characteristic polynomial against the
full one on L5b.

Does **not** certify: `V_grp^max` (OPEN), the scale of validity in
`d >= 2` (OPEN), terms beyond the stated order, or any reading of the
hypotheses beyond the printed coefficients. The verdicts on Hd, He and Hf
are drawn in the report from the printed values; the script prints them
but asserts none. Not independently reviewed.

## Dispersion L3 row gate (2026-11-04)

`verify_dispersion_L3_row_gate.py` certifies
[`DISPERSION_L3_ROW`](../theory/DISPERSION_L3_ROW_GATE.md), preregistered at
`d3868fa`, for the [report](../reports/2026-11-04--dispersion-L3-row.md).
35 exact checks, about 10 s (`python3 -B`, sympy 1.14.0). It imports
read-only the helpers of `verify_dispersion_corrections_gate.py` and the
symbols of `verify_weyl_dirac_gate.py` (`published_symbol(3, ±1, ·)` and
transposes: cases A+, B+, A−, B−), `verify_directional_saturation.py`
(`walk1`, CJWW (5.12)) and `verify_c_across_lattices_gate.py`
(`row_L5a`); those files are unchanged. The comparison rows (CJWW (5.12),
L5a) are recomputed with the parent's own row setup.

Certified per case: unitarity, `det U = 1`, `tr U = 2(ccc + chi sss)`,
support `{±1}^3`, and the parent's per-row checks (no degree-0/1 terms in
`omega^2`, `c_0 = 1/sqrt3`, no linear phase). Prints the contract row verdict; hypothesis verdicts print «NOT CERTIFIED» if any check fails. Printed, not asserted: `beta`,
`alpha`, their cubic projections, `G_walk`, and the verdicts on HL3b–HL3e.

Does **not** certify: `V_grp^max`, the scale of validity, terms beyond
relative order `t^2`. Reviewed by gpt-6.1-sol (REPAIR_REQUIRED, repairs applied, not re-reviewed).
