# IG-S0 — diseñar la referencia física antes de las puertas

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Padre: [charter de diseño inverso](INVERSE_GRAVITY_DESIGN_CHARTER.md).
Autorización directa: «adelante con tu recomendacion», después de recomendar
una arquitectura que incorpore selección de estado y control de excitaciones.

## 1. Alcance y presupuesto de este expediente

Abrir una arquitectura sucesora dentro de la misma envolvente: Z³, dimensión
local finita independiente de L, tick e inversa de alcance estricto uniforme.
El objetivo continúa siendo Einstein 3+1; R0–R8 no cambian. El tick q=3
anterior conserva sus resultados y A/B sus cierres; no se retocan sus puertas.

Este expediente formula el mecanismo de selección, examina dos recetas
concretas y deriva filtros antes de especificar otro autómata. Un único
preflight analítico y tres controles algebraicos auxiliares, sin barridos.
Se cierra con una decisión de diseño y obligaciones de construcción.
No incluye espectro de un QCA nuevo: todavía falta su regla microscópica.

## 2. Mecanismo prioritario: energía conservada y vacío correlacionado

Construir conjuntamente `(álgebra local, sector físico, K_L, U_L)`:

1. `K_L = sum_x k_x` tiene términos de soporte y norma acotados uniformemente,
   con periodo espacial fijo. Es autoadjunto y acotado inferiormente por
   `-b L³`. Se permite frustración: su mínimo global no tiene por qué minimizar
   cada término. Debe tener una justificación física previa; no basta elegir
   una función espectral global de U y llamarla energía local.
2. `U_L` es un QCA exacto, con inversa explícita; preserva el sector físico y
   satisface `U_L† K_L U_L = K_L` en él. La identidad se exige al tick completo,
   sin imponer que cada puerta conserve K o su estado fundamental.
3. En cada toro admisible, `G_L` es el proyector al mínimo de K en ese sector.
   La receta fija `rho_0,L = G_L/Tr G_L`. Exige un límite local reproducible y
   expectativas accesibles con error controlado. Si hay degeneración, debe
   controlarse su efecto local; no se escoge un vector favorable a posteriori.
   La conservación implica estacionariedad por cálculo funcional, no por
   promediar tiempos. La preparación de rho es una condición inicial;
   no se supone que U enfríe cualquier estado hasta ella.
4. Hay que demostrar que K ordena las excitaciones del tiempo físico del tick.
   Como condición suficiente de esta ruta, exigir una fase común del vacío
   `U_L G_L = exp(-i phi_0,L) G_L` y, con tick de duración adimensional 1,

   `||(exp(i phi_0,L) U_L - exp(-i (K_L-E_0,L))) P_L(Lambda)||`
   `<= C Lambda^(1+eta)`, con `eta>0` y C independientes de L.

   Aquí `P_L(Lambda)` incluye **todo** el espectro físico con
   `0 <= K_L-E_0,L <= Lambda`. Lambda está por debajo de una constante fija
   menor que pi. No se omiten nodos, especies o fases pi por conveniencia.
   Estos proyectores son herramientas del análisis, no puertas no locales.
   La exponencial del lado derecho tampoco define el QCA.
5. El estado y sus observables deben permitir controlar la respuesta y el
   sector tensorial. Dos polarizaciones físicas, z=1 y positividad de pesos
   espectrales se comprueban después; ninguna se deduce de `[U,K]=0`.

El orden de límites será L→∞ sobre toros compatibles a Lambda fija y después
Lambda→0. La dimensión local, periodo, términos, puertas, simetrías y
perturbaciones admisibles se fijarán antes de ejecutar el candidato.
El criterio del punto 4 es una elección exigente de esta ruta, no un teorema
de necesidad para toda gravedad emergente. Una alternativa requiere contrato
previo con errores y significado físico comparables.

Esta receta evita el promedio de tiempos de B, pero **no** suministra por
sí sola K, U ni acceso a su vacío. Resolver sus identidades es el problema
de construcción; no se declara R1 satisfecho.

## 3. Dos recetas que deben pasar el filtro temprano

**S — núcleo común de términos locales.** Elegir `h_X>=0` con
`h_X |Omega>=0` y puertas `exp(-i theta_X h_X)`. El vacío queda fijo por
construcción. Examinar separadamente: existencia de términos no triviales,
conservación de `sum h_X`, y relación entre su gap y las fases del tick.
No transferir un teorema de Hamiltonianos a una unitaria discreta sin puente.

