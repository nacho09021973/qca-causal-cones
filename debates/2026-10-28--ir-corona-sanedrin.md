---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-10-28 14:31
proyecto: /home/ignac/qca-causal-cones
tema: debates/2026-10-28--ir-corona-sanedrin-request.md
rondas: 2
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - ASTRA — GPT (OpenAI) — codex exec -m gpt-6-astra (sellado)
  - CIRO — Grok (xAI) — grok --model grok-4.6 (sellado)
  - ABNER — DeepSeek — api.deepseek.com/deepseek-v4-pro
  - GEMINI — Google — generativelanguage.googleapis.com/gemini-3.1-pro-preview
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

# Sanedrín: ¿está el paper de la corona listo para enviarse?

Solicitud del P.I. (2026-10-28): «lanza el sanedrín con el paper de la corona».

## Objetivo

Atacar las afirmaciones centrales de `papers/ir-corona/ir-corona.tex` (adjunto, versión
autoritativa) antes de decidir si se envía como preprint. El manuscrito se escribió con ayuda de
Claude; por eso este sanedrín no incluye ningún miembro de esa familia.

## Qué se pide atacar

1. **Corrección del resultado principal (Theorem 4.3, leading asymptotics).** ¿Hay algún paso
   del análisis de punto de silla, de la unicidad del minimizador regional que fija
   `K_* ≈ 0.1905`, del exponente `N^{-13/2}` o del coeficiente `C(θ)` que no esté justificado o
   que dependa de una hipótesis no declarada? La no anulación de `C(θ)` se certifica con
   aritmética de intervalos: ¿qué cubre exactamente ese certificado y qué no?
2. **Theorem 4.1 (cota explícita) y 4.2 (tasa regional).** La parte no asintótica de 4.1 está
   formalizada en Lean (README adjunto, con lo que *no* se formaliza). ¿Es coherente lo que el
   paper atribuye a Lean con lo que el README dice que se demostró?
3. **Novedad.** El párrafo de novedad (sección 1) afirma ser «the first prefactor-level
   asymptotic, with a leading coefficient that is oscillatory and certified to be non-vanishing,
   for an infrared-controlled operational response in the strictly outside-propagation-region
   regime of a three-dimensional multi-component quantum walk». ¿Es defendible y
   suficientemente estrecho frente a la literatura de grandes desviaciones de paseos cuánticos,
   ACSV (Pemantle–Wilson) y la desigualdad de Bernstein (trabajo previo reconocido en la nota
   adjunta)? Si conocéis un resultado previo concreto que lo cubra, citadlo con autores, año y
   título; marcad como no verificado lo que no podáis asegurar.
4. **Lectura física.** ¿Se sigue del teorema la conclusión «the emergent cone is not
   operationally sharp, even for infrared-admissible operations»? ¿Es la definición de
   admisibilidad infrarroja razonable o está hecha a medida del resultado?

## Resultado esperado

Cada miembro termina con un veredicto de esta lista y nada más:

- `ENVIABLE`: ningún cambio obligatorio.
- `ENVIABLE_CON_REPARACIONES`: con una lista numerada de reparaciones **obligatorias**, separada
  de las sugerencias **opcionales**.
- `NO_ENVIABLE`: con el defecto que lo impide, localizado (sección, ecuación o teorema).

Cada objeción debe señalar el lugar exacto del paper. Lo que no se pueda comprobar con el material
adjunto se marca `[NO VERIFICADO]`.

## Límites y cierre

- Máximo **2 rondas**. Se cierra con los veredictos finales de la segunda ronda.
- Sólo cuenta como fuente lo adjunto: el `.tex`, `formal/README.md` y `sources/README.md`.
- El resultado no autoriza nada: no se envía el paper ni se cambia `CURRENT_STATE.md` sin decisión
  del P.I. Las reparaciones que se acepten se harán en commits aparte.

## Contexto

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
bound $\delta(N)\le 36N^4e^{-JN}$ with $J=(1-\sqrt3/2)\log 2$.  For the twelve
Pauli encoder--detector pairs of a concrete family, it has the exact leading
asymptotics
\[
\delta(N)=\bigl|C(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad \theta_N=\{\sqrt3N/4\}.
\]
Here $K_*\approx0.1905$ is the value of a Legendre rate function at a unique
regional minimiser.  The coefficient $C(\theta)$ is given in closed form, and
interval arithmetic shows that it does not vanish for any $\theta$ in any of
these pairs; four further pairs with $M=I$ serve as reference controls.  The emergent cone is therefore not operationally sharp,
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
\item \emph{Leading asymptotics} (Theorem~\ref{thm:main}).  For the twelve
  Pauli encoder--detector pairs ($M\ne I$; the four pairs with $M=I$ are
  reference controls),
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

Throughout, the operational claim concerns the twelve Pauli pairs,
$M\in\{\sigma_1,\sigma_2,\sigma_3\}$.  The four pairs with $M=I$ are
included as reference controls.  Theorem~\ref{thm:main} and
Table~\ref{tab:C} cover all sixteen pairs.

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
certified by interval arithmetic (Appendix~\ref{app:numerics}).  Rows with
$M=I$ are reference controls.}
\label{tab:C}
\end{table}

\begin{corollary}\label{cor:suppressed}
In this protocol the emergent light cone is not operationally sharp for
infrared-admissible operations.  For each of the twelve Pauli pairs the response is
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

### Contexto adjunto: formal/README.md
```
# Lean formalization of Theorem 4.1 (explicit upper bound)

Lean 4 (`v4.31.0`) + Mathlib (`v4.31.0`, rev `fabf563`).  Machine-checks the
**non-asymptotic** part of `papers/ir-corona/ir-corona.tex`: the explicit
bound of Theorem 4.1, for every `N ≥ 2`.  No `sorry`; the main theorems
depend only on the standard axioms `propext`, `Classical.choice`, `Quot.sound`
(`#print axioms`).

## Build

```sh
cd formal
lake exe cache get   # prebuilt Mathlib
lake build
```

## What is proved

