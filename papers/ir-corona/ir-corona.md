# An infrared operational response outside the emergent light cone of a three-dimensional Weyl quantum walk

> **Markdown transcription for review.** Source: `papers/ir-corona/ir-corona.tex`
> (pre-publication revision of 2026-09-18). Section, theorem, equation and
> reference numbers match the compiled PDF. If this file and the `.tex`
> disagree, the `.tex` is authoritative. The prior art of the revised Markdown
> draft (`papers/ir-corona-operational-response-draft.md`, commit `9812cbc`) is
> now merged: Carteret–Richmond–Temme, Baryshnikov–Brady–Bressler–Pemantle,
> ACSV, and the narrowed novelty statement.

**José Ignacio Martín Gandul**  
Independent Researcher, Seville, Spain

## Abstract

In a finite-range quantum walk the relativistic light cone that emerges at
long wavelength need not exhaust the strict microscopic causal support. We
study the three-dimensional Weyl walk introduced by Cedzich, Joye, Werner and
Werner as a model with a spherical propagation region. All of its group
velocities lie in the closed Euclidean unit ball, which is also the light
cone of its Weyl node. Its one-step causal support is the cube $[-1,1]^3$.
Velocities in the cube but outside the ball form a *corona*. There,
propagation is non-ballistic but not causally forbidden.

We ask whether the corona carries an operational response that survives
infrared control. Alice prepares a narrow-band state and applies a local
encoding, and Bob reads out with a local detector. All three operations are
required to be infrared-admissible: acting on the band $|p|\le N^{-1}$, each
has an outside-band map whose operator norm is vanishingly small relative
to the norm of its restriction to the input band, with wider output band
$|p|\le N^{-1/2}$. This is not a per-input leakage-fraction bound. Bob's
region lies outside the emergent light cone of every site of Alice's region.
After $N$ steps, Bob's distinguishability $\delta(N)$ obeys the explicit
bound $\delta(N)\le 36N^4e^{-JN}$ with $J=(1-\sqrt3/2)\log 2$. For the twelve
Pauli encoder–detector pairs of a concrete family, it has the exact leading
asymptotics

