<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 5ef0adaa9752398082d550ec2c74860aa43378562046a703efbce7ff27d1d092
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-29T09:20:58Z  fin: 2026-10-29T09:31:49Z
documento: /home/ignac/qca-causal-cones/theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md ; último commit observado: 88b07ed ; sha256 de la copia enviada bb12375faff7b16fcd5e40c85995dc9fe8f374f6d26b51c60819fa94bba176a6
documento: /home/ignac/qca-causal-cones/reports/2026-10-28--irreducible-isotropy-step01.md ; último commit observado: 88b07ed (con cambios sin commit) ; sha256 de la copia enviada 01db8e845670f170873341fa541f131718b0f810b66d8c7bce0a89d17618c9a1
documento: /home/ignac/qca-causal-cones/scripts/verify_irreducible_isotropy_step01.py ; último commit observado: 88b07ed (con cambios sin commit) ; sha256 de la copia enviada d4b3d242bdd259aa45aa532b6b212bfe75eb0009097f85883805507857f1bfe4
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
documento: /home/ignac/qca-causal-cones/debates/2026-10-28--irreducible-isotropy-step01-review-deepseek/reintento-01-red/informe_deepseek.md ; último commit observado: sin versionar ; sha256 de la copia enviada d9499ba9a903c2fa97d1613cc07116307948c5e2427772717a4828637aee0949
entrada_grok.txt sha256 abb7933155795d17fccafd62bdcd10f9d98e9942b5fd8eaf283e6ebf5889c86d
respuesta sha256 24e501a4a27ef920c7b2f2610508310dd3ea9ab5908e89ba2c3751f1f37cfc46
-->

**Veredicto global: ACCEPT_WITH_REPAIRS.** Las reparaciones de DeepSeek sobre la representación lineal `E` y el mensaje falso quedan bien hechas, y no veo un error estático que invalide el vacío de T3, O3 y O4. Siguen en pie dos sobreafirmaciones de método y un límite mal acotado del control nuevo del conmutante. No he ejecutado nada.

| Punto | Veredicto |
|---|---|
| (1) Alcance de `E` y cuantificadores T3/O3/O4 | **ACCEPT** |
| (2) Mensaje y comparaciones simbólicas | **ACCEPT_WITH_REPAIRS** |
| (3) Dimensiones 2 y 6 del conmutante | **ACCEPT_WITH_REPAIRS** |
| (4) Código y sobreafirmaciones restantes | **ACCEPT_WITH_REPAIRS** |
| (5) Revisión sin ejecución frente a 33/33 y 47/47 | No es un pase matemático; los dos conteos quedan **sin verificar por ejecución** |

## (1) `E` y cuantificadores — ACCEPT

La frase universal que DeepSeek rechazó ya no está. El informe, el docstring y la nota impresa dicen lo mismo: espín 1 y espín 3/2 cubren T3, O3 y O4 salvo caracteres unidimensionales, y el control de espín 1/2 bajo `O` no cubre la `E` lineal de `2O`.

Eso es correcto. Los caracteres unidimensionales de `2O` valen `+1` sobre `-I`, así que no cambian el carácter central. `E` (lineal, carácter central `+2`) no es un torcimiento de `E_{1/2}` ni de `E_{5/2}` (carácter central `-2`). En cambio, `T2 = T1 ⊗ A2` y `E_{5/2} = E_{1/2} ⊗ A2` tienen la misma acción por conjugación, porque `|χ(g)| = 1` implica `(χ R) X (χ R)^† = R X R^†`. Un solo cálculo de Gröbner para espín 1 cubre las dos representaciones de O3; no hace falta un segundo sistema. O4 es la única irreducible de dimensión 4, y el torcimiento por `A2` tampoco cambia la conjugación. T3 es la única irreducible tridimensional de `T`, realizada por el espín 1, que factoriza por `T` al ser el peso par.

El informe no deduce de ahí el vacío de la clase `(O, s = 2, R = E)`. El estatuto de la hipótesis —vacua en T3, O3 y O4, ni refutada ni confirmada— se mantiene.

## (2) Mensaje y comparaciones — ACCEPT_WITH_REPAIRS

