<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 8f27d57c293bd9edf527e5efeb6e081248640a20ffa67732a13b8f309c36fed8
inicio: 2026-10-31T17:32:51Z  fin: 2026-10-31T17:34:19Z
documento: /home/adnac/qca-causal-cones/debates/2026-09-25--schur-physical-bridge-grok-input.md ; último commit observado: f6aad62 ; sha256 de la copia enviada 2c805293f8d3fbe6afb536fc7d6d09a0ef53b245856aaed4936faa134b591fb6
entrada_gemini.txt sha256 c4085e2a74e6496184bf1c05efc4ec56a6abf419c69af93db56ac6e1c13221a8
respuesta sha256 63e563b39cdb1952e3feb1ce008b2543e0734d62e6328a317e36384bdf99529d
-->

# Revisión Adversarial Independiente: Puente Schur → Extremos Físicos Actuales

**Autor auditado:** Codex (OpenAI) (`reports/2026-09-24--schur-stability-physical-transfer.md`)  
**Alcance:** Reconstrucción matemática línea por línea desde las fuentes congeladas adjuntas (`T1` e `ir-corona.tex`), verificando el uso de los extremos físicos actuales, las interfaces del proyector, el dato $Q$ inicial y la distinción entre cota absoluta y líder firmado no nulo.

---

## Resumen de Dictámenes por Gate

1. **SCHUR_STABILITY:** `PASS`
2. **PHYSICAL_ENDPOINTS:** `PASS`
3. **PROPAGATOR_ERROR:** `PASS`
4. **SIGNED_REDUCTION:** `REPAIR_REQUIRED`
5. **CLAIM_CEILING:** `PASS`

---

## 1. SCHUR_STABILITY — Dictamen: `PASS`

### Reconstrucción de las desigualdades (3)–(7)
* **Espectro de $R(p)$ (Ec. 3):** Del Lema 5.2 de `ir-corona.tex`, $\rho(S(\eta-i\xi_*)) \le e^{\Phi(\xi_*)} = \Lambda$, con igualdad si y sólo si $\eta \in \Sigma = \{0,\pi\}^3$. Como $D = S \oplus S^{-1}$ y $\det S = 1$, los autovalores de $S^{-1}(p-i\xi_*)$ son exactamente los recíprocos $\lambda(p)^{\mp 1}$ de los de $S(p-i\xi_*)$, por lo que $\rho(D_\xi(p)) = \rho(S(p-i\xi_*)) \le \Lambda$ y $\rho(R(p)) \le 1$.
* **No normalidad exterior y rangos oblicuos (Ec. 4):** En $\operatorname{Ran} P$, $R_P$ actúa en cada fibra $p \in W$ como multiplicación por el escalar $\lambda(p)/\Lambda$ con $|\lambda(p)| \le \Lambda$, luego $\|R_P^h\|_{L^2 \to L^2} \le 1$ para todo $h \ge 0$ (incluso aunque $P(p)$ no sea ortogonal). En $\operatorname{Ran} Q$:
  - Para $p \in W$, $R_Q(p)$ actúa en el subespacio espectral asociado a $\lambda(p)^{-1}/\Lambda$, donde $|\lambda(p)^{-1}|/\Lambda \le \Lambda^{-2} < 1$, luego es multiplicación escalar en $\operatorname{Ran} Q(p)$ con módulo $\le \Lambda^{-2}$.
  - Para $p \in W^c$ (compacto disjunto de $\Sigma$), $P(p)=0, Q(p)=I_4$ y $\sup_{p \in W^c} \rho(R(p)) = r_0 < 1$. Aplicando el Lema 5.3 de `ir-corona.tex` (triangularización de Schur unitaria $2\times 2$ en cada bloque de $D_\xi$), $\|R(p)^h\| \le r_0^h + h \|R(p)\| r_0^{h-1}$. Fijando $\rho \in (\max(r_0, \Lambda^{-2}), 1)$, existe $C_0(W) < \infty$ tal que $\|R_Q^h\| \le C_0 \rho^h$. Los saltos de $P$ en $\partial W$ no interfieren con $R$ porque $R(p)$ y $P(p)$ son multiplicadores puntuales que conmutan fibra a fibra.
