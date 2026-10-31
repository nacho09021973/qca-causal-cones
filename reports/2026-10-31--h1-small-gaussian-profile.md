# Small fixed Gaussian profile: first correction and a survival bound

Date: 2026-10-31. Author: Codex (OpenAI).
Preregistration: `6ef57da`, support corrected **before execution** at
`067f8fa`; corrected contract SHA256
`d739db6b4b476c79c4a51d9a26f0dcf03dda31b5c3d818b8b0d040f6e972cddd`.
Status: **SMALL_PROFILE_SURVIVAL_PROOF_WRITTEN /
INDEPENDENT_REVIEW_PENDING**. Evidence level: **PRELIMINARY**.

This executes only the user's selected small-profile step after bridge
consolidation at `2e6af3a`. It is a candidate proof, not a canonical H1 PASS.
No external review of this new result has been requested or performed.

## 1. Objects and result claimed for review

Use the corrected [contract](../theory/H1_SMALL_GAUSSIAN_PROFILE_GATE.md),
the [promoted bridge](2026-09-24--schur-stability-physical-transfer.md),
and T1 without modifying their operators or observable. Write

\[
V_N\psi(x)=e^{-|x/N|^2}\psi(x),\quad B_N=V_N\beta,\quad
U_\varepsilon=e^{-i\varepsilon B_N/N}D,\quad D=S\oplus S^{-1},
\quad J\phi=(\phi,0),\quad Z=\operatorname{diag}(I_2,-I_2).
\tag{1}
\]

Fix M=sigma_2, M_B=I, f_0=(U_M-I)phi_N, E=h_N I and the physical
reference r_{+,epsilon}=1_B pi_+ U_epsilon^N J phi_N. In this report
`mathcal F_N` is a scalar functional, distinguished from Alice's spatial
profile F_N(x):

\[
\mathcal F_N(\varepsilon)
=2\Re\langle r_{+,\varepsilon},ES^Nf_0\rangle,\qquad
A_N=N^{-13/2}e^{-K_*N}.
\tag{2}
\]

All constants below are independent of N and of real |epsilon|<=1,
unless a smaller fixed interval is explicitly chosen. The profile shape,
pair, geometry, and tilt are fixed. Constants in bridge statements may
depend on the fixed admissible W. No W_N is allowed.

The candidate conclusions are:

1. `mathcal F_N` is exactly even. Its linear derivative at zero vanishes;
   the first potentially nonzero correction is quadratic, given explicitly
   by (8). Its coefficient is not asserted nonzero.
2. There is C<infinity, independent of N and epsilon, such that
   `|mathcal F_N(epsilon)-mathcal F_N(0)| <= C epsilon^2 A_N`.
   A fourth-order Taylor remainder is controlled on the same scale.
3. There exist epsilon_0>0 and N_0<infinity, independent of each other,
   such that for all |epsilon|<=epsilon_0 and N>=N_0 the **full** L_+ is
   negative and `|L_+|=Theta(A_N)`, uniformly in epsilon; L_-=O(N^-7 e^-K*N)
   uniformly there. This is conditional on the frozen flat theorem and
   promoted bridge, with their hypotheses checked below.

Neither a new coefficient C_epsilon(theta) nor equality to the flat
coefficient is claimed. Uniform scale/sign survival is weaker than a full
asymptotic expansion at nonzero epsilon.

## 2. Gaussian admissibility and a useful Banach norm

With v(X)=exp(-|X|^2), direct product Gaussian integration gives

\[
\widehat v(k)=\pi^{3/2}e^{-|k|^2/4},\quad
a_0(v)=\int\widehat v(k)\frac{d^3k}{(2\pi)^3}=1,\quad
a_1(v)=\int|k|\widehat v(k)\frac{d^3k}{(2\pi)^3}
=\frac4{\sqrt\pi}.
\tag{3}
\]

