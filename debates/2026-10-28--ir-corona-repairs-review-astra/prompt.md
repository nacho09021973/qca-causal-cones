# Revisión ciega — reparaciones de ir-corona tras el sanedrín del 28-10

Fecha: 2026-10-28. Autorización directa del usuario: «revision ciega con codex».
Objetivo: comprobar si las tres reparaciones del commit `cd8ff54` cierran las objeciones
obligatorias del sanedrín `debates/2026-10-28--ir-corona-sanedrin.md`.
Resultado esperado: veredicto por reparación y global (CERRADA / CERRADA_CON_ARREGLOS / ABIERTA),
con los arreglos obligatorios numerados.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra (familia
OpenAI; las reparaciones las escribió una sesión de Claude).
Cierre: informe del revisor y lectura crítica del autor en `verificacion_autor.md`. No autoriza
enviar el paper ni cambiar `state/CURRENT_STATE.md`.
Documentos: `papers/ir-corona/ir-corona.tex` en `cd8ff54` (SHA256 `90fb2c8ec712463c…`) y
`reparaciones.diff` (`git diff a187753 cd8ff54`).
Herramienta: revision-ciega del PATH; ~/herramientas commit `0c150e8`.

---
Responde en español. Revisión matemática adversarial e independiente, una sola ronda. Tu sesión
está sellada: sólo tienes los dos documentos adjuntos (el manuscrito completo y el diff de las
reparaciones).

Una revisión previa, entre otros modelos, encontró tres defectos obligatorios en la sección de
asintóticas del manuscrito:

1. Lemma «Layers»(b): la corrección de Bob se escribía como un escalar `E_B` multiplicando la fila
   fija `R_0(w_*)^† M_B`, lo que es falso porque la dirección de `R_0(y/N)` varía en `B_N`.
   Se pedía una fila residual acotada en norma por `C(N^{-1/2}+|η_n|)`, uniforme en `θ_N` y
   cerca de `πu`, propagada con normas en «Assembly» sin perder el `O(N^{-7})`.
2. Lemma «Layers»(d): «the character is non-trivial on each plane. The Poisson sum therefore has
   no m=0 term» es falso; el término m=0 está, en una frecuencia desplazada no nula. Se pedía la
   separación de las frecuencias desplazadas y una cota sumable en profundidad que dé
   `|A_f(η_0+η)| ≤ C N^{-4}` y el `O(N^{-8})` de «Assembly».
3. Tabla 1: «Mean leading coefficients» para `C̄ = K c_r Γ̄ ℓ_0`, que no es el promedio de `C(θ)`.

El diff contiene las reparaciones. Para cada una:

1. Rehaz el argumento nuevo desde cero. En (b): la cota `‖ρ(y)‖ ≤ C N^{-2}(1+δ')`, el uso de
   `y_* = N w_*` y de la suavidad de `R_0` en `B_N`, el recuento de sitios y la cota `C N^{-3}` del
   término con `ρ`, y la definición de `E_B`. En (d): la reducción a `η_{0,t}`, `d_0 > 0`, la
   reducción de `r_0` y su compatibilidad con Lemma «symbol»(d)–(e), la convergencia de la suma
   sobre `Λ_0^*`, y cada término de la cota `‖∂³G_δ‖_M ≤ C N^{-4}(1+δ)^3` (salto de la segunda
   derivada en el borde, parte interior, derivadas de `S`, Leibniz con `φ_N`). En «Assembly»: la
   cota en norma del segundo reemplazo.
2. Busca errores de constantes, de potencias de N o δ, de cuantificadores (uniformidad en `θ_N`,
   `η`, profundidad) y pasos que usen una hipótesis no enunciada en el manuscrito.
3. Comprueba que la nueva leyenda de la Tabla 1 es correcta (la afirmación sobre los promedios de
   `Γ_±`) y que no queda en el texto ningún otro uso de `C̄` como promedio.
4. Señala cualquier cambio del diff que introduzca un error nuevo o contradiga otra parte del
   manuscrito.

Da un veredicto por reparación y global: CERRADA, CERRADA_CON_ARREGLOS o ABIERTA, con los arreglos
obligatorios numerados y localizados (lema, línea del diff o ecuación). Distingue error matemático,
laguna de justificación y cuestión de redacción. Marca como NO VERIFICADO lo que dependa de algo que
no está en los documentos.
---
