# Lectura crítica del autor (Claude Opus 5.5), 2026-10-28

Revisión sellada de la versión reparada de
`reports/2026-09-28--iid-message-discrimination-cost.md`
(sha256 `9838662a64401b1ae5e34f61599d3d3fbd4279096f8a9c1321b1c166b5954e01`,
último commit `262ce03`; base de la rama `research/inverse-gravity-design` en `01fd957`):
- Grok (grok-4.7, CLI sellado como CIRO; `informe_grok.md`): **PASS** global, sin
  reparaciones obligatorias. Una sola ronda, sin reintentos; 0 llamadas a herramienta.
- Herramienta: `revision-ciega`, ~/herramientas `1656820`.
- Grok no participó en la revisión del 2026-10-22 (Astra, Gemini).

| Punto | Veredicto de Grok | Comprobación del autor |
|---|---|---|
| R1. abs(C(θ_N)) ≤ 8N^{19/2}(1+10N) | PASS | Rehecha de forma independiente antes de leer el informe: δ ≤ D_B ≤ 4N³(1+10N)e^{−K*N} está en `papers/ir-corona/ir-corona.tex:462` y `:576`; con abs(ρ_N) < 1/2, abs(C) ≤ 2δ_N N^{13/2}e^{K*N} ≤ 8N^{19/2}(1+10N). Coincide. |
| R1, alcance | La cota es suficiente, no necesaria: (5) con C explícito no la usa; log R_ε/N → 2K* necesita log abs(C) = o(N), con la mitad inferior dada por la separación de cero (premisa de §1, no retirada) | Correcto. Cuestión de redacción; no exige cambio. |
| R2. log c_N = o(N) | PASS | Correcto y bilateral, como dice el texto reparado. |
| R3. U = U_A ⊕ I_{A^c} en el sector de una partícula | PASS; es exactamente lo que necesita el argumento de norma y de bloques (`tex:459-462`) | Concuerda con §5: «toda unitaria U igual a I fuera de A_N». La adenda solo precisa la lectura en Fock. |
| Coherencia del resto (§2, §6, resumen) | Sin incoherencias; el encabezado «sin revisión independiente» es residuo editorial | Aceptado como residuo editorial: la adenda fija el estado y el texto original se conserva por diseño. |

Observaciones no obligatorias que se registran sin aplicar:
- La constante 8 no es aguda: cualquier constante > 4 vale desde algún N.
- El N_* desde el que abs(ρ_N) < 1/2 no es efectivo (ya declarado en §6, punto 5).

Nivel de evidencia: la versión reparada tiene ahora una revisión independiente PASS
(Grok), además de las del 2026-10-22 (Astra PASS_WITH_REPAIRS, Gemini PASS) sobre la
versión original. Las premisas heredadas de la corona siguen fuera del alcance de las
tres revisiones. Esta lectura no promociona ningún gate ni establece una frontera
operacional en c; la actualización de `state/CURRENT_STATE.md` es un paso aparte.
