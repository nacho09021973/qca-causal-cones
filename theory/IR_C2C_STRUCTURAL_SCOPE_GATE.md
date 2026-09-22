# C2c — alcance estructural de la compensación espectral

Fecha: 2026-09-22. Estado: **UNBLOCKED / NOT_EXECUTED**.

Este contrato recoge la decisión del usuario de aceptar C2b y redefinir
C2c como un gate de alcance estructural. La tarea de C2c es determinar
hasta dónde se extiende el mecanismo ya demostrado para \(\sigma_2/I\).
No se registra aquí un resultado nuevo ni una extensión ya certificada.

## Provenance y entradas

- [Contrato C1/C2/C3](IR_ATTRIBUTION_C1_C2_C3_GATE.md).
- [Contrato C2a](IR_C2A_OSCILLATORY_TRANSFER_GATE.md),
  [derivación](../reports/2026-09-22--c2a-oscillatory-transfer.md) y
  [revisión](../reports/2026-09-22--c2a-independent-review.md).
- [Contrato C2b](IR_C2B_BLOCK_DECOMPOSITION_GATE.md),
  [candidato](../reports/2026-09-22--c2b-block-decomposition-candidate.md) y
  [revisión independiente](../reports/2026-09-22--c2b-independent-review.md).
- [Manuscrito](../papers/ir-corona/ir-corona.md), convenciones, protocolo
  y Teorema 4.1; [estado vigente](../state/CURRENT_STATE.md), §10.1.

C2b fue un **POST-DISCOVERY VERIFICATION GATE** sobre el commit
`19eb7a383cbb09464e91b64e89f724204e58cccb`. Su revisión es de Codex,
agente `/root`, independiente del autor Claude Opus 5; no se registra como
una revisión adicional de Astra ni como evidencia de diversidad de modelo.
SHA256 del informe aceptado:
`65bab830c6960f2c661ae47d739d90c1ecf8ae06b5f9923383919f76c2b234d5`.

Este contrato fija el alcance de la siguiente auditoría después de conocer
el mecanismo de C2b. No es una preregistración retrospectiva de ese mecanismo
ni de las generalizaciones sugeridas en la discusión. No presupone que el
patrón principal se extienda a todos los pares.

## Estado de partida y objetos congelados

C1 = PASS; C2a = PASS para \(\sigma_2/I\); C2b = PASS para ese par,
con B4_PRIME_PASS registrado aparte; C2c = UNBLOCKED; C3 = SEPARATE;
E/AdS = FROZEN. No se reabre la ley total del observable.

Se conserva el walk homogéneo CJWW (5.15), dos componentes, nodo cero,
recurso \(\phi_N\), perfiles y regiones originales, \(N\ge2\) entero,
\(P=1_{|p|\le N^{-1/2}}I_2\), \(Q=I-P\). Se conservan

\[
a=(U_M-I)\phi_N,\quad r=S^N\phi_N,\quad d=S^Na,
\quad d_P=S^NPa,\quad d_Q=S^NQa,
\]
\[
L_{XY}=\operatorname{tr}(ES^NX\Delta YS^{-N}),\quad
\mathrm{Lin}_N=2\operatorname{Re}\langle r,Ed_P\rangle,\quad
\mathcal Q_N=\langle d_P,Ed_P\rangle.
\]

Los dieciséis pares que deben clasificarse son exactamente

\[
M\in\{I,\sigma_1,\sigma_2,\sigma_3\},\qquad
M_B\in\{I,(I+\sigma_1)/2,(I+\sigma_2)/2,(I+\sigma_3)/2\},
\quad E=h_N\otimes M_B.
\]

Los proyectores internos de Bob no se confunden con \(P\). El encoder
\(M=I\) se conserva como control original; no se identifica con omitir
el encoder. Ningún filtro, detector, perfil o geometría se sustituye.

## Preguntas y obligaciones de alcance

### S1 — qué depende sólo del álgebra

Separar las hipótesis de cada identidad: \(Q=I-P\), linealidad,
ortogonalidad de los proyectores, \(P\phi_N=\phi_N\), unitariedad,
\(E=E^\dagger\), positividad y conmutación con \(S\). Explicitar cuáles
son necesarias en cada paso y cuáles sólo están disponibles en el modelo.
No presentar \([S,P]=0\) como requisito de B1.

### S2 — qué depende de la localidad y del Teorema 4.1

Auditar la extensión de B3 a los dieciséis pares, comprobando para cada
familia la normalización, el soporte de \(a\), \(0\le E\le I\), el
soporte de Bob y la uniformidad de las constantes. Distinguir la
cancelación de amplitudes en la norma localizada por \(E^{1/2}\) de una
afirmación en norma global. La cota causal se aplica al objeto local
\(a\), nunca automáticamente a \(Pa\) o \(Qa\).

