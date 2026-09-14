# Massless rigidity: primary-source and class-definition audit

Date: 2026-09-14. Focus: spatial dimension d=3.
Repository baseline: `a6d24cfcb6fd59d362b1c76bbf125781faad3b3d`.

**Scope: source audit only; no executable class contract, calculation,
solver, counterexample or status promotion.**
[CURRENT_STATE](../state/CURRENT_STATE.md) remains authoritative. The
[rigidity charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) remains OPEN.

## 1. Sources actually checked

The original derivation is not the last classification statement. A later
Pavia paper must be included before assessing coverage or novelty.

| ID | Primary source | Reading coordinates |
| --- | --- | --- |
| P14 | G. M. D'Ariano and P. Perinotti, *Derivation of the Dirac equation from principles of information processing*, Phys. Rev. A **90**, 062106 (2014), [DOI](https://doi.org/10.1103/PhysRevA.90.062106), [arXiv v2](https://arxiv.org/abs/1306.1934v2) | Published PDF, 18 pages; Secs. II-IV, VII and Appendix A |
| P17 | G. M. D'Ariano, M. Erba and P. Perinotti, *Isotropic quantum walks on lattices and the Weyl equation*, Phys. Rev. A **96**, 062101 (2017), [DOI](https://doi.org/10.1103/PhysRevA.96.062101), [arXiv v2](https://arxiv.org/abs/1708.00826v2) | Published PDF, 14 pages; Definition 1, Eq. (2), Propositions 1-5, Appendix 4 |
| R17 | P. Raynal, *Simple derivation of the Weyl and Dirac quantum cellular automata*, Phys. Rev. A **95**, 062344 (2017), [DOI](https://doi.org/10.1103/PhysRevA.95.062344), [arXiv v2](https://arxiv.org/abs/1703.05890v2) | arXiv v2 PDF, 10 pages; Secs. II, III.E-F, IV |

P14/P17 page numbers below are the published page suffixes, not arXiv
pagination. R17 page numbers refer to its arXiv PDF. This is an audit of
definitions, theorem statements and their application boundaries, not an
independent reconstruction of every classification proof.

### Source-byte provenance

Retrieved and inspected on the audit date. PDFs were read outside the repo;
only this report is added. The URLs and hashes identify the inspected bytes,
not a claim that the journal and arXiv versions are byte-identical.

| ID | Inspected PDF | Bytes | SHA256 |
| --- | --- | ---: | --- |
| P14 | [Author-hosted published PDF](https://wordpress.qubit.it/wp-content/uploads/publications-dariano/1306.1934.pdf) | 1674024 | `bc0e1b4dab0c20abbd85a72e6efa0cc67ce71e23a016e8c5798d3ab88e2d7fe6` |
| P17 | [Author-hosted published PDF](https://wordpress.qubit.it/wp-content/uploads/publications-dariano/PhysRevA.96.062101.pdf) | 435784 | `a649bbc31740ac37ee6456aae43af839216c8b941f2446446ce34f77a7690b97` |
| R17 | [Versioned arXiv PDF](https://arxiv.org/pdf/1703.05890v2) | 903103 | `342427941a466d2ec9302d5d595e7f433ce7c497fdbaef56b5818acf38c5fb4f` |

Inspection used `pdfinfo`, `pdftotext -layout`, a rendered check of P17 p. 2,
and `sha256sum`. No scientific script or new numerical result was produced.

## 2. Published assumptions versus published consequences

### P14: original minimal construction

**Assumptions/reductions:** linear unitary evolution; finite, reciprocal
neighborhood; homogeneity; connected Cayley graph; discrete covariance with
a faithful internal representation, transitive on S+ (Sec. II, pp. 2-3,
Eq. (5)). Euclidean embedding and the Abelian restriction precede the
Bravais-lattice analysis. Internal dimension s=2 is selected as minimal
nontrivial, not derived for arbitrary internal spaces (p. 4).

**Consequences:** within that reduction, BCC survives; four representatives
modulo unitary conjugation form transpose-related pairs (Sec. IV, p. 4).
The chosen BCC generators have unit length, Eq. (20). The expansion about
k=0 has Weyl coefficient 1/sqrt(d), Sec. VII, p. 7, Eq. (60).

**Normalization/equivalences:** Eqs. (18)-(19) remove A(0) by left
multiplication; the commutant restores that freedom. Momentum shifts also
relate transpose representatives, with phases (p. 5, after Eq. (33)).

The connected-graph reduction concerns spatial copies; it is not an
assumption of internal spinor irreducibility. The physical coordinate
choice must not be confused with a classification of embedded metrics.

### P17: later complete minimal classification

| Published assumptions | Locator |
| --- | --- |
| Linear QW on l²(Z^d) tensor C²; finite generating set; d=1,2,3 | Secs. II-III, pp. 1-3 |
| S=S+ union S- union {e}; S-=S+ inverse; every nonidentity coefficient nonzero; on-site term allowed | p. 2 |
| Color-automorphism covariance; projective unitary representation; transitivity on S+ for Z^d | Definition 1, p. 2 |
| Distinguishability: [U_l,A_h] != 0 whenever l(h) != h | Eq. (2), p. 2 |

| Published consequences | Locator |
| --- | --- |
| Finite isotropy subgroup of Aut(Z^d); generating-set orbit construction | Propositions 1-2; Sec. IV |
| Rank-one transitions in the classified s=2 setting | Sec. V, Eqs. (12)-(13) |
| d=3: BCC; tetrahedral S+; projective Pauli image {I,i sigma_X,i sigma_Y,i sigma_Z} | Proposition 4; Fig. 1(c), p. 5 |
| d=3: A_e=0; two Weyl normal forms modulo stated equivalences | Sec. V(c); Proposition 5, pp. 6-7 |

P17 removes P14's nearest-neighbor empty-sphere technical assumption
(P17 introduction, p. 1). This retrospective identification is attributed to
P17, not presented as a quotation located in P14.

Its Eq. (2) supplements homogeneity; footnote 1 points to unpublished
reference [23]. No published derivation of that supplement from ordinary
translation invariance is certified here.

### R17: useful independent comparison, not identical hypotheses

R17 fixes the d=3 BCC geometry and s=2 from the outset (Sec. II, p. 2).
Its Eq. (15), p. 4, imposes A(0)=I after discussing Schur's lemma.
Internal representation irreducibility is explicitly recalled as an
assumption at the end of Sec. III.E, p. 8. The specific rotation group is
identified afterwards, not prescribed initially. An on-site coefficient is
allowed before the derivation, rather than set to zero initially.

Its tetrahedral vectors are unnormalized (Eq. (17), p. 4); its coefficient
in Eq. (68), p. 8, is therefore not directly comparable to the repo's
unit-neighbor convention. Its s=4 discussion explicitly uses a restricted
form (Sec. IV, p. 8), not an exhaustive enlarged-coin classification.

**Do not transfer R17's explicit irreducibility assumption into P17's
Proposition 5. They are different derivations.**

## 3. Application boundaries: our interpretation and required choices

These are audit conclusions for this repository, not additional published
theorem statements and not a frozen adversarial contract.

### Internal dimension, irreducibility and coverage

- Choosing s=2 would place our first case in the published minimal class;
  allowing arbitrary finite s would not. Minimality is a restriction on the
  quantified class, not a consequence of our general causal-body question.
- P17 does not impose internal irreducibility as a separate global premise
  of Proposition 5. Its d=3 Pauli image has no common invariant line; that
  is an implication of the resulting representation. This must be kept
  distinct from irreducibility of the spatial representations used in its
  appendix and from irreducibility of an arbitrary QW coefficient algebra.
- A two-dimensional coin and a chosen two-band node leave no extra internal
  spectator block. A sector inside a larger coin would require its own
  support and reducibility contract; these sources do not classify it.
- P17 claims coefficient-class coverage through graph exclusions and
  unitarity constraints, rather than completeness of a chosen product-coin
  ansatz. A new restricted ansatz would not improve that coverage.

### Group/action and representation

For the standard BCC realization, distinguish the four-element spatial
group of coordinate-axis half-turns, D2 isomorphic to Z2 x Z2, from its
projective internal representatives. The Pauli matrices listed above are
not a four-element ordinary subgroup of SU(2): multiplication involves
phases. Faithfulness must be interpreted for the effective projective
action, not inferred merely from a list of distinct matrices.

Transitivity concerns the four positive generators, not a requirement of
covariance under every rotation of the cube or of transitivity on all eight
neighbors. Fixing the full cubic group instead would change the question.
Fixing an internal representation in our contract would select a
representative of the classification outcome; it was not P17's starting
choice.

Most importantly, the charter's translation-invariant symbol and covariance
equations do not explicitly include P17 Eq. (2). Before invoking P17, we
must either require that condition or establish its implication from our
eventual contract. Simply writing "homogeneity" does not perform this check.
Conversely, omission of the condition is not evidence that a counterexample
exists.

### Geometry and equivalences

Our fixed Euclidean embedding and update interval are indispensable extra
comparison data. Graph equivalence, or an invertible change of lattice
coordinates used to classify a presentation, does not preserve the
numerical inradius in an independently fixed physical metric.

Keep constant basis conjugation separate from left multiplication by a
uniform local unitary. The latter need not preserve eigenphases. In the
irreducible d=3 Pauli case its allowed commutant is scalar, so only a
quasienergy-origin phase remains. Schur's lemma alone gives scalar V, not
literally V=I without fixing that phase.

The eventual contract must list which generator relabelings, transposes,
chirality labels and momentum/node shifts it identifies, and transport the
symmetry representation consistently. P14's four representatives and
P17's two normal forms use different equivalence bookkeeping; their counts
are not independent geometrical evidence. This audit does not supply a
complete representative-by-representative dictionary.

### Node and sector

Use A(k) for the Bloch symbol and A_e for the on-site coefficient: A(0)=I
and A_e=0 are different statements. The former is a normalized representative
choice in the classification; the latter is a d=3 result.

Our first application would still have to declare the origin node,
quasienergy origin, logarithm branch and whole two-band sector. P14's
origin expansion is not an exhaustive certificate about every node in the
Brillouin zone. Moving the selected node requires an explicit mapping;
it must not be silently treated as the same fixed-node problem. The
positive Fourier exponent in the sources also needs translation into the
repo's negative-exponent convention before comparing chirality labels.

## 4. Answer and claim ceiling

**The minimal d=3 symbol classification is already published.** A search
wholly inside P17's actual class, with its distinguishability condition and
normalization/equivalences respected, is not a new open coefficient search.
This does not make the repository's unspecified broader class classified.

**Conditional application, not a new theorem:** combining that published
classification with the existing
[standard-family certificate](2026-09-14--weyl-dirac-exact-gate.md) would
give origin-node inradius matching for the fully matched minimal class
in our fixed unit-neighbor BCC embedding. The speed/inradius equality is
our application of existing ingredients, not a theorem stated in P17 in
causal-body language. No new rigidity or novelty status is assigned here.

Before freezing a contract, the remaining decision is therefore precise:
are we testing that already classified minimal class, including Eq. (2),
or a genuinely broader class with a documented hypothesis difference?
No broader class is selected or authorized by this report. In particular,
there is no inference about arbitrary s, every gapless sector, general
massless QCA, general Dirac couplings, or inter-species universality A.

**Disposition:** primary-class audit recorded; class contract pending.
No solver run, no new model, no computation of c_0 or r_in, and no changes
to canonical state or historical evidence.
