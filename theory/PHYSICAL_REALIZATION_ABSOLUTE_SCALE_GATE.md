# PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE

**Fecha:** 2026-09-17. **Estado al congelar:** contrato fijado antes de
cualquier cálculo; `NOT_EXECUTED / OUTCOME_OPEN`. El estado posterior se
registra sólo en `state/CURRENT_STATE.md`; este encabezado no se actualiza.

**Autorización:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` (2026-09-17).
Cubre **únicamente congelar este contrato**. No autoriza su ejecución.
No autoriza el fork 4A (implementación física del walk). No autoriza
otro gate de señalización, ni un encoder, detector, geometría, perfil,
walk o nodo nuevos.

**Precisión de contrato (2026-09-17, antes de cualquier cálculo).**
Incorpora los cuatro criterios de cierre y los desenlaces negativos
como cierres de primera clase. El paso 3 **no se reabre por inercia**.

Sucesor de `REGIONAL_LAPLACE_COEFFICIENT_GATE` (`CURRENT_STATE` §8.20),
sin reabrirlo. Aquel resultado,

`PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`,

conserva sus bytes y entra **como input**. Hereda, sin reabrirla, la
auditoría dimensional §8.15 (`DIMENSIONAL_MAP_CONDITIONAL`): el modelo
no fija `a` ni `τ`.

Este gate **no** es de señalización, ni de tasa, ni de coeficiente
Laplace, ni de traducción dimensional del testigo `3/128`.

Separación vinculante, no negociable:

```
modelo: cerrado  ≠  naturaleza: establecido  ≠  experimento: diseñado
```

`e9353ad` marca esa transición: se deja de preguntar si el efecto
existe en el modelo y se pregunta si el modelo puede adquirir
significado físico absoluto. Ése es ya otro problema.

## 1. Pregunta única

**No** se pregunta si existe \(\delta_{M,M_B}(N)\neq 0\). Eso está
cerrado en §8.20 y se hereda. Cualquier trabajo posterior sobre física
real usa ese resultado como input; **no** vuelve a optimizar encoder,
detector, geometría o asintótica para “mejorarlo”.

La pregunta es si existe una identificación **físicamente defendible**

\[
(a,\tau,\Lambda,\text{modos internos},A,B)
\;\longleftrightarrow\;
(\text{magnitudes y operaciones físicas})
\]

que convierta

\[
\delta(N)\sim\bigl|C(\theta_N)\bigr|\,N^{-13/2}e^{-K_*N}
\]

en una predicción **dimensional y falsable**.

La pregunta no es si el QCA “es la naturaleza”. Es si la estructura ya
demostrada admite una correspondencia absoluta, y qué predicción
dimensionada —o qué inaccesibilidad— seguiría.

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

**Prohibido.** Reabrir el paso 3 ni §§8.16–8.20. Recalcular `K_*`, `β`
o `C`. Nuevos encoders, detectores, regiones, walk o nodo, aunque sea
“para mejorar la señal”. Tratar `3/128` como si fuera esta ley IR.
Fijar `a` o `τ` por decreto (Planck u otra escala nombrada) como si el
modelo los derivara: `a=ℓ_P` es `ASSUMPTION`, nunca `DERIVED`. Diseñar
el experimento 4A. Forzar el desenlace hacia “experimento viable”.
Afirmar violación de microcausalidad. Afirmar que la naturaleza queda
establecida porque el modelo está cerrado.

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

## 4. Cuatro criterios de cierre (duros, los cuatro)

Cada uno se puntúa por separado. El gate **no** tiene como criterio de
éxito un experimento viable. Un negativo en cualquiera es un cierre
legítimo y **no** debilita el paso 3.

**1. Escala absoluta.** No basta \(a/\tau=c\). Tiene que aparecer
información **externa** que fije \(a\) o \(\tau\), o una relación
adicional **físicamente motivada**. Poner \(a=\ell_P\) por conveniencia
es `ASSUMPTION`, nunca `DERIVED`.

**2. Diccionario físico.** Identificar qué son realmente los dos
componentes internos, qué operación física implementa \(M=\sigma_j\),
qué representa \(M_B\), y qué significa una preparación narrow-band en
el sistema candidato. Un relabeling formal no es diccionario.

**3. Observable dimensional.** Pasar de una distancia/probabilidad
adimensional a algo que un aparato registre: conteos, fase, frecuencia,
energía, ocupación, correlación, u otro, con una **ley explícita en SI**.
\(\delta\) adimensional no es esa ley.

**4. Detectabilidad.** Aunque exista el mapa, si al sustituir escalas
físicas resulta

\[
\delta\sim e^{-K_*\lambda/a}
\]

con \(\lambda/a\) astronómico, el efecto puede ser físicamente real y
experimentalmente inaccesible. Eso **también** cierra el gate.

## 5. Método vinculante

**Paso 0.** Heredar §§8.15 y 8.20 como input. No redemostrar la ley IR.
No redemostrar que el modelo no fija `a` ni `τ`. No retocar encoder,
detector, geometría ni asintótica.

**Paso 1.** Restaurar \(\delta(N)\) condicionalmente en \((a,\tau,\Lambda)\):
separación de las bolas, duración \(N\tau\), corte \(\Lambda/a\), tasa
\(e^{-K_*N}\). \(N\to\infty\) **no** es \(a,\tau\to 0\). Esto no satisface
el criterio 1.

**Paso 2.** Candidatas de identificación, cada una `HYPOTHESIS` o
`ASSUMPTION`, nunca `DERIVED` salvo prueba de forzamiento. Criterios 1
y 2.

**Paso 3.** Observable SI (criterio 3) sobre esa identificación, forzada
o asumida. Si sólo hay familia parametrizada, el observable queda en
función de \((a,\tau,\Lambda)\).

**Paso 4.** Detectabilidad (criterio 4) al sustituir escalas. No se
descarta un mapa por ser inobservable; se clasifica.

**Paso 5.** Numerics de \(N\) concreto o de una escala nombrada: sólo
diagnóstico, nunca fijan el estado terminal.

## 6. Estados terminales (orden, sin solapes)

El desenlace **no** se fuerza hacia experimento viable. Los tres
negativos son cierres de primera clase.

| Estado | Condición |
| --- | --- |
| `PHYSICAL_MAP_ABSOLUTE_AND_DETECTABLE` | Los cuatro criterios se cumplen: escala absoluta con información externa o relación adicional motivada (no fiat); diccionario físico de modos, \(M\), \(M_B\) y preparación; ley SI de un observable de aparato; \(\lambda/a\) no astronómico. **No** autoriza 4A ni “naturaleza establecida”. |
| `PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE` | Hay mapa defendible (absoluto o bajo `ASSUMPTION` declarada) y ley SI, pero al sustituir escalas \(\delta\sim e^{-K_*\lambda/a}\) con \(\lambda/a\) astronómico. Cierre legítimo. El paso 3 no se debilita. |
| `PHYSICAL_MAP_CONDITIONAL_ONLY` | Diccionario y/o observable SI existen como familia parametrizada; \(a\) o \(\tau\) siguen siendo calibración externa. \(a/\tau=c\) no basta para el criterio 1. Análogo de §8.15 para esta ley IR. |
| `NO_ABSOLUTE_SCALE_DERIVABLE` | La estructura congelada no determina \(a\) ni \(\tau\) más allá de \(a/\tau=c\); no hay relación adicional físicamente motivada; Planck y similares quedan `ASSUMPTION`. No se alcanza un mapa útil para (2)–(4). |
| `OPEN_AFTER_REALIZATION_ANALYSIS` | Cualquier otro caso: criterios no puntuados; fiat usado como `DERIVED`; paso 3 reabierto; 4A ejecutado como si fuera 4B. |

**Regla explícita.** Que §8.15 sea `CONDITIONAL` no decide este gate:
el objeto es la ley IR de §8.20, no `3/128`. Un diccionario simbólico
sin (2) ni (3) no es `PHYSICAL_MAP_CONDITIONAL_ONLY`. `a=ℓ_P` no
promociona a `PHYSICAL_MAP_ABSOLUTE_AND_DETECTABLE`. Un mapa
inobservable no se relabela como fracaso del modelo.

## 7. Techo de reclamo

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

## 8. Implementación

Los verificadores revisados conservan sus bytes. Un certificado nuevo
sólo con necesidad demostrada y autorización en la instrucción de
ejecución. No se añade script en este preregistro.
