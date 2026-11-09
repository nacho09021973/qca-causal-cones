<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 96215fab2379234d288429aa79790039aa2cc1cd6106cede07e685c481fbaac9
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-09T08:11:55Z  fin: 2026-11-09T08:23:36Z
documento: /home/ignac/qca-causal-cones/theory/S4_GENERAL_COIN_VIABILITY.md ; último commit observado: 170910b ; sha256 de la copia enviada a817034f28736469d5ecccb0901bc9ba2c49832dde5dcff6117bc4bca2b1de13
documento: /home/ignac/qca-causal-cones/reports/2026-11-06--s4-general-coin-viability.md ; último commit observado: 170910b ; sha256 de la copia enviada 46e80a084b78f70f9903e749db4cced0843e4b65de1c4a0542ba32c4c5053bc5
documento: /home/ignac/qca-causal-cones/scripts/verify_s4_general_coin_viability.py ; último commit observado: 170910b ; sha256 de la copia enviada 6565ddc135215e371279b97c298422e809124110b3b3b439f79941fe6437a5f4
documento: /home/ignac/qca-causal-cones/reports/2026-11-06--s4-general-coin-viability-verifier.txt ; último commit observado: 170910b ; sha256 de la copia enviada 897a6208bd8f9f50de772ed1730091127502332f3a566be205e45cafc19e6728
entrada_grok.txt sha256 cdea9a8cdae8f8eaeec174dae7bf8ea6f85b7cc14caeb5c24b63996490d81485
respuesta sha256 dc2962c63a649cda1a12b293f88b5b93746de3308d1b4e942a9c631717273a0a
-->

**Veredicto: se sostiene.**

Para todo \(W\in U(4)\), si \(U(0)=W\) tiene un autovalor de multiplicidad exactamente dos y separado del resto, y el cono lineal de cuasienergía de ese doblete es isotrópico, sin inclinación y no degenerado, entonces \(c=1/3\). La clase no es vacía. El recuento 55/55 no es esa prueba: son identidades auxiliares. No hay error, supuesto oculto que invalide el enunciado, ni hueco en las hipótesis declaradas.

Lo que sigue está derivado a mano, salvo donde indico que solo inspecciono el script o el registro.

## Derivaciones

**(1) Álgebra de los \(G_i\) y de los \(E_h\).**  
Con \(\sigma_i\) las Pauli habituales y \(G_i=\sigma_i\otimes\sigma_i\),

\[
G_iG_j=(\sigma_i\sigma_j)\otimes(\sigma_i\sigma_j).
\]

Si \(i\neq j\), cada factor anticommuta y los dos signos se cancelan, así que \([G_i,G_j]=0\). Además \(G_i^2=I_4\). Para índices distintos, \(G_iG_j=-G_k\) (el índice que falta): \(G_xG_y=-G_z\), y por tanto \(G_xG_yG_z=-I_4\). Los autovalores conjuntos cumplen \(g_xg_yg_z=-1\). Hay cuatro, no ocho.

En ese espectro, \(E_h=(I+\sum_i h_i G_i)/4\) es el proyector de rango uno del patrón \(h\). El producto \(h_xh_yh_z=-1\) entra aquí: equivale a \(h_ih_j=-h_k\), y con eso

\[
\bigl(I+\sum_i h_i G_i\bigr)^2=4\bigl(I+\sum_i h_i G_i\bigr).
\]

Sin ese signo no sería proyector. La traza vale \(1\), así que el rango es uno. Los cuatro suman \(I_4\) y \(\sum_h h_i E_h=G_i\). También \(\sum_h h_i=0\) y \(\sum_h h_ih_j=4\delta_{ij}\). Como \(W\) es invertible, \(WE_h\neq 0\); eso fija el soporte, no el valor de \(c\).

**(2) Pendiente lineal, sin término extra de \(W\).**  
Los \(G_i\) conmutan, luego la identidad de soporte es exacta, no perturbativa:

\[
U(k)=\sum_h WE_h\exp(-ik\cdot h/\sqrt3).
\]

Derivando en el origen, \(\partial_i U(0)=-iWG_i/\sqrt3\), y

\[
iW^\dagger\partial_i U(0)=G_i/\sqrt3.
\]

\(W\) se cancela por \(W^\dagger W=I\), antes de comprimir.

Sea \(T:\mathbb{C}^2\to\mathbb{C}^4\) una isometría sobre el doblete, \(WT=zT\), \(|z|=1\). Entonces \(W^\dagger T=\bar z\,T\) y \(T^\dagger W=zT^\dagger\). No hace falta que \(W\) conmute con \(G_i\):

\[
T^\dagger WG_iT=z\,T^\dagger G_iT,
\]

y por tanto

\[
T^\dagger U(q)T=z\Bigl[I-i\sum_i q_i H_i\Bigr]+O(q^2),\qquad H_i=T^\dagger G_iT/\sqrt3.
\]