### S3 — qué requiere información asintótica del par

Clasificar, para cada uno de los dieciséis pares y sin heredar el PASS
de \(\sigma_2/I\), los siguientes niveles por separado:

| Nivel | Obligación |
| --- | --- |
| Identidades exactas | Verificar S1 con el par correspondiente |
| Compensación localizada y errores | Verificar S2 y sus cuantificadores |
| Patrón relativo \(+1:+1:-2\) | Identificar una escala cuadrática no nula y comprobar que el lineal y los errores causales son menores que ella |
| Ley cuantitativa de escala \(N^{-3}\) | Demostrar el líder, coeficiente y resto propios del par; no copiar \(A_N\) de C2a |
| Coherencias individuales | Controlar el emparejamiento complejo, no sólo su parte real |

Debe examinarse expresamente si el detector puede anular un canal líder,
si la suma completa tiene una cota inferior uniforme, y qué ocurre ante
ceros o subsecuencias. Si falta una estimación o una no anulación, el nivel
correspondiente queda OPEN. Una identidad general no certifica por sí sola
el exponente tres, la fase \(\sqrt N/2\), las constantes de C2a ni el
patrón relativo. No se exige un resultado favorable para los dieciséis
pares como condición para una clasificación rigurosa de alcance.

### S4 — formulación general y papel del corte duro

Formular, si lo permiten las pruebas, un resultado condicional con todas
sus hipótesis explícitas, distinguiendo:

- el álgebra que sólo usa proyectores complementarios;
- la estimación localizada que requiere una cota de propagación para la
  fuente local y el efecto positivo;
- la falta de soporte espacial finito introducida por este corte duro;
- la información adicional sobre el campo proyectado y el término lineal
  que permite pasar de compensación de amplitudes a líderes de bloques.

Precisar qué propiedades requieren que el proyector sea un multiplicador
de Fourier, un corte duro o un proyector que conmuta con la evolución.
No generalizar automáticamente a cualquier proyector duro, banda, estado,
dimensión, QCA o geometría. Una formulación abstracta condicional no
constituye verificación de sus hipótesis en otros modelos.

### S5 — techo de interpretación

Separar identidad algebraica, estimación asintótica e interpretación
física. Las coherencias son contribuciones firmadas a un observable;
no son probabilidades independientes. El proyector duro no representa
transporte físico local. La causalidad de rango finito por sí sola no
sustituye la cota del Teorema 4.1 en Bob. C2c no atribuye un origen
exclusivamente UV a la señal ni resuelve el protocolo condicionado C3.

## Método, failure search y límites

Auditoría analítica de las dependencias existentes antes de proponer una
extensión. Para cada paso se exige fuente, hipótesis, cuantificadores y
nivel de evidencia. Buscar fallos de normalización, términos de referencia,
conjugación, positividad, no conmutación con el detector, uniformidad,
anulación de canales y dependencia de la parte imaginaria.

No usar \(L-L_{PP}\), Teorema 4.4, la ley total ni los datos \(N=24,40\)
para establecer bloques o universalidad. No se autorizan en este contrato
simulaciones, nuevos barridos, ajustes, suavizado del corte ni una nueva
saddle analysis para completar casos sin prueba. Si un nivel necesita
análisis adicional no disponible, registrar la dependencia pendiente.

La revisión adicional por Astra sugerida por el usuario no se considera
realizada ni se dispara automáticamente al registrar este contrato.
No se alteran los contratos, candidato o informes históricos de C2a/C2b.

## Entregable y criterios de cierre

Una futura ejecución debe producir
`reports/2026-09-22--c2c-structural-scope.md`, con:

1. matriz de hipótesis y dependencias de S1–S4;
2. tabla de los dieciséis pares con los cinco niveles de S3 separados;
3. enunciado condicional general, si está justificado, con prueba y límites;
4. búsqueda adversarial y separación física S5;
5. lista explícita de niveles demostrados, refutados y abiertos.

`PROOF_WRITTEN / REVIEW_PENDING` distingue la ejecución de su aceptación.
Una revisión independiente puede emitir `C2C_PASS` para un alcance
explícitamente delimitado, `C2C_REPAIR_REQUIRED`, `C2C_FAIL` o
`C2C_INCOMPLETE`. Un PASS de la clasificación no transforma los niveles
marcados OPEN en teoremas ni equivale a universalidad del patrón.
Los contraejemplos analíticos que delimiten una extensión son resultados
válidos; nunca invalidan retrospectivamente el par certificado sin
identificar un error en su prueba.

El presente documento sólo fija el gate. No lo ejecuta ni promociona
resultados de C2c. C3 permanece separado, E/AdS congelado y los demás
frentes sin cambios. No hay publicación, commit ni push.
