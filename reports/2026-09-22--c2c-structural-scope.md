# C2c — alcance estructural de la compensación espectral

Fecha: 2026-09-22. Autor: Codex, agente `/root`.
**Estado: `REPAIRED / REVIEW_PENDING`.**
Reparación registrada: 2026-09-23, sobre el objeto original `fa9c07f`.

Esta es la ejecución analítica de C2c, no su revisión independiente ni una
promoción a PASS. C2b se usa como entrada certificada para su par congelado;
las extensiones demostradas en esta nota requieren su propia revisión.

## 1. Snapshot obligatorio y resultado de alcance

Snapshot único de entrada:
`f4f937e102def05f8797a94e256a460d81b0cc33`, rama
`research/b-infinity-post-s4-gate`.

Ese commit, creado antes de ejecutar C2c, contiene exactamente:

- `reports/2026-09-22--c2b-independent-review.md`;
- la actualización de `state/CURRENT_STATE.md`;
- `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md`.

Título: `Promote C2b PASS and open C2c structural-scope gate`.
No se hizo push. El trabajo no versionado ajeno a ese paquete se preservó.
Las entradas científicas de esta ejecución se consultaron en ese SHA;
esta nota es un artefacto posterior y no forma parte del snapshot.

La conclusión estructural principal, probada en §4, es:

\[
\boxed{T_N=o(\mathcal Q_N),\quad
\mathrm{Lin}_N=o(\mathcal Q_N)
\quad\Longrightarrow\quad
\frac{(L_{PP},L_{QQ},L_{PQ}+L_{QP})}{\mathcal Q_N}
\longrightarrow(1,1,-2).}
\tag{C1}
\]

Se presupone \(\mathcal Q_N>0\) finalmente y las hipótesis operativas
explicitadas en §3. No se necesita fijar su potencia de decaimiento.
El criterio es suficiente, no se afirma que sea necesario ni óptimo.
Para las coherencias individuales hace falta además
\(\lvert\langle r,Ed_P\rangle\rvert=o(\mathcal Q_N)\).

Para los dieciséis pares **originales**, la auditoría de dependencias y el
argumento de no anulación de §§5–7 dan una derivación más específica:

\[
\mathcal Q_{M,D,N}=N^{-3}\mathscr A_{M,D}(\sqrt N)
 +O(N^{-13/4}),\qquad
\lvert\langle r,Ed_P\rangle\rvert=O(N^{-7/2}),
\tag{C2}
\]

con coeficientes definidos explícitamente por integrales finitas en §6,
acotados superiormente y con una cota inferior positiva uniforme.
Aquí y en adelante \(D=M_B\). No se copia el coeficiente de
\(\sigma_2/I\): con detectores de rango uno se retienen los términos
cruzados entre bandas de Weyl. La clasificación completa figura en §8.

La obtención de (C2) usa el campo radial y los presupuestos de transferencia
ya escritos en C2/C2a, comprobando sus hipótesis para cada familia, más
álgebra de una matriz de Gram finita. No introduce una nueva saddle
analysis, cálculo numérico, simulación, barrido o ajuste. La nueva
generalización analítica se identifica como tal y no se atribuye al PASS
previo de C2a.

## 2. Fuentes y los cuatro niveles A–D

Entradas del snapshot:

| Entrada | Uso concreto |
| --- | --- |
| [Contrato C2c](../theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md) | S1–S5 y restricciones de método |
| [Estado §10.1](../state/CURRENT_STATE.md) | C1/C2a/C2b PASS; C2c UNBLOCKED; C3 y E/AdS separados |
| [Revisión C2b](2026-09-22--c2b-independent-review.md), §§4–9 y 12 | Identidades, errores explícitos y alcance complejo de C2a |
| [Derivación C2a](2026-09-22--c2a-oscillatory-transfer.md), §§2–6 | Lemas matriciales, integración angular y presupuestos separados |
| [Revisión C2a](2026-09-22--c2a-independent-review.md), §§2–7 | Hipótesis y validez de los pasos importados |
| [Representación C2](2026-09-22--c2-projected-response-representation.md), (2)–(3), (8)–(9) | Representación exacta para M y D; campo radial para los cuatro M |
| [Derivación C1](2026-09-22--ir-projection-leakage-and-conditioning.md), §3, y [revisión C1](2026-09-22--c1-leakage-independent-review.md), §§2–5 | Fuentes de los cuatro encoders, borde, uniformidad y aliases |
| [Manuscrito](../papers/ir-corona/ir-corona.md), §§2–3 y Teorema 4.1 | Walk, normalizaciones, dieciséis pares y cota regional |

Los contratos C1/C2/C3, C2a y C2b conservan sus alcances. Se excluyen las
consecuencias de las notas anteriores basadas en la ley total del observable.

| Nivel | Qué se establece y qué se necesita |
| --- | --- |
| A. Algebraico | B1 y los cuatro bloques; condiciones de proyector, referencia y hermiticidad, sin una potencia asintótica |
| B. Localidad | Compensación en Bob a partir de una fuente local y una cota de propagación; la exponencial requiere el Teorema 4.1 del walk congelado |
| C. Asintótico relativo | (C1) separa el patrón de cualquier ley \(N^{-3}\); la comparación de escalas y el término lineal son hipótesis sustantivas |
| D. Protocolo cuantitativo | (C2), sus coeficientes, el exponente tres, el corte y la geometría se verifican en los dieciséis pares originales; no son universales para cualquier QCA |

La afirmación \(\mathcal Q_N\sim N^{-3}A_N\) pertenece a la parte
cuantitativa C/D: no se necesita para formular el criterio estructural (C1).

## 3. Hipótesis y extensión de A/B

### 3.1. Enunciado abstracto operativo

