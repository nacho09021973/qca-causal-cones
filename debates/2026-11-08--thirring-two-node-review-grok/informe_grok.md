<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 e497e1d6b959955a09e7146f59456187876c3e8976a224cde16588dfebaf3ff3
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-08T13:25:33Z  fin: 2026-11-08T13:45:50Z
documento: /home/adnac/qca-causal-cones/theory/THIRRING_TWO_NODE_GATE.md ; último commit observado: fd1ef6c ; sha256 de la copia enviada 684290668d7e64f62e9aa1c75c55fc1e9103942ebff8729c63f01149bb8a27ac
documento: /home/adnac/qca-causal-cones/reports/2026-11-08--thirring-two-node.md ; último commit observado: 58a345b ; sha256 de la copia enviada 21141cabf7256fc86e6a0df545e987b17f2cda141174495deb38217270310881
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_two_node.py ; último commit observado: 20a78c4 ; sha256 de la copia enviada 2280cf0e37ca312e4ddf43fa8750d8ad1786bd876035f39c34d9d43c411f7e96
documento: /home/adnac/qca-causal-cones/sources/1804.08508v1.pdf ; último commit observado: 58a345b ; sha256 de la copia enviada 495646b1a0c0a2822422c4d65536b8c4caa0d82c5efe7e48df878766af91f0d0
entrada_grok.txt sha256 5789fccde1c129109e9e2bc25c1df2e864d2d73f127603f71762dee1cbf21247
respuesta sha256 0e51826e1c8ecc09c175914a1ebbc20ed0f13cf739f9d028ddb3412b974c9d0e
-->

La colisión de dos nodos, su entrelazamiento y su composición cuadran con una rederivación independiente. El no-go unitario también cuadra, pero solo para este código sin masa y estos recursos. El alcance de \(c_{IR}=a/\tau\) y lo que el verificador demuestra quedan por debajo de cómo puede leerse el informe. No ejecuté el código: leí el verificador y rehíce el álgebra a mano. Las cifras de coma flotante del informe quedan sin reproducir.

## Veredictos

| Bloque | Veredicto |
| --- | --- |
| 1. Signo, fase y orden \(FJ\) | **PASS** |
| 2. Fermiones idénticos y producto de modos | **PASS** |
| 3. Composición y tiempos de cruce | **PASS** |
| 4. Paridad, testigo de Hadamard, ancillas, escapatorias del contrato | **PASS** |
| 5. Dos nodos, portador de Floquet, momento y \(c_{IR}\) | **REPAIR_REQUIRED** |
| 6. Qué verifica el código y qué afirma el informe | **REPAIR_REQUIRED** |

El criterio de abandono del contrato se cumple para esta codificación: hay una restricción algebraica exacta. Eso no es un no-go del autómata de Thirring completo, del caso con masa ni de otra codificación.

## 1. Signo, fase y orden \(FJ\) — PASS

En Bisio et al., ec. (1), \(\mu=0\) y \(\nu=1\) dejan la caminata diagonal: \(\uparrow\) se desplaza con \(T_x^\dagger\) y \(\downarrow\) con \(T_x\). Con \(T_x|x\rangle=|x+1\rangle\), la primera componente es la que se mueve a la izquierda. El informe pone el derecho \(R\) primero, con \(W(k)=\mathrm{diag}(e^{-ik},e^{ik})\), y lo declara. La interacción \(n_R n_L\) es simétrica, así que el intercambio de etiqueta no cambia la fase de colisión.

El artículo define \(U=WV\), interacción y después caminata libre. Eso es el \(U=FJ\) del informe: \(J\) y luego \(F\).

Si \(R\) sale de \(x\) y \(L\) de \(y\), antes del salto del paso \(t\) están en \(x+t\) y \(y-t\). Coinciden solo si \(y-x\) es par, en el único instante \(t=(y-x)/2\). En la recta no vuelven a coincidir. Cada configuración de posiciones recibe \(e^{i\chi}\) o \(1\), según la paridad relativa.

