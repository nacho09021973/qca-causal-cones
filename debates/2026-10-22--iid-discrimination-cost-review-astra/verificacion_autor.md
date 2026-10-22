# Lectura crítica del autor (Claude Opus 5.5), 2026-10-22

Revisiones selladas del informe `reports/2026-09-28--iid-message-discrimination-cost.md`:
- Astra (gpt-6-astra, vía codex exec): **PASS_WITH_REPAIRS**, con tres reparaciones obligatorias.
- Gemini (`../2026-10-22--iid-discrimination-cost-review-gemini/`): **PASS** sin reparaciones. No detectó ninguna de las tres de Astra.
- Primer intento de ambos: no se envió nada, por un error de formato del encargo (faltaba el `---` de cierre); queda en `lanzamiento_fallido_formato.out`.

| Reparación | Comprobación del autor | Decisión |
|---|---|---|
| R1. La separación de C respecto de cero no implica que esté acotada por arriba; la frase «permanece acotada» no tiene premisa | Se confirma en el texto: §1 solo declara «uniformemente separado de cero». Derivación: δ_N ≤ D_B(N) ≤ 4N³(1+10N)e^{−K*N} (premisa de la tabla, thm:rate (d)); con el resto relativo eventualmente < 1/2, sale abs(C(θ_N)) ≤ 8N^{19/2}(1+10N). Es polinómica, así que log R_ε/N → 2K* se mantiene | aceptada |
| R2. «Sólo si el coste por copia fuese como máximo polinómico» es falso como condición necesaria | log(R c_N)/N = log R/N + log c_N/N; basta log c_N = o(N) (p. ej. c_N = e^{√N}) | aceptada |
| R3. Las unitarias de (8) deben preservar el sector de una partícula (U = U_A ⊕ I_{A^c}) | La prueba descrita en §5 usa bloques de vacío y de una partícula; la lectura amplia en Fock no está cubierta | aceptada como precisión de alcance |

Resultado central sin cambios: R_ε(N) = Θ(δ_N^{−2}) para los dieciséis pares congelados, y la obstrucción necesaria (10) para la clase de una partícula.
Nivel de evidencia: una revisión independiente PASS_WITH_REPAIRS y otra PASS. Reparaciones aplicadas por el autor en una adenda; **la versión reparada no se ha vuelto a revisar**. Las premisas heredadas de la corona no entraban en el encargo.
