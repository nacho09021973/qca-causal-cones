---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-25 10:34
proyecto: /home/ignac/qca-causal-cones
tema: debates/2026-09-25--flat-endpoint-l2-n3-review-request.md
rondas: 1
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - ABNER — DeepSeek — api.deepseek.com/deepseek-v4-pro
  - GEMINI — Google — generativelanguage.googleapis.com/gemini-3.1-pro-preview
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

# Revisión independiente estrecha: extremos planos en ℓ² inclinado

Fecha: 2026-09-25. Autor de la derivación: Claude (familia Anthropic).
Objeto: `2026-09-25--flat-endpoint-l2-n3-derivation-DRAFT.md` (adjunto).
Revisores solicitados: familias distintas de Anthropic. Una sola ronda. No
es un Sanedrín completo ni un comité.

## Pregunta y límite

¿Demuestra el borrador \(\|f_N\|,\|w_N\|_{\ell^2_{\rm tilt}}=O(N^{-3})\) para
los extremos planos heredados, en la norma que empareja con Schur (8)?
Intentad refutarlo. El estado declarado en el borrador no es evidencia.
Rehaced cada paso desde las definiciones del TeX y del informe regional.

## Cuatro criterios, puntuados por separado

1. **Cota puntual \(O(N^{-7/2})\):** ¿es uniforme en \(x\), \(u\) y \(N\)?
   ¿Oculta factores que crezcan en \(j\), en la dirección tangencial o en
   \(N\)? Comprobad (1a) \(\sup|b_N|=b_N(0)\) con \(g\ge0\); (1b)
   \(\sup|r|\le\int|\hat\phi_N|\) por unitariedad de \(S(p)\); (1c)
   \(F_N=64\varepsilon_\perp^2/N^2\) exacta y \(\varepsilon_\perp\le\delta\);
   (1d) el signo del peso.
2. **Conteo y suma:** ¿es correcto \(\#_j\le CN(1+j)\), con celda de diámetro
   \(\sqrt6\) y covolumen \(\sqrt3\)? ¿Da la suma cuadrática \(O(N^{-6})\) con
   el \(q(j)\) real?
3. **Norma de Schur:** ¿coinciden exactamente la inclinación \(\xi_*\), los
   centros, \(\Lambda=e^{\Phi_*}\), Parseval con \(d\mu=d^3p/(2\pi)^3\) y el
   embebido en \(\mathbb C^4\) con la norma P de Schur (6)–(8)? Señalad
   cualquier diferencia de peso, variable, medida o normalización.
4. **Alcance:** ¿queda limitado a los extremos planos, sin transferir nada al
   contrato de dos canales ni a \(r_c\)? ¿Se insinúa `N^{-7}`?

Para cada objeción: ecuación, contraejemplo y reparación. Clasificad cada una
como FATAL, REQUIRED_REPAIR u OPTIONAL. Si no hay objeción, decidlo sin
inventarla.

**Veredicto:** `PASS`, `PASS_WITH_REPAIRS` o `FAIL`.

No revisar Schur (8) en sí, ni H1c, Volterra, cancelaciones o las piezas
lineales. No proponer nuevos frentes.

## Snapshot

Base: `863fe8e86e2174a2b96fc38635d179e9114b2ce6`.

| Archivo | SHA256 |
| --- | --- |
| papers/ir-corona/ir-corona.tex | 05a2eb09d2f103608683978c292de939511359677727982de441970f2e655636 |
| reports/2026-09-17--regional-laplace-coefficient-gate.md | 8d0af529559887bdfa6cba125a23bc1629c19a96c7ba2adcb8c378f6a3294623 |
| reports/2026-09-17--scaled-ir-signaling-gate.md | 86a086dcc7e13f65dafc4f1003f7fe6d6801156a659b2b179f1fa8f2884fcf92 |
| reports/2026-09-24--h1c-return-kernel-schur-audit.md | ac92cb8c10fa49a94dd36387846e38ce3a8885bfbdc2b0c8001e407f046e4e9b |
| reports/2026-09-24--h1c-exact-dyson-decomposition.md | 0c911bea4176e6ed1a84eb21f95eae30d9957019d4b4ddcff0386a2d1252efd7 |
| reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md | ab06bb4136a4a96565670bc87d66eb6c8b13679abc7f9f3db31cfbe0b58dee9d |
| state/CURRENT_STATE.md | 99eb8024b4643bf319d69259fed2fd76efe61f0d674c5ad2fca9cdb18262931e |

## Contexto

### Contexto adjunto: debates/2026-09-25--flat-endpoint-l2-n3-derivation-DRAFT.md
```
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
```

### Contexto adjunto: papers/ir-corona/ir-corona.tex
```
\documentclass[11pt]{amsart}

\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\Z}{\mathbb{Z}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\T}{\mathbb{T}}
\newcommand{\cA}{\mathcal{A}}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cK}{\mathcal{K}}
\newcommand{\cS}{\mathcal{S}}
\newcommand{\up}{{\uparrow}}
\newcommand{\dn}{{\downarrow}}
\newcommand{\Cmicro}{C_{\mathrm{micro}}}
\newcommand{\cIR}{c_{\mathrm{IR}}}
\newcommand{\arcosh}{\operatorname{arcosh}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Tr}{\operatorname{Tr}}
\newcommand{\Hess}{\operatorname{Hess}}
\newcommand{\re}{\operatorname{Re}}
\newcommand{\im}{\operatorname{Im}}
\newcommand{\vstar}{v_*}
\newcommand{\xistar}{\xi_*}
\newcommand{\uhat}{\hat u}

\begin{document}

\title[Infrared response outside the emergent light cone]{An infrared operational response outside the emergent light cone of a three-dimensional Weyl quantum walk}

% TODO(author): any AI-assistance disclosure required by the target journal.
\author{Jos\'e Ignacio Mart\'in Gandul}
\address{Independent Researcher, Seville, Spain}
\email{adnacho@gmail.com}

\date{\today}

\begin{abstract}
In a finite-range quantum walk the relativistic light cone that emerges at
long wavelength need not exhaust the strict microscopic causal support.  We
study the three-dimensional Weyl walk introduced by Cedzich, Joye, Werner and
Werner as a model with a spherical propagation region.  All of its group
velocities lie in the closed Euclidean unit ball, which is also the light
cone of its Weyl node.  Its one-step causal support is the cube $[-1,1]^3$.
Velocities in the cube but outside the ball form a \emph{corona}.  There,
propagation is non-ballistic but not causally forbidden.

We ask whether the corona carries an operational response that survives
infrared control.  Alice prepares a narrow-band state and applies a local
encoding, and Bob reads out with a local detector.  All three operations are
required to be infrared-admissible: acting on the band $|p|\le N^{-1}$, each
produces only a vanishing fraction of its output outside the wider band
$|p|\le N^{-1/2}$.  Bob's
region lies outside the emergent light cone of every site of Alice's region.
After $N$ steps, Bob's distinguishability $\delta(N)$ obeys the explicit
bound $\delta(N)\le 36N^4e^{-JN}$ with $J=(1-\sqrt3/2)\log 2$.  For a concrete
family of sixteen encoder--detector pairs, it has the exact leading
asymptotics
\[
\delta(N)=\bigl|C(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad \theta_N=\{\sqrt3N/4\}.
\]
Here $K_*\approx0.1905$ is the value of a Legendre rate function at a unique
regional minimiser.  The coefficient $C(\theta)$ is given in closed form, and
interval arithmetic shows that it does not vanish for any $\theta$ in any of
the sixteen pairs.  The emergent cone is therefore not operationally sharp,
even for infrared-admissible operations.  The response is non-perturbatively
small, invisible to every power of the infrared scale, and it lies strictly
inside the microscopic causal support.  The result is purely asymptotic: the
remainder constants are not explicit, and numerical diagnostics indicate
that the leading term is quantitatively accurate only for $N$ of order
$10^3$ and beyond.
\end{abstract}

\maketitle

\section{Introduction}\label{sec:intro}

Quantum cellular automata and quantum walks are unitary dynamics on a lattice
with a strict bound on the speed of propagation
\cite{SchumacherWerner,Arrighi,Farrelly}.  After $N$ steps of a finite-range
walk, the propagator vanishes identically outside $N\Cmicro$.  Here
$\Cmicro=\operatorname{conv}F$ is the convex hull of the one-step jumps.
Many such walks have a conical point in their dispersion relation.  Near it,
the long-wavelength dynamics is that of a Weyl or Dirac equation with a
speed of light $\cIR$
\cite{BialynickiBirula,DArianoPerinotti,BDPT,DArianoErbaPerinotti}.

In spatial dimension $d\ge2$ the two causal structures cannot coincide.  The
infrared cone of a Weyl node is a Euclidean ball, and $\Cmicro$ is a
polytope.  Exact isotropy of the microscopic causal structure is incompatible
with a regular lattice.  It can be compatible with random discreteness, as in
the causal-set theorem of Bombelli, Henson and Sorkin \cite{BHS}, but that
setting lies outside the scope of this paper.  For a lattice walk, some
velocities are therefore causally allowed but not relativistic.  How much
physics can be sent through them?

Three questions must be kept apart.

\begin{description}
\item[(U) Ultraviolet propagator] Does the exact kernel assign non-zero
  amplitude to sites outside the infrared ball but inside $N\Cmicro$?  For
  the walk studied here it does: along the eight vertex rays a single
  lattice path contributes, with amplitude of norm $4^{-N}$
  (Proposition~\ref{prop:geometry}).  One-step Alice/Bob protocols built
  from localized operations turn this into a finite distinguishability
  (for instance $3/128$ after one step for a suitable localized
  preparation, as recorded in~\cite{Repo}).  Such protocols are broadband:
  their operations are not concentrated near the Weyl node.
\item[(I) Infrared operational response] Require the preparation, the
  encoder and the detector to be infrared-admissible, and put Bob outside
  the infrared cone of \emph{every} site of Alice.  Does Bob's
  distinguishability still fail to vanish as the infrared scale goes to
  zero, and at what rate?
\item[(N) Nature] Is there a physical system in which the lattice scale and
  the operations are given rather than engineered?  This question is not
  addressed here.
\end{description}

A non-zero ultraviolet kernel does not answer (I).  Infrared admissibility
could in principle force exact cancellations, and conversely an exponentially
small infrared response is compatible with (U).  This paper answers (I), for
one walk and one explicit protocol.

\subsection*{The walk}
We work with the Weyl walk of Cedzich, Joye, Werner and Werner
\cite[Eq.~(5.15)]{CJWW}.  They introduced it as a modification of the
Bialynicki-Birula Weyl automaton \cite[Eq.~(5.12)]{CJWW},
\cite{BialynickiBirula}, with the same conical points and with a
\emph{spherical} propagation region.  For this walk the three velocity sets
are nested as
\begin{equation}\label{eq:three-bodies}
\Gamma\;\subseteq\;B(1)\;\subsetneq\;\Cmicro=[-1,1]^3,
\qquad \sup_{v\in\Gamma}|v|=\cIR=1 .
\end{equation}
Here $B(1)=\overline B(0,1)$ is the closed infrared light cone ($\cIR=1$),
$\Gamma$ is the closed set of group velocities, and $\Cmicro$ is the strict
causal body.  Both statements in \eqref{eq:three-bodies} are exact, and
moreover $\partial B(1)\subseteq\Gamma$ (Proposition~\ref{prop:geometry}).
Numerically, $\Gamma$ fills the ball; this is not proved and not used.
Every ballistic mode, at every energy, therefore respects the emergent light
speed.  Nevertheless, in every non-axial direction $\hat n$ the causal
support extends to $\|\hat n\|_1\in(1,\sqrt3\,]$ times the light speed.
Probability outside $\Gamma$ is exponentially small in $N$ \cite{CJWW}.  The
question is whether it can be \emph{used} under infrared control.

\subsection*{Main results}
Section~\ref{sec:protocol} gives the precise definitions.  In outline,
Alice's region is the lattice ball $\cA_N$ of radius $N/4$ at the origin,
and Bob's region is the lattice ball $\cB_N$ of radius $N/4$ at $N(1,1,1)$.
After $N$ steps, every pair $(x,y)\in\cA_N\times\cB_N$ is separated by more
than $N+N/5$.  Bob is thus outside the emergent cone of every site of
Alice, with a margin of order $N$.  The resource is a narrow-band packet of
momentum width $\Lambda=1/N$.  Alice's encoder is a smooth local unitary
$\exp(i\frac\pi2F_N(x)M)$ with $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$.  Bob's
effect is $h_N(y)\otimes M_B$ with $M_B\in\{I,(I+\sigma_j)/2\}$.  The
profiles $F_N,h_N$ are smooth bumps of width $N/4$ that vanish quadratically
on the spheres.

\begin{enumerate}[label=(\roman*)]
\item \emph{Infrared admissibility} (Theorem~\ref{thm:admissible}).  All
  eight operations map the band $|p|\le N^{-1}$ into the band
  $|p|\le N^{-1/2}$, up to relative errors $O(N^{-1/2})$ with explicit
  constants.  Single-site operations fail this criterion maximally
  (Lemma~\ref{lem:point}).
\item \emph{Explicit upper bound} (Theorem~\ref{thm:upper}).  For every
  $N\ge2$, every unitary acting in $\cA_N$, every one-particle state and
  every effect in $\cB_N$, Bob's distinguishability is at most
  $36N^4e^{-JN}$, with $J=(1-\tfrac{\sqrt3}{2})\log2$.  Polynomial infrared
  signalling is excluded.
\item \emph{Regional rate} (Theorem~\ref{thm:rate}).  The kernel between
  the two regions is $O(N^4)\,e^{-K_*N}$, where $K_*=I(v_*)$ is the minimal
  regional value of a Legendre rate function.  Here $I$ is the Legendre
  transform of $\Phi(\xi)=\arcosh(\prod_j\cosh\xi_j)$, and
  $v_*=(1-\frac1{2\sqrt3})(1,1,1)$ is the unique minimiser of $I$ over the
  regional velocity set.  Moreover $J<K_*<\log4$.  By (iv), the rate $K_*$
  is attained by an explicit response.
\item \emph{Leading asymptotics} (Theorem~\ref{thm:main}).  For all sixteen
  encoder--detector pairs,
  $\delta_{M,M_B}(N)=|C_{M,M_B}(\theta_N)|N^{-13/2}e^{-K_*N}(1+O(N^{-1/2}))$.
  The coefficient $C_{M,M_B}(\theta)$ is given in closed form and is
  uniformly non-zero, with relative oscillation in $\theta$ at most
  $1.5\times10^{-3}$.
\end{enumerate}

Result (iv) is an asymptotic statement and not a numerical approximation
valid from small $N$.  The constants in its remainder are not explicit, and
neither is the threshold $N_*$ beyond which $\delta_{M,M_B}(N)>0$ is
guaranteed.  Finite-$N$ diagnostics (Appendix~\ref{app:numerics}) indicate
a relative correction of about $-100/N$, so the leading term is
quantitatively accurate only for $N\gtrsim10^3$.  For the pairs with the
smallest coefficients, the next-order term $N^{-17/2}e^{-K_*N}$ dominates
throughout the diagnostic range $N\le56$ (Remark~\ref{rem:features}).

The coefficient is not a product of local factors.  It arises from the
interference between the \emph{free tail} of the resource at Bob, which is
only polynomially small, and the part of Alice's encoding that reaches Bob,
which is exponentially small.  Two points of the complex-shifted Brillouin
torus contribute, and they enter with different projectors.  The power
$13/2$ is not a count of Gaussian directions.  The two normal directions are
discrete sums over lattice planes of depth $O(1)$, and the common tangential
direction is a flat direction of the exponent that is confined only by the
profiles.

\subsection*{Relation to the literature}
Ballistic scaling and weak limit theorems for translation-invariant quantum
walks are classical \cite{Konno,GJS,AVWW}: $Q(t)/t$ converges in
distribution to the group velocity distributed by the initial state.
Cedzich, Joye, Werner and Werner \cite{CJWW} proved that the probability of
velocities outside the support of this limit decays exponentially.  They gave
a method for bounding the rate uniformly in the initial state and discussed
the ``fuzziness'' of the emergent light cone in exactly this language.  Our
upper bound (ii) uses their contour-shift idea, supplemented by an elementary
ellipse lemma and a Jordan-safe bound on matrix powers.  Their method bounds
rates; it does not give prefactor-level asymptotics.

Sharp asymptotics with prefactors outside the propagation region are known
in one dimension.  Sunada and Tate \cite{SunadaTate} obtained exact local
asymptotics of transition probabilities, including exponential decay with an
explicit prefactor in the region hidden from the weak limit.  Carteret,
Richmond and Temme \cite{CRT} obtained uniformly convergent asymptotics in
the exponentially decaying regions of coined walks on the line.  These are
the closest precursors of the saddle-point analysis of
Section~\ref{sec:asymptotics}.  In two dimensions, Baryshnikov, Brady,
Bressler and Pemantle \cite{BBBP} analysed quantum walks through multivariate
generating functions and determined the limiting profile in the feasible
region, outside of which the probability is exponentially small.  Analytic
combinatorics in several variables \cite{ACSV} provides general transfer
theorems for multivariate coefficient asymptotics, whose standard sharp
forms assume minimality hypotheses on the critical points.  We do not claim
that these methods cannot reproduce the present result.  We are not aware of
a transfer theorem that yields it directly, and we carry out the
model-specific saddle-point analysis explicitly.

What we add is a \emph{lower} bound, in the strong form of exact leading
asymptotics.  It concerns an \emph{operational} quantity: the
distinguishability produced by a local encoding.  The encoding is spread
over a region of size $O(N)$ and constrained to be infrared-admissible, in
dimension three, and at a point strictly inside the corona.  Upper bounds
alone cannot distinguish an exponentially small response from an exactly
vanishing one.  In the problem studied here that distinction is the
content of the result.  The novelty claim is correspondingly narrow.  To our
knowledge, Theorem~\ref{thm:main} is the first prefactor-level asymptotic,
with a leading coefficient that is oscillatory and certified to be
non-vanishing, for an infrared-controlled operational response in the
strictly outside-propagation-region regime of a three-dimensional
multi-component quantum walk.  Exponential decay outside the propagation
region, large-deviation rates, Weyl-cone dispersion and microscopic support
outside an emergent cone all have prior art, cited above.

Lieb--Robinson bounds \cite{LiebRobinson,BHV} give exponentially small
leakage outside a linear cone for continuous-time lattice dynamics.  For
quantum walks the strict cone $\Cmicro$ plays that role exactly, and the
question here is the one \emph{inside} it.

\subsection*{Organisation}
Section~\ref{sec:walk} sets up the walk and proves the geometric statements.
Section~\ref{sec:protocol} defines the protocol and infrared admissibility.
Section~\ref{sec:results} states the results.  Sections~\ref{sec:upper}
to~\ref{sec:asymptotics} contain the proofs.  Section~\ref{sec:discussion}
discusses scope and limitations.  Appendix~\ref{app:numerics} lists the
computer-assisted parts and the finite-$N$ diagnostics.

\section{The walk and its three velocity sets}\label{sec:walk}

\subsection{Conventions}
The one-particle Hilbert space is $\mathcal H=\ell^2(\Z^3;\C^2)$ with
internal basis $\up=(1,0)^T$ and $\dn=(0,1)^T$.  We use the Fourier
transform $\hat\psi(p)=\sum_{x}e^{ip\cdot x}\psi(x)$, with inverse
$\psi(x)=\int_{\T^3}e^{-ip\cdot x}\hat\psi(p)\,d\mu(p)$ and
$d\mu=d^3p/(2\pi)^3$ on $\T^3=[-\pi,\pi)^3$.  We write $c_j=\cos p_j$ and
$s_j=\sin p_j$.  $B(1)=\overline B(0,1)$ denotes the closed Euclidean unit
ball.

The walk $W$ of \cite[Eq.~(5.15)]{CJWW} has symbol
\[
W(p)=\begin{pmatrix} c_1c_2e^{ip_3} & -c_1s_2+is_1\\ c_1s_2+is_1 & c_1c_2e^{-ip_3}\end{pmatrix},
\qquad \det W(p)=1 .
\]
States evolve by the unitary $S$ with symbol
\begin{equation}\label{eq:symbol}
S(p)=W(p)^{-1}=\begin{pmatrix} c_1c_2e^{-ip_3} & c_1s_2-is_1\\ -c_1s_2-is_1 & c_1c_2e^{ip_3}\end{pmatrix}.
\end{equation}
Both are matrix-valued trigonometric polynomials, so they extend to entire
functions of $p\in\C^3$.  For $p\in\C^3$, $S(p)$ denotes the continuation of
\eqref{eq:symbol}, which is the inverse of $W(p)$ and not its adjoint.
Writing $S(p)=\sum_dS_de^{ip\cdot d}$, the walk acts as
$(S\psi)(y)=\sum_dS_d\psi(y-d)$.  The $N$-step kernel is
\begin{equation}\label{eq:kernel}
(S^N)_{y,x}=G_N(y-x),\qquad G_N(d)=\int_{\T^3}e^{-ip\cdot d}S(p)^N\,d\mu(p).
\end{equation}

\begin{lemma}[Jumps]\label{lem:jumps}
The set $F=\{d:S_d\ne0\}$ has fourteen elements: the eight vertices
$(\pm1,\pm1,\pm1)$, the four face diagonals $(\pm1,\pm1,0)$, and the two
axial jumps $(\pm1,0,0)$.  Each vertex block is $\frac14$ times a rank-one
diagonal projector; in particular $S_{(1,1,1)}=\frac14|\dn\rangle\langle\dn|$.
The face-diagonal blocks have norm $\frac14$ and the axial blocks have norm
$\frac12$, so that $\sum_d\|S_d\|=4$.
\end{lemma}

\begin{proof}
This is a direct expansion of \eqref{eq:symbol} in $z_j=e^{ip_j}$.  The
coefficient of $z_1z_2z_3$ comes only from the $(2,2)$ entry
$c_1c_2e^{ip_3}$ and equals $\frac14$.
\end{proof}

\subsection{Dispersion and the infrared node}
Since $\det S=1$ and $\tr S(p)=2c_1c_2c_3$, the eigenvalues of $S(p)$ are
$e^{\mp i\omega(p)}$ with
\begin{equation}\label{eq:dispersion}
\cos\omega(p)=\cos p_1\cos p_2\cos p_3 .
\end{equation}
At $p=0$ one has $S(p)=I-iH_W(p)+O(|p|^2)$ with
\[
H_W(p)=p_1\sigma_1-p_2\sigma_2+p_3\sigma_3,\qquad H_W(p)^2=|p|^2I .
\]
This is a Weyl Hamiltonian with speed $\cIR=1$.  The same conical structure
occurs at the eight points of $\{0,\pi\}^3$.

\begin{proposition}[Geometry]\label{prop:geometry}
\begin{enumerate}[label=(\alph*)]
\item The causal body is $\Cmicro=\operatorname{conv}F=[-1,1]^3$.  Its
  support function is $h_{\Cmicro}(\hat n)=\|\hat n\|_1$ for unit vectors
  $\hat n$.
\item At every $p$ where $\omega$ is differentiable,
  \begin{equation}\label{eq:SOS}
  \bigl(1-f^2\bigr)-|\nabla f|^2=s_2^2s_3^2+s_1^2s_2^2c_3^2+s_1^2c_2^2s_3^2\ \ge0,
  \qquad f=c_1c_2c_3,
  \end{equation}
  and hence $|\nabla\omega(p)|\le1$.  At the conical points $\nabla\omega$
  takes every value in the unit sphere.  Thus $\Gamma\subseteq B(1)$ and
  $\partial B(1)\subseteq\Gamma$, where $\Gamma$ is the closure of the set
  of group velocities.
\item For every vertex $\sigma\in\{\pm1\}^3$ and every $N\ge1$,
  $(S^N)_{N\sigma,0}=S_\sigma^N=4^{-N}\Pi_\sigma\ne0$, where $\Pi_\sigma$ is
  a diagonal rank-one projector.  In particular
  $(S^N)_{(N,N,N),0}=4^{-N}|\dn\rangle\langle\dn|$.  Hence the $N$-step
  support function equals $N\|\hat n\|_1$ exactly.
\end{enumerate}
\end{proposition}

\begin{proof}
(a) follows from Lemma~\ref{lem:jumps}.  The supremum of $\hat n\cdot x$ over
the cube is separable and equals $\sum_j|n_j|$.

(b) With $\cos\omega=f$ we have $\nabla\omega=-\nabla f/\sin\omega$ and
$\sin^2\omega=1-f^2$.  The identity \eqref{eq:SOS} is a polynomial identity
in $(c_j,s_j)$ modulo $c_j^2+s_j^2=1$, and is checked by expansion.  Near a
conical point, $\omega(p)=|p-p_\vee|+O(|p-p_\vee|^2)$, so
$\nabla\omega=(p-p_\vee)/|p-p_\vee|+o(1)$ sweeps the unit sphere.

(c) Let $d_1+\dots+d_N=N\sigma$ with $d_k\in F$.  Every $d\in F$ satisfies
$\sigma_i d_i\le1$ for each coordinate $i$, so
$\sum_k\sigma_i(d_k)_i=N$ forces $\sigma_i(d_k)_i=1$ for all $i$ and $k$,
that is, $d_k=\sigma$.  Hence $(S^N)_{N\sigma,0}=S_\sigma^N$.  By Lemma~\ref{lem:jumps},
$S_\sigma=\frac14\Pi_\sigma$, so $S_\sigma^N=4^{-N}\Pi_\sigma$.
\end{proof}

\begin{remark}
The reverse inclusion $B(1)\subseteq\Gamma$, that is, that $\Gamma$ fills
the ball, holds numerically but is not proved and not used.  What is used is
the exact inclusion $\Gamma\subseteq B(1)$, equivalently
$\sup|\nabla\omega|\le\cIR$, with equality by $\partial B(1)\subseteq\Gamma$.  Consequently the relation
$\sup|v_g|=\cIR$ does \emph{not} imply that the emergent cone coincides with
the causal boundary.  The two coincide only in the six axial directions.
The \emph{corona} is $\Cmicro\setminus B(1)$.  Propagation into $N$ times
the corona is not ballistic, but by (c) it is not forbidden.
\end{remark}

\begin{remark}
For the Bialynicki-Birula walk \cite[Eq.~(5.12)]{CJWW}, $\Gamma$ is contained
in the intersection of three orthogonal cylinders (and numerically equal to
it \cite[Fig.~5]{CJWW}).  It contains group velocities up to
$\sqrt{3/2}>\cIR$, attained at $p=-\frac\pi4(1,1,1)$.  In that walk the corona contains a ballistic sector
faster than the emergent light.  We restrict to \cite[Eq.~(5.15)]{CJWW}
precisely because it has no such sector.
\end{remark}

\section{Protocol and infrared admissibility}\label{sec:protocol}

Fix an integer $N\ge2$.  The infrared scale is $\Lambda_N=N^{-1}$ and the
admissibility budget is $\Lambda'_N=N^{-1/2}$.  Let $\Pi_\Lambda$ denote the
spectral projection onto $\{|p|_2\le\Lambda\}$, and write $\Pi=\Pi_{\Lambda_N}$
and $\Pi'=\Pi_{\Lambda'_N}$.  For $N\ge2$ both balls lie in $|p|<\pi/4$,
where $f>0$ and the only conical point is $p=0$.

\subsection{Regions}
Let
\[
\cA_N=\{x\in\Z^3:|x|\le N/4\},\qquad \cB_N=\{y\in\Z^3:|y-N(1,1,1)|\le N/4\},
\]
with Euclidean norms throughout.  For every $x\in\cA_N$ and $y\in\cB_N$,
\begin{equation}\label{eq:separation}
|y-x|-N\ge(\sqrt3-\tfrac32)N>\tfrac N5,
\qquad
u\cdot(y-x)\ge(3-\tfrac{\sqrt3}2)N,\quad u=(1,1,1).
\end{equation}
Both follow from the triangle inequality, and the last inequality in the
first display is $3>(17/10)^2$.  Each region has at most $(N/2+1)^3\le N^3$
sites.

\subsection{Resource, encoder, detector}
Let $g(q)=(1-|q|^2)_+^2$.  The resource is
\[
\hat\phi_N(p)=Z_N^{-1/2}\,g(Np)\,\dn,
\qquad Z_N=\frac{64}{3465\,\pi^2N^3},
\]
so that $\|\phi_N\|=1$ and $\Pi\phi_N=\phi_N$.  In position space
$\phi_N=\varphi_N\,\dn$ with the real, radial function
\begin{equation}\label{eq:resource}
\varphi_N(x)=N^{-3/2}\,\Phi_0(x/N),\qquad
\Phi_0(w)=c_r\int_{\R^3}g(q)\,e^{-iq\cdot w}\,d^3q,\qquad c_r=\frac{\sqrt{3465}}{64\pi^2}.
\end{equation}
This is exact, with no truncation of the spatial tail.

Alice's profile is $F_N(x)=(1-16|x|^2/N^2)_+^2$, supported in $\cA_N$.  For
$M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$ the encoder is the multiplication
operator
\[
U_M=\exp\bigl(i\tfrac\pi2F_N(x)\,M\bigr)=I+c_N(x)I+is_N(x)M,
\qquad c_N=\cos(\tfrac\pi2F_N)-1,\ \ s_N=\sin(\tfrac\pi2F_N).
\]
It acts as the identity outside $\cA_N$.  In the second-quantized free
fermion picture it is the one-particle restriction of an even,
number-preserving local unitary.

Bob's profile is $h_N(y)=(1-16|y-Nu|^2/N^2)_+^2$, with $u=(1,1,1)$,
supported in $\cB_N$.
For $M_B\in\{I,P_1,P_2,P_3\}$, with $P_j=(I+\sigma_j)/2$, the effect is
\[
E=h_N\otimes M_B,\qquad 0\le E\le I .
\]

\subsection{Signal}
Alice encodes a bit $b\in\{0,1\}$ by applying $U^{(1)}=U_M$ or $U^{(0)}=I$ to
the resource.  After $N$ steps the state is
$\psi_b(N)=S^NU^{(b)}\phi_N$.  The signal is
\begin{equation}\label{eq:signal}
\delta_{M,M_B}(N)=\bigl|\langle\psi_1,E\psi_1\rangle-\langle\psi_0,E\psi_0\rangle\bigr|=|L_{M,M_B}(N)|,
\end{equation}
where $L_{M,M_B}(N)$ denotes the signed difference.  No spectral projection is
applied to the signal.  Infrared admissibility is a property of the
operations only.  We also consider the trace distance $D_B(N)$ between Bob's
reduced states.  In the free-fermion description, the reduced state of a
one-particle vector $\psi$ on the modes of $\cB_N$ is
$(1-\|P_B\psi\|^2)|\Omega\rangle\langle\Omega|+|P_B\psi\rangle\langle P_B\psi|$,
and $D_B=\frac12\|\rho_1-\rho_0\|_1\ge\delta$.

\subsection{Infrared admissibility}
\begin{definition}\label{def:admissible}
For a bounded operator $X$ on $\mathcal H$ with $X\Pi\ne0$, set
\[
\eta_{\mathrm{op}}(X)=\frac{\|(I-\Pi')X\Pi\|}{\|X\Pi\|}.
\]
The encoder $U_M$ is \emph{infrared-admissible} if
$\eta_{\mathrm{op}}(U_M-I)\to0$ and
\[
\eta_{\mathrm{enc}}^M=\frac{\|\Delta_M-\Pi'\Delta_M\Pi'\|_1}{\|\Delta_M\|_1}\to0,
\qquad \Delta_M=U_M|\phi_N\rangle\langle\phi_N|U_M^*-|\phi_N\rangle\langle\phi_N|,
\]
as $N\to\infty$, where $\Delta_M\ne0$ is required for $\eta_{\mathrm{enc}}^M$
to be defined.  The effect $E$ is infrared-admissible if
$\eta_{\mathrm{op}}(E)\to0$.
\end{definition}

For the operations of this paper all denominators are non-zero for every
$N\ge2$ (Theorem~\ref{thm:admissible}).

In words: acting on anything in the infrared band, an admissible operation
leaves only a vanishing fraction of its output outside the wider band
$\Pi'$.  A strictly local gate cannot do this.

\begin{lemma}[Single-site operations are ultraviolet]\label{lem:point}
If $X\Pi\ne0$ and $\operatorname{ran}X\subseteq\ell^2(\{x_0\};\C^2)$ for a
single site $x_0$, then
$\eta_{\mathrm{op}}(X)=\sqrt{1-\kappa'_N}\to1$, where
$\kappa'_N=(6\pi^2N^{3/2})^{-1}$.
\end{lemma}

\begin{proof}
For every vector $e_{x_0}\otimes\chi$,
$\|\Pi'(e_{x_0}\otimes\chi)\|^2=\mu(\{|p|\le\Lambda'_N\})=(\Lambda'_N)^3/(6\pi^2)$.
Hence every vector in $\operatorname{ran}X$ has exactly the fraction
$1-\kappa'_N$ of its squared norm outside $\Pi'$.
\end{proof}

This is the reason the encoder is spread over a region of size $O(N)$ with
a smooth profile.  A pointlike phase gate, such as $I-2P_{x_0}$, is
excluded by Lemma~\ref{lem:point}.  The regional operations pass:

\begin{theorem}[Admissibility]\label{thm:admissible}
Let $K_e=\frac\pi2(2+8\sqrt3\pi)$, $K_d=\frac\pi2(1+16\sqrt3)$ and
$m=11/(560\pi^2\,32^3)$.  For all $N\ge32$, all four $M$ and all four
$M_B$,
\[
\eta_{\mathrm{op}}(U_M-I)\le\frac{K_e}{\sqrt{(2-\sqrt2)m}}\,N^{-1/2},\qquad
\eta_{\mathrm{enc}}^M\le\frac{K_e}{m\sqrt{2-\sqrt2}}\,N^{-1/2},\qquad
\eta_{\mathrm{op}}(E)\le\frac{2K_d}{\sqrt m}\,N^{-1/2}.
\]
All denominators are non-zero for every $N\ge2$.
\end{theorem}

The constants are conservative.  The proof is in Section~\ref{sec:admissible}.

\section{Results}\label{sec:results}

\begin{theorem}[Explicit upper bound]\label{thm:upper}
Let $N\ge2$ and $T_N=\|P_{\cB_N}S^NP_{\cA_N}\|$.  Then
\[
T_N\le9N^4e^{-JN},\qquad J=\bigl(1-\tfrac{\sqrt3}2\bigr)\log2\approx0.0929 .
\]
Consequently, for every unitary $U$ acting as the identity outside
$\cA_N\otimes\C^2$, every one-particle state and every effect in $\cB_N$,
\[
\delta\le D_B\le4T_N\le36N^4e^{-JN}.
\]
\end{theorem}

\begin{remark}[Formal verification]
Theorem~\ref{thm:upper} is machine-checked in Lean~4 with Mathlib
(\texttt{formal/} in~\cite{Repo}), for every $N\ge2$ and without
additional axioms.  This covers the kernel bound, the geometry
\eqref{eq:separation}, the counting of lattice points, the operator bound on
$T_N$, and the step $\delta\le4T_N$.  The formal proof bounds the matrix
powers through Cayley--Hamilton and entrywise estimates instead of
Lemma~\ref{lem:schur}, and obtains the sharper constant
$T_N\le4N^4e^{-JN}$.  Both constants are valid; the proof in
Section~\ref{sec:upper} keeps the constant $9$ that the elementary
Lemma~\ref{lem:schur} gives.  The identification of Bob's amplitudes with the
restricted walk, and the second-quantized distance $D_B$, are not
formalized.
\end{remark}

For $\xi\in\R^3$ put $\Phi(\xi)=\arcosh\bigl(\prod_{j=1}^3\cosh\xi_j\bigr)$
and define the rate function
\begin{equation}\label{eq:rate}
I(v)=\sup_{\xi\in\R^3}\bigl[\xi\cdot v-\Phi(\xi)\bigr].
\end{equation}
Let $V_{\mathrm{reg}}=(1,1,1)+\overline B(0,\tfrac12)$.  This is the set of
velocities $(y-x)/N$ for $x,y$ in the continuum balls underlying
$\cA_N,\cB_N$.

\begin{theorem}[Regional rate]\label{thm:rate}
\begin{enumerate}[label=(\alph*)]
\item $I$ is convex, $I=0$ on $\overline B(0,1)$, $I>0$ outside it, and
  $I=+\infty$ outside $[-1,1]^3$.
\item On $V_{\mathrm{reg}}$, $I$ has the unique minimiser
  $v_*=\alpha(1,1,1)$, $\alpha=1-\frac1{2\sqrt3}$.  The corresponding dual
  tilt is $\xi_*=t_*(1,1,1)$, where $t_*>0$ is the unique solution of
  $\alpha=\nabla_1\Phi(t,t,t)$.  Moreover
  \[
  K_*:=I(v_*)=3\alpha t_*-\arcosh(\cosh^3t_*),\qquad
  \cosh^2t_*=\frac{\alpha\bigl(\alpha+\sqrt{4-3\alpha^2}\bigr)}{2(1-\alpha^2)} .
  \]
\item $J<K_*<\log4$.  Numerically $t_*=0.7357528144\ldots$ and
  $K_*=0.1905189296\ldots$.
\item For all $N\ge2$ and all $(x,y)\in\cA_N\times\cB_N$,
  \[
  \|G_N(y-x)\|\le\bigl(1+4e^{3t_*-\Phi_*}N\bigr)e^{-K_*N},\qquad \Phi_*=\Phi(\xi_*),
  \]
  and hence $\delta\le D_B\le4N^3(1+10N)e^{-K_*N}$.
\end{enumerate}
\end{theorem}

The main result identifies the exact leading behaviour of every signal in
the family.  Write $\theta_N=\{\sqrt3N/4\}\in[0,1)$ for the fractional part.

\begin{theorem}[Leading asymptotics]\label{thm:main}
For each of the sixteen pairs $(M,M_B)$ there is a continuous, $1$-periodic,
real function $C_{M,M_B}(\theta)$ such that, as $N\to\infty$,
\[
L_{M,M_B}(N)=e^{-K_*N}N^{-13/2}\Bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\Bigr).
\]
Explicitly,
\begin{equation}\label{eq:C}
C_{M,M_B}(\theta)=\cK\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\end{equation}
with the constants $\cK$, $c_r$, the functions $\Gamma_\pm$ and the numbers
$\ell_0,\ell_\pi$ defined in Section~\ref{sec:asymptotics}.  For every pair,
\[
C_{M,M_B}(\theta)=\overline C_{M,M_B}\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad \sup_\theta|\vartheta_{M,M_B}(\theta)|\le1.47\times10^{-3},
\qquad \overline C_{M,M_B}\ne0,
\]
with the values in Table~\ref{tab:C}.  Consequently, for every pair,
\[
\delta_{M,M_B}(N)=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\]
and $\delta_{M,M_B}(N)>0$ for all $N$ larger than some finite $N_*$.
\end{theorem}

The constants implicit in the $O(N^{-1/2})$ terms are finite but not
explicit, and neither is $N_*$.  Theorem~\ref{thm:main} therefore does not
assert $\delta_{M,M_B}(N)>0$ at any specified $N$.  It also does not say from
which $N$ on the leading term is numerically accurate
(Section~\ref{sec:discussion}).

\begin{table}[t]
\centering
\small
\begin{tabular}{llrr}
\toprule
$M$ & $M_B$ & $\overline C_{M,M_B}$ & $\sup_\theta|C/\overline C-1|$\\
\midrule
$I$ & $I$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$I$ & $P_1$ & $+1.2072650683$ & $1.09\cdot10^{-3}$\\
$I$ & $P_2$ & $+0.8164098576$ & $1.08\cdot10^{-3}$\\
$I$ & $P_3$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_1$ & $I$ & $-3.7206303938$ & $1.05\cdot10^{-3}$\\
$\sigma_1$ & $P_1$ & $-1.5567800857$ & $1.06\cdot10^{-3}$\\
$\sigma_1$ & $P_2$ & $-2.8203960182$ & $1.02\cdot10^{-3}$\\
$\sigma_1$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $I$ & $-2.9389199724$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $P_1$ & $-0.5846543741$ & $1.02\cdot10^{-3}$\\
$\sigma_2$ & $P_2$ & $-1.7729950974$ & $1.04\cdot10^{-3}$\\
$\sigma_2$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_3$ & $I$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_3$ & $P_1$ & $-1.2072650683$ & $1.09\cdot10^{-3}$\\
$\sigma_3$ & $P_2$ & $-0.8164098576$ & $1.08\cdot10^{-3}$\\
$\sigma_3$ & $P_3$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
\bottomrule
\end{tabular}
\caption{Mean leading coefficients $\overline C_{M,M_B}=\cK c_r\overline\Gamma\ell_0$
and the uniform bound on their relative oscillation in $\theta$.  Values are
certified by interval arithmetic (Appendix~\ref{app:numerics}).}
\label{tab:C}
\end{table}

\begin{corollary}\label{cor:suppressed}
In this protocol the emergent light cone is not operationally sharp for
infrared-admissible operations.  For each pair the response is
non-perturbatively small: $\delta_{M,M_B}(N)=o(N^{-k})$ for every $k$.  It is
nevertheless non-zero for all large $N$, with the exact rate $K_*$, the exact
power $13/2$ and an explicit non-vanishing coefficient.
\end{corollary}

\begin{remark}\label{rem:features}
Three features of Table~\ref{tab:C} were not assumed and come out of the
computation.  First, $C(\sigma_3,\cdot)=-C(I,\cdot)$ at leading order;
the two encoders differ only at lower orders.  Second, the three Pauli
encoders are not equivalent: with $M_B=I$ they give three different
coefficients.  Third, for $M=\sigma_2$ the two contributing saddles enter with
the same sign for every detector: $\ell_0$ and $\ell_\pi$ of
Appendix~\ref{app:numerics} have the same sign.  Since $\Gamma_+>0$ and
$\Gamma_-\ge0$ (Lemma~\ref{lem:depth}), non-vanishing then follows without
the margin estimate in the proof of Theorem~\ref{thm:main}, so for this
encoder the non-cancellation mechanism is particularly transparent.  The smallest coefficients,
$|\overline C|\approx0.0753$, occur for $M\in\{I,\sigma_3\}$ with
$M_B\in\{I,P_3\}$.  For these two encoders with $M_B=I$, the diagnostics of
Appendix~\ref{app:numerics} show that the next-order term, of size
$N^{-17/2}e^{-K_*N}$, dominates numerically throughout the diagnostic range
$N\le56$.
\end{remark}

\begin{remark}[Methodology]
The protocol (regions, profiles, encoders, detectors, scalings
$\Lambda_N=N^{-1}$, $\Lambda'_N=N^{-1/2}$ and the encoding angle $\pi/2$) was fixed before
the asymptotic analysis and was not tuned afterwards.  The family of
encoders and detectors is not exhaustive: a general generator
$M=aI+b\cdot\sigma$ is not covered, because no symmetry of the walk relating
the directions $\hat n\cdot\sigma$ has been established.
\end{remark}

\section{Proof of the upper bounds}\label{sec:upper}

\subsection{An ellipse lemma}
For $a\ge1$ let
$E_a=\{z\in\C:(\re z)^2/a^2+(\im z)^2/(a^2-1)\le1\}$, where $E_1=[-1,1]$.
These are the confocal ellipses with foci $\pm1$.  The Joukowski map
$\lambda\mapsto(\lambda+\lambda^{-1})/2$ sends the circle $|\lambda|=r\ge1$
onto $\partial E_{(r+r^{-1})/2}$.

\begin{lemma}\label{lem:ellipse}
Let $a,c\ge1$.  If $z\in\partial E_a$ and $w\in E_c$, then $zw\in E_{ac}$;
consequently $E_aE_c\subseteq E_{ac}$.  If moreover $a,c>1$, then
$zw\in\partial E_{ac}$ only if $z=\pm a$ and $w=\pm c$.
\end{lemma}

\begin{proof}
If $c=1$, then $w\in[-1,1]$ and $zw\in E_a$ by convexity and symmetry.  If
$a=1$, then $z\in[-1,1]$ and the same argument applies.  So let $a,c>1$.
Write
$z=a\cos p+i\sqrt{a^2-1}\sin p$ and $w=c\,x+i\sqrt{c^2-1}\,y$ with
$x^2+y^2\le1$.  In the coordinates adapted to $E_{ac}$, the point $zw$
corresponds to $L(x,y)^T$ with
\[
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\ \sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
\]
With $A=a^2$, $C=c^2$ and $u=\cos^2p$, a direct computation gives
\[
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},\qquad
\det(I-L^TL)=\frac{(C-1)(1-u)\bigl[A-1+C(1-u)\bigr]}{AC(AC-1)} .
\]
Both are non-negative, so $I-L^TL\ge0$ by Sylvester's criterion and
$\|L\|\le1$.  If $u<1$, both are positive, so $\|L\|<1$ and $zw$ is
interior.  If $u=1$, then $z=\pm a$ and
\[
L=\pm\operatorname{diag}\Bigl(1,\ \frac{a\sqrt{c^2-1}}{\sqrt{a^2c^2-1}}\Bigr),
\]
whose second entry is $<1$.  Hence $|L(x,y)^T|=1$ forces $y=0$ and $|x|=1$,
that is, $w=\pm c$.
\end{proof}

\begin{lemma}\label{lem:specrad}
For $\eta\in\R^3$ and $\xi\in\R^3$,
$\rho\bigl(S(\eta-i\xi)\bigr)\le e^{\Phi(\xi)}$.  If all $\xi_j\ne0$, equality
holds if and only if $\eta\in\Sigma:=\{0,\pi\}^3$ modulo $2\pi$.
\end{lemma}

\begin{proof}
$\cos(\eta_j-i\xi_j)=\cos\eta_j\cosh\xi_j+i\sin\eta_j\sinh\xi_j\in\partial E_{\cosh\xi_j}$.
By Lemma~\ref{lem:ellipse} applied twice,
$f(\eta-i\xi)=\prod_j\cos(\eta_j-i\xi_j)\in E_{\prod\cosh\xi_j}$.  When all
$\xi_j\ne0$, it lies on the boundary only if every factor is a real vertex,
that is, only if every $\sin\eta_j=0$.  The eigenvalues $\lambda^{\pm1}$ of
the unimodular matrix $S(\eta-i\xi)$ satisfy $(\lambda+\lambda^{-1})/2=f$.
If $|\lambda|=r\ge1$, then $f\in\partial E_{(r+r^{-1})/2}$.  Since the
ellipses are nested, $(r+r^{-1})/2\le\prod\cosh\xi_j$, which is
$r\le e^{\Phi(\xi)}$, with strict inequality when $f$ is interior.  On
$\Sigma$, $f=\pm\prod\cosh\xi_j$ is real and equality holds.
\end{proof}

\begin{lemma}[Powers without a gap]\label{lem:schur}
Let $T$ be a $2\times2$ matrix with $\rho(T)\le e^{\varkappa}$ and
$\|T\|\le\beta$.  Then $\|T^N\|\le e^{N\varkappa}+\beta Ne^{(N-1)\varkappa}$.
\end{lemma}

\begin{proof}
Take a unitary Schur form $T=V\begin{psmallmatrix}\lambda_1&b\\0&\lambda_2\end{psmallmatrix}V^*$,
so $|b|\le\|T\|$.  The upper-right entry of the $N$-th power is
$b\sum_{j=0}^{N-1}\lambda_1^j\lambda_2^{N-1-j}$, also when
$\lambda_1=\lambda_2$.  The diagonal part has norm
$\max_j|\lambda_j|^N$.
\end{proof}

\subsection{Proof of Theorem~\ref{thm:upper}}
Since the integrand in \eqref{eq:kernel} is entire and $2\pi$-periodic in
each variable, the contour can be shifted to $p=\eta-i\xi$ for any
$\xi\in\R^3$ without boundary terms:
\begin{equation}\label{eq:tilt}
G_N(d)=e^{-\xi\cdot d}\int_{\T^3}e^{-i\eta\cdot d}\,S(\eta-i\xi)^N\,d\mu(\eta).
\end{equation}
Take $\xi=tu$ with $t=\log2$, so $\cosh^3t=125/64$.  Lemma~\ref{lem:specrad}
gives
\[
\rho\bigl(S(\eta-itu)\bigr)\le\exp\arcosh(125/64)<4,
\]
because $125/64<17/8=\cosh\log4$.  By Lemma~\ref{lem:jumps},
\[
\|S(\eta-itu)\|\le\sum_d\|S_d\|e^{t|u\cdot d|}\le4e^{3t}=32 .
\]
Lemma~\ref{lem:schur}, with the cruder bound $|\lambda_j|\le4$, gives
$\|S(\eta-itu)^N\|\le4^N+32N4^{N-1}\le9N4^N$.  With
\eqref{eq:separation},
\[
\|G_N(y-x)\|\le9N\exp\bigl[-t\,u\cdot(y-x)+N\log4\bigr]\le9Ne^{-JN}
\]
for all $(x,y)\in\cA_N\times\cB_N$.  The Schur test with $|\cA_N|,|\cB_N|\le N^3$
gives $T_N\le9N^4e^{-JN}$.

Let $v_b=P_BS^NU^{(b)}\psi$ for a one-particle state $\psi$.  Then
$v_1-v_0=P_BS^NP_A(U-I)\psi$, so $\|v_1-v_0\|\le2T_N$.  The difference of
Bob's reduced states is $X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|$ on
the one-particle block, together with $-\tr X$ on the vacuum block.  Hence
$D_B=\frac12(|\tr X|+\|X\|_1)\le\|X\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le4T_N$.
Mixed states follow by convexity, and $\delta\le D_B$ holds for every effect.
\qed

\subsection{Proof of Theorem~\ref{thm:rate}}
(a) $I$ is a supremum of affine functions, so it is convex, and $I\ge0$
(take $\xi=0$).  The inequality
$\cosh\sqrt{a^2+b^2}\le\cosh a\cosh b$, applied twice, gives
$\Phi(\xi)\ge|\xi|$, so $I=0$ on $\overline B(0,1)$.  Since
$\Phi(\xi)=|\xi|+O(|\xi|^3)$, $I(v)>0$ for $|v|>1$.  Finally $I=+\infty$ outside
$\operatorname{conv}F$ by \cite[Lemma~4.1]{CJWW}.  Directly, if
$v_j>1$, take $\xi=se_j$ and let $s\to\infty$, using $\Phi(se_j)=s$.

(b) $\Phi$ is smooth where $\Pi(\xi)=\prod_j\cosh\xi_j>1$, with
\[
\nabla\Phi(\xi)=\frac{\Pi(\xi)}{\sqrt{\Pi(\xi)^2-1}}\,(\tanh\xi_1,\tanh\xi_2,\tanh\xi_3).
\]
On the diagonal, $h(t)=\nabla_1\Phi(t,t,t)$ tends to $1/\sqrt3$ as
$t\to0^+$ and to $1$ as $t\to\infty$.  It is strictly increasing, since
$3h'(t)=u^T\Hess\Phi(t,t,t)\,u=3q_n(t)>0$, where $q_n(t)$ is given by the
formula of Lemma~\ref{lem:symbol}(d) with $c_*$ replaced by $\cosh t>1$.  Since
$\alpha\in(1/\sqrt3,1)$, there is a unique $t_*>0$ with $h(t_*)=\alpha$, and
then $\nabla\Phi(\xi_*)=v_*$.  Solving $h(t)=\alpha$ for $\cosh^2t$ gives the
stated closed form.  By the definition of $I$, for every $v$,
\[
I(v)\ge\xi_*\cdot v-\Phi(\xi_*)=I(v_*)+\xi_*\cdot(v-v_*)
=I(v_*)+\sqrt3\,t_*\bigl(\uhat\cdot v-|v_*|\bigr),
\qquad \uhat=u/\sqrt3 .
\]
On $V_{\mathrm{reg}}$ we have $\uhat\cdot v\ge\sqrt3-\frac12=|v_*|$, with
equality only at $v=v_*$.  Hence $v_*$ is the unique minimiser.

(c) The tilt $\xi=(\log2)u$ gives
$I(v_*)\ge3\alpha\log2-\arcosh(125/64)>(3-\tfrac{\sqrt3}2)\log2-\log4=J$.
Also $\xi_*\cdot v_*<\xi_*\cdot u$ because $\alpha<1$ and $t_*>0$, so
$I(v_*)<\xi_*\cdot u-\Phi(\xi_*)\le I(u)$.  Along the diagonal,
$3t-\arcosh(\cosh^3t)\uparrow\log4$, and $I(u)=\log4$ is also the exact
vertex rate of Proposition~\ref{prop:geometry}(c).  The numerical values are
enclosed by interval arithmetic.

(d) Apply \eqref{eq:tilt} with $\xi=\xi_*$.  By Lemma~\ref{lem:specrad},
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*}$ for all $\eta$.  By
Lemma~\ref{lem:jumps}, $\|S(\eta-i\xi_*)\|\le4e^{3t_*}$.
Lemma~\ref{lem:schur} gives
$\sup_\eta\|S(\eta-i\xi_*)^N\|\le e^{N\Phi_*}(1+4e^{3t_*-\Phi_*}N)$.  For
$(x,y)\in\cA_N\times\cB_N$, \eqref{eq:separation} and $\xi_*\parallel\uhat$
give $\xi_*\cdot(y-x)\ge N\,\xi_*\cdot v_*$, and
$N\xi_*\cdot v_*-N\Phi_*=NK_*$.  Numerically $4e^{3t_*-\Phi_*}<9.2$, so
$1+4e^{3t_*-\Phi_*}N\le1+10N$, and the Schur test concludes as before.
\qed

\section{Proof of admissibility}\label{sec:admissible}

\begin{lemma}\label{lem:IR1}
Let $a:\Z^3\to M_2(\C)$ satisfy $\sup\|a\|\le A$ and
$\|a(x+e_j)-a(x)\|\le L/N$ for all $x,j$.  Then
\[
\|(I-\Pi')\,a\,\Pi\|\le\tfrac\pi2(A+\sqrt3L)\,N^{-1/2}.
\]
\end{lemma}

\begin{proof}
Let $D_j\xi(x)=\xi(x+e_j)-\xi(x)$.  On the complement of $\Pi'$,
\[
\sum_j|e^{ip_j}-1|^2=\sum_j4\sin^2(p_j/2)\ge(2/\pi)^2|p|^2\ge(2/\pi)^2N^{-1},
\]
using $\sin s\ge2s/\pi$ on $[0,\pi/2]$.  By Plancherel,
$\|(I-\Pi')\xi\|\le\frac\pi2N^{1/2}(\sum_j\|D_j\xi\|^2)^{1/2}$.  For
$\psi=\Pi\psi$, $(\sum_j\|D_j\psi\|^2)^{1/2}\le N^{-1}\|\psi\|$.  The
discrete product rule
$D_j(a\psi)=a(\cdot+e_j)D_j\psi+(D_ja)\psi$ and Minkowski's inequality give
$(\sum_j\|D_j(a\psi)\|^2)^{1/2}\le(A+\sqrt3L)N^{-1}\|\psi\|$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:admissible}]
\emph{Numerators.}  $|\nabla F_N|=64|x|(1-16|x|^2/N^2)/N^2\le16/N$ inside
$\cA_N$, and the gradient vanishes on the sphere, so $F_N$ is
$16/N$-Lipschitz on $\Z^3$.  For $a_M=U_M-I$ we get $A=2$ and $L=8\pi$,
because $\|\frac{d}{dF}e^{i\pi FM/2}\|=\pi/2$.  For $E=h_N\otimes M_B$ we get
$A=1$ and $L=16$.  Lemma~\ref{lem:IR1} bounds the numerators by
$K_eN^{-1/2}$ and $K_dN^{-1/2}$.  For $\eta_{\mathrm{enc}}$, write
$v=U_M\phi_N$, $w=\Pi'v$ and $r=v-w=(I-\Pi')a_M\phi_N$.  Since
$\Pi'\phi_N=\phi_N$, $\Delta_M-\Pi'\Delta_M\Pi'=|r\rangle\langle v|+|w\rangle\langle r|$,
whose trace norm is at most $2\|r\|\le2K_eN^{-1/2}$.

\emph{Denominators.}  For $|x|\le N$ and $|p|\le N^{-1}$, $\cos(p\cdot x)\ge\frac12$.
Hence $\varphi_N(x)\ge\frac12\sqrt{11/(140\pi^2)}\,N^{-3/2}$ for $|x|\le N$.
Let $N\ge32$, and consider two auxiliary sets.  The first is
$Q_{\mathrm{in}}=\{|x_j|\le N/32\}$, with at least $(N/32)^3$ sites, on which
$F_N\ge(61/64)^2>\frac12$.  The second is
$Q_{\mathrm{out}}=\{N/2\le x_1\le5N/8,\ 0\le x_2,x_3\le N/8\}$, with at least
$(N/16)^3$ sites, on which $F_N=0$ and $|x|<N$.  Each carries resource
weight at least $m$.

On $Q_{\mathrm{in}}$, $\frac\pi2F_N\in[\frac\pi4,\frac\pi2]$, so
$a_M^*a_M=2(1-\cos\frac\pi2F_N)I\ge(2-\sqrt2)I$.  Thus
$\|a_M\Pi\|\ge\|a_M\phi_N\|\ge\sqrt{(2-\sqrt2)m}$.  For the detector, test
on the resource translated to $N(1,1,1)$, with internal state a
$+1$ eigenvector of $M_B$.  This test vector lies in $\operatorname{ran}\Pi$,
and it gives $\|E\Pi\|\ge\frac12\sqrt m$.

For $\eta_{\mathrm{enc}}$, $\|\Delta_M\|_1=2\sqrt{1-|z|^2}$ with
$z=\sum_xw_xt_x$, $w_x=|\varphi_N(x)|^2$ and
$t_x=\langle\dn|e^{i\pi F_N(x)M/2}|\dn\rangle$.  This gives $t_x=e^{i\pi F_N/2}$
for $M=I$, $\cos(\pi F_N/2)$ for $M=\sigma_{1,2}$, and $e^{-i\pi F_N/2}$ for
$M=\sigma_3$.  Then
$1-|z|^2=\sum_{x,y}w_xw_y(1-\re t_x\bar t_y)$.  All terms are non-negative,
and for $x\in Q_{\mathrm{in}}$, $y\in Q_{\mathrm{out}}$ one has
$\re t_x\bar t_y=\cos(\frac\pi2F_N(x))\le1/\sqrt2$.  Counting both orders
gives $1-|z|^2\ge(2-\sqrt2)m^2$.  For $2\le N<32$ the same argument, with
the origin and the site $(\lfloor N/4\rfloor+1,0,0)$, shows that the
denominators are non-zero.
\end{proof}

\section{Proof of the leading asymptotics}\label{sec:asymptotics}

Throughout, $C$ denotes a finite constant independent of $N$ whose value may
change from line to line.  The constants $r_0,c,c_3,c_P$ below are finite
but not made explicit.

\subsection{Reduction to one interference functional}
Let $P_B$ be the restriction to $\cB_N$ (not a spectral projection).  Write
$\widetilde r=S^N\phi_N$ for the free evolution of the resource on all of
$\Z^3$, and put
\[
r=P_B\widetilde r,\qquad a_c=P_BS^N(c_N\varphi_N\dn),\qquad
a_\up=P_BS^N(s_N\varphi_N\up),\qquad a_\dn=P_BS^N(s_N\varphi_N\dn).
\]
Since $\sigma_1\dn=\up$, $\sigma_2\dn=-i\up$ and $\sigma_3\dn=-\dn$, Bob's
encoded amplitude $P_B\psi_1$ is $v+ia_\dn$, $v+ia_\up$, $v+a_\up$ or
$v-ia_\dn$ for $M=I,\sigma_1,\sigma_2,\sigma_3$, where $v=r+a_c$.  Expanding
\eqref{eq:signal} with $E$ supported in $\cB_N$,
\begin{equation}\label{eq:Lexp}
\begin{aligned}
L_{I}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\dn\rangle+Q_I, &
L_{\sigma_3}&=2\re\langle r,Ea_c\rangle+2\im\langle r,Ea_\dn\rangle+Q_{\sigma_3},\\
L_{\sigma_1}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\up\rangle+Q_{\sigma_1}, &
L_{\sigma_2}&=2\re\langle r,Ea_c\rangle+2\re\langle r,Ea_\up\rangle+Q_{\sigma_2}.
\end{aligned}
\end{equation}
Each $Q_M$ is a sum of terms quadratic in $(a_c,a_\up,a_\dn)$.  For
example, $Q_I=\langle a_c,Ea_c\rangle+\langle a_\dn,Ea_\dn\rangle-2\im\langle a_c,Ea_\dn\rangle$.
Positivity of $E$ does not fix the sign of $L$, because the interference
terms can have either sign.

By Theorem~\ref{thm:rate}(d), $a_c,a_\up,a_\dn$ have $\ell^2$-norm at most
$T_N=O(N^4e^{-K_*N})$, so $Q_M=O(N^{8}e^{-2K_*N})$.  The free tail is only polynomially
small (Lemma~\ref{lem:tail}).  The $e^{-K_*N}$ sector therefore consists of
the linear interference terms.  Define, for $\chi\in\{\up,\dn\}$,
\[
\mathcal T_\chi(N)=e^{K_*N}\,\bigl\langle r,\,E\,S^N(s_N\varphi_N\chi)\bigr\rangle .
\]
Theorem~\ref{thm:main} follows from Theorem~\ref{thm:T} below.  The piece
$\langle r,Ea_c\rangle$ is $O(N^{-17/2}e^{-K_*N})$ by the same argument,
because $c_N=\Theta(N^{-4})$ in the relevant layer while $s_N=\Theta(N^{-2})$.

\subsection{Exact tilted representation}
Let $R=N/4$, $x_*=R\uhat$ and $y_*=N u-R\uhat$, so that $y_*-x_*=Nv_*$.  For
$f$ supported in $\cA_N$ and $w$ supported in $\cB_N$, put
\[
\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x),\qquad
\mathfrak B_w(\eta)=\sum_ye^{-i\eta\cdot(y-y_*)}e^{-\xi_*\cdot(y-y_*)}w(y)^\dagger .
\]
Let $\widetilde S_N(\eta)=e^{-N\Phi_*}S(\eta-i\xi_*)^N$.  By \eqref{eq:tilt}
with $\xi=\xi_*$, and using $\xi_*\cdot v_*-\Phi_*=K_*$,
\begin{equation}\label{eq:exactrep}
e^{K_*N}\sum_yw(y)^\dagger(S^Nf)(y)=\int_{\T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,\mathfrak A_f(\eta)\,e^{-iN\eta\cdot v_*}\,d\mu(\eta).
\end{equation}
This identity is exact: the sums are finite and no poles are crossed.

\subsection{The tilted symbol}\label{ssec:tilted}
\begin{lemma}\label{lem:symbol}
\begin{enumerate}[label=(\alph*)]
\item $S(-i\xi)$ is Hermitian for every real $\xi$, with $\det=1$.  At
  $\xi_*$, with $c_*=\cosh t_*$ and $s_*=\sinh t_*$,
  \[
  S(-i\xi_*)=\begin{pmatrix}c_*^2e^{-t_*}&-(1+ic_*)s_*\\-(1-ic_*)s_*&c_*^2e^{t_*}\end{pmatrix},
  \]
  with eigenvalues $e^{\pm\Phi_*}$, $e^{\Phi_*}=c_*^3+\sqrt{c_*^6-1}=3.97314\ldots$.
  The orthogonal projector onto the $e^{\Phi_*}$-eigenspace is
  \[
  P=\frac12\begin{pmatrix}1-\alpha&-(1+ic_*)\alpha/c_*^2\\-(1-ic_*)\alpha/c_*^2&1+\alpha\end{pmatrix}.
  \]
\item For all $p\in\C^3$: $S(p+\pi e_1)=-S(p)$, $S(p+\pi e_3)=-\sigma_3S(p)\sigma_3$,
  $S(p+\pi e_2)=-\sigma_3S(p)^T\sigma_3$ and $S(p+\pi(1,1,1))=-S(p)^T$.
\item The character $x\mapsto e^{i\eta_0\cdot x}$, $\eta_0\in\Sigma$,
  restricted to $\Lambda_0=\{u\in\Z^3:u_1+u_2+u_3=0\}$ is trivial if and only if
  $\eta_0\in\{0,\pi u\}$.
\item There is $r_0>0$ such that, for $|\eta|\le r_0$,
  $S(\eta-i\xi_*)=\lambda(\eta)P(\eta)+\lambda(\eta)^{-1}(I-P(\eta))$ with
  $\lambda,P$ analytic, $P(0)=P$, $\|P(\eta)-P\|\le c_P|\eta|$ and
  \[
  \lambda(\eta)=\exp\Bigl(\Phi_*+iv_*\cdot\eta-\tfrac12\eta^TQ\eta+\rho_3(\eta)\Bigr),\qquad
  |\rho_3(\eta)|\le c_3|\eta|^3\le\tfrac14\eta^TQ\eta .
  \]
  Here $Q=\Hess\Phi(\xi_*)=q_t(I-\uhat\uhat^T)+q_n\uhat\uhat^T$ with
  \[
  q_t=\frac{c_*}{D_*}=0.68956\ldots,\qquad
  q_n=\frac{c_*}{D_*}\frac{(c_*^2-1)(c_*^2+2)}{c_*^4+c_*^2+1}=0.30338\ldots,\qquad D_*=\sqrt{c_*^6-1}.
  \]
\item Outside $\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$,
  $\|\widetilde S_N(\eta)\|\le CNe^{-cN}$ for some $c>0$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) and (b) are identities between trigonometric polynomials and are checked
by expansion.  (c): $\Lambda_0$ is generated by $e_1-e_2$ and $e_2-e_3$, so
the character is trivial on it if and only if
$\eta_{0,1}\equiv\eta_{0,2}\equiv\eta_{0,3}\pmod{2\pi}$.  (d): the
eigenvalues of $S(\eta-i\xi_*)$ are
$\exp(\pm\arcosh f(\eta-i\xi_*))$ and
$f(\eta-i\xi)=\prod_j\cosh(\xi_j+i\eta_j)$.  Hence
$\log\lambda(\eta)=\Phi(\xi_*+i\eta)$, which is holomorphic near $\eta=0$
because $\Pi(\xi_*)>1$.  Taylor expansion gives $\nabla\Phi(\xi_*)=v_*$ and
$\Hess\Phi(\xi_*)=Q$.  The explicit Hessian is
$\Hess\Phi=\frac{\Pi}{D}\operatorname{diag}(\operatorname{sech}^2\xi_j)-\frac{\Pi}{D^3}(\tanh\xi_i\tanh\xi_j)$
with $D=\sqrt{\Pi^2-1}$.  The eigenvalues $\lambda^{\pm1}$ are separated
by the gap $e^{2\Phi_*}\approx15.8$, so the spectral projector is analytic.
(e): by Lemma~\ref{lem:specrad} and compactness,
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*-c'}$ away from $\Sigma$.  Conclude with
Lemma~\ref{lem:schur}.
\end{proof}

By (b), near $\pi u$ we have $S(\pi u+\eta-i\xi_*)^N=(-1)^N(S(\eta-i\xi_*)^N)^T$,
whose Perron projector is $P^T=\overline P$.  The other six points of
$\Sigma$ have the same spectral radius, but by (c) their characters are
non-trivial on the lattice planes $u\cdot x=k$.  This is why only $0$ and
$\pi u$ contribute at leading order (Lemma~\ref{lem:layers}(d)).

\subsection{Lattice-plane coordinates and profiles}
The planes $\{u\cdot x=k\}$ are orthogonal to $\xi_*$, and each is a translate
of the two-dimensional lattice $\Lambda_0$, of covolume $\sqrt3$.  Write
Alice's sites as $x=x_*-\delta\uhat+u_\perp$ with $u_\perp\perp\uhat$ and
depth $\delta=(\sqrt3R-u\cdot x)/\sqrt3$.  Since $u\cdot x\in\Z$,
\[
\sqrt3\,\delta=\theta_N+j,\qquad j\in\Z_{\ge0},\qquad \theta_N=\{\sqrt3R\}=\{\sqrt3N/4\}.
\]
Similarly $y=y_*+\delta'\uhat+u'_\perp$ with $\sqrt3\delta'=\theta_N+j'$, with
the \emph{same} $\theta_N$.  Then
$\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)$ and $\xi_*\cdot(y-y_*)=t_*(\theta_N+j')$.
Moreover $u\cdot(y-x)=3N-2\lfloor\sqrt3R\rfloor+j+j'$, so
$(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$.

On the plane at depth $\delta$, exactly,
\[
F_N=\frac{64}{N^2}\varepsilon_\perp^2,\qquad
\varepsilon_\perp=\delta-\frac{\delta^2}{2R}-\frac{|u_\perp|^2}{2R}\ \ (\ge0),
\]
and therefore
$s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6})$ and
$c_N=-\frac{512\pi^2}{N^4}\varepsilon_\perp^4+O(N^{-8})$ for $\delta=O(1)$.  The
same holds for $h_N$ with $\delta'$ and $u'_\perp$.  Replacing
$\varepsilon_\perp$ by $\delta-|u_\perp|^2/2R$ costs a relative $O(N^{-1})$.

\subsection{The free tail}
\begin{lemma}\label{lem:tail}
Uniformly in $y\in\Z^3$,
$\widetilde r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$, where
\[
R_0(w)=c_r\bigl[\mathcal I_0(|w|)\,I-\mathcal I_1(|w|)\,H_W(\hat w)\bigr]\dn,
\]
\[
\mathcal I_0(\rho)=4\pi\int_0^1k^2(1-k^2)^2\cos k\;j_0(k\rho)\,dk,\qquad
\mathcal I_1(\rho)=4\pi\int_0^1k^2(1-k^2)^2\sin k\;j_1(k\rho)\,dk .
\]
At the facing point $w_*=u-\uhat/4$, with $\rho_*=|w_*|=\sqrt3-\frac14$ and
$\hat w_*=\uhat$, one has
$R_0(w_*)=c_r\bigl(-\tfrac{\mathcal I_1}{\sqrt3}(1+i),\ \mathcal I_0+\tfrac{\mathcal I_1}{\sqrt3}\bigr)^T$,
with $\mathcal I_0=0.716577\ldots>0$ and $\mathcal I_1=0.132252\ldots>0$.
In particular $r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$ uniformly in $y\in\cB_N$,
and $r=0$ outside $\cB_N$.
\end{lemma}

\begin{proof}
For $|p|\le N^{-1}$, $S(p)=e^{-iH(p)}$ with $H$ Hermitian, analytic, and
$H-H_W=O(|p|^2)$.  Duhamel's formula gives
$\|S(p)^N-e^{-iNH_W(p)}\|\le CN|p|^2\le C/N$.  With $q=Np$,
$e^{-iH_W(q)}=\cos|q|-i\sin|q|\,H_W(\hat q)$, and the angular integrals of
$e^{-iq\cdot w}$ and $e^{-iq\cdot w}\hat q$ are $4\pi j_0$ and
$-4\pi ij_1\hat w$.  The resource enters through $g(Np)$ and is not
truncated.  The integrands defining $\mathcal I_0,\mathcal I_1$ are positive
because $k\rho_*<\pi$.  The value of $H_W(\uhat)\dn=(1+i,-1)^T/\sqrt3$ follows
by direct computation.
\end{proof}

The resource on Alice's sphere has the exact value
$N^{3/2}\varphi_N=\Phi_0(\frac14)=c_rI_b$ with
$I_b=16\pi\int_0^1k(1-k^2)^2\sin(k/4)\,dk$.  We write
$\varphi_\partial=c_rI_b$.

\subsection{Layer sums}
Let $\Psi_\delta(\tau)=\int_{\R^2}(\delta-|\sigma|^2)_+^2e^{i\tau\cdot\sigma}\,d^2\sigma$,
which is real and radial in $\tau$.  Define
\[
\cS_\pm(\tau;\theta)=\sum_{j\ge0}(\pm1)^je^{-t_*(\theta+j)}\,\Psi_{(\theta+j)/\sqrt3}(\tau),
\qquad
\Gamma_\pm(\theta)=\int_{\R^2}e^{-q_t|\tau|^2}\,\cS_\pm(\tau;\theta)^2\,d^2\tau .
\]

\begin{lemma}[Depth sums]\label{lem:depth}
Let $c_g=2\pi/(3\sqrt3)$ and $s_\omega=t_*+i\omega$.  Then
\[
\cS_+=\sum_{n\in\Z}\hat g_\tau(2\pi n)e^{2\pi in\theta},\qquad
\cS_-=\sum_{n\in\Z}\hat g_\tau\bigl(\pi(2n+1)\bigr)e^{i\pi(2n+1)\theta},\qquad
\hat g_\tau(\omega)=c_g\,\frac{e^{-|\tau|^2/(4\sqrt3\,s_\omega)}}{s_\omega^4}.
\]
Consequently $|\cS_+-\hat g_\tau(0)|\le c_g/720$ and $|\cS_-|\le c_g/48$.
Moreover
\[
\overline\Gamma:=\int e^{-q_t|\tau|^2}\hat g_\tau(0)^2d^2\tau=\frac{c_g^2}{t_*^8}\frac{\pi}{q_t+\frac1{2\sqrt3t_*}}=49.44186\ldots,
\qquad |\Gamma_+-\overline\Gamma|\le\varepsilon_+,\qquad 0\le\Gamma_-\le\varepsilon_-,
\]
with
$\varepsilon_+=2\frac{c_g}{720}\frac{c_g}{t_*^4}\frac{\pi}{q_t+1/(4\sqrt3t_*)}+\bigl(\frac{c_g}{720}\bigr)^2\frac\pi{q_t}=0.04917\ldots$
and $\varepsilon_-=\bigl(\frac{c_g}{48}\bigr)^2\frac\pi{q_t}=0.00289\ldots$.
\end{lemma}

\begin{proof}
Radially, $\Psi_\delta(\tau)=\pi H(\delta)$ with
$H(\delta)=\int_0^\delta(\delta-s)^2J_0(|\tau|\sqrt s)\,ds$.  So $H'''=2J_0(|\tau|\sqrt\delta)$
and $H(0)=H'(0)=H''(0)=0$.  Since
$\int_0^\infty e^{-ps}J_0(|\tau|\sqrt s)\,ds=e^{-|\tau|^2/4p}/p$, the function
$g_\tau(x)=e^{-t_*x}\Psi_{x/\sqrt3}(\tau)\mathbf 1_{x\ge0}$ has Fourier
transform $\hat g_\tau$ as stated.  It is continuous, vanishing to third
order at $x=0$, and $\hat g_\tau\in\ell^1(2\pi\Z)$.  Poisson summation is
therefore exact.  The bounds use $|e^{-|\tau|^2/(4\sqrt3s)}|\le1$,
$|s_{2\pi n}|\ge2\pi|n|$, $\sum_{n\ne0}(2\pi n)^{-4}=1/720$ and
$\sum_n|\pi(2n+1)|^{-4}=1/48$.  The Gaussian integrals are elementary.
\end{proof}

\begin{lemma}[Layers]\label{lem:layers}
Let $\chi\in\{\up,\dn\}$, $f=s_N\varphi_N\chi$, $w=h_N\,M_B\,r$ and
$\tau=\sqrt{N/2}\,\eta_t$, where $\eta=\eta_n\uhat+\eta_t$ with
$\eta_t\perp\uhat$.
\begin{enumerate}[label=(\alph*)]
\item $|\mathfrak A_f(\eta)|,\ \|\mathfrak B_w(\eta)\|\le CN^{-5/2}$ for all $\eta$.
\item For $|\eta|\le r_0$,
  \[
  \mathfrak A_f(\eta)=N^{-5/2}\tfrac{16\pi}{\sqrt3}\varphi_\partial\bigl[\cS_+(\tau;\theta_N)+\mathcal E_A\bigr]\chi,\qquad
  \mathfrak B_w(\eta)=N^{-5/2}\tfrac{32}{\sqrt3}\,R_0(w_*)^\dagger M_B\bigl[\cS_+(\tau;\theta_N)+\mathcal E_B\bigr],
  \]
  with $|\mathcal E_{A,B}|\le C(N^{-1/2}+|\eta_n|)$.
\item Near $\pi u$ the same holds with $\cS_-$ in place of $\cS_+$.  The
  alternating sign comes from the parity $(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$,
  combined with $S^N\mapsto(-1)^N(S^N)^T$.
\item For $\eta_0\in\Sigma\setminus\{0,\pi u\}$ and $|\eta|\le r_0$,
  $|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Decompose the sums into lattice planes.  On the plane at depth
$\delta=(\theta_N+j)/\sqrt3$ the tilt weight is $e^{-t_*(\theta_N+j)}$.  The
profile $s_N\varphi_N$ is supported in a disc of radius
$\varrho=\sqrt{2R\delta-\delta^2}=O(\sqrt N)$ and has size $O(N^{-7/2}\delta^2)$.
Planes with $\delta>R/2$ contribute $O(e^{-cN})$.  This gives (a).

For (b), apply Poisson summation on each plane.  The $m=0$ term is
$\frac1{\sqrt3}\int e^{i\eta_t\cdot u_\perp}G_0(u_\perp)\,d^2u_\perp$.  The
terms $m\ne0$ are bounded by $\|\partial^3G_0\|_{\mathcal M}|2\pi m-\eta_t|^{-3}$,
since the profile vanishes quadratically on the rim and its third
derivative is a finite measure.  After the weighted depth sum, they give a
relative error $O(N^{-3/2})$.  In the $m=0$ term, use the profile
expansions, $\varphi_N=N^{-3/2}\varphi_\partial(1+O(|u_\perp|/N+\delta/N))$ and
$|e^{-i\eta_n\delta}-1|\le|\eta_n|\delta$.  With the substitution
$u_\perp=\sqrt{2R}\,\sigma$,
\[
\int e^{i\eta_t\cdot u_\perp}\Bigl(\delta-\frac{|u_\perp|^2}{2R}\Bigr)_+^2d^2u_\perp=2R\,\Psi_\delta(\tau).
\]
Collecting the factors
$\frac1{\sqrt3}\cdot\frac{32\pi}{N^2}\cdot N^{-3/2}\varphi_\partial\cdot2R$ gives
the prefactor of $\mathfrak A_f$.  For $\mathfrak B_w$ the factors are
$\frac1{\sqrt3}\cdot\frac{64}{N^2}\cdot N^{-3/2}R_0(w_*)^\dagger\cdot2R$, using
Lemma~\ref{lem:tail}, the smoothness of $R_0$ and $M_B^\dagger=M_B$.  (c)
follows from Lemma~\ref{lem:symbol}(b) and the parity identity.  (d): by
Lemma~\ref{lem:symbol}(c), the character is non-trivial on each plane.  The
Poisson sum therefore has no $m=0$ term, and the remaining terms are
$O(N^{-4})$.
\end{proof}

\subsection{Assembly}
\begin{theorem}\label{thm:T}
For $\chi\in\{\up,\dn\}$ and each $M_B$,
\[
\mathcal T_\chi(N)=N^{-13/2}\,\cK\,c_r\bigl[\Gamma_+(\theta_N)\,x_0+\Gamma_-(\theta_N)\,x_\pi\bigr]+O(N^{-7}),
\]
where $x_0=\tilde R^\dagger M_BP\chi$, $x_\pi=\tilde R^\dagger M_B\overline P\chi$,
$\tilde R=R_0(w_*)/c_r$ and
\[
\cK=\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}\;\varphi_\partial=1.749269\ldots .
\]
\end{theorem}

\begin{proof}
Insert Lemmas~\ref{lem:symbol} and~\ref{lem:layers} into
\eqref{eq:exactrep}.  Away from the balls $B(\eta_0,r_0)$ the contribution is
$O(Ne^{-cN}N^{-5})$.  The six points of $\Sigma$ with non-trivial
characters give $O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})=O(N^{-8})$, using the
Gaussian decay of $\widetilde S_N$.  Near $\eta_0\in\{0,\pi u\}$ we make
three replacements.  First, $\widetilde S_Ne^{-iN\eta\cdot v_*}$ is replaced
by $e^{-N\eta^TQ\eta/2}P$ (respectively $\overline P$), at cost
$N^{-5}\int(c_P|\eta|+Nc_3|\eta|^3)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.
Second, the layers are replaced by their leading forms, at cost
$N^{-5}\int(N^{-1/2}+|\eta_n|)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.  Third,
the integral is extended to $\R^3$, at cost $O(e^{-cNr_0^2})$.  What
remains is
\[
N^{-5}\,\frac{512\pi}{3}\,\varphi_\partial\,c_r\,x_{0,\pi}\,\sqrt{\frac{2\pi}{Nq_n}}\;\frac2N\;(2\pi)^{-3}\int_{\R^2}e^{-q_t|\tau|^2}\cS_\pm^2\,d^2\tau .
\]
Here we used $d^2\eta_t=(2/N)d^2\tau$ and
$N\eta^TQ\eta/2=Nq_n\eta_n^2/2+q_t|\tau|^2$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:main}]
By \eqref{eq:Lexp}, the $e^{-K_*N}N^{-13/2}$ sector of $L_{M,M_B}$ is
$\ell(\mathcal T_\chi)$, where $\ell$ is the real-linear functional
$-2\im$ for $M\in\{I,\sigma_1\}$, $+2\im$ for $M=\sigma_3$ and $+2\re$ for
$M=\sigma_2$, and $\chi=\dn$ for $M\in\{I,\sigma_3\}$, $\chi=\up$ for
$M\in\{\sigma_1,\sigma_2\}$.  Since $\cK$, $c_r$ and $\Gamma_\pm$ are real,
Theorem~\ref{thm:T} gives \eqref{eq:C} with $\ell_0=\ell(x_0)$ and
$\ell_\pi=\ell(x_\pi)$.  Closed forms of $\ell_0,\ell_\pi$ in terms of
$\alpha,c_*,\mathcal I_0,\mathcal I_1$ are listed in
Appendix~\ref{app:numerics}.

The remainder budget, relative to $N^{-13/2}$, is as follows:
\begin{itemize}
\item $O(N^{-1/2})$ from the cubic term of the exponent, from
  $P(\eta)-P$, from the normal phase, and from the variation of
  $\varphi_N$ and $R_0$ across the layer;
\item $O(N^{-1})$ from $r-N^{-3/2}R_0$ and from the exact profile and disc
  geometry;
\item $O(N^{-3/2})$ from in-plane Poisson terms and from the six
  non-contributing torus points;
\item $O(N^{-2})$ from $2\re\langle r,Ea_c\rangle$;
\item exponentially small terms from the region away from $\Sigma$ and from
  the sector $e^{-2K_*N}$.
\end{itemize}
Hence $L=e^{-K_*N}N^{-13/2}(C(\theta_N)+R_N)$ with $|R_N|\le C'N^{-1/2}$.

For non-vanishing, note that $\Gamma_-\ge0$.  For every pair, interval
arithmetic certifies $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$.
Therefore $C(\theta)$ has the sign of $\ell_0$ for every $\theta$, and
$|C(\theta)/\overline C-1|\le(\varepsilon_+|\ell_0|+\varepsilon_-|\ell_\pi|)/(\overline\Gamma|\ell_0|)$,
which gives the bounds of Table~\ref{tab:C}.  Since
$\inf_\theta|C(\theta)|\ge(1-1.5\cdot10^{-3})|\overline C|>0$, the remainder
cannot cancel the leading term for $N$ large, and the asymptotics of
$\delta=|L|$ follow.
\end{proof}

\begin{remark}[Counting the power]
The exponent $13/2$ decomposes as follows.  The resource contributes
$\frac32$ at the layer and the free tail $\frac32$ at Bob.  The profiles
$s_N$ and $h_N$ contribute $2+2$.  The two in-plane areas contribute $-2$.
The normal Gaussian contributes $\frac12$, and the tangential rescaling
$d^2\eta_t=(2/N)d^2\tau$ contributes $1$.  The depths $j,j'$ are discrete
sums of size $O(1)$ and contribute no power.  The common tangential
direction $u_\perp+u'_\perp$ is a flat direction of the exponent, because
$\xi_*$ is orthogonal to the planes.  It is confined by the profiles and
produces the area factors, not a Gaussian factor.
\end{remark}

\begin{remark}[Dependence on $\theta_N$]
Since $\sqrt3/4\notin\mathbb Q$, the sequence $\theta_N$ is equidistributed.
$C(\theta_N)$ is therefore quasi-periodic in $N$ and not a constant.  The
oscillation comes from the commensurability of the lattice planes with the
spheres bounding the regions.  It is below $0.15\%$, and it never changes
the sign.
\end{remark}

\section{Discussion}\label{sec:discussion}

\subsection{What the theorem says and does not say}
The theorem is a statement about one walk and one explicitly specified
family of operations.  It shows that the gap between the emergent
relativistic cone and the microscopic causal support is not merely
geometric.  Under an infrared-controlled protocol it carries an
operational response whose asymptotic law is known exactly: rate, power
and coefficient.  It does not claim that $D_B>0$ for every protocol, that
every quantum walk behaves this way, or that every smooth encoder
$M=aI+b\cdot\sigma$ signals.  It is not a violation of the model's
microcausality, since Bob remains inside $N\Cmicro$.  The limit
$N\to\infty$ is an infrared scaling at fixed lattice units, not a continuum
limit $a,\tau\to0$.

The result is asymptotic.  The remainder constants and $N_*$ are finite but
not explicit.  The finite-$N$ diagnostics of Appendix~\ref{app:numerics}
indicate an effective relative correction of about $-100/N$.  The leading
formula is therefore quantitatively reliable only for $N\gtrsim10^3$.  For
$M\in\{I,\sigma_3\}$ with $M_B=I$, whose coefficient is among the smallest,
the $N^{-17/2}$ term dominates over the whole diagnostic range.

\subsection{Physical reading}
Restoring a lattice spacing $a$, the integer $N$ is both the number of
steps and the separation scale in lattice units, so $N\sim\ell/a$ for a
separation $\ell$, and $\delta\sim e^{-K_*N}$ up to algebraic factors.  The
response is therefore negligible at any separation large compared with the
lattice spacing, and by the preceding subsection the leading formula becomes
accurate only for $N\gtrsim10^3$.  We make no claim about observability, and
regard the result as a statement in the mathematical physics of finite-range
unitary dynamics.
Its interest lies in the structure it exhibits: an exact separation between
ballistic propagation, which respects $\cIR$, and operational influence,
which does not vanish inside the corona even under infrared control.

\subsection{Open problems}
\begin{enumerate}[label=(\arabic*)]
\item General encoders $M=aI+b\cdot\sigma$, and optimisation over
  admissible operations.
\item Other walks, in particular the Bialynicki-Birula walk
  \cite[Eq.~(5.12)]{CJWW}, whose corona contains ballistic modes faster than
  $\cIR$, and the massive Dirac case.
\item Explicit remainder constants and $N_*$, which would make the
  statement effective at finite $N$.
\item Many-particle and second-quantized versions.  The upper bound
  extends to even local unitaries on the full CAR algebra, with prefactor
  $288N^7$ in place of $36N^4$~\cite{Repo}, but no lower bound is available
  there.
\end{enumerate}

\appendix

\section{Computer-assisted parts and diagnostics}\label{app:numerics}

Theorem~\ref{thm:upper}, together with Lemma~\ref{lem:ellipse}, is
formally verified in Lean~4/Mathlib (\texttt{formal/} in~\cite{Repo}).  The
asymptotic results (Theorems~\ref{thm:rate} and~\ref{thm:main}) are not.
The analytic arguments above are complete up to the following verified
computations.  All of them are performed by the certificate scripts listed
in~\cite{Repo}, at the commit given there, with Python~3.12.3, SymPy~1.14.0
and mpmath~1.3.0.  Exact identities use SymPy.  Enclosures use the interval
context \texttt{mpmath.iv} with 50 digits, and only its elementary
operations: the four arithmetic operations, integer powers by repeated
multiplication, $\sqrt{\cdot}$, $\exp$, $\log$, $\sin$, $\cos$ and $\pi$.
No interval quadrature is used: $\mathcal I_0(\rho_*)$, $\mathcal I_1(\rho_*)$
and $I_b$ are enclosed through exact closed forms in $\sin$ and $\cos$,
obtained from the moments $\int_0^1k^m\{\sin,\cos\}(\omega k)\,dk$, $m\le5$,
which are checked symbolically.
\begin{itemize}
\item The symbol identities: Lemma~\ref{lem:jumps}, \eqref{eq:SOS}, and
  Lemma~\ref{lem:symbol}(a)--(b).  Also the ellipse-lemma polynomials,
  $\cosh^3(\log2)=125/64$ and the vertex blocks.
\item Closed forms and enclosures of $t_*$, $K_*$, $c_*^2$, $\Phi_*$,
  $q_t$, $q_n$, $P$, $\mathcal I_0$, $\mathcal I_1$, $\varphi_\partial$, $\cK$,
  $\overline\Gamma$ and $\varepsilon_\pm$.
\item The sixteen pairs $(\ell_0,\ell_\pi)$, the sign margin
  $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$, the
  bounds of Table~\ref{tab:C}, and $C(\sigma_3,\cdot)=-C(I,\cdot)$.
\end{itemize}
Closed forms of $\ell_0,\ell_\pi$ are given below, with $c=c_*$,
$A=\mathcal I_0(\rho_*)$ and $B=\mathcal I_1(\rho_*)$.  The rows for
$\sigma_3$ are the negatives of the rows for $I$.

{\small
\[
\begin{array}{lll}
\toprule
(M,M_B) & \ell_0 & \ell_\pi\\
\midrule
(I,I),(I,P_3) & -\frac{\sqrt3}{3}\frac{B\alpha(c-1)}{c^2} & +\frac{\sqrt3}{3}\frac{B\alpha(c+1)}{c^2}\\[3pt]
(I,P_1) & \frac{3Ac\alpha-\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2} & -\frac{3Ac\alpha+\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}\\[3pt]
(I,P_2) & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2+c\alpha-2\alpha)}{6c^2} & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2-c\alpha-2\alpha)}{6c^2}\\[3pt]
(\sigma_1,I) & -\frac{3A\alpha+\sqrt3B(c-c\alpha+\alpha)}{3c} & \frac{3A\alpha-\sqrt3B(c-c\alpha-\alpha)}{3c}\\[3pt]
(\sigma_1,P_1) & -\frac{3Ac\alpha+\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2} & \frac{3Ac\alpha-\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_2) & -\frac{3A(c^2(1-\alpha)+c\alpha)+\sqrt3B(2c^2(1-\alpha)+2c\alpha-\alpha)}{6c^2} & -\frac{3A(c^2(1-\alpha)-c\alpha)+\sqrt3B(2c^2(1-\alpha)-2c\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_3),(\sigma_2,P_3) & -\frac{\sqrt3}{3}B(1-\alpha) & -\frac{\sqrt3}{3}B(1-\alpha)\\[3pt]
(\sigma_2,I) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}\\[3pt]
(\sigma_2,P_1) & -\frac{3A(\alpha-c^2(1-\alpha))+\sqrt3Bc\alpha}{6c^2} & -\frac{3A(\alpha-c^2(1-\alpha))-\sqrt3Bc\alpha}{6c^2}\\[3pt]
(\sigma_2,P_2) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+c\alpha+2\alpha)}{6c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)-c\alpha+2\alpha)}{6c^2}\\
\bottomrule
\end{array}
\]
}

\medskip\noindent\emph{Finite-$N$ diagnostics.}  These are floating-point
and not used in any proof; they use NumPy~1.26.4 and are produced by the
\texttt{--diagnostics} option of the coefficient certificate~\cite{Repo}.  A
floating-point FFT evaluation of the exact discrete convolution formula in
tilted variables (``brute'') was compared with a reference that keeps the
exact lattice geometry but replaces the kernel by its Gaussian form at the
eight points of $\Sigma$.  Their ratio tends to $1$ with deviation of order
$c/N$, $c\in[-0.5,14]$, at $N=24,40,56$.  For $M\in\{I,\sigma_3\}$ and
$M_B=I$, the ratio of the $N^{-17/2}$ piece $2\re\langle r,Ea_c\rangle$ to
the piece $2\im\langle r,Ea_\dn\rangle$ that carries the $N^{-13/2}$ term is
$15.2$, $9.4$ and $6.4$ at $N=24,40,56$.  A semi-analytic evaluation with discrete
planes and exact profiles gives semi/lead $=0.906$, $0.990$ and $0.997$ at
$N=10^3$, $10^4$ and $3\cdot10^4$, consistent with a relative correction
$\approx-100/N$.  The free tail agrees with $N^{-3/2}R_0$ to relative
accuracy $2\cdot10^{-6}$ at $N=40$ and $8\cdot10^{-9}$ at $N=640$.

\begin{thebibliography}{99}

\bibitem{AVWW}
A.~Ahlbrecht, H.~Vogts, A.~H.~Werner, R.~F.~Werner,
\emph{Asymptotic evolution of quantum walks with random coin},
arXiv:1009.2019.

\bibitem{Arrighi}
P.~Arrighi,
\emph{An overview of quantum cellular automata},
arXiv:1904.12956.

\bibitem{BBBP}
Y.~Baryshnikov, W.~Brady, A.~Bressler, R.~Pemantle,
\emph{Two-dimensional quantum random walk},
J.\ Stat.\ Phys.\ \textbf{142}, 78--107 (2011), arXiv:0810.5495.

\bibitem{BialynickiBirula}
I.~Bialynicki-Birula,
\emph{Weyl, Dirac, and Maxwell equations on a lattice as unitary cellular automata},
Phys.\ Rev.\ D \textbf{49}, 6920 (1994), arXiv:hep-th/9304070.

\bibitem{BDPT}
A.~Bisio, G.~M.~D'Ariano, P.~Perinotti, A.~Tosini,
\emph{Free quantum field theory from quantum cellular automata: derivation of Weyl, Dirac and Maxwell quantum cellular automata},
arXiv:1601.04832.

\bibitem{BHS}
L.~Bombelli, J.~Henson, R.~D.~Sorkin,
\emph{Discreteness without symmetry breaking: a theorem},
arXiv:gr-qc/0605006.

\bibitem{BHV}
S.~Bravyi, M.~B.~Hastings, F.~Verstraete,
\emph{Lieb--Robinson bounds and the generation of correlations and topological quantum order},
Phys.\ Rev.\ Lett.\ \textbf{97}, 050401 (2006), arXiv:quant-ph/0603121.

\bibitem{CRT}
H.~A.~Carteret, B.~Richmond, N.~M.~Temme,
\emph{Evanescence in coined quantum walks},
J.\ Phys.\ A: Math.\ Gen.\ \textbf{38}, 8641--8665 (2005), arXiv:quant-ph/0506048.

\bibitem{CJWW}
C.~Cedzich, A.~Joye, A.~H.~Werner, R.~F.~Werner,
\emph{Exponential tail estimates for quantum lattice dynamics},
Ann.\ Henri Poincar\'e \textbf{27}, 2843--2870 (2026), doi:10.1007/s00023-025-01598-4, arXiv:2408.02108.

\bibitem{DArianoErbaPerinotti}
G.~M.~D'Ariano, M.~Erba, P.~Perinotti,
\emph{Isotropic quantum walks on lattices and the Weyl equation},
Phys.\ Rev.\ A \textbf{96}, 062101 (2017), arXiv:1708.00826.

\bibitem{DArianoPerinotti}
G.~M.~D'Ariano, P.~Perinotti,
\emph{Derivation of the Dirac equation from principles of information processing},
Phys.\ Rev.\ A \textbf{90}, 062106 (2014), arXiv:1306.1934.

\bibitem{Farrelly}
T.~Farrelly,
\emph{A review of quantum cellular automata},
Quantum \textbf{4}, 368 (2020), arXiv:1904.13318.

\bibitem{GJS}
G.~Grimmett, S.~Janson, P.~F.~Scudo,
\emph{Weak limits for quantum random walks},
Phys.\ Rev.\ E \textbf{69}, 026119 (2004), arXiv:quant-ph/0309135.

\bibitem{Konno}
N.~Konno,
\emph{Quantum random walks in one dimension},
Quantum Inf.\ Process.\ \textbf{1}, 345--354 (2002).

\bibitem{LiebRobinson}
E.~H.~Lieb, D.~W.~Robinson,
\emph{The finite group velocity of quantum spin systems},
Commun.\ Math.\ Phys.\ \textbf{28}, 251--257 (1972).

\bibitem{ACSV}
R.~Pemantle, M.~C.~Wilson, S.~Melczer,
\emph{Analytic Combinatorics in Several Variables}, 2nd ed.,
Cambridge University Press (2024), doi:10.1017/9781108874144.

\bibitem{Repo}
Repository \texttt{nacho09021973/qca-causal-cones},
% TODO(author): replace by an archived release (tag and DOI) before submission.
\url{https://github.com/nacho09021973/qca-causal-cones}, commit
\texttt{551addabe28b} (branch \texttt{research/b-infinity-post-s4-gate}).
Certificates
\texttt{scripts/verify\_scaled\_ir\_gate.py},
\texttt{scripts/verify\_regional\_directional\_asymptotics\_gate.py},
\texttt{scripts/verify\_regional\_laplace\_coefficient\_gate.py},
\texttt{scripts/verify\_directional\_saturation.py}; Lean formalization in
\texttt{formal/}.

\bibitem{SchumacherWerner}
B.~Schumacher, R.~F.~Werner,
\emph{Reversible quantum cellular automata},
arXiv:quant-ph/0405174.

\bibitem{SunadaTate}
T.~Sunada, T.~Tate,
\emph{Asymptotic behavior of quantum walks on the line},
J.\ Funct.\ Anal.\ \textbf{262}, 2608--2645 (2012), arXiv:1108.1878.

\end{thebibliography}

\end{document}
```

### Contexto adjunto: reports/2026-09-17--regional-laplace-coefficient-gate.md
```
# REGIONAL_LAPLACE_COEFFICIENT_GATE — ejecución del contrato publicado

Registro de ejecución, 2026-09-17. Evaluación del autor; **sin revisión
independiente** ni promoción canónica. Etiquetas: [A] prueba analítica;
[V] identidad o enclosure de intervalo del certificado; [D] diagnóstico
numérico `SUPPORTED` (nunca decide \(\beta\), \(C\) ni el estado).
**No se ha modificado el charter.**

**Resultado (autor): `PAULI_LEADING_COEFFICIENT_NONVANISHING`.**

Para los dieciséis pares,

\[
L_{M,M_B}(N)=e^{-K_*N}\,N^{-13/2}\Bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\Bigr),
\qquad \theta_N=\Bigl\{\tfrac{\sqrt3\,N}{4}\Bigr\}\in[0,1),
\]

con \(\beta=13/2\) derivado (no por recuento de direcciones gaussianas) y
\(C_{M,M_B}(\theta)\) el coeficiente **completo**: la interferencia de la
cola libre \(r\) con la capa del encoder, sumada sobre los dos saddles de
toro que sobreviven, las capas discretas de Alice y Bob, el Hessiano, los
perfiles y el proyector de Perron con sus fases. Para cada par

\[
C_{M,M_B}(\theta)=\overline C_{M,M_B}\,\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad |\vartheta_{M,M_B}|\le 1.47\times10^{-3}\ \ \forall\theta,
\qquad \overline C_{M,M_B}\neq0\ \ [V].
\]

Dos precisiones de alcance que el revisor debe mirar primero:

1. **El coeficiente no es una constante de \(N\).** Depende de
   \(\theta_N\) (conmensurabilidad de los planos de red
   \(x_1+x_2+x_3=k\) con las esferas). La oscilación está acotada
   rigurosamente por \(1.5\times10^{-3}\) relativo y no cambia el signo; la
   no nulidad es uniforme en \(\theta\). El ansatz del charter con \(C\)
   constante se cumple sólo con \(C\to C(\theta_N)\) (§14).
2. **El resto está controlado asintóticamente, no con constantes
   explícitas.** \(R_N=O(N^{-1/2})\) [A]. Los diagnósticos [D] muestran
   una corrección efectiva \(\approx-100/N\): la fórmula líder es
   cuantitativamente fiable sólo para \(N\gtrsim10^3\) (§13).

## 1. Preflight

- Repositorio `nacho09021973/qca-causal-cones`, rama
  `research/b-infinity-post-s4-gate`.
- `HEAD`, `origin/research/b-infinity-post-s4-gate` y
  `git ls-remote origin research/b-infinity-post-s4-gate`:
  `6f520ada13151b864fd77bd9c2ead0ddb1cb7fbb`, idénticos al baseline exigido.
- Charter `theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md`:
  `git rev-parse HEAD:<charter>` = `git hash-object <charter>` =
  `18d1f65a662e31a4c44a9d61c0b31e3fc09d56d0` (blob exigido);
  SHA256 `234f94a73bf0af1160e528c854774af256254cba0aa4f0d6afb09c9336de878d`
  (fijado en el check 1 del certificado).
- Sin cambios tracked (ni staged ni unstaged) al arrancar.
- Cuatro untracked históricos, preservados byte a byte:

  | Archivo | SHA256 |
  | --- | --- |
  | `Auditoría De Novedad Matemática.md` | `a5e2f98e74231be68641b73493d67a36d7ee1a891dc0985ce850899a5c2b92f1` |
  | `debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.log` | `b33727d824f711b1f4b8919870ea9edf6ef0b67cbeb91936fe7cb07e639bb1fa` |
  | `debates/2026-09-16--ratificacion-gate-completitud-axial-n3.log` | `d4855e39d9800733fae01d3454cf14443d0b4aab1ce830fa58c21e57fe091486` |
  | `scripts/__pycache__/` (dos `.pyc`) | `39fa4fc6…a44272`, `d3eeec7b…fbe732` |

- SHA256 de `state/CURRENT_STATE.md` al arrancar:
  `075f92b5cb1a107e90246c8d9e666780409793774663c42679a7d41ba2d3598e`.
  **No se modifica.** Todo Python con `-B`.

Leídos íntegramente antes de calcular: el charter; el informe y la
revisión independiente de §8.19; el informe y la revisión de §8.18; el
informe de §8.17 (para (L), (F), la cota de Schur (P) y el lema de
elipses (E)); `CURRENT_STATE` §§8.16–8.20; el certificado de §8.19 y, de
`verify_directional_saturation.py`, sólo `walk2`, `PS`, `PAULI`,
`laurent`, `is_zero`.

**Lógica terminal reconstruida antes del cálculo** (orden del charter §4):
(i) \(\beta\) identificado y algún par Pauli con \(C\neq0\) controlado
frente al resto, sumadas todas las contribuciones de tasa \(K_*\);
(ii) \(C=0\) en los dieciséis (o en todos los Pauli) con primer
\(C^{(j)}\) clasificado; (iii) sólo \(M=I\) con \(C\neq0\); (iv) en
cualquier otro caso `OPEN`. Candado: un término \(e^{-2K_*N}\) no es un
\(C^{(j)}N^{-j}\) del sector \(e^{-K_*N}\); \(K_*\) no se reoptimiza.

## 2. Premisas heredadas (Paso 0)

| Premisa | Fuente | Uso |
| --- | --- | --- |
| \(K_*=I(v_*)=3\alpha t_*-\operatorname{arccosh}(\cosh^3t_*)\), \(v_*=\alpha(1,1,1)\), \(\alpha=1-\frac1{2\sqrt3}\), \(\xi_*=t_*(1,1,1)\) | §8.19, PASS | tilt fijo del contorno |
| \(J<K_*<\log4\) | §8.19 | consistencia [V] |
| \(\hat u\cdot(y-x)\ge N\lvert v_*\rvert\) en \(A_N\times B_N\), igualdad sólo en el par enfrentado | §§8.18–8.19 | \(\xi_*\cdot(y-x)\ge N\xi_*\cdot v_*\) |
| perfiles \(O(\log N)\), desplazamiento \(O(1)\), \(K_*\) intacto | §8.19 | capa de profundidad \(O(1)\) |
| (L), (F), columnas \(v\pm id\), \(v+ib\), \(v+b\) | §8.17 [V] | sectores (§10) |
| \(r=P_BS^N\phi_N=O(N^{-3/2})\) en \(B_N\) | §§8.17–8.18 | aquí se deriva su coeficiente (§9) |
| lema de elipses (E) y cota de Schur (P) | §8.17, PASS | Lema 1 |

Valores [V] (enclosures de intervalo de 50 dígitos): \(t_*=0.735752814420\),
\(K_*=0.190518929584\), \(\cosh^2t_*=C_*^2=\alpha(\alpha+\sqrt{4-3\alpha^2})/(2(1-\alpha^2))=1.64634199258\)
(algebraico), \(e^{\varphi_*}=C_*^3+\sqrt{C_*^6-1}=3.97314862735\).

**Precisión sobre §8.19 (no reabre la tasa).** El informe de §8.19 afirma
que el máximo de \(\rho(S(\eta-i\xi_*))\) en el toro es único en
\(\eta=0\). No lo es: \(\cos(\pi-i\xi)=-\cosh\xi\) también es vértice real
de su elipse, y la igualdad se alcanza en los **ocho** puntos
\(\Sigma=\{0,\pi\}^3\) (§3.3). \(K_*\) y la cota de Legendre no cambian
(los ocho tienen el mismo radio espectral). Sí importa para el
coeficiente, y se trata aquí completo. Los archivos de §8.19 no se tocan.

## 3. Coordenadas locales del saddle

### 3.1 Representación exacta inclinada [A]

Para campos espinoriales \(f\) soportado en \(A_N\) y \(w\) en \(B_N\),
\(T[w,f]:=\sum_y w(y)^\dagger(S^Nf)(y)\). Con \(x_*=R\hat u\),
\(y_*=N(1,1,1)-R\hat u\), \(R=N/4\), \(y_*-x_*=Nv_*\),

\[
\mathfrak A_f(\eta)=\sum_x e^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x),\qquad
\mathfrak B_w(\eta)=\sum_y e^{-i\eta\cdot(y-y_*)}e^{-\xi_*\cdot(y-y_*)}w(y)^\dagger,
\]

\[
\boxed{e^{K_*N}\,T[w,f]=\int_{\mathbb T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,
\mathfrak A_f(\eta)\,e^{-i\eta\cdot Nv_*}\,d\mu(\eta),\qquad
\widetilde S_N(\eta)=e^{-N\varphi_*}S(\eta-i\xi_*)^N.}
\]

Es exacta: las sumas son finitas, el integrando es entero y
\(2\pi\)-periódico, y el desplazamiento \(p\mapsto\eta-i\xi_*\) no cruza
polos. \(e^{-\xi_*\cdot(y_*-x_*)+N\varphi_*}=e^{-K_*N}\).

### 3.2 Coordenadas de red [A]/[V]

Los planos \(\{x_1+x_2+x_3=k\}\) son ortogonales a \(\xi_*\). En cada uno
los sitios forman una traslación de la red 2D \(\Lambda_0\) (covolumen
\(\sqrt3\)). Coordenadas **exactas**:

- Alice: \(x=x_*-\delta\hat u+u\), \(u\perp\hat u\), profundidad
  \(\delta=(\sqrt3R-k_x)/\sqrt3=(\theta_N+j)/\sqrt3\), \(j\in\mathbb Z_{\ge0}\);
- Bob: \(y=y_*+\delta'\hat u+u'\), \(\delta'=(\theta_N+j')/\sqrt3\);
- \(y-x=Nv_*+(\delta+\delta')\hat u+(u'-u)\) y
  \(\xi_*\cdot(y-x)=N\xi_*\cdot v_*+t_*(2\theta_N+j+j')\).

El mismo \(\theta_N=\{\sqrt3N/4\}\) gobierna Alice y Bob. Paridad [V]:
\(k_y-k_x=3N-2\lfloor\sqrt3R\rfloor+j+j'\), luego
\((-1)^{N+k_y-k_x}=(-1)^{j+j'}\).

### 3.3 Los ocho puntos de toro [A]/[V]

**Lema 1.** Sea \(\Sigma=\{0,\pi\}^3\).

(a) \(\rho(S(\eta-i\xi_*))\le e^{\varphi_*}\), con igualdad **sii**
\(\eta\in\Sigma\). *Prueba.* Cada \(\cos(\eta_j-it_*)\) está en la frontera
de \(E_{\cosh t_*}\). En la prueba de (E) (§8.17),
\(I-L^TL\) tiene \(g_{11}=(1-u)(C-1)/(AC-1)\) y
\(\det=(C-1)(1-u)[A-1+C(1-u)]/(AC(AC-1))\), \(u=\cos^2p\): si
\(\sin\eta_j\neq0\) ambos son \(>0\), \(\|L\|<1\) y el producto cae en el
**interior** de \(E_{C^3}\); si ya un factor es interior, \(|Lu|<1\).
Interior de la elipse confocal \(\Rightarrow\) semieje \(<C^3\Rightarrow
\rho<e^{\varphi_*}\). En \(\Sigma\), \(f=\pm C^3\). \(\square\)

(b) Simetrías exactas del símbolo [V] (identidades de Laurent, válidas
para \(p\) complejo): \(W(p+\pi e_1)=-W\), \(W(p+\pi e_3)=-\sigma_3W\sigma_3\),
\(W(p+\pi e_2)=-\sigma_3W^T\sigma_3\), \(W(p+\pi(e_2+e_3))=W^T\),
\(W(p+\pi(1,1,1))=-W^T\). Por tanto \(S(\eta_0+p)=\epsilon_{\eta_0}\mathcal T_{\eta_0}(S(p))\)
con \(\epsilon=\pm1\) y \(\mathcal T\in\{\mathrm{id},\ \sigma_3\cdot\sigma_3,\ \sigma_3(\cdot)^T\sigma_3,\ (\cdot)^T\}\).
Todos comparten \(\lambda\), \(Q\) y gap.

(c) **Qué puntos contribuyen.** El carácter \((-1)^{\eta_0\cdot x/\pi}\)
restringido a \(\Lambda_0\) es trivial **sólo** para
\(\eta_0\in\{0,\pi(1,1,1)\}\) [V]. Para los otros seis, las sumas en
plano no tienen término de momento cero (Lema 2(d)), y su contribución es
\(O(N^{-3/2})\) relativa. \(\eta_0=\pi(1,1,1)\) contribuye al mismo orden
que \(\eta_0=0\), con \(S^N\to(-1)^N(S^N)^T\) y signo \((-1)^{j+j'}\).

(d) Existe \(r_0>0\) tal que en \(|\eta|\le r_0\)
\(S(\eta-i\xi_*)=\lambda(\eta)P(\eta)+\lambda(\eta)^{-1}(I-P(\eta))\) con
\(\lambda,P\) analíticas,
\(\lambda(\eta)=\exp\bigl(\varphi_*+iv_*\cdot\eta-\tfrac12\eta^TQ\eta+\rho_3(\eta)\bigr)\),
\(|\rho_3|\le c_3|\eta|^3\le\tfrac14\eta^TQ\eta\), \(\|P(\eta)-P\|\le c_P|\eta|\)
(holomorfía: \(\partial_\eta\omega=iv_*\), \(\partial^2_\eta\omega=-\operatorname{Hess}\varphi\) [V]).
Fuera de \(\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)\), por (a), continuidad y
Schur (P) con \(\|S(\eta-i\xi_*)\|\le4e^{3t_*}\):
\(\|\widetilde S_N\|\le CNe^{-cN}\). Constantes \(r_0,c,c_3,c_P,C\) finitas
y **no explícitas**.

## 4. Hessiano completo

### 4.1 Hessiano en momento [A]/[V]

\(\operatorname{Hess}\varphi=\frac{\Pi}{D}\operatorname{sech}^2\xi_i\,\delta_{ij}-\frac{\Pi}{D^3}\tanh\xi_i\tanh\xi_j\),
\(\Pi=\prod\cosh\xi_j\), \(D=\sqrt{\Pi^2-1}\) [V]. En \(\xi_*\), con
\(D_*=\sqrt{C_*^6-1}\):

\[
Q=q_t\,(I-\hat u\hat u^T)+q_n\,\hat u\hat u^T,\quad
q_t=\frac{C_*}{D_*}=0.689567486595,\quad
q_n=\frac{C_*}{D_*}\,\frac{(C_*^2-1)(C_*^2+2)}{C_*^4+C_*^2+1}=0.303383821276.
\]

\(\det Q=q_nq_t^2>0\): **no degenerado** [V]. Lo comparten los ocho puntos
de \(\Sigma\).

### 4.2 Estructura en posición: las seis variables [A]

Exponente del integrando en las coordenadas exactas de §3.2 (kernel local,
perfiles y pesos):

\[
-t_*(2\theta_N+j+j')-\frac{(\delta+\delta')^2}{2Nq_n}-\frac{\lvert u'-u\rvert^2}{2Nq_t}
+2\log\varepsilon_\perp+2\log\varepsilon'_\perp+\text{const},
\]
\(\varepsilon_\perp=\delta-\delta^2/2R-|u|^2/2R\) (§7).

| Variable | Tipo | Escala | Tratamiento |
| --- | --- | --- | --- |
| \(j\) (profundidad Alice) | normal **discreta**, borde/Laplace | \(O(1)\) planos | suma de semiespacio exacta (§6.2) |
| \(j'\) (profundidad Bob) | normal **discreta**, borde/Laplace | \(O(1)\) planos | idem |
| \(u'-u\) (2 comps.) | **gaussiana** | \(\sqrt{Nq_t}\) | Hessiano \(1/(Nq_t)\) |
| \((u+u')/2\) (2 comps.) | **modo cero** del exponente | \(\sqrt N\) | confinada por el soporte del perfil (discos de radio \(\sqrt{2R\delta}\)), no por un Hessiano |
| \(\delta+\delta'\) en el kernel | gaussiana normal | \(\sqrt{Nq_n}\gg O(1)\) | sólo normaliza: \((2\pi Nq_n)^{-1/2}\); su curvatura es \(O(1/N)\) |

El bloque tangencial \((u,u')\) del Hessiano es
\(\frac1{Nq_t}\begin{psmallmatrix}I&-I\\-I&I\end{psmallmatrix}\): rango 2,
con modo cero en \(u+u'\). **No es una degeneración inesperada**: es
estructural, porque \(\xi_*\perp\) planos y el peso exponencial es
constante en cada plano. En coordenadas de profundidad euclídea ese modo
reaparece como gaussiana de curvatura \(\kappa/R\); ambas descripciones
dan la misma integral. Se usa la de planos porque es la exacta en red.

No hay variables eliminadas por constraints salvo la cuantización de la
profundidad (\(\delta\in(\theta_N+\mathbb Z_{\ge0})/\sqrt3\)) y las paridades
de sub-red, codificadas por los ocho puntos de \(\Sigma\).

## 5. Derivación de \(\beta\) [A]/[V]

Recuento sobre la representación de §3.1 (Lemas 2–4):

| Factor | Orden |
| --- | --- |
| \(b_N\) en la capa | \(N^{-3/2}\) |
| \(r\) en la capa de Bob | \(N^{-3/2}\) |
| \(s_N\) (lineal en \(F\)) | \(N^{-2}\) |
| \(h_B\) | \(N^{-2}\) |
| áreas en plano de Alice y de Bob | \(N\cdot N\) |
| \(\int d\eta_n\) gaussiana | \(N^{-1/2}\) |
| \(d^2\eta_t=(2/N)\,d^2\tau\), \(\tau=\sqrt{N/2}\,\eta_t\) | \(N^{-1}\) |

\[
\boxed{\beta=\tfrac32+\tfrac32+2+2-2+\tfrac12+1=\tfrac{13}{2}}\quad[V]
\]

Las dos normales no aportan \(N^{-1/2}\) (son sumas discretas \(O(1)\));
las dos direcciones tangenciales comunes aportan área, no gaussiana. Un
recuento de "seis direcciones gaussianas" sería erróneo. La pieza
\(\langle r,Ea\rangle\) (con \(c_N=O(F^2)\)) tiene potencia
\(N^{-17/2}\): mismo sector exponencial, dos órdenes algebraicos más
abajo.

## 6. Capa \(O(1)\): tratamiento discreto/continuo

### 6.1 Dirección tangencial [A]

En el plano \(k\), \(G_0(u)=b_N(x)s_N(x)\) (Alice) es radial alrededor del
pie \((k/3)(1,1,1)\), soportada en un disco de radio
\(\varrho=\sqrt{2R\delta-\delta^2}\sim\sqrt N\), \(C^1\) con
\(\partial^3G_0\) una medida finita. Poisson en \(\Lambda_k\):

\[
\sum_{u\in\Lambda_k}e^{i\eta_t\cdot u}G_0(u)=\frac1{\sqrt3}\sum_{m\in\Lambda_0^*}
\widehat G_0(2\pi m-\eta_t)\,e^{i\phi_{k,m}}.
\]

Para \(m\neq0\) y \(|\eta_t|\le r_0\): \(|\widehat G_0(k)|\le\|\partial^3G_0\|_{\mathcal M}/|k|^3\),
con \(\|\partial^3G_0\|_{\mathcal M}\lesssim N^{-3/2}\varrho^3/R^4\), y
\(\sum_{m\neq0}|m|^{-3}<\infty\) en 2D. Tras la suma ponderada en
profundidad, el error es \(O(N^{-4})\) frente a \(\mathfrak A=\Theta(N^{-5/2})\):
**relativo \(O(N^{-3/2})\)**. Aquí sustituir la suma por la integral **sí**
está controlado.

### 6.2 Dirección normal: suma de semiespacio exacta [A]/[V]

No se sustituye por una integral. Con \(\Psi_\delta(\tau)=\int_{\mathbb R^2}(\delta-|\sigma|^2)^2_+e^{i\tau\cdot\sigma}d^2\sigma\),
el factor de capa líder es

\[
\mathcal S_\pm(\tau;\theta)=\sum_{j\ge0}(\pm1)^j\,e^{-t_*(\theta+j)}\,\Psi_{(\theta+j)/\sqrt3}(\tau).
\]

\(\Psi_\delta=\pi H(\delta)\) con \(H'''=2J_0(\tau\sqrt\delta)\),
\(H(0)=H'(0)=H''(0)=0\) [V], y
\(\mathcal L[J_0(\tau\sqrt s)](p)=e^{-\tau^2/4p}/p\) [V]. Por tanto
\(g_\tau(x)=e^{-t_*x}\Psi_{x/\sqrt3}(\tau)\mathbf 1_{x\ge0}\) es continua,
\(\hat g_\tau\in\ell^1\), y **Poisson en la profundidad** es exacto:

\[
\mathcal S_+=\sum_{n\in\mathbb Z}\hat g_\tau(2\pi n)e^{2\pi in\theta},\quad
\mathcal S_-=\sum_{n\in\mathbb Z}\hat g_\tau(\pi(2n+1))e^{i\pi(2n+1)\theta},\quad
\hat g_\tau(\omega)=c_g\,\frac{e^{-\tau^2/(4\sqrt3\,s)}}{s^4},
\]
\(s=t_*+i\omega\), \(c_g=2\pi/(3\sqrt3)\) [V].

- El término \(n=0\) es exactamente la integral continua de Laplace en la
  profundidad.
- Los \(n\neq0\) dan la dependencia en \(\theta_N\). Como
  \(|e^{-\tau^2/(4\sqrt3s)}|\le1\) y \(|s_n|\ge2\pi|n|\):
  \(|\mathcal S_+-\hat g_\tau(0)|\le c_g/720\) y \(|\mathcal S_-|\le c_g/48\) [V].
- Euler–Maclaurin no se invoca: el decaimiento por plano \(e^{-t_*}=0.48\)
  no es lento. La precisión del término continuo (\(\sim10^{-3}\)) se debe a
  que \(g\) se anula a orden 3 en la superficie (\(\hat g\sim s^{-4}\)).

Con \(w(\tau)=e^{-q_t|\tau|^2}\), \(\Gamma_\pm(\theta)=\int_{\mathbb R^2}w\,\mathcal S_\pm^2\,d^2\tau\):

\[
\overline\Gamma=\frac{c_g^2}{t_*^8}\,\frac{\pi}{q_t+\frac1{2\sqrt3t_*}}=49.4418684782,
\quad |\Gamma_+(\theta)-\overline\Gamma|\le\varepsilon_+=0.0491723,
\quad 0\le\Gamma_-(\theta)\le\varepsilon_-=0.00289126,
\]

\(\varepsilon_+=2\frac{c_g}{720}\,\frac{c_g}{t_*^4}\frac{\pi}{q_t+1/(4\sqrt3t_*)}+\bigl(\frac{c_g}{720}\bigr)^2\frac\pi{q_t}\),
\(\varepsilon_-=\bigl(\frac{c_g}{48}\bigr)^2\frac\pi{q_t}\):
\(\varepsilon_+/\overline\Gamma<1.1\times10^{-3}\),
\(\varepsilon_-/\overline\Gamma<6\times10^{-5}\) [V].

## 7. Expansiones de perfiles [A]/[V]

Exactas en el plano \(k\) (Alice; Bob igual con \(\delta'\), \(u'\)):

\[
F_N=\frac{64}{N^2}\,\varepsilon_\perp^2,\qquad
\varepsilon_\perp=\delta-\frac{\delta^2}{2R}-\frac{|u|^2}{2R}\ \ (\ge0),
\]
\[
s_N=\sin\tfrac{\pi F_N}2=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),\qquad
c_N=\cos\tfrac{\pi F_N}2-1=-\frac{512\pi^2}{N^4}\varepsilon_\perp^4+O(N^{-8}),\qquad
h_B=\frac{64}{N^2}\varepsilon_\perp'^2.
\]

Órdenes reales en la capa: \(F_N,h_B,s_N=\Theta(N^{-2})\);
\(c_N=\Theta(N^{-4})\). Se mantienen separados: \(s_N\) produce el líder
\(N^{-13/2}\), \(c_N\) la corrección \(N^{-17/2}\). La sustitución de
\(\varepsilon_\perp\) por \(\delta-|u|^2/2R\) y del disco exacto por el de
radio \(\sqrt{2R\delta}\) cuesta \(O(\delta/R)=O(N^{-1})\) relativo. El
perfil entra **dentro** de \(\Psi_\delta\) y de \(\Gamma_\pm\), no como
factor aparte.

## 8. Amplitud spinorial inclinada [A]/[V]

- \(S(-i\xi)\) es **hermítica** para todo \(\xi\) real [V], con
  \(\det=1\). En \(\xi_*\):
  \(S_*=\begin{psmallmatrix}C_*^2e^{-t_*}&-(1+iC_*)S_*\\-(1-iC_*)S_*&C_*^2e^{t_*}\end{psmallmatrix}\),
  \(S_*=\sinh t_*\) [V].
- Autovalores \(e^{\pm\varphi_*}\), \(e^{\varphi_*}=C_*^3+S_*\sqrt{C_*^4+C_*^2+1}\) [V].
  Gap \(e^{2\varphi_*}\approx15.8\).
- Hermítica \(\Rightarrow\) autovectores izquierdo y derecho coinciden;
  proyector de Perron ortogonal [V]:
  \[
  P=\frac12\begin{pmatrix}1-\alpha&-(1+iC_*)\alpha/C_*^2\\-(1-iC_*)\alpha/C_*^2&1+\alpha\end{pmatrix},
  \qquad P_{12}=-0.216031927-0.277190261\,i,\ \ \arg P_{12}=-0.7107\pi.
  \]
  (La normalización \(P_{11}=(1-\alpha)/2\) es exacta.)
- Saddle \(\pi(1,1,1)\): \(S^N\to(-1)^N(S^N)^T\), proyector \(P^T=\overline P\).
- Dependencia en \(\uparrow,\downarrow\): \(P\downarrow=(P_{12},\tfrac{1+\alpha}2)\),
  \(P\uparrow=(\tfrac{1-\alpha}2,\overline{P_{12}})\). Las fases se
  conservan hasta la suma final (§11).
- \(\sinh t_*\neq0\) **no se usa** como argumento de no nulidad; el
  argumento es el signo del funcional completo \(\ell\) de §11.

## 9. Asintótica completa de \(r\) [A]/[V]

**Lema 3.** Uniformemente en \(y\in\mathbb Z^3\),
\[
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),\qquad
R_0(w)=c_r\bigl[A(|w|)\,I-B(|w|)\,H_W(\hat w)\bigr]\!\downarrow,\qquad c_r=\frac{\sqrt{3465}}{64\pi^2},
\]
\(A(\rho)=4\pi\int_0^1k^2(1-k^2)^2\cos k\,j_0(k\rho)dk\),
\(B(\rho)=4\pi\int_0^1k^2(1-k^2)^2\sin k\,j_1(k\rho)dk\).

*Prueba.* \(S(p)=I-iH_W(p)+O(p^2)\) [V]; para \(|p|\le1/N\),
\(S=e^{-iH(p)}\) con \(H\) hermítica analítica y \(H-H_W=O(|p|^2)\);
Duhamel da \(\|S^N-e^{-iNH_W}\|\le CN|p|^2=C|q|^2/N\) (\(q=Np\)).
\(e^{-iH_W(q)}=\cos|q|-i\sin|q|H_W(q)/|q|\) porque \(H_W^2=|q|^2\) [V]; las
integrales angulares dan \(4\pi j_0\) y \(-4\pi ij_1\hat w\) [V]. El
recurso completo entra por su transformada \(g(Np)\) de soporte
\(|p|\le1/N\): **no se trunca**. \(\square\)

En el punto enfrentado \(w_*=(1,1,1)-\hat u/4\), \(|w_*|=\rho_*=\sqrt3-\tfrac14<\pi\),
\(\hat w_*=\hat u\), \(H_W(\hat u)\downarrow=(1+i,-1)/\sqrt3\) [V]:

\[
R_0(w_*)=c_r\Bigl(-\tfrac{B}{\sqrt3}(1+i),\ A+\tfrac{B}{\sqrt3}\Bigr),\quad
A=0.716577583139,\ B=0.132252374571\ \ [V].
\]

\(A,B>0\): integrandos positivos porque \(k\rho_*<\pi\) y
\(x\mapsto\sin x-x\cos x\) crece en \((0,\pi)\) [V]; confirmado por
enclosure. Variación en la capa: \(|y-y_*|/N=O(N^{-1/2})\), relativa
\(O(N^{-1/2})\). [D]: la cuadratura de \(r(y_*)\) coincide con
\(N^{-3/2}R_0\) con error relativo \(2\cdot10^{-6}\) (\(N=40\)) y
\(8\cdot10^{-9}\) (\(N=640\)).

## 10. Sectores exponenciales [A]

Con \(v=r+a\), (L) da, **exhaustivamente**, términos lineales o
cuadráticos en \((a,b,d)\):

| Sector | \(M=I\) | \(\sigma_3\) | \(\sigma_1\) | \(\sigma_2\) |
| --- | --- | --- | --- | --- |
| \(e^{-K_*N}N^{-13/2}\) | \(-2\operatorname{Im}\langle r,Ed\rangle\) | \(+2\operatorname{Im}\langle r,Ed\rangle\) | \(-2\operatorname{Im}\langle r,Eb\rangle\) | \(+2\operatorname{Re}\langle r,Eb\rangle\) |
| \(e^{-K_*N}N^{-17/2}\) | \(2\operatorname{Re}\langle r,Ea\rangle\) | idem | idem | idem |
| \(e^{-2K_*N}N^{O(1)}\) | \(\langle a,Ea\rangle,\langle d,Ed\rangle,\operatorname{Im}\langle a,Ed\rangle\) | idem | \(\langle a,Ea\rangle,\langle b,Eb\rangle,\operatorname{Im}\langle a,Eb\rangle\) | \(\langle a,Ea\rangle,\langle b,Eb\rangle,\operatorname{Re}\langle a,Eb\rangle\) |

**Lema 4.** \(|G_N(d)|\le(1+4e^{3t_*}Ne^{-\varphi_*})e^{N\varphi_*-\xi_*\cdot d}\)
(Schur (P) con tilt \(t_*\)). Con \(\xi_*\cdot(y-x)\ge N\xi_*\cdot v_*\):
\(|a(y)|,|b(y)|,|d(y)|\le CN^qe^{-K_*N}\) en \(B_N\), luego los términos
cuadráticos son \(O(N^{q'}e^{-2K_*N})\). \(|\langle r,Ea\rangle|=O(N^{-17/2}e^{-K_*N})\)
por la maquinaria de §11 con \(c_N=\Theta(N^{-4})\).

Candado respetado: \(e^{-2K_*N}\) sólo se acota; no se calcula ni se
introduce como \(C^{(j)}\). No hace falta: el sector \(e^{-K_*N}\) **no**
cancela. Ningún otro sector aparece. \(K_*\) no se reoptimiza.

## 11. Construcción del coeficiente completo [A]/[V]

**Lema 2 (capas).** Sea \(\chi\in\{\uparrow,\downarrow\}\),
\(f=s_Nb_N\chi\), \(w=h_BM_Br\), \(\tau=\sqrt{N/2}\,\eta_t\),
\(\widehat B=c_rI_b\), \(I_b=16\pi\int_0^1k(1-k^2)^2\sin(k/4)dk\).

(a) \(|\mathfrak A_f(\eta)|,|\mathfrak B_w(\eta)|\le CN^{-5/2}\) para todo \(\eta\).

(b) Para \(|\eta|\le r_0\):
\(\mathfrak A_f(\eta)=N^{-5/2}\frac{16\pi}{\sqrt3}\widehat B\,[\mathcal S_+(\tau)+\mathcal E_A]\chi\),
\(\mathfrak B_w(\eta)=N^{-5/2}\frac{32}{\sqrt3}R_0(w_*)^\dagger M_B\,[\mathcal S_+(\tau)+\mathcal E_B]\),
con \(|\mathcal E|\le C(N^{-1/2}+|\eta_n|)\).

(c) En \(\eta_0=\pi(1,1,1)\) lo mismo con \(\mathcal S_-\), incluida la
fase \((-1)^{j+j'}\) de §3.2.

(d) Para \(\eta_0\in\Sigma\setminus\{0,\pi(1,1,1)\}\):
\(|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}\).

*Prueba.* Descomposición exacta en planos; Poisson en plano (§6.1): el
término \(m=0\) da la integral del disco; en (d) no existe término
\(m=0\), porque el carácter es no trivial. Perfiles (§7): \(O(N^{-1})\).
\(b_N(x)=N^{-3/2}B_\phi(|x|/N)\) y \(R_0\) suaves: \(O(|u|/N)=O(N^{-1/2})\).
\(|e^{-i\eta_n\delta}-1|\le|\eta_n|\delta\). Planos con \(\delta>R/2\):
\(O(e^{-\kappa R/2})\). Integral en plano:
\(\int e^{i\eta_t\cdot u}(\delta-|u|^2/2R)^2_+d^2u=2R\,\Psi_\delta(\tau)\). \(\square\)

**Teorema.** Para cada par, con \(\mathcal T_\chi:=e^{K_*N}\langle r,E\,S^N(s_Nb_N\chi)\rangle\),

\[
\mathcal T_\chi=N^{-13/2}\,\mathcal K\,c_r\Bigl[\Gamma_+(\theta_N)\,x_0+\Gamma_-(\theta_N)\,x_\pi\Bigr]+O(N^{-7}),
\]
\[
x_0=\tilde R_0^\dagger M_BP\chi,\quad x_\pi=\tilde R_0^\dagger M_B\overline P\chi,\quad
\tilde R_0=R_0(w_*)/c_r,\quad
\mathcal K=\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}\,\widehat B=1.74926941930.
\]

*Prueba.* §3.1. Fuera de las bolas \(B(\eta_0,r_0)\): \(O(Ne^{-cN}N^{-5})\)
(Lema 1(d), Lema 2(a)). Seis puntos con carácter no trivial:
\(O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})=O(N^{-8})\) (Lema 2(d), gaussiana).
En \(\eta_0\in\{0,\pi(1,1,1)\}\): sustituir \(\widetilde S_Ne^{-i\eta\cdot Nv_*}\)
por \(e^{-N\eta^TQ\eta/2}P\) (resp. \(\overline P\)) cuesta
\(N^{-5}\int(c_P|\eta|+Nc_3|\eta|^3)e^{-N\eta^TQ\eta/4}=O(N^{-7})\)
(con \(|e^{N\rho_3}-1|\le N|\rho_3|e^{N|\rho_3|}\)); sustituir las capas
por su forma líder cuesta \(N^{-5}\int e^{-N\eta^TQ\eta/4}(N^{-1/2}+|\eta_n|)=O(N^{-7})\);
extender a \(\mathbb R^3\): \(O(e^{-cNr_0^2})\). Queda
\(N^{-5}\frac{512\pi}{3}\widehat B\,\sqrt{\frac{2\pi}{Nq_n}}\,\frac2N\,(2\pi)^{-3}\int w\,\mathcal S_\pm^2\), es decir
\(\mathcal K\) [V]. \(\square\)

**Coeficiente completo.** Con \(\ell\) el funcional real que (L) impone al
par (\(-2\operatorname{Im}\) para \(I\) y \(\sigma_1\), \(+2\operatorname{Im}\)
para \(\sigma_3\), \(+2\operatorname{Re}\) para \(\sigma_2\); \(\chi=\downarrow\)
para \(I,\sigma_3\), \(\chi=\uparrow\) para \(\sigma_1,\sigma_2\)):

\[
\boxed{C_{M,M_B}(\theta)=\mathcal K\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\qquad \ell_0=\ell(x_0),\ \ell_\pi=\ell(x_\pi).}
\]

Suma **todo** el sector \(e^{-K_*N}N^{-13/2}\): los dos puntos de toro que
contribuyen, ambas capas discretas con sus fases de paridad, perfiles,
Hessiano, Jacobianos (\(1/\sqrt3\) por plano, \(2/N\), \((2\pi)^{-3}\)),
spin, detector, encoder y la interferencia con \(r\). **No es un producto
de factores locales.** Los puntos \(0\) y \(\pi(1,1,1)\) entran con
proyectores distintos (\(P\), \(\overline P\)) y pesos distintos
(\(\Gamma_+\), \(\Gamma_-\)).

Formas exactas [V], con \(C=C_*\) y \(A,B\) de §9. Para cada \(M_B\),
\(\ell(\sigma_3,M_B)=-\ell(I,M_B)\) exactamente.

| Par | \(\ell_0\) | \(\ell_\pi\) |
| --- | --- | --- |
| \((I,I)\), \((I,P_3)\) | \(-\frac{\sqrt3}{3}\frac{B\alpha(C-1)}{C^2}\) | \(+\frac{\sqrt3}{3}\frac{B\alpha(C+1)}{C^2}\) |
| \((I,P_1)\) | \(\frac{3AC\alpha-\sqrt3B(C^2\alpha+C^2-\alpha)}{6C^2}\) | \(-\frac{3AC\alpha+\sqrt3B(C^2\alpha+C^2-\alpha)}{6C^2}\) |
| \((I,P_2)\) | \(\frac{3A\alpha-\sqrt3B(C^2\alpha+C^2+C\alpha-2\alpha)}{6C^2}\) | \(\frac{3A\alpha-\sqrt3B(C^2\alpha+C^2-C\alpha-2\alpha)}{6C^2}\) |
| \((\sigma_1,I)\) | \(-\frac{3A\alpha+\sqrt3B(C-C\alpha+\alpha)}{3C}\) | \(\frac{3A\alpha-\sqrt3B(C-C\alpha-\alpha)}{3C}\) |
| \((\sigma_1,P_1)\) | \(-\frac{3AC\alpha+\sqrt3B(C^2-C^2\alpha-\alpha)}{6C^2}\) | \(\frac{3AC\alpha-\sqrt3B(C^2-C^2\alpha-\alpha)}{6C^2}\) |
| \((\sigma_1,P_2)\) | \(-\frac{3A(C^2(1-\alpha)+C\alpha)+\sqrt3B(2C^2(1-\alpha)+2C\alpha-\alpha)}{6C^2}\) | \(-\frac{3A(C^2(1-\alpha)-C\alpha)+\sqrt3B(2C^2(1-\alpha)-2C\alpha-\alpha)}{6C^2}\) |
| \((\sigma_1,P_3)\), \((\sigma_2,P_3)\) | \(-\frac{\sqrt3}{3}B(1-\alpha)\) | igual |
| \((\sigma_2,I)\) | \(-\frac{3A\alpha+\sqrt3B(C^2(1-\alpha)+\alpha)}{3C^2}\) | igual |
| \((\sigma_2,P_1)\) | \(-\frac{3A(\alpha-C^2(1-\alpha))+\sqrt3BC\alpha}{6C^2}\) | \(-\frac{3A(\alpha-C^2(1-\alpha))-\sqrt3BC\alpha}{6C^2}\) |
| \((\sigma_2,P_2)\) | \(-\frac{3A\alpha+\sqrt3B(C^2(1-\alpha)+C\alpha+2\alpha)}{6C^2}\) | \(-\frac{3A\alpha+\sqrt3B(C^2(1-\alpha)-C\alpha+2\alpha)}{6C^2}\) |

**No nulidad uniforme en \(\theta\)** [V]. Para cada par,
\(|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|\) en
aritmética de intervalos. Entonces \(C(\theta)\) tiene signo fijo y
\(|C(\theta)/\overline C-1|\le(\varepsilon_+|\ell_0|+\varepsilon_-|\ell_\pi|)/(\overline\Gamma|\ell_0|)\),
con \(\overline C=\mathcal Kc_r\overline\Gamma\ell_0\) y
\(\mathcal Kc_r\overline\Gamma=8.05978541\).

Casos estructurales:

- \(\sigma_2\): \(\ell_0,\ell_\pi\) del mismo signo en los cuatro
  detectores (en \(I,P_3\) son iguales), por positividad de
  \(A,B,\alpha,1-\alpha\) y \(\alpha-C^2(1-\alpha)=0.2361>0\).
- \((I,I)\): \(\ell_0\propto-B\alpha(C-1)\), nulo sólo si \(B=0\) o
  \(C=1\) [V]. Es el coeficiente más pequeño, \(|\overline C|=0.0753\).

## 12. Tabla de los dieciséis pares

\(P_j=(I+\sigma_j)/2\). En todas las filas: \(K_*=I(v_*)\), \(\beta=13/2\);
contribuciones de tasa \(K_*\) = interferencia \(r\times\)capa (\(N^{-13/2}\))
más \(2\operatorname{Re}\langle r,Ea\rangle\) (\(N^{-17/2}\), en el resto);
saddles \(\eta_0\in\{0,\pi(1,1,1)\}\) (los otros seis en el resto,
\(O(N^{-3/2})\)); resto \(O(N^{-1/2})\) [A]; \(C\) real (\(L\) es real) y
de signo fijo en \(\theta\); mecanismo de cancelación: ninguno;
\(C^{(j)}\): no procede.

| Encoder | Detector | Funcional | \(\overline C\) [V] | \(\lvert C(\theta)/\overline C-1\rvert\le\) | Estado individual |
| --- | --- | --- | --- | --- | --- |
| \(I\) (REFERENCE_CONTROL) | \(I\) | \(-2\operatorname{Im}\mathcal T_\downarrow\) | \(-0.0752752093\) | \(1.47\cdot10^{-3}\) | `REFERENCE_NONVANISHING` |
| \(I\) (REFERENCE_CONTROL) | \(P_1\) | \(-2\operatorname{Im}\mathcal T_\downarrow\) | \(+1.2072650683\) | \(1.09\cdot10^{-3}\) | `REFERENCE_NONVANISHING` |
| \(I\) (REFERENCE_CONTROL) | \(P_2\) | \(-2\operatorname{Im}\mathcal T_\downarrow\) | \(+0.8164098576\) | \(1.08\cdot10^{-3}\) | `REFERENCE_NONVANISHING` |
| \(I\) (REFERENCE_CONTROL) | \(P_3\) | \(-2\operatorname{Im}\mathcal T_\downarrow\) | \(-0.0752752093\) | \(1.47\cdot10^{-3}\) | `REFERENCE_NONVANISHING` |
| \(\sigma_1\) | \(I\) | \(-2\operatorname{Im}\mathcal T_\uparrow\) | \(-3.7206303938\) | \(1.05\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_1\) | \(P_1\) | \(-2\operatorname{Im}\mathcal T_\uparrow\) | \(-1.5567800857\) | \(1.06\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_1\) | \(P_2\) | \(-2\operatorname{Im}\mathcal T_\uparrow\) | \(-2.8203960182\) | \(1.02\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_1\) | \(P_3\) | \(-2\operatorname{Im}\mathcal T_\uparrow\) | \(-0.1776542932\) | \(1.05\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_2\) | \(I\) | \(+2\operatorname{Re}\mathcal T_\uparrow\) | \(-2.9389199724\) | \(1.05\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_2\) | \(P_1\) | \(+2\operatorname{Re}\mathcal T_\uparrow\) | \(-0.5846543741\) | \(1.02\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_2\) | \(P_2\) | \(+2\operatorname{Re}\mathcal T_\uparrow\) | \(-1.7729950974\) | \(1.04\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_2\) | \(P_3\) | \(+2\operatorname{Re}\mathcal T_\uparrow\) | \(-0.1776542932\) | \(1.05\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_3\) | \(I\) | \(+2\operatorname{Im}\mathcal T_\downarrow\) | \(+0.0752752093\) | \(1.47\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_3\) | \(P_1\) | \(+2\operatorname{Im}\mathcal T_\downarrow\) | \(-1.2072650683\) | \(1.09\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_3\) | \(P_2\) | \(+2\operatorname{Im}\mathcal T_\downarrow\) | \(-0.8164098576\) | \(1.08\cdot10^{-3}\) | `NONVANISHING_PAIR` |
| \(\sigma_3\) | \(P_3\) | \(+2\operatorname{Im}\mathcal T_\downarrow\) | \(+0.0752752093\) | \(1.47\cdot10^{-3}\) | `NONVANISHING_PAIR` |

Observaciones que **no** se presuponían y salen del cálculo:

- \(C(\sigma_3,M_B)=-C(I,M_B)\) en el líder, así que
  \(\delta_{\sigma_3}\sim\delta_I\) asintóticamente. Difieren en órdenes
  inferiores.
- \(C(I,I)=C(I,P_3)\) y \(C(\sigma_1,P_3)=C(\sigma_2,P_3)\).
- No hay equivalencia entre direcciones Pauli: \(\sigma_1\), \(\sigma_2\),
  \(\sigma_3\) dan coeficientes distintos para \(M_B=I\).

## 13. Control del resto

Presupuesto de error relativo al líder \(N^{-13/2}\) [A]:

| Fuente | Orden relativo | Dónde |
| --- | --- | --- |
| término cúbico del exponente y \(P(\eta)-P\) | \(N^{-1/2}\) (cota bruta; \(N^{-1}\) por paridad) | Lema 1(d), Teorema |
| fase normal \(e^{-i\eta_n\delta}\) | \(N^{-1/2}\) | Lema 2(b) |
| variación de \(b_N\) y de \(R_0\) en la capa | \(N^{-1/2}\) | Lemas 2, 3 |
| \(r\) frente a \(N^{-3/2}R_0\) | \(N^{-1}\) | Lema 3 |
| geometría exacta de perfiles y discos | \(N^{-1}\) | §7 |
| Poisson en plano | \(N^{-3/2}\) | §6.1 |
| seis puntos de toro con carácter no trivial | \(N^{-3/2}\) | Lema 2(d) |
| \(2\operatorname{Re}\langle r,Ea\rangle\) | \(N^{-2}\) | Lema 4 |
| fuera de \(\bigcup B(\eta_0,r_0)\); planos \(\delta>R/2\) | \(e^{-cN}\) | Lema 1(d) |
| sector \(e^{-2K_*N}\) | \(e^{-K_*N}N^{O(1)}\) | Lema 4 |

Por tanto
\(L_{M,M_B}(N)=e^{-K_*N}N^{-13/2}\bigl(C_{M,M_B}(\theta_N)+R_N\bigr)\) con
\(|R_N|\le C'N^{-1/2}\), \(C'<\infty\) **no explícita**. Como
\(\inf_\theta|C_{M,M_B}(\theta)|\ge(1-1.5\cdot10^{-3})|\overline C_{M,M_B}|>0\),
existe \(N_*\) (no explícito) a partir del cual \(L\neq0\) y el resto no
puede cancelar el líder. No se da una cota \(\varepsilon_N\) con
constantes numéricas: es deuda de certificación declarada.

**Diagnósticos [D]** (`--diagnostics`, float64; no deciden nada):

| \(N\) | brute/ref \((d,I)\) | ref/lead \((d,I)\) | \(\lvert2\operatorname{Re}\langle r,Ea\rangle\rvert/\lvert2\operatorname{Im}\langle r,Ed\rangle\rvert\) (\(M_B=I\)) | idem \(/\lvert2\operatorname{Re}\langle r,Eb\rangle\rvert\) |
| --- | --- | --- | --- | --- |
| 24 | \(1.479+0.005i\) | \(0.0583\) | 15.2 | 0.77 |
| 40 | \(1.296+0.003i\) | \(0.1488\) | 9.4 | 0.40 |
| 56 | \(1.214+0.002i\) | \(0.2359\) | 6.4 | 0.24 |

- *brute*: convolución FFT exacta en variables inclinadas (sin
  cancelación catastrófica) con \(r\) por cuadratura del recurso completo.
- *ref*: geometría de red exacta, pero kernel sustituido por la forma
  gaussiana de los ocho puntos de \(\Sigma\) con \(P\), \(\sigma_3P\sigma_3\),
  \(\sigma_3P^T\sigma_3\), \(P^T\). brute/ref \(\to1\) con desviación
  \(\approx c/N\), \(c\in[-0.5,14]\) según la componente (en \(N=24,40,56\)):
  valida kernel, proyectores y fases.
- *semi*: planos discretos y perfiles exactos a \(R\) finito, integrales en
  plano. semi/lead \(=0.9064\ (N=10^3)\), \(0.9901\ (10^4)\),
  \(0.9967\ (3\cdot10^4)\), o sea \(\approx1-100/N\); semi coincide con ref
  en \(N=40,56\). Valida \(\mathcal K\overline\Gamma\). El \(-100/N\)
  procede sobre todo de la gaussiana normal
  \(e^{-(\delta+\delta')^2/2Nq_n}\) con \(q_n=0.30\) y
  \(\langle(\delta+\delta')^2\rangle\approx44\).
- Para \(M\in\{I,\sigma_3\}\), cuyo \(|\overline C|\) es pequeño, el término
  \(N^{-17/2}\) domina numéricamente en todo el rango diagnóstico. El
  líder \(N^{-13/2}\) sólo es la ley observable más allá.

## 14. Estado terminal

Asignación en el orden del charter:

1. **`PAULI_LEADING_COEFFICIENT_NONVANISHING` — se asigna.** Motivo:
   \(\beta=13/2\) identificado (§5); los doce pares con
   \(M\in\{\sigma_1,\sigma_2,\sigma_3\}\) tienen \(C_{M,M_B}(\theta)\neq0\)
   de signo fijo y uniforme en \(\theta\) (§§11–12 [V]); se han sumado
   todas las contribuciones de tasa \(K_*\) (§10); el resto es
   \(O(N^{-1/2})\) [A] (§13). Basta un par; se cumplen doce. El caso
   estructuralmente más robusto es \(\sigma_2\) (mismo signo en ambos
   saddles, sin comparar \(\Gamma_\pm\)).
2. `ALL_LEADING_COEFFICIENTS_VANISH`: no. Ningún \(C\) se anula.
3. `REFERENCE_CONTROL_ONLY_LEADING_NONVANISHING`: no. Los Pauli también
   sobreviven (el control \(I\) también es no nulo).
4. `OPEN_AFTER_LAPLACE_COEFFICIENT_ANALYSIS`: no se asigna. \(\beta\)
   identificado, coeficiente completo cerrado, cola \(r\) con coeficiente,
   fases controladas, resto acotado, ninguna factorización usada como
   prueba, ningún sector \(e^{-2K_*N}\) confundido con \(C^{(j)}\).

**Punto interpretativo para la revisión independiente.** El charter
escribe \(C_{M,M_B}\) como constante. El coeficiente completo es
\(C_{M,M_B}(\theta_N)\): continuo, 1-periódico, cuasi-periódico en \(N\)
(\(\sqrt3/4\notin\mathbb Q\)), y con
\(|C(\theta)/\overline C-1|\le1.5\cdot10^{-3}\). La pregunta
\(C\stackrel?=0\) queda respondida sin ambigüedad (no, uniformemente en
\(\theta\)). Pero una forma con \(C\) **constante** y \(o(1)\) sólo vale con
\(C\to C(\theta_N)\). Con la constante \(\overline C\), el error es
\(\le1.5\cdot10^{-3}|\overline C|+O(N^{-1/2})\), que no es \(o(1)\).
Diagnóstico: \(\Gamma_+\) varía \(\approx\pm0.09\%\) con \(\theta\); la no
constancia no se prueba formalmente y nada depende de ella. Si el
revisor exigiera la constancia literal, el estado correcto sería
`OPEN_AFTER_LAPLACE_COEFFICIENT_ANALYSIS` con esta misma tabla. El autor
considera que el estado asignado responde a la pregunta del charter.

**Consecuencia autorizada por el charter (§4), para los doce pares
Pauli, pendiente de revisión:**

\[
\delta_{M,M_B}(N)=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\]

junto con §8.17 (\(\delta\le36N^4e^{-JN}\)):
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` para esos pares.

## 15. Techo exacto del claim

- Sólo la clase congelada de §2 del charter: CJWW (5.15), una partícula,
  bolas euclídeas, perfiles, \(\theta=\pi/2\), las cuatro \(M\) y las
  cuatro \(M_B\), recurso \(g(Np)\).
- Afirmación **asintótica**. \(N_*\) y \(C'\) no son explícitos. A
  \(N\lesssim10^3\) la fórmula líder sobreestima la interferencia
  (brute/lead \(=1.214\times0.236\approx0.29\) para
  \(\mathcal T_\downarrow\), \(M_B=I\), \(N=56\) [D]). Para
  \(M\in\{I,\sigma_3\}\), en el rango diagnóstico domina la pieza
  \(N^{-17/2}\).
- \(C\) depende de \(\theta_N\); no se afirma un \(C\) constante (§14).
- No se afirma \(\delta\equiv0\) ni \(D_B=0\) para ningún par. No se
  calcula el sector \(e^{-2K_*N}\) ni \(D_B\).
- No reabre \(K_*\), \(v_*\), la geometría, el encoder, el detector, los
  perfiles, el nodo ni el walk. La precisión sobre los ocho máximos de
  toro (§2) corrige una frase de §8.19 sin cambiar su tasa ni su estado.
- No reabre §§8.16–8.19, `3/128`, no-corner ni `Delta T=2`.
- \(N\to\infty\) no es \(a,\tau\to0\). Sin unidades físicas (§8.15). No se
  afirma violación de la microcausalidad del modelo.
- La familia \(M=aI+b\cdot\sigma\) general no queda cubierta.
- \(I\) sigue siendo `REFERENCE_CONTROL`: su no nulidad es un dato, no
  un control negativo fallido.

## 16. Implementación / certificado

Se crea `scripts/verify_regional_laplace_coefficient_gate.py`. No se
modifica ningún verificador revisado.

**Necesidad.** Ningún certificado existente contiene: la hermiticidad de
\(S(-i\xi)\); las cinco simetrías de medio periodo y la trivialidad de los
caracteres en planos; la forma cerrada de \(P\), \(C_*^2\), \(q_n\),
\(q_t\); el límite de Weyl de \(r\) y los signos de \(A,B\); la identidad
de Laplace de \(\Psi_\delta\), las cotas de Poisson \(1/720\), \(1/48\) y
\(\overline\Gamma,\varepsilon_\pm\); el prefactor \(\mathcal K\); los
funcionales \(\ell_0,\ell_\pi\) y el margen de signo de los dieciséis
pares. Los helpers congelados sólo aportan `walk2`, `PS`, `PAULI`,
`is_zero`; añadir lo anterior a un script revisado cambiaría sus bytes.

**Qué certifica: 58/58 checks exactos.** Identidades SymPy y enclosures de
intervalo mpmath (`iv`, 50 dígitos) de formas cerradas. Hash del charter
y de los artefactos de §8.19. Identidades y cotas de §§3–9 y 11. Signo y
margen uniforme en \(\theta\) de \(C_{M,M_B}(\theta)\) para los dieciséis
pares, y \(C(\sigma_3)=-C(I)\).

**Qué no certifica:** los Lemas 1(d), 2, 3, 4 y el Teorema como
enunciados asintóticos (constantes \(r_0,c,C'\)), ni \(N_*\). Son [A].

**Diagnósticos** (`--diagnostics`, numpy): SUPPORTED, fuera del contador,
no usados para \(\beta\), \(C\) ni el estado. La exploración previa se hizo
en scratch (no versionado); los números [D] de §§9 y 13 son los que
reproduce este modo.

Dependencias: Python 3.12.3, SymPy 1.14.0, mpmath 1.3.0 (ya requerido por
SymPy), NumPy 1.26.4 (transitivo por el helper y en diagnósticos). No se
instala nada. SciPy se usó sólo en scratch, no en el certificado. Sin
coma flotante en cantidades decisivas.

SHA256 del certificado:
`d008417debe149743396bfbeb7d55be11fe7aa00bce3b4aecebf6a50997884b2`.

## 17. Regresiones

Todos con código de salida `0`, desde la raíz, `python3 -B`:

| Comando | Resultado |
| --- | --- |
| `scripts/verify_regional_laplace_coefficient_gate.py` | 58/58 |
| `scripts/verify_regional_laplace_coefficient_gate.py --diagnostics` | 58/58 + diagnósticos §13 |
| `scripts/verify_regional_directional_asymptotics_gate.py` | 18/18 |
| `scripts/verify_lower_bound_no_cancellation_gate.py` | 24/24 |
| `scripts/verify_scaled_ir_gate.py` | 53/53 |
| `scripts/verify_narrow_band_gate.py` | 34/34 |
| `scripts/verify_signaling_witness.py` | 17/17 |
| `scripts/verify_directional_saturation.py` | 27/27 |
| `scripts/verify_weyl_dirac_gate.py` | PASS, 375 exactas |
| `scripts/cert_Aa_s4_counterexample.py` | PASS |
| `scripts/review_Aa_s4_exact.py` | PASS, 117 identidades |

Los verificadores revisados conservan sus SHA256 (§§8.17–8.19). Charter y
`CURRENT_STATE.md` conservan los hashes de §1.

## 18. `git diff --check`

`git diff --check`: sin salida (no hay cambios tracked). Para los dos
archivos nuevos, `git diff --no-index --check /dev/null <archivo>`: sin
incidencias de whitespace. Nada staged. **Sin commit ni push.**
```

### Contexto adjunto: reports/2026-09-17--scaled-ir-signaling-gate.md
```
# SCALED_IR_SIGNALING_GATE — ejecución del contrato publicado

Registro de ejecución, 2026-09-17. Evaluación del autor; sin revisión
independiente ni promoción canónica. [A] identifica pruebas analíticas;
[V] identifica exclusivamente identidades comprobadas por el certificado.
El orden de ejecución es geometría/carta, admisibilidad, upper bound,
análisis de los dieciséis pares, clasificación.

**Resultado: `OPEN_AFTER_SCALED_IR_ANALYSIS`.** Admisibilidad IR demostrada
para las ocho operaciones; upper bound direccional exponencial demostrada;
positividad o nulidad de las dieciséis señales no resuelta. Certificado
auxiliar: **53/53 identidades**, sin cobertura software de la prueba completa.

## 1. Preflight

- Repositorio: `nacho09021973/qca-causal-cones`.
- Rama: `research/b-infinity-post-s4-gate`.
- `HEAD`, `refs/remotes/origin/research/b-infinity-post-s4-gate` y consulta
  efectiva `git ls-remote origin refs/heads/research/b-infinity-post-s4-gate`:
  `31b5797119a9aad03b11c5ee00db99e0d96ed9e4`, idénticos al baseline exigido.
  La consulta remota se repitió fuera del sandbox tras un fallo DNS.
- SHA256 de `theory/SCALED_IR_SIGNALING_GATE.md`:
  `325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c`.
- Ningún cambio tracked inicial, ni staged ni unstaged.
- Cuatro entradas untracked preexistentes, preservadas:
  `Auditoría De Novedad Matemática.md`,
  `debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.log`,
  `debates/2026-09-16--ratificacion-gate-completitud-axial-n3.log`,
  `scripts/__pycache__/` (dos `.pyc`). Todo Python se ejecuta con `-B`.
- SHA256 inicial de `state/CURRENT_STATE.md`:
  `7cb84de881b4a03b751842ef4f46a1bf10f54a1c6fd468c6029cfa5acf791098`.

Leídos íntegramente antes del cálculo: el charter escalado, el charter
narrow-band, `CURRENT_STATE`, `OPERATIONAL_INVISIBILITY_GATE`,
`COUPLING_MAP_SIGNALING_WITNESS`, `ALICE_LOCAL_PREPARATION_WITNESS`,
`NONCORNER_SIGNALING_GATE`, el informe de ejecución narrow-band y los scripts
`verify_directional_saturation.py`, `verify_signaling_witness.py`,
`verify_narrow_band_gate.py`, `verify_weyl_dirac_gate.py`; además las reglas
del proyecto y `scripts/README.md`. Las referencias bibliográficas a otros
walks son motivación solamente; no se transfieren sus propiedades.

La lógica terminal se reconstruyó antes de calcular, en el orden de §7:
ninguna Pauli admisible; obstrucción exacta de toda la familia incluido `I`;
lower bound polinómica de una Pauli; lower bound exponencial/asintótica no
nula y upper exponencial de una Pauli; en cualquier otro caso `OPEN`.
Una cota débil de admisibilidad no activa el primer estado. El control `I`
nunca establece por sí solo un estado positivo.

## 2. Geometría [A]

Se conservan exactamente `N` entero, `N>=2`, `Lambda=1/N`,
`Lambda'=1/sqrt(N)`, `Delta T=N`, y las bolas **euclídeas**

\[
A_N=\mathbb Z^3\cap\overline B_2(0,N/4),\qquad
B_N=\mathbb Z^3\cap\overline B_2(N(1,1,1),N/4).
\]

Para **cada** par `x` en Alice, `y` en Bob, la desigualdad triangular da

\[
|y-x|_2-N\ge(\sqrt3-3/2)N>N/5.
\]

La última desigualdad es exacta: `3>(17/10)^2`. También
`dist(A_N,B_N)-N <= (sqrt3-1)N`, tomando los centros, que son sitios de red.
Por tanto el margen es `Theta(N)`, en particular `O(N)`. Los centros sólo
se usan para esta cota superior; la separación inferior cubre las regiones
completas. Con `u=(1,1,1)` se obtiene asimismo

\[
u\cdot(y-x)\ge(3-\sqrt3/2)N. \tag{G}
\]

Los bloques de Laurent heredados son
`W_(1,1,1)=diag(1/4,0)` y `W_(-1,-1,-1)=diag(0,1/4)`.
Para llegar a un vértice en `N` pasos cada paso debe ser ese mismo vértice:

\[
K_N((N,N,N),0)=4^{-N}\operatorname{diag}(1,0)\ne0,
\quad (S^N)_{(N,N,N),0}=4^{-N}\operatorname{diag}(0,1)\ne0.
\]

Así se certifica tanto el candidato literal del charter como el sentido de
propagación de estados. Ese par pertenece a las dos regiones y al soporte
exacto microscópico, en su frontera. No se afirma que todos los pares sean
microscópicamente accesibles: algunos desplazamientos quedan fuera de
`[-N,N]^3` y tienen kernel exactamente cero.

## 3. Carta y dominio analítico [A]

Se usa el símbolo literal `walk2()`, con `S(p)=W(p)^{-1}` y
`f(p)=tr S(p)/2=cos(p1)cos(p2)cos(p3)`, `det S=1`.
La inversión, y no la conjugación antiholomorfa, define la continuación
compleja. Tanto `W` como `S=adj W` son polinomios trigonométricos enteros.

En el toro real las colisiones de eigenvalores exigen `f=+1` o `f=-1`;
esto ocurre sólo cuando cada coordenada está en `pi Z`, módulo `2pi`.
En la bola `|p|<pi/4` sólo queda el nodo `p=0`, donde `W=I`.
Todos los cosenos son positivos y `0<f<=1`; por tanto no hay eigenvalor
`-1` ni corte del logaritmo principal. Las dos bandas se conservan; los
proyectores individuales pueden ser singulares en el nodo, pero el
logaritmo matricial es regular allí. `1/sqrt(N)<=1/sqrt2<pi/4` para `N>=2`
(basta `pi>3>2sqrt2`), así que ambas bandas del contrato están en la carta.

La expansión directa es `W=I+iH_W+O(|p|^2)`,
`H_W=p1 sigma1-p2 sigma2+p3 sigma3`, `H_W^2=|p|^2 I`.
La continuación de potencias usará el símbolo entero en el tubo entre el
toro real y su desplazamiento complejo, sin exigir una rama global de
`arccos(f)`. Las colisiones complejas `f^2=1` no son polos de `S^N`;
deben tratarse sin dividir por la separación de eigenvalores.

La normalización, por integración radial exacta, es

\[
Z_N=\frac{64}{3465\pi^2 N^3},\qquad
\int g(Np)d\mu=\frac4{105\pi^2N^3},\qquad
|\phi_N(0)|^2=\frac{11}{140\pi^2N^3}.
\]

**Geometría y carta: PASS.** No se detecta aquí una inconsistencia que
active la parada. La carta local no se usa como sustituto del control del
toro complejo completo requerido para una upper bound de propagación.

## 4. Admisibilidad IR [A]

Escribimos `F_N(x)=(1-16|x|^2/N^2)^2_+` y
`a_M(x)=exp(i pi F_N(x) M/2)-I`. Cada `M` es una involución hermítica.
El perfil extendido por cero es globalmente Lipschitz, con constante
`16/N`: dentro de la bola, `|grad F_N|=64|x|(1-16|x|^2/N^2)/N^2<=16/N`,
y la derivada se anula en la frontera. En consecuencia
`||a_M||_infty<=2`, `Lip(a_M)<=8pi/N`. Para `h_B M_B`, las constantes son
`1` y `16/N`, ya que los cuatro `M_B` tienen norma uno.

### 4.1 Cotas de operador, uniformes en toda la banda de entrada

Sea `D_j xi(x)=xi(x+e_j)-xi(x)`. Por Plancherel y
`sin(t)>=2t/pi` para `0<=t<=pi/2`,

\[
\|(I-\Pi')\xi\|\le\frac{\pi}{2\Lambda'}
 \Big(\sum_j\|D_j\xi\|^2\Big)^{1/2}.
\]

Si `Pi psi=psi`, entonces `||D psi||<=Lambda ||psi||`. La regla de
producto discreta y Minkowski dan, para un multiplicador de norma `A`
y constante Lipschitz `L/N`,

\[
\|(I-\Pi')a\Pi\|\le\frac\pi2(A+\sqrt3 L)N^{-1/2}.
\tag{IR1}
\]

Definimos las constantes explícitas

\[
K_e=\frac\pi2(2+8\sqrt3\pi),\qquad
K_d=\frac\pi2(1+16\sqrt3).
\]

Esta prueba controla las operaciones completas sobre cualquier vector en
la banda de entrada; no descompone ni proyecta la señal de Bob.

### 4.2 Denominadores no nulos y uniformemente separados de cero

La componente escalar real `b_N` de `phi_N=b_N down` satisface, para
`|x|<=N`,

\[
b_N(x)=Z_N^{-1/2}\int g(Np)\cos(p\cdot x)d\mu
\ge\tfrac12\sqrt{11/(140\pi^2)}\,N^{-3/2}.
\]

Se usó `cos t>=1-t^2/2>=1/2` para `|t|<=1`. Para `N>=32`, tomamos
únicamente como conjuntos auxiliares de prueba, sin cambiar las regiones:

- `Q_in={|x_j|<=N/32}`: al menos `(N/32)^3` sitios,
  `F_N >= (61/64)^2 > 1/2`.
- `Q_out={N/2<=x1<=5N/8, 0<=x2,x3<=N/8}`: al menos `(N/16)^3`
  sitios, `F_N=0`, `|x|<N`.

Ambos tienen probabilidad al menos

\[
m=\frac{11}{560\pi^2\,32^3}>0.
\]

En `Q_in`, `theta F_N` pertenece a `[pi/4,pi/2]`. Por tanto, para las
cuatro `M`, `a_M^*a_M=2(1-cos(theta F_N))I` y

\[
\|a_M\Pi\|\ge b_e:=\sqrt{(2-\sqrt2)m}>0.
\]

Para el detector, se puede probar la norma de operador sobre el mismo
paquete **trasladado** al centro de Bob, con un autovector de eigenvalor
uno de `M_B`. Es sólo un vector de prueba para la norma, no un cambio del
recurso físico. Su soporte espectral sigue en `Pi`. Así

\[
\|(h_B\otimes M_B)\Pi\|\ge b_d:=\sqrt m/2>0.
\]

Con `w_x=|b_N(x)|^2`, `t_x=<down|U_M(x)|down>` y `z=sum_x w_x t_x`,
se tiene `|t_x|<=1`. Para un punto de `Q_in` y otro de `Q_out`,
`Re(t_x conjugate(t_y))=cos(theta F_N(x))<=1/sqrt2`. Para todos los
otros pares, esa parte real es como máximo uno. Sumando las dos
orientaciones de esos pares se obtiene

\[
1-|z|^2\ge(2-\sqrt2)m^2,\qquad
\|\Delta_M\|_1=2\sqrt{1-|z|^2}\ge d_e:=2m\sqrt{2-\sqrt2}>0.
\tag{IR2}
\]

Esto cubre separadamente `t_x=e^{i theta F_N}` para `I`,
`t_x=cos(theta F_N)` para `sigma1,sigma2`, y
`t_x=e^{-i theta F_N}` para `sigma3`; no invoca simetría del protocolo.
Para los finitos `2<=N<32`, el origen tiene peso positivo y fase distinta
de cero y hay un punto exterior de peso positivo con `|x|<=N`; por ejemplo
`x=(floor(N/4)+1,0,0)`. El mismo argumento prueba denominadores no nulos,
sin necesitar las constantes uniformes anteriores.

### 4.3 Norma de traza y tabla completa

Para `v=U_M phi_N`, `w=Pi' v`, `r=v-w`, se tiene
`Delta_M-Pi' Delta_M Pi'=|v><v|-|w><w|`, porque `Pi' phi_N=phi_N`.
La identidad `|v><v|-|w><w|=|r><v|+|w><r|` da norma de traza `<=2||r||`.
Por (IR1), `||r||<=K_e/sqrt N`, de donde, para `N>=32`,

| Operación | Cota relativa explícita | Límite | Admisibilidad |
| --- | --- | --- | --- |
| Encoder `I` (`REFERENCE_CONTROL`) | `eta_op<=K_e/(b_e sqrt N)`; `eta_enc<=2K_e/(d_e sqrt N)` | ambos 0 | PASS |
| Encoder `sigma1` | mismas dos cotas, demostradas con `M^2=I` | ambos 0 | PASS |
| Encoder `sigma2` | mismas dos cotas, demostradas con `M^2=I` | ambos 0 | PASS |
| Encoder `sigma3` | mismas dos cotas; actúa como fase sobre `down` al elegir | ambos 0 | PASS |
| Detector `I` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |
| Detector `(I+sigma1)/2` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |
| Detector `(I+sigma2)/2` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |
| Detector `(I+sigma3)/2` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |

Las constantes son conservadoras, no ajustadas numéricamente. Las cotas
son asintóticas explícitas y no aseguran un pequeño error para `N=2`.
La tabla cubre las familias congeladas y no todos los generadores internos
ni todos los efectos locales posibles.

### 4.4 Sanity check puntual

Sea `kappa'=1/(6pi^2 N^(3/2))`, medida de la bola de radio `Lambda'`.
Para cualquier vector de un sitio, la fracción de norma cuadrada dentro
de `Pi'` es exactamente `kappa'`. Por tanto, con entrada `Pi`,

\[
\eta_{enc,op}^{point}=\eta_{read}^{point}=\sqrt{1-\kappa'}\longrightarrow1.
\]

Para la puerta `I-2P_0`, la reducción de Gram del gate anterior se aplica
con `Pi'` porque `Pi' psi=psi`. Con `s=||P_0 psi||^2`,

\[
\eta_{enc}^{point\,2}=
\frac{(1-\kappa')[1-3s(1-\kappa')]}{1-s}\longrightarrow1.
\]

Vale para el recurso actual (`s=11/(140pi^2 N^3)`) y para el recurso
puntual anterior `psi=S^2 phi_N`: por su prueba congelada,
`cos^2(2/N) 11/(140pi^2N^3)<=s<=11/(140pi^2N^3)`. En ambos casos
`0<s<=kappa'`, con denominador positivo. Así, el sanity check prueba
literalmente la persistencia del negativo puntual con las dos escalas.

## 5. Stop rule

**Admisibilidad: PASS. Sanity check: PASS. Stop rule: NO ACTIVADA.**
Las tres Pauli y el control pasan. Se continúa con los dieciséis pares.
No se ha evaluado aún señal alguna para obtener este resultado.

## 6. Upper bound geométrica: derivación direccional [A]

Esta prueba es independiente de los encoders, detectores y recurso
concretos. No usa la LDP radial ni su maximización numérica.

### 6.1 Lema de producto de elipses

Para `a>1` escribimos
`E_a={z: (Re z)^2/a^2+(Im z)^2/(a^2-1)<=1}`. Entonces

\[
E_a E_c\subset E_{ac},\qquad a,c>1. \tag{E}
\]

Prueba explícita. Basta fijar un punto de la frontera del primer factor,
`z=a cos p+i sqrt(a^2-1) sin p`; los puntos interiores son contracciones
radiales de éstos. Multiplicar por `z` y pasar de coordenadas unitarias de
`E_c` a las de `E_ac` da la matriz real

\[
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\
\sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
\]

Sean `A=a^2`, `C=c^2`, `u=cos^2 p`. Las identidades exactas [V] son

\[
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},
\]
\[
(I-L^TL)_{22}=(1-u)\frac{A+C-1}{AC}
 +u\frac{A-1}{AC-1},
\]
\[
\det(I-L^TL)=
\frac{(C-1)(1-u)[A-1+C(1-u)]}{AC(AC-1)}.
\]

La entrada extra-diagonal `(I-L^TL)_{12}` no es idénticamente cero: cambia
de signo con `sin p` y `cos p`. El criterio de Sylvester para una matriz
`2x2` simétrica usa `g_{11}>=0` y `det>=0`; el extra-diagonal queda
absorbido en el determinante ya escrito. Los tres polinomios mostrados son
no negativos para `A,C>1`, `0<=u<=1`; luego `I-L^TL>=0`.
Esto prueba (E), incluida la frontera por continuidad. La implicación de
los menores a positividad y la inclusión geométrica son [A], no checks.

### 6.2 Espectro complejo y colisiones

Se fija el desplazamiento de contorno `t=log 2`, en la dirección
`u=(1,1,1)`. Cada `cos(p_j-it)` pertenece a `E_cosh(t)`; (E) aplicado dos
veces prueba uniformemente en **todo** el toro real

\[
f(p-it u)\in E_{\cosh^3 t}=E_{125/64}.
\]

Para una matriz unimodular, los eigenvalores `lambda,lambda^-1` satisfacen
`(lambda+lambda^-1)/2=f`. Si `|lambda|=r>=1`, la imagen es una elipse
de semieje mayor `(r+r^-1)/2`. Las elipses están anidadas, por lo que

\[
\rho(S(p-it u))\le e^{\kappa},\qquad
\kappa=\operatorname{arcosh}(125/64)<\log4,
\]

pues `125/64 < 17/8=cosh(log4)`. No se selecciona una rama global de
eigenvalores. Esto cubre también `f=+1,-1` y cualquier nodo del toro.

Los catorce bloques de `S` tienen suma de normas `4` [V]: ocho vértices
de norma `1/4`, cuatro desplazamientos `(+-1,+-1,0)` de norma `1/4` y
dos axiales de norma `1/2`. Como `|u·d|<=3`,

\[
\|S(p-it u)\|\le4e^{3t}=32.
\]

En la forma de Schur unitaria `T=[[lambda1,b],[0,lambda2]]`, `|b|<=32` y
`|lambda_j|<=4`. La entrada superior de `T^N` es
`b sum_(j=0)^(N-1) lambda1^j lambda2^(N-1-j)`, también para eigenvalores
coincidentes. La norma de operador de la parte diagonal es el máximo,
`||diag(lambda1^N, lambda2^N)||_2 = max_j |lambda_j|^N <= 4^N`, y
`|||e1><e2|||_2 = 1`. Por tanto

\[
\|S(p-it u)^N\|\le4^N+32N4^{N-1}\le9N4^N. \tag{P}
\]

Se ha controlado el posible factor de Jordan sin dividir por un gap.

### 6.3 Contorno y norma entre las regiones completas

Con Fourier inversa `e^{-ip·d}`, se desplaza **hacia abajo**,
`p -> p-it u`. El factor se convierte en `e^{-t u·d}`. La periodicidad y
el carácter entero cancelan las caras laterales del contorno. (P) da

\[
\|(S^N)_{y,x}\|\le9N\exp[-t\,u\cdot(y-x)+N\log4].
\]

Usando (G), para todos los pares de las regiones congeladas,

\[
\|(S^N)_{y,x}\|\le9N e^{-JN},\qquad
\boxed{J=(1-\sqrt3/2)\log2>0}. \tag{J}
\]

`J` es una tasa inferior certificada para el exponente de una **upper
bound**, no una tasa óptima ni una equivalencia asintótica. La desigualdad
es direccional: se derivó con la proyección sobre `u` y sirve en todo
`(B_N-A_N)/N`. No afirma resolver `I(v)` en otras geometrías.

Cada región tiene a lo sumo `(N/2+1)^3<=N^3` sitios (`N>=2`). La cota de
Schur por bloques, o Cauchy–Schwarz para la suma de normas, da

\[
T_N:=\|P_{B_N}S^NP_{A_N}\|\le9N^4e^{-JN}. \tag{T}
\]

### 6.4 De propagación a distinguibilidad operacional

En el sector de una partícula, para cualquier estado puro normalizado y
cualquier unitario que actúe como identidad fuera de Alice,
`||v1-v0||<=2T_N`, con `v_b=P_B S^N U_b psi`.
El estado reducido completo es
`(1-||v_b||^2)|vac><vac|+|v_b><v_b|`, incluidos todos los modos de Bob.
Como `||v_b||<=1`, se usa la convención de distancia de traza del charter
narrow-band, `D_B=\tfrac12\|\rho_1-\rho_0\|_1`, que es la que hace
`D_B>=delta`. Con `X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|` y
`α=-tr X` en el bloque de vacío, `\|\rho_1-\rho_0\|_1=|α|+\|X\|_1`, luego

\[
D_B=\tfrac12\bigl(|α|+\|X\|_1\bigr)\le\|X\|_1
\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|
\le4T_N\le36N^4e^{-JN}. \tag{D1}
\]

La desigualdad `D_B\le\|X\|_1` incluye el bloque de vacío porque
`|tr X|\le\|X\|_1`. Convexidad extiende (D1) a cualquier estado mixto de
una partícula. Todo efecto físico de Bob satisface `delta<=D_B`; esto
incluye exactamente los cuatro del charter.

Para no dejar ambigua la frase «toda operación unitaria, todo estado» de
§6, también se obtiene una cota uniforme en el CAR completo para unitarios
**pares** locales de Alice, sin restringir a Gaussianos ni a una partícula:

\[
D_B\le32|B_N|T_N\le288N^7e^{-JN}. \tag{DF}
\]

Prueba. El subespacio de los `d_B=2|B_N|` modos de Bob evolucionados hacia
atrás es `L=(S^N)^* ran P_B`; su proyección a Alice tiene norma `T_N`.
Si `T_N<1/2`, proyectar `L` en `A^perp` y ortonormalizar produce `L'`
de la misma dimensión. Sus ángulos principales con `L` son como máximo
`arcsin T_N<=2T_N` (los valores singulares de la proyección a `A^perp`
son `sqrt(1-s_j^2)`, `s_j<=T_N`). La rotación canónica `V` que lleva
`L` a `L'` actúa en dimensión a lo sumo `2d_B`, con fases `+-theta_j`.
Su segunda cuantización cumple
`||Gamma(V)-I||<=sum 2theta_j<=4d_B T_N` por
`|e^{i alpha}-1|<=|alpha|` para cada suma de fases ocupadas.
Todo efecto `E` en el álgebra de `L` queda a distancia de norma
`<=2||Gamma(V)-I||` de un efecto `E'` en `L'`. Este último conmuta con
todo unitario par de Alice, pues `L'` es ortogonal a sus modos. Luego
`||U^* E U-E||<=2||E-E'||<=16d_B T_N=32|B_N|T_N`.
Tomar el supremo sobre efectos prueba (DF), para cualquier estado.
Si `T_N>=1/2`, la misma cota se cumple trivialmente por `D_B<=1`.
Se trata de una cota adicional para los cuantificadores de la obligación;
no amplía las familias ni los recursos evaluados por el gate.

Para los dieciséis pares se usará la cota más fuerte (D1), junto con
`delta<=1`: `U_N=min(1,36N^4 exp(-JN))`. Queda excluida una lower bound
polinómica positiva. **No se ha demostrado positividad de ninguna señal.**

## 7. Análisis de los dieciséis pares: lower bounds y cancelaciones [A]

### 7.1 Reducción exacta de la señal física, sin proyección espectral

Definimos, sólo como abreviaturas de amplitudes del protocolo,

\[
c_N(x)=\cos(\pi F_N(x)/2)-1,\qquad
s_N(x)=\sin(\pi F_N(x)/2),\qquad \phi_N(x)=b_N(x)\downarrow,
\]
\[
r=P_B S^N\phi_N,\quad a=P_B S^N(c_N b_N\downarrow),\quad
b=P_B S^N(s_N b_N\uparrow),\quad d=P_B S^N(s_N b_N\downarrow),
\qquad v=r+a.
\]

`P_B` aquí restringe a los sitios del aparato físico; **no** es `Pi` ni
`Pi'`. Todas las convoluciones son exactas: por ejemplo,

\[
a(y)=\sum_{x\in A_N}(S^N)_{y,x}c_N(x)b_N(x)\downarrow,
\qquad
r(y)=\int e^{-ip\cdot y}S(p)^N\widehat\phi_N(p)d\mu.
\]

La primera suma es finita por soporte exacto del encoder. La segunda
integral representa el recurso completo, sin truncar su cola espacial.
También se puede escribir como suma finita sobre los desplazamientos del
kernel de `S^N`, evaluando `b_N(y-d)` por su integral exacta. No se ha
sustituido el recurso por uno de soporte espacial finito.

Las cuatro amplitudes de Bob codificadas son, por acción explícita de cada
Pauli sobre `down` [V],

| Encoder | Amplitud física codificada en Bob |
| --- | --- |
| `I` | `v+i d` |
| `sigma1` | `v+i b` |
| `sigma2` | `v+b` |
| `sigma3` | `v-i d` |

Esto no supone equivalencia entre direcciones. Para un detector concreto
`E=h_B M_B` y `H_E=<v,E v>-<r,E r>`, se obtienen las identidades
de respuestas **con signo**

\[
L_{I,E}=H_E+\langle d,Ed\rangle-2\operatorname{Im}\langle v,Ed\rangle,
\quad
L_{3,E}=H_E+\langle d,Ed\rangle+2\operatorname{Im}\langle v,Ed\rangle,
\]
\[
L_{1,E}=H_E+\langle b,Eb\rangle-2\operatorname{Im}\langle v,Eb\rangle,
\quad
L_{2,E}=H_E+\langle b,Eb\rangle+2\operatorname{Re}\langle v,Eb\rangle.
\tag{L}
\]

Siempre `delta_(M,M_B)=|L_(M,E)|`. En particular, un término cuadrático
positivo en (L) **no** prueba positividad de la respuesta completa: puede
cancelarse con `H_E` o con la interferencia.

Para mostrar los cuatro detectores de cada encoder sin omitir componentes,
sea la matriz interna hermítica

\[
R_M=\sum_{y\in B_N}h_B(y)
 [\psi_1^M(y)\psi_1^M(y)^*-r(y)r(y)^*]
 =\begin{pmatrix}\alpha_M&z_M\\\bar z_M&\beta_M\end{pmatrix}.
\]

Con datos de la **misma** pareja física de estados, las cuatro respuestas
son exactamente [V]

\[
\begin{split}
F_0(R_M)&=\alpha_M+\beta_M,\\
F_1(R_M)&=(\alpha_M+\beta_M)/2+\operatorname{Re}z_M,\\
F_2(R_M)&=(\alpha_M+\beta_M)/2-\operatorname{Im}z_M,\\
F_3(R_M)&=\alpha_M.
\end{split} \tag{F}
\]

Así los detectores Pauli no han sido sustituidos por ocupación total.
La matriz `R_M` es suficiente para estos cuatro efectos, pero no contiene
todas las coherencias entre sitios del estado reducido de Bob: ni siquiera
probar `R_M=0` bastaría por sí solo para concluir `D_B=0`.

### 7.2 Intentos de cerrar una lower bound y obligación que queda abierta

Se examinaron las siguientes vías sobre (L), para cada una de sus cuatro
columnas de detector (F):

1. **Extraer el rayo de vértice.** El término del kernel de §2 es no nulo,
   pero las amplitudes son sumas coherentes de todos los sitios de Alice,
   y (L) incluye la interferencia con `r`. No hay una desigualdad inferior
   que sobreviva al reemplazo de estas sumas por un término. La prueba de
   camino único para un bloque no se extiende a la señal de región.
2. **Usar positividad del efecto.** Da `delta>=0` y positividad de los
   términos cuadrados, pero no signo de su diferencia con el estado de
   referencia. (L) expone explícitamente los términos que faltaría dominar.
   En `I` y `sigma3`, cambiar el signo de la fase cambia un término de
   interferencia; no certifica ni igualdad ni no nulidad de sus respuestas.
   En `sigma1` y `sigma2` se requieren, respectivamente, las partes
   imaginaria y real de un solapamiento distinto. No se identifica ninguna
   de ellas mediante una simetría no probada del protocolo.
3. **Saddle del contorno de §6.** El lema de elipses controla un supremo de
   norma; no identifica el término dominante de las sumas con `c_N,s_N,h_B`
   ni su fase relativa a `r`. Los perfiles se anulan en las fronteras y las
   bolas son conjuntos de red dependientes de `N`. No se ha obtenido una
   expansión uniforme con resto relativo ni una amplitud principal no nula
   para ninguna de las dieciséis respuestas. El uso de Schur evita
   singularidades para la upper bound, pero no resuelve esa obligación.
4. **Aproximación Weyl en la banda.** La cota heredada por paso es
   `||S-e^{-iH_W}||<=O(N^-2)` sobre `Pi`, y la telescópica hasta `N` pasos
   da error `O(N^-1)`. Para el estado codificado, el control IR probado es
   también algebraico. Estos errores no permiten resolver el signo de una
   cantidad cuya upper bound es exponencial. No se usan para atribuir la
   señal a una banda ni para reemplazarla por otra observable.

Estos son límites de lo demostrado en este run, **no** pruebas de que una
lower bound sea imposible. No se ejecutó un barrido de valores finitos de
`N` ni se usó coma flotante para inferir ceros. No se dispone de diagnóstico
numérico `SUPPORTED` con error certificado que añadir.

### 7.3 Tabla exhaustiva de la familia congelada

En la tabla, `P_j=(I+sigma_j)/2`, `U_N=min(1,36N^4e^{-JN})` y
`F_j` es la respuesta física exacta (F). «No decidida» significa que no se
ha demostrado ni cero exacto eventual ni estricta positividad eventual.
La lower bound `0` es sólo la trivial; no cumple ningún criterio positivo.
`OPEN_PAIR` es una etiqueta individual, no un estado terminal adicional.

| Encoder | Detector | Admisibilidad | Upper bound | Lower bound / asintótica | Signo / no nulidad | Estado individual |
| --- | --- | --- | --- | --- | --- | --- |
| `I` (REFERENCE_CONTROL) | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_I))` | no decidida | OPEN_PAIR |
| `I` (REFERENCE_CONTROL) | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_I))` | no decidida | OPEN_PAIR |
| `I` (REFERENCE_CONTROL) | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_I))` | no decidida | OPEN_PAIR |
| `I` (REFERENCE_CONTROL) | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_I))` | no decidida | OPEN_PAIR |
| `sigma1` | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_1))` | no decidida | OPEN_PAIR |
| `sigma1` | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_1))` | no decidida | OPEN_PAIR |
| `sigma1` | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_1))` | no decidida | OPEN_PAIR |
| `sigma1` | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_1))` | no decidida | OPEN_PAIR |
| `sigma2` | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_2))` | no decidida | OPEN_PAIR |
| `sigma2` | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_2))` | no decidida | OPEN_PAIR |
| `sigma2` | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_2))` | no decidida | OPEN_PAIR |
| `sigma2` | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_2))` | no decidida | OPEN_PAIR |
| `sigma3` | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_3))` | no decidida | OPEN_PAIR |
| `sigma3` | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_3))` | no decidida | OPEN_PAIR |
| `sigma3` | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_3))` | no decidida | OPEN_PAIR |
| `sigma3` | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_3))` | no decidida | OPEN_PAIR |

## 8. Clasificación final

**Único estado terminal asignado: `OPEN_AFTER_SCALED_IR_ANALYSIS`.**

Se aplica literalmente la regla explícita de §7 del charter: hay upper
bound exponencial con `J>0`, pero no lower bound positiva ni asintótica
de amplitud no nula para ningún par. Las operaciones son IR-admisibles;
la exclusión por admisibilidad no procede. No se ha demostrado la
obstrucción exacta `D_B=0` para la familia. La alternativa polinómica queda
excluida por (D1). La alternativa positiva exponencial no está certificada.

No se asignan constantes `C_1`, `c`, `p` ni `N_*` de una lower bound que
no se ha obtenido. Para las upper bounds sí se dan constantes efectivas:
`C_2=J=(1-sqrt3/2)log2`, `C=36`, `q=4`, para todo `N>=2` en el sector
congelado; y `C=288`, `q=7` para la cota CAR general (DF).

## 9. Techo de reclamo

Demostración analítica del autor: geometría y carta admisibles, encoders y
detectores de las familias congeladas IR-admisibles, sanity puntual correcto,
upper bound direccional exponencial para la propagación y la distinguibilidad.
No hay revisión independiente nueva ni certificación formal de las pruebas.

No demostrado: positividad eventual de `delta`, nulidad exacta de `D_B`,
lower bound, asintótica equivalente, tasa óptima, ni transporte de la señal
por el sector IR. No se califica la señal de «puramente de red» ni se adopta
la lectura positiva reservada por §7 al estado exponencial señalizante.

Las cotas IR son propiedades de las operaciones; la señal física siempre
es la estadística no proyectada del protocolo. La familia interna no es
exhaustiva fuera de los dieciséis pares declarados. `I` es exclusivamente
`REFERENCE_CONTROL`, con nulidad desconocida. La acción de `sigma3` como
fase inicial no autoriza a borrarla de la familia.

Se mantienen sin cambios los witnesses `3/128`, narrow-band, no-corner,
y `Delta T=2` como frente separado. No se fija `a`, `tau`, metros, segundos
ni eV; no hay predicción experimental ni afirmación sobre nuestro universo.
Tampoco se formula una reclamación de novedad bibliográfica.

## 10. Implementación

Sólo se crean este informe y `scripts/verify_scaled_ir_gate.py`. No se
modifica ningún archivo preexistente. El nuevo certificado está limitado a
este gate y reutiliza `walk2`, `is_zero`, `PAULI`, `PS` y `exact_blocks`.

Justificación: los helpers existentes bastan para extraer el símbolo y sus
bloques, pero no contienen la identidad de contracción de elipses ni las
identidades de las operaciones extendidas. Los helpers `evolve` y
`reduced_state` asumen estados de soporte espacial finito; no representan
el recurso actual. Añadir estas comprobaciones a un verificador revisado
cambiaría innecesariamente sus bytes. El archivo separado preserva esa
evidencia y deja trazabilidad permanente de las identidades nuevas.

Cobertura real: el script comprueba el hash del charter, geometría
algebraica, bloques orientados y recurrencia, símbolo y normalización,
identidades internas de las operaciones, límites del sanity puntual,
identidades racionales del lema de elipses, constantes del contorno, suma
de normas de los bloques y los dieciséis funcionales de respuesta.
**No** calcula señales ni certifica positividad. Tampoco formaliza
Plancherel/Minkowski, el conteo de los cubos para todo entero, las cotas de
denominadores y norma de traza, el paso de menores a contracción, el
argumento de contorno, Schur, la reducción CAR, ni las conclusiones
asintóticas que dependen de esas pruebas. Todo ello está demostrado o
declarado abierto en el texto [A], no inferido de un contador de checks.

Dependencias: biblioteca estándar de Python, SymPy y, transitivamente por
`verify_directional_saturation`, NumPy. SymPy y NumPy ya están declarados en
`scripts/requirements.txt` (`1.14.0` y `1.26.4`). SymPy depende a su vez de
mpmath, cuya versión instalada se registra en validación. No se instala
ninguna dependencia nueva. No se usa punto flotante en las cantidades
decisivas del certificado. Los diagnósticos numéricos de las regresiones
históricas conservan su nivel `SUPPORTED` y no apoyan este veredicto.

## 11. Validación

Todos los comandos científicos siguientes terminaron con código de salida
`0`. Se ejecutaron desde la raíz con `python3 -B`, sin `--output` ni
escritura sobre registros anteriores. Los logs de ejecución auxiliares se
capturaron en `/tmp/scaled-ir-*.log`; la procedencia permanente son los
scripts existentes y el certificado nuevo.

| Comando después de `python3 -B` | Resultado |
| --- | --- |
| `scripts/verify_scaled_ir_gate.py` | 53/53 identidades exactas |
| `scripts/verify_narrow_band_gate.py` | 34/34 exactas; negativo congelado conservado |
| `scripts/verify_directional_saturation.py` | 27/27; incluye diagnósticos históricos `SUPPORTED` |
| `scripts/verify_directional_saturation.py --local-preparation-only` | 21/21 exactas |
| `scripts/verify_directional_saturation.py --noncorner-gate-only` | 20/20 exactas |
| `scripts/verify_signaling_witness.py` | 17/17 exactas |
| `scripts/verify_weyl_dirac_gate.py` | PASS, 375 comprobaciones exactas |
| `scripts/cert_Aa_s4_counterexample.py` | PASS |
| `scripts/review_Aa_s4_exact.py` | PASS, 117 identidades matriciales o escalares |

Entorno efectivo: Python `3.12.3`, SymPy `1.14.0`, NumPy `1.26.4`,
mpmath `1.3.0`. No se añadieron dependencias. El import del helper hace
trabajo simbólico a nivel de módulo; no ejecuta sus suites ni aporta un
diagnóstico numérico al gate nuevo.

Durante la construcción del certificado, una comparación sintáctica de
`cosh(log 2)` con `5/4` produjo un fallo cerrado tras 29 checks. Se corrigió
la **normalización simbólica del checker**, usando la representación exacta
en exponenciales. No se cambió la igualdad objetivo, ninguna constante
científica ni el charter. La ejecución completa posterior dio 53/53.

`git diff --check`: sin incidencias. Se comprobó además whitespace de los
dos archivos nuevos con `git diff --no-index --check /dev/null <archivo>`:
sin salida de errores (el modo no-index señala la existencia de archivos
diferentes con exit 1). Los nuevos archivos no fueron staged.

SHA256 del certificado nuevo:
`b8c6b56ea114b7cf135c73d344dc7a4911d43d7cba8cef609ea3dcfee415763c`.

Manifiesto de preservación de los helpers revisados:

| Archivo | SHA256 inicial y final |
| --- | --- |
| `verify_directional_saturation.py` | `1d1894730f83ea24808bb5e939492fe2144fdd97cdcf87961a0978da35ae4596` |
| `verify_narrow_band_gate.py` | `23be80f2dad55313eb7f0fc88a9dd4429666af3fb2172b10f17ac0951b8d4586` |
| `verify_signaling_witness.py` | `4953009ebf838b98e0dd095e4cbeefdde1bc65a83ee716e96d1ce3eb9ee58d17` |
| `verify_weyl_dirac_gate.py` | `6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597` |

Manifiesto de los untracked preexistentes (bytes y mtimes preservados):

| Archivo | SHA256 |
| --- | --- |
| `Auditoría De Novedad Matemática.md` | `a5e2f98e74231be68641b73493d67a36d7ee1a891dc0985ce850899a5c2b92f1` |
| log `2026-09-15--1100--siguiente-gate-b-infinito-post-s4` | `b33727d824f711b1f4b8919870ea9edf6ef0b67cbeb91936fe7cb07e639bb1fa` |
| log `2026-09-16--ratificacion-gate-completitud-axial-n3` | `d4855e39d9800733fae01d3454cf14443d0b4aab1ce830fa58c21e57fe091486` |
| `__pycache__/verify_directional_saturation.cpython-312.pyc` | `39fa4fc6e2d61bd1d690951b6087f48eea1c040dc7963ecea4fb909a29a44272` |
| `__pycache__/verify_signaling_witness.cpython-312.pyc` | `d3eeec7b6ae396db63a4e33fd2377824d8aaa023ac12227b1b989d79b2fbe732` |

Estado final: los cuatro untracked previos más los dos archivos nuevos;
ningún cambio tracked ni staged. `HEAD` y la referencia remota local siguen
en el baseline exacto. Charter y `CURRENT_STATE.md` conservan los hashes
de §1. **Sin modificación del contrato, sin promoción, sin commit ni push.**

## 12. Registro de congelación (redacción solamente)

Tras la revisión independiente `PASS` (sin reparaciones obligatorias), se
incorporan aquí las tres aclaraciones de redacción recomendadas. **No
cambian** `J`, el prefactor `36 N^4`, (D1), (P), el lema de elipses, ni el
estado `OPEN_AFTER_SCALED_IR_ANALYSIS`.

| Aclaración | Dónde | Contenido |
| --- | --- | --- |
| Convención `D_B=\tfrac12\|\rho_1-\rho_0\|_1` | §6.4, (D1) | Explicitada; es la del charter narrow-band y la que hace `D_B\le\|X\|_1` con constante `36` |
| Extra-diagonal de `I-L^TL` | §6.1 | `(I-L^TL)_{12}` no es idénticamente cero; Sylvester usa `g_{11}` y el `det` ya escrito |
| Norma de Schur de la diagonal | §6.2, (P) | `\|\mathrm{diag}(\lambda_1^N,\lambda_2^N)\|_2=\max_j\|\lambda_j\|^N` |

Sha256 del informe **antes** de estas tres frases:
`4876ecab8ed6a7000aa2d2b991ad4bbb12a3f29538d2a7be910fb9c5476b7f31`.
El hash posterior no se autoincluye aquí; se registra en la revisión
independiente y en `CURRENT_STATE` §8.17. El certificado y el charter no
se tocan. La cota CAR (DF) sigue siendo adicional al sector de una
partícula y no forma parte del claim de los dieciséis pares.
```

### Contexto adjunto: reports/2026-09-24--h1c-return-kernel-schur-audit.md
```
# H1c: auditoría de la cota Schur y cierre del contrato operacional

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Objeto: el resolvente Volterra de
`reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md`.
`H1c_LOCALIZATION (L') = OPEN`.

**Cierre de sesión, 2026-09-24:** §§1–5 conservan el precheck analítico
previo, preliminar y sin revisión independiente. §6 congela por instrucción
expresa del usuario `TWO_DISTINGUISHABLE_CHANNELS`, con observable primario
`(L_+, L_-)`. H1c-0a está CLOSED; H1c-0b está
FIXED_BY_EXPLICIT_ASSUMPTION. La justificación física concreta sigue OPEN.
Volterra/localización asintótica: PAUSED; la prueba de H1c sigue abierta.
§7 fija el orden de la próxima sesión y no registra su ejecución.

## 1. La suma propuesta no implica la cota de susceptibilidad

Pongamos `R_{m,k}=B_mG_Q(m,k+1)C_k` para `m>k`. La memoria exacta es
\[
(\mathbb M_Nx)_n=
\sum_{m=0}^{n-1}\sum_{k=0}^{m-1}
\Phi_P(n,m+1)R_{m,k}x_k.
\tag{1}
\]
El kernel propuesto
`\widetilde R_{m,k}=\Phi_P(N,m+1)R_{m,k}\Phi_P(k,0)`
es la contribución de **una excursión** al elemento final cuando la
entrada sigue el transporte P libre. No es el kernel de `\mathbb M_N`
sobre secuencias arbitrarias `x_k`: (1) debe evaluarse también en
tiempos intermedios y con todas las posibles entradas `x_k`.

Contraejemplo algebraico: en espacios P y Q escalares, durante N pasos
tomar `A_j=D_j=1` y `B_j=C_j=1/N`, con pesos `w_j=1`. Entonces
`\Phi_P=1`, `G_Q=1`, y para `j>k`,
\[
R_{j,k}=\widetilde R_{j,k}=N^{-2},\qquad
\sup_k\sum_{j>k}\|\widetilde R_{j,k}\|\le N^{-1}.
\tag{2}
\]
Sin embargo, para la secuencia `x_k=1`,
\[
(\mathbb M_Nx)_N
=N^{-2}\sum_{m=0}^{N-1}m
=\frac{N-1}{2N}\longrightarrow\frac12.
\tag{3}
\]
Así, la cota de (2) con `C/N` no implica
`\|\mathbb M_N\|=O(N^{-1})`. El ejemplo refuta sólo esa implicación;
no pretende representar el sector Q del walk inclinado.

Una condición suficiente que sí conserva el transporte temporal es
\[
\boxed{
\mathcal S_N(w):=
\sup_{0\le n\le N}\frac1{w_n}
\sum_{m=0}^{n-1}\sum_{k=0}^{m-1}
\|\Phi_P(n,m+1)R_{m,k}\|w_k
\le\frac{C}{N}.}
\tag{4}
\]
Por la desigualdad triangular, (4) implica
`\chi_N=\|\mathbb M_N\|_{w\to w}\le C/N`. También basta controlar
uniformemente el transporte P ponderado y exigir
`\sup_m w_{m+1}^{-1}\sum_{k<m}\|R_{m,k}\|w_k=O(N^{-2})`.
Con transporte P acotado y pesos unitarios, una suma por columnas
`\sup_k\sum_{m>k}\|R_{m,k}\|=O(N^{-2})` es otra condición suficiente.
El orden `N^{-2}` en estas sumas deja una suma adicional de `O(N)`
tiempos P en (1).
Como caso límite independiente, si `D_j=\rho` con `0<\rho<1`
fijo en el ejemplo escalar, entonces
`R_{j,k}=N^{-2}\rho^{j-k-1}`. La suma en duración es `O(N^{-2})`
por tiempo de origen y (1) es `O(N^{-1})`, como predice (4).

## 2. Cota completa en una norma auxiliar L2

Hay una forma de acotar el retorno **sandwichado** sin exigir una
estimación final para el Green Q desnudo. Se usa una partición
auxiliar que no afirma un Riesz splitting global. Sea W la unión de
vecindades fijas y disjuntas de los ocho saddles. En W, `P(p)` es el
proyector Riesz dominante de rango dos del símbolo libre inclinado;
fuera de W se define `P(p)=0` y `Q(p)=I`. Esta partición es medible y
acotada en `L^2(\mathbb T^3;\mathbb C^4)`; el salto en el borde de W
forma parte de los bloques de la moneda.

Normalicemos por el escalar global `\Lambda=e^{\Phi_*}>1`. El lema
espectral del TeX plano (`papers/ir-corona/ir-corona.tex`,
`lem:specrad` y `lem:symbol(d,e)`) da esa propiedad para S; para
`D=S\oplus S^{-1}` se sigue porque S es unimodular y ambos sumandos
tienen el mismo radio espectral. Por tanto
`\rho(D_\xi(p)/\Lambda)\le1`, con igualdad sólo en los ocho saddles.
En W, el bloque libre Q tiene autovalor
`\lambda(p)^{-1}/\Lambda`, uniformemente dentro del disco unidad.
Fuera de W, `Q=I` y el radio espectral libre es estrictamente menor
que uno por compacidad. En consecuencia existe `\rho_0<1` que
acota el radio espectral de todo el bloque libre Q, aun donde la
matriz exterior sea no normal.

En dimensión finita por fibra, el resolvente de la familia libre en
una circunferencia `\rho_0<\rho_1<1` es uniformemente acotado en
cada uno de los dos compactos (cierres de W y de su exterior).
Por la fórmula de Cauchy,
\[
\|(D_Q^{(0)})^h\|_{L^2\to L^2}
\le C_0\rho_1^h,
\qquad D_Q^{(0)}=Q(D_\xi/\Lambda)Q.
\tag{5}
\]
La norma equivalente
`\|y\|_*:=\sup_{h\ge0}\rho_1^{-h}\|(D_Q^{(0)})^hy\|_2`
satisface `\|D_Q^{(0)}y\|_*\le\rho_1\|y\|_*`.

En la representación de momento, la moneda espacial es convolución,
pero su norma `L^2\to L^2` es la norma del multiplicador en posición:
`\|C_N-I\|\le C/N` para `\vartheta` acotada. Las proyecciones
auxiliares son multiplicadores acotados en momento. Por ello, en
las normas P=`L^2`, Q=`\|\cdot\|_*`, los bloques exactos satisfacen
\[
\|B_j\|,\|C_j\|\le C/N,\quad
\|D_j\|_*\le\rho_1+C/N<\rho_2<1,
\quad\|A_j\|_2\le1+C/N.
\tag{6}
\]
La última desigualdad usa `|\lambda(p)|/\Lambda\le1` en W.
Permite variación uniforme de la moneda entre pasos; no presume
conservación del momento.

De (6) se obtiene directamente para el **retorno completo**
\[
\|R_{m,k}\|_{P\to P}
\le\frac{C}{N^2}\rho_2^{m-k-1},\qquad
\|\Phi_P(n,m+1)\|\le e^C.
\tag{7}
\]
La suma de (4) con `w=1` da
\[
\boxed{\|\mathbb M_N\|_{\ell^\infty_t L^2_p\to
\ell^\infty_t L^2_p}=O(N^{-1}).}
\tag{8}
\]
Esta es una cota preliminar en un espacio auxiliar para el producto
normalizado; la no normalidad exterior queda absorbida en la norma
equivalente de (5). No demuestra la cota física ponderada de `L'`.

## 3. Techo físico de la cota auxiliar

La cota (8) no recupera por sí sola el factor gaussiano tangencial
de los elementos Alice/Bob. `state/CURRENT_STATE.md`, §9.2, sólo
certifica masas absolutas inclinadas `O(N^{-5/2})` para cada extremo.
Usándolas sin información adicional, (8) produciría para la
corrección interna una cota `O(N^{-6})`. La escala líder que se intenta
conservar es `N^{-13/2}`: esa cota gruesa pierde `N^{1/2}` y no prueba
dominancia relativa. Una norma física con envolventes de momento,
fases y endpoints podría recuperar la potencia, pero aún no se ha
fijado ni estimado.

Además, definir `P=0` fuera de W asigna todas las trayectorias
exteriores a Q. Sus entradas/salidas y los saltos entre W y su
exterior siguen presentes en `B,C,D`; (8) no demuestra que la
contribución Q inicial/final al elemento físico sea pequeña.

## 4. Resultado del subgate

- **REFUTADO:** la condición
  `\sup_k\sum_{j>k}\|\widetilde R_{j,k}\|_w\le C/N`
  implica por sí sola `\chi_N=O(N^{-1})`.
- **PRELIMINARY:** la condición correcta es una suma Volterra doble
  como (4), o una suma de retornos `O(N^{-2})` por tiempo bajo
  transporte P controlado.
- **PRELIMINARY:** en `\ell^\infty_t L^2_p`, el splitting auxiliar
  local-en-W / exterior-en-Q y el lema espectral plano dan (8).
- **OPEN:** trasladar (8) a una envolvente física que preserve el
  factor de saddle, y controlar los términos Q de los extremos
  reales de `L'`.

En el precheck de §§1–4 no se ejecutó código numérico ni se modificaron
C2c, el manuscrito o `state/CURRENT_STATE.md`. El cierre documental de §6
sí se resume ahora en el estado canónico, por instrucción del usuario.

## 5. Cortafuegos del elemento físico

Antes del cierre de §6, la prueba propuesta era comparar directamente la primera
corrección `\ell_P(\mathbb M_Nx^{(0)})_N` y los términos con entrada o
salida Q de (8) en el precheck Volterra con el líder `L'_{N,P}`.
La búsqueda en `state/CURRENT_STATE.md`, §9,
`reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md`,
§§8–9, y `reports/2026-09-20--h1-chat-research-log.md`, §§12–13,
no proporciona los extremos físicos de cuatro componentes, el
funcional firmado final ni una cota inferior uniforme para
`|L'_{N,P}|`. El TeX plano, §7.3, fija un elemento de dos componentes;
su embedding en cuatro componentes es un test auxiliar, no una
definición del observable inhomogéneo.

Por ello los cocientes físicos
`\ell_P(\mathbb M_Nx^{(0)})_N/L'_{N,P}` y
`L'_{\mathrm{boundary}-Q}/L'_{N,P}` son **NO EVALUABLES CON EL
CONTRATO ACTUAL**. La cota (8) no se convierte en un PASS de H1c.
Según el cortafuegos de esta línea, se detiene aquí la vía Volterra:
no se introducen nuevas normas, proyectores o resolventes para
suplantar esos datos físicos. Ese diagnóstico describe el contrato anterior.
§6 fija ahora el protocolo por hipótesis explícita; su traducción exacta a
P/Q sigue pendiente y no se obtiene automáticamente de (1)–(8).

## 6. Cierre H1c-0 / decisión explícita de modelo — 2026-09-24

### 6.1 Procedencia y alcance del cierre

La búsqueda local previa al cierre no encontró las etiquetas
`H1C0_UNDERSPECIFIED`, `CONTRACT_VALID`, `PHYSICAL_INTERPRETATION_OPEN`
o `MODEL_CHOICE_REQUIRED` en archivos del repositorio. Se registran aquí
como etapas de la auditoría y decisión de esta sesión, sin atribuirlas
retroactivamente a un commit anterior:

1. `H1C0_UNDERSPECIFIED`: el contrato H1 fijaba propagación y beta,
   pero no el lift operacional del protocolo plano.
2. `CONTRACT_VALID / PHYSICAL_INTERPRETATION_OPEN`: el candidato con
   preparación en el primer bloque y POVM refinado supera las identidades
   de normalización, positividad y recuperación plana, en auditoría interna.
3. `MODEL_CHOICE_REQUIRED`: el repositorio anterior no seleccionaba qué
   significado operacional dar a los bloques.
4. Decisión aceptada y congelada por el usuario:
   **`TWO_DISTINGUISHABLE_CHANNELS`**, como nueva hipótesis de modelo.

El contrato algebraico figura en la
[reconstrucción H1, §1](2026-09-20--h1-inhomogeneous-localization-reconstruction.md),
introducida en `bbc898be6c68cd8594449a7a52988c95b655dff4`. La
[bitácora H1, §§1–2](2026-09-20--h1-chat-research-log.md),
archivada en `3f8ae75f327aa06d23a2e5ee726a81866bcdfe33`, se identifica
como reconstrucción de chat y no certifica la convención gamma original.
Esos textos documentan las identidades del doblado; no derivan la
accesibilidad física de sus dos bloques. La falta de ese diccionario
tampoco demuestra que el doblado se introdujera exclusivamente como
dispositivo auxiliar.

El cierre H1c-0a se limita a la consistencia y definición del contrato
matemático siguiente. No certifica los prechecks de §§1–5, no constituye
revisión independiente y no cierra la localización H1c ni H1.

### 6.2 Espacio, propagación, preparación y encoder

El Hilbert operacional completo de una partícula es
\[
\mathcal H=
\ell^2(\mathbb Z^3)\otimes
\mathbb C^2_{\rm canal}\otimes\mathbb C^2_{\rm espín}.
\]
Para esta extensión candidata, los bloques de
\[
D=S\oplus S^{-1},\qquad
\beta=\sigma_x^{\rm canal}\otimes I_{\rm espín},\qquad
U_N=C_N(x)D,\quad C_N(x)=e^{-i\vartheta(x/N)\beta/N}
\]
se interpretan como canales internos distinguibles `+` y `-`. Se conserva
el perfil real y las hipótesis de regularidad del contrato H1 existente.
Beta intercambia los canales y la moneda los mezcla coherentemente.
La interpretación y la capacidad de Bob para resolver el canal son
**supuestos nuevos**, no consecuencias de esas identidades algebraicas.

Se heredan sin cambio el recurso, las regiones, los perfiles y las familias
de encoder/detector de [ir-corona.tex, §3](../papers/ir-corona/ir-corona.tex):
\[
\widehat\phi_N(p)=Z_N^{-1/2}g(Np)|\downarrow\rangle,
\quad \|\phi_N\|=1,\qquad
U_M=e^{i\pi F_N M/2},\qquad E=h_N\otimes M_B,
\quad 0\le E\le I.
\]
Aquí `M` recorre `I, sigma_1, sigma_2, sigma_3` y `M_B` recorre
`I, (I+sigma_j)/2`, como en el protocolo plano.
Con `Jx=(x,0)`, la preparación fijada es
\[
\Phi_N=J\phi_N=\binom{\phi_N}{0}.
\]
El bit `b=0` aplica la identidad; para `b=1` se usa un representante
\[
\mathcal U_M^{(1)}=U_M\oplus U_M,\qquad
\mathcal U_M^{(0)}=I_{\mathcal H}.
\]
La identidad
\[
(U_M\oplus U_M)J=(U_M\oplus I)J=JU_M
\]
registra equivalencia operacional en el instante del encoding bajo esta
preparación. No afirma identidad física de ambos encoders sobre otros
estados o protocolos. Ambos son unitarios y actúan como identidad fuera
de Alice. Para el mismo perfil real, `U_N` es unitario en el Hilbert físico.

Tras encoding y `N` pasos,
\[
\Psi_b=U_N^N\mathcal U_M^{(b)}\Phi_N
=\binom{\psi_b^+}{\psi_b^-},\qquad \|\Psi_b\|=1.
\]
La referencia no codificada de Bob procede de
`Psi_0=U_N^N Phi_N`; depende del walk doblado. No se reemplaza por la
referencia plana al activar la moneda.

### 6.3 POVM y respuesta física primaria

Bob resuelve la etiqueta de canal, por hipótesis de modelo. Su POVM es
\[
F_+=E\oplus0,\qquad F_-=0\oplus E,\qquad
F_\varnothing=I_4-(E\oplus E).
\]
En esta fórmula `I_4` abrevia la identidad completa
`I_{ell^2(Z^3)} tensor I_4`; no se restringe el espacio a la región Bob.
Como `0<=E<=I`, los tres efectos son positivos y suman
`I_{mathcal H}`. El resultado vacío incluye toda ausencia de detección.

Con la dependencia en `N,M,M_B` implícita, se fija como respuesta primaria
\[
\boxed{(L_+,L_-)},\qquad
L_\pm=
\langle\psi_1^\pm,E\psi_1^\pm\rangle
-\langle\psi_0^\pm,E\psi_0^\pm\rangle.
\]
Por normalización de las dos distribuciones de resultados,
\[
L_\varnothing=-L_+-L_-.
\]
Las dos lecturas binarias posibles son coarse-grainings explícitos:
\[
L_{\rm block}=L_+,\qquad L_{\rm incl}=L_++L_-.
\]
La primera cuenta `+` frente a `-` o ausencia de detección; la segunda
cuenta cualquiera de los dos canales frente a ausencia de detección.
Ninguna es el observable primario del contrato. Las respuestas se suman
con signo antes de tomar cualquier valor absoluto. No se seleccionará
posteriormente una lectura porque proporcione mejores potencias.

Los canales pueden mantener coherencia cuántica. Este POVM conserva la
información de sus tres resultados; no reconstruye todas las coherencias
del estado. Tampoco identifica los canales físicos `+/-` con los sectores
espectrales auxiliares `P/Q` de los prechecks.

### 6.4 Control plano exacto y límites

Para `vartheta=0`,
\[
C_N=I,\qquad U_N=D=S\oplus S^{-1},\qquad
U_N^N\binom{x}{0}=\binom{S^Nx}{0}.
\]
Por tanto para ambos bits y todos los pares heredados,
\[
\Psi_b=\binom{S^NU_M^{(b)}\phi_N}{0},\qquad
L_+=L_{\rm plano},\quad L_-=0,\quad
L_{\rm incl}=L_{\rm plano}.
\]
Esta recuperación exacta justifica inicialmente la extensión propuesta.
No se usa comportamiento asintótico favorable para elegirla.

Sigue **OPEN** la justificación de este doubled walk como representación
de un sistema físico concreto. Ningún resultado futuro de esta extensión
se presentará como universal para el protocolo plano original: quedará
condicionado a la hipótesis de dos canales distinguibles accesibles a Bob.

Estado conceptual congelado por instrucción del usuario:

```text
model choice: TWO_DISTINGUISHABLE_CHANNELS
H1c-0a mathematical doubled-walk contract: CLOSED
H1c-0b operational model choice: FIXED_BY_EXPLICIT_ASSUMPTION
physical realization/justification: OPEN
Volterra/asymptotic localization: PAUSED
primary observable: (L_+, L_-)
```

H1c y H1 permanecen matemáticamente abiertos. El cierre de contrato no
promueve ninguna cota preliminar. En particular, el `O(N^-6)` de §3
procede de multiplicar cotas absolutas auxiliares; no se ha aislado un
coeficiente `E_6`, ni se ha trasladado esa cota a cada respuesta firmada
del protocolo recién fijado.

## 7. Next session / 2026-09-25

Plan registrado; T1–T3 no se ejecutan en este cierre documental.

### T1 — Lift exacto del observable a P/Q

Partir del POVM de §6 y derivar, sin estimaciones de norma, las expresiones
exactas firmadas de `L_+` y `L_-` dentro de la descomposición P/Q existente.
Determinar si tiene sentido escribir
`L_± = L_{±,P} + L_{±,Q}`. No asumir esa aditividad: si el observable
cuadrático genera términos cruzados, escribir la expansión exacta completa,
incluyendo la referencia de Bob y ambos bits. No confundir canal físico con
proyector de Riesz ni cambiar la partición para obtener el resultado.

### T2 — Identificar qué significa realmente el actual O(N^-6)

Sólo tras cerrar T1, trazar la cota auxiliar
`||mathbb M_N||=O(N^-1)` de (8) y las cotas de extremo hasta cada
contribución firmada de `L_+` y `L_-`. Distinguir cota de norma, término
asintótico real, términos cruzados y posible cancelación firmada.
Comprobar el alcance de las cotas heredadas para la nueva referencia de Bob.
No llamar `E_6` a nada salvo que exista un coeficiente realmente aislado.

### T3 — Test de proyección

Sólo cuando T1 y T2 estén cerrados, comprobar separadamente qué contenido
del techo `O(N^-6)` sobrevive en `L_+`, en `L_-`, se cancela en alguno,
o se cancela únicamente en `L_++L_-`. Toda afirmación de cancelación
requiere contribuciones firmadas identificadas; una cota sola no basta.
Una cancelación en `L_incl` no permite cambiar el observable primario.

### STOP GATE

- Si T1 no produce un observable firmado exacto compatible con la
  descomposición existente, parar.
- Si T2 muestra que `N^-6` sólo es una cota gruesa sin coeficiente
  identificable, no buscar simetrías de un término inexistente.
- No introducir otra técnica analítica hasta cerrar T1–T3. La vía Volterra
  y la localización asintótica permanecen PAUSED durante este cierre.

## 8. Cadena documental archivada

Los siete informes de hoy pertenecen a esta cadena. Se conservan sus
argumentos previos con su alcance y falta de revisión independiente:

- [Conteo de parejas Dyson](2026-09-24--h1c-dyson-pair-audit.md).
- [Cota por inserción Dyson](2026-09-24--h1c-dyson-target-check.md).
- [Descomposición Dyson exacta](2026-09-24--h1c-exact-dyson-decomposition.md).
- [Masa de excursiones: kill-tests](2026-09-24--h1c-excursion-mass-kill-tests.md).
- [Resolvente de excursiones](2026-09-24--h1c-kernel-excursion-resolvent-audit.md).
- [Núcleo de memoria Volterra](2026-09-24--h1c-volterra-memory-kernel-precheck.md).
- Este informe de Schur y cierre operacional.

El cierre añade documentación y el resumen de `state/CURRENT_STATE.md`.
No ejecuta Volterra, nuevos fits, cálculos asintóticos, scripts científicos
ni el plan de mañana. El manuscrito plano y el código no se modifican.
```

### Contexto adjunto: reports/2026-09-24--h1c-exact-dyson-decomposition.md
```
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
```

### Contexto adjunto: reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md
```
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
```

### Contexto adjunto: /tmp/claude-1000/-home-ignac-qca-causal-cones/3c111a78-8f97-4e46-a059-6b4da58da570/scratchpad/state/CURRENT_STATE.md
```
# CURRENT_STATE

**Date:** 2026-09-24
**Status:** STANDARD WEYL/DIRAC EXACT GATE: PASS; strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS; point-(3) ceiling PROVED UNDER FROZEN CONTRACT, one independent review PASS; flat CJWW (5.15) operational IR-corona result CLOSED in its frozen class; **H1-only extension: TWO_DISTINGUISHABLE_CHANNELS frozen by explicit model assumption** (Sec. 9.6): H1c-0a CLOSED, H1c-0b FIXED_BY_EXPLICIT_ASSUMPTION, primary observable `(L_+, L_-)`; physical realization/justification OPEN; Volterra/asymptotic localization PAUSED. H1-SR proved under frozen beta contract, H1a/H1b proof written/unreviewed, layer absolute-mass bound PASS, G-insertion and final-Q-leakage PASS_IN_LOCAL_WINDOW retain their prior scope; H1c localization and H1 remain unproved/OPEN. Exploratory sequence: T1 `PASS` with independent adversarial review for the frozen model and admissible fixed W; T2 `TRACE_COMPLETE / BOUND_NOT_TRANSFERRED`; T3 `STOPPED_NO_SIGNED_TERM`. The quantitative bridge from the existing P/Q bounds to the ten physical endpoint pieces is not executed. No H1/H1c promotion. E0 and POWER_13/2_STABILITY remain OPEN_AT_STOP; E/AdS remains STOPPED_UNPROVEN. IR spectral-attribution front (Sec. 10.1): C1 PASS, C2a PASS for sigma2/I (one independent agent review), C2b PASS for sigma2/I (B4_PRIME_PASS separately; one independent agent review), C2c structural scope C2C_PASS for the frozen 16-pair scope, C3 conditioning C3_PASS for the frozen four-encoder `M_B=I` scope.

**Branch-local state.** This file is reconciled on
`research/b-infinity-post-s4-gate` only, so that it agrees with all evidence
merged on this branch. It is **not** a canonical promotion: `main` is
unchanged, and promotion requires a separate explicit decision.

**Repository:** `nacho09021973/qca-causal-cones`

**Evidence baseline:** `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.
Canonical promotion is recorded in
[`2026-09-14--standard-gate-promotion.md`](../reports/2026-09-14--standard-gate-promotion.md).
**Only point (3), the strict-cone ceiling, is chartered and authorized by
direct user instruction** (Sec. 7.2). The full C gate is not ratified.

**Correction (2026-09-14):** `B*` as a comparison against the one-step
inradius `r_in(C_micro)` is superseded by `B_infty^*`, a comparison against
the strict asymptotic isotropic speed `c_strict^iso`. See
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) and
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0. New baseline-specific certificate: for the
standard Pavia Weyl family in d=3, `C_infty^strict = C_micro` exactly, so
`c_strict^iso = r_in(C_micro) = 1/sqrt(3)`; see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
This baseline-specific certificate did not by itself close the gate; the
later s=4 counterexample completed it for the declared s=4 class.

**Integration (2026-09-15, branch-local):** an explicit irreducible `s=4`
family on the same `N_3`, with the same `D2` action, has
`C_infty^strict = C_micro` and `c_strict^iso = 1/sqrt(3)`, but
`c_0(a) = a/sqrt(3)` for every `0 < a < 1`. This is `COUNTEREXAMPLE_VERIFIED`
in the sense of the
[gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) Sec. 5 for the
declared `s=4` class (Sec. 4.1 below). It does not refute the standard Pavia
`s=2` certificate above. Evidence:
[analytic note](../theory/S4_STRICT_CONE_COUNTEREXAMPLE.md) and
[freeze record](../reports/2026-09-15--s4-strict-cone-counterexample-freeze.md)
(`1dae941`), [independent review](../reports/2026-09-15--s4-independent-review.md)
(`aeec462`), [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md)
(`f74018f`). **NOVELTY = OPEN.**

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.
- In the verified standard Dirac couplings they differ for every `0 < m < 1`.
  Name the extraction `c_H` or `c_{ω^2}`; do not use an unspecified finite-lattice
  `c_IR` as though those coefficients were interchangeable.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Canonical hypothesis status

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

### B_infty^* — strict asymptotic matching (supersedes B* / inradius matching)

Candidate:

`c_0 = c_strict^iso`, `c_strict^iso = min_{n̂} h_infty(n̂)`,

with `h_infty` the strict asymptotic support function of
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md) Sec. 6.
Interpretation: `c` would match the exact long-run isotropic propagation
speed of the same dynamics, not necessarily the inradius of the one-step
body `C_micro` — the two satisfy `c_strict^iso <= r_in(C_micro)` in general,
with equality only where separately certified (see the d=3 row below).

| Claim | Status and scope |
| --- | --- |
| A — IR universality | **OPEN** |
| B_max | **REJECTED** under isotropic containment in an anisotropic causal body, d >= 2 |
| B_full | **REJECTED / GEOMETRICALLY IMPOSSIBLE** for a nondegenerate isotropic ball equaling a finite lattice polytope, d >= 2 |
| Exact finite-mass B* | **REJECTED IN STANDARD DIRAC FAMILY**, for both specified extractions, every 0 < m < 1 (comparison against `r_in(C_micro)`, unaffected by the B_infty^* correction) |
| B*_0 (linear order, `c_0=r_in`) | **VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN** |
| B*_cont | **VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN** |
| B_infty^*, d=3 Pavia baseline (`C_infty^strict=C_micro`, full nonlinear order) | **CERTIFIED for the standard Weyl family `A+,B+,A-,B-`** (`s=2`): `c_0 = c_strict^iso = 1/sqrt(3)`; d=1,2 not checked; unaffected by the s=4 result |
| Strong B_infty^* (`c_0 = c_strict^iso` forced by locality, unitarity, homogeneity and D2 covariance at fixed `N_3`) | **REJECTED IN DECLARED s=4 CLASS** — explicit counterexample, Sec. 4.1; false for any class containing that family |
| B_infty^* in the published minimal `s=2` class (P17, including its Eq. (2)) | **NOT REFUTED by the s=4 result; rigidity OPEN as an in-repo claim.** Origin-node inradius matching there is a conditional application of P17's classification plus the standard certificate, not a new theorem. The strict-body certificate is recorded for `A+,B+,A-,B-`; its transfer across all of P17's equivalences is not separately checked |
| B_infty^* for `s=2` without P17 Eq. (2), or with an irreducible internal symmetry representation `R` for `s>2` | **OPEN** |
| Novelty of the s=4 family and its strict-support statement | **OPEN** — no equivalent found in eleven checked primary sources; not a novelty certificate |

The restricted statements are established for the declared cases below.
There is no general rigidity theorem, proof of A, or novelty claim.

### 4.1 Declared s=4 counterexample class

**Status: COUNTEREXAMPLE_VERIFIED for this class; independent review PASS;
NOVELTY = OPEN.**

| Item | Declaration |
| --- | --- |
| Geometry | d=3, `N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`, all eight modes active, no on-site coefficient, one complete update per time unit, phase `exp(-i k.h)` |
| Internal space | `s=4 = C^2_sigma (x) C^2_tau`; parameter `0<a<1`, `b=sqrt(1-a^2)` |
| Symbol | `A_a(k) = W exp(-i q_x Gamma_x) exp(-i q_y Gamma_y) exp(-i q_z Gamma_z)`, `q_i=k_i/sqrt(3)`, `W = I (x) exp(-i pi tau_z/4)` |
| Isotropy | D2 half-turns acting on `N_3`; `R_i = sigma_i (x) I_2` — two copies of the Pauli projective class, hence a **reducible** representation; full cubic symmetry not assumed |
| Irreducibility | Dynamics irreducible: scalar joint commutant of all eight Fourier coefficients |
| Gapless sector | `k=0`; two isolated rank-two clusters at quasienergies `+/-theta`, `theta=pi/4`; isotropic, untilted cones measured from each cluster's node |
| Result | `C_infty^strict = C_micro` exactly (all vertex traces nonzero, so no vertex coefficient is nilpotent); `c_strict^iso = 1/sqrt(3)`; `c_0(a) = a/sqrt(3)` |
| Coverage | One particular product ansatz, not a classification of four-component walks |

Scope limits, all retained:

- **Procedure.** The class table above was written at the freeze and review,
  after the construction, not before solving as charter Sec. 2 requires. This
  limits which classes the example speaks to; it does not affect the
  mathematical validity of the certified inequality.
- **Strict means exact support.** Vertex amplitudes may decay exponentially.
  No ballistic, essential or Lieb-Robinson front statement is made.
- **Floquet-shifted nodes.** `A(0) = W` is not a global phase.
- **Family identity only.** For `0<theta<pi/2`,
  `c_0^2 + 2 sin^2(Delta eps/2) g_ii(0) = 1/3`, where `Delta eps = 2 theta`
  and `g` is the projector quantum metric. It comes from the
  intra/inter-sector split `a^2 + b^2 = 1` of the involutions `Gamma_i`.
  Equating `1/3` with `(c_strict^iso)^2` additionally needs vertex survival,
  which is certified at `theta=pi/4`, or, for fixed `a`, on an open
  neighbourhood where all vertex traces remain nonzero. This is not a
  general QCA theorem.
- **Prior art.** Product-of-projector walks (MB18, BM25), four-component Weyl
  mixing (BB94), shifted Floquet Weyl nodes, adjustable continuum velocity,
  and involution block completion (AF16/17) are antecedents and must be
  attributed. Raynal's explicit s=4 Dirac family is excluded as an
  identification. The most useful open equivalence check is AF16/17's
  homogeneous paired-walk specialization.
- **Certificates.** `scripts/cert_Aa_s4_counterexample.py` and
  `scripts/review_Aa_s4_exact.py` both return PASS (SymPy 1.14.0, zero
  tolerance), and `scripts/verify_weyl_dirac_gate.py` still returns PASS
  (375 checks), on this branch.

## 5. Completed standard Weyl/Dirac exact gate

**Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**

Evidence is the committed
[contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
[analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
[verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
[permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
Source provenance and the published sign/dagger issues are recorded there.
The analytic proof establishes the open mass interval and continuum scaling;
the check count alone is not their justification or a formal proof certificate.

### Declared family and coordinates

The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
the minimal two-component blocks. The seven symbols are not seven independent
geometries: transposes/chiralities within a dimension share support, inradius
and linear speed. There are three dimension-specific geometries in this battery.

Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
complete update per time unit:

`N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,

`C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,

`r_in = 1/sqrt(d)`, `V_causal^max = 1`.

### Massless equality

For d=1,2,3 in this family, at the declared zero node,

`m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.

This is equality of the linear IR coefficient, not exact finite-momentum
relativistic dispersion or a theorem about every admissible symbol.

### Fixed nonzero lattice mass

For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
`0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
continuous from the identity near the massless zero node. Then

`cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,

`F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.

Exact finite-mass B* is refuted in the standard family under either extraction.
This result is no longer PRELIMINARY.

The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
expansions: `b = r_in^2 n (1-F)/(2m)` and
`c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
not a failure of the exact spectrum or an inconsistent calculation.

The endpoint m=1 is separate: actual hopping vanishes, active support becomes
`{0}`, and its inradius and spatial coefficients are zero. It is not covered
by the strict inequalities for `0 < m < 1`.

### Small-mass / continuum matching

For each standard coupling in d=1,2,3,

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
the equality of the limits is established analytically. The joint scaling
of momentum, dimensionless mass, neighbor length and time step is specified
in the report. Its continuum statement is local at fixed rescaled momentum
and mass, not a full propagator convergence theorem on arbitrary states.

## 6. Current scientific interpretation

**Superseded as the active line by Sec. 8 (2026-09-16).** This section records
the `B_infty^*` reading of the project and remains valid where proved, but its
scalar summaries must be read under the scope correction in Sec. 8.6.

The live idea is no longer:

`c = maximum microscopic speed`,

nor, unqualified, `c_massless = r_in(C_micro)`. The corrected comparison is
`B_infty^*`: `c_0 = c_strict^iso`, the exact strict asymptotic isotropic
speed of the same dynamics (Sec. 4). Its strong form is rejected in the
declared s=4 class (update below). `r_in(C_micro)` remains a provable
upper bound (`c_strict^iso <= r_in(C_micro)`), and is known to be exactly
attained — `c_strict^iso = r_in(C_micro)` — for the standard Pavia Weyl
family in d=3, by an explicit vertex non-nilpotency certificate, not merely
by the linear-order Taylor coefficient.

**Update (2026-09-15, branch-local).** Locality, unitarity, homogeneity and
D2 covariance at fixed `N_3` do **not** force `c_0 = c_strict^iso` once the
internal dimension is enlarged. The s=4 family (Sec. 4.1) keeps the whole
strict body, `C_infty^strict = C_micro`, while its Weyl slope varies
continuously below `1/sqrt(3)`. The strict causal body alone therefore does
not fix the Weyl speed. In this family the missing speed is exactly
accounted for by the inter-sector part of the involutions (the family
identity in Sec. 4.1). Whether that is a structural principle or a feature of
this ansatz is **OPEN**.

What remains unknown is which additional hypotheses restore matching: `s=2`
minimality with or without P17 Eq. (2), irreducibility of the internal
symmetry representation, a whole-symbol common cone, or something else.
Whether `c_strict^iso` saturates `r_in(C_micro)` for every admissible symbol
(saturation, charter Sec. 0(ii)) is a separate question and also remains
open.

At finite mass the two natural extraction procedures differ exactly. A common
relativistic coefficient is recovered in the specified continuum limit.
Additional equivalent representatives cannot resolve the open generality issue;
any successor gate must examine structural freedom under fixed causal geometry
and discrete isotropy.

**Update (2026-09-17, branch-local, frozen class of Sec. 8 only).**
`B_infty^*` matching in Sec. 4 is unchanged. What is now closed is the
**operational IR question** on the preregistered CJWW (5.15) protocol of
Secs. 8.16–8.20, not the matching hypothesis. In that class there is an
IR-controlled operational response outside the emergent cone, and it is
not a mere UV-propagator artefact:

`c_IR < v_micro` (already geometric for (5.15)) and
`IR probe → δ_B(N) ≠ 0` for large `N`, with
`δ_{M,M_B}(N) ∼ |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N}`
on the twelve Pauli pairs (Sec. 8.20). The signal is
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. This is theoretical step 3
of the physical line, closed inside the preregistered class. It is not
`D_B > 0` for every QCA, not a claim about nature, and not a further
signalling calculation. The authorized next front is Sec. 8.21.

## 7. GATE STATUS — only point (3) authorized by the user

**MASSLESS INRADIUS RIGIDITY GATE — COUNTEREXAMPLE_VERIFIED IN DECLARED s=4
CLASS (branch-local); s=2 and irreducible-R classes OPEN; point (3) ceiling
investigation separately chartered by direct user instruction.**
(Charter name kept for continuity; its comparison target is corrected, see
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0.) Where the charter or
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) still describe the
gate as having no counterexample, this section overrides them
(`PROJECT_INSTRUCTIONS.md` Sec. 2).

### 7.1 Superseded operative plan

The 2026-09-14 deliberation
([`debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md`](../debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md))
predates the s=4 result. It recommended freezing an `s=2` contract on `N_3`,
filtering candidates by non-nilpotent vertices, and escalating to `s>2` only
after exhausting that class. That order was not followed, and its
"rigidity vs saturation" framing cannot continue as written. It is kept as
historical decision material, not as a current plan. Its open point about
whether P17 Eq. (2) is derivable from the charter's identities still matters
for the `s=2` question.

### 7.2 Point (3) — direct user authorization, not a ratification

**Authorization (2026-09-16):** after the incomplete ratification, the user
explicitly instructed: "pues adelante, punto (3)". Accordingly,
`STRICT_CONE_CEILING_N3 = AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` under the
[frozen point-(3) contract](../theory/STRICT_CONE_CEILING_N3_GATE.md).
Its sole target is `c_0 <= c_strict^iso` in all directions, including
degenerate Floquet nodes and eigenvalue collisions in U^n. The contract
was frozen at `4135625` with initial scientific status **OPEN**. No L1,
defect-metric or other C step is authorized by this instruction.

**Point-(3) result (2026-09-16):**
`PROOF_COMPLETE_ONE_INDEPENDENT_ADVERSARIAL_REVIEW_PASS`;
`THEOREM_STATUS = PROVED_UNDER_FROZEN_CONTRACT`. The
[analytic report](../reports/2026-09-16--point-3-strict-cone-ceiling.md)
supplies a matrix-polynomial boundary bound, compression to the original
eigenspace, a direct directional-slope argument, and the exact support
limit. The author's assessment is `PASS_ANALYTIC` under the frozen
contract. The [independent adversarial review](../informe_adversarial_punto_3.md)
at `bd44122`, reviewing `db083af` against `4135625`, records
`ACCEPT_AS_WRITTEN`, with no mandatory repairs. One independent review is
complete; it is not a five-member ratification. The follow-up incorporates
its recommended sign control and expository clarifications without changing
the frozen quantifiers. The bound is proved for the admitted cones and the
exact support of the full symbol on N3, including degenerate Floquet nodes
and collisions of eigenvalues after taking powers. It does not establish a
sector-intrinsic or ballistic bound, or an extension to incommensurable
displacement sets. No numerical search or scientific script was run.
The full C gate is neither ratified nor closed;
L1 remains a manual candidate and the defect identity remains family-only.
The s=4 example refutes equality and is consistent with this ceiling.
**NOVELTY = OPEN.**

The 2026-09-16 ratification attempt is `ABORTED_OR_INCOMPLETE`: Gemini was
absent at launch; the process was interrupted without a final verdict. Three
first-round turns completed — ASTRA `PREFER_A`, CLAUDE OPUS `RATIFY_C`
conditioned on its own amendment (i), CIRO `RATIFY_C` — and ABNER's turn was
sent but never returned. That is neither a closed round nor five-member
ratification, so the status above is unchanged. The partial acta is archived
at [`2026-09-16--ratificacion-gate-completitud-axial-n3.md`](../debates/2026-09-16--ratificacion-gate-completitud-axial-n3.md);
the raw session log stays local and unversioned.

**Candidate from a degraded debate (2026-09-15):**
`GATE_COMPLETITUD_AXIAL_N3 = CANDIDATE_FROM_DEGRADED_DEBATE`, **not
authorized.** In the
[deliberation](../debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.md),
four members proposed `AUTHORIZE_C`. The tool classified the run as
`DEGRADED_NO_CONSENSUS`: ASTRA failed two turns (Codex usage limit) and was
excluded. ASTRA's recorded preference was A, and its objection that C reaches
`c_strict^iso` only through the still unproven bound `c_0 <= c_strict^iso`
was left unanswered. The earlier requirement of five-member ratification
has not been met. The later direct user instruction above authorizes only
point (3) under a separate contract; it does not authorize the full C gate
or convert either incomplete debate into consensus.

Research directions (only the point-(3) ceiling is now frozen):

1. **Surviving bounds.** Which inequalities between `c_0`, `c_strict^iso`
   and `r_in(C_micro)` hold for every admissible symbol? Currently
   `c_strict^iso <= r_in(C_micro)` is established. `c_IR <= r_in(C_micro)`
   is established only under the isotropic-containment premise of Sec. 3.3.
   `c_0 <= c_strict^iso` is proved under the frozen point-(3) assumptions,
   with one independent adversarial review PASS. Thus every admitted cone
   satisfies `0 < c_0 <= c_strict^iso <= 1/sqrt(3)`. Equality and microscopic
   saturation are not consequences of this ceiling.
2. **Restoring hypotheses.** Which explicitly stated extra assumptions (for
   example `s=2` minimality with or without Eq. (2), or an irreducible `R`)
   give `c_0 = c_strict^iso` for a whole declared class?
3. **Intra/inter rule.** Does the s=4 family identity reflect a general
   structure that accounts for the missing speed, or is it specific to this
   ansatz?

Every class must keep the quantifiers of charter Sec. 2 and be declared
**before** solving.

### 7.3 Original gate question (answered for the declared s=4 class)

The original question was whether another admissible massless symbol can have
`0 < c_0 < c_strict^iso` for its own strict asymptotic body, while preserving
the same `N`, `C_micro`, embedding, unitarity, homogeneity and discrete
isotropy as its selected standard baseline. A candidate whose `c_0 < r_in(C_micro)`
only because its own strict body already falls short of `r_in(C_micro)` is not
this counterexample; see the charter's Sec. 0 for the (i)/(ii) split.

**Erratum (2026-09-15).** Earlier wording here attributed such a shortfall to
a nilpotent one-step coefficient. What is established is only this: a
saturation failure `c_strict^iso < r_in(C_micro)` requires at least one
nilpotent vertex coefficient (contrapositive of the vertex lemma). The
converse is not established. A nilpotent vertex removes the exact ray `n.h`
from `S_n`, but it does not by itself determine `c_strict^iso`, which must be
computed. See the charter's erratum.

The [gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) requires the
internal dimension, isotropy group/action and representation, node/sector,
and any irreducibility assumptions to be explicit before solving. Do not
silently introduce minimality or weaken the symmetry when interpreting a result.

- One exact admissible counterexample refutes B_infty^* for a class containing
  it (realized for the declared s=4 class, Sec. 4.1).
- A rigidity claim requires an exhaustive analytic argument for an explicitly
  quantified class; failure to find a deformation is not such an argument.
- The absence of a continuous deformation alone does not exclude disconnected
  admissible symbols. A restricted proof leaves wider generality open.
- Prior-art classification assumptions must be checked before any novelty claim.

### Stop rule

Until a successor gate is chartered and closed:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO anisotropic-QCA detour**;
- **NO change of support, embedding, time normalization or discrete isotropy
  within a declared rigidity comparison**;
- **NO novelty claim for B*, B_infty^* or the s=4 family (NOVELTY = OPEN)**;
- **NO use of a scalar `v_max` without definition**;
- **NO promotion of the s=4 family identity to a general QCA law**;
- **NO reading of `c_strict^iso`, `r_in(C_micro)` or `S_min` as "the microscopic
  speed of the substrate"** (Sec. 8.6);
- **NO new novelty audit, Bernstein-rigidity, paraunitary-classification or
  d=3-theorem line** under the Sec. 8.7 scope decision;
- **NO directional/anisotropic `I(v)` computation** (Sec. 8.8, NOT_AUTHORIZED);
- **NO operational-invisibility or no-signalling claim** from a rate function
  (Sec. 8.8); that question requires its own charter.

A certified falsification within the frozen admissible class is a successful
gate outcome. The s=4 counterexample is such an outcome for its declared
class only. This branch-local reconciliation does not promote anything to
`main`. The only later successor authorization is the point-(3) contract
in Sec. 7.2, by direct user instruction.

## 8. Directional causal saturation — canonical physical interpretation (2026-09-16)

**Evidence commit:** `2494192`.
[Report](../reports/2026-09-16--directional-causal-saturation.md),
[verifier](../scripts/verify_directional_saturation.py) (15/15, fail-closed,
fourteen exact).

The active physical question is: **does `c_IR` coincide with the microscopic
causal boundary of the discrete substrate?** The canonical answer is
**direction-dependent; in general, no.**

### 8.1 Three objects, never identified

For the two 3D finite-range walks of CJWW `sources/2408.02108v1.pdf`,
Eqs. (5.12) and (5.15):

`B(c_IR) ⊆ Γ ⊆ C_micro`,

- `B(c_IR)`: the emergent isotropic IR light cone;
- `Γ`: the ballistic / group-velocity propagation body;
- `C_micro = conv F`: the strict microscopic causal body of the finite step set `F`.

`Γ ⊆ C_micro` is general (CJWW Lemma 4.1: the rate function is `+∞` outside
`conv F`). `B(c_IR) ⊆ Γ` is **not** general and is asserted here only for these
two walks; CJWW Sec. 5.3 exhibits a non-convex `Γ`, so no convexity of `Γ` may
be assumed.

### 8.2 The canonical saturation function

For both walks `C_micro = [-1,1]^3`, hence for `||n̂||_2 = 1`

`v_sub(n̂) := h_{C_micro}(n̂) = ||n̂||_1`,

and, in the normalization `c_IR = 1`, the canonical directional saturation
function is the **support-function ratio**

`S(n̂) := h_{B(c_IR)}(n̂) / h_{C_micro}(n̂) = 1/||n̂||_1`.

`S(n̂) = 1` only for the six axial directions `n̂ = ±e_i`; `S(n̂) < 1` for every
non-axial direction, with `S_min = S((1,1,1)/sqrt(3)) = 1/sqrt(3)`.

`S_min` is a **descriptive scalar summary only**. The full directional function
`S(·)` is the canonical object. No scalar separates the two walks: `c_IR/r_in`
is `1` and `S_min` is `1/sqrt(3)` for both; their difference lives in `Γ`.

### 8.3 Walk (5.12)

`B(1) ⊊ Γ_1 ⊊ [-1,1]^3`, with `sup|∇ω| = sqrt(3/2) > c_IR`, attained exactly at
`p = (-π/4,-π/4,-π/4)`. This walk contains finite-momentum ballistic modes
faster than the emergent IR light speed while remaining inside `C_micro`.
`Γ_1 ⊆` tricylinder is exact (SOS identity); the reverse inclusion is numerical.

### 8.4 Walk (5.15) — the clean counterexample

`Γ_2 = B(1) ⊊ [-1,1]^3`, with `sup|∇ω| = c_IR = 1`.

This refutes the identification

`sup|v_g| = c_IR  ⟹  IR light cone = microscopic causal boundary`.

Even when **all ballistic propagation respects `c_IR`**, the substrate permits
causal propagation outside the relativistic ball in non-axial directions.

**Evidence tags, not to be merged.** `sup|∇ω| = c_IR = 1` and
`Γ_2 ⊆ B(1)` are **ESTABLISHED (exact SOS certificate**
`(1-f²) - |∇f|² = s₂²s₃² + s₁²s₂²c₃² + s₁²c₂²s₃²`**)**, and `∂B(1) ⊆ Γ_2` is
exact from the conical point. That `Γ_2` also fills the open ball is
**SUPPORTED (numerical)** only. The counterexample does **not** depend on that
last half: it needs only `sup|v_g| = c_IR`, which is exact.

### 8.5 The gap is not a one-step artefact

At the eight vertex rays a single lattice path contributes, so
`(W^n)_{nσ} = (W_σ)^n`. Each `W_σ` has rank 1 with nonzero trace, hence
`(W_σ)^n = tr(W_σ)^{n-1} W_σ ≠ 0` **for every `n ≥ 1`** (exact). Therefore
`h_infty = h_{C_micro} = ||·||_1` exactly, and the distinction between `Γ` and
`C_micro` is not an artefact of a one-step support bound.

Between `Γ` and `C_micro`, propagation is non-ballistic and may be exponentially
suppressed; it is **not generically causally forbidden**. **No claim is made
that every point of this intermediate region has nonzero amplitude** — what is
proved is the statement about the vertex rays.

### 8.6 Scope correction to earlier scalar summaries

`c_strict^iso` and `r_in(C_micro)` remain mathematically valid summaries where
previously proved (Secs. 4, 6, 7), but **must not be interpreted as "the
microscopic speed of the substrate."** The microscopic causal boundary is
anisotropic and is represented by `C_micro`, equivalently by `h_{C_micro}(n̂)`.

Under (i) finite `F`, (ii) `d ≥ 2` and (iii) an isotropic IR cone, exact
equality `B(c_IR) = C_micro` is impossible, because `C_micro` is a finite
polytope and the IR body a Euclidean ball. This restates `B_full` (Sec. 3.3)
with its hypotheses made explicit; relaxing (i), (ii) or (iii) leaves it open.

### 8.7 Scope decision

The physical relation **emergent relativistic cone vs microscopic causal
body** remains the line. As of 2026-09-17, inside the frozen IR class of
Secs. 8.16–8.20, theoretical step 3 of that line is **closed**: the gap
is not only geometric (`c_IR < v_micro`) but operational
(`IR probe → δ_B(N) ≠ 0` for large `N`, nonperturbatively suppressed;
Sec. 8.20). No further signalling gate is authorized.

The live front is whether that structure can correspond to something in
nature (Sec. 8.21, `NOT_EXECUTED`), not another calculation of `C` and
not yet a laboratory implementation of the walk (fork 4A, identified,
not chartered).

**Not authorized by this result:** further search for mathematical novelty,
Bernstein rigidity, paraunitary classification, or a new dimension-3 theorem.

The previous novelty / Gate-C material is retained as historical project state
and is **not an active prerequisite** for the physical line. Sec. 7 is unchanged
and still governs anything done under the point-(3) contract.

### 8.8 LDP_RADIAL_INTERPRETATION — PASSED, subline CLOSED (2026-09-16)

**Status: `DOCUMENT_EXISTING_RESULT` — PASSED. This subline is CLOSED.**
Contract: [`OPERATIONAL_INVISIBILITY_GATE.md`](../theory/OPERATIONAL_INVISIBILITY_GATE.md).
A first freeze at `a9e611a` chartered the *directional* variant; it was narrowed
by user instruction before any solving and is **SUPERSEDED, UNSOLVED** — nothing
may be cited from it.

For walk (5.15), CJWW's own radial rate function Eq. (5.21),
`R̃(ℓ) = 2 arccosh(cosh(ℓ/2√3)³)`, has exactly the two slopes

`R̃'(0) = 1 = c_IR`   and   `R̃'(∞) = √3 = max_n̂ v_sub(n̂) = v_sub(body diagonal)`,

so by Legendre duality `Ĩ(r) = 0` for `r ≤ 1`, `0 < Ĩ(r) < ∞` for `1 < r < √3`,
and `Ĩ(r) = ∞` for `r > √3`, reproducing CJWW's control value `Ĩ(1.1) ≈ 0.104`.
Three regimes, with boundaries at precisely the two numbers Sec. 8 canonizes:

**ballistic/emergent | causal but exponentially suppressed | causally forbidden**

**ESTABLISHED (exact).** The *value* of (5.21) at CJWW's stated maximizer is
exact; the *location* of that maximizer is their numerical finding, not ours.

**Declared limitations, not to be dropped.**
- `Ĩ` is radial and demonstrably coarse. Since `v_sub(ê_i) = c_IR`, a velocity
  `r ê_i` with `r > 1` is already outside `C_micro`, where the amplitude is
  **exactly zero**, not suppressed. The finite rate `Ĩ` reports for `1 < r < √3`
  is therefore carried by non-axial directions only. The angular structure of
  `I(x)` is **not resolved**.
- Upper bound only; CJWW prove no lower bound.
- It bounds the position distribution of one particle, nothing else.

**Non-implication, explicit.** This does **not** yield an operational-invisibility
or no-signalling theorem. At QCA level an exponentially small tail still lies
inside the exact causal support, so "operationally invisible" may not be
asserted. That question needs resources, distinguishability or channel capacity
defined first, changes problem class, and merits an independent charter.

**NOT_AUTHORIZED:** anisotropic/directional `I(v)`; probability vs signalling.

(For the canonical conclusion of Sec. 8 as a whole, see Sec. 8.9.)

### 8.9 Canonical conclusion — stated at the right logical level

Earlier wording here read "`c_IR` **can** be the boundary of typical macroscopic
propagation without coinciding with the microscopic causal boundary". That is
modal, and too weak: this is not a possibility claim but an **explicit
counterexample**. Corrected, and canonical:

**(i) Existence — PROVED (exact).**

> There exists at least one local, unitary, finite-range model in 3D — the
> one-particle translation-invariant walk of CJWW Eq. (5.15) on `Z^3`, internal
> space `C^2`, jump length 1 — in which **all** ballistic propagation satisfies
> `|v_g| ≤ c_IR`, while the microscopic causal region is **strictly larger**
> than the emergent relativistic cone:
>
> `sup|v_g| = c_IR`  **and**  `B(c_IR) ⊊ C_micro`.

Both halves are exact: `sup|v_g| = c_IR = 1` by the SOS certificate of Sec. 8.4,
and `B(c_IR) ⊊ C_micro = [-1,1]^3` with `v_sub(n̂) = ||n̂||_1` reaching `√3 c_IR`
on the body diagonals, certified at every vertex ray for every `n` (Sec. 8.5),
hence not a one-step artefact. This statement does **not** rest on the
numerically supported half of `Γ_2 = B(1)`.

**(ii) Logical consequence — PROVED in the class studied.**

> `c_IR = sup|v_g|  ⇏  B(c_IR) = C_micro`.
>
> Equivalently: the equality "`c_IR` = microscopic causal limit" is **not a
> necessary consequence of relativistic emergence**.

**(iii) Explicitly NOT established — UNKNOWN.**

> `c_universe < ` the fundamental causal limit of our universe.

No evidence is offered here in either direction. This project makes **no claim
about our universe**; asserting (iii) from (i)-(ii) would be a category error,
since (i) is an existence result inside a declared model class.

### 8.10 SUBSTRATE_CONE_OBSERVABILITY — PASSED, gate CLOSED (2026-09-16)

Contract [`SUBSTRATE_CONE_OBSERVABILITY_GATE.md`](../theory/SUBSTRATE_CONE_OBSERVABILITY_GATE.md)
frozen at `d86b018` before solving;
[outcome](../reports/2026-09-16--substrate-cone-observability.md). This lifts
the Sec. 8.8 `NOT_AUTHORIZED` for the signalling question only.

The question was operational: for `ct < L < v_sub(n̂)t`, is `D = 0` or `D > 0`?
It is **undefined** for the one-particle walk, so the gate declared a
free-fermion (CAR) lift. On the one-particle sector `α_t(n_x) = W^t P_x W^{t†}`,
so `[α_t(n_x), n_y]` has `(y,y')` block `(W^t)_{y,x}((W^t)_{y',x})†` and is
nonzero exactly when the single-particle kernel is. **The operational causal
structure of the lift is the strict support of `W^t`** — the object already
certified in Sec. 8.5.

**Answer: `D > 0`, exponentially small, strictly off-axis.** Exactly zero for
`L > v_sub(n̂)t` (H4); nonzero `∝ 4^{-t}` at the vertex rays for
`ct < L < v_sub(n̂)t` (H2); **exactly zero in the six axial directions** for
every `L > ct`, since `v_sub(ê_i) = c` (H3). At `t = 3`, 108 of the 148
populated sites lie strictly outside `B(c)t`, all inside `C_micro t`, none
axial. **ESTABLISHED (exact, Gaussian-integer kernels).**

This is the signature sought: fundamental causality outside the light cone with
no superluminal ballistic propagation, carrying the angular fingerprint
`v_sub(n̂) = ‖n̂‖₁ c`.

**Limits.** Statements are about the lift, not the one-particle walk. A nonzero
commutator means *there exists* an intervention and a state with `D > 0`; no
specific protocol's `D` and no channel capacity were computed. How the
suppression varies across `C_micro \ B(c)` is the anisotropic `I(v)` question,
still `NOT_AUTHORIZED`. No claim about our universe: Sec. 8.9(iii) stands at
UNKNOWN, and a wider cone fully decoupled from accessible observables would be
invisible to any experiment, so no null result can establish exact coincidence.
No experimental or LIV constraint survey is authorized.

### 8.11 EMPIRICAL_SUBSTRATE_CONE_SURVEY — COMPLETE (2026-09-16)

Contract [`EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md`](../theory/EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md)
frozen at `416dde1`;
[outcome](../reports/2026-09-16--empirical-substrate-cone-survey.md).

**Declared premise (computed before surveying).** With `t` in lattice steps, a
Planck-scale substrate puts this model's own effect at `10^(-8.4e41)` over one
second, against finest-ever bounds of `10^-20` to `10^-30`. The model's effect is
**unobservable in principle**. The survey is therefore model-independent. The
geometric window is by contrast not small: it reaches `√3 ct`, 73% beyond the
light cone.

**Verdict, in three levels.**

| | |
| --- | --- |
| Scalar no-signalling | experimentally tested, to finite precision |
| Directional causal tail of Sec. 8.10 | no specific localized operational test |
| Exact equality `C_fundamental = B(c)` | **not established** by null results |

In contract categories: `DIRECT_CONSTRAINTS_FOUND` for the scalar variable,
`NO_CURRENT_OPERATIONAL_TEST` for the directional structure.

**Missing coupling map — the real obstacle.** `[A(t),B] ≠ 0` gives `∃` a state
and intervention with `D > 0`; it does **not** give that a standard Bell-test
protocol is that intervention. Converting a bound on Bell marginals into a
quantitative bound on the tail needs a coupling/protocol map — which observable
realizes `A`, which realizes `B`, which preparation exploits the commutator.
None exists. The scalar bound therefore constrains the right *kind* of variable
without being convertible into a number about our `D`.

**Withdrawn.** An earlier phrasing used Adenier–Khrennikov to fix the empirical
level at "percent-to-permille". That was an overreach: it is a contested
reanalysis of one dataset, not a universal bound nor a calibrated interval for
`D`. No numerical empirical level is claimed. Likewise "essentially untested" is
replaced by the exact-equality statement above.

**Category error recorded, the survey's main result.** Salart 2008 (`v > 10⁴ c`)
and Bancal 2012 (finite-speed influence ⟹ superluminal signalling) constrain
models where the superluminal influence *explains* the quantum correlations. The
tail of Sec. 8.10 is non-explanatory, so those bounds do **not** apply to it;
using them to "exclude" it would be a category error. LIV/dispersion/threshold
limits are `INDIRECT_ONLY` by contract Sec. 2.1, since Sec. 8 proves
`sup|v_g| = c` is compatible with influence outside `B(c)`. Lieb–Robinson
experiments (Cheneau 2012 and successors) **observe** this structure in
engineered lattices: realizability, not a constraint on nature.

**Consequence, and the firm epistemological point.** No finite sequence of null
results can prove `D = 0` exactly; it can only yield ever smaller upper bounds.
A reproducible positive result outside `B(c)` could falsify the identification
of `c` with the fundamental causal boundary. Sec. 8.9(iii) stands at UNKNOWN.

**Next step if the line continues (not opened).** Not a further theoretical
front, and not a generic FTL search: design the experiment that **maximizes `D`**
for a Sec. 8.10-type tail — which two local operations, which spacelike
separation, which remote observable optimally exploit an exponentially small,
anisotropic causal tail. Only afterwards does it make sense to ask whether an
existing experiment already did this accidentally, and by how much it falls
short. This is the coupling map above, and it is **not chartered**.

### 8.12 COUPLING_MAP_OPTIMAL_D — PARTIAL; exact signalling witness CLOSED (2026-09-16)

Contract [`COUPLING_MAP_GATE.md`](../theory/COUPLING_MAP_GATE.md) frozen at
`0f7628d`: frozen Sections 0–6 unchanged, outcome corrected;
[report](../reports/2026-09-16--coupling-map.md).

**Correction authorized by the user, 2026-09-16.** The former conditional H1
confirmation, universal linear/quadratic scaling and claimed restricted
optimal-D upper bound are withdrawn. The code computed an occupation
witness, not full trace-distance optimization. Four finite times cannot
establish asymptotic scaling; moreover `t = 5` exceeded the frozen `{2,3,4}`.
The historical ratios remain descriptive only. H1 is **OPEN**; H2 establishes
preparation dependence for the specified protocol, not necessity of coherence
for all admissible interventions. **H3 and H4 remain NOT REACHED**.

**Finite existence task: EXISTENCE_WITNESS_PROVED / INDEPENDENTLY_REVIEWED.** The user's
subsequent instruction chartered closure as a theorem/witness, not further
optimization or an experimental study. See
[`COUPLING_MAP_SIGNALING_WITNESS.md`](../theory/COUPLING_MAP_SIGNALING_WITNESS.md).
At `t = 2`, Alice at `0`, Bob at `y = (2,2,2)`, prepare
`(|0,down> + |y,down>)/sqrt(2)` before Alice chooses between `I` and
`exp(i pi n_0)`. Bob measures the even non-vacuum projection at his site.
The exact probabilities are

`p_0 = 121/512`, `p_1 = 169/512`, `Delta p_B = 3/32 > 0`, hence **`D >= 3/32`**.

The theorem fixes the existing CAR/Heisenberg convention, the state,
intervention, measurement and spacetime point. The exact kernel is nonzero
there: Bob is outside the emergent ball and **on the microscopic boundary**.
This proves membership in the exact causal support, not strict interior
membership. Each local site has two modes; the original `N = M = 1`
optimization is not closed. The
[verifier](../scripts/verify_signaling_witness.py) passes **17/17 exact checks**.
The [independent review](../reports/2026-09-16--signaling-witness-independent-review.md)
returns **PASS on the four requested points, no mandatory repairs**: analytic
probabilities, code correspondence, causal location, and the convention
`D = (1/2)||rho_1-rho_0||_1`. It records hashes of the unchanged reviewed
theorem and both scripts. This is one separate agent's independent review,
not external human review, consensus, or a full PASS of the optimal-D gate.

**Claim ceiling, branch-local:**

> In this free-fermion lift, given a state prepared with coherence between
> Alice and Bob's own site before Alice's choice, that local choice changes
> a measurement probability accessible
> to Bob outside the emergent relativistic cone and within the exact
> microscopic causal support. The choices are distinguishable in principle.
> Preparation of this operational channel from resources initially localized
> around Alice, Bob's optimal measurement, a globally optimal protocol and
> experimental feasibility are not established.

**Superseded clause, 2026-09-16.** The requirement of a resource already
distributed before Alice acts is no longer open: Sec. 8.13 exhibits a
*different* channel, in the same model, driven from a particle initially at
Alice alone. That successor does **not** supply a preparation protocol for
*this* channel, whose theorem, review and ceiling above are unchanged.

**Controls and limits.** For an Alice-localized particle the phase gate gives
only a global phase, hence exactly zero signal. Removing spatial coherence
also removes this protocol's signal. At the axial control the exact zero
kernel excludes Alice from the evolved Bob algebra, hence forbids signalling
for any initial state under even local Alice unitaries. By contrast, a zero
occupation witness alone never certifies `D = 0`.

The second coherent arm in this construction is **at Bob's initial site**;
the earlier hint excluding Bob from the resource is withdrawn. No Bell
protocol has been modelled. The finite interference term involves both
`K_0y` and `K_yy` with their internal alignment, not a universal asymptotic
law in one kernel. The empirical transfer of Sec. 8.11 remains unresolved;
the experimental problem is not opened. No claim about our universe follows.

**The original question, split.**

| Question | Answer |
| --- | --- |
| Theoretical: must `c` coincide with the substrate's causal limit? | **No** — (ii), proved |
| Physical: does it coincide in our universe? | **Unknown** — (iii) |

### 8.13 ALICE_LOCAL_PREPARATION_SIGNALING_WITNESS_PROVED / INDEPENDENTLY_REVIEWED (2026-09-16)

Successor to Sec. 8.12, chartered by direct user instruction as an
**existence question only**: does the signalling channel require a resource
that is already spatially distributed before Alice acts? **It does not.**
See [`ALICE_LOCAL_PREPARATION_WITNESS.md`](../theory/ALICE_LOCAL_PREPARATION_WITNESS.md)
and the [construction report](../reports/2026-09-16--alice-local-preparation.md).

Same unchanged CAR lift of CJWW (5.15), same conventions. At `T = 0` the
resource is exactly one particle, `|0,down>`, with every other mode vacant.
Between `T = 0` and `T = 2` **only the declared free dynamics acts**, equally
for both messages: the prepared state is `chi = S^2|0,down>`, given in closed
form by Cayley-Hamilton (`S^2 = 2fS - I`, `f = cos p1 cos p2 cos p3`), with
38 populated sites, `||chi|| = 1`, `chi(0) = -3 down/4` and
`||P chi||^2 = 9/16`, `||Q chi||^2 = 7/16`. Alice encodes at `A = (2,0)`
with `I` or `exp(i pi n_0)`; Bob measures the even non-vacuum projection at
`B = (3,(1,1,1))`. The exact probabilities are

`p_0 = 49/1024`, `p_1 = 25/1024`, `Delta p_B = 3/128 > 0`, hence **`D >= 3/128`**.

**Causal origin — the load-bearing step.** The bit is exogenous at `T = 2`.
Both conditional histories are *identical operators on the whole Fock space*
for `T = 0, 1, 2^-`, so the mutual information between the bit and any
pre-choice observable is exactly zero and no earlier encoding exists. Bob's
own site is **exactly vacant** at the encoding event (`chi(1,1,1) = 0`).
Comparing cones from `T = 2` is therefore the appropriate operational
reference for communication. From the encoding event,
`|y_B| = sqrt(3) > c_IR Delta T = 1` while `||y_B||_inf = 1` and
`K_1(0,y_B) = diag(0,1/4) != 0`: Bob is outside the emergent cone and on the
**boundary of the exact microscopic causal support**. **No microscopic
causality bound of the model is violated.** It is explicitly *not* claimed
that Bob is outside the emergent cone of the initial event: from `T = 0`,
`sqrt(3) < 3`.

**Claim ceiling, branch-local:**

> A particle initially localized at Alice alone suffices. The ordinary
> microscopic dynamics generates the required spatial coherence before the
> message is chosen. A later local choice by Alice then changes a Bob
> statistic one step afterwards, with Bob outside the emergent causal cone
> of **that encoding event** and within the microscopic causal support.
> This is not a violation of the model's microcausality. Optimality,
> minimal preparation time, experimental feasibility, asymptotics, capacity
> and any claim about our universe are **not** established.

**Evidence.** `verify_directional_saturation.py --local-preparation-only`
passes **21/21 exact checks**; the frozen witness verifier still passes
17/17 and the default suite 27/27, unchanged. The
[independent review](../reports/2026-09-16--alice-local-preparation-independent-review.md)
returns **PASS, no mandatory repairs**, and explicitly covers the item most
exposed to adversarial attack: the closed-form derivation of `S^2|0,down>`
and the identity of the two pre-choice histories. It reconstructs the
prepared state from a separately transcribed symbol, records SHA256 hashes of
every reviewed input, and confirms the script change is one added function
plus a CLI dispatch, with the frozen witness path untouched. This is one
separate agent's independent review — **not** external human review,
multi-member consensus, or ratification.

**Relation to Sec. 8.12.** The hypothesis is strictly weaker (no pre-existing
Alice-Bob coherence) and the geometry differs (one readout step to
`(1,1,1)`, not two to `(2,2,2)`); the signal is smaller, `3/128` against
`3/32`. This does **not** retroactively supply a preparation protocol for the
Sec. 8.12 channel, whose frozen theorem and review keep their exact bytes and
scope. The optimal-D gate stays **PARTIAL**; H1 stays **OPEN**; H3 and H4 stay
**NOT REACHED**. The experimental problem remains unopened, by instruction.

### 8.14 NONCORNER_SIGNALING_CONSTRUCTED / INDEPENDENTLY_REVIEWED (2026-09-17)

Successor to Sec. 8.13, executed under the frozen
[`NONCORNER_SIGNALING_GATE.md`](../theory/NONCORNER_SIGNALING_GATE.md): the
Alice-local preparation channel is **not** confined to the vertex
`(1,1,1)`. The [corrected execution report](../reports/2026-09-16--noncorner-signaling-gate.md)
and its [independent review](../reports/2026-09-16--noncorner-signaling-gate-independent-review.md)
are frozen together here. The review verdict is **PASS with three mandatory
textual repairs (`MR1`--`MR3`)**, all applied to the report; none changes a
computed quantity or the scientific verdict.

The exact one-step kernel support gives precisely four admissible non-vertex
sites, `y = (+/-1,+/-1,0)`, and the preregistered construction succeeds at
all four. At each site,

`M(y) = diag(-3/256,0) != 0`,
`p_0 = 25/1024`, `p_1 = 49/1024`, and `Delta p_B = 3/128`.

The reduced-state trace distance is exactly `D = 3/128`, so the exhibited
projection saturates the distinguishability bound for each computed pair of
states. This is pairwise measurement optimality only; it is not protocol,
preparation, site or intervention optimality. The result refutes
vertex-exclusivity for this protocol at `Delta T = 1`; it says nothing about
`Delta T = 2`, other vertices, asymptotic scaling, capacity, experimental
feasibility or our universe. No violation of the model's microscopic causal
bound is claimed.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NONCORNER_SIGNALING_CONSTRUCTED /
  INDEPENDENTLY_REVIEWED` in the exact scope above.
- **Software certificate: PASS with six externally verified properties not
  yet encoded as checks.** The run
  `verify_directional_saturation.py --noncorner-gate-only` passes **20/20
  exact checks**, but that count **is not by itself an exhaustive certificate**
  of the six properties listed in the execution report Sec. 8. They were
  independently checked by the reviewer. They remain recorded certification
  debt, not gaps in the scientific result.

The reviewed script is deliberately unchanged after review. Encoding those
six additional checks would alter the reviewed artefact and therefore require
a new review of that file. The earlier frozen contracts and witnesses retain
their bytes and scope; the optimal-D gate remains **PARTIAL** and no
experimental-design gate is opened here.

### 8.15 PHYSICAL_DIMENSIONAL_TRANSLATION — CLOSED / CONDITIONAL (2026-09-17)

Contract
[`PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md`](../theory/PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md)
frozen at `fca5881` before solving; see the
[dimensional audit](../reports/2026-09-17--physical-dimensional-translation-audit.md).

**Verdict: `DIMENSIONAL_MAP_CONDITIONAL`.** The source conventions support the
symbolic restoration

`x = a n`, `t = N tau`, `k = p/a`,
`E = hbar omega/tau (mod 2 pi hbar/tau)`, and
`v_phys = (a/tau) grad_p omega`.

Hence `c_IR^phys = a/tau`. Identifying it with an observed `c_phys` imposes
`a = c_phys tau`; it does not determine either absolute scale. The model and
checked sources specify no numerical `a` or `tau`, and the earlier Planck-scale
calculation was explicitly conditional, not a scale derivation.

For the frozen non-corner witness, conditionally on `(a,tau)`, the
encoding-to-readout interval is `tau` and Bob is at Euclidean distance
`sqrt(2)a`. If `a/tau = c_phys`, then the scale-free ratio is
`L/(c_phys tau) = sqrt(2)`: outside the emergent cone and inside the exact
one-step microscopic support, exactly as in lattice units.

The value `3/128` acquires **no units**. It remains the exact probability
difference and trace distance for the two idealized local states. It is not an
energy, rate or dimensional coupling. The exactly localized preparation is
broad over the full Brillouin zone, not a low-energy narrow-band state, so no
unique physical energy or momentum can be assigned from the IR dispersion.

**Claim ceiling.** A consistent conditional dictionary is established; a
parameter-free prediction in SI units is not. Absolute cutoff scale, physical
realization/coupling, efficiencies, noise, feasibility and any identification
with nature remain unspecified. No experiment was designed and `Delta T = 2`
was not opened.

### 8.16 NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`NARROW_BAND_SIGNALING_GATE.md`](../theory/NARROW_BAND_SIGNALING_GATE.md)
preregistered at `817050d` before any computation. Three artefacts are frozen
together at `778a44a`, through the provenance chain `5f6d350` -> `f00f64e` ->
`778a44a`:

- the [execution report](../reports/2026-09-17--narrow-band-signaling-gate.md);
- its exact certificate
  [`verify_narrow_band_gate.py`](../scripts/verify_narrow_band_gate.py);
- the [independent review](../reports/2026-09-17--narrow-band-signaling-gate-independent-review.md).

The question was whether the Alice-local signalling mechanism admits an
IR-controlled version with a preestablished narrow-band resource. The frozen
class is:

- node `p = 0`, both Weyl branches;
- `g(q) = (1-|q|^2)^2_+` supported on `|p| <= Lambda`, with
  `0 < Lambda < pi/4`;
- spin `down` and two common steps;
- the point gate `U_1 = exp(i pi n_0)` at the origin;
- Bob at `(1,1,0)`, with `Delta T = 1`.

**Verdict.** The Sec. 7 stop rule fires at the first control, before any signal
in Bob is computed: the point encoder is incompatible with the preregistered
relative IR criterion. Let `kappa = Lambda^3/(6 pi^2)`, the in-band share of
any one-site vector, and `s = ||P_0 psi_Lambda||^2`, with `0 < s <= kappa`. Then

`||Delta_Lambda||_1 = 4 sqrt(s(1-s)) -> 0`,
`eta_enc = ||Delta - Pi Delta Pi||_1/||Delta||_1 = sqrt((1-kappa)(1-3s(1-kappa))/(1-s))`.

So `eta_enc > 2 sqrt(6)/5` on the whole chart and `eta_enc -> 1`, while the
absolute leakage `epsilon_UV = 4s(1-kappa)` also tends to zero. The residual
outside the IR-IR block is dominated by the IR-UV and UV-IR coherences; the
UV-UV block is relatively `O(sqrt s)`. This is **not** a statement that the
encoding, the information or any signal is UV.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS /
  INDEPENDENTLY_REVIEWED`, in the exact scope below.
- **Review metadata.**
  - Cold independent agent review: PASS, after the mandatory repairs R1-R4 and
    MR1, all textual and all applied.
  - Human review: PASS.
  - No external peer review / no external replication yet.
  - Two earlier same-session adversarial reviews are archived as secondary,
    non-independent records. The self-review contains errors that the
    independent review corrected.
- **Software certificate: PASS, 34/34 exact checks.** The count covers only
  the identities and limits marked [V] in the report. The analytic steps listed
  in report Sec. 12 are not encoded as checks; the independent reviewer
  verified them by hand. They are recorded certification debt, not gaps in the
  result. The certificate imports `verify_directional_saturation.py`, which
  requires numpy, pinned in `scripts/requirements.txt`.

**Claim ceiling.** The result holds only for the frozen class and the Sec. 7
criterion.

- `D_B` was not computed, and `D_B = 0` is not asserted.
- It does not refute `3/128`, either at the vertex or at the non-corner sites.
  The non-corner witness uses the same `y_B = (1,1,0)`, but with an exactly
  localized resource and no IR criterion.
- It is no impossibility result for other encoders (extended, smoothed or
  `Lambda`-dependent gates), for resources without exact spectral support, for
  other notions of IR control, for other QCA, or for the physical continuum.
- `Lambda -> 0` is not `a, tau -> 0`, and no physical scale is set
  (Sec. 8.15).

**Erratum, charter header.** Lines 3-7 of the charter are pre-publication
text. They cite drafting base `HEAD=11efe1f` and scientific remote `780ecb0`,
state `NOT_EXECUTED / OUTCOME_OPEN`, and say that publication and execution
are pending. All of that is superseded: the charter was published at
`817050d`, executed, and frozen at `778a44a` with the status recorded in this
section. The charter deliberately keeps its bytes, for two reasons:

- its sha256 `3d559ced...` is pinned by the frozen certificate (check 1)
  and recorded in the report, the independent review and the freeze
  commits;
- contracts in this repository keep their pre-execution text, as
  `NONCORNER_SIGNALING_GATE.md` does.

The header was never part of the scientific contract (Secs. 1-15), which
is unchanged. `Delta T = 2` and the experimental problem remain unopened.

### 8.17 OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`SCALED_IR_SIGNALING_GATE.md`](../theory/SCALED_IR_SIGNALING_GATE.md)
preregistered at `31b5797` before any computation. Successor of Sec. 8.16,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--scaled-ir-signaling-gate.md);
- its exact certificate
  [`verify_scaled_ir_gate.py`](../scripts/verify_scaled_ir_gate.py);
- the [independent review](../reports/2026-09-17--scaled-ir-signaling-gate-independent-review.md).

The question is the disappearance law of Bob's distinguishability when
regions of size `O(1/Lambda)`, a margin `O(1/Lambda)` outside the emergent
cone of Alice's whole region, and time `O(1/Lambda)` are scaled together
(`N = Delta T = 1/Lambda`, Euclidean balls of radius `N/4`, frozen internal
families). A signal at fixed `Delta T`, or with an `O(1)`-site margin, does
not answer it.

**Verdict.** `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The eight frozen operations are IR-admissible. There is a directional
exponential upper bound, independently re-derived, for every one-particle
state and every unitary supported on `A_N`:

`δ_{M,M_B}(N) ≤ D_B(N) ≤ 36 N^4 exp[-(1 - √3/2)(log 2) N]`, `N ≥ 2`,

with `J = (1 - √3/2) log 2 > 0`. This **excludes**
`IR_RESOLVABLE_SIGNALING_POLYNOMIAL` in the frozen class and **does not
authorize** `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. All sixteen pairs
remain `OPEN_PAIR`: no positive lower bound, no proven vanishing, no
non-vanishing amplitude. `D_B = 0` is not asserted. The independent review
attacks specifically the three load-bearing steps named before promotion
(the geometry-to-kernel derivation of `J`, uniformity of `36 N^4`, and
polynomial exclusion without an existence claim) and returns **PASS**, with
no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with a one-sided quantitative bound.**
  `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`, in the exact
  scope below.
- **Review metadata.**
  - Cold independent agent review: PASS. No mandatory repairs. The three
    recommended drafting clarifications (`D_B = (1/2)||ρ1-ρ0||_1`;
    off-diagonal of the ellipse matrix; Schur diagonal operator-norm) were
    applied to the execution report at freeze. They change no quantity and
    no classification. Execution-report sha256 before/after those phrases:
    `4876ecab…` / `86a086dc…`. The CAR bound (DF) is not part of the frozen
    claim for the sixteen pairs.
  - Human freeze authorization: the 2026-09-17 instruction to freeze this
    status if the cold review passed, then to publish with those
    clarifications and without additional science.
  - No external peer review / no external replication yet.
- **Software certificate: PASS, 53/53 exact checks.** The count covers only
  the identities and limits marked [V] in the execution report. The
  analytic steps for `J`, `T_N`, `(D1)` and the classification were
  re-derived by the independent reviewer; they are not encoded as checks.

**Claim ceiling.** The result holds only for the frozen scaled class
(Euclidean balls, `α = 1/2`, `θ = π/2`, the declared internal families,
CJWW (5.15) in the one-particle sector).

- Any allowed effect in this class is at most `O(N^4 e^{-JN})`. That is a
  one-sided, model-falsifiable bound. It is not a two-sided prediction and
  not an existence result.
- Polynomial IR-resolvable signalling is discarded **in this
  geometry/class**. If a positive signal exists, it is at most
  nonperturbatively small. Existence is not claimed.
- The bound does not refute `3/128`, the vertex or non-corner witnesses, or
  the narrow-band negative (Sec. 8.16).
- `N → ∞` is not `a, τ → 0`. No physical scale is set (Sec. 8.15). An
  `e^{-JN}` law would translate only conditionally to a form
  `e^{-J' λ/a}`, with no numerical prediction.
- The internal families are not exhaustive. `M = a I + b·σ` in general is
  not covered. `I` is `REFERENCE_CONTROL` only.
- No new encoder is authorized. The cancellation analysis of the sixteen
  pairs is Sec. 8.18. The regional exponential rate is Sec. 8.19. The
  remaining bottleneck is the integrated Laplace coefficient
  (Hessian, profiles, spin, interference with the free tail `r`), not
  yet chartered.

`Delta T = 2` and the experimental problem remain unopened.

### 8.18 OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`LOWER_BOUND_NO_CANCELLATION_GATE.md`](../theory/LOWER_BOUND_NO_CANCELLATION_GATE.md)
preregistered at `1717d5e` before any computation. Successor of Sec. 8.17,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--lower-bound-no-cancellation-gate.md);
- its exact certificate
  [`verify_lower_bound_no_cancellation_gate.py`](../scripts/verify_lower_bound_no_cancellation_gate.py);
- the [independent review](../reports/2026-09-17--lower-bound-no-cancellation-independent-review.md).

**Verdict.** `OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The unique-path vertex

`(S^N)_{(N,N,N),0} = 4^{-N} |↓⟩⟨↓|`

exists and cannot be promoted to a regional leader (`K = log 4`, kills
`↑`, coherent regional sum). The Euclidean minimum of `|y-x|_2` on the
two balls is unique and lies on both spheres, where the profiles vanish.
That implies neither `A = 0` nor `A ≠ 0`. All sixteen pairs remain
`OPEN_PAIR`. `D_B = 0` is not asserted. The independent review attacks
those three load-bearing claims and returns **PASS**, with one recommended
drafting clarification applied at freeze (execution-report sha256 before /
after: `33691df6…` / `2da09280…`).

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN.** The obstacle is now localized: the
  competition between the propagation exponent and the profile zero at
  the boundary, not a missing trajectory and not a new encoder.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed.
- **Software certificate: PASS, 24/24 exact checks.** Identities only;
  leader, `A` and remainder are analytic and open.

**Claim ceiling.** Same frozen class as Sec. 8.17. No existence, no
vanishing, no `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The regional
rate is Sec. 8.19.

### 8.19 OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md`](../theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md)
preregistered at `08613d0` before any computation. Successor of Sec. 8.18,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--regional-directional-asymptotics-gate.md);
- its exact certificate
  [`verify_regional_directional_asymptotics_gate.py`](../scripts/verify_regional_directional_asymptotics_gate.py);
- the [independent review](../reports/2026-09-17--regional-directional-asymptotics-independent-review.md).

**Verdict.** `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The regional exponential rate is

`K_* = I(v_*)`, `v_* = (1 - 1/(2√3))(1,1,1)`,

with `I(v) = sup_ξ [ξ·v - arcosh(∏_j cosh ξ_j)]`. This is strictly
between `J` and `log 4`. It is the unique minimizer of `I` on the
regional velocity set (supporting tilt `ξ_* ∥ û`). The profile logarithms
are `O(log N)` and shift the saddle by `O(1)` lattice sites; they do
**not** change `K_*`. The coefficient `C` and the power `β` remain
unclassified. All sixteen pairs remain `OPEN_PAIR`. The independent
review attacks the three load-bearing claims (`I(v)` and the dual saddle;
uniqueness of `v_*`; `O(log N)` profiles) and returns **PASS**, with no
mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with the exponential rate identified.**
  `K_* = I(v_*)` is the Legendre envelope of the regional kernel. It is
  the exponential rate of `L` only if some `C` (or `C^{(j)}`) is
  non-vanishing and controlled, which is not claimed.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed, and not to open a
  coefficient gate before that review.
- **Software certificate: PASS, 18/18 exact checks.** Identities only;
  `C`, `β` and remainder are analytic and open.

**Claim ceiling.** Same frozen class. This section does not claim
existence, vanishing, or `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.
No new encoder. The complete Laplace coefficient at this unique saddle
is Sec. 8.20.

### 8.20 PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_LAPLACE_COEFFICIENT_GATE.md`](../theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md)
preregistered at `6f520ad` before any computation (blob `18d1f65`).
Successor of Sec. 8.19, without reopening it. Three artefacts are
recorded together here:

- the [execution report](../reports/2026-09-17--regional-laplace-coefficient-gate.md);
- its exact certificate
  [`verify_regional_laplace_coefficient_gate.py`](../scripts/verify_regional_laplace_coefficient_gate.py);
- the [independent review](../reports/2026-09-17--regional-laplace-coefficient-gate-independent-review.md).

**Verdict.** `PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`.
For all sixteen frozen pairs,

`L_{M,M_B}(N) = e^{-K_* N} N^{-13/2} (C_{M,M_B}(θ_N) + O(N^{-1/2}))`,

with `θ_N = {√3 N/4}` and `β = 13/2`. The complete coefficient is a sum
of the free-tail interference against the encoder layer, over the two
torus saddles `η ∈ {0, π(1,1,1)}` (distinct projectors `P` and `P̄`,
weights `Γ_±`). `C(θ)` is sign-definite and uniformly non-vanishing; the
relative oscillation is bounded by `1.47×10^{-3}`. Quadratic terms are
only bounded, at rate `e^{-2 K_* N}`. The independent review attacks the
seven load-bearing claims (`β`; complete `C` as a sum; uniform
non-vanishing; remainder vs charter `o(1)`; `C(θ)` vs constant `C`;
eight torus points vs frozen `K_*`; terminal state) and returns **PASS**,
with no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: PAULI_LEADING_COEFFICIENT_NONVANISHING.** `β = 13/2`
  is identified. All twelve Pauli pairs have `C(θ) ≠ 0` uniformly in `θ`,
  controlled against an `O(N^{-1/2})` remainder. With Secs. 8.17 and 8.19
  this authorizes, for those twelve pairs,
  `δ_{M,M_B}(N) = |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N} (1 + O(N^{-1/2}))`
  and `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` for those pairs. The
  four `M = I` pairs are also non-vanishing (`REFERENCE_CONTROL`).
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze, commit and promote as separate steps if the cold review passed.
- **Software certificate: PASS, 58/58 exact checks.** Identities and
  interval enclosures of closed forms, including uniform sign of
  `C_{M,M_B}(θ)` for all sixteen pairs. Analytic remainder lemmas (`N_*`,
  `C'`) are report `[A]`, not encoded. Finite-`N` diagnostics are
  `SUPPORTED` only.

**Claim ceiling.** Same frozen class. `C = C(θ_N)`, not an `N`-independent
constant. The remainder is asymptotic: `N_*` and `C'` are not explicit;
the leading formula is not quantitatively reliable for `N ≲ 10^3`, and
for `M ∈ {I, σ_3}` the `N^{-17/2}` piece dominates at diagnostic `N`.
No `D_B = 0`, no `δ ≡ 0`. Does not reopen `K_*`, `v_*`, geometry,
encoders, detectors, profiles, node or walk. Does not reopen
Secs. 8.16–8.19, `3/128`, no-corner, or `Delta T = 2`. `N → ∞` is not
`a, τ → 0`. No physical units. No claim of a microcausality violation.
The general family `M = a I + b · σ` is not covered.

The Sec. 8.19 sentence that the spectral-radius maximum is unique at
`η = 0` is false (equality on `{0,π}³`); `K_*` is unchanged and the extra
contributing point `π(1,1,1)` is included in `C`. The Sec. 8.19 files
are not edited.

This is a branch-local promotion only; `main` is unchanged.

**Project-level consequence (direct user instruction, 2026-09-17).**
In this frozen class, theoretical step 3 of the physical line is closed.
There is an operational IR response outside the emergent cone, and it is
not a mere consequence of the UV propagator. For the twelve Pauli pairs
the response is asymptotically non-vanishing and
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The precise claim, not to
be exaggerated, is:

> In the 3D Weyl QCA under study, the difference between the emergent
> relativistic cone and the microscopic causal support is not only a
> geometric possibility: under the preregistered IR-controlled protocol
> it produces an asymptotically non-vanishing operational response,
> albeit nonperturbatively suppressed.

That is a property of the model, with standing outside the repository as
such. It is not a statement about nature, not `D_B > 0` for every QCA,
and not an experimental prediction. No further signalling gate is
authorized. Fork 4A (a physical implementation of the walk that could
test the derived law) is identified and **not chartered**. The authorized
next front is Sec. 8.21.

### 8.21 PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE — AUTHORIZED, NOT_EXECUTED (2026-09-17)

Contract
[`PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md`](../theory/PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md)
frozen before any calculation, by direct user instruction (2026-09-17),
with the four closure criteria and first-class negative outcomes
incorporated before execution (this commit; first preregistration
`e9353ad`). Successor of Sec. 8.20, without reopening it. Inherits
Sec. 8.15 (`DIMENSIONAL_MAP_CONDITIONAL`) without reopening the `3/128`
audit. **Not a signalling gate, not a rate gate, not a Laplace-coefficient
gate, not a laboratory-implementation gate (4A).**

**Initial evidence status: `NOT_EXECUTED / OUTCOME_OPEN`.**

Step 3 is **input**, not an object to re-optimize. The gate does **not**
ask whether `δ_{M,M_B}(N) ≠ 0`. It asks whether a physically defensible
identification

`(a, τ, Λ, internal modes, A, B) ↔ (physical magnitudes and operations)`

converts `δ(N) ∼ |C(θ_N)| N^{-13/2} e^{-K_* N}` into a dimensional,
falsifiable prediction.

**Four hard closure criteria, all scored separately:**

1. **Absolute scale.** `a/τ = c` is not enough. External information must
   fix `a` or `τ`, or an additional physically motivated relation must
   appear. `a = ℓ_P` is `ASSUMPTION`, never `DERIVED`.
2. **Physical dictionary.** What the two internal components are, which
   physical operation implements `M = σ_j`, what `M_B` is, and what a
   narrow-band preparation is in the candidate system. A formal relabelling
   is not a dictionary.
3. **Dimensional observable.** From a dimensionless distance/probability
   to something an apparatus records (counts, phase, frequency, energy,
   occupation, correlation, or other), with an explicit SI law.
4. **Detectability.** If substituting physical scales yields
   `δ ∼ e^{-K_* λ/a}` with `λ/a` astronomical, the effect may be real
   and experimentally inaccessible. That is a legitimate closure.

A viable experiment is **not** the success criterion. First-class
negative outcomes: `NO_ABSOLUTE_SCALE_DERIVABLE`,
`PHYSICAL_MAP_CONDITIONAL_ONLY`,
`PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE`. None of these weakens Sec. 8.20.

Binding separation: model closed ≠ nature established ≠ experiment designed.

**Premises, not reopened:** `K_*`, `β`, `C(θ_N)`, the sixteen pairs, the
conditional dictionary of Sec. 8.15. **Not authorized:** execution of
this gate; fork 4A; a new signalling encoder, detector or geometry;
re-optimizing `K_*` or `C`; treating `N → ∞` as `a, τ → 0`; using a
Planck fiat as `DERIVED`.

**Theory paper (draft, not a gate).** The closed model result is written
as
[`papers/ir-corona-operational-response-draft.md`](../papers/ir-corona-operational-response-draft.md).
It does not wait on 4B. It separates ultraviolet propagator, infrared
operational response, and nature.

**Literature input to 4B, not execution.**
[`2026-09-17--physical-realization-literature-scan.md`](../reports/2026-09-17--physical-realization-literature-scan.md).
Adversarial bibliographic scan only. Three bins:
`ENGINEERED_EMULATOR`, `NATURAL_EFFECTIVE_ANALOG`,
`FUNDAMENTAL_CANDIDATE`. Hard question (natural system, `a` and `τ`
physically fixed, infrared cone strictly narrower than microscopic
support, known observable of that gap): **no** on this pass. Ion-trap
and photonic Dirac automata are 4A antecedents. Pavia/Mlodinow–Brun
are incomplete fundamental candidates (Planck `ASSUMPTION`, different
observables). This scan does **not** assign a 4B terminal state.


## 9. H1-only inhomogeneous reopening — branch-local update (2026-09-20)

**Status (2026-09-24): H1 OPEN; H1c localization unproved, work PAUSED.
The operational contract is fixed in Sec. 9.6; the next gate is T1.**

This update supersedes the older statement that physical-realization / absolute-scale
Sec. 8.21 is the active line. The flat CJWW (5.15) operational IR-corona result
remains closed in its frozen class. The later inhomogeneous/AdS extension is not
reactivated as a whole: only H1 has been reopened.

Full research record:
- [H1 chat research log](../reports/2026-09-20--h1-chat-research-log.md)
- [H1 localization reconstruction and gate ledger](../reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md)
- primary endpoint/layer source: [regional Laplace-coefficient gate](../reports/2026-09-17--regional-laplace-coefficient-gate.md)

### 9.1 Frozen local structure

For
\[
D(z)=S(z)\oplus S(z)^{-1},\qquad
C_N(X)=e^{-i\vartheta(X)\beta/N},
\]
under the working frozen beta contract
\[
\beta^2=I,\qquad \beta D\beta=D^{-1},
\]
the dominant rank-two Riesz bundle satisfies
\[
\mathcal P\beta\mathcal P=0.
\]

Current statuses:
- \`H1-SR = PROVED_UNDER_FROZEN_BETA_CONTRACT\`;
- \`H1a = PROOF_WRITTEN / UNREVIEWED\`;
- \`H1b = PROOF_WRITTEN / UNREVIEWED\`;
- \`DERIVATIVE_SELECTION_RULE = PASS\`.

No global torus spectral gap is claimed.

### 9.2 Endpoint absolute-mass gate

The 2026-09-17 primary regional report was rechecked. It uses the complete
endpoint spinors, before spectral projection,
\[
f=s_Nb_N\chi,\qquad w=h_BM_Br,
\]
with
\[
b_N=O(N^{-3/2}),\quad
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),
\]
\[
s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),\quad
h_B=\frac{64}{N^2}{\varepsilon'_\perp}^{\,2}.
\]

Accounting for tangential area \(O(N(1+j))\) at normal depth \(j\) and the
exponentially summable tilted normal weight gives
\[
\sum_x e^{\xi_*\cdot(x-x_*)}\|f(x)\|=O(N^{-5/2}),
\]
\[
\sum_y e^{-\xi_*\cdot(y-y_*)}\|w(y)\|=O(N^{-5/2}).
\]

Therefore:
\[
\boxed{\texttt{LAYER_ABSOLUTE_MASS_BOUND = PASS}}.
\]

This is a full-spinor absolute bound, not a cancellation or dominant-projection
bound.

**Scope at the 2026-09-24 freeze:** these are the inherited flat endpoint
estimates. Their transfer to the two-channel response and its reference
`U_N^N Phi_N` is not certified here; that trace belongs to T1–T2 in Sec. 9.6.

### 9.3 Local-window insertion and leakage gates

Using the derivative selection rule and the endpoint bounds:
\[
\boxed{\texttt{G_INSERTION_POWER_STABILITY = PASS_IN_LOCAL_WINDOW}}.
\]

The final complementary-bundle leakage is controlled by the full Bob norm.
The safe dominant correction is the zeroth-order \(Q\beta\mathcal P/N\) term,
giving
\[
|\Delta T_Q|=O(N^{-15/2}),
\]
not the earlier exploratory \(O(N^{-8})\) count. Hence:
\[
\boxed{\texttt{FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW}}.
\]

These are local-window statements only.

### 9.4 Remaining H1c gate

Literal pathwise H1b is not valid because a spatial path carries individual
hopping matrices \(D_h\), not the full symbol \(D(z)\). Thus:
\[
\texttt{H1c_GLOBAL = UNNECESSARY},
\qquad
\texttt{H1c_LOCALIZED = OPEN}.
\]

The unresolved localization statement recorded before the model freeze is:
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

Work on that asymptotic statement is **PAUSED** by the 2026-09-24 decision.
Sec. 9.6 supersedes the immediate route below with an exact observable gate.

A candidate momentum-space Dyson route has been formulated. Its key local
selection factor is
\[
\mathcal P(\eta+q)\beta\mathcal P(\eta)=O(|q|),
\]
and, for \(K_N(q)=N^3\widehat\vartheta(Nq)\),
\[
\int |q||K_N(q)|\,dq
=\frac1N\int |p||\widehat\vartheta(p)|\,dp.
\]
The working regularity assumption for this route is the Fourier-moment
condition
\[
\int_{\mathbb R^3}(1+|p|)|\widehat\vartheta(p)|\,dp<\infty.
\]

The historical candidate \(n\)-insertion estimate was
\[
e^{-N\varphi_*}|T_n|
\le C N^{-13/2}\frac{(C'/N)^n}{n!}.
\]

**This estimate is not proved.** The missing step is uniform control of
non-normal variable-momentum products, including complementary-bundle visits,
transitions among the eight saddle neighborhoods, and regions where the local
Riesz splitting is unavailable. No momentum-conservation assumption may be
smuggled into that proof.

The [2026-09-24 Dyson precheck](../reports/2026-09-24--h1c-dyson-target-check.md)
also challenges this target when `n` counts raw insertions and the fixed
flat embedded endpoints are admitted. That precheck remains preliminary,
without independent review; this freeze does not promote it or transfer
its fixed-endpoint conclusion to the new physical response.

### 9.5 Locks

The H1 reopening does not change:
- \`E0 = OPEN_AT_STOP\`;
- \`POWER_13/2_STABILITY = OPEN_AT_STOP\`;
- \`E / AdS = STOPPED_UNPROVEN\`.

No localization or H1 promotion is authorized without proof and review.
The explicit operational model choice in Sec. 9.6 closes a contract only.

### 9.6 H1c-0 close / two-channel operational model — 2026-09-24

Direct user instruction freezes **TWO_DISTINGUISHABLE_CHANNELS** for this
candidate extension. The complete contract, prior diagnostic stages and
seven-report provenance are in the
[Schur audit and operational close, §§6–8](../reports/2026-09-24--h1c-return-kernel-schur-audit.md).

The one-particle space is `ell^2(Z^3) tensor C^2_channel tensor C^2_spin`.
The blocks of `D=S direct-sum S^-1` are assumed to be distinguishable
internal channels; `beta=sigma_x_channel tensor I_spin` exchanges them.
Bob's ability to resolve the channel is part of the new assumption. The
earlier repository did not derive this physical interpretation.

Prepare `Phi_N=(phi_N,0)` and evolve
`Psi_b=U_N^N mathcal U_M^(b) Phi_N=(psi_b^+,psi_b^-)`.
At encoding, `U_M direct-sum U_M` and `U_M direct-sum I` agree on this
preparation; they are not identified as physical operations on other states.
Bob uses `F_+=E direct-sum 0`, `F_-=0 direct-sum E` and
`F_empty=I_H-(E direct-sum E)`. The primary response is `(L_+,L_-)`,
where `L_±=<psi_1^±,E psi_1^±>-<psi_0^±,E psi_0^±>` and
`L_empty=-L_+-L_-`. `L_block=L_+` and `L_incl=L_++L_-` are only
coarse-grainings; signed responses are summed before absolute values.

For `vartheta=0`, `C_N=I` and `U_N^N(x,0)=(S^N x,0)`, so
`(L_+,L_-)=(L_flat,0)` and `L_incl=L_flat` exactly. This flat control
motivates the candidate; favorable asymptotics do not select its detector.
Channels may retain quantum coherence; the three-outcome POVM does not
reconstruct every coherence. Identification with a concrete physical
system remains OPEN. All future extension claims are conditional on this
contract, not universal claims about the original flat protocol. Neither
coarse-graining may later replace the primary observable for better powers.

```text
H1c-0a mathematical doubled-walk contract: CLOSED
H1c-0b operational model choice: FIXED_BY_EXPLICIT_ASSUMPTION
physical realization/justification: OPEN
Volterra/asymptotic localization: PAUSED
primary observable: (L_+, L_-)
```

**Exploratory sequence executed by direct user instruction, 2026-09-24:**

1. **T1 — exact signed P/Q lift:** derivation and frozen five-piece
   vocabulary in
   [`two-channel T1 report`](../reports/2026-09-24--two-channel-t1-exact-signed-pq.md).
   Status: `PASS`, reviewed by Claude Opus and DeepSeek V4-Pro in the
   deliberative session
   [`T1 re-review`](../debates/2026-09-24--two-channel-t1-rereview.md).
   This is independent agent review across two model families, not human
   review. The pass is conditional on the explicit two-channel contract and
   a fixed admissible W. It does not certify estimates.
2. **T2 — trace of `O(N^-6)`:**
   [`T2 trace`](../reports/2026-09-24--two-channel-t2-trace.md) locates
   the old bound in the normalized auxiliary bilinear return correction.
   Status: `TRACE_COMPLETE / BOUND_NOT_TRANSFERRED`. It is a potential sub-contribution in the terminal-P linear slot
   `A_cP` for the earlier functional, conditional on matching its endpoint.
   No transfer to any of the ten current pieces is proved. The old
   `O(N^-6)` remains a coarse ceiling, not a signed term or coefficient.
3. **T3 — cancellation:** status `STOPPED_NO_SIGNED_TERM`. The frozen stop applies because T2 isolated no
   signed term or coefficient. No cancellation or symmetry search was
   performed; see [`T3 stop`](../reports/2026-09-24--two-channel-t3-stop.md).

These records do not prove H1c or H1, promote preliminary localization
prechecks, or alter C2/C3, E0, POWER_13/2_STABILITY, E/AdS, or the flat
manuscript. Physical realization of the two channels remains OPEN.
The next candidate question is whether bounds for all ten signed pieces
can be derived from the physical endpoints \((r_c,d_{c,P},d_{c,Q})\).
It is not executed or opened in this record.

## 10. IR spectral-attribution audit — 2026-09-22

User-authorized exploratory audit and commit/push, documented in the
[full report](../reports/2026-09-22--ir-spectral-attribution-audit.md).
Status: **SUPPORTED / FINITE_N_NUMERICAL_DIAGNOSTIC**.
For the fixed sigma2/I pair, N=24 and N=40 pass the stated empirical precision
criterion. Lpp and R=L-Lpp nearly cancel. At N=40, direct nonperiodic
position evolution agrees with the tilted FFT: field discrepancy normalized
by maximum amplitude 1.62e-15; signal relative discrepancy 5.07e-16.
No asymptotic trend, exclusively UV origin, or rigorous numerical enclosure
is claimed. IR admissibility of operations does not by itself prove
predominance of the PP contribution at the exponentially small signal scale.
The stronger spectral attribution remains OPEN. The Sec. 8.20 flat theorem
retains its scope and status; its full proof is not re-certified here.
H1c, E0, POWER_13/2_STABILITY and E/AdS statuses of Sec. 9 are unchanged.
This records completed authorized diagnostics, not authorization for larger scans.

### 10.1 IR spectral-attribution front C1/C2/C3 — gate ledger (2026-09-22)

Explicit user decision on 2026-09-22 to record the certified C1 and C2a
verdicts here. Branch-local, like the rest of this file; `main` is unchanged.
Subsequent user acceptance on the same date promotes C2b after its independent
review and unblocks C2c as a structural-scope gate, without promoting C2c.
Contracts: [C1/C2/C3](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md),
[C2a](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md),
[C2b](../theory/IR_C2B_BLOCK_DECOMPOSITION_GATE.md),
[C2c structural scope](../theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md).
The front is fixed to P=Pi'=1_{|p|<=N^-1/2} (hard cutoff), Q=I-P, and the
signed block observable
Lpp=tr(E S^N P Delta P S^-N). This observable is not the conditioned Lcond
of C3.

| Subgate | Status | Evidence |
| --- | --- | --- |
| C1 leakage | **PASS** | [derivation](../reports/2026-09-22--ir-projection-leakage-and-conditioning.md), [independent review](../reports/2026-09-22--c1-leakage-independent-review.md) |
| C2a transfer, sigma2/I | **PASS** | [derivation](../reports/2026-09-22--c2a-oscillatory-transfer.md), [independent review](../reports/2026-09-22--c2a-independent-review.md) |
| C2b block decomposition, sigma2/I | **PASS** | [candidate](../reports/2026-09-22--c2b-block-decomposition-candidate.md), [independent review](../reports/2026-09-22--c2b-independent-review.md); B4_PRIME_PASS separately |
| C2c structural scope | **PASS — C2C_PASS, scope frozen** | [repaired execution](../reports/2026-09-22--c2c-structural-scope.md), [repaired review criteria](../theory/IR_C2C_REPAIRED_REVIEW_CRITERIA.md), [independent review](../reports/2026-09-23--c2c-independent-review.md); 16 original pairs only |
| C3 conditioning | **PASS — C3_PROOF_WRITTEN_REVIEW_ACCEPTED, scope frozen** | [execution](../reports/2026-09-23--c3-conditioning-execution.md), [DeepSeek/Gemini independent review](../reports/2026-09-23--c3-deepseek-gemini-review.md), commit `191ca20`; four original encoders, `M_B=I` only |
| E/AdS | **FROZEN** (STOPPED_UNPROVEN, Sec. 9.5) | unchanged |

- **C1 result:** q_N = ||Q(U_M-I)phi_N||^2 = D N^-5/2 (1+O(N^-1/2)) with
  D = 1024 pi^2 Phi_0(1/4)^2/5 > 0, for all four encoders. It follows that
  ||Delta - P Delta P||_1 = 2 sqrt(D) N^-5/4 (1+O(N^-1/2)).
- **C2a result (sigma2/I):**
  Lpp = N^-3 [C0 + C1 cos(sqrt(N)/2)] + O(N^-13/4), with C0 > C1 > 0 proved
  analytically (no numerical input). Hence Lpp = Theta(N^-3) and Lpp > 0 for
  all sufficiently large N.
- **Earlier consequence of C2a (arithmetic only):** R = L - Lpp = -Lpp + L
  exactly, and Thm 4.1 gives |L| <= 36 N^4 e^{-JN}. The complement of the PP
  block therefore cancels an algebraic Theta(N^-3) response. This establishes
  the cancellation's existence; it is not the proof of C2b below.
- **C2b result (sigma2/I):** direct block decomposition gives
  Lpp = +N^-3 A_N + O(N^-13/4), Lqq = +N^-3 A_N + O(N^-13/4), and
  Lpq + Lqp = -2 N^-3 A_N + O(N^-13/4), with the same
  A_N = C0 + C1 cos(sqrt(N)/2) >= C0-C1 > 0 as C2a.
  Thus the diagonal leaders are positive and the opposite leader lies in
  the coherences. Lqq >= 0 exactly; positivity of Lpp is asymptotic.
  B4_PRIME_PASS additionally gives Lpq = -N^-3 A_N + O(N^-13/4) and
  Lqp = -N^-3 A_N + O(N^-13/4); exactly, Lqp is the complex conjugate
  of Lpq, not necessarily equal to it at finite N.
- **Autonomous mechanism and bounds:** d_Q = d - d_P follows from Q=I-P
  and linearity. Thm 4.1 applies to the local source a, giving
  ||E^(1/2)(d_Q+d_P)|| <= 2 T_N. For every N>=2,
  |Lqq-Q_N| <= 8 T_N + 4 T_N^2 and
  |Lpq+Lqp+Lin_N+2 Q_N| <= 12 T_N, with T_N <= 9 N^4 exp(-JN).
  Here Q_N denotes the quadratic form <d_P,E d_P>, not the projector Q.
  C2a controls this quadratic form and Lin_N separately. No L-Lpp,
  Thm 4.4, total-signal asymptotics or N=24/40 data establish these blocks.

Caveats that must be retained with the C2a PASS:

1. The error term gains only N^-1/4 over the leading term.
2. The asymptotic regime is reached slowly: the oscillatory gains are powers
   of 1/(gamma sqrt(N)), where gamma = sqrt(3) - 3/2, which is about 1.1 at
   N=24 and 1.5 at N=40. The retained N=24/40 values do not validate or
   refute the sign.
3. The PASS is one independent **agent** review (Claude Opus 5). It is not
   an external human verification or a multi-member ratification.

C2b remains a `POST-DISCOVERY VERIFICATION GATE`: its discovery preceded
its contract. The independent review covers exactly snapshot
`19eb7a383cbb09464e91b64e89f724204e58cccb` and returns C2B_PASS and
B4_PRIME_PASS without required repairs. Review artifact SHA256:
`65bab830c6960f2c661ae47d739d90c1ecf8ae06b5f9923383919f76c2b234d5`.
The reviewer is recorded as **Codex, agent `/root`**, distinct from the
candidate's author, Claude Opus 5. This is one independent agent review,
not external human review, multi-member consensus or documented model
diversity. No additional Astra review has been recorded; such a review
remains an optional additional audit before publication, not a condition
retroactively imposed on this internal PASS.

C2c addressed **structural scope**, starting from the mechanism already
proved for sigma2/I: distinguish algebra and localized compensation from
pair-dependent leading coefficients, classify the sixteen original pairs,
and state the hypotheses and limits of any general hard-cutoff result.
The repaired execution makes the detector/espinor transfer explicit, retains
all band crossings, changes the grouping claim to **at most eight families**,
and restricts §9.2 to scalar indicator cuts with the stated open-set and
finite-support hypotheses. An independent review records
`C2C_PASS` for all five S3 levels on all sixteen original pairs, C1, and
§9.2 within that scope. The exponent `N^-3` remains a property of the frozen
`K=sqrt(N)` protocol, not a general QCA law; `N_0` and remainder constants
remain non-effective, and `NOVELTY=OPEN`.

C3 conditioning is now **C3_PROOF_WRITTEN_REVIEW_ACCEPTED** for the four
original encoders with `M_B=I`, the frozen hard cutoff and the same CJWW
protocol. The accepted result is
`Lcond-LPP = D p_infty N^-5/2 (1+o(1))`, with `D>0` and `p_infty>0`.
The result concerns the postselection increment. The leader and absolute
magnitude of `Lcond`, and comparison with the total signal `L`, remain outside
the C3 contract; no broader detector or QCA claim follows.

The C2c promotion is branch-local and does not alter the C3 result, E/AdS or FR1–FR3.
The repaired report and review retain their own commits and hashes; no
finite-N claim or broader detector/QCA class is added.

C3 is PASS in its frozen scope; E/AdS remains FROZEN. H1c, E0,
POWER_13/2_STABILITY and the Sec. 8.20 flat theorem are unchanged. No new
numerical calculation, scan, manuscript publication, commit or push follows
from this update.
```


## Ronda 1 — ABNER

La versión más fuerte del borrador es acotada: no afirma \(N^{-7}\), no transfiere al contrato de dos canales ni a \(r_c\), y no controla la parte Q de Schur (8). Sólo afirma que los extremos planos heredados \(f=s_Nb_N\chi\), \(w=h_BM_Br\) tienen norma \(\ell^2_{\mathrm{tilt}}\) \(O(N^{-3})\), con los pesos \(e^{2\xi_*\cdot(x-x_*)}\) y \(e^{-2\xi_*\cdot(y-y_*)}\). [RECONSTRUCTION]

Los pasos 1 y 2 sostienen esa versión. [INFERENCE] La cota puntual (1a)–(1d) descansa en \(g\ge0\), en la unitariedad de \(S(p)\) sobre el toro real, en \(F_N=64\varepsilon_\perp^2/N^2\) sobre el soporte y en \(\delta\le(1+j)/\sqrt3\); no detecto un factor oculto en \(u\), en \(\theta_N\) ni en \(N\). [INFERENCE] El conteo \(\#_j\le CN(1+j)\) con covolumen \(\sqrt3\) y una celda fundamental de diámetro \(\sqrt6\) es válido como cota superior, aunque no sea el diámetro de la celda de Voronoi; anclar una celda fundamental de diámetro \(\sqrt6\) y área \(\sqrt3\) permite dividir el área del disco agrandado por \(\sqrt3\). [INFERENCE] La suma cuadrática da \(N^{-6}\), por tanto norma \(N^{-3}\). [SOURCE] No veo en los pasos 1–2 una objeción fatal. [INFERENCE]

El punto más débil es el paso 3, donde el borrador afirma que no hay diferencia de peso, variable, medida ni normalización con Schur (8). [SOURCE] En el acta no consta la definición literal de las ecuaciones (6)–(8) de Schur. [ABSENCE: busqué en el contexto adjunto y sólo aparece la descripción fragmentaria de \(P=L^2\), \(Q=\|\cdot\|_*\), \(P=0\) fuera de ventanas \(W\), y \(\Lambda=e^{\Phi_*}\) en el informe H1c.] Bajo esa descripción, la norma \(P\) de un extremo no es automáticamente la norma \(L^2\) plana total: es la norma \(L^2\) de la componente espectral dominante \(P\mathfrak A_f\) en las ventanas locales, mientras que la componente Q usa otra norma. [RECONSTRUCTION]

El extremo plano heredado \(f=s_Nb_N\chi\) es un espinor completo. En general no está en el rango del proyector de Perron \(P\); tiene componente Q. [INFERENCE] El propio borrador admite que la parte Q de los extremos no queda controlada. [SOURCE] Por tanto, la identidad exacta de Parseval
\[
\|\mathfrak A_f\|_{L^2(d\mu)}=\|f\|_{\ell^2_{\mathrm{tilt}}}
\]
demuestra igualdad de la norma total de \(\mathfrak A_f\), no igualdad de \(\|P\mathfrak A_f\|_{L^2(d\mu)}\) con \(\|f\|_{\ell^2_{\mathrm{tilt}}}\). [INFERENCE] La afirmación “coinciden exactamente” es, con esa lectura de Schur, falsa o al menos no demostrada. [INFERENCE]

No es fatal para la cota principal: como \(\|P\mathfrak A_f\|_{L^2}\le\|\mathfrak A_f\|_{L^2}\), el resultado \(O(N^{-3})\) en \(\ell^2_{\mathrm{tilt}}\) sí acota la componente P, que es la que Schur (8) controla. [INFERENCE] Pero el criterio 3 pide verificar coincidencia exacta; el borrador no la establece. [SOURCE]

Condición de concesión: la objeción queda desactivada si se exhibe en Schur (6)–(8) que la norma \(P\) de los extremos es literalmente \(\|\mathfrak A_f\|_{L^2(d\mu)}\) sobre el embebido completo \((f,0)\), con \(P\) igual a la identidad en ese rango y sin multiplicar los extremos por \(\Lambda=e^{\Phi_*}\). Si esa condición no se cumple, la reparación obligada es sustituir “coinciden exactamente” por “la norma \(P\) está dominada por la norma \(\ell^2_{\mathrm{tilt}}\)”, y declarar que no se transfiere control a la componente Q. [ORIGINAL]

En esas condiciones, mi veredicto sería \(PASS\_WITH\_REPAIRS\): los pasos 1–2 prueban la cota declarada, y el paso 3 requiere la reparación de alcance indicada. [ORIGINAL]

## Ronda 1 — GEMINI

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
{
  "error": {
    "code": 402,
    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",
    "status": "RESOURCE_EXHAUSTED"
  }
}
```

## Ronda Residuo — ABNER

Queda en pie la cota \(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\) para los extremos planos heredados: la cota puntual, el conteo \(\#_j\le CN(1+j)\) y la suma cuadrática \(O(N^{-6})\) no presentan objeción fatal. Debe abandonarse la afirmación del paso 3 de coincidencia exacta entre la norma P de Schur (6)–(8) y la norma \(\ell^2_{\rm tilt}\) de los extremos completos: lo único establecido por Parseval es \(\|P\mathfrak A_f\|_{L^2}\le\|\mathfrak A_f\|_{L^2}=\|f\|_{\ell^2_{\rm tilt}}\). No está justificada la frase “no se encuentra diferencia de peso, variable, medida ni normalización”, porque el acta no muestra la definición literal de (6)–(8) ni que el extremo \(f\) quede en el rango de \(P\); la componente Q sigue sin control, como admite el propio borrador. No discrepo de otro residuo: GEMINI no produjo turno. Veredicto resultante: \(PASS\_WITH\_REPAIRS\), con la reparación obligatoria de restringir el paso 3 a dominación y excluir transferencia a Q, dos canales y \(r_c\).

## Ronda Residuo — GEMINI

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
{
  "error": {
    "code": 402,
    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",
    "status": "RESOURCE_EXHAUSTED"
  }
}
```

> GEMINI queda fuera del resto de la sesión tras 2 fallos; no se interpreta su ausencia como acuerdo.

## Ronda Veredicto — ABNER

1. ACUERDO — No hay acuerdo colectivo entre los dos miembros: GEMINI falló dos turnos y quedó excluido, y su ausencia no se interpreta como acuerdo. La única posición registrada, la de ABNER, acepta lo siguiente: la versión más fuerte del borrador es acotada, no reivindica \(N^{-7}\) y no transfiere nada al contrato de dos canales ni a \(r_c\); los pasos 1 y 2, con la excepción discutida del paso 3, sostienen \(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\), en particular la cota puntual, el conteo \(\#_j\le CN(1+j)\) y la suma cuadrática \(O(N^{-6})\); la objeción al paso 3 no es fatal para esa cota, porque \(\|P\mathfrak A_f\|_{L^2}\le\|\mathfrak A_f\|_{L^2}=\|f\|_{\ell^2_{\rm tilt}}\).

2. DESACUERDO VIVO — No hay desacuerdo entre miembros, porque sólo ABNER intervino. La discrepancia viva es con el texto sometido. El paso 3 del borrador afirma que no hay diferencia de peso, variable, medida ni normalización entre la inclinación, los centros, \(\Lambda=e^{\Phi_*}\), el Parseval con \(d\mu=d^3p/(2\pi)^3\), el embebido en \(\mathbb C^4\) y la norma P de Schur (6)–(8). ABNER sostiene que el acta no contiene la definición literal de (6)–(8), que la lectura disponible de Schur identifica la norma P con la norma \(L^2\) de la componente espectral dominante \(P\mathfrak A_f\) en ventanas locales, y que por tanto lo único establecido es dominación, no coincidencia exacta; la componente Q de los extremos completos queda sin control, como el propio borrador admite. Esta discrepancia no fue resuelta por otro miembro.

3. ABANDONADO — Queda abandonada la afirmación del paso 3 de coincidencia exacta entre la norma P de Schur (6)–(8) y la norma \(\ell^2_{\rm tilt}\) de los extremos completos, en la forma escrita. Queda igualmente abandonada toda lectura que haga derivar de Parseval que la componente Q queda controlada o que Schur (8) controla la norma total de los extremos planos. No se abandona: la cota \(O(N^{-3})\) en \(\ell^2_{\rm tilt}\), la dominación \(\|P\mathfrak A_f\|_{L^2}\le\|f\|_{\ell^2_{\rm tilt}}\), ni la declaración del borrador de no transferencia a dos canales y a \(r_c\).

4. PENDIENTE — Para cerrar lo abierto haría falta: el texto literal de Schur (6)–(8), con la definición exacta de \(P\), \(Q\), \(\|\cdot\|_*\), las ventanas, la medida y la normalización, de modo que pueda decidirse si la norma P de los extremos es literalmente \(\|\mathfrak A_f\|_{L^2(d\mu)}\) sobre el embebido completo \((f,0)\), con \(P\) igual a la identidad en ese rango y sin multiplicar por \(\Lambda\); demostrar que \(f=s_Nb_N\chi\) y \(w=h_BM_Br\) quedan en el rango de \(P\) con \(\|P\mathfrak A_f\|=\|\mathfrak A_f\|\), o aceptar la reparación de degradar el paso 3 a dominación y excluir expresamente la componente Q; y una revisión adversarial de los pasos 1 y 2 y de esa reparación por un miembro distinto de ABNER, ya que GEMINI no llegó a emitir turno.

## Ronda Veredicto — ABNER

1. AGREEMENT — There is no collective agreement between the two members: GEMINI missed two turns and was excluded, and its absence is not interpreted as agreement. The only recorded position, ABNER’s, accepts the following: the strongest version of the draft is bounded, does not claim \(N^{-7}\), and transfers nothing to the two-channel contract or to \(r_c\); steps 1 and 2, with the discussed exception of step 3, support \(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\), in particular the pointwise bound, the count \(\#_j\le CN(1+j)\), and the quadratic sum \(O(N^{-6})\); the objection to step 3 is not fatal to that bound, because \(\|P\mathfrak A_f\|_{L^2}\le\|\mathfrak A_f\|_{L^2}=\|f\|_{\ell^2_{\rm tilt}}\).

2. LIVE DISAGREEMENT — There is no disagreement between members, because only ABNER intervened. The live discrepancy is with the submitted text. Step 3 of the draft asserts that there is no difference of weight, variable, measure, or normalization among the tilt, the centers, \(\Lambda=e^{\Phi_*}\), the Parseval with \(d\mu=d^3p/(2\pi)^3\), the embedding into \(\mathbb C^4\), and Schur’s P norm (6)–(8). ABNER holds that the record does not contain the literal definition of (6)–(8), that the available reading of Schur identifies the P norm with the \(L^2\) norm of the dominant spectral component \(P\mathfrak A_f\) in local windows, and that therefore the only thing established is domination, not exact coincidence; the Q component of the complete endpoints remains uncontrolled, as the draft itself admits. This discrepancy was not resolved by another member.

3. ABANDONED — The assertion of step 3 of exact coincidence between Schur’s P norm (6)–(8) and the \(\ell^2_{\rm tilt}\) norm of the complete endpoints, in the written form, is abandoned. Also abandoned is any reading that derives from Parseval that the Q component is controlled or that Schur (8) controls the total norm of the flat endpoints. Not abandoned: the \(O(N^{-3})\) bound in \(\ell^2_{\rm tilt}\), the domination \(\|P\mathfrak A_f\|_{L^2}\le\|f\|_{\ell^2_{\rm tilt}}\), or the draft’s declaration of no transfer to two channels and to \(r_c\).

4. OUTSTANDING — To close what remains open, the following would be needed: the literal text of Schur (6)–(8), with the exact definition of \(P\), \(Q\), \(\|\cdot\|_*\), the windows, the measure, and the normalization, so that it can be decided whether the P norm of the endpoints is literally \(\|\mathfrak A_f\|_{L^2(d\mu)}\) on the complete embedding \((f,0)\), with \(P\) equal to the identity on that range and without multiplying by \(\Lambda\); prove that \(f=s_Nb_N\chi\) and \(w=h_BM_Br\) lie in the range of \(P\) with \(\|P\mathfrak A_f\|=\|\mathfrak A_f\|\), or accept the repair of downgrading step 3 to domination and expressly excluding the Q component; and an adversarial review of steps 1 and 2 and of that repair by a member other than ABNER, since GEMINI did not manage to issue a turn.

## Resultado operativo

- Estado: `DEGRADED_NO_CONSENSUS`
- Turnos con fallo, cuota, ausencia o respuesta corta: 2
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-25T08:34:44Z` |
| Finished (UTC) | `2026-09-25T08:42:38Z` |
| Wall clock | 0h 7m 54s |
| Command | `sanedrin -r 1 -m abner,gemini -i es -p 1600 -t 900 -q 1 -R /home/ignac/sanedrin/reglas/base.md -c debates/2026-09-25--flat-endpoint-l2-n3-derivation-DRAFT.md -c papers/ir-corona/ir-corona.tex -c reports/2026-09-17--regional-laplace-coefficient-gate.md -c reports/2026-09-17--scaled-ir-signaling-gate.md -c reports/2026-09-24--h1c-return-kernel-schur-audit.md -c reports/2026-09-24--h1c-exact-dyson-decomposition.md -c reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md -c /tmp/claude-1000/-home-ignac-qca-causal-cones/3c111a78-8f97-4e46-a059-6b4da58da570/scratchpad/state/CURRENT_STATE.md -o debates/2026-09-25--flat-endpoint-l2-n3-review.md debates/2026-09-25--flat-endpoint-l2-n3-review-request.md` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-25T08:40:42Z | 1 | ABNER | api.deepseek.com/deepseek-v4-pro | 358 | 505 | ok |
| 2026-09-25T08:40:45Z | 1 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 3 | 43 | FAILED |
| 2026-09-25T08:41:05Z | Residuo | ABNER | api.deepseek.com/deepseek-v4-pro | 20 | 144 | ok |
| 2026-09-25T08:41:08Z | Residuo | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 3 | 43 | FAILED |
| 2026-09-25T08:41:46Z | Veredicto | ABNER | api.deepseek.com/deepseek-v4-pro | 38 | 449 | ok |
| 2026-09-25T08:42:38Z | Veredicto | ABNER | api.deepseek.com/deepseek-v4-pro | 52 | 445 | ok |

Turns: 6 · failed: 2 · model time: 7m 54s

Full log: `2026-09-25--flat-endpoint-l2-n3-review.log`
