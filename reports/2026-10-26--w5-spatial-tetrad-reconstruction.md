# W5 completitud espacial del tetrad — reconstrucción

Fecha: 2026-10-26. Autor: Codex. Base: `1ece734`.
Autorización: «ADELANTE» al bloque f de la hoja del 22 de octubre.
Este gate de rango es distinto del W5 de fuente conjugada al tetrad.

## Reconstrucción y certificado

Se restauraron manualmente las barras invertidas del contrato
`theory/W5_SPATIAL_TETRAD_COMPLETENESS_GATE.md` y del informe
`reports/2026-09-30--w5-spatial-tetrad-completeness.md`.
Ambos pasan `scripts/check_reconstruction.py` contra `2d144d9`:
fuera de las cabeceras no cambian palabras, coeficientes ni criterios.
No se modificó código ni se reinterpretaron los componentes ausentes como gauge.

Se leyó y ejecutó `scripts/verify_w5_spatial_tetrad_rank.py`. Construye las
tres matrices derivadas respecto a z, calcula el rango de la matriz de
componentes del tetrad y el de los seis componentes simétricos del métrico.
Ambas aserciones pasan. SymPy calcula aquí el rango simbólico genérico:
se requiere g distinto de cero. En g = 0 los dos mapas son nulos, de rango cero.

## Segunda comprobación manual por entradas independientes

Para el tetrad linealizado declarado, las tres entradas diagonales son

\[
(\delta E_{11},\delta E_{22},\delta E_{33})
=(-2gz_1,-2gz_2,-2gz_3).
\]

Para g no nulo se recupera cada z dividiendo su entrada diagonal por -2g.
Por tanto el núcleo del mapa desde tres controles es cero y su rango es tres.
El menor diagonal del Jacobiano tiene determinante `-8g^3`, una comprobación
independiente del cálculo de rango de la matriz completa 9 por 3.

Para el métrico, la fórmula del informe da

\[
(\delta h^{11},\delta h^{22},\delta h^{33})
=(-4gz_1,4gz_2,-4gz_3).
\]

El menor correspondiente tiene determinante `64g^3`. Permite recuperar
los tres controles y prueba rango tres del mapa a las seis componentes,
para g no nulo. En particular, las tres direcciones del tetrad disponibles
en este ansatz no se pierden como rotaciones de frame dentro del mapa métrico.

## Relaciones que caracterizan la imagen métrica

Las entradas no diagonales cumplen, a este orden,

\[
2\delta h^{12}=\delta h^{22},\qquad
2\delta h^{13}=\delta h^{33},\qquad
\delta h^{23}=\delta h^{13}.
\]

Son tres relaciones independientes en el espacio simétrico de dimensión seis.
Recíprocamente, cualquier matriz simétrica que las cumpla se obtiene escogiendo
los z a partir de sus tres entradas diagonales para g no nulo. Esto identifica
la imagen sin recurrir al algoritmo de rango. Como control negativo, una
perturbación con solo componente 12 no nula viola la primera relación y no
pertenece a esta imagen. En g = 0 las relaciones siguen siendo necesarias,
pero ya no suficientes: la única perturbación accesible es cero.

Estas comprobaciones son manuales y se refieren al mapa lineal declarado,
no a un tetrad efectivo derivado de nuevo desde el walk ni a una clasificación
de todas las familias de QCA. Los términos desconocidos de orden g al cuadrado
no se fijan aquí. Las relaciones anteriores no se presentan como identidades
a todos los órdenes.

## Gauge, tiempo y antecedentes del registro

El rango por sí solo no identifica un sector gravitatorio con gauge fijado:
faltan la simetría, las restricciones y las condiciones de gauge que exige T3.
El mapa espacial tampoco introduce lapse, shift o una pierna temporal; no
resuelve T4. La ampliación abstracta a nueve controles de la sección 6 queda
como propuesta histórica, no como una construcción realizada en este bloque.

El lenguaje de retroacción y propagación del informe se lee con las adendas
posteriores: la corrección W3 es de campo medio y el espectro W4 requiere
las precisiones de fase, unidades y observable registradas en
`2026-10-26--w4-spectrum-reconstruction.md`. Esta reconstrucción no valida
afirmaciones más fuertes de la cadena W3–W5 ni cambia el gate de fuente W5.

## Validación y cierre

```sh
python3 -B scripts/check_reconstruction.py theory/W5_SPATIAL_TETRAD_COMPLETENESS_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-30--w5-spatial-tetrad-completeness.md
python3 -B scripts/verify_w5_spatial_tetrad_rank.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción 2/2 PASS; certificado de rango dos PASS. Los contrastes
manuales quedan trazados arriba; no se ejecutó código científico temporal.
No se ejecutó un barrido nuevo de certificados porque no se cambió código.

Avisos globales: de 211 a 165; se retiran 46 delimitadores desnudos (14 + 32).
No quedan avisos en el par reconstruido ni en este registro. El detector
global sigue saliendo con código 1 por la cola previa; el diff pasa la
comprobación de espacios.

Se mantiene `RESTRICTED_SPATIAL_METRIC_SUBMANIFOLD / GAUGE_COMPLETION_OPEN`,
con los rangos 3/9 y 3/6 para g no nulo. No hay revisión independiente nueva
ni promoción de evidencia; W1–W12 permanece cerrado por contrato.
El siguiente bloque tipográfico es W7 cinemática de espín 2 (bloque g).
