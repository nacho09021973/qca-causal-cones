# Lectura del autor (sesión Claude, claude-opus-5-5), 2026-11-12

Informe: `informe_grok.md` (grok-4.7, `COMPLETED`, herramientas `7d111a1`,
10:10–10:41 UTC), sobre la base `65e1ec4`: contrato, enmiendas 1–3, los
tres informes de las etapas y el manuscrito anonimizado (`ir-corona-v3`).
Una ronda, sin herramientas, sin ejecución de código.

**Dictamen del revisor: etapa 1 PASS; etapa 2 PASS.** Ninguna objeción
fatal ni hipótesis que falte; las diez hipótesis coherentes y cada una
usada donde se dice; el caso del manuscrito cumple H1–H10 (rederivado por
el revisor, incluidas `c_* > 1` y la no colinealidad `e_0`, `R~`).

## Objeciones (todas de exposición)

1. Rama de la raíz del determinante en §6 del informe del término
   principal: aceptada; añadido el argumento para `m <= 2` y la frase de
   que falla para `m >= 3`.
2. Resto `O(|p|^2)` del cono en §2: aceptada; añadida la frase sobre la
   analiticidad.
3. «Integral positiva» en la enmienda 2: aceptada; la enmienda está
   aprobada y no se edita; el informe final ya dice «parte real
   positiva», que es el texto que vale.
4. Frase de la bandera en el lema 1.2: aceptada, añadida.
5. Test de Schur escrito: aceptada, añadido.

Reparaciones aplicadas tras la revisión y no re-revisadas.

## Lo que la revisión no cubre

- NO_VERIFICADO por el revisor, y fuera de la cadena de (T): la relación
  de `I` con la tasa de CJWW, el contraste con ACSV y la inferencia sobre
  el caso tetraédrico (los documentos no se adjuntaron).
- **Errata no detectada por el revisor:** la cláusula «`B - A` ... inside
  `conv F`» del contrato excluye las regiones del propio manuscrito; el
  informe de etapas 0–1 dice que K3 está en la clase. Registrada en
  `theory/GENERAL_IR_RATE_POLYHEDRA_DIAGNOSTIC.md`; ningún paso de la
  prueba usa la cláusula (el revisor tampoco la usa en su verificación).
  Su corrección queda pendiente de decisión del usuario.
- Una sola casa (xAI), una ronda. Novedad no juzgada.
