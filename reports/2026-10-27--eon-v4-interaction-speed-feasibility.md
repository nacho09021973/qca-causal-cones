# A.int: viabilidad de definir velocidades interactuantes en Eon v4

Fecha: 2026-10-27. Autor: Codex.
Base: `01fd957ec1f4fd80afdf8281d86fd19a94e45bd5`.
Autorización: «empezamos con 1», al estudio de vacío físico, excitaciones
comparables y definición de velocidad. Este documento completa ese estudio;
no constituye un contrato de cálculo ni ejecuta un lazo.

## Dictamen

`FEASIBILITY_AUDIT_COMPLETE / REFERENCE_AND_OBSERVABLE_OPEN`.
**No está listo para ejecutar un cálculo a un lazo a partir del vacío de
referencia citado en el artículo. El modelo no queda rechazado.**

El circuito está especificado, pero no se ha establecido aquí un estado de
referencia estacionario con espectro físico controlado, una expansión débil
alrededor de ese estado, ni una definición común ya calibrada de velocidades
fermiónica y electromagnética. Estos son problemas previos al matching.

La siguiente tarea acotada que permitiría avanzar es especificar y comprobar
el estado de referencia, sus fronteras y su sector de Gauss. Si no se obtiene,
se detiene esta ruta antes de producir correcciones de velocidad.
Esta recomendación no ejecuta ni autoriza ese nuevo trabajo.

## Fuente primaria y alcance

