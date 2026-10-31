<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 f6f5552b7b6ad013f3a8d5b7ded4d0fc9729be54e1f370eb30233f11011fcd91
inicio: 2026-10-31T17:45:40Z  fin: 2026-10-31T17:46:29Z
documento: /home/adnac/qca-causal-cones/reports/2026-09-24--schur-stability-physical-transfer.md ; último commit observado: 72e6daa (con cambios sin commit) ; sha256 de la copia enviada caee6fa254fd83d64ac16ce6de2f04b359087e9a8f1668b0d4f93a089589bf65
documento: /home/adnac/qca-causal-cones/reports/2026-09-24--two-channel-t1-exact-signed-pq.md ; último commit observado: 7f68fa7 ; sha256 de la copia enviada c320aaa5060f343f1f0e726f663058f62fb6c1d2f19f71da43ef4bd759e24e8d
documento: /home/adnac/qca-causal-cones/papers/ir-corona/ir-corona.tex ; último commit observado: 3a44725 ; sha256 de la copia enviada a3849451dbac2d3e3a68ace47b0b50ae2bbf5ae3f6902c8bc92b9c2d820a42c5
documento: /home/adnac/qca-causal-cones/debates/2026-10-31--schur-physical-bridge-review/informe_gemini.md ; último commit observado: sin versionar ; sha256 de la copia enviada 4eb9c78947c93dc0a3d8c477b4a8e1486cc8afde47dd5b86fcb4f2bf911f0834
documento: /home/adnac/qca-causal-cones/reports/2026-10-31--schur-physical-bridge-review-disposition.md ; último commit observado: sin versionar ; sha256 de la copia enviada ecaed9a3a79a88e8f6f14cc24d9970ae1b6ec2ca982e572bc39d62d001fe9017
entrada_gemini.txt sha256 4b2370734e6a08e58c12b9a93d4e3e441d31324c363d890be2ead9d0e2d13aae
respuesta sha256 f7da119311bbc340c0647ad9bc015f43df034fce690aa6c1500210a79187dae4
-->

# Verificación de las aclaraciones del puente Schur y cierre acotado

**Expediente examinado:** `2026-09-24--schur-stability-physical-transfer.md` (con aclaraciones incorporadas), `2026-09-24--two-channel-t1-exact-signed-pq.md` (`T1`), `ir-corona.tex`, `informe_gemini.md` y `2026-10-31--schur-physical-bridge-review-disposition.md`.

---

## Resumen de Dictámenes

* **Punto 1 (Absorción de $\rho(W)^N$ en $C(W)/N$):** `PASS`
* **Punto 2 (Identidad de reconstrucción libre $P+Q$, absorción de $Q$ libre y alcance de (21)–(22)):** `PASS`
* **Punto 3 (Cota interior de la raíz subdominante en $W$ bajo hipótesis de T1):** `PASS`
* **Punto 4 (Estabilidad de hipótesis y validez de los cuatro bloques previos):** `PASS`
* **Gate `SIGNED_REDUCTION`:** `PASS`

---

## 1. Recálculo desde cero de $\rho(W)^N \le C(W)/N$ para $0 < \rho(W) < 1$ fijo — Dictamen: `PASS`

Sea $r = \rho(W) \in (0,1)$ un número real fijo (dependiente de la ventana fija $W$, y en el caso de $\rho_2$, también del perfil fijo $\vartheta$). Queremos determinar si existe una constante $C(r) < \infty$, independiente de $N$, tal que para todo entero $N \ge 1$ (y en particular $N \ge 2$):
\[
r^N \le \frac{C(r)}{N} \iff N r^N \le C(r).
\]

**Cálculo directo (vía continua):**  
Sea $a = -\log r = |\log r| > 0$. Consideremos $g(x) = x e^{-a x}$ en $[0, \infty)$. Esta función es continua, no negativa, satisface $g(0)=0$, $\lim_{x\to\infty} g(x) = 0$, y su derivada es:
\[
g'(x) = (1 - a x) e^{-a x}.
\]
El único punto crítico es $x_* = 1/a > 0$, donde $g$ alcanza su máximo global estricto:
\[
\sup_{N \ge 1} N r^N \le \sup_{x \ge 0} x e^{-a x} = g(1/a) = \frac{1}{e a} = \frac{1}{e |\log \rho(W)|} < \infty.
\]

**Cálculo directo alternativo (vía serie geométrica):**  
Como todos los términos de la serie $\sum_{n=1}^\infty n r^n$ son positivos para $r \in (0,1)$, para cualquier $N \ge 1$ un solo sumando es menor que la suma total:
\[
N r^N \le \sum_{n=1}^\infty n r^n = \frac{r}{(1-r)^2} < \infty.
\]

