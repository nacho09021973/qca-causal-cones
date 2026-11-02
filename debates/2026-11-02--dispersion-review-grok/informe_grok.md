<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 2456cded4f631f4881a3df4706b4ff897567f7e808b9d9034637bd900d506e06
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-02T17:17:26Z  fin: 2026-11-02T17:39:48Z
documento: /home/adnac/qca-causal-cones/theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md ; último commit observado: a7ff5b7 ; sha256 de la copia enviada 6df09e81fae231ebbb00d19de546298559d333d33e965c95a1aa6027842231ea
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices.md ; último commit observado: 9557aa9 ; sha256 de la copia enviada 6f0f9394c73b13dd62e3f1034cbeec187824c91c54a26c180d03dbabca45203e
documento: /home/adnac/qca-causal-cones/scripts/verify_dispersion_corrections_gate.py ; último commit observado: 9557aa9 ; sha256 de la copia enviada 791f0d80d2790f34b72521c90622fa0056fd629fa1b3ef89addfc2ad664e6c2a
documento: /home/adnac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
documento: /home/adnac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/adnac/qca-causal-cones/scripts/verify_directional_saturation.py ; último commit observado: 78fcaca ; sha256 de la copia enviada 1d1894730f83ea24808bb5e939492fe2144fdd97cdcf87961a0978da35ae4596
documento: /home/adnac/qca-causal-cones/scripts/cert_Aa_s4_counterexample.py ; último commit observado: 1dae941 ; sha256 de la copia enviada 635a24706df763efda1458e6742a1c43763f6a7ff7c22ddc7c6637f78ea5787a
documento: /home/adnac/qca-causal-cones/scripts/verify_l6b_triangular_row_gate.py ; último commit observado: a19e480 ; sha256 de la copia enviada c2e91c237b023abde1199f8ef3bea143f49e559da35899c01e049a9ddf3f2441
entrada_grok.txt sha256 5859cd5784e9882225d85484b267e203fbde162f70e6e344a6b7d17579714843
respuesta sha256 26d1dc14fa37084dded0cd626a88b4f103b00eadc0e435107dc488e8c7d49a65
-->

**Dictamen global: REPAIR_REQUIRED.** El método de serie, los bloques, la simetría y los veredictos Hd, He y Hf se sostienen en lo reconstruido por otra vía. No promocionar: el informe afirma dos cosas falsas (signo direccional universal cuando \(\beta\neq 0\); «cada» bloque de L5b) y el verificador tiene un `record` de predicado constante. No ejecuté nada y no confirmo 79/79.

## 1. SERIES — PASS

El factor \(\lambda^2-s_1\lambda+s_2\) de un bloque unitario con autovalores \(e^{-i(\varepsilon_0+\varphi\pm\omega)}\) cumple
\[
e^{-2i\varphi}=\frac{s_2}{s_2(0)},\qquad \cos^2\omega=\frac{s_1^2}{4s_2}.
\]
Con \(v=2(1-\cos^2\omega)=1-\cos 2\omega\), \(\omega^2=\arccos(1-v)^2/4\). Los coeficientes guardados coinciden con las series: \(\log(1+v)\), \(\sqrt{1+v}\), \(1/(1+v)\) y
\[
\arccos(1-v)^2=2v+\tfrac13 v^2+\tfrac4{45}v^3+\tfrac1{35}v^4+O(v^5).
\]
La composición truncada es el producto formal correcto: \(v=O(|k|^2)\), de modo que hasta grado 6 bastan \(v,v^2,v^3\).

\(N=4\) (\(d=3\)) fija \(Q_3,Q_4\) y, con ellos, \(\beta\) y \(\alpha\): el término \(-\frac18(Q_3/c_0^2)^2\) que mete \(n_1^2 n_2^2 n_3^2\) en \(\alpha\) solo depende de \(Q_3\). \(N=6\) (\(d\le 2\)) fija \(E_5\), el orden relativo \(|k|^4\) que el contrato pide a las filas \(C_6\). En las pares, \(x=O(t^2)\) y \(x^3=O(t^6)\) no entra en \(E_5\).

