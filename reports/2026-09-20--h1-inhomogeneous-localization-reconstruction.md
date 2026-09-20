# H1 inhomogeneous localization — reconstruction and gate ledger

Date: 2026-09-20
Branch: \`research/b-infinity-post-s4-gate\`
Status: **research note / H1 remains OPEN**

## 0. Scope and locks

This note records the latest reconstruction of the inhomogeneous H1 front. It does not reopen the flat paper.

Locked and untouched:
- \`E0 = OPEN_AT_STOP\`.
- \`POWER_13/2_STABILITY = OPEN_AT_STOP\`.
- AdS / inhomogeneous extension \`E = STOPPED_UNPROVEN\`.

## 1. Operator contract

Use
\[
D(z)=S(z)\oplus S(z)^{-1},\qquad
C_N(X)=\exp[-i\vartheta(X)\beta/N],
\qquad
A_N(X,z)=C_N(X)D(z).
\]

Working beta contract:
\[
\beta=\sigma_x\otimes I_2,\quad \beta^2=I,\quad \beta D\beta=D^{-1}.
\]

The original-source gamma-matrix convention is not re-certified here.

## 2. H1-SR

Let \(\mathcal P\) be the dominant rank-two Riesz bundle and \(Q=I-\mathcal P\). Since beta exchanges the lambda and inverse-lambda sectors,
\[
\mathcal P\beta\mathcal P=0.
\]

Therefore the first-order frozen intrabundle compression vanishes; dominant feedback starts at \(O(N^{-2})\) per step and can accumulate to \(O(N^{-1})\). The frozen dominant projector may shift by \(O(N^{-1})\).

\[
\boxed{\texttt{H1-SR = PROVED_UNDER_FROZEN_BETA_CONTRACT}}.
\]

## 3. H1a and H1b

On fixed neighborhoods of the eight relevant maxima, choose the dominant root with \(|\lambda|>1\). Compactness gives a uniform local gap. Since
\[
A_N-D=O(N^{-1}),
\]
common local Riesz contours persist and
\[
P_N-P=O(N^{-1}).
\]
For bounded lattice steps,
\[
A_N(X+e/N)-A_N(X)=O(N^{-2}),
\quad
P_N(X+e/N)-P_N(X)=O(N^{-2}).
\]

\[
\boxed{\texttt{H1a = PROOF_WRITTEN / UNREVIEWED}}.
\]

No global torus gap is claimed.

For nearby idempotents \(P,Q\), use
\[
T(Q,P)=QP+(I-Q)(I-P),
\quad QT=TP,
\quad T-I=(Q-P)(2P-I).
\]
Then \(T^{\pm1}=I+O(N^{-1})\), while consecutive frames differ by \(O(N^{-2})\). After conjugation to a fixed bundle, the frozen symbol is exactly block diagonal. The complementary block contracts relatively by a uniform local factor \(\rho<1\). With H1-SR the dominant product is
\[
\lambda^N[I+O(N^{-1})].
\]

\[
\boxed{\texttt{H1b = PROOF_WRITTEN / UNREVIEWED}}.
\]

## 4. Derivative selection rule

For the Fourier-coordinate insertion,
\[
\mathcal P Y_j\beta\mathcal P
=i\mathcal P\beta(\partial_j\mathcal P)\mathcal P
\]
(up to Fourier sign convention), using
\[
\mathcal P(\partial_j\mathcal P)\mathcal P=0,
\qquad
\mathcal P\beta\mathcal P=0.
\]
Thus
\[
\mathcal G_j(z)=i\mathcal P\beta(\partial_j\mathcal P)\mathcal P
\]
is a uniformly bounded analytic local amplitude by the Riesz formula.

\[
\boxed{\texttt{DERIVATIVE_SELECTION_RULE = PASS}}.
\]

## 5. Alice/Bob absolute layer scale recovered from the primary report

Verified against \`reports/2026-09-17--regional-laplace-coefficient-gate.md\`.

The layer lemma uses the complete endpoint spinors
\[
f=s_N b_N\chi,\qquad w=h_B M_B r,
\]
before spectral projection.

The report gives
\[
b_N=O(N^{-3/2}),\qquad
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),
\]
and
\[
s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),
\qquad
h_B=\frac{64}{N^2}{\varepsilon'_\perp}^{\,2}.
\]

At normal depth \(j\), the tangential area is \(O(N(1+j))\), while the tilted normal factor is exponentially summable, of the form \(e^{-t_*(\theta_N+j)}\). Hence, without phase cancellation,
\[
\sum_x e^{\xi_*\cdot(x-x_*)}\|f(x)\|=O(N^{-5/2}),
\]
\[
\sum_y e^{-\xi_*\cdot(y-y_*)}\|w(y)\|=O(N^{-5/2}).
\]
Therefore
\[
\sup_\eta\|\mathfrak A_f(\eta)\|=O(N^{-5/2}),
\qquad
\sup_\eta\|\mathfrak B_w(\eta)\|=O(N^{-5/2}).
\]

This is an absolute full-spinor bound, not a dominant-bundle bound.

The same report records a tangential Poisson correction \(O(N^{-4})\) against the \(N^{-5/2}\) Alice scale, i.e. relative \(O(N^{-3/2})\).

\[
\boxed{\texttt{LAYER_ABSOLUTE_MASS_BOUND = PASS}}.
\]

## 6. G insertion: local-window stability

Inside a fixed saddle neighborhood, \(\mathcal G_j\) is uniformly bounded. With \(\vartheta\in C^1\), the accumulated intrabundle insertion is \(O(N^{-1})\). Combining endpoint bounds and the three-dimensional Gaussian factor:
\[
N^{-1}N^{-5/2}N^{-5/2}N^{-3/2}=N^{-15/2}.
\]
This is below the flat absolute remainder \(O(N^{-7})\).

\[
\boxed{\texttt{G_INSERTION_POWER_STABILITY = PASS_IN_LOCAL_WINDOW}}.
\]

No global localization statement is implied.

## 7. Final Q leakage: corrected local estimate

An earlier exploratory \(O(N^{-8})\) count omitted the zeroth-order coin term
\[
-\frac{i}{N}\vartheta(\bar X_k)\beta.
\]
Its \(\mathcal P\beta\mathcal P\) compression vanishes, but \(Q\beta\mathcal P\) need not. In the frozen-frame analysis this appears as the \(O(N^{-1})\) change of basis/projector,
\[
\mathcal P_N=\mathcal P+O(N^{-1}).
\]

Because the primary layer estimate bounds the complete Bob spinor,
\[
\|\mathfrak B_w(\eta)Q(\eta)\|
\le \|\mathfrak B_w(\eta)\|\,\|Q(\eta)\|
=O(N^{-5/2})
\]
uniformly on a local Riesz neighborhood.

Thus the safe local matrix-element estimate is
\[
|\Delta T_Q|\lesssim N^{-1}N^{-13/2}=O(N^{-15/2}).
\]
The linear-in-eta leakage has an additional Gaussian gain and is smaller.

\[
\boxed{\texttt{FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW}}.
\]

No calculation of a leading \(B_{Q,\sigma}^{(0)}\) coefficient is needed for this upper-bound gate.

## 8. H1c reformulation

A finite-range path carries individual hopping matrices \(D_h\), not the full symbol \(D(z)\), so literal pathwise use of H1b is invalid.

\[
\boxed{\texttt{H1c_GLOBAL = UNNECESSARY}},
\qquad
\boxed{\texttt{H1c_LOCALIZED = OPEN}}.
\]

The remaining bottleneck is
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

The required result concerns the exact tilted Alice/Bob matrix element, not merely an operator norm.

## 9. Candidate route for L': absolute Dyson expansion in momentum

**Status: unverified proposal, not a proved lemma.**

Schematically,
\[
C_N-I=-\frac{i}{N}\vartheta(x/N)\beta+O(N^{-2}).
\]
In Fourier space the leading perturbation is convolution with
\[
K_N(q)=N^3\widehat\vartheta(Nq)
\]
(up to Fourier normalization).

For nearby dominant bundles,
\[
\mathcal P(\eta+q)\beta\mathcal P(\eta)
=
[\mathcal P(\eta+q)-\mathcal P(\eta)]\beta\mathcal P(\eta),
\]
so locally
\[
\|\mathcal P(\eta+q)\beta\mathcal P(\eta)\|\le C|q|.
\]

Kernel moments:
\[
\int |K_N(q)|dq=\int|\widehat\vartheta(p)|dp,
\]
\[
\int |q||K_N(q)|dq
=\frac1N\int|p||\widehat\vartheta(p)|dp.
\]
Hence a candidate intrabundle Dyson insertion costs
\[
\frac1N\int |q||K_N(q)|dq=O(N^{-2}),
\]
provided
\[
\int_{\mathbb R^3}(1+|p|)|\widehat\vartheta(p)|dp<\infty.
\]

After summing insertion times, the hoped-for effective gain is \(O(N^{-1})\) per insertion. The target is
\[
e^{-N\varphi_*}|T_n|
\le C N^{-13/2}\frac{(C'/N)^n}{n!}.
\]

### Unresolved step (ii)

This Dyson estimate is **not proved**. The delicate point is uniform control of variable-momentum chains
\[
\eta_0\to\eta_1\to\cdots\to\eta_n,
\qquad q_j=\eta_j-\eta_{j-1},
\]
because the walk is non-normal and both spectral radii and Riesz projectors vary with momentum.

A proof must control dominant-bundle products after extracting the global tilted rate, chains visiting \(Q\), transitions among the eight saddle neighborhoods, and passages through regions where the local Riesz splitting is unavailable. It may not assume momentum conservation or the flat localization statement that L' is intended to replace.

Until that step is written and independently checked,
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

## 10. Current ledger

| Gate | Status |
|---|---|
| H1-SR | PROVED_UNDER_FROZEN_BETA_CONTRACT |
| H1a | PROOF_WRITTEN / UNREVIEWED |
| H1b | PROOF_WRITTEN / UNREVIEWED |
| DERIVATIVE_SELECTION_RULE | PASS |
| LAYER_ABSOLUTE_MASS_BOUND | PASS |
| G_INSERTION_POWER_STABILITY | PASS_IN_LOCAL_WINDOW |
| FINAL_Q_LEAKAGE_MATRIX_ELEMENT | PASS_IN_LOCAL_WINDOW |
| H1c_GLOBAL | UNNECESSARY |
| H1c_LOCALIZED | OPEN |
| H1c_LOCALIZATION (L') | OPEN |
| H1 | OPEN |
| E0 | OPEN_AT_STOP — untouched |
| POWER_13/2_STABILITY | OPEN_AT_STOP — untouched |
| E / AdS extension | STOPPED_UNPROVEN — not reactivated |

## 11. Next admissible step

Write and audit the missing dominant-transport estimate for the momentum-space Dyson chain. Do not promote L', H1c, or H1 until the non-normal variable-momentum product in step (ii) is controlled.

No further inference is authorized by this note.
