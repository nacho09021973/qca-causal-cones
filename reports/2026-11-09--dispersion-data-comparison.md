# Dispersion data comparison: results

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: exact checks plus
decimal arithmetic with stated physical constants; one sealed cross-family
review (GPT-6 Astra) with repairs applied, not re-reviewed; no promotion.**

Contract [DISPERSION_DATA_COMPARISON_GATE.md](../theory/DISPERSION_DATA_COMPARISON_GATE.md),
frozen at `ad445aa`. Verifier committed before running at `6b0e049`; first
run 9/9.

[Sealed Astra review](reviews/2026-11-09-dispersion-data-comparison-astra/informe_astra.md)
of the text at 121f679 (herramientas 97292a9): «reparación necesaria». The
matching factors, the angular suprema and the arithmetic were re-derived by
the reviewer and agree. Each repair below was checked by the author:

1. **Quantifier.** Values at the direction of maximal coefficient are a
   **sensitivity comparison**, not bounds on a lattice of unknown
   orientation. Near zero-coefficient directions the linear analysis gives
   no uniform bound. The old conclusion and Sec. 4 are rewritten.
2. **L3s4.** It has zero-coefficient directions only if a^2 ≥ x_c ≈ 0.7825,
   located at n1 n2 n3 = -(1-a^2)/(2(2a^2-1)), not on the coordinate planes.
   Its supremum is S(a), not 1/9. The numbers given use 1/9 and are
   conservative envelopes.
3. **Zero directions.** Where beta(n̂) = 0 but beta is not identically 0, the
   order-2 group-speed term is 3 alpha + (1/2)|grad_S beta|^2, not 3 alpha.
   For L5a, L5b and L4 on n3 = 0 the two cancel (3 alpha = -n1^2 n2^2/6;
   checked by hand). The claim that such directions fall back to order-2
   bounds is withdrawn.
4. **"Nothing outruns c".** This is proved only for L2 and L3
   (observational-signature gate, Sec. 3). For L6e, L6c, L6d and L6f the
   maximal group speed is OPEN.
5. **Missing quantities.** The D2 frequencies and L3s4's f_min were not
   computed by the verifier. Formulas are given (Sec. 2); the reviewer's
   numerical estimates are quoted as such.
