# Revisión de la propuesta documental sobre PS′ (autor Codex) por Claude

Fecha: 2026-11-04. Encargo del usuario: «como el texto es de Codex haz tú la
revisión». Revisor: Claude Opus 5.5 (Anthropic), familia distinta de la del
autor (Codex, OpenAI). Base: `757d13f` (local). Herramientas compartidas:
ninguna usada (`~/herramientas` en `ce09890`, sin `revision-ciega`).

Candidato revisado:
`reports/2026-11-04--ps-prime-intrinsic-definition-proposal.md`,
SHA256 `1163873f353b4d187de78716057f068d8d71cc88b1d590a84321596cd08279e9`.

## Límites de independencia

- **No es ciega.** El revisor tenía el contexto completo de la sesión y ya
  había hecho una lectura documental del borrador (cuyas tres peticiones
  incorporó el autor).
- **Entradas del propio revisor.** La propuesta se apoya en la traza G1
  (`reports/2026-11-04--substrate-saturation-phase0-G1-trace.md`), redactada
  por Claude y revisada por gpt-6.1-sol. En lo que la propuesta toma de esa
  traza, esta revisión no es independiente; por eso los hechos de L6e se
  comprobaron otra vez desde la fuente primaria (abajo, punto 2).
- Revisión de otra familia respecto al autor, pero no sustituye una revisión
  sellada si el usuario quiere usar la propuesta como base de una enmienda.

## Comprobaciones

1. **Contrato.** `theory/SUBSTRATE_SATURATION_PHASE0_GATE.md` Sec. 1 define
   PS′ para «a product of `n` coin–partial-shift factors» y sus generadores
   reducidos; no elige presentación ni cuantifica sobre factorizaciones. Sec.
   2, punto 1, fija el cuantificador existencial sobre walks del sustrato.
   Lo que dice la propuesta (Sec. 0, Sec. 2) concuerda.
2. **L6e desde la fuente primaria.** `sources/1803.01304v1.pdf` p.2 (texto
   extraído con `pdftotext -layout`): `Ŵ0 = Ŵ3 Ŵ2 Ŵ1`, `Ŵj = Ûj Ŝj`,
   `Ûj = U(0, 0, −π/2, (j−2)π/4)` (Eq. (6)); vecinos `X1 = (x+ε, y)`,
   `X2 = (x+ε/2, y+ε/2)`, `X3 = (x−ε/2, y+ε/2)`, `X4..X6` opuestos;
   `(Ŝj Ψ)(X) = (ψ^L(N_j(X)), ψ^R(N_{j+3}(X)))`.
   - `j = 2`: `θ = 0`, `ξ = 0`, `α = 0`; con Eq. (1), `U = I` para cualquier
     `ζ`. Luego `Ŵ3 Ŵ2 = Û3 Ŝ3 Ŝ2`: la fusión no requiere conmutar nada.
   - Desplazamientos por paso (L se mueve a `−N_j`, R a `−N_{j+3}`):
     `±(1,0)`, `±(1/2,1/2)`, `±(−1/2,1/2)` en unidades de `ε`. El factor
     fusionado `Ŝ3 Ŝ2` mueve L por `−(0,1)` y R por `+(0,1)`: es simétrico,
     `±a` con `a = (0,1)`, así que la presentación de dos factores está en la
     clase producto en el sentido de Sec. 1.
   - Zonótopo de la presentación impresa: vértices `±(2,0)`, `±(1,1)`,
     `±(1,−1)` (seis); el de la fusionada: `±(1,1)`, `±(1,−1)` (cuadrado).
     `EXPECTED_MASSLESS` (l. 74–80 del script) registra 4 vértices y
     `r_in = c_0 = √2/2` para L6e, coherente con el cuadrado normalizado
     (lado mayor `√2` → 1). Faltan pues `±(2,0)` (`±(2,−2)` en coordenadas
     `ISO`), como dice la tabla de la Sec. 1.
   - Las líneas citadas del script (`u2` 92–97, `jdw_shift` 303–305, `ISO`
     348–349, `row_L6e` 352–364) implementan lo mismo.
3. **Biblioteca.** `biblioteca/INDICE.md` existe en este checkout y no tiene
   entrada de JDW 1803.01304 (búsqueda por `1803`, `jay`, `debbasch`).
   Coincide con la Sec. 1.
4. **Lógica de la recomendación.** Si dos presentaciones del mismo operador
   dan distinto valor de verdad a «exactamente `d` direcciones reducidas
   independientes», el predicado no es función del operador. Es inmediato y
   L6e lo realiza. La recomendación no va más allá: no declara imposible una
   regla, no emite veredicto sobre PS′, no toca PH.
5. **Sec. 3, opción de vértices.** Si `Z(P) = conv F`, el número de
   direcciones reducidas lo fija el cuerpo, y «exactamente `d`
   independientes» equivale a «paralelepípedo». Correcto como condicional
   sobre el criterio que el propio contrato enuncia (con fuente no leída,
   como la propuesta advierte).
6. **G1-a.** Centrar un desplazamiento asimétrico `(u, v)` produce la
   traslación `(u+v)/2`, que puede no pertenecer al grupo original. La
   propuesta dice «may» y no adopta la ampliación. Correcto.
7. **Estado.** PH, G1-a/b/c, fase 0 y `CURRENT_STATE` quedan sin cambio en el
   texto; la propuesta no promueve nada.

## Aclaraciones (no bloqueantes)

- **A1.** Sec. 1, tabla: la presentación fusionada pertenece a la clase
  producto porque el factor `Ŝ3 Ŝ2` es simétrico, `±(0,1)`. La propuesta lo da
  por hecho; conviene escribirlo, pues sin ello «dos direcciones» no sería un
  recuento de PS′.
- **A2.** Sec. 3, opción de vértices: la equivalencia con «paralelepípedo»
  supone que los generadores generan `R^d` (cuerpo de dimensión plena). Vale en
  todas las filas del expediente; conviene decirlo.

## Dictamen

**PASS.** Sin reparaciones obligatorias. Dos aclaraciones no bloqueantes
(A1, A2). La adopción de la recomendación sigue siendo decisión del usuario;
este dictamen no la adopta ni promueve nada.
