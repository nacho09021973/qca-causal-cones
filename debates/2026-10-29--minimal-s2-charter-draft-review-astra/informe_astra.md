<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.165.0)
inicio: 2026-10-29T10:21:12Z  fin: 2026-10-29T10:28:41Z
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: sin versionar ; sha256 de la copia enviada 8541cf728da5baf87f9a414783953d98d72ae4ba708daf98b72aaf1ad296afc6
documento: /home/ignac/qca-causal-cones/theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md ; último commit observado: 05eb1eb ; sha256 de la copia enviada 2ef8690e5eb4c4e0799ae6c38038b988d0fe7f7ea64fdcc596095d5bab257e26
documento: /home/ignac/qca-causal-cones/theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md ; último commit observado: 88b07ed ; sha256 de la copia enviada bb12375faff7b16fcd5e40c85995dc9fe8f374f6d26b51c60819fa94bba176a6
documento: /home/ignac/qca-causal-cones/reports/2026-09-14--massless-rigidity-source-audit.md ; último commit observado: 5845eda ; sha256 de la copia enviada 468918501dd6bf84603cf78c201cb956ef11352c09506c98d3eb2c2999b05e72
documento: /home/ignac/qca-causal-cones/biblioteca/1708.00826v2.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81
entrada_astra.txt sha256 067bee5daddadd19db6e72ac8cad216e5ba1f4b2534c91d09c36e5e32b9cbc1b
respuesta sha256 71554f201d2741fe15a29dabcfcd76b0175dfddb03e7e197e1e4032bab2385e6
-->

**Veredicto global: NOT_READY.** Hay dos errores matemáticos concretos —la identidad propuesta para la partición en caras y la inclusión de clases con grupo espacial \(O\)—, además de ambigüedades sobre unidades, nodos y cobertura algebraica que deben resolverse antes de congelar.

Supuestos de esta revisión: uso exclusivamente los cinco documentos suministrados. Las comprobaciones bibliográficas se refieren al texto extraído del Documento 5; no certifico los bytes ni la tipografía del PDF. Los resultados previos cuyos certificados no están adjuntos quedan **[UNVERIFIED]** como resultados del repositorio. Los cálculos siguientes son derivaciones manuales de esta revisión.

## 1. Pregunta y cuantificadores — REPARAR

Están fijados \(s=2\), los ocho desplazamientos activos, ausencia de término local, convención de Fourier, unidad temporal y ausencia de la Eq. (2). También puede fijarse una **unión exhaustiva de clases** antes de conocer su enumeración: no es necesario escoger un único \(G,R\), siempre que «todos» tenga una definición inequívoca y ninguna clase se descarte después por conveniencia.

Quedan tres problemas.

**Nodos y sectores.** «Declared per candidate» no determina si se cuantifica sobre todos los nodos admisibles o sobre uno seleccionado. Un símbolo con varios nodos podría permitir seleccionar retrospectivamente el que satisface la igualdad. Para \(s=2\), el cono \(\omega_\pm\) ocupa todo el espacio interno; no hay otro bloque espectador, pero siguen pendientes el cuantificador sobre nodos y la convención local de cuasienergía.

La formulación más clara sería:

\[
\forall(G,S_+,[R]),\ \forall U,\ \forall(k_\star,\omega_\star)
\text{ que satisfagan las condiciones de admisión},
\quad c_0(U,k_\star)=c_{\rm strict}^{\rm iso}(U).
\]

Un contraejemplo sería una sola tupla admisible que incumpla la igualdad.

**Unidades.** El Documento 2 usa \(h=(\pm1,\pm1,\pm1)/\sqrt3\); el Documento 1 usa vectores sin normalizar, pero conserva \(1/\sqrt3\) en su presentación del certificado basal. Bajo ese cambio,

\[
U_{\rm nuevo}(k)=U_{\rm antiguo}(\sqrt3\,k),\qquad
c_{0,\rm nuevo}=\sqrt3\,c_{0,\rm antiguo},
\]

y el cuerpo estricto también se dilata por \(\sqrt3\). Por tanto, si se acepta el certificado previo, sus velocidades en las unidades nuevas son **\(1\)**. La igualdad es invariante; el número no lo es.

**Dominio de coeficientes.** «Álgebra exacta» no debe significar que solo se admiten coeficientes algebraicos. Un sistema definido sobre un cuerpo algebraico puede describir soluciones con parámetros reales trascendentes. Esa cobertura debe declararse.

