# LOWER_BOUND_NO_CANCELLATION_GATE — ejecución del contrato publicado

Registro de ejecución, 2026-09-17. Evaluación del autor; sin revisión
independiente ni promoción canónica. [A] identifica pruebas analíticas;
[V] identifica exclusivamente identidades comprobadas por el certificado.
El orden de ejecución es herencia, contribución dominante, cancelación,
resto, clasificación. **No se ha modificado el charter.**

**Resultado: `OPEN_AFTER_CANCELLATION_ANALYSIS`.** Se identifican dos
mecanismos candidatos; ninguno suministra un \(A_{M,M_B}(N)e^{-KN}\) con
coeficiente clasificado y resto controlado. No hay \(\delta>0\) para
\(N\ge N_*\) ni nulidad exacta de las dieciséis respuestas. Certificado
auxiliar: **24/24 identidades**, sin cobertura de la no-cancelación ni
de la nulidad.

## 1. Preflight

- Repositorio: `nacho09021973/qca-causal-cones`.
- Rama: `research/b-infinity-post-s4-gate`.
- `HEAD`, `origin/research/b-infinity-post-s4-gate` y
  `git ls-remote origin refs/heads/research/b-infinity-post-s4-gate`:
  `1717d5ec01cb13b74c1178afd659d9fefd31c9c0`, el baseline exigido.
- SHA256 de `theory/LOWER_BOUND_NO_CANCELLATION_GATE.md`:
  `5db6f88a2ca77bfd6d8af2bde9c20f683e05288a0c941f6cd59724e4fb510afb`,
  idéntico a `git show 1717d5e:theory/LOWER_BOUND_NO_CANCELLATION_GATE.md`.
- Ningún cambio tracked inicial, ni staged ni unstaged.
- Cuatro entradas untracked preexistentes, preservadas:
  `Auditoría De Novedad Matemática.md`,
  `debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.log`,
  `debates/2026-09-16--ratificacion-gate-completitud-axial-n3.log`,
  `scripts/__pycache__/` (dos `.pyc`). Todo Python se ejecuta con `-B`.
- SHA256 de `state/CURRENT_STATE.md` al arrancar:
  `0f316960d5892a069cef64d77f9f313f167b8a825de1267592d2aac0b3d46d52`.
  Este archivo **no se modifica**.

Leídos íntegramente antes del cálculo: el charter de este gate, el charter
escalado, el informe y la revisión independiente del gate escalado,
`CURRENT_STATE` §§8.17–8.18, y los scripts
`verify_scaled_ir_gate.py`, `verify_directional_saturation.py`,
`verify_signaling_witness.py`.

La lógica terminal se reconstruyó antes de calcular, en el orden de §4:
un par Pauli no nulo con resto controlado; las dieciséis respuestas
idénticamente nulas; sólo el control `I` no nulo; en cualquier otro caso
`OPEN`. Un término cuadrático positivo de (L) no clasifica \(A\). El rayo
de vértice no nulo no clasifica \(A\) de región. \(K\) no se identifica
con \(J\).

## 2. Herencia — Paso 0 [A]/[V]

Premisas, sin recálculo de la cota ni de la admisibilidad IR:

| Objeto | Fuente | Uso aquí |
| --- | --- | --- |
| \(D_B(N)\le 36 N^4 e^{-JN}\), \(J=(1-\sqrt3/2)\log 2\), \(N\ge 2\) | §8.17, revisión independiente PASS | techo; \(K\ge J\) para \(\|P_B S^N P_A\|\) |
| Ocho operaciones IR-admisibles | informe escalado §4 | las dieciséis señales son del protocolo congelado |
| Columnas \(v\pm id\), \(v+ib\), \(v+b\), \(v-id\) | informe escalado §7.1, [V] | entrada de (L) |
| Identidades (L) y (F) | idem | \(\delta=\|L\|=\|F_j(R_M)\|\) |
| \((S^N)_{(N,N,N),0}=4^{-N}\|{\downarrow}\rangle\langle{\downarrow}\|\) | informe escalado §2, [V] | contribución de vértice, no líder de región |
| \(S_{(1,1,1)}=\frac14\|{\downarrow}\rangle\langle{\downarrow}\|\) | [V] este certificado | el camino único aniquila \(\uparrow\) |

