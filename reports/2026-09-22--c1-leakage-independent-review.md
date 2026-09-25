# C1: revisión analítica independiente de la fuga IR

Fecha: 2026-09-22. **Veredicto: PASS**, exclusivamente para C1 del
[contrato C1/C2/C3](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md).
No quedan reparaciones necesarias para las afirmaciones revisadas.

Revisor: agente independiente `/root/c1_independent_review`, separado del
agente que deriva C2. Firma de responsabilidad: **Codex,
`/root/c1_independent_review`, 2026-09-22**. Es una revisión independiente
de agente, no revisión humana, consenso de varios revisores, formalización
ni promoción canónica. La nota revisada no fue modificada.

## 1. Objeto, evidencia y límites

Se revisan desde las definiciones originales las secciones 2 y 3 de
[la nota de fuga](2026-09-22--ir-projection-leakage-and-conditioning.md):

\[
q_N=\|Q(U_M-I)\phi_N\|^2
=D N^{-5/2}+O(N^{-3}),\qquad
D=\frac{1024\pi^2\Phi_0(1/4)^2}{5}>0,
\]

para cada \(M\in\{I,\sigma_1,\sigma_2,\sigma_3\}\), y la identidad y
consecuencias de norma traza. Se conserva \(P=1_{|p|\le N^{-1/2}}\),
\(Q=I-P\), el recurso exacto y el perfil original de Alice. No se cambia
el filtro ni se modifica la clase de encoders.

Las convenciones y definiciones se contrastaron con las secciones 2.1,
3.1–3.4 y 6 del
[manuscrito](../papers/ir-corona/ir-corona.md), y con las definiciones
correspondientes del `.tex`, que es su fuente autoritativa. También se
leyeron `/home/ignac/AGENTS.md`, `PROJECT_INSTRUCTIONS.md` y el estado
canónico, especialmente sus secciones 9 y 10. La ley total de señal de
Theorem 4.4 se usa como premisa previamente registrada, sin volver a
certificar su prueba.

Base Git observada: `2b29b1935e6414ab9d9490290849b8a0ffbb618f`.
Los siguientes SHA256 identifican los archivos efectivamente revisados;
la nota y el contrato eran archivos locales no incorporados a esa base.

| Archivo | SHA256 |
| --- | --- |
| `reports/2026-09-22--ir-projection-leakage-and-conditioning.md` | `c2f99ce9d2a17946c167f8534a5a5964837aa53a7f0dbcf64c80dad98cbbf9cb` |
| `theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md` | `ebc862f3d9dc7fa40c1cf7764aa2d6d6e8669013dfb97fcb98067a8c58c5edf8` |
| `papers/ir-corona/ir-corona.md` | `afcc25057f0a258888b71e25a5692ec06bfec1c76ac59132da73ded2ee89e7f3` |
| `papers/ir-corona/ir-corona.tex` | `05a2eb09d2f103608683978c292de939511359677727982de441970f2e655636` |
| `scripts/verify_ir_projection_leakage.py` | `0fc8fad300cbca9adb6a30dd26b00bf11817a68fe9ae90754d4035221a956094` |
| `PROJECT_INSTRUCTIONS.md` | `6eeb95aa082ac45ce33d5e016db53f1f3991fed105ae7f865dedc0e552d59c03` |
| `state/CURRENT_STATE.md` | `47d77da9daeee9696c376c6a011096be6b73c38ad9343041660a7f5f8892142a` |

C2, C3, la estabilidad inhomogénea y E/AdS quedan fuera de esta revisión.
En particular, no se decide el término líder de \(L_{PP}\), el predominio
del bloque PP ni la interpretación experimental de la proyección global.

## 2. Reconstrucción del recurso y ataque a la normalización

La convención es \(\hat\psi(p)=\sum_xe^{ip\cdot x}\psi(x)\), con medida
\(d^3p/(2\pi)^3\). Para \(g(q)=(1-|q|^2)_+^2\),

\[
\int_0^1 r^2(1-r^2)^4dr=\frac{128}{3465},\qquad
\int_{\mathbb R^3}|g(q)|^2\frac{d^3q}{(2\pi)^3}
=\frac{64}{3465\pi^2}.
\]

Por tanto el \(Z_N\) del manuscrito normaliza exactamente el estado.
El cambio \(q=Np\), cuyo soporte queda dentro de la celda de Brillouin,
da sin aproximación

\[
\phi_N(x)=N^{-3/2}\Phi_0(x/N)\chi,\quad \chi=\downarrow,\qquad
\Phi_0(X)=\frac{\sqrt{3465}}{64\pi^2}
\int g(q)e^{-iq\cdot X}d^3q.
\]

