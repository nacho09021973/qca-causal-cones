# C2a: revisión matemática independiente y adversarial

Fecha: 2026-09-22. **Veredicto: PASS**, exclusivamente para C2a del
[contrato C2a](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md) y el par
congelado \(M=\sigma_2\), \(M_B=I\). No hay reparaciones obligatorias.
Las observaciones de la sección 9 son editoriales y no bloquean.

Revisor: Claude Opus 5 (`claude-opus-5`) en Claude Code, en una sesión
separada del agente que escribió la
[derivación C2a](2026-09-22--c2a-oscillatory-transfer.md). Es la revisión
de un agente, no una revisión humana. Es una sola revisión: no hay
consenso de varios miembros, formalización ni promoción canónica. No se
modificó la nota revisada.

Formato del veredicto: el encargo recibido se corta en «Emite exactamente».
Se usa el vocabulario del contrato C2a (`PASS`, `FAIL_TO_CLOSE`,
`TRANSFER_REFUTED`). `PASS` también forma parte del vocabulario del contrato
C1/C2/C3.

## 1. Objeto, entradas y límites

Afirmación revisada, sin darla por buena:
\[
L^W_{PP}=N^{-3}\bigl[\mathcal C_0+\mathcal C_1\cos(\sqrt N/2)\bigr]+O(N^{-7/2}),
\qquad \mathcal C_0>\mathcal C_1>0,
\]
\[
L_{PP}-L^W_{PP}=O(N^{-13/4}),\qquad
L_{PP}=N^{-3}A_N+O(N^{-13/4}),\quad A_N\ge\mathcal C_0-\mathcal C_1>0.
\]

Estado de partida congelado: C1 = PASS; C2a = proof written / review pending;
C2b bloqueado por C2a; C2c bloqueado por C2b; C3 separado; E/AdS congelado.
Esta revisión no abre C2b ni C2c, no deriva \(L_{PQ},L_{QP},L_{QQ}\) y no
usa \(L-L_{PP}\) para inferir un mecanismo.

Archivos revisados (SHA256 observados en esta sesión):

| Archivo | SHA256 |
| --- | --- |
| `reports/2026-09-22--c2a-oscillatory-transfer.md` | `8235d69707d7e83065a287e4d90005a55972fbd2710e91634be02f67fba93069` |
| `theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md` | `f5dea4d2683468ffee5556381b2800a67be84803e732624fe800a1a1076b108f` |
| `theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md` | `ebc862f3d9dc7fa40c1cf7764aa2d6d6e8669013dfb97fcb98067a8c58c5edf8` |
| `reports/2026-09-22--c2-projected-response-representation.md` | `fe50c58c237202514c8816184f853592999f4b70f49820db6256f11669974732` |
| `reports/2026-09-22--c1-leakage-independent-review.md` | `22f5a10fefee1946eb481c36b4ea85c1fa74a89d1c91856bbbbacb523680794d` |
| `reports/2026-09-22--ir-projection-leakage-and-conditioning.md` | `c2f99ce9d2a17946c167f8534a5a5964837aa53a7f0dbcf64c80dad98cbbf9cb` |
| `papers/ir-corona/ir-corona.md` | `afcc25057f0a258888b71e25a5692ec06bfec1c76ac59132da73ded2ee89e7f3` |
| `state/CURRENT_STATE.md` (sin cambios) | `47d77da9daeee9696c376c6a011096be6b73c38ad9343041660a7f5f8892142a` |

Los hashes del contrato, de C2, de la revisión C1 y del estado canónico
coinciden con los registrados en la nota C2a. Del manuscrito sólo se usaron
las secciones 2–3 (convenciones y protocolo) y el Teorema 4.4, este último
para situar la sección 7 de la nota fuera del veredicto. Los valores
N=24/40 de la
[auditoría retenida](2026-09-22--ir-spectral-attribution-audit.md)
sólo se leyeron; se usan en la sección 10 como contexto, no como prueba.

