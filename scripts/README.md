# Scripts

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

### IG-S2 true-ground-space sum-rule controls (2026-10-08)

`verify_inverse_gravity_ground_sum_rules.py` checks
[the frozen ground-space audit](../theory/INVERSE_GRAVITY_GROUND_SPACE_SUM_RULE_GATE.md).
Its tests cover support geometry, a degree-two Fourier identity and an
auxiliary three-level ground-space example. The example tests D=2F and
refutes inference of two physical excited states from a rank-two averaged
Gram matrix alone. It does not compute any true N-type ground expectation.
See [the analytic report](../reports/2026-10-08--ig-s2-true-ground-sum-rules.md).
Run `python3 -B scripts/verify_inverse_gravity_ground_sum_rules.py`;
`--output <path>` retains output only after all checks pass.

### IG-S2 constraint-preserving curvature probes (2026-10-08)

`verify_inverse_gravity_curvature_probes.py` certifies the stencils and
axial tangent symbol of the fixed R_xx/R_yy/R_xy pair in
[the curvature contract](../theory/INVERSE_GRAVITY_CURVATURE_PROBE_GATE.md).
It additionally checks sparse Weyl-word charges, costs and absence of
translation collisions on the two declared tori L=4,6.
It does not compute a true-ground correlator or spectral mode.
All-volume conclusions use the analytic
[report](../reports/2026-10-08--ig-s2-curvature-probe-preflight.md).
Run `python3 -B scripts/verify_inverse_gravity_curvature_probes.py`;
`--output <path>` retains the certificate only after all checks pass.

### IG-S2 compact tensor-probe commutator controls (2026-10-08)

`verify_inverse_gravity_sma_commutator.py` checks the permanent contract
[IG-S2/M3](../theory/INVERSE_GRAVITY_SMA_TENSOR_PREFLIGHT_GATE.md).
It uses exact 3x3/9x9 clock identities and a 27-state single-vertex momentum
term to verify signs, trace-cosine coefficients, vector incidences and the
zero-product-state witness. All-volume bounds require the analytic argument
in [the M3 report](../reports/2026-10-08--ig-s2-method-three-commutator.md).
It does not calculate the ground-state Gram matrix or excitation spectrum.

Run from the repository root:

```sh
python3 -B scripts/verify_inverse_gravity_sma_commutator.py
```

Optional `--output <path>` retains the record only after every check passes.

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

## Mixed-test sufficiency audit (2026-10-08)

`verify_inverse_gravity_mixed_test_sufficiency.py` checks the local q=3
conditional kinetic average, face counts, and symbolic mixed cost matrix
for the explicit false-positive density. Contract:
`theory/INVERSE_GRAVITY_MIXED_TEST_SUFFICIENCY_GATE.md`.
Run `python3 -B scripts/verify_inverse_gravity_mixed_test_sufficiency.py`
from the repo root; optional `--output <path>` retains passing output.
The all-volume state-admission and stationarity arguments are analytic;
the code does not compute an N-type vacuum or bound its tensor numerator.

## Mixed ground stationarity test (2026-10-08)

`verify_inverse_gravity_mixed_ground_test.py` checks the preregistered local
projector/partial-shift algebra, sign of the scalar-orbit stationarity witness,
and signed scalar-word collisions at L=4,6. The H_g diagonal-species check
uses the structural property inspected in Gu-Wen v3 p.18; it does not audit
all rho coordinates or calculate the N-type vacuum. Contract:
`theory/INVERSE_GRAVITY_MIXED_GROUND_TEST_GATE.md`. Run from the repo root:

```sh
python3 -B scripts/verify_inverse_gravity_mixed_ground_test.py
```

Optional `--output <path>` records output only after every check passes.
No tensor energy bound, all-volume extrapolation or independent review follows.

## Exploratory IR spectral attribution (2026-09-22)

`ir_precision_N24.py` preserves the original fixed-N record. `ir_cancellation.py`
accepts N (default 24) and optional `--direct --scripts-dir scripts`.
The optional check imports the existing exact blocks and evolves the compact
perturbation in a nonperiodic box. No frozen verifier is modified.
See the [audit and reproduction commands](../reports/2026-09-22--ir-spectral-attribution-audit.md).
These are empirical finite-N diagnostics, not certificates or asymptotic gates.

## Integrity tooling (2026-10-22)

See [audit](../reports/2026-10-22--escape-corruption-audit.md).

- `run_all_verifiers.py --output <tsv>`: runs every `verify_*.py` in its own
  process, records git HEAD, versions, exit code, time and last line; exits nonzero
  if any fails. It certifies nothing scientific; it tells whether the committed
  certificates still execute.
- `text_integrity.py --check | --repair --log <tsv> | --list-newline-suspects`:
  detects escape-sequence corruption in tracked `.md`/`.tex` (control characters,
  lone CR, suspected lost `\n`, bare `[`/`]` display delimiters). `--repair` restores
  only mechanically certain cases; decisions on lost newlines are in
  `text_integrity_newline_decisions.tsv`.
- `certificate_utils.py`: `assert_sym_equal` / `sym_zero`, value equality for
  SymPy identities (normalizes trig/exp). Used by `verify_w2_transport_tetrad.py` and
  `verify_w5_tetrad_source.py`, which failed under SymPy 1.14.0 with structural `==`.

29 verifiers (W1–W12, inverse-gravity, elastic families, others) still have no entry
in this README stating what they certify and what they do not. Until they do, do not
cite them for more than their own docstring and report say.
