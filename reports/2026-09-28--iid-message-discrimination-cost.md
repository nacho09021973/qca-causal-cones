# Coste de distinguir mensajes mediante repeticiones independientes

Fecha: 2026-09-28. Baseline: `13d398a`, rama
`claude/endpoint-transfer-partial`.

Estado: **PRELIMINARY / derivación analítica del autor, sin revisión**
**independiente**. Se responde al primer paso solicitado por el usuario:
coste de repetir el protocolo congelado y alcance de las cotas existentes.
Las asintóticas de la corona se heredan como premisas; no se recalculan.
Este informe no promociona un gate ni demuestra una frontera universal en c.
No se ha ejecutado código para producir resultados científicos nuevos.


> Nota de incorporación — 2026-09-28. Texto aportado por el usuario, conservado
> en su idioma original. Se normalizan el Markdown, las fórmulas y los enlaces;
> «RN pasos-copia» aclara el recuento agregado de §4. Esta incorporación no es
> una revisión matemática independiente. El baseline local declarado `13d398a`
> no era recuperable en GitHub al incorporar el texto; la base remota es
> `0ad333fb645200a409733642cfccc7dd2fec8f48`.
> El expediente 4B del 25 de septiembre ya existe en esa base (estado §8.21);
> la última frase del informe no lo cierra de nuevo ni incorpora el distinto
> informe local del 28 de septiembre mencionado por el usuario.

## 1. Contrato estadístico y resultados disponibles

Se fijan CJWW (5.15), dos componentes, nodo cero, S=W†, el recurso phi_N,
las bolas A_N y B_N, sus perfiles y los dieciséis pares (M,M_B) del
[contrato original](../theory/SCALED_IR_SIGNALING_GATE.md), §§2–5.
El bit b es el mismo durante R usos. Cada uso comienza con una copia
independiente del recurso y aplica el mismo encoder y la medición binaria
{E_N,I-E_N}, E_N=h_N M_B. Se conservan detecciones y no detecciones.
R es fijado antes de observar; no se estudian reglas de parada adaptativas.

Por defecto, los bits tienen probabilidades previas iguales. El objetivo es
error medio ≤ epsilon, con 0<epsilon<1/2 fijo e independiente de N.
Las leyes de ambos mensajes se consideran conocidas: se excluye del recuento
el coste de calibrarlas. Al final se considera también error máximo por bit.

Definimos

$$
p_{b,N}=\langle S^NU^{(b)}\phi_N,E_NS^NU^{(b)}\phi_N\rangle,
\quad X_i\mid b\sim\operatorname{Bernoulli}(p_{b,N}),
\quad \delta_N=|p_{1,N}-p_{0,N}|.
$$

Las premisas localizadas antes de derivar el coste son:

| Premisa | Evidencia del repo | Uso |
|---|---|---|
| delta_N=abs(C(theta_N)) N^(-13/2) exp(-K_*N)(1+O(N^(-1/2))), con C uniformemente separado de cero | `state/CURRENT_STATE.md` §8.20; manuscrito, teorema de asintótica principal | Diferencia entre las probabilidades |
| Campo libre r_N(y)=N^(-3/2)R_0(y/N)+O(N^(-5/2)), uniformemente en Bob | [Informe de coeficiente](2026-09-17--regional-laplace-coefficient-gate.md), §9; [TeX](../papers/ir-corona/ir-corona.tex), lema `lem:tail` | Fondo de detección |
| p_{0,N} → p_infty>0 para M_B=I | [Informe C3](2026-09-23--c3-conditioning-execution.md), §2, C3.5–C3.6 | Ya da la positividad para el detector escalar |
| D_B≤4T_N, T_N≤9N^4 exp(-JN) | TeX, teorema `thm:upper` y su prueba | Alcance uniforme de la obstrucción |
| D_B≤4N^3(1+10N) exp(-K_*N) | TeX, teorema `thm:rate`, parte (d) | Versión uniforme de tasa más fuerte |

Aquí theta_N={sqrt(3)N/4}. No se sustituye C(theta_N) por una constante.
El contrato original excluye postselección. Las proyecciones de C1–C3 son
otro objeto; sus probabilidades condicionadas no son p_{b,N}.

## 2. El fondo queda separado de cero y de uno