En el paquete de \(2M\) sitios consecutivos hay \(M\) pares y \(M\) impares, así que
\[
|0\rangle=\frac{|e\rangle+|o\rangle}{\sqrt{2}},\qquad
|1\rangle=\frac{|e\rangle-|o\rangle}{\sqrt{2}},
\]
con \(|e\rangle,|o\rangle\) los soportes uniforme par e impar. \(\Pi\) actúa como \(X\) lógico. La misma paridad es el sector \(XX=+1\) y recibe \(e^{i\chi}\); la opuesta recibe \(1\). Por tanto
\[
S_\chi=e^{i\chi(1+X_R X_L)/2}
=\frac{1+e^{i\chi}}{2}\,I+\frac{e^{i\chi}-1}{2}\,X_R X_L.
\]
En la base \(00,01,10,11\) la matriz es la del informe. Equivale a \(e^{i\chi/2}\exp(i\chi X_R X_L/2)\).

Comprobación directa, \(M=1\), soportes \(\{0,1\}\) y \(\{2,3\}\). Solo coinciden \((0,2)\) y \((1,3)\), en \(t=1\). Proyectar el estado fasado de \(|00\rangle\) da
\[
\langle00|S|00\rangle=a,\qquad\langle11|S|00\rangle=b,\qquad\langle01|S|00\rangle=\langle10|S|00\rangle=0,
\]
con \(a=(1+e^{i\chi})/2\) y \(b=(e^{i\chi}-1)/2\). En \(\chi=\pi\), \(a=0\), \(b=-1\), luego \(S=-X_R X_L\). El signo que el primer test comparaba con \(+XX\) era un error del test; la corrección \(a=0\), \(b=-1\) es la correcta.

Sobre \(|00\rangle\) los coeficientes de Schmidt son \(|\cos(\chi/2)|\) y \(|\sin(\chi/2)|\). La concurrencia es \(2|ab|=|\sin\chi|\). Máxima en \(\chi=\pi/2\), nula en \(0\) y en \(\pi\). En \(\chi=\pi/2\) el estado es \(e^{i\pi/4}(|00\rangle+i|11\rangle)/\sqrt{2}\).

El factor \(Z^T\) por paquete aparece solo si \(\Pi\) se redefine con \((-1)^x\) en las coordenadas nuevas: el nodo \(1\) transportado recoge \((-1)^T\). En el marco que descuenta \(F^T\) y compara con los modos iniciales, ese factor no está. Las dos fórmulas del verificador cubren los dos marcos. Conmutan con \(S_\chi\).

Al cerrar el cruce, \(S_\chi\) deja invariante el código para todo \(M\). La fuga de un cruce completo es exactamente cero. Durante el cruce la fase depende del sitio concreto, no solo de su paridad, y la compresión deja de ser unitaria. Eso no altera la matriz final.

## 2. Fermiones idénticos y producto tensorial — PASS

\(R\) y \(L\) son modos distintos. El estado de un paquete de cada tipo es \(\sum\phi(x)\psi(y)\,a^\dagger_{R,x}a^\dagger_{L,y}|0\rangle\). El automorfismo \(F a^\dagger_{R,x} F^{-1}=a^\dagger_{R,x+1}\), y el análogo para \(L\), actúa sobre ese monomio sin un signo de más: el orden de etiqueta se conserva aunque el orden espacial cambie.

Ese signo sí aparecería al reescribir el estado en el orden canónico por sitio. El contrato fija la lectura por etiqueta de paquete. Con esa lectura el signo de intercambio no es una puerta. El propagador antisimétrico de dos cuerpos, con \(\Psi\mapsto(\phi_R\otimes\phi_L-\phi_L\otimes\phi_R)/\sqrt{2}\) y soportes de espín disjuntos, calcula el mismo \(S_\chi\) y el mismo \(Z^T\). No hay un signo relativo escondido entre \(|01\rangle\) y \(|10\rangle\).

Dos paquetes de la misma componente, con soportes disjuntos y la misma velocidad, siguen disjuntos. Sus operadores se trasladan en paralelo y el orden de etiqueta no se cruza. El producto lógico de tres paquetes es el producto de creación en ese orden. \(J\) solo aporta \(e^{i\chi}\) por cada par \(R\)-\(L\) que ocupa el mismo sitio; con un fermión por paquete ese número es \(0\) o \(1\).

