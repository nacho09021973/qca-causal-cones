<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 033e5f09349941cd68bb7bbd8935cdaeef2d985272b8fd03e81e6ae890555b0d
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-05T12:55:36Z  fin: 2026-11-05T13:05:47Z
documento: /home/ignac/qca-causal-cones/theory/PH_REFUTATION_HEX_S25_GATE.md ; último commit observado: 6eb50c1 ; sha256 de la copia enviada 53567f77a539541e0539243d9b36fd519dff7222e41fa953247ec7f1dec0ac55
documento: /home/ignac/qca-causal-cones/scripts/verify_ph_refutation_hex_s25_gate.py ; último commit observado: 7e7bf7d ; sha256 de la copia enviada ddf853866d1e249b9de3689030e85d4477bfe310a6bf0b0cc7a22b3f8567e10e
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--ph-refutation-hex-s25.md ; último commit observado: 7e7bf7d ; sha256 de la copia enviada d3c9a92c9d5b7545945ed940c7da83ca58380e2754bf11a00dfc455acc95f464
documento: /home/ignac/qca-causal-cones/debates/2026-11-05--ph-refutation-hex-s25-review-grok/salida_verificador.txt ; último commit observado: sin versionar ; sha256 de la copia enviada d5389b99d1f8656049422b3f82296450ccd09c041a077204382ef5496b7f4f15
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_s25_review.py ; último commit observado: da49c00 ; sha256 de la copia enviada 010fa7fb805710baa80932a2538195c28041de741434a2e0cf05877d6ac09b7a
documento: /home/ignac/qca-causal-cones/debates/2026-11-05--ph-refutation-hex-s25-review-grok/salida_verificador_geometria.txt ; último commit observado: sin versionar ; sha256 de la copia enviada a092240a17550f72f82b1f2e8cf39cfa93634e5d3c8db6e1e65d8232432e51d2
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_supremum_gate.py ; último commit observado: 8abca3c ; sha256 de la copia enviada ef4b0114124d16937ced9a600a65b229c6fd968ab417d8493d1297806bf46a55
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_supremum_b19.py ; último commit observado: 6302328 ; sha256 de la copia enviada 244bb1065a7a0f76edc890637e289bda94b8477b3a1488792185e7e7c07cbb7a
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_ceiling_gate.py ; último commit observado: bb4fcdb ; sha256 de la copia enviada 8f3b7a10ecee91c515429640b794da91e2c0e273176f5bbbd62e56a0f3b43d72
documento: /home/ignac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--hex-supremum.md ; último commit observado: 677bec0 ; sha256 de la copia enviada 177d94d3e6991fb45fddadad218dd05c4ce7c0011419c481a2c94c5acccf0c88
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
entrada_grok.txt sha256 0599eecbc2ff0941345fea32559d5067cfacb5e399596b88e95af363759ae2d1
respuesta sha256 6d5ad294f5e798131bc633d4321b70f104a4b629e32a5c7f07313bb1e6562cd4
-->

La prueba de no saturación para `conv F = H25` (y `H25′`) es correcta. El hueco cualitativo en `W_hex^sym`, y por tanto en `W_hex`, se sigue de la rigidez en las rectas de faceta, del lema A1 y del certificado ya revisado de T2, sin usar la forma de producto. No he ejecutado código: la geometría y la reducción están rederivadas a mano; el discriminante `−1/12` es el certificado heredado de `check_T2_minimal`, no recalculado aquí.

## 1. SOPORTE — PASS

El verificador del contrato, `check_support` en `verify_ph_refutation_hex_s25_gate.py`, certifica las cuatro propiedades geométricas de H25, y la rederivación coincide.

