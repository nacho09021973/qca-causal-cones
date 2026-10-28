# Re-revisión independiente — adenda de reparación del coste de discriminación (informe del 28-09)

Fecha: 2026-10-28. Autorización directa del usuario: «sigamos con la revisión del coste de discriminación» y elección explícita de «Re-revisar el addendum» (revisión sellada por una casa que no ha visto el informe).
Objetivo: cerrar «versión reparada no revisada de nuevo» (`state/CURRENT_STATE.md`, sección del 2026-10-22). Comprobar que la adenda de 2026-10-22 repara correctamente las tres objeciones y no introduce errores nuevos.
Resultado esperado: veredicto PASS / PASS_WITH_REPAIRS / FAIL por reparación y global.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (xAI, familia distinta de Claude, que escribió el informe y la adenda; Grok no participó en la revisión del 22-10).
Cierre: informe del revisor y lectura crítica del autor en `verificacion_autor.md`. La revisión no promociona ningún gate por sí sola.
Documentos: `reports/2026-09-28--iid-message-discrimination-cost.md` (incluye la adenda al final) y `theory/SCALED_IR_SIGNALING_GATE.md` (contrato de definiciones).
Herramienta: revision-ciega del PATH; ~/herramientas commit `1656820`.

---
Responde en español. Revisión matemática adversarial e independiente, una sola ronda. Tu sesión está sellada: solo tienes los dos documentos adjuntos.

El documento 1 deriva el número de repeticiones independientes necesarias para distinguir dos mensajes con un detector binario fijo en un autómata celular cuántico (CJWW), y una cota uniforme para la clase de una partícula. Las asintóticas de la «corona» (delta_N, el campo libre r_N, las cotas D_B) se HEREDAN como premisas de otro manuscrito: no las revises. El documento 2 es el contrato que fija los objetos.

Una revisión anterior pidió tres reparaciones, aplicadas en la «Adenda de reparación — 2026-10-22» al final del documento 1. El texto original se conserva y la adenda lo sustituye donde lo contradice. Tu encargo es la versión reparada:

1. Reparación 1 (§3, acotación de C): rehaz la derivación de abs(C(theta_N)) <= 8 N^{19/2}(1+10N) a partir de delta_N <= D_B(N) <= 4N^3(1+10N)e^{-K* N} y de la expansión de §3. Comprueba exponentes, constantes, el sentido de cada desigualdad, qué significa «resto relativo eventualmente < 1/2» y si basta. Comprueba que log R_eps(N)/N -> 2K* y (5) con Theta siguen valiendo con C explícito, y si la cota es necesaria o solo suficiente para ello.
2. Reparación 2 (§4, coste por copia): comprueba que log c_N = o(N) es suficiente para conservar la tasa exponencial del coste agregado, y que la nueva redacción no afirma de más ni de menos.
3. Reparación 3 (§5, alcance de (8)): comprueba que la restricción U = U_A ⊕ I_{A^c} (o implementaciones en Fock que preservan el sector de una partícula) es exactamente la que necesita la prueba de (8)–(10), ni más ni menos, y si (9)–(10) y las afirmaciones de §6 siguen siendo coherentes con ella.
4. Busca cualquier otra parte del documento 1 que la adenda deje inconsistente (frases del texto original que dependan de lo retirado, el resumen inicial, §6).
5. Da un veredicto por reparación y global: PASS, PASS_WITH_REPAIRS o FAIL, con reparaciones obligatorias numeradas. Distingue error matemático, laguna de justificación y cuestión de redacción.
Marca como NO VERIFICADO lo que dependa de fuentes que no tienes.
---
