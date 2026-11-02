<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 f2bbd5ed595d9d31eec9783205cc003462bfcfdc82624c4829a5d20d674b4062
inicio: 2026-11-01T22:32:55Z  fin: 2026-11-01T22:33:15Z
documento: /home/adnac/qca-causal-cones/theory/C_ACROSS_LATTICES_GATE.md ; último commit observado: 30672ba ; sha256 de la copia enviada b58deeec91184fbf976a6cb857c8e935ec7d4a4e52d6608a62768452759e34e3
documento: /home/adnac/qca-causal-cones/reports/2026-11-01--c-across-lattices-review.md ; último commit observado: 2c24712 ; sha256 de la copia enviada d886388f7f95f024cb548f6f3d8732b67c590409e90206dd4d63dc4879efd859
documento: /home/adnac/qca-causal-cones/debates/2026-11-01--c-across-lattices-rereview/repair.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 5bd386076abf6a69b783b8bbd2475806f8e4dcddb3ffbca929243d3085b96816
documento: /home/adnac/qca-causal-cones/reports/2026-11-01--c-across-lattices.md ; último commit observado: 8d0276e ; sha256 de la copia enviada 01a18c70a1b031e99ca4f944c9f6810f29b1327067138c8eb3ee089deca1ea3f
documento: /home/adnac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
entrada_gemini.txt sha256 28f6c9ded4da3a99f308e5c6f5ad7dc48652196bf54b9a40f11235b647f09a27
respuesta sha256 313f5797f1a0c5b77f9f05aea623afd7c61c408374f2fbf823916db27a4af571
-->

### Dictamen por punto

**R1. Asertos de tabla: PASS**
Cada valor tabulado en el informe para las filas computadas está ahora cerrado mediante una llamada exacta a `record()` en `scripts/verify_c_across_lattices_gate.py`, garantizando que el proceso falle (exit 1) si algún valor discrepa:
- **Conjuntos de pasos ($F$) e índices:** `EXPECTED_F` cierra los conjuntos compuestos de L6a y L6c–L6f (mientras que L5a y L5b ya estaban cerrados en `row_L5a` y `row_L5b` frente a $\{\pm 1\}^3$). `EXPECTED_INDEX` cierra los índices del subgrupo de traslación generado por $F$ para todas las filas nuevas (4 para BCC/L5a/L5b, L6a, L6d, L6e; 1 para L6c; 3 para L6f). En las coordenadas de generadores declaradas, los conjuntos de `EXPECTED_F` corresponden exactamente a la geometría descrita en la Tabla 3 (hexágono de radio 2 para L6a/L6d, bola hexagonal de 19 puntos para L6c, los 4 puntos $(\pm 1, \pm 1)$ cartesianos para L6e y el hexágono rotado de radio $\sqrt{3}$ con origen para L6f).
- **Cantidades sin masa ($r_{\text{in}}$, $c_0$, número de vértices):** `EXPECTED_MASSLESS` afirma exactamente los valores de la Tabla 4 para L1, L2, L5a, L5b, L6a y L6c–L6f (y la supervivencia de todos los vértices junto con $c_{\text{strict}}^{\text{iso}} = r_{\text{in}}$ queda cerrada por `all_survive`).
- **Matrices de Gram y corrección de curvatura ($K$):** En `part3`, `exp_g` y `exp_K` verifican elemento a elemento (vía `is_zero_matrix`) las matrices de Gram normalizadas y los tensores matriciales $K_{ab}$ para L5b y L6c–L6f, además del control positivo Dirac 1D. Aunque el bucle de afirmación de $K$ recorre las claves $(0,0), (0,1), (1,1)$ (y $(0,2), (1,2), (2,2)$ en 3D), la simetría $K_{ab} = K_{ba}$ está garantizada analíticamente porque provienen de las segundas derivadas parciales conmutativas de $G(k)$. Todos los valores coinciden exactamente con la Tabla 5.
- **No tautología:** Ningún aserto nuevo es tautológico; todos comparan resultados extraídos simbólicamente de los símbolos de Bloch y la geometría convexa contra constantes explícitas predeclaradas.

**R2. Orden del producto: PASS**
En la Sección 2 del informe («Control against the sources») y en el docstring del verificador se ha eliminado la afirmación de que reproducir la velocidad continua de las fuentes valide el orden del producto. Se explica explícitamente que, dado que cada factor cumple $W_j(0) = I$, el término lineal es la suma de las derivadas de los factores y por tanto independiente del orden; y se declara que el orden en $\prod_j$ para JDW Eqs. (2) y (8) es una lectura declarada de la que sí pueden depender $K$ (Sección 5) y los coeficientes de los vértices de L6c y L6f.

**R3. Tokens Hb/Hc: PASS**
Tanto en la tabla de la Sección 6 del informe como en `part2` del verificador se ha retirado el token `CONFIRMED_IN_DECLARED_ROWS` para Hb y Hc. El informe los declara como **OPEN** porque la fila declarada L6b está sin decidir (no codificada), haciendo constar con precisión que ambas hipótesis se cumplen en todas las filas decididas (computadas y registradas).

**R4. Aclaraciones: PASS**
- **Identidad de Duhamel:** La Sección 5 del informe y los comentarios de la Parte 3 del código incluyen ahora el factor unitario correcto: $i\, dU\, U(0)^\dagger = X_{\text{par}} + (\sin\theta/\theta) X_{\text{perp}} e^{i\theta Q}$. Se explica claramente que el verificador construye $B_a = X_{\text{par}} + X_{\text{perp}} e^{i\theta Q}$ y que, tras verificar $X_{\text{par}} = 0$, $B_a$ es hermítico, anticonmuta con $Q$ y satisface $\{B_a, B_b\} = \{X_a, X_b\}$, por lo que su matriz de Gram coincide exactamente con la de $dH$ sin alterar ningún número tabulado.
- **Grupo fino de L6c:** La Sección 3 distingue ahora entre las **dos** formas de $C_{\text{micro}}$ en 2D (cuadrado y hexágono) y los **tres** sustratos al contar también el grupo de traslación, separando el grupo triangular más fino de L6c (índice 1, razón espaciado/radio $1/2$).
- **Signo de Fourier $k \to -k$ y docstring:** La Sección 2 documenta la convención $k \to -k$ respecto a la onda plana de JDW y su inocuidad sobre las cantidades pares tabuladas. El docstring del script describe ahora las Partes 1, 2 y 3, y el print de resumen de la Parte 3 etiqueta `iso_W` con precisión como `K = 0 (isotropic c_omega2)`.

**R5. Regresiones: PASS**
El diff es limpio, acotado a las reparaciones y aclaraciones solicitadas, no altera la física ni los cálculos ya aceptados en los bloques 1–5 y mantiene todas las conclusiones dentro de los límites estrictos del contrato congelado.

---

### Dictamen global

**PASS.** No hay reparaciones obligatorias.
