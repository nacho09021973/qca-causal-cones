# Procedencia y comprobaciones de la primera edición

Fecha: 2026-09-30. Checkout inspeccionado:
`research/gravitational-normalization-gate` @
`16850476a6320c55aaf6d25471d00454cdc15b41`.

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

El atlas conserva los resultados negativos y las incertidumbres. Al recuperar
un expediente, reemplazar «pendiente» solo después de comprobar sus
cuantificadores, evidencia y estado vigente; registrar el commit de origen.
Un cambio documental no modifica contratos ni autoriza cálculos sucesores.