$$
\delta(N)=\bigl|C(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad \theta_N=\{\sqrt3N/4\}.
$$

Here $K_*\approx0.1905$ is the value of a Legendre rate function at a unique
regional minimiser. The coefficient $C(\theta)$ is given in closed form, and
interval arithmetic shows that it does not vanish for any $\theta$ in any of
these pairs; four further pairs with $M=I$ serve as reference controls. The emergent cone is therefore not operationally sharp,
even for infrared-admissible operations. The response is non-perturbatively
small, invisible to every power of the infrared scale, and it lies strictly
inside the microscopic causal support. The result is purely asymptotic: the
remainder constants are not explicit, and the diagnostics do not establish
quantitative accuracy of the exact-signal asymptotic at a specified size.

---

## 1. Introduction

Quantum cellular automata and quantum walks are unitary dynamics on a lattice
with a strict bound on the speed of propagation [18, 2, 12]. After $N$ steps
of a finite-range walk, the propagator vanishes identically outside
$N C_{\mathrm{micro}}$. Here $C_{\mathrm{micro}}=\operatorname{conv}F$ is the
convex hull of the one-step jumps. Many such walks have a conical point in
their dispersion relation. Near it, the long-wavelength dynamics is that of a
Weyl or Dirac equation with a speed of light $c_{\mathrm{IR}}$ [4, 11, 5, 10].

In spatial dimension $d\ge2$ the two causal structures cannot coincide. The
infrared cone of a Weyl node is a Euclidean ball, and $C_{\mathrm{micro}}$ is
a polytope. Exact isotropy of the microscopic causal structure is incompatible
with a regular lattice. It can be compatible with random discreteness, as in
the causal-set theorem of Bombelli, Henson and Sorkin [6], but that setting
lies outside the scope of this paper. For a lattice walk, some velocities are
therefore causally allowed but not relativistic. How much physics can be sent
through them?

Three questions must be kept apart.

- **(U) Ultraviolet propagator.** Does the exact kernel assign non-zero
  amplitude to sites outside the infrared ball but inside
  $N C_{\mathrm{micro}}$? For the walk studied here it does: along the eight
  vertex rays a single lattice path contributes, with amplitude of norm
  $4^{-N}$ (Proposition 2.2). One-step Alice/Bob protocols built from
  localized operations turn this into a finite distinguishability (for
  instance $3/128$ after one step for a suitable localized preparation, as
  recorded in [17]). Such protocols are broadband: their operations are not
  concentrated near the Weyl node.
- **(I) Infrared operational response.** Require the preparation, the encoder
  and the detector to be infrared-admissible, and put Bob outside the
  infrared cone of *every* site of Alice. Does Bob's distinguishability still
  fail to vanish as the infrared scale goes to zero, and at what rate?
- **(N) Nature.** Is there a physical system in which the lattice scale and
  the operations are given rather than engineered? This question is not
  addressed here.

A non-zero ultraviolet kernel does not answer (I). Infrared admissibility
could in principle force exact cancellations, and conversely an exponentially
small infrared response is compatible with (U). This paper answers (I), for
one walk and one explicit protocol.

### The walk

We work with the Weyl walk of Cedzich, Joye, Werner and Werner
[9, Eq. (5.15)]. They introduced it as a modification of the
Bialynicki-Birula Weyl automaton [9, Eq. (5.12)], [4], with the same conical
points and with a *spherical* propagation region. For this walk the three
velocity sets are nested as

$$
\Gamma\;\subseteq\;B(1)\;\subsetneq\;C_{\mathrm{micro}}=[-1,1]^3,
\qquad \sup_{v\in\Gamma}|v|=c_{\mathrm{IR}}=1 .
\tag{1}
$$

Here $B(1)=\overline B(0,1)$ is the closed infrared light cone
($c_{\mathrm{IR}}=1$), $\Gamma$ is the closed set of group velocities, and
$C_{\mathrm{micro}}$ is the strict causal body. Both statements in (1) are
exact, and moreover $\partial B(1)\subseteq\Gamma$ (Proposition 2.2).
Numerically, $\Gamma$ fills the ball; this is not proved and not used. Every
ballistic mode, at every energy, therefore respects the emergent light speed.
Nevertheless, for every non-axial unit vector $\hat n$ the support
function of the causal cube is $h(\hat n)=\|\hat n\|_1>1$.
Its radial extent along the ray $r\hat n$ is instead
$r_{\max}=1/\|\hat n\|_\infty>1$; these are distinct geometric quantities. Probability outside
$\Gamma$ is exponentially small in $N$ [9]. The question is whether it can be
*used* under infrared control.

### Main results

Section 3 gives the precise definitions. In outline, Alice's region is the
lattice ball $\mathcal A_N$ of radius $N/4$ at the origin, and Bob's region
is the lattice ball $\mathcal B_N$ of radius $N/4$ at $N(1,1,1)$. After $N$
steps, every pair $(x,y)\in\mathcal A_N\times\mathcal B_N$ is separated by
more than $N+N/5$. Bob is thus outside the emergent cone of every site of
Alice, with a margin of order $N$. The resource is a narrow-band packet of
momentum width $\Lambda=1/N$. Alice's encoder is a smooth local unitary
$\exp(i\frac\pi2F_N(x)M)$ with $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$. Bob's
effect is $h_N(y)\otimes M_B$ with $M_B\in\{I,(I+\sigma_j)/2\}$. The
profiles $F_N,h_N$ are smooth bumps of width $N/4$ that vanish
quadratically on the spheres.

1. *Infrared admissibility* (Theorem 3.3). All eight operations map the band
   $|p|\le N^{-1}$ into the band $|p|\le N^{-1/2}$, up to relative errors
   $O(N^{-1/2})$ with explicit constants. Single-site operations fail this
   criterion maximally (Lemma 3.2).
2. *Explicit upper bound* (Theorem 4.1). For every $N\ge2$, every unitary
   acting in $\mathcal A_N$, every one-particle state and every effect in
   $\mathcal B_N$, Bob's distinguishability is at most $36N^4e^{-JN}$, with
   $J=(1-\tfrac{\sqrt3}{2})\log2$. Polynomial infrared signalling is
   excluded.
3. *Regional rate* (Theorem 4.3). The kernel between the two regions is
   $O(N^4)\,e^{-K_*N}$, where $K_*=I(v_*)$ is the minimal regional value of
   a Legendre rate function. Here $I$ is the Legendre transform of
   $\Phi(\xi)=\operatorname{arcosh}(\prod_j\cosh\xi_j)$, and
   $v_*=(1-\frac1{2\sqrt3})(1,1,1)$ is the unique minimiser of $I$ over the
   regional velocity set. Moreover $J<K_*<\log4$. By item 4, the rate $K_*$
   is attained by an explicit response.
4. *Leading asymptotics* (Theorem 4.4). For the twelve Pauli
   encoder–detector pairs ($M\ne I$; the four pairs with $M=I$ are
   reference controls),
   $\delta_{M,M_B}(N)=|C_{M,M_B}(\theta_N)|N^{-13/2}e^{-K_*N}(1+O(N^{-1/2}))$.
   The coefficient $C_{M,M_B}(\theta)$ is given in closed form and is
   uniformly non-zero, with relative oscillation in $\theta$ at most
   $1.5\times10^{-3}$.

Result 4 is an asymptotic statement and not a numerical approximation valid
from small $N$. The constants in its remainder are not explicit, and neither
is the threshold $N_*$ beyond which $\delta_{M,M_B}(N)>0$ is guaranteed.
Finite-$N$ diagnostics (Appendix A) indicate a correction of about $-100/N$ in a semi-analytic approximation; this does
not establish an accuracy threshold for the exact signal. For the pairs with the smallest coefficients, the next-order
term $N^{-17/2}e^{-K_*N}$ dominates throughout the diagnostic range $N\le56$
(Remark 4.6).

The coefficient is not a product of local factors. It arises from the
interference between the *free tail* of the resource at Bob, which is only
polynomially small, and the part of Alice's encoding that reaches Bob, which
is exponentially small. Two points of the complex-shifted Brillouin torus
contribute, and they enter with different projectors. The power $13/2$ is
not a count of Gaussian directions. The two normal directions are discrete
sums over lattice planes of depth $O(1)$, and the common tangential direction
is a flat direction of the exponent that is confined only by the profiles.

### Relation to the literature

Ballistic scaling and weak limit theorems for translation-invariant quantum
walks are classical [14, 13, 1]: $Q(t)/t$ converges in distribution to the
group velocity distributed by the initial state. Cedzich, Joye, Werner and
Werner [9] proved that the probability of velocities outside the support of
this limit decays exponentially. They gave a method for bounding the rate
uniformly in the initial state and discussed the "fuzziness" of the emergent
light cone in exactly this language. Our upper bound (item 2) uses their
contour-shift idea, supplemented by an elementary ellipse lemma and a
Jordan-safe bound on matrix powers. Their method bounds rates; it does not
give prefactor-level asymptotics.

In particular their diagonal tilt formula
[9, Eq. (5.21)] is
$\widetilde R(\ell)=2\arcosh(\cosh^3(\ell/(2\sqrt3)))$.
With $\ell=2\sqrt3t$, this is $2\Phi(tu)$, and the corresponding
probability-rate transform at $r=\sqrt3-1/2$ equals $2K_*$.
Thus the diagonal rate formula is prior art. Our argument proves the
spectral bound used here and identifies the regional minimiser; the
operational prefactor is a separate calculation.

Sharp asymptotics with prefactors outside the propagation region are known in
one dimension. Sunada and Tate [19] obtained exact local asymptotics of
transition probabilities, including exponential decay with an explicit
prefactor in the region hidden from the weak limit. Carteret, Richmond and
Temme [8] obtained uniformly convergent asymptotics in the exponentially
decaying regions of coined walks on the line. These are the closest
precursors of the saddle-point analysis of Section 7. In two dimensions,
Baryshnikov, Brady, Bressler and Pemantle [3] analysed quantum walks through
multivariate generating functions and determined the limiting profile in the
feasible region, outside of which the probability is exponentially small;
the shape theorem they prove gives $O(e^{-cn})$ uniformly on compact subsets
of the complement of the feasible region, and prefactor asymptotics only
inside it [20, Thms. 2.2–2.3]. Analytic combinatorics in several variables
[16] provides general transfer theorems for multivariate coefficient
asymptotics, whose standard sharp forms assume minimality hypotheses on the
critical points. In its quantum-walk examples the asymptotics hold uniformly
for directions in compact subsets of the feasible region, and outside it the
conclusion is exponential decay [22, Thm. 12.12 and its proof, Thm. 12.14];
the quadratic-point theory gives asymptotics uniformly over compact subcones
of the interior of the dual cone and only exponential smallness outside it
[21, Thm. 3.7]. Cedzich, Joye, Werner and Werner count two studies of the
asymptotics outside the propagation region, both of walks on the line
[9, Sec. 5.1], namely [8, 19]. We do not claim that
these methods cannot reproduce the present result. We are not aware of a
transfer theorem that yields it directly, and we carry out the model-specific
saddle-point analysis explicitly.

What we add is a *lower* bound, in the strong form of exact leading
asymptotics. It concerns an *operational* quantity: the distinguishability
produced by a local encoding. The encoding is spread over a region of size
$O(N)$ and constrained to be infrared-admissible, in dimension three, and at
a point strictly inside the corona. Upper bounds alone cannot distinguish an
exponentially small response from an exactly vanishing one. In the problem
studied here that distinction is the content of the result. The novelty
claim is correspondingly narrow. To our knowledge, Theorem 4.4 is the first
prefactor-level asymptotic, with a leading coefficient that is oscillatory and
certified to be non-vanishing, for an infrared-controlled operational response
in the strictly outside-propagation-region regime of a three-dimensional
multi-component quantum walk. Exponential decay outside the propagation
region, large-deviation rates, Weyl-cone dispersion and microscopic support
outside an emergent cone all have prior art, cited above.

Lieb–Robinson bounds [15, 7] give exponentially small leakage outside a
linear cone for continuous-time lattice dynamics. For quantum walks the
strict cone $C_{\mathrm{micro}}$ plays that role exactly, and the question
here is the one *inside* it.

### Organisation

Section 2 sets up the walk and proves the geometric statements. Section 3
defines the protocol and infrared admissibility. Section 4 states the
results. Sections 5 to 7 contain the proofs. Section 8 discusses scope and
limitations. Appendix A lists the computer-assisted parts and the finite-$N$
diagnostics.

---

## 2. The walk and its three velocity sets

### 2.1. Conventions

The one-particle Hilbert space is $\mathcal H=\ell^2(\mathbb Z^3;\mathbb C^2)$
with internal basis ${\uparrow}=(1,0)^T$ and ${\downarrow}=(0,1)^T$. We use the
Fourier transform $\hat\psi(p)=\sum_{x}e^{ip\cdot x}\psi(x)$, with inverse
$\psi(x)=\int_{\mathbb T^3}e^{-ip\cdot x}\hat\psi(p)\,d\mu(p)$ and
$d\mu=d^3p/(2\pi)^3$ on $\mathbb T^3=[-\pi,\pi)^3$. We write $c_j=\cos p_j$
and $s_j=\sin p_j$. $B(1)=\overline B(0,1)$ denotes the closed Euclidean unit
ball.

The walk $W$ of [9, Eq. (5.15)] has symbol

$$
W(p)=\begin{pmatrix} c_1c_2e^{ip_3} & -c_1s_2+is_1\\ c_1s_2+is_1 & c_1c_2e^{-ip_3}\end{pmatrix},
\qquad \det W(p)=1 .
$$

States evolve by the unitary $S$ with symbol

$$
S(p)=W(p)^{-1}=\begin{pmatrix} c_1c_2e^{-ip_3} & c_1s_2-is_1\\ -c_1s_2-is_1 & c_1c_2e^{ip_3}\end{pmatrix}.
\tag{2}
$$

Both are matrix-valued trigonometric polynomials, so they extend to entire
functions of $p\in\mathbb C^3$. For $p\in\mathbb C^3$, $S(p)$ denotes the
continuation of (2), which is the inverse of $W(p)$ and not its adjoint.
Writing $S(p)=\sum_dS_de^{ip\cdot d}$, the walk acts as
$(S\psi)(y)=\sum_dS_d\psi(y-d)$. The $N$-step kernel is

$$
(S^N)_{y,x}=G_N(y-x),\qquad G_N(d)=\int_{\mathbb T^3}e^{-ip\cdot d}S(p)^N\,d\mu(p).
\tag{3}
$$

**Lemma 2.1 (Jumps).** The set $F=\{d:S_d\ne0\}$ has fourteen elements: the
eight vertices $(\pm1,\pm1,\pm1)$, the four face diagonals $(\pm1,\pm1,0)$,
and the two axial jumps $(\pm1,0,0)$. Each vertex block is $\frac14$ times a
rank-one diagonal projector; in particular
$S_{(1,1,1)}=\frac14|{\downarrow}\rangle\langle{\downarrow}|$. The
face-diagonal blocks have norm $\frac14$ and the axial blocks have norm
$\frac12$, so that $\sum_d\|S_d\|=4$.

*Proof.* This is a direct expansion of (2) in $z_j=e^{ip_j}$. The coefficient
of $z_1z_2z_3$ comes only from the $(2,2)$ entry $c_1c_2e^{ip_3}$ and equals
$\frac14$. ∎

### 2.2. Dispersion and the infrared node

Since $\det S=1$ and $\operatorname{tr} S(p)=2c_1c_2c_3$, the eigenvalues of
$S(p)$ are $e^{\mp i\omega(p)}$ with

$$
\cos\omega(p)=\cos p_1\cos p_2\cos p_3 .
\tag{4}
$$

At $p=0$ one has $S(p)=I-iH_W(p)+O(|p|^2)$ with

$$
H_W(p)=p_1\sigma_1-p_2\sigma_2+p_3\sigma_3,\qquad H_W(p)^2=|p|^2I .
$$

This is a Weyl Hamiltonian with speed $c_{\mathrm{IR}}=1$. The same conical
structure occurs at the eight points of $\{0,\pi\}^3$.

**Proposition 2.2 (Geometry).**

- (a) The causal body is $C_{\mathrm{micro}}=\operatorname{conv}F=[-1,1]^3$.
  Its support function is $h_{C_{\mathrm{micro}}}(\hat n)=\|\hat n\|_1$ for
  unit vectors $\hat n$.
- (b) At every $p$ where $\omega$ is differentiable,

  $$
  \bigl(1-f^2\bigr)-|\nabla f|^2=s_2^2s_3^2+s_1^2s_2^2c_3^2+s_1^2c_2^2s_3^2\ \ge0,
  \qquad f=c_1c_2c_3,
  \tag{5}
  $$

  and hence $|\nabla\omega(p)|\le1$. At the conical points $\nabla\omega$
  takes every value in the unit sphere. Thus $\Gamma\subseteq B(1)$ and
  $\partial B(1)\subseteq\Gamma$, where $\Gamma$ is the closure of the set of
  group velocities.
- (c) For every vertex $\sigma\in\{\pm1\}^3$ and every $N\ge1$,
  $(S^N)_{N\sigma,0}=S_\sigma^N=4^{-N}\Pi_\sigma\ne0$, where $\Pi_\sigma$ is
  a diagonal rank-one projector. In particular
  $(S^N)_{(N,N,N),0}=4^{-N}|{\downarrow}\rangle\langle{\downarrow}|$. Hence the
  $N$-step support function equals $N\|\hat n\|_1$ exactly.

*Proof.* (a) follows from Lemma 2.1. The supremum of $\hat n\cdot x$ over the
cube is separable and equals $\sum_j|n_j|$.

(b) With $\cos\omega=f$ we have $\nabla\omega=-\nabla f/\sin\omega$ and
$\sin^2\omega=1-f^2$. The identity (5) is a polynomial identity in
$(c_j,s_j)$ modulo $c_j^2+s_j^2=1$, and is checked by expansion. Near a
conical point, $\omega(p)=|p-p_\vee|+O(|p-p_\vee|^2)$, so
$\nabla\omega=(p-p_\vee)/|p-p_\vee|+o(1)$ sweeps the unit sphere.

(c) Let $d_1+\dots+d_N=N\sigma$ with $d_k\in F$. Every $d\in F$ satisfies
$\sigma_i d_i\le1$ for each coordinate $i$, so $\sum_k\sigma_i(d_k)_i=N$
forces $\sigma_i(d_k)_i=1$ for all $i$ and $k$, that is, $d_k=\sigma$. Hence
$(S^N)_{N\sigma,0}=S_\sigma^N$. By Lemma 2.1, $S_\sigma=\frac14\Pi_\sigma$,
so $S_\sigma^N=4^{-N}\Pi_\sigma$. ∎

**Remark 2.3.** The reverse inclusion $B(1)\subseteq\Gamma$, that is, that
$\Gamma$ fills the ball, holds numerically but is not proved and not used.
What is used is the exact inclusion $\Gamma\subseteq B(1)$, equivalently
$\sup|\nabla\omega|\le c_{\mathrm{IR}}$, with equality by
$\partial B(1)\subseteq\Gamma$. Consequently the relation
$\sup|v_g|=c_{\mathrm{IR}}$ does *not* imply that the emergent cone coincides
with the causal boundary. The two coincide only in the six axial directions.
The *corona* is $C_{\mathrm{micro}}\setminus B(1)$. Propagation into $N$
times the corona is not ballistic, but by (c) it is not forbidden.

**Remark 2.4.** For the Bialynicki-Birula walk [9, Eq. (5.12)], $\Gamma$ is
contained in the intersection of three orthogonal cylinders (and numerically
equal to it [9, Fig. 5]). It contains group velocities up to
$\sqrt{3/2}>c_{\mathrm{IR}}$, attained at $p=-\frac\pi4(1,1,1)$. In that
walk the corona contains a ballistic sector faster than the emergent light.
We restrict to [9, Eq. (5.15)] precisely because it has no such sector.

---

## 3. Protocol and infrared admissibility

Fix an integer $N\ge2$. The infrared scale is $\Lambda_N=N^{-1}$ and the
admissibility budget is $\Lambda'_N=N^{-1/2}$. Let $\Pi_\Lambda$ denote the
spectral projection onto $\{|p|_2\le\Lambda\}$, and write
$\Pi=\Pi_{\Lambda_N}$ and $\Pi'=\Pi_{\Lambda'_N}$. For $N\ge2$ both balls lie
in $|p|<\pi/4$, where $f>0$ and the only conical point is $p=0$.

### 3.1. Regions

Let

$$
\mathcal A_N=\{x\in\mathbb Z^3:|x|\le N/4\},\qquad \mathcal B_N=\{y\in\mathbb Z^3:|y-N(1,1,1)|\le N/4\},
$$

with Euclidean norms throughout. For every $x\in\mathcal A_N$ and
$y\in\mathcal B_N$,

$$
|y-x|-N\ge\bigl(\sqrt3-\tfrac32\bigr)N>\tfrac N5,
\qquad
u\cdot(y-x)\ge\bigl(3-\tfrac{\sqrt3}2\bigr)N,\quad u=(1,1,1).
\tag{6}
$$

Both follow from the triangle inequality, and the last inequality in the
first display is $3>(17/10)^2$. Each region has at most $(N/2+1)^3\le N^3$
sites.

### 3.2. Resource, encoder, detector

Let $g(q)=(1-|q|^2)_+^2$. The resource is

$$
\hat\phi_N(p)=Z_N^{-1/2}\,g(Np)\,{\downarrow},
\qquad Z_N=\frac{64}{3465\,\pi^2N^3},
$$

so that $\|\phi_N\|=1$ and $\Pi\phi_N=\phi_N$. In position space
$\phi_N=\varphi_N\,{\downarrow}$ with the real, radial function

$$
\varphi_N(x)=N^{-3/2}\,\Phi_0(x/N),\qquad
\Phi_0(w)=c_r\int_{\mathbb R^3}g(q)\,e^{-iq\cdot w}\,d^3q,\qquad c_r=\frac{\sqrt{3465}}{64\pi^2}.
\tag{7}
$$

This is exact, with no truncation of the spatial tail.

Alice's profile is $F_N(x)=(1-16|x|^2/N^2)_+^2$, supported in
$\mathcal A_N$. For $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$ the encoder is the
multiplication operator

