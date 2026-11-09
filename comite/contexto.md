qca-causal-cones estudia autómatas celulares cuánticos (QCA) de alcance finito. Pregunta del
proyecto desde el 2026-11-09 (`README.md`, `PROJECT_INSTRUCTIONS.md` §1): ¿admite un mismo QCA de
alcance finito, con una sola regla fija, a la vez computación cuántica universal (un código cuyas
puertas implementa la propia regla, sin control externo de sus partes libre o interactuante, que
componen un conjunto universal, con preparación y lectura declaradas) y un régimen relativista de
baja energía de esa misma regla? Toda afirmación es por código, por conjunto de recursos
(ancillas, medida, geometría) y por elección de parámetros; un negativo para un código no es un
no-go del sustrato. Modelo de trabajo: el QCA de Thirring, `U = F J`.

Líneas heredadas de la pregunta original (la velocidad relativista a partir de la geometría causal
microscópica), válidas en su alcance registrado: `B_infty^*` (c_0 frente a c_strict^iso) y A
(universalidad IR entre especies).

- **Autoridad canónica:** `state/CURRENT_STATE.md` es la única fuente de verdad del estado del
  proyecto, de los gates y de lo que está autorizado. Si otro fichero lo contradice, gana
  `CURRENT_STATE.md`. Reglas del proyecto: `PROJECT_INSTRUCTIONS.md`.
- **Estado branch-local:** el trabajo vive en `research/schur-stability-audit`; `main` no se
  promociona sin decisión explícita.
- **Niveles de evidencia:** ESTABLISHED, SUPPORTED, PRELIMINARY, OPEN, REJECTED
  (`PROJECT_INSTRUCTIONS.md` §4). Toda afirmación no trivial lleva el suyo.
- **Método:** álgebra y geometría exactas antes que ajuste numérico; seguir los seis pasos de
  `PROJECT_INSTRUCTIONS.md` §5 antes de comparar velocidades. Con masa, no identificar `c_IR` con
  `|∇ω(0)|`; distinguir `c_H` y `c_{ω^2}`. `c_IR` (longitud/tiempo) no se compara con una
  frecuencia (1/tiempo) sin una escala espacial, una temporal y el coeficiente adimensional.
- **Gates:** cada paso comprometido tiene un contrato congelado en `theory/*_GATE.md`; un
  resultado pasa por derivación, revisión independiente de otra familia y promoción registrada en
  `CURRENT_STATE.md`. Los resultados negativos son resultados válidos.
- **Límite de las afirmaciones:** sólo lo que declara cada contrato, en su clase declarada. Nada
  de generalidad, universalidad ni novedad sin prueba y auditoría de prior art separadas.
