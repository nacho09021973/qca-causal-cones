# Extremos planos heredados: norma ℓ² inclinada O(N^{-3})

Fecha: 2026-09-25. **BORRADOR para revisión independiente. No commiteado.**
Autor: Claude (familia Anthropic). Estado propuesto:
`FLAT_ENDPOINT_L2_N3_PASS — PRELIMINARY`. Base: `863fe8e`.

**Esto no es `N^{-7} PROVED`.** Siguen abiertos Schur (8), que es PRELIMINARY,
y la transferencia al contrato de dos canales y a \(r_c\).

## Pregunta

¿Las estimaciones registradas implican, para los extremos planos heredados
\(f=s_Nb_N\chi\) y \(w=h_BM_Br\), la cota
\(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\), con
\[
\|f\|_{\ell^2_{\rm tilt}}^2=\sum_x e^{2\xi_*\cdot(x-x_*)}\|f(x)\|^2,\qquad
\|w\|_{\ell^2_{\rm tilt}}^2=\sum_y e^{-2\xi_*\cdot(y-y_*)}\|w(y)\|^2 ?
\]
No se usan la masa ℓ¹ de §9.2, la heurística gaussiana \(\sqrt N\), el
"soporte efectivo" ni el Lema 3 del informe regional.

## Datos de partida (definiciones exactas)

- TeX §3: \(\hat\phi_N(p)=Z_N^{-1/2}g(Np)\downarrow\), con
  \(g(q)=(1-|q|^2)_+^2\ge0\), \(Z_N=64/(3465\pi^2N^3)\) y
  \(d\mu=d^3p/(2\pi)^3\) (l. 282–284).
- TeX §3: \(F_N(x)=(1-16|x|^2/N^2)_+^2\), soportado en \(\mathcal A_N\)
  (bola de radio \(R=N/4\)); \(s_N=\sin(\pi F_N/2)\);
  \(h_N(y)=(1-16|y-Nu|^2/N^2)_+^2\); \(M_B\in\{I,(I+\sigma_j)/2\}\).
