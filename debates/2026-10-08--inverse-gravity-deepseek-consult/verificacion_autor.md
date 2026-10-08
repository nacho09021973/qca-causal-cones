# Lectura crítica de la consulta DeepSeek

Fecha: 2026-10-08. Alcance: evaluar la respuesta recibida, sin implementar
un candidato nuevo ni abrir una batería científica. El informe original
permanece íntegro en [retry-1](retry-1/informe_deepseek.md).

## 1. Resultado aceptado por el revisor

DeepSeek considera válidas, con las hipótesis declaradas, las pruebas de
conservación, referencia fundamental, `2<=gap<=16` en toros admitidos y
radio <=4 para todos los tiempos. No identifica error matemático concreto.
Respalda el rechazo de IG-S1 para el objetivo gapless con propagación z=1.
No se interpreta su respuesta como prueba de imposibilidad general de QCA.

Se comprobó el alcance contra el texto efectivamente enviado y su hash.
La respuesta no contiene una nueva derivación detallada ni ejecución del
script; se registra como una consulta externa completada que acepta el
resultado acotado, no como una replicación experimental o certificación global.

## 2. Las reparaciones de formulación ya estaban presentes

| Petición de DeepSeek | Evidencia en el material enviado | Decisión |
|---|---|---|
| Limitar el gap uniforme a L>=6 múltiplo de 6 | Informe IG-S1, líneas 124–127; contrato §2; certificado menciona toros admitidos | Satisfecha antes de la consulta; no hay reparación nueva |
| Limitar la prueba de soporte a la cancelación D F D† | Informe IG-S1, líneas 149–160 y 174–178; distingue expresamente otras reglas que transporten términos | Satisfecha antes de la consulta; conservar el límite |
| No confundir el intervalo con gap exacto | Informe IG-S1, líneas 11–14; certificado lo declara explícitamente | Conservar |

Referencia de líneas: `reports/2026-10-08--inverse-gravity-dressed-parent.md`
en `7774a89`, sin modificación posterior del informe durante la consulta.

La objeción de que IG-S0 confunde condición suficiente con necesidad física
tampoco identifica una omisión literal: su §2, líneas 40–42 y 59–61, declara
ambas distinciones. Sí queda como pregunta estratégica legítima si la ruta
elegida resulta demasiado exigente. No se rebaja por ello el contrato vigente.

## 3. Sugerencias que sí merecen conservarse

**Ventana de baja energía no vacía.** El puente energía–tick solo tiene
contenido físico si existen excitaciones retenidas. IG-S1 ya muestra que
Lambda<2 contiene únicamente el vacío. Para un futuro contrato, pedir una
demostración de cierre del gap, acceso a los estados y peso observable antes
de interpretar el puente como éxito IR. No basta que la desigualdad se cumpla
en un subespacio donde no hay excitaciones.

**Transporte como prueba separada.** El crecimiento de distancia alcanzada
debe comprobarse con una fuente/detector y tiempos fijados, conservando las
distinciones de soporte, respuesta y velocidad IR. La energía conservada no
lo garantiza. El resultado de IG-S1 ya ofrece el contraejemplo concreto.

**Conservación exacta como elección de ruta.** Una alternativa quasilocal o
efectiva podría estudiarse bajo otro contrato, con errores, tiempos, límites
y estabilidad de referencia definidos previamente. La consulta no demuestra
que esa alternativa produzca dos modos físicos ni Einstein, y no la abre.

## 4. Problemas de las dos propuestas concretas

| Propuesta del revisor | Qué falta o qué inferencia no vale | Estado |
|---|---|---|
| A: defectos móviles con energía «quasilocal» | Su objeto inicial se escribe como suma estrictamente local con conservación exacta; no presenta un operador quasilocal ni una puerta concreta. Transportar defectos no prueba que su energía de creación tienda a cero | `NO_RULE_SPECIFIED / GAP_CLOSURE_UNPROVED` |
| B: parent frustrado no conmutante | No presenta términos, referencia accesible o tick. No conmutación/frustración no implican criticalidad. Una cota inferior `gap>=epsilon(L)` con epsilon→0 no prueba cierre del gap | `NO_RULE_SPECIFIED / GAP_CLOSURE_UNPROVED` |

Las objeciones anteriores son comprobaciones lógicas, no resultados de una
nueva simulación. Por ejemplo, un gap constante 1 satisface `gap>=1/L` para
L>=1, así que esa cota inferior no distingue gapped de gapless.

Para demostrar cierre podría servir, con hipótesis y normalizaciones fijadas,
una secuencia de estados físicos normalizados ortogonales al espacio
fundamental con energía variacional <=epsilon(L)→0: daría una **cota superior**
al primer nivel excitado. Aún faltarían densidad de excitaciones, pesos y
control del estado/límite, de modo que tampoco bastaría para z=1 o gravedad.

De modo semejante, si se conserva el K_0 de IG-S1, cambiar únicamente el
transporte de sus defectos no altera la prueba espectral: sus energías son
el número de R violados y cualquier energía positiva sigue siendo >=2.
Una regla que transporte esos estados podría propagar excitaciones gapped.
Esta observación separa los dos obstáculos y evita promover movilidad a
criticalidad. No se afirma lo mismo de cualquier nueva energía no especificada.

El test propuesto «la norma del conmutador crece con n» tampoco es un
criterio acabado de transporte: un conmutador de operadores de norma 1
está acotado por 2 y no tiene por qué crecer monótonamente. Hace falta
formular alcance de distancias crecientes y visibilidad/error con cuantificadores.

Finalmente, «la frustración no conmutante es la única vía restante» no está
demostrado por una clasificación y se rechaza como conclusión exhaustiva.

## 5. Recomendación depurada y cierre

Conservar dos obligaciones simultáneas: una referencia con excitaciones
controladas de energía arbitrariamente pequeña y una regla estrictamente
causal capaz de transportarlas. Antes de más puertas, exigir un candidato
con operadores concretos y una prueba de criticalidad que no sea una cota
inferior decreciente ni simple movimiento de defectos de coste fijo.

La consulta confirma el alcance del negativo IG-S1, pero no entrega ese
candidato. No se implementan A/B ni se cambian q, pesos o la condición de
conservación para rescatar un intento cerrado. La construcción crítica
sigue `OPEN`. El encargo externo termina con esta lectura y su procedencia.
