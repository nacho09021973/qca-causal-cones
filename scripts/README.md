# Scripts

## Reconstruction integrity controls (2026-10-26)

`text_integrity.py --check` checks tracked text for escape corruption; bare
math delimiters inside fenced code are excluded, but control characters and
lost-newline suspects remain checked there. Run its regression tests with
`python3 -B scripts/test_text_integrity.py` (six tests).
`check_reconstruction.py <file> [base]` compares restored notation after
removing provenance blockquotes. `--allow-lost-cr-newlines` is an explicit
exception for logged CR-to-LF damage, used for CURRENT_STATE against `8dd9080`;
it is off by default. These checks do not certify scientific correctness.

No scientific script was present at the initial freeze (`44ad178`).

## W4 full-spectrum and observable audit (2026-10-26)

Run `python3 -B scripts/verify_w4_long_wavelength_spectrum.py` and
`python3 -B scripts/verify_w4_spectrum_observables.py` from the repository root.
The first has seven exact check blocks, including the occupied-bond phase
relative to the vacuum, the quadratic same-sign branch for fixed
0<kappa<pi/2, the opposite-sign linear node, exceptional endpoints and the
two-register/two-layer velocity convention. It supersedes the old printed
verdict that treated the phase-stripped smooth gap as a gap of the full gate.

The second has six blocks. It independently builds the full qubit circuit
on L=4,6 rings at kappa=0,pi/4,pi/2 for both signs (12 exact circuits), then
checks its restriction against the Bloch symbol. It derives the Z expectation,
tests a stationary uniform-density cell-pi eigenstate, verifies zero linear
Z response around the polarized vacuum and gives a coherence counterexample
to a closed density update. It shares only the equality helper and proposed
Bloch symbol with the first script; the real-space circuit is built separately.

See [audit and branch arguments](../reports/2026-10-26--w4-spectrum-audit.md).
Finite rings are regression witnesses, not a general infinite-volume proof.
Neither verifier certifies a linear metric wave, tensor/3D propagation or an
independent review. The suite now contains 43 verifiers. The existing stiffness
certificate and frozen W4 contract are unchanged; the control is not adopted
as a replacement model.

## Strengthened W3/W5/W6 certificates (2026-10-26)

Run each as `python3 -B scripts/<name>.py` from the repository root.
All use value equality via `certificate_utils.assert_sym_equal`.

| Script | Contract and report | Executed check blocks | Scope and exclusions |
| --- | --- | --- | --- |
| `verify_w3_backreacting_tetrad.py` | `W3_BACKREACTING_TETRAD_FLOQUET_GATE.md`; `2026-09-30--w3-backreacting-tetrad.md` | 4: exact rotation, initial-product slope, derived transport tetrad/sign control, mean-field feedback | Derives the transport g-jet from edge currents and CJWW; does not derive the full correlated O(g²) feedback or complete Floquet logarithm. |
| `verify_w5_tetrad_source.py` | `W5_TETRAD_CONJUGATE_SOURCE_GATE.md`; `2026-09-30--w5-tetrad-conjugate-source.md` | 4: three source families and product-state expectation | Includes the zero-current subspace, exact local kick and variational derivative of the leading transport generator; no conserved full stress tensor or closure after entanglement. |
| `verify_w6_full_spatial_tetrad.py` | `W6_FULL_SPATIAL_TETRAD_GATE.md`; `2026-09-30--w6-full-spatial-tetrad.md` | 11: four rank/kernel blocks, F5, F1, source-off negative control, F6, two schedule boxes, omitted-layer negative control | Derives nine-control transport jet and local F1/F5/F6 witnesses. Ranks require g≠0. Added-interaction schedule only; no full CJWW circuit synthesis, continuum metric propagation or gauge symmetry. |

`tetrad_transport.py` is permanent shared derivation code, not a separate
verdict. `w6_schedule.py` defines a conservative 90-layer scheduling witness;
matching/coverage checks run at L=4,6 and the all-volume parity argument is in
`reports/2026-10-26--w3-w6-certificate-strengthening.md`.
The sweep uses the existing glob, so the inventory remains 42 verifiers.
The modified certificates are author-checked versions; the earlier independent
reviews do not automatically review their new bytes.

