# Sources

Primary sources currently relevant to the freeze.

## Joint Yukawa flow — acquired 2026-11-06

Fei et al., *Yukawa conformal field theories and emergent supersymmetry*,
PTEP 2016, 12C105. Original PDF from
https://inspirehep.net/files/ffbb5687cb89ebffbb5cffb7e40dcb64,
stored as `fei_giombi_klebanov_tarnopolsky_2016_yukawa.pdf`.
SHA256 `83cdf266ca7c6c03fb58872a527679acbe380bbc78d8ad2052ea20bca3470393`.
Read pp.2–5, especially action (1.4), N=4Nf and beta functions (2.1).
Application and limits in the joint-flow report dated 2026-11-06.

## Interaction-driven velocity flow — acquired 2026-11-06

M. M. Anber and J. F. Donoghue, *The emergence of a universal limiting
speed*, arXiv:1102.0789v2, Phys. Rev. D 83, 105027 (2011).
Downloaded unchanged from `https://arxiv.org/pdf/1102.0789`; checked the
v2 stamp, title and authors on p.1. Stored as `1102.0789v2.pdf`, 291803
bytes, 13 pages. SHA256:
`46b33eb09d810174b2e54c71e39970be96b9acfa7f1cf92bb345d4557d8ed67d`.
Versioned URL: https://arxiv.org/pdf/1102.0789v2 .

Read with `pdftotext -f/-l -layout`: pp.1–4 and 7–10, in particular
Eqs. (18)–(19), the Jacobian at the top of p.4, and Eqs. (51)–(55).
Scope and transfer limits are recorded in
`reports/2026-11-06--velocity-selection-mechanism-search.md`.
This acquisition does not authorize an interacting QCA extension.

## Pavia QCA program

1. **A. Bisio, G. M. D'Ariano, P. Perinotti, A. Tosini**  
   *Weyl, Dirac and Maxwell Quantum Cellular Automata: analytical solutions and phenomenological predictions of the Quantum Cellular Automata Theory of Free Fields*  
   arXiv:1601.04842  
   https://arxiv.org/abs/1601.04842

2. **A. Bisio, G. M. D'Ariano, P. Perinotti, A. Tosini**  
   *Free quantum field theory from quantum cellular automata: derivation of Weyl, Dirac and Maxwell quantum cellular automata*  
   arXiv:1601.04832  
   https://arxiv.org/abs/1601.04832

3. **G. M. D'Ariano, P. Perinotti**  
   *Quantum cellular automata and free quantum field theory*  
   arXiv:1608.02004  
   https://arxiv.org/abs/1608.02004

## Bernstein background

The scalar/trigonometric Bernstein derivative inequality and equality theory are classical background and must not be presented as project novelty.

A separate prior-art audit should eventually record the exact primary references used for:

- trigonometric Bernstein inequality;
- Riesz interpolation formula;
- equality/extremal cases;
- matrix/Laurent extensions genuinely relevant to unitary Bloch symbols.

## Checked inputs for the exact battery — 2026-09-14

The local `1601.04832v1.pdf` is the 10-page primary source above, downloaded
without transformation from `https://arxiv.org/pdf/1601.04832v1` (583334 bytes).
SHA256: `0dbf0a0bea497701e0408ce410d62ca0183a4aa14b4116254d029ff6602f1367`.
Its title and authors were checked against the first page; equations (15)-(17)
on p.6 and (20), (23)-(28) on p.7 were read, including visual PDF inspection.

Reacquisition and manual inspection commands, from the repository root:

```sh
curl -fL --retry 2 https://arxiv.org/pdf/1601.04832v1 -o sources/1601.04832v1.pdf
sha256sum sources/1601.04832v1.pdf
pdfinfo sources/1601.04832v1.pdf
pdftotext -f 6 -l 7 -layout sources/1601.04832v1.pdf -
```

