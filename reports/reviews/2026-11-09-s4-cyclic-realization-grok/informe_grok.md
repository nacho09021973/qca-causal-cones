<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 89bcea0ef68be493f8e395850b598a7e47a0eeb8e6edf0bf44b1e8bb42e30e80
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-09T08:23:36Z  fin: 2026-11-09T08:44:18Z
documento: /home/ignac/qca-causal-cones/theory/S4_CYCLIC_REALIZATION_ATTEMPT.md ; último commit observado: 170910b ; sha256 de la copia enviada c065cb8c91c0945e09aa6267d5933f47ab8cc5069d696fb89818826fb1734330
documento: /home/ignac/qca-causal-cones/reports/2026-11-06--s4-cyclic-realization.md ; último commit observado: 170910b ; sha256 de la copia enviada 300471056b1cb71a5eb4145ab03fe2b6b6576ee742ed346d8ae74ac22def89a1
documento: /home/ignac/qca-causal-cones/scripts/verify_s4_cyclic_realization.py ; último commit observado: 170910b ; sha256 de la copia enviada 9a13907240311d26e8db7bc356b9826efd63f0a65190182404a819461ba19224
documento: /home/ignac/qca-causal-cones/reports/2026-11-06--s4-cyclic-realization-verifier.txt ; último commit observado: 170910b ; sha256 de la copia enviada a935056d0422653c225f32af58453e5119c0b1292eebfc34c345f11765d13e0d
entrada_grok.txt sha256 60c13b98fadf476f568d4c1537ea05faef000d9b6f7645aa2522e6595c5c8b7b
respuesta sha256 0d09a34037016d51ee6357f11b87566e9fe89b71dbf093455af0534e0572d79e
-->

**Veredicto: se sostiene.**

La realización, con el alcance que ella misma declara, es correcta. Lo que sigue está derivado a mano desde las definiciones; el recuento 143/143 no es la prueba. El registro solo se inspeccionó: sus etiquetas coinciden con las del script (el recuento de comprobaciones que el código encola es 143) y no se reejecutó nada. El PDF `1708.00826` no está adjunto: no confirmo qué dicen su Def. 1 y su Ec. (4).

## Derivaciones

**(1) W, soporte y unitariedad.** Sea \(m=n\cdot\tau\). Como \(|n|=1\), \(m^2=I_2\) y
\[
\exp(-i\pi m/4)=\cos(\pi/4)\,I-i\sin(\pi/4)\,m=(I_2-im)/\sqrt{2}.
\]
Por tanto el \(W\) del contrato es exactamente \((I_4-iN)/\sqrt{2}\) del informe. No hay un factor escondido: el script guarda \(W_{\mathrm{raw}}=\sqrt{2}\,W\) y por eso compara las convoluciones contra \(2I\), no contra \(I\).

\(G_i=\sigma_i\otimes\tau_i\) es hermítica e involutiva. Para \(i\neq j\), las dos constantes de estructura se multiplican: \(G_iG_j=G_jG_i=-G_k\). En particular conmutan, el orden \(xyz\) del producto es irrelevante y \(G_xG_yG_z=-I_4\). Los \(E_h=\prod_i(I+h_iG_i)/2\) son proyectores que conmutan. Su traza vale \((1-h_xh_yh_z)/2\): rango 1 si el producto de signos es \(-1\), y el proyector nulo si es \(+1\). Los cuatro no nulos son ortogonales y suman \(I_4\). Así
\[
U(k)=\sum_{h_xh_yh_z=-1}WE_h\exp(-ik\cdot h/\sqrt{3}),
\]
con soporte exactamente
\[
F=\{(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1)\}/\sqrt{3}.
\]
Unitaridad: \(U^\dagger U=\sum_h E_h=I\) para todo \(k\), y lo mismo para \(UU^\dagger\). Los 13 desplazamientos posibles entre vértices (el \(0\) y los 12 dirigidos de las aristas) agotan las \(4\times 4\) parejas; la convolución del script cubre esos 13 en los dos órdenes.

