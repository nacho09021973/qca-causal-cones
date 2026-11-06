<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 90fcee2c0953e396922c73e3fa8314738bb53f511e227e1e0e12137912522a2f
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-06T10:30:25Z  fin: 2026-11-06T10:44:37Z
documento: /home/ignac/qca-causal-cones/.worktrees/massive-vgrp-bcc/theory/DIRAC_VGRP_MAX_GATE.md ; último commit observado: 5ebe10d ; sha256 de la copia enviada 731058c4e11046ff2cca90c2cd4adb492607ef20fb820287cdf8c52973df6027
documento: /home/ignac/qca-causal-cones/.worktrees/massive-vgrp-bcc/theory/THREE_VELOCITIES.md ; último commit observado: 95f423f ; sha256 de la copia enviada bf1a746c557408d1ab5249210fba0566502677ab302e1068886f39b31d32ba41
documento: /home/ignac/qca-causal-cones/.worktrees/massive-vgrp-bcc/reports/2026-09-14--weyl-dirac-gate-contract.md ; último commit observado: 2c7c2c9 ; sha256 de la copia enviada e0e3483380b0352198c64cbca64985a5240389b7fc70a2694c9a79f9a2f33d27
documento: /home/ignac/qca-causal-cones/.worktrees/massive-vgrp-bcc/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
entrada_grok.txt sha256 93c8cd0bd16317b8e9cc9fdc4296c7b4a8498c96a3ca1d2668f2d0128bcc9346
respuesta sha256 b2b276fe15109eee9d2208bd9b1932386bf8b5ffaadc457b9cf3bf16ff06ad3f
-->

**No congelar.** El núcleo analítico —`ω`, la normalización `k = sqrt(3) q`, `Φ` y `|n u| ≤ n < 1`— es correcto, y `V_grp^max` queda separado de `c_IR`, `c_H`, `c_{ω²}` y `C_micro`. La carta no es todavía un procedimiento cerrado: el caso de dimensión positiva no calcula el máximo, T3 pide signos que la etapa algebraica no decide, y B3 no es un predicado decidible.

## Supuestos

Solo están los cuatro textos pegados. No ejecuté el verificador, no leí el PDF de Pavia ni `CURRENT_STATE.md`, y no doy por hecho el PASS histórico: solo el contrato y el código adjuntos. Rehíce a mano la regla de la cadena, `Φ`, la ecuación crítica, `F = M cot M`, las cinco parejas `(m, n)`, el control unidimensional y el recubrimiento de las cartas. Conté el Python pegado: las líneas 66–68 son el escalar `u` y las 133–134 son `spatial_derivative`. «Error demostrado» significa que la frase o el procedimiento, leídos como están, no hacen lo que dicen; «laguna», que falta un caso o una obligación; «redacción», que el contenido se salva cambiando la frase.

## 1. Definiciones

`ω = acos(n u)`, `k = sqrt(3) q`, `Φ` y `|n u| ≤ n < 1` son correctos. La separación de velocidades también, con un choque de redacción en T3.

El código da, en `d = 3`,
`u = cos q_x cos q_y cos q_z + χ sin q_x sin q_y sin q_z`, `χ = ±1`.
La identidad de Laurent `W² − 2 u W + I = 0` y la unitariedad sobre `|z_j| = 1` ponen los autovalores de `W` en el círculo, así que `u = cos θ ∈ [−1, 1]` en todo el toro. Para `0 < m < 1`, `n = sqrt(1−m²) ∈ (0, 1)` y `|n u| ≤ n < 1`. El denominador cumple `1 − n² u² ≥ m² > 0`. `acos` es analítica en `[−n, n] ⊂ (−1, 1)`, luego `ω` y `Φ` son analíticas en todo el toro. La etapa 0 pide solo `|n u| < 1`; es verdad, pero es más débil que `|n u| ≤ n`.

El contrato fija `q_j = k_j/sqrt(d)` y el verificador implementa `∂/∂k = (i z ∂/∂z)/sqrt(d)`. Con `d = 3`,
`∂ω/∂q_i = −n (∂_i u) / sqrt(1 − n² u²)`,
`||∇_k ω||² = (1/3) ||∇_q ω||² = (n²/3) G / (1 − n² u²)`,
`G = ||∇_q u||²`. Eso es exactamente `Φ`. El signo de la derivada de `acos` desaparece al elevar al cuadrado. Las cinco masas cumplen `n² + m² = 1`.

