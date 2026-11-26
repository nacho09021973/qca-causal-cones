<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-26T12:07:54Z  fin: 2026-11-26T12:12:38Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-amendment2-astra/amendment2.diff ; último commit observado: sin versionar ; sha256 de la copia enviada e1363940f474ef8cc07d07ea364885613a34c4a1d70776754c2ea0b932fd5030
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transfer-matrix-audit.md ; último commit observado: b1c6d75 ; sha256 de la copia enviada f343b25ba654931811198307deee3846f0289cf2d3a1bd507faeacd6da456e72
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-amendment1-grok/informe_grok.md ; último commit observado: b1c6d75 ; sha256 de la copia enviada 4e72f4846ff6ef7a80f07651fa41b83276ef0f5b2a22da4d7e0897dbb434629d
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_amendment2.py ; último commit observado: b1c6d75 ; sha256 de la copia enviada b6c68dc431aba0b21425b1e24a3329ffbe560e673250261c234e064d0dcff243
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_repairs.py ; último commit observado: 63db34b ; sha256 de la copia enviada 5a315b68b7f48ded51290408a256e2c7485e8edb22a8b0299fbcfc750c99b0e8
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_matrix.py ; último commit observado: d0114b2 ; sha256 de la copia enviada 98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2
entrada_astra.txt sha256 4a767cdf6cb92e4aa42be9d2155bbf72e0428629e1b60aedd230147dfcb9d7e7
respuesta sha256 748185c2289586d5ad64e6f43f6513f5b916e713a085da261f227a7c3e5eed08
-->

**Veredicto global: REPAIR_REQUIRED.** Las multiplicidades y el coeficiente cúbico son correctos. También pueden cerrarse a mano los dos puntos pendientes: la partición es **3+1** y el borde interior es **cuadrático, con un bloque de Jordan de tamaño 2**.

La reparación necesaria afecta a una afirmación literal falsa sobre las raíces en \([0,1]\) y a la delimitación de lo certificado por G4. No encuentro un fallo de la matriz dentro del alcance solicitado.

Todo lo siguiente procede de derivación manual e inspección del material adjunto. **La ejecución de los verificadores y la identidad histórica de sus bytes quedan UNVERIFIED.** Uso la correspondencia de Bloch y la identidad característica suministradas, sin reabrir las 144 entradas.

| Punto | Veredicto |
|---|---|
| 1. Gemelo \((-1,-1)\) en el horizonte | **PASS** |
| 2. Semisimplicidad en los extremos | **PASS** |
| 3. Coeficiente cúbico y G3 | **PASS**, con el alcance analítico precisado abajo |
| 4. Ecuación del borde, raíces y extremos | **REPAIR_REQUIRED** |
| 5(a). Jordan \(3+1\) frente a \(2+2\) | **PASS**, demostrado aquí |
| 5(b). Curvatura y defecto del borde interior | **PASS**, demostrado aquí |
| 6. Verificador nuevo | **REPAIR_REQUIRED** en documentación y alcance; aserciones correctas por inspección |
| 7. Alcance y atribución | **REPAIR_REQUIRED** |

**1–3. Expansión, gemelo y extremos.**

En el horizonte,
\[
A=-\frac3{32},\qquad
f(k)=A\cos3k+(1-A)\cos k
=1-\frac{k^2}{8}-\frac{13}{48}k^4+O(k^6).
\]
Para la rama con pendiente positiva, escribimos
\[
E(k)=\frac{k}{2}+\beta k^3+O(k^5).
\]
Entonces
\[
\cos E
=1-\frac{k^2}{8}
+\left(\frac1{384}-\frac{\beta}{2}\right)k^4+O(k^6),
\]
y resulta
\[
\beta=\frac{35}{64},\qquad
\Omega_+=\frac{35}{32}k^3+O(k^5),\qquad
\Omega_-=-2k-\frac{35}{32}k^3+O(k^5).
\]

