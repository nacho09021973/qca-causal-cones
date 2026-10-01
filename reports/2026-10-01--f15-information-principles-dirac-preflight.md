# F15 — Preflight de Dirac desde principios informacionales

Fecha: 2026-10-01. Fuente primaria local:
`biblioteca/Derivation of the Dirac Equation from Principles of Information
Processing.pdf`, D’Ariano y Perinotti, arXiv:1306.1934v2. SHA256:
`940dde862ab1ba74a4ce1b3f85f8056f7e0f00abd93b403fdbf6543849a9c72f`.

## Lectura primaria

Se leyeron las pp.1-7 mediante `pdftotext -layout`. Las pp.1-3 fijan una QCA
fermiónica lineal con un conjunto numerable de sistemas, localidad, unitaridad,
homogeneidad e isotropía; las relaciones de transición definen un grafo de
Cayley y el operador `A = sum_h T_h tensor A_h` (pp.1-3, Ecs.1-6).

La p.2 afirma que el grafo y la noción de espacio emergen de los generadores,
relatores y una embedding cuasi-isométrica, en vez de imponerse inicialmente
una métrica euclídea (Ecs.7-9). Las pp.3-5 restringen el análisis a grupos
abelianos y resuelven la QCA de complejidad mínima en `Z^3`: la única red que
admite soluciones no triviales bajo las condiciones declaradas es BCC, y hay
cuatro soluciones agrupadas en los pares `A^±` y `B^±` (pp.4-5, Ecs.17-22).

Las pp.5-7 identifican estas soluciones como autómatas Weyl, obtienen la
dispersión y su límite relativista a bajo momento; las pp.7-8 describen el
acoplamiento local de dos autómatas Weyl que produce los autómatas Dirac. El
resumen y la p.1 dejan explícito que la covariancia de Lorentz se distorsiona
en el régimen ultrarrelativista.

## Comprobaciones de alcance

F15 es una derivación basada en principios informacionales de una QCA Weyl/Dirac;
no es la clasificación de isotropía de F14 ni el QCA Maxwell compuesto de F12.
La fuente trabaja con la QCA lineal y sus sectores de una partícula, con BCC
en el caso 3D y baja cantidad de onda para el límite de Dirac.

La fuente no define controles métricos CJWW, cuatro especies comunes, una
deformación variable del soporte, stress/source local o backreaction. El
lenguaje de espacio emergente y de gravedad es motivación del artículo, no un
puente ejecutable al contrato W6.

## Resultado documental

```text
F15_INFORMATION_PRINCIPLES_DIRAC_PREFLIGHT =
INFORMATION_AXIOM_DERIVED_WEYL_DIRAC_QCA_PRIOR_ART /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT

D3_RULE = MINIMAL_BCC_WEYL_QCA
DIRAC_COUPLING = TWO_WEYL_AUTOMATA
FOUR_SPECIES_TEST = NOT_EXECUTED
EVIDENCE = BOUNDED_PRIMARY_SOURCE_READING
INDEPENDENT_REVIEW = NOT_PERFORMED
```

La entrada es distinta porque registra la derivación axiomática desde
principios de procesamiento de información y el acoplamiento Weyl–Dirac,
no solo la clasificación geométrica de F14.
