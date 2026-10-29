# A.int — construcción y comprobación de un estado materia–gauge

Fecha: 2026-10-27. Autor: Codex. Encargo del usuario: «hazlo».
Especificación previa:
[A_INT_EON_PROJECTED_GAUSSIAN_REFERENCE.md](../theory/A_INT_EON_PROJECTED_GAUSSIAN_REFERENCE.md).

## Resultado y objetivo pendiente

`EXPLICIT_NORMALIZABLE_GAUSS_STATE_CONSTRUCTED / GAUSSIAN_TAIL_STATIONARITY_FAIL`.
**No se ha conseguido un vacío físico aceptado del QCA original.**
Se ha construido un estado puro materia–gauge con Gauss exacta, norma
finita, energía eléctrica esperada finita y un criterio auxiliar explícito
de preparación. El intento no cierra el objetivo: la demostración analítica
de abajo excluye su estacionariedad exacta bajo las hipótesis declaradas.

Evidencia: `AUTHOR_ANALYTIC_PROOF_AND_EXACT_INGREDIENT_CHECKS /
INDEPENDENT_REVIEW_PENDING`. El código no es una segunda revisión de
la demostración de análisis complejo. No se registra un no-go para todo
vacío de Eon, ni un resultado sobre velocidades o lazos.

## 1. Modelo y criterio de selección que se han fijado

Se conserva Eon v4, `U=D_M D_E D_F`, sobre el toro cúbico L=3,
epsilon=1, m=pi/4, g_E=g_M=1, en el sector `div E+N-2=0`.
Los registros eléctricos son enteros, no cíclicos ni truncados.
Se utiliza la exponencial magnética exacta (21)/(36), con ángulo 1/2.

Fuente primaria: `biblioteca/arXiv-2205.03148v4.pdf`, pp.6–9
(rotores, V conmutativos, localidad y plaquetas), pp.11–13 (Gauss),
pp.18–23 y 28–29 (paso gauge) y pp.24–26 (matrices de Dirac y transporte).
Se comprobó primero el índice local y después estos objetos directamente
en el PDF. Su hash es el del manifiesto primario anterior.

Como criterio **auxiliar de preparación** se toma el Hamiltoniano
fermiónico aditivo con símbolo

`h_D(k)=m gamma_0 - sum_a sin(k_a) gamma_a`.

Es local, gapped para m>0 y coincide con el primer jet Dirac usado en el
walk. Su extensión a toda la zona de Brillouin es una elección adicional,
no una energía exacta o conservada que se haya deducido de U. En concreto,
no se reemplaza el circuito por `exp(-i h_D)` ni se minimiza `log U`.
Los gamma son los del PDF p.24. Sus anticomutadores dan

`h_D(k)²=[m²+sum_a sin²(k_a)] I`.

El estado |FS_D> llena las dos bandas negativas de cada momento;
es el mínimo fermiónico de esa energía aditiva con N_total=2V.
El subespacio ocupado y el Slater quedan determinados salvo una fase
global. El código comprueba el proyector
`P_-(k)=[I-h_D(k)/sqrt(m²+sum sin²(k_a))]/2`, su rango 2 y su ecuación
espectral. No se le atribuye estacionariedad bajo D_F original.

El campo se prepara con pesos eléctricos gaussianos, beta=log(2), y
se impone Gauss por proyección. El criterio es una preparación Dirac
con amortiguamiento de energía eléctrica y Gauss; es físicamente motivado
como candidato, pero **no demuestra selección del vacío del QCA**.
La prueba de estacionariedad es un requisito separado que no supera.

## 2. Estado explícito, incluyendo materia y campo

Se usan la base de ocupaciones fermiónicas y la base de rotor definida
por las traslaciones V de las ecuaciones (4)–(6). Al ser V unitarios,
conmutativos y con acción de desplazamiento sobre los enteros, sus potencias
fijan las fases de esa base. En la realización local JW del artículo puede
haber fases diagonales adicionales: se transporta la preparación mediante
esa equivalencia, no se borra su efecto sobre U. Las cotas de módulos
eléctricos usadas después no cambian por esas fases.

Para un enlace,

