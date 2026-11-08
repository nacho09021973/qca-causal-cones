# Thirring: código de dos nodos y composición

Fecha: 2026-11-08. Autor: Codex (OpenAI).
Autorización: usuario «adelante, estas autorizado para hacer el experimento completo»,
tras propuesta de comprobar código de dos nodos, colisión, composición y régimen
relativista. Contrato escrito antes de ejecutar el cálculo. No revisión externa,
promoción, push ni cambio de otros gates autorizados por este contrato.

## Sabido, pregunta y abandono

- Sabido: la nota `2026-11-08--thirring-primera-colision.md` obtiene fuga hacia
  el segundo nodo para una codificación en uno solo; es un resultado de autor,
  no revisado. La definición primaria del modelo es Bisio et al.,
  arXiv:1804.08508v1, Ecs. (1), (2) y sección 3. La separación interactuante/libre
  está en sección 4, Ec. (8). El artículo se volverá a comprobar en PDF.
- Pregunta: ¿la inclusión de ambos nodos proporciona un código cerrado con
  colisiones entrelazantes componibles, y operaciones universales sin controles
  externos ni medidas intermedias, en el caso sin masa de esa primera colisión?
- Abandono de esta codificación: fuga que no pueda hacerse arbitrariamente
  pequeña o una restricción algebraica exacta que impida la universalidad de
  sus operaciones. Un fallo numérico no prueba imposibilidad general. El éxito
  de una puerta entrelazante tampoco prueba universalidad.

## Contrato congelado

Retículo Z, dos modos fermiónicos R,L por sitio (Fock local de dimensión 4).
U=F J, J=producto_x exp(i chi n_R(x)n_L(x)); F traslada R una celda a la derecha
y L una a la izquierda. Masa mu=0. Chi fijo durante cada ejecución; se comparan
modelos con chi=0,0.7,pi/2,pi, sin presentar variar chi como un control disponible.
No monedas locales, espejos, cambios de masa, medidas adaptativas o
postselección. Preparación inicial ideal de paquetes permitida y contabilizada;
no se contará como una puerta realizable por U.

Cada paquete de componente fija lleva un qubit:
|0>=f_s, |1>=Pi f_s, Pi f(x)=(-1)^x f(x), f_s uniforme en 2M sitios consecutivos.
Paquetes de la misma componente disjuntos; sectores fermiónicos con orden de
creación fijo. Se comprobará ortonormalidad. Se descontará la traslación libre
solo para comparar mapas; no es una operación física añadida.

Se estudiarán cruces completos de dos paquetes y una composición explícita
con al menos tres paquetes. Se caracterizará la familia de puertas accesibles
y el efecto de ancillas inicialmente independientes sin medidas intermedias.
La prueba de no universalidad se limitará al código y recursos declarados:
no excluirá otras codificaciones, programas cuánticos generales ni mu distinto
de cero. Si aparece una obstrucción exacta, no se abrirá automáticamente una
búsqueda de monedas, modelos o parámetros alternativos.

La comprobación física distinguirá: dinámica libre de los dos nodos, envolventes
lentamente variables, colisión, y existencia de una QFT relativista interactuante.
No se deducirá la última de las primeras. Se declararán a, tau, C_micro,
V_causal^max, V_grp^max y c_IR antes de compararlos. No se ajustará un reloj absoluto.

## Verificación y cierre

1. Álgebra de la colisión y de las operaciones compuestas.
2. Evolución directa en coordenadas de paquetes (sin introducir la matriz lógica
   esperada en el propagador) y contraste con la fórmula analítica.
3. Comprobación fermiónica mediante amplitudes antisimétricas, separada de la
   simulación por trayectorias. Casos límite chi=0 y pi.
4. Tres paquetes: evolución por coincidencias y comparación con composición;
   comprobación de obstrucción mediante un estado testigo.
5. Dispersión exacta y concentración de momento; no ajuste numérico como prueba.

Toda implementación y salida permanecerá en scripts/ y reports/. Se registrarán
versiones, semilla si procede, parámetros y hashes. No scripts científicos
temporales. Un informe final asignará por separado cierre, entrelazamiento,
composición, universalidad y alcance relativista. Nivel PRELIMINARY aunque pasen
las verificaciones de autor; ninguna revisión independiente se presume.

Nota de entorno: este checkout no contiene biblioteca/; se consultó
sources/README.md como inventario disponible. No se crea un índice alternativo.
