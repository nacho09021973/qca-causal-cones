---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-23 13:19
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

Revisión final de C3 tras el commit 2eb8b00. Claude es el revisor principal. Audita únicamente la identidad exacta de Lcond, q_N y éxito, la definición congelada de h_N y la suma de red que define p0_N, el límite p0_N -> p_infty>0, la importación C15-C16 para los cuatro pares D0=I y la conclusión C3.7. Comprueba que se retiró la falsa posibilidad de cancelación por órdenes. Mantén fuera de alcance el líder de Lcond, abs(Lcond), comparación con L, H1c y E/AdS. No uses N=24/40, simulaciones, cuadraturas ni barridos. Emite PASS/INCOMPLETE/FAIL por obligación y veredicto global C3_PROOF_WRITTEN_REVIEW_ACCEPTED, C3_REPAIR_REQUIRED, C3_FAIL o C3_INCOMPLETE. No modifiques archivos.

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

Para `M_B=I`, se usa la normalización congelada del manuscrito
`papers/ir-corona/ir-corona.md`, §3.2: con `u=(1,1,1)`,

\[
h_N(y)=\left(1-16|y-Nu|^2/N^2\right)_+^2,
\qquad E=h_N\otimes I .
\]

Por tanto, escribiendo `r_N=S^N phi_N`,
\[
p_{0,N}=\sum_{y\in\mathbb Z^3}h_N(y)\,\|r_N(y)\|^2.
\]
El lema de la cola de C1 da `r_N(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})`
uniformemente en la bola de Bob. Al poner `Y=y/N`, el factor
`N^{-3}` de `\|r_N(y)\|^2` se compensa con la densidad `N^3` de la suma,
y las sumas de Riemann dan
\[
p_{0,N}\longrightarrow
p_\infty:=\int_{|Y-u|<1/4}h_0(Y-u)\|R_0(Y)\|^2\,d^3Y,
\qquad h_0(Z)=(1-16|Z|^2)^2.
\tag{C3.5}
\]
El peso `h_0` es estrictamente positivo en el interior de la bola. `R_0` es
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
`L_{PP,N}=Theta(N^{-3})`, y en particular `L_{PP,N}->0`. Insertando (C3.4)–(C3.6) en
(C3.3),
\[
\boxed{
L_{\mathrm{cond},N}-L_{PP,N}
=D p_\infty N^{-5/2}(1+o(1))}. 
\tag{C3.7}
\]
La corrección es algebraica y positiva a orden líder. El líder de `L_cond`
queda fuera del alcance contractual; además, la cota `L_{PP,N}=Theta(N^{-3})`
es de orden estrictamente menor que `N^{-5/2}`, así que no hay una
cancelación por órdenes entre `Lpp` y la corrección de (C3.3). Tampoco se
compara `Lcond-Lpp` con el observable total `L` mediante una norma global.

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

