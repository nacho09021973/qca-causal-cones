# Sources

Primary sources currently relevant to the freeze.

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
