<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 6c8f5d450f0c0c6ae1749fe3b948fae0b4f5b38010c379cdd112a70f77c575f6
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-29T16:57:23Z  fin: 2026-10-29T17:14:14Z
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step4b2.md ; último commit observado: 7c741df ; sha256 de la copia enviada 2f4bda870aeb367435484574f48cf6e5c3d6a7a07f94d61797a676fe1ddd266f
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step4b2.py ; último commit observado: 7c741df ; sha256 de la copia enviada 8849e87a0041205f9b9d4578c775fba728fe94706834f61ff8e46ab556aad1e3
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step4b1.md ; último commit observado: 014753e ; sha256 de la copia enviada 4444d54b4c43de073dd00eeb7f338c5bdfd23886d6fe2ab62a5269f45c1faaa5
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 785565c ; sha256 de la copia enviada 657fa6d3e9f17b69fedfde5d592d038b1eca90e90c496a8da1b43ffaa5ae8ea5
documento: /home/ignac/qca-causal-cones/theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md ; último commit observado: 05eb1eb ; sha256 de la copia enviada 2ef8690e5eb4c4e0799ae6c38038b988d0fe7f7ea64fdcc596095d5bab257e26
documento: /home/ignac/qca-causal-cones/biblioteca/1708.00826v2.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81
entrada_grok.txt sha256 859c1f782e3a621baa32aebe2f1e559063bbd43759dbf5b7e72692110fda0ce4
respuesta sha256 f88a55d165886f00e828a91e07e1089b36435635245c28ae82aae95ed2d1d48e
-->

Las cuatro conclusiones de la clase congelada se sostienen. La deducción de las 48 familias, los 16 puntos escalares, los cuatro nodos y `c_0 = c_strict^iso = rho_micro = 1/sqrt(3)` cierran a mano. No reejecuté el script: las igualdades de ideales que solo viven en la base de Gröbner quedan como no reproducidas aquí, y no hacen falta para el conjunto de soluciones.

**Supuestos.** La clase se representa por `ρ` = inclusión, como en 4b-1; una conjugación unitaria constante no cambia nodos, `c_0`, nilpotencia ni la Eq. (2). `N_3` es el del charter, `{ε/√3}`. La Eq. (2) es la de P17 p.2, `[U_l, A_h] ≠ 0` para `h ∈ S_+` y `l(h) ≠ h`. El lema del vértice se usa solo en la dirección que el erratum da por establecida. No doy por ejecutado nada de SymPy.

| # | Pregunta | Veredicto |
| --- | --- | --- |
| 1 | Parametrización, signo de `S_−`, biyección, cobertura de 4b-1 | Correcto |
| 2 | Sistema `R` (27), bases de Gröbner, independencia | `R` es necesario y suficiente; el principio de Gröbner es correcto; la igualdad de ideales no la reejecuté |
| 3 | Paso de `R` a 48 familias y el recuento `2·3·8` | Completo; no falta el caso nulo |
| 4 | Q-a, Eq. (2) y ruta (ii) | (i) implica la Q-a del charter y es más fuerte que la Eq. (2) literal; el párrafo a mano de (ii) tiene una laguna |
| 5 | 16 puntos, cuatro nodos, `H_j`, admisibilidad | Correcto |
| 6 | Lema del vértice, `h_∞`, mínimo, unidades | Correcto, con ambigüedad de notación en el informe |
| 7 | Alcance, «Consecuencia», P17 | Los resultados no exceden lo demostrado; la «Consecuencia» sí se puede leer de más |

## 1. Parametrización

El convenio de `S_−` es correcto, no un signo arbitrario mal cerrado. Con `h_0 = (−1,−1,−1)` y `T_{h_0} = c I + d·σ`, si `h = g h_0` entonces `g_j = −h_j`, luego `T_h = c I − Σ_j h_j d_j σ_j`.

La suma sobre los dos tetraedros da la identidad anunciada. Con `e^{−i q_j h_j} = c_j − i h_j s_j` y `χ = h_1 h_2 h_3`,

`e^{−iq·h} = C_0 + i χ S_0 − χ Σ_j h_j C_j − i Σ_j h_j S_j`.

Al sumar, los términos lineales en `h_j` se anulan en cada tetraedro (cuatro vértices, suma de cada coordenada cero). Queda