$$
U_M=\exp\bigl(i\tfrac\pi2F_N(x)\,M\bigr)=I+c_N(x)I+is_N(x)M,
\qquad c_N=\cos(\tfrac\pi2F_N)-1,\ \ s_N=\sin(\tfrac\pi2F_N).
$$

It acts as the identity outside $\mathcal A_N$. In the second-quantized free
fermion picture it is the one-particle restriction of an even,
number-preserving local unitary.

Bob's profile is $h_N(y)=(1-16|y-Nu|^2/N^2)_+^2$, with $u=(1,1,1)$,
supported in $\mathcal B_N$. For $M_B\in\{I,P_1,P_2,P_3\}$, with
$P_j=(I+\sigma_j)/2$, the effect is

$$
E=h_N\otimes M_B,\qquad 0\le E\le I .
$$

### 3.3. Signal

Alice encodes a bit $b\in\{0,1\}$ by applying $U^{(1)}=U_M$ or $U^{(0)}=I$
to the resource. After $N$ steps the state is $\psi_b(N)=S^NU^{(b)}\phi_N$.
The signal is

$$
\delta_{M,M_B}(N)=\bigl|\langle\psi_1,E\psi_1\rangle-\langle\psi_0,E\psi_0\rangle\bigr|=|L_{M,M_B}(N)|,
\tag{8}
$$

where $L_{M,M_B}(N)$ denotes the signed difference. No spectral projection is
applied to the signal. Infrared admissibility is a property of the operations
only. We also consider the trace distance $D_B(N)$ between Bob's reduced
states. In the free-fermion description, the reduced state of a one-particle
vector $\psi$ on the modes of $\mathcal B_N$ is
$(1-\|P_B\psi\|^2)|\Omega\rangle\langle\Omega|+|P_B\psi\rangle\langle P_B\psi|$,
and $D_B=\frac12\|\rho_1-\rho_0\|_1\ge\delta$.

### 3.4. Infrared admissibility

**Definition 3.1.** For a bounded operator $X$ on $\mathcal H$ with
$X\Pi\ne0$, set

$$
\eta_{\mathrm{op}}(X)=\frac{\|(I-\Pi')X\Pi\|}{\|X\Pi\|}.
$$

The encoder $U_M$ is *infrared-admissible* if $\eta_{\mathrm{op}}(U_M-I)\to0$
and

$$
\eta_{\mathrm{enc}}^M=\frac{\|\Delta_M-\Pi'\Delta_M\Pi'\|_1}{\|\Delta_M\|_1}\to0,
\qquad \Delta_M=U_M|\phi_N\rangle\langle\phi_N|U_M^*-|\phi_N\rangle\langle\phi_N|,
$$

as $N\to\infty$, where $\Delta_M\ne0$ is required for
$\eta_{\mathrm{enc}}^M$ to be defined. The effect $E$ is infrared-admissible
if $\eta_{\mathrm{op}}(E)\to0$.

For the operations of this paper all denominators are non-zero for every
$N\ge2$ (Theorem 3.3).

This is an operator-norm comparison: the norm of the leakage map is small
relative to the norm of the full map restricted to the infrared band.
It is not a uniform bound on the leakage fraction for each input separately.

**Lemma 3.2 (Single-site operations are ultraviolet).** If $X\Pi\ne0$ and
$\operatorname{ran}X\subseteq\ell^2(\{x_0\};\mathbb C^2)$ for a single site
$x_0$, then $\eta_{\mathrm{op}}(X)=\sqrt{1-\kappa'_N}\to1$, where
$\kappa'_N=(6\pi^2N^{3/2})^{-1}$.

*Proof.* For every vector $e_{x_0}\otimes\chi$,
$\|\Pi'(e_{x_0}\otimes\chi)\|^2=\mu(\{|p|\le\Lambda'_N\})=(\Lambda'_N)^3/(6\pi^2)$.
Hence every vector in $\operatorname{ran}X$ has exactly the fraction
$1-\kappa'_N$ of its squared norm outside $\Pi'$. ∎

This is the reason the encoder is spread over a region of size $O(N)$ with a
smooth profile. A pointlike phase gate, such as $I-2P_{x_0}$, is excluded by
Lemma 3.2. The regional operations pass:

**Theorem 3.3 (Admissibility).** Let $K_e=\frac\pi2(2+8\sqrt3\pi)$,
$K_d=\frac\pi2(1+16\sqrt3)$ and $m=11/(560\pi^2\,32^3)$. For all $N\ge32$,
all four $M$ and all four $M_B$,

$$
\eta_{\mathrm{op}}(U_M-I)\le\frac{K_e}{\sqrt{(2-\sqrt2)m}}\,N^{-1/2},\qquad
\eta_{\mathrm{enc}}^M\le\frac{K_e}{m\sqrt{2-\sqrt2}}\,N^{-1/2},\qquad
\eta_{\mathrm{op}}(E)\le\frac{2K_d}{\sqrt m}\,N^{-1/2}.
$$

All denominators are non-zero for every $N\ge2$.

The constants are conservative. The proof is in Section 6.

---

## 4. Results

**Theorem 4.1 (Explicit upper bound).** Let $N\ge2$ and
$T_N=\|P_{\mathcal B_N}S^NP_{\mathcal A_N}\|$. Then

$$
T_N\le9N^4e^{-JN},\qquad J=\bigl(1-\tfrac{\sqrt3}2\bigr)\log2\approx0.0929 .
$$

Consequently, for every unitary $U$ acting as the identity outside
$\mathcal A_N\otimes\mathbb C^2$, every one-particle state and every effect in
$\mathcal B_N$,

$$
\delta\le D_B\le4T_N\le36N^4e^{-JN}.
$$

**Remark 4.2 (Formal verification).** The kernel and operator-bound components
of Theorem 4.1 and the abstract signal inequality are machine-checked in
Lean 4 with Mathlib (`formal/` in [17]), for every $N\ge2$ and without
additional axioms. This covers the kernel bound, the geometry (6), the
counting of lattice points, the operator bound on $T_N$, and the step
$\delta\le4T_N$. The formal proof bounds the matrix powers through
Cayley–Hamilton and entrywise estimates instead of Lemma 5.3, and obtains the
sharper constant $T_N\le4N^4e^{-JN}$. Both constants are valid; the proof in
Section 5 keeps the constant $9$ that the elementary Lemma 5.3 gives. The
identification of Bob's amplitudes
with the restricted walk, and the second-quantized distance $D_B$, are not
formalized.

For $\xi\in\mathbb R^3$ put
$\Phi(\xi)=\operatorname{arcosh}\bigl(\prod_{j=1}^3\cosh\xi_j\bigr)$ and
define the rate function

$$
I(v)=\sup_{\xi\in\mathbb R^3}\bigl[\xi\cdot v-\Phi(\xi)\bigr].
\tag{9}
$$

Let $V_{\mathrm{reg}}=(1,1,1)+\overline B(0,\tfrac12)$. This is the set of
velocities $(y-x)/N$ for $x,y$ in the continuum balls underlying
$\mathcal A_N,\mathcal B_N$.

**Theorem 4.3 (Regional rate).**

- (a) $I$ is convex, $I=0$ on $\overline B(0,1)$, $I>0$ outside it, and
  $I=+\infty$ outside $[-1,1]^3$.
- (b) On $V_{\mathrm{reg}}$, $I$ has the unique minimiser
  $v_*=\alpha(1,1,1)$, $\alpha=1-\frac1{2\sqrt3}$. The corresponding dual tilt
  is $\xi_*=t_*(1,1,1)$, where $t_*>0$ is the unique solution of
  $\alpha=\nabla_1\Phi(t,t,t)$. Moreover

  $$
  K_*:=I(v_*)=3\alpha t_*-\operatorname{arcosh}(\cosh^3t_*),\qquad
  \cosh^2t_*=\frac{\alpha\bigl(\alpha+\sqrt{4-3\alpha^2}\bigr)}{2(1-\alpha^2)} .
  $$

- (c) $J<K_*<\log4$. Numerically $t_*=0.7357528144\ldots$ and
  $K_*=0.1905189296\ldots$.
- (d) For all $N\ge2$ and all $(x,y)\in\mathcal A_N\times\mathcal B_N$,

  $$
  \|G_N(y-x)\|\le\bigl(1+4e^{3t_*-\Phi_*}N\bigr)e^{-K_*N},\qquad \Phi_*=\Phi(\xi_*),
  $$

  and hence $\delta\le D_B\le4N^3(1+10N)e^{-K_*N}$.

The main result identifies the exact leading behaviour of every signal in the
family. Write $\theta_N=\{\sqrt3N/4\}\in[0,1)$ for the fractional part.

**Theorem 4.4 (Leading asymptotics).** For each of the sixteen pairs
$(M,M_B)$ there is a continuous, $1$-periodic, real function
$C_{M,M_B}(\theta)$ such that, as $N\to\infty$,

$$
L_{M,M_B}(N)=e^{-K_*N}N^{-13/2}\Bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\Bigr).
$$

Explicitly,

$$
C_{M,M_B}(\theta)=\mathcal K\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\tag{10}
$$

with the constants $\mathcal K$, $c_r$, the functions $\Gamma_\pm$ and the
numbers $\ell_0,\ell_\pi$ defined in Section 7. For every pair,

$$
C_{M,M_B}(\theta)=\overline{C}_{M,M_B}\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad \sup_\theta|\vartheta_{M,M_B}(\theta)|\le1.47\times10^{-3},
\qquad \overline{C}_{M,M_B}\ne0,
$$

with the values in Table 1. Consequently, for every pair,

$$
\delta_{M,M_B}(N)=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
$$

and $\delta_{M,M_B}(N)>0$ for all $N$ larger than some finite $N_*$.

Throughout, the operational claim concerns the twelve Pauli pairs,
$M\in\{\sigma_1,\sigma_2,\sigma_3\}$. The four pairs with $M=I$ are
included as reference controls. Theorem 4.4 and Table 1 cover all sixteen
pairs.

The constants implicit in the $O(N^{-1/2})$ terms are finite but not
explicit, and neither is $N_*$. Theorem 4.4 therefore does not assert
$\delta_{M,M_B}(N)>0$ at any specified $N$. It also does not say from which
$N$ on the leading term is numerically accurate (Section 8).

**Table 1.** Mean leading coefficients
$\overline{C}_{M,M_B}=\mathcal K c_r\overline\Gamma\ell_0$ and the uniform
bound on their relative oscillation in $\theta$. Values are certified by
interval arithmetic (Appendix A). Rows with $M=I$ are reference controls.

| $M$ | $M_B$ | $\overline{C}_{M,M_B}$ | $\sup_\theta \lvert C/\overline{C}-1\rvert$ |
| --- | --- | ---: | ---: |
| $I$ | $I$ | $-0.0752752093$ | $1.47\cdot10^{-3}$ |
| $I$ | $P_1$ | $+1.2072650683$ | $1.09\cdot10^{-3}$ |
| $I$ | $P_2$ | $+0.8164098576$ | $1.08\cdot10^{-3}$ |
| $I$ | $P_3$ | $-0.0752752093$ | $1.47\cdot10^{-3}$ |
| $\sigma_1$ | $I$ | $-3.7206303938$ | $1.05\cdot10^{-3}$ |
| $\sigma_1$ | $P_1$ | $-1.5567800857$ | $1.06\cdot10^{-3}$ |
| $\sigma_1$ | $P_2$ | $-2.8203960182$ | $1.02\cdot10^{-3}$ |
| $\sigma_1$ | $P_3$ | $-0.1776542932$ | $1.05\cdot10^{-3}$ |
| $\sigma_2$ | $I$ | $-2.9389199724$ | $1.05\cdot10^{-3}$ |
| $\sigma_2$ | $P_1$ | $-0.5846543741$ | $1.02\cdot10^{-3}$ |
| $\sigma_2$ | $P_2$ | $-1.7729950974$ | $1.04\cdot10^{-3}$ |
| $\sigma_2$ | $P_3$ | $-0.1776542932$ | $1.05\cdot10^{-3}$ |
| $\sigma_3$ | $I$ | $+0.0752752093$ | $1.47\cdot10^{-3}$ |
| $\sigma_3$ | $P_1$ | $-1.2072650683$ | $1.09\cdot10^{-3}$ |
| $\sigma_3$ | $P_2$ | $-0.8164098576$ | $1.08\cdot10^{-3}$ |
| $\sigma_3$ | $P_3$ | $+0.0752752093$ | $1.47\cdot10^{-3}$ |

**Corollary 4.5.** In this protocol the emergent light cone is not
operationally sharp for infrared-admissible operations. For each of the
twelve Pauli pairs the response is non-perturbatively small: $\delta_{M,M_B}(N)=o(N^{-k})$ for every
$k$. It is nevertheless non-zero for all large $N$, with the exact rate
$K_*$, the exact power $13/2$ and an explicit non-vanishing coefficient.

**Remark 4.6.** Three features of Table 1 were not assumed and come out of
the computation. First, $C(\sigma_3,\cdot)=-C(I,\cdot)$ at leading order; the
two encoders differ only at lower orders. Second, the three Pauli encoders
are not equivalent: with $M_B=I$ they give three different coefficients.
Third, for $M=\sigma_2$ the two contributing saddles enter with the same sign
for every detector: $\ell_0$ and $\ell_\pi$ of Appendix A have the same sign.
Since $\Gamma_+>0$ and $\Gamma_-\ge0$ (Lemma 7.3), non-vanishing then follows
without the margin estimate in the proof of Theorem 4.4, so for this encoder
the non-cancellation mechanism is particularly transparent. The smallest
coefficients, $|\overline C|\approx0.0753$, occur for $M\in\{I,\sigma_3\}$
with $M_B\in\{I,P_3\}$. For these two encoders with $M_B=I$, the
diagnostics of Appendix A show that the next-order term, of size
$N^{-17/2}e^{-K_*N}$, dominates numerically throughout the diagnostic range
$N\le56$.

**Remark 4.7 (Methodology).** The protocol (regions, profiles, encoders,
detectors, scalings $\Lambda_N=N^{-1}$, $\Lambda'_N=N^{-1/2}$ and the
encoding angle $\pi/2$) was fixed before the asymptotic analysis and was not tuned
afterwards. The family of encoders and detectors is not exhaustive: a general
generator $M=aI+b\cdot\sigma$ is not covered, because no symmetry of the walk
relating the directions $\hat n\cdot\sigma$ has been established.

---

## 5. Proof of the upper bounds

### 5.1. An ellipse lemma

For $a\ge1$ let
$E_a=\{z\in\mathbb C:(\operatorname{Re} z)^2/a^2+(\operatorname{Im} z)^2/(a^2-1)\le1\}$,
where $E_1=[-1,1]$. These are the confocal ellipses with foci $\pm1$. The
Joukowski map $\lambda\mapsto(\lambda+\lambda^{-1})/2$ sends the circle
$|\lambda|=r\ge1$ onto $\partial E_{(r+r^{-1})/2}$.

**Lemma 5.1.** Let $a,c\ge1$. If $z\in\partial E_a$ and $w\in E_c$, then
$zw\in E_{ac}$; consequently $E_aE_c\subseteq E_{ac}$. If moreover $a,c>1$,
then $zw\in\partial E_{ac}$ only if $z=\pm a$ and $w=\pm c$.

*Proof.* If $c=1$, then $w\in[-1,1]$ and $zw\in E_a$ by convexity and
symmetry. If $a=1$, then $z\in[-1,1]$ and the same argument applies. So let
$a,c>1$. Write $z=a\cos p+i\sqrt{a^2-1}\sin p$ and
$w=c\,x+i\sqrt{c^2-1}\,y$ with $x^2+y^2\le1$. In the coordinates adapted to
$E_{ac}$, the point $zw$ corresponds to $L(x,y)^T$ with

$$
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\ \sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
$$

With $A=a^2$, $C=c^2$ and $u=\cos^2p$, a direct computation gives

$$
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},\qquad
\det(I-L^TL)=\frac{(C-1)(1-u)\bigl[A-1+C(1-u)\bigr]}{AC(AC-1)} .
$$

