---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-23 13:12
proyecto: /home/ignac/qca-causal-cones
tema: (tema en línea de órdenes)
rondas: 2
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - CLAUDE OPUS — Claude (Anthropic) — claude -p --model claude-opus-5 --effort high (sellado)
  - GEMINI — Google — generativelanguage.googleapis.com/gemini-3.1-pro-preview
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

Revisión independiente de la versión reparada de C3. Claude es el revisor principal. Audita únicamente: identidad exacta de Lcond; q_N y éxito; p0_N -> p_infty>0 para M_B=I; demostración fila a fila de L_PP,N=O(N^-3) para M en {I,sigma1,sigma2,sigma3}, D0=I, usando C15-C16 de C2c; y conclusión C3.7. Mantén OPEN el líder de Lcond, |Lcond|, comparación con L, H1c y E/AdS. No uses N=24/40, simulaciones, cuadraturas, barridos ni fuentes externas. Emite PASS/INCOMPLETE/FAIL por obligación y veredicto global C3_PROOF_WRITTEN_REVIEW_ACCEPTED, C3_REPAIR_REQUIRED, C3_FAIL o C3_INCOMPLETE. No modifiques archivos.

## Contexto

### Contexto adjunto: theory/IR_C3_CONDITIONING_GATE.md
```
# C3 — condicionamiento posterior a la proyección IR

Fecha: 2026-09-23. Estado inicial: **AUTHORIZED / NOT_EXECUTED**.

Este gate es la continuación separada de C1/C2/C2c. No sustituye el observable
firmado `Lpp` por el observable condicionado y no reabre C2, C3 de otras líneas,
H1c ni E/AdS.

## Objetos congelados

Se conserva el walk homogéneo CJWW (5.15), nodo cero, dos componentes,
recurso, perfiles, regiones y corte
`P=1_{|p|<=N^{-1/2}}`, `Q=I-P`. Se consideran los cuatro encoders
`M in {I,sigma1,sigma2,sigma3}` y se fija el detector de Bob `M_B=I`,
`E=h_N I`. La elección `M_B=I` es parte del alcance: no se extiende la
asintótica de condicionamiento a detectores de rango uno.

Con `v=U_M phi_N`, `w=P v`, `t=Q v`, `q_N=||t||^2` y
`p0_N=<S^N phi_N,E S^N phi_N>`, se mantienen
\[
L_{PP}=\operatorname{tr}(E S^N P\Delta P S^{-N}),
\qquad
L_{\mathrm{cond}}=\frac{L_{PP}+q_Np0_N}{1-q_N}.
\]

## Obligaciones

1. Derivar la identidad exacta de los estados condicionados y de
   `Lcond`, incluyendo las probabilidades de éxito `1` y `1-q_N`.
2. Usar únicamente la asintótica C1 ya certificada para los cuatro encoders,
   `q_N=D N^{-5/2}(1+O(N^{-1/2}))`, con `D>0`.
3. Probar para `M_B=I` que `p0_N -> p_infty>0` mediante la convergencia
   del recurso y la positividad analítica del recurso Weyl en una bola abierta.
4. Derivar la corrección
   `Lcond-Lpp=D p_infty N^{-5/2}(1+o(1))`.
5. Mantener OPEN cualquier afirmación sobre el término líder de `Lcond`,
   `|Lcond|`, `Lcond-Lpp` frente a `L`, o una interpretación como protocolo
   local. No usar diagnósticos N=24/40 para cerrar ninguna asintótica.

## Veredictos posibles

La ejecución puede producir `C3_PROOF_WRITTEN / REVIEW_PENDING`,
`C3_REPAIR_REQUIRED`, `C3_FAIL` o `C3_INCOMPLETE`. La aceptación final exige
una revisión independiente posterior. Ningún resultado actualiza por sí solo
`state/CURRENT_STATE.md` ni reabre E/AdS.
```

### Contexto adjunto: reports/2026-09-23--c3-conditioning-execution.md
```
# C3 — ejecución del gate de condicionamiento

Fecha: 2026-09-23. Estado: **C3_PROOF_WRITTEN / REVIEW_PENDING**.
Contrato: [IR_C3_CONDITIONING_GATE](../theory/IR_C3_CONDITIONING_GATE.md),
commit `8ce5cc1`.

La ejecución conserva el walk CJWW (5.15), nodo cero, recurso, regiones,
perfiles y corte de C1/C2/C2c. El alcance cuantitativo es para los cuatro
encoders originales y `M_B=I`. No se usan N=24/40, simulaciones, cuadraturas,
barridos, `L-Lpp` ni el Teorema 4.4.

## 1. Identidad exacta del condicionamiento

Sea
\[
v=U_M\phi_N,\qquad w=P v,\qquad t=Qv,
\qquad q_N=\|t\|^2.
\]
Como `P phi_N=phi_N`, `w` es el resultado de retener el sector P para el
bit cero, mientras que para el bit uno la probabilidad de retención es
`||w||^2=1-q_N`. Para `q_N<1`, el estado condicionado del bit uno es
`|w><w|/(1-q_N)`, y el del bit cero es `|phi_N><phi_N|`.

Por tanto, con
\[
\Delta=|v\rangle\langle v|-|\phi_N\rangle\langle\phi_N|,
\qquad
\Delta_{PP}=P\Delta P,
\]
se obtiene exactamente
\[
\Delta_{\mathrm{cond}}
=\frac{\Delta_{PP}+q_N|\phi_N\rangle\langle\phi_N|}{1-q_N}.
\tag{C3.1}
\]

Para el efecto de Bob `E=h_N I`, tomando la traza después de `S^N`,
\[
\boxed{
L_{\mathrm{cond},N}
=\frac{L_{PP,N}+q_Np_{0,N}}{1-q_N}},
\qquad
p_{0,N}=\langle S^N\phi_N,E S^N\phi_N\rangle.
\tag{C3.2}
\]
En particular,
\[
\boxed{
L_{\mathrm{cond},N}-L_{PP,N}
=\frac{q_N(p_{0,N}+L_{PP,N})}{1-q_N}}.
\tag{C3.3}
\]
La identidad no identifica `Lpp` con una diferencia de probabilidades
condicionadas: `Lpp` es el observable firmado antes de la normalización.

## 2. Probabilidad de éxito y límite de `p0_N`

C1 da, para cada uno de los cuatro encoders,
\[
q_N=D N^{-5/2}(1+O(N^{-1/2})),
\qquad D=\frac{1024\pi^2 B^2}{5}>0.
\tag{C3.4}
\]
Así `q_N -> 0` y la probabilidad de éxito del bit uno es
`1-q_N=1-DN^{-5/2}(1+O(N^{-1/2}))`; la del bit cero es exactamente uno.

Para `M_B=I`, el recurso libre escalado converge uniformemente en la bola de
Bob al campo Weyl `R_0` usado en C1. Las sumas de Riemann dan
\[
p_{0,N}\longrightarrow
p_\infty:=\int_{|Y-u|<1/4}h(Y)\|R_0(Y)\|^2\,d^3Y.
\tag{C3.5}
\]
El peso `h` es estrictamente positivo en el interior de la bola. `R_0` es
la transformada de Fourier de una función compacta no nula y, por tanto,
es analítica; no puede anularse en toda una bola abierta. De aquí
\[
p_\infty>0.
\tag{C3.6}
\]
No se evalúa numéricamente `p_infty`.

## 3. Corrección de normalización

La premisa que se usa aquí está demostrada fila a fila en C2c, no sólo
por la cobertura global de los dieciséis pares. En §8 de
`reports/2026-09-22--c2c-structural-scope.md` aparecen explícitamente las
cuatro filas con `D_0=I` y
`M in {I, sigma_1, sigma_2, sigma_3}`. La expansión (C16), aplicada a cada
una de esas filas, es

\[
L_{PP}^{M,D_0}=N^{-3}\mathscr A_{M,D_0}(\sqrt N)+O(N^{-13/4}).
\]

La propia clasificación de C2c controla uniformemente el coeficiente líder
en el alcance congelado; por tanto cada uno de esos cuatro pares satisface
`L_{PP,N}=O(N^{-3})`, y en particular `L_{PP,N}->0`. Insertando (C3.4)–(C3.6) en
(C3.3),
\[
\boxed{
L_{\mathrm{cond},N}-L_{PP,N}
=D p_\infty N^{-5/2}(1+o(1))}. 
\tag{C3.7}
\]
La corrección es algebraica y positiva a orden líder. Esto no determina el
término líder de `L_cond` ni de `Lpp` por separado: puede existir cancelación
entre `Lpp` y la corrección de (C3.3). Tampoco compara `Lcond-Lpp` con el
observable total `L` mediante una norma global.

## 4. Veredicto de ejecución y límites

| Obligación | Estado |
| --- | --- |
| Identidad exacta de estados y `Lcond` | PASS, pendiente de revisión |
| Probabilidades de éxito | PASS, pendiente de revisión |
| `p0_N -> p_infty > 0` para `M_B=I` | PASS, pendiente de revisión |
| Corrección (C3.7) | PASS, pendiente de revisión |
| Líder de `Lcond` o `abs(Lcond)` | OPEN |
| Comparación `Lcond-Lpp` con `L` | OPEN y fuera del gate |

Resultado de esta ejecución: **`C3_PROOF_WRITTEN / REVIEW_PENDING`**. C3 no
reabre C2, no modifica C2c, no abre H1c ni E/AdS y no constituye una
interpretación de transporte local.
```

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