Es real, radial y analítica; su germen radial en el origen es par.
Además \(P\phi_N=\phi_N\), pues \(N^{-1}\le N^{-1/2}\).
Para \(b=1/4\), la fórmula angular da

\[
B:=\Phi_0(b)=\frac{\sqrt{3465}}{64\pi^2}\,16\pi
\int_0^1 r(1-r^2)^2\sin(r/4)dr>0.
\]

La positividad procede de un integrando estrictamente positivo en
\((0,1)\); no depende de una evaluación flotante ni de un posible signo
de una expresión trigonométrica cancelante.

Como \(M^2=I\) para los cuatro encoders, incluyendo \(M=I\), se obtiene
exactamente \(a_N=(U_M-I)\phi_N=N^{-3/2}A_M(x/N)\), donde

\[
A_M(X)=\Phi_0(X)\left[(\cos(\pi F(|X|)/2)-1)\chi
+i\sin(\pi F(|X|)/2)M\chi\right],
\quad F(r)=(1-16r^2)_+^2.
\]

No se introdujo aquí un estado continuo sustituto: \(A_M\) es una
función fija cuyas muestras son exactamente la perturbación discreta.

## 3. Ataque al borde, al origen y al resto de Fourier

Poniendo \(t=b-r\),

\[
F(b-t)=64t^2-256t^3+256t^4,
\qquad A_M(b-t)=i32\pi B M\chi\,t^2+O(t^3).
\]

El término de coseno empieza en \(t^4\), por lo que no puede cancelar el
coeficiente cuadrático. \(A_M\) es analítica desde el interior y su
extensión por cero es \(C^1\); no se presupone que sea \(C^\infty\) a
través de la esfera. Es precisamente este borde el que genera la cola.

Para \(h(r)=rA_M(r)\), las condiciones relevantes son

\[
h(0)=h''(0)=h(b)=h'(b)=0,\qquad
h''(b)=i16\pi B M\chi.
\]

