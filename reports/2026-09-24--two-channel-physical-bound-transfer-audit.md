# Transferencia de cotas a las diez piezas físicas P/Q

Fecha: 2026-09-24. Estado: `PHYSICAL_BOUND_TRANSFER_BLOCKED`.
Alcance: transferir únicamente estimaciones P/Q ya existentes a las diez
piezas de `(L_+,L_-)` del contrato de dos canales. No se estudian
cancelaciones, H1c, simetrías ni términos dominantes.

## 1. Fuentes auditadas y veredicto

Se leyeron el contrato canónico `state/CURRENT_STATE.md`, §§9.2–9.6;
T1 y su re-revisión independiente; T2 y T3; el precheck Volterra;
la auditoría Schur; las auditorías de resolvente de excursiones y de
masa de excursiones; y la reconstrucción H1 que contiene las cotas
regionales de extremos. El índice local `biblioteca/INDICE.md` se buscó
por QCA, P/Q, Volterra y corona; no se usa ningún resultado bibliográfico
para este traslado.

El contrato físico y las identidades exactas son los de T1,
`reports/2026-09-24--two-channel-t1-exact-signed-pq.md`, §§1–4.
En particular, para W fijo,
\[
r_c=B\pi_cU_N^NJ\phi_N,\qquad
d_{c,P}=e^{-K_*N}\mathcal V_cPt_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_cQt_N.
\]
El vector de salida `P` contiene la trayectoria siempre-P, la entrada
inicial desde Q y los retornos; la salida `Q` contiene Q inicial y
salidas desde P. Esto se lee en T1 (14)–(15), §§4. El sector final P
no clasifica el historial como libre de visitas a Q.

La única cota de extremo registrada como `PASS` es
`O(N^{-5/2})` para masas absolutas inclinadas de spinors completos del
protocolo plano: `state/CURRENT_STATE.md`, §9.2, y
`reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md`,
§§5–7. No es una cota de las salidas actuales reconstruidas
`\mathcal V_cPt_N`, `\mathcal V_cQt_N`, ni de la nueva referencia
`B\pi_cU_N^NJ\phi_N`; el propio estado conserva esa transferencia como
no certificada.

La cota `||\mathbb M_N||=O(N^{-1})` de
`reports/2026-09-24--h1c-return-kernel-schur-audit.md`, §2, es preliminar,
para el producto normalizado en `\ell^\infty_tL^2_p`. No controla por
sí sola los pesos gaussianos, las fronteras Q ni los extremos físicos;
§§3, 5. El precheck Volterra, §§3–4, deja abiertos transporte P
ponderado, sumabilidad Q con momentos variables/no-normalidad, interfaces
de ventanas y extremos físicos. La auditoría de resolvente,
`reports/2026-09-24--h1c-kernel-excursion-resolvent-audit.md`, §§3–6,
confirma que las cargas P y Q de los extremos planos embebidos pueden
ser ambas `O(N^{-5/2})`; la proyección final no aporta automáticamente
una potencia extra. Los kill-tests (`reports/2026-09-24--h1c-excursion-mass-kill-tests.md`,
§§2–4) niegan que la masa de excursiones local controle por sí sola el
producto espacial completo.

Por tanto, la regla de parada se activa: **las fuentes existentes no
controlan `d_{c,P}` ni `d_{c,Q}` después de la reconstrucción física**.
No hay para ninguna de las diez piezas una escala polinómica o
exponencial superior transferida. El `O(N^{-6})` antiguo no se transfiere
a ninguna fila (T2, §§1–4). El resultado final es
`PHYSICAL_BOUND_TRANSFER_BLOCKED`.

## 2. Niveles de afirmación y cotas generales disponibles

`EXACT_IDENTITY`: las cinco definiciones de las piezas y sus expresiones
auxiliares están en T1, §§3–4. Los factores `e^{-K_*N}` en términos
lineales y `e^{-2K_*N}` en términos cuadráticos son exactos en T1 (12),
no cotas de la magnitud de los factores normalizados.

`RIGOROUS UPPER BOUND`: para todo N, la unitariedad de `U_N`, la
normalización `||J\phi_N||=1`, el encoder unitario y la restricción de
canal/Bob dan `||r_c||≤1` y `||d_{c,P}+d_{c,Q}||≤||f||≤2`. Como
`0≤E≤I`, `|L_c|≤1` también se sigue de ser diferencia de dos
probabilidades. Estas cotas controlan la referencia y la suma física,
no cada proyección oblicua por separado.