**Evaluación crítica de la objeción de la revisión anterior:**  
La afirmación contenida en `informe_gemini.md` (§4) de que *"no existe una constante $C_W$ independiente de $N$ tal que $\rho^N \le C_W N^{-1}$ para todo $N \ge 2$"* es matemáticamente falsa. Para cualquier $\rho(W) \in (0,1)$ fijo, el supremo en $N \ge 2$ es finito y está explícitamente acotado por $\frac{1}{e|\log \rho(W)|}$. El hecho de que dicha constante diverja si $\rho(W) \to 1^-$ (cuando $W$ se encoge o se acerca al exterior sin hueco) refleja simplemente su dependencia en $W$, la cual está expresamente permitida por la notación $O_W(\cdot)$ y por el contrato de `T1` (§2: $W$ se fija una sola vez, independiente de $N$, sin prometer uniformidad en $W$). Por tanto, se retira íntegramente esa objeción. Las ecuaciones (15) y la previa a (21) del documento aclarado son exactas.

---

## 2. Identidad de reconstrucción libre $P+Q$ y ecuaciones (21)–(22) — Dictamen: `PASS`

**Comprobación de la identidad exacta antes de (21) con Bob físico actual:**  
En el documento aclarado (§8), con $f_0 = (U_M - I)\phi_N$, $f = J f_0 = (f_0, 0)$ y $s = \mathcal{F} H_\xi f$, consideremos la evolución libre ($\vartheta = 0$). Allí $U_N$ se reduce a $D = S \oplus S^{-1}$ y el operador inclinado $T$ se reduce a $R = \Lambda^{-1} D_\xi$. Aplicando la identidad exacta (5) y (7) de `T1` al paso libre $D^N$:
\[
\mathbf{1}_{\mathcal{B}_N} D^N f = e^{-K_* N} \mathcal{V} R^N s.
\]
Como $f = (f_0, 0)$ sólo tiene componente en el canal $+$, y $D = S \oplus S^{-1}$ es diagonal en canales, $\pi_+ D^N f = S^N f_0$. Proyectando en el canal $+$ (con $\mathcal{V}_+ = \pi_+ \mathcal{V}$):
\[
\mathbf{1}_{\mathcal{B}_N} S^N f_0 = e^{-K_* N} \mathcal{V}_+ R^N s.
\]
Usando que $P + Q = I$ en $\mathscr{H} = L^2(\mathbb{T}^3; \mathbb{C}^4)$ y que $R$ conmuta fibra a fibra con $P$ y $Q$ ($R^N = R^N P + R^N Q = R_P^N P + R_Q^N Q$), obtenemos:
\[
\mathbf{1}_{\mathcal{B}_N} S^N f_0 = e^{-K_* N} \mathcal{V}_+ R_P^N P s + e^{-K_* N} \mathcal{V}_+ R_Q^N Q s.
\]
Emparejando esta identidad en el producto interno con el extremo físico actual de Bob, $r_+ = \mathbf{1}_{\mathcal{B}_N} \pi_+ U_N^N J\phi_N$ (que incluye la evolución completa con moneda $\vartheta \ne 0$), y recordando de (12) que $v_+ = \mathcal{V}_+^* E r_+$ y $E = \mathbf{1}_{\mathcal{B}_N} E \mathbf{1}_{\mathcal{B}_N}$ está soportado en $\mathcal{B}_N$, resulta exactamente:
\[
\begin{aligned}
2\operatorname{Re}\langle r_+, E S^N f_0 \rangle 
&= 2\operatorname{Re}\langle r_+, E \mathbf{1}_{\mathcal{B}_N} S^N f_0 \rangle \\
&= 2 e^{-K_* N} \operatorname{Re}\langle r_+, E \mathcal{V}_+ R_P^N P s \rangle + 2 e^{-K_* N} \operatorname{Re}\langle r_+, E \mathcal{V}_+ R_Q^N Q s \rangle \\
&= 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_P^N P s \rangle + 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_Q^N Q s \rangle.
\end{aligned}
\]
La identidad añadida en §8 es algebraicamente exacta y mantiene $r_+$ sin sustituirlo por la cola libre plana.