La nota nueva no repite el error. Homomorfismo de rotaciones, intertwiners, independencia del representante de la clase lateral y el test de ideal unidad pasan por `sym_zero` / `assert_sym_equal`, no por `==` estructural ni por `exprs == [1]`.

Quedan tres canales de falso pase, ninguno demostrado sobre estas expresiones:

- `key()` canoniza con `sp.nsimplify`, que es numérico. El docstring del certificado dice «zero tolerance». Eso es falso mientras la identidad de los elementos del grupo dependa de `nsimplify`. Una colisión de claves achicaría el grupo; el test `|2O| = 48` lo cierra solo si el colapso no cae exactamente en 48.
- `sym_zero` hace `simplify(e) == 0`. Si `simplify` devuelve 0 de más, se puede aceptar un homomorfismo falso, un transporte mal definido o un intertwiner nulo que no lo es. Esa dirección es fail-open para el vacío. El `==` estructural antiguo fallaba al revés.
- `diagonal_sign` sigue usando `img == e`. Si la entrada no está en `{-1,0,1}` exactos, el `next` aborta: fail-closed, no un vacío espurio.

El certificado solo comprueba que, sin la normalización, el término constante es cero. Eso basta para que el ideal relajado sea propio y el `(1)` no salga de esas ecuaciones solas. No comprueba homogeneidad de un solo grado. Por la construcción las ecuaciones relajadas son cuadráticas, así que la palabra «homogeneous» del mensaje es más fuerte que el test, pero la inferencia que se usa es válida.

## (3) Dimensiones 2 y 6 — ACCEPT_WITH_REPAIRS

La cuenta del comentario es correcta, y no depende del certificado. El levantamiento de la rotación de ángulo `2π/3` es `exp(-i (2π/3) n·σ / 2)`. En espín `j` sus autovalores son `e^{-i m 2π/3}` con `m = -j,…,j`. El preimagen binaria del estabilizador es cíclico de orden 6, generado por ese levantamiento (`ρ^3 = -I`), así que el conmutante del grupo es el del generador: dimensión compleja `∑ m_i^2`.

- Espín 1/2: autovalores `e^{±iπ/3}`, multiplicidades `(1,1)`, dimensión `1+1 = 2`.
- Espín 3/2: `e^{±iπ/3}` simples y `-1` con multiplicidad 2, dimensión `1+1+4 = 6`. El plano de autovalor `-1` no se parte: el generador actúa ahí por escalar.
- Espín 1, no incluido en el control nuevo: `e^{±2πi/3}` y `1`, tres autovalores simples, dimensión compleja **3**.

El test `len(params) == 2 * expected` solo iguala el número de reales que devuelve `covariant_class` con el doble de ese entero escrito a mano. Como el conmutante es un subespacio lineal, esa igualdad implica parametrización completa **solo si** las ecuaciones pasadas a `linsolve` son exactamente `[D(u), X] = 0` para ese estabilizador y `linsolve` devuelve todo el espacio. No construye una base independiente, no mete una matriz testigo dentro ni fuera, y llama a la misma función que luego alimenta el Gröbner. Descarta el colapso a `{0}` y el olvido total del conmutante (dimensiones `0` o `s^2`), no un subespacio equivocado de la dimensión justa producido por un estabilizador mal filtrado.

Además el bucle solo corre `2O` con `n = 1` y `n = 3`. No toca el espín 1. T3 y O3, las dos clases tridimensionales del resultado principal, siguen sin control de dimensión. La frase «dimension controls for that branch» no dice esto: «that branch» puede leerse como el control Q8 o como todas las clases con estabilizador no trivial.

## (4) Código y sobreafirmaciones — ACCEPT_WITH_REPAIRS

No veo un fallo estático que fabrique por sí solo el ideal `(1)` en T3, O3 u O4. Covarianza, un coeficiente por órbita, transporte `T_v = D(u) A D(u)^†`, cancelación de la fase al conjugar, las 27 diferencias `ℓ = h' - h` y el criterio de ideal unidad sobre `C` están bien planteados. El conteo estático de `require` es 33 (los 31 antiguos más los dos de dimensión). `S4_FAMILY_OUTSIDE_O4` para todo `a`, si O4 está vacía, es lógico: una clase vacía no contiene a ningún `A_a`. No prueba rigidez. El informe lo dice.

