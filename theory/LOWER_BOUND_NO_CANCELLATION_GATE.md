# LOWER_BOUND_NO_CANCELLATION_GATE

**Fecha:** 2026-09-17. **Estado al congelar:** contrato fijado antes de
cualquier cálculo; `NOT_EXECUTED / OUTCOME_OPEN`. El estado posterior se
registra sólo en `state/CURRENT_STATE.md`; este encabezado no se actualiza.

**Autorización:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` (2026-09-17). Cubre
únicamente congelar este contrato. No autoriza un encoder, detector o
geometría nuevos, ni reabre `SCALED_IR_SIGNALING_GATE`.

Sucesor de `SCALED_IR_SIGNALING_GATE` (`CURRENT_STATE` §8.17), sin
reabrirlo. Aquel resultado,

`OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`,

conserva sus bytes, su cota

\[
\delta_{(M,M_B)}(N)\le D_B(N)\le 36N^4 e^{-JN},
\qquad
J=\Bigl(1-\frac{\sqrt3}{2}\Bigr)\log 2,
\]

y su alcance. Esta cota es **premisa**, no obligación de re-prueba.

## 1. Pregunta única

Para alguno de los dieciséis pares IR-admisibles congelados, ¿puede
demostrarse

\[
\delta_{(M,M_B)}(N)>0
\]

para todo \(N\ge N_*\), o bien puede demostrarse nulidad exacta

\[
\delta_{(M,M_B)}(N)=0
\]

(idénticamente, o para todo \(N\ge N_*\))?

No se pide un nuevo techo. El techo ya existe. La pregunta es si **llega
algo**, o si **todo cancela exactamente**.

## 2. Clase congelada — nada se varía

Todo lo siguiente queda fijado por
[`SCALED_IR_SIGNALING_GATE.md`](SCALED_IR_SIGNALING_GATE.md) y por
`CURRENT_STATE` §8.17. Variar cualquiera de estos objetos es otro gate.

- Walk CJWW (5.15), sector de una partícula, `S = adj W`.
- `N\ge 2` entero, `Delta T = N`, `Lambda_N = 1/N`, `Lambda'_N = N^{-1/2}`.
- Bolas euclídeas `A_N`, `B_N` de radio `N/4`, centros `0` y `(N,N,N)`.
- Recurso `phi_N`, encoders `M ∈ {I, σ1, σ2, σ3}`, detectores
  `M_B ∈ {I, (I+σ1)/2, (I+σ2)/2, (I+σ3)/2}`, perfiles y `θ = π/2`
  literales del charter escalado.
- Señal física no proyectada `δ_{(M,M_B)}(N) = |L_{(M,E)}|` de las
  identidades (L) y (F) del informe escalado. `I` sigue siendo
  `REFERENCE_CONTROL`.
- Admisibilidad IR ya demostrada para las ocho operaciones. No se
  re-abre el criterio `eta`.

**Prohibido.** Nuevos encoders, nuevos detectores, nuevas regiones, otro
walk, otro nodo, otro `α` o `θ`, proyección espectral de la señal,
ancillas, postselección, y cualquier familia `M = aI + b·σ` no congelada.

## 3. Método vinculante — no empezar por una lower bound bruta

El primer ataque no es acotar directamente toda `δ_B`. Es la **estructura
de cancelación** de la amplitud dominante.

**Paso 0 — herencia.** Registrar, sin recalcular, la cota §8.17, las
ocho admisibilidades, y las identidades (L), (F) y las cuatro columnas
de amplitud (`v±id`, `v+ib`, `v+b`, `v-id`).

**Paso 1 — contribución dominante.** Sobre el mismo contorno o un
saddle compatible con el símbolo trigonométrico, identificar, para cada
par o para una clase de pares con razón escrita, una contribución
candidata de la forma

\[
A_{M,M_B}(N)\,e^{-K N}
\]

con \(K>0\) y \(A\) de crecimiento a lo sumo polinómico. \(K\) no se
identifica con \(J\): \(J\) es una tasa inferior de una upper bound;
la tasa líder puede ser estrictamente mayor. Un prefactor \(N^p\) se
absorbe en \(A(N)\). Si no hay un término líder identificable, se
registra y no se finge.

**Paso 2 — clasificación del coeficiente.** Para cada \(A_{M,M_B}\)
identificado, decidir exactamente una de:

- \(A_{M,M_B}\not\equiv 0\) (con control del signo o módulo, no un
  diagnóstico numérico);
- \(A_{M,M_B}=0\) **por simetría** del protocolo congelado (hay que
  exhibir la simetría);
- \(A_{M,M_B}\) cancela sólo **hasta un orden finito**, con el primer
  término no nulo identificado o con la prueba de que todos los órdenes
  accesibles cancelan.