### Contexto adjunto: state/CURRENT_STATE.md
```
# CURRENT_STATE

**Date:** 2026-09-22
**Status:** STANDARD WEYL/DIRAC EXACT GATE: PASS; strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS; point-(3) ceiling PROVED UNDER FROZEN CONTRACT, one independent review PASS; flat CJWW (5.15) operational IR-corona result CLOSED in its frozen class; **ACTIVE RESEARCH LINE = H1-only reopening for the slowly inhomogeneous extension**: H1-SR proved under frozen beta contract, H1a/H1b proof written/unreviewed, layer absolute-mass bound PASS, G-insertion and final-Q-leakage PASS_IN_LOCAL_WINDOW, `H1c_LOCALIZATION (L') = OPEN`; H1 remains OPEN; E0 and POWER_13/2_STABILITY remain OPEN_AT_STOP; E/AdS remains STOPPED_UNPROVEN. IR spectral-attribution front (Sec. 10.1): C1 PASS, C2a PASS for sigma2/I (one independent agent review), C2b PASS for sigma2/I (B4_PRIME_PASS separately; one independent agent review), C2c structural scope C2C_PASS for the frozen 16-pair scope, C3 SEPARATE.

**Branch-local state.** This file is reconciled on
`research/b-infinity-post-s4-gate` only, so that it agrees with all evidence
merged on this branch. It is **not** a canonical promotion: `main` is
unchanged, and promotion requires a separate explicit decision.

**Repository:** `nacho09021973/qca-causal-cones`

**Evidence baseline:** `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.
Canonical promotion is recorded in
[`2026-09-14--standard-gate-promotion.md`](../reports/2026-09-14--standard-gate-promotion.md).
**Only point (3), the strict-cone ceiling, is chartered and authorized by
direct user instruction** (Sec. 7.2). The full C gate is not ratified.

**Correction (2026-09-14):** `B*` as a comparison against the one-step
inradius `r_in(C_micro)` is superseded by `B_infty^*`, a comparison against
the strict asymptotic isotropic speed `c_strict^iso`. See
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) and
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0. New baseline-specific certificate: for the
standard Pavia Weyl family in d=3, `C_infty^strict = C_micro` exactly, so
`c_strict^iso = r_in(C_micro) = 1/sqrt(3)`; see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
This baseline-specific certificate did not by itself close the gate; the
later s=4 counterexample completed it for the declared s=4 class.

**Integration (2026-09-15, branch-local):** an explicit irreducible `s=4`
family on the same `N_3`, with the same `D2` action, has
`C_infty^strict = C_micro` and `c_strict^iso = 1/sqrt(3)`, but
`c_0(a) = a/sqrt(3)` for every `0 < a < 1`. This is `COUNTEREXAMPLE_VERIFIED`
in the sense of the
[gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) Sec. 5 for the
declared `s=4` class (Sec. 4.1 below). It does not refute the standard Pavia
`s=2` certificate above. Evidence:
[analytic note](../theory/S4_STRICT_CONE_COUNTEREXAMPLE.md) and
[freeze record](../reports/2026-09-15--s4-strict-cone-counterexample-freeze.md)
(`1dae941`), [independent review](../reports/2026-09-15--s4-independent-review.md)
(`aeec462`), [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md)
(`f74018f`). **NOVELTY = OPEN.**

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.
- In the verified standard Dirac couplings they differ for every `0 < m < 1`.
  Name the extraction `c_H` or `c_{ω^2}`; do not use an unspecified finite-lattice
  `c_IR` as though those coefficients were interchangeable.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Canonical hypothesis status

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

### B_infty^* — strict asymptotic matching (supersedes B* / inradius matching)

Candidate:

`c_0 = c_strict^iso`, `c_strict^iso = min_{n̂} h_infty(n̂)`,

with `h_infty` the strict asymptotic support function of
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md) Sec. 6.
Interpretation: `c` would match the exact long-run isotropic propagation
speed of the same dynamics, not necessarily the inradius of the one-step
body `C_micro` — the two satisfy `c_strict^iso <= r_in(C_micro)` in general,
with equality only where separately certified (see the d=3 row below).

| Claim | Status and scope |
| --- | --- |
| A — IR universality | **OPEN** |
| B_max | **REJECTED** under isotropic containment in an anisotropic causal body, d >= 2 |
| B_full | **REJECTED / GEOMETRICALLY IMPOSSIBLE** for a nondegenerate isotropic ball equaling a finite lattice polytope, d >= 2 |
| Exact finite-mass B* | **REJECTED IN STANDARD DIRAC FAMILY**, for both specified extractions, every 0 < m < 1 (comparison against `r_in(C_micro)`, unaffected by the B_infty^* correction) |
| B*_0 (linear order, `c_0=r_in`) | **VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN** |
| B*_cont | **VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN** |
| B_infty^*, d=3 Pavia baseline (`C_infty^strict=C_micro`, full nonlinear order) | **CERTIFIED for the standard Weyl family `A+,B+,A-,B-`** (`s=2`): `c_0 = c_strict^iso = 1/sqrt(3)`; d=1,2 not checked; unaffected by the s=4 result |
| Strong B_infty^* (`c_0 = c_strict^iso` forced by locality, unitarity, homogeneity and D2 covariance at fixed `N_3`) | **REJECTED IN DECLARED s=4 CLASS** — explicit counterexample, Sec. 4.1; false for any class containing that family |
| B_infty^* in the published minimal `s=2` class (P17, including its Eq. (2)) | **NOT REFUTED by the s=4 result; rigidity OPEN as an in-repo claim.** Origin-node inradius matching there is a conditional application of P17's classification plus the standard certificate, not a new theorem. The strict-body certificate is recorded for `A+,B+,A-,B-`; its transfer across all of P17's equivalences is not separately checked |
| B_infty^* for `s=2` without P17 Eq. (2), or with an irreducible internal symmetry representation `R` for `s>2` | **OPEN** |
| Novelty of the s=4 family and its strict-support statement | **OPEN** — no equivalent found in eleven checked primary sources; not a novelty certificate |

The restricted statements are established for the declared cases below.
There is no general rigidity theorem, proof of A, or novelty claim.

### 4.1 Declared s=4 counterexample class

**Status: COUNTEREXAMPLE_VERIFIED for this class; independent review PASS;
NOVELTY = OPEN.**

| Item | Declaration |
| --- | --- |
| Geometry | d=3, `N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`, all eight modes active, no on-site coefficient, one complete update per time unit, phase `exp(-i k.h)` |
| Internal space | `s=4 = C^2_sigma (x) C^2_tau`; parameter `0<a<1`, `b=sqrt(1-a^2)` |
| Symbol | `A_a(k) = W exp(-i q_x Gamma_x) exp(-i q_y Gamma_y) exp(-i q_z Gamma_z)`, `q_i=k_i/sqrt(3)`, `W = I (x) exp(-i pi tau_z/4)` |
| Isotropy | D2 half-turns acting on `N_3`; `R_i = sigma_i (x) I_2` — two copies of the Pauli projective class, hence a **reducible** representation; full cubic symmetry not assumed |
| Irreducibility | Dynamics irreducible: scalar joint commutant of all eight Fourier coefficients |
| Gapless sector | `k=0`; two isolated rank-two clusters at quasienergies `+/-theta`, `theta=pi/4`; isotropic, untilted cones measured from each cluster's node |
| Result | `C_infty^strict = C_micro` exactly (all vertex traces nonzero, so no vertex coefficient is nilpotent); `c_strict^iso = 1/sqrt(3)`; `c_0(a) = a/sqrt(3)` |
| Coverage | One particular product ansatz, not a classification of four-component walks |

Scope limits, all retained:

- **Procedure.** The class table above was written at the freeze and review,
  after the construction, not before solving as charter Sec. 2 requires. This
  limits which classes the example speaks to; it does not affect the
  mathematical validity of the certified inequality.
- **Strict means exact support.** Vertex amplitudes may decay exponentially.
  No ballistic, essential or Lieb-Robinson front statement is made.
- **Floquet-shifted nodes.** `A(0) = W` is not a global phase.
- **Family identity only.** For `0<theta<pi/2`,
  `c_0^2 + 2 sin^2(Delta eps/2) g_ii(0) = 1/3`, where `Delta eps = 2 theta`
  and `g` is the projector quantum metric. It comes from the
  intra/inter-sector split `a^2 + b^2 = 1` of the involutions `Gamma_i`.
  Equating `1/3` with `(c_strict^iso)^2` additionally needs vertex survival,
  which is certified at `theta=pi/4`, or, for fixed `a`, on an open
  neighbourhood where all vertex traces remain nonzero. This is not a
  general QCA theorem.
- **Prior art.** Product-of-projector walks (MB18, BM25), four-component Weyl
  mixing (BB94), shifted Floquet Weyl nodes, adjustable continuum velocity,
  and involution block completion (AF16/17) are antecedents and must be
  attributed. Raynal's explicit s=4 Dirac family is excluded as an
  identification. The most useful open equivalence check is AF16/17's
  homogeneous paired-walk specialization.
- **Certificates.** `scripts/cert_Aa_s4_counterexample.py` and
  `scripts/review_Aa_s4_exact.py` both return PASS (SymPy 1.14.0, zero
  tolerance), and `scripts/verify_weyl_dirac_gate.py` still returns PASS
  (375 checks), on this branch.

## 5. Completed standard Weyl/Dirac exact gate

**Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**

Evidence is the committed
[contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
[analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
[verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
[permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
Source provenance and the published sign/dagger issues are recorded there.
The analytic proof establishes the open mass interval and continuum scaling;
the check count alone is not their justification or a formal proof certificate.

### Declared family and coordinates

The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
the minimal two-component blocks. The seven symbols are not seven independent
geometries: transposes/chiralities within a dimension share support, inradius
and linear speed. There are three dimension-specific geometries in this battery.

Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
complete update per time unit:

`N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,

`C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,

`r_in = 1/sqrt(d)`, `V_causal^max = 1`.

### Massless equality

For d=1,2,3 in this family, at the declared zero node,

`m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.

This is equality of the linear IR coefficient, not exact finite-momentum
relativistic dispersion or a theorem about every admissible symbol.

### Fixed nonzero lattice mass

For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
`0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
continuous from the identity near the massless zero node. Then

`cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,

`F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.

Exact finite-mass B* is refuted in the standard family under either extraction.
This result is no longer PRELIMINARY.

The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
expansions: `b = r_in^2 n (1-F)/(2m)` and
`c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
not a failure of the exact spectrum or an inconsistent calculation.

The endpoint m=1 is separate: actual hopping vanishes, active support becomes
`{0}`, and its inradius and spatial coefficients are zero. It is not covered
by the strict inequalities for `0 < m < 1`.

### Small-mass / continuum matching

For each standard coupling in d=1,2,3,

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
the equality of the limits is established analytically. The joint scaling
of momentum, dimensionless mass, neighbor length and time step is specified
in the report. Its continuum statement is local at fixed rescaled momentum
and mass, not a full propagator convergence theorem on arbitrary states.

## 6. Current scientific interpretation

**Superseded as the active line by Sec. 8 (2026-09-16).** This section records
the `B_infty^*` reading of the project and remains valid where proved, but its
scalar summaries must be read under the scope correction in Sec. 8.6.

The live idea is no longer:

`c = maximum microscopic speed`,

nor, unqualified, `c_massless = r_in(C_micro)`. The corrected comparison is
`B_infty^*`: `c_0 = c_strict^iso`, the exact strict asymptotic isotropic
speed of the same dynamics (Sec. 4). Its strong form is rejected in the
declared s=4 class (update below). `r_in(C_micro)` remains a provable
upper bound (`c_strict^iso <= r_in(C_micro)`), and is known to be exactly
attained — `c_strict^iso = r_in(C_micro)` — for the standard Pavia Weyl
family in d=3, by an explicit vertex non-nilpotency certificate, not merely
by the linear-order Taylor coefficient.

**Update (2026-09-15, branch-local).** Locality, unitarity, homogeneity and
D2 covariance at fixed `N_3` do **not** force `c_0 = c_strict^iso` once the
internal dimension is enlarged. The s=4 family (Sec. 4.1) keeps the whole
strict body, `C_infty^strict = C_micro`, while its Weyl slope varies
continuously below `1/sqrt(3)`. The strict causal body alone therefore does
not fix the Weyl speed. In this family the missing speed is exactly
accounted for by the inter-sector part of the involutions (the family
identity in Sec. 4.1). Whether that is a structural principle or a feature of
this ansatz is **OPEN**.

What remains unknown is which additional hypotheses restore matching: `s=2`
minimality with or without P17 Eq. (2), irreducibility of the internal
symmetry representation, a whole-symbol common cone, or something else.
Whether `c_strict^iso` saturates `r_in(C_micro)` for every admissible symbol
(saturation, charter Sec. 0(ii)) is a separate question and also remains
open.

At finite mass the two natural extraction procedures differ exactly. A common
relativistic coefficient is recovered in the specified continuum limit.
Additional equivalent representatives cannot resolve the open generality issue;
any successor gate must examine structural freedom under fixed causal geometry
and discrete isotropy.

**Update (2026-09-17, branch-local, frozen class of Sec. 8 only).**
`B_infty^*` matching in Sec. 4 is unchanged. What is now closed is the
**operational IR question** on the preregistered CJWW (5.15) protocol of
Secs. 8.16–8.20, not the matching hypothesis. In that class there is an
IR-controlled operational response outside the emergent cone, and it is
not a mere UV-propagator artefact:

`c_IR < v_micro` (already geometric for (5.15)) and
`IR probe → δ_B(N) ≠ 0` for large `N`, with
`δ_{M,M_B}(N) ∼ |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N}`
on the twelve Pauli pairs (Sec. 8.20). The signal is
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. This is theoretical step 3
of the physical line, closed inside the preregistered class. It is not
`D_B > 0` for every QCA, not a claim about nature, and not a further
signalling calculation. The authorized next front is Sec. 8.21.

## 7. GATE STATUS — only point (3) authorized by the user

**MASSLESS INRADIUS RIGIDITY GATE — COUNTEREXAMPLE_VERIFIED IN DECLARED s=4
CLASS (branch-local); s=2 and irreducible-R classes OPEN; point (3) ceiling
investigation separately chartered by direct user instruction.**
(Charter name kept for continuity; its comparison target is corrected, see
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0.) Where the charter or
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) still describe the
gate as having no counterexample, this section overrides them
(`PROJECT_INSTRUCTIONS.md` Sec. 2).

### 7.1 Superseded operative plan

The 2026-09-14 deliberation
([`debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md`](../debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md))
predates the s=4 result. It recommended freezing an `s=2` contract on `N_3`,
filtering candidates by non-nilpotent vertices, and escalating to `s>2` only
after exhausting that class. That order was not followed, and its
"rigidity vs saturation" framing cannot continue as written. It is kept as
historical decision material, not as a current plan. Its open point about
whether P17 Eq. (2) is derivable from the charter's identities still matters
for the `s=2` question.

### 7.2 Point (3) — direct user authorization, not a ratification

**Authorization (2026-09-16):** after the incomplete ratification, the user
explicitly instructed: "pues adelante, punto (3)". Accordingly,
`STRICT_CONE_CEILING_N3 = AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` under the
[frozen point-(3) contract](../theory/STRICT_CONE_CEILING_N3_GATE.md).
Its sole target is `c_0 <= c_strict^iso` in all directions, including
degenerate Floquet nodes and eigenvalue collisions in U^n. The contract
was frozen at `4135625` with initial scientific status **OPEN**. No L1,
defect-metric or other C step is authorized by this instruction.

**Point-(3) result (2026-09-16):**
`PROOF_COMPLETE_ONE_INDEPENDENT_ADVERSARIAL_REVIEW_PASS`;
`THEOREM_STATUS = PROVED_UNDER_FROZEN_CONTRACT`. The
[analytic report](../reports/2026-09-16--point-3-strict-cone-ceiling.md)
supplies a matrix-polynomial boundary bound, compression to the original
eigenspace, a direct directional-slope argument, and the exact support
limit. The author's assessment is `PASS_ANALYTIC` under the frozen
contract. The [independent adversarial review](../informe_adversarial_punto_3.md)
at `bd44122`, reviewing `db083af` against `4135625`, records
`ACCEPT_AS_WRITTEN`, with no mandatory repairs. One independent review is
complete; it is not a five-member ratification. The follow-up incorporates
its recommended sign control and expository clarifications without changing
the frozen quantifiers. The bound is proved for the admitted cones and the
exact support of the full symbol on N3, including degenerate Floquet nodes
and collisions of eigenvalues after taking powers. It does not establish a
sector-intrinsic or ballistic bound, or an extension to incommensurable
displacement sets. No numerical search or scientific script was run.
The full C gate is neither ratified nor closed;
L1 remains a manual candidate and the defect identity remains family-only.
The s=4 example refutes equality and is consistent with this ceiling.
**NOVELTY = OPEN.**

The 2026-09-16 ratification attempt is `ABORTED_OR_INCOMPLETE`: Gemini was
absent at launch; the process was interrupted without a final verdict. Three
first-round turns completed — ASTRA `PREFER_A`, CLAUDE OPUS `RATIFY_C`
conditioned on its own amendment (i), CIRO `RATIFY_C` — and ABNER's turn was
sent but never returned. That is neither a closed round nor five-member
ratification, so the status above is unchanged. The partial acta is archived
at [`2026-09-16--ratificacion-gate-completitud-axial-n3.md`](../debates/2026-09-16--ratificacion-gate-completitud-axial-n3.md);
the raw session log stays local and unversioned.

**Candidate from a degraded debate (2026-09-15):**
`GATE_COMPLETITUD_AXIAL_N3 = CANDIDATE_FROM_DEGRADED_DEBATE`, **not
authorized.** In the
[deliberation](../debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.md),
four members proposed `AUTHORIZE_C`. The tool classified the run as
`DEGRADED_NO_CONSENSUS`: ASTRA failed two turns (Codex usage limit) and was
excluded. ASTRA's recorded preference was A, and its objection that C reaches
`c_strict^iso` only through the still unproven bound `c_0 <= c_strict^iso`
was left unanswered. The earlier requirement of five-member ratification
has not been met. The later direct user instruction above authorizes only
point (3) under a separate contract; it does not authorize the full C gate
or convert either incomplete debate into consensus.

Research directions (only the point-(3) ceiling is now frozen):

1. **Surviving bounds.** Which inequalities between `c_0`, `c_strict^iso`
   and `r_in(C_micro)` hold for every admissible symbol? Currently
   `c_strict^iso <= r_in(C_micro)` is established. `c_IR <= r_in(C_micro)`
   is established only under the isotropic-containment premise of Sec. 3.3.
   `c_0 <= c_strict^iso` is proved under the frozen point-(3) assumptions,
   with one independent adversarial review PASS. Thus every admitted cone
   satisfies `0 < c_0 <= c_strict^iso <= 1/sqrt(3)`. Equality and microscopic
   saturation are not consequences of this ceiling.
2. **Restoring hypotheses.** Which explicitly stated extra assumptions (for
   example `s=2` minimality with or without Eq. (2), or an irreducible `R`)
   give `c_0 = c_strict^iso` for a whole declared class?
3. **Intra/inter rule.** Does the s=4 family identity reflect a general
   structure that accounts for the missing speed, or is it specific to this
   ansatz?

Every class must keep the quantifiers of charter Sec. 2 and be declared
**before** solving.

### 7.3 Original gate question (answered for the declared s=4 class)

The original question was whether another admissible massless symbol can have
`0 < c_0 < c_strict^iso` for its own strict asymptotic body, while preserving
the same `N`, `C_micro`, embedding, unitarity, homogeneity and discrete
isotropy as its selected standard baseline. A candidate whose `c_0 < r_in(C_micro)`
only because its own strict body already falls short of `r_in(C_micro)` is not
this counterexample; see the charter's Sec. 0 for the (i)/(ii) split.

**Erratum (2026-09-15).** Earlier wording here attributed such a shortfall to
a nilpotent one-step coefficient. What is established is only this: a
saturation failure `c_strict^iso < r_in(C_micro)` requires at least one
nilpotent vertex coefficient (contrapositive of the vertex lemma). The
converse is not established. A nilpotent vertex removes the exact ray `n.h`
from `S_n`, but it does not by itself determine `c_strict^iso`, which must be
computed. See the charter's erratum.

The [gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) requires the
internal dimension, isotropy group/action and representation, node/sector,
and any irreducibility assumptions to be explicit before solving. Do not
silently introduce minimality or weaken the symmetry when interpreting a result.

- One exact admissible counterexample refutes B_infty^* for a class containing
  it (realized for the declared s=4 class, Sec. 4.1).
