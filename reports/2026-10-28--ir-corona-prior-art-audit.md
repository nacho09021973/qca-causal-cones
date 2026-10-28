# ir-corona: bibliographic priority audit — 2026-10-28

User instruction: "ahora la prioridad bibliográfica". This audit checks the novelty paragraph of
`papers/ir-corona/ir-corona.tex` (tag `ir-corona-v1`, §1 "Relation to the literature") against
primary sources. It changes no gate and no status. **NOVELTY remains OPEN**: a search that finds
nothing proves only that this search found nothing.

## The claim audited

> To our knowledge, Theorem 4.3 is the first prefactor-level asymptotic, with a leading
> coefficient that is oscillatory and certified to be non-vanishing, for an infrared-controlled
> operational response in the strictly outside-propagation-region regime of a three-dimensional
> multi-component quantum walk.

It has four components: (a) prefactor-level asymptotics, (b) outside the propagation region,
(c) dimension three, multi-component, (d) an operational, infrared-controlled response with a
certified non-vanishing coefficient. The paper already concedes prior art for exponential decay
outside the region, large-deviation rates, Weyl-cone dispersion and microscopic support outside
an emergent cone.

## Method

- Library index first (`biblioteca/INDICE.md`): only CJWW was present. Three cited sources were
  downloaded from arXiv into `biblioteca/` and registered in
  `scripts/biblioteca_catalog/curated.csv` with a new tag `asintotica-qw`:
  `arXiv-1108.1878.pdf` (SHA-256 prefix `d383bb8dce6cbb11`), `arXiv-quant-ph_0506048.pdf`
  (`2a28da0f18ccadb2`), `arXiv-0810.5495.pdf` (`2b7d76054c83fd7e`).
- Searches: web search and the alphaXiv index (queries in English on outside-region / hidden-region
  / large-deviation asymptotics of 2D and 3D quantum walks, ACSV quantum walks, signalling
  outside emergent light cones in QW/QCA, and works citing CJWW). The summaries returned by those
  tools are AI-generated and were used only to locate papers. Every statement below marked as read
  was checked in the PDF.
- No text was sent to a reviewing model. No `investigacion-gemini` run.

## Primary sources read

| Source | What it establishes | Where read |
|---|---|---|
| CJWW, arXiv:2408.02108v1 (the only arXiv version; AHP 27(8):2843–2870, 2026, online 2025-06-23 per Crossref) | Upper bounds on the rate outside the propagation region, uniform in the initial state. "Typically, in that theory one also shows lower bounds, but since these would be state dependent, we do not consider them here." "To our best knowledge, only two studies [8, 23] have been made of the asymptotics outside of the propagation region … this also gives the prefactors." [8] = Carteret–Richmond–Temme, [23] = Sunada–Tate, both on the line. | `biblioteca/EXPONENTIAL_TAIL_ESTIMATES_FOR_QUANTUM_LATTICE_DYNAMICS.pdf` p.3 (lower bounds), p.13 (§5.1, the two studies) |
| Sunada–Tate, arXiv:1108.1878 | 1D two-state walks. In the "hidden" region \|a\|<\|ξ\|<1, Thm 1.4 gives p_n = (1+(−1)^{n+y})\|b\|/(πn(1−ξ²)√(ξ²−\|a\|²)) e^{−nH_Q(ξ)} (G(ξ)+O(1/n)), with G smooth and non-negative and H_Q explicit. | `arXiv-1108.1878.pdf` p.1 (abstract), p.4 (Thm 1.4, Cor. 1.5) |
| Carteret–Richmond–Temme, quant-ph/0506048 | 1D: uniformly convergent asymptotics for the exponential-decay regions at the leading edges of the peaks. | `arXiv-quant-ph_0506048.pdf` p.1 (abstract) |
| BBBP, arXiv:0810.5495v4 | 2D: feasible region and profile inside it; probabilities exponentially small outside. "Explicit formulae for probability amplitudes at specific points inside and outside of the feasible set may be obtained; however, these details differ greatly from one instance to another." "No family of QRW in dimension three or higher has been analyzed to date, for example, but such an undertaking should be a modest extension of the present work." | `arXiv-0810.5495.pdf` p.1 (abstract), p.2 (inside/outside), p.4 (dimension three) |