Para cada N, sean \(\mathcal H_N\) un espacio de Hilbert,
\(\|\phi_N\|=1\), \(V_N,U_N\) unitarios, y \(P_N\) un proyector
ortogonal con \(P_N\phi_N=\phi_N\). Sean \(Q_N=I-P_N\),
\(0\le E_N\le I\), y \(A_N^{\mathrm{sp}},B_N^{\mathrm{sp}}\)
proyectores espaciales tales que

\[
a=(U_N-I)\phi_N=A_N^{\mathrm{sp}}a,\qquad
E_N=B_N^{\mathrm{sp}}E_NB_N^{\mathrm{sp}},\qquad
T_N=\|B_N^{\mathrm{sp}}V_NA_N^{\mathrm{sp}}\|.
\]

No se confunden estos proyectores espaciales con los coeficientes
oscilatorios. Se definen \(r=V_N\phi_N\), \(d=V_Na\),
\(d_P=V_NP_Na\), \(d_Q=V_NQ_Na\),
\(\Delta=|U_N\phi_N\rangle\langle U_N\phi_N|-|\phi_N\rangle\langle\phi_N|\)
y \(L_{XY}=\operatorname{tr}(E_NV_NX\Delta YV_N^\dagger)\),
para \(X,Y\in\{P_N,Q_N\}\). Son los bloques de la perturbación
inicial evolucionada.

Las identidades y cotas siguientes no requieren \([V_N,P_N]=0\).
Esa conmutación sí permite identificar los vectores con las proyecciones
del estado **final**, \(d_P=P_Nd\), \(d_Q=Q_Nd\), y está satisfecha
en el protocolo homogéneo congelado.

### 3.2. Matriz de dependencias

| Paso | Hipótesis utilizadas | Hipótesis que no requiere |
| --- | --- | --- |
| \(d_Q=d-d_P\) | \(Q=I-P\), linealidad de V | Ortogonalidad, positividad, conmutación, Fourier, localidad |
| Cuatro bloques por inserción de \(P+Q\) | Complementariedad; para las fórmulas de rango uno se usa \(P=P^\dagger\) | Corte duro y conmutación con V |
| Ausencia de referencia en QQ/PQ/QP | \(P\phi=\phi\), \(Q\phi=0\) | Una pequeñez asintótica de la referencia |
| \(L_{QP}=\overline{L_{PQ}}\), término lineal real | Hermiticidad de E y de \(\Delta\) | Positividad de E |
| \(L_{QQ},\mathcal Q_N\ge0\), Cauchy–Schwarz con \(E^{1/2}\) | \(E\ge0\) | Conmutación de E con P |
| Normas \(\|r\|\le1\), \(\|d_P\|,\|a\|\le2\) | Normalización, unitariedad de U/V, contractividad de P | Conteo de sitios |
| \(\|E^{1/2}d\|\le2T_N\) | Soporte de a y E, \(0\le E\le I\) y normas anteriores | Localidad de Pa o Qa |
| Tasa exponencial de \(T_N\) | Teorema 4.1, símbolo y geometría concretos | Asintótica de L o Teorema 4.4 |
| Patrón relativo | Dos comparaciones de escalas de (C1) | Una potencia específica de N o un proyector duro |
| Coherencias individuales relativas | Control complejo adicional | Inferencia de parte imaginaria desde parte real |

### 3.3. Cotas reutilizables

Poniendo \(c_N=\langle r,Ed_P\rangle\) y
\(\mathcal Q_N=\|E^{1/2}d_P\|^2\), la expansión de C2b, aplicada
con esas hipótesis, da

\[
\begin{aligned}
L_{PP}&=2\operatorname{Re}c_N+\mathcal Q_N,\\
L_{QQ}&=\mathcal Q_N+\rho_N,\quad
 |\rho_N|\le8T_N+4T_N^2,\\
L_{PQ}&=-\overline{c_N}-\mathcal Q_N+\eta_N,\quad |\eta_N|\le6T_N,\\
L_{QP}&=-c_N-\mathcal Q_N+\overline{\eta_N}.
\end{aligned}
\tag{C3}
\]

Aquí \(\rho_N\) es un resto escalar, no una coordenada radial ni un
estado. Para ver que las constantes se conservan, bastan
\(\|E^{1/2}d_P\|\le2\), \(\|E^{1/2}r\|\le1\),
\(\|E^{1/2}d\|\le2T_N\); los dos errores son
\(-2\operatorname{Re}\langle d_P,Ed\rangle+\langle d,Ed\rangle\)
y \(\eta_N=\langle d,E(r+d_P)\rangle\). No se añade ninguna
hipótesis específica sobre \(\sigma_2\) o sobre un detector identidad.

Para los cuatro encoders del manuscrito, M es hermítico y
\(U_M=\exp(i\pi F_NM/2)\) es unitario y coincide con I fuera de Alice.
El recurso es el mismo, normalizado, y \(P\phi_N=\phi_N\).
Para los cuatro detectores, \(D=I\) o \((I+\sigma_j)/2\), se tiene
\(0\le D\le I\), \(E=h_ND\),
\(E^{1/2}=\sqrt{h_N}D^{1/2}\) y soporte en Bob. El Teorema 4.1
no depende del espinor de a ni del detector. Por tanto (C3) y

\[
\|E^{1/2}(d_P+d_Q)\|\le2T_N,\qquad
T_N\le9N^4e^{-JN},\quad J=(1-\sqrt3/2)\log2>0
\tag{C4}
\]

valen para los dieciséis pares, para todo entero \(N\ge2\), con las
mismas constantes. Esta extensión de A/B queda demostrada por
verificación directa de hipótesis; no por analogía con C2b.

## 4. Criterio estructural sin potencia prefijada