**(2) Simetrías.** \(R_j=\sigma_j\otimes I\) conmuta con \(W\) y cumple \(R_jG_iR_j=\varepsilon_{ji}G_i\), con \(\varepsilon_{jj}=+1\) y \(\varepsilon_{ji}=-1\) si \(i\neq j\). En los coeficientes cambia el signo de las componentes de \(h\) distintas de \(j\), y eso es el semigiro \((k_x,k_y,k_z)\mapsto\) esa misma inversión de signos. El conjunto \(F\) es estable.

\(V=\sigma_y\otimes\tau_y\) es real, simétrica y \(V^2=I\), así que \(C=VK\) cumple \(C^{-1}=C\) y \(C^2=+I\). Se comprueba \(VG_i^*V=G_i\) y \(VW^*V=W\), luego \(VA_h^*V=A_h\). Como la conjugación de la onda plana invierte \(k\),
\[
VU(k)^*V^\dagger=U(-k),
\]
que es \(CU(k)C^{-1}=U(-k)\). No es una identidad con adjuntos. Además \(VN^*V=-N\), así que \(C\) intercambia \(P\) y \(Q\).

\(t=(I-i(\sigma_x+\sigma_y+\sigma_z))/2=\exp(-i(2\pi/3)\,n\cdot\sigma/2)\) es la rotación de espín \(1/2\) de \(+120^\circ\) alrededor de \(n\): lleva \(e_x\to e_y\to e_z\to e_x\). Por tanto \(t\sigma_it^\dagger=\sigma_{i+1}\) y \(S=t\otimes t\) cicla \(G_i\) y \(R_i\) en el mismo sentido. Como \(n\) es el eje, \(SNS^\dagger=N\) y \(SWS^\dagger=W\). Los \(G_i\) conmutan, así que reordenar da exactamente
\[
SU(k_x,k_y,k_z)S^\dagger=U(k_z,k_x,k_y),
\]
no el ciclo inverso. Además \(t^3=-I_2\) pero \(S^3=(-I)\otimes(-I)=I_4\). Y \(\sigma_yt^*\sigma_y=t\), luego \(VS^*V=S\).

**(3) Nodos y conos.** \(N\) tiene autovalores \(\pm 1\) de multiplicidad 2. \(NP=P\) y \(NQ=-Q\), de modo que
\[
WP=e^{-i\pi/4}P,\qquad WQ=e^{i\pi/4}Q.
\]
En \(k=0\), \(U(0)=W\): dos dobletes de fases distintas, separadas por \(\pi/2\).

Aunque \(W\) no conmuta con \(G_i\), \(\partial_iU(0)=(-i/\sqrt{3})WG_i\), y por tanto \(J_i=iW^\dagger\partial_iU(0)=G_i/\sqrt{3}\). Con \(P=I\otimes|n_+\rangle\langle n_+|\) y \(\langle n_+|\tau_i|n_+\rangle=n_i=1/\sqrt{3}\),
\[
PG_iP=R_iP/\sqrt{3}\implies PJ_iP=(\sigma_i\otimes I)P/3,
\]
y en \(Q\) el signo se invierte porque \(\langle n_-|\tau_i|n_-\rangle=-1/\sqrt{3}\). El bloque efectivo es \(\pm(q\cdot\sigma)/3\), sin término de traza. Su polinomio es \(\lambda^2-|q|^2/9\): dos cruces cónicos, no degenerados para \(q\neq 0\), velocidad \(1/3\) en toda dirección. El acoplamiento \(P\)–\(Q\) no entra a primer orden porque las fases ya están separadas. No hay isotropía a todo orden, y el informe no la afirma.