`F = M cot M` con `M = arcsin m` coincide con `F = M n/m` del documento 2, y `c_H² + 2 M b = c_{ω²}²` cierra algebraicamente. `V_grp^max` se define como máximo espectral de `||∇_k ω||`; `r_in = 1/sqrt(3)` y `V_causal^max = 1` salen del casco de `N_3` (ocho vértices, seis caras, arista del cubo `[-1/sqrt(3), 1/sqrt(3)]³`). La sección 1 los usa solo como comparación y prohíbe inferir `c_IR`. Eso respeta la sección 4 del documento 2.

**G-V-01.** Sección 0, «Known», «massless group speed at the node equals `r_in`». Redacción. El verificador iguala la pendiente lineal del nodo sin masa con `r_in`. En `m = 0` la propia carta dice que `ω` no es diferenciable en el nodo, así que eso no es una velocidad de grupo clásica. No es `V_grp^max`.

**G-V-02.** Sección 3, T3, frente a las secciones 1 y 6. Laguna. Comparar con `c_H(m)` y `c_{ω²}(m)` no los identifica con `V_grp^max`, pero tampoco es «no calcularlos»: hace falta un procedimiento de signo que la carta no da. Detalle en el punto 5.

## 2. Etapa A

Enumerar los ceros reales de `∇Φ` en las ocho cartas basta para el máximo global solo si `Φ` es diferenciable, no se ganan ni se pierden ceros reales y el caso de dimensión positiva se evalúa como constante en cada componente conexa euclídea. Lo primero es cierto cuando la etapa 0 prueba `|n u| < 1`. Lo segundo es cierto para la sustitución de Weierstrass, no para una resultante sin controlar. Lo tercero, tal como está escrito, es falso.

En el círculo, `t = tan(q/2)` es difeomorfismo de `q ∈ (−π, π)` sobre `R` y falla en `q ≡ π`. `t = cot(q/2)` es difeomorfismo de `(0, 2π)` sobre `R`, vale `0` en `q ≡ π` y falla en `q ≡ 0`. En cada coordenada se elige `tan` si `q_i ≡ 0`, `cot` si `q_i ≡ π`, y cualquiera en otro caso: las `2³` combinaciones cubren el toro. En el dominio de cada carta `dt_i/dq_i ≠ 0`, así que `∇_q Φ = 0` equivale a `∇_t Φ = 0`. El toro es compacto y sin borde, `Φ` es lisa, y el máximo se alcanza en un punto crítico. Comparar valores algebraicos en todos los críticos reales da el máximo y el conjunto de maximizadores, si la lista es completa.

La ecuación de A2 es la correcta. Con `D = 1 − n² u² > 0`,
`∂_i(G/D) = 0` si y solo si `D ∂_i G − G ∂_i D = 0`,
y `∂_i D = −2 n² u ∂_i u`, que es
`(1 − n² u²) ∂_i G + 2 n² u G ∂_i u = 0`.
`u` y `G` son polinomios trigonométricos. Tras Weierstrass, los denominadores son potencias de `1 + t_i²`, positivas en `t` real. Multiplicar solo por esos factores no añade ni quita ceros reales de esa carta. El punto `q ≡ π`, que es el infinito de `tan`, cae en la carta `cot`. No hace falta anular `G` ni `u`: los ceros de `G` son críticos genuinos (velocidad nula).

**G-V-03.** Sección 4, A1, y la zona `q ∈ [−π, π)³` de la sección 2. Redacción. El representante `q_i = −π` está en el cubo declarado y hace diverger `tan(q/2)` y `cot(q/2)`. El punto del toro es la clase `q ≡ π`, regular en la carta `cot` con valor `0`. El recubrimiento vale en la variedad, no en ese representante. Implementar el extremo del cubo produce un NaN o pierde el punto.

**G-V-04.** Sección 4, A2–A3. Laguna. A2 afirma equivalencia «tras despejar denominadores positivos» sin listarlos. Una resultante no conserva el conjunto de ceros si se anula el coeficiente director. Hace falta el ideal saturado, o una comprobación de que cada cero real cumple la ecuación sin despejar. Si no, A4 puede evaluar `Φ` en un punto espurio.

**G-V-05.** Sección 4, A3. Error demostrado. Si el ideal crítico tiene dimensión positiva, `dΦ = 0` en todo su lugar real. En cada componente conexa por caminos, `Φ` es constante: a lo largo de un camino `C¹` la integral de `dΦ` es cero. «Restringir y repetir» busca críticos de una función cuya derivada ya es identicamente nula; la ecuación no baja la dimensión y no termina. Además, una componente irreducible puede tener varias componentes euclídeas con constantes distintas. Un solo punto por componente algebraica no da el máximo. Lo correcto es una muestra exacta por componente conexa real, más el paro si eso no se certifica. El paro de la sección 5 evita un certificado solo si quien implementa reconoce que no sabe seguir; el texto actual dice que repita.

