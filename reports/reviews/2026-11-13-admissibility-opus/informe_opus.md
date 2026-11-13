<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.322 (Claude Code))
opus.json sha256 b18e87384029f5409482fa28820871c5f8123f825fb80863b2dd3740a600a28f
inicio: 2026-11-13T12:29:30Z  fin: 2026-11-13T12:35:24Z
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_ADMISSIBILITY_GATE.md ; último commit observado: ecc5827 ; sha256 de la copia enviada 375045b5b56f03c05e8a2192bd9b7f4fbabadfcf75f7425fa6315aaad5fdf70a
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_ADMISSIBILITY_GATE_AMENDMENT_1.md ; último commit observado: 156657e ; sha256 de la copia enviada e219a7b9823f965abb14cdcf482f89f860eeb0385f6de9c7045cd07555362dd8
documento: /home/ignac/qca-causal-cones/reports/2026-11-13--general-ir-admissibility-stage-a.md ; último commit observado: c740dbb ; sha256 de la copia enviada 0e654540b8c0a71921f6df42c254264ef346d2f2710172c643fb1ea22c140628
documento: /home/ignac/qca-causal-cones/reports/2026-11-13--general-ir-admissibility-active-encoders.md ; último commit observado: bb3592b ; sha256 de la copia enviada 56eb54cdbd040257346ff5ad9e175b667fc8589e134454d0b941c4ed2541d87c
documento: /home/ignac/qca-causal-cones/reports/2026-11-13--general-ir-admissibility-bravais.md ; último commit observado: 6ddda97 ; sha256 de la copia enviada ce8737e3c05fa76fad1131c57c16df3f3b2e0e1cac004b6f9fdfa4f500a81769
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-stage2-leading-term.md ; último commit observado: b7c720d ; sha256 de la copia enviada 8cd9a4d95eff380090289e2b2552a9d52caae7dfb17849b7e890be51443ae2b3
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-bravais-stage1.md ; último commit observado: 6516892 ; sha256 de la copia enviada 0b48e5b01faa1f3b3f81051ef529c23c6a938e5ddde0e57b865e48859b37678a
entrada_opus.txt sha256 8048dcbeac99ee0456bf2af43bb0f1a7d37f145aee49c6acf55f7bc4a90b9745
respuesta sha256 02797bc3ceb9c93446516af459c0f9921c18aae2ef3b4abc0fe30cdc1313ea7a
-->

# Revisión adversarial: admisibilidad infrarroja de codificadores activos en Z^d y en una red de Bravais fija

**Naturaleza de esta revisión.** Es una sola ronda, analítica, hecha sin herramientas. He rederivado a mano los pasos que se indican abajo. No he ejecutado ningún verificador, y una comprobación analítica mía no equivale a ejecutarlo. Los veredictos de los autores no se han usado como evidencia.

---

## Veredicto global: **PASS**, con alcance acotado

- **Bajo el cuantificador original de la carta** (todo miembro de una base hermítica arbitraria), la afirmación de admisibilidad **no vale**. El informe de Stage A lo establece correctamente: el contraejemplo `M = |v><v|`, con `v ⊥ χ`, da `Δ_M ≡ 0`, y entonces `η_enc` queda indefinida. Es un fallo de denominador, no de convergencia, y está bien clasificado.
- **Bajo los cuantificadores de la Enmienda 1** (codificadores activos `Mχ ≠ 0` y proyectores detectores no nulos), las tres razones están definidas para N suficientemente grande y son `O(N^(-1/2))`, tanto en `Z^d` como en cada red de Bravais fija de rango completo. Las constantes y umbrales dependen de los datos fijos y de la red. No se afirma uniformidad indebida.
- **El enlace condicionado con B1 es válido como implicación.** La eliminación de los miembros nulos es legítima. Además, es más robusta de lo que el informe argumenta, porque no depende de la forma concreta del coeficiente principal (ver Bloque D).

No encuentro errores fatales ni huecos obligatorios. Las objeciones de abajo son huecos menores de redacción o mejoras expositivas opcionales.

El PASS se refiere solo a esta ronda. El enlace hereda el estado de revisión de B1: el Doc 6 depende de las Enmiendas 3–6, no adjuntas, y las reparaciones del Doc 7 no han sido re-revisadas. Este dictamen no constituye base para promoción.

---

## Separación entre lo rederivado y lo asumido