- A rigidity claim requires an exhaustive analytic argument for an explicitly
  quantified class; failure to find a deformation is not such an argument.
- The absence of a continuous deformation alone does not exclude disconnected
  admissible symbols. A restricted proof leaves wider generality open.
- Prior-art classification assumptions must be checked before any novelty claim.

### Stop rule

Until a successor gate is chartered and closed:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO anisotropic-QCA detour**;
- **NO change of support, embedding, time normalization or discrete isotropy
  within a declared rigidity comparison**;
- **NO novelty claim for B*, B_infty^* or the s=4 family (NOVELTY = OPEN)**;
- **NO use of a scalar `v_max` without definition**;
- **NO promotion of the s=4 family identity to a general QCA law**;
- **NO reading of `c_strict^iso`, `r_in(C_micro)` or `S_min` as "the microscopic
  speed of the substrate"** (Sec. 8.6);
- **NO new novelty audit, Bernstein-rigidity, paraunitary-classification or
  d=3-theorem line** under the Sec. 8.7 scope decision;
- **NO directional/anisotropic `I(v)` computation** (Sec. 8.8, NOT_AUTHORIZED);
- **NO operational-invisibility or no-signalling claim** from a rate function
  (Sec. 8.8); that question requires its own charter.

A certified falsification within the frozen admissible class is a successful
gate outcome. The s=4 counterexample is such an outcome for its declared
class only. This branch-local reconciliation does not promote anything to
`main`. The only later successor authorization is the point-(3) contract
in Sec. 7.2, by direct user instruction.

## 8. Directional causal saturation — canonical physical interpretation (2026-09-16)

**Evidence commit:** `2494192`.
[Report](../reports/2026-09-16--directional-causal-saturation.md),
[verifier](../scripts/verify_directional_saturation.py) (15/15, fail-closed,
fourteen exact).

The active physical question is: **does `c_IR` coincide with the microscopic
causal boundary of the discrete substrate?** The canonical answer is
**direction-dependent; in general, no.**

### 8.1 Three objects, never identified

For the two 3D finite-range walks of CJWW `sources/2408.02108v1.pdf`,
Eqs. (5.12) and (5.15):

`B(c_IR) ⊆ Γ ⊆ C_micro`,

- `B(c_IR)`: the emergent isotropic IR light cone;
- `Γ`: the ballistic / group-velocity propagation body;
- `C_micro = conv F`: the strict microscopic causal body of the finite step set `F`.

`Γ ⊆ C_micro` is general (CJWW Lemma 4.1: the rate function is `+∞` outside
`conv F`). `B(c_IR) ⊆ Γ` is **not** general and is asserted here only for these
two walks; CJWW Sec. 5.3 exhibits a non-convex `Γ`, so no convexity of `Γ` may
be assumed.

### 8.2 The canonical saturation function

For both walks `C_micro = [-1,1]^3`, hence for `||n̂||_2 = 1`

`v_sub(n̂) := h_{C_micro}(n̂) = ||n̂||_1`,

and, in the normalization `c_IR = 1`, the canonical directional saturation
function is the **support-function ratio**

`S(n̂) := h_{B(c_IR)}(n̂) / h_{C_micro}(n̂) = 1/||n̂||_1`.

`S(n̂) = 1` only for the six axial directions `n̂ = ±e_i`; `S(n̂) < 1` for every
non-axial direction, with `S_min = S((1,1,1)/sqrt(3)) = 1/sqrt(3)`.

`S_min` is a **descriptive scalar summary only**. The full directional function
`S(·)` is the canonical object. No scalar separates the two walks: `c_IR/r_in`
is `1` and `S_min` is `1/sqrt(3)` for both; their difference lives in `Γ`.

### 8.3 Walk (5.12)

`B(1) ⊊ Γ_1 ⊊ [-1,1]^3`, with `sup|∇ω| = sqrt(3/2) > c_IR`, attained exactly at
`p = (-π/4,-π/4,-π/4)`. This walk contains finite-momentum ballistic modes
faster than the emergent IR light speed while remaining inside `C_micro`.
`Γ_1 ⊆` tricylinder is exact (SOS identity); the reverse inclusion is numerical.

### 8.4 Walk (5.15) — the clean counterexample

`Γ_2 = B(1) ⊊ [-1,1]^3`, with `sup|∇ω| = c_IR = 1`.

This refutes the identification

`sup|v_g| = c_IR  ⟹  IR light cone = microscopic causal boundary`.

Even when **all ballistic propagation respects `c_IR`**, the substrate permits
causal propagation outside the relativistic ball in non-axial directions.

**Evidence tags, not to be merged.** `sup|∇ω| = c_IR = 1` and
`Γ_2 ⊆ B(1)` are **ESTABLISHED (exact SOS certificate**
`(1-f²) - |∇f|² = s₂²s₃² + s₁²s₂²c₃² + s₁²c₂²s₃²`**)**, and `∂B(1) ⊆ Γ_2` is
exact from the conical point. That `Γ_2` also fills the open ball is
**SUPPORTED (numerical)** only. The counterexample does **not** depend on that
last half: it needs only `sup|v_g| = c_IR`, which is exact.

### 8.5 The gap is not a one-step artefact

At the eight vertex rays a single lattice path contributes, so
`(W^n)_{nσ} = (W_σ)^n`. Each `W_σ` has rank 1 with nonzero trace, hence
`(W_σ)^n = tr(W_σ)^{n-1} W_σ ≠ 0` **for every `n ≥ 1`** (exact). Therefore
`h_infty = h_{C_micro} = ||·||_1` exactly, and the distinction between `Γ` and
`C_micro` is not an artefact of a one-step support bound.

Between `Γ` and `C_micro`, propagation is non-ballistic and may be exponentially
suppressed; it is **not generically causally forbidden**. **No claim is made
that every point of this intermediate region has nonzero amplitude** — what is
proved is the statement about the vertex rays.

### 8.6 Scope correction to earlier scalar summaries

`c_strict^iso` and `r_in(C_micro)` remain mathematically valid summaries where
previously proved (Secs. 4, 6, 7), but **must not be interpreted as "the
microscopic speed of the substrate."** The microscopic causal boundary is
anisotropic and is represented by `C_micro`, equivalently by `h_{C_micro}(n̂)`.

Under (i) finite `F`, (ii) `d ≥ 2` and (iii) an isotropic IR cone, exact
equality `B(c_IR) = C_micro` is impossible, because `C_micro` is a finite
polytope and the IR body a Euclidean ball. This restates `B_full` (Sec. 3.3)
with its hypotheses made explicit; relaxing (i), (ii) or (iii) leaves it open.

### 8.7 Scope decision

The physical relation **emergent relativistic cone vs microscopic causal
body** remains the line. As of 2026-09-17, inside the frozen IR class of
Secs. 8.16–8.20, theoretical step 3 of that line is **closed**: the gap
is not only geometric (`c_IR < v_micro`) but operational
(`IR probe → δ_B(N) ≠ 0` for large `N`, nonperturbatively suppressed;
Sec. 8.20). No further signalling gate is authorized.

The live front is whether that structure can correspond to something in
nature (Sec. 8.21, `NOT_EXECUTED`), not another calculation of `C` and
not yet a laboratory implementation of the walk (fork 4A, identified,
not chartered).

**Not authorized by this result:** further search for mathematical novelty,
Bernstein rigidity, paraunitary classification, or a new dimension-3 theorem.

The previous novelty / Gate-C material is retained as historical project state
and is **not an active prerequisite** for the physical line. Sec. 7 is unchanged
and still governs anything done under the point-(3) contract.

### 8.8 LDP_RADIAL_INTERPRETATION — PASSED, subline CLOSED (2026-09-16)

**Status: `DOCUMENT_EXISTING_RESULT` — PASSED. This subline is CLOSED.**
Contract: [`OPERATIONAL_INVISIBILITY_GATE.md`](../theory/OPERATIONAL_INVISIBILITY_GATE.md).
A first freeze at `a9e611a` chartered the *directional* variant; it was narrowed
by user instruction before any solving and is **SUPERSEDED, UNSOLVED** — nothing
may be cited from it.

For walk (5.15), CJWW's own radial rate function Eq. (5.21),
`R̃(ℓ) = 2 arccosh(cosh(ℓ/2√3)³)`, has exactly the two slopes

`R̃'(0) = 1 = c_IR`   and   `R̃'(∞) = √3 = max_n̂ v_sub(n̂) = v_sub(body diagonal)`,

so by Legendre duality `Ĩ(r) = 0` for `r ≤ 1`, `0 < Ĩ(r) < ∞` for `1 < r < √3`,
and `Ĩ(r) = ∞` for `r > √3`, reproducing CJWW's control value `Ĩ(1.1) ≈ 0.104`.
Three regimes, with boundaries at precisely the two numbers Sec. 8 canonizes:

**ballistic/emergent | causal but exponentially suppressed | causally forbidden**

**ESTABLISHED (exact).** The *value* of (5.21) at CJWW's stated maximizer is
exact; the *location* of that maximizer is their numerical finding, not ours.

**Declared limitations, not to be dropped.**
- `Ĩ` is radial and demonstrably coarse. Since `v_sub(ê_i) = c_IR`, a velocity
  `r ê_i` with `r > 1` is already outside `C_micro`, where the amplitude is
  **exactly zero**, not suppressed. The finite rate `Ĩ` reports for `1 < r < √3`
  is therefore carried by non-axial directions only. The angular structure of
  `I(x)` is **not resolved**.
- Upper bound only; CJWW prove no lower bound.
- It bounds the position distribution of one particle, nothing else.

**Non-implication, explicit.** This does **not** yield an operational-invisibility
or no-signalling theorem. At QCA level an exponentially small tail still lies
inside the exact causal support, so "operationally invisible" may not be
asserted. That question needs resources, distinguishability or channel capacity
defined first, changes problem class, and merits an independent charter.

**NOT_AUTHORIZED:** anisotropic/directional `I(v)`; probability vs signalling.

(For the canonical conclusion of Sec. 8 as a whole, see Sec. 8.9.)

### 8.9 Canonical conclusion — stated at the right logical level

Earlier wording here read "`c_IR` **can** be the boundary of typical macroscopic
propagation without coinciding with the microscopic causal boundary". That is
modal, and too weak: this is not a possibility claim but an **explicit
counterexample**. Corrected, and canonical:

**(i) Existence — PROVED (exact).**

> There exists at least one local, unitary, finite-range model in 3D — the
> one-particle translation-invariant walk of CJWW Eq. (5.15) on `Z^3`, internal
> space `C^2`, jump length 1 — in which **all** ballistic propagation satisfies
> `|v_g| ≤ c_IR`, while the microscopic causal region is **strictly larger**
> than the emergent relativistic cone:
>
> `sup|v_g| = c_IR`  **and**  `B(c_IR) ⊊ C_micro`.

Both halves are exact: `sup|v_g| = c_IR = 1` by the SOS certificate of Sec. 8.4,
and `B(c_IR) ⊊ C_micro = [-1,1]^3` with `v_sub(n̂) = ||n̂||_1` reaching `√3 c_IR`
on the body diagonals, certified at every vertex ray for every `n` (Sec. 8.5),
hence not a one-step artefact. This statement does **not** rest on the
numerically supported half of `Γ_2 = B(1)`.

**(ii) Logical consequence — PROVED in the class studied.**

> `c_IR = sup|v_g|  ⇏  B(c_IR) = C_micro`.
>
> Equivalently: the equality "`c_IR` = microscopic causal limit" is **not a
> necessary consequence of relativistic emergence**.

**(iii) Explicitly NOT established — UNKNOWN.**

> `c_universe < ` the fundamental causal limit of our universe.

No evidence is offered here in either direction. This project makes **no claim
about our universe**; asserting (iii) from (i)-(ii) would be a category error,
since (i) is an existence result inside a declared model class.

### 8.10 SUBSTRATE_CONE_OBSERVABILITY — PASSED, gate CLOSED (2026-09-16)

Contract [`SUBSTRATE_CONE_OBSERVABILITY_GATE.md`](../theory/SUBSTRATE_CONE_OBSERVABILITY_GATE.md)
frozen at `d86b018` before solving;
[outcome](../reports/2026-09-16--substrate-cone-observability.md). This lifts
the Sec. 8.8 `NOT_AUTHORIZED` for the signalling question only.

The question was operational: for `ct < L < v_sub(n̂)t`, is `D = 0` or `D > 0`?
It is **undefined** for the one-particle walk, so the gate declared a
free-fermion (CAR) lift. On the one-particle sector `α_t(n_x) = W^t P_x W^{t†}`,
so `[α_t(n_x), n_y]` has `(y,y')` block `(W^t)_{y,x}((W^t)_{y',x})†` and is
nonzero exactly when the single-particle kernel is. **The operational causal
structure of the lift is the strict support of `W^t`** — the object already
certified in Sec. 8.5.

**Answer: `D > 0`, exponentially small, strictly off-axis.** Exactly zero for
`L > v_sub(n̂)t` (H4); nonzero `∝ 4^{-t}` at the vertex rays for
`ct < L < v_sub(n̂)t` (H2); **exactly zero in the six axial directions** for
every `L > ct`, since `v_sub(ê_i) = c` (H3). At `t = 3`, 108 of the 148
populated sites lie strictly outside `B(c)t`, all inside `C_micro t`, none
axial. **ESTABLISHED (exact, Gaussian-integer kernels).**

This is the signature sought: fundamental causality outside the light cone with
no superluminal ballistic propagation, carrying the angular fingerprint
`v_sub(n̂) = ‖n̂‖₁ c`.

**Limits.** Statements are about the lift, not the one-particle walk. A nonzero
commutator means *there exists* an intervention and a state with `D > 0`; no
specific protocol's `D` and no channel capacity were computed. How the
suppression varies across `C_micro \ B(c)` is the anisotropic `I(v)` question,
still `NOT_AUTHORIZED`. No claim about our universe: Sec. 8.9(iii) stands at
UNKNOWN, and a wider cone fully decoupled from accessible observables would be
invisible to any experiment, so no null result can establish exact coincidence.
No experimental or LIV constraint survey is authorized.

### 8.11 EMPIRICAL_SUBSTRATE_CONE_SURVEY — COMPLETE (2026-09-16)

Contract [`EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md`](../theory/EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md)
frozen at `416dde1`;
[outcome](../reports/2026-09-16--empirical-substrate-cone-survey.md).

**Declared premise (computed before surveying).** With `t` in lattice steps, a
Planck-scale substrate puts this model's own effect at `10^(-8.4e41)` over one
second, against finest-ever bounds of `10^-20` to `10^-30`. The model's effect is
**unobservable in principle**. The survey is therefore model-independent. The
geometric window is by contrast not small: it reaches `√3 ct`, 73% beyond the
light cone.

**Verdict, in three levels.**

| | |
| --- | --- |
| Scalar no-signalling | experimentally tested, to finite precision |
| Directional causal tail of Sec. 8.10 | no specific localized operational test |
| Exact equality `C_fundamental = B(c)` | **not established** by null results |

In contract categories: `DIRECT_CONSTRAINTS_FOUND` for the scalar variable,
`NO_CURRENT_OPERATIONAL_TEST` for the directional structure.

