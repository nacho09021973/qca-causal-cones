# Lectura del autor de la revisión de Grok, ronda 2 (borrador fase 0, revisión 2)

Autor: Claude (Anthropic). Objeto: revisión 2 del borrador (SHA-256
`def7e7e5…`, copia en `borrador_rev2_snapshot.md`). Grok (`grok-4.7`),
COMPLETED: **REPAIR_REQUIRED**, una reparación obligatoria (trazabilidad de
L6b). Puntos 1 (dominio y circularidad), 2 (lógica) y 4 (independencia):
PASS. Ninguna reparación aplicada todavía: decide el usuario.

## Dominio y circularidad (punto 1, PASS)

Grok confirma, con las fuentes adjuntas, lo que preocupaba al usuario:
el nodo isótropo sin inclinación se define sobre el término lineal
(`{T_a, T_b} = 2 c_0^2 delta_ab`; `A(n)^2 = c_0^2 |n|^2 I` en
HEX_CEILING_GATE Sec. 1), no sobre la forma de `C_micro`; L6a, L6c, L6d y
L6f están dentro del dominio; un walk de `W_hex` o `W_hex^sym` que
saturase estaría dentro y refutaría (PH⇒); el bicondicional no es verdadero
por construcción.

## Reparación obligatoria (Sec. 2.2, L6b)

Grok tiene razón en el texto y en lo que podía comprobar. Comprobado por
el autor en esta sesión: CS l. 88–94 dice que L6B_TRIANGULAR_ROW, «a
revision of `C_ACROSS_LATTICES` restricted to row L6b, is promoted ... row
L6b ... with `s = 6`», y l. 106 dice «`s = 6`, not the parent's `s = 2`».
La cita existe, pero no estaba en los adjuntos, y «supersedes the parent
contract's declaration» es más fuerte que las fuentes: el contrato padre no
se enmendó y su tabla sigue en `s = 2`. Cierre propuesto: citar el informe
L6b Secs. 1–2 (`s = 6` por celda; el `s = 2` del padre cuenta por arista),
CS l. 88–94 y l. 106 para la promoción, decir que el contrato padre y la
tabla de retículos no se enmendaron, mantener la exclusión por `s = 6` y
quitar «supersedes».

## Aclaraciones (no obligatorias), propuestas de texto

1. «Admissible»: una frase que lo defina como nodo isótropo sin inclinación
   más pertenencia a las clases declaradas, no el grafo admisible de P17.
2. Sec. 7: «Finding one would refute (PH⇒)» solo para un testigo dentro
   del dominio; con `s ≠ 2` estaría fuera y no refutaría (PH).
3. (PS′): añadir la misma cláusula `OUTSIDE_DEFINITIONS`; quitar «no
   verdict on (PS′) beyond the counterexample test of Sec. 4», porque la
   Sec. 4 solo define contraejemplos de (PH).
4. L4: media frase para no tomar los vértices del rótulo `[-1,1]^3` junto
   al radio `1/sqrt3` de la columna.
5. Sec. 3.5 en condicional («record whether ...»), para no presuponer el
   hallazgo.
