# Revisión ciega, ronda 3 — borrador v3 del charter de rigidez mínima s=2

Fecha: 2026-10-29. Autorización directa del usuario: «si, tercera ronda con Astra».
Objetivo: comprobar si el borrador v3 (`theory/MINIMAL_S2_RIGIDITY_GATE.md` en el commit
`8d8802a`, sha256 `b24ca44049589305…`) resuelve las seis lagunas A-R2-01..06 de la ronda 2 sin
introducir errores. También se pide confirmar que siguen resueltas las reparaciones de la
ronda 1.
La v3 aplica además dos decisiones del usuario: se mantiene la clase `C4` sobre una cara, con
contraejemplo admitido en ambos sentidos donde la cota general no esté certificada, y Q-a se
pregunta solo sobre símbolos con al menos un nodo admisible.
Resultado esperado: veredicto por laguna (RESUELTA / PARCIAL / NO RESUELTA), errores nuevos
A-R3-NN y un veredicto global READY_TO_FREEZE / FREEZE_WITH_REPAIRS / NOT_READY.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra
(familia OpenAI). Las sesiones son selladas y no recuerdan las rondas anteriores, por eso se
adjuntan los informes de las rondas 1 y 2. El borrador lo escribió Claude.
Cierre: informe y lectura crítica del autor en `verificacion_autor.md`. No autoriza congelar ni
calcular.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`. No se adjuntan las lecturas del autor.
Herramienta: revision-ciega del PATH; ~/herramientas `a32e189`.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, grupos
finitos, geometría convexa, geometría algebraica real). Solo tienes los documentos adjuntos; no
tienes herramientas y no puedes ejecutar código. No supongas que nada es correcto.

Documento 1: borrador v3 de un contrato que debe congelarse ANTES de cualquier cálculo. No
contiene resultados.
Documento 2: informe de revisión de la ronda 2 (sobre la v2), con las lagunas A-R2-01..06.
Documento 3: informe de la ronda 1 (sobre la v1), con A-R1-01..14.
Documentos 4 y 5: contratos predecesores; el 5 es la cota general `c_0 <= c_strict^iso`.
Documento 6: texto extraído de P17.

Comprueba:
1. Para cada A-R2-NN: ¿la v3 la resuelve? Cita la sección.
2. La salida principal con dirección (`..._BELOW` / `..._ABOVE`) y la regla de «conflicto»
   cuando aparece `c_0 > c_strict^iso` dentro de una clase con cota certificada. ¿Es coherente
   con el Documento 5? ¿Puede leerse como permiso para relajar la cota?
3. Paso 0.4: la condición `g^{-1}k_star − k_star ∈ Λ^*` para todo `g ∈ D2`, y la fórmula de
   `Λ^*` (Sec. 1). Comprueba la fórmula de la red recíproca con la convención `e^{-ik.h}`.
4. Q-a restringida a símbolos con nodo admisible, y leída sobre todo `N_3` en la familia F. ¿Está
   bien definido el testigo de refutación?
5. La fila de saturación separada (∀ / ∃) y el resto de la Sec. 5: ¿son exhaustivas y
   coherentes las etapas de cierre?
6. Anticipaciones A5–A8 (Sec. 0). Están marcadas como derivaciones del revisor sin verificar.
   ¿Es correcta la forma de registrarlas? ¿Alguna es falsa?
7. ¿Quedan ambigüedades que impidan congelar? Distingue lo que bloquea de lo que puede
   resolverse en la ejecución.

Salida: una tabla de A-R2-01..06; una sección por cada punto 2–7; errores nuevos A-R3-NN con
ubicación y gravedad (error demostrado, laguna o redacción); veredicto global. Si señalas un
error, da el cálculo. Una sola ronda: declara tus supuestos en vez de preguntar.
---