El germen impar de \(h\) justifica \(h''(0)=0\). No hace falta que
\(h'(0)\) se anule: su término de borde lleva \(\sin0\).
Con \(k=|k|>0\), la integración angular es exacta:

\[
\widehat A_M(k)=\frac{4\pi}{k}\int_0^b h(r)\sin(kr)dr.
\]

Integrando por partes cuatro veces únicamente en el intervalo interior,
donde todas las derivadas existen y son integrables, resulta

\[
\widehat A_M(k)=
\frac{4\pi h''(b)\cos(kb)}{k^4}
-\frac{4\pi h'''(b)\sin(kb)}{k^5}
+\frac{4\pi}{k^5}\int_0^b h''''(r)\sin(kr)dr.
\]

Así queda verificado tanto el signo como el resto:

\[
\widehat A_M(k)=i64\pi^2B M\chi\frac{\cos(k/4)}{k^4}+R_M(k),
\quad
\|R_M(k)\|\le\frac{4\pi}{k^5}
\left(\|h'''(b)\|+\int_0^b\|h''''(r)\|dr\right).
\]

La uniformidad angular es exacta por radialidad. Para \(k\) pequeño,
la norma \(L^1\) de \(A_M\) completa la cota global
\(\|\widehat A_M(k)\|\le C(1+|k|)^{-4}\). Todas las constantes pueden
tomarse uniformes en los cuatro encoders, al ser una familia finita.
Los vectores \(M\chi\) son respectivamente
\(\downarrow,\uparrow,-i\uparrow,-\downarrow\), siempre de norma uno.

## 4. Ataque a los ceros oscilatorios y a la constante D

El cuadrado del término principal, integrado con la medida congelada,
es

\[
\frac{4\pi}{(2\pi)^3}(64\pi^2B)^2
\int_K^\infty k^{-6}\cos^2(k/4)dk
=2048\pi^2B^2\int_K^\infty k^{-6}\cos^2(k/4)dk.
\]

El término cruzado con \(R_M\) es \(O(K^{-6})\): su integrando radial
en valor absoluto es \(O(k^{-7})\). El cuadrado del resto es
\(O(K^{-7})\). No se exige una cota inferior puntual para el coseno.
La identidad \(\cos^2(k/4)=(1+\cos(k/2))/2\) y una integración por
partes en el término oscilatorio dan

\[
\int_K^\infty k^{-6}\cos^2(k/4)dk
=\frac{K^{-5}}{10}+O(K^{-6}).
\]

En consecuencia,

\[
\int_{|k|>K}\|\widehat A_M(k)\|^2\frac{d^3k}{(2\pi)^3}
=\frac{1024\pi^2B^2}{5}K^{-5}+O(K^{-6}).
\]

Los nodos de \(\cos(k/4)\) no eliminan la masa integrada ni permiten
excepciones en subsecuencias de \(N\). El coeficiente positivo es el
mismo para los cuatro encoders, sin afirmar igualdad a \(N\) finito.

## 5. Ataque a Poisson y a las imágenes de la red

La legitimidad de Poisson se puede demostrar sin invocar una versión
que exija suavidad global mayor que la disponible. Defínase

\[
H_N(k)=\sum_{m\in\mathbb Z^3}\widehat A_M(k+2\pi Nm),\qquad
C_N=[-\pi N,\pi N]^3.
\]

La cota de orden cuatro asegura convergencia absoluta y uniforme en la
celda, y \(\widehat A_M\in L^1(\mathbb R^3)\). Los coeficientes de
Fourier de esta función continua y periódica son, por intercambio
absolutamente convergente e inversión de Fourier,

\[
\frac{1}{(2\pi N)^3}\int_{C_N}H_N(k)e^{-ik\cdot x/N}d^3k
=N^{-3}A_M(x/N),\qquad x\in\mathbb Z^3.
\]

Sólo un número finito de estos coeficientes es no nulo. La unicidad de
los coeficientes de una función periódica continua identifica \(H_N\)
con ese polinomio finito. Por ello

\[
\widehat a_N(p)=N^{3/2}H_N(Np)
=N^{3/2}\sum_m\widehat A_M(Np+2\pi Nm)
\]

es una identidad exacta, no una aproximación de suma por integral.

Para \(k\in C_N\) y \(m\ne0\), coordenada a coordenada,
\(|k_j+2\pi Nm_j|\ge\pi N|m_j|\) si \(m_j\ne0\); por tanto
\(|k+2\pi Nm|\ge\pi N|m|\). Como
\(\sum_{m\ne0}|m|^{-4}<\infty\) en dimensión tres,

\[
E_N(k):=\sum_{m\ne0}\widehat A_M(k+2\pi Nm)=O(N^{-4})
\]

uniformemente en toda la celda, incluso sus caras y esquinas. Su norma
\(L^2(C_N,d^3k/(2\pi)^3)\) es \(O(N^{-5/2})\).

El cambio \(k=Np\) cancela exactamente el factor \(N^3\) de la norma
cuadrada del transformado. El complemento de \(P\) se convierte en
\(\Omega_N=C_N\cap\{|k|>\sqrt N\}\), de modo que

\[
q_N=\int_{\Omega_N}\|\widehat A_M(k)+E_N(k)\|^2
\frac{d^3k}{(2\pi)^3}.
\]

El presupuesto completo de errores es:

| Contribución | Orden absoluto |
| --- | --- |
| Masa central continua | \(D N^{-5/2}+O(N^{-3})\) |
| Masa central fuera de \(C_N\) | \(O(N^{-5})\) |
| Norma central en \(\Omega_N\) | \(O(N^{-5/4})\) |
| Norma de las imágenes en \(\Omega_N\) | \(O(N^{-5/2})\) |
| Término cruzado central/imágenes | \(O(N^{-15/4})\) |
| Cuadrado de las imágenes | \(O(N^{-5})\) |

La segunda fila usa \(\mathbb R^3\setminus C_N\subset\{|k|>\pi N\}\);
la quinta usa Cauchy–Schwarz. Todos los errores de muestreo son menores
que \(O(N^{-3})\). No se necesita cancelación entre imágenes ni una
hipótesis sobre la aritmética de la esfera. Queda probado

\[
\boxed{q_N=D N^{-5/2}\bigl(1+O(N^{-1/2})\bigr),\quad D>0.}
\]

## 6. Ataque a la interpretación en norma traza

Sean \(v=U_M\phi_N\), \(w=Pv\), \(t=Qv=Qa_N\) y \(q=\|t\|^2\).
Como \(\|v\|=1\), \(w\perp t\) y \(P\phi_N=\phi_N\),

\[
\Delta-P\Delta P=|w\rangle\langle t|+|t\rangle\langle w|
+|t\rangle\langle t|,
\qquad \operatorname{tr}(P\Delta P)=-q.
\]

Para \(0<q<1\) su matriz en las direcciones normalizadas de \(w,t\) es
\(\left(\begin{smallmatrix}0&\sqrt{q(1-q)}\\
\sqrt{q(1-q)}&q\end{smallmatrix}\right)\). El determinante es negativo;
los autovalores tienen signos opuestos y su diferencia es
\(\sqrt{4q-3q^2}\). Los extremos \(q=0,1\) se verifican directamente.
Por tanto

\[
\boxed{\|\Delta-P\Delta P\|_1=\sqrt{4q_N-3q_N^2}
=2\sqrt D\,N^{-5/4}\bigl(1+O(N^{-1/2})\bigr).}
\]

No es la distancia traza entre dos estados normalizados: \(P\Delta P\)
tiene traza \(-q_N\), y no corresponde insertar aquí automáticamente
un factor \(1/2\) ni identificarla con el observable de Bob.

La fuga es estrictamente positiva para todo \(N\ge2\): \(a_N\) es de
soporte finito, no nula en el origen, y si \(Qa_N=0\), su polinomio
trigonométrico se anularía en un abierto del toro. La continuidad y
analiticidad forzarían que fuera idénticamente cero.

También se verificó el denominador de la admisibilidad relativa. Con
los dos conjuntos interiores/exteriores de la sección 6 del manuscrito,
ambos de masa al menos \(m>0\), las fases obedecen
\(\operatorname{Re}(t_x\overline t_y)\le1/\sqrt2\) entre ellos.
Todos los demás sumandos de
\(1-|\langle\phi_N,U_M\phi_N\rangle|^2\) son no negativos. Así

\[
2m\sqrt{2-\sqrt2}\le\|\Delta\|_1\le2\quad(N\ge32).
\]

Por ello \(\eta_{\rm enc}^M=\Theta(N^{-5/4})\) para el recurso
congelado. Esto no mejora automáticamente la cota de norma de operador
\(\eta_{\rm op}\), que cuantifica sobre todos los estados de la banda.

Al aceptar como premisa la ley total ya registrada, con coeficiente
uniformemente no nulo y acotado, se sigue

\[
\frac{\|\Delta-P\Delta P\|_1}{\delta_{M,M_B}(N)}
=\frac{2\sqrt D}{|C_{M,M_B}(\theta_N)|}
N^{21/4}e^{K_*N}\bigl(1+O(N^{-1/2})\bigr)\longrightarrow\infty.
\]

Esta consecuencia sí tiene una cota inferior asintótica positiva en el
numerador. Una mera cota superior original \(O(N^{-1/2})\) no habría
bastado. Pero

\[
|L-L_{PP}|\le\|\Delta-P\Delta P\|_1
\]

es sólo una cota superior: no permite decidir
\(L-L_{PP}=o(|L|)\), su negación, ni atribuir predominio espectral.

## 7. Verificación auxiliar y dictamen

Se leyó y ejecutó el verificador existente, sin modificarlo:

```sh
python3 -B scripts/verify_ir_projection_leakage.py
```

Resultado: **27/27 PASS**, Python 3.12.3, SymPy 1.14.0. Su texto final
`analytic remainders UNREVIEWED` describe correctamente el alcance del
programa; la revisión analítica de esos restos es la prueba escrita en
las secciones 3–5 de este documento. No se creó código, no hubo ajuste
ni barrido nuevo de valores de \(N\).

| Ataque con posible efecto decisivo | Resultado |
| --- | --- |
| Normalización, medida y escala del corte | PASS: factores exactos reconstruidos |
| Cancelación del borde en alguno de los cuatro encoders | PASS: coeficiente no nulo y misma norma |
| Contribución espuria del origen radial | PASS: paridad y términos de borde controlados |
| Resto de Fourier sin suavidad global suficiente | PASS: derivadas interiores bastan y resto explícitamente acotado |
| Ceros oscilatorios que destruyan la equivalencia | PASS: promedio integrado con resto \(O(K^{-6})\) |
| Uso ilegítimo de Poisson para una función sólo \(C^1\) | PASS: periodización continua y coeficientes reconstruidos |
| Imágenes de la red del mismo orden que la masa principal | PASS: todos los errores son \(o(N^{-3})\) salvo el resto continuo previsto |
| Identificación indebida con distancia operacional | PASS: se conserva el defecto de traza y la separación del observable |

**C1 = PASS; reparaciones necesarias pendientes = ninguna.** La
conclusión independiente es válida para estos cuatro encoders, este
recurso, perfil, dimensión y corte. Las constantes de resto y el umbral
asintótico no se hacen numéricamente explícitos. El PASS no establece
novedad, predominio PP, cierre de C2/C3, consenso de múltiples miembros,
promoción del estado canónico ni reapertura de E/AdS.
