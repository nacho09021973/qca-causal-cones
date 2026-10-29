# Lectura crítica del autor — revisión Gemini de las reparaciones (isotropía irreducible)

Fecha: 2026-10-29. Rama base: `research/inverse-gravity-design` @ `57b8564`, con las
reparaciones sin commit. Autor de esta lectura: Claude. Las reparaciones las escribió Codex;
el certificado original, Claude. **No es una revisión independiente**: es la contrastación que
pide `prompt.md` («Cierre»). La revisión independiente es la de Gemini.

## Intentos (todos conservados, sin editar)

| Carpeta | Resultado | Evidencia |
|---|---|---|
| `./` (2026-10-29 08:39Z) | `FAILED`, curl exit 6: `Could not resolve host: generativelanguage.googleapis.com` | `estado_gemini.json`, `gemini.log`; no llegó al proveedor |
| `reintento-01/` (2026-10-29 09:20Z) | `COMPLETED`, `finish_reason: STOP`, 09:20:58Z–09:21:49Z | `estado_gemini.json`, `informe_gemini.md` |

`reintento-01` es el único reintento operativo que permite `prompt.md`; lo autorizó el usuario
en esta sesión («si, autorizo»). Los dos `prompt.md` son idénticos (`cmp`) y las dos entradas
tienen el mismo sha256 `bc82d98d…6fad`. Herramienta: `revision_ciega.sh` @ `a32e189`.

Documentos enviados (sha256 de la cabecera de procedencia, iguales a los ficheros actuales del
árbol de trabajo, comprobado con `sha256sum`):

- `theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md` `bb12375f…76a6`
- `reports/2026-10-28--irreducible-isotropy-step01.md` `01db8e84…c9a1`
- `scripts/verify_irreducible_isotropy_step01.py` `d4b3d242…1bfe4`
- `scripts/certificate_utils.py` `5a3591e1…70ba`
- `debates/2026-10-28--irreducible-isotropy-step01-review-deepseek/reintento-01-red/informe_deepseek.md` `d9499ba9…0949`

## Veredicto del revisor

`ACCEPT` global, sin reparaciones obligatorias. Por punto: 1 ACCEPT, 2 ACCEPT, 3 ACCEPT,
4 ACCEPT, 5 ACCEPT (distinción de niveles). El revisor no ejecutó código y marca como
NO VERIFICADO las bases de Gröbner, los pases 33/33 y 47/47, los sha256 y los módulos
importados no adjuntos (`cert_Aa_s4_counterexample.py`, `verify_weyl_dirac_gate.py`).

## Contraste de sus afirmaciones

**Punto 1 (alcance de `E`).** Se acepta. El certificado construye `E` como `χ_4 − T2`
(`scripts/verify_irreducible_isotropy_step01.py:251`), lineal; `E1/2` y `E5/2 = E1/2 · A2`
son espinoriales (`:252–253`). El texto reparado del informe y el docstring excluyen `E`.

**Punto 2 (comparaciones simbólicas).** Se acepta. `sym_zero`
(`scripts/certificate_utils.py:13–18`) simplifica a cero tras reescribir en exponenciales.
Quedan dos comparaciones estructurales, que el revisor señala solo en parte:
- `:142` (`diagonal_sign`, `img == e or img == -e`): compara matrices enteras de signo y
  permutación. Si fallara, `next()` lanza `StopIteration` y el script sale con error.
- `:164` (`sum(d ** 2 …) == order`): dimensiones ya simplificadas a enteros. Un fallo hace
  fallar el `require`.
Ninguna puede producir un falso pase. No requieren reparación.

**Punto 3 (dimensiones 2 y 6 del conmutante).** Derivación rehecha aquí por separado. El
estabilizador de `(1,1,1)` en `O` es la rotación de ángulo 2π/3 en torno a ese eje. Sus
autovalores en espín `j` son `e^{-i m 2π/3}`, `m = −j…j`:
- espín 1/2: `e^{∓iπ/3}`, distintos, conmutante 1 + 1 = 2;
- espín 3/2: `e^{∓iπ}` = −1 (dos veces) y `e^{∓iπ/3}`, conmutante 1 + 1 + 4 = 6.
Coincide con el revisor y con el control (`:267–274`). Que el preimagen en `2O` sea cíclica de
orden 6 no cambia el conmutante, porque `−I` actúa como escalar. El revisor reconoce que el
recuento no prueba por sí solo la completitud de la parametrización; el informe reparado lo
dice. Su argumento de inyectividad (cada símbolo libre de `linsolve` aparece aislado) es
plausible y no lo he comprobado. `[UNVERIFIED]`

**Punto 4 (`EMPTY_CLASS`, sobreafirmaciones).** Se acepta. No encuentro afirmaciones que
excedan el alcance declarado en el texto reparado.

**Punto 5 (ejecución).** Correcto. Los pases 33/33 (683 s) y 47/47 los ejecutó el autor de
las reparaciones; esta sesión no los ha vuelto a ejecutar.

## Conclusión del autor

- La revisión de una familia distinta acepta las reparaciones R1–R4 sin reparaciones nuevas.
  Las dos comparaciones `==` que quedan fallan cerradas.
- Lo que la sección 6 de la carta pide para salir de PRELIMINARY está cubierto por esta
  revisión, sujeto a la lectura de la revisión de Grok (`../2026-10-29--irreducible-isotropy-repairs-review-grok/`).
- Este fichero no promociona nada ni cambia `state/CURRENT_STATE.md`. Promover es decisión
  del usuario.
