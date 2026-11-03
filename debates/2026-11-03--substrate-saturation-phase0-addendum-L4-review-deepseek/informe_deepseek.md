<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 e520fe652281aa330395af9c5ab8bfd4b346fe72e52a5825053863c72234e700
inicio: 2026-11-03T18:15:22Z  fin: 2026-11-03T18:18:45Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0-addendum-L4.md ; último commit observado: 3e20c70 ; sha256 de la copia enviada 39a6d17ac369c92fac97250f46f0ba0dec4e4f65fe9feee3dc434a13da0fc174
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0.md ; último commit observado: 2f6160e ; sha256 de la copia enviada 3b88e925ec75a3efb81bb13ba9f07c1d4ca4cd2fef374bc9b9627ee312621676
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-addendum-L4-review-deepseek/cjww_pp17-18.txt ; último commit observado: sin versionar ; sha256 de la copia enviada fb9abfc2c21693729a348394112d6e910aa1538a3445674e07f24d3f414b61e9
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-addendum-L4-review-deepseek/extracto_current_state.md ; último commit observado: sin versionar ; sha256 de la copia enviada 17f9d76633ce4e5c5d8f3118bb87e6397c9fed77985d5d706a19b415d67e271f
entrada_deepseek.txt sha256 cfed8a5a9028d3e4285d91c19e5bce3534bde65757338933aa5428a3d67a0bb5
respuesta sha256 1b752a245e043a860c89adf27173c6541904c12504ec9848ef8682341dbdacbd
-->

## Dictámenes separados

### 1. FUENTE — **PASS con salvedad documental**

Lo verificable en el extracto adjunto es correcto:

- La transcripción de **(5.15)** coincide literalmente con `DOC 4`.
- La transcripción de **(5.16)** también coincide:  
  `ω(p) = arccos(cos p1 cos p2 cos p3)`.
- El texto sobre **determinante 1** está bien leído: el extracto dice literalmente que la continuación analítica de `W` “is still a 2×2-matrix with determinant 1”.
- La lectura de los **puntos cónicos** es compatible: el propio texto dice que el modelo (5.15) tiene “exactly the same conical points p∨” y luego identifica esos puntos por `c1 = c2 = c3 = 1`, es decir `p_i ∈ πZ`.

Salvedad: el extracto suministrado (`DOC 4`) no contiene las líneas literales de **(5.12)** ni **(5.14)**; empieza después de (5.14). Por tanto, no puedo cotejar literalmente esas dos ecuaciones. La lectura de (5.14) como errata tipográfica es sustantivamente correcta si la impresión es la que declara el addendum: la forma corregida `p_1^2 + p_2^2 + p_3^2` es la única compatible con isotropía. Cierre: adjuntar las líneas literales de (5.12)–(5.14), sin rehacer nada.

No hay defecto de transcripción detectable en lo adjunto.

---

### 2. DERIVACIONES — **PASS**

Rehechas a mano:

#### (5.12), `W(p) = e^{i p_1 σ_1} e^{i p_2 σ_2} e^{i p_3 σ_3}`

- `W(0) = I`, escalar: correcto.
- `∂_a W(0) = i σ_a`: correcto, porque cada factor es  
  `cos p_a + i sin p_a σ_a`.
- `T_a = i ∂_a W(0) = −σ_a`: correcto.
- Hermiticidad y traza nula: correcto, `σ_a` son Hermíticas y de traza nula.
- `{T_a, T_b} = {−σ_a, −σ_b} = {σ_a, σ_b} = 2 δ_ab I`: correcto.
- `c_0 = 1`: correcto.

No hay error de signo ni factor.

#### (5.15)

- `W(0) = I`: correcto.
- Derivadas en `p = 0`:
  - `∂_1 W(0) = i σ_1`: correcto.
  - `∂_2 W(0) = −i σ_2`: correcto; el addendum no se equivoca en este signo.
  - `∂_3 W(0) = i σ_3`: correcto.
- Por tanto:
  `T = (T_1, T_2, T_3) = (−σ_1, σ_2, −σ_3)`: correcto.
- Hermiticidad y traza nula: correctas.
- Anticonmutación y cuadrados:
  `{T_a, T_b} = 2 δ_ab I`: correcto, los signos no alteran las relaciones de Clifford.
- `c_0 = 1`: correcto.

#### Unitaridad de (5.15) para `p` real

También es correcta. Para la primera fila,

`|w_11|^2 + |w_12|^2 = cos^2 p_1 cos^2 p_2 + cos^2 p_1 sin^2 p_2 + sin^2 p_1 = 1`.

