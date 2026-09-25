# FRONT-RESOURCE SCALING — lectura y propuesta FR1–FR3

Fecha: 2026-09-22. Estado: **PROPUESTA TEÓRICA / OPTIMALIDAD ABIERTA**.
Entrada local: `f4f937e102def05f8797a94e256a460d81b0cc33`, más los
informes no versionados de roadmap y C2c presentes al iniciar esta lectura.
Esta nota registra la propuesta del usuario y comprueba sus conexiones con
las fuentes. No ejecuta una optimización ni certifica un operador límite.

Lectura posterior del cuerpo y apéndices A–C:
[herramientas y límites de Liu–Chen](2026-09-22--liu-chen-full-reading.md).
Incluye la convergencia de óptimos, la comparación de paridades y la
distinción entre perfiles óptimos para la media y para sesgo fijo.

## 1. Fuente comprobada

Kangqiao Liu y Deyou Chen, *Maximal-velocity deficit under a finite-support
constraint in a hard-wall half-line continuous-time quantum walk*,
**Physical Review A 114, 032434 (2026)**,
[DOI: 10.1103/dyyr-z1k8](https://doi.org/10.1103/dyyr-z1k8),
[arXiv:2609.01970v2](https://arxiv.org/abs/2609.01970v2).

- La [ficha de aceptación de APS](https://journals.aps.org/pra/accepted/10.1103/dyyr-z1k8)
  registra aceptación el 1 de septiembre de 2026; la
  [ficha publicada](https://journals.aps.org/pra/abstract/10.1103/dyyr-z1k8)
  registra publicación el 15 de septiembre.
- arXiv fecha la entrega de v2 el 15 de septiembre. La portada del
  [PDF local](../biblioteca/Maximal-velocity%20deficit%20under%20a%20finite-support_cn.pdf)
  dice 17 de septiembre. Son fechas distintas de metadatos, no una nueva
  versión inferida a partir de la portada.
- SHA256 del PDF leído:
  `b49ef0fdd5944ece4fa50d48fbeb8ee2a4c7fbdb41b8638d1506cc95ce784a88`.

La lectura comprobó §§IV–VI y las fórmulas indicadas abajo; no constituye
una auditoría independiente completa de todas las pruebas del artículo.

| Resultado de la fuente | Localización | Uso aquí |
| --- | --- | --- |
| Optimización de MGF y deriva media por matrices hermíticas finitas | (18)–(24) | Modelo de reducción variacional |
| Defecto escalado y límite conjunto | (30)–(39), (48) | Separar tamaño de preparación, tiempo y sesgo |
| Proyector sinc y operador gaussiano | (40)–(47) | Concentración bajo una ventana de Fourier |
| Déficit de deriva media óptima, coeficiente pi²/4 | (49)–(65) | Ejemplo de exponente explicado por geometría y recurso |
| Segundo momento, trazas nulas y Laplaciano de Dirichlet | §VI.B, (66)–(67) | Antecedente de colas inducidas por cortes duros |

## 2. Transferencia conceptual y límites

El artículo demuestra, para su CTQW en una semirrecta y su clase de estados,

\[
2J-v_{\mathrm{opt}}(M)=\frac{\pi^2J}{4M^2}+o(M^{-2}).
\]

Aquí se optimiza la **media de la velocidad límite**; el frente balístico
sigue en 2J. El exponente combina un máximo cuadrático de velocidad y una
resolución de momento de orden M inversa. El coeficiente exige el problema
variacional: no lo determina por sí sola la estimación de anchura.

En el operador continuo, p es conjugado de la variable ampliada
xi = M(k − pi/2). El corte |p| ≤ 1 no debe identificarse literalmente
con nuestra ventana IR microscópica. Para sesgo u > 0,
T_u = M_{u/2} P M_{u/2} es compacto; en u = 0 se obtiene P, que no es
compacto en el espacio completo. Además, lambda(u) optimiza separadamente
para cada u: no es automáticamente la transformada de una única
distribución óptima para todos los sesgos.

La condición H¹₀(−1,1) equivale al segundo momento finito de la envolvente
inversa de Fourier, con la regularidad y normalización de §VI.B. Trazas
no nulas producen colas lentas; trazas nulas no restauran soporte compacto.
Esta es una referencia externa pertinente para
[C2c §9.2](2026-09-22--c2c-structural-scope.md), pero no demuestra su
compensación localizada ni el patrón +1:+1:−2. C2c tiene estado
`PROOF_WRITTEN / REVIEW_PENDING`; C2b conserva su PASS para sigma2/I.

## 3. FR1 — hacer explícita la estructura ya demostrada

El punto de partida no es una descomposición empírica: el
[manuscrito, Lema 7.4, Teorema 7.5 y Observación 7.6](../papers/ir-corona/ir-corona.md)
ya da la contabilidad analítica en el protocolo congelado:

\[
\boxed{\frac{13}{2}
=\underbrace{\left(\frac32+2-1\right)}_{\text{Alice}}
+\underbrace{\left(\frac32+2-1\right)}_{\text{Bob}}
+\underbrace{\left(\frac12+1\right)}_{\text{integral gaussiana}}.}
\]

| Factor | Potencia aportada al exponente de decaimiento |
| --- | --- |
| Recurso en Alice y campo libre de referencia en Bob | 3/2 + 3/2 |
| Ceros cuadráticos de s_N y h_N en las capas relevantes | 2 + 2 |
| Dos áreas tangenciales, cada una de orden N | −1 −1 |
| Integral normal y reescala de dos variables tangenciales | 1/2 + 1 |
| Sumas discretas de profundidad con peso exponencial | 0 |

La dirección tangencial común está confinada por los perfiles; no se debe
contar además como una dirección gaussiana. Las dos contribuciones de
saddle, sus paridades y matrices internas entran en C(theta_N). La prueba
de no anulación impide que su interferencia elimine el líder en los
dieciséis pares congelados. No hay una potencia adicional de cancelación
que deba sumarse aquí. La cancelación de bloques de C2b/C2c es otro nivel
de descripción y no se usa para rededucir este 13/2.

**Siguiente obligación FR1:** identificar qué hipótesis de cada factor
se conservan al variar un recurso admisible. Toda ley para otros órdenes
de cero, dimensiones o geometrías exige controlar de nuevo capas, saddles,
restos y no anulación. El conteo actual no certifica universalidad ni
estabilidad inhomogénea. No hay evidencia aquí para identificar j = 13/2.

**Lectura de dependencias, 2026-09-22:** la
[auditoría FR1](2026-09-22--fr1-power-hypotheses.md) precisa las hipótesis
de cada contribución, el control de restos y el margen de no anulación.
La robustez para una nueva clase de perfiles o recursos permanece abierta.
Esta ejecución se limita a FR1.

## 4. FR2 — distinguir estado, fuente y encoder

Para U y E fijos, definir exactamente

\[
H_N=(S^N)^\dagger E S^N,\qquad K_N(U)=U^\dagger H_NU-H_N.
\]

Entonces L_N(psi) = <psi,K_N(U)psi>. Si se permite variar psi sobre **toda**
la esfera de un subespacio finito V, con proyector R_V, Rayleigh–Ritz da

\[
\sup_{\psi\in V,\ \|\psi\|=1}L_N(\psi)
=\lambda_{\max}(R_VK_N(U)R_V|_V),\qquad
\sup_{\psi\in V,\ \|\psi\|=1}|L_N(\psi)|
=\|R_VK_N(U)R_V|_V\|.
\]

Es una identidad algebraica para ese problema de estados. Nuestro recurso
phi_N está fijado, es bandlimited y tiene cola espacial: imponerle soporte
finito cambia el protocolo. El soporte finito de Alice pertenece a U−I.
Además, restricciones IR adicionales pueden hacer que el conjunto
admisible sea una parte de la esfera y destruir la igualdad variacional.

Para optimizar U con phi_N fijo, la fuente a = (U−I)phi_N satisface

\[
L_N=2\operatorname{Re}\langle S^N\phi_N,E S^Na\rangle
+\langle S^Na,E S^Na\rangle.
\]

Hay un término lineal y restricciones de realizabilidad unitaria, localidad
y admisibilidad IR sobre a. Un autovalor de una relajación no demuestra que
su autovector sea un encoder realizable. Si se optimiza la distinguibilidad
completa de Bob, también cambia el objetivo: delta = |L| es el test con
efecto fijado, no en general la distancia de traza optimizada.

**Contrato necesario antes de resolver FR2:** fijar recurso, conjunto de
encoders, norma/presupuesto, geometría de Alice, detector, restricciones IR
y relación entre tamaño de soporte y N. Reservar M para la matriz interna
existente y usar, por ejemplo, ell_A para la longitud de preparación; en
tres dimensiones longitud y número de sitios no son intercambiables.

**Cierre exigido:** reducción exacta para la clase declarada, o relajación
con cota superior y construcción admisible que alcance su líder. Deben
separarse optimalidad de tasa exponencial, de potencia y de coeficiente.
Un fracaso de la reducción espectral simple es un resultado válido.

## 5. FR3 — operador límite y función de escala

La ley actual contiene theta_N = {sqrt(3)N/4}, no un coeficiente constante.
Una primera formulación candidata debe permitir F(z,theta), o especificar
subsecuencias con fase convergente. Un promedio sobre theta sería un
observable nuevo. También debe definir qué geometría varía con v.

Antes de fijar z = N^beta(v−v_*), expandir la tasa K(v). Si su primera
variación relevante es de orden r, mantener N[K(v)−K(v_*)] de orden uno
sugiere beta = 1/r; esto es un balance condicional, no un exponente probado
para una familia nueva. Debe comprobarse además si cambian las capas o
degeneran los saddles.

Un T_corona requiere espacio, dominio, reescalamiento, normalización,
topología de convergencia y control suficiente de los extremos espectrales.
K_N puede ser firmado: para |L| pueden importar ambos extremos del espectro,
y no se hereda positividad ni un autovalor principal simple de T_u.
Convergencia fuerte por sí sola no basta para transferir los óptimos.

La regla heurística déficit ~ ell_A^(−r) para un máximo de orden r exige
una familia que alcance la concentración, una cota variacional inferior y
control de las colas. En varias dimensiones deben fijarse anisotropía,
codimensión y costes de preparación; un punto de Dirac no determina por sí
solo estos datos.

## 6. Secuencia y techo de conclusión

1. FR1: usar la prueba existente como inventario de dependencias.
2. FR2: congelar la clase de optimización y derivar su formulación exacta.
3. FR3: sólo después, estudiar convergencia del problema reescalado y
   eventual función de escala, conservando las fases necesarias.

El objetivo futuro de optimalidad por localización finita permanece OPEN.
Esta nota no autoriza barridos, ajustes, sustitución de perfiles ni cambios
del observable congelado. E/AdS continúa congelado; H1, H1c, E0 y
POWER_13/2_STABILITY no reciben una promoción. No modifica el estado
canónico, el manuscrito ni las pruebas previas. No hay commit ni push.
