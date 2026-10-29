# Revisión ciega — borrador v1 del charter de rigidez con masa

Bytes revisados: commit `afc2b64`.
Fecha: 2026-10-29. Autorización del usuario: «manda la revision de masa, ya tengo datos en astra,
asi que se lo puedes lanzar a ella».
Objetivo: revisión de otra familia del borrador antes de congelarlo como preregistro.
Resultado esperado: READY / READY_WITH_REPAIRS / NOT_READY, con reparaciones obligatorias
numeradas A-M-NN, y un veredicto sobre cada anticipación C1–C5 (correcta / incorrecta /
incompleta), con el cálculo o el contraejemplo.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra (familia
OpenAI). Todo lo revisado lo escribió Claude.
Cierre: informe y lectura del autor en `verificacion_autor.md`. Congelar lo decide el usuario.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, símbolos de
Laurent unitarios, representaciones proyectivas, dispersión de sectores con masa, cuerpos
causales). Solo tienes los documentos adjuntos; no tienes herramientas y no puedes ejecutar
código. No supongas que nada es correcto.

Documento 1: el borrador del charter con masa. Documento 2: el estado canónico del repo
(`CURRENT_STATE`; las secciones relevantes son la 5, resultados con masa en la familia de Dirac
estándar, y las entradas del 2026-10-29). Documento 3: la nota de las tres velocidades.
Documento 4: el contraejemplo s=4 sin masa, en la misma clase de simetría que el borrador
declara. Documento 5: el certificado de la puerta Weyl/Dirac, con la familia de Dirac estándar y
su soporte con masa. Documento 6: el charter predecesor con las definiciones (`S_n`, `h_infty`,
`c_strict^iso`, `rho_micro`, lema del vértice). Documento 7: el charter de la cota general
`c_0 <= c_strict^iso`, que es solo para sectores sin masa.

Comprueba:
1. Definiciones: ¿está bien definido un nodo con masa admisible (sector, rango, aislamiento,
   isotropía de `ω²` a segundo orden, ausencia de término lineal)? ¿Están bien definidas y bien
   separadas las dos extracciones `c_H` y `c_{ω²}`, y el caso `NO_DIRAC_FORM`? ¿Es `M` un
   parámetro de masa adecuado para comparar símbolos?
2. Anticipaciones C1–C5, una por una. En particular C2 (lema de Schur en nodos invariantes: ¿es
   correcto, y es correcto el conmutante de `σ_i ⊗ I_2`?) y C3 (¿se aplica el lema del vértice a
   la familia de Dirac estándar con término on-site?).
3. Clase: ¿es coherente declarar el soporte `N_3 ∪ {0}` con `T_0` libre y la covarianza incluida
   en `h = 0`? ¿Qué cambia respecto del soporte sin término on-site para `c_strict^iso`?
4. Preguntas QM-0..QM-3 y sus resultados: ¿son decidibles con la secuencia propuesta? ¿Hay
   preguntas sin resultado o resultados sin pregunta? ¿Es correcto que QM-3 compare con `c_0` del
   límite sin masa y no con `c_strict^iso`? ¿Es suficiente un testigo explícito para
   `MASS_DEFICIT_ADJUSTABLE_WITNESS` tal como está definido?
5. QM-1: ¿tiene sentido una cota `c_X <= c_strict^iso` para sectores con masa, dado que la cota
   probada (documento 7) es solo para conos sin masa? ¿Qué haría falta?
6. Alcance: ¿alguna frase promete más de lo que el charter puede decidir, en particular sobre la
   pregunta A (universalidad entre especies)?

Salida: veredicto global; tabla C1–C5; una sección por punto; reparaciones obligatorias A-M-NN
con ubicación y gravedad (error demostrado, laguna o redacción). Una sola ronda: declara tus
supuestos.
---