La velocidad de grupo del código es el gradiente cartesiano, no la derivada radial. Si \(\varepsilon=c_0 r\bigl(1+\beta(\hat n)\,r+\alpha(\hat n)\,r^2+O(r^3)\bigr)\),
\[
|\nabla\varepsilon|/c_0=1+2\beta\,t+O(t^2),
\]
porque \(\nabla_S\beta\) es tangente y su cuadrado empieza en \(t^2\). Si \(\beta=0\) y la rama es par, el término impar se va y queda \(1+3\alpha\,t^2+O(t^4)\). Las dos fórmulas del informe (§3.5) son esas. En L6b el divisor 3 escala \(\Omega\) y \(c_0\) a la vez, así que el cociente \(|\nabla\varepsilon|/c_0\) no lo pierde.

Aclaración: \(\omega=c_0|k|\) no es analítica en \(k=0\); el contrato pide el desarrollo en el rayo, que sí lo es.

## 2. BLOCKS — PASS

**L5b.** \(\Gamma=\Delta P_X\Delta P_Y\Delta P_Z\) con involuciones que anticonmutan cumple \(\Gamma^2=-I\) y conmuta con cada \(\Delta P_b\), luego con \(U\). El proyector \((I-\mathrm{sgn}\,i\Gamma)/2\) es el del autovalor \(\mathrm{sgn}\,i\). Los bloques son las dos quiralidades: mismo \(\alpha\), \(\beta\) opuesto.

**L6b.** \(V=U^3\), escala \(1/2\) (paso de una actualización) y divisor 3 son los del contrato. La relación con L6a queda abajo.

**L3s4.** En \(\theta=\pi/4\), \(W=\mathrm{diag}(e^{\mp i\pi/4})\) con multiplicidad 2. El nombre `+pi/4` va con \(\lambda=e^{-i\pi/4}\) porque \(\varepsilon_0=i\log\lambda\). El levantamiento de Hensel (factor mónico de grado 2, cofactor mónico, \(n\) incógnitas y Newton–Girard sobre trazas) es el correcto; el contraste con el característico completo está hecho en el \(4\times 4\) de L5b, que es el sustituto honesto de no poder expandir \(A_a\) simbólico.

El test de cero es exacto en la forma reducida \(c_0(a)+c_1(a)b\) con \(b^2=1-a^2\): \(1\) y \(\sqrt{1-a^2}\) son linealmente independientes sobre las funciones racionales de \(a\). `simplify` solo es respaldo; si no reconoce un cero, el script cae (fail-closed). No hay un falso cero exhibido.

**Lectura de \(\varphi\neq 0\).** Por Schur entre cúmulos, con \(\lambda_0-\lambda_-=-i\sqrt2\) y \(\lvert\langle+|t_j|-\rangle\rvert^2=b^2\),
\[
\varphi_{+\pi/4}=\frac{1-a^2}{2}\,|q|^2+O(|q|^3)=\frac{1-a^2}{6}\,t^2+O(t^4),
\]
\(q=k/\sqrt3\), y \(\varphi_{-\pi/4}=-\varphi\) porque \(\det U=1\). Parte real del mismo cálculo: \(\omega^2=a^2|q|^2\), luego \(c_0=a/\sqrt3\). \(\varphi\) desplaza los dos niveles del cúmulo juntos; \(\pm\omega\) es el desdoble. La parte isotrópica de \(\beta\) es exactamente \(\varphi/c_0\):
\[
\beta_0=\pm\frac{\sqrt3\,(1-a^2)}{6a}.
\]
En \(a=1\) desaparece y el coeficiente de \(n_1 n_2 n_3\) queda \(\sqrt3/3\), el de L5a. «Repulsión» describe el signo: los centros \(\pm\pi/4\) se separan.

## 3. SYMMETRY — PASS

Igualdad de \(\mathrm{tr}\,U^m\), \(m=1..s\), en característica 0, más Newton, es igualdad de polinomios característicos. La sustitución \(z^h\mapsto z^{Mh}\) con \(M=G^{-1} g^\top G\) es \(U(gk)\) en las mismas variables de Laurent. Es la noción del contrato y la adecuada: el característico fija el espectro; los armónicos permitidos son los de \(G_\mathrm{walk}\).

