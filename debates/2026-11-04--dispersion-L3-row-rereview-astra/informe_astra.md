<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.1-sol, esfuerzo: high, vía: codex exec sellado (codex-cli 0.166.0)
inicio: 2026-11-04T12:30:54Z  fin: 2026-11-04T12:33:36Z
documento: /home/ignac/qca-causal-cones/scripts/verify_dispersion_L3_row_gate.py ; último commit observado: 414259c ; sha256 de la copia enviada 89b33e700aedb7ae19bb80e00f45d8452f6a550ba7c836c5d3c246f070adae10
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--dispersion-L3-row.md ; último commit observado: 414259c ; sha256 de la copia enviada 7d08604673825db2aaf3ff0c6f605ef9f5c729fd91cba33da94feed575b6f531
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--dispersion-L3-row-rereview-astra/salida_verificador.txt ; último commit observado: sin versionar ; sha256 de la copia enviada c60be49564e9d06eb0337dbc9fec0b7e2bcb9c500a2d1c97489eacce3f6370f5
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--dispersion-L3-row-rereview-astra/diff_reparacion.txt ; último commit observado: sin versionar ; sha256 de la copia enviada 07b911416b64b1505045a6b220ddd81936c22ce652f8f638a1757dd347904ef7
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--dispersion-L3-row-review-astra/informe_astra.md ; último commit observado: 540e079 ; sha256 de la copia enviada cac6b9b173ae4e513d9f61175ebfae9dadef2cc244c0d289a83dc9afe64f8322
documento: /home/ignac/qca-causal-cones/theory/DISPERSION_L3_ROW_GATE.md ; último commit observado: d3868fa ; sha256 de la copia enviada d47b0ea66663bde73aff660ea0aad2b79a7309ae3d4fd87bb2df7e9a24db0fca
documento: /home/ignac/qca-causal-cones/scripts/verify_dispersion_corrections_gate.py ; último commit observado: 4a45280 ; sha256 de la copia enviada b7c451e213b60a0ae22e5c2ad15630abe5f5f4ee1c7c3d11dc660f43ffdb9a7e
documento: /home/ignac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/ignac/qca-causal-cones/scripts/verify_directional_saturation.py ; último commit observado: 78fcaca ; sha256 de la copia enviada 1d1894730f83ea24808bb5e939492fe2144fdd97cdcf87961a0978da35ae4596
entrada_astra.txt sha256 cf86eecf5e84f3aca0bab7118801d128f0166519e9d92e2366df3d42152381b3
respuesta sha256 9b95c480873c3ccc9b9f90c6d5f2f49cbbb73370d35fc5eb4a56cde37209ef8e
-->

**Dictamen global: PASS. No encuentro reparaciones obligatorias en los cinco puntos solicitados.** La revisión es estática, sobre los documentos adjuntos. La ejecución efectiva, los hashes y la historia de commits quedan **[UNVERIFIED]**; la salida suministrada es coherente con el código y con la derivación algebraica siguiente.

1. **REPARACIÓN 1 — PASS.**

Las comprobaciones del constructor quedan incorporadas mediante:

```python
n_parent_before = len(P.CHECKS)
...
all(ok for _, ok, _ in P.CHECKS[n_parent_before:])
```

El resultado agregado se registra en `D.CHECKS`. Es el mismo mecanismo que utiliza el padre. `row_L5a()` contiene dos comprobaciones: unitaridad y soporte. Si cualquiera registra `False`, también resulta falso el nuevo check agregado, entra en `prereq_failed` y determina una salida distinta de cero.

La Parte 3 bloquea correctamente las confirmaciones mediante la primera condición de `verdict`:

```python
if not certified:
    return "NOT CERTIFIED (failed prerequisite checks)"
```

La fotografía de prerrequisitos se toma después de las seis expansiones y del agregado del constructor; después no se registran nuevos checks. Por tanto, no queda desactualizada durante esta ejecución.

Para HL3e, `None` produce `UNDECIDED`, mientras que un signo decidido contrario a la hipótesis produce `REFUTED`. En los datos presentes, los cuatro signos son inequívocos porque `alpha0 = -4/315`.

No encuentro un camino, en las comprobaciones ejecutadas por este verificador, que termine con cero después de un fallo registrado. Los fallos propios de `P.row_L5a` quedan propagados; los de `D.CHECKS` se evalúan al terminar. Una excepción sin capturar también termina el proceso con error: no es necesario capturarla para garantizar esto.

**Aclaración de contabilidad:** son 35 checks en `D.CHECKS`, uno de ellos agregado sobre dos checks de `P.CHECKS`. No son 35 verificaciones independientes.

2. **REPARACIÓN 2 — PASS para la batería fijada.**

El programa emite ahora los identificadores contractuales:

```python
L3_DISPERSION_OPEN_FAILED_CHECKS
L3_DISPERSION_OPEN_QUANTITIES_MISSING_...
L3_DISPERSION_COMPLETE
```

