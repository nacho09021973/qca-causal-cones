<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 16568209771dc898346bd4af0c78ec10530c3b9e; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 91bee96b008d707188487ad26871460296ba02cf99300ae272afd81dce1d64e6; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=enabled, reasoning_effort=high, max_tokens=65536, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 41f9145fc4fd3303eace77f33f8fe6b337acd574d569adb80b336c21aa00828b
inicio: 2026-10-28T08:11:42Z  fin: 2026-10-28T08:39:03Z
documento: /home/ignac/qca-causal-cones/reports/2026-10-27--eon-projected-gaussian-reference.md ; último commit observado: sin versionar ; sha256 de la copia enviada ce267c5bc800e8c4c2b7ca38a37d435ed9d9bfa059aa57f85375276b6a5c2c7f
documento: /home/ignac/qca-causal-cones/theory/A_INT_EON_PROJECTED_GAUSSIAN_REFERENCE.md ; último commit observado: sin versionar ; sha256 de la copia enviada 8dcc2f30a5796edbdf20ecd832ebd969de7c2245e37267e7351372a7be93ecd0
documento: /home/ignac/qca-causal-cones/scripts/verify_eon_projected_gaussian_reference.py ; último commit observado: sin versionar ; sha256 de la copia enviada a12951dcfa7e61c0b5d5a13c9ef27c0ddac303b563e9af8b88bd74a2496274eb
documento: /home/ignac/qca-causal-cones/scripts/verify_eon_reference_state.py ; último commit observado: sin versionar ; sha256 de la copia enviada 4d7f708536af90cfa8a341e8935dfa292302a84edd0bd56c99d2b563f3182d50
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
documento: /home/ignac/qca-causal-cones/biblioteca/arXiv-2205.03148v4.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada c366b8a8482a762c93e534e43d6572323737df4677556b1a764e02a1389d2d02
documento: /home/ignac/qca-causal-cones/reports/2026-10-27--eon-projected-gaussian-certificate.json ; último commit observado: sin versionar ; sha256 de la copia enviada ff98a6420274e715521fd2f5fc4e8c304da71422745ea4f49d5718f80c195fcf
entrada_deepseek.txt sha256 1acbf8f3d0ea883fa8db0c59227b2b4673e55c1de01bb15ced9c9980cf4fe012
respuesta sha256 241523e71116da45b27653cf4ca24f53fb9e912adf28f5eaf733d9bb9187d39e
-->

## Veredicto global

**ACCEPT_WITH_REPAIRS**

No he encontrado un error fatal demostrado que invalide la construcción del estado proyectado ni la conclusión global del informe: el estado es no nulo, normalizable y con energía eléctrica esperada finita; la obstrucción de estacionariedad para colas gaussianas es esencialmente correcta. Sin embargo, la prueba de Fourier/Jensen tal como está escrita contiene un error de signo en la igualdad de autoestado, y varios pasos importantes están solo esbozados y deben formalizarse.

---

## 1. Separación de bloques

### 1.1 Construcción del candidato

La construcción

\[
|\Omega_\beta\rangle = Z^{-1/2} P_G \big(|FS_D\rangle \otimes \bigotimes_\ell |g_\beta\rangle\big)
\]

está bien definida en volumen finito y con rotores enteros sin truncar.

Puntos que son correctos:

- \(|g_\beta\rangle\) está normalizado exactamente para \(\beta>0\).
- \(P_G\) es un proyector ortogonal, de modo que \(Z=\|P_G(\cdots)\|^2\le 1\).
- \(Z>0\): basta que exista una configuración fermiónica con amplitud de Slater no nula y una solución entera de Gauss. La neutralidad total se cumple porque \(|FS_D\rangle\) tiene \(N=2V\) fermiones, y en un toro conexo la ecuación
  \[
  \operatorname{div} E = 2-N_x
  \]
  tiene solución entera si la carga total es nula. El algoritmo de árbol es una prueba existencial válida.
- La energía eléctrica esperada es finita porque las sumas
  \[
  \sum_{E\in\mathbb Z^M} \Big(\sum_\ell E_\ell^2\Big) e^{-2\beta \sum_\ell E_\ell^2}
  \]
  convergen para \(\beta>0\), y restringir a un subretículo de Gauss no empeora la convergencia.
