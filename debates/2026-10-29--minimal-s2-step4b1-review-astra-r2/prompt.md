# Revisión ciega, ronda 2 — Step 4b-1 del charter de rigidez mínima s=2

Bytes revisados: commit `4646be5`, certificado `5b0122f1…`.
Fecha: 2026-10-29. Autorización del usuario: «si a todo» (aplicar las reparaciones, segunda ronda,
promoción tras ella y autorización de 4b-2).
Objetivo: comprobar que las reparaciones A-4B1-01..06 de la ronda 1 de Astra están bien aplicadas
en el informe y en el certificado de 4b-1, antes de promocionar el resultado.
Resultado esperado: por cada reparación, RESUELTA / PARCIAL / NO RESUELTA, y un veredicto global
(ACCEPT / ACCEPT_WITH_REPAIRS / REJECT), con objeciones nuevas numeradas A-4B1-R2-NN si las hay.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: astra (familia
OpenAI). Todo lo revisado lo escribió Claude.
Cierre: informe y lectura del autor en `verificacion_autor.md`. La promoción la hace el autor solo
si no queda ninguna objeción obligatoria abierta.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red,
representaciones proyectivas, geometría algebraica real, bases de Gröbner). Solo tienes los
documentos adjuntos; no tienes herramientas y no puedes ejecutar código. Los scripts son
argumentos que inspeccionas, no ejecuciones tuyas. No supongas que nada es correcto.

Documento 1: el informe de 4b-1 reparado (las reparaciones están listadas al final). Documento 2:
el certificado reparado. Documento 3: tu informe de la ronda 1, con las reparaciones A-4B1-01..06.
Documento 4: `verify_irreducible_isotropy_step01.py`, del que el certificado importa el generador
de identidades de unitariedad, la llamada a Gröbner y el símbolo de Pavia (no iba adjunto en la
ronda 1; A-4B1-01). Documento 5: el certificado de la etapa (a). Documento 6: el charter.
Documento 7: utilidades simbólicas. Documento 8: el texto de DEP19 (arXiv:1902.10227). Documento 9: `verify_weyl_dirac_gate.py`, que define `published_symbol` (Pavia), importado por el documento 4.

Comprueba:
1. Cada reparación A-4B1-01..06: ¿está resuelta tal como la pediste?
2. El testigo explícito ahora certificado en el script (`witness_symbol`, `laurent_unitary`,
   `covariant`):
   - ¿es correcto el convenio `T_(x,y,z) = P_x^x P_y^y P_z^z` respecto a `U(q) = Σ_h T_h e^{-iq·h}`?
   - ¿comprueba `laurent_unitary` de verdad `U†U = I` y `UU† = I` como identidades de Laurent?
   - ¿comprueba `covariant` la covarianza de la clase con `ρ` = inclusión?
3. Documento 4: ¿hay algo en `unitarity_equations`, `groebner_is_unit` o en el símbolo de Pavia
   que invalide las vaciedades o el control secundario?
4. Alcance: ¿alguna frase nueva del informe excede lo certificado?

Salida: una tabla de reparaciones con su estado; una sección por punto; objeciones nuevas
A-4B1-R2-NN con ubicación y gravedad (error demostrado, laguna o redacción); un veredicto global.
Si señalas un error, da el cálculo o el contraejemplo. Una sola ronda: declara tus supuestos.
---
