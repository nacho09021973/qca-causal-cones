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