# Saturación causal direccional: walks 3D de Cedzich–Joye–Werner–Werner

Fecha: 2026-09-16. Alcance: sólo la pregunta física de cuándo `c_IR` satura el
límite causal microscópico. No abre líneas nuevas ni propone teoremas nuevos.

Fuente primaria: `sources/2408.02108v1.pdf` (CJWW, *Exponential tail estimates
for quantum lattice dynamics*, Ann. Henri Poincaré, DOI 10.1007/s00023-025-01598-4),
Secs. 2.1–2.2, Lema 4.1, Sec. 5.4. Identificación Pavia: `sources/1601.04832v1.pdf`,
Ec. (15) y (21).

Verificación: [`scripts/verify_directional_saturation.py`](../scripts/verify_directional_saturation.py),
15/15 checks, fail-closed. Catorce son **exactos** (SymPy: soporte de Fourier como
polinomio de Laurent en `z_k = e^{ip_k}`, identidades SOS, series en `u = 1 − f`);
sólo el llenado de los cuerpos de velocidad es numérico y va etiquetado SUPPORTED.

## 0. Correcciones de partida (concretas, verificadas)

1. **Signo de la dispersión.** El producto literal de CJWW (5.12),
   `W(p)=e^{ip1σ1}e^{ip2σ2}e^{ip3σ3}`, tiene `tr W(p)/2 = c1c2c3 + s1s2s3`
   (verificado a 0.00e+00 sobre 3000 puntos). La ec. (5.13) impresa da
   `arccos(c1c2c3 − s1s2s3)`, que es la traza de `e^{-ip1σ1}e^{-ip2σ2}e^{-ip3σ3}`.
   Las dos difieren por `p → −p`. La fórmula del enunciado (signo `+`) es por
   tanto la correcta para (5.12), y coincide con la quiralidad `ω⁻` de Pavia
   Ec. (15), `ω_k^± = arccos(c_x c_y c_z ∓ s_x s_y s_z)`, con
   `c_i = cos(k_i/√3)`, `s_i = sin(k_i/√3)`; es decir `p = k/√3`. **ESTABLISHED.**
   Irrelevante físicamente: `ω_± = ±ω` y la región de velocidades es idéntica
   bajo ambos signos (verificado: mismos `sup|v|`, mismas cotas cilíndricas).
2. CJWW (5.14) imprime `(p1²+p1²+p1²)`; se lee `(p1²+p2²+p3²)`. Exacto, con
   `p = t(a,b,c)` y `arccos(1−u)² = 2u + u²/3 + 4u³/45 + O(u⁴)`:
   `ω² = |p|² − 2abc·t³ + O(t⁴)` (walk 1) y `ω² = |p|² + O(t⁴)`, sin término cúbico
   (walk 2). En ambos casos `c_IR = 1`.
3. **No** hay esfera de radio `√3`. El frente estricto es el cubo `[−1,1]³`.

## 1. Definiciones

Unidades fijas: un paso de red por paso de tiempo, en las coordenadas `p`
(equivalentemente `k/√3`). Todas las cantidades siguientes son velocidades en
esas mismas coordenadas; `S` es invariante bajo el reescalado global `p = k/√3`.

**(a) Cuerpo causal microscópico y frente causal direccional.**
Sea `F = {x : W_x ≠ 0}` el conjunto de saltos de un paso, `W(p) = Σ_x W_x e^{ip·x}`.
`C_micro := conv F`. El **frente causal microscópico direccional** es la función
soporte
`v_sub(n̂) := h_{C_micro}(n̂) = sup_{x∈C_micro} n̂·x`, `‖n̂‖₂ = 1`.
Es el objeto que aparece ya en CJWW Lema 4.1 como `R_F(λ) = sup{λ·x : x ∈ F}`,
y que da `I(x) = ∞` fuera de `conv F`: fuera de `C_micro` la amplitud es
**exactamente cero**, no sólo improbable.

