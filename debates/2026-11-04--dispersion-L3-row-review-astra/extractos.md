# Extractos literales con numeración original (preparado 2026-11-04, base b9b0e58)

## scripts/verify_directional_saturation.py, l. 36–82
```
36: Z = sp.symbols("z1 z2 z3")
37: CHECKS = []
38: 
39: 
40: def laurent(e):
41:     """Canonical form: every symbol here is a Laurent polynomial in z_k = e^{i p_k}.
42: 
43:     Two such expressions agree as functions of real p iff they agree as Laurent
44:     polynomials, so `laurent(a - b) == 0` is a sound equality test.  Needed
45:     because (5.12) is written in cos/sin and (5.15) in exp, and SymPy does not
46:     reconcile the two forms on its own.
47:     """
48:     e = sp.expand(sp.expand(e).rewrite(sp.exp))
49:     e = e.subs({p: -sp.I * sp.log(z) for p, z in zip(PS, Z)})
50:     return sp.cancel(sp.powsimp(sp.expand(sp.powsimp(e, force=True)), force=True))
51: 
52: 
53: def is_zero(e):
54:     return sp.simplify(laurent(e)) == 0
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

## reports/2026-11-02--dispersion-corrections-across-lattices.md, l. 36–50
```
36: `sigma2 = n1^2 n2^2 + n2^2 n3^2 + n3^2 n1^2`.
37: 
38: | Row | Substrate | `c_0` | `G_walk` (exact) | Lowest correction | `beta(n̂)` | `alpha(n̂)` | `alpha_0` |
39: | --- | --- | --- | --- | --- | --- | --- | --- |
40: | L1 | line | 1 | `{±1}` | none: `omega = |k|` exactly | 0 | 0 | **0** |
41: | L2 | square | `1/sqrt2` | `D_4` (8) | `alpha`, anisotropic | 0 | `-n1^2 n2^2/12 = -(1 - cos 4θ)/96` | `-1/96` |
42: | L6e | square | `1/sqrt2` | `D_4` (8) | `alpha`, anisotropic | 0 | identical to L2 | `-1/96` |
43: | L3 | BCC | `1/sqrt3` | `O_h` (48) | `alpha`, anisotropic | 0 | `-sigma2/18 = -1/90 + K4/36` | `-1/90` |
44: | L5a | BCC | `1/sqrt3` | 24, `T_d` | `beta`, anisotropic | `(sqrt3/3) n1 n2 n3` | `-sigma2/18 - n1^2 n2^2 n3^2/6` | `-4/315` |
45: | L5b (each Weyl block) | BCC | `1/sqrt3` | 24, `T_d` | `beta`, anisotropic | `±(sqrt3/3) n1 n2 n3` | as L5a | `-4/315` |
46: | L4 | cube | `1/sqrt3` | 24, `T_d` | `beta`, anisotropic | `-(sqrt3/3) n1 n2 n3` | as L5a | `-4/315` |
47: | L3s4 (each cluster) | BCC, `s = 4` | `a/sqrt3` | 8 (`D_2` half-turns and the `x <-> z` swap composed with them) | `beta`, isotropic + anisotropic | `±[sqrt3 (1-a^2)/(6a) + sqrt3 (2a^2-1)/(3a) n1 n2 n3]`, upper sign for the cluster at `+pi/4` | non-cubic content (Sec. 3.4) | `2(27a^4 - 34a^2 + 5)/(315 a^2)` |
48: | L6a | hexagon | `1/2` | `D_3` (6) | `beta`, anisotropic | `-(sqrt15/36) cos 3θ` | `-41/1728 - (5/1728) cos 6θ` | `-41/1728` |
49: | L6c | hexagon | `3/4` | `D_6` (12) | `alpha`, isotropic | 0 | `-1/512` | `-1/512` |
50: | L6d | hexagon | `3/4` | `D_6` (12) | `alpha`, isotropic | 0 | `-1/128` | `-1/128` |
```

## theory/C_ACROSS_LATTICES_GATE.md, l. 72–87
```
72: | Id | d | Source label | Source, equations, page | s |
73: | --- | --- | --- | --- | --- |
74: | L1 | 1 | line `{±1}` | standard battery (done) | 2 |
75: | L2 | 2 | square, `N_2={(±1,±1)/sqrt2}` | P17 / standard battery (done massless) | 2 |
76: | L3 | 3 | BCC, `N_3` | P17 / standard battery (done) | 2 |
77: | L3s4 | 3 | BCC, `N_3` | S4 family (done) | 4 |
78: | L4 | 3 | Z^3, `C_micro=[-1,1]^3` | CJWW `2408.02108v1` (5.12), (5.15) (done in part) | 2 |
79: | L5a | 3 | BCC via axis product | Farrelly–Short `1312.2852v1` Eqs. (20)–(21) p.4–5 | 2 |
80: | L5b | 3 | BCC via axis product | Mlodinow–Brun `1802.03910v1` Eq. (23) p.5, symbol Eq. (33) p.7, `Delta P_i`, `Q` mutually anticommuting involutions (Eqs. (25)–(27) p.6); mass `theta` | 4 |
81: | L6a | 2 | honeycomb | ADMP `1803.01015v2` Eq. (10) p.3 (coin `W` Eq. (9), axes Eq. (4)) | 2 |
82: | L6b | 2 | triangular | ADMP `1803.01015v2` Eq. (12) p.4 (source: equivalent to L6a over three updates) | 2 |
83: | L6c | 2 | equilateral triangular, six-step | JDW `1803.01304v1` Eq. (2) p.2, `U(·)` Eq. (1) p.1, neighbours p.1 | 2 |
84: | L6d | 2 | equilateral triangular, three-step | JDW `1803.01304v1` Eq. (4) p.2 | 2 |
85: | L6e | 2 | isosceles triangular, three-step | JDW `1803.01304v1` Eq. (6) p.2 | 2 |
86: | L6f | 2 | honeycomb, three-step | JDW `1803.01304v1` Eqs. (7)–(8) p.2 | 2 |
87: 
```