No se reabre el charter escalado. No se cambia encoder, detector, geometría,
perfil, \(\theta\), walk, nodo, \(\Lambda_N\), \(\Lambda'_N\), \(\delta\), ni
regiones. \(D_B=\tfrac12\|\rho_1-\rho_0\|_1\) se hereda.

Expansión exacta de (L), con \(v=r+a\) y
\(H_E=\langle a,Ea\rangle+2\operatorname{Re}\langle r,Ea\rangle\) [A]:

\[
\begin{aligned}
L_{I,E}&=\langle a,Ea\rangle+2\operatorname{Re}\langle r,Ea\rangle
+\langle d,Ed\rangle-2\operatorname{Im}\langle r+a,Ed\rangle,\\
L_{3,E}&=\langle a,Ea\rangle+2\operatorname{Re}\langle r,Ea\rangle
+\langle d,Ed\rangle+2\operatorname{Im}\langle r+a,Ed\rangle,\\
L_{1,E}&=\langle a,Ea\rangle+2\operatorname{Re}\langle r,Ea\rangle
+\langle b,Eb\rangle-2\operatorname{Im}\langle r+a,Eb\rangle,\\
L_{2,E}&=\langle a,Ea\rangle+2\operatorname{Re}\langle r,Ea\rangle
+\langle b,Eb\rangle+2\operatorname{Re}\langle r+a,Eb\rangle.
\end{aligned}
\]

Los detectores son positivos, así que \(\langle a,Ea\rangle\) y
\(\langle d,Ed\rangle\), \(\langle b,Eb\rangle\) son \(\ge 0\). Eso **no**
fija el signo de \(L\): la interferencia con \(r\) puede cancelarlos.

\(r=P_B S^N\phi_N\) suma sobre **todo** \(\mathbb Z^3\), no sólo sobre
\(A_N\). Las piezas \(a,b,d\) sí están soportadas en Alice. Esta distinción
se usa abajo; no se trunca el recurso.

## 3. Método asintótico — Paso 1 [A]

Contorno heredado: \(p\mapsto p-itu\), \(t=\log 2\), \(u=(1,1,1)\). Da la
premisa \(J\), no la tasa líder. El walk es anisótropo (axiales sólo en
\(x\), diagonales de cara en \(xy\)); el tilt óptimo para cada \(v\) no se
identifica. **No se impone \(K=J\).**

Hay dos mecanismos candidatos. Ninguno se promueve a
\(A_{M,M_B}(N)e^{-KN}\) controlado.

### 3.1 Mecanismo V — vértice / centros [V]/[A]

Desplazamiento \((N,N,N)\) en \(N\) pasos: cada paso debe ser \((1,1,1)\).
Entonces

\[
(S^N)_{(N,N,N),0}=4^{-N}\lvert{\downarrow}\rangle\langle{\downarrow}\rvert,
\qquad K_{\mathrm V}=\log 4.
\]

El recurso es \(\downarrow\), así que este camino conecta Alice en el
origen con el centro de Bob. El mismo camino **aniquila** \(\uparrow\):
\(S_{(1,1,1)}\lvert{\uparrow}\rangle=0\). Por tanto la amplitud \(b\)
(encoder \(\sigma_1,\sigma_2\)) **no** viaja por el rayo de vértice.

\(K_{\mathrm V}=\log 4>2\log 2>\operatorname{arcosh}(125/64)\) [V]: el
vértice tiene tasa exacta estrictamente mayor que \(J\). Eso compara
\(4^{-N}\) con una **cota** sobre los demás kernels, no demuestra que
otro término lo domine. El charter prohíbe promover este rayo a
\(A\not=0\) de región: la suma coherente sobre \(A_N\times B_N\) incluye
otros desplazamientos, con combinatoria hasta \(O(N)\) relativa al término
único, y perfiles que varían. **El vértice no puede promoverse a líder
regional;** no está clasificado como líder.

### 3.2 Mecanismo B — capa de los puntos enfrentados [A]/[V]

El infimo euclídeo sobre las bolas continuas se alcanza en los puntos
enfrentados sobre \(\hat u=(1,1,1)/\sqrt3\):

\[
x_\ast=\frac N4\hat u,\qquad
y_\ast=N(1,1,1)-\frac N4\hat u,\qquad
\frac{|y_\ast-x_\ast|_2}N=\sqrt3-\frac12>1.
\]

La última desigualdad es \(3>9/4\) [V]. Ese \(v\) está fuera de la bola
IR \(|v|_2\le 1\) y dentro de \(\|v\|_\infty\le 1\). El tilt es exactamente
el mínimo (G): \(u\cdot v=3-\sqrt3/2\). Sobre todo \(A_N\times B_N\) se
tiene por tanto \(I(v)\ge J>0\) (premisa), y el candidato a **mínimo** de
\(I\) es este borde.

En esos puntos los perfiles **se anulan** [V]: \(F_N(x_\ast)=h_B(y_\ast)=0\).
A profundidad euclídea \(\varepsilon=N/4-|x|_2\),

\[
F_N=\frac{64\varepsilon^2(N-2\varepsilon)^2}{N^4}.
\]

Con \(F\to 0\) [V],

\[
s_N=\sin(\pi F/2)=\frac\pi2 F+O(F^3),\qquad
c_N=\cos(\pi F/2)-1=-\frac{\pi^2}{8}F^2+O(F^4).
\]

En la capa que minimizaría \(I\), la respuesta lineal en el encoder es
\(s_N\) (amplitudes \(b\) y \(d\)); \(a\) es de segundo orden en \(F\) y
está subdominante **en esa capa**. Eso no clasifica \(A\) de (L): faltan
el valor de \(I\) en el borde, el óptimo anisótropo, y el coeficiente de
Laplace.

### 3.3 Interferencia con la cola libre [A]

\(r=S^N\phi_N\) es de banda \(|p|\le N^{-1}\). En la escala \(q=Np\),
\(S(q/N)^N\) permanece acotada y \(r(y)=O(N^{-3/2})\) uniformemente en
\(B_N\), **sin** el factor \(e^{-JN}\) de \(P_B S^N P_A\). Los términos
cuadráticos \(\langle d,Ed\rangle\) son \(O(e^{-2KN})\) si \(d=O(e^{-KN})\);
la interferencia \(\langle r,Ed\rangle\) es candidata a líder de \(L\)
(un solo factor del kernel, por una cola polinómica). El factor de forma
\(\int_{|q|\le 1}e^{-iq\cdot y/N}S(q/N)^N g(q)\,d\mu_q\) en
\(|y|/N\in[\sqrt3-1/2,\sqrt3+1/2]\) **no** se ha demostrado no nulo.
No se usa como \(A\not=0\).

### 3.4 Conclusión del Paso 1

No hay una contribución líder identificable con control suficiente para
ningún par. No se inventa \(A_{M,M_B}(N)e^{-KN}\). La única tasa
certificada que acota las piezas soportadas en Alice sigue siendo
\(K\ge J\) (premisa), y no es una equivalencia asintótica.

## 4. Estructura de cancelación — Paso 2 [A]

Sin líder identificado, \(A_{M,M_B}\) **no se clasifica** en ninguno de
los tres apartados del charter.

- **No nulo.** No hay demostración analítica de \(A\not\equiv 0\). El
  término de vértice \(4^{-N}b_N(0)\) es no nulo [V] y entra en \(a\) y
  \(d\) en el origen, pero no controla la suma de región. Un término
  \(\langle d,Ed\rangle\ge 0\) no impide la cancelación contra
  \(H_E\) o \(\langle r,Ed\rangle\).
- **Nulo por simetría.** No se exhibe ninguna simetría del protocolo
  congelado (el walk no intercambia \(1\leftrightarrow 2\leftrightarrow 3\);
  \(A_N\) y \(B_N\) no son inversos; el kernel no es real; \(I\) y
  \(\sigma_3\) difieren por \(4\operatorname{Im}\langle v,Ed\rangle\),
  que no se ha demostrado cero). El aniquilamiento de \(\uparrow\) en el
  **único** camino \((1,1,1)^N\) es una cancelación de un sumando, no una
  simetría de \(b\) sobre la región.
- **Orden finito.** En la capa enfrentada, \(c_N=O(F^2)\) frente a
  \(s_N=O(F)\) es una jerarquía local, no una expansión de \(L\) con
  primer término no nulo identificado. El resto de esa jerarquía no se
  cierra.

No se ejecutó un barrido de \(N\) ni se usó coma flotante para inferir
ceros o no-ceros. No hay diagnóstico `SUPPORTED` que añadir.

El Paso 3 no procede: exige el Paso 2 escrito para el par. La lower bound
bruta no se usa para saltar la cancelación.

## 5. Tabla de los dieciséis pares

\(P_j=(I+\sigma_j)/2\). «No identificado» significa que no hay
\(A e^{-KN}\) con \(A\) clasificado. \(K\) certificado: sólo la cota
inferior \(J\) sobre \(\|P_B S^N P_A\|\), no una tasa líder del par.
Resto: no controlado, porque no hay líder. Estado individual: `OPEN_PAIR`.

| Encoder | Detector | Líder | \(K\) | Clasificación de \(A\) | Simetría / primer término | Resto | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \(I\) (REFERENCE_CONTROL) | \(I\) | no identificado | \(\ge J\) (premisa) | no clasificado | — | no | OPEN_PAIR |
| \(I\) (REFERENCE_CONTROL) | \(P_1\) | no identificado | \(\ge J\) | no clasificado | — | no | OPEN_PAIR |
| \(I\) (REFERENCE_CONTROL) | \(P_2\) | no identificado | \(\ge J\) | no clasificado | — | no | OPEN_PAIR |
| \(I\) (REFERENCE_CONTROL) | \(P_3\) | no identificado | \(\ge J\) | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_1\) | \(I\) | no identificado | \(\ge J\) | no clasificado | vértice mata \(\uparrow\); no es simetría de región | no | OPEN_PAIR |
| \(\sigma_1\) | \(P_1\) | no identificado | \(\ge J\) | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_1\) | \(P_2\) | no identificado | \(\ge J\) | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_1\) | \(P_3\) | no identificado | \(\ge J\) | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_2\) | \(I\) | no identificado | \(\ge J\) | no clasificado | vértice mata \(\uparrow\); no es simetría de región | no | OPEN_PAIR |
| \(\sigma_2\) | \(P_1\) | no identificado | \(\ge J\) | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_2\) | \(P_2\) | no identificado | \(\ge J\) | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_2\) | \(P_3\) | no identificado | \(\ge J\) | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_3\) | \(I\) | no identificado | \(\ge J\) | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_3\) | \(P_1\) | no identificado | \(\ge J\) | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_3\) | \(P_2\) | no identificado | \(\ge J\) | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_3\) | \(P_3\) | no identificado | \(\ge J\) | no clasificado | — | no | OPEN_PAIR |