**(b) Velocidad de grupo y región de propagación.**
`v_j(p) = ∇_p ω_j(p)` en los puntos regulares (CJWW Ec. (2.11)); `Γ` = región de
propagación = soporte de la distribución límite de `Q(t)/t` (CJWW Sec. 2.2).
`h_Γ(n̂) = sup_{v∈Γ} n̂·v`. Siempre `Γ ⊆ C_micro`, luego `h_Γ ≤ v_sub`.

**(c) `c_IR`.** Pendiente de la dispersión en el punto cónico:
`ω(p∨+p)² = c_IR²|p|² + o(|p|²)`. Cono IR isótropo `B(c_IR)`, con
`h_{B(c_IR)}(n̂) = c_IR` para toda `n̂`.

**(d) Saturación direccional — definición final.**
La definición candidata `S(n̂) = c_IR / v_sub(n̂)` es **geométricamente correcta**
pero debe escribirse como cociente de funciones soporte, y su parte "global"
debe reemplazarse. Forma final:

> `S(n̂) := h_{B(c_IR)}(n̂) / h_{C_micro}(n̂)`, que en el caso isótropo es
> exactamente `c_IR / v_sub(n̂)`.
> **Saturación direccional** en `n̂`: `S(n̂) = 1`. **Subsaturación**: `S(n̂) < 1`.
> **Conjunto de saturación** `Σ := {n̂ : S(n̂) = 1}`.
> Objeto fundamental: la función `S(·)` completa, no un resumen escalar. Si hace
> falta **un solo número** que mida la separación máxima, úsese la estadística
> descriptiva `S_min := inf_{n̂} S(n̂)`; no es un frente de trabajo.

Tres modificaciones mínimas y su razón:

- *Numerador como función soporte.* `S ≤ 1` para toda `n̂` equivale exactamente a
  `B(c_IR) ⊆ C_micro` (dos cuerpos convexos se comparan por sus funciones
  soporte). Con `c_IR` escalar suelto esa equivalencia queda implícita y la
  definición no se extiende a conos IR anisótropos (sector masivo del repo).
- *`S ≤ 1` es teorema, no convenio.* En los puntos cónicos `∇ω = p/|p|` recorre
  toda la esfera unidad, luego `∂B(c_IR) ⊆ Γ ⊆ C_micro`; de ahí `c_IR ≤ r_in`.
- *"Saturación global" es vacía y debe eliminarse — bajo hipótesis explícitas.*
  `S ≡ 1` exige `h_{C_micro} ≡ c_IR`, es decir que `C_micro` sea una bola euclídea.
  Bajo **(i)** rango finito con conjunto de saltos `F` finito, **(ii)** `d ≥ 2` y
  **(iii)** cono IR isótropo en las coordenadas fijadas, `C_micro = conv F` es un
  politopo y no puede coincidir con una bola, luego `S ≡ 1` es **imposible**
  (ya registrado como `B_full` imposible en `theory/CAUSAL_BODY_GEOMETRY.md` §4).
  Esto es una afirmación sobre la clase congelada, **no** sobre cualquier sustrato
  concebible: relajar (i), (ii) o (iii) la deja abierta.
  La dicotomía útil es `Σ = ∅` (equivalentemente `c_IR < r_in(C_micro)`: bola
  estrictamente interior) frente a `Σ ≠ ∅` (equivalentemente `c_IR = r_in(C_micro)`:
  bola inscrita y tangente; `B_touch`). **ESTABLISHED en la clase (i)-(iii).**

**(e) No es artefacto de un paso.** Con `h_∞` de `CAUSAL_BODY_GEOMETRY.md` §6:
para cualquier `n̂`, el vértice `σ = (sgn n̂₁, sgn n̂₂, sgn n̂₃)` cumple
`n̂·σ = ‖n̂‖₁`, y al vértice `nσ` llega **un solo camino de red**, de modo que
`(W^n)_{nσ} = (W_σ)^n`. Verificado para los 8 vértices y ambos walks:
`‖(W_σ)^n‖ = 2^{-3n/2}` (walk 1) y `4^{-n}` (walk 2), nunca nulo. Luego
`h_∞(n̂) = v_sub(n̂) = ‖n̂‖₁` **exactamente**. **ESTABLISHED (derivado + numérico).**