La segunda fila da lo mismo. La ortogonalidad se cumple porque la segunda fila es de la forma  
`(−\overline{w_{12}}, \overline{w_{11}})`, salvo conjugación global, lo que anula el producto escalar fila-fila.

**Única imprecisión no bloqueante:** en §2, para (5.12) y (5.15), el addendum dice:

> “Traceless plus (iv) gives `A(n)^2 = |n|^2 I`”.

En realidad `(iv)` sola ya da `A(n)^2 = |n|^2 I`, porque `{T_a,T_b} = 2 δ_ab I` implica `T_a^2 = I` y anula los términos cruzados. La traza nula no es necesaria para esa conclusión. Es una aclaración, no un error de factor ni de signo, y no afecta a ninguna cláusula.

---

### 3. CORRESPONDENCIA CON EL CONTRATO — **PASS**

Las cláusulas (i)–(v) cubren la condición algebraica congelada de nodo isótropo sin inclinación:

- (i) `W(0) = I` cubre `U(0)` escalar.
- (ii)–(iii) cubren término lineal Hermítico y traceless.
- (iv) cubre `{T_a, T_b} = 2 c_0^2 δ_ab`, con `c_0 = 1`.
- (v) cubre la forma equivalente `A(n)^2 = c_0^2 |n|^2 I`, declarada en el contrato.

No falta la hipótesis del nodo en `k = 0`: el addendum usa `p = 0`, que es el nodo sin masa en ambos modelos. La convención de signo del momento no afecta a las cláusulas; cambiar `p → −p` cambia el signo global de `T_a`, pero no la hermiticidad, la traza, el álgebra de Clifford ni `A(n)^2`.

**Advertencia formal, no matemática:** la condición congelada del contrato también exige que el modelo pertenezca a una clase declarada. Las cláusulas (i)–(v) no demuestran por sí mismas la pertenencia de L4 a una de las clases congeladas; solo demuestran la parte algebraica del nodo. El addendum es explícito en que no reclasifica L4 ni se usa como resolución dentro de la auditoría. Por tanto, no hay contradicción con el contrato.

---

### 4. SOPORTE Y UNIDADES — **PASS**

La afirmación de que el soporte compuesto contiene `(±1, ±1, ±1)` en ambos walks es correcta:

- **(5.12):** es producto de tres factores, cada uno con pasos `±e_a`. El paso compuesto es `sum_i ε_i e_i`, con `ε_i ∈ {±1}`, de modo que los ocho vértices `(±1, ±1, ±1)` están presentes.
- **(5.15):** los términos diagonales `cos p_1 cos p_2 e^{± i p_3}` generan todas las frecuencias `(ε_1, ε_2, ±1)` con `ε_1, ε_2 ∈ {±1}`. No aparecen frecuencias con componentes mayores que 1.

Por tanto, `C_micro = [−1,1]^3` y `r_in = 1` en unidades CJWW.

El reescalado es correcto:

- paso más largo crudo: `√3`;
- dividir longitudes por `√3` convierte el cubo en `[−1/√3, 1/√3]^3`;
- `r_in = 1/√3`;
- `c_0` crudo `1` se reescala a `1/√3`.

Así se obtiene el par `(1/√3, 1/√3)`.

La afirmación de que la fuente de L4 sigue siendo `l. 147` es correcta en el alcance del addendum: el propio addendum dice que el reescalado se enuncia “only to show consistency” y no modifica la tabla ni reclasifica L4. No detecto cruce ilegítimo de unidades entre CS Sec. 8 y la tabla `c-across-lattices`.

---

### 5. ALCANCE — **PASS**

El addendum deja intactas las salidas de la auditoría:

- mantiene `OPEN_AFTER_ROW_SURVEY`;
- mantiene L4 sin clasificar;
- mantiene los dos `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`;
- no se presenta como evidencia para `(PH)`;
- no se presenta como resolución de L4;
- condiciona cualquier uso a una enmienda y a revisión independiente.

La frase final de §3:

> “If this derivation were independently reviewed and adopted by an amendment, L4 would be an admissible row…”

está calificada como provisional, no ejecutada, y no modifica el estado actual. Por tanto, no invade el alcance del contrato.

---

## Dictamen global: **PASS**

No encuentro errores de signo, factor, fuente, alcance ni correspondencia que obliguen a reparar el addendum.

**Reparaciones obligatorias:** ninguna.

**Salvedad no bloqueante:** para cerrar por completo la verificación literal de fuente, faltaría adjuntar las líneas exactas de (5.12) y (5.14), ausentes del extracto `DOC 4`; no es un defecto demostrado del addendum.