**A-R1-01 — Secs. 1–2; laguna.** Fijar el cuantificador sobre todos los nodos admisibles, el sector completo de dos bandas y la rama local de cuasienergía. Precisar también la red y su toro recíproco: los vectores declarados generan la red BCC \(\Lambda=\{x\in\mathbb Z^3:x_1\equiv x_2\equiv x_3\pmod2\}\).

**A-R1-02 — Sec. 0 y tabla de geometría; error demostrado de normalización.** Separar explícitamente el certificado histórico en unidades normalizadas de su transporte a las unidades nuevas; sustituir por \(1\) cualquier velocidad basal referida a estas últimas.

## 2. Definición de isotropía y comparación con P17 — ERROR

La definición propuesta es una restricción legítima, pero **no coincide con la Definición 1 de P17 sin la Eq. (2)**.

En P17, p.2, la definición exige una representación unitaria proyectiva y transitividad sobre cada subconjunto de generadores del mismo orden. Para \(\mathbb Z^3\), todos los generadores no nulos tienen orden infinito, por lo que corresponde transitividad sobre \(S_+\). La definición no fija cuatro generadores ni excluye transformaciones que invierten la orientación. En p.3 se contempla también \(S_+=S_-\).

En el contrato:

- \(|S_+|=4\) y \(S_+\cap(-S_+)=\varnothing\) seleccionan una presentación concreta del soporte.
- Se excluyen los grupos con reflexiones.
- Se fija una métrica cúbica. Dentro de esa métrica, todo automorfismo lineal del conjunto de ocho vértices es una simetría del cubo: excluir grupos de rotaciones fuera de \(O\) no pierde rotaciones que preserven ese soporte. Sí restringe la clase general considerada en P17.

**No exigir fidelidad es razonable.** En P17 no figura como hipótesis independiente de la Definición 1; aparece vinculada a la Eq. (2) y se exige después en la exposición. Aquí debe distinguirse la fidelidad proyectiva:

\[
\ker_{\rm proj}R=\{g:R_g\text{ es escalar}\}.
\]

Si \(g\neq e\) está en ese núcleo y mueve algún generador, la covarianza hace iguales sus coeficientes y viola la Eq. (2). Eliminar esa ecuación justifica incluir representaciones no fieles; no justifica identificarlas con las fieles.

**El error interno es incluir \(O\).** El grupo completo de rotaciones del cubo es transitivo sobre los ocho vértices. Por ello no preserva ningún subconjunto de cuatro vértices. **No existe ningún par \((O,S_+)\) de la Sec. 2.** Las filas anunciadas para \(E\) «under \(O\)» y para representaciones reducibles de \(O\) no pertenecen a esta clase congelada.

**A-R1-03 — Sec. 2 y techos; redacción.** Describir la clase como «rotaciones propias del cubo, presentación orientada de cuatro generadores y sin Eq. (2)», no como toda la clase de P17 al retirar únicamente esa ecuación. Definir fidelidad en \(PU(2)\).

**A-R1-04 — Paso 0.2 y A2; error demostrado.** Retirar las filas con grupo espacial \(O\) de la enumeración principal. Si se estudia la restricción de una representación de \(O\) a un grupo permitido, etiquetarla bajo ese grupo y demostrar la restricción.

## 3. Anticipaciones A1–A4 — ERROR

### A1: tetraedro correcto; desplazamiento de la cara incorrecto

Escribamos

\[
T_h=A\quad(h\in S_+),\qquad T_h=B\quad(h\in-S_+).
\]

La identidad de desplazamiento cero es

\[
4(A^\dagger A+B^\dagger B)=I.
\]

Para el tetraedro \(S_+=\{h:h_xh_yh_z=1\}\), el desplazamiento \(\ell=(0,2,2)\) tiene exactamente los pares

\[
(1,-1,-1)\longrightarrow(1,1,1),
\]
\[
(-1,-1,-1)\longrightarrow(-1,1,1).
\]

El primero está dentro de \(S_+\); el segundo, dentro de \(S_-\). Luego

\[
A^\dagger A+B^\dagger B=0,
\]

en contradicción directa con la normalización. Esta contradicción es algebraica: no necesita invocar positividad.

Para la cara \(S_+=\{(1,y,z):y,z=\pm1\}\), el desplazamiento propuesto \(\ell=(2,0,0)\) da cuatro pares

\[
(-1,y,z)\longrightarrow(1,y,z),
\]

y por tanto la ecuación correcta es

\[
4B^\dagger A=0.
\]

**No** da \(A^\dagger A+B^\dagger B=0\). Por ejemplo,