La existencia de esa rama analítica impar se justifica, por ejemplo, mediante
\[
E(k)=2\arcsin\!\left(
k\sqrt{\frac{1-f(k)}{2k^2}}
\right).
\]
El cociente tiene prolongación analítica positiva en cero. La fórmula corresponde a \(k\to0^+\) o a esta continuación impar; el \(\arccos\) principal bilateral tiene pendiente de signo opuesto a cada lado.

**G3 comprueba correctamente la serie de \(f\), la cancelación cuadrática y la ecuación que determina \(\beta\).** La elección y existencia de la rama, así como la deducción del resto \(O(k^5)\), requieren el argumento analítico anterior. No son una ejecución de inversión de series por G3.

Para el gemelo, poniendo \(k=\pi+q\),
\[
f(\pi+q)=-f(q).
\]
Podemos elegir la continuación \(E_\pi(q)=\pi+E(q)\). Módulo \(2\pi\),
\[
\Omega_+(\pi+q)=\pi+\frac{35}{32}q^3+O(q^5),
\]
\[
\Omega_-(\pi+q)=\pi-2q-\frac{35}{32}q^3+O(q^5).
\]
Por tanto,
\[
\det(-I-U(\pi+q))
=\frac{35}{16}q^4+O(q^5).
\]
El orden es exactamente cuatro. Como
\[
\lambda=-e^{-iq},\qquad
\lambda+1=iq+O(q^2),
\]
el cambio de coordenada conserva ese orden. Los factores \(\lambda^5\) y \(-zA^2\) de la identidad característica no se anulan: la multiplicidad algebraica es **4**.

La simetría operatorial confirma independientemente el gemelo:
\[
W(k+\pi)=-W(k),\qquad U(k+\pi)=-U(k).
\]

Para la multiplicidad geométrica,
\[
S(\pi)=-I,\qquad
W(\pi)=-C(\theta)^2C(-2\theta)=-I,\qquad U(\pi)=-I.
\]
Cada espinor \(v\in\mathbb C^2\) genera las etapas
\[
q_{j+1}=-C(\beta_j)q_j,\qquad q_1=v.
\]
El vector de transferencia correcto es
\[
Y=(a_1,\ldots,a_6,b_1/\lambda,\ldots,b_6/\lambda).
\]
Para \(\lambda=-1\), su mitad inferior es \((-b_1,\ldots,-b_6)\).

Los espinores \(e_1,e_2\) producen vectores independientes: en las coordenadas \(a_1,b_1/\lambda\), el menor es \(\operatorname{diag}(1,-1)\). Además, todo vector propio queda determinado por \(q_1\), mediante las etapas de Bloch. La dimensión no puede exceder dos. Así, la multiplicidad geométrica es **2**.

En los extremos, sea \(a=4t-1>0\). Las pendientes locales son
\[
\Omega_+'(0)=-1+2a=8t-3,\qquad
\Omega_-'(0)=-1-2a=1-8t.
\]

| \(t\) | \(\Omega_+'(0)\) | \(\Omega_-'(0)\) |
|---|---:|---:|
| \(5/16\) | \(-1/2\) | \(-3/2\) |
| \(7/16\) | \(1/2\) | \(-5/2\) |

Ambas bandas tienen contacto de orden uno. La multiplicidad algebraica es dos, tanto en \((1,1)\) como en \((-1,-1)\). El argumento de los dos espinores sigue siendo válido: la geométrica también es dos. **Son raíces semisimples y esos puntos no son bordes de banda.**

**4. Ecuación del borde y recuento de raíces.**

