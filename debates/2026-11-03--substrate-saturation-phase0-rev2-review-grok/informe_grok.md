<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 89f5d673fe94bb19daf2c658f5b7d58684a76788bc2df54867c80451b97b12ef
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-03T17:09:24Z  fin: 2026-11-03T17:19:46Z
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: sin versionar ; sha256 de la copia enviada def7e7e5b98b3e2110db4c05ddfb53330d7cabc0da807743cf2220ea71a33693
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-draft-review-grok/informe_grok.md ; último commit observado: sin versionar ; sha256 de la copia enviada 00b110c8fe9a657a1e95e98804aeafddc74ca2da4e988d66b09f5b69bf93fca2
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--c-across-lattices.md ; último commit observado: 8d0276e ; sha256 de la copia enviada 01a18c70a1b031e99ca4f944c9f6810f29b1327067138c8eb3ee089deca1ea3f
documento: /home/ignac/qca-causal-cones/theory/C_ACROSS_LATTICES_GATE.md ; último commit observado: 30672ba ; sha256 de la copia enviada b58deeec91184fbf976a6cb857c8e935ec7d4a4e52d6608a62768452759e34e3
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--c-across-substrates-answer.md ; último commit observado: 98e9a69 ; sha256 de la copia enviada 4d35f826420fc84096af1ead8bf98366d3c6763c76c7de93b7d9faacbe2329df
documento: /home/ignac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--l6b-triangular-row.md ; último commit observado: a19e480 ; sha256 de la copia enviada 201a62e186976639dc351da55355820b8327dff971e0badd53a58ed9835afe4c
entrada_grok.txt sha256 d9a23736727240948c3406091521b3860e18bd48afcd4a54fa28ef996d16e2d6
respuesta sha256 92d3e1a6f534bd2f8b2cc51645487d33df3c73d463d731d6778db69c0461fc07
-->

**Dictamen global: REPAIR_REQUIRED.** Hay una reparación obligatoria, de trazabilidad en la exclusión de L6b. El dominio de (PH), los cuantificadores, la no equivalencia con (PS′) y el carácter no confirmatorio de la fase 0 aguantan el contraste con los adjuntos.

## 1. Dominio y circularidad — PASS

**(a)** La condición tiene definición propia y no depende de que `C_micro` sea un hipercubo. El borrador, Sec. 2.4, fija `c_0` como la velocidad del cono isótropo sin inclinación en el nodo sin masa mediante `{T_a, T_b} = 2 c_0^2 delta_ab`, «as certified per row» en el informe c-across-lattices, Sec. 4. Ese informe certifica la fórmula en todas las filas calculadas, incluidas L6a, L6c, L6d y L6f, cuyo `C_micro` es un hexágono. El contrato hexagonal da la forma equivalente, sobre el término lineal y no sobre los vértices: `A(n)^2 = c_0^2 |n|^2 I`, con `A` sin traza (`HEX_CEILING_GATE`, Sec. 1). El mismo contrato separa ese cono de la isotropía de representación de P17, que sí excluye la red triangular.

**(b)** L6a, L6c, L6d y L6f quedan dentro: `s = 2`, `d = 2`, cono certificado, clases declaradas, `c_0 < r_in`. No refutan (PH⇒). Un walk de `W_hex` o de `W_hex^sym` con `c_0 = r_in` también queda dentro: ambas clases exigen `s = 2` y nodo isótropo, y su `C_micro` es un hexágono regular, no un hipercubo. `W_hex^sym` está declarada en `HEX_SUPREMUM_GATE`, Sec. 2, contrato que la Sec. 2.2 incluye en el dominio. Saturar no borra el nodo: el informe hexagonal, Sec. 3, estudia precisamente `c_0 = r_in` junto con el cono. Ese testigo refutaría (PH⇒). La Sec. 4 y la Sec. 7 lo dicen.

**(c)** La restricción no vuelve verdadero el bicondicional por construcción. El cono existe en el hexágono, que no es hipercubo, y la clase hexagonal sigue abierta: T1, el soporte mínimo, S13 y S19 no cierran `W_hex`. `OUTSIDE_DEFINITIONS` es la ausencia de nodo, no el dejar de ser hipercubo ni el hecho de saturar.

