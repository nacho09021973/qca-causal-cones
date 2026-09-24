# H1c: descomposición exacta y gate de la ganancia ausente

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Objeto: el elemento Alice/Bob inclinado del walk doblado. Este documento
formula un **precheck interno de H1c**; no cambia `CURRENT_STATE.md`.

**Cierre documental del día:** el precheck siguiente precede al contrato
operacional fijado en [el cierre H1c, §§6–8](2026-09-24--h1c-return-kernel-schur-audit.md),
ahora resumido en `CURRENT_STATE.md`. Las carencias de definición descritas
abajo corresponden a aquella etapa. El lift firmado a P/Q sigue pendiente
en T1; Volterra/localización asintótica está PAUSED. No se transfiere este
test de extremos fijos a `(L_+, L_-)` sin ese lift.

## 1. Qué está fijado y qué falta fijar

`state/CURRENT_STATE.md`, §9, fija `D`, `C_N` y el contrato de `\beta`;
la reconstrucción H1, §1, escribe el producto `C_ND`:
\[
D=S\oplus S^{-1},\qquad
U_N=C_N(x)D,\qquad C_N(x)=e^{-i\vartheta(x/N)\beta/N},
\qquad \beta^2=I,\quad \beta D\beta=D^{-1}.
\]
La reconstrucción H1, §8, exige un elemento Alice/Bob exacto y su §9
propone una cota para `T_n`, pero no define `T_n` mediante extremos de
cuatro componentes ni fija su funcional final. El TeX plano, §7.3,
define extremos de dos componentes y una identidad inclinada exacta.
Por ello, en lo que sigue `f_N,w_N` son **extremos arbitrarios de cuatro
componentes** con los soportes Alice/Bob planos. La elección
`(f_N,0),(w_N,0)` es un test admisible de la formulación general, pero no
se identifica sin más con todos los extremos de una extensión física.
Si la referencia de Bob depende a su vez de `U_N`, habrá que expandir
también esa dependencia: (1) corresponde a extremos fijados antes de
variar el propagador.

Póngase `V_N=(C_N-I)D`, de modo que `U_N=D+V_N`. Con el funcional complejo
\[
\mathfrak L_N(f_N,w_N)
:=e^{K_*N}\langle w_N,U_N^Nf_N\rangle,
\]
la identidad no conmutativa exacta es
\[
\mathfrak L_N=\sum_{n=0}^{N}\mathfrak L_{N,n},\qquad
\mathfrak L_{N,n}
=e^{K_*N}\sum_{\substack{m_0,\ldots,m_n\ge0\\
                         m_0+\cdots+m_n=N-n}}
\left\langle w_N,
D^{m_n}V_ND^{m_{n-1}}V_N\cdots V_ND^{m_0}f_N
\right\rangle .
\tag{1}
\]
Para `n=0` se entiende `\mathfrak L_{N,0}=e^{K_*N}\langle w_N,D^Nf_N\rangle`.
Así queda definido qué significa **número de inserciones Dyson crudas**.
La probabilidad o diferencia firmada del protocolo se obtiene después
aplicando el funcional de interferencia pertinente; no debe sustituirse
este elemento complejo por una norma.

## 2. Representación inclinada con momentos variables