## 2. Tarea 1 — `v_sub(n̂) = ‖n̂‖₁` para `[−1,1]³`

`F` calculado por FFT: walk (5.12) tiene exactamente los 8 vértices `(±1,±1,±1)`,
cada uno con `‖W_x‖ = 2^{-3/2}`; walk (5.15) tiene 14 saltos, entre ellos los 8
vértices. En ambos casos `C_micro = conv F = [−1,1]³`. El supremo es separable:

`h(n̂) = sup_{x∈[−1,1]³} Σᵢ nᵢxᵢ = Σᵢ sup_{xᵢ∈[−1,1]} nᵢxᵢ = Σᵢ |nᵢ| = ‖n̂‖₁`,

alcanzado en el vértice `xᵢ = sgn nᵢ`. Con `‖n̂‖₂ = 1`, Cauchy–Schwarz da
`1 = ‖n̂‖₂ ≤ ‖n̂‖₁ ≤ √3‖n̂‖₂ = √3`, con igualdad izquierda sólo si una única
componente es no nula y derecha sólo si `|n₁|=|n₂|=|n₃|`. Por tanto
`r_in([−1,1]³) = 1` y `V_causal^max = √3`. **ESTABLISHED.**

## 3. Tarea 2 — `S(n̂)` con `c_IR = 1`

`S(n̂) = 1/‖n̂‖₁ = 1/(|n₁|+|n₂|+|n₃|)`.

| dirección | `v_sub` | `S` |
| --- | ---: | ---: |
| eje `(1,0,0)` | `1` | `1` (saturación) |
| diagonal de cara `(1,1,0)/√2` | `√2` | `1/√2 ≈ 0.7071` |
| diagonal espacial `(1,1,1)/√3` | `√3` | `1/√3 ≈ 0.5774` |
| genérica `n̂` | `‖n̂‖₁` | `1/‖n̂‖₁ ∈ [1/√3, 1]` |

`Σ = {±e₁, ±e₂, ±e₃}`: seis direcciones, medida cero en `S²`. Como estadística
descriptiva, `S_min = 1/√3`.
Invariancia de escala: en coordenadas `k`, `c_IR = 1/√3` y los saltos BCC son
`(±1,±1,±1)/√3`, luego `S(n̂) = (1/√3)/(‖n̂‖₁/√3) = 1/‖n̂‖₁`, idéntico.

## 4. Tarea 3 — Clasificación del walk Weyl (5.12)

- **No es globalmente saturante** — y no por un accidente del modelo: ningún walk
  de rango finito en `d ≥ 2` puede serlo (§1d).
- **Satura exactamente en las 6 direcciones axiales.** En `p = (q,0,0)`:
  `ω = arccos(cos q) = |q|` y `∇ω = (sgn sin q, 0, 0)`, luego
  `c_IR = |v_g| = v_sub = 1`: allí coinciden las **tres** cantidades.
  La bola IR es la esfera inscrita en el cubo, tangente en los 6 centros de cara.
- **Estrictamente subsaturante en toda dirección no axial**, con déficit máximo
  `S = 1/√3` en las 4 diagonales espaciales.

## 5. Tarea 4 — La región de velocidades de grupo, por separado

`Γ₁` **no** es el frente causal; es un tercer cuerpo, intermedio.
Con `f = c1c2c3 + s1s2s3` y `B = −∇f`, el álgebra da (**derivado aquí**)

`B₁² + B₂² = s₁²c₂² + c₁²s₂² + 4PQ`, `1 − f² = 1 − P² + 2PQ − Q²` con `P = c1c2c3`, `Q = s1s2s3`,

