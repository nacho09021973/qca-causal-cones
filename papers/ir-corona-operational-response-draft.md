# A prefactor-level operational large-deviation asymptotic for a 3D Weyl-cone quantum walk

**Revised draft, 2026-09-17.** Not submitted. Based on branch
`research/b-infinity-post-s4-gate` at `e15da39`. The mathematical claims
are those frozen in `state/CURRENT_STATE.md` Secs. 8.4 and 8.16–8.20,
with independent review of the leading-coefficient analysis. This paper
does not reopen encoder, detector, geometry, or asymptotics, and it does
not execute the physical-realization gate.

## Abstract

We study the modified three-dimensional two-component quantum walk of
Cedzich–Joye–Werner–Werner (CJWW), their Eq. (5.15). Its long-wavelength
dispersion has an isotropic Weyl cone with infrared speed one in the
coordinates used here, while its exact one-step causal body is the cube
\([-1,1]^3\). CJWW proved that all group velocities satisfy
\(|\nabla\omega|\le 1\) and developed exponential large-deviation bounds
outside the propagation region. We consider a preregistered Alice/Bob
protocol whose entire regional velocity set lies strictly outside that
propagation region but remains inside the microscopic causal body.

For Pauli encoders and detectors, Euclidean regions of radius \(N/4\),
and a compactly supported momentum profile of width \(1/N\), the Bob
response has the asymptotic form

\[
\delta_{M,M_B}(N)
=
\bigl|C_{M,M_B}(\theta_N)\bigr|\,
N^{-13/2}\,
e^{-K_* N}
\bigl(1+O(N^{-1/2})\bigr),
\]

where \(K_*=I(v_*)\) is the unique regional Legendre rate,
\(J<K_*<\log4\), and \(C_{M,M_B}(\theta)\) is uniformly non-vanishing for
the twelve Pauli pairs. The coefficient is modulated by the
lattice–sphere commensurability phase
\(\theta_N=\{\sqrt3 N/4\}\), with relative oscillation below
\(1.5\times10^{-3}\) in the certified enclosure.

The existence of exponential tails outside a propagation region is not
new: CJWW give the rate-function framework, and prefactor-level
large-deviation asymptotics are known for one-dimensional coined walks.
The contribution here is narrower. To our knowledge, this is the first
prefactor-level, rigorously non-vanishing operational large-deviation
asymptotic for a three-dimensional multi-component quantum walk in a
strictly outside-propagation-region geometry. The result is a property
of the model, not a statement about nature or an experimental design.

## 1. Three questions that must not be mixed

A finite-range lattice walk has at least three distinct velocity objects:
the infrared cone, the propagation region determined by group velocities,
and the microscopic causal body determined by exact finite-range support.
They need not coincide. The present result concerns one specific relation
among them and should not be read as a claim that every point outside an
infrared cone is evanescent.

We separate three questions.

**(U) Ultraviolet propagator.** Does the exact kernel assign non-zero
amplitude to some site outside the infrared ball and inside the
microscopic causal body \(C_{\mathrm{micro}}\)? For the walk below, the
eight body-diagonal vertices have a unique path and a non-zero
exponentially small amplitude. Localized Alice/Bob protocols can convert
such ultraviolet support into finite distinguishability, but those
protocols are broadband.

**(I) Infrared operational large deviation.** If Alice's preparation,
encoder, and Bob's detector are infrared-admissible, and the complete
regional velocity set of the protocol lies outside the propagation
region \(\Gamma\), does Bob's operational response remain non-zero as the
infrared scale tends to zero? A positive answer is compatible with an
exponentially small signal. This is the question answered here.

**(N) Nature.** Can the dimensionless law of (I) be identified with a
natural physical system in which the lattice scale, internal degrees of
freedom, and operations are not simply imposed by an experimenter? That
is a separate physical-realization problem and is not solved here.

The theorem is therefore a result of type (I), for one frozen walk and
one frozen protocol. It uses (U) as causal geometry, not as evidence for
an infrared signal, and it makes no type-(N) claim.

## 2. The modified CJWW walk and its three velocity sets

Units are one lattice coordinate step per update. The one-particle
symbol is the **modified** three-dimensional walk introduced by
Cedzich–Joye–Werner–Werner in Eq. (5.15). Its dispersion satisfies

\[
\cos\omega(p)=\cos p_1\cos p_2\cos p_3.
\]

