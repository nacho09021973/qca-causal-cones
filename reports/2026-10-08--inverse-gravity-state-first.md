# IG-S0 — selección del estado como requisito de construcción

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato y controles congelados en `9bd3003`:
[IG-S0](../theory/INVERSE_GRAVITY_STATE_FIRST_GATE.md).
Corrección del comparador simbólico en `2dad9c4`, antes de la ejecución válida.

## 1. Resultado y decisión

`STATE_FIRST_PREFLIGHT_COMPLETE_AUTHOR_SIDE`.
`PRIORITY = CONSERVED_LOCAL_ENERGY_WITH_CORRELATED_REFERENCE`.
`STATE_FIRST_CONSTRUCTION_OPEN / NO_NEW_RULE_SPECIFIED`.

Se adopta como problema de construcción un par `(K,U)`: energía local con
vacío correlacionado accesible y tick exactamente unitario que conserve K.
El contrato exige además un puente cuantitativo entre energías pequeñas y
fases del tick, incluyendo todo el sector físico de baja energía.

La decisión es metodológica. No se ha construido ese par ni un nuevo vacío
tensorial. R1, dos polarizaciones, z=1, materia universal y Einstein siguen
OPEN. Los controles anteriores q=3 y los resultados A/B no se modifican.

Se descartan como justificación suficiente dos atajos: exigir que cada
puerta conserve el vacío, e identificar automáticamente la energía de un
parent con la quasienergía. La primera receta puede conservarse como
herramienta si supera sus filtros; no se demuestra que todos sus circuitos
sean inviables. Una tercera derivación acota la alternativa de partículas
de energía positiva sobre un vacío vacío.

## 2. Fuentes primarias y procedencia

Índice local consultado antes de la búsqueda. Lectura directa con
`pdftotext -f N -l M -layout <PDF> -`.

