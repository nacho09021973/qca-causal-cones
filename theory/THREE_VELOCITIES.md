# THREE_VELOCITIES

## Purpose

This note fixes the vocabulary for propagation speeds in the project.

## 1. Microscopic causal geometry

For a finite one-step displacement set `N`, define

`C_micro = conv(N)`.

This is the primary causal object in more than one spatial dimension. It records which average velocities are geometrically compatible with repeated local moves.

For direction `n̂`, the support function is

`h_C(n̂) = sup_{v in C_micro} n̂·v`.

The directional causal speed is proportional to `h_C(n̂)` after restoring lattice/time units.

Two scalar summaries are useful but secondary:

- inradius: `r_in = min h_C`;
- maximal directional support: `V_causal^max = max h_C`.

## 2. Spectral group velocity

Let the Bloch unitary have eigenvalues

`exp[-i ω_s(k) Δt]`.

The group velocity of branch `s` is

`v_s(k) = ∇_k ω_s(k)`.

Define

`V_grp^max = sup_{s,k} ||v_s(k)||`.

This quantity belongs to the spectrum of a specific QCA. It is not identical by definition to the geometric boundary of `C_micro`.

## 3. Relativistic IR speed

`c_IR` belongs to the low-energy effective theory.

For a gapless node with isotropic linear dispersion,

`ω(k) = c_IR |k| + higher orders`,

so `c_IR` is the low-energy slope.

For a massive relativistic EFT,

`H_eff(k) = M β + c_IR α·k + ...`,

or, in the exact continuum relativistic form,

`ω^2 = M^2 + c_IR^2 |k|^2`.

On a finite lattice, higher-order Hamiltonian terms can contribute to the `|k|^2` coefficient of `ω^2`, so the two extraction procedures must be checked rather than assumed equivalent.

The completed standard Dirac gate establishes a strict difference for
`0 < m < 1`: with `F = arcsin(m) sqrt(1-m^2)/m`,
`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`.
The quadratic mass-direction correction satisfies
`c_H^2 + 2 M b = c_{ω^2}^2`, where `M = arcsin(m)` and
`b = r_in^2 sqrt(1-m^2)(1-F)/(2m)`.

Thus an unspecified finite-lattice `c_IR` is ambiguous between these
extractions. Their common massless/continuum limit is verified for the standard
family; see the [canonical state](../state/CURRENT_STATE.md) for the claim ceiling.

## 4. Safe inequalities and unsafe identifications

The robust locality statement is that spectral propagation cannot outrun the microscopic causal geometry. In one dimension this reduces to a scalar Bernstein-type bound.

Unsafe universal identifications include:

`c_IR = V_grp^max`,

`V_grp^max = V_causal^max`,

and therefore

`c_IR = V_causal^max`.

Each equality requires an independent mechanism or proof.

## 5. Current geometric candidate

If the IR cone is isotropic and must fit inside `C_micro`, then

`c_IR <= r_in(C_micro)`.

The strongest isotropic cone compatible with the microscopic causal body has radius exactly `r_in`.

This motivates, but does not prove, the restricted hypothesis

`B*: c_IR = r_in(C_micro)`.

See `B_STAR_HYPOTHESIS.md` for current status.
