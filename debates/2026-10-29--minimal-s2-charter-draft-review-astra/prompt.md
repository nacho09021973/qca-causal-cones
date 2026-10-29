# Revisión ciega — borrador del charter de rigidez mínima s=2

Fecha: 2026-10-29. Autorización directa del usuario: «mandale el borrador a Astra».
Objetivo: revisar adversarialmente el borrador `theory/MINIMAL_S2_RIGIDITY_GATE.md` (DRAFT, sin
commit; sha256 `8541cf728da5baf8…` en `inputs.sha256`) antes de congelarlo como charter. La
revisión cubre si la pregunta, la definición de isotropía, las clases, los pasos, las salidas y
los techos están bien cuantificados y libres de sesgo post-hoc, y si las citas de P17 son
correctas.
Resultado esperado: un veredicto global (READY_TO_FREEZE / FREEZE_WITH_REPAIRS / NOT_READY) y
reparaciones obligatorias numeradas con su ubicación.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra
(familia OpenAI). El borrador y el comité que lo propuso son de la familia Claude.
Cierre: informe del revisor y lectura crítica del autor en `verificacion_autor.md`. No autoriza
congelar el charter ni ejecutar ningún paso: eso lo decide el usuario.
Documentos (`docs.txt`, sha256 en `inputs.sha256`): el borrador, los dos charters predecesores,
la auditoría de fuentes de P17 y el PDF de P17. No se envía el informe del comité
(`reports/comite/comite_decision_002_…`) para no condicionar al revisor.
Herramienta: revision-ciega del PATH; ~/herramientas `a32e189`.

---
Responde en español. Eres un revisor independiente de física matemática (paseos cuánticos y QCA
en red, teoría de representaciones de grupos finitos, geometría convexa). Solo tienes los
documentos adjuntos; no tienes herramientas y no puedes ejecutar código. No supongas que nada es
correcto.

El Documento 1 es el BORRADOR de un contrato que debe congelarse ANTES de hacer ningún cálculo.
No contiene resultados. Tu tarea es decidir si está listo para congelarse. Los Documentos 2 y 3
son contratos anteriores cuyas definiciones hereda. El Documento 4 es una auditoría de la fuente
primaria P17, y el Documento 5 es el texto extraído de P17 (las fórmulas pueden venir dañadas; el
PDF es la autoridad).

Comprueba:
1. Pregunta y cuantificadores. ¿Están fijados antes de calcular la dimensión interna, el grupo y
   su acción, la representación (proyectiva, fiel o no), el soporte, el nodo y el sector, y la
   presencia o ausencia de la Eq. (2) de P17? ¿Queda algún grado de libertad que pueda elegirse
   después de ver resultados?
2. Definición de isotropía (Sec. 2): pares `(G, S_+)` con `G` subgrupo de rotaciones del cubo,
   transitivo sobre un `S_+` de cuatro vértices disjunto de `−S_+`. Compárala con la Definición 1
   de P17. ¿Sobra o falta algo? Por ejemplo: reflexiones, grupos que no estén en `O`, `S_+` con
   otra cardinalidad, o el requisito de fidelidad. ¿Es razonable no exigir fidelidad?
3. Las anticipaciones A1–A4 (Sec. 0), que se declaran post-descubrimiento. Comprueba a mano A1:
   identidad de unitariedad en `ℓ=(0,2,2)` para la partición tetraédrica y en `ℓ=(2,0,0)` para la
   partición en caras. Comprueba A2: la irrep lineal `E` de `2O` es trivial sobre las medias
   vueltas axiales. Comprueba A3: un polinomio de Laurent escalar unimodular en el toro es un
   monomio. Di si alguna es falsa o está mal enunciada. ¿Basta la declaración para neutralizar el
   sesgo post-hoc, o el contrato debería cambiar?
4. Pasos 0′, 0, 4a y 4b. ¿Es correcto el orden? ¿Es exhaustiva y finita la enumeración del
   Paso 0′? En 4a, ¿está bien la lista de equivalencias, y está justificado excluir la
   multiplicación a la izquierda por un unitario local? ¿Separa 4b correctamente «ideal distinto
   de (1)» de «existencia de símbolos unitarios reales»?
5. Salidas y techos (Sec. 5). ¿Son exhaustivas y tienen todas el mismo rango? ¿Hay alguna frase
   que permita leer rigidez general, universalidad o novedad?
6. Citas de P17. Verifica en el Documento 5: Eq. (2) en p.2 y su atribución a las refs. [23]/[31];
   s=1 «trivial» en p.4 citando [24]; Eqs. (12)–(13) en p.4; la imagen de Pauli en la Fig. 1(c) y
   en la Sec. V/Prop. 5; `A_e = 0` en d=3 en pp.6–7. Marca cada una como CORRECTA, INCORRECTA o NO
   VERIFICABLE.
7. Presupuesto, reglas de parada y revisión (Secs. 4 y 6). ¿Son suficientes?

Salida: una sección por punto, con veredicto CORRECTO / REPARAR / ERROR; un veredicto global
READY_TO_FREEZE, FREEZE_WITH_REPAIRS o NOT_READY; y reparaciones obligatorias numeradas
(A-R1-NN), cada una con su ubicación y gravedad (error demostrado, laguna o redacción). Si
señalas un error, da el cálculo o el contraejemplo. Una sola ronda: declara tus supuestos en vez
de preguntar.
---
