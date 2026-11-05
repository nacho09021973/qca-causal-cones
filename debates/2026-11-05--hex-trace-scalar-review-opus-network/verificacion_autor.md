# Registro y respuesta del autor: reducción escalar

Fecha: 2026-11-05. Autor: Codex (OpenAI).
Autorización del usuario: «perdon claude», corrigiendo inmediatamente la
petición anterior de que lo hiciera Codex. Encargo: revisión de la
reducción general previamente escrita, no resolver la factibilidad.

## Procedencia y entrega

Herramienta: `revision-ciega opus` del PATH, herramientas
`ce09890a0d5f68a6634f358eff2e477ac5f15ec7`.
Modelo: claude-opus-5-5, esfuerzo high, sesión sellada sin herramientas.
Base local al encargo: `84e22ef16f7af46f93443a60ba013fa9c5fce9d4`.

Primer intento, carpeta `../2026-11-05--hex-trace-scalar-review-opus/`:
FAILED, salida 1, `missing_or_failed_result`; el CLI registró diez
eventos `api_retry` con error `unknown` y sin estado HTTP. No entregó
informe. No es revisión ni rechazo científico.

Reintento en esta carpeta: acceso fuera del sandbox aprobado tras el
fallo; COMPLETED, salida 0, `cli_exit_0`, 10:16:32--10:21:16 UTC.
Entrada sellada SHA256:
`cf8387e841dc3adbdb202891ca088815bd54a18dcdef994dd06dc75e3aed966a`.
Informe fuente SHA256 antes de actualizar la cabecera de estado:
`8791ddb115dd27f912b3c2b2fc17c89561ab1968bb27691e2ea69124f5ce3563`.
Script revisado SHA256:
`a00574f90b6c2191dbb92d20f75b260c3a6f4987b683e97a96c7585717647ce3`.

## Dictamen y comprobación del alcance

PASS en los seis bloques: Hessiano, rejilla y derivada transversal,
familia alineada, divisibilidad doble, soporte por polígonos de Newton,
y límites del verificador y de la conclusión. Ninguna reparación
obligatoria. Claude rederiva los argumentos en el informe; no ejecuta
el código. Es una revisión por un modelo de otra familia, no una revisión
humana ni una ejecución independiente del verificador.

La derivación del cociente sigue restringida a la familia alineada y a
los candidatos promediados por D6. La factibilidad escalar para m>=3
y la saturación universal permanecen OPEN. La revisión no cubre de nuevo
la rigidez matricial heredada de HEX_CEILING ni establece novedad.

## Sugerencias opcionales O1--O9

No se necesita una segunda ronda: no hay reparaciones obligatorias.
Se conserva el cuerpo matemático revisado, sin incorporar extensiones.

- O1--O2: R es la rotación antihoraria de 60 grados, con acción
  (a,b)->(-b,a+b). Las letras reutilizadas en secciones distintas son
  locales a cada sección; no se alteran fórmulas por la observación.
- O3: para los hexágonos alineados, promediar un candidato factible por
  D6 conserva su factibilidad; el recíproco es la inclusión de clases.
  Esta es la justificación de la reducción simétrica, no una hipótesis
  de simetría matricial del walk.
- O4: no se añade otra familia de orientaciones. El informe no afirma
  que solo la familia alineada admita reflexión reticular.
- O5: anularse para todo w en la circunferencia unidad implica identidad
  del polinomio de Laurent en w: al multiplicar por una potencia de w
  se obtiene un polinomio ordinario con infinitas raíces. Así se obtienen
  las identidades de restricción usadas para la divisibilidad.
- O6: no se incorpora el posible refuerzo sin promedio; no hace falta
  para el resultado revisado.
- O7: no se añade un resultado nuevo para S7 en este encargo.
- O8--O9: los ceros dobles comprobados por el código son los de Delta,
  no la divisibilidad de un candidato arbitrario. El signo de la segunda
  derivada en los extremos es débil; no obliga a anularla.

Solo se actualiza la cabecera de estado del informe para enlazar esta
revisión. Entrada e informe bruto del revisor permanecen intactos.
No se modifica CURRENT_STATE, no se promociona el resultado y no se
realiza commit ni push en este encargo.
