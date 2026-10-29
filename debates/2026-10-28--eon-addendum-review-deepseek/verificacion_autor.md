# Lectura crítica del autor — re-revisión DeepSeek de la adenda Eon

Fecha: 2026-10-29. Rama: `research/inverse-gravity-design` @ `57b8564`. Autor de esta
lectura: Claude, la misma familia que escribió la adenda. **No es una revisión
independiente**: es la contrastación que pide `prompt.md`. La revisión independiente es la de
DeepSeek.

## Intentos (todos conservados, sin editar)

| Carpeta | Resultado | Evidencia |
|---|---|---|
| `./` (2026-10-28) | sin respuesta; `lanzamiento.out` = `Terminated`; `deepseek.json` y `deepseek.log` vacíos | no llegó informe |
| `reintento-01/` (2026-10-29 09:32Z–09:41Z) | `COMPLETED`, `finish_reason: stop` | `estado_deepseek.json`, `informe_deepseek.md` |

El reintento es el único operativo que permite `prompt.md`. Lo autorizó el usuario en esta
sesión («si, autorizo a y b»). Antes de enviarlo, `sha256sum -c inputs.sha256` dio OK para los
cuatro documentos. El cuerpo de `reintento-01/prompt.md` es idéntico al original (`diff`); solo
se añadió una nota en la cabecera, que no se envía. Herramienta: `revision_ciega.sh` @
`a32e189` (el primer intento citaba `1656820`).

## Veredicto del revisor

`PASS_WITH_REPAIRS` global. Reparaciones 1, 2, 3, 5, 4.b, 4.c y 4.d: PASS. 4.a: PASS con
reparación obligatoria de formalización. Ningún error demostrado en la adenda. Siete
reparaciones obligatorias, todas de redacción o formalización.
`GAUSSIAN_TAIL_STATIONARITY_FAIL` no se discute.

Sobre G-R1-01, el revisor confirma la lectura de la adenda: con la convención del texto
(`f` es la serie de `phi`, `g` la de `psi`) la cota es correcta. G-R1-01 era una ambigüedad
de redacción, no un error.

## Contraste de cada reparación obligatoria

**D1–D2 (§3.B, «a=4» y «el código comprueba ese recuento en L=3,4»).** **Se aceptan en el
fondo.** `reports/2026-10-27--eon-projected-gaussian-reference.md:194–196` sigue diciendo ambas
cosas. La adenda (`:339–342`) las retira, pero el texto original no las marca. La práctica del
repo es conservar el texto y añadir una adenda; para cumplir con eso y evitar la contradicción
basta con anotar esas líneas con una remisión a la reparación 4 de la adenda, sin borrarlas.

**D3 (§3.C, `g(z)=exp[i theta B] f(z)` «absorbiendo en g la fase lambda»).** **Se acepta como
redacción.** `:217–218` sigue con la forma ambigua; la adenda (reparación 1) da la forma con
`lambda`. Mismo tratamiento que D1–D2.

**D4 (reducción de dos campos gauge por enlace a un entero).** **Se acepta: es una laguna
real.** La adenda dice que la reducción «se toma de §1», pero §1 (`:21–58`) solo dice que los
registros eléctricos son enteros; no deriva la reducción. Comprobado en la fuente primaria
(`biblioteca/arXiv-2205.03148v4.pdf`, texto extraído con `pdftotext`):
- p.6: cada enlace tiene un campo en cada extremo, `x:eta` y `(x+eta):-eta`, y «following the
  restriction that the two gauge fields of a link be of opposite signs, one has
  `E_{x:eta} = -E_{x+eta:-eta}`». El PDF presenta la restricción como una elección que elimina
  grados de libertad no exigidos por la invariancia gauge, no como consecuencia de ella.
- p.7, ec. (6): `V_{x:eta} = U_{x:eta} prod_y Z_y`, con `U` desplazando a la vez los dos
  extremos y `Z_y` diagonales.

Por tanto, dentro de esa restricción, un entero `E_l` por enlace es legítimo, y `V_l` es un
desplazamiento de ese entero por una fase diagonal ±1. Esto confirma el argumento de 4.a.

**D5 (ortonormalidad de `|E>'`).** **Se acepta como formalización.** Se sigue de D4: cada `V_l`
desplaza un solo entero y multiplica por una fase diagonal, así que `V_1^{E_1}···V_M^{E_M}|0>`
está soportado en una única configuración eléctrica. La adenda ya decía que `|E>'` difiere de
`|E>` en una fase; falta escribir por qué.

**D6 (prueba de que las cuatro plaquetas dan monomios distintos).** **Se acepta como
redacción.** La adenda lo afirma; el revisor da la prueba (dos plaquetas a cada lado del enlace
en cada uno de los dos planos que lo contienen; para `L>=3` sus otros enlaces son conjuntos
distintos). Coincide con la lectura del autor de la ronda anterior
(`../2026-10-28--eon-gaussian-review-deepseek/verificacion_autor.md`, G-R1-04).

**D7 (convención de signo entre `|E>'` y la base eléctrica).** **Se acepta como redacción.**

**NO VERIFICADO del revisor.** `plaquette_flow` está en `scripts/verify_eon_reference_state.py`,
que no se le envió. No afecta: la adenda ya no se apoya en ese recuento.

## Conclusión del autor

- La adenda pasa la re-revisión. Lo que queda son siete reparaciones de redacción o
  formalización, sin cambio de veredicto.
- La única con contenido es D4, y la fuente primaria la confirma (PDF p.6 y p.7, ec. (6)).
- Para aplicarlas sin reescribir el texto original, propongo:
  - una segunda adenda breve con D4–D7, citando PDF p.6 y p.7;
  - anotaciones de remisión en `:194–196` y `:217–218` para D1–D3.
  Es decisión del usuario, igual que si hace falta otra ronda.
- El certificado y el JSON no cambian. Este fichero no promociona nada.
