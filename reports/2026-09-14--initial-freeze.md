# Initial freeze — 2026-09-14

## Why this repository exists

The discussion had accumulated enough definitions, negative results, and competing versions of the substrate-speed hypothesis that continuing only in chat risked terminology drift. This freeze records the state before any further model search.

## Frozen conclusions

1. Finite-range locality supplies a microscopic causal body, not automatically the relativistic speed.
2. Spectral group velocity is a separate object belonging to a specific QCA.
3. The relativistic low-energy speed belongs to the EFT and must be extracted appropriately for gapless versus massive sectors.
4. Classical Bernstein theory supplies a derivative/group-velocity bound; the bound itself is not novel.
5. The old statement `c_IR = maximum microscopic speed` fails generically for an anisotropic finite-range lattice causal body in `d >= 2`.
6. Exact equality between an isotropic IR ball and a finite microscopic polytope is geometrically impossible in `d >= 2`.
7. Tangency of an isotropic IR ball to the microscopic causal body is a weaker statement and motivates the inradius candidate `B*`.

## Live questions

### A — IR universality

Why should different species share one effective relativistic cone?

### B* — inradius selection

Why should the massless or continuum relativistic speed equal the inradius of the microscopic causal body rather than some smaller value?

## Pavia status at freeze

The massless Weyl coefficients in the standard isotropic 2D/3D automata appear to match the corresponding normalized inradii (`1/sqrt(2)` and `1/sqrt(3)`). This is treated as supported evidence pending a normalization-controlled rederivation.

A preliminary calculation for the massive Dirac block automaton indicates finite lattice mass lowers the Hamiltonian spatial coefficient below the massless inradius value. This calculation is explicitly **not yet promoted to an established result**.

## Next gate

The only allowed science step is an exact Weyl/Dirac battery over the available `d = 1,2,3` cases:

- freeze neighborhood geometry and coordinate normalization;
- compute causal-body support and inradius;
- derive exact Bloch eigenphases;
- derive the low-energy interpolating Hamiltonian;
- compare massless and massive speed parameters against the inradius;
- classify equality as exact, asymptotic, false, or convention-dependent.

Until that gate closes, do not generalize to causal sets or other substrate classes.
