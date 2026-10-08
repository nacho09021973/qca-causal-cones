# Consulta Codex — sin informe completo

Fecha: 2026-10-08. Autorización directa: «prueba con codex».
Estado: `FAILED_NO_COMPLETED_RESPONSE`.

Se usó `revision-ciega astra` del PATH, vía `codex exec` sellado:
modelo solicitado `gpt-6-astra`, esfuerzo high, sin herramientas, web,
plugins, memoria ni documentos adicionales. Commit de `~/herramientas`:
`783f078e04c4a82d48968494714aefbb25acc81b`.

El [encargo](prompt.md) se congeló en `3f944e6`. Una ronda sustantiva,
máximo dos intentos operativos, 600 segundos por intento. El input SHA256
`6b855e7e0d9a60a0ab156c70db2468e01fc51ccecfe5f1379b283142abbbbe30`
coincide con Grok y DeepSeek: mismas preguntas y documentos científicos.
No se adjuntó la respuesta de DeepSeek ni la evaluación del autor.

| Intento | Resultado | Estado retenido |
|---|---|---|
| Inicial | El cliente del CLI no pudo iniciar por sistema de archivos de solo lectura; salida 1, `cli_exit_1` | [estado](estado_astra.json), [log](astra.log) |
| Reintento autorizado fuera del sandbox | Venció el timeout de 600 s sin producir informe; salida 124, `cli_exit_124`; 09:05:50–09:15:51 UTC | [estado](retry-1/estado_astra.json), [log](retry-1/astra.log) |

Se conservan entradas exactas, logs y estados. No existe `informe_astra.md`
ni se generaron archivos `parcial_astra.txt`; no se recibió texto final.
No se determina a partir del timeout la causa interna de falta de respuesta.
No hay aceptación, objeción ni recomendación atribuible a Codex.

Codex pertenece a la misma familia que el autor-agente: incluso una respuesta
completa habría sido una revisión adicional, no verificación independiente
según las reglas del proyecto. Este intento fallido no aumenta el número
de revisiones completadas. DeepSeek sigue siendo la única consulta con
informe completo; no se modifican IG-S1, sus evidencias ni la ruta crítica OPEN.
El encargo acotado termina sin otra ronda ni cambios al lanzador.
