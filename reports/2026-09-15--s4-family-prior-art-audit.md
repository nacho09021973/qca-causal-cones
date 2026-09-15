# S4 family: targeted prior-art audit

**Date:** 2026-09-15

**Family:** `1dae941e8df7f20203aacba9d5fa8f8ad9692bac`.

**Independent review committed:** `aeec462` on
`research/s4-strict-cone-counterexample`.

**Result:** no equivalent realization of the complete declared family was
identified in the inspected sources. **NOVELTY = OPEN**, not a novelty
certificate. Mathematical correctness and canonical state are unchanged.

## 1. What this audit can decide

The target is the conjunction of: four internal components; all eight
normalized BCC displacements and no on-site Fourier coefficient; fixed D2
covariance with `R_i=sigma_i tensor I_2`; irreducible dynamics; separated
rank-two Floquet Weyl clusters; continuously adjustable isotropic slope;
and the same certified strict asymptotic support body.

An older work need not use our terminology to anticipate this result.
A published broader construction may contain the family even if its authors
did not formulate the strict-cone comparison. Conversely, one shared
ingredient does not establish equivalence of the complete construction.

The audit distinguishes:

- **Direct exclusion:** a preserved property contradicts identification with
  the specific published symbol.
- **Structural antecedent:** an existing construction supplies the circuit
  template or mechanism, but a complete identification has not been checked.
- **Related result:** establishes context without supplying the target.

Direct comparisons preserve one complete update, the Euclidean embedding,
internal dimension and active Fourier support. Constant unitary conjugation,
global phase, orthogonal lattice relabeling and momentum-node relabeling are
admissible if the symmetry representation is transported consistently.
Left multiplication by a non-scalar coin is a new dynamics, not a change of
basis. Cell regrouping, changed time steps, and momentum-dependent basis
changes require separate support and representation checks. A claim about
the full class of such transformations is not supplied here.

No new model algebra, numerical search, equivalence solver or generalization
of the sum rule was run. Comparisons below use published equations and the
already reviewed properties of our family.

## 2. Most relevant comparisons

### R17 — Raynal: direct published Dirac family excluded

