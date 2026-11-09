<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 323a8c9d24ca8e916f8ad23f73d1a2a5fd70dc634b3a5a2c5fe781b6f69a1399
inicio: 2026-11-03T12:15:06Z  fin: 2026-11-03T12:16:00Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--hex-supremum.md ; último commit observado: 8abca3c ; sha256 de la copia enviada 8a4c4eece8cda613d9945e8aa106729620e31c958c1c43941c70d781d0db26b5
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_supremum_gate.py ; último commit observado: 8abca3c ; sha256 de la copia enviada ef4b0114124d16937ced9a600a65b229c6fd968ab417d8493d1297806bf46a55
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_ceiling_gate.py ; último commit observado: bb4fcdb ; sha256 de la copia enviada 8f3b7a10ecee91c515429640b794da91e2c0e273176f5bbbd62e56a0f3b43d72
documento: /home/ignac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
entrada_gemini.txt sha256 b1ef01f64fc78e3b902c98bd5669c3d5b0d18b870e2f6e9675025e0f3d53b408
respuesta sha256 207fcc8645016ab6129bd20ffa1eda60ff15ccb8a52d6aedc6a1ec59cf226400
-->

### Revisión Adversarial e Independiente: `HEX_SUPREMUM` (Etapa A y M1-B13)

He auditado de forma independiente cada afirmación matemática, paso algebraico y rutina de verificación de `2026-11-03--hex-supremum.md` y `verify_hex_supremum_gate.py`, contrastándolos con su contrato (`HEX_SUPREMUM_GATE.md`) y los documentos promovidos del gate padre (`HEX_CEILING_GATE.md`).

---

### 1. LEMA A1
**Dictamen: PASS**

* **Malla uniforme y nivel extremo $r = N\delta$:** Por el paso L0 del gate padre (Sec. 1 de `hex-ceiling`), si $C = \operatorname{conv} F$ es un hexágono regular centrado con vértices en la red triangular $\Lambda$, el vector arista $d = p g_1 + q g_2 \in \Lambda$ define la normal exterior unitaria $n_f = \operatorname{Rot}_{90}(d)/|d|$. Para todo $h = a g_1 + b g_2 \in \Lambda$ (antes de reescalar), el producto escalar es $h \cdot n_f = \frac{\sqrt{3}}{2|d|}(bp - aq) = m_h \delta_{\text{raw}}$ con $m_h \in \mathbb{Z}$. Al normalizar la longitud de los vértices a $1$ dividiendo por $L = |v|$ (donde en un hexágono regular $|d| = L$), el espaciado reescalado es $\delta = \frac{\sqrt{3}}{2L^2}$. Como los vértices pertenecen a $F \subset \Lambda$ y en ellos se alcanzan los extremos $\pm h_C(n_f) = \pm r_{\text{in}} = \pm \frac{\sqrt{3}}{2}$, existe un entero $N = m_{v_{\text{top}}} \in \mathbb{Z}_{>0}$ tal que $r = r_{\text{in}} = N\delta$, y para todo $h \in C \cap \Lambda$ se cumple $h \cdot n_f = m_h \delta$ con $m_h \in \{-N, \dots, N\}$.
* **Rigidez de saturación y capa unitaria (*singleton*):** Evaluando $U(k) = \sum_{h \in F} A_h e^{-i k \cdot h}$ sobre la recta $k = t n_f$, al agrupar por niveles de proyección $m \in \{-N, \dots, N\}$ se obtiene el polinomio de Laurent matricial en una variable $z = e^{-i\delta t}$:
  $$U(t n_f) = \sum_{m=-N}^{N} \left(\sum_{h \in F,\; h \cdot n_f = m\delta} A_h\right) e^{-i m \delta t}.$$
  La rigidez en la línea normal a la cara (Sec. 3, Paso 1 de `hex-ceiling`, caso de igualdad de Bernstein / lema de Julia) exige que si $c_0 = r$, entonces idénticamente en $t \in \mathbb{R}$:
  $$U(t n_f) = e^{-i N \delta t} P_+(n_f) + e^{i N \delta t} P_-(n_f).$$
  Por la independencia lineal de los caracteres $\{e^{-i m \delta t}\}_{m=-N}^N$, el coeficiente de cada frecuencia intermedia ($|m| < N$) se anula exactamente: $\sum_{h \in C \cap \Lambda,\; h \cdot n_f = m\delta} A_h = 0$ (tomando $A_h = 0$ si $h \notin F$). Si para algún $m \in (-N, N)$ la intersección de $C \cap \Lambda$ con el hiperplano $\{x \cdot n_f = m\delta\}$ consta de un único punto $h_0$, la suma se reduce a un término y fuerza $A_{h_0} = 0$, sin ninguna hipótesis adicional sobre $F$.

