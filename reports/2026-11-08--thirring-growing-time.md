# Thirring con salida libre exacta: puerta microscópica y tiempos crecientes abiertos

2026-11-08. Autor Codex/OpenAI. **PRELIMINARY: derivaciones y comprobaciones
de autor, sin revisión independiente ni promoción.** Usuario «adelante» a
estudiar acumulación de interacción con T(M) y salida libre exacta.

Contrato [THIRRING_GROWING_TIME_FREE_OUTPUT_GATE.md](../theory/THIRRING_GROWING_TIME_FREE_OUTPUT_GATE.md),
congelado en `61a180a`; código versionado antes de ejecutar en `7903d2b`;
corrección numérica de un control y repetición en `faa9347`.

## Resultado

1. **Resultado positivo exacto de alcance microscópico:** para M=1, T=1 y
   salida libre exacta, el código admite D_chi=diag(1,e^{i chi},e^{i chi},1)
   sin fuga. En chi=pi/2, D_chi entrelaza máximamente la entrada lógica ++.
   Vale para cualquier mu admisible: F transporta el código de salida y no
   cambia la matriz lógica de J. No se ha demostrado composición de esa
   puerta con las demás operaciones del autómata.
2. **Resultado negativo asintótico probado con la cota disponible:** si
   M->infinito y T(M)=o(M^(1/4)), la evolución real se aproxima a la libre
   uniformemente sobre las cuatro entradas. No hay puerta entrelazante de
   efecto finito en ese régimen. Es un cierre de escalas lentas, no de todas
   las escalas crecientes.
3. **Escalas lineal y cuadrática:** calculadas en M=1,2,4,8,16. No se obtiene
   una estimación de fuga y error tendiendo a cero ni una unitaria límite.
   Las muestras tienen fuga apreciable y no autorizan una puerta asintótica.
   Tampoco demuestran imposibilidad para M mayores u otras T(M).

Veredicto: `EXACT_MICROSCOPIC_ONE_STEP_ENTANGLER_AT_M1 /
SUBQUARTER_POWER_TIME_ROUTE_CLOSED /
LINEAR_QUADRATIC_LIMIT_NOT_ESTABLISHED /
GENERAL_GROWING_TIME_ROUTE_OPEN`.

La decisión de corte del contrato se cumple: se completa la lista congelada
sin ampliar el barrido ni reclamar una puerta de tiempos crecientes. El
hallazgo M=1 es un resultado distinto, sin límite de envolvente lenta o
interpretación de procesador relativista universal establecida.

## 1. Regla, código y salida

Se mantiene exactamente U=FJ, mu=3/5,nu=4/5,chi=pi/2, dos modos fermiónicos
por sitio, y el código inicial B=B_+ wedge B_- del preflight `cbfae56`:
f_M=M^(-1/2) sum_{j=0}^{M-1}|2j>, g_M=T f_M,
B_+=(R f_M,L g_M), B_-=(R g_M,L f_M). Cada etiqueta ocupa un sector
opuesto de Gamma=sigma_z Pi; el estado físico de dos fermiones tiene Q=0.

Ahora B_T=F^T B, con la misma ordenación de creación A,B. Son cuatro
estados ortonormales para todo T. Cada modo de una partícula sigue su
evolución libre exacta, incluidas mezcla y dispersión. Definir este marco
de lectura no implementa una inversión F^{-T} ni agrega un control.
Tampoco reetiqueta el estado interactuante como código: la salida se
construye exclusivamente con F, sin usar U ni la puerta que se busca.

La matriz lógica es

\[
 K_{M,T}=B_T^\dagger U^T B
 =B^\dagger F^{-T}U^T B.
\]

El proyector de salida P_T=B_T B_T† ya no tiene el soporte espacial fijo
del preflight. Por eso el argumento previo de trayectoria extrema fuera
de ese soporte no prueba fuga en este nuevo marco.

## 2. Qué significa una puerta sobre todas las entradas

Sean sigma_j los valores singulares de K. Como U^T B y B_T son isometrías,

\[
 p_{\rm fuga,max}=\|(I-P_T)U^T B\|^2
 =\|I-K^\dagger K\|=1-\sigma_{\min}^2.
\]

Es el máximo sobre todo el código, incluidas entradas entrelazadas. Si
K=L diag(sigma) R† es una SVD, su polar unitaria Q=L R† es única cuando
sigma_min>0. El error de la evolución completa respecto de esa candidata es

\[
 \epsilon_Q^2=\|U^T B-B_TQ\|^2
 =\|2I-Q^\dagger K-K^\dagger Q\|
 =2(1-\sigma_{\min}).
\]

