# Revisión independiente: REGIONAL_LAPLACE_COEFFICIENT_GATE

**Fecha:** 2026-09-17. **Rama:** `research/b-infinity-post-s4-gate`.

**Veredicto de revisión: `PASS`.** No hay reparación obligatoria.

**Veredicto científico revisado:** `PAULI_LEADING_COEFFICIENT_NONVANISHING`.
**Correcto.**

**Estado congelable hoy:**
`PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`.

Encargo: rederivar las afirmaciones de carga del coeficiente Laplace
completo y decidir exactamente uno de los cuatro estados del charter.
No se reabre \(K_*\). No se promociona \(D_B=0\). No se abre encoder,
detector, geometría ni sucesor. Los numerics de \(N\) concreto no
deciden el estado.

La derivación es propia (`/tmp/review_laplace_*.py`, sin importar el
certificado del gate). Helpers congelados `walk2`, `PS`, `PAULI`,
`is_zero` sólo de lectura.

## 0. Orden y hashes

1. Charter de este gate, íntegro.
2. Premisas heredadas: `CURRENT_STATE` §§8.17–8.20 (8.20 sigue
   `NOT_EXECUTED`); informe y revisión de §8.19; identidades (L)/(F)
   del informe escalado.
3. Reconstrucción independiente: contorno \(p=\eta-i\xi_*\); los ocho
   máximos de \(\rho\); Hessiano de \(\varphi\); seis variables de
   posición; \(\beta\) por recuento de factores; capa discreta;
   cola \(r\); sectores \(e^{-K_*N}\) vs \(e^{-2K_*N}\); \(C\) como
   suma; no nulidad de al menos un par Pauli.
4. **Después**, informe de ejecución y certificado.
5. Reejecución del certificado (sin `--diagnostics` como evidencia).
   Regresión 18/18 del certificado de §8.19.

| Archivo | sha256 |
| --- | --- |
| `theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md` | `234f94a73bf0af1160e528c854774af256254cba0aa4f0d6afb09c9336de878d` |
| `reports/2026-09-17--regional-laplace-coefficient-gate.md` | `8d0af529559887bdfa6cba125a23bc1629c19a96c7ba2adcb8c378f6a3294623` |
| `scripts/verify_regional_laplace_coefficient_gate.py` | `d008417debe149743396bfbeb7d55be11fe7aa00bce3b4aecebf6a50997884b2` |
| `state/CURRENT_STATE.md` (aún `NOT_EXECUTED` en §8.20) | `075f92b5cb1a107e90246c8d9e666780409793774663c42679a7d41ba2d3598e` |

`HEAD = origin = ls-remote = 6f520ada13151b864fd77bd9c2ead0ddb1cb7fbb`.
Blob del charter: `18d1f65a662e31a4c44a9d61c0b31e3fc09d56d0`. Tracked
limpio. Certificado reejecutado: **58/58**. Certificado de §8.19:
**18/18**, bytes `e8a9df88…` inalterados.

## 1. A. \(\beta=13/2\) — PASS

**Hessiano de \(\varphi=\operatorname{arcosh}(\prod\cosh\xi_j)\) en
\(\xi_*=t_*(1,1,1)\).** Dual \(v_j=\lambda\tanh\xi_j\),
\(\lambda=\Pi/\sqrt{\Pi^2-1}\). En el rayo isótropo, por simetría,
\(\operatorname{Hess}\varphi=q_t(I-\hat u\hat u^T)+q_n\hat u\hat u^T\)
con autovalores propios (scratch, 50 dígitos)

\[
q_n=0.303383821276,\qquad q_t=0.689567486595\ \text{(doble)}.
\]

Ambos \(>0\): **definido positivo, sin núcleo**. Coincide con
\(Q=-\operatorname{Hess}_\eta\log\rho\) en \(\eta=0\). En los ocho
puntos \(\{0,\pi\}^3\) el Hessiano de \(\log\rho\) es el mismo, con
autovalores \(-q_t,-q_t,-q_n\), todos estrictamente negativos. No hay
degeneración no declarada en el toro.

**Seis variables de posición.** Coordenadas exactas sobre los planos
\(x_1+x_2+x_3=k\), ortogonales a \(\xi_*\):

