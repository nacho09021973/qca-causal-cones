# Lectura del autor (sesión Claude, claude-opus-5-5), 2026-11-12

Informe: `informe_astra.md` (gpt-6-astra vía `codex exec` sellado,
`COMPLETED`, herramientas `7d111a1`), segunda ronda, base `755f2ba`.
Candidatos: Etapa 1 reparada (SHA256 `0b48e5b0…678a`) y enmienda 5
(SHA256 `bfe04c51…4c84`). Adjunta la primera ronda sin su cabecera de
procedencia (rutas locales); no se adjuntó la lectura del autor.

## Dictámenes

- **Etapa 1 reparada: PASS**, como adaptación relativa de las
  demostraciones generales. Las cuatro objeciones de la primera ronda:
  RESUELTAS. Inventario U1–U15 completo dentro del alcance declarado
  (excluidas la admisibilidad y las comprobaciones de K3).
- **Enmienda 5: REPAIR_REQUIRED.** La sustitución de la Hessiana es
  correcta (identidad de pluriarmonicidad rama a rama; `Q > 0` implica
  Hessiana compleja no degenerada; K3 cumple H2′, rederivado con
  `q_t = c/D`, `q_n > 0`). Falta la dominancia estricta.

## Objeciones nuevas (comprobadas)

1. **Dominancia estricta no declarada (decisiva para la enmienda 5).**
   Correcta: «a simple dominant eigenvalue»
   (`theory/GENERAL_IR_RATE_GATE.md:95`) no excluye otro autovalor de igual
   módulo; las pruebas lo usan. La intención era estricta: los
   diagnósticos exigen `|lambda_2|/|lambda_1| < 1` (`gap_ratio`,
   `scripts/diagnose_general_ir_rate_polyhedra.py:218-219`) y K3 tiene
   salto `e^(2 Phi_*)`. **Reparación: borrador de enmienda 6 (H2″), que
   también acota «no proof changes».**
2. **`Q` no es en general `Hess Phi`.** Correcta como precisión; la
   enmienda 5 solo cita esa identificación para K3, pero conviene decirlo.
   Recogida en la enmienda 6.
3. **Frase de ACSV en la etapa 0(ii) de B1** («ACSV can supply … under
   H2»): debe ser condicional a las obligaciones que el mismo apartado
   deja abiertas. Correcta; afecta a un documento de base, no a esta
   carta. Pendiente de decisión del usuario.
4. **Factores globales en LT §3(c)**: la fórmula abreviada omite
   `e^(-i eta_k.x_*)`, `e^(i eta_k.y_*)`; CA §2 los incluye y prueba su
   cancelación, y la Etapa 1 §5 usa esa versión. Correcta; exposición en
   un documento de base. Pendiente de decisión del usuario.
5. **Diagnósticos no adjuntos: NO_VERIFICADO por el revisor.** Las
   columnas H2 las he comprobado yo en esta sesión (`hess_kappa_logabs`,
   Hessiana real en momento; `gap_ratio`); no es verificación
   independiente.

## Estado

Etapa 1 (Bravais): `PROVED_UNDER_FROZEN_CONTRACT`, autor, con revisión
cruzada PASS tras una ronda de reparación (Codex, dos rondas). Sin
promoción. Enmienda 5 en vigor pero con REPAIR_REQUIRED; enmienda 6 en
borrador.
