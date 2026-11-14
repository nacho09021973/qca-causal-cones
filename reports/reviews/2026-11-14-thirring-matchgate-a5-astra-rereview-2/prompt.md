# Segunda re-revisión acotada: R2 del gate A5

Autorización: usuario «si, re-revisión y push» (2026-11-14). Envío a
OpenAI (Astra), sin publicación ni promoción automática. Autor: Claude
(Opus 5.5); revisor: Astra (OpenAI), otra familia. Herramientas:
~/herramientas 2a7342b. Astra generó el mismo día (re-revisión anterior
archivada en `e3413e3`). Texto re-revisado:
reports/2026-11-14--thirring-matchgate-a5.md en `030e585`.

Objetivo: decidir si R2 queda resuelta. Resultado esperado: dictamen sobre
R2 y global. Máximo: una ronda. Cierre: PASS → listo para que el usuario
decida si promociona (no autorizado por este encargo); otro dictamen →
nueva decisión del usuario.

---
Re-revisa solo la reparación R2 del informe adjunto
2026-11-14--thirring-matchgate-a5.md, escrito por Claude (Anthropic). Se
adjunta tu re-revisión anterior, que dio R1, R3, R4 y R5 por PASS y pidió
completar R2 en cuatro puntos. No tienes herramientas: no ejecutes, edites
ni navegues. No reabras lo ya aprobado salvo que las ediciones lo afecten.

Dictámenes PASS / REPAIR_REQUIRED / OPEN:

1. ORIENTACIÓN. ¿Fija la orientación de cada par (paquete inicialmente a
   la derecha primero) el signo del denominador, de modo que
   sign(t_pq - t_rs) = sign(E)?
2. EMPATES. ¿Es correcta y explícita la regla para eventos con igual t
   (intercambiar repetidamente el menor par pendiente entre los que ocupan
   slots adyacentes)? ¿Preserva adyacencia, termina, intercambia cada par
   una vez y trata bien pares que coinciden en puntos distintos al mismo
   t? Pruébala con tu ejemplo K = (3/4, -3/4, 0), x = (3/5, -3/5, 0).
3. CUERPO DE ALPHA. ¿Es correcta la nueva redacción?
4. COSTES. ¿Están poly(n) y poly(n, m) bien expresados y distinguidos del
   modelo de Jozsa-Miyake?
5. EDICIONES. ¿Recogen el encabezado y la Sec. 3 estos cambios sin
   introducir errores nuevos?

Hasta 700 palabras en español. Dictamen global y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
