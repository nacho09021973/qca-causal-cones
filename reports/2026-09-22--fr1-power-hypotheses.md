# FR1 — hipótesis del conteo de potencias

Fecha: 2026-09-22. Autor: Codex, agente `/root`.
Estado: **AUDITORÍA DE DEPENDENCIAS ESCRITA / ROBUSTEZ DE CLASE ABIERTA**.

## 1. Alcance y fuentes leídas

Se ejecuta únicamente la petición de precisar las hipótesis que sostienen
cada contribución de la Observación 7.6. Se conserva el walk CJWW (5.15),
dimensión tres, nodo cero, tiempo N, regiones y dieciséis pares originales.
No se sustituye ningún perfil ni recurso y no se resuelve una nueva clase.
FR2, FR3 y E/AdS quedan fuera de esta auditoría.

Entrada: `HEAD = f4f937e102def05f8797a94e256a460d81b0cc33`.
El roadmap, C2c y la nota FR1–FR3 estaban sin versionar al inicio.

| Fuente | Pasajes utilizados |
| --- | --- |
| [Manuscrito](../papers/ir-corona/ir-corona.md) | §§3.1–3.3, Teoremas 4.3–4.4, §6, §§7.1–7.7, Observaciones 7.6–7.7 |
| [Nota FR1–FR3](2026-09-22--front-resource-scaling.md) | §3, contabilidad y obligación de robustez |
| [Contrato del coeficiente](../theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md) | §§1–3, clase y coeficiente completo |
| [Revisión independiente existente](2026-09-17--regional-laplace-coefficient-gate-independent-review.md) | §§1–4, conteo, suma de saddles, no anulación y restos |
| [Estado vigente](../state/CURRENT_STATE.md) | §8.20, alcance del resultado revisado |

SHA256 del manuscrito leído:
`afcc25057f0a258888b71e25a5692ec06bfec1c76ac59132da73ded2ee89e7f3`.
SHA256 de la nota FR1–FR3 antes de añadir el enlace a esta auditoría:
`a39b3e95beaad0640fced567de26717d335c69c360ca5e28cc27fe41a0c58034`.
Esta lectura reutiliza el resultado revisado; no cuenta como una nueva
revisión independiente ni como reejecución de su certificado.

## 2. Qué se está contando

La cantidad es la respuesta firmada L, con delta = |L| para el efecto
fijado de Bob. No se cuenta una probabilidad de propagación aislada ni la
distancia de traza óptima. Por §7.1, el sector exponencial e^(−K_*N)
procede de interferencia lineal entre la cola libre r y la fuente local
propagada. Las piezas cuadráticas están acotadas por
O(N^8 e^(−2K_*N)); la pieza con c_N empieza a orden algebraico inferior.

La representación inclinada (13) multiplica dos sumas de capa y el símbolo
evolucionado, e integra en tres variables de Fourier. El Lema 7.4 aporta
N^(−5/2) de cada capa; el Teorema 7.5 aporta N^(−3/2) de la medida:

$$
\frac{13}{2}
=\underbrace{\left(\frac32+2-1\right)}_{\text{Alice}}
+\underbrace{\left(\frac32+2-1\right)}_{\text{Bob}}
+\underbrace{\left(\frac12+1\right)}_{\text{integración gaussiana}}.
$$

Este conteo identifica una escala candidata de la expansión. Para que sea
el término dominante del observable real se necesita además §5 de esta nota.

## 3. Hipótesis de cada contribución

### 3.1. Recurso en Alice: 3/2

En §3.2, la forma g(Np), con g fijo, soporte compacto en la bola unidad y
norma no nula, da Z_N proporcional a N^(−3). El cambio q = Np produce
exactamente varphi_N(x) = N^(−3/2) Phi_0(x/N). El origen de 3/2 es la
normalización de una ventana tridimensional de anchura N inversa; no es
el orden dos del cero de g en su borde espectral.

Para usar esa escala como líder en la capa hace falta la traza espacial
Phi_0(hat u/4), aquí varphi_partial > 0, y regularidad para sustituir la
amplitud por su valor enfrentado. En la capa, desplazamientos tangenciales
O(sqrt(N)) cambian x/N en O(N^(−1/2)); el Lema 7.4 controla ese error.
Normalización y banda por sí solas no garantizan una traza distinta de cero.

**Dependencia:** la escala N inversa, dimensión y forma reescalada fija
sostienen la potencia; la traza, el espinor y la regularidad sostienen la
amplitud y el resto. Para otra g de forma fija puede repetirse el cambio de
variables de normalización, pero no se heredan la traza ni el coeficiente.

### 3.2. Campo libre en Bob: 3/2

