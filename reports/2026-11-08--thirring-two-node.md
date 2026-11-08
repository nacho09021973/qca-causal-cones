# Thirring sin masa: dos nodos cierran la colisión, pero no dan puertas universales

2026-11-08. Autor: Codex (OpenAI). **PRELIMINARY: derivación y verificaciones
del autor, sin revisión independiente ni promoción.**

Contrato previo al cálculo: [THIRRING_TWO_NODE_GATE.md](../theory/THIRRING_TWO_NODE_GATE.md),
commit `fd1ef6c`. Autorización: «adelante, estas autorizado para hacer el experimento
completo», referida al experimento de código, colisión, composición y sector relativista.

## 1. Resultado y alcance

Se completaron los cuatro puntos del experimento para la continuación **sin masa**
de la primera colisión. El qubit es ahora el nodo 0/pi de un paquete, no el par
de posiciones de la nota anterior.

| Pregunta | Resultado de autor |
| --- | --- |
| ¿Código ortonormal con ambos nodos? | Sí, exactamente para los paquetes definidos abajo. |
| ¿Colisión completa sin fuga del código? | Sí: S_chi = a I + b X tensor X. |
| ¿Entrelaza? | Sí para sin(chi) distinto de cero; máximo en chi=pi/2. |
| ¿Se componen colisiones? | Sí para cruces completos; se demuestra la fórmula multipaquete y se comprueba una secuencia con tres partículas. |
| ¿Computación cuántica universal con esos recursos? | No en este código: las paridades de las trayectorias impiden una Hadamard lógica. |
| ¿Sector libre relativista? | Dos envolventes de Dirac sin masa con la misma velocidad a/tau, retirando el portador de Floquet del nodo pi. |
| ¿QFT interactuante relativista / procesador universal relativista? | No demostrados. La primera afirmación no se deduce de la cinemática libre; la segunda falla para el código y recursos probados. |

Veredicto: `TWO_NODE_COLLISION_CLOSED_AND_ENTANGLING /
MASSLESS_NODE_CODE_NOT_UNITARILY_UNIVERSAL`. Se activa el criterio de cierre
algebraico del contrato. No es un no-go del Thirring masivo, de todas las
codificaciones ni de toda coexistencia entre relatividad y computación universal.

## 2. Modelo, preparación y lectura

Z, dos modos fermiónicos R,L por celda, Fock local de dimensión 4. La regla fija es

\[
 U=FJ,\qquad J=\prod_x e^{i\chi n_R(x)n_L(x)}.
\]

F mueve R una celda a la derecha y L una a la izquierda; mu=0. Chi es fijo durante
cada ejecución. Comparar chi=0,0.7,pi/2,pi significa comparar reglas, no disponer
de un control temporal del acoplamiento. Es el límite sin masa del modelo primario
de [1], PDF p.3, Ec.(1) y sección 3; orientación R/L escogida por su desplazamiento.

Para un entero M>=1,

\[
 f_s(x)=(2M)^{-1/2}{\bf1}_{[s,s+2M-1]}(x),\quad
 \Pi f(x)=(-1)^x f(x),\quad |0\rangle_s=f_s,\ |1\rangle_s=\Pi f_s.
\]

Son ortonormales: cada soporte tiene M sitios pares y M impares. En el código,
Pi es el Pauli X. Los estados |+>=(|0>+|1>)/sqrt(2) y
|->=(|0>-|1>)/sqrt(2) tienen soporte únicamente par e impar, respectivamente.

Cada paquete tiene componente fija. Paquetes con la misma componente tienen
soportes disjuntos, que siguen disjuntos porque se trasladan con la misma velocidad.
El producto tensorial lógico se incrusta por productos de operadores de creación
en orden de **etiqueta de paquete**, sin reordenarlos cuando se cruzan espacialmente.
Así se evita introducir un signo de intercambio ficticio como puerta.

Se concede preparación inicial ideal de estos modos y lectura final ideal en el
código. No se ha construido un dispositivo autónomo para prepararlos o leerlos.
Una transformación usada al definir o medir la base no cuenta como puerta
intermedia generada por U. Se excluyen medidas adaptativas, postselección,
monedas externas, espejos y cambios de masa.

## 3. Colisión exacta y entrelazamiento

