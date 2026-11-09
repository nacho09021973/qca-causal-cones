# Dispersion data comparison: results

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: exact checks plus
decimal arithmetic with stated physical constants; no independent review, no
promotion.**

Contract [DISPERSION_DATA_COMPARISON_GATE.md](../theory/DISPERSION_DATA_COMPARISON_GATE.md),
frozen at `ad445aa`. Verifier committed before running at `6b0e049`; first
run 9/9. Bounds used: only those verified in
[the source check](../investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md)
(LHAASO arXiv:2402.06009v3 Table I; Kostelecký–Mewes arXiv:1301.5367 Table III).

Everything below is conditional on H_gamma (the row's massless branch is the
photon) and on the frozen dictionaries:

- **D1:** both helicities follow the same correction.
- **D2:** order-1 corrections of opposite sign for the two helicities,
  matched to the SME CPT-odd d = 5 form.

No claim that any row describes the photon, or that our universe is a QCA.

## 1. Result

Route verdict: `DATA_SEPARATE_ORDER1_FROM_ORDER2_ROWS`.

| Rows | Leading correction | D1: largest allowed step at the most sensitive direction | D1: minimal clock rate | D2 (birefringent) |
| --- | --- | --- | --- | --- |
| L5a, L5b, L4, L3s4 (all a) | order 1 (super-c rows) | ell ≤ 0.55 ell_P (≈ 9×10^-36 m) | ≈ 6×10^43 Hz | ell ≤ 2×10^-14 ell_P (≈ 4×10^-49 m) |
| L6a | order 1 | ell ≤ 0.57 ell_P | ≈ 7×10^43 Hz | ell ≤ 2×10^-14 ell_P |
| L6b | order 1 | ell ≤ 0.28 ell_P | ≈ 2×10^44 Hz | ell ≤ 1×10^-14 ell_P |
| L2, L6e | order 2 | ell ≤ 1.4×10^-27 m ≈ 9×10^7 ell_P | ≈ 3×10^35 Hz | — |
| L3 | order 2 | ell ≤ 1.5×10^-27 m ≈ 9×10^7 ell_P | ≈ 3.5×10^35 Hz | — |
| L6c, L6d, L6f | order 2, isotropic | ell ≤ 2.3-4.6×10^-27 m ≈ 1.4-2.8×10^8 ell_P | ≈ 0.9-1.7×10^35 Hz | — |
| L1 | none (omega = abs(k)) | no constraint at any order | — | — |

In the D2 column the range of K (strongest and weakest source) changes the
value by a factor of about 3. The table gives the weakest bound.

- **Hi** `CONFIRMED_IN_DECLARED_ROWS`: under D1, every order-1 row needs
  ell < ell_P at its most sensitive direction.
- **Hk** `CONFIRMED_IN_DECLARED_ROWS`: every order-2-only row allows
  ell > 10^6 ell_P in every direction where its coefficient is nonzero. The
  bound is weakest where |alpha| is smallest and largest at sup |alpha|.

The two classes are separated by about 8 orders of magnitude in the allowed
ell under D1, and by about 21 under D2.

## 2. Inputs and matching (contract Sec. 3)

- **Group-speed corrections** (parent table): 2 beta(n̂) t at order 1 and
  3 alpha(n̂) t^2 at order 2, with t = k ell = E ell/(hbar c).
- **LHAASO form:** v = c[1 - s (n+1)/2 (E/E_QG,n)^n]. Hence
  ell_max = hbar c/(2|beta| E_QG,1) (n = 1) and
  ell_max = hbar c/(sqrt(2|alpha|) E_QG,2) (n = 2). The subluminal or
  superluminal E_QG is used according to the sign; all order-2 rows here
  have alpha ≤ 0, so they are delay-only.
- **D2:** |varsigma_3| = |beta| ell/(hbar c) < K, so ell_max = K hbar c/|beta|,
  with K = 7×10^-35 to 2×10^-34 GeV^-1.
- **Clock rate:** f_min = c/(c_0 ell_max).
- **Exact suprema over directions:**
  - L2, L6e: |alpha| ≤ 1/48, from 1/4 - n1^2 n2^2 = (n1^2 - n2^2)^2/4;
  - L3: |alpha| ≤ 1/54, from sigma2 ≤ 1/3;
  - beta rows: |beta| ≤ 1/9, √15/36 and √15/18;
  - L3s4: sup |beta| ≥ 1/9 for every 0 < a < 1, certified by a factorization
    on a^2 ≥ 1/2 and a monotonicity argument on a^2 ≤ 1/2;
  - L6c, L6d, L6f: isotropic, |alpha| = 1/512, 1/128 and 1/128.
- **Constants:** hbar c = 1.973269804×10^-16 GeV m; ell_P = 1.616255×10^-35 m;
  E_Pl = 1.22×10^19 GeV; c exact.
- **Hand checks:** L5a: ell/ell_P = E_Pl · 9/(2×10^20) = 0.549. L2:
  1.973×10^-16/(0.204 × 6.9×10^11) = 1.40×10^-27 m.

## 3. Limits

- **Direction.** The bounds are for the most sensitive direction. The
  orientation of the lattice relative to the sources is unknown. Every
  order-1 row and L2, L6e, L3 have directions where the leading coefficient
  vanishes:
  - coordinate planes for the n1 n2 n3 rows;
  - cos 3θ = 0 for L6a and L6b;
  - coordinate axes for L2 and L3.

  A source in such a direction constrains the row only at the next order.
  Order-1 rows there fall back to order-2-like bounds. Several sources in
  different directions would close this gap; combining them is outside this
  contract.
- **Dictionaries.** D1 and D2 are assumptions. Whether a row's beta term
  would be birefringent for the photon is not decided here. L5b's two Weyl
  blocks carry opposite beta, which is the D2 situation if those blocks were
  the two helicities.
- **Isotropic data analyses.** The LHAASO limits come from an isotropic
  analysis. Applying them to one direction is the leading-order reading.
- **Not decided:** L3s4's f_min (c_0 depends on a), the full validity range
  of the expansions, and any statement beyond the declared rows.

## 4. What this says for "c is the clock"

Under the photon dictionary and these 13 rows:

- Rules that let excitations outrun c at first order (the super-c rows)
  need a cell no larger than about half a Planck length, and 10^-14 Planck
  lengths if birefringent. A clock of at least about 10^44 Hz.
- Rules in which nothing outruns c, or that have only second-order delays,
  are allowed by current data with cells up to about 10^-27 m, a clock of
  about 10^35 Hz or more. 10^-27 m is about 10^8 Planck lengths.

The data do not say that c is a clock frequency. They say, for this class
and dictionary, that a first-order super-c rule would need its clock at or
above the Planck scale, while an order-2-only rule is still allowed with a
clock some eight orders slower.

## 5. Verifier

[Script](../scripts/verify_dispersion_data_comparison.py),
[record](2026-11-09--dispersion-data-comparison.txt),
[JSON](2026-11-09--dispersion-data-comparison.json): 9/9. The count covers:

- 7 exact identities and inequalities (suprema, the L3s4 bound);
- 2 recorded hypothesis evaluations (either outcome allowed).

The ell and f values are decimal arithmetic on stated constants, not
certified quantities.
