<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=medium, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 8376713a45254b68dd8d953a278ca2f4c2898037f267040a9563f2d2e4c9b026
inicio: 2026-11-03T11:18:33Z  fin: 2026-11-03T11:19:22Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--c-across-substrates-answer.md ; último commit observado: 99771c0 ; sha256 de la copia enviada 21cb74e83679d2d9c546ee830cef4828975d27deba5785b591c191853e64f0cc
documento: /home/ignac/qca-causal-cones/state/CURRENT_STATE.md ; último commit observado: 56f6831 ; sha256 de la copia enviada b8e55e2b4aa0acc094c879b3feacbaba888a2fb6f286b097448d6a1c6d067edf
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--l6b-triangular-row.md ; último commit observado: a19e480 ; sha256 de la copia enviada 201a62e186976639dc351da55355820b8327dff971e0badd53a58ed9835afe4c
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices.md ; último commit observado: 70dd98c ; sha256 de la copia enviada 5aaaea6af9704abb2a1a16613f1ede7fc1639956800e66d2580824484b31bec9
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--c-across-lattices.md ; último commit observado: 8d0276e ; sha256 de la copia enviada 01a18c70a1b031e99ca4f944c9f6810f29b1327067138c8eb3ee089deca1ea3f
entrada_gemini.txt sha256 7ebd297fc0e62ae5068640511d79bb77e595975725f3ff2683407eecc4c521a9
respuesta sha256 92e4b597c3a981c8489e88fa0ed4c11d4ef7a5675d894fc970cbd34811c22c78
-->

Revisión adversarial e independiente de `2026-11-02--c-across-substrates-answer.md` frente a `CURRENT_STATE.md` (CS) y los cuatro informes de ejecución adjuntos.

---

### Dictámenes por bloque

#### 1. TRAZABILIDAD: **PASS**
Todas las afirmaciones de las Secs. 0–3 se rastrean exactamente a las secciones citadas de CS o de los cuatro informes adjuntos, con los mismos valores numéricos y algebraicos:
- **Sec. 0:**
  - Punto 1: `L3s4` con $c_0 = a/\sqrt{3}$ para $0 < a < 1$ está en CS Sec. 4.1. `ADMP L6a` ($c_0 = 1/2$) y `JDW L6d` ($c_0 = 3/4$) sobre el mismo sustrato hexagonal están en CS Sec. 11 y `c-across-lattices` Secs. 3–4. La fila `L6b` ($s=6$, $c_0 = 1/3$) está en CS (entrada de promoción de `L6B_TRIANGULAR_ROW` y Sec. 11) y en `l6b-triangular-row` Sec. 1.
  - Punto 2: $c_{\text{strict}}^{\text{iso}} \le r_{\text{in}}(C_{\text{micro}})$ en general (CS Secs. 4, 6, 7.2 dir. 1); $c_0 \le c_{\text{strict}}^{\text{iso}}$ probado en $N_3$ bajo el contrato congelado del punto (3) (CS Sec. 7.2) y confirmado fila por fila en el resto de filas declaradas (CS Sec. 11, `c-across-lattices` Secs. 4, 6 y `l6b-triangular-row` Sec. 1).
  - Punto 3: Saturación en línea, cuadrado, BCC estándar y cubo (CS Secs. 4, 5, 8, 11); no saturación de `L3s4` en BCC (CS Sec. 4.1); ninguna de las cinco caminatas hexagonales declaradas alcanza $r_{\text{in}}$ (CS Sec. 11 y `l6b-triangular-row`); supremo $\sqrt{3}/2$ en la subclase antipodal $n=3$ y no saturación para $s=2$ con soporte mínimo $F \subseteq \{0\} \cup \operatorname{vert}(H)$, quedando el resto de $W_{\text{hex}}$ `OPEN` y nada afirmado para $s>2$ (CS Sec. 12 y `hex-ceiling` Secs. 2, 3, 5).
  - Punto 4: `NO_ABSOLUTE_SCALE_DERIVABLE` en la clase plana congelada (CS Sec. 8.21 y resumen de estado).