---

### 2. GEOMETRÍA DE S13
**Dictamen: PASS**

* **Recuento de puntos de $S_{13}$:** Para $v = g_1 + g_2 = (3/2, \sqrt{3}/2)$, la longitud sin normalizar es $L = \sqrt{9/4 + 3/4} = \sqrt{3}$ y el inradio sin normalizar es $r_{\text{raw}} = L\frac{\sqrt{3}}{2} = \frac{3}{2}$. Las seis normales unitarias $n_f$ (rotadas $\pi/6 + j\pi/3$ respecto de $v$, que está a $\pi/6$) apuntan en los ángulos $\pi/3 + j\pi/3$, que son exactamente las seis direcciones de los vectores cortos de la red ($\pm g_1, \pm g_2, \pm(g_2 - g_1)$). Para $h = a g_1 + b g_2$, las tres proyecciones independientes son:
  $$h \cdot g_1 = a + \frac{b}{2}, \quad h \cdot g_2 = \frac{a}{2} + b, \quad h \cdot (g_2 - g_1) = \frac{b - a}{2}.$$
  La condición $|h \cdot n_f| \le \frac{3}{2}$ equivale a $|2a+b| \le 3$, $|a+2b| \le 3$ y $|b-a| \le 3$. Como $(2a+b) + (b-a) = a+2b$, un par $(a,b) \in \mathbb{Z}^2$ pertenece a $S_{13}$ si y solo si los tres enteros $x = 2a+b$, $y = b-a$, $z = -(a+2b)$ suman $0$ y satisfacen $\max(|x|,|y|,|z|) \le 3$ con $x \equiv y \pmod 3$. Las soluciones son exactamente:
  1. **Origen (1 punto):** $(x,y,z) = (0,0,0) \implies (a,b) = (0,0)$.
  2. **Anillo interior (6 puntos):** Permutaciones con signo de $(2,-1,-1)$, que corresponden a los 6 vectores de norma $1$ de $\Lambda$: $\pm g_1, \pm g_2, \pm(g_2-g_1)$. Tras dividir por $L=\sqrt{3}$, tienen $|h| = 1/\sqrt{3}$ y ángulos $k\pi/3$.
  3. **Vértices (6 puntos):** Permutaciones con signo de $(3,0,-3)$ y $(3,-3,0)$, que son $\pm(g_1+g_2), \pm(2g_1-g_2), \pm(2g_2-g_1)$, de norma $\sqrt{3}$. Tras dividir por $L=\sqrt{3}$, tienen $|h| = 1$ y ángulos $\pi/6 + k\pi/3$.
  No existen soluciones con $\max(|x|,|y|,|z|) = 1$ (pues $1+0-1$ no cumple $x \equiv y \pmod 3$). Total: $1 + 6 + 6 = 13$ puntos. El barrido `range(-5, 6)` en `hexagon(v)` (línea 58 de `verify_hex_supremum_gate.py`) cubre holgadamente el recinto (que requiere $|a|, |b| \le 2$).
* **Estructura de capas y eliminación del anillo interior:** Con $L = \sqrt{3}$, tras normalizar por $1/L$, el inradio es $r = \sqrt{3}/2$ y la malla de proyección tiene paso $\delta = \frac{1/2}{\sqrt{3}} = \frac{1}{2\sqrt{3}} = \frac{r}{3}$, luego $N = 3$ y los niveles son $m \in \{-3, -2, -1, 0, 1, 2, 3\}$. Para la normal $n_0 = g_1 = (1,0)$, el nivel de $h = a g_1 + b g_2$ es $m = 2a+b$:
  * $m = \pm 3$: $\pm(1,1)$ y $\pm(2,-1)$ (2 vértices en cada borde extremo).
  * $m = \pm 2$: exclusivamente $\pm(1,0) = \pm g_1$ (**1 punto del anillo interior** en $+2$ y **1 punto** en $-2$).
  * $m = \pm 1$: $\pm(0,1)$ y $\pm(1,-1)$ (2 puntos del anillo interior en cada capa).
  * $m = 0$: $(0,0)$ y $\pm(1,-2)$ (el origen y 2 vértices).
  Por simetría bajo rotación de $60^\circ$, a lo largo de las tres normales $n \in \{g_1, g_2, g_2-g_1\}$, las capas $m = \pm 2$ aíslan exactamente como *singletons* a $\pm g_1$, $\pm g_2$ y $\pm(g_2-g_1)$, cubriendo los 6 puntos del anillo interior. Por el Lema A1, sus 6 matrices de coeficientes se anulan, reduciendo el soporte a $F \subseteq \{0\} \cup \operatorname{vert}(H)$.