de modo que `v₁² + v₂² ≤ 1` equivale a `s₁²c₂² + c₁²s₂² + (P+Q)² ≤ 1`, y como
`(P+Q)² = (c₁c₂·c₃ + s₁s₂·s₃)² ≤ c₁²c₂² + s₁²s₂²`, el miembro izquierdo es
`≤ s₁² + c₁² = 1`. Por simetría en los tres pares: **`Γ₁ ⊆` intersección de los
tres cilindros ortogonales**, coherente con el pie de la Fig. 5 de CJWW. La
rejilla 300³ satura la cota a `1.00000000` y llena el sólido, y

`max|v_g| = √(3/2) = 1.224745`, alcanzado en `v = ±(1,1,1)/√2`.

Lo que esto añade físicamente, y sólo esto: el walk 1 tiene un **sector balístico
superlumínico** respecto de `c_IR`. Modos a momento finito (lejos de los puntos
cónicos, fuera del alcance de la EFT) transportan peso de probabilidad `O(1)` a
velocidades hasta `1.2247 c_IR`. Es una afirmación sobre el contenido UV del
mismo walk, **no** sobre su estructura causal: `Γ₁` sigue estrictamente dentro
del cubo salvo en los ejes, donde `h_{Γ₁}(e₁) = 1 = v_sub(e₁)` (el tricilindro es
tangente a las 6 caras). Usar `max|v_g| = √(3/2)` como "velocidad causal" sería
un error en las dos direcciones a la vez: excede `c_IR` y queda por debajo de `√3`.

## 6. Tarea 5 — Segundo walk, Ec. (5.15)

`W` es unitaria con `det W = 1` y `tr W/2 = c1c2c3`, luego `ω = arccos(c1c2c3)`
(5.16), exacto. La identidad (5.17) admite un **certificado SOS exacto**
(derivado aquí, con `B = −∇f`):

`(1 − f²) − |B|² = s₂²s₃² + s₁²s₂²c₃² + s₁²c₂²s₃² ≥ 0`,

luego `|∇ω| ≤ 1` en todo punto. *Matiz sobre la fuente:* CJWW sitúan el máximo
"en los puntos cónicos"; el conjunto de igualdad del SOS es en realidad mayor —se
anula siempre que dos de los `pᵢ` estén en `πZ`—, de modo que `|∇ω| = 1` en las
**rectas axiales completas** que pasan por los puntos cónicos, no sólo en las
puntas. Es precisamente ese hecho el que hace saturar los ejes. `Γ₂` llena la bola
unidad (numérico), así que `Γ₂ = B(c_IR)` exactamente.

Y sin embargo: `F` contiene los 8 vértices `(±1,±1,±1)` con `‖W_x‖ = 1/4`
(el término `exp(i(p₁+p₂+p₃))` que el propio CJWW señala al justificar
`Ĩ(r) = ∞` para `r > √3`). Por tanto `C_micro = [−1,1]³` igual que antes y

`v_sub(n̂) = ‖n̂‖₁`, `S(n̂) = 1/‖n̂‖₁`, `Σ = {±eᵢ}`.

**La clasificación de saturación de los dos walks es idéntica.** `S` no los
distingue, porque `S` sólo depende de `c_IR` y de `C_micro`. Toda la diferencia
entre ellos vive en el cuerpo intermedio `Γ`. Resumen:

| | `B(c_IR)` | `Γ` | `C_micro` |
| --- | --- | --- | --- |
| walk (5.12) | bola de radio 1 | tricilindro, `sup\|v\|=√(3/2)` | cubo `[−1,1]³` |
| walk (5.15) | bola de radio 1 | **= bola de radio 1** | cubo `[−1,1]³` |
| soporte direccional en eje | 1 | 1 | 1 |
| soporte en diagonal espacial | 1 | `√(3/2)` / `1` | `√3` |

Respuesta a la tarea 5: **sí**, el frente causal microscópico sigue siendo
estrictamente mayor que `c_IR` en toda dirección no axial, por el factor
`‖n̂‖₁ ∈ (1, √3]`. **ESTABLISHED.**

## 7. Tareas 6 y 7 — La proposición

