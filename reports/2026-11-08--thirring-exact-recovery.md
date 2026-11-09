# Código microscópico Thirring: no hay recuperación exacta posterior

2026-11-08. Autor Codex/OpenAI. **PRELIMINARY: demostración analítica y
contrastes del autor, con una revisión externa de Claude y sin promoción.
El teorema de tiempo arbitrario no está formalizado en Lean.**

[Revisión ciega de Claude](reviews/2026-11-08-thirring-exact-recovery-opus/informe_opus.md)
del texto en 0828861: «Se sostiene», con dos aclaraciones menores incorporadas
abajo. Una ronda, herramientas ce09890; el revisor inspeccionó el script sin
ejecutarlo y no comprobó PDF ni Lean. Su informe se conserva sin editar.

Usuario «adelante» a estudiar si existe T>=3 y una unitaria entrelazante V
con U^T B=F^T B V. Contrato
[THIRRING_EXACT_RECOVERY_GATE.md](../theory/THIRRING_EXACT_RECOVERY_GATE.md),
congelado antes del verificador en `0212df6`, después de anunciar la idea
manual de los rayos. Código versionado antes de ejecutar en `578607b`.

## 1. Teorema y alcance

Para el código microscópico M=1 del trabajo anterior, regla fija con
mu=3/5,nu=4/5,chi=pi/2, recta infinita y salida libre exacta F^T B:

\[
 \boxed{\text{para todo entero }T\ge2,\quad
 \nexists\,V\in\mathbb C^{4\times4}:\ U^T B=F^T B V.}
\]

Se excluye cualquier matriz V, y en particular una unitaria entrelazante.
Más concretamente, la entrada producto lógica 01 tiene fuga estrictamente
positiva para cada T>=2. En T=1 permanece la puerta exacta D ya comprobada.

Veredicto: `EXACT_RECOVERY_EXCLUDED_FOR_ALL_FINITE_T_GE2 /
FIRST_STEP_GATE_RETAINED / APPROXIMATE_RECOVERY_OPEN`.

El argumento que sigue usa solo 0<mu,nu<1, mu²+nu²=1 y una fase
z=e^{i chi} distinta de uno. Por tanto esas hipótesis bastan para la misma
exclusión con este código. La ejecución y el contrato físico conservan
los parámetros congelados; no se realizó búsqueda de masas o acoplamientos.

No se excluyen recuperación aproximada, otro código de salida, medidas,
auxiliares o una geometría distinta. No es una imposibilidad del autómata
de Thirring completo ni de un procesador universal relativista.

## 2. Definiciones y coordenadas

Se mantiene U=FJ y

\[
 W=\begin{pmatrix}\nu\mathsf T&-i\mu\\-i\mu&\nu\mathsf T^{-1}\end{pmatrix},
 \quad J=\prod_x e^{i\chi n_R(x)n_L(x)}.
\]

La traslación espacial se escribe mathsf T para distinguirla del tiempo T.
El modelo publicado se consultó en `1804.08508v1.pdf` p.3, Ec.(1) y sección 3.
La fase precede al paso libre. La orientación R/L es la declarada en los
informes previos; no cambia la interacción local.

Los qubits iniciales son A=(R|0>,L|1>) y B=(R|1>,L|0>), con producto de
creación en orden A,B. Escribimos B para la isometría de sus cuatro
entradas, en orden 00,01,10,11. Como antes, los modos pertenecen a sectores
opuestos de Gamma=sigma_z(-1)^x. En cada tiempo se sigue cada etiqueta
en su sector alternante. Las amplitudes ordenadas por sus dos posiciones
son una representación isométrica del sector fermiónico correspondiente,
no una eliminación de la estadística sin justificación.

Explícitamente, para modos de sectores opuestos, el mapa es
I_t(psi tensor phi)=(psi tensor phi-phi tensor psi)/sqrt(2).
Es isométrico porque los sectores son ortogonales. La evolución libre
satisface F I_t=I_{t+1}(W tensor W): se conserva el orden A,B mientras
sus sectores alternan. J conserva esta imagen y actúa como fase z solo
si las posiciones coinciden, pues entonces las componentes son opuestas.
Así no se introduce un signo dependiente del camino al usar posiciones
ordenadas A,B, tanto para U como para F.

La salida B_T=F^T B se obtiene de modos libres de una partícula. No depende
de U, de V o del estado lógico de entrada. No se aplica F^{-T} como control.

El primer contacto preserva el código:

\[
 JB=BD,\qquad D=\operatorname{diag}(1,z,z,1),\qquad UB=FB D.
\]

## 3. Cuatro rayos extremos fuerzan la matriz V

En el sector ordenado de Gamma opuestos, sea Pi_T la extracción de las
cuatro amplitudes en posiciones (x_A,x_B), en este orden:

