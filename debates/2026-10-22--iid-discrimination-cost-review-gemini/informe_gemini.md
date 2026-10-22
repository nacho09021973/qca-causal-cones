<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ d32e8507c32aefc0acd0721a000eeeb2a261d824; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 9b4a1d94214494e23afece076b33e017e142a7c79f1b026be0dcea2a1a9b1557; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 d685ac12e3d14d652edb8cc23e84040a13d2e82cea9210994ed99b5187765c5b
inicio: 2026-10-22T07:36:41Z  fin: 2026-10-22T07:38:12Z
documento: /home/ignac/qca-causal-cones/reports/2026-09-28--iid-message-discrimination-cost.md ; último commit observado: adba394 ; sha256 de la copia enviada 44244cd773cc0270b10bf8c75b7dc6c5f67a9a7001f83c426e6f69cf5ab26f81
documento: /home/ignac/qca-causal-cones/theory/SCALED_IR_SIGNALING_GATE.md ; último commit observado: 31b5797 ; sha256 de la copia enviada 325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c
entrada_gemini.txt sha256 d8eb93c124c06b0283062ef2143d8c663f8b4f5ab0b01d62058ef477da6148e1
respuesta sha256 6e3a69d62389e564c782861a4b804786c459fa44153fcff3c2a3cafe9ce7b4a5
-->

A continuación se presenta la revisión matemática adversarial e independiente del **Documento 1** (`2026-09-28--iid-message-discrimination-cost.md`), contrastado contra el contrato fijado en el **Documento 2** (`SCALED_IR_SIGNALING_GATE.md`).

---

### Declaración de alcance y elementos NO VERIFICADOS
Por las reglas de la sesión sellada, se toman como premisas heredadas sin recalcular (y quedan marcadas como **NO VERIFICADO** en su origen externo):
1. La asintótica principal $\delta_N = |C(\theta_N)| N^{-13/2} e^{-K_* N}(1 + O(N^{-1/2}))$ y el hecho de que $C(\theta_N)$ está uniformemente separado de cero (y acotado superiormente) para los 16 pares (`CURRENT_STATE.md` §8.20 / manuscrito `ir-corona.tex`).
2. El desarrollo del campo libre $r_N(y) = N^{-3/2} R_0(y/N) + O(N^{-5/2})$ uniforme en $B_N$, la normalización asintótica de $Z_N$ que fija la constante $c_r > 0$, y el límite en `2026-09-23--c3-conditioning-execution.md` (lema `lem:tail`).
3. Las cotas uniformes $D_B \le 4T_N \le 36 N^4 e^{-JN}$ y $D_B \le 4N^3(1+10N)e^{-K_* N}$ y el alcance de su demostración en el sector de una partícula (`thm:upper`, `thm:rate` en `ir-corona.tex`).
4. Las páginas específicas citadas de Fuchs–van de Graaf y Watrous (`Theory of Quantum Information.pdf`), aunque las desigualdades matemáticas que se les atribuyen se verifican aquí desde primeros principios.

---

### Revisión por secciones

#### Sección 2 (§2): El fondo queda separado de cero y de uno

**1. Rehacer derivaciones clave:**
* **Suma de Riemann (1):** Para el mensaje $b=0$, $U^{(0)} = I$, por lo que $\psi_0(N) = S^N \phi_N = r_N$. En el sector de una partícula (Documento 2, §4), $E_B$ actúa como $h_B \otimes M_B$, con $h_B(y) = (1 - 16|y/N - u|^2)_+^2$, $u=(1,1,1)$. La probabilidad de clic es:
  $$p_{0,N} = \sum_{y \in B_N} h_B(y) \, r_N(y)^\dagger M_B r_N(y).$$
  Sustituyendo la premisa $r_N(y) = N^{-3/2} R_0(y/N) + \varepsilon_N(y)$ con $\|\varepsilon_N(y)\| = O(N^{-5/2})$ uniformemente en $y \in B_N$, y usando $\|M_B\| = 1$, $0 \le h_B \le 1$, el término principal de $r_N(y)^\dagger M_B r_N(y)$ es $N^{-3} R_0(y/N)^\dagger M_B R_0(y/N)$, mientras que los términos cruzados y cuadráticos en $\varepsilon_N$ son $O(N^{-3/2} \cdot N^{-5/2}) + O(N^{-5}) = O(N^{-4})$ uniformemente en $B_N$ (ya que $R_0$ es continua en un compacto y por tanto acotada). Al sumar sobre $|B_N \cap \mathbb{Z}^3| = O(N^3)$ sitios, el error de amplitud aporta $O(N^3 \cdot N^{-4}) = O(N^{-1})$. La suma principal $N^{-3} \sum_{y \in \mathbb{Z}^3} (1 - 16|y/N - u|^2)_+^2 R_0(y/N)^\dagger M_B R_0(y/N)$ es una suma de Riemann de un integrando continuo con soporte compacto $\{|Y-u| \le 1/4\}$, que converge exactamente a la integral (1). **Correcto.**