\[
A=\tfrac12\operatorname{diag}(1,0),\qquad
B=\tfrac12\operatorname{diag}(0,1)
\]

satisfacen esa ecuación y la normalización, aunque no todas las demás identidades de unitariedad.

El argumento de vaciedad se repara usando un desplazamiento **tangencial** a la cara, por ejemplo \((0,2,2)\). Sus dos pares dan de nuevo \(A^\dagger A+B^\dagger B=0\).

### A2: correcta con precisión sobre el grupo

Las rotaciones axiales de media vuelta actúan sobre las cuatro diagonales corporales como las tres dobles transposiciones de \(S_4\). Estas, junto con la identidad, forman el núcleo \(V_4\) de

\[
S_4\longrightarrow S_3,
\]

obtenido mediante la acción sobre las tres particiones en dos pares. La representación bidimensional estándar de \(S_3\), compuesta con este cociente, da \(E\). Por tanto,

\[
E(v)=I_2\qquad(v\in V_4).
\]

En \(2O\), el núcleo correspondiente es la **preimagen \(Q_8\)** de ese \(V_4\), no un \(V_4\) de medias vueltas dentro de \(SU(2)\). La afirmación sobre \(E\) es correcta; su aplicación a una clase espacial \(O\) no lo es, por el problema del punto 2.

### A3: correcta para un polinomio de Laurent finito en un toro

Sea

\[
p(z)=\sum_{a\in F}c_a z^a,\qquad |p(z)|=1.
\]

Si \(F\) contiene al menos dos exponentes, elijamos una forma lineal que tenga máximo único \(a_+\) y mínimo único \(a_-\) en \(F\). El coeficiente de \(z^{a_+-a_-}\) en \(p\,p^*\) es únicamente

\[
c_{a_+}\overline{c_{a_-}}\neq0.
\]

Pero \(p\,p^*=1\) exige que ese coeficiente no constante sea cero. Contradicción. Así, \(p=c z^a\), con \(|c|=1\).

Como segunda caracterización, \(p\,p^*=1\) hace a \(p\) una unidad del anillo de Laurent, cuyas unidades son constantes no nulas por monomios. Con ocho coeficientes activos, la clase escalar es vacía. «Trivial» no debe confundirse con identidad: un monomio puede representar una traslación.

### A4: correcta como posibilidad geométrica

La rotación

\[
r(x,y,z)=(x,-z,y)
\]

genera un \(C_4\) transitivo sobre la cara \(x=1\). Ese grupo no contiene \(V_4\). Esto comprueba la admisibilidad del **par geométrico**, no la existencia de un símbolo unitario con cono admisible.

La declaración retrospectiva es útil, pero no convierte las anticipaciones en predicciones anteriores al descubrimiento. Además, el Paso 0 está escrito como una orden de confirmarlas: «show that the ideal is (1)» y «follow from 1».

**A-R1-05 — A1 y Paso 0.1; error demostrado.** Corregir el desplazamiento para la cara y conservar los pares que producen cada identidad.

**A-R1-06 — Sec. 0 y Paso 0; laguna.** Reformular el paso como «verificar o refutar A1–A4». Registrar separadamente antecedentes retrospectivos, correcciones de esta revisión y trabajo prospectivo. Precisar \(Q_8\) en A2 y «par geométrico» en A4.

## 4. Pasos 0′, 0, 4a y 4b — REPARAR

El orden básico es correcto: definir y enumerar antes de resolver; comprobar cierres sencillos antes de abordar sistemas generales; separar clasificación de análisis espectral. La transferencia de P17 puede preceder a 4b, pero sus conclusiones solo cubren candidatos que satisfagan sus hipótesis.

**La enumeración geométrica es finita y puede delimitarse a mano.** Hay \(2^4=16\) maneras de elegir un vértice de cada pareja antipodal:

- Dos tetraedros.
- Seis caras.
- Ocho conjuntos formados por un vértice y sus tres vecinos.

En el último caso, el vértice central tiene tres vecinos dentro del conjunto y los otros tienen uno. Esa propiedad impide una acción transitiva por simetrías del cubo.

El estabilizador rotacional de un tetraedro es \(T\simeq A_4\); sus subgrupos transitivos sobre cuatro vértices son \(V_4\) y \(T\). El estabilizador rotacional de una cara es \(C_4\), cuyo único subgrupo transitivo sobre ella es el propio \(C_4\). Por tanto, salvo conjugación en \(O\), aparecen **tres pares geométricos**:

\[
(V_4,\text{tetraedro}),\qquad
(T,\text{tetraedro}),\qquad
(C_4,\text{cara}).
\]

La parte representacional también es finita **módulo equivalencia proyectiva y unitaria**, pero «cada clase proyectiva» es ambiguo: una clase de multiplicadores en \(H^2(G,U(1))\) no determina una representación bidimensional. Hay que incluir todas las representaciones de dimensión total dos, también las reducibles.

**4a necesita distinguir invariancia de transporte.**

- Conjugación constante, fase global y desplazamiento de momento preservan los conjuntos \(S_n\).
- Inversión espacial transporta \(S_n\) a \(-S_n\).
- Una rotación \(Q\) los transporta a \(QS_n\).
- El mínimo esférico de la función soporte se conserva bajo transformaciones ortogonales, aunque el cuerpo no permanezca literalmente igual.

Además, un desplazamiento arbitrario de momento no preserva automáticamente la covarianza con el mismo \(R\). Debe verificarse la covarianza transportada. «Conjugación compleja» debe especificar si actúa sobre coeficientes o sobre el símbolo a momento fijo.

P17, p.7, utiliza expresamente el intercambio \(h_1\leftrightarrow h_4\), ausente de la lista. Debe identificarse su realización geométrica. Permitir una reflexión como equivalencia entre modelos es distinto de exigirla como simetría de cada modelo.

**Excluir la multiplicación izquierda está justificado.** Por ejemplo,

\[
U(k)=\operatorname{diag}(e^{-ik},e^{ik}),\qquad V=\sigma_x.
\]

Para \(U\), \(S_n=\{-n,n\}\). Sin embargo,

\[
(VU(k))^2=I,
\]

por lo que el soporte de sus potencias permanece acotado y su velocidad estricta es cero. Este ejemplo prueba que la operación no es una equivalencia general para el observable estudiado. En el caso irreducible de Pauli, un \(V\) que conmuta con toda la representación es escalar; esa libertad ya queda cubierta por la fase global.

**4b distingue correctamente ideal propio de existencia real**, pero aún falta operacionalizarlo. El ejemplo \(\langle x^2+1\rangle\) muestra por qué un ideal propio puede no tener puntos reales. También deben incorporarse \(T_h\neq0\), y distinguir componentes algebraicas complejas de componentes del conjunto real admisible.

**A-R1-07 — Paso 0′; laguna.** Definir equivalencia de representaciones, fases proyectivas, multiplicadores y transporte por conjugación espacial. Incluir representaciones reducibles y una prueba de exhaustividad.

**A-R1-08 — Sec. 2 y Paso 4a; laguna.** Sustituir la invariancia literal por leyes explícitas de transporte; completar el diccionario de equivalencias realmente usado por P17 y verificar admisión tras cada transformación.

**A-R1-09 — Paso 4b-1; laguna.** Declarar variables reales para partes reales e imaginarias, condiciones de soporte activo y certificado de existencia o inexistencia real. Aclarar que los parámetros recorren todo el dominio declarado, no solo puntos algebraicos.

## 5. Salidas y techos — REPARAR

Los techos contra universalidad, naturaleza, otros soportes y novedad son adecuados. «Not located in the sources checked» es una formulación prudente, siempre que se identifiquen esas fuentes.

Las salidas **no tienen el mismo rango lógico**:

- `NONEMPTY_CLASS_DERIVED` es un hito intermedio.
- `DISTINGUISHABILITY_IMPLIED_IN_CLASS` es una propiedad adicional.
- `TRANSFER_CERTIFIED...` responde a otra pregunta.
- Un contraejemplo decide la pregunta universal por existencia.
- Rigidez exige cobertura universal.
- Un candidato inadmisible no decide una clase.

Pueden coexistir. «Equal standing» puede significar igual aceptación editorial, pero no que todas constituyan desenlaces excluyentes o cierren el contrato.

Falta distinguir una clase sin símbolos unitarios de una clase con símbolos unitarios pero **sin ningún cono admisible**. También falta una salida explícita para la refutación de Q-a. `INADMISSIBLE_SATURATION` conserva un nombre engañoso: su propia definición describe un candidato admisible.

Finalmente, la cota general \(c_0\leq c_{\rm strict}^{\rm iso}\) se remite a una sección no adjunta y queda **[UNVERIFIED]** aquí. La dicotomía igualdad/desigualdad estricta propuesta depende de que esa cota cubra precisamente los nodos y unidades congelados.

