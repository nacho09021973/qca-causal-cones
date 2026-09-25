# C2c — revisión interna de Codex

Fecha: 2026-09-23. Revisor: Codex, agente `/root`.

**Naturaleza de la revisión.** Esta es una revisión interna y adversarial, no
independiente: el revisor es también el autor de la derivación C2c. Sustituye
la revisión Claude solicitada en los criterios sólo por autorización explícita
del usuario. No es una ratificación, no promociona `state/CURRENT_STATE.md` y
no emite evidencia de diversidad de modelo.

## Objeto y protocolo

Se revisó la nota
`reports/2026-09-22--c2c-structural-scope.md` en `fa9c07f`, blob
`94cdf0f8801a219fc45df5000b86bb04614027ef`, SHA256
`f6266e951d3f5ffed20aef9ef8a75fe189f56b90df2b2f2e9af0abf11d407fb5`, contra
el contrato `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md` y los criterios congelados
en `537e108`. §12 y los documentos FR1–FR3 quedan fuera de la revisión.

No se usaron `L-L_PP`, el Teorema 4.4, datos `N=24,40`, simulaciones,
cuadraturas ni barridos nuevos. El Teorema 4.1 se usa únicamente como cota
superior de `T_N`.

## Test de falsación mínimo

Para la fila adversa `M=I`, `D_3=(I+sigma_3)/2`, la representación C2 da
`zeta_M=downarrow` y el campo de referencia de C2c queda, con
`b=1/4`,

\[
D^W_{M,K}(Y)=-\frac{i16\beta}{\rho K^3}
\sum_{\sigma,\epsilon=\pm1}
\frac{\Pi_\sigma(n)\downarrow}{\rho+\sigma+\epsilon b}
\cos((\rho+\sigma+\epsilon b)K)+O(K^{-4}).
\]

Al formar el emparejamiento lineal con el recurso, las fases radiales tienen
la forma

\[
\pm\sqrt3+(\epsilon-\eta)b-\sigma,
\qquad \epsilon,\eta,\sigma\in\{\pm1\}.
\]

Como `|epsilon-eta| b <= 1/2` y `|sigma|=1`, cada módulo es al menos
\(\sqrt3-3/2=\gamma>0\). Las fases dependen linealmente de la variable
radial con derivada `+1` o `-1`, por lo que no hay fase radial estacionaria.
Los cruces `Pi_+ D_3 Pi_-` no pueden descartarse algebraicamente y deben
permanecer en la forma cuadrática.

En `n_0=u/sqrt(3)`, el vector de Bloch de `J(n_0)` es
`(1,-1,1)/sqrt(3)`. Para `downarrow` y `D_3`, (C14) da, para ambos signos
`sigma`,

\[
\|D_3^{1/2}\Pi_\sigma(n_0)\downarrow\|^2
 =\frac{1-\sigma/\sqrt3}{2}\frac{1+\sigma/\sqrt3}{2}
 =\frac16>0.
\]

Este test no encuentra una fase estacionaria ni una anulación inmediata del
canal. No demuestra todavía la transferencia completa de §5.2.

## Auditoría algebraica y de localidad

Las identidades de bloques (C3) se siguen de `Q=I-P`, `P phi=phi`,
hermiticidad de `E` y positividad de `E`; no requieren `[S,P]=0` para la
descomposición previa a la evolución. Las constantes `8 T_N+4 T_N^2` y
`6 T_N` son compatibles con las normas indicadas en la nota. La forma
individual requiere además `|<r,E d_P>|=o(Q_N)`; no basta controlar su parte
real.

Para los cuatro encoders y los cuatro detectores congelados, `0<=D<=I`, el
recurso es el mismo, la fuente sigue siendo local y el soporte de Bob es el
mismo. Bajo el Teorema 4.1, la extensión de la cota `T_N` y de la
compensación localizada a los dieciséis pares es correcta. Esto no aplica la
cota causal a `P a` o `Q a` por separado.

**C1:** `PASS` como teorema condicional. `T_N=o(Q_N)` y
`Lin_N=o(Q_N)` implican el patrón; no se presentan como condiciones
necesarias u óptimas. Para la componente PP aislada,
`Lin_N=o(Q_N)` sí es necesaria y suficiente porque
`L_PP/Q_N=1+Lin_N/Q_N` exactamente.

