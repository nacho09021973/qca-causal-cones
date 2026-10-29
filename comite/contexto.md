qca-causal-cones estudia autómatas celulares cuánticos (QCA) de alcance finito, su geometría
causal microscópica, las velocidades espectrales de propagación y su límite relativista de baja
energía. Pregunta central: bajo qué hipótesis estructurales explícitas la velocidad relativista
sin masa `c_0` coincide con la velocidad isótropa asintótica estricta `c_strict^iso` de la misma
dinámica (`B_infty^*`), y por qué especies distintas compartirían un mismo cono IR (A).

- **Autoridad canónica:** `state/CURRENT_STATE.md` es la única fuente de verdad del estado del
  proyecto, de los gates y de lo que está autorizado. Si otro fichero lo contradice, gana
  `CURRENT_STATE.md`. Reglas del proyecto: `PROJECT_INSTRUCTIONS.md`.
- **Estado branch-local:** desde octubre de 2026 el trabajo vive en
  `research/inverse-gravity-design` (antes, `research/b-infinity-post-s4-gate`); `main` no se
  promociona sin decisión explícita. Comprobar la rama activa con `git branch --show-current`.
- **Niveles de evidencia:** ESTABLISHED, SUPPORTED, PRELIMINARY, OPEN, REJECTED
  (`PROJECT_INSTRUCTIONS.md` §4). Toda afirmación no trivial lleva el suyo.
- **Método:** álgebra y geometría exactas antes que ajuste numérico; seguir los seis pasos de
  `PROJECT_INSTRUCTIONS.md` §5 antes de comparar velocidades. Con masa, no identificar `c_IR` con
  `|∇ω(0)|`; distinguir `c_H` y `c_{ω^2}`.
- **Gates:** cada paso comprometido tiene un contrato congelado en `theory/*_GATE.md`; un
  resultado pasa por derivación, revisión independiente y promoción registrada en
  `CURRENT_STATE.md`. Los resultados negativos son resultados válidos.
- **Límite de las afirmaciones:** sólo lo que declara cada contrato, en su clase declarada. Nada
  de generalidad, universalidad ni novedad sin prueba y auditoría de prior art separadas.
