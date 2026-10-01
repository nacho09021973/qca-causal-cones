# F16 — Preflight Białynicki-Birula: QCA de Weyl y Dirac

Fecha: 2026-10-01. Fuente: `biblioteca/Dirac and Weyl Equations on a Lattice as Quantum Cellular Automata.pdf`, Białynicki-Birula. SHA256: `656a1345b77c6b1288fb54492f40213e59ead8f58e67b42203e722cc3bb04842`.

Lectura primaria: pp.1-5 mediante `pdftotext -layout`. El artículo define una evolución local y unitaria en red cúbica para una función de onda de dos componentes; localidad, unitaridad, invariancia de valores constantes y simetría de la red llevan al límite Weyl (pp.1-3). La regla BCC usa ocho desplazamientos diagonales y matrices locales, y el límite de baja escala recupera el propagador Weyl (pp.2-5, Ecs.2-34). La masa se incorpora mediante inversiones de helicidad y el potencial electromagnético mediante fases locales (p.5).

Resultado:
```text
F16_BIALYNICKI_BIRULA_PREFLIGHT = PUBLISHED_CUBIC_QCA_WEYL_DIRAC_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT
FOUR_SPECIES_TEST = NOT_EXECUTED
EVIDENCE = BOUNDED_PRIMARY_SOURCE_READING
INDEPENDENT_REVIEW = NOT_PERFORMED
```

Es un antecedente de regla QCA explícita, distinto de F14 (clasificación por isotropía), F15 (axiomas informacionales) y F12 (Maxwell compuesto). No aporta métrica variable, controles CJWW ni backreaction.
