# Lectura del autor: revisión de Grok de la respuesta «c en distintos sustratos»

**Fecha:** 2026-11-03. **Autor de la respuesta y de esta lectura:** Claude Code
(Claude Opus 5.5). **Revisión:** `informe_grok.md` (grok-4.7, sellado,
COMPLETED, 0 llamadas a herramienta; herramienta `ce09890`). **Base:**
`dac86d8`; respuesta revisada con SHA-256 `39ef1625…` (`inputs.sha256`).

El informe de Grok no es fuente: cada reparación se ha contrastado con el
texto de `state/CURRENT_STATE.md` (CS) o de los informes, con la línea citada.

**Dictamen de Grok:** REPAIR_REQUIRED (puntos 1-4), PASS en el punto 5
(contenido propio). Diez reparaciones obligatorias.

| R | Objeción | Comprobación | Decisión |
| --- | --- | --- | --- |
| 1 | `c_0 = 1/3, 1/2, 3/4` «en un sustrato hexagonal» | CS:2320 solo pone ADMP y JDW L6d en el sustrato idéntico; L6b es `s = 6` (CS:2324) | Aceptada; aplicada |
| 2 | «el techo se alcanza según el sustrato» ignora L3s4 en el mismo `N_3` | CS Sec. 4.1 (`c_0 = a/sqrt3`) | Aceptada; aplicada |
| 3 | falta el cuantificador `s = 2`, `F ⊆ {0} ∪ vert(H)`; `OPEN` limitado al resto de `W_hex` | CS:110-111, CS:2359-2364 | Aceptada; aplicada en Secs. 0, 2, 4 y 5 |
| 4 | «any fixed `s` and representation» no está en CS 7.2 | CS:625-628: conos admitidos, soporte exacto en `N_3`, nodos degenerados, colisiones; no desplazamientos inconmensurables | Aceptada; aplicada con el cuantificador de CS |
| 5 | «even the long-run propagation speed is not fixed by the substrate» | L6b no está en el conjunto de pasos de L6a/L6d (CS:2320-2325) | Aceptada; sustituida por «`r_in` no fuerza `c_strict^iso = r_in` (fila L6b)» |
| 6 | velocidad de grupo `c_0(1 + 2 beta |k|)` no está en CS Sec. 13 | Cierto para CS; pero está en el informe de ejecución del gate promocionado, `reports/2026-11-02--dispersion-corrections-across-lattices.md:189` (`|grad eps_+|/c_0 = 1 + 2 beta t + O(t^2)`), que Grok no recibió | Aceptada **como reparación de cita**: se conserva, citando ese informe; «radial» corregido a `|grad eps_+|` como en la fuente |
| 7 | `a* ≈ 0.412` en vez del valor exacto | CS:2430 `a* = sqrt3 sqrt(17 - sqrt154)/9` | Aceptada; aplicada |
| 8 | filas con masa como moneda aparte y anisotropía de L6e no están en CS 11 | Cierto para CS (CS:2329-2330 solo da el resumen); está en `reports/2026-11-01--c-across-lattices.md:202-229` (tabla y lecturas 1-3), informe de la tabla promocionada | Aceptada **como reparación de cita**: se conserva, citando ese informe; se añade `c_H < c_omega2 < r_in` de la familia estándar (CS Sec. 5) |
| 9 | cubo `[-1,1]^3` con `r_in = 1/sqrt3` mezcla unidades | CS:762, CS:908: `C_micro = [-1,1]^3`, `r_in = 1` en unidades de la Sec. 8 | Aceptada; la celda declara el reescalado a paso máximo 1. Citas de L1/L2 a CS Sec. 5 y de L6a/L6d al informe hexagonal |
| 10 | la Sec. 5 cita el informe de líneas (M1), fuera del corpus enviado | El informe existe, pero no es un resultado promocionado | Aceptada; frase suprimida |

**Aclaraciones de Grok** («anticommute», «five sources», lectura del «so» de
0.2, «no novelty»): «five sources» se cita ahora a
`reports/2026-11-01--c-across-lattices.md`; se añade a la Sec. 4 que no se
cierra `NOVELTY = OPEN` del techo hexagonal ni se afirma que todo walk BCC
declarado alcance el techo. «Anticommute» se deja como glosa de T1.

**Valores:** ningún valor de la tabla ni ningún veredicto ha cambiado.

**Contenido propio (punto 5) y criterio de cierre del plan (Sec. 4):** Grok
da PASS y la lectura del autor coincide: tras las reparaciones la respuesta
sigue diciendo qué fija el sustrato (el techo `r_in` y si se alcanza en las
filas declaradas) y qué no fija (`c_0`, y en L6b ni siquiera
`c_strict^iso = r_in`). **El criterio de cierre no se cumple.**

**Estado:** la respuesta sigue PRELIMINARY como síntesis. Una re-revisión
acotada de las reparaciones, o una segunda casa, queda a decisión del usuario.