The Dirac dagger was cross-checked against
[1601.04842v1, equation (9)](https://arxiv.org/html/1601.04842v1#S2.E9);
its equations (4), (7), (8) also display the Weyl inputs.
See the [analytic report](../reports/2026-09-14--weyl-dirac-exact-gate.md)
for the relevant sign, dagger, and fixed-mass expansion issues. The verifier
uses the declared unitary matrices, not the inconsistent prose phase sign or
the block with the missing dagger. No general literature/novelty audit is claimed.

## Source discipline

Do not cite this file as evidence for a mathematical claim. It is only an index. Before promoting a claim to `ESTABLISHED`, verify it against the primary source and record the exact equation/theorem location in a report or derivation note.

## Triangular / honeycomb walk sources — added 2026-11-01

Acquired for row L6 of the draft `theory/C_ACROSS_LATTICES_GATE.md`
(user instruction 2026-11-01). Downloaded without transformation with
`curl -fL https://arxiv.org/pdf/<id> -o sources/<id>v<n>.pdf`.

| File | Paper | SHA256 | Bytes |
| --- | --- | --- | --- |
| `1803.01015v2.pdf` | P. Arrighi, G. Di Molfetta, I. Márquez-Martín, A. Pérez, *The Dirac equation as a quantum walk over the honeycomb and triangular lattices*, arXiv:1803.01015v2 (Phys. Rev. A 97, 062111 (2018)) | `1d1de6058787437bb712448af11dd6b57d83f73fbe6cb7e6dffd242a45f8a570` | 281758 |
| `1803.01304v1.pdf` | G. Jay, F. Debbasch, J. B. Wang, *Dirac quantum walks on triangular and honeycomb lattices*, arXiv:1803.01304v1 (Phys. Rev. A 99, 032113 (2019)) | `9fa0ea34763b4dd01fe2c38d699ecf5358b98b6b1582381f95330c84eb90ff90` | 9452775 |

Read 2026-11-01 (text extraction, `pdftotext -layout`, per page):

- `1803.01015v2.pdf`: p.1–2 (scope; regular-lattice Dirac QW Eq. (3);
  claim that it circumvents the P17 no-go by placing two-component spinors
  on edges shared by adjacent triangles, p.2); p.3 honeycomb QW,
  axes `u_i` Eq. (4), matrices `tau_i` Eq. (5), coin `W` Eq. (9), walk
  `W T_2 W T_1 W T_0` Eq. (10); p.4 triangular QW Eq. (12), stated to
  implement the honeycomb QW "in a covert way", continuum factor
  `sqrt(3)/6` after three steps; p.5 summary.
- `1803.01304v1.pdf`: p.1 `U(alpha,xi,zeta,theta)` Eq. (1), equilateral
  triangular neighbours `X_1..X_6` at distance epsilon, partial shifts
  `(S_j Psi)(X) = (psi^L(N_j), psi^R(N_{j+1}))`; p.2 six-step walk Eq. (2)
  with mass `U_m`, three-step equilateral walk Eq. (4)–(5), three-step
  isosceles walk Eq. (6), three-step honeycomb walk Eqs. (7)–(9) with
  `Delta t = 3 sqrt(3) epsilon/4`; p.3–4 dispersion figures only (not
  used as evidence).
- Also read for the same draft: `1802.03910v1.pdf` p.3–8 (1D walk
  Eq. (17); BCC axis-product walk Eqs. (22)–(23) p.5; anticommutation of
  `Delta P_i` Eqs. (25)–(27) p.6; momentum symbol Eq. (33) p.7);
  `1312.2852v1.pdf` p.4–5 Eqs. (20)–(21) and the BCC remark;
  `1609.00305v2.pdf` p.1–3 (paired/encoded QW, Eqs. (3)–(6)).

## CJWW tail-estimate paper — entry added 2026-11-04

Archived on 2026-09-15 in `f74018f` (s4-family prior-art audit); this entry
was missing until 2026-11-04 (work plan, Sec. 3). Size and SHA256 measured
on 2026-11-04 with `stat -c %s` and `sha256sum`; title, authors and arXiv
stamp checked against p.1 (`pdftotext -l 1`).

| File | Paper | SHA256 | Bytes |
| --- | --- | --- | --- |
| `2408.02108v1.pdf` | C. Cedzich, A. Joye, A. H. Werner, R. F. Werner, *Exponential tail estimates for quantum lattice dynamics*, arXiv:2408.02108v1 [quant-ph], 4 Aug 2024 | `25e2b03ff056fc78a7105fb81a6859be326ae2ee5717b35f7fc664b89ae7bdf8` | 1146894 |

Pages recorded as read live in the reports that cite them, not here:
`reports/2026-09-15--s4-family-prior-art-audit.md` (Sec. 5.3);
`reports/2026-09-16--directional-causal-saturation.md` (PDF pp. 17–18);
`reports/2026-10-31--h1-small-gaussian-profile.md` (p. 17);
`reports/2026-11-03--substrate-saturation-phase0-addendum-L4.md`
(Sec. 5.4, Eqs. (5.12)–(5.17), PDF pp. 16–17).

## Matchgate simulation (A5 contract, 2026-11-14)

Acquired for T1 of `theory/THIRRING_MATCHGATE_A5_GATE.md` (frozen at
`915e55f`), under the user's Q-b authorization (read-only download).
Downloaded 2026-11-14 from `https://arxiv.org/pdf/<id>` (latest version at
that date, checked on the abs page); size and SHA256 with `stat -c %s` and
`sha256sum`; title, authors and arXiv stamp checked against p.1
(`pdftotext -l 1`).

| File | Paper | SHA256 | Bytes |
| --- | --- | --- | --- |
| `0804.4050v2.pdf` | R. Jozsa, A. Miyake, *Matchgates and classical simulation of quantum circuits*, arXiv:0804.4050v2 [quant-ph], 19 Nov 2008 | `5f6ea3d7cf51f6e1981cd9139743161ca3847f59627c6b278c3e6ed2e52d497a` | 221878 |
| `quant-ph-0108010v2.pdf` | B. M. Terhal, D. P. DiVincenzo, *Classical simulation of noninteracting-fermion quantum circuits*, arXiv:quant-ph/0108010v2, 7 Aug 2001 | `71a6c85976f3697a24eb6c32219e6322915f4e2684cd772b25f4f67c3edb271a` | 219409 |
| `quant-ph-0108033v2.pdf` | E. Knill, *Fermionic Linear Optics and Matchgates* (extended abstract), arXiv:quant-ph/0108033v2, 8 Aug 2001 | `f01663a354b2b03a0e38931dbc277460101920248216b2acbdc9f3f5258086a9` | 130006 |

Read so far (2026-11-14), page numbers as printed / PDF page:
- Jozsa-Miyake p.2: definition of G(A, B), eq. (1) (A on span{|00>, |11>},
  B on span{|01>, |10>}, both SU(2) or both U(2) with equal determinant);
  Theorem 1 (n.n. lines, any product input, computational-basis
  measurement of any single line, <Z_k> computable classically); p.2-3:
  comparison with Valiant / Terhal-DiVincenzo and the notion of
  simulation; p.4: Theorem 2 (n.n. plus next-n.n. G(A, B), or n.n. with
  SWAP, are universal) — headings and statement only, proof not read.
- Terhal-DiVincenzo p.3-4: their restricted statement of Valiant's theorem
  (Theorem 1: n.n. gates of form (1) up to a phase, U^1, U^2 in SU(2);
  polynomial-time evaluation of |<y|M|x>|^2, of k-bit marginals, and
  sampling, for computational-basis input x); p.4-5: Hamiltonian form
  (Z, XX+YY-type, XY-type terms) and the remark that XY interactions on
  arbitrary pairs are universal, so the n.n. constraint is crucial.
- Knill: p.1 (title, abstract) only; not used.

Valiant (added 2026-11-14, after the user located a copy): the ACM URL
had returned an HTML page; the PDF was downloaded from
`https://www2.cs.sfu.ca/~abulatov/CMPT881QC/topics/valiant.pdf` (course
copy hosted at Simon Fraser University; the repository is private). p.1
carries «STOC'01, July 6-8, 2001, Hersonissos, Crete, Greece» and
«Copyright 2001 ACM 1-58113-349-9/01/0007»; printed pages 114-123.

| File | Paper | SHA256 | Bytes |
| --- | --- | --- | --- |
| `valiant-stoc2001.pdf` | L. G. Valiant, *Quantum Computers that can be Simulated Classically in Polynomial Time*, STOC 2001, pp. 114-123, doi:10.1145/380752.380785 | `ff54395f2a04bcffcb8f483bca409d9328aceed2545312d7a35479beb9958572` | 490658 |

Read (printed page numbers): p.118, Proposition 3 (a 4x4 character with
zeros outside the parity pattern and B(1,1)B(4,4) - B(2,2)B(3,3) =
B(1,4)B(4,1) - B(2,3)B(3,2) is realizable by a matchgate if B(4,4) != 0),
the five matchgate identities, and the remark that for unitary characters
with that pattern the first identity is equality of the two 2x2 block
determinants; Main Theorem (character entries of a matchcircuit as
Pfaffians when its gates are (a) diagonal, (b) on bits with indices
differing by one with only the parity-pattern entries nonzero, or (c) any
matchgate on bits x1, x2), Corollary 1 (|PfS(M_{x,y})|^2 is the transition
probability of a quantum matchcircuit), Theorem 4 (sums over partial
assignments in polynomial time) — all on p.120 (corrected 2026-11-14 after
Astra's review; first written as p.119); p.121, Measurement Theorem (randomized
polynomial-time sampling of outputs consistent with a partial assignment,
given a total input assignment). The identification of the character with
the gate matrix in the computational basis is as restated by
Terhal-DiVincenzo p.3; Valiant p.120 notes a complemented 0/1 reading
"inessential".

## S4 isotropy gate (DEP Definition 1) — acquired 2026-11-17

| File | Source | SHA256 | Bytes |
| --- | --- | --- | --- |
| `1708.00826v2.pdf` | G. M. D'Ariano, M. Erba, P. Perinotti, *Isotropic quantum walks on lattices and the Weyl equation*, arXiv:1708.00826v2 (Phys. Rev. A 96, 062101), downloaded from `https://arxiv.org/pdf/1708.00826v2` | `dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81` | 1856564 |

Read (in the alphaXiv full text of the same version, 2026-11-17): abstract,
introduction, Sec. II (generating set with or without the identity,
Definition 1, homogeneity condition (2)), d=1, d=2, d=3 solution passages,
summary theorem, conclusions. Title and authors checked on p.1 of this PDF.
Used by `theory/S4_DEP_ISOTROPY_GATE.md` and its execution report.