Para cada uno de los cuatro detectores, la suma de Riemann del campo libre da

$$
p_{0,N}\longrightarrow p_\infty^{(M_B)}
=\int_{|Y-u|<1/4} (1-16|Y-u|^2)^2
R_0(Y)^\dagger M_B R_0(Y)\,d^3Y,
\qquad u=(1,1,1).
\tag{1}
$$

El error uniforme de amplitud aporta O(N^-1) a la probabilidad al sumar
O(N^3) sitios. La convergencia restante es una suma de Riemann de una
función continua con soporte compacto. Esta operación ya aparece en C3
para M_B=I; aquí se explicita su extensión a los detectores originales.

**Positividad.** R_0 es la transformada inversa de
c_r g(q) exp(-i H_W(q)) down, con soporte |q|≤1. Es analítica real.
Si M_B^(1/2)R_0 se anulase en toda la bola abierta de Bob, se anularía
en todas partes y también su transformada de Fourier. Para I, P_1 y P_2,
esto contradice M_B down ≠0 en q=0. Para P_3=(I+sigma_3)/2, que anula
down, la derivada en q_1 en cero es -i P_3 sigma_1 down ≠0.
Por tanto el integrando es positivo en algún abierto interior y
p_infty^(M_B)>0 en los cuatro casos.

**Cota estricta superior.** Por Plancherel, la normalización heredada
del recurso y la unitariedad de exp(-iH_W(q)), integral ||R_0||²=1.
El peso extendido por cero satisface 0≤h<1 salvo en un punto de medida
cero, y 0≤M_B≤I. Así p_infty^(M_B)<1. Esto también se ve integrando
(1-h)||R_0||², que es estrictamente positivo.

Como delta_N→0, ambos mensajes tienen el mismo límite en (0,1).
Para cada detector existe m>0 y N_0 finito tales que
m≤p_{b,N}≤1-m para N≥N_0. No se proporciona un valor efectivo de N_0.

Esta condición es esencial. Un evento por sitio puede ser pequeño mientras
la probabilidad integrada sobre O(N^3) sitios tenga un límite positivo.
El límite p_infty puede ser numéricamente pequeño; la afirmación es que
no decrece con N.

## 3. Problema exacto de decisión y cotas de repeticiones

El conteo K=sum_i X_i es suficiente: condicionado al conteo, las cadenas
binarias son equiprobables bajo ambos mensajes. Por decisión de máxima
verosimilitud, el error óptimo entre los registros de esta medición es

$$
P_e^*(R,N)=\frac12\sum_{k=0}^R {R\choose k}
\min\{p_{0,N}^k(1-p_{0,N})^{R-k},
        p_{1,N}^k(1-p_{1,N})^{R-k}\}.
\tag{2}
$$

Sea R_epsilon(N) el mínimo entero R que hace (2) ≤ epsilon.
La optimización es sobre la decisión clásica después de medir el efecto
fijo; no es una optimización sobre mediciones cuánticas alternativas.

Escribimos la afinidad de Bhattacharyya de un uso como

B_{N}=√(p_{0,N}p_{1,N})+ √((1-p_{0,N})(1-p_{1,N})),  a_{N}=-log B_{N}.

Para distribuciones P,Q, TV=(1/2)sum|P-Q| y B=sum sqrt(PQ) satisfacen
1-B≤TV≤sqrt(1-B²). La primera desigualdad sigue de
(sqrt(P)-sqrt(Q))²≤|P-Q|; la segunda, de Cauchy–Schwarz aplicado a
|P-Q|=|sqrt(P)-sqrt(Q)|(sqrt(P)+sqrt(Q)). En productos independientes
la afinidad es B_N^R. Dado P_e^*=(1-TV)/2, resulta

$$
\frac{1-\sqrt{1-B_N^{2R}}}{2}
\le P_e^*(R,N)\le\frac{B_N^R}{2}.
\tag{3}
$$

Para 0<B_N<1 esto da cotas no asintóticas:

$$
\frac{\log[1/(4\epsilon(1-\epsilon))]}{2a_N}
\le R_\epsilon(N)
\le\left\lceil\frac{\log[1/(2\epsilon)]}{a_N}\right\rceil.
\tag{4}
$$

