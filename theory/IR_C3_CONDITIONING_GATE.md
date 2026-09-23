# C3 — condicionamiento posterior a la proyección IR

Fecha: 2026-09-23. Estado inicial: **AUTHORIZED / NOT_EXECUTED**.

Este gate es la continuación separada de C1/C2/C2c. No sustituye el observable
firmado `Lpp` por el observable condicionado y no reabre C2, C3 de otras líneas,
H1c ni E/AdS.

## Objetos congelados

Se conserva el walk homogéneo CJWW (5.15), nodo cero, dos componentes,
recurso, perfiles, regiones y corte
`P=1_{|p|<=N^{-1/2}}`, `Q=I-P`. Se consideran los cuatro encoders
`M in {I,sigma1,sigma2,sigma3}` y se fija el detector de Bob `M_B=I`,
`E=h_N I`. La elección `M_B=I` es parte del alcance: no se extiende la
asintótica de condicionamiento a detectores de rango uno.

Con `v=U_M phi_N`, `w=P v`, `t=Q v`, `q_N=||t||^2` y
`p0_N=<S^N phi_N,E S^N phi_N>`, se mantienen
\[
L_{PP}=\operatorname{tr}(E S^N P\Delta P S^{-N}),
\qquad
L_{\mathrm{cond}}=\frac{L_{PP}+q_Np0_N}{1-q_N}.
\]

## Obligaciones

1. Derivar la identidad exacta de los estados condicionados y de
   `Lcond`, incluyendo las probabilidades de éxito `1` y `1-q_N`.
2. Usar únicamente la asintótica C1 ya certificada para los cuatro encoders,
   `q_N=D N^{-5/2}(1+O(N^{-1/2}))`, con `D>0`.
3. Probar para `M_B=I` que `p0_N -> p_infty>0` mediante la convergencia
   del recurso y la positividad analítica del recurso Weyl en una bola abierta.
4. Derivar la corrección
   `Lcond-Lpp=D p_infty N^{-5/2}(1+o(1))`.
5. Mantener OPEN cualquier afirmación sobre el término líder de `Lcond`,
   `|Lcond|`, `Lcond-Lpp` frente a `L`, o una interpretación como protocolo
   local. No usar diagnósticos N=24/40 para cerrar ninguna asintótica.

## Veredictos posibles

La ejecución puede producir `C3_PROOF_WRITTEN / REVIEW_PENDING`,
`C3_REPAIR_REQUIRED`, `C3_FAIL` o `C3_INCOMPLETE`. La aceptación final exige
una revisión independiente posterior. Ningún resultado actualiza por sí solo
`state/CURRENT_STATE.md` ni reabre E/AdS.
