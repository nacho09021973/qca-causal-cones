<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.316 (Claude Code))
opus.json sha256 fc5f5d4c840ec5aabb626950311279d7fd9f9dd5beb0c02748087e8824850906
inicio: 2026-10-31T18:01:22Z  fin: 2026-10-31T18:06:53Z
documento: /home/adnac/qca-causal-cones/reports/2026-10-31--h1-small-gaussian-profile.md ; último commit observado: 11ea2d8 ; sha256 de la copia enviada 98e96a47fdb584e921210e71c07559b773a2bd85258ab8fc1606ac6bc5972611
documento: /home/adnac/qca-causal-cones/theory/H1_SMALL_GAUSSIAN_PROFILE_GATE.md ; último commit observado: 067f8fa ; sha256 de la copia enviada d739db6b4b476c79c4a51d9a26f0dcf03dda31b5c3d818b8b0d040f6e972cddd
documento: /home/adnac/qca-causal-cones/reports/2026-09-24--two-channel-t1-exact-signed-pq.md ; último commit observado: 7f68fa7 ; sha256 de la copia enviada c320aaa5060f343f1f0e726f663058f62fb6c1d2f19f71da43ef4bd759e24e8d
documento: /home/adnac/qca-causal-cones/reports/2026-09-24--schur-stability-physical-transfer.md ; último commit observado: 2e6af3a ; sha256 de la copia enviada caee6fa254fd83d64ac16ce6de2f04b359087e9a8f1668b0d4f93a089589bf65
documento: /home/adnac/qca-causal-cones/papers/ir-corona/ir-corona.tex ; último commit observado: 3a44725 ; sha256 de la copia enviada a3849451dbac2d3e3a68ace47b0b50ae2bbf5ae3f6902c8bc92b9c2d820a42c5
documento: /home/adnac/qca-causal-cones/scripts/verify_small_gaussian_profile_algebra.py ; último commit observado: 11ea2d8 ; sha256 de la copia enviada 5647b1d52cce9392bac6d239ae4dd40b31b147b1e3541ee170b08c475990cfa2
documento: /home/adnac/qca-causal-cones/scripts/verify_regional_laplace_coefficient_gate.py ; último commit observado: ae6dd3e ; sha256 de la copia enviada d008417debe149743396bfbeb7d55be11fe7aa00bce3b4aecebf6a50997884b2
entrada_opus.txt sha256 60df1c1e292ee78ff8416cad02addae2cccc391bb0c6d24ac3565c4acf5850b1
respuesta sha256 4536f005baac8d2c060bc9ffe175dad3e716be5bda852fe053f9426a3b31b7f7
-->

# Revisión adversarial: `2026-10-31--h1-small-gaussian-profile.md`

**Alcance.** He reconstruido las desigualdades desde las definiciones de T1, del puente y de `ir-corona.tex`. El puente promovido y el teorema plano σ₂/I se usan como entradas congeladas: compruebo sus hipótesis y su aplicación, no los revalido. No he ejecutado los verificadores; los leo como texto. Por tanto, no confirmo los SHA256 ni los recuentos «21/21» y «58/58».

---

## 1. PROFILE_AND_PARITY — **PASS**

**Fourier.** En 1D, ∫e^{-x²}e^{ikx}dx = √π e^{-k²/4}. Por tanto v̂(k) = π^{3/2}e^{-|k|²/4} en la convención del puente, v(X) = ∫e^{-ik·X}v̂ d³k/(2π)³.

- a₀ = v(0) = 1.
- a₁ = (π^{3/2}·4π/8π³)∫₀^∞ r³e^{-r²/4}dr. Con s = r²/4, la integral vale 8, luego a₁ = 4/√π. ✓
- La densidad radial r²e^{-r²/4}/(2√π) es correcta.
- Para ϑ_ε = εv: b = |ε|, a₀ = |ε|, a₁ = 4|ε|/√π. La hipótesis F vale uniformemente en |ε| ≤ 1.

**Norma Wiener.** Con ψ̂(p) = Σ_x e^{ip·x}ψ(x):

$$(V_N\psi)^\wedge(p)=\int\widehat v(k)\,\widehat\psi(p-k/N)\,\tfrac{d^3k}{(2\pi)^3}.$$

