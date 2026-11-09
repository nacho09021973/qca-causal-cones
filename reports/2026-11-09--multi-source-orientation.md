# Multi-source orientation: results

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: exact checks, an
interval branch-and-bound that did not close, and decimal arithmetic; no
independent review, no promotion.**

Contract [MULTI_SOURCE_ORIENTATION_GATE.md](../theory/MULTI_SOURCE_ORIENTATION_GATE.md),
frozen at `dd9ab5c`. Sky positions verified in the original circulars and
recorded in the [source check](../investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md):

- GRB 090510: GCN 9339.
- GRB 221009A = Swift J1913.1+1946: GCN 32632 for the position, GCN 32635
  for the identification.

Verifier committed before running at `2464e1a`. First and only run: 4/5. The
failing check is the D2 branch-and-bound, which returned OPEN (budget
exceeded). That outcome is allowed by the contract and is recorded as the
result, not repaired.

Everything is conditional on H_gamma, on the dictionaries D1/D2, on H_min
(ell ≥ lambda ell_P, lambda in [1/2, 2]) where used, and on the sources'
observational assumptions.

## 1. Result

| Row | D1 (time of flight: GRB 221009A, GRB 090510) | D2 (polarization: 4 Kostelecký–Mewes GRBs) |
| --- | --- | --- |
| L5a, L5b, L4 | `ESCAPES_ALL_SOURCES`: some orientation puts both sources on coordinate planes, where the correction vanishes through order 2 | `OPEN` (minimum over orientations not certified) |
| L3s4, a < 0.7731 (both clusters) | `EXCLUDED_ROBUST` under H_min for every orientation | `EXCLUDED_ROBUST` for every orientation (B - M ≫ 1.7×10^-15) |
| L3s4, 0.7731 ≤ a < 0.7826 | upper cluster `EXCLUDED_ROBUST`; lower cluster not | excluded except a sliver at a^2 → x_c |
| L3s4, a ≥ 0.7826 | not excluded (B - M below threshold, or blind directions for a^2 ≥ x_c) | `OPEN` for a^2 ≥ x_c |
| L3 | `ALLOWED_ROBUST` for every orientation (ell_max ≥ 9.2×10^7 ell_P) | not applicable (no beta) |

Line verdict: `ORIENTATION_INDEPENDENT_EXCLUSION_UNDER_HMIN_L3s4`, for
a < 0.7731 under D1 and for a^2 < x_c except a thin sliver under D2. The
L5a/L5b/L4 rows escape D1 and are OPEN under D2.

- **Hm1** `CONFIRMED`: L5a, L5b and L4 have escape count ≥ 3 through order 2.
- **Hm2** `OPEN`: no certification. A sampled diagnostic suggests that the
  four sources can be brought close to the blind planes.

## 2. Arguments

- **Order-2 cancellation (exact, part A).** Since beta is homogeneous of
  degree 3, n·grad beta = 3 beta, so on beta = 0 the gradient is tangential.
  On n3 = 0, |grad_S beta|^2 = n1^2 n2^2/3 and 3 alpha = -n1^2 n2^2/6. Hence
  the order-2 group-speed coefficient 3 alpha + |grad_S beta|^2/2 vanishes.
  The expansion |grad eps|/c_0 = 1 + 2 beta t + (3 alpha + |grad_S beta|^2/2) t^2
  is checked symbolically. By permutation symmetry the same holds on every
  coordinate plane, for +beta and -beta.
- **Escape count ≥ 3 (written construction).** Two source directions span a
  plane. Rotate it onto n3 = 0. A rotation about the new n3 axis then moves
  the third direction into n1 = 0 (or it already lies on that axis). So any
  2 or 3 sources sit on coordinate planes, where L5a, L5b and L4 have no
  correction through order 2. With the two D1 sources this needs no data
  beyond their existence.
- **D2 branch-and-bound (part B, not closed).** ZYZ Euler boxes; float
  interval arithmetic with np.nextafter outward rounding; Lipschitz sin/cos
  enclosures with a 10^-15 slack for libm error (assumed, not proved);
  source directions enclosed with ±0.5° (the positions are given to integer
  degrees). Targets |n1 n2 n3| > delta_i = 2 (hbar c/ell_P) K_i sqrt3, about
  3-8×10^-15. It processed 4.7×10^6 boxes over 27 levels without pruning
  everything. Sampled diagnostic (floats, 20,000 random orientations, no
  verdict): the smallest max_i |n1 n2 n3| found is 0.0099. A ±0.5° position
  box changes |n1 n2 n3| by up to about 0.02, so an exact escape within the
  positional uncertainty is plausible. It is not decided.
- **L3s4 (part C, decimal).** For a^2 < x_c, inf |beta| = B - M > 0 in every
  direction, with B = sqrt3 (1-a^2)/(6a) and M = |2a^2 - 1|/(9a). So any
  single source gives an orientation-independent bound.
  - Under D1 and H_min, `EXCLUDED_ROBUST` iff B - M > (hbar c/ell_P)/E_QG,1.
    The threshold is 0.1110 for the upper cluster (beta > 0, superluminal
    E_QG) and 0.1221 for the lower cluster. The boundary roots are
    a = 0.78262 and a = 0.77315, from quadratics on the branch a^2 ≥ 1/2;
    for example f(1/√2) = 0.204.
  - Under D2, with the strongest K and a single source, the threshold is
    B - M > 1.7×10^-15, met for a^2 < x_c except arbitrarily close to x_c.
- **L3.** Its bound at the most sensitive direction is already
  ell_max = 9.2×10^7 ell_P. Any orientation gives a larger or equal ell_max
  (weaker coefficient), so `ALLOWED_ROBUST` under H_min for every
  orientation.

## 3. What this says for "c is the clock"

Under the photon dictionary, the 3D rows and H_min:

- **One rule is excluded whatever the orientation of the lattice:** L3s4 for
  a < 0.77. It lets excitations outrun c at first order and has no blind
  directions.
- **The rules at the isotropic ceiling that let excitations outrun c**
  (L5a, L5b, L4) are not excluded by time of flight: two sources can always
  be hidden on their blind planes. Under the birefringent dictionary, four
  polarization sources might exclude them, but this was not certified and
  may fail within the positional uncertainty.
- **The rule in which nothing outruns c (L3) is allowed.**

## 4. Limits

- The D2 result is OPEN; nothing about L5a, L5b or L4 under D2 is claimed.
- The interval method assumes a libm error below 10^-15, which is not
  proved. Constants enter as floats. These limits matter only for a CERTIFIED
  outcome, which did not occur.
- The L3s4 thresholds are decimal arithmetic on stated constants; the
  boundaries in a inherit their roundings.
- Dictionaries and H_min are assumptions. The LHAASO analysis is isotropic
  and is transferred direction by direction at leading order.
- 2D rows are excluded from scope as photon models.

## 5. Verifier

[Script](../scripts/verify_multi_source_orientation.py),
[record](2026-11-09--multi-source-orientation.txt),
[JSON](2026-11-09--multi-source-orientation.json): 4/5 PASS, 1 FAIL. The
failing check is the D2 certification, outcome OPEN (budget exceeded). The
sampled minimum is a labelled diagnostic and feeds no verdict.
