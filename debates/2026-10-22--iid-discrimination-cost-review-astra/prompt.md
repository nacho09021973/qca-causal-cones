# Revisión independiente — coste de discriminación con usos independientes (informe del 28-09)

Fecha: 2026-10-22. Autorización directa del usuario: «adelante con 2 y 3, autorizado» (paso 3 = revisión independiente de lo PRELIMINARY, empezando por este informe, que `state/CURRENT_STATE.md` fija como «Next step before new research»).
Objetivo: comprobar la corrección matemática del informe dadas sus premisas declaradas.
Resultado esperado: veredicto PASS / PASS_WITH_REPAIRS / FAIL por sección y reparaciones obligatorias.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra (familia distinta de Claude; el informe procede de una sesión Claude según su rama `claude/endpoint-transfer-partial`).
Cierre: informe del revisor y lectura crítica del autor en `verificacion_autor.md`. La revisión no promociona ningún gate por sí sola.
Documentos: `reports/2026-09-28--iid-message-discrimination-cost.md` y `theory/SCALED_IR_SIGNALING_GATE.md` (contrato de definiciones).
Herramienta: revision-ciega del PATH; ~/herramientas commit `d32e850`.

---
Responde en español. Revisión matemática adversarial e independiente, una sola ronda. Tu sesión está sellada: solo tienes los dos documentos adjuntos.

El documento 1 deriva el número de repeticiones independientes necesarias para distinguir dos mensajes con un detector binario fijo en un autómata celular cuántico (CJWW), y una cota uniforme para la clase de una partícula. Las asintóticas de la «corona» (delta_N, el campo libre r_N, las cotas D_B) se HEREDAN como premisas de otro manuscrito: no las revises; revisa todo lo que el informe deriva a partir de ellas. El documento 2 es el contrato que fija los objetos.

Para cada sección (§2 a §5):
1. Rehaz las derivaciones clave: límite y positividad de p_infty (incluido el argumento de analiticidad real para P_3 y la cota estricta <1); la fórmula del error óptimo (2); las desigualdades de Bhattacharyya/TV (3)–(4) y sus constantes; la expansión de la afinidad y la uniformidad del resto; el resultado (5) con Theta; la segunda vía (6) con chi² y Chebyshev; el caso límite p_0=0; la telescopación (9) y la cota (10).
2. Busca errores de signo, constantes, cuantificadores (uniformidad en N, en theta_N, en los 16 pares), confusión entre error medio y error por bit, y usos de las premisas fuera de su alcance (p. ej. (8) solo para una partícula).
3. Comprueba que las afirmaciones de alcance (lo que NO se demuestra, §4 y §6) son correctas y suficientes, y señala cualquier sobreafirmación.
4. Da un veredicto por sección y global: PASS, PASS_WITH_REPAIRS o FAIL, con las reparaciones obligatorias numeradas. Distingue error matemático, laguna de justificación y cuestión de redacción.
Marca como NO VERIFICADO lo que dependa de fuentes que no tienes.
---
