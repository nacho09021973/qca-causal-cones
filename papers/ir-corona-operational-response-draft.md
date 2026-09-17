# An operational infrared response in the microscopic causal corona of a 3D Weyl quantum cellular automaton

**Draft, 2026-09-17.** Not submitted. Branch-local to
`research/b-infinity-post-s4-gate` at `0d21286`. The mathematical claims
are those frozen in `state/CURRENT_STATE.md` Secs. 8.4 and 8.16–8.20,
with independent review of the leading-coefficient analysis. This file
is a paper, not a gate report: it does not reopen encoder, detector,
geometry, or asymptotics, and it does not execute the physical-realization
gate.

## Abstract

In a finite-range quantum cellular automaton the relativistic speed that
emerges at long wavelength need not exhaust the microscopic causal
support. For the three-dimensional Weyl walk of Cedzich–Joye–Werner–Werner
(their Eq. (5.15)), every group velocity lies in the Euclidean unit ball
while the exact one-step support is the cube \([-1,1]^3\). The difference
is a *corona*: directions in which influence is causally allowed and
non-ballistic.

A localized, broadband Alice/Bob protocol can witness that corona in one
step, but that witness is a ultraviolet propagator effect. The question
addressed here is whether an *infrared-controlled* protocol still leaves
a non-vanishing operational response. For the preregistered family of
Pauli encoders and detectors, Euclidean regions of radius \(N/4\), and
a compactly supported momentum profile of width \(1/N\), the
distinguishability at Bob after \(N\) steps admits the regional Laplace
expansion

\[
\delta_{M,M_B}(N)
=
\bigl|C_{M,M_B}(\theta_N)\bigr|\,
N^{-13/2}\,
e^{-K_* N}
\bigl(1+O(N^{-1/2})\bigr),
\]

with \(K_*=I(v_*)\) the unique regional Legendre rate, strictly between
the scaled-IR majorant \(J=(1-\sqrt3/2)\log 2\) and the vertex rate
\(\log 4\), and with \(C(\theta)\) uniformly non-vanishing for the twelve
Pauli pairs. The coefficient depends on the lattice–sphere
commensurability phase \(\theta_N=\{\sqrt3 N/4\}\); the oscillation is
bounded by \(1.5\times10^{-3}\) relatively and does not change sign.

The result is a property of the model. It is not a statement about
nature, not a designed experiment, and not a claim that \(D_B>0\) for
every QCA. Ultraviolet propagation, infrared operational response, and
physical realization are three different questions.

## 1. The claim, and three questions that must not be mixed

The slogan that “\(c\) is the maximum speed of the substrate” does not
survive as an identity of convex bodies once the substrate is a
finite-range lattice in dimension \(d\ge 2\). The infrared velocity set
of a Weyl node is a Euclidean ball. The microscopic causal body
\(C_{\mathrm{micro}}\) of a finite neighborhood is a polytope. A ball is
not a polytope, so exact coincidence is geometrically impossible under
those hypotheses.

That geometric gap is not, by itself, an operational statement. Three
questions must be kept apart.

**(U) Ultraviolet propagator.** Does the exact kernel of the walk assign
non-zero amplitude to some site outside the infrared ball and inside
\(C_{\mathrm{micro}}\)? For the walk below, the eight body-diagonal
vertices have a unique path and amplitude \(4^{-N}\). Localized
one-step Alice/Bob protocols can convert that fact into a finite
distinguishability (the non-corner witness \(3/128\)). Those protocols
are broadband. They do not answer the infrared question.

**(I) Infrared operational response.** If Alice’s preparation, her
encoder, and Bob’s detector are required to be infrared-admissible, and
if Bob’s region lies outside the infrared cone of *every* site of Alice,
does Bob’s distinguishability remain non-zero as the infrared scale
tends to zero? A positive answer is compatible with an exponentially
small signal. A vanishing answer is compatible with a non-zero
ultraviolet kernel.

**(N) Nature.** Can the dimensionless law of (I) be identified with a
physical system in which the lattice scale, the internal degrees of
freedom, and the operations are not put in by an experimenter? That is a
different problem. It is not solved here.