- El criterio auxiliar \(h_D(k)=m\gamma_0-\sum_a \sin(k_a)\gamma_a\) es solo una preparación auxiliar. El informe no lo presenta como energía conservada de \(U\), lo cual es correcto.

No hay objeción de fondo en este bloque.

---

### 1.2 Hipótesis de modelo y alcance

El alcance declarado es:

- volumen finito \(L\ge 3\);
- rotores enteros no truncados;
- magnetismo exponencial exacto, no la implementación aproximada QW-like \(D_M^{(1)}\);
- ángulo magnético real no nulo;
- colas eléctricas gaussianas;
- no se extiende a límite termodinámico, continuo, velocidades radiativas ni a todos los vacíos.

Esto es correcto y no hay extrapolación indebida evidente. La prueba no pretende ser un no-go de todos los autoestados de \(U\).

---

## 2. Objeciones a la prueba de obstrucción

### G-R1-01 — Error de signo en la igualdad de autoestado en Fourier

**Gravedad:** moderada.  
**Tipo:** error demostrado, reparable.  
**Localización:** informe, sección 3.C, donde se escribe

\[
g(z)=\exp[i\theta(a z+b/z+c)]f(z)
\]

y luego se elige un arco con \(\mathrm{Re}(i\theta a z)\ge |\theta a|r/2\).

**Problema:**

Si \(D_M\) multiplica en Fourier por

\[
e^{i\theta B(z)},
\]

y si

\[
\varphi = D_E D_F \psi,
\]

con transformada de Fourier \(g\), entonces la condición \(U\psi=\lambda\psi\), es decir

\[
D_M\varphi=\lambda\psi,
\]

se traduce en

\[
e^{i\theta B(z)} g(z) = \lambda f(z).
\]

Por tanto

\[
f(z)=\lambda^{-1} e^{i\theta B(z)} g(z),
\]

o equivalentemente

\[
g(z)=\lambda e^{-i\theta B(z)} f(z).
\]

La igualdad escrita en el informe tiene el signo de \(\theta\) invertido y absorbe \(\lambda\) de forma ambigua.

Con la relación correcta, para obtener una cota superior de \(f\) a partir de la cota de \(g\), debe elegirse el arco donde

\[
\mathrm{Re}(i\theta a z)\le -|\theta a|r/2,
\]

no \(\ge\). O bien se reemplaza consistentemente \(\theta\) por \(-\theta\) en toda la prueba.

**Reparación:**

Corregir la igualdad de autoestado a

\[
f(z)=\lambda^{-1}e^{i\theta B(z)}g(z)
\]

y elegir el arco donde la exponencial magnética es pequeña:

\[
\mathrm{Re}(i\theta a z)\le -\frac{|\theta a|r}{2}.
\]

La medida angular de ese arco sigue siendo \(1/3\) del círculo. La conclusión de contradicción con Jensen/convexidad se mantiene sin cambios sustanciales.

---

### G-R1-02 — El paso Jensen/convexidad está subenunciado

**Gravedad:** moderada.  
**Tipo:** paso justificable pero omitido.  
**Localización:** informe, sección 3.C.

**Observación:**

El informe afirma:

> “Para una función holomorfa no nula en un anillo exterior, la media angular de \(\log|f|\) es convexa en \(\log r\) … En particular tiene una cota inferior afín.”

La afirmación es esencialmente correcta, pero debe formularse con precisión porque se trata del corazón de la contradicción.

**Reparación sugerida:**

Sea \(f\) holomorfa y no idénticamente nula en \(\{R_0<|z|<\infty\}\). Para \(r>R_0\),

\[
I_f(r)=\frac1{2\pi}\int_0^{2\pi}\log|f(re^{i\theta})|\,d\theta
\]

es finita salvo posiblemente en valores aislados de \(r\) donde hay ceros sobre la circunferencia, y la singularidad logarítmica es integrable en \(\theta\).

Como \(\log|f|\) es subarmónica en el anillo, la media circular \(I_f(r)\) es convexa en \(t=\log r\). Una forma de justificarlo es usar que para subarmónicas \(u\),

