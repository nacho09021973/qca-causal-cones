# C3 — ejecución del gate de condicionamiento

Fecha: 2026-09-23. Estado: **C3_PROOF_WRITTEN / REVIEW_PENDING**.
Contrato: [IR_C3_CONDITIONING_GATE](../theory/IR_C3_CONDITIONING_GATE.md),
commit `8ce5cc1`.

La ejecución conserva el walk CJWW (5.15), nodo cero, recurso, regiones,
perfiles y corte de C1/C2/C2c. El alcance cuantitativo es para los cuatro
encoders originales y `M_B=I`. No se usan N=24/40, simulaciones, cuadraturas,
barridos, `L-Lpp` ni el Teorema 4.4.

## 1. Identidad exacta del condicionamiento

Sea
\[
v=U_M\phi_N,\qquad w=P v,\qquad t=Qv,
\qquad q_N=\|t\|^2.
\]
Como `P phi_N=phi_N`, `w` es el resultado de retener el sector P para el
bit cero, mientras que para el bit uno la probabilidad de retención es
`||w||^2=1-q_N`. Para `q_N<1`, el estado condicionado del bit uno es
`|w><w|/(1-q_N)`, y el del bit cero es `|phi_N><phi_N|`.

Por tanto, con
\[
\Delta=|v\rangle\langle v|-|\phi_N\rangle\langle\phi_N|,
\qquad
\Delta_{PP}=P\Delta P,
\]
se obtiene exactamente
\[
\Delta_{\mathrm{cond}}
=\frac{\Delta_{PP}+q_N|\phi_N\rangle\langle\phi_N|}{1-q_N}.
\tag{C3.1}
\]

Para el efecto de Bob `E=h_N I`, tomando la traza después de `S^N`,
\[
\boxed{
L_{\mathrm{cond},N}
=\frac{L_{PP,N}+q_Np_{0,N}}{1-q_N}},
\qquad
p_{0,N}=\langle S^N\phi_N,E S^N\phi_N\rangle.
\tag{C3.2}
\]
En particular,
\[
\boxed{
L_{\mathrm{cond},N}-L_{PP,N}
=\frac{q_N(p_{0,N}+L_{PP,N})}{1-q_N}}.
\tag{C3.3}
\]
La identidad no identifica `Lpp` con una diferencia de probabilidades
condicionadas: `Lpp` es el observable firmado antes de la normalización.

## 2. Probabilidad de éxito y límite de `p0_N`

C1 da, para cada uno de los cuatro encoders,
\[
q_N=D N^{-5/2}(1+O(N^{-1/2})),
\qquad D=\frac{1024\pi^2 B^2}{5}>0.
\tag{C3.4}
\]
Así `q_N -> 0` y la probabilidad de éxito del bit uno es
`1-q_N=1-DN^{-5/2}(1+O(N^{-1/2}))`; la del bit cero es exactamente uno.

Para `M_B=I`, se usa la normalización congelada del manuscrito
`papers/ir-corona/ir-corona.md`, §3.2: con `u=(1,1,1)`,

\[
h_N(y)=\left(1-16|y-Nu|^2/N^2\right)_+^2,
\qquad E=h_N\otimes I .
\]

Por tanto, escribiendo `r_N=S^N phi_N`,
\[
p_{0,N}=\sum_{y\in\mathbb Z^3}h_N(y)\,\|r_N(y)\|^2.
\]
El lema de la cola de C1 da `r_N(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})`
uniformemente en la bola de Bob. Al poner `Y=y/N`, el factor
`N^{-3}` de `\|r_N(y)\|^2` se compensa con la densidad `N^3` de la suma,
y las sumas de Riemann dan
\[
p_{0,N}\longrightarrow
p_\infty:=\int_{|Y-u|<1/4}h_0(Y-u)\|R_0(Y)\|^2\,d^3Y,
\qquad h_0(Z)=(1-16|Z|^2)^2.
\tag{C3.5}
\]
El peso `h_0` es estrictamente positivo en el interior de la bola. `R_0` es
la transformada de Fourier de una función compacta no nula y, por tanto,
es analítica; no puede anularse en toda una bola abierta. De aquí
\[
p_\infty>0.
\tag{C3.6}
\]
No se evalúa numéricamente `p_infty`.

## 3. Corrección de normalización

La premisa que se usa aquí está demostrada fila a fila en C2c, no sólo
por la cobertura global de los dieciséis pares. En §8 de
`reports/2026-09-22--c2c-structural-scope.md` aparecen explícitamente las
cuatro filas con `D_0=I` y
`M in {I, sigma_1, sigma_2, sigma_3}`. La expansión (C16), aplicada a cada
una de esas filas, es

\[
L_{PP}^{M,D_0}=N^{-3}\mathscr A_{M,D_0}(\sqrt N)+O(N^{-13/4}).
\]

La propia clasificación de C2c controla uniformemente el coeficiente líder
en el alcance congelado; por tanto cada uno de esos cuatro pares satisface
`L_{PP,N}=Theta(N^{-3})`, y en particular `L_{PP,N}->0`. Insertando (C3.4)–(C3.6) en
(C3.3),
\[
\boxed{
L_{\mathrm{cond},N}-L_{PP,N}
=D p_\infty N^{-5/2}(1+o(1))}. 
\tag{C3.7}
\]
La corrección es algebraica y positiva a orden líder. El líder de `L_cond`
queda fuera del alcance contractual; además, la cota `L_{PP,N}=Theta(N^{-3})`
es de orden estrictamente menor que `N^{-5/2}`, así que no hay una
cancelación por órdenes entre `Lpp` y la corrección de (C3.3). Tampoco se
compara `Lcond-Lpp` con el observable total `L` mediante una norma global.

## 4. Veredicto de ejecución y límites

| Obligación | Estado |
| --- | --- |
| Identidad exacta de estados y `Lcond` | PASS, pendiente de revisión |
| Probabilidades de éxito | PASS, pendiente de revisión |
| `p0_N -> p_infty > 0` para `M_B=I` | PASS, pendiente de revisión |
| Corrección (C3.7) | PASS, pendiente de revisión |
| Líder de `Lcond` o `abs(Lcond)` | OPEN |
| Comparación `Lcond-Lpp` con `L` | OPEN y fuera del gate |

Resultado de esta ejecución: **`C3_PROOF_WRITTEN / REVIEW_PENDING`**. C3 no
reabre C2, no modifica C2c, no abre H1c ni E/AdS y no constituye una
interpretación de transporte local.
