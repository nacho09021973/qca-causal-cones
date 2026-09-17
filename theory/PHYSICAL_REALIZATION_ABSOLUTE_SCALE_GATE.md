# PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE

**Fecha:** 2026-09-17. **Estado al congelar:** contrato fijado antes de
cualquier cálculo; `NOT_EXECUTED / OUTCOME_OPEN`. El estado posterior se
registra sólo en `state/CURRENT_STATE.md`; este encabezado no se actualiza.

**Autorización:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` (2026-09-17).
Cubre **únicamente congelar este contrato**. No autoriza su ejecución.
No autoriza el fork 4A (implementación física del walk). No autoriza
otro gate de señalización, ni un encoder, detector, geometría, perfil,
walk o nodo nuevos.

Sucesor de `REGIONAL_LAPLACE_COEFFICIENT_GATE` (`CURRENT_STATE` §8.20),
sin reabrirlo. Aquel resultado,

`PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`,

conserva sus bytes. Hereda, sin reabrirla, la auditoría dimensional
§8.15 (`DIMENSIONAL_MAP_CONDITIONAL`): el modelo no fija `a` ni `τ`.

Este gate **no** es de señalización, ni de tasa, ni de coeficiente
Laplace, ni de traducción dimensional del testigo `3/128`.

## 1. Pregunta única

Dada la ley IR ya derivada, para los doce pares Pauli de la clase
congelada y `N` suficientemente grande,

\[
\delta_{M,M_B}(N)
=
\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad
K_*=I(v_*),
\qquad
\theta_N=\bigl\{\sqrt3\,N/4\bigr\},
\]

identificar qué **podrían** significar `a`, `τ`, `Λ`, los grados internos,
Alice y Bob en un sistema natural, y decidir si alguna identificación
convierte esa asintótica adimensional en una predicción en metros,
segundos, energía y sensibilidad instrumental.

La pregunta no es si el QCA “es la naturaleza”. Es si la **estructura**
ya demostrada admite una correspondencia con algo natural, y qué
predicción dimensionada seguiría.

## 2. Clase congelada — nada se varía

Fijado por [`SCALED_IR_SIGNALING_GATE.md`](SCALED_IR_SIGNALING_GATE.md)
y por `CURRENT_STATE` §§8.15–8.20:

- Walk CJWW (5.15), una partícula, `S = adj W`.
- Bolas euclídeas, perfiles, `θ=π/2`, las cuatro `M` y las cuatro `M_B`.
- Recurso `g(Np)`, `c_IR = 1`, `C_micro = [-1,1]^3`.
- `K_* = I(v_*)`, `β = 13/2`, `C = C(θ_N)` uniformemente no nulo en
  los doce pares Pauli (y en el control `I`).
- Diccionario simbólico de §8.15: `x = a n`, `t = N τ`, `k = p/a`,
  `E = ħ ω/τ` (mod `2π ħ/τ`), `v_phys = (a/τ) ∇_p ω`, de donde
  `c_IR^phys = a/τ`.

**Prohibido.** Reabrir §§8.16–8.20. Recalcular `K_*`, `β` o `C`. Nuevos
encoders, detectores, regiones, walk o nodo. Tratar `3/128` como si fuera
esta ley IR. Fijar `a` o `τ` por decreto (Planck u otra escala nombrada)
como si el modelo los derivara. Diseñar el experimento 4A. Afirmar
violación de microcausalidad.

## 3. Bifurcación 4A / 4B

Tras el cierre teórico del paso 3 en la clase preregistrada, el frente
se bifurca:

| Fork | Contenido | Estado en este acto |
| --- | --- | --- |
| **4A** | Implementación física del walk que permita contrastar la ley ya derivada | **Identificado, no chartered** |
| **4B** | Este gate: puente conceptual hacia física fundamental (`a,τ,Λ`, grados internos, Alice, Bob; predicción en SI y sensibilidad) | **Chartered, `NOT_EXECUTED`** |

4B se prioriza conceptualmente antes de construir 4A. Ésa era la
ambición original. El siguiente cálculo autorizado, si se ejecuta, es
éste, no otro sobre `C` ni un diseño de laboratorio.

## 4. Método vinculante

**Paso 0.** Heredar §§8.15 y 8.20. No redemostrar la ley IR. No
redemostrar que el modelo no fija `a` ni `τ`.

**Paso 1 — diccionario condicional de la ley IR.** Restaurar
`δ_{M,M_B}(N)` a unidades físicas **condicionalmente** en `(a,τ,Λ)`:
separación de las bolas, duración `Nτ`, corte `Λ/a`, y la tasa
`e^{-K_* N}` como función de esas escalas. `N → ∞` **no** es
`a,τ → 0`.

**Paso 2 — identificaciones candidatas.** Enumerar, como **hipótesis
externas** y no como salidas del QCA, qué podrían ser `a`, `τ`, `Λ`,
los dos modos internos, Alice y Bob en un sistema natural
(condensado, red óptica, escala de Planck, u otras). Cada candidata
se etiqueta `HYPOTHESIS`, nunca `DERIVED_FROM_THE_MODEL`.

**Paso 3 — forzamiento vs posibilidad.** Decidir, para cada candidata,
si la estructura la **fuerza**, la **permite** o la **excluye**. Un
ejemplo compatible no es una identificación. Un fiat Planck no es
una derivación.

**Paso 4 — predicción dimensionada y sensibilidad.** Donde una
identificación (forzada o meramente parametrizada) esté bien
definida, convertir la ley en una predicción en metros, segundos,
energía, y en el umbral instrumental que haría observable
`δ ∼ N^{-13/2} e^{-K_* N}`. Si ninguna identificación está forzada,
la salida es una **familia** parametrizada, no un número único.

**Paso 5.** Numerics de `N` concreto o de una escala nombrada: sólo
diagnóstico, nunca fijan el estado terminal.

## 5. Estados terminales (orden, sin solapes)

| Estado | Condición |
| --- | --- |
| `NATURAL_SCALE_FORCED` | Alguna identificación con un sistema natural está **forzada** por la estructura congelada (no meramente permitida) y produce una predicción cuantitativa en SI y sensibilidad. |
| `CONDITIONAL_SI_FAMILY` | La ley se convierte en una familia parametrizada en metros, segundos, energía y sensibilidad, pero al menos una escala o identificación sigue siendo calibración externa. Análogo de §8.15 para esta ley IR. |
| `NO_NATURAL_REALIZATION_IN_SCOPE` | Bajo las hipótesis declaradas, el protocolo IR congelado no admite correspondencia con un sistema natural. |
| `OPEN_AFTER_REALIZATION_ANALYSIS` | Cualquier otro caso: identificaciones no clasificadas; fiat usado como si fuera derivación; 4A ejecutado como si fuera 4B; ley IR reabierta. |

**Regla explícita.** Que §8.15 sea `CONDITIONAL` no decide este gate:
aquí el objeto es la ley IR de §8.20 y el significado físico de
`a,τ,Λ`, no el testigo localizado `3/128`. Un diccionario simbólico
sin candidatos de naturaleza no es `NATURAL_SCALE_FORCED`. Un
candidato único nombrado sin argumento de forzamiento no lo es
tampoco.

## 6. Techo de reclamo

Sólo la clase de §2. No reabre §§8.15–8.20, `3/128`, no-corner,
`Delta T = 2`, ni `B_infty^*` (Sec. 4). No afirma `D_B > 0` fuera de
los doce pares Pauli de esa clase. No afirma que el modelo sea la
naturaleza. No diseña 4A. `N → ∞` no es `a,τ → 0`. Sin violación de
microcausalidad.

Conclusión ya autorizada por §§8.4, 8.17 y 8.20, que este gate **no**
reabre y **no** refuerza:

> En el Weyl QCA 3D estudiado, la diferencia entre el cono relativista
> emergente y el soporte causal microscópico no es sólo una posibilidad
> geométrica: bajo el protocolo IR controlado preregistrado produce una
> respuesta operacional asintóticamente no nula, aunque no
> perturbativamente suprimida.

Eso es entidad científica del modelo, no de la naturaleza. El objeto
de este gate es si esa estructura puede corresponder a algo natural.

## 7. Implementación

Los verificadores revisados conservan sus bytes. Un certificado nuevo
sólo con necesidad demostrada y autorización en la instrucción de
ejecución. No se añade script en este preregistro.