`|g_beta> = Theta(2 beta)^(-1/2) sum_(E in Z) exp(-beta E²)|E>`;
`Theta(2 beta)=sum_(E in Z) exp(-2 beta E²)`.

Sean P_G los proyectores conjuntos de todos los `G_x=div E_x+N_x-2`.
La propuesta completa es

`|Omega_beta> = Z^(-1/2) P_G (|FS_D> tensor tensor_links |g_beta>)`;
`Z=||P_G (|FS_D> tensor tensor_links |g_beta>)||²`.

En términos de configuraciones, si A(n) es el determinante de Slater
para la ocupación n, su coeficiente es proporcional a

`A(n) exp[-beta sum_links E_l²] 1_(div E=2-N(n))`.

El orden de sitios y modos está fijado en la especificación. Es una
fórmula explícita en un volumen finito con rotores enteros infinitos,
no un «autoestado de U» definido circularmente por el problema a resolver.

### Gauss, existencia y normalización

Cada término retenido satisface G_x=0 como identidad de operador. Para
cualquier configuración n del Slater, `sum_x [2-N_x(n)]=0`. En una red
conexa existe un flujo entero con esa divergencia: se elige un árbol,
se acumula la carga de cada subárbol y se envía al padre, desde las hojas
hasta la raíz. La neutralidad anula el remanente en la raíz.
Ese procedimiento solo demuestra existencia; no elige un árbol privilegiado
en el estado, que suma sobre todos los flujos admitidos.

Hay al menos un A(n) no nulo. Como el peso gaussiano es positivo para
todo E entero, la proyección no puede anular todo el estado: Z>0.
Por ser P_G una proyección sobre un vector normalizado, Z<=1.
Así, el estado está definido y normalizado exactamente.

Además, la suma de `sum E_l² exp(-2 beta sum E_l²)` sobre los enteros
converge para beta>0. Hay un número finito de configuraciones fermiónicas
y de enlaces. Restringir la suma a Gauss y dividir por Z>0 conserva la
finitud de la energía eléctrica esperada. No se usa un corte de E.

El Slater tiene fluctuaciones locales de número, porque su proyector
depende del momento. Gauss correlaciona cada patrón de carga con una
divergencia eléctrica distinta. Los estados de campo de dos divergencias
distintas son ortogonales: la proyección produce entrelazamiento, en vez
de dejar un producto con E=0. Todos los patrones de carga con amplitud
inicial no nula siguen teniendo algún flujo de peso no nulo.

En la representación abstracta de fermiones y rotores, el Slater es
homogéneo hasta fase, los pesos de enlace son homogéneos y P_G es
covariante bajo traslaciones. La densidad resultante es homogénea.
Esto no afirma invariancia bajo rotaciones que no sean simetrías exactas
del orden de capas del QCA.

### Segunda vía de control, con cola infinita acotada

El certificado implementa el algoritmo de flujo entero en L=3,4 para
configuraciones neutras de control, y contrasta su divergencia exactamente.
También conserva un control de dos patrones opuestos de carga en un enlace
y un número entero n de vueltas alrededor de una plaqueta. Es un control
algebraico de la construcción, **no la evaluación del Slater 3D completo**.

Sus dos energías eléctricas son `4n²+2n+1` y `4n²-2n+1`. Con beta=log(2),
los pesos cuadrados son `4^(-energia)`. Ambas series tienen la misma
norma por n -> -n; los sectores de divergencia son ortogonales. La
pureza reducida de materia es 1/2: el control está entrelazado y es normalizable.

Para |n|>=1, ambas energías son al menos `2n²+1`. Tras conservar
|n|<=K, la cola de la norma no normalizada está acotada por

`T_K <= [16^(-(K+1)²)/2]/[1-16^(-(2K+3))]`.

La norma parcial S_K es una cota inferior estrictamente positiva; la
probabilidad de la cola normalizada es <=T_K/S_K. El JSON conserva los
valores racionales K=0,1,2. Esto controla las sumas de ese ejemplo sin
sustituir el rotor del modelo por un registro finito.

## 3. Prueba de estacionariedad: obstrucción para colas gaussianas

### Alcance del argumento

Volumen finito L>=3; número finito de modos fermiónicos; flujos enteros;
magnetismo exponencial exacto con ángulo real no nulo. Supóngase un
vector no nulo con coeficientes en la base eléctrica que satisfacen

