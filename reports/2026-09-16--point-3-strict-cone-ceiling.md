# Point (3): an analytic derivation of the strict-cone ceiling

**Contract frozen at:** `4135625`,
[`STRICT_CONE_CEILING_N3_GATE.md`](../theory/STRICT_CONE_CEILING_N3_GATE.md).
**Authorization:** direct user instruction, point (3) only.
**Author assessment:** `PASS_ANALYTIC` for the frozen point-(3) statement.
**Evidence level:** `PRELIMINARY_PROOF_COMPLETE_REVIEW_PENDING`.
**Independent review:** NOT PERFORMED. This report is not an independent
certificate, a five-member ratification, or a PASS of the full C gate.
**NOVELTY = OPEN.**

## 1. Statement and exact scope

For every symbol and selected cone admitted by the frozen contract,

\[
\boxed{0<c_0\le c_{\rm strict}^{\rm iso}
             \le r_{\rm in}(C_{\rm micro})=1/\sqrt3.}
\tag{1}
\]

The new target is the middle inequality. Internal dimension s and D2
representation R are fixed but arbitrary as specified by the contract.
The selected cone may lie in a higher-rank eigenspace with other slopes;
the entire eigenspace need not be purely conical. Floquet eigenphase zero
is not assumed. Support always means the exact matrix Fourier support of
the full U, with all cancellations included.

No L1 identity, metric-defect identity, non-nilpotent vertex hypothesis,
scalar-node condition, or asymptotic probability distribution is used.
The proof below supplies the needed derivative and eigenphase-slope
arguments rather than invoking unverified Bernstein or Rellich statements.

## 2. A polynomial boundary lemma

Let F(z) be an s-by-s matrix polynomial of degree at most D, unitary on
the unit circle. Then

\[
 B=F(1)^\dagger F'(1)=B^\dagger,
 \qquad 0\preceq B\preceq D I.
\tag{2}
\]

Here `preceq` is the order on Hermitian matrices, and the prime is the
complex polynomial derivative.

**Disk contraction.** For fixed unit vectors a,b, the scalar polynomial
`a^dagger F(z)b` has modulus at most one on the circle, hence throughout
the disk. For completeness, the scalar polynomial maximum principle
follows by contradiction: at an interior local maximum with nonzero value,
choose the phase of a small displacement so that the first nonzero Taylor
term has the same argument as that value. Its leading increase dominates
the higher terms, contradicting maximality. A zero maximum forces the
polynomial to vanish. Compactness of the closed disk then puts its maximum
on the boundary unless it is constant. Taking the supremum over a,b gives
`||F(z)|| <= 1` for `|z| <= 1`.

**Hermiticity and lower bound.** Differentiating
`F(exp(-it))^dagger F(exp(-it))=I` at t=0 gives `B=B^dagger`.
For any v, the real polynomial function `g(r)=||F(r)v||^2` obeys
`g(r)<=||v||^2=g(1)` for `r<1`. Thus its left derivative at 1 is
nonnegative. Since

\[
 g'(1)=2\operatorname{Re}\langle v,Bv\rangle
       =2\langle v,Bv\rangle,
\]

B is positive semidefinite.

**Upper bound.** The reversed polynomial `G(z)=z^D F(1/z)` is a
polynomial, extended at z=0, and is also unitary on the circle. Its lower
bound gives

\[
 0\preceq G(1)^\dagger G'(1)=D I-B.
\]

This proves (2), including D=0 and singular F(0). No invertibility inside
the disk is required.

## 3. Finite-time bound in every direction

For n>=1, write the exact, already combined Fourier expansion

\[
 U(k)^n=\sum_{x\in S_n}e^{-ik\cdot x}A_{n,x},\qquad A_{n,x}\ne0,
\]

and put `H_n(q)=max_{x in S_n}q.x`. At the frozen node define

\[
 J_n(q)=i U(0)^{-n}\left.\partial_q U(k)^n\right|_{k=0}.
\]

Unitarity makes J_n(q) Hermitian. We claim

\[
 -H_n(-q)I\preceq J_n(q)\preceq H_n(q)I
 \quad\text{for every real }q.
\tag{3}
\]

First take `q=sqrt(3)m`, `m in Z^3`. Every displacement of U^n belongs
to `(1/sqrt(3))Z^3`, so every `q.x` is an integer. Let

\[
 a=\min_{x\in S_n}q\cdot x=-H_n(-q),\quad
 b=H_n(q),\quad D=b-a.
\]

Group terms with the same q.x and form the Laurent polynomial L satisfying

