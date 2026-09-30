<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ b817ac0; lo que sigue a la cabecera es la respuesta sin editar)
modelo: deepseek-v4-pro, esfuerzo: por defecto de la API, vía: API api.deepseek.com/chat/completions, sin herramientas
inicio: 2026-09-30T10:37:30Z  fin: 2026-09-30T10:41:23Z
documento: /home/ignac/qca-causal-cones/theory/W6_FULL_SPATIAL_TETRAD_GATE.md ; último commit: 318fff2 ; sha256 b5eef47f0377dfaa9fc6a7439fcb757f2a70f338f0062b97a174301bb22c1ceb
documento: /home/ignac/qca-causal-cones/theory/W12_FOUR_SPECIES_METRIC_UNIVERSALITY_GATE.md ; último commit: 2ff88b2 ; sha256 24fc0f507bfa82d6054293814da9c883a1fbcdd09f7c1204b2a789c6ecb66474
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w12-four-species-metric-universality.md ; último commit: 5485cb0 ; sha256 efc00217914112c324e4b919df6b3dddb8b535b151b0bf6dbd50756d5695b324
documento: /home/ignac/qca-causal-cones/scripts/verify_w12_four_species_metric_universality.py ; último commit: 5485cb0 ; sha256 dc17823a267a0085ec10f030e6e1bade738fbf91c95a3e119bf009fbbdbbcc73
documento: /home/ignac/qca-causal-cones/debates/2026-09-30--w12-blind-review/cjww_walk_definition.md ; último commit: sin versionar ; sha256 9ed70fe0ffd964d012a0f9a1013740942a126339ec598b7c1322d8522fc48417
entrada_deepseek.txt sha256 59dd88997890c404fb34c7a6cae04ef2daa86d49d1945a51cfd7e8dd664e09aa
respuesta sha256 d01205ebca7a93a66f4d25fb0bc557bd8aed866abde6b3da29400180fac0cd8d
-->

1. **Setting.**  
The report follows the frozen W12 contract. The four decisive nodes are exactly the `+I` set
\((0,0,0),(1,1,0),(1,0,1),(0,1,1)\); the `−I` nodes are only diagnostic. Coordinates are held
common; ranks are computed on the coefficient of \(g\) with the nine real \(z_{ar}\) as variables;
both product orders \(W_0(I-igJ)\) and \((I-igJ)W_0\) are checked. The direction matrix \(D\) is
used with rows \(d_1,d_2,d_3\), as in W6. No contract deviation is found.

2. **Derivation.**  
Let \(p_*=\pi b\), \(\sigma_i=(-1)^{b_i}\), and \(s_*=(-1)^{b_1+b_2+b_3}\). The flat walk satisfies
\(W_0(p_*)=s_*I\). Expanding \(W_0\) gives the frame
\[
E_*=\operatorname{diag}(\sigma_2\sigma_3,-\sigma_3,1),
\]
which matches the report and the W11 table.

For the control symbol,
\[
J^{(a,r)}(p_*+k)=2\sin((p_*+k)\cdot d_r)\sigma_a
=2\tau_r(k\cdot d_r)\sigma_a+O(|k|^3),
\]
where
\[
\tau_r=\cos(p_*\cdot d_r)=(-1)^{b\cdot d_r}.
\]
Thus
\[
J(p_*+k)=2\sigma^a (Z\operatorname{diag}(\tau)D k)_a+O(|k|^3).
\]
Using \(s_*W_g(p_*+k)=I+i\sigma^a(E_*+\delta E_*)_a{}^i k_i+\cdots\), one obtains
\[
\frac{\delta E_*}{g}=-2Z\operatorname{diag}(\tau)D.
\]
Therefore
\[
\frac{\delta h_*}{g}
=
E_*^T\frac{\delta E_*}{g}+\frac{\delta E_*^T}{g}E_*
=
-2\Big[E_* Z\operatorname{diag}(\tau)D
+D^T\operatorname{diag}(\tau)Z^T E_*\Big].
\]
I find no sign or factor error. The report’s statement that the two product orders agree at
\(O(gk)\) is also correct: \(J(p_*)=0\), and the first derivative only sees \(\partial J\).

3. **Linear algebra.**  
For the `+I` nodes, \(s_1s_2s_3=1\), so
\[
E_*=\operatorname{diag}(s_1,-s_3,1),\qquad
\operatorname{diag}(\tau)=(s_1,s_3,1).
\]
Writing the metric components explicitly gives, at every `+I` node,
\[
\begin{aligned}
(\delta h/g)_{11}&=-4(Z_{11}+s_2Z_{12}+s_1Z_{13}),\\
(\delta h/g)_{22}&=4(Z_{22}+s_3Z_{23}),\\
(\delta h/g)_{33}&=-4Z_{33},\\
(\delta h/g)_{12}&=-2[s_2Z_{12}+s_1Z_{13}-s_2Z_{21}-Z_{22}-s_3Z_{23}],\\
(\delta h/g)_{13}&=-2[s_1Z_{13}+s_1Z_{31}+s_3Z_{32}+Z_{33}],\\
(\delta h/g)_{23}&=-2[-s_3Z_{23}+s_3Z_{32}+Z_{33}].
\end{aligned}
\]
Requiring these to be identical for all four sign patterns forces
\[
Z_{12}=Z_{13}=Z_{23}=Z_{21}=Z_{31}=Z_{32}=0.
\]
Hence
\[
\mathcal U=\operatorname{span}\{e_{11},e_{22},e_{33}\},\qquad \dim\mathcal U=3,
\]
and \(\Phi\) has rank \(9-3=6\).

