# W1 — reconstrucción del puente perturbativo

Fecha: 2026-10-26. Autor: Codex. Base: `d9bec1a`.
Autorización: «commit y push y continúa», tras el cierre del bloque W2.
Alcance: bloque b de la hoja del 22 de octubre; contrato e informe del puente
perturbativo W1. No incluye reconstruir todavía geometricidad y métrica gruesa.

## Reconstrucción

Se restauraron manualmente las barras invertidas de:

- `theory/W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE.md`;
- `reports/2026-09-29--w1-perturbative-backreaction-bridge.md`.

Los dos documentos pasan `scripts/check_reconstruction.py` contra `2d144d9`:
fuera de las cabeceras de procedencia solo cambian barras invertidas.
Se recuperaron también los saltos de línea que ocultaban `\ne`.
No se cambiaron criterios, coeficientes ni conclusiones del texto histórico.

## Comprobaciones manuales desde los operadores

Se trabaja en el sector de una partícula y con registros de enlace inicialmente
independientes de la materia. Para el fondo regular los enlaces están en
producto de estados cero. Las comprobaciones siguientes son del autor de esta
reconstrucción, no una revisión independiente ni un certificado ejecutable nuevo.

Para el proyector A del informe, la descomposición de la puerta en los sectores
A = 0 y A = 1 da exactamente identidad y `exp(-ig B)`, respectivamente.
Eso comprueba unitariedad y recuperación en g = 0 sin expansión perturbativa.
Los proyectores de ocupación conmutan; los operadores B de distintos enlaces
actúan en registros distintos. Por tanto también conmutan los generadores.
El argumento de paridad se conserva: un desplazamiento con primera componente
uno cambia la paridad y da dos matchings por cada una de las siete familias.

Para un enlace con ocupación media a, su estado reducido es exactamente
`(1-a) eta + a exp(-ig B) eta exp(ig B)`. Derivar en cero da el conmutador
del informe. Con B = Z + X y eta = |0><0|, la relación de Pauli
`[B,Y] = -2i X + 2i Z` da la pendiente `-2a` de la expectativa de Y.
En sentido inverso, los estados cero y uno tienen medias de B iguales a
uno y menos uno; inducen la diferencia `2A` del generador de materia.
Esto demuestra el test existencial con esos estados concretos, sin afirmar
que cualesquiera estados con distinta media de Z tengan distinta media de B.

En el fondo regular cada sitio pertenece a catorce enlaces, por lo que
la suma de A es `14 I`. El término de primer orden es un conmutador con
la identidad y desaparece. La covarianza de B entre enlaces es la identidad
en los índices de enlace: varianza uno y covarianzas cruzadas cero.
La expansión de doble conmutador queda entonces

\[
-\frac{g^2}{2}\sum_e[A_e,[A_e,\sigma]]
=g^2\sum_e\left(A_e\sigma A_e-\frac12\{A_e,\sigma\}\right).
\]

Aquí se usa A al cuadrado igual a A. Esta igualdad fija las barras perdidas
de la suma, sigma, paréntesis y anticonmutador del informe.

## Segunda vía: solapamientos exactos del entorno

Para una posición x, solo rotan los catorce registros incidentes a x.
Sean Sx y Sy los conjuntos de enlaces incidentes a dos posiciones distintas.
Su intersección tiene tamaño k = 1 cuando son vecinas y k = 0 en otro caso.
De `B^2 = 2 I` se obtiene, poniendo t igual a raíz de dos por g,

\[
c(g)=\langle0|e^{-igB}|0\rangle
=\cos t-\frac{i}{\sqrt2}\sin t,
\qquad
q(g)=|c(g)|^2=1-\frac12\sin^2 t.
\]

Los enlaces exclusivos de Sx y Sy son 14-k en cada conjunto, así que el
factor exacto de una coherencia de posición después de la interacción es

\[
c(g)^{14-k}\overline{c(g)}^{14-k}
=q(g)^{14-k}
=1-(14-k)g^2+O(g^4).
\]

Se recuperan los coeficientes -13 y -14 del informe por una vía distinta
de la expansión de covarianzas. Para x = y los estados del entorno son
iguales y el factor es uno: la población no cambia. El resto O(g^3)
escrito en el informe es compatible con este resto más restrictivo.

## Límites de lectura detectados

La frase histórica de la sección 7 «cannot remain exactly CJWW for finite
nonzero g» debe leerse en el régimen perturbativo con adquisición no trivial
de información. No demuestra exclusión para todos los acoplamientos reales.
La fórmula exacta anterior tiene recurrencias cuando t es un múltiplo entero
de pi: q = 1, la puerta condicionada es más o menos identidad y ya no hay
adquisición de información por el entorno. No contradice el no-go condicionado
a retroacción, pero impide usar esa frase como afirmación global en g.
Esta observación se registra aparte y no se incorpora como cambio silencioso
del texto histórico o del contrato congelado.

El regulador de caja periódica debe preservar los catorce vecinos distintos;
una caja de lado dos identifica desplazamientos opuestos. Para la lectura
de estas fórmulas basta una caja cúbica de lado par al menos cuatro, o la
red infinita con las mismas relaciones locales. El texto histórico solo dice
«even periodic cubic box» y no explicita esta condición.

## Comprobaciones ejecutadas

```sh
python3 -B scripts/check_reconstruction.py theory/W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-29--w1-perturbative-backreaction-bridge.md
python3 -B scripts/verify_w1_geometricity.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción: 2/2 PASS. Certificado relacionado de geometricidad: cinco
PASS, incluidos los catorce bloques y el testigo de interferencia de dos pasos.
Ese certificado no comprueba la derivación completa del canal reducido que
se contrastó arriba manualmente. No se modificó código ni se ejecutó código
temporal para producir resultados científicos.

Avisos globales: 499 antes, 411 después; se retiran los 88 delimitadores
desnudos de estos dos documentos (22 + 66). El detector sigue terminando
con código 1 por la cola restante. No aparecen avisos en los dos documentos
reconstruidos. `git diff --check` pasa. No se ejecutó un nuevo barrido
completo de certificados al no cambiar código.

## Estado y siguiente bloque

No hay revisión independiente ni promoción científica. El puente conserva
su techo causal-unitario y la síntesis QCGD completa sigue abierta. La
conclusión posterior `W1_SCALAR_POTENTIAL_ONLY / NO_METRIC_DEFORMATION`
permanece vigente; W1–W12 sigue cerrado por contrato.

El siguiente bloque documental es el c de la hoja: contratos e informes de
geometricidad W1 y métrica gruesa W1. Las dos limitaciones de lectura anteriores
deben acompañar cualquier futura revisión del puente perturbativo.
