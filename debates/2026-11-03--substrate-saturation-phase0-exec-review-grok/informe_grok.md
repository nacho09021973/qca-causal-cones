<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 192915864d16a6d764657f4f5bb65e621b79db415df97c81633999bdc99c6b52
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-03T17:32:57Z  fin: 2026-11-03T17:44:08Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0.md ; último commit observado: sin versionar ; sha256 de la copia enviada 1253fd075a57e5c104e013e5afcff0538f3886a99d8ed166664bb5bb2865f0e2
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-exec-review-grok/extracto_current_state.md ; último commit observado: sin versionar ; sha256 de la copia enviada 925a3ea0eac896710612ae89a67d9585460a65474dfcb8283166f80435fe1eb0
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--c-across-lattices.md ; último commit observado: 8d0276e ; sha256 de la copia enviada 01a18c70a1b031e99ca4f944c9f6810f29b1327067138c8eb3ee089deca1ea3f
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--l6b-triangular-row.md ; último commit observado: a19e480 ; sha256 de la copia enviada 201a62e186976639dc351da55355820b8327dff971e0badd53a58ed9835afe4c
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--hex-supremum-b19.md ; último commit observado: f16c835 ; sha256 de la copia enviada 08d5c724a7c99c1a4c89b11ab2c65941c221f6aa5b6a8b460f4cbad474af0d89
entrada_grok.txt sha256 8792f3bd52fd9f7a9ccc836c194e7ccffdd9df8f2d01a6c3831cf5c87222087a
respuesta sha256 3117ee5bba4c1a0eda4197439058c11c9bcaf0bde0ca81cd1fc67cfc8eed1ede
-->

**Dictamen global: REPAIR_REQUIRED.** No hay circularidad en (PH), el dominio o los cuantificadores, y F2 no contamina (PH). No se sostienen `DEFINITIONS_CLOSED` ni la forma exigida por la Sec. 5 para `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`. La ausencia de contraejemplo en la tabla, en cambio, sí se sostiene.

## 1. DEFINICIONES — REPAIR_REQUIRED

No hay círculo. «Admisible» sigue siendo clase declarada más nodo isótropo sin inclinación en el término lineal (contrato Sec. 2.2 y 2.4), no la forma de `C_micro`. El hexágono queda dentro del dominio. «Se alcanza el techo» se lee como existencia (campo (c)); un hueco de subclase no se lee como «ningún walk satura».

La aplicación de Sec. 2.4 falla en L4. El informe dice: «i.e. `h_{B(c_IR)} ≡ c_IR`, a ball centred at the origin, hence no tilt» y «Isotropy and zero tilt are thus stated in promoted text, but not through the same certificate as the other rows; recorded, not flagged.»

`h_{B(c_IR)} ≡ c_IR` no basta para «sin inclinación» en el sentido congelado.

- Esa identidad no está en CS l. 784–789. Ahí está `S(n̂) = h_B/h_C = 1/||n̂||_1` (l. 787), con `c_IR = 1` (l. 784). Hace falta `h_C(n̂) = ||n̂||_1` (l. 782), fuera del tramo citado. El cuantificador «para `||n̂||_2 = 1`» está en l. 780.
- Aunque se conceda la bola centrada, el contrato pide `U(0)` escalar, término lineal hermítico sin traza, `{T_a, T_b} = 2 c_0^2 delta_ab`, inclinación nula, o equivalente `A(n)^2 = c_0^2 |n|^2 I`. Ninguna de esas fórmulas está en CS l. 764–789. L. 769 dice «emergent isotropic IR light cone»: isotropy de `B`, no el certificado algebraico. L. 789, dentro del tramo citado, dice que `S = 1` solo en los ejes; eso no es inclinación nula del generador.
- CS Sec. 8.1 (l. 762–769) separa `B`, `Γ` y `C_micro`. El certificado de c-across-lattices l. 154–156 no cubre L4; el informe lo reconoce y aun así da el nodo por «stated» y no lo marca.