## Transferencia cuantitativa (§5.1–§7)

La nota identifica correctamente el riesgo: para detectores de rango uno no
se puede eliminar `Pi_+ D Pi_-`. También son correctos, a nivel algebraico,
los factores `128`, `64` y `512`, las frecuencias posibles y el argumento de
independencia racional por polos simples, siempre que los campos (C5) y los
restos de transferencia ya estén establecidos.

El problema que impide aceptar las quince extensiones nuevas es probatorio.
§5.2 sustituye la rederivación de los lemas de C2a por la frase de que `D` es
una matriz constante de norma a lo sumo uno. Eso no escribe, lema por lema,
la transferencia con `h D R_N`, los espinores `zeta_M`, los cruces de banda,
los correctores (17)–(19), el cambio de recurso (20) ni las cotas (21)–(23).
La representación C2 se etiqueta además
`REPRESENTATION_DERIVED / PRELIMINARY; PROJECTED_ASYMPTOTICS_OPEN`; sus
identidades exactas sirven como entrada, pero las asintóticas proyectadas no
pueden promoverse sólo por referencia.

Por tanto, (C7), la cota inferior (C15) aplicada a los campos transferidos y
las expansiones (C16) quedan sin demostración revisada para los detectores de
rango uno y para los encoders distintos del caso ya certificado. El argumento
de positividad de la matriz de Gram es plausible y el test mínimo lo apoya,
pero no repara la ausencia de la transferencia completa.

La comparación para `sigma_2/I` reproduce las constantes `C_0,C_1` de C2a
cuando `D=I`; se acepta con el alcance de C2a. La frase de §8 debe decir
**a lo sumo ocho familias**: la igualdad de densidades de espinor da esa
cota, pero no se demuestra que las ocho funciones sean distintas.

## Veredictos por fila y nivel

`PASS` en esta tabla significa resultado de esta revisión interna y no PASS
independiente.

| Fila | Identidades exactas | Compensación localizada | Patrón relativo | Ley `N^-3` y coeficiente | Coherencias individuales |
| --- | --- | --- | --- | --- | --- |
| `sigma_2`, `D_0=I` | PASS (alcance C2b) | PASS (alcance C2b) | PASS (alcance C2a/C2b) | PASS (alcance C2a) | PASS (alcance C2b) |
| Las otras 15 filas | PASS | PASS | REPAIR_REQUIRED | REPAIR_REQUIRED | REPAIR_REQUIRED |

La clasificación de las quince filas no es un FAIL matemático: identifica un
hueco reparable de demostración. En particular, el resultado no se extiende
por esta revisión a una ley universal ni a otras clases de QCA.

## §9.2 y techo de interpretación

El argumento concreto para el multiplicador escalar duro, una fuente local no
nula y regiones espectrales interiores/exteriores abiertas es correcto como
argumento de analiticidad: una transformada trigonométrica que se anula en un
abierto exterior se anula en todo el toro, lo que contradice una fuente no
nula. No demuestra una tasa de cola.

La frase «Este argumento se extiende a cortes escalares con esas propiedades
de abiertos» no fija suficientemente qué multiplicadores, regularidad y
relación con la evolución se permiten. Veredicto de §9.2: `REPAIR_REQUIRED`
para precisar esas hipótesis; el núcleo del argumento queda `PASS` dentro del
corte escalar declarado.

La separación física de S5 es correcta: los bloques son contribuciones
firmadas de un observable espectral, no probabilidades independientes ni
transporte físico. No se infiere origen exclusivamente UV, señalización
general, microcausalidad ni una aplicación AdS.

## Veredicto global

**`C2C_REPAIR_REQUIRED` (revisión interna, no independiente).**

La nota cierra el álgebra S1, la compensación S2, el criterio condicional C1 y
el caso ya certificado `sigma_2/I`. No cierra la transferencia analítica
necesaria para las quince filas restantes. Para convertirlas en `PASS` hace
falta una nota corregida que rederive §5.2 lema por lema desde el texto
primario de C2a, y que precise la frase general de §9.2 y cambie «ocho» por
«a lo sumo ocho».

Este informe no modifica `state/CURRENT_STATE.md`, no cambia el contrato C2c,
no reabre C3 ni E/AdS y no promociona ningún resultado al estado canónico.