* **Positividad y analiticidad real ($P_3$ incluido):** $R_0(Y)$ es la transformada de Fourier inversa (o directa, según el signo de la fase tras el escalado $p = q/N$) de $\hat{R}_0(q) = c_r g(q) e^{-i H_W(q)} \binom{0}{1}$, soportada en la bola compacta $|q| \le 1$. Por el teorema de Paley–Wiener, $R_0(Y)$ (y por ende $M_B^{1/2} R_0(Y)$) es la restricción a $\mathbb{R}^3$ de una función entera en $\mathbb{C}^3$, luego es analítica real en $\mathbb{R}^3$.
  Si el integrando se anulara en toda la bola abierta $|Y-u| < 1/4$, entonces $M_B^{1/2} R_0(Y) = 0$ en dicho abierto (pues el peso $(1-16|Y-u|^2)^2 > 0$ allí). Por continuación analítica conexa en $\mathbb{R}^3$, $M_B^{1/2} R_0(Y) \equiv 0$ en todo $\mathbb{R}^3$. Por unicidad de la transformada de Fourier, $M_B^{1/2} \hat{R}_0(q) = 0$ para todo $q$ (al ser continua en $|q| \le 1$). Como $M_B \ge 0$, esto equivale a $M_B \hat{R}_0(q) = 0$.
  - En $q=0$, $g(0)=1$, $H_W(0)=0$, $e^{-i H_W(0)} = I$, luego $\hat{R}_0(0) = c_r \binom{0}{1}$ con $c_r > 0$.
  - Para $M_B = I$: $I \binom{0}{1} = \binom{0}{1} \neq 0$.
  - Para $P_1 = \frac{1}{2}\binom{1 \ \ 1}{1 \ \ 1}$: $P_1 \binom{0}{1} = \frac{1}{2}\binom{1}{1} \neq 0$.
  - Para $P_2 = \frac{1}{2}\binom{1 \ -i}{i \ \ \ 1}$: $P_2 \binom{0}{1} = \frac{1}{2}\binom{-i}{1} \neq 0$.
  - Para $P_3 = \frac{I+\sigma_3}{2} = \binom{1 \ 0}{0 \ 0}$: en $q=0$ se tiene $P_3 \binom{0}{1} = 0$. Calculamos la derivada parcial respecto a $q_1$ en $q=0$ de $f(q) := c_r^{-1} P_3 \hat{R}_0(q) = g(q) P_3 e^{-i(q_1\sigma_1 - q_2\sigma_2 + q_3\sigma_3)} \binom{0}{1}$. Como $g(q) = (1-|q|^2)^2$ en $|q|<1$, tenemos $g(0)=1$ y $\partial_{q_1} g(0) = 0$. Por tanto:
    $$\partial_{q_1} f(0) = g(0) P_3 (-i \sigma_1) e^0 \binom{0}{1} = -i P_3 \sigma_1 \binom{0}{1} = -i P_3 \binom{1}{0} = -i \binom{1}{0} \neq 0.$$
  La expresión del texto (`-i P_3 sigma_1 down != 0`) es exacta (salvo el escalar no nulo $c_r$, que no afecta la no nulidad). Como $M_B^{1/2} R_0$ es continua y no idénticamente nula en $|Y-u|<1/4$, el integrando es estrictamente positivo en un abierto interior, luego $p_\infty^{(M_B)} > 0$. **Correcto.**
