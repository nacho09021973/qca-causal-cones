# H1c: auditoría adversarial del resolvente de excursiones

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Alcance: auditar el resolvente P/Q del **núcleo exacto en momento**;
`H1c_LOCALIZATION (L') = OPEN`.

**Cierre documental del día:** este precheck precede a la decisión
operacional de [el cierre H1c, §§6–8](2026-09-24--h1c-return-kernel-schur-audit.md).
Las carencias físicas descritas abajo son el diagnóstico previo; el nuevo
contrato fija `(L_+, L_-)`, pero su lift exacto al P/Q de este informe sigue
pendiente en T1. Volterra/localización asintótica está PAUSED. Los usos de
«canal» para P/Q en el precheck no identifican P/Q con los canales `+/-`.

## 1. Objeto exacto y elección pendiente

Sea `\mathscr H=\bigoplus_{j=0}^{N}L^2(\mathbb T^3;\mathbb C^4)` y
`\mathbb V` el operador que lleva la capa temporal `j` a `j+1`
mediante el núcleo inclinado exacto de `U_N=C_N(x)D`. El núcleo sin
normalizar es
\[
\mathcal K_N(p',p)
=\delta(p'-p)D_\xi(p)
 +\widehat M_N(p'-p)D_\xi(p),\qquad
M_N(x)=e^{-i\vartheta(x/N)\beta/N}-I,
\tag{1}
\]
con la convención de Fourier de
`reports/2026-09-24--h1c-exact-dyson-decomposition.md`, (2)-(3).
Una normalización escalar por el canal dominante puede incluirse en
`\mathcal K_j`; no cambia las identidades de bloques de abajo.
Si `s` vive en la capa 0 y `\ell` lee la capa `N`, entonces
\[
L_N=\ell(I-\mathbb V)^{-1}s
=\ell\mathbb V^Ns.
\tag{2}
\]
La segunda igualdad usa que cada aplicación avanza exactamente una
capa. Las fases y pesos Alice/Bob pueden absorberse en `s,\ell` como
en la representación inclinada exacta. La definición del `L'` físico
todavía requiere fijar sus extremos de cuatro componentes y el
funcional final; aquí `L_N` es el elemento complejo con extremos fijos.

Para insertar `\mathbb P+\mathbb Q=I` exactamente en `\mathscr H`, se
necesita un proyector `P_j(p)` medible **en todo el toro**. El proyector
de Riesz del repositorio está controlado sólo en ocho ventanas locales
(`state/CURRENT_STATE.md`, §9.1). Se puede elegir una extensión
auxiliar, por ejemplo `P=0` fuera de ventanas, pero entonces los
saltos que cruzan sus bordes entran en los bloques mixtos y deben
estimarse. La existencia algebraica de un resolvente Volterra no
resuelve esa elección.

## 2. Schur-Volterra exacto: propagación P y excursiones repetidas

Escribamos `V_{ab}=\mathbb a\mathbb V\mathbb b` para `a,b\in\{P,Q\}`.
Como `\mathbb V` adelanta el tiempo, todos sus bloques y productos
cerrados son nilpotentes en el intervalo finito. Definamos
\[
G_P=(I-V_{PP})^{-1},\qquad G_Q=(I-V_{QQ})^{-1},\qquad
\Sigma=V_{PQ}G_QV_{QP},\qquad
R_P=(I-V_{PP}-\Sigma)^{-1}.
\tag{3}
\]
Entonces, por inversión de bloques de `I-\mathbb V`, **exactamente**
\[
\begin{array}{ll}
R_{PP}=R_P,&R_{PQ}=R_PV_{PQ}G_Q,\\
R_{QP}=G_QV_{QP}R_P,&
R_{QQ}=G_Q+G_QV_{QP}R_PV_{PQ}G_Q.
\end{array}
\tag{4}
\]
La contribución que nunca entra en Q es `L_{N,P}=\ell_PG_Ps_P`.
Restando esta contribución y usando
`R_P-G_P=G_P\Sigma R_P=R_P\Sigma G_P`, se obtiene
\[
\begin{aligned}
L_N-L_{N,P}={}&
\ell_PG_P\Sigma R_Ps_P
+\ell_PR_PV_{PQ}G_Qs_Q\\
&+\ell_QG_QV_{QP}R_Ps_P
+\ell_QG_Qs_Q\\
&+\ell_QG_QV_{QP}R_PV_{PQ}G_Qs_Q.
\end{aligned}
\tag{5}
\]
Éstas son las cuatro clases de extremos P/Q, con la clase Q/Q
dividida en supervivencia Q pura y visitas a P. En (5) aparecen los
tramos `G_P` y `R_P` antes/después de una excursión; `R_P` suma además
excursiones repetidas. La expresión de cuatro términos sin esos
factores no es una descomposición exacta y su suma de normas no puede
ser todavía una cota de `|L_N-L_{N,P}|`.

**Kill-test finito.** En cuatro capas temporales `0,1,2,3`, tomemos
`s_P` en 0, `\ell_P` en 3, una transición `P\to Q` de amplitud `a`
en `0\to1`, otra `Q\to P` de amplitud `b` en `1\to2`, y
`P\to P=1` en `2\to3`; los demás bloques son cero. El elemento
completo vale `ab`, el camino puramente P vale cero, pero
`\ell_P\Sigma s_P=0` porque `\Sigma s_P` acaba en la capa 2.
El factor `G_P` de (5) transporta esa contribución hasta la capa 3.

## 3. Boundary test en los extremos planos embebidos

En el saddle `p=0`, el TeX plano, §7.3, da un proyector hermítico
`P_S` de rango uno con elemento fuera de diagonal
`-(1+ic_*)\alpha/(2c_*^2)\ne0`. En el walk doblado,
\[
P_D=\operatorname{diag}(P_S,I-P_S),\qquad
Q_D=\operatorname{diag}(I-P_S,P_S).
\tag{6}
\]
Para la fuente plana embebida `(f,0)`, el spinor principal de Alice
es `\chi=\uparrow` o `\downarrow`; por (6),
`Q_D(\chi,0)=((I-P_S)\chi,0)\ne0`. La fórmula de capas del TeX,
§7.3, da `\mathfrak A_f(0)=N^{-5/2}` por un coeficiente no nulo
(la suma de capas `\mathcal S_+(0;\theta_N)` es positiva);
por tanto **esta entrada Q no gana una potencia de N en el extremo**.

Para Bob con `M_B=I`, el mismo TeX da, en el punto enfrentado,
`R_0/c_r=(-\mathcal I_1(1+i)/\sqrt3,\,
\mathcal I_0+\mathcal I_1/\sqrt3)^T`, con
`\mathcal I_0,\mathcal I_1>0`, y `c_*>1`. Su razón de componentes
tiene fase `\pi+\pi/4`, distinta de la razón de un vector del rango
de `P_S`, con fase `\pi+\arctan c_*`; así
`R_0^\dagger(I-P_S)\ne0`. La capa Bob principal también es
`N^{-5/2}` y **su carga Q no recibe por proyección una potencia extra**.
La localización puede seguir viniendo de `G_Q` y de los bloques de
salida, no de una pequeñez automática de `s_Q,\ell_Q`.

Este cálculo usa la inserción de los extremos planos en la primera
componente y no certifica cuáles son los extremos físicos de `L'`;
éstos siguen sin fijarse en los archivos H1c.

## 4. Kernel mismatch: el primer bloque mixto es de orden 1/N

Tomemos en una ventana local `P(p)` del símbolo libre `D_\xi(p)` y
`Q=I-P`. De (1) y `D_\xi(p)P(p)=\lambda(p)P(p)`, la parte libre no
mezcla canales y
\[
Q(p')\mathcal K_N(p',p)P(p)
=\lambda(p)Q(p')\widehat M_N(p'-p)P(p).
\tag{7}
\]
La identidad exacta de la moneda separa
\[
\widehat M_N(q)=\widehat{\cos(\vartheta/N)-1}(q)I
-i\widehat{\sin(\vartheta/N)}(q)\beta.
\tag{8}
\]
En `p'=p`, `Q(p)P(p)=0`, pero
`Q(p)\beta P(p)=\beta P(p)\ne0` bajo el contrato congelado.
La parte impar de (8) tiene tamaño `O(N^{-1})` **como operador de
convolución** (equivale a multiplicar por
`\sin(\vartheta(x/N)/N)` en posición). Su núcleo puntual en `q=0`
no tiene por qué ser `O(N^{-1})`: para soporte espacial de volumen
`O(N^3)` puede alcanzar `O(N^2)`. No se obtiene un factor de
`|p'-p|` en el bloque `Q\leftarrow P`. La cota ideal
`\|V_{QP}\|=O(N^{-2})` no se sigue de la regla de selección
`P\beta P=0`. Para el perfil suave con meseta constante de §4 del
informe de Dyson, un paquete de momento centrado en `p=0` y anchura
`N^{-1/2}` tiene anchura espacial `O(\sqrt N)` dentro de la meseta.
Sobre ese paquete, la compresión mixta es
`-i\theta\beta P(0)/N+o(N^{-1})`; por tanto su norma local es al menos
`c/N` para `\theta\ne0`. El orden local del acoplamiento impar es
`N^{-1}`. Lo mismo vale para `P\leftarrow Q`.

En el test de moneda constante sobre todos los caminos Alice/Bob,
la parte impar es exactamente `-i\theta\beta/N` allí; dos cambios
de canal producen el término de orden relativo `N^{-1}` de
`reports/2026-09-24--h1c-dyson-target-check.md`. En lenguaje
Volterra, `\Sigma` cuesta dos acoplamientos `O(N^{-1})` y un
`G_Q` local sumable, pero los `G_P` de (5) permiten `O(N)`
posiciones para la pareja. Por eso un `\|\Sigma\|=O(N^{-2})`
no implica por sí solo una corrección observada `O(N^{-2})`.

## 5. Q-Green: existencia algebraica y tamaño son problemas distintos

La nilpotencia temporal prueba `G_Q=\sum_{k=0}^{N}V_{QQ}^k`
sin hipótesis de gap. No acota su norma. Un shift nilpotente de
`N+1` capas con peso `c>1` tiene radio espectral cero, pero
`\|G_Q\|\ge c^N`. Esto muestra que la finitud de la suma Volterra
no controla transitorios no normales ni sectores fuera de las ventanas.

Dentro de una ventana fija y a momento congelado, H1b da un Q
relativamente contractivo; fuera de las ventanas no hay splitting
de Riesz certificado, y (1) conecta momentos distintos. El gate útil
debe estimar **las composiciones de (5) entre los extremos reales**,
no sólo una norma global de `G_Q`.

## 6. Veredicto del precheck

El resolvente de excursiones es una identidad algebraica válida y
admite rango dos y transferencia de momento, siempre que se fije una
partición P/Q global. Para convertirse en una cota de `L'` necesita:

1. extremos y funcional físico de cuatro componentes;
2. una partición P/Q definida fuera de las ventanas, con cargas de
   cruce de ventana;
3. las cinco composiciones de (5), incluyendo transporte P y
   excursiones repetidas;
4. un control de `G_Q` compatible con no-normalidad y con el elemento
   Alice/Bob, además del coste `O(N^{-1})` de los bloques mixtos.

La fórmula inicial de cuatro términos y el pronóstico
`\|V_{PQ}\|,\|V_{QP}\|=O(N^{-2})` no superan este precheck en su
lectura uniforme. Esto no refuta una versión corregida basada en (5).
`H1c_LOCALIZATION (L') = OPEN`; no se promueven H1, E0 ni
`POWER_13/2_STABILITY`, y E/AdS sigue detenido. No se ejecutó código
numérico.
