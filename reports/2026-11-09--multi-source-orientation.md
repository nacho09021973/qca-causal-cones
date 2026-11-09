# Multi-source orientation: results

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: exact checks, an
interval branch-and-bound attempt that did not close, and decimal
arithmetic; one sealed cross-family review (GPT-6 Astra) with repairs
applied, not re-reviewed; no promotion.**

Contract [MULTI_SOURCE_ORIENTATION_GATE.md](../theory/MULTI_SOURCE_ORIENTATION_GATE.md),
frozen at `dd9ab5c`. Sky positions verified in the original circulars and
recorded in the [source check](../investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md):
GCN 9339 for GRB 090510; GCN 32632 and 32635 for GRB 221009A =
Swift J1913.1+1946. Verifier committed before running at `2464e1a`. Single
run: 4/5. The failing check is the D2 branch-and-bound: OPEN, budget
exceeded. That outcome is allowed by the contract.

[Sealed Astra review](reviews/2026-11-09-multi-source-orientation-astra/informe_astra.md)
of the text at 630bd6e (herramientas 97292a9): «reparación necesaria». Each
repair was checked by the author; the original text is in git at 630bd6e.

1. **Wave vector vs propagation direction.** The order-2 cancellation holds
   for wave-vector directions n. Observed sources fix propagation
   directions r. With n = r - t grad_S beta(r) + O(t^2),
   |v|/c_0 = 1 + 2 beta(r) t + (3 alpha - (3/2)|grad_S beta|^2) t^2 + O(t^3).
   On r3 = 0 this is 1 - (2/3) r1^2 r2^2 t^2: the cancellation disappears
   except on the axes. Re-derived by hand: beta(n) = beta(r) - t|grad_S beta|^2,
   so the t^2 coefficient shifts by -2|grad_S beta|^2. The D1 statement is
   restated in Sec. 1.
2. **L3s4 wording.** Failing the single-source uniform criterion does not
   mean "not excluded". The boundaries are the exact roots, and the decimal
   values are approximations. D2 gets its own boundary a(q_2).
3. **D2 failure.** The plausibility argument for an escape within ±0.5° is
   withdrawn. The reviewer's bound |Delta p| ≤ (pi/360) sqrt(2/3) ≈ 0.0071
   shows that no sampled orientation can become an exact escape through
   those variations. The cause of the failed closure (geometry,
   interval overestimation or budget) is undetermined.
4. **Status of the branch-and-bound.** It is a conditional interval attempt,
   not a certified implementation. The ±0.5° is a hypothesis of rounding to
   the nearest degree, not a demonstrated astrometric uncertainty.
5. **L3s4 cluster signs.** The association of "upper cluster" with beta > 0
   is `[UNVERIFIED]`: the script hard-codes it and the branch formulas were
   not attached. The per-sign thresholds stand.
6. **Minor.**
   - `boxes_processed` includes the batch that triggered the exit.
   - The diagnostic docstring is inaccurate: it computes max_i |p_i|.
   - PASS C checks only the existence of the roots.
   - The L3 bound is a written argument, not computed by the script.

Conditional throughout on H_gamma, the dictionaries D1/D2, H_min
(ell ≥ lambda ell_P, lambda in [1/2, 2]) where used, and the sources'
observational assumptions.

## 1. Result

| Row | D1 (time of flight: GRB 221009A, GRB 090510) | D2 (polarization: 4 Kostelecký–Mewes GRBs) |
| --- | --- | --- |
| L5a, L5b, L4 | For any ≤ 3 propagation directions some orientation puts them on coordinate planes, where the **linear** term vanishes. The order-2 term does not vanish there (repair 1). Its coefficient, \|alpha_eff\| ≤ 1/18, gives ell_max ≳ 8.6×10^-28 m ≫ ell_P (written arithmetic, not machine-checked). So **not excluded under H_min** by these two sources. | `OPEN` (conditional interval attempt did not close) |
| L3s4, 0 < a < a(q_sub) ≈ 0.77315 | `EXCLUDED_ROBUST` under H_min for every orientation, for either sign | `EXCLUDED_ROBUST` (0 < a < a(q_2)) |
| L3s4, a(q_sub) ≤ a < a(q_super) ≈ 0.78262 | the beta > 0 branch is excluded; for the beta < 0 branch the single-source criterion does not decide | `EXCLUDED_ROBUST` |
| L3s4, a(q_super) ≤ a < a(q_2) | the single-source criterion does not decide; several sources might | `EXCLUDED_ROBUST` |
| L3s4, a ≥ a(q_2) (within about 3×10^-15 in a^2 of x_c, or beyond) | not decided | `OPEN` |
| L3 | `ALLOWED_ROBUST`: for every orientation and lambda there are lengths compatible with H_min and D1 (ell_max ≥ 9.2×10^7 ell_P) | not applicable |