El Lema 7.2 usa el mismo recurso sin truncar, el tiempo N y la expansión
H(p) = H_W(p) + O(|p|²) en el nodo cero. En |p| ≤ N inversa, Duhamel da
S(p)^N = exp(−iNH_W(p)) + O(N inversa) en norma. Tras reescalar,

$$
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})\quad(y\in\mathcal B_N).
$$

R_0 es suave y su valor en w_* = u − hat u/4 se calcula explícitamente.
El campo de referencia tiene cola espacial: no se le asigna el factor
exponencial de la propagación desde la fuente local de Alice.

**Dependencia:** ventana, tiempo, aproximación de Weyl y regularidad.
R_0(w_*) no nulo aún no garantiza que su contracción con detector,
proyector inclinado y fuente sobreviva al funcional real del observable.

### 3.3. Perfiles de Alice y Bob: 2 + 2

Con R = N/4, profundidad delta = O(1) y coordenada tangencial u_perp,
§7.4 escribe exactamente F_N = 64 N^(−2) epsilon_perp², donde
epsilon_perp = delta − delta²/(2R) − |u_perp|²/(2R) en el disco soporte.
Por tanto,

$$
s_N=32\pi N^{-2}\varepsilon_\perp^2+O(N^{-6}),\qquad
c_N=-512\pi^2N^{-4}\varepsilon_\perp^4+O(N^{-8})
$$

para profundidades acotadas. Bob aporta h_N = 64 N^(−2) epsilon_B².
Los dos exponentes 2 proceden de ceros espaciales cuadráticos, del radio
proporcional a N y de un ángulo de codificación fijo con término lineal
del seno no nulo. En el borde epsilon = 0 el perfil se anula: no se afirma
una cota inferior puntual uniforme s_N ≥ c N^(−2) en todo el disco.

Alice aporta s_N al término lineal y Bob aporta el efecto h_N una sola
vez. No se debe elevar h_N al cuadrado ni duplicar el orden de s_N como
si el líder fuese una probabilidad cuadrática de la fuente.

**Dependencia:** estas potencias están ligadas a los perfiles elegidos.
El Lema 6.1 de admisibilidad IR controla amplitud y diferencias discretas
O(N inversa); esa estimación no exige un cero exactamente cuadrático.
La admisibilidad completa también requiere cotas inferiores de sus
denominadores (§6). No se deduce una nueva clase admisible ni una potencia
alternativa únicamente cambiando el orden del cero en este conteo.

### 3.4. Áreas de capa: −1 −1; profundidades: 0

Cada plano de red tiene covolumen fijo sqrt(3). A profundidad delta,
la sección es un disco de radio sqrt(2R delta − delta²). Para profundidad
de orden uno y R proporcional a N, las dos coordenadas tangenciales
son de orden sqrt(N); el cambio u_perp = sqrt(2R) sigma aporta el
jacobiano 2R, de orden N, en cada capa. Eso resta uno a cada exponente.

Los planos se suman con delta = (theta_N+j)/sqrt(3) y peso
exp[−t_*(theta_N+j)], con t_* > 0 fijo. Sus momentos polinómicos se
acotan uniformemente en theta_N: la suma discreta no aporta una potencia
de N. Conserva, en cambio, la fase theta_N y las paridades.

La sustitución de sumas tangenciales por integrales usa Poisson, el cero
cuadrático del borde y derivadas terceras como medidas finitas; el error
relativo es O(N^(−3/2)) en el Lema 7.4. Contar área sin controlar el
muestreo sólo daría una heurística. Los desarrollos a profundidad acotada
se ensamblan con el peso exponencial y las cotas de capa, no suponiendo
que una expansión puntual sea uniforme hasta profundidad N.

**Dependencia:** geometría esférica, radio proporcional a N, contacto
cuadrático, red de planos y tilt positivo fijo. Si el tilt tendiese a cero,
si el contacto fuera plano o degenerado o si el radio cambiara de escala,
estas justificaciones dejarían de aplicar. La dirección tangencial común
es plana para el exponente y está confinada por los perfiles; no aporta
otro factor gaussiano además de las áreas ya contadas.

### 3.5. Integral de Fourier: 1/2 + 1

El Lema 7.1(d) proporciona un autovalor inclinado simple, proyector analítico
y Hessiano Q con autovalores q_n > 0 y q_t > 0 (doble), independientes
de N. La cancelación de la fase lineal deja exp(−N eta^T Q eta/2), con
resto cúbico controlado. Así la integral normal tiene escala N^(−1/2)
y d²eta_t = (2/N)d²tau aporta N inversa.