No se ejecutó código, cuadratura, barrido ni ajuste. Todas las
comprobaciones de este informe se hicieron a mano sobre las fórmulas.

## 2. Observable, proyector, convenciones y escalado

1. **Proyector.** \(P=1_{|p|\le N^{-1/2}}\) es la bola cerrada del
   contrato, sin suavizar. Está contenida en \(\mathbb T^3\) y conmuta
   con \(S\), porque ambos son multiplicadores de Fourier. Además
   \(P\phi_N=\phi_N\), ya que el soporte de \(\hat\phi_N\) es
   \(|p|\le N^{-1}\). En variables \(k=Np\), el corte es \(|k|\le K=\sqrt N\).
   La referencia Weyl usa el mismo corte duro, sin desplazamiento.
2. **Observable.** Con \(a=(U_M-I)\phi\):
   \(P\Delta P=|\phi\rangle\langle Pa|+|Pa\rangle\langle\phi|+|Pa\rangle\langle Pa|\).
   Por tanto
   \(\operatorname{tr}(ES^NP\Delta PS^{-N})=2\operatorname{Re}\langle r,Ed_P\rangle+\langle d_P,Ed_P\rangle\).
   Es el \(L_{PP}\) firmado de C2 y el de la auditoría retenida. No aparece
   la normalización \(1/(1-q_N)\) ni el término \(q_Np0_N\); no es
   \(L_{\rm cond}\). C3 no entra en ninguna estimación.
3. **Convenciones.**
   \(\hat\psi(p)=\sum_xe^{ip\cdot x}\psi(x)\), \(d\mu=d^3p/(2\pi)^3\) y
   \(\hat A(k)=\int e^{ik\cdot X}A\,dX\) son compatibles en el manuscrito,
   C1, C2 y C2a. Con Poisson,
   \(\hat a_N(k/N)=N^{3/2}\mathscr A_N(k)\), con imágenes \(2\pi Nm\) en la
   celda escalada \([-\pi N,\pi N)^3\). La medida
   \(d\mu=d^3k/((2\pi)^3N^3)\) da exactamente
   \(d_P(y)=N^{-3/2}D_N(y/N)\) y \(r(y)=N^{-3/2}R_N(y/N)\). El factor de
   \(R_N\) es \(c_r\), porque
   \(Z_N^{-1/2}N^{-3}(2\pi)^{-3}=N^{-3/2}c_r\). Así
   \[
   L_{PP}=N^{-3}\sum_y h(y/N)\bigl[2\operatorname{Re}R_N^\dagger D_N+\|D_N\|^2\bigr](y/N)
   \]
   es exacto. \(D_N\) y \(R_N\) son interpolantes de banda limitada. Los
   pasos de Poisson posteriores reescriben este mismo número y no cambian
   el observable.
4. **Símbolo.** De la ecuación (2) del manuscrito,
   \(S=fI-ia\cdot\sigma\) con \(a=(s_1,-c_1s_2,c_1c_2s_3)\): comprobado
   entrada por entrada. \(H=(\omega/\sin\omega)a\cdot\sigma\) es analítico
   e impar, y \(\omega/\sin\omega=1+|p|^2/6+O(|p|^4)\) es par. El \(H_3\)
   de (2.3) se recalculó con el Taylor cúbico de \(a\) y coincide
   componente a componente. Para la prueba sólo cuentan dos hechos: \(H_3\)
   es un polinomio homogéneo cúbico (es decir, un operador diferencial
   local) y no hay término cuadrático.
5. **Duhamel.** Escribimos
   \(V_N=\exp(-i[H_W+N^{-2}H_3+\rho_N])\) con
   \(\|\rho_N\|\le C|k|^5N^{-4}\) y aplicamos un Duhamel de dos órdenes.
   Resulta \(\|\mathcal T_N\|\le CN^{-4}(|k|^5+|k|^6)\) para \(|k|\le K\),
   donde \(|k|/N\le N^{-1/2}\) está dentro de la región de analiticidad.
   Esto confirma (7) de la nota.

