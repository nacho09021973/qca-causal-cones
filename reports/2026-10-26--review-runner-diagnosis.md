# Diagnóstico y corrección del envío de revisiones

Fecha: 2026-10-26. Autor: Codex. Autorización: envío W4 y posterior petición
del usuario de corregir los fallos recurrentes de los agentes.

## Dos fallos distintos, con evidencia

1. El intento en sandbox falló al resolver `api.deepseek.com`, curl 6. Se
   conservó en `debates/2026-10-26--w4-spectrum-review-deepseek/intentos/01-dns/`.
   Se corrigió el acceso de red mediante el mecanismo de autorización del
   entorno. Repetir dentro del mismo sandbox no habría corregido ese acceso.
2. La llamada con red llegó al modelo `deepseek-v4-pro`, pero acabó con
   `finish_reason=length`: 32768 tokens de generación, todos de razonamiento,
   cero caracteres de contenido final. El resultado se conserva en la raíz
   del expediente W4 como `INCOMPLETE`. La llamada íntegra al proveedor no
   equivale a una revisión íntegra y no ofrece ningún veredicto utilizable.

No se generalizan estos dos casos a todos los proveedores o encargos. El
incidente es reproducible como un caso de contrato del lanzador; no hace falta
repetir una llamada de pago para comprobar que una salida así debe rechazarse.

## Causa de configuración y cambio acotado

El lanzador permitía `thinking` y `max_tokens`, pero no `reasoning_effort`.
La documentación oficial indica que el esfuerzo omitido es high y permite
low/high/max. El límite de salida abarca razonamiento más texto final: no
reserva una parte para el informe. Fuentes consultadas en esta sesión:
[Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/),
[Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion/) y
[semántica explícita del límite de salida](https://api-docs.deepseek.com/api/create-response/).

Corrección en `~/herramientas`, commit
`16568209771dc898346bd4af0c78ec10530c3b9e`:

- `DEEPSEEK_REASONING_EFFORT=low|high|max` se envía y queda en la cabecera.
- Valores inválidos o esfuerzo junto a thinking desactivado se rechazan
  antes de llamar al proveedor.
- La omisión conserva el default de la API: no se rebaja silenciosamente el
  esfuerzo de otras revisiones ni se cambia su presupuesto.
- Si todo el presupuesto se consume en razonamiento sin contenido final,
  se informa de ese motivo y se mantiene INCOMPLETE, sin fabricar un informe.
- No se introducen reintentos automáticos, cambios de modelo o aumentos de
  presupuesto. Cada reintento conserva los diagnósticos anteriores.

El cambio permite seleccionar low para el reintento W4 manteniendo thinking
habilitado y el tope de 32768. Es una reducción explícita del esfuerzo, no
una garantía de respuesta ni de calidad matemática. La autenticación y las
reglas de acceso de red siguen siendo responsabilidad del entorno.

## Validación de implementación

Se prepararon los cuatro archivos cambiados en una carpeta temporal de
pruebas, sin llamar a modelos. La batería completa del repositorio compartido
pasó: **41 pruebas**, incluidas cuatro nuevas para esfuerzo enviado y registrado,
default conservado, combinación inválida sin llamada y agotamiento sólo en
razonamiento sin publicación. Los backends son simulados, con claves ficticias.

Tras aplicar la corrección a la fuente única se compararon byte a byte los
cuatro archivos instalados con los probados. `bash -n` y `git diff --check`+pasan. El código y las pruebas permanecen versionados en `~/herramientas`;
la copia temporal sólo sirvió para probar la modificación antes de instalarla.
No se copió un lanzador operativo dentro de QCA.

Comando reproducible en `~/herramientas`:

```sh
python3 -B -m unittest discover -s tests -v
```

El reintento real de W4 usa exclusivamente `revision-ciega` del PATH. El
registro de envío y su eventual comprobación del autor viven en el expediente
W4; pasar las pruebas del lanzador no certifica el contenido de esa revisión.
