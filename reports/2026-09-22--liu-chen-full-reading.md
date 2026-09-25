# Liu–Chen — lectura completa y herramientas para la corona

Fecha: 2026-09-22. Autor: Codex, agente `/root`.
Estado: **LECTURA ANALÍTICA / TRANSFERENCIAS PROPUESTAS**.

## 1. Fuente, alcance y diferencias entre problemas

K. Liu y D. Chen, *Maximal-velocity deficit under a finite-support constraint
in a hard-wall half-line continuous-time quantum walk*, Phys. Rev. A 114,
032434 (2026), [DOI](https://doi.org/10.1103/dyyr-z1k8),
[arXiv:2609.01970v2](https://arxiv.org/abs/2609.01970v2).
Fuente efectivamente leída: [PDF local de 16 páginas](../biblioteca/Maximal-velocity%20deficit%20under%20a%20finite-support_cn.pdf),
portada fechada el 17 de septiembre de 2026; SHA256:
`b49ef0fdd5944ece4fa50d48fbeb8ee2a4c7fbdb41b8638d1506cc95ce784a88`.

Se han leído cuerpo, apéndices A–C y bibliografía. Se reconstruyen abajo
pasos concretos, no una revisión independiente integral del artículo.
Las referencias citadas por éste se identifican como rutas bibliográficas;
no se consideran leídas sus pruebas originales. Los metadatos editoriales
son los comprobados en la [nota previa](2026-09-22--front-resource-scaling.md).
En esta sesión las consultas web a APS/arXiv fallaron; el análisis utiliza
el PDF local, no una supuesta nueva verificación editorial.

Entrada local: `f4f937e102def05f8797a94e256a460d81b0cc33`, con las notas
FR1, FR1–FR3, C2c y roadmap sin versionar. Se contrastan con el
[manuscrito](../papers/ir-corona/ir-corona.md), la
[auditoría FR1](2026-09-22--fr1-power-hypotheses.md) y
[C2c §§6–7](2026-09-22--c2c-structural-scope.md).

| Aspecto | Liu–Chen | Corona congelada |
| --- | --- | --- |
| Dinámica | CTQW de vecinos próximos en semirrecta, tiempo continuo | QCA CJWW tridimensional, pasos discretos |
| Recurso | Estado inicial arbitrario en los primeros M sitios | Recurso IR fijado; la operación U−I tiene soporte local |
| Cantidad | Media o transformada de la velocidad límite V | Diferencia firmada de expectativas L; delta = |L| |
| Límites | Primero velocidad asintótica a tiempo infinito; luego M grande y sesgo escalado | Tiempo, radios, separación y banda ligados a N |
| Potencia | Déficit de media óptima M^(−2) | Prefactor de respuesta N^(−13/2) e^(−K_*N) |

La ley débil de velocidad (7) no controla por sí sola respuestas
exponencialmente pequeñas que desaparecen en ese límite. Tampoco el
frente balístico 2J es un soporte causal estricto: e^(−itH) contiene
potencias arbitrarias de H y no hereda rango espacial finito a tiempo fijo.
No se identifica ese frente con C_micro o C_infty^strict del QCA.

## 2. Herramienta principal: separar cuatro pasos variacionales

La prueba contiene más estructura que el balance heurístico
M^(−2) = (M inversa)²:

1. **Reducción exacta finita**, (18)–(24): matriz hermítica del observable
   comprimida a la clase completa de estados de soporte M.
2. **Convergencia de los óptimos**, Apéndice A.1(c): control en norma de
   operador después de encajar los espacios discretos en un espacio común.
3. **Cota que impide mejorar el líder**, (55)–(60), A.3 y A.5: Jensen,
   compactación de casi minimizadores y desigualdad de Dirichlet.
4. **Familia que alcanza el líder**, A.4: muestreo de perfiles suaves,
   normalización, control de aliases por Poisson y aproximación en H¹₀
   al coseno óptimo.

En concreto, para d_M = min E[Delta_M], Jensen da

$$
d_M\ge-\frac{\log G_M(u)}u,\qquad
\liminf_{M\to\infty}d_M\ge-\frac{\log\lambda(u)}u.
$$

Se toma después u hacia cero para obtener la cota pi²/4. La familia de
prueba da el limsup contrario. No se intercambia sin justificación
derivación, máximo y límite.

**Uso para nosotros:** una construcción de encoder con cierta respuesta
no prueba optimalidad. Harían falta una cota para toda la clase admisible
y una familia realizable que la alcance. El signo de L impide aplicar
directamente el argumento de Jensen, que aquí usa un defecto no negativo.
Esta lectura no abre ni resuelve FR2.

## 3. El argumento de convergencia que sí merece conservarse

Apéndice A.1(c), (A14)–(A26):

- La simetría de paridad descompone exactamente las matrices discretas.
- El peso reescalado W_M^(u) converge en L¹ a exp(−u xi²), para u > 0
  fijo. Una cota de suma de filas convierte ese error en error de operador.
- La matriz gaussiana es una discretización por cuadratura de un kernel
  continuo, cuya diferencia respecto de promedios de celda se controla
  por un módulo de continuidad.
- Las proyecciones de celda convergen fuertemente. Al comprimir un
  operador compacto localizado, eso produce convergencia en norma.
- Min–max transfiere finalmente el autovalor máximo.

El último paso no se deduce de convergencia fuerte sola. La compacidad y
el control uniforme de la discretización son esenciales. Tampoco se
demuestra aquí uniformidad al llevar simultáneamente u a cero: el kernel
gaussiano se estrecha y en u = 0 el límite deja de ser compacto.

Si alguna vez se formula un operador de corona, este esquema especifica
qué debe probarse. Un gráfico de autovalores convergentes no sustituye
estos pasos. En una familia autoadjunta, un control en norma también
proporcionaría estabilidad de los extremos espectrales; la construcción
de esa familia para nuestra señal sigue pendiente.

## 4. Sobolev y bordes: lo que un corte duro permite y lo que no

En §VI.B y A.5, escribir

$$
g(\xi)=\frac1{\sqrt{2\pi}}\int_{-1}^1 f(p)e^{ip\xi}\,dp
$$

identifica segundo momento finito con extensión por cero de f en H¹(R),
equivalentemente f en H¹₀(−1,1), y entonces

$$
\int_{\mathbb R}\xi^2|g(\xi)|^2d\xi
=\int_{-1}^1|f'(p)|^2dp.
$$

La condición de borde no es decorativa: una traza no nula genera un salto
en la extensión por cero y términos delta en su derivada distribucional.
El Apéndice A.5 obtiene el dominio H¹₀ a partir de compactación y energía,
en vez de imponerlo informalmente al principio.

**Deducción de esta lectura:** para f suficientemente suave, controlar
momentos de orden 2m requiere controlar la derivada m de la extensión por
cero. Anular las trazas de f, f', ..., f^(m−1) elimina los términos de
borde y permite la identidad de Plancherel de orden m. No basta conocer
una anchura de pico. Esta observación se refiere a una transformada 1D;
no transfiere potencias de cola a nuestra geometría tridimensional.

Para C2c, el antecedente apoya las colas inducidas por proyección, pero
no su compensación. Además, p es conjugado de xi = M(k−pi/2), no el
momento microscópico IR de nuestro protocolo. Las variables deben
identificarse antes de trasladar una condición funcional.

## 5. Dos consecuencias adicionales sobre los estados óptimos

Las siguientes son **deducciones analíticas de esta lectura, sin revisión
independiente**, no teoremas nuevos atribuidos textualmente a los autores.

### 5.1. El óptimo de sesgo fijo tiene segundo momento infinito

Para u > 0, (45)–(46) da el kernel

$$
K_u(p,q)=(4\pi u)^{-1/2}e^{-(p-q)^2/(4u)}.
$$

Su autovector principal normalizado f_u es suave, par y positivo. La
ecuación integral se prolonga continuamente a p = ±1 y da
f_u(±1) > 0. Por tanto su extensión por cero no está en H¹(R).
La transformada inversa g_u, que optimiza la forma bandlimited (44),
satisface, integrando por partes dos veces,

$$
g_u(\xi)=\sqrt{\frac2\pi}\,f_u(1)\frac{\sin\xi}{\xi}
+O(|\xi|^{-2}),\qquad
\int\xi^2|g_u(\xi)|^2d\xi=\infty.
$$

Esto no contradice el paper: el objetivo para u fijo es una integral
acotada con peso exp(−u xi²), que no penaliza las colas como el segundo
momento. La afirmación concierne a la envolvente bandlimited g_u, no al
autovector gaussiano de T_u en su otra representación ni a los momentos
del problema discreto a M finito, donde Delta_M está acotado.

### 5.2. El óptimo de la media tampoco controla todos los momentos

El estado f_*(p) = cos(pi p/2), normalizado en (−1,1), tiene

$$
g_*(\xi)=\frac{\pi}{\sqrt{2\pi}}
\frac{\cos\xi}{\pi^2/4-\xi^2},
$$

con singularidades removibles en xi = ±pi/2. Su cola tiene amplitud de
orden xi^(−2), de modo que

$$
\int\xi^2|g_*|^2d\xi=\pi^2/4,
\qquad \int\xi^4|g_*|^2d\xi=\infty.
$$

Así, el defecto continuo xi² tiene media finita y segundo momento
infinito en este perfil. No se infiere de ello una fórmula concreta para
la segunda derivada de la envolvente optimizada lambda(u), porque el
optimizador depende de u. Sí impide deducir una jerarquía de momentos
finitos del mero conocimiento del óptimo de la media. §IX, (69), deja
precisamente condicionada la discusión de cumulantes superiores.

**Consecuencia práctica:** no identificar optimalidad de media, masa en
ventana, cola, momento y señal. Cada objetivo selecciona su propia clase
de regularidad y puede seleccionar otro perfil.

## 6. Un kernel de calor comprimido no es ya un Laplaciano de Dirichlet

La fórmula (46) es el kernel de calor de la recta, restringido en entrada
y salida a (−1,1). No es el kernel del semigrupo de calor con condición
de Dirichlet en ese intervalo: este último impone condiciones de frontera
durante la evolución. La diferencia también se ve en f_u(±1) > 0.

Por ello no se puede reemplazar lambda(u) por exp(−pi²u/4) para todo u.
Dirichlet emerge en el límite de la forma de energía (1−S_u)/u, que
A.5 estudia, y determina la pendiente en cero. La pendiente no determina
la función de escala completa ni su siguiente corrección.

Esto delimita la analogía con FR3: encontrar una energía límite no equivale
a haber identificado el operador para todo el parámetro de escala.

## 7. Paridad y Gram: una herramienta concreta para no anulación

El Apéndice C prueba, para bloques pares e impares de la matriz de media,

$$
a^\dagger(A_e^{(r)}-A_o^{(r)})a
=\frac{2J}{\pi}\int_0^1
\left|\sum_{i=0}^{r-1}a_i x^{2i}\right|^2(1-x^2)^2dx>0
\quad(a\ne0).
$$

La positividad estricta viene de independencia de polinomios en un
intervalo. Permite ordenar los máximos espectrales y deducir exactamente
v_opt(2r−1) = v_opt(2r). El recurso adicional puede entrar en un sector
que no mejora el óptimo. Para pesos decrecientes, C.2 obtiene una
comparación de cocientes de Rayleigh mediante una covarianza de signo
conocido; no necesita volver a diagonalizar para demostrar la selección.
La meseta no se hereda entre M sucesivos para A_u^(M), cuyo peso cambia
con M.

**Conexión concreta:** C2c §§6–7 usa una matriz de Gram de funciones
racionales y su independencia para excluir cancelaciones entre fases.
La estrategia matemática es análoga. Esto no revisa ni valida aquella
prueba, que permanece `PROOF_WRITTEN / REVIEW_PENDING`.

Una vez demostrado G > 0 para una familia finita, una perturbación
hermítica con ||G_tilde−G|| < lambda_min(G)/2 conserva un margen positivo.
Para una familia infinita hace falta un margen uniforme. El coeficiente
firmado del 13/2 no es sin más esa Gram positiva: exige su propio control
de interferencias y parte real/imaginaria.

## 8. Qué reducción positiva tenemos disponible como identidad

La factorización (43), AA† frente a A†A, sugiere aislar formas positivas
antes de optimizar un observable firmado. Sea J_A la inclusión isométrica
de los espinores soportados en la región finita de Alice y defínase

$$
B_N=E^{1/2}S^N P J_A.
$$

Para una fuente local a = J_A b,

$$
\mathcal Q_N(a)=\|B_Nb\|^2,\qquad
\sup_{\|b\|=1}\mathcal Q_N(J_Ab)
=\lambda_{\max}(B_N^\dagger B_N).
$$

Es una identidad de álgebra lineal para una **relajación sobre fuentes
arbitrarias normalizadas**. La fuente real es (U−I)phi_N y debe satisfacer
realizabilidad unitaria y restricciones IR. Además, Q_N es un bloque
proyectado cuyas contribuciones pueden cancelarse al reconstruir L;
maximizarlo no equivale a maximizar señalización. No se ha ensamblado ni
evaluado esta matriz. Esta observación no ejecuta FR2.

El contraste coherente/incoherente del artículo, v_inc = 16J/(3pi)
independiente de M, también es útil como método de diseño de controles.
Pero desfasar sin más nuestro recurso en posición puede destruir la
restricción IR; no sería automáticamente un control del mismo protocolo.

## 9. Qué aprovechar ahora, manteniendo FR1 como único trabajo activo

La aplicación inmediata es preparar una clase de perturbaciones que
conserve órdenes de borde, geometría, ventana y amplitudes de capa, y
demostrar estabilidad del coeficiente completo con restos uniformes.
Una posible parametrización para un futuro contrato, no ejecutada, sería
F_epsilon = F_0(1+epsilon a), h_epsilon = h_0(1+epsilon b) en coordenadas
reescaladas, y g_epsilon proporcional a g_0(1+epsilon c), con normas
de regularidad uniformes y normalización. Habría que fijar además cotas
de positividad, 0 ≤ E ≤ I y admisibilidad IR; la forma multiplicativa
sola no verifica estas obligaciones.

El objetivo candidato sería, para |epsilon| pequeño,

$$
L_{N,\epsilon}=e^{-K_*N}N^{-13/2}
\bigl(C_\epsilon(\theta_N)+R_{N,\epsilon}\bigr),
\quad \sup_\epsilon\|R_{N,\epsilon}\|=o(1),
\quad \inf_{\epsilon,\theta}|C_\epsilon(\theta)|>0.
$$

Para el margen bastaría probar continuidad uniforme respecto del caso
congelado en una topología especificada, con variación menor que la mitad
de su margen original. La continuidad de C, la uniformidad de los restos
y la pertenencia a la clase admisible son trabajos pendientes. Este sería
un resultado de robustez local, no optimalidad ni universalidad entre QCA.

| Prioridad | Extracción | Situación |
| --- | --- | --- |
| Inmediata, FR1 | Bordes, dominios funcionales, control de momentos y margen uniforme del coeficiente | Útil para congelar la siguiente clase |
| Referencia de C2c | Corte duro, colas y prueba por Gram | Analogía comprobada; revisión de C2c pendiente |
| Reserva FR2 | Reducción exacta o relajación, más cota y familia realizable | No ejecutada |
| Reserva FR3 | Convergencia en norma por compacidad y cuadratura, con fases de red conservadas | No ejecutada |

Apéndice B ofrece ensamblaje Toeplitz–Hankel y cuadratura simétrica
sqrt(w_i) K(p_i,p_j) sqrt(w_j), útiles si se llega a un problema integral.
Sus controles numéricos son refinamientos de malla; no sustituyen cotas
certificadas uniformes en u ni justifican ahora un nuevo barrido.

La bibliografía abre las rutas Slepian–Pollak/Landau–Pollak [33–34],
Widom [35–36], Nyström [51] y compacidad de Kolmogorov–Riesz [53].
La referencia [11] es Cedzich–Joye–Werner–Werner, ya central en nuestro
proyecto: hay continuidad bibliográfica, no una demostración de novedad.

No se modifica el manuscrito, el estado canónico ni los contratos. E/AdS
sigue congelado. No hay simulaciones, scripts científicos nuevos, commit
ni push. La conclusión es metodológica y de alcance; el artículo no
demuestra nuestro 13/2, su optimalidad ni su estabilidad de clase.