* **Norma adaptada $|\cdot|_*$ y bloques (Ec. 5):** Definiendo $|y|_* = \sup_{h \ge 0} \rho^{-h} \|R_Q^h y\|_2$ en $\operatorname{Ran} Q$, se cumple $\|y\|_2 \le |y|_* \le C_0 \|y\|_2$ y $|R_Q y|_* \le \rho |y|_*$. Como $\|C_N - I\| \le 2\sin(\|\vartheta\|_\infty/(2N)) \le b/N$ y $C_N$ conmuta con $H_\xi$, se tiene $\|T - R\|_{L^2 \to L^2} \le b \|R\| / N$. Usando que $\|P\|_{L^2\to L^2}, \|Q\|_{L^2\to L^2} \le C_P(W)$ y la equivalencia entre $\|\cdot\|_2$ y $|\cdot|_*$, los acoplamientos satisfacen $\|\mathsf{B}\|_{* \to 2}, \|\mathsf{C}\|_{2 \to *} \le a/N$, $\|\mathsf{A}\|_{2 \to 2} \le 1 + a/N$ y $\|\mathsf{D}\|_{* \to *} \le \rho + a/N \le \rho_2 < 1$ para $N$ grande, con $a = a(W, b)$.
* **Recurrencia acoplada y suma doble de Schur (Ec. 6–7):** En la norma $|z|_\oplus = \|Pz\|_2 + |Qz|_*$, $|Tz|_\oplus \le (1+2a/N)|z|_\oplus$, lo que da $\sup_{j \le N} \|T^j\| \le C_0 e^{2a} = C_W$ (y también se verifica de forma independiente por Duhamel + Gronwall discreto). Para $y_N = Q t_N$, la recurrencia $y_{j+1} = \mathsf{C} x_j + \mathsf{D} y_j$ da $|y_N|_* \le \rho_2^N |y_0|_* + \sum_{k=0}^{N-1} \rho_2^{N-1-k} (a/N) \|x_k\|_2 \le C_W (\rho_2^N + N^{-1}) \|s\|_2$. Finalmente, en el kernel de memoria (14) de `T1`,
  \[
  \sum_{m=0}^{n-1} \sum_{k=0}^{m-1} \|\Phi_P(n,m+1)\|_{2\to 2} \|\mathsf{B}\|_{*\to 2} \|G_Q(m,k+1)\|_{*\to *} \|\mathsf{C}\|_{2\to *} \le \sum_{m=0}^{n-1} e^a \frac{a^2}{N^2} \sum_{k=0}^{m-1} \rho_2^{m-1-k} \le \frac{e^a a^2}{N(1-\rho_2)}.
  \]
  No hay confusión de adjuntos ni de normas.

---

## 2. PHYSICAL_ENDPOINTS — Dictamen: `PASS`

### Reconstrucción de las desigualdades (8)–(15)
* **Extremo de Alice con encoder completo (Ec. 8–9):** En `T1` (1), $f = J(U_M - I)\phi_N = J(c_N \phi_N + i s_N M \phi_N)$. Dado que $U_M(x) = e^{i \frac{\pi}{2} F_N(x) M}$ con $M^2 = I$, los autovalores de $U_M(x) - I$ tienen módulo $|e^{\pm i \frac{\pi}{2} F_N(x)} - 1| = 2 |\sin(\frac{\pi}{4} F_N(x))| \le \frac{\pi}{2} F_N(x)$. Esto acota simultáneamente $c_N$ y $s_N$ sin omitir el término coseno. Por (7) de `ir-corona.tex`, $\|\phi_N(x)\| = |\varphi_N(x)| \le C N^{-3/2}$. En las coordenadas de capas de `ir-corona.tex` (§6.4), $x = x_* - \delta \hat u + u_\perp$ con $\delta_j = (\theta_N + j)/\sqrt{3}$ y $F_N(x) = \frac{64}{N^2}(\delta - \frac{\delta^2}{2R_b} - \frac{|u_\perp|^2}{2R_b})_+^2 \le 64 \delta_j^2 / N^2$. El soporte en el plano $j$ es un disco de radio cuadrado $2 R_b \delta_j - \delta_j^2 \le N \delta_j / 2$; como $\Lambda_0$ es una red 2D fija, el número de sitios en ese disco es $\le C(1 + N \delta_j)$ uniformemente en el centro del disco. Con $\xi_* \cdot (x - x_*) = -\sqrt{3} t_* \delta_j = -t_*(\theta_N + j)$, Plancherel da:
  \[
  \|s\|_2^2 = \|H_\xi f\|_{\ell^2}^2 \le C N^{-3} \sum_{j \ge 0} e^{-2t_*(\theta_N+j)} \frac{\delta_j^4}{N^4} (1 + N\delta_j) = O(N^{-6}) \implies \|s\|_2 = O(N^{-3}).
  \]
