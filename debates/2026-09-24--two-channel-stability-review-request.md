# Revisión independiente: estabilidad Schur y reconstrucción a Bob

## Decisión solicitada

Revisar únicamente la cadena matemática
\[
\text{cotas de bloques Schur}\Longrightarrow
\|t_N\|_{L^2}=O_W(1)\Longrightarrow
\|E^{1/2}\mathcal V_cPt_N\|,
\|E^{1/2}\mathcal V_cQt_N\|=O_W(N^{-1}),
\]
y las cotas de piezas que se deducen inmediatamente por Cauchy–Schwarz.
Atacar cuantificadores, constantes, normas y operadores. No revisar T1
completo ni T2/T3; no buscar cancelaciones, coeficientes, dominancia ni
H1c. No proponer Volterra nuevo.

## Enunciados que deben verificarse

1. En el soporte de Alice, `xi_*·(x-x_*) <= 0`; como
   `f=J(U_M-I)phi_N`, `||phi_N||=1` y `U_M` es unitario,
   `||s||=||F H_xi f||<=2`.
2. Para Bob, `R=N/4`, `y_*=Nu-R uhat`, `xi_*=lambda uhat` y
   `sqrt(h_N(y))=(1-|y-Nu|^2/R^2)_+`. Determinar si
   `||E^(1/2)V_c|| = sup_{y in B_N} sqrt(h_N(y)) exp[-xi_*·(y-y_*)]`
   y la cota `<= 8/(e lambda N)` son correctas, incluido el orden
   ajustado `Theta(N^-1)` sobre la red.
3. Con W fijo, verificar que `P,Q` tienen cotas operatoriales
   independientes de N y que se deduce
   `||E^(1/2)V_cP||, ||E^(1/2)V_cQ|| = O_W(N^-1)`.
4. Examinar si las estimaciones Schur (6), en sus normas diferentes
   P=`L2`, Q=`||·||_*`, bastan para que la recurrencia acoplada tenga
   norma de paso `<=1+C'/N` en `||x||_2+||y||_*`, con equivalencia
   uniforme en N, y por iteración `||t_N||_2<=C_W||s||_2`.
   Comprobar el retorno de la norma producto a la norma L2 de `t_N`.
5. Si esos pasos pasan, verificar el traslado al vector actual con el
   factor exacto `e^{-K_*N}` y las cotas superiores
   `|A_cP|,|A_cQ|<=C_W N^-1 e^{-K_*N}` y
   `0<=B_cPP,B_cQQ<=C_W N^-2 e^{-2K_*N}`,
   `|B_cPQ|<=C_W N^-2 e^{-2K_*N}`. Confirmar expresamente que sólo
   son cotas superiores y que las consecuencias de (4) heredan el
   nivel probatorio de Schur, rotulado PRELIMINARY / SIN REVISIÓN
   INDEPENDIENTE.

## Criterio de veredicto

Dar `PASS`, `REPAIR_REQUIRED` o `OPEN` para esta cadena, con la premisa
crítica, el primer paso que falla (si lo hay), la condición exacta que
desactivaría cada objeción y el alcance de cualquier pase. Separar la
cota operatorial geométrica (independiente de la estabilidad Schur) de
la cota sobre el vector `t_N`. No convertir un paso preliminar en un
resultado certificado. No inferir que los términos lineales dominan,
que las cotas son ajustadas, ni que exista término firmado líder.