Para declarar una puerta límite V, además se necesita Q->V (permitiendo
fase global), con V entrelazante. Entonces
||U^T B-B_T V||<=epsilon_Q+||Q-V||. Un Q entrelazante con p_fuga grande
no es una puerta física de baja fuga: no se aplica la polar como control
ni se postseleccionan los estados retenidos.

Se registran las 16 concurrencias de Q sobre productos de 0,1,+,+i. Un
valor positivo es un testigo de entrelazamiento de Q, no una maximización
ni una prueba de implementación física o convergencia asintótica. Los
valores singulares y matrices K,Q completos están en el JSON.

## 3. Reducción exacta y comprobación independiente de representación

En un sector Gamma=s, el modo de una partícula en x tiene componente
sigma_z=s(-1)^x. Una traslación de esa componente manda x a
x+s(-1)^x, y la masa deja x fijo cambiando la componente. Ambas operaciones
invierten Gamma. En coordenadas de posición,

\[
 P_s|x\rangle=|x+s(-1)^x\rangle,\quad P_s^2=I,\quad
 w_s=\nu P_s-i\mu I.
\]

P_s intercambia pares adyacentes y es autoadjunto; w_s es unitario.
En el paso t, A tiene Gamma=(-1)^t y B tiene el signo contrario.
Su amplitud ordenada psi(x,y) evoluciona por

\[
 \psi_{t+1}=w_s\big(e^{i\chi\delta_{x,y}}\psi_t\big)w_{-s}^{\mathsf T}.
\]

En coincidencia, las componentes son necesariamente opuestas: el contacto
es exactamente delta_xy. La transpuesta aparece porque psi es una matriz
de amplitudes de ket, no una matriz de densidad.

La incrustación en Fock es la isometría normalizada del producto exterior
entre los dos autoespacios ortogonales de Gamma, probada en la sección 5
del informe previo. Así se conserva exactamente la estadística fermiónica
en este sector: no se la sustituye por partículas distinguibles sin
justificación. Para M=1,2 y todos los checkpoints T<=4 se implementó además
W tensor W en las amplitudes antisimétricas completas con espín explícito.
El máximo residuo de comparación de representaciones observado fue
5.26e-16 (redondeado por exceso del máximo observado).

La interacción es la de `1711.03920v1.pdf` pp.1–2, Ecs.(1)–(2), con
orientación R/L declarada en el preflight; se releyó `1804.08508v1.pdf`
p.3 y pp.5–6, donde se define W y el subespacio libre/interactuante.
La reducción y las fórmulas de error aquí son derivaciones del autor.

## 4. Una puerta exacta microscópica que el marco fijo ocultaba

Para M=1: f=|0>,g=|1>. Los estados 01 y 10 tienen dos componentes
opuestas en un mismo sitio; 00 y 11 tienen posiciones distintas. Por eso

\[
 JB=BD_\chi,\quad
 D_\chi=\operatorname{diag}(1,e^{i\chi},e^{i\chi},1)
 =e^{i\chi/2}\exp(-i\chi Z\otimes Z/2).
\]

Por la regla fija U=FJ, se sigue exactamente

\[
 UB=FB D_\chi=B_1 D_\chi.
\]

No hay fuga ni aproximación de masa en ese paso. Sobre ++, la concurrencia
es |sin chi|, por lo que en chi=pi/2 es uno. Esta prueba algebraica contrasta
con ambas representaciones numéricas; no depende de redondear un singular.

El preflight anterior obtenía fuga al comparar con un código alternante de
soporte fijo. No hay contradicción: FB ya incluye los modos que antes se
contaban como fuga. Tampoco es una puerta universal: tras ese paso los
modos han cambiado, y no se ha demostrado que la siguiente aplicación de
J mantenga el nuevo código o produzca la misma D_chi. Los ejemplos
numéricos de concurrencia no resuelven esa composición.

El código M=1 ocupa dos sitios y combina escala reticular/nodos. La puerta
es microscópica: no es un límite de paquetes anchos ni una construcción de
computación universal en un sector relativista de baja energía.

## 5. Régimen de tiempos excluido por la cota analítica

La cota del informe previo, con su justificación de sectores ortogonales,
vale para cualquier entero T y conserva su significado al usar salida
libre exacta, porque mide directamente la diferencia U^T-F^T:

\[
 \|(U^T-F^T)B\|
 \leq d_\chi\left(\frac{T}{\sqrt M}
 +\nu\sqrt{\frac2M}T(T-1)\right),
 \quad d_\chi=|e^{i\chi}-1|.
\]