Lo que lo cierra: no llamar «stated» a esa inferencia; si se menciona la bola, citar l. 780–787 y decir que es geometría de `B` en unidades de CS Sec. 8, no el certificado de Sec. 2.4. Marcar L4 según Sec. 3.4, sin resolverlo. Con eso, `OUTSIDE_DEFINITIONS: none` y `DEFINITIONS_CLOSED` no caben: el resultado definicional es `OPEN_AFTER_ROW_SURVEY`.

La pareja `(r_in, c_0) = (1/sqrt3, 1/sqrt3)` sí sale solo de c-across-lattices l. 147, sin cruzar `[-1,1]^3` con ese radio. Eso está bien y no salva el nodo.

## 2. TRAZABILIDAD — REPAIR_REQUIRED

Comprobado y correcto: tabla masiva l. 140–152 (L4 en l. 147; L6b padre en l. 152 con `s = 2`, OPEN, not encoded); pasos l. 106–113; certificado de filas computadas l. 154–156; L6b informe l. 24 (`s = 6`, tres aristas, `C^2` cada una) y l. 70–71 (la `s = 2` del padre cuenta por arista). La exclusión `s = 6` es la correcta: el padre no fue enmendado.

Errores:

- L6b, columna Source: «CS l. 88–94, l. 106». En el extracto, l. 88–94 es el cierre de otra puerta y el encabezado de la promoción; la frase «a revision of `C_ACROSS_LATTICES` restricted to row L6b» está en l. 97, y `s = 6` en l. 99. L. 106 es la instrucción de usuario; «`s = 6`, not the parent's `s = 2`» está en l. 111. El contrato trae esos mismos números; copiarlos no los hace verdaderos. Cierre: citar CS l. 97–99 y l. 111. No cambia la exclusión.
- L2 y L3, columna «Single source»: «l. 141; CS l. 484–496» y «l. 143; CS l. 484–496». La apertura toma además, para L1–L3, `c_0 = r_in = 1/sqrt(d)` de CS l. 484–496. Sec. 2.4 exige la pareja de exactamente una fuente. La Sec. 5 del informe («one traced source … (L4 from l. 147 only)») contradice esas dos celdas. Mismas unidades, pero dos fuentes. Cierre: una sola cita para la pareja; si los vértices salen de CS l. 486–490, decirlo aparte.

Aclaración, no error de fondo: L6a, L6d y L6f sí están en el soporte mínimo, y L6c no. Hex-ceiling l. 156 nombra L6a, L6d y L6f y corta en «it does not»; «contain JDW L6c (19 points)» es l. 157. L. 152 está en blanco. El informe dice «hex-ceiling l. 152–156» y, para L6c, «l. 156». La pertenencia es verdadera; la localización de L6c no. Cierre: l. 156–157. L6c en S19, dentro de `W_hex^sym`, está en el informe B19, Sec. 3 («includes the support of JDW L6c»), y en CS Sec. 14. `g = 1/3` en hex-ceiling l. 138–139 y el techo T1 en l. 125 cuadran.

## 3. F2 — PASS

La hipótesis de signos afecta solo a (PS′). El contrato escribe `F = {sum_i ε_i a_i}` y `conv F = sum_i [-a_i, a_i]`. Si una amplitud se anula, el soporte real puede ser menor y esa igualdad falla. Eso no está tabulado por fila. El informe no da veredicto sobre (PS′), que es lo que pide el contrato.

No compromete (PH). Forma de `C_micro`, hipercubo sí/no, paralelepípedo y `r_in` salen de vértices certificados y de la pareja de la fuente única, no de los factores. Leer «direcciones de zonotopo» como aristas de `C_micro` es correcto: los politopos de la tabla son zonotopos y sus generadores geométricos se leen de las aristas. El límite también es correcto: F2 dice que no queda establecido que coincidan con los desplazamientos de los factores, y que (PS′) no se puede ensayar hasta explicitar la hipótesis. F1 no usa esa hipótesis para afirmar (PH); solo registra que la tabla no separa predicados que coinciden en segmento, cuadrado, cubo y hexágono regular.

## 4. NIVELES LÓGICOS — PASS

Ninguna frase de los tres campos ni de la Sec. 3 convierte un walk, una subclase o un soporte acotado en «el sustrato no satura».