No se presupone equivalencia entre \(\sigma_1,\sigma_2,\sigma_3\). Las
filas de \(\sigma_1\) y \(\sigma_2\) registran el mismo hecho de camino
único porque ambas producen la columna \(b\) (componente \(\uparrow\));
eso no es una simetría del walk.

## 6. Resultado terminal global

**Único estado terminal asignado: `OPEN_AFTER_CANCELLATION_ANALYSIS`.**

No hay par Pauli con \(\delta(N)>0\) para todo \(N\ge N_*\) ni asintótica
de amplitud no nula con resto controlado:
`SIGNAL_NONVANISHING_IN_FROZEN_PAULI_PAIR` no procede, y no se registra
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.

No hay \(\delta=0\) para los dieciséis pares:
`ALL_SIXTEEN_EXACTLY_ZERO` no procede. Tampoco se afirma \(D_B=0\).

Ningún par con \(M=I\) ha sido demostrado no nulo:
`REFERENCE_CONTROL_ONLY_NONVANISHING` no procede.

El charter §4, caso residual, se aplica literalmente: líder no
identificado, coeficiente no clasificado, resto no controlado.

La cota \(0\le\delta\le 36 N^4 e^{-JN}\) permanece exactamente el
resultado de §8.17; no es un estado nuevo.