\[
 U(tq)^n=L(e^{-it}),\qquad F(z)=z^{-a}L(z).
\]

F is an ordinary matrix polynomial of degree at most D and is unitary on
the circle. Grouping may cancel some projected coefficients, including an
endpoint, but cannot introduce exponents outside [a,b]; exact endpoint
attainment by the grouped polynomial is not needed. Applying (2),

\[
 J_n(q)=a I+F(1)^\dagger F'(1),
\]

which proves (3) for these directions with their stated normalization.

For `q=sqrt(3)m/l`, `l` a positive integer, divide the inequality for
`sqrt(3)m` by l. This is valid because J_n is real-linear in q and H_n
is positively homogeneous. These rational vectors are dense in R^3.
For each fixed n, J_n is continuous and H_n is the maximum of finitely
many linear functions. The Hermitian positive cone is closed, so (3)
extends to every q, including irrational and non-axial directions.

No time limit was used in this density argument.

## 4. Compression before taking powers

Let `U_*=U(0)`, `J(q)=i U_*^dagger partial_q U(0)`, and let P be the
full spectral projector of U_* at `lambda_*=exp(-i omega_*)`. The product
rule, using `partial_q U(0)=-i U_* J(q)`, gives exactly

\[
 J_n(q)=\sum_{j=0}^{n-1}U_*^{-j}J(q)U_*^j.
\]

Since `U_*P=lambda_*P` and P commutes with U_*, each compressed summand
is `P J(q) P`. Therefore

\[
 \boxed{P J_n(q)P=nP J(q)P.}
\tag{4}
\]

P is the projector of U_*, **not** the full projector of U_*^n. Distinct
eigenvalues may have identical n-th powers without changing any step in
(4). In particular, there is no need to divide by a Floquet phase gap of
U_*^n. Off-diagonal matrix elements connecting P and its complement are
not assumed to vanish.

Compressing (3) and dividing by n gives an operator inequality on Ran P:

\[
 -\frac{H_n(-q)}n I_P
 \preceq (P J(q)P)|_{\operatorname{Ran}P}
 \preceq \frac{H_n(q)}n I_P.
\tag{5}
\]

## 5. Cone slopes belong to the compressed spectrum

Fix a unit q. By the admission hypothesis there is an eigenphase emerging
from omega_* with

\[
 \omega(tq)=\omega_*+t c_0+o(t),\qquad t\downarrow0.
\]

Write `lambda(t)=exp(-i omega(tq))` and choose any normalized eigenvector
v(t) of U(tq) for lambda(t). No continuous choice of v(t) is assumed.
Along a sequence tending to zero, finite-dimensional compactness gives
`v(t_j) -> v_*`, with `||v_*||=1`. The limiting eigenvalue equation gives
`v_* in Ran P`. Projecting the eigenvalue equation before dividing by t,

\[
 P\frac{U(tq)-U_*}{t}v(t)
  =\frac{\lambda(t)-\lambda_*}{t}P v(t).
\]

Taking that subsequential limit yields

\[
 P\partial_q U(0)P v_*=-i\lambda_*c_0 v_*.
\]

Multiplying by `i conjugate(lambda_*)` proves

\[
 P J(q)P v_*=c_0 v_*.
\tag{6}
\]

The same argument applies to the negative cone slope and to any other
admitted directional slope. For the upper bound only (6) is needed.
This proves the required implication from a cone slope to a compressed
eigenvalue; it does not assume a global smooth eigenbasis or claim to
prove the existence of a cone for an arbitrary symbol. Existence of the
selected cone is an admission condition, not a consequence of locality.

Combining (5) and (6), for every unit q and every n>=1,

\[
 c_0\le\frac{H_n(q)}n.
\tag{7}
\]

Additional nonconical branches in Ran P do not affect this argument.

## 6. Exact support limit and minimum over directions

Unitarity makes S_n nonempty. Fourier convolution gives
`S_{n+m} subseteq S_n+S_m`, with inclusion rather than equality because
of cancellations. Consequently H_n(q) is subadditive. Since every
one-step displacement has Euclidean norm one,

\[
 -n\|q\|\le H_n(q)\le n\|q\|.
\]

Here is the needed Fekete argument. Set H_0(q)=0. For fixed m and
`n=am+r`, `0<=r<m`, subadditivity gives `H_n<=a H_m+H_r`.
Dividing by n and taking limsup gives `limsup H_n/n<=H_m/m`.
Taking the infimum over m and using the defining lower bound of that
infimum proves

\[
 h_\infty(q)=\lim_n H_n(q)/n=\inf_{n\ge1}H_n(q)/n.
\tag{8}
\]

