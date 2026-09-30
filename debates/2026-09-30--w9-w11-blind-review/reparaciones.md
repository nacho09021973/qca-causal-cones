# Reparaciones W9–W11 tras la revisión ciega — 2026-09-30

Para: Astra (autor de W9–W11 en `research/gravitational-normalization-gate`).
Fuente: `informe_deepseek.md`, `informe_opus.md` (esta carpeta) y la comprobación
`verify_reviewer_claims.py`. Veredictos: ninguna puerta rechazada; W10 y W11
`ACCEPT_WITH_REPAIRS` por ambos revisores; W9 `ACCEPT` (DeepSeek) / `ACCEPT_WITH_REPAIRS` (Opus).

Etiquetas de estado de cada reparación:
- **VERIFICADO**: comprobado en esta sesión por `verify_reviewer_claims.py` o leyendo el fichero
  y el orden de commits que se citan.
- **AMBOS**: lo piden los dos revisores (DeepSeek y Opus).
- **OPUS** / **DEEPSEEK**: lo pide uno solo; sin comprobar, salvo que se diga otra cosa.
  `[UNVERIFIED]` hasta que el autor lo derive.

Reglas: no se reescribe ningún commit congelado. Cada reparación va como addendum fechado en el
informe correspondiente (y en `state/CURRENT_STATE.md` de la rama), citando esta carpeta. Si un
veredicto baja, se dice explícitamente qué cambia.

## A. Bloqueantes para el siguiente gate (JOINT EINSTEIN–WEYL)

Sin estas, el gate conjunto parte de una fuente de materia mal planteada.

**A1. Cuatro nodos Weyl, no uno (W11 F1/F2). VERIFICADO. OPUS.**
`W = +I` en `(0,0,0), (π,π,0), (π,0,π), (0,π,π)` y `W = −I` en las otras cuatro esquinas de
`{0,π}³`. Los marcos lineales en los nodos `+I` tienen signos de determinante `−,+,−,+`:
quiralidad neta 0. El sector de cuasienergía baja son cuatro especies Weyl, más cuatro nodos π.
- Reparar: F1 dice "the low-energy matter generator is the expected Weyl Hamiltonian"; limitarlo a
  un entorno de `p = 0` y registrar los ocho nodos.
- Decidir y justificar una de dos: (i) acoplar la geometría a las cuatro especies; (ii) probar que
  una geometría suave (`|q| ≪ π`) suprime la dispersión entre nodos hasta un orden declarado.
- Cierre: tabla de nodos con marco y quiralidad, y la opción elegida con su cota o su contrato.

**A2. `H_IR` tiene doblones y no se conserva (W11 F2). VERIFICADO. OPUS.**
`[H_IR(p), W(p)] = O(|p|⁴)` y no nulo, así que `Σ_x H_IR` deriva bajo el walk exacto. `H_IR` se
anula en las ocho esquinas: asigna energía 0 a estados de cuasienergía π. Según Opus, en
`(π,π,0)` tiene la quiralidad opuesta a la del walk (esto último sin comprobar).
- Reparar, en orden de preferencia:
  - (a) usar `K = i(U − U†)/2`: local, hermítico y `[K, U] = 0` exactamente (VERIFICADO), con
    `K − H_eff = O(|p|³)` (VERIFICADO);
  - (b) mantener `H_IR` y acotar su no conservación en tiempo `t` para estados de banda estrecha.
- Cierre: F2 reescrito sobre `K`, o cota explícita, y el certificado actualizado.

**A3. `T^{0i}` y `T^{ij}` no son los de Belinfante (W11 F2, W9 B3, W10 C3). AMBOS (Opus más fuerte).**
- `π_i` es la densidad canónica. Según Opus, `T^{0i}_Bel = P^i_can + ½(∇×S)^i`, con
  `S = ψ†σψ/2`, y el término de rotacional es del mismo orden que el canónico en banda estrecha
  `[UNVERIFIED]`.
- `T^{ij}` viene de W5/W6 como símbolo conjugado de la tétrada (`σ_a p_i`), no simétrico, y solo
  a transferencia `q = 0`.
- Reparar: derivar los núcleos `T^{μν}(p, p+q)` a primer orden en `(p, q)` y compararlos con el
  Belinfante simétrico del Weyl continuo, incluido el término de espín en `T^{0i}` y la
  eliminación de la parte antisimétrica de la tétrada en `T^{ij}`. Si no se hace, rebajar F2:
  "representantes de las cargas integradas y de las partes longitudinales", no "los tres tipos
  de fuente".