\[
\frac{d}{d\log r}\left(r\frac{dI_u}{dr}\right)
=
\frac{1}{2\pi}\int \Delta u\,dA
\]

en el sentido distribucional; como \(\Delta u\ge 0\), la derivada es no decreciente.

Por convexidad en \(t\), para cualquier \(t_0\) existe un subgradiente finito y por tanto constantes \(A,B\) reales tales que

\[
I_f(r)\ge A+B\log r.
\]

Esto es lo que necesita la prueba. No hace falta que \(f\) sea libre de ceros; los ceros no invalidan el argumento porque contribuyen con singularidades logarítmicas integrables y no rompen la subarmonicidad.

**Veredicto de la objeción:** omisión justificable, no error.

---

### G-R1-03 — Preservación de cota gaussiana por \(D_F\) y \(D_E\) solo está esbozada

**Gravedad:** baja–moderada.  
**Tipo:** paso justificable pero omitido.  
**Localización:** informe, sección 3.A.

**Observación:**

El informe dice que \(D_F\) consta de un número finito de gates, que los transportes desplazan \(E\) en una cantidad acotada y que una combinación finita de gaussianas desplazadas sigue acotada por otra gaussiana. La idea es correcta, pero conviene formalizarla para que quede claro que no hay una dependencia peligrosa en \(E\).

**Reparación sugerida:**

En la base de ocupaciones fermiónicas y campos eléctricos \(\{|n,E\rangle\}\):