## Previously undocumented verifiers (inventory of 2026-10-28)

Twenty-four committed verifiers had no entry here. Each row is taken from the
script's own docstring and its printed `Scope`/`VERDICT` lines, cross-checked
against the contract and report it names; it adds no scientific claim. All
passed (exit 0) in a full sweep of 46 verifiers at `233a553` (SymPy 1.14.0).
"Printed PASS lines" counts output lines starting with `PASS`/`[PASS]`/`OK`; it
is an inventory figure, not a count of independent theorems. Several scripts
certify a negative verdict: exit 0 means the declared outcome was reproduced,
not that a hypothesis survived. Run each as `python3 -B scripts/<name>` from
the repository root. None of these rows records an independent review of the
script itself; consult the report and `state/CURRENT_STATE.md` for review status.

| Script | Contract; report | Printed PASS lines | Certified verdict | Does not certify |
| --- | --- | --- | --- | --- |
| `verify_signaling_witness.py` | `theory/COUPLING_MAP_SIGNALING_WITNESS.md`; `2026-09-16--noncorner-signaling-gate.md`, `2026-09-16--alice-local-preparation.md` | 17 | 17/17 exact checks: finite signalling existence witness | Any optimum, asymptotic rate, state search or trace-distance optimization |
| `verify_irreducible_d2_pavia.py` | `2026-09-23--irreducible-d2-pavia-checks.md`; writes `2026-09-23--irreducible-d2-pavia-verification.md` with `--output` | — (writes a checklist record) | Exact checks for the scoped irreducible-D2 application of P17 | The analytic completeness and all-time support arguments, which live in the companion report |
| `verify_cjww_coordinate_factorization.py` | `theory/CJWW_SINGLE_COORDINATE_FACTORIZATION_AUDIT.md`; `2026-09-30--cjww-coordinate-factorization-audit.md` | 8 | Scoped factorization audit (frozen at `f9dcb46`) | Grouping, ancillas, repeated coordinate factors, powers of W, coordinate mixing; more than one tick or other cells. Prints `AUTHOR_SIDE_CERTIFICATE / INDEPENDENT_REVIEW_PENDING` |
| `verify_w1_geometricity.py` | `theory/W1_GEOMETRICITY_GATE.md`; `2026-09-29--w1-geometricity.md` | 5 | Two-step exact matter support depends on the link-register state; one-step adjacency and outer CJWW body unchanged | Any continuum or gravity interpretation |
| `verify_w4_geometry_stiffness.py` | `theory/W4_GEOMETRY_STIFFNESS_GATE.md`; `2026-09-30--w4-geometry-stiffness.md` | 5 | Geometry-only partial-SWAP transports the tetrad-control variable in vacuum | The corrected long-wavelength spectrum reading (see the W4 audit section above) |
| `verify_w5_spatial_tetrad_rank.py` | `theory/W5_SPATIAL_TETRAD_COMPLETENESS_GATE.md`; `2026-09-30--w5-spatial-tetrad-completeness.md` | 2 | W3–W5 geometry spans only a restricted spatial-metric submanifold | Gauge completion |
| `verify_w7_spin2_kinematics.py` | `theory/W7_SPIN2_KINEMATICS_GATE.md`; `2026-09-30--w7-spin2-kinematics.md` | 4 | W6 contains a 5-component kinematic spin-2 sector | Any TT reduction or dynamics |
| `verify_w8_tt_gauge_reduction.py` | `theory/W8_TT_GAUGE_COMPLETION_GATE.md`; `2026-09-30--w8-tt-gauge-completion.md` | 2 | A proposed local vector gauge symmetry would reduce 5 components to 2 TT components | That W6 realizes this redundancy microscopically |
| `verify_w9_continuum_gauge_bridge.py` | `2026-09-30--w9-cjww-graviton-matter-bridge.md` (repair D1) | 3 | Algebraic on-shell O(lambda) gauge-variation consistency | Weyl stress conservation and microscopic matching (inputs), local-Lorentz Ward identity, W6 source matching |
| `verify_w10_linearized_constraints.py` | `2026-09-30--w10-sourced-gu-wen-constraints.md` (repairs B1–B3) | 4 | Continuum test-source consistency at O(lambda) for linearized Einstein | A lattice Gu–Wen L-model calculation, coupled Ward identity, microscopic and reciprocal completion |
| `verify_w11_ir_stress_source.py` | `2026-09-30--w11-cjww-floquet-stress-tensor.md` (repairs A1/A2) | 6 | Free-walk integrated-charge conservation at all eight nodes, in Bloch space and by real-space convolution | q≠0 Belinfante stress kernel, interacting constraint identity, Floquet-logarithm no-go |
| `verify_w12_four_species_metric_universality.py` | `theory/W12_FOUR_SPECIES_METRIC_UNIVERSALITY_GATE.md`; `2026-09-30--w12-four-species-metric-universality.md` | 3 | `UNIVERSAL_SUBFAMILY_DEFICIENT` at first order in g and k, four +I nodes | Emergent gravity, higher orders, −I universality (diagnostic only), dynamics/backreaction of Z |
| `verify_elastic_graph_species_universality.py` | `theory/ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE.md`; `2026-09-30--elastic-graph-species-universality.md` | 5 | `KINEMATIC_COMMON_EMBEDDING_UNIVERSAL / ELASTIC_HOPPING_RESPONSE_OPEN` | Strain-dependent hopping rules, backreaction, curvature, gravity |
| `verify_elastic_hopping_orientation_obstruction.py` | `theory/ELASTIC_HOPPING_UNITARY_RESPONSE_GATE.md`; `2026-09-30--elastic-hopping-unitary-response.md` | 3 | `UNITARY_ELASTIC_RESPONSE_INCONSISTENT` (orientation-independence premise fails) | Any four-species metric calculation, which the obstruction precedes |
| `verify_elastic_hopping_hermitian_response.py` | `theory/ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE.md`; `2026-09-30--elastic-hopping-hermitian-response.md` | 6 | `HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY`, first order in epsilon and momentum, four +I nodes | Dynamical strain or gravity; no coefficient search was performed |
| `verify_inverse_gravity_constraint_module.py` | `theory/INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md`; `2026-10-08--inverse-gravity-constraint-mechanism.md` | 7 | Finite commuting tensor-constraint algebra (IG1a) | Any QCA tick, spectrum, IR modes or gravity |
| `verify_inverse_gravity_local_gates.py` | `theory/INVERSE_GRAVITY_LOCAL_GATE_GATE.md`; `2026-10-08--inverse-gravity-local-gate.md` | 6 | Local constraint-preserving non-scalar gate (IG1b) | Tick locality and state (argued in the report), modes, IR |
| `verify_inverse_gravity_full_tick_dynamics.py` | `theory/INVERSE_GRAVITY_FULL_TICK_DYNAMICS_GATE.md`; `2026-10-08--inverse-gravity-full-tick-dynamics.md` | 2 | One-step physical influence of the frozen tick (IG1c) | IR, modes, gravity, many-body diagonalization |
| `verify_inverse_gravity_ir_reference.py` | `theory/INVERSE_GRAVITY_IR_REFERENCE_GATE.md`; `2026-10-08--inverse-gravity-ir-reference.md` | 6 | `TRACIAL_REFERENCE_RESPONSE_NULL / TERMWISE_VACUUM_INCOMPATIBLE` (IG1d algebra controls) | The general sector proof (in the report), QCA modes, IR spectrum |
| `verify_inverse_gravity_ir_options_ab.py` | `theory/INVERSE_GRAVITY_IR_OPTIONS_AB.md`; `2026-10-08--inverse-gravity-ir-options-ab.md` | 4 | `AB_ALGEBRA_CONTROLS_PASS / SPATIAL_A_AND_B_OPEN` (IG1e) | Any verdict on the spatial QCA options |
| `verify_inverse_gravity_a0_conservation.py` | `theory/INVERSE_GRAVITY_A0_CONSERVATION_GATE.md`; `2026-10-08--inverse-gravity-a0-and-b0.md` | 1 | `A0_FAIL_NONCONSERVED_PHYSICAL_PARENT` via an exact energy witness | A Gibbs state or IR spectrum |
| `verify_inverse_gravity_b0_error_control.py` | `theory/INVERSE_GRAVITY_B0_ACCESS_GATE.md`; `2026-10-08--inverse-gravity-b0-access-audit.md` | 4 | `STATIONARITY_DEFECT_NOT_AN_ENSEMBLE_ERROR_BOUND` on an auxiliary two-level family | B-state convergence of the fixed QCA (`NOT_TESTED`) |
| `verify_inverse_gravity_dressed_parent.py` | `theory/INVERSE_GRAVITY_DRESSED_PARENT_GATE.md`; `2026-10-08--inverse-gravity-dressed-parent.md` | 4 | `DRESSED_PARENT_ALGEBRA_PASS_AUTHOR_SIDE`; gap interval uniform on admitted tori | That either endpoint is the exact gap; spatial claims (proved in the report) |
| `verify_inverse_gravity_state_first.py` | `theory/INVERSE_GRAVITY_STATE_FIRST_GATE.md`; `2026-10-08--inverse-gravity-state-first.md` | 5 | `STATE_FIRST_AUXILIARY_CONTROLS_PASS` | A new QCA rule, physical IR state, spin-2 spectrum or gravity (`NOT_COMPUTED`) |