Supóngase, además de §3.1, que \(\mathcal Q_N>0\) para N grande,
\(T_N/\mathcal Q_N\to0\) y
\(\mathrm{Lin}_N/\mathcal Q_N\to0\). Como \(T_N\le1\),
\(T_N^2/\mathcal Q_N\le T_N/\mathcal Q_N\to0\).
Dividir (C3) y su suma de coherencias por \(\mathcal Q_N\) demuestra

\[
\begin{aligned}
L_{PP}/\mathcal Q_N&=1+\mathrm{Lin}_N/\mathcal Q_N\to1,\\
L_{QQ}/\mathcal Q_N&=1+O((T_N+T_N^2)/\mathcal Q_N)\to1,\\
(L_{PQ}+L_{QP})/\mathcal Q_N
 &=-2-\mathrm{Lin}_N/\mathcal Q_N+O(T_N/\mathcal Q_N)\to-2.
\end{aligned}
\]

Esto prueba (C1). Si se añade \(|c_N|/\mathcal Q_N\to0\),
las dos últimas identidades individuales de (C3) dan
\(L_{PQ}/\mathcal Q_N\to-1\), \(L_{QP}/\mathcal Q_N\to-1\)
en módulo complejo. Sin esa hipótesis extra no se afirma el resultado
individual.

No se requiere que \(T_N\) sea exponencial: basta la comparación
indicada. Tampoco se requiere Fourier, un corte duro, una dimensión fija
o una velocidad emergente para este enunciado abstracto. En cada modelo
habría que verificar sus hipótesis. Si \(\mathcal Q_N\) tiene ceros o
es demasiado pequeña, el enunciado no se aplica allí; restringirlo a una
subsucesión exige declararla y verificar las comparaciones en ella.

La condición \(\mathrm{Lin}_N=o(\mathcal Q_N)\) no es opcional.
Como prueba analítica de ese límite lógico, considérese únicamente el
álgebra en \(\mathbb C^2\): \(A^{\mathrm{sp}}=|e_1\rangle\langle e_1|\),
\(B^{\mathrm{sp}}=E=|e_2\rangle\langle e_2|\), \(V=I\),
\(\phi=(e_1+e_2)/\sqrt2\), \(P=|\phi\rangle\langle\phi|\),
\(U=\operatorname{diag}(-1,1)\). Se obtiene
\(a=-\sqrt2e_1\), \(d_P=-\phi\), \(T=0\),
\(\mathcal Q=1/2\), \(c=-1/2\). Así

\[
(L_{PP},L_{QQ},L_{PQ}+L_{QP})=(-1/2,1/2,0).
\]

La compensación localizada es exacta, pero no da el patrón pretendido
porque \(\mathrm{Lin}=-2\mathcal Q\). Este contraejemplo de álgebra
finita no es un nuevo modelo QCA ni una modificación del protocolo: sólo
refuta la implicación abstracta que omitiría el control lineal.

## 5. Auditoría de transferencia a los dieciséis pares

El PASS anterior de C2a cubría sólo \(\sigma_2/I\). Esta sección
comprueba qué hipótesis de sus lemas sobreviven al cambiar M y D dentro
de las listas originales. Se conserva \(K=\sqrt N\), \(b=1/4\),
\(u=(1,1,1)\), \(\beta=\Phi_0(b)>0\), y
\(\zeta_M=M\downarrow\). El símbolo \(\beta\) en esta nota es sólo
ese escalar del recurso; no es la matriz beta de H1.

### 5.1. Fuente y campo radial

C1 demuestra para todos los M la fuente exacta radial
\(a_N(x)=N^{-3/2}A_M(x/N)\). La reducción C2 §4 precisa sus dos
transformadas escalares:

\[
\widehat A_M(k)=\widehat c(k)\downarrow+i\widehat s(k)\zeta_M,
\quad \widehat s(k)=64\pi^2\beta\cos(bk)k^{-4}
 +\beta_5\sin(bk)k^{-5}+O(k^{-6}),\quad \widehat c(k)=O(k^{-6}).
\]

Las funciones escalares son comunes a los cuatro M;
\(\zeta_M\in\{\downarrow,\uparrow,-i\uparrow,-\downarrow\}\).
Su norma es uno. La reducción radial exacta C2 (8)–(9), comprobada en
C2a, es por tanto la misma identidad matricial actuando sobre otro
espinor. En Bob da

\[
D^W_{M,K}(Y)=-\frac{i16\beta}{\rho K^3}
\sum_{\sigma,\epsilon=\pm1}
\frac{\Pi_\sigma(n)\zeta_M
\cos[(\rho+\sigma+\epsilon b)K]}{\rho+\sigma+\epsilon b}
 +O(K^{-4}),
\tag{C5}
\]

con \(\rho=|Y|\), \(n=Y/\rho\),
\(J(n)=n_1\sigma_1-n_2\sigma_2+n_3\sigma_3\),
\(\Pi_\sigma(n)=(I+\sigma J(n))/2\). Estos \(\Pi_\sigma\) son
proyectores de bandas Weyl, distintos del corte P.
Todos los denominadores son \(\ge\gamma=\sqrt3-3/2>0\).

La justificación del resto es la ya escrita: la parte \(\widehat c\)
y el resto \(O(k^{-6})\) dan \(O(K^{-4})\) absolutamente después
de la reducción angular; los términos \(k^{-5}\) de \(\widehat s\)
y la pieza subdominante de \(j_1\) usan las mismas fases radiales
no nulas para ganar una potencia. Cambiar el espinor unitario no cambia
las cotas matriciales. Se obtiene uniformidad en Bob y en los cuatro M,
sin recalcular saddles.

### 5.2. Emparejamiento complejo lineal