Si T(M)=o(M^(1/4)), ambos términos tienden a cero. En consecuencia,
K->I, p_fuga->0, y cualquier puerta de efecto entrelazante finito queda
excluida en ese régimen. La demostración es uniforme sobre todas las
entradas y no usa las muestras como evidencia del límite.

Esta es una condición suficiente para que la interacción desaparezca;
no es una estimación óptima del tiempo necesario. Que la cota deje de
tender a cero en T=M o M² no demuestra una puerta ni una imposibilidad:
en esas escalas la cota puede ser mayor que la cota trivial 2 y ser inútil.

## 6. Tiempos lineales y cuadráticos: resultados finitos

| M | T=M: fuga máxima | T=M: error epsilon_Q | T=M²: fuga máxima | T=M²: error epsilon_Q |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | 0 (exacto) | 0 | 0 (exacto) |
| 2 | 0.670307 | 0.922833 | 0.972901 | 1.292581 |
| 4 | 0.886061 | 1.151044 | 0.918253 | 1.195061 |
| 8 | 0.859201 | 1.117827 | 0.983778 | 1.321087 |
| 16 | 0.318999 | 0.591222 | 0.964616 | 1.274278 |

Redondeo ordinario a seis decimales, sin convertir estos números en cotas
certificadas de error flotante. La fuga se obtuvo tanto por singular mínimo
como por el residuo completo fuera del código. La epsilon_Q se calculó
directamente como norma del error de isometrías.

La serie lineal no es monótona. La cuadrática tiene fuga alta en estas
muestras. Ninguna de esas observaciones demuestra su límite. La polar
puede presentar concurrencia positiva mientras la fuga es grande; por
ejemplo en M=16,T=256 el mayor testigo entre los 16 productos vale
aproximadamente 0.271, con fuga 0.965 y epsilon_Q=1.274. Ese Q no se
declara una puerta implementada con error pequeño.

Los cambios de Q entre tamaños consecutivos, alineados en fase, también
están registrados. Una reducción de esas diferencias en los últimos dos
tamaños no es un certificado de Cauchy ni identifica una unitaria límite.

## 7. Ejecución, procedencia y reparación numérica

[Código permanente](../scripts/evaluate_thirring_growing_time.py),
[JSON con matrices](2026-11-08--thirring-growing-time.json),
[registro completo](2026-11-08--thirring-growing-time.txt).
Python 3.12.3, NumPy 2.4.4, sin semilla porque no hay aleatoriedad.
Parámetros, perfiles, tiempos y estados testigo se congelaron antes de ejecutar.

**123/123 controles** tras reparación: consistencia, gramianos, representación
completa frente a reducida, fuga, polar y cotas. No son 123 pruebas
independientes del resultado asintótico. Mayor residuo de conservación del
gramiano de las entradas observado: 4.50e-14 (redondeado por exceso).

La longitud L=2M+2T_max+12 y el origen par se eligen con margen de al menos
cuatro sitios fuera del cono causal de todas las entradas. Se comprueba
amplitud cero en las franjas de frontera. El anillo implementa por tanto
exactamente, salvo coma flotante, la evolución de la recta en estos tiempos:
no se extrapola una simulación con retornos por frontera periódica.

Primer intento: 122/123. Falló el test de epsilon_Q=sqrt(2(1-sigma_min))
en la representación completa M=1,T=1: un sigma_min=1+O(eps) indujo un
error de aproximadamente 2.1e-8 al tomar la raíz, aunque el mapa es
exactamente unitario por álgebra. Se conservan [datos originales](2026-11-08--thirring-growing-time-first-failed.json)
y [registro original](2026-11-08--thirring-growing-time-first-failed.txt).
Se rederivó y contrastó la identidad equivalente de **errores al cuadrado**,
estable cerca de sigma_min=1. No cambió el propagador físico. La raíz
formal guardada como polar_error_formula puede amplificar redondeos cerca
de uno: se usa el error directo, y el test estable usa su cuadrado.

Los hashes del script, contrato y originales primarios están en el JSON.
No se enviaron nuevos documentos a modelos externos ni se reclamó novedad.

## 8. Punto de parada y límites de la respuesta

Se completó la búsqueda acotada acordada: marco de salida definido,
restricción asintótica derivada y dos escalas evaluadas sin selección por
éxito. No se ha obtenido una escala creciente con puerta entrelazante
uniformemente controlada. La cuestión general sigue OPEN, sin convertir
el resultado finito en un cierre de todas las T(M).

La puerta exacta microscópica M=1 merece distinguirse del objetivo original:
es un recurso de un paso, no una prueba de composición, de universalidad
ni de emergencia relativista interactuante. Ninguna frecuencia absoluta
de reloj ni valor de c se deduce de este experimento.