This is the same function as the limsup in
[`CAUSAL_BODY_GEOMETRY.md`, Sec. 6](../theory/CAUSAL_BODY_GEOMETRY.md).
From (7)-(8), `c_0<=h_infty(q)` for every unit q.

The minimum exists: all `H_n(q)/n` are 1-Lipschitz in q because
`||x/n||<=1` on S_n. Their pointwise limit h_infty is also 1-Lipschitz.
It therefore attains a minimum on the compact unit sphere. Taking this
minimum proves

\[
 c_0\le\min_{\|q\|=1}h_\infty(q)=c_{\rm strict}^{\rm iso}.
\]

There is no interchange of a directional minimum with the time limit.
The already established containment `S_n/n subseteq C_micro` supplies
`c_strict^iso<=1/sqrt(3)`, finishing (1).

## 7. Author adversarial checks against the frozen obligations

These are manual checks of the proof, not independent review or a
numerical verification suite. No scientific script was executed.

| Potential failure | Check and outcome |
| --- | --- |
| Wrong Fourier sign | For the predeclared scalar-shift sign control `U(k)=exp(-ik.h)`, `J_n(q)=n q.h`, and both bounds in (3) equal that value. This is only a sign check, not an admitted isotropic N3 counterexample. |
| Only coordinate axes proved | Rational vectors, followed by fixed-n continuity, give (3) for every real q. No coordinate-axis minimum is assumed. |
| Ignored Fourier cancellations | S_n is defined after cancellation; grouping in Sec. 3 uses its actual extremes as enclosing bounds. No path-counting support is substituted. |
| Nonzero Floquet phase | Factors lambda_* and its conjugate cancel in (4) and (6); omega_*=0 is not needed. |
| Power collisions | (4) uses the original projector. The already recorded s=4 node has phases +/-pi/4 which coincide after the fourth power; the algebra does not require their fourth powers to be distinct. |
| Degenerate node or r=s | Compactness plus the projected eigenvalue equation works at any finite rank, including P=I. There is no denominator involving a spectral gap. |
| Spectators in the same eigenspace | Only the existence of the selected slope +c_0 is used; other slopes are unrestricted. |
| Asymptotic limit/minimum | Subadditivity, a linear lower bound and a common Lipschitz bound discharge both existence obligations separately. |
| Negative strict speed silently excluded | Positivity is not assumed. The conclusion would exclude zero or negative `c_strict^iso` when an admitted c_0>0 cone exists. |
| Saturation smuggled into the proof | No vertex or face coefficient is assumed to survive; neither L1 nor non-nilpotency appears in (2)-(8). |
| Pavia and s=4 controls | The existing certificates have respectively `c_0=c_strict^iso=1/sqrt(3)` and `c_0=a/sqrt(3)<c_strict^iso=1/sqrt(3)` for 0<a<1. Both are consistent with (1); their scripts were not rerun. |
| Support of a sector confused with full support | S_n always belongs to U^n on the whole internal space. No sector-specific support theorem is claimed. |

## 8. Source boundary and interpretation

The maximum-principle argument and the support subadditivity are standard
mathematical tools. Their application here is not claimed as novel.
The power-compression route was suggested in Astra's partial ratification
turn; that incomplete discussion was motivation, not validation. The
full boundary lemma and slope argument above are supplied here for review.

A targeted primary-source check located Cedzich, Joye, A. H. Werner and
R. F. Werner, [*Exponential Tail Estimates for Quantum Lattice Dynamics*,
DOI 10.1007/s00023-025-01598-4](https://doi.org/10.1007/s00023-025-01598-4)
([arXiv:2408.02108](https://arxiv.org/abs/2408.02108)). Its introduction
relates the ballistic propagation region to group velocity; Sec. 4.2,
Lemma 4.1 discusses the convex hull of finite jumps. Sec. 5.4 explicitly
distinguishes one-parameter branches through a conical point from
multivariable analyticity. These passages were read on 2026-09-16. They
are relevant prior context, not an independent review of (2)-(8) or an
identification of exact support with ballistic propagation. Whether this
precise formulation is already published has not been exhaustively audited.

The author derivation closes the frozen analytic obligations on paper;
its project evidence level remains PRELIMINARY pending independent review.
It supports a ceiling, not a mechanism selecting equality. The certified
s=4 strict inequality remains a counterexample to strong matching and is
compatible with the ceiling. L1 remains a separate candidate; the metric
identity remains family-specific; the vertex-nilpotency erratum stands.
Neither full C authorization nor the next C calculation follows from this
report. **NOVELTY = OPEN.**