Fijemos la convención de Fourier del TeX plano, §7.3, y sus centros
`x_*`, `y_*`, con `y_*-x_*=Nv_*` y
`K_*=\xi_*\cdot v_*-\Phi_*`. Denotemos por
`\mathfrak A_f(\eta)` y `\mathfrak B_w(\eta)` las transformadas centradas
e inclinadas allí definidas, ahora para cuatro componentes. Sea
`D_\xi(\eta)=D(\eta-i\xi_*)`. Para `\vartheta\in C_c^\infty`, el
multiplicador `M_N(x)=C_N(x)-I` tiene núcleo toroidal exacto
\[
\widehat M_N(q)=\sum_{x\in\mathbb Z^3}e^{iq\cdot x}M_N(x),
\qquad q\in\mathbb T^3.
\tag{2}
\]
Esta es una suma finita para cada `N`; no se reemplaza por
`N^3\widehat\vartheta(Nq)` en la identidad exacta. Para
`m_0,\ldots,m_n\ge0` con `\sum m_a=N-n`, la contribución de (1) es
\[
\begin{aligned}
\mathfrak L_{N,n}
=e^{-N\Phi_*}\!\sum_{m_0+\cdots+m_n=N-n}
\int_{(\mathbb T^3)^{n+1}}&
\mathfrak B_w(\eta_n)
e^{-i\eta_n\cdot y_*+i\eta_0\cdot x_*}
D_\xi(\eta_n)^{m_n}\\[-2pt]
&\widehat M_N(\eta_n-\eta_{n-1})
D_\xi(\eta_{n-1})^{m_{n-1}+1}\cdots\\[-2pt]
&\widehat M_N(\eta_1-\eta_0)
D_\xi(\eta_0)^{m_0+1}
\mathfrak A_f(\eta_0)\,d\mu^{n+1}.
\end{aligned}
\tag{3}
\]
Con el convenio de producto vacío, para `n=0` (3) se reduce exactamente
a la representación plana del TeX con `D_\xi^N`. La fase tiene **dos
momentos extremos distintos** cuando `n\ge1`;
`e^{-iN\eta\cdot v_*}` sólo aparece cuando todos los momentos coinciden.
La moneda local conmuta con la inclinación, pero su núcleo de Fourier
permite `\eta_{a-1}\ne\eta_a`. (3) no presume conservación de momento.
Como caso límite, `N=n=1` deja `m_0=m_1=0` y (3) representa exactamente
`e^{K_*}\langle w_N,(C_N-I)Df_N\rangle`.

La moneda se separa exactamente en paridad de `\beta`:
\[
M_N(x)=\underbrace{[\cos(\vartheta(x/N)/N)-1]I}_{M_N^{\rm e}}
\;\underbrace{-i\sin(\vartheta(x/N)/N)\beta}_{M_N^{\rm o}}.
\tag{4}
\]
La parte par es `O(N^{-2})` por paso; la impar es `O(N^{-1})`.
En una ventana de Riesz, `\mathcal P(\eta)\beta\mathcal P(\eta)=0`,
pero `\mathcal P(\eta')\beta\mathcal P(\eta)=O(|\eta'-\eta|)` sólo
controla la transición dominante a dominante. Las excursiones
`\mathcal P\to\mathcal Q\to\mathcal P` de dos factores impares no
contienen necesariamente ese factor de diferencia de momentos.

## 3. Tres ubicaciones posibles de la ganancia

La descomposición (1)-(4) permite separar afirmaciones diferentes:

1. **Término crudo:** cada `\mathfrak L_{N,n}` satisface la cota
   `N^{-13/2}(C'/N)^n/n!`. El precheck de pareja en
   `reports/2026-09-24--h1c-dyson-target-check.md` contradice esta
   lectura para `n=2` en el test con moneda constante sobre los caminos,
   siempre que se permita el embedding plano y el líder plano no nulo.
2. **Suma Dyson:** sólo `\sum_{n\ge1}\mathfrak L_{N,n}`, posiblemente
   tras aplicar el funcional físico, obtiene una ganancia adicional por
   cancelación entre paridad par, pares de factores impares y otros
   términos. Esto no se sigue de `\mathcal P\beta\mathcal P=0`.
3. **Transferencia de momento/localización:** el núcleo de (2) y las fases
   de (3) producen una ganancia que no existe en el caso constante.
   Hay que demostrarla para el elemento completo, incluyendo visitas a
   `\mathcal Q`, transiciones entre las ocho ventanas y el exterior.

