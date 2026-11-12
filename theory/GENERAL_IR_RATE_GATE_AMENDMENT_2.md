# Amendment 2 to the general infrared operational rate charter — DRAFT

2026-11-12. Drafted by Claude (claude-opus-5-5). **Status: DRAFT; not in
force until approved by the user.** The frozen charter
(`GENERAL_IR_RATE_GATE.md`, `aa6c5f6`) and Amendment 1 (`91be396`) are not
edited.

## Reason

Before starting Stage 2(A) every input of manuscript Sec. 7 was checked for
what it needs in a general walk of the class. Three non-degeneracy
conditions are used there and are not implied by H1–H5, H4′, H6. They
should have been listed with Amendment 1; they were found after it and are
declared so. For two of them (H7, H8) a failure makes the leading term
vanish or decay at a strictly larger rate, so they are not artefacts of
the method: a walk violating them is a candidate for outcome (a), which
stays outside this charter.

## Changes

- **H7 (Alice's boundary value).** `Phi_0(w_A) != 0`, where
  `Phi_0(w) = c_r int g(q) e^(-i q.w) d^d q` is the resource profile
  (manuscript Eq. (7) in dimension `d`) and `w_A` is Alice's facing point,
  the point of `A` maximising `xi_*.w`. In manuscript notation this is
  `phi_partial != 0`. Sufficient: `|w_A| < pi` for `d = 3`, `|w_A| < j_{0,1}`
  (about 2.405) for `d = 2`, because the radial integrand is then positive.
- **H8 (smooth rate at the dual point).** `Phi` is differentiable at
  `xi_*`. Equivalently, every dominant branch active at `xi_*` has
  `grad_xi log|lambda| = v_*`. If the zero-momentum branch had another
  gradient, its contribution would carry the phase `e^(i N eta.(g_0 - v_*))`
  and, after the Gaussian integral, be exponentially smaller than
  `e^(-K_* N)`.
- **H9 (arithmetic of the depth offsets).** Let `u` be the primitive normal
  of H3 and `theta^A_N = {N u.w_A}`, `theta^B_N = {-N u.w_B}`, with `w_B`
  Bob's facing point, the fractional depth offsets of the first lattice
  plane in each region. Require one of: (i) `1, u.w_A, u.w_B` rationally
  independent; (ii) `theta^A_N = theta^B_N` for all `N`, with `u.w_A`
  irrational.

## Why H9 is enough (to be proved in Stage 2, stated here so the condition is not chosen after the fact)

The leading depth factor is `Gamma_0(theta^A, theta^B) =
int W(tau) S_A(tau; theta^A) S_B(tau; theta^B) dtau`, with `W` a positive
Gaussian weight and `S_A`, `S_B` real depth sums. Poisson summation in the
depth index writes each `S` as a Fourier series in its offset whose
coefficients are Gaussians in `tau` divided by `(t_* + i omega)^(d+1)`.
Under (i) the average of `Gamma_0` over `N` keeps only the zero mode, a
positive integral. Under (ii) it keeps the diagonal modes, each with
positive real part. In both cases the average is positive, so
`Gamma_0(theta^A_N, theta^B_N)` is bounded away from zero on a set of `N`
of positive density, which is what the limsup form of (T) needs. K3
satisfies (ii) with `u.w_A = sqrt(3)/4`.

## What stays the same

Class, protocol family, stages, budget, verdicts, stop rules and the
result that ends the line. K3 satisfies H7 (`phi_partial = c_r I_b > 0`),
H8 (all eight dominant points share the gradient, manuscript Lemma 7.1(b))
and H9(ii).

## Effect

The amended theorem is a statement under a list of checkable
non-degeneracy conditions (H1–H3, H4′, H5–H9), in the style of the ACSV
transfer theorems. Rational offset relations other than (ii) are left to
Stage 3.
