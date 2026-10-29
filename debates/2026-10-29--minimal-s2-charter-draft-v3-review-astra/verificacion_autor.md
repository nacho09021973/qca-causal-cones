# Lectura crítica del autor — revisión Astra, ronda 3 (borrador v3 del charter s=2)

Fecha: 2026-10-29. Autor de esta lectura: Claude, autor del borrador. **No es una revisión
independiente.** La revisión independiente es la de Astra (gpt-6-astra, familia OpenAI).

## Ejecución

- Un intento, `COMPLETED`, de 10:43:40Z a 10:50:10Z.
- Antes del envío, `sha256sum -c inputs.sha256` dio OK.
- Documentos enviados: el borrador v3 (`8d8802a`, `b24ca440…`), los informes de las rondas 1 y 2,
  los contratos de rigidez y de la cota general, y P17.
- Herramienta: `revision_ciega.sh` @ `a32e189`.
- Autorización: «si, tercera ronda con Astra».

## Veredicto del revisor

`NOT_READY`, con **una sola reparación bloqueante**:

- A-R3-01: la regla de transferencia entre las familias P y F es demasiado amplia para Q-a.
- A-R3-02: una abreviatura «inside a certified class», no bloqueante.

Las seis lagunas A-R2 quedan resueltas; la A-R2-02, con la precisión A-R3-01. A5–A8 son
correctas, y también la red recíproca, la condición de traslado del nodo y las filas de rigidez
y de saturación. La regla de conflicto no autoriza relajar la cota.

## Contraste

**A-R3-01. Se acepta.** Comprobado razonando con cuantificadores.
- Q-a en F comprueba los pares `(g, h)` con `g ∈ G` y `h ∈ N_3`. En la clase P restringida a
  `V4`, solo los de `V4 × S_+`.
- Por tanto `E_F(U) ⇒ E_P(U)`, pero no al revés. Un resultado universal de Q-a en P no
  certifica Q-a en F.
- Una violación en F tampoco pasa a P: el `g` infractor puede no estar en `V4`, o el `h` no
  estar en `S_+`.
- La rigidez y la saturación dependen solo del símbolo, no de la simetría declarada. Por eso
  sí se transfieren por inclusión.

**A-R3-02. Se acepta.** «Inside a certified class» pasa a «where the ceiling is certified and
applies to that tuple, node included».

**Precisiones editoriales del revisor. Se aceptan:**
- A8 se asigna a un apartado del Paso 0.
- `UNITARY_SYMBOLS_EXIST` no autoriza ninguna salida universal.
- La parada de 4b-2 no borra resultados ya certificados.
- En un dominio vacío, Q-a y la saturación son verdaderas por vacuidad, y así se anota.
- 4a transporta solo los nodos de partida.

## Conclusión del autor

Las reparaciones se aplican al borrador como v4, sin cambiar el universo matemático. El revisor
dice que A-R3-01 es la única que bloquea y que el resto puede resolverse en la ejecución. El
usuario decide si congela con la v4 o pide una cuarta ronda.