Para cada N fijo existen las desigualdades formales
\[
|A_{cP}|\le2\|E^{1/2}r_c\|\,\|E^{1/2}d_{c,P}\|,
\quad
|A_{cQ}|\le2\|E^{1/2}r_c\|\,\|E^{1/2}d_{c,Q}\|,
\]
\[
0\le B_{cPP}\le\|E^{1/2}d_{c,P}\|^2,\qquad
0\le B_{cQQ}\le\|E^{1/2}d_{c,Q}\|^2,
\]
\[
|B_{cPQ}|\le2\|E^{1/2}d_{c,P}\|\,\|E^{1/2}d_{c,Q}\|.
\]
Son Cauchy–Schwarz para el efecto positivo; expresan exactamente qué
normas hacen falta, pero no producen una cota asintótica porque no hay
control de las dos normas P/Q tras reconstrucción. La suma de las dos
salidas sí es pequeña en el sentido trivial `||d_{c,P}+d_{c,Q}||≤2`;
esto no acota cada sumando cuando la partición inclinada no es ortogonal.

`ASYMPTOTIC UPPER BOUND`: no se obtiene para ninguna pieza actual.

`LEADING ASYMPTOTIC TERM`: ninguno identificado. En particular, no hay
coeficiente firmado `E_6`.

## 3. Trazabilidad exacta de los objetos

* `r_c`: referencia completa no codificada, evolucionada por el walk
  doblado `U_N^N`, luego extraída en el canal y restringida a Bob.
  T1 (1), (9); contrato en el Schur audit, §6.2. Es norma-controlada
  trivialmente por unitariedad, pero no con la masa `O(N^{-5/2})` del
  extremo plano tras activar la moneda.
* `d_{c,P}`: parte de salida final `P` de la diferencia codificada
  completa `f=J(U_M-I)\phi_N`, después de `T^N`, reconstrucción ponderada
  a Bob y extracción del canal. T1 (1), (4)–(8), (14)–(15). No se
  descarta el sumando coseno del encoder. Contiene memoria Q en general.
* `d_{c,Q}`: salida final `Q` de la misma diferencia y reconstrucción.
  Incluye `G_Q(N,0)Qs` y las salidas desde `C_kx_k`; véase T1 (14)–(15).
  No es una cota de “no P históricamente”: cuenta componente final Q.
* `P,Q`: idempotentes espectrales inclinados, oblicuos en general y
  relativos a W fijo; no son los canales físicos ni el corte IR.
  T1 §2 prueba acotación como multiplicadores para N fijo, no una cota
  asintótica para la composición con `\mathcal V_c`.
* `\mathcal V_c`: inversa de Fourier, multiplicador de restricción a
  Bob con peso de desinclinación y extracción del canal. T1 (6)–(8)
  prueba que está bien definido para cada N; explícitamente dice que
  esto no transfiere cotas asintóticas (T1 §2, líneas de (6)–(8)).

El objeto operador que falta controlar, de forma uniforme en N y con W
fijo, es al menos
\[
\|E^{1/2}\mathcal V_cPt_N\|,\qquad
\|E^{1/2}\mathcal V_cQt_N\|,
\]
incluidos los factores `e^{-K_*N}`; para afinar las interferencias
lineales también hace falta un control refinado del funcional de
referencia `E^{1/2}r_c` o de su emparejamiento efectivo. Equivalentemente,
se requieren estimaciones de las composiciones físicas completas de
(14) con esos extremos, controlando transporte P, borde Q, momentos
variables, cruces dentro/fuera de W y la norma de reconstrucción ponderada.
Esas cotas no aparecen en los informes auditados. No se propone derivarlas
en este expediente.

## 4. Tabla de las diez piezas

Convenciones de la tabla: el factor exponencial indicado es sólo el
factor exacto exterior de la identidad auxiliar; la parte que lo
multiplica no está acotada uniformemente por las estimaciones actuales.
`NO_CURRENT_BOUND` significa que no se justifica una cota cuantitativa
asintótica de la pieza física. Las afirmaciones valen separadamente para
`c=+` y `c=-`.