- **Sec. 1:** Todos los valores de la tabla y las cinco lecturas (*readings*) están en CS Secs. 4, 4.1, 5, 8, 11, `c-across-lattices` Sec. 4, `l6b-triangular-row` Secs. 1 y 4, y `hex-ceiling` Sec. 2 (T1).
- **Sec. 2:** Todos los resultados y etiquetas de estado coinciden con CS Secs. 4, 4.1, 7.2, 11, 12 y los informes `hex-ceiling` y `l6b-triangular-row`.
- **Sec. 3:**
  - *Dispersion:* La forma de la expansión, la condición exacta de aparición del término impar $\beta$ en las seis filas cuyo grupo carece de inversión (`L5a, L5b, L4, L6a, L6b, L3s4`), la linealidad exacta de `L1`, el signo $\alpha_0 < 0$ salvo en `L1` y en `L3s4` para $0 < a < a_* = \sqrt{3}\sqrt{17-\sqrt{154}}/9$, y $V_{\text{grp}}^{\max}$ `OPEN` están en CS Sec. 13 y `dispersion-corrections-across-lattices` Secs. 1, 3.1, 3.3, 3.5. La fórmula de la velocidad de grupo cerca del nodo $|\nabla \varepsilon_+| = c_0(1 + 2\beta|k| + \dots)$ está en `dispersion-corrections-across-lattices` Sec. 3.5.
  - *Finite mass:* La desigualdad $c_H < c_{\omega^2} < r_{\text{in}}$ para $0 < m < 1$ en la familia estándar de Dirac está en CS Secs. 4 y 5. Los resultados para moneda de masa separada (`L5b, L6c, L6d, L6f`) con $c_H = c_0 \theta/\sin\theta > c_0$, ausencia de coeficiente cuadrático isótropo en $\omega^2$, anisotropía lineal en `L6e` y fila masiva de ADMP `OPEN` están en CS Sec. 11 y `c-across-lattices` Sec. 5.

*(Nota menor de aclaración, no de error: en la Sec. 1, quinto punto de "Readings", se escribe $a_i \cdot a_j = -l^2/2$ para $i \ne j$, lo cual se sigue inmediatamente de la definición de `hex-ceiling` Sec. 2: tres vectores de longitud $l$ a $120^\circ$ con $a_1+a_2+a_3=0$).*

---

#### 2. ALCANCE: **PASS**
El documento conserva escrupulosamente todos los cuantificadores y restricciones de alcance de las fuentes:
- En el punto 0.2 y en la Sec. 2, la cadena $c_0 \le c_{\text{strict}}^{\text{iso}} \le r_{\text{in}}(C_{\text{micro}})$ **no** se extrapola ilegítimamente fuera de $N_3$: el texto distingue explícitamente que $c_{\text{strict}}^{\text{iso}} \le r_{\text{in}}(C_{\text{micro}})$ vale en general, mientras que $c_0 \le c_{\text{strict}}^{\text{iso}}$ está **probado** únicamente para los conos admitidos y el soporte exacto del símbolo completo en $N_3$ (excluyendo conjuntos de desplazamientos inconmensurables, Sec. 2), y fuera de $N_3$ está únicamente **confirmado fila por fila** en las demás filas declaradas (`CONFIRMED_IN_DECLARED_ROWS`, Hc). De ahí concluye correctamente que $c_0 \le r_{\text{in}}(C_{\text{micro}})$ se cumple *«in every declared row»* (y en $W_{\text{hex}}$ por L0, Sec. 2), sin convertirlo en ley general para todo QCA.
- Se mantienen explícitos los cuantificadores de clase declarada ($s=4$ en `L3s4`), soporte $N_3$, dimensión interna $s$ fija ($s=2$ frente a $s=4, 6$), subclase antipodal $n=3$ (T1), soporte mínimo $F \subseteq \{0\} \cup \operatorname{vert}(H)$ con $s=2$ (T2), y la ausencia de afirmaciones para $s>2$ en el caso hexagonal.
- En la lectura sobre `L6b` (Sec. 1), el texto advierte expresamente que ninguna fuente coloca a `L6b` sobre el mismo conjunto de pasos que `L6a/L6d`, evitando extrapolar que un mismo sustrato deje libre $c_{\text{strict}}^{\text{iso}}$.