Para D fijo se sustituye el test de C2a por
\(w_{D,N}=hDR_N\). La transferencia se comprueba lema a lema, no sólo
por la frase «D es constante». Como \(D=D^\dagger\), \(0\le D\le I\) y
\(\|D\|=\|D^{1/2}\|\le1\), para toda función matricial \(F\) y todo
multiíndice angular \(\alpha\) se tiene
\[
\|D F\|_{C^{|\alpha|}}\le\|F\|_{C^{|\alpha|}},\qquad
\|D^{1/2}F\|_{L^2}\le\|F\|_{L^2}.
\tag{C6a}
\]
Estas desigualdades son las únicas propiedades del detector usadas en los
lemas siguientes; no se conmuta D con \(J(n)\) ni con \(\Pi_\sigma(n)\).

La fuente \(A_M\) conserva radialidad, borde y soporte para los cuatro
espinores \(\zeta_M\), todos de norma uno. En el lema angular (C2a (6)),
cada componente de \(D R_N\) tiene la misma regularidad y la norma
\(C^6\) queda acotada por la de \(R_N\) mediante (C6a). Por tanto se
conserva la ganancia \(O(r^{-1})\) y las fases radiales
\(\pm\sqrt3+(\epsilon-\eta)b-\sigma\), cuyo módulo es al menos
\(\gamma=\sqrt3-3/2\). En el muestreo (C2a (16)), multiplicar por D sólo
multiplica las transformadas por una matriz constante y conserva la cota
\(L^1\) de las imágenes. En los correctores (17)–(19), D no cambia los
soportes de los tests ni el operador diferencial local; (C6a) conserva cada
cota de resto. En el cambio de recurso (20), las cotas \(C^m\) de
\(D(R_N-R_0)\) son las de \(R_N-R_0\). Así la transferencia lineal vale
para cada M y D, con el mismo orden y constantes uniformes en la familia
finita. Esta comprobación tampoco requiere que D conmute con \(J(n)\).

Por ello el mismo presupuesto, ahora para
\(c_{M,D,N}=\langle r,Ed_P\rangle\), es:

| Pieza | Orden | Dependencia comprobada |
| --- | --- | --- |
| Referencia Weyl compleja, C2a (10)–(11) | \(K^{-7}\) | Fuente radial; test D por una función suave; frecuencias separadas |
| Imágenes y muestreo, (16) | \(K^{-8}\) | Transformadas de orden cuatro y norma \(L^1\) uniforme |
| Corrector cúbico, (17)–(18) | \(K^{-7}\) | Operador diferencial local, mismos soportes y ganancia angular |
| Resto de dispersión, (19) | \(K^{-7}\) | Dos factores Fourier de orden cuatro; \(\|D\|\le1\) |
| Cambio de recurso, (20) | \(K^{-9}\) | Mismo soporte; (C6a) y \(R_N-R_0=O(N^{-2})\) con derivadas |

Todas son cotas en módulo complejo, como explicita C2b §8. Con los
interpolantes exactos de C2 (2)–(3), incluidos aliases y suma de red,

\[
|c_{M,D,N}|=O(K^{-7})=O(N^{-7/2})
\tag{C6}
\]

para los dieciséis pares, uniformemente al ser una familia finita.

### 5.3. Transferencia cuadrática

La cota C2a (21) sólo requiere el decaimiento de \(\widehat A_M\),
las imágenes y Duhamel matricial. Para cada M da
\(\|D_{M,N}-D^W_{M,K}\|_2=O(K^{-7/2})\). Por (C6a) y (C5),
\[
\|\sqrt hD^{1/2}D^W_{M,K}\|_2=O(K^{-3}),\qquad
\|\sqrt hD^{1/2}(D_{M,N}-D^W_{M,K})\|_2=O(K^{-7/2}).
\]
Cauchy–Schwarz da, con \(\|D^{1/2}\|\le1\),
\(O(K^{-13/2})\) para la diferencia de las formas cuadráticas. En el
muestreo de \(hD_{M,N}^\dagger D D_{M,N}\), se insertan D entre los dos
factores y (C6a) conserva cada norma de C2a (23); el error sigue siendo
\(O(K^{-8})\). Los cruces \(\Pi_+D\Pi_-\) no se eliminan: se mantienen
en la matriz de Gram de §6.

Así queda justificada, para todos los pares, la transferencia separada

\[
\mathcal Q_{M,D,N}
=\int h(Y)(D^W_{M,K}(Y))^\dagger D D^W_{M,K}(Y)\,d^3Y
 +O(K^{-13/2}).
\tag{C7}
\]

Falta analizar la forma cuadrática de (C5) con D, incluyendo sus cruces.
Ese paso se hace a continuación; no se reemplaza por el resultado para I.

## 6. Coeficiente completo: matriz de Gram, sin descartar cruces

Indexemos por \(i=(\sigma,\epsilon)\in\{\pm1\}^2\) los cuatro
términos de (C5), y pongamos

\[
\alpha_i=\sigma+\epsilon b\in\{5/4,3/4,-3/4,-5/4\},\qquad
f_i(Y)=\frac{\sqrt{h(Y)}}{\rho(\rho+\alpha_i)}
D^{1/2}\Pi_\sigma(n)\zeta_M.
\]

Definimos una matriz hermítica fija, independiente de K y N,

\[
G^{M,D}_{ij}=\int_{\mathbb R^3} f_i(Y)^\dagger f_j(Y)\,d^3Y.
\tag{C8}
\]

Todas las entradas están dadas por integrales ordinarias sobre la bola
fija de Bob, sin límites impropios ni denominadores pequeños. No se evalúan
numéricamente. La matriz conserva, en particular,
\(\Pi_+D\Pi_-\), que puede ser no nulo cuando \(D\ne I\).

