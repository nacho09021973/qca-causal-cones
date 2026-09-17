# Revisión independiente: LOWER_BOUND_NO_CANCELLATION_GATE

**Fecha:** 2026-09-17. **Rama:** `research/b-infinity-post-s4-gate`.

**Veredicto de revisión: `PASS`.** No hay reparación obligatoria de
cantidades ni de clasificación. Hay una aclaración recomendada de
redacción en el informe §3.1 (véase §4).

**Veredicto científico revisado:** `OPEN_AFTER_CANCELLATION_ANALYSIS`.
**Correcto.**

**Estado congelable hoy:**
`OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`.

Encargo restringido a tres afirmaciones de carga. No se reabre la cota
escalada. No se busca \(\delta>0\) ni \(\delta\equiv0\).

## 0. Independencia

El mensaje de encargo ya nombraba el vértice \(4^{-N}\), la capa
enfrentada y que \(A\) no queda clasificado. La derivación de las tres
afirmaciones es propia; no es ciega a esas conclusiones.

Orden: charter de este gate; geometría euclídea de las dos bolas y el
camino único, a mano y con SymPy propio (`/tmp/review_three_claims.py`,
sin importar `scripts/`); **después**, informe de ejecución y certificado.

| Archivo | sha256 |
| --- | --- |
| `theory/LOWER_BOUND_NO_CANCELLATION_GATE.md` | `5db6f88a2ca77bfd6d8af2bde9c20f683e05288a0c941f6cd59724e4fb510afb` |
| `reports/2026-09-17--lower-bound-no-cancellation-gate.md` | `33691df63d2f5449af435bf2436b52bd03e39160db751bd2814ac1d898578e90` |
| `scripts/verify_lower_bound_no_cancellation_gate.py` | `60ede622468e85b844385ede075cc2f13eb773161ceaa72d8c0e1f097157c06f` |
| `state/CURRENT_STATE.md` (aún `NOT_EXECUTED` en §8.18) | `0f316960d5892a069cef64d77f9f313f167b8a825de1267592d2aac0b3d46d52` |

`HEAD = origin = 1717d5e…`. Tracked limpio. Certificado reejecutado:
**24/24**.

## 1. El vértice no puede promoverse a líder regional — PASS

**Hechos rederivados [M]/[C].** Cada paso tiene coordenadas en
\(\{-1,0,1\}\). Un desplazamiento \((N,N,N)\) en \(N\) pasos exige
\(+1\) en cada coordenada en **cada** paso, luego sólo el bloque
\(S_{(1,1,1)}=\frac14\lvert\downarrow\rangle\langle\downarrow\rvert\).
Por tanto

\[
(S^N)_{(N,N,N),0}=4^{-N}\lvert\downarrow\rangle\langle\downarrow\rvert,
\qquad
S_{(1,1,1)}\lvert\uparrow\rangle=0.
\]

Tasa exacta \(K_{\mathrm V}=\log 4\). El canal \(b\) (columnas
\(\sigma_1,\sigma_2\)) no usa este rayo.

**Por qué no se promueve.** El charter lo prohíbe expresamente (rayo de
vértice \(\neq A\not=0\) de región). Independientemente: \(L\) es una
suma coherente sobre \(A_N\times B_N\), no el término \(x=0\), \(y=N(1,1,1)\).
Otros desplazamientos existen; su combinatoria no está controlada por el
camino único. Además \(\log 4>J=(1-\sqrt3/2)\log 2\) [C], así que la
**cota** heredada sobre otros kernels es exponencialmente más floja que
\(4^{-N}\). Eso impide tratar el vértice como el término de decaimiento
más lento. No prueba, por sí sola, que otro término lo domine: una cota
superior ajena no es una cota inferior de esos kernels.

**Carga aceptada:** el vértice **no puede promoverse** a líder regional
ni a \(A\not=0\). La frase del informe «Mecanismo V no es el líder de
región» es más fuerte que lo demostrado; véase §4. El `OPEN` no depende
de esa frase más fuerte.

## 2. El mínimo geométrico cae donde los perfiles se anulan — PASS

En unidades \(N=1\), \(R=1/4\), \(c=(1,1,1)\):

