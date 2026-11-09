<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 f112580125aa7135a4ec6a92a5b6b72a318239f8ebfbbe6d35aeedd26e983bb3
inicio: 2026-11-04T10:50:19Z  fin: 2026-11-04T10:55:43Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--ps-prime-intrinsic-definition-proposal.md ; último commit observado: 0d85366 ; sha256 de la copia enviada ea7b864639a72ea50a16e4672c5f512c7dbe72471decfc479c7324798444ec67
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--substrate-saturation-phase0-G1-trace.md ; último commit observado: d60eaba ; sha256 de la copia enviada 33826163fba95df8aed75724594ebea680b425c868dc670e5d77c54bee87276c
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--ps-prime-proposal-review-deepseek/extractos.md ; último commit observado: sin versionar ; sha256 de la copia enviada cbe4cefb91cf4bb0f5b9e6c8a33dd9b215fab7f3a9d9e6882197501c8ec15d97
entrada_deepseek.txt sha256 2fc64cb1a9844ad3648f77132d22cec208f9db97df7348bbcfc3e1f1675d0d5a
respuesta sha256 8ff9f963b4fe49a156ab3f825fdebb32eee6b620540eb20c831b9766ca59a668
-->

### 1. L6e desde la fuente — **PASS**

La propuesta afirma: “In Eq. (6), the second-step coin has angle zero; Eq. (1) then gives the identity.” Es correcto: en JDW p.2 Eq. (6), `Û_2 = U(0,0,−π/2,0)`; en Eq. (1), con `θ=0`, la matriz es identidad.

También es correcto que los pasos 2 y 3 pueden fusionarse sin cambiar el operador completo ni la unidad de tiempo. En el producto `Ŵ_3 Ŵ_2 Ŵ_1`, con `Û_2=I`, queda `Û_3 Ŝ_3 Ŝ_2 Û_1 Ŝ_1`; como `Ŝ_2` y `Ŝ_3` son diagonales en la misma base L/R, conmutan, y `Ŝ_3 Ŝ_2` es un solo desplazamiento. La duración sigue siendo una actualización completa (`Δt=ε` en JDW p.2).

Los desplazamientos cartesianos son correctos desde los vecinos `X1..X6`: `N1=(1,0)`, `N2=(1/2,1/2)`, `N3=(−1/2,1/2)`, y la suma de los dos últimos es `(0,1)`. El fusionado es simétrico: L se mueve por `−(0,1)` y R por `+(0,1)`.

Las líneas citadas del verificador implementan lo mismo. `row_L6e` usa `Uj = u2(0,0,−π/2,(j−2)π/4)` y `jdw_shift(zs, ISO[j], ISO[j+3])`. La convención de `jdw_shift` es consistente: lee L en `read_L`, por lo que L se desplaza `−read_L`; con `ISO[j+3]=−ISO[j]`, R se desplaza `+ISO[j]`. No se detecta error.

### 2. Recuento y zonótopos — **PASS**

La presentación impresa de L6e tiene tres direcciones reducidas en `d=2`: `(1,0)`, `(1/2,1/2)` y `(−1/2,1/2)`, ninguna paralela. La presentación fusionada tiene dos direcciones ortogonales: `(1,0)` y `(0,1)`. Correcto.

El zonótopo impreso con tres generadores es un hexágono. En coordenadas ISO sus vértices son `±(2,0)`, `±(2,−2)`, `±(0,2)`. El soporte certificado de L6e contiene `(−2,0),(0,−2),(0,2),(2,0)`, cuatro vértices. Faltan los vértices `±(2,−2)`; además están fuera de `conv F`, que es el cuadrado/diamante con los cuatro puntos del soporte. La afirmación de la propuesta de que hay “two candidate vertices absent” es correcta.

La presentación fusionada tiene generadores `(1,0)` y `(0,1)`; su zonótopo es el cuadrado de cuatro vértices, coincidente con el cuerpo registrado en `EXPECTED_MASSLESS` para L6e línea 78, que registra `4` vértices. También es compatible con `r_in = R2/2` y `c_0 = R2/2`. Correcto.

### 3. Contrato — **PASS**

El contrato define PS′ “for a walk that is a product of `n` coin–partial-shift factors, each partial shift moving by `±a_i`”. No selecciona una presentación canónica ni cuantifica sobre factorizaciones. Por tanto, no afirma que el número de direcciones reducidas sea intrínseco al walk completo. La lectura de la propuesta es fiel.

En cuanto al cuantificador existencial: el contrato Sec. 2, punto 1, dice que “the ceiling is attained on a substrate” significa que existe al menos una caminata admisible con `c_0 = r_in`, no que toda caminata sature. La propuesta representa correctamente esa distinción en su Sec. 2, punto 2, y no la confunde con el cuantificador sobre presentaciones de una misma caminata.

Señalo únicamente una aclaración menor no bloqueante: la propuesta cita “Sec. 2.1” del contrato, aunque el contrato no tiene subdivisiones numeradas 2.1; se refiere al punto 1 de la Sec. 2. No es error de fondo.

### 4. Lógica — **PASS**

La recomendación de la Sec. 4 está acotada: “do not extend the presentation-based generator count to an intrinsic saturation criterion without an explicit presentation rule”. No declara imposible una regla futura; explícitamente dice que “No justified rule is available here” no significa “no such rule can exist”. Tampoco emite veredicto sobre PS′ ni sobre PH: lo separa expresamente en Sec. 1 y Sec. 4.

La consecuencia condicional de la opción `Z(P)=conv F` es correcta. Bajo `Z(P)=conv F` y generadores que generan `R^d`, “exactamente `d` direcciones reducidas independientes” equivale a que el cuerpo común sea un paralelepípedo. La hipótesis de dimensión plena está incluida y es válida para las filas del registro. La afirmación de que la verdad del predicado queda fijada por el cuerpo, sin factorización canónica, es correcta bajo esa restricción.

El párrafo sobre G1-a también es correcto. En L6c/L6f, la lectura afín produce vectores `a_j` con componentes medias que no son traslaciones del grupo original. Que el desplazamiento total del centro sea cero (`∑ m_j=0`) no basta para admitir esos factores centrados como operadores intermedios sobre el espacio original. La propuesta no afirma imposibilidad, solo requiere una regla de dominio; es una postura lógicamente prudente.

### 5. Honestidad de estado — **PASS**

La propuesta declara expresamente que su criterio es retrospectivo y no preregistrado: “Retrospective stopping rationale, not preregistration. This document was written knowing the L6e example.” También aclara que no es predicción ni evidencia independiente.

En cuanto al estado del proyecto, dice:

- no cambia el contrato congelado;
- no cierra G1;
- no emite el veredicto sobre PS′ excluido por la fase 0;
- no actualiza `state/CURRENT_STATE.md` Sec. 15;
- PH queda sin cambios;
- fase 0 queda `PRELIMINARY / OPEN_AFTER_ROW_SURVEY`, sin valor confirmatorio.

Todo es consistente con el contrato y con la traza G1. No se detecta una alteración encubierta del estado.

### Dictamen global

**PASS**

No hay reparaciones obligatorias. La propuesta es documental, distingue evidencia de propuesta, identifica correctamente la dependencia de presentación en L6e, no excede los hechos establecidos y es honesta sobre su carácter retrospectivo y su falta de valor confirmatorio. La única observación es una aclaración menor de cita (“Sec. 2.1” en lugar de “Sec. 2, punto 1”), que no exige reparación.