* **Segunda vía del verificador:** En las líneas 106–124 de `verify_hex_supremum_gate.py`, se asignan $13 \times 8 = 104$ variables reales simbólicas independientes (`a{k}_0:8`) a las partes real e imaginaria de las entradas de $A_0, \dots, A_{12}$, se imponen las ecuaciones lineales exactas de las 7 capas en cada una de las 3 normales ($\sum_{i \in L_m} A_i = P_+(n), P_-(n), \text{ó } 0$), y `sp.solve` resuelve el sistema lineal sobre $\mathbb{Q}(\sqrt{3})$. La comprobación `len(sol) == 1 and all(hexg.base.is_zero_matrix(A[i].subs(sol[0])) for i in inner)` certifica de manera constructiva e independiente que las ecuaciones de capa son compatibles entre sí y fuerzan $A_i = 0$ para los 6 índices del anillo interior.

---

### 3. APLICABILIDAD DE T2
**Dictamen: PASS**

* **Validez en $W_{\text{hex}}^{\text{sym}}$ sin factorización ni red:** La demostración de T2 para el soporte mínimo (Sec. 3 de `hex-ceiling` y `check_T2_minimal` en `verify_hex_ceiling_gate.py`, líneas 166–238) parte únicamente de un polinomio de Laurent matricial $2 \times 2$ con soporte en $\{0\} \cup \operatorname{vert}(H)$ que cumple: (1) nodo e isotropía con $c_0 = r_{\text{in}}$ (que fijan las sumas de capa por rigidez de Bernstein/Julia tras llevar $A(n)$ a la forma normal $r_{\text{in}}\, n \cdot \sigma$), y (2) unitariedad algebraica $\sum_{h_1 - h_2 = d} A_{h_1} A_{h_2}^\dagger = \delta_{d,0} I_2$ y $\sum_{h_1 - h_2 = d} A_{h_2}^\dagger A_{h_1} = \delta_{d,0} I_2$. En ningún punto interviene la descomposición en producto de monedas y desplazamientos $C_n D_n \dots C_1 D_1$ ni la aritmética de la red $\Lambda$ más allá de los 7 vectores de posición.
* **Legitimidad de la semejanza:** Una vez anulado el anillo interior en $S_{13}$, los puntos supervivientes ya están normalizados a longitud de vértice $|v| = 1$ (no hace falta reescalar; el cambio de escala ya se hizo al normalizar $S_{13}$ por $1/\sqrt{3}$), con los vértices situados en ángulos $\pi/6 + k\pi/3$. La rotación espacial $R_{-\pi/6}$ (de $-30^\circ$) lleva estos seis vértices exactamente al conjunto $\{(\cos \frac{k\pi}{3}, \operatorname{sen} \frac{k\pi}{3})\}_{k=0}^5$ de `check_T2_minimal`. Si rotamos simultáneamente el espacio de momentos ($k' = R_{-\pi/6} k$) y el espacio interno de espín mediante $V = e^{i \frac{\pi}{12} \sigma_z} \in SU(2)$ ($\tilde{U}(k') = V U(R_{\pi/6} k') V^\dagger$), la identidad $V (n \cdot \sigma) V^\dagger = (R_{-\pi/6} n) \cdot \sigma$ preserva exactamente la forma normal del término lineal $A(n') = r_{\text{in}}\, n' \cdot \sigma$, los proyectores $P_\pm(n')$ y las relaciones de unitariedad (pues $h_1 - h_2 = d \iff R_{-\pi/6} h_1 - R_{-\pi/6} h_2 = R_{-\pi/6} d$).
* **Codificación abstracta en `check_T2_minimal`:** La inspección de las líneas 174–238 de `verify_hex_ceiling_gate.py` confirma que los vértices se definen directamente en coordenadas cartesianas abstractas `v = [sp.Matrix([sp.cos(sp.pi * k / 3), sp.sin(sp.pi * k / 3)]) for k in range(6)]`, sin referencia a `G1`, `G2` ni a desplazamientos parciales.

---

### 4. LEMA A2
**Dictamen: PASS**