Es convolución con una medida positiva de masa a₀ = 1, con todas las imágenes periódicas incluidas. Por Minkowski, ‖V_N‖_{𝒲→𝒲} ≤ 1. El signo «k ↦ −k/N» del informe es irrelevante porque v̂ es par. D es unitario en cada fibra real y β es unitario. Además, sup_x‖ψ(x)‖ ≤ ‖ψ‖_𝒲. ✓

**C_φ.** ∫_{B₁}g = 4π(1/3 − 2/5 + 1/7) = 32π/105 y Z_N^{-1/2} = √3465·πN^{3/2}/8. Entonces

$$\|J\phi_N\|_{\mathcal W}=\frac{\sqrt{3465}\,\pi N^{3/2}}{8}\cdot\frac{32\pi}{105N^3}\cdot\frac1{8\pi^3}=\frac{\sqrt{3465}}{210\pi}N^{-3/2}.\ ✓$$

Comprobación independiente de la normalización: ∫₀¹r²(1−r²)⁴dr = 128/3465 da exactamente ‖φ_N‖₂ = 1.

**Paridad.** De ZDZ = D y ZβZ = −β se sigue ZU_εZ = U_{−ε}. Con ZJ = J se obtiene (5). Consecuencias:

- π_+ es par y π_− es impar en ε, tanto para r = U^NJφ como para d = U^Nf.
- Por la fórmula (2) de T1, L_+ (par·par) y L_− (impar·impar) son pares, incluidos sus términos cuadráticos.
- El funcional 𝓕_N sólo depende de ε a través de r₊, luego es par y real-analítico, y 𝓕_N′(0) = 0.
- Ningún paso usa conservación de momento.

---

## 2. FIRST_CORRECTION — **PASS**

**Expansión del producto.** Escribo (C_εD)^N con C_ε = Σ_n(−iεB_N/N)^n/n!. La cota (6) es la identidad multinomial:

$$N^{-m}\sum_{n_1+\dots+n_N=m}\frac{1}{n_1!\cdots n_N!}=\frac1{m!}.$$

Usa ‖B_N^n‖_𝒲 ≤ 1, que vale por submultiplicatividad. La serie converge absolutamente en norma de operador sobre 𝒲, así que la expansión es legítima para todo N.

**Términos de (7).**

- *Una sola moneda.* Si n_{j+1} = 2 y las demás monedas valen I, el término es (−i/N)²/2 · D^{N−1−j}V_N²β²D^{j+1}. Como β² = I, aparece −(1/2N²)S^{N−1−j}V_N²S^{j+1}. ✓
- *Dos tiempos j < k.* El término es (−i/N)² D^{N−1−k}B_N D^{k−j}B_N D^{j+1}. El primer β lleva el estado al canal −, donde actúan k−j factores S^{-1}; el segundo lo devuelve. Resultado: −(1/N²)S^{N−1−k}V_N S^{−(k−j)}V_N S^{j+1}. Signo y exponente son correctos. ✓
- *Control de normas.* N/(2N²) + [N(N−1)/2]/N² = 1/2, que coincide con la cota 1/2! de (6).

**Segunda vía.** D(a,b) = (Sa, S^{-1}b) seguido de C = cos − i sin·β da exactamente las recurrencias de b_{1,j} y a_{2,j}. Al resolverlas, el producto (−i/N)(−i/N) = −1/N² reproduce (7). Esto es una verificación general en N, independiente del verificador de tres pasos.

**Restos.** Sólo contribuyen los m pares, porque Z W_m Z = (−1)^m W_m. Por eso los restos son cosh|ε| − 1 y cosh|ε| − 1 − ε²/2, sin pérdida. Para |ε| ≤ 1, la serie de términos no negativos da (cosh1 − 1)ε² y (cosh1 − 3/2)ε⁴. ✓

**Coeficiente.** Como 𝓕 es analítica y 𝓡_N = O(ε⁴), 𝓕″(0) = 2𝒬_N. El factor 2 es correcto.

**Coeficiente cuadrático de L_+ completo.** El informe da 2Re⟨a₂,Eb₀⟩ + 2Re⟨a₀,Eb₂⟩ + 2Re⟨b₀,Eb₂⟩. La expansión de 2Re⟨r,Ed⟩ + ⟨d,Ed⟩ lo confirma, y el informe no sustituye L_+ por 𝓕.

**Uniformidad.** Las cotas (9) son uniformes en N e y. Ningún umbral depende de N.

---