| Lean | Paper | Statement |
| --- | --- | --- |
| `Ssym`, `kernel` (`Symbol.lean`) | eq. (2), (3) | the symbol `S(p)` as a 2×2 matrix of Laurent polynomials; `G_N(d)` = coefficient of `e^{ip·d}` in `S^N` |
| `gauge_mul_le` (`Ellipse.lean`) | Lemma 5.1 | `E_a E_c ⊆ E_{ac}` for confocal ellipses, in gauge form, for all `a, c > 1` |
| `norm_le_four_of_gauge` | Lemma 5.2 (use) | if `l m = 1` and `(l+m)/2 ∈ E_{17/8}` then `‖l‖ ≤ 4` |
| `pow_succ_eq`, `norm_pow_entry_le` (`Chebyshev.lean`) | Lemma 5.3 (replaced) | `T^{n+1} = h_n T − h_{n−1} I` for unimodular 2×2 `T`, with no spectral gap needed |
| `det_Tz`, `trace_Tz`, `norm_Tz_tilt_pow_le` | proof of Thm 4.1 | at every tilted point `z = 2w`, `‖w_j‖ = 1`: `det = 1`, `f ∈ E_{17/8}`, `‖(T^N)_{ij}‖ ≤ (33/32) N 4^N` |
| `dft_coeff` (`Kernel.lean`) | eq. (11), contour shift | exact recovery of a box-supported Laurent coefficient from its values at `2ζ^k`, with `ζ` a root of unity (a finite DFT; no integrals) |
| `kernel_entry_bound` | proof of Thm 4.1 | `‖G_N(d)_{ij}‖ ≤ (33/32) N 4^N 2^{-(d₀+d₁+d₂)}` for all `d` |
| `sum_sub_ge` (`Theorem41.lean`) | eq. (6) | `u·(y−x) ≥ (3 − √3/2) N` on `𝒜_N × ℬ_N` |
| `kernel_bound_regions` | Thm 4.1 | `‖G_N(y−x)_{ij}‖ ≤ (33/32) N e^{−JN}`, `J = (1 − √3/2) log 2` |
| `card_regA_le`, `card_regB_le` | §3.1 | each region has at most `N³` sites (`N ≥ 2`) |
| `TN_bound` | Thm 4.1 | `‖P_ℬ S^N P_𝒜 ψ‖ ≤ 4 N⁴ e^{−JN} ‖ψ‖`, i.e. `T_N ≤ 4N⁴e^{−JN}` (stronger than the paper's `9N⁴e^{−JN}`) |
| `delta_le_four_T` | Thm 4.1 | `|⟨v₁,Ev₁⟩ − ⟨v₀,Ev₀⟩| ≤ 4T` when `‖v_b‖ ≤ 1`, `‖E‖ ≤ 1`, `‖v₁−v₀‖ ≤ 2T` |

The Lean proof of the power bound differs from the paper: it uses
Cayley–Hamilton with the complete homogeneous polynomials `h_n(λ, λ⁻¹)` and
entrywise bounds, instead of a Schur form and `Σ‖S_d‖ = 4`.  This yields the
sharper constant `4` in place of `9`.

## Statement apart from proof (`QcaComparator`)

To know what is claimed, read only `QcaComparator/Challenge.lean`. It imports
Mathlib and nothing from `QcaFormal`, restates the definitions it needs
(`Ssym`, `kernel`, `regA`, `regB`, `Kop`, `l2sq`) and states `TN_bound` and
`delta_le_four_T` as `Prop`s. `QcaComparator/Solution.lean` proves them with
the `QcaFormal` theorems, so it compiles only if the restated definitions unfold
to the originals. `QcaComparator/Axioms.lean` fails the build unless both
depend on exactly `propext`, `Classical.choice`, `Quot.sound`, using
`#assert_standard_axioms` from `QcaComparator/AssertAxioms.lean` (a copy of
`~/herramientas/lean/HerramientasLean/AssertAxioms.lean`, commit in its header).

Pattern and tooling: `~/herramientas/lean/README.md`, after `Comparator/` in
AxiomMath/CFSG (commit `69cb972`).

Mutation checks are versioned in `QcaComparator/mutaciones.toml` and run with
`lean-mutar formal formal/QcaComparator/mutaciones.toml --salida <record>` from
the repo root; records are in `QcaComparator/registros/`. Each mutation (the two
statements, the copied `regA` and `Ssym`, a `sorry`) must be rejected with the
expected error. With the default heartbeat limit the `regA` mutation was a
`whnf` timeout instead of a type mismatch, hence `maxHeartbeats 1000000` on
`tn_bound`.

## What is not formalized

* The identification `v₁ − v₀ = P_ℬ S^N P_𝒜 (U − I)ψ` with `‖(U − I)ψ‖ ≤ 2`, and
  the second-quantized trace distance `D_B`.  Both are one-line modelling
  steps; only the one-particle signal `δ` is covered through
  `delta_le_four_T`.
* Theorem 4.2 (the rate `K_*`, its uniqueness, and `J < K_* < log 4`),
  Theorem 3.3 (admissibility) and Theorem 4.3 (the leading asymptotics).
  Mathlib lacks the multidimensional Laplace method, lattice Poisson
  summation and analytic perturbation theory that Theorem 4.3 needs.
  Those parts rely on the paper's proofs, the independent review and the
  certificate scripts.

## Found while formalizing

The paper's Lemma 2.1 listed the axial jumps as `(0,0,±1)`; they are
`(±1,0,0)` (from `−i s₁` in the off-diagonal entries).  This is corrected in
the paper; nothing downstream depended on it.
```

### Contexto adjunto: sources/README.md
```
# Sources

Primary sources currently relevant to the freeze.

## Pavia QCA program

1. **A. Bisio, G. M. D'Ariano, P. Perinotti, A. Tosini**  
   *Weyl, Dirac and Maxwell Quantum Cellular Automata: analytical solutions and phenomenological predictions of the Quantum Cellular Automata Theory of Free Fields*  
   arXiv:1601.04842  
   https://arxiv.org/abs/1601.04842

2. **A. Bisio, G. M. D'Ariano, P. Perinotti, A. Tosini**  
   *Free quantum field theory from quantum cellular automata: derivation of Weyl, Dirac and Maxwell quantum cellular automata*  
   arXiv:1601.04832  
   https://arxiv.org/abs/1601.04832

3. **G. M. D'Ariano, P. Perinotti**  
   *Quantum cellular automata and free quantum field theory*  
   arXiv:1608.02004  
   https://arxiv.org/abs/1608.02004

## Bernstein background

The scalar/trigonometric Bernstein derivative inequality and equality theory are classical background and must not be presented as project novelty.

A separate prior-art audit should eventually record the exact primary references used for:

- trigonometric Bernstein inequality;
- Riesz interpolation formula;
- equality/extremal cases;
- matrix/Laurent extensions genuinely relevant to unitary Bloch symbols.

## Checked inputs for the exact battery — 2026-09-14

The local `1601.04832v1.pdf` is the 10-page primary source above, downloaded
without transformation from `https://arxiv.org/pdf/1601.04832v1` (583334 bytes).
SHA256: `0dbf0a0bea497701e0408ce410d62ca0183a4aa14b4116254d029ff6602f1367`.
Its title and authors were checked against the first page; equations (15)-(17)
on p.6 and (20), (23)-(28) on p.7 were read, including visual PDF inspection.

Reacquisition and manual inspection commands, from the repository root:

```sh
curl -fL --retry 2 https://arxiv.org/pdf/1601.04832v1 -o sources/1601.04832v1.pdf
sha256sum sources/1601.04832v1.pdf
pdfinfo sources/1601.04832v1.pdf
pdftotext -f 6 -l 7 -layout sources/1601.04832v1.pdf -
```

The Dirac dagger was cross-checked against
[1601.04842v1, equation (9)](https://arxiv.org/html/1601.04842v1#S2.E9);
its equations (4), (7), (8) also display the Weyl inputs.
See the [analytic report](../reports/2026-09-14--weyl-dirac-exact-gate.md)
for the relevant sign, dagger, and fixed-mass expansion issues. The verifier
uses the declared unitary matrices, not the inconsistent prose phase sign or
the block with the missing dagger. No general literature/novelty audit is claimed.

## Source discipline

Do not cite this file as evidence for a mathematical claim. It is only an index. Before promoting a claim to `ESTABLISHED`, verify it against the primary source and record the exact equation/theorem location in a report or derivation note.
```


## Ronda 1 — ASTRA

[RECONSTRUCTION] La versión más fuerte de la tesis es una existencia asintótica: para operaciones concretas que satisfacen la definición de admisibilidad, la diferencia de probabilidades es estrictamente positiva para todo \(N\) suficientemente grande. No exige observabilidad, un umbral efectivo ni una respuesta positiva en el límite. Su soporte decisivo es la identificación del coeficiente mediante dos contribuciones de silla; certificar que una fórmula no se anula sólo sirve si esa fórmula es efectivamente el coeficiente del observable.

[INFERENCE] La objeción principal está en §7, lema «Layers», apartado (b): la expansión de \(\mathfrak B_w\) exige una proporcionalidad vectorial exacta que es falsa. Se escribe
\[
\mathfrak B_w(\eta)=N^{-5/2}\frac{32}{\sqrt3}
R_0(w_*)^\dagger M_B\,[\mathcal S_++\mathcal E_B],
\]
con \(\mathcal E_B\) escalar. Esto obliga a que toda la fila \(\mathfrak B_w(\eta)\), incluida su corrección, pertenezca a una única recta del espacio interno para cada \(\eta\) del entorno. Una aproximación de la dirección del espinor no implica esa identidad.

[INFERENCE] Puede comprobarse el defecto por dos vías complementarias. Para \(M_B=I\), aplicar a esa identidad un vector columna anulado por \(R_0(w_*)^\dagger\) daría cero para todo \(\eta\) de un abierto. Como \(\mathfrak B_w\) es una suma finita de exponenciales, la independencia de sus frecuencias obligaría a que cada \(r(y)^\dagger\), donde \(h_N(y)>0\), fuese proporcional a \(R_0(w_*)^\dagger\). Pero el propio lema «The free tail» impide esa conclusión: en puntos interiores con coordenadas macroscópicas \(w=u+\varepsilon(1,-1,0)\), para \(\varepsilon\) pequeño y no nulo, la componente superior de \(R_0(w)\) es proporcional a \(w_1+iw_2\), mientras que la inferior es real y positiva. No tiene la misma dirección compleja que \(R_0(w_*)\), cuya componente superior tiene partes real e imaginaria iguales. La aproximación uniforme del lema transfiere esta incompatibilidad a la supuesta proporcionalidad para todos los \(N\) grandes.

[INFERENCE] Esto refuta el lema tal como está escrito, no el exponente \(13/2\) ni necesariamente el teorema principal. La condición de concesión es sustituir la corrección escalar por una fila residual:
\[
\mathfrak B_w(\eta)=N^{-5/2}\frac{32}{\sqrt3}
\left[R_0(w_*)^\dagger M_B\,\mathcal S_+
+\mathbf E_B(\eta,N)\right],
\qquad
\|\mathbf E_B\|\le C(N^{-1/2}+|\eta_n|),
\]
y demostrar esa cota uniformemente en \(\theta_N\), también en la contribución de \(\pi u\). Insertada en «Assembly», esta reparación permitiría conservar el presupuesto \(O(N^{-7})\); debe verificarse mediante normas, sin factorizar artificialmente la dirección del espinor.

[INFERENCE] Hay además un error comprobable en la interpretación de los coeficientes: \(\overline C\) no es, en general, el **promedio** anunciado en el pie de la tabla. Las propias series de «Depth sums» dan
\[
\int_0^1\Gamma_+(\theta)\,d\theta
=\int_{\mathbb R^2}e^{-q_t|\tau|^2}
\sum_{n\in\mathbb Z}|\hat g_\tau(2\pi n)|^2\,d^2\tau
>\overline\Gamma,
\]
y el promedio de \(\Gamma_-\) es estrictamente positivo. Para \((M,M_B)=(\sigma_2,P_3)\), el apéndice da \(\ell_0=\ell_\pi<0\): ambas correcciones tienen el mismo signo y no pueden cancelarse. Por tanto, el promedio de \(C\) difiere de \(\mathcal Kc_r\overline\Gamma\ell_0\). Condición de concesión: llamar a este último «coeficiente de referencia», conservando las cotas respecto de esa referencia, o calcular el promedio verdadero y actualizar las afirmaciones correspondientes.

[UNVERIFIED] La ejecución y corrección de los certificados de intervalos no se han comprobado: sólo está adjunta su descripción. Tampoco se han leído las fuentes originales necesarias para resolver la prioridad bibliográfica.

[INFERENCE] Veredicto provisional: `ENVIABLE_CON_REPARACIONES`. Reparaciones obligatorias:

1. [INFERENCE] Corregir el residuo vectorial de «Layers» y comprobar su propagación en «Assembly».
2. [INFERENCE] Corregir la identificación de \(\overline C\) como promedio y cualquier interpretación que dependa de ella.

## Ronda 1 — CIRO

Concuerdo con ASTRA en la tesis fuerte (existencia asintótica para una familia concreta, no observabilidad) y en las dos reparaciones que formula: el lema Layers (b) está mal escrito y «Mean» en la Tabla 1 no es un promedio. No suscribo que eso refute el teorema principal.

[INFERENCE] El defecto vectorial está localizado. En Layers (b), \(\mathfrak A_f\) sí es proporcional al espinor fijo \(\chi\), porque la fuente es \(s_N\varphi_N\chi\); \(\mathcal E_A\) escalar es admisible. Sólo \(\mathfrak B_w\) es falso tal como está: \(w=h_N M_B r\) y \(R_0(y/N)\) gira con \(y\). En las capas de profundidad \(O(1)\), \(|u_\perp|=O(\sqrt N)\), luego \(y/N=w_*+O(N^{-1/2})\). Por la suavidad de \(R_0\) en \(w_*\) (\(\rho_*=\sqrt3-1/4\neq0\), lema del free tail), el error es una fila \(\mathbf E_B\) del tamaño que ASTRA pide, no un término a la misma orden que \(\mathcal S_\pm\). Insertado en Assembly, reproduce el \(O(N^{-7})\) ya presupuestado. Condición de concesión: si esa cota uniforme en \(\theta_N\) (y en \(\pi u\)) se escribe con normas, \(C(\theta)\) queda identificado por el valor en \(w_*\) y el certificado de no anulación no se cae.

[SOURCE] El certificado, según el Apéndice, cubre identidades del símbolo, recintos de \(t_*\), \(K_*\), \(q_t\), \(q_n\), \(\mathcal I_0\), \(\mathcal I_1\), \(\varphi_\partial\), \(\cK\), \(\overline\Gamma\), \(\varepsilon_\pm\), los dieciséis pares \((\ell_0,\ell_\pi)\) y la desigualdad \(|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|\). No cubre la ejecución de los scripts ([UNVERIFIED]), ni el resto analítico de 4.3, ni que Layers-como-está iguale esa fórmula, ni un \(N_*\) efectivo. Para \(M=\sigma_2\) la no anulación es anterior al margen (Remark features), porque \(\ell_0\) y \(\ell_\pi\) tienen el mismo signo.

[SOURCE] Lean y el Remark de 4.1 son coherentes. El README demuestra \(T_N\le4N^4e^{-JN}\) y \(\delta\le4T\) bajo \(\|v_b\|\le1\), \(\|E\|\le1\), \(\|v_1-v_0\|\le2T\); no formaliza la identificación \(v_1-v_0=P_{\mathcal B}S^NP_{\mathcal A}(U-I)\psi\) ni \(D_B\). El paper lo declara y retiene la constante 9 de Schur. 4.2 y 4.3 no están en Lean, como dice el README.

[INFERENCE] El minimizador regional de 4.2 es el argumento estándar de hiperplano: en \(V_{\mathrm{reg}}\) se tiene \(\hat u\cdot v\ge\sqrt3-1/2=|v_*|\), con igualdad sólo en \(v_*\). \(J<K_*\) se reduce a \(\operatorname{arcosh}(125/64)<\log4\), i.e. \(125/64<17/8\). Eso no depende de intervalos. Los valores numéricos de \(t_*\) y \(K_*\) sí ([UNVERIFIED] los recintos). El recuento \(N^{-13/2}\) es algebraicamente consistente con los prefactores de Layers y con \(\cK\).

[ABSENCE] En lo adjunto no hay un resultado previo que cubra la conjunción del párrafo de novedad (prefactor operacional IR, coeficiente oscilatorio certificado, corona estricta, 3D, multicomponente). Sunada–Tate y CRT son 1D y de probabilidades de transición; BBBP es 2D en la región factible; CJWW da tasas, no prefactores; ACSV no se invoca como teorema de transferencia. No he leído esas fuentes ([UNVERIFIED]). La frase es estrecha hasta casi no falsificable; no es un defecto de corrección. Bernstein, en `sources/README.md`, no está reclamado como novedad aquí.

[INFERENCE] Del teorema se sigue que, en este protocolo, \(\delta_{M,M_B}(N)>0\) para \(N\) grande. No se sigue que toda operación IR-admisible señalice, ni que el cono no sea agudo «en general». El corolario restringe a «this protocol»; el abstracto no: «The emergent cone is therefore not operationally sharp, even for infrared-admissible operations». Condición de concesión: leer esa frase como existencia, y escribirlo así.

La admisibilidad no está hecha a medida del coeficiente. Prohíbe puertas puntuales (lema Single-site) y es el recinto natural de perfiles Lipschitz \(O(1/N)\) (lema IR1 da fuga \(N^{-1/2}\)). El par \((\Lambda,\Lambda')\) está ajustado a lo que esas operaciones consiguen; es modelización declarada, no hipótesis oculta de 4.3. El fenómeno lineal en \(e^{-K_*N}\) exige la cola polinomial del paquete (Paley–Wiener del bump), interferida con el núcleo de la corona; el paper lo dice. Sin cola libre el signo iría en \(e^{-2K_*N}\). Eso no trivializa (I): si el núcleo se anulara en la corona, \(L=0\).

`ENVIABLE_CON_REPARACIONES`

Obligatorias:
1. Residuo vectorial en Layers (b) y su paso a Assembly, como ASTRA.
2. Dejar de llamar promedio a \(\overline C=\cK c_r\overline\Gamma\ell_0\); cotas respecto de esa referencia.
3. En abstracto (y, si se mantiene el «therefore», en la lectura física), restringir la no-agudeza a la familia.

Opcionales: acortar la novedad; archivar `Repo` (el TODO del bibitem); alinear la constante 9 con la 4 de Lean; no proyectar espectralmente la señal ya está en §3, puede subrayarse.

## Ronda 1 — ABNER

Concuerdo con ASTRA y con CIRO en que el residuo vectorial de Layers(b) y el falso “promedio” de la Tabla 1 son reparaciones obligatorias, y en que ninguna de las dos derriba por sí sola el Theorem 4.3. Añado un defecto distinto, localizado en la misma sección asintótica.

[SOURCE] En la prueba de Lemma Layers, apartado (d), el texto dice: “by Lemma symbol(c), the character is non-trivial on each plane. The Poisson sum therefore has no \(m=0\) term, and the remaining terms are \(O(N^{-4})\).”

[INFERENCE] Ese “therefore” es falso. Para una suma sobre el plano \(\Lambda_0\) con fase \(e^{i(\eta_{0,t}+\eta_t)\cdot u}\), la fórmula de Poisson da
\[
\sum_{u\in\Lambda_0} g(u)e^{i(\eta_{0,t}+\eta_t)\cdot u}
=
\frac1{\operatorname{vol}(\Lambda_0)}
\sum_{m\in\Lambda_0^*}\hat g(\eta_{0,t}+\eta_t+2\pi m).
\]
El término \(m=0\) es \(\hat g(\eta_{0,t}+\eta_t)\), no \(\hat g(0)\). La no trivialidad del carácter no anula ese término; simplemente desplaza el argumento de la transformada a un vector fijo no nulo. Para los seis puntos de \(\Sigma\setminus\{0,\pi u\}\), \(\eta_{0,t}\) es fijo y de orden \(1\), de modo que \(\hat g(\eta_{0,t}+\eta_t)\) es una integral no estacionaria, no una integral de un carácter sobre un periodo.

[INFERENCE] El resultado \(O(N^{-4})\) puede ser verdadero, pero exige una estimación distinta: integración por partes en la integral no estacionaria con frecuencia fija \(\eta_{0,t}\), uniforme en \(\eta_t\) cerca de cero. Esa estimación no está escrita. Condición de concesión: exhibir la cota de \(\hat g(\eta_{0,t}+\eta_t)\) en la escala de las capas, o reescribir Poisson con una red desplazada que absorba la fase, y propagar el error en “Assembly”. Si no, el presupuesto que en Assembly asigna \(O(N^{-8})\) a los seis puntos no contribuyentes carece de soporte probado.

[INFERENCE] No afirmo que esto cambie el exponente \(13/2\) ni el coeficiente; sólo que la supresión de los seis puntos está mal justificada tal como está escrita. Una vez reparada, la tesis principal se mantiene.

`ENVIABLE_CON_REPARACIONES`

Reparaciones obligatorias:
1. Residuo vectorial en Layers(b) y su paso por Assembly, como formulan ASTRA y CIRO.
2. Eliminar la identificación de \(\overline C\) como promedio; presentar las cotas respecto de una referencia declarada.
3. Reparar la justificación de Poisson/non-stationary phase en Layers(d), con cota explícita del término \(m=0\) desplazado.

Sugerencias opcionales: no repito las ya formuladas; suscribo la restricción del abstract a la familia concreta señalada por CIRO.

## Ronda 1 — GEMINI

**TURNO FALLIDO.** El backend no completó una respuesta válida. Traza:

```
Gemini: finishReason=MAX_TOKENS; respuesta incompleta o bloqueada
```

## Ronda 2 — CIRO

Suscribo la objeción de ABNER sobre Layers(d). El «therefore» del lema es falso: la no trivialidad del carácter sobre \(\Lambda_0\) no anula el modo \(m=0\); lo desplaza a \(\hat g(\eta_{0,t}+\eta_t)\) con \(\eta_{0,t}\) de orden uno. [SOURCE] Los seis puntos de \(\Sigma\setminus\{0,\pi u\}\) tienen proyección tangencial no nula; [INFERENCE] el término es una integral no estacionaria, no un carácter sobre un periodo. La cota \(O(N^{-4})\) es recuperable por la misma estimación de \(\|\partial^3G_0\|_{\mathcal M}\,|\xi|^{-3}\) ya usada para \(m\neq0\) en Layers(b), y con ella el presupuesto \(O(N^{-8})\) de Assembly se sostiene. No está escrita. No cambia el exponente ni el coeficiente; sí deja sin soporte, tal como está, que \(C(\theta)\) reciba sólo dos sillas.

No hay desacuerdo de fondo con ASTRA: Layers(b) refuta el lema como está escrito, no el Theorem 4.3. [INFERENCE] En las capas de profundidad \(O(1)\), \(y/N=w_*+O(N^{-1/2})\) y la suavidad de \(R_0\) en \(w_*\) (\(\rho_*\neq0\)) da una fila residual del tamaño ya presupuestado. La identidad con \(\mathcal E_B\) escalar es falsa; la fórmula de \(C(\theta)\) por el valor en \(w_*\) se conserva si la cota se escribe con normas, uniforme en \(\theta_N\) y en \(\pi u\).

[SOURCE] \(\overline C=\cK c_r\overline\Gamma\ell_0\) no es el promedio de \(C(\theta)\): las series de Depth sums hacen \(\int\Gamma_+>\overline\Gamma\) y \(\int\Gamma_->0\). Las cotas relativas a esa referencia siguen siendo las del certificado descrito.

Siguen en pie, y no las retiro. [SOURCE] Lean y el Remark de 4.1 coinciden: \(T_N\le4N^4e^{-JN}\) y \(\delta\le4T\) bajo las hipótesis declaradas; no se formalizan la identificación \(v_1-v_0=P_{\mathcal B}S^NP_{\mathcal A}(U-I)\psi\) ni \(D_B\); 4.2 y 4.3 no están en Lean. [INFERENCE] El minimizador regional es el argumento de hiperplano en \(V_{\mathrm{reg}}\); \(J<K_*\) se reduce a \(125/64<17/8\), independiente de intervalos. El recuento \(N^{-13/2}\) es algebraicamente consistente. [SOURCE] El certificado cubre recintos de \(t_*\), \(K_*\), \(\overline\Gamma\), \(\varepsilon_\pm\), los dieciséis pares \((\ell_0,\ell_\pi)\) y el margen de no anulación; [UNVERIFIED] la ejecución de los scripts. [ABSENCE] En lo adjunto no hay un resultado previo que cubra la conjunción del párrafo de novedad. Del teorema se sigue \(\delta>0\) para \(N\) grande en esta familia, no que toda operación IR-admisible señalice. [SOURCE] El corolario restringe a «this protocol»; el abstracto no. La admisibilidad no está hecha a medida del coeficiente: excluye puertas puntuales y acota la fuga Lipschitz.

`ENVIABLE_CON_REPARACIONES`

Obligatorias:
1. Residuo vectorial en Layers(b) y su paso a Assembly.
2. No llamar promedio a \(\overline C\); cotas respecto de esa referencia.
3. Justificar Layers(d) por fase no estacionaria (o red desplazada) con cota del término \(m=0\) desplazado, y cerrar el presupuesto de Assembly.
4. Restringir la no-agudeza del abstracto (y el «therefore» de la lectura física) a la familia del teorema.

Opcionales: las de la ronda 1; no añado otras.

## Ronda 2 — ABNER

Concedo las reparaciones 1–4 y las hago mías sin atenuantes. [SOURCE] En Layers(b) la identidad con \(\mathcal E_B\) escalar es falsa: obliga a que toda la fila viva en una recta del espacio interno, y el propio lema del free tail produce direcciones distintas en puntos interiores de \(\cB_N\). [INFERENCE] La reparación correcta es la fila residual \(\mathbf E_B(\eta,N)\) con cota \(C(N^{-1/2}+|\eta_n|)\), uniforme en \(\theta_N\) y en \(\pi u\), insertada con normas en Assembly; esto conserva el \(O(N^{-7})\) y no cambia \(C(\theta)\) ni el exponente.

[SOURCE] Layers(d) también está mal escrito: la no trivialidad del carácter sobre \(\Lambda_0\) no anula el modo \(m=0\), lo desplaza a \(\hat g(\eta_{0,t}+\eta_t)\) con \(\eta_{0,t}\) de orden uno. [INFERENCE] Es una fase no estacionaria, recuperable con la cota \(\|\partial^3G_0\|_{\mathcal M}|\xi|^{-3}\), pero la estimación no está escrita; sin ella, el presupuesto de Assembly para esos seis puntos carece de soporte. [SOURCE] \(\overline C\) no es el promedio de \(C(\theta)\): las series de Depth sums dan \(\int\Gamma_+>\overline\Gamma\) y \(\int\Gamma_->0\). [INFERENCE] Debe llamarse referencia para las cotas de oscilación, no “mean”. [SOURCE] El abstract y la lectura física afirman no-agudeza sin restringir; [INFERENCE] debe decir “in this protocol” o “for the family of Theorem 4.3”.

No veo objeción central que sobreviva a esas reparaciones. [INFERENCE] La tesis principal, existencia asintótica con coeficiente no nulo para las doce parejas, queda en pie: el defecto de Layers(b) es de escritura de una corrección cuyo tamaño ya estaba presupuestado, y la no anulación no depende de la identidad escalar falsa. [UNVERIFIED] La ejecución de los certificados de Appendix A no se ha podido contrastar con el material adjunto; [INFERENCE] debe ejecutarse y registrarse la traza del commit antes del envío.

Obligatorias:
1. Residuo vectorial en Layers(b) y su paso por Assembly.
2. Renombrar \(\overline C\) como referencia, no promedio.
3. Justificación explícita de fase no estacionaria en Layers(d).
4. Restringir la no-agudeza del abstract y de la lectura física a la familia.
5. Ejecutar y contrastar los certificados de Appendix A y registrar commit/resultado.

Opcionales: suscribo las ya formuladas (acortar novedad, archivar Repo, alinear constante 9 con la 4 de Lean, realzar que la señal no se proyecta espectralmente).

`ENVIABLE_CON_REPARACIONES`

## Ronda 2 — GEMINI

Concedo y suscribo sin reservas las objeciones de ASTRA, CIRO y ABNER. 

1. Suscribo la objeción de ASTRA y CIRO sobre `Layers(b)`. [SOURCE] La afirmación de proporcionalidad exacta con $\mathcal E_B$ escalar es matemáticamente falsa dado que $R_0$ gira. [INFERENCE] La reparación exigida (sustituir por un residuo vectorial $\mathbf E_B(\eta,N)$ acotado en norma) desactiva el ataque porque la cota se preserva a través de la integración en `Assembly`.
2. Suscribo la objeción de ASTRA sobre $\overline C$. [SOURCE] Nombrarlo "promedio" contradice las propias integrales de Gauss aportadas. [INFERENCE] Debe usarse como constante de referencia.
3. Suscribo la objeción de ABNER sobre `Layers(d)`. [SOURCE] El carácter no trivial desplaza el término de Poisson, no lo anula. [INFERENCE] La cota $O(N^{-4})$ requiere la aplicación explícita de integración por partes (fase no estacionaria), sin la cual el error $O(N^{-8})$ presupuestado en la suma final es un salto injustificado en la demostración. 
4. Suscribo la objeción de CIRO sobre el abstract y la sección de lectura física. [SOURCE] Proyectar que el cono emergente no es agudo "even for infrared-admissible operations" enuncia una proposición universal categórica. [INFERENCE] El paso lógico de "funciona en el ejemplo" a "funciona en general" (Regla 6) no está demostrado; la aserción debe ceñirse a la familia de codificadores examinada.

[INFERENCE] El sanedrín ha convergido unánimemente, no por cortesía, sino porque habiendo atacado la versión más fuerte de las estimaciones (el núcleo del análisis de punto de silla en la Sección 7), el teorema asintótico sobrevive a las reparaciones. El recuento que da origen al exponente $13/2$ resiste el escrutinio: la perturbación cúbica de la fase $\exp(-N|\eta|^3)$ evaluada en las coordenadas de integración reescaladas $\eta_n \sim O(N^{-1/2})$, $\eta_t \sim O(N^{-1/2})$ induce exactamente una penalización relativa $O(N^{-1/2})$, lo cual agota los márgenes de error sin comprometer el término principal. Además, la carga de la prueba respecto a la observabilidad está bien delimitada: el autor declara que la asintótica exige $N \gtrsim 10^3$ para dominar, evitando elevar un límite formal a una promesa de detección experimental.

`ENVIABLE_CON_REPARACIONES`

Reparaciones obligatorias:
1. Sustituir en `Layers(b)` el error escalar por un residuo vectorial $\mathbf E_B(\eta,N)$ acotado en norma por $C(N^{-1/2}+|\eta_n|)$, uniformemente en $\theta_N$ y en $\pi u$, y demostrar su correcta inserción en `Assembly`.
2. Eliminar la terminología de "promedio" para $\overline C$ (incluyendo la Tabla 1); redefinirlo como coeficiente de referencia y declarar las cotas de oscilación respecto al mismo.
3. Escribir explícitamente la estimación de fase no estacionaria en `Layers(d)` para el modo desplazado $m=0$, justificando rigurosamente el abandono de los seis puntos del toro no contribuyentes.
4. Restringir la aseveración sobre la falta de agudeza del cono ("not operationally sharp") en el abstract y en la sección de discusión explícitamente al protocolo/familia analizada.
5. Ejecutar los scripts de certificados de intervalos mencionados en el Appendix A, comprobando su consistencia, y registrar el entorno y hash del commit correspondiente antes del envío.

Reparaciones opcionales:
1. Aclarar tempranamente (Sección 3) que la señal de detectabilidad $\delta$ no lleva proyección espectral, para evitar confusiones de modelado.
2. Hacer coincidir la constante del cota superior explícita (el 9 conservador de Schur en el texto frente al 4 exacto verificado formalmente en Lean).
3. Estrechar la afirmación de novedad en el párrafo introductorio.

## Ronda 2 — ASTRA

[INFERENCE] Mantengo las dos reparaciones de mi primera ronda y suscribo la objeción de ABNER sobre «Layers(d)». Concedo que ninguna demuestra que el teorema principal sea falso. Tampoco equivale a demostrarlo afirmar que las reparaciones conservarán el resultado: hay que incorporar las estimaciones corregidas antes de dar por cerrado el argumento.

[INFERENCE] La reparación de «Layers(d)» puede precisarse sin introducir otra técnica. Sea \(a=\eta_{0,t}\) la proyección tangencial de uno de los seis puntos descartados. La no trivialidad del carácter implica
\[
d_0=\operatorname{dist}(a,2\pi\Lambda_0^*)>0.
\]
Escogiendo \(r_0<d_0/2\), todas las frecuencias desplazadas quedan separadas de cero, incluido el término indexado por \(m=0\). Además,
\[
\sup_{|\eta_t|\le r_0}
\sum_{m\in\Lambda_0^*}|a+\eta_t+2\pi m|^{-3}<\infty.
\]
La convergencia corresponde a una red bidimensional y una potencia tres. Esto permite aplicar a **todos** los términos la estimación mediante terceras derivadas que ya propone «Layers(b)».

[INFERENCE] La escala también concuerda: un perfil de amplitud \(N^{-7/2}\) y radio tangencial \(O(\sqrt N)\) tiene norma integrada de tercera derivada de orden \(N^{-4}\), para profundidad fija. Para cerrar la demostración debe expresarse su dependencia en la profundidad mediante una cota sumable con \(e^{-t_*(\theta+j)}\), uniforme en \(\theta\). Ésta es la condición de concesión del ataque: demostrar esa cota y obtener el \(O(N^{-8})\) de «Assembly». La frase «no hay término \(m=0\)» debe sustituirse por «no hay frecuencia cero».

[INFERENCE] Disiento de la reparación obligatoria sobre la lectura física que comparten los otros miembros. La versión fuerte y pertinente de «cono operacionalmente nítido para operaciones admisibles» sería que **ninguna** operación de esa clase produce respuesta fuera del cono. Un solo protocolo admisible con respuesta positiva refuta esa propiedad universal. No exige demostrar que todas las operaciones señalicen. Por tanto, la frase del resumen admite precisamente la lectura existencial que el teorema pretende establecer; calificarla, como hace GEMINI, de ascenso necesario desde un ejemplo a una afirmación universal confunde los cuantificadores.

[SOURCE] El resumen presenta expresamente una familia concreta, y el corolario comienza «In this protocol». La discusión añade que no se afirma respuesta positiva para todo protocolo ni para todo paseo cuántico.

[INFERENCE] Concedería la objeción física si el texto afirmase que toda operación admisible señaliza o que el resultado vale para cualquier paseo. Los pasajes anteriores delimitan lo contrario. Añadir «for this family» al resumen puede mejorar la claridad; no lo considero una reparación matemática obligatoria.

[UNVERIFIED] No he comprobado los scripts ni sus ejecuciones. La no anulación certificada sigue dependiendo de una comprobación computacional cuya descripción, pero no cuya ejecución, está disponible aquí.

[INFERENCE] La coincidencia entre intervenciones no convierte esa comprobación en realizada, ni convierte nuestras deducciones sobre los lemas en tesis explícitas de una fuente. Mantengo las etiquetas de inferencia para los defectos identificados.

[INFERENCE] Reparaciones obligatorias:

1. En §7, «Layers(b)», sustituir el residuo escalar de Bob por una fila residual, demostrar su cota uniforme y propagarla mediante normas en «Assembly», también alrededor de \(\pi u\).
2. En §7, «Layers(d)», justificar la separación de las frecuencias desplazadas y la cota sumable en profundidad que suprime las seis contribuciones restantes.
3. En la tabla y las definiciones correspondientes, presentar \(\overline C\) como coeficiente de referencia, o calcular el promedio verdadero y revisar las cotas asociadas.

[INFERENCE] Sugerencia opcional: explicitar en el resumen el alcance existencial de la conclusión física.

[INFERENCE] `ENVIABLE_CON_REPARACIONES`

## Ronda Residuo — ASTRA

[INFERENCE] Queda en pie una tesis de existencia asintótica que no ha sido refutada; todavía no una demostración cerrada tras esta revisión. Deben corregirse el residuo vectorial de «Layers(b)», la estimación uniforme de frecuencias desplazadas en «Layers(d)» y la identificación de \(\overline C\) como promedio. Esas reparaciones desactivan las objeciones únicamente cuando sus cotas estén demostradas e incorporadas en «Assembly».

[INFERENCE] Debe abandonarse la afirmación de GEMINI de que el teorema ya «sobrevive a las reparaciones»: anticipar que una corrección funcionará no equivale a comprobarla. También disiento de considerar obligatoria la restricción física adicional: una propiedad de ausencia universal de señal queda refutada por un solo protocolo admisible que señalice. Concedería esa objeción si se afirmara que todos los protocolos señalizan; el manuscrito excluye expresamente ese alcance.

[UNVERIFIED] No están verificadas aquí la ejecución de los certificados ni la prioridad bibliográfica. La deliberación no justifica todavía afirmar que la fórmula corregida está íntegramente demostrada y computacionalmente contrastada.

[INFERENCE] `ENVIABLE_CON_REPARACIONES`: condicionado al cierre efectivo de las tres reparaciones, no al acuerdo entre revisores.

## Ronda Residuo — CIRO

Suscribo el residuo de ASTRA. [INFERENCE] Queda en pie la existencia asintótica para la familia concreta, no una demostración cerrada. Deben abandonarse la identidad escalar de Layers(b), el «therefore» de Layers(d), el «mean» de \(\overline C\), y la tesis de GEMINI de que el teorema ya sobrevive a las reparaciones: anticipar una cota no es demostrarla.

Disiento de ABNER y GEMINI en dos puntos. [INFERENCE] Restringir el abstracto no es obligatorio. [SOURCE] El corolario dice «this protocol» y la discusión niega universalidad. [INFERENCE] Un protocolo admisible con \(\delta>0\) refuta la nitidez operacional del cono; concedería si se afirmara que toda operación señaliza. Ejecutar certificados no es reparación del texto. [UNVERIFIED] su traza.

[INFERENCE] No está justificado que las cotas corregidas, insertadas en Assembly, cierren el presupuesto ni que \(C(\theta)\) quede identificado y no nulo tras esa inserción.

`ENVIABLE_CON_REPARACIONES`

## Ronda Residuo — ABNER

[INFERENCE] Queda en pie la tesis de existencia asintótica para la familia concreta; no queda una demostración cerrada. [INFERENCE] Deben abandonarse la identidad escalar de Layers(b), el «therefore» de Layers(d), la denominación «mean» de \(\overline C\), y la afirmación de GEMINI de que el teorema ya sobrevive a las reparaciones. [INFERENCE] No mantengo como obligatoria la restricción adicional del abstract: [SOURCE] el corolario ya dice «this protocol» y la discusión niega universalidad; un solo protocolo admisible refuta la nitidez operacional universal, así que degrada mi objeción a sugerencia. [INFERENCE] Conservo, como condición previa al envío y no como reparación de texto, ejecutar y contrastar los certificados de intervalos. [UNVERIFIED] Esa ejecución no está disponible aquí. [INFERENCE] NO está justificado todavía que las cotas corregidas, insertadas en Assembly, cierren el presupuesto \(O(N^{-7})\) y que \(C(\theta)\) quede identificado y no nulo tras esa inserción. `ENVIABLE_CON_REPARACIONES`, condicionado al cierre efectivo de esas estimaciones.

## Ronda Residuo — GEMINI

[INFERENCE] Concedo a ASTRA y retiro mis dos errores lógicos de la ronda anterior: un solo protocolo admisible con $\delta>0$ basta para refutar la nitidez operacional del cono, por lo que la lectura del resumen es lícita; y anticipar el éxito de una reparación matemática no sustituye su demostración escrita. 

[INFERENCE] Queda en pie la viabilidad de la tesis de existencia asintótica para la familia concreta (Theorem 4.3).

[SOURCE] Debe abandonarse la identidad con residuo escalar en Layers(b), la inferencia que asume la anulación del modo $m=0$ en Layers(d), y la denominación de $\overline C$ como promedio.

[INFERENCE] NO está justificada todavía la demostración del Theorem 4.3. Falta probar explícitamente que la cota de la fila residual en Layers(b) y la estimación de las frecuencias desplazadas en Layers(d) logran propagarse a través de Assembly para cerrar el presupuesto de error $O(N^{-7})$, garantizando la identificación y no anulación de $C(\theta)$ sin alterar el exponente. Adicionalmente, [UNVERIFIED] la ejecución de los certificados de intervalos no está constatada.

ENVIABLE_CON_REPARACIONES

## Ronda Veredicto — ASTRA

1. ACUERDO

[SOURCE] Los cuatro miembros terminan con `ENVIABLE_CON_REPARACIONES`. Sus intervenciones finales coinciden en que la tesis de existencia asintótica para la familia concreta no ha sido refutada, pero la demostración del Theorem 4.3 todavía no queda cerrada.

[SOURCE] Todos aceptan tres reparaciones obligatorias: sustituir el residuo escalar de Bob en «Layers(b)» por una fila residual acotada en norma; justificar en «Layers(d)» la supresión de las seis contribuciones mediante frecuencias desplazadas separadas de cero; y dejar de presentar \(\overline C=\mathcal Kc_r\overline\Gamma\ell_0\) como promedio.

[SOURCE] El acuerdo final es condicional: prever que esas correcciones conservarán el coeficiente y el exponente no equivale a demostrarlo. Deben incorporarse las estimaciones y comprobarse su propagación en «Assembly».

[SOURCE] Tras las retiradas expresas de CIRO, ABNER y GEMINI, todos aceptan que un solo protocolo admisible con respuesta positiva basta para refutar la ausencia universal de respuesta fuera del cono. La aclaración adicional del resumen queda como sugerencia, no como reparación matemática obligatoria.

2. DESACUERDO VIVO

[SOURCE] No queda una discrepancia matemática explícita entre las intervenciones finales sobre las tres reparaciones ni sobre los cuantificadores de la conclusión física.

[RECONSTRUCTION] Subsiste una diferencia de exigencia procedimental respecto de los certificados: ABNER mantiene expresamente su ejecución y contraste como condición previa al envío; GEMINI los había incluido entre las obligaciones y termina señalando que no están constatados. ASTRA registra esa falta de verificación sin formular una obligación adicional; CIRO distingue ejecutar certificados de reparar el texto. Estas posiciones no establecen una oposición entre ejecutar y no ejecutar: el carácter obligatorio de ese control no recibió una resolución común explícita.

3. ABANDONADO

[INFERENCE] Quedan descartadas la proporcionalidad vectorial exacta impuesta por el residuo escalar de «Layers(b)», la supuesta desaparición del término indexado por \(m=0\) en «Layers(d)» y la identificación general de \(\overline C\) con el promedio de \(C(\theta)\). El diagnóstico sobre Poisson distingue ausencia de frecuencia cero de ausencia de un término con determinado índice.

[SOURCE] GEMINI retira expresamente que la conclusión física cometa necesariamente una generalización injustificada y que pueda darse por demostrado que el teorema «sobrevive» a reparaciones todavía pendientes. CIRO y ABNER también retiran la obligatoriedad de restringir adicionalmente el resumen.

[SOURCE] ASTRA mantiene sus dos objeciones iniciales y concede expresamente que ninguna refuta por sí misma el teorema principal.

4. PENDIENTE

[INFERENCE] Para cerrar «Layers(b)» hace falta demostrar la cota de la fila residual, uniforme en \(\theta_N\), alrededor de ambas contribuciones relevantes, y obtener mediante normas el error \(O(N^{-7})\) en «Assembly».

[INFERENCE] Para cerrar «Layers(d)» hace falta justificar la separación uniforme de todas las frecuencias desplazadas, controlar las terceras derivadas con dependencia en profundidad sumable bajo el peso exponencial y deducir la contribución \(O(N^{-8})\) de los seis puntos restantes.

[INFERENCE] Debe renombrarse \(\overline C\) como referencia o calcularse el promedio verdadero y revisarse las cotas correspondientes.

[UNVERIFIED] La ejecución de los certificados y la prioridad bibliográfica no están comprobadas en esta deliberación. Su cierre requiere, respectivamente, contrastar código y resultados identificados por commit, y leer las fuentes primarias pertinentes. El acuerdo entre miembros no sustituye ninguna de esas comprobaciones.

## Ronda Veredicto — ASTRA

1. AGREEMENT

[SOURCE] All four members conclude with `ENVIABLE_CON_REPARACIONES`. Their final interventions agree that the asymptotic existence thesis for the specific family has not been refuted, but the proof of Theorem 4.3 is still incomplete.

[SOURCE] All accept three mandatory repairs: replace Bob’s scalar residual in “Layers(b)” with a residual row bounded in norm; justify in “Layers(d)” the suppression of the six contributions through shifted frequencies bounded away from zero; and stop presenting \(\overline C=\mathcal Kc_r\overline\Gamma\ell_0\) as an average.

[SOURCE] The final agreement is conditional: expecting those corrections to preserve the coefficient and exponent is not equivalent to proving it. The estimates must be incorporated and their propagation through “Assembly” checked.

[SOURCE] Following the explicit withdrawals by CIRO, ABNER, and GEMINI, all accept that a single admissible protocol with a positive response suffices to refute the universal absence of response outside the cone. The additional clarification in the abstract remains a suggestion, not a mandatory mathematical repair.

2. LIVE DISAGREEMENT

[SOURCE] No explicit mathematical discrepancy remains among the final interventions regarding the three repairs or the quantifiers in the physical conclusion.

[RECONSTRUCTION] A difference in procedural requirements concerning the certificates persists: ABNER explicitly maintains that running and checking them is a prerequisite for submission; GEMINI had included them among the obligations and concludes by noting that they have not been verified. ASTRA records that lack of verification without formulating an additional obligation; CIRO distinguishes running certificates from repairing the text. These positions do not establish an opposition between running and not running them: whether that check is mandatory received no explicit joint resolution.

3. ABANDONED

[INFERENCE] The exact vector proportionality imposed by the scalar residual in “Layers(b),” the supposed disappearance of the term indexed by \(m=0\) in “Layers(d),” and the general identification of \(\overline C\) with the average of \(C(\theta)\) are ruled out. The diagnosis concerning Poisson distinguishes the absence of zero frequency from the absence of a term with a particular index.

[SOURCE] GEMINI explicitly withdraws the claims that the physical conclusion necessarily commits an unjustified generalization and that the theorem can be considered proven to “survive” repairs that are still pending. CIRO and ABNER also withdraw the requirement to restrict the abstract further.

[SOURCE] ASTRA maintains its two initial objections and explicitly concedes that neither, on its own, refutes the main theorem.

4. OUTSTANDING

[INFERENCE] Completing “Layers(b)” requires proving the bound on the residual row, uniformly in \(\theta_N\), around both relevant contributions, and obtaining the \(O(N^{-7})\) error in “Assembly” through norms.

[INFERENCE] Completing “Layers(d)” requires justifying the uniform separation of all shifted frequencies, controlling the third derivatives with depth dependence that is summable under the exponential weight, and deriving the \(O(N^{-8})\) contribution of the six remaining points.

[INFERENCE] \(\overline C\) must be renamed as a reference, or the true average must be calculated and the corresponding bounds revised.

[UNVERIFIED] The execution of the certificates and bibliographic priority have not been verified in this deliberation. Resolving these requires, respectively, checking code and results identified by commit, and reading the relevant primary sources. Agreement among members replaces neither of those checks.

## Resultado operativo

- Estado: `DEGRADED_NO_CONSENSUS`
- Turnos con fallo, cuota, ausencia o respuesta corta: 1
- Miembros solicitados ausentes desde el inicio: 0
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-10-28T13:31:20Z` |
| Finished (UTC) | `2026-10-28T14:06:05Z` |
| Wall clock | 0h 34m 45s |
| Command | `sanedrin -m astra,ciro,abner,gemini -r 2 -i es -p 800 -R /home/ignac/sanedrin/reglas/base.md -c papers/ir-corona/ir-corona.tex -c formal/README.md -c sources/README.md -o debates/2026-10-28--ir-corona-sanedrin.md debates/2026-10-28--ir-corona-sanedrin-request.md` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-10-28T13:35:45Z | 1 | ASTRA | codex exec -m gpt-6-astra (sellado) | 263 | 532 | ok |
| 2026-10-28T13:39:56Z | 1 | CIRO | grok --model grok-4.6 (sellado) | 251 | 682 | ok |
| 2026-10-28T13:53:03Z | 1 | ABNER | api.deepseek.com/deepseek-v4-pro | 787 | 370 | ok |
| 2026-10-28T13:57:07Z | 1 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 244 | 18 | FAILED |
| 2026-10-28T13:59:27Z | 2 | CIRO | grok --model grok-4.6 (sellado) | 140 | 442 | ok |
| 2026-10-28T14:00:33Z | 2 | ABNER | api.deepseek.com/deepseek-v4-pro | 65 | 359 | ok |
| 2026-10-28T14:01:09Z | 2 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 36 | 535 | ok |
| 2026-10-28T14:02:20Z | 2 | ASTRA | codex exec -m gpt-6-astra (sellado) | 71 | 535 | ok |
| 2026-10-28T14:02:50Z | Residuo | ASTRA | codex exec -m gpt-6-astra (sellado) | 30 | 172 | ok |
| 2026-10-28T14:03:50Z | Residuo | CIRO | grok --model grok-4.6 (sellado) | 60 | 138 | ok |
| 2026-10-28T14:04:32Z | Residuo | ABNER | api.deepseek.com/deepseek-v4-pro | 42 | 150 | ok |
| 2026-10-28T14:04:47Z | Residuo | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 15 | 166 | ok |
| 2026-10-28T14:05:39Z | Veredicto | ASTRA | codex exec -m gpt-6-astra (sellado) | 52 | 505 | ok |
| 2026-10-28T14:06:05Z | Veredicto | ASTRA | codex exec -m gpt-6-astra (sellado) | 26 | 511 | ok |

Turns: 14 · failed: 1 · model time: 34m 42s

Full log: `2026-10-28--ir-corona-sanedrin.log`