| TERM | BOUND | SOURCE | ASSUMPTIONS | EXPONENTIAL_SCALE | POWER_OF_N | SIGNED_INFORMATION_RETAINED | LOST_BY_ABSOLUTE_VALUE | STATUS |
|---|---|---|---|---|---|---|---|---|
| `A_{+P}` | `NO_CURRENT_BOUND`; condicional: `|A|≤2||E^{1/2}r_+||||E^{1/2}d_{+,P}||` | T1 (10a),(12),(14)–(15); endpoint gap T2 §3 | E efecto; W fijo; falta cota de ambos extremos reconstruidos | factor exacto `e^{-K_*N}`; no es escala de cota | `NO_CURRENT_BOUND` | La definición conserva `Re`; sin término líder firmado | C–S elimina signo/fase; viejo `N^-6` no transferido | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `A_{+Q}` | `NO_CURRENT_BOUND`; condicional: `|A|≤2||E^{1/2}r_+||||E^{1/2}d_{+,Q}||` | T1 (10a),(12),(14)–(15); Schur §3; resolvente §3 | E efecto; W fijo; falta referencia refinada y borde Q físico | factor exacto `e^{-K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Conserva `Re` exactamente | C–S elimina signo/fase; no hay potencia extra por proyectar Q | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `B_{+PP}` | `NO_CURRENT_BOUND`; condicional: `0≤B≤||E^{1/2}d_{+,P}||²` | T1 (10a),(12),(14)–(15) | E efecto; falta salida P reconstruida | factor exacto `e^{-2K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Signo no negativo exacto | Norma pierde magnitud/fase de la amplitud; no se identifica líder | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `B_{+QQ}` | `NO_CURRENT_BOUND`; condicional: `0≤B≤||E^{1/2}d_{+,Q}||²` | T1 (10a),(12),(14)–(15); Volterra (8) | E efecto; falta supervivencia Q y salida Q en extremos físicos | factor exacto `e^{-2K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Signo no negativo exacto | Norma pierde magnitud; fuga Q previa es sólo local/anterior | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `B_{+PQ}` | `NO_CURRENT_BOUND`; condicional: `|B|≤2||E^{1/2}d_{+,P}||||E^{1/2}d_{+,Q}||` | T1 (10a),(12),(14)–(15) | E efecto; faltan ambas salidas reconstruidas | factor exacto `e^{-2K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Conserva `Re` y posible signo | C–S pierde fase relativa; no hay `E_6` | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `A_{-P}` | `NO_CURRENT_BOUND`; condicional: `|A|≤2||E^{1/2}r_-||||E^{1/2}d_{-,P}||` | T1 (10a),(12),(14)–(15); endpoint gap T2 §3 | E efecto; W fijo; falta cota de ambos extremos reconstruidos | factor exacto `e^{-K_*N}`; no es escala de cota | `NO_CURRENT_BOUND` | La definición conserva `Re`; sin término líder firmado | C–S elimina signo/fase; viejo `N^-6` no transferido | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `A_{-Q}` | `NO_CURRENT_BOUND`; condicional: `|A|≤2||E^{1/2}r_-||||E^{1/2}d_{-,Q}||` | T1 (10a),(12),(14)–(15); Schur §3; resolvente §3 | E efecto; W fijo; falta referencia refinada y borde Q físico | factor exacto `e^{-K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Conserva `Re` exactamente | C–S elimina signo/fase; no hay potencia extra por proyectar Q | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `B_{-PP}` | `NO_CURRENT_BOUND`; condicional: `0≤B≤||E^{1/2}d_{-,P}||²` | T1 (10a),(12),(14)–(15) | E efecto; falta salida P reconstruida | factor exacto `e^{-2K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Signo no negativo exacto | Norma pierde magnitud/fase de la amplitud; no se identifica líder | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `B_{-QQ}` | `NO_CURRENT_BOUND`; condicional: `0≤B≤||E^{1/2}d_{-,Q}||²` | T1 (10a),(12),(14)–(15); Volterra (8) | E efecto; falta supervivencia Q y salida Q en extremos físicos | factor exacto `e^{-2K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Signo no negativo exacto | Norma pierde magnitud; fuga Q previa es sólo local/anterior | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |
| `B_{-PQ}` | `NO_CURRENT_BOUND`; condicional: `|B|≤2||E^{1/2}d_{-,P}||||E^{1/2}d_{-,Q}||` | T1 (10a),(12),(14)–(15) | E efecto; faltan ambas salidas reconstruidas | factor exacto `e^{-2K_*N}`; resto sin escala | `NO_CURRENT_BOUND` | Conserva `Re` y posible signo | C–S pierde fase relativa; no hay `E_6` | `PHYSICAL_BOUND_TRANSFER_BLOCKED` |

En las diez filas el término de retorno Q puede aparecer: en `d_{c,P}`
por entradas y retornos de (14), y en `d_{c,Q}` a través de los `x_k`
que ya contienen retornos. Esto es dependencia algebraica, no una cota
transferida. Ninguna fila deriva del antiguo `O(N^{-6})`; no hay
candidato a término dominante real con la evidencia actual.

## 5. Gate final

```text
PHYSICAL_BOUND_TRANSFER_BLOCKED
```

Falta una estimación uniforme post-reconstrucción para las normas de
efecto de las salidas P y Q actuales, es decir, para
`E^{1/2}\mathcal V_cPt_N` y `E^{1/2}\mathcal V_cQt_N` con su dependencia
en N y W, más control de referencia si se busca una cota mejor para A.
El `O(N^{-5/2})` de los extremos planos y el retorno normalizado
`O(N^{-1})` no suministran esas estimaciones. No se ejecutaron scripts,
datos numéricos ni barridos. No se editó el manuscrito ni el estado
canónico. No se hizo commit ni push.
