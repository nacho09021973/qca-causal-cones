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
