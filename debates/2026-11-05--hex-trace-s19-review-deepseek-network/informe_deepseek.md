<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 afbf014ff8ad09fa44a3d6ce8f9d2638ac6fd4b3744fb5c2341742c87afc37e3
inicio: 2026-11-05T09:16:25Z  fin: 2026-11-05T09:37:21Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-s19.md ; último commit observado: sin versionar ; sha256 de la copia enviada 7ce0e1cec365c24ec6b8ca16f20c7c29db48dc2a33f7170b3537ba6b54f52cb4
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_trace_s19.py ; último commit observado: sin versionar ; sha256 de la copia enviada 00505fe6fa67d579e1b5d3bb98dec34264939c37b407ef8b08d3d3959590e959
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
entrada_deepseek.txt sha256 de612d487c509b9c958d7b9642911fc8440b1486c221e7706322755ca5b803b3
respuesta sha256 9b7a8d44d95134b37f9c9017d0cc71da58b570950e9e00bf1e1f74ae1fc4975c
-->

## Overall verdict: PASS

The scalar proof is valid for the stated bounded-support class (`F \subset S19`, exact regular hexagonal hull of radius one, `s=2`, node, isotropic cone). The algebraic reductions and both contradiction points check out by direct hand derivation. I found no mandatory repair.

---

### (1) Phase and trace bound — PASS

After scalar phase removal, `U(0)=I` is legitimate and does not change `F` or `c_0`.

For any unitary `2x2` matrix with eigenvalues `e^{i\theta_1}, e^{i\theta_2}`,

```
f(k) = Re Tr U(k)/2 = (cos theta_1 + cos theta_2)/2
```

so indeed `-1 <= f(k) <= 1`, and `f(0)=1`.

The support of `f` is contained in `F ∪ (-F)`, because

```
Re Tr U(k) = 1/2 sum_h ( tr A_h e^{-ik·h} + overline{tr A_h} e^{ik·h} ).
```

Since `S19 = -S19`, this support remains in `S19`.

---

### (2) Orbit averaging and preservation of normal rigidity — PASS

The coordinate action used by the verifier is correct:

```
rotate(a,b) = (-b, a+b)
reflect(a,b) = (a+b, -b)
```

These are the 60-degree rotation and a reflection for the normalized lattice coordinates.

The three nonzero D6 orbits have representatives

```
(1,0), (1,1), (2,0)
```

and all have size 6. The corresponding orbit cosine sums are exactly `S1,S2,S3`.

Averaging `f` over D6 and over `k -> -k` preserves:

- the global bounds `[-1,1]`,
- the support inside `S19`,
- the value `fbar(0)=1`.

The normal-line restriction is also preserved. If `n` is a facet normal and `R` is any D6 element, then `R n` is another facet normal. At saturation `c_0 = r = sqrt3/2`, the rigidity input gives

```
U(t n) = e^{-irt} P_+(n) + e^{irt} P_-(n)
```

with rank-one projectors, so

```
f(t n) = cos(rt).
```

Hence every term in the D6 average along a normal line equals the same `cos(rt)`, and therefore `fbar` does too.

The analytic rigidity input from HEX_CEILING Step 1 is applicable beyond minimal support. The equality case argument is classical and valid: from `c_0 = r_in`, the scalar Bernstein equality case forces the diagonal matrix element to be an extreme Fourier character, and Cauchy–Schwarz then forces the full `U(tn)` to have the two-projector form. Interior layers do not affect the argument.

One small presentation caveat: for `S19` one should view the support as lying in the refined lattice `Λ/2`, so the integer-layer version of the HEX_CEILING Step 1 applies verbatim. This is implicit in the integer coordinates `(a,b)`, but could be stated explicitly.

---

### (3) Normalization and Fourier orbits — PASS

The set

```
S19 = { (a g1 + b g2)/2 : max(|a|,|b|,|a+b|) <= 2 }
```

has exactly 19 points: the origin, six points in orbit `(1,0)`, six in orbit `(1,1)`, and six vertices in orbit `(2,0)`.

The physical length squared is

```
| (a g1 + b g2)/2 |^2 = (a^2 + ab + b^2)/4
```

and the maximum over `S19` is `1`, at the six vertices.

With

```
p = k·g1/2, q = k·g2/2,
```

the orbit sums are:

```
S1 = 2[cos p + cos q + cos(p-q)]
S2 = 2[cos(p+q) + cos(2p-q) + cos(p-2q)]
S3 = 2[cos 2p + cos 2q + cos 2(p-q)].
```

I re-derived all three and they match the orbit sums.

For the facet normal `n = (0,1)`, we have

```
k = t n => p = 0, q = sqrt3 t / 4,
```

so

```
r t = sqrt3/2 * t = 2q
```

and therefore

```
fbar(0,q) = cos(2q).
```

