- Artefactos formales: `formal/` (Lean 4 + Mathlib; formaliza la cota explícita del Teorema 4.1
  de `papers/ir-corona/ir-corona.tex`, sin `sorry`). Ver `formal/README.md` para qué está probado.
- Regla de cuantificadores (`PROJECT_INSTRUCTIONS.md` §7): antes de resolver se congelan
  dimensión interna, grupo/acción y representación, nodo/sector, e irreducibilidad o minimalidad;
  toda conclusión de rigidez conserva esos cuantificadores.
- Comprobaciones propias:
  1. ¿La afirmación es "para todo par / toda clase" o sólo para los pares declarados?
  2. ¿Un criterio suficiente se presenta como necesario u óptimo?
  3. ¿Qué parte está formalizada en Lean y cuál sólo en papel? No extender el alcance del Lean.
  4. ¿Hay implicaciones que la prosa trata como equivalencias?
