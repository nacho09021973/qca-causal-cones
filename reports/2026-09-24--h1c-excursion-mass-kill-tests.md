# H1c: kill-tests de la masa de excursiones P/Q

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Alcance: comprobar si la carga
`N\epsilon_N^2\sum_\ell\Gamma_N(\ell)` es un objeto suficiente para
`H1c_LOCALIZATION (L')`. No se modifica el contrato de H1c.

**Cierre documental del día:** este precheck conserva su alcance previo.
El contrato operacional posterior, los estados vigentes y el plan T1–T3
se fijan en [el cierre H1c, §§6–8](2026-09-24--h1c-return-kernel-schur-audit.md).
Volterra/localización asintótica está PAUSED; este archivo no prueba las
respuestas físicas `(L_+, L_-)` del nuevo contrato.

## 1. Identidad de historias: válida para matrices, alcance restringido

Sea `A_j` una sucesión de matrices diagonalizables con autovalor
dominante `\lambda_j`, proyector de Riesz `P_j`, `Q_j=I-P_j` y
`B_j=\lambda_j^{-1}A_j`. Si el autovalor dominante es semisimple,
`B_jP_j=P_j` y `P_jB_jQ_j=Q_jB_jP_j=0`. Al insertar
`I=P_j+Q_j` entre factores se obtiene una suma **exacta** de historias
para el producto de matrices. La entrada y salida en canales distintos
obligan a contar también historias con una sola transición, y una
entrada `Q_0` puede permanecer en `Q` sin transición alguna.

En el walk doblado del repo, el haz dominante de
`D(z)=S(z)\oplus S(z)^{-1}` es de **rango dos**, no simple:
`state/CURRENT_STATE.md`, §9.1. En una ventana local con gap, la moneda
débil preserva ese rango. La contabilidad P/Q sigue teniendo sentido
para un haz semisimple de rango dos; el supuesto de simplicidad del
esquema propuesto debe sustituirse por ese contrato.

## 2. Dos contraejemplos exactos a una lectura demasiado fuerte

### 2.1 La carga sola no controla el canal Q inicial

En `\mathbb C^2` tomemos proyectores ortogonales constantes
`P=\operatorname{diag}(1,0)`, `Q=I-P` y
\[
B_j=P+\rho_NQ,\qquad \rho_N=1-N^{-1}.
\]
Para cada `N`, el autovalor dominante `1` es simple y
`\epsilon_N=0`. Por tanto la carga propuesta es exactamente cero,
aunque `\Gamma_N(\ell)=\rho_N^\ell` y
`\sum_{\ell=0}^{N}\Gamma_N(\ell)=\Theta(N)`. Sin embargo,
\[
B_{N-1}\cdots B_0-P=\rho_N^NQ\longrightarrow e^{-1}Q.
\]
Luego `\mathfrak L_N\to0` **por sí solo** no implica localización en
norma del producto completo. Hace falta una condición separada de
supervivencia de `Q_0`, como `\Gamma_N(N)\to0`, o proyectar el extremo
inicial a `P_0`. La condición adicional propuesta
`\sup_N\sum_\ell\Gamma_N(\ell)<\infty` sí excluye este ejemplo;
el contraejemplo afecta a la implicación encerrada en caja, no a esa
versión reforzada.

### 2.2 Una transición de borde puede dominar la carga

En `\mathbb R^2`, sean
`u_j=(\cos j\delta_N,\sin j\delta_N)`,
`P_j=u_ju_j^T`, `Q_j=I-P_j` y `B_j=P_j`, con
`\delta_N=N^{-2}`. Aquí el autovalor dominante `1` es simple,
`\epsilon_N=\sin\delta_N`, `\Gamma_N(0)=1` y
`\Gamma_N(\ell)=0` para `\ell\ge1`. Por tanto
`\mathfrak L_N=N\sin^2\delta_N=\Theta(N^{-3})`.
Pero la diferencia entre el producto completo y la trayectoria que
termina en `P_N` es exactamente
\[
Q_NP_{N-1}\cdots P_0
=Q_Nu_{N-1}u_0^T(\cos\delta_N)^{N-1},
\]
cuya norma es
`(\cos\delta_N)^{N-1}\sin\delta_N=\Theta(N^{-2})`.
Una cota **sólo** de orden `O(\mathfrak L_N)` para el producto completo
es falsa, incluso con `\sum\Gamma_N=1` y matrices normales. La fórmula
propuesta con un `+o(1)` sin cuantificar no queda refutada, pero ese
resto debe contener al menos la transición de borde `O(\epsilon_N)`.
Para el bloque comprimido `P_N(\cdot)P_0`, este contraejemplo de borde
desaparece; esa es una conclusión distinta.

### 2.3 Lema abstracto que sí sobrevive