Esa compresión no es el doblete exacto para \(q\neq 0\). La separación sí lo convierte en la pendiente correcta. Con \(P\) el proyector ortogonal del doblete y \(Q=I-P\), en el origen \(QU(0)P=0\). El bloque diagonal es \(zP+q\cdot P(\partial U)P+O(q^2)\). El complemento de Schur lleva \(PUQ=O(|q|)\) y \(QUP=O(|q|)\), y el resolvente de \(QU(0)Q-z\) está acotado precisamente por la separación, así que ese complemento es \(O(q^2)\). La unitariedad importa: \(U(k)\) es normal, el proyector espectral es ortogonal y no hay que distinguir autovectores izquierdos y derechos.

El autovalor que sale de \(z\) es \(z(1-i\kappa)+O(q^2)\), con \(\kappa\) autovalor de \(\sum q_i H_i\). Si \(z=e^{-i\omega_0}\) y el autovalor es \(e^{-i(\omega_0+\varphi)}\), entonces \(\varphi=\kappa+O(q^2)\). La fase global \(z\) no cambia la pendiente. Los \(H_i\) son hermitianos porque los \(G_i\) lo son.

**(3) \(B_h\), inclinación, isotropía y el determinante.**  
\(E_h\) de rango uno implica que \(B_h=T^\dagger E_hT\) es hermitiana, semidefinida positiva y de rango a lo sumo uno, para cualquier isometría \(T\). La fórmula del proyector da, sin aproximación,

\[
B_h=\bigl[I+\sqrt3\sum_i h_i H_i\bigr]/4.
\]

Sin inclinación, \(\operatorname{tr} H_i=0\), luego \(\operatorname{tr} B_h=1/2\). Entonces \(H_i=a_i\cdot\sigma\) con \(a_i\in\mathbb{R}^3\) y

\[
M_{ij}=a_i\cdot a_j=\operatorname{tr}(H_iH_j)/2.
\]

Si \(b=\sum_i h_ia_i\), se tiene \(|b|^2=h^TMh\) y

\[
B_h=\bigl[I+\sqrt3\,b\cdot\sigma\bigr]/4,
\]

cuyos autovalores son \((1\pm\sqrt3\,|b|)/4\). Por tanto

\[
\det B_h=\bigl[1-3\,h^TMh\bigr]/16.
\]

Isotropía no degenerada: \(M=c^2I\) con \(c>0\). Como \(|h|^2=3\), \(h^TMh=3c^2\) y \(\det B_h=(1-9c^2)/16\). El factor \(9\) es \(3\times 3c^2\), no un \(|h|^2\) sustituido a mano.

**(4) Las dos vías.**  
En dimensión \(2\), rango \(\le 1\) equivale a determinante nulo. Luego \(1-9c^2=0\). Con \(c>0\), \(c=1/3\). La traza \(1/2\) excluye la compresión nula, pero no hace falta para esta implicación.

Segunda vía, con las mismas hipótesis. Rango uno, traza \(1/2\) y hermiticidad dan autovalores \(1/2\) y \(0\), así que \(\operatorname{tr}(B_h^2)=1/4\) y la suma sobre los cuatro vértices vale \(1\). Expandiendo (1) y usando \(\sum_h h_i=0\), \(\sum_h h_ih_j=4\delta_{ij}\),

\[
\sum_h\operatorname{tr}(B_h^2)=\frac12+\frac34\sum_i\operatorname{tr}(H_i^2).
\]

Isotropía: \(\operatorname{tr}(H_i^2)=2c^2\), suma \(6c^2\), y la expresión queda \(1/2+(9/2)c^2\). Igualar a \(1\) devuelve \(c^2=1/9\). Es la misma restricción, no una hipótesis distinta. El informe lo dice.

**(5) Hipótesis: se usan y bastan.**  
- Multiplicidad exactamente dos: \(B_h\) es \(2\times 2\). En dimensión mayor, rango \(\le 1\) no es «determinante cero».
- Separación: identifica la cuasienergía lineal con los \(H_i\). Sin ella, la cota algebraica sobre el subespacio sigue en pie, pero no hay doblete nodal aislado.
- Sin inclinación: la fórmula del determinante y \(\operatorname{tr} B_h=1/2\).
- Isotropía: hace constante \(h^TMh\). Sin ella el rango solo obliga a que \(M\) sea diagonal y de traza \(1/3\) (sale restando las cuatro ecuaciones \(h^TMh=1/3\)); caben conos anisótropos.
- No degenerado: sobra como hipótesis independiente. Las demás ya dan \(c=1/3\neq 0\), así que tampoco existe el caso isótropo hasta con \(c=0\). No es una escapatoria.
- \(W\in U(4)\): hace \(U(k)\) unitaria y el proyector ortogonal. No se usa ninguna forma especial de \(W\).

