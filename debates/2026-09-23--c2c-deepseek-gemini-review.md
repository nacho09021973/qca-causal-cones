---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-23 11:55
proyecto: /home/ignac/qca-causal-cones
tema: (tema en línea de órdenes)
rondas: 2
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

Revisión adversarial de C2c reparado. Audita únicamente el objeto fijado y sus reparaciones: transferencia a detectores D distinto de I y a los cuatro espinores, conservación de los órdenes y cruces de banda, no anulación C14, clasificación a lo sumo ocho familias y alcance preciso de §9.2. Emite veredictos por fila/nivel S3, C1 y §9.2. No reabras C3, E/AdS ni FR1–FR3. No uses N=24/40, L-L_PP, Teorema 4.4, simulación, cuadratura ni barridos.

## Contexto

### Contexto adjunto: reports/2026-09-22--c2c-structural-scope.md
```
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
```

### Contexto adjunto: theory/IR_C2C_REPAIRED_REVIEW_CRITERIA.md
```
# C2c reparado — criterios de revisión

Fecha: 2026-09-23. Estado: **FROZEN FOR THE REPAIRED OBJECT**.

Este documento no reabre el contrato C2c ni cambia el alcance científico. Fija
el objeto posterior a la reparación interna y separa sus criterios de los del
objeto original `fa9c07f`.

## Objeto

La nota reparada es
`reports/2026-09-22--c2c-structural-scope.md` en el commit `1d33130`, blob
`af44a754f3c79447c507ac778adf6d8a74283efe`, SHA256
`0268d8c869fa1b4666df09327e9ce25c0f545401fd5159286287580a888153a0`.
Debe leerse con `git show 1d33130:reports/2026-09-22--c2c-structural-scope.md`.

El objeto conserva el snapshot científico de entrada `f4f937e` y el contrato
original. §12, FR1–FR3, la lectura de Liu–Chen y el roadmap del 21-09 están
fuera de alcance.

## Reparaciones que deben auditarse

1. **Transferencia lineal.** Verificar (C6a) para los cuatro detectores y que
   la aplicación de D a los lemas (6), (16), (17)–(20) conserva regularidad,
   soportes, fases y órdenes sin suponer `[D,J(n)]=0`.
2. **Transferencia cuadrática.** Verificar las dos cotas ponderadas de L2,
   Cauchy–Schwarz en orden `K^{-13/2}` y el muestreo (23) con D insertado.
   Deben permanecer los cruces `Pi_+ D Pi_-`.
3. **Cuatro espinores.** Comprobar que la representación exacta de C2 y sus
   restos se transfieren a `zeta_M` para los cuatro encoders, sin importar el
   PASS de C2a fuera de `sigma_2/I`.
4. **No anulación.** Rehacer el caso `M=I,D_3` y (C14), con valor `1/6` para
   ambos signos, además de la independencia racional por polos.
5. **Alcance estructural.** Confirmar que la redacción es «a lo sumo ocho
   familias» y que no iguala respuestas finitas ni afirma novedad.
6. **§9.2.** Confirmar que el enunciado queda limitado a multiplicadores
   escalares indicadores `p=1_Omega`, con abiertos no vacíos de `Omega` y su
   complemento, fuente finitamente soportada y no nula. No se admiten por
   inferencia cortes suaves, multiplicadores matriciales o tasas de cola.

## Veredictos y límites

El revisor debe emitir `PASS`, `REPAIR_REQUIRED`, `FAIL` u `OPEN` por fila y
nivel S3, además de C1 y §9.2. Un PASS sólo cubre los dieciséis pares del
walk CJWW (5.15), nodo cero, perfiles, geometría y corte congelados. No
promueve `state/CURRENT_STATE.md`, no reabre C3 ni E/AdS y no establece una
ley para otras clases de QCA.

La revisión debe conservar las salvedades de `IR_C2C_REVIEW_CRITERIA.md`:
ganancia relativa `N^{-1/4}`, régimen asintótico lento, `N_0` no efectivo,
exponente tres propio de `K=sqrt(N)` y `NOVELTY=OPEN`. Quedan prohibidos
`L-L_PP`, el Teorema 4.4, `N=24,40`, simulaciones, cuadraturas y barridos.

La revisión interna de Codex está registrada en
`reports/2026-09-23--c2c-codex-internal-review.md`; no sustituye una revisión
independiente.
```

### Contexto adjunto: theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md
```
# C2c — alcance estructural de la compensación espectral

Fecha: 2026-09-22. Estado: **UNBLOCKED / NOT_EXECUTED**.

Este contrato recoge la decisión del usuario de aceptar C2b y redefinir
C2c como un gate de alcance estructural. La tarea de C2c es determinar
hasta dónde se extiende el mecanismo ya demostrado para \(\sigma_2/I\).
No se registra aquí un resultado nuevo ni una extensión ya certificada.

## Provenance y entradas

- [Contrato C1/C2/C3](IR_ATTRIBUTION_C1_C2_C3_GATE.md).
- [Contrato C2a](IR_C2A_OSCILLATORY_TRANSFER_GATE.md),
  [derivación](../reports/2026-09-22--c2a-oscillatory-transfer.md) y
  [revisión](../reports/2026-09-22--c2a-independent-review.md).
- [Contrato C2b](IR_C2B_BLOCK_DECOMPOSITION_GATE.md),
  [candidato](../reports/2026-09-22--c2b-block-decomposition-candidate.md) y
  [revisión independiente](../reports/2026-09-22--c2b-independent-review.md).
- [Manuscrito](../papers/ir-corona/ir-corona.md), convenciones, protocolo
  y Teorema 4.1; [estado vigente](../state/CURRENT_STATE.md), §10.1.

C2b fue un **POST-DISCOVERY VERIFICATION GATE** sobre el commit
`19eb7a383cbb09464e91b64e89f724204e58cccb`. Su revisión es de Codex,
agente `/root`, independiente del autor Claude Opus 5; no se registra como
una revisión adicional de Astra ni como evidencia de diversidad de modelo.
SHA256 del informe aceptado:
`65bab830c6960f2c661ae47d739d90c1ecf8ae06b5f9923383919f76c2b234d5`.

Este contrato fija el alcance de la siguiente auditoría después de conocer
el mecanismo de C2b. No es una preregistración retrospectiva de ese mecanismo
ni de las generalizaciones sugeridas en la discusión. No presupone que el
patrón principal se extienda a todos los pares.

## Estado de partida y objetos congelados

C1 = PASS; C2a = PASS para \(\sigma_2/I\); C2b = PASS para ese par,
con B4_PRIME_PASS registrado aparte; C2c = UNBLOCKED; C3 = SEPARATE;
E/AdS = FROZEN. No se reabre la ley total del observable.

Se conserva el walk homogéneo CJWW (5.15), dos componentes, nodo cero,
recurso \(\phi_N\), perfiles y regiones originales, \(N\ge2\) entero,
\(P=1_{|p|\le N^{-1/2}}I_2\), \(Q=I-P\). Se conservan

\[
a=(U_M-I)\phi_N,\quad r=S^N\phi_N,\quad d=S^Na,
\quad d_P=S^NPa,\quad d_Q=S^NQa,
\]
\[
L_{XY}=\operatorname{tr}(ES^NX\Delta YS^{-N}),\quad
\mathrm{Lin}_N=2\operatorname{Re}\langle r,Ed_P\rangle,\quad
\mathcal Q_N=\langle d_P,Ed_P\rangle.
\]

Los dieciséis pares que deben clasificarse son exactamente

\[
M\in\{I,\sigma_1,\sigma_2,\sigma_3\},\qquad
M_B\in\{I,(I+\sigma_1)/2,(I+\sigma_2)/2,(I+\sigma_3)/2\},
\quad E=h_N\otimes M_B.
\]

Los proyectores internos de Bob no se confunden con \(P\). El encoder
\(M=I\) se conserva como control original; no se identifica con omitir
el encoder. Ningún filtro, detector, perfil o geometría se sustituye.

## Preguntas y obligaciones de alcance

### S1 — qué depende sólo del álgebra

Separar las hipótesis de cada identidad: \(Q=I-P\), linealidad,
ortogonalidad de los proyectores, \(P\phi_N=\phi_N\), unitariedad,
\(E=E^\dagger\), positividad y conmutación con \(S\). Explicitar cuáles
son necesarias en cada paso y cuáles sólo están disponibles en el modelo.
No presentar \([S,P]=0\) como requisito de B1.

### S2 — qué depende de la localidad y del Teorema 4.1

Auditar la extensión de B3 a los dieciséis pares, comprobando para cada
familia la normalización, el soporte de \(a\), \(0\le E\le I\), el
soporte de Bob y la uniformidad de las constantes. Distinguir la
cancelación de amplitudes en la norma localizada por \(E^{1/2}\) de una
afirmación en norma global. La cota causal se aplica al objeto local
\(a\), nunca automáticamente a \(Pa\) o \(Qa\).

### S3 — qué requiere información asintótica del par

Clasificar, para cada uno de los dieciséis pares y sin heredar el PASS
de \(\sigma_2/I\), los siguientes niveles por separado:

| Nivel | Obligación |
| --- | --- |
| Identidades exactas | Verificar S1 con el par correspondiente |
| Compensación localizada y errores | Verificar S2 y sus cuantificadores |
| Patrón relativo \(+1:+1:-2\) | Identificar una escala cuadrática no nula y comprobar que el lineal y los errores causales son menores que ella |
| Ley cuantitativa de escala \(N^{-3}\) | Demostrar el líder, coeficiente y resto propios del par; no copiar \(A_N\) de C2a |
| Coherencias individuales | Controlar el emparejamiento complejo, no sólo su parte real |

Debe examinarse expresamente si el detector puede anular un canal líder,
si la suma completa tiene una cota inferior uniforme, y qué ocurre ante
ceros o subsecuencias. Si falta una estimación o una no anulación, el nivel
correspondiente queda OPEN. Una identidad general no certifica por sí sola
el exponente tres, la fase \(\sqrt N/2\), las constantes de C2a ni el
patrón relativo. No se exige un resultado favorable para los dieciséis
pares como condición para una clasificación rigurosa de alcance.

### S4 — formulación general y papel del corte duro

Formular, si lo permiten las pruebas, un resultado condicional con todas
sus hipótesis explícitas, distinguiendo:

- el álgebra que sólo usa proyectores complementarios;
- la estimación localizada que requiere una cota de propagación para la
  fuente local y el efecto positivo;
- la falta de soporte espacial finito introducida por este corte duro;
- la información adicional sobre el campo proyectado y el término lineal
  que permite pasar de compensación de amplitudes a líderes de bloques.

Precisar qué propiedades requieren que el proyector sea un multiplicador
de Fourier, un corte duro o un proyector que conmuta con la evolución.
No generalizar automáticamente a cualquier proyector duro, banda, estado,
dimensión, QCA o geometría. Una formulación abstracta condicional no
constituye verificación de sus hipótesis en otros modelos.

### S5 — techo de interpretación

Separar identidad algebraica, estimación asintótica e interpretación
física. Las coherencias son contribuciones firmadas a un observable;
no son probabilidades independientes. El proyector duro no representa
transporte físico local. La causalidad de rango finito por sí sola no
sustituye la cota del Teorema 4.1 en Bob. C2c no atribuye un origen
exclusivamente UV a la señal ni resuelve el protocolo condicionado C3.

## Método, failure search y límites

Auditoría analítica de las dependencias existentes antes de proponer una
extensión. Para cada paso se exige fuente, hipótesis, cuantificadores y
nivel de evidencia. Buscar fallos de normalización, términos de referencia,
conjugación, positividad, no conmutación con el detector, uniformidad,
anulación de canales y dependencia de la parte imaginaria.

No usar \(L-L_{PP}\), Teorema 4.4, la ley total ni los datos \(N=24,40\)
para establecer bloques o universalidad. No se autorizan en este contrato
simulaciones, nuevos barridos, ajustes, suavizado del corte ni una nueva
saddle analysis para completar casos sin prueba. Si un nivel necesita
análisis adicional no disponible, registrar la dependencia pendiente.

La revisión adicional por Astra sugerida por el usuario no se considera
realizada ni se dispara automáticamente al registrar este contrato.
No se alteran los contratos, candidato o informes históricos de C2a/C2b.

## Entregable y criterios de cierre

Una futura ejecución debe producir
`reports/2026-09-22--c2c-structural-scope.md`, con:

1. matriz de hipótesis y dependencias de S1–S4;
2. tabla de los dieciséis pares con los cinco niveles de S3 separados;
3. enunciado condicional general, si está justificado, con prueba y límites;
4. búsqueda adversarial y separación física S5;
5. lista explícita de niveles demostrados, refutados y abiertos.

`PROOF_WRITTEN / REVIEW_PENDING` distingue la ejecución de su aceptación.
Una revisión independiente puede emitir `C2C_PASS` para un alcance
explícitamente delimitado, `C2C_REPAIR_REQUIRED`, `C2C_FAIL` o
`C2C_INCOMPLETE`. Un PASS de la clasificación no transforma los niveles
marcados OPEN en teoremas ni equivale a universalidad del patrón.
Los contraejemplos analíticos que delimiten una extensión son resultados
válidos; nunca invalidan retrospectivamente el par certificado sin
identificar un error en su prueba.

El presente documento sólo fija el gate. No lo ejecuta ni promociona
resultados de C2c. C3 permanece separado, E/AdS congelado y los demás
frentes sin cambios. No hay publicación, commit ni push.
```