**Missing coupling map — the real obstacle.** `[A(t),B] ≠ 0` gives `∃` a state
and intervention with `D > 0`; it does **not** give that a standard Bell-test
protocol is that intervention. Converting a bound on Bell marginals into a
quantitative bound on the tail needs a coupling/protocol map — which observable
realizes `A`, which realizes `B`, which preparation exploits the commutator.
None exists. The scalar bound therefore constrains the right *kind* of variable
without being convertible into a number about our `D`.

**Withdrawn.** An earlier phrasing used Adenier–Khrennikov to fix the empirical
level at "percent-to-permille". That was an overreach: it is a contested
reanalysis of one dataset, not a universal bound nor a calibrated interval for
`D`. No numerical empirical level is claimed. Likewise "essentially untested" is
replaced by the exact-equality statement above.

**Category error recorded, the survey's main result.** Salart 2008 (`v > 10⁴ c`)
and Bancal 2012 (finite-speed influence ⟹ superluminal signalling) constrain
models where the superluminal influence *explains* the quantum correlations. The
tail of Sec. 8.10 is non-explanatory, so those bounds do **not** apply to it;
using them to "exclude" it would be a category error. LIV/dispersion/threshold
limits are `INDIRECT_ONLY` by contract Sec. 2.1, since Sec. 8 proves
`sup|v_g| = c` is compatible with influence outside `B(c)`. Lieb–Robinson
experiments (Cheneau 2012 and successors) **observe** this structure in
engineered lattices: realizability, not a constraint on nature.

**Consequence, and the firm epistemological point.** No finite sequence of null
results can prove `D = 0` exactly; it can only yield ever smaller upper bounds.
A reproducible positive result outside `B(c)` could falsify the identification
of `c` with the fundamental causal boundary. Sec. 8.9(iii) stands at UNKNOWN.

**Next step if the line continues (not opened).** Not a further theoretical
front, and not a generic FTL search: design the experiment that **maximizes `D`**
for a Sec. 8.10-type tail — which two local operations, which spacelike
separation, which remote observable optimally exploit an exponentially small,
anisotropic causal tail. Only afterwards does it make sense to ask whether an
existing experiment already did this accidentally, and by how much it falls
short. This is the coupling map above, and it is **not chartered**.

### 8.12 COUPLING_MAP_OPTIMAL_D — PARTIAL; exact signalling witness CLOSED (2026-09-16)

Contract [`COUPLING_MAP_GATE.md`](../theory/COUPLING_MAP_GATE.md) frozen at
`0f7628d`: frozen Sections 0–6 unchanged, outcome corrected;
[report](../reports/2026-09-16--coupling-map.md).

**Correction authorized by the user, 2026-09-16.** The former conditional H1
confirmation, universal linear/quadratic scaling and claimed restricted
optimal-D upper bound are withdrawn. The code computed an occupation
witness, not full trace-distance optimization. Four finite times cannot
establish asymptotic scaling; moreover `t = 5` exceeded the frozen `{2,3,4}`.
The historical ratios remain descriptive only. H1 is **OPEN**; H2 establishes
preparation dependence for the specified protocol, not necessity of coherence
for all admissible interventions. **H3 and H4 remain NOT REACHED**.

**Finite existence task: EXISTENCE_WITNESS_PROVED / INDEPENDENTLY_REVIEWED.** The user's
subsequent instruction chartered closure as a theorem/witness, not further
optimization or an experimental study. See
[`COUPLING_MAP_SIGNALING_WITNESS.md`](../theory/COUPLING_MAP_SIGNALING_WITNESS.md).
At `t = 2`, Alice at `0`, Bob at `y = (2,2,2)`, prepare
`(|0,down> + |y,down>)/sqrt(2)` before Alice chooses between `I` and
`exp(i pi n_0)`. Bob measures the even non-vacuum projection at his site.
The exact probabilities are

`p_0 = 121/512`, `p_1 = 169/512`, `Delta p_B = 3/32 > 0`, hence **`D >= 3/32`**.

The theorem fixes the existing CAR/Heisenberg convention, the state,
intervention, measurement and spacetime point. The exact kernel is nonzero
there: Bob is outside the emergent ball and **on the microscopic boundary**.
This proves membership in the exact causal support, not strict interior
membership. Each local site has two modes; the original `N = M = 1`
optimization is not closed. The
[verifier](../scripts/verify_signaling_witness.py) passes **17/17 exact checks**.
The [independent review](../reports/2026-09-16--signaling-witness-independent-review.md)
returns **PASS on the four requested points, no mandatory repairs**: analytic
probabilities, code correspondence, causal location, and the convention
`D = (1/2)||rho_1-rho_0||_1`. It records hashes of the unchanged reviewed
theorem and both scripts. This is one separate agent's independent review,
not external human review, consensus, or a full PASS of the optimal-D gate.

**Claim ceiling, branch-local:**

> In this free-fermion lift, given a state prepared with coherence between
> Alice and Bob's own site before Alice's choice, that local choice changes
> a measurement probability accessible
> to Bob outside the emergent relativistic cone and within the exact
> microscopic causal support. The choices are distinguishable in principle.
> Preparation of this operational channel from resources initially localized
> around Alice, Bob's optimal measurement, a globally optimal protocol and
> experimental feasibility are not established.

**Superseded clause, 2026-09-16.** The requirement of a resource already
distributed before Alice acts is no longer open: Sec. 8.13 exhibits a
*different* channel, in the same model, driven from a particle initially at
Alice alone. That successor does **not** supply a preparation protocol for
*this* channel, whose theorem, review and ceiling above are unchanged.

**Controls and limits.** For an Alice-localized particle the phase gate gives
only a global phase, hence exactly zero signal. Removing spatial coherence
also removes this protocol's signal. At the axial control the exact zero
kernel excludes Alice from the evolved Bob algebra, hence forbids signalling
for any initial state under even local Alice unitaries. By contrast, a zero
occupation witness alone never certifies `D = 0`.

The second coherent arm in this construction is **at Bob's initial site**;
the earlier hint excluding Bob from the resource is withdrawn. No Bell
protocol has been modelled. The finite interference term involves both
`K_0y` and `K_yy` with their internal alignment, not a universal asymptotic
law in one kernel. The empirical transfer of Sec. 8.11 remains unresolved;
the experimental problem is not opened. No claim about our universe follows.

**The original question, split.**

| Question | Answer |
| --- | --- |
| Theoretical: must `c` coincide with the substrate's causal limit? | **No** — (ii), proved |
| Physical: does it coincide in our universe? | **Unknown** — (iii) |

### 8.13 ALICE_LOCAL_PREPARATION_SIGNALING_WITNESS_PROVED / INDEPENDENTLY_REVIEWED (2026-09-16)

Successor to Sec. 8.12, chartered by direct user instruction as an
**existence question only**: does the signalling channel require a resource
that is already spatially distributed before Alice acts? **It does not.**
See [`ALICE_LOCAL_PREPARATION_WITNESS.md`](../theory/ALICE_LOCAL_PREPARATION_WITNESS.md)
and the [construction report](../reports/2026-09-16--alice-local-preparation.md).

Same unchanged CAR lift of CJWW (5.15), same conventions. At `T = 0` the
resource is exactly one particle, `|0,down>`, with every other mode vacant.
Between `T = 0` and `T = 2` **only the declared free dynamics acts**, equally
for both messages: the prepared state is `chi = S^2|0,down>`, given in closed
form by Cayley-Hamilton (`S^2 = 2fS - I`, `f = cos p1 cos p2 cos p3`), with
38 populated sites, `||chi|| = 1`, `chi(0) = -3 down/4` and
`||P chi||^2 = 9/16`, `||Q chi||^2 = 7/16`. Alice encodes at `A = (2,0)`
with `I` or `exp(i pi n_0)`; Bob measures the even non-vacuum projection at
`B = (3,(1,1,1))`. The exact probabilities are

`p_0 = 49/1024`, `p_1 = 25/1024`, `Delta p_B = 3/128 > 0`, hence **`D >= 3/128`**.

**Causal origin — the load-bearing step.** The bit is exogenous at `T = 2`.
Both conditional histories are *identical operators on the whole Fock space*
for `T = 0, 1, 2^-`, so the mutual information between the bit and any
pre-choice observable is exactly zero and no earlier encoding exists. Bob's
own site is **exactly vacant** at the encoding event (`chi(1,1,1) = 0`).
Comparing cones from `T = 2` is therefore the appropriate operational
reference for communication. From the encoding event,
`|y_B| = sqrt(3) > c_IR Delta T = 1` while `||y_B||_inf = 1` and
`K_1(0,y_B) = diag(0,1/4) != 0`: Bob is outside the emergent cone and on the
**boundary of the exact microscopic causal support**. **No microscopic
causality bound of the model is violated.** It is explicitly *not* claimed
that Bob is outside the emergent cone of the initial event: from `T = 0`,
`sqrt(3) < 3`.

**Claim ceiling, branch-local:**

> A particle initially localized at Alice alone suffices. The ordinary
> microscopic dynamics generates the required spatial coherence before the
> message is chosen. A later local choice by Alice then changes a Bob
> statistic one step afterwards, with Bob outside the emergent causal cone
> of **that encoding event** and within the microscopic causal support.
> This is not a violation of the model's microcausality. Optimality,
> minimal preparation time, experimental feasibility, asymptotics, capacity
> and any claim about our universe are **not** established.

**Evidence.** `verify_directional_saturation.py --local-preparation-only`
passes **21/21 exact checks**; the frozen witness verifier still passes
17/17 and the default suite 27/27, unchanged. The
[independent review](../reports/2026-09-16--alice-local-preparation-independent-review.md)
returns **PASS, no mandatory repairs**, and explicitly covers the item most
exposed to adversarial attack: the closed-form derivation of `S^2|0,down>`
and the identity of the two pre-choice histories. It reconstructs the
prepared state from a separately transcribed symbol, records SHA256 hashes of
every reviewed input, and confirms the script change is one added function
plus a CLI dispatch, with the frozen witness path untouched. This is one
separate agent's independent review — **not** external human review,
multi-member consensus, or ratification.

**Relation to Sec. 8.12.** The hypothesis is strictly weaker (no pre-existing
Alice-Bob coherence) and the geometry differs (one readout step to
`(1,1,1)`, not two to `(2,2,2)`); the signal is smaller, `3/128` against
`3/32`. This does **not** retroactively supply a preparation protocol for the
Sec. 8.12 channel, whose frozen theorem and review keep their exact bytes and
scope. The optimal-D gate stays **PARTIAL**; H1 stays **OPEN**; H3 and H4 stay
**NOT REACHED**. The experimental problem remains unopened, by instruction.

### 8.14 NONCORNER_SIGNALING_CONSTRUCTED / INDEPENDENTLY_REVIEWED (2026-09-17)

Successor to Sec. 8.13, executed under the frozen
[`NONCORNER_SIGNALING_GATE.md`](../theory/NONCORNER_SIGNALING_GATE.md): the
Alice-local preparation channel is **not** confined to the vertex
`(1,1,1)`. The [corrected execution report](../reports/2026-09-16--noncorner-signaling-gate.md)
and its [independent review](../reports/2026-09-16--noncorner-signaling-gate-independent-review.md)
are frozen together here. The review verdict is **PASS with three mandatory
textual repairs (`MR1`--`MR3`)**, all applied to the report; none changes a
computed quantity or the scientific verdict.

The exact one-step kernel support gives precisely four admissible non-vertex
sites, `y = (+/-1,+/-1,0)`, and the preregistered construction succeeds at
all four. At each site,

`M(y) = diag(-3/256,0) != 0`,
`p_0 = 25/1024`, `p_1 = 49/1024`, and `Delta p_B = 3/128`.

The reduced-state trace distance is exactly `D = 3/128`, so the exhibited
projection saturates the distinguishability bound for each computed pair of
states. This is pairwise measurement optimality only; it is not protocol,
preparation, site or intervention optimality. The result refutes
vertex-exclusivity for this protocol at `Delta T = 1`; it says nothing about
`Delta T = 2`, other vertices, asymptotic scaling, capacity, experimental
feasibility or our universe. No violation of the model's microscopic causal
bound is claimed.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NONCORNER_SIGNALING_CONSTRUCTED /
  INDEPENDENTLY_REVIEWED` in the exact scope above.
- **Software certificate: PASS with six externally verified properties not
  yet encoded as checks.** The run
  `verify_directional_saturation.py --noncorner-gate-only` passes **20/20
  exact checks**, but that count **is not by itself an exhaustive certificate**
  of the six properties listed in the execution report Sec. 8. They were
  independently checked by the reviewer. They remain recorded certification
  debt, not gaps in the scientific result.

The reviewed script is deliberately unchanged after review. Encoding those
six additional checks would alter the reviewed artefact and therefore require
a new review of that file. The earlier frozen contracts and witnesses retain
their bytes and scope; the optimal-D gate remains **PARTIAL** and no
experimental-design gate is opened here.

### 8.15 PHYSICAL_DIMENSIONAL_TRANSLATION — CLOSED / CONDITIONAL (2026-09-17)

Contract
[`PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md`](../theory/PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md)
frozen at `fca5881` before solving; see the
[dimensional audit](../reports/2026-09-17--physical-dimensional-translation-audit.md).

**Verdict: `DIMENSIONAL_MAP_CONDITIONAL`.** The source conventions support the
symbolic restoration

`x = a n`, `t = N tau`, `k = p/a`,
`E = hbar omega/tau (mod 2 pi hbar/tau)`, and
`v_phys = (a/tau) grad_p omega`.

Hence `c_IR^phys = a/tau`. Identifying it with an observed `c_phys` imposes
`a = c_phys tau`; it does not determine either absolute scale. The model and
checked sources specify no numerical `a` or `tau`, and the earlier Planck-scale
calculation was explicitly conditional, not a scale derivation.

For the frozen non-corner witness, conditionally on `(a,tau)`, the
encoding-to-readout interval is `tau` and Bob is at Euclidean distance
`sqrt(2)a`. If `a/tau = c_phys`, then the scale-free ratio is
`L/(c_phys tau) = sqrt(2)`: outside the emergent cone and inside the exact
one-step microscopic support, exactly as in lattice units.

The value `3/128` acquires **no units**. It remains the exact probability
difference and trace distance for the two idealized local states. It is not an
energy, rate or dimensional coupling. The exactly localized preparation is
broad over the full Brillouin zone, not a low-energy narrow-band state, so no
unique physical energy or momentum can be assigned from the IR dispersion.

**Claim ceiling.** A consistent conditional dictionary is established; a
parameter-free prediction in SI units is not. Absolute cutoff scale, physical
realization/coupling, efficiencies, noise, feasibility and any identification
with nature remain unspecified. No experiment was designed and `Delta T = 2`
was not opened.

### 8.16 NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`NARROW_BAND_SIGNALING_GATE.md`](../theory/NARROW_BAND_SIGNALING_GATE.md)
preregistered at `817050d` before any computation. Three artefacts are frozen
together at `778a44a`, through the provenance chain `5f6d350` -> `f00f64e` ->
`778a44a`:

- the [execution report](../reports/2026-09-17--narrow-band-signaling-gate.md);
- its exact certificate
  [`verify_narrow_band_gate.py`](../scripts/verify_narrow_band_gate.py);
- the [independent review](../reports/2026-09-17--narrow-band-signaling-gate-independent-review.md).

The question was whether the Alice-local signalling mechanism admits an
IR-controlled version with a preestablished narrow-band resource. The frozen
class is:

- node `p = 0`, both Weyl branches;
- `g(q) = (1-|q|^2)^2_+` supported on `|p| <= Lambda`, with
  `0 < Lambda < pi/4`;
- spin `down` and two common steps;
- the point gate `U_1 = exp(i pi n_0)` at the origin;
- Bob at `(1,1,0)`, with `Delta T = 1`.

**Verdict.** The Sec. 7 stop rule fires at the first control, before any signal
in Bob is computed: the point encoder is incompatible with the preregistered
relative IR criterion. Let `kappa = Lambda^3/(6 pi^2)`, the in-band share of
any one-site vector, and `s = ||P_0 psi_Lambda||^2`, with `0 < s <= kappa`. Then

`||Delta_Lambda||_1 = 4 sqrt(s(1-s)) -> 0`,
`eta_enc = ||Delta - Pi Delta Pi||_1/||Delta||_1 = sqrt((1-kappa)(1-3s(1-kappa))/(1-s))`.

So `eta_enc > 2 sqrt(6)/5` on the whole chart and `eta_enc -> 1`, while the
absolute leakage `epsilon_UV = 4s(1-kappa)` also tends to zero. The residual
outside the IR-IR block is dominated by the IR-UV and UV-IR coherences; the
UV-UV block is relatively `O(sqrt s)`. This is **not** a statement that the
encoding, the information or any signal is UV.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS /
  INDEPENDENTLY_REVIEWED`, in the exact scope below.