* **Cota estricta $< 1$:** Como $0 \le M_B \le I$, $R_0^\dagger M_B R_0 \le \|R_0\|^2$. El peso extendido $h(Y) = (1-16|Y-u|^2)_+^2$ cumple $0 \le h(Y) < 1$ para todo $Y \neq u$. Dado que $\|R_0(Y)\|^2$ es analítica real e integra $1$ en $\mathbb{R}^3$, no es idénticamente nula y por tanto es $>0$ c.t.p. en $\mathbb{R}^3$. Así, $1 - p_\infty^{(M_B)} \ge \int_{\mathbb{R}^3} (1 - h(Y)) \|R_0(Y)\|^2 d^3Y > 0$. **Correcto.**

**2. Búsqueda de errores y cuantificadores:**
* No hay errores de signo ni de constantes.
* Cuantificadores: La separación uniforme respecto de $0$ y $1$ ($m \le p_{b,N} \le 1-m$ para $N \ge N_0$) se deduce correctamente para ambos $b \in \{0,1\}$ y los 16 pares porque $p_{0,N}$ depende solo de $M_B$ (hay 4 límites $p_\infty^{(M_B)} \in (0,1)$) y $|p_{1,N} - p_{0,N}| = \delta_N \to 0$ para las 4 elecciones de $M$.
* *Cuestión menor de redacción:* Al escribir la derivada en $q_1=0$ como `-i P_3 sigma_1 down`, se omite el factor $c_r$ de la definición previa `c_r g(q) exp(-i H_W(q)) down`. No altera en nada el argumento de no nulidad.

**Veredicto §2:** **PASS**.

---

#### Sección 3 (§3): Problema exacto de decisión y cotas de repeticiones

**1. Rehacer derivaciones clave:**
* **Fórmula del error óptimo (2):** Para $X_1, \dots, X_R \stackrel{\text{i.i.d.}}{\sim} \text{Bern}(p_{b,N})$ y prior uniforme $(1/2, 1/2)$, la probabilidad de observar una cadena $x \in \{0,1\}^R$ con peso de Hamming $k = \sum x_i$ es $p_{b,N}^k (1-p_{b,N})^{R-k}$. El test de máxima verosimilitud (Bayes óptimo) elige el bit que maximiza esta probabilidad, cometiendo en la cadena $x$ un error condicional $\frac{1}{2}\min\{p_{0,N}^k (1-p_{0,N})^{R-k}, p_{1,N}^k (1-p_{1,N})^{R-k}\}$. Sumando sobre las $\binom{R}{k}$ cadenas de peso $k$ y sobre $k=0,\dots,R$, se obtiene exactamente (2). **Correcto.**
* **Desigualdades de Bhattacharyya/TV (3)–(4):**
  Sean $P, Q$ dos distribuciones de probabilidad discretas, $TV = \frac{1}{2}\sum_x |P(x)-Q(x)|$, y $B = \sum_x \sqrt{P(x)Q(x)}$.
  - *Cota inferior de TV:* Como $|\sqrt{a}-\sqrt{b}| \le \sqrt{|a-b|}$, tenemos $(\sqrt{P}-\sqrt{Q})^2 \le |P-Q|$. Sumando en $x$: $2 - 2B \le 2TV \implies 1 - B \le TV$.
  - *Cota superior de TV:* Por Cauchy–Schwarz,
    $$(2TV)^2 = \left(\sum |\sqrt{P}-\sqrt{Q}|(\sqrt{P}+\sqrt{Q})\right)^2 \le \left(\sum (\sqrt{P}-\sqrt{Q})^2\right)\left(\sum (\sqrt{P}+\sqrt{Q})^2\right) = (2-2B)(2+2B) = 4(1-B^2),$$
    luego $TV \le \sqrt{1-B^2}$.
  - Para la ley producto $P_b = \text{Bern}(p_{b,N})^{\otimes R}$, la afinidad se factoriza como $B(P_0, P_1) = B_N^R$. Sustituyendo en $P_e^*(R,N) = \frac{1 - TV(P_0, P_1)}{2}$ se obtiene inmediatamente (3):
    $$\frac{1 - \sqrt{1 - B_N^{2R}}}{2} \le P_e^*(R,N) \le \frac{B_N^R}{2}.$$
  - *Paso a (4):* Como $\delta_N > 0$ (para $N$ grande donde $C(\theta_N)\neq 0$) y $p_{b,N} \in (0,1)$, por desigualdad de Cauchy–Schwarz estricta se tiene $0 < B_N < 1$ y $a_N = -\log B_N > 0$.
    - Cota superior: Si $R = \lceil \frac{\log(1/(2\epsilon))}{a_N} \rceil$, entonces $R a_N \ge \log(1/(2\epsilon)) \implies \frac{1}{2} B_N^R = \frac{1}{2} e^{-R a_N} \le \epsilon \implies P_e^*(R,N) \le \epsilon$. Como $R_\epsilon(N)$ es el mínimo entero que cumple $P_e^* \le \epsilon$, se tiene $R_\epsilon(N) \le \lceil \frac{\log(1/(2\epsilon))}{a_N} \rceil$.
    - Cota inferior: Por definición, para $R = R_\epsilon(N)$ se cumple $P_e^*(R,N) \le \epsilon$. Por la cota inferior de (3),
      $$\frac{1 - \sqrt{1 - B_N^{2R}}}{2} \le \epsilon \iff 1 - 2\epsilon \le \sqrt{1 - B_N^{2R}}.$$
      Como $0 < \epsilon < 1/2$, ambos lados son positivos; elevando al cuadrado:
      $$(1-2\epsilon)^2 = 1 - 4\epsilon(1-\epsilon) \le 1 - B_N^{2R} \iff B_N^{2R} = e^{-2R a_N} \le 4\epsilon(1-\epsilon) \iff R \ge \frac{\log[1/(4\epsilon(1-\epsilon))]}{2a_N}.$$
      **Ambas cotas en (3) y (4) son exactas.**