La ortonormalidad pedida es exacta: soportes disjuntos, y dentro de un paquete \(\sum(-1)^x=0\) porque hay tantos pares como impares.

## 3. Composición y tiempos — PASS

Geometría del informe: \(R\) en \([-8M,-6M-1]\), \(L_1\) en \([0,2M-1]\), \(L_2\) en \([8M,10M-1]\).

- \(R\) con \(L_1\): diferencias pares desde \(6M+2\) hasta \(10M-2\), tiempos \(t\in[3M+1,5M-1]\).
- \(R\) con \(L_2\): tiempos \(t\in[7M+1,9M-1]\).
- \(L_1\) y \(L_2\) no se cruzan.

Con \(T\) pasos se aplican \(t=0,\ldots,T-1\). En \(T=6M+1\) el último tiempo es \(6M\): el primer cruce ya terminó en \(5M-1\) y el segundo no ha empezado, porque empieza en \(7M+1\). En \(T=10M+1\) el último tiempo es \(10M\) y ambos cruces han terminado. El caso de dos paquetes, salidas \(\pm4M\) y \(T=5M+1\), cierra el único cruce, cuyos tiempos caen en \([3M+1,5M-1]\).

Cada par opuesto aporta un factor \(\exp[i\chi(1+X_i X_j)/2]\) al completar su cruce. Esos operadores conmutan: toda cadena de \(X\) conmuta con toda cadena de \(X\). Da igual que las ventanas se solapen. El producto no sale del grupo abeliano generado por \(\{X_i X_j\}\). La geometría de la recta solo permite un cruce por par opuesto y ninguno entre paquetes de la misma componente.

Un paquete solo, leído con \(\Pi\) en el sitio nuevo, recoge \(Z^T\). Una ancilla en \(|+\rangle_X\) o \(|-\rangle_X\), al cruzar, deja en el dato
\[
e^{i\chi/2}\exp(\pm i\chi X/2)
\]
y se factoriza. El eje es el de \(X\), y el ángulo es el \(\chi\) fijo de esa ejecución. Prepararla es recurso inicial del contrato, no una puerta hecha por \(U\).

## 4. Obstrucción — PASS

Sea \(G\) el conjunto de unitarias lógicas generadas por \(Z_i\) independientes, rotaciones \(\exp(i\alpha X_i)\) de ángulo arbitrario y \(\exp(i\theta X_i X_j)\) de ángulo arbitrario. El conjunto físico es más pequeño: \(\chi\) fijo, un solo cruce por par, \(Z^T\) común a todos los paquetes si se lee \((-1)^x\) en el retículo, y rotaciones \(X\) solo de ángulo \(\pm\chi/2\) mediante ancillas \(|\pm\rangle\).

En \(G\), cada elemento cumple \(V^\dagger X_i V=\pm X_i\) con el signo numérico, no un operador. Las rotaciones \(X\) y los \(XX\) conmutan con todos los \(X_i\). Cada \(Z_i\) cambia el signo de su \(X_i\). Por inducción lo cumple todo producto.

Consecuencia: si \(X_i|\Psi\rangle=\lambda|\Psi\rangle\), entonces \(X_i V|\Psi\rangle=\pm\lambda V|\Psi\rangle\). El dato de paridad definida sigue teniendo paridad definida. Si el estado global es autoestado de \(X_{\mathrm{dato}}\otimes I\), es un producto \(|\lambda\rangle\otimes|\mathrm{resto}\rangle\). Descartar la ancilla no crea coherencia entre paridades. Una ancilla inicial independiente, aunque no sea autoestado de \(X\), queda cubierta: el dato definido sigue siendo autoestado después de cualquier elemento de \(G\).

Eso prohíbe la Hadamard lógica. \(H|+\rangle=|0\rangle=(|+\rangle+|-\rangle)/\sqrt{2}\). Cualquier salida admitida es \(e^{i\alpha}|+\rangle\) o \(e^{i\alpha}|-\rangle\), con fidelidad \(1/2\) frente a \(|0\rangle\). La distancia de traza \((1/2)\|\rho-\sigma\|_1=\sqrt{1-|\langle\psi|\phi\rangle|^2}\) vale exactamente \(1/\sqrt{2}\) en ese caso, así que la cota del informe es saturada por la identidad. No baja al crecer \(M\) ni al añadir cruces o ancillas.