\[
 (T,T+1),\quad(1-T,T+1),\quad(T,-T),\quad(1-T,-T).
\]

Son cuatro coordenadas ortogonales, así que ||Pi_T||=1. Para T>=1,

\[
 R_T:=\Pi_T F^T B=\nu^{2T-1}G,\qquad
 G=\begin{pmatrix}
 \nu&0&-i\mu&0\\
 -i\mu&0&\nu&0\\
 0&\nu&0&-i\mu\\
 0&-i\mu&0&\nu
 \end{pmatrix},\qquad G^\dagger G=I.
\]

Justificación de los factores, sin extrapolar casos finitos:

- B en T+1 solo proviene del modo inicial R|1> mediante T traslaciones
  a derecha. Su amplitud es nu^T. Ninguna trayectoria del modo L|0>
  puede llegar allí: necesita primero convertir su componente y pierde
  al menos un desplazamiento.
- B en -T solo proviene del modo inicial L|0> por T traslaciones a
  izquierda, también con amplitud nu^T.
- A en T tiene amplitudes (nu^T,-i mu nu^(T-1)) desde sus modos 0 y 1.
  A en 1-T tiene amplitudes (-i mu nu^(T-1),nu^T). Para esos extremos,
  la conversión de componente, cuando hace falta, tiene que ocurrir
  en el primer paso; después todas las traslaciones deben ser exteriores.

Además, las trayectorias extremas de B no pueden volver a contactar con A
tras t=0: B corre hacia fuera a velocidad máxima, y después del primer
paso A queda estrictamente detrás. En efecto, para t>=1 cualquier trayectoria
de A satisface 1-t<=x_A(t)<=t: desde R0 no puede empezar a izquierda,
y desde L1 no puede empezar a derecha; una conversión de componente
consume un paso sin desplazamiento. Frente a ello los rayos de B están
en t+1 o -t. Una trayectoria de A de alcance uno
por paso no puede alcanzarlo. Esto vale independientemente de los caminos
internos de A. Las únicas fases posibles son las del contacto inicial,
por lo que para **todos** los T>=1,

\[
 \Pi_T U^T B=R_T D.
\]

Como nu>0 y G es unitaria, R_T es invertible. Si existiera una matriz V
con U^T B=F^T B V, al extraer esas coordenadas se obtendría
R_T V=R_T D y necesariamente **V=D**. Esto incluye cualquier fase global
o cambio de base lógico que se pretendiera absorber en V.

## 4. El segundo contacto emite una amplitud que no puede cancelarse

Definimos Delta_T=U^T B-F^T B D. Usando UB=FB D y telescopaje de potencias,

\[
 \Delta_T=\sum_{k=1}^{T-1}
 U^{T-1-k}F(J-I)F^k B D,\qquad T\ge2.
\]

Cada factor J-I es (z-1)C, con C el proyector de coincidencia de dos
componentes opuestas. Su fuente tiene separación relativa cero. Desde
la fuente k quedan T-k pasos: la separación relativa absoluta alcanzable
es como máximo 2(T-k), porque cada partícula se desplaza a lo sumo
una celda por paso y el contacto no mueve posiciones.

Consideremos la entrada lógica 01, y extraigamos la coordenada

\[
 q_T=(1-T,T-1),\qquad x_A-x_B=-2(T-1).
\]

Ningún término k>=2 puede llegar a q_T, pues 2(T-k)<2(T-1).
Para k=1, sobre esa entrada, la única coincidencia tras el primer paso
libre es la rama de masa en el sitio cero:

\[
 CFB D|01\rangle=-\mu^2z\,|L0,R0\rangle.
\]

Para llegar desde allí a q_T en los T-1 pasos restantes, A debe trasladarse
siempre a izquierda y B siempre a derecha. Es un único par de caminos,
de peso nu^(2T-2), sin nuevos contactos. Por consiguiente,

\[
 \boxed{\langle q_T|\Delta_T|01\rangle
 =-\mu^2z(z-1)\nu^{2T-2}\ne0,\qquad T\ge2.}
\]

Con los parámetros congelados es mu² nu^(2T-2)(1+i). En numeradores
gaussianos sobre el denominador 25^T, sus dos componentes son exactamente
9*4^(2T-2). No hay suma de fases tardías que pueda anular esta amplitud:
las fuentes tardías tienen un cono de separación relativa demasiado corto.

La sección 3 forzaba V=D. Esta amplitud contradice U^T B=F^T B D y cierra
la posibilidad para cualquier T>=2. La prueba no procede de buscar
numéricamente un tiempo de recuperación y no utiliza un anillo finito.

Incluso si solo se exigiera recuperar la entrada 01 en algún vector del
código libre, sus cuatro amplitudes extremas fuerzan los coeficientes a
D|01>. La misma coordenada q_T lo impide. Por tanto esa entrada producto
queda fuera del código libre en todo T>=2.