Read Sec. IV, PDF pp. 8–9, especially Eqs. (75)–(77), in
[Raynal, arXiv:1703.05890v2](https://arxiv.org/html/1703.05890v2#S4).
His symbol couples a Weyl walk and its adjoint with the constant block
`i sqrt(1-s^2) I_2`. For `0<s<1` this is a nonzero on-site coefficient.
At `s=1` the symbol is block diagonal; at `s=0` it has no spatial hopping.
Its eigenvalues remain twofold degenerate at every momentum.

**Audit inference:** none of these cases is our irreducible, no-on-site
family with linearly splitting Weyl doublets. Support and reducibility
already exclude a constant-basis identification; the spectral multiplicity
also obstructs an isospectral identification. This excludes those explicit
families, not every possible s=4 construction or modification of Raynal.

### BB94 — Bialynicki-Birula: a closer ancestor than the on-site Dirac walk

Read Secs. II–III and V, especially printed p. 6924, Eqs. (38)–(41), in
[Bialynicki-Birula, Phys. Rev. D 49, 6920](https://doi.org/10.1103/PhysRevD.49.6920).
Equation (40) mixes two opposite-helicity coefficient blocks by a uniform
two-by-two rotation. Equation (39) still sums over the spatial neighbors:
the local coin rotation is not an on-site Fourier displacement.

**Audit inference:** enlarging two Weyl components to four and applying a
uniform mixing rotation is prior art. The on-site obstruction used for R17
must not be transferred to BB94. The paper gives a Dirac continuum limit;
this review has not certified a global inequivalence after arbitrary node
or Floquet-frame changes. It is a structural antecedent requiring an
explicit comparison in any publication.

### MB18 — Mlodinow–Brun: the product-of-projectors architecture is prior art

Read PDF pp. 5–6, Eqs. (22)–(25), in
[Mlodinow and Brun, arXiv:1802.03910v1](https://arxiv.org/abs/1802.03910v1).
Their BCC construction uses three directional conditional shifts and a
uniform coin. They explicitly collect intermediate coins into a single
coin by redefining projectors. The subsequent equal-norm requirement
enforces additional relations between the directional projectors.

**Audit inference:** the product architecture and moving coins between
factors cannot be claimed as new. Their restricted relativistic model uses
stronger internal conditions than the frozen D2 covariance alone. This
distinction does not prove that their broad construction excludes our
family; inclusion or equivalence of a specialization remains unresolved.

### BM25 — Brun–Mlodinow: explicit extra assumptions behind the Clifford choice

Read Secs. 2–3, PDF pp. 4–5, Eqs. (3), (5)–(7), in
[Brun and Mlodinow, arXiv:2503.05998v2](https://arxiv.org/html/2503.05998v2).
The fermion update has precisely the three-shift-plus-coin template.
They require the coin generator to exchange forward/backward projectors;
the equal-norm condition yields mutually anticommuting directional
generators, identified with Dirac matrices.

**Audit inference:** these conditions must be named when comparing their
velocity selection with ours. Our reviewed within-doublet generators are
nonzero, `P_+ Gamma_i P_+=a sigma_i P_+`; simply identifying their parity
coin eigenspaces with our two clusters would not reproduce that property.
This is a restriction on that identification, not an exhaustive theorem
about alternative factorizations or node choices.

### AF16/17 — Arrighi–Facchini: the strongest overlap with the proposed mechanism

Read Sec. III.E, PDF pp. 4–5, Eqs. (27)–(34), and Sec. IV in
[Arrighi and Facchini, arXiv:1609.00305v2](https://arxiv.org/html/1609.00305v2).
Their paired walks encode fields into a larger space. Compressing a
Hermitian involution gives an effective velocity matrix with eigenvalues
in `[-1,1]`; Eq. (27) is

\[
B_1^2+B_2^\dagger B_2=I_{2s}.
\]

They construct the complementary block and extend the method to multiple
spatial directions. Their symbol `s` is not our internal-dimension label.

**Audit inference:** adjustable effective speed from compression, with a
complementary square completing an involution, is already present. This
limits a broad novelty claim about a causal budget. It does not identify
their complete walk with our BCC family or establish our weighted
projector-metric formula. Grouping, encoding, full support, D2 action and
constant-basis irreducibility must be compared before deciding that question.

## 3. Floquet alternatives and background controls

| Source and checked location | What was found and comparison ceiling |
| --- | --- |
| [Wang–Zhou–Chong, arXiv:1512.00111v2](https://arxiv.org/html/1512.00111v2), Sec. II, Eq. (4); Appendix A, Eqs. (A5), (A10), PDF pp. 3, 8 | A two-component unitary network with parameter-dependent Weyl linearization; extra scattering phases translate quasienergy and momentum. Its displayed `U_mu` contains both constant and directional terms. Weyl quasienergy displacement and tuning a network are prior art. The displayed two-component symbol is not our four-component family. Enlarging or regrouping it is a separate, unperformed comparison. |
| [Sun et al., arXiv:1806.09296v2](https://arxiv.org/html/1806.09296v2), PDF pp. ii–iii, Eq. (10) | A driven four-component Clifford Hamiltonian with an adiabatic low-/high-energy sector construction. It is a relevant ancestor for sector-separated Floquet Weyl physics. The checked passages do not supply a certified eight-mode one-step BCC symbol; no identification with ours was established. |
| [Higashikawa–Nakagawa–Ueda, arXiv:1806.06868v2](https://arxiv.org/abs/1806.06868v2), PDF p. 2, Eqs. (2)–(5) | Eight spin-selective pumping stages on a lattice with a third-direction sublattice. The full four-band Floquet operator is displayed as `U(k) direct-sum U^H(k)` in their Bloch description. Four Floquet bands and Weyl physics therefore do not by themselves identify our model. Whether a spatial regrouping changes the meaning of this block decomposition must be checked, rather than calling it our constant onsite commutant. |
| [D'Ariano–Erba–Perinotti, arXiv:1708.00826v2](https://arxiv.org/abs/1708.00826v2), Proposition 5, PDF p. 7 | The classification explicitly fixes coin dimension two. It remains relevant to the baseline but does not classify the enlarged family. This rechecks the coverage ceiling recorded in the earlier repository audit, without rerunning the classification proof. |
| [Farrelly–Short, arXiv:1312.2852v1](https://arxiv.org/abs/1312.2852v1), Sec. IV, PDF pp. 3–4, Eq. (19) and surrounding coordinate rescaling | Generic two-component massless limits can be put in Weyl form using suitable coordinate changes. Such rescaling does not establish speed matching in our fixed Euclidean units. A generic relativistic limit is prior art; it is not the complete fixed-BCC counterexample sought here. |
| [Cedzich–Joye–Werner–Werner, arXiv:2408.02108v1](https://arxiv.org/abs/2408.02108v1), Sec. 5.3, PDF p. 16, Eqs. (5.12)–(5.14), Fig. 5 | They explicitly distinguish small-momentum Weyl propagation from faster finite-momentum propagation for the standard product walk, in a study of ballistic limits and exponential tails. Separation of low-energy speed from other propagation velocities is prior art. Their observable is not our exact-support asymptotic body; this does not certify an equivalent s=4 family. |

## 4. Search coverage and limitations

The web search was performed on 2026-09-15, followed by reading the original
papers listed above. Bibliographic snippets were discovery aids only.
PDF versions, page counts, hashes and acquisition URLs are retained in
[the source manifest](../sources/S4_FAMILY_AUDIT_SOURCES.md).

Query families included BCC/body-centered/body-centred cubic with four
components, four-band or four-dimensional coin; Weyl with adjustable/tunable
velocity, quasienergy separation and irreducibility; Pauli multiplicity;
and named-author/title searches for the candidates identified. Concrete
queries included:

```text
quantum walk BCC four component Weyl tunable velocity Raynal
"quantum walk" "body centered cubic" coin
"quantum walk" "Weyl" "four-component"
"quantum walk" "Weyl" "four-band"
"quantum walk" "Weyl" "tunable velocity"
"quantum walk" "BCC" "irreducible" "4"
"Weyl" "BCC" "quasienergy"
"quantum cellular automata" "Pauli" "multiplicity"
"Quantum walking in curved spacetime" "3+1"
"Discrete spacetime, quantum walks and relativistic wave equations" arxiv
"Exponential Tail Estimates for Quantum Lattice Dynamics" arxiv
"Floquet chiral magnetic effect" Higashikawa Nakagawa Ueda quantum walk
```

Reference following connected Raynal to the earlier BCC work and paired
walks, the 2025 paper to MB18, and Sun et al.'s note added to Higashikawa
et al. This is a targeted audit of eleven primary papers, not an exhaustive
forward-citation census, database-export search or classification of all
four-state walks. No negative search result is treated as a proof of absence.
Publication dates and version dates come from the papers/arXiv records,
not search-engine crawl dates or automatically regenerated HTML dates.

## 5. Claim ceiling after this audit

The direct Raynal identification is excluded, and no full match was found
in the checked corpus. The exact family and its strict-support theorem
remain a **candidate specific contribution**. The following broader
ingredients must be attributed to antecedents rather than advertised as new:
product walks, four-component Weyl mixing, shifted Floquet Weyl nodes,
adjustable continuum velocity, involution block completion, and the
distinction between low-energy and other propagation velocities.

The single most useful next equivalence target is **AF16/17's homogeneous
paired-walk specialization**: compare the complete encoded update with
the frozen family, including the physical cell, internal representation,
full Fourier support, sector origins and strict-support statement. MB18
and BB94 supply the circuit ancestry against which that comparison must
be interpreted. No new algebra on these targets is undertaken in this audit.

No claim of first discovery, comprehensive inequivalence, universal causal
budget or closed bibliographic novelty gate is warranted. The independent
mathematical PASS is unaffected.
