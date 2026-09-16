# COUPLING_MAP_OPTIMAL_D — frozen contract

**Frozen:** 2026-09-16, before solving. **Initial status: OPEN.**
**Authorization:** direct user instruction, 2026-09-16 ("congela ese gate del
mapa de acoplamiento").

## 0. Single question

> For the Sec. 8.10 causal tail, which local operation, which remote observable,
> which state and which geometry **maximize** `D = ½‖ρ_B^{(1)} − ρ_B^{(0)}‖₁`,
> and what is `max D` as a function of the single-particle kernel?

This is the object whose absence blocked the empirical transfer in Sec. 8.11:
`[α_t(A), B] ≠ 0` gives *existence* of some intervention with `D > 0`, not that
any particular protocol realizes it.

## 1. Frozen target

The free-fermion (CAR) lift of CJWW Eq. (5.15) declared in
[`SUBSTRATE_CONE_OBSERVABILITY_GATE.md`](SUBSTRATE_CONE_OBSERVABILITY_GATE.md)
Sec. 1, unchanged: even local observables, `α_t(a(f)) = a(W^t f)`,
`C_micro = [-1,1]^3`, `c = 1`, `v_sub(n̂) = ‖n̂‖₁`. No new model, no new lift, no
change of normalization.

## 2. Two boundaries fixed here, because the question is otherwise ill-posed

**(a) Optimize over protocol at fixed geometry; do not range over geometry.**
Optimizing `(L, t, n̂)` as well would require the magnitude of the kernel
throughout `C_micro \ B(c)`, which *is* the anisotropic `I(v)` object that
Sec. 8.10 left `NOT_AUTHORIZED`. Permitted instead: evaluation at a **finite,
declared list** of geometries, fixed in Sec. 4 before solving. Evaluating
finitely many points is not computing a rate function; if the work starts to
require the rate function, the gate **stops** and reports that.

**(b) Declare the resource, or "maximize" is meaningless.** `D` is bounded for
fixed regions and bounded operator norms, but Alice's region may hold many
particles and modes. Whether `D` amplifies with that number is exactly the
"how far short would sensitivity fall" question, so it must be asked, not
assumed. The declared resource is: `N` = number of fermionic modes Alice may
act on in `A`, and `M` = number Bob may measure in `B`, with all operations even,
local and norm-bounded by 1.

## 3. Declared hypotheses, stated before solving

- **H1 (kernel is the figure of merit).** `max D = Θ(‖(W^t)_{y,x}‖)` at fixed
  geometry and `N = M = 1`, with a state-independent constant — i.e. the
  single-particle kernel is tight, not merely an upper bound.
- **H2 (the state is not free).** The optimum requires occupation or coherence
  supported at `A`; in particular `D = 0` in the vacuum for number-type
  interventions, so no protocol works on an arbitrary state.
- **H3 (Bell protocols are not optimal).** The optimal Alice operation is **not**
  a Bell-type measurement-setting choice. If true, this is the precise reason the
  Sec. 8.11 scalar bound cannot be transferred, and it converts that gap from
  "unknown" into "known to be the wrong probe".
- **H4 (amplification).** `max D` scales with the declared resource as `N^p` for
  some `p ∈ {0, 1/2, 1}`, to be determined. `p` is the exponent that says how
  much sensitivity collective protocols can buy.

Refutation of any `Hi` is a valid outcome. In particular, if `max D` turns out
to be **exactly zero** for all admissible even protocols despite the nonzero
commutator, that is a decisive outcome and must be recorded as such: it would
mean the Sec. 8.10 tail is real but operationally inert.

## 4. Declared geometries (fixed before solving)

With `x = 0` and `t ∈ {2, 3, 4}`, the remote site `y` is taken from exactly:

1. the vertex ray `y = (t,t,t)` — maximal `v_sub`, minimal kernel;
2. a face-diagonal ray `y = (t,t,0)`;
3. the nearest off-axis lattice site strictly outside `B(c)t`;
4. an axial control `y = (t+1,0,0)` — where Sec. 8.10 gives exactly zero, and
   any nonzero `D` would indicate an error.

No other geometry is admitted without a new freeze.

## 5. Explicit exclusions

- **No mapping to a real experiment.** Which physical system realizes the lift,
  and what a laboratory would have to do, is a **later** question, per the
  authorizing instruction ("sólo después"). Not chartered here.
- **No claim about our universe.** Sec. 8.9(iii) stays UNKNOWN; the
  falsifiability asymmetry of Sec. 8.11 applies unchanged.
- **No anisotropic `I(v)`**, per Sec. 2(a).
- **No re-opening of the empirical survey**; its verdict stands until this gate
  supplies the map.
- **No channel-capacity theory** beyond what is needed for `max D`; capacities
  are a separate object and are not claimed.

## 6. What counts as PASS

A map `(state, Alice operation, Bob observable, geometry, resource) → D`, with
an **achievability** construction and a **matching upper bound**. If only one
side is obtained, the gate records that asymmetry rather than claiming the map.

## 7. Outcome record

**Status: PARTIAL — stop rule applied at the first classifiable result (2026-09-16).**
H1 CONFIRMED conditionally, H2 CONFIRMED and sharpened, axial control passed;
**H3 and H4 NOT REACHED.** Returns achievability plus an upper bound restricted
to number-conserving Gaussian local operations, so the map is recorded with that
asymmetry rather than claimed in full (Sec. 6). See
[`2026-09-16--coupling-map.md`](../reports/2026-09-16--coupling-map.md).