En la base de paridades, \(G\) está formado por fases diagonales y por inversiones de bits \(s\mapsto s+c\). Es un subgrupo cerrado propio de \(U(2^n)\): el componente conexo tiene dimensión \(O(n^2)\) por las fases a lo sumo cuadráticas en los valores \(\pm1\), frente a \(4^n-1\) de \(SU(2^n)\). No es denso.

La vía microscópica cierra las escapatorias que el contrato aún dejaría abiertas. Con \(\mu=0\), \(F\) permuta los modos y \(J\) es diagonal en ocupación. En las coordenadas iniciales,
\[
F^{-T}U^T=\prod_{t=0}^{T-1} F^{-t}JF^{t}
\]
es diagonal: multiplica cada configuración por la fase de los contactos ya ocurridos. \(\Pi_i\), multiplicar por \((-1)^{x_i}\), también es diagonal, luego conmuta con esa fase incluso a medio cruce. El proyector del código conmuta con \(\Pi_i\) porque \(\Pi\) deja invariante \(\mathrm{span}\{f,\Pi f\}\) y su ortogonal. La compresión \(K(T)\) cumple \([K(T),X_i]=0\). Esperar, salir del código mientras los paquetes se solapan y volver a proyectar no produce la Hadamard. Todas esas compresiones son diagonales en la base \(X\) y conmutan entre sí.

Escapatorias que siguen cerradas dentro del contrato:

- Postselección sobre no haber fugado. El contrato la prohíbe, y además el proyector del código conmuta con \(X\), así que tampoco mezclaría paridades.
- Variar \(\chi\) entre ejecuciones. Sigue siendo un ángulo \(XX\); el sobreconceso ya admite todos los ángulos.
- Segunda pasada, si se doblara la recta en un anillo. Otro factor \(XX\), el mismo eje.
- Medida final ideal en la base del código, incluso absorbiendo una capa local final en la lectura, más preparación inicial arbitraria del código. El tramo generado por \(U\) seguiría siendo un circuito que conmuta, de fases \(X\) y \(XX\), más un \(Z^T\) global. Eso no aproxima una Hadamard intercalada ni es denso en \(U(2^n)\).
- Ancilla en \(|0\rangle=(|+\rangle+|-\rangle)/\sqrt{2}\). Sobre un dato de paridad definida el factor se queda en la ancilla; sobre un dato en superposición, \(S_\chi\) solo pone fases en la base \(X\). Las poblaciones de paridad no pasan de \((1,0)\) a \((1/2,1/2)\).

La prueba usa \(\mu=0\) en el momento en que dice que \(F\) permuta cada quiralidad por separado. No se extiende al modelo con masa.

## 5. Dos nodos, Floquet, momento y \(c_{IR}\) — REPAIR_REQUIRED

La dispersión libre del verificador es una identidad: \(W(\pi+q)=-W(q)\) porque \(e^{\pm i(\pi+q)}=-e^{\pm iq}\). Cerca de \(0\), y de hecho para todo \(q\), \(W(q)=\exp(-iq\sigma_z)\) con \(\sigma_z=\mathrm{diag}(1,-1)\). Quitar el portador \((-1)^t\) al nodo \(\pi\) deja exactamente \(W(q)^t\). En dos pasos, \(W(\pi+q)^2=W(q)^2\). No hace falta identificar la cuasienergía \(\pi/\tau\) con una energía de un único hamiltoniano, y el informe no lo hace.