- Informe regional 2026-09-17, §3.2: \(x=x_*-\delta\hat u+u\),
  \(\delta=(\theta_N+j)/\sqrt3\), \(j\in\mathbb Z_{\ge0}\), \(u\perp\hat u\),
  \(\theta_N\in[0,1)\); Bob igual con \(\delta',u'\);
  \(\xi_*\cdot(y-x)=N\xi_*\cdot v_*+t_*(2\theta_N+j+j')\), \(t_*=0.7357\ldots>0\).
- Informe regional, §7: \(F_N=64\varepsilon_\perp^2/N^2\),
  \(\varepsilon_\perp=\delta-\delta^2/2R-|u|^2/2R\).

## Paso 1: cota puntual

**(1a)** \(\phi_N=b_N\downarrow\) con
\(b_N(x)=Z_N^{-1/2}\int g(Np)e^{-ip\cdot x}d\mu\). Como \(g\ge0\),
\[
\sup_{x\in\mathbb Z^3}|b_N(x)|\le Z_N^{-1/2}\!\int g(Np)\,d\mu=b_N(0)=c_\phi N^{-3/2},
\qquad c_\phi=\sqrt{11/140}/\pi,
\]
usando \(|\phi_N(0)|^2=11/(140\pi^2N^3)\) (scaled-IR §3).

**(1b)** \(r=P_BS^N\phi_N\), con
\(r(y)=\int e^{-ip\cdot y}S(p)^N\hat\phi_N(p)d\mu\). Como \(S(p)\) es
unitaria en el toro real, \(\|S(p)^N\|=1\) y
\(\sup_y\|r(y)\|\le\int\|\hat\phi_N\|d\mu=c_\phi N^{-3/2}\). No se usa el
Lema 3.

**(1c)** Perfiles. En Alice,
\(1-16|x|^2/N^2=(R^2-|x|^2)/R^2=2\varepsilon_\perp/R=8\varepsilon_\perp/N\),
luego \(F_N=64\varepsilon_\perp^2/N^2\) exactamente. Como
\(0\le\varepsilon_\perp\le\delta\), \(F_N\le1\) y
\(|s_N|\le\tfrac\pi2F_N\le32\pi\delta^2/N^2\). En Bob,
\(h_N\le64\delta'^2/N^2\), con \(\|M_B\|\le1\).

**(1d)** Peso: \(\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)\) y
\(-\xi_*\cdot(y-y_*)=-t_*(\theta_N+j')\). Usando \(\delta\le(1+j)/\sqrt3\):
\[
e^{\xi_*\cdot(x-x_*)}\|f(x)\|\le\tfrac{32\pi}{3}c_\phi\,N^{-7/2}(1+j)^2e^{-t_*j},
\qquad
e^{-\xi_*\cdot(y-y_*)}\|w(y)\|\le\tfrac{64}{3}c_\phi\,N^{-7/2}(1+j')^2e^{-t_*j'}.
\]
La cota es uniforme en \(u\) y en \(N\). La dependencia en \(j\) es
explícita: \((1+j)^2e^{-t_*j}\).

## Paso 2: suma cuadrática directa

Cada plano de profundidad \(j\) es un trasladado de
\(\Lambda_0=\mathbb Z^3\cap\{x_1+x_2+x_3=0\}\), con covolumen \(\sqrt3\) y
celda generada por \((1,-1,0)\) y \((0,1,-1)\), de diámetro \(\sqrt6\). El
soporte dentro del plano es el disco de radio
\(\rho_j=\sqrt{2R\delta-\delta^2}\le\sqrt{2R\delta}\). Cada punto de red del
disco tiene su celda contenida en el disco de radio \(\rho_j+\sqrt6\). Por tanto
\[
\#_j\le\frac{\pi(\rho_j+\sqrt6)^2}{\sqrt3}\le\frac{2\pi}{\sqrt3}\bigl(2R\delta+6\bigr)
\le\frac{2\pi}{\sqrt3}\Bigl(\frac{N(1+j)}{2\sqrt3}+6\Bigr)\le C\,N(1+j)\quad(N\ge1).
\]
Entonces
\[
\|f\|_{\ell^2_{\rm tilt}}^2\le\sum_{j\ge0}\#_j\Bigl(\tfrac{32\pi}{3}c_\phi\Bigr)^2N^{-7}(1+j)^4e^{-2t_*j}
\le C'N^{-6}\sum_{j\ge0}(1+j)^5e^{-2t_*j}=O(N^{-6}),
\]
con \(q(j)=(1+j)^4e^{-2t_*j}\) y \(\sum(1+j)q(j)<\infty\) porque \(t_*>0\).
Lo mismo vale para \(w\). Así \(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\).

Control de coherencia: la misma cuenta en ℓ¹ da \(O(N^{-5/2})\), la masa
registrada en §9.2.

## Paso 3: compatibilidad con Schur (8)

- **Inclinación:** Dyson §2 y Volterra usan \(D_\xi(\eta)=D(\eta-i\xi_*)\),
  los centros \(x_*,y_*\), \(\Lambda=e^{\Phi_*}\) y \(K_*=\xi_*\cdot v_*-\Phi_*\).
  Coincide con el peso de arriba.
- **Parseval:** con \(\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x)\)
  y \(d\mu=d^3p/(2\pi)^3\), se tiene
  \(\|\mathfrak A_f\|_{L^2(d\mu)}=\|f\|_{\ell^2_{\rm tilt}}\) exactamente.
  Lo mismo para \(\mathfrak B_w\).
- **Fases y componentes:** las fases \(e^{i\eta\cdot x_*}\) y
  \(e^{-i\eta\cdot y_*}\) son unimodulares. El embebido \((f,0)\) en
  \(\mathbb C^4\) es isométrico.
- **Norma:** la norma P de (6)–(8) es la \(L^2\) plana. \(\|\cdot\|_*\) solo
  actúa en Q, con constantes independientes de \(N\).

No se encuentra diferencia de peso, variable, medida ni normalización.

Límites que no son de norma: Schur (8) es PRELIMINARY, y (8) solo controla la
parte \(P\mathfrak A\) dentro de W. La parte Q de los extremos no queda
controlada (T2).

## Paso 4: alcance

- Extremos planos heredados: cubiertos.
- Contrato de dos canales: **no transferido**. La fuente de T1 es
  \(J(U_M-I)\phi_N\) (incluye \(c_N\) y \(J\)); no se ha comprobado.
- Referencia \(r_c=BU_N^NJ\phi_N\): **no transferida**. El paso (1b) usa que
  el walk libre es invariante por traslación. \(U_N\) contiene
  \(C_N(X)\), que no lo es, y la unitariedad solo da \(\|r_c\|_2\le1\).

Cuenta formal no declarada: \(N^{-3}\cdot N^{-1}\cdot N^{-3}\) para la
sub-contribución plana, condicionada a Schur (8). **No es `N^{-7} PROVED`.**
