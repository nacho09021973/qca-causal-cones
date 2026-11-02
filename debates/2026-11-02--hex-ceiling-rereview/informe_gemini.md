<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 7b9720b2995bdec0941415c9aca817a58ab5b120364c5a0dc7c8c0c5c0854209
inicio: 2026-11-02T08:42:26Z  fin: 2026-11-02T08:42:49Z
documento: /home/adnac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--hex-ceiling-review.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada b6daf1a7ad96c09eba521a63383a8015256bd9a6181fe056a90a981cc5bf4460
documento: /home/adnac/qca-causal-cones/debates/2026-11-02--hex-ceiling-rereview/repair.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 73fc9964e29b57f42ec9aa377cb5b73130fe73fcc368970a58fd6ae277e775fa
documento: /home/adnac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/adnac/qca-causal-cones/scripts/verify_hex_ceiling_gate.py ; último commit observado: bb4fcdb ; sha256 de la copia enviada 8f3b7a10ecee91c515429640b794da91e2c0e273176f5bbbd62e56a0f3b43d72
documento: /home/adnac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
entrada_gemini.txt sha256 474062a1d9ba3c2146bd149993ed5810c95245226c70e5055d2ce49e314aaef0
respuesta sha256 c5154c770e2b7cb29ccf2f980d5ebcc2e6fc1c656c9033b5dfa2c80ffc220ef5
-->

### Dictamen por punto

