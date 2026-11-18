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

The strongest isotropic cone compatible with the *one-step* microscopic causal body has radius exactly `r_in`.

**Correction (2026-09-14):** `r_in(C_micro)` is only an upper bound, and it
bounds the one-step body, not the propagation actually achievable after
repeated time steps. The object that should be compared against `c_IR` is the
*strict asymptotic* isotropic speed `c_strict^iso = min h_infty`, defined from
the actual long-run Fourier support in
[`CAUSAL_BODY_GEOMETRY.md`](CAUSAL_BODY_GEOMETRY.md) Sec. 6, which satisfies
`c_strict^iso <= r_in(C_micro)` in general and need not be an "inradius" at
all (a pure shift gives a negative value). The live hypothesis is therefore

`B_infty^*: c_0 = c_strict^iso`,

not the old `c_IR = r_in(C_micro)`. The standard Pavia Weyl family in d=3 is
the one baseline where the two targets are certified to coincide exactly
(`c_strict^iso = r_in = 1/sqrt(3)`); see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
See `B_STAR_HYPOTHESIS.md` for current status.

## 6. Tachyonic-sector diagnostic (2026-11-18; exploratory)

**Status: PRELIMINARY algebraic observation / OPEN for interacting sectors.**
This is a documentary consistency check, not a new gate, executed verifier,
independent review, or promotion. **NOVELTY = OPEN.**

- **Known:** the Thirring rule is `U = FJ`, and the one-particle sector
  is free because the on-site two-particle phase `J` acts trivially there.
  The one-particle walk is recorded in
  [the massive preflight](../reports/2026-11-08--thirring-massive-preflight.md),
  Sec. 1. The distinctions among microscopic support, spectral group speed,
  and IR speed are fixed in Secs. 1-4 above.
- **Question:** does this *fixed* one-particle rule exhibit a tachyonic
  low-energy branch, or a group velocity outside its microscopic cone?
- **Stop rule:** if the proposed branch requires a nonunitary parameter
  continuation or is absent from the declared one-particle spectrum, stop
  this check; do not extrapolate to collective/unstable backgrounds or
  introduce another automaton without a separate user-chartered gate.

In lattice units `a = Δt = 1`, with real `0 <= μ <= 1` and
`ν = sqrt(1-μ²)`, the fixed Bloch walk is

```text
W(k) = [[ν exp(ik), -i μ], [-i μ, ν exp(-ik)]],
cos ω(k) = ν cos k,              0 <= ω(k) <= π.
```

Consequently both unitary eigenphases are real. At differentiable points,

```text
|v_g(k)| = |ν sin k| / sqrt(1 - ν² cos² k) <= ν <= 1.
```

The inequality follows from `1 - ν² cos² k >= 1 - cos² k`;
the massless degeneracies are interpreted by one-sided band velocities.
For `0 < μ <= 1`, the gap at `k = 0` is
`ω(0) = arccos(ν) = arcsin(μ) >= 0`. Thus this branch does **not**
realize an imaginary-frequency region corresponding to the naive
continuum tachyonic form `ω² = c_eff² k² - κ²` near `k = 0`
for `κ > 0`. This is a statement about this branch, not a general
no-tachyon theorem for QCA.

A group speed exceeding a specifically defined effective `c_IR` would
not alone establish superluminal signaling: it must be compared with
`C_micro` and its actual strict causal support. In a massive lattice
sector, `c_H` and `c_{ω²}` must first be distinguished (Sec. 3).
Tachyonic effective instabilities around a many-body background, if any,
are **OPEN / NOT TESTED** here. No interacting spectrum, continuation,
numerics, or new particle species has been introduced.
