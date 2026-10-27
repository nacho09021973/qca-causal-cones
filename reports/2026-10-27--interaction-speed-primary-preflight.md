# A.int: preflight de fuentes primarias sobre velocidades e interacción

Fecha: 2026-10-27. Autor: Codex. Base: `02f88d9328e35e4e46b713f0becf2b3b9cdfefa5`.
Autorización: continuación del usuario, «la primera», al preflight propuesto.
Procedencia de la pregunta: Claude, según el documento importado
[original](2026-10-26--interaction-renormalized-species-speed.md), conservado sin reescribir.

## Dictamen y cierre del encargo

`PRIMARY_SOURCE_PREFLIGHT_COMPLETE / A.int_OPEN / NO_LOOP_CALCULATION`.

La preocupación de naturalidad está motivada, pero el corpus comprobado no
demuestra una separación radiativa de velocidades en un QCA 3+1 concreto.
Tampoco establece una simetría protectora de ese modelo. La ausencia de una
prueba de protección en estos artículos no prueba que no exista protección.
No procede convertir Q1/Q2 en un sí/no general ni deducir Q3.

El encargo termina con este contraste de fuentes y la decisión de no iniciar
un cálculo a un lazo sin contrato. No abre un gate ni cambia W1–W12.
Las deducciones locales de abajo son comprobaciones del autor; no han recibido
revisión independiente y no se promueven a un resultado general de QCA.

## Corpus y trazabilidad

Se leyó primero `biblioteca/INDICE.md`. Solo F17 estaba en el catálogo local;
se incorporaron seis PDFs, con etiquetas `proposed`, y se regeneró el índice.
Las páginas siguientes son páginas PDF, contando desde 1. Los enlaces fijan
la versión leída; el manifiesto adyacente fija los bytes locales. El PDF de
Entropy se descargó de
`https://mdpi-res.com/d_attachment/entropy/entropy-27-00198/article_deploy/entropy-27-00198.pdf`.