`α = 4(a+c)`, `β = 4i(a−c)`, `γ = −4(b+d)`, `δ = −4i(b−d)`,

con inversa `a = (α − iβ)/8`, `c = (α + iβ)/8`, `b = (−γ + iδ)/8`, `d = (−γ − iδ)/8`. Es una biyección lineal de los 16 parámetros reales. Cubre todo el espacio covariante de 4b-1: estabilizadores triviales, un punto base por órbita, y la conjugación constante ya estaba absorbida en 4b-1.

El testigo `e^{−iq_x σ_x} e^{−iq_y σ_y} e^{−iq_z σ_z}` es exactamente `κ = −1`, `ε = (1,−1,1)`, `η = (−1,−1,−1)`, `α = 1`: la parte escalar sale `C_0 − S_0` y los coeficientes de Pauli coinciden con `i(ε_j κ C_j + η_j S_j)`. Además `Σ ε_j η_j = −1`, así que cae dentro de las 48.

## 2. Unitaridad

`U = w I + v·σ` da, en `U^†U`,

`(|w|^2 + v̄·v) I + (2 Re(w̄ v) − 2 Im(v̄_k v_l)) · σ`,

con `(j,k,l)` cíclico positivo. La fórmula del informe es correcta. En dimensión finita `U^†U = I` ya implica `UU^† = I`; el segundo orden no añade soluciones.

Parte escalar. Los ocho monomios `C_0^2, S_0^2, C_j^2, S_j^2` son `Π_j u_j` con `u_j ∈ {c_j^2, s_j^2}`. En las ocho esquinas del cubo `t_j = c_j^2 ∈ {0,1}` la matriz de evaluación es la identidad, así que son independientes en el toro, y suman `1`. `C_0 S_0` es impar bajo `q_1 ↦ −q_1` y los cuadrados son pares. Por tanto

`|α| = |β| = |γ_j| = |δ_j| = 1`, `Re(ᾱ β) + Σ_j Re(γ̄_j δ_j) = 0`.

Parte de `σ_1`, con funciones

- `A = c_1^2 c_2 s_2 c_3 s_3 = C_0 C_1 = S_2 S_3`
- `B = s_1^2 c_2 s_2 c_3 s_3 = S_0 S_1 = C_2 C_3`
- `C = c_1 s_1 c_2^2 c_3^2 = C_0 S_1`
- `D = c_1 s_1 s_2^2 s_3^2 = S_0 C_1`
- `E = c_1 s_1 c_2^2 s_3^2 = C_2 S_3`
- `F = c_1 s_1 s_2^2 c_3^2 = S_2 C_3`

Independencia: en `q_1 = π/2` solo sobrevive `B`; en `q_1 = 0` solo `A`; en `q_1 = π/4` el bloque `{C,D,E,F}` es `c_1 s_1` por la base `{c^2, s^2}⊗{c^2, s^2}`, y las cuatro esquinas `(q_2,q_3) ∈ {0, π/2}^2` aíslan cada coeficiente. Igual para los otros dos índices por permutación. Igualar coeficientes reproduce exactamente las seis ecuaciones del informe. En total: 8 módulos + 1 cruce + 6·3 = 27. `R` corta el mismo conjunto real que la unitariedad.

La igualdad de bases de Gröbner reducidas, mismo orden y mismo anillo, sí equivale a la igualdad de ideales: la base reducida es única. El certificado compara `grevlex` sobre los 16 reales. Ese principio es correcto. No reejecuté el cálculo, ni reconté las 78 ecuaciones; el generador sí recorre todos los pares y ambos órdenes. Para clasificar soluciones basta la igualdad de conjuntos, que es el cálculo de arriba, no la igualdad de ideales.

## 3. Las 48 familias

No falta el caso nulo: `R` obliga módulo 1 a los ocho coeficientes complejos.

`|δ_j| = |α| = 1` y `Re(ᾱ δ_j) = 0` dan `ᾱ δ_j = ±i`, luego `δ_j = i η_j α`. La identidad

`|δ − iα|^2 |δ + iα|^2 = (|δ|^2 − |α|^2)^2 + 4 Re(ᾱ δ)^2`

