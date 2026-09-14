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