**Rederivado por mí:**
- Normalización de Fourier y `c_d`.
- Factor `sqrt(v_L)`.
- Valor de `c_r(Z^3)`.
- Analiticidad de Φ y masas locales.
- Estimación de multiplicadores en `Z^d` y en Bravais, con los factores β, `B_op` y `B_F`.
- Representación del toro y complemento de Π'.
- Identidad de rango uno del numerador de estado.
- Identidad de traza y suma doble.
- Denominadores de operador mediante estados trasladados.
- Casos de fase escalar, Pauli y generador nulo.
- La propiedad exacta de que un miembro nulo anula toda la señal y todo orden de su expansión.

**Asumido de B1 (Docs 6 y 7) y de documentos no adjuntos, sin verificar:**
- (i) La conclusión de B1 tiene la forma «existe un par básico `(M_i, M_B,j)` de la familia fija con `limsup e^(K_* N) N^(5+d/2) δ(N) > 0`», donde δ(N) es la señal real con el codificador exponencial.
- (ii) Para cada par fijo, `L_N = -2 Im Z_1 + (términos de orden inferior)`, según el progress record (SP), no adjunto.
- (iii) La existencia de un testigo en el span real con limsup positivo, que depende de H5–H7, H9, H10 y de las Enmiendas 3–6.
- (iv) La transferencia Bravais de estas afirmaciones (Doc 7, §§1–4, §7).
- (v) El contenido real de la Definición 3.1 del manuscrito: uso la reformulación de la carta.
- (vi) La elección «F ≥ 1/2» del manuscrito en el chequeo Pauli.
- (vii) Que la clase B1 admita bases hermíticas arbitrarias.
- (viii) Los commits, autorizaciones y tiempos citados.

---

## Bloque A — Stage A (Doc 3): numeradores, denominadores de operador y obstrucción nula

**Dictamen: correcto.** La parada por la regla de cambio de clase es procedente.

### 1. Multiplicador
- Para `|x| ≤ π` se cumple `|sin(x/2)| ≥ |x|/π`. Por tanto, en `[-π,π]^d`, `G(p) = Σ 4 sin²(p_j/2) ≥ 4|p|²/π²`.
- Como la bola de radio `N^(-1/2) ≤ 1 < π` está dentro de la celda para todo N ≥ 1, se obtiene `||(I-Π')f|| ≤ (π/2)√N (Σ_j ||D_j f||²)^(1/2)`.
- Regla del producto: `D_j(aΠψ) = (D_j a)·τ_j Πψ + a·D_j Πψ`.
  - El primer término aporta `≤ √d·L/N·||ψ||`.
  - El segundo aporta `≤ A·(∫_{|p|≤1/N} G|ψ̂|²)^(1/2) ≤ A/N·||ψ||`, usando `|e^{ix}-1| ≤ |x|`.
- Resultado: `(π/2)(A+√d L)N^(-1/2)`. Confirmado. No depende de s.

### 2. Constantes A y L
- Para M hermítica, `||e^{iθ₁M} - e^{iθ₂M}|| = max_λ |e^{iθ₁λ} - e^{iθ₂λ}| ≤ ||M||·|θ₁-θ₂|`. Con `θ = πF/2`, esto da `L ≤ (π/2)||M|| L_F`.
- `F = (1-s)_+²` es C¹ en todo `R^d`, con gradiente nulo en la esfera y `|∇F| ≤ 8/(3√3 r_A)`. Por tanto es globalmente lipschitziana, y `L_F` es finito también a través del borde.

### 3. Denominadores de operador
- La prueba con el recurso trasladado a `z_N`, con `|z_N - N w_0| ≤ √d/2`, y vector interno v autovector de autovalor λ ≠ 0, da `(U_M - I)ψ = (e^{iπλF_N/2} - 1)ψ` punto a punto.
- La traslación por un punto de red multiplica `ψ̂` por una fase y preserva la banda, de modo que `Πψ = ψ`.
- Como `z_N/N → w_0` y `Φ(0) > 0`, la masa en una caja pequeña alrededor de `w_0` está acotada inferiormente.
- No se supone que Alice esté cerca del origen.
- Este denominador está definido también para miembros nulos con `M ≠ 0`. Solo `η_enc` queda indefinida.