- **Review metadata.**
  - Cold independent agent review: PASS, after the mandatory repairs R1-R4 and
    MR1, all textual and all applied.
  - Human review: PASS.
  - No external peer review / no external replication yet.
  - Two earlier same-session adversarial reviews are archived as secondary,
    non-independent records. The self-review contains errors that the
    independent review corrected.
- **Software certificate: PASS, 34/34 exact checks.** The count covers only
  the identities and limits marked [V] in the report. The analytic steps listed
  in report Sec. 12 are not encoded as checks; the independent reviewer
  verified them by hand. They are recorded certification debt, not gaps in the
  result. The certificate imports `verify_directional_saturation.py`, which
  requires numpy, pinned in `scripts/requirements.txt`.

**Claim ceiling.** The result holds only for the frozen class and the Sec. 7
criterion.

- `D_B` was not computed, and `D_B = 0` is not asserted.
- It does not refute `3/128`, either at the vertex or at the non-corner sites.
  The non-corner witness uses the same `y_B = (1,1,0)`, but with an exactly
  localized resource and no IR criterion.
- It is no impossibility result for other encoders (extended, smoothed or
  `Lambda`-dependent gates), for resources without exact spectral support, for
  other notions of IR control, for other QCA, or for the physical continuum.
- `Lambda -> 0` is not `a, tau -> 0`, and no physical scale is set
  (Sec. 8.15).

**Erratum, charter header.** Lines 3-7 of the charter are pre-publication
text. They cite drafting base `HEAD=11efe1f` and scientific remote `780ecb0`,
state `NOT_EXECUTED / OUTCOME_OPEN`, and say that publication and execution
are pending. All of that is superseded: the charter was published at
`817050d`, executed, and frozen at `778a44a` with the status recorded in this
section. The charter deliberately keeps its bytes, for two reasons:

- its sha256 `3d559ced...` is pinned by the frozen certificate (check 1)
  and recorded in the report, the independent review and the freeze
  commits;
- contracts in this repository keep their pre-execution text, as
  `NONCORNER_SIGNALING_GATE.md` does.

The header was never part of the scientific contract (Secs. 1-15), which
is unchanged. `Delta T = 2` and the experimental problem remain unopened.

### 8.17 OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`SCALED_IR_SIGNALING_GATE.md`](../theory/SCALED_IR_SIGNALING_GATE.md)
preregistered at `31b5797` before any computation. Successor of Sec. 8.16,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--scaled-ir-signaling-gate.md);
- its exact certificate
  [`verify_scaled_ir_gate.py`](../scripts/verify_scaled_ir_gate.py);
- the [independent review](../reports/2026-09-17--scaled-ir-signaling-gate-independent-review.md).

The question is the disappearance law of Bob's distinguishability when
regions of size `O(1/Lambda)`, a margin `O(1/Lambda)` outside the emergent
cone of Alice's whole region, and time `O(1/Lambda)` are scaled together
(`N = Delta T = 1/Lambda`, Euclidean balls of radius `N/4`, frozen internal
families). A signal at fixed `Delta T`, or with an `O(1)`-site margin, does
not answer it.

**Verdict.** `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The eight frozen operations are IR-admissible. There is a directional
exponential upper bound, independently re-derived, for every one-particle
state and every unitary supported on `A_N`:

`δ_{M,M_B}(N) ≤ D_B(N) ≤ 36 N^4 exp[-(1 - √3/2)(log 2) N]`, `N ≥ 2`,

with `J = (1 - √3/2) log 2 > 0`. This **excludes**
`IR_RESOLVABLE_SIGNALING_POLYNOMIAL` in the frozen class and **does not
authorize** `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. All sixteen pairs
remain `OPEN_PAIR`: no positive lower bound, no proven vanishing, no
non-vanishing amplitude. `D_B = 0` is not asserted. The independent review
attacks specifically the three load-bearing steps named before promotion
(the geometry-to-kernel derivation of `J`, uniformity of `36 N^4`, and
polynomial exclusion without an existence claim) and returns **PASS**, with
no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with a one-sided quantitative bound.**
  `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`, in the exact
  scope below.
- **Review metadata.**
  - Cold independent agent review: PASS. No mandatory repairs. The three
    recommended drafting clarifications (`D_B = (1/2)||ρ1-ρ0||_1`;
    off-diagonal of the ellipse matrix; Schur diagonal operator-norm) were
    applied to the execution report at freeze. They change no quantity and
    no classification. Execution-report sha256 before/after those phrases:
    `4876ecab…` / `86a086dc…`. The CAR bound (DF) is not part of the frozen
    claim for the sixteen pairs.
  - Human freeze authorization: the 2026-09-17 instruction to freeze this
    status if the cold review passed, then to publish with those
    clarifications and without additional science.
  - No external peer review / no external replication yet.
- **Software certificate: PASS, 53/53 exact checks.** The count covers only
  the identities and limits marked [V] in the execution report. The
  analytic steps for `J`, `T_N`, `(D1)` and the classification were
  re-derived by the independent reviewer; they are not encoded as checks.

**Claim ceiling.** The result holds only for the frozen scaled class
(Euclidean balls, `α = 1/2`, `θ = π/2`, the declared internal families,
CJWW (5.15) in the one-particle sector).

- Any allowed effect in this class is at most `O(N^4 e^{-JN})`. That is a
  one-sided, model-falsifiable bound. It is not a two-sided prediction and
  not an existence result.
- Polynomial IR-resolvable signalling is discarded **in this
  geometry/class**. If a positive signal exists, it is at most
  nonperturbatively small. Existence is not claimed.
- The bound does not refute `3/128`, the vertex or non-corner witnesses, or
  the narrow-band negative (Sec. 8.16).
- `N → ∞` is not `a, τ → 0`. No physical scale is set (Sec. 8.15). An
  `e^{-JN}` law would translate only conditionally to a form
  `e^{-J' λ/a}`, with no numerical prediction.
- The internal families are not exhaustive. `M = a I + b·σ` in general is
  not covered. `I` is `REFERENCE_CONTROL` only.
- No new encoder is authorized. The cancellation analysis of the sixteen
  pairs is Sec. 8.18. The regional exponential rate is Sec. 8.19. The
  remaining bottleneck is the integrated Laplace coefficient
  (Hessian, profiles, spin, interference with the free tail `r`), not
  yet chartered.

`Delta T = 2` and the experimental problem remain unopened.

### 8.18 OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`LOWER_BOUND_NO_CANCELLATION_GATE.md`](../theory/LOWER_BOUND_NO_CANCELLATION_GATE.md)
preregistered at `1717d5e` before any computation. Successor of Sec. 8.17,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--lower-bound-no-cancellation-gate.md);
- its exact certificate
  [`verify_lower_bound_no_cancellation_gate.py`](../scripts/verify_lower_bound_no_cancellation_gate.py);
- the [independent review](../reports/2026-09-17--lower-bound-no-cancellation-independent-review.md).

**Verdict.** `OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The unique-path vertex

`(S^N)_{(N,N,N),0} = 4^{-N} |↓⟩⟨↓|`

exists and cannot be promoted to a regional leader (`K = log 4`, kills
`↑`, coherent regional sum). The Euclidean minimum of `|y-x|_2` on the
two balls is unique and lies on both spheres, where the profiles vanish.
That implies neither `A = 0` nor `A ≠ 0`. All sixteen pairs remain
`OPEN_PAIR`. `D_B = 0` is not asserted. The independent review attacks
those three load-bearing claims and returns **PASS**, with one recommended
drafting clarification applied at freeze (execution-report sha256 before /
after: `33691df6…` / `2da09280…`).

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN.** The obstacle is now localized: the
  competition between the propagation exponent and the profile zero at
  the boundary, not a missing trajectory and not a new encoder.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed.
- **Software certificate: PASS, 24/24 exact checks.** Identities only;
  leader, `A` and remainder are analytic and open.

**Claim ceiling.** Same frozen class as Sec. 8.17. No existence, no
vanishing, no `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The regional
rate is Sec. 8.19.

### 8.19 OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md`](../theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md)
preregistered at `08613d0` before any computation. Successor of Sec. 8.18,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--regional-directional-asymptotics-gate.md);
- its exact certificate
  [`verify_regional_directional_asymptotics_gate.py`](../scripts/verify_regional_directional_asymptotics_gate.py);
- the [independent review](../reports/2026-09-17--regional-directional-asymptotics-independent-review.md).

**Verdict.** `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The regional exponential rate is

`K_* = I(v_*)`, `v_* = (1 - 1/(2√3))(1,1,1)`,

with `I(v) = sup_ξ [ξ·v - arcosh(∏_j cosh ξ_j)]`. This is strictly
between `J` and `log 4`. It is the unique minimizer of `I` on the
regional velocity set (supporting tilt `ξ_* ∥ û`). The profile logarithms
are `O(log N)` and shift the saddle by `O(1)` lattice sites; they do
**not** change `K_*`. The coefficient `C` and the power `β` remain
unclassified. All sixteen pairs remain `OPEN_PAIR`. The independent
review attacks the three load-bearing claims (`I(v)` and the dual saddle;
uniqueness of `v_*`; `O(log N)` profiles) and returns **PASS**, with no
mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with the exponential rate identified.**
  `K_* = I(v_*)` is the Legendre envelope of the regional kernel. It is
  the exponential rate of `L` only if some `C` (or `C^{(j)}`) is
  non-vanishing and controlled, which is not claimed.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed, and not to open a
  coefficient gate before that review.
- **Software certificate: PASS, 18/18 exact checks.** Identities only;
  `C`, `β` and remainder are analytic and open.

**Claim ceiling.** Same frozen class. This section does not claim
existence, vanishing, or `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.
No new encoder. The complete Laplace coefficient at this unique saddle
is Sec. 8.20.

### 8.20 PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_LAPLACE_COEFFICIENT_GATE.md`](../theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md)
preregistered at `6f520ad` before any computation (blob `18d1f65`).
Successor of Sec. 8.19, without reopening it. Three artefacts are
recorded together here:

- the [execution report](../reports/2026-09-17--regional-laplace-coefficient-gate.md);
- its exact certificate
  [`verify_regional_laplace_coefficient_gate.py`](../scripts/verify_regional_laplace_coefficient_gate.py);
- the [independent review](../reports/2026-09-17--regional-laplace-coefficient-gate-independent-review.md).

**Verdict.** `PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`.
For all sixteen frozen pairs,

`L_{M,M_B}(N) = e^{-K_* N} N^{-13/2} (C_{M,M_B}(θ_N) + O(N^{-1/2}))`,

with `θ_N = {√3 N/4}` and `β = 13/2`. The complete coefficient is a sum
of the free-tail interference against the encoder layer, over the two
torus saddles `η ∈ {0, π(1,1,1)}` (distinct projectors `P` and `P̄`,
weights `Γ_±`). `C(θ)` is sign-definite and uniformly non-vanishing; the
relative oscillation is bounded by `1.47×10^{-3}`. Quadratic terms are
only bounded, at rate `e^{-2 K_* N}`. The independent review attacks the
seven load-bearing claims (`β`; complete `C` as a sum; uniform
non-vanishing; remainder vs charter `o(1)`; `C(θ)` vs constant `C`;
eight torus points vs frozen `K_*`; terminal state) and returns **PASS**,
with no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: PAULI_LEADING_COEFFICIENT_NONVANISHING.** `β = 13/2`
  is identified. All twelve Pauli pairs have `C(θ) ≠ 0` uniformly in `θ`,
  controlled against an `O(N^{-1/2})` remainder. With Secs. 8.17 and 8.19
  this authorizes, for those twelve pairs,
  `δ_{M,M_B}(N) = |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N} (1 + O(N^{-1/2}))`
  and `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` for those pairs. The
  four `M = I` pairs are also non-vanishing (`REFERENCE_CONTROL`).
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze, commit and promote as separate steps if the cold review passed.
- **Software certificate: PASS, 58/58 exact checks.** Identities and
  interval enclosures of closed forms, including uniform sign of
  `C_{M,M_B}(θ)` for all sixteen pairs. Analytic remainder lemmas (`N_*`,
  `C'`) are report `[A]`, not encoded. Finite-`N` diagnostics are
  `SUPPORTED` only.

**Claim ceiling.** Same frozen class. `C = C(θ_N)`, not an `N`-independent
constant. The remainder is asymptotic: `N_*` and `C'` are not explicit;
the leading formula is not quantitatively reliable for `N ≲ 10^3`, and
for `M ∈ {I, σ_3}` the `N^{-17/2}` piece dominates at diagnostic `N`.
No `D_B = 0`, no `δ ≡ 0`. Does not reopen `K_*`, `v_*`, geometry,
encoders, detectors, profiles, node or walk. Does not reopen
Secs. 8.16–8.19, `3/128`, no-corner, or `Delta T = 2`. `N → ∞` is not
`a, τ → 0`. No physical units. No claim of a microcausality violation.
The general family `M = a I + b · σ` is not covered.

The Sec. 8.19 sentence that the spectral-radius maximum is unique at
`η = 0` is false (equality on `{0,π}³`); `K_*` is unchanged and the extra
contributing point `π(1,1,1)` is included in `C`. The Sec. 8.19 files
are not edited.

This is a branch-local promotion only; `main` is unchanged.