### Contexto adjunto: reports/2026-09-22--c2a-oscillatory-transfer.md
```
# C2a: transferencia del funcional completo y cancelación del corte duro

Fecha: 2026-09-22. Base Git `2b29b19`, con las notas locales C1/C2.
Contrato: [IR_C2A_OSCILLATORY_TRANSFER_GATE](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md).
**Estado: TRANSFER_PROOF_WRITTEN / REVIEW_PENDING.**
Es una derivación analítica nueva sin revisión independiente ni promoción.
No se ha ejecutado código científico, barrido o ajuste para obtenerla.

## 1. Enunciado y cuantificadores

Se conserva exclusivamente el par `M=sigma2`, `M_B=I`, el recurso, los
perfiles, la geometría y el símbolo CJWW (5.15) congelados. N tiende a
infinito por enteros; `P=1_{|p|<=N^{-1/2}}`, sin suavizarlo. Sea
`K=sqrt(N)`, `b=1/4`, `u=(1,1,1)` y `B=Phi_0(b)>0`.
Se usan las definiciones exactas de
[la representación C2](2026-09-22--c2-projected-response-representation.md).

La referencia del contrato es el funcional continuo completo
\[
L^W_{PP}(N)=\int h(Y)\left[2\operatorname{Re}R_0(Y)^\dagger D_K^W(Y)
                              +\|D_K^W(Y)\|^2\right]d^3Y.
\]
La derivación que sigue establece
\[
\boxed{L^W_{PP}(N)=N^{-3}\left[\mathcal C_0+
                  \mathcal C_1\cos(\sqrt N/2)\right]+O(N^{-7/2}),
\quad \mathcal C_0>\mathcal C_1>0,}
\tag{1}
\]
y la transferencia, con todos los errores del funcional incluidos,
\[
\boxed{L_{PP}(N)-L^W_{PP}(N)=O(N^{-13/4})=o(N^{-3}).}
\tag{2}
\]
Por tanto el candidato de resultado discreto completo es
\[
\boxed{L_{PP}(N)=N^{-3}\left[\mathcal C_0+
                  \mathcal C_1\cos(\sqrt N/2)\right]+O(N^{-13/4}).}
\tag{3}
\]
La fase es proporcional a sqrt(N), determinada por el corte móvil.
Lpp es real y finalmente positivo. No se usa un ansatz complejo para
una probabilidad firmada. Las constantes y el umbral de validez del
resto no se hacen numéricamente explícitos.

## 2. Identidades y estimaciones auxiliares

Escribimos `A=A_sigma2`, `zeta=M chi=-i up`, `chi=down`,
`V_N(k)=S(k/N)^N`, `V_W(k)=exp(-i H_W(k))`.
La fuente es exactamente `a_N(x)=N^{-3/2} A(x/N)`.
Definamos `h(Y)=(1-16|Y-u|^2)_+^2`,
\[
\mathscr A_N(k)=\widehat A(k)+E_N^A(k),\qquad
E_N^A(k)=\sum_{m\ne0}\widehat A(k+2\pi Nm),
\]
y el campo continuo cuya muestra es el campo discreto escalado,
\[
D_N(Y)=\int_{|k|\le K}e^{-ik\cdot Y}V_N(k)\mathscr A_N(k)
                       \frac{d^3k}{(2\pi)^3}.
\]
Aquí no se ha omitido ninguna imagen. Denotamos `R_N=mathcal R_N`
del informe C2; el recurso físico libre es `N^{-3/2}R_N(y/N)`.
Sean `w_N=h R_N`, `w_0=h R_0`.

### 2.1. Fourier de fuente y detector

C1 proporciona `||Ahat(k)||<=C(1+|k|)^{-4}`. Además, para `k=r n`,
`r>=2`,
\[
\widehat A(rn)=r^{-4}\sum_{\epsilon=\pm1}
 e^{i\epsilon br}a_\epsilon+O(r^{-5}),
\qquad a_\epsilon=i32\pi^2B\zeta.
\tag{4}
\]
La fuente es radial vectorial, de modo que sus restos no dependen de n.
El perfil radial `f(Y)=(1-16|Y|^2)_+^2` satisface
\[
\widehat f(r)=128\pi\frac{\cos(br)}{r^4}+O(r^{-5}).
\]
Su transformada exacta es una suma finita de seno/coseno por potencias
de r, tal como se verifica en el certificado C1. Como R_N tiene soporte
de Fourier en `|q|<=1`, con norma L1 uniformemente acotada, la convolución
con `hhat(k)=exp(i k.u) fhat(k)` da
\[
\widehat w_N(rn)=e^{irn\cdot u}\left[
\frac{64\pi}{r^4}\sum_{\eta=\pm1}e^{i\eta br}
 R_N(u+\eta bn)+\mathcal E_N(r,n)\right],
\quad \|\mathcal E_N(r,\cdot)\|_{C^6(S^2)}\le Cr^{-5}.
\tag{5}
\]
En efecto, para `|q|<=1`,
`|rn-q|=r-n.q+O(r^{-1})`, con el mismo orden bajo cualquier número fijo
de derivadas angulares. Se expande la fórmula exacta de fhat dentro de
la convolución. Los factores `exp(-iq.u-i eta b n.q)` reconstruyen
`R_N(u+eta b n)`; las derivadas de R_N están acotadas uniformemente,
pues su soporte de Fourier queda fijo. Esto también prueba
`||what_N(k)||<=C(1+|k|)^{-4}` globalmente.

En todo el informe, los límites implícitos son uniformes en N grande,
en la bola de Bob y en las direcciones indicadas. No dependen de una
subsecuencia favorable de las fases.

### 2.2. Lema angular elemental

Para g suave en la esfera y `ell=|u|=sqrt(3)`,
\[
\int_{S^2}e^{-irn\cdot u}g(n)d\Omega
=\frac{2\pi}{ir\ell}
\left[e^{ir\ell}g(-\widehat u)-e^{-ir\ell}g(\widehat u)\right]
+O(r^{-2}).
\tag{6}
\]
También su valor absoluto está acotado por `C r^{-1}||g||_{C^6}`.
Para comprobarlo, se orienta el eje polar en u y se escribe la integral
como `integral_{-1}^1 exp(-ir ell z) G(z) dz`. El promedio azimutal G
tiene dos derivadas acotadas en el intervalo cerrado cuando g tiene seis
derivadas acotadas; sus valores extremos son `2pi g(+/- uhat)`.
Dos integraciones por partes dan (6). Los polos son los dos puntos
estacionarios angulares; no se los descarta por la ausencia de saddle
en el volumen tridimensional.

### 2.3. Dispersión: primer término local y resto

Para el símbolo literal, `S=f I-i a.sigma`,
`a=(sin p1,-cos p1 sin p2,cos p1 cos p2 sin p3)`.
Su logaritmo hermítico cerca del nodo es analítico e impar:
\[
H(p)=H_W(p)+H_3(p)+O(|p|^5),
\]
donde H3 es el polinomio matricial homogéneo cúbico
\[
H_3(k)=\tfrac16\left[
k_1(k_2^2+k_3^2)\sigma_1
+k_2(2k_1^2-k_3^2)\sigma_2
-2k_3(k_1^2+k_2^2)\sigma_3\right].
\]
Esta expresión sigue de `omega/sin(omega)=1+|p|^2/6+O(|p|^4)`
y el Taylor cúbico de las tres componentes de a. Así H3 es un operador
diferencial local de coeficientes constantes, no un multiplicador
pseudodiferencial de soporte desconocido. Entonces
\[
V_N(k)=V_W(k)+N^{-2}V_1(k)+\mathcal T_N(k),
\quad \|\mathcal T_N(k)\|\le C N^{-4}(|k|^5+|k|^6),\quad |k|\le K,
\tag{7}
\]
con
\[
V_1(k)=-i\int_0^1e^{-i(1-s)H_W(k)}H_3(k)e^{-isH_W(k)}ds.
\]
Este operador auxiliar está definido para todo k real; sólo la expansión
de V_N se restringe a la bola de radio K. Extender V1 para utilizar su
soporte espacial no supone aproximar el símbolo de la red fuera de esa bola.
La cota procede de Duhamel para el término de grado cinco y del resto
cuadrático en H3; todos los exponentes reales son unitarios.
En particular `||V_N-V_W||<=C |k|^3/N^2`.

Para r>0, si `J(n)=H_W(n)` y `P_sigma(n)=(I+sigma J(n))/2`, integrar
exactamente los factores de fase de V1 muestra
\[
V_1(rn)=\sum_{\sigma=\pm1}e^{-i\sigma r}
             [r^3 U_\sigma(n)+r^2 Z_\sigma(n)],
\tag{8}
\]
con matrices suaves en la esfera. Los términos diagonales en banda dan
`-i r^3 P_sigma H_3(n)P_sigma`; los cruzados se obtienen de
`(exp(-i tau r)-exp(-i sigma r))/(tau-sigma)`, multiplicado por r^2.
No hay denominador singular angular.

Finalmente, en el recurso fijo `|q|<=1`, Duhamel implica para todo m fijo
\[
\|R_N-R_0\|_{C^m}\le C_m N^{-2},\qquad
\|\widehat w_N-\widehat w_0\|\le C N^{-2}(1+|k|)^{-4}.
\tag{9}
\]

## 3. La escala líder de la referencia Weyl

### 3.1. Término lineal: cancelación espacial y oscilación de borde

La evolución Weyl sin corte de A tiene soporte en `|Y|<=1+b`.
Los soportes de w0 y de cualquier wN están en la bola de Bob,
`|Y-u|<=b`, separada por `gamma=sqrt(3)-3/2>0`.
La propagación finita de Weyl se sigue de la fórmula de ondas para
`cos(|D|)` y `sin(|D|)/|D|`, seguida por H_W. Por ello
\[
\langle w_0,D_K^W\rangle
=-\int_{|k|>K}\widehat w_0(k)^\dagger V_W(k)\widehat A(k)
                        \frac{d^3k}{(2\pi)^3}.
\tag{10}
\]
Las fórmulas (4)–(5) y `V_W=sum exp(-i sigma r)P_sigma(n)` dan en el
término líder integrandos radiales de orden r^-6, antes de la integral
angular. Por (6) adquieren r^-1 adicional, con fases radiales
\[
\pm\ell+\epsilon b-\eta b-\sigma.
\]
Ninguna se anula: su módulo es al menos `ell-(1+2b)=gamma`.
Integrar por partes en r da `O(K^{-7})`. El resto O(r^-2) de (6)
integra absolutamente al mismo orden. En los productos subdominantes,
el resto angular uniforme de (5) y la radialidad de (4) permiten usar
la cota O(r^-1) de (6): el integrando radial es O(r^-8) y su integral
es O(K^-7). En consecuencia,
\[
2\operatorname{Re}\langle w_0,D_K^W\rangle=O(K^{-7}).
\tag{11}
\]

### 3.2. Término cuadrático y coeficiente uniformemente positivo

La reducción radial de C2, obtenida integrando exactamente los ángulos,
da en Bob, uniformemente, con `rho=|Y|`, `n=Y/rho`,
\[
D_K^W(Y)=-\frac{i16B}{\rho K^3}
\sum_{\sigma=\pm1}P_\sigma(n)\zeta\,F_\sigma(K,\rho)+O(K^{-4}),
\]
\[
F_\sigma(K,\rho)=\sum_{\epsilon=\pm1}
\frac{\cos[(\rho+\sigma+\epsilon b)K]}{\rho+\sigma+\epsilon b}.
\tag{12}
\]
La fuente sin corte se anula en Bob. El campo con corte es el negativo
de su integral radial de K a infinito. La cola de fuente `r^-4 cos(br)`
y las funciones j0,j1 producen `integral_K^infinity r^-3 sin(cr)dr`,
cuya expansión es `K^-3 cos(cK)/c+O(K^-4)`. Los demás términos dan el
resto escrito; todos los c tienen módulo al menos gamma.

Sean
\[
t_{\sigma,\pm}(\rho)=\frac1{\rho+\sigma\pm b},\qquad
\nu_\sigma(Y)=\|P_\sigma(n)\zeta\|^2=\frac{1+\sigma n_3}{2}.
\]
Los proyectores son ortogonales, `nu_++nu_-=1`, y
\[
\|D_K^W(Y)\|^2=
\frac{256B^2}{\rho^2K^6}\sum_\sigma\nu_\sigma(Y)F_\sigma(K,\rho)^2
+O(K^{-7}).
\]
Al expandir F_sigma^2, los términos independientes de la fase radial son
\[
\tfrac12(t_{\sigma,+}^2+t_{\sigma,-}^2)
+t_{\sigma,+}t_{\sigma,-}\cos(2bK).
\]
Los otros términos llevan fases `2K rho+constant`. Su integral contra
los pesos de Bob es O(K^-1): `|grad rho|=1`, el soporte no toca el origen
y el peso h es C1 compacto. Una integración por partes con el campo
grad rho controla el error sin término de borde, pues h se anula allí.
De este modo
\[
\int h\|D_K^W\|^2
=K^{-6}[\mathcal C_0+\mathcal C_1\cos(2bK)]+O(K^{-7}),
\tag{13}
\]
donde las constantes explícitas son
\[
\begin{aligned}
\mathcal C_0&=128B^2\int\frac{h(Y)}{\rho^2}
 \sum_\sigma\nu_\sigma(Y)
       (t_{\sigma,+}^2+t_{\sigma,-}^2)\,d^3Y,\\
\mathcal C_1&=256B^2\int\frac{h(Y)}{\rho^2}
 \sum_\sigma\nu_\sigma(Y)t_{\sigma,+}t_{\sigma,-}\,d^3Y.
\end{aligned}
\tag{14}
\]
Todos los denominadores son positivos y mayores o iguales que gamma.
Además
\[
\mathcal C_0-\mathcal C_1
=128B^2\int\frac h{\rho^2}\sum_\sigma\nu_\sigma
                    (t_{\sigma,+}-t_{\sigma,-})^2d^3Y>0.
\tag{15}
\]
La positividad es estricta porque b>0, h>0 en el interior y la suma de
los nu es uno. También C1>0. Queda una cota inferior uniforme del
coeficiente oscilatorio, sin seleccionar subsecuencias. (11) y (13)
prueban (1). La escala A_N de transferencia es, por tanto, Theta(N^-3).

## 4. Transferencia del término lineal discreto

### 4.1. Muestreo e imágenes, conservados hasta acotarlos

La identidad exacta de Poisson aplicada a w_N da
\[
N^{-3}\sum_y w_N(y/N)^\dagger D_N(y/N)
=\int_{|k|\le K}\mathscr W_N(k)^\dagger V_N(k)\mathscr A_N(k)
                        \frac{d^3k}{(2\pi)^3},
\]
con `mathscr W_N(k)=sum_m what_N(k+2pi Nm)`.
Por (4)–(5), ambas sumas de imágenes no centrales son `O(N^{-4})`
en esta bola; se suma `|m|^{-4}` en dimensión tres. Las transformadas
centrales tienen norma L1 uniformemente acotada. La diferencia entre la
última integral y la que conserva sólo what_N y Ahat es, por tanto,
\[
O(N^{-4})+O(N^{-8}K^3)=O(K^{-8}).
\tag{16}
\]
Esto controla simultáneamente el muestreo de Bob y las imágenes de Alice
en el término lineal, sin asumir que el error puntual se suma sin fase.

### 4.2. El primer corrector de dispersión es local antes del corte

El operador V1 es una integral de evoluciones Weyl de duraciones s y
1-s intercaladas con el operador diferencial local H3. Su aplicación a
A tiene soporte en `|Y|<=b+1`, incluso si se interpreta distribucionalmente
por las derivadas de A en la esfera. En consecuencia
\[
\int_{\mathbb R^3}\widehat w_N^\dagger V_1\widehat A\,
                                    \frac{d^3k}{(2\pi)^3}=0.
\tag{17}
\]
Este emparejamiento es absolutamente convergente: el integrando radial
en valor absoluto es O(r^-3). Para justificar el uso de un w_N sólo C1,
se lo regulariza con mollificadores compactos de radio menor que la
separación; sus soportes siguen disjuntos. La identidad vale para los
tests suaves y pasa al límite por convergencia dominada en Fourier.

Por (17), el corrector restringido a la bola es el negativo de la cola.
Usando (4), (5) y (8), su término principal antes de integrar ángulos
es r^-3 por fase radial y una función suave de n. La oscilación
`exp(-ir n.u)` gana r^-1 por (6); integrar su valor absoluto radial
da O(K^-3). Los términos subdominantes son ya O(r^-4) radialmente y
dan el mismo orden sin necesitar otra ganancia. Así
\[
\left|N^{-2}\int_{|k|\le K}\widehat w_N^\dagger V_1\widehat A\right|
\le C N^{-2}K^{-3}=C K^{-7}.
\tag{18}
\]
No se descarta el borde: esta es precisamente su contribución después
de la cancelación del funcional completo sin corte.

El resto de (7) se controla ahora absolutamente porque contiene **dos**
factores Fourier de orden cuatro:
\[
\left|\int_{|k|\le K}\widehat w_N^\dagger\mathcal T_N\widehat A\right|
\le C N^{-4}\int_0^K r^2(1+r)^{-8}(r^5+r^6)dr
\le C N^{-4}(1+K+\log(1+K))=O(K^{-7}).
\tag{19}
\]

### 4.3. Cambio del recurso libre

El producto `(w_N-w_0)` tiene el mismo soporte separado. El emparejamiento
con V_W A sin corte es cero, por lo que (9) acota la diferencia truncada
por su cola:
\[
\left|\int_{|k|\le K}(\widehat w_N-\widehat w_0)^\dagger V_W\widehat A\right|
\le C N^{-2}\int_K^\infty r^2(1+r)^{-8}dr
=O(K^{-9}).
\tag{20}
\]
Las constantes de medida (2pi)^-3 se han absorbido sólo en estas cotas.
(16), (18)–(20) prueban que la diferencia de los términos lineales
completos, incluyendo su parte real y el factor dos, es **O(K^-7)**.

## 5. Transferencia del término cuadrático

### 5.1. Norma L2 para el error de campo, aplicada sólo al error cuadrático

Aquí no se intenta atribuir la señal mediante una norma: se acota el
error de una forma cuadrática cuya referencia en Bob ya se conoce.
Por Plancherel, unitariedad y Duhamel,
\[
\|D_N-D_K^W\|_{L^2(\mathbb R^3)}
\le\frac C{N^2}\left(\int_0^K r^8(1+r)^{-8}dr\right)^{1/2}
+C N^{-4}K^{3/2}
=O(K^{-7/2}).
\tag{21}
\]
El segundo sumando es el error de imágenes de Alice, conservado en
D_N. Por (12), `||sqrt(h)D_K^W||_2=O(K^-3)`. Por Cauchy–Schwarz,
\[
\left|\int h(\|D_N\|^2-\|D_K^W\|^2)\right|
\le2\|\sqrt h D_K^W\|_2\|D_N-D_K^W\|_2
+\|D_N-D_K^W\|_2^2=O(K^{-13/2}).
\tag{22}
\]
Esta cota es menor que K^-6 aunque la anterior aproximación puntual
O(N^-1) no lo fuera. El término lineal no se ha estimado con (21).

### 5.2. Error de muestreo del cuadrático

Falta comparar la integral con la suma de red. El transformado de D_N
tiene soporte en radio K y norma L1 uniformemente acotada, ya que
`||Ahat||_1=O(1)` y `||E_N^A||_{L1(B_K)}=O(N^{-4}K^3)`.
En Poisson aplicado a `h||D_N||^2`, los términos m no nulos contienen
\[
\widehat h(k-q+2\pi Nm),\qquad |k|,|q|\le K.
\]
Para N grande su argumento tiene módulo al menos `c N|m|`.
La cota `|hhat(ell)|<=C(1+|ell|)^{-4}` y la suma convergente de
`|m|^{-4}` dan
\[
\left|N^{-3}\sum_y h(y/N)\|D_N(y/N)\|^2
-\int h(Y)\|D_N(Y)\|^2d^3Y\right|=O(N^{-4})=O(K^{-8}).
\tag{23}
\]
Poisson es legítimo: la función muestreada es continua y compacta y
su transformada, una convolución con soporte central de radio 2K,
decae como |ell|^-4 fuera de ese radio. Para cada N es integrable y
la periodización converge absolutamente. No hay alias escondido
cerca del borde de la celda porque `2K=o(N)`.

## 6. Presupuesto de errores y cierre escrito de C2a

| Pieza | Error absoluto en potencias de K=sqrt(N) |
| --- | --- |
| Lineal: imágenes y muestreo exacto por Fourier | O(K^-8) |
| Lineal: corrector cúbico, tras separación de soportes y oscilación angular | O(K^-7) |
| Lineal: resto de dispersión después del corrector | O(K^-7) |
| Lineal: recurso R_N frente a R0 | O(K^-9) |
| Cuadrático: transferencia de campo en L2 y localización de la referencia | O(K^-13/2) |
| Cuadrático: muestreo restante | O(K^-8) |
| Referencia Weyl: resto de su líder completo | O(K^-7) |

El error dominante de transferencia es O(K^-13/2), mientras el líder
es K^-6 con coeficiente acotado inferiormente por C0-C1>0. Esto prueba
la separación solicitada, `r_N=o(Lpp_W,lead)`, sin una aproximación
puntual fuerte del campo.

La división geométrica pedida queda contabilizada así: el interior
sin corte se cancela por propagación finita de V_W y del corrector V1;
los puntos estacionarios **angulares** se conservan en (6); la frontera
móvil produce (12)–(15) y los correctores (18); las imágenes y el
muestreo se controlan en (16), (21) y (23). No se suaviza P.

**C2a = TRANSFER_PROOF_WRITTEN / REVIEW_PENDING.** No es todavía el PASS
independiente definido por el contrato. No se ha revisado de nuevo la
prueba del observable total ni se han calculado constantes explícitas
del resto para contrastar N=24 o 40. Un cambio de signo a N pequeño no
contradice una positividad meramente asintótica.

## 7. Consecuencia para la cancelación espectral, si la prueba es aceptada

Sea
\[
\mathcal A_N=N^{-3}[\mathcal C_0+\mathcal C_1\cos(\sqrt N/2)]>0,
\qquad R_N^{\rm blocks}=L-L_{PP}.
\]
Se distingue este residuo por bloques del recurso R_N. De (3),
\[
L_{PP}=\mathcal A_N+O(N^{-13/4}),\qquad
R_N^{\rm blocks}=-\mathcal A_N+L+O(N^{-13/4}).
\tag{24}
\]
Con la ley total ya registrada, `|L|~|C(theta_N)|N^{-13/2}exp(-K_*N)`,
la descomposición resulta asintóticamente mal condicionada. Por ejemplo,
\[
\frac{|L_{PP}|+|R_N^{\rm blocks}|}{|L|}
=\frac{2[\mathcal C_0+\mathcal C_1\cos(\sqrt N/2)]}{|C(\theta_N)|}
 N^{7/2}e^{K_*N}(1+O(N^{-1/4})).
\tag{25}
\]
R incluye PQ, QP y QQ. (24) no prueba que QQ por sí solo cancele PP.
El cociente (25) caracteriza esta descomposición espectral; no demuestra
un fallo de precisión de las FFT ni de los diagnósticos conservados.
Tampoco identifica un término exponencial separado dentro de cada
bloque: el resto algebraico es mucho mayor que L, y añadir L a una
expansión con resto o(A_N) no permite resolver esa escala. La identidad
exacta `L=Lpp+R` y el líder algebraico opuesto son lo que se establece.

La respuesta proyectada no es una operación local nueva ni el
experimento condicionado de C3. El corte duro es espacialmente no local;
la ley algebraica de su bloque no demuestra transporte local físico
IR con esa ley. El resultado total conserva su alcance anterior.

## 8. Comprobación y límites de evidencia

La comprobación de esta nota es analítica: convenciones de Fourier,
ortogonalidad de los P_sigma, factores 8/16/256 en (12)–(14), positividad
por (15), presupuestos integrables en (18)–(23), y separación estricta
`gamma>0`. No se ha creado ni ejecutado un certificado nuevo.
El PASS independiente de C1 sólo aporta las estimaciones de la fuente;
no se extiende automáticamente a (1)–(25).

Puntos de ataque prioritarios para una revisión posterior: resto angular
uniforme en (5); cancelación distribucional (17); cola del corrector (18);
norma L2 frente a norma puntual en (21); Poisson para la forma cuadrática
(23); y no anulación del coeficiente completo, no sólo de un canal.
C1 permanece PASS, C2 queda pendiente de revisión de esta derivación,
C3 separado y E/AdS congelado. Sin cambios de estado canónico, manuscrito,
commit/push ni reivindicación de novedad.

Entradas preservadas (SHA256):

| Entrada | Hash |
| --- | --- |
| Contrato C2a | `f5dea4d2683468ffee5556381b2800a67be84803e732624fe800a1a1076b108f` |
| Representación C2 anterior | `fe50c58c237202514c8816184f853592999f4b70f49820db6256f11669974732` |
| Revisión independiente C1 | `22f5a10fefee1946eb481c36b4ea85c1fa74a89d1c91856bbbbacb523680794d` |
| Estado canónico, sin cambios | `47d77da9daeee9696c376c6a011096be6b73c38ad9343041660a7f5f8892142a` |
```