Segunda vía. En el eje \(i\), cada sector \(\sigma_i=\varepsilon\) reduce a
\[
w_\tau\bigl(\cos x\,I-i\varepsilon\sin x\,\tau_i\bigr),\qquad x=k_i/\sqrt{3},
\]
con \(w_\tau=(I-im)/\sqrt{2}\). Determinante 1. La semitraza sale
\[
f(x)=\bigl(\cos x-\varepsilon\sin x/\sqrt{3}\bigr)/\sqrt{2}:
\]
hace falta \(\operatorname{Tr}(w\tau_i)=-i\sqrt{2}\,n_i\) y \(n_i=1/\sqrt{3}\). Las autofases del bloque son \(\pm\operatorname{acos}(f)\); en el origen valen \(\pm\pi/4\), y
\[
\frac{d}{dk_i}\operatorname{acos}(f)\Big|_0=\varepsilon/3.
\]
Con la convención autovalor \(=e^{-i\varphi}\), la rama \(P\) (\(\varphi=\pi/4\)) tiene pendiente \(+\varepsilon/3\) y la \(Q\) tiene \(-\varepsilon/3\). Coinciden con las compresiones. Esta vía solo ve los ejes; la isotropía fuera de ellos sale del bloque \((q\cdot\sigma)/3\).

