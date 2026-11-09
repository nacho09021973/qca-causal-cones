<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.318 (Claude Code))
opus.json sha256 8d3d7783c63fd0dd0d411077c9fafd831319e372e4e4b33887d56ed402d0e7dc
inicio: 2026-11-05T10:16:32Z  fin: 2026-11-05T10:21:16Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-scalar-method.md ; último commit observado: c7c2dcb ; sha256 de la copia enviada 8791ddb115dd27f912b3c2b2fc17c89561ab1968bb27691e2ea69124f5ce3563
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_trace_scalar_structure.py ; último commit observado: c7c2dcb ; sha256 de la copia enviada a00574f90b6c2191dbb92d20f75b260c3a6f4987b683e97a96c7585717647ce3
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-scalar-structure-verifier.txt ; último commit observado: c7c2dcb ; sha256 de la copia enviada 910cb06e6692f45a1a7def0a8e13e18c628429318025cf477693afea03c029d2
documento: /home/ignac/qca-causal-cones/theory/HEX_TRACE_SCALAR_GATE.md ; último commit observado: c7c2dcb ; sha256 de la copia enviada 10d74f8943af3faffc96693d40f565929b43679a45ae1d7c6f74f60c1bd2b10f
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-s19.md ; último commit observado: c7c2dcb ; sha256 de la copia enviada 6dff1eeb5c9c6d7669c235e1cb15bdbd7c2f8f1720ee99b6599dcdc4878cbb24
entrada_opus.txt sha256 cf8387e841dc3adbdb202891ca088815bd54a18dcdef994dd06dc75e3aed966a
respuesta sha256 ba2b054af1de6d048d99032084ce23fd9fa50efbc40007ca683561a5d3a7f303
-->

# Revisión adversarial de «Scalar method beyond S19» (Codex, 2026-11-05)

**Revisor:** Claude (Opus 5.5). **Modo:** sesión sellada, sin herramientas. No he ejecutado el script. Las referencias al verificador se basan solo en la lectura del código adjunto. Ninguna afirmación del texto de Codex se ha usado como autoridad: cada paso se ha re-derivado abajo.

**Dictamen global: PASS.** No hay objeciones obligatorias pendientes. Las secciones 2 y 3 son demostraciones correctas con los cuantificadores y la normalización declarados. Dejo sugerencias opcionales de claridad y notación. El estado OPEN_AFTER_SCALAR_ANALYSIS es la descripción correcta del resultado.

| Bloque | Veredicto |
|---|---|
| 1. Coseno normal ⇒ D²f(0) = −r²I | PASS |
| 2. Proyección, rejilla δ, grado N, ceros ⇒ (T) | PASS |
| 3. Familia alineada, f_m^0, disponibilidad de D6 | PASS |
| 4. Divisibilidad por Δ, multiplicidades, realidad y simetría de h | PASS |
| 5. Polígonos de Newton ⇒ supp h ⊂ H_(m−2) | PASS |
| 6. Alcance del verificador y del resultado | PASS (con nota opcional de redacción) |

---

## Bloque 1 — Hessiano: PASS

**Re-derivación.** Sea f un polinomio trigonométrico real (por tanto C^∞). Para un normal unitario n, d²/dt² f(tn)|₀ = nᵀD²f(0)n, y d²/dt² cos(rt)|₀ = −r². Por tanto Q := D²f(0) + r²I cumple nᵀQn = 0 en tres rectas distintas (las normales a facetas de un hexágono regular forman tres rectas separadas 60°).

Una forma cuadrática binaria no nula se factoriza sobre ℂ en a lo sumo dos formas lineales, así que se anula en a lo sumo dos rectas reales. Luego Q = 0.

**Hipótesis usadas.** Solo la restricción normal en las tres rectas y la suavidad. No se usan acotación, f(0)=1 ni isotropía separada. La afirmación del informe es exacta.

---

## Bloque 2 — Proyección, rejilla y argumento de ceros: PASS

**Rotación.** Con R = rotación de +60°, se tiene Rg1 = g2 y Rg2 = g2 − g1. Por tanto Rv = −b·g1 + (a+b)·g2, y la arista es Rv − v = (−a−b)·g1 + a·g2, lo que coincide con el informe. Además |Rv − v| = L, porque el lado del hexágono regular es igual a su circunradio.