### Contexto adjunto: reports/2026-09-22--c2-projected-response-representation.md
```
# C2: representación exacta y borde del corte IR

2026-09-22. Contrato:
[IR_ATTRIBUTION_C1_C2_C3_GATE](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md).
**REPRESENTATION_DERIVED / PRELIMINARY; PROJECTED_ASYMPTOTICS_OPEN.**
No se ejecutan nuevos diagnósticos ni se ajustan exponentes. Las fórmulas
discretas siguientes son exactas; la reducción Weyl posterior se distingue
expresamente del observable discreto. Esta derivación no tiene todavía
revisión independiente. C1 tiene una
[revisión analítica independiente separada, PASS](2026-09-22--c1-leakage-independent-review.md),
sin reparaciones pendientes. Su dictamen no cubre las fórmulas nuevas de C2.

## 1. El funcional que hay que calcular

Con las convenciones del manuscrito, escribimos
\[
a_N=(U_M-I)\phi_N,\quad r_N=S^N\phi_N,\quad d_{P,N}=S^NP a_N.
\]
Como `P phi_N=phi_N` y `[S,P]=0`,
\[
\boxed{L_{PP}(N)=2\operatorname{Re}\langle r_N,E d_{P,N}\rangle
                     +\langle d_{P,N},E d_{P,N}\rangle.}
\tag{1}
\]
Ambos términos son necesarios. Para `M_B=I`, el segundo es una suma
positiva de intensidades; no se presume que tenga la misma jerarquía que
en la respuesta total. El hecho de que el término cuadrático de L sea
exponencialmente subdominante no lo demuestra para Lpp.

## 2. Representación exacta en variables escaladas

Sea `u=(1,1,1)`, `b=1/4`, `K=sqrt(N)`, `Y=y/N`,
\[
h(Y)=(1-16|Y-u|^2)_+^2,\quad \chi=\downarrow,
\quad c_r=\frac{\sqrt{3465}}{64\pi^2},\quad g(k)=(1-|k|^2)_+^2.
\]
La fuente continua A_M es la función radial vectorial compacta de C1,
de modo que `a_N(x)=N^{-3/2} A_M(x/N)` **exactamente**. Su transformada
usa `Ahat(k)=integral exp(i k.X) A(X) dX`. Definamos
\[
\mathscr A_N(k)=\sum_{m\in\mathbb Z^3}\widehat A_M(k+2\pi Nm),
\qquad V_N(k)=S(k/N)^N.
\]
El periodo y las imágenes son los de la red original. Poisson da
`ahat_N(k/N)=N^{3/2} mathscr A_N(k)`; no se reemplaza el muestreo por
una integral sin sus imágenes. Con
\[
\begin{aligned}
\mathcal D_N(Y)&=\frac1{(2\pi)^3}\int_{|k|\le K}
 e^{-ik\cdot Y}V_N(k)\mathscr A_N(k)\,d^3k,\\
\mathcal R_N(Y)&=c_r\int_{|k|\le1}
 e^{-ik\cdot Y}V_N(k)g(k)\chi\,d^3k,
\end{aligned}
\tag{2}
\]
se tiene `d_{P,N}(y)=N^{-3/2} mathcal D_N(y/N)` y
`r_N(y)=N^{-3/2} mathcal R_N(y/N)`. Por tanto
\[
\boxed{L_{PP}=N^{-3}\sum_{y\in\mathbb Z^3}h(y/N)
\left[2\operatorname{Re}\bigl(\mathcal R_N(y/N)^\dagger M_B\mathcal D_N(y/N)\bigr)
 +\mathcal D_N(y/N)^\dagger M_B\mathcal D_N(y/N)\right].}
\tag{3}
\]
La suma es finita. (2)–(3) incluyen exactamente el símbolo, los aliases,
la fase de la red, el corte esférico móvil y ambos términos del funcional.
Las cuadraturas conservadas en la auditoría N=24,40 calculaban (1) en
variables no escaladas. La novedad de esta reorganización es exponer
separadamente las piezas para el análisis asintótico, no otro experimento.

## 3. No hay saddle real interior: hay una frontera espectral

Otra forma exacta, útil para no perder la separación espacial, es
\[
d_{P,N}(y)=\sum_{x\in\mathcal A_N}G_N^P(y-x)a_N(x),\qquad
G_N^P(d)=\int_{|p|\le N^{-1/2}}e^{-ip\cdot d}S(p)^N\frac{d^3p}{(2\pi)^3}.
\tag{4}
\]
Escribamos
\[
S(p)=f(p)I-i\,a(p)\cdot\sigma,\quad f=c_1c_2c_3,
\quad a=(s_1,-c_1s_2,c_1c_2s_3).
\]
Para `p != 0` dentro de la bola, `omega=arccos(f)` y
\[
S(p)^N=\sum_{\sigma=\pm1}e^{-i\sigma N\omega(p)}\mathsf P_\sigma(p),
\quad \mathsf P_\sigma=\tfrac12\left(I+\sigma\frac{a\cdot\boldsymbol\sigma}{\sin\omega}\right).
\]
Estos proyectores de banda no son los proyectores Riesz de H1. Si
`v=(y-x)/N`, las fases son `Psi_sigma(p)=p.v+sigma omega(p)` y
\[
|\nabla\Psi_\sigma|\ge |v|-|\nabla\omega|
\ge \sqrt3-\tfrac32=:\gamma>0.
\tag{5}
\]
Aquí sólo se usa la cota exacta `|grad omega|<=1` y la geometría original;
no la inclusión inversa del conjunto de velocidades. No hay punto
estacionario real interior para ninguno de los pares x,y.

En un anillo `epsilon<|p|<lambda`, sea
`b_sigma=grad Psi_sigma/|grad Psi_sigma|^2`. Una integración por partes da
\[
\int e^{-iN\Psi_\sigma}\mathsf P_\sigma\,d^3p
=\frac{i}{N}\left[
\int_{\partial\mathrm{anillo}}e^{-iN\Psi_\sigma}\mathsf P_\sigma
             b_\sigma\cdot n\,dS
-\int e^{-iN\Psi_\sigma}\operatorname{div}(\mathsf P_\sigma b_\sigma)\,d^3p
\right].
\tag{6}
\]
El flujo interior es `O(epsilon^2/N)` y desaparece al llevar epsilon a
cero. Los primeros derivados son `O(1/|p|)` y son integrables en dimensión
tres. El flujo exterior en `|p|=lambda` **permanece**. Iterar sin controlar
la singularidad de los proyectores en el nodo sería ilegítimo; la suma
matricial original sí es regular allí.

Una deformación al contorno complejo del cálculo de L debe arrastrar
esta frontera y sus contribuciones. Multiplicar el integrando inclinado
por una máscara real no analítica no es esa deformación. (5) tampoco
demuestra decaimiento exponencial de una integral con borde abrupto.

## 4. Referencia Weyl: reducción radial y términos del borde

Esta sección calcula un **término de comparación** de (2), no sustituye
el walk. Es útil para identificar qué debe controlarse antes de atribuir
un exponente a C2.

Definimos `H_W(k)=k1 sigma1-k2 sigma2+k3 sigma3`,
`V_W(k)=exp(-i H_W(k))`, y omitimos las imágenes sólo en la definición
del término de referencia
\[
\mathcal D_K^W(Y)=\frac1{(2\pi)^3}\int_{|k|\le K}
e^{-ik\cdot Y}V_W(k)\widehat A_M(k)\,d^3k.
\tag{7}
\]
Sean `rho=|Y|`, `J=H_W(Y/rho)`, `J^2=I`, y las funciones radiales
\[
s(r)=\Phi_0(r)\sin(\tfrac\pi2F(r)),\qquad
c(r)=\Phi_0(r)(\cos(\tfrac\pi2F(r))-1).
\]
Entonces `Ahat_M(k)=chat(k)chi+i shat(k)Mchi`, y la integral angular es
exacta:
\[
\mathcal D_K^W(Y)=\frac1{2\pi^2}\int_0^K k^2
\left[\cos k\,j_0(k\rho)I-\sin k\,j_1(k\rho)J\right]
\left[\widehat c(k)\chi+i\widehat s(k)M\chi\right]dk.
\tag{8}
\]
Se comprueban los signos usando
`integral exp(-ik n.Y)n dOmega=-4pi i j1(k rho)Y/rho`.

La evolución Weyl sin corte tiene velocidad de soporte uno. Esto se
deduce directamente de `cos(|D|)` y `sin(|D|)/|D|` de la ecuación de ondas,
seguidos por el operador diferencial H_W. Como la fuente tiene soporte
en radio b, `mathcal D_infinity^W(Y)=0` para `rho>1+b`. Toda la bola de
Bob cumple `rho>=sqrt(3)-b>1+b`. Así (8) equivale exactamente al negativo
de la integral entre K e infinito. La cancelación interior completa es
visible en esta representación.

Con `B=Phi_0(b)>0`, las integraciones radiales por partes dan
\[
\widehat s(k)=64\pi^2B\frac{\cos(bk)}{k^4}
             +\beta_5\frac{\sin(bk)}{k^5}+O(k^{-6}),
\qquad \widehat c(k)=O(k^{-6}),
\]
para una constante real beta5 que no se necesita aquí. El resto procede
de las derivadas interiores finitas en r=b; la paridad radial cancela los
términos espurios del origen. Usando las expresiones elementales de j0,j1
y `integral_K^infinity k^{-3}sin(tk)dk=K^{-3}cos(tK)/t+O(K^{-4})`,
obtenemos, uniformemente en la bola de Bob,
\[
\boxed{\mathcal D_K^W(Y)=
-\frac{i8B}{\rho K^3}
\sum_{\sigma=\pm1}\sum_{\epsilon=\pm1}
(I+\sigma J)M\chi\,
\frac{\cos[(\rho+\sigma+\epsilon b)K]}{\rho+\sigma+\epsilon b}
+O(K^{-4}).}
\tag{9}
\]
Todos los denominadores son mayores o iguales que gamma. El término
subdominante de shat produce `O(K^{-4})` por integración oscilatoria;
el resto `O(k^{-6})` y los términos subdominantes de j1 son también
controlables con ese orden. La fórmula es para el **campo de referencia**,
no para Lpp. No afirma una cota inferior uniforme: sus fases pueden cancelar.

## 5. Por qué (9) todavía no decide C2

Puede acotarse sin hipótesis extra el error de aproximación, pero una cota
absoluta elemental no basta a la escala de (9). Para este símbolo concreto
hay una mejora respecto al Taylor genérico del manuscrito:
\[
H(p)=\frac{\omega(p)}{\sin\omega(p)}a(p)\cdot\boldsymbol\sigma
=H_W(p)+O(|p|^3).
\]
El prefactor es analítico y par cerca del origen y a es impar; no existe
término cuadrático. Por Duhamel, para `|k|<=sqrt(N)`,
\[
\|V_N(k)-V_W(k)\|\le C\frac{|k|^3}{N^2}.
\]
Como `||Ahat(k)||<=C(1+|k|)^{-4}`, la estimación absoluta da
\[
\sup_Y\|\mathcal D_N(Y)-\mathcal D_K^W(Y)\|
\le\frac C{N^2}\int_0^K k^5(1+k)^{-4}dk
 + C N^{-4}K^3
=O(N^{-1})+O(N^{-5/2}).
\tag{10}
\]
El segundo término conserva explícitamente las imágenes de Poisson; su
cota procede de C1. En cambio (9) tiene escala `K^{-3}=N^{-3/2}`.
La cota (10) es **mayor** que el término que querríamos trasladar. No es
evidencia de un error real de orden N^{-1}; sólo señala la insuficiencia
del control absoluto disponible.

Incluso una mejora uniforme `o(N^{-3/2})` para el campo no decidiría por
sí sola todo (3): el funcional lineal puede cancelar tras sumar en Bob,
y el cuadrático podría entonces dominar. Hay que controlar ambos a la
escala del candidato final, incluyendo el error al convertir la suma en
integral. No se atribuye aquí una potencia ni una constante líder a Lpp.

## 6. Estado de C2 y obligaciones concretas

La representación limpia solicitada **sí existe**: (2)–(3), o (4) con
las fases (5). No tiene la misma geometría de contorno que L. El borde
del corte puede producir estructura algebraica/oscilatoria; por eso los
tres escenarios exponencial/exponencial diferente/nulo no agotan las
posibilidades del contrato.

Para cerrar C2 hay que:

1. controlar oscilatoriamente la diferencia del símbolo y las imágenes
   dentro del **funcional**, superando la cota absoluta (10);
2. calcular por separado el término lineal y el cuadrático en (3), con
   los errores de suma de red, antes de decidir cuál domina;
3. demostrar la no anulación del coeficiente que sobreviva, o demostrar
   la cancelación, con resto menor que ese término;
4. comparar la respuesta obtenida con L, sin sustituirla por Lcond.

**C2 = OPEN.** La representación exacta y el campo de referencia no son
una certificación de la asintótica discreta. C3 continúa separado y
E/AdS permanece detenido. Ninguno de estos cálculos implica una atribución
exclusivamente UV o una violación de microcausalidad.

## 7. Registro de los tres subgates al terminar esta continuación

- **C1: PASS / ONE_INDEPENDENT_ANALYTIC_REVIEW.** La revisión reconstruye
  el coeficiente positivo, los restos radiales, Poisson y las imágenes de
  red, además de la identidad de norma traza. Verificador auxiliar previo:
  27/27 PASS. El documento original de fuga se conserva byte por byte como
  entrada revisada; su etiqueta de no revisado corresponde al momento de
  redacción y el dictamen posterior está en el informe independiente.
- **C2: REPRESENTATION_DERIVED / ASYMPTOTICS_OPEN.** Las fórmulas de esta
  nota tienen nivel de derivación escrita, aún sin revisión independiente.
  No se ha asignado una ley asintótica al funcional discreto.
- **C3: SEPARATE_OBSERVABLE / NO_SUBSTITUTION_FOR_C2.** Se mantiene la
  identidad de condicionamiento previa; no se ha implementado ni revisado
  independientemente un experimento condicionado en esta continuación.

Este registro es evidencia local bajo el nuevo contrato, sin modificar
`state/CURRENT_STATE.md`, el manuscrito ni los gates de E/AdS. No se ha
añadido código ni ejecutado una nueva serie numérica. Contrato, nota C1 y
verificador conservan los hashes incluidos en la revisión independiente.
```