El argumento de grado de la Sec. 1 es correcto. Bajo el giro \(2\pi/m\), un polinomio homogéneo de grado \(n\) solo admite \(|k|^{n-jm}\mathrm{Re}/\mathrm{Im}(k_x+ik_y)^{jm}\). Para \(C_6\), \(n\) impar es imposible (\(p-q\) sería impar y múltiplo de 6) y en grado 4 solo queda \(|k|^4\); el primer anisótropo es \(\cos 6\theta\), orden relativo \(|k|^4\). Para \(C_3\), \(\mathrm{Re}(k_x+ik_y)^3\) entra en grado 3, orden relativo \(|k|\). Para \(C_4\), \(\cos 4\theta\) en grado 4. El armónico cúbico de grado 4 es el indicado.

Grupos que quedan forzados por la dispersión, no solo por el nombre:

- L3: \(\cos\omega=\prod\cos p_i\) aguanta las 48 permutaciones con signo. \(O_h\).
- L4 y las BCC quirales: \(\cos\omega=c_1 c_2 c_3+s_1 s_2 s_3\) aguanta permutaciones y un número par de cambios de signo (24), que incluye isometrías impropias (una transposición sin signos tiene determinante \(-1\)). Es \(T_d\), el del tetraedro \((1,1,1)\) y conjugados, no el grupo de rotaciones del cubo.
- L6a: derivé \(\beta=-(\sqrt{15}/36)\cos 3\theta\). Un giro de \(60^\circ\) cambia el signo de \(\cos 3\theta\), así que no está en \(G_\mathrm{walk}\). El de \(120^\circ\) y las reflexiones sí. \(D_3\) de orden 6, no \(D_6\). Igual L6b.
- Cuadrado: orden 8 es \(D_4\) en el sentido del contrato. L1: \(\{\pm 1\}\).

Aclaración: no reenumeré los 8 elementos de L3s4. El conteo por debajo de 24 sí está forzado: \(t_2=-b\sigma_x+a\sigma_z\) no cicla \(x\) con \(y\), y el término impar de \(\beta\) excluye \(-I\). La descripción «medias vueltas de \(D_2\) y el intercambio \(x\leftrightarrow z\)» es compatible con eso; no la doy por listada elemento a elemento.

## 4. VALUES — REPAIR_REQUIRED

Formas cerradas reconstruidas, no leídas del informe.

Con \(\cos\omega=\prod_i\cos p_i\), \(p=k/\sqrt d\) y \(\log\cos x=-x^2/2-x^4/12+O(x^6)\),
\[
\omega^2=|p|^2-\frac13\sum_{i<j}p_i^2 p_j^2+O(p^6),\qquad
\alpha=-\frac1{6d}\sum_{i<j}n_i^2 n_j^2.
\]
L2 (\(d=2\)): \(\alpha=-n_1^2 n_2^2/12=-(1-\cos 4\theta)/96\), \(\alpha_0=-1/96\). L3: \(\alpha=-\sigma_2/18=-1/90+K_4/36\), y \(\langle\sigma_2\rangle=1/5\) da \(\alpha_0=-1/90\).

El producto quiral \(\prod\exp(\pm i p_b\sigma_b)\) tiene el mismo \(Q_4=-\sigma_2/27\) (el triple producto entra en grado 3 y 5, no en 4) y \(Q_3=\pm(2\sqrt3/9)\,n_1 n_2 n_3\). De ahí \(\beta=\pm(\sqrt3/3)\,n_1 n_2 n_3\) y
\[
\alpha=-\frac{\sigma_2}{18}-\frac{n_1^2 n_2^2 n_3^2}{6}.
\]
L4 es el producto con el signo \(+i\) de CJWW (5.12), cuyo término cúbico de \(\omega^2\) es \(-2p_1 p_2 p_3\): \(\beta\) negativo. L5a es ese producto con \(p\to -p\): \(\beta\) positivo, el mismo \(\alpha\). Media esférica: \(\langle\sigma_2\rangle/18=1/90\), \(\langle n_1^2 n_2^2 n_3^2\rangle=1/105\), luego \(\alpha_0=-1/90-1/630=-4/315\).