**Project-level consequence (direct user instruction, 2026-09-17).**
In this frozen class, theoretical step 3 of the physical line is closed.
There is an operational IR response outside the emergent cone, and it is
not a mere consequence of the UV propagator. For the twelve Pauli pairs
the response is asymptotically non-vanishing and
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The precise claim, not to
be exaggerated, is:

> In the 3D Weyl QCA under study, the difference between the emergent
> relativistic cone and the microscopic causal support is not only a
> geometric possibility: under the preregistered IR-controlled protocol
> it produces an asymptotically non-vanishing operational response,
> albeit nonperturbatively suppressed.

That is a property of the model, with standing outside the repository as
such. It is not a statement about nature, not `D_B > 0` for every QCA,
and not an experimental prediction. No further signalling gate is
authorized. Fork 4A (a physical implementation of the walk that could
test the derived law) is identified and **not chartered**. The authorized
next front is Sec. 8.21.

### 8.21 PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE — AUTHORIZED, NOT_EXECUTED (2026-09-17)

Contract
[`PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md`](../theory/PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md)
frozen before any calculation, by direct user instruction (2026-09-17),
with the four closure criteria and first-class negative outcomes
incorporated before execution (this commit; first preregistration
`e9353ad`). Successor of Sec. 8.20, without reopening it. Inherits
Sec. 8.15 (`DIMENSIONAL_MAP_CONDITIONAL`) without reopening the `3/128`
audit. **Not a signalling gate, not a rate gate, not a Laplace-coefficient
gate, not a laboratory-implementation gate (4A).**

**Initial evidence status: `NOT_EXECUTED / OUTCOME_OPEN`.**

Step 3 is **input**, not an object to re-optimize. The gate does **not**
ask whether `δ_{M,M_B}(N) ≠ 0`. It asks whether a physically defensible
identification

`(a, τ, Λ, internal modes, A, B) ↔ (physical magnitudes and operations)`

converts `δ(N) ∼ |C(θ_N)| N^{-13/2} e^{-K_* N}` into a dimensional,
falsifiable prediction.

**Four hard closure criteria, all scored separately:**

1. **Absolute scale.** `a/τ = c` is not enough. External information must
   fix `a` or `τ`, or an additional physically motivated relation must
   appear. `a = ℓ_P` is `ASSUMPTION`, never `DERIVED`.
2. **Physical dictionary.** What the two internal components are, which
   physical operation implements `M = σ_j`, what `M_B` is, and what a
   narrow-band preparation is in the candidate system. A formal relabelling
   is not a dictionary.
3. **Dimensional observable.** From a dimensionless distance/probability
   to something an apparatus records (counts, phase, frequency, energy,
   occupation, correlation, or other), with an explicit SI law.
4. **Detectability.** If substituting physical scales yields
   `δ ∼ e^{-K_* λ/a}` with `λ/a` astronomical, the effect may be real
   and experimentally inaccessible. That is a legitimate closure.

A viable experiment is **not** the success criterion. First-class
negative outcomes: `NO_ABSOLUTE_SCALE_DERIVABLE`,
`PHYSICAL_MAP_CONDITIONAL_ONLY`,
`PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE`. None of these weakens Sec. 8.20.

Binding separation: model closed ≠ nature established ≠ experiment designed.

**Premises, not reopened:** `K_*`, `β`, `C(θ_N)`, the sixteen pairs, the
conditional dictionary of Sec. 8.15. **Not authorized:** execution of
this gate; fork 4A; a new signalling encoder, detector or geometry;
re-optimizing `K_*` or `C`; treating `N → ∞` as `a, τ → 0`; using a
Planck fiat as `DERIVED`.

**Theory paper (draft, not a gate).** The closed model result is written
as
[`papers/ir-corona-operational-response-draft.md`](../papers/ir-corona-operational-response-draft.md).
It does not wait on 4B. It separates ultraviolet propagator, infrared
operational response, and nature.

**Literature input to 4B, not execution.**
[`2026-09-17--physical-realization-literature-scan.md`](../reports/2026-09-17--physical-realization-literature-scan.md).
Adversarial bibliographic scan only. Three bins:
`ENGINEERED_EMULATOR`, `NATURAL_EFFECTIVE_ANALOG`,
`FUNDAMENTAL_CANDIDATE`. Hard question (natural system, `a` and `τ`
physically fixed, infrared cone strictly narrower than microscopic
support, known observable of that gap): **no** on this pass. Ion-trap
and photonic Dirac automata are 4A antecedents. Pavia/Mlodinow–Brun
are incomplete fundamental candidates (Planck `ASSUMPTION`, different
observables). This scan does **not** assign a 4B terminal state.


## 9. H1-only inhomogeneous reopening — branch-local update (2026-09-20)

**Status: H1 OPEN. Active bottleneck: \`H1c_LOCALIZATION (L')\`.**

This update supersedes the older statement that physical-realization / absolute-scale
Sec. 8.21 is the active line. The flat CJWW (5.15) operational IR-corona result
remains closed in its frozen class. The later inhomogeneous/AdS extension is not
reactivated as a whole: only H1 has been reopened.

Full research record:
- [H1 chat research log](../reports/2026-09-20--h1-chat-research-log.md)
- [H1 localization reconstruction and gate ledger](../reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md)
- primary endpoint/layer source: [regional Laplace-coefficient gate](../reports/2026-09-17--regional-laplace-coefficient-gate.md)

### 9.1 Frozen local structure

For
\[
D(z)=S(z)\oplus S(z)^{-1},\qquad
C_N(X)=e^{-i\vartheta(X)\beta/N},
\]
under the working frozen beta contract
\[
\beta^2=I,\qquad \beta D\beta=D^{-1},
\]
the dominant rank-two Riesz bundle satisfies
\[
\mathcal P\beta\mathcal P=0.
\]

Current statuses:
- \`H1-SR = PROVED_UNDER_FROZEN_BETA_CONTRACT\`;
- \`H1a = PROOF_WRITTEN / UNREVIEWED\`;
- \`H1b = PROOF_WRITTEN / UNREVIEWED\`;
- \`DERIVATIVE_SELECTION_RULE = PASS\`.

No global torus spectral gap is claimed.

### 9.2 Endpoint absolute-mass gate

The 2026-09-17 primary regional report was rechecked. It uses the complete
endpoint spinors, before spectral projection,
\[
f=s_Nb_N\chi,\qquad w=h_BM_Br,
\]
with
\[
b_N=O(N^{-3/2}),\quad
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),
\]
\[
s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),\quad
h_B=\frac{64}{N^2}{\varepsilon'_\perp}^{\,2}.
\]

Accounting for tangential area \(O(N(1+j))\) at normal depth \(j\) and the
exponentially summable tilted normal weight gives
\[
\sum_x e^{\xi_*\cdot(x-x_*)}\|f(x)\|=O(N^{-5/2}),
\]
\[
\sum_y e^{-\xi_*\cdot(y-y_*)}\|w(y)\|=O(N^{-5/2}).
\]

Therefore:
\[
\boxed{\texttt{LAYER_ABSOLUTE_MASS_BOUND = PASS}}.
\]

This is a full-spinor absolute bound, not a cancellation or dominant-projection
bound.

### 9.3 Local-window insertion and leakage gates

Using the derivative selection rule and the endpoint bounds:
\[
\boxed{\texttt{G_INSERTION_POWER_STABILITY = PASS_IN_LOCAL_WINDOW}}.
\]

The final complementary-bundle leakage is controlled by the full Bob norm.
The safe dominant correction is the zeroth-order \(Q\beta\mathcal P/N\) term,
giving
\[
|\Delta T_Q|=O(N^{-15/2}),
\]
not the earlier exploratory \(O(N^{-8})\) count. Hence:
\[
\boxed{\texttt{FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW}}.
\]

These are local-window statements only.

### 9.4 Remaining H1c gate

Literal pathwise H1b is not valid because a spatial path carries individual
hopping matrices \(D_h\), not the full symbol \(D(z)\). Thus:
\[
\texttt{H1c_GLOBAL = UNNECESSARY},
\qquad
\texttt{H1c_LOCALIZED = OPEN}.
\]

The sole active H1c bottleneck is:
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

A candidate momentum-space Dyson route has been formulated. Its key local
selection factor is
\[
\mathcal P(\eta+q)\beta\mathcal P(\eta)=O(|q|),
\]
and, for \(K_N(q)=N^3\widehat\vartheta(Nq)\),
\[
\int |q||K_N(q)|\,dq
=\frac1N\int |p||\widehat\vartheta(p)|\,dp.
\]
The working regularity assumption for this route is the Fourier-moment
condition
\[
\int_{\mathbb R^3}(1+|p|)|\widehat\vartheta(p)|\,dp<\infty.
\]

The desired \(n\)-insertion estimate is
\[
e^{-N\varphi_*}|T_n|
\le C N^{-13/2}\frac{(C'/N)^n}{n!}.
\]

**This estimate is not proved.** The missing step is uniform control of
non-normal variable-momentum products, including complementary-bundle visits,
transitions among the eight saddle neighborhoods, and regions where the local
Riesz splitting is unavailable. No momentum-conservation assumption may be
smuggled into that proof.

### 9.5 Locks

The H1 reopening does not change:
- \`E0 = OPEN_AT_STOP\`;
- \`POWER_13/2_STABILITY = OPEN_AT_STOP\`;
- \`E / AdS = STOPPED_UNPROVEN\`.

No further promotion is authorized until L' is proved and reviewed.

## 10. IR spectral-attribution audit — 2026-09-22

User-authorized exploratory audit and commit/push, documented in the
[full report](../reports/2026-09-22--ir-spectral-attribution-audit.md).
Status: **SUPPORTED / FINITE_N_NUMERICAL_DIAGNOSTIC**.
For the fixed sigma2/I pair, N=24 and N=40 pass the stated empirical precision
criterion. Lpp and R=L-Lpp nearly cancel. At N=40, direct nonperiodic
position evolution agrees with the tilted FFT: field discrepancy normalized
by maximum amplitude 1.62e-15; signal relative discrepancy 5.07e-16.
No asymptotic trend, exclusively UV origin, or rigorous numerical enclosure
is claimed. IR admissibility of operations does not by itself prove
predominance of the PP contribution at the exponentially small signal scale.
The stronger spectral attribution remains OPEN. The Sec. 8.20 flat theorem
retains its scope and status; its full proof is not re-certified here.
H1c, E0, POWER_13/2_STABILITY and E/AdS statuses of Sec. 9 are unchanged.
This records completed authorized diagnostics, not authorization for larger scans.

### 10.1 IR spectral-attribution front C1/C2/C3 — gate ledger (2026-09-22)

Explicit user decision on 2026-09-22 to record the certified C1 and C2a
verdicts here. Branch-local, like the rest of this file; `main` is unchanged.
Subsequent user acceptance on the same date promotes C2b after its independent
review and unblocks C2c as a structural-scope gate, without promoting C2c.
Contracts: [C1/C2/C3](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md),
[C2a](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md),
[C2b](../theory/IR_C2B_BLOCK_DECOMPOSITION_GATE.md),
[C2c structural scope](../theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md).
The front is fixed to P=Pi'=1_{|p|<=N^-1/2} (hard cutoff), Q=I-P, and the
signed block observable
Lpp=tr(E S^N P Delta P S^-N). This observable is not the conditioned Lcond
of C3.

| Subgate | Status | Evidence |
| --- | --- | --- |
| C1 leakage | **PASS** | [derivation](../reports/2026-09-22--ir-projection-leakage-and-conditioning.md), [independent review](../reports/2026-09-22--c1-leakage-independent-review.md) |
| C2a transfer, sigma2/I | **PASS** | [derivation](../reports/2026-09-22--c2a-oscillatory-transfer.md), [independent review](../reports/2026-09-22--c2a-independent-review.md) |
| C2b block decomposition, sigma2/I | **PASS** | [candidate](../reports/2026-09-22--c2b-block-decomposition-candidate.md), [independent review](../reports/2026-09-22--c2b-independent-review.md); B4_PRIME_PASS separately |
| C2c structural scope | **PASS — C2C_PASS, scope frozen** | [repaired execution](../reports/2026-09-22--c2c-structural-scope.md), [repaired review criteria](../theory/IR_C2C_REPAIRED_REVIEW_CRITERIA.md), [independent review](../reports/2026-09-23--c2c-independent-review.md); 16 original pairs only |
| C3 conditioning | **SEPARATE** | identity Lcond=(Lpp+q_N p0_N)/(1-q_N); not a substitute for C2 |
| E/AdS | **FROZEN** (STOPPED_UNPROVEN, Sec. 9.5) | unchanged |

- **C1 result:** q_N = ||Q(U_M-I)phi_N||^2 = D N^-5/2 (1+O(N^-1/2)) with
  D = 1024 pi^2 Phi_0(1/4)^2/5 > 0, for all four encoders. It follows that
  ||Delta - P Delta P||_1 = 2 sqrt(D) N^-5/4 (1+O(N^-1/2)).
- **C2a result (sigma2/I):**
  Lpp = N^-3 [C0 + C1 cos(sqrt(N)/2)] + O(N^-13/4), with C0 > C1 > 0 proved
  analytically (no numerical input). Hence Lpp = Theta(N^-3) and Lpp > 0 for
  all sufficiently large N.
- **Earlier consequence of C2a (arithmetic only):** R = L - Lpp = -Lpp + L
  exactly, and Thm 4.1 gives |L| <= 36 N^4 e^{-JN}. The complement of the PP
  block therefore cancels an algebraic Theta(N^-3) response. This establishes
  the cancellation's existence; it is not the proof of C2b below.
- **C2b result (sigma2/I):** direct block decomposition gives
  Lpp = +N^-3 A_N + O(N^-13/4), Lqq = +N^-3 A_N + O(N^-13/4), and
  Lpq + Lqp = -2 N^-3 A_N + O(N^-13/4), with the same
  A_N = C0 + C1 cos(sqrt(N)/2) >= C0-C1 > 0 as C2a.
  Thus the diagonal leaders are positive and the opposite leader lies in
  the coherences. Lqq >= 0 exactly; positivity of Lpp is asymptotic.
  B4_PRIME_PASS additionally gives Lpq = -N^-3 A_N + O(N^-13/4) and
  Lqp = -N^-3 A_N + O(N^-13/4); exactly, Lqp is the complex conjugate
  of Lpq, not necessarily equal to it at finite N.
- **Autonomous mechanism and bounds:** d_Q = d - d_P follows from Q=I-P
  and linearity. Thm 4.1 applies to the local source a, giving
  ||E^(1/2)(d_Q+d_P)|| <= 2 T_N. For every N>=2,
  |Lqq-Q_N| <= 8 T_N + 4 T_N^2 and
  |Lpq+Lqp+Lin_N+2 Q_N| <= 12 T_N, with T_N <= 9 N^4 exp(-JN).
  Here Q_N denotes the quadratic form <d_P,E d_P>, not the projector Q.
  C2a controls this quadratic form and Lin_N separately. No L-Lpp,
  Thm 4.4, total-signal asymptotics or N=24/40 data establish these blocks.

Caveats that must be retained with the C2a PASS:

1. The error term gains only N^-1/4 over the leading term.
2. The asymptotic regime is reached slowly: the oscillatory gains are powers
   of 1/(gamma sqrt(N)), where gamma = sqrt(3) - 3/2, which is about 1.1 at
   N=24 and 1.5 at N=40. The retained N=24/40 values do not validate or
   refute the sign.
3. The PASS is one independent **agent** review (Claude Opus 5). It is not
   an external human verification or a multi-member ratification.

C2b remains a `POST-DISCOVERY VERIFICATION GATE`: its discovery preceded
its contract. The independent review covers exactly snapshot
`19eb7a383cbb09464e91b64e89f724204e58cccb` and returns C2B_PASS and
B4_PRIME_PASS without required repairs. Review artifact SHA256:
`65bab830c6960f2c661ae47d739d90c1ecf8ae06b5f9923383919f76c2b234d5`.
The reviewer is recorded as **Codex, agent `/root`**, distinct from the
candidate's author, Claude Opus 5. This is one independent agent review,
not external human review, multi-member consensus or documented model
diversity. No additional Astra review has been recorded; such a review
remains an optional additional audit before publication, not a condition
retroactively imposed on this internal PASS.

C2c addressed **structural scope**, starting from the mechanism already
proved for sigma2/I: distinguish algebra and localized compensation from
pair-dependent leading coefficients, classify the sixteen original pairs,
and state the hypotheses and limits of any general hard-cutoff result.
The repaired execution makes the detector/espinor transfer explicit, retains
all band crossings, changes the grouping claim to **at most eight families**,
and restricts §9.2 to scalar indicator cuts with the stated open-set and
finite-support hypotheses. An independent review records
`C2C_PASS` for all five S3 levels on all sixteen original pairs, C1, and
§9.2 within that scope. The exponent `N^-3` remains a property of the frozen
`K=sqrt(N)` protocol, not a general QCA law; `N_0` and remainder constants
remain non-effective, and `NOVELTY=OPEN`.

This promotion is branch-local and does not reopen C3, E/AdS or FR1–FR3.
The repaired report and review retain their own commits and hashes; no
finite-N claim or broader detector/QCA class is added.

C3 remains SEPARATE; E/AdS remains FROZEN. H1c, E0,
POWER_13/2_STABILITY and the Sec. 8.20 flat theorem are unchanged. No new
numerical calculation, scan, manuscript publication, commit or push follows
from this update.
```


