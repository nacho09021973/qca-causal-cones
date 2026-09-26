# Revisión focalizada: transferencia de extremos planos a `A_{cP}`, `A_{cQ}`

## Decisión solicitada

Revisar únicamente el informe adjunto
`reports/2026-09-25--physical-linear-endpoint-transfer-gate.md`. No revisar
la estabilidad de Schur (ya revisada, `SCHUR_STABILITY_PASS`) salvo para
comprobar cómo se usa; no buscar cancelaciones entre `+` y `-` ni entre
piezas; no proponer simetrías, Wronskianos, scattering ni observables nuevos;
no promover H1/H1c; no proponer rutas nuevas de estimación.

Atacar cuantificadores, constantes, normas, identidades exactas y
alcance. Toda afirmación que no pueda comprobarse con el material adjunto
debe marcarse `[UNVERIFIED]`.

## Cuatro obligaciones

1. **Alice.** Verificar que la identidad exacta
   `f^{T1} = J[c_N b_N ↓ + ε_M s_N b_N χ_M]` (tabla de `M↓`), la igualdad
   `‖s‖_2 = ‖f^{T1}‖_{ℓ²_tilt}` (Parseval) y el resto `c_N` dan
   `‖s‖_2 = O(N^{-3})`, y que de la linealidad de Schur se sigue
   `‖t_j‖_2 = O_{W,Θ}(N^{-3})`.
2. **Bob.** Verificar que (i) para `ϑ=0` la representación
   `⟨r_c,E V_c z⟩ = ⟨F w_c, π_c z⟩`, `w_+ = w_N`, `w_- = 0` es exacta;
   (ii) `‖E V_c‖ ≤ 256/(3e²t_*²) N^{-2}` es correcta; (iii) para `ϑ≠0`
   el material disponible **no** permite probar `‖E r_c‖_{ℓ²_tilt} = O(N^{-3})`.
   Atacar expresamente si existe un argumento con el material adjunto que sí lo
   dé (sin usar invariancia por traslaciones de `U_N`).
3. **Potencias provisionales.** Revisar
   `A_{cP} = O(N^{-5} e^{-K_*N})` y `A_{cQ} = O(N^{-6} e^{-K_*N})`, incluidas
   las tres partes de `x_N` y las cuatro de `y_N`, las cotas de bloque
   usadas y la condición `N ≥ N_0`. No promoverlas: indicar de qué
   ingredientes revisados o no revisados dependen. Revisar también la
   afirmación de §0 (a `ϑ=0`, `A_{+P}` contiene el líder plano, luego no puede
   ser subdominante) y la de §3 (Cauchy–Schwarz da `N^{-6}` para `stay`
   incluso con `‖E r_c‖ = O(N^{-3})`).
4. **Lemas que faltan.** Confirmar o corregir que los huecos son exactamente
   - **L1:** control de `‖r_c‖_{ℓ²(capa)}` (o `sup_y‖r_c(y)‖`) de la referencia
     `r_c = B π_c U_N^N J φ_N`;
   - **L2:** control del término `stay` en P por debajo de `N^{-6}`;
   - **L3:** revisión de las cotas tipo `𝕄_N` para `f_{Q,N}` y `(𝕄_N x)_N`;
   y si falta algún otro. Confirmar también que `FINAL_Q_LEAKAGE_MATRIX_ELEMENT`
   no puede reutilizarse por las cuatro razones que da el informe (§4).

## Criterio de veredicto

Para cada obligación: `PASS`, `PASS_WITH_REPAIRS`, `REPAIR_REQUIRED` u
`OPEN`, con el primer paso que falla (si lo hay) y la condición exacta que
lo desactiva. Veredicto global sobre el estado `ENDPOINT_TRANSFER_PARTIAL`.
No convertir una cota preliminar en resultado certificado.
