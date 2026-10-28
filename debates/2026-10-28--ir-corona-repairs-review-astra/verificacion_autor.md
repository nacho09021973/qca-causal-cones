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

## Lo que no he comprobado

La parte del informe sobre la Tabla 1 que va más allá de la leyenda (b/a > 13.5 y |ℓ₀/ℓ_π| < 3 en
las filas de signo opuesto, de donde ⟨C⟩ ≠ C̄ en las dieciséis filas) no la he rehecho:
`[UNVERIFIED]`. La leyenda no depende de ello.

El revisor es de otra familia, pero los arreglos de esta segunda vuelta los escribió de nuevo una
sesión Claude; no han sido revisados.
