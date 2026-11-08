# Thirring masivo: rotación lógica de masa y dilución del contacto

2026-11-08. Autor Codex/OpenAI. **PRELIMINARY, derivación y contraste del autor;
sin revisión independiente ni promoción.** Usuario «adelante» al filtro
algebraico previo a otra colisión completa.

Contrato [THIRRING_MASSIVE_ALGEBRA_PREFLIGHT.md](../theory/THIRRING_MASSIVE_ALGEBRA_PREFLIGHT.md),
congelado en `cbfae56`; implementación versionada antes de ejecutar en `e76226a`.

## Resultado y decisión

La masa permite una mezcla lógica en un código de carga alternante definida.
La simetría no obliga a que todas las matrices comprimidas conmuten: la masa
y el contacto tienen ejes diferentes. Sin embargo, esto **no proporciona dos
puertas autónomas componibles**. F y J no son controles separados de U=FJ.

Para la familia de códigos y marcos congelados, con mu fijo en (0,1) y chi fijo,
no existe una familia de puertas entrelazantes de **duración acotada** que se
aproxime con fuga arbitrariamente pequeña variando solo el ancho M. Al reducir
esa fuga, la evolución se aproxima a un producto de rotaciones libres y el
contacto pierde su efecto. La demostración se da abajo; no procede de un ajuste.

Veredicto: `MASS_LOGICAL_MIXING_AVAILABLE /
BOUNDED_DURATION_ENTANGLING_GATE_CLOSED_FOR_DECLARED_CODE /
GROWING_TIME_SCATTERING_OPEN`.

El filtro no establece dos operaciones finitas componibles, de modo que se
activa su corte: termina este preflight sin abrir dispersión a tiempos largos.
No hay no-go del Thirring masivo completo, de otras codificaciones, de tiempos
crecientes con M ni de un procesador relativista universal en general.

## 1. Regla y código

Z, dos modos R,L por sitio, Fock local de dimensión 4. T|x>=|x+1> y

\[
 W=\begin{pmatrix}\nu T&-i\mu\\-i\mu&\nu T^{-1}\end{pmatrix},\quad
 \nu^2+\mu^2=1,\quad 0<\mu<1,\quad
 U=FJ,\quad J=\prod_xe^{i\chi n_R(x)n_L(x)}.
\]

F es la segunda cuantización de W. Las orientaciones R,L se intercambian
respecto de las etiquetas up/down publicadas; la interacción es simétrica.
La fuente primaria es `1711.03920v1.pdf` pp.1–2, Ec.(1) y Ec.(2), y
`1804.08508v1.pdf` p.3. La definición global explícita de J es la usada por
el contrato, compatible con la fase local publicada. No se importa una
solución de tres cuerpos ni un teorema de universalidad de esas fuentes.

Definimos f_M=M^(-1/2) sum_{j=0}^{M-1}|2j>, g_M=T f_M. Las traslaciones
comunes de origen par no alteran lo siguiente. Pi|x>=(-1)^x|x> y
Gamma=sigma_z Pi con sigma_z R=+R, sigma_z L=-L.

\[
 B_+=(|R f_M\rangle,|L g_M\rangle),\qquad
 B_-=(|R g_M\rangle,|L f_M\rangle).
\]

Cada B es una isometría de C² a una partícula; Gamma B_+=B_+ y
Gamma B_-=-B_-. W intercambia los sectores de Gamma, no necesariamente
los códigos bidimensionales. Se conceden preparación/lectura ideales en
la base lógica Z y datos cuánticos arbitrarios; no medidas intermedias.

Un qubit A ocupa B_+, y B ocupa B_-, en ese orden de operadores de creación.
Son subespacios de una partícula ortogonales aunque coincidan espacialmente.
Su producto exterior define una isometría de C² tensor C² al sector de dos
fermiones con Q=dGamma(Gamma)=0. En t impar se comparan A en B_- y B en B_+;
en t par, con el código inicial. El origen y soporte espacial del marco
congelado son los mismos. No se aplica una inversión libre física ni se
sustituye la etiqueta A por B al alternar sus signos de Gamma.

## 2. Por qué no se usa el mismo signo de Gamma en los dos qubits

Un contacto requiere componentes opuestas en un mismo sitio. Sus valores de
Gamma son entonces opuestos. Por tanto el proyector de contacto C se anula
en el sector con dos fermiones de igual Gamma. Como W invierte simultáneamente
ambos signos y J los preserva, la interacción queda inactiva en toda la
evolución de ese sector, a cualquier mu y chi. Es una consecuencia directa
de la regla, compatible con el subespacio libre publicado en Ec.(8) de
`1804.08508v1.pdf` pp.5–6. No se introduce allí una puerta entrelazante.

