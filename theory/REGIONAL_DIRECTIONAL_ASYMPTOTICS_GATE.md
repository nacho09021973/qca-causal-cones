# REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE

**Fecha:** 2026-09-17. **Estado al congelar:** contrato fijado antes de
cualquier cálculo; `NOT_EXECUTED / OUTCOME_OPEN`. El estado posterior se
registra sólo en `state/CURRENT_STATE.md`; este encabezado no se actualiza.

**Autorización:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` (2026-09-17).
Cubre únicamente congelar este contrato. No autoriza un encoder, detector
o geometría nuevos, ni reabre `LOWER_BOUND_NO_CANCELLATION_GATE` ni
`SCALED_IR_SIGNALING_GATE`.

Sucesor de `LOWER_BOUND_NO_CANCELLATION_GATE` (`CURRENT_STATE` §8.18),
sin reabrirlo. Aquel resultado,

`OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`,

conserva sus bytes. La cota escalada §8.17 sigue siendo premisa:

\[
\delta_{(M,M_B)}(N)\le D_B(N)\le 36N^4 e^{-JN},
\qquad
J=\Bigl(1-\frac{\sqrt3}{2}\Bigr)\log 2.
\]

Este gate **no** se llama lower bound. No empieza por acotar \(\delta\).

## 1. Pregunta única

¿Cuál es el saddle anisótropo dominante de la **propagación regional**
entre \(A_N\) y \(B_N\), y cuál es su primer coeficiente no nulo después
de integrar los perfiles congelados?

Se busca una asintótica de las respuestas (L) de la forma

\[
L_{M,M_B}(N)
=
e^{-K_* N}\,N^{-\beta}
\left(
C_{M,M_B}
+\frac{C^{(1)}_{M,M_B}}{N}
+\cdots
\right),
\]

con tres preguntas **sucesivas**:

1. \(K_*\,?\)
2. \(C_{M,M_B}\stackrel{?}{=}0\)
3. si \(C=0\), cuál es el primer \(C^{(j)}\neq 0\).

El hecho de carga heredado es que el mínimo **geométrico**
(\(|y-x|_2=\sqrt3 N-N/2\)) cae donde \(F_N=h_B=0\). Por tanto el saddle
geométricamente óptimo **puede no ser** el saddle físicamente dominante:
el cero del perfil desplaza el máximo efectivo hacia el interior, y ese
desplazamiento puede cambiar \(K_*\) y el prefactor.

La física matemática del gate es la competición

\[
\text{exponente de propagación}
\quad\text{vs}\quad
\text{cero del perfil en la frontera}.
\]

## 2. Clase congelada — nada se varía

Todo lo siguiente queda fijado por
[`SCALED_IR_SIGNALING_GATE.md`](SCALED_IR_SIGNALING_GATE.md) y por
`CURRENT_STATE` §§8.17–8.18. Variar cualquiera es otro gate.

- Walk CJWW (5.15), una partícula, `S = adj W`.
- \(N\ge 2\), `Delta T = N`, bolas euclídeas \(A_N\), \(B_N\) de radio
  \(N/4\), centros \(0\) y \((N,N,N)\).
- Recurso \(\phi_N\), encoders \(M\in\{I,\sigma_1,\sigma_2,\sigma_3\}\),
  detectores \(M_B\in\{I,(I+\sigma_j)/2\}\), perfiles y \(\theta=\pi/2\).
- Señal \(\delta=|L|\) no proyectada; identidades (L), (F) heredadas.
- \(I\) es `REFERENCE_CONTROL`.

**Prohibido.** Nuevos encoders, detectores, regiones, walk, nodo, \(\alpha\),
\(\theta\), proyección espectral, ancillas, postselección. No se reabre
el rayo de vértice como líder regional.

## 3. Método vinculante

**Paso 0 — herencia.** Cota §8.17; admisibilidad IR; (L)/(F); el vértice
no se promueve; el mínimo geométrico está en la esfera de perfiles nulos;
\(A\) no está clasificado.

**Paso 1 — tasa regional \(K_*\).** Sobre el conjunto de velocidades
\((B_N-A_N)/N\), identificar la tasa anisótropa del kernel inclinado
(óptimo de \(\xi\mapsto \xi\cdot v-\log\rho(S(-i\xi))\), o equivalente
holomorfo). No se identifica \(K_*\) con \(J\), ni con \(\log 4\), ni
con \(I\) evaluado sólo en los puntos enfrentados **sin** la competición
con el perfil.

**Paso 2 — competición perfil vs exponente.** Maximizar, sobre
\(x\in A_N\), \(y\in B_N\), el exponente efectivo que combina
\(I((y-x)/N)\) con \(\log F_N(x)\) y \(\log h_B(y)\) (y con \(s_N\),
\(c_N\) según el par). El candidato interior desplazado, de profundidad
\(O(1/N)\) u otra escala demostrada, es el saddle **físico**. Si el
máximo efectivo permanece en la frontera, hay que demostrarlo.

**Paso 3 — Laplace / saddle.** En ese saddle físico, extraer \(\beta\) y
el coeficiente líder \(C_{M,M_B}\) para cada par, o para una clase con
equivalencia demostrada. Controlar el resto a un orden que decida si
\(C=0\). Si \(C=0\), bajar al primer \(C^{(j)}\neq 0\) o demostrar que
todos los órdenes de la expansión usada cancelan (eso **no** es
\(\delta\equiv 0\)).

**Paso 4 — clasificación** según §4. Dieciséis pares, sin selección.
Sin numerics como estado terminal.

## 4. Estados terminales (orden, sin solapes)

| Estado | Condición |
| --- | --- |
| `SADDLE_RATE_AND_NONVANISHING_LEADING_COEFFICIENT` | Se identifican \(K_*>0\) y \(\beta\), y hay un par con \(M\in\{\sigma_1,\sigma_2,\sigma_3\}\) cuyo \(C\neq 0\) está controlado frente al resto. Con §8.17, eso autoriza `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` **para ese par**. |
| `SADDLE_RATE_LEADING_VANISHES` | \(K_*\) y \(\beta\) identificados, \(C=0\) para los dieciséis (o para todos los Pauli, con el control \(I\) registrado aparte), y el primer \(C^{(j)}\) queda clasificado o se demuestra que la expansión usada cancela a todos los órdenes accesibles. No implica \(\delta\equiv 0\). |
| `REFERENCE_CONTROL_ONLY_LEADING_NONVANISHING` | Sólo pares con \(M=I\) tienen \(C\neq 0\) controlado. |
| `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS` | Cualquier otro caso: \(K_*\) no identificado; competición perfil/exponente no resuelta; \(C\) no clasificado; resto no controlado. |

**Regla explícita.** Evaluar \(I\) sólo en \(x_\ast,y_\ast\) **sin** el
perfil no determina \(K_*\). Un coeficiente de Laplace no calculado no
es \(C=0\). El vértice \(4^{-N}\) no es \(K_*\).

## 5. Techo de reclamo

Sólo la clase de §2. No reabre §§8.16–8.18, `3/128`, no-corner, ni
`Delta T=2`. \(N\to\infty\) no es \(a,\tau\to 0\). Sin unidades físicas.
No se afirma violación de microcausalidad. DP14, BDP17 y BB93 sólo
motivan.

## 6. Implementación

Los verificadores revisados conservan sus bytes. Un certificado nuevo
sólo con necesidad demostrada y autorización en la instrucción de
ejecución. No se añade script en este preregistro.
