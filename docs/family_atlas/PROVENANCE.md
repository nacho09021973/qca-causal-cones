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

## Lectura F12 — 2026-10-01

Fuente primaria ya presente en la biblioteca:
`biblioteca/Quantum Cellular Automaton Theory of Light.pdf`, Bisio–D’Ariano–Perinotti,
arXiv:1407.6928v1. SHA256:
`8f36b0936fd8ab3f396d8495f15bd66033657fd860f94179db2819d708672fa0`.
Leídas pp.1-7 mediante `pdftotext -layout`; ver
[informe F12](../../reports/2026-10-01--f12-bisio-dariano-perinotti-light-preflight.md)
para localizadores y límites.

Resultado documental:
`PUBLISHED_3D_WEYL_QCA_MAXWELL_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT`.
No se ejecutó un test de cuatro especies, no se implementó la regla y no se
invocó revisión independiente.

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

## New F9 reading

F9 records a primary-source preflight of `biblioteca/arXiv-1606.08857.pdf`
and `biblioteca/arXiv-1702.07613.pdf`. The retained terminal state is:

```text
RANK2_GAUSS_LAW_PRIOR_ART /
DIRECT_CJWW_QCA_BRIDGE_ABSENT
```

The result separates Pretko's rank-2 tensor-gauge/fracton dictionary from
Gu-Wen's qubit/spin construction. F9 supplies Gauss-law architecture and a
claim ceiling for tensor-gauge mode counting; it does not supply a CJWW walk,
local stress source, reciprocal backreaction or exact QCA update.

## New F10 reading

F10 records a primary-source preflight of `biblioteca/arXiv-2102.06912.pdf`
by Arrighi, Costes and Eon, *Universal gauge-invariant cellular automata*.
The PDF was downloaded from arXiv and has checksum:

```text
c44d21281318b1340aa4336c02306a18b2326128452ce6e7d751fc62db721b20
```

Read pages: pp.1-14. The retained terminal state is:

```text
GAUGE_EXTENSION_CA_ARCHITECTURE_PRIOR_ART /
DIRECT_CJWW_QCA_BRIDGE_ABSENT
```

The result records gauge extension, relative link gauge fields, universal
gauge-invariant CA and a reversible non-relative matter/gauge feedback example
as useful discrete architecture. It does not promote link gauge variables to
geometry and does not supply a CJWW/QCA metric family.

The library catalog row for `arXiv-2102.06912.pdf` was added to
`scripts/biblioteca_catalog/curated.csv` and the ignored local index was
regenerated with the shared engine:

```bash
python3 /home/ignac/herramientas/biblioteca_catalog/build_catalog.py --repo /home/ignac/qca-causal-cones
```

Shared-tool provenance for the catalog run:
`~/herramientas` @ `b817ac0`.

## Lectura F11 — 2026-10-01

Base inspeccionada: `ccc2e9f`. Fuente primaria ya presente en la biblioteca:
`biblioteca/arXiv-2208.14997.pdf` (Arnault–Cedzich, arXiv:2208.14997v4).
Leídas pp.1-11 y 19-20 mediante `pdftotext -layout`; ver
[informe F11](../../reports/2026-10-01--f11-arnault-cedzich-lattice-gauge-preflight.md)
para checksum, localizadores y alcance de la comprobación.

Resultado documental:
`DISCRETE_TIME_U1_ACTION_CURRENT_PRIOR_ART / DIRECT_CJWW_GEOMETRY_BRIDGE_ABSENT`.
La segunda derivación de conservación de carga está en el apéndice E de la
misma fuente; no es revisión independiente. No se implementó una regla,
no se ejecutó un test de especies y no se invocaron herramientas externas
de revisión ni el motor del catálogo.

## Mantenimiento

El atlas conserva los resultados negativos y las incertidumbres. Al recuperar
un expediente, reemplazar «pendiente» solo después de comprobar sus
cuantificadores, evidencia y estado vigente; registrar el commit de origen.
Un cambio documental no modifica contratos ni autoriza cálculos sucesores.

## Lectura F13 — 2026-10-01

