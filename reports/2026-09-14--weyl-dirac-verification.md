# Weyl/Dirac exact verification record

Result: PASS — 247 exact checks; zero tolerance; seven Weyl symbols and their Dirac couplings.

This is a local verification record, not a canonical status update.

Python: 3.12.3; SymPy: 1.14.0.

| Case | Weyl neighbors | Facets | r_in | V_causal^max | c_0 |
| --- | ---: | ---: | --- | --- | --- |
| d=1 A | 2 | 2 | 1 | 1 | 1 |
| d=2 A | 4 | 4 | sqrt(2)/2 | 1 | sqrt(2)/2 |
| d=2 B | 4 | 4 | sqrt(2)/2 | 1 | sqrt(2)/2 |
| d=3 A+ | 8 | 6 | sqrt(3)/3 | 1 | sqrt(3)/3 |
| d=3 B+ | 8 | 6 | sqrt(3)/3 | 1 | sqrt(3)/3 |
| d=3 A- | 8 | 6 | sqrt(3)/3 | 1 | sqrt(3)/3 |
| d=3 B- | 8 | 6 | sqrt(3)/3 | 1 | sqrt(3)/3 |

For each row and 0<m<1: M=asin(m), F=M*sqrt(1-m^2)/m;
c_H=c_0*F and c_omega2=c_0*sqrt(F). Analytically 0<F<1.
At m=0 both equal r_in (EXACT); at fixed 0<m<1 both equalities
with r_in are FALSE; matching as m tends to zero is ASYMPTOTIC.

At m=1 active support is {0}; all spatial coefficients and its inradius
are zero. The limiting ratio to the nonzero-mass substrate inradius is not
an inradius ratio for that collapsed active body.

Negative controls: missing dagger, reversed phase sign, omitted quadratic mass term detected.
Interval proof, continuum scaling and convention limits: see the analytic report.

## Provenance

- Script SHA256: `21841c3535036205f4026afd31038694fa91ccc0b6a846d7d1c93c873b97f058`
- Contract SHA256: `e0e3483380b0352198c64cbca64985a5240389b7fc70a2694c9a79f9a2f33d27`
- 1601.04832v1 PDF SHA256: `0dbf0a0bea497701e0408ce410d62ca0183a4aa14b4116254d029ff6602f1367`
- Weyl input: https://arxiv.org/abs/1601.04832v1, equations (15)-(17).
- Dirac dagger cross-check: https://arxiv.org/html/1601.04842v1#S2.E9.
- Baseline: 44ad178; fixed cases and semantics are specified by the contract.
