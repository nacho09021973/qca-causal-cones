# Norma de la reconstrucción física P/Q sobre la salida normalizada

Fecha: 2026-09-24. Estado: `BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM`
al nivel **PRELIMINARY**, condicionado al lema de bloques Schur §2.
Alcance: sólo las cuatro normas
`||E^{1/2} V_c P t_N||`, `||E^{1/2} V_c Q t_N||`, `c=+,-`, y su uso
inmediato para acotar las diez piezas por Cauchy–Schwarz. No se cambia
Volterra, no se buscan cancelaciones y no se identifican términos líderes.

Este informe actualiza el resultado de la primera auditoría
`reports/2026-09-24--two-channel-physical-bound-transfer-audit.md`:
el STOP inicial localizó correctamente las normas que faltaban; la
presente estimación, usando la geometría explícita del efecto de Bob y
las cotas de bloques ya escritas, cierra ese hueco como cota superior.

## 1. Norma exacta del operador de reconstrucción

Del contrato en T1, §§2 y (6)–(8),
\[
(\mathcal V_c z)(y)=\mathbf1_{\mathcal B_N}(y)
e^{-\xi_*\cdot(y-y_*)}(\mathcal F^{-1}\pi_c z)(y),
\quad
d_{c,P/Q}=e^{-K_*N}\mathcal V_c(P/Q)t_N.
\]
El efecto del TeX plano, §3 y la definición del perfil Bob, es
\[
E=h_N\otimes M_B,\quad \|M_B\|=1,\quad
h_N(y)=\left(1-\frac{|y-Nu|^2}{R^2}\right)_+^2,
\quad R=N/4,\quad u=(1,1,1).
\]
Además, su representación inclinada fija
\(y_*=Nu-R\widehat u\), \(\widehat u=u/\sqrt3\), y
\(\xi_*=t_*u=\lambda\widehat u\), \(\lambda=\sqrt3t_*>0\).
Estas posiciones están en `papers/ir-corona/ir-corona.tex`, §§3,
exact tilted representation, y en T1 (6)–(8).

Como Fourier y la extracción de un canal tienen norma uno,
\[
\|E^{1/2}\mathcal V_c\|
=m_N:=\sup_{y\in\mathbb Z^3}
\sqrt{h_N(y)}e^{-\xi_*\cdot(y-y_*)}.
\]
Esta igualdad usa que \(M_B\) tiene autovalor máximo uno y que el
dominio permite cualquier función de Fourier L² en el canal elegido.
Para un y dentro de Bob, ponga
\(s=\widehat u\cdot(y-y_*)\) y descomponga
\(y-Nu=(s-R)\widehat u+q\), con \(q\perp\widehat u\). La condición
\(|y-Nu|\le R\) da \(0\le s\le2R\), y
\[
\sqrt{h_N(y)}
=\left(1-\frac{(s-R)^2+|q|^2}{R^2}\right)_+
\le \frac{2s}{R}-\frac{s^2}{R^2}
\le \frac{2s}{R}.
\]
Por ello
\[
0\le m_N\le\sup_{s\ge0}\frac{2s}{R}e^{-\lambda s}
=\frac{2}{e\lambda R}=\frac{8}{e\sqrt3t_*}\,N^{-1}.
\tag{1}
\]
El orden \(N^{-1}\) es ajustado para el operador sin P/Q: elija puntos
de red sobre la diagonal \(y=(m,m,m)\) con
\(s=\sqrt3(m-(y_*)_1)\) en un intervalo fijo positivo, por ejemplo
\([\sqrt3,2\sqrt3]\). Para N grande están dentro de Bob, con \(q=0\),
\(\sqrt{h_N}\ge c/N\), y el factor exponencial es uniformemente
positivo. Así \(m_N=\Theta(N^{-1})\). El factor exponencial de
desinclinación no hace crecer la norma: en la cara enfrentada donde
el peso sería máximo, \(h_N\) se anula; dentro, el peso decae.

Para W admisible y fijo, T1 §2 da
\(C_P(W)=\|P\|_{L^2\to L^2}<\infty\) y
\(C_Q(W)=\|Q\|_{L^2\to L^2}<\infty\), independientes de N. Por (1),
\[
\boxed{\|E^{1/2}\mathcal V_cP\|\le C_P(W)m_N=O_W(N^{-1}),\qquad
\|E^{1/2}\mathcal V_cQ\|\le C_Q(W)m_N=O_W(N^{-1}).}
\tag{2}
\]
Vale para ambos canales. No se afirma una cota inferior para ninguna
composición con P o Q.

## 2. Norma del vector normalizado actual

La fuente exacta T1 §1 es
\(s=\mathcal F H_\xi f\), con
\(f=J(U_M-I)\phi_N\), \(\|f\|\le2\), soportada en Alice.
Alice es la bola de radio R centrada en el origen y
\(x_*=R\widehat u\). Para todo x de Alice,
\(\xi_*\cdot(x-x_*)\le0\); luego el multiplicador \(H_\xi\) tiene
norma a lo sumo uno sobre el soporte de f y
\[
\|s\|_2=\|H_\xi f\|_2\le2.
\tag{3}
\]