The last identity uses radial density
`r^2 exp(-r^2/4)/(2 sqrt(pi))`. Thus the bridge's F condition holds,
uniformly for |epsilon|<=1. Define
`||psi||_W=integral_T ||psi_hat(p)|| dmu(p)`. Fourier inversion implies
`sup_x||psi(x)||<=||psi||_W`. Multiplication by V_N has W-operator norm
at most a_0(v)=1: its Fourier action is convolution with the periodized
pushforward of the positive Gaussian measure under k->-k/N. All periodic
images are included. The real-momentum D is unitary in each fiber, hence
`||D psi||_W=||psi||_W` exactly. Beta also has norm one in each fiber.

The exact resource of ir-corona.tex gives

\[
\|J\phi_N\|_{\mathcal W}=C_\phi N^{-3/2},\qquad
C_\phi=\frac{\sqrt{3465}}{210\pi},
\tag{4}
\]

by integrating g(q)=(1-|q|^2)^2 on its unit ball and using its exact Z_N.
This is a norm of the full untruncated resource, not of a spatial cutoff.

## 3. Parity, exact quadratic coefficient and remainder

Since ZD=DZ, ZB_NZ=-B_N and ZJ=J,

\[
U_{-\varepsilon}^N J=ZU_\varepsilon^N J.
\tag{5}
\]

The physical plus amplitudes are even and minus amplitudes are odd in
epsilon, for both preparations. Consequently both primary signed responses
L_+, L_- and the retained functional (2) are even. In particular
`mathcal F_N'(0)=0` for every N, without a momentum-conservation assumption.

Expand the entire finite product
`U_epsilon^N=sum_(m>=0) epsilon^m W_(m,N)`. Each coefficient consists of
all compositions n_1+...+n_N=m with factors
`(-i/N)^m (B_N^n_N/n_N!)D ... (B_N^n_1/n_1!)D` in that order. Thus

\[
\|W_{m,N}\|_{\mathcal W\to\mathcal W}
\le\frac1{N^m}\sum_{n_1+\cdots+n_N=m}\frac1{n_1!\cdots n_N!}
=\frac1{m!}.
\tag{6}
\]

The same bound holds in l2, since ||V_N||_infty=1 and D is unitary.
Only even m contribute to pi_+ W_(m,N) J. Direct differentiation yields
the following exact operator on the original spin space:

\[
\begin{split}
\mathscr A_N:=\pi_+W_{2,N}J
={}&-\frac1{2N^2}\sum_{j=0}^{N-1}
 S^{N-1-j}V_N^2S^{j+1}\\
&-\frac1{N^2}\sum_{0\le j<k\le N-1}
 S^{N-1-k}V_NS^{-(k-j)}V_NS^{j+1}.
\end{split}
\tag{7}
\]

The first sum is the second derivative inside a **single coin**; omitting
it would change the result. The second sum is the ordered two-time
contribution, including propagation in the reciprocal channel between
insertions. Multiplication V_N is not commuted through S.

**Second derivation of the insertion ordering.** Write the channel
amplitudes after j steps as `a_j=S^j phi+epsilon^2 a_(2,j)+...` and
`b_j=epsilon b_(1,j)+...`. The exact cosine/sine coin recurrence gives

\[
\begin{aligned}
b_{1,j+1}&=S^{-1}b_{1,j}-\tfrac iN V_NS^{j+1}\phi,\\
a_{2,j+1}&=Sa_{2,j}-\tfrac1{2N^2}V_N^2S^{j+1}\phi
 -\tfrac iN V_NS^{-1}b_{1,j},
\end{aligned}
\]

with zero initial correction vectors. Solving the first recurrence and
substituting into the second reproduces both ordered sums in (7), including
the exponent `-(k-j)` and the negative sign of the two-time term. This is
a general-N check independent of the formal three-step verifier.

The first potentially nonzero scalar correction is therefore