El walk (5.15) demuestra limpiamente el contenido de la proposición, pero la
proposición tal como está en la caja no es formulable: compara un escalar con
"el límite causal microscópico", que en un sustrato anisótropo no es un escalar.
Además, leída como "`c_IR` = el cuerpo causal", sería cierta por una razón trivial
e inútil: bajo las hipótesis (i)-(iii) de §1d, un politopo nunca es una bola.
Versión correcta, direccional:

> **Proposición (saturación axial, subsaturación genérica).**
> Para los walks CJWW (5.12) y (5.15) en `d = 3`, en unidades de un paso de red
> por paso de tiempo: `C_micro = [−1,1]³`, `h_∞ = v_sub = ‖·‖₁` y `c_IR = 1`, de
> modo que `S(n̂) = 1/‖n̂‖₁` vale `1` exactamente en las seis direcciones axiales y
> `< 1` en todas las demás, con mínimo `1/√3` en las diagonales espaciales.
> Para (5.15) esto se cumple **aunque** `Γ = B(c_IR)` exactamente, es decir aunque
> ninguna velocidad de grupo, a ninguna energía, exceda `c_IR` en ninguna dirección.
> Por tanto `sup_{p,j} |∇ω_j(p)| = c_IR` **no** implica `v_sub(n̂) = c_IR`.

## 8. Resultado físico (§4 del entregable)

> Un sustrato local discreto puede tener una relación causal microscópica
> estrictamente más ancha que el cono relativista emergente en casi toda
> dirección, aun cuando toda su dinámica balística —no sólo la de baja energía—
> respete `c_IR` exactamente. El walk CJWW (5.15) lo realiza: `Γ = B(c_IR)` y sin
> embargo `v_sub(n̂) = ‖n̂‖₁ c_IR`, hasta `√3 c_IR` en las diagonales. La
> saturación causal es direccional, se da sólo en las seis direcciones axiales, y
> `c_IR = r_in(C_micro)` es tangencia, no identidad de conos.

## 9. Riesgos conceptuales (§5 del entregable)

1. **Confundir `Γ` con el frente causal.** Son tres cuerpos anidados
   `B(c_IR) ⊆ Γ ⊆ C_micro` con tres estatus distintos. Dentro de `Γ`, peso de
   probabilidad `O(1)`. Entre `Γ` y `C_micro`, la propagación **no es balística** y
   puede estar exponencialmente suprimida —CJWW dan tasa positiva fuera de la bola
   `r = 1` para el walk (5.15)—; **no es, sin embargo, causalmente prohibida en
   general**. En particular, los ocho rayos de vértice tienen amplitud
   explícitamente no nula a todo `n`: `(Wⁿ)_{nσ} = (W_σ)ⁿ ≠ 0` (§1e). Fuera de
   `C_micro` la amplitud es exactamente cero. Sólo esta última frontera es causal.
   *Nota de alcance:* la cota exponencial de CJWW no afirma por sí sola que cada
   punto de la región intermedia tenga amplitud no nula; lo demostrado aquí es el
   enunciado sobre los vértices, que es el que hace falta.
2. **Escalarizar un cuerpo anisótropo.** Ni `max|v_g|` ni `V_causal^max = √3`
   ni el radio `r_in = 1` son "la velocidad del sustrato". El objeto primario es
   `h_{C_micro}(·)`; cualquier resumen escalar rompe la comparación en alguna
   dirección.
3. **Leer la tangencia como saturación.** `c_IR = r_in(C_micro)` sólo dice que la
   bola IR está inscrita y toca las caras; el conjunto `Σ` donde satura tiene
   medida cero en `S²`. Y "saturación global" no es un caso raro sino
   geométricamente imposible en la clase (i)-(iii) de §1d, así que no puede usarse
   como hipótesis discriminante. Ningún resumen escalar —ni `c_IR/r_in`, que vale
   `1` en los dos walks, ni `S_min`, que vale `1/√3` en los dos— separa (5.12) de
   (5.15): la diferencia entre ellos vive en `Γ`, no en `S`.
