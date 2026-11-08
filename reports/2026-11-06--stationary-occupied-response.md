# Estado ocupado estacionario y respuesta a primer orden

2026-11-06. PRELIMINARY, derivación de autor, sin revisión independiente.
Contrato: theory/STATIONARY_OCCUPIED_RESPONSE_GATE.md, escrito antes
del cálculo. No se afirma novedad ni igualación de velocidades.

## Estado y prueba de estacionariedad

En un volumen periódico finito de la red BCC, con cuatro modos de cada
especie por celda, fijamos
rho=Z^-1 exp(-lambda_1 N1_total-lambda_2 N2_total).
Cada modo tiene ocupación p_a=1/(1+exp(lambda_a)), 0<p_a<1.
El modelo es U_chi=V_chi U_0 del contrato interactuante anterior.

U_0 y V_chi conservan por separado ambos números totales. Por tanto
[rho,U_chi]=0 exactamente para cualquier chi. Es un estado ocupado
mixto de temperatura infinita con fugacidades, no un estado de baja
energía ni un vacío relativista.

Segunda vía: en cada sector (N1_total,N2_total), rho es múltiplo de la
identidad; la evolución solo mezcla estados con el mismo peso. La
estacionariedad no depende de que la colisión conserve un estado de
Slater puro particular. El límite termodinámico se define por sus
expectaciones locales de producto.

## Observable y cálculo

Definimos G^R_ab(x,t)=-i theta(t) Tr rho {c_a(x,t),c_b†(0)},
con t entero y c(t)=U_chi^-t c U_chi^t. A chi=0 la respuesta reproduce
los propagadores libres y sus dos pendientes distintas. Para concretar
el control libre pueden emplearse dos copias de la familia s=4 del repo,
a_1=1/3 y a_2=2/3, theta=pi/4: las pendientes documentadas son
a_a/sqrt3; no se ajustan para obtener igualdad.

La identidad local exacta es

    V_chi† c_1(x) V_chi = exp(-i chi N_2(x)) c_1(x),

y análogamente intercambiando especies. Se comprueba porque aniquilar
una partícula de especie 1 reduce N1 N2 en N2. En un paso, la expansión
es c_1-i chi N_2 c_1+O(chi²).

En la expansión de t pasos a primer orden, cada inserción contiene
exactamente una densidad libre de la otra especie. El estado factoriza
entre especies y es estacionario bajo U_0, de modo que la traza de esa
densidad es siempre 4p_2. La parte restante es el mismo propagador libre
por composición de las evoluciones antes y después de la inserción.
Las t posiciones posibles de la inserción dan, a tiempo fijo,

    G^R_11(k,t;chi) = (1-i chi 4p_2 t) G^R_11(k,t;0)+O_t(chi²),
    G^R_22(k,t;chi) = (1-i chi 4p_1 t) G^R_22(k,t;0)+O_t(chi²).

Los términos cruzados de una partícula entre especies se anulan por
conservación de sus cargas. El resultado de primer orden corresponde
al desplazamiento Hartree escalar de fase 4chi p_other, sin dependencia
de k. Su derivada espacial es cero: no hay corrección de pendiente a
orden chi en esta expansión. No hay Fock entre especies distinguibles
sin coherencia entre ellas en este estado.

La segunda lectura del mismo resultado es la contracción de una única
inserción N_other c_a: el único valor del otro sector que entra es su
densidad media homogénea. No es una aproximación de campo medio a todos
los órdenes; solo calcula el coeficiente lineal exacto a tiempo fijo.

## Límite del resultado y siguiente obligación

El resto O_t(chi²) no es uniforme en t. No se extrae una prueba de polos
estables a tiempo infinito de esta expansión secular. La denominación
«desplazamiento Hartree» identifica el término perturbativo; no demuestra
una quasipartícula exacta del sistema interactuante.

La varianza local de la otra especie es 4p_other(1-p_other), no nula.
Por ello no puede reemplazarse N_other por su media para concluir que
la evolución completa es libre. A orden dos se requieren correlaciones
de densidad a tiempos distintos y el control de la anchura espectral.

Resultado: STATIONARY_OCCUPIED_STATE_FIXED / FIRST_ORDER_PHASE_ONLY.
Queda una terna consistente de modelo, estado y respuesta, pero este
estado no establece el puente al RG relativista de baja energía. Antes
de afirmar selección se debe comprobar si sobrevive una excitación
coherente y si su diferencia de pendientes disminuye en el régimen
controlado. El cálculo a orden dos queda pendiente; no se declara
irrelevancia RG ni un mecanismo realizado.

Control auxiliar permanente: scripts/verify_stationary_occupied_response.py.
Comprueba normalización, media, varianza y diferencias de energía de
colisión en los 256 estados locales. El argumento de estacionariedad
y el coeficiente a tiempo fijo están derivados arriba; el control local
no sustituye una prueba global ni una revisión independiente.
Registro: 2026-11-06--stationary-occupied-response-verifier.txt.
