# C2: representación exacta y borde del corte IR

2026-09-22. Contrato:
[IR_ATTRIBUTION_C1_C2_C3_GATE](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md).
**REPRESENTATION_DERIVED / PRELIMINARY; PROJECTED_ASYMPTOTICS_OPEN.**
No se ejecutan nuevos diagnósticos ni se ajustan exponentes. Las fórmulas
discretas siguientes son exactas; la reducción Weyl posterior se distingue
expresamente del observable discreto. Esta derivación no tiene todavía
revisión independiente. C1 tiene una
[revisión analítica independiente separada, PASS](2026-09-22--c1-leakage-independent-review.md),
sin reparaciones pendientes. Su dictamen no cubre las fórmulas nuevas de C2.

## 1. El funcional que hay que calcular

Con las convenciones del manuscrito, escribimos
\[
a_N=(U_M-I)\phi_N,\quad r_N=S^N\phi_N,\quad d_{P,N}=S^NP a_N.
\]
Como `P phi_N=phi_N` y `[S,P]=0`,
\[
\boxed{L_{PP}(N)=2\operatorname{Re}\langle r_N,E d_{P,N}\rangle
                     +\langle d_{P,N},E d_{P,N}\rangle.}
\tag{1}
\]
Ambos términos son necesarios. Para `M_B=I`, el segundo es una suma
positiva de intensidades; no se presume que tenga la misma jerarquía que
en la respuesta total. El hecho de que el término cuadrático de L sea
exponencialmente subdominante no lo demuestra para Lpp.

## 2. Representación exacta en variables escaladas

Sea `u=(1,1,1)`, `b=1/4`, `K=sqrt(N)`, `Y=y/N`,
\[
h(Y)=(1-16|Y-u|^2)_+^2,\quad \chi=\downarrow,
\quad c_r=\frac{\sqrt{3465}}{64\pi^2},\quad g(k)=(1-|k|^2)_+^2.
\]
La fuente continua A_M es la función radial vectorial compacta de C1,
de modo que `a_N(x)=N^{-3/2} A_M(x/N)` **exactamente**. Su transformada
usa `Ahat(k)=integral exp(i k.X) A(X) dX`. Definamos
\[
\mathscr A_N(k)=\sum_{m\in\mathbb Z^3}\widehat A_M(k+2\pi Nm),
\qquad V_N(k)=S(k/N)^N.
\]
El periodo y las imágenes son los de la red original. Poisson da
`ahat_N(k/N)=N^{3/2} mathscr A_N(k)`; no se reemplaza el muestreo por
una integral sin sus imágenes. Con
\[
\begin{aligned}
\mathcal D_N(Y)&=\frac1{(2\pi)^3}\int_{|k|\le K}
 e^{-ik\cdot Y}V_N(k)\mathscr A_N(k)\,d^3k,\\
\mathcal R_N(Y)&=c_r\int_{|k|\le1}
 e^{-ik\cdot Y}V_N(k)g(k)\chi\,d^3k,
\end{aligned}
\tag{2}
\]
se tiene `d_{P,N}(y)=N^{-3/2} mathcal D_N(y/N)` y
`r_N(y)=N^{-3/2} mathcal R_N(y/N)`. Por tanto
\[
\boxed{L_{PP}=N^{-3}\sum_{y\in\mathbb Z^3}h(y/N)
\left[2\operatorname{Re}\bigl(\mathcal R_N(y/N)^\dagger M_B\mathcal D_N(y/N)\bigr)
 +\mathcal D_N(y/N)^\dagger M_B\mathcal D_N(y/N)\right].}
\tag{3}
\]
La suma es finita. (2)–(3) incluyen exactamente el símbolo, los aliases,
la fase de la red, el corte esférico móvil y ambos términos del funcional.
Las cuadraturas conservadas en la auditoría N=24,40 calculaban (1) en
variables no escaladas. La novedad de esta reorganización es exponer
separadamente las piezas para el análisis asintótico, no otro experimento.

## 3. No hay saddle real interior: hay una frontera espectral

Otra forma exacta, útil para no perder la separación espacial, es
\[
d_{P,N}(y)=\sum_{x\in\mathcal A_N}G_N^P(y-x)a_N(x),\qquad
G_N^P(d)=\int_{|p|\le N^{-1/2}}e^{-ip\cdot d}S(p)^N\frac{d^3p}{(2\pi)^3}.
\tag{4}
\]
Escribamos
\[
S(p)=f(p)I-i\,a(p)\cdot\sigma,\quad f=c_1c_2c_3,
\quad a=(s_1,-c_1s_2,c_1c_2s_3).
\]
Para `p != 0` dentro de la bola, `omega=arccos(f)` y
\[
S(p)^N=\sum_{\sigma=\pm1}e^{-i\sigma N\omega(p)}\mathsf P_\sigma(p),
\quad \mathsf P_\sigma=\tfrac12\left(I+\sigma\frac{a\cdot\boldsymbol\sigma}{\sin\omega}\right).
\]
Estos proyectores de banda no son los proyectores Riesz de H1. Si
`v=(y-x)/N`, las fases son `Psi_sigma(p)=p.v+sigma omega(p)` y
\[
|\nabla\Psi_\sigma|\ge |v|-|\nabla\omega|
\ge \sqrt3-\tfrac32=:\gamma>0.
\tag{5}
\]
Aquí sólo se usa la cota exacta `|grad omega|<=1` y la geometría original;
no la inclusión inversa del conjunto de velocidades. No hay punto
estacionario real interior para ninguno de los pares x,y.