Both are non-negative, so $I-L^TL\ge0$ by Sylvester's criterion and
$\|L\|\le1$. If $u<1$, both are positive, so $\|L\|<1$ and $zw$ is interior.
If $u=1$, then $z=\pm a$ and

$$
L=\pm\operatorname{diag}\Bigl(1,\ \frac{a\sqrt{c^2-1}}{\sqrt{a^2c^2-1}}\Bigr),
$$

whose second entry is $<1$. Hence $|L(x,y)^T|=1$ forces $y=0$ and $|x|=1$,
that is, $w=\pm c$. ∎

**Lemma 5.2.** For $\eta\in\mathbb R^3$ and $\xi\in\mathbb R^3$,
$\rho\bigl(S(\eta-i\xi)\bigr)\le e^{\Phi(\xi)}$. If all $\xi_j\ne0$, equality
holds if and only if $\eta\in\Sigma:=\{0,\pi\}^3$ modulo $2\pi$.

*Proof.*
$\cos(\eta_j-i\xi_j)=\cos\eta_j\cosh\xi_j+i\sin\eta_j\sinh\xi_j\in\partial E_{\cosh\xi_j}$.
By Lemma 5.1 applied twice,
$f(\eta-i\xi)=\prod_j\cos(\eta_j-i\xi_j)\in E_{\prod\cosh\xi_j}$. When all
$\xi_j\ne0$, it lies on the boundary only if every factor is a real vertex,
that is, only if every $\sin\eta_j=0$. The eigenvalues $\lambda^{\pm1}$ of
the unimodular matrix $S(\eta-i\xi)$ satisfy $(\lambda+\lambda^{-1})/2=f$. If
$|\lambda|=r\ge1$, then $f\in\partial E_{(r+r^{-1})/2}$. Since the ellipses
are nested, $(r+r^{-1})/2\le\prod\cosh\xi_j$, which is $r\le e^{\Phi(\xi)}$,
with strict inequality when $f$ is interior. On $\Sigma$,
$f=\pm\prod\cosh\xi_j$ is real and equality holds. ∎

**Lemma 5.3 (Powers without a gap).** Let $T$ be a $2\times2$ matrix with
$\rho(T)\le e^{\varkappa}$ and $\|T\|\le\beta$. Then
$\|T^N\|\le e^{N\varkappa}+\beta Ne^{(N-1)\varkappa}$.

*Proof.* Take a unitary Schur form
$T=V\begin{pmatrix}\lambda_1&b\\0&\lambda_2\end{pmatrix}V^*$, so
$|b|\le\|T\|$. The upper-right entry of the $N$-th power is
$b\sum_{j=0}^{N-1}\lambda_1^j\lambda_2^{N-1-j}$, also when
$\lambda_1=\lambda_2$. The diagonal part has norm $\max_j|\lambda_j|^N$. ∎

### 5.2. Proof of Theorem 4.1

Since the integrand in (3) is entire and $2\pi$-periodic in each variable,
the contour can be shifted to $p=\eta-i\xi$ for any $\xi\in\mathbb R^3$
without boundary terms:

$$
G_N(d)=e^{-\xi\cdot d}\int_{\mathbb T^3}e^{-i\eta\cdot d}\,S(\eta-i\xi)^N\,d\mu(\eta).
\tag{11}
$$

Take $\xi=tu$ with $t=\log2$, so $\cosh^3t=125/64$. Lemma 5.2 gives

$$
\rho\bigl(S(\eta-itu)\bigr)\le\exp\operatorname{arcosh}(125/64)<4,
$$

because $125/64<17/8=\cosh\log4$. By Lemma 2.1,

$$
\|S(\eta-itu)\|\le\sum_d\|S_d\|e^{t|u\cdot d|}\le4e^{3t}=32 .
$$

Lemma 5.3, with the cruder bound $|\lambda_j|\le4$, gives
$\|S(\eta-itu)^N\|\le4^N+32N4^{N-1}\le9N4^N$. With (6),

$$
\|G_N(y-x)\|\le9N\exp\bigl[-t\,u\cdot(y-x)+N\log4\bigr]\le9Ne^{-JN}
$$

for all $(x,y)\in\mathcal A_N\times\mathcal B_N$. The Schur test with
$|\mathcal A_N|,|\mathcal B_N|\le N^3$ gives $T_N\le9N^4e^{-JN}$.

Let $v_b=P_BS^NU^{(b)}\psi$ for a one-particle state $\psi$. Then
$v_1-v_0=P_BS^NP_A(U-I)\psi$, so $\|v_1-v_0\|\le2T_N$. The difference of
Bob's reduced states is $X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|$
on the one-particle block, together with $-\operatorname{tr} X$ on the vacuum
block. Hence
$D_B=\frac12(|\operatorname{tr} X|+\|X\|_1)\le\|X\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le4T_N$.
Mixed states follow by convexity, and $\delta\le D_B$ holds for every effect.
∎

### 5.3. Proof of Theorem 4.3

(a) $I$ is a supremum of affine functions, so it is convex, and $I\ge0$
(take $\xi=0$). The inequality $\cosh\sqrt{a^2+b^2}\le\cosh a\cosh b$,
applied twice, gives $\Phi(\xi)\ge|\xi|$, so $I=0$ on $\overline B(0,1)$.
Since $\Phi(\xi)=|\xi|+O(|\xi|^3)$, $I(v)>0$ for $|v|>1$. Finally
$I=+\infty$ outside $\operatorname{conv}F$ by [9, Lemma 4.1]. Directly, if
$v_j>1$, take $\xi=se_j$ and let $s\to\infty$, using $\Phi(se_j)=s$.

(b) $\Phi$ is smooth where $\Pi(\xi)=\prod_j\cosh\xi_j>1$, with

$$
\nabla\Phi(\xi)=\frac{\Pi(\xi)}{\sqrt{\Pi(\xi)^2-1}}\,(\tanh\xi_1,\tanh\xi_2,\tanh\xi_3).
$$

On the diagonal, $h(t)=\nabla_1\Phi(t,t,t)$ tends to $1/\sqrt3$ as
$t\to0^+$ and to $1$ as $t\to\infty$. It is strictly increasing, since
$3h'(t)=u^T\operatorname{Hess}\Phi(t,t,t)\,u=3q_n(t)>0$, where $q_n(t)$ is
given by the formula of Lemma 7.1(d) with $c_*$ replaced by $\cosh t>1$.
Since $\alpha\in(1/\sqrt3,1)$, there is a unique $t_*>0$ with
$h(t_*)=\alpha$, and then $\nabla\Phi(\xi_*)=v_*$. Solving $h(t)=\alpha$ for
$\cosh^2t$ gives the stated closed form. To justify attainment of the Legendre supremum, note
that $\Phi$ is convex. Away from zero its Hessian has the form given in
Lemma 7.1. Cauchy--Schwarz gives
$(\sum_j\tanh\xi_j x_j)^2\le
(\sum_j\operatorname{sech}^2\xi_j x_j^2)\sum_j\sinh^2\xi_j$,
and $\sum_j\sinh^2\xi_j\le\prod_j(1+\sinh^2\xi_j)-1=D^2$.
Thus the Hessian is positive semidefinite. At zero, continuity and
$\Phi(\xi)=|\xi|+O(|\xi|^3)$ extend convexity across the origin
(the one-sided directional derivatives are $-|x|$ and $|x|$).
Consequently $\nabla\Phi(\xi_*)=v_*$ gives a supporting hyperplane and
$I(v_*)=\xi_*\cdot v_*-\Phi_*$. By the definition of $I$, for every
$v$,

$$
I(v)\ge\xi_*\cdot v-\Phi(\xi_*)=I(v_*)+\xi_*\cdot(v-v_*)
=I(v_*)+\sqrt3\,t_*\bigl(\hat u\cdot v-|v_*|\bigr),
\qquad \hat u=u/\sqrt3 .
$$

On $V_{\mathrm{reg}}$ we have $\hat u\cdot v\ge\sqrt3-\frac12=|v_*|$, with
equality only at $v=v_*$. Hence $v_*$ is the unique minimiser.

(c) The tilt $\xi=(\log2)u$ gives
$I(v_*)\ge3\alpha\log2-\operatorname{arcosh}(125/64)>(3-\tfrac{\sqrt3}2)\log2-\log4=J$.
Also $\xi_*\cdot v_*<\xi_*\cdot u$ because $\alpha<1$ and $t_*>0$, so
$I(v_*)<\xi_*\cdot u-\Phi(\xi_*)\le I(u)$. Along the diagonal,
$3t-\operatorname{arcosh}(\cosh^3t)\uparrow\log4$, and $I(u)=\log4$ is also
the exact vertex rate of Proposition 2.2(c). The numerical values are
enclosed by interval arithmetic.

