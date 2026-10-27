# Envío autorizado de W4 — 2026-10-26

Autorización directa del usuario: «enviala», después de inspeccionar el
paquete preparado y publicado en `85e22e0e987cfd99cba127de2303a872358e769d`.
Autor del registro: Codex. Estado operativo actual: **COMPLETED / ACCEPT_WITH_REPAIRS**.

Se envía la misma entrada sellada, sin cambiar el encargo ni sus seis adjuntos.
SHA256 de la entrada:
`c381322ed9d1b54e4b03bf257509afd1a8e7d33ca8300b0ddf2369790605d35e`.
`inputs.sha256` y `entrada.sha256` pasan antes del lanzamiento. La nota
PREPARED_NOT_SENT del prompt y del informe adjunto describe la preparación
anterior; esta autorización posterior habilita el envío sin reescribirlos.

Herramienta: `revision-ciega` del PATH, en `~/herramientas` commit
`d32e8507c32aefc0acd0721a000eeeb2a261d824`. Modelo solicitado:
`deepseek-v4-pro`, con thinking habilitado y máximo de 32768 tokens de salida.
Tiempo máximo de la llamada: 1800 segundos. Una ronda de contenido, sin
herramientas ni búsqueda, según el encargo sellado.

## Transporte y procedencia

El primer intento falló antes de contactar al proveedor: curl salió con
código 6, `Could not resolve host: api.deepseek.com`. Sus cuatro archivos se
conservan en `intentos/01-dns/`; no produjo informe ni cuenta como una ronda
de revisión. Se reintentó la misma llamada con acceso de red autorizado.

Comando de lanzamiento desde la raíz:

```sh
REVISION_SOLO_ENTRADA=0 REVISION_TIEMPO=1800 \
DEEPSEEK_THINKING=enabled DEEPSEEK_MAX_TOKENS=32768 \
revision-ciega deepseek debates/2026-10-26--w4-spectrum-review-deepseek \
  theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md \
  reports/2026-10-26--w4-spectrum-audit.md \
  scripts/verify_w4_long_wavelength_spectrum.py \
  scripts/verify_w4_spectrum_observables.py \
  scripts/certificate_utils.py \
  scripts/requirements.txt
```

El lanzador conserva el JSON original del proveedor, el log, el estado y el
informe sin editar con su cabecera de procedencia. COMPLETED sólo acredita
una respuesta íntegra del proveedor; no valida sus afirmaciones. La revisión
se contrastará localmente y su alcance no reabre W1–W12.

## Resultado del intento con esfuerzo implícito high

La llamada de 13:15:59 a 13:24:21 UTC llegó al proveedor y terminó con
`finish_reason=length`, código de transporte 0 y estado `INCOMPLETE`.
La API declaró 9912 tokens de entrada y 32768 de generación; los 32768 de
generación fueron razonamiento, con **cero caracteres de informe**. Los
archivos `deepseek.json`, `deepseek.log`, `estado_deepseek.json` y
`parcial_deepseek.txt` de esta carpeta conservan ese intento. No se obtiene
ningún veredicto científico de su razonamiento interno.

## Corrección y reintento autorizado

El usuario pidió corregir los fallos recurrentes. Se añadió el control
`DEEPSEEK_REASONING_EFFORT` al lanzador compartido, con validación, procedencia,
diagnóstico de agotamiento sólo en razonamiento y cuatro pruebas nuevas.
Las 41 pruebas completas con backends simulados pasan. Código instalado:
`~/herramientas` commit `16568209771dc898346bd4af0c78ec10530c3b9e`.
El [diagnóstico](../../reports/2026-10-26--review-runner-diagnosis.md) documenta
fuentes oficiales, límites y validación. No se cambiaron defaults globales.

El nuevo intento está en `intentos/03-low/`. Conserva modelo, documentos,
texto sellado, límite de 32768 tokens y 1800 segundos; sólo se fija
`DEEPSEEK_REASONING_EFFORT=low` manteniendo thinking habilitado y se usa
el lanzador corregido con acceso de red autorizado. No hay feedback al
revisor ni una segunda ronda de contenido: se intenta obtener el primer
informe completo. Reducir esfuerzo no garantiza salida ni reserva tokens
para texto, y debe constar al evaluar la revisión.

## Resultado del reintento

El intento `03-low` terminó con `finish_reason=stop` y produjo el
[informe íntegro](intentos/03-low/informe_deepseek.md). El veredicto es
`ACCEPT_WITH_REPAIRS`, con cinco objeciones. La comprobación local y las reparaciones constan en el
[registro](../../reports/2026-10-27--w4-review-objections.md); no se promueve
la evidencia ni se atribuye al revisor la validación de cambios posteriores.