Generadores `g1 = (1,0)`, `g2 = (1/2, √3/2)`, norma `a²+ab+b²`. El vértice `v = 2g1+g2` tiene norma 7. Los enteros de Eisenstein de norma ≤ 7 son 31; la otra órbita de norma 7, la de `(3,−1)`, cae fuera de las desigualdades del hexágono. Quedan 25 puntos: el origen, las órbitas de norma 1, 3 y 4 (6+6+6) y los 6 vértices. Con circunradio 1, `r_in = √3/2` vale para todo hexágono regular. El enumerador `a,b ∈ [−5,5]` es holgado: si `|a| ≥ 4`, la norma es al menos 12.

Cada arista es el giro de 60° del vector `(−3,2)`, de coordenadas coprimas, así que no hay puntos de red en el interior. El chequeo del verificador (producto cruzado nulo contra el resto de los 25) es más débil en el enunciado, pero equivalente: la recta de una arista corta al hexágono convexo exactamente en esa arista.

La reflexión `y → −y` es simetría de la red: en coordenadas, `(a,b) ↦ (a+b,−b)`, y manda `(2,1)` a `(3,−1)`, que está en la órbita de `(1,2)`. `H25′` es esa imagen. El mismo conteo y el mismo A1 se aplican directamente a `H25′`.

Los únicos hexágonos de red centrados contenidos en H25 son S7, S13 y S19, de vértices `(1,0)`, `(1,1)` y `(2,0)`. Toda órbita bajo el giro de 60° de un punto de los 25 queda dentro, y no hay más órbitas. Por convexidad, el hexágono está dentro si y sólo si lo están sus vértices. Un walk con `F ⊂ H25` y envolvente S7, S13 o S19 ya está decidido; lo nuevo es `conv F = H25` o `H25′`.

Esa clasificación no la comprueba el verificador del contrato. La comprueba `verify_hex_s25_review.py` (órbitas y productos cruzados enteros). El contrato, sección 2, la lista entre los hechos a certificar. No es premisa del hueco para `conv F = H25`: el informe no la usa como lema. Aclaración, no error.

## 2. CAPAS Y LEMA A1 — PASS

La rejilla `δ = r_in/7` es exacta. Sin normalizar, la arista tiene longitud `√7` y `h · Rot90(d) = (√3/2)(2a+3b)`; el espaciado es `√3/(2√7)` y el inradio `√21/2`, cociente 7. Al normalizar, el cociente no cambia. La forma `2a+3b` recorre niveles enteros de −7 a 7.

Tamaños de esa normal, de +7 a −7, contados sobre los 25 puntos:

`2, 1, 1, 2, 1, 2, 2, 3, 2, 2, 1, 2, 1, 1, 2`

Suman 25. Los extremos ±7 son las dos parejas de vértices consecutivos `(2,1),(−1,3)` y `(−2,−1),(1,−3)`. El giro de 60° conserva el soporte y permuta las tres normales, así que las otras dos normales repiten la tabla. Hay seis capas intermedias unitarias por normal.

Esas unitarias son, en la primera normal, `(0,2)`, `(1,1)`, `(0,1)`, `(0,−1)`, `(−1,−1)`, `(0,−2)`. Sus giros cubren, sin solapes y sin tocar el origen ni los vértices, las tres órbitas de seis puntos. Son exactamente los 18. La rigidez (techo hexagonal, sección 3, paso 1: igualdad de Bernstein / Julia, con `P'(1) = 0`) dice que toda capa intermedia suma 0; una capa de un solo punto obliga a `A_h = 0`. Eso no depende de que el punto estuviera de antemano en `F`: si `conv F = H25`, el soporte está entre los 25, y la saturación expulsa esos 18.

La segunda vía resuelve el sistema lineal de todas las capas. No es independiente: cada unitaria ya es la ecuación `A_h = 0`, y las capas dobles intermedias son pares de esos 18, redundantes una vez anulados. El propio verificador lo dice («not independent of A1»). Queda el sistema de T2 sobre `{0} ∪ vértices`, que es compatible. La declaración es correcta.