This identification is important. Eq. (5.15) is **not** the standard
body-centred-cubic Weyl automaton of Białynicki-Birula or
D'Ariano–Perinotti, whose dispersion contains the additional
\(\pm\sin p_1\sin p_2\sin p_3\) term (up to convention and global
rescaling). CJWW introduce (5.15) as a modified model sharing Weyl-cone
structure while having a particularly simple propagation-speed bound.

For (5.15),

\[
C_{\mathrm{micro}}=[-1,1]^3,
\qquad
c_{\mathrm{IR}}=1.
\]

Let

\[
\Gamma=\overline{\{\nabla\omega(p):p\text{ regular}\}}
\]

denote the propagation region. The exact sum-of-squares identity used
in the frozen analysis implies

\[
|\nabla\omega(p)|\le1,
\]

hence

\[
\Gamma\subseteq \overline B_2(0,1)
\subsetneq C_{\mathrm{micro}}.
\]

The numerical evidence that \(\Gamma\) fills the open unit ball is not
needed below. All that is required for the theorem is the exact inclusion
\(\Gamma\subseteq\overline B_2(0,1)\).

Along a unit direction \(\hat n\), the microscopic support function is
\(h_{C_{\mathrm{micro}}}(\hat n)=\|\hat n\|_1\). The ratio of the
infrared support function to the microscopic one is therefore

\[
S(\hat n)=\frac1{\|\hat n\|_1}.
\]

Saturation occurs only on the six coordinate axes, while the body
diagonal gives \(S_{\min}=1/\sqrt3\). For this modified walk, every
velocity with Euclidean norm strictly larger than one is automatically
outside \(\Gamma\), although it may remain inside the microscopic cube.
That is the large-deviation sector used in the theorem.

On the eight cube vertices a unique path gives, for the frozen spin
convention,

\[
(S^N)_{(N,N,N),0}
=4^{-N}|\downarrow\rangle\langle\downarrow|.
\]

That vertex ray is not the regional leader: it is a special ultraviolet
path, does not represent the extended Alice/Bob geometry, and its rate
\(\log4\) is strictly faster than the regional rate derived below.

## 3. The infrared protocol and strict separation from \(\Gamma\)

The protocol is the scaled infrared class frozen before the coefficient
calculation and not varied afterwards.

- Resource: a compactly supported profile
  \(g(Np)=(1-|Np|^2)^2_+\) on the down spinor, so the free tail at Bob is
  the Weyl packet \(r=S^N\phi_N=O(N^{-3/2})\).
- Geometry, \(N\ge2\):
  \[
  A_N=\mathbb Z^3\cap\overline B_2(0,N/4),\qquad
  B_N=\mathbb Z^3\cap\overline B_2(N(1,1,1),N/4),
  \]
  with frozen radial profiles that vanish on the spheres.
- Encoders \(M\in\{I,\sigma_1,\sigma_2,\sigma_3\}\) and detectors
  \(M_B\in\{I,(I+\sigma_j)/2\}\). The identity encoder is a reference
  control, not a negative control. No Pauli equivalence is assumed.
- Signal: \(\delta=|L|\), with \(L\) the unprojected response functional
  of the one-particle sector inherited from the scaled-IR analysis.

For every \(x\in A_N\) and \(y\in B_N\), the scaled displacement
\(v=(y-x)/N\) obeys

\[
v\in (1,1,1)+\overline B_2(0,1/2).
\]

Therefore

\[
|v|_2\ge \sqrt3-\frac12>1.
\]

Since \(\Gamma\subseteq\overline B_2(0,1)\), the entire regional velocity
set satisfies the exact, uniform separation

\[
\boxed{V_{\mathrm{reg}}\cap\Gamma=\varnothing.}
\]

The unique minimum-norm point is

\[
v_*=\Bigl(1-\frac1{2\sqrt3}\Bigr)(1,1,1),
\qquad
|v_*|_2=\sqrt3-\frac12.
\]

Thus the theorem is not merely about being outside the infrared cone: the
frozen Alice/Bob geometry lies strictly in the large-deviation region
outside \(\Gamma\), while remaining inside \(C_{\mathrm{micro}}\).

A pointlike encoder at the origin is incompatible with the relative
infrared criterion used in the earlier narrow-band gate. That negative
result is not a vanishing theorem for regional encoders. The frozen
protocol above replaces the point gate by a regional, profiled encoder
and lets the infrared scale run with \(N\).

A uniform majorant, independent of pair, is