**(4) Irreducibilidad.** Quien conmuta con los cuatro \(A_h=WE_h\) conmuta con \(W=\sum A_h\) y con \(E_h=W^\dagger A_h\). En la base de Bell (autovectores reales de los \(G_i\), uno por cada signo de producto \(-1\)) eso obliga a \(X=\sum\lambda_h E_h\). Cada \(I\otimes\tau_i\) es unitaria y cambia los dos signos \(j\neq i\), así que conecta cada rayo con otro rayo permitido mediante un elemento de módulo 1. Como las tres componentes de \(n\) son no nulas, \(\langle h'|N|h\rangle\neq 0\) para todo par distinto. Conmutar con \(N\), luego con \(W\), iguala las cuatro \(\lambda_h\). El conmutante es exactamente los escalares: no hay descomposición en suma directa con base interna fija. El rango 15 del script es la misma afirmación; la prueba no depende de él.

**(5) Geometría.** Los cuatro vértices tienen norma 1, productos distintos \(-1/3\) y baricentro 0: tetraedro regular. La cara opuesta a \(v\) es el plano \(x\cdot v=-1/3\), normal exterior \(-v\), distancia \(1/3\). Luego \(r_{\mathrm{in}}=1/3\) (también por \(R=3r\) en el tetraedro regular) y \(h_C(u)=\max_{v\in F}u\cdot v\). La longitud máxima de paso es 1. El valor \(c=1/3\) sale de \(n_i/\sqrt{3}\); \(r_{\mathrm{in}}=1/3\) sale de los productos escalares. Son cuentas distintas. El informe las iguala solo en esta realización y no calcula ni el cuerpo estricto asintótico ni una cota general.

Los tres primeros generadores enteros, en el orden de inserción \((-1,-1,-1)\), \((-1,1,1)\), \((1,-1,1)\), tienen determinante \(-4\). La red de paridad igual tiene índice 4 en \(\mathbb{Z}^3\) y los contiene, así que esos tres la generan entera. No se renormaliza después.

**(6) Argumento local.** Con las representaciones fijas: \(U(0)\) conmuta con todos los \(R_j\), cuyo conmutante es \(I\otimes M_2\), luego \(U(0)=I\otimes w'\). Conmutar con \(S\) equivale a que \(w'\) conmute con \(t\). Los autovalores de \(t\) son \(e^{\pm i\pi/3}\), distintos, y sus ejes son los de \(n\cdot\tau\). Si los dos autovalores de \(w'\) siguen separados, el eje es \(n\) salvo intercambio de \(P\) con \(Q\).

La covarianza bajo \(D_2\) fuerza \(J_i=\sigma_i\otimes\mu_i\) con \(\mu_i\) hermítica, \(\mu_i=a_iI+v_i\cdot\tau\). La condición \(VM_i^*V=-M_i\), usando que la conjugación entrada a entrada conserva el orden del producto, se reduce a \(\tau_y\mu_i^*\tau_y=-\mu_i\), es decir \(a_i=0\). Queda \(J_i=\sigma_i\otimes(v_i\cdot\tau)\). El ciclo de \(S\) impone \(v_{i+1}=Rv_i\) con la misma rotación de \(+120^\circ\). Como \(Rn=n\), los tres \(v_i\cdot n\) coinciden; llamémoslo \(\gamma\). Las compresiones son \(+\gamma\,q\cdot\sigma\) en \(P\) y \(-\gamma\,q\cdot\sigma\) en \(Q\): opuestas, y la métrica lineal es isotrópica, con \(|c_P|=|c_Q|=|\gamma|\). En el punto construido \(\gamma=1/3\neq 0\). Esto es una restricción del 1-jet dentro de la clase de simetrías, no una clasificación de todas las unitarias de Laurent ni una prueba de que esa clase tenga dimensión positiva. El informe lo dice.

**(7) Script e informe.** Coinciden en lo que importa: \(W_{\mathrm{raw}}=\sqrt{2}W\); paridad negativa del soporte; convoluciones con blanco \(2I\); \(C\) por \(VA^*V\), no por adjuntos; ciclo \((h_z,h_x,h_y)\); semigiros por cambio de signo; fases \((1\mp i)\) de \(W_{\mathrm{raw}}\), que son \(\sqrt{2}\,e^{\mp i\pi/4}\); compresiones \(PG_iP/\sqrt{3}=RP/3\) y el signo opuesto en \(Q\); polinomio \(\lambda^2-|q|^2/9\); semitraza axial, determinante 1 y pendiente física \(\varepsilon/3\); rango 15; radios, productos \(\pm 1\) o \(-1/3\), baricentro y \(|\det|=4\). No hay una comprobación que afirme otra cosa que el informe.

**(8) Alcance.** No se excede. \(F\) no contiene a \(-F\): el inverso de cada vértice es uno de los cuatro puntos de paridad positiva, que están anulados. Negarse a entrar en una clase que pida un salto y su inverso es coherente con ese hecho. No se afirma hull cúbico, ni ocho coeficientes no nulos, ni cuerpo estricto, ni selección, ni valor físico de \(c\).

## Objeciones

Ninguna. No hay error de signo en el ciclo, ni en las fases \(\pm\pi/4\), ni en el paso de \(n_i=1/\sqrt{3}\) a la velocidad \(1/3\), ni un supuesto oculto del que dependa el veredicto.

## Alcance que acepto

Una unitaria exacta de dimensión interna 4 y alcance finito, con soporte real \(F\) (tetraedro regular de circunradio 1, no el cubo de ocho vértices), irreducible en el sentido de conmutante común escalar. Simetrías exactas \(D_2\), \(C=VK\) con \(VU(k)^*V^\dagger=U(-k)\), y \(SU(k_x,k_y,k_z)S^\dagger=U(k_z,k_x,k_y)\). En \(k=0\), dos dobletes de fases \(\pm\pi/4\). A primer orden, dos conos isotrópicos sin inclinación, \(c_P=c_Q=1/3\), confirmados por compresión y por las tres derivadas axiales. El hull de un paso tiene \(r_{\mathrm{in}}=1/3\); la igualdad con \(c\) es de esta normalización y de este constructor. La red generada es la de paridad igual, escalada por \(1/\sqrt{3}\), índice 4.

Queda fuera: la variante de ocho saltos no nulos, el cuerpo causal estricto, cualquier ley \(c=r_{\mathrm{in}}\), la selección de las simetrías, un valor físico de \(c\), la pertenencia a la clase de `1708.00826` y toda lectura de ese PDF. Preliminar y de comprobación de autor.
