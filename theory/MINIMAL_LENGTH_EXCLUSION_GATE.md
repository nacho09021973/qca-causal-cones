# MINIMAL_LENGTH_EXCLUSION — contract

**Status of this text:** frozen at the commit that introduces it
(preregistration). Written 2026-11-09 by Claude (Opus 5.5); user instruction
«mételo como hipótesis en un contrato», after the remark that "nothing can be
smaller than the Planck length".
**Parent:** `DISPERSION_DATA_COMPARISON` (contract ad445aa, report at
121f679). The parent's cross-family review (Astra) is **pending** at freeze;
any repair it requires propagates here.
**Initial scientific status: OPEN.**

## 0. Single question

> If the lattice step cannot be smaller than a minimal length lambda ell_P
> (hypothesis H_min), which of the 13 declared rows are excluded by the
> verified astrophysical bounds, under H_gamma and each dictionary D1/D2, and
> is each exclusion robust to the order-one factor lambda?

## 1. Known, question, abandonment

- **Known.** The parent gives ell_max/ell_P at the most sensitive direction
  of each row (D1 and D2).
- **Known.** The Planck length as a minimal length is a hypothesis, not
  established physics. Some quantum-gravity proposals have a minimum and
  others do not. This is `[UNVERIFIED]` here, since no source was read for
  it. The contract therefore treats it as a postulate.
- **Question.** See Sec. 0.
- **Abandonment.** If no row is robustly excluded under either dictionary,
  record `NO_ROBUST_EXCLUSION_UNDER_HMIN` and stop this line.

## 2. Hypotheses (explicit, conditional)

- **H_min:** ell ≥ lambda ell_P, with lambda in the frozen range
  [1/2, 2]. The range covers order-one ambiguities: which step is called
  "the cell" (the parent uses the longest step), and Planck conventions.
  lambda = 1 is the nominal value.
- H_gamma, D1 and D2 exactly as in the parent contract Sec. 3.
- No claim that H_min holds in nature.

## 3. Classification rules (frozen before any new evaluation)

For each row and dictionary, let r = ell_max/ell_P at the most sensitive
direction (parent values, recomputed by the verifier):

- `EXCLUDED_ROBUST`: r < 1/2. The row is excluded for every lambda in the
  range.
- `EXCLUDED_NOMINAL_ONLY`: 1/2 ≤ r < 1. Excluded at lambda = 1, not at
  lambda = 1/2.
- `ALLOWED_NOMINAL_EXCLUDED_AT_LAMBDA2`: 1 ≤ r < 2.
- `ALLOWED_ROBUST`: r ≥ 2.
- `UNCONSTRAINED`: L1, which has no correction.

Directional caveat (fixed now): every classification refers to the most
sensitive direction only. A row with zero-coefficient directions is
**not excluded** in those directions at leading order. The report must say,
for each excluded row, that a source in such a direction would not exclude
it at this order.

## 4. Quantities

1. r for each row under D1, and under D2 for beta rows (both K values),
   recomputed from the parent formulas and constants.
2. The class of Sec. 3 for each row and dictionary.
3. A summary: which rows survive H_min under D1 and under D2, and whether the
   survivors are exactly the order-2-only rows (where nothing outruns c at
   first order).

## 5. Verdicts

- Per row and dictionary: the class of Sec. 3.
- Line: `ONLY_ORDER2_ROWS_SURVIVE_HMIN_<D1|D2|BOTH>` /
  `NO_ROBUST_EXCLUSION_UNDER_HMIN` / `MIXED` (with the list).

## 6. Method and limits

- One permanent verifier `scripts/verify_minimal_length_exclusion.py`,
  committed before its first run; it imports the parent verifier read-only
  and recomputes r. Two command entries.
- Decimal arithmetic on the parent's stated constants. The class boundaries
  are exact thresholds on r.
- One session.
- No new data or directions. No combination of sources.
- No claim about our universe. PRELIMINARY until a cross-family review. No
  promotion without a separate user decision.

## 7. Explored before freezing (declared)

The parent's r values are known:

- D1, order-1 rows: 0.28-0.57;
- D2, beta rows: about 1e-14;
- order-2 rows: about 1e8.

In conversation I said that the D1 margin is about a factor 2 and not
robust. The class boundaries above were chosen with that knowledge, and the
range lambda in [1/2, 2] was fixed to express that order-one ambiguity, not
tuned to a desired split. This is declared so that a reviewer can judge it.
