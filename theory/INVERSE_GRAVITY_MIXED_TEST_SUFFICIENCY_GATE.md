# IG-S2 — sufficiency audit of the added mixed stationarity test

Date: 2026-10-08. Branch: `research/inverse-gravity-design`.
Authorization: user continuation of the curvature-cost obligation.
Initial status: OPEN. Keep q=3 full N-type H, even L>=4, unchanged comparable
positive couplings, and the fixed curvature pair.

Freeze the tested necessary conditions explicitly: positivity and normalization
of a density, translation/reality symmetry, stationarity for all Hermitian
polynomials in the curvature angle words, ground-cost positivity for all
polynomials in those angle words, and stationarity for every translated
Y_i=i(P_i S_i^dagger-S_i P_i) previously fixed. This is NOT the entire
common commutant of H_U,H_g and NOT every ground-state condition.

Attempt an analytic bound on the curvature numerator from these conditions.
Test the explicit density tau=(I/3) on each diagonal register and |0><0|
on every face register. If it passes those conditions with a constant
positive numerator, reject only their sufficiency. Never admit tau as a
true ground density or as a tensor trial vacuum.

Also audit the exact two-operator ground-cost matrix for A_1=P_i and
A_2=T_i=S_iP_i. A true ground density must make its Hermitian cost matrix
positive semidefinite. Determine whether the coherent span excludes tau.
Auxiliary code may check only the q=3 central diagonal trace average,
scalar-stencil face count, and the resulting two-by-two symbolic matrix and
explicit energy-lowering coefficient. Freeze permanent code before execution.
No many-body diagonalization, SDP search or provider review.

All-volume claims require analytic proofs. Stop OPEN for the true-ground
numerator if no bound is obtained. Do not expand to further test families
automatically or promote a local exclusion to a spectral result.


## Authorized bounded continuation — 2026-10-10

The user instructed "Intentalo" after requesting a quantitative link from
the existing mixed ground-cost tests to the fixed curvature Rayleigh quotient.
Base: `dfe2241a596289c718e9dc54d12c43c10cc2a33b`.
This dated extension leaves the October 8 contract and outcome intact.

Question: can the admitted coherent mixed-cost matrices control an upper
curvature energy bound, uniformly in even L>=4, for the unchanged full q=3
Hamiltonian and positive comparable L-independent couplings? The spectral
target remains G_R(p_L)>0 and F_R(p_L)<=C|p_L|G_R(p_L) after removal of the
entire ground space. Quartic numerator scaling is one sufficient route,
not an admission requirement for every possible quotient proof.

Reuse the fixed P_i, S_i P_i, Y_i, curvature pair and existing exact
derivations. First work analytically with the positive ground-energy form:
derive the full block relation between mixed tests and curvature probes,
including singular blocks and a complete degenerate ground space. Audit
the direction of every resulting inequality and any proposed operator-span
or residual estimate. A relaxation obstruction must state precisely the
information it excludes; an abstract PSD countermodel is not a physical
N-type state and cannot refute the full ground inequalities or spectrum.

No Hamiltonian/coupling/probe adjustment, many-body diagonalization, SDP,
new test hierarchy or outside-model review is authorized by this attempt.
No new scientific script is planned: identities will be proved analytically
and existing code read without modification. Any retained computation
would require permanent code frozen before execution.

Stop after this fixed transfer attempt. Record either an explicit uniform
bound, a rigorously scoped obstruction to the attempted transfer, or OPEN
with the exact missing inequality. An additional rejected trial state alone
does not meet the objective. Reuse the existing sufficiency report for the
dated outcome; update the branch-local state without scientific promotion.