**Proyección.** La normal exterior es n = J⁻¹(Rv−v)/L. El signo es correcto porque det(v, Rv) = L²·sin 60° > 0, lo que da h·n = det(h, Rv−v)/L. Para h = (m·g1 + l·g2)/L:

  h·n = det(g1,g2)·[a·m + (a+b)·l]/L² = r·[a·m + (a+b)·l]/D,  con det(g1,g2) = r y L² = D.

Comprobación: h = v/L da h·n = r, la apotema correcta.

**Rejilla y grado.** Los valores de a·m + (a+b)·l son exactamente los múltiplos de gcd(a, a+b) = d. Por tanto los niveles normales son múltiplos de δ = r·d/D, con |k| ≤ D/d = N. N es entero porque d² divide a D. Se cumple N·δ = r, así que cos(rt) = cos(Nθ) con θ = δt.

Las otras facetas se obtienen por R^j. R preserva Λ y actúa en coordenadas como (a,b) ↦ (−b, a+b), que es unimodular, de modo que D y d son invariantes. La faceta opuesta es R³ = −I. Basta con una rejilla conmensurable; no hace falta que cada nivel esté poblado. Correcto.

**Ceros.** G(θ) = Σ i(h·e)·b_h·e^{ikθ} es real y de grado ≤ N. En θ_j = jπ/N (j = 0,…,2N−1, puntos distintos módulo 2π) se tiene f = (−1)^j = ±1. Como −1 ≤ f ≤ 1 en todo ℝ² y f es diferenciable, ∇f = 0 en esos puntos, luego G(θ_j) = 0.

z^N·G es un polinomio de grado ≤ 2N que se anula en las 2N raíces 2N-ésimas de la unidad. El espacio de tales polinomios tiene dimensión 1, así que z^N·G = c(z^{2N} − 1). Por tanto G = 2ic·sin(Nθ), y la realidad de G fuerza G = β·sin(Nθ) con β real.

Por el Bloque 1, G′(0) = g′(0)/δ = nᵀD²f(0)e/δ = −r²(n·e)/δ = 0. Como G′(0) = Nβ, resulta β = 0 y se obtiene (T).

**Reflexiones.** No se introduce ninguna reflexión. El argumento usa solo acotación, cosenos normales y soporte finito, para cualquier v. La forma por coeficientes (sumas de primer momento por nivel) es equivalente a (T) por independencia lineal de exponenciales con frecuencias distintas. Las sumas usuales por nivel (1/2 en los extremos y 0 en los intermedios, incluido λ = 0) son correctas.

**Comprobación cruzada propia.** Para v = m·g1 (a = m, b = 0) se obtiene N = m y δ = r/m. En la faceta entre m·g1 y m·g2, (h·n)/r = (i+j)/m, que coincide con la restricción de §3 a p = q.

*Opcional:*
- **O1.** Declarar R explícitamente (sentido antihorario, acción (a,b) ↦ (−b, a+b)).
- **O2.** Colisión de notación: `b` designa una coordenada de v, el coeficiente del seno y los b_h; `m` designa una coordenada de frecuencia en §2 y el radio en §3; `d` designa el gcd en §2 y f − f_m^0 en §3. Conviene renombrar (por ejemplo β para el coeficiente del seno, (i,j) para las frecuencias de §2 y R_m para f − f_m^0).

---

## Bloque 3 — Familia alineada: PASS

**Frecuencias.** Con L = m y h = (i·g1 + j·g2)/m, se tiene h·k = i·p + j·q. El hexágono de vértices ±m·g1, ±m·g2, ±m(g2−g1) es {max(|i|,|j|,|i+j|) ≤ m}. Correcto.

**Rectas normales** (direcciones a 30°, 90° y 150°):

| Recta | Dirección de k | Variable no nula | Restricción |
|---|---|---|---|
| p = 0 | k ∝ (0,1) | q = rt/m | cos(mq) |
| q = 0 | k ∝ (√3/2, −1/2) | p = rt/m | cos(mp) |
| p = q | k ∝ (√3/2, 1/2) | p = rt/m | cos(mp) |

Todo coincide con el informe.

**Interpolante.** f_m^0 da cos(mq), cos(mp) y cos(mp) en las tres rectas, respectivamente. Su soporte es {0} más la órbita C6 de (m,0), que es invariante por la reflexión (i,j) ↦ (i+j, −j). Por tanto f_m^0 es real, par, invariante por D6, y f_m^0(0) = 1.

*Observación:* f_m^0 no está acotado. Vale −5/4 en (mp, mq) = (2π/3, 4π/3). El informe no afirma lo contrario.

