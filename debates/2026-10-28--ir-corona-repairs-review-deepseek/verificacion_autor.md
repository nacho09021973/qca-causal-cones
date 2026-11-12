# Lectura crítica del autor (sesión Claude), 2026-10-28

Informe: `informe_deepseek.md` (deepseek-v4-pro, `COMPLETED`, `finish_reason=stop`,
65 361 tokens de salida), sobre `ir-corona.tex` en `f85f429` y el diff `a187753..f85f429`.
Veredicto: global `CERRADA`; (b), (d), Tabla 1 y los cambios cerca de πu, correctos. Sin arreglos
obligatorios.

## Intentos

1. `intento_1_length/`: herramientas `0c150e8`, `max_tokens` por defecto de la API (65 536),
   agotado en el razonamiento sin informe. Leí el razonamiento: verificaba paso a paso y no se
   detuvo en ningún error. Su único «Mismatch!» (fase de la fórmula de 𝒮₋ en Lemma «Depth sums»)
   lo resolvió él mismo; lo rehíce: Σ_j (−1)^j g(θ+j) = e^{−iπθ} Σ_n ĝ(2πn−π) e^{2πinθ}
   = Σ_n ĝ(π(2n+1)) e^{iπ(2n+1)θ}, como en el paper.
2. `intento_2_detenido/`: `max_tokens=262144`, detenido a petición del usuario para usar el
   máximo.
3. Este informe: herramientas `83c04f9` (max_tokens = 393 216 por defecto), `REVISION_TIEMPO=7200`.
   La entrada enviada es la misma en los tres intentos (mismo `prompt.md` entre `---`, mismos
   documentos).

## Observaciones menores

1. **r₀ en Layers(b)** para los términos m ≠ 0. Aceptada: el texto no decía que η_t queda lejos
   de 2πΛ₀*∖{0}. Añadido r₀ ≤ ½ min_{m≠0}|2πm|, de donde |2πm − η_t| ≥ π|m|.
2. **Cota gaussiana en los seis puntos** (Assembly). Aceptada. Lemma symbol(b) relaciona
   S(η₀+η−iξ_*) con S(η−iξ_*) por signo, conjugación con σ₃ y transposición, que conservan la
   norma; la cota de (d) en la bola de 0 pasa así a la bola de η₀. Añadida una línea.
3. Valores de la Tabla `[NO VERIFICADO]` por el revisor: los certificados se ejecutaron en esta
   sesión (`papers/ir-corona/certificados/2026-10-28/`, 156/156).

Además, `G_0` en la prueba de Layers(b) no estaba definido (lo notó el razonamiento del intento
1); ahora es `G_δ = s_Nφ_N` en el plano, como en (d).

Los cambios de esta lectura (líneas añadidas por una sesión Claude) no han sido revisados.
