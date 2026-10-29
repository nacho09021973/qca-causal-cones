# Revisión ciega — Step 4b-1 del charter de rigidez mínima s=2

Fecha: 2026-10-29. Autorización del usuario: «mejor Astra»; «no voy a estar en la oficina, así
que los autorizo ya»; «pero la revisión 4b-1 con Astra sí puedes lanzarla».
Objetivo: revisión de otra familia del resultado PRELIMINARY de 4b-1 (commit `38f462c`;
certificado `5f91feae…`), antes de promocionarlo. El resultado es que, de las cinco clases fieles
de la etapa (a), solo `(V4, tetraedro, Pauli)` es no vacía, y que `O`, `(T, tetraedro)`, `D4` y
`(C4, cara)` son vacías.
Resultado esperado: un veredicto por clase y uno global (ACCEPT / ACCEPT_WITH_REPAIRS / REJECT),
con reparaciones obligatorias numeradas A-4B1-NN.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra (familia
OpenAI). Todo lo revisado lo escribió Claude.
Cierre: informe y lectura del autor en `verificacion_autor.md`. No promociona ni autoriza 4a ni
4b-2; aplicar reparaciones lo decide el usuario.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH; ~/herramientas `a32e189`.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red,
representaciones proyectivas, geometría algebraica real, bases de Gröbner). Solo tienes los
documentos adjuntos; no tienes herramientas y no puedes ejecutar código. Los scripts son
argumentos que inspeccionas, no ejecuciones tuyas. No supongas que nada es correcto.

Documento 1: el informe de 4b-1. Documento 2: su certificado. Documento 3: el certificado de la
etapa (a), del que importa funciones. Documento 4: el informe de la etapa (a), ya revisado por
otra familia. Documento 5: el charter. Documento 6: utilidades simbólicas. Documento 7: el texto
extraído de DEP19 (D'Ariano, Erba y Perinotti, arXiv:1902.10227), cuyo apéndice A.2 da una familia
unitaria s=2 en BCC; las fórmulas pueden venir dañadas.

Comprueba:
1. Parametrización.
   - ¿Es correcto reducir cada clase fiel a `ρ` = inclusión `G ⊂ SO(3)`, absorbiendo la
     conjugación en un cambio de base constante?
   - ¿Es correcta la acción `T_h = a_h I + b_h·σ`, `a ↦ a`, `b ↦ g b` bajo conjugación por el
     levantamiento de espín ½ de `g`, con `g` entera?
   - ¿Hay alguna clase fiel con más de una clase de conjugación de inclusiones que se haya pasado
     por alto, por ejemplo por un automorfismo exterior?
2. Las dos construcciones (relleno de órbitas y covarianza lineal sobre `T_h` libres). ¿Son
   correctas e independientes en un sentido útil? Comprueba el código de `class_symbol` y de
   `class_symbol_linear`, en particular la restricción al espacio fijo del estabilizador.
3. Vaciedad de `O`, `T`, `D4` y `(C4, cara)`. Puedes rehacer a mano alguna. Por ejemplo, busca un
   argumento corto con pocas identidades de unitariedad que lleve a contradicción en `D4` o en
   `(C4, cara)`. ¿Es fiable concluir vaciedad sobre C por una base de Gröbner `[1]` con
   `grevlex` y coeficientes exactos?
4. `(V4, Pauli)`.
   - ¿Basta el punto real de Pavia para `UNITARY_SYMBOLS_EXIST`?
   - ¿Es correcta la comprobación de covarianza de Pavia en `pavia_point`?
   - ¿Qué falta para conocer las componentes de la clase?
   - Compáralo con la familia (A30) de DEP19: ¿cabe la clase `(V4, Pauli)` sin la Eq. (2) dentro
     de (A30) con el unitario `V` libre? ¿Sugiere (A30) símbolos de esta clase que violen la
     Eq. (2)?
5. Alcance: ¿alguna afirmación del informe excede lo certificado? En particular «solo el marco
   de isotropía de P17 es no vacío» y lo que se dice de la clase `C4` y de la cota general.

Salida: una tabla por clase con su veredicto; una sección por punto; reparaciones obligatorias
A-4B1-NN con ubicación y gravedad (error demostrado, laguna o redacción); un veredicto global. Si
señalas un error, da el cálculo o el contraejemplo. Una sola ronda: declara tus supuestos.
---