La expresión “ganancia adicional” requiere fijar **respecto a qué cota
del elemento completo** se mide. El único objetivo numérico escrito en
`CURRENT_STATE.md`, §9.4, es la cota por `n` de la primera fila, ya
cuestionada. Este precheck no reemplaza esa fórmula por otro exponente.

## 4. Kill-test de moneda constante para la suma

Sea `\vartheta` suave, compactamente soportada e igual a
`\theta\ne0` en `[-2,2]^3`. Para los extremos planos embebidos en la
primera componente, todos los caminos de `N` pasos ven la moneda
constante `e^{-i\theta\beta/N}`. En cada par de haces recíprocos,
\[
\operatorname{tr}(e^{-i\theta\beta/N}D)
=\cos(\theta/N)(\lambda+\lambda^{-1}),\quad
\log(\mu_+/\lambda)
=-\frac{\theta^2}{2N^2}
\frac{\lambda^2+1}{\lambda^2-1}+O(N^{-4}).
\tag{5}
\]
Al sumar `N` pasos, el coeficiente dominante de segundo orden es
\[
-\frac{\theta^2}{N}
\left[\frac12+\frac1{\lambda^2-1}\right].
\tag{6}
\]
El primer sumando procede de una inserción de `M_N^{\rm e}`: su bloque
dominante es exactamente
`N[\cos(\theta/N)-1]\lambda^N\mathcal P`
al primer orden no nulo. El segundo procede de dos inserciones de
`M_N^{\rm o}` y una excursión por `\mathcal Q`, cuya suma temporal es la
de (1) en `reports/2026-09-24--h1c-dyson-target-check.md`.
Para `\lambda^2=e^{2\Phi_*}>1`, ambos tienen el mismo signo. En la
primera componente no hay término impar lineal; la compresión del
proyector dominante perturbado cambia sólo en orden `N^{-2}` por paridad:
`\Gamma=\operatorname{diag}(I_2,-I_2)` conmuta con `D` y lleva
`\beta\mapsto-\beta`, mientras deja fija esa compresión.
Así, **la suma completa del propagador con extremos fijados tampoco
cancela universalmente el orden relativo `N^{-1}`** en este test. Los
dos saddles principales reciben el
mismo factor (6); para el par plano `(\sigma_2,I)` el coeficiente de
interferencia es uniformemente no nulo según el TeX, §7.3 y su
certificado en `reports/2026-09-17--regional-laplace-coefficient-gate.md`.

Esto es un test estructural de la formulación uniforme: el perfil es
globalmente variable pero exactamente constante en los caminos
relevantes. Una posible ganancia debida a variación espacial sólo puede
ser una afirmación con hipótesis que excluyan este perfil, o referirse a
otro observable/otra combinación de extremos. No se impone ninguna de
esas restricciones aquí.

## 5. Precheck único dentro de H1c

**Pregunta:** fijados los extremos de cuatro componentes y el funcional
final del `L'` real, ¿qué cota necesita el elemento completo de (1), y
puede demostrarse mediante (3) después de sumar/localizar los momentos
variables, sin contradecir (5)-(6)?

**Salidas discriminantes, todavía abiertas:**

- La cota requerida es compatible con una corrección relativa `O(N^{-1})`:
  la pareja constante no la refuta; falta probar el control global del
  elemento completo a momento variable.
- La cota requerida exige `o(N^{-1})` para los extremos y perfiles
  admitidos: el test constante con embedding plano la refuta si éstos
  pertenecen a la clase congelada; de lo contrario debe explicitarse la
  diferencia de clase o funcional.
- La cota se obtiene para otra combinación física por cancelación:
  exhibir la identidad exacta de esa combinación, incluida una eventual
  dependencia de la referencia Bob respecto de `U_N`, **antes** de estimar,
  y verificarla en el test constante y en (3).

`H1c_LOCALIZATION (L') = OPEN`. No se promueve H1 ni se modifica C2c,
E0, `POWER_13/2_STABILITY`, E/AdS o el manuscrito. No se ejecutó código
numérico ni se usó el barrido antiguo de C2c.