En \(0<k<\pi/2\),
\[
g'(C)=12AC^2+1-4A\ge 1+8A=(4t-1)^2>0.
\]
Además, \(0<g(C)<1\), de modo que \(0<E<\pi/2\). Por ello
\[
E'=\frac{\sin k\,g'(C)}{\sin E}>0.
\]
La ecuación \(v_+=-1+2E'=0\) equivale a
\[
2\sin k\,g'(C)=\sin E.
\]
**Ambos miembros son positivos**, por lo que elevar al cuadrado es reversible en ese intervalo:
\[
P_t(u):=4(1-u)g'(C)^2-\bigl(1-g(C)^2\bigr)=0.
\]

La expansión algebraica da, con \(w=u-1\),
\[
P_{5/16}(u)
=\frac3{1024}(1-u)(2625w^2+5w-16),
\]
\[
P_{3/8}(u)
=\frac{105}{64}(u-1)^2(4-3u),
\]
\[
P_{7/16}(u)
=\frac5{1024}(1-u)(343w^2-525w+144).
\]

De aquí:

- En \(t=5/16\), el discriminante es \(168025\). Las raíces del cuadrático son
  \[
  w_\pm=\frac{-5\pm\sqrt{168025}}{5250}.
  \]
  Hay exactamente una en \((-1,0)\) y otra positiva. El único punto interior queda determinado por
  \[
  u_*=\frac{5245-\sqrt{168025}}{5250},\qquad
  k_*=\arccos\sqrt{u_*}.
  \]
- En \(t=3/8\), \(u=1\) tiene multiplicidad exactamente dos y la otra raíz es \(4/3\). No hay raíces en \((0,1)\).
- En \(t=7/16\), el cuadrático es estrictamente positivo para \(w\in[-1,0]\): sus tres términos son no negativos y el término constante es positivo. **El cociente no tiene raíces en \([0,1]\), pero \(P_{7/16}\) sí tiene la raíz \(u=1\).**

Esta última distinción exige reparación. El texto de la auditoría y la cabecera del verificador dicen «no root in \([0,1]\)» sin identificar el cociente. Tomado como afirmación sobre el polinomio resultante de la ecuación, es falso.

En realidad, **\(P_t(1)=0\) para todo \(t\)**. En \(k=0\), la ecuación cuadrada se reduce a \(0=0\); allí no puede usarse la equivalencia demostrada solo en el intervalo abierto. La ausencia de velocidad nula en ese extremo se comprueba mediante las pendientes anteriores.

El recuento de Sturm también concuerda. Para el cuadrático de \(t=5/16\), en variable \(u\),
\[
T(u)=2625u^2-5245u+2604.
\]
Su sucesión de Sturm puede tomarse como
\[
T,\quad 5250u-5245,\quad \frac{168025}{10500}.
\]
En cero los signos son \(+,-,+\), con dos variaciones; en uno son \(-,+,+\), con una. Hay exactamente una raíz interior.

`roots_in_open_unit` es correcto con la semántica de `Poly.count_roots`: cuenta raíces reales **distintas**, incluidos los extremos finitos, y luego resta cada extremo que sea raíz. Para los usos presentes:

| Polinomio pasado a la función | Raíces distintas en \([0,1]\) | Extremos restados | Resultado |
|---|---:|---:|---:|
| `Q516` | 1 | 0 | 1 |
| `P38` | 1 | 1 | 0 |

La raíz doble \(u=1\) de `P38` se cuenta una vez y se resta una vez. No hay error de multiplicidad en esa resta. No he comprobado una instalación concreta de SymPy.

**5(a). La partición de Jordan es \(3+1\).**

Los órdenes del determinante, por sí solos, no bastan para identificar una partición de Jordan. Aquí puede construirse una cadena.

Cerca de \(k=0\), \(W(0)=I\) y sus autovalores son
\[
e^{\pm iE(k)},\qquad E'(0)=\frac12.
\]
La matriz analítica
\[
\frac{W(k)-I}{k}
\]
se prolonga a cero y tiene allí autovalores distintos \(\pm i/2\). Por tanto, pueden elegirse autovectores analíticos no nulos para ambas ramas. Lo mismo vale cerca de \(\pi\), por la simetría anterior.

Sea \(Y(h)\) el vector de Bloch analítico de la rama cúbica, usando
\[
h=\lambda-\lambda_0,\qquad
(z_0,\lambda_0)=(1,1)\ \text{o}\ (-1,-1).
\]
Entonces
\[
z(h)=z_0+O(h^3),\qquad
M(z(h))Y(h)=(\lambda_0+h)Y(h).
\]
Como \(M\) es analítica en \(z_0\ne0\), escribiendo
\[
Y(h)=Y_0+hY_1+h^2Y_2+O(h^3),\qquad
K=M(z_0)-\lambda_0I,
\]
la comparación de coeficientes da
\[
KY_0=0,\qquad KY_1=Y_0,\qquad KY_2=Y_1.
\]
Y \(Y_0\ne0\). Existe, pues, una cadena de longitud tres.

Con multiplicidad algebraica cuatro y geométrica dos, la única partición compatible es
\[
\boxed{3+1}.
\]
En particular,
\[
\dim\ker K=2,\qquad
\dim\ker K^2=3,\qquad
\dim\ker K^3=4.
\]

Esto cierra el punto mediante una derivación propia; no depende de aceptar la afirmación de Grok ni de ejecutar nulidades.

**5(b). El borde interior tiene \(\Omega''\ne0\) y geométrica uno.**

Escribamos \(v=\Omega_+'=2E'-1\). La identidad cuadrada puede expresarse como
\[
P_t(u(k))
=\sin^2E\,\bigl(4E'^2-1\bigr)
=\sin^2E\,v(v+2).
\]
En el punto \(k_*\) donde \(v=0\), derivar da
\[
P_t'(u_*)\,u'(k_*)
=2\sin^2E(k_*)\,\Omega_+''(k_*).
\]
Todos los factores necesarios son no nulos:

- \(u'(k_*)=-\sin2k_*\ne0\);
- \(\sin E(k_*)>0\);
- \(P_t'(u_*)\ne0\), porque la raíz del cuadrático es simple y \(u_*\ne1\).

Por tanto,
\[
\boxed{\Omega_+''(k_*)\ne0}.
\]
Además, en la raíz negativa \(w_-\),
\[
5250w_-+5=-\sqrt{168025}<0.
\]
Así, \(P_t'(u_*)<0\), mientras que \(u'(k_*)<0\); resulta \(\Omega_+''(k_*)>0\): es un mínimo.

La banda de \(U\) es simple allí. En efecto, \(0<E<\pi/2\) implica
\[
e^{2iE}\ne e^{-2iE}.
\]
Para \(z_*=e^{i\Omega_+(k_*)}\), el determinante tiene entonces un cero de orden exactamente dos en \(k\), y por tanto en \(\lambda\). El núcleo de moneda tiene dimensión uno; la correspondencia de Bloch conserva esa dimensión. La raíz de transferencia tiene:

\[
\boxed{\text{algebraica }2,\quad \text{geométrica }1,\quad \text{Jordan }2.}
\]

**6. Inspección del verificador.**

El recuento estático sí da **39 comprobaciones**:
\[
5\text{ de G1}+20\text{ de G2}+3\text{ de G3}+11\text{ de G4}=39.
\]

- **Multiplicidad algebraica.** El polinomio característico es mónico de grado doce, por lo que no es nulo y el bucle termina. Solo se divide cuando el resto se reconoce como cero. La comprobación final de no anulación del cociente distingue multiplicidad exacta de mera divisibilidad. Si una simplificación no reconoce un cero, la evaluación final mediante polinomio mínimo impide certificar una multiplicidad menor incorrecta.
- **Vectores en \(\lambda=-1\).** La construcción introduce correctamente tanto \(S(\pi)=-I\) en cada etapa como \(b_j/\lambda=-b_j\) en \(Y\). No falta ninguno de los dos signos.
- **Menor \(10\times10\).** Un menor no nulo da rango al menos diez. Los dos vectores propios independientes dan rango a lo sumo diez. Juntos prueban nulidad exactamente dos. Las comprobaciones previas abortan ante fallo, por lo que la conclusión final no descansa únicamente en el menor.
- **No anulación algebraica.** Para las expresiones algebraicas concretas usadas, el polinomio mínimo es \(X\) precisamente cuando el número es cero. No encuentro un falso positivo en este uso de `nonzero_alg`.
- **G4 y extremos.** La última aserción comprueba explícitamente el **cociente** `Q716`; es correcta. El error está en la descripción más amplia del resultado.
- **Orden exacto del factor en el horizonte.** G4 comprueba que \((u-1)^2\) divide `P38`, pero no comprueba expresamente que no divida \((u-1)^3\). La ausencia de raíces interiores no suple eso. Aquí el orden exacto queda demostrado por la factorización manual:
  \[
  Q38(1)=\frac{105}{64}\ne0.
  \]
  Si se quiere atribuir esa exactitud exclusivamente a G4, debe añadirse esa comprobación.
- **Importaciones.** Los módulos anteriores se ejecutan y sus excepciones no se capturan. Un fallo en ellos aborta antes de G1: no queda enmascarado. Sus mensajes de éxito previos no sustituyen el resultado final del proceso.
- **Resumen `n/n`.** No comprueba un número esperado de aserciones; en el código adjunto el recuento de 39 se obtiene inspeccionando sus llamadas y bucles.

No encuentro falsos positivos en las aserciones concretas inspeccionadas, bajo las operaciones algebraicas y el contrato de SymPy utilizados. **Sí hay conclusiones más amplias que las aserciones:** G3 necesita la justificación de rama; G4 necesita el argumento analítico para pasar de raíz simple a curvatura y estructura de Jordan.

**7. Alcance y atribución.**

G1, G2 y G3 reparan correctamente las atribuciones principales: el gemelo, la geométrica en los extremos y el coeficiente ya tienen comprobaciones específicas.

Persisten dos problemas de redacción:

- La introducción afirma globalmente que las reparaciones están certificadas por las 39 comprobaciones. Algunas son argumentos escritos, y la propia auditoría reconoce esa diferencia para la reversibilidad del cuadrado.
- Se llama al borde **«ordinary band extremum»** y se incluye entre lo validado, mientras se deja \(\Omega''\ne0\) como pendiente. La conclusión es verdadera, como demuestra el apartado anterior, pero su justificación debe incorporarse y atribuirse al argumento escrito.

La marca **UNVERIFIED** de la partición de Jordan es prudente: no presenta la afirmación de Grok como certificada. Puede cerrarse incorporando la construcción de cadena anterior. La coincidencia con Astra o Grok no aporta por sí misma prueba adicional.

Las objeciones, por gravedad, son:

1. **Media — §4, apartado interior, y cabecera de G4.** «En \(t=7/16\), no hay raíces en \([0,1]\)» es falso para \(P_t\), que siempre tiene \(u=1\). **Reparación:** escribir «el cociente \(P_t/(u-1)\) no tiene raíces en \([0,1]\); por tanto, no hay puntos de velocidad nula en \(0<k<\pi/2\)». Mantener separado el análisis del extremo.

2. **Media — §4, “ordinary band extremum”, introducción de A2 y lista “Validated”.** La atribución a G4 excede sus aserciones y convive con una curvatura marcada como pendiente. **Reparación:** incorporar
   \[
   P_t'(u_*)u'(k_*)=2\sin^2E(k_*)\Omega''(k_*),
   \]
   la simplicidad de la banda y la deducción de geométrica uno; atribuir a G4 la factorización y el recuento, y al argumento escrito la curvatura y el bloque de Jordan.

No identifico otras objeciones sustantivas dentro del alcance pedido.