(d) Apply (11) with $\xi=\xi_*$. By Lemma 5.2,
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*}$ for all $\eta$. By Lemma 2.1,
$\|S(\eta-i\xi_*)\|\le4e^{3t_*}$. Lemma 5.3 gives
$\sup_\eta\|S(\eta-i\xi_*)^N\|\le e^{N\Phi_*}(1+4e^{3t_*-\Phi_*}N)$. For
$(x,y)\in\mathcal A_N\times\mathcal B_N$, (6) and $\xi_*\parallel\hat u$ give
$\xi_*\cdot(y-x)\ge N\,\xi_*\cdot v_*$, and $N\xi_*\cdot v_*-N\Phi_*=NK_*$.
Numerically $4e^{3t_*-\Phi_*}<9.2$, so $1+4e^{3t_*-\Phi_*}N\le1+10N$, and the
Schur test concludes as before. ∎

---

## 6. Proof of admissibility

**Lemma 6.1.** Let $a:\mathbb Z^3\to M_2(\mathbb C)$ satisfy
$\sup\|a\|\le A$ and $\|a(x+e_j)-a(x)\|\le L/N$ for all $x,j$. Then

$$
\|(I-\Pi')\,a\,\Pi\|\le\tfrac\pi2(A+\sqrt3L)\,N^{-1/2}.
$$

*Proof.* Let $D_j\xi(x)=\xi(x+e_j)-\xi(x)$. On the complement of $\Pi'$,

$$
\sum_j|e^{ip_j}-1|^2=\sum_j4\sin^2(p_j/2)\ge(2/\pi)^2|p|^2\ge(2/\pi)^2N^{-1},
$$

using $\sin s\ge2s/\pi$ on $[0,\pi/2]$. By Plancherel,
$\|(I-\Pi')\xi\|\le\frac\pi2N^{1/2}(\sum_j\|D_j\xi\|^2)^{1/2}$. For
$\psi=\Pi\psi$, $(\sum_j\|D_j\psi\|^2)^{1/2}\le N^{-1}\|\psi\|$. The discrete
product rule $D_j(a\psi)=a(\cdot+e_j)D_j\psi+(D_ja)\psi$ and Minkowski's
inequality give $(\sum_j\|D_j(a\psi)\|^2)^{1/2}\le(A+\sqrt3L)N^{-1}\|\psi\|$.
∎

*Proof of Theorem 3.3.* **Numerators.**
$|\nabla F_N|=64|x|(1-16|x|^2/N^2)/N^2\le16/N$ inside $\mathcal A_N$, and the
gradient vanishes on the sphere, so $F_N$ is $16/N$-Lipschitz on
$\mathbb Z^3$. For $a_M=U_M-I$ we get $A=2$ and $L=8\pi$, because
$\|\frac{d}{dF}e^{i\pi FM/2}\|=\pi/2$. For $E=h_N\otimes M_B$ we get $A=1$
and $L=16$. Lemma 6.1 bounds the numerators by $K_eN^{-1/2}$ and
$K_dN^{-1/2}$. For $\eta_{\mathrm{enc}}$, write $v=U_M\phi_N$, $w=\Pi'v$ and
$r=v-w=(I-\Pi')a_M\phi_N$. Since $\Pi'\phi_N=\phi_N$,
$\Delta_M-\Pi'\Delta_M\Pi'=|r\rangle\langle v|+|w\rangle\langle r|$, whose
trace norm is at most $2\|r\|\le2K_eN^{-1/2}$.

**Denominators.** For $|x|\le N$ and $|p|\le N^{-1}$,
$\cos(p\cdot x)\ge\frac12$. Hence
$\varphi_N(x)\ge\frac12\sqrt{11/(140\pi^2)}\,N^{-3/2}$ for $|x|\le N$. Let
$N\ge32$, and consider two auxiliary sets. The first is
$Q_{\mathrm{in}}=\{|x_j|\le N/32\}$, with at least $(N/32)^3$ sites, on which
$F_N\ge(61/64)^2>\frac12$. The second is
$Q_{\mathrm{out}}=\{N/2\le x_1\le5N/8,\ 0\le x_2,x_3\le N/8\}$, with at least
$(N/16)^3$ sites, on which $F_N=0$ and $|x|<N$. Each carries resource weight
at least $m$.

On $Q_{\mathrm{in}}$, $\frac\pi2F_N\in[\frac\pi4,\frac\pi2]$, so
$a_M^*a_M=2(1-\cos\frac\pi2F_N)I\ge(2-\sqrt2)I$. Thus
$\|a_M\Pi\|\ge\|a_M\phi_N\|\ge\sqrt{(2-\sqrt2)m}$. For the detector, test on
the resource translated to $N(1,1,1)$, with internal state a $+1$
eigenvector of $M_B$. This test vector lies in $\operatorname{ran}\Pi$, and it
gives $\|E\Pi\|\ge\frac12\sqrt m$.

For $\eta_{\mathrm{enc}}$, $\|\Delta_M\|_1=2\sqrt{1-|z|^2}$ with
$z=\sum_xw_xt_x$, $w_x=|\varphi_N(x)|^2$ and
$t_x=\langle{\downarrow}|e^{i\pi F_N(x)M/2}|{\downarrow}\rangle$. This gives
$t_x=e^{i\pi F_N/2}$ for $M=I$, $\cos(\pi F_N/2)$ for $M=\sigma_{1,2}$, and
$e^{-i\pi F_N/2}$ for $M=\sigma_3$. Then
$1-|z|^2=\sum_{x,y}w_xw_y(1-\operatorname{Re} t_x\bar t_y)$. All terms are
non-negative, and for $x\in Q_{\mathrm{in}}$, $y\in Q_{\mathrm{out}}$ one has
$\operatorname{Re} t_x\bar t_y=\cos(\frac\pi2F_N(x))\le1/\sqrt2$. Counting
both orders gives $1-|z|^2\ge(2-\sqrt2)m^2$. For $2\le N<32$ the same
argument, with the origin and the site $(\lfloor N/4\rfloor+1,0,0)$, shows
that the denominators are non-zero. ∎

---

## 7. Proof of the leading asymptotics

Throughout, $C$ denotes a finite constant independent of $N$ whose value may
change from line to line. The constants $r_0,c,c_3,c_P$ below are finite but
not made explicit.

### 7.1. Reduction to one interference functional

Let $P_B$ be the restriction to $\mathcal B_N$ (not a spectral projection).
Write $\widetilde r=S^N\phi_N$ for the free evolution of the resource on all
of $\mathbb Z^3$, and put

$$
r=P_B\widetilde r,\qquad a_c=P_BS^N(c_N\varphi_N{\downarrow}),\qquad
a_{\uparrow}=P_BS^N(s_N\varphi_N{\uparrow}),\qquad a_{\downarrow}=P_BS^N(s_N\varphi_N{\downarrow}).
$$

Since $\sigma_1{\downarrow}={\uparrow}$, $\sigma_2{\downarrow}=-i{\uparrow}$
and $\sigma_3{\downarrow}=-{\downarrow}$, Bob's encoded amplitude $P_B\psi_1$
is $v+ia_{\downarrow}$, $v+ia_{\uparrow}$, $v+a_{\uparrow}$ or
$v-ia_{\downarrow}$ for $M=I,\sigma_1,\sigma_2,\sigma_3$, where $v=r+a_c$.
Expanding (8) with $E$ supported in $\mathcal B_N$,

$$
\begin{aligned}
L_{I}&=2\operatorname{Re}\langle r,Ea_c\rangle-2\operatorname{Im}\langle r,Ea_{\downarrow}\rangle+Q_I, &
L_{\sigma_3}&=2\operatorname{Re}\langle r,Ea_c\rangle+2\operatorname{Im}\langle r,Ea_{\downarrow}\rangle+Q_{\sigma_3},\\
L_{\sigma_1}&=2\operatorname{Re}\langle r,Ea_c\rangle-2\operatorname{Im}\langle r,Ea_{\uparrow}\rangle+Q_{\sigma_1}, &
L_{\sigma_2}&=2\operatorname{Re}\langle r,Ea_c\rangle+2\operatorname{Re}\langle r,Ea_{\uparrow}\rangle+Q_{\sigma_2}.
\end{aligned}
\tag{12}
$$

Each $Q_M$ is a sum of terms quadratic in $(a_c,a_{\uparrow},a_{\downarrow})$.
For example,
$Q_I=\langle a_c,Ea_c\rangle+\langle a_{\downarrow},Ea_{\downarrow}\rangle-2\operatorname{Im}\langle a_c,Ea_{\downarrow}\rangle$.
Positivity of $E$ does not fix the sign of $L$, because the interference
terms can have either sign.

By Theorem 4.3(d), $a_c,a_{\uparrow},a_{\downarrow}$ have $\ell^2$-norm at
most $T_N=O(N^4e^{-K_*N})$, so $Q_M=O(N^{8}e^{-2K_*N})$. The free tail is only
polynomially small (Lemma 7.2). The $e^{-K_*N}$ sector therefore consists of
the linear interference terms. Define, for $\chi\in\{{\uparrow},{\downarrow}\}$,

$$
\mathcal T_\chi(N)=e^{K_*N}\,\bigl\langle r,\,E\,S^N(s_N\varphi_N\chi)\bigr\rangle .
$$

Theorem 4.4 follows from Theorem 7.5 below. The piece
$\langle r,Ea_c\rangle$ is $O(N^{-17/2}e^{-K_*N})$ by the same argument,
For completeness, in a boundary layer of depth $\delta$ put
$d=(\delta-|u_\perp|^2/(2R))_+$. The exact spherical profile gives
$F_N=O(N^{-2}d^2)$ with polynomial depth bounds, and
$|c_N|\le C F_N^2\le C N^{-4}d^4$.
Thus the tilted Alice layer is $O(N^{-9/2})$: resource, profile and
disc area contribute $N^{-3/2}$, $N^{-4}$ and $N$, respectively.
The fourth-order profile's third-derivative variation is
$O(\delta^{7/2}R^{-1/2})$, giving $O(N^{-6})$ after prefactors and
the exponentially weighted depth sum. Hence its nonzero Poisson modes
are smaller than its layer bound, uniformly in $\theta_N$.
The Bob layer is $O(N^{-5/2})$ and the three-dimensional local Gaussian
integral is $O(N^{-3/2})$, yielding $N^{-17/2}$.
The complementary spectral region is exponentially suppressed as in
the assembly proof. Only this bound, not a fourth-order leading
coefficient, is needed here.

### 7.2. Exact tilted representation

Let $R=N/4$, $x_*=R\hat u$ and $y_*=Nu-R\hat u$, so that $y_*-x_*=Nv_*$. For
$f$ supported in $\mathcal A_N$ and $w$ supported in $\mathcal B_N$, put

$$
\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x),\qquad
\mathfrak B_w(\eta)=\sum_ye^{-i\eta\cdot(y-y_*)}e^{-\xi_*\cdot(y-y_*)}w(y)^\dagger .
$$

Let $\widetilde S_N(\eta)=e^{-N\Phi_*}S(\eta-i\xi_*)^N$. By (11) with
$\xi=\xi_*$, and using $\xi_*\cdot v_*-\Phi_*=K_*$,

$$
e^{K_*N}\sum_yw(y)^\dagger(S^Nf)(y)=\int_{\mathbb T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,\mathfrak A_f(\eta)\,e^{-iN\eta\cdot v_*}\,d\mu(\eta).
\tag{13}
$$

This identity is exact: the sums are finite and no poles are crossed.

### 7.3. The tilted symbol

**Lemma 7.1.**

- (a) $S(-i\xi)$ is Hermitian for every real $\xi$, with $\det=1$. At
  $\xi_*$, with $c_*=\cosh t_*$ and $s_*=\sinh t_*$,

  $$
  S(-i\xi_*)=\begin{pmatrix}c_*^2e^{-t_*}&-(1+ic_*)s_*\\-(1-ic_*)s_*&c_*^2e^{t_*}\end{pmatrix},
  $$

  with eigenvalues $e^{\pm\Phi_*}$, $e^{\Phi_*}=c_*^3+\sqrt{c_*^6-1}=3.97314\ldots$.
  The orthogonal projector onto the $e^{\Phi_*}$-eigenspace is

  $$
  P=\frac12\begin{pmatrix}1-\alpha&-(1+ic_*)\alpha/c_*^2\\-(1-ic_*)\alpha/c_*^2&1+\alpha\end{pmatrix}.
  $$

- (b) For all $p\in\mathbb C^3$: $S(p+\pi e_1)=-S(p)$,
  $S(p+\pi e_3)=-\sigma_3S(p)\sigma_3$,
  $S(p+\pi e_2)=-\sigma_3S(p)^T\sigma_3$ and $S(p+\pi(1,1,1))=-S(p)^T$.
- (c) The character $x\mapsto e^{i\eta_0\cdot x}$, $\eta_0\in\Sigma$,
  restricted to $\Lambda_0=\{u\in\mathbb Z^3:u_1+u_2+u_3=0\}$ is trivial if
  and only if $\eta_0\in\{0,\pi u\}$.
- (d) There is $r_0>0$ such that, for $|\eta|\le r_0$,
  $S(\eta-i\xi_*)=\lambda(\eta)P(\eta)+\lambda(\eta)^{-1}(I-P(\eta))$ with
  $\lambda,P$ analytic, $P(0)=P$, $\|P(\eta)-P\|\le c_P|\eta|$ and

  $$
  \lambda(\eta)=\exp\Bigl(\Phi_*+iv_*\cdot\eta-\tfrac12\eta^TQ\eta+\rho_3(\eta)\Bigr),\qquad
  |\rho_3(\eta)|\le c_3|\eta|^3\le\tfrac14\eta^TQ\eta .
  $$

  Here $Q=\operatorname{Hess}\Phi(\xi_*)=q_t(I-\hat u\hat u^T)+q_n\hat u\hat u^T$ with

  $$
  q_t=\frac{c_*}{D_*}=0.68956\ldots,\qquad
  q_n=\frac{c_*}{D_*}\frac{(c_*^2-1)(c_*^2+2)}{c_*^4+c_*^2+1}=0.30338\ldots,\qquad D_*=\sqrt{c_*^6-1}.
  $$

- (e) Outside $\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$,
  $\|\widetilde S_N(\eta)\|\le CNe^{-cN}$ for some $c>0$.

*Proof.* (a) and (b) are identities between trigonometric polynomials and
are checked by expansion. (c): $\Lambda_0$ is generated by $e_1-e_2$ and
$e_2-e_3$, so the character is trivial on it if and only if
$\eta_{0,1}\equiv\eta_{0,2}\equiv\eta_{0,3}\pmod{2\pi}$. (d): the eigenvalues
of $S(\eta-i\xi_*)$ are $\exp(\pm\operatorname{arcosh} f(\eta-i\xi_*))$ and
$f(\eta-i\xi)=\prod_j\cosh(\xi_j+i\eta_j)$. Hence
$\log\lambda(\eta)=\Phi(\xi_*+i\eta)$, which is holomorphic near $\eta=0$
because $\Pi(\xi_*)>1$. Taylor expansion gives $\nabla\Phi(\xi_*)=v_*$ and
$\operatorname{Hess}\Phi(\xi_*)=Q$. The explicit Hessian is
$\operatorname{Hess}\Phi=\frac{\Pi}{D}\operatorname{diag}(\operatorname{sech}^2\xi_j)-\frac{\Pi}{D^3}(\tanh\xi_i\tanh\xi_j)$
with $D=\sqrt{\Pi^2-1}$. The eigenvalues $\lambda^{\pm1}$ are separated by the
gap $e^{2\Phi_*}\approx15.8$, so the spectral projector is analytic. (e): by
Lemma 5.2 and compactness, $\rho(S(\eta-i\xi_*))\le e^{\Phi_*-c'}$ away from
$\Sigma$. Conclude with Lemma 5.3. ∎

By (b), near $\pi u$ we have
$S(\pi u+\eta-i\xi_*)^N=(-1)^N(S(\eta-i\xi_*)^N)^T$, whose Perron projector
is $P^T=\overline P$. The other six points of $\Sigma$ have the same spectral
radius, but by (c) their characters are non-trivial on the lattice planes
$u\cdot x=k$. This is why only $0$ and $\pi u$ contribute at leading order
(Lemma 7.4(d)).

### 7.4. Lattice-plane coordinates and profiles

The planes $\{u\cdot x=k\}$ are orthogonal to $\xi_*$, and each is a
translate of the two-dimensional lattice $\Lambda_0$, of covolume $\sqrt3$.
Write Alice's sites as $x=x_*-\delta\hat u+u_\perp$ with
$u_\perp\perp\hat u$ and depth $\delta=(\sqrt3R-u\cdot x)/\sqrt3$. Since
$u\cdot x\in\mathbb Z$,

$$
\sqrt3\,\delta=\theta_N+j,\qquad j\in\mathbb Z_{\ge0},\qquad \theta_N=\{\sqrt3R\}=\{\sqrt3N/4\}.
$$

Similarly $y=y_*+\delta'\hat u+u'_\perp$ with $\sqrt3\delta'=\theta_N+j'$,
with the *same* $\theta_N$. Then $\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)$ and
$\xi_*\cdot(y-y_*)=t_*(\theta_N+j')$. Moreover
$u\cdot(y-x)=3N-2\lfloor\sqrt3R\rfloor+j+j'$, so
$(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$.

On the plane at depth $\delta$, exactly,

$$
F_N=\frac{64}{N^2}\varepsilon_\perp^2,\qquad
\varepsilon_\perp=\delta-\frac{\delta^2}{2R}-\frac{|u_\perp|^2}{2R}\ \ (\ge0),
$$

and therefore $s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6})$ and
$c_N=-\frac{512\pi^2}{N^4}\varepsilon_\perp^4+O(N^{-8})$ for $\delta=O(1)$.
The same holds for $h_N$ with $\delta'$ and $u'_\perp$. Replacing
$\varepsilon_\perp$ by $\delta-|u_\perp|^2/2R$ costs a relative $O(N^{-1})$.

### 7.5. The free tail

**Lemma 7.2.** Uniformly in $y\in\mathbb Z^3$,
$\widetilde r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$, where

$$
R_0(w)=c_r\bigl[\mathcal I_0(|w|)\,I-\mathcal I_1(|w|)\,H_W(\hat w)\bigr]{\downarrow},
$$

$$
\mathcal I_0(\rho)=4\pi\int_0^1k^2(1-k^2)^2\cos k\;j_0(k\rho)\,dk,\qquad
\mathcal I_1(\rho)=4\pi\int_0^1k^2(1-k^2)^2\sin k\;j_1(k\rho)\,dk .
$$

At the facing point $w_*=u-\hat u/4$, with $\rho_*=|w_*|=\sqrt3-\frac14$ and
$\hat w_*=\hat u$, one has
$R_0(w_*)=c_r\bigl(-\tfrac{\mathcal I_1}{\sqrt3}(1+i),\ \mathcal I_0+\tfrac{\mathcal I_1}{\sqrt3}\bigr)^T$,
with $\mathcal I_0=0.716577\ldots>0$ and $\mathcal I_1=0.132252\ldots>0$.
In particular $r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$ uniformly in
$y\in\mathcal B_N$, and $r=0$ outside $\mathcal B_N$.

*Proof.* For $|p|\le N^{-1}$, $S(p)=e^{-iH(p)}$ with $H$ Hermitian, analytic,
and $H-H_W=O(|p|^2)$. Duhamel's formula gives
$\|S(p)^N-e^{-iNH_W(p)}\|\le CN|p|^2\le C/N$. With $q=Np$,
$e^{-iH_W(q)}=\cos|q|-i\sin|q|\,H_W(\hat q)$, and the angular integrals of
$e^{-iq\cdot w}$ and $e^{-iq\cdot w}\hat q$ are $4\pi j_0$ and
$-4\pi ij_1\hat w$. The resource enters through $g(Np)$ and is not
truncated. The integrands defining $\mathcal I_0,\mathcal I_1$ are positive
because $k\rho_*<\pi$. The value of $H_W(\hat u){\downarrow}=(1+i,-1)^T/\sqrt3$
follows by direct computation. ∎

The resource on Alice's sphere has the exact value
$N^{3/2}\varphi_N=\Phi_0(\frac14)=c_rI_b$ with
$I_b=16\pi\int_0^1k(1-k^2)^2\sin(k/4)\,dk$. We write
$\varphi_\partial=c_rI_b$.

### 7.6. Layer sums

Let
$\Psi_\delta(\tau)=\int_{\mathbb R^2}(\delta-|\sigma|^2)_+^2e^{i\tau\cdot\sigma}\,d^2\sigma$,
which is real and radial in $\tau$. Define

$$
\mathcal S_\pm(\tau;\theta)=\sum_{j\ge0}(\pm1)^je^{-t_*(\theta+j)}\,\Psi_{(\theta+j)/\sqrt3}(\tau),
\qquad
\Gamma_\pm(\theta)=\int_{\mathbb R^2}e^{-q_t|\tau|^2}\,\mathcal S_\pm(\tau;\theta)^2\,d^2\tau .
$$

**Lemma 7.3 (Depth sums).** Let $c_g=2\pi/(3\sqrt3)$ and
$s_\omega=t_*+i\omega$. Then

$$
\mathcal S_+=\sum_{n\in\mathbb Z}\hat g_\tau(2\pi n)e^{2\pi in\theta},\qquad
\mathcal S_-=\sum_{n\in\mathbb Z}\hat g_\tau\bigl(\pi(2n+1)\bigr)e^{i\pi(2n+1)\theta},\qquad
\hat g_\tau(\omega)=c_g\,\frac{e^{-|\tau|^2/(4\sqrt3\,s_\omega)}}{s_\omega^4}.
$$

Consequently $|\mathcal S_+-\hat g_\tau(0)|\le c_g/720$ and
$|\mathcal S_-|\le c_g/48$. Moreover

$$
\overline\Gamma:=\int e^{-q_t|\tau|^2}\hat g_\tau(0)^2d^2\tau=\frac{c_g^2}{t_*^8}\frac{\pi}{q_t+\frac1{2\sqrt3t_*}}=49.44186\ldots,
\qquad |\Gamma_+-\overline\Gamma|\le\varepsilon_+,\qquad 0\le\Gamma_-\le\varepsilon_-,
$$

with
$\varepsilon_+=2\frac{c_g}{720}\frac{c_g}{t_*^4}\frac{\pi}{q_t+1/(4\sqrt3t_*)}+\bigl(\frac{c_g}{720}\bigr)^2\frac\pi{q_t}=0.04917\ldots$
and $\varepsilon_-=\bigl(\frac{c_g}{48}\bigr)^2\frac\pi{q_t}=0.00289\ldots$.

*Proof.* Radially, $\Psi_\delta(\tau)=\pi H(\delta)$ with
$H(\delta)=\int_0^\delta(\delta-s)^2J_0(|\tau|\sqrt s)\,ds$. So
$H'''=2J_0(|\tau|\sqrt\delta)$ and $H(0)=H'(0)=H''(0)=0$. Since
$\int_0^\infty e^{-ps}J_0(|\tau|\sqrt s)\,ds=e^{-|\tau|^2/4p}/p$, the function
$g_\tau(x)=e^{-t_*x}\Psi_{x/\sqrt3}(\tau)\mathbf 1_{x\ge0}$ has Fourier
transform $\hat g_\tau$ as stated. It is continuous, vanishing to third
order at $x=0$, and $\hat g_\tau\in\ell^1(2\pi\mathbb Z)$. Poisson summation
is therefore exact. The bounds use $|e^{-|\tau|^2/(4\sqrt3s)}|\le1$,
$|s_{2\pi n}|\ge2\pi|n|$, $\sum_{n\ne0}(2\pi n)^{-4}=1/720$ and
$\sum_n|\pi(2n+1)|^{-4}=1/48$. The Gaussian integrals are elementary. ∎

**Lemma 7.4 (Layers).** Let $\chi\in\{{\uparrow},{\downarrow}\}$,
$f=s_N\varphi_N\chi$, $w=h_N\,M_B\,r$ and $\tau=\sqrt{N/2}\,\eta_t$, where
$\eta=\eta_n\hat u+\eta_t$ with $\eta_t\perp\hat u$.

- (a) $|\mathfrak A_f(\eta)|,\ \|\mathfrak B_w(\eta)\|\le CN^{-5/2}$ for all $\eta$.
- (b) For $|\eta|\le r_0$,

  $$
  \mathfrak A_f(\eta)=N^{-5/2}\tfrac{16\pi}{\sqrt3}\varphi_\partial\bigl[\mathcal S_+(\tau;\theta_N)+\mathcal E_A\bigr]\chi,\qquad
  \mathfrak B_w(\eta)=N^{-5/2}\tfrac{32}{\sqrt3}\,R_0(w_*)^\dagger M_B\bigl[\mathcal S_+(\tau;\theta_N)+\mathcal E_B\bigr],
  $$

  with $|\mathcal E_{A,B}|\le C(N^{-1/2}+|\eta_n|)$.
- (c) Near $\pi u$ the same holds with $\mathcal S_-$ in place of
  $\mathcal S_+$. The alternating sign comes from the parity
  $(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$, combined with
  $S^N\mapsto(-1)^N(S^N)^T$.
- (d) For $\eta_0\in\Sigma\setminus\{0,\pi u\}$ and $|\eta|\le r_0$,
  $|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}$.

*Proof.* Decompose the sums into lattice planes.  On the plane at depth
$\delta=(\theta_N+j)/\sqrt3$ the tilt weight is $e^{-t_*(\theta_N+j)}$.  The
profile $s_N\varphi_N$ is supported in a disc of radius
$\varrho=\sqrt{2R\delta-\delta^2}=O(\sqrt N)$ and has size $O(N^{-7/2}\delta^2)$.
Planes with $\delta>R/2$ contribute $O(e^{-cN})$.  This gives (a).

For (b), apply Poisson summation on each plane.  The $m=0$ term is
$\frac1{\sqrt3}\int e^{i\eta_t\cdot u_\perp}G_0(u_\perp)\,d^2u_\perp$.  The
terms $m\ne0$ are bounded by $\|\partial^3G_0\|_{\mathcal M}|2\pi m-\eta_t|^{-3}$,
since the profile vanishes quadratically on the rim and its third
derivative is a finite measure. Before the resource prefactor, its total
variation is $O(\delta^{3/2}R^{-1/2})$: the interior derivative is
$O(|u|/R^2)$ and the boundary measure has density $O(\delta/R)$ on
a rim of length $O(\sqrt{R\delta})$. Including the prefactors gives
$\|\partial^3G_0\|_{\mathcal M}=O(N^{-4}\delta^{3/2})$, with additional
polynomial depth factors when derivatives hit the resource. These are
absolute bounds uniform at $\delta=0$. Choose $r_0$ below half the
shortest nonzero reciprocal-lattice length in the $2\pi$ normalization.
The inverse-cube sum converges on this two-dimensional lattice;
translations of the planes add only unit-modulus phases. All polynomial
depth moments are uniformly summable against $e^{-t_*(\theta_N+j)}$.
After the weighted depth sum, they give a
relative error $O(N^{-3/2})$.  In the $m=0$ term, use the profile
expansions, $\varphi_N=N^{-3/2}\varphi_\partial(1+O(|u_\perp|/N+\delta/N))$ and
$|e^{-i\eta_n\delta}-1|\le|\eta_n|\delta$.  With the substitution
$u_\perp=\sqrt{2R}\,\sigma$,
$$
\int e^{i\eta_t\cdot u_\perp}\Bigl(\delta-\frac{|u_\perp|^2}{2R}\Bigr)_+^2d^2u_\perp=2R\,\Psi_\delta(\tau).
$$
Collecting the factors
$\frac1{\sqrt3}\cdot\frac{32\pi}{N^2}\cdot N^{-3/2}\varphi_\partial\cdot2R$ gives
the prefactor of $\mathfrak A_f$.  For $\mathfrak B_w$ the factors are
$\frac1{\sqrt3}\cdot\frac{64}{N^2}\cdot N^{-3/2}R_0(w_*)^\dagger\cdot2R$, using
Lemma 7.2, the smoothness of $R_0$ and $M_B^\dagger=M_B$.
For Bob's Poisson remainder one uses the exact unrestricted free tail:
its smooth Fourier interpolation has support in $|p|\le N^{-1}$, hence
$\|\partial^\beta\widetilde r\|_\infty\le C_\beta N^{-3/2-|\beta|}$
by the Fourier $L^1$ bound. Leibniz's rule through order three for
$h_N\widetilde r$ therefore gives the same variation estimates.
The cutoff causes no extra boundary term beyond the profile's
third-derivative measure, since $h_N$ vanishes quadratically. (c)
follows from Lemma 7.1(b) and the parity identity.  (d): by
Lemma 7.1(c), the character is non-trivial on each plane.  The
Poisson sum therefore has no $m=0$ term, and the remaining terms are
$O(N^{-4})$.
 ∎

### 7.7. Assembly

**Theorem 7.5.** For $\chi\in\{{\uparrow},{\downarrow}\}$ and each $M_B$,

$$
\mathcal T_\chi(N)=N^{-13/2}\,\mathcal K\,c_r\bigl[\Gamma_+(\theta_N)\,x_0+\Gamma_-(\theta_N)\,x_\pi\bigr]+O(N^{-7}),
$$

where $x_0=\tilde R^\dagger M_BP\chi$, $x_\pi=\tilde R^\dagger M_B\overline P\chi$,
$\tilde R=R_0(w_*)/c_r$ and

$$
\mathcal K=\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}\;\varphi_\partial=1.749269\ldots .
$$

*Proof.* Insert Lemmas 7.1 and 7.4 into (13). Away from the balls
$B(\eta_0,r_0)$ the contribution is $O(Ne^{-cN}N^{-5})$. The six points of
$\Sigma$ with non-trivial characters give
$O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})=O(N^{-8})$, using the Gaussian decay
of $\widetilde S_N$. The half-period identities of
Lemma 7.1(b) transport these local spectral estimates to
all eight points. The reciprocal eigenvalue branch has a bounded
projector on each small neighbourhood and is exponentially suppressed
after normalization. Its ratio to the dominant branch is
$e^{-2N\Phi_*}$ at the centre; shrinking the neighbourhood gives a
uniform $O(e^{-cN})$ bound with $c>0$. Near $\eta_0\in\{0,\pi u\}$ we make three replacements.
First, $\widetilde S_Ne^{-iN\eta\cdot v_*}$ is replaced by
$e^{-N\eta^TQ\eta/2}P$ (respectively $\overline P$), at cost
$N^{-5}\int(c_P|\eta|+Nc_3|\eta|^3)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.
Second, the layers are replaced by their leading forms, at cost
$N^{-5}\int(N^{-1/2}+|\eta_n|)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$. Third, the
integral is extended to $\mathbb R^3$, at cost $O(e^{-cNr_0^2})$. What
remains is

$$
N^{-5}\,\frac{512\pi}{3}\,\varphi_\partial\,c_r\,x_{0,\pi}\,\sqrt{\frac{2\pi}{Nq_n}}\;\frac2N\;(2\pi)^{-3}\int_{\mathbb R^2}e^{-q_t|\tau|^2}\mathcal S_\pm^2\,d^2\tau .
$$

Here we used $d^2\eta_t=(2/N)d^2\tau$ and
$N\eta^TQ\eta/2=Nq_n\eta_n^2/2+q_t|\tau|^2$. ∎

*Proof of Theorem 4.4.* By (12), the $e^{-K_*N}N^{-13/2}$ sector of
$L_{M,M_B}$ is $\ell(\mathcal T_\chi)$, where $\ell$ is the real-linear
functional $-2\operatorname{Im}$ for $M\in\{I,\sigma_1\}$,
$+2\operatorname{Im}$ for $M=\sigma_3$ and $+2\operatorname{Re}$ for
$M=\sigma_2$, and $\chi={\downarrow}$ for $M\in\{I,\sigma_3\}$,
$\chi={\uparrow}$ for $M\in\{\sigma_1,\sigma_2\}$. Since $\mathcal K$, $c_r$
and $\Gamma_\pm$ are real, Theorem 7.5 gives (10) with $\ell_0=\ell(x_0)$ and
$\ell_\pi=\ell(x_\pi)$. Closed forms of $\ell_0,\ell_\pi$ in terms of
$\alpha,c_*,\mathcal I_0,\mathcal I_1$ are listed in Appendix A.

The remainder budget, relative to $N^{-13/2}$, is as follows:

- $O(N^{-1/2})$ from the cubic term of the exponent, from $P(\eta)-P$, from
  the normal phase, and from the variation of $\varphi_N$ and $R_0$ across
  the layer;
- $O(N^{-1})$ from $r-N^{-3/2}R_0$ and from the exact profile and disc
  geometry;
- $O(N^{-3/2})$ from in-plane Poisson terms and from the six
  non-contributing torus points;
- $O(N^{-2})$ from $2\operatorname{Re}\langle r,Ea_c\rangle$;
- exponentially small terms from the region away from $\Sigma$ and from the
  sector $e^{-2K_*N}$.

Hence $L=e^{-K_*N}N^{-13/2}(C(\theta_N)+R_N)$ with $|R_N|\le C'N^{-1/2}$.

For non-vanishing, note that $\Gamma_-\ge0$. For every pair, interval
arithmetic certifies
$|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$. Therefore
$C(\theta)$ has the sign of $\ell_0$ for every $\theta$, and
$|C(\theta)/\overline{C}-1|\le(\varepsilon_+|\ell_0|+\varepsilon_-|\ell_\pi|)/(\overline\Gamma|\ell_0|)$,
which gives the bounds of Table 1. Since
$\inf_\theta|C(\theta)|\ge(1-1.5\cdot10^{-3})|\overline{C}|>0$, the remainder
cannot cancel the leading term for $N$ large, and the asymptotics of
$\delta=|L|$ follow. ∎

**Remark 7.6 (Counting the power).** The exponent $13/2$ decomposes as
follows. The resource contributes $\frac32$ at the layer and the free tail
$\frac32$ at Bob. The profiles $s_N$ and $h_N$ contribute $2+2$. The two
in-plane areas contribute $-2$. The normal Gaussian contributes $\frac12$,
and the tangential rescaling $d^2\eta_t=(2/N)d^2\tau$ contributes $1$. The
depths $j,j'$ are discrete sums of size $O(1)$ and contribute no power. The
common tangential direction $u_\perp+u'_\perp$ is a flat direction of the
exponent, because $\xi_*$ is orthogonal to the planes. It is confined by the
profiles and produces the area factors, not a Gaussian factor.

**Remark 7.7 (Dependence on $\theta_N$).** Since $\sqrt3/4\notin\mathbb Q$,
the sequence $\theta_N$ is equidistributed. $C(\theta_N)$ is therefore
quasi-periodic in $N$ and not a constant. The oscillation comes from the
commensurability of the lattice planes with the spheres bounding the regions.
It is below $0.15\%$, and it never changes the sign.

---

## 8. Discussion

### 8.1. What the theorem says and does not say

The theorem is a statement about one walk and one explicitly specified
family of operations.  It shows that the gap between the emergent
relativistic cone and the microscopic causal support is not merely
geometric.  Under an infrared-controlled protocol it carries an
operational response whose asymptotic law is known exactly: rate, power
and coefficient. Here infrared control qualifies the operations under
Definition 3.1; it does not identify the spectral origin
of the exponentially small response. The admissibility error is only
polynomially small and can exceed the entire response. The repository's
later hard-cutoff analysis for the fixed $\sigma_2/I$ pair records an
$\Theta(N^{-3})$ infrared block cancelled by the blocks involving its
complement (`state/CURRENT_STATE.md`, Sec. 10.1, with its scoped
review records). That result is not re-proved here. In particular, the
projected infrared block alone must not be identified with this signal.
The tilted representation also includes the saddle at $\pi u$, outside
the admissibility band centred at zero. The power $13/2$ depends on the
quadratic vanishing of the chosen profiles; no claim for other vanishing
orders or infinitely smooth cutoffs follows.
It does not claim that $D_B>0$ for every protocol, that
every quantum walk behaves this way, or that every smooth encoder
$M=aI+b\cdot\sigma$ signals.  It is not a violation of the model's
microcausality, since Bob remains inside $NC_{\mathrm{micro}}$.  The limit
$N\to\infty$ is an infrared scaling at fixed lattice units, not a continuum
limit $a,\tau\to0$.

The result is asymptotic.  The remainder constants and $N_*$ are finite but
not explicit.  The finite-$N$ diagnostics of Appendix A
suggest an effective relative correction of about $-100/N$ in the
semi-analytic approximation. No common range compares the exact signal
directly with the leading formula, so this does not establish a threshold
of quantitative accuracy for the exact signal. For
$M\in\{I,\sigma_3\}$ with $M_B=I$, whose coefficient is among the smallest,
the $N^{-17/2}$ term dominates over the whole diagnostic range.


### 8.2. Physical reading

Restoring a lattice spacing $a$, the integer $N$ is both the number of steps
and the separation scale in lattice units, so $N\sim\ell/a$ for a separation
$\ell$, and $\delta\sim e^{-K_*N}$ up to algebraic factors. The response is
therefore negligible at any separation large compared with the lattice
spacing; a quantitative threshold for exact-signal accuracy has not been established. We make no claim about observability, and regard the
result as a statement in the mathematical physics of finite-range unitary
dynamics. Its
interest lies in the structure it exhibits: an exact separation between
ballistic propagation, which respects $c_{\mathrm{IR}}$, and operational
influence, which does not vanish inside the corona even under infrared
control.

### 8.3. Open problems

1. General encoders $M=aI+b\cdot\sigma$, and optimisation over admissible
   operations.
2. Other walks, in particular the Bialynicki-Birula walk [9, Eq. (5.12)],
   whose corona contains ballistic modes faster than $c_{\mathrm{IR}}$, and
   the massive Dirac case.
3. Explicit remainder constants and $N_*$, which would make the statement
   effective at finite $N$.
4. Many-particle and second-quantized versions. The upper bound extends to
   even local unitaries on the full CAR algebra, with prefactor $288N^7$ in
   place of $36N^4$ [17], but no lower bound is available there.

---

## Appendix A. Computer-assisted parts and diagnostics

The kernel, geometry, counting and operator-bound components of Theorem 4.1,
the abstract one-particle signal inequality, and the inclusion part of Lemma 5.1 are formally
verified in Lean 4/Mathlib (`formal/` in [17]). The identification with the
protocol and the second-quantized distance $D_B$ are not formalized, as
specified in the formal-verification remark after Theorem 4.1.
The boundary equality characterization of Lemma 5.1 is also outside the
formalization and rests on the written proof.
The asymptotic results (Theorems 4.3 and 4.4) are not.
The analytic arguments above are complete up to the following verified
computations. All of them are performed by the certificate scripts listed in
[17], at the commit given there, with Python 3.12.3, SymPy 1.14.0 and mpmath
1.3.0. Exact identities use SymPy. Enclosures use the interval context
`mpmath.iv` with 50 digits, and only its elementary operations: the four
arithmetic operations, integer powers by repeated multiplication,
$\sqrt{\cdot}$, $\exp$, $\log$, $\sin$, $\cos$ and $\pi$. No interval
quadrature is used: $\mathcal I_0(\rho_*)$, $\mathcal I_1(\rho_*)$ and $I_b$
are enclosed through exact closed forms in $\sin$ and $\cos$, obtained from
the moments $\int_0^1k^m\{\sin,\cos\}(\omega k)\,dk$, $m\le5$, which are
checked symbolically.

- The symbol identities: Lemma 2.1, (5), and Lemma 7.1(a)–(b). Also the
  ellipse-lemma polynomials, $\cosh^3(\log2)=125/64$ and the vertex blocks.
- Closed forms and enclosures of $t_*$, $K_*$, $c_*^2$, $\Phi_*$, $q_t$,
  $q_n$, $P$, $\mathcal I_0$, $\mathcal I_1$, $\varphi_\partial$,
  $\mathcal K$, $\overline\Gamma$ and $\varepsilon_\pm$.
- The sixteen pairs $(\ell_0,\ell_\pi)$, the sign margin
  $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$, the
  bounds of Table 1, and $C(\sigma_3,\cdot)=-C(I,\cdot)$.

Closed forms of $\ell_0,\ell_\pi$ are given below, with $c=c_*$,
$A=\mathcal I_0(\rho_*)$ and $B=\mathcal I_1(\rho_*)$. The rows for
$\sigma_3$ are the negatives of the rows for $I$.

| $(M,M_B)$ | $\ell_0$ | $\ell_\pi$ |
| --- | --- | --- |
| $(I,I),\ (I,P_3)$ | $-\frac{\sqrt3}{3}\frac{B\alpha(c-1)}{c^2}$ | $+\frac{\sqrt3}{3}\frac{B\alpha(c+1)}{c^2}$ |
| $(I,P_1)$ | $\frac{3Ac\alpha-\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}$ | $-\frac{3Ac\alpha+\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}$ |
| $(I,P_2)$ | $\frac{3A\alpha-\sqrt3B(c^2\alpha+c^2+c\alpha-2\alpha)}{6c^2}$ | $\frac{3A\alpha-\sqrt3B(c^2\alpha+c^2-c\alpha-2\alpha)}{6c^2}$ |
| $(\sigma_1,I)$ | $-\frac{3A\alpha+\sqrt3B(c-c\alpha+\alpha)}{3c}$ | $\frac{3A\alpha-\sqrt3B(c-c\alpha-\alpha)}{3c}$ |
| $(\sigma_1,P_1)$ | $-\frac{3Ac\alpha+\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}$ | $\frac{3Ac\alpha-\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}$ |
| $(\sigma_1,P_2)$ | $-\frac{3A(c^2(1-\alpha)+c\alpha)+\sqrt3B(2c^2(1-\alpha)+2c\alpha-\alpha)}{6c^2}$ | $-\frac{3A(c^2(1-\alpha)-c\alpha)+\sqrt3B(2c^2(1-\alpha)-2c\alpha-\alpha)}{6c^2}$ |
| $(\sigma_1,P_3),\ (\sigma_2,P_3)$ | $-\frac{\sqrt3}{3}B(1-\alpha)$ | $-\frac{\sqrt3}{3}B(1-\alpha)$ |
| $(\sigma_2,I)$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}$ |
| $(\sigma_2,P_1)$ | $-\frac{3A(\alpha-c^2(1-\alpha))+\sqrt3Bc\alpha}{6c^2}$ | $-\frac{3A(\alpha-c^2(1-\alpha))-\sqrt3Bc\alpha}{6c^2}$ |
| $(\sigma_2,P_2)$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+c\alpha+2\alpha)}{6c^2}$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)-c\alpha+2\alpha)}{6c^2}$ |

**Finite-$N$ diagnostics.** These are floating-point and not used in any
proof; they use NumPy 1.26.4 and are produced by the `--diagnostics` option
of the coefficient certificate [17]. A floating-point FFT evaluation of the
exact discrete convolution formula in tilted variables ("brute") was compared
with a reference that keeps the exact lattice geometry but replaces the
kernel by its Gaussian form at the eight points of $\Sigma$. Their ratio
tends to $1$ with deviation of order $c/N$, $c\in[-0.5,14]$, at
$N=24,40,56$. For $M\in\{I,\sigma_3\}$ and $M_B=I$, the ratio of the
$N^{-17/2}$ piece $2\operatorname{Re}\langle r,Ea_c\rangle$ to the piece
$2\operatorname{Im}\langle r,Ea_{\downarrow}\rangle$ that carries the
$N^{-13/2}$ term is $15.2$, $9.4$ and $6.4$ at $N=24,40,56$. These ratios scale approximately
as $1/N$, not $1/N^2$, and do not validate the relative asymptotic order.
No common range compares the exact signal with the leading formula. A semi-analytic evaluation with discrete planes and exact
profiles gives semi/lead $=0.906$, $0.990$ and $0.997$ at $N=10^3$, $10^4$
and $3\cdot10^4$, consistent with a relative correction $\approx-100/N$. The
free tail agrees with $N^{-3/2}R_0$ to relative accuracy $2\cdot10^{-6}$ at
$N=40$ and $8\cdot10^{-9}$ at $N=640$.

---

## References

1. A. Ahlbrecht, H. Vogts, A. H. Werner, R. F. Werner, *Asymptotic evolution
   of quantum walks with random coin*, arXiv:1009.2019.
2. P. Arrighi, *An overview of quantum cellular automata*, arXiv:1904.12956.
3. Y. Baryshnikov, W. Brady, A. Bressler, R. Pemantle, *Two-dimensional
   quantum random walk*, J. Stat. Phys. **142**, 78–107 (2011),
   arXiv:0810.5495.
4. I. Bialynicki-Birula, *Weyl, Dirac, and Maxwell equations on a lattice as
   unitary cellular automata*, Phys. Rev. D **49**, 6920 (1994),
   arXiv:hep-th/9304070.
5. A. Bisio, G. M. D'Ariano, P. Perinotti, A. Tosini, *Free quantum field
   theory from quantum cellular automata: derivation of Weyl, Dirac and
   Maxwell quantum cellular automata*, arXiv:1601.04832.
6. L. Bombelli, J. Henson, R. D. Sorkin, *Discreteness without symmetry
   breaking: a theorem*, arXiv:gr-qc/0605006.
7. S. Bravyi, M. B. Hastings, F. Verstraete, *Lieb–Robinson bounds and the
   generation of correlations and topological quantum order*, Phys. Rev.
   Lett. **97**, 050401 (2006), arXiv:quant-ph/0603121.
8. H. A. Carteret, B. Richmond, N. M. Temme, *Evanescence in coined quantum
   walks*, J. Phys. A: Math. Gen. **38**, 8641–8665 (2005),
   arXiv:quant-ph/0506048.
9. C. Cedzich, A. Joye, A. H. Werner, R. F. Werner, *Exponential tail
   estimates for quantum lattice dynamics*, Ann. Henri Poincaré **27**,
   2843–2870 (2026), doi:10.1007/s00023-025-01598-4, arXiv:2408.02108.
10. G. M. D'Ariano, M. Erba, P. Perinotti, *Isotropic quantum walks on
    lattices and the Weyl equation*, Phys. Rev. A **96**, 062101 (2017),
    arXiv:1708.00826.
11. G. M. D'Ariano, P. Perinotti, *Derivation of the Dirac equation from
    principles of information processing*, Phys. Rev. A **90**, 062106
    (2014), arXiv:1306.1934.
12. T. Farrelly, *A review of quantum cellular automata*, Quantum **4**, 368
    (2020), arXiv:1904.13318.
13. G. Grimmett, S. Janson, P. F. Scudo, *Weak limits for quantum random
    walks*, Phys. Rev. E **69**, 026119 (2004), arXiv:quant-ph/0309135.
14. N. Konno, *Quantum random walks in one dimension*, Quantum Inf. Process.
    **1**, 345–354 (2002).
15. E. H. Lieb, D. W. Robinson, *The finite group velocity of quantum spin
    systems*, Commun. Math. Phys. **28**, 251–257 (1972).
16. R. Pemantle, M. C. Wilson, S. Melczer, *Analytic Combinatorics in Several
    Variables*, 2nd ed., Cambridge University Press (2024),
    doi:10.1017/9781108874144.
17. Repository `nacho09021973/qca-causal-cones`,
    <https://github.com/nacho09021973/qca-causal-cones>, commit
    `551addabe28b` (branch `research/b-infinity-post-s4-gate`). Certificates
    `scripts/verify_scaled_ir_gate.py`,
    `scripts/verify_regional_directional_asymptotics_gate.py`,
    `scripts/verify_regional_laplace_coefficient_gate.py`,
    `scripts/verify_directional_saturation.py`; Lean formalization in
    `formal/`.
18. B. Schumacher, R. F. Werner, *Reversible quantum cellular automata*,
    arXiv:quant-ph/0405174.
19. T. Sunada, T. Tate, *Asymptotic behavior of quantum walks on the line*,
    J. Funct. Anal. **262**, 2608–2645 (2012), arXiv:1108.1878.
20. A. Bressler, T. Greenwood, R. Pemantle, M. Petkovšek, *Quantum random
    walk on the integer lattice: examples and phenomena*, arXiv:0903.2967.
21. Y. Baryshnikov, R. Pemantle, *Asymptotics of multivariate sequences,
    part III: quadratic points*, arXiv:0810.4898.
22. R. Pemantle, M. C. Wilson, S. Melczer, *Analytic Combinatorics in Several
    Variables*, Expanded Second Edition, manuscript,
    <https://ACSVproject.com/PemantleWilsonMelczer23.pdf> (theorem numbers as
    in this manuscript; not compared with the printed edition [16]).