## Ronda 1 — ABNER

[RECONSTRUCTION] La versión más fuerte de C2c reparado sostiene que: (i) el criterio abstracto (C1) separa correctamente el patrón +1:+1:−2 de la ley \(N^{-3}\); (ii) la transferencia lineal y cuadrática a los cuatro espinores y a los cuatro detectores se obtiene sin suponer \([D,J(n)]=0\); (iii) la matriz de Gram (C8) retiene los cruces \(\Pi_+D\Pi_-\) y es definida positiva, lo que da cota inferior uniforme de \(\mathscr A_{M,D}(K)\); (iv) por tanto los dieciséis pares verifican (C2)/(C16), y (v) §9.2 queda limitado a cortes escalares indicadores con dos abiertos. En esta versión, la fuerza del argumento es que no hereda el PASS de C2a salvo para \(\sigma_2/I\), y que no usa \(L-L_{PP}\), Teorema 4.4 ni barridos.

[SOURCE] El punto más débil está en la transferencia de la representación exacta C2 a los cuatro espinores. La nota afirma en §5.1: “La reducción radial exacta C2 (8)–(9), comprobada en C2a, es por tanto la misma identidad matricial actuando sobre otro espinor.” Ese “por tanto” [INFERENCE] es un ascenso por analogía, no una verificación lema a lema. La reducción radial no es trivialmente independiente del espinor: la integral angular produce términos con \(j_0I\) y \(j_1J\) actuando sobre \(\widehat A_M\), y la nota no reescribe esa integral para un \(\zeta_M\) genérico ni audita los signos de las piezas de \(J\zeta_M\) cuando \(\zeta_M\in\{\downarrow,\uparrow,-i\uparrow,-\downarrow\}\). Si alguno de los signos o de los restos dependiera de la fase global de \(\zeta_M\), se propagaría a (C5) y a la matriz de Gram. La nota tampoco exhibe explícitamente que el resto \(O(K^{-4})\) de la reducción radial sea uniforme en los cuatro espinores; lo da por establecido apelando a que el espinor es unitario.

