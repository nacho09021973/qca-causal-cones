# Lectura crítica del autor (sesión Claude), 2026-10-28

Informe: `informe_astra.md` (astra, `COMPLETED`, herramientas `0c150e8`), sobre `ir-corona.tex` en
`cd8ff54`. Veredicto del revisor: global `CERRADA_CON_ARREGLOS`; (b) `CERRADA_CON_ARREGLOS`,
(d) `CERRADA`, Tabla 1 `CERRADA`.

Primer lanzamiento fallido por formato: al `prompt.md` le faltaba la segunda línea `---`; no se
envió nada. Se añadió y se relanzó.

## Arreglos obligatorios

1. **Recuento de sitios en Layers(b).** Aceptado. Para un disco de radio² ≤ 2Rδ′ en un trasladado
   de una red plana, el recuento uniforme es O(1+Nδ′), no O(Nδ′) cuando δ′ → 0. La cota final
   CN^{-3} no cambia: (1+Nδ′)·δ′²/N²·N^{-2}(1+δ′) ≤ CN^{-3}(1+δ′)⁴. Cambiado en el texto.
2. **Fase global cerca de πu (Layers(c) y Assembly).** Aceptado; el defecto es anterior a las
   reparaciones. Comprobado: u·(x−x_*) = −(θ_N+j) porque √3δ = √3R − u·x = θ_N+j, y
   u·(y−y_*) = θ_N+j′; luego cada capa lleva e^{−iπθ_N}. En el producto,
   u·(y_*−x_*) = 3N − 2√3R = 3N − √3N/2, y
   e^{−2πiθ_N}·(−1)^N·(−1)^N e^{iπ√3N/2} = e^{−iπ√3N/2}e^{iπ√3N/2} = 1, ya que
   θ_N = {√3N/4}. Añadidas las fases a (c) y la cancelación a Assembly.

## Nota de exposición

En Assembly la cota del segundo reemplazo usaba S̃_N aunque el primero ya lo había sustituido.
Añadido que vale para los dos, pues ambos están acotados por Ce^{−Nη^TQη/4} (Lemma symbol(d)).

## Otras afirmaciones del informe, comprobadas después (2026-10-28)

A petición del usuario («los avisos de Astra revísalos tú»).

- **⟨C⟩ ≠ C̄ en las dieciséis filas.** Rehecho.
  - Expresión de W(ω). Con s = t_* + iω y Re(1/s) = t_*/|s|², se tiene
    |ĝ_τ(ω)|² = c_g² e^{−|τ|² t_*/(2√3|s|²)}/|s|⁸. La integral gaussiana da
    W(ω) = π c_g² / (|s|⁶ (q_t|s|² + t_*/(2√3))), igual que en el informe. Por Parseval, al ser
    𝒮_± reales, a = ⟨Γ₊⟩ − Γ̄ = 2Σ_{n≥1} W(2πn) y b = ⟨Γ₋⟩ = 2Σ_{n≥0} W(π(2n+1)).
  - Cociente b/a. W es decreciente en ω. Por tanto
    W(2πn)/W(π) ≤ [(t_*²+π²)/(4π²n²)]³ ≤ 0.0209/n⁶ < 1/(27n⁶), usando t_* = 0.7357… < 1 (salida
    de `verify_regional_directional_asymptotics_gate.py`). Como b ≥ 2W(π), queda
    b/a ≥ 27/ζ(6) ≈ 26.5. El informe da > 13.5; la cota es correcta pero conservadora.
  - |ℓ₀/ℓ_π|. Evalué en coma flotante las fórmulas cerradas del Apéndice A (inspección con
    `python3 -c`; no es un certificado). Datos: t_* = 0.73575281442, 𝓘₀ = 0.716577,
    𝓘₁ = 0.132252. Los C̄ reproducen la Tabla 1 con 5 cifras. En las filas de signo opuesto,
    |ℓ₀/ℓ_π| vale 0.124 (I,I), 0.605 (I,P₁), 1.106 (σ₁,I), 0.946 (σ₁,P₁) y 2.651 (σ₁,P₂). Las
    filas de σ₃ y P₃ repiten esos valores. Su máximo es 2.651 < 3. El margen frente a 26.5 hace
    irrelevante el error de coma flotante.
  - Conclusión. ⟨C⟩ − C̄ = 𝒦c_r(aℓ₀ + bℓ_π) ≠ 0 en todas las filas. La leyenda nueva no depende
    de esto.
- **θ_N ≥ 1/(8√3N)** (nota de astra; no se usa en el texto). Comprobado. Sea k = ⌊√3N/4⌋.
  Entonces θ_N = (3N² − 16k²)/(16(√3N/4 + k)). El numerador es un entero positivo, porque
  3N² = 16k² no tiene solución entera con N ≥ 1, y el denominador es ≤ 8√3N.
- **(e) con r₀ menor.** El informe precisa que la constante c de Lemma symbol(e) puede cambiar.
  Correcto, y compatible con el texto: «(e) holds for every r₀>0 by the same compactness
  argument» no fija c.
- **Cotas de S′, S″, S‴.** El informe precisa que valen para e > 0 y que la parte singular de la
  tercera derivada se cuenta aparte, en el borde. Es lo que hace el texto. Además
  |S‴| ≤ 12κ²e·κe² + 8κ³e³ ≤ Cκ²e, usando κe² ≤ π/2.

El revisor es de otra familia, pero los arreglos de esta segunda vuelta los escribió de nuevo una
sesión Claude; no han sido revisados.