### 4. Obstrucción
- `Mχ = 0` implica `M^kχ = 0` para todo k ≥ 1, luego `e^{iθM}χ = χ` sitio a sitio.
- `{I, σx, σy, diag(0,1)}` es base real, porque `σz = I - 2·diag(0,1)`.
- **Comprobación independiente propia:** para s = 3, la base `{I} ∪ {Gell-Mann}` con `χ = e_3` (si ese vector está en el espacio nodal declarado) tiene tres miembros nulos: λ₁, λ₂ y λ₃.
- El subespacio `{M : Mχ = 0}` tiene dimensión real `(s-1)²`. Por tanto, los miembros nulos son no genéricos pero permitidos, y la obstrucción no es exótica.

---

## Bloque B — Codificadores activos en Z^d (Doc 4)

**Dictamen: correcto.**

### 1. Fourier y `c_d`
- Con `φ̂ = Z^(-1/2) g(Np) χ` y medida `dp/(2π)^d` se obtiene `Z = N^(-d)(2π)^(-d) J_2`.
- De ahí `φ_N(x) = N^(-d/2) (2π)^(-d/2) J_2^(-1/2) ∫ g(q) e^{-iq·x/N} dq χ`, es decir, `c_d = (2π)^(-d/2) J_2^(-1/2)`.
- La igualdad `Σw_x = 1` es exacta por Parseval, porque el soporte `|p| ≤ 1/N` está dentro de la celda para N ≥ 1.
- **Contraste independiente:** `∫_0^1 (1-r²)^4 r² dr = 128/3465`. Por tanto `J_2 = 512π/3465` en d = 3 y `c_3 = √3465/(64π²)`, que coincide con el Doc 7, §4.

### 2. Analiticidad y masas
- Φ es la transformada de una función integrable de soporte compacto, luego es entera.
- Si se anulara en un abierto, todas sus derivadas se anularían en un punto. La serie de Taylor de una función entera converge en todo `C^d`, así que Φ ≡ 0, en contradicción con `Φ(0) = c_d ∫g > 0`. Esto es más directo que el argumento por cadenas de vecindades, que también es válido.
- Conteo: cada intervalo `[N a_j, N(a_j + l_j)]` contiene `≥ ⌊N l_j⌋ ≥ N l_j/2` enteros si `N l_j ≥ 2`. De ahí `masa ≥ b_Q² ∏(l_j/2)`.
- La afirmación correcta, y la que se usa, es que todo abierto **contiene** una subcaja con masa positiva. No se afirma lo mismo para toda caja.

### 3. Denominador de estado
- `<φ_N(x), U_M(x) φ_N(x)> = w_x t(x/N)`, porque `F_N(x) = F(x/N)` exactamente.
- Como `|z|²` es real y `Σ w_x w_y = 1`, se tiene `1 - |z|² = Σ w_x w_y (1 - Re t_x t̄_y)`, con cada sumando `≥ 0` porque `|t| ≤ Σp_λ = 1`.
- En `Q_out` se cumple `t = 1`, ya que `F = 0` fuera de la bola abierta, esfera incluida. Para `x ∈ Q_in` e `y ∈ Q_out`, el corchete vale `1 - Re t_x ≥ ε` en ambos órdenes, lo que da `2ε m_in m_out`.
- **Actividad:** `Mχ ≠ 0` equivale a que exista λ ≠ 0 con `P_λ χ ≠ 0`.
- Los valores excepcionales `f = 4k/λ_*` forman un conjunto discreto, y F alcanza todo `f ∈ (0,1)` en el interior de A.
- La fórmula `||Δ||_1 = 2√(1-|z|²)` para proyectores de rango uno es correcta.
- **Casos de control:**
  - Fase escalar `Mχ = λχ`: `t = e^{iλθ}` y la cota es positiva. Una fase espacialmente variable no es una fase global.
  - Pauli: `e^{iθM} = cos θ + i sin θ M`, luego `Re t = cos θ ≤ 1/√2` donde F ≥ 1/2. El valor `ε = 1 - 1/√2` es correcto, aunque la referencia al manuscrito no es verificable.
  - Generador nulo: `p_λ = 0` para todo λ ≠ 0, de modo que no se afirma cota alguna. Esto es coherente.

### 4. Numerador de estado
- La identidad de rango uno es correcta: `|v><v| - |w><w| = |r><v| + |w><r|`. La cancelación de los términos en φ requiere `Π'φ = φ`.
- Ver la objeción O1 sobre el paso intermedio.

