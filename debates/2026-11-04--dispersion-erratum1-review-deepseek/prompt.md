# Revisión independiente (casa DeepSeek) de la Errata 1 del gate de correcciones de dispersión

Autorización explícita del usuario (2026-11-04): «haz la 4 y la 3», donde la
opción 3 es «una errata con fecha y una revisión breve» sobre la incoherencia
de símbolos L3/L4. Se elige DeepSeek (gpt-6.1-sol está revisando en paralelo
otro documento). Autor: Claude (Anthropic). Base: 648be9c. Herramienta:
ce09890. Modelo: deepseek-v4-pro (comprobar generación antes del envío). Una
revisión, una ronda. Hashes en `inputs.sha256`.

Comprobación previa. Sabido: la Enmienda 1 de la fase 0 (aprobada) anotó sin
reparar que el contrato de dispersión (l. 63, 67) asigna `walk2()` = CJWW
(5.15) a la fila L3 «BCC» y `walk1()` = CJWW (5.12) a L4 «cube», contra el
contrato padre C_ACROSS (l. 76, 78). Los resultados de ese gate están
promovidos (CS Sec. 13). Pregunta: ¿describe la errata con exactitud la
incoherencia, lo que se mantiene y lo que cambia, sin afirmar más? Cierre:
PASS → el usuario decide aprobarla y se anota en CS Sec. 13;
REPAIR_REQUIRED → se repara; un fallo de fondo devuelve la cuestión al
usuario.

---
Revisa de forma adversarial e independiente la errata
theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_ERRATUM_1.md, escrita por
Claude (Anthropic). Se adjuntan: la errata, el contrato congelado del gate
de dispersión, su contrato padre (theory/C_ACROSS_LATTICES_GATE.md), el
informe del gate de dispersión y extractos literales numerados del
verificador de dispersión, de scripts/verify_directional_saturation.py
(walk1, walk2), de la Enmienda 1 de la fase 0 (Sec. 2, punto 4, grupos
generados) y de state/CURRENT_STATE.md Sec. 13. La errata no es premisa. No
tienes herramientas: no ejecutes ni navegues. No propongas ampliar la
investigación ni calcular la fila que falta.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. INCOHERENCIA. ¿Es exacta la tabla de la Sec. 1 (padre l. 76, 78;
   contrato de dispersión l. 63, 67; verificador l. 573–576;
   walk1/walk2)? ¿Se sigue de la Enmienda 1 que (5.12) genera BCC y (5.15)
   genera Z^3, con C_micro = [−1,1]^3 para ambos? ¿Es justo decir que el
   defecto está en la tabla del contrato y no en la ejecución?
2. LO QUE SE MANTIENE. ¿Son los coeficientes de la tabla del informe
   resultados para los símbolos importados, y es correcta la reasignación
   («L3» impreso = (5.15), «L4» impreso = (5.12))? ¿Es cierto que no
   dependen de las etiquetas los hallazgos listados (términos beta, contenido
   armónico, Hd, refutación de Hf por L2 = L6e)?
3. LO QUE CAMBIA. (a) ¿Es cierto que la fila L3 del padre (batería estándar
   d = 3) no tiene entrada, según las líneas 560 y 562 del verificador, y que
   «the thirteen massless rows» sobrestima la cobertura en una fila? (b) ¿Es
   correcto restringir He a las filas declaradas salvo L3? (c) Con los grupos
   corregidos, ¿es correcta la nueva pertenencia al sustrato BCC, el par
   compartido (5.12) con el bloque de L5b de signo de beta opuesto al de L5a
   (leído a mano de la tabla) y la afirmación de que las l. 81 y 263 del
   informe siguen siendo ciertas? ¿Queda intacto REFUTED_BY_ROW_L6e?
4. ALCANCE. ¿Respeta la errata lo que dice no hacer (no cambia bytes de
   contrato, informe ni verificador; no recalcula; no decide la
   coincidencia de símbolos)? ¿Se le escapa algún enunciado promovido de CS
   Sec. 13 que dependa de las etiquetas L3/L4?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global PASS,
REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente.
---
