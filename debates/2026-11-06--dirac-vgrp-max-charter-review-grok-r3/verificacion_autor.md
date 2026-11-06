# Lectura del autor — ronda 3 de Grok, carta DIRAC_VGRP_MAX v4

Autor de la carta y de esta lectura: Claude Code (Claude Opus 5.5). Fecha: 2026-11-06.
Informe: `informe_grok.md` (modelo `grok-4.7`, estado `COMPLETED`, fin 11:50:38Z). Carta
revisada: `theory/DIRAC_VGRP_MAX_GATE.md` en `ef4c9f5`.

**Procedencia de la herramienta.** El `prompt.md` cita `~/herramientas` `ce09890`. Según
`estado_grok.json`, el lanzador corrió con `~/herramientas` en `97292a9`: el repositorio de
herramientas avanzó entre la ronda 2 y la ronda 3. Vale lo que dice `estado_grok.json`.

**Veredicto de Grok:** no congelar. El balance es este:
- de la ronda 2, nueve objeciones resueltas y dos parciales (G-V-R2-02, G-V-R2-04);
- de la ronda 1, G-V-05 queda resuelta y G-V-11 sigue parcial;
- hay nueve objeciones nuevas: un error demostrado, cinco lagunas y tres de redacción;
- el núcleo analítico se confirma por tercera vez.

**Lectura del autor:** acepto las nueve. Las he comprobado releyendo el texto de la v4, sin
cálculo nuevo. El error demostrado, G-V-R3-01, lo introdujo la v4: la frase de H3 verdadera
admitía «an isolated critical point» sin exigir que alcanzara el máximo.

| Id | Acepto | Comprobación del autor | Reparación propuesta para la v5 |
| --- | --- | --- | --- |
| G-V-R3-01 | Sí (error) | Un punto crítico que no maximiza y cae en `A` haría H3 verdadera, y a la vez el conjunto certificado podría hacerla falsa | Exigir que todo punto usado para H3 verdadera alcance el máximo certificado: punto crítico aislado con `Φ = V_grp^max(m)^2`, muestra con ese valor, o testigo de A5 |
| G-V-R3-02 | Sí | Las cajas de A3 están en `t` o en `t'`, no en `q` | Convertir de forma exacta a `q` (`q = 2 atan t` o `q = 2 acot t'`, con aislamiento por intervalos racionales de la imagen), refinar a anchura `≤ 1e-9` en `q` y medir la distancia `1e-6` a esas cajas. No cambia las cifras de D8 |
| G-V-R3-03 | Sí | Puede haber hasta cuatro clases de símbolo y había un solo veredicto por masa | Los veredictos son por par (masa, clase). `V_grp^max` se informa por clase. Las hipótesis se cuantifican sobre todos los pares, con la misma precedencia: un par que refuta refuta; confirmar exige todos los pares; en otro caso `UNDECIDED`. `STOPPED_EXACT_ROUTE_EXHAUSTED` cuando todos los pares quedan `OPEN` |
| G-V-R3-04 | Sí | Si el lugar singular del modelo compacto tiene dimensión positiva, sus puntos no forman una muestra finita | Reducción recursiva: restringir la misma lineal genérica al lugar singular y repetir, con la dimensión bajando en cada paso. Si no termina dentro del presupuesto, el certificado no existe y se pasa a A5 |
| G-V-R3-05 | Sí | Si A3 termina pero A4 no certifica, A5 no tenía disparador | A5 corre siempre que A3–A4 no certifique, por la causa que sea |
| G-V-R3-06 | Sí | Decir solo «available» permitía no emitir el conjunto, y entonces H3 nunca podía ser falsa | `MAXIMIZER_SET_CERTIFIED` se emite obligatoriamente cuando el camino cero-dimensional certifica el valor |
| G-V-R3-07 | Sí | En la Sec. 6, «until the Stage 0 literature check» sugiere que la lectura levanta la etiqueta | Repetir en la Sec. 6 la frase de la Sec. 0 |
| G-V-R3-08 | Sí | La Sec. 5 dice «OPEN» en lugar del token completo | Escribir `OPEN_AFTER_CRITICAL_POINT_ANALYSIS` |
| G-V-R3-09 | Sí | D7 dice que la regla es bilateral, pero para los techos es unilateral | D7: bilateral para el valor certificado; para `CEILING_ONLY`, la regla unilateral de B3 |

**Tendencia.** Ronda 1: 17 objeciones, 2 errores. Ronda 2: 11 objeciones, 3 errores. Ronda 3:
9 objeciones, 1 error. Las tres rondas han introducido, o heredado, errores en las frases
reparadas. G-V-R3-03 añade una regla nueva (veredictos por par masa–clase).

**Estado:** la carta sigue en DRAFT v4, no congelada. Si se escribe la v5 y si hay una cuarta
ronda, lo decide el usuario.
