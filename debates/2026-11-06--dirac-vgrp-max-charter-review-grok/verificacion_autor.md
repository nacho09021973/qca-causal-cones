# Lectura del autor — revisión ciega de Grok, carta DIRAC_VGRP_MAX v2

Autor de la carta y de esta lectura: Claude Code (Claude Opus 5.5). Fecha: 2026-11-06.
Informe: `informe_grok.md`. Modelo `grok-4.7`, estado `COMPLETED`, cero llamadas a herramientas,
sha256 de la respuesta `b2b276fe…06ad3f`. Carta revisada: `theory/DIRAC_VGRP_MAX_GATE.md` en
`5ebe10d`, sha256 de la copia enviada `731058c4…6027`. Herramienta: `~/herramientas` `ce09890`.

**Veredicto de Grok:** no congelar (en la práctica `NOT_READY`). El núcleo analítico es correcto
(`ω`, `k = sqrt(3) q`, `Φ`, `|n u| ≤ n < 1`) y la separación de velocidades se respeta. Hay
diecisiete objeciones: dos errores demostrados, once lagunas y cuatro de redacción.

**Lectura del autor:** acepto las diecisiete. He comprobado cada una contra el texto de la carta;
la comprobación consiste en releerlo y rehacer a mano el argumento, sin cálculo nuevo. Ninguna
cambia la pregunta, la familia ni las masas; todas cambian el procedimiento o la redacción. Una
revisión de la misma familia que el autor no cuenta como verificación; esta lectura solo registra
qué acepto y qué propongo cambiar.

