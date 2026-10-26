# W1 geometricidad — reconstrucción tipográfica

Fecha: 2026-10-26. Autor: Codex. Base de sesión: `ec7c7ee`.
Autorización: «adelante» al bloque documental de geometricidad y métrica gruesa
W1. Este registro corresponde al primero de los dos gates del bloque c.

## Alcance y procedencia

Restauración manual de barras invertidas en
`theory/W1_GEOMETRICITY_GATE.md` y
`reports/2026-09-29--w1-geometricity.md`, con cabecera de procedencia.
Ambos pasan `scripts/check_reconstruction.py` contra `2d144d9`:
fuera de la cabecera no cambian palabras, coeficientes o criterios.
Se recuperaron también `\ne` y `\ni` que habían pasado a saltos de línea.

Se leyó y ejecutó `scripts/verify_w1_geometricity.py`, incluida su extracción
exacta de bloques desde `walk2()` en `scripts/verify_directional_saturation.py`.
Sus cinco comprobaciones pasan: cancelación de ocho contribuciones, matriz
del camino elegido, enlace exclusivo, derivada no nula del enlace volteado
y control de fondo propio de B. No es una revisión independiente.

## Contraste manual y segunda formulación

Cada A es diagonal en posición. Por tanto V es una suma de proyectores de
posición por unitarios R del entorno. Los documentos alternan el orden de
los factores materia/entorno; estas expresiones se entienden mediante el
intercambio canónico de factores tensoriales, no como otro modelo.

En un paso, cada bloque de materia S se multiplica por un unitario R del
entorno. Como R es invertible, no puede anular un bloque S no nulo.
El argumento conserva el soporte de operadores, sin exigir que toda matriz
S no nula actúe de modo no nulo sobre cualquier espinor inicial.

Para dos pasos, la expansión manual es

\[
\sum_y R_z(g)R_y(g)\otimes M_y,
\qquad M_y=S_{z-y}S_y.
\]

La derivada en cero es la suma de los términos con Kz y Ky. El término
con Kz desaparece porque la suma de M es cero. En la componente con solo
el enlace elegido volteado, queda `-i M_*`, como comprueba el certificado.
Para explicitar el testigo de amplitud escalar, se puede elegir el espinor
inicial `(1,0)` y el final `(0,1)`: la derivada es `1/16`.
No se afirma no anulación para todos los espinores. En una caja finita que
no identifique los sitios usados, la amplitud es analítica; una derivada
no nula garantiza un entorno perforado de cero con amplitud no nula.
Para este testigo basta una caja periódica de lado par al menos seis.

Como control independiente del desarrollo por caminos, en el fondo propio
homogéneo de B cada uno de los catorce enlaces aporta la misma fase.
V actúa entonces como `exp(-i 14 sqrt(2) g)` sobre toda la materia, y sus
potencias conservan exactamente la cancelación de CJWW para cualquier g.
Esto explica por qué el PASS se limita al soporte sensible a interferencias.

## Alcance del cuerpo exterior

Que cada paso use el mismo conjunto de saltos demuestra la cota exterior
del cubo; la igualdad del soporte convexo necesita además alcanzar vértices.
La sección correspondiente de `scripts/verify_directional_saturation.py`
expone el argumento plano: para cada vértice s, S_s tiene rango uno y traza
no nula, de modo que `S_s^t = tr(S_s)^(t-1) S_s` no se anula.
Se leyó ese argumento; no se ejecutó en esta sesión el certificado completo.

En W1 sobre la red infinita, llegar a t por s en t pasos tiene un único
camino de posiciones. En un regulador finito se exige ausencia de envolturas
periódicas durante ese intervalo; no se afirma crecimiento indefinido en un toro.
Su bloque es el producto de los unitarios del entorno a lo largo del camino,
tensorizado con la potencia anterior. El producto de unitarios no se anula
ni anula un estado no nulo del entorno. Así se justifica manualmente la
igualdad del cuerpo convexo de soporte de operadores con el cubo escalado.
Esto no convierte en alcanzable cada punto interior, ni prueba una afirmación
uniforme para todos los espinores fijados. El certificado de geometricidad
ejecutado no comprueba por sí solo esta extensión para todo t.

## Validación y techo

```sh
python3 -B scripts/check_reconstruction.py theory/W1_GEOMETRICITY_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-29--w1-geometricity.md
python3 -B scripts/verify_w1_geometricity.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción 2/2 PASS, certificado relacionado cinco PASS. Se retiran
58 delimitadores desnudos (14 + 44). El detector global conserva avisos
previos y sigue saliendo con código 1; no quedan avisos en este par.
No se modificó código ni se ejecutó código científico temporal.

Permanece `W1_OPERATIONAL_GEOMETRY_PASS` con
`FINITE_TIME_EXACT_SUPPORT_ONLY`; no acredita métrica ni dinámica de Einstein.
No se promueve evidencia ni se reabre W1–W12.