- Masaoka–Soejima–Watanabe, [arXiv:2406.06415v3](https://arxiv.org/pdf/2406.06415v3),
  `biblioteca/arXiv-2406.06415v3.pdf`, pp.3–5, teorema 1.
  SHA256 `15ddef1f64ae417845fef63e374b2c79048deaa5a74cea2c53aade3012f8ba66`.
- Gu–Wen, [arXiv:0907.1203v3](https://arxiv.org/pdf/0907.1203v3),
  `biblioteca/arXiv-0907.1203.pdf`, pp.11–12, ecs.27–37.
  SHA256 `3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
  Distingue el sector tensorial cúbico del lineal continuo. No aporta aquí
  un vacío finito controlado ni un tick conservador de la energía propuesta.

El PDF nuevo se descargó de su URL versionada. Se añadió a `curated.csv` y
se regeneró el catálogo con `~/herramientas/biblioteca_catalog/build_catalog.py`,
commit `783f078e04c4a82d48968494714aefbb25acc81b`. PDF e índice son locales
ignorados por Git; URL, versión, hash y ficha curada quedan trazados.
Las notas generadas anteriormente no se usan como fuentes primarias.

## 3. P1: preservar el vacío puerta a puerta puede trivializar la regla

Derivación del autor, álgebra finita. Sea X un soporte y

`|Omega> = sum_a sqrt(p_a) |a>_X |a>_rest`, con `p_a>0`

en su soporte de Schmidt. Si una puerta g_X cumple
`(g_X tensor I)|Omega> = lambda |Omega>`, entonces

`(g_X-lambda I)|a>_X=0` para cada a con `p_a>0`.

Si la reducida `rho_X` tiene rango completo en todo el Hilbert local,
`g_X=lambda I`. Para `h_X|Omega>=0` se obtiene análogamente `h_X=0`.
No se necesita positividad de h para esta última implicación.

Segunda derivación: escribir `D=g_X-lambda I`. Se tiene

`||(D tensor I)Omega||² = Tr(rho_X D†D) = ||D sqrt(rho_X)||_HS²`.

La norma nula implica que D se anula en el soporte de rho. Si
`rho_X>=mu I`, mu>0, también da
`||D||_HS <= ||(D tensor I)Omega||/sqrt(mu)`.
Esta cota no es uniforme si mu disminuye al cambiar soporte o volumen.

Alcance: no se ha demostrado que una futura referencia gravitatoria tenga
reducidas de rango completo. Con constraints pueden ser singulares; hace
falta comprobar su soporte. Ser fiel en un subespacio no implica rango
completo en el Hilbert local. Tampoco se exige invariancia por cada puerta
para que el tick completo conserve el estado.

Los controles fijados ilustran ambas excepciones. Para
`sqrt(1/3)|00>+sqrt(2/3)|11>`, el mapa de operadores locales tiene rango 4,
pero `Z tensor Z` conserva el estado aunque cada Z separado cambia su rayo.
Para `|11>`, el rango es 2 y una puerta local no escalar puede conservarlo.
Son controles de álgebra, no un diseño de vacío crítico.

## 4. P2: vacío común, energía y tiempo discreto son condiciones diferentes

### Hecho primario acotado

El teorema 1 citado supone un Hamiltoniano local frustration-free con grado
y coloreado de interacción acotados, y una correlación normalizada
`|<Omega|O(1-G)O'|Omega>|/(||O†Omega|| ||O'Omega||) >= b L^-alpha`
a distancia proporcional a L. G es todo el proyector fundamental.
Con normas locales uniformes obtiene
`gap(K_L) <= C (log L)²/L²`: el exponente del gap satisface z>=2.
No acota directamente quasifases ni cada banda por separado.

**Inferencia de diseño:** con esas hipótesis, K no puede tener un gap
puramente relativista `a/L`, a>0, como el de un sector dominante z=1.
No excluye una banda lineal acompañada de excitaciones más blandas. Usar K
solo para seleccionar un estado, sin identificarlo con el generador físico,
requiere examinar por separado la dinámica del tick.

### Comprobación algebraica independiente de la transferencia al tick

En tres niveles fijar el vacío |0> y, en los otros dos,
`P=|1><1|`, `Q=|v><v|`, `v=c|1>+s|2>`, `c²+s²=1`.
Entonces `K=P+Q` es positivo, tiene vacío común, y
`U=(I-2Q)(I-2P)` lo conserva exactamente.

Sobre el bloque excitado:

`K = [[1+c², cs], [cs, s²]]`,
`U = [[2c²-1, -2cs], [2cs, 2c²-1]]`.

Traza y determinante dan energías `1-c,1+c` para 0<c<1.
Tomando la familia prefijada `c=(1-t²)/(1+t²)`, `s=2t/(1+t²)`,
las fases del bloque son `±4 atan(t)` y la energía menor es
`epsilon=2t²/(1+t²)`. Por tanto `phase²/epsilon -> 8`.
El exponente de una fase no se hereda del gap del parent por identidad.
Además, a t=1/2,

`||U†KU-K||_HS² = 41472/15625 > 0`.

Es un contraejemplo exacto a «vacío común implica conservación del parent».
El parámetro t no es momento ni tamaño de red. Este control no certifica
una dispersión lineal QCA, ni elude por sí mismo el teorema Hamiltoniano.
Justifica mantener separados estado, conservación y puente energía–tick.

## 5. P3: el vacío vacío con energía positiva no da una banda lineal simple

Derivación del autor, con hipótesis restringidas. Sea h(k) una matriz
hermítica analítica de tamaño fijo, positiva para k a ambos lados del origen.
Sea P el proyector a `ker h(0)` de dimensión r>0. Para cualquier v en ese
kernel y dirección n, `v†h(t n)v>=0` tiene mínimo en t=0. Luego

`v† (n·grad h)(0) v = 0` y, por polarización,
`P (n·grad h)(0) P = 0`.

La expansión da `P h(k) P = O(|k|²)`. Por mínimo–máximo, las r menores
autovalores satisfacen `0 <= lambda_j(k) <= C |k|²` cerca del origen:
basta usar el subespacio fijo ran(P) como espacio variacional. Si r es toda
la dimensión, el mismo argumento acota toda la matriz. Las otras bandas
permanecen separadas de cero por continuidad.

Por tanto esas bandas que nacen de cero no pueden ser `c|k|+o(|k|)`, c>0.
Una energía de una partícula de alcance finito produce un símbolo analítico,
pero la aplicación requiere además positividad sobre el vacío elegido.
No se aplica automáticamente a modos colectivos interactuantes, a matrices
dinámicas bosónicas BdG o a un mar fermiónico con bandas llenas.

Segunda vía de control: `2 sum_j(1-cos k_j) I_2` es positivo y cuadrático;
`sin(k) sigma_z` tiene pendientes opuestas, pero una energía negativa.
Convertir ambas ramas en positivas usando valor absoluto introduce una
no analiticidad en k=0. Estos ejemplos delimitan las hipótesis; la prueba
general es la anterior, no una extrapolación desde los ejemplos.

## 6. Ejecución, reparación y nivel de evidencia

La primera ejecución falló al comparar el polinomio característico: SymPy
recrea su generador sin la hipótesis `real=True` del símbolo solicitado y
ambos símbolos resultaban distintos. El stdout y la transcripción del punto
de fallo se conservan en [intento 1](2026-10-08--inverse-gravity-state-first-attempt1.txt).
La reparación alinea el generador y añade reconstrucción por traza y
determinante; no cambia matrices, parámetros ni criterios del contrato.

Con código `2dad9c4` se ejecutó:

`python3 -B scripts/verify_inverse_gravity_state_first.py`

SymPy 1.14.0, aritmética exacta, salida 0. La salida completa está en
[certificado](2026-10-08--inverse-gravity-state-first-certificate.txt).
Confirma también que el símbolo solicitado y el generador eran distintos.
Las tres familias auxiliares pasan; la prueba general del teorema citado
pertenece a sus autores. Nuestras derivaciones no tienen revisión independiente.

## 7. Lo que debe entregar el siguiente candidato

La ruta E queda formulada como un problema simultáneo, no como búsqueda de
un Gibbs para puertas ya elegidas. Debe entregar una identidad local de
conservación de K, una construcción accesible de su estado fundamental y
control del puente energía–tick. Conservación implica estacionariedad de
`G/Tr G`; no implica preparación, unicidad, correlaciones críticas ni z=1.

La primera admisión de un candidato exige celda y operadores concretos. No
se reutiliza automáticamente q=3, no se declara que un estado sea fiel sin
calcularlo y no se impone TT microscópico para contar dos modos. Las puertas
pueden alterar el estado dentro del tick si lo restablecen al completarlo.
La frustración está permitida para evitar imponer la receta S como necesidad;
su mera presencia tampoco garantiza viabilidad.

El trabajo de este expediente termina con estos filtros y el contrato de
construcción. No hay nuevo autómata certificado ni prueba de imposibilidad
general. La selección del estado entra ahora como condición previa de diseño.