Sobreafirmaciones que sí quedan:

- El informe dice que el Gröbner es «rational arithmetic». No lo es para todas las clases. El espín 1 mete `√2` por `sqrt(binomial(2,1))`, el espín 3/2 mete `√3`, y el giro de orden 4, `exp(±iπ/4)`, mete `√2` también en el control de espín 1/2 bajo `O`. El anillo es una extensión algebraica de `Q`. El docstring, que dice «rational/algebraic», es más fiel que el informe.
- «Zero tolerance», en el mismo docstring, no cuadra con `nsimplify` en `key()`.
- «That class contains the Pavia symbols» no es lo que calcula el control positivo. Ese control, con `commutant=False`, solo muestra que el ideal Q8/espín 1/2 no es `(1)`. Como el estabilizador de `D2` en el vértice es trivial, `commutant=False` es aquí la clase completa, no una relajación; pero sigue sin ejercitar un conmutante no trivial, y el certificado no sustituye el símbolo de Pavia como punto de esa variedad. Para Control A, intertwiner nulo sí prueba que no hay covarianza bajo el giro de orden 3 o 4. Intertwiner no nulo no prueba por sí solo una representación unitaria de `D2`; la parte positiva queda por debajo de la frase «are `D2`-isotropic».

`cert_Aa_s4_counterexample.py` y `verify_weyl_dirac_gate.py` no están en este paquete. Controles A y B y la anulación del generador sobre `A_a` y Pavia dependen de ellos.

## (5) 33/33 y 47/47

Esos números son afirmaciones de ejecución. Esta revisión no los reproduce. Si el fuente adjunto llegara al final, el contador imprimiría `33/33`, porque hay 33 llamadas a `require`; eso no dice que hayan pasado. `47/47` no se deduce del fuente adjunto: el barrido y el TSV citados no están aquí. El propio informe separa bien las dos cosas: esas corridas, si ocurrieron, ejecutan los bytes reparados y no son una revisión matemática. El hash `d4b3d242…f1bfe4`, los 683 s, Python 3.12.3 y SymPy 1.14.0 tampoco los puedo atar a este texto.

## Reparaciones obligatorias

1. **Aritmética racional.** En `2026-10-28--irreducible-isotropy-step01.md`, sección «Step 1: method and controls», quitar «rational arithmetic». Sustituir por aritmética exacta en una extensión algebraica de `Q` que incluye `√2` y `√3`. No dejar «exact» como si el dominio del Gröbner ya estuviera inspeccionado.
2. **«Zero tolerance».** En el docstring de `verify_irreducible_isotropy_step01.py`, y en `key()`. O se elimina `sp.nsimplify` y la clave de grupo se canoniza de forma exacta, o se declara que esa identidad pasa por `nsimplify`.
3. **Alcance de las dimensiones 2 y 6.** En el informe, el párrafo que empieza por «The repaired verifier adds dimension controls». Decir que solo cubren `O`, espín 1/2 (dimensión compleja 2) y espín 3/2 (dimensión 6, clase O4); que no cubren el espín 1 de T3/O3, cuya dimensión compleja es 3; y que no exhiben una base del conmutante, así que no cierran la completitud de la parametrización usada en el Gröbner.

## Sin ejecutar no puedo verificar

- Que algún `require` pase, ni el `33/33`, ni el `47/47`, ni el hash, ni el tiempo, ni el intérprete.
- Que el Gröbner sea realmente `[1]` en T3, O3, O4, T2s y O2s, y que no lo sea en el control Q8.
- Que SymPy 1.14 trate el dominio `Q(√2, √3, i)` sin caer en flotantes ni en indeterminadas.
- Que `simplify` no anule residuos no nulos, ni que `nsimplify` no fusione elementos distintos de `2O` o `2T`.
- El contenido de `C4.coefficients` y `WD.published_symbol`, ni los TSV del barrido.
- Una prueba analítica alternativa del vacío. Las condiciones de traza en `k = 0` no bastan, igual que en la revisión anterior; las identidades `ℓ ≠ 0` siguen sin una segunda derivación en este paquete.
