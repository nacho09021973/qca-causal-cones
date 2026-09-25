# H1c: precheck del núcleo de memoria Volterra

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Objeto: probar o matar la ruta de memoria P/Q en el elemento Alice/Bob
inclinado. `H1c_LOCALIZATION (L') = OPEN`.

**Cierre documental del día:** este precheck precede a la decisión
operacional de [el cierre H1c, §§6–8](2026-09-24--h1c-return-kernel-schur-audit.md).
Las carencias físicas descritas abajo son el diagnóstico previo; el nuevo
contrato fija `(L_+, L_-)`, pero su lift exacto al P/Q de este informe sigue
pendiente en T1. Volterra/localización asintótica está PAUSED; estas
identidades para extremos genéricos no son por sí solas el lift firmado.

## 1. Identidad finita y cuantificadores

Fijada una partición `P_j(p)+Q_j(p)=I` en cada capa de momento, sean
`A_j=P_{j+1}T_jP_j`, `B_j=P_{j+1}T_jQ_j`, `C_j=Q_{j+1}T_jP_j` y
`D_j=Q_{j+1}T_jQ_j`. Estos son operadores integrales entre capas;
sus argumentos de entrada y salida pueden tener momentos distintos.
Escribiendo `x_j=P_j\psi_j`, `y_j=Q_j\psi_j`, se tiene exactamente
\[
x_{j+1}=A_jx_j+B_jy_j,\qquad
y_{j+1}=C_jx_j+D_jy_j.
\tag{1}
\]
Para `j\ge k`, `G_Q(j,k)=D_{j-1}\cdots D_k` y
`G_Q(k,k)=I` en el espacio Q de la capa `k`. La eliminación exacta es
\[
y_j=G_Q(j,0)y_0+
\sum_{k=0}^{j-1}G_Q(j,k+1)C_kx_k,
\tag{2}
\]
\[
x_{j+1}=A_jx_j+B_jG_Q(j,0)y_0
 +\sum_{k=0}^{j-1}K_{j,k}x_k,
\quad K_{j,k}=B_jG_Q(j,k+1)C_k.
\tag{3}
\]
En particular, `K_{k+1,k}=B_{k+1}C_k`: no hay paso Q interno.

Para evitar esconder el transporte P, definamos
`\Phi_P(j,k)=A_{j-1}\cdots A_k`, `\Phi_P(k,k)=I` en P. La forma
Volterra exacta para `0\le j\le N` es
\[
x_j=x_j^{(0)}+f_{Q,j}+(\mathbb M_Nx)_j,
\qquad x_j^{(0)}=\Phi_P(j,0)x_0,
\tag{4}
\]
\[
f_{Q,j}=\sum_{m=0}^{j-1}
\Phi_P(j,m+1)B_mG_Q(m,0)y_0,
\tag{5}
\]
\[
(\mathbb M_Nx)_j
=\sum_{m=0}^{j-1}\sum_{k=0}^{m-1}
\Phi_P(j,m+1)B_mG_Q(m,k+1)C_kx_k.
\tag{6}
\]
`\mathbb M_N` es estrictamente triangular en tiempo; por tanto
`(I-\mathbb M_N)^{-1}` existe como polinomio finito y
\[
x=(I-\mathbb M_N)^{-1}(x^{(0)}+f_Q).
\tag{7}
\]
Las excursiones repetidas están incluidas en (7). La salida Q sigue
siendo una obligación separada:
\[
y_N=G_Q(N,0)y_0+
\sum_{k=0}^{N-1}G_Q(N,k+1)C_kx_k,
\quad L_N=\ell_Px_N+\ell_Qy_N.
\tag{8}
\]

La identidad requiere una partición P/Q definida en todos los momentos
que visitan los kernels. El Riesz projector del proyecto sólo está
controlado en ventanas locales (`state/CURRENT_STATE.md`, §9.1).
Una extensión fuera de ellas es una elección auxiliar y sus cruces
deben entrar en `A,B,C,D`. Además siguen sin fijarse los extremos
físicos de cuatro componentes y el funcional final de `L'`; (1)-(8)
son identidades para extremos genéricos.

## 2. Primer núcleo no nulo con el kernel exacto

