# B_STAR_HYPOTHESIS

## 1. Motivation

The original strong thesis identified the relativistic low-energy speed with the maximum microscopic speed of the substrate. That thesis fails generically for anisotropic finite-range lattice QCAs in spatial dimension `d >= 2`.

A weaker geometric candidate remains:

`B*: c_IR = r_in(C_micro)`.

Interpretation: the relativistic speed is the largest isotropic causal speed compatible with every microscopic direction.

## 2. What B* does and does not say

B* does **not** say that `c_IR` equals the fastest microscopic direction.

B* does **not** say that the IR cone equals the entire microscopic causal body.

B* says only that the isotropic IR velocity ball is maximally inscribed in the microscopic causal body.

## 3. Current evidence

**STANDARD WEYL/DIRAC EXACT GATE: PASS.** The derivation, verifier, contract
and provenance at `2c7c2c9` establish `c_0 = r_in = 1/sqrt(d)` for the
declared standard massless family in d=1,2,3, in unit-neighbor and unit-time
coordinates. See the [canonical state](../state/CURRENT_STATE.md) and
[promotion record](../reports/2026-09-14--standard-gate-promotion.md).

The seven symbols include transpose/chirality partners sharing geometry and
linear speed. They cover three dimension-specific geometries, not seven
independent tests of generality. No theorem for a general class follows.

## 4. Massive warning

For the standard Dirac couplings and every `0 < m < 1`, define
`F = arcsin(m) sqrt(1-m^2)/m`. The exact result is

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`, with `0 < F < 1`.

This is an established result for the declared family, no longer preliminary.
The quadratic mass-direction Hamiltonian correction accounts for the exact
discrepancy between the two extraction procedures.

Therefore the unrestricted statement

`c_IR(m) = r_in(C_micro) for all m`

is **REJECTED IN THE STANDARD DIRAC FAMILY** under either specified
finite-mass extraction. At m=1 the active support collapses; treat that endpoint
separately rather than extending the strict inequalities to it.

The live restricted forms are:

### B*_0 — massless matching

`c_0 = r_in(C_micro)`.

**VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN.**

### B*_cont — continuum/small-mass matching

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in(C_micro)`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN.** The continuum
scaling and local convergence scope are fixed in the exact-gate report.

These are logically distinct. In the declared standard family, continuum
matching holds while exact finite-mass matching fails.

## 5. Required mechanism

A successful explanation must do more than fit a known coefficient. It must explain why, once the microscopic neighbor geometry and normalization are fixed, the EFT selects the inradius rather than a smaller isotropic speed.

A candidate derivation should identify which assumptions are essential among:

- locality;
- unitarity;
- homogeneity;
- discrete isotropy;
- minimal internal dimension;
- analyticity / smooth low-energy branch structure;
- massless versus massive sector.

## 6. Falsifiers

B*_0 is falsified for a class by one member whose exact, nonzero, isotropic
massless coefficient is strictly below its microscopic inradius. The active
front is [MASSLESS INRADIUS RIGIDITY GATE](MASSLESS_INRADIUS_RIGIDITY_GATE.md):
retain the selected standard neighborhood, causal body, normalization,
unitarity, homogeneity and discrete isotropy. Freeze the internal dimension,
symmetry representation and massless sector before solving.

An exhaustive proof for one fixed class is a class-specific rigidity result;
a failed search or a test of equivalent representatives is not. Added
minimality or irreducibility assumptions must remain explicit in the conclusion.

B*_cont is falsified if a valid massive family has a small-mass/continuum limit whose relativistic speed does not approach the microscopic inradius.

A failure is scientifically useful: it identifies which extra structural principle, if any, is missing.