| Fuente primaria | PDF local y páginas comprobadas | Pertinencia y límite |
| --- | --- | --- |
| [Collins et al., gr-qc/0403053v4](https://arxiv.org/pdf/gr-qc/0403053v4) | `biblioteca/arXiv-gr-qc_0403053v4.pdf` pp.2–4 | Ejemplo explícito de autoenergía Yukawa con corte espacial preferido; no es un QCA. |
| [Arrighi–Facchini–Forets, 1404.4499v1](https://arxiv.org/pdf/1404.4499v1) | `biblioteca/arXiv-1404.4499v1.pdf` pp.1, 4–5, 17–18 | Covariancia discreta 1+1; Clock QCA de dimensión de hilo 3. |
| [Bisio–D'Ariano–Perinotti, 1707.08455v1](https://arxiv.org/pdf/1707.08455v1) | `biblioteca/Quantum Walks, Weyl equation and the Lorentz group.pdf` pp.5, 7–8 | Simetría no lineal de la ecuación espectral del Weyl walk libre. |
| [Debbasch, 1806.02313v1](https://arxiv.org/pdf/1806.02313v1) | `biblioteca/arXiv-1806.02313v1.pdf` pp.1–2, 8–9 | Acción covariante 1+1 con campos que representan el marco de la red. |
| [Bisio et al., 1711.03920v1, PRA 97, 032132](https://arxiv.org/pdf/1711.03920v1) | `biblioteca/arXiv-1711.03920v1.pdf` pp.1–2 | Thirring 1+1 con número conservado; solución en dos partículas. |
| [Bisio et al., Entropy 27, 198 (2025)](https://doi.org/10.3390/e27020198) | `biblioteca/entropy-27-00198.pdf` pp.3–4, 8, 12–13, 21–22 | Amplitudes de procesos en dos/tres partículas; expansión en vértices y masa. |
| [Eon et al., 2205.03148v4](https://arxiv.org/pdf/2205.03148v4) | `biblioteca/arXiv-2205.03148v4.pdf` pp.1–3, 29–30 | Construcción QED 2+1/3+1; v4 corrige el transporte 3D. |

Se usó `pdftotext -layout`, con `-f N -l N` para inspecciones por página.
No se generó ninguna métrica científica ni se ejecutó código de modelos.
El preprint `2406.19917v1` se consultó para localizar el artículo de 2025;
las referencias anteriores usan la versión publicada, de 30 páginas.

Búsqueda web complementaria, acotada a estas tres consultas:
`"quantum cellular automaton" "speed" "renormalization" interaction`,
`"quantum cellular automata" "self-energy"`,
`"Thirring" "cellular automaton" "renormalization"`.
No se localizó en esta búsqueda una respuesta directa multiespecie a Q1.
Esto no es una búsqueda exhaustiva ni un dictamen de novedad.

## Qué prueba Collins y qué no se transfiere automáticamente

En pp.3–4, apéndice A, se introduce una modificación del propagador fermiónico
por `f(|k|/Lambda)`. La ecuación (A.2) da
`xi = g²/(6 pi²) [1 + 2 integral_0^infty dx x f'(x)²]`, sin potencias de
la escala de corte. En p.4 se relaciona con una modificación del parámetro de
velocidad y se explica por qué una sola redefinición métrica no elimina
correcciones diferentes entre campos. La discusión de p.3 pide protección
frente a operadores de dimensión cuatro y explicita el contexto de tiempo real.

Ese cálculo motiva examinar el matching ultravioleta del QCA; no da sus
propagadores, vértices, vacío ni prescripción de polos. Sustituir el corte de
Collins por una zona de Brillouin sin derivar esos objetos no es una prueba.
El orden dominante y su coeficiente se deben calcular en el modelo elegido.

## Q1: permitido por simetría no equivale a generado

Control manual de operadores, condicionado a que exista una descripción
efectiva local de campos escalares en 3+1, con traslaciones y simetría cúbica
espacial, sin simetría que intercambie especies ni espacio y tiempo:

`L_kin = sum_i [Z_t,i (partial_t phi_i)² - Z_s,i sum_a (partial_a phi_i)²]/2`.

Cada sumando temporal y espacial es invariante bajo esas simetrías. Estas
no relacionan `Z_t,i` con `Z_s,i`, ni los cocientes de especies distintas.
En unidades comunes y para un polo estable de ese operador,
`c_i² = Z_s,i/Z_t,i`. Una normalización del campo elimina un factor común,
pero no el cociente. Comprobación por segunda vía: un cambio común de unidades
temporales multiplica todos los `c_i` por el mismo factor; deja `c_i/c_j`
invariante. El término tiene dimensión cuatro con el conteo canónico escalar
en 3+1. Este conteo no se traslada sin cambios al Thirring 1+1.

Es un argumento de admisibilidad en EFT, no la construcción de un QCA que
realice coeficientes arbitrarios. Para campos fermiónicos o gauge hace falta
su propia base de operadores y representación de simetrías. Una simetría
interna adicional podría relacionar especies; tampoco se ha descartado una
atracción hacia velocidades comunes mediante dinámica de escala.

Por tanto: **la simetría espacial indicada por sí sola no impone universalidad
en esa EFT; `delta c_i != delta c_j` a orden g² en un QCA sigue OPEN**.

## Q2: alcance de los tres candidatos

Arrighi–Facchini–Forets: la conclusión de p.18 distingue covariancia de primer
orden del Dirac QW y covariancia exacta del Clock QCA. Las transformaciones
usan codificaciones isométricas y parches rectangulares, con reparametrización
en la formulación general. En p.17 se exige que los múltiples walkers no
interactúen entre sí. No se obtiene de ello una identidad de Ward para el
modelo QED 3+1 ni una clasificación de sus contraterminos.

Bisio–D'Ariano–Perinotti: en p.5 las transformaciones preservan la ecuación
de autovalores; p.7 construye la representación no lineal de Lorentz que
recupera la lineal a bajo momento. La discusión pp.7–8 se sitúa en el espacio
energía-momento del walk. Falta extender la transformación a un paso
interactuante común, sus vértices y sus correladores. La protección radiativa
multiespecie no está establecida por ese resultado libre.

Debbasch: pp.8–9 conservan explícitamente la velocidad temporal de la red y
su vector ortogonal en la formulación covariante. Comprobación conceptual
independiente: escribir un término con un vector de fondo `u` que también
transforma, por ejemplo `(u^mu partial_mu phi)²`, permite covariancia formal
y a la vez una dirección temporal física distinguida. Por tanto la forma
covariante no basta para prohibir el cociente cinético anterior. No se ha
derivado aquí una obstrucción a todas las posibles extensiones de su acción.

**Protección no demostrada en el corpus; inexistencia de protección no probada.**
La propuesta euclídea del documento importado queda `[UNVERIFIED]` en este
preflight: no se ha contrastado su reconstrucción real con positividad,
localidad estricta y un paso QCA unitario. `Delta t = Delta x` fija escalas;
por sí solo no proporciona una transformación que intercambie los ejes de
espacio y tiempo del circuito completo.

## Control de sector: por qué Thirring no decide el problema de Collins

El modelo de 2018, pp.1–2, tiene dos modos fermiónicos por sitio en Z,
transporte Dirac y fase de doble ocupación; conserva el número total.
El trabajo publicado de 2025 escribe en p.8, ecuaciones (8)–(9),
`J(chi) = exp[i chi sum_x n_R(x)n_L(x)]` y `U = W J(chi)`.
Sus pp.12–13 desarrollan la expansión en inserciones; pp.21–22 tratan
amplitudes y sus dificultades en más partículas. No calculan una separación
de velocidades de especies físicas por autoenergía de vacío.

Deducción local desde esa definición: en el sector de número total N=1,
`n_R(x)n_L(x)` anula todos los vectores de la base de ocupaciones, para todo x.
Por linealidad anula cualquier superposición. Luego `J|_(N=1)=I`,
`U|_(N=1)=W_1` y, como N se conserva, `U^T|_(N=1)=W_1^T` para todo T
entero positivo. Segunda vía: en la expansión `J=I+(J-I)` cada término con
una inserción se anula al restringirlo a ese sector.

Así, sobre el vacío sin ocupaciones, la dispersión de una partícula es
independiente de chi exactamente, no solo a orden chi². Esto no dice nada
sobre excitaciones sobre un estado lleno, densidad finita, estados ligados,
ni sobre QED con fluctuaciones gauge y un vacío físico diferente.
Una diagonalización pequeña en N=1 de este Thirring no probaría el efecto
buscado. Un espectro en volumen finito tampoco basta por sí solo para fijar
una velocidad IR termodinámica renormalizada.

## Eon y Q3: lo que sigue abierto

Eon et al. construyen el circuito QED y argumentan la correspondencia entre
cableado y velocidad de luz en pp.1–3; pp.29–30 recapitulan la construcción y
sus continuaciones. Esas secciones no proporcionan matching a un lazo de
velocidades vestidas. Se fija v4 porque corrige el transporte 3D. La frase de
velocidad de circuito no reemplaza el cálculo de polos interactuantes.

Q3 sigue **NOT_DERIVED**. Este preflight no adopta el intervalo experimental
`10^-21–10^-22` como cota universal: no se revisaron aquí sus fuentes
experimentales primarias ni sus hipótesis por especies/operadores. Una
corrección marginal no suprimida por potencias de `k Delta x` tampoco
garantiza independencia completa del espaciado: pueden intervenir running,
masas y el ajuste de acoplamientos al cambiar el regulador.

Para decidir si se autoriza un cálculo, el próximo contrato debería fijar
modelo y versión, grados gauge y truncación si la hay, simetrías exactas,
estado de referencia, especies y nodos, rama de cuasienergía, definición
observable de velocidad, límites IR/volumen, acoplamiento y contraterminos.
Debe comparar polos físicos con unidades comunes y distinguir velocidad
IR, velocidad de grupo y soporte causal. No se ejecuta ese contrato aquí.

## Validación documental

El catálogo se regenera con el motor de `~/herramientas` en
`16568209771dc898346bd4af0c78ec10530c3b9e`.
El manifiesto `2026-10-27--interaction-speed-primary-sources.sha256` permite
comprobar la identidad de los siete PDFs. Los PDFs nuevos son locales e
ignorados por Git; sus URLs y hashes quedan en el registro versionable.
Validación ejecutada: `text_integrity.py --check` devuelve cero problemas;
`git diff --check` pasa; los siete hashes del manifiesto coinciden. El índice
regenerado contiene 33 PDFs, sin duplicados. No se modifican certificados ni
se requiere otro barrido de W.