## Ronda 1 — CLAUDE OPUS

Reconstrucción más fuerte del objeto auditado: C3 no afirma nada sobre el líder de `Lcond`; sólo encadena una identidad algebraica exacta con dos asintóticas importadas. Verifico la identidad con lo adjunto. Con `Pφ_N=φ_N` se tiene `Δ_PP=|w><w|-|φ><φ|`, y `(Δ_PP+q_N|φ><φ|)/(1-q_N)=|w><w|/(1-q_N)-|φ><φ|`, que es exactamente el estado condicionado declarado [SOURCE, C3.1 comprobada]. (C3.3) sale de (C3.2) sin residuo: `q_N(p_0+L_PP)/(1-q_N)` [INFERENCE, álgebra reproducida]. También es consistente el uso de C1: `Qv=Q(U_M-I)φ_N` porque `Qφ_N=0`, luego el `q_N` de C3 es el `q_N` certificado en §10.1 del estado y no una cantidad distinta con el mismo nombre [INFERENCE].

El punto más débil no es ninguna de esas piezas, sino la cláusula de reserva de §3, que es la que sostiene el cumplimiento de la obligación 5:

> «Esto no determina el término líder de `L_cond` ni de `Lpp` por separado: puede existir cancelación entre `Lpp` y la corrección de (C3.3).»

Esa frase es **falsa bajo las premisas que el propio informe acaba de usar** [INFERENCE]. C2c (C15)–(C16) no dan `O(N^{-3})`: dan `L_PP=N^{-3}𝒜_{M,D_0}(√N)+O(N^{-13/4})` con `0<512β²λ ≤ 𝒜 ≤ 512β²Λ`, es decir `L_PP=Θ(N^{-3})` [SOURCE, C2c §§7–8]. Como `N^{-3}=o(N^{-5/2})` y `Dp_∞>0`, la corrección domina a `L_PP` por un factor `N^{1/2}`, y no hay cancelación posible: `L_cond=Dp_∞N^{-5/2}(1+o(1))`, positivo finalmente, con `|L_cond|∼Dp_∞N^{-5/2}`. O sea: el informe mantiene OPEN el líder de `Lcond` por obediencia al contrato, pero lo justifica con una imposibilidad matemática. Dejar OPEN por decisión de alcance es legítimo; dejarlo OPEN alegando una cancelación que sus propias cotas excluyen no lo es, y contamina la lectura de (C3.7), cuyo `(1+o(1))` sólo tiene sentido precisamente porque esa cancelación no ocurre.

Esto es un dilema, no una objeción de estilo. O bien `L_PP=O(N^{-3})` está disponible —y entonces §3 contiene una afirmación falsa que exige reparación textual— o bien no lo está, y entonces la obligación 4 no está cumplida y (C3.7) pierde su premisa. El informe no puede tener las dos cosas.

**Condición de concesión:** retiro el ataque si C3 sustituye esa frase por una que separe alcance de matemática —por ejemplo: «el contrato no autoriza pronunciarse sobre el líder de `Lcond`; con `L_PP=O(N^{-3})` ese líder sería deducible, y se deja fuera de alcance, no abierto»— o si se muestra que la cota importada de C2c es sólo `o(1)` y no `O(N^{-3})`, caso en el que la reserva sería correcta pero la obligación 4 quedaría INCOMPLETE.

Segunda objeción, más corta y también admisible. (C3.5) postula `p_{0,N}→∫h||R_0||²` «por sumas de Riemann», sin fijar la normalización de `h_N` ni el peso de red [SOURCE: el informe no la escribe]. Con `h_N=h(y/N)` el límite es no degenerado; con cualquier potencia de `N` en `h_N`, `p_∞` sería `0` o `∞` y (C3.6) caería. **Condición de concesión:** que se exhiba la normalización congelada de `E=h_N I` y el conteo `N³·(N^{-3/2})²=1`. Sin eso, obligación 3 es INCOMPLETE, no PASS.

Anoto además que `2026-09-23--c2c-independent-review.md`, del que depende (C15)–(C16) como entrada certificada, no está adjunto: [ABSENCE] en esta acta.

## Ronda 1 — GEMINI

**Veredicto global: C3_REPAIR_REQUIRED.**

Suscribo las objeciones de CLAUDE OPUS sobre la imposibilidad matemática de la cancelación en (C3.7) y la ausencia de la constante de normalización para $h_N$. La partición inicial, la identidad de los estados condicionados (C3.1) y las definiciones operativas de los proyectores quedan validadas como contexto establecido [RECONSTRUCTION]. 

El salto asintótico final contiene una laguna estructural no cubierta. La Obligación 3 exige probar $p_\infty > 0$ para el detector de Bob. El informe invoca la analiticidad del recurso de Weyl $R_0$ para afirmar que no puede anularse en una bola abierta [SOURCE], lo cual garantiza que la integral continua (C3.5) es estrictamente positiva. Sin embargo, se deduce directamente de esto que $p_\infty > 0$ legitima el límite del protocolo discreto [INFERENCE]. Este salto omite la transformación crítica: la sucesión $p_{0,N}$ es una evaluación de sumas de Riemann sobre una malla finita. El ascenso de "integral continua positiva" a "evaluación discreta garantizada lejos de cero" exige aislar el error de cuadratura frente a la topología de los ceros de la función analítica. Quien asciende de la positividad de un objeto continuo a la validez operativa de su homólogo discreto debe aportar el paso de control.

**Condición de concesión:** Retiro este ataque si el informe se repara integrando explícitamente el control del error de cuadratura (invocando la convergencia uniforme ya certificada en C1) para demostrar formalmente que $p_{0,N} \ge c > 0$ para todo $N$ suficientemente grande, cerrando así la brecha de evaluación discreta.

En su estado actual, la reserva impuesta en el §3 del informe emplea una justificación espuria que choca con la asintótica $O(N^{-3})$ importada, y la deducción de la Obligación 3 adolece de un salto técnico injustificado en la transición discreto-continuo.

## Ronda 2 — CLAUDE OPUS

Concedo a GEMINI la coincidencia en las dos objeciones de la ronda 1 y no las repito. Ataco sólo el punto donde su turno añade algo, porque ahí hay un ascenso injustificado en dirección contraria.

GEMINI exige, como paso adicional, «aislar el error de cuadratura frente a la topología de los ceros de la función analítica» para pasar de `p_∞>0` a `p_{0,N}≥c>0`. Ese paso no falta: es una línea. Si (C3.5) —`p_{0,N}→p_∞`— está establecida y `p_∞>0`, entonces `p_{0,N}≥p_∞/2` para `N` grande, por definición de límite [INFERENCE]. Los ceros de `R_0` no intervienen: la analiticidad se usa una sola vez, para que la integral límite no se anule, y no vuelve a hacer falta después. Además (C3.7) sólo necesita convergencia, no una tasa: el `(1+o(1))` absorbe cualquier velocidad. La regla 6 se invoca aquí contra un tramo trivial mientras el tramo realmente no escrito queda intacto.

El tramo no escrito es el anterior, y es el mío: (C3.5) misma. El informe no fija la normalización de `E=h_N I` ni el peso de red, de modo que la sucesión cuyo límite se invoca no está definida en el acta [SOURCE: §2 del informe C3 no escribe `h_N`]. Sin el conteo `N³·(N^{-3/2})²=1` no hay sumas de Riemann que converjan a nada. La objeción de GEMINI, desplazada un escalón hacia arriba, se disuelve en la mía; hacia abajo, no es un ataque. Mantengo por tanto la condición de concesión ya formulada, y sólo esa.

Sobre mi primera objeción, añado un refuerzo que la cierra. (C15) no da sólo `Θ(N^{-3})`: da `𝒜_{M,D}≥512β²λ>0`, luego `L_PP>0` finalmente. Ambos sumandos de (C3.3) son positivos a orden líder. La cancelación que §3 reserva como posible está excluida dos veces: por orden (`N^{-3}=o(N^{-5/2})`) y por signo. Nada en el turno de GEMINI la rescata.

Veredictos por obligación, con el alcance del encargo:

- Identidad exacta de estados y de `L_cond` (C3.1)–(C3.3): **PASS**. Reproducida en la ronda 1; `Qφ_N=0` garantiza que el `q_N` es el certificado en C1.
- `q_N` y probabilidades de éxito `1` y `1-q_N`: **PASS**.
- `p_{0,N}→p_∞>0` para `M_B=I`: **INCOMPLETE**. Falta la normalización congelada de `h_N` y el peso de red; la positividad analítica de `R_0`, una vez definido el objeto, no es el eslabón débil.
- `L_{PP,N}=O(N^{-3})` fila a fila con C15–C16 para `M∈{I,σ1,σ2,σ3}`, `D_0=I`: **PASS** como importación (las cuatro filas figuran en C2c §8 y el estado registra `C2C_PASS`), con la salvedad de que el enunciado correcto es `Θ(N^{-3})`; la revisión independiente de C2c no está adjunta [ABSENCE].
- Corrección (C3.7): **INCOMPLETE por herencia**. El álgebra es correcta; su premisa `p_∞>0` no está cerrada.
- §3, conclusión C3.7 y cláusula de reserva: **REPAIR**. La reserva alega una cancelación que las cotas importadas excluyen.

Veredicto global: **C3_REPAIR_REQUIRED**. Dos reparaciones textuales acotadas, ninguna refutación del mecanismo.

## Ronda 2 — GEMINI

Veredicto global: C3_REPAIR_REQUIRED. [INFERENCE] Las obligaciones 1, 2 y la importación asintótica superan la auditoría de este sanedrín, mientras que las obligaciones 3 y 4 exigen reparaciones textuales exactas en el documento auditado para su promoción.

[RECONSTRUCTION] Concedo a CLAUDE OPUS la disolución de mi objeción previa: la definición elemental de convergencia domina el error de cuadratura, descartando mi exigencia sobre los ceros de la función analítica. 

[SOURCE] La partición de estados, el álgebra exacta en (C3.1)-(C3.3) y las probabilidades asintóticas derivadas de C1 quedan convalidadas como contexto operativo firme, sin requerir revisión adicional.

[INFERENCE] La primera transformación requerida para el éxito ocurre en (C3.5), donde es imperativo inyectar la normalización $h_N(y) = h(y/N)$ y la compensación de escala $N^3 \cdot N^{-3} = 1$ para legitimar la transición a la suma de Riemann; sin ello, la probabilidad límite carece de asidero dimensional.

[SOURCE] La segunda transformación exige la eliminación en §3 de la conjetura sobre una cancelación entre $L_{PP}$ y la corrección, dado que choca frontalmente con la cota $O(N^{-3})$ proveniente de C2c (C15-C16).

[INFERENCE] La asimetría estricta de órdenes matemáticos y la positividad concurrente erradican cualquier cancelación; la justificación para mantener OPEN el líder de $L_{\mathrm{cond}}$ debe fundarse exclusivamente en los límites declarados del contrato, extirpando la falsa premisa algebraica de la literatura final.

## Ronda Residuo — CLAUDE OPUS

Queda en pie el núcleo algebraico: (C3.1)–(C3.3) son exactas y reproducibles con `Pφ_N=φ_N` y `Qφ_N=0`; el `q_N` de C3 es el certificado en C1, no un homónimo; la importación fila a fila de C15–C16 para los cuatro `M` con `D_0=I` es legítima como entrada, con la salvedad de que el enunciado correcto es `Θ(N^{-3})`, no `O(N^{-3})`. Nada en dos rondas ha tocado este bloque.

Debe abandonarse la cláusula de reserva de §3. No es una imprecisión: es una afirmación falsa bajo las cotas que el propio informe invoca dos líneas antes. La cancelación está excluida por orden y por signo. Mantener OPEN el líder de `L_cond` es correcto por alcance contractual, y sólo por eso; la justificación matemática debe extirparse, no matizarse.

No está justificada todavía (C3.5), y por herencia (C3.7). El informe invoca el límite de una sucesión que no define: sin la normalización congelada de `E=h_N I` ni el peso de red, `p_{0,N}` no es un objeto en el acta y `p_∞>0` no tiene sujeto.

Discrepo del residuo de GEMINI en un punto. Escribe que hay que «inyectar la normalización `h_N(y)=h(y/N)`». Eso no es residuo: es la reparación que el informe debe justificar, no que el sanedrín deba suministrarle. Ninguno de los dos hemos visto `h_N` escrito en parte alguna del acta; proponer su forma es completar el documento auditado, no auditarlo. La obligación 3 queda INCOMPLETE hasta que C3 exhiba la normalización que ya tuviera congelada, sea cual sea.