Usar signos opuestos evita este bloqueo exacto del contacto. No asegura
invariancia del código finito ni universalidad.

## 3. Mezcla de masa: una operación lógica y un error de envolvente

Sea theta=arcsin(mu) y R_theta=nu I-i mu X=exp(-i theta X).

\[
 WB_+=B_-R_\theta.
\]

La igualdad es exacta: R f se traslada a R g y la masa lo convierte en L f;
L g se traslada a L f y la masa lo convierte en R g. Una partícula preparada
en B_+ adquiere una rotación lógica finita, con salida en B_- y sin fuga.
Es mezcla de los dos estados del código, no mera mezcla fuera de él.

Pero el siguiente paso tiene desplazamientos de envolvente:
R g pasa libremente a R T²f, y L f a L T^{-1}f. Con
r_M=<f,T²f>=(M-1)/M,

\[
 B_+^\dagger WB_-=\nu r_M I-i\mu X,\qquad
 \|(I-B_+B_+^\dagger)WB_-\|^2=\nu^2(1-r_M^2).
\]

Esta fuga es estrictamente positiva a M finito para 0<nu<1.
La distancia al mapa ideal es exactamente

\[
 \delta_M=\|WB_--B_+R_\theta\|=\nu\sqrt{2/M}.
\]

Como comprobación alternativa, el mapa comprimido de dos pasos vale

\[
 B_+^\dagger W^2 B_+
 =(\nu^2r_M-\mu^2)I-i\mu\nu(1+r_M)X
 \longrightarrow R_\theta^2.
\]

La alternancia admite rotaciones libres de error controlado para un número
fijo de pasos a M grande. La masa homogénea no proporciona por sí sola
rotaciones independientes direccionables de cada qubit.

## 4. Contacto: segundo eje algebraico, no una puerta finita de baja fuga

Denotemos B^(2) la isometría exterior B_+ wedge B_-. Solo los estados lógicos
01 y 10 pueden coincidir, sobre M sitios y con probabilidad 1/M cada uno.
Como J=I+(e^{i chi}-1)C en el sector de dos partículas,

\[
 K_J=B^{(2)\dagger}JB^{(2)}=\operatorname{diag}(1,c_M,c_M,1),
 \quad c_M=1+\frac{e^{i\chi}-1}{M}.
\]

La fuga máxima sobre entradas del código es exactamente

\[
 p_J=1-|c_M|^2
 =\frac{2(M-1)}{M^2}(1-\cos\chi),\qquad
 \|CB^{(2)}\|=1/\sqrt M.
\]

Para M=1, K_J es unitaria y puede entrelazar; pero el paso libre de uno
de los dos qubits tiene fuga nu², que vale 0.64 con los parámetros congelados.
Para M>1 y chi no múltiplo de 2pi, K_J no es una puerta unitaria determinista.
Cuando M->infinito, tanto p_J como K_J-I tienden a cero. El segundo eje
algebraico es ZZ (mediante el proyector lógico (I-ZZ)/2), y no conmuta en
general con la rotación de masa. Ese conmutador no establece dos operaciones
implementables: el autómata aplica FJ, no J y F bajo control independiente.

De hecho, en un paso completo, sin proyección intermedia,

\[
 \|(U-F)B^{(2)}\|=|e^{i\chi}-1|/\sqrt M.
\]

La igualdad proviene de la unitariedad de F y del proyector C; se verifica
también por propagación reticular completa. No se reemplaza FJ por el
producto de sus compresiones: la fuga intermedia puede volver al código.

## 5. Cota para duración acotada y criterio de cierre

Sea B_t^(2) el código de salida alternante y L_T=R_theta^T tensor R_theta^T.
Con la norma de operador sobre las cuatro entradas lógicas, una cota
conservadora del paso libre, por telescopaje de las dos partículas, es

\[
 \|F^T B^{(2)}-B_T^{(2)}L_T\|\leq 2T\delta_M.
\]

Todos los códigos B_t^(2) tienen el mismo valor ||CB_t^(2)||=1/sqrt M.
La identidad de diferencias de potencias (sin proyectar en cada paso) da

\[
 U^T-F^T=\sum_{t=0}^{T-1}U^{T-1-t}F(J-I)F^t.
\]

Insertando el control del paso libre en cada término,