Aclaración, no error. «Admissible» no está definido como predicado distinto del cono más la pertenencia a las clases declaradas. No debe leerse como el grafo admisible de P17. Conviene una frase que lo diga. En la Sec. 7, «Finding one would refute (PH⇒)» solo vale para un testigo dentro del dominio: la misma frase deja abierto «larger `s`», y `s ≠ 2` está fuera (Sec. 2.2 y Sec. 4) y no refuta (PH). No hallarlo no prueba (PH), y eso la Sec. 7 sí lo dice.

## 2. Lógica — PASS

(PH⇐) es existencial por sustrato: hipercubo implica que existe un walk admisible con `c_0 = r_in`. (PH⇒) es universal: si `C_micro` no es hipercubo, todo walk admisible cumple `c_0 < r_in`. La Sec. 2.1 impide leer el existencial como «todo walk satura»; L3s4 queda marcado `s = 4` y fuera. La Sec. 2.5 impide leer el universal como hueco uniforme. Con la cota `c_0 ≤ r_in` (Sec. 2.6) y sin filas por encima, la negación de saturar es la desigualdad estricta. Las etiquetas ⇐ y ⇒ no están cruzadas.

Que un cuerpo fuera del dominio no esté en ningún lado es coherente: el bicondicional no se evalúa ahí. La Sec. 1, la Sec. 3.4 y la Sec. 4 coinciden en que eso no es contraejemplo ni apoyo. No es una implicación material que se vuelva verdadera porque el conjunto de walks sea vacío.

La afirmación de que (PS′) no equivale a (PH) es correcta. El consecuente de (PS′) es «los generadores reducidos son `d` y linealmente independientes»; el de (PH) es «hipercubo salvo escala e isometría». Un rombo de 60° es un paralelepípedo y no un hipercubo. Además (PS′) se restringe a la clase producto y no hereda el corte del nodo. En las filas adjuntas no se separan las dos lecturas: segmento, cuadrado y cubo caen en ambas, y el hexágono de `W_hex` (tres direcciones a 120° en `d = 2`) no es paralelepípedo ni hipercubo. La Sec. 3.5 lo registra. La geometría del zonotopo que usa el borrador —`conv{sum ε_i a_i} = sum [-a_i, a_i]`, paralelepípedo exactamente con `d` generadores independientes— cuadra con esos ejemplos.

Aclaración. (PS′) afirma «el techo se alcanza» en la clase producto sin repetir el corte del nodo, así que en el rombo hablaría de un `c_0` que puede no existir. No invalida la no equivalencia: conviene la misma cláusula `OUTSIDE_DEFINITIONS`, para que ese cuerpo no caiga del lado «se alcanza». La frase «no verdict on (PS′) beyond the counterexample test of Sec. 4» sobra: la Sec. 4 solo define contraejemplos de (PH).

## 3. Trazabilidad — REPAIR_REQUIRED

Sustentado por los adjuntos:

- Dominio `s = 2`. L5b y L3s4 tienen `s = 4` en la tabla de la Sec. 4 del informe c-across-lattices (también en el contrato padre). L5b además satura; excluirlo por `s` no esconde un contraejemplo de (PH).
- L4: un solo par, en paso más largo 1, `r_in = c_0 = 1/sqrt3`, tomado de esa misma tabla, con prohibición de cruzarlo con `C_micro = [-1,1]^3`, `r_in = 1`, `c_IR = 1` de CS Sec. 8. Los dos miembros del par están en la fuente elegida y coinciden con el reescalado de la síntesis.
- Tres campos separados en la Sec. 3.3, y la prohibición de leer un hueco de subclase como «el sustrato no satura».
- Alcance de clase, coincidente con la síntesis (Secs. 1 y 2) y con el informe hexagonal: T1 es el supremo uniforme `sqrt3/2` solo en la subclase antipodal `n = 3`; el soporte mínimo, M1-B13 y M1-B19 son huecos cualitativos, sin cota bajo `r_in`, este último par en `W_hex^sym` con `F` dentro de S13 o S19; la clase hexagonal entera sigue abierta. El contrato M1 define S13, S19 y `W_hex^sym`, pero no contiene esos veredictos: el respaldo es la síntesis, no el contrato. Llamar `W_hex^sym` al resultado de soporte mínimo es un levantamiento correcto de una prueba que no supone forma de producto, no una cita literal del informe hexagonal.

