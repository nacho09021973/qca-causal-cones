<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 ead46cd50fe9538bc2edea386b54034d4f34d242126c2d34b6799aaef922ada4
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-29T16:05:23Z  fin: 2026-10-29T16:17:24Z
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step4b1.md ; último commit observado: 4646be5 ; sha256 de la copia enviada f7ff509f01143d0b4b33cb5022e8939dc39353328ddfd936cc966be686567f26
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step4b1.py ; último commit observado: 4646be5 ; sha256 de la copia enviada 5b0122f11df6f88d01cea7c88a45a07680606c8b78fbd4df2146dab08dfe0b33
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--minimal-s2-step4b1-review-astra/informe_astra.md ; último commit observado: 0460743 ; sha256 de la copia enviada a4e7fc3100f2b88a3377c832e7db6c799580bd1035dc15db166b1137abf06645
documento: /home/ignac/qca-causal-cones/scripts/verify_irreducible_isotropy_step01.py ; último commit observado: d4a8134 ; sha256 de la copia enviada d4b3d242bdd259aa45aa532b6b212bfe75eb0009097f85883805507857f1bfe4
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step00.py ; último commit observado: ebebca7 ; sha256 de la copia enviada adeb8afc4d4be5ed8d692f47727882e688991a36e7e5739a3eeb1bd053bbec5b
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 785565c ; sha256 de la copia enviada 657fa6d3e9f17b69fedfde5d592d038b1eca90e90c496a8da1b43ffaa5ae8ea5
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
documento: /home/ignac/qca-causal-cones/biblioteca/arXiv-1902.10227.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada 663d7ca3ba6a38cbb2073d1f2e65f59b22901eb778f24f9d78a9ecc2b2b8a5d4
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
entrada_grok.txt sha256 3e1e396584dbc37b13769fce0715e371d089a3fc1894f6b3797fce3e309263fc
respuesta sha256 67f5a00f80429416059130804e3388b4e8d925b46465568ed0fd774d22375172
-->

**Veredicto:** las seis reparaciones quedan resueltas como las pidió Astra, y las cinco conclusiones por clase son correctas por pruebas directas, no por la aceptación previa. El testigo `T_{(x,y,z)}=P_x^x P_y^y P_z^z` es el desarrollo de Fourier de ese producto de exponenciales; `laurent_unitary` y `covariant` comprueban lo que dicen. El generador de la etapa 01 no invalida las vaciedades ni el control secundario. Queda una laguna de auditabilidad, no un error de las conclusiones: el informe atribuye controles negativos que no están en el certificado.

## Supuestos

No ejecuté nada. Tiempos, hashes, «17/17» y «49/49» quedan **[UNVERIFIED]** como ejecuciones. El 17 coincide solo con el número de `require` del camino de éxito.

Acepto el universo de las cinco clases fieles de la etapa (a) sin reenumerar los 30 subgrupos. En los scripts, \(N_3=\{\pm1\}^3\); el \(q\) del testigo es el conjugado de esas etiquetas, no de \(\varepsilon/\sqrt3\). Eso no cambia existencia ni vaciedad. No tengo el PDF de P17: la frase sobre grupo y representación se juzga contra el charter. DEP19 se juzga por el texto adjunto.

## Tabla de reparaciones

| ID | Pedido de Astra | Estado |
| --- | --- | --- |
| A-4B1-01 | Adjuntar `unitarity_equations`, `groebner_is_unit` y `published_symbol`, o sustituir la existencia por un certificado algebraico | **Resuelta.** La existencia ya no usa `S1`: el testigo se comprueba en el certificado. Las tres funciones están en los documentos 4 y 9. |
| A-4B1-02 | Quitar «same Groebner outcome» en \(V_4\); allí solo se compara el número de parámetros | **Resuelta.** El informe lo dice, y la rama `else` solo exige `len(p2)==len(params)`. |
| A-4B1-03 | Infraestructura compartida; la igualdad de dimensiones no es igualdad de subespacios | **Resuelta.** El texto precisa qué pueden y qué no pueden detectar. |
| A-4B1-04 | Nombrar la clase congelada; coincidencia con P17 solo de grupo y representación | **Resuelta.** Se niega explícitamente «P17 menos Eq. (2)». |
| A-4B1-05 | Restringir `COUNTEREXAMPLE_VERIFIED_ABOVE` a \(C_4\) | **Resuelta.** La clase superviviente queda abierta y remitida a 4b-2. |
| A-4B1-06 | (14) es la normalización \(\sum_h A_h=I_s\), no isotropía | **Resuelta.** Coincide con la ecuación (14) del texto adjunto. |