The theorem of this paper is a result of type (I), for one frozen walk
and one frozen protocol. It uses (U) only as geometry and as a warning
not to confuse a vertex ray with a regional leader.

## 2. The walk

Units: one lattice step per update. The one-particle symbol is the Weyl
walk of Cedzich–Joye–Werner–Werner, Ann. Henri Poincaré (2025),
Eq. (5.15), equivalently (up to the global \(p=k/\sqrt3\) rescaling) a
standard Pavia Weyl automaton on the cubic lattice. In the coordinates
\(p\) of (5.15),

\[
C_{\mathrm{micro}}=[-1,1]^3,
\qquad
c_{\mathrm{IR}}=1,
\qquad
\sup_p|\nabla\omega(p)|=1.
\]

The group-velocity envelope fills the Euclidean unit ball (the filling
of the open ball is numerical; the counterexample needs only the exact
identity \(\sup|v_g|=c_{\mathrm{IR}}\)). Thus

\[
B(c_{\mathrm{IR}})
\;\subsetneq\;
C_{\mathrm{micro}}.
\]

Along a unit direction \(\hat n\), the support-function ratio is
\(S(\hat n)=1/\|\hat n\|_1\). Saturation \(S=1\) holds only on the six
axes. The body diagonal has \(S_{\min}=1/\sqrt3\). The *corona* is the
set of velocities in \(C_{\mathrm{micro}}\setminus B(c_{\mathrm{IR}})\).
Propagation there is non-ballistic. It is not causally forbidden: the
amplitude is exactly zero only outside \(C_{\mathrm{micro}}\).

On the eight vertices a unique path gives
\((S^N)_{(N,N,N),0}=4^{-N}|\downarrow\rangle\langle\downarrow|\). That
ray is not the regional leader: it annihilates the up component, it does
not represent an extended region, and its rate \(\log 4\) is strictly
faster than the regional rate derived below.

## 3. The infrared protocol

The protocol is the scaled infrared class frozen before the coefficient
calculation (and not varied afterwards).

- Resource: a compactly supported profile \(g(Np)=(1-|Np|^2)^2_+\) on
  the down spinor, so the free tail at Bob is the Weyl packet
  \(r=S^N\phi_N=O(N^{-3/2})\).
- Geometry, \(N\ge 2\): Euclidean balls
  \(A_N=\mathbb Z^3\cap\overline B_2(0,N/4)\) and
  \(B_N=\mathbb Z^3\cap\overline B_2(N(1,1,1),N/4)\), with frozen radial
  profiles that vanish on the spheres.
- Time: \(N\) updates. Every pair \((x,y)\in A_N\times B_N\) then
  satisfies \(\hat u\cdot(y-x)\ge N|v_*|\) with equality only at the
  facing pair, where
  \(v_*=\bigl(1-1/(2\sqrt3)\bigr)(1,1,1)\) and
  \(\hat u=(1,1,1)/\sqrt3\).
- Encoders \(M\in\{I,\sigma_1,\sigma_2,\sigma_3\}\) and detectors
  \(M_B\in\{I,(I+\sigma_j)/2\}\). The identity encoder is a reference
  control, not a negative control. No Pauli equivalence is assumed.
- Signal: \(\delta=|L|\), with \(L\) the unprojected response functional
  of the one-particle sector (identities (L) and (F) of the scaled-IR
  analysis).

A pointlike encoder at the origin is incompatible with a relative
infrared criterion (narrow-band gate). That negative is not a vanishing
theorem for other encoders. The protocol above replaces the point gate
by a regional, profiled encoder and lets the infrared scale run with
\(N\).

A uniform majorant, independent of pair, is

\[
\delta(N)\le D_B(N)\le 36 N^4 e^{-JN},
\qquad
J=\bigl(1-\tfrac{\sqrt3}{2}\bigr)\log 2>0.
\]

Polynomial infrared signalling is thereby excluded without any lower
bound. The bound is compatible with \(\delta\sim A(N)e^{-KN}\), with
\(\delta\sim e^{-2JN}\), and with \(\delta\equiv0\). Existence is the
content of the next two sections.

## 4. Regional rate

The Legendre envelope of the tilted kernel is