**Absorción del término $Q$ libre y alcance de (21)–(22):**  
Bajo la hipótesis **F**, tenemos $\|v_+\|_2 = O_\vartheta(N^{-3})$ por (13), $\|s\|_2 = O(N^{-3})$ por (9), $\|Q\|_{L^2\to L^2} \le C_P(W)$ por `T1` (3a), y $\|R_Q^N\|_{L^2\to L^2} \le C_0(W) \rho(W)^N$ por (4). Por Cauchy–Schwarz:
\[
\bigl| 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_Q^N Q s \rangle \bigr| 
\le 2 e^{-K_* N} \|v_+\|_2 \|R_Q^N\| \|Q\| \|s\|_2 
\le C_{W,\vartheta} N^{-6} \rho(W)^N e^{-K_* N}.
\]
Por el Punto 1, $\rho(W)^N \le \frac{1}{e|\log \rho(W)|} N^{-1}$, luego este término es $O_{W,\vartheta}(N^{-7} e^{-K_* N})$.  
Por otro lado, de (18), $\|P t_N - R_P^N P s\|_2 \le C_W N^{-1} \|s\|_2 = O_W(N^{-4})$, por lo que:
\[
\bigl| A_{+P} - 2 e^{-K_* N} \operatorname{Re}\langle v_+, R_P^N P s \rangle \bigr| 
= \bigl| 2 e^{-K_* N} \operatorname{Re}\langle v_+, P t_N - R_P^N P s \rangle \bigr| 
\le 2 e^{-K_* N} \|v_+\|_2 \|P t_N - R_P^N P s\|_2 = O_{W,\vartheta}(N^{-7} e^{-K_* N}).
\]
Restando la identidad de reconstrucción libre se obtiene la primera línea de (21):
\[
A_{+P} = 2\operatorname{Re}\langle r_+, E S^N f_0 \rangle + O_W(N^{-7} e^{-K_* N}).
\]
Las cotas $A_{+Q}, A_{-P}, A_{-Q} = O_W(N^{-7} e^{-K_* N})$ en (21) y la descomposición completa de $L_\pm$ en (22) (sumando las tres piezas cuadráticas $B_{cPP} + B_{cQQ} + B_{cPQ} = O_W(N^{-8} e^{-2K_* N})$ de la tabla de §5) conservan plenamente su validez y su alcance declarado.

---

## 3. Corrección de la cota interior de la raíz subdominante en $W$ — Dictamen: `PASS`

**Error en el informe previo:**  
En `informe_gemini.md` (§1) se escribió: *"donde $|\lambda(p)^{-1}|/\Lambda \le \Lambda^{-2} < 1$"*, intentando deducirlo de $|\lambda(p)| \le \Lambda$. Esa deducción es incorrecta porque la inversión invierte el sentido de la desigualdad:
\[
|\lambda(p)| \le \Lambda \implies |\lambda(p)|^{-1} \ge \Lambda^{-1} \implies \frac{|\lambda(p)|^{-1}}{\Lambda} \ge \Lambda^{-2}.
\]
De hecho, la igualdad $|\lambda(p)|^{-1}/\Lambda = \Lambda^{-2}$ sólo se alcanza en los saddles $p \in \Sigma$, donde $|\lambda(p)| = \Lambda$ es máximo, y crece a medida que $p$ se aleja del saddle dentro de $W$.

**Verificación de separación uniforme usando las hipótesis efectivas de T1:**  
En `T1` (§2), las ventanas admisibles $W = \bigcup_{\alpha \in \Sigma} W_\alpha$ se definen exigiendo que $\overline{W_\alpha} \subset O_\alpha$, donde en cada $O_\alpha$ existe una rama continua dominante $\lambda_\alpha(p)$ con $|\lambda_\alpha(p)| > 1$ en todo $O_\alpha$.  
Como cada cierre $\overline{W_\alpha}$ es compacto y $|\lambda_\alpha(p)|$ es continua en $\overline{W_\alpha}$, alcanza su mínimo en $\overline{W_\alpha}$, y al haber ocho ventanas:
\[
\underline{\lambda}(W) := \min_{\alpha \in \Sigma} \min_{p \in \overline{W_\alpha}} |\lambda_\alpha(p)| > 1.
\]
Además, sabemos que $\Lambda = e^{\Phi_*} = \cosh^3 t_* + \sqrt{\cosh^6 t_* - 1} > 1$ (en `ir-corona.tex`, Lema 6.1(a), $\Lambda \approx 3.973 > 1$).  
En $\operatorname{Ran} Q(p)$ para $p \in W$, el operador $R(p) = \Lambda^{-1} D_\xi(p)$ actúa como multiplicación escalar por $\lambda(p)^{-1}/\Lambda$ (ya que en el primer bloque $S(p-i\xi_*)$ restringido a $I_2 - p_S(p)$ tiene autovalor $\lambda(p)^{-1}$, y en el segundo bloque $S(p-i\xi_*)^{-1}$ restringido a $p_S(p)$ tiene autovalor $\lambda(p)^{-1}$). Por tanto, para todo $p \in W$:
\[
\frac{|\lambda(p)|^{-1}}{\Lambda} \le \frac{1}{\Lambda\,\underline{\lambda}(W)} < \frac{1}{\Lambda} < 1.
\]
Incluso usando únicamente $|\lambda(p)| > 1$ en $\overline{W}$ y $\Lambda > 1$, la raíz subdominante está uniformemente acotada por $\frac{1}{\Lambda \underline{\lambda}(W)} < 1$. Así, la afirmación del documento de Codex en §2 (*"En Ran Q dentro de W la raíz es $\lambda^{-1}/\Lambda$, uniformemente menor que uno"*) es completamente cierta bajo las hipótesis efectivas de `T1`. Tomando $\rho \in (\max(r_0(W), (\Lambda \underline{\lambda}(W))^{-1}), 1)$, la cota $\|R_Q^h\| \le C_0 \rho^h$ de (4) queda rigurosamente establecida.