## 1. Reparaciones y conclusiones por clase

Las cuatro vaciedades valen para la complexificación y sin soporte activo. La existencia en \((V_4,\mathrm{Pauli})\) es un punto real con los ocho coeficientes no nulos.

**\((C_4,\mathrm{cara})\), y por restricción \(D_4\) y \(O\).** Sea \(r(x,y,z)=(-y,x,z)\) y \(q_*=(\pi/2,\pi/2,0)\), con vértices en \(\{\pm1\}^3\). Entonces \(w(h)=e^{-iq_*\cdot h}=-h_x h_y\) y \(w(rh)=-w(h)\). La covarianza da \(R U(q_*)R^\dagger=-U(q_*)\).

El levantamiento de esa rotación de \(90^\circ\) actúa sobre \(\mathrm{span}\{I,\sigma_z\}\) con autovalor \(1\) y sobre \(\mathrm{span}\{\sigma_x,\sigma_y\}\) por \(\sigma_x\mapsto\sigma_y\), \(\sigma_y\mapsto-\sigma_x\), de polinomio característico \(\lambda^2+1\). Autovalores \(1,1,i,-i\): no está \(-1\), luego \(U(q_*)=0\).

Eso es incompatible con la unitariedad. En el ideal, los pesos \(e^{-iq_*\cdot\ell}=(-1)^{(\ell_x+\ell_y)/2}\) son \(\pm1\), y la misma identidad escribe \(I\) como combinación de los bloques \(E_\ell\). El grupo de la cara es ese \(C_4\); \(D_4\) y \(O\) lo contienen. Un cambio de base constante transporta la vaciedad a cualquier \(\rho\) fiel conjugada a la inclusión.

**\((T,\mathrm{tetraedro})\).** Dos órbitas, estabilizador de orden 3, y \(T_h=a_p I+c_p\,h\cdot\sigma\) con \(p=h_x h_y h_z\). Si \(U\) es unitario, \(\det U\) es unidad de Laurent, luego \(d\,z^m\) con \(d\neq0\). La covarianza fuerza \(g\cdot m=m\) para todo \(g\in T\); el único vector de \(\{-2,0,2\}^3\) fijado también por el semigiro \((x,y,z)\mapsto(x,-y,-z)\) es \(m=0\).

Con \(U=fI+b\cdot\sigma\), \(\det U=f^2-b\cdot b\). El modo \(2h\) da \(a_\pm^2=3c_\pm^2\). El modo \((0,2,2)\) recibe las dos parejas \((1,1,1)+(-1,1,1)\) y da \(a_+a_-=c_+c_-\). Por tanto \((c_+c_-)^2=9(c_+c_-)^2\), así \(c_+c_-=a_+a_-=0\). El término constante es \(8(a_+a_-+3c_+c_-)=0\), contradicción.

**\((V_4,\mathrm{tetraedro},\mathrm{Pauli})\).** El testigo de la sección 2 es unitario, covariante bajo el \(V_4\) axial y con ocho coeficientes no nulos. El \(V_4\) diagonal es normal en \(O\), así que el representante de la clase es ese grupo. Un punto real implica que el ideal no es \((1)\): los 79 s son **[UNVERIFIED]**, la afirmación no. Los 16 parámetros son los de dos órbitas con estabilizador trivial: \(2+6\) reales por órbita. No afirmo que las dos construcciones definan el mismo subespacio; el informe ya no lo afirma. El testigo entra por la covarianza, no por esa comparación.

## 2. Testigo

El convenio es el correcto. Con \(P_j^\varepsilon=(I+\varepsilon\sigma_j)/2\),

\[
e^{-iq_j\sigma_j}=\sum_{\varepsilon=\pm1}e^{-iq_j\varepsilon}P_j^\varepsilon.
\]

El producto, en el orden \(x\), luego \(y\), luego \(z\), es \(\sum_h T_h e^{-iq\cdot h}\) con \(T_h=P_x^{h_x}P_y^{h_y}P_z^{h_z}\). El código multiplica en ese orden. No es el símbolo de Pavia de quiralidad \(1\): en el documento 9, `signs = (1, -chirality, 1)`, de modo que el testigo es la quiralidad \(-1\). La quiralidad \(1\) lleva \(P_y^{-h_y}\) y es otro punto, también covariante bajo \(V_4\).

