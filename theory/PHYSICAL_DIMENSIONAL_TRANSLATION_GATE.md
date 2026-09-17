# PHYSICAL_DIMENSIONAL_TRANSLATION — frozen charter

**Frozen:** 2026-09-17, before the dimensional audit. **Initial status: OPEN.**
**Authorization:** direct user instruction, 2026-09-17.

## 0. Single question

> Does the declared CJWW (5.15) model and its checked source material specify a
> defensible map from its dimensionless lattice protocol to physical length,
> time, momentum and energy scales, sufficient to turn the exact non-corner
> signal `3/128` into a quantitative physical prediction?

This gate audits the existence and scope of a dimensional map. It does **not**
design an experiment and does not extend the witness to `Delta T = 2`.

## 1. Frozen input

- Model: the unchanged free-fermion CAR lift of CJWW Eq. (5.15).
- Protocol and result: `NONCORNER_SIGNALING_CONSTRUCTED /
  INDEPENDENTLY_REVIEWED`, at the four sites `y = (+/-1,+/-1,0)` and one
  post-encoding update.
- Exact operational quantity:
  `Delta p_B = D(rho_B^(0),rho_B^(1)) = 3/128` for each computed pair.
- Dimensionless normalization already established in-repo: one lattice step
  per update, `c_IR = 1`, and `C_micro = [-1,1]^3`.
- The localized preparation is not assumed to lie in the low-energy sector.

The numerical value `3/128` is frozen. A choice of units may not change a
probability or trace distance.

## 2. Candidate dimensional dictionary to audit, not assume

Introduce positive scales only as symbols until a source or an independently
declared physical model fixes them:

| Discrete object | Candidate physical quantity |
| --- | --- |
| lattice coordinate `n` | `x_phys = a n` |
| update count `N` | `t_phys = N tau` |
| torus momentum `p` | `k_phys = p/a` |
| eigenphase `omega(p)` | `E = hbar omega(p)/tau` modulo `2 pi hbar/tau` |
| dimensionless velocity `grad_p omega` | `v_phys = (a/tau) grad_p omega` |

Here `a` is a spatial lattice scale and `tau` one complete update time. The
audit must check conventions and whether the model fixes either scale or their
ratio. It must not silently set `a` to a named fundamental length or `tau` to a
named fundamental time.

## 3. Required questions

1. **Internal dimensional consistency.** Does the dictionary above follow
   from the Fourier and one-step conventions actually used for (5.15)?
2. **Scale determination.** Are `a`, `tau`, or `a/tau` fixed by the model or
   its source, or are they freely assignable external calibration data?
3. **Relativistic identification.** If the low-energy slope is identified
   with an observed speed `c_phys`, what relation follows, and is that an
   output or an imposed calibration?
4. **Protocol spacetime data.** What physical separations and durations follow
   conditionally from `a` and `tau` for the frozen witness?
5. **Energy/momentum content.** Does the localized protocol have a controlled
   low-energy or narrow-band interpretation that supports a characteristic
   physical energy/momentum prediction?
6. **Meaning of `3/128`.** Which dimensionful claims, if any, follow from it?

## 4. Outcome categories

- `DIMENSIONAL_MAP_SPECIFIED`: the checked model fixes the scales needed for a
  numerical physical prediction, not merely a change-of-units formula.
- `DIMENSIONAL_MAP_CONDITIONAL`: a consistent symbolic dictionary exists, but
  at least one physical scale or identification must be supplied externally.
- `DIMENSIONAL_MAP_NOT_SPECIFIED`: the checked material does not provide even
  a defensible mapping between the discrete and physical variables.

The audit must separately state whether `3/128` remains an operational
dimensionless prediction under a conditional calibration. A conditional map
is not a prediction of the lattice scale.

## 5. Evidence and stop rules

- Read the local primary CJWW source and the frozen in-repo model definitions
  before interpreting units.
- Distinguish source statements, algebraic consequences and optional physical
  identifications.
- Do not infer a Planck scale from the earlier explicitly conditional
  Planck-substrate estimate.
- Do not use empirical bounds to choose `a` or `tau`.
- Do not design apparatus, optimize the protocol, compute `Delta T = 2`, or
  claim feasibility.
- Stop once one outcome category is established and the exact claim ceiling
  is recorded.

## 6. PASS/FAIL semantics

This is an audit, not a demand that nature supply a scale. Any one of the three
outcome categories closes the gate if supported. `DIMENSIONAL_MAP_CONDITIONAL`
or `DIMENSIONAL_MAP_NOT_SPECIFIED` forbids calling `3/128` a parameter-free
physical prediction in SI units.