The other facet-normal lines are indeed `q=0` and `p=q`.

---

### (4) One-parameter reduction and P/Q inequalities — PASS

At `p=0`:

```
S1 = 2 + 4 cos q
S2 = 4 cos q + 2 cos 2q
S3 = 2 + 4 cos 2q
```

So

```
fbar(0,q) = (a0 + 2a1 + 2a3) + (4a1 + 4a2) cos q + (2a2 + 4a3) cos 2q.
```

Equating this with `cos 2q` gives:

```
a2 = -a1
a3 = (1 + 2a1)/4
a0 = -1/2 - 3a1
```

which is exactly the claimed one-parameter family.

At

```
P = (pi/3, 2pi/3)
```

the orbit sums are

```
(S1,S2,S3) = (1,-2,-3)
```

so

```
fbar(P) = -5/4 - 3a1/2.
```

The bound `fbar(P) >= -1` gives

```
a1 <= -1/6.
```

At

```
Q = (2pi/3, 4pi/3)
```

the orbit sums are

```
(S1,S2,S3) = (-3,6,-3)
```

so

```
fbar(Q) = -5/4 - 27a1/2.
```

The bound `fbar(Q) <= 1` gives

```
a1 >= -1/6.
```

Hence

```
a1 = -1/6
```

and therefore

```
fbar = (S2 + S3 - S1)/6.
```

This is correct.

---

### (5) Both exact contradiction points — PASS

With the candidate

```
fbar = (S2 + S3 - S1)/6
```

at

```
C = (3pi/5, 3pi/10)
```

I re-derived the trigonometric values.

At `C`:

```
p = 3pi/5, q = 3pi/10
p-q = 3pi/10
p+q = 9pi/10
2p-q = 9pi/10
p-2q = 0
2p = 6pi/5
2q = 3pi/5
2(p-q) = 3pi/5
```

So:

```
S2 = 2(1 + 2 cos(9pi/10)) = 2 - 4 cos(pi/10)
S3 = -2 cos(pi/5) - 4 cos(2pi/5)
S1 = -2 cos(2pi/5) + 4 cos(3pi/10)
```

Using

```
cos(pi/10) = sqrt(10+2sqrt5)/4
cos(pi/5) = (1+sqrt5)/4
cos(2pi/5) = (sqrt5-1)/4
cos(3pi/10) = sqrt(10-2sqrt5)/4
```

one gets

```
S2+S3-S1
= 2 - sqrt5 - sqrt(20+8sqrt5).
```

Thus

```
fbar(C) = (2 - sqrt5 - sqrt(20+8sqrt5))/6.
```

Since `sqrt5 > 2` and `20+8sqrt5 > 36`, we have

```
sqrt(20+8sqrt5) > 6
```

and therefore

```
2 - sqrt5 - sqrt(20+8sqrt5) < -6.
```

So

```
fbar(C) < -1,
```

which is the desired contradiction.

The second contradiction point is also correct. On `p=2q`, with `x = cos q`,

```
(S2+S3-S1)/6 = (8x^4 + 8x^3 - 6x^2 - 8x + 1)/3.
```

At `x = 3/5`:

```
(8x^4 + 8x^3 - 6x^2 - 8x + 1)/3 = -1997/1875 < -1.
```

So either point suffices.

---

### (6) Scope and verifier coverage — PASS

The proof is correctly scoped: it proves non-attainment `c0 < r` for the stated `S19`-bounded class, not for all hexagonal supports and not for general `s > 2`.

The verifier covers the algebraic steps independently:

- support enumeration,
- D6 orbit decomposition,
- orbit sums,
- normal-line coefficient reduction,
- P/Q affine values and inequalities,
- candidate reduction,
- C radical value,
- second polynomial contradiction.

It does not mechanize the analytic unitarity/averaging/rigidity bridge, but that bridge is stated in the report and I audited it above. This is not a mathematical defect for this proof format.

---

## Mandatory repairs

None.

## Optional clarity improvements

1. Explicitly state that a regular hexagon of circumradius 1 contained in `S19` must be a D6 conjugate of `S19`; this makes the identification of facet-normal lines `p=0`, `q=0`, `p=q` fully explicit.

2. When invoking HEX_CEILING Step 1 for `S19`, explicitly say that the support is viewed in the refined lattice `Λ/2`, so the integer-layer version of the rigidity lemma applies unchanged.

3. The exact radical inequality could be made even more verifier-explicit by proving  
   `8 - sqrt5 < sqrt(20+8sqrt5)`  
   through squaring rather than relying on SymPy’s relational evaluation of radicals. The report text already gives the exact argument.

4. The Julia-lemma/Bernstein equality-case citation in the underlying HEX_CEILING report is marked `[UNVERIFIED]`. For a standalone promoted proof, it would be better to either include the short equality-case proof in-repo or add a primary source page. Mathematically, the step is valid.