El término principal del campo localizado es
\(-i16\beta K^{-3}\sum_i f_i(Y)\cos[(\rho+\alpha_i)K]\).
Al cuadrarlo, la identidad producto de cosenos separa

\[
\cos[(\rho+\alpha_i)K]\cos[(\rho+\alpha_j)K]
=\tfrac12\cos[(\alpha_j-\alpha_i)K]
 +\tfrac12\cos[(2\rho+\alpha_i+\alpha_j)K].
\]

La segunda parte integra a \(O(K^{-1})\), exactamente por el argumento
de C2a §3.2: cada amplitud \(f_i^\dagger f_j\) es h por una función
suave en Bob, se anula en su frontera, y \(|\nabla\rho|=1\).
Una integración por partes con \(\nabla\rho\) da una constante uniforme,
ya que las fases adicionales son constantes en Y y tienen módulo uno.
No se deriva \(\sqrt h\) por separado ni se presupone suavidad de orden
superior a la disponible. Es el mismo control de fases \(2K\rho\) del
snapshot, aplicado a un número finito de productos cruzados.

El resto de campo en (C5) produce \(O(K^{-7})\) al cuadrar, pues
el líder localizado es \(O(K^{-3})\) y el resto \(O(K^{-4})\).
Por tanto, definiendo

\[
\mathscr A_{M,D}(K)
=128\beta^2\sum_{i,j}G^{M,D}_{ij}
\cos[(\alpha_j-\alpha_i)K],
\tag{C9}
\]

se obtiene

\[
\int h(D^W_{M,K})^\dagger D D^W_{M,K}
=K^{-6}\mathscr A_{M,D}(K)+O(K^{-7}).
\tag{C10}
\]

La suma (C9) es real porque G es hermítica y el coseno es simétrico.
En términos de \(z_i(K)=e^{i\alpha_iK}\), su forma positiva es

\[
\boxed{\mathscr A_{M,D}(K)=64\beta^2
\left[z(K)^\dagger G^{M,D}z(K)
+\overline{z(K)}^{\,\dagger}G^{M,D}\overline{z(K)}\right].}
\tag{C11}
\]

Los factores se comprueban desde \(16^2=256\), el factor \(1/2\)
del producto de cosenos y el segundo \(1/2\) al expresar coseno como
suma de exponenciales. En general (C9) puede contener las frecuencias
\(0,1/2,3/2,2,5/2\) en K; no se afirma que todas tengan coeficiente
no nulo para cada par.

Para \(D=I\), \(\Pi_+\Pi_-=0\) elimina sólo los cruces entre
bandas. Con \(\nu_\sigma^M=\|\Pi_\sigma\zeta_M\|^2\) y
\(t_{\sigma,\epsilon}=1/(\rho+\sigma+\epsilon b)\), (C9) se reduce a

\[
\begin{aligned}
\mathscr A_{M,I}(K)&=C_{0,M}+C_{1,M}\cos(K/2),\\
C_{0,M}&=128\beta^2\int\frac h{\rho^2}
 \sum_\sigma\nu_\sigma^M(t_{\sigma,+}^2+t_{\sigma,-}^2),\\
C_{1,M}&=256\beta^2\int\frac h{\rho^2}
 \sum_\sigma\nu_\sigma^M t_{\sigma,+}t_{\sigma,-}.
\end{aligned}
\tag{C12}
\]

Aquí \(\nu_\sigma^M=(1+\sigma n_3)/2\) para
\(M\in\{\sigma_1,\sigma_2\}\), y \((1-\sigma n_3)/2\) para
\(M\in\{I,\sigma_3\}\). El argumento de diferencia de cuadrados
de C2a da \(C_{0,M}>C_{1,M}>0\). Para \(\sigma_2/I\), son exactamente
\(\mathcal C_0,\mathcal C_1\) del resultado certificado.

## 7. No anulación uniforme, incluso con detector de rango uno

La mera semidefinitud de G no basta: podría dejar una fase z en su
núcleo. Aquí se puede demostrar **definitud positiva** de cada una de
las matrices (C8), usando sólo independencia de funciones racionales.

Supóngase \(\sum_i a_i f_i=0\) en \(L^2\). En el interior de Bob
la función es continua, por lo que se anula punto a punto. Restrinjamos
a la dirección \(n_0=u/\sqrt3\). El segmento radial
\(\sqrt3-b<\rho<\sqrt3+b\) está en ese interior y \(h>0\) allí.
Después de retirar \(\sqrt h/\rho\), queda

\[
\sum_{\sigma,\epsilon}
\frac{a_{\sigma,\epsilon}}{\rho+\sigma+\epsilon b}
v_\sigma=0,\qquad
v_\sigma=D^{1/2}\Pi_\sigma(n_0)\zeta_M.
\tag{C13}
\]

Los dos vectores \(v_\sigma\) son no nulos para **todos** los pares
originales. En efecto, el vector de Bloch de \(J(n_0)\) es
\(m_0=(1,-1,1)/\sqrt3\). Para un espinor up/down de polarización
\(s=\pm1\),

\[
\|\Pi_\sigma(n_0)\zeta_M\|^2
=\tfrac12(1+\sigma s/\sqrt3)>0.
\]

Para \(D=(I+\sigma_j)/2\), al ser \(\Pi_\sigma\) de rango uno,

\[
\|D^{1/2}\Pi_\sigma(n_0)\zeta_M\|^2
=\frac{1+\sigma s/\sqrt3}{2}\,
 \frac{1+\sigma(m_0)_j}{2}>0.
\tag{C14}
\]

Esto también cubre \(M\in\{I,\sigma_3\}\), \(D=(I+\sigma_3)/2\):
aunque D anula el espinor down antes de propagarlo, no anula los dos
vectores \(\Pi_\sigma(n_0)\downarrow\). No se omite este posible
contraejemplo de selección interna.