`|psi_n(E)| <= C exp[-beta sum_l E_l²]`, beta>0.

Se demuestra que **no puede ser autoestado de U** en esta clase.
Para un vector puro, estacionariedad de la densidad equivale a ser
autoestado hasta fase. La propuesta anterior pertenece a esta clase,
incluso después de Gauss y normalización: la proyección solo anula
coeficientes y Z es una constante positiva en el volumen fijado.

Este es un argumento analítico del autor, pendiente de revisión
independiente. El certificado comprueba sus ingredientes algebraicos;
no pretende certificar por un muestreo la conclusión universal.

### A. Antes del magnetismo las colas siguen siendo gaussianas

D_F consta de un número finito de gates en el volumen fijado. Sus
transportes desplazan los E enteros un número acotado de unidades;
sus monedas mezclan un número finito de componentes. Los factores JW
solo añaden fases. Una combinación finita de gaussianas desplazadas
sigue acotada por otra gaussiana, por ejemplo con beta/2 y una constante
mayor. D_E multiplica por fases `exp(i alpha_E sum E²)` y no cambia
sus módulos. Por tanto `phi=D_E D_F psi` tiene también esa cota.

Esto no aproxima D_F ni D_E. Las constantes pueden depender del volumen;
no se afirma una cota termodinámica uniforme.

### B. El magnetismo en la representación de Fourier

Los V de enlaces distintos conmutan (PDF pp.7–8). Los operadores de
plaqueta son productos de V y V†, de modo que sus exponenciales exactas
se diagonalizan simultáneamente en Fourier eléctrico. En cada componente
fermiónica, D_M multiplica por

`exp[i theta B(z_1,...,z_M)]`,

donde B es la suma de los monomios de plaqueta y sus inversos. No se
están diagonalizando los subpasos fermiónicos. Elegido un enlace e y
fijados los otros ángulos, B tiene la forma

`B(z)=a z+b/z+c`.

a no es idénticamente cero: al fijar los otros ángulos a cero, las
cuatro plaquetas adyacentes dan coeficiente a=4. El código comprueba
ese recuento en L=3,4. Para ángulos genéricos de los otros enlaces se
tiene a!=0, y puede elegirse a la vez una componente no nula de phi.
Si la componente desapareciese para todo un abierto de esos ángulos,
la unicidad de sus series analíticas la haría idénticamente nula.

> Nota 2026-10-29: «a=4» y la frase sobre el código están **retiradas**
> (Adenda 2026-10-28, reparación 4; Adenda 2026-10-29, D1–D2). a es una suma de cuatro
> monomios de Laurent distintos con signos ±1 y no es idénticamente nulo.

### C. Crecimiento de Fourier y contradicción

Las colas gaussianas hacen holomorfas las series en z!=0. Al sumar los
otros índices, y con r=|z|, la identidad

`-beta n²+n log r = -beta[n-log r/(2 beta)]² + (log r)²/(4 beta)`

da, uniformemente en el ángulo de z,

`log |f(z)| <= C_0+C_1(log r)²`.

La suma gaussiana trasladada está uniformemente acotada, por ejemplo
por `1+sqrt(pi/beta)`. La misma estimación vale para la serie g de psi.
Si U psi=lambda psi, en la componente elegida se tendría

`g(z)=exp[i theta(a z+b/z+c)] f(z)`

(absorbiendo en g la fase lambda). f no es idénticamente nula.

> Nota 2026-10-29: la forma correcta es `exp[i theta B(z)] f(z) = lambda g(z)`,
> con f la serie de `phi=D_E D_F psi` y g la de psi (Adenda 2026-10-28, reparación 1).

En un arco de fracción 1/3 del círculo puede imponerse
`Re(i theta a z) >= |theta a|r/2`. Allí, usando la cota de g,

`log |f(z)| <= C_0+C_1(log r)²-|theta a|r/2+O(1)`.

En el resto del círculo se conserva la cota propia de f.
Por tanto su media angular satisface

`M_f(r) <= C_2+C_3(log r)²-|theta a|r/6`.

