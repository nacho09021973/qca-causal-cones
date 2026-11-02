<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 f4e7507593434bad19f5c709fd2c5e15578bc25472a48e33a47138a6c26d540e
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-02T08:34:19Z  fin: 2026-11-02T08:42:00Z
documento: /home/adnac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--hex-ceiling-review.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada b6daf1a7ad96c09eba521a63383a8015256bd9a6181fe056a90a981cc5bf4460
documento: /home/adnac/qca-causal-cones/debates/2026-11-02--hex-ceiling-rereview/repair.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 73fc9964e29b57f42ec9aa377cb5b73130fe73fcc368970a58fd6ae277e775fa
documento: /home/adnac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/adnac/qca-causal-cones/scripts/verify_hex_ceiling_gate.py ; último commit observado: bb4fcdb ; sha256 de la copia enviada 8f3b7a10ecee91c515429640b794da91e2c0e273176f5bbbd62e56a0f3b43d72
documento: /home/adnac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
entrada_grok.txt sha256 474062a1d9ba3c2146bd149993ed5810c95245226c70e5055d2ce49e314aaef0
respuesta sha256 ce21f2776ed953d1f9b19131d73f9fb5a4c75d1e49af268a787c49d0316d6bd7
-->

**Dictamen global: PASS.** No hay reparaciones obligatorias.

## R1 — Lema B: PASS

La prueba cierra y L0 queda `PROVED_IN_REPO` según la sec. 2 del contrato: la desigualdad escalar queda escrita en el informe, y el paso de malla ya aceptado no se toca.

