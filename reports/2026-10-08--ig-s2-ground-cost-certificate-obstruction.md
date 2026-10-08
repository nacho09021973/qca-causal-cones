# IG-S2 — obstruction to curvature-only ground-cost certificates

Date: 2026-10-08. Branch: `research/inverse-gravity-design`.
Preregistration: `db2e5f6`,
`theory/INVERSE_GRAVITY_GROUND_COST_CERTIFICATE_GATE.md`.
Evidence: author-side analytic derivation, not independent review.

## Outcome

`RESTRICTED_GROUND_CERTIFICATE_CLASS_FAIL / NTYPE_GROUND_COST_OPEN`.

There is an exact ground-energy-independent certificate principle. However,
tests restricted to the common commutant of H_U and H_g cannot certify a small
curvature numerator: the momentum-zero product state satisfies every such
test and has a strictly positive, volume-independent numerator. This is a
counterexample to sufficiency of the restricted tests, not a computation in
the true N-type ground space and not a no-go for N-type soft modes.

## 1. Fixed model and observable

Use the preceding q=3 curvature pair, even periodic tori, and unchanged
positive comparable couplings. Let H=H_U+H_J+H_g, P0 its complete ground
projector and rho0=P0/Tr(P0). The observable of interest is the Hermitian
double-commutator matrix at zero envelope momentum. For a real unit vector
z in the two probe directions, put

\[
 B_z=z_+ B_+(0)+z_\times B_\times(0),\qquad
 O_z=[B_z,[H,B_z]]=[B_z,[H_J,B_z]].
\]

Its true-ground expectation is z^T D_R(0) z. The finite-support expansion
from the parent report writes this as the translation average of a local
Hermitian observable; taking the Hermitian part of that local expression
does not change the average. Thus it is an intensive certificate target,
not an extensive approximation to E0.

Primary source inspected this session: `biblioteca/arXiv-0907.1203.pdf`,
Gu-Wen v3, p.18 (full N-type terms) and p.19 (the stated approximation caveat).
The source fixes the Hamiltonian, not the certificate principle below.

## 2. A sufficient certificate that cancels E0

For any operator A define the Hermitian local ground-cost operator

\[
 T_A=\tfrac12\{A^\dagger[H,A]+[A^\dagger,H]A\}.
\]

For every density rho supported on the complete ground space,

\[
 \operatorname{Tr}\rho T_A
 =\operatorname{Tr}\rho A^\dagger(H-E0)A\ge0,
 \qquad \operatorname{Tr}\rho i[H,Y]=0\quad(Y=Y^\dagger).
\]

Proof: expand both commutators and use H rho=rho H=E0 rho.
The first equality follows term by term; positivity uses H-E0>=0.
The second equality is cyclicity of trace. For local A, only Hamiltonian
terms meeting its support contribute to [H,A]; E0 never enters the
operator T_A. Hermiticity follows by taking the adjoint of the first term.

An exact operator identity of the form

\[
 \epsilon I-O_z=\sum_r C_r^\dagger C_r
                +\sum_s w_s T_{A_s}+i[H,Y],\qquad w_s\ge0,
\]

would imply Tr(rho O_z)<=epsilon. The same identity with O_z-delta I on
the left would give a lower bound delta. Translation averages of local
identities, and lattice divergences with zero periodic sum, are allowed.
For a matrix upper bound the identity must hold for all probe directions,
for instance as a positive block-operator identity; checking two diagonal
entries alone is not sufficient.

This is only a sufficient principle. No identity with a small epsilon or
positive delta has been obtained for the full N-type ground cost.

## 3. First obstruction: individual unitary tests cannot give a positive lower bound

If A is unitary, then T_A=A^dagger H A-H and its full Hilbert-space trace
vanishes. The trace of O_z also vanishes, as does the trace of i[H,Y].
Consequently an identity

\[
 O_z-\delta I=\sum_r C_r^\dagger C_r
             +\sum_s w_s T_{U_s}+i[H,Y],\quad U_s^\dagger U_s=I,
\]

with delta>0 is impossible: its left trace is -delta dim(H), whereas the
right trace is nonnegative. Periodic divergences do not change this.
This excludes this particular dual certificate class, not every lower-bound
proof. Nonunitary variations or coherent combinations of Weyl words need
not have zero trace and are not excluded by this argument.

Second formulation: the normalized tracial density obeys each individual
unitary-cost inequality and every stationarity condition, and has zero O_z
expectation. Such tests alone cannot force a positive lower expectation.

## 4. Stronger obstruction: all variations in the potential commutant miss state selection

