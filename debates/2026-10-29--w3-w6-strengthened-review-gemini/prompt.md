# Encargo: certificados reforzados W3/W5/W6 y reparaciones W4

Estado operativo: SENT 2026-10-29 tras confirmación del usuario («si a las 3 preguntas»). Fecha: 2026-10-29. Autorización del usuario para
preparar el encargo: «si, autorizo a y b». El envío exige otra confirmación expresa.
Revisor previsto: Gemini. Es de familia distinta de los autores (Codex escribió el
refuerzo de W3–W6 y las reparaciones de W4; la reconstrucción tipográfica es de Claude) y
de los revisores anteriores (DeepSeek y Astra en W3–W6; DeepSeek en W4).
Objetivo: comprobar si los certificados reforzados de W3, W5 y W6 (2026-10-26) cumplen las
reparaciones obligatorias de las revisiones del 2026-10-22, y si las reparaciones del
autor de W4 (2026-10-27) resuelven las objeciones W4-R1-01 a 05.
Resultado esperado: veredicto por bloque y global, con reparaciones obligatorias numeradas.
Máximo: una ronda sellada y un reintento operativo si falla el transporte.
Cierre: informe completo y contrastación local de cada objeción en `verificacion_autor.md`.
No promociona evidencia ni reabre W1–W12, que siguen CLOSED_BY_CONTRACT.
Documentos: `docs.txt`, con los sha256 en `inputs.sha256`; todos están en commits y sin
cambios en el árbol de trabajo. Herramienta: `revision-ciega` del PATH, ~/herramientas
`a32e189`. `preparar.sh` solo arma la entrada (`REVISION_SOLO_ENTRADA=1`).

---
Responde en español. Eres un revisor independiente de física matemática (paseos cuánticos y
QCA, fermiones en red, gravedad linealizada). Solo tienes los documentos adjuntos: no tienes
herramientas, no puedes ejecutar código y no has visto el resto del repositorio. Un script es
un argumento que inspeccionas, no la prueba de una ejecución. No supongas que nada es correcto.

Contexto: W3–W6 son gates consecutivos de una construcción de juguete de «geometría dinámica»
acoplada a un paseo cuántico 3D de dos componentes (CJWW, ec. 5.15; `walk2()` en
`verify_directional_saturation.py`). Su línea está cerrada por contrato: tu revisión no la
reabre, solo dice si lo certificado es lo que se afirma. Se adjuntan los contratos congelados,
las dos revisiones del 2026-10-22 (DeepSeek y Astra) con sus reparaciones obligatorias, el
informe de refuerzo del 2026-10-26 y sus certificados.

Bloque A — W3/W5/W6 reforzados.
1. Para cada reparación obligatoria de certificado de las revisiones del 2026-10-22, di si el
   código nuevo la cumple, la cumple en parte o no la cumple, con la función concreta.
2. `tetrad_transport.py`: rehaz la afirmación de que la derivada en g=0 de un producto de
   capas, cada una igual a la identidad en g=0, es la suma de los generadores, y que las dos
   paridades dan el símbolo uniforme a primer orden. Comprueba la extracción de E por traza de
   Pauli de la derivada en momento y si sigue siendo circular (definir E y comprobar su
   definición).
3. W3: ¿se distingue bien el término de campo medio de orden g² de las correlaciones del mismo
   orden, que no se certifican?
4. W5: rehaz `J^2=A`, `JA=J`, la exponencial del kick, la conjugación de Z y la derivada
   `-2 X⊗J`, y `dH_transport/dz = gJ`. ¿Sirve el control con signo contrario?
5. W6: F1 (geometría que no toca la materia a g=eta=0), F5 (nueve corrientes y nueve
   variaciones) y F6 (puerta K). Rehaz el argumento de paridad del calendario de 90 capas, que
   prueba que las anclas de igual paridad forman un matching, y di para qué tamaños de toro
   vale. Los recuentos L=4,6 son controles finitos: ¿se presentan como tales?

Bloque B — reparaciones de W4. Se adjuntan la auditoría de W4, la revisión previa de DeepSeek
(objeciones W4-R1-01 a 05), la comprobación del autor y los dos certificados ya modificados.
6. Para cada objeción W4-R1-NN di si el tratamiento del autor la resuelve, la resuelve en
   parte o no. Revisa especialmente W4-R1-02 (signo de `tan(kappa)/4` en `(pi/2, pi)` y elección
   de rama) y W4-R1-04 (la comprobación de traza añadida y su dependencia de SymPy).
7. ¿Introducen los cambios de los dos scripts W4 algún error o afirmación nueva?

Para ambos bloques:
8. Busca sobreafirmaciones respecto a los techos de cada contrato: onda del métrico, gravitón,
   identidad Ward, tensor conservado, unicidad del calendario, independencia del orden.
9. Separa lo que compruebas a mano, lo que solo inspeccionas en el código y lo que depende de
   una ejecución que no puedes verificar (barridos de 42 y 43 verificadores, sha256).

Salida: una sección por bloque; tabla final (afirmación / SUPPORTED, SUPPORTED_WEAKER o
NOT_SUPPORTED / motivo en una línea); veredicto por bloque y global: ACCEPT,
ACCEPT_WITH_REPAIRS o REJECT. Numera las objeciones como W36-G-NN, con gravedad
(error demostrado, laguna o redacción) y ubicación. Si señalas un error, da el cálculo o el
contraejemplo. Una sola ronda: declara tus supuestos en vez de preguntar.
---