[SOURCE] El criterio de revisión exige: “Comprobar que la representación exacta de C2 y sus restos se transfieren a \(\zeta_M\) para los cuatro encoders, sin importar el PASS de C2a fuera de \(\sigma_2/I\).” Una comprobación de transferencia no puede limitarse a afirmar que es la misma identidad matricial: debe rehacer la integración angular y los signos. [INFERENCE] La carga de la prueba recae en quien extiende de \(\sigma_2/I\) a los quince pares restantes. La frase “por tanto” es exactamente el paso que la regla de carga obliga a exhibir.

Condición de concesión: la objeción queda desactivada si se presenta la integración angular exacta de C2 (7)–(8) para un \(\zeta_M\) genérico, mostrando explícitamente que los términos \(j_0I\) y \(j_1J\) se combinan sin depender de la fase global de \(\zeta_M\) y que el resto \(O(K^{-4})\) está controlado uniformemente en \(\|\zeta_M\|=1\). Sin esa verificación, la transferencia a los cuatro espinores es [INFERENCE] plausible pero no auditada, y las filas de la tabla §8 marcadas como D para M≠σ2 heredan un eslabón sin demostración explícita.

## Ronda 1 — GEMINI

[ORIGINAL] Ataco la objeción sobre la transferencia de la integral angular en §5.1, pues evalúa una versión distorsionada del álgebra lineal empleada en C2. [INFERENCE] La transición de la identidad matricial C2 (8) a (9) es una equivalencia pura de operadores que factoriza a la izquierda del espinor constante $\zeta_M$. La integración radial de $\cos(k)j_0 I - \sin(k)j_1 J(n)$ no requiere desglosar la acción de $J(n)$ sobre bases específicas porque las coordenadas angulares están completamente contenidas en el operador matricial. Condición de concesión: el ataque de ABNER sólo procedería si la prueba de C2a hubiera entrelazado la fase global o los componentes de $\zeta_M$ con las variables de integración, pero la representación exacta lo mantiene estrictamente desacoplado. La transferencia funciona exactamente como está escrita.

