# Revisión ciega, ronda 2 — borrador v2 del charter de rigidez con masa

Bytes revisados: commit `HEAD_PLACEHOLDER`.
Fecha: 2026-10-29. Autorización del usuario: «masa a segunda ronda».
Objetivo: comprobar que el v2 aplica bien las reparaciones A-M-01..13 de la ronda 1 y que se puede
congelar como preregistro.
Resultado esperado: READY / READY_WITH_REPAIRS / NOT_READY; por cada reparación de la ronda 1,
RESUELTA / PARCIAL / NO RESUELTA; objeciones nuevas numeradas A-M-R2-NN.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra (familia
OpenAI). Todo lo revisado lo escribió Claude, salvo la familia explícita de C4, que procede de tu
ronda 1 y no está certificada.
Cierre: informe y lectura del autor en `verificacion_autor.md`. Congelar lo decide el usuario.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, símbolos de
Laurent unitarios, dispersión de sectores con masa, cuerpos causales). Solo tienes los documentos
adjuntos; no tienes herramientas y no puedes ejecutar código. No supongas que nada es correcto.

Documento 1: el borrador v2. Documento 2: tu informe de la ronda 1. Documento 3: la lectura del
autor de esa ronda. Documentos 4–6: la nota de las tres velocidades, el contraejemplo s=4 sin masa
y el certificado Weyl/Dirac (familia de Dirac estándar).

Comprueba:
1. Cada reparación A-M-01..13: ¿resuelta?
2. La definición de `c_H` (logaritmo espectral en la base microscópica fija, forma de Dirac con
   relaciones de Clifford): ¿elimina la ambigüedad que señalaste? ¿Es correcto el convenio de
   signo de `β`?
3. La división de QM-2 en QM-2a y QM-2b, y la definición de familia admisible para QM-3: ¿son
   correctas y decidibles?
4. La etapa (a): ¿basta lo que lista para decidir QM-0, QM-1 para `H`, QM-2a, QM-2b y QM-3 en la
   familia, si todo pasa? ¿Falta algo que el certificado deba comprobar?
5. C4′ (cota `c_{ω²} < c_strict^iso` dentro de la familia): ¿correcta?
6. Alcance: ¿alguna frase promete más de lo que el charter puede decidir?

Salida: veredicto global; tabla de reparaciones; una sección por punto; objeciones nuevas
A-M-R2-NN con ubicación y gravedad (error demostrado, laguna o redacción). Una sola ronda: declara
tus supuestos.
---
