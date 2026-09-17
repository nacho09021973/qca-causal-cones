# Revisión independiente: REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE

**Fecha:** 2026-09-17. **Rama:** `research/b-infinity-post-s4-gate`.

**Veredicto de revisión: `PASS`.** No hay reparación obligatoria.

**Veredicto científico revisado:** `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS`.
**Correcto.**

**Estado congelable hoy:**
`OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`.

Encargo restringido a tres afirmaciones. No se clasifica \(C\). No se
abre un gate de coeficientes en este acto.

El mensaje de encargo ya nombraba \(v_*\), \(I(v)\) y \(O(\log N)\). La
derivación es propia; no es ciega a esos valores.

## 0. Orden y hashes

1. Charter de este gate.
2. Símbolo `walk2`, continuación \(p=-i\xi\), \(\nabla\phi\), \(h(t)\), a
   mano y SymPy propio (`/tmp/review_Kstar.py`, sin el certificado del
   gate).
3. Geometría de \(V_{\mathrm{reg}}\) y el hiperplano de soporte.
4. Taylor de \(F_N\) y el modelo unidimensional de la capa.
5. **Después**, informe de ejecución y certificado.

| Archivo | sha256 |
| --- | --- |
| `theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md` | `3a5fe8d4b22c26d017994eb849ea4e896b6e9a5230758f5c678c135c8e38977d` |
| `reports/2026-09-17--regional-directional-asymptotics-gate.md` | `13edb516b89d87b6b159baef55d394ffb323c7f0046572502891ff35da79000e` |
| `scripts/verify_regional_directional_asymptotics_gate.py` | `e8a9df88d1ae1aa3b2dcf51b5c1050b23be79ca452a69220d65dbab4ed98eb4f` |
| `state/CURRENT_STATE.md` (aún `NOT_EXECUTED` en §8.19) | `b9576ef18c1db1b7233043f85cdfbc6d9adde7ae7e9673cc15247c1d278d2100` |

`HEAD = origin = 08613d0…`. Tracked limpio. Certificado reejecutado:
**18/18**.

## 1. Derivación de \(I(v)\) y del saddle dual — PASS

**Holomorfía y traza.** \(S(p)\) es trigonométrico, \(\det S\equiv 1\).
La traza continúa como \(f(-i\xi)=\prod\cosh\xi_j\). Independientemente:
\(\nabla\phi=\lambda\tanh\xi\) componente a componente, con
\(\phi=\operatorname{arcosh}(\prod\cosh)\) y
\(\lambda=f/\sqrt{f^2-1}\) [C].

**Cota de Legendre.** El tilt del kernel da, para todo \(\xi\),
\(|G_N(Nv)|\le CN\exp(-N[\xi\cdot v-\log\rho(S(-i\xi))])\). El lema de
elipses heredado (revisado en el gate escalado) acota
\(\rho(S(\eta-i\xi))\le\exp\operatorname{arcosh}(\prod\cosh\xi_j)\), con
igualdad en \(\eta=0\). Por tanto

\[
|G_N(Nv)|\le CN\,e^{-NI(v)},\qquad
I(v)=\sup_\xi\bigl[\xi\cdot v-\operatorname{arcosh}(\prod\cosh\xi_j)\bigr].
\]

Eso identifica \(I\) como **envolvente convexa de la tasa** (limsup
\((1/N)\log|G|\le -I\)). El informe no afirma el matching inferior de
\(G\) ni de \(L\); \(C\) queda abierto. Coherente con `OPEN`.

**Saddle dual isótropo.** En \(\xi=t(1,1,1)\),
\(v=h(t)(1,1,1)\) con \(h(t)=\lambda(t)\tanh t\). Límites [C]:
\(h(0^+)=1/\sqrt3\), \(h(\infty)=1\). La derivada [C]

\[
h'(t)=\frac{(\sinh^2 t+3)\sinh^4 t\cosh t}{\mathrm{den}>0}
\]

es **estrictamente positiva** para \(t>0\). Luego \(h:(0,\infty)\to(1/\sqrt3,1)\)
es un difeomorfismo. Como \(\alpha=1-1/(2\sqrt3)\) cumple
\(1/\sqrt3<\alpha<1\) (\(4>3\) y \(\alpha<1\)), existe un único \(t_*>0\)
con \(h(t_*)=\alpha\), y \(\xi_*=t_*(1,1,1)\) es el dual de