Los cuatro denominadores de (C13) tienen polos simples distintos.
Multiplicar por su producto da una identidad polinómica vectorial,
válida porque se anula en un intervalo. Evaluarla en cada raíz
\(\rho=-\alpha_i\) obliga a \(a_i v_{\sigma(i)}=0\), y por
(C14) a \(a_i=0\). La evaluación en esos polos es sólo una prueba
de independencia racional; no prolonga físicamente el campo a radios
negativos. Así los cuatro \(f_i\) son linealmente independientes y
\(G^{M,D}>0\).

Sean \(\lambda_{M,D}>0\) y \(\Lambda_{M,D}<\infty\) sus autovalores
extremos. Como \(\|z\|^2=\|\bar z\|^2=4\), (C11) implica

\[
0<512\beta^2\lambda_{M,D}
\le\mathscr A_{M,D}(K)
\le512\beta^2\Lambda_{M,D}<\infty
\quad\text{para todo K real}.
\tag{C15}
\]

No se usa una evaluación numérica, una fase favorable ni densidad de la
sucesión \(\sqrt N\). Las constantes pueden uniformarse en los
dieciséis pares tomando un mínimo y un máximo sobre una familia finita.
El argumento no afirma que un detector arbitrario conserve esta propiedad;
se verificó (C14) para la lista congelada.

Combinando (C7), (C10) y (C15), se obtiene (C2), con
\(\mathcal Q_{M,D,N}=\Theta(N^{-3})\). Entonces

\[
T_N/\mathcal Q_{M,D,N}=O(N^7e^{-JN})\to0,\qquad
|c_{M,D,N}|/\mathcal Q_{M,D,N}=O(N^{-1/2})\to0.
\]

Las condiciones del criterio abstracto se verifican para los dieciséis
pares. Esta no anulación y la adaptación de transferencia de §5 son
pasos nuevos de alcance en C2c, pendientes de revisión independiente.

## 8. Clasificación de los dieciséis pares

Escribamos \(D_0=I\), \(D_j=(I+\sigma_j)/2\) para \(j=1,2,3\).
Sean \(\mathscr A_{+,j}\), \(\mathscr A_{-,j}\) las funciones (C9)
con espinor up y down respectivamente, y detector \(D_j\).
Las fases globales de \(\zeta_M\) se cancelan en la matriz de Gram.
Por tanto los dieciséis pares se agrupan en **a lo sumo ocho familias** de
coeficiente líder: \(\sigma_1\) y \(\sigma_2\) comparten el coeficiente para
cada detector; I y \(\sigma_3\) comparten el otro. Esto no afirma
igualdad de las fuentes completas, de los restos o de las respuestas a N
finito.

En la tabla, **D** significa «demostrado en esta ejecución, pendiente de
revisión independiente»; **E** significa «entrada ya certificada por C2b».
La columna de coherencias individuales incluye el control complejo de §5.2.

| M | Detector | A: bloques | B: compensación | Patrón relativo | Ley cuadrática \(N^{-3}\), coeficiente en \(K=\sqrt N\) | Coherencias individuales |
| --- | --- | --- | --- | --- | --- | --- |
| I | \(D_0\) | D | D | D | D: \(\mathscr A_{-,0}\) | D |
| I | \(D_1\) | D | D | D | D: \(\mathscr A_{-,1}\) | D |
| I | \(D_2\) | D | D | D | D: \(\mathscr A_{-,2}\) | D |
| I | \(D_3\) | D | D | D | D: \(\mathscr A_{-,3}\) | D |
| \(\sigma_1\) | \(D_0\) | D | D | D | D: \(\mathscr A_{+,0}\) | D |
| \(\sigma_1\) | \(D_1\) | D | D | D | D: \(\mathscr A_{+,1}\) | D |
| \(\sigma_1\) | \(D_2\) | D | D | D | D: \(\mathscr A_{+,2}\) | D |
| \(\sigma_1\) | \(D_3\) | D | D | D | D: \(\mathscr A_{+,3}\) | D |
| \(\sigma_2\) | \(D_0\) | E | E | E | E: \(\mathscr A_{+,0}=\mathcal C_0+\mathcal C_1\cos(K/2)\) | E |
| \(\sigma_2\) | \(D_1\) | D | D | D | D: \(\mathscr A_{+,1}\) | D |
| \(\sigma_2\) | \(D_2\) | D | D | D | D: \(\mathscr A_{+,2}\) | D |
| \(\sigma_2\) | \(D_3\) | D | D | D | D: \(\mathscr A_{+,3}\) | D |
| \(\sigma_3\) | \(D_0\) | D | D | D | D: \(\mathscr A_{-,0}\) | D |
| \(\sigma_3\) | \(D_1\) | D | D | D | D: \(\mathscr A_{-,1}\) | D |
| \(\sigma_3\) | \(D_2\) | D | D | D | D: \(\mathscr A_{-,2}\) | D |
| \(\sigma_3\) | \(D_3\) | D | D | D | D: \(\mathscr A_{-,3}\) | D |

El significado cuantitativo de cada fila es

\[
\begin{aligned}
L_{PP}^{M,D}&=+N^{-3}\mathscr A_{M,D}(\sqrt N)+O(N^{-13/4}),\\
L_{QQ}^{M,D}&=+N^{-3}\mathscr A_{M,D}(\sqrt N)+O(N^{-13/4}),\\
L_{PQ}^{M,D}+L_{QP}^{M,D}
 &=-2N^{-3}\mathscr A_{M,D}(\sqrt N)+O(N^{-13/4}),\\
L_{PQ}^{M,D}&=-N^{-3}\mathscr A_{M,D}(\sqrt N)+O(N^{-13/4}),\\
L_{QP}^{M,D}&=-N^{-3}\mathscr A_{M,D}(\sqrt N)+O(N^{-13/4}).
\end{aligned}
\tag{C16}
\]