### 5. Hipótesis y uniformidad
- No interviene H1–H10, ni la dinámica de la marcha, ni d ∈ {2,3}: el lema vale para todo d.
- No se afirma uniformidad cuando `Mχ → 0`. Correcto.

---

## Bloque C — Transferencia Bravais (Doc 5)

**Dictamen: correcto.**

### 1. Isometría
- Con `x = Bn` y `t = Bᵀp`: `p·x = t·n`, `dp = dt/v_L` y `dμ_L = dt/(2π)^d` sobre `R^d/2πZ^d`. Confirmado.

### 2. Celda y complemento de Π'
- Si `|p| < π/max|b_j|`, entonces `|b_j·p| < π`. La bola queda en el interior de `P_B`.
- Como `P_B` es un dominio fundamental, todo punto del toro fuera de la imagen de la bola tiene su representante en `P_B` con `|p| ≥ N^(-1/2)` y `|t_j| ≤ π`. Por tanto `G ≥ (4/π²)|Bᵀp|² ≥ (4β²/π²)|p|²`, con `σ_min(Bᵀ) = σ_min(B) = β`.
- Umbral: `N > max_j |b_j|²/π²`.

### 3. Factores de B
- En la banda de entrada, `G ≤ |Bᵀp|² ≤ B_op²/N²`, lo que da el término `A_0 B_op`.
- `||D_j a_N|| ≤ ℓ|b_j|/N`, y `(Σ_j ℓ²|b_j|²)^(1/2) = ℓ B_F`, lo que da el término `ℓ B_F`.
- Constante: `(π/2β)(A_0 B_op + ℓ B_F)`. Confirmado.
- Casos de control:
  - `B = I`: se recupera Stage A.
  - `B = aI`: la constante es independiente de a y el umbral depende de a. Correcto.

### 4. Normalización
- `Z_{N,L} = v_L (2π)^(-d) N^(-d) J_2`.
- `φ = Z^(-1/2) v_L (2π)^(-d) N^(-d) ∫ g e^{-iq·x/N} χ = √v_L N^(-d/2) Φ(x/N) χ`.
- Masa: `v_L b² ∏(l_j/2) = b² vol(Q)/2^d`, que equilibra correctamente `v_L` frente a la densidad `1/v_L`.

### 5. Punto de red cercano
- `|B(n - s)| ≤ ½ Σ|b_j|`. Correcto.
- Los umbrales dependen de la red (`r_B`, `l_j`, `Σ|b_j|`) y se declaran como tales. No hay uniformidad sobre redes que degeneren.

---

## Bloque D — Enlace condicionado con B1 (Doc 4 §5 y Doc 5 §5)

**Dictamen: válido como implicación condicional.** La eliminación de los miembros nulos es legítima.

### 1. Bilinealidad frente al codificador no lineal
- La señal δ(N) del par básico usa el codificador exponencial real y **no** es bilineal.
- B1 solo aplica la bilinealidad a `Im Z_1`. El testigo `M = Σ a_i M_i` del span nunca se realiza físicamente: `exp(iθ Σ a_i M_i)` no es una combinación de los `U_{M_i}`, y no necesita serlo.
- De «limsup positivo de `Im Z_1` escalado para el testigo» se deduce lo mismo para algún par básico, y luego la conclusión sobre δ(N) para **ese** par mediante la hipótesis asumida (ii).
- El lema de admisibilidad se aplica a ese mismo par con su codificador exponencial. No hay desajuste.

### 2. Eliminación de los miembros nulos (rederivado)
- La perturbación de primer orden es `f_1 = θ φ_N Mχ`, que depende de M solo a través de Mχ.
- Por tanto, si M es nulo, tanto la contribución a Mχ como `Z_1` se anulan **exactamente**, no solo en el coeficiente principal.
- Además, `{Mχ : M ∈ span real de la base} = {Mχ : M ∈ span real de los miembros activos}`, de modo que la construcción del testigo de B1 (`Mχ = v`) no se ve afectada.
- **Argumento más fuerte y más simple:** `U_M φ_N = φ_N` implica que la señal, `Z_1`, `Z_2` y `Q_N` se anulan para todo N. Si `M_B = 0`, la señal también es cero. Por tanto, **cualquier** par con `limsup δ(N) > 0` es activo y tiene detector no nulo. Esto solo depende de la forma (i) de la conclusión de B1, no de la estructura `(R̃†M_B e_k)(f_k†Mχ)` ni de las Enmiendas 5–6.

