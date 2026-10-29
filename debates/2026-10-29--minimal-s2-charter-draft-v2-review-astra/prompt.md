# Revisión ciega, ronda 2 — borrador v2 del charter de rigidez mínima s=2

Fecha: 2026-10-29. Autorización directa del usuario: «si, segunda ronda y los commit pendientes».
Objetivo: comprobar si el borrador v2 (`theory/MINIMAL_S2_RIGIDITY_GATE.md` en el commit
`e117d2e`, sha256 `6c7594a90c4eb1e2…`) resuelve las 14 reparaciones A-R1-01..14 de la ronda 1 y
no introduce errores nuevos. La v2 añade además una segunda familia de isotropía (F: grupos
transitivos sobre los ocho vértices), por decisión del usuario.
Resultado esperado: un veredicto por reparación (RESUELTA / PARCIAL / NO RESUELTA), los errores
nuevos y un veredicto global READY_TO_FREEZE / FREEZE_WITH_REPAIRS / NOT_READY, con reparaciones
obligatorias numeradas A-R2-NN.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra (familia
OpenAI; el borrador lo escribió Claude). El revisor es el mismo de la ronda 1, en una sesión
sellada y sin memoria de ella, por eso se adjunta su informe anterior.
Cierre: informe y lectura crítica del autor en `verificacion_autor.md`. No autoriza congelar ni
calcular.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`. No se adjunta la lectura del autor de la
ronda 1.
Herramienta: revision-ciega del PATH; ~/herramientas `a32e189`.

---
Responde en español. Eres un revisor independiente de física matemática (paseos cuánticos y QCA
en red, teoría de representaciones de grupos finitos, geometría convexa, geometría algebraica
real). Solo tienes los documentos adjuntos; no tienes herramientas y no puedes ejecutar código.
No supongas que nada es correcto.

Documento 1: borrador v2 de un contrato que debe congelarse ANTES de cualquier cálculo. No
contiene resultados.
Documento 2: el informe de revisión de la ronda 1 sobre la v1, con las reparaciones A-R1-01 a 14.
Documentos 3 a 5: contratos anteriores cuyas definiciones se heredan; el 5 es la cota general
`c_0 <= c_strict^iso`.
Documento 6: auditoría de la fuente P17.
Documento 7: texto extraído de P17 (las fórmulas pueden venir dañadas; el PDF es la autoridad).

Comprueba:
1. Para cada A-R1-NN del Documento 2: ¿la v2 la resuelve? Cita la sección de la v2.
2. Familia F (nueva). ¿Está bien definida? ¿Es compatible con la familia P y con la covarianza
   declarada? ¿Hay solapamientos entre clases de P y de F que puedan contarse dos veces o dar
   conclusiones contradictorias? Comprueba a mano si `D4` en torno a un eje coordenado es
   transitivo sobre los ocho vértices y si existen otros subgrupos de `O` que lo sean. En F,
   si `R` es escalar sobre un subgrupo transitivo, ¿todos los `T_h` son iguales y la clase queda
   vacía? Da el cálculo.
3. Anticipaciones corregidas (Sec. 0). Comprueba la identidad para la cara con desplazamiento
   tangencial. Comprueba el enunciado de A2 con `Q8`.
4. Unidades y red (Sec. 1). ¿Son coherentes la normalización, la red BCC y el valor basal?
5. El nuevo Paso 0.4 sobre el alcance de la cota general, frente al Documento 5: ¿está bien
   planteado? ¿Qué cubre exactamente esa cota respecto a nodos distintos de `k_star = 0`?
6. 4a y 4b-1: leyes de transporte (en especial la conjugación compleja y `h_1 ↔ h_4`), variables
   reales, condiciones de soporte activo y certificados de existencia real (Positivstellensatz o
   SOS). ¿Son viables y suficientes?
7. Salidas por pregunta (Sec. 5), presupuesto y paradas (Sec. 4), revisión (Sec. 6). ¿Algo
   ambiguo, incompleto o que permita leer rigidez general, universalidad o novedad?

Salida: una tabla de A-R1-01..14 con su veredicto y ubicación; una sección por cada punto 2–7;
los errores nuevos (A-R2-NN), cada uno con ubicación y gravedad (error demostrado, laguna o
redacción); y un veredicto global. Si señalas un error, da el cálculo o el contraejemplo. Una
sola ronda: declara tus supuestos en vez de preguntar.
---
