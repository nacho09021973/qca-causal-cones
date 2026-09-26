# Solicitud de revisión matemática a DeepSeek

Fecha: 2026-09-25. Solicitada expresamente por el usuario.
Estado: NOT_INVOKED / API_CREDENTIAL_REQUIRED.

Revisar el expediente de
[preguntas de revisión](2026-09-24--schur-physical-bridge-review-request.md),
sustituyendo el revisor allí nombrado por DeepSeek. El autor de la prueba
es Codex (OpenAI); la revisión debe proceder de DeepSeek y registrar el
identificador exacto del modelo devuelto por el servicio.

Entradas que deberán adjuntarse:

- reports/2026-09-24--schur-stability-physical-transfer.md, versión actual.
- reports/2026-09-24--two-channel-t1-exact-signed-pq.md, definiciones de T1.
- papers/ir-corona/ir-corona.tex, perfiles y pruebas del símbolo inclinado.
- El cuestionario enlazado arriba, sin tomar sus afirmaciones como premisas.

Emitir dictámenes separados para estabilidad Schur, extremos físicos
actuales, error del propagador, reducción firmada y alcance de las
conclusiones. Atacar especialmente la cota del extremo de Bob derivada
de U_N^N J phi_N y la compresión con P extendido por cero fuera de W.
PASS, REPAIR_REQUIRED u OPEN deben ir acompañados de su justificación.

No sustituir silenciosamente DeepSeek por otro proveedor. Tampoco contar
un fallo de acceso, un turno vacío o un resumen de la prueba como aceptación.
El modelo local deepseek-coder:6.7b-instruct no se utilizará como certificación
de este expediente: la documentación del wrapper ya lo excluye para deliberar.
Cuando esté configurado el acceso, registrar hashes de todas las entradas
efectivamente enviadas y conservar íntegra la respuesta recibida.
