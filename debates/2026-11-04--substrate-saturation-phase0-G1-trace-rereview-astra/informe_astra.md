<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.1-sol, esfuerzo: high, vía: codex exec sellado (codex-cli 0.166.0)
inicio: 2026-11-04T11:14:22Z  fin: 2026-11-04T11:15:52Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--substrate-saturation-phase0-G1-trace.md ; último commit observado: d60eaba ; sha256 de la copia enviada 33826163fba95df8aed75724594ebea680b425c868dc670e5d77c54bee87276c
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-G1-trace-rereview-astra/diff_reparacion.txt ; último commit observado: sin versionar ; sha256 de la copia enviada 19cfdd4504946ff4cd777ece77330ee4fdbee8c3b0dcd01b5df3685d597f314e
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-G1-trace-review-astra/informe_astra.md ; último commit observado: 8d70e58 ; sha256 de la copia enviada bffcba7f9de86b8b194630ec2d2f2100ec54c43d344e8dced1eeb23c07a87140
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-G1-trace-review-astra/extractos.md ; último commit observado: 8d70e58 ; sha256 de la copia enviada ce7632dc6469689fa0e35cdd398c6e9a51a4c7bb45bd5e35cb9ba3aa81f60cfb
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-G1-trace-review-astra/cjww_pp16-17.txt ; último commit observado: 8d70e58 ; sha256 de la copia enviada 68d4b9c97dedcc638ba1f55cc50e888497a3d1ce313d83a85c6ebe3399d70f5e
entrada_astra.txt sha256 320ef0234d04a0cf5f22d7b6edcbcab7ae90faad711a51af4110dcecfe31b0d0
respuesta sha256 14fcae6de30e92cb1136bb5cb06d373900416360c4fec166fa8776b92d5dab8a
-->

**Dictamen global: INSUFFICIENT_EVIDENCE.** Las dos reparaciones y las tres aclaraciones son correctas. El diff no introduce regresiones identificables. La limitación afecta a la ratificación independiente de L1–L3: falta el código de `verify_weyl_dirac_gate.py` que sustenta su pertenencia literal y sus generadores. El informe anterior, generado por una IA, no sustituye esa fuente.

Revisión manual de los adjuntos, sin herramientas ni ejecuciones.

**1. REPARACIÓN 1 — PASS.**

De `row_L6e` y `u2` se obtiene
\[
U^2=I,\qquad
U^1=e^{i\pi\sigma_x/4},\qquad
U^3=e^{-i\pi\sigma_x/4}.
\]
Con \(+\) asociado a R, el desplazamiento es \(\sum_j s_jN_j\), y la amplitud matricial:
\[
A_s=U^3P_{s_3}P_{s_2}U^1P_{s_1}.
\]
La ortogonalidad de los proyectores —el criterio de P en esta base— la anula cuando \(s_2\ne s_3\). Cuando son iguales, las entradas no nulas de \(U^1\) garantizan amplitud no nula.

| Patrones | Desplazamientos ISO | Amplitud |
| --- | --- | --- |
| \(++-\), \(--+\) | \((2,-2)\), \((-2,2)\) | cero |
| \(+-+\), \(-+-\) | ambos \(0\) | cero |
| \(+++\), \(---\) | \((2,0)\), \((-2,0)\) | no nula |
| \(+--\), \(-++\) | \((0,-2)\), \((0,2)\) | no nula |

Son **cuatro patrones nulos**, dos en vértices ausentes y dos en el origen. Como segunda comprobación, los cuatro restantes producen exactamente el conjunto `EXPECTED_F["L6e"]`.

La sección L6e, la tabla y G1-c son coherentes. La tabla dice «`0`, two patterns, both zero»: cuenta únicamente los patrones coincidentes en cero, no el total de patrones nulos. No queda el recuento antiguo.

**2. REPARACIÓN 2 — PASS.**

El Lema V establece correctamente, para el soporte contenido en las sumas candidatas:
\[
\operatorname{conv}F=Z
\iff \operatorname{vert}(Z)\subseteq F.
\]
Un funcional que expone un vértice fuerza todos los signos; por tanto, ese vértice tiene patrón único. La dependencia lineal o el paralelismo de los generadores no invalidan el argumento.

La reparación distingue correctamente:

- amplitud matricial de cada patrón;
- coeficiente de un desplazamiento, obtenido sumando las amplitudes coincidentes;
- soporte de coeficientes no nulos;
- envolvente convexa del soporte.