El criterio corresponde a las Secs. 2 y 4 considerando conjuntamente el predicado `missing` y el flujo que lo precede. No depende solamente de cuatro claves: antes de insertar cada resultado, `analyse_block` calcula el factor nodal, `phi`, `omega2`, las expansiones radiales, la velocidad, las proyecciones y el primer coeficiente no nulo. `analyse` calcula después `G_walk`.

Las comprobaciones anteriores certifican el término cuadrático esperado y la ausencia de inclinación. Las expresiones proyectadas y sus residuos se calculan explícitamente; exigir residuos cero certifica además la representación angular utilizada en la tabla de esta batería.

Una hipótesis refutada no fuerza incorrectamente un dictamen OPEN: el cálculo puede estar completo y una predicción resultar falsa. El código conserva esa separación.

La salida adjunta muestra las cuatro filas completas, residuos cero y el dictamen `L3_DISPERSION_COMPLETE`. Los dos conceptos que el contrato excluye expresamente —velocidad máxima y escala de validez— siguen marcados OPEN.

3. **REPARACIÓN 3 Y ACLARACIONES — PASS.**

La segunda vía ya no atribuye a la identidad de trazas la comparación con L5a. La frase exacta:

> «The comparison of A−/B− with L5a rests on the expansion only»

cierra el exceso anterior.

La afirmación de que la identidad espectral proporciona HL3b incluye correctamente `G_walk`: con determinante uno, la igualdad de trazas implica igualdad del polinomio característico completo. Al usar las mismas coordenadas y el mismo grupo de 48 transformaciones, coinciden también sus estabilizadores espectrales.

La sustitución por:

> «an identity of traces, not of matrices»

es correcta. La inversión de momento relaciona las trazas de ambas quiralidades; no establece igualdad literal de los símbolos matriciales. Para estas trazas, cambia el término cúbico de `omega²`, invierte β y conserva α.

El emparejamiento corregido también es preciso: A+/B+ con CJWW (5.12), A−/B− con L5a. La referencia a los bloques L5b distingue ahora explícitamente el signo correspondiente.

La explicación de «recomputed» es una **aclaración interpretativa**, no una equivalencia literal: el contrato contiene tanto «nothing else … is recomputed» como la repetición explícita del control en HL3b. El informe declara correctamente lo que hace el programa: recalcula dos controles y no introduce otras filas nuevas ni modifica la tabla padre.

4. **LO ANTES NO VERIFICABLE — PASS para el uso presente.**

- **`laurent_adjoint`:** conjuga los coeficientes, sustituye `conjugate(z)` por `1/z` y transpone. Con los símbolos sin supuestos reales utilizados aquí, implementa correctamente el adjunto sobre el toro.
- **`laurent_support`:** extrae exponentes algebraicos `h = powers − bound` y agrupa sus matrices. El desplazamiento auxiliar de ocho basta para los exponentes ±1 presentes. Elimina correctamente coeficientes matriciales nulos.
- **`is_zero_matrix`:** aplica una prueba simbólica de cero entrada por entrada. Para estas expresiones de Laurent y coeficientes exactos, no introduce tolerancias ni aceptación numérica.
- **`row_L5a`:** construye el producto `T_x T_y T_z`, con proyectores de Pauli y factores unitarios de determinante uno. Su soporte consta de las ocho esquinas.

La convención del docstring de `laurent_support` no cambia los exponentes extraídos. La reconstrucción efectiva es:

\[
U(k)=\sum_h A_h e^{\sigma i k\cdot h/\sqrt3}.
\]

Así, `sigma=+1` reproduce los símbolos publicados y CJWW; `sigma=-1` reproduce L5a. No hay una inversión adicional escondida.

Como comprobación algebraica independiente, en L5a cada factor reconstruido es \(c_jI-i s_j\sigma_j\). Su producto tiene semitraza \(ccc-sss\), coherente con el β positivo mostrado.

5. **NO REGRESIÓN — PASS en el diff suministrado.**

Los cambios afectan a propagación de checks, certificación de hipótesis, dictamen contractual y aclaraciones del informe. No modifican constructores, normalización, expansiones ni cálculo de simetrías.

Los valores nuevos del informe siguen leyéndose de la salida. Además, se comprueban directamente tomando \(p=k/\sqrt3\):

\[
\omega^2=|p|^2-2\chi p_1p_2p_3
-\frac13\sum_{i<j}p_i^2p_j^2+O(|p|^5),
\]

de donde

\[
\beta=-\frac{\chi}{\sqrt3}n_1n_2n_3,\qquad
\alpha=-\frac{\sum_{i<j}n_i^2n_j^2}{18}
-\frac{n_1^2n_2^2n_3^2}{6}.
\]

Las medias esféricas \(1/5\) y \(1/105\) dan \(\alpha_0=-4/315\); la proyección produce \(7K_4/198-K_6/6\). El estabilizador de la traza contiene exactamente las seis permutaciones y los cuatro cambios de signo de producto positivo: 24 elementos.

Las referencias al estado histórico del padre no son resultados de esta salida y quedan **[UNVERIFIED]** como antecedentes históricos en esta revisión.

**Reparaciones obligatorias: ninguna.**