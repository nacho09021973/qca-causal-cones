# T3: parada del test de cancelación

Fecha: 2026-09-24. Estado: `STOP_GATE_TRIGGERED / CANCELLATION_TEST_NOT_EXECUTED`.
Prerrequisito T2: completado en
`reports/2026-09-24--two-channel-t2-trace.md`.

## Motivo

El gate congelado en `reports/2026-09-24--h1c-return-kernel-schur-audit.md`,
§7, ordena no buscar simetrías cuando T2 deja \(N^{-6}\) como una cota
gruesa sin término ni coeficiente aislado. Eso es exactamente el resultado
de T2: el techo sólo se localiza en un sandwich auxiliar del funcional
anterior y no se transfiere a ninguna de las diez piezas de la respuesta
actual.

Por tanto no se buscó una cancelación asintótica en ninguno de los tres
niveles:

1. Dentro de \(A_{cP}, A_{cQ}, B_{cPP}, B_{cQQ}\) o \(B_{cPQ}\).
2. Entre piezas de un mismo canal \(L_c\).
3. Entre canales en \(L_++L_-\).

Esto significa `NOT TESTED`, no que se haya probado la ausencia de
cancelaciones. Sin un término firmado identificado, asignarle una paridad,
una simetría o una cancelación sería atribuir estructura a una cota superior.

## Identidades que sí quedan en pie

T1 da, para cada canal, la identidad firmada exacta
\[
L_c=A_{cP}+A_{cQ}+B_{cPP}+B_{cQQ}+B_{cPQ}.
\]
La normalización del POVM da \(L_\varnothing=-L_+-L_-\). Ninguna de
estas identidades implica \(L_+=0\), \(L_-=0\), ni una cancelación
entre los canales. En el control plano de T1, \(L_-=0\) y
\(L_+=L_{\rm plano}\) exactamente; ese límite no decide el orden
\(N^{-6}\) para \(\vartheta\ne0\).

## Decisión

Se cierra la pregunta exploratoria en el límite permitido por la evidencia:
T1 tiene revisión independiente aceptada; T2 muestra que \(N^{-6}\) no
es aún una escala del observable actual; el test de cancelación T3 se
detiene por la regla previa. El resultado no demuestra que el techo sea
un artefacto físico, ni justifica continuar hacia una afirmación de
simetría, H1c o una ley asintótica.

No se ejecutó código ni cálculo numérico. No se modifican los claims físicos,
la realización del modelo, H1c, H1, E0, `POWER_13/2_STABILITY`, E/AdS,
C2/C3, ni el manuscrito plano.