**G-V-06.** Sección 4, A5, frente a T1. Laguna. La lógica bilateral es válida: si `D > 0`, `Φ ≤ V²` equivale a `V² D − (n²/3) G ≥ 0`, y un testigo exacto con igualdad fija el máximo. Una suma de cuadrados de polinomios trigonométricos con coeficientes racionales es suficiente y comprobable. No es un procedimiento completo: hay trigonométricos no negativos que no son suma de cuadrados, no hay cota de grado, y con coeficientes racionales `V²` tiene que estar en `Q`. T1 admite un algebraico no racional. En ese caso A5 solo puede dar un techo racional, no el valor de T1. La carta tampoco dice de dónde sale el testigo si A3 no termina, y B está prohibido como entrada de un chequeo exacto.

## 3. Etapa 0

El orden —probar simetrías antes de reducir— es el correcto, y el paso 4 sí pide la relación entre los cuatro símbolos. Faltan dos obligaciones que la carta usa antes de tenerlas, y el control C0 choca con la fórmula de `Φ`.

El paso 1 (reproducir `cos ω = n u` sin modificar el verificador), el paso 2 (analiticidad y derivar `Φ`), el paso 5 (literatura, todavía `[UNVERIFIED]`) y el veto si C0 falla están bien colocados. C0, leído en norma unidimensional, es cierto: con `u = cos q` y `k = q`,
`||dω/dq||² = n² sin² q / (1 − n² cos² q) = n² s / (m² + n² s)`, `s = sin² q`.
Crece con `s` y vale `n²` en `q = ±π/2`. Y `n = cos(arcsin m)` para `m ∈ (0, 1)`.

La traza no cambia al transponer, así que `A±` y `B±` comparten `u`. El reflejo `q_z → −q_z` cambia el signo de `χ` y es una isometría lineal de `q`, luego de `k = sqrt(3) q`. `Φ` depende de `u²` y de `G`, así que también es invariante si `u → −u`. Eso hay que probarlo; no está escrito.

**G-V-07.** Sección 2, fila «Branch», frente a la lista numerada de la etapa 0. Laguna. La tabla afirma que las fases son `±ω` y que sus gradientes solo cambian de signo, y ordena verificarlo en la etapa 0. La lista no tiene ese ítem. El material adjunto alcanza para probarlo: `D² − 2 n u D + I = 0`, `tr D = 4 n u` real y `sin ω ≥ m > 0` obligan a las dos raíces `e^{±iω}`, cada una con multiplicidad 2. Sin ese chequeo, la norma sobre ramas se usa antes de certificarla. `cos ω = n u` no fija el signo ni la multiplicidad.

**G-V-08.** Sección 4, etapa 0, paso 4. Laguna. El paso pide invariancia de `u`, o una biyección entre casos. Reducir el dominio exige otra cosa: que la transformación sea ortogonal en `k` y conserve `||∇_k ω||`, y que el conjunto de maximizadores se reconstruya por la órbita. Una simetría de `u` que no conserve la métrica euclídea cambiaría la norma. Las permutaciones con signo son de `O(3)`, pero eso es parte de la prueba, no una consecuencia de `u(Sq) = u(q)`.

**G-V-09.** Sección 4, definición de `Φ` y control C0. Redacción. `Φ` se define con el factor `n²/3` de `d = 3`. C0 pide `max Φ = n²` «con `r_in = 1`». Las dos lecturas no pueden ser verdaderas a la vez sobre el mismo símbolo: reutilizar la fórmula tridimensional hace fallar un control cuyo enunciado unidimensional es correcto, y pararía la puerta con `STOPPED_CONTROL_FAILED`.

## 4. Etapa B

Queda relegada como certificado de un valor, no como veto. B3 no es decidible con lo escrito, y no es circular en el flujo de datos.

B corre después de A, solo con `--diagnostics`, no alimenta ningún chequeo exacto y no puede rescatar una etapa A parada. Una malla finita no certifica el máximo. Hasta ahí es diagnóstico. El veredicto de puerta `STOPPED_EXACT_NUMERIC_DISAGREEMENT` sale de B. Por tanto B sí puede cerrar la puerta.

No hay círculo de certificación: A no lee B. El predicado de acuerdo sí presupone que A3 produjo cajas aislantes. Si el certificado es A5, o si el crítico es de dimensión positiva, esas cajas no existen y B3 no está definido.