Las dos últimas son expansiones complejas separadas, no una igualdad
exacta entre PQ y QP. Exactamente son conjugados. Los errores
exponenciales de (C3) se absorben en el resto algebraico porque J es
positivo y fijo. No se infiere la expansión de los bloques desde la
asintótica de su suma total.

La potencia tres se ha obtenido en los dieciséis pares, pero por la
verificación del protocolo de §§5–7. No fue una condición de éxito
impuesta a la clasificación. Un cambio de espinor o detector constante
dentro de estas listas no cambia el borde radial, y (C14) descarta la
anulación completa de su líder. En otra familia podría fallar esa
condición; el criterio abstracto seguiría disponible con otra escala.

## 9. Qué es estructural y qué conserva dependencia del protocolo

### 9.1. Parte estructural

La descomposición inicial complementaria y la reconstrucción del vector
local son identidades de operadores. La norma localizada de la suma
evolucionada se controla por una cota de propagación del vector local.
El criterio (C1) usa esas identidades y comparaciones de escalas, sin
requerir una ley particular ni un proyector de Fourier.

En particular, el patrón relativo se aplica condicionalmente a cualquier
secuencia que cumpla §3.1 y (C1), incluso si su escala cuadrática no es
una potencia de N. Esto no certifica esas hipótesis en ningún otro modelo.
La conmutación con V sólo refuerza la interpretación como sectores
conservados bajo la evolución. La no conmutación del detector con P
explica por qué no se pueden eliminar sus términos cruzados.

### 9.2. Parte específica de los cortes duros considerados

En la red homogénea, el multiplicador duro escalar de la bola tiene
abiertos interiores y exteriores no vacíos. Para una fuente local no
nula de soporte finito, \(Pa\) no puede tener soporte finito: su
transformada sería un polinomio trigonométrico que se anula en el
exterior abierto; luego sería cero en todo el toro. Eso obligaría a
\(\widehat a\) a anularse en el interior abierto y por analiticidad a
\(a=0\), contradicción. Fuera de Alice, \(Qa=-Pa\), de modo que
Qa tiene también cola no local.

La misma prueba vale para un **corte escalar indicador** \(p=1_\Omega\) en
el toro de momentos, siempre que \(\Omega\) y su complemento contengan
abiertos no vacíos, la fuente tenga soporte finito y sea no nula, y la
proyección se defina por el multiplicador escalar \(p\). Si \(Pa\) tuviera
soporte finito, su transformada trigonométrica se anularía en el abierto
del complemento de \(\Omega\), luego sería idénticamente nula; en el abierto
de \(\Omega\) esto forzaría \(\widehat a=0\), contradiciendo la fuente.
Este enunciado no cubre multiplicadores suaves, proyectores internos
matriciales, regiones sin abiertos, fuentes sin soporte finito ni una tasa
cuantitativa para la cola o su funcional en Bob. El criterio de §4 es más
abstracto que este mecanismo concreto de producción de colas.

### 9.3. Parte cuantitativa del protocolo

La ley de (C2) utiliza conjuntamente:

- el cero cuadrático del perfil de Alice, que produce la cola
  \(\widehat A_M(k)\) de orden \(k^{-4}\);
- la reducción radial tridimensional del Weyl de este nodo, que aporta
  \((k\rho)^{-1}\), y la separación geométrica
  \(\gamma=\sqrt3-3/2>0\);
- el corte \(K=\sqrt N\): el campo líder de orden \(K^{-3}\)
  produce una forma cuadrática de orden \(K^{-6}=N^{-3}\);
- la desaparición del término lineal a ese orden por soportes y
  oscilación, y la transferencia discreta completa con sus aliases;
- el peso de Bob, su bola con interior, y los acoplamientos internos
  que permiten demostrar definitud positiva en §7.

Las frecuencias \(\alpha_i-\alpha_j\), las matrices G y sus constantes
dependen de estas elecciones. Con D=I la ortogonalidad entre bandas
reduce el coeficiente a una constante más \(\cos(K/2)\); con D de
rango uno esa simplificación no se presupone. Tampoco se afirma una
potencia alternativa al cambiar perfiles, corte o geometría: esos
cambios no se ejecutan en C2c.

### 9.4. Techo físico

La compensación es entre componentes de una descomposición espectral.
\(\|E^{1/2}(d_P+d_Q)\|\) es pequeña en Bob, no en norma global.
La localidad estricta del walk no implica por sí sola la pequeñez
exponencial en la corona; en este protocolo ésta procede del Teorema 4.1.
Ni P ni Q se presentan como una preparación física local. Las coherencias
no son probabilidades independientes, y su signo no establece transporte
local por un sector. La nota no atribuye un origen exclusivamente UV a
la respuesta ni cambia el experimento por un protocolo condicionado.

## 10. Failure search

