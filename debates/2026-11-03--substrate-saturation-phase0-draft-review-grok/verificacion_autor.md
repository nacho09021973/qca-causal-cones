# Lectura del autor de la revisión de Grok del borrador de fase 0

Autor: Claude (Anthropic). Objeto revisado: el borrador de
`theory/SUBSTRATE_SATURATION_PHASE0_GATE.md` con el hash que figura en
`inputs.sha256` (antes de los dos cambios pedidos por el usuario). Grok
(`grok-4.7`), COMPLETED: **REPAIR_REQUIRED**, seis reparaciones
obligatorias y cinco aclaraciones. No hay contraejemplo en los adjuntos.

## Cambios aplicados después de la revisión (instrucción del usuario)

«espera a Grok y luego aplica los dos cambios»:
1. «parallelotope» → «parallelepiped» en todo el borrador, con nota de
   terminología (Moriyama–Otozawa, arXiv:2411.09141v1, p. 11, usa
   paralelotopo = politopo que tesela por traslaciones; el hexágono lo es).
2. Lectura alternativa (PS′) por zonotopos, solo en la clase producto.

Ninguna de las seis reparaciones de Grok está aplicada: la decide el
usuario.

## Lectura de cada reparación

1. **Predicado: hipercubo, no paralelepípedo.** Aceptada en el diagnóstico.
   Las filas que saturan son segmento, cuadrado y cubo; ninguna es un
   paralelepípedo que no sea hipercubo, así que la tabla no distingue las
   dos nociones. Un rombo de 60° es paralelepípedo y puede no tener nodo
   isótropo; (PS⇐) afirmaría un `c_0` no definido. El cambio 1 (renombrar)
   no lo arregla: es terminológico. (PS′) hereda el mismo problema (dos
   generadores no ortogonales dan un rombo). Opciones para el usuario:
   (a) predicado «hipercubo salvo isometría», como pide Grok; (b) mantener
   «paralelepípedo» pero restringir (PS⇐) a los que admiten nodo isótropo
   sin inclinación en la clase declarada. Las dos estrechan el enunciado;
   (a) es la que la tabla puede auditar.
2. **L6b, `s`.** Resuelta con fuente: CS l. 94 y l. 106 («`s = 6`, not the
   parent's `s = 2`») fijan `s = 6` en el gate propio, promocionado, que
   sustituye la declaración del contrato padre. Cierre: citar esas líneas;
   L6b queda fuera por `s = 6` con cita, no por afirmación.
3. **Dos enunciados con el mismo nombre (filas declaradas / general).**
   Aceptada: quitar de la Sec. 6 «PS⇐ for general parallelepipeds».
4. **L4 con dos pares promocionados.** Aceptada: una sola fuente por fila
   (la tabla reescalada) y prohibición explícita de cruzar con CS Sec. 8.
5. **«the row or its class».** Aceptada: tres campos separados (walk,
   enunciado promocionado con su alcance, existencial por sustrato).
6. **La fase 0 no puede fallar y abre la fase 2.** Aceptada, y es la de
   más peso. La conjetura se leyó de esta misma tabla; auditarla sobre ella
   no aporta evidencia. Cierre: renombrar el veredicto como auditoría
   (p. ej. `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`), decir en la misma frase
   que no es evidencia, y quitar la condición «fase 2 solo tras
   NOT_REFUTED». Una prueba que pueda fallar exige una forma que no esté
   en la tabla (otra carta, con cálculo).

## Valoración

La revisión confirma lo que el borrador ya admitía en su Sec. 5 y va más
lejos: la fase 0, tal como está, es casi vacía. Su utilidad real se reduce
a fijar definiciones y el alcance del enunciado antes de la fase que sí
puede fallar.
