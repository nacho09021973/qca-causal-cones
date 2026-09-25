# Extremos planos heredados: norma ℓ² inclinada O(N^{-3})

Fecha: 2026-09-25. Base: `863fe8e`. Autor de la derivación: Claude (familia
Anthropic).

Estado:

```text
FLAT_ENDPOINT_L2_N3_PASS — PRELIMINARY
```

Revisión: sanedrín de una ronda, sin turnos fallidos, con veredicto
`PASS_WITH_REPAIRS` por consenso. DeepSeek (abner) es el único revisor externo;
Opus es de la misma familia que el autor. Acta:
`debates/2026-09-25--flat-endpoint-l2-n3-review-opus-abner.md`. Las cuatro
reparaciones acordadas y la opcional sobre \(F_N\) están aplicadas aquí.

**Esto no es `N^{-7} PROVED`.** Ver §6.

## 1. Pregunta

¿Implican las fórmulas registradas, para los extremos planos heredados
\(f=s_Nb_N\chi\) y \(w=h_BM_Br\), la cota
\(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\), con
\[
\|f\|_{\ell^2_{\rm tilt}}^2=\sum_x e^{2\xi_*\cdot(x-x_*)}\|f(x)\|^2,\qquad
\|w\|_{\ell^2_{\rm tilt}}^2=\sum_y e^{-2\xi_*\cdot(y-y_*)}\|w(y)\|^2 ?
\]
La derivación no usa la masa ℓ¹ de `CURRENT_STATE` §9.2, la heurística
gaussiana \(\sqrt N\), el "soporte efectivo" ni el Lema 3 del informe regional.

## 2. Definiciones usadas

- `papers/ir-corona/ir-corona.tex` §3:
  \(\hat\phi_N(p)=Z_N^{-1/2}g(Np)\downarrow\), con \(g(q)=(1-|q|^2)_+^2\ge0\),
  \(Z_N=64/(3465\pi^2N^3)\) y \(d\mu=d^3p/(2\pi)^3\) (l. 282–284).
  \(F_N(x)=(1-16|x|^2/N^2)_+^2\), \(s_N=\sin(\pi F_N/2)\),
  \(h_N(y)=(1-16|y-Nu|^2/N^2)_+^2\) y \(M_B\in\{I,(I+\sigma_j)/2\}\).