Sea `\epsilon=\max_j\|P_{j+1}-P_j\|`,
`M=\sup_j\|B_jQ_j\|`,
`G=\sum_{\ell=0}^{N}\Gamma_N(\ell)` y supóngase
`\|P_0\|\le K`, `N\epsilon\le c_0`, `N\epsilon^2MG<1`.
Para **entrada `P_0` y salida `P_N`**, la suma de historias con al menos
una excursión completa obedece la cota algebraica
\[
\left\|P_NB_{N-1}\cdots B_0P_0
-P_NB_{N-1}P_{N-1}\cdots P_1B_0P_0\right\|
\le K e^{c_0}
\frac{N\epsilon^2MG}{1-N\epsilon^2MG}.
\tag{7}
\]
En efecto, una transición `P_j\to Q_{j+1}` cuesta a lo sumo
`\epsilon`, una `Q_j\to P_{j+1}` cuesta a lo sumo `\epsilon M`, y
la propagación interna de longitud `\ell` cuesta `\Gamma_N(\ell)`.
Los segmentos P entre excursiones cuestan a lo sumo
`(1+\epsilon)^N\le e^{c_0}` en total. Para `k` excursiones, la suma
cruda sobre posiciones y longitudes es a lo sumo
`(N\epsilon^2MG)^k`; sumar `k\ge1` da (7). Esta prueba no precisa
normalidad ni rango uno, pero sí el bloque comprimido y las hipótesis
escritas. No controla historias de borde ni una dinámica espacial con
transferencia de momento.

## 3. Qué sí da el cálculo local del walk congelado

La reconstrucción H1, §§2-3, demuestra sólo en ventanas fijas de los
ocho máximos que el proyector dominante tiene rango dos y que, para
un salto espacial acotado, la variación de los proyectores congelados
`P_N(X,z)` es `O(N^{-2})`, debido al factor `1/N` de la moneda además de
la variación `X\mapsto X+e/N`. Esta es más pequeña que el
`O(N^{-1})` genérico del esquema abstracto.

En esas ventanas, el símbolo congelado `A_N(X,z)=C_N(X)D(z)` conserva
dos raíces recíprocas `\mu_+(X,z)`, `\mu_-(X,z)=\mu_+^{-1}`, cada una
de multiplicidad dos: `\beta` empareja los haces de `D`, y en una base
emparejada `A_N` consta de dos bloques idénticos de dimensión dos.
Para `B=\mu_+^{-1}A_N` y el `Q` de ese símbolo,
\[
B=P+\mu_+^{-2}Q.
\]
La brecha local y la acotación uniforme de proyectores dan, para `X,z`
fijos, `\|QB^\ell Q\|\le C\rho^\ell` con `\rho<1`. Si `X_j`
cambia por pasos `O(N^{-1})` manteniendo `z` en la misma ventana, la
variación `O(N^{-2})` de `Q_j` permite absorber el producto de
proyectores sucesivos en una tasa `\rho'<1` para `N` grande. Éste es
un test **local congelado** favorable a `\sum\Gamma_N<\infty`;
reproduce el alcance de H1b, todavía sin revisión independiente.

No se sigue una cota para el supremo sobre todos los parámetros
complejos de H1c: `CURRENT_STATE.md`, §9.1, no declara gap global
en el toro. Tampoco se sigue el elemento Alice/Bob espacial.

## 4. Por qué la carga propuesta aún no es la de L'

El operador real es `U_N=C_N(x)D`, con `D` de alcance finito. Una
trayectoria espacial lleva matrices de salto individuales `D_h`, no la
matriz congelada `D(z)`; la reconstrucción H1, §8, ya descarta usar
H1b camino a camino. En la representación exacta de
`reports/2026-09-24--h1c-exact-dyson-decomposition.md`, (3), cada
inserción de moneda transfiere momento
`\eta_{a-1}\to\eta_a`. El cambio de canal puede venir de la parte
impar del núcleo `\widehat M_N(\eta_a-\eta_{a-1})`, proporcional a
`\beta`, incluso cuando los
proyectores congelados no cambian espacialmente. El test de moneda
constante de ese informe deja `\epsilon_N=0` para una secuencia
congelada, pero produce una corrección relativa no nula `O(N^{-1})`
en el elemento Alice/Bob embebido. Es la corrección espectral de
`\lambda_j` y la excursión respecto de la base de `D`, no una
transición entre `P_j` consecutivos del símbolo ya perturbado.

Por tanto, calcular numéricamente `\Gamma_N(\ell)` sólo para matrices
`A_N(X_j,z)` a `z` fijo puede verificar H1b y aun así dejar intacto
el problema `L'`: momentos variables, ocho ventanas, regiones sin
splitting local y extremos. No sería un kill-test decisivo de H1c.

## 5. Salida del precheck

La idea de sumar **excursiones completas** es algebraicamente válida
para el bloque `P_N B_{N-1}\cdots B_0P_0` de una sucesión de matrices,
si se controlan transporte P, propagación Q y transiciones. La carga
propuesta no controla por sí sola el producto completo. En el walk
espacial, el objeto pertinente tendría que definirse sobre el núcleo
de momentos de la identidad Dyson exacta, con términos de borde y
supervivencia Q separados. Los tres tests propuestos sobre fibras
congeladas no alcanzan ese objeto.

`H1c_LOCALIZATION (L') = OPEN`. No se promueve H1, ni se cambian C2c,
E0, `POWER_13/2_STABILITY`, E/AdS, TeX o estado canónico. No se ejecutó
código numérico: los contraejemplos y la cota local son algebraicos.