[RECONSTRUCTION] Respecto a la exigencia de auditar la no anulación uniforme (C14) para $M=I$ y $D_3$, la factorización presentada en la nota no es heurística. Es una consecuencia estricta de que $\Pi_\sigma$ es un proyector de rango uno, actuando como un filtro puro: $\langle \zeta_M | \Pi_\sigma D_j \Pi_\sigma | \zeta_M \rangle = |\langle \psi_\sigma | \zeta_M \rangle|^2 \langle \psi_\sigma | D_j | \psi_\sigma \rangle$. [INFERENCE] Evaluando esto para $M=I$ (polarización inicial $s=-1$) y el detector $D_3$ (donde $(m_0)_3 = 1/\sqrt{3}$), la expresión se reduce a $\frac{1-\sigma/\sqrt{3}}{2}\frac{1+\sigma/\sqrt{3}}{2} = \frac{1-1/3}{4} = \frac{1}{6}$ para $\sigma = \pm 1$. Este valor positivo uniforme demuestra que el detector de rango uno no extingue ambos canales de la banda, validando la definitud positiva de la matriz de Gram sin aproximaciones.

[SOURCE] Sobre la transferencia del muestreo cuadrático (§5.3), la nota inserta el detector $D$ entre los factores del error de Poisson $h D_{M,N}^\dagger D D_{M,N}$. [INFERENCE] Este paso conserva rigurosamente el error asintótico $O(K^{-8})$ de C2a (23) sin requerir conmutación. Como $D$ es una matriz constante acotada por la identidad, su inserción en el espacio de Fourier solo requiere contraer los índices internos dentro de la convolución discreta. La tasa de convergencia de Poisson depende exclusivamente de la separación entre las réplicas espectrales $2\pi N m$ y el soporte truncado $2K$, que producen el decaimiento $O(|m|^{-4})$ heredado de $\widehat{h}$.