On \(\mathcal U\), writing \(a=z_{11}, b=z_{22}, c=z_{33}\),
\[
\frac{\delta h_*}{g}
=
\begin{pmatrix}
-4a&2b&-2c\\
2b&4b&-2c\\
-2c&-2c&-4c
\end{pmatrix}
\]
at every `+I` node. In the ordered metric components
\((h_{11},h_{22},h_{33},h_{12},h_{13},h_{23})\), the restricted map is
\[
\begin{pmatrix}
-4&0&0\\
0&4&0\\
0&0&-4\\
0&2&0\\
0&0&-2\\
0&0&-2
\end{pmatrix},
\]
whose rank is \(3\). The three independent missing directions are correctly reported:
\[
(\delta h/g)_{12}=\tfrac12(\delta h/g)_{22},\quad
(\delta h/g)_{13}=\tfrac12(\delta h/g)_{33},\quad
(\delta h/g)_{23}=\tfrac12(\delta h/g)_{33}.
\]
Setting \(\delta h=0\) at all four `+I` nodes forces all nine \(z_{ar}\) to vanish, so the common
frame-rotation kernel is zero. The report’s U5 statement is therefore correct.

4. **Certificate.**  
The script actually checks:

- U1: extracts all eight frames from `walk2()` and compares with the W11 formula.
- U2: differentiates both product orders symbolically and checks equality with
  \(-2Z\operatorname{diag}(\tau)D\).
- U3: builds the exact \(18\times 9\) coefficient matrix of \(\Phi\), computes its rank and
  nullspace, and asserts the nullspace basis is \(e_{11},e_{22},e_{33}\).
- U4: computes the metric map at the reference `+I` node, restricts it to \(\mathcal U\), asserts
  the exact restricted matrix, and counts the left-nullspace relations.
- U5: computes the common metric map on all four `+I` nodes and asserts its kernel is empty.
- U6: checks \(W_g|_{g=0}=W_0\).

This matches the report’s substantive claims. Two minor caveats: the exact three missing
relations are printed from a nullspace computation but are not separately asserted in the script;
and the terminal-state `if/elif` logic would not correctly classify a hypothetical case
\(\Phi=0\) with \(\operatorname{rank}(\text{metric}|_{\mathcal U})<6\). Neither affects the
present verdict.

5. **Robustness of the negative conclusion.**  
Within the contract’s rules the negative conclusion is robust. A global sign change of \(g\) or
\(\delta E\) changes \(\delta h\) by a global sign, so ranks and kernels are unchanged. Changing
the reference node replaces the rows of \(\Phi\) by an invertible linear combination, so
\(\ker\Phi\) and the restricted rank are unchanged; moreover on \(\mathcal U\) the metric
perturbation is already identical at all four `+I` nodes. Component ordering and control ordering
do not affect ranks or kernel dimension. Metric index placement is frozen by W6 as \(h=E^TE\);
changing it would be outside the contract. The common-coordinate rule is essential: allowing
species-dependent spatial reflections or redefinitions could alter the sign pattern and is
explicitly forbidden. Comparing \(\delta h\) at the four nodes is the correct first-order test
of species universality for the metric, since first-order frame rotations cancel in
\(E^T\delta E+\delta E^TE\); the calculation separately checks that no nonzero common
frame-rotation direction appears. Thus the negative result is not a convention artefact under the
frozen rules.

6. **Scope.**  
The report respects the claim ceiling. It states the result is first order in \(g\) and \(k\),
one-particle CJWW (5.15), W6 controls only, and that the `−I` nodes do not decide the verdict.
It explicitly disclaims higher orders, interacting walks, dynamics, backreaction, constraints and
gravitational normalization. No overclaim is found.

| Claim | Status | Reason |
|---|---:|---|
| Frozen W12 setting followed | SUPPORTED | Common coordinates, \(+I\) nodes, coefficient of \(g\), both product orders |
| U1 node frames | SUPPORTED | Recomputed from `walk2()`; matches W11 expression |
| U2 induced frames and product order | SUPPORTED | \(\delta E/g=-2Z\operatorname{diag}(\tau)D\); orders agree at \(O(gk)\) |
| U3 \(\dim\mathcal U=3\), rank \(\Phi=6\) | SUPPORTED | Universality forces six off-diagonal controls to vanish |
| U4 rank \(3/6\) and missing relations | SUPPORTED | Restricted matrix and three relations verified |
| U5 no common frame-rotation direction | SUPPORTED | Common \(\delta h=0\) forces all nine controls to zero |
| Certificate matches report | SUPPORTED_WEAKER | Exact missing relations printed but not asserted; terminal logic incomplete only for unused hypothetical |
| Negative result robust under allowed conventions | SUPPORTED | Sign/reference/order changes do not alter rank or kernel |
| Scope and claim ceiling respected | SUPPORTED | Preliminary, first-order, W6/CJWW-only claims stated |

Final verdict: **ACCEPT**.  
No mandatory repairs are required. Optional repairs: assert the three explicit missing relations in the certificate and make the terminal-state branching exhaustive for the unused \(\Phi=0\), rank-deficient case.