Todos los patrones no nulos garantizan conservar los vértices y, por ello, la envolvente. No son necesarios para esa igualdad. Tampoco deben confundirse con la condición para conservar **todas** las sumas candidatas en el soporte: allí cuentan las amplitudes sumadas.

El contraejemplo es correcto. Para \(a\ne0\) y proyectores complementarios:
\[
\bigl(P_+T(a)+P_-T(-a)\bigr)^2
=P_+T(2a)+P_-T(-2a).
\]
Los patrones mixtos se anulan, \(F=\{\pm2a\}\), y su envolvente sigue siendo \([-2a,2a]=Z\).

No quedan menciones afirmativas de F2 con la lectura antigua. «Audit F2 said…» es una atribución histórica inmediatamente corregida; las referencias posteriores remiten expresamente a la condición de vértices.

**3. ACLARACIONES — PASS.**

**Signos en L6e y L6c.** `jdw_shift` implementa desplazamientos opuestos a las posiciones leídas. En L6e, R lee en \(-N_j\) y se desplaza por \(+N_j\); la convención añadida reproduce correctamente la tabla.

En L6c,
\[
b_j=-N_j,\quad c_j=-N_{j+1},\quad
m_j=-\frac{N_j+N_{j+1}}2.
\]
Si \(+\) designa R:
\[
a_j=c_j-m_j=\frac{N_j-N_{j+1}}2.
\]
Con la convención de L6f, \(b_j=m_j+a_j\), el generador sería el opuesto. La aclaración explica correctamente esa diferencia; no cambia los segmentos ni las direcciones reducidas. **Es aclaración de orientación, no corrección geométrica.**

**Cláusula \(\pm a\).** En los factores impresos de L6c y L6f, los dos desplazamientos no son opuestos. La frase añadida «this does not show that no other factorization exists» limita correctamente la conclusión. Los «no» de la tabla deben leerse bajo su encabezado «Product class (literal)», referido a esas presentaciones; no constituyen una prueba de inexistencia de otra factorización.

**Cita suprimida en (5.12).** La eliminación es correcta. CJWW p. 16 proporciona el producto original y `walk1` lo transcribe. Los proyectores de ejes de Pauli distintos tienen solapamientos no nulos, y las ocho sumas son distintas. La reseña de otro modelo no hace falta como evidencia.

**4. NO REGRESIÓN — INSUFFICIENT_EVIDENCE para la ratificación completa; PASS respecto al diff.**

El diff modifica únicamente las dos reparaciones, las tres aclaraciones y la cabecera de revisión. No cambia constructores, soportes, magnitudes ni clasificación de filas.

Las filas comprobables directamente con los adjuntos siguen siendo correctas:

- **L5a y L4-(5.12):** tres factores por ejes ortogonales, ocho desplazamientos distintos y patrones no nulos.
- **L6a:** tres generadores con suma cero; seis vértices y dos patrones centrales. Los vectores de Bloch distintos tienen producto escalar \(1/3\), por lo que P permite los ocho patrones.
- **L6d:** la agrupación del constructor da tres factores conjugados. Los vectores de Bloch consecutivos difieren en ángulo \(\pi/3\); los ocho patrones son no nulos y las sumas dan los seis vértices y el origen.

Las lagunas conservan su sentido: **G1-a**, adecuación de las presentaciones asimétricas al contrato; **G1-b**, factorización no documentada en el material revisado; **G1-c**, dependencia de la presentación en L6e. En esta última, fusionar \(S^3S^2\) produce el generador cartesiano \((0,1)\), ortogonal al primero \((1,0)\).

La limitación documental exacta está en L1–L3:

> «`rotation_product` (l. 80–88)…»  
> «the check “published vs product” (l. 145)…»

Ese archivo y esos extractos **no están adjuntos**. `part2` únicamente importa y llama a `published_symbol`; no muestra su definición. El diff acredita que estas afirmaciones no cambiaron, pero su correspondencia con el constructor queda **[UNVERIFIED]** en esta revisión. Lo cerraría el extracto primario ya citado, sin nuevas filas ni ejecuciones. Esto es insuficiencia de evidencia, no un error demostrado de la traza.

**Reparaciones obligatorias del texto: ninguna identificada.** Las reparaciones 1 y 2 están cerradas; el PASS global queda pendiente exclusivamente de la evidencia primaria ausente para L1–L3.