* **Extremo de Bob actual bajo la hipótesis F (Ec. 10–13):** Bajo F, $\vartheta(x/N) = \int_{\mathbb{R}^3} e^{-ik\cdot x/N} \hat\vartheta(k) \frac{d^3k}{(2\pi)^3}$. En espacio de momentos $p \in \mathbb{T}^3$, la multiplicación por $\vartheta(x/N)$ actúa sobre $\hat\psi(p) = \sum_x e^{ip\cdot x} \psi(x)$ como convolución respecto a la medida periodizada $\mu_N$ empujada por $k \mapsto -k/N \pmod{2\pi}$. Por subaditividad en las fibras del cociente $\mathbb{R}^3 \to \mathbb{T}^3$, $\|\mu_N\|_{\mathrm{TV}} \le a_0$ y $\int_{\mathbb{T}^3} d_{\mathbb{T}}(q,0) d|\mu_N|(q) \le a_1 / N$.
  - En el toro real $\mathbb{T}^3$, $D(p) = S(p) \oplus S(p)^{-1}$ es unitario en $\mathbb{C}^4$ para cada $p$, luego $\|\widehat{D\psi}\|_{L^1(\mathbb{T}^3;\mathbb{C}^4)} = \|\hat\psi\|_{L^1(\mathbb{T}^3;\mathbb{C}^4)}$.
  - Por la desigualdad de Young para medidas en el grupo compacto $\mathbb{T}^3$, la convolución con $-i \frac{\mu_N}{N} \beta$ tiene norma $L^1 \to L^1$ a lo sumo $\|\mu_N\|_{\mathrm{TV}} \|\beta\| / N \le a_0 / N$, y su exponencial $\widehat{C_N}$ tiene norma $L^1 \to L^1$ a lo sumo $e^{a_0/N}$.
  - Iterando $N$ veces sobre $J\phi_N$, se obtiene $\|\widehat{U_N^N J\phi_N}\|_{L^1(\mathbb{T}^3)} \le e^{a_0} \|\hat\phi_N\|_{L^1(\mathbb{T}^3)}$. Como $\hat\phi_N(p) = Z_N^{-1/2} g(Np)\downarrow$ con $Z_N = \Theta(N^{-3})$ y $\operatorname{supp} g(Np) \subset \{|p| \le N^{-1}\}$ de volumen $O(N^{-3})$, tenemos $\|\hat\phi_N\|_{L^1(\mathbb{T}^3)} = O(N^{3/2} \cdot N^{-3}) = O(N^{-3/2})$. Por inversión de Fourier, $\sup_{y \in \mathbb{Z}^3} \|r(y)\| \le \|\hat r\|_{L^1(\mathbb{T}^3)} \le e^{a_0} C N^{-3/2}$.
  - Para $v_c = \mathcal{V}_c^* E r_c$, usando que $\mathcal{F}$ es unitaria de $\ell^2(\mathbb{Z}^3)$ a $L^2(\mathbb{T}^3, d\mu)$ y $r_c = \mathbf{1}_{\mathcal{B}_N} \pi_c r$, tenemos $\|v_c\|_{L^2(\mathbb{T}^3)}^2 = \sum_{y \in \mathcal{B}_N} e^{-2\xi_*\cdot(y-y_*)} h_N(y)^2 \|M_B \pi_c r(y)\|^2$. Con $y = y_* + \delta' \hat u + u'_\perp$, $\xi_*\cdot(y-y_*) = +t_*(\theta_N + j') > 0$ (signo correcto del tilt saliente) y $h_N(y) \le 64 (\delta')^2 / N^2$, la misma suma de capas da $\|v_c\|_2^2 \le C e^{2a_0} N^{-7} \sum_{j'\ge 0} e^{-2t_*(\theta_N+j')} (\delta'_{j'})^4 (1 + N\delta'_{j'}) = O_\vartheta(N^{-6})$, luego $\|v_c\|_2 = O_\vartheta(N^{-3})$.