a(q) = (sqrt(q^2 + 4DC) - q)/(2D), with C = sqrt3/6 + 1/9 and
D = sqrt3/6 + 2/9. The thresholds are q_super = 0.110990, q_sub = 0.122089
and q_2 = 1.709×10^-15. The sign-to-cluster identification is
`[UNVERIFIED]` (repair 5).

Line verdict: `ORIENTATION_INDEPENDENT_EXCLUSION_UNDER_HMIN_L3s4`, for
0 < a < a(q_sub) under D1 and 0 < a < a(q_2) under D2. L5a, L5b and L4: not
excluded by the two time-of-flight sources under H_min (D1); D2 OPEN.

- **Hm1:** `CONFIRMED` for wave-vector directions, through order 2, and for
  propagation directions at order 1. Not through order 2 in propagation
  directions.
- **Hm2:** `OPEN`.

## 2. Arguments

- **Wave-vector identities (exact, part A).**
  - Since beta is homogeneous, n·grad beta = 3 beta.
  - On n3 = 0, 3 alpha + |grad_S beta|^2/2 = 0.
  - The expansion |grad eps|/c_0 = 1 + 2 beta t + (3 alpha + |grad_S beta|^2/2) t^2
    holds; it is symmetric under permutations and under ±beta.
- **Escape construction (written, all degenerate cases).** Take e3 normal to
  the first two directions (any normal if they are parallel). Take
  e1 ∥ e3 × w for the third direction w, or any e1 ⊥ e3 if w ∥ e3. The
  generic maximum is 3: for four directions, the extra condition is
  algebraically exceptional (reviewer). That argument does not decide the
  specific GRB quadruple.
- **Propagation directions (repair 1).** On a coordinate plane the linear
  term vanishes. The quadratic coefficient is 3 alpha_eff = -(2/3) r1^2 r2^2,
  so |alpha_eff| ≤ 1/18. With the LHAASO quadratic bound this gives
  ell_max = hbar c/(sqrt(2|alpha_eff|) E_QG,2) ≥ 3 hbar c/E_QG,2 ≈ 8.6×10^-28 m.
  Not excluded under H_min.
- **D2 attempt (part B).**
  - The pruning logic is sufficient: a box is pruned only if some source
    violates the threshold for every enclosed orientation and position.
  - The threshold is |p_i| > delta_i = 2 sqrt3 (hbar c/ell_P) K_i.
  - It processed about 4.7×10^6 boxes over 27 levels without closing.
  - Limits: libm slack and the float constants are not certified; the
    Cartesian source boxes lose correlations.
  - Sampled diagnostic (no verdict): min over 20,000 sampled R of
    max_i |p_i| = 0.0099. By repair 3, this does not indicate an escape.
- **L3s4 (part C).**
  - inf |beta| = max(B - M, 0), since n1 n2 n3 reaches ±1/(3 sqrt3).
  - f = B - M is strictly decreasing on both branches, with
    f(1/√2) = sqrt6/12 and f(sqrt x_c) = 0.
  - Hence the roots a(q) are unique, and the criterion f > q gives an
    orientation-independent single-source exclusion.
  - The D2 sliver excluded from the argument has width
    x_c - a(q_2)^2 ≈ (sqrt(x_c)/D) q_2 ≈ 3×10^-15, positive.
- **L3.** sigma2 ≤ 1/3, so |alpha| ≤ 1/54 and ell_max(R) ≥ 9.2×10^7 ell_P.
  "Nothing outruns c" for L3 rests on the observational-signature gate (Sec. 3
  there, proved exactly), not on alpha ≤ 0.

## 3. What this says for "c is the clock"

Under the photon dictionary, the 3D rows and H_min:

- **L3s4 is excluded for every lattice orientation,** for a below about
  0.773, under either dictionary. It is a subfamily that lets excitations
  outrun c at first order and has no blind directions.
- **L5a, L5b and L4 are not excluded by the two available time-of-flight
  sources.** These are the ceiling rules that let excitations outrun c.
  Their linear term can be hidden on blind planes. The quadratic residual
  that then remains is far too weak to reach the Planck scale. Under the
  birefringent dictionary the result is OPEN.
- **L3 is compatible with H_min.**

This is not a general selection between rules with and without super-c
excitations; it concerns the declared rows only.

## 4. Verifier

[Script](../scripts/verify_multi_source_orientation.py),
[record](2026-11-09--multi-source-orientation.txt),
[JSON](2026-11-09--multi-source-orientation.json): 4/5 PASS, 1 FAIL. The
failing check is the D2 certification, OPEN. Several statements above are
written arguments not checked by the script (repair 6): the propagation-
direction coefficient, the bounds on L3s4's a, and L3.
