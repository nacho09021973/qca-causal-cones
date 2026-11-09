# Revisión independiente (casa OpenAI, gpt-6.1-sol) del gate de dispersión de la fila L3

Autorización explícita del usuario (2026-11-04): «que lo revise astra».
Autoriza el envío a OpenAI (`gpt-6.1-sol`, vía `codex exec`, miembro
astra); no autoriza promover. Autor: Claude (Anthropic). Base: b9b0e58
(local). Herramienta: ce09890. Generación comprobada antes del envío
(«OK»; el primer sondeo superó 180 s, el segundo respondió). Una revisión,
una ronda. Hashes en `inputs.sha256`.

Comprobación previa. Sabido: contrato congelado d3868fa antes de calcular;
verificador nuevo 34/34; informe con HL3a–e confirmadas. Pregunta: ¿son
correctos el contrato, el verificador y el informe, y se siguen las
conclusiones de lo que imprime el verificador? Cierre: PASS → el usuario
decide promover (junto con la Errata 1); REPAIR_REQUIRED → se repara; un
fallo de fondo devuelve la cuestión al usuario.

---
Revisa de forma adversarial e independiente el gate DISPERSION_L3_ROW,
escrito por Claude (Anthropic): contrato theory/DISPERSION_L3_ROW_GATE.md,
verificador scripts/verify_dispersion_L3_row_gate.py, informe
reports/2026-11-04--dispersion-L3-row.md y la salida completa del
verificador (salida_verificador.txt). Se adjuntan también, para leer el
código importado, scripts/verify_dispersion_corrections_gate.py (gate padre,
revisado y promovido) y scripts/verify_weyl_dirac_gate.py (símbolos de L3,
revisado), la Errata 1 del gate padre y extractos literales numerados de
scripts/verify_directional_saturation.py (walk1 = CJWW (5.12)), de la tabla
del informe padre y de la tabla de filas del contrato C_ACROSS. Nada de lo
escrito por Claude es premisa. No tienes herramientas: no ejecutes ni
navegues. No propongas ampliar la investigación ni nuevas filas.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. CONTRATO. ¿Fija la pregunta, los cuatro símbolos (A±, B± de
   `verify_case`), la normalización, el método y las hipótesis antes del
   cálculo? ¿Es honesto sobre que las hipótesis se escribieron tras leer el
   código? ¿Respeta el alcance del padre?
2. VERIFICADOR. ¿Reproduce la rama genérica s = 2 del padre (Parte 2:
   soporte, escala, `taylor_symbol`, traza y determinante truncados,
   `analyse_block`, `walk_group`) sin cambiar bytes revisados? ¿Es correcta
   la convención `sigma = +1` para `published_symbol` (la que usa el padre
   para L1, L2) y `sigma = −1` para L5a? ¿Son correctas y suficientes las
   comprobaciones afirmadas (unitaridad con `P.laurent_adjoint`, det = 1,
   traza, soporte)? ¿Hay algún modo en que imprima CONFIRMED sin que la
   comparación lo justifique (por ejemplo, `same_pair`, la igualdad de
   listas de `G_walk`, `alpha0.is_negative`)?
3. RESULTADOS. ¿Se leen de la salida los valores de la tabla del informe
   (β, α, α_0, G_walk)? ¿Reproducen las filas de comparación ((5.12) y L5a)
   la tabla del padre? ¿Es correcta la segunda vía (con det U = 1 el
   polinomio característico depende sólo de la traza; χ = −1 es k → −k de
   χ = +1, que invierte β y conserva α)?
4. CONSECUENCIAS. ¿Son correctas y acotadas las consecuencias de la Sec. 4
   (lista de filas con β; cobertura de He; Hd; pares compartidos en BCC y
   Hf; la advertencia de que igual polinomio característico no implica
   igual símbolo)? ¿Afirma el informe algo que no esté en la salida?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global PASS,
REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente.
---
