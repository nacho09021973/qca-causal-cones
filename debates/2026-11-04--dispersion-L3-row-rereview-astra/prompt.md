# Segunda revisión (casa OpenAI, gpt-6.1-sol) del gate de dispersión de la fila L3, tras reparaciones

Autorización explícita del usuario (2026-11-04): «SUBE LOS 8 commit y push y
volvemos a revisar». Autor: Claude (Anthropic). Base: 414259c (subido).
Herramienta: ce09890. Generación comprobada antes del envío («OK», tras un
sondeo que superó 400 s). Una revisión, una ronda. Hashes en
`inputs.sha256`. Esta vez se adjuntan todos los módulos que importa el
verificador.

Comprobación previa. Sabido: la primera revisión (540e079) dio
REPAIR_REQUIRED con tres reparaciones; aplicadas en 414259c (35/35,
`L3_DISPERSION_COMPLETE`). Pregunta: ¿cierran las reparaciones lo pedido, sin
regresiones, y queda verificable lo que antes quedó [UNVERIFIED] por falta de
`verify_c_across_lattices_gate.py`? Cierre: PASS → el usuario decide promover
L3 con la Errata 1; REPAIR_REQUIRED → se repara; un fallo de fondo devuelve la
cuestión al usuario.

---
Revisa de forma adversarial e independiente la versión reparada del gate
DISPERSION_L3_ROW, escrito por Claude (Anthropic). Se adjuntan: el
verificador reparado, el informe reparado, la salida completa del
verificador reparado, el diff de la reparación, tu informe anterior sobre la
versión previa, el contrato congelado, y todos los módulos que el verificador
importa (verify_dispersion_corrections_gate.py, verify_c_across_lattices_gate.py,
verify_weyl_dirac_gate.py, verify_directional_saturation.py). Nada de lo
escrito por Claude es premisa. No tienes herramientas: no ejecutes ni
navegues. No propongas ampliar la investigación ni nuevas filas.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. REPARACIÓN 1. ¿Entran ahora en el registro evaluado las comprobaciones del
   constructor `row_L5a` (`P.CHECKS`), como hace el padre? ¿Bloquea la Parte 3
   las confirmaciones cuando falla un prerrequisito, y distingue «UNDECIDED»
   de «REFUTED»? ¿Queda algún camino en que el script termine con 0 tras un
   fallo registrado?
2. REPARACIÓN 2. ¿Emite el script el dictamen del contrato
   (`L3_DISPERSION_COMPLETE` / `_OPEN_<reason>`) con un criterio que
   corresponda a la Sec. 2 y 4 del contrato?
3. REPARACIÓN 3 Y ACLARACIONES. ¿Se limita ahora la segunda vía a lo que
   demuestra? ¿Son correctas las aclaraciones añadidas (alcance de
   «recomputed», identidad de trazas y no de matrices, emparejamiento por
   signo de β)?
4. LO ANTES NO VERIFICABLE. Con verify_c_across_lattices_gate.py adjunto:
   ¿son correctos `laurent_adjoint`, `laurent_support`, `is_zero_matrix` y
   `row_L5a` para el uso que hace el verificador (convención de soporte
   `z^h <-> exp(-i k.h)` combinada con `sigma` en `taylor_symbol`)?
5. NO REGRESIÓN. ¿Cambia el diff algo fuera de lo pedido? ¿Siguen leyéndose
   de la salida los valores del informe?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global PASS,
REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente.
---