- Cierre: núcleos con `q ≠ 0` en un certificado que los construya desde los operadores de enlace,
  o F2 rebajado por escrito.

**A4. Estado terminal de W10 registrado antes de cumplirse su condición. VERIFICADO. OPUS.**
El contrato de W10, §6 (C5), exige que "controlled low-energy operators exist" para el estado
`CONTINUUM_SOURCED_CONSTRAINT_BRIDGE_PASS / MICROSCOPIC_CJWW_CHARGES_OPEN`. El informe W10 (C4) no
los tiene, y W10 (`f956f68`, 09:34) se registró antes de congelar W11 (`cfdc5c6`, 09:35).
- Reparar: addendum en W10 que haga el estado terminal condicional a W11 y lo reevalúe tras A2–A3.
  No se reescribe `f956f68`.

## B. Derivaciones que faltan

**B1. Coeficientes y signos de las restricciones con fuente (W10 C1). AMBOS.**
C1 escribe `C⁰ = λT⁰⁰` y `C^j = λT^{0j}` con normalizaciones independientes. Opus calcula, con los
términos de Gu–Wen tal como se citan, `(λ/2)T⁰⁰` en la escalar y `λT^{0i}` en la vectorial
(`∂_jE^{ij} ∝ (λ/2)T^{0i}` tras dividir por 2), y dice que el coeficiente relativo lo fija la
invariancia gauge de B2 `[UNVERIFIED]`.
- Reparar: escribir una `S_grav^(2)` concreta, variar respecto a `h_00`, `h_0i` y `h_ij`, y fijar
  signos (signatura) y prefactores. C2 depende de ello.

**B2. Alcance de C2: materia de prueba a O(λ) (W10 C2). OPUS.**
Con backreaction, la materia cumple `∇_μT^{μν} = 0` en la métrica perturbada, y
`∂_μT^{μν} = O(λhT)`: el sistema linealizado con fuente es inconsistente a O(λ²) (problema de
Deser/Gupta) `[UNVERIFIED]`. Esto afecta directamente al gate conjunto, que quiere reciprocidad.
- Reparar: restringir C2 a O(λ) sin backreaction, o incluir la autoenergía gravitatoria.

**B3. Qué sector de Gu–Wen da `G_lin` (W10 C2, prior art). OPUS.**
C2 usa la dinámica de Einstein linealizada. Según la propia auditoría de W8, el modelo controlado
de Gu–Wen (L) tiene `ω ∝ k³`, que no es Einstein linealizado. El de dispersión lineal (N) tiene
menos control.
- Reparar: declarar el sector y rehacer C2 con su dinámica real.

**B4. Orden del desajuste `H_eff − H_IR` (W11 F2). VERIFICADO. AMBOS.**
Es `Θ(|p|³)` en valor absoluto, no solo `O(|p|²)`. Contraejemplo de Opus (VERIFICADO): en el eje
`p₃`, `W = e^{ip₃σ₃}` exactamente, luego `H_eff = −p₃σ₃` y `H_IR = −sin p₃ σ₃`.
Nota: el término cúbico que propone DeepSeek, `H_eff = −A − (p²/6)A`, es **erróneo** (refutado
en ese mismo eje); no usarlo.
- Reparar: corregir el orden y añadir una cota dinámica `O(tΛ³)` para estados de banda estrecha.

**B5. Transformación de la materia y paso de Lorentz local (W9 B2). OPUS.**
B2 vale en la capa de masas de la materia. La invariancia de `S_m + S_int` a O(λ) necesita una
transformación de `ψ` a O(λ). Además, reducir a `h_{μν}T^{μν}` simétrico desde la tétrada requiere
invariancia Lorentz local. Ninguna de las dos está escrita.
- Reparar: explicitarlas, o marcar B2 como resultado de libro, en la capa de masas y a O(λ).

**B6. La IR de Weyl se asume en W9. OPUS.**
W9 §2 toma el Weyl continuo "schematically"; se establece después, en W11 F1, y en un solo nodo.
- Reparar: nota en W9 de que B2 no es específico de CJWW y depende de W11 F1 y de A1.

## C. Veredictos que hay que reformular

**C1. B1 = FAIL es una afirmación sobre un gauge truncado (W9). OPUS.**
`δS = −λ∫(∂_tξ_j)T^{0j}` se anula para `∂_tξ = 0`. Poner `h_{0μ} = 0` es una elección de gauge
con grupo residual `ξ` independiente del tiempo. B1 muestra que faltan las restricciones, no que
hagan falta campos lapse/shift.
- Reparar: reformular B1 así. La cuenta no cambia.

