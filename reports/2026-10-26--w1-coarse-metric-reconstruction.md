# W1 métrica gruesa — reconstrucción tipográfica

Fecha: 2026-10-26. Autor: Codex. Base de sesión: `ec7c7ee`.
Autorización: «adelante» al bloque documental de geometricidad y métrica gruesa
W1. Este registro corresponde al segundo gate del bloque c.

## Alcance

Restauración manual de barras invertidas en `theory/W1_COARSE_METRIC_GATE.md`
y `reports/2026-09-29--w1-coarse-metric.md`, con cabeceras de procedencia.
Ambos pasan `scripts/check_reconstruction.py` contra `2d144d9` sin cambiar
palabras, coeficientes o criterios fuera de la cabecera. Se recuperaron
también los saltos de línea de `\ni`. No se modificaron certificados.

## Contraste desde los proyectores

Con registros inicialmente independientes de la materia, el generador reducido
de primer orden es la suma de las medias de B multiplicadas por los A.
Agrupar los proyectores de extremos por sitio da la suma de las medias de B
de los enlaces incidentes, multiplicada por el proyector de posición y la
identidad de coin. No aparece ningún desplazamiento de materia nuevo.

En un fondo producto propio de B, el acoplamiento no entrelaza los registros
con materia. Su acción es exactamente una fase de posición. Congelando v
en un punto, la multiplicación del símbolo W0 por `exp(-igv)` multiplica
ambos valores propios por el mismo escalar. Las eigenfases suman gv en una
rama local continua; derivar en momento elimina ese término.

Como segunda vía, la matriz de eigenvectores es la misma para el símbolo
congelado. En una rama compatible del logaritmo, el generador es el plano
más `g v I`, por lo que su derivada en momento coincide con la plana.
En un fondo homogéneo, v = 14b y estas relaciones son exactas para el
símbolo global, sin aproximación de fondo lento.

Para el producto de estados cero, se contrastó el término de doble conmutador
con la derivación de covarianzas y solapamientos exactos del
[puente perturbativo reconstruido](2026-10-26--w1-typographic-reconstruction.md).
La expresión representa decoherencia del canal reducido, no un Hamiltoniano
unitario ni una deformación demostrada del tetrad.

## Defecto no tipográfico y límites de lectura

La sección 2 del informe escribe `H_g = v I + H_W + ...`, pero su propio
símbolo contiene `exp(-igv)` y sus eigenfases contienen gv. Con las definiciones
de v y g que allí se usan, falta el factor g en el término escalar de H_g.
No se puede restaurar ese factor añadiendo solo barras invertidas. Se conserva
la fórmula histórica y se señala el defecto aquí y en su cabecera; no debe
citarse esa fórmula como comprobada. La expresión consistente, en la rama
local indicada arriba, es `H_g = g v I + H_W` al orden declarado.
El defecto no cambia la derivada en momento porque el término es escalar
e independiente de p.

La derivada del símbolo W_g en sí recibe la misma fase que W0; no es
literalmente idéntica. La igualdad pertinente es la de las pendientes de
eigenfases o la del término de Weyl del generador local.

Para v variable, el símbolo congelado no establece por sí solo una identidad
exacta del logaritmo de Floquet global: los operadores de fase y transporte
pueden no conmutar, y las correcciones de gradiente necesitan análisis propio.
No se extiende el resultado local a todos los órdenes, fondos o acoplamientos.
La igualdad del cuerpo exterior usa también el argumento de camino extremo
registrado en la [reconstrucción de geometricidad](2026-10-26--w1-geometricity-reconstruction.md),
no solo la cota por saltos permitidos.

## Validación

```sh
python3 -B scripts/check_reconstruction.py theory/W1_COARSE_METRIC_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-29--w1-coarse-metric.md
python3 -B scripts/verify_w1_geometricity.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción 2/2 PASS. Se ejecutó el certificado relacionado de geometricidad,
con cinco PASS; no certifica este argumento métrico, contrastado manualmente.
Se retiran 52 delimitadores desnudos (18 + 34). El bloque c completo retira
110 avisos: de 411 a 301; el detector sigue saliendo con código 1 por la cola
restante. No aparecen avisos en los cuatro documentos reconstruidos ni en
estos registros nuevos. El diff pasa la comprobación de espacios.

Se conserva `W1_SCALAR_POTENTIAL_ONLY / NO_METRIC_DEFORMATION` con el alcance
local y perturbativo anterior. No hay revisión independiente ni promoción
científica; W1–W12 continúa cerrado por contrato. Sigue pendiente el bloque d:
reconstruir el contrato e informe de curvatura y dinámica W3.
