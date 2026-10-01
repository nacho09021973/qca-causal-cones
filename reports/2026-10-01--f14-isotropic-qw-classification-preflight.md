# F14 — Preflight de clasificación de walks isotrópicos

Fecha: 2026-10-01. Fuente primaria local:
`biblioteca/1708.00826v2.pdf`, *Isotropic quantum walks on lattices and the
Weyl equation*, D’Ariano, Erba y Perinotti, arXiv:1708.00826v2. SHA256:
`dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81`.

## Lectura primaria

Se leyeron las pp.1-8 y la Fig.1 mediante `pdftotext -layout`. Las pp.1-3
definen el walk en un grafo de Cayley, el operador de transición
`A = sum_h T_h tensor A_h`, la isotropía como covariancia bajo un grupo de
automorfismos del grafo y la representación proyectiva del coin (pp.1-3,
Ecs.1-9). La p.4 restringe la clasificación a `G ~= Z^d`, `d=1,2,3`, y
dimensión de coin `s=2`; la isotropía se usa para restringir las presentaciones
de la red.

La Fig.1 (p.6) identifica las celdas primitivas: red entera en d=1, red
cuadrada simple en d=2 y red BCC en d=3. La Proposición 5 (pp.7-8) afirma
que las gráficas admisibles son únicas por dimensión y que en d=3 los únicos
walks isotrópicos son los dos walks Weyl, con las matrices de transición de
las Ecs.24-25 (pp.7-8). La conclusión de la p.8 presenta esto como una
clasificación completa para `d=1,2,3`, `s=2`.

## Comprobaciones de alcance

F14 es una clasificación de walks isotrópicos en grafos de Cayley abelianos;
no es la construcción Maxwell compuesta de F12 ni la clase general de
partículas causales de F13. El resultado depende de `s=2`, `G ~= Z^d`,
isotropía definida por automorfismos del grafo y las hipótesis de unitaridad
del artículo. No cubre dimensiones internas mayores, `Z^3` con cuatro
especies CJWW, controles geométricos variables ni dinámica de la red.

La clasificación selecciona un soporte/representación Weyl en el caso 3D,
pero no convierte la isotropía en una métrica dinámica, una respuesta a
strain o una escala física absoluta.

## Resultado documental

```text
F14_ISOTROPIC_QW_CLASSIFICATION_PREFLIGHT =
PUBLISHED_ISOTROPIC_CAYLEY_QW_CLASSIFICATION /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT

D3_RESULT = UNIQUE_BCC_GRAPH / TWO_WEYL_WALKS
FOUR_SPECIES_TEST = NOT_EXECUTED
EVIDENCE = BOUNDED_PRIMARY_SOURCE_READING
INDEPENDENT_REVIEW = NOT_PERFORMED
```

La entrada es distinta porque aporta una clasificación por isotropía y
automorfismos de Cayley, no solo un ejemplo de QCA/Weyl o un límite continuo.
