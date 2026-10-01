# F11 — Preflight de acción gauge en tiempo discreto

Fecha: 2026-10-01. Base inspeccionada: `ccc2e9f`, rama
`research/gravitational-normalization-gate`.

## 1. Pregunta y cierre de la lectura

¿Qué aporta Arnault–Cedzich al atlas, además de la extensión gauge de CA
clásicos de F10, y qué queda sin especificar para CJWW?

Una ronda de lectura primaria, sin construir reglas ni calcular métricas.
Antes de extraer resultados se fijaron las comprobaciones: acción ligada
a walk local, tipo de corriente, alcance del sourcing, dimensiones del
sector de materia y presencia de puente CJWW. El cierre es una ficha con
fuentes y límites, no un gate científico ni una búsqueda exhaustiva.

## 2. Fuente y comandos de lectura

Arnault y Cedzich, *A single-particle framework for unitary lattice gauge
theory in discrete time*, [arXiv:2208.14997v4](https://arxiv.org/abs/2208.14997v4).
La página oficial confirma título, autores y versión v4 de 8 septiembre
2022. Fuente de las afirmaciones técnicas: PDF local
`biblioteca/arXiv-2208.14997.pdf`, pp.1-11 y 19-20.

SHA256:

```text
8e134e16a5f765cb7446bb339c54917edf540f54863d46418f8cfd5b538879d9
```

Inspección mediante `pdftotext -layout`, con lecturas específicas de páginas
4-8, 9-11 y 19-20, y `sha256sum`. La extracción temporal de texto sirve solo
para inspección del PDF; no produce resultados científicos. No hay script
de cálculo nuevo, certificado ni revisión externa.

## 3. Hechos localizados

| Objeto | Localizador PDF | Alcance de la fuente |
|---|---|---|
| Materia | pp.2-3 | Una partícula spin-1/2 en (1+1)D; campos no cuantizados; C² suficiente |
| Walk local y ecuación de dos pasos | p.4, Ecs.18-23 | Saltos −1, 0, +1; segunda condición inicial fijada por el walk |
| Acción de materia | p.5, Ecs.34-36 | Versiones asimétrica y simétrica; EOM de dos pasos |
| Noether interno | pp.5-6, Ecs.43-49 | Corriente de carga U(1) con divergencia discreta nula on shell |
| Segunda derivación de la corriente | pp.19-20, apéndice E | EOM de uno y dos pasos llevan a la conservación de carga |
| Gauging | pp.7-8, Ecs.50-63 | Gauging del esquema de uno o dos pasos no conmutan en general; la fuente declara suficiente A₀ independiente de posición |
| Links y plaquetas | pp.8-9, Ecs.64-76 | Campo electromagnético y acción gauge en tiempo real |
| Sourcing | pp.9-10, Ecs.77-94 | Variación de acción total; corriente U(1) como fuente de ecuaciones clásicas gauge |
| Dimensiones | p.9, Sec.V.D | La acción de materia (3+1)D no está construida; las ecuaciones generales con fuente requieren esa extensión |
| Pendientes expresos | p.11 | Noether espaciotemporal, cuantización de campos y cuestión de doubling sin resolver en este trabajo |

Los resultados son atribuciones a la fuente leída, no una reejecución o
auditoría algebraica completa. La lectura del apéndice E es una segunda vía
dentro del mismo artículo para comprobar qué corriente se está usando;
no cuenta como revisión independiente.

## 4. Separaciones decisivas

**Carga frente a stress.** La simetría usada es interna U(1), y la corriente
se compara con la corriente de carga de Dirac (p.6). La conclusión deja
abierto Noether para simetrías externas/espaciotemporales (p.11). Por tanto
la fuente no proporciona el stress local CJWW pendiente en W11.

**Gauge frente a geometría.** Los links comparan fases U(1), y sus
plaquetas codifican campo electromagnético en red fija (pp.8-9). La ficha
no localiza ni calcula un control de métrica o tetrad común.

**Sourcing clásico frente a QCA conjunta.** El artículo deriva ecuaciones
de campo gauge desde una acción que incluye materia (pp.9-10), pero dice
que los campos no están cuantizados (p.2) y deja esa extensión para trabajo
futuro (p.11). No se deduce una unitaria conjunta materia/enlaces.

**Acción gauge general frente a materia 3D.** La p.9 advierte que la acción
de materia en (3+1)D no está construida. No trasladar el resultado gauge
general al tick CJWW, ni siquiera antes de un test de especies.

## 5. Resultado documental

```text
F11_ARNAULT_CEDZICH_LATTICE_GAUGE_PREFLIGHT =
DISCRETE_TIME_U1_ACTION_CURRENT_PRIOR_ART /
DIRECT_CJWW_GEOMETRY_BRIDGE_ABSENT

FOUR_SPECIES_TEST = NOT_EXECUTED
EVIDENCE = BOUNDED_PRIMARY_SOURCE_READING
INDEPENDENT_REVIEW = NOT_PERFORMED
```

El término ABSENT se restringe al puente directo en esta fuente. No excluye
una construcción futura ni establece inexistencia en la literatura.

## 6. Consecuencia para el atlas

F11 aporta una arquitectura variacional para amplitudes de walk y corriente
gauge, distinta de F10 y de las restricciones tensoriales F8/F9. Su uso
admisible es técnico/documental. Para una familia CJWW ejecutable harían
falta un contrato propio, regla 3D exacta, límite plano CJWW y observable
geométrico separados de la carga. Esta lectura no abre ese contrato ni
modifica resultados anteriores.