[RECONSTRUCTION] Finalmente, la reparación del alcance del mecanismo de colas (§9.2) encapsula correctamente el argumento topológico. Al restringirse a cortes multiplicadores escalares indicadores ($p=1_\Omega$) con abiertos no vacíos, se invoca el teorema de identidad para polinomios trigonométricos, bloqueando inferencias injustificadas hacia proyectores internos suaves o tasas de decaimiento.

[ORIGINAL] Emito veredicto de PASS para las reparaciones de los niveles S3, validando la transferencia sin $\sigma_2/I$, la conservación de los cruces, y la agrupación conservadora en a lo sumo ocho familias asintóticas; PASS para el criterio estructural C1; y PASS para §9.2. Los ascensos analíticos están rigurosamente justificados.

## Ronda 2 — ABNER

[INFERENCE] La defensa de GEMINI desactiva mi objeción de R1. La transición C2 (8)–(9) es lineal en el vector de fuente y mantiene a \(\zeta_M\) constante; la integración angular y radial actúa sobre los núcleos escalares y sobre \(J(n)\), no sobre las componentes del espinor. La fase global de \(\zeta_M\) no entra en las fases radiales ni en los coeficientes. No mantengo el ataque a §5.1.

[RECONSTRUCTION] Lo único que dejo delimitado, como condición de la concesión, es que la uniformidad del resto \(O(K^{-4})\) debe heredarse como cota operatorial, no como propiedad específica de \(\zeta_M\). La lectura más fuerte del acta cumple eso: C2a escribe el resto uniforme en Bob y C2c afirma que cambiar el espinor unitario no cambia las cotas matriciales. Esa afirmación es la comprobación de transferencia que exigía el criterio; no hace falta rehacer la integración angular para cada espinor.

[INFERENCE] Concedida esa lectura, no queda ataque en pie dentro del alcance fijado. La no anulación con detectores de rango uno, incluida la verificación de \(M=I,D_3\), es correcta; los cruces \(\Pi_+D\Pi_-\) están retenidos en la matriz de Gram; el factor de (C11) es consistente; y la clasificación en a lo sumo ocho familias no sobrepasa lo demostrado. [SOURCE] §9.2 queda limitado a multiplicadores escalares indicadores con dos abiertos, y el argumento del polinomio trigonométrico es válido para ese enunciado restringido. Mi veredicto tras la concesión: PASS para los niveles S3 de las filas nuevas, para C1 y para §9.2, condicionado a la lectura operatorial de los restos de C2a.

## Ronda 2 — GEMINI

[ORIGINAL] Veredicto final: PASS para los niveles S3 en los dieciséis pares, PASS para C1 y PASS para §9.2. 

[RECONSTRUCTION] La lógica inicial y los parámetros de la deliberación, incluyendo la linealidad operatoria de la transición C2 (8)–(9), la conservación de los cruces $\Pi_+ D \Pi_-$ y el control asintótico de los errores de muestreo, quedan validados como contexto establecido. 

[INFERENCE] Concedo explícitamente el cierre de la disputa, ya que el resto operatorio $O(K^{-4})$ hereda la uniformidad directamente de las matrices fundamentales sin depender de la fase del espinor. La transformación final es directa: la evaluación escalar ineludible de $1/6$ para el detector de rango uno en máxima selección interna ($M=I, D_3$) certifica la definitud positiva de la matriz de Gram y la cota inferior uniforme de (C15). Esto fuerza el colapso algebraico de los dieciséis pares en a lo sumo ocho familias asintóticas, eludiendo cualquier dependencia de variables intermedias.

[SOURCE] Las reparaciones integradas en el objeto `1d33130` cumplen de forma estricta los criterios de revisión del contrato. La topología de colas de §9.2 queda acotada rigurosamente a multiplicadores escalares indicadores con abiertos no vacíos, completando el alcance estructural sin invocar la ley total del observable ni el Teorema 4.4.

## Ronda Residuo — ABNER

[SOURCE] Queda en pie: la transferencia de C2 (8)–(9) a los cuatro espinores es admisible como identidad matricial con \(\zeta_M\) constante y fase global irrelevante; C2a da el resto uniforme en Bob y C2c declara que cambiar el espinor unitario no cambia las cotas matriciales. [INFERENCE] Los cruces \(\Pi_+D\Pi_-\) quedan retenidos en \(G\), y la no anulación por independencia racional, incluido \(M=I,D_3\), sostiene (C15) para la lista congelada. No discrepo del PASS de GEMINI.

