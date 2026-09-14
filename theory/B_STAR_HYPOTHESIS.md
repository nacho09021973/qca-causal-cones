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

For the standard isotropic massless Weyl QCAs discussed in the Pavia literature, the low-momentum coefficients in two and three spatial dimensions match the inradius factors associated with the normalized neighbor polytopes used in the present embedding:

- `d = 2`: candidate `c_IR = 1/sqrt(2)`;
- `d = 3`: candidate `c_IR = 1/sqrt(3)`.

This is evidence for a massless matching mechanism, not a theorem of the class.

## 4. Massive warning

The standard Dirac construction couples two Weyl automata with a dimensionless lattice mass parameter. A preliminary exact-phase calculation indicates that finite lattice mass reduces the spatial coefficient of the interpolating Hamiltonian below the massless inradius value.

Therefore the unrestricted statement

`c_IR(m) = r_in(C_micro) for all m`

is not currently viable.

The live restricted forms are:

### B*_0 — massless matching

`c_IR(m = 0) = r_in(C_micro)`.

### B*_cont — continuum/small-mass matching

`lim_{m_lattice -> 0} c_IR(m_lattice) = r_in(C_micro)`.

These are logically distinct. `B*_cont` can survive even if exact finite-mass `B*` fails.

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

B*_0 is falsified by one valid finite-range QCA satisfying the intended symmetry assumptions whose exact massless relativistic coefficient is strictly below its microscopic inradius.

B*_cont is falsified if a valid massive family has a small-mass/continuum limit whose relativistic speed does not approach the microscopic inradius.

A failure is scientifically useful: it identifies which extra structural principle, if any, is missing.