\[
\delta(N)\le D_B(N)\le 36N^4e^{-JN},
\qquad
J=\Bigl(1-\frac{\sqrt3}{2}\Bigr)\log2>0.
\]

This excludes polynomially large infrared signalling but provides no
lower bound. It is compatible with several exponentially small sectors
and with exact cancellation. Establishing non-cancellation is the content
of the next two sections.

## 4. Regional rate

The Legendre envelope of the tilted kernel is

\[
I(v)=\sup_{\xi}\left[
\xi\cdot v-
\operatorname{arcosh}\left(\prod_{j=1}^3\cosh\xi_j\right)
\right].
\]

On the regional velocity set, \(I\) is minimized uniquely at \(v_*\),
with dual tilt \(\xi_*=t_*(1,1,1)\). The value

\[
K_*=I(v_*)
\]

satisfies

\[
J<K_*<\log4.
\]

Profile logarithms are \(O(\log N)\) and shift the effective saddle by
\(O(1)\) lattice sites. They change the algebraic power and coefficient,
but not \(K_*\). The geometric facing point, where the profiles vanish,
is therefore not itself the physical leader.

The spectral radius of \(S(\eta-i\xi_*)\) reaches the equal-rate maximum
at the eight torus points \(\{0,\pi\}^3\). The rate is the same at all
eight. After the lattice-plane character sum is imposed, only
\(\eta=0\) and \(\eta=\pi(1,1,1)\) contribute to the leading coefficient;
they enter with projectors \(P\) and \(\overline P\), respectively.

## 5. Leading coefficient

The complete leading term at rate \(K_*\) is not a product of independent
local factors. It is the interference of the free tail \(r\) against the
encoder layer, after summing the contributing torus saddles, the discrete
depth sums of Alice and Bob, the Hessian, the profiles, and the Perron
projectors with their phases.

Quadratic terms in encoder amplitudes sit at \(e^{-2K_*N}\) and are only
bounded. They are not promoted to algebraic corrections in the
\(e^{-K_*N}\) sector. The piece
\(2\operatorname{Re}\langle r,Ea\rangle\), associated with the
\(c_N=O(F^2)\) channel, is \(N^{-17/2}e^{-K_*N}\): the same exponential
rate, but two algebraic orders down.

The power \(\beta=13/2\) follows from the full factor count, not from a
naive count of Gaussian directions. The Alice and Bob depth variables
are discrete half-space sums of scale \(O(1)\); the shared Alice–Bob
tangent is a flat direction of the exponent confined by profile support;
only three momentum directions are Gaussian.

For every one of the sixteen frozen pairs,

\[
L_{M,M_B}(N)
=
e^{-K_*N}N^{-13/2}
\left(C_{M,M_B}(\theta_N)+O(N^{-1/2})\right),
\qquad
\theta_N=\left\{\frac{\sqrt3N}{4}\right\}.
\]

The function \(C(\theta)\) is continuous and 1-periodic in \(\theta\),
so its evaluation along \(\theta_N\) is quasiperiodic in \(N\). Certified
interval enclosures give, uniformly in \(\theta\),

\[
C_{M,M_B}(\theta)
=
\overline C_{M,M_B}
\left(1+\vartheta_{M,M_B}(\theta)\right),
\qquad
|\vartheta|\le1.47\times10^{-3},
\qquad
\overline C_{M,M_B}\neq0.
\]

The twelve pairs with \(M\in\{\sigma_1,\sigma_2,\sigma_3\}\) are
non-vanishing. The \(\sigma_2\) channel is structurally especially
transparent because the two contributing saddle terms have the same
sign. The identity encoder is also non-vanishing but is not used as a
substitute for a Pauli result. At leading order,

\[
C(\sigma_3,\cdot)=-C(I,\cdot)
\]

exactly.

The remainder is \(O(N^{-1/2})\) with non-explicit constants. Combined
with \(\inf_\theta|C(\theta)|>0\), this implies the existence of a finite
\(N_*\) beyond which the remainder cannot cancel the leader. The formula
is asymptotic; it is not claimed to be quantitatively accurate at the
small \(N\) values used for diagnostics.

## 6. Theorem

**Theorem.** For the modified CJWW walk (5.15) and the frozen protocol of
Sec. 3, every Alice-to-Bob regional velocity lies in
\(C_{\mathrm{micro}}\setminus\Gamma\). For each of the twelve Pauli
encoder–detector pairs and all sufficiently large \(N\),

