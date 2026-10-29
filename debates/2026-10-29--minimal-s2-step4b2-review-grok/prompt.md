# Revisión ciega — Step 4b-2 del charter de rigidez mínima s=2

Bytes revisados: commit `7c741df`, certificado `8849e87a…`.
Fecha: 2026-10-29. Autorización del usuario: «permiso concedido, y si, lanza a GRok».
Objetivo: revisión de otra familia del resultado PRELIMINARY de 4b-2 antes de promocionarlo. El
resultado: en la clase `(V4, tetraedro, Pauli)` todo símbolo unitario es `α W_σ` (48 familias);
Q-a `DISTINGUISHABILITY_IMPLIED_IN_CLASS`; cuatro nodos admisibles por símbolo;
`c_0 = c_strict^iso = rho_micro = 1/sqrt(3)` (`RIGIDITY_PROVED_FOR_FROZEN_CLASS`,
`SATURATION_PROVED_FOR_CLASS`).
Resultado esperado: un veredicto por pregunta (descripción de la clase, Q-a, sectores, rigidez,
saturación) y uno global (ACCEPT / ACCEPT_WITH_REPAIRS / REJECT), con reparaciones obligatorias
numeradas G-4B2-NN.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI). Todo lo revisado lo escribió Claude.
Cierre: informe y lectura del autor en `verificacion_autor.md`. La promoción la hace el autor solo
si no queda ninguna objeción obligatoria abierta.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, símbolos de
Laurent unitarios, geometría algebraica real, bases de Gröbner, cuerpos causales). Solo tienes los
documentos adjuntos; no tienes herramientas y no puedes ejecutar código. Los scripts son
argumentos que inspeccionas, no ejecuciones tuyas. No supongas que nada es correcto.

Documento 1: el informe de 4b-2. Documento 2: su certificado. Documento 3: el informe de 4b-1, ya
revisado. Documento 4: el charter (Step 4b-2, Sec. 1 y Sec. 5). Documento 5: el charter
predecesor, con las definiciones de `S_n`, `h_infty`, `c_strict^iso`, `rho_micro`, los criterios
de admisión (Sec. 3) y el lema del vértice (erratum, líneas 24–29). Documento 6: P17
(D'Ariano–Erba–Perinotti), con la Eq. (2) en la p.2.

Comprueba:
1. Parametrización y la identidad `U = α C0 + β S0 + Σ σ_j(γ_j C_j + δ_j S_j)`: convenio de
   signos en `S_−`, biyección lineal, y que cubre toda la clase de 4b-1.
2. Unitariedad: ¿es correcto el sistema reducido R (27 ecuaciones)? ¿Basta la igualdad de bases
   de Gröbner reducidas para la igualdad de ideales? Rehaz a mano la independencia de las
   funciones usadas.
3. Soluciones reales: ¿es completa la deducción de R a las 48 familias? ¿Falta algún caso
   (por ejemplo, un coeficiente nulo)? ¿Es correcto el recuento 2·3·8?
4. Q-a: ¿es la comprobación (i) la Eq. (2) de P17 tal como la lee el charter? ¿Es correcta la
   ruta (ii) por ideales unidad, y el argumento a mano?
5. Nodos: ¿es completo el conjunto de 16 puntos? ¿Es correcta la reducción a cuatro nodos módulo
   `Λ^*`? ¿Son correctos `H_j` y la condición de admisibilidad (cono isótropo, sin inclinación,
   sector completo de dos bandas)?
6. Cuerpo estricto: ¿se aplica el lema del vértice tal como está enunciado? ¿Es correcto
   `h_infty(q) = |q|_1/sqrt(3)` y su mínimo `1/sqrt(3)`? ¿Coinciden `rho_micro` y el convenio de
   unidades?
7. Alcance: ¿alguna frase del informe excede lo certificado o lo demostrado a mano? En particular
   la «Consecuencia» y la relación con P17.

Salida: una tabla por pregunta con su veredicto; una sección por punto; reparaciones obligatorias
G-4B2-NN con ubicación y gravedad (error demostrado, laguna o redacción); un veredicto global. Si
señalas un error, da el cálculo o el contraejemplo. Una sola ronda: declara tus supuestos.
---
