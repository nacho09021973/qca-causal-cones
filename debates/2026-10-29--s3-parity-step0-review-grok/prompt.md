# Revisión ciega — Step 0 del charter s=3 (lema de paridad del determinante)

Bytes revisados: commit `HEAD_PLACEHOLDER`.
Fecha: 2026-10-29. Autorización del usuario: «si, manda s=3 a Grok».
Objetivo: revisión de otra familia del resultado PRELIMINARY del paso 0, antes de promocionarlo.
Resultado: en las familias P y F, con `s = 3`, soporte `N_3` y sin término on-site, toda clase es
`EMPTY_CLASS` para toda `R` proyectiva unitaria; desenlace de la unión
`S3_VACUOUS_IN_DECLARED_FAMILIES`.
Resultado esperado: ACCEPT / ACCEPT_WITH_REPAIRS / REJECT, con reparaciones obligatorias numeradas
G-S3P-NN.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI). Todo lo revisado lo escribió Claude. Tú propusiste el lema en la revisión del borrador
(G-S3-01): revísalo como si no lo conocieras.
Cierre: informe y lectura del autor en `verificacion_autor.md`. Promocionar lo decide el autor
solo si no queda ninguna objeción obligatoria abierta.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, polinomios
de Laurent, representaciones proyectivas). Solo tienes los documentos adjuntos; no tienes
herramientas y no puedes ejecutar código. Los scripts son argumentos que inspeccionas, no
ejecuciones tuyas. No supongas que nada es correcto.

Documento 1: el informe del paso 0. Documento 2: su certificado. Documento 3: el charter s=3
congelado. Documento 4: el certificado de la etapa (a) de s=2, del que se importan los grupos.
Documento 5: el certificado Weyl/Dirac, del que se importan los símbolos de Pavia. Documento 6: el
charter s=2 (A3 y las familias).

Comprueba:
1. Lema 1 (paridad): ¿correcto y completo? ¿La expansión genérica del certificado lo comprueba de
   verdad (64 exponentes `{±1,±3}^3`)?
2. Lema 2 (un polinomio de Laurent unimodular en el toro es un monomio): ¿es correcta la prueba
   del exponente extremal, en general y no solo en el soporte del lema 1? ¿Qué comprueba
   realmente el certificado?
3. Lema 3: ¿es correcto `det U(gk) = det U(k)` con `R` proyectiva, y la condición `g^T m = m`
   con el convenio de Fourier del charter?
4. Espacios fijos comunes de los cinco grupos: ¿son correctos? ¿Reconstruye el certificado los
   grupos correctos (en particular el `C4` de cara)?
5. Controles negativo y positivo: ¿son adecuados?
6. Alcance: ¿alguna frase excede lo demostrado? En particular la extensión a `s` impar, que el
   informe no afirma.

Salida: veredicto global; una sección por punto; reparaciones G-S3P-NN con ubicación y gravedad
(error demostrado, laguna o redacción). Si señalas un error, da el cálculo o el contraejemplo. Una
sola ronda: declara tus supuestos.
---
