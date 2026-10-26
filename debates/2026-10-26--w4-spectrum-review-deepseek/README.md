# Revisión independiente de la interpretación W4

Estado: **PREPARED_NOT_SENT**. Preparada el 2026-10-26 a petición del usuario.
Revisor previsto: DeepSeek, mediante `revision-ciega` del PATH. Familia
distinta de la de Codex, autor de la auditoría. Esto prepara una revisión
independiente; no acredita que haya ocurrido ni sustituye revisión humana.

## Objeto y cierre

El encargo revisa sólo el espectro 1D, fase respecto al vacío, unidades y
observable Z de W4. `prompt.md` fija una ronda y exige derivaciones y
objeciones verificables, no una aprobación del relato. No se solicita un
modelo sucesor, novedad, un resultado tensorial ni reapertura de W1–W12.

Se cierra la ronda con un informe íntegro y una lista finita de objeciones o
con REJECT/INCONCLUSIVE. ACCEPT_WITH_REPAIRS requiere después comprobar las
reparaciones; «respondida» no significa «resuelta». Una respuesta truncada o
con llamadas a herramientas escritas como texto no se considera informe.
No se ha creado ningún informe, archivo de respuesta API ni veredicto externo.

## Archivos y procedencia

- `prompt.md`: instrucciones al revisor; sólo el bloque entre `---` se adjunta.
- `inputs.sha256`: huellas del encargo y sus seis adjuntos, relativos a la raíz.
- `preparar.sh`: comprueba las huellas y arma la entrada, siempre sin envío.
- `entrada_deepseek.txt`: contenido exacto preparado por la herramienta compartida.
- `entrada.sha256`: huella de la entrada preparada, relativa a la raíz.

La entrada conserva los dos espacios de salto de línea Markdown del contrato
congelado. La regla local `.gitattributes` permite esos espacios finales sólo
en `entrada_deepseek.txt`; no se normaliza ni altera el contenido sellado para
satisfacer el control de whitespace.

Herramienta inspeccionada: `~/herramientas`, commit
`d32e8507c32aefc0acd0721a000eeeb2a261d824`,
`revision/revision_ciega.sh` y `lib/encargo.sh`. La preparación acaba antes
de leer claves o invocar al proveedor. No se copia el lanzador al repositorio.

Desde la raíz:

```sh
sha256sum -c debates/2026-10-26--w4-spectrum-review-deepseek/inputs.sha256
bash debates/2026-10-26--w4-spectrum-review-deepseek/preparar.sh
sha256sum -c debates/2026-10-26--w4-spectrum-review-deepseek/entrada.sha256
```

Si cambia cualquier adjunto, no reutilizar esta entrada como si revisara los
bytes nuevos: congelar una versión nueva y conservar las huellas anteriores.
El futuro lanzamiento debe usar los mismos seis adjuntos y comprobar que
coinciden; el comando de preparación no ejecuta esa acción.

Las reglas globales `~/herramientas/REGLAS.md` exigen permiso explícito para
enviar texto a terceros con `revision-ciega`. La autorización actual pide
**preparar** la revisión; el envío queda pendiente. No falta ningún trabajo
local para que el usuario pueda inspeccionar qué se sometería al revisor.