## 3. Punto 1: de dónde salen \(\mathcal C_0\) y \(\mathcal C_1\)

**(a) Cancelación del interior.** La evolución Weyl libre tiene kernels de
\(\cos(t|D|)\) y \(\sin(t|D|)/|D|\) con soporte en \(|x|\le t\), seguidos del
operador local \(H_W(D)\). Por eso \(D^W_\infty\) se anula para
\(|Y|>1+b\). Bob cumple \(|Y|\ge\sqrt3-b\), y la separación es
\(\gamma=\sqrt3-\tfrac32>0\) porque \(3>9/4\). Como
\(\|V_W\hat A\|=O(k^{-4})\), la cola es absolutamente convergente y
\(D^W_K(Y)=-\text{(integral sobre }|k|>K)\) punto a punto.

**(b) Núcleo angular exacto.** Se usan
\(\int e^{ixz}d\Omega=4\pi j_0(x)\) y
\(\int e^{ixz}z\,d\Omega=4\pi i j_1(x)\), con \(j_1\) impar. Así
\(\int e^{-ikn\cdot Y}V_W(kn)d\Omega=4\pi[\cos k\,j_0(k\rho)I-\sin k\,j_1(k\rho)J]\).
Con el factor \((2\pi)^{-3}\) se obtiene \(1/(2\pi^2)\): los signos de C2 (8)
son correctos.

**(c) Descomposición en bandas.** Como \(j_0=\sin x/x\) y
\(j_1=\sin x/x^2-\cos x/x\), el término principal es
\(\cos k\sin k\rho\,I+\sin k\cos k\rho\,J=\sum_\sigma\sin((\rho+\sigma)k)P_\sigma(n)\),
con \(P_\sigma=(I+\sigma J)/2\) proyectores ortogonales, pues \(J\) es
hermítico y \(J^2=I\).

