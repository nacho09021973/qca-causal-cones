# Verificación del informe de gpt-6.1-sol (por Claude, 2026-11-04)

Informe: `informe_astra.md` (gpt-6.1-sol vía `codex exec`, `revision-ciega`
@ ce09890). Generación comprobada antes del envío (`OK`, segundo sondeo; el
primero superó 180 s). Dictamen: **REPAIR_REQUIRED**, tres reparaciones
obligatorias; coeficientes de L3 rederivados a mano por el revisor, sin error.

Comprobado:
- Reparación 1: cierto. `P.row_L5a()` registra en `P.CHECKS`
  (`verify_c_across_lattices_gate.py` l. 55, 83–84) y el script sólo evaluaba
  `D.CHECKS`. El padre los incorpora (`n_parent_before`). Además la Parte 3
  imprimía CONFIRMED aunque hubiera fallado una comprobación previa.
- Reparación 2: cierto. El contrato Sec. 4 exige `L3_DISPERSION_COMPLETE` /
  `_OPEN_<reason>` y el script no lo emitía.
- Reparación 3: cierto. La segunda vía no deriva la traza de L5a; la
  comparación A−/B− con L5a depende sólo de la expansión.
- `verify_c_across_lattices_gate.py` no se adjuntó (limitación anotada por el
  revisor, sin atribuir error): omisión de preparación del autor, como en la
  segunda revisión de la traza G1.

Reparaciones aplicadas (versión nueva del verificador, 35/35,
`L3_DISPERSION_COMPLETE`), sin nueva revisión. El bloqueo por prerrequisitos
fallidos no se ha probado con un fallo inyectado.
