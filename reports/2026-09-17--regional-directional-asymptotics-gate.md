# REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE — ejecución del contrato publicado

Registro de ejecución, 2026-09-17. Evaluación del autor; sin revisión
independiente ni promoción canónica. [A] identifica pruebas analíticas;
[V] identidades del certificado. **No se ha modificado el charter.**

**Resultado: `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS`.** Se identifica la
tasa exponencial regional

\[
K_*=I(v_\ast),\qquad
v_\ast=\Bigl(1-\frac1{2\sqrt3}\Bigr)(1,1,1),
\]

con \(I(v)=\sup_\xi\bigl[\xi\cdot v-\operatorname{arcosh}(\prod_j\cosh\xi_j)\bigr]\).
La competición perfil/exponente es \(O(\log N)\) y desplaza el saddle
una distancia **\(O(1)\)** (sitios de red); **no cambia \(K_*\)**. El
coeficiente \(C_{M,M_B}\) y el exponente \(\beta\) **no** quedan
clasificados: el Hessiano regional completo y la suma de interferencias
(incluida la cola libre \(r\)) no se controlan hasta \(C+o(1)\).

Certificado auxiliar: **18/18 identidades**. No cubre \(C\), \(\beta\) ni
el resto.

## 1. Preflight

- Repositorio: `nacho09021973/qca-causal-cones`.
- Rama: `research/b-infinity-post-s4-gate`.
- `HEAD`, `origin/research/b-infinity-post-s4-gate` y
  `git ls-remote origin refs/heads/research/b-infinity-post-s4-gate`:
  `08613d0bdcd5a47ebbbd0f94204a60051dee2d47`.
- SHA256 de `theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md`:
  `3a5fe8d4b22c26d017994eb849ea4e896b6e9a5230758f5c678c135c8e38977d`,
  idéntico al blob de `08613d0`.
- Tracked limpio. Untracked preexistentes preservados (auditoría, dos
  logs, `__pycache__/`). Python con `-B`.
- SHA256 de `state/CURRENT_STATE.md` al arrancar:
  `b9576ef18c1db1b7233043f85cdfbc6d9adde7ae7e9673cc15247c1d278d2100`.
  **No se modifica.**

Leídos el charter de este gate, §§8.17–8.18, los dos charters e informes
escalado y de cancelación, y los helpers de `walk2` / bloques.

## 2. Herencia — Paso 0

Premisas, sin reabrirlas: cota \(36N^4 e^{-JN}\); ocho operaciones
IR-admisibles; (L)/(F) y las cuatro columnas; el vértice \(4^{-N}\) no se
promueve; el mínimo euclídeo cae en \(F_N=h_B=0\) y no clasifica \(A\).
\(D_B=\tfrac12\|\rho_1-\rho_0\|_1\). \(I\) es `REFERENCE_CONTROL`.

## 3. Tasa anisótropa — Paso 1 [A]/[V]

### 3.1 Dominio holomorfo

\(S(p)\) es un polinomio trigonométrico, entero en cada \(e^{ip_j}\).
La continuación \(p=\eta-i\xi\), \(\eta\in\mathbb T^3\), \(\xi\in\mathbb R^3\),
no encuentra polos. \(\det S\equiv 1\) [V]. La traza continúa como

\[
f(-i\xi)=\prod_{j=1}^3\cosh\xi_j \tag{Fξ}
\]

[V]. El lema de elipses heredado da, para todo \(\eta\) real,

\[
\rho\bigl(S(\eta-i\xi)\bigr)\le\exp\operatorname{arcosh}\Bigl(\prod\cosh\xi_j\Bigr)=\rho\bigl(S(-i\xi)\bigr),
\]

con igualdad en \(\eta=0\) (cada factor en el vértice real de su elipse).

### 3.2 Legendre

El kernel \(G_N(d)=(S^N)_d\) admite el tilt \(G_N(d)=e^{-\xi\cdot d}\int S(\eta-i\xi)^N e^{-i\eta\cdot d}\,d\mu\).
Por tanto, para todo \(\xi\),

\[
|G_N(Nv)|\le C N\,e^{-N[\xi\cdot v-\log\rho(S(-i\xi))]}.
\]

Se define

\[
I(v)=\sup_{\xi\in\mathbb R^3}\Bigl[\xi\cdot v-\operatorname{arcosh}\Bigl(\prod_j\cosh\xi_j\Bigr)\Bigr].
\]

Entonces \(|G_N(Nv)|\le C N\,e^{-N I(v)}\). \(I\) es convexa, \(I=0\) sobre
la bola \(|v|_2\le 1\) (porque \(\operatorname{arcosh}(\prod\cosh\xi)\sim|\xi|_2\)
cerca de \(0\)), e \(I=\infty\) si \(\|v\|_\infty>1\). En el vértice del cubo,
el camino único fija \(I(1,1,1)=\log 4\).