**G-V-10.** Sección 4, B3, última frase, y sección 7. Error demostrado. «Stage B never feeds a terminal verdict» es incompatible con un veredicto de puerta disparado por B. «A finite scan proves no global maximum» dice, en inglés literal, que la malla demuestra que no existe máximo global. Lo que puede querer decir es que no lo demuestra. Como está, es falso.

**G-V-11.** Sección 4, B3. Laguna. La tolerancia se deja al script, fuera de la carta que se quiere congelar; puede elegirse después de ver A y la malla. La pertenencia de un punto de Newton o BFGS a una caja racional no es exacta en coma flotante. La regla es asimétrica: un grid por encima del valor certificado detecta un máximo demasiado bajo; un crítico espurio que infla `Φ` pasa la cláusula «el grid no excede» y no está obligado a aparecer en la malla. B3 no caza ese error. Tampoco exige que el máximo del grid se acerque al valor certificado por debajo.

## 5. Hipótesis y veredictos

H1 y H2 son decidibles en las cinco masas si A4 entrega el algebraico aislado. H3 no lo es todavía. T3 promete más de lo que la etapa A calcula. Ningún veredicto, por su etiqueta, extiende el resultado fuera de las cinco masas de esta familia; la sección 3 lo dice de forma explícita.

Con `V²` dado por polinomio mínimo e intervalo aislante racional:

- H1 es `V² − n²/3 = 0`. Ambas cantidades están en una extensión algebraica controlada; `n²/3 ∈ Q`. Decidable.
- H2 es `V² − 1/3 < 0`. Mismo método. Decidable.
- Un contraejemplo exacto en una masa refuta la hipótesis universal sobre las cinco. Una confirmación es solo «en las cinco masas», no en la familia ni en todo `m`. Esa limitación está bien escrita.

**G-V-12.** Sección 3, T3, y `VGRP_MAX_CERTIFIED` en la sección 7. Laguna. El signo de `V − r_in` es algebraico. `c_H = r_in M n/m` y `c_{ω²} = r_in sqrt(F)` contienen `arcsin` de un racional. A4 solo compara críticos algebraicos. No hay aislamiento de `arcsin(3/5)`, `arcsin(4/5)`, `arcsin(5/13)`, `arcsin(12/13)` ni `arcsin(8/17)`, ni regla si la diferencia es cero. Certificar T3 promete un signo exacto que la carta no sabe calcular. Choca con la sección 6, que dice que `c_H` y `c_{ω²}` no se calculan.

**G-V-13.** Sección 3, H1–H3, y sección 7. Laguna. H1 dice «refutada en el primer contraejemplo»; la sección 7 dice `UNDECIDED` si alguna masa queda abierta. Si una masa refuta y otra queda abierta, los dos veredictos se aplican. `CEILING_ONLY` no tiene imagen en los veredictos de hipótesis: un techo racional `< r_in` demostraría H2 en esa masa y la tabla no sabe registrarlo; un techo `≥ r_in` no la decide.

**G-V-14.** Sección 3, H3. Laguna. «Se alcanza en un eje coordenado de `q`» no define el conjunto. En el toro, `q_y = q_z = 0` es un círculo. No se dice si vale la existencia o la universalidad de maximizadores, ni si `q_i ≡ π` cuenta como eje, ni cómo se lee la órbita si T2 entrega representantes. Sin ese conjunto, el signo de H3 no es una función del certificado.

## 6. Parada, presupuesto y exclusiones

Las exclusiones de pregunta sí impiden ampliar la puerta a otras masas, a `n` simbólico, a `d = 2` o a otro sustrato. El presupuesto y el encaje de T3 con la sección 6 no están igual de cerrados.

Sirven como cierre: cinco masas fijas; etapa 0 decide qué identificaciones hay, no qué símbolos nuevos aparecen; A que no termina deja esa masa `OPEN` y no autoriza más tiempo; C0 fallido para todo; B no rescata a A; la sección 5 prohíbe masas extra, `n` simbólico, `s = 4`, otros sustratos y `d = 2`; la promoción a `CURRENT_STATE` queda fuera, en otro commit y por decisión del usuario. El verificador por defecto no ejecuta B.

El parcial «las masas que sí terminan quedan certificadas» no amplía la hipótesis: H1–H3 siguen `UNDECIDED` si falta una masa, salvo el conflicto G-V-13.