Pero para una función holomorfa no nula en un anillo exterior,
la media angular de log|f| es convexa en log r (fórmula de Jensen
en anillos). En particular tiene una cota inferior afín
`M_f(r)>=A+B log r` para r suficientemente grande. Los ceros aislados
son integrables en la media; no invalidan esta propiedad.
Las dos cotas son incompatibles al crecer r. Contradicción.

### D. Controles alternativos y límites

Para series de Laurent finitas la obstrucción tiene una segunda prueba
puramente algebraica. Derivar la misma igualdad exige

`f g' - g f' = i theta(a-b/z²) f g`.

Si los grados máximos de f y g son p y q, la izquierda tiene grado
<=p+q-1; la derecha contiene un término no nulo de grado p+q cuando
theta a!=0. El certificado contrasta ejemplos de grados positivos y
negativos; el argumento general es el de grados escrito aquí.

Un control fuera de la hipótesis de colas gaussianas es
`f=exp[-i theta(z+1/z)]`, `g=1`, que sí cancela el multiplicador.
El código verifica esa identidad. Su crecimiento logarítmico en una
dirección compleja es lineal en r, no cuadrático en log r. No es un
autoestado del QCA: solo muestra por qué la hipótesis de crecimiento
es esencial y por qué no se ha demostrado ausencia de todos sus estados.

El argumento no se aplica a una red sin plaquetas, a ángulo magnético
cero, a rotores cíclicos finitos ni automáticamente a la implementación
magnética aproximada (26). Tampoco compara límites continuos o
termodinámicos. No se afirma que una cota gaussiana sea necesaria para
un vacío físico; aquí es una propiedad del candidato que se ha probado
incompatible con su estacionariedad exacta.

## 4. Qué se ha logrado y qué no

El problema de Gauss del producto Slater tensor E=0 sí se ha reparado:
hay una fórmula explícita, normalizable y materia–gauge entrelazada,
con energía eléctrica esperada finita y sin cambio de circuito.
También se ha declarado, sin ocultarlo, el criterio auxiliar que la
selecciona como preparación de referencia.

**No se ha satisfecho el requisito de estacionariedad y, por tanto,
no hay vacío aceptado para los correladores.** El rechazo no se basa
en un error numérico de una caja ni en el logaritmo principal de U,
sino en la obstrucción analítica anterior, con su alcance limitado.
Una revisión independiente de esa prueba sigue pendiente.

Variar beta>0 o aumentar un corte eléctrico no evita esta obstrucción
del ansatz. Tampoco autoriza a cambiar el modelo por el Hamiltoniano
de preparación. Un candidato distinto tendría que justificar otra
estructura de colas y una selección física, y resolver su propia
ecuación de estacionariedad. Que esos estados puedan existir no se
ha probado ni refutado aquí. No se inicia un nuevo ensayo ni un lazo
como continuación automática de este fallo.

## Artefactos y validación

* Especificación previa: [candidato proyectado](../theory/A_INT_EON_PROJECTED_GAUSSIAN_REFERENCE.md).
* Código permanente: [verify_eon_projected_gaussian_reference.py](../scripts/verify_eon_projected_gaussian_reference.py).
* Resultados de controles: [JSON](2026-10-27--eon-projected-gaussian-certificate.json).
* Barrido: `2026-10-27--eon-projected-gaussian-verifier-sweep.tsv`.
* Manifiesto: `2026-10-27--eon-projected-gaussian-inputs.sha256`.

El comando del certificado consta en su `--help`. Los objetos grandes
de volumen 3D se definen analíticamente; no se afirma haber enumerado
todos los determinantes o todos los flujos. El JSON distingue los
controles pequeños de la construcción general y de la prueba analítica.
Ningún PASS de esos controles convierte este intento en un vacío válido.
El barrido final pasa los 46 verificadores, con cero fallos. La integridad
textual devuelve cero problemas y `git diff --check` pasa. El barrido
registra el HEAD de base porque el código nuevo aún no está en un commit;
el manifiesto fija todos los verificadores, helper, runner, especificación,
PDF y JSON de esta ronda. No se invocó revisión externa.

## Adenda de reparación — 2026-10-28