| Posible fallo | Resultado de la comprobación |
| --- | --- |
| Universalizar el patrón desde A/B | Refutado sin control lineal por el ejemplo algebraico de §4 |
| Importar C2a como PASS para quince pares adicionales | No se hace: §5 verifica las hipótesis de sus lemas y §§6–7 son prueba nueva pendiente de revisión |
| Utilizar positividad sin \(E\ge0\) | El enunciado abstracto la exige; todos los detectores congelados la cumplen |
| Referencia en Q omitida | Se conserva la condición \(P\phi=\phi\); fuera de ella las fórmulas simplificadas no se afirman |
| Exigir conmutación innecesaria o intercambiar proyecciones | Los bloques abstractos proyectan antes de V; sólo se escribe \(d_P=Pd\) bajo conmutación |
| Aplicar causalidad a Pa o Qa | La cota se aplica exclusivamente a a |
| Inferir parte imaginaria pequeña | Se audita el módulo complejo en §5.2; el criterio individual añade esa condición |
| Descartar cruces \(\Pi_+D\Pi_-\) | Se conservan todos los índices i,j en G; sólo D=I permite eliminarlos por ortogonalidad |
| Usar positividad semidefinida como no anulación uniforme | §7 prueba independencia de cuatro funciones y G definida positiva |
| Detector \(D_3\) anula la fuente down | Puede anular ese espinor antes de la propagación; (C14) prueba que no elimina los canales propagados relevantes |
| Una combinación de fases mata el líder | (C15) controla todas las fases, no sólo \(K=\sqrt N\) o una subsecuencia |
| Vector n fijo no basta para una integral tridimensional | La anulación en \(L^2\) más continuidad implica anulación en todo el interior antes de restringir al segmento radial |
| Extender la física a radios negativos | Los polos de (C13) se usan sólo para una identidad polinómica, no para evaluar el campo físico |
| Error de borde al promediar fases \(2K\rho\) | Las amplitudes son h por funciones suaves; h se anula en la frontera y \(\nabla\rho\) no se anula |
| Perder muestreo o imágenes en un detector distinto | §5.3 retiene D en la forma cuadrática; su norma no aumenta las cotas de Poisson |
| Constantes dependientes de una fase favorable | La geometría es fija, G no depende de N y la familia es finita |
| Forzar una potencia común | Primero se prueba (C1) sin potencia; (C2) es una verificación posterior del protocolo concreto |
| Circularidad con L o evidencia finita | No se usan \(L-L_{PP}\), Teorema 4.4, ley total ni N=24/40 |

Puntos prioritarios de una revisión independiente: la adaptación uniforme
de los lemas complejos de §5.2; la inclusión de todos los cruces en
(C9)–(C11); el factor 64 en (C11); el argumento de definitud positiva,
especialmente con detectores de rango uno; y la separación entre la
escala del criterio abstracto y la escala del protocolo.

## 11. Resultado, límites y consecuencia de estado

**Demostrado en esta ejecución, pendiente de revisión independiente:**

1. La extensión exacta de A/B a los dieciséis pares originales, con las
   constantes explícitas de C2b y los mismos cuantificadores.
2. El criterio abstracto (C1) y su versión individual con control complejo.
3. La transferencia lineal y cuadrática para los dieciséis pares, las
   fórmulas completas de coeficientes (C8)–(C12), su cota inferior
   uniforme (C15) y las expansiones (C16).
4. La agrupación de coeficientes líderes en a lo sumo ocho familias según el
   espinor up/down y los cuatro detectores, sin igualar respuestas a N
   finito.

**Refutado como inferencia general:** A/B por sí solos obligan al patrón
relativo. La pequeñez del lineal es una hipótesis adicional que aquí se
verifica gracias a la geometría y al análisis de C2a.

**Permanece abierto o fuera de alcance:** una revisión independiente de
esta ejecución; constantes numéricas y umbral efectivo de sus restos;
extensiones a otras clases de fuentes, detectores, filtros, geometrías,
dimensiones o QCA; atribución física exclusivamente IR/UV, novedad y
cualquier aplicación inhomogénea/AdS. No quedan filas sin derivación
dentro de los dieciséis pares, pero sólo \(\sigma_2/I\) tiene el PASS
previo: la tabla nueva no es una promoción canónica.

El estado de C2c que registra **esta nota reparada** es
`REPAIRED / REVIEW_PENDING`. No emite `C2C_PASS`. La reparación añade las
cotas explícitas (C6a) para la transferencia con D, corrige la clasificación
a «a lo sumo ocho familias» y restringe §9.2 a cortes escalares indicadores
con dos abiertos. La reparación sigue necesitando revisión independiente; la
autoría de esta derivación no constituye esa revisión.
`state/CURRENT_STATE.md` y el contrato se conservan exactamente como
entradas congeladas en el commit obligatorio; su `NOT_EXECUTED` describe
ese punto anterior a esta ejecución. Una actualización posterior del
registro deberá distinguir esta prueba escrita de su eventual aceptación.

C1, C2a y C2b mantienen sus PASS y alcances previos. C3 sigue SEPARATE y
E/AdS FROZEN. No se modifica el manuscrito ni se ejecuta código científico.
Esta reparación es un objeto nuevo que debe recibir su propia revisión; no
hay promoción ni push.

## 12. Addendum bibliográfico — 2026-09-22

K. Liu y D. Chen, *Maximal-velocity deficit under a finite-support constraint
in a hard-wall half-line continuous-time quantum walk*, **Phys. Rev. A 114,
032434 (2026)**, [DOI: 10.1103/dyyr-z1k8](https://doi.org/10.1103/dyyr-z1k8),
[arXiv:2609.01970v2](https://arxiv.org/abs/2609.01970v2), §§V.B–VI.B,
(40)–(47), (66)–(67).

El proyector sinc y la condición de traza nula para segundo momento finito
proporcionan un antecedente externo del mecanismo de colas inducidas por
cortes duros discutido en §9.2. Su variable de Fourier es conjugada de una
envolvente de momento reescalada; no se identifica con nuestro corte IR.
No demuestra la compensación localizada, las escalas de C2c ni el patrón
+1:+1:−2. Esta referencia se mantiene fuera del alcance de la revisión y no
cambia `REPAIRED / REVIEW_PENDING`.
La [nota FRONT-RESOURCE SCALING](2026-09-22--front-resource-scaling.md)
registra la lectura, la provenance del PDF y las propuestas FR1–FR3.
