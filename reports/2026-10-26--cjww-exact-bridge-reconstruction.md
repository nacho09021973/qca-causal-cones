# Puente CJWW exacto de grafo dinámico — reconstrucción

Fecha: 2026-10-26. Autor: Codex. Base: `b27dcdb`.
Autorización: «adelante» al bloque h de la hoja del 22 de octubre.
Este registro contrasta manualmente la prueba; no es revisión independiente.

## Alcance y comprobador

Se restauraron manualmente las barras invertidas del contrato
`theory/EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE.md` y del informe
`reports/2026-09-29--explicit-cjww-dynamic-graph-bridge.md`.
Ambos pasan `scripts/check_reconstruction.py` contra `2d144d9`:
fuera de las cabeceras solo cambian barras invertidas, sin alterar palabras,
coeficientes, criterios o cuantificadores. Se restauraron también las
desigualdades que habían pasado a saltos de línea.

La búsqueda en los scripts no localizó un certificado ejecutable específico
del lema de canal complementario constante. Los scripts de factorización
CJWW y de estado de referencia de gravedad inversa responden a otras preguntas;
no se ejecutaron como sustitutos. No se declara un PASS computacional del lema.

## Primera vía: pureza y superposiciones

Con un fondo puro fijo y una evolución conjunta unitaria, V es una isometría.
Conjugar su salida de materia por U inversa reduce B1 al canal identidad.
Para cada vector puro de materia, la salida conjunta es pura y su marginal
de materia también: por tanto la salida es producto con ese mismo vector.

La linealidad sobre una base y las superposiciones de cada par fija el
coeficiente no diagonal del estado de materia. El solapamiento de los dos
vectores geométricos debe ser exactamente uno, no solo tener módulo uno.
Con norma uno, esto obliga a que ambos vectores geométricos coincidan.
Se obtiene una única Gamma independiente de la entrada. Al deshacer la
conjugación, V es el producto de Gamma con la evolución U de materia.

En la materia separable de este repo, las combinaciones finitas de vectores
de base son densas. V y U son operadores acotados, de modo que la igualdad
se extiende por continuidad a todos los vectores de norma finita. La misma
igualdad para matrices de densidad se extiende en norma de traza desde las
de rango finito. Así se explicita el paso que la prueba histórica deja
implícito para la red infinita, sin cambiar sus cuantificadores.

## Segunda vía: operadores de canal

En una base ortonormal del entorno, definir

\[
K_\alpha=(\langle\alpha|\otimes I)V,
\qquad L_\alpha=U^\dagger K_\alpha.
\]

B1 implica que para cada vector unitario psi,

\[
\sum_\alpha |L_\alpha\psi\rangle\langle L_\alpha\psi|
=|\psi\rangle\langle\psi|.
\]

Cada sumando es positivo y el resultado tiene soporte de dimensión uno.
Proyectar sobre cualquier vector ortogonal a psi da una suma de módulos
cuadrados igual a cero: cada L alfa por psi es colineal con psi.
Un operador lineal que deja cada vector en su propia recta es un escalar:
en una base tiene valores diagonales, y aplicar la condición a la suma
de dos vectores de base obliga a que sus valores diagonales sean iguales.
Así `L_alpha = c_alpha I` y `K_alpha = c_alpha U`.

La normalización de V da `sum_alpha |c_alpha|^2 = 1`. Los elementos del
estado geométrico de salida son

\[
\operatorname{tr}(K_\alpha\rho K_\beta^\dagger)
=c_\alpha\overline{c_\beta}\operatorname{tr}(U\rho U^\dagger)
=c_\alpha\overline{c_\beta},
\]

independientes de rho. Esto reproduce la conclusión sin usar el argumento
de rango de Schmidt. Es un contraste manual, no un nuevo resultado de novedad.

## Controles de cuantificadores y casos límite

- B1 es para todo estado de materia, incluidas superposiciones coherentes,
  con el mismo fondo y la misma evolución conjunta. No basta verificar una base.
- B2 pide que el marginal de geometría distinga al menos dos entradas sobre
  ese mismo fondo. El teorema prohíbe esa información, no cualquier cambio
  de geometría. Un producto `R_g tensor U` satisface B1 y puede cambiar
  el fondo a otro estado fijo, pero no satisface B2.
- Como control negativo de la universalidad, una copia controlada de un bit
  a un registro inicialmente cero conserva los dos estados de base de materia
  y deja información en el registro; una superposición pierde sus coherencias
  al trazarlo. Satisface el test restringido de base y viola B1 para todas las
  entradas. No es un contraejemplo al lema.
- No intervienen el soporte de catorce saltos, la localidad, la dimensión de
  grafo ni una síntesis de puertas. El argumento ya actúa en la isometría
  abstracta. No se generaliza aquí el contrato a fondos mixtos, correlacionados,
  otros factores relacionales o aproximaciones de canal.
- Las etiquetas W1–W4 de la sección histórica de escapes nombran cuatro rutas
  de relajación. No deben confundirse con los nombres posteriores de gates,
  como el W2 de transporte o el W4 de rigidez geométrica.

## Validación y cierre

```sh
python3 -B scripts/check_reconstruction.py theory/EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-29--explicit-cjww-dynamic-graph-bridge.md
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción 2/2 PASS. La prueba se contrastó manualmente por las dos vías
anteriores. No se modificó código, no se ejecutó código científico temporal
ni un barrido nuevo de certificados, y no se atribuye al lema un certificado
ejecutable que no tiene.

Avisos globales: de 119 a 65, al retirar 54 delimitadores desnudos (14 + 40).
No quedan avisos en el par reconstruido ni en este registro. El detector
global sigue saliendo con código 1 por la cola restante; el diff pasa la
comprobación de espacios.

Se mantiene `STRONG_EXACT_BRIDGE_IMPOSSIBLE` bajo los cuantificadores del
contrato. No es un no-go para toda geometría dinámica, no se abre una ruta
sucesora y no se promueve evidencia por una revisión del mismo autor.
W1–W12 permanece cerrado por contrato. El bloque documental siguiente es
normalización gravitatoria G0 y selección de clase dinámica (bloque i).