6. **Inputs and presentation.** LHAASO entries are the Table I ML values.
   The abstract's "10 E_Pl" and "6×10^-8 E_Pl" are coarser roundings of the
   same results. Minor wording corrected (≃ in the hand check, "most
   restrictive" at sup |alpha|, about 22 orders between 1e-27 and 1e-49 m).

The original text is in git at 121f679.

Everything below is conditional on H_gamma (the massless branch is the
photon), on the frozen dictionaries D1 (non-birefringent) and D2
(birefringent, SME CPT-odd d = 5 matching), and on the observational
assumptions of the sources (isotropic analyses, transferred direction by
direction as a leading-order reading). No claim that any row describes the
photon, or that our universe is a QCA.

## 1. Result: sensitivities at the direction of maximal coefficient

Route verdict: `DATA_SEPARATE_ORDER1_FROM_ORDER2_ROWS`, read as a comparison
of leading-order sensitivities at each row's direction of maximal |coefficient|
(repair 1). It is not a separation valid for an unknown lattice orientation.

| Rows | Leading correction | D1 sensitivity: ell at max coefficient | D2 sensitivity |
| --- | --- | --- | --- |
| L5a, L5b, L4 | order 1 | 0.55 ell_P (8.9×10^-36 m) | 7.7×10^-15 - 2.2×10^-14 ell_P |
| L6a | order 1 | 0.57 ell_P | 7.9×10^-15 - 2.3×10^-14 ell_P |
| L6b | order 1 | 0.28 ell_P | 4.0×10^-15 - 1.1×10^-14 ell_P |
| L3s4 | order 1 | ≤ 0.55 ell_P (conservative envelope with 1/9 ≤ S(a)) | envelope |
| L2, L6e | order 2 | 1.40×10^-27 m (8.7×10^7 ell_P) | — |
| L3 | order 2 | 1.49×10^-27 m (9.2×10^7 ell_P) | — |
| L6c, L6d, L6f | order 2, isotropic | 2.3 - 4.6×10^-27 m | — |
| L1 | none | no constraint | — |

The order-1 rows use the subluminal E_QG, which is the weaker of the two
signs. With the superluminal value, ell is divided by 1.1.

- **Hi** `CONFIRMED_IN_DECLARED_ROWS`, with its stated quantifier: at the
  direction of maximal coefficient, under D1, every order-1 row has
  sensitivity below ell_P.
- **Hk** `CONFIRMED_IN_DECLARED_ROWS` as a comparison of leading-order
  limits: the order-2 limits exceed 10^6 ell_P. They are most restrictive
  at sup |alpha|.

## 2. Matching and quantities

- **D1.** u = E ell/(hbar c) equals t at leading order, which suffices at
  the orders used.
  - n = 1: ell = hbar c/(2|beta| E_QG,1). beta < 0 corresponds to s = +1
    (subluminal) and beta > 0 to s = -1.
  - n = 2 (beta ≡ 0): ell = hbar c/(sqrt(2|alpha|) E_QG,2), using
    6.9×10^11 GeV since alpha < 0.
- **D2.** Per-helicity correction ±2E|q_5|, so |q_5| = |beta| ell/(hbar c)
  and ell = K hbar c/|beta|. K is a direction-dependent combination,
  7×10^-35 to 2×10^-34 GeV^-1 from different sources. This range is not a
  statistical interval.
- **Suprema and zeros:**

  | Rows | Supremum | Zero directions |
  | --- | --- | --- |
  | L2, L6e | 1/48 | coordinate axes |
  | L3 | 1/54 | coordinate axes |
  | L5a, L5b, L4 | 1/9 | coordinate planes |
  | L6a | √15/36 | cos 3θ = 0 |
  | L6b | √15/18 | cos 3θ = 0 |
  | L6c, L6d, L6f | 1/512, 1/128, 1/128 | none |
  | L3s4 | S(a) = B + M | only if a^2 ≥ x_c |

  For L3s4, B = sqrt3 (1-a^2)/(6a) and M = |2a^2 - 1|/(9a), with
  inf |beta| = max(B - M, 0). S(a) > 1/9 on (0,1) (certified lower bound),
  and S(1/√2) = sqrt6/12 ≈ 0.204, isotropic.
- **Frequencies.** f_min = c/(c_0 ell).
  - D1 values: L5a, L5b, L4 5.85×10^43 Hz; L6a 6.54×10^43; L6b 1.96×10^44;
    L2, L6e 3.0×10^35; L3 3.5×10^35; L6c 8.7×10^34; L6d, L6f 1.7×10^35.
  - L3s4 conservative D1 bound:
    f_min(a) = 2 sqrt3 c E_QG,1 S(a)/(a hbar c).
  - D2: f_min(a,K) = sqrt3 c S(a)/(a K hbar c) for L3s4, and
    c |beta|/(c_0 K hbar c) in general. Not computed by the verifier
    (repair 5). The reviewer estimates 1.5-4.2×10^57 Hz for L5a, L5b and L4.

## 3. Limits

- **Orientation.** For one source and lattice orientation R, the bound
  depends on |beta(R^-1 n̂_source)|. When this can vanish, the linear
  analysis gives no uniform finite bound over R.
- **Zero directions.** On the zero directions of beta rows, the order-2
  group-speed coefficient is 3 alpha + (1/2)|grad_S beta|^2, and for L5a,
  L5b and L4 on n3 = 0 it vanishes (repair 3). Those directions are
  unconstrained through order 2. The distinction between wave-vector
  direction and propagation direction matters there.
- **Dictionaries and source transfer** are assumptions (see header).
- **Source fidelity.** The bounds were read in the originals by the author
  (source check). The reviewer could not verify them independently.

## 4. What this says for "c is the clock"

Within these assumptions, the comparison concerns sensitivity only:

- At their direction of maximal coefficient, rules with a first-order
  correction (the super-c rows of the previous gate) would be probed down to
  about half a Planck length, and to about 10^-14 ell_P if birefringent.
- Order-2-only rules are probed only down to about 10^-27 m.
- Among the order-2-only rules, it is proved only for L2 and L3 that
  nothing outruns c.
- For an unknown lattice orientation, no row is excluded by this analysis,
  because blind directions exist (for all order-1 rows except L3s4 below
  x_c, and for L2, L6e and L3).

## 5. Verifier

[Script](../scripts/verify_dispersion_data_comparison.py),
[record](2026-11-09--dispersion-data-comparison.txt),
[JSON](2026-11-09--dispersion-data-comparison.json): 9/9. These are 7 exact
identities and inequalities plus 2 recorded hypothesis evaluations, where
either outcome was allowed. The script stores 1/9 for L3s4 as if it were the
supremum; it is a lower bound of S(a) (repair 2). The ell and f values are
decimal arithmetic, not certified quantities.

**Effect on `MINIMAL_LENGTH_EXCLUSION` (frozen at 130cdbc, not executed).**
Its inputs are these sensitivities. Any "exclusion" there refers only to the
direction of maximal coefficient, never to an unknown orientation. L3s4
must use the envelope label.
