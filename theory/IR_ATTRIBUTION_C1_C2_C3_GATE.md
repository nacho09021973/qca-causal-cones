# IR attribution: C1 / C2 / C3

Frozen 2026-09-22 by the user's instruction to review C1 independently and
derive a representation of Lpp. This is the spectral-attribution front C,
not the older strict-cone successor named Gate C elsewhere in this repo.
Baseline: `2b29b19` plus the local
[leakage derivation](../reports/2026-09-22--ir-projection-leakage-and-conditioning.md).
The C1 derivation predates this contract; this is not a retrospective
preregistration of its discovery. C2 criteria below precede this turn's
new representation and asymptotic analysis.

## Frozen objects

The literal homogeneous two-component CJWW (5.15) walk S, zero node,
Fourier convention and original regional protocol in
`papers/ir-corona/ir-corona.md`, sections 2–3. No new model or filter.
`Lambda=N^{-1}`, `P=Pi'=1_{|p|<=N^{-1/2}}`, `Q=I-P`.
Alice and Bob are radius N/4 balls centered at 0 and N(1,1,1).
Resource `phi_N=N^{-3/2} Phi_0(x/N) down`;
profiles `(1-16|x/N|^2)_+^2` and its Bob translate.

## C1 — leakage

Scope: the four original encoders `M in {I,sigma1,sigma2,sigma3}`.
Review the analytic chain, not just the software checks:

1. `q_N=||Q(U_M-I)phi_N||^2 = D N^{-5/2}(1+O(N^{-1/2}))`;
2. `D=1024 pi^2 Phi_0(1/4)^2/5 > 0` for all four encoders;
3. continuous radial boundary asymptotics, Poisson summation, and uniform
   alias/cross-term estimates;
4. `||Delta-PDeltaP||_1=sqrt(4q_N-3q_N^2)`;
5. the consequent failure of norm-relative attribution at the total
   exponential signal scale, without inferring observable dominance.

Verdicts: `PASS`, `REPAIR_REQUIRED`, `FAIL`, or `INCOMPLETE`.
PASS requires a completed independent analytic review with an explicit
verdict and no outstanding load-bearing repair. A software PASS alone
does not close C1. One review is one review, not multi-member consensus
or canonical promotion.

## C2 — projected response

Initial pair: `M=sigma2`, `M_B=I`, the pair in the retained N=24,40 audit.
General identities may cover all original pairs, but any asymptotic
extension must state its own quantifiers.

Object: `Lpp=tr(E S^N P Delta P S^{-N})`, signed; `delta_pp=abs(Lpp)`.
Keep both `2 Re<r,E dP>` and `<dP,E dP>`, with
`r=S^N phi`, `dP=S^N P(U_M-I)phi`. Do not drop the quadratic term because
it was negligible for the unprojected signal.

This turn's deliverable is an exact real-momentum representation, separating
the moving cutoff boundary, the full lattice symbol and alias terms.
An analytic approximation must have an explicit error before it can
decide Lpp. No new numerical scan, fits, or code pipeline is authorized
by this contract; existing exact checks may be rerun for C1.

Terminal asymptotic outcomes, if later proved:

- same exponential rate/power with nonzero coefficient (allow bounded
  lattice-phase dependence; the total coefficient is C(theta_N));
- different exponential structure;
- zero or asymptotically negligible versus the total signal;
- algebraic/oscillatory cutoff response, possibly larger than total L;
- `OPEN` if the leading term, nonvanishing, or sufficient remainder control
  is missing. The list does not force an exponential ansatz.

Never infer `L-Lpp=o(abs(L))` or its negation from a global norm alone.
The nonlocal projection also prevents identifying a nonzero Lpp with a
new strictly local band-limited protocol without additional argument.

## C3 — conditioning

Keep `Lcond=(Lpp+q_N p0_N)/(1-q_N)` separate, with success probabilities
1 and `1-q_N`. It cannot replace C2. The existing polynomial correction
for `M_B=I` is not a determination of the leading term of either signal
separately. No conditioned experiment is implemented in this task.

## Locks and evidence

The total flat theorem and its prior review retain their exact scope.
No canonical-state promotion, manuscript publication, commit/push,
new code scan, or reopening of E/AdS follows from this contract.
H1c, E0 and POWER_13/2_STABILITY retain their prior states.
The edge power 3/2 is prior art, not a candidate novelty claim.
