# Re-revisión sellada acotada: gate S4 de isotropía DEP

Autorización: usuario «si, aplica 1-3 y lanza la re-revisión» (2026-11-17).
Envío a OpenAI (Astra, gpt-6-astra vía codex exec). Autor: Claude (Opus
5.5); revisor: Astra, otra familia. Herramientas ~/herramientas 7d111a1.
Primera revisión: reports/reviews/2026-11-17-s4-dep-isotropy-astra/
(sobre 251c163, archivada ed63258): REPAIR_REQUIRED documental; bloques
1-4 PASS, 5 OPEN (faltaba el diff), 6 REPAIR_REQUIRED. Reparaciones en
929f7f7, 0ec49f3, 6331fa5. Candidato: informe en 6331fa5.

Objetivo: cerrar los bloques 5 y 6. Resultado esperado: dictamen sobre
R1-R3 y bloque 5. Máximo: una ronda. Cierre: PASS → el usuario decide si
promociona (no autorizado aquí).

---
Re-revisión acotada. Se adjuntan: tu revisión anterior (informe_astra.md);
el informe reparado 2026-11-17--s4-dep-isotropy.md; el diff entre las
versiones del verificador usadas en las ejecuciones 1 y 2
(verifier_fdae12c_to_36fb8fd.diff); el verificador actual; y
scripts/README.md (contiene la fe de erratas R1). No tienes herramientas:
no ejecutes, edites ni navegues. No reabras los bloques 1-4 salvo que las
reparaciones introduzcan un error nuevo.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:

A. BLOQUE 5. Con el diff, ¿es el cambio entre las ejecuciones 1 y 2 solo
   un cambio de método (cálculo de conjuntos de ceros) sin cambio de
   expectativas, de tareas C1-C5 ni de la lógica de veredicto?
B. R1. ¿Es aceptable registrar la discrepancia de la cabecera del
   verificador como fe de erratas en el informe y en scripts/README.md,
   sin cambiar los bytes del verificador revisado? ¿Es correcta la
   redacción?
C. R3. ¿Separa ahora el párrafo del veredicto la isotropía certificada de
   la pendiente obtenida aparte, con su procedencia, y nombra el cuerpo de
   soporte estricto como término de comparación? ¿Restringe la
   homogeneidad a la condición (2)?
D. ERRORES NUEVOS. ¿Introducen las reparaciones alguna afirmación nueva no
   sostenida?

Termina con un dictamen global.
---