sale al poner `α = 1`, `δ = x+iy`: ambos lados valen `(r^2 − 1)^2 + 4x^2`. Lo análogo con `Im(ᾱ β)` da `β = κα`. El mismo cálculo con `(γ, β)` da `γ_j = i ε_j β`.

Sustituyendo, `γ̄_k δ_l = ε_k η_l β̄ α`, así que `Im(γ̄_k δ_l) = 0` es `Im(β̄ α) = 0`, la misma condición en todos los pares. El cruce escalar queda

`κ(1 + Σ_j ε_j η_j) = 0`.

Como `κ = ±1`, `Σ ε_j η_j = −1`: de tres signos, eso es exactamente uno `+1` y dos `−1`. El resto de `R` se anula solo: `ᾱ γ_j = i ε_j κ` es imaginario puro, `δ̄_k δ_l = η_k η_l` es real, e igual las otras cuatro familias. No hay otra rama.

Recuento: `κ` (2) × índice del único producto `+1` (3) × `ε ∈ {±1}^3` (8), con `η` determinado. `2·3·8 = 48`. Sobre los 128 patrones, los `(ε,η)` con suma `−1` son 24, por 2 valores de `κ`. Las 48 circunferencias son disjuntas: todo `W_σ` vale `I` en `q = 0`, así que una fase relativa entre dos patrones obligaría a signos iguales.

Soporte activo: `a = α(1 − iκ)/8` y `c = α(1 + iκ)/8` tienen módulo `|α|√2/8 ≠ 0`. La traza es `2a` en `S_+` y `2c` en `S_−`.

## 4. Q-a

La Eq. (2) de P17, p.2, es `[U_l, A_h] ≠ 0` para `h ∈ S_+` y `l(h) ≠ h`. La glosa de esa página pide matrices de transición distintas, y con la covarianza `A_{l(h)} = U_l A_h U_l^†` ambas formas coinciden. El charter, familia P, restringe el predicado a `G × S_+`.

**(i)** En las 48 familias

`b_j = −α(η_j + i κ ε_j)/8`, `d_j = α(η_j − i κ ε_j)/8`.

Parte real y parte imaginaria son ambas no nulas, así que ningún `b_j` ni `d_j` se anula. Para `g ≠ e`, `T_{gh} = T_h` en `S_+` exige `b_j = 0` en los dos ejes que `g` cambia de signo, e igual con `d` en `S_−`. Luego `T_{gh} ≠ T_h` para todo `g ≠ e` y todo `h ∈ N_3`. `V4` mueve todos los vértices: ninguno de `N_3` tiene una coordenada cero. Esto implica la Eq. (2) y la Q-a del charter. Decir que eso *es* la Eq. (2) sobre todo `N_3` alarga el cuantificador: P17 y el charter paran en `S_+`.

**(ii)** Un representante por órbita basta. Para `g` fijo, `T_{gh} = T_h` no depende de `h`: es `b_j = 0` (o `d_j = 0`) en los ejes invertidos. Los seis ideales unidad, si la base es `[1]`, darían el vacío. No reejecuté esas bases. No hace falta: (i) ya cierra Q-a en toda la clase, no solo en los símbolos con nodo. Todos tienen nodo, así que el resultado del charter está cubierto.

El párrafo a mano no cierra como está escrito. El desplazamiento `gh − h` tiene exactamente los pares `(h, gh)` y `(−gh, −h)`, y la suma es

`T_h^† T_{gh} + T_{−gh}^† T_{−h} = 0`,

no `T_h^† T_h + T_{−h}^† T_{−h} = 0`. Contraejemplo del paso, no del teorema: `T_h = T_{gh} = |0⟩⟨0|`, `T_{−h} = |1⟩⟨1|`, `T_{−gh} = 0` da `|0⟩⟨0|` en la suma real y `I` en la expresión escrita. Dentro de la clase el hueco se repara: `T_{gh} = T_h` pone el vector de Bloch de `S_+` en el eje de `g`; el par antipodal `2h` y `s = 2` dan `T_h = λ P` y `T_{−h} = μ(I−P)`; eso anula las componentes transversas de `d`, y entonces `T_{−gh} = T_{−h}`. La suma pasa a `|λ|^2 P + |μ|^2 (I−P) = 0`, luego `λ = 0`.