- Los gates fermiónicos locales de masa y cambio de base no desplazan \(E\) y mezclan finitamente componentes \(n\).
- Los gates de transporte desplazan un enlace por \(0,\pm1\) y multiplican por fases dependientes de paridades \(E\), es decir, fases de módulo \(1\).
- Por tanto, para cada componente fermiónica final \(n'\), el coeficiente de \(\varphi=D_F\psi\) cumple

\[
|\varphi_{n'}(E')|
\le
\sum_{\delta\in S}\sum_n C
|\psi_n(E'+\delta)|,
\]

donde \(S\) es un conjunto finito de vectores de desplazamiento, porque el volumen es finito.

Si

\[
|\psi_n(E)|\le C_\psi e^{-\beta\sum_\ell E_\ell^2},
\]

entonces para cada desplazamiento finito \(\delta\) y cada \(0<\beta'<\beta\),

\[
e^{-\beta\|E+\delta\|^2}
\le
C_{\delta,\beta'}\, e^{-\beta'\|E\|^2}.
\]

Como \(S\) es finito, \(\varphi\) satisface una cota gaussiana con exponente \(\beta'>0\). \(D_E\) solo multiplica por fases \(e^{i\alpha\sum E_\ell^2}\), así que no cambia los módulos.

Este desarrollo debe escribirse explícitamente.

---

### G-R1-04 — Diagonalización simultánea de los \(V\) y fases JW no está formalizada

**Gravedad:** moderada.  
**Tipo:** paso justificable pero omitido.  
**Localización:** informe, secciones 2 y 3.B.

**Observación:**

El informe afirma que los \(V_\ell\) son unitarios, conmutan y que en la base de Fourier eléctrico \(D_M\) se convierte en multiplicación por

\[
\exp[i\theta B(z_1,\dots,z_M)].
\]

Esto es correcto, pero está demasiado comprimido. Las fases JW de los \(V_\ell\) podrían inducir fases no triviales en la transformada.

**Reparación sugerida:**

Dado que los \(V_\ell\) conmutan y son unitarios, existe una equivalencia unitaria con los desplazamientos estándar en \(\ell^2(\mathbb Z^M)\). Las fases JW provenientes de cadenas de \(Z\) son fases diagonales en la base eléctrica; pueden absorberse con una unitaria diagonal \(W=\operatorname{diag}(e^{i\chi(E)})\). En esa realización, \(V_\ell\) actúa como multiplicación por \(z_\ell\).

Como \(B\) es una suma de monomios de \(V_\ell\), la exponencial magnética exacta actúa como

\[
e^{i\theta B(z)}
\]

en la representación espectral. Además, los coeficientes espectrales son los coeficientes eléctricos multiplicados por una fase \(e^{-i\chi(E)}\), por lo que las cotas gaussianas sobre módulos se transfieren sin problema.

Este paso no rompe la acción de \(U\), porque no se está cambiando el circuito; solo se está usando una representación unitaria equivalente.

---

### G-R1-05 — Elección simultánea de componente no nula y \(a\neq 0\)

**Gravedad:** baja.  
**Tipo:** omisión menor.  
**Localización:** informe, sección 3.B–3.C.

**Observación:**

El informe dice que puede elegirse una componente no nula de \(\varphi\) y a la vez un enlace con \(a\neq 0\). La idea es correcta, pero está condensada.

**Reparación sugerida:**

Puesto que \(f\) no es idénticamente nula, su transformada espectral es una función holomorfa no nula en \((C^*)^M\). El conjunto de ceros de una función holomorfa no idénticamente nula en un dominio conexo tiene interior vacío. Análogamente, \(a(z_{\neq e})\) es un polinomio de Laurent no idénticamente nulo, así que su conjunto de ceros es propio.

Por tanto, pueden fijarse genéricamente las otras variables \(z_{\neq e}\) fuera de ambos conjuntos de ceros. En ese punto:

- la restricción a la variable \(z_e\) no es idénticamente nula;
- \(a\neq 0\).

Esto es exactamente lo que la prueba necesita.

---

### G-R1-06 — Control “inverse-kick” y convención de signo

**Gravedad:** baja.  
**Tipo:** inconsistencia menor.  
**Localización:** informe, sección 3.D.

**Observación:**

El control

\[
f=e^{-i\theta(z+1/z)},\qquad g=1
\]

ilustra correctamente por qué la clase de crecimiento gaussiano es esencial. Sin embargo, según la relación corregida \(f=\lambda^{-1}e^{i\theta B}g\), el signo de este control debe ajustarse a la convención usada.

No es un error sustancial, porque se trata de un ejemplo fuera de la clase gaussiana, no de un autoestado del QCA.

---

## 3. Qué verifican realmente los scripts

No ejecuté los scripts, y no afirmo haberlo hecho.

De la lectura del código y del JSON:

- `verify_eon_projected_gaussian_reference.py` verifica ingredientes algebraicos:
  - proyector de Dirac auxiliar, rango y espectro;
  - soluciones enteras de Gauss para configuraciones de prueba en \(L=3,4\);
  - control de cola para un bucle infinito simplificado;
  - recuento de armónicos magnéticos \(z\) e \(1/z\);
  - término dominante de Laurent finito;
  - identidad “inverse-kick” fuera de la clase gaussiana.

- No verifica:
  - la preservación gaussiana completa bajo \(D_F\) para el estado proyectado real;
  - la diagonalización espectral simultánea de \(V\) con fases JW;
  - el teorema de Jensen/convexidad;
  - la conclusión global de no estacionariedad para el candidato completo.

Los `PASS` de esos scripts no convierten la prueba analítica en una revisión independiente. El informe lo declara correctamente.

---

## 4. Conclusión

### Construcción

**ACCEPT.**  
El candidato proyectado es explícito, no nulo, normalizable, con Gauss exacta y energía eléctrica esperada finita. El criterio de preparación auxiliar está correctamente declarado como no físico fundamental.

### Hipótesis de modelo y alcance

**ACCEPT.**  
No hay extrapolación indebida a otros vacíos, al límite continuo, al límite termodinámico ni a velocidades radiativas.

### Prueba de obstrucción

**ACCEPT_WITH_REPAIRS.**

La obstrucción de Fourier/Jensen es estructuralmente correcta, pero debe repararse:

- corregir el signo de la igualdad de autoestado y la elección del arco;
- formalizar el paso Jensen/convexidad con enunciado preciso;
- explicitar la preservación gaussiana bajo \(D_F,D_E\);
- escribir la diagonalización simultánea de \(V\) con fases JW;
- detallar la elección genérica de componente no nula y \(a\neq 0\).

No hay error fatal demostrado. El error de signo, aunque real, es reparable sin cambiar la conclusión.
