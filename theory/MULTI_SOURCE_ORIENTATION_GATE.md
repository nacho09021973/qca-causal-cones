# MULTI_SOURCE_ORIENTATION — contract

**Status of this text:** frozen at the commit that introduces it
(preregistration). Written 2026-11-09 by Claude (Opus 5.5); user choice «2»
(open a contract combining several sources before executing
`MINIMAL_LENGTH_EXCLUSION`).
**Parents:** `DISPERSION_DATA_COMPARISON` (repaired after Astra review: only
sensitivities at the direction of maximal coefficient; no exclusion for an
unknown orientation), `OBSERVATIONAL_SIGNATURE_SATURATION`,
`MINIMAL_LENGTH_EXCLUSION` (frozen at 130cdbc, not executed), and the source
check `investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md`.
**Initial scientific status: OPEN.**

## 0. Single question

> For a lattice of unknown orientation R in SO(3), and using several verified
> sources at known sky directions, does any 3D row's leading dispersion,
> under H_gamma and D1 or D2, imply a bound on ell that holds for **every** R?
> If so, is that bound below lambda ell_P (H_min, lambda in [1/2, 2])?

## 1. Known, question, abandonment

Known:

- Only d = 3 rows can describe a photon in 3D space: L3, L5a, L5b, L4 and
  L3s4. The 2D rows are out of scope here.
- Leading coefficients and zero sets (parent, after repair):
  - L5a, L5b, L4: beta ∝ n1 n2 n3, zero on the coordinate planes. There the
    order-2 group-speed term 3 alpha + |grad_S beta|^2/2 also vanishes, at
    least on n3 = 0 for L5a, L5b and L4 (reviewer computation, to be
    re-derived).
  - L3: alpha = -sigma2/18, zero only on the coordinate axes.
  - L3s4: zeros only if a^2 ≥ x_c.
- Verified sources with sky positions:
  - Kostelecký–Mewes Table I gives (theta, phi) for GRB 041219A, 100826A,
    110301A and 110721A, with per-source d = 5 bounds (Table III).
  - LHAASO GRB 221009A and Fermi GRB 090510 give time-of-flight bounds, but
    their sky positions were not read in a primary source. They must be
    verified before use.

Question: see Sec. 0.

Abandonment: if, for every 3D row and both dictionaries, some orientation
places all available sources in the row's zero set through the order
considered, record `NO_ORIENTATION_INDEPENDENT_BOUND_FROM_AVAILABLE_SOURCES`
and stop.

## 2. Quantities

1. **Escape count (exact).** For each 3D row, the largest k such that any k
   generic directions can be placed simultaneously in the zero set of the
   leading correction, and of the order-2 group-speed correction where the
   leading one vanishes, by some R. Exact argument or explicit construction.
   This includes the order-2 cancellation on the zero set (re-derived, not
   imported from the review).
2. **Available sources per dictionary.**
   - D1 (time of flight): GRB 221009A and GRB 090510, if their positions are
     verified in a primary source; otherwise D1 is `OPEN (positions not
     verified)`.
   - D2 (polarization): the four Kostelecký–Mewes GRBs, each with its own K_i.
3. **Orientation-independent bound.** For rows and dictionaries where the
   number of sources exceeds the escape count, compute
   m = min over R of max_i |coef(R^{-1} s_i)|/K_i. The bound is then
   ell_max = hbar c/(m · const), with the dictionary's constant. m must be
   certified by a **rigorous lower bound**: exact algebra, or interval
   branch-and-bound over SO(3) with outward rounding and certified
   constants (the Astra repairs of the previous gate apply; no float
   comparisons in a certified path). An upper bound on m, obtained by
   exhibiting an R, is allowed only as a non-verdict diagnostic.
4. **H_min comparison.** Compare each certified ell_max with lambda ell_P,
   lambda in [1/2, 2], using the class rules of `MINIMAL_LENGTH_EXCLUSION`
   Sec. 3.

## 3. Hypotheses (before computing)

- **Hm1:** L5a, L5b and L4 have escape count 3 through order 2, so two or
  three sources never exclude them for an unknown orientation.
- **Hm2:** with the four Kostelecký–Mewes sources, under D2, L5a, L5b and L4
  have a certified m > 0, and the resulting ell_max is below ell_P/2 for
  every orientation (`EXCLUDED_ROBUST` under H_min).

## 4. Method, budget, stop rules

- Sky positions of GRB 221009A and GRB 090510 are read in a primary source
  (paper or GCN), cited with page or circular number, and recorded in the
  source check. A web search may locate them; the original must be read.
- Rotation parametrization and search are fixed in the verifier before
  running.
- One permanent verifier `scripts/verify_multi_source_orientation.py`,
  committed before its first run; failed runs retained; two command entries.
- One session. If the rigorous lower bound on m does not close, the row and
  dictionary are `OPEN (min over orientations not certified)`. No
  floating-point verdict.
- No new data beyond verified sources, and no combination with unverified
  bounds.

## 5. Verdicts and claim ceiling

- Per row and dictionary: `ESCAPES_ALL_SOURCES` /
  `ORIENTATION_INDEPENDENT_BOUND_<value>` / `OPEN (...)`, and the H_min class
  where a bound exists.
- Hm1, Hm2: `CONFIRMED` / `REFUTED` / `OPEN`.
- Line: `ORIENTATION_INDEPENDENT_EXCLUSION_UNDER_HMIN_<rows,dict>` /
  `NO_ORIENTATION_INDEPENDENT_BOUND_FROM_AVAILABLE_SOURCES` /
  `OPEN_AFTER_BOUNDED_ATTEMPT`.

Everything is conditional on H_gamma, D1/D2 and H_min (when used), and on
the sources' observational assumptions. D2 additionally relies on the SME
matching and on each K_i being a bound on the combination at that source's
direction. No claim about our universe. PRELIMINARY until a cross-family
review; no promotion without a separate user decision.

## 6. Explored before freezing (declared)

Before writing this, I reasoned informally:

- two directions fit in one plane, and a rotation about its normal can
  place a third direction in a second coordinate plane; hence the expected
  escape count of 3 for n1 n2 n3 rows;
- with three rotation parameters, a fourth generic direction is not
  expected to fit.

Hm1 and Hm2 encode this expectation. No m, no position and no rotation
search has been computed.