| Id | Acepto | Comprobación del autor | Reparación propuesta para la v3 |
| --- | --- | --- | --- |
| G-V-01 | Sí | En `m = 0`, `ω` no es diferenciable en el nodo (la carta lo dice en Sec. 2). Lo que el verificador iguala con `r_in` es la pendiente lineal en el nodo, no una velocidad de grupo | Escribir «massless linear slope at the node (`m = 0`) equals `r_in`» |
| G-V-02, G-V-12, G-V-16 | Sí | `c_H` y `c_{ω²}` contienen `arcsin` de un racional, que es trascendente. A4 solo compara números algebraicos. T3 pide un signo que la carta no sabe calcular y que choca con la Sec. 6 | Quitar `c_H` y `c_{ω²}` de T3. T3 queda con los signos algebraicos `V − r_in` y `V − V_causal^max`. `c_H` y `c_{ω²}` solo se citan, sin comparación certificada |
| G-V-03 | Sí | `q_i = −π` está en el cubo declarado y es singular en las dos cartas | Declarar la zona como el toro `R³/(2πZ)³`. Las cartas se aplican a clases, y la implementación usa representantes en `(−π, π)` o `(0, 2π)` según la carta |
| G-V-04 | Sí | Una eliminación por resultantes puede añadir soluciones si se anula el coeficiente director | Todo cero real que salga de la eliminación se comprueba exactamente en la ecuación crítica sin despejar, o se usa el ideal saturado por los denominadores. Un cero que no pase se descarta y se registra |
| G-V-05 | Sí (error) | Sobre un conjunto crítico de dimensión positiva, `dΦ = 0`, así que `Φ` es constante en cada componente conexa real. «Restringir y repetir» no termina y no da el máximo | Si hay dimensión positiva: un punto muestra exacto por componente conexa real, con certificado de que cubre todas. Si eso no se certifica dentro del presupuesto: `OPEN_AFTER_CRITICAL_POINT_ANALYSIS` para esa masa |
| G-V-06 | Sí | Una SOS con coeficientes racionales exige `V² ∈ Q`, mientras que T1 admite un algebraico no racional | A5 da un techo racional (`CEILING_ONLY`), salvo que haya un testigo exacto con igualdad. El testigo solo puede salir de un cero real certificado de A3 (aunque A3 no haya terminado del todo), nunca de B |
| G-V-07 | Sí | La tabla de la Sec. 2 ordena verificar el signo y la multiplicidad de `±ω`, pero la lista de la etapa 0 no lo incluye | Nuevo paso de la etapa 0: `D² − 2 n u D + I = 0`, `tr D = 4 n u` y `sin ω ≥ m > 0` implican los autovalores `e^{±iω}`, cada uno con multiplicidad 2 |
| G-V-08 | Sí | Que `u` sea invariante no implica que `‖∇_k ω‖` lo sea | Solo se admiten permutaciones con signo de `q`, que son ortogonales en `k` porque la escala `sqrt(3)` es isótropa. Para cada una se comprueba exactamente `Φ∘S = Φ`, y los maximizadores se reconstruyen por la órbita |
| G-V-09 | Sí | El `Φ` de la carta lleva el factor `n²/3` de `d = 3`, mientras que C0 pide `max = n²` | C0 usa su propia función `Φ₁(q) = n² sin² q / (1 − n² cos² q)` en `d = 1`, con `max Φ₁ = n²` en `q = ±π/2` |
| G-V-10 | Sí (error) | «A finite scan proves no global maximum» se lee como «demuestra que no hay máximo». Además, B sí produce un veredicto de puerta | Reescribir: «a finite scan does not prove a global maximum». B puede vetar (parar la puerta), pero nunca certifica un valor ni decide una hipótesis |
| G-V-11 | Sí | La tolerancia quedaba al script, y la pertenencia a una caja en coma flotante no es exacta | Fijar en la carta, antes de ejecutar nada: el máximo refinado de B2 debe distar del máximo exacto (pasado a coma flotante) menos de `1e-9` relativo, en los dos sentidos. Cualquier máximo local refinado con `Φ` por encima del máximo exacto más `1e-9` relativo provoca el veto. Las cifras son propuesta del autor y las decide el usuario |
| G-V-13 | Sí | `REFUTED` choca con `UNDECIDED`, y `CEILING_ONLY` no tiene traducción a hipótesis | Reglas: `REFUTED` si alguna masa refuta, aunque otras queden abiertas; `CONFIRMED_AT_DECLARED_MASSES` solo si las cinco certifican; si no, `UNDECIDED`. Con `CEILING_ONLY`, un techo racional `< 1/3` confirma H2 en esa masa y un techo `< n²/3` refuta H1; en los demás casos esa masa no decide |
| G-V-14 | Sí | En el toro, «eje coordenado» no define un conjunto | `A := {q : al menos dos coordenadas ≡ 0 o π (mod 2π)}`. H3 es existencial: algún maximizador está en `A` |
| G-V-15 | Sí | El presupuesto no tiene techo en el número de clases, el de A5 es ambiguo, y «no s = 4» no estaba definido | Como mucho cuatro clases de símbolo; A5, 900 s por masa y clase, una sola vez. «No s = 4» pasa a ser «no the s=4 family of `S4_STRICT_CONE_COUNTEREXAMPLE.md`» |
| G-V-17 | Sí | Afirmar prior art contradice la Sec. 0, que deja la lectura de la literatura pendiente | Reescribir: «the prior-art status of the 1D formula and of Bernstein-type bounds is `[UNVERIFIED]` until the Stage 0 literature check» |

**Además (del autor, no de Grok).** Desde 2026-11-06, `CLAUDE.md` exige que cada carta registre
qué resultado obligaría a abandonar la línea, separado de los veredictos por hipótesis. La v2 no
lo hace. Propuesta para la v3:
- se abandona la línea si la lectura de la etapa 0 encuentra `V_grp^max` de esta familia ya
  publicado de forma exacta;
- se abandona la ruta exacta para esta familia, sin carta nueva con otro método, si las cinco
  masas acaban `OPEN_AFTER_CRITICAL_POINT_ANALYSIS`.

**Estado:** la carta sigue en DRAFT v2, no congelada. Aplicar las reparaciones da una v3. Si la v3
necesita otra ronda de revisión acotada antes de congelarse, y si se aceptan las cifras de
G-V-11, lo decide el usuario.