La transformada del paquete uniforme, con el convenio \((2\pi)^{-1/2}\sum_x e^{-ikx}f(x)\) del artículo, es
\[
|\widehat f_s(k)|^2=\frac{\sin^2(Mk)}{4\pi M\sin^2(k/2)}.
\]
Para \(\Lambda\in(0,\pi)\) y \(|k|\in[\Lambda,\pi]\), \(\sin^2(k/2)\ge\sin^2(\Lambda/2)\), y la medida de esa región es como máximo \(2\pi\). La cola cumple
\[
\int_{|k|>\Lambda}|\widehat f|^2\,dk\le\min\Bigl(1,\frac{1}{2M\sin^2(\Lambda/2)}\Bigr).
\]
\(\Pi\) traslada la densidad en \(\pi\). Con \(\Lambda\) fijo en \((0,\pi/2)\) los dos entornos se separan, y cualquier superposición de dimensión fija concentra su masa \(L^2\) en la unión de los nodos por la desigualdad triangular. A \(M\) finito la cola no es cero. El uso de la FFT como diagnóstico, no como prueba, respeta el contrato.

Restaura \(x_{\mathrm{phys}}=ax\) y \(t_{\mathrm{phys}}=\tau t\). Cada envolvente, la del nodo \(0\) y la del nodo \(\pi\) después de sacar \((-1)^{x+t}\), cumple el transporte quiral a velocidad \(a/\tau\). \(U^\dagger n_R(x)U=n_R(x-1)\) porque \(J\) conmuta con \(n_R(x)\) y \(F\) lo traslada; lo análogo vale para \(L\). El cono microscópico es exactamente una celda por paso, saturado, no una cota holgada. En una partícula la velocidad de grupo también es \(a/\tau\) en todo el círculo. El informe no calcula la de muchas cuerpos, y no deduce covariancia de Lorentz ni una QFT interactuante. La fase lógica \(S_\chi\) no tiende a \(I\) cuando \(M\) crece: es independiente de \(M\).

**Objeción 1.** \(c_{IR}=a/\tau\) es la velocidad de esas envolventes libres, y \(\alpha=1\) solo dice que coincide con la velocidad causal en esta normalización. El qubit del código es la coherencia entre el nodo \(0\) y el nodo \(\pi\). \(\Pi\) transfiere momento \(\pi\), que es la escala del retículo. \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt{2}\) está soportado en los sitios pares: oscila a la escala de la celda. No es una envolvente lenta. Llamar infrarrojo a este código mezcla la cinemática de cada nodo por separado con un grado lógico ultravioleta, el doblaje de fermión.

**Objeción 2.** La igualdad \(V_{\mathrm{causal}}^{\max}=V_{\mathrm{grp}}^{\max,1p}=c_{IR}=a/\tau\) es la traslación quiral sin masa escrita tres veces. No aporta evidencia sobre una relación entre computación universal y cono emergente. El propio informe lo separa de la universalidad; hay que dejarlo así de estrecho para que no se reutilice como resultado más fuerte.

**Reparación obligatoria R1.** En la sección 6 y en el veredicto, escribir que \(c_{IR}=a/\tau\) es la velocidad de cada envolvente libre una vez retirado el portador del nodo \(\pi\); que el qubit \(0/\pi\) no es un grado de libertad infrarrojo; y que no se ha aislado un cúbit lógico de baja cuasienergía. Mantener la negativa a deducir una QFT interactuante.

## 6. Código e informe — REPAIR_REQUIRED

Leído el fuente, sin ejecutarlo, el propagador de trayectorias y el propagador antisimétrico no insertan la puerta predicha en la evolución. La comparación posterior sí usa `gate`. Para dos cuerpos son dos implementaciones distintas y la matriz que contrastan es la que sale de la sección 1. Los tiempos de `composition_checks` son los de la sección 3. El número de llamadas a `check` es 228: 49 son gramianos, 64 el mapa de dos paquetes, 36 el sector antisimétrico, 64 la composición, 3 el cruce parcial, 6 la obstrucción y 6 la parte física. El denominador coincide con el informe. El numerador «228 pasaron», y los errores \(1.37\times10^{-15}\), \(6.60\times10^{-16}\), \(1.53\times10^{-15}\), \(2.26\times10^{-30}\) y la fuga \(0.46875\), son cifras del autor; aquí quedan sin reproducir. Contar `check` no los certifica.