\[
y-x=c+w,\qquad |w|_2\le 1/2,
\qquad
|y-x|_2\ge |c|_2-1/2=\sqrt3-1/2>1
\]

(\(3>9/4\) [C]). Igualdad **si y sólo si** \(w=-(1/2)\hat c\), un único
par continuo:

\[
x_\ast=\frac14\hat u,\qquad
y_\ast=(1,1,1)-\frac14\hat u,
\qquad \hat u=(1,1,1)/\sqrt3.
\]

Ambos están sobre las esferas euclídeas [C]. Allí
\(F_N=(1-16|x|^2/N^2)^2=0\) y \(h_B=0\) [C].

La diferencia de Minkowski de dos bolas cerradas es una bola cerrada;
el punto de \(|c+w|\) mínimo es único. Por tanto el mínimo de
\(|y-x|_2\) sobre las regiones **continuas** es ese par, y los perfiles
se anulan ahí.

Esto es el mínimo **geométrico** (euclídeo / exceso sobre el cono IR).
No se afirma que sea el mínimo de la tasa anisótropa verdadera \(I(v)\).
El informe lo llama «candidato a mínimo de \(I\)»; esa cautela es
correcta y se conserva.

Sobre la red, el mínimo discreto es \(\ge\) el continuo. Los sitios
estrictamente interiores tienen \(F>0\); la capa próxima a la esfera
sigue siendo el locus geométrico relevante.

## 3. De ahí no se sigue \(A=0\) ni \(A\neq 0\) — PASS

Anular el integrando **en** el mínimo geométrico no anula el integral.
Es el caso estándar de Laplace con prefactor que se anula: el máximo
efectivo se desplaza hacia el interior, de orden \(O(1/N)\) si
\(I(v)\) tiene pendiente finita, y el líder toma la forma

\[
N^{-\beta}e^{-K_*N}\bigl(C+O(N^{-1})\bigr)
\]

con \(K_*\) posiblemente distinto de \(I\) en \(x_\ast,y_\ast\), y con
\(C\) no determinado por \(F(x_\ast)=0\).

Tampoco se obtiene \(C\neq 0\): hace falta el coeficiente tras integrar
los perfiles contra el kernel inclinado. El informe no lo calcula y no
lo finge. Un término \(\langle d,Ed\rangle\ge 0\) o el rayo de vértice
no nulo no cierran el signo de \(L\).

Sin \(A\) clasificado, el Paso 3 no procede. El estado
`OPEN_AFTER_CANCELLATION_ANALYSIS` es el único compatible con §4 del
charter. Los dieciséis `OPEN_PAIR` son correctos. No se asigna
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` ni \(D_B=0\).

El certificado 24/24 cubre camino único, esfera, Taylor de \(c_N,s_N\) y
geometría enfrentada. No cubre líder, \(A\) ni resto. Coherente.

## 4. Aclaración recomendada, no obligatoria

En el informe de ejecución, §3.1, última frase:

> «Mecanismo V no es el líder de región.»

Sustituible, sin cambiar el veredicto, por: el vértice **no puede
promoverse** a líder regional; no está clasificado como líder, y
\(\log 4>J\) sólo compara su tasa exacta con una **cota** sobre los
demás kernels. El `OPEN` ya no depende de una dominancia demostrada.

## 5. Veredicto

| Afirmación | Resultado |
| --- | --- |
| El vértice no puede promoverse a líder regional | **PASS** |
| El mínimo geométrico cae en la capa de perfiles nulos | **PASS** |
| Eso no implica \(A=0\) ni \(A\neq 0\) | **PASS** |

Congelar `OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`
está autorizado. El obstáculo que queda es la competición entre
exponente de propagación y cero del perfil en la frontera, no un
encoder nuevo.

## 6. Aplicación de la aclaración

La frase de §3.1 del informe de ejecución se sustituyó, en el acto de
congelación, por la formulación de §4. Sha256 del informe **antes**:
`33691df63d2f5449af435bf2436b52bd03e39160db751bd2814ac1d898578e90`.
Sha256 **después**:
`2da09280b1e35078f05ee4b9bd1bbd650f0d93143acf797fb76fc52af856b094`.
El veredicto no cambia.
