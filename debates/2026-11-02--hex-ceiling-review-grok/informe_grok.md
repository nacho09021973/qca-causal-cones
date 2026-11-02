<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 27bdf34aa39190b7eeb6489eaabe5d4555ba9c3e904941eaee3bfccd9288be78
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-02T08:02:29Z  fin: 2026-11-02T08:23:24Z
documento: /home/adnac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
documento: /home/adnac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: 61232d7 ; sha256 de la copia enviada 29d88bf0de0f09f5121b277f7e1dd3fcb68cf441df1eafc0876c6519255bb244
documento: /home/adnac/qca-causal-cones/scripts/verify_hex_ceiling_gate.py ; último commit observado: b1a84a3 ; sha256 de la copia enviada d1734d8e3dc14b1579cddfd9875e3fd0a1da7cbeb9a9c7e0f2865a18827de348
documento: /home/adnac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
documento: /home/adnac/qca-causal-cones/scripts/explore_hex_saturation_support.py ; último commit observado: 61232d7 ; sha256 de la copia enviada 1388975d0346d599d2f36be45258f277c1addc3dc714d560f9f40b4ad88bb218
entrada_grok.txt sha256 64e38b3b420f0a2d1b697c7a50e125c0bdc46632c9324abd4314f067a9d2feaf
respuesta sha256 973d9374856a6e4bcc68b25a8b4081ef7464252958fc6a003c18d0d67f9ca086
-->

**Dictamen global: REPAIR_REQUIRED.** Las fórmulas de T1 y la imposibilidad de saturar con soporte mínimo son correctas; las reconstruí por otra vía. No confirmo el recuento 24/24: no ejecuté nada. Hay dos reparaciones obligatorias (cierre de L0 según el contrato, y el cuantificador del rango en el verificador). El resto son aclaraciones.

## 1. L0 — REPAIR_REQUIRED

La reducción de rejilla es correcta. Con \(g_1=(1,0)\), \(g_2=(1/2,\sqrt3/2)\), \(d=pg_1+qg_2\) y \(h=ag_1+bg_2\),

\[
h\cdot\mathrm{Rot}_{90}(d)=\frac{\sqrt3}{2}(bp-aq)\in\frac{\sqrt3}{2}\mathbb Z.
\]

La normal unitaria exterior de la arista es \(\pm\mathrm{Rot}_{90}(d)/|d|\), así que \(h\cdot n_f=m_h\delta\) con \(\delta=\sqrt3/(2|d|)\) y \(m_h\in\mathbb Z\). Los vértices de \(C=\mathrm{conv}\,F\) están en \(F\subset\Lambda\), luego la arista une puntos de la rejilla. El hexágono regular centrado en el origen es centralmente simétrico, así que sus vértices vienen en pares \(\pm v\) y \(h_C(n_f)=N\delta\) con \(|m_h|\le N\). Si el vector más largo de \(F\) tiene longitud 1, el circunradio es 1 (el máximo de \(|x|\) se alcanza en un vértice) y \(h_C(n_f)=r_\mathrm{in}=\sqrt3/2\).

La aplicación escalar también cuadra. Con \(U(0)=I\) y \(p(s)=\langle y,U(s n_f/\delta)x\rangle\),

\[
p(s)=\sum_{|m|\le N}c_m e^{-ims},\qquad |p|\le 1.
\]

