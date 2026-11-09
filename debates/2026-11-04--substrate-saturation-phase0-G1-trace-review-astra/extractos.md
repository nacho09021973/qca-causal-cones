# Extractos literales con numeración de línea original (preparado 2026-11-04, base cb814b5)

## scripts/verify_directional_saturation.py, l. 55–150
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
83: # B := -grad f, so that grad(arccos f) = B / sqrt(1 - f^2)
84: B1 = [sp.simplify(-sp.diff(F1, p)) for p in PS]
85: B2 = [sp.simplify(-sp.diff(F2, p)) for p in PS]
86: 
87: 
88: @check("source byte identity")
89: def _():
90:     if not SOURCE.exists():
91:         return False, f"missing {SOURCE}"
92:     got = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
93:     return got == SOURCE_SHA256, got
94: 
95: 
96: @check("both symbols unitary with det 1")
97: def _():
98:     out = []
99:     for nm, W in (("5.12", walk1()), ("5.15", walk2())):
100:         if not is_zero((W.H * W - I2).norm()) or not is_zero(sp.det(W) - 1):
101:             return False, f"{nm}: not unitary or det != 1"
102:         out.append(f"{nm}: W^dag W = I, det W = 1")
103:     return True, "; ".join(out)
104: 
105: 
106: @check("tr W(5.12)/2 = ccc + sss  (NOT the printed ccc - sss of (5.13))")
107: def _():
108:     tr = sp.trace(walk1()) / 2
109:     printed = C[0] * C[1] * C[2] - S[0] * S[1] * S[2]      # as printed in (5.13)
110:     return is_zero(tr - F1) and not is_zero(tr - printed), (
111:         "matches ccc+sss; the printed (5.13) ccc-sss is the trace of "
112:         "exp(-i p1 s1) exp(-i p2 s2) exp(-i p3 s3), i.e. the image under p -> -p")
113: 
114: 
115: @check("tr W(5.15)/2 = ccc, i.e. CJWW (5.16)")
116: def _():
117:     return is_zero(sp.trace(walk2()) / 2 - F2), "omega = arccos(c1 c2 c3)"
118: 
119: 
120: def jump_set(W):
121:     """Exact Fourier support F = {x : W_x != 0}.
122: 
123:     Both symbols have jump length 1 per coordinate, so multiplying by z1 z2 z3
124:     clears all negative powers and the monomials can be read off directly.
125:     """
126:     support = set()
127:     for entry in W:
128:         poly = sp.Poly(sp.expand(laurent(entry) * Z[0] * Z[1] * Z[2]), *Z)
129:         for mono, coeff in poly.terms():
130:             if sp.simplify(coeff) != 0:
131:                 support.add(tuple(int(m) - 1 for m in mono))
132:     return support
133: 
134: 
135: CORNERS = set(itertools.product((-1, 1), repeat=3))
136: 
137: 
138: @check("jump set of (5.12) is exactly the 8 cube vertices")
139: def _():
140:     F = jump_set(walk1())
141:     return F == CORNERS, f"{len(F)} vectors: {sorted(F)}"
142: 
143: 
144: @check("jump set of (5.15) has 14 vectors and contains the 8 cube vertices")
145: def _():
146:     F = jump_set(walk2())
147:     ok = CORNERS <= F and len(F) == 14 and max(max(abs(v) for v in x) for x in F) == 1
148:     return ok, f"{len(F)} vectors: {sorted(F)}"
149: 
150: 
```

## reports/2026-11-01--c-across-lattices.md, l. 102–115
```
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
```

## reports/2026-11-01--c-across-lattices.md, l. 136–152
```
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
```

## state/CURRENT_STATE.md, l. 750–758
```
750: 
751: ## 8. Directional causal saturation — canonical physical interpretation (2026-09-16)
752: 
753: **Evidence commit:** `2494192`.
754: [Report](../reports/2026-09-16--directional-causal-saturation.md),
755: [verifier](../scripts/verify_directional_saturation.py) (15/15, fail-closed,
756: fourteen exact).
757: 
758: The active physical question is: **does `c_IR` coincide with the microscopic
```