Trabajamos en una ventana local del símbolo libre inclinado
`D_\xi(p)=\lambda(p)P(p)+\lambda(p)^{-1}Q(p)` y fijamos la
normalización **escalar global** `\Lambda=e^{\Phi_*}`. Así se conserva
la relación con el elemento físico inclinado; dividir por
`\lambda(p)` en cada paso y cada momento sería otra dinámica y
exigiría reponer su cociclo. Pongamos
\[
a(p)=\lambda(p)/\Lambda,\qquad
d(p)=\lambda(p)^{-1}/\Lambda,\qquad
\Theta_N(q)=\sum_{x\in\mathbb Z^3}e^{iq\cdot x}\vartheta(x/N).
\tag{9}
\]
El kernel de un paso es exactamente
`T(p',p)=\delta(p'-p)D_\xi(p)/\Lambda+
\widehat M_N(p'-p)D_\xi(p)/\Lambda`, con
`M_N=e^{-i\vartheta\beta/N}-I`. Su parte impar lineal en la moneda
da, a primer orden en `1/N`,
\[
C^{(1)}(r,p)
=-\frac{i}{N}\Theta_N(r-p)a(p)
 Q(r)\beta P(p),
\tag{10}
\]
\[
B^{(1)}(p',r)
=-\frac{i}{N}\Theta_N(p'-r)d(r)
 P(p')\beta Q(r).
\tag{11}
\]
La parte libre Q entre ambos factores conserva el momento y, para
`h=j-k\ge1`, aporta `d(r)^{h-1}Q(r)`. Por tanto el primer término
cuadrático de la memoria, para `h` **fijo**, es
\[
\boxed{
K_{j,k}^{(2)}(p',p)
=-\frac{a(p)}{N^2}
\int_{\mathbb T^3}
\Theta_N(p'-r)\Theta_N(r-p)
d(r)^h
P(p')\beta Q(r)\beta P(p)\,d\mu(r).
}
\tag{12}
\]
La fórmula conserva ambos saltos de momento. Es el término de dos
factores impares del **kernel exacto**; no convierte
`\Theta_N` en una delta. El resto de la expansión a `h` fijo no
establece uniformidad para `h=O(N)` ni control fuera de las ventanas.
La afirmación `K_{j,k}=O(N^{-2})` se refiere aquí a la norma de
operador de una excursión con separación fija y propagación Q
controlada; el valor puntual de `\Theta_N` puede crecer como `N^3`.

Como segunda comprobación, si la moneda es globalmente constante
`\vartheta=\theta`, el kernel se hace diagonal en momento. En el
saddle `p'=p=0`, `a(0)=1`, `d(0)=\Lambda^{-2}` y
`P\beta Q\beta P=P`; el **coeficiente de la delta diagonal** de
(12) en esa fibra se reduce a
\[
K_{j,k}^{(2)}(0,0)
=-\frac{\theta^2}{N^2}\Lambda^{-2h}P.
\tag{13}
\]
Sumar las `N-h` posiciones de cada pareja da
`-\theta^2/[N(\Lambda^2-1)]P+O(N^{-2})`, de acuerdo con el
cálculo Dyson independiente en
`reports/2026-09-24--h1c-dyson-pair-audit.md`.
Un perfil suave con meseta constante sobre los caminos Alice/Bob
reproduce ese test para el elemento pertinente, aunque su kernel
global no sea diagonal.

## 3. Qué falta para una cota de susceptibilidad

La propuesta `\chi_N=\|\mathbb M_N\|_{w\to w}` es un criterio
condicional claro **después** de fijar una envolvente `w_j>0` para
el elemento inclinado y una norma de los campos en momento.
Como (7) es finita, `\chi_N<1` implica
`\|(I-\mathbb M_N)^{-1}\|_{w\to w}\le(1-\chi_N)^{-1}`.
El orden `N^{-2}` de (12) para cada pareja no prueba
`\chi_N=O(N^{-1})`. Una cota de ese tipo requeriría, uniformemente
en ventanas y pesos elegidos, controlar:

1. el transporte `\Phi_P(j,m+1)` con el tilt y las fases físicas;
2. la suma en duración de `G_Q(m,k+1)` con momentos variables y
   posibles picos no normales;
3. la suma en `m,k`, que cuenta `O(N)` posiciones aun cuando las
   duraciones Q sean sumables;
4. interfaces de ventanas y contribuciones fuera de ellas.

Bajo **hipótesis adicionales** de transporte P ponderado uniforme,
dos acoplamientos mixtos `O(N^{-1})` en la norma apropiada y suma
Q ponderada uniforme, (6) permite una cota `O(N^{-1})`: una suma
temporal de `O(N)` posiciones multiplica el coste `O(N^{-2})` de
cada excursión. Ninguna de esas hipótesis globales está demostrada
para el elemento Alice/Bob de `L'`. Su líder firmado también puede
cancelar, de modo que `\chi_N=o(1)` no implica por sí solo
que el complemento sea `o(|L'_{N,P}|)`.

Los bordes no están incluidos en `\chi_N`: hay que estimar `f_Q`
y los dos términos Q de (8) con los extremos físicos. El test plano
embebido de `reports/2026-09-24--h1c-kernel-excursion-resolvent-audit.md`,
§3, muestra que `s_Q,\ell_Q` no reciben automáticamente una
potencia extra de N.

## 4. Estado del precheck

El núcleo (12) es un candidato concreto de orden dos para una
excursión interna y es no nulo en el test de fibra constante (13).
La ecuación Volterra (1)-(8) incluye
exactamente excursiones repetidas y bordes Q. Es una ruta
algebraicamente consistente para un gate de H1c, condicionada a
la partición global, los extremos físicos, la envolvente `w` y
las cotas de transporte/sumabilidad indicadas. No se promueve
`H1c_LOCALIZATION (L')`: el control uniforme de momentos variables
y regiones sin Riesz splitting sigue abierto.

No se ejecutó código numérico, ni se modificaron C2c, el manuscrito,
`state/CURRENT_STATE.md`, E0 o E/AdS.