\[
 \|(U^T-F^T)B^{(2)}\|
 \leq d_\chi\left(\frac{T}{\sqrt M}+\delta_M T(T-1)\right),
 \quad d_\chi=|e^{i\chi}-1|.
\]

Por tanto la evolución real se aproxima a B_T^(2)L_T con error que tiende
a cero uniformemente para T en cualquier conjunto acotado de enteros.
L_T es un producto local, y no una puerta entrelazante fija.

Además, no hay cierre exacto escondido a M finito en este marco. Para la
entrada 00, hay dos componentes R, una en sitios pares y otra en impares.
Sea x_max=2M-1 el extremo derecho ocupado inicialmente. El modo R en
x_max+T solo puede provenir de la trayectoria totalmente a derecha de ese
extremo inicial; no puede contactar con otra partícula que empezó detrás.
Su ocupación al tiempo T es

\[
 \langle n_R(x_{\max}+T)\rangle=\nu^{2T}/M.
\]

Para T>=1, ese modo está fuera de todo el soporte del código de salida
congelado, así que p_fuga,max>=nu^{2T}/M>0. Es una prueba por trayectoria
extrema, diferente del telescopaje; el verificador contrasta también esa
ocupación directamente en las amplitudes antisimétricas.

Si T<=T_max fijo y la fuga tiende a cero variando M, necesariamente M->infinito
(salvo el paso T=0, identidad). Pero en ese límite el mapa real se aproxima
a un producto local. No puede converger simultáneamente a una puerta
entrelazante fija. Esto cierra **solo las puertas de duración acotada en el
código y marco congelados**. No excluye U a tiempos T(M) crecientes, otro
perfil, otra geometría o un código que siga evoluciones espaciales distintas.

## 6. Contraste reticular y límites físicos

[Verificador permanente](../scripts/verify_thirring_massive_preflight.py),
[JSON](2026-11-08--thirring-massive-preflight.json),
[registro](2026-11-08--thirring-massive-preflight.txt).
Parámetros fijos mu=3/5,nu=4/5,chi=pi/2; M=1,2,4,8,16; T=1,2.
Python 3.12.3, NumPy 2.4.4, sin aleatoriedad. **140/140 controles de autor**:
incluyen propagación, fórmulas, cotas y consistencia estructural; no son
140 evidencias independientes ni sustituyen las pruebas con cuantificadores.

| M | T | Distancia real a evolución libre, norma | Fuga real máxima sobre entradas |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1.414214 | 0.640000 |
| 4 | 1 | 0.707107 | 0.550000 |
| 16 | 1 | 0.353553 | 0.185605 |
| 1 | 2 | 1.543841 | 0.870400 |
| 4 | 2 | 0.944606 | 0.832576 |
| 16 | 2 | 0.493168 | 0.346476 |

Redondeo ordinario a seis decimales de residuos/valores observados; no cotas
certificadas de redondeo. Las matrices y las fugas se calcularon con amplitudes
antisimétricas de dos fermiones y desplazamientos reales, sin insertar el mapa
lógico esperado en el propagador. Un anillo con márgenes de al menos seis
sitios evita que las trayectorias T<=2 alcancen su frontera. Las fases de
contacto se aplican antes de cada W tensor W.

Las fórmulas de masa y contacto se derivan también desde los modos y el conteo
de coincidencias; las cotas de duración fija no se ajustan a la tabla. El
resultado numérico solo contrasta los casos indicados y las implementaciones.

Este código tiene soporte par/impar y combina nodos; no se ha aislado un
qubit de baja cuasienergía. El mu=3/5 fijo no es un límite continuo de Dirac
masivo. No se ha calculado un límite interactuante relativista, una velocidad
IR común ni una relación entre universalidad y frecuencia absoluta de reloj.
Esas preguntas no se deducen del presente filtro algebraico.

Los hashes de contrato, script y PDF están en el JSON. Los PDF primarios son
los originales locales leídos en esta sesión; las ecuaciones de este informe
son derivaciones del autor a partir del W y J explícitos. No se afirma novedad.

## 7. Punto de parada

Se obtuvo mezcla lógica por masa, pero no dos puertas autónomas de efecto
finito, fuga controlable y composición demostrada. El candidato elemental
de duración acotada queda cerrado. La pregunta de interacción acumulada a
tiempos crecientes con M queda **OPEN** y requiere otro contrato; no se ha
ejecutado dispersión larga ni un barrido de parámetros como sustituto.
El Thirring masivo completo y la hipótesis general del usuario siguen abiertos.