\[
\mathcal Q_N=2\Re\langle 1_B\mathscr A_N\phi_N,ES^Nf_0\rangle,
\quad \mathcal F_N''(0)=2\mathcal Q_N,
\quad
\mathcal F_N(\varepsilon)=\mathcal F_N(0)+\varepsilon^2\mathcal Q_N
 +\mathcal R_N(\varepsilon).
\tag{8}
\]

No sign or nonvanishing of Q_N is established. From (4)–(6), uniformly
in N and y,

\[
\begin{aligned}
\|\pi_+U_\varepsilon^NJ\phi_N(y)-S^N\phi_N(y)\|
 &\le C_\phi N^{-3/2}(\cosh|\varepsilon|-1),\\
\|\mathscr A_N\phi_N(y)\|&\le\tfrac12 C_\phi N^{-3/2},\\
\|\pi_+U_\varepsilon^NJ\phi_N(y)-S^N\phi_N(y)
 -\varepsilon^2\mathscr A_N\phi_N(y)\|
 &\le C_\phi N^{-3/2}
 (\cosh|\varepsilon|-1-\varepsilon^2/2).
\end{aligned}
\tag{9}
\]

These bounds concern the actual inhomogeneous reference, before Bob's
effect. For |epsilon|<=1 the two scalar parentheses are at most
`(cosh(1)-1) epsilon^2` and `(cosh(1)-3/2) epsilon^4`, respectively,
by their nonnegative power series. Thus no order-of-limits argument or
N-dependent smallness assumption has entered.

For completeness, the full L_+ has a different quadratic coefficient.
Let a_0=S^N phi_N, b_0=S^N f_0, a_2=Acal_N phi_N, b_2=Acal_N f_0,
with restrictions/effects understood. Its coefficient is
`2 Re<a_2,E b_0>+2 Re<a_0,E b_2>+2 Re<b_0,E b_2>`.
Only the first summand is Q_N. We do not silently replace L_+ by (2);
the full response is treated in Sec. 7 using the reviewed bridge.

## 4. Integrated tilted-kernel norm: the scale-critical bound

Set Lambda=exp(Phi_*), M(p)=S(p-i xi_*)/Lambda and

\[
I_N=\int_{\mathbb T^3}\|M(p)^N\|\,d\mu(p).
\]

We need an integrated norm, not a sup_p norm. The required estimate is

\[
I_N\le C_K N^{-3/2},\qquad N\ge2.
\tag{10}
\]

Here is a direct proof from the fixed symbol. Its determinant is one and
half-trace f(p-i xi_*)=product_j cos(p_j-i t_*). The checked ellipse-product
argument of ir-corona.tex, `lem:specrad`, gives rho(M)<=1, with equality
exactly at the eight points Sigma={0,pi}^3. No other maxima are discarded.
At p=0 the dominant root is Lambda, separated from Lambda^-1. Its local
logarithm has real part

\[
\Re\log(\lambda(p)/\Lambda)
=-\tfrac12p^TQp+O(|p|^3),\qquad
Q=q_t(I-\hat u\hat u^T)+q_n\hat u\hat u^T>0.
\tag{11}
\]

For clarity, differentiating Phi(xi)=arcosh(product cosh xi_j) at
xi_*=t_*u, with c=cosh t_*>1 and d=sqrt(c^6-1), gives
`q_t=c/d` and `q_n=c(c^6-3c^2+2)/d^3`
`=c(c^2-1)^2(c^2+2)/d^3>0`. Analyticity and the positive minimum eigenvalue
give a fixed small ball with
`Re log(lambda/Lambda)<=-c_0|p|^2` and bounded Riesz projectors.