Also scanned, not anticipating: Kuklinski–Kon, arXiv:1905.00057 (2D walks; boundaries of the
regions of *polynomial* decay, not outside-region prefactors; abstract and introduction).
D'Ariano–Mosco–Perinotti–Tosini, arXiv:1705.08552 (3+1 Weyl walk on a Cayley graph of Z³) and
arXiv:1410.6032 (2+1): exact path-sum solutions; the text contains no asymptotic analysis outside
the light cone (full-text search for asymptotic / outside / decay / saddle / stationary phase).

## Findings

1. **The paper's statements about cited prior art are accurate** (CJWW, Sunada–Tate, CRT, BBBP).
   The CJWW bibitem matches Crossref (volume 27, issue 8, pages 2843–2870, 2026).
2. **Components (a)+(b) in dimension ≥ 2.** The most specific statement found is CJWW's own: as of
   v1 (August 2024), only two outside-region asymptotic studies, both 1D. CJWW also explicitly
   leaves out lower bounds. No later work giving outside-region prefactors in d ≥ 2 was found.
3. **Component (c).** BBBP (2010) state that no QRW family in dimension ≥ 3 had been analysed and
   call it "a modest extension". They also say that outside-region formulae "may be obtained" by
   their method. The paper's sentence "We do not claim that these methods cannot reproduce the
   present result" is therefore the right posture. Priority rests on the result having been
   carried out, not on the method being unavailable.
4. **Component (d)** (operational distinguishability under an infrared-admissible encoding,
   certified non-vanishing coefficient): no prior treatment found. The searches on signalling
   outside emergent cones in QW/QCA returned only general light-cone, Lieb–Robinson and
   Lorentz-symmetry material.

## Not verified

- Andrew Bressler's PhD thesis (Penn, 2009, advisor Pemantle) has a section titled "QRWs on Z^d
  for d > 2" whose content could not be read. The server refused the download (HTTP 403), and a
  workaround was not attempted. Its date precedes BBBP v4 (2010), which still says no
  d ≥ 3 family had been analysed. **[UNVERIFIED]**
- The quantum-walk material of the ACSV book (Pemantle–Wilson–Melczer, 2nd ed., 2024), which is
  not available locally. **[UNVERIFIED]**
- T. Tate, "Quantum walks in low dimension" (Geometric Methods in Physics, 2016). Its abstract, as
  reported by search, has large-deviation asymptotics from the 1D formula and an nth-power formula
  for the 2D Grover walk. The chapter was not read. **[UNVERIFIED]**
- Whether the published AHP version of CJWW keeps the "only two studies" sentence. Only arXiv v1
  exists, and the journal page needs authentication. **[UNVERIFIED]**
- Citation search of CJWW for 2025–2026 follow-ups was attempted. No citing list was obtained.

## Assessment

No anticipating result was found. The novelty paragraph is consistent with the sources read and
is already narrow. Optional text improvements, applied on 2026-10-28 at the user's request
("si"), in `.tex` and `.md`, with two new bibitems (DMPT15, DMPT17):

1. Support "the closest precursors" with CJWW's own statement (p.13) that the only
   outside-region asymptotics are the two 1D studies, and with its remark that lower bounds are
   not considered (p.3).
2. Mention BBBP's remark (p.2) that outside-region formulae can be obtained by their method in
   specific instances. This strengthens the existing disclaimer.
3. Optionally cite the exact path-sum solutions of the 3+1 Weyl walk (arXiv:1705.08552) as
   related exact work without asymptotics outside the cone.

Status: `PRIOR_ART_AUDIT: NO_ANTICIPATION_FOUND / NOVELTY OPEN`. The four `[UNVERIFIED]` items
should be closed, or acknowledged, before submission. The Bressler thesis is the most relevant of
them.