Revisión independiente sellada: DeepSeek **ACCEPT_WITH_REPAIRS**
([registro y lectura del autor](../debates/2026-10-28--eon-gaussian-review-deepseek/verificacion_autor.md)),
sobre los bytes de `5dbd843`. Esta adenda la escribe Claude Opus 5.5. El texto
anterior se conserva; estas reparaciones lo sustituyen donde lo contradicen.
El certificado y el JSON no cambian.

1. **§3.C, notación (G-R1-01, G-R1-06).** Se fija: f es la serie de Fourier de
   la componente elegida de `phi=D_E D_F psi`, y g la de la misma componente
   de psi. `U psi=lambda psi` con `abs(lambda)=1` se escribe
   `exp[i theta B(z)] f(z) = lambda g(z)`, es decir
   `f(z)=lambda exp[-i theta B(z)] g(z)`. En el arco donde
   `Re(i theta a z) >= abs(theta a) r/2`, que ocupa 1/3 del círculo, se tiene
   `abs(f) <= exp[-abs(theta a) r/2 + O(1)] abs(g)`. Es la cota que ya usaba
   el texto; el revisor había intercambiado f y g. El control de §3.D
   (`f=exp[-i theta(z+1/z)]`, `g=1`) es coherente con esta convención.
2. **§3.C, convexidad (G-R1-02).** Enunciado preciso: si f es holomorfa y no
   idénticamente nula en `R_0<abs(z)<infinito`, `log abs(f)` es subarmónica.
   La media `M_f(r)=(2 pi)^-1 integral log abs(f(r e^{i t})) dt` es finita
   salvo en radios aislados con ceros sobre la circunferencia, y es convexa en
   `log r`. Una recta de apoyo da `M_f(r) >= A+B log r`.
3. **§3.A, cotas gaussianas (G-R1-03).** En volumen finito, D_F desplaza E por
   vectores de un conjunto finito S y mezcla un número finito de componentes
   fermiónicas con coeficientes acotados. Para `0<beta'<beta` y cada `delta`
   en S, `exp(-beta abs(E+delta)²) <= C exp(-beta' abs(E)²)`. D_E solo
   multiplica por fases. La cota con `beta/2` del texto es un caso de esto.
4. **§3.B, operadores V y coeficiente a (G-R1-04). Reparación de contenido.**
   En Eon v4 los `V_{x:eta}` llevan cadenas JW y la paridad gauge se trata
   como fermión (PDF p.7, §§2.2–2.3); conmutan por la ec. (4). Para una
   configuración fermiónica fija, que D_M no cambia, se define
   `|E>' := V_1^{E_1}···V_M^{E_M}|0>`. Por la conmutación está bien definido
   y difiere de `|E>` solo en una fase. En esa base cada V_ℓ es un
   desplazamiento puro, D_M multiplica la serie de Fourier por
   `exp[i theta B(z)]` y los módulos de los coeficientes no cambian. Así
   pasan las cotas gaussianas. El precio es que, en esa base, cada monomio de
   plaqueta puede llevar un signo ±1 fijo. Por eso **se retira** «al fijar los
   otros ángulos a cero, las cuatro plaquetas adyacentes dan a=4». El recuento
   del certificado (`magnetic_harmonic_counts`) cuenta flujos sin esos signos y
   no certifica el valor de a. Lo que vale es que a es una suma de cuatro
   monomios de Laurent en los otros enlaces, con coeficientes no nulos. Para
   L>=3 los cuatro usan conjuntos distintos de enlaces, son linealmente
   independientes y a no es idénticamente nulo, con cualquier signo. La
   reducción del registro de enlace a un entero E_ℓ por enlace se toma de §1
   y no se vuelve a derivar aquí.
5. **§3.B, elección genérica (G-R1-05).** La restricción de la componente
   elegida a z_e, y a como función de `z_{≠e}`, son no nulas fuera de
   conjuntos de ceros propios. Se fijan `z_{≠e}` en el toro unidad fuera de
   ambos.

Estado: `REVIEWED_ACCEPT_WITH_REPAIRS`; reparaciones aplicadas por el autor de
esta adenda y **no revisadas de nuevo**. La reparación 4 descansa en un
argumento del autor que DeepSeek no ha visto. No cambia el veredicto
`GAUSSIAN_TAIL_STATIONARITY_FAIL` en su clase ni promueve evidencia. No hay
vacío físico, correladores, velocidades ni lazo.