Bernstein escalar da \(|p'(0)|\le N\). Si \(t\) es el parámetro de \(U(t n_f)\), entonces \(s=\delta t\) y \(|\langle y,\partial_t U(0)\,x\rangle|\le N\delta=h_C(n_f)\). Con \(A(n)=i\partial_t U(tn)|_{0}\),

\[
\|A(n_f)\|\le h_C(n_f)=r_\mathrm{in}.
\]

Basta una normal de faceta: la isotropía hace \(\|A(n)\|\) independiente de la dirección y \(r_\mathrm{in}=\min_{|n|=1}h_C(n)\) se alcanza ahí. El paso \(\|A(n_f)\|=c_0\) es cierto porque \(A\) es hermítica: si \(\widetilde U(0)=I\) y \(\widetilde U\widetilde U^\dagger=I\), la derivada en 0 es antihermítica, así que \(A=i\,d\widetilde U\) es hermítica y \(A(n_f)^2=c_0^2 I\) implica espectro \(\{\pm c_0\}\). Esa frase no está en el §1; conviene escribirla. Sin hermiticidad, \(M^2=c_0^2 I\) no fija la norma de operador.

El verificador solo certifica la identidad del producto mixto (`check_L0_grid`). El propio docstring deja Bernstein fuera.

**Reparación R1.** Informe §1, la frase que concluye \(|p'(0)|\le N\). Lo que falla: la sec. 2 del contrato cierra L0 solo si la desigualdad se prueba en el repo o se cita con página de una fuente leída en este gate. El texto la nombra como arte previo y el veredicto es `PROVED_IN_REPO`. La aplicación del enunciado clásico (orden \(N\), constante \(N\)) es la correcta; el agujero es de cierre, no de factor. Lo cierra una cita con página, o una prueba corta de Bernstein escalar en el informe. Hasta entonces la etiqueta honesta es `CITED_…` incompleta, no `PROVED_IN_REPO`.

## 2. T1 — REPAIR_REQUIRED

La reducción al producto es correcta. Con \(D_j=\exp(-i(k\cdot a_j)\sigma_z)\) y \(G_1=I\), \(G_2=C_1\), \(G_3=C_2C_1\),

\[
C_3D_3C_2D_2C_1D_1=(C_3C_2C_1)\prod_{j=3}^{1} G_j^\dagger D_j G_j.
\]

El nodo hace \(C_3C_2C_1\) escalar. Cada conjugado es \(\exp(-i(k\cdot a_j)\tau_j)\) con \(\tau_j=t_j\cdot\sigma\) y \(|t_j|=1\). Los tres vectores de Bloch quedan libres salvo una rotación global: \(C_1\) mueve \(t_2\) y \(C_2\) mueve \(t_3\) con independencia. En \(k=0\) cada factor es \(I\), así que el término lineal no depende del orden:

\[
A(k)=\sum_{j=1}^3 (k\cdot a_j)\tau_j,\qquad A(k)^2=(k^T Mk)\,I,\quad M=\sum_{ij}g_{ij}a_ia_j^T.
\]

Con \(a_j\) de longitud \(\ell\) a \(120^\circ\) y \(a_1+a_2+a_3=0\), \(\sum_i a_ia_i^T=(3/2)\ell^2 I\) y \(\sum_{i\neq j}a_ia_j^T=-(3/2)\ell^2 I\). Si \(g_{ij}=g\),

\[
M=\frac32\ell^2(1-g)I,\qquad c_{0,\mathrm{raw}}^2=\frac32\ell^2(1-g).
\]

La parte sin traza de \(M\) es lineal en \((g_{12},g_{13},g_{23})\). Cada par \(i\neq j\) aporta, en las coordenadas \(((M_{xx}-M_{yy})/2,\,M_{xy})\), un vector de ángulo doble \(\omega_i+\omega_j\): los tres ángulos son \(2\theta_0\), \(2\theta_0+2\pi/3\), \(2\theta_0+4\pi/3\). En \(\mathbb R^2\), tres vectores a \(120^\circ\) tienen rango 2 y núcleo exactamente \((1,1,1)\). El menor \(2\times 2\) vale \(-\ell^4\sqrt3/2\), constante, para todo \(\theta_0\). Por tanto isotropía \(\Leftrightarrow\) solapes iguales. El núcleo \((1,1,1)\) sí queda certificado: `jac * (1,1,1)` es la expresión nula.

La Gramiana \( (1-g)I+g\,11^T \) tiene autovalores \(1+2g\) (simple) y \(1-g\) (doble), luego es realizable en la esfera de Bloch si y solo si \(-1/2\le g\le 1\).

Los desplazamientos del producto son \(\varepsilon_1 a_1+\varepsilon_2 a_2+\varepsilon_3 a_3\) con \(\varepsilon_j=\pm 1\), es decir \(\{0,\pm 2a_j\}\). El hexágono regular exige los seis vértices en \(F\), así que el paso más largo es \(2\ell\) y \(c_0=c_{0,\mathrm{raw}}/(2\ell)\). Con \(r_\mathrm{in}=\sqrt3/2\),

\[
\frac{c_0}{r_\mathrm{in}}=\frac{\sqrt{1-g}}{\sqrt2}\le\frac{\sqrt3}{2},
\]

igualdad si y solo si \(g=-1/2\). En ese punto \(c_0=3/4\). El testigo \(t_j=(\cos 2\pi j/3,\sin 2\pi j/3,0)\) tiene solapes \(-1/2\). El coeficiente de \(+2a_0\) es \(P_-^{(2)}P_-^{(1)}P_+^{(0)}\) y el de \(-2a_0\) es \(P_+^{(2)}P_+^{(1)}P_-^{(0)}\); ambos son no nulos sobre \(|\pm x\rangle\), y la equivariancia por \(120^\circ\) arrastra los seis vértices. El símbolo es unitario por construcción, \(U(0)=I\) y el cono es el de la fórmula. El supremo se alcanza dentro de la clase. ADMP, con los \(\tau_i\) de la ec. (5) y \(g=1/3\), da \(c_0=1/2\). JDW L6d está en la misma subclase (tres saltos antipodales a \(120^\circ\)) y la tabla de entrada le asigna \(c_0=3/4\), luego \(g=-1/2\). La diferencia ADMP–JDW es el solape. \(\xi=\sqrt5/3\) es la componente \(z\), no un ángulo.

La frase «la cota solo usa nodo e isotropía; el hexágono solo restringe más» hay que precisarla: el hexágono fija el denominador \(2\ell\). No cambia el supremo, porque \(g=-1/2\) se realiza con los seis vértices.

**Reparación R2.** `check_T1_algebra`, el `record` cuyo rótulo dice «rank 2 for every theta0» y cuyo predicado es

```python
sp.simplify(jac[:, :2].det()) != 0 or sp.simplify(jac[:, 1:].det()) != 0
```

Qué falla: `expr != 0` solo dice que el menor no es el elemento nulo del anillo. Una expresión con ceros aislados (ambos menores múltiplos de \(\sin\theta_0\), por ejemplo) pasaría el test y el rango caería en esos \(\theta_0\). El informe atribuye al verificador el cuantificador universal. Lo cierra sustituir el predicado por la igualdad al constante \(-\ell^4\sqrt3/2\) (o a su cuadrado positivo, libre de \(\theta_0\)). La afirmación matemática es verdadera; el certificado escrito no la prueba.

## 3. T2, paso de saturación — PASS

Si \(c_0=r_\mathrm{in}\) y \(Ax=c_0 x\) con \(|x|=1\), el mismo \(p\) cumple \(p(0)=1\) y \(p'(0)=-iN\): de \(i\partial_t U\,x=N\delta\,x\) sale \(\langle x,\partial_t U\,x\rangle=-iN\delta=\delta p'(0)\). Con \(z=e^{is}\) y \(P(z)=z^N p\), \(P\) es polinomio, \(|P|=|p|\le 1\) en la circunferencia y, por el módulo máximo, \(|P|\le 1\) en el disco. \(P(1)=1\). Además \(dP/ds=izP'\), y en \(s=0\)

\[
\frac{dP}{ds}=iN\cdot 1+(-iN)=0\implies P'(1)=0.
\]

El lema de Julia en la forma usada es el correcto: si \(f(\mathbb D)\subset\mathbb D\), \(f(1)=1\) y la derivada angular existe, esa derivada es real y \(\ge 0\), y vale 0 solo para \(f\equiv 1\) (la desigualdad de Julia con \(\alpha=0\) fuerza \(f=1\)). Luego \(P\equiv 1\) y \(p(s)=e^{-iNs}\). Como \(|\langle x,Ux\rangle|=1=\|Ux\|\), Cauchy–Schwarz da \(U(t n_f)x=e^{-ir_\mathrm{in}t}x\). Para el autovector negativo, \(q(s)=p(-s)\) cae en el mismo caso, así que \(p(s)=e^{iNs}\). En la base propia,

\[
U(t n_f)=e^{-ir_\mathrm{in}t}P_+(n_f)+e^{ir_\mathrm{in}t}P_-(n_f).
\]

Por unicidad de Fourier, la suma de \(A_h\) en la arista superior (\(h\cdot n_f=+r_\mathrm{in}\)) es \(P_+\), la inferior es \(P_-\) y cada capa intermedia suma 0. El signo cuadra con el convenio \(e^{-ik\cdot h}\): la capa de proyección máxima oscila como \(e^{-ir t}\). El paso no usa la forma producto; vale para cualquier símbolo unitario de \(W_\mathrm{hex}\) con \(c_0=r_\mathrm{in}\). Conviene nombrar el módulo máximo en la frase que pone \(|P|\le 1\) en el disco cerrado. La página de Julia está marcada `[UNVERIFIED]`; el enunciado aplicado es el que hace falta, y el contrato no pide esa página.

## 4. T2, certificado mínimo — PASS

La forma normal es lícita: una conjugación constante gira el triedro de Bloch hasta \(A(n)=r_\mathrm{in}(n_x\sigma_x+n_y\sigma_y)\) (SU(2) actúa por SO(3) y absorbe la orientación), y un giro espacial compensado por un giro de Bloch alrededor de \(z\) lleva los vértices a \((\cos k\pi/3,\sin k\pi/3)\). Las normales de faceta quedan en \(30^\circ\), \(90^\circ\), \(150^\circ\). En cada una las capas son dos vértices / dos vértices más el origen / dos vértices. Lo comprobé por productos escalares: para \(n=(\sqrt3/2,1/2)\) la capa alta es \(\{v_0,v_1\}\), y análogamente \(\{v_1,v_2\}\) y \(\{v_2,v_3\}\).

Las nueve ecuaciones matriciales son compatibles y dejan libre \(X_0=S\). Sumando las seis ecuaciones de arista, cada vértice aparece dos veces y \(P_++P_-=I\), así que \(\sum_{j=0}^5 X_j=3I/2\). Las tres capas medias dan \(\sum X_j=-3Z\). Luego \(Z=-I/2\). La solución general es

\begin{align*}
X_1&=P_0-S,\\
X_2&=P_1-P_0+S,\\
X_3&=I/2-S,\\
X_4&=I/2-P_0+S,\\
X_5&=M_2-S,
\end{align*}

con \(P_k=(I+n_k\cdot\sigma)/2\) y \(M_k=I-P_k\). La identidad \(P_0-P_1+P_2=I/2\) (porque \(n_0-n_1+n_2=0\)) hace que las nueve ecuaciones cierren para todo \(S\).

La unitariedad por coeficientes de Fourier está completa: \(\sum_h A_{h+d}A_h^\dagger=\delta_{d0}I\) para todo \(d\) ya equivale a \(UU^\dagger=I\) en el toro, y para matrices \(2\times 2\) eso implica \(U^\dagger U=I\). Incluir las dos familias no quita soluciones.

El vacío real no depende del discriminante \(-1/12\), que no recomputé. Sale por los diámetros. El modo \(v_0-v_3=(2,0)\) tiene un solo par, luego \(S(I/2-S)^\dagger=0\), es decir \(SS^\dagger=S/2\). Tomando adjuntos, \(S=S^\dagger\) y \(S^2=S/2\). Los únicos casos son \(S=0\), \(S=I/2\) y \(S=\tfrac12|\psi\rangle\langle\psi|\).

- Si \(S=0\), el diámetro \(v_1-v_4\) da \(X_1X_4^\dagger=P_0(I/2-P_0)=-P_0/2\neq 0\).
- Si \(S=I/2\), el mismo modo da \((P_0-I/2)M_0=-M_0/2\neq 0\).
- Si \(S=\tfrac12|\psi\rangle\langle\psi|\) y \(X_1X_4^\dagger=0\), entonces \(|\langle n_0|\psi\rangle|=1\), luego \(S=P_0/2\). En ese punto \(X_2=P_1-P_0/2\) y \(X_5=I/2-X_2\), y la entrada \((0,0)\) de \(X_2X_5\) vale \(-1/8\neq 0\). El modo \(v_2-v_5\) es exactamente ese producto.

No hay matriz compleja \(S\) que satisfaga capas y unitariedad, y por tanto ninguna real. El certificado por base de Gröbner (un elemento del ideal sin raíz real) tendría la misma consecuencia si el cálculo es correcto; la lógica del `record` final es válida y, si la base fuera \(\{1\}\), el test del grado 2 fallaría en cerrado, lo cual es aceptable. No hace falta fiarse del polinomio concreto \(x^2-x/2+1/12\).

El control cuadrado prueba algo concreto y no es tautológico. Para \(F\subset\{0\}\cup\{(\pm1,\pm1)\}\), con normales \(e_x,e_y\), el caminante \(e^{-ik_x\sigma_x}e^{-ik_y\sigma_y}\) tiene coeficientes \(P_x^\pm P_y^\pm\), soporte exactamente esos cuatro vértices, \(Z=0\) y \(A(n)=n_x\sigma_x+n_y\sigma_y\), que satura \(h_C(e_x)=1\). Esas matrices cumplen las ecuaciones de capa (por ejemplo \(P_xP_y+P_xP_y^-=P_x\)) y la unitariedad. El control muestra que el mismo generador de ecuaciones acepta un saturador conocido: un signo global mal puesto lo rechazaría. No demuestra el ideal hexagonal; esa mitad ya quedó cerrada por los diámetros. La frase del informe que separa «consistente sobre \(\mathbb C\)» de «contradicción real» habla del anillo de polinomios en las ocho coordenadas reales: soluciones complejas de esas coordenadas no fabrican una matriz del caminante. En el problema matricial el sistema es inconsistente también sobre \(\mathbb C\), como muestra \(SS^\dagger=S/2\).

Dentro de esta subclase, \(c_0=r_\mathrm{in}\) es imposible para todo símbolo \(s=2\) con ese \(F\), haya o no forma producto. El informe no afirma un supremo más fino que el \(\sqrt3/2\) heredado de T1, que está contenido (el testigo, normalizado por \(2\), cae en \(\{0\}\cup\mathrm{vert}(H)\)).

## 5. Alcance y código — REPAIR_REQUIRED

| Veredicto del informe | Lectura |
|---|---|
| L0 `PROVED_IN_REPO` | La rejilla está en el repo; Bernstein, no. Choca con la sec. 2. Es R1. |
| T1 `GAP_PROVED_IN_CLASS`, supremo \(\sqrt3/2\), alcanzado | Correcto para la subclase \(n=3\) antipodal. HX1 queda confirmada ahí. |
| T2 `PROVED_FOR_MINIMAL_SUPPORT` | Correcto, y vale para todo símbolo \(s=2\) con ese \(F\), no solo para productos. El texto lo dice. |
| T2 `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS` | Correcto. No se extrapola a soportes mayores ni a \(s>2\). |

El resultado mínimo es más amplio que \(W_\mathrm{hex}\) y está declarado como tal; implica el caso producto. No vi una afirmación que extienda el hueco a toda \(W_\mathrm{hex}\), ni a \(s>2\), ni a otras redes. HX2 general sigue abierto. L6c (19 puntos) queda fuera, como dice el informe.

Checks débiles, distintos de un fallo de enunciado:

- `bool(R3/2 < 1)` solo compara dos constantes. Tras la cota del cociente es el paso final, y no prueba nada más.
- El rango «para todo \(\theta_0\)» es R2.
- El control cuadrado, con la sustitución del caminante conocido dentro de `eqs`, sí ata el generador de ecuaciones. La comparación `Groebner != {1}` aislada sería débil; va acompañada de esa sustitución.

El script exploratorio está tratado como pide la sec. 5. El docstring lo marca como no certificado, avisa de que una base distinta de \(\{1\}\) no decide solubilidad real, y el informe no mete el corte a 900 s ni el caso `ball19` en ningún veredicto. Un base \(\{1\}\) sobre ese anillo sí habría probado inconsistencia; no la obtuvieron, y no infieren rigidez de la búsqueda fallida. Correcto.

## Reparaciones obligatorias

1. **R1 — L0, informe §1 (Bernstein) y el veredicto `PROVED_IN_REPO`.** Falla el cierre que exige la sec. 2 del contrato: la desigualdad se usa sin prueba en el repo y sin página. La rejilla, la simetría, el paso de \(\langle y,Ux\rangle\) a \(\|A(n_f)\|\) y la igualdad \(\|A\|=c_0\) (con \(A\) hermítica) están bien. Lo cierra una cita con página leída en este gate, o una prueba escrita de Bernstein escalar, y alinear la etiqueta.
2. **R2 — `verify_hex_ceiling_gate.py`, `check_T1_algebra`, predicado del rango.** Falla el cuantificador «para todo \(\theta_0\)»: se comprueba que un menor no es idénticamente cero. El núcleo \((1,1,1)\) sí está bien certificado, y el menor es de hecho el constante \(-\ell^4\sqrt3/2\). Lo cierra afirmar esa constante (libre de \(\theta_0\)).

No hay más reparaciones obligatorias. Aclaraciones que no cambian los enunciados: escribir que \(A\) es hermítica al pasar de \(A^2=c_0^2 I\) a la norma; nombrar el módulo máximo antes de Julia; decir que el hexágono fija \(L=2\ell\); llamar a \(\xi=\sqrt5/3\) componente y no ángulo; recordar que el control cuadrado acredita el generador de ecuaciones en el cuadrado, mientras el vacío hexagonal queda en el argumento de los diámetros.