* **Expansión de la afinidad y uniformidad del resto:**
  Sea $p \in [m, 1-m]$ con $m > 0$ y $|d| \le m/2$. Expandiendo por Taylor alrededor de $d=0$:
  $$\sqrt{p(p+d)} = p\sqrt{1 + \frac{d}{p}} = p\left(1 + \frac{d}{2p} - \frac{d^2}{8p^2} + \frac{d^3}{16p^3} + O\left(\frac{d^4}{p^4}\right)\right) = p + \frac{d}{2} - \frac{d^2}{8p} + \frac{d^3}{16p^2} + O_m(d^4).$$
  Análogamente, reemplazando $p \mapsto 1-p$ y $d \mapsto -d$:
  $$\sqrt{(1-p)(1-p-d)} = 1 - p - \frac{d}{2} - \frac{d^2}{8(1-p)} - \frac{d^3}{16(1-p)^2} + O_m(d^4).$$
  Sumando ambas expresiones:
  $$B_N = 1 - \frac{d^2}{2}\left(\frac{1}{4p} + \frac{1}{4(1-p)}\right) + O_m(|d|^3) = 1 - \frac{d^2}{8p(1-p)} + O_m(|d|^3).$$
  Como $p \in [m, 1-m]$, las derivadas terceras están acotadas por una constante que solo depende de $m$, por lo que el resto $O(|d|^3)$ es uniforme en $N$. Tomando $a_N = -\log B_N = (1 - B_N) + O((1-B_N)^2)$ y usando $p_{0,N} \to p_\infty^{(M_B)} \in (0,1)$ y $|d| = \delta_N \to 0$, se obtiene $a_N = \frac{\delta_N^2}{8 p_\infty^{(M_B)}(1-p_\infty^{(M_B)})}(1+o(1))$. **Correcto.**
* **Resultado (5) con $\Theta$:**
  Sustituyendo $a_N$ y la premisa $\delta_N = |C(\theta_N)| N^{-13/2} e^{-K_* N}(1 + O(N^{-1/2}))$ en (4), se obtiene exactamente (5). Además, como $0 < c_1 \le |C(\theta_N)| \le c_2 < \infty$ por premisa, $\frac{1}{N}\log R_\epsilon(N) = 2K_* + O\left(\frac{\log N}{N}\right) \to 2K_*$. **Correcto.**
