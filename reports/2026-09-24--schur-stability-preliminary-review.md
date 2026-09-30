# Preliminary review: Schur stability and physical reconstruction bounds

**Date:** 2026-09-24
**Status:** PRELIMINARY — independent review pending

**Provenance correction:** this file initially recorded the user's proposed
analysis while the checkout was on `main`; that branch did not contain the
Schur derivation. The actual source is
`research/b-infinity-post-s4-gate` at `7f68fa7`, in the H1c Schur and T1
reports. The follow-up derivation is
[the stability audit](2026-09-24--schur-stability-physical-transfer.md).
This note is not evidence that an independent review had already occurred.

## 1. Main structural observation

The useful new estimate is

\[
\boxed{\|E^{1/2}\mathcal V_c\|=\Theta(N^{-1})}.
\]

Thus the physical reconstruction toward Bob does not amplify the problem. It
introduces a polynomial suppression of order \(N^{-1}\). The mechanism is
geometric: in the region where de-tilting would be most dangerous, the weight
\(h_N\) vanishes.

Conditionally on the preliminary bound

\[
\|t_N\|=O_W(1),
\]

this gives

\[
\|E^{1/2}\mathcal V_cPt_N\|,
\quad
\|E^{1/2}\mathcal V_cQt_N\|
=O_W(N^{-1}),
\]

and therefore the physical pieces satisfy the upper bounds

\[
A_{cP},A_{cQ}=O_W\!\left(N^{-1}e^{-K_*N}\right),
\]

while

\[
B_{cPP},B_{cQQ},B_{cPQ}
=O_W\!\left(N^{-2}e^{-2K_*N}\right).
\]

The upper bounds for the quadratic pieces have a stronger exponential
suppression than the upper bounds for the linear pieces. This does not
establish their actual relative sizes: a nonzero linear piece can itself
be much smaller than its upper bound. With the exact T1 decomposition,
the conditional remainder statement is

\[
L_c=A_{cP}+A_{cQ}
 +O_W\!\left(N^{-2}e^{-2K_*N}\right).
\]

This is a structural upper-bound statement, not a signed asymptotic
expansion.

## 2. Required caution

The estimate

\[
\|t_N\|=O_W(1)
\]

remains **PRELIMINARY** and has not received an independent review. All
quantitative transfer to the physical pieces depends on that estimate. The
next task is therefore a focused review of the chain

\[
\text{Schur stability}
\;\Longrightarrow\;
\|t_N\|=O_W(1)
\;\Longrightarrow\;
\text{physical bounds}.
\]

No claim is made yet that

\[
A_{cP}\sim N^{-1}e^{-K_*N},
\]

nor that either \(A_{cP}\) or \(A_{cQ}\) is the dominant signed term. The
current estimates are upper bounds only.

## 3. Priority reduction after confirmation

If the independent Schur review confirms the bound, the next analysis can
focus on the four signed linear pieces

\[
A_{+P},\quad A_{+Q},\quad A_{-P},\quad A_{-Q}.
\]

There are three quadratic pieces per channel, six in total. Their upper
bounds carry the
stronger exponential penalty \(e^{-2K_*N}\).

## 4. Gate impact

This note records a promising reduction of the active calculation front. It
does **not** close the Schur-stability question, establish the \(t_N\) bound,
identify a signed leading term, or change the canonical project status in
`state/CURRENT_STATE.md`.
