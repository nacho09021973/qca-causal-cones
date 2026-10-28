# A.int — contraste de la respuesta recibida sobre el vacío

Fecha: 2026-10-27. Autor del contraste: Codex.
Encargo: «continua», después de que el usuario aportase una respuesta a
la pregunta para un experto. El autor, método y alcance de revisión de
esa respuesta no están identificados en el mensaje. Se registra como
texto recibido del usuario, no como fuente primaria ni como revisión
independiente acreditada. No se le atribuye origen humano o de IA.

## Dictamen

`EXPLANATION_COMPATIBLE / PROPOSED_VACUUM_SHORTCUTS_REJECTED_AS_SUFFICIENT`.
La explicación del fallo de la referencia de ocupaciones es compatible
con el certificado anterior. **Las recetas propuestas no establecen un
vacío físico de Eon.** Hay dos problemas concretos: el Slater de bandas
negativas no satisface en general Gauss al tensorizarlo con flujo cero;
el mínimo del logaritmo principal de U no selecciona automáticamente el
vacío de la energía aditiva ni proporciona un generador local.

Este encargo contrasta esas afirmaciones. No ensaya otro candidato del
QCA interactuante, no altera `STOP_THIS_CANDIDATE`, ni calcula lazos.
Las comprobaciones nuevas son del autor, sin revisión independiente.

## Afirmaciones recibidas y tratamiento

Los fragmentos entre comillas proceden del mensaje recibido; el resto de
la columna describe su contenido para poder contrastarlo.

| ID | Afirmación recibida | Resultado del contraste |
| --- | --- | --- |
| R1 | La referencia local es «no el vacío estacionario del QCA» | Compatible con nuestro rechazo en los casos ya delimitados. La cita del artículo define una referencia, pero no contiene por sí misma una prueba general de no estacionariedad. |
| R2 | Llenar bandas negativas da un Slater «gauge-invariante en el sector N=2 por sitio (o equivalente)» con E=0 | La inferencia es incorrecta en general: número total o media local no equivalen al autovalor local exigido por Gauss. Véanse lema y control exacto abajo. |
| R3 | Para masa pequeña el Slater está «cerca del estado local de referencia» | No se deduce solo de masa pequeña. El proyector de banda y el llenado local ya difieren a masa cero en un momento no degenerado. |
| R4 | El fundamental del logaritmo principal de U es el vacío físico | No es un criterio suficiente. Un control exacto de dos modos cambia el mínimo al plegar la energía, conservando U exactamente. |
| R5 | La rama principal es adecuada por tratarse de «pasos pequeños» | Falta una condición espectral global y uniforme. El transporte de un QCA no tiende a la identidad en norma sobre toda la zona de Brillouin por reducir epsilon a momento físico fijo. |
| R6 | Encender gradualmente g_E y g_M, o usar tiempo imaginario, construirá el vacío completo | Propuestas condicionales: falta fijar una trayectoria compatible con su relación, generador, selección espectral y controles de preparación. No son un resultado del artículo ni de este contraste. |
| R7 | El error de ocupación por paso de orden (m epsilon)² hace controlable usar la referencia local para velocidades | Ese dato aislado no controla tiempos largos ni espectros. Un control de rotación exacta acumula cambio de orden uno. |
| R8 | Los bucles producidos desde E=0 son «bucles de flujo virtuales» | La no estacionariedad demuestra evolución desde una preparación. No basta para identificar esas excitaciones como virtuales respecto a un vacío todavía no construido. |

La simetría y los correladores propuestos en la respuesta pueden servir
como condiciones de consistencia una vez se construya un estado físico.
Exigir de antemano que las velocidades sean las relativistas deseadas no
puede sustituir su cálculo ni constituir una prueba de universalidad.

## Evidencia primaria y código

Se volvió a consultar primero `biblioteca/INDICE.md`, y después
`biblioteca/arXiv-2205.03148v4.pdf` pp.11–13 y 24–26: Gauss exige
autovalores locales f(x), los creadores físicos necesitan acompañamiento
gauge y las ecuaciones del walk libre fijan las matrices usadas abajo.
El PDF conserva el hash del manifiesto primario previo. Las ecuaciones
de acoplamiento de pp.18–19 y las alternativas magnéticas conservan el
alcance documentado en el informe de viabilidad.

Las deducciones se implementan en el artefacto permanente
[verify_eon_received_answer_audit.py](../scripts/verify_eon_received_answer_audit.py).
Su docstring fija antes de la ejecución los tres controles: Slater libre
unidireccional, plegado de fase en dos modos y rotación de masa aislada.
Son controles algebraicos, no nuevas referencias físicas aceptadas ni
simulaciones del QCA 3D gauge completo. No se utilizó código efímero para
producir los resultados retenidos.