For alpha in Sigma, f(alpha+p-i xi_*)=s_alpha f(p-i xi_*) with
s_alpha=(-1)^(sum alpha_j/pi). The two roots there are
`s_alpha lambda(p)` and `s_alpha lambda(p)^-1`, so their moduli have the
same local bounds. The projector
`(S(alpha+p-i xi_*)-(s_alpha lambda(p))^-1 I)`
`/(s_alpha lambda(p)-(s_alpha lambda(p))^-1)` is analytic and bounded
on a smaller fixed closure. There are finitely many such neighborhoods.
The subdominant normalized root has modulus at most some fixed r<1 on
these closures. Thus in every neighborhood

\[
\|M(\alpha+p)^N\|\le C(e^{-c_0N|p|^2}+r^N).
\tag{12}
\]

On the compact complement of these neighborhoods rho(M)<=r_out<1.
The elementary unitary Schur triangularization of each 2x2 M gives
`||M(p)^N||<=r_out^N+C N r_out^(N-1)` uniformly, including repeated roots;
no exterior diagonalization is required. The compact symbol norm is bounded.
Integrating (12) in three real dimensions gives C N^-3/2. The exterior
and subdominant exponentials satisfy the same bound after increasing C,
because `sup_(x>=2) x^(5/2) exp(-a x)<infinity` for every fixed a>0.
This proves (10). The proof does not require a claim about cancellation
of the six other saddles, any moving W, or the full localization program.

## 5. Weighted layer masses with the complete Alice source

Put R=N/4, u=(1,1,1), gamma=sqrt(3)t_*, x_*=R uhat,
y_*=Nu-R uhat, so y_*-x_*=Nv_* and xi_*.v_*-Phi_*=K_*.
At depth delta=(theta_N+j)/sqrt(3), the plane intersects either ball in a
disk of squared radius at most N delta/2. Projection onto the first two
integer coordinates is injective on a plane u.x=k. The number of sites is
therefore at most `(2 radius+2)^2<=8(1+radius^2)<=8(1+N delta)`.
This remains valid for translated disks and all fractional theta_N.

The exact smooth profiles satisfy F_N(x),h_N(y)<=64 delta^2/N^2.
Moreover `||(U_M-I)phi_N(x)|| <= (pi/2) F_N(x) C_phi N^-3/2`, since
M=sigma_2 is a Hermitian involution and `|exp(it)-1|<=|t|` for real t.
This includes the cosine part of the encoder.

Write q=exp(-t_*) and define the finite constant

\[
H=\frac{1+q}{3(1-q)^3}
 +\frac{1+4q+q^2}{3\sqrt3(1-q)^4}.
\tag{13}
\]

Indeed the normal-depth sum
`sum_j exp(-t_*(theta+j)) delta_j^2(1+delta_j)` is at most H,
using delta_j<=(j+1)/sqrt(3) and the elementary geometric moments.
Since `1+N delta<=N(1+delta)` for N>=2, the complete source has mass

\[
a_N:=\sum_{x\in A}e^{\xi_*\cdot(x-x_*)}\|f_0(x)\|
\le C_A N^{-5/2},\qquad C_A=256\pi C_\phi H.
\tag{14}
\]

More generally, for any spinor z_N(y) with
`sup_y||z_N(y)||<=C_phi h N^-3/2`, its effected Bob mass obeys

\[
b_N(z):=\sum_{y\in B}e^{-\xi_*\cdot(y-y_*)}h_N(y)\|z_N(y)\|
\le C_B h N^{-5/2},\qquad C_B=512C_\phi H.
\tag{15}
\]

In (15) h is a nonnegative scalar bound, not the detector h_N.
The sign of the outgoing tilt is negative in the exponent; both normal
weights are exp(-t_*(theta_N+j)). No physical tail was tilted globally.

## 6. Comparison and Taylor remainder on the signal scale

The exact contour representation of the finite Alice-to-Bob kernel gives
for any z_N restricted to Bob

\[
\left|2\Re\langle 1_Bz_N,ES^Nf_0\rangle\right|
\le2e^{-K_*N}a_N b_N(z) I_N.
\tag{16}
\]

