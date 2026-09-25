# CAUSAL_BODY_GEOMETRY

## 1. Finite-range lattice locality

Let `N = {n_1, ..., n_m}` be the finite set of one-step lattice displacements allowed by locality. Ignoring internal amplitudes, repeated paths after `Nstep` steps lie in the Minkowski sum of the one-step support. After dividing by the number of steps, the asymptotic geometric velocity body is the convex hull

`C_micro = conv(N)`

up to the physical scale `a/Δt` (or the appropriate anisotropic coordinate scales).

For finite `N`, `C_micro` is a polytope.

## 2. Support function

For a unit direction `n̂`,

`h_C(n̂) = sup_{v in C_micro} n̂·v`.

The convex body can be recovered as

`C_micro = intersection over n̂ of {v : n̂·v <= h_C(n̂)}`.

Define

`r_in(C_micro) = min_{||n̂||=1} h_C(n̂)`

when the origin and Euclidean norm are fixed by the same velocity coordinates used for the proposed isotropic IR cone.

Also define

`V_causal^max = max_{||n̂||=1} h_C(n̂)`.

## 3. Isotropic IR containment lemma

Suppose an isotropic low-energy causal ball

`B(c_IR) = {v : ||v||_2 <= c_IR}`

must be contained in `C_micro`.

Then for every unit `n̂`,

`c_IR <= h_C(n̂)`.

Hence

`c_IR <= min h_C = r_in(C_micro)`.

If `C_micro` is anisotropic, then

`min h_C < max h_C`,

so

`c_IR < V_causal^max`.

This rules out identifying an isotropic `c_IR` with the largest directional microscopic speed in an anisotropic causal body.

## 4. Three old saturation statements

- `B_max`: `c_IR = V_causal^max`.
- `B_full`: `B(c_IR) = C_micro`.
- `B_touch`: `∂B(c_IR)` intersects `∂C_micro`.

For an anisotropic `C_micro`, `B_max` is impossible under isotropic containment.

For finite-range lattice QCA in `d >= 2`, exact `B_full` is impossible because `C_micro` is a finite polytope whereas a nondegenerate Euclidean ball is not.

`B_touch` can still hold and, for a centered isotropic ball, corresponds to

`c_IR = r_in(C_micro)`.

Tangency is therefore much weaker than “`c` is the fastest speed of the substrate.”

## 5. Scope of the lemma

The statement is geometric. It assumes:

- a fixed embedding/velocity coordinate system;
- a Euclidean isotropic IR cone in those coordinates;
- containment of the IR velocity ball inside the microscopic causal body.

Changing coordinates or the norm changes the numerical inradius. Therefore every comparison must freeze the physical embedding before computing `r_in`.

## 6. Strict asymptotic support and `c_strict^iso` (added 2026-09-14)

`C_micro = conv(N)` is the *one-step* body: it only records which average velocities are compatible with a single update. It says nothing about whether a given direction is actually reachable arbitrarily far after repeated coarse-graining in time — that depends on whether the relevant Fourier coefficients survive under repeated multiplication, not on `N` alone.

For a homogeneous step `U(k) = sum_h e^{-ik.h} T_h` and `n >= 1`, let

`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`.

Define the **strict asymptotic support function**

`h_infty(n̂) = limsup_{n->infty} (1/n) max_{x in S_n} n̂.x`,

and, with the origin fixed at the physically privileged rest point `v = 0`,

`c_strict^iso = min_{||n̂||=1} h_infty(n̂)`.

Since `S_n/n subseteq C_micro` for every `n` (each one-step displacement lies in `C_micro` by definition), `h_infty(n̂) <= h_C(n̂)` for every `n̂`, hence

`c_strict^iso <= r_in(C_micro)`.

This is the exact and general relation between the two objects: `r_in(C_micro)` is a provable *upper bound* on the strict asymptotic isotropic speed, not a definition of it, and the two need not coincide. A pure one-step shift by `h_0 != 0` (`S_n = {n h_0}`) gives `h_infty(n̂) = n̂.h_0` and `min_{n̂} h_infty(n̂) = -||h_0|| < 0`: there is no bidirectional isotropic cone centered at `v=0` at all, which "inradius" language silently assumes. Do not call `c_strict^iso` an inradius except where a separate argument shows the relevant body is centered and `c_strict^iso = r_in(C_micro)` exactly.

The live hypothesis built on this object, `B_infty^*`, and the exact d=3 Pavia baseline in which `c_strict^iso = r_in(C_micro) = 1/sqrt(3)` is certified (not merely bounded), are in [`B_STAR_HYPOTHESIS.md`](B_STAR_HYPOTHESIS.md) and
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).