F13 registra la lectura primaria acotada de `biblioteca/1312.2852v1.pdf`,
Farrelly–Short. Se comprobaron las pp.1-5: clase causal de una partícula con
`U_D = sum_q A_q S_q`, límite Weyl para espacio interno de dimensión 2 y
ejemplo de dimensión 3 con `H = J dot P` rotacional pero no Lorentziano.
La fuente no especifica una regla CJWW, controles métricos, cuatro especies ni
backreaction. El resultado documental queda
`PUBLISHED_CAUSAL_SINGLE_PARTICLE_WALK_PRIOR_ART /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT`; no se ejecutó cálculo ni revisión externa.

## Lecturas F16–F20 — 2026-10-01

Se cerró la ronda documental F16–F20 con cinco fuentes primarias locales:

| ID | Fuente | Resultado |
|---|---|---|
| F16 | Białynicki-Birula, `Dirac and Weyl Equations on a Lattice as Quantum Cellular Automata.pdf`, pp.1-5 | `PUBLISHED_CUBIC_QCA_WEYL_DIRAC_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT` |
| F17 | Bisio–D’Ariano–Perinotti, `Quantum Walks, Weyl equation and the Lorentz group.pdf`, pp.1-8 | `NONLINEAR_POINCARE_SYMMETRY_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT` |
| F18 | `arXiv-1702.07613.pdf`, pp.1-5, 8-12 | `FRACTON_TENSOR_GRAVITY_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT` |
| F19 | `arXiv-2108.06582.pdf`, pp.1-6, 9-22, 28-29 | `EFFECTIVE_GAUGE_EMERGENCE_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT` |
| F20 | `arXiv-1003.0009.pdf`, pp.1-3, 5-8 | `LATTICE_BOSE_LIQUID_LIFSHITZ_GRAVITY_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT` |

No se ejecutaron tests CJWW, cálculos nuevos ni revisiones externas. Las cinco
entradas son documentales y no abren gates.

## Relaciones F1–F20 — 2026-10-01

Se añadió la primera capa relacional del atlas en
[`docs/family_atlas/RELATIONS.md`](RELATIONS.md) y
[`docs/family_atlas/relations.csv`](relations.csv). La clasificación distingue
subclase, soporte compartido, comprobación independiente, alcance de una
obstrucción, complemento arquitectónico, contraste y puente bibliográfico.
Cada arista conserva su alcance y estado (`ESTABLISHED_FROM_ATLAS`,
`RESTRICTED`, `ABSENT` u `OPEN`); no se ejecutaron cálculos ni se promovieron
gates.

## Uso del atlas en el proyecto — 2026-10-01

La traducción operativa se conserva en
[`PROJECT_NAVIGATION.md`](PROJECT_NAVIGATION.md). Organiza las familias por
frentes del proyecto y fija el límite: el atlas selecciona antecedentes,
comparadores y posibles contratos, pero no transfiere gates ni autoriza una
regla CJWW nueva.

## Lectura F15 — 2026-10-01

F15 registra la lectura primaria acotada de `biblioteca/Derivation of the
Dirac Equation from Principles of Information Processing.pdf`,
D’Ariano–Perinotti. Se comprobaron las pp.1-7: principios de la QCA, grafo de
Cayley, emergencia de espacio vía embedding cuasi-isométrica, cuatro
soluciones Weyl BCC y acoplamiento local Weyl–Dirac. La fuente no especifica
controles métricos CJWW, cuatro especies ni backreaction. Resultado:
`INFORMATION_AXIOM_DERIVED_WEYL_DIRAC_QCA_PRIOR_ART /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT`; no se ejecutó cálculo ni revisión externa.

## Lectura F14 — 2026-10-01

F14 registra la lectura primaria acotada de `biblioteca/1708.00826v2.pdf`,
D’Ariano–Erba–Perinotti. Se comprobaron las pp.1-8 y Fig.1: definición de
walk isotrópico en grafo de Cayley, clasificación para `Z^d`, `d=1,2,3`, y
Proposición 5, que deja en d=3 la red BCC y los dos walks Weyl. La fuente no
especifica controles métricos CJWW, cuatro especies ni dinámica de red.
Resultado: `PUBLISHED_ISOTROPIC_CAYLEY_QW_CLASSIFICATION /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT`; no se ejecutó cálculo ni revisión externa.