## 1. Gauss con flujo cero: lema para un Slater puro

Sea P el proyector de correlación unipartícula de un Slater puro que
conserva número, y P_xy su bloque entre sitios. La regla de Wick da

`Var(N_x) = tr(P_xx) - tr(P_xx²)`.

La identidad `P²=P` proporciona una segunda expresión:

`Var(N_x) = sum_(y!=x) tr(P_xy P_yx) = sum_(y!=x) ||P_xy||_F²`.

Los términos son no negativos. Si E=0 exactamente y f(x)=2,
Gauss exige `N_x |FS> = 2 |FS>`: media 2 **y varianza cero** en todo
sitio. Para un Slater eso obliga a que no haya bloques P_xy fuera del
sitio. En un estado homogéneo obliga a un proyector P(k) constante.
Un proyector de bandas que dependa del momento no cumple esa condición.
El lema se limita a Slaters puros sin apareamiento y al producto con
flujo definido cero; no descarta estados materia–gauge entrelazados.
Tampoco prohíbe usar un vacío auxiliar con gauge fijado en una formulación
perturbativa: en ese caso hay que declarar cómo se imponen las restricciones
y se reconstruyen los observables físicos. Esa receta no está especificada
en la respuesta recibida.

### Control exacto con las matrices libres de Eon

Se usa un anillo de cuatro sitios y cuatro modos por sitio, con

`W(q) = exp(-i t gamma_0) exp(i q gamma_kappa)`,
`gamma_0 = Y tensor I`, `gamma_kappa = Z tensor Z`,
`t=pi/4`, `q=0,pi/2,pi,3pi/2`.

Es el control de una dirección del walk libre de pp.24–26, con los otros
momentos en cero. **No es el QCA gauge 3D interactuante.** En los cuatro
momentos las fases positivas son respectivamente
`omega=pi/4,pi/2,3pi/4,pi/2`, sin ambigüedad de signo en cero o pi.
Se ocupa el subespacio con fase `exp(+i omega)` (energía -omega).

El certificado comprueba que cada proyector es hermítico, idempotente,
de rango 2 y que cumple la ecuación espectral. Reconstruye por Fourier
el proyector global de 16 dimensiones y verifica su estacionariedad
bajo el walk libre. Sin embargo, en cada sitio resulta

`P_xx = I_4/2`, `<N_x>=2`, `Var(N_x)=1`.

Si se tensoriza con E=0, `<G_x²>=1`, no cero. La distribución local de N
se comprueba por la función generatriz `det(I-P_xx+z P_xx)`; la
probabilidad de N_x=2 es solo 3/8. El estado es estacionario como Slater
**del sistema libre**, pero no pertenece al sector físico propuesto
cuando se añade por producto el flujo cero. Esa es la distinción que
la respuesta recibida omite.

Para el walk 3D completo, si un llenado negativo se prolonga con esta
misma rama sobre el eje, los proyectores en q=0 y q=pi/2 ya son
distintos: no pueden formar un proyector constante en toda la zona.
El lema detectaría el mismo problema con E=0. No se ha construido aquí
esa prolongación, ni resuelto la clasificación de todos sus nodos.

Además, a t=0 y q=pi/2, no degenerado, el proyector negativo es
`(I+gamma_kappa)/2`, frente al de ocupaciones locales
`P_occ=diag(0,0,1,1)`. La distancia de Frobenius al cuadrado es 2.
Reducir la masa no los identifica. Esto contrasta la receta, no sustituye
el vacío físico por el control unidireccional.

## 2. El logaritmo principal pliega energías aditivas

Control de dos modos independientes, epsilon=1:

`H_add = (3 pi/4)(n_1+n_2)`;
`U = exp(-i H_add)`.

La representación de U por fases principales en (-pi,pi) tiene

`H_pr = H_add - 2 pi n_1 n_2`.

| Ocupación | Energía aditiva / pi | Energía principal / pi |
| --- | --- | --- |
| 00 | 0 | 0 |
| 10 | 3/4 | 3/4 |
| 01 | 3/4 | 3/4 |
| 11 | 3/2 | -1/2 |

Ambos operadores generan exactamente el mismo U, como comprueba el
código. Sus mínimos son distintos: vacío 00 para H_add y estado lleno
11 para H_pr. El término cruzado aparece incluso si los dos modos están
en sitios independientes separados arbitrariamente: el logaritmo
principal global no preserva automáticamente la localidad del generador
aditivo conocido. Esta tabla es una segunda vía explícita para ver el
fallo de aditividad, además de comprobar la igualdad de exponenciales.