Si R parte en x y L en y>x, coinciden en un sitio si y solo si y-x es par, en
t=(y-x)/2. Aplicamos J en t=0,...,T-1 antes de cada traslado. Una vez completo
el cruce de todos los componentes de los paquetes, cada trayectoria con paridad
igual ha recibido una fase e^{i chi}; las de paridad distinta ninguna.

Descontando F^T matemáticamente, el operador exacto es

\[
 S_\chi=e^{i\chi(1+\Pi_R\Pi_L)/2}
 =aI+b\Pi_R\Pi_L,\quad
 a=\frac{1+e^{i\chi}}2,\quad b=\frac{e^{i\chi}-1}2.
\]

El código es invariante bajo cada Pi, por lo que la fuga al terminar el cruce
es exactamente cero, para todo M. En orden lógico 00,01,10,11:

\[
 S_\chi=\begin{pmatrix}
 a&0&0&b\\0&a&b&0\\0&b&a&0\\b&0&0&a
 \end{pmatrix}
 =e^{i\chi/2}\exp\left(i\frac\chi2 X_R X_L\right).
\]

Sobre |00> da a|00>+b|11>. Los coeficientes de Schmidt son |a| y |b|;
la concurrencia es 2|ab|=|sin chi|. En chi=pi/2, el estado es
e^{i pi/4}(|00>+i|11>)/sqrt(2), con entrelazamiento máximo.
En chi=0 es identidad; en chi=pi es **-X_R X_L**, un producto local con fase
global, y no entrelaza. Ambos límites se verificaron.

Convención de salida: si se usan como modos finales f_{s+vT}, Pi f_{s+vT},
en lugar de trasladar cada modo inicial, aparece Z^T por paquete, porque
T_v Pi=-Pi T_v. La comprobación fermiónica incluye este factor. No confundir
un cambio de marco o una convención de lectura con un control físico adicional.

La ausencia de fuga se afirma **al completar el cruce**. Durante el encuentro
pueden correlacionarse paridad y forma espacial; la proyección sobre los mismos
cuatro modos no es una puerta unitaria. Un caso intermedio del verificador
(M=4,T=17,chi=pi/2) da fuga máxima 0.46875.

## 4. Composición y puertas de un qubit

Para n paquetes de componente fija, cada configuración de posiciones iniciales
sigue una trayectoria fija. Las fases de contacto de pares se multiplican.
Si E es el conjunto de pares R/L cuyos cruces se han completado (los demás aún
no han empezado),

\[
 S_E=\prod_{(i,j)\in E}\exp\left[i\chi(1+X_iX_j)/2\right].
\]

Todos los factores conmutan, incluso cuando comparten un paquete. El orden de
colisiones no genera un segundo eje lógico. La geometría real restringe además
E: paquetes de la misma componente no se cruzan y cada par opuesto se encuentra
a lo sumo una vez en la recta. No se afirma un enrutamiento arbitrario.

Prueba explícita: R en -8M, L_1 en 0, L_2 en 8M; todas las anchuras 2M.
En T=6M+1 ha terminado solo el primer cruce; en T=10M+1, ambos.
La evolución directa reproduce S_01 y S_02 S_01 para M=1,2,4,8 y los cuatro
acoplamientos del contrato. Los dos paquetes L son modos ortogonales de fermiones
idénticos: las etiquetas representan soportes disjuntos persistentes, no especies
distinguibles añadidas.

Un paquete aislado solo se traslada: en el marco natural produce Z^T, no una
rotación arbitraria. Una ancilla preparada en |+> o |->, eigenestado de X,
puede producir sobre el dato una rotación exp(+-i chi X/2), salvo fase global,
al cruzarlo. Este recurso también conserva el eje X. Preparar esa ancilla es
un recurso inicial concedido, no una prueba de preparación autónoma.

## 5. Obstrucción exacta a universalidad en este código

Primera vía: las colisiones conmutan con todos los X_i. Las posibles Z_i de
traslación solo invierten sus signos. Incluso concediendo **más** recursos que
los físicos —Z_i independientes, rotaciones X_i arbitrarias y colisiones XX
de cualquier ángulo—, cada unidad lógica satisface

\[
 V^\dagger X_i V=\pm X_i.
\]