El punto crítico en \(\xi\) cumple \(v=\nabla\phi\),
\(\phi=\operatorname{arcosh}(\prod\cosh)\), i.e.
\(v_j=\lambda\tanh\xi_j\) con \(\lambda=\prod\cosh/\sqrt{(\prod\cosh)^2-1}\).
El máximo de \(\rho(S(\eta-i\xi))\) en el toro es único en \(\eta=0\).

### 3.3 Mínimo sobre el conjunto regional

\[
V_{\mathrm{reg}}=\bigl\{(y-x)/N:x\in A_N,\,y\in B_N\bigr\}
\subset (1,1,1)+\overline B(0,1/2),\qquad \|v\|_\infty\le 1.
\]

El punto de \(|v|_2\) mínimo es único [V]:

\[
v_\ast=\alpha(1,1,1),\qquad \alpha=1-\frac1{2\sqrt3},\qquad
|v_\ast|_2=\sqrt3-\frac12>1.
\]

Sea \(\xi_\ast=t_\ast(1,1,1)\) el dual de \(v_\ast\) (\(t_\ast>0\) único:
\(\alpha\in(1/\sqrt3,1)\) [V], y \(h(t)=\lambda(t)\tanh t\) interpola
continuamente \((1/\sqrt3,1)\)). Por definición de \(I\), para todo \(v\)

\[
I(v)\ge \xi_\ast\cdot v-\phi(\xi_\ast)=I(v_\ast)+\xi_\ast\cdot(v-v_\ast).
\]

Sobre \(V_{\mathrm{reg}}\), \(\hat u\cdot v\ge |v_\ast|\) con igualdad **sólo**
en \(v_\ast\) (igualdad en \(|c+w|\ge|c|-|w|\)). Como \(\xi_\ast\parallel\hat u\)
y \(t_\ast>0\),

\[
I(v)\ge I(v_\ast)\qquad\text{en }V_{\mathrm{reg}},
\]

con igualdad únicamente en \(v_\ast\) [A].

Así el infimo de la tasa anisótropa sobre las velocidades regionales es
**exactamente** \(I(v_\ast)\), no el mínimo radial sustituido a ciegas, sino
el dual de \(\phi\) evaluado en el único minimizador geométrico, que el
soporte de \(\xi_\ast\) demuestra que también minimiza \(I\).

### 3.4 \(K_*\) no es \(J\) ni \(\log 4\)

El tilt factible \(\xi=(\log 2)(1,1,1)\) da

\[
I(v_\ast)\ge \sigma\log 2-\operatorname{arcosh}(125/64)> \sigma\log 2-\log 4=J,
\]

porque \(125/64<17/8\) [V] y \(\sigma=3\alpha=3-\sqrt3/2\). Por el otro
lado, \(\alpha<1\) y \(\xi_\ast>0\) implican
\(\xi_\ast\cdot v_\ast<\xi_\ast\cdot(1,1,1)\), luego
\(I(v_\ast)<I(1,1,1)=\log 4\).

Se **no** identifica \(K_*\) con \(J\) ni con \(\log 4\). Queda

\[
\boxed{K_*=I(v_\ast)=3\alpha t_\ast-\operatorname{arcosh}(\cosh^3 t_\ast)},
\]

donde \(t_\ast>0\) es la única solución de
\(\alpha=\lambda(t)\tanh t\). (Numéricamente \(K_*\approx 0.1905\),
estrictamente entre \(J\approx 0.0929\) y \(\log 4\); esa cifra es
diagnóstico, no evidencia terminal.)

## 4. Perfil vs exponente — Paso 2 [A]

Logaritmo del integrando \(h_B(y)\,G_N(y-x)\,s_N(x)\) (o \(c_N\)):

\[
\log = \underbrace{-N\,I((y-x)/N)}_{O(N)}
+\underbrace{\log h_B+\log s_N}_{O(\log N)\text{ o }O(1)}.
\]

En el interior macroscópico, \(F_N\) y \(h_B\) son \(O(1)\), luego
\(O(1)\) en el log. En una capa de profundidad \(\varepsilon\) (unidades
de red), \(F_N=\Theta(\varepsilon^2/N^2)\) [V], \(s_N=\Theta(F)= \Theta(\varepsilon^2/N^2)\),
\(\log s_N=2\log\varepsilon-2\log N+O(1)\), que es \(O(\log N)\) para
\(\varepsilon=N^{O(1)}\) y \(O(N)\) **sólo** si \(\varepsilon=e^{-\Theta(N)}\),
lo cual **empeora** el funcional y no es un máximo.

