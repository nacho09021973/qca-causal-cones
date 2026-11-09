# Revisión independiente de la respuesta «c en distintos sustratos» (paso 1 del plan)

Autorización explícita del usuario: «si» (2026-11-03) a pasar al paso 1 de
`reports/2026-11-02--work-plan-next-session.md`, revisión independiente que
exige enviar texto a terceros. Autoriza este envío externo a xAI; no
autoriza publicación ni promoción. Autor: Claude (Anthropic). Revisor: Grok
grok-4.7 (xAI), vía revision-ciega. Base: dac86d8. Una revisión, una ronda.
Herramienta: ce09890a0d5f68a6634f358eff2e477ac5f15ec7. Hashes de entrada en
`inputs.sha256`.

Comprobación previa (regla de los tres puntos). Sabido: la respuesta es una
síntesis de resultados promocionados en CURRENT_STATE, PRELIMINARY como
síntesis. Pregunta: ¿afirma algo más de lo que esos resultados sostienen?
Cierre: PASS, y la respuesta es citable; REPAIR_REQUIRED, y se repara; si la
reparación la deja sin contenido propio, se cumple el criterio de cierre
del repo (plan, Sec. 4).

---
Revisa de forma adversarial e independiente el documento
2026-11-02--c-across-substrates-answer.md, escrito por Claude (Anthropic).
Es una síntesis que dice no contener ningún resultado nuevo: cada
afirmación debe poder rastrearse a una sección de CURRENT_STATE.md (CS) o a
uno de los dos informes adjuntos (hex-ceiling, fila L6b), con el mismo
alcance y el mismo nivel de evidencia. Tu tarea no es revisar esos
resultados, sino si la síntesis los transmite fielmente. El documento no es
premisa. No tienes herramientas: no ejecutes, edites ni navegues.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. TRAZABILIDAD: para cada afirmación de las Secs. 0-3, ¿está en la fuente
   citada? Señala las que no estén, o estén en otra sección, o con otro
   valor.
2. ALCANCE: ¿alguna afirmación pierde un cuantificador de su fuente (clase
   declarada, soporte N_3, s fijo, filas declaradas, subclase n=3
   antipodal, soporte mínimo) o pasa de «en las filas declaradas» a
   «en general»? En particular, la cadena c_0 <= c_strict^iso <= r_in del
   punto 0.2 y su validez fuera de N_3.
3. NIVELES: ¿se presenta algo con un nivel superior al de su fuente
   (PROVED_UNDER_FROZEN_CONTRACT, CONFIRMED_IN_DECLARED_ROWS,
   GAP_PROVED_IN_CLASS, OPEN...)? ¿Algún valor de la tabla de la Sec. 1
   (r_in, c_0, c_0/r_in, c_strict^iso) no coincide con la fuente o es
   aritméticamente incoherente con las unidades declaradas?
4. LECTURAS Y LÍMITES: ¿las «readings» de la Sec. 1 y la Sec. 3 se siguen de
   las filas citadas sin extrapolar? ¿La Sec. 4 cubre lo que la respuesta
   no establece? ¿Hay alguna afirmación sobre universalidad IR, escala
   absoluta o novedad que exceda las fuentes?
5. CONTENIDO PROPIO: una vez aplicadas tus reparaciones, ¿queda una
   respuesta con contenido (qué fija y qué no fija el sustrato), o se
   reduce a nada más que la lista de fuentes?

Hasta 2000 palabras en español. Cada reparación obligatoria debe citar la
frase afectada, la sección de la fuente con la que choca y qué la cerraría.
Distingue aclaración de error. Dictamen global y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente. No exijas resultados
nuevos: la síntesis no los promete.
---