## 5. Cota cuantitativa y distinción entre exacto y aproximado

Una segunda formulación usa la compresión y el residuo, sin suponer una
recuperación exacta. Sean

\[
 K_T=B_T^\dagger U^T B,\quad
 E_T=(I-B_TB_T^\dagger)U^T B,\quad
 \rho_T=\nu^{2T-1}.
\]

La identidad de los cuatro bordes da

\[
 \Pi_TE_T=R_T(D-K_T),\qquad
 \|(K_T-D)|01\rangle\|\leq\rho_T^{-1}\|E_T|01\rangle\|.
\]

Al extraer q_T de Delta_T=E_T+B_T(K_T-D), con B_T isométrica,

\[
 |\langle q_T|\Delta_T|01\rangle|
 \leq(1+\rho_T^{-1})\|E_T|01\rangle\|.
\]

Resulta una cota explícita para la probabilidad de fuga de la entrada 01:

\[
 \boxed{p_{01}(T)\geq
 \frac{|z-1|^2\mu^4\nu^{8T-6}}{(1+\nu^{2T-1})^2}>0,\quad T\ge2.}
\]

También es una cota inferior de p_max(T). Es dependiente de T y tiende
a cero cuando T crece. No prueba que p_01 real tienda a cero ni que tenga
un límite positivo, y **no excluye recuperación aproximada** o un límite
por una subsecuencia de tiempos. La cota no se convierte en un no-go de
aproximación por ser estrictamente positiva en cada tiempo finito.

## 6. Comprobaciones exactas y segunda implementación

[Script permanente](../scripts/verify_thirring_exact_recovery.py),
[JSON](2026-11-08--thirring-exact-recovery.json),
[registro](2026-11-08--thirring-exact-recovery.txt). **80/80 controles de autor**.
Las cuatro columnas se propagan sobre Z mediante diccionarios de enteros
gaussianos, con denominador común 25^T. No hay frontera periódica ni ajuste
numérico en las identidades de rayos. Los tiempos fijados antes de ejecutar
son 1,2,3,4,6,8,12: contrastan la implementación de las fórmulas, no prueban
el cuantificador de todos los T por muestreo.

Se contrastan: cuatro filas libres, cuatro filas reales y sus fases,
Gram invertible de extracción, Grams de las cuatro columnas completas,
cono de soporte, diferencia de amplitud emitida y fuga racional exacta
de la entrada 01. Esta última se obtiene por proyección sobre las cuatro
columnas libres ortonormales, no suponiendo que los coeficientes sean D.
La cota cuantitativa se compara con esa probabilidad racional.

Como segunda representación se propaga W tensor W con espín explícito y
amplitudes antisimétricas completas para T=1,2,3,4. Un anillo de 20 sitios,
origen par +6, mantiene las trayectorias dentro del intervalo causal sin
contactar con la frontera. Se comparan amplitudes completas libres/reales
y la probabilidad de proyección con el cálculo gaussiano exacto. Es otro
contraste de implementación del autor, no una revisión independiente.

| T | p_01 observado por aritmética racional exacta (redondeado aquí) | Cota inferior de los rayos (redondeada aquí) |
| ---: | ---: | ---: |
| 1 | 0 | No aplicable |
| 2 | 0.165888 | 0.012174 |
| 3 | 0.301608 | 0.002649 |
| 4 | 0.399219 | 0.000535 |
| 6 | 0.529932 | 0.000019 |
| 8 | 0.566089 | 5.79187e-7 |
| 12 | 0.555645 | 4.85984e-10 |

El JSON conserva las fracciones completas. Las cifras de la tabla se
redondean para lectura; no se usan como certificados de redondeo ni para
inferir monotonicidad o comportamiento asintótico. La fila T=1 verifica
la puerta exacta conservada.

## 7. Alcance formal y decisión de cierre

El certificado Lean existente cubre las identidades de dos pasos y conserva
su alcance. No se modificó ni se presenta como prueba de los rayos para
tiempo arbitrario. La demostración general anterior es del autor, con una
revisión externa de otra familia y las aclaraciones señaladas incorporadas;
estas ediciones posteriores no tuvieron una segunda ronda. Sin promoción.
Los hashes de script, contrato y PDF primario
leído en esta sesión están registrados en el JSON.

Se responde negativamente la pregunta congelada: no hay T>=3 con
U^T B=F^T B V, ni siquiera para una matriz V no unitaria. Esperar más
tiempo no recupera **exactamente** este código libre con esta arquitectura.
La puerta de un paso sigue siendo válida y el Thirring completo no queda
descartado. La recuperación aproximada, los cambios de código o recursos,
la universalidad y el régimen relativista son cuestiones distintas y
permanecen fuera de este cierre.