## A.int Eon v4 reference-state controls (2026-10-27)

Run each as `python3 -B scripts/<name>` from the repository root. Each prints a
single summary `PASS` line after its internal exact checks; the counts in the
table above do not apply. Source model: Eon, Di Molfetta, Magnifico, Arrighi,
arXiv:2205.03148v4 (`biblioteca/`, sha256 in
`reports/2026-10-27--interaction-speed-primary-sources.sha256`).

| Script | Specification; report | Certified verdict | Does not certify |
| --- | --- | --- | --- |
| `verify_eon_reference_state.py` | `theory/A_INT_EON_REFERENCE_CHECK.md`; `2026-10-27--eon-reference-state-check.md` | Gauss and exact witness checks; the occupation-product candidate fails stationarity in the declared cases (`STOP_THIS_CANDIDATE`) | Rotor truncation, full gauge simulation, any vacuum construction, IR limit or loop; the full-step conclusions also rely on analytic arguments in the report |
| `verify_eon_received_answer_audit.py` | Report `2026-10-27--eon-received-answer-audit.md` | Exact algebra controls on two proposed shortcuts (sharp local number for E=0; principal-log selection) and a mass-only long-time control | The interacting 3D gauge QCA; it uses a four-site one-directional free slice and two-mode controls only; no vacuum construction |
| `verify_eon_projected_gaussian_reference.py` | `theory/A_INT_EON_PROJECTED_GAUSSIAN_REFERENCE.md`; `2026-10-27--eon-projected-gaussian-reference.md` | Construction ingredients of the Gauss-projected Gaussian reference (Dirac projector, integer Gauss solutions at L=3,4, tail control, magnetic harmonic counts, finite-Laurent and inverse-kick identities) | The Fourier/Jensen stationarity lemma, which is analytic; the harmonic count ignores JW/rishon plaquette signs (see the 2026-10-28 DeepSeek review, G-R1-04) |

`verify_eon_projected_gaussian_reference.py` imports helpers from
`verify_eon_reference_state.py`.

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

The October 22 audit recorded 29 verifiers without scope entries. The W3/W5/W6
entries above address three of those; the broader documentation backlog is not
closed here. Do not cite undocumented verifiers beyond their docstring/report scope.