* **Demostración de unicidad y simetría central:** Sea $C = \operatorname{conv} F$ un hexágono regular centrado en el origen y $v$ uno de sus vértices. En los productos $U(k) U(k)^\dagger$ y $U(k)^\dagger U(k)$, el coeficiente de Fourier asociado al desplazamiento $d = 2v \ne 0$ viene dado por $\sum_{h, h' \in F,\; h - h' = 2v} A_h A_{h'}^\dagger$ (y análogamente $A_{h'}^\dagger A_h$).
  1. **Simetría central:** Como $C$ es centralmente simétrico ($C = -C$), para todo $h' \in F \subset C$ se tiene que $-h' \in C$.
  2. **Convexidad y extremalidad:** La condición $h - h' = 2v$ se reescribe como $\frac{1}{2} h + \frac{1}{2}(-h') = v$. Es decir, $v$ es el punto medio del segmento que une $h \in C$ y $-h' \in C$. Por definición geométrica de vértice de un politopo convexo, $v$ es un punto extremo de $C$ (no puede escribirse como combinación convexa no trivial de dos puntos distintos de $C$). Por consiguiente, la igualdad fuerza necesariamente $h = v$ y $-h' = v \iff h' = -v$.
  3. **Conclusión por unitariedad:** La suma para $d = 2v \ne 0$ consta de un único sumando ($A_v A_{-v}^\dagger$ para $U U^\dagger$, y $A_{-v}^\dagger A_v$ para $U^\dagger U$). La unitariedad exige que todos los coeficientes con $d \ne 0$ se anulen, de donde $A_v A_{-v}^\dagger = 0$ y $A_{-v}^\dagger A_v = 0$. El argumento es exacto y válido para cualquier soporte cuyo cierre convexo sea un polígono convexo centralmente simétrico (en particular, todo hexágono regular centrado).

---

### 5. ALCANCE Y NIVELES
**Dictamen: PASS**

* **Adecuación de los veredictos al contrato:**
  * `M1-A: OPEN_AFTER_SINGLETON_LAYER_ANALYSIS` cumple la Sec. 7 de `HEX_SUPREMUM_GATE.md` (los lemas A1 y A2 son válidos en toda la clase, pero por sí solos no cierran $W_{\text{hex}}^{\text{sym}}$ ni reducen $S_{19}$).
  * `M1-B13: PROVED_FOR_S13` y `HX2: CONFIRMED_FOR_S13` se ajustan exactamente a las etiquetas prescritas en la Sec. 7 del contrato para una prueba de brecha (*gap*) en un soporte acotado.
* **Respeto de las exclusiones y separación informe/verificador:** El informe declara expresamente en las Secciones 3, 5 y 6 que el resultado en $S_{13}$ es cualitativo ($c_0 < r_{\text{in}}$, sin reclamar un supremo numérico más allá de T1), que no establece nada para $S_{19}$, soportes mayores ni $s > 2$, y que no cierra ni mantiene la línea M1 (por tratarse de un soporte acotado, conforme a la Sec. 0 del contrato). Asimismo, tanto el informe como el *docstring* de `verify_hex_supremum_gate.py` (líneas 26–31) delimitan con total transparencia qué certifica el script (recuentos de puntos, proyecciones en la malla $\delta = r/N$, estructura de capas de $S_{13}$ y $S_{19}$, resolución lineal simbólica en $S_{13}$, rotación de $-30^\circ$ a los vértices de T2 y re-ejecución de `check_T2_minimal`) y qué reside como prueba analítica en el informe (la rigidez de Bernstein/Julia, la forma normal del Paso 2, el Lema A2 y la invariancia de T2).

*(Nota menor de aclaración, no constituye error ni requiere reparación: en `verify_hex_supremum_gate.py`, línea 23, y en el texto de la pregunta se menciona «rotation by -30 deg, scale»; dado que `hexagon(v)` ya normaliza $|v|=1$ en la línea 62, el factor de escala entre los vértices normalizados de $S_{13}$ y los de `check_T2_minimal` es $1$, por lo que en la línea 128 basta la rotación pura `rot(-sp.pi / 6)`).*

---

### Dictamen Global y Lista de Reparaciones Obligatorias

* **Dictamen Global:** **PASS**
* **Lista de reparaciones obligatorias:** **Ninguna.** No se requiere ninguna reparación en `2026-11-03--hex-supremum.md` ni en `verify_hex_supremum_gate.py`; ambos artefactos son matemáticamente exactos, fieles al contrato `HEX_SUPREMUM_GATE.md` y están listos para su promoción.