**E — energía global conservada con vacío correlacionado.** Es la receta de
§2. Permite que las puertas intermedias cambien el estado, siempre que el
tick cumpla las identidades. Es prioritaria si S solo proporciona
estacionariedad o entra en una obstrucción bajo las hipótesis declaradas.
Su viabilidad queda OPEN hasta construir un par local concreto.

## 4. Preflight congelado antes de ejecutar controles

P1. Para estado puro y soporte X, derivar qué permite
`(g_X tensor I)|Omega> = lambda |Omega>` a partir de la matriz reducida.
Comprobar por Schmidt y por norma de Hilbert–Schmidt. Distinguir rango
completo en el espacio local de rango dentro de un subespacio restringido.

P2. Contrastar el alcance del teorema 1 de Masaoka–Soejima–Watanabe,
`arXiv:2406.06415v3`, PDF pp.3–5, para un parent frustration-free crítico.
Especificar hipótesis sobre correlaciones, degeneración y gap; no inferir
que prohíbe cualquier banda lineal o todo circuito que preserve ese vacío.
Comprobar explícitamente que compartir vacío no implica conservar el parent.

P3. Para un símbolo hermítico analítico finito `h(k)>=0` cerca de k=0 con
kernel no vacío, examinar si las bandas que nacen de cero pueden tener
pendiente lineal no nula. Segunda vía: mínimo–máximo y ejemplos exactos.
Este filtro afecta a excitaciones de una partícula sobre vacío vacío cuando
h es su energía; no a toda teoría bosónica interactuante ni a sistemas BdG.

Script permanente: `scripts/verify_inverse_gravity_state_first.py`.
Controles prefijados, auxiliares y sin interpretación como red gravitatoria:

- Schmidt: `Omega_p=sqrt(p)|00>+sqrt(1-p)|11>` para p=1/3 y p=0;
  rango del mapa `D -> (D tensor I)Omega_p`, identidad de norma y acción de
  `Z tensor Z`. El caso p=0 comprueba la excepción de rango deficiente.
- Núcleo común: en tres niveles, añadir |0> a dos proyectores de rango uno
  en span{|1>,|2>}. `P=|1><1|`, `Q=|v><v|`,
  `v=c|1>+s|2>`, `c=(1-t²)/(1+t²)`, `s=2t/(1+t²)`, `0<t<1`.
  `K=P+Q`, `U=(I-2Q)(I-2P)`. Verificar vacío, unitariedad,
  no conservación a t=1/2 y relación de fase/gap cuando t→0.
  Esta familia no es un límite IR espacial ni un nuevo candidato.
- Bandas: laplaciano `2 sum_j(1-cos k_j) I_2`; control firmado
  `sin(k) sigma_z`. Verificar órdenes y signo exactamente.

PASS de controles significa que se verifican las identidades del preflight,
no que una receta genera gravedad. Un error obliga a reparar y registrar el
motivo, sin sustituir ejemplos para obtener PASS.

## 5. Salidas y siguiente frontera

- `STATE_FIRST_PREFLIGHT_COMPLETE_AUTHOR_SIDE`: filtros derivados y controles
  consistentes; no certifica una arquitectura.
- `STATE_FIRST_CONSTRUCTION_OPEN / NO_NEW_RULE_SPECIFIED`: falta un par
  `(K,U)` y un estado accesible que cumplan §2.
- Una contradicción dentro de una receta se declara con sus hipótesis, sin
  promoverla a no-go general de QCA.

El siguiente expediente deberá especificar **un solo** par `(K,U)` con celda,
sector, localidad, inversa, simetrías y receta de vacío antes de sus pruebas.
Primera prueba: conservación exacta y acceso controlado al estado; después
el puente energía–tick. Si falta especificación se cierra como tal, sin
volver al promedio B ni iniciar un catálogo de circuitos.
La prioridad sigue siendo un sector tensorial colectivo; un control escalar
o fermión libre aislado no satisface el objetivo. No se añade materia ni se
invoca el bootstrap gravitatorio antes de R1/R3/R4.

No hay autorización de revisión externa, claim de novedad o promoción a
gravedad. Los cálculos auxiliares y las derivaciones son evidencia del autor.