La simplificación de normales no afecta a la parte 2. Las unitarias y la rejilla se calculan con las normales sin simplificar. Los radicales `(√21/7, 2√7/7)`, `(−√21/14, 5√7/14)` y `(−3√21/14, √7/14)` son exactamente `atan(√3/5)+π/6` y sus giros, y tienen norma 1. Sólo reescriben los proyectores de la segunda vía.

Aclaración: la etiqueta «the two extreme layers of each normal are the two vertices of an edge» está en

```python
all(s[0] == 2 and s[-1] == 2 for s in table)
```

y eso sólo mira el cardinal. El hecho es cierto por los niveles ±7 de arriba; tras el giro, `check_T2_minimal` sí comprueba que la cara superior es la arista de vértices adyacentes 0 y 1. No hace falta repararlo para el hueco.

## 3. REDUCCIÓN A T2 — PASS

El giro espacial de `−atan(√3/5)` es lícito. El primer vértice normalizado tiene ese argumento, y los otros están a `k·60°`. El conjunto cae sobre `(cos kπ/3, sin kπ/3)`. `atan(√3/5)` no es simetría de la red; no hace falta que lo sea. T2 no usa la red: `check_T2_minimal` coloca siete puntos abstractos, impone las sumas de capa de la saturación y la unitariedad por los dos lados, y no hay factorización en producto. Las diferencias `h−h'` y las capas se transportan por cualquier isometría. El giro de Bloch alrededor de `z`, hecho a la vez, conjuga `A(n) = r n·σ` en el plano `xy` y conserva unitariedad, nodo e isotropía. Lo mismo, con su propio ángulo, para `H25′`.

El certificado usa la geometría de esos siete puntos, la unitariedad y, a través de la forma normal y de los proyectores, el nodo y la isotropía. Cubre todo walk `s = 2` con `F ⊆ {0} ∪ vert(H)`, con o sin forma de producto. Como A1 mete cualquier soporte de envolvente H25 dentro de ese conjunto, no queda ningún walk de `W_hex` ni de `W_hex^sym` con `conv F = H25` fuera del argumento. Las aristas sin puntos interiores hacen que la cara extrema sea sólo los dos vértices, que es la hipótesis de T2.

## 4. CONTROLES — PASS

Los controles del cuadrado de M1-B19, reejecutados tal cual, son los que el contrato pide («as in M1»): las sumas de capa, y de hecho también L2 y L3, no expulsan el walk saturante del cuadrado. Son pertinentes como control de la maquinaria importada, no como prueba del paso unitario. En el cuadrado de cuatro vértices no hay capa intermedia; en el 3×3 las capas son de tamaño 3. El informe lo dice con precisión: «A1 itself has no nontrivial instance on the square substrate … this control tests the layer equations, not the singleton step as such.» El control del método de T2 en el cuadrado está en `check_T2_square_control` y no se relanza; no es una afirmación falsa del informe.

## 5. DICTÁMENES Y ALCANCE — PASS

`PROVED_FOR_S25` está bien usado: no hay walk `s = 2` de `W_hex^sym`, luego tampoco de `W_hex`, con `conv F = H25` o `H25′` y `c_0 = r_in`. El hueco es cualitativo. `NOT_REFUTED_ON_H25` es el token del contrato: un hueco en un soporte no refuta (PH⇒) y no es `CONFIRMED`. `CONFIRMED_FOR_S25` es el token de HX2 para este soporte. La sección 5 limita el resultado a H25 y H25′, deja la clase hexagonal abierta, niega valor de evidencia para (PH) fuera de H25 y marca el parecido con S13 como no afirmado. No hay walk con `conv F = H25` que el argumento no cubra.

## Dictamen global

**PASS.** No hay reparaciones obligatorias. Las dos aclaraciones (la clasificación S7/S13/S19 no está en el verificador del contrato; la etiqueta de las capas extremas sólo comprueba el cardinal) no entran en la cadena del hueco.
