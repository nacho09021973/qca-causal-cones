# Revisión independiente (casa Grok) de M1, etapa A y M1-B13 (soporte de 13 puntos)

Autorización explícita del usuario (2026-11-03): «Mi decisión: revisión
independiente de la etapa A antes de iniciar M1-B19», con cuatro puntos a
comprobar; permiso de envío: «si: enviaselo a los dos a Gemini y a Grok»
(2026-11-03). Autoriza el envío externo a xAI (Grok) y a Google (Gemini),
encargos gemelos con entrada idéntica; no autoriza publicación ni
promoción. Autor: Claude (Anthropic). Base: 8abca3c (local). Herramienta:
ce09890. Una revisión por casa, una ronda. Hashes en `inputs.sha256`.

Comprobación previa (regla de los tres puntos). Sabido: rigidez en rectas
normales y T2 de soporte mínimo (promocionados); la etapa A da A1, A2 y
PROVED_FOR_S13, PRELIMINARY, verificador 12/12. Pregunta: ¿la implicación
matemática es correcta en los cuatro puntos del usuario? Cierre: PASS en
ambas casas → registrar validación, push y pasar a M1-B19;
REPAIR_REQUIRED → reparar; si una objeción invalida la reducción de S13,
el veredicto vuelve a OPEN y S13 pasa al solver con su presupuesto.

---
Revisa de forma adversarial e independiente el informe
2026-11-03--hex-supremum.md (etapa A y M1-B13 del contrato
HEX_SUPREMUM_GATE.md), escrito por Claude (Anthropic), y su verificador
verify_hex_supremum_gate.py. Se adjuntan, como fuentes ya revisadas y
promocionadas, el informe y el verificador del gate padre (hex-ceiling) y
su contrato. El informe no es premisa: comprueba cada paso. No tienes
herramientas: no ejecutes, edites ni navegues.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. LEMA A1. ¿La rigidez de saturación a lo largo de una normal de cara
   (informe hex-ceiling, Sec. 3, Paso 1) implica realmente que la suma de
   coeficientes de cada capa intermedia es cero, sin hipótesis adicionales
   sobre el soporte? Comprueba en particular que las proyecciones caen en
   una malla uniforme con el nivel extremo r = N·delta entero, y que una
   capa de un solo punto de C ∩ Λ fuerza ese coeficiente a cero.
2. GEOMETRÍA DE S13. ¿El hexágono cerrado de vértice g1+g2 tiene
   exactamente 13 puntos de red? ¿Las tres normales de cara identifican
   exactamente los seis puntos del anillo interior como capas de un solo
   punto (niveles ±2 delta), y su eliminación deja solo {0} ∪ vértices?
   ¿Es correcta la segunda vía del verificador (resolución exacta de las
   ecuaciones de capa con coeficientes genéricos)?
3. APLICABILIDAD DE T2. ¿La exclusión del soporte mínimo (T2) vale para la
   clase ampliada W_hex^sym, sin usar la factorización moneda–
   desplazamiento ni la red? ¿Es legítima la semejanza (rotación de -30°
   conjunta del espacio y de la esfera de Bloch, y escala) que lleva los
   vértices de S13 a los de T2, conservando la forma normal
   A(n) = r n·sigma? ¿Codifica check_T2_minimal la geometría en abstracto?
4. LEMA A2. Comprueba especialmente la unicidad de 2v = h − h' con
   h, h' ∈ C: ¿qué propiedad de extremalidad y de simetría central se usa,
   y vale para todo soporte con C hexágono regular centrado? (A2 no se usa
   para S13; se registra para S19.)
5. ALCANCE Y NIVELES. ¿Los veredictos (M1-A
   OPEN_AFTER_SINGLETON_LAYER_ANALYSIS, M1-B13 PROVED_FOR_S13, HX2
   CONFIRMED_FOR_S13) se corresponden con lo demostrado, sin extenderse a
   S19, a soportes mayores ni a s > 2? ¿Dice el informe lo que el
   verificador no certifica?

Hasta 1800 palabras en español. Cada reparación obligatoria debe citar la
frase o la línea afectada, por qué falla y qué la cerraría. Distingue
aclaración de error. Dictamen global y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente. No exijas resultados nuevos (S19 no
está en el alcance).
---