No sustentado. La frase exacta es la de la Sec. 2.2: «L6b (`s = 6`, CS l. 94 and l. 106: «`s = 6`, not the parent's `s = 2`», fixed by the promoted L6B_TRIANGULAR_ROW gate, which supersedes the parent contract's declaration)». Las líneas 94 y 106 de CURRENT_STATE no se adjuntan, y esa cita inglesa no está en ningún adjunto. El informe L6b sí sostiene el contenido numérico: Sec. 1, `s = 6` por celda (tres aristas, `C^2` cada una); Sec. 2, el `s = 2` del padre cuenta por arista, no por celda. No sostiene lo demás. Dice «Recorded, not repaired in the parent» y, en la cabecera, que ese informe no promociona nada. El contrato padre, aún adjunto, declara L6b con `s = 2`. La tabla del informe de retículos lo deja en `s = 2` y `OPEN`, sin codificar: es el estado anterior, no una medición que contradiga el `s = 6`. Quien llama promocionada a la fila es la síntesis («L6b row (promoted)», `s = 6`, `c_0 = 1/3`).

Qué lo cierra: citar informe L6b, Secs. 1 y 2, para `s = 6`, y la síntesis para el carácter promocionado de la fila. Decir que el contrato padre no fue enmendado y que su tabla sigue en `s = 2`. Mantener la exclusión del dominio `s = 2`. Quitar la cita de líneas no adjuntas y el verbo «supersedes the parent contract».

Aclaración. En la fila L4 de esa tabla el rótulo sigue siendo `cube [-1,1]^3` junto a `r_in = 1/sqrt3`. La prohibición de cruzar pares ya está; media frase evitaría tomar los vértices del rótulo y el radio de la columna. La síntesis, en su tabla de BCC, no marca `s = 4` en la fila donde agrupa a L5b: el borrador cita la fuente que sí lo marca.

## 4. Independencia — PASS

La fase 0 queda como auditoría de definiciones, sin valor confirmatorio. `DEFINITIONS_CLOSED` se limita a «defined well enough to be tested for refutation. Nothing more» (Sec. 5). `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE` exige, en la misma frase, que no es evidencia independiente: la frase se leyó de una tabla con tres formas hipercúbicas y un hexágono, y sin un paralelepípedo que no sea hipercubo; el veredicto no puede ser `CONFIRMED`. «No outcome of this gate authorizes any later phase»: ese veredicto no es condición ni motivo para un test posterior. La Sec. 7 se titula como no autorizada y exige otra carta, con una forma o un soporte que no esté en la tabla; no hallar saturación hexagonal no prueba (PH).

Ninguna frase concede apoyo. La Sec. 0 llama a (PH) `[UNVERIFIED]` y dice que la conclusión no es «the conjecture survives». La Sec. 3.5 manda anotar que la tabla no separa (PH) de (PS′): es el mismo hecho ya dado como conocido, no un pase a fases posteriores.

Aclaración. La Sec. 3.5 está en imperativo («Record … that the table contains no…») y presupone el hallazgo. En condicional no cambiaría el fondo y no podría leerse como dictar el resultado antes del recorrido.

## Reparación obligatoria

1. **Sec. 2.2, la exclusión de L6b.** Reescribir la cita como arriba. La exclusión por `s = 6` puede quedarse; no pueden quedarse la línea de CURRENT_STATE no adjunta, la cita entre comillas ni «supersedes the parent contract's declaration».

No hay otra reparación obligatoria. Los puntos 1, 2 y 4 pasan; las notas de esos puntos son aclaraciones.
