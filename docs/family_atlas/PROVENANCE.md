# Procedencia y comprobaciones de la primera edición

Fecha: 2026-09-30. Checkout inspeccionado:
`research/gravitational-normalization-gate` @
`16850476a6320c55aaf6d25471d00454cdc15b41`.

Sincronización posterior: el primer commit del atlas fue publicado como
`f21af94`. Después se incorporó la rama remota hasta `3976026`, que contenía
los contratos, scripts e informes de F2-F5. Esta página conserva el origen de
la primera edición y añade abajo la trazabilidad vigente.

## Alcance

Edición documental del núcleo F1–F5 solicitado, con reservas F6–F8.
Los nombres y resultados alegados de F2–F5 proceden del mensaje del usuario;
ese mensaje permite registrar candidatos, pero no sustituye contratos,
código o fuentes primarias. Se consultaron instrucciones del proyecto,
estado canónico, índice bibliográfico, contratos, scripts e informes locales.

La búsqueda por nombres y literales (`elastic`, `embedding`, `paired`,
`KINEMATIC_COMMON_EMBEDDING`, `UNITARY_ELASTIC_RESPONSE`,
`HERMITIAN_ELASTIC`, `STRUCTURALLY_BLOCKED_IN_STANDARD`) no localizó
expedientes F2–F5 en el checkout. Se inspeccionaron las referencias locales
de Git; no se descargaron ni sincronizaron otras ramas. No es una afirmación
de inexistencia fuera del material inspeccionado.

## F1: código permanente reejecutado

Desde la raíz del repositorio, los tres comandos terminaron con código 0:

```bash
python3 -B scripts/verify_w12_four_species_metric_universality.py
python3 -B debates/2026-09-30--w12-blind-review/verify_w12_independent.py
python3 -B debates/2026-09-30--w12-blind-review/verify_reviewer_claims.py
```

Los dos primeros reproducen `rank(Φ)=6`, `dim(U)=3`, rango métrico `3/6`
y núcleo común nulo. El tercero confirma la inversión de signo en −I,
el rango 6 por nodo +I y el determinante gauge registrado en F1.
Es una reejecución local de código existente; no es una nueva revisión
independiente ni una reparación de los scripts.

La revisión externa histórica y sus límites se toman del
[expediente W12](../../debates/2026-09-30--w12-blind-review/README.md)
en `4b0797d`. Su herramienta declarada fue `revision-ciega`,
`~/herramientas` @ `b817ac0`; no se ha invocado esa herramienta en esta edición.
La decisión de cierre consta en `687ffc3` y en la cabecera actual del estado.

## Lectura primaria acotada

Se leyó la página 1 de cada PDF mediante `pdftotext -f 1 -l 1 -layout`:

| PDF local | Atribución que sustenta |
|---|---|
| `biblioteca/1609.00305v2.pdf` | Arrighi–Facchini: paired QWs, grouping/encoding, operator splitting y objetivo Dirac curvo (3+1)D |
| `biblioteca/arXiv-1505.07023.pdf` | Arrighi–Facchini–Forets: antecedente (1+1)D |
| `biblioteca/arXiv-1609.00722.pdf` | Arnault–Debbasch: DTQWs curvos en (1+2)D |
| `biblioteca/arXiv-0907.1203.pdf` | Gu–Wen: diferencia entre modelo L cúbico y modelo N lineal sin control fiable |

Estas lecturas acreditan el contenido indicado de esas páginas, no una
auditoría completa de los artículos ni el supuesto bloqueo del puente F5.
Los PDFs viven en la biblioteca local ignorada por Git. Sus identificadores
arXiv y páginas permiten localizar las fuentes; no se copian al atlas.

## Mantenimiento

Comprobación editorial: ocho archivos Markdown, 26 enlaces locales resueltos,
diez secciones en cada ficha y sin espacios finales. Los diagramas se
entregan como fuente Mermaid; no se ha comprobado su renderizado en un visor.

## Sincronización F2-F5

Tras `git fetch` y rebase sobre `origin/research/gravitational-normalization-gate`,
se recuperaron y leyeron los expedientes remotos:

| Familia | Contrato / informe / script | Estado incorporado |
|---|---|---|
| F2 | `theory/ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE.md`; `reports/2026-09-30--elastic-graph-species-universality.md`; `scripts/verify_elastic_graph_species_universality.py` | `KINEMATIC_COMMON_EMBEDDING_UNIVERSAL / ELASTIC_HOPPING_RESPONSE_OPEN` |
| F3 | `theory/ELASTIC_HOPPING_UNITARY_RESPONSE_GATE.md`; `reports/2026-09-30--elastic-hopping-unitary-response.md`; `scripts/verify_elastic_hopping_orientation_obstruction.py` | `UNITARY_ELASTIC_RESPONSE_INCONSISTENT` |
| F4 | `theory/ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE.md`; `reports/2026-09-30--elastic-hopping-hermitian-response.md`; `scripts/verify_elastic_hopping_hermitian_response.py` | `HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY` |
| F5 | `reports/2026-09-30--arrighi-facchini-cjww-directed-reading.md`; new scoped audit below | `STRUCTURALLY_BLOCKED_IN_STANDARD_OPERATOR_SPLIT` kept only with restricted quantifiers |

The following existing commands were re-run locally and ended with code 0:

```bash
python3 -B scripts/verify_elastic_graph_species_universality.py
python3 -B scripts/verify_elastic_hopping_orientation_obstruction.py
python3 -B scripts/verify_elastic_hopping_hermitian_response.py
```

These runs are local author-side reproductions. They are not independent
external reviews.

## New F5 restricted certificate

The new permanent script
`scripts/verify_cjww_coordinate_factorization.py` verifies the restricted
claim in
[`reports/2026-09-30--cjww-coordinate-factorization-audit.md`](../../reports/2026-09-30--cjww-coordinate-factorization-audit.md):

```bash
python3 -B scripts/verify_cjww_coordinate_factorization.py
```

The run ended with code 0 and verdict
`SINGLE_COORDINATE_FACTORIZATION_EXCLUDED`. Its scope is one CJWW tick, the
original two-component cell, one factor per original coordinate, and constant
on-site conjugation allowed. It does not exclude grouped, ancilla, blocked or
repeated-axis paired-QW constructions.

## New F6-F7 reading

F6 records `biblioteca/arXiv-1609.00722.pdf` as a bibliographic comparator:
the read sections support a published (1+2)D curved DTQW, not a direct exact
(3+1)D CJWW bridge.

F7 records a primary-source preflight of `biblioteca/arXiv-1607.06700v2.pdf`.
The read definitions and theorem use finite labelled graphs and
vertex-preserving causal unitaries; they do not by themselves specify an
exact CJWW rule on infinite Z3. The terminal state recorded for the next
family selection is
`BRIDGE_QUANTIFIERS_OPEN / EXPLICIT_CJWW_RULE_NOT_SPECIFIED`.

The next F7 specification gate is frozen in
`theory/F7_QCGD_CJWW_RULE_SPECIFICATION_GATE.md` and executed in
`reports/2026-09-30--f7-qcgd-rule-specification.md`. It audits the existing
QCGD preflight, the 2026-09-29 class-selection result, the strong exact bridge
no-go and W1. It stops at `NO_RULE_SPECIFIED`: no complete `U_F7(g)` with
geometric observables is specified in the audited material.

The library catalog row for `arXiv-1607.06700v2.pdf` was added to
`scripts/biblioteca_catalog/curated.csv` and regenerated with the shared
engine:

```bash
python3 /home/ignac/herramientas/biblioteca_catalog/build_catalog.py --repo /home/ignac/qca-causal-cones
```

Shared-tool provenance for the catalog run:
`~/herramientas` @ `b817ac0`.

## New F8 reading

F8 records a primary-source preflight of `biblioteca/arXiv-0907.1203.pdf`
and the existing W8-W10 repair records. The retained terminal state is:

```text
VACUUM_CONSTRAINT_ARCHITECTURE_PRIOR_ART /
DIRECT_CJWW_SOURCE_BRIDGE_OPEN
```

The result separates the controlled L-type model with cubic dispersion from
the less controlled N-type linear-dispersion proposal, and it keeps W10 in
its repaired `OPEN_AFTER_AUDIT` scope. F8 is a constraint/gauge architecture
and novelty ceiling, not an executable CJWW metric family.

## Mantenimiento

El atlas conserva los resultados negativos y las incertidumbres. Al recuperar
un expediente, reemplazar «pendiente» solo después de comprobar sus
cuantificadores, evidencia y estado vigente; registrar el commit de origen.
Un cambio documental no modifica contratos ni autoriza cálculos sucesores.