La reducción es correcta. Con \(e^{i\alpha}p'(s_0)=|p'(s_0)|\) real y no negativo, \(R=\mathrm{Re}(e^{i\alpha}p)\) es trigonométrico real de grado \(\le N\), \(|R|\le 1\) y \(R'(s_0)=|p'(s_0)|\). Basta la cota unilateral \(R'\le N\).

La perturbación también. Si \(R'(s_0)>N\), hay \(0<\varepsilon<1\) con \(R_\varepsilon=(1-\varepsilon)R\) y \(R_\varepsilon'(s_0)>N\). Entonces \(|R_\varepsilon|\le 1-\varepsilon<1\). Como \(|R_\varepsilon(s_0)|<1\), existe un único \(\beta\in(-\pi,0)\) con \(\cos\beta=R_\varepsilon(s_0)\): el coseno es biyectivo de \((-\pi,0)\) en \((-1,1)\). Con \(C(s)=\cos(N(s-s_0)+\beta)\),
\[
C'(s_0)=-N\sin\beta\in(0,N],
\]
porque \(\sin\beta\in[-1,0)\). Así \(D=C-R_\varepsilon\) cumple \(D(s_0)=0\) y \(D'(s_0)=C'(s_0)-R_\varepsilon'(s_0)<0\), luego \(D\not\equiv 0\).

El recuento da \(2N+2\) ceros distintos. En un periodo, \(C\) vale \(\pm 1\) en \(2N\) puntos, alternando. Ahí \(|R_\varepsilon|<1\), así que \(\mathrm{sign}\,D(t_j)=\mathrm{sign}\,C(t_j)\neq 0\). Hay al menos un cero en cada uno de los \(2N\) arcos abiertos. El punto \(s_0\) cae en un arco \((t_j,t_{j+1})\) donde \(C\) es estrictamente monótona; \(C'(s_0)>0\) lo hace creciente, de modo que \(C(t_j)=-1\), \(C(t_{j+1})=+1\) y \(D(t_j)<0<D(t_{j+1})\). Como \(D'(s_0)<0\), \(D>0\) a la izquierda inmediata de \(s_0\) y \(D<0\) a la derecha. Hay un cero en \((t_j,s_0)\), el cero \(s_0\) y otro en \((s_0,t_{j+1})\), tres puntos distintos. Ese arco aporta dos ceros además del que ya contaba el cambio de signo: \((2N-1)+3=2N+2\).

La cota superior encaja. \(e^{iNs}D(s)\) es polinomio algebraico de grado \(\le 2N\) en \(z=e^{is}\). Un \(D\not\equiv 0\) tiene como máximo \(2N\) ceros por periodo. Contradicción, luego \(R'(s_0)\le N\).

El caso simétrico cierra la otra banda. Para \(S(s)=R(-s)\) se tiene \(S'(-s_0)=-R'(s_0)\le N\), es decir \(R'(s_0)\ge -N\). En L0 solo hace falta el lado positivo, que es el que da \(|p'(s_0)|\).

Con el paso de malla ya aceptado, \(|p'(0)|\le N\) da \(\|A(n_f)\|\le h_C(n_f)=r_{in}\). La sec. 2 pide esa consecuencia demostrada en el repositorio o citada con página; el Lema B es la primera vía, y la sec. 6 sigue sin reclamar novedad.

## R2 — Rango: PASS

El `record` nuevo afirma exactamente que el menor \(2\times 2\) de las dos primeras columnas vale \(\sqrt3\,\ell^4/2\), y esa identidad certifica rango 2 para todo \(\theta_0\).

Con \(a_j=\ell(\cos(\theta_0+2\pi j/3),\sin(\theta_0+2\pi j/3))\) y \(\varphi_{12}=2\theta_0+2\pi/3\), \(\varphi_{13}=2\theta_0+4\pi/3\), \(\varphi_{23}=2\theta_0\), la parte sin traza de \(M\) contribuye, por cada par,
\[
\ell^2 g\,(\cos\varphi,\sin\varphi).
\]
El menor de las columnas \((g_{12},g_{13})\) es \(\ell^4\sin(\varphi_{13}-\varphi_{12})=\ell^4\sin(2\pi/3)=\sqrt3\,\ell^4/2\). No depende de \(\theta_0\) y, con \(\ell>0\), no se anula. La matriz es \(2\times 3\), así que un menor \(2\times 2\) no nulo fija el rango en 2 para todo \(\theta_0\). El núcleo \((1,1,1)\) sigue comprobado por el producto `jac*(1,1,1)`.

Los otros dos menores son \(\ell^4\sin(-4\pi/3)=\sqrt3\,\ell^4/2\) y \(\ell^4\sin(-2\pi/3)=-\sqrt3\,\ell^4/2\). La frase del informe, «menores \(\pm\sqrt3\,\ell^4/2\)», coincide con esas tres evaluaciones. El verificador registra uno, y con ese basta para el rango. No ejecuté el script; la identidad está hecha a mano sobre el mismo menor que calcula `jac[:, :2].det()`.

## R3 — Aclaraciones: PASS

Hermiticidad. Tras quitar la fase global, \(U(0)=I\). Derivar \(UU^\dagger=I\) en \(t=0\) da \(U'+(U')^\dagger=0\). Con \(A=iU'\), \(A^\dagger=A\). En \(s=2\), con cono sin traza e isótropo, \(A(n_f)^2=c_0^2 I\) y traza nula: el espectro es \(\{+c_0,-c_0\}\) y \(\|A(n_f)\|=c_0\).

Módulo máximo. En \(|z|=1\), \(|P|=|p|\le 1\). \(P\) es polinomio (\(z^N e^{-ims}=z^{N-m}\), exponentes de \(0\) a \(2N\)), luego \(|P|\le 1\) en el disco cerrado.

Denominador \(2l\). En la subclase T1, \(F\subset\{0,\pm 2a_j\}\). El hexágono regular obliga a los seis vértices en \(F\), así que el paso más largo es \(2l\) y \(r_{in}=\sqrt3/2\). El cociente queda \(\sqrt{1-g}/\sqrt2\le\sqrt3/2\), con igualdad en \(g=-1/2\), realizado con los seis vértices presentes.

\(\xi\). En el testigo ADMP los tres vectores de Bloch tienen tercera coordenada \(\xi=\sqrt5/3\). Con las partes \(xy\) a \(120^\circ\), el solape es \(-2/9+5/9=1/3\). Esa componente común los saca de un plano lineal por el origen y sube \(g\) de \(-1/2\) a \(1/3\).

## R4 — Regresiones: PASS

El diff no mete un error ni una afirmación fuera del contrato. El Lema B permanece como argumento clásico, sin reclamo de novedad. T1 conserva el supremo \(\sqrt3/2\), alcanzado, y el veredicto `GAP_PROVED_IN_CLASS`. T2 no cambia de alcance: el módulo máximo solo nombra el paso que ya daba \(|P|\le 1\) en el disco; Julia sigue citada como clásica con página sin verificar, como antes. El estado sigue en `PRELIMINARY` y sin promoción. El `record` sustituye al anterior; no añadí ni quité comprobaciones, y no confirmo el recuento de checks.

**Reparaciones obligatorias: ninguna.**