La derivación es autocontenida; las desigualdades estándar se contrastaron
con Fuchs–van de Graaf, [Fuchs–van de Graaf](https://arxiv.org/pdf/quant-ph/9712042v2),
pp. 17–18, proposición 5 y ecuaciones (43), (49)–(57). Para las convenciones
de error óptimo y distancia se leyó también el PDF local
`biblioteca/Theory of Quantum Information.pdf`, pp. PDF 148 y 183–184
(páginas impresas 140 y 175–176; teoremas 3.4 y 3.36).

Con p=p_{0,N}, d=p_{1,N}-p_{0,N}, la expansión directa es

$$
\sqrt{p(p+d)}+\sqrt{(1-p)(1-p-d)}=1-\frac{d^2}{8p(1-p)}+O(|d|^3).
$$

El resto es uniforme cuando p está separado de 0 y 1. Usando (1),

$$
a_N=\frac{\delta_N^2}{8p_\infty^{(M_B)}(1-p_\infty^{(M_B)})}(1+o(1)).
$$

Por (4), para cada par congelado y epsilon fijo,

$$
\boxed{R_\epsilon(N)=\Theta_{\epsilon,M,M_B}(\delta_N^{-2})
=\Theta_{\epsilon,M,M_B}\left(
\frac{N^{13}e^{2K_*N}}{|C_{M,M_B}(\theta_N)|^2}\right).}
\tag{5}
$$

En particular, log R_epsilon(N)/N → 2K_*. La dependencia oscilante de C
permanece acotada y no altera esta tasa. Theta expresa cotas de orden;
no se ha demostrado aquí un prefactor óptimo exacto de R_epsilon.

**Segunda vía de comprobación.** El test de umbral en
(p_{0,N}+p_{1,N})/2 tiene, por Chebyshev, error bajo cada bit ≤1/(R delta_N²).
Para una cota necesaria, chi²(Bern(p_1)||Bern(p_0))=delta_N²/[p_0(1-p_0)].
La identidad de producto 1+chi²(P_1^R||P_0^R)=(1+chi²(P_1||P_0))^R
y TV≤sqrt(chi²)/2 implican

$$
R_\epsilon(N)\ge
\frac{\log[1+4(1-2\epsilon)^2]}
{\log[1+\delta_N^2/(p_{0,N}(1-p_{0,N}))]}.
\tag{6}
$$

(6) y el test de umbral recuperan (5) sin usar afinidad ni (3).
También prueban el mismo orden si se exige error ≤epsilon bajo **cada**
bit: la cota inferior de error medio sigue siendo necesaria y el test de
umbral controla ambos errores. Son comprobaciones analíticas del autor,
no una revisión independiente.

**Caso límite que impide usar solamente delta.** Para p_0=0, p_1=delta,
el test óptimo da P_e^*=(1-delta)^R/2 y R_epsilon=Theta(delta^-1).
Ese caso tiene un fondo distinto al demostrado en §2. Por ello, la señal
delta por sí sola no permite inferir el exponente doble de (5).

## 4. Preparaciones, mediciones y postselección

En (5) se cuentan R copias independientes del recurso, R usos del encoder
y R mediciones binarias. Cada uso contiene N pasos del walk: el volumen
de trabajo agregado es RN pasos-copia. Si los usos son secuenciales, la
evolución requiere RN ticks, además de preparar y medir. Si son paralelos,
pueden compartir N ticks de evolución, a costa de R sistemas preparados.
Ninguna de esas modalidades identifica una duración absoluta sin tau.

El recurso phi_N, con cola espacial, se supone disponible en el contrato.
No hay un procedimiento de preparación local certificado ni un modelo de
coste de construir regiones de tamaño O(N). Por tanto (5) es un coste de
discriminación dado ese recurso. Sólo si el coste por copia fuese como
máximo polinómico podría afirmarse que el coste total tiene la misma tasa
exponencial 2K_*; esa hipótesis adicional no se prueba aquí.

El protocolo original no descarta ensayos. Las no detecciones son parte
de (2). Para un protocolo distinto con éxito s_b y probabilidad de click
condicionada q_b, el registro mínimo que incluye el fallo tendría ley

$$
(1-s_b,\ s_b q_b,\ s_b(1-q_b)).
\tag{7}
$$

Cuando s_0=s_1=s, obtener r éxitos cuesta r/s intentos **en esperanza**;
una garantía de coste con probabilidad fijada necesita además controlar
la cola del número de intentos. Si s_0≠s_1, las marcas de fallo y los
tiempos de espera pueden contener información y se requiere la ley conjunta.
Una mejora de la distancia condicionada no basta para demostrar un ahorro.
El posprocesamiento clásico de registros completos no aumenta TV.

La proyección espectral de C3 no pertenece a las operaciones locales del
protocolo original. Además del recuento de intentos, necesitaría justificar
implementación y acceso a la marca de éxito. No se incorpora como vía de
comunicación para eludir (5).

## 5. Qué extensión ya se deduce de las cotas uniformes

El manuscrito demuestra, en las mismas bolas A_N,B_N y con tiempo N,
para **todo** estado inicial de una partícula compartido antes de elegir
el bit, toda unitaria U igual a I fuera de A_N y cualquier efecto en Bob,

$$
D_B(N)\le\eta_N:=\min\{1,4N^3(1+10N)e^{-K_*N}\}.
\tag{8}
$$

La prueba usa ||v_1-v_0||≤2T_N y la forma explícita del estado reducido
en los bloques de vacío y una partícula. Su lectura confirma ese alcance;
no es una cota para estados arbitrarios del Fock de muchas partículas.

Para R salidas independientes, telescopar la diferencia de los productos
y usar la multiplicatividad de la norma traza da

$$
D(\rho_{0,B}^{\otimes R},\rho_{1,B}^{\otimes R})\le R\eta_N,
\qquad
P_{e,\mathrm{opt}}\ge\frac{1-\min\{1,R\eta_N\}}2.
\tag{9}
$$

Esta cota incluye una medición conjunta arbitraria sobre las R salidas de
Bob: por el principio de discriminación binaria, ni siquiera la medición
óptima supera su distancia de traza. La telescopación funciona igualmente
para protocolos predeterminados distintos en cada uso, si cada uno cumple
(8) y sus entradas son independientes. En particular, fiabilidad fija exige

$$
R\ge\frac{1-2\epsilon}{\eta_N}
=\Omega_\epsilon(N^{-4}e^{K_*N})\qquad(N\to\infty).
\tag{10}
$$

De aquí ya sale que R polinómico, e incluso R=exp(o(N)), no mantiene
un error separado de 1/2 en esta clase y geometría. Es una cota necesaria
uniforme; no afirma que exista un protocolo que alcance la tasa $K_*$.
La tasa $2K_*$ de (5) describe el detector binario congelado con su fondo.
No se transfiere como tasa óptima a todos los protocolos de (8).

## 6. Obligaciones que quedan para una frontera operacional

1. **Geometría:** (8) controla las bolas y su separación diagonal congeladas.
   Una frontera en c_IR=1 requiere familias con un margen fijo fuera del cono
   en todas las direcciones pertinentes, y constantes uniformes en su clase.
   No se toma el margen hacia cero en las cotas presentes.
2. **Clase de recursos:** especificar muchas partículas, densidad o energía,
   ancillas, entrelazamiento entre usos, adaptatividad, tamaño de laboratorios
   y coste de preparar el recurso. (9) no controla entradas correlacionadas
   ni un protocolo general de múltiples rondas.
3. **Interior:** exhibir comunicación con fiabilidad fija y recursos
   controlados dentro del cono. La velocidad de grupo, por sí sola, no es
   ese protocolo operacional.
4. **Estabilidad y universalidad:** quedan fuera de esta derivación; requieren
   una familia explícita de perturbaciones y/o especies y cotas uniformes.
5. **Valores finitos:** obtener constantes de resto y N_* efectivos, y
   calibración/control de p_{b,N}, para transformar (5) en un presupuesto
   numérico certificado a N dado. No se da aquí un número de ensayos concreto.

El resultado obtenido es un coste exponencial de repeticiones para los
dieciséis pares originales y una obstrucción uniforme más débil para la
clase de una partícula descrita en §5. La hipótesis de que c delimita una
frontera estable de comunicación macroscópica sigue abierta. Su formulación
adimensional es compatible con el cierre acotado de 4B.