It can also be read directly from the finite double sum: shift each kernel
to p-i xi_*, split its real weights at x_*,y_* and bound the two endpoint
Fourier sums by their weighted l1 masses. These sums are finite, so the
entire-symbol contour shift does not involve the infinite preparation tail.
The right side uses the integrated matrix norm I_N, not just a spectral
radius or a pointwise kernel asymptotic.

Apply (16) to the reference difference, quadratic coefficient, and remainder
in (9). With D_*=2 C_A C_B C_K (a new bound constant, unrelated to any
earlier symbol named D), we obtain

\[
\begin{aligned}
|\mathcal F_N(\varepsilon)-\mathcal F_N(0)|
 &\le D_*(\cosh|\varepsilon|-1)A_N
 \le C_*\varepsilon^2 A_N,\\
|\mathcal Q_N|&\le\tfrac12D_* A_N,\\
|\mathcal R_N(\varepsilon)|
 &\le D_*(\cosh|\varepsilon|-1-\varepsilon^2/2)A_N
 \le D_*(\cosh1-3/2)\varepsilon^4 A_N,
\qquad C_*=D_*(\cosh1-1).
\end{aligned}
\tag{17}
\]

The power is `5/2+5/2+3/2=13/2`. Bounds (17) supply the scale control
which a plain l2 continuity bound misses. Q_N/A_N is bounded; no limit,
theta-dependent asymptotic coefficient, or nonvanishing of Q_N is inferred.

## 7. Uniform bridge transfer and small-amplitude survival

The bridge's constants can be chosen uniformly on |epsilon|<=1 here.
Specifically b=|epsilon|<=1, a_0=|epsilon|<=1 and
a_1=4|epsilon|/sqrt(pi)<=4/sqrt(pi). Its unperturbed R, P, Q, W and
exterior separation constants do not vary with epsilon. The estimate
`||T_epsilon-R||<=|epsilon| ||R||/N` gives uniformly bounded off-diagonal
block constants. Choose one rho_2 in (rho,1) and one sufficiently large
N_1 so that `rho+a/N<=rho_2` for all |epsilon|<=1. The product stability
and double Schur sums then have common constants. In the compressed-P
comparison, `||A_epsilon-R_P||<=C_W(|epsilon|a_1(v)+epsilon^2)/N^2`
also has a common bound. Bob's real Fourier L1 estimate costs at most e,
and Alice is unchanged. No step divides by epsilon. Thus the complete
proof of the promoted bridge, not just a compactness assertion about its
conclusion, supplies C_W,N_1 uniform on this interval:

\[
\begin{aligned}
L_{+,\varepsilon}
 &=\mathcal F_N(\varepsilon)
   +O_W(N^{-7}e^{-K_*N})+O_W(N^{-8}e^{-2K_*N}),\\
L_{-,\varepsilon}
 &=O_W(N^{-7}e^{-K_*N})+O_W(N^{-8}e^{-2K_*N}).
\end{aligned}
\tag{18}
\]

Keep all quadratic pieces in this comparison: their sum per channel is
the nonnegative `||E^(1/2)(d_P+d_Q)||^2`, not a discarded signed cross term.
Uniformity of (18) does not require uniformity in W.

For epsilon=0, the flat reference is exact. The accepted flat theorem in
its sigma_2/I scope gives a continuous negative coefficient C_0(theta),
uniformly separated from zero. Equivalently, with

\[
m=\min_{\theta\in[0,1]}(-C_0(\theta))>0,\quad
M_0=\max_\theta|C_0(\theta)|<\infty,
\]

`L_(+,0)/A_N=C_0(theta_N)+O(N^-1/2)`. At zero the linear functional
differs from full L_flat only by the quadratic source term, bounded in
(18) and negligible relative to A_N. Therefore

\[
\mathcal F_N(0)/A_N=C_0(\theta_N)+O(N^{-1/2}).
\tag{19}
\]

Choose

