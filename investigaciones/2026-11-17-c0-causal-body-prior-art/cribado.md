# Screening of forward citations by abstract — 2026-11-17

User «filtralos». Screener: Claude (claude-opus-5-5). Input: the 103 arXiv
abstracts in `resumenes_citas.md` (literal, fetched by
`scripts/prior_art_fetch_abstracts.py`) of the forward citations listed in
`citas_hacia_adelante.csv` (`scripts/prior_art_forward_citations.py`,
OpenAlex). The 61 citing works without arXiv were not screened.

Target (restricted claim, `CURRENT_STATE.md` Sec. 4 table): an s>2 walk,
isotropic in the sense of 1708.00826, on a fixed step set without on-site
term, with continuously variable low-energy speed — or any statement that
the s=2 isotropic rigidity does or does not extend to s>2.

Method: all 103 titles read; abstracts read in full for the 24 below
(title-selected plus every abstract matching isotrop / speed of light /
propagation speed / coin or internal dimension / larger dimension / s=4 /
tunable / plastic / velocity). This is an AI screening by abstract only:
a paper whose abstract does not mention the target can still contain it.
Classifications are judgements, not results.

## Result

No abstract states the target claim or its negation. Classified RELATED
(same objects, different statement), most relevant first:

| arXiv | Why related | Read in full? |
| --- | --- | --- |
| 1511.03992 Virtually Abelian QWs | reduces non-Abelian Cayley-graph walks to Abelian ones with larger coin dimension (planar examples) — a route to s>2 walks from symmetry | proposed |
| 2112.11828 QW, limits and transport (thesis) | plastic QWs with tunable speed in 1D and 2D, triangular lattices | proposed |
| 2007.01425 Plasticity in 2D+1 | necessary and sufficient conditions for plastic (tunable-speed) DTQW in 2D, general 4-parameter coins | proposed |
| 1711.04662 Curved spacetime: discrete metric | 1+1 massless scalar transport with tunable speeds, all such QWs characterised | optional (1D) |
| 1902.10227 Chirality without coin | regrouping isotropic scalar QWs; no s=2 QW from isotropic scalar QW | optional |
| 2609.14749 Coincube (2026) | 3D Weyl node with isotropic leading cone in a probabilistic CA; different setting | no |
| 2304.14687 Massless interacting FCA | interactions invariant under the Weyl-automaton isotropy group | no |
| 1407.6928 QCA theory of light | s=4 tensor product of Weyl QCAs (Maxwell); speed inherited from s=2 | no |
| 1603.07666 One-dimensional coin | scalar QWs trivial on infinite Abelian groups | no |
| 1705.08552, 2011.09881, 1707.08455, 1601.04832, 1608.02004, 1703.05890, 1701.06309 | uniqueness of the s=2 isotropic Weyl walk restated or used; s=4 only as Dirac/Maxwell block couplings (1701.06309 read in original) | already covered |
| 2010.09104, 2011.05597, 2006.08927, 2503.05998, 2506.20136 | multiparticle QCA / phenomenology of the standard walks | no |
| 2408.04493, 2501.05349, 2407.12652, 2511.23398 | classification/renormalisation of qubit or fermionic CA (cells, not coin-isotropy speed) | no |

All other titles (curved-spacetime walks, gauge fields, circuits,
foundations, causal sets, unrelated physics) were judged not relevant from
title and, where matched, abstract.

## Next step proposed

Read in full 1511.03992, 2112.11828 and 2007.01425, checking for an
isotropic (Definition 1 of 1708.00826) walk with s>2 and adjustable speed.
Then the 61 non-arXiv works (titles only so far), and the AF regrouping
check. NOVELTY = OPEN.

## Full-text reading of the three proposed papers — 2026-11-17

User «autorizado». Read from `biblioteca/citas-s4-2026-11-17/` (pdftotext).

- **1511.03992v3** (D'Ariano, Erba, Perinotti, Tosini, Virtually Abelian
  QWs), read in full. Isotropy defined as in 1306.1934 (Sec. III, Eq. (4)),
  classified by imposing sum_g A_g = I_s and then left-multiplying by a
  unitary commuting with U (Eq. (5) and text). Examples: two planar
  virtually Abelian groups, s=2 on the original graph; coarse-graining to
  Z^2 with larger coin (4 and 2 cosets). Example A is massive
  (mass sqrt(1-nu^2)); example B is "equivalent, up to shifts in
  wave-vectors, to the Weyl QW one" (p.7). No isotropic s>2 walk on an
  Abelian group with adjustable massless speed. RELATED, not SAME.
  Side remark: their classification route (sum = I, then a commuting
  unitary) is consistent with the s=4 family, whose sum is W ≠ I with W
  commuting with U_l.
- **2007.01425** (plasticity in 2D+1), searched in full text: coins are
  2x2 unitaries (Theorem 1, Eq. (6)); speeds come from epsilon-dependent
  coin angles in continuum-limit families; the word "isotrop" does not
  occur. RELATED (tunable speed, s=2, no isotropy in the DEP sense).
- **2112.11828** (thesis, 87 pp.), searched in full text: plastic QWs in
  1D/2D/triangulations; isotropy mentioned only generically ("replaced by
  the invariance under the action of a finite group of rotations", p.3);
  speed/velocity fields set by epsilon-dependent coins; no isotropic s>2
  walk with adjustable speed located. RELATED. Not read line by line.

Outcome of this step: the restricted claim was not found in these three
papers. Remaining: the 61 non-arXiv works (titles only), the AF
regrouping check, a human expert. NOVELTY = OPEN.
