# DISPERSION_DATA_COMPARISON — contract

**Status of this text:** frozen at the commit that introduces it
(preregistration). Written 2026-11-09 by Claude (Opus 5.5); user authorization
«adelante», after being offered "un contrato para hacer esta comparación en
serio". Nothing in Secs. 3-5 has been computed in a retained form. A rough
orientation was given in conversation (Sec. 8).
**Parents:** `DISPERSION_CORRECTIONS_ACROSS_LATTICES` (promoted 2026-11-02;
coefficient table), `OBSERVATIONAL_SIGNATURE_SATURATION` (2026-11-09,
reviewed, not promoted), and the source check
`investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md`.
**Initial scientific status: OPEN.**

## 0. Single question

> Under an explicit photon dictionary, what upper bound on the lattice step
> ell, and what lower bound on the update frequency f = 1/tau, does each
> declared row's leading dispersion correction imply when compared with the
> verified astrophysical bounds, as a range over the unknown orientation of
> the lattice relative to the sources?

## 1. Known, question, abandonment

Known: the parent coefficients (exact; group-speed correction
|grad eps|/c_0 = 1 + 2 beta(n̂) t + ... or 1 + 3 alpha(n̂) t^2 + ..., with t = k ell);
verified bounds (source check, items 1-3):

- LHAASO ML values: E_QG,1 > 1.0e20 GeV (subluminal), 1.1e20 GeV (superluminal);
  E_QG,2 > 6.9e11 GeV (sub), 7.0e11 GeV (super); with
  v = c[1 - s (n+1)/2 (E/E_QG,n)^n];
- Kostelecký–Mewes d = 5 CPT-odd: |varsigma^(5)_3| bounded between 7e-35 and
  2e-34 GeV^-1 depending on the source direction, with
  delta v_gr = ±2 E |varsigma_3|.

No absolute scale is derivable (4B), and c = c_0 ell/tau.

Abandonment of this route: if every row's bound is either vacuous (no
constraint in any direction) or flips qualitatively between dictionaries
D1 and D2 for every row, record `NO_DATA_DISCRIMINATION_UNDER_DICTIONARY`.

## 2. Rows

The 13 rows of the parent table, with coefficients imported as transcribed
in `scripts/verify_observational_signature_gate.py` (parent_table). No new
walk.

## 3. Dictionary (frozen; conditional, not a result)

- **H_gamma:** the row's massless branch near the node is the photon;
  E = hbar c k at leading order, so t = k ell = E ell/(hbar c).
- **D1 (non-birefringent):** both photon helicities follow the same branch
  correction. Matching gives:
  - n = 1: 2|beta(n̂)| ell/(hbar c) = 1/E_QG,1, so
    ell_max(n̂) = hbar c/(2 |beta(n̂)| E_QG,1). Use the subluminal E_QG if
    beta(n̂) < 0 and the superluminal one if beta(n̂) > 0.
  - n = 2 (beta ≡ 0): 3|alpha(n̂)| ell^2/(hbar c)^2 = (3/2)/E_QG,2^2, so
    ell_max(n̂) = hbar c/(sqrt(2|alpha(n̂)|) E_QG,2), with the sign rule
    analogous.
- **D2 (birefringent):** the two helicities carry opposite order-1
  corrections ±beta(n̂). This applies only to rows with beta ≢ 0; for L5b it
  is the row's own pair of Weyl blocks. Matching to the SME CPT-odd d = 5
  form: |varsigma_3| = |beta(n̂)| ell/(hbar c), so
  ell_max(n̂) = K hbar c/|beta(n̂)|, with K = 7e-35 GeV^-1 (strongest source)
  and K = 2e-34 GeV^-1 (weakest).
- **Frequency:** f_min(n̂) = c/(c_0 ell_max(n̂)).

## 4. Quantities per row

1. The order n and the exact range of |coefficient| over the unit sphere or
   circle: the supremum, and whether the infimum is 0 (directions with no
   constraint at that order).
2. Under D1: ell_max at the most sensitive direction (sup |coef|) in metres
   and in units of the Planck length ell_P, the corresponding f_min, and the
   list of unconstrained directions (coef = 0) if any.
3. Under D2 (beta rows): the same with both values of K.
4. A summary table comparing the order-1 rows (super-c rows) and the
   order-2-only rows.

Constants: hbar c = 1.973269804e-16 GeV m; ell_P = 1.616255e-35 m;
E_Pl = 1.22e19 GeV (LHAASO's value); c = 299792458 m/s. These are physical
input, stated to the digits given. Exact SymPy for the coefficient ranges;
decimal arithmetic for the constants.

## 5. Hypotheses (before computing)

- **Hi:** under D1, every order-1 row requires ell_max < ell_P at its most
  sensitive direction.
- **Hk:** under D1, every order-2-only row allows ell_max > 10^6 ell_P at
  every direction where its coefficient is nonzero.

## 6. Method, budget, stop rules

- One permanent verifier `scripts/verify_dispersion_data_comparison.py`,
  committed before its first run; failed runs retained; two command entries.
- Only the verified bounds of the source check. No unverified source. No
  combination of sources, no likelihood, no new data.
- L3s4 is kept symbolic in a; any sample value of a is labelled as such.
- One session. Stop when Sec. 4 is filled or `OPEN` with reason.

## 7. Verdicts and claim ceiling

- Per row: bound ranges, or `UNCONSTRAINED_AT_LEADING_ORDER` (L1, and the
  zero-coefficient directions).
- Hi, Hk: `CONFIRMED_IN_DECLARED_ROWS` / `REFUTED_BY_ROW_<Id>`.
- Route: `DATA_SEPARATE_ORDER1_FROM_ORDER2_ROWS` /
  `NO_DATA_DISCRIMINATION_UNDER_DICTIONARY` /
  `OPEN_AFTER_BOUNDED_ATTEMPT`.

Everything is conditional on H_gamma and on D1/D2. No claim that our
universe is a QCA or a simulation, and no claim that any row describes the
photon. PRELIMINARY until a cross-family review; no promotion without a
separate user decision.

## 8. Explored before freezing (declared)

In conversation I gave rough estimates by hand:

- order-1 rows: ell ≲ ell_P/(20|beta|);
- order-2 rows: ell ≲ 1e-27 m;
- a birefringent mapping: ell ~ 1e-49 m.

These motivated Hi and Hk. They are not retained results; the verifier
recomputes everything.