### 3. Transferencia Bravais
- La misma lógica vale sin cambios, porque la distinción activo/nulo es interna.
- Dependencia asumida: la transferencia Bravais de (i) y (ii) en el Doc 7, no re-revisada.

---

## Bloque E — Contrato, excepciones y afirmaciones

- **Contrato:**
  - Stage A se detuvo en el cambio de clase.
  - La Enmienda 1 se aprobó antes de continuar.
  - No se sustituyen matrices ni se impone `M² = I`.
  - Los ratios indefinidos se registran y no se etiquetan como contraejemplos de convergencia.
  - No se usan cómputos ni se modifican verificadores.
  - Stage B cita una autorización separada. Esto no es verificable, pero es coherente con la carta.
- **Hipótesis ocultas:** ninguna con efecto. Se usa que los detectores son proyectores ortogonales (para `||P|| = 1` y para que exista un vector unitario en el rango). La extensión a efectos `0 ≤ E ≤ I` sería inmediata, pero no se pide.
- **Afirmaciones más fuertes de lo demostrado:** ninguna sustantiva. Ver O3 y O4, que son de redacción.
- **Tiempos:** los registros de 66 y 78 segundos no son evidencia en ningún sentido y no afectan a la evaluación matemática.

---

## Objeciones

**Obligatorias (errores fatales o huecos de prueba):** ninguna.

**Huecos menores de redacción.** Recomiendo repararlos, pero no condicionan el veredicto.

- **O1 — Numerador de estado.**
  - *Localización:* Doc 3 §2 («`≤ 2||r|| = O(N^(-1/2))`») y Doc 4 §4.
  - *Derivación omitida:* `r = (I-Π')U_M φ_N = (I-Π')(U_M - I)Π φ_N`, usando `Πφ_N = φ_N` (banda `|p| ≤ 1/N`) y `(I-Π')φ_N = 0`. De ahí `||r|| ≤ ||(I-Π')(U_M - I)Π|| ≤ C_M N^(-1/2)`.
  - *Reparación mínima:* añadir esa línea.

- **O2 — Formulación del enlace.**
  - *Localización:* Doc 4 §5, «B1's selected non-vanishing basis pair».
  - *Problema:* B1 no selecciona un par, sino que afirma existencia. El argumento de «eliminar términos cero» es correcto pero innecesario.
  - *Reparación mínima:* sustituirlo por «todo par básico con `limsup` escalado positivo de δ(N) es activo y tiene `M_B ≠ 0`, porque los miembros nulos dan señal idénticamente nula», y enumerar explícitamente las dependencias (i)–(iv).

**Mejoras expositivas opcionales.**

- **O3.** Doc 4 §5: «every member of an unrestricted basis has defined ratios remains false» debería decir «falla para algunas bases permitidas». Vale para bases sin miembros nulos, como las de Pauli con s = 2, y es genéricamente cierto.
- **O4.** Doc 4 §1: indicar explícitamente que, para miembros nulos, `η_op(U_M - I)` sí está definida y es `O(N^(-1/2))`. Solo `η_enc` queda indefinida.
- **O5.** Doc 5: hay colisión de notación. B designa la matriz de la red y también la bola de Bob, y `r_B` designa tanto el radio recíproco como el radio de Bob en la carta.
- **O6.** Doc 4 §4: marcar el chequeo Pauli como consistencia dependiente del manuscrito (F ≥ 1/2), no como recuperación demostrada.
- **O7.** Doc 3 §3: «for sufficiently large N the momentum ball lies inside the cell» vale para todo N ≥ 1. La notación `||(D_jΠf)_j||` debería explicitarse como norma de suma directa.
- **O8.** Etiquetar la compatibilidad como «PROVED…, conditional» es aceptable, pero conviene un rótulo que no se confunda con una prueba incondicional, dado que B1 tiene partes no re-revisadas.

---

## Conclusión

Las tres razones de fuga son `O(N^(-1/2))` con denominadores positivos para N suficientemente grande, para todo codificador activo y todo proyector detector no nulo, en `Z^d` y en cada red de Bravais fija. Las constantes y umbrales dependen de los datos fijos y de la red. Para la familia sin restricción la afirmación falla por denominador indefinido, como reportan los autores.

El enlace con B1 es una implicación válida que solo requiere la forma de la conclusión de B1 y el control por par de los términos de orden inferior. Ambos se asumen y no se han verificado aquí.