Un término cuadrático positivo en (L) **no** clasifica \(A\): puede
cancelarse con \(H_E\) o con la interferencia. El rayo de vértice no
nulo **no** se promueve, por sí solo, a \(A\not=0\) de región.

**Paso 3 — resto, sólo después del paso 2.**

- Si \(A\not\equiv 0\), controlar el resto para promoverlo a
  \(\delta(N)>0\) para todo \(N\ge N_*\), o a una asintótica
  \(\delta(N)=A(N)e^{-KN}(1+o(1))\) con \(A(N)\not=0\) controlado.
- Si \(A=0\) por simetría o a todos los órdenes de la expansión usada,
  decidir si eso implica \(\delta\equiv 0\) o sólo que el líder se
  anuló y queda un resto no controlado.
- Una lower bound bruta de toda \(\delta\) **sólo** está autorizada
  cuando el paso 2 está escrito para el par en cuestión y el resto no
  cierra. No se usa para saltarse la cancelación.

**Paso 4 — clasificación** según §4. Se reportan los dieciséis pares,
sin selección.

Se priorizan identidades, simetrías exactas y restos acotados. Una
evaluación numérica en \(N\) concretos es a lo sumo diagnóstico
`SUPPORTED` con error certificado. Nunca establece un estado terminal,
una no-cancelación, ni una ley asintótica.

## 4. Estados terminales (orden de asignación, sin solapamientos)

| Estado | Condición |
| --- | --- |
| `SIGNAL_NONVANISHING_IN_FROZEN_PAULI_PAIR` | Hay un par con `M ∈ {σ1, σ2, σ3}` y `δ(N)>0` para todo `N ≥ N_*`, o asintótica de amplitud no nula controlada. Con la cota §8.17, esto autoriza a registrar `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` **para ese par**, no para la familia entera. |
| `ALL_SIXTEEN_EXACTLY_ZERO` | Se demuestra `δ_{(M,M_B)}(N)=0` para los dieciséis pares, para todo `N ≥ N_*`. Es obstrucción exacta de esas dieciséis respuestas, **no** la afirmación `D_B=0`. |
| `REFERENCE_CONTROL_ONLY_NONVANISHING` | Algún par con `M=I` es no nulo con la disciplina de §3, y **ningún** par Pauli lo es. `I` no establece por sí solo un estado de señalización IR positivo. |
| `OPEN_AFTER_CANCELLATION_ANALYSIS` | Cualquier otro caso: líder no identificado; `A` no clasificado; resto no controlado; cancelación a orden finito sin término siguiente; lower bound bruta insuficiente; inconsistencia de convenciones. |

**Regla explícita.** Demostrar \(A=0\) en el término líder **no** autoriza
`ALL_SIXTEEN_EXACTLY_ZERO`. Demostrar \(A\not=0\) **no** autoriza
`SIGNAL_NONVANISHING_IN_FROZEN_PAULI_PAIR` sin control del resto. Una
cota `0 ≤ δ ≤ 36 N^4 e^{-JN}` sigue siendo el resultado de §8.17, no un
estado nuevo.

Se registra, aunque el estado sea `OPEN`: la tabla de los dieciséis
pares con la clasificación de \(A\), el valor de \(K\) si existe, y si
el resto está controlado.

## 5. Techo de reclamo

- Sólo la clase congelada de §2. Un positivo es
  `..._IN_FROZEN_PAULI_PAIR`. Un negativo de las dieciséis respuestas no
  es `D_B=0` ni «ningún encoder suave funciona».
- No reabre ni refuta `3/128`, no-corner, el negativo narrow-band
  (§8.16), ni la cota escalada (§8.17).
- `N → ∞` no es `a, τ → 0`. Se mantiene `DIMENSIONAL_MAP_CONDITIONAL`.
  Una ley `A e^{-KN}` sólo se traduciría condicionalmente, sin predicción
  numérica en eV, metros ni segundos.
- No se diseña un experimento. No se abre `Delta T = 2`. No se afirma
  violación de la microcausalidad del modelo.
- La lectura «invisible a cualquier expansión en potencias de `Lambda`»
  sólo se autoriza si se alcanza `SIGNAL_NONVANISHING_IN_FROZEN_PAULI_PAIR`
  (o el estado equivalente ya definido en el charter escalado). No se
  usará «puramente de red».
- DP14, BDP17 y BB93 sólo motivan. No se transfieren propiedades de
  otros walks.

## 6. Implementación

Los verificadores revisados conservan sus bytes. Si la ejecución necesita
código nuevo, se crea un certificado propio, con necesidad demostrada y
autorización de implementación en la instrucción de ejecución. Toda la
aritmética decisiva será exacta o con cotas rigurosas. Los helpers de
soporte espacial finito no pueden truncar sin control el recurso
extendido. No se añade script en este acto de preregistro.