* **Reconstrucción ponderada y diez piezas (Ec. 14–15):** En (14), $E = h_N \otimes M_B \ge 0$ con $\|M_B\| = 1$ (ya que $M_B \in \{I, (I+\sigma_j)/2\}$ tiene autovalor máximo $1$). No se confunde $E$ con $E^{1/2}$: al factorizar $|\langle d_{c,A}, E d_{c,B} \rangle| \le \|E^{1/2} d_{c,A}\| \|E^{1/2} d_{c,B}\|$, entra exactamente $\sqrt{h_N(y)} = 1 - 16|y-Nu|^2/N^2 = \frac{2R_b \delta' - (\delta')^2 - |u'_\perp|^2}{R_b^2} \le \frac{2\delta'}{R_b} = \frac{8\delta'}{N}$. Maximizando $\frac{8\delta'}{N} e^{-\gamma \delta'}$ en $\delta' \ge 0$ se obtiene el máximo exacto $\frac{8}{e\gamma N}$ en $\delta' = 1/\gamma$. Para la cota inferior en la red, el punto de $\mathbb{Z}^3$ más cercano a $y_* + 2\hat u$ dista a lo sumo $\sqrt{3}/2$, luego $\delta' \in [2-\sqrt{3}/2, 2+\sqrt{3}/2] \subset [1.13, 2.87]$ y $|u'_\perp| \le \sqrt{3}/2$; para $N$ grande esto garantiza $\sqrt{h_N(y)} \ge \frac{2(2-\sqrt{3}/2)}{N/4} - O(N^{-2}) \ge \frac{9}{N}$ y $e^{-\gamma \delta'} \ge e^{-\gamma(2+\sqrt{3}/2)}$, probando rigurosamente $\|E^{1/2}\mathcal{V}_c\| = \Theta(N^{-1})$.

---

## 3. PROPAGATOR_ERROR — Dictamen: `PASS`