* **Segunda vía (6) con $\chi^2$ y Chebyshev:**
  - *Test de umbral y Chebyshev (Laguna de una constante):* Sea $\bar{X} = \frac{1}{R}\sum_{i=1}^R X_i$ y el umbral $\tau = \frac{p_{0,N}+p_{1,N}}{2}$. La distancia de la media de cada hipótesis al umbral es $|\mathbb{E}_b[\bar{X}] - \tau| = \frac{\delta_N}{2}$. La varianza bajo el bit $b$ es $\text{Var}_b(\bar{X}) = \frac{p_{b,N}(1-p_{b,N})}{R}$.
    Si se aplica la desigualdad de Chebyshev estándar unilateral/bilateral:
    $$\mathbb{P}_b(\text{error}) \le \mathbb{P}_b\left(|\bar{X} - p_{b,N}| \ge \frac{\delta_N}{2}\right) \le \frac{\text{Var}_b(\bar{X})}{(\delta_N/2)^2} = \frac{4 p_{b,N}(1-p_{b,N})}{R \delta_N^2}.$$
    Para obtener la cota del texto $\le \frac{1}{R \delta_N^2}$, es **imprescindible** usar la cota uniforme de la varianza de Bernoulli $p_{b,N}(1-p_{b,N}) \le 1/4$, la cual cancela exactamente el factor $4$ procedente de $(1/2)^2 = 1/4$ en el denominador (o bien usar la desigualdad de Cantelli $\frac{\sigma^2}{\sigma^2 + (\delta_N/2)^2} < \frac{4\sigma^2}{\delta_N^2} \le \frac{1}{R\delta_N^2}$). La cota $\le 1/(R\delta_N^2)$ es **matemáticamente verdadera**, pero el texto no menciona que el $1/4$ de $p(1-p) \le 1/4$ cancela el $4$ del semiancho $(\delta_N/2)^2$.
  - *Cota inferior con $\chi^2$ (6):*
    Por definición, para $P_1 = \text{Bern}(p_1)$ y $P_0 = \text{Bern}(p_0)$:
    $$\chi^2(P_1 \| P_0) = \frac{(p_1 - p_0)^2}{p_0} + \frac{((1-p_1)-(1-p_0))^2}{1-p_0} = \delta_N^2 \left(\frac{1}{p_0} + \frac{1}{1-p_0}\right) = \frac{\delta_N^2}{p_0(1-p_0)}.$$
    Como $1 + \chi^2(Q \| P) = \sum_x \frac{Q(x)^2}{P(x)}$, para distribuciones producto se factoriza: $1 + \chi^2(P_1^{\otimes R} \| P_0^{\otimes R}) = (1 + \chi^2(P_1 \| P_0))^R$.
    Por Cauchy–Schwarz, $(2 TV(Q,P))^2 = \left(\sum_x \frac{|Q(x)-P(x)|}{\sqrt{P(x)}}\sqrt{P(x)}\right)^2 \le \chi^2(Q \| P) \cdot 1$, luego $TV \le \frac{1}{2}\sqrt{\chi^2}$.
    Para $R = R_\epsilon(N)$, $P_e^* = \frac{1-TV}{2} \le \epsilon \implies 1 - 2\epsilon \le TV \le \frac{1}{2}\sqrt{\chi^2(P_1^{\otimes R} \| P_0^{\otimes R})}$, de donde:
    $$4(1-2\epsilon)^2 \le \chi^2(P_1^{\otimes R} \| P_0^{\otimes R}) = \left(1 + \frac{\delta_N^2}{p_{0,N}(1-p_{0,N})}\right)^R - 1.$$
    Despejando $R$ se obtiene exactamente (6). **Correcto.**
* **Caso límite $p_0 = 0, p_1 = \delta$:**
  Si $p_0 = 0$ y $p_1 = \delta \in (0,1)$, bajo $b=0$ la única cadena con probabilidad positiva (igual a $1$) es $0^R$. Para $x \neq 0^R$, el término mínimo en (2) es $0$. Para $x = 0^R$ ($k=0$), el mínimo es $\min\{1, (1-\delta)^R\} = (1-\delta)^R$. Por tanto, $P_e^* = \frac{1}{2}(1-\delta)^R$, lo que da $R_\epsilon = \lceil \frac{\log(1/(2\epsilon))}{-\log(1-\delta)} \rceil = \Theta(\delta^{-1})$ cuando $\delta \to 0$. **Correcto.**

