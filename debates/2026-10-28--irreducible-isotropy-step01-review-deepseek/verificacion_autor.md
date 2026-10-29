# Lectura crítica del autor — revisión DeepSeek de los pasos 0–1 (isotropía irreducible)

Fecha: 2026-10-29. Rama base: `research/inverse-gravity-design` @ `57b8564`.
Autor de esta lectura: Claude (la misma familia que escribió la carta, el certificado y el
informe). **No es una revisión independiente**: es la contrastación que pide `prompt.md`
(«Cierre»). La revisión independiente es la de DeepSeek.

## Intentos (todos conservados, sin editar)

| Carpeta | Resultado | Evidencia |
|---|---|---|
| `./` (2026-10-28 19:04) | sin respuesta; `lanzamiento.out` = `Terminated`; `deepseek.json` y `deepseek.log` vacíos | proceso terminado a las 19:12 |
| `reintento-01/` (2026-10-29 08:34) | `FAILED`, curl exit 6: `Could not resolve host: api.deepseek.com` | `estado_deepseek.json`; no llegó al proveedor |
| `reintento-01-red/` (2026-10-29 08:35) | `COMPLETED`, `finish_reason: stop`, 07:35:30Z–07:52:14Z | `estado_deepseek.json`, `informe_deepseek.md` |

Las tres entradas tienen el mismo sha256 `36df225f…e910`, y los tres `prompt.md` son idénticos
(comprobado con `cmp`). Los cinco documentos enviados no han cambiado entre `88b07ed` y
`57b8564` (`git diff --stat 88b07ed HEAD` vacío). Herramienta de los reintentos:
`revision_ciega.sh` @ `a32e189`; `prompt.md` cita `83c04f9`, que era el commit del primer
intento.

`prompt.md` permite «un reintento operativo si falla el transporte». El primer reintento no
llegó a enviar nada (fallo de DNS); el segundo es el que llegó al proveedor. Lo anoto para que
el usuario decida si cuenta como el único reintento permitido. Esta sesión no lanzó ningún
intento; encontró `reintento-01-red` en curso y esperó a que terminara.

## Veredicto del revisor

`ACCEPT_WITH_REPAIRS` global. Por punto: 1 ACCEPT, 2 ACCEPT, 3 REJECT de la afirmación de
cobertura (dimensiones correctas), 4 ACCEPT_WITH_REPAIRS, 5 NO VERIFICADO, 6 ACCEPT_WITH_REPAIRS.
El revisor no ejecutó código.

## Contraste de cada reparación con el certificado

**R1 (cobertura, `E` lineal de 2O).** **Se acepta: es correcta.** La tabla del propio certificado
construye `E` como `χ_4 − T2` (`scripts/verify_irreducible_isotropy_step01.py:246`), es decir,
como representación lineal (trivial en `−I`). `E1/2` y `E5/2 = E1/2 · A2` son espinoriales, y los
caracteres de dimensión 1 de 2O son triviales en `−I`, así que `E` no es espín 1/2 por un carácter.
La afirmación «irreps of equal dimension differ by a one-dimensional character» es falsa en
dimensión 2 de 2O. En 2T sí es cierta (las tres irreps de dimensión 2 son `E`, `E'`, `E''` =
espín 1/2 por los tres caracteres, `:255–257`), y en dimensiones 3 y 4 de 2O también lo es
(`T2 = T1 · A2`; `G3/2` es única). **No afecta a T3, O3 ni O4.** Afecta a la frase de «Scope and
limits» del informe y a la de Step 0.2 sobre la cobertura: la clase `O`, `s = 2`, `R = E` lineal
no está cubierta por el control `O2s`. No es una clase declarada en la carta (la Sec. 1 declara
T3, O3 y O4); los casos `s = 2` eran controles.

**R2 (mensaje `NOTE` del certificado, `:259–261`).** **Se acepta.** El mensaje impreso repite la
afirmación falsa de R1. Es texto, no una comprobación: no cambia ninguno de los 31 `require`.
Corregirlo cambia los bytes de un verificador ya revisado; hay que decidir si se corrige ahora
(con nueva revisión de ese fichero) o se deja constancia en el informe y en `scripts/README.md`.

**R3 (el control positivo no ejercita el conmutante).** **Se acepta como laguna de
justificación.** El control Q8/D2 se llama con `commutant=False` (`:326`). Además, en `D2` el
estabilizador de un vértice es trivial (dos órbitas de tamaño 4 con un grupo de rotaciones de
orden 4), así que con `commutant=True` tampoco habría ecuaciones de conmutante. Ningún control
actual ejercita la rama `commutant=True` con estabilizador no trivial. La restricción
`[D(u), X] = 0` es necesaria (punto 1 del revisor, aceptado); un error solo podría restringir de
más si `linsolve` perdiera soluciones, y eso no lo descarta ningún control.

**R4 (comparaciones estructurales `==`).** **Se acepta en parte.** Revisé las comparaciones que
cita:
- `:199` y `:208` comparan matrices de rotación con vértices enteros: exactas.
- `:217` (`exprs == [1]`) compara la base de Gröbner reducida; una base que no sea literalmente
  `[1]` da `False` y el `require` falla. No puede dar un falso `EMPTY_CLASS`.
- `:228` (homomorfismo de rotaciones) y `:297–306` (intertwiners nulos) piden igualdad o cero
  estructural. Un cero no simplificado haría fallar el `require` (falla cerrado); un valor no
  nulo no puede pasar por `== 0`.

Ninguna de estas comparaciones puede producir un falso positivo en las conclusiones. Aun así, la
regla del repo (`CLAUDE.md`, «Hard rules») pide `certificate_utils.assert_sym_equal` para las
identidades simbólicas. Es una cuestión de conformidad, no de corrección.

**R5 (no verificado por ejecución).** Es una limitación del revisor, no una reparación. El autor
ejecutó el certificado el 2026-10-28 (31/31,
`reports/2026-10-28--irreducible-isotropy-step01-run_all.tsv`); esa ejecución es del autor.

## Conclusión del autor

- Ninguna objeción afecta al vacío de T3, O3 u O4. No hace falta rehacer esos cálculos.
- Hay una sobreafirmación real (R1/R2) en el alcance de los controles `s = 2` bajo `O`, y una
  laguna de control (R3).
- Estado: `ACCEPT_WITH_REPAIRS`, con R1–R3 sin aplicar. El resultado **sigue siendo
  PRELIMINARY**: la revisión pide reparaciones que no se han hecho. Este fichero no promociona
  nada ni cambia `state/CURRENT_STATE.md`.

Decisiones para el usuario:

1. Aplicar R1 (texto del informe) y R3 (nota en el informe; un control nuevo solo si se
   autoriza).
2. Decidir sobre R2 y R4, que cambian los bytes de un verificador revisado.
3. Decidir si se trata la clase `O`, `s = 2`, `R = E` lineal. Hoy no está en la carta.
4. Decidir si basta con que el autor relea el texto reparado o hace falta otra revisión.
