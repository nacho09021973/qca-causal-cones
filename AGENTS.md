# AGENTS.md — qca-causal-cones

Guía de entrada para cualquier agente de IA (Claude Code, Codex, Grok…). Las reglas
globales de todos los repos están en `~/herramientas/REGLAS.md` y también se aplican aquí.

Antes de hacer cualquier trabajo, lee y sigue:

1. `PROJECT_INSTRUCTIONS.md` — alcance, distinciones obligatorias, niveles de evidencia,
   método y disciplina de novedad. Es la norma de trabajo del proyecto.
2. `state/CURRENT_STATE.md` — única fuente de verdad del estado, los gates y lo que está
   autorizado. Si otro fichero lo contradice, gana este.

Antes de investigar cualquier cuestión, lee `biblioteca/INDICE.md` (una línea por PDF, con
etiquetas de materia: `grep -i <tema|palabra> biblioteca/INDICE.md`) y comprueba si hay algún
paper útil. El índice localiza, no prueba: lee el PDF y cita `fichero.pdf p.N`, si no
`[UNVERIFIED]`. Las etiquetas `proposed` las escribió una IA. No edites `INDICE.md` a mano:
edita `scripts/biblioteca_catalog/curated.csv` y regenera con
`python3 ~/herramientas/biblioteca_catalog/build_catalog.py --repo .`. `biblioteca/` está en
`.gitignore`: el índice es local, pero `curated.csv` y `tags.csv` sí se versionan.

Herramientas:

- `/comite`: comité de expertos (motor común en `~/herramientas/skills/comite`); los roles
  de este repo están en `comite/config.toml` y los informes van a `reports/comite/`.
- `sanedrin`: debate adversarial entre modelos de casas distintas.
