# B0 — cierre del intento acotado por falta de control

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato/código previos en `04f0207ebb56408aa66b6b5d6ab0cf0959b34842`:
[contrato](../theory/INVERSE_GRAVITY_B0_ACCESS_GATE.md),
[script](../scripts/verify_inverse_gravity_b0_error_control.py).
Se conserva el [contrato A/B](../theory/INVERSE_GRAVITY_IR_OPTIONS_AB.md):
misma semilla Gibbs β=1, tick, q, θ, constraints y batería.

## 1. Resultado del expediente

`B0 = METHOD_NOT_CLOSED`.
`B = OPEN_BY_CONTROL_LIMITATION`.
`B1/B2/B3 = NOT_EXECUTED`.
`IR_SELECTION_OPEN_AFTER_AB`.

Es cierre del intento acotado de acceso, no fallo físico del estado B.
No se calculó su respuesta ni se demostró que B sea localmente tracial.
La existencia y estacionariedad de su promedio en volumen finito siguen válidas.

## 2. Vía de acceso examinada

La identidad dual de A0/B0 evita la matriz global de U:

`Tr(ρ_M A)=Tr(σ_B,L M^-1 sum_n U^-n A U^n)`.

El soporte requerido crece hasta radio 3(M-1), por el alcance del tick.
La semilla es el Gibbs restringido de un Hamiltoniano local no conmutante.
Las puertas R/T no comparten base y H_A no es conservado por U, probado
en A0. El Gibbs de la región aislada no es la densidad reducida de la semilla
global por una identidad general; faltan cotas de frontera/contracción.

Una expansión de Taylor de exp(-H_A) podría dar aproximaciones certificadas
en volumen finito usando ||H_A||≤6L³, pero no resuelve el acceso local sin
objetos de tamaño exponencial ni aporta un error uniforme útil por esa sola
cota extensiva. No se ejecuta como si fuera un método escalable.
No se afirmó que toda expansión local sea imposible; queda sin establecer
un control aplicable a β=1 y las constraints fijadas.

El filtro de fases del informe A0/B0 requiere separación no nula de
quasifases o un sustituto específico de los observables. No se dispone de
esa información para el tick. Una diagonalización del control qutrit o un
toro con otra celda no la suministra.

## 3. La cota de estacionariedad no cierra el promedio

Se ejecutó `python3 -B scripts/verify_inverse_gravity_b0_error_control.py`,
SymPy 1.14.0, código 0, aritmética exacta. Salida íntegra en
[certificado](2026-10-08--inverse-gravity-b0-error-certificate.txt).
Los cuatro controles prefijados pasan. No simulan el tick ni la semilla B.

Prueba general independiente de esos casos: en dos niveles fijar
V_N=diag(1,z_N), z_N=(N²+i)/(N²-i), y semilla |+><+|. La fase no nula
δ_N=2 arctan(1/N²) cumple δ_N≤2/N². El promedio de N pasos conserva
off-diagonal f_N/2, con f_N=N^-1 sum_j exp(i jδ_N). El ensemble infinito
es I/2 y su distancia traza al promedio es |f_N|.

Como jδ_N≤2/N y cos(t)≥1-t²/2,

`|f_N|≥Re(f_N)≥1-2/N²≥1/2`, para N≥2.

El defecto de estacionariedad es |z_N-1||f_N|≤2/N² y tiende a cero,
mientras la distancia al ensemble no lo hace. En esta familia el operador
cambia con N: no prueba falta de convergencia para nuestro U fijo.
Sí demuestra que no hay una inferencia uniforme de proximidad al ensemble
desde un defecto pequeño sin información dinámica adicional.

El control exacto calcula los cuadrados de esas dos normas para N=2,4,8,16.
La prueba anterior muestra por qué no es un accidente de cuatro muestras.
No se confundió el defecto 2/M con el error de respuesta de B.

## 4. Balance A/B sin cambiar el objetivo

| Ruta | Evidencia actual | Interpretación |
|---|---|---|
| A | Testigo físico de cambio de energía exacto | Rechazada la receta de Gibbs conservado fijada |
| B | Estado formal estacionario; acceso local dual exacto | Sigue abierta; faltan control de semilla y convergencia local del promedio |
| Tick de control | Influencia física de un paso exacta | No garantiza vacío, gap, modos ni gravedad |

Estos resultados no demuestran ausencia de gravedad en QCA. El circuito
actual no proporciona aún una referencia IR controlada para el programa.
No se ha obtenido una respuesta B «aproximada» que luego se conserve sin
provenance o sin error. No se introducen baño, nuevo β, ángulo pequeño,
otro seed, pesos modificados o una ruta C como rescate de B.

## 5. Punto de retorno al diseño inverso

Se cumple la regla de cierre acotado del contrato A/B. El primer requisito
pendiente sigue siendo R1: un mecanismo de selección de estado/sector y
control IR propio de la arquitectura, previo al espectro.

Continuar requeriría un método concreto con control de expectativas Gibbs
locales y de convergencia para esta B, o un charter distinto de arquitectura
que justifique el estado antes de elegir puertas. No basta ejecutar más ticks
o matrices pequeñas. Este informe no abre esa nueva arquitectura ni la
promociona; registra dónde termina la prueba autorizada de A/B.

Evidencia propia, sin revisión independiente. Einstein, dos polarizaciones,
z=1, fuente universal y NOVELTY permanecen OPEN.
