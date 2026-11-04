<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.1-sol, esfuerzo: high, vía: codex exec sellado (codex-cli 0.166.0)
inicio: 2026-11-04T12:01:15Z  fin: 2026-11-04T12:03:31Z
documento: /home/ignac/qca-causal-cones/theory/DISPERSION_L3_ROW_GATE.md ; último commit observado: d3868fa ; sha256 de la copia enviada d47b0ea66663bde73aff660ea0aad2b79a7309ae3d4fd87bb2df7e9a24db0fca
documento: /home/ignac/qca-causal-cones/scripts/verify_dispersion_L3_row_gate.py ; último commit observado: b9b0e58 ; sha256 de la copia enviada 1beb8fd94aac55ec99bc9b7a1ed226158ab2b1dfb265825e2e7b1e3035f85cf4
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--dispersion-L3-row.md ; último commit observado: b9b0e58 ; sha256 de la copia enviada cf24f8994eac1ddae458a870aa986784010a5c6beadcc0260c78c93b90994005
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--dispersion-L3-row-review-astra/salida_verificador.txt ; último commit observado: sin versionar ; sha256 de la copia enviada 4e9e7845c47f8859297d5acd6b3da831364de4a19bc60be8798439115ba4e45c
documento: /home/ignac/qca-causal-cones/scripts/verify_dispersion_corrections_gate.py ; último commit observado: 4a45280 ; sha256 de la copia enviada b7c451e213b60a0ae22e5c2ad15630abe5f5f4ee1c7c3d11dc660f43ffdb9a7e
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/ignac/qca-causal-cones/theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_ERRATUM_1.md ; último commit observado: d01decc ; sha256 de la copia enviada b50a4c2fbeb2e3f51027474ced870f7201f7ff964f36c0419cdd16ef90152449
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--dispersion-L3-row-review-astra/extractos.md ; último commit observado: sin versionar ; sha256 de la copia enviada d6b9e33b3c3f30e2058d206b5c02d54c4c6c585d00ee238660e750976c5d5417
entrada_astra.txt sha256 5fe0c809a86c40dfbc748dd0fc5f7d566bb621484ff44b86e583019dfbd3814f
respuesta sha256 ff64ff0d775bace05cdf03f311cead67da961ffd89ce112ff70d811ade9c26d2
-->

**Dictamen global: REPAIR_REQUIRED.** Los coeficientes de L3 son coherentes y se pueden comprobar algebraicamente con lo adjuntado. Las reparaciones afectan al cierre del verificador y a dos afirmaciones del informe.

1. **CONTRATO — PASS, con aclaraciones documentales.**

Fija la pregunta, los cuatro símbolos de `verify_case`, la normalización, `N = 4`, las cantidades y las hipótesis. Las transpuestas corresponden correctamente a B±. Declara expresamente que las hipótesis proceden de leer el código; el informe tampoco las presenta como evidencia independiente sobre otros walks.

La cronología «**Nothing computed before it**» y la conservación de bytes revisados quedan **[UNVERIFIED]**: los documentos suministrados no permiten acreditar historia de commits ni ejecuciones anteriores. Esto limita la certificación de procedencia, no contradice el cálculo.

Hay una inconsistencia literal menor: «**nothing else of the parent is recomputed or changed**», frente a HL3b, «**recomputed here with the same helpers**», y las dos llamadas de comparación. El alcance científico sigue siendo una sola fila nueva. **Aclaración:** distinguir incorporación de resultados nuevos de repetición de dos controles; no se modifica ni recalcula toda la tabla padre.

2. **VERIFICADOR — REPAIR_REQUIRED.**

La función `analyse` reproduce estáticamente la rama genérica `s = 2` del padre: extracción de soporte, posiciones cartesianas, máximo de longitudes, `taylor_symbol`, traza y determinante truncados, `analyse_block` y `walk_group`. Las constantes particulares son las correctas: dimensión tres, divisor uno, `N = 4` y velocidad esperada `1/sqrt3`.

También reproduce las convenciones del padre: `sigma = +1` para `published_symbol` y CJWW (5.12), y `sigma = −1` para L5a. Cambiar arbitrariamente ese signo invertiría el término cúbico y, por tanto, β.

Las identidades comprobadas —unitaridad de Laurent, determinante, traza y soporte— son pertinentes. Hay una limitación concreta: **no se adjunta `verify_c_across_lattices_gate.py`**, que define `P.laurent_adjoint`, `P.laurent_support`, `P.is_zero_matrix` y `row_L5a`. Su implementación literal queda **[UNVERIFIED]**. No atribuyo por ello un error al adjunto de Laurent; tampoco puedo certificar su código.

Los mecanismos señalados no producen falsos `CONFIRMED` en esta comparación:

- `same_pair` exige identidades polinómicas exactas. Las expresiones ya están reducidas sobre la esfera por el mismo procedimiento; la prueba es suficiente.
- La igualdad de listas de `G_walk` compara elementos, no solamente cardinalidades. Ambas listas recorren el mismo diccionario determinista.
- `alpha0.is_negative` vale inequívocamente `True` para `−4/315`. Un resultado indeterminado no daría `CONFIRMED`, aunque debería distinguirse de una refutación si apareciera en otra ejecución.

