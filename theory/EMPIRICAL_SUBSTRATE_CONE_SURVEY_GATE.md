# EMPIRICAL_SUBSTRATE_CONE_SURVEY — frozen contract

**Frozen:** 2026-09-16, before surveying. **Initial status: OPEN.**
**Authorization:** direct user instruction, 2026-09-16.

## 0. Single question

> Which existing observations place quantitative limits on a **nonzero causal
> influence outside `B(c)`**, given that this influence may be non-ballistic,
> anisotropic and exponentially suppressed?

## 1. Declared premise — the scale computation, done before surveying

Sec. 8.10 gives, for the free-fermion lift of CJWW (5.15), a suppression of
`4^{-t}` at the vertex rays and `e^{-Ĩ(r) t}` radially, with `t` counted in
**lattice steps**. If the substrate is Planckian, `t = T/t_P`:

| `T` | `t = T/t_P` | `exp(-Ĩ(1.1) t)` |
| --- | --- | --- |
| 1 ns | `1.9e34` | `10^(-8.4e32)` |
| 1 s | `1.9e43` | `10^(-8.4e41)` |
| age of the universe | `8.1e60` | `10^(-3.6e59)` |

The finest experimental bounds ever achieved are `~10^-20` to `10^-30`.
**Therefore: this model's own effect is unobservable in principle, by tens of
orders of magnitude in the exponent, under any Planck-scale substrate
hypothesis.** The geometric window is by contrast *not* small: the accessible
region reaches `√3 ct`, i.e. 73% beyond the light cone.

Two consequences, binding on the survey:

- The survey may **not** be conducted as a search for constraints on this
  model's prediction. No such constraint can exist, and finding none would be
  uninformative.
- The survey is therefore **model-independent**: it asks what is constrained
  about spacelike causal influence *as such*, whatever its rate. A slower-rate
  substrate is not excluded by the table above, which is specific to an `O(1)`
  per-step rate.

## 2. Exclusions (as instructed)

1. **A bound on `v_g` is not a bound on this effect.** Sec. 8 proves
   `sup|v_g| = c` is compatible with influence outside `B(c)`. Dispersion,
   birefringence and species-comparison limits do not constrain the variable.
2. **Null results are not evidence for `C_micro = B(c)`.** The falsifiability
   asymmetry of `SUBSTRATE_CONE_OBSERVABILITY_GATE.md` Sec. 4 applies in full.
3. **No model of our universe.** No lattice, no preferred frame, no substrate is
   attributed to nature.
4. **No anisotropic `I(v)`** for the QCA; that remains `NOT_AUTHORIZED`.

## 3. Outcome categories — exactly three

- `DIRECT_CONSTRAINTS_FOUND` — an experiment genuinely bounds spacelike
  signalling or spacelike causal response.
- `INDIRECT_ONLY` — only Lorentz, dispersion, threshold or similar are found.
- `NO_CURRENT_OPERATIONAL_TEST` — no existing observation touches the variable.

`NO_CURRENT_OPERATIONAL_TEST` is a scientifically informative outcome, not a
failure: it would mean `c = ` fundamental causal boundary is not merely
unproved but **untested in the operational sense isolated in Sec. 8.10**.

## 4. Evidence discipline

Every cited bound must name the observable it actually constrains, and be
classified as direct or indirect **against Sec. 2.1**, not against its own
abstract's phrasing. A paper claiming to "test causality" that in fact bounds a
dispersion coefficient is `INDIRECT_ONLY`. Sources are primary where possible;
anything unverified is tagged as such.

## 5. Outcome record

**Status: COMPLETE (2026-09-16).** Split verdict, see
[`2026-09-16--empirical-substrate-cone-survey.md`](../reports/2026-09-16--empirical-substrate-cone-survey.md):
`DIRECT_CONSTRAINTS_FOUND` for the scalar variable (Bell no-signalling tests),
`NO_CURRENT_OPERATIONAL_TEST` for the directional structure of Sec. 8.10.
