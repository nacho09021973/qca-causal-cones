# Extractos literales con numeración de línea original (preparado 2026-11-04, base 78eb306)

## state/CURRENT_STATE.md, l. 462–537 (Sec. 5)
```
462: ## 5. Completed standard Weyl/Dirac exact gate
463: 
464: **Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**
465: 
466: Evidence is the committed
467: [contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
468: [analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
469: [verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
470: [permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
471: Source provenance and the published sign/dagger issues are recorded there.
472: The analytic proof establishes the open mass interval and continuum scaling;
473: the check count alone is not their justification or a formal proof certificate.
474: 
475: ### Declared family and coordinates
476: 
477: The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
478: on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
479: the minimal two-component blocks. The seven symbols are not seven independent
480: geometries: transposes/chiralities within a dimension share support, inradius
481: and linear speed. There are three dimension-specific geometries in this battery.
482: 
483: Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
484: complete update per time unit:
485: 
486: `N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,
487: 
488: `C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,
489: 
490: `r_in = 1/sqrt(d)`, `V_causal^max = 1`.
491: 
492: ### Massless equality
493: 
494: For d=1,2,3 in this family, at the declared zero node,
495: 
496: `m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.
497: 
498: This is equality of the linear IR coefficient, not exact finite-momentum
499: relativistic dispersion or a theorem about every admissible symbol.
500: 
501: ### Fixed nonzero lattice mass
502: 
503: For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
504: `0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
505: continuous from the identity near the massless zero node. Then
506: 
507: `cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,
508: 
509: `F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,
510: 
511: `c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.
512: 
513: Exact finite-mass B* is refuted in the standard family under either extraction.
514: This result is no longer PRELIMINARY.
515: 
516: The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
517: expansions: `b = r_in^2 n (1-F)/(2m)` and
518: `c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
519: not a failure of the exact spectrum or an inconsistent calculation.
520: 
521: The endpoint m=1 is separate: actual hopping vanishes, active support becomes
522: `{0}`, and its inradius and spatial coefficients are zero. It is not covered
523: by the strict inequalities for `0 < m < 1`.
524: 
525: ### Small-mass / continuum matching
526: 
527: For each standard coupling in d=1,2,3,
528: 
529: `lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.
530: 
531: **VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
532: the equality of the limits is established analytically. The joint scaling
533: of momentum, dimensionless mass, neighbor length and time step is specified
534: in the report. Its continuum statement is local at fixed rescaled momentum
535: and mass, not a full propagator convergence theorem on arbitrary states.
536: 
537: ## 6. Current scientific interpretation
```

## reports/2026-11-01--c-across-lattices.md, l. 100–160 y l. 230–240
```
100: unaffected.
101: 
102: ## 3. Step sets: what the substrates actually are (Part 1)
103: 
104: | Row | Source label | Composite `F` (source units) | Substrate |
105: | --- | --- | --- | --- |
106: | L5a | BCC, axis product (FS Eqs. (20)–(21)) | the 8 points `{±1}^3` | BCC, same as L3 |
107: | L5b | BCC, axis product (MB Eqs. (23), (33)), s=4 | `{±1}^3` | BCC, same as L3 |
108: | L6a | honeycomb (ADMP Eq. (7)/(10)) | `0` and the hexagon `{±2u_i}`, radius 2 | triangular lattice, hexagonal `C_micro` |
109: | L6c | equilateral triangular, six-step (JDW Eq. (2)) | 19 points: the full hexagonal ball of radius 2 | same hexagonal `C_micro` as L6a, finer group (index 1 vs 4) |
110: | L6d | equilateral triangular, three-step (JDW Eq. (4)) | identical to L6a | **identical substrate to L6a** |
111: | L6e | isosceles triangular (JDW Eq. (6)) | the 4 points `(±1,±1)` | **square lattice with diagonal steps, same as L2** |
112: | L6f | honeycomb (JDW Eqs. (7)–(8)) | `0` and a hexagon of radius `sqrt3`, rotated 30° | triangular lattice, hexagonal `C_micro` (L6a up to rotation and scale) |
113: | L6b | triangular (ADMP Eq. (12)) | **not encoded** | edge geometry fixed only by Fig. 1 of the source |
114: 
115: No "honeycomb" walk in the declared sources acts on a honeycomb Bravais
116: structure: as homogeneous walks they move on a triangular lattice. The JDW
117: "isosceles" walk is on the standard square substrate. In two dimensions the
118: declared rows realise **two `C_micro` shapes** up to isometry and scale,
119: square and hexagonal. Counting the translation group as well, there are
120: three: square (L2, L6e); hexagon with step spacing equal to the hull radius
121: (L6a, L6d, L6f); and the same hexagon over the finer triangular group of
122: L6c (spacing/radius `1/2`, a scale invariant).
123: 
124: **Source sign issues (ADMP 1803.01015v2 p.3), certified as recorded
125: issues, not repaired silently:** (i) Eq. (8) holds for
126: `alpha = -arccos(sqrt5/3)`, not the printed `+arccos(sqrt5/3)`; (ii) with the
127: printed `S = e^{i pi/3} R_z(2 pi/3)`, `U_0 S` yields `tau_2`, not `tau_1`;
128: with `S^{-1}` the relations hold and the Eq. (10) symbol equals
129: `U_0 (Eq. (7) symbol) U_0^dag` exactly. L6a is built from the `tau_i` of
130: Eq. (5), which conditions C1–C2 define and the script verifies. Neither
131: issue changes `F` or `c_0`.
132: 
133: ## 4. Massless table (Part 2)
134: 
135: Units: longest step 1, one update per time unit. `V_causal^max = 1` in
136: every row by this normalisation. All entries exact.
137: 
138: | Row | Substrate | s | `r_in` | `c_0` | `c_0 / r_in` | `c_strict^iso` | `S_min = c_0` | Status |
139: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
140: | L1 | line | 2 | 1 | 1 | **1** | 1 | 1 | computed here |
141: | L2 | square | 2 | `1/sqrt2` | `1/sqrt2` | **1** | `1/sqrt2` | `1/sqrt2` | `C_infty^strict` new here; `c_0` from Sec. 5 |
142: | L6e | square | 2 | `1/sqrt2` | `1/sqrt2` | **1** | `1/sqrt2` | `1/sqrt2` | new |
143: | L3 | BCC | 2 | `1/sqrt3` | `1/sqrt3` | **1** | `1/sqrt3` | `1/sqrt3` | CURRENT_STATE Secs. 4, 5 (certified) |
144: | L5a | BCC | 2 | `1/sqrt3` | `1/sqrt3` | **1** | `1/sqrt3` | `1/sqrt3` | new |
145: | L5b | BCC | 4 | `1/sqrt3` | `1/sqrt3` | **1** | `1/sqrt3` | `1/sqrt3` | new |
146: | L3s4 | BCC | 4 | `1/sqrt3` | `a/sqrt3`, `0<a<1` | **a** | `1/sqrt3` | `a/sqrt3` | CURRENT_STATE Sec. 4.1 (reviewed) |
147: | L4 | cube `[-1,1]^3` | 2 | `1/sqrt3` | `1/sqrt3` | **1** | `1/sqrt3` | `1/sqrt3` | CURRENT_STATE Sec. 8 (CJWW (5.12), (5.15)) |
148: | L6a | hexagon | 2 | `sqrt3/2` | `1/2` | **`1/sqrt3` ≈ 0.577** | `sqrt3/2` | `1/2` | new |
149: | L6c | hexagon | 2 | `sqrt3/2` | `3/4` | **`sqrt3/2` ≈ 0.866** | `sqrt3/2` | `3/4` | new |
150: | L6d | hexagon | 2 | `sqrt3/2` | `3/4` | **`sqrt3/2`** | `sqrt3/2` | `3/4` | new |
151: | L6f | hexagon | 2 | `sqrt3/2` | `3/4` | **`sqrt3/2`** | `sqrt3/2` | `3/4` | new |
152: | L6b | — | 2 | — | — | — | — | — | OPEN (not encoded) |
153: 
154: For every computed row the script certifies: `U(0) = I` (node at `k=0`),
155: Hermitian linear generators, zero tilt, an isotropic untilted cone
156: (`{T_a, T_b} = 2 c_0^2 delta_ab`), the exact facets and vertices of
157: `C_micro`, and that every vertex Fourier coefficient is non-nilpotent. A
158: vertex `v` of `conv F` is reached in `n` updates only by repeating `v`, so
159: the coefficient of `n v` in `U^n` is `A_v^n != 0` for all `n`; hence
160: `C_infty^strict = C_micro` and `c_strict^iso = r_in` exactly in those rows.
230: 
231: ## 6. Hypotheses (contract Sec. 5)
232: 
233: | Hypothesis | Verdict |
234: | --- | --- |
235: | Ha: `c_0 = r_in` in every declared s=2 row with a massless node | **`REFUTED_BY_ROW_L6a`** (also L6c, L6d, L6f). Holds in L1, L2, L5a, L6e and the recorded L3, L4. |
236: | Hb: `c_strict^iso = r_in` in every declared row | **OPEN**: holds in every decided row (all computed and recorded rows); L6b undecided. The token `CONFIRMED_IN_DECLARED_ROWS` is not used because a declared row is OPEN. |
237: | Hc: no declared row with `c_0 > c_strict^iso` | **OPEN**: holds in every decided row (asserted by the script for the computed rows; L3, L3s4, L4 from their records); L6b undecided. |
238: 
239: ## 7. What this does not establish
240: 
```

## reports/2026-09-14--weyl-dirac-exact-gate.md, l. 120–145 (el «exact-gate report» que cita la auditoría)
```
120: \(u^2+|\mathbf v|^2=1\). Its characteristic polynomial is
121: \(\lambda^2-2u\lambda+1\). Hence its eigenvalues are
122: \(e^{\pm i\theta}\), \(\theta=\arccos u\), near the zero node. In d=1 one
123: may instead follow signed branches \(\pm k\); the positive phase is locally
124: \(|k|\). This distinction does not affect the speed coefficient.
125: 
126: The products give \(u=\cos k\) in d=1, \(u=\cos q_x\cos q_y\) in d=2, and
127: \(u=\cos q_x\cos q_y\cos q_z\pm\sin q_x\sin q_y\sin q_z\) for A±.
128: The sign is fixed by \(u=\operatorname{tr}W/2\), not an independent phase choice.
129: 
130: For all seven cases,
131: 
132: \[
133: u=1-\frac{|\mathbf k|^2}{2d}+O(|\mathbf k|^3),\quad
134: H_W=i\log W=\frac{\theta}{\sin\theta}\sigma\cdot\mathbf v
135: =\frac1{\sqrt d}\sum_j\Sigma_j k_j+O(|\mathbf k|^2),
136: \]
137: 
138: where \(\{\Sigma_i,\Sigma_j\}=2\delta_{ij}I\). Some symbols reflect a Pauli
139: axis; replacing that reflection silently by an identical matrix would be
140: incorrect, but its speed is unchanged. The displayed remainder is sufficient
141: in all dimensions; d=1,2 have no cubic scalar term. It follows that
142: \(\theta=c_0|\mathbf k|+O(|\mathbf k|^2)\), \(c_0=1/\sqrt d=r_d\).
143: This is an exact coefficient, not an exactly linear finite-momentum dispersion.
144: 
145: ## 5. Fixed-mass Dirac logarithm
```