Fuente central: Eon, Di Molfetta, Magnifico y Arrighi,
[arXiv:2205.03148v4](https://arxiv.org/pdf/2205.03148v4),
`biblioteca/arXiv-2205.03148v4.pdf`, 37 páginas PDF. Identidad comprobada con
`2026-10-27--interaction-speed-primary-sources.sha256`:
`c366b8a8482a762c93e534e43d6572323737df4677556b1a764e02a1389d2d02`.
Se leyó primero el índice local; después se comprobaron directamente pp.5–7,
10–15, 17–30 mediante `pdftotext -layout -f N -l N`.
Las páginas citadas son páginas PDF, no numeración de una versión HTML.

Se separan datos del artículo, deducciones manuales y propuestas operativas.
Las deducciones son comprobaciones del autor sin revisión independiente;
no promueven la evidencia científica. No se ejecutaron scripts científicos,
simulaciones, diagonalizaciones ni estimaciones de autoenergía.
El [preflight anterior](2026-10-27--interaction-speed-primary-preflight.md)
y la pregunta importada mantienen sus propios alcances.

## Inventario de lo que se puede fijar y lo que falta

| Elemento | Comprobación | Consecuencia para la viabilidad |
| --- | --- | --- |
| Paso microscópico | pp.28–29, ecuaciones (34)–(37): `U = D_M D_E D_F` | La regla puede reconstruirse conservando el orden de capas. |
| Espacio local | p.6: cuatro modos fermiónicos en 3D y contadores gauge en `H_Z`, con extremos de enlace opuestos | Los cuatro componentes del espinor no son la dimensión total de celda; el modelo original tiene registros gauge infinitos. |
| Sector físico | pp.11–12: carga local total fijada por `f(x)`; para la referencia de pares, `f=d/2` | En 3D se propone `f(x)=2`. Esto fija un sector, no un vacío único. |
| Referencia de ocupaciones | p.13: modos de antipartícula llenos y campos gauge en cero | No se aporta allí una demostración de que ese producto sea un estado estacionario del paso completo. |
| Excitación cargada | p.12: creador fermiónico acompañado por una cadena gauge hasta una frontera | El fermión local desnudo no es por sí solo un creador físico dentro del mismo sector. |
| Excitación electromagnética | pp.18–23: operadores de enlace y plaqueta con dos implementaciones magnéticas | Se pueden proponer correladores gauge invariantes, pero falta identificar su rama propagante sobre el estado elegido. |
| Comparación física | p.24: espinor Dirac de cuatro componentes y un campo gauge | Comparación candidata: sector fermiónico frente al electromagnético. No hay dos sabores fermiónicos independientes especificados. |
| Límite débil | pp.18–19: coeficientes eléctrico y magnético relacionados inversamente | No se obtiene un punto libre de ambos sectores apagando un único coeficiente sin más construcción. |
| Duplicación y nodos | p.30 deja abierta la cuestión de fermion doubling en 2+1/3+1 | No se deben bautizar los nodos adicionales como especies físicas ya identificadas. |

## 1. Sector físico y significado de vacío

La restricción de p.12 puede escribirse como

`G_x = sum_eta E_(x:eta) + sum_(j=0)^3 n_(x,j) - f(x)`;
`G_x |psi_phys> = 0`.

Para la referencia propuesta, `f(x)=2`. El estado producto con dos modos
ocupados por sitio y todos los contadores eléctricos en cero satisface esta
restricción. Eso comprueba pertenencia al sector. No comprueba ni
`U rho U† = rho`, ni la condición de vacío de sus correladores.

Para una función de dos puntos estacionaria, la condición mínima sería un
estado físico, homogéneo en el volumen de interés y estacionario para el
paso elegido. Un vector propio de U cumple estacionariedad; no basta para
seleccionar un vacío físico entre todos los vectores propios. La cuasienergía
es periódica y no ofrece por sí sola una ordenación global como la energía
de un Hamiltoniano acotado inferiormente. Elegir una rama de `log U` no
sustituye la construcción o justificación del estado.

Dos controles manuales muestran por qué no se debe suponer que las
ocupaciones en p.13 ya resuelven esto:

* El subpaso de masa de pp.25–26 mezcla componentes mediante `gamma_0`.
  Una ocupación definida en la base local no es automáticamente un llenado
  de bandas espectrales de todo el walk.
* En la base de plaqueta de p.20, `P|n> = |n+1>`, absorbiendo los signos
  indicados allí. Para `K(theta)=exp[i theta(P+P†)]`,
  `d K(theta)|0>/d theta` en cero es `i(|1>+|-1>)`, ortogonal a `|0>`.
  Así, en el registro no truncado, un flujo definido no es vector propio
  de ese subpaso para ángulos genéricos próximos a cero. Segunda vía:
  en la representación de Fourier del desplazamiento, p.21–22, la fase
  depende del momento conjugado; un delta en n ocupa todo ese espectro.

Estos controles son de subpasos. **No prueban por sí solos que el producto
completo U no pueda devolver la referencia**: habría que comprobarlo para
la regla y parámetros elegidos. Sí impiden justificar su estacionariedad
alegando simplemente que no contiene partículas ni flujo inicial.

Tampoco se traslada sin más el argumento de Thirring: la referencia física
aquí es de semillenado y flujo restringido, no el vacío vacío de un sector
de una partícula. El llenado de bandas negativas del walk libre, si se
propone, requeriría comprobar además Gauss y su acompañamiento gauge.

## 2. Fronteras y excitaciones que pueden compararse

Control global de Gauss en una red periódica finita sin cargas externas:
al sumar sobre sitios, cada medio enlace E se cancela con su opuesto.
Entonces `N_fermiones = sum_x f(x) = 2 V`. Segunda vía: el transporte
intercambia ocupación fermiónica y flujo en los extremos, conservando el
generador local, como se comprueba en pp.10–11.

Por ello una inserción fermiónica desnuda cambia de sector. En volumen
finito, si `P_f` proyecta al sector fijado,
`P_f a†_(x,j) P_f = 0`. Un electrón aislado de carga neta no cabe como
excitación de ese sector periódico neutral. No se concluye que todo
correlador fermiónico formal sea cero: una función gauge fijada o con
sectores intermedios distintos es otro objeto que habría que definir.

La construcción de p.12 permite acompañar un creador con una cadena de
operadores gauge hasta una frontera, incluso infinitamente lejana. En una
caja abierta esto obliga a fijar qué flujo o carga puede absorber la
frontera; al cambiar el dressing se cambia la preparación física. Una
cadena entre dos extremos permite objetos neutros de par, pero su
dispersión no equivale automáticamente a la de un electrón individual.

Para el sector electromagnético son candidatos gauge invariantes los
contadores E y la combinación hermítica `F_p=(P_p-P_p†)/(2i)`. Sus
componentes transversales y su identificación con campos físicos se deben
calibrar sobre el estado de referencia. No se ha probado aquí una fase
Coulomb ni un fotón gapless. La fase del sector gauge no debe suponerse
por el nombre QED de la construcción.

Así, el par candidato es **excitación fermiónica cargada vestida / modo
electromagnético transversal**, si ambos admiten definición controlada.
Espín arriba/abajo y partícula/antipartícula no suministran por sí solos
dos sabores con acoplamientos independientes. Añadirlos sería un modelo
nuevo. Tampoco se presume una simetría exacta que iguale sus velocidades.

## 3. Qué expansión sería necesaria

Con la notación de las ecuaciones (20)–(21), pp.18–19, los ángulos son
`alpha_E = epsilon² g_E²/2` y `alpha_M = epsilon² g_M²/2`.
El texto relaciona `g_M=1/(Delta_x g_E)`. Al usar `Delta_x=epsilon`,

`alpha_M = 1/(2 g_E²)`;
`alpha_E alpha_M = epsilon²/4`.

Esta sustitución, y el producto como segundo control algebraico, muestran
que a epsilon fijo no se apagan ambos términos tomando `g_E` a cero.
La lectura alternativa de variarlos como dos constantes independientes
no sería la misma familia con esa relación impuesta.

Esto **no demuestra la imposibilidad de una expansión débil de QED**.
Podría requerir reescalar campos, elegir variables de flujo/fase apropiadas
y construir un estado gaussiano de referencia con transporte desacoplado
en un sentido preciso. Ninguna de esas operaciones se ha ejecutado aquí.
No se identifica `g_E` con un acoplamiento adimensional de lazo sin derivar
la normalización en 3+1 y el papel de epsilon. No se asume que el límite
de epsilon y la expansión de acoplamiento conmuten.

Dos decisiones microscópicas también afectan a la futura pregunta:

* La implementación magnética exponencial y la de dos subpasos de p.23
  coinciden en el límite declarado, pero difieren a epsilon finito. Debe
  escogerse una, conservando el orden de (36)–(37).
* Las truncaciones de pp.18, 20–21 tienen condiciones propias. Un registro
  cíclico finito no se puede tratar como el rotor `H_Z` sin comprobar de
  nuevo su álgebra gauge y la convergencia del observable.

Asimismo, que la retícula sea cúbica no prueba que el paso ordenado completo
tenga exactamente todas las rotaciones cúbicas. Una rotación puede permutar
el orden de capas. Debe comprobarse su acción sobre U, o una equivalencia
estroboscópica precisa, antes de usarla para eliminar términos de la EFT.

## 4. Definición candidata de velocidad y comprobaciones previas

Lo siguiente es una propuesta operativa condicional, no un observable ya
construido. Dado un estado estacionario, se estudiarían correladores
retardados gauge invariantes del sector electromagnético y correladores
fermiónicos con dressing o una prescripción gauge controlada. No se exige
de antemano que el sector cargado tenga un polo aislado: su estructura
espectral debe comprobarse. Si aparece un umbral en lugar de un polo,
habrá que justificar otra definición; no se ajustará una recta y se llamará
velocidad de partícula.

Para una rama estable identificada cerca de un nodo fijado, sea q el
desplazamiento de momento en unidades de la red y phi(q) la diferencia de
fase por paso respecto a la referencia, con rama continua local. Entonces
`k=q/Delta_x` y `Omega=phi/Delta_t`. Las siguientes extracciones son distintas:

| Sector y condición | Cantidad candidata | Prueba necesaria |
| --- | --- | --- |
| Modo electromagnético gapless | `c_gamma(n)=(Delta_x/Delta_t) lim_(q->0+) phi_gamma(q n)/q` | Identificar modo, nodo y rama; resolver direcciones y polarizaciones. |
| Fermión masivo con rama regular y sin término impar | `c_(e,Omega²)²(n)=(Delta_x/Delta_t)² lim_(q->0) [phi_e(q n)²-phi_e(0)²]/q²` | Verificar expansión y ausencia del término lineal; separar masa y coeficiente espacial. |
| Fermión massless con rama lineal | Pendiente de definir rama, reguladores y límite de masa | No intercambiar límites sin demostración. |

La ausencia de término impar o deriva debe probarse por simetría o cálculo;
no se presume por la forma deseada de la dispersión. Si una rama masiva no
es suave, la segunda fila no se aplica. `c_(e,Omega²)` no se identifica con
el coeficiente `c_H` de un Hamiltoniano interpolante a masa de red finita.
Tampoco la pendiente de grupo en k=0 de una partícula masiva mide ese
coeficiente relativista.

Primero habría que comprobar, **sobre referencias y observables físicos
compatibles**, la igualdad libre de las dos velocidades con unidades comunes.
El primer jet Dirac de p.25 no calibra por sí solo la rama electromagnética.
Solo después tendría sentido extraer un cambio de su cociente al interactuar.
Unas pocas frecuencias en una caja no certifican el límite IR termodinámico.
Los cocientes se conservarán por dirección hasta justificar isotropía;
no se confunden con el soporte causal ni con la velocidad de los cables.

## 5. Resultado del paso 1 y frontera del siguiente trabajo

| Condición previa | Resultado de esta sesión |
| --- | --- |
| Regla y versión localizables | Sí: v4 y sus dos opciones magnéticas, aún sin seleccionar una para cálculo. |
| Sector y restricciones físicos identificados | Sí: Gauss y semillenado; las fronteras deben fijarse. |
| Vacío estacionario con selección física justificada | No establecido. |
| Excitaciones y correladores físicos construidos | Candidatos delimitados; no construidos. |
| Expansión débil y comparación libre calibradas | No establecidas. |
| Cálculo a un lazo ejecutable con lo anterior | No listo. |

El siguiente encargo útil sería **solo el problema del estado de referencia**:
elegir implementación magnética y fronteras, especificar un candidato físico
con sus hipótesis, comprobar Gauss y estacionariedad, y explicar qué selecciona
sus excitaciones de baja frecuencia. Un candidato que solo sea estacionario
pero no permita distinguir vacío de un estado genérico no cierra el problema.

Si esto exige introducir un Hamiltoniano padre, una interpolación adiabática
o una modificación del circuito, debe declararse como nueva hipótesis o
cambio de modelo antes de usarlo. No se ejecuta esa construcción aquí.
No procede todavía una cota experimental ni una afirmación de tuning.

## Validación y límites de documentación

Se conserva el manifiesto de fuentes ya publicado; los siete PDFs coinciden
con sus hashes. Solo se añade este informe y se actualiza A.int en el estado
canónico. Las deducciones son manuales y están escritas arriba, con controles
alternativos; no hay resultados de código temporal que conservar.
No se invocó revisión externa. No se promueve evidencia ni se reabre W1–W12.
Validación documental: `python3 -B scripts/text_integrity.py --check` devuelve
cero problemas y `git diff --check` pasa. No cambian certificados.
