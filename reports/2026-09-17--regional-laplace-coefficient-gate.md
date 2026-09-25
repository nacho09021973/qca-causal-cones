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