## 5. Nodos

`U` es escalar si y solo si `ε_j κ C_j + η_j S_j = 0`. En `s = 2` un unitario es escalar si y solo si las dos cuasienergías coinciden, así que no hay otro punto de contacto de bandas.

Si algún `c_j = 0`, los tres se anulan. Con `c_1 = 0` la ecuación `j = 1` da `c_2 c_3 = 0`; si solo uno de ellos es cero, otra ecuación exige el seno correspondiente nulo, imposible. Si todos los `c_j ≠ 0`, dividir por `c_1 c_2 c_3` da `t_j + μ_j t_k t_l = 0` con `μ_j = κ ε_j η_j`. Un `t_j = 0` arrastra a los tres, y eso es `q ∈ {0, π}^3`, que sí cumple el sistema original. Si ninguno se anula, `t_j^2 = μ_k μ_l`, luego `μ_1 = μ_2 = μ_3`. Pero `Σ ε_j η_j = −1` impide que los tres productos, y por tanto los `μ_j`, sean iguales. Si todos los `c_j = 0`, el sistema se anula y `|a| = 1`. Los puntos escalares son exactamente esos 16, en toda familia.

Módulo `Λ^* = π{m : Σ m_j par}` en la coordenada `q` (el charter, pasado por `q = k/√3`):

- `{0, π}^3` cae en dos órbitas, `0` y `(π,0,0)`. La diferencia es `π m` con suma par o impar según la paridad del número de π.
- `{π/2, 3π/2}^3 = (π/2)(1,1,1) + π{0,1}^3` cae en dos, según la paridad de esa suma. `(π/2)(1,1,−1) ≡ (π/2, π/2, 3π/2)` porque `2π ℤ^3 ⊂ Λ^*`.
- Las cuatro están separadas: las diferencias entre estratos no están en `π ℤ^3`.

El covolumen de `Λ^*` es `2π^3` y el de `[0, 2π)^3` es `8π^3`, así que cada nodo del toro tiene cuatro representantes. `4 · 4 = 16`. No sobra ni falta ninguno.

En `{0, π}^3`, `W = C_0 I` y `∂W/∂q_r = i η_r C_0 σ_r`. Con `∂/∂k_r = ∂/∂q_r / √3` y `a_w = C_0 = ±1`,

`H_r = i C_0 · (1/√3) · i η_r C_0 σ_r = −η_r σ_r / √3`.

En `{π/2, 3π/2}^3`, `W = κ S_0 I` y `∂W/∂q_r = −i ε_r κ S_0 σ_r`, luego `H_r = ε_r σ_r / √3`. En ambos estratos la derivada escalar se anula. Como `λ_j = ±1`,

`H_j H_j = I/3`, `½ tr(H_j H_l) = δ_{jl}/3`, `tr H_j = 0`.

El generador lineal es `(1/√3) Σ λ_j p_j σ_j`, de espectro `±|p|/√3`, sin término en `I`. Cono isótropo, sin inclinación, sector completo de dos bandas, `c_0 = 1/√3` en los cuatro nodos de cada símbolo.

## 6. Cuerpo estricto

El erratum dice: si todo coeficiente de vértice es no nilpotente, entonces `C_∞^strict = C_micro` y vale la saturación. La recíproca no está establecida, y el informe no la usa. Cada vértice de `N_3` es extremo. Rango uno y traza no nula dan `T_h^2 = (tr T_h) T_h`, luego `T_h^n = (tr T_h)^{n−1} T_h ≠ 0`. Para rango uno, `tr T_h = ⟨v|u⟩`, que es la hipótesis del charter de 4b-2. El lema se aplica como está enunciado.

Con `h = ε/√3`,

`h_∞(q̂) = max_ε q̂·ε / √3 = |q̂|_1 / √3`.

En la esfera unidad, `|q|_1 ≥ |q|_2`, con igualdad solo en los ejes: el mínimo es `1/√3`. En la diagonal unidad vale `1`, que es el máximo, no el mínimo. El cuerpo es el cubo centrado `[−1/√3, 1/√3]^3`, así que `rho_micro = 1/√3`. El mismo `1/√3` sale de `∂/∂k` en el convenio del charter (con `ε` sin normalizar ambos lados escalarían por `√3`). `c_strict^iso = rho_micro = c_0`.