**Disponibilidad de D6.** Los ejes de reflexión de H_{m·g1} están a k·30°, y coinciden con los ejes de simetría de la red triangular. Por tanto el promedio D6 preserva Λ/m ∩ H, la acotación, f(0) = 1 y el conjunto de rectas normales (cada una con la misma restricción cos(rt)). En consecuencia, existe un candidato factible si y solo si existe uno D6-invariante.

*Opcional:*
- **O3.** Enunciar esa equivalencia explícitamente: es lo que justifica restringirse a candidatos D6-invariantes en la pregunta de existencia.
- **O4.** La familia v = m(g1+g2) también admite D6 legítimo (eje a 30°). No es necesario incluirla, pero evita que el lector infiera que solo m·g1 lo admite.

---

## Bloque 4 — Divisibilidad por Δ: PASS

**Factores simples.** Sea R_m := f − f_m^0. En la recta p = 0 se tiene R_m(1, w) = 0 para todo |w| = 1. Un polinomio de Laurent en w que se anula en la circunferencia unidad es idénticamente nulo, luego (z−1) divide a R_m. Lo mismo ocurre con (w−1). En la recta p = q, R_m(z, z) = 0 en |z| = 1, luego también en todo z, y (z−w) divide a R_m.

**Multiplicidad dos.** La reflexión respecto del eje y lleva p a −p y q a q − p, lo que coincide con el informe (y está en D6). La invariancia R_m(p,q) = R_m(−p, q−p), derivada en p = 0, da ∂_p R_m = −∂_p R_m − ∂_q R_m. Como ∂_q R_m = 0 en p = 0, resulta ∂_p R_m = 0.

Si R_m = (z−1)·R₁, entonces ∂_p R_m = i·z·∂_z R_m, que en z = 1 vale i·R₁(1, w). Esto se anula en |w| = 1, luego en todo w, así que (z−1)² divide a R_m.

Hay una vía más limpia que las «reflexiones conjugadas». La rotación (z, w) ↦ (w, w/z) (el mismo mapa que usa el script) es un automorfismo del anillo que preserva R_m. Lleva z−1 a w−1, y w−1 a (w−z)/z, que es un asociado de z−w. Transporta así (z−1)² a los otros dos factores dobles.

**Producto.** ℂ[z^±, w^±] es un DFU, y z−1, w−1, z−w son irreducibles y no asociados entre sí (las unidades son c·z^a·w^b). Por tanto su producto al cuadrado divide a R_m.

**Fórmula de Δ.** Se tiene sin²(p/2) = −(z−1)²/(4z), sin²(q/2) = −(w−1)²/(4w) y sin²((p−q)/2) = −(z−w)²/(4zw). El producto da −(z−1)²(w−1)²(z−w)²/(64z²w²), como afirma el informe.

**Realidad y simetría de h.** Los tres cosenos de Δ forman la órbita D6 de (1,0), así que D6 los permuta y Δ es invariante y real. Entonces h = R_m/Δ es real e invariante en {Δ ≠ 0}, que es denso e invariante, y por continuidad lo es en todas partes.

**Recíproco.** Para m ≥ 2, H_2 + H_{m−2} ⊂ H_m por subaditividad de la norma hexagonal, y Δ se anula en las tres rectas y en 0. Esto da soporte, restricciones y f(0) = 1, pero no acotación, que el informe distingue correctamente.

*Opcional:*
- **O5.** Explicitar en una frase el paso «se anula en la circunferencia unidad ⇒ se anula como polinomio de Laurent». El informe lo usa tácitamente tres veces.
- **O6.** Posible refuerzo: la propiedad (T) de §2 da los factores dobles para cualquier f acotada sin promediar, porque ∂_e f_m^0 = 0 en los ejes por simetría de f_m^0. Bastaría con añadir una frase; no es necesario.

---

## Bloque 5 — Polígonos de Newton: PASS

**Argumento.** Para cualquier dirección u, la forma inicial cumple in_u(Δh) = in_u(Δ)·in_u(h). Es no nula por ser ℂ[z^±, w^±] un dominio. Por tanto max_{supp(Δh)} u·x = max_{supp Δ} u·x + max_{supp h} u·x.

Las cancelaciones internas pueden ocurrir, pero nunca en las caras expuestas, así que no afectan al argumento. Basta aplicarlo a las seis normales de faceta ±i, ±j, ±(i+j).