---

## 4. Impacto de las aclaraciones sobre las hipótesis y los cuatro bloques previos — Dictamen: `PASS`

Examinamos críticamente si las adiciones en `2026-09-24--schur-stability-physical-transfer.md` alteran las hipótesis o invalidan alguno de los bloques:

1. **Hipótesis B y F (§1):** Inalteradas. **B** sigue siendo $b = \|\vartheta\|_\infty < \infty$, y **F** sigue siendo $a_0, a_1 < \infty$ en (2).
2. **`SCHUR_STABILITY` (§2, Ecs. 3–7):** Inalterado en el documento de Codex. Con la corrección del Punto 3 anterior, la prueba de (3)–(7) bajo **B** es sólida: $\rho(R(p)) \le 1$, $\|R_Q^h\| \le C_0 \rho^h$, la norma adaptada $|\cdot|_*$ controla la no normalidad en $W^c$, y tanto la recurrencia acoplada como Duhamel–Gronwall discreto y la suma doble de Schur (7) son exactas.
3. **`PHYSICAL_ENDPOINTS` (§3–§5, Ecs. 8–15):** La única adición es explicitar en (15) la desigualdad $\sup_{N\ge 2} N r^N \le \frac{1}{e|\log r|} < \infty$ para absorber $\rho_2^N$ en $O_W(N^{-1})$. Como se verificó en el Punto 1, esto no introduce ninguna hipótesis nueva y valida las cotas $\|P t_N\| = O_W(N^{-3})$, $\|Q t_N\| = O_W(N^{-4})$ bajo **B**, así como $\|s\|_2 = O(N^{-3})$, $\|v_c\|_2 = O_\vartheta(N^{-3})$ bajo **F**, y la tabla de las diez piezas de `T1` (10a).
4. **`PROPAGATOR_ERROR` (§6, Ecs. 16–19):** Inalterado. Bajo **F**, la identidad $\beta P(p) = Q(p)\beta$ en $W$ (`T1` (3b)) y la anulación idéntica de $P(p')\beta P(p)$ cuando $p \notin W$ o $p' \notin W$ evitan derivar el salto de $P$ en $\partial W$. La cota Lipschitz en $W$ junto con el momento $a_1 < \infty$ de $\mu_N$ dan $\|\mathsf{A} - R_P\| \le C_W/N^2$ y $\|T^N - R^N\| = O_W(N^{-1})$.
5. **`CLAIM_CEILING` (§7–§9):** Las aclaraciones en §8 refuerzan el techo: se explicita que el funcional libre completo $2\operatorname{Re}\langle r_+, E S^N f_0 \rangle$ no depende de $W$, pero que su comparación con $A_{+P}$ tiene constantes dependientes de $W$ y del perfil, por lo que no permite tomar $W = W_N$. Se mantiene intacta la advertencia de que $O_W(N^{-7} e^{-K_* N})$ es una cota absoluta de error y no certifica que el término principal sea no nulo ni de orden $N^{-13/2} e^{-K_* N}$.

---

## Conclusión de Cierre Acotado vs. Revisión Integral

* **Estado de reparaciones obligatorias:** **No queda ninguna reparación obligatoria pendiente** para el puente Schur → extremos físicos → cuatro términos lineales bajo las hipótesis **B/F** y ventana admisible $W$ fija. El gate `SIGNED_REDUCTION` pasa a `PASS`.
* **Diferenciación de alcance:** Este dictamen constituye la **verificación y cierre acotado** de las aclaraciones aplicadas a `2026-09-24--schur-stability-physical-transfer.md` y la corrección de los dos errores del informe de revisión previo (`informe_gemini.md`), confirmando la solidez de los cinco bloques del puente hasta las ecuaciones (21)–(22). Este cierre acotado **no** certifica un líder asintótico firmado no nulo para $\vartheta \ne 0$, no evalúa la evolución asintótica de la referencia inhomogénea $r_+ = \mathbf{1}_{\mathcal{B}_N} \pi_+ U_N^N J\phi_N$, no abre ni promueve `H1`/`H1c`, `POWER_13/2_STABILITY`, `E0` ni `AdS`, y no sustituye una revisión integral independiente de futuros desarrollos (como `T3`).