**(d) Borde de Alice.** Con \(t=b-r\), \(h_s(r)=r\,s(r)\) satisface
\(h_s(b)=h_s'(b)=0\) y \(h_s''(b)=2b\cdot32\pi B=16\pi B\). De ahí
\(\hat s(k)=64\pi^2B\cos(bk)/k^4-4\pi h_s'''(b)\sin(bk)/k^5+O(k^{-6})\).
El quinto paso de integración por partes es legítimo porque \(h_s\) es
analítica en \([0,b]\). Para \(c(r)\) se tiene
\(\cos(\pi F/2)-1=O(t^4)\), luego \(h_c^{(j)}(b)=0\) para \(j\le3\) y
\(\hat c=O(k^{-6})\). La imparidad de \(h\) elimina todos los términos del
origen. Con \(\zeta=\sigma_2\!\downarrow=-i\!\uparrow\), el término
principal es \(i\hat s\,\zeta\).

**(e) Factores.** \(-(2\pi^2)^{-1}\cdot i64\pi^2B/\rho=-32iB/\rho\), y
\(\sin(\cdot)\cos(bk)=\tfrac12\sum_\epsilon\sin((\rho+\sigma+\epsilon b)k)\)
da \(-16iB/\rho\). Además
\(\int_K^\infty k^{-3}\sin(ck)\,dk=\cos(cK)/(cK^3)+O(K^{-4})\) con
\(c\ge\gamma\). Se reproduce (12):
\(D^W_K=-(16iB/\rho K^3)\sum_\sigma P_\sigma\zeta F_\sigma+O(K^{-4})\).
Este resultado coincide con C2 (9), porque \((I+\sigma J)=2P_\sigma\).

**(f) Restos de (12).** Hay cuatro contribuciones. El término \(\sin x/x^2\)
de \(j_1\) y el término \(\beta_5\) de \(\hat s\) darían \(O(K^{-3})\) en
valor absoluto, igual que el líder. Sólo bajan a \(O(K^{-4})\) por
oscilación radial con frecuencias \(\rho\pm1\pm b\), todas de módulo
\(\ge\gamma\). Esta oscilación es imprescindible para el resultado y se
verificó. El resto \(O(k^{-6})\) de \(\hat s\) y la contribución de
\(\hat c\) dan \(O(K^{-4})\) de forma absoluta. Todo es uniforme en Bob.

**(g) Cuadrado del campo.** \(\nu_\sigma=\langle\zeta,P_\sigma\zeta\rangle=(1+\sigma n_3)/2\),
porque \(\langle\uparrow,J\uparrow\rangle=n_3\). Al desarrollar
\(F_\sigma^2\), los términos cruzados \(\epsilon\ne\epsilon'\) llevan
multiplicidad 2. La parte sin fase \(2K\rho\) es
\(\tfrac12(t_+^2+t_-^2)+t_+t_-\cos(2bK)\). El resto lleva fases
\(2K\rho+\text{const}\).

**(h) Eliminación de las fases \(2K\rho\).** Una integración por partes a lo
largo de \(\nabla\rho\) (\(|\nabla\rho|=1\), Bob lejos del origen) da
\(O(K^{-1})\). El peso \(W=h\,\nu_\sigma t\,t'/\rho^2\) es \(C^1\) y se anula
en \(\partial\)Bob, de modo que no hay término de frontera. Sin este paso
el error sería \(K^{-6}\), del orden del líder. Queda verificado.

**(i) Término lineal de referencia: \(O(K^{-7})\).** Necesita **dos**
ganancias. En valor absoluto sería \(K^{-5}\); la fase angular
\(e^{-irn\cdot u}\), con polos \(\pm\hat u\), lo baja a \(K^{-6}\); la
ausencia de fase radial estacionaria lo baja a \(K^{-7}\). Se comprobaron
las 16 combinaciones \(\pm\ell+(\epsilon-\eta)b-\sigma\): el mínimo es
\(\ell-1-2b=\gamma\). Para los restos hace falta una cota \(C^k(S^2)\)
uniforme de \(\mathcal E_N(r,\cdot)\) en (5). Se verificó:
\(|rn-q|-(r-n\cdot q)\) y todas sus derivadas tangenciales son \(O(1/r)\)
para \(r\ge2\) y \(|q|\le1\), y \(\hat R_N\) está uniformemente acotado en
\(L^1\).

**Por qué el líder es exactamente \(N^{-3}\).** El campo proyectado en Bob
es la cola del corte:
\(\int_K^\infty k^2\cdot(k\rho)^{-1}\cdot k^{-4}\cdot\text{osc}\,dk\sim K^{-3}\).
Los factores son la medida radial, la dispersión esférica y la cola
\(k^{-4}\) que el borde \(C^1\) del perfil de Alice deja en \(\hat A\). El
prefactor \(N^{-3}\) de la representación exacta se compensa con los
\(\sim N^3\) sitios de la suma de Riemann. El término cuadrático vale, pues,
\(\int h\|D\|^2\sim K^{-6}=N^{-3}\), y el lineal queda suprimido por (i). La
fase \(2bK=\sqrt N/2\) es la interferencia entre los dos frentes
(\(\epsilon=\pm\)) del borde esférico de Alice, separados \(2b\), muestreada
a la frecuencia de corte. Tras (h), la única dependencia en \(N\) del líder
es \(\cos(2bK)\), con coeficiente acotado inferiormente. No hay cancelación
oculta dependiente de \(N\).

## 4. Punto 2: separación estricta

\[
\mathcal C_0-\mathcal C_1=128B^2\int\frac h{\rho^2}\sum_\sigma\nu_\sigma
\Bigl(\frac{-2b}{(\rho+\sigma)^2-b^2}\Bigr)^2d^3Y>0,
\qquad
\mathcal C_1=256B^2\int\frac h{\rho^2}\sum_\sigma\nu_\sigma t_{\sigma,+}t_{\sigma,-}\,d^3Y>0.
\]
La primera integral es estrictamente positiva por cuatro razones: \(b>0\);
el integrando es continuo; \(h>0\) en la bola abierta; y
\(\nu_++\nu_-=1\) con \(\nu_\sigma\ge0\). La segunda lo es porque
\(\rho+\sigma\pm b\ge\gamma>0\) implica \(t_{\sigma,\pm}>0\). Los únicos
datos de entrada son \(B\ne0\) y \(\gamma>0\). \(B>0\) se sigue de un
integrando estrictamente positivo (C1) y \(\gamma>0\) de \(3>9/4\).
**La desigualdad está demostrada simbólicamente y no depende de ningún
cálculo numérico.** \(\mathcal C_0\) y \(\mathcal C_1\) son constantes, así
que no hace falta ninguna condición de uniformidad en \(N\). La cota
\(A_N\ge\mathcal C_0-\mathcal C_1\) vale para todo \(N\), sin elegir
subsucesiones.

## 5. Punto 3: presupuesto completo de errores

La descomposición es exhaustiva. \(L_{PP}\) es exactamente la suma del
término lineal y del cuadrático de la sección 2. El lineal, tras Poisson
exacto, es
\(\int_{B_K}\hat w_0^\dagger V_W\hat A+\int_{B_K}(\hat w_N-\hat w_0)^\dagger V_W\hat A+N^{-2}\int_{B_K}\hat w_N^\dagger V_1\hat A+\int_{B_K}\hat w_N^\dagger\mathcal T_N\hat A\)
más el término de imágenes. El cuadrático es \(\int h\|D_N\|^2\) más el
error de muestreo. Ninguna otra pieza entra en \(L_{PP}\).

| Pieza pedida | Dónde | Orden | Mecanismo y verificación |
| --- | --- | --- | --- |
| Discretización/muestreo, lineal | (16) | \(K^{-8}\) | Poisson exacto para \(w_N^\dagger D_N\), función continua compacta con serie absolutamente convergente. Imágenes de \(\hat w_N\) y de \(\hat A\): \(O(N^{-4})\) en \(B_K\), porque \(\lvert k+2\pi Nm\rvert\ge\pi N\lvert m\rvert\). Las transformadas centrales están en \(L^1\). Verificado. |
| Discretización/muestreo, cuadrático | (23) | \(K^{-8}\) | \(\widehat{\lVert D_N\rVert^2}\) tiene soporte en \(\lvert\eta\rvert\le2K\) y norma \(L^1\le C\lVert\hat D_N\rVert_1^2=O(1)\). \(\lvert\hat h(2\pi Nm-\eta)\rvert\le C(N\lvert m\rvert)^{-4}\). Verificado. |
| Imágenes de Alice en el campo | (16), (21) | \(K^{-8}\), \(N^{-4}K^{3/2}\) | Se conservan en \(D_N\) hasta acotarlas. Verificado. |
| Dispersión, primer corrector | (17)–(18) | \(K^{-7}\) | Separación de soportes y ganancia angular (sección 6). Verificado. |
| Dispersión, resto | (19) | \(K^{-7}\) | Absoluto: \(N^{-4}\int_0^Kr^2(1+r)^{-8}(r^5+r^6)dr=O(N^{-4}K)\). Margen de una potencia de \(K\). Verificado. |
| Recurso \(R_N\to R_0\) | (9), (20) | \(K^{-9}\) | \(\lVert V_N-V_W\rVert\le CN^{-2}\) en \(\lvert q\rvert\le1\). Soportes separados: el término truncado es menos la cola. Verificado. |
| Corte espectral móvil | (10), (12), (21) | — | Representación de cola exacta para el corte duro. El volumen de \(B_K\) aparece como \(\int_0^Kr^8(1+r)^{-8}dr\sim K\). Verificado. |
| Bordes | (d), (h) | — | El borde de Alice da el líder. El de Bob no deja término de frontera porque \(h\in C^1\) y se anula allí. El borde del corte es la cola. Verificado. |
| Lineal de referencia | (11) | \(K^{-7}\) | Sección 3 (i). Verificado. |
| Cuadrático, transferencia | (21)–(22) | \(K^{-13/2}\) | Sección 7. **Término dominante del presupuesto.** Verificado. |
| Resto del líder Weyl | (12)–(13) | \(K^{-7}\) | Sección 3 (f)–(h). Verificado. |

No se sustituye el campo discreto por el campo Weyl mediante una
aproximación puntual. Esa sustitución sólo aparece en las piezas de la
tabla: la cota puntual insuficiente \(O(N^{-1})\) de C2 (10) no se usa.
**No queda ningún término sin control de orden \(N^{-3}\) o mayor.** El
error total es \(O(K^{-13/2})=O(N^{-13/4})=N^{-3}\cdot O(N^{-1/4})\). Las
constantes son uniformes en \(N\): se usan \(\hat R_N\) acotado en \(L^1\),
cotas analíticas de \(V_N\) y una geometría fija. Esto basta para concluir
\(L_{PP}/(N^{-3}A_N)\to1\) y \(L_{PP}>0\) para \(N\) grande.

## 6. Punto 4: cancelación del primer corrector de dispersión

**Soportes.** \(\operatorname{supp}(V_1(D)A)\subset\overline B(0,1+b)=\overline B(0,5/4)\)
y \(\operatorname{supp}w_N\subset\overline B(u,1/4)\), con \(|u|=\sqrt3\). La
distancia entre ambos es \(\gamma=\sqrt3-3/2\approx0.232\).

**Por qué el primero está donde se dice.**
\(V_1(D)A=-i\int_0^1U_W(1-s)H_3(D)U_W(s)A\,ds\), con \(U_W(t)\) de
propagación \(\le t\) y \(H_3(D)\) diferencial y local. Una vía equivalente
es Paley–Wiener–Schwartz: \(V_1\) es entera de tipo exponencial 1 con
crecimiento polinómico. En los dos casos \(V_1A\) es una distribución
temperada con soporte en radio \(1+b\), aunque \(A\) sea sólo \(C^1\).

**Por qué la identidad (17) es exacta.** El emparejamiento en Fourier
converge absolutamente: el integrando radial es \(O(r^{-3})\). Para el test
mollificado \(w_N*\rho_\delta\in C_c^\infty\), con \(\delta<\gamma\), vale
\(\langle w^\delta,V_1A\rangle=0\), y la forma de Fourier de ese
emparejamiento es válida. Al hacer \(\delta\to0\), convergencia dominada.
La identidad se obtiene en \(\mathbb R^3\) **antes** del corte. El corte
sólo interviene después, al escribir la integral truncada como menos la
cola. No es una cancelación numérica, ni posterior al corte, ni un
argumento de pequeñez.

**Por qué persiste para todo \(N\).** En variables escaladas, el tiempo Weyl
es exactamente 1 y \(V_1\) no depende de \(N\): el \(N^{-2}\) se extrae. Los
soportes de fuente y detector son fijos. La separación \(\gamma\) no
depende ni de \(N\) ni de \(K\).

**Paso que no se puede omitir.** Sin la ganancia angular, la cola daría
\(N^{-2}K^{-2}=K^{-6}\), del orden del líder. La ganancia se aplica a
funciones analíticas en la esfera: \(R_N(u+\eta bn)\) y
\(P_\sigma H_3P_\sigma\). Los términos cruzados de (8) no tienen
denominadores singulares (\(\sigma-\tau=\pm2\)). Así se obtiene
\(N^{-2}K^{-3}=K^{-7}\). El mismo mecanismo de soportes, sin ganancia
adicional, da (10) y (20).

## 7. Punto 5: paso \(L^2\) del término cuadrático

Por Plancherel, \(\|D_N-D^W_K\|_2\) se acota por
\(\|(V_N-V_W)\hat A\|_{L^2(B_K)}\le CN^{-2}\bigl(\int_0^Kr^8(1+r)^{-8}dr\bigr)^{1/2}=O(N^{-2}K^{1/2})\)
más \(\|V_NE^A_N\|_{L^2(B_K)}=O(N^{-4}K^{3/2})\). El resultado es
\(O(K^{-7/2})\). Por (12), \(\|\sqrt hD^W_K\|_2=O(K^{-3})\). Con
\(0\le h\le1\) y Cauchy–Schwarz,
\(2\cdot K^{-3}\cdot K^{-7/2}+K^{-7}=O(K^{-13/2})\). Controles específicos:

- de amplitudes a productos, el término cruzado pierde exactamente lo que
  se contabiliza;
- el único dominio que depende de \(N\) es \(B_K\), y entra por
  \(\int_0^K\), sin supremos sobre regiones crecientes;
- no se usa ninguna equivalencia de normas dependiente de \(N\). La norma
  \(L^2(\mathbb R^3)\) sólo se usa como cota superior de la norma sobre
  Bob;
- el corte móvil está incluido en \(B_K\);
- las imágenes y el aliasing aparecen por separado, en \(E^A_N\) y en (23).

La mejora frente al control puntual procede de medir el error en \(L^2\) y
no en \(L^\infty\). Sólo se usa para acotar un error, nunca para atribuir la
señal a un sector, como exige el contrato. El margen respecto al líder es
\(K^{-1/2}=N^{-1/4}\): es el cuello de botella del resultado.

## 8. Comprobaciones adicionales

| Comprobación | Resultado |
| --- | --- |
| \(P\) es exactamente el proyector del contrato | Sí: bola dura \(\lvert p\rvert\le N^{-1/2}\), también en la referencia Weyl |
| \(L_{PP}\) de la prueba = \(L_{PP}\) de C2 | Sí; identidad reconstruida en la sección 2 |
| Sustitución inadvertida por \(L_{\rm cond}\) | No |
| C3 en la prueba | No |
| Una aproximación continua cambia el observable | No: interpolantes exactos y Poisson exacto; la referencia Weyl sólo aparece a través de errores acotados |
| Imágenes y convenciones de Brillouin/Fourier entre documentos | Compatibles (sección 2) |
| \(O(\cdot)\) suficientes para \(o(N^{-3})\) | Sí: \(O(N^{-13/4})=N^{-3}O(N^{-1/4})\), con constantes uniformes y cota inferior \(\mathcal C_0-\mathcal C_1\) |
| Afirmación dependiente de evidencia numérica | Ninguna |

## 9. Observaciones no bloqueantes

1. En (4.2), «interpretarse distribucionalmente» es impreciso. Conviene
   citar la propagación finita de la integral de Duhamel o
   Paley–Wiener–Schwartz, como en la sección 6.
2. En (2.2) se afirma sin prueba que \(g\in C^6\) implica \(G\in C^2\). Es
   estándar, y además conservador. Todas las \(g\) con desarrollo explícito
   son analíticas; sólo \(\mathcal E_N\) requiere la cota \(C^k\), que se
   verificó en la sección 3 (i). Ahí la ganancia angular sí es
   imprescindible: sin ella (11) sería \(K^{-6}\).
3. En (3.2), «También C1>0» no se justifica. La razón es
   \(\rho+\sigma\pm b\ge\gamma>0\).
4. Ni las constantes ni el umbral \(N_0\) son explícitos, y la convergencia
   es lenta: el error relativo es \(N^{-1/4}\), y las ganancias oscilatorias
   van en potencias de \(1/(\gamma K)\). En los \(N\) retenidos,
   \(\gamma K\approx1.14\) (N=24) y \(1.47\) (N=40). El enunciado es
   puramente asintótico y no fija el signo en esos \(N\).
5. La sección 7 de la nota (24)–(25) queda **fuera de este veredicto**. No se
   revisa como parte de C2a ni se usa aquí. Toca C2b y depende del
   Teorema 4.4 como premisa.

## 10. Diagnóstico no probatorio

Una estimación de orden de magnitud hecha a mano, sin código, a partir de
(15) da \(\mathcal C_0-\mathcal C_1\approx1.5\times10^{-3}\) y
\(\mathcal C_1\approx6\times10^{-3}\). Método: \(B\approx0.089\) por
desarrollo de \(\sin(k/4)\); \(\int h=\pi/210\); promedio axial de los
pesos con densidad \((1-16z^2)^3\) por Simpson de nueve nodos; \(\nu_\sigma\)
evaluado en el eje. La incertidumbre es de decenas por ciento.

- **N=40:** \(\cos(\sqrt{40}/2)\approx-0.9998\), el mínimo de \(A_N\). La
  estimación da \(N^{-3}(\mathcal C_0-\mathcal C_1)\approx2.4\times10^{-8}\)
  frente al valor retenido \(L_{PP}=2.68\times10^{-8}\).
- **N=24:** el líder estimado, \(\approx2\times10^{-7}\), tiene signo
  contrario al retenido, \(-3.8\times10^{-7}\).

Con \(\gamma K\approx1\), ninguno de los dos datos es evidencia a favor ni
en contra de un enunciado asintótico con constantes no explícitas. No
forman parte del veredicto.

## 11. Dictamen

| Ataque con posible efecto decisivo | Resultado |
| --- | --- |
| Normalización, Jacobianos y escala del corte | PASS: factores reconstruidos |
| Signos de \(j_0,j_1\) y bandas \(P_\sigma\) | PASS |
| Líder \(K^{-6}\) y ausencia de otro término \(K^{-6}\) | PASS: lineal \(K^{-7}\), fases \(2K\rho\) \(K^{-7}\) |
| Nulidad del coeficiente oscilatorio | PASS: \(\mathcal C_0-\mathcal C_1>0\) simbólico |
| Término olvidado de orden \(\ge N^{-3}\) | PASS: descomposición exhaustiva (sección 5) |
| Cancelación del corrector \(V_1\) | PASS: identidad exacta por soportes antes del corte |
| Cola del corrector | PASS: ganancia angular verificada |
| Paso \(L^2\) cuadrático | PASS: \(O(K^{-13/2})\) con constantes uniformes |
| Poisson y aliasing | PASS |
| Confusión con \(L_{\rm cond}\) o con C3 | PASS: ausente |

**C2a = PASS; reparaciones obligatorias pendientes = ninguna.** Se aceptan
el líder de \(L^W_{PP}\) y la transferencia
\(L_{PP}=N^{-3}[\mathcal C_0+\mathcal C_1\cos(\sqrt N/2)]+O(N^{-13/4})\),
con \(\mathcal C_0>\mathcal C_1>0\). El alcance es el par
\(\sigma_2/I\), el recurso, los perfiles y la geometría congelados, y el
corte duro \(N^{-1/2}\), con \(N\to\infty\) y umbral no explícito. Es una
revisión independiente de agente. No es revisión humana, consenso,
formalización ni promoción canónica. No afirma novedad ni transporte local
físico, y no es una interpretación de \(L-L_{PP}\).

Estado tras esta revisión: C1 = PASS; C2a = PASS (una revisión
independiente). La dependencia de C2b respecto de C2a queda satisfecha,
pero C2b **no** se abre sin decisión del usuario. C2c sigue bloqueado por
C2b, C3 separado y E/AdS congelado. No se modifican `state/CURRENT_STATE.md`,
el manuscrito, los contratos ni la nota revisada. No hay commit ni push.