**Defecto obligatorio 1.** «**Fails closed: any failed check or exception exits nonzero**» no queda garantizado por:

```python
failed = [c for c in D.CHECKS if not c[1]]
return 1 if failed else 0
```

Se llama a `P.row_L5a()`, pero no se incorporan sus comprobaciones de `P.CHECKS`. El padre sí lo hace explícitamente mediante `n_parent_before` y `record("parent row constructors pass…", ...)`. Si el constructor registra un fallo sin lanzar excepción, este verificador puede terminar con cero. **Cierre:** trasladar al registro evaluado los checks nuevos del constructor, como hace el padre.

Además, la Parte 3 puede imprimir confirmaciones de hipótesis aunque haya fallado una comprobación estructural anterior. Las igualdades concretas podrían seguir siendo ciertas, pero ya no constituirían un certificado válido para la fila declarada. **Cierre:** bloquear la confirmación final cuando fallen sus prerrequisitos.

**Defecto obligatorio 2.** El contrato exige «**`L3_DISPERSION_COMPLETE` … or `L3_DISPERSION_OPEN_<reason>`**». El programa no emite ninguno. **Cierre:** producir ese dictamen después de evaluar todos los prerrequisitos y cantidades requeridas. Una hipótesis refutada no equivale por sí sola a un cálculo incompleto.

Los 34 checks corresponden a 16 identidades de L3 y 18 comprobaciones de las seis expansiones. No significan 34 comprobaciones independientes ni incluyen los tests propios del constructor L5a.

3. **RESULTADOS — REPAIR_REQUIRED por la descripción de la segunda vía; valores PASS.**

La tabla se lee correctamente de la salida: signos opuestos de β, α común, `alpha_0 = −4/315`, residuos cero y los mismos 24 elementos para los seis símbolos analizados. Las comparaciones reproducen las filas 44 y 46 del informe padre.

Una derivación manual confirma los coeficientes. Con \(p=k/\sqrt3\) y
\(u_\chi=\prod_i\cos p_i+\chi\prod_i\sin p_i\),

\[
\omega^2=|p|^2-2\chi p_1p_2p_3
-\frac13\sum_{i<j}p_i^2p_j^2+O(|p|^5).
\]

Al tomar la raíz sobre \(k=tn\), resulta

\[
\beta=-\frac{\chi}{\sqrt3}n_1n_2n_3,\qquad
\alpha=-\frac{\sigma_2}{18}-\frac{n_1^2n_2^2n_3^2}{6}.
\]

Las medias esféricas \(\langle\sigma_2\rangle=1/5\) y
\(\langle n_1^2n_2^2n_3^2\rangle=1/105\) dan `−4/315`. La proyección indicada, `7/198 K4 − K6/6`, concuerda con la definición de esos invariantes.

La lista de simetrías también tiene comprobación directa: la traza es invariante bajo cualquier permutación y bajo cambios de signo cuyo producto sea positivo. Son exactamente \(6\times4=24\) elementos, el grupo tetraédrico completo indicado.

**Defecto obligatorio 3.** «**HL3b and HL3c also follow without the expansion**» excede la segunda vía expuesta. Esta demuestra la igualdad espectral con CJWW (5.12) y la relación de paridad entre quiralidades. No demuestra por sí sola la parte de HL3c que compara con L5a: falta establecer su traza y determinante exactos bajo `sigma = −1`. **Cierre:** restringir la frase a lo efectivamente demostrado, o añadir esa identidad para el símbolo L5a ya utilizado.

**Aclaración:** «**chi = −1 is k -> −k of chi = +1**» debe referirse a la traza o al polinomio característico. No expresa igualdad literal de matrices. Para la dispersión, la inversión cambia β y conserva α correctamente.

4. **CONSECUENCIAS — PASS, con una aclaración de signos.**

La inclusión de L3 entre las filas con β y la cobertura de He están justificadas para los cuatro casos declarados: β no es idénticamente cero y es anisotrópico. Que se anule en determinadas direcciones no contradice esa conclusión.

«**Hd. Unchanged**» es correcto: esta fila tiene media negativa, pero no elimina la refutación previa por L1. Hf tampoco se redecide: las coincidencias adicionales y los dos signos distintos son compatibles con las consecuencias expuestas.

La frase «**L3 A± with CJWW (5.12) and with L5a**» es ambigua. La correspondencia precisa es:

- A+/B+ con CJWW (5.12).
- A−/B− con L5a.
- Cada signo con el bloque L5b correspondiente, según la tabla padre.

Es una **aclaración**, porque la tabla y la Sec. 3 ya deshacen la ambigüedad.

La advertencia final es correcta: igualdad del polinomio característico no demuestra igualdad de símbolos. Las referencias a L5b y al estado previo de He/Hf proceden del material padre adjunto, no de esta salida; deben entenderse como consecuencias combinadas.

**Reparaciones obligatorias:** propagar los fallos del constructor y bloquear certificación con prerrequisitos fallidos; emitir el dictamen contractual COMPLETE/OPEN; acotar o completar la segunda vía respecto de L5a. No encuentro un error en los coeficientes de L3 presentados.