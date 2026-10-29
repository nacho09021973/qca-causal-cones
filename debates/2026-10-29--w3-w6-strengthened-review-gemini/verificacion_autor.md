# Lectura crítica — revisión Gemini de W3/W5/W6 reforzados y reparaciones W4

Fecha: 2026-10-29. Rama: `research/inverse-gravity-design` @ `3f4c972`. Autor de esta
lectura: Claude, que preparó el encargo. Codex escribió el refuerzo y las reparaciones; Claude
hizo la reconstrucción tipográfica. **No es una revisión independiente**: es la contrastación
que pide `prompt.md`. La revisión independiente es la de Gemini.

## Ejecución

Un solo intento: `COMPLETED`, `finish_reason: STOP`, 09:43:26Z–09:45:26Z. El modelo fue
`gemini-4-argon` con `thinkingLevel=medium`, sin herramientas. Antes de enviar,
`sha256sum -c inputs.sha256` dio OK para los 19 documentos, todos en commits. Herramienta:
`revision_ciega.sh` @ `a32e189`. El usuario confirmó el envío en esta sesión («si a las 3
preguntas»).

Antes de enviar se borró la entrada armada por `preparar.sh` (`REVISION_SOLO_ENTRADA=1`) y
el lanzador la volvió a generar. La cabecera de `prompt.md` cambió de PREPARED_NOT_SENT a SENT
antes del envío; esa cabecera no se envía.

## Veredicto del revisor

`ACCEPT` en el bloque A (W3/W5/W6), en el bloque B (W4) y en el global. No encuentra ningún
error ni laguna probatoria. Hace dos observaciones informativas:

- W36-G-01: el contrato y el verificador de rigidez W4 (`W4_GEOMETRY_STIFFNESS_GATE.md`) no
  se adjuntaron.
- W36-G-02: falta un comentario sobre `PAULI[2]` en el bloque F1.

## Contraste

Comprobaciones hechas en esta sesión:

- **Direcciones.** `DIRECTIONS = ((1,0,0),(1,1,0),(1,1,1))` (`scripts/tetrad_transport.py:12`):
  todas tienen primera componente 1, como usa el argumento de paridad del revisor.
- **Expansión de W4.** De `F_eps = sin 2kappa` y `F_kk = -sin² kappa` sale
  `eps'' = tan(kappa)/2`, es decir, `eps = tan(kappa) k²/4`. Coincide con la auditoría.
- **Tamaños de toro.** El revisor deriva la validez del calendario para la red infinita y
  toros de lado par `>= 4`. El informe de refuerzo dice lo mismo
  (`reports/2026-10-26--w3-w6-certificate-strengthening.md:101–102`).
- **W36-G-02.** En `scripts/verify_w6_full_spatial_tetrad.py:67–69`, `T` usa `PAULI[2]` como
  la Z del registro geométrico. Es correcto. Añadir el comentario cambiaría los bytes de un
  verificador revisado; no se aplica.
- **W36-G-01.** Es correcta como límite de alcance. La rigidez W4 ya tuvo su revisión del
  2026-10-22 y no estaba en este encargo.

Observación propia que el revisor no señala:
`scripts/verify_w4_long_wavelength_spectrum.py:70,72` usa `==` y `!=` estructurales.
- `== -sp.I` falla cerrado.
- `mutated_trace != -sp.I` podría pasar en falso si SymPy dejara sin simplificar una forma
  igual a `-i`. El valor es 1 (comprobado por el revisor y aquí: `2(1/2 - 0) = 1`), así que no
  hay fallo, pero el control de mutación es estructural.

Cautela: la revisión es un `ACCEPT` completo, obtenido en dos minutos y con esfuerzo medio.
Un solo revisor que acepta todo no descarta errores que no buscó. Las revisiones anteriores
de W3–W6 (DeepSeek y Astra, 2026-10-22) sí pidieron reparaciones, y esta revisión dice que se
cumplieron.

## Conclusión

- Los certificados reforzados de W3, W5 y W6 y las reparaciones de W4 tienen ahora una
  revisión independiente de una familia distinta, con resultado `ACCEPT` y sin reparaciones
  obligatorias.
- W1–W12 sigue `CLOSED_BY_CONTRACT`; esta revisión no la reabre.
- Este fichero no cambia `state/CURRENT_STATE.md` ni promociona evidencia. Registrar
  `NEW_INDEPENDENT_REVIEW_PENDING → REVIEWED_ACCEPT` es decisión del usuario.