Let C be the algebra of operators commuting with both H_U and H_g. It
contains every fixed curvature word and every polynomial in those words.
Let omega=|0_L> be the product state with all momenta zero. At q=3,

\[
 H_J=3\widetilde J\left[\sum_{i,a}f(L^{aa}_i)
 +2\sum_{i,ab}f(L^{ab}_i)
 -\tfrac12\sum_i f\Big(\sum_aL^{aa}_i\Big)\right],
 \quad f(t)=\tfrac32\mathbf1_{t\not\equiv0\pmod3}.
\]

H_J>=0 and H_J omega=0. Indeed, at a diagonal vertex with m nonzero
diagonal momenta its contribution inside the brackets is
(3/2)(m-(1/2)1_{sum L!=0}). It vanishes at m=0 and is at least 3/4 when
m>=1. The off-diagonal contributions are nonnegative.

For every A in C, including nonunitary coherent combinations,

\[
 \langle\omega,T_A\omega\rangle
 =\langle\omega,A^\dagger H_J A\omega\rangle\ge0.
\]

Proof: [H,A]=[H_J,A], then use H_J omega=0 on both sides of the symmetrized
expression. Likewise, for Hermitian Y in C,
<omega,i[H,Y]omega>=<omega,i[H_J,Y]omega>=0.
The product state is translation invariant and real as well.

It therefore satisfies *all* the necessary ground conditions used by this
restricted certificate class, even though it is not being admitted as a
true H_N ground state. Increasing the range or number of tests within C
does not cure this issue.

For the fixed probes the independently entered sparse-word costs give

\[
 \langle\omega,O_z\omega\rangle
 =\widetilde J\left(\tfrac{207}{4}z_+^2+54z_\times^2\right).
\]

Reproduction this session: `python3 -B
scripts/verify_inverse_gravity_curvature_probes.py`, exit 0, SymPy 1.14.0,
unchanged permanent code. It checks L=4,6 signed-word costs and collisions;
the all-volume argument is the sparse-support distinction below, not finite
extrapolation. R_xx/R_yy have four off-diagonal nonzero registers, giving
36 J, and six diagonal registers: their diagonal contribution is 27 J and
their five nonzero vertex traces subtract 45 J/4, giving 63 J/4;
total 207 J/4. R_xy has eleven off-diagonal nonzero registers,
giving 99 J, and four diagonal registers, giving 9 J; total 108 J.
At q=3 the central coefficient 2 and endpoint coefficients 1 distinguish
the axial three-register support for each species on even L>=4. The xx/yy
words are distinguished by diagonal species; the xy word uses only zz
diagonal species. Their translations and inverses are distinct. Hence
the normalized sine sums have no cross-word matrix elements in omega.
Since H_J omega=0, the double commutator equals twice the kinetic norm;
this gives the displayed diagonal expectation, independent of momentum.

Evaluating the proposed upper-bound identity in omega now proves that,
if every A_s and Y lies in C, epsilon must be at least the displayed
constant for its chosen z. In particular no epsilon tending to zero is
possible. This obstruction uses the actual unchanged H_N operator in the
tests; it does not change any coupling or substitute H_J as the physical
Hamiltonian.

Its second formulation is feasibility: omega defines a positive normalized
functional satisfying the entire restricted ground-test family but violating
the desired small-cost bound. Thus any relaxation with precisely those tests
must retain this counterexample. Positivity tests C_r^dagger C_r cannot
exclude a genuine density matrix.

## 5. Precision correction and claim ceiling

The earlier report's momentwise sufficient route requires
||M_j(L)||=O(p_L^(4-j)). Within that route M0 requires O(L^-4).
This is not a necessary theorem for D_R(p_L)=O(p_L^4) alone: L-dependent
coefficients can cancel at the specific sampled momentum. The previous
final answer's wording "needs" must be read with this stronger-route scope.
Nor is a quartic numerator necessary for every possible spectral quotient.

What has actually failed is a proposed *class of certificates* that omits
the potential's state-selection information. No bound on an unknown true
ground expectation has been obtained. The actual ground cost, Gram,
degeneracy, tensor admission and spectral gate remain OPEN.

## 6. Single next obligation

Any continuation of the local ground-test route must supply one explicit
finite-support mixed angle/momentum variation outside C that excludes
omega by stationarity or the ground-cost inequality for the unchanged H_N.
Its support, coefficients and exact violation must be stated before a
verifier is introduced. This would only establish that the relaxation
detects the potential's selection of the state; it would not yet give the
required N-type bound. No SDP scan, new vacuum ansatz or further architecture
was opened in this execution.