En la base de paridad es una matriz monomial con permutaciones restringidas a
inversiones de bits; no puede mezclar coherentemente dos paridades de entrada.
Esta familia cerrada no es densa en U(2^n).

Testigo cuantitativo: H|+>=|0> tiene probabilidades de paridad (1/2,1/2),
mientras que cualquier operación admitida lleva el dato de paridad definida
a paridad definida. Su fidelidad con ese objetivo es como máximo 1/2 y la
distancia de traza (convención ||rho-sigma||_1/2) es al menos 1/sqrt(2).
La cota no disminuye al ensanchar los paquetes ni al añadir cruces.

Ancillas inicialmente independientes no reparan esto: para datos de paridad
definida, una unitaria diagonal en las paridades conjuntas deja fija la paridad
del dato, incluso si luego se descarta la ancilla. Las inversiones Z cambian
solo el signo. Se sigue la misma trayectoria de datos, sin sustituirla por una
ancilla preparada con la respuesta; no se concede una codificación nueva.

Segunda vía, microscópica: mu=0 hace de F una permutación fija de los modos
ocupados, y J es diagonal en sus ocupaciones. En coordenadas que siguen las
trayectorias, F^{-T}U^T es diagonal en las posiciones iniciales y conmuta con
cada Pi_i. Esta afirmación vale también en colisiones parciales, donde el código
puede tener fuga. Como el proyector del código conmuta con Pi_i, su compresión
también conmuta con X_i. Por tanto, esperar tiempos intermedios, permitir
deformaciones temporales y recuperar después el código no evita la obstrucción.

Esto completa el criterio de abandono declarado: **el código de nodos probado
no implementa un conjunto unitario universal con la evolución autónoma sin masa**.
No es un resultado sobre otra codificación no local, computación con medidas,
programas inicialmente entrelazados con los datos, ni masa no nula. La prueba
microscópica usa explícitamente mu=0; no se extrapola al modelo masivo.

## 6. Dos nodos y velocidad relativista: qué se obtiene

Con Fourier e^{ikx}, el paso libre empleado en el verificador es

\[
 W(k)=\operatorname{diag}(e^{-ik},e^{ik}),\quad W(\pi+q)=-W(q).
\]

Esta convención intercambia la orientación de componentes respecto a [1];
la dispersión y la colisión no cambian. Cerca de 0, W(q)=exp(-i q sigma_z).
Cerca de pi, retirar el factor de portador (-1)^t da la misma evolución.
En dos pasos se pliegan ambos nodos: W(pi+q)^2=W(q)^2. No se debe identificar
sin más cuasienergía pi/tau con una energía positiva infinita, ni afirmar que
se ha construido un vacío de baja energía de un Hamiltoniano único.

La concentración de los paquetes es controlable sin un ajuste numérico:

\[
 |\widehat f_s(k)|^2=\frac{\sin^2(Mk)}{4\pi M\sin^2(k/2)},\qquad
 \int_{|k|>\Lambda}|\widehat f_s(k)|^2dk
 \leq\min\left(1,\frac{1}{2M\sin^2(\Lambda/2)}\right).
\]

Pi desplaza esta distribución en pi. Para Lambda fijo en (0,pi/2), cada modo
se concentra en su nodo cuando M crece; por linealidad lo hace cualquier
superposición normalizada en un código de dimensión fija, alrededor de la
unión de nodos. Los modos no son estrictamente limitados en momento a M finito.
El programa incluye diagnósticos FFT, no los usa como prueba del límite.

Restaurando espacio x_phys=a x y tiempo t_phys=tau t, las envolventes libres
satisfacen el transporte de Dirac sin masa

\[
 (\partial_{t_{\rm phys}}+v\partial_{x_{\rm phys}})\phi_R=0,\quad
 (\partial_{t_{\rm phys}}-v\partial_{x_{\rm phys}})\phi_L=0,
 \qquad v=a/\tau.
\]

Son ecuaciones de las envolventes libres (mu=0), no una demostración de
covariancia Lorentz de toda la dinámica discreta interactuante. La fase de
colisión finita persiste al crecer M, pero no se han construido un vacío,
renormalización ni convergencia a una QFT interactuante relativista. La
obstrucción computacional ya cierra el candidato sin necesitar esa promoción.

Geometría y velocidades con esta normalización:

- Vecindario espacial del paso: {-1,+1}; C_micro=[-1,+1]. Soporte h(u)=|u|,
  inradio 1, en unidades de celda/paso.
- V_causal^max=a/tau. No es solo una cota: U^dagger n_R(x) U=n_R(x-1), y
  análogamente para L, de modo que la dependencia alcanza +-t tras t pasos.
- V_grp^{max,1p}=a/tau en el sector de una partícula; no se ha calculado una
  velocidad de grupo de todas las excitaciones de muchos cuerpos.
- c_IR=a/tau para las dos envolventes libres identificadas. Aquí alpha=1.

La igualdad de estas cantidades en este caso procede de la traslación quiral
sin masa. **No procede de universalidad computacional**, que no se obtiene.
Tampoco determina a o tau por separado ni una frecuencia absoluta de reloj.

## 7. Verificación, reparación y procedencia

Implementación permanente: [verify_thirring_two_node.py](../scripts/verify_thirring_two_node.py).
Se versionó antes de ejecutarla (`578f27c`). Ejecución final con código
`20a78c4`, Python 3.12.3, NumPy 2.4.4, sin aleatoriedad:

```sh
/home/adnac/venvs/torch-gpu/bin/python scripts/verify_thirring_two_node.py
```

Resultados: [JSON](2026-11-08--thirring-two-node.json),
[registro](2026-11-08--thirring-two-node-verifier.txt). **228/228 comprobaciones**.

| Comprobación | Máximo observado |
| --- | ---: |
| Error de matriz, trayectorias de dos paquetes | 1.37e-15 |
| Error de matriz, espacio antisimétrico fermiónico | 6.60e-16 |
| Error de matriz, composición de tres paquetes | 1.53e-15 |
| Fuga máxima al cerrar los cruces | 2.26e-30 |

Son residuos de coma flotante; no cotas certificadas del error numérico.
La fuga exactamente nula y la obstrucción general se deducen del álgebra.
El test antisimétrico usa anillo de 64 sitios, M=1,2,3 y tiempos sin contacto
con la frontera; no depende de un ajuste de tamaño finito. Los otros métodos
son evolución directa de coincidencias sobre soportes finitos en la recta.
Son dos implementaciones del autor, no revisión independiente.

Primer intento: 225/226. La expectativa del test chi=pi omitía el signo global:
comparaba con +XX en lugar de -XX. Se rederivó a=0,b=-1, se corrigió el test
y se añadieron dos verificaciones de paridad en el cruce parcial. No se cambió
la regla física ni el resultado. Se conservaron [salida fallida](2026-11-08--thirring-two-node-initial-failed.txt)
y [datos fallidos](2026-11-08--thirring-two-node-initial-failed.json), que registran
el hash del script inicial. El registro final contiene hashes de script,
contrato, PDF primario y nota de partida.
La nota de partida sigue siendo un fichero del usuario no versionado: su hash
se registra si está disponible, pero no es una entrada necesaria del cálculo.

## 8. Fuentes y decisión

[1] Bisio, D'Ariano, Mosco, Perinotti, Tosini,
*Solutions of a two-particle interacting quantum walk*, arXiv:1804.08508v1,
[PDF original](https://arxiv.org/pdf/1804.08508v1), conservado en
`sources/1804.08508v1.pdf`: pp.3–6 leídas en esta sesión, especialmente
p.3 Ec.(1), Ec.(2), sección 3 y pp.5–6 Ec.(8). SHA256:
`495646b1a0c0a2822422c4d65536b8c4caa0d82c5efe7e48df878766af91f0d0`.
Se usa para la definición y simetría del modelo, no como fuente de nuestra
afirmación sobre universalidad. No se afirma novedad del álgebra anterior.

La [nota anterior](../2026-11-08--thirring-primera-colision.md) es contexto de
autor, no fuente primaria ni revisión independiente. Su bloqueo de un solo nodo
motivó este experimento; aquí las fases se han derivado de nuevo directamente
desde la regla y comprobado con propagadores que no usan la puerta esperada.

Se cierra este experimento y esta codificación sin masa. No se abre una búsqueda
de modelos ni un barrido masivo. Pasar al modelo con masa, otras codificaciones
o controles cambiaría las hipótesis y requeriría otro contrato. El objetivo
general «procesador universal con emergencia relativista» queda abierto.