Obligación 1: PASS. Obligación 2: PASS. Obligación 3: INCOMPLETE. Obligación 4: INCOMPLETE por herencia. Importación C15–C16: PASS, con la revisión independiente de C2c no adjunta [ABSENCE]. Global: **C3_REPAIR_REQUIRED**.

## Ronda Residuo — GEMINI

Veredicto global: C3_REPAIR_REQUIRED.

[RECONSTRUCTION] La partición algebraica (C3.1)–(C3.3) y la importación del bloque C15–C16 se consolidan como contexto operativo firme. La validez de las identidades condicionales iniciales es absoluta.

[SOURCE] Debe suprimirse la cláusula de reserva del §3. La justificación de una supuesta cancelación matemática es falsa frente a la asimetría de órdenes probada; mantener OPEN el líder de $L_{\mathrm{cond}}$ se sostiene exclusivamente por mandato perimetral del contrato.

[INFERENCE] Las fórmulas (C3.5) y (C3.7) no están justificadas. Sin la definición explícita de la normalización para $E=h_N I$ en el acta, el límite $p_{0,N} \to p_\infty > 0$ carece de sujeto y operabilidad.

[INFERENCE] Suscribo la rectificación de CLAUDE OPUS sobre mi residuo previo. Proponer la solución funcional $h_N(y)=h(y/N)$ constituyó un exceso reconstructivo. Requerir que el reporte aporte su propia normalización congelada es el único curso auditable. Las Obligaciones 3 y 4 caen a INCOMPLETE por estricta ausencia de anclaje dimensional original en la fuente.

## Ronda Veredicto — CLAUDE OPUS

# 1. ACUERDO

Ambos miembros convergen, por vías distintas, en lo siguiente:

**Bloque algebraico validado.** (C3.1)–(C3.3) son exactas y fueron reproducidas en el acta: con `Pφ_N=φ_N` se obtiene `Δ_PP=|w><w|-|φ><φ|` y `(Δ_PP+q_N|φ><φ|)/(1-q_N)=|w><w|/(1-q_N)-|φ><φ|`, que coincide con el estado condicionado declarado; (C3.3) se sigue de (C3.2) sin residuo. Obligación 1: **PASS**.

**Identidad de `q_N`.** Como `Qφ_N=0`, `Qv=Q(U_M-I)φ_N`, de modo que el `q_N` usado en C3 es el certificado en C1 y no una cantidad homónima. Probabilidades de éxito `1` y `1-q_N`: **PASS** (obligación 2).

**Importación C15–C16.** Las cuatro filas con `D_0=I` y `M∈{I,σ1,σ2,σ3}` figuran en C2c §8; la importación es legítima como entrada, con la precisión —no discutida por ninguno— de que el enunciado correcto es `Θ(N^{-3})`, no `O(N^{-3})`, porque (C15) acota `𝒜_{M,D}` por debajo por `512β²λ>0`. **PASS** como importación.

**Reparación obligatoria en §3.** La cláusula «puede existir cancelación entre `Lpp` y la corrección de (C3.3)» es falsa bajo las cotas que el propio informe invoca: `N^{-3}=o(N^{-5/2})` excluye la cancelación por orden, y `L_PP>0` finalmente la excluye además por signo. Mantener OPEN el líder de `L_cond` es correcto por alcance contractual y sólo por eso; la justificación matemática debe extirparse, no matizarse.

**Obligaciones 3 y 4: INCOMPLETE.** El informe no escribe la normalización de `E=h_N I` ni el peso de red, de modo que la sucesión `p_{0,N}` cuyo límite invoca (C3.5) no está definida en el acta; `p_∞>0` queda sin sujeto y (C3.7) sin premisa.

**Veredicto global coincidente: `C3_REPAIR_REQUIRED`** — dos reparaciones textuales acotadas, ninguna refutación del mecanismo.

# 2. DESACUERDO VIVO

Ninguno sustantivo al cierre. Los dos puntos en que hubo choque se resolvieron dentro de la deliberación (registrados en §3). Queda una diferencia menor de método, ya concedida por GEMINI y por tanto no viva: si el sanedrín puede proponer la forma de `h_N` o debe exigir que C3 exhiba la suya. Se registra la posición que prevaleció: es el informe quien debe aportar su normalización congelada; suministrarla desde el arbitraje completaría el documento auditado en lugar de auditarlo.

# 3. ABANDONADO

**Objeción de GEMINI sobre el error de cuadratura (ronda 1), retirada por su autor en ronda 2.** Exigía aislar el error de cuadratura frente a la topología de los ceros de `R_0` para ascender de `p_∞>0` a `p_{0,N}≥c>0`. Refutada: dada (C3.5) y `p_∞>0`, la definición de límite da `p_{0,N}≥p_∞/2` para `N` grande; los ceros de `R_0` no reintervienen tras el único uso de la analiticidad, y (C3.7) necesita convergencia, no tasa. La objeción, desplazada un escalón hacia arriba, se disuelve en la de la definición de `h_N`.

**Propuesta de GEMINI de inyectar `h_N(y)=h(y/N)` y el conteo `N³·N^{-3}=1` (residuo).** Retirada por su autor como «exceso reconstructivo».

**Posición previa del árbitro que no sobrevivió intacta.** En ronda 1 formulé la segunda objeción proponiendo yo mismo la normalización candidata (`con h_N=h(y/N) el límite es no degenerado… el conteo N³·(N^{-3/2})²=1`). Por el mismo criterio que luego opuse a GEMINI, esa formulación era también reconstructiva: la condición de concesión correcta es que C3 exhiba su normalización congelada, no que el revisor valide una que él mismo ha supuesto. Registro la corrección contra mi propio turno.

**Presentado en ronda 1 como dilema, resuelto como una sola rama.** Planteé que o bien `L_PP=O(N^{-3})` está disponible —y §3 es falso— o bien no lo está —y la obligación 4 pierde premisa. La deliberación cerró la primera rama: la cota está disponible y es más fuerte (`Θ`). La segunda rama nunca se activó; la obligación 4 cae por una razón distinta de la contemplada allí (la indefinición de `p_{0,N}`, no la indisponibilidad de la cota de C2c).

# 4. PENDIENTE

1. **La normalización congelada de `E=h_N I` y el peso de red.** Es el único bloqueo técnico real. C3 debe exhibir la definición que ya tuviera congelada en C1/C2 —sea cual sea— y el conteo que hace no degenerado el límite de sumas de Riemann de (C3.5). Cerrado eso, la obligación 3 pasa a PASS y la 4 con ella, sin más álgebra.

2. **Redacción sustitutiva de §3.** Una formulación que separe alcance de matemática, del tipo: el contrato no autoriza pronunciarse sobre el líder de `L_cond`; con `L_PP=Θ(N^{-3})` ese líder sería deducible, y se deja *fuera de alcance*, no *abierto*.

3. **`reports/2026-09-23--c2c-independent-review.md` no está adjunto** [ABSENCE]. La importación de C15–C16 descansa en él vía el registro `C2C_PASS` de `state/CURRENT_STATE.md` §10.1. Este sanedrín verificó la presencia de las cuatro filas en C2c §8 y la consistencia interna de (C15), no la revisión que las certifica. Una revisión posterior que quiera cerrar C3 debe leerla directamente.

4. **Corrección de `O` a `Θ`** en la cita que C3 hace de C2c, si se quiere que (C3.7) y la supresión de la reserva de §3 queden trazadas a la misma cota.

5. **Fuera del alcance de este sanedrín y no tocado:** líder de `L_cond`, `|L_cond|`, comparación con `L`, H1c y E/AdS permanecen OPEN, como exigía el encargo. Nada de lo deliberado los mueve.

## Ronda Veredicto — CLAUDE OPUS

# 1. AGREEMENT

Both members converge, by different routes, on the following:

**Validated algebraic block.** (C3.1)–(C3.3) are exact and were reproduced in the record: with `Pφ_N=φ_N` one obtains `Δ_PP=|w><w|-|φ><φ|` and `(Δ_PP+q_N|φ><φ|)/(1-q_N)=|w><w|/(1-q_N)-|φ><φ|`, which coincides with the declared conditioned state; (C3.3) follows from (C3.2) with no residue. Obligation 1: **PASS**.

**Identity of `q_N`.** Since `Qφ_N=0`, `Qv=Q(U_M-I)φ_N`, so that the `q_N` used in C3 is the one certified in C1 and not a homonymous quantity. Success probabilities `1` and `1-q_N`: **PASS** (obligation 2).

**Import of C15–C16.** The four rows with `D_0=I` and `M∈{I,σ1,σ2,σ3}` appear in C2c §8; the import is legitimate as an input, with the qualification —not disputed by either member— that the correct statement is `Θ(N^{-3})`, not `O(N^{-3})`, because (C15) bounds `𝒜_{M,D}` from below by `512β²λ>0`. **PASS** as an import.

**Mandatory repair in §3.** The clause «there may exist cancellation between `Lpp` and the correction in (C3.3)» is false under the bounds that the report itself invokes: `N^{-3}=o(N^{-5/2})` rules out cancellation by order, and `L_PP>0` finally rules it out by sign as well. Keeping the leading term of `L_cond` OPEN is correct on grounds of contractual scope and only on those grounds; the mathematical justification must be excised, not qualified.

**Obligations 3 and 4: INCOMPLETE.** The report does not write down the normalization of `E=h_N I` nor the lattice weight, so that the sequence `p_{0,N}` whose limit (C3.5) invokes is not defined in the record; `p_∞>0` is left without a subject and (C3.7) without a premise.

**Coinciding global verdict: `C3_REPAIR_REQUIRED`** — two bounded textual repairs, no refutation of the mechanism.

# 2. LIVE DISAGREEMENT

None substantive at closing. The two points where there was a clash were resolved within the deliberation (recorded in §3). There remains a minor difference of method, already conceded by GEMINI and therefore not live: whether the sanhedrin may propose the form of `h_N` or must require that C3 exhibit its own. The position that prevailed is recorded: it is the report that must supply its frozen normalization; supplying it from the arbitration would complete the audited document instead of auditing it.

# 3. ABANDONED

**GEMINI's objection about the quadrature error (round 1), withdrawn by its author in round 2.** It demanded isolating the quadrature error against the topology of the zeros of `R_0` in order to ascend from `p_∞>0` to `p_{0,N}≥c>0`. Refuted: given (C3.5) and `p_∞>0`, the definition of limit yields `p_{0,N}≥p_∞/2` for large `N`; the zeros of `R_0` do not re-enter after the single use of analyticity, and (C3.7) needs convergence, not a rate. The objection, displaced one step upward, dissolves into the one about the definition of `h_N`.

**GEMINI's proposal to inject `h_N(y)=h(y/N)` and the count `N³·N^{-3}=1` (residue).** Withdrawn by its author as «reconstructive excess».

**Prior position of the arbiter that did not survive intact.** In round 1 I formulated the second objection by myself proposing the candidate normalization (`with h_N=h(y/N) the limit is non-degenerate… the count N³·(N^{-3/2})²=1`). By the same criterion I later opposed to GEMINI, that formulation was also reconstructive: the correct concession condition is that C3 exhibit its frozen normalization, not that the reviewer validate one he has himself assumed. I record the correction against my own turn.

**Presented in round 1 as a dilemma, resolved as a single branch.** I posed that either `L_PP=O(N^{-3})` is available —and §3 is false— or it is not —and obligation 4 loses its premise. The deliberation closed the first branch: the bound is available and is stronger (`Θ`). The second branch was never activated; obligation 4 falls for a reason different from the one contemplated there (the undefinedness of `p_{0,N}`, not the unavailability of the C2c bound).

# 4. OUTSTANDING

1. **The frozen normalization of `E=h_N I` and the lattice weight.** This is the only real technical blocker. C3 must exhibit the definition it already had frozen in C1/C2 —whatever it may be— and the count that makes the limit of Riemann sums in (C3.5) non-degenerate. Once that is closed, obligation 3 passes to PASS and obligation 4 with it, with no further algebra.

2. **Substitute wording for §3.** A formulation that separates scope from mathematics, of the type: the contract does not authorize pronouncing on the leading term of `L_cond`; with `L_PP=Θ(N^{-3})` that leading term would be derivable, and it is left *out of scope*, not *open*.

3. **`reports/2026-09-23--c2c-independent-review.md` is not attached** [ABSENCE]. The import of C15–C16 rests on it via the `C2C_PASS` record in `state/CURRENT_STATE.md` §10.1. This sanhedrin verified the presence of the four rows in C2c §8 and the internal consistency of (C15), not the review that certifies them. A subsequent review seeking to close C3 must read it directly.

4. **Correction of `O` to `Θ`** in the citation C3 makes of C2c, if one wants (C3.7) and the removal of the reservation in §3 to be traced to the same bound.

5. **Outside the scope of this sanhedrin and untouched:** leading term of `L_cond`, `|L_cond|`, comparison with `L`, H1c and E/AdS remain OPEN, as the commission required. Nothing deliberated moves them.

## Resultado operativo

- Estado: `COMPLETED`
- Turnos con fallo, cuota, ausencia o respuesta corta: 0
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-23T11:12:18Z` |
| Finished (UTC) | `2026-09-23T11:16:56Z` |
| Wall clock | 0h 4m 38s |
| Command | `sanedrin -r 2 -m opus,gemini --secuencial --timeout 900 --reintentos 1 -i es -o debates/2026-09-23--c3-claude-gemini-review.md -c theory/IR_C3_CONDITIONING_GATE.md -c reports/2026-09-23--c3-conditioning-execution.md -c reports/2026-09-22--c2c-structural-scope.md -c state/CURRENT_STATE.md Revisión independiente de la versión reparada de C3. Claude es el revisor principal. Audita únicamente: identidad exacta de Lcond; q_N y éxito; p0_N -> p_infty>0 para M_B=I; demostración fila a fila de L_PP,N=O(N^-3) para M en {I,sigma1,sigma2,sigma3}, D0=I, usando C15-C16 de C2c; y conclusión C3.7. Mantén OPEN el líder de Lcond, |Lcond|, comparación con L, H1c y E/AdS. No uses N=24/40, simulaciones, cuadraturas, barridos ni fuentes externas. Emite PASS/INCOMPLETE/FAIL por obligación y veredicto global C3_PROOF_WRITTEN_REVIEW_ACCEPTED, C3_REPAIR_REQUIRED, C3_FAIL o C3_INCOMPLETE. No modifiques archivos.` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-23T11:13:44Z | 1 | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 86 | 479 | ok |
| 2026-09-23T11:14:21Z | 1 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 37 | 285 | ok |
| 2026-09-23T11:15:03Z | 2 | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 42 | 458 | ok |
| 2026-09-23T11:15:30Z | 2 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 27 | 215 | ok |
| 2026-09-23T11:15:42Z | Residuo | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 12 | 270 | ok |
| 2026-09-23T11:16:04Z | Residuo | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 22 | 154 | ok |
| 2026-09-23T11:16:33Z | Veredicto | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 29 | 812 | ok |
| 2026-09-23T11:16:56Z | Veredicto | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 22 | 831 | ok |

Turns: 8 · failed: 0 · model time: 4m 37s

Full log: `2026-09-23--c3-claude-gemini-review.log`
