# Astrophysical bounds on photon dispersion and birefringence — source check

2026-11-09. Requested by the user («busca esas cotas astrofisicas reales») after
the observational-signature gate (`reports/2026-11-09--observational-signature-saturation.md`),
whose Sec. 5 deferred any comparison with data. Located with WebSearch
(standard mode); every number below was read in the original arXiv text
through the alphaXiv full-text tool in this session. Search summaries were
used only to locate papers. This file records literature, not a comparison:
no translation of these bounds to the repository's rows is made here (that
needs a successor charter).

## Verified in the original

| # | Source | What was read | Numbers (95% CL unless stated) |
| --- | --- | --- | --- |
| 1 | LHAASO Collaboration, "Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A", arXiv:2402.06009v3 (dated 17 Feb 2026) | Abstract; Eqs.(1)-(5); Table I; Sec. IV | Dispersion convention E^2 ≃ p^2c^2[1 - Σ s (E/E_QG,n)^n], s = +1 subluminal, -1 superluminal; v(E) ≈ c[1 - s (n+1)/2 (E/E_QG,n)^n]. ML (MINOS): E_QG,1 > 1.0×10^20 GeV (subluminal), > 1.1×10^20 GeV (superluminal); E_QG,2 > 6.9×10^11 GeV (sub), > 7.0×10^11 GeV (super). Abstract: E_QG,1 > 10 E_Pl, E_QG,2 > 6×10^-8 E_Pl; E_Pl ≃ 1.22×10^19 GeV. Source at z = 0.151; isotropic (direction-independent) dispersion model. |
| 2 | V. Vasileiou et al., "Constraints on Lorentz Invariance Violation from Fermi-LAT Observations of GRBs", arXiv:1305.3463v1 | Abstract | Subluminal, no source-intrinsic dispersion assumed, GRB 090510: E_QG,1 > 7.6 E_Pl, E_QG,2 > 1.3×10^11 GeV. (LHAASO [ref 21] quotes the same work as E_QG,1 > 9.3×10^19 GeV sub, 1.3×10^20 GeV super; consistent with 7.6 E_Pl.) |
| 3 | V.A. Kostelecký, M. Mewes, "Constraints on relativity violations from gamma-ray bursts", arXiv:1301.5367v1 (PRL 110, 201601) | Full text, Tables II-III | In the SME photon sector, dispersion for odd mass dimension d is necessarily accompanied by birefringence; only CPT-even, even-d coefficients give dispersion without birefringence. Direction-dependent bounds from GRB polarization: |Σ Y_jm k^(5)_(V)jm| < 7×10^-35 to 2×10^-34 GeV^-1 depending on the source direction (GRB 041219A, 100826A, 110301A, 110721A); isotropic |k^(5)_(V)00| < 2×10^-34 to 9×10^-34 GeV^-1. A single source constrains only one direction-dependent combination. |

## Located, not verified

- J.D. Finke, S. Razzaque, arXiv:2210.11261: claimed possible evidence for
  subluminal LIV from the survival of an 18 TeV photon of GRB 221009A
  (E_QG,1 ≲ 49 E_Pl). Known only from the search summary; contested by later
  analyses; not read. `[UNVERIFIED]`
- Abdo et al. (Fermi), Nature 462, 331 (2009), arXiv:0908.1832, GRB 090510,
  E_QG,1 > 1.2 E_Pl (earlier, more conservative). Seen only in summaries and
  as LHAASO ref. [20]. `[UNVERIFIED]`
- Yang, Bi, Yin (2024) LHAASO-data analysis with stronger quoted limits. Seen
  only in the search summary. `[UNVERIFIED]`

## Relevance to the repository (not a result)

- The verified time-of-flight bounds assume an isotropic dispersion law. The
  repository's order-1 (beta) rows have direction-dependent corrections that
  vanish on certain planes; one source bounds one direction.
- Source 3 says that, within the SME effective field theory, an order-1
  (d = 5) dispersion of photons is necessarily birefringent and is then
  bounded by polarization at the 10^-34 GeV^-1 level. Whether a QCA row's
  beta term maps to an SME d = 5 coefficient (for example via opposite signs
  in two helicity blocks, as in L5b) is a modelling question not addressed
  here.
- Any numerical bound on the lattice step ell or the clock frequency from
  these sources requires the dictionary H_gamma plus a successor contract.

Tools: WebSearch; alphaXiv full text. No ~/herramientas tool used.

## Sky positions (added 2026-11-09 for MULTI_SOURCE_ORIENTATION, read in the original circulars)

| Source | Circular read | Position (J2000) | Uncertainty |
| --- | --- | --- | --- |
| GRB 090510 | GCN 9339, M.R. Goad, J.P. Osborne, A.P. Beardmore, P.A. Evans, "GRB 090510: Enhanced Swift-XRT position" | RA, Dec = 333.55271, -26.58266 deg (22h14m12.65s, -26d34'57.6") | 1.4 arcsec (90%) |
| GRB 221009A | GCN 32632, S. Dichiara et al., "Swift J1913.1+1946 a new bright hard X-ray and optical transient": XRT source | RA, Dec = 288.2643, +19.7712 deg (19h13m3.43s, +19d46'16.3") | 5.6 arcsec (90%) |
| (identification) | GCN 32635, J.A. Kennea, M. Williams, subject "GRB 221009A: Swift detected transient may be GRB": BAT trigger 1126853 = Swift J1913.1+1946 | — | — |

Kostelecký–Mewes positions (codeclination theta, right ascension phi), Table I of
arXiv:1301.5367, given to integer degrees: GRB 041219A (27, 6), 100826A (112, 279),
110301A (61, 229), 110721A (129, 333). Per-source d = 5 bounds (Table III, first row):
2e-34, 7e-35, 2e-34, 1e-34 GeV^-1 respectively.

## Per-source time-of-flight limits (added 2026-11-09, read in the original)

Vasileiou et al., arXiv:1305.3463v1, Table IV ("Lower Limits on E_QG ... total degree of
dispersion"), linear case n = 1, in Planck units, 95% one-sided, methods PairView / SMM /
Likelihood:

| GRB | subluminal (s=+1) | superluminal (s=-1) |
| --- | --- | --- |
| 080916C | 0.11 / 0.09 / 0.22 | 18 / 5.4 / 0.2 |
| 090510 | 7.6 / 5.9 / 5.2 | 0.56 / 0.57 / 11 |
| 090902B | 0.17 / 0.15 / 0.12 | 0.38 / 0.86 / 0.37 |
| 090926A | – / 8 / 1.2 | 0.24 / 0.2 / 0.17 |

(Text extraction; column alignment read from the table layout. Other strong sources such as
the MAGIC GRB 190114C quadratic limit and H.E.S.S. AGN-flare limits are located but not read.)

Consequence for MULTI_SOURCE_ORIENTATION (arithmetic, not a gate result): under D1 a source
with E_QG,1 = X E_Pl gives at best ell_max/ell_P = 1/(2 X sup|beta|) = 4.5/X for L5a/L5b/L4.
EXCLUDED_ROBUST (< 1/2) would need X > 9; the strongest verified source (LHAASO, ~8.2 for
1.0e20 GeV) gives 0.549 at the most favorable direction. Sources with X ~ 0.1-1 can only give
ell_max of order 4.5-45 ell_P.