## 3. INTEGRATED_KERNEL — **PASS**

**Máximos.** Lem. `specrad` con ξ_* = t_*u (todas las componentes son no nulas) da ρ(M) ≤ 1, con igualdad exactamente en Σ = {0,π}³. No se descarta ningún máximo.

**Otros saddles.** cos(p_j + π) = −cos p_j implica f(α + p − iξ_*) = s_α f(p − iξ_*). Para una matriz unimodular, las raíces pasan a ser exactamente s_αλ^{±1}(p), porque (sλ)^{-1} = sλ^{-1}. El proyector de Riesz (S − s_αλ^{-1})/(s_αλ − s_αλ^{-1}) es analítico y acotado mientras |λ − λ^{-1}| ≈ Λ − Λ^{-1} se mantenga separado de cero.

**No normalidad.** Se controla mediante ‖P(p)‖ ≤ C, sin asumir proyectores ortogonales. De ahí

$$\|M(\alpha+p)^N\|\le|\lambda/\Lambda|^N\|P\|+|\lambda^{-1}/\Lambda|^N\|I-P\|,$$

que es (12), con r ≈ Λ^{-2} < 1.

**Hessiano.** Re log(λ/Λ) = Re[Φ(ξ_* + ip) − Φ_*] = −½pᵀQp + O(|p|⁴). El término cúbico es imaginario puro, así que el O(|p|³) del informe es correcto aunque no óptimo.

La forma de q_n del informe coincide con la del manuscrito:

$$\frac{c(c^2-1)^2(c^2+2)}{d^3}=\frac{c}{d}\cdot\frac{(c^2-1)(c^2+2)}{c^4+c^2+1},\qquad d^2=(c^2-1)(c^4+c^2+1).$$

Además (c²−1)²(c²+2) = c⁶ − 3c² + 2, así que q_n > 0 y q_t > 0. ✓

**Complemento compacto.** Por continuidad del radio espectral, ρ ≤ r_out < 1 fuera de las ocho vecindades. El Lem. `schur` da r_out^N + CNr_out^{N−1}, también para raíces repetidas.

**Integración.** La parte gaussiana da ∫e^{−c₀N|p|²}d³p ≤ (π/c₀N)^{3/2}. Los términos exponenciales se absorben con sup_x x^{5/2}e^{−ax} < ∞. Las seis sillas no contribuyentes entran con la misma cota; para una cota superior no hace falta su cancelación por caracteres.

**Integral de la norma frente a norma de la integral.** I_N se define como integral de la norma, y así se usa en (16) (véase §4). No hay confusión.

---

## 4. SCALE_BOUND — **PASS**

**Representación exacta (16).** Partiendo de G_N(d) = e^{−ξ·d}∫e^{−iη·d}S(η−iξ)^N dμ:

- La fuente y Bob tienen soporte finito, y el kernel es de alcance finito, así que el desplazamiento de contorno no toca la cola infinita.
- La factorización e^{−ξ_*·(y−x)} = e^{−ξ_*·(y−y_*)}e^{ξ_*·(x−x_*)}e^{−Nξ_*·v_*}, junto con Λ^N, da e^{−K_*N}.

Así,

$$|\langle 1_Bz,ES^Nf_0\rangle|\le e^{-K_*N}\int\|\mathfrak B(\eta)\|\,\|M(\eta)^N\|\,|\mathfrak A(\eta)|\,d\mu\le e^{-K_*N}\,a_N\,b_N(z)\,I_N.$$

Esto usa sup_η|𝔄| ≤ a_N, sup_η‖𝔅‖ ≤ b_N y la integral de la norma. El factor 2 procede de 2Re. El kernel es el libre S^N, que es exactamente el que fija el funcional del contrato. ✓

**Signos del tilt.**

- Alice: u·x = √3(R−δ), luego ξ_*·(x−x_*) = −t_*(θ_N + j).
- Bob: u·y − 3N + √3R ∈ θ_N + ℤ, con el mismo θ_N, y el peso es e^{−t_*(θ_N + j′)}.

Ambos pesos decaen hacia el interior de su región. ✓

**Capas.**

