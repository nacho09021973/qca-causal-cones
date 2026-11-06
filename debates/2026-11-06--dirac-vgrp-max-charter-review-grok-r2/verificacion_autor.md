# Lectura del autor — ronda 2 de Grok, carta DIRAC_VGRP_MAX v3

Autor de la carta y de esta lectura: Claude Code (Claude Opus 5.5). Fecha: 2026-11-06.
Informe: `informe_grok.md` (modelo `grok-4.7`, estado `COMPLETED`). Carta revisada:
`theory/DIRAC_VGRP_MAX_GATE.md` en `7697593`. Herramienta: `~/herramientas` `ce09890`.

**Veredicto de Grok:** no congelar.
- De la ronda 1, quince objeciones quedan resueltas y dos parciales (G-V-05 y G-V-11).
- Hay once objeciones nuevas: tres errores demostrados, cinco lagunas y tres de redacción.
- El núcleo analítico se vuelve a confirmar.

**Lectura del autor:** acepto las once. La comprobación consiste en releer el texto de la v3 y
rehacer a mano el argumento, sin cálculo nuevo. Dos de los errores demostrados los introdujo la
propia v3 al reparar la ronda 1:
- G-V-R2-01: el paro en A3 contradice A5;
- G-V-R2-03: mi ejemplo de la función lineal genérica.

| Id | Acepto | Comprobación del autor | Reparación propuesta para la v4 |
| --- | --- | --- | --- |
| G-V-R2-01 | Sí (error) | A3 declaraba `OPEN` cuando la muestra no cabía en el presupuesto; A5 y la Sec. 5 solo declaran `OPEN` si A5 tampoco termina | Un solo orden: si A3 falla, corre A5; `OPEN_AFTER_CRITICAL_POINT_ANALYSIS` solo si ninguna de las dos certifica. Se quita el veredicto del último inciso de A3 |
| G-V-R2-02 | Sí (error) | Un testigo de A5, o una muestra por componente, da el valor pero no el conjunto de maximizadores. T2 no tiene formato para una componente continua. Un punto fuera de `A` no refuta H3 | Separar dos veredictos por masa. `VGRP_MAX_VALUE_CERTIFIED` cubre T1, T3, H1 y H2. `MAXIMIZER_SET_CERTIFIED` cubre T2, solo en el camino cero-dimensional. H3 es verdadera en una masa si algún maximizador certificado está en `A`; falsa solo con el conjunto certificado; en otro caso esa masa no la decide |
| G-V-R2-03 | Sí (error) | En las cartas afines `t ∈ R³` el lugar no es compacto, así que una función lineal genérica puede no tener crítico en un trozo y perder la componente | Quitar el ejemplo de la lineal en las cartas. Se admite la descomposición cilíndrica algebraica, o una lineal genérica sobre el modelo compacto `(sᵢ, cᵢ)`, `sᵢ² + cᵢ² = 1`, incluyendo sus puntos singulares. En una componente compacta la lineal alcanza su máximo, que es crítico o singular |
| G-V-R2-04 | Sí | (iii) refinaba el intervalo del valor, no las cajas de `q`. No decía qué hacer si el refinamiento no converge, ni cómo tratar `CEILING_ONLY` | Refinar las cajas de `q` a anchura `≤ 1e-9`. Un refinamiento que no converge cuenta como desacuerdo. Para `CEILING_ONLY`, regla unilateral: el máximo de la malla y los máximos refinados `≤ V² (1 + 1e-9)`. La distancia `1e-6` de (iii) es una cifra nueva, fuera de D7: **la decide el usuario** |
| G-V-R2-05 | Sí | No se decía qué pasa si B veta después de que A haya decidido una hipótesis | El veto suspende los veredictos de hipótesis de las masas en desacuerdo. Esos veredictos no se registran como decididos ni se promocionan |
| G-V-R2-06 | Sí | «Published exactly» no es un predicado. Dos PDF de Pavía no zanjan el estado de Bernstein | `STOPPED_PRIOR_ART` solo si las páginas leídas dan de forma explícita el valor exacto de `max ‖∇_k ω‖` (o de su cuadrado) para esta familia, con quiralidad y masa identificables y unidades convertibles. Bernstein y la fórmula 1D quedan `[UNVERIFIED]` si esos PDF no los enuncian. Una lectura vacía no implica novedad |
| G-V-R2-07 | Sí | El paso 2 usaba `sin ω ≥ m`, que necesita `|u| ≤ 1`, demostrado solo en el paso 3 | Cambiar el orden: primero `|u| ≤ 1`, después ramas y multiplicidad |
| G-V-R2-08 | Sí | La Sec. 1 tomaba el máximo sobre `k ∈ BZ` con `u(k/√3)`, cuyo periodo en `k` es `2π√3` | Cuantificar sobre `q ∈ T³`: `V_grp^max(m)^2 := max_{q ∈ T³} Φ(q)` |
| G-V-R2-09 | Sí | «No other time is authorized» podía leerse como que las etapas 0 y B tienen presupuesto cero | Escribir «No other time is authorized for A or A5. Stages 0 and B do not widen the question» |
| G-V-R2-10 | Sí | La etiqueta tenía un solo hueco para la masa | `REFUTED_AT_m ∈ {…}`, con todas las masas que refutan |
| G-V-R2-11 | Sí | El abandono por cinco `OPEN` no tenía veredicto de puerta | Nuevo veredicto de puerta `STOPPED_EXACT_ROUTE_EXHAUSTED`, emitido exactamente cuando las cinco masas acaban `OPEN_AFTER_CRITICAL_POINT_ANALYSIS` |

**Estado:** la carta sigue en DRAFT v3, no congelada. El encargo admitía una ronda y ya se ha
hecho. Si se escribe la v4, si se fija la tolerancia espacial de B3 (iii) y si hay una tercera
ronda antes de congelar, lo decide el usuario.