## Adenda 2026-10-29 — formalización tras la re-revisión

Re-revisión independiente sellada de la adenda anterior: DeepSeek **PASS_WITH_REPAIRS**
([registro y lectura del autor](../debates/2026-10-28--eon-addendum-review-deepseek/verificacion_autor.md)).
Revisó este informe con sha256 `9539e275…400f`, que es el de `3395c1c`. No encuentra ningún
error en la adenda. Pide siete reparaciones de redacción o formalización (D1–D7). Las escribe
Claude Opus 5.5. El certificado y el JSON no cambian.

- **D1–D3.** Las frases de §3.B («a=4», «el código comprueba ese recuento») y la forma de §3.C
  sin `lambda` se conservan. Llevan ahora una nota que remite a las reparaciones 1 y 4 de la
  adenda anterior.
- **D4. Un entero por enlace.** En Eon v4 cada enlace tiene un campo en cada extremo, `x:eta` y
  `(x+eta):-eta`, y se impone `E_{x:eta} = -E_{x+eta:-eta}` (PDF p.6). El PDF lo presenta como
  una restricción que elimina grados de libertad no exigidos por la invariancia gauge, no como
  una consecuencia de ella. Este informe trabaja dentro de esa restricción. Para cada enlace se
  fija la orientación positiva `eta` y se toma `E_l := E_{x:eta}`.
  - `U_{x:eta} = r_{x:eta} r^dagger_{x+eta:-eta}` (ec. (2), PDF p.7) baja `E_{x:eta}` en uno y sube el
    otro extremo, así que conserva la restricción.
  - `V_{x:eta} = U_{x:eta} prod_y Z_y` (ec. (6), PDF p.7). Las `Z_y` son paridades diagonales
    en la base eléctrica y de ocupación (PDF p.7).
  - Por tanto, en esa base `V_l` es un desplazamiento `E_l -> E_l - 1` multiplicado por un
    signo diagonal. No cambia las ocupaciones fermiónicas.
- **D5. Ortonormalidad.** Como cada `V_l` desplaza un solo entero y multiplica por un signo
  diagonal, `V_1^{n_1}···V_M^{n_M}|0>` está soportado en una única configuración eléctrica
  estándar, con un signo. Los vectores de distintas `n` son ortogonales y de norma uno. El
  estabilizador es trivial y la etiqueta es inyectiva.
- **D7. Convención de signo.** Por D4, `V_l` baja `E_l`, así que la definición de la adenda
  anterior, `V_1^{E_1}···V_M^{E_M}|0>`, está soportada en la configuración `-E`. Se fija
  `|E>' := V_1^{-E_1}···V_M^{-E_M}|0>`, soportado en `E`. El cambio `E -> -E` solo intercambia
  `z` y `1/z` en las series, y `a` con `b` en `B(z)=a z+b/z+c`. Tanto `a` como `b` son sumas de
  cuatro monomios de plaqueta, así que el argumento no depende de esta convención.
- **D6. Las cuatro plaquetas.** En el toro cúbico 3D, un enlace e en la dirección `mu` está en
  dos plaquetas de cada uno de los dos planos que lo contienen (`mu-nu`, `mu-kappa`), una a
  cada lado. Cada plaqueta contribuye a `a` con el producto de sus otros tres enlaces (o sus
  inversos), con un signo ±1 fijo. Para `L >= 3`, las dos plaquetas de un plano usan enlaces
  paralelos distintos, y las de planos distintos usan enlaces en direcciones distintas. Los
  cuatro conjuntos de otros enlaces son distintos, así que los cuatro monomios de Laurent son
  distintos y linealmente independientes. Con coeficientes no nulos, `a` no es idénticamente
  nulo, sean cuales sean los signos.

Estado: `REVIEWED_PASS_WITH_REPAIRS`; D1–D7 aplicadas por el autor y **no revisadas de
nuevo**. D4 se apoya en el PDF primario (p.6, ec. (1) y la restricción de signos; p.7, ecs. (2) y (6) y la paridad Z), leído en texto
extraído. No cambia `GAUSSIAN_TAIL_STATIONARITY_FAIL` en su clase ni promueve evidencia.
