# Extractos literales con numeración de línea original (preparado 2026-11-04, base cecf75a)

## state/CURRENT_STATE.md, l. 482–492
```
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
```

## scripts/verify_weyl_dirac_gate.py, l. 54–77
```
54: def published_symbol(dimension, chirality, variables):
55:     cosines = [(variable + 1 / variable) / 2 for variable in variables]
56:     sines = [(variable - 1 / variable) / (2 * sp.I) for variable in variables]
57:     if dimension == 1:
58:         scalar = cosines[0]
59:         vector = (0, 0, sines[0])
60:     elif dimension == 2:
61:         cos_x, cos_y = cosines
62:         sin_x, sin_y = sines
63:         scalar = cos_x * cos_y
64:         vector = (sin_x * cos_y, cos_x * sin_y, sin_x * sin_y)
65:     else:
66:         cos_x, cos_y, cos_z = cosines
67:         sin_x, sin_y, sin_z = sines
68:         scalar = cos_x * cos_y * cos_z + chirality * sin_x * sin_y * sin_z
69:         vector = (
70:             sin_x * cos_y * cos_z - chirality * cos_x * sin_y * sin_z,
71:             -chirality * cos_x * sin_y * cos_z - sin_x * cos_y * sin_z,
72:             cos_x * cos_y * sin_z - chirality * sin_x * sin_y * cos_z,
73:         )
74:     matrix = scalar * IDENTITY
75:     for component, pauli in zip(vector, PAULI):
76:         matrix -= sp.I * component * pauli
77:     return matrix.applyfunc(sp.expand), sp.expand(scalar)
```

## scripts/verify_directional_saturation.py, l. 55–82
```
55: 
56: 
57: def check(name, tag="ESTABLISHED"):
58:     def wrap(fn):
59:         CHECKS.append((name, tag, fn))
60:         return fn
61:     return wrap
62: 
63: 
64: def walk1():
65:     """CJWW (5.12): W(p) = exp(i p1 s1) exp(i p2 s2) exp(i p3 s3)."""
66:     W = I2
67:     for c, s, sig in zip(C, S, PAULI):
68:         W = W * (c * I2 + sp.I * s * sig)
69:     return sp.expand(W)
70: 
71: 
72: def walk2():
73:     """CJWW (5.15), transcribed entry by entry."""
74:     e = sp.exp(sp.I * P3)
75:     return sp.Matrix([
76:         [C[0] * C[1] * e, -C[0] * S[1] + sp.I * S[0]],
77:         [C[0] * S[1] + sp.I * S[0], C[0] * C[1] / e],
78:     ])
79: 
80: 
81: F1 = C[0] * C[1] * C[2] + S[0] * S[1] * S[2]     # tr W1 / 2
82: F2 = C[0] * C[1] * C[2]                          # tr W2 / 2
```

## theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md, l. 1–12
```
1: # DISPERSION_CORRECTIONS_ACROSS_LATTICES — frozen contract
2: 
3: **Status of this text:** frozen at the commit that introduces it; that
4: commit is the preregistration commit. Authorized by user instruction of
5: 2026-11-02 («haz lo que consideres, estás autorizado») on the draft
6: revised as recorded in `state/CURRENT_STATE.md` Sec. 13. Nothing computed
7: before this commit.
8: **Parent:** `C_ACROSS_LATTICES` (`theory/C_ACROSS_LATTICES_GATE.md`), its
9: table of massless rows, and `L6B_TRIANGULAR_ROW` for row L6b (promoted
10: 2026-11-02). Those rows are input; none is recomputed.
11: **Initial scientific status: OPEN.**
12: 
```

## theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md, l. 55–75
```
55: script, imported read-only (the bytes of a reviewed verifier are not
56: changed):
57: 
58: | Row | Substrate | Symbol taken from |
59: | --- | --- | --- |
60: | L1 | line | `verify_weyl_dirac_gate.published_symbol(1, 1, ·)` |
61: | L2 | square | `verify_weyl_dirac_gate.published_symbol(2, 1, ·)` |
62: | L6e | square | `verify_c_across_lattices_gate.row_L6e()` |
63: | L3 | BCC | `verify_directional_saturation.walk2()` (CJWW (5.15)) |
64: | L5a | BCC | `verify_c_across_lattices_gate.row_L5a()` |
65: | L5b | BCC | `verify_c_across_lattices_gate.row_L5b()` |
66: | L3s4 | BCC, `s = 4` | `cert_Aa_s4_counterexample.core(a, theta)` with `a` symbolic, `0 < a < 1`, at the massless point recorded in `CURRENT_STATE.md` Sec. 4.1 |
67: | L4 | cube `[-1,1]^3` | `verify_directional_saturation.walk1()` (CJWW (5.12)) |
68: | L6a | hexagon | `verify_c_across_lattices_gate.row_L6a()` |
69: | L6c | hexagon | `verify_c_across_lattices_gate.row_L6c()` |
70: | L6d | hexagon | `verify_c_across_lattices_gate.row_L6d()` |
71: | L6f | hexagon | `verify_c_across_lattices_gate.row_L6f()` |
72: | L6b | hexagon, `s = 6` | `verify_l6b_triangular_row_gate.step_symbol(...)` cubed, `V = U^3`, one admissible assignment and one coin reading, as the L6b report fixes them (all six are isometric) |
73: 
74: If a listed constructor turns out not to return the symbol in the form
75: the parent used, the row is marked `OPEN (symbol not reusable)` with the
```

## reports/2026-11-01--c-across-lattices.md, l. 138–150
```
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
```