`laurent_unitary` sí comprueba las dos identidades de Laurent. Con \(\ell=h'-h\), la suma \(T_h^\dagger T_{h'}\) es el modo de \(U^\dagger U\), y \(T_{h'}T_h^\dagger\) el de \(UU^\dagger\). Recorre los 27 desplazamientos de \(\{-2,0,2\}^3\). Además el producto de tres unitarios es unitario en todo \(q\) real, y un polinomio de Laurent idénticamente \(I\) tiene todos los modos nulos salvo el de \(\ell=0\).

`covariant` sí es la covarianza con \(\rho\) igual a la inclusión. De \(T=aI+b\cdot\sigma\) salen \(a=\mathrm{tr}(T)/2\) y \(b_j=\mathrm{tr}(T\sigma_j)/2\), y \(\{I,\sigma_x,\sigma_y,\sigma_z\}\) es base. Comparar trazas y \(b_{gh}=gb_h\) es la igualdad matricial. La conjugación por el levantamiento de un semigiro axial actúa por \(P_j^\varepsilon\mapsto P_j^{g_{jj}\varepsilon}\), y el producto de proyectores va a \(T_{gh}\). Los ocho coeficientes son no nulos: los solapes consecutivos de autovectores de ejes distintos son todos no nulos (\(\langle\pm x|\pm y\rangle=(1\pm i)/2\) o \((1\mp i)/2\), y \(\langle\pm y|\pm z\rangle\) tiene módulo \(1/\sqrt2\)).

## 3. Documento 4

No invalida las vaciedades ni el control secundario.

`unitarity_equations` solo impone \(U^\dagger U=I\). Para matrices cuadradas sobre el anillo de Laurent, inverso por la izquierda implica inverso por la derecha, así que no falta una solución unitaria. Eliminar una ecuación haría más difícil obtener el ideal \((1)\), no más fácil. `groebner_is_unit` exige base \([1]\) en grevlex; eso es vaciedad compleja del sistema real/imaginario. Las vaciedades de arriba no dependen de esa ejecución.

El control de Pavia solo se llama en la rama no vacía, y solo mira covarianza. La extracción —coeficiente de \(z^{v+\mathbf1}\) en \(z^{\mathbf1}M(z)\) guardado en \(T_{-v}\)— es la correcta si \(M=\sum_h T_h z^{-h}\). Su unitariedad se importa de la etapa 01 y el informe lo dice. No sostiene la existencia: esa la sostiene el testigo.

## 4. Alcance

Las frases nuevas sobre el ideal de la segunda construcción, la infraestructura compartida, el nombre de la clase, \(C_4\) y la ecuación (14) se mantienen dentro de lo certificado. También es correcto no adoptar aquí el argumento de Astra sobre la Eq. (2): el charter lo deja en 4b-2. La cota en la clase superviviente se enuncia solo en nodos con transporte admisible.

Excede el certificado la frase de controles negativos (objeción de abajo). «Sin código importado» es impreciso: el testigo usa `sym_zero` y `S0.act`, aunque no usa el generador ni la base de Gröbner. Llamar «anticipaciones» a los controles `T2s`/`O2s` tampoco coincide con el documento 4, donde forman parte de lo que ese script certifica.

## Objeciones nuevas

| ID | Ubicación | Gravedad | Hecho |
| --- | --- | --- | --- |
| A-4B1-R2-01 | Informe, «Existence» | Laguna | «Negative controls run during the repair» no está en el certificado: no hay coeficiente doblado ni generador de \(C_4\). La no covarianza bajo \(r\) es cierta, pero no está certificada. Para \(h=(1,1,1)\), \(T=P_x^+P_y^+P_z^+=\begin{pmatrix}(1+i)/4&0\\(1+i)/4&0\end{pmatrix}\), luego \(b=((1+i)/8,(1-i)/8,(1+i)/8)\). En \(rh=(-1,1,1)\), la componente \(z\) sale \((1-i)/8\), no \((1+i)/8\). |
| A-4B1-R2-02 | Informe, «Result», frase de `T2s`/`O2s`; certificado, «no imported code» | Redacción | Esos controles de la etapa 01 no son anticipaciones. El testigo no está libre de código importado: usa `sym_zero` y `S0.act`. |

No hay error demostrado en las cinco conclusiones ni en el testigo.

**Veredicto global:** 4b-1 puede permanecer **PRELIMINARY** con estas cinco conclusiones. A-4B1-R2-01 no las toca; se cierra tachando la frase o metiendo esos dos controles en el certificado. No promocionaría el «49/49» ni los tiempos: no están en los adjuntos.