**2. Búsqueda de errores y cuantificadores:**
* No hay confusión entre error medio y error máximo por bit: el documento define claramente el problema por defecto con error medio $\le \epsilon$ y prior uniforme, y en el párrafo de la segunda vía justifica correctamente que exigir error $\le \epsilon$ bajo **cada** bit mantiene el mismo orden $\Theta(\delta_N^{-2})$ porque el error máximo domina al error medio (heredando la cota inferior (6)) y el test de umbral acota simultáneamente ambos errores condicionales por $1/(R\delta_N^2)$.
* Los subíndices en $\Theta_{\epsilon, M, M_B}$ reflejan adecuadamente que las constantes dependen de $\epsilon$ y del par $(M, M_B)$ fijo, pero son uniformes en $N$.

**Veredicto §3:** **PASS** (con una observación menor de exposición sobre la cancelación $4 \cdot \frac{1}{4} = 1$ en Chebyshev).

---

#### Sección 4 (§4): Preparaciones, mediciones y postselección

**1. Revisión de fórmulas y lógica:**
* El recuento de recursos ($R$ copias, $RN$ pasos-copia, modalidad secuencial vs. paralela) es claro y preciso.
* La ley ternaria (7) para un protocolo con éxito de postselección $s_b$ y probabilidad condicionada de clic $q_b$ suma $(1-s_b) + s_b q_b + s_b(1-q_b) = 1$ y representa fielmente el registro completo cuando no se descartan los fallos.
* La distinción entre esperanza del número de ensayos ($r/s$ cuando $s_0=s_1=s$) y garantías con probabilidad fija (que requieren controlar la cola binomial negativa), así como la advertencia sobre la información contenida en las marcas de fallo cuando $s_0 \neq s_1$, son rigurosas.
* La aplicación de la desigualdad de procesamiento de datos (el posprocesamiento clásico no aumenta TV) es correcta.

**2. Comprobación de afirmaciones de alcance:**
* Respeta estrictamente el Documento 2 (§4 y §5): el recurso $\phi_N$ se asume disponible sin coste de preparación certificado, el protocolo congelado no admite postselección, y los proyectores espectrales $C_1$–$C_3$ no son operaciones locales admisibles del contrato. No hay ninguna sobreafirmación.

**Veredicto §4:** **PASS**.

---

#### Sección 5 (§5): Qué extensión ya se deduce de las cotas uniformes

**1. Rehacer derivaciones clave:**
* **Cota de un uso (8):** Heredada del manuscrito (`thm:rate`, parte (d)) para el sector de una partícula: $D_B(N) \le \eta_N := \min\{1, 4N^3(1+10N)e^{-K_* N}\}$, donde $D_B(N) = D(\rho_{0,B}, \rho_{1,B}) = \frac{1}{2}\|\rho_{0,B} - \rho_{1,B}\|_1$ es la distancia de traza en $B_N$.
* **Telescopación y cota (9):**
  Sean $\rho_0^{(i)}, \rho_1^{(i)}$ los estados reducidos en Bob en el uso $i \in \{1,\dots,R\}$, con entradas independientes entre usos. Podemos escribir la diferencia de productos tensoriales como la suma telescópica:
  $$\bigotimes_{i=1}^R \rho_0^{(i)} - \bigotimes_{i=1}^R \rho_1^{(i)} = \sum_{j=1}^R \left(\bigotimes_{i=1}^{j-1} \rho_0^{(i)}\right) \otimes \left(\rho_0^{(j)} - \rho_1^{(j)}\right) \otimes \left(\bigotimes_{i=j+1}^R \rho_1^{(i)}\right).$$
  Aplicando la desigualdad triangular para la distancia de traza $D(\cdot,\cdot) = \frac{1}{2}\|\cdot\|_1$ y la multiplicatividad de la norma traza respecto al producto tensorial ($\|A \otimes B\|_1 = \|A\|_1 \|B\|_1$, con $\|\rho_b^{(i)}\|_1 = 1$):
  $$D\left(\bigotimes_{i=1}^R \rho_0^{(i)}, \bigotimes_{i=1}^R \rho_1^{(i)}\right) \le \sum_{j=1}^R D(\rho_0^{(j)}, \rho_1^{(j)}) \le R \eta_N.$$
  Como la distancia de traza nunca supera $1$, se tiene $D \le \min\{1, R\eta_N\}$. Por el teorema de Helstrom, para **cualquier** POVM conjunto en el sistema compuesto $B_N^{\otimes R}$, el error medio óptimo con prior uniforme cumple:
  $$P_{e,\text{opt}} = \frac{1 - D(\rho_{0,B}^{\otimes R}, \rho_{1,B}^{\otimes R})}{2} \ge \frac{1 - \min\{1, R\eta_N\}}{2}.$$
  **La derivación de (9) es completamente rigurosa** (incluso para protocolos no idénticos entre usos mientras las entradas sean independientes y cada uso cumpla (8)).