- Radio al cuadrado: 2Rδ − δ² − |v|² ≤ Nδ/2, válido para todo δ ≤ 2R.
- Perfiles: F_N = (16/N²)²(2Rδ − δ² − |v|²)² ≤ 64δ²/N².
- Conteo: la proyección sobre (x₁,x₂) es inyectiva y 1-Lipschitz, luego hay ≤ (2ρ+2)² ≤ 8(1+ρ²) puntos.
- Fuente: ‖U_{σ₂} − I‖ = |e^{iπF/2} − 1| ≤ πF/2, lo que incluye la parte coseno.

**Masas.**

$$a_N\le\sum_j e^{-t_*(\theta+j)}\cdot8(1+N\delta_j)\cdot\tfrac{32\pi\delta_j^2}{N^2}\cdot C_\phi N^{-3/2}\le 256\pi C_\phi H\,N^{-5/2}.$$

Los pasos son 1 + Nδ ≤ N(1+δ), δ_j ≤ (j+1)/√3, y las series Σ(j+1)²q^j = (1+q)/(1−q)³ y Σ(j+1)³q^j = (1+4q+q²)/(1−q)⁴. Por tanto H es correcto.

Para Bob, el efecto h_N entra **una sola vez**, porque se trata de una masa ℓ¹ y no de la norma ℓ² con h² del puente. Así 8·64 = 512 y C_B es correcto.

**Paso a la escala.** Con h = cosh|ε| − 1, h = ½ y h = cosh|ε| − 1 − ε²/2 respectivamente, se obtiene (17):

$$2C_AC_BC_K\,h\,N^{-5/2-5/2-3/2}e^{-K_*N}=D_*\,h\,A_N.$$

Esto incluye el resto de orden ε⁴ en la escala A_N. La cota es del orden exacto del término principal plano, así que no pierde potencias.

---

## 5. FULL_SIGNAL_SURVIVAL — **PASS** (con una aclaración no bloqueante)

**Uniformidad del puente.** He rastreado la dependencia en ϑ de cada constante del puente con W fijo:

| Paso del puente | Dependencia en ϑ |
| --- | --- |
| (4) y norma \|·\|_* | ninguna (sólo R) |
| (5)–(7) | a(b), monótona; ρ₂ y N₁ fijados para b = 1 |
| Gronwall | b |
| (9) Alice | ninguna |
| (11)/(13) Bob | e^{a₀} ≤ e |
| (16) | ninguna |
| (17) | C_W(a₁ + b²)/N² |
| (19) | suma geométrica con ρ₂ fijo |
| absorción Nρ₂^N | 1/(e\|log ρ₂\|) con ρ₂ fijo |

Todas las constantes son funciones no decrecientes de (b, a₀, a₁), y estas son ≤ (1, 1, 4/√π). Ningún paso divide por ε. **Ningún paso usa continuidad en ε a N fijo.** Se usan cotas explícitas, no un argumento de compacidad sobre la conclusión. El funcional de (22) del puente, con r₊ = 1_Bπ₊U_N^NJφ_N, es literalmente 𝓕_N(ε). La parte cuadrática se conserva como ‖E^{1/2}(d_P + d_Q)‖² = O(N^{−8}e^{−2K_*N}).

**ε = 0.** El control plano de T1 da L_{+,0} = L_{σ₂,I}. 𝓕_N(0) es su parte lineal, con f₀ = c_Nφ↓ + s_Nφ↑, que coincide con «v + a_↑» del manuscrito. La diferencia es cuadrática y exponencialmente menor que A_N, así que (19) es correcta.

Según la tabla, C̄ = −2.9389 con oscilación ≤ 1.05·10⁻³. Por tanto m > 0, C₀ es continua y 1-periódica, y M₀ < ∞.

**Cuantificadores.** ε₀ = min{1, √(m/4C_*)} depende sólo de (m, C_*). N₀ depende de (m, umbral plano, C_W, N₁), uniformemente en |ε| ≤ 1. Para todo |ε| ≤ ε₀ y todo N ≥ N₀:

$$L_+\le A_N\bigl(-m+\tfrac m4\bigr)+\tfrac m4A_N+\tfrac m4A_N=-\tfrac m4A_N,\qquad |L_+|\le(M_0+\tfrac{3m}4)A_N.$$

Por (18), L_− = O_W(N^{−7}e^{−K_*N}) = o(A_N). ✓

**Aclaración (no es un fallo matemático).** La §7 enumera la uniformidad paso a paso de forma comprimida. Recomiendo enunciarla como lema: «con W fijo, C_W y N₁ del puente son funciones no decrecientes de (b, a₀, a₁)», citando las líneas (5), (11), (13), (15), (17) y (19) del puente. El contenido ya está en el informe; falta sólo hacerlo explícito.

