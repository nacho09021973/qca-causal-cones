# IG-S2 — fixed N-type ground-reference candidate

Date: 2026-10-08
Branch: `research/inverse-gravity-design`
Parent: [inverse-gravity design charter](INVERSE_GRAVITY_DESIGN_CHARTER.md)
Status: `REFUTED_AS_EXACT_GROUND_REFERENCE`

Author-side correction (2026-10-08): the first execution at `edf54ff`
misread the trace cosine in H_J. The linked execution report now contains
the repaired q=3 proof, retaining the failed proof's commit as provenance.
The candidate frozen at `801bc0e` is unchanged; no independent review is
claimed. This exact-reference test is one possible method, not a necessary
prerequisite for every excitation bound.

## 1. Question

Does the following fixed reference state provide the exact finite-volume ground
state, or a sufficiently sharp lower-energy reference, for the complete Gu–Wen
N-type Hamiltonian

\[
H_N(L)=H_U(L)+H_J(L)+H_g(L)
\]

in the original regime \(\tilde U\sim\tilde J\sim\tilde g\)?

This contract fixes one candidate only. It does not assert that the candidate
is an eigenstate, a ground state, or a tensor vacuum.

## 2. Frozen microscopic domain

- Periodic primitive-cell torus \(\Lambda_L=(\mathbb Z/L\mathbb Z)^3\), with
  \(L\ge3\) so the nearest-neighbour stencil offsets remain distinct.
- Six qutrit registers per primitive cell, ordered
  \(xx,yy,zz,xy,yz,zx\), with \(n_G=3\).
- Clock algebra \(X|n\rangle=|n+1\pmod3\rangle\),
  \(Z|n\rangle=\omega^n|n\rangle\),
  \(\omega=e^{2\pi i/3}\), and \(ZX=\omega XZ\).
- The scalar and vector constraint operators are exactly the stencils frozen
  in `INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md`; all offsets are reduced modulo
  the periodic torus.
- No change of \(n_G\), coupling hierarchy, stencil, boundary condition,
  Hamiltonian term, or Hilbert-space representation is permitted under this
  contract.

## 3. Candidate definition

Let \(|0_L\rangle\) be the product state with every momentum register in the
\(L^{ab}=0\) eigenstate. Therefore every vector constraint has eigenvalue one:

\[
V(i,i+a)|0_L\rangle=|0_L\rangle.
\]

Define the scalar projector

\[
P_S(L)=\prod_{i\in\Lambda_L}
       \left(\frac13\sum_{m=0}^{2}S(i)^m\right),
\]

where the product is well-defined because the scalar constraints commute. The
frozen normalized candidate is

\[
|\Omega_L\rangle=
\frac{P_S(L)|0_L\rangle}{\|P_S(L)|0_L\rangle\|}.
\]

The candidate is defined only when the denominator is nonzero. Under the
frozen qutrit stencils it is nonzero: the scalar operators are products of
shift operators, and the orbit sum contains the nonzero identity-orbit
component. This existence statement is about the constraint projector, not
about \(H_N\).

## 4. Exact properties intended for verification

The following are obligations, not assumed properties:

1. `CONSTRAINT_PASS`: \(S(i)|\Omega_L\rangle=|\Omega_L\rangle\) and
   \(V(i,i+a)|\Omega_L\rangle=|\Omega_L\rangle\) for every admissible site
   and direction.
2. `EIGENSTATE_OR_REFUTED`: **refuted for \(J>0\)**; see the execution report
   `reports/2026-10-08--inverse-gravity-ground-reference-refutation.md`.
3. `GROUND_LOWER_BOUND_OR_REFUTED`: determine whether there is a controlled
   bound \(H_N(L)-e_L\mathbf1\ge0\), or a lower bound whose error relative to
   the candidate is \(O(1/L)\) in the excitation estimate.

Only item 1 follows from the already frozen constraint algebra. Item 2 is
refuted for this candidate. Item 3 is not evaluated as a separate
lower-bound problem because failure of the eigenstate condition already
rejects this reference as the exact ground state. The refutation is not a
statement about other references or about all N-type ground states.

## 5. Exclusions

This candidate is not identified with:

- the exact ground state of \(H_N\);
- the ground state of \(H_U\) being sufficient for the full Hamiltonian;
- the finite-volume trace state \(P/\operatorname{Tr}P\);
- a TT-projected state;
- a state with two physical tensor polarizations;
- evidence for a gapless mode, \(z=1\), or emergent gravity.

No finite-size diagonalization or exploratory scan is authorized by this
contract. Any computation producing a retained result requires a permanent
verifier and a separate execution report.

## 6. Result and remaining obligation

The exact-ground-state statement is refuted for \(J>0\):

\[
H_N(L)|\Omega_L\rangle\ne e_L|\Omega_L\rangle
\quad\text{for every scalar }e_L.
\]

The repaired proof uses the exact compact operators and the q=3 diagonal
energies of the complete \(H_J\), including its negative trace-cosine term.
This refutes this candidate as an exact ground-state
reference; it does not refute the N-type Hamiltonian or all possible ground
references. Alternatives include a different controlled reference or a
ground-state commutator method that eliminates the absolute ground energy.
See the five-method preflight in
`reports/2026-10-08--ig-s2-five-ground-energy-methods.md`.