**C2. B4: restricciones, no registros (W9). OPUS.**
Con la arquitectura de Gu–Wen importada en W10, `a₀₀` y `a₀ᵢ` son multiplicadores de Lagrange. Lo
que falta microscópicamente son operadores de restricción locales con cargas de materia, impuestos
por penalización o proyección, no "registros de lapse/shift".
- Reparar: reformular B4 y el "minimal successor" de W9 §7.

**C3. F3 y F4 (W11). OPUS.**
- F4 (VERIFICADO en parte): `Σ_x π_i` tiene símbolo escalar `sin p_i` y conmuta con `W`, así que se
  conserva exactamente. Según Opus existe además una ecuación de continuidad local de un paso
  `[UNVERIFIED]`. El obstáculo es canónico frente a Belinfante (A3), no la conservación. Corregir
  el razonamiento de F4.
- F3: Opus propone un no-go de paridad: no existe un generador continuo invariante por traslación
  con `e^{−iH(p)} = W(p)`, porque la traza tendría que valer `2π·par` en los nodos `+I` y
  `2π·impar` en los nodos `−I` `[UNVERIFIED]`, así que toda rama de `i log U` tiene colas no
  sumables.
- Reparar: comprobar el no-go. Si se sostiene, F3 pasa de OPEN a obstrucción probada para
  generadores invariantes por traslación, y `K` (A2) es la alternativa.

## D. Certificados

**D1. `verify_w9_continuum_gauge_bridge.py`. AMBOS.**
- Las comprobaciones 1–3 sustituyen la ley de conservación en sí misma; la 2 divide por `k_z`.
- No aparecen `h`, `ξ`, la simetría de `T`, el factor `½ → 1` ni la integración por partes.
- `det D = 1` usa una matriz fija sin enlazarla con W6.
- Reparar: rehacerlo con `h`, `ξ` y `T` simétrico explícitos, y tomar `D` de W6. O bien
  reetiquetarlo como "comprobación de consistencia algebraica".

**D2. `verify_w11_ir_stress_source.py`. AMBOS.**
- Solo es genuina la comprobación de derivadas de `walk2()`.
- `H_IR` está escrito a mano en vez de construirse desde los operadores de enlace.
- La comprobación del momento es `cos 0 = 1`.
- Reparar: construir los símbolos desde los operadores de enlace en espacio real y comprobar:
  - el orden `H_eff − H_IR` (B4);
  - la conservación (A2);
  - los otros nodos (A1);
  - `q ≠ 0` (A3).

  Reetiquetarlo mientras tanto como "comprobación de símbolos de primer orden a transferencia
  cero en `p = 0`".

## E. Prior art

- Nada de Gu–Wen (arXiv:0907.1203) ni de Pretko está en `biblioteca/`. Los dos revisores lo
  marcan todo `[UNVERIFIED]`, y Opus no puede confirmar:
  - las etiquetas L/N;
  - que Gu–Wen difieran explícitamente "gravedad + fermiones casi sin masa";
  - la forma exacta del término `a₀₀`.

  Reparar: descargar ambos papers, leer y citar `fichero.pdf p.N` para cada atribución de W8–W10.
  Si no, `[UNVERIFIED]` en el informe.
- Prior art que Opus señala y que no se ha auditado:
  - C. Xu, modelos de red de rango 2 ("soft graviton", ≈2006);
  - Xu–Hořava, gravedad de Lifshitz emergente (≈2010);
  - Rasmussen–You–Xu (≈2016);
  - Arrighi–Facchini–Forets y Di Molfetta–Debbasch, walks cuánticos en espacio-tiempo curvo;
  - **Arnault–Debbasch, *Quantum walks and gravitational waves* (≈2017)**, que toca directamente
    la afirmación de novedad del puente walk–gravitón;
  - el teorema de Weinberg–Witten, que cualquier gravitón emergente acoplado a un `T`
    conservado covariante tiene que eludir.

  Candidato a `investigacion-gemini` con dos vías (`prompt.md` y `prompt_abierto.md`); con
  permiso del usuario.

## Orden propuesto

1. E (prior art, sobre todo Arnault–Debbasch y Gu–Wen en el original): puede cambiar qué es nuevo.
2. A1, A2, A4: baratos y verificados.
3. A3 y B1: las derivaciones de fondo que necesita el gate conjunto.
4. B2–B6, C1–C3, D1–D2.
5. Solo entonces congelar el JOINT EINSTEIN–WEYL LOW-ENERGY GATE, con el alcance de B2
   (O(λ) o con autoenergía) y la opción de A1 declarados en el contrato.