El ejemplo también admite una codificación dentro de un solo sector de
Gauss: cada sitio contiene un fermión en dos orbitales, y n_1,n_2 indican
la excitación al orbital alto, no la carga total. Los cuatro estados
tienen exactamente un fermión por sitio. Con E=0 y f=1 todos satisfacen
el mismo Gauss; el certificado comprueba la isometría de esa codificación
y los dos números locales. El cambio de mínimo no depende por tanto de
comparar sectores de carga distintos. Es un control de selección, no una
identificación de estos orbitales con los de Eon.

El ejemplo refuta la suficiencia del criterio general recibido; no
calcula `log U_Eon` ni demuestra que ninguna rama pueda ser útil.
En volumen finito, con un corte espectral y una interpolación controlados,
puede elegirse un logaritmo útil. Esas hipótesis adicionales deben
demostrarse; no vienen de escribir la expresión formal.

Una cota de paso pequeño por grado de libertad tampoco es uniforme en
volumen: la suma de suficientes energías positivas pequeñas atraviesa
el corte de fase. En el walk, además, a masa cero y q=pi/2 se tiene
`W=i gamma_kappa`, con distancia en norma sqrt(2) a la identidad.
Ese q corresponde a momento físico ultravioleta al reducir epsilon.
El límite IR no controla por sí solo la norma en toda la zona, que es
pertinente al definir el logaritmo global o un matching ultravioleta.

## 3. Error pequeño por paso y control de correladores

La rotación de masa satisface `C(a)C(b)=C(a+b)`.
En el control **solo de masa**, la ocupación tras n pasos es
`2 sin²(n t)`. Tomar `t=pi/(2 n)` hace pequeño el cambio por paso
`2 sin²(t)`, pero deja el cambio tras n pasos exactamente igual a 2.
El certificado verifica la identidad de composición y los controles
n=8,16,32, sin ajuste numérico.

No se atribuye esta fórmula al paso Eon completo repetido: los bloques
cinéticos y gauge pueden modificar la dinámica entre pasos. Precisamente
por eso el dato de un paso no justifica una aproximación espectral.
Harían falta cotas para los tiempos y observables usados; no basta
llamar virtuales a las ocupaciones generadas ni pequeños a los errores
instantáneos. Los correladores para extraer velocidades exigen ese control.

## Qué ruta queda físicamente pendiente

Llenar las bandas libres sigue siendo una herramienta para definir el
problema fermiónico desacoplado. Para el sector gauge físico requiere
acompañamiento de flujo o una preparación/proyección explícita. Una
proyección de Gauss puede perder gaussianidad y estacionariedad: proyectar
un autoestado del walk sin gauge no lo convierte automáticamente en
autoestado del paso gauge original, que es otro operador.

Una preparación adiabática exige definir su estado inicial físico, la
trayectoria de reglas y el control espectral. g_E y g_M no pueden tratarse
sin más como interruptores independientes manteniendo la relación de
p.19. El tiempo imaginario requiere seleccionar antes un generador
físicamente justificado; aplicarlo a H_pr no resuelve su selección.

El encargo siguiente, si se decide continuar esa construcción, debe aportar
un estado materia–gauge explícito, demostrar Gauss como condición de
operador y su selección física, y comprobarlo con U original. No se
aceptan aquí las recetas recibidas como solución de esos requisitos.
No se elige otro candidato ni se abre el cálculo de propagadores o lazos.

## Reproducción y validación

Comando: `python3 -B scripts/verify_eon_received_answer_audit.py --output reports/2026-10-27--eon-received-answer-certificate.json`.
La salida conserva las matrices/escalas declaradas mediante sus controles
y los resultados exactos en el [JSON](2026-10-27--eon-received-answer-certificate.json).
El barrido y el manifiesto de esta ronda llevan los nombres
`2026-10-27--eon-received-answer-verifier-sweep.tsv` y
`2026-10-27--eon-received-answer-inputs.sha256`.

En la primera ejecución, la comparación de una fase exponencial exacta
no fue normalizada por el helper compartido. Se reescribió como
`cos(omega)+i sin(omega)`, conservando la misma ecuación espectral;
el certificado pasó después. No se modificó el helper ni se aceptó
el resultado fallido como evidencia.

El PASS del certificado valida estos controles y contraejemplos acotados;
no acredita un vacío, una revisión independiente ni un resultado sobre
velocidades físicas. A.int y la construcción del vacío siguen abiertas.
El barrido final pasa sus 45 verificadores; los hashes del manifiesto
coinciden, `text_integrity.py --check` devuelve cero problemas y
`git diff --check` pasa. El HEAD registrado es la base: el código nuevo
todavía no está comprometido y queda identificado por el manifiesto.