\[
I(v)=\sup_{\xi}\Bigl[\xi\cdot v-\operatorname{arcosh}\Bigl(\prod_{j=1}^3\cosh\xi_j\Bigr)\Bigr].
\]

On the regional velocity set, \(I\) is minimized uniquely at \(v_*\),
with dual tilt \(\xi_*=t_*(1,1,1)\). The value \(K_*=I(v_*)\) satisfies

\[
J<K_*<\log 4.
\]

Profile logarithms are \(O(\log N)\) and shift the effective saddle by
\(O(1)\) lattice sites. They change the power and the coefficient; they
do not change \(K_*\). The geometric facing point, where the profiles
vanish, is therefore not the physical leader.

The spectral radius of \(S(\eta-i\xi_*)\) attains \(e^{\varphi_*}\) at
the eight torus points \(\{0,\pi\}^3\), not only at the origin. The
rate is unaffected (same spectral radius). Only two of those points have
trivial characters on the lattice planes \(x_1+x_2+x_3=k\), namely
\(\eta=0\) and \(\eta=\pi(1,1,1)\). Both enter the leading coefficient,
with projectors \(P\) and \(\overline P\).

## 5. Leading coefficient

The complete leading term at rate \(K_*\) is not a product of local
factors. It is the interference of the free tail \(r\) against the
encoder layer, summed over the two contributing torus saddles, the
discrete depth sums of Alice and Bob, the Hessian, the profiles, and the
Perron projector with its phases.

Quadratic terms in the encoder amplitudes sit at \(e^{-2K_*N}\) and are
only bounded. They are not promoted to coefficients of the
\(e^{-K_*N}\) sector. The piece \(2\operatorname{Re}\langle r,Ea\rangle\)
(the \(c_N=O(F^2)\) channel) is \(N^{-17/2}e^{-K_*N}\): same exponential,
two algebraic orders down.

The power \(\beta=13/2\) is a factor count, not a count of Gaussian
directions. Depths are discrete half-space sums of scale \(O(1)\). The
Alice–Bob shared tangent is a flat direction of the exponent, confined
by profile support. Only three momentum directions are Gaussian.

For every one of the sixteen pairs,

\[
L_{M,M_B}(N)
=
e^{-K_*N}N^{-13/2}
\bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\bigr),
\qquad
\theta_N=\bigl\{\sqrt3 N/4\bigr\}.
\]

The function \(C(\theta)\) is continuous, 1-periodic, and
quasi-periodic in \(N\). Interval enclosures give, uniformly in
\(\theta\),

\[
C_{M,M_B}(\theta)
=
\overline C_{M,M_B}\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad
|\vartheta|\le 1.47\times10^{-3},
\qquad
\overline C_{M,M_B}\neq0.
\]

The twelve pairs with \(M\in\{\sigma_1,\sigma_2,\sigma_3\}\) are
non-vanishing. The structurally most robust is \(\sigma_2\), for which
both saddles contribute with the same sign. The identity encoder is
also non-vanishing; it is not used as a substitute for a Pauli pair.
Exactly, \(C(\sigma_3,\cdot)=-C(I,\cdot)\) at leading order.

The remainder is \(O(N^{-1/2})\) with non-explicit constants. Combined
with \(\inf_\theta|C(\theta)|>0\), there exists a finite \(N_*\) (not
computed) beyond which the remainder cannot cancel the leader. The
formula is an asymptotic statement. It is not quantitatively reliable
for \(N\lesssim10^3\); for \(M\in\{I,\sigma_3\}\) a lower-order piece
dominates throughout the diagnostic range \(N\le56\).

## 6. Theorem

**Theorem.** In the frozen class of Sec. 3, for each of the twelve
Pauli pairs and for all sufficiently large \(N\),

\[
\delta_{M,M_B}(N)
=
\bigl|C_{M,M_B}(\theta_N)\bigr|
N^{-13/2}e^{-K_*N}
\bigl(1+O(N^{-1/2})\bigr)
\neq0.
\]

The signal is infrared-admissible and lies outside the emergent cone of
every Alice site. It is nonperturbatively suppressed:
\(\delta=o(N^{-k})\) for every \(k\), and \(\delta\le 36N^4 e^{-JN}\).

