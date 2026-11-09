# Lectura del autor de la revisión de M1-B19 (Grok; Gemini sin informe)

Autor: Claude (Anthropic). Base revisada: 6302328 (publicado). Herramienta:
ce09890. Fecha: 2026-11-03.

## Estado de las dos casas

- **Grok** (`grok-4.7`, COMPLETED, 15:46–15:57 UTC, sin llamadas a
  herramienta): dictamen global **REPAIR_REQUIRED**, con una reparación
  obligatoria (enmienda); puntos 1–5 y 7 PASS (1 y 7 con aclaraciones).
  Entrada idéntica a la de Gemini (`entrada_*.txt` sha256 `55928596…`);
  hashes de los ocho documentos en `inputs.sha256`, iguales a 6302328
  (`git diff --quiet 6302328` limpio antes del envío).
- **Gemini** (`gemini-4-argon`): **sin informe**. Cuatro intentos
  (`intento1..4_fallido_402/`) devolvieron `402 RESOURCE_EXHAUSTED`,
  «Your prepayment credits are depleted»: fallo de cuenta, no de modelo;
  no se descendió de modelo. El cuarto intento usó la clave indicada por
  el usuario, que coincide con la de `~/.config/sanedrin/env`. La
  revisión doble que pidió el usuario **no está completa**.

## Verificación propia previa

- Verificador sobre 6302328: 17/17, 10 min 52 s, rc 0 (repetición en esta
  sesión, salida no versionada; mismo resultado que el registrado en el
  informe). Una corrida del autor no es revisión independiente.

## Lectura de cada objeción

1. **A3 usa la forma normal (aclaración de Grok, punto 1).** Aceptada:
   comprobado en el informe B19, l. 41: `g(1) = -i<x_+, A(e) x_+> =
   -i r (e.n)` usa `A(e) = r e.sigma`, que es la forma normal del informe
   hex-ceiling, Sec. 3, Paso 2 (l. 181), consecuencia de nodo e
   isotropía en la clase, no de la rigidez. La frase del informe B19,
   l. 57, «A3 and A4 are consequences of unitarity and rigidity», omite
   esa hipótesis. No cambia ninguna ecuación ni el veredicto: la forma
   normal está en el contrato (Sec. 4, «Unknowns») y en el verificador.
   Reparación textual: añadir «and the normal form».
2. **A4, no eliminación de soluciones, reducción (puntos 2–4).** PASS sin
   objeciones. Grok confirma además que las normales opuestas no añaden
   restricciones (A3 se repite, A4(−n) es el conjugado de A4(n)).
3. **Certificado (punto 5).** PASS en la implicación; Grok no puede
   ejecutar y lo dice. La positividad de los 19 pivotes descansa en la
   corrida exacta fail-closed (dos corridas del autor, mismo resultado);
   no hay comprobación independiente ejecutada por otra familia.
4. **Reparación obligatoria (punto 6): forma del contrato.** Aceptada.
   El informe B19, l. 102, dice «In the contract's form (Sec. 4 (ii))» y
   el docstring de `check_certificate` cita «contract Sec. 4 (ii)»; la
   (ii) congelada exige coeficientes racionales y que el verificador
   expanda los dos lados, y aquí G, d_j y l_j están en QQ(sqrt3) y la
   identidad `-1 = ...` no se construye. Es la misma desviación que el
   usuario señaló antes de enviar.
   Observación propia, comprobada en el contrato (Sec. 4, l. 118–122):
   la forma (i) acepta «a polynomial p in the ideal, given with explicit
   exact cofactors p = sum_i h_i f_i, whose absence of real zeros is
   itself certified exactly», sin restringir el cuerpo. Lo que hace el
   verificador (c_i racionales explícitos; identidad polinómica
   `p = (1,t) G (1,t)^T`; 19 pivotes > 0 exactos en QQ(sqrt3)) encaja en
   la letra de (i), como dice Grok. Queda en cualquier caso «checked
   exactly and quickly»: unos 11 min. Por indicación del usuario, la
   clasificación y el tiempo se fijan con una **enmienda explícita**
   posterior a 86573ca, sin editar el prerregistro.
5. **Cifras impresas, no exigidas (aclaración, punto 7).** Aceptada: el
   `record` de S7 es `True` incondicional (informativo, ya rotulado así),
   y los controles 3×3 no exigen 13 parámetros ni 298 ecuaciones, solo
   pertenencia y anulación. El informe debe decir que esas cifras son
   salida impresa, no comprobaciones.
6. **Nombre `OPEN_AFTER_SINGLETON_LAYER_ANALYSIS` (punto 7).** Se mantiene:
   es el vocabulario promocionado; cambiarlo es decisión del usuario.

## Qué hace falta antes de promocionar (decide el usuario)

- Segunda revisión independiente (Gemini con crédito, u otra familia que
  el usuario autorice).
- Enmienda del contrato: certificado de B19 como forma (i), con lo que
  hace exactamente el verificador, y tiempo de verificación declarado.
- Reparaciones textuales del informe B19 (puntos 1, 4 y 5). El docstring
  de `check_certificate` está en el verificador revisado: tocarlo cambia
  sus bytes y exige nueva revisión; propuesta del autor: no tocarlo y
  dejar constancia en el informe de que la enmienda prevalece sobre esa
  cita.

Nada de lo anterior está aplicado. S19 sigue PRELIMINARY.
