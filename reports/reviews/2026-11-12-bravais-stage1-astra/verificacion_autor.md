# Lectura del autor (sesión Claude, claude-opus-5-5), 2026-11-12

Informe: `informe_astra.md` (gpt-6-astra vía `codex exec` sellado,
`COMPLETED`, herramientas `7d111a1`, 15:58–16:04 UTC), sobre la base
`24e1965`. Candidato: `reports/2026-11-12--general-ir-rate-bravais-stage1.md`,
SHA256 `922162b8…4b1c` (coincide con la copia enviada, según la cabecera).
Una ronda, sin herramientas.

**Dictamen del revisor: REPAIR_REQUIRED.** No encuentra obstáculo
matemático específico de Bravais, ni hipótesis nueva necesaria, ni
contraejemplo; el resultado (b) es defendible tras las reparaciones. La
celda abierta de B2 sigue abierta. Rederiva por su cuenta la geometría de
§0 con los dos ejemplos, Fourier/convexidad/contorno/Schur, U6, la cola
libre, Poisson en clases, todas las constantes de §4 con la comprobación
`Z^3`, las fases y promedios de §5 y las observaciones de §6.

## Objeciones al candidato (comprobadas contra los documentos)

1. **Inventario incompleto: el determinante monomio (reparación necesaria).**
   Correcta. S01 (`reports/2026-11-12--general-ir-rate-stages-0-1.md:86`)
   usa que `det S(p)` de un símbolo unitario de Laurent es un monomio para
   que `Phi` sea finita; es un uso de la estructura de red que no figura en
   U1–U14. Se traslada sin hipótesis nueva (el revisor da dos argumentos:
   unidades del anillo de Laurent en `t = B^T p`, o `S S^sharp = I` como
   identidad de sumas exponenciales). **Aceptada; pendiente de aplicar.**
2. **U6 debe referirse a la celda de Voronoi (exposición).** Correcta: el
   umbral `N > 1/(pi lambda_1(L*))` es el de la celda de Voronoi centrada
   en cero (o de inyectividad de la bola en el toro), no el de cualquier
   zona fundamental; el «iff» es impreciso en el caso de igualdad.
   **Aceptada; pendiente.**
3. **§6.1 necesita «en general» (exposición).** Correcta: si
   `L = a Q Z^d` con `Q` ortogonal, el cambio es una semejanza y conserva
   bolas e isotropía. La conclusión (la extensión no se obtiene por un
   cambio de coordenadas que conserve la clase de B1) sigue en pie.
   **Aceptada; pendiente.**
4. **Delimitar el inventario frente a las comprobaciones de K3
   (exposición).** Correcta: LT §8 y la comprobación de K3 en S01 usan
   propiedades del paseo particular, no de la red; el inventario debe
   decir que cubre las demostraciones generales. **Aceptada; pendiente.**

Ninguna cambia hipótesis, constantes ni el veredicto propuesto; las cuatro
son reparaciones del texto del candidato.

## Notas sobre B1/B2 (fuera de esta carta; no deciden el dictamen)

- **Admisibilidad general: NO_VERIFICADO.** Coincide con la observación 3
  de §6 del candidato. El revisor matiza que una prueba futura en `L`
  tendrá ingredientes de red (el manuscrito usa diferencias en
  direcciones de la base de `Z^3`); la frase «no involucra la red» debe
  leerse solo como «la carencia ya existía». Aceptada como matiz.
- **H2 leída literalmente (objeción a B1).** Correcta según los textos:
  H2 (`theory/GENERAL_IR_RATE_GATE.md:93-96`) pide «Hessiana no degenerada
  de `log lambda`», y SP §3.1
  (`reports/2026-11-12--general-ir-rate-stage2-progress.md:60`) deduce de
  ella que `Q = Hess_xi log|lambda_0|` es definida positiva. Con
  `log lambda` holomorfa en `p = eta - i xi`, `Q = -Re H` siendo `H` la
  Hessiana compleja; `H` no degenerada no implica `Re H` definida
  negativa (la maximalidad en `eta` solo da semidefinida). El ejemplo del
  revisor lo muestra en una variable. La intención de H2 («análogo del
  lema 7.1(d) del manuscrito», que da `Q` definida positiva) es la lectura
  real, y el diagnóstico de la segunda ronda comprobaba la Hessiana real
  (`max(hessian_eigs) < -1e-6`), pero el texto de H2 no lo dice. Reparar
  exige una enmienda aclaratoria a la carta general (cambio de enunciado
  de una hipótesis), que decide el usuario. La revisión de Grok de B1 no
  lo señaló.

## Estado

Revisión registrada; reparaciones no aplicadas (pendientes de instrucción
del usuario). Etapa 1 sigue siendo `PROVED_UNDER_FROZEN_CONTRACT` de autor,
ahora con **una revisión cruzada REPAIR_REQUIRED** (cuatro reparaciones de
texto) y sin promoción.
