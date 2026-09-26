# Revisión focalizada de la versión reparada: transferencia a `A_{cP}`, `A_{cQ}`

## Decisión solicitada

Revisar únicamente la **versión reparada** de
`reports/2026-09-25--physical-linear-endpoint-transfer-gate.md` (las
reparaciones están marcadas `[rev. 2026-09-25]`). No reconstruir H1c. No
revisar Schur (`SCHUR_STABILITY_PASS`, ya revisado) salvo cómo se usa. No
buscar cancelaciones, simetrías ni observables nuevos; no proponer rutas
nuevas; no abrir L2; no ordenar L1/L2/L3 por importancia.

Toda afirmación que no pueda comprobarse con el material adjunto debe
marcarse `[UNVERIFIED]`.

## Seis puntos a verificar

1. La distinción `w_c^{fis} = E r_c` frente a su versión inclinada
   `w~_c = e^{-ξ_*·(y−y_*)}1_{B_N} w_c^{fis}` es ya correcta y consistente en
   fórmulas, diferencias de Duhamel y tabla final (a `ϑ=0`, `w_+^{fis}=w_N`,
   `w_-^{fis}=0`).
2. La única afirmación fuerte sobre Bob es: no hay `O(N^{-3})` demostrado para
   `ϑ≠0`; la cota disponible es `C_BΘN^{-2}`, con `C_B = 256/(3e²t_*²)`
   (≈21.3, sin redondear a la baja). Atacar expresamente si con el material
   adjunto existe un argumento que sí dé `O(N^{-3})` sin invariancia por
   traslación de `U_N`.
3. La descomposición de `y_N` usa exactamente T1 (14), con Q inicial y
   entradas desde `x_k^{stay}`, `f_{Q,k}`, `(𝕄x)_k`, sin partición inventada ni
   dominancia del último paso; `N_0` y `q` correctos.
4. El informe ya no atribuye `A_{cQ}=O(N^{-6}e^{-K_*N})` al PASS de Schur: con
   lo certificado sólo sale `N^{-5}`, y la mejora adicional depende de sumas
   de la clase de L3.
5. L1, L2 y L3 están formulados correctamente y son los únicos huecos
   identificados; ninguno está formulado con más de lo que exige.
6. La conclusión no dice más que `ENDPOINT_TRANSFER_PARTIAL` en el sentido
   concreto: Alice transfiere `O(N^{-3})` (preliminar); Bob no transfiere
   `O(N^{-3})` para `ϑ≠0`; ninguna conclusión sobre la supervivencia de la
   señal, sobre dominancia ni sobre subdominancia (salvo que `A_{+P}` a `ϑ=0`
   contiene el líder plano).

## Criterio de veredicto

`PASS`, `PASS_WITH_REPAIRS` o `REPAIR_REQUIRED` **sobre la versión reparada**,
con el primer paso que falla (si lo hay) y la condición exacta que lo
desactiva. No convertir una cota preliminar en resultado certificado.