**Corollary (model, not nature).** In this 3D Weyl QCA, the difference
between the emergent relativistic cone and the microscopic causal
support is not only a geometric possibility. Under the preregistered
infrared-controlled protocol it produces an asymptotically
non-vanishing operational response, albeit nonperturbatively
suppressed.

## 7. What the theorem is not

- It is not \(D_B=0\), and it is not a computation of \(D_B\) beyond
  the response \(L\).
- It is not a statement about every QCA, every encoder, or the general
  family \(M=aI+b\cdot\sigma\).
- It is not a continuum limit \(a,\tau\to0\). The limit \(N\to\infty\)
  is an infrared scaling at fixed lattice units.
- It is not a violation of the model’s own microcausality:
  Bob remains inside \(C_{\mathrm{micro}}\).
- It is not a physical prediction in metres, seconds, or detector
  counts. The sources do not fix \(a\) or \(\tau\); identifying
  \(a/\tau\) with an observed \(c\) calibrates a ratio, not an
  absolute scale.
- It is not an experimental design, and it is not evidence that the
  walk is the microscopic substrate of nature.

The last two items are a different problem. A positive theoretical
signal does not become a laboratory protocol by changing units, and an
engineered simulator of a Dirac walk does not become a fundamental
identification by sharing a continuum limit.

## 8. Proof architecture (for the reader of the frozen notes)

The argument is recorded, with certificates, in the repository named at
the head of this draft. The load-bearing steps are:

1. Geometry of \(C_{\mathrm{micro}}\) versus \(B(c_{\mathrm{IR}})\) for
   (5.15): exact SOS identity for \(\sup|v_g|=1\).
2. Infrared admissibility of the eight operations, and the uniform
   exponential majorant \(36N^4 e^{-JN}\).
3. Identification of \(K_*=I(v_*)\) as the unique regional rate;
   profiles \(O(\log N)\).
4. Factor count \(\beta=13/2\); two torus saddles; complete coefficient
   as a *sum*; quadratic terms only bounded.
5. Interval enclosures of \(\overline C\neq0\) uniformly in \(\theta\);
   remainder \(O(N^{-1/2})\).

Independent review of (3)–(5) returned PASS, with no mandatory
repairs. Software certificates cover algebraic identities and
enclosures (58/58 for the coefficient), not the analytic remainder
lemmas.

## 9. Outlook

The model question of type (I) is closed in this class. The next
scientific question is of type (N): whether there exists a physically
defensible identification of \((a,\tau,\Lambda)\), the two internal
modes, and the operations \((M,M_B)\) with magnitudes and operations in
a natural system, converting the law of the Theorem into a dimensional
and falsifiable prediction. That question has four independent closure
criteria—absolute scale, physical dictionary, dimensional observable,
detectability—and first-class negative outcomes. None of them reopens
the Theorem.

If no such identification exists, the Theorem remains a result in the
mathematical physics of finite-range unitary dynamics. That is a
complete paper.

## References (primary, not exhaustive)

1. C. Cedzich, A. Joye, A. H. Werner, R. F. Werner, *Exponential tail
   estimates for quantum lattice dynamics*, Ann. Henri Poincaré (2025),
   arXiv:2408.02108.
2. G. M. D’Ariano, P. Perinotti, *Derivation of the Dirac equation from
   principles of information processing*, Phys. Rev. A **90**, 062106
   (2014).
3. A. Bisio, G. M. D’Ariano, P. Perinotti, A. Tosini, *Free quantum
   field theory from quantum cellular automata*, Phys. Rev. A **93**,
   062334 (2016), arXiv:1601.04832.
4. G. M. D’Ariano, M. Erba, P. Perinotti, *Isotropic quantum walks on
   lattices and the Weyl equation*, Phys. Rev. A **96**, 062101 (2017).
5. I. Bialynicki-Birula, *Weyl, Dirac, and Maxwell equations on a
   lattice as quantum cellular automata*, Phys. Rev. D **49**, 6925
   (1994).
6. Repository `nacho09021973/qca-causal-cones`, branch
   `research/b-infinity-post-s4-gate`, `state/CURRENT_STATE.md`
   Secs. 8.4, 8.16–8.20, and the reports cited there.
