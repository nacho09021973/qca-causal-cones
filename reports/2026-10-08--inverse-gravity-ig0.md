# IG0: requisitos y primeras obstrucciones del diseño inverso

Fecha: 2026-10-08. Base local `0a4606c61a3f75e5516a245f3837ed009b0a56b4`.
Rama: `research/inverse-gravity-design`.
Contrato: [INVERSE_GRAVITY_DESIGN_CHARTER](../theory/INVERSE_GRAVITY_DESIGN_CHARTER.md).
Evidencia: lectura primaria acotada y análisis conceptual del autor-agente;
sin cálculo de un candidato, sin revisión independiente.

## 1. Lectura primaria y procedencia

Índice `biblioteca/INDICE.md` consultado antes de investigar. PDFs leídos
directamente mediante `pdftotext -f N -l M -layout <PDF> -`, sin extraer
resultados científicos con código temporal. Las notas anteriores y fichas
del atlas solo sirvieron para localizar problemas y fuentes.

| Fuente | Páginas comprobadas | Resultado de alcance |
|---|---|---|
| Gu–Wen, `biblioteca/arXiv-0907.1203.pdf`, v3 | p.1 y pp.9–12 | La fuente distingue L: helicidades ±2 con dispersión cúbica; N: expectativa lineal con control cuántico menor. Ecs.13–30 muestran que vector constraint y eliminación escalar no bastan para garantizar z=1. Ecs.32–37 exponen la ruta continua lineal y su estructura de constraints |
| Xu–Hořava, `biblioteca/arXiv-1003.0009.pdf`, v1 | pp.1–2 | Red rígida, variables colectivas y fases Lifshitz z=2/3; cambiar conectividad no es requisito universal de geometría efectiva. Esta fuente no acredita Einstein z=1 |
| Deser, `biblioteca/arXiv-gr-qc_0411023.pdf`, v3 | pp.1–2 | En su marco continuo de spin-2 sin masa, consistencia de fuente y autointeracción conduce al cierre Einstein. No construye una QCA ni demuestra que una fase de red satisfaga las hipótesis |

Metadatos/abstracts contrastados también en fuentes originales:
[Gu–Wen](https://arxiv.org/abs/0907.1203v3),
[Xu–Hořava](https://arxiv.org/abs/1003.0009v1),
[Deser](https://arxiv.org/abs/gr-qc/0411023v3).
El índice no prueba sus etiquetas y esta lectura no es búsqueda exhaustiva.

Se leyó además Farrelly, `biblioteca/review of Quantum Cellular Automata.pdf`,
pp.33–34, como orientación secundaria sobre Hamiltonianos, simulación y
ausencia de orden energético canónico en una unitaria. No se usa esa revisión
para certificar un candidato. La identidad exacta de alcance de una regla
futura deberá probarse directamente a partir de sus puertas.

## 2. Tres opciones conceptuales

| Opción | Ventaja buscada — hipótesis de diseño | Primer problema sin resolver | Decisión IG0 |
|---|---|---|---|
| Variables tensoriales locales + sector colectivo restringido | Permite preguntar por dos modos físicos y propagación antes de imponer una métrica de materia | Realizar constraints y sector IR en celda finita con tick exacto; conseguir z=1 | Prioridad de especificación, viabilidad OPEN |
| Geometría como deformación compartida del embedding | Da una referencia cinemática universal F2 | Falta respuesta autónoma del estado y hopping que realice esa geometría | Comparador; insuficiente como arquitectura completa |
| Grafo dinámico con materia | Permite geometría combinatoria variable | Falta regla completa y mecanismo de constraints/conos comunes; variar grafo no los garantiza | Diferida; fuera de la envolvente fija inicial |

La prioridad tensorial es una decisión de trabajo, no un resultado de
optimización ni una nueva familia certificada. No se importan los controles
W6 y no se fuerza recuperación CJWW. Gu–Wen constituye antecedente central,
por lo que «qubits que producen modos tensoriales» no es claim de novedad.

## 3. Objeciones antes de construir

**O1 — selección IR en tiempo discreto.** Una unitaria da fases módulo 2π;
por sí sola no identifica un vacío ni ordena una energía. La especificación
debe aportar un sector invariante o un régimen efectivo controlado, con
selección de rama y escalas. Un Hamiltoniano auxiliar puede guiar un diseño,
pero conservar su fase bajo el tick sigue siendo una obligación abierta.

**O2 — constraints no equivalen a dispersión lineal.** Gu–Wen pp.10–12 permite
comparar dos rutas con restricciones tensoriales y distinta dinámica. La
supresión de modos y el exponente de dispersión se deben comprobar por separado.
No rescatar z=2/3 cambiando el nombre del objetivo.

**O3 — localidad de densidad, dinámica y observables.** Gu–Wen p.12 llama
«nonlocal gauge invariant» a una ruta cuya densidad cambia por una derivada
total. No identificar automáticamente esa etiqueta con alcance infinito del
QCA. Se deberán comprobar alcance de las puertas, preservación del sector
físico y acción sobre observables por separado.

**O4 — celda finita y variables continuas.** Los tensores canónicos del
continuo no se convierten automáticamente en registros finitos. Un truncamiento
debe especificar álgebra y errores; no mantener indefinidamente rotores infinitos
como si ya cumplieran la envolvente microscópica del charter.

**O5 — velocidad común.** Un tensor y dos especies relativistas pueden tener
velocidades distintas. Es una posibilidad a excluir, no un cálculo realizado.
Debe existir un mecanismo común y declararse qué perturbaciones lo preservan;
poner tres coeficientes iguales no acredita protección.

**O6 — fuente y cierre.** La fuente de Deser es stress total, incluido el
campo gravitatorio. Una carga de enlace, un número de ocupación o una fuerza
entre defectos no certifica ese objeto. El bootstrap es condicional a las
hipótesis continuas verificadas; no es un teorema de emergencia para la red.

**O7 — simulación frente a emergencia.** Una futura construcción que codifique
un Hamiltoniano gravitatorio elegido podrá ser un simulador válido. Se registrará
como tal mientras no se derive la estabilidad y el origen colectivo de sus
variables/constraints. Escribir Einstein como entrada no cierra esta pregunta.

Todas las objeciones siguen abiertas para el candidato todavía no especificado.

## 4. Segunda vía de control: resultados insuficientes

La formulación inversa se comprueba contra casos que satisfacen parte del
objetivo: F2 da métrica común sin dinámica; el antecedente L de Gu–Wen da dos
helicidades sin z=1; el spin-2 libre no contiene el cierre con fuente total
descrito por Deser. Cada caso rompe una inferencia distinta. Por ello el
contrato separa geometría, modos, propagación, universalidad y cierre.
Esto verifica el alcance de las preguntas, no la existencia de una solución.

## 5. Decisión y siguiente pregunta concreta

`IG0 = ARCHITECTURE_UNDERSPECIFIED`.
`PRIORITY = LOCAL_TENSOR_COLLECTIVE_SECTOR`.
`IG1 = NOT_EXECUTED / NO_RULE_SPECIFIED`.
`EINSTEIN_EMERGENCE = OPEN`; `NOVELTY = OPEN`.

La siguiente pregunta es: **¿cómo definir un tick local exactamente unitario,
una celda finita y un sector tensorial controlado que admita dos modos físicos
con dispersión lineal, sin imponer una proyección TT no local?**

Antes del espectro se especificarán el mecanismo de restricciones y el sector
IR, o se registrará que faltan. El cono común con materia es el siguiente
filtro, no una propiedad ya asumida. No se calculó, simuló ni seleccionó una
regla microscópica en este IG0.