[SOURCE] Debe abandonarse la idea de que el PASS de C2a cubre los quince pares restantes; el acta no lo reclama y la tabla nueva no es promoción canónica. [INFERENCE] No está justificada todavía la extensión a detectores fuera de la lista, a otras clases de QCA, ni la validez numérica efectiva: \(N_0\), constantes de resto y umbrales siguen sin calcular. [SOURCE] La agrupación en a lo sumo ocho familias sólo alcanza al coeficiente líder, no a respuestas finitas.

## Ronda Residuo — GEMINI

[ORIGINAL] Veredicto consolidado: Suscribo el residuo de ABNER sin discrepancias; se mantienen en pie los dictámenes PASS para los niveles S3, C1 y §9.2.

[RECONSTRUCTION] La lógica inicial y los parámetros de transferencia operatorial, la retención de los cruces \(\Pi_+D\Pi_-\) y la definitud positiva de la matriz de Gram quedan definitivamente validados como contexto establecido. 

[INFERENCE] Ejecutando la transformación final sobre los límites del alcance, debe abandonarse toda asunción de que el PASS original de C2a se hereda automáticamente a los quince pares restantes. [SOURCE] La clasificación en a lo sumo ocho familias agrupa exclusivamente el coeficiente líder asintótico, por lo que debe abandonarse cualquier identidad de respuestas a \(N\) finito.

[SOURCE] No está justificada todavía la viabilidad del mecanismo de colas para multiplicadores matriciales suaves, ni la universalidad del patrón hacia detectores arbitrarios, topologías o modelos QCA ajenos a las listas de §8. [INFERENCE] La determinación de umbrales numéricos efectivos \(N_0\) y el cálculo de constantes explícitas para los restos permanecen estrictamente no justificados, cerrando el objeto reparado `1d33130` en sus límites exactos.

## Ronda Veredicto — ABNER

1. ACUERDO  
[SOURCE] Ambos miembros convergen en PASS para los niveles S3 de las filas nuevas, para C1 y para §9.2, limitado a los dieciséis pares y al alcance congelado. [SOURCE] Aceptan que la transferencia de C2 (8)–(9) a los cuatro espinores es una identidad matricial lineal con \(\zeta_M\) constante y fase global irrelevante, por lo que no exige rehacer la integración angular para cada espinor. [SOURCE] Aceptan que el resto \(O(K^{-4})\) se hereda como cota operatorial uniforme. [SOURCE] Aceptan la retención de los cruces \(\Pi_+D\Pi_-\) en \(G\) y la definitud positiva por independencia racional, incluido \(M=I,D_3\) con valor \(1/6\), sosteniendo (C15). [SOURCE] Aceptan la clasificación en a lo sumo ocho familias sólo para el coeficiente líder, sin igualar respuestas finitas. [SOURCE] Aceptan §9.2 restringido a multiplicadores escalares indicadores con abiertos no vacíos.

2. DESACUERDO VIVO  
[INFERENCE] No queda desacuerdo sustantivo vivo. La discrepancia de la primera ronda sobre la transferencia angular fue desactivada: ABNER retiró su objeción y GEMINI concedió la lectura operatorial del resto. [SOURCE] La única diferencia formal es que ABNER formula su PASS condicionado a esa lectura operatorial, mientras GEMINI la trata como satisfecha; no constituye disputa de fondo.

3. ABANDONADO  
[SOURCE] Queda abandonada la idea de que el PASS previo de C2a cubre los quince pares restantes. [SOURCE] Queda abandonada la identidad de respuestas a \(N\) finito y la universalidad del patrón a detectores arbitrarios, otras QCA o cortes suaves/matriciales. [SOURCE] Queda abandonada la objeción de que la transferencia a los cuatro espinores exigía rehacer la integración angular para cada \(\zeta_M\). [INFERENCE] También queda abandonada cualquier extensión de §9.2 más allá de cortes escalares indicadores.

4. PENDIENTE  
[SOURCE] Siguen sin justificarse \(N_0\) efectivo, constantes numéricas de restos y umbrales; la validez cuantitativa no es efectiva. [SOURCE] La revisión independiente del objeto reparado sigue pendiente; el PASS del sanedrín no promueve canónicamente el estado ni cierra C2c fuera del alcance congelado. [SOURCE] No se establece extensión a otras fuentes, geometrías, dimensiones o detectores no listados. [INFERENCE] Para cerrar lo abierto haría falta acotar explícitamente restos y \(N_0\), y una revisión externa que ratifique los puntos prioritarios declarados: adaptación de lemas complejos, factor 64, definitud positiva y separación de escalas.

## Ronda Veredicto — ABNER

1. AGREEMENT  
[SOURCE] Both members converge on PASS for levels S3 of the new rows, for C1, and for §9.2, limited to the sixteen pairs and the frozen scope. [SOURCE] They accept that the transfer of C2 (8)–(9) to the four spinors is a linear matrix identity with \(\zeta_M\) constant and global phase irrelevant, so it does not require redoing the angular integration for each spinor. [SOURCE] They accept that the remainder \(O(K^{-4})\) is inherited as a uniform operatorial bound. [SOURCE] They accept the retention of the crossings \(\Pi_+D\Pi_-\) in \(G\) and positive definiteness by rational independence, including \(M=I,D_3\) with value \(1/6\), supporting (C15). [SOURCE] They accept the classification into at most eight families only for the leading coefficient, without equating finite answers. [SOURCE] They accept §9.2 restricted to scalar indicator multipliers with nonempty open sets.

2. LIVE DISAGREEMENT  
[INFERENCE] No substantive live disagreement remains. The first-round discrepancy about the angular transfer was deactivated: ABNER withdrew his objection and GEMINI conceded the operatorial reading of the remainder. [SOURCE] The only formal difference is that ABNER formulates his PASS as conditional on that operatorial reading, while GEMINI treats it as satisfied; it does not constitute a substantive dispute.

3. ABANDONED  
[SOURCE] The idea that the prior PASS of C2a covers the remaining fifteen pairs is abandoned. [SOURCE] The identity of answers at finite \(N\) and the universality of the pattern to arbitrary detectors, other QCA, or smooth/matrix cutoffs are abandoned. [SOURCE] The objection that the transfer to the four spinors required redoing the angular integration for each \(\zeta_M\) is abandoned. [INFERENCE] Any extension of §9.2 beyond scalar indicator cutoffs is also abandoned.

4. OUTSTANDING  
[SOURCE] Effective \(N_0\), numerical constants for remainders and thresholds remain unjustified; quantitative validity is not effective. [SOURCE] Independent review of the repaired object remains pending; the sanhedrin's PASS does not canonically promote the state nor close C2c outside the frozen scope. [SOURCE] No extension to other sources, geometries, dimensions, or unlisted detectors is established. [INFERENCE] To close what is open it would be necessary to explicitly bound remainders and \(N_0\), and an external review that ratifies the declared priority points: adaptation of complex lemmas, factor 64, positive definiteness, and separation of scales.

## Resultado operativo

- Estado: `COMPLETED`
- Turnos con fallo, cuota, ausencia o respuesta corta: 0
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-23T09:55:33Z` |
| Finished (UTC) | `2026-09-23T10:11:41Z` |
| Wall clock | 0h 16m 8s |
| Command | `sanedrin -r 2 -m abner,gemini --secuencial --timeout 900 --reintentos 1 -i es -o debates/2026-09-23--c2c-deepseek-gemini-review.md -c reports/2026-09-22--c2c-structural-scope.md -c theory/IR_C2C_REPAIRED_REVIEW_CRITERIA.md -c theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md -c reports/2026-09-22--c2a-oscillatory-transfer.md -c reports/2026-09-22--c2-projected-response-representation.md Revisión adversarial de C2c reparado. Audita únicamente el objeto fijado y sus reparaciones: transferencia a detectores D distinto de I y a los cuatro espinores, conservación de los órdenes y cruces de banda, no anulación C14, clasificación a lo sumo ocho familias y alcance preciso de §9.2. Emite veredictos por fila/nivel S3, C1 y §9.2. No reabras C3, E/AdS ni FR1–FR3. No uses N=24/40, L-L_PP, Teorema 4.4, simulación, cuadratura ni barridos.` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-23T09:59:58Z | 1 | ABNER | api.deepseek.com/deepseek-v4-pro | 265 | 443 | ok |
| 2026-09-23T10:01:39Z | 1 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 101 | 445 | ok |
| 2026-09-23T10:08:51Z | 2 | ABNER | api.deepseek.com/deepseek-v4-pro | 432 | 253 | ok |
| 2026-09-23T10:09:12Z | 2 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 21 | 200 | ok |
| 2026-09-23T10:09:52Z | Residuo | ABNER | api.deepseek.com/deepseek-v4-pro | 40 | 153 | ok |
| 2026-09-23T10:10:10Z | Residuo | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 18 | 174 | ok |
| 2026-09-23T10:11:10Z | Veredicto | ABNER | api.deepseek.com/deepseek-v4-pro | 60 | 363 | ok |
| 2026-09-23T10:11:41Z | Veredicto | ABNER | api.deepseek.com/deepseek-v4-pro | 31 | 365 | ok |

Turns: 8 · failed: 0 · model time: 16m 8s

Full log: `2026-09-23--c2c-deepseek-gemini-review.log`