\[
\delta_{M,M_B}(N)
=
\bigl|C_{M,M_B}(\theta_N)\bigr|
N^{-13/2}e^{-K_*N}
\bigl(1+O(N^{-1/2})\bigr)
\neq0.
\]

The response is infrared-admissible and nonperturbatively suppressed:

\[
\delta=o(N^{-k})\quad\text{for every }k,
\qquad
\delta\le36N^4e^{-JN}.
\]

**Corollary (model, not nature).** In the modified three-dimensional
CJWW walk, the part of the microscopic causal body sampled by the frozen
protocol lies beyond the propagation region yet supports an
asymptotically non-vanishing operational infrared response. The response
is exponentially small and does not violate the walk's own microscopic
causal support.

## 7. What the theorem is not

- It is not a theorem that all velocities outside an infrared Weyl cone
  are evanescent. That statement is model-dependent and is false for
  other Weyl walks, including the BCC/Pavia-type symbol with the
  \(\pm s_1s_2s_3\) term.
- It is not a computation of the optimal distinguishability \(D_B\)
  beyond the stated response functional \(L\).
- It is not a statement about every quantum walk, QCA, encoder, detector,
  or the general family \(M=aI+b\cdot\sigma\).
- It is not a continuum limit \(a,\tau\to0\). The limit \(N\to\infty\)
  is an infrared scaling at fixed lattice units.
- It is not a violation of microscopic causality: Bob remains inside
  \(C_{\mathrm{micro}}\).
- It is not a prediction in metres, seconds, energies, or detector
  counts. The model does not determine an absolute physical lattice
  spacing or update time.
- It is not an experimental design and not evidence that (5.15) is the
  microscopic substrate of nature.

An engineered simulator of the same walk could test the model law, but
that would be a realization of the dynamics, not evidence that the walk
is fundamental.

## 8. Proof architecture

The complete derivation and certificates are recorded in the repository
named at the head of this draft. The load-bearing steps are:

1. **Velocity geometry.** For (5.15), the exact SOS identity gives
   \(|\nabla\omega|\le1\), while the frozen regional geometry gives
   \(|v|\ge\sqrt3-1/2>1\). Hence \(V_{\mathrm{reg}}\cap\Gamma=\varnothing\).
2. **Infrared admissibility and upper bound.** The eight frozen operations
   are infrared-admissible and satisfy the uniform majorant
   \(36N^4e^{-JN}\).
3. **Regional exponential rate.** The unique regional minimizer is
   \(v_*\) and \(K_*=I(v_*)\); profile logarithms are only \(O(\log N)\).
4. **Prefactor structure.** The factor count gives \(\beta=13/2\).
   There are eight equal-rate torus maxima; after lattice-plane characters
   are summed, two contribute to the leading coefficient. The full
   coefficient is a sum, not a product, and quadratic pieces remain in
   the \(e^{-2K_*N}\) sector.
5. **Non-cancellation.** Interval enclosures prove the leading coefficient
   is uniformly separated from zero for all frozen pairs, and the analytic
   remainder is \(O(N^{-1/2})\).

Independent review of the regional rate and leading-coefficient analysis
returned PASS. Software certificates cover algebraic identities and
interval enclosures; the analytic remainder lemmas remain mathematical
arguments rather than numerical evidence.

## 9. Relation to prior work and scope of novelty

The existence of exponentially small tails outside a propagation region
is established prior art. CJWW prove exponential tail estimates for
translation-invariant quantum lattice dynamics and construct the
Legendre-type rate function used here. For their modified model (5.15),
they analyze the radial rate and its near-boundary behaviour. Their method
is deliberately a rate/bound framework and does not supply the
prefactor-level pointwise asymptotic derived here.

Sharp outside-support asymptotics with prefactors are known in one
dimension. Sunada and Tate derive large-deviation asymptotics for
one-dimensional two-state quantum walks, including the rate function and
wall/Airy behaviour. Carteret, Richmond and Temme obtain uniformly
convergent asymptotics in the exponentially decaying regions of the
one-dimensional coined walk. These works are the closest direct
precursors to the present steepest-descent calculation, but they do not
cover a three-dimensional multi-component saddle geometry or the frozen
operational response considered here.

In two dimensions, Baryshnikov, Brady, Bressler and Pemantle analyze
quantum random walks using multivariate generating functions and derive
the probability profile in the feasible region; outside that region the
probability is exponentially small, but their result does not give the
present deep-outside prefactor-level operational law.