## 7. Techo del claim

- **No-cancelación de un par:** no demostrada.
- **Nulidad de los 16 pares:** no demostrada.
- **\(D_B=0\):** no afirmada y no implicada por nada de lo anterior.
- **Fuera de la familia congelada:** nada. Un encoder suave
  \(M=aI+b\cdot\sigma\), otra geometría u otro walk no se tocan.
- El rayo de vértice no nulo no se ha convertido en señal de región.
- No se usa «puramente de red» ni «invisible a potencias de \(\Lambda\)».
- No se reabre §8.16, §8.17, `3/128`, no-corner, ni `Delta T=2`.
- \(N\to\infty\) no es \(a,\tau\to 0\). Sin metros, segundos ni eV.

## 8. Implementación

Se crea `scripts/verify_lower_bound_no_cancellation_gate.py`. No se
modifica ningún verificador revisado.

**Necesidad.** Los helpers existentes extraen el símbolo y las columnas
(L)/(F), pero no contienen: el aniquilamiento de \(\uparrow\) por
\(S_{(1,1,1)}\); la geometría de los puntos enfrentados; la anulación y
el desarrollo de \(F_N\), \(c_N\), \(s_N\) en la esfera; ni la comparación
\(\operatorname{cosh}^3(\log 2)=125/64<4\). Añadirlos a un script ya
revisado cambiaría sus bytes.