**G-V-15.** Sección 5, presupuesto. Laguna. «900 s por masa y por clase de símbolo» no pone el techo «a lo sumo las cuatro declaradas». «One additional budget of the same size» para A5 no dice si es 900 s en total o 900 s por masa y por clase. No cambia la pregunta científica; sí permite estirar el cómputo sin una carta nueva. `no s = 4` no está definido (la dimensión interna ya es 4), así que no excluye nada.

**G-V-16.** Sección 6 frente a T3. Laguna. La lista de exclusiones es suficiente para la pregunta si T3 cita las formas cerradas ya certificadas y no las rederiva. Hoy T3 las mete en el certificado y la sección 6 dice que no se calculan. Falta el protocolo de una de las dos frases.

## 7. Alcance

La carta acierta al marcar como desconocidos `V_grp^max`, el lugar del máximo y su posición respecto de `r_in`, y al dejar la literatura de `∇ω` en `[UNVERIFIED]`. Hay dos frases que afirman como sabido algo que esta carta no ha comprobado.

No son excesos: heredan el contrato y el verificador la familia, `u`, `cos ω = n u`, `r_in = 1/sqrt(3)`, el soporte máximo `1` y las fórmulas de `c_H` y `c_{ω²}`. El borrador dice que no registra cómputo, candidato ni teorema. H1–H3 se declaran pruebas, no predicciones, y se niega cualquier ley para «cualquier QCA masivo isótropo».

**G-V-17.** Sección 6, última frase, frente a la sección 0. Redacción. «The 1D formula and Bernstein-type bounds are prior art» afirma un estado bibliográfico. La sección 0 dice que la lectura de los PDF no está hecha y que cualquier prior art es `[UNVERIFIED]`. Que el análogo unidimensional se pueda comprobar (C0) no lo convierte en literatura citada. El documento 2 menciona una cota de tipo Bernstein en una dimensión y no da fuente.

**G-V-01**, ya citada, cae también aquí: llamar «group speed» a la pendiente del nodo sin masa afirma una identificación que el verificador no comprueba y que la propia carta excluye al tachar `m = 0`.

## Objeciones

| Id | Dónde | Gravedad | Qué falla |
| --- | --- | --- | --- |
| G-V-01 | Sec. 0, Known | Redacción | La pendiente sin masa en el nodo no es velocidad de grupo |
| G-V-02 | T3 vs Sec. 1 y 6 | Laguna | Signos frente a `c_H` y `c_{ω²}` sin procedimiento |
| G-V-03 | A1 y zona de Brillouin | Redacción | `q_i = −π` no es un punto regular de `tan` ni de `cot` |
| G-V-04 | A2–A3 | Laguna | Equivalencia del despeje no probada; resultantes espurias |
| G-V-05 | A3 | Error demostrado | Repetir críticos no evalúa una componente donde `dΦ = 0` |
| G-V-06 | A5 vs T1 | Laguna | SOS racional no certifica un `V²` algebraico no racional |
| G-V-07 | Sec. 2 vs etapa 0 | Laguna | El signo de `±ω` se ordena y no entra en la lista |
| G-V-08 | Etapa 0, paso 4 | Laguna | Invariancia de `u` no es invariancia de `||∇_k ω||` |
| G-V-09 | Definición de `Φ` y C0 | Redacción | El mismo `Φ` no puede llevar `n²/3` y tener máximo `n²` |
| G-V-10 | B3 y Sec. 7 | Error demostrado | B no alimenta un veredicto, pero tiene uno; la malla «prueba que no hay máximo» |
| G-V-11 | B3 | Laguna | Tolerancia, cajas y máximo inflado no forman un predicado |
| G-V-12 | T3 y veredicto certificado | Laguna | T3 sale del álgebra de A4 |
| G-V-13 | Sec. 3 y Sec. 7 | Laguna | `REFUTED` choca con `UNDECIDED`; `CEILING_ONLY` no tiene hipótesis |
| G-V-14 | H3 | Laguna | «Eje coordenado» no está definido en el toro |
| G-V-15 | Sec. 5 | Laguna | Presupuesto de A5 y número de clases sin techo |
| G-V-16 | Sec. 6 vs T3 | Laguna | Exclusión y objetivo no dicen lo mismo |
| G-V-17 | Sec. 6 vs Sec. 0 | Redacción | Prior art afirmado con la lectura todavía abierta |

No hace falta reescribir la pregunta ni abrir la familia. Hace falta cerrar G-V-05, G-V-07, G-V-08, G-V-11, G-V-12 y G-V-13 antes de congelar; el resto es condición de implementación o redacción que cambiaría un veredicto si se deja como está.
