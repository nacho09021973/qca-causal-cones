# H1 reopening — chat research record

Date: 2026-09-20  
Scope: reconstruction of the research carried out in the ChatGPT project after the 2026-09-17 flat IR-corona paper.  
Authority: this is a research log. Exact committed primary reports and formal manuscript formulas override a chat reconstruction if they conflict.

## 1. Starting point

The flat CJWW (5.15) operational IR-corona result was already closed in its frozen class. The later inhomogeneous/AdS extension had previously stopped as \`STOPPED_UNPROVEN\`. The reopening authorized in this research thread was deliberately narrower: **H1 only**.

Locks retained throughout:
- \`E0 = OPEN_AT_STOP\`;
- \`POWER_13/2_STABILITY = OPEN_AT_STOP\`;
- \`E / AdS = STOPPED_UNPROVEN\`;
- no new physical-realization claim.

The inhomogeneous model considered is the doubled walk
\[
D(z)=S(z)\oplus S(z)^{-1},
\]
with slowly varying on-site coin
\[
C_N(X)=e^{-i\vartheta(X)\beta/N},
\qquad
A_N(X,z)=C_N(X)D(z).
\]
The analytic continuation uses \(S(z)^{-1}\), not \(S(z)^\dagger\).

## 2. Frozen spectral structure and H1-SR

Working beta contract:
\[
\beta=\sigma_x\otimes I_2,\qquad
\beta^2=I,\qquad
\beta D\beta=D^{-1}.
\]

For the dominant rank-two Riesz bundle \(\mathcal P\), beta exchanges the dominant and reciprocal sectors. Hence
\[
\mathcal P\beta\mathcal P=0.
\]

This kills the first-order frozen intrabundle coin correction. The first dominant feedback is \(O(N^{-2})\) per step and can accumulate to \(O(N^{-1})\).

Status:
\[
\texttt{H1-SR = PROVED_UNDER_FROZEN_BETA_CONTRACT}.
\]

The original-source gamma-zero convention was not separately re-certified and is not promoted by this log.

## 3. H1a — local spectral/Riesz bundle

Near each of the eight relevant spectral maxima, choose the root with \(|\lambda|>1\). On compact local neighborhoods there is a uniform gap from the reciprocal root. The weak coin satisfies
\[
A_N-D=O(N^{-1}),
\]
so a common local Riesz contour persists and
\[
P_N-P=O(N^{-1}).
\]

For bounded spatial steps,
\[
A_N(X+e/N)-A_N(X)=O(N^{-2}),
\qquad
P_N(X+e/N)-P_N(X)=O(N^{-2}).
\]

This is local; no global torus gap is claimed.

Status:
\[
\texttt{H1a = PROOF_WRITTEN/UNREVIEWED}.
\]

## 4. H1b — frozen product transport

For nearby idempotents use
\[
T(Q,P)=QP+(I-Q)(I-P).
\]
Then \(QT=TP\) and \(T-I=(Q-P)(2P-I)\). Consecutive frozen frames differ by \(O(N^{-2})\). In the transported frame the frozen symbol is exactly block diagonal, and the complementary block contracts relative to the dominant block by a uniform local factor \(\rho<1\).

With H1-SR,
\[
U_{N:1}=\lambda^N[I+O(N^{-1})]
\]
inside the dominant block.

Status:
\[
\texttt{H1b = PROOF_WRITTEN/UNREVIEWED}.
\]

## 5. Why the global pathwise version was abandoned

The finite-range tilted spatial operator has an exact path expansion, but each path carries individual hopping matrices \(D_h\), not the full symbol \(D(z)\). Therefore H1b cannot simply be applied path by path.

Also, although \([D_\xi,C_N]=O(N^{-2})\), a naive \(N^2\)-swap argument only gives an \(O(1)\) upper bound. This is not a counterexample; it shows that the crude reordering estimate is insufficient.

Decision:
\[
\texttt{H1c_GLOBAL = UNNECESSARY},
\qquad
\texttt{H1c_LOCALIZED = OPEN}.
\]

## 6. Derivative selection rule

Writing the fluctuation coordinate as a Fourier derivative gives
\[
\mathcal P Y_j\beta\mathcal P
=i\mathcal P\beta(\partial_j\mathcal P)\mathcal P
\]
(up to Fourier sign convention), because
\[
\mathcal P(\partial_j\mathcal P)\mathcal P=0,
\qquad
\mathcal P\beta\mathcal P=0.
\]

Thus
\[
\mathcal G_j=i\mathcal P\beta(\partial_j\mathcal P)\mathcal P
\]
is a bounded analytic local amplitude. The apparent \(Y=O(\sqrt N)\) promotion disappears after projection.

Status:
\[
\texttt{DERIVATIVE_SELECTION_RULE = PASS}.
\]

## 7. Character/Poisson observations

The flat source has eight spectral maxima. Six are eliminated by nontrivial lattice characters; only the two leading sectors survive. A coordinate/derivative insertion does not change the character sector. The bounded symbol \(\mathcal G_j\) therefore preserves the character bookkeeping.

Recorded statuses:
- \`G_CHARACTER_COVARIANCE = PASS\`;
- \`CHARACTER_SECTOR_PRESERVATION_UNDER_FIRST_INSERTION = PASS\`;
- \`POISSON_SYMBOL_CLASS_STABILITY = PASS\`;
- \`POISSON_GAIN_N^{-3/2}_STABILITY = CONDITIONAL_ON_FLAT_POISSON_MECHANISM\`;
- \`SIX_SADDLE_CANCELLATION_STABLE = OPEN\`.

These observations were not used to claim global H1c localization.

## 8. Recovery of the missing Alice/Bob formulas

The chat reconstruction initially lacked the exact endpoint definitions and therefore held
\[
\texttt{LAYER_ABSOLUTE_MASS_BOUND = NOT_RECOVERABLE_FROM_CURRENT_MD}.
\]

The private repository was then inspected. The primary report
\`reports/2026-09-17--regional-laplace-coefficient-gate.md\`
contains the needed formulas. Its layer lemma uses the complete endpoint spinors
\[
f=s_N b_N\chi,\qquad w=h_BM_Br,
\]
before spectral projection, with
\[
b_N=O(N^{-3/2}),
\]
\[
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})
\]
uniformly in the relevant Bob layer, and
\[
s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),
\qquad
h_B=\frac{64}{N^2}{\varepsilon'_\perp}^{\,2}.
\]

At normal depth \(j\), the tangential area is \(O(N(1+j))\), not simply \(O(N)\); the normal tilted factor is exponentially summable in \(j\). Therefore
\[
\sum_xe^{\xi_*\cdot(x-x_*)}\|f(x)\|=O(N^{-5/2}),
\]
\[
\sum_ye^{-\xi_*\cdot(y-y_*)}\|w(y)\|=O(N^{-5/2}).
\]

Consequently,
\[
\sup_\eta\|\mathfrak A_f(\eta)\|=O(N^{-5/2}),
\qquad
\sup_\eta\|\mathfrak B_w(\eta)\|=O(N^{-5/2}).
\]

This is an absolute full-spinor bound, not a cancellation statement and not a bound only after projection. The primary report also gives a tangential Poisson correction \(O(N^{-4})\) against the \(N^{-5/2}\) Alice scale, i.e. relative \(O(N^{-3/2})\).

Promotion:
\[
\texttt{LAYER_ABSOLUTE_MASS_BOUND = PASS}.
\]

## 9. Clarification of the Gaussian count

The momentum Hessian is positive definite:
\[
Q=q_t(I-\hat u\hat u^T)+q_n\hat u\hat u^T,
\qquad q_t,q_n>0.
\]
Hence the local spectral factor has a full three-dimensional Gaussian majorant and contributes \(N^{-3/2}\).

The apparent spatial tangential zero modes arise later, after assembling the two endpoint layers: the block in the two tangential endpoint variables has rank two, so the common tangential coordinate is confined by the profiles rather than by an additional Gaussian. There is no contradiction between these two statements.

## 10. G insertion power stability

Inside a fixed saddle neighborhood, \(\mathcal G_j\) is bounded. With \(\vartheta\in C^1\), the accumulated intrabundle correction is \(O(N^{-1})\). Therefore
\[
N^{-1}\,N^{-5/2}\,N^{-5/2}\,N^{-3/2}
=N^{-15/2},
\]
below the flat absolute remainder \(O(N^{-7})\).

Status:
\[
\texttt{G_INSERTION_POWER_STABILITY = PASS_IN_LOCAL_WINDOW}.
\]

The scope qualifier is essential: momentum localization outside the local saddle neighborhoods remains open.

## 11. Final Q leakage — correction retained

An intermediate estimate \(O(N^{-8})\) was corrected. It had omitted the zeroth-order coin term
\[
-\frac{i}{N}\vartheta(\bar X_k)\beta.
\]
Its \(\mathcal P\beta\mathcal P\) component vanishes, but \(Q\beta\mathcal P\) need not. In the frozen-frame language this is the \(O(N^{-1})\) change
\[
\mathcal P_N=\mathcal P+O(N^{-1}).
\]

Since the Bob bound controls the complete spinor,
\[
\|\mathfrak B_wQ\|\le \|\mathfrak B_w\|\,\|Q\|=O(N^{-5/2})
\]
locally by the Riesz gap. Thus the safe estimate is
\[
|\Delta T_Q|\lesssim N^{-1}N^{-13/2}=O(N^{-15/2}).
\]

The term linear in momentum receives an extra Gaussian \(N^{-1/2}\) gain and is smaller. No leading \(B_{Q,\sigma}^{(0)}\) coefficient is needed for this upper-bound gate.

Status:
\[
\texttt{FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW}.
\]

## 12. Remaining bottleneck: L'

The only unresolved H1c gate after the local endpoint and leakage estimates is
\[
\texttt{H1c_LOCALIZATION (L') = OPEN}.
\]

A simple operator-norm commutator localization is insufficient: at cutoff scale \(L_N/\sqrt N\) it gives roughly \(1/(L_N\sqrt N)\) relative to the tilted exponential scale, far too large compared with the \(N^{-13/2}\) matrix element. Localization must therefore be proved at matrix-element level while preserving endpoint powers and character structure.

## 13. Candidate Dyson route

This is a proposal only.

Write
\[
C_N-I=-\frac{i}{N}\vartheta(x/N)\beta+O(N^{-2}).
\]
In momentum space the leading perturbation convolves with
\[
K_N(q)=N^3\widehat\vartheta(Nq).
\]

For nearby dominant bundles,
\[
\mathcal P(\eta+q)\beta\mathcal P(\eta)
=
[\mathcal P(\eta+q)-\mathcal P(\eta)]\beta\mathcal P(\eta)
=O(|q|).
\]

Moreover
\[
\int|K_N(q)|\,dq=\int|\widehat\vartheta(p)|\,dp,
\]
\[
\int|q||K_N(q)|\,dq
=\frac1N\int|p||\widehat\vartheta(p)|\,dp.
\]
Thus an intrabundle insertion has candidate cost \(O(N^{-2})\) provided
\[
\int_{\mathbb R^3}(1+|p|)|\widehat\vartheta(p)|\,dp<\infty.
\]

After summing insertion times, the desired bound is
\[
e^{-N\varphi_*}|T_n|
\le
C N^{-13/2}\frac{(C'/N)^n}{n!}.
\]

This has **not** been proved. The unresolved step is uniform control of variable-momentum, non-normal products
\[
\eta_0\to\eta_1\to\cdots\to\eta_n
\]
after extracting the global tilted rate, including chains visiting \(Q\), transitions among the eight saddle neighborhoods, and passages through regions without the local Riesz splitting. The proof may not assume the flat momentum conservation/localization that L' is intended to replace.

The Fourier-moment hypothesis above should be kept as the actual working regularity condition until a sufficient Sobolev condition is derived correctly; no \(H^s\) threshold is frozen here.

## 14. Ledger at end of chat reconstruction

| Gate | Status |
|---|---|
| H1-SR | PROVED_UNDER_FROZEN_BETA_CONTRACT |
| H1a | PROOF_WRITTEN / UNREVIEWED |
| H1b | PROOF_WRITTEN / UNREVIEWED |
| DERIVATIVE_SELECTION_RULE | PASS |
| G_CHARACTER_COVARIANCE | PASS |
| CHARACTER_SECTOR_PRESERVATION_UNDER_FIRST_INSERTION | PASS |
| POISSON_SYMBOL_CLASS_STABILITY | PASS |
| POISSON_GAIN_N^-3/2_STABILITY | CONDITIONAL_ON_FLAT_POISSON_MECHANISM |
| SIX_SADDLE_CANCELLATION_STABLE | OPEN |
| LAYER_ABSOLUTE_MASS_BOUND | PASS |
| G_INSERTION_POWER_STABILITY | PASS_IN_LOCAL_WINDOW |
| FINAL_Q_LEAKAGE_MATRIX_ELEMENT | PASS_IN_LOCAL_WINDOW |
| H1c_GLOBAL | UNNECESSARY |
| H1c_LOCALIZED | OPEN |
| H1c_LOCALIZATION (L') | OPEN |
| H1 | OPEN |
| E0 | OPEN_AT_STOP — untouched |
| POWER_13/2_STABILITY | OPEN_AT_STOP — untouched |
| E / AdS | STOPPED_UNPROVEN — not reactivated |

## 15. Next admissible step

Write and adversarially audit the dominant-transport estimate for the momentum-space Dyson chain. No promotion of L', H1c, or H1 is authorized before the non-normal variable-momentum product is controlled.

This log and \`2026-09-20--h1-inhomogeneous-localization-reconstruction.md\` together preserve the research that previously existed only in the chat.