**NP(Δ) = H_2.** Analíticamente, NP(Δ) es el zonotopo 2[0,e₁] + 2[0,e₂] + 2[e₁,e₂], desplazado por (−2,−2), que es H_2. Por ejemplo, la cara i = 2 tiene j ∈ [−2, 0]. El script comprueba lo mismo: vértices en el soporte y soporte dentro de H_2.

**Casos.**
- **m ≥ 3:** max_{supp h} ℓ ≤ m − 2 para las seis formas ℓ, luego supp h ⊂ H_{m−2}.
- **m = 2:** el soporte es ⊂ {0}, luego h es constante.
- **m = 1:** se tendría max ℓ ≤ −1 y max(−ℓ) ≤ −1, con suma ≤ −2. Pero max ℓ + max(−ℓ) ≥ 0 en un conjunto no vacío. Luego h = 0.
- **R_m = 0:** h = 0, porque Δ ≠ 0 en un dominio.

Riguroso.

**Especialización m = 2, re-derivada de forma independiente.** Se tiene f_2^0(P) = f_2^0(Q) = −5/4, Δ(P) = 3/64 y Δ(Q) = 27/64. Con f = f_2^0 + cΔ:
- f(P) ≥ −1 da c ≥ 16/3;
- f(Q) ≤ 1 da c ≤ 16/3.

Por tanto c = 16/3, lo que coincide con −32·a1 para a1 = −1/6.

La identidad −3 + S1 − S2 + S3/2 = −32Δ se comprueba en P (−3/2) y en Q (−27/2). Como la diferencia ya es un múltiplo constante de Δ por la estructura con m = 2, esas dos evaluaciones bastan.

En la recta p = 2q, con x = cos q, f_2^0 + (16/3)Δ = (8x⁴ + 8x³ − 6x² − 8x + 1)/3. En x = 3/5 vale −1997/1875 < −1. Coincide con el documento S19.

*Opcional:*
- **O7.** Una consecuencia gratuita que el informe no menciona es el caso m = 1 (soporte S7). Allí f = f_1^0 queda forzado y alcanza −5/4, así que no hay candidato escalar acotado. Si se añade, debe marcarse como no revisado ni promovido.

---

## Bloque 6 — Alcance: PASS

El informe delimita correctamente lo que queda establecido y lo que no:

- **El verificador** comprueba identidades sobre Δ (factorización, ceros dobles de Δ, invariancia, polígono de Newton) y la identidad residual de S19. No comprueba §2, la divisibilidad de un R_m arbitrario ni la acotación.
  - Por lectura del código, los mapas (z,w) ↦ (w, w/z) y (z,w) ↦ (1/z, w/z) corresponden a (p,q) ↦ (q, q−p), de orden 6, y (p,q) ↦ (−p, q−p), de determinante −1. Ambos preservan p² − pq + q², así que generan el D6 correcto.
  - El valor a1 = −1/6 se toma del documento S19. Arriba lo he re-derivado de forma independiente.
- **La reducción alineada** no cubre orientaciones como v = 2g1 + g2, donde las reflexiones no preservan Λ. El informe lo dice expresamente.
- **Un candidato escalar no es un walk.** También lo dice.
- **La implicación de §1** («no existe para todo v ⇒ se excluye la saturación») depende de que la rigidez normal de HEX_CEILING valga para todo hull H_v. Es un insumo externo, fuera del alcance de esta revisión.
- **§4:** la observación sobre ∂_e²f es correcta. Solo se fuerza un signo débil (≤ 0 en máximos, ≥ 0 en mínimos). Por ejemplo, H(θ) = −r²·cos(Nθ) es compatible, así que el argumento no se itera.

*Opcional:*
- **O8.** En §3 último párrafo, escribir «double zeros *of Δ*» para que no se lea como una certificación de la divisibilidad general.
- **O9.** En §4, escribir «weak alternating sign» en lugar de «alternating sign».

---

## Cierre

- Las secciones 2 y 3 son correctas tal como están, con sus cuantificadores (todo v en §2; v = m·g1 y candidatos D6-invariantes en §3) y con la normalización de radio 1 y r = √3/2.
- **Cambios obligatorios: ninguno.** Las sugerencias O1–O9 son opcionales, por lo que no procede una ronda de re-revisión.
- Esta revisión no promociona ningún resultado. La factibilidad escalar para m ≥ 3 y para las orientaciones no alineadas sigue abierta, igual que la cuestión universal de saturación.