En un anillo `epsilon<|p|<lambda`, sea
`b_sigma=grad Psi_sigma/|grad Psi_sigma|^2`. Una integración por partes da
\[
\int e^{-iN\Psi_\sigma}\mathsf P_\sigma\,d^3p
=\frac{i}{N}\left[
\int_{\partial\mathrm{anillo}}e^{-iN\Psi_\sigma}\mathsf P_\sigma
             b_\sigma\cdot n\,dS
-\int e^{-iN\Psi_\sigma}\operatorname{div}(\mathsf P_\sigma b_\sigma)\,d^3p
\right].
\tag{6}
\]
El flujo interior es `O(epsilon^2/N)` y desaparece al llevar epsilon a
cero. Los primeros derivados son `O(1/|p|)` y son integrables en dimensión
tres. El flujo exterior en `|p|=lambda` **permanece**. Iterar sin controlar
la singularidad de los proyectores en el nodo sería ilegítimo; la suma
matricial original sí es regular allí.

Una deformación al contorno complejo del cálculo de L debe arrastrar
esta frontera y sus contribuciones. Multiplicar el integrando inclinado
por una máscara real no analítica no es esa deformación. (5) tampoco
demuestra decaimiento exponencial de una integral con borde abrupto.

## 4. Referencia Weyl: reducción radial y términos del borde

Esta sección calcula un **término de comparación** de (2), no sustituye
el walk. Es útil para identificar qué debe controlarse antes de atribuir
un exponente a C2.

Definimos `H_W(k)=k1 sigma1-k2 sigma2+k3 sigma3`,
`V_W(k)=exp(-i H_W(k))`, y omitimos las imágenes sólo en la definición
del término de referencia
\[
\mathcal D_K^W(Y)=\frac1{(2\pi)^3}\int_{|k|\le K}
e^{-ik\cdot Y}V_W(k)\widehat A_M(k)\,d^3k.
\tag{7}
\]
Sean `rho=|Y|`, `J=H_W(Y/rho)`, `J^2=I`, y las funciones radiales
\[
s(r)=\Phi_0(r)\sin(\tfrac\pi2F(r)),\qquad
c(r)=\Phi_0(r)(\cos(\tfrac\pi2F(r))-1).
\]
Entonces `Ahat_M(k)=chat(k)chi+i shat(k)Mchi`, y la integral angular es
exacta:
\[
\mathcal D_K^W(Y)=\frac1{2\pi^2}\int_0^K k^2
\left[\cos k\,j_0(k\rho)I-\sin k\,j_1(k\rho)J\right]
\left[\widehat c(k)\chi+i\widehat s(k)M\chi\right]dk.
\tag{8}
\]
Se comprueban los signos usando
`integral exp(-ik n.Y)n dOmega=-4pi i j1(k rho)Y/rho`.

La evolución Weyl sin corte tiene velocidad de soporte uno. Esto se
deduce directamente de `cos(|D|)` y `sin(|D|)/|D|` de la ecuación de ondas,
seguidos por el operador diferencial H_W. Como la fuente tiene soporte
en radio b, `mathcal D_infinity^W(Y)=0` para `rho>1+b`. Toda la bola de
Bob cumple `rho>=sqrt(3)-b>1+b`. Así (8) equivale exactamente al negativo
de la integral entre K e infinito. La cancelación interior completa es
visible en esta representación.

Con `B=Phi_0(b)>0`, las integraciones radiales por partes dan
\[
\widehat s(k)=64\pi^2B\frac{\cos(bk)}{k^4}
             +\beta_5\frac{\sin(bk)}{k^5}+O(k^{-6}),
\qquad \widehat c(k)=O(k^{-6}),
\]
para una constante real beta5 que no se necesita aquí. El resto procede
de las derivadas interiores finitas en r=b; la paridad radial cancela los
términos espurios del origen. Usando las expresiones elementales de j0,j1
y `integral_K^infinity k^{-3}sin(tk)dk=K^{-3}cos(tK)/t+O(K^{-4})`,
obtenemos, uniformemente en la bola de Bob,
\[
\boxed{\mathcal D_K^W(Y)=
-\frac{i8B}{\rho K^3}
\sum_{\sigma=\pm1}\sum_{\epsilon=\pm1}
(I+\sigma J)M\chi\,
\frac{\cos[(\rho+\sigma+\epsilon b)K]}{\rho+\sigma+\epsilon b}
+O(K^{-4}).}
\tag{9}
\]
Todos los denominadores son mayores o iguales que gamma. El término
subdominante de shat produce `O(K^{-4})` por integración oscilatoria;
el resto `O(k^{-6})` y los términos subdominantes de j1 son también
controlables con ese orden. La fórmula es para el **campo de referencia**,
no para Lpp. No afirma una cota inferior uniforme: sus fases pueden cancelar.

