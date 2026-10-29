# Lectura crítica del autor — revisión Grok de las reparaciones (isotropía irreducible)

Fecha: 2026-10-29. Rama base: `research/inverse-gravity-design` @ `57b8564`, con las
reparaciones sin commit. Autor de esta lectura: Claude. Las reparaciones las escribió Codex;
el certificado original, Claude. **No es una revisión independiente**: es la contrastación que
pide `prompt.md` («Cierre»). La revisión independiente es la de Grok.

## Intentos (todos conservados, sin editar)

| Carpeta | Resultado | Evidencia |
|---|---|---|
| `./` (2026-10-29 08:40Z) | `FAILED`, `Read-only file system (os error 30)` al crear la sesión del CLI | `estado_grok.json`, `grok.log`; no llegó al proveedor |
| `reintento-01/` (08:40Z–08:52Z) | `FAILED`, `reqwest error stream … cli-chat-proxy.grok.com` | `estado_grok.json`, `grok.log` |
| `reintento-02/` (09:20Z–09:31Z) | `COMPLETED` | `estado_grok.json`, `informe_grok.md` |

`prompt.md` permite un reintento operativo. El segundo (`reintento-02`) lo autorizó
expresamente el usuario en esta sesión, con una clave de API de xAI nueva pasada solo por
entorno. La nota de autorización está en la cabecera de `reintento-02/prompt.md`, fuera del
texto enviado. La clave no aparece en ningún fichero de esta carpeta (`grep -r`, sin
coincidencias). Herramienta: `revision_ciega.sh` @ `a32e189`. Documentos enviados: los mismos
cinco que en la revisión de Gemini, con los mismos sha256 (certificado `d4b3d242…1bfe4`,
informe `01db8e84…c9a1`).

## Veredicto del revisor

`ACCEPT_WITH_REPAIRS` global. Por punto: 1 ACCEPT; 2, 3 y 4 ACCEPT_WITH_REPAIRS; 5 sin
verificar por ejecución. No encuentra ningún error que fabrique el ideal `(1)` en T3, O3 u O4.
Pide tres reparaciones obligatorias, todas de redacción o alcance.

## Contraste de cada reparación

**G1 («rational arithmetic»).** **Se acepta: es correcta.**
`reports/2026-10-28--irreducible-isotropy-step01.md:76` dice «exact Groebner basis (grevlex,
rational arithmetic)». La representación de espín usa `sp.sqrt(sp.binomial(n, k))`
(`scripts/verify_irreducible_isotropy_step01.py:101`), que introduce `√2` (n = 2, 3) y `√3`
(n = 3), y los elementos de `2O` llevan `√2/2`. El cuerpo de coeficientes es una extensión
algebraica de `Q`, no `Q`. El docstring (`:7`, «rational/algebraic») es más fiel que el
informe. No cambia ningún resultado: el criterio de ideal unidad vale igual sobre esa
extensión.

**G2 («zero tolerance» frente a `nsimplify`).** **Se acepta como redacción.** `key()`
(`:63–64`) canoniza con `sp.nsimplify(simp(x))`, que identifica números con una aproximación
numérica. Las entradas de `2O` están en un conjunto finito y bien separado
(`0, ±1, ±1/2, ±√2/2`, y sus versiones con `i`), y el certificado comprueba `|2O| = 48`,
`|2T| = 24` y el homomorfismo sobre todos los pares. Una colisión es muy improbable, pero eso
no es una prueba. «Zero tolerance» exagera para la identidad de los elementos del grupo.

Los otros dos posibles falsos pases de su punto 2 no inclinan la conclusión hacia el vacío.
- Si `sym_zero` descartara por error una ecuación en `unitarity_equations`, el ideal quedaría
  más pequeño. Eso dificulta obtener `(1)`, no lo facilita.
- El filtro del estabilizador (`:202`) compara matrices de rotación enteras con un vértice
  entero, así que es exacto.

**G3 (alcance de los controles de dimensión).** **Se acepta: es correcta.** El bucle
(`:270`) solo prueba `2O` con `n = 1` y `n = 3`. El espín 1 (T3, O3) no tiene control. Rehecho
aquí: el estabilizador del vértice es la rotación de 2π/3; en espín 1 sus autovalores
`e^{∓2πi/3}` y `1` son simples, así que la dimensión compleja es 3. El informe (`:86–89`) dice
«adds dimension controls for that branch», que puede leerse como si cubriera las tres clases.

**Observación adicional (no obligatoria): «That class contains the Pavia symbols».**
`reports/…:86`. Grok tiene razón en que el certificado no comprueba que los símbolos de Pavia
sean un punto de la variedad Q8/espín 1/2. Control A comprueba intertwiners no nulos, no una
representación unitaria de `D2`. La frase se apoya en P17, no en el certificado.

## Conclusión del autor

- Ninguna objeción afecta al vacío de T3, O3 u O4.
- Las tres reparaciones son correctas y estrechan el alcance de lo que se afirma.
  - G1 y G3 son cambios de texto en el informe.
  - G2 puede resolverse en el texto (informe y `scripts/README.md`) sin tocar los bytes del
    certificado. La otra opción es cambiar el docstring o canonizar `key()` de forma exacta,
    pero eso exigiría revisar de nuevo ese fichero.
- Las dos revisiones de familias distintas coinciden: Gemini da `ACCEPT` y Grok
  `ACCEPT_WITH_REPAIRS`, con reparaciones de redacción. Ninguna pide rehacer cálculos.
- Este fichero no aplica las reparaciones ni promociona nada. Ambas cosas las decide el usuario.