Conclusión vinculante: el cero del perfil **no** introduce un término
\(O(N)\) en el log. No autoriza a cambiar \(K_*\). Puede cambiar
\(\beta\), \(C\), \(C^{(j)}\) y desplazar el saddle submacroscópicamente.

Escala del desplazamiento. \(I\) es \(C^1\) en \(v_\ast\) (el dual
\(\xi_\ast\neq 0\); \(\phi\) es \(C^\infty\) fuera del origen). La derivada
normal hacia el interior de las bolas es \(\kappa=|\xi_\ast|>0\). El modelo
unidimensional \(- \kappa\varepsilon+p\log\varepsilon\) tiene crítico
\(\varepsilon=p/\kappa=O(1)\) [V] (\(p=2\) para \(s_N\sim\varepsilon^2/N^2\),
o \(p=4\) si se cuentan ambos perfiles). El Hessiano tangencial de \(I\)
es definido positivo (Legendre de \(\phi\) estrictamente convexa fuera de
\(0\)), así que el máximo efectivo está a distancia **\(O(1)\)** de
\((x_\ast,y_\ast)\) en unidades de red, i.e. \(O(1/N)\) en \(v\).

Eso produce \(N\Delta I=O(1)\), absorbido en \(C\), no en \(K_*\).

El saddle **físico** es esa capa \(O(1)\), no el punto geométrico (donde
el integrando se anula) y no un desplazamiento macroscópico \(O(N)\).
Tras la competición,

\[
K_*=I(v_\ast)
\]

queda justificado, no por omitir el perfil, sino porque el perfil no
toca el orden \(N\).

## 5. Laplace regional — Paso 3 [A]

Un único saddle geométrico en \(V_{\mathrm{reg}}\) (\(v_\ast\)). Un único
máximo de \(\rho(S(\eta-i\xi_\ast))\) en el toro (\(\eta=0\)). El segundo
autovalor de \(S(-i\xi_\ast)\) es \(1/\lambda_{\mathrm{max}}\) (unimodular),
con gap. La mezcla \(\sinh t\) del símbolo inclinado es no nula para
\(t>0\) [V]: el autovector de Perron **no** está alineado con
\(\downarrow\). Las amplitudes \(\uparrow\) (\(b\)) y \(\downarrow\)
(\(a,d\)) comparten la misma tasa \(K_*\); \(b\) no es un segundo
exponente. \(c_N=O(F^2)\) frente a \(s_N=O(F)\) cambia el orden del
prefactor en la capa, no \(K_*\).

**No se clasifica \(C\).** Razones, todas obligatorias por el charter:

- Un integrando local no nulo (Perron con ambas componentes, \(s_N>0\)
  dentro de la bola) no implica \(C\neq 0\) tras integrar perfiles,
  fases y la cola libre \(r=S^N\phi_N\).
- \(L\) incluye interferencias \(\langle r,E\,\cdot\,\rangle\). \(r\) es
  de banda \(|p|\le N^{-1}\) y es \(O(N^{-3/2})\) en \(B_N\), no
  \(e^{-K_*N}\). Su factor de forma en \(|y|/N\sim\sqrt3-1/4\) no se ha
  demostrado no nulo, ni se ha sumado contra la capa.
- El Hessiano \(6\)-dimensional (dos bolas, relativas y tangenciales) no
  se reduce a un \(\beta\) único certificado. El \(N^{-3/2}\) del toro
  \(p\) es el recuento estándar si \(\mathrm{Hess}_p\log\rho\) es no
  degenerado en \(0\); esa no degeneración no se certifica aquí.
- No hay otros saddles de igual \(K_*\) en \(V_{\mathrm{reg}}\). No hay
  cancelación entre saddles geométricos que se pueda invocar para
  \(C=0\). Tampoco hay prueba de \(C=0\).

Sin \(C+o(1)\) controlado, el Paso 3 no cierra. No se baja a
\(C^{(j)}\) porque el líder \(C\) no está clasificado. La lower bound
bruta de \(\delta\) no se usa.

## 6. Los dieciséis pares

Misma \(K_*=I(v_\ast)\) para todos (un solo saddle regional). \(\beta\) y
\(C\) no clasificados. `OPEN_PAIR` en cada fila. No se supone equivalencia
Pauli: se registra el mismo saddle porque la tasa sale del radio
espectral, simétrico en las tres coordenadas, no porque \(\sigma_1\) y
\(\sigma_2\) coincidan internamente. El canal \(\uparrow\) comparte \(K_*\)
por la mezcla \(\sinh t\neq 0\), con prefactor distinto y no evaluado.