- `reports/2026-09-17--regional-laplace-coefficient-gate.md` §3.2:
  \(x=x_*-\delta\hat u+u\), \(\delta=(\theta_N+j)/\sqrt3\),
  \(j\in\mathbb Z_{\ge0}\), \(\theta_N\in[0,1)\); Bob análogo con \(\delta'\).
  \(\xi_*\cdot(y-x)=N\xi_*\cdot v_*+t_*(2\theta_N+j+j')\), con
  \(t_*=0.735752\ldots>0\).
  §7: \(\varepsilon_\perp=\delta-\delta^2/2R-|u|^2/2R\), \(R=N/4\).
- `reports/2026-09-17--scaled-ir-signaling-gate.md` §3:
  \(|\phi_N(0)|^2=11/(140\pi^2N^3)\).

## 3. Cota puntual

**(a)** \(\phi_N=b_N\downarrow\) con
\(b_N(x)=Z_N^{-1/2}\int g(Np)e^{-ip\cdot x}d\mu\). Como \(g\ge0\),
\(\sup_{x\in\mathbb Z^3}|b_N(x)|=b_N(0)=c_\phi N^{-3/2}\), con
\(c_\phi=\sqrt{11/140}/\pi=0.08922\ldots\)

**(b)** \(r(y)=\int e^{-ip\cdot y}S(p)^N\hat\phi_N(p)d\mu\). \(S(p)\) es
unitaria en el toro real, luego \(\sup_y\|r(y)\|\le\int\|\hat\phi_N\|d\mu=c_\phi N^{-3/2}\).

**(c)** \(0\le F_N\le1\) por definición. Además
\(1-16|x|^2/N^2=(R^2-|x|^2)/R^2=8\varepsilon_\perp/N\), luego
\(F_N=64\varepsilon_\perp^2/N^2\) exactamente. Con
\(0\le\varepsilon_\perp\le\delta\):
\(|s_N|\le\tfrac\pi2F_N\le32\pi\delta^2/N^2\). En Bob,
\(h_N\le64\delta'^2/N^2\) y \(\|M_B\|\le1\).

**(d)** \(\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)\) y
\(-\xi_*\cdot(y-y_*)=-t_*(\theta_N+j')\). Con \(\delta\le(1+j)/\sqrt3\):
\[
e^{\xi_*\cdot(x-x_*)}\|f(x)\|\le a_f\,N^{-7/2}(1+j)^2e^{-t_*j},\qquad
e^{-\xi_*\cdot(y-y_*)}\|w(y)\|\le a_w\,N^{-7/2}(1+j')^2e^{-t_*j'},
\]
con \(a_f=\tfrac{32\pi}{3}c_\phi=2.990\ldots\) y
\(a_w=\tfrac{64}{3}c_\phi=1.903\ldots\). Las cotas son uniformes en \(u\) y
en \(N\); la dependencia en \(j\) queda explícita.

## 4. Suma cuadrática

Cada plano de profundidad \(j\) es un trasladado de
\(\Lambda_0=\mathbb Z^3\cap\{x_1+x_2+x_3=0\}\), con covolumen \(\sqrt3\) y
celda generada por \((1,-1,0)\) y \((0,1,-1)\). Tomamos el diámetro de la celda
como \(\sqrt6\), que es conservador. El soporte en el plano es un disco de radio
\(\rho_j\le\sqrt{2R\delta}\). Así, para \(N\ge1\),
\[
\#_j\le\frac{\pi(\rho_j+\sqrt6)^2}{\sqrt3}
\le\frac{2\pi}{\sqrt3}\Bigl(\frac{N(1+j)}{2\sqrt3}+6\Bigr)
\le k\,N(1+j),\qquad k=\frac{2\pi}{\sqrt3}\Bigl(\frac1{2\sqrt3}+6\Bigr).
\]
Por tanto
\[
\|f\|_{\ell^2_{\rm tilt}}^2\le k\,a_f^2\,N^{-6}\sum_{j\ge0}(1+j)^5e^{-2t_*j},
\qquad \sum_{j\ge0}(1+j)^5e^{-2t_*j}=51.48\ldots
\]
Es decir, \(q(j)=(1+j)^4e^{-2t_*j}\) con \(\sum(1+j)q(j)<\infty\).
Para \(N\ge1\):
\[
\boxed{\|f\|_{\ell^2_{\rm tilt}}\le103\,N^{-3},\qquad
\|w\|_{\ell^2_{\rm tilt}}\le66\,N^{-3}.}
\]
Las constantes son burdas y no óptimas; no hay cota inferior. Opus propuso una
saturación \(\gtrsim cN^{-6}\), que queda como [UNVERIFIED]: exige comprobar
\(\varphi_\partial\neq0\) en la capa \(j=1\).

## 5. Norma de Schur (8), componente P

Dyson §2 y Volterra usan \(D_\xi(\eta)=D(\eta-i\xi_*)\), los centros
\(x_*,y_*\), \(\Lambda=e^{\Phi_*}\) y \(K_*=\xi_*\cdot v_*-\Phi_*\). Con
\(\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x)\) y
\(d\mu=d^3p/(2\pi)^3\), Parseval da exactamente
\(\|\mathfrak A_f\|_{L^2(d\mu)}=\|f\|_{\ell^2_{\rm tilt}}\); igual para
\(\mathfrak B_w\). Las fases \(e^{i\eta\cdot x_*}\) y \(e^{-i\eta\cdot y_*}\) son
unimodulares.

Lo verificado se limita a la **componente P** que entra en (8):
\(\|P\mathfrak A_f\|_{L^2}\le C_P\|f\|_{\ell^2_{\rm tilt}}\), con
\(C_P=\sup_p\|P(p)\|<\infty\) (multiplicador acotado, Schur §2); igual para
Bob. No se afirma compatibilidad para la parte Q de los extremos: (8) no la
controla (T2).

## 6. Alcance y lo que no se afirma

- **Cubierto:** los extremos planos heredados \(f,w\).
- **No transferido al contrato de dos canales.** La fuente de T1 es
  \(J(U_M-I)\phi_N\); no se ha comprobado.
- **No transferido a \(r_c=BU_N^NJ\phi_N\).** El paso 3(b) usa la invariancia
  por traslación del walk libre. \(U_N\) contiene \(C_N(X)\), que no la tiene.
- **La cuenta \(N^{-3}\cdot N^{-1}\cdot N^{-3}\) no está instalada en ninguna
  pieza firmada del contrato actual.** T2 es `BOUND_NOT_TRANSFERRED`, T3 es
  `STOPPED_NO_SIGNED_TERM`, el extremo de Bob del observable es \(r_c\) y no
  \(w\), y Schur (8) es PRELIMINARY.
- **Margen nulo.** Aunque se instalara, \(e^{-K_*N}N^{-7}\) coincide con el
  resto absoluto ya presente en el líder plano: informe regional §13,
  \(|R_N|\le C'N^{-1/2}\) sobre \(e^{-K_*N}N^{-13/2}\), con \(C'\) no explícita.
  La holgura frente a ese resto es \(N^0\). Una corrección \(O(N^{-7})\) queda
  por debajo del líder, pero no por debajo del resto conocido.

No se ejecutó código salvo el cálculo aritmético de \(a_f,a_w,k\) y de la serie.
No se modifican Schur, Volterra, H1c, T1–T3 ni las piezas lineales.
