# SCALED_IR_SIGNALING_GATE

**Fecha:** 2026-09-17. **Estado al congelar:** contrato fijado antes de
cualquier cálculo; `NOT_EXECUTED / OUTCOME_OPEN`. El estado posterior se
registra sólo en `state/CURRENT_STATE.md`; este encabezado no se actualiza.

**Autorización:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` (2026-09-17). Cubre:

- congelar este contrato;
- sustituir el gate de existencia con `Delta T` fijo por esta formulación de
  escalado;
- investigar la tasa direccional `I(v)`, sólo como obligación de prueba
  dentro del gate. Esto levanta, únicamente aquí, el `NOT_AUTHORIZED` de
  `CURRENT_STATE` §8.8.

**Ratificado por el usuario el 2026-09-17**, con dos precisiones incorporadas:
las regiones son bolas euclídeas (§3), y las familias de encoders y detectores
son **familias internas congeladas, no exhaustivas** (§4).

Sucesor de `NARROW_BAND_SIGNALING_GATE` (`CURRENT_STATE` §8.16), sin
reabrirlo. Aquel resultado, `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS /
INDEPENDENTLY_REVIEWED`, conserva sus bytes y su alcance.

## 1. Pregunta única

Con recurso, encoder y detector IR-admisibles, regiones de Alice y Bob de
tamaño `O(1/Lambda)` separadas por un margen `O(1/Lambda)` fuera del cono
emergente de **toda** la región de Alice, y tiempo `O(1/Lambda)`: ¿la
distinguibilidad de Bob decae polinómicamente, es no perturbativamente
pequeña, es exactamente nula o queda indeterminada?

Se estudia la **ley de desaparición** cuando `Lambda -> 0`; no se exige un
límite positivo. Una señal a `Delta T` fijo, o con un margen de `O(1)` sitios,
no responde a esta pregunta, porque no es resoluble a la escala IR `~ 1/Lambda`.

## 2. Modelo y convenciones heredadas

Sin cambios respecto de `NARROW_BAND_SIGNALING_GATE.md` §2:

- CAR libre de CJWW (5.15), en el sector de una partícula, con dos modos
  internos por sitio;
- `S = W^dagger` para estados y `K_t(x,z) = (W^t)_{x,z}`;
- convención de Fourier `hat psi(p) = sum_x e^{i p.x} psi(x)`, con
  `dmu = d^3p/(2pi)^3` sobre `B = [-pi,pi)^3`;
- nodo `p = 0`, `H_W = p1 sigma1 - p2 sigma2 + p3 sigma3` y `c_IR = 1`;
- `C_micro = [-1,1]^3`;
- ambas ramas conservadas, sin ningún nuevo acoplamiento dinámico.

Hechos previos del repo que se usan tal cual:

- `sup|grad omega| = c_IR = 1`, exacto (`CURRENT_STATE` §8.4);
- rayos de vértice no nulos para todo `n`, exacto (§8.5);
- la LDP radial de CJWW (§8.8), que es una cota superior radial y sólo motiva:
  no se usa como premisa.

## 3. Parametrización escalada (congelada)

Parámetro único `N ∈ Z`, con `N >= N_0 = 2`, y

\[
\Delta T=N,\qquad \Lambda_N=N^{-1},\qquad \Lambda'_N=N^{-1/2},
\qquad\text{de modo que}\quad \Lambda_N\ll\Lambda'_N\ll1 .
\]

Equivale a `tau_0 = 1` y `alpha = 1/2`. `N` es entero por construcción, así
que no hay redondeos retrospectivos. Para `N >= 2`, `Lambda_N` y `Lambda'_N`
son menores que `pi/4`, dentro de la carta del charter anterior (§3), que se
re-certificará.

**Regiones.** Son bolas **euclídeas** (norma `l2`) intersecadas con `Z^3`:

\[
A_N=\{x\in\mathbb Z^3:\ |x|_2\le N/4\},\qquad
B_N=\{y\in\mathbb Z^3:\ |y-(N,N,N)|_2\le N/4\}.
\]

En unidades de `1/Lambda_N`: `ell_A = ell_B = 1/4`, separación de centros
`r_0 = sqrt(3)`, margen `mu = 1/5`. Todas las distancias de este contrato son
euclídeas.

**Admisibilidad causal**, sobre regiones completas y nunca sobre centros:

\[
\operatorname{dist}_2(A_N,B_N)-c_{\rm IR}N\ \ge\ \mu N=\frac{N}{5}.
\]

Para las bolas continuas, `dist = sqrt(3) N - N/2`. Los conjuntos de red sólo
pueden estar más separados, así que el exceso sobre el cono emergente es al
menos `(sqrt3 - 3/2) N ≈ 0.232 N > N/5`. Se re-certificará de forma exacta.

Se exige además un par `(x,y) ∈ A_N x B_N` con `K_N(y,x) != 0`, para que la
clase no sea trivialmente nula. El candidato declarado es `x = 0`,
`y = (N,N,N)`, un rayo de vértice; su no nulidad se re-certificará con la
convención de desplazamiento de §2.

## 4. Recurso, encoder, detector y protocolo

**Recurso.** Centrado en el origen, con espín `down`:

\[
\widehat\phi_N(p)=Z_N^{-1/2}\,g(p/\Lambda_N)\binom01,
\qquad g(q)=(1-|q|^2)^2_+ .
\]

No hay pasos comunes: el recurso en la elección es `phi_N`. Se asume
disponible; no es una preparación local certificada.

**Encoder de Alice** (en `T = 0`, soportado en `A_N`). Con
`F_A(x) = (1 - 16|x|^2/N^2)^2_+`, `theta = pi/2` y `M ∈ {I, sigma1, sigma2, sigma3}`:

\[
U^{(1)}_M=\exp\!\Big(i\theta\sum_x F_A(x)\,c_x^\dagger M c_x\Big),\qquad U^{(0)}=I .
\]

Es par, conserva el número y es local en `A_N`. En el sector de una
partícula es la multiplicación por `exp(i theta F_A(x) M)`.

`{I, sigma1, sigma2, sigma3}` es la **familia interna congelada**: una base
interna fija. Se evalúan y reportan todos sus miembros con la misma
disciplina, sin selección. **No es exhaustiva.** Un generador general
`M = aI + b·sigma` no queda cubierto, porque no se ha certificado ninguna
simetría del walk que haga equivalentes todas las direcciones
`n̂·sigma`. Extender el resultado a `M` arbitrario requiere un teorema aparte,
que no se presupone.

- `M = I` es `REFERENCE_CONTROL` (generador de carga), no un control negativo:
  su nulidad no está demostrada y no se presume. Por sí solo no puede
  establecer un estado positivo.
- Hecho algebraico declarado: con el recurso en `down`, `sigma3` actúa en el
  instante de la elección como una fase de densidad; sólo `sigma1` y `sigma2`
  mezclan grados internos. Se reporta y no altera la familia.

**Detector de Bob** (en `T = N`, soportado en `B_N`). Con
`h_B(y) = (1 - 16|y-(N,N,N)|^2/N^2)^2_+` y
`M_B ∈ {I, (I+sigma1)/2, (I+sigma2)/2, (I+sigma3)/2}`:

\[
E_{B}=I-\Gamma\big(I-h_B\otimes M_B\big),\qquad 0\le E_B\le I ,
\]

donde `Gamma` es la segunda cuantización de una contracción. `E_B` es par y
local en `B_N`; en el sector de una partícula coincide con `h_B (x) M_B`.
También es una **familia congelada**, no exhaustiva.

**Protocolo.** El bit es exógeno e independiente del recurso, y

\[
\psi_b(N)=S^N U^{(b)}\phi_N .
\]

Las historias previas a la elección son idénticas por construcción. No se
admiten ancillas, postselección ni filtros que dependan del bit.

## 5. Cantidades y admisibilidad IR

**Señal física primaria** para cada par `(M, M_B)`, calculada sin ninguna
proyección:

\[
\delta_{M,M_B}(N)=\big|\langle\psi_1(N)|h_B\!\otimes\! M_B|\psi_1(N)\rangle-\langle\psi_0(N)|h_B\!\otimes\! M_B|\psi_0(N)\rangle\big|
=\big|\operatorname{Tr}E_B(\rho^{(1)}-\rho^{(0)})\big| .
\]

`D_B(N)` es la distancia de traza entre los estados reducidos del Fock
completo a los modos de `B_N`. Se cumple `D_B >= delta`.

**Presupuesto IR de las operaciones**, con `Pi' = Pi_{Lambda'_N}` y
`Pi = Pi_{Lambda_N}`:

\[
\eta_{\rm enc,op}^{M}(N)=\frac{\|(I-\Pi')(U_M-I)\,\Pi\|}{\|(U_M-I)\,\Pi\|},
\qquad
\eta_{\rm read}^{M_B}(N)=\frac{\|(I-\Pi')(h_B\otimes M_B)\,\Pi\|}{\|(h_B\otimes M_B)\,\Pi\|},
\]

y, por continuidad con el criterio de §8.16, con `Delta_M = U_M rho U_M^† - rho`
y `rho = |phi_N><phi_N|`:

\[
\eta_{\rm enc}^{M}(N)=\frac{\|\Delta_M-\Pi'\Delta_M\Pi'\|_1}{\|\Delta_M\|_1}.
\]

Rige la convención `Delta = 0` de §7 del charter anterior. Un denominador
nulo se clasifica aparte y nunca cuenta como cumplimiento.

**Encoder IR-admisible:** se demuestran, con cotas explícitas,
`eta_enc,op^M(N) -> 0` y `eta_enc^M(N) -> 0`.
**Detector IR-admisible:** `eta_read^{M_B}(N) -> 0`.

**Sanity check obligatorio.** Con los mismos `Pi'` y `Pi`, la puerta puntual
congelada `I - 2P_0` debe seguir dando `eta_enc,op -> 1` y `eta_enc -> 1`, y
un detector puntual `P_y` debe dar `eta_read -> 1`. Así se comprueba que
ensanchar el proyector no ha "curado" artificialmente el negativo de §8.16.
Si falla, el criterio es incoherente y el gate queda `OPEN` por
inconsistencia de convenciones.

**Separación vinculante.** La admisibilidad IR es una propiedad de las
operaciones (recurso, encoder, detector). La señal `delta` se evalúa sin
proyección artificial. No se afirmará que una señal exponencialmente pequeña
"la transporta el sector IR": partirla con proyectores espectrales introduce
una no localidad artificial que puede ser mucho mayor que la propia señal.

## 6. Obligaciones de prueba, en orden vinculante

**Paso 0 — geometría y carta.** Re-certificar los conjuntos euclídeos, el
margen, el par de vértice no nulo, la carta para `N >= 2` y la normalización
`Z_N`.

**Paso 1 — admisibilidad IR.** Cotas explícitas de `eta_enc,op^M` y `eta_enc^M`
para las cuatro `M`, de `eta_read^{M_B}` para los cuatro detectores, y del
sanity check puntual.

*Stop rule:* si se demuestra que ninguna `M ∈ {sigma1, sigma2, sigma3}` es un
encoder IR-admisible, cerrar con `NO_IR_ADMISSIBLE_ENCODER_IN_FROZEN_FAMILY`
sin evaluar la señal. Una cota demasiado débil deja el caso `OPEN`.

**Paso 2 — cota superior geométrica.** Demostrar, con constantes explícitas,

\[
D_B(N)\le C\,N^{q}\,e^{-J\,N},\qquad J>0,
\]

para toda operación unitaria soportada en `A_N`, todo estado inicial y todo
efecto en `B_N`; por ejemplo, a partir de `||P_{B_N} S^N P_{A_N}||`. La tasa
`J`, o la forma direccional de `I(v)` sobre el conjunto de velocidades
`(B_N - A_N)/N`, **debe derivarse aquí; no puede asumirse**. Técnicas
autorizadas:

- desplazamiento del contorno a momentos complejos (el símbolo es un
  polinomio trigonométrico);
- análisis del símbolo y control uniforme de potencias de matrices `2x2`;
- derivación de una tasa direccional;
- reutilización de la LDP radial de §8.8 sólo donde realmente aplique.

Un resultado sólo para algunas direcciones se registra como tal.

**Paso 3 — cotas inferiores.** Para los doce pares con
`M ∈ {sigma1, sigma2, sigma3}` y los cuatro de `REFERENCE_CONTROL`, buscar:

- una cota inferior explícita, `delta(N) >= c N^{-p}` o
  `delta(N) >= c N^{-p} e^{-C_1 N}`, válida para todo `N >= N_*`; o
- una asintótica demostrada `delta(N) = A(N) e^{-C N}(1 + o(1))` con
  `A(N) != 0` controlado.

Se reportan los dieciséis pares, sin selección.

**Paso 4 — clasificación** según §7.

Se priorizan identidades, integrales analíticas y restos acotados. Una
evaluación numérica en `N` concretos sólo puede figurar como diagnóstico
`SUPPORTED` con error certificado. Nunca establece un estado terminal ni una
ley asintótica, ni autoriza a cambiar parámetros después de verla.

## 7. Estados terminales (orden de asignación, sin solapamientos)

| Estado | Condición |
| --- | --- |
| `NO_IR_ADMISSIBLE_ENCODER_IN_FROZEN_FAMILY` | Se demuestra que ninguna `M ∈ {sigma1, sigma2, sigma3}` es un encoder IR-admisible (§5). |
| `NO_SIGNALING_IN_SCALED_IR_CLASS` | Se demuestra `D_B(N) = 0` para todo `N >= N_*` y toda `M` de la familia congelada, `REFERENCE_CONTROL` incluido. Tiene que ser una obstrucción exacta, no una cota. |
| `IR_RESOLVABLE_SIGNALING_POLYNOMIAL` | Hay un par admisible con `M ∈ {sigma1, sigma2, sigma3}` y cota inferior polinómica demostrada. |
| `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` | Hay un par admisible con `M ∈ {sigma1, sigma2, sigma3}` con cota inferior `c N^{-p} e^{-C_1 N}` o asintótica de amplitud no nula, **y** cota superior `C N^q e^{-C_2 N}` para ese par. |
| `OPEN_AFTER_SCALED_IR_ANALYSIS` | Cualquier otro caso: sólo cota superior; cotas inferiores ausentes o insuficientes; tasa sin demostrar; admisibilidad sin demostrar; inconsistencia de convenciones. |

**Regla explícita.** Si sólo se obtiene `0 <= delta(N) <= C N^q e^{-J N}` sin
decidir si `delta` es exactamente cero, el estado es
`OPEN_AFTER_SCALED_IR_ANALYSIS`. Una cota superior sola, con `J > 0`,
**excluye** `IR_RESOLVABLE_SIGNALING_POLYNOMIAL`, pero **no autoriza**
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. Que se vaya a obtener no se
presume.

Se registran por separado aunque el estado sea `OPEN`: la cota superior
geométrica del paso 2, las constantes `J`, `C_1` y `C_2` si existen, y la tabla
completa de los dieciséis pares.

La lectura "invisible a cualquier expansión en potencias de `Lambda`" sólo se
autoriza con `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. No se usará la
expresión "puramente de red".

## 8. Techo de reclamo

- El resultado vale sólo para la clase congelada: familias internas
  congeladas, geometría euclídea, `alpha`, `tau_0`, `theta`, perfiles y walk.
- Un negativo significa exactamente `..._IN_FROZEN_FAMILY`
  o `..._IN_SCALED_IR_CLASS`. No significa que ningún generador interno suave
  `M = aI + b·sigma` pueda funcionar, ni que no exista señal con otras
  operaciones, preparaciones, nociones de control IR u otros QCA.
- No reabre ni refuta `3/128`, los witnesses de vértice y no-corner, ni el
  negativo narrow-band (§8.16).
- `N -> infinity` con `Lambda_N = 1/N` es un límite espectral y geométrico
  escalado de la red, no un límite continuo físico `a, tau -> 0`. Se mantiene
  `DIMENSIONAL_MAP_CONDITIONAL` (§8.15): no se fijan `a`, `tau`, eV, metros ni
  segundos. Una ley `e^{-J N}` sólo se traduciría condicionalmente a una forma
  `e^{-J' lambda/a}`, sin predicción numérica.
- No se diseña ningún experimento. No se abre `Delta T = 2` como pregunta de
  existencia. No se afirma violación de la microcausalidad del modelo.
- DP14, BDP17 y BB93 sólo motivan. No se transfieren a CJWW (5.15)
  propiedades de otros walks.

## 9. Implementación

Los verificadores revisados conservan sus bytes. Si la ejecución necesita
código nuevo, se crea un certificado propio, con necesidad demostrada y
autorización de implementación en la instrucción de ejecución, según
`scripts/README.md` ("Current scope"). Toda la aritmética decisiva será exacta
o con cotas rigurosas. Los helpers de soporte espacial finito no pueden
truncar sin control el recurso extendido.