La desigualdad de rango vale para todo \(2\)-plano, no para una muestra de monedas. Casos límite que no escapan: complemento también doble, siempre que su autovalor sea distinto; cambio de base \(T\mapsto TV\), que conjuga los \(H_i\) y no cambia \(M\); cierre del hueco, que solo encoge el entorno donde manda el término lineal, no el coeficiente.

Corolario más fuerte que el informe, también a mano. Si se admite inclinación \(\tau_i=\operatorname{tr} H_i\) pero la parte sin traza sigue con \(M=c^2I\), el rango \(\le 1\) da

\[
\bigl(1+(\sqrt3/2)\,h\cdot\tau\bigr)^2=9c^2,
\]

y la positividad de \(B_h\) obliga al miembro sin cuadrado a ser \(+3c\), no \(-3c\). Entonces \(h\cdot\tau\) es constante en los cuatro vértices, luego \(\tau=0\) y \(c=1/3\). No hay cono isótropo inclinado en este desplazamiento, en \(k=0\), para un doblete de rango dos. El informe lo deja fuera; no lo afirma falso.

La clase no es vacía. En la base conjunta \(\{|h\rangle\}\), sean \(|\chi_h\rangle\) estados de qubit con vector de Bloch \(h/\sqrt3\) y

\[
T=\sum_h |h\rangle\langle\chi_h|/\sqrt2.
\]

Se comprueba \(T^\dagger T=I_2\) y \(T^\dagger G_iT=\sigma_i/\sqrt3\), luego \(H_i=\sigma_i/3\), \(M=I/9\), \(c=1/3\), traza nula. Cualquier \(W=z\,TT^\dagger+z'(I-TT^\dagger)\) con \(z\neq z'\) en el círculo realiza el doblete separado. Esto sustituye, para la no vacuidad, al constructor cíclico anterior, que no está en los documentos y no he comprobado.

**(6) Script y registro, solo por inspección.**  
No lo ejecuté. El registro tiene 55 líneas `PASS` y el script appende exactamente 55 comprobaciones, en este orden: \(4\times 4\) de proyectores, suma, tres momentos primeros, tres sumas de vértices de orden uno, nueve de orden dos, completitud comprimida, tres momentos comprimidos, y por cada vértice traza, determinante general e identidad \(2\times 2\), más pureza, cuatro especializaciones isótropas, acuerdo de obstrucciones y la raíz positiva. Las identidades que reconocí coinciden con lo derivado arriba; no puedo dar fe de la salida de SymPy más allá de esa concordancia de texto.

El script no cuantifica sobre \(W\), no menciona la separación ni el rango de \(T^\dagger E_hT\), y parte ya de \(H_i\) sin traza con nueve coeficientes reales. La comprobación llamada de obstrucción isótropa solo simplifica \((1-3h^T(c^2I)h)/16=(1-9c^2)/16\). La identidad \(2\times 2\) de traza y determinante es tautológica. `solve(1-9c^2)` no es el argumento de rango. La sección 5 del informe describe ese alcance y dice que los controles no sustituyen la prueba. Esa frase es correcta. Tratar 55/55 como demostración del enunciado universal sería un error; el informe no lo hace.

**(7) Alcance del informe.**  
La sección 4 no se sale del contrato: solo \(k=0\), este desplazamiento tetraédrico, doblete separado de multiplicidad dos, isotropía lineal y sin inclinación. No clasifica monedas, no impone las simetrías del constructor anterior y no afirma nada de otros nodos. La frase sobre la subclase irreducible es una restricción, no una ampliación. Que dos bloques así tengan ambos \(c=1/3\) es el mismo enunciado repetido.

## Objeciones

No hay. La separación espectral está escrita en una frase, pero el estimador de Schur cierra. La redundancia de «no degenerado» y el hecho de que el caso isótropo inclinado también muera por positividad no son fallos del enunciado: el informe no afirma lo contrario, solo no los incluye.

## Alcance que acepto

Para \(U(k)=W\prod_{i=1}^3\exp(-ik_iG_i/\sqrt3)\), \(G_i=\sigma_i\otimes\sigma_i\), \(W\in U(4)\): todo autovalor de \(U(0)\) de multiplicidad exactamente dos, separado, cuyo cono de cuasienergía de primer orden cumpla \(\operatorname{tr} H_i=0\), \(M=c^2I\) y \(c>0\), tiene \(c=1/3\) en las unidades del contrato (paso uno, duración uno, nodo en el origen). Además existe al menos un \(W\) que lo realiza, y no existe variante isótropa con deriva común \(\operatorname{tr} H_i\neq 0\).

No acepto el enunciado para otros desplazamientos, otras dimensiones, otros \(k\), conos anisótropos, multiplicidad distinta de dos, ni modelos con \(W\) dependiente de \(k\). Tampoco acepto los hashes, el commit base ni el informe cíclico previo: no están comprobados en esta sesión y la exclusión no depende de ellos.