* **Cota (10):**
  Para alcanzar $P_{e,\text{opt}} \le \epsilon < 1/2$, (9) exige $\frac{1 - \min\{1, R\eta_N\}}{2} \le \epsilon \iff \min\{1, R\eta_N\} \ge 1 - 2\epsilon > 0$. Como $1 - 2\epsilon < 1$, esto equivale a $R\eta_N \ge 1 - 2\epsilon$, es decir:
  $$R \ge \frac{1 - 2\epsilon}{\eta_N}.$$
  Para $N$ suficientemente grande, $4N^3(1+10N)e^{-K_* N} < 1$, por lo que $\eta_N = 4N^3(1+10N)e^{-K_* N} = \Theta(N^4 e^{-K_* N})$, de donde:
  $$R \ge \frac{1-2\epsilon}{4N^3(1+10N)} e^{K_* N} = \Omega_\epsilon(N^{-4} e^{K_* N}) \qquad (N \to \infty).$$
  En consecuencia, si $R = e^{o(N)}$, entonces $R\eta_N \to 0$ y $P_{e,\text{opt}} \to 1/2$. **Correcto.**

**2. Búsqueda de errores y alcance de las premisas:**
* El texto delimita con total honestidad que (8) **solo** está probada en el sector de una partícula (usando la estructura de bloques de vacío y una partícula del estado reducido en Fock), y que **no** aplica a estados arbitrarios de muchas partículas ni a entradas entrelazadas/correlacionadas entre los $R$ usos.
* Asimismo, distingue perfectamente entre la tasa $2K_*$ de (5) (específica del detector binario congelado con fondo $p_\infty \in (0,1)$) y la cota inferior uniforme con tasa $K_*$ de (10) (que permite cualquier estado inicial de una partícula y cualquier medición conjunta en $B_N^{\otimes R}$, donde un protocolo hipotético con fondo nulo podría no sufrir la penalización cuadrática de $\delta_N^2$).

**Veredicto §5:** **PASS**.

---

#### Sección 6 (§6): Obligaciones que quedan para una frontera operacional

**Comprobación de afirmaciones de alcance:**
* Las 5 limitaciones enumeradas (geometría congelada en la diagonal vs. margen arbitrario fuera del cono, restricción a una partícula sin ancillas ni adaptatividad ni correlación entre usos, ausencia de protocolo positivo en el interior del cono, falta de universalidad/perturbaciones, y carácter no efectivo de $N_*$ y de los restos) son exactas, exhaustivas y plenamente coherentes con el "Techo de reclamo" (§8) del Documento 2. No existe ninguna sobreafirmación.

**Veredicto §6:** **PASS**.

---

### Resumen de hallazgos y Veredicto Global

* **Errores matemáticos:** Ninguno. Todas las identidades, desigualdades, constantes, signos y órdenes asintóticos en (1)–(10) son exactos.
* **Lagunas de justificación:** Ninguna que invalide un paso. Únicamente hay un paso implícito trivial en §3 al aplicar Chebyshev al test de umbral (donde el factor $4$ de $(1/2)^2$ en el denominador se cancela con la cota $p(1-p) \le 1/4$ de la varianza de Bernoulli).
* **Cuestiones de redacción (opcionales, no bloqueantes):**
  1. En §2 (**Positividad**), en `-i P_3 sigma_1 down != 0`, podría escribirse `-i c_r P_3 sigma_1 down != 0` para mantener el prefactor $c_r$ de la línea anterior.
  2. En §3 (**Segunda vía de comprobación**), podría añadirse tras «error bajo cada bit $\le 1/(R\delta_N^2)$» el paréntesis «(usando $\text{Var}(X_i) = p_{b,N}(1-p_{b,N}) \le 1/4$ y distancia al umbral $\delta_N/2$)».

**Veredicto por sección:**
* **§2:** **PASS**
* **§3:** **PASS**
* **§4:** **PASS**
* **§5:** **PASS**
* **§6:** **PASS**

**Veredicto Global:** **PASS** (sin reparaciones obligatorias).