Analytic combinatorics in several variables provides powerful general
transfer theorems for multivariate coefficient asymptotics. The standard
sharp transfer results are formulated under minimal-critical-point
hypotheses. We therefore do **not** claim that ACSV is incapable in
principle of reproducing the present result. The narrower statement is
that we are not aware of an existing off-the-shelf multivariate transfer
theorem that directly yields this strictly large-deviation,
complex-saddle prefactor together with the non-vanishing oscillatory
coefficient. The calculation here performs that model-specific saddle
analysis explicitly.

There is also a broad lattice-field-theory and lattice-Green-function
literature on exponentially decaying spacelike or massive propagators.
Those results are important analogues but have a different analytic
object and scaling problem: the present theorem concerns a discrete-time
unitary, two-component walk and a frozen operational response, with an
explicit \(N^{-13/2}\) prefactor and a certified quasiperiodic leading
coefficient.

Accordingly, the novelty claim is intentionally narrow:

> **To our knowledge, the theorem gives the first prefactor-level
> asymptotic with a rigorously non-vanishing oscillatory leading
> coefficient for an infrared-controlled operational response in the
> strictly outside-propagation-region regime of a three-dimensional
> multi-component quantum walk.**

This claim does not include the discovery of exponential evanescence,
large-deviation rates, Weyl-cone dispersion, or microscopic support
outside an emergent cone; all of those have prior art.

## 10. Outlook

The model question is closed in the frozen class. The next scientific
question is whether there exists a physically defensible identification
of \((a,\tau,\Lambda)\), the two internal modes, and the operations
\((M,M_B)\) with quantities and operations in a natural system, thereby
converting the dimensionless theorem into a falsifiable physical
prediction.

That physical-realization problem has four logically independent
criteria: absolute scale, physical dictionary, dimensional observable,
and detectability. A negative answer to any of those questions does not
weaken the mathematical theorem.

If no natural realization exists, the result remains a theorem in the
mathematical physics of finite-range unitary dynamics. An engineered
realization of the walk would instead constitute a separate simulator
question.

## References

1. C. Cedzich, A. Joye, A. H. Werner, R. F. Werner, *Exponential Tail
   Estimates for Quantum Lattice Dynamics*, Ann. Henri Poincaré **27**,
   2843–2870 (2026), DOI 10.1007/s00023-025-01598-4; arXiv:2408.02108.
2. T. Sunada, T. Tate, *Asymptotic behavior of quantum walks on the
   line*, J. Funct. Anal. **262**, 2608–2645 (2012),
   DOI 10.1016/j.jfa.2011.12.016; arXiv:1108.1878.
3. H. A. Carteret, B. Richmond, N. M. Temme, *Evanescence in coined
   quantum walks*, J. Phys. A: Math. Gen. **38**, 8641–8665 (2005),
   DOI 10.1088/0305-4470/38/40/011; arXiv:quant-ph/0506048.
4. Y. Baryshnikov, W. Brady, A. Bressler, R. Pemantle,
   *Two-dimensional Quantum Random Walk*, J. Stat. Phys. **142**, 78–107
   (2011), DOI 10.1007/s10955-010-0098-2; arXiv:0810.5495.
5. R. Pemantle, M. C. Wilson, S. Melczer, *Analytic Combinatorics in
   Several Variables*, 2nd ed., Cambridge University Press (2024),
   DOI 10.1017/9781108874144.
6. G. M. D'Ariano, P. Perinotti, *Derivation of the Dirac equation from
   principles of information processing*, Phys. Rev. A **90**, 062106
   (2014).
7. A. Bisio, G. M. D'Ariano, P. Perinotti, A. Tosini, *Free quantum
   field theory from quantum cellular automata*, Phys. Rev. A **93**,
   062334 (2016), arXiv:1601.04832.
8. G. M. D'Ariano, M. Erba, P. Perinotti, *Isotropic quantum walks on
   lattices and the Weyl equation*, Phys. Rev. A **96**, 062101 (2017).
9. I. Bialynicki-Birula, *Weyl, Dirac, and Maxwell equations on a lattice
   as unitary cellular automata*, Phys. Rev. D **49**, 6920 (1994).
10. Repository `nacho09021973/qca-causal-cones`, branch
    `research/b-infinity-post-s4-gate`, `state/CURRENT_STATE.md`
    Secs. 8.4 and 8.16–8.20, and the reports cited there.