| Variable | Tipo | Escala |
| --- | --- | --- |
| profundidad Alice \(j\) | suma discreta de semiespacio | \(O(1)\) |
| profundidad Bob \(j'\) | idem | \(O(1)\) |
| tangente relativa \(u'-u\) (2) | gaussiana, Hessiano \(1/(Nq_t)\) | \(\sqrt N\) |
| tangente común \((u+u')/2\) (2) | modo cero del exponente | \(\sqrt N\), confinada por el disco de perfil |
| resto gaussiano normal \(\eta_n\) | Fourier de la normal relativa | \(N^{-1/2}\) en la medida |

El bloque tangencial \(\frac1{Nq_t}\begin{psmallmatrix}I&-I\\-I&I\end{psmallmatrix}\)
tiene rango 2 y modo cero en \(u+u'\). **No es degeneración inesperada:**
el peso \(e^{-\xi_*\cdot(y-x)}\) es constante en cada plano. Las dos
profundidades **no** se tratan como gaussianas: el lineal
\(e^{-t_*(j+j')}\) más el perfil \(\varepsilon^2\) pican en \(O(1)\);
la curvatura \(O(1/N)\) de la normal relativa es resto, no una
integración gaussiana de profundidad.

**\(\beta\) por recuento de factores**, no por «seis direcciones
gaussianas»:

| Factor | Orden |
| --- | --- |
| \(b_N\) en la capa (recurso bandlimited) | \(N^{-3/2}\) |
| \(r\) en la capa de Bob | \(N^{-3/2}\) |
| \(s_N=\Theta(F)=\Theta(N^{-2})\) | \(N^{-2}\) |
| \(h_B=\Theta(N^{-2})\) | \(N^{-2}\) |
| áreas en plano Alice y Bob | \(N\cdot N\) |
| \(\int d\eta_n\) | \(N^{-1/2}\) |
| jacobiano \(d^2\eta_t\sim N^{-1}d^2\tau\) | \(N^{-1}\) |

\[
\beta=\tfrac32+\tfrac32+2+2-2+\tfrac12+1=\tfrac{13}{2}.
\]

La pieza \(\langle r,Ea\rangle\) con \(c_N=\Theta(F^2)=\Theta(N^{-4})\)
es \(N^{-17/2}\), mismo sector exponencial, dos órdenes algebraicos
abajo. \(s_N=O(F)\) no se identifica con \(c_N=O(F^2)\).

Sustituir la suma en plano por la integral está controlado (Poisson 2D:
términos \(m\neq0\) relativos \(O(N^{-3/2})\)). La profundidad **no**
se sustituye por una integral sin control: la suma de semiespacio es
exacta vía Poisson en \(j\), con colas \(\zeta(4)\) (\(1/720\),
\(1/48\)).

## 2. B. \(C\) completo, no un producto — PASS

**Representación inclinada.** Para \(T[w,f]=\sum_y w(y)^\dagger(S^Nf)(y)\),

\[
e^{K_*N}T[w,f]
=\int_{\mathbb T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,
\mathfrak A_f(\eta)\,e^{-i\eta\cdot Nv_*}\,d\mu(\eta),
\]

con \(\widetilde S_N(\eta)=e^{-N\varphi_*}S(\eta-i\xi_*)^N\). Exacta:
símbolo entero, sin polos en el tubo.

**Sectores de (L).** Con \(v=r+a\), los únicos términos a tasa \(K_*\)
son las interferencias lineales en \((a,b,d)\) contra \(r\). Los
cuadráticos \(\langle a,Ea\rangle\), \(\langle b,Eb\rangle\),
\(\langle d,Ed\rangle\) y \(\langle a,E\{b,d\}\rangle\) son
\(O(N^{O(1)}e^{-2K_*N})\) por la cota de Schur inclinada
\(|G_N(d)|\le CNe^{N\varphi_*-\xi_*\cdot d}\) y
\(\xi_*\cdot(y-x)\ge N\xi_*\cdot v_*\). Se **acotan**, no se promocionan
a \(C^{(j)}\) del sector \(e^{-K_*N}\). \(\langle r,Ea\rangle\) es
\(N^{-17/2}e^{-K_*N}\), resto algebraico, no líder.

El líder \(N^{-13/2}e^{-K_*N}\) es, y sólo es,

\[
\begin{aligned}
M=I&:\ -2\operatorname{Im}\langle r,Ed\rangle,\\
M=\sigma_3&:\ +2\operatorname{Im}\langle r,Ed\rangle,\\
M=\sigma_1&:\ -2\operatorname{Im}\langle r,Eb\rangle,\\
M=\sigma_2&:\ +2\operatorname{Re}\langle r,Eb\rangle.
\end{aligned}
\]

**Dos saddles, no ocho.** \(\rho(S(\eta-i\xi_*))=e^{\varphi_*}\) en
todo \(\Sigma=\{0,\pi\}^3\) (elipses: \(\cos(\pi-it)=-\cosh t\) es
vértice real). Fuera, \(\rho\) estrictamente menor (gaps numéricos
\(0.02\)–\(0.88\) en puntos de prueba; el argumento de interior de
elipse es [A]). El carácter \((-1)^{n\cdot x}\) restringido al plano
\(x_1+x_2+x_3=k\) es trivial **si y sólo si** \(n\in\{(0,0,0),(1,1,1)\}\):
en el plano, \(n\cdot x=(n_1-n_3)x_1+(n_2-n_3)x_2+n_3 k\), constante
iff \(n_1=n_2=n_3\). Los otros seis no tienen término de momento cero
en el plano; su suma es \(O(N^{-3/2})\) relativa (y, contra una
envolvente gaussiana de ancho \(\sqrt N\), de hecho \(e^{-\Theta(N)}\)
si se completa el cuadrado a momento \(\pi\)). El análisis del
coeficiente **incluye** \(\eta=\pi(1,1,1)\) al mismo orden, con
proyector \(\overline P=P^T\) y peso \(\Gamma_-\).

**Cola \(r\), recurso no truncado.**
\(\widehat\phi_N(p)=Z_N^{-1/2}g(Np)\lvert\downarrow\rangle\),
\(g(q)=(1-|q|^2)^2_+\), soporte \(|p|\le N^{-1}\). Cota \(L^1\):
\(\|r\|_\infty=O(N^{-3/2})\) uniforme, **sin** \(e^{-K_*N}\). En el
límite de Weyl, \(S(q/N)^N=e^{-iH_W(q)}+O(|q|^2/N)\) y

\[
R_0(w)=c_r\bigl[A(|w|)I-B(|w|)H_W(\hat w)\bigr]\downarrow,
\]

con \(A,B>0\) en \(\rho_*=\sqrt3-1/4<\pi\) porque \(j_0,j_1,\cos k,\sin k\)
son positivos en el rango de integración. Scratch: \(A\approx0.71658\),
\(B\approx0.13225\), \(\hat g\) sin ceros en \([0,3]\), \(R_0(w_*)\)
dominado por la componente \(\downarrow\) y no nulo. Variación de \(r\)
y de \(b_N\) en la capa: relativa \(O(N^{-1/2})\).

**Coeficiente como suma.** Tras Laplace en \(\eta\) y Poisson en
planos/profundidad,

\[
C_{M,M_B}(\theta)
=\mathcal K\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\]

\(\ell_0=\ell(\widetilde R_0^\dagger M_B P\chi)\),
\(\ell_\pi=\ell(\widetilde R_0^\dagger M_B\overline P\chi)\),
\(\chi=\downarrow\) para \(I,\sigma_3\) y \(\uparrow\) para
\(\sigma_1,\sigma_2\). \(\Gamma_\pm\) son las sumas discretas de capa
con paridad par/impar, no factores locales. Los perfiles entran
**dentro** de \(\Psi_\delta\) y de \(\Gamma_\pm\). \(\sinh t_*\neq0\)
**no** se usa como prueba de \(C\neq0\).

Esto no es un producto \(C_{\mathrm{kernel}}C_{\mathrm{perfil}}C_{\mathrm{spin}}C_{\mathrm{interferencia}}\).

## 3. C. No nulidad uniforme — PASS

El objeto encerrado por aritmética de intervalos **no** es un factor
local. Es el funcional completo \(\ell\) de (L) sobre la suma de los
dos saddles con pesos \(\Gamma_\pm(\theta)\).

**Identificación analítica, scratch propio.** Proyector de Perron
( \(S(-i\xi_*)\) hermítica \(\Rightarrow\) \(P\) ortogonal):

\[
P=\frac12\begin{pmatrix}1-\alpha&-(1+iC_*)\alpha/C_*^2\\
-(1-iC_*)\alpha/C_*^2&1+\alpha\end{pmatrix},
\]

con \(P_{11}=(1-\alpha)/2\) exacto (verificado:
\(P_{11}=0.144337567\ldots\)). En \(\eta=\pi(1,1,1)\),
\(S^N\mapsto(-1)^N(S^N)^T\) y \(P\mapsto\overline P\). Paridad de red:
\((-1)^{N+k_y-k_x}=(-1)^{j+j'}\) exactamente (el \(4N-2\lfloor\sqrt3 R\rfloor\)
es par). El mismo \(\theta_N=\{\sqrt3 N/4\}\) gobierna las dos bolas:
la primera capa interior de Bob está a profundidad \(\theta_N/\sqrt3\),
no a \(\{1-\theta_N\}\).

Reconstrucción de \(\ell_0\) a partir de \(R_0\) y \(P\), sin el
certificado:

- \((I,I)\): \(-2\operatorname{Im}(\widetilde R_0^\dagger P\downarrow)
  =-\frac{\sqrt3}{3}B\alpha(C_*-1)/C_*^2\approx-0.0093396\).
  Nulo sólo si \(B=0\) o \(C_*=1\), ambos excluidos (\(B>0\),
  \(t_*>0\Rightarrow C_*>1\)). Es el coeficiente más pequeño porque
  \(\operatorname{Im}\langle r,Id\rangle\) nace de la rotación de Weyl
  \(B\) y de la mezcla, no del canal \(\downarrow\downarrow\) real.
- \((\sigma_2,I)\): \(+2\operatorname{Re}(\widetilde R_0^\dagger P\uparrow)
  =-[3A\alpha+\sqrt3 B(C_*^2(1-\alpha)+\alpha)]/(3C_*^2)\approx-0.36464\).
  Signo fijo por \(A,B,\alpha,1-\alpha>0\). Además
  \(\alpha-C_*^2(1-\alpha)\approx0.236>0\), usado en otros detectores
  de \(\sigma_2\).

Para \(\sigma_2\), \(\ell_0\) y \(\ell_\pi\) tienen el **mismo signo**
en los cuatro detectores (en \(I,P_3\) son iguales). Entonces
\(C(\theta)\propto\Gamma_+\ell_0+\Gamma_-\ell_\pi\) no necesita
comparar \(\Gamma_\pm\): \(\Gamma_+\ge\overline\Gamma-\varepsilon_+>0\)
y \(\Gamma_-\ge0\). Este es el par estructuralmente robusto, y es un
par Pauli.

Para pares con \(\ell_0\ell_\pi<0\) (p. ej. \((I,I)\)), la condición
\(|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|\) se
cierra porque \(\varepsilon_-/\overline\Gamma<6\cdot10^{-5}\) y
\(|\ell_\pi/\ell_0|=(C_*+1)/(C_*-1)\) es \(O(1)\). La enclosure de
intervalo (50 dígitos) cubre los dieciséis pares con oscilación
relativa \(\le1.47\cdot10^{-3}\). Eso **apoya** la no nulidad; no la
sustituye: la identificación de lo encerrado es el funcional \(\ell\)
sobre \(P,\overline P,R_0,M_B,\chi\).

Un modelo discreto propio de las capas (pesos
\(\varepsilon^3 e^{-\kappa\varepsilon}\), \(\kappa=t_*\sqrt3\)) da
fracción par/impar \(=1/2+O(10^{-5})\) uniforme en \(\theta\). Aunque
un canal real \(\downarrow\downarrow\) cancelara en una paridad, la
otra sobrevive con peso \(\Theta(1)\). No se usa como prueba terminal;
confirma que la oscilación de red no atraviesa cero.

## 4. D. Resto vs \(o(1)\) del charter — PASS

Distinción exigida:

**(i) Existencia de algún \(N_*\) tras el cual el resto no puede
cancelar el líder.** El presupuesto [A] identifica cada fuente y la
cierra en \(O(N^{-1/2})\) relativo o menos (cúbico del exponente y
\(P(\eta)-P\); fase \(e^{-i\eta_n\delta}\); variación de \(b_N\) y
\(R_0\); Weyl de \(r\) a \(O(N^{-1})\); geometría de discos
\(O(N^{-1})\); Poisson en plano \(O(N^{-3/2})\); seis puntos no
triviales \(O(N^{-3/2})\); \(\langle r,Ea\rangle\) a \(O(N^{-2})\);
exterior de las bolas \(e^{-cN}\); cuadráticos \(e^{-K_*N}\)). Las
constantes \(r_0,c,C'\) son finitas porque el símbolo es trigonométrico
entero y el Hessiano es no degenerado, y **no son explícitas**. Como
\(\inf_\theta|C(\theta)|\ge(1-1.5\cdot10^{-3})|\overline C|>0\), existe
\(N_*<\infty\) (no explícito) con \(|R_N|<|C|/2\). Eso es exactamente
\(L=e^{-K_*N}N^{-\beta}(C(\theta_N)+o(1))\) con \(C\neq0\). El charter
pide \(o(1)\), no un \(N_*\) numérico.

**(ii) Fórmula cuantitativa fiable a \(N\) moderado.** No se afirma, y
no se usa. Los diagnósticos [D] (no evidencia) muestran corrección
efectiva \(\approx-100/N\) y, para \(M\in\{I,\sigma_3\}\), dominio de
la pieza \(N^{-17/2}\) en \(N\le56\). Eso es coherente con
\(|\overline C(I,I)|\approx0.075\) frente a
\(|\overline C(\sigma_1,I)|\approx3.72\): el líder \(N^{-13/2}\) de
\(I,\sigma_3\) es asintótico, no observable en el rango diagnóstico.
**No decide el estado.** Finite-\(N\) nunca fija el estado terminal.

El resto está controlado en el sentido (i) del charter. La deuda de
constantes explícitas está declarada y no bloquea \(C+o(1)\).

## 5. E. \(C(\theta_N)\) vs \(C\) constante — PASS
(fallo literal del ansatz, no del estado)

El charter escribe

\[
L_{M,M_B}(N)=e^{-K_*N}N^{-\beta}\bigl(C_{M,M_B}+o(1)\bigr)
\]

con \(C_{M,M_B}\) sin argumento \(N\). En la red, los planos
\(x_1+x_2+x_3=k\) no se alinean con las esferas, y el coeficiente
completo es \(C_{M,M_B}(\theta_N)\), 1-periódico, cuasi-periódico en
\(N\) porque \(\sqrt3/4\notin\mathbb Q\). Con la constante
\(\overline C\), el error de oscilación es
\(\le1.5\cdot10^{-3}|\overline C|\), que **no es** \(o(1)\). El límite
de \(N^{\beta}e^{K_*N}L(N)\) **no existe**.

**Fallar el ansatz constante no es dejar \(C\) sin clasificar.** La
pregunta estricta del charter §1 es \(C\stackrel{?}{=}0\). El estado
`PAULI_LEADING_COEFFICIENT_NONVANISHING` exige \(\beta\) identificado y
algún par Pauli con \(C\neq0\) controlado frente al resto. El estado
`OPEN_AFTER_LAPLACE_COEFFICIENT_ANALYSIS` es para \(\beta\) no
identificado, \(C\) no clasificado, resto no controlado, o
factorización usada como si fuera \(C\).

Aquí \(C\) está clasificado: función continua de \(\theta\), signo fijo,
\(\inf_\theta|C(\theta)|>0\). Eso responde \(C\neq0\) **con más fuerza**
que un único valor. El reemplazo \(C\to C(\theta_N)\) es la forma
correcta del coeficiente Laplace en \(\mathbb Z^3\), no una
factorización ni un resto incontrolado.

**Fallo de OPEN.** Asignar `OPEN` diría que no se sabe si el líder se
anula. Se sabe que no se anula, uniformemente en \(\theta\). El hedge
del autor («si el revisor insiste en la constante literal, OPEN») se
registra y se rechaza: el revisor no caucho-sella la preferencia del
autor ni el hedge. El único estado del charter que casa con la
pregunta \(C\stackrel{?}{=}0\) ya respondida, con \(\beta\) y resto
(i), es `PAULI_LEADING_COEFFICIENT_NONVANISHING`.

## 6. F. Ocho puntos de toro vs §8.19 congelado — PASS

La frase de §8.19 que afirma unicidad del máximo de \(\rho\) en
\(\eta=0\) es **falsa**. Igualdad en los ocho puntos \(\{0,\pi\}^3\).
Esto **no reabre \(K_*\)**: \(I(v)\) depende de \(\log\rho\), y \(\rho\)
es el mismo; la cota de Legendre y el minimizador regional único
siguen. Los archivos de §8.19 no se tocan, como está mandado.

El análisis de coeficientes trata el punto extra \(\pi(1,1,1)\) al
mismo orden (proyector conjugado, \(\Gamma_-\), paridad
\((-1)^{j+j'}\)). Los otros seis quedan en el resto. \(K_*\) no se
reoptimiza. Consistencia numérica independiente:
\(t_*=0.735752814420\), \(K_*=0.190518929584\), \(J<K_*<\log4\).

## 7. G. Estado terminal — PASS

Único estado, en el orden del charter:

1. **`PAULI_LEADING_COEFFICIENT_NONVANISHING` — se asigna.**
   \(\beta=13/2\); los doce pares con \(M\in\{\sigma_1,\sigma_2,\sigma_3\}\)
   tienen \(C(\theta)\neq0\) uniforme; el sector \(e^{-K_*N}\) está
   sumado; el resto es \(o(1)\) en el sentido (i). Basta un par; el más
   robusto es \(\sigma_2\) (mismo signo en ambos saddles).
2. `ALL_LEADING_COEFFICIENTS_VANISH`: no.
3. `REFERENCE_CONTROL_ONLY_LEADING_NONVANISHING`: no (el control \(I\)
   también es no nulo, y los Pauli sobreviven).
4. `OPEN_AFTER_LAPLACE_COEFFICIENT_ANALYSIS`: no. Véanse §§1–5.

**Autorización de `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.** Con
§§8.17 y 8.19, para **los doce pares Pauli**
(\(M\in\{\sigma_1,\sigma_2,\sigma_3\}\times\{I,P_1,P_2,P_3\}\)):

\[
\delta_{M,M_B}(N)
=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr).
\]

También vale, como dato y no como control negativo, para los cuatro
pares con \(M=I\). No se afirma \(D_B=0\) ni \(\delta\equiv0\).

**Techo del claim.**

- Sólo la clase congelada: CJWW (5.15), una partícula, bolas euclídeas,
  perfiles, \(\theta=\pi/2\), las cuatro \(M\) y las cuatro \(M_B\),
  recurso \(g(Np)\).
- Afirmación **asintótica**. \(N_*\) y \(C'\) no explícitos. A
  \(N\lesssim10^3\) la fórmula líder no es cuantitativa; para
  \(I,\sigma_3\) el \(N^{-17/2}\) domina en el rango diagnóstico.
- \(C=C(\theta_N)\), no una constante.
- No reabre \(K_*\), \(v_*\), geometría, encoder, detector, perfiles,
  nodo ni walk. No reabre §§8.16–8.19, `3/128`, no-corner ni
  `Delta T=2`.
- \(N\to\infty\) no es \(a,\tau\to0\). Sin unidades físicas. **No se
  afirma violación de microcausalidad.**
- La familia \(M=aI+b\cdot\sigma\) general no está cubierta.

## 8. Qué certifica el certificado (y qué no)

**58/58**, reejecutado desde la raíz, `python3 -B`, sin
`--diagnostics`. Cubre: hash del charter y bytes de §8.19; hermiticidad
de \(S(-i\xi)\); cinco simetrías de medio periodo y trivialidad de
caracteres en planos; forma cerrada de \(P\), \(C_*^2\), \(q_n\),
\(q_t\); Weyl formal de \(r\) (ángulos, signos de \(A,B\)); Laplace de
\(\Psi_\delta\), colas \(1/720\) y \(1/48\); prefactor \(\mathcal K\);
recuento algebraico de \(\beta\); paridad \(j+j'\); enclosures de
\(\overline C\) y margen uniforme en \(\theta\) para los dieciséis
pares; \(C(\sigma_3)=-C(I)\).

**No certifica** los lemas asintóticos 1(d), 2, 3, 4 ni el teorema
(constantes \(r_0,c,C'\), \(N_*\)). Esos son [A], rederivados aquí.
`--diagnostics` es `SUPPORTED`, no se usó para \(\beta\), \(C\) ni el
estado.

## 9. Tabla de afirmaciones de carga

| Afirmación | Resultado |
| --- | --- |
| A. \(\beta=13/2\), profundidades discretas, modo cero declarado, Hessiano ND | **PASS** |
| B. \(C\) completo = interferencia \(r\) sumada en dos saddles; cuadráticos acotados | **PASS** |
| C. No nulidad uniforme, no un factor local | **PASS** |
| D. Resto \(O(N^{-1/2})\) basta para \(o(1)\) asintótico; no para \(N\) moderado | **PASS** |
| E. \(C(\theta_N)\) no fuerza `OPEN`; el estado que casa es `PAULI_…_NONVANISHING` | **PASS** |
| F. Corrección de los 8 puntos no reabre \(K_*\); \(\pi(1,1,1)\) está en \(C\) | **PASS** |
| G. Estado terminal único | **PASS** |

## 10. Reparaciones obligatorias

Ninguna.

## 11. Veredicto

Congelar `PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`
está autorizado. Queda autorizada
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` para los doce pares Pauli
de la clase congelada, en el techo asintótico de §7. El cuello de
botella de §§8.17–8.19 (coeficiente Laplace integrado) queda cerrado
en esa clase. No se abre un gate nuevo en esta revisión.
