- Autoridad: `state/CURRENT_STATE.md` (estado y autorizaciones) y `PROJECT_INSTRUCTIONS.md`.
  Registro de gates vigente del frente IR: `CURRENT_STATE.md` §10.1. Autorizaciones generales:
  §7 (sólo punto (3) cartografiado por el usuario) y §8.21 (4B cerrado).
  Pregunta de coexistencia (2026-11-09): extensión interactuante autorizada el 2026-11-06, un
  modelo, código y conjunto de recursos por contrato; cada contrato sigue necesitando decisión
  explícita del usuario.
- Comprobaciones propias:
  1. ¿El paso propuesto figura como autorizado (UNBLOCKED, chartered) en `CURRENT_STATE.md`, o
     requiere una decisión explícita del usuario que aún no existe?
  2. ¿Existe contrato congelado (`theory/*_GATE.md`) con criterios de PASS/FAIL escritos antes
     de la evidencia?
  3. ¿El paso respeta el estado branch-local y no promociona nada a `main`?
  4. ¿Mantiene separados C3, E/AdS (FROZEN) y H1c/E0 (sin cambios)?
  5. ¿Implica commit, push, publicación o barridos numéricos no autorizados?