---

#### 3. NIVELES: **PASS**
- **Niveles de evidencia:** Ninguna afirmación se presenta con un nivel superior al de su fuente. El propio documento se declara `PRELIMINARY as a synthesis` y preserva las etiquetas exactas de CS: `NO_ABSOLUTE_SCALE_DERIVABLE`, `PROVED_UNDER_FROZEN_CONTRACT` (con una revisión independiente), `CONFIRMED_IN_DECLARED_ROWS`, `REJECTED IN THE DECLARED s=4 CLASS`, `PROVED_IN_REPO`, `GAP_PROVED_IN_CLASS`, `PROVED_FOR_MINIMAL_SUPPORT`, `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS` y `OPEN`.
- **Tabla de la Sec. 1 y coherencia aritmética:** Todos los valores de $r_{\text{in}}$, $c_0$, $c_0/r_{\text{in}}$ y $c_{\text{strict}}^{\text{iso}}$ coinciden exactamente con las fuentes y son aritméticamente coherentes con las unidades declaradas (paso más largo de una actualización $= 1$, una actualización por unidad de tiempo, $V_{\text{causal}}^{\max} = 1$):
  - `L1`: $1, 1, 1, 1$.
  - `L2, L6e`: $1/\sqrt{2}, 1/\sqrt{2}, 1, 1/\sqrt{2}$.
  - `L3, L5a, L5b`: $1/\sqrt{3}, 1/\sqrt{3}, 1, 1/\sqrt{3}$.
  - `L3s4`: $1/\sqrt{3}, a/\sqrt{3}, a, 1/\sqrt{3}$.
  - `L4` (reescalado explícitamente de $[-1,1]^3$ con paso máximo $\sqrt{3}$ en CS Sec. 8 a paso máximo $1$ como en `c-across-lattices` Sec. 4): $1/\sqrt{3}, 1/\sqrt{3}, 1, 1/\sqrt{3}$.
  - `L6a`: $r_{\text{in}} = \sqrt{3}/2$, $c_0 = 1/2 \implies c_0/r_{\text{in}} = 1/\sqrt{3}$, $c_{\text{strict}}^{\text{iso}} = \sqrt{3}/2$.
  - `L6c, L6d, L6f`: $r_{\text{in}} = \sqrt{3}/2$, $c_0 = 3/4 \implies c_0/r_{\text{in}} = \sqrt{3}/2$, $c_{\text{strict}}^{\text{iso}} = \sqrt{3}/2$.
  - `L6b`: $r_{\text{in}} = \sqrt{3}/2$, $c_0 = 1/3 \implies c_0/r_{\text{in}} = (1/3)/(\sqrt{3}/2) = 2/(3\sqrt{3}) = 2\sqrt{3}/9$, $c_{\text{strict}}^{\text{iso}} = 1/\sqrt{3}$ (y $c_{\text{strict}}^{\text{iso}}/r_{\text{in}} = 2/3$ en el texto).

---

#### 4. LECTURAS Y LÍMITES: **PASS**
- Las *readings* de la Sec. 1 y la Sec. 3 se deducen directamente de las filas citadas sin extrapolación. En particular, la observación en la Sec. 1 de que `L3s4` en $a = \sqrt{3}/2$ comparte $c_0 = 1/2$ con `L6a` (en unidades de paso máximo 1) es una consecuencia aritmética inmediata del continuo $(0, 1/\sqrt{3})$ de `L3s4`, y el texto acota de inmediato su alcance: señala que en unidades de $r_{\text{in}}$ difieren ($\sqrt{3}/2$ frente a $1/\sqrt{3}$) y que esto solo muestra posibilidad por elección de parámetros, dejando la universalidad IR (pregunta A) `OPEN`.
- En la Sec. 3, el hecho de que $|\nabla \varepsilon_+| = c_0(1 + 2\beta|k| + \dots) > c_0$ cerca del nodo en las direcciones donde $\beta > 0$ se sigue analíticamente de la fórmula de la Sec. 3.5 de `dispersion-corrections-across-lattices` y del hecho (Sec. 3.3 de ese informe) de que en todas las filas con $\beta \ne 0$ (tanto las cinco impares como `L3s4` para al menos una de las elecciones de signo de $\pm\beta_0$ en los *clusters* $\pm\pi/4$) existen direcciones con $\beta > 0$.
- La Sec. 4 cubre de forma completa y precisa todo lo que la respuesta no establece (no hay ley general QCA, ni imposibilidad general en el hexágono fuera de T1/T2, ni saturación general en BCC, ni cierre de novedad para el techo hexagonal, ni escala física absoluta o identificación con el fotón, ni universalidad IR, ni novedad sobre Bernstein o las construcciones de las fuentes). No hay ninguna extralimitación sobre universalidad IR, escala absoluta o novedad.

