# REGIONAL_LAPLACE_COEFFICIENT_GATE

**Fecha:** 2026-09-17. **Estado al congelar:** contrato fijado antes de
cualquier cálculo; `NOT_EXECUTED / OUTCOME_OPEN`. El estado posterior se
registra sólo en `state/CURRENT_STATE.md`; este encabezado no se actualiza.

**Autorización:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` (2026-09-17).
Cubre únicamente congelar este contrato. No autoriza un encoder, detector
o geometría nuevos, ni reabre `REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE`.

Sucesor de `REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE` (`CURRENT_STATE`
§8.19), sin reabrirlo. Aquel resultado,

`OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`,

conserva sus bytes. La tasa

\[
K_*=I(v_*),\qquad
v_*=\Bigl(1-\frac1{2\sqrt3}\Bigr)(1,1,1),\qquad
J<K_*<\log 4
\]

es **premisa**. No se reoptimiza. El cero del perfil es \(O(\log N)\) y
desplaza el saddle \(O(1)\) sitios; eso tampoco se reabre.

Este gate **no** es de tasa, ni de geometría, ni de lower bound.

## 1. Pregunta única

Calcular el primer coeficiente Laplace **completo** de los dieciséis
pares en el saddle regional ya certificado, incluyendo Hessiano, ceros
de perfil, amplitud spinorial y término de interferencia con la cola
libre, y decidir si algún par Pauli tiene coeficiente no nulo con resto
controlado.

El objeto es

\[
L_{M,M_B}(N)
=
e^{-K_* N}\,N^{-\beta}
\bigl(C_{M,M_B}+o(1)\bigr).
\]

La pregunta estricta es \(C_{M,M_B}\stackrel{?}{=}0\).

**No se asume** una factorización

\[
C=C_{\mathrm{kernel}}\,C_{\mathrm{perfil}}\,C_{\mathrm{spin}}\,C_{\mathrm{interferencia}}.
\]

Esa descomposición puede organizar el cálculo, pero \(C\) es el
coeficiente completo: puede ser una **suma de contribuciones acopladas**
(en particular por la interferencia con \(r\)). Se calcula el objeto
entero antes de factorizarlo, si se factoriza.

## 2. Clase congelada — nada se varía

Fijado por [`SCALED_IR_SIGNALING_GATE.md`](SCALED_IR_SIGNALING_GATE.md) y
por `CURRENT_STATE` §§8.17–8.19:

- Walk CJWW (5.15), una partícula, `S = adj W`.
- \(N\ge 2\), bolas euclídeas \(A_N\), \(B_N\), perfiles, \(\theta=\pi/2\).
- Encoders \(M\in\{I,\sigma_1,\sigma_2,\sigma_3\}\), detectores
  \(M_B\in\{I,(I+\sigma_j)/2\}\). \(I\) es `REFERENCE_CONTROL`.
- Señal \(\delta=|L|\) no proyectada; identidades (L), (F).
- \(K_*=I(v_*)\), saddle único en \(V_{\mathrm{reg}}\), capa \(O(1)\).

**Prohibido.** Reoptimizar \(K_*\). Nuevos encoders, detectores, regiones,
walk, nodo. Reabrir el rayo de vértice como líder. Tratar el mínimo
euclídeo enfrentado como si los perfiles no se anularan.

## 3. Método vinculante

**Paso 0.** Heredar \(K_*\), \(v_*\), \(\xi_*\), (L)/(F), y que los
perfiles no cambian el orden \(N\).

**Paso 1 — Hessiano y \(\beta\).** Hessiano completo del saddle regional
(toro \(p\), relativas, tangenciales a las esferas, normales de la capa
\(O(1)\)). De ahí \(\beta\). No degeneraciones no declaradas.

**Paso 2 — perfiles en la capa.** Expansión local de \(F_N\), \(h_B\),
\(s_N\), \(c_N\) a profundidad \(O(1)\) desde la frontera. \(c_N=O(F^2)\)
no se identifica con \(s_N=O(F)\) sin control.

**Paso 3 — amplitud spinorial.** Kernel inclinado \(S(-i\xi_*)\) y su
proyector de Perron, con fases. \(\sinh t_*\neq 0\) no basta para
\(C\neq 0\).

**Paso 4 — interferencia con \(r\).** La cola libre
\(r=S^N\phi_N=O(N^{-3/2})\) en \(B_N\) puede dominar las piezas
cuadráticas \(e^{-2K_*N}\). \(C\) incluye este término. Una cancelación
puede esconderse aquí. No se trunca el recurso.

**Paso 5 — coeficiente completo.** Sumar **todas** las contribuciones de
tasa \(K_*\) (capa, spin, \(r\), fases) **antes** de decidir
\(C\neq 0\) o \(C=0\). Si \(C=0\), el primer \(C^{(j)}\) accesible, o
constatar que la expansión usada no cierra (eso no es \(\delta\equiv 0\)).

**Paso 6.** Dieciséis pares, sin selección, sin equivalencia Pauli
presupuesta. Numerics de \(N\) concreto: sólo diagnóstico.

Para afirmar \(C\neq 0\) hace falta

\[
L(N)=e^{-K_*N}N^{-\beta}\bigl(C+o(1)\bigr),\qquad C\neq 0.
\]

## 4. Estados terminales (orden, sin solapes)

| Estado | Condición |
| --- | --- |
| `PAULI_LEADING_COEFFICIENT_NONVANISHING` | \(\beta\) identificado, y hay un par con \(M\in\{\sigma_1,\sigma_2,\sigma_3\}\) cuyo \(C\neq 0\) está controlado frente al resto. Con §§8.17 y 8.19, eso autoriza \(\delta\sim\|C\|N^{-\beta}e^{-K_*N}\) y `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` **para ese par**. |
| `ALL_LEADING_COEFFICIENTS_VANISH` | \(\beta\) identificado, \(C=0\) para los dieciséis (o para todos los Pauli, con \(I\) aparte), y el primer \(C^{(j)}\) queda clasificado o la expansión usada cancela a todos los órdenes accesibles. No implica \(\delta\equiv 0\). |
| `REFERENCE_CONTROL_ONLY_LEADING_NONVANISHING` | Sólo pares con \(M=I\) tienen \(C\neq 0\) controlado. |
| `OPEN_AFTER_LAPLACE_COEFFICIENT_ANALYSIS` | Cualquier otro caso: \(\beta\) no identificado; \(C\) no clasificado; resto no controlado; factorización usada como si fuera el coeficiente. |

**Regla explícita.** Un factor local no nulo no es \(C\neq 0\). Un
perfil nulo en el punto geométrico no es \(C=0\). Un producto de cuatro
factores no sustituye a \(C\).

## 5. Techo de reclamo

Sólo la clase de §2. No reabre §§8.16–8.19, `3/128`, no-corner, ni
`Delta T=2`. \(N\to\infty\) no es \(a,\tau\to 0\). Sin unidades físicas.
No se afirma violación de microcausalidad.

## 6. Implementación

Los verificadores revisados conservan sus bytes. Un certificado nuevo
sólo con necesidad demostrada y autorización en la instrucción de
ejecución. No se añade script en este preregistro.