---

## 6. SCOPE_AND_CODE — **PASS**

**Afirmaciones del informe.** El informe distingue correctamente entre:

- supervivencia uniforme de signo y escala (probada, condicional a las entradas congeladas);
- el coeficiente asintótico a ε ≠ 0 (no afirmado);
- la no anulación de 𝒬_N (abierta; sólo |𝒬_N| ≤ ½D_*A_N);
- H1/H1c general, E0, POWER_13/2 y AdS (no tocados).

El observable (L_+, L_−) se conserva sin sustituciones.

**Verificador nuevo (leído como texto).**

- La convención gaussiana de Fourier es correcta.
- La comprobación de C_φ es correcta.
- Las comprobaciones de paridad con Z = diag(1,−1) y β = σ_x son correctas, aunque se hacen sobre el bloque de canal sin el factor de espín.
- La identidad de tres pasos con moneda truncada a O(ε²) es válida para los coeficientes ε⁰ a ε² y para el cúbico del canal +. Una inserción ε³ es fuera de diagonal y sólo alimenta el canal −.
- El control negativo y la inserción del canal − son correctos.

Dos comprobaciones son tautológicas: el «majorante multinomial» (N²/2N² = ½) y el control negativo geométrico. No certifican (6) ni H, pero tampoco afirman hacerlo.

El docstring delimita bien el alcance: no se certifican (10), (14)–(16), la uniformidad ni (19)–(21). El verificador de base no codifica restos analíticos, y el informe lo dice.

---

## Contraargumentos examinados y descartados

1. **Norma de la integral en lugar de integral de la norma.** No ocurre: (16) usa I_N.
2. **Sólo el máximo en 0.** No ocurre: se tratan los ocho saddles, con proyectores no normales acotados.
3. **Omisión del término de una sola moneda.** El término está en (7) y además se comprueba por recurrencia.
4. **Masas ℓ² en lugar de ℓ¹.** Una cota ℓ² del tipo de (13) del puente perdería escala; el informe usa ℓ¹ con h_N lineal.
5. **ρ₂ dependiente de ε.** No: se fija una vez para b = 1.
6. **Continuidad en ε a N fijo.** No se usa.
7. **Descarte de la cuadrática firmada.** No: se acota como norma no negativa.
8. **Inclinación de la cola infinita.** No: las sumas son finitas.

---

## Aclaraciones no bloqueantes

- **(a)** Enunciar como lema explícito la monotonía de las constantes del puente en (b, a₀, a₁) (ver §5).
- **(b)** Colisiones de notación: a₀ designa a la vez la masa Fourier y S^Nφ_N (§3, «For completeness»); Q designa el Hessiano, el idempotente Q de T1 y 𝒬_N; D designa la evolución y aparece en D_*. Desambiguar.
- **(c)** En (11), el resto real es O(|p|⁴). El O(|p|³) del informe es correcto pero no óptimo.
- **(d)** Mencionar que la forma de q_n de (11) coincide con la de Lem. `symbol`(d), mediante d² = (c²−1)(c⁴+c²+1).
- **(e)** El signo «k ↦ −k/N» depende de la convención y no afecta a la norma.

---

## Dictamen global

| Bloque | Dictamen |
| --- | --- |
| 1. PROFILE_AND_PARITY | **PASS** |
| 2. FIRST_CORRECTION | **PASS** |
| 3. INTEGRATED_KERNEL | **PASS** |
| 4. SCALE_BOUND | **PASS** |
| 5. FULL_SIGNAL_SURVIVAL | **PASS** (aclaración (a) recomendada) |
| 6. SCOPE_AND_CODE | **PASS** |

**Global: PASS**, condicional al puente Schur promovido y al teorema plano σ₂/I, cuyas hipótesis se cumplen aquí. Esto incluye la uniformidad en |ε| ≤ 1 con W fijo.

**Reparaciones obligatorias: ninguna.**

Siguen abiertos, fuera de este gate, el signo y la no anulación de 𝒬_N, el coeficiente asintótico a ε ≠ 0, y los valores efectivos de ε₀ y N₀. Este dictamen no constituye promoción canónica, que requiere el paso explícito previsto en el contrato.