---

#### 5. CITAS A INFORMES DE EJECUCIÓN: **PASS**
- **Exactitud y alcance:** Los informes `dispersion-corrections-across-lattices` (Sec. 3.5 y Sec. 3.3) y `c-across-lattices` (Sec. 5) dicen exactamente lo que la Sec. 3 les atribuye y con ese mismo alcance (restringido a las filas declaradas y con $V_{\text{grp}}^{\max}$ y la fila masiva de ADMP `OPEN`).
- **Legitimidad de citar los informes de ejecución:** Es plenamente legítimo —y metodológicamente correcto en este repositorio— citar los informes de ejecución de gates cuyos resultados ya están promocionados en CS. CS funciona como un registro de estado y alcance congelado (*ledger*), y en cada entrada de promoción enlaza expresamente al informe de ejecución correspondiente (`[report](...)`) como el artefacto que contiene las derivaciones, tablas detalladas y lecturas técnicas del gate promocionado. Además, el propio encabezado de la síntesis declara explícitamente esta práctica: *«Every statement cites the promoted section or report it comes from and keeps that result's scope»*. Citar la sección exacta del informe de ejecución junto con la sección de CS aporta trazabilidad granular sin alterar el alcance ni el nivel de evidencia promocionado en CS.

---

#### 6. CONTENIDO PROPIO: **PASS**
Sin necesidad de reparaciones, el documento constituye una síntesis sustantiva y bien articulada, mucho más útil que una mera lista de fuentes. Responde directamente a la pregunta del proyecto (*qué fija y qué no fija el sustrato sobre $c$ dentro de las clases declaradas*) estructurando los resultados dispersos en cuatro tesis claras:
1. El sustrato por sí solo no fija $c_0$ (demostrado tanto en dimensión interna $s=4$ mediante el continuo de `L3s4` en BCC como en dimensión mínima $s=2$ mediante `L6a` vs `L6d` sobre idéntico sustrato hexagonal).
2. El sustrato fija un techo geométrico a través del inradio $r_{\text{in}}(C_{\text{micro}})$ (mediante $c_{\text{strict}}^{\text{iso}} \le r_{\text{in}}$ y $c_0 \le c_{\text{strict}}^{\text{iso}}$, distinguiendo dónde está probado y dónde confirmado por filas).
3. Alcanzar o no ese techo depende conjuntamente de la geometría de los pasos y de los solapamientos internos de la moneda (alcanzado en línea, cuadrado, BCC estándar y cubo; acotado estrictamente por debajo en las subclases hexagonales analizadas).
4. El modelo plano no fija ninguna escala física absoluta (`NO_ABSOLUTE_SCALE_DERIVABLE`), y fuera del límite sin masa en $k=0$ (dispersión no lineal y masa finita) $c_0$ deja de coincidir en general con la velocidad de grupo máxima o con los coeficientes efectivos $c_H, c_{\omega^2}$.

---

### Dictamen global y lista de reparaciones obligatorias

- **Dictamen global:** **PASS**
- **Lista de reparaciones obligatorias:** **Ninguna.** El documento transmite con total fidelidad los resultados promocionados en `CURRENT_STATE.md` y sus informes de ejecución adjuntos, respetando todos los cuantificadores de alcance, niveles de evidencia y controles aritméticos.