L6a, rayo \(q=(t,0)\), \(\varphi_0=t\), \(\varphi_{1,2}=-t/2\), \(m_i\cdot m_j=1/3\) y \([m_2,m_1,m_0]=-2\sqrt{15}/9\):
\[
\cos\omega=1-\frac{t^2}{2}+\frac{\sqrt{15}}{18}t^3+\frac18 t^4+O(t^5).
\]
El \(t^2\) y el \(t^3\) salieron por dos vías (traza del triple producto y parte escalar del producto de tres \(SU(2)\)). Con \(q=k/2\), \(\beta(0)=-\sqrt{15}/36\). Bajo \(C_3\) el único invariante polinómico de grado 4 es \(|k|^4\), así que la anisotropía de \(\alpha\) es solo \(-\beta^2/2\), es decir \(-(5/1728)\cos 6\theta\). El valor en \(\theta=0\) fija el resto: \(\alpha=-41/1728-(5/1728)\cos 6\theta\).

L6b. Generadores a la mitad y \(\varepsilon=\Omega/3\) dan \(\varepsilon_{L6b}(k)=\varepsilon_{L6a}(2Rk)/3\). Por tanto \(c_0\) escala por \(2/3\) (\(1/2\to 1/3\)), \(\beta\) por 2 y \(\alpha\) por 4. El giro de \(60^\circ\) manda \(\cos 3\theta\to-\cos 3\theta\) y no cambia \(\cos 6\theta\): \(\beta_{L6b}=(\sqrt{15}/18)\cos 3\theta\), \(\alpha_{L6b}=-41/432-(5/432)\cos 6\theta\). La relación del informe es correcta.

L3s4. \(\alpha_0(1)=-4/315\) recupera L5a. El numerador \(27a^4-34a^2+5\) tiene una sola raíz en \((0,1)\),
\[
a_*=\frac{\sqrt3\,\sqrt{17-\sqrt{154}}}{9}\approx 0{,}412,
\]
y \(\alpha_0>0\) en \((0,a_*)\), \(\alpha_0<0\) en \((a_*,1)\). Eso sí está comprobado. No rederivé los coeficientes 27 y \(-34\) término a término, ni \(\alpha\) de L6c, L6d, L6f, ni los tres coeficientes de \(E_5\). No los contradigo; tampoco los certifico.

**Fallo, informe §3.3.** La frase que atribuye a toda fila con \(\beta\neq 0\) una corrección impar, que toma ambos signos, es falsa en L3s4. Ahí
\[
\beta=\beta_0+\beta_3 n_1 n_2 n_3,\qquad \beta_0=\pm\frac{\sqrt3(1-a^2)}{6a}\neq 0,
\]
así que \(\beta(-\hat n)\neq -\beta(\hat n)\). Como \(\max|n_1 n_2 n_3|=1/(3\sqrt3)\), \(\beta\) conserva el signo de \(\beta_0\) cuando
\[
a^2<\frac{19-6\sqrt3}{11}\approx 0{,}783
\]
y solo por encima de ese umbral toma ambos signos. El §3.4, que separa la parte isotrópica, es el texto que hay que dejar en pie.

Qué lo cierra: restringir la frase de §3.3 a L5a, L5b, L4, L6a y L6b, y escribir el umbral de L3s4 (depende del cúmulo y de la rama, porque el signo isotrópico se invierte al pasar a \(\varepsilon_0+\varphi-\omega\)).

## 5. HYPOTHESES — PASS

Textos del contrato §4, no del resumen.

**Hd — `REFUTED_BY_ROW_L1`.** «\(\alpha_0<0\) en toda fila declarada». L1 tiene \(\alpha_0=0\) porque \(U=\exp(-ik\sigma_z)\) y \(\omega=|k|\) exacto. La simetría de \(d=1\) solo dice que \(\alpha\) es constante; no lo anula. No es `DECIDED_BY_SYMMETRY`. L3s4 refuerza la refutación en \(a<a_*\) (\(\alpha_0>0\)); el identificador L1 es el que cubre la fila entera. Correcto.

**He — `CONFIRMED_IN_DECLARED_ROWS`.** El contrato, en el ítem 3, trata \(\beta_3\cos 3\theta\) como la corrección más baja y su contenido anisótropo. El monomio impar \(n_1 n_2 n_3\) cuenta igual: es la corrección más baja de L5a, L5b y L4, no es constante en la esfera, y su coeficiente \(\sqrt3/3\) no es cero. \(D_4\), \(O_h\) y \(T_d\) lo permiten y no lo imponen (L3 tiene \(K_4/36\neq 0\) por cálculo, no por el grupo). Ninguna hexagonal alcanza \(c_0=r_\mathrm{in}\), así que la isotropía \(C_6\) no decide He. No toca `DECIDED_BY_SYMMETRY`.