### Reconstrucción de las desigualdades (16)–(19)
* **Regularidad de $P(p')\beta P(p)$ e interfaces de $W$ (Ec. 16):** Éste es el punto analítico más delicado. El proyector $P(p)$ se extiende por cero fuera de $W = \bigcup_{\alpha \in \Sigma} W_\alpha$, por lo que $P(p)$ es discontinuo en $\partial W$. Sin embargo, el bloque diagonal $P \vartheta(x/N)\beta P$ tiene núcleo integral $\int_{\mathbb{T}^3} P(p') \beta P(p'-q) d\mu_N(q)$. El operador actúa únicamente cuando **ambos** argumentos $p'$ y $p = p'-q$ pertenecen a $W$; si $p' \notin W$ o $p \notin W$, entonces $P(p') = 0$ o $P(p) = 0$, anulando idénticamente el integrando $P(p')\beta P(p)$. Por tanto, las discontinuidades en $\partial W$ jamás producen términos de borde ni deltas.
  - Cuando ambos $p, p' \in W$: si pertenecen a la misma componente $W_\alpha$, como $\overline{W_\alpha} \subset O_\alpha$ y $p_S$ es analítico en $O_\alpha$ (Ec. 3a de `T1`), $P$ es $C^1$ con derivada uniformemente acotada en el compacto $\overline{W_\alpha}$. Usando (3b) de `T1` ($\beta P(p) = Q(p)\beta$ para $p \in W$) y $P(p)Q(p)=0$, se obtiene $P(p')\beta P(p) = P(p')Q(p)\beta = [P(p') - P(p)] Q(p)\beta = [P(p') - P(p)]\beta P(p)$, cuya norma es $\le \|\nabla P\|_{L^\infty(\overline{W_\alpha})} \|P\|_{L^\infty(W)} d_{\mathbb{T}}(p',p)$.
  - Si $p \in W_\alpha$ y $p' \in W_{\alpha'}$ con $\alpha \ne \alpha'$, como los cierres $\overline{W_\alpha}$ son disjuntos, existe $\delta_W = \min_{\alpha \ne \alpha'} \operatorname{dist}(\overline{W_\alpha}, \overline{W_{\alpha'}}) > 0$, de modo que $\|P(p')\beta P(p)\| \le C_P(W)^2 \le \frac{C_P(W)^2}{\delta_W} d_{\mathbb{T}}(p',p)$.
  - Así, $\|P(p')\beta P(p)\| \le C_W d_{\mathbb{T}}(p',p)$ se cumple para **todo** par $(p', p) \in \mathbb{T}^3 \times \mathbb{T}^3$.
* **Desigualdad de Young con $\mu_N$ y término siempre-$P$ (Ec. 17):** Para cada $q \in \mathbb{T}^3$ fijo, el operador $K_q: f(p') \mapsto P(p')\beta P(p'-q) f(p'-q)$ es una traslación compuesta con un multiplicador puntual acotado por $C_W d_{\mathbb{T}}(q,0)$, por lo que $\|K_q\|_{L^2 \to L^2} \le C_W d_{\mathbb{T}}(q,0)$. Integrando respecto a $d|\mu_N|(q)$ (desigualdad de Minkowski/Young en $L^2(\mathbb{T}^3)$) y usando (10), resulta:
  \[
  \Bigl\| P \frac{\vartheta(x/N)}{N} \beta P \Bigr\|_{L^2 \to L^2} \le \frac{1}{N} \int_{\mathbb{T}^3} \|K_q\|_{L^2 \to L^2}\, d|\mu_N|(q) \le \frac{C_W a_1}{N^2}.
  \]
  Expandiendo $C_N(x) = I - i \frac{\vartheta(x/N)}{N}\beta + R_{2,N}(x)$ con $\|R_{2,N}\|_\infty \le \frac{b^2}{2N^2}$ y usando que $R$ conmuta con $P$, se tiene $\mathsf{A} - R_P = P(C_N - I)R P = -i P \frac{\vartheta(x/N)}{N}\beta P R_P + P R_{2,N} R P$, luego $\|\mathsf{A} - R_P\|_{L^2 \to L^2} \le C'_W / N^2$. Como $\|R_P^k\| \le 1$ y $\|\mathsf{A}^k\| \le e^a$, la suma telescópica $\mathsf{A}^N - R_P^N = \sum_{k=0}^{N-1} \mathsf{A}^{N-1-k}(\mathsf{A} - R_P) R_P^k$ da $\|\mathsf{A}^N - R_P^N\| \le N e^a (C'_W / N^2) = O_W(N^{-1})$.
* **Control de dato $Q$ inicial de orden uno y propagador completo (Ec. 18–19):** ¿Impide un dato $Qs$ de orden $\|s\|$ que $T^N - R^N = O(N^{-1})$? No:
  - En el bloque $P$, la entrada desde $Qs$ es $f_{Q,N} = \sum_{m=0}^{N-1} \Phi_P(N,m+1) \mathsf{B} G_Q(m,0) Qs$, cuya norma es $\le e^a \frac{a}{N} \sum_{m=0}^{N-1} \rho_2^m |Qs|_* \le \frac{e^a a C_0}{(1-\rho_2)N} \|Qs\|_2 = O_W(N^{-1}) \|s\|_2$. Sumando esto con $\|(\mathbb{M}_N x)_N\|_2 \le O_W(N^{-1})\|s\|_2$ de (7) y $\|\mathsf{A}^N - R_P^N\| \le O_W(N^{-1})$, se obtiene (18): $\|Pt_N - R_P^N Ps\|_2 \le C_W N^{-1} \|s\|_2$.
  - En el bloque $Q$, el término homogéneo libre satisface $\|\mathsf{D}^N - R_Q^N\|_{* \to *} \le \sum_{j=0}^{N-1} \|\mathsf{D}^{N-1-j}\|_* \|\mathsf{D} - R_Q\|_* \|R_Q^j\|_* \le \frac{a}{N} \sum_{j=0}^{N-1} \rho_2^{N-1-j} \rho^j \le \frac{a}{(1-\rho_2)N}$ (notar que incluso evaluando por separado $\|\mathsf{D}^N\|_* + \|R_Q^N\|_* \le \rho_2^N + \rho^N$, decae exponencialmente y por tanto es $O_W(N^{-1})$). El término forzado desde $P$ en (14) de `T1`, $\sum_{k=0}^{N-1} G_Q(N,k+1) \mathsf{C} x_k$, tiene norma $\le \frac{a}{N(1-\rho_2)} \sup_k \|x_k\|_2 = O_W(N^{-1})\|s\|_2$.
  - Así, $\|Qt_N - R_Q^N Qs\|_2 \le C_W N^{-1} \|s\|_2$, completando rigurosamente $\|T^N - R^N\|_{\mathscr{H} \to \mathscr{H}} = O_W(N^{-1})$.

---

## 4. SIGNED_REDUCTION — Dictamen: `REPAIR_REQUIRED`

### Verificación de (20) y de las piezas $A_{-P}, A_{+Q}, A_{-Q}$
* La cadena (20) es exacta: $|\langle r_c, E d_{c,A}^{\mathrm{err}} \rangle| = e^{-K_* N} |\langle v_c, \mathcal{E}_N s \rangle| \le e^{-K_* N} \|v_c\|_2 \|\mathcal{E}_N\| \|s\|_2 = O_W(N^{-3} \cdot N^{-1} \cdot N^{-3} e^{-K_* N}) = O_W(N^{-7} e^{-K_* N})$.
* Para $A_{-P}$: como $s = \mathcal{F} H_\xi J f_0$ tiene soporte exclusivamente en el canal $+$, y tanto $P$ como $R$ son diagonales en el espacio de canales $\{+,-\}$, se cumple $\pi_- R_P^N P s = 0$. Por (18), $\|\pi_- P t_N\|_2 = \|\pi_- (P t_N - R_P^N P s)\|_2 \le \|P t_N - R_P^N P s\|_2 = O_W(N^{-4})$. Emparejando con $\|v_-\|_2 = O_\vartheta(N^{-3})$ de (13), resulta $|A_{-P}| \le 2 e^{-K_* N} \|v_-\|_2 \|\pi_- P t_N\|_2 = O_W(N^{-7} e^{-K_* N})$.
* Para $A_{+Q}$ y $A_{-Q}$: de (6) y (9), $\|Q t_N\|_2 \le C_W (\rho_2^N + N^{-1}) \|s\|_2 = O_W(N^{-4})$. Emparejando con $\|v_\pm\|_2 = O_\vartheta(N^{-3})$, se obtiene $|A_{\pm Q}| \le 2 e^{-K_* N} \|v_\pm\|_2 \|Q t_N\|_2 = O_W(N^{-7} e^{-K_* N})$.

### Defecto detectado en la primera línea de (21) y (22)

* **Ecuación afectada:** Primera línea de (21) y primera línea de (22) en `reports/2026-09-24--schur-stability-physical-transfer.md` (§8):
  \[
  A_{+P} = 2\operatorname{Re}\langle r_+, E S^N f_0 \rangle + O_W(N^{-7} e^{-K_* N}), \qquad
  L_+ = 2\operatorname{Re}\langle r_+, E S^N (U_M - I)\phi_N \rangle + O_W(N^{-7} e^{-K_* N}) + O_W(N^{-8} e^{-2K_* N}).
  \]
* **Contraargumento matemático (reconstrucción exacta del término libre $Q$):**  
  Por definición en `T1` (8) y (10a), $A_{+P} = 2 e^{-K_* N} \operatorname{Re}\langle v_+, P t_N \rangle$. Sustituyendo (18), $P t_N = R_P^N P s + O_W(N^{-4})$, junto con $\|v_+\|_2 = O_\vartheta(N^{-3})$, se obtiene legítimamente:
  \[
  A_{+P} = 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_P^N P s \rangle + O_W(N^{-7} e^{-K_* N}).
  \]
  Por otro lado, por (7) de `T1` aplicada a la evolución libre ($\vartheta = 0 \implies U_N = D, T = R$), como $s = \mathcal{F} H_\xi J f_0$ está en el canal $+$, se tiene la identidad exacta:
  \[
  \mathbf{1}_{\mathcal{B}_N} S^N f_0 = \mathbf{1}_{\mathcal{B}_N} \pi_+ D^N J f_0 = e^{-K_* N} \mathcal{V}_+ R^N s = e^{-K_* N} \mathcal{V}_+ R_P^N P s + e^{-K_* N} \mathcal{V}_+ R_Q^N Q s.
  \]
  Por tanto, la diferencia entre el funcional escrito en (21) y el término principal libre en $P$ es exactamente la contribución libre en $Q$:
  \[
  2\operatorname{Re}\langle r_+, E S^N f_0 \rangle - 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_P^N P s \rangle = 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_Q^N Q s \rangle.
  \]
  El autor afirma en §8 que *"El Q libre terminal es exponencialmente pequeño por (4)"* y usa esto para absorber $2 e^{-K_* N} \operatorname{Re}\langle v_+, R_Q^N Q s \rangle$ dentro de $O_W(N^{-7} e^{-K_* N})$. Sin embargo, de (4), (9) y (13), la única cota demostrada para ese término es:
  \[
  \bigl| 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_Q^N Q s \rangle \bigr| \le 2 e^{-K_* N} \|v_+\|_2 \|R_Q^N Q s\|_2 \le C_W C_0 N^{-6} \rho^N e^{-K_* N}.
  \]
  Aunque $\rho^N$ es exponencialmente pequeño frente a $N^{-1}$ cuando $N \to \infty$ (es decir, $\rho^N = o_W(N^{-1})$), **no existe una constante $C_W$ independiente de $N$ tal que $\rho^N \le C_W N^{-1}$ para todo $N \ge 2$** salvo que esa constante absorba el umbral donde $\rho^N$ cae por debajo de $N^{-1}$. Pero en (4), $\rho \in (r_0(W), 1)$ depende de $W$, y si la notación $O_W(\cdot)$ se aplica para todo $N$ o si se compara con la tasa exponencial $e^{-K_* N}$, reemplazar $R_P^N P s$ por $R^N s$ (que reintroduce el exterior $W^c$ y la rama subdominante en $W$) mezcla el funcional proyectado en $P$ con el propagador completo $S^N$ a través de un error $O_W(N^{-6} \rho^N e^{-K_* N})$. Más importante aún desde el punto de vista estructural del contrato `T1`/`T2`: `T1` introdujo $P$ y $Q$ precisamente para aislar la rama dominante en las ventanas $W$; si al final de (21) se vuelve a sumar $R_Q^N Q s$ para escribir $\langle r_+, E S^N f_0 \rangle$, la expresión final de (21)–(22) ya no contiene $P$ ni $W$ en su término principal, mientras que el resto $O_W(N^{-7} e^{-K_* N})$ sí depende de $W$ (porque absorber $\rho(W)^N \le C_W N^{-1}$ hace que la constante implícita en $O_W(N^{-7})$ explote exponencialmente cuando $\partial W$ se acerca a $\Sigma$ y $1-\rho(W) \to 0$).
* **Condición de cierre:** En (21) y (22) (y en la línea intermedia previa a (15) donde se dice *"Se ha absorbido $\rho_2^N$ en $O(N^{-1})$"*), el autor debe hacer una de las dos reparaciones siguientes (o ambas explícitamente):
  1. Conservar explícitamente la forma proyectada $2 e^{-K_* N} \operatorname{Re}\langle v_+, R_P^N P s \rangle$ en (21), o bien escribir el término libre de $Q$ separado como $+ O_W(N^{-6} \rho^N e^{-K_* N})$ antes de absorberlo.
  2. Si se absorbe $\rho^N$ (y $\rho_2^N$) dentro de $C_W N^{-1}$ para pasar a $2\operatorname{Re}\langle r_+, E S^N f_0 \rangle$, declarar explícitamente en el texto de (15) y (21)–(22) que dicha absorción utiliza $\sup_{N \ge 2} N \rho(W)^N \le \frac{1}{e |\log \rho(W)|} < \infty$ para $W$ fijo, haciendo constar que el término principal escrito $2\operatorname{Re}\langle r_+, E S^N f_0 \rangle$ es formalmente independiente de $W$ sólo porque la contribución de $W^c$ ha sido volcada en la constante dependiente de $W$ del resto $O_W(N^{-7} e^{-K_* N})$.

---

## 5. CLAIM_CEILING — Dictamen: `PASS`

### Auditoría de alcance, cuantificadores y techo de las afirmaciones
* **Separación entre hipótesis B y F:** El informe distingue con total rigor qué se obtiene bajo $B$ ($\|\vartheta\|_\infty \le b < \infty$) y qué requiere $F$ ($a_0, a_1 < \infty$ en (2)). Bajo $B$ sólo se obtienen la estabilidad de Schur en §2 y las cotas gruesas $|A_{cP}| = O_W(N^{-4} e^{-K_* N})$, $|A_{cQ}| = O_W(N^{-5} e^{-K_* N})$ y $B_{cAB} = O_W(N^{-8} e^{-2K_* N})$ en §5 (usando $\|r_c\|_2 \le 1$). Tanto la cota puntual de Bob (11),(13) ($a_0 < \infty$) como el conmutador de transporte (16)–(19) ($a_1 < \infty$) dependen de $F$, y el informe señala expresamente en §1 y §9 que $F$ no se deduce de $B$ ni de ser meramente $C^1$.
* **Cuantificadores e independencia en $N$ pero no en $W$/perfil:** No se elige $W = W_N$ ni se exige un perfil numérico para las pruebas analíticas: los cuantificadores están bien ordenados (se fija $W$ admisible y $\vartheta \in F$, y las constantes $C_W, O_W, O_\vartheta$ son independientes de $N$).
* **Subordinación absoluta frente a líder firmado no nulo:** El informe respeta estrictamente el techo del resultado:
  - Demuestra que el error del puente hacia el funcional libre con referencia actual es absolutamente $O_W(N^{-7} e^{-K_* N})$, que es $o(N^{-13/2} e^{-K_* N})$ en comparación con la escala del protocolo plano de `ir-corona.tex`.
  - Declara explícitamente en §7, §8 y §9 que esto **no** demuestra que el nuevo funcional $2\operatorname{Re}\langle r_+, E S^N (U_M - I)\phi_N \rangle$ tenga orden $N^{-13/2} e^{-K_* N}$, ni fija su signo, ni excluye que se anule o sufra cancelaciones para un perfil $\vartheta \ne 0$.
  - No promueve `H1`/`H1c`, `POWER_13/2_STABILITY`, `E0` ni `AdS`, ni presenta la subordinación de Schur como novedad conceptual.
* **Controles límite:** El caso $\vartheta = 0$ ($T=R, r_-=0, L_-=0, L_+ = L_{\mathrm{plano}}$) y el control de fuente nula ($U_{\mathrm{enc}} = I \implies f=s=0$, distinguiéndolo correctamente del encoder congelado $M=I$ donde $U_I = e^{i\pi F_N/2}I \ne I$) son exactos y consistentes con `T1` e `ir-corona.tex`.
