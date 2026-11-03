<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 77e5525c8d2af4ed579e8c34dce60926ff9a7627b03f15504ba41906844c3c88
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-03T17:49:28Z  fin: 2026-11-03T17:59:59Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0.md ; último commit observado: sin versionar ; sha256 de la copia enviada 8f68a1267a8ceb025ea2e9f564fbb38e58e7481a3f5dbeb2e5762141f02a1740
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-exec-review2-grok/extracto_current_state.md ; último commit observado: sin versionar ; sha256 de la copia enviada 26e13221c563702eaeb1b478a3f1481ee4e8c43df824413b04f59bd31eca3d89
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-exec-review-grok/informe_grok.md ; último commit observado: sin versionar ; sha256 de la copia enviada 1c2062ca8687ebece15201f031799aa0be2050e412ecde797b2e21f5ccc0c178
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-exec-review-grok/verificacion_autor.md ; último commit observado: sin versionar ; sha256 de la copia enviada ca95285e53022dde1b9e68b892ed51d745bf9362ff74bdf0165d27e61336ca59
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--c-across-lattices.md ; último commit observado: 8d0276e ; sha256 de la copia enviada 01a18c70a1b031e99ca4f944c9f6810f29b1327067138c8eb3ee089deca1ea3f
documento: /home/ignac/qca-causal-cones/reports/2026-09-14--weyl-dirac-gate-contract.md ; último commit observado: 2c7c2c9 ; sha256 de la copia enviada e0e3483380b0352198c64cbca64985a5240389b7fc70a2694c9a79f9a2f33d27
documento: /home/ignac/qca-causal-cones/reports/2026-09-14--weyl-dirac-exact-gate.md ; último commit observado: 2c7c2c9 ; sha256 de la copia enviada 4c6b11cea989070b4f6387df771a962773a078b1dad3ffaa54b6c050c2703403
documento: /home/ignac/qca-causal-cones/reports/2026-09-14--weyl-dirac-verification.md ; último commit observado: 2c7c2c9 ; sha256 de la copia enviada be6a67eb9c092088ffce58d2d2f34d18e0b3609ae38d33e4c0d5dc571ca4ef7b
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
entrada_grok.txt sha256 eb8620e75eefe42d46f7a8e955320638858c66cebcd9a1f0b3ab3ff5eeeb3c33
respuesta sha256 bf54949c2762084bc962a06a42db937bb98f843ae0ef76d50d38fedf27a1bbfa
-->

**Dictamen global: REPAIR_REQUIRED.** Hay dos reparaciones obligatorias (traza de L3; L4 reintroducida en el dominio). Las cinco reparaciones de la ronda 1 están aplicadas. El token definicional `OPEN_AFTER_ROW_SURVEY` es el correcto aunque L3 se cierre.

## L3 — REPAIR_REQUIRED

La comprobación que el informe cita no es la condición de nodo. El PASS, leído en otras líneas del mismo dossier, sí contiene esa condición algebraica. El informe traza el nodo a las líneas equivocadas y luego lo da por trazado.

La cita es esta: el nodo de L3 se remite al PASS de CS l. 462–464, al ítem congelado «Compute all first spatial derivatives and the full Hessian of the scalar Weyl symbol at zero; check isotropy including mixed entries», a «`∇u(0)=0`» y a `c_0 = r_in = 1/sqrt(d)` (CS l. 496). En el verificador ese ítem es la hessiana del símbolo escalar, `Hessian {a,b}`: segunda derivada de `u` en el origen igual a `−δ_ab/d`, entradas mixtas incluidas. La condición congelada pide otra identidad, sobre los generadores matriciales: `{T_a, T_b} = 2 c_0^2 δ_ab`.

Correspondencia con lo que sí está escrito:

- **`U(0)` escalar.** El verificador impone `matrix` en el origen menos la identidad igual a cero (`zero node`): `W(0) = I`. No se sigue de las derivadas de `u`.
- **Término lineal hermítico.** La derivación analítica, Sec. 4, escribe `H_W = i log W = (θ/sin θ) σ·v = (1/√d) Σ_j k_j + O(|k|²)`, con `H` el logaritmo continuo desde la identidad (contrato de la puerta). El verificador construye `spatial = i ∂W/∂k` y comprueba la unitaridad como identidad de Laurent. De esa identidad, derivada en el origen donde `W = I`, `∂W` es antihermítico y `spatial` hermítico. El informe no cita ni la fórmula ni esa identidad.
- **Sin traza.** En esa misma fórmula el término lineal es `σ·v`. En el verificador, `tr(W) = 2u` (`scalar trace`) y el gradiente escalar en cero es cero, luego la traza de `i ∂W/∂k` es cero. La frase citada «`∇u(0)=0`» está en la Sec. 5 analítica y solo dice que el prefactor masivo no tiene corrección lineal.
- **`{T_a, T_b} = 2 c_0^2 δ_ab`.** Con `T_j = Σ_j/√d` y `{Σ_i, Σ_j} = 2 δ_ij I` (Sec. 4 analítica) sale `{T_i, T_j} = 2 c_0^2 δ_ij I` y `c_0 = 1/√d`. El verificador lo comprueba aparte (`Clifford`, contra `2 (δ_ab/d) I`, y `massless matching`). La hessiana de `u` no es ese anticonmutador: fija la traza de la forma cuadrática de `u`, no la identidad de operadores.
- **Inclinación nula.** El contrato de la puerta, la derivación, el registro y el verificador no usan esa palabra. El contrato de la fase 0 la mete en el mismo paréntesis y declara equivalente `A(n)^2 = c_0^2 |n|^2 I`. Esa forma es la polarización del anticonmutador ya escrito, `A(n) = n_a T_a`, no un corolario de la hessiana. `∇u(0) = 0` anula el coeficiente de `I` en el término lineal; esa glosa no está en el dossier Weyl.

La frase que falla es: «Reading that check as the frozen untilted-node condition is the author's reading of a different certificate, recorded here for review», unida a «all except L4 a traced node» y a la celda «yes: L3, L5a». La primera presenta el ítem escalar como la lectura del nodo; las otras dos dan el nodo de L3 por trazado y a L3 por testigo. Lo que lo cierra: reescribir la traza cláusula por cláusula con las líneas de arriba y decir que la hessiana escalar no es el certificado; o retirar el nodo trazado de L3 y quitar L3 de la celda existencial. No hace falta ningún cálculo nuevo.

Aclaración, no error de la Sec. 3: «the line, square and BCC substrates each have a promoted admissible walk» no depende de L3. L5a está en la lista de filas calculadas y cae bajo el certificado de c-across-lattices l. 154–156, que sí nombra generadores hermíticos, inclinación nula y el anticonmutador.

## L4 — REPAIR_REQUIRED

La insuficiencia está bien fundada, y no usar `OUTSIDE_DEFINITIONS` es lo correcto. Dos frases posteriores vuelven a meter L4 en el dominio.

CS l. 762–789 separa `B`, `Γ` y `C_micro`, llama a `B(c_IR)` cono IR isótropo emergente (l. 769) y da `S(n̂) = 1/||n̂||_1` (l. 787, unidades de la Sec. 8). No hay `U(0)`, ni término lineal, ni anticonmutador. El certificado de l. 154–156 cubre filas calculadas; L4 está re-tabulada en l. 147. La pareja `(1/√3, 1/√3)` sale de esa línea y no se cruza con `[-1,1]^3`. El párrafo que retira «no tilt» y deja L4 «unclassified, not shown to be outside the domain» no convierte el hueco en exclusión ni en apoyo: la Sec. 3 dice que un nodo marcado no es testigo ni resultado de que ningún walk satura.