**Objeción 3.** El no-go no está verificado por esos 228 tests. `H-witness-both-parities-fidelity-one-half` calcula \(|\langle+|H|+\rangle|^2\) y \(|\langle-|H|+\rangle|^2\). No aplica ninguna \(U\), ninguna ancilla ni ningún cruce. Un código que implementara la Hadamard seguiría pasando ese test. El test monomial cubre una sola palabra del sobreconceso, no el grupo. El test de ancilla cubre un estado producto y un solo \(XX\). La frase «la obstrucción general se deduce del álgebra» es la que sostiene el resultado; el recuento de tests no.

**Objeción 4.** El propagador antisimétrico es de dos fermiones, anillo de 64 sitios, \(M=1,2,3\), y aparta los tiempos del borde. La composición de tres paquetes está solo en el producto tensorial de trayectorias. El argumento de la sección 2 justifica esa sustitución, pero el informe no debe leerse como si el sector de Fock de tres cuerpos hubiera sido propagado.

**Objeción 5.** «Fuga máxima \(0.46875\)» es un punto, \(M=4\), \(T=17\), \(\chi=\pi/2\), no un máximo demostrado sobre tiempos y tamaños. La afirmación que sí queda demostrada sin ese número es otra: a medio cruce \([K,X_i]=0\), aunque \(K\) no sea unitaria.

El informe acierta al marcar PRELIMINARY, al no vender los residuos flotantes como cotas certificadas y al no deducir la QFT interactuante. Se pasa de lo que el verificador hace en cuanto el veredicto conjunto parece apoyado por «228/228» y en cuanto \(c_{IR}\) se deja leer como sector computacional infrarrojo.

**Reparación obligatoria R2.** Separar en el informe y en el registro del verificador tres clases: contraste de \(S_\chi\) y de la composición; ilustraciones que no podrían fallar si el no-go fuera falso; y consecuencias que solo salen del álgebra. Quitar al testigo de Hadamard la apariencia de haber ejecutado una puerta.

**Reparación obligatoria R3.** Declarar en la sección 7 que la antisimetrización comprobada es de dos cuerpos, y que tres paquetes se comprobaron como trayectorias en orden de etiqueta. No hace falta retirar la composición si se mantiene esa frase.

**Reparación obligatoria R4.** Sustituir «fuga máxima \(0.46875\)» por «fuga en el caso \(M=4\), \(T=17\), \(\chi=\pi/2\)», o calcular el máximo que realmente se quiera afirmar.

## Qué queda demostrado, y dónde

Para el código declarado —un cúbit por paquete, \(X=\Pi\), \(\mu=0\), \(\chi\) fijo, sin monedas, espejos, medidas intermedias ni postselección— la colisión completa es exactamente \(S_\chi\), fuga cero, entrelaza cuando \(\sin\chi\neq0\), y los cruces completos se componen mediante factores \(XX\) que conmutan. Con esos recursos, y aun concediendo el sobreconceso de la sección 5 del informe, no hay un conjunto unitario denso en \(U(2^n)\). El testigo de un cúbit ya lo impide.

Eso es un cierre de esta codificación sin masa. No alcanza al autómata con \(\mu\neq0\), donde la caminata mezcla quiralidades, aparecen los saltos de momento entre zonas de Brillouin y los estados ligados del artículo, y \(F^{-T}U^T\) deja de ser diagonal en la posición inicial. Tampoco alcanza a otra codificación, a programas iniciales entrelazados con los datos, ni a medidas intermedias. La existencia de una QFT de Thirring relativista interactuante sigue sin estar construida: harían falta vacío, renormalización y límite, y el artículo primario resuelve el sector de dos partículas del autómata discreto, no ese límite.

## Hipótesis que habría que cambiar para seguir

Habría que abandonar al menos una de las hipótesis que hacen diagonal a la evolución en el marco comóvil: pasar a \(\mu\neq0\), o cambiar el observable lógico para que no sea la paridad \(\Pi\) de cada paquete, o admitir recursos que el contrato excluye (moneda, \(\chi\) variable en el tiempo, medida intermedia). Cualquiera de esos cambios deja sin validez esta obstrucción. Ninguno, por sí solo, produce un conjunto universal ni un sector relativista interactuante; eso exigiría otro contrato y otra prueba. No hay en estos documentos una vía alternativa ya demostrada.