**Hf — `REFUTED_BY_ROW_L6e`.** La cláusula operativa es: se refuta si dos filas del mismo sustrato tienen el mismo \(\beta(\hat n)\) y el mismo \(\alpha(\hat n)\). L2 y L6e lo cumplen (mismo cuadrado, pasos en las diagonales cartesianas \((\pm1,\pm1)\), no un giro de \(45^\circ\) que cambiaría el signo de \(\cos 4\theta\)). Con solo dos filas, la lectura del encabezado («no comparten todas») da la misma refutación. L6d y L6f, si de verdad coinciden hasta \(t^2\), son otro par; el veredicto puede citar solo L6e. En hexagonal y BCC no todas las filas coinciden, y el informe lo dice. La lectura es la del contrato.

**Fallo de prosa, no del veredicto (informe §1).** «L5a con cada bloque de Weyl de L5b» contradice la tabla y el §4: los bloques tienen \(\beta\) opuesto, así que \((\beta,\alpha)\) coincide con un solo bloque. Qué lo cierra: sustituir «cada» por «el bloque cuyo \(\beta\) tiene el signo de L5a; el otro difiere en ese signo». El veredicto Hf no depende de esa frase.

## 6. SCOPE_AND_CODE — REPAIR_REQUIRED

El veredicto `CORRECTIONS_TABLE_PARTIAL_VALIDITY_SCALE_AND_VGRP_OPEN` es el que autoriza la Sec. 8: en \(d=1\) las ramas se juntan en \(|k|=\pi\) (de \(e^{ik}=e^{-ik}\)); en \(d\ge 2\) la escala y \(V_\mathrm{grp}^\mathrm{max}\) quedan `OPEN`, que el ítem 5 y el ítem 6 permiten. No hay diccionario observacional, ni filas masivas, ni paseos nuevos. Las cuatro correcciones de la Sec. 5 son legítimas: Newton contrastado en L5b, \(b\) independiente porque \(\sqrt{1-a^2}\) no es racional en \(a\), el factor 4 de L6b que aquí sale de \(\varepsilon(k)=\varepsilon(2Rk)/3\), y restringir la proyección cúbica a \(|G_\mathrm{walk}|\ge 24\) porque L3s4 tiene 8 elementos. No es un ajuste para forzar Hd/He/Hf.

El `record` de Hd con predicado `True` (Parte 4) no puede fallar. No certifica el signo. Qué lo cierra: sustituirlo por el predicado que ya calcula el script (signo de cada \(\alpha_0\) numérico, y el cuadro de signos de L3s4 en los intervalos de Sturm). Hardcodear \(-1/512\) o \(-41/1728\) sería el otro vicio, codificar el resultado; no lo pido. Que Hd/He/Hf se impriman y el veredicto viva en el informe es aceptable: la cláusula de refutación es lógica, y las premisas cuantitativas de L2, L3, L4, L5 y L6a/L6b sí están en `record`. Aclaración: L6c, L6d, L6f y los órdenes de \(G_\mathrm{walk}\) salen solo por `print`; quien no ejecuta no los ata. No es una omisión de un ítem que el contrato deje sin salida `OPEN`.

El paquete no trae `.claude/settings.json`. No doy por revisadas las dos formas de comando de la Sec. 9.

## Reparaciones obligatorias

1. Informe §3.3, la oración que dice que toda fila con \(\beta\neq 0\) tiene corrección impar y de ambos signos. Falla en L3s4, donde \(\beta_0\neq 0\). La cierra el enunciado restringido y el umbral \(a^2=(19-6\sqrt3)/11\).
2. Informe §1, «L5a con cada bloque de Weyl de L5b». Falla porque \(\beta\) cambia de signo entre bloques. La cierra citar un solo bloque.
3. `verify_dispersion_corrections_gate.py`, el `record` de Hd cuyo tercer argumento efectivo es `True`. Falla como certificado. Lo cierra el predicado de signos ya calculado.

No hay más reparaciones obligatorias. En particular no hace falta tabular el \(\alpha\) no cúbico de L3s4: la corrección más baja ahí es \(\beta\), y esa sí está descompuesta; \(\alpha_0\) cubre el ítem 4.