No hace falta estimar Volterra. Se usan directamente las cotas de
bloques ya establecidas en la auditoría Schur, §2, ecuación (6): en
las normas P=L² y Q=\(\|\cdot\|_*\), uniformemente para N grande,
\[
\|A_j\|\le1+C/N,\quad \|B_j\|,\|C_j\|\le C/N,
\quad \|D_j\|_*\le\rho_2<1.
\]
(**[corregido 2026-09-25]** \(A_j\) sobre \(\operatorname{ran}P\), y los
bloques como aplicaciones entre rangos; ver
`2026-09-25--schur-block-stability-repaired.md`.)
En la norma producto \(\|x\|_2+\|y\|_*\), la recurrencia T1 (13)
queda acotada por \(1+C'/N\) paso a paso (absorbiendo la contracción
\(\rho_2\) y los dos bloques cruzados \(O(N^{-1})\)). Iterar N pasos
da una constante independiente de N. El dato inicial satisface
\(\nu_0=\|Ps\|_2+\|Qs\|_*\le(C_P(W)+C_0(W)C_Q(W))\|s\|\)
**[corregido 2026-09-25: la versión anterior, con \(C_P+C_Q\), ignoraba
la constante \(C_0\) de la norma \(\|\cdot\|_*\)]**. Por tanto
\[
\boxed{\|t_N\|_2\le C_{\rm stab}(W,\Theta)\|s\|_2
=O_{W,\Theta}(1),\quad\|\vartheta\|_\infty\le\Theta.}
\tag{4}
\]
Ésta es sólo estabilidad L² del producto ya normalizado, que sale de
las cotas de bloques Schur; no es una nueva cota de memoria ni una
afirmación sobre historias individuales. **[actualizado 2026-09-25]** La estabilidad (4) tiene ahora revisión
independiente documentada (ABNER/DeepSeek `PASS`; Astra/Ciro
`PASS_WITH_REPAIRS`, reparaciones aplicadas; ver
`2026-09-25--schur-block-stability-repaired.md` §5), con
\(O_{W,\Theta}(1)\) en lugar de \(O_W(1)\). Esa revisión se limitó a
(4); (5), (6) y las cotas por pieza que usan t_N son consecuencias
inmediatas de (2) y (4) que no se revisaron expresamente y conservan el
rótulo `PRELIMINARY`. En
cambio (1) y (2) son cotas operatoriales directas de la definición
geométrica, condicionadas sólo a W fijo y a la acotación P/Q de T1.

De (2) y (4), para c=+ y c=-,
\[
\boxed{\|E^{1/2}\mathcal V_cPt_N\|=O_{W,\Theta}(N^{-1}),\qquad
\|E^{1/2}\mathcal V_cQt_N\|=O_{W,\Theta}(N^{-1}).}
\tag{5}
\]
Al volver a las amplitudes físicas,
\[
\boxed{\|E^{1/2}d_{c,P}\|,
\|E^{1/2}d_{c,Q}\|=O_W(N^{-1}e^{-K_*N}).}
\tag{6}
\]
La fuente de la potencia \(N^{-1}\) es la norma del multiplicador
Bob ponderado en (1), no el antiguo retorno \(\mathbb M_N\) ni una
proyección de saddle. La cota es superior; no hay lower bound ni
asintótica equivalente para los vectores concretos \(t_N\).

## 3. Transferencia inmediata a las diez piezas

La unitariedad física y \(0\le E\le I\) dan
\(\|E^{1/2}r_c\|\le1\). Aplicando Cauchy–Schwarz a las identidades
exactas T1 (10a), sin cambiar los signos de las definiciones:
\[
|A_{cP}|,|A_{cQ}|=O_W(N^{-1}e^{-K_*N}),
\]
\[
0\le B_{cPP},B_{cQQ}=O_W(N^{-2}e^{-2K_*N}),\qquad
|B_{cPQ}|=O_W(N^{-2}e^{-2K_*N}),
\quad c=+,-.
\]
Estas son cotas superiores uniformes en N para W fijo, **condicionales
al lema de estabilidad preliminar Schur §2**; no se promueven a
`ESTABLISHED`. No son \(\sim\), no contienen lower bounds y no
identifican `LEADING_ASYMPTOTIC_TERM`. En particular, el operador bound no atribuye al observable el antiguo
\(O(N^{-6})\), que dependía de otros extremos y otro sandwich.

| TERM | BOUND | SOURCE | ASSUMPTIONS | EXPONENTIAL_SCALE | POWER_OF_N | SIGNED_INFORMATION_RETAINED | LOST_BY_ABSOLUTE_VALUE | STATUS |
|---|---|---|---|---|---|---|---|---|
| `A_{+P}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` en identidad | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{+Q}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; P→Q incluido; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+PP}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+QQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; borde Q sin historia separada; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+PQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; ambas salidas; Schur §2 | `e^-2K*N` | `N^-2` upper only | `Re` y signo | C–S pierde fase relativa | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{-P}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` en identidad | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{-Q}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; P→Q incluido; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-PP}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-QQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; borde Q sin historia separada; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-PQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; ambas salidas; Schur §2 | `e^-2K*N` | `N^-2` upper only | `Re` y signo | C–S pierde fase relativa | `PRELIMINARY_BOUNDS_TRANSFERRED` |

Memoria Q: ambas salidas P contienen entradas/retornos desde Q; la salida
Q contiene Q inicial y las salidas desde P, con historia de retornos en
los \(x_k\) (T1 (14)). La tabla no separa una contribución de
“permanencia P” ni atribuye historias. El mismo bound operatorial cubre
ambos canales porque extracción de canal tiene norma uno; no suma ni
cancela \(L_+\) y \(L_-\).

## 4. Límite de la conclusión

Los términos lineales tienen una envolvente exponencial menos pequeña
que la de los cuadráticos. Eso los hace candidatos naturales si una
lower bound posterior los mantiene en esa escala; la auditoría no prueba
dominancia, porque todos los resultados aquí son cotas superiores y
pueden ser estrictamente no ajustados. No se abre esa pregunta ahora.

```text
PRELIMINARY: BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM
```

No se ejecutaron scripts ni barridos. No se modificó el manuscrito.
No se hizo commit ni push.
