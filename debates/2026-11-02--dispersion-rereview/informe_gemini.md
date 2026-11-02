<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 9b0290bef3cc56cadf72f2ef0d4b82247a80dd0d6855337cc2bce50a9f76bb56
inicio: 2026-11-02T18:07:20Z  fin: 2026-11-02T18:07:41Z
documento: /home/adnac/qca-causal-cones/theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md ; último commit observado: a7ff5b7 ; sha256 de la copia enviada 6df09e81fae231ebbb00d19de546298559d333d33e965c95a1aa6027842231ea
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices-review.md ; último commit observado: 4a45280 ; sha256 de la copia enviada 483b29e4848d3002fcaaa9fcccdf45c6325a9c213a706eb402b97e5b050880f6
documento: /home/adnac/qca-causal-cones/debates/2026-11-02--dispersion-review-grok/repair.diff ; último commit observado: 4a45280 ; sha256 de la copia enviada 32389d42dcf3b712fa0a81a2e4532f93b2b3164fb100795c00fa102e7b1151fd
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices.md ; último commit observado: 4a45280 ; sha256 de la copia enviada fe14d132ee6d2308ecabb089d39aecca37f4bfec167e03d97a65f8ccdeb3a877
documento: /home/adnac/qca-causal-cones/scripts/verify_dispersion_corrections_gate.py ; último commit observado: 4a45280 ; sha256 de la copia enviada b7c451e213b60a0ae22e5c2ad15630abe5f5f4ee1c7c3d11dc660f43ffdb9a7e
entrada_gemini.txt sha256 f4976edfcc8a722b2257ce316528adf2d4086ee98e0f9dfcbb7a5d50d5d3fb6d
respuesta sha256 9ee433495b452b36c698809973d932fa4750b724065f5f044fcd27829fd5c58c
-->

### Dictamen por punto

**R1. Signo de $\beta$ en L3s4: PASS.**
Con $\beta(\hat{n}) = \beta_0 + \beta_3 n_1 n_2 n_3$, donde $\beta_0 = \pm\frac{\sqrt{3}(1-a^2)}{6a}$ y $\beta_3 = \pm\frac{\sqrt{3}(2a^2-1)}{3a}$, dado que el rango de $n_1 n_2 n_3$ en la esfera unidad $S^2$ es el intervalo cerrado $\left[-\frac{1}{3\sqrt{3}}, \frac{1}{3\sqrt{3}}\right]$, la función $\beta(\hat{n})$ conserva estrictamente el signo de $\beta_0$ en toda la esfera si y solo si $|\beta_3| \frac{1}{3\sqrt{3}} < |\beta_0|$, lo que equivale a $\beta_0^2 - \frac{\beta_3^2}{27} > 0$. 
Desarrollando exactamente la diferencia:
$$\beta_0^2 - \frac{\beta_3^2}{27} = \frac{3(1-a^2)^2}{36a^2} - \frac{3(2a^2-1)^2}{27 \cdot 9a^2} = \frac{27(1 - 2a^2 + a^4) - 4(4a^4 - 4a^2 + 1)}{324a^2} = \frac{11a^4 - 38a^2 + 23}{324a^2}.$$
Las raíces del numerador en $a^2$ son $\frac{19 \pm \sqrt{361 - 253}}{11} = \frac{19 \pm 6\sqrt{3}}{11}$. Como $6\sqrt{3} = \sqrt{108} \in (10, 11)$, la raíz $\frac{19 + 6\sqrt{3}}{11} > 2$ queda fuera del intervalo $a \in (0, 1)$, mientras que $a_*^2 = \frac{19 - 6\sqrt{3}}{11} \approx 0.7825 \in (0, 1)$ (con $a_* \approx 0.8846$) es la única raíz en $0 < a < 1$. El polinomio es positivo en $0 < a^2 < \frac{19 - 6\sqrt{3}}{11}$ y negativo para $\frac{19 - 6\sqrt{3}}{11} < a^2 < 1$. En la frontera $a^2 = \frac{19 - 6\sqrt{3}}{11}$, $\beta$ se anula en las diagonales principales $|n_1|=|n_2|=|n_3|=1/\sqrt{3}$, por lo que no conserva un signo estricto en toda la esfera.

El nuevo texto de la Sec. 3.3 es completamente exacto: restringe la imparidad de $\beta$ a L5a, L5b, L4, L6a y L6b, expone el umbral exacto para L3s4 y aclara correctamente que el signo de $\beta_0$ depende del cúmulo ($\pm\pi/4$) y se invierte entre la rama superior y la inferior (pues $\varepsilon_\pm = \varepsilon_0 + \phi \pm \omega$, donde $\phi$ es par y cuadrático mientras que $\omega = c_0 t + O(t^2)$ cambia de signo entre ramas, invirtiendo el signo relativo de $\phi / (\pm c_0)$).
Asimismo, los dos nuevos `record` en el verificador (uno por cada cúmulo de L3s4) certifican exactamente lo que anuncian: extraen el numerador de `gap = beta0**2 - beta3**2 / 27`, cuentan mediante Sturm (`count_roots`) que hay exactamente una raíz en $(0, 1)$, verifican con `zero(...)` que se anula exactamente en $\sqrt{(19 - 6\sqrt{3})/11}$, y comprueban con `P.positive` el signo positivo en $a = 1/2$ ($\le 0.8846$) y negativo en $a = 19/20 = 0.95$ ($\ge 0.8846$).

**R2. Frase de la Sec. 1 sobre L5a y los bloques de L5b: PASS.**
La tabla de la Sec. 1 muestra que L5a tiene $\beta = (\sqrt{3}/3) n_1 n_2 n_3$, mientras que los dos bloques de Weyl de L5b tienen $\beta = \pm(\sqrt{3}/3) n_1 n_2 n_3$ y el mismo $\alpha$. Por tanto, L5a solo comparte el par $(\beta, \alpha)$ con el bloque de L5b cuyo $\beta$ tiene el mismo signo (`L5b[+i]`). Esto concuerda exactamente con la lista de pares que construye y evalúa el verificador en la Parte 4 (`("BCC", ["L3", "L5a", "L5b[+i]"])`).

**R3. Record de Hd en el verificador: PASS.**
El predicado constante `True` ha sido sustituido por `not undecided`, que puede fallar si para alguna fila `table[l]` es `None` (lo que ocurriría si `P.positive` no decidiera un signo numérico o si una expresión simbólica tuviera raíces/polos en $(0,1)$) y simultáneamente `sturm_table_complete(results[l])` fuera `False`. La función auxiliar `sturm_table_complete` certifica rigurosamente que la lista de intervalos `alpha0_signs` existe, empieza en `0`, termina en `1`, es contigua (`sg[i][1] == sg[i+1][0]`) y tiene un signo exacto no nulo (`1` o `-1`) en cada subintervalo. Junto con el registro previo que verifica `len(rts) == roots_in and poles_in == 0`, esto garantiza de forma cerrada (fail-closed) que el signo de $\alpha_0$ queda exactamente decidido en todas las filas.

**R4. Regresiones: PASS.**
El `diff` está estrictamente acotado a las tres reparaciones y al registro documental de la revisión (actualización de hashes SHA256, conteo de checks de 79 a 81, estado de revisión y resumen de reparaciones en Sec. 5 y Sec. 7). No introduce ningún error matemático ni de código, no altera ningún valor tabulado ni veredicto de hipótesis (`Hd`, `He`, `Hf`), y respeta íntegramente el techo de afirmaciones y las exclusiones del contrato congelado.

---

### Dictamen global

**PASS.** No hay reparaciones obligatorias.