`OUTSIDE_DEFINITIONS` (contrato Sec. 3.4) es para cuando una definición congelada no rige, por ejemplo porque la clase no tiene nodo admisible. Aquí los documentos no muestran eso: no alcanzan para decidir. Dejar la fila sin clasificar es la lectura fiel. El resultado sigue siendo `OPEN_AFTER_ROW_SURVEY` (cantidad ausente), no `DEFINITIONS_CLOSED`.

Fallan estas dos frases. «the domain has five substrates (… cube, L4 …)» (F3). Y: «All rows in the domain have one traced source for the pair `(r_in, c_0)` … and all except L4 a traced node». El dominio de la Sec. 2.2 exige nodo admisible. El propio informe dice que L4 no es fila admisible. Esas frases lo recolocan dentro y solo le exceptúan el nodo. No es apoyo de (PH); es una clasificación que el estatuto «sin clasificar» prohíbe. Lo que lo cierra: contar el cubo como sustrato tabulado de pertenencia no establecida, y limitar «filas del dominio» a las que tienen nodo trazado.

## INTEGRIDAD — PASS, con la salvedad de L3

Las cinco reparaciones están aplicadas. L4: desaparecen «hence no tilt», «stated» y el uso de `h_B ≡ c_IR` como nodo; el resultado es `OPEN_AFTER_ROW_SURVEY`. L2 y L3: la pareja sale solo de l. 141 y l. 143; los vértices, aparte, de CS l. 486–488, que es donde están `N_d` y `C_micro`. L6b: CS l. 97–99 y l. 111, con la nota de que l. 88–94 y l. 106 son la numeración de `9bf3019`; el extracto confirma la frase de la revisión y `s = 6` en l. 111. L6c: hex-ceiling l. 156–157. El chequeo de contraejemplo es una sola frase y contiene los dos tokens, la no independencia, la lectura desde esta tabla (tres hipercubos, un hexágono regular, ningún paralelepípedo que no sea hipercubo), nunca `CONFIRMED` y la no autorización de una fase posterior.

Aclaración: esa frase es agramatical («which are not independent evidence …, are never `CONFIRMED`»). El contenido exigido está; el sujeto de «are never» queda colgando. No es otra reparación de fondo.

Conclusión que sí depende de una inferencia no certificada: el nodo de L3 «traced» y el «yes: L3» de la celda existencial, que identifican el ítem escalar con la Sec. 2.4. No dependen de ella los dos `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`: (PH⇒) usa solo hexágonos con `c_0 < r_in` en la tabla; (PH⇐) tiene testigo en la recta, el cuadrado y BCC por L5a; L4 marcado no es un resultado de que ningún walk satura.

Con L4 sin resolver, `OPEN_AFTER_ROW_SURVEY` sigue siendo el token aunque L3 pase. `DEFINITIONS_CLOSED` pide toda fila del dominio cerrada y la lista exterior explícita. Una fila sin nodo establecido es una cantidad ausente. Cerrar L3 no la elimina. Si L3 permanece sin traza válida, es un segundo hueco y el token tampoco cambia.

## Reparaciones obligatorias

1. L3: dejar de identificar la hessiana escalar, `∇u(0)=0` y `c_0 = r_in` con el nodo congelado. Citar `W(0)=I`, `H_W = (1/√d) Σ_j k_j` con `{Σ_i, Σ_j} = 2 δ_ij I`, las comprobaciones `Clifford` del verificador, y decir que «inclinación nula» no es una palabra de ese dossier: o se ata a la forma equivalente `A(n)^2 = c_0^2 |n|^2 I` vía el anticonmutador, o no se da el nodo por trazado. Mientras tanto, quitar L3 de «traced node» y de «yes: L3, L5a». No tocar el testigo BCC por L5a.
2. L4: sacar el cubo del recuento «the domain has five substrates» y no incluir L4 entre «all rows in the domain». Mantenerlo sin clasificar: ni admisible, ni `OUTSIDE_DEFINITIONS`, ni testigo, ni contraejemplo.

No hay más.