**A-R1-10 — Sec. 5; laguna.** Separar estado de clasificación, existencia de sectores admisibles, resultado de rigidez y respuestas Q-a/Q-b. Añadir «sin sectores admisibles» y «distinguibilidad refutada mediante testigo». Especificar qué resultados cierran cada tarea.

**A-R1-11 — Sec. 0 y Sec. 5; laguna.** Incorporar una referencia verificable al certificado de la cota general y comprobar su alcance. Distinguir las afirmaciones históricas de los resultados certificados para este contrato.

## 6. Citas de P17 — REPARAR

Estos veredictos comprueban la atribución en el **Documento 5**, no la validez completa de las demostraciones citadas.

| Afirmación | Veredicto | Comprobación |
|---|---|---|
| Eq. (2), p.2: conmutador no nulo cuando se mueve el generador | **CORRECTA** | Aparece explícitamente, con \(h\in S_+\). |
| Eq. (2) remite a [23], que remite a [31] | **CORRECTA** | [23], p.15, explica el suplemento de distinguibilidad y remite a [31]. |
| «Las referencias [23]/[31] son inéditas» | **INCORRECTA** | [23] es una nota explicativa publicada en el propio artículo; [31], p.16, dice “Unpublished”. |
| Existe allí una derivación publicada completa de Eq. (2) | **NO VERIFICABLE** | El texto remite los detalles a [31]; esos detalles no están adjuntos. |
| \(s=1\) es “trivial”, p.4, citando [24] | **CORRECTA** | La frase y la cita están presentes. Esto no verifica el contenido de [24]. |
| Eqs. (12)–(13), p.4, sustentan rango uno | **CORRECTA** | (12) es la descomposición polar; el argumento intermedio y (13) establecen rango uno para transiciones no nulas con \(s=2\). |
| Imagen de Pauli en Fig. 1(c) y Sec. V | **CORRECTA** | La leyenda está en p.6; Sec. V introduce \(H\) en p.5 y lo usa para \(d=3\) en p.6. |
| Prop. 5, pp.6–7, como localización conjunta | **CORRECTA**, con precisión | La proposición está en p.7; la imagen de Pauli se identifica en la leyenda y la derivación precedente. |
| \(A_e=0\) en \(d=3\), pp.6–7 | **CORRECTA** | La leyenda de p.6 excluye autointeracción salvo en \(d=1\); p.7 lo afirma en la derivación y en Prop. 5(c). |

El Documento 4 usa paginación de la versión publicada y el Documento 1 declara paginación arXiv. Esas coordenadas no deben mezclarse.

**A-R1-12 — Bibliografía inicial y localizadores; error demostrado y redacción.** Sustituir «unpublished refs. [23]/[31]» por «nota [23], que remite al trabajo inédito [31]». Separar las coordenadas de Fig. 1(c), Sec. V y Prop. 5, indicando la versión inspeccionada.

## 7. Presupuesto, parada y revisión — REPARAR

La división en cuatro autorizaciones y la revisión por otra familia son buenas medidas. No bastan como están redactadas.

«Within its authorization» no define un presupuesto operativo. Faltan límites para enumeración, cálculo algebraico, análisis de cuerpos estrictos y revisión. No es obligatorio fijar ahora cada segundo de CPU, pero sí exigir que cada autorización incluya límites concretos **antes de ejecutar su etapa**.

También falta una parada para 4b-2: que la clase de coeficientes sea manejable no garantiza que todos sus cuerpos estrictos puedan determinarse exactamente. «Otherwise compute the strict body» no es un procedimiento garantizado.

La revisión debe cubrir la exhaustividad de 0′ antes de usar su lista como universo de clasificación. Debe prever qué ocurre si hay objeciones abiertas, cambios posteriores del certificado o discrepancias entre informe y verificador. Una revisión por otra familia es una comprobación adicional, no sustituye el certificado matemático.

**A-R1-13 — Sec. 4; laguna.** Exigir por etapa presupuesto de tiempo y recursos, alcance, entregable y condición de cierre; añadir parada explícita por dificultad en 0′, 4a y 4b-2. Un límite agotado produce resultado parcial u abierto, nunca rigidez.

**A-R1-14 — Sec. 6; laguna.** Revisar la enumeración y sus convenciones antes de utilizarla; fijar máximo de rondas, tratamiento de objeciones y nueva revisión cuando cambie el contenido certificado. Registrar hashes, commit, herramientas y autorización de cualquier envío externo.

**El contrato debe permanecer DRAFT hasta incorporar estas reparaciones.** La revisión no autoriza cálculos ni certifica los resultados históricos citados.