- (a) es la comparación exacta de esa fila. Aclaración de notación: en L6a el paréntesis `(1/sqrt3)`, y en L6c, L6d y L6f `(sqrt3/2)`, son cocientes `c_0/r_in`, no valores de `c_0` (L6a tiene `c_0 = 1/2`). La desigualdad es la correcta y la tabla trae los dos números. Conviene etiquetar el cociente; no es un error de cuantificador.
- (b) mantiene T1 en la subclase antipodal `n = 3`, T2 en `F` dentro de `{0} ∪ vert(H)`, y M1-B13/B19 en `W_hex^sym` con `F` dentro de S13 o S19, huecos cualitativos, clase hexagonal OPEN.
- (c) dice «no promoted saturating walk; **not** "no walk saturates"». L6c lo repite en su sustrato más fino.
- Sec. 3 habla de walks promocionados: ningún hexágono promocionado con `c_0 = r_in`; cada sustrato hipercubo de la tabla tiene un walk promocionado que sí iguala. No dice que todo walk admisible del cubo sature, ni que ninguno hexagonal pueda hacerlo.

El salto de nivel de L4 (función soporte de `B` leída como nodo algebraico) está en el párrafo `OUTSIDE_DEFINITIONS`, no en estos tres campos. Ya está contado en el dictamen 1.

## 5. VEREDICTO — REPAIR_REQUIRED

`DEFINITIONS_CLOSED` no cumple la Sec. 5. Falta el nodo de L4 en el sentido congelado, la lista `OUTSIDE_DEFINITIONS` no marca esa fila, y L2 y L3 no tienen una sola fuente. El sentido permitido («solo que (PH) está definido lo bastante para intentar refutarlo») no cura un cierre que la propia sección no autoriza. Corresponde `OPEN_AFTER_ROW_SURVEY`.

El chequeo de contraejemplo sí cumple la Sec. 4. Contra (PH⇒) no hay sustrato no hipercubo en el dominio con un walk promocionado en `c_0 = r_in`. Contra (PH⇐) no hay resultado promocionado exacto de que ningún walk admisible satura en un hipercubo del dominio: un nodo mal cerrado en L4 no es ese resultado. El token `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`, en las dos direcciones, es el correcto. No es `REFUTED_BY_ROW_<row>`.

No cumple la forma de la Sec. 5. El token ocupa una frase; «This is not independent evidence for (PH): … three hypercube shapes and one non-hypercube shape and no parallelepiped that is not a hypercube (F1). Never `CONFIRMED`» va detrás; «No outcome of this gate authorizes any later phase» es otro párrafo. El contrato exige la salvedad en la misma frase que el veredicto, y que quede dicho que ningún resultado autoriza una fase posterior. El contenido está, partido. Cierre: una sola frase con los dos tokens, que no son evidencia independiente, que el enunciado se leyó de esta tabla (tres hipercubos, un hexágono regular, ningún paralelepípedo que no sea hipercubo), que no es `CONFIRMED`, y que ningún resultado de esta puerta autoriza una fase posterior.

## Reparaciones obligatorias

1. L4: retirar «hence no tilt» y «stated in promoted text»; no usar `h_B ≡ c_IR` como certificado de Sec. 2.4; marcar la fila (Sec. 3.4) y sustituir `DEFINITIONS_CLOSED` por `OPEN_AFTER_ROW_SURVEY`.
2. L2 y L3: una sola fuente para la pareja `(r_in, c_0)`; separar, si hace falta, la cita de vértices de CS l. 486–490. Ajustar la frase de la Sec. 5 que dice que toda fila tiene una sola fuente.
3. L6b: cambiar CS l. 88–94 y l. 106 por l. 97–99 y l. 111. Mantener informe L6b l. 24 y l. 70–71, y la tabla padre l. 152.
4. L6c: citar hex-ceiling l. 156–157, no l. 156.
5. Unir, en una sola frase, el token de contraejemplo, la salvedad de no independencia y la prohibición de autorizar fases posteriores.

No hay más reparaciones. F2, la separación de los tres campos y la Sec. 3 pueden quedarse como están, salvo etiquetar el cociente del campo (a) si se toca ese párrafo.
