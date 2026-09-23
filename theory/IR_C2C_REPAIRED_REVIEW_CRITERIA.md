# C2c reparado — criterios de revisión

Fecha: 2026-09-23. Estado: **FROZEN FOR THE REPAIRED OBJECT**.

Este documento no reabre el contrato C2c ni cambia el alcance científico. Fija
el objeto posterior a la reparación interna y separa sus criterios de los del
objeto original `fa9c07f`.

## Objeto

La nota reparada es
`reports/2026-09-22--c2c-structural-scope.md` en el commit `1d33130`, blob
`af44a754f3c79447c507ac778adf6d8a74283efe`, SHA256
`0268d8c869fa1b4666df09327e9ce25c0f545401fd5159286287580a888153a0`.
Debe leerse con `git show 1d33130:reports/2026-09-22--c2c-structural-scope.md`.

El objeto conserva el snapshot científico de entrada `f4f937e` y el contrato
original. §12, FR1–FR3, la lectura de Liu–Chen y el roadmap del 21-09 están
fuera de alcance.

## Reparaciones que deben auditarse

1. **Transferencia lineal.** Verificar (C6a) para los cuatro detectores y que
   la aplicación de D a los lemas (6), (16), (17)–(20) conserva regularidad,
   soportes, fases y órdenes sin suponer `[D,J(n)]=0`.
2. **Transferencia cuadrática.** Verificar las dos cotas ponderadas de L2,
   Cauchy–Schwarz en orden `K^{-13/2}` y el muestreo (23) con D insertado.
   Deben permanecer los cruces `Pi_+ D Pi_-`.
3. **Cuatro espinores.** Comprobar que la representación exacta de C2 y sus
   restos se transfieren a `zeta_M` para los cuatro encoders, sin importar el
   PASS de C2a fuera de `sigma_2/I`.
4. **No anulación.** Rehacer el caso `M=I,D_3` y (C14), con valor `1/6` para
   ambos signos, además de la independencia racional por polos.
5. **Alcance estructural.** Confirmar que la redacción es «a lo sumo ocho
   familias» y que no iguala respuestas finitas ni afirma novedad.
6. **§9.2.** Confirmar que el enunciado queda limitado a multiplicadores
   escalares indicadores `p=1_Omega`, con abiertos no vacíos de `Omega` y su
   complemento, fuente finitamente soportada y no nula. No se admiten por
   inferencia cortes suaves, multiplicadores matriciales o tasas de cola.

## Veredictos y límites

El revisor debe emitir `PASS`, `REPAIR_REQUIRED`, `FAIL` u `OPEN` por fila y
nivel S3, además de C1 y §9.2. Un PASS sólo cubre los dieciséis pares del
walk CJWW (5.15), nodo cero, perfiles, geometría y corte congelados. No
promueve `state/CURRENT_STATE.md`, no reabre C3 ni E/AdS y no establece una
ley para otras clases de QCA.

La revisión debe conservar las salvedades de `IR_C2C_REVIEW_CRITERIA.md`:
ganancia relativa `N^{-1/4}`, régimen asintótico lento, `N_0` no efectivo,
exponente tres propio de `K=sqrt(N)` y `NOVELTY=OPEN`. Quedan prohibidos
`L-L_PP`, el Teorema 4.4, `N=24,40`, simulaciones, cuadraturas y barridos.

La revisión interna de Codex está registrada en
`reports/2026-09-23--c2c-codex-internal-review.md`; no sustituye una revisión
independiente.