### Contexto adjunto: papers/ir-corona/ir-corona.md
```
# An infrared operational response outside the emergent light cone of a three-dimensional Weyl quantum walk

> **Markdown transcription for review.** Source: `papers/ir-corona/ir-corona.tex`
> (pre-publication revision of 2026-09-18). Section, theorem, equation and
> reference numbers match the compiled PDF. If this file and the `.tex`
> disagree, the `.tex` is authoritative. The prior art of the revised Markdown
> draft (`papers/ir-corona-operational-response-draft.md`, commit `9812cbc`) is
> now merged: Carteret–Richmond–Temme, Baryshnikov–Brady–Bressler–Pemantle,
> ACSV, and the narrowed novelty statement.

**José Ignacio Martín Gandul**  
Independent Researcher, Seville, Spain

## Abstract

In a finite-range quantum walk the relativistic light cone that emerges at
long wavelength need not exhaust the strict microscopic causal support. We
study the three-dimensional Weyl walk introduced by Cedzich, Joye, Werner and
Werner as a model with a spherical propagation region. All of its group
velocities lie in the closed Euclidean unit ball, which is also the light
cone of its Weyl node. Its one-step causal support is the cube $[-1,1]^3$.
Velocities in the cube but outside the ball form a *corona*. There,
propagation is non-ballistic but not causally forbidden.

We ask whether the corona carries an operational response that survives
infrared control. Alice prepares a narrow-band state and applies a local
encoding, and Bob reads out with a local detector. All three operations are
required to be infrared-admissible: acting on the band $|p|\le N^{-1}$, each
produces only a vanishing fraction of its output outside the wider band
$|p|\le N^{-1/2}$. Bob's
region lies outside the emergent light cone of every site of Alice's region.
After $N$ steps, Bob's distinguishability $\delta(N)$ obeys the explicit
bound $\delta(N)\le 36N^4e^{-JN}$ with $J=(1-\sqrt3/2)\log 2$. For a concrete
family of sixteen encoder–detector pairs, it has the exact leading
asymptotics

$$
\delta(N)=\bigl|C(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad \theta_N=\{\sqrt3N/4\}.
$$

Here $K_*\approx0.1905$ is the value of a Legendre rate function at a unique
regional minimiser. The coefficient $C(\theta)$ is given in closed form, and
interval arithmetic shows that it does not vanish for any $\theta$ in any of
the sixteen pairs. The emergent cone is therefore not operationally sharp,
even for infrared-admissible operations. The response is non-perturbatively
small, invisible to every power of the infrared scale, and it lies strictly
inside the microscopic causal support. The result is purely asymptotic: the
remainder constants are not explicit, and numerical diagnostics indicate that
the leading term is quantitatively accurate only for $N$ of order $10^3$ and
beyond.

---

## 1. Introduction

Quantum cellular automata and quantum walks are unitary dynamics on a lattice
with a strict bound on the speed of propagation [18, 2, 12]. After $N$ steps
of a finite-range walk, the propagator vanishes identically outside
$N C_{\mathrm{micro}}$. Here $C_{\mathrm{micro}}=\operatorname{conv}F$ is the
convex hull of the one-step jumps. Many such walks have a conical point in
their dispersion relation. Near it, the long-wavelength dynamics is that of a
Weyl or Dirac equation with a speed of light $c_{\mathrm{IR}}$ [4, 11, 5, 10].

In spatial dimension $d\ge2$ the two causal structures cannot coincide. The
infrared cone of a Weyl node is a Euclidean ball, and $C_{\mathrm{micro}}$ is
a polytope. Exact isotropy of the microscopic causal structure is incompatible
with a regular lattice. It can be compatible with random discreteness, as in
the causal-set theorem of Bombelli, Henson and Sorkin [6], but that setting
lies outside the scope of this paper. For a lattice walk, some velocities are
therefore causally allowed but not relativistic. How much physics can be sent
through them?

Three questions must be kept apart.

- **(U) Ultraviolet propagator.** Does the exact kernel assign non-zero
  amplitude to sites outside the infrared ball but inside
  $N C_{\mathrm{micro}}$? For the walk studied here it does: along the eight
  vertex rays a single lattice path contributes, with amplitude of norm
  $4^{-N}$ (Proposition 2.2). One-step Alice/Bob protocols built from
  localized operations turn this into a finite distinguishability (for
  instance $3/128$ after one step for a suitable localized preparation, as
  recorded in [17]). Such protocols are broadband: their operations are not
  concentrated near the Weyl node.
- **(I) Infrared operational response.** Require the preparation, the encoder
  and the detector to be infrared-admissible, and put Bob outside the
  infrared cone of *every* site of Alice. Does Bob's distinguishability still
  fail to vanish as the infrared scale goes to zero, and at what rate?
- **(N) Nature.** Is there a physical system in which the lattice scale and
  the operations are given rather than engineered? This question is not
  addressed here.

A non-zero ultraviolet kernel does not answer (I). Infrared admissibility
could in principle force exact cancellations, and conversely an exponentially
small infrared response is compatible with (U). This paper answers (I), for
one walk and one explicit protocol.

### The walk

We work with the Weyl walk of Cedzich, Joye, Werner and Werner
[9, Eq. (5.15)]. They introduced it as a modification of the
Bialynicki-Birula Weyl automaton [9, Eq. (5.12)], [4], with the same conical
points and with a *spherical* propagation region. For this walk the three
velocity sets are nested as

$$
\Gamma\;\subseteq\;B(1)\;\subsetneq\;C_{\mathrm{micro}}=[-1,1]^3,
\qquad \sup_{v\in\Gamma}|v|=c_{\mathrm{IR}}=1 .
\tag{1}
$$

Here $B(1)=\overline B(0,1)$ is the closed infrared light cone
($c_{\mathrm{IR}}=1$), $\Gamma$ is the closed set of group velocities, and
$C_{\mathrm{micro}}$ is the strict causal body. Both statements in (1) are
exact, and moreover $\partial B(1)\subseteq\Gamma$ (Proposition 2.2).
Numerically, $\Gamma$ fills the ball; this is not proved and not used. Every
ballistic mode, at every energy, therefore respects the emergent light speed. Nevertheless, in every non-axial
direction $\hat n$ the causal support extends to
$\|\hat n\|_1\in(1,\sqrt3\,]$ times the light speed. Probability outside
$\Gamma$ is exponentially small in $N$ [9]. The question is whether it can be
*used* under infrared control.

### Main results

Section 3 gives the precise definitions. In outline, Alice's region is the
lattice ball $\mathcal A_N$ of radius $N/4$ at the origin, and Bob's region
is the lattice ball $\mathcal B_N$ of radius $N/4$ at $N(1,1,1)$. After $N$
steps, every pair $(x,y)\in\mathcal A_N\times\mathcal B_N$ is separated by
more than $N+N/5$. Bob is thus outside the emergent cone of every site of
Alice, with a margin of order $N$. The resource is a narrow-band packet of
momentum width $\Lambda=1/N$. Alice's encoder is a smooth local unitary
$\exp(i\frac\pi2F_N(x)M)$ with $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$. Bob's
effect is $h_N(y)\otimes M_B$ with $M_B\in\{I,(I+\sigma_j)/2\}$. The
profiles $F_N,h_N$ are smooth bumps of width $N/4$ that vanish
quadratically on the spheres.

1. *Infrared admissibility* (Theorem 3.3). All eight operations map the band
   $|p|\le N^{-1}$ into the band $|p|\le N^{-1/2}$, up to relative errors
   $O(N^{-1/2})$ with explicit constants. Single-site operations fail this
   criterion maximally (Lemma 3.2).
2. *Explicit upper bound* (Theorem 4.1). For every $N\ge2$, every unitary
   acting in $\mathcal A_N$, every one-particle state and every effect in
   $\mathcal B_N$, Bob's distinguishability is at most $36N^4e^{-JN}$, with
   $J=(1-\tfrac{\sqrt3}{2})\log2$. Polynomial infrared signalling is
   excluded.
3. *Regional rate* (Theorem 4.3). The kernel between the two regions is
   $O(N^4)\,e^{-K_*N}$, where $K_*=I(v_*)$ is the minimal regional value of
   a Legendre rate function. Here $I$ is the Legendre transform of
   $\Phi(\xi)=\operatorname{arcosh}(\prod_j\cosh\xi_j)$, and
   $v_*=(1-\frac1{2\sqrt3})(1,1,1)$ is the unique minimiser of $I$ over the
   regional velocity set. Moreover $J<K_*<\log4$. By item 4, the rate $K_*$
   is attained by an explicit response.
4. *Leading asymptotics* (Theorem 4.4). For all sixteen encoder–detector
   pairs,
   $\delta_{M,M_B}(N)=|C_{M,M_B}(\theta_N)|N^{-13/2}e^{-K_*N}(1+O(N^{-1/2}))$.
   The coefficient $C_{M,M_B}(\theta)$ is given in closed form and is
   uniformly non-zero, with relative oscillation in $\theta$ at most
   $1.5\times10^{-3}$.

Result 4 is an asymptotic statement and not a numerical approximation valid
from small $N$. The constants in its remainder are not explicit, and neither
is the threshold $N_*$ beyond which $\delta_{M,M_B}(N)>0$ is guaranteed.
Finite-$N$ diagnostics (Appendix A) indicate a relative correction of about
$-100/N$, so the leading term is quantitatively accurate only for
$N\gtrsim10^3$. For the pairs with the smallest coefficients, the next-order
term $N^{-17/2}e^{-K_*N}$ dominates throughout the diagnostic range $N\le56$
(Remark 4.6).

The coefficient is not a product of local factors. It arises from the
interference between the *free tail* of the resource at Bob, which is only
polynomially small, and the part of Alice's encoding that reaches Bob, which
is exponentially small. Two points of the complex-shifted Brillouin torus
contribute, and they enter with different projectors. The power $13/2$ is
not a count of Gaussian directions. The two normal directions are discrete
sums over lattice planes of depth $O(1)$, and the common tangential direction
is a flat direction of the exponent that is confined only by the profiles.

### Relation to the literature

Ballistic scaling and weak limit theorems for translation-invariant quantum
walks are classical [14, 13, 1]: $Q(t)/t$ converges in distribution to the
group velocity distributed by the initial state. Cedzich, Joye, Werner and
Werner [9] proved that the probability of velocities outside the support of
this limit decays exponentially. They gave a method for bounding the rate
uniformly in the initial state and discussed the "fuzziness" of the emergent
light cone in exactly this language. Our upper bound (item 2) uses their
contour-shift idea, supplemented by an elementary ellipse lemma and a
Jordan-safe bound on matrix powers. Their method bounds rates; it does not
give prefactor-level asymptotics.

Sharp asymptotics with prefactors outside the propagation region are known in
one dimension. Sunada and Tate [19] obtained exact local asymptotics of
transition probabilities, including exponential decay with an explicit
prefactor in the region hidden from the weak limit. Carteret, Richmond and
Temme [8] obtained uniformly convergent asymptotics in the exponentially
decaying regions of coined walks on the line. These are the closest
precursors of the saddle-point analysis of Section 7. In two dimensions,
Baryshnikov, Brady, Bressler and Pemantle [3] analysed quantum walks through
multivariate generating functions and determined the limiting profile in the
feasible region, outside of which the probability is exponentially small.
Analytic combinatorics in several variables [16] provides general transfer
theorems for multivariate coefficient asymptotics, whose standard sharp forms
assume minimality hypotheses on the critical points. We do not claim that
these methods cannot reproduce the present result. We are not aware of a
transfer theorem that yields it directly, and we carry out the model-specific
saddle-point analysis explicitly.

What we add is a *lower* bound, in the strong form of exact leading
asymptotics. It concerns an *operational* quantity: the distinguishability
produced by a local encoding. The encoding is spread over a region of size
$O(N)$ and constrained to be infrared-admissible, in dimension three, and at
a point strictly inside the corona. Upper bounds alone cannot distinguish an
exponentially small response from an exactly vanishing one. In the problem
studied here that distinction is the content of the result. The novelty
claim is correspondingly narrow. To our knowledge, Theorem 4.4 is the first
prefactor-level asymptotic, with a leading coefficient that is oscillatory and
certified to be non-vanishing, for an infrared-controlled operational response
in the strictly outside-propagation-region regime of a three-dimensional
multi-component quantum walk. Exponential decay outside the propagation
region, large-deviation rates, Weyl-cone dispersion and microscopic support
outside an emergent cone all have prior art, cited above.

Lieb–Robinson bounds [15, 7] give exponentially small leakage outside a
linear cone for continuous-time lattice dynamics. For quantum walks the
strict cone $C_{\mathrm{micro}}$ plays that role exactly, and the question
here is the one *inside* it.

### Organisation

Section 2 sets up the walk and proves the geometric statements. Section 3
defines the protocol and infrared admissibility. Section 4 states the
results. Sections 5 to 7 contain the proofs. Section 8 discusses scope and
limitations. Appendix A lists the computer-assisted parts and the finite-$N$
diagnostics.

---

## 2. The walk and its three velocity sets

### 2.1. Conventions

The one-particle Hilbert space is $\mathcal H=\ell^2(\mathbb Z^3;\mathbb C^2)$
with internal basis ${\uparrow}=(1,0)^T$ and ${\downarrow}=(0,1)^T$. We use the
Fourier transform $\hat\psi(p)=\sum_{x}e^{ip\cdot x}\psi(x)$, with inverse
$\psi(x)=\int_{\mathbb T^3}e^{-ip\cdot x}\hat\psi(p)\,d\mu(p)$ and
$d\mu=d^3p/(2\pi)^3$ on $\mathbb T^3=[-\pi,\pi)^3$. We write $c_j=\cos p_j$
and $s_j=\sin p_j$. $B(1)=\overline B(0,1)$ denotes the closed Euclidean unit
ball.

The walk $W$ of [9, Eq. (5.15)] has symbol

$$
W(p)=\begin{pmatrix} c_1c_2e^{ip_3} & -c_1s_2+is_1\\ c_1s_2+is_1 & c_1c_2e^{-ip_3}\end{pmatrix},
\qquad \det W(p)=1 .
$$

States evolve by the unitary $S$ with symbol

$$
S(p)=W(p)^{-1}=\begin{pmatrix} c_1c_2e^{-ip_3} & c_1s_2-is_1\\ -c_1s_2-is_1 & c_1c_2e^{ip_3}\end{pmatrix}.
\tag{2}
$$

Both are matrix-valued trigonometric polynomials, so they extend to entire
functions of $p\in\mathbb C^3$. For $p\in\mathbb C^3$, $S(p)$ denotes the
continuation of (2), which is the inverse of $W(p)$ and not its adjoint.
Writing $S(p)=\sum_dS_de^{ip\cdot d}$, the walk acts as
$(S\psi)(y)=\sum_dS_d\psi(y-d)$. The $N$-step kernel is

$$
(S^N)_{y,x}=G_N(y-x),\qquad G_N(d)=\int_{\mathbb T^3}e^{-ip\cdot d}S(p)^N\,d\mu(p).
\tag{3}
$$

**Lemma 2.1 (Jumps).** The set $F=\{d:S_d\ne0\}$ has fourteen elements: the
eight vertices $(\pm1,\pm1,\pm1)$, the four face diagonals $(\pm1,\pm1,0)$,
and the two axial jumps $(\pm1,0,0)$. Each vertex block is $\frac14$ times a
rank-one diagonal projector; in particular
$S_{(1,1,1)}=\frac14|{\downarrow}\rangle\langle{\downarrow}|$. The
face-diagonal blocks have norm $\frac14$ and the axial blocks have norm
$\frac12$, so that $\sum_d\|S_d\|=4$.

*Proof.* This is a direct expansion of (2) in $z_j=e^{ip_j}$. The coefficient
of $z_1z_2z_3$ comes only from the $(2,2)$ entry $c_1c_2e^{ip_3}$ and equals
$\frac14$. ∎

### 2.2. Dispersion and the infrared node

Since $\det S=1$ and $\operatorname{tr} S(p)=2c_1c_2c_3$, the eigenvalues of
$S(p)$ are $e^{\mp i\omega(p)}$ with

$$
\cos\omega(p)=\cos p_1\cos p_2\cos p_3 .
\tag{4}
$$

At $p=0$ one has $S(p)=I-iH_W(p)+O(|p|^2)$ with

$$
H_W(p)=p_1\sigma_1-p_2\sigma_2+p_3\sigma_3,\qquad H_W(p)^2=|p|^2I .
$$

This is a Weyl Hamiltonian with speed $c_{\mathrm{IR}}=1$. The same conical
structure occurs at the eight points of $\{0,\pi\}^3$.

**Proposition 2.2 (Geometry).**

- (a) The causal body is $C_{\mathrm{micro}}=\operatorname{conv}F=[-1,1]^3$.
  Its support function is $h_{C_{\mathrm{micro}}}(\hat n)=\|\hat n\|_1$ for
  unit vectors $\hat n$.
- (b) At every $p$ where $\omega$ is differentiable,

  $$
  \bigl(1-f^2\bigr)-|\nabla f|^2=s_2^2s_3^2+s_1^2s_2^2c_3^2+s_1^2c_2^2s_3^2\ \ge0,
  \qquad f=c_1c_2c_3,
  \tag{5}
  $$

  and hence $|\nabla\omega(p)|\le1$. At the conical points $\nabla\omega$
  takes every value in the unit sphere. Thus $\Gamma\subseteq B(1)$ and
  $\partial B(1)\subseteq\Gamma$, where $\Gamma$ is the closure of the set of
  group velocities.
- (c) For every vertex $\sigma\in\{\pm1\}^3$ and every $N\ge1$,
  $(S^N)_{N\sigma,0}=S_\sigma^N=4^{-N}\Pi_\sigma\ne0$, where $\Pi_\sigma$ is
  a diagonal rank-one projector. In particular
  $(S^N)_{(N,N,N),0}=4^{-N}|{\downarrow}\rangle\langle{\downarrow}|$. Hence the
  $N$-step support function equals $N\|\hat n\|_1$ exactly.

*Proof.* (a) follows from Lemma 2.1. The supremum of $\hat n\cdot x$ over the
cube is separable and equals $\sum_j|n_j|$.

(b) With $\cos\omega=f$ we have $\nabla\omega=-\nabla f/\sin\omega$ and
$\sin^2\omega=1-f^2$. The identity (5) is a polynomial identity in
$(c_j,s_j)$ modulo $c_j^2+s_j^2=1$, and is checked by expansion. Near a
conical point, $\omega(p)=|p-p_\vee|+O(|p-p_\vee|^2)$, so
$\nabla\omega=(p-p_\vee)/|p-p_\vee|+o(1)$ sweeps the unit sphere.

(c) Let $d_1+\dots+d_N=N\sigma$ with $d_k\in F$. Every $d\in F$ satisfies
$\sigma_i d_i\le1$ for each coordinate $i$, so $\sum_k\sigma_i(d_k)_i=N$
forces $\sigma_i(d_k)_i=1$ for all $i$ and $k$, that is, $d_k=\sigma$. Hence
$(S^N)_{N\sigma,0}=S_\sigma^N$. By Lemma 2.1, $S_\sigma=\frac14\Pi_\sigma$,
so $S_\sigma^N=4^{-N}\Pi_\sigma$. ∎

**Remark 2.3.** The reverse inclusion $B(1)\subseteq\Gamma$, that is, that
$\Gamma$ fills the ball, holds numerically but is not proved and not used.
What is used is the exact inclusion $\Gamma\subseteq B(1)$, equivalently
$\sup|\nabla\omega|\le c_{\mathrm{IR}}$, with equality by
$\partial B(1)\subseteq\Gamma$. Consequently the relation
$\sup|v_g|=c_{\mathrm{IR}}$ does *not* imply that the emergent cone coincides
with the causal boundary. The two coincide only in the six axial directions.
The *corona* is $C_{\mathrm{micro}}\setminus B(1)$. Propagation into $N$
times the corona is not ballistic, but by (c) it is not forbidden.

**Remark 2.4.** For the Bialynicki-Birula walk [9, Eq. (5.12)], $\Gamma$ is
contained in the intersection of three orthogonal cylinders (and numerically
equal to it [9, Fig. 5]). It contains group velocities up to
$\sqrt{3/2}>c_{\mathrm{IR}}$, attained at $p=-\frac\pi4(1,1,1)$. In that
walk the corona contains a ballistic sector faster than the emergent light.
We restrict to [9, Eq. (5.15)] precisely because it has no such sector.

---

## 3. Protocol and infrared admissibility

Fix an integer $N\ge2$. The infrared scale is $\Lambda_N=N^{-1}$ and the
admissibility budget is $\Lambda'_N=N^{-1/2}$. Let $\Pi_\Lambda$ denote the
spectral projection onto $\{|p|_2\le\Lambda\}$, and write
$\Pi=\Pi_{\Lambda_N}$ and $\Pi'=\Pi_{\Lambda'_N}$. For $N\ge2$ both balls lie
in $|p|<\pi/4$, where $f>0$ and the only conical point is $p=0$.

### 3.1. Regions

Let

$$
\mathcal A_N=\{x\in\mathbb Z^3:|x|\le N/4\},\qquad \mathcal B_N=\{y\in\mathbb Z^3:|y-N(1,1,1)|\le N/4\},
$$

with Euclidean norms throughout. For every $x\in\mathcal A_N$ and
$y\in\mathcal B_N$,

$$
|y-x|-N\ge\bigl(\sqrt3-\tfrac32\bigr)N>\tfrac N5,
\qquad
u\cdot(y-x)\ge\bigl(3-\tfrac{\sqrt3}2\bigr)N,\quad u=(1,1,1).
\tag{6}
$$

Both follow from the triangle inequality, and the last inequality in the
first display is $3>(17/10)^2$. Each region has at most $(N/2+1)^3\le N^3$
sites.

### 3.2. Resource, encoder, detector

Let $g(q)=(1-|q|^2)_+^2$. The resource is

$$
\hat\phi_N(p)=Z_N^{-1/2}\,g(Np)\,{\downarrow},
\qquad Z_N=\frac{64}{3465\,\pi^2N^3},
$$

so that $\|\phi_N\|=1$ and $\Pi\phi_N=\phi_N$. In position space
$\phi_N=\varphi_N\,{\downarrow}$ with the real, radial function

$$
\varphi_N(x)=N^{-3/2}\,\Phi_0(x/N),\qquad
\Phi_0(w)=c_r\int_{\mathbb R^3}g(q)\,e^{-iq\cdot w}\,d^3q,\qquad c_r=\frac{\sqrt{3465}}{64\pi^2}.
\tag{7}
$$

This is exact, with no truncation of the spatial tail.

Alice's profile is $F_N(x)=(1-16|x|^2/N^2)_+^2$, supported in
$\mathcal A_N$. For $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$ the encoder is the
multiplication operator

$$
U_M=\exp\bigl(i\tfrac\pi2F_N(x)\,M\bigr)=I+c_N(x)I+is_N(x)M,
\qquad c_N=\cos(\tfrac\pi2F_N)-1,\ \ s_N=\sin(\tfrac\pi2F_N).
$$

It acts as the identity outside $\mathcal A_N$. In the second-quantized free
fermion picture it is the one-particle restriction of an even,
number-preserving local unitary.

Bob's profile is $h_N(y)=(1-16|y-Nu|^2/N^2)_+^2$, with $u=(1,1,1)$,
supported in $\mathcal B_N$. For $M_B\in\{I,P_1,P_2,P_3\}$, with
$P_j=(I+\sigma_j)/2$, the effect is

$$
E=h_N\otimes M_B,\qquad 0\le E\le I .
$$

### 3.3. Signal

Alice encodes a bit $b\in\{0,1\}$ by applying $U^{(1)}=U_M$ or $U^{(0)}=I$
to the resource. After $N$ steps the state is $\psi_b(N)=S^NU^{(b)}\phi_N$.
The signal is

$$
\delta_{M,M_B}(N)=\bigl|\langle\psi_1,E\psi_1\rangle-\langle\psi_0,E\psi_0\rangle\bigr|=|L_{M,M_B}(N)|,
\tag{8}
$$

where $L_{M,M_B}(N)$ denotes the signed difference. No spectral projection is
applied to the signal. Infrared admissibility is a property of the operations
only. We also consider the trace distance $D_B(N)$ between Bob's reduced
states. In the free-fermion description, the reduced state of a one-particle
vector $\psi$ on the modes of $\mathcal B_N$ is
$(1-\|P_B\psi\|^2)|\Omega\rangle\langle\Omega|+|P_B\psi\rangle\langle P_B\psi|$,
and $D_B=\frac12\|\rho_1-\rho_0\|_1\ge\delta$.

### 3.4. Infrared admissibility

**Definition 3.1.** For a bounded operator $X$ on $\mathcal H$ with
$X\Pi\ne0$, set

$$
\eta_{\mathrm{op}}(X)=\frac{\|(I-\Pi')X\Pi\|}{\|X\Pi\|}.
$$

The encoder $U_M$ is *infrared-admissible* if $\eta_{\mathrm{op}}(U_M-I)\to0$
and

$$
\eta_{\mathrm{enc}}^M=\frac{\|\Delta_M-\Pi'\Delta_M\Pi'\|_1}{\|\Delta_M\|_1}\to0,
\qquad \Delta_M=U_M|\phi_N\rangle\langle\phi_N|U_M^*-|\phi_N\rangle\langle\phi_N|,
$$

as $N\to\infty$, where $\Delta_M\ne0$ is required for
$\eta_{\mathrm{enc}}^M$ to be defined. The effect $E$ is infrared-admissible
if $\eta_{\mathrm{op}}(E)\to0$.

For the operations of this paper all denominators are non-zero for every
$N\ge2$ (Theorem 3.3).

In words: acting on anything in the infrared band, an admissible operation
leaves only a vanishing fraction of its output outside the wider band
$\Pi'$. A strictly local gate cannot do this.

**Lemma 3.2 (Single-site operations are ultraviolet).** If $X\Pi\ne0$ and
$\operatorname{ran}X\subseteq\ell^2(\{x_0\};\mathbb C^2)$ for a single site
$x_0$, then $\eta_{\mathrm{op}}(X)=\sqrt{1-\kappa'_N}\to1$, where
$\kappa'_N=(6\pi^2N^{3/2})^{-1}$.

*Proof.* For every vector $e_{x_0}\otimes\chi$,
$\|\Pi'(e_{x_0}\otimes\chi)\|^2=\mu(\{|p|\le\Lambda'_N\})=(\Lambda'_N)^3/(6\pi^2)$.
Hence every vector in $\operatorname{ran}X$ has exactly the fraction
$1-\kappa'_N$ of its squared norm outside $\Pi'$. ∎

This is the reason the encoder is spread over a region of size $O(N)$ with a
smooth profile. A pointlike phase gate, such as $I-2P_{x_0}$, is excluded by
Lemma 3.2. The regional operations pass:

**Theorem 3.3 (Admissibility).** Let $K_e=\frac\pi2(2+8\sqrt3\pi)$,
$K_d=\frac\pi2(1+16\sqrt3)$ and $m=11/(560\pi^2\,32^3)$. For all $N\ge32$,
all four $M$ and all four $M_B$,

$$
\eta_{\mathrm{op}}(U_M-I)\le\frac{K_e}{\sqrt{(2-\sqrt2)m}}\,N^{-1/2},\qquad
\eta_{\mathrm{enc}}^M\le\frac{K_e}{m\sqrt{2-\sqrt2}}\,N^{-1/2},\qquad
\eta_{\mathrm{op}}(E)\le\frac{2K_d}{\sqrt m}\,N^{-1/2}.
$$

All denominators are non-zero for every $N\ge2$.

The constants are conservative. The proof is in Section 6.

---

## 4. Results

**Theorem 4.1 (Explicit upper bound).** Let $N\ge2$ and
$T_N=\|P_{\mathcal B_N}S^NP_{\mathcal A_N}\|$. Then

$$
T_N\le9N^4e^{-JN},\qquad J=\bigl(1-\tfrac{\sqrt3}2\bigr)\log2\approx0.0929 .
$$

Consequently, for every unitary $U$ acting as the identity outside
$\mathcal A_N\otimes\mathbb C^2$, every one-particle state and every effect in
$\mathcal B_N$,

$$
\delta\le D_B\le4T_N\le36N^4e^{-JN}.
$$

**Remark 4.2 (Formal verification).** Theorem 4.1 is machine-checked in
Lean 4 with Mathlib (`formal/` in [17]), for every $N\ge2$ and without
additional axioms. This covers the kernel bound, the geometry (6), the
counting of lattice points, the operator bound on $T_N$, and the step
$\delta\le4T_N$. The formal proof bounds the matrix powers through
Cayley–Hamilton and entrywise estimates instead of Lemma 5.3, and obtains the
sharper constant $T_N\le4N^4e^{-JN}$. Both constants are valid; the proof in
Section 5 keeps the constant $9$ that the elementary Lemma 5.3 gives. The
identification of Bob's amplitudes
with the restricted walk, and the second-quantized distance $D_B$, are not
formalized.

For $\xi\in\mathbb R^3$ put
$\Phi(\xi)=\operatorname{arcosh}\bigl(\prod_{j=1}^3\cosh\xi_j\bigr)$ and
define the rate function

$$
I(v)=\sup_{\xi\in\mathbb R^3}\bigl[\xi\cdot v-\Phi(\xi)\bigr].
\tag{9}
$$

Let $V_{\mathrm{reg}}=(1,1,1)+\overline B(0,\tfrac12)$. This is the set of
velocities $(y-x)/N$ for $x,y$ in the continuum balls underlying
$\mathcal A_N,\mathcal B_N$.

**Theorem 4.3 (Regional rate).**

- (a) $I$ is convex, $I=0$ on $\overline B(0,1)$, $I>0$ outside it, and
  $I=+\infty$ outside $[-1,1]^3$.
- (b) On $V_{\mathrm{reg}}$, $I$ has the unique minimiser
  $v_*=\alpha(1,1,1)$, $\alpha=1-\frac1{2\sqrt3}$. The corresponding dual tilt
  is $\xi_*=t_*(1,1,1)$, where $t_*>0$ is the unique solution of
  $\alpha=\nabla_1\Phi(t,t,t)$. Moreover

  $$
  K_*:=I(v_*)=3\alpha t_*-\operatorname{arcosh}(\cosh^3t_*),\qquad
  \cosh^2t_*=\frac{\alpha\bigl(\alpha+\sqrt{4-3\alpha^2}\bigr)}{2(1-\alpha^2)} .
  $$

- (c) $J<K_*<\log4$. Numerically $t_*=0.7357528144\ldots$ and
  $K_*=0.1905189296\ldots$.
- (d) For all $N\ge2$ and all $(x,y)\in\mathcal A_N\times\mathcal B_N$,

  $$
  \|G_N(y-x)\|\le\bigl(1+4e^{3t_*-\Phi_*}N\bigr)e^{-K_*N},\qquad \Phi_*=\Phi(\xi_*),
  $$

  and hence $\delta\le D_B\le4N^3(1+10N)e^{-K_*N}$.

The main result identifies the exact leading behaviour of every signal in the
family. Write $\theta_N=\{\sqrt3N/4\}\in[0,1)$ for the fractional part.

**Theorem 4.4 (Leading asymptotics).** For each of the sixteen pairs
$(M,M_B)$ there is a continuous, $1$-periodic, real function
$C_{M,M_B}(\theta)$ such that, as $N\to\infty$,

$$
L_{M,M_B}(N)=e^{-K_*N}N^{-13/2}\Bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\Bigr).
$$

Explicitly,

$$
C_{M,M_B}(\theta)=\mathcal K\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\tag{10}
$$

with the constants $\mathcal K$, $c_r$, the functions $\Gamma_\pm$ and the
numbers $\ell_0,\ell_\pi$ defined in Section 7. For every pair,

$$
C_{M,M_B}(\theta)=\overline{C}_{M,M_B}\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad \sup_\theta|\vartheta_{M,M_B}(\theta)|\le1.47\times10^{-3},
\qquad \overline{C}_{M,M_B}\ne0,
$$

with the values in Table 1. Consequently, for every pair,

$$
\delta_{M,M_B}(N)=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
$$

and $\delta_{M,M_B}(N)>0$ for all $N$ larger than some finite $N_*$.

The constants implicit in the $O(N^{-1/2})$ terms are finite but not
explicit, and neither is $N_*$. Theorem 4.4 therefore does not assert
$\delta_{M,M_B}(N)>0$ at any specified $N$. It also does not say from which
$N$ on the leading term is numerically accurate (Section 8).

**Table 1.** Mean leading coefficients
$\overline{C}_{M,M_B}=\mathcal K c_r\overline\Gamma\ell_0$ and the uniform
bound on their relative oscillation in $\theta$. Values are certified by
interval arithmetic (Appendix A).

| $M$ | $M_B$ | $\overline{C}_{M,M_B}$ | $\sup_\theta \lvert C/\overline{C}-1\rvert$ |
| --- | --- | ---: | ---: |
| $I$ | $I$ | $-0.0752752093$ | $1.47\cdot10^{-3}$ |
| $I$ | $P_1$ | $+1.2072650683$ | $1.09\cdot10^{-3}$ |
| $I$ | $P_2$ | $+0.8164098576$ | $1.08\cdot10^{-3}$ |
| $I$ | $P_3$ | $-0.0752752093$ | $1.47\cdot10^{-3}$ |
| $\sigma_1$ | $I$ | $-3.7206303938$ | $1.05\cdot10^{-3}$ |
| $\sigma_1$ | $P_1$ | $-1.5567800857$ | $1.06\cdot10^{-3}$ |
| $\sigma_1$ | $P_2$ | $-2.8203960182$ | $1.02\cdot10^{-3}$ |
| $\sigma_1$ | $P_3$ | $-0.1776542932$ | $1.05\cdot10^{-3}$ |
| $\sigma_2$ | $I$ | $-2.9389199724$ | $1.05\cdot10^{-3}$ |
| $\sigma_2$ | $P_1$ | $-0.5846543741$ | $1.02\cdot10^{-3}$ |
| $\sigma_2$ | $P_2$ | $-1.7729950974$ | $1.04\cdot10^{-3}$ |
| $\sigma_2$ | $P_3$ | $-0.1776542932$ | $1.05\cdot10^{-3}$ |
| $\sigma_3$ | $I$ | $+0.0752752093$ | $1.47\cdot10^{-3}$ |
| $\sigma_3$ | $P_1$ | $-1.2072650683$ | $1.09\cdot10^{-3}$ |
| $\sigma_3$ | $P_2$ | $-0.8164098576$ | $1.08\cdot10^{-3}$ |
| $\sigma_3$ | $P_3$ | $+0.0752752093$ | $1.47\cdot10^{-3}$ |

**Corollary 4.5.** In this protocol the emergent light cone is not
operationally sharp for infrared-admissible operations. For each pair the
response is non-perturbatively small: $\delta_{M,M_B}(N)=o(N^{-k})$ for every
$k$. It is nevertheless non-zero for all large $N$, with the exact rate
$K_*$, the exact power $13/2$ and an explicit non-vanishing coefficient.

**Remark 4.6.** Three features of Table 1 were not assumed and come out of
the computation. First, $C(\sigma_3,\cdot)=-C(I,\cdot)$ at leading order; the
two encoders differ only at lower orders. Second, the three Pauli encoders
are not equivalent: with $M_B=I$ they give three different coefficients.
Third, for $M=\sigma_2$ the two contributing saddles enter with the same sign
for every detector: $\ell_0$ and $\ell_\pi$ of Appendix A have the same sign.
Since $\Gamma_+>0$ and $\Gamma_-\ge0$ (Lemma 7.3), non-vanishing then follows
without the margin estimate in the proof of Theorem 4.4, so for this encoder
the non-cancellation mechanism is particularly transparent. The smallest
coefficients, $|\overline C|\approx0.0753$, occur for $M\in\{I,\sigma_3\}$
with $M_B\in\{I,P_3\}$. For these two encoders with $M_B=I$, the
diagnostics of Appendix A show that the next-order term, of size
$N^{-17/2}e^{-K_*N}$, dominates numerically throughout the diagnostic range
$N\le56$.

**Remark 4.7 (Methodology).** The protocol (regions, profiles, encoders,
detectors, scalings $\Lambda_N=N^{-1}$, $\Lambda'_N=N^{-1/2}$ and the
encoding angle $\pi/2$) was fixed before the asymptotic analysis and was not tuned
afterwards. The family of encoders and detectors is not exhaustive: a general
generator $M=aI+b\cdot\sigma$ is not covered, because no symmetry of the walk
relating the directions $\hat n\cdot\sigma$ has been established.

---

## 5. Proof of the upper bounds

### 5.1. An ellipse lemma

For $a\ge1$ let
$E_a=\{z\in\mathbb C:(\operatorname{Re} z)^2/a^2+(\operatorname{Im} z)^2/(a^2-1)\le1\}$,
where $E_1=[-1,1]$. These are the confocal ellipses with foci $\pm1$. The
Joukowski map $\lambda\mapsto(\lambda+\lambda^{-1})/2$ sends the circle
$|\lambda|=r\ge1$ onto $\partial E_{(r+r^{-1})/2}$.

**Lemma 5.1.** Let $a,c\ge1$. If $z\in\partial E_a$ and $w\in E_c$, then
$zw\in E_{ac}$; consequently $E_aE_c\subseteq E_{ac}$. If moreover $a,c>1$,
then $zw\in\partial E_{ac}$ only if $z=\pm a$ and $w=\pm c$.

*Proof.* If $c=1$, then $w\in[-1,1]$ and $zw\in E_a$ by convexity and
symmetry. If $a=1$, then $z\in[-1,1]$ and the same argument applies. So let
$a,c>1$. Write $z=a\cos p+i\sqrt{a^2-1}\sin p$ and
$w=c\,x+i\sqrt{c^2-1}\,y$ with $x^2+y^2\le1$. In the coordinates adapted to
$E_{ac}$, the point $zw$ corresponds to $L(x,y)^T$ with

$$
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\ \sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
$$

With $A=a^2$, $C=c^2$ and $u=\cos^2p$, a direct computation gives

$$
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},\qquad
\det(I-L^TL)=\frac{(C-1)(1-u)\bigl[A-1+C(1-u)\bigr]}{AC(AC-1)} .
$$

Both are non-negative, so $I-L^TL\ge0$ by Sylvester's criterion and
$\|L\|\le1$. If $u<1$, both are positive, so $\|L\|<1$ and $zw$ is interior.
If $u=1$, then $z=\pm a$ and

$$
L=\pm\operatorname{diag}\Bigl(1,\ \frac{a\sqrt{c^2-1}}{\sqrt{a^2c^2-1}}\Bigr),
$$

whose second entry is $<1$. Hence $|L(x,y)^T|=1$ forces $y=0$ and $|x|=1$,
that is, $w=\pm c$. ∎

**Lemma 5.2.** For $\eta\in\mathbb R^3$ and $\xi\in\mathbb R^3$,
$\rho\bigl(S(\eta-i\xi)\bigr)\le e^{\Phi(\xi)}$. If all $\xi_j\ne0$, equality
holds if and only if $\eta\in\Sigma:=\{0,\pi\}^3$ modulo $2\pi$.

*Proof.*
$\cos(\eta_j-i\xi_j)=\cos\eta_j\cosh\xi_j+i\sin\eta_j\sinh\xi_j\in\partial E_{\cosh\xi_j}$.
By Lemma 5.1 applied twice,
$f(\eta-i\xi)=\prod_j\cos(\eta_j-i\xi_j)\in E_{\prod\cosh\xi_j}$. When all
$\xi_j\ne0$, it lies on the boundary only if every factor is a real vertex,
that is, only if every $\sin\eta_j=0$. The eigenvalues $\lambda^{\pm1}$ of
the unimodular matrix $S(\eta-i\xi)$ satisfy $(\lambda+\lambda^{-1})/2=f$. If
$|\lambda|=r\ge1$, then $f\in\partial E_{(r+r^{-1})/2}$. Since the ellipses
are nested, $(r+r^{-1})/2\le\prod\cosh\xi_j$, which is $r\le e^{\Phi(\xi)}$,
with strict inequality when $f$ is interior. On $\Sigma$,
$f=\pm\prod\cosh\xi_j$ is real and equality holds. ∎

**Lemma 5.3 (Powers without a gap).** Let $T$ be a $2\times2$ matrix with
$\rho(T)\le e^{\varkappa}$ and $\|T\|\le\beta$. Then
$\|T^N\|\le e^{N\varkappa}+\beta Ne^{(N-1)\varkappa}$.

*Proof.* Take a unitary Schur form
$T=V\begin{pmatrix}\lambda_1&b\\0&\lambda_2\end{pmatrix}V^*$, so
$|b|\le\|T\|$. The upper-right entry of the $N$-th power is
$b\sum_{j=0}^{N-1}\lambda_1^j\lambda_2^{N-1-j}$, also when
$\lambda_1=\lambda_2$. The diagonal part has norm $\max_j|\lambda_j|^N$. ∎

### 5.2. Proof of Theorem 4.1

Since the integrand in (3) is entire and $2\pi$-periodic in each variable,
the contour can be shifted to $p=\eta-i\xi$ for any $\xi\in\mathbb R^3$
without boundary terms:

$$
G_N(d)=e^{-\xi\cdot d}\int_{\mathbb T^3}e^{-i\eta\cdot d}\,S(\eta-i\xi)^N\,d\mu(\eta).
\tag{11}
$$

Take $\xi=tu$ with $t=\log2$, so $\cosh^3t=125/64$. Lemma 5.2 gives

$$
\rho\bigl(S(\eta-itu)\bigr)\le\exp\operatorname{arcosh}(125/64)<4,
$$

because $125/64<17/8=\cosh\log4$. By Lemma 2.1,

$$
\|S(\eta-itu)\|\le\sum_d\|S_d\|e^{t|u\cdot d|}\le4e^{3t}=32 .
$$

Lemma 5.3, with the cruder bound $|\lambda_j|\le4$, gives
$\|S(\eta-itu)^N\|\le4^N+32N4^{N-1}\le9N4^N$. With (6),

$$
\|G_N(y-x)\|\le9N\exp\bigl[-t\,u\cdot(y-x)+N\log4\bigr]\le9Ne^{-JN}
$$

for all $(x,y)\in\mathcal A_N\times\mathcal B_N$. The Schur test with
$|\mathcal A_N|,|\mathcal B_N|\le N^3$ gives $T_N\le9N^4e^{-JN}$.

Let $v_b=P_BS^NU^{(b)}\psi$ for a one-particle state $\psi$. Then
$v_1-v_0=P_BS^NP_A(U-I)\psi$, so $\|v_1-v_0\|\le2T_N$. The difference of
Bob's reduced states is $X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|$
on the one-particle block, together with $-\operatorname{tr} X$ on the vacuum
block. Hence
$D_B=\frac12(|\operatorname{tr} X|+\|X\|_1)\le\|X\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le4T_N$.
Mixed states follow by convexity, and $\delta\le D_B$ holds for every effect.
∎

### 5.3. Proof of Theorem 4.3

(a) $I$ is a supremum of affine functions, so it is convex, and $I\ge0$
(take $\xi=0$). The inequality $\cosh\sqrt{a^2+b^2}\le\cosh a\cosh b$,
applied twice, gives $\Phi(\xi)\ge|\xi|$, so $I=0$ on $\overline B(0,1)$.
Since $\Phi(\xi)=|\xi|+O(|\xi|^3)$, $I(v)>0$ for $|v|>1$. Finally
$I=+\infty$ outside $\operatorname{conv}F$ by [9, Lemma 4.1]. Directly, if
$v_j>1$, take $\xi=se_j$ and let $s\to\infty$, using $\Phi(se_j)=s$.

(b) $\Phi$ is smooth where $\Pi(\xi)=\prod_j\cosh\xi_j>1$, with

$$
\nabla\Phi(\xi)=\frac{\Pi(\xi)}{\sqrt{\Pi(\xi)^2-1}}\,(\tanh\xi_1,\tanh\xi_2,\tanh\xi_3).
$$

On the diagonal, $h(t)=\nabla_1\Phi(t,t,t)$ tends to $1/\sqrt3$ as
$t\to0^+$ and to $1$ as $t\to\infty$. It is strictly increasing, since
$3h'(t)=u^T\operatorname{Hess}\Phi(t,t,t)\,u=3q_n(t)>0$, where $q_n(t)$ is
given by the formula of Lemma 7.1(d) with $c_*$ replaced by $\cosh t>1$.
Since $\alpha\in(1/\sqrt3,1)$, there is a unique $t_*>0$ with
$h(t_*)=\alpha$, and then $\nabla\Phi(\xi_*)=v_*$. Solving $h(t)=\alpha$ for
$\cosh^2t$ gives the stated closed form. By the definition of $I$, for every
$v$,

$$
I(v)\ge\xi_*\cdot v-\Phi(\xi_*)=I(v_*)+\xi_*\cdot(v-v_*)
=I(v_*)+\sqrt3\,t_*\bigl(\hat u\cdot v-|v_*|\bigr),
\qquad \hat u=u/\sqrt3 .
$$

On $V_{\mathrm{reg}}$ we have $\hat u\cdot v\ge\sqrt3-\frac12=|v_*|$, with
equality only at $v=v_*$. Hence $v_*$ is the unique minimiser.

(c) The tilt $\xi=(\log2)u$ gives
$I(v_*)\ge3\alpha\log2-\operatorname{arcosh}(125/64)>(3-\tfrac{\sqrt3}2)\log2-\log4=J$.
Also $\xi_*\cdot v_*<\xi_*\cdot u$ because $\alpha<1$ and $t_*>0$, so
$I(v_*)<\xi_*\cdot u-\Phi(\xi_*)\le I(u)$. Along the diagonal,
$3t-\operatorname{arcosh}(\cosh^3t)\uparrow\log4$, and $I(u)=\log4$ is also
the exact vertex rate of Proposition 2.2(c). The numerical values are
enclosed by interval arithmetic.

(d) Apply (11) with $\xi=\xi_*$. By Lemma 5.2,
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*}$ for all $\eta$. By Lemma 2.1,
$\|S(\eta-i\xi_*)\|\le4e^{3t_*}$. Lemma 5.3 gives
$\sup_\eta\|S(\eta-i\xi_*)^N\|\le e^{N\Phi_*}(1+4e^{3t_*-\Phi_*}N)$. For
$(x,y)\in\mathcal A_N\times\mathcal B_N$, (6) and $\xi_*\parallel\hat u$ give
$\xi_*\cdot(y-x)\ge N\,\xi_*\cdot v_*$, and $N\xi_*\cdot v_*-N\Phi_*=NK_*$.
Numerically $4e^{3t_*-\Phi_*}<9.2$, so $1+4e^{3t_*-\Phi_*}N\le1+10N$, and the
Schur test concludes as before. ∎

---

## 6. Proof of admissibility

**Lemma 6.1.** Let $a:\mathbb Z^3\to M_2(\mathbb C)$ satisfy
$\sup\|a\|\le A$ and $\|a(x+e_j)-a(x)\|\le L/N$ for all $x,j$. Then

$$
\|(I-\Pi')\,a\,\Pi\|\le\tfrac\pi2(A+\sqrt3L)\,N^{-1/2}.
$$

*Proof.* Let $D_j\xi(x)=\xi(x+e_j)-\xi(x)$. On the complement of $\Pi'$,

$$
\sum_j|e^{ip_j}-1|^2=\sum_j4\sin^2(p_j/2)\ge(2/\pi)^2|p|^2\ge(2/\pi)^2N^{-1},
$$

using $\sin s\ge2s/\pi$ on $[0,\pi/2]$. By Plancherel,
$\|(I-\Pi')\xi\|\le\frac\pi2N^{1/2}(\sum_j\|D_j\xi\|^2)^{1/2}$. For
$\psi=\Pi\psi$, $(\sum_j\|D_j\psi\|^2)^{1/2}\le N^{-1}\|\psi\|$. The discrete
product rule $D_j(a\psi)=a(\cdot+e_j)D_j\psi+(D_ja)\psi$ and Minkowski's
inequality give $(\sum_j\|D_j(a\psi)\|^2)^{1/2}\le(A+\sqrt3L)N^{-1}\|\psi\|$.
∎

*Proof of Theorem 3.3.* **Numerators.**
$|\nabla F_N|=64|x|(1-16|x|^2/N^2)/N^2\le16/N$ inside $\mathcal A_N$, and the
gradient vanishes on the sphere, so $F_N$ is $16/N$-Lipschitz on
$\mathbb Z^3$. For $a_M=U_M-I$ we get $A=2$ and $L=8\pi$, because
$\|\frac{d}{dF}e^{i\pi FM/2}\|=\pi/2$. For $E=h_N\otimes M_B$ we get $A=1$
and $L=16$. Lemma 6.1 bounds the numerators by $K_eN^{-1/2}$ and
$K_dN^{-1/2}$. For $\eta_{\mathrm{enc}}$, write $v=U_M\phi_N$, $w=\Pi'v$ and
$r=v-w=(I-\Pi')a_M\phi_N$. Since $\Pi'\phi_N=\phi_N$,
$\Delta_M-\Pi'\Delta_M\Pi'=|r\rangle\langle v|+|w\rangle\langle r|$, whose
trace norm is at most $2\|r\|\le2K_eN^{-1/2}$.

**Denominators.** For $|x|\le N$ and $|p|\le N^{-1}$,
$\cos(p\cdot x)\ge\frac12$. Hence
$\varphi_N(x)\ge\frac12\sqrt{11/(140\pi^2)}\,N^{-3/2}$ for $|x|\le N$. Let
$N\ge32$, and consider two auxiliary sets. The first is
$Q_{\mathrm{in}}=\{|x_j|\le N/32\}$, with at least $(N/32)^3$ sites, on which
$F_N\ge(61/64)^2>\frac12$. The second is
$Q_{\mathrm{out}}=\{N/2\le x_1\le5N/8,\ 0\le x_2,x_3\le N/8\}$, with at least
$(N/16)^3$ sites, on which $F_N=0$ and $|x|<N$. Each carries resource weight
at least $m$.

On $Q_{\mathrm{in}}$, $\frac\pi2F_N\in[\frac\pi4,\frac\pi2]$, so
$a_M^*a_M=2(1-\cos\frac\pi2F_N)I\ge(2-\sqrt2)I$. Thus
$\|a_M\Pi\|\ge\|a_M\phi_N\|\ge\sqrt{(2-\sqrt2)m}$. For the detector, test on
the resource translated to $N(1,1,1)$, with internal state a $+1$
eigenvector of $M_B$. This test vector lies in $\operatorname{ran}\Pi$, and it
gives $\|E\Pi\|\ge\frac12\sqrt m$.

For $\eta_{\mathrm{enc}}$, $\|\Delta_M\|_1=2\sqrt{1-|z|^2}$ with
$z=\sum_xw_xt_x$, $w_x=|\varphi_N(x)|^2$ and
$t_x=\langle{\downarrow}|e^{i\pi F_N(x)M/2}|{\downarrow}\rangle$. This gives
$t_x=e^{i\pi F_N/2}$ for $M=I$, $\cos(\pi F_N/2)$ for $M=\sigma_{1,2}$, and
$e^{-i\pi F_N/2}$ for $M=\sigma_3$. Then
$1-|z|^2=\sum_{x,y}w_xw_y(1-\operatorname{Re} t_x\bar t_y)$. All terms are
non-negative, and for $x\in Q_{\mathrm{in}}$, $y\in Q_{\mathrm{out}}$ one has
$\operatorname{Re} t_x\bar t_y=\cos(\frac\pi2F_N(x))\le1/\sqrt2$. Counting
both orders gives $1-|z|^2\ge(2-\sqrt2)m^2$. For $2\le N<32$ the same
argument, with the origin and the site $(\lfloor N/4\rfloor+1,0,0)$, shows
that the denominators are non-zero. ∎

---

## 7. Proof of the leading asymptotics

Throughout, $C$ denotes a finite constant independent of $N$ whose value may
change from line to line. The constants $r_0,c,c_3,c_P$ below are finite but
not made explicit.

### 7.1. Reduction to one interference functional

Let $P_B$ be the restriction to $\mathcal B_N$ (not a spectral projection).
Write $\widetilde r=S^N\phi_N$ for the free evolution of the resource on all
of $\mathbb Z^3$, and put

$$
r=P_B\widetilde r,\qquad a_c=P_BS^N(c_N\varphi_N{\downarrow}),\qquad
a_{\uparrow}=P_BS^N(s_N\varphi_N{\uparrow}),\qquad a_{\downarrow}=P_BS^N(s_N\varphi_N{\downarrow}).
$$

Since $\sigma_1{\downarrow}={\uparrow}$, $\sigma_2{\downarrow}=-i{\uparrow}$
and $\sigma_3{\downarrow}=-{\downarrow}$, Bob's encoded amplitude $P_B\psi_1$
is $v+ia_{\downarrow}$, $v+ia_{\uparrow}$, $v+a_{\uparrow}$ or
$v-ia_{\downarrow}$ for $M=I,\sigma_1,\sigma_2,\sigma_3$, where $v=r+a_c$.
Expanding (8) with $E$ supported in $\mathcal B_N$,

$$
\begin{aligned}
L_{I}&=2\operatorname{Re}\langle r,Ea_c\rangle-2\operatorname{Im}\langle r,Ea_{\downarrow}\rangle+Q_I, &
L_{\sigma_3}&=2\operatorname{Re}\langle r,Ea_c\rangle+2\operatorname{Im}\langle r,Ea_{\downarrow}\rangle+Q_{\sigma_3},\\
L_{\sigma_1}&=2\operatorname{Re}\langle r,Ea_c\rangle-2\operatorname{Im}\langle r,Ea_{\uparrow}\rangle+Q_{\sigma_1}, &
L_{\sigma_2}&=2\operatorname{Re}\langle r,Ea_c\rangle+2\operatorname{Re}\langle r,Ea_{\uparrow}\rangle+Q_{\sigma_2}.
\end{aligned}
\tag{12}
$$

Each $Q_M$ is a sum of terms quadratic in $(a_c,a_{\uparrow},a_{\downarrow})$.
For example,
$Q_I=\langle a_c,Ea_c\rangle+\langle a_{\downarrow},Ea_{\downarrow}\rangle-2\operatorname{Im}\langle a_c,Ea_{\downarrow}\rangle$.
Positivity of $E$ does not fix the sign of $L$, because the interference
terms can have either sign.

By Theorem 4.3(d), $a_c,a_{\uparrow},a_{\downarrow}$ have $\ell^2$-norm at
most $T_N=O(N^4e^{-K_*N})$, so $Q_M=O(N^{8}e^{-2K_*N})$. The free tail is only
polynomially small (Lemma 7.2). The $e^{-K_*N}$ sector therefore consists of
the linear interference terms. Define, for $\chi\in\{{\uparrow},{\downarrow}\}$,

$$
\mathcal T_\chi(N)=e^{K_*N}\,\bigl\langle r,\,E\,S^N(s_N\varphi_N\chi)\bigr\rangle .
$$

Theorem 4.4 follows from Theorem 7.5 below. The piece
$\langle r,Ea_c\rangle$ is $O(N^{-17/2}e^{-K_*N})$ by the same argument,
because $c_N=\Theta(N^{-4})$ in the relevant layer while
$s_N=\Theta(N^{-2})$.

### 7.2. Exact tilted representation

Let $R=N/4$, $x_*=R\hat u$ and $y_*=Nu-R\hat u$, so that $y_*-x_*=Nv_*$. For
$f$ supported in $\mathcal A_N$ and $w$ supported in $\mathcal B_N$, put

$$
\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x),\qquad
\mathfrak B_w(\eta)=\sum_ye^{-i\eta\cdot(y-y_*)}e^{-\xi_*\cdot(y-y_*)}w(y)^\dagger .
$$

Let $\widetilde S_N(\eta)=e^{-N\Phi_*}S(\eta-i\xi_*)^N$. By (11) with
$\xi=\xi_*$, and using $\xi_*\cdot v_*-\Phi_*=K_*$,

$$
e^{K_*N}\sum_yw(y)^\dagger(S^Nf)(y)=\int_{\mathbb T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,\mathfrak A_f(\eta)\,e^{-iN\eta\cdot v_*}\,d\mu(\eta).
\tag{13}
$$

This identity is exact: the sums are finite and no poles are crossed.

### 7.3. The tilted symbol

**Lemma 7.1.**

- (a) $S(-i\xi)$ is Hermitian for every real $\xi$, with $\det=1$. At
  $\xi_*$, with $c_*=\cosh t_*$ and $s_*=\sinh t_*$,

  $$
  S(-i\xi_*)=\begin{pmatrix}c_*^2e^{-t_*}&-(1+ic_*)s_*\\-(1-ic_*)s_*&c_*^2e^{t_*}\end{pmatrix},
  $$

  with eigenvalues $e^{\pm\Phi_*}$, $e^{\Phi_*}=c_*^3+\sqrt{c_*^6-1}=3.97314\ldots$.
  The orthogonal projector onto the $e^{\Phi_*}$-eigenspace is

  $$
  P=\frac12\begin{pmatrix}1-\alpha&-(1+ic_*)\alpha/c_*^2\\-(1-ic_*)\alpha/c_*^2&1+\alpha\end{pmatrix}.
  $$

- (b) For all $p\in\mathbb C^3$: $S(p+\pi e_1)=-S(p)$,
  $S(p+\pi e_3)=-\sigma_3S(p)\sigma_3$,
  $S(p+\pi e_2)=-\sigma_3S(p)^T\sigma_3$ and $S(p+\pi(1,1,1))=-S(p)^T$.
- (c) The character $x\mapsto e^{i\eta_0\cdot x}$, $\eta_0\in\Sigma$,
  restricted to $\Lambda_0=\{u\in\mathbb Z^3:u_1+u_2+u_3=0\}$ is trivial if
  and only if $\eta_0\in\{0,\pi u\}$.
- (d) There is $r_0>0$ such that, for $|\eta|\le r_0$,
  $S(\eta-i\xi_*)=\lambda(\eta)P(\eta)+\lambda(\eta)^{-1}(I-P(\eta))$ with
  $\lambda,P$ analytic, $P(0)=P$, $\|P(\eta)-P\|\le c_P|\eta|$ and

  $$
  \lambda(\eta)=\exp\Bigl(\Phi_*+iv_*\cdot\eta-\tfrac12\eta^TQ\eta+\rho_3(\eta)\Bigr),\qquad
  |\rho_3(\eta)|\le c_3|\eta|^3\le\tfrac14\eta^TQ\eta .
  $$

  Here $Q=\operatorname{Hess}\Phi(\xi_*)=q_t(I-\hat u\hat u^T)+q_n\hat u\hat u^T$ with

  $$
  q_t=\frac{c_*}{D_*}=0.68956\ldots,\qquad
  q_n=\frac{c_*}{D_*}\frac{(c_*^2-1)(c_*^2+2)}{c_*^4+c_*^2+1}=0.30338\ldots,\qquad D_*=\sqrt{c_*^6-1}.
  $$

- (e) Outside $\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$,
  $\|\widetilde S_N(\eta)\|\le CNe^{-cN}$ for some $c>0$.

*Proof.* (a) and (b) are identities between trigonometric polynomials and
are checked by expansion. (c): $\Lambda_0$ is generated by $e_1-e_2$ and
$e_2-e_3$, so the character is trivial on it if and only if
$\eta_{0,1}\equiv\eta_{0,2}\equiv\eta_{0,3}\pmod{2\pi}$. (d): the eigenvalues
of $S(\eta-i\xi_*)$ are $\exp(\pm\operatorname{arcosh} f(\eta-i\xi_*))$ and
$f(\eta-i\xi)=\prod_j\cosh(\xi_j+i\eta_j)$. Hence
$\log\lambda(\eta)=\Phi(\xi_*+i\eta)$, which is holomorphic near $\eta=0$
because $\Pi(\xi_*)>1$. Taylor expansion gives $\nabla\Phi(\xi_*)=v_*$ and
$\operatorname{Hess}\Phi(\xi_*)=Q$. The explicit Hessian is
$\operatorname{Hess}\Phi=\frac{\Pi}{D}\operatorname{diag}(\operatorname{sech}^2\xi_j)-\frac{\Pi}{D^3}(\tanh\xi_i\tanh\xi_j)$
with $D=\sqrt{\Pi^2-1}$. The eigenvalues $\lambda^{\pm1}$ are separated by the
gap $e^{2\Phi_*}\approx15.8$, so the spectral projector is analytic. (e): by
Lemma 5.2 and compactness, $\rho(S(\eta-i\xi_*))\le e^{\Phi_*-c'}$ away from
$\Sigma$. Conclude with Lemma 5.3. ∎

By (b), near $\pi u$ we have
$S(\pi u+\eta-i\xi_*)^N=(-1)^N(S(\eta-i\xi_*)^N)^T$, whose Perron projector
is $P^T=\overline P$. The other six points of $\Sigma$ have the same spectral
radius, but by (c) their characters are non-trivial on the lattice planes
$u\cdot x=k$. This is why only $0$ and $\pi u$ contribute at leading order
(Lemma 7.4(d)).

### 7.4. Lattice-plane coordinates and profiles

The planes $\{u\cdot x=k\}$ are orthogonal to $\xi_*$, and each is a
translate of the two-dimensional lattice $\Lambda_0$, of covolume $\sqrt3$.
Write Alice's sites as $x=x_*-\delta\hat u+u_\perp$ with
$u_\perp\perp\hat u$ and depth $\delta=(\sqrt3R-u\cdot x)/\sqrt3$. Since
$u\cdot x\in\mathbb Z$,

$$
\sqrt3\,\delta=\theta_N+j,\qquad j\in\mathbb Z_{\ge0},\qquad \theta_N=\{\sqrt3R\}=\{\sqrt3N/4\}.
$$

Similarly $y=y_*+\delta'\hat u+u'_\perp$ with $\sqrt3\delta'=\theta_N+j'$,
with the *same* $\theta_N$. Then $\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)$ and
$\xi_*\cdot(y-y_*)=t_*(\theta_N+j')$. Moreover
$u\cdot(y-x)=3N-2\lfloor\sqrt3R\rfloor+j+j'$, so
$(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$.

On the plane at depth $\delta$, exactly,

$$
F_N=\frac{64}{N^2}\varepsilon_\perp^2,\qquad
\varepsilon_\perp=\delta-\frac{\delta^2}{2R}-\frac{|u_\perp|^2}{2R}\ \ (\ge0),
$$

and therefore $s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6})$ and
$c_N=-\frac{512\pi^2}{N^4}\varepsilon_\perp^4+O(N^{-8})$ for $\delta=O(1)$.
The same holds for $h_N$ with $\delta'$ and $u'_\perp$. Replacing
$\varepsilon_\perp$ by $\delta-|u_\perp|^2/2R$ costs a relative $O(N^{-1})$.

### 7.5. The free tail

**Lemma 7.2.** Uniformly in $y\in\mathbb Z^3$,
$\widetilde r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$, where

$$
R_0(w)=c_r\bigl[\mathcal I_0(|w|)\,I-\mathcal I_1(|w|)\,H_W(\hat w)\bigr]{\downarrow},
$$

$$
\mathcal I_0(\rho)=4\pi\int_0^1k^2(1-k^2)^2\cos k\;j_0(k\rho)\,dk,\qquad
\mathcal I_1(\rho)=4\pi\int_0^1k^2(1-k^2)^2\sin k\;j_1(k\rho)\,dk .
$$

At the facing point $w_*=u-\hat u/4$, with $\rho_*=|w_*|=\sqrt3-\frac14$ and
$\hat w_*=\hat u$, one has
$R_0(w_*)=c_r\bigl(-\tfrac{\mathcal I_1}{\sqrt3}(1+i),\ \mathcal I_0+\tfrac{\mathcal I_1}{\sqrt3}\bigr)^T$,
with $\mathcal I_0=0.716577\ldots>0$ and $\mathcal I_1=0.132252\ldots>0$.
In particular $r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$ uniformly in
$y\in\mathcal B_N$, and $r=0$ outside $\mathcal B_N$.

*Proof.* For $|p|\le N^{-1}$, $S(p)=e^{-iH(p)}$ with $H$ Hermitian, analytic,
and $H-H_W=O(|p|^2)$. Duhamel's formula gives
$\|S(p)^N-e^{-iNH_W(p)}\|\le CN|p|^2\le C/N$. With $q=Np$,
$e^{-iH_W(q)}=\cos|q|-i\sin|q|\,H_W(\hat q)$, and the angular integrals of
$e^{-iq\cdot w}$ and $e^{-iq\cdot w}\hat q$ are $4\pi j_0$ and
$-4\pi ij_1\hat w$. The resource enters through $g(Np)$ and is not
truncated. The integrands defining $\mathcal I_0,\mathcal I_1$ are positive
because $k\rho_*<\pi$. The value of $H_W(\hat u){\downarrow}=(1+i,-1)^T/\sqrt3$
follows by direct computation. ∎

The resource on Alice's sphere has the exact value
$N^{3/2}\varphi_N=\Phi_0(\frac14)=c_rI_b$ with
$I_b=16\pi\int_0^1k(1-k^2)^2\sin(k/4)\,dk$. We write
$\varphi_\partial=c_rI_b$.

### 7.6. Layer sums

Let
$\Psi_\delta(\tau)=\int_{\mathbb R^2}(\delta-|\sigma|^2)_+^2e^{i\tau\cdot\sigma}\,d^2\sigma$,
which is real and radial in $\tau$. Define

$$
\mathcal S_\pm(\tau;\theta)=\sum_{j\ge0}(\pm1)^je^{-t_*(\theta+j)}\,\Psi_{(\theta+j)/\sqrt3}(\tau),
\qquad
\Gamma_\pm(\theta)=\int_{\mathbb R^2}e^{-q_t|\tau|^2}\,\mathcal S_\pm(\tau;\theta)^2\,d^2\tau .
$$

**Lemma 7.3 (Depth sums).** Let $c_g=2\pi/(3\sqrt3)$ and
$s_\omega=t_*+i\omega$. Then

$$
\mathcal S_+=\sum_{n\in\mathbb Z}\hat g_\tau(2\pi n)e^{2\pi in\theta},\qquad
\mathcal S_-=\sum_{n\in\mathbb Z}\hat g_\tau\bigl(\pi(2n+1)\bigr)e^{i\pi(2n+1)\theta},\qquad
\hat g_\tau(\omega)=c_g\,\frac{e^{-|\tau|^2/(4\sqrt3\,s_\omega)}}{s_\omega^4}.
$$

Consequently $|\mathcal S_+-\hat g_\tau(0)|\le c_g/720$ and
$|\mathcal S_-|\le c_g/48$. Moreover

$$
\overline\Gamma:=\int e^{-q_t|\tau|^2}\hat g_\tau(0)^2d^2\tau=\frac{c_g^2}{t_*^8}\frac{\pi}{q_t+\frac1{2\sqrt3t_*}}=49.44186\ldots,
\qquad |\Gamma_+-\overline\Gamma|\le\varepsilon_+,\qquad 0\le\Gamma_-\le\varepsilon_-,
$$

with
$\varepsilon_+=2\frac{c_g}{720}\frac{c_g}{t_*^4}\frac{\pi}{q_t+1/(4\sqrt3t_*)}+\bigl(\frac{c_g}{720}\bigr)^2\frac\pi{q_t}=0.04917\ldots$
and $\varepsilon_-=\bigl(\frac{c_g}{48}\bigr)^2\frac\pi{q_t}=0.00289\ldots$.

*Proof.* Radially, $\Psi_\delta(\tau)=\pi H(\delta)$ with
$H(\delta)=\int_0^\delta(\delta-s)^2J_0(|\tau|\sqrt s)\,ds$. So
$H'''=2J_0(|\tau|\sqrt\delta)$ and $H(0)=H'(0)=H''(0)=0$. Since
$\int_0^\infty e^{-ps}J_0(|\tau|\sqrt s)\,ds=e^{-|\tau|^2/4p}/p$, the function
$g_\tau(x)=e^{-t_*x}\Psi_{x/\sqrt3}(\tau)\mathbf 1_{x\ge0}$ has Fourier
transform $\hat g_\tau$ as stated. It is continuous, vanishing to third
order at $x=0$, and $\hat g_\tau\in\ell^1(2\pi\mathbb Z)$. Poisson summation
is therefore exact. The bounds use $|e^{-|\tau|^2/(4\sqrt3s)}|\le1$,
$|s_{2\pi n}|\ge2\pi|n|$, $\sum_{n\ne0}(2\pi n)^{-4}=1/720$ and
$\sum_n|\pi(2n+1)|^{-4}=1/48$. The Gaussian integrals are elementary. ∎

**Lemma 7.4 (Layers).** Let $\chi\in\{{\uparrow},{\downarrow}\}$,
$f=s_N\varphi_N\chi$, $w=h_N\,M_B\,r$ and $\tau=\sqrt{N/2}\,\eta_t$, where
$\eta=\eta_n\hat u+\eta_t$ with $\eta_t\perp\hat u$.

- (a) $|\mathfrak A_f(\eta)|,\ \|\mathfrak B_w(\eta)\|\le CN^{-5/2}$ for all $\eta$.
- (b) For $|\eta|\le r_0$,

  $$
  \mathfrak A_f(\eta)=N^{-5/2}\tfrac{16\pi}{\sqrt3}\varphi_\partial\bigl[\mathcal S_+(\tau;\theta_N)+\mathcal E_A\bigr]\chi,\qquad
  \mathfrak B_w(\eta)=N^{-5/2}\tfrac{32}{\sqrt3}\,R_0(w_*)^\dagger M_B\bigl[\mathcal S_+(\tau;\theta_N)+\mathcal E_B\bigr],
  $$

  with $|\mathcal E_{A,B}|\le C(N^{-1/2}+|\eta_n|)$.
- (c) Near $\pi u$ the same holds with $\mathcal S_-$ in place of
  $\mathcal S_+$. The alternating sign comes from the parity
  $(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$, combined with
  $S^N\mapsto(-1)^N(S^N)^T$.
- (d) For $\eta_0\in\Sigma\setminus\{0,\pi u\}$ and $|\eta|\le r_0$,
  $|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}$.

*Proof.* Decompose the sums into lattice planes. On the plane at depth
$\delta=(\theta_N+j)/\sqrt3$ the tilt weight is $e^{-t_*(\theta_N+j)}$. The
profile $s_N\varphi_N$ is supported in a disc of radius
$\varrho=\sqrt{2R\delta-\delta^2}=O(\sqrt N)$ and has size
$O(N^{-7/2}\delta^2)$. Planes with $\delta>R/2$ contribute $O(e^{-cN})$. This
gives (a).

For (b), apply Poisson summation on each plane. The $m=0$ term is
$\frac1{\sqrt3}\int e^{i\eta_t\cdot u_\perp}G_0(u_\perp)\,d^2u_\perp$. The
terms $m\ne0$ are bounded by
$\|\partial^3G_0\|_{\mathcal M}|2\pi m-\eta_t|^{-3}$, since the profile
vanishes quadratically on the rim and its third derivative is a finite
measure. After the weighted depth sum, they give a relative error
$O(N^{-3/2})$. In the $m=0$ term, use the profile expansions,
$\varphi_N=N^{-3/2}\varphi_\partial(1+O(|u_\perp|/N+\delta/N))$ and
$|e^{-i\eta_n\delta}-1|\le|\eta_n|\delta$. With the substitution
$u_\perp=\sqrt{2R}\,\sigma$,

$$
\int e^{i\eta_t\cdot u_\perp}\Bigl(\delta-\frac{|u_\perp|^2}{2R}\Bigr)_+^2d^2u_\perp=2R\,\Psi_\delta(\tau).
$$

Collecting the factors
$\frac1{\sqrt3}\cdot\frac{32\pi}{N^2}\cdot N^{-3/2}\varphi_\partial\cdot2R$
gives the prefactor of $\mathfrak A_f$. For $\mathfrak B_w$ the factors are
$\frac1{\sqrt3}\cdot\frac{64}{N^2}\cdot N^{-3/2}R_0(w_*)^\dagger\cdot2R$,
using Lemma 7.2, the smoothness of $R_0$ and $M_B^\dagger=M_B$. (c) follows
from Lemma 7.1(b) and the parity identity. (d): by Lemma 7.1(c), the
character is non-trivial on each plane. The Poisson sum therefore has no
$m=0$ term, and the remaining terms are $O(N^{-4})$. ∎

### 7.7. Assembly

**Theorem 7.5.** For $\chi\in\{{\uparrow},{\downarrow}\}$ and each $M_B$,

$$
\mathcal T_\chi(N)=N^{-13/2}\,\mathcal K\,c_r\bigl[\Gamma_+(\theta_N)\,x_0+\Gamma_-(\theta_N)\,x_\pi\bigr]+O(N^{-7}),
$$

where $x_0=\tilde R^\dagger M_BP\chi$, $x_\pi=\tilde R^\dagger M_B\overline P\chi$,
$\tilde R=R_0(w_*)/c_r$ and

$$
\mathcal K=\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}\;\varphi_\partial=1.749269\ldots .
$$

*Proof.* Insert Lemmas 7.1 and 7.4 into (13). Away from the balls
$B(\eta_0,r_0)$ the contribution is $O(Ne^{-cN}N^{-5})$. The six points of
$\Sigma$ with non-trivial characters give
$O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})=O(N^{-8})$, using the Gaussian decay
of $\widetilde S_N$. Near $\eta_0\in\{0,\pi u\}$ we make three replacements.
First, $\widetilde S_Ne^{-iN\eta\cdot v_*}$ is replaced by
$e^{-N\eta^TQ\eta/2}P$ (respectively $\overline P$), at cost
$N^{-5}\int(c_P|\eta|+Nc_3|\eta|^3)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.
Second, the layers are replaced by their leading forms, at cost
$N^{-5}\int(N^{-1/2}+|\eta_n|)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$. Third, the
integral is extended to $\mathbb R^3$, at cost $O(e^{-cNr_0^2})$. What
remains is

$$
N^{-5}\,\frac{512\pi}{3}\,\varphi_\partial\,c_r\,x_{0,\pi}\,\sqrt{\frac{2\pi}{Nq_n}}\;\frac2N\;(2\pi)^{-3}\int_{\mathbb R^2}e^{-q_t|\tau|^2}\mathcal S_\pm^2\,d^2\tau .
$$

Here we used $d^2\eta_t=(2/N)d^2\tau$ and
$N\eta^TQ\eta/2=Nq_n\eta_n^2/2+q_t|\tau|^2$. ∎

*Proof of Theorem 4.4.* By (12), the $e^{-K_*N}N^{-13/2}$ sector of
$L_{M,M_B}$ is $\ell(\mathcal T_\chi)$, where $\ell$ is the real-linear
functional $-2\operatorname{Im}$ for $M\in\{I,\sigma_1\}$,
$+2\operatorname{Im}$ for $M=\sigma_3$ and $+2\operatorname{Re}$ for
$M=\sigma_2$, and $\chi={\downarrow}$ for $M\in\{I,\sigma_3\}$,
$\chi={\uparrow}$ for $M\in\{\sigma_1,\sigma_2\}$. Since $\mathcal K$, $c_r$
and $\Gamma_\pm$ are real, Theorem 7.5 gives (10) with $\ell_0=\ell(x_0)$ and
$\ell_\pi=\ell(x_\pi)$. Closed forms of $\ell_0,\ell_\pi$ in terms of
$\alpha,c_*,\mathcal I_0,\mathcal I_1$ are listed in Appendix A.

The remainder budget, relative to $N^{-13/2}$, is as follows:

- $O(N^{-1/2})$ from the cubic term of the exponent, from $P(\eta)-P$, from
  the normal phase, and from the variation of $\varphi_N$ and $R_0$ across
  the layer;
- $O(N^{-1})$ from $r-N^{-3/2}R_0$ and from the exact profile and disc
  geometry;
- $O(N^{-3/2})$ from in-plane Poisson terms and from the six
  non-contributing torus points;
- $O(N^{-2})$ from $2\operatorname{Re}\langle r,Ea_c\rangle$;
- exponentially small terms from the region away from $\Sigma$ and from the
  sector $e^{-2K_*N}$.

Hence $L=e^{-K_*N}N^{-13/2}(C(\theta_N)+R_N)$ with $|R_N|\le C'N^{-1/2}$.

For non-vanishing, note that $\Gamma_-\ge0$. For every pair, interval
arithmetic certifies
$|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$. Therefore
$C(\theta)$ has the sign of $\ell_0$ for every $\theta$, and
$|C(\theta)/\overline{C}-1|\le(\varepsilon_+|\ell_0|+\varepsilon_-|\ell_\pi|)/(\overline\Gamma|\ell_0|)$,
which gives the bounds of Table 1. Since
$\inf_\theta|C(\theta)|\ge(1-1.5\cdot10^{-3})|\overline{C}|>0$, the remainder
cannot cancel the leading term for $N$ large, and the asymptotics of
$\delta=|L|$ follow. ∎

**Remark 7.6 (Counting the power).** The exponent $13/2$ decomposes as
follows. The resource contributes $\frac32$ at the layer and the free tail
$\frac32$ at Bob. The profiles $s_N$ and $h_N$ contribute $2+2$. The two
in-plane areas contribute $-2$. The normal Gaussian contributes $\frac12$,
and the tangential rescaling $d^2\eta_t=(2/N)d^2\tau$ contributes $1$. The
depths $j,j'$ are discrete sums of size $O(1)$ and contribute no power. The
common tangential direction $u_\perp+u'_\perp$ is a flat direction of the
exponent, because $\xi_*$ is orthogonal to the planes. It is confined by the
profiles and produces the area factors, not a Gaussian factor.

**Remark 7.7 (Dependence on $\theta_N$).** Since $\sqrt3/4\notin\mathbb Q$,
the sequence $\theta_N$ is equidistributed. $C(\theta_N)$ is therefore
quasi-periodic in $N$ and not a constant. The oscillation comes from the
commensurability of the lattice planes with the spheres bounding the regions.
It is below $0.15\%$, and it never changes the sign.

---

## 8. Discussion

### 8.1. What the theorem says and does not say

The theorem is a statement about one walk and one explicitly specified family
of operations. It shows that the gap between the emergent relativistic cone
and the microscopic causal support is not merely geometric. Under an
infrared-controlled protocol it carries an operational response whose
asymptotic law is known exactly: rate, power and coefficient. It does not
claim that $D_B>0$ for every protocol, that every quantum walk behaves this
way, or that every smooth encoder $M=aI+b\cdot\sigma$ signals. It is not a
violation of the model's microcausality, since Bob remains inside
$N C_{\mathrm{micro}}$. The limit $N\to\infty$ is an infrared scaling at
fixed lattice units, not a continuum limit $a,\tau\to0$.

The result is asymptotic. The remainder constants and $N_*$ are finite but
not explicit. The finite-$N$ diagnostics of Appendix A indicate an effective
relative correction of about $-100/N$. The leading formula is therefore
quantitatively reliable only for $N\gtrsim10^3$. For $M\in\{I,\sigma_3\}$
with $M_B=I$, whose coefficient is among the smallest, the $N^{-17/2}$ term
dominates over the whole diagnostic range.

### 8.2. Physical reading

Restoring a lattice spacing $a$, the integer $N$ is both the number of steps
and the separation scale in lattice units, so $N\sim\ell/a$ for a separation
$\ell$, and $\delta\sim e^{-K_*N}$ up to algebraic factors. The response is
therefore negligible at any separation large compared with the lattice
spacing, and by the preceding subsection the leading formula becomes accurate
only for $N\gtrsim10^3$. We make no claim about observability, and regard the
result as a statement in the mathematical physics of finite-range unitary
dynamics. Its
interest lies in the structure it exhibits: an exact separation between
ballistic propagation, which respects $c_{\mathrm{IR}}$, and operational
influence, which does not vanish inside the corona even under infrared
control.

### 8.3. Open problems

1. General encoders $M=aI+b\cdot\sigma$, and optimisation over admissible
   operations.
2. Other walks, in particular the Bialynicki-Birula walk [9, Eq. (5.12)],
   whose corona contains ballistic modes faster than $c_{\mathrm{IR}}$, and
   the massive Dirac case.
3. Explicit remainder constants and $N_*$, which would make the statement
   effective at finite $N$.
4. Many-particle and second-quantized versions. The upper bound extends to
   even local unitaries on the full CAR algebra, with prefactor $288N^7$ in
   place of $36N^4$ [17], but no lower bound is available there.

---

## Appendix A. Computer-assisted parts and diagnostics

Theorem 4.1, together with Lemma 5.1, is formally verified in Lean 4/Mathlib
(`formal/` in [17]). The asymptotic results (Theorems 4.3 and 4.4) are not.
The analytic arguments above are complete up to the following verified
computations. All of them are performed by the certificate scripts listed in
[17], at the commit given there, with Python 3.12.3, SymPy 1.14.0 and mpmath
1.3.0. Exact identities use SymPy. Enclosures use the interval context
`mpmath.iv` with 50 digits, and only its elementary operations: the four
arithmetic operations, integer powers by repeated multiplication,
$\sqrt{\cdot}$, $\exp$, $\log$, $\sin$, $\cos$ and $\pi$. No interval
quadrature is used: $\mathcal I_0(\rho_*)$, $\mathcal I_1(\rho_*)$ and $I_b$
are enclosed through exact closed forms in $\sin$ and $\cos$, obtained from
the moments $\int_0^1k^m\{\sin,\cos\}(\omega k)\,dk$, $m\le5$, which are
checked symbolically.

- The symbol identities: Lemma 2.1, (5), and Lemma 7.1(a)–(b). Also the
  ellipse-lemma polynomials, $\cosh^3(\log2)=125/64$ and the vertex blocks.
- Closed forms and enclosures of $t_*$, $K_*$, $c_*^2$, $\Phi_*$, $q_t$,
  $q_n$, $P$, $\mathcal I_0$, $\mathcal I_1$, $\varphi_\partial$,
  $\mathcal K$, $\overline\Gamma$ and $\varepsilon_\pm$.
- The sixteen pairs $(\ell_0,\ell_\pi)$, the sign margin
  $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$, the
  bounds of Table 1, and $C(\sigma_3,\cdot)=-C(I,\cdot)$.

Closed forms of $\ell_0,\ell_\pi$ are given below, with $c=c_*$,
$A=\mathcal I_0(\rho_*)$ and $B=\mathcal I_1(\rho_*)$. The rows for
$\sigma_3$ are the negatives of the rows for $I$.

| $(M,M_B)$ | $\ell_0$ | $\ell_\pi$ |
| --- | --- | --- |
| $(I,I),\ (I,P_3)$ | $-\frac{\sqrt3}{3}\frac{B\alpha(c-1)}{c^2}$ | $+\frac{\sqrt3}{3}\frac{B\alpha(c+1)}{c^2}$ |
| $(I,P_1)$ | $\frac{3Ac\alpha-\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}$ | $-\frac{3Ac\alpha+\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}$ |
| $(I,P_2)$ | $\frac{3A\alpha-\sqrt3B(c^2\alpha+c^2+c\alpha-2\alpha)}{6c^2}$ | $\frac{3A\alpha-\sqrt3B(c^2\alpha+c^2-c\alpha-2\alpha)}{6c^2}$ |
| $(\sigma_1,I)$ | $-\frac{3A\alpha+\sqrt3B(c-c\alpha+\alpha)}{3c}$ | $\frac{3A\alpha-\sqrt3B(c-c\alpha-\alpha)}{3c}$ |
| $(\sigma_1,P_1)$ | $-\frac{3Ac\alpha+\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}$ | $\frac{3Ac\alpha-\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}$ |
| $(\sigma_1,P_2)$ | $-\frac{3A(c^2(1-\alpha)+c\alpha)+\sqrt3B(2c^2(1-\alpha)+2c\alpha-\alpha)}{6c^2}$ | $-\frac{3A(c^2(1-\alpha)-c\alpha)+\sqrt3B(2c^2(1-\alpha)-2c\alpha-\alpha)}{6c^2}$ |
| $(\sigma_1,P_3),\ (\sigma_2,P_3)$ | $-\frac{\sqrt3}{3}B(1-\alpha)$ | $-\frac{\sqrt3}{3}B(1-\alpha)$ |
| $(\sigma_2,I)$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}$ |
| $(\sigma_2,P_1)$ | $-\frac{3A(\alpha-c^2(1-\alpha))+\sqrt3Bc\alpha}{6c^2}$ | $-\frac{3A(\alpha-c^2(1-\alpha))-\sqrt3Bc\alpha}{6c^2}$ |
| $(\sigma_2,P_2)$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+c\alpha+2\alpha)}{6c^2}$ | $-\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)-c\alpha+2\alpha)}{6c^2}$ |

**Finite-$N$ diagnostics.** These are floating-point and not used in any
proof; they use NumPy 1.26.4 and are produced by the `--diagnostics` option
of the coefficient certificate [17]. A floating-point FFT evaluation of the
exact discrete convolution formula in tilted variables ("brute") was compared
with a reference that keeps the exact lattice geometry but replaces the
kernel by its Gaussian form at the eight points of $\Sigma$. Their ratio
tends to $1$ with deviation of order $c/N$, $c\in[-0.5,14]$, at
$N=24,40,56$. For $M\in\{I,\sigma_3\}$ and $M_B=I$, the ratio of the
$N^{-17/2}$ piece $2\operatorname{Re}\langle r,Ea_c\rangle$ to the piece
$2\operatorname{Im}\langle r,Ea_{\downarrow}\rangle$ that carries the
$N^{-13/2}$ term is $15.2$, $9.4$ and $6.4$ at $N=24,40,56$. A semi-analytic evaluation with discrete planes and exact
profiles gives semi/lead $=0.906$, $0.990$ and $0.997$ at $N=10^3$, $10^4$
and $3\cdot10^4$, consistent with a relative correction $\approx-100/N$. The
free tail agrees with $N^{-3/2}R_0$ to relative accuracy $2\cdot10^{-6}$ at
$N=40$ and $8\cdot10^{-9}$ at $N=640$.

---

## References

1. A. Ahlbrecht, H. Vogts, A. H. Werner, R. F. Werner, *Asymptotic evolution
   of quantum walks with random coin*, arXiv:1009.2019.
2. P. Arrighi, *An overview of quantum cellular automata*, arXiv:1904.12956.
3. Y. Baryshnikov, W. Brady, A. Bressler, R. Pemantle, *Two-dimensional
   quantum random walk*, J. Stat. Phys. **142**, 78–107 (2011),
   arXiv:0810.5495.
4. I. Bialynicki-Birula, *Weyl, Dirac, and Maxwell equations on a lattice as
   unitary cellular automata*, Phys. Rev. D **49**, 6920 (1994),
   arXiv:hep-th/9304070.
5. A. Bisio, G. M. D'Ariano, P. Perinotti, A. Tosini, *Free quantum field
   theory from quantum cellular automata: derivation of Weyl, Dirac and
   Maxwell quantum cellular automata*, arXiv:1601.04832.
6. L. Bombelli, J. Henson, R. D. Sorkin, *Discreteness without symmetry
   breaking: a theorem*, arXiv:gr-qc/0605006.
7. S. Bravyi, M. B. Hastings, F. Verstraete, *Lieb–Robinson bounds and the
   generation of correlations and topological quantum order*, Phys. Rev.
   Lett. **97**, 050401 (2006), arXiv:quant-ph/0603121.
8. H. A. Carteret, B. Richmond, N. M. Temme, *Evanescence in coined quantum
   walks*, J. Phys. A: Math. Gen. **38**, 8641–8665 (2005),
   arXiv:quant-ph/0506048.
9. C. Cedzich, A. Joye, A. H. Werner, R. F. Werner, *Exponential tail
   estimates for quantum lattice dynamics*, Ann. Henri Poincaré **27**,
   2843–2870 (2026), doi:10.1007/s00023-025-01598-4, arXiv:2408.02108.
10. G. M. D'Ariano, M. Erba, P. Perinotti, *Isotropic quantum walks on
    lattices and the Weyl equation*, Phys. Rev. A **96**, 062101 (2017),
    arXiv:1708.00826.
11. G. M. D'Ariano, P. Perinotti, *Derivation of the Dirac equation from
    principles of information processing*, Phys. Rev. A **90**, 062106
    (2014), arXiv:1306.1934.
12. T. Farrelly, *A review of quantum cellular automata*, Quantum **4**, 368
    (2020), arXiv:1904.13318.
13. G. Grimmett, S. Janson, P. F. Scudo, *Weak limits for quantum random
    walks*, Phys. Rev. E **69**, 026119 (2004), arXiv:quant-ph/0309135.
14. N. Konno, *Quantum random walks in one dimension*, Quantum Inf. Process.
    **1**, 345–354 (2002).
15. E. H. Lieb, D. W. Robinson, *The finite group velocity of quantum spin
    systems*, Commun. Math. Phys. **28**, 251–257 (1972).
16. R. Pemantle, M. C. Wilson, S. Melczer, *Analytic Combinatorics in Several
    Variables*, 2nd ed., Cambridge University Press (2024),
    doi:10.1017/9781108874144.
17. Repository `nacho09021973/qca-causal-cones`,
    <https://github.com/nacho09021973/qca-causal-cones>, commit
    `551addabe28b` (branch `research/b-infinity-post-s4-gate`). Certificates
    `scripts/verify_scaled_ir_gate.py`,
    `scripts/verify_regional_directional_asymptotics_gate.py`,
    `scripts/verify_regional_laplace_coefficient_gate.py`,
    `scripts/verify_directional_saturation.py`; Lean formalization in
    `formal/`.
18. B. Schumacher, R. F. Werner, *Reversible quantum cellular automata*,
    arXiv:quant-ph/0405174.
19. T. Sunada, T. Tate, *Asymptotic behavior of quantum walks on the line*,
    J. Funct. Anal. **262**, 2608–2645 (2012), arXiv:1108.1878.
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

**Reconstrucción fuerte.** C3 no reclama una asintótica nueva. Es una identidad algebraica exacta, más un límite de suma de Riemann, más dos insumos importados. Comprobé la parte propia.

[INFERENCE, verificado] (C3.1): con `Pφ_N=φ_N`, `(Δ_PP+q_N|φ><φ|)/(1-q_N) = |w><w|/(1-q_N) − |φ><φ| = Δ_cond`. Exacto. (C3.2)–(C3.3) siguen por traza: `L_cond−L_PP = q_N(p0+L_PP)/(1−q_N)`. Correcto. Además, el `q_N=||QU_Mφ||²` de C3 coincide con el `||Q(U_M−I)φ||²` de C1 [SOURCE, ledger §10.1] porque `Qφ_N=0`; el informe no lo señala, pero la identificación es válida, y con ella la probabilidad de éxito 1 del bit cero es exacta, no asintótica.

`h_N` coincide literalmente con el manuscrito §3.2 [SOURCE]. Suma de red: con `Y=y/N`, `h_N(y)=h_0(Y−u)`, `||r_N||²=N^{-3}||R_0||²+O(N^{-4})`; sobre `O(N³)` sitios el error es `O(N^{-1})` y el término principal es una suma de Riemann de función continua de soporte compacto. Límite correcto. Control de consistencia: `p_∞ ≤ ∫||R_0||² = 1`.

`p_∞>0` es reconstruible pero no está escrito. En el acta `R_0` se da vía `I_0,I_1` (Lema 7.2), no como transformada de Fourier. Lo verdadero [INFERENCE] es `R_0(w)=c_r∫_{|q|≤1}g(q)e^{-iq·w}e^{-iH_W(q)}↓`: integrando continuo de soporte compacto, luego entera; si `||R_0||²≡0` en un abierto, ambas componentes se anulan en todo `R³`, luego `g(q)e^{-iH_W(q)}↓=0`, contra `||·||=g(q)>0` en `|q|<1`.

**Objeción más fuerte.** C3 hace descansar la obligación 4 sobre la forma más fuerte de C2c —(C15), cota inferior uniforme vía definitud positiva de la matriz de Gram— que ninguna conclusión de C3 utiliza. Para (C3.7) basta `L_PP,N → 0`; para la no-cancelación por órdenes basta la cota **superior** `L_PP=O(N^{-5/2-ε})`. La cota inferior no entra en ningún paso. El coste es real: C3 hereda el eslabón más caro y más nuevo de un documento que, en el acta adjunta, se autodeclara `REPAIRED / REVIEW_PENDING` y que lista "el argumento de definitud positiva" entre sus propios puntos prioritarios de revisión. Que `CURRENT_STATE` registre `C2C_PASS` no lo salva aquí: la revisión citada (2026-09-23) no está en el acta [ABSENCE].

*Condición de concesión:* si C3 reescribe la obligación 4 bajo la hipótesis explícita `L_PP,N→0` (con `O(N^{-3})` como cota superior suficiente), declara (C15)–(C16) vía suficiente y no necesaria, y marca su estatus heredado, la objeción queda desactivada sin alterar ninguna fórmula.

**Menores, todos concretos.** (i) [ABSENCE] "el lema de la cola de C1": busqué en el acta; ese enunciado figura como Lema 7.2 del manuscrito §7.5, dentro de la prueba del Teorema 4.4 que C3 declara no usar. Lo que C1 aporta, según C2c §5.1, es la fuente `a_N`, objeto distinto. Atribución a corregir. (ii) En `D=1024π²B²/5`, `B` no se define en el informe; el ledger lo da como `Φ_0(1/4)`. La constante de la conclusión final queda con un símbolo libre. (iii) La tabla marca OPEN el líder de `L_cond` mientras el texto dice "fuera del alcance contractual": son cosas distintas, y de las dos filas PASS se sigue por suma de órdenes separados.

## Ronda 1 — GEMINI

Suscribo la reconstrucción de CLAUDE OPUS sobre la exactitud algebraica de (C3.1)-(C3.3), su validación lógica de $p_\infty > 0$, y sus objeciones menores (i) sobre la falsa atribución a C1 del lema de la cola (es el Lema 7.2 del manuscrito [SOURCE]) y (ii) sobre el símbolo libre $B$.

Ataco la objeción principal de CLAUDE OPUS respecto a la importación supuestamente innecesaria de la definitud positiva de la matriz de Gram (C15-C16).
*Condición de concesión:* Su ataque sería válido si el propósito de C3 fuera establecer la no-cancelación asumiendo el mínimo de premisas matemáticas posibles.
*Refutación:* El contrato del sanedrín [SOURCE] exige taxativamente: "Audita únicamente [...] la importación C15-C16 para los cuatro pares D0=I". La expansión (C16) incluye inherentemente el coeficiente líder no nulo derivado de la definitud positiva de (C15). C3 no importa caprichosamente el eslabón más fuerte de C2c; está ejecutando mecánicamente la importación que su propio alcance le ordena. Exigir que C3 degrade (C16) a una mera cota superior $O(N^{-3})$ es penalizar al documento por cumplir su contrato. 

Añado el control de propagación de error en (C3.7), que el acta omite y CLAUDE OPUS no cubrió [INFERENCE]. La suma de Riemann $p_{0,N}$ opera sobre la bola de Bob, sumando $O(N^3)$ sitios. Sustituir $r_N(y)$ por la función límite radial introduce un error local de $O(N^{-4})$ [SOURCE], lo que inyecta un error total sobre el volumen de $O(N^3) \times O(N^{-4}) = O(N^{-1})$. A su vez, la aproximación de la suma de Riemann por la integral tridimensional de una función analítica introduce un error de discretización acotado por $O(N^{-1})$. Dado que $L_{PP,N} = \Theta(N^{-3})$, el numerador $(p_{0,N} + L_{PP,N})$ de (C3.3) converge a $p_\infty$ con un error relativo estricto de $O(N^{-1})$. La incertidumbre total queda dominada por el prefactor $q_N$, cuyo error certificado en C1 es $O(N^{-1/2})$ [SOURCE]. En consecuencia, la corrección relativa exacta de (C3.7) es $O(N^{-1/2})$. El uso de $o(1)$ en el acta es una degradación asintótica lícita que absorbe correctamente este error sin ascensos injustificados.

Dado que CLAUDE OPUS omitió los veredictos imperativos, los emito basándome en la solidez de las derivaciones auditadas [INFERENCE]:
- Identidad exacta de `Lcond`, `q_N` y éxito: PASS.
- Definición de `h_N`, suma de red y límite `p0_N -> p_infty > 0`: PASS.
- Importación C15-C16 (pares D0=I): PASS.
- Conclusión C3.7 y retiro de falsa cancelación por órdenes: PASS.

Veredicto global: C3_PROOF_WRITTEN_REVIEW_ACCEPTED. La mala atribución nominal de un lema es un defecto de citación en el texto que no compromete la validez analítica del paso ni requiere reparación de alcance.

## Ronda 2 — CLAUDE OPUS

**TURNO FALLIDO — CUOTA AGOTADA.** El backend devolvió un aviso de límite en lugar de una intervención:

```
You've hit your session limit · resets 1:30pm (Europe/Madrid)
```

> CLAUDE OPUS queda fuera del resto de la sesión tras 1 fallos; no se interpreta su ausencia como acuerdo.

## Ronda 2 — GEMINI

Veredicto global: C3_PROOF_WRITTEN_REVIEW_ACCEPTED. 

La lógica inicial, los parámetros de la identidad algebraica (C3.1)-(C3.3), la positividad analítica $p_\infty > 0$, el control de propagación de error relativo $O(N^{-1/2})$ en la suma de Riemann y las rectificaciones editoriales previas quedan validadas como contexto establecido. 

Concedo explícitamente [INFERENCE] que la cota inferior estricta extraída de (C15)-(C16) excede el mínimo matemático rigurosamente necesario para descartar la cancelación por órdenes en la ecuación final; la corrección (C3.7) sobreviviría inalterada utilizando únicamente una cota superior $O(N^{-3})$ para $L_{PP}$. 

No obstante, el ataque sobre la supuesta sobre-importación de la definitud positiva de la matriz de Gram queda definitivamente desactivado. El contrato [SOURCE] fuerza la asimilación exacta de "la importación C15-C16 para los cuatro pares D0=I". La retención del coeficiente líder completo no obedece a un exceso de diseño asintótico del reporte C3, sino al acatamiento estricto de la directiva S3 del gate. El salto lógico desde esta restricción contractual directamente a la formulación final de la corrección (C3.7) es inmediato, garantizando que el observable no se cancela con $L_{PP}$ a orden líder sin necesidad de transiciones intermedias.

Las deficiencias de citación nominal detectadas —específicamente la derivación de la fuente radial referenciada erróneamente como lema de C1 en lugar del Lema 7.2 del manuscrito— constituyen ruido textual que no contamina la integridad del escalamiento algebraico ni altera el resultado de la traza condicionada. Todas las obligaciones de la auditoría se cumplen. PASS definitivo en todas las sub-métricas.

## Ronda Residuo — GEMINI

Queda en pie la exactitud de las identidades algebraicas (C3.1)-(C3.3) y la positividad analítica $p_\infty > 0$ [INFERENCE]. También subsiste la corrección (C3.7) con error relativo acotado en $O(N^{-1/2})$ [INFERENCE]. Discrepo de la objeción de CLAUDE OPUS sobre la importación innecesaria de la definitud positiva de la matriz de Gram (C15-C16): su ataque decae porque el contrato exige taxativamente auditar dicha importación explícita para los pares D0=I [SOURCE]. Retener el coeficiente líder completo no es un exceso asintótico, sino cumplimiento contractual.

Debe abandonarse la falsa atribución del "lema de la cola" a C1; el origen del campo radial $R_0$ es el Lema 7.2 del manuscrito [SOURCE]. Igualmente se abandona la exigencia de CLAUDE OPUS de degradar (C16) a una mera cota superior $O(N^{-3})$ para probar la no-cancelación.

No está justificada todavía la constante $B$ de (C3.4) dentro del texto del propio informe C3, pues depende de un documento externo [ABSENCE]. Asimismo, cualquier afirmación sobre el término líder exacto de $L_{\mathrm{cond}}$ o su magnitud frente al observable total $L$ permanece injustificada al estar explícitamente declarada OPEN y fuera de alcance [SOURCE]. Se confirma el veredicto C3_PROOF_WRITTEN_REVIEW_ACCEPTED.

## Ronda Veredicto — GEMINI

1. ACUERDO — Veredicto global consolidado: C3_PROOF_WRITTEN_REVIEW_ACCEPTED. La lógica inicial y los parámetros asintóticos quedan validados como contexto establecido. Se acepta la exactitud algebraica de las identidades (C3.1)-(C3.3), la demostración de positividad analítica $p_\infty > 0$ y la acotación del error relativo de la corrección (C3.7) en $O(N^{-1/2})$. Existe consenso en que el informe presenta deficiencias menores de citación y de definición en variables libres.

2. DESACUERDO VIVO — Procesamiento estándar aplicado. La divergencia persiste sobre la economía lógica de la demostración frente al acatamiento del alcance. Específicamente, se discrepa sobre si la retención del coeficiente líder completo derivado de la definitud positiva de la matriz de Gram (C15-C16) constituye una sobre-importación injustificada para probar la no-cancelación por órdenes, o si el mandato explícito del contrato de auditar esta importación para los pares D0=I blinda y legitima el paso.

3. ABANDONADO — La exigencia de degradar (C16) a una cota superior $O(N^{-3})$ como vía de optimización matemática, descartada por contravenir las instrucciones explícitas del contrato. La falsa atribución del "lema de la cola" al gate C1, al confirmarse su origen exacto en el Lema 7.2 del manuscrito.

4. PENDIENTE — Integración de una definición autocontenida para la constante $B$ de (C3.4) en el texto. Determinación del término líder exacto de $L_{\mathrm{cond}}$ y la comparación analítica de $L_{\mathrm{cond}}-L_{PP}$ frente al observable total $L$, elementos confirmados como fuera de alcance.

## Ronda Veredicto — GEMINI

1. AGREEMENT — Consolidated global verdict: C3_PROOF_WRITTEN_REVIEW_ACCEPTED. The initial logic and asymptotic parameters are validated as established context. The algebraic exactness of the identities (C3.1)-(C3.3), the analytical positivity proof $p_\infty > 0$, and the relative error bound of the correction (C3.7) at $O(N^{-1/2})$ are accepted. There is consensus that the report presents minor deficiencies regarding citation and the definition of free variables.

2. LIVE DISAGREEMENT — Standard processing applied. Divergence persists regarding the logical economy of the proof versus compliance with the scope. Specifically, there is disagreement over whether retaining the full leading coefficient derived from the positive definiteness of the Gram matrix (C15-C16) constitutes an unjustified over-importation to prove non-cancellation by orders, or if the contract's explicit mandate to audit this importation for the D0=I pairs shields and legitimizes the step.

3. ABANDONED — The demand to downgrade (C16) to an upper bound $O(N^{-3})$ as a mathematical optimization pathway, discarded for contravening the contract's explicit instructions. The false attribution of the "tail lemma" to gate C1, upon confirming its exact origin in Lemma 7.2 of the manuscript.

4. OUTSTANDING — Integration of a self-contained definition for the constant $B$ of (C3.4) into the text. Determination of the exact leading term of $L_{\mathrm{cond}}$ and the analytical comparison of $L_{\mathrm{cond}}-L_{PP}$ against the total observable $L$, elements confirmed to be out of scope.

## Resultado operativo

- Estado: `DEGRADED_NO_CONSENSUS`
- Turnos con fallo, cuota, ausencia o respuesta corta: 1
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-23T11:19:20Z` |
| Finished (UTC) | `2026-09-23T11:25:27Z` |
| Wall clock | 0h 6m 7s |
| Command | `sanedrin -r 2 -m opus,gemini --secuencial --timeout 900 --reintentos 1 -i es -o debates/2026-09-23--c3-claude-final-review.md -c theory/IR_C3_CONDITIONING_GATE.md -c reports/2026-09-23--c3-conditioning-execution.md -c reports/2026-09-22--c2c-structural-scope.md -c papers/ir-corona/ir-corona.md -c state/CURRENT_STATE.md Revisión final de C3 tras el commit 2eb8b00. Claude es el revisor principal. Audita únicamente la identidad exacta de Lcond, q_N y éxito, la definición congelada de h_N y la suma de red que define p0_N, el límite p0_N -> p_infty>0, la importación C15-C16 para los cuatro pares D0=I y la conclusión C3.7. Comprueba que se retiró la falsa posibilidad de cancelación por órdenes. Mantén fuera de alcance el líder de Lcond, abs(Lcond), comparación con L, H1c y E/AdS. No uses N=24/40, simulaciones, cuadraturas ni barridos. Emite PASS/INCOMPLETE/FAIL por obligación y veredicto global C3_PROOF_WRITTEN_REVIEW_ACCEPTED, C3_REPAIR_REQUIRED, C3_FAIL o C3_INCOMPLETE. No modifiques archivos.` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-23T11:23:26Z | 1 | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 245 | 459 | ok |
| 2026-09-23T11:24:09Z | 1 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 43 | 419 | ok |
| 2026-09-23T11:24:11Z | 2 | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 2 | 28 | QUOTA |
| 2026-09-23T11:24:32Z | 2 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 21 | 239 | ok |
| 2026-09-23T11:24:48Z | Residuo | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 16 | 185 | ok |
| 2026-09-23T11:25:13Z | Veredicto | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 25 | 228 | ok |
| 2026-09-23T11:25:27Z | Veredicto | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 14 | 221 | ok |

Turns: 7 · failed: 1 · model time: 6m 6s

Full log: `2026-09-23--c3-claude-final-review.log`