| Encoder | Detector | Saddle | \(K_*\) | \(\beta\) | \(C\) | si \(C=0\), motivo / \(C^{(j)}\) | Resto | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \(I\) (REFERENCE_CONTROL) | \(I\) | \(v_\ast\), capa \(O(1)\) | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |
| \(I\) | \(P_1\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |
| \(I\) | \(P_2\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |
| \(I\) | \(P_3\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_1\) | \(I\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | mezcla \(\uparrow\) a la misma tasa | no | OPEN_PAIR |
| \(\sigma_1\) | \(P_1\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_1\) | \(P_2\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_1\) | \(P_3\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_2\) | \(I\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | mezcla \(\uparrow\) a la misma tasa | no | OPEN_PAIR |
| \(\sigma_2\) | \(P_1\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_2\) | \(P_2\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_2\) | \(P_3\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | idem | no | OPEN_PAIR |
| \(\sigma_3\) | \(I\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_3\) | \(P_1\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_3\) | \(P_2\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |
| \(\sigma_3\) | \(P_3\) | idem | \(I(v_\ast)\) | no cert. | no clasificado | — | no | OPEN_PAIR |

\(P_j=(I+\sigma_j)/2\).

## 7. Estado terminal

**Único estado: `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS`.**

- No hay \(C\neq 0\) con resto \(o(1)\): no
  `SADDLE_RATE_AND_NONVANISHING_LEADING_COEFFICIENT`, y no se registra
  `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.
- No hay \(C=0\) clasificado ni primer \(C^{(j)}\): no
  `SADDLE_RATE_LEADING_VANISHES`. Eso no es \(\delta\equiv 0\).
- Ningún par \(M=I\) tiene \(C\) controlado: no
  `REFERENCE_CONTROL_ONLY_LEADING_NONVANISHING`.

Lo que sí queda establecido, y no es un estado terminal del charter, es
la tasa \(K_*=I(v_\ast)\) con el split \(O(N)\) vs \(O(\log N)\) y el
desplazamiento \(O(1)\). El cuello de botella pasa a ser el coeficiente
integrado (Hessiano + perfiles + cola \(r\) + fases), no la tasa.

## 8. Techo del claim

- \(K_*\) es la tasa de Legendre del kernel regional, no una asintótica
  completa de \(L\) ni de \(\delta\).
- No se afirma \(C\neq 0\), \(C=0\), ni \(\delta>0\).
- No se afirma \(D_B=0\).
- El vértice \(4^{-N}\) no es \(K_*\). \(J\) no es \(K_*\).
- Un desplazamiento \(O(1)\) del saddle no cambia la tasa exponencial.
- Sólo la clase congelada. Sin unidades físicas, sin `Delta T=2`, sin
  reabrir §§8.16–8.18.

## 9. Implementación

Se crea `scripts/verify_regional_directional_asymptotics_gate.py`. No se
modifica ningún verificador revisado.

**Necesidad.** Los certificados anteriores no contienen (Fξ), el dual
\(\alpha\in(1/\sqrt3,1)\), la mezcla \(\sinh t\) del símbolo inclinado, ni
el crítico unidimensional \(\varepsilon=p/\kappa\). Añadirlos a un script
revisado cambiaría sus bytes.

**Qué demuestra:** 18 identidades [V]. **Qué no:** \(C\), \(\beta\), el
resto, ni el estado terminal.

Dependencias: las mismas (Python 3.12, SymPy 1.14.0, NumPy transitivo).
Sin coma flotante en cantidades decisivas.

SHA256 del certificado nuevo:
`e8a9df88d1ae1aa3b2dcf51b5c1050b23be79ca452a69220d65dbab4ed98eb4f`.

## 10. Validación

Todos los comandos siguientes terminaron con código de salida `0`, desde
la raíz, `python3 -B`.

| Comando | Resultado |
| --- | --- |
| `scripts/verify_regional_directional_asymptotics_gate.py` | 18/18 identidades exactas |
| `scripts/verify_lower_bound_no_cancellation_gate.py` | 24/24 |
| `scripts/verify_scaled_ir_gate.py` | 53/53 |
| `scripts/verify_narrow_band_gate.py` | 34/34 |
| `scripts/verify_signaling_witness.py` | 17/17 |
| `scripts/verify_directional_saturation.py` | 27/27 |
| `scripts/verify_weyl_dirac_gate.py` | PASS |
| `scripts/cert_Aa_s4_counterexample.py` | PASS |
| `scripts/review_Aa_s4_exact.py` | PASS |

`git diff --check`: sin incidencias en los archivos nuevos. Ningún
archivo staged. `CURRENT_STATE.md` conserva el hash de §1.
**Sin commit ni push.**