**Qué demuestra el certificado.** 24 identidades exactas [V] listadas en
su salida. **Qué no demuestra:** identificación del líder, clasificación
de \(A\), control del resto, \(\delta>0\), \(\delta=0\), ni el estado
terminal. Eso está en el texto [A].

Dependencias: las mismas que el certificado escalado (Python 3.12, SymPy
1.14.0, NumPy 1.26.4 transitivo por el import de
`verify_directional_saturation`). No se instala nada nuevo. No hay
punto flotante en cantidades decisivas.

SHA256 del certificado nuevo:
`60ede622468e85b844385ede075cc2f13eb773161ceaa72d8c0e1f097157c06f`.

## 9. Validación

Todos los comandos siguientes terminaron con código de salida `0`, desde
la raíz, `python3 -B`, sin `--output`.

| Comando | Resultado |
| --- | --- |
| `scripts/verify_lower_bound_no_cancellation_gate.py` | 24/24 identidades exactas |
| `scripts/verify_scaled_ir_gate.py` | 53/53; cota escalada intacta |
| `scripts/verify_narrow_band_gate.py` | 34/34 |
| `scripts/verify_directional_saturation.py` | 27/27 |
| `scripts/verify_signaling_witness.py` | 17/17 |
| `scripts/verify_weyl_dirac_gate.py` | PASS |
| `scripts/cert_Aa_s4_counterexample.py` | PASS |
| `scripts/review_Aa_s4_exact.py` | PASS |

`git diff --check`: sin incidencias en los archivos nuevos (comparados
con `/dev/null` en modo no-index). Ningún archivo se ha staged.
`CURRENT_STATE.md` conserva el hash de §1. **Sin commit ni push.**

## 10. Registro de congelación (redacción solamente)

Tras la revisión independiente `PASS`, se incorpora la aclaración
recomendada de §3.1: el vértice **no puede promoverse** a líder
regional; \(\log 4>J\) compara su tasa exacta con una cota, no demuestra
dominancia. **No cambian** el estado
`OPEN_AFTER_CANCELLATION_ANALYSIS`, la tabla de dieciséis pares, ni
ninguna cantidad. El certificado no se toca.