La integral tangencial conserva las funciones de capa S_±(tau;theta);
su coeficiente no es sólo un determinante gaussiano. Las profundidades
j,j' no son dos integrales gaussianas adicionales. La separación espectral,
el control del resto y el gap fuera de los ocho máximos completan la
localización. Sólo dos máximos contribuyen al orden principal por los
caracteres de red; los seis restantes se controlan con Poisson.

**Dependencia:** rango tres del Hessiano, gap, regularidad del símbolo,
geometría y estimaciones globales. Positividad puntual de Q en cada miembro
de una familia no basta para una estimación uniforme si sus autovalores
pueden acercarse a cero.

## 4. Qué significaría preservar el conteo

Manteniendo walk, nodo, tiempo, geometría y red originales, la parte
geométrica y gaussiana ya está fijada. Una futura variación de perfiles o
recurso necesitaría verificar las siguientes obligaciones antes de heredar
la potencia:

| Obligación | Qué permite conservar |
| --- | --- |
| Recurso reescalado normalizado, expansión de campo libre y trazas de capa controladas | Dos factores N^(−3/2) |
| Expansiones de capa de orden dos con coeficientes principales no triviales | Dos factores N^(−2) |
| Regularidad y cotas de muestreo y profundidad suficientes | Áreas, sumas y restos del Lema 7.4 |
| Control de todos los sectores y puntos del toro | Ensamblaje del Teorema 7.5 sin otra contribución mayor |
| Admisibilidad IR con denominadores controlados | Pertenencia al protocolo operacional exigido |
| Cota inferior del coeficiente real completo | Identificación del término dominante de delta |

Ésta es una lista de dependencias suficientes a verificar siguiendo la
prueba, no una caracterización necesaria y suficiente ni un teorema de
robustez ya probado para perfiles distintos. Mantener el orden del cero
es relevante, pero no basta por sí solo. La supresión por paridades y las
cotas de restos también dependen de la regularidad del perfil.

## 5. No anulación: obligación separada del conteo

En el protocolo original, Teorema 4.4 y estado §8.20 ya certifican para
los dieciséis pares

$$
L_N=e^{-K_*N}N^{-13/2}\bigl(C(\theta_N)+R_N\bigr),\qquad
|R_N|\le C' N^{-1/2},\qquad \inf_\theta|C(\theta)|>0.
$$

La positividad de E, del Hessiano o de amplitudes escalares separadas
no demuestra esa última desigualdad. El coeficiente es

$$
C(\theta)=\mathcal Kc_r\bigl[\Gamma_+(\theta)\ell_0
+\Gamma_-(\theta)\ell_\pi\bigr],
$$

donde ell_0 y ell_pi incluyen la contracción spinorial y la parte real
o imaginaria que selecciona cada encoder. La prueba existente acota
la suma completa mediante
|ell_0|(Gamma_bar−epsilon_+) > epsilon_- |ell_pi|.
Las funciones Gamma actuales usan ambos perfiles cuadráticos iguales;
no se heredan sus fórmulas de cuadrados ni sus cotas numéricas al variar
los perfiles de forma independiente.

Para una familia parametrizada por a, distinguir:

- resultado para cada a fijo: resto o(1) y margen positivo para ese a;
- resultado uniforme en la familia: resto o(1) uniforme y
  inf_(a,theta) |C_a(theta)| > 0.

Si C_a tiene ceros o se aproxima a cero a lo largo de las fases muestreadas,
el conteo no asegura dominancia uniforme. Si un líder desaparece, tampoco
puede proclamarse automáticamente 17/2 como nueva potencia: el resto
actual contiene correcciones anteriores que habría que expandir.

Una ruta condicional para preservar el margen, una vez justificada la
expansión de cada miembro, sería demostrar
sup_theta |C_a(theta)−C_0(theta)| < c_0/2 con
c_0 = inf_theta |C_0(theta)| > 0. La desigualdad triangular daría margen
c_0/2. No se ha definido aquí una topología de perfiles ni probado esa
continuidad o su uniformidad; ambas siguen pendientes.

## 6. Resultado y techo

FR1 parte de una descomposición analítica revisada en la clase congelada.
Queda identificado el papel de escala del recurso, ceros de perfil,
curvatura de las regiones, profundidad localizada, Hessiano, muestreo e
interferencia. Ninguno de esos papeles debe confundirse con una prueba
automática de universalidad del 13/2.

El siguiente problema acotado de FR1 es definir una clase de variaciones
con el mismo orden de borde y verificar las obligaciones de §4, incluido
el margen de §5. La robustez en esa clase queda OPEN. No se ha ensayado
otra dimensión, geometría, ventana, encoder ni detector; no se ha ejecutado
código científico ni una optimización. Los estados canónicos, FR2, FR3,
C2c y E/AdS no cambian. No hay commit ni push.