\[
\varepsilon_0=\min\{1,\sqrt{m/(4C_*)}\}>0.
\tag{20}
\]

For one N_0 independent of epsilon, the remainder in (19) and the total
bridge error in (18) are each at most m A_N/4. The latter follows from
`N^-7 e^-KN / A_N=N^-1/2` and the exponentially smaller quadratic term.
Equations (17)–(20) then imply for every |epsilon|<=epsilon_0, N>=N_0:

\[
\boxed{L_{+,\varepsilon}\le-\tfrac14m A_N<0,\qquad
\tfrac14m A_N\le|L_{+,\varepsilon}|\le C A_N,\qquad
|L_{-,\varepsilon}|\le C_W N^{-7}e^{-K_*N}=o(A_N).}
\tag{21}
\]

This proves the stated candidate **scale and sign persistence** uniformly
on one fixed epsilon interval, assuming the already accepted flat theorem
and promoted bridge. The positive epsilon_0 and N_0 are not numerically
effective here, since C_K and the baseline remainder thresholds were not
made effective. No finite-N signal value is predicted.

## 8. Checks, sources and stop

The source walk was checked directly in `sources/2408.02108v1.pdf p.17`,
Eq. (5.15); S is its inverse with the repository's explicit Fourier sign.
That paper defines the walk, not the inhomogeneous survival result.
The full jump support was checked in ir-corona.tex's explicit symbol and
Jumps lemma: fourteen jumps, not merely the eight vertices. The preregistered
contract was corrected before any result execution. The local library index
is absent; no external prior-art or novelty conclusion is made.

Primary in-repo definitions and checked baseline inputs are ir-corona.tex,
the Protocol section, exact tilted representation, spectral-radius and
Schur-power proofs, tilted-symbol Hessian, and the accepted flat sigma_2/I
coefficient theorem. Sections 2–7 above derive the new estimates explicitly;
the prior AI review is not used as a substitute for these arguments.

The permanent verifier
[`verify_small_gaussian_profile_algebra.py`](../scripts/verify_small_gaussian_profile_algebra.py)
passes 21 exact SymPy 1.14.0 checks. It checks Gaussian normalization and
moment, resource normalization, channel parity, the exact noncommutative
three-step quadratic formula with a negative control that omits single-coin
terms, Hessian factorization, geometric moments and exponent arithmetic.
This one abstract three-step identity is not a physical N scan or evidence
of an asymptotic law. General-N product ordering and all analytic estimates
are proved in this text, not by that finite algebra check.

Reproduce from the repo root:

```sh
/home/adnac/venvs/torch-gpu/bin/python -B scripts/verify_small_gaussian_profile_algebra.py
```

The corrected contract is pinned in the verifier by SHA256. No reviewed
verifier, source manuscript or T1 file was edited. The unedited external
review archives contain original trailing whitespace; checks on authored
state/report/code changes are separated from archival byte preservation.
New verifier SHA256:
`5647b1d52cce9392bac6d239ae4dd40b31b147b1e3541ee170b08c475990cfa2`.

The existing, unchanged `verify_regional_laplace_coefficient_gate.py` was
also run once in its default exact mode in the same interpreter: **58/58
checks pass**, including the uniform negative sigma_2/I coefficient margin
and the positive Hessian eigenvalues used here. That verifier does not
encode the baseline analytic remainder or any new estimate in this report.
Unchanged baseline verifier SHA256:
`d008417debe149743396bfbeb7d55be11fe7aa00bce3b4aecebf6a50997884b2`.

Stop: this bounded gate execution is complete at **proof written / review
pending**. The new survival claim is PRELIMINARY, not installed as H1 PASS.
The coefficient Q_N may vanish, and its normalized asymptotic behavior is
OPEN. General H1/H1c localization, general profiles/pairs, E0, general
POWER_13/2_STABILITY and E/AdS retain their prior scope/status. No external
review, broader investigation, parameter scan or publication follows
automatically from this report.