\[
v_*=\Bigl(1-\frac1{2\sqrt3}\Bigr)(1,1,1).
\]

Esa es la expresión pretendida. \(I(v_*)=3\alpha t_*-\operatorname{arcosh}(\cosh^3 t_*)\).

**No es \(J\) ni \(\log 4\).** El tilt factible \(t=\log 2\) da
\(I(v_*)\ge\sigma\log 2-\operatorname{arcosh}(125/64)>J\) porque
\(125/64<17/8\). Y \(\alpha<1\), \(\xi_*>0\) dan
\(\xi_*\cdot v_*<\xi_*\cdot(1,1,1)\), luego \(I(v_*)<I(1,1,1)=\log 4\).

## 2. Unicidad de \(v_*\) como minimizador regional — PASS

\(V_{\mathrm{reg}}\subset(1,1,1)+\overline B(0,1/2)\) y
\(\|v_\ast\|_\infty=\alpha<1\), así que \(v_*\) es microscópicamente
admisible.

Por definición de \(I\), \(I(v)\ge\xi_*\cdot v-\phi(\xi_*)=I(v_*)+\xi_*\cdot(v-v_*)\).
Con \(\hat u=(1,1,1)/\sqrt3\),

\[
\hat u\cdot v=\sqrt3+\hat u\cdot w\ge\sqrt3-\tfrac12=|v_*|
\]

para todo \(w\) con \(|w|_2\le 1/2\), igualdad **si y sólo si**
\(w=-(1/2)\hat u\), i.e. \(v=v_*\). Como \(\xi_*\parallel\hat u\) y
\(t_*>0\),

\[
I(v)\ge I(v_*)\quad\text{en }V_{\mathrm{reg}},
\]

igualdad únicamente en \(v_*\). No se sustituye el mínimo euclídeo a
ciegas: el mismo punto minimiza \(I\) porque el dual es radial en
\(\hat u\). Sobre la red, el ínfimo asintótico sigue siendo \(I(v_*)\)
por continuidad.

## 3. Los perfiles son \(O(\log N)\) y no cambian \(K_*\) — PASS

En profundidad de red \(\varepsilon=N/4-|x|_2\),

\[
F_N=\frac{64\varepsilon^2(N-2\varepsilon)^2}{N^4},
\]

luego \(\log F_N=2\log\varepsilon-2\log N+O(1)\) y lo mismo para
\(h_B\) y para \(s_N=\Theta(F)\). Eso es \(O(\log N)\) si
\(\varepsilon=N^{O(1)}\) no exponencialmente pequeño, y \(O(1)\) en el
interior macroscópico. Sería \(O(N)\) sólo si \(\varepsilon=e^{-\Theta(N)}\),
que manda \(\log s_N\to-\infty\) linealmente en \(N\) y **no** maximiza.

El término \(O(N)\) del log es \(-NI(v)\). \(I\) es \(C^1\) en \(v_*\)
porque \(\xi_*\neq 0\). La derivada normal interior es \(\kappa=|\xi_*|>0\).
El modelo \(-\kappa\varepsilon+p\log\varepsilon\) tiene crítico
\(\varepsilon=p/\kappa=O(1)\). Ese desplazamiento es submacroscópico:
\(N\Delta I=O(1)\), absorbido en \(C\), no en \(K_*\).

Por tanto, tras la competición —no omitiéndola—

\[
K_*=I(v_*).
\]

Los perfiles pueden cambiar \(\beta\) y \(C\); el informe no los finge
clasificados. El estado `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS` es el
único compatible: \(K_*\) está identificado y \(C\) no.

**Alcance de \(K_*\).** Es la envolvente de Legendre del kernel
regional. Es la tasa de \(L\) si y sólo si algún \(C\) (o \(C^{(j)}\))
es no nulo y controlado, lo cual el informe no afirma. Esa distinción
está en §§7–8 del informe y se conserva.

## 4. Veredicto

| Afirmación | Resultado |
| --- | --- |
| Derivación de \(I(v)\) y del saddle dual | **PASS** |
| Unicidad de \(v_*\) como minimizador regional | **PASS** |
| Perfiles \(O(\log N)\), no alteran \(K_*\) | **PASS** |

Congelar `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`
está autorizado. El cuello de botella restante es el coeficiente
Laplace integrado (Hessiano, perfiles en la capa \(O(1)\), spin,
interferencia con \(r\)), no la tasa ni la geometría. No se abre ese
gate en esta revisión.