El informe escribe `h_∞(q̂) = max_h q̂·h` y el mínimo `1/√3`. Eso es correcto solo si `h` es el vértice ya dividido por `√3`. En los apartados 1–5 la misma letra es el signo `±1`. El certificado sí divide por `√3`. El número del informe coincide con el certificado; la frase, leída con los signos, daría mínimo `1`.

## 7. Alcance

No excede lo demostrado: una clase congelada, `d = 3`, `N_3`, `s = 2`, sin término on-site, `V4` de Pauli; Q-b abierto; las 48 familias no se identifican con la lista de P17; novedad abierta; el lema del vértice citado y no certificado por el script; evidencia preliminar. `RIGIDITY_PROVED_FOR_FROZEN_CLASS`, `SATURATION_PROVED_FOR_CLASS`, `ADMISSIBLE_SECTORS_EXIST` y `DISTINGUISHABILITY_IMPLIED_IN_CLASS` tienen el significado del charter y el dominio no está vacío. Vacío implica `VACUOUS` solo se enuncia para las otras clases, y el informe lo deja supeditado a que 4b-1 esté revisado.

La «Consecuencia» es lo que se pasa. «La Eq. (2) no restringe nada» es cierto dentro de la clase. «La clase queda dentro del marco de P17 con la Eq. (2)» es cierto solo como: cada símbolo cumple la Definición 1 y la Eq. (2) sobre `S_+`. No impone la normalización `Σ A_h = I` de P17, que es un cociente que el charter excluye del transporte, ni dice que las 48 circunferencias sean los dos paseos de Weyl salvo equivalencia. El párrafo de alcance lo niega; la «Consecuencia», que es el resultado que se lee primero, no.

La procedencia dice que la segunda ronda de 4b-1 sigue pendiente. El informe de 4b-1 ya la incorpora y da por cerradas sus dos objeciones. Es un desajuste de registro, no de la derivación.

## Reparaciones

| ID | Gravedad | Dónde | Qué cambiar |
| --- | --- | --- | --- |
| G-4B2-01 | Laguna | Informe, §4, ruta (ii), el párrafo «By hand» | La suma del desplazamiento `gh − h` es `T_h^† T_{gh} + T_{−gh}^† T_{−h}`. Hay que probar `T_{−gh} = T_{−h}` (Bloch transverso nulo en `S_−`) antes de escribir `T_h^† T_h + T_{−h}^† T_{−h} = 0`, y citar el par `2h` como origen del rango uno. La conclusión no cae: la ruta (i) ya da Q-a. |
| G-4B2-02 | Redacción | Informe, §4(i) y la «Consecuencia» | La Eq. (2) y el charter (familia P) cuantifican `h ∈ S_+`. El chequeo en `N_3` es más fuerte y es verdadero; no es el enunciado literal. |
| G-4B2-03 | Redacción | Informe, §6 | Escribir `h_∞(q̂) = \|q̂\|_1/√3` con `h = ε/√3`. Con la letra `h` de los apartados 1–5 el mínimo sería `1`, no `1/√3`. |
| G-4B2-04 | Redacción | Informe, «Consecuencia» | Limitarla a: unitariedad, covarianza y soporte activo implican la Eq. (2) sobre `S_+`, y la velocidad es `1/√3`. Quitar que la clase «queda dentro del marco de P17» sin decir que no se ha pasado por la Eq. (9) ni se han identificado las 48 familias con la lista de P17. |
| G-4B2-05 | Redacción | Informe, procedencia | La segunda ronda de 4b-1 no está pendiente: el informe de 4b-1 ya la recoge. Alinear la frase. |

## Veredicto global

**Sostenido, con reparaciones obligatorias antes de promocionar.** No hay un error que invalide las 48 familias, los cuatro nodos admisibles ni `c_0 = c_strict^iso = rho_micro = 1/sqrt(3)`. Q-a queda demostrada por la forma explícita en toda `N_3`, de sobra para el charter. La laguna G-4B2-01 es un paso escrito que no se sigue de lo que lo precede; el teorema de inconsistencia se recupera con el arreglo indicado. La «Consecuencia» no debe promocionarse tal como está: G-4B2-02 y G-4B2-04.
