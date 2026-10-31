# H1 small fixed Gaussian profile gate

Date: 2026-10-31. Initial status: `OPEN / NOT_EXECUTED`.
User authorization: «1 y despues 3»: consolidate the bridge, then study
`vartheta=epsilon v` for a fixed admissible profile, its first signed
correction, and possible flat-leader survival at small epsilon.
This contract is committed before execution.

## 1. Frozen model and quantifiers

The promoted Schur physical bridge at `2e6af3a` is input. Retain the exact
two-channel contract and T1: dimension 3, C^2_channel tensor C^2_spin,
D=S direct-sum S^-1 for the explicit CJWW (5.15) symbol in
`papers/ir-corona/ir-corona.tex`, beta=sigma_x_channel tensor I_spin.
Keep the body-diagonal one-step displacements, lattice units, complete
update, J phi_N, Alice/Bob balls of radius N/4, profiles and time N.
No new isotropy, representation, minimality or irreducibility assumption
is imposed on the inhomogeneous coin. Any admissible T1 W is fixed
independently of N and epsilon.

Fix one nonconstant real shape and one original encoder/detector pair:

\[
v(X)=e^{-|X|^2},\quad \vartheta_\varepsilon=\varepsilon v,\quad
U_{N,\varepsilon}=e^{-i\varepsilon v(x/N)\beta/N}D,\quad
M=\sigma_2,\quad M_B=I_2,\quad E=h_N I_2.
\]

Use the bridge Fourier convention
`v(X)=integral exp(-ik.X) vhat(k) d^3k/(2pi)^3` and verify F.
Epsilon is real, initially `|epsilon|<=1`; any smaller threshold must be
positive and independent of N. No profile or parameter scan is authorized.
The primary observable remains (L_+,L_-). Freeze the retained functional

\[
f_0=(U_M-I)\phi_N,\quad
r_{+,\varepsilon}=1_{\mathcal B_N}\pi_+U_{N,\varepsilon}^N J\phi_N,
\qquad F_N(\varepsilon)=2\Re\langle r_{+,\varepsilon},ES^N f_0\rangle.
\]

This F_N is not full L_+ or the older fixed-flat-reference functional.
N->infinity and epsilon->0 are distinct limits.

## 2. Tasks, in order

1. Derive finite-N epsilon derivatives and exact channel parity. Identify
   the first potentially nonzero correction, including same-coin and
   distinct-time insertions. Do not assert a quadratic coefficient is
   nonzero without proof.
2. Bound the physical-reference Taylor remainder uniformly in N on a fixed
   epsilon interval, stating the norm and tracing both physical endpoints.
3. Test whether `|F_N(epsilon)-F_N(0)|` is at most
   `C epsilon^2 N^-13/2 exp(-K_*N)`, or establish a sufficient alternative.
   Constants must be independent of N and epsilon in the interval.
   Bare norm continuity does not establish survival at this scale.
4. Only if this and the flat coefficient lower bound hold, derive a
   small-epsilon sign/nonvanishing statement. Any transfer to (L_+,L_-)
   must prove uniformity of the promoted bridge on the epsilon interval.

## 3. Admission, outcomes and stopping

Use exact algebra and analytic bounds. No new finite-N scan, fitting,
preparation, encoder, detector, geometry or substrate. Retained computations
need permanent generators; do not change reviewed verifiers. Check the
library index first; if absent, record that and use explicit in-repo
definitions/primary sources as needed. No novelty search or claim.

Stop after the first complete bounded analysis. If only derivatives or
weaker bounds are available, state the precise missing estimate and stop
without asymptotic survival. An uncomputed coefficient stays OPEN.
Execution outcomes are `DERIVATIVES_ONLY / ASYMPTOTIC_SURVIVAL_OPEN`,
`SMALL_PROFILE_SURVIVAL_PROOF_WRITTEN / INDEPENDENT_REVIEW_PENDING`,
`OPEN_AT_SCALE_BOUND`, or `COUNTEREXAMPLE_CANDIDATE /
INDEPENDENT_REVIEW_PENDING` with an exact admissible construction.

New results stay PRELIMINARY until independent cross-family review and
separate explicit promotion. External submission of new results and
publication are not authorized here; prepare a reviewable report.

## 4. Locks

Only this one-profile/one-pair H1 subproblem is reopened. General H1 and H1c
remain OPEN; broad localization remains paused. E0, general
POWER_13/2_STABILITY, E/AdS, physical realization, C1/C2/C3 and the flat
manuscript are unchanged. A small-epsilon result here is not a theorem for
arbitrary profiles, a computed new asymptotic coefficient or an implementation.