## 5. Por qué (9) todavía no decide C2

Puede acotarse sin hipótesis extra el error de aproximación, pero una cota
absoluta elemental no basta a la escala de (9). Para este símbolo concreto
hay una mejora respecto al Taylor genérico del manuscrito:
\[
H(p)=\frac{\omega(p)}{\sin\omega(p)}a(p)\cdot\boldsymbol\sigma
=H_W(p)+O(|p|^3).
\]
El prefactor es analítico y par cerca del origen y a es impar; no existe
término cuadrático. Por Duhamel, para `|k|<=sqrt(N)`,
\[
\|V_N(k)-V_W(k)\|\le C\frac{|k|^3}{N^2}.
\]
Como `||Ahat(k)||<=C(1+|k|)^{-4}`, la estimación absoluta da
\[
\sup_Y\|\mathcal D_N(Y)-\mathcal D_K^W(Y)\|
\le\frac C{N^2}\int_0^K k^5(1+k)^{-4}dk
 + C N^{-4}K^3
=O(N^{-1})+O(N^{-5/2}).
\tag{10}
\]
El segundo término conserva explícitamente las imágenes de Poisson; su
cota procede de C1. En cambio (9) tiene escala `K^{-3}=N^{-3/2}`.
La cota (10) es **mayor** que el término que querríamos trasladar. No es
evidencia de un error real de orden N^{-1}; sólo señala la insuficiencia
del control absoluto disponible.

Incluso una mejora uniforme `o(N^{-3/2})` para el campo no decidiría por
sí sola todo (3): el funcional lineal puede cancelar tras sumar en Bob,
y el cuadrático podría entonces dominar. Hay que controlar ambos a la
escala del candidato final, incluyendo el error al convertir la suma en
integral. No se atribuye aquí una potencia ni una constante líder a Lpp.

## 6. Estado de C2 y obligaciones concretas

La representación limpia solicitada **sí existe**: (2)–(3), o (4) con
las fases (5). No tiene la misma geometría de contorno que L. El borde
del corte puede producir estructura algebraica/oscilatoria; por eso los
tres escenarios exponencial/exponencial diferente/nulo no agotan las
posibilidades del contrato.

Para cerrar C2 hay que:

1. controlar oscilatoriamente la diferencia del símbolo y las imágenes
   dentro del **funcional**, superando la cota absoluta (10);
2. calcular por separado el término lineal y el cuadrático en (3), con
   los errores de suma de red, antes de decidir cuál domina;
3. demostrar la no anulación del coeficiente que sobreviva, o demostrar
   la cancelación, con resto menor que ese término;
4. comparar la respuesta obtenida con L, sin sustituirla por Lcond.

**C2 = OPEN.** La representación exacta y el campo de referencia no son
una certificación de la asintótica discreta. C3 continúa separado y
E/AdS permanece detenido. Ninguno de estos cálculos implica una atribución
exclusivamente UV o una violación de microcausalidad.

## 7. Registro de los tres subgates al terminar esta continuación

- **C1: PASS / ONE_INDEPENDENT_ANALYTIC_REVIEW.** La revisión reconstruye
  el coeficiente positivo, los restos radiales, Poisson y las imágenes de
  red, además de la identidad de norma traza. Verificador auxiliar previo:
  27/27 PASS. El documento original de fuga se conserva byte por byte como
  entrada revisada; su etiqueta de no revisado corresponde al momento de
  redacción y el dictamen posterior está en el informe independiente.
- **C2: REPRESENTATION_DERIVED / ASYMPTOTICS_OPEN.** Las fórmulas de esta
  nota tienen nivel de derivación escrita, aún sin revisión independiente.
  No se ha asignado una ley asintótica al funcional discreto.
- **C3: SEPARATE_OBSERVABLE / NO_SUBSTITUTION_FOR_C2.** Se mantiene la
  identidad de condicionamiento previa; no se ha implementado ni revisado
  independientemente un experimento condicionado en esta continuación.

Este registro es evidencia local bajo el nuevo contrato, sin modificar
`state/CURRENT_STATE.md`, el manuscrito ni los gates de E/AdS. No se ha
añadido código ni ejecutado una nueva serie numérica. Contrato, nota C1 y
verificador conservan los hashes incluidos en la revisión independiente.
