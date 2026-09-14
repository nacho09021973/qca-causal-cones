# CURRENT_STATE

**Date:** 2026-09-14  
**Status:** INITIAL FREEZE — NO SCOPE EXPANSION  
**Repository:** `nacho09021973/qca-causal-cones`

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Live hypotheses

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

### B* — inradius matching

Candidate:

`c_IR = r_in(C_micro)`.

Interpretation: `c` would be the largest isotropic causal speed compatible with every microscopic direction, not the largest microscopic directional speed.

**Status: TOO STRONG IF ASSERTED FOR ALL MASSIVE FINITE-LATTICE SECTORS; LIVE IN RESTRICTED FORM**

Current restricted versions:

- `B*_0`: exact matching in the massless sector;
- `B*_cont`: matching in the relativistic continuum / small dimensionless lattice-mass limit.

Both remain to be tested systematically.

## 5. Pavia-family evidence

Primary sources to check are recorded in `sources/README.md`.

### Massless Weyl

For the standard isotropic Weyl automata, the published low-`k` coefficients in `d = 2, 3` match the inradius of the normalized microscopic neighbor polytope under the embedding used in the current discussion:

- `d = 2`: candidate factor `1/sqrt(2)`;
- `d = 3`: candidate factor `1/sqrt(3)`.

**Status: SUPPORTED; MUST BE RE-DERIVED WITH NORMALIZATION FROZEN IN THE CURRENT GATE**

### Massive Dirac

For the standard block coupling

`U_k = [[n A_k, i m I], [i m I, n A_k^†]]`, with `n^2 + m^2 = 1`,

a preliminary derivation gives, if the Weyl phase is `θ(k)`,

`cos ω_D(k) = n cos θ(k)`.

Writing `M := ω_D(0) = arcsin(m)`, the preliminary spatial coefficient of the interpolating Hamiltonian is

`c_H(m) = r_in * sqrt(1-m^2) * arcsin(m) / m`

or

`c_H / r_in = M cot M`.

For `0 < m < 1`, this is strictly below 1, with expansion

`c_H / r_in = 1 - m^2/3 - 2 m^4/15 + O(m^6)`.

The coefficient inferred from the `k^2` term of `ω_D^2` is preliminarily

`c_{ω^2} = r_in * sqrt(M sqrt(1-m^2) / m)`,

which differs from `c_H(m)` at finite lattice mass.

**Status: PRELIMINARY — NOT YET CANONICAL THEOREM. MUST BE RECHECKED FROM THE EXACT PUBLISHED AUTOMATON AND BRANCH CONVENTIONS.**

If confirmed, exact finite-mass `B*` fails while `B*_0` / `B*_cont` survive as the relevant candidates.

## 6. Current scientific interpretation

The live idea is no longer:

`c = maximum microscopic speed`.

The live geometric possibility is:

`c_massless/continuum = largest isotropic speed compatible with the microscopic causal body = r_in(C_micro)`.

Whether this is forced by locality + unitarity + discrete isotropy, or is merely a feature of the Pavia construction, is unknown.

## 7. NEXT GATE — only allowed calculation

Complete an exact Weyl/Dirac battery before opening any new substrate class.

For every available Pavia case in `d = 1, 2, 3`:

1. freeze the generator/neighbor set and coordinate normalization;
2. compute `C_micro`, `h_C`, `r_in`, and `V_causal^max`;
3. write the exact Bloch unitary;
4. derive eigenphases exactly;
5. derive the low-energy interpolating Hamiltonian;
6. record the massless `c_IR`;
7. for Dirac mass `m`, compare `r_in`, `c_H(m)`, and `c_{ω^2}(m)`;
8. classify each equality as exact, asymptotic, false, or convention-dependent.

### Stop rule

Until this gate closes:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO novelty claim for B***;
- **NO use of a scalar `v_max` without definition**.

A clean falsification of `B*_0` or `B*_cont` is a successful project outcome.