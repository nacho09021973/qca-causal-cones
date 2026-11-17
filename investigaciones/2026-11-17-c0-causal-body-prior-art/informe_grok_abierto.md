<!-- AI output, not verified primary evidence. Model usage: grok-4.7-build; requested grok-4.7. Raw stream retained. -->

The infrared coefficient, the group velocity, and the exact-support speed are different quantities. Sources below were read in arXiv HTML excerpts, not in full.

## 1. Emergent speed and the microscopic cone

**SAME.** G. M. D’Ariano and P. Perinotti, “Derivation of the Dirac equation from principles of information processing,” Phys. Rev. A 90, 062106 (2014), arXiv:1306.1934. Not read in full.

The homogeneous, local, isotropic, unitary automata are built on Cayley graphs: the line, the square lattice, and the body-centred cubic lattice. Section VII sets the infrared speed to \(c=a/(\sqrt{d}\,t_P)\) and compares it with the word-metric cone, one generator per time step:

> “the speed of light \(c\) is slower than the causal speed—i.e. one site per Planck time—by a factor \(\sqrt{3}\).”

The same paragraph says the factor is \(\sqrt{d}\) for \(d=1,2,3\). In \(d=1\) the massless dispersion is exactly linear, equation (53),

> “The dispersion relation is simply \(\omega^{A^{(1)}}_k=k\).”

So the infrared coefficient, the group velocity, and the exact-support speed coincide and the neighbourhood bound is attained. In \(d=2\) the exact-support boundary is strictly outside the infrared propagation: Figure 3,

> “the causal velocity, which is \(\sqrt{2}\) times larger than the propagation speed.”

Higher-than-\(c\) propagation remains inside \(\sqrt{d}\,c\), with negligible probability on that outer boundary. The infrared bound is therefore attained in one dimension and strict in two and three for these isotropic automata.

**SAME.** C. Cedzich, A. Joye, A. H. Werner, and R. F. Werner, “Exponential tail estimates for quantum lattice dynamics,” Ann. Henri Poincaré (2025), doi:10.1007/s00023-025-01598-4, arXiv:2408.02108. Not read in full.

Section 2: a walk of jump length \(L\) has symbol a trigonometric polynomial of degree at most \(L\), and

> “an initially localized state \(\rho\) is strictly localized in a ball of radius \(tL\).”

Lemma 4.1: the large-deviation rate satisfies

> “\(I(x)=\infty\) for all \(x\) outside the convex hull of the possible jumps.”

Thus every group velocity lies in the convex hull of the step set. For Białynicki-Birula’s three-dimensional Weyl walk, Section 5.4, that hull reaches the corner jump \((1,1,1)\), of length \(\sqrt{3}\), while

> “\(\widetilde{I}(r)=0\) for \(r<1\), i.e., in the propagation region, and \(\widetilde{I}(r)=\infty\) for \(r>\sqrt{3}\).”

The group-velocity region is the ball of radius 1. The neighbourhood bound \(\sqrt{3}\) is not attained by the group velocity. The two-dimensional walk with dispersion \(\arccos(\cos p_1\cos p_2)\), the same dispersion as D’Ariano–Perinotti in lattice coordinates, has propagation region the unit disc (Figure 3), inside the convex hull of the jumps \((\pm 1,\pm 1)\).

**SPECIAL CASE.** P. Arrighi, S. Facchini, and M. Forets, “Quantum walking in curved spacetime,” arXiv:1505.07023 (no journal reference on the arXiv abstract). Not read in full.

For paired walks wired on the usual one-dimensional light-like shifts, the continuum Dirac coefficient \(B_1\) obeys

> “The constraint that the eigenvalues of \(B_1\) are \(d_{1,2}\in[-1,1]\) represents the finite speed of propagation on the lattice.”

Appendix B gets the closed interval from hermiticity and \(B^2=I\). The endpoint \(|d_i|=1\) is included in the parametrization. Coins may depend on spacetime, so translation invariance is not kept in the general theorem. The homogeneous case is the special case.

**RELATED.** L. Mlodinow and T. A. Brun, “Discrete spacetime, quantum walks and relativistic wave equations,” Phys. Rev. A 97, 042131 (2018), arXiv:1802.03910. Not read in full.

> “in the continuum limit the ratio of the lattice spacing to the time step corresponds to the speed of light”

They identify the infrared speed with \(\Delta x/\Delta t\) by the continuum scaling. That does not compare it with the convex hull of a fixed step set.

## 2. Fixed by the lattice, or walk-dependent?

**SAME — speed fixed once isotropy and minimality are imposed.** D’Ariano and Perinotti, arXiv:1306.1934, as above. Not read in full.

On \(\mathbb{Z}^3\) only one of the three Cayley graphs works. Section IV:

> “allow for a solution only on one out of three possible Cayley graphs for \(\mathbb{Z}^3\).”

That graph is body-centred cubic, coordination number 8. The square lattice, not the hexagonal lattice, is the two-dimensional solution. Within that symmetry class the automaton is unique up to chirality and transposition, and \(c=a/(\sqrt{d}\,t_P)\) is then fixed by the graph. What is held fixed is the Cayley neighbourhood, not merely the point set of the lattice.

Mass does not change this infrared coefficient. The massive group velocity, Appendix B, equation (181), is the massless group velocity times a factor at most 1. The small-wave-vector limit is still Dirac with the same \(c\). For \(m\neq 0\) the coupling \(im\,I\) is on-site, so the exact step support is \(\{-1,0,+1\}\) rather than the massless support \(\{\pm 1\}\). Same lattice, different exact causal body, same infrared coefficient.

**SAME — infrared coefficient not fixed by the shift set.** G. Di Molfetta and P. Arrighi, “A quantum walk with both a continuous-time and a continuous-spacetime limit,” arXiv:1906.04483 (no journal reference on the arXiv abstract). Not read in full.

