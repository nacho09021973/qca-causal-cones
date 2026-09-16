# OPERATIONAL_INVISIBILITY_GATE — frozen contract

**Frozen:** 2026-09-16, before solving, per `PROJECT_INSTRUCTIONS.md` Sec. 5 and
the charter discipline of `MASSLESS_INRADIUS_RIGIDITY_GATE.md` Sec. 2.
**Initial scientific status: OPEN.**
**Authorization:** direct user instruction, 2026-09-16, selecting the directional
variant ("añadir la función de tasa direccional I(v)") over the narrow and the
signalling variants.

## 0. Question

`state/CURRENT_STATE.md` Sec. 8 establishes that the substrate permits causal
relations outside the emergent cone: `B(c_IR) ⊊ C_micro`, with the gap certified
at the vertex rays for every `n`. This gate asks the immediate physical
follow-up, and only this:

> In the region `C_micro \ B(c_IR)`, is the propagation exponentially suppressed
> at a **direction-dependent** rate, and does that rate distinguish the axial
> directions (where `v_sub = c_IR`) from the rest?

## 1. Frozen object

The CJWW walk of `sources/2408.02108v1.pdf` Eq. (5.15) **only**
(SHA256 `25e2b03e...a7bd8e0`, recorded in `sources/S4_FAMILY_AUDIT_SOURCES.md`):

`ω(p) = arccos(cos p1 cos p2 cos p3)`, `C_micro = [-1,1]^3`, `c_IR = 1`,
`Γ = B(1)` in the normalization of Sec. 8, one lattice step per time step.

No other walk, lattice, internal dimension, mass term or substrate class is
admitted. Walk (5.12) may be cited for contrast but is not part of the target.

## 2. Admitted method

CJWW Theorem 2.1 only:

`I(x) = sup_λ ( λ·x − R(λ) )`,
`R(λ) = sup_{p∈B} sup { log|u|² : u ∈ spec W(p + iλ/2) }`.

For this walk `det W = 1`, so both eigenvalues follow from the trace and
`log|u|² = 2|Im ω|` with `cos ω = ∏_k cos(p_k + i λ_k/2)`.

Nothing outside this is admitted: no new inequality, no new model, no
Bernstein/paraunitary/novelty line (`CURRENT_STATE.md` Sec. 8.7).

## 3. Declared hypotheses, stated before solving

- **H1 (closed form).** The inner supremum over `p` is attained at the conical
  points, giving `R(λ) = 2 arccosh( ∏_k cosh(λ_k/2) )`.
- **H2 (two asymptotic regimes).** `R(λ) → h_{B(c_IR)}(λ) = |λ|` as `λ → 0`, and
  `R(λ) → h_{C_micro}(λ) = ||λ||_1` as `|λ| → ∞`, so that the **small-λ regime is
  governed by the emergent cone and the large-λ regime by the microscopic
  causal body**.
- **H3 (trichotomy).** `I(x) = 0` iff `x ∈ B(c_IR)`; `0 < I(x) < ∞` iff
  `x ∈ int C_micro \ B(c_IR)`; `I(x) = ∞` iff `x ∉ C_micro`.
- **H4 (axial sharpness).** In each of the six axial directions, where
  `v_sub(ê_i) = c_IR`, there is **no** exponentially suppressed tail:
  `I(r ê_i) = ∞` for every `r > 1`. The tail of H3 exists only off-axis.

Refutation of any `Hi` is a valid gate outcome and must be recorded as such.
`H1` in particular is a conjecture; it must not be assumed while testing H2-H4.

## 4. Consistency control (must pass, or the gate fails)

Restricted to `λ = ℓ(1,1,1)/√3`, the result must reproduce CJWW's own published
radial function, Eq. (5.21), `R̃(ℓ) = 2 arccosh( cosh(ℓ/2√3)³ )`, together with
`Ĩ(r) = 0` for `r < 1`, `Ĩ(r) = ∞` for `r > √3` and `Ĩ(1.1) ≈ 0.104`.
A directional result that fails this control is wrong, not new.

## 5. Evidence discipline

Each claim carries its own tag (`PROJECT_INSTRUCTIONS.md` Sec. 4). In
particular the location of the inner supremum over `p` is expected to be
numerical; if so, `H1` is capped at **SUPPORTED** and every consequence drawn
from it inherits that cap. Exact asymptotics and exact axial statements are not
capped by it if they are derived without assuming `H1`.

## 6. Explicit exclusions

- **No signalling claim.** `I(x)` bounds the position distribution of one
  particle. It is **not** a statement about commutators, operational
  distinguishability or no-signalling. The probability/signalling question is
  the variant the user did **not** select and remains unchartered.
- **No QCA lift.** The walk is not promoted to a many-body QCA here.
- **No lower bound on probability.** CJWW give an upper bound only (their
  Sec. 2.1); "suppressed at rate `I`" means bounded above by `exp(-tI)`, not
  asymptotically equal to it.
- **No continuum-limit theorem.** Any statement about the Weyl scaling limit is
  a corollary at fixed rescaled velocity, with the scaling written out, not a
  convergence theorem on arbitrary states.
- Sec. 7 of `CURRENT_STATE.md` and the point-(3) contract are untouched.

## 7. Outcome record

To be filled by the report. Status on freezing: **OPEN**.
