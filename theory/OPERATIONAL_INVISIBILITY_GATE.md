# LDP_RADIAL_INTERPRETATION — frozen contract

**Gate name:** `LDP_RADIAL_INTERPRETATION = DOCUMENT_EXISTING_RESULT`.
**Frozen:** 2026-09-16.
**Authorization:** direct user instruction, 2026-09-16.

## 0. Revision note — supersedes the first freeze

This file was first frozen at `a9e611a` chartering the **directional** variant
(computing `I(x)` by direction from CJWW Ec. (2.9)). Before any solving was
done under it, the user narrowed the scope to documenting the existing radial
result. That first charter is therefore **SUPERSEDED, UNSOLVED**; no result was
produced under it and none may be cited from it. History is not rewritten: the
narrowing is recorded here.

Reason given, and adopted: computing `I(v)` by direction is new work and is not
needed to answer the physical question.

## 1. Scope — exactly this, nothing more

1. Verify CJWW Eq. (5.21) exactly.
2. Derive its two asymptotic slopes.
3. Record the dual transform and the three resulting regimes.
4. Connect the slope `1` to `c_IR` and the slope `√3` to the body diagonal of
   `C_micro`.
5. Declare explicitly that **no** operational-invisibility or no-signalling
   theorem follows from this.
6. Leave anisotropic `I(v)` and the signalling question as `NOT_AUTHORIZED`.

Target: the CJWW walk of `sources/2408.02108v1.pdf` Eq. (5.15) only, in the
normalization of `state/CURRENT_STATE.md` Sec. 8 (`C_micro = [-1,1]^3`,
`c_IR = 1`, one lattice step per time step).

## 2. What is being documented

`R̃(ℓ) = 2 arccosh( cosh(ℓ/2√3)³ )` — CJWW Eq. (5.21) — and its Legendre
transform `Ĩ`, which bounds the probability leakage outside a ball of radius
`r` by `exp(-t Ĩ(r))` (their Eq. (5.18)).

## 3. Consistency control (must pass, or the gate fails)

`Ĩ(r) = 0` for `r < 1`, `Ĩ(r) = ∞` for `r > √3`, and `Ĩ(1.1) ≈ 0.104` as quoted
by CJWW. A result that fails this control is wrong, not new.

## 4. Declared limitations, stated before solving

- **The radial function is coarse, and demonstrably so.** `Ĩ` is a radial
  reduction; CJWW state that `I(x)` "is certainly not a rotation invariant
  function". The angular structure of `I` is **not resolved by this gate**, and
  Sec. 8 already implies the radial picture cannot be the whole story: since
  `v_sub(ê_i) = c_IR` axially, a velocity `r ê_i` with `r > 1` lies outside
  `C_micro`, where the amplitude is exactly zero — not exponentially suppressed.
  So the finite rate that `Ĩ` reports for `1 < r < √3` is carried by non-axial
  directions only.
- **Upper bound only.** CJWW give no lower bound (their Sec. 2.1), so
  "suppressed at rate `Ĩ`" means bounded above by `exp(-tĨ)`, never
  asymptotically equal to it.
- **One particle, position distribution.** `Ĩ` bounds the distribution of
  `Q(t)/t`. It says nothing about commutators, distinguishability or channel
  capacity.

## 5. Explicit non-authorizations

- `I(v)` anisotropic / directional: **NOT_AUTHORIZED**.
- Probability vs signalling (operational invisibility proper): **NOT_AUTHORIZED**.
  It needs resources, distinguishability or channel capacity to be defined
  first, and changes problem class; it merits an independent charter if ever
  attacked. At QCA level an exponentially small tail still lies inside the exact
  causal support, so "operationally invisible" may **not** be asserted.
- No new model, no Bernstein/paraunitary/novelty line
  (`CURRENT_STATE.md` Sec. 8.7).

## 6. Closure

This is a documentation gate. On passing Sec. 3 and recording Secs. 1 and 4,
the subline is **CLOSED**.