The shift in equation (3) is the state-dependent nearest-neighbour shift and does not depend on \(c\). The coin does. Section II:

> “Later \(c\in[0,1]\) will be interpreted as a speed of propagation or a hopping rate.”

For the continuum scaling \(\alpha=0\), the limit is the Dirac equation at that \(c\),

> “\(i\partial_t\Psi=(c\sigma_x\partial_x-m\sigma_z)\Psi\).”

Same lattice \(\mathbb{Z}\) and the same shift. For every \(c\in(0,1)\) the coin has both diagonal and off-diagonal entries, so one double step has nonzero displacements \(\{-2,0,+2\}\): the exact causal body stays the same while \(c\) changes. At \(c=1\) the coin is diagonal, the stay channel closes, and the infrared speed meets the double-step support speed. The paper does not itself discuss that support; it is read off equations (2)–(5) and (23).

**SPECIAL CASE.** T. C. Farrelly and A. J. Short, “Discrete spacetime and relativistic quantum particles,” Phys. Rev. A 89, 062109 (2014), arXiv:1312.2852. Not read in full.

Before any rescaling, equation (9) and the singular-value step give continuum coefficients \(\gamma_i\) that depend on the transition matrices \(A_{\vec{q}}\). Then

> “If all the \(\gamma_i\) are non-zero, we can rescale the spatial axes so that \(\gamma_i P'_i\to P'_i\).”

Different walks can have different \(\gamma_i\) in lattice units. After one rescaling they all become the same Weyl equation. They do not exhibit two numerical coins on one common step set. The neighbourhood is part of the data: the axis-neighbour cubic graph is excluded,

> “the cubic neighbourhood, cannot give the three dimensional Weyl equation in the continuum limit,”

while the product of three conditional shifts

> “essentially uses a body centred cubic neighbourhood.”

**RELATED.** I. Białynicki-Birula, “Weyl, Dirac, and Maxwell equations on a lattice as unitary cellular automata,” Phys. Rev. D 49, 6920 (1994), arXiv:hep-th/9304070. Abstract only; not read in full.

> “Every local and unitary automaton on a cubic lattice, under some natural assumptions, leads in the continuum limit to the Weyl equation.”

This fixes the continuum equation up to coordinates, not a lattice-unit speed on a named step set.

## 3. Group velocity, ballistic region, exact support

These are nested, not equal.

- Exact support: finite jump length \(L\) gives support in the ball of radius \(tL\), by the wiring or by Paley–Wiener. Cedzich, Joye, Werner, and Werner, Section 2, quote in Section 1. Outside the convex hull of the jumps the rate is infinite (Lemma 4.1).
- Ballistic region: \(Q(t)/t\) converges to the group-velocity law. The propagation region \(\Gamma\) is the closure of \(\{\nabla\omega_j(p)\}\). Cedzich et al., Section 2.2. Probability strictly outside \(\Gamma\) decays exponentially; near the boundary the rate vanishes like the distance to the power \(3/2\).
- Infrared coefficient: the slope of a Weyl or Dirac cone at small wave-vector. It is one point of the group-velocity map, not the maximum over the Brillouin zone, and not the jump length.

On the three-dimensional Weyl walk of Section 5.4, the group-velocity region is the ball of radius 1 and the exact-support radius is \(\sqrt{3}\). On D’Ariano–Perinotti’s massless line, equation (53), all three numbers equal 1.

**SPECIAL CASE.** A. Pérez, “Asymptotic properties of the Dirac quantum cellular automaton,” Phys. Rev. A 93, 012328 (2016), arXiv:1504.07418. Not read in full.

The one-dimensional Dirac automaton is the nearest-neighbour walk plus an on-site mass term. The group velocity is

> “\(v(p)=\sqrt{1-\beta^2}\sin(p)/\sin\lambda(p)\) is the group velocity”

and the position spread is ballistic,

> “\(\sigma(t)=t\sqrt{1-|\beta|}\), which accounts for the ballistic spreading.”

Changing \(\beta\) changes this group-velocity scale. The Dirac Hamiltonian is recovered only for \(pd/\hbar\ll 1\) and \(mdc/\hbar\ll 1\), where \(\sqrt{1-\beta^2}\simeq 1\), so the infrared coefficient does not follow \(\sqrt{1-|\beta|}\). Same lattice; for \(\beta\neq 0\) the exact step support includes the on-site term.

## 4. Inequalities used to bound the speeds

Located in the sources above:

- Paley–Wiener, applied to a trigonometric polynomial of degree at most \(L\): exact cone of radius \(tL\). Cedzich et al., Section 2.
- The Legendre transform of the logarithm of the norm of the symbol at complex momentum. Outside the convex hull of the jumps the rate is infinite (Lemma 4.1). The support function of that jump set is the comparison function in the proof.
- Hermiticity together with \(B^2=I\): the continuum coefficients lie in \([-1,1]\). Arrighi, Facchini, and Forets, Appendix B. Equality is in the parametrization.

## Not found

- A use of Bernstein’s inequality, or of Markov’s inequality, to bound these speeds.
- Two explicit isotropic automata on one and the same Cayley graph with different infrared coefficients. Under D’Ariano and Perinotti’s hypotheses the automaton on that graph is unique.
- A result in which the maximum group velocity of the two- or three-dimensional isotropic Weyl walk equals the Euclidean length of the longest jump. The sources above give radius 1 against \(\sqrt{2}\) or \(\sqrt{3}\).
- A statement by Di Molfetta and Arrighi of the exact step support as a function of \(c\). Only the shift and the coin are written down.
- Journal page numbers. Citations above use arXiv section and equation numbers.