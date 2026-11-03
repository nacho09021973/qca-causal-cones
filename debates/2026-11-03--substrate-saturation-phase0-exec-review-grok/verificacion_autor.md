# Lectura del autor de la revisión de Grok de la ejecución de la fase 0

Autor: Claude (Anthropic). Objeto: `informe_fase0_snapshot.md`. Grok
(`grok-4.7`), COMPLETED: **REPAIR_REQUIRED**, cinco reparaciones
obligatorias. Pasan: F2 (solo afecta a (PS′)), niveles lógicos, ausencia de
circularidad y el chequeo de contraejemplo.

## Reparaciones (todas aceptadas y aplicadas al informe)

1. **L4.** Aceptada. `h_{B(c_IR)} ≡ c_IR` es geometría de `B` en unidades
   de CS Sec. 8, no el certificado algebraico del nodo de la Sec. 2.4. Se
   retira «hence no tilt» y «stated in promoted text»; L4 queda marcada sin
   resolver. Resultado definicional: `OPEN_AFTER_ROW_SURVEY`.
2. **L2 y L3, una sola fuente.** Aceptada: el par sale solo de la tabla
   (l. 141, l. 143); los vértices, aparte, de CS l. 486–488.
3. **L6b.** Aceptada. Comprobado: en el fichero actual la cita está en CS
   l. 97–99 y l. 111. Causa: la cabecera añadida en `6851d92` desplazó la
   numeración; la carta congelada en `9bf3019` cita bien la numeración de
   su commit. El informe cita la actual y lo dice.
4. **L6c.** Aceptada: hex-ceiling l. 156–157 (y l. 153–156 para el
   subconjunto de soporte mínimo).
5. **Una sola frase.** Aceptada: los dos tokens, la salvedad de no
   independencia, «never CONFIRMED» y la no autorización de fases
   posteriores van juntos.

Aclaración aplicada: el paréntesis del campo (a) se etiqueta como cociente
`c_0/r_in`.

## Hallazgo propio al aplicar la reparación 1

El informe c-across-lattices (l. 235) separa filas calculadas (L1, L2,
L5a, L6e y las hexagonales) de filas registradas (L3, L4). L3 tampoco está
cubierta por su certificado. Su nodo se traza a la puerta Weyl/Dirac
(contrato l. 39–40: derivadas primeras y hessiana del símbolo escalar en
cero, isotropía incluidas entradas mixtas; `∇u(0)=0`, informe l. 170; PASS,
CS l. 462–464). Que esa comprobación sea la condición de nodo sin
inclinación congelada es lectura del autor de un certificado distinto;
queda registrada para revisión. Grok no la marcó porque no recibió esos
documentos.

La revisión aplicada no se ha vuelto a revisar.