**R1. Lema B y cierre de L0: PASS**
La prueba de la desigualdad de Bernstein escalar en el Lema B es completa y rigurosa:
- **Reducción al caso real:** Al elegir $\alpha$ tal que $e^{i\alpha} p'(s_0) = |p'(s_0)|$, la función $R(s) = \operatorname{Re}(e^{i\alpha} p(s)) = \frac{1}{2}(e^{i\alpha} p(s) + e^{-i\alpha} \overline{p(s)})$ es un polinomio trigonométrico real de grado $\le N$, acotado por $|R(s)| \le |p(s)| \le 1$, y cumple $R'(s_0) = |p'(s_0)|$.
- **Perturbación y elección de fase:** Si $R'(s_0) > N$, para $\varepsilon \in (0,1)$ suficientemente pequeño, $R_\varepsilon = (1-\varepsilon)R$ mantiene $R_\varepsilon'(s_0) > N$ y garantiza $|R_\varepsilon(s)| \le 1-\varepsilon < 1$ en todo $\mathbb{R}$. Esto permite elegir de forma única $\beta \in (-\pi, 0)$ tal que $\cos\beta = R_\varepsilon(s_0)$, con $\sin\beta < 0$.
- **Comparación y recuento de ceros:** Para $C(s) = \cos(N(s-s_0)+\beta)$, se tiene $C(s_0) = R_\varepsilon(s_0)$ y $C'(s_0) = -N\sin\beta \in (0, N]$. Por tanto, la diferencia $D = C - R_\varepsilon$ verifica $D(s_0) = 0$ y $D'(s_0) = C'(s_0) - R_\varepsilon'(s_0) < 0$. En un periodo $[0, 2\pi)$ (para $N \ge 1$; el caso $N=0$ es trivial pues $R'=0$), $C(s)$ alcanza los valores extremos $\pm 1$ alternadamente en $2N$ puntos $t_1 < t_2 < \dots < t_{2N}$. Como $|R_\varepsilon(t_j)| < 1$, el signo de $D(t_j)$ coincide con el de $C(t_j)$ y alterna entre puntos consecutivos. Esto garantiza al menos un cero en cada uno de los $2N$ arcos abiertos $(t_j, t_{j+1})$ (con $t_{2N+1} = t_1 + 2\pi$). Como $D(s_0) = 0 \ne D(t_j)$ y $C'(s_0) > 0$, $s_0$ pertenece al interior de un arco $(t_j, t_{j+1})$ donde $C$ es estrictamente creciente, es decir, $C(t_j) = -1$ y $C(t_{j+1}) = +1$, luego $D(t_j) < 0 < D(t_{j+1})$. Dado que $D(s_0) = 0$ y $D'(s_0) < 0$, se tiene $D(s) > 0$ inmediatamente a la izquierda de $s_0$ y $D(s) < 0$ inmediatamente a su derecha; por el teorema del valor intermedio, existen al menos un cero en $(t_j, s_0)$ y otro en $(s_0, t_{j+1})$, sumando al menos tres ceros distintos en dicho arco y al menos $2N+2$ ceros simples/distintos en el periodo.
- **Contradicción algebraica y simetría:** En la variable $z = e^{is}$ sobre el círculo unidad, $e^{iNs} D(s)$ es un polinomio algebraico no nulo de grado $\le 2N$, que puede tener a lo sumo $2N$ raíces en $|z|=1$. La contradicción prueba $R'(s_0) \le N$, y aplicar el resultado a $R(-s)$ da $R'(s_0) \ge -N$.
- **Cumplimiento del contrato:** Esto cierra formalmente L0 como `PROVED_IN_REPO` en estricto cumplimiento de la Sección 2 de `HEX_CEILING_GATE.md`.

**R2. Certificación del rango en T1: PASS**
En `verify_hex_ceiling_gate.py`, el cálculo del menor $2\times 2$ de las dos primeras columnas de la matriz jacobiana `jac` (`minor = sp.simplify(sp.expand_trig(jac[:, :2].det()))`) se compara simbólicamente contra $\frac{\sqrt{3}}{2}\ell^4$ mediante `sp.simplify(minor - R3 * ell ** 4 / 2) == 0`. Al ser $\ell > 0$, esta constante es estrictamente distinta de cero e independiente del ángulo de orientación $\theta_0$. Esto certifica de manera exacta que la matriz de coeficientes $2\times 3$ tiene rango 2 para todo $\theta_0$, por lo que su núcleo es de dimensión 1 (generado por $(1,1,1)$). El texto del informe refleja fielmente este hecho.

**R3. Aclaraciones incorporadas: PASS**
Las cuatro aclaraciones se han integrado con precisión matemática:
1. **Hermiticidad de $A(n_f)$ en L0:** Se demuestra diferenciando $U(t)U(t)^\dagger = I$ en $t=0$ con $U(0)=I$, lo que implica que $\frac{dU}{dt}(0)$ es antihermítica y $A(n_f) = i\frac{dU}{dt}(0)$ es hermítica. Esto justifica rigurosamente que $A(n_f)^2 = c_0^2 I$ implique espectro $\{\pm c_0\}$ y norma de operador $\|A(n_f)\| = c_0$.
2. **Principio del módulo máximo en T2:** Se explicita que $P(z) = z^N p(s)$ (con $z=e^{is}$) es un polinomio analítico que cumple $|P(z)| = |p(s)| \le 1$ en la circunferencia unidad $|z|=1$, de donde se sigue $|P(z)| \le 1$ en todo el disco cerrado $|z|\le 1$ por el principio del módulo máximo antes de invocar el lema de Julia.
3. **El hexágono fija el denominador $2\ell$:** Se aclara en T1 que la condición de soporte hexagonal obliga a que los seis vértices $\pm 2a_j$ estén en $F$, fijando el paso más largo en $2\ell$ (el denominador de normalización de $c_0$), sin restringir el supremo ya que $g = -1/2$ realiza los seis vértices.
4. **$\xi$ como componente de Bloch:** Se corrige la redacción indicando que los ejes de ADMP comparten la componente $z$ de Bloch $\xi = \sqrt{5}/3$ (en lugar de describir $\xi$ como un ángulo de inclinación), lo que eleva el solapamiento a $g = 1/3$.

**R4. Regresiones y alcance: PASS**
El diff es limpio y acotado a las reparaciones solicitadas. No introduce errores algebraicos ni afirmaciones que excedan el alcance del contrato congelado `HEX_CEILING_GATE.md`. (Como observación menor no bloqueante, el comentario en la docstring inicial de `verify_hex_ceiling_gate.py` aún menciona que Bernstein es *prior art* aplicado en el informe, lo cual sigue siendo cierto aunque ahora además esté demostrado en el Lema B del informe).

---

### Dictamen global

**PASS**. No hay reparaciones obligatorias pendientes.
