# Proyección IR: fuga real, compresión y condicionamiento

Fecha: 2026-09-22. Base leída y actualizada desde GitHub: `2b29b19`, rama
`research/b-infinity-post-s4-gate`. Continuación de la pregunta C solicitada
por el usuario, después de leer `biblioteca/QCAQW inhomogeneas.md`.

**Estado: PRELIMINARY / ANALYTIC_DERIVATION_WRITTEN / NOT_INDEPENDENTLY_REVIEWED.**
Las identidades algebraicas tienen un verificador separado; éste no formaliza
los argumentos de Fourier, Poisson ni los restos asintóticos de esta nota.
No se modifica el estado canónico, el manuscrito ni el resultado plano.

## 1. Alcance y criterio de interpretación

Se conserva exactamente el walk CJWW (5.15), nodo cero, dos componentes,
recurso, regiones y perfiles de las secciones 2–3 del
[manuscrito](../papers/ir-corona/ir-corona.md). Se fija
`P = Pi' = 1_{|p| <= N^{-1/2}}`, `Q = I-P` y `Lambda = N^{-1}`.
Las fórmulas de fuga se derivan para los cuatro encoders originales
`M in {I, sigma1, sigma2, sigma3}`; el resultado sobre Bob condicionado
se restringe a `M_B = I`, incluyendo el par `sigma2/I` ya diagnosticado.
No se cambia de filtro, modelo o escala, ni se ejecuta una serie numérica.

Se distinguen tres preguntas:

1. ¿Es pequeña la compresión en norma **respecto a la señal**?
2. ¿Domina el bloque PP el observable concreto, es decir, `L-Lpp=o(|L|)`?
3. ¿Qué observable resulta de proyectar y normalizar físicamente?

Un fallo de 1 no demuestra un fallo de 2. Una fórmula para 3 no es una
fórmula para 2. Esta separación fija el alcance de las conclusiones.

La [auditoría incorporada de GitHub](2026-09-22--ir-spectral-attribution-audit.md)
ya registra cancelaciones PP/complemento en N=24 y N=40. No se extrapolan.

## 2. La compresión tiene un defecto de traza exacto

Escribamos, suprimiendo N y M,
\[
v=U_M\phi,\quad a=(U_M-I)\phi,\quad w=Pv,\quad t=Qv=Qa,
\quad q=\|t\|^2,\qquad P\phi=\phi.
\]
Como v está normalizado, `||w||^2=1-q` y `w` es ortogonal a `t`. Para
\[
\Delta=|v\rangle\langle v|-|\phi\rangle\langle\phi|,
\qquad \Delta_{PP}=P\Delta P,
\]
se obtiene
\[
\operatorname{tr}\Delta_{PP}=-q,
\qquad
\Delta-\Delta_{PP}=|w\rangle\langle t|+|t\rangle\langle w|+|t\rangle\langle t|.
\]
En la base ortonormal de w y t, el segundo operador es
\[
\begin{pmatrix}0&\sqrt{q(1-q)}\\\sqrt{q(1-q)}&q\end{pmatrix}.
\]
Sus autovalores son `(q +/- sqrt(4q-3q^2))/2`; por tanto
\[
\boxed{\|\Delta-P\Delta P\|_1=\sqrt{4q-3q^2}.}
\tag{1}
\]
La fórmula se extiende por continuidad a q=0,1.

Para estos encoders, a tiene soporte finito y no es nulo. Si `Qa=0`, su
transformada, un polinomio trigonométrico vectorial, se anularía en el
abierto exterior a la bola IR; analiticidad obliga a `a=0`. Así q>0.
La fuente no es nula ya en x=0, donde `F_N=1`, `Phi_0(0)>0` y
`exp(i pi M/2)-I` no anula el espinor. No existe una perturbación no nula
simultáneamente de soporte finito y estrictamente limitada a esta banda.

## 3. Fuga del protocolo congelado: una asintótica algebraica

Sea `b=1/4`, `chi=down`, `F(r)=(1-16r^2)^2` para `0<=r<=b` y cero fuera.
El recurso satisface exactamente
\[
\phi_N(x)=N^{-3/2}\Phi_0(x/N)\chi.
\]
Definimos la función radial vectorial de soporte compacto
\[
A_M(X)=\Phi_0(X)
\left[(\cos(\tfrac\pi2F(|X|))-1)\chi
       +i\sin(\tfrac\pi2F(|X|))M\chi\right].
\]
Entonces `a_N(x)=N^{-3/2} A_M(x/N)` exactamente. Escribamos
\[
B=\Phi_0(b)
=\frac{\sqrt{3465}}{64\pi^2}\,16\pi
\int_0^1 k(1-k^2)^2\sin(k/4)\,dk>0.
\]
La positividad procede del integrando, sin evaluación decimal.

### 3.1. Borde de Alice y cola de Fourier continua

Para `t=b-r` positivo y pequeño,
\[
F(b-t)=64t^2+O(t^3),\qquad
A_M(b-t)=i32\pi B\,M\chi\,t^2+O(t^3).
\]
La parte proporcional a `cos-1` empieza en orden `t^4`. La función es
suave y par radial cerca del origen, analítica hasta el borde desde dentro,
y C1 después de extenderla por cero. Con la convención
`Ahat(k)=integral exp(i k.X) A(X) dX`, para `k=|k|`,
\[
\widehat A_M(k)=\frac{4\pi}{k}\int_0^b r A_M(r)\sin(kr)\,dr.
\]
Sea `h(r)=r A_M(r)`. Sus datos de borde son
\[
h(0)=h''(0)=h(b)=h'(b)=0,\qquad h''(b)=i16\pi B M\chi.
\]
Tres integraciones por partes, y una más para acotar el resto, dan
\[
\boxed{\widehat A_M(k)=i64\pi^2B M\chi\,
            \frac{\cos(k/4)}{k^4}+O(k^{-5}).}
\tag{2}
\]
El resto es uniforme en dirección porque A es radial. En particular
`||Ahat_M(k)|| <= C(1+|k|)^{-4}`. Los cuatro M tienen `||M chi||=1`.

Integrando el cuadrado fuera de radio K, con medida `d^3k/(2pi)^3`,
\[
\begin{aligned}
\frac1{(2\pi)^3}\int_{|k|>K}\|\widehat A_M(k)\|^2\,d^3k
&=2048\pi^2B^2\int_K^\infty k^{-6}\cos^2(k/4)\,dk+O(K^{-6})\\
&=D K^{-5}+O(K^{-6}),\qquad
D=\frac{1024\pi^2B^2}{5}>0.
\end{aligned}
\tag{3}
\]
Se usa `cos^2(k/4)=(1+cos(k/2))/2`: el término no oscilatorio integra
a `K^{-5}/10`, y una integración por partes acota el oscilatorio por
`O(K^{-6})`. No se reemplaza una función oscilatoria por una cota inferior
puntual.

### 3.2. Control del muestreo de la red

Es necesario comprobar que (3) se aplica al protocolo discreto, sin
confundirlo con un modelo continuo nuevo. La fórmula exacta de Poisson es
\[
\widehat a_N(p)=N^{3/2}\sum_{m\in\mathbb Z^3}
                 \widehat A_M(Np+2\pi Nm).
\]
Es legítima aquí: A es continua y compacta, su transformada es integrable
y la serie de imágenes converge absolutamente por el decaimiento de orden 4.
En `C_N=[-pi N,pi N]^3`, las imágenes `m != 0` satisfacen
\[
\left\|\sum_{m\ne0}\widehat A_M(k+2\pi Nm)\right\|\le C N^{-4},
\]
uniformemente: `|k+2pi Nm| >= c N |m|` y `sum_{m != 0}|m|^{-4}<infinity`.
Su norma L2 en C_N es `O(N^{-5/2})`.

Después de cambiar `k=Np`, el corte P es `|k|<=sqrt(N)`. La norma L2 de
la imagen central en su complemento es `O(N^{-5/4})` por (3). Por
Cauchy–Schwarz, el término cruzado con las imágenes es `O(N^{-15/4})`,
y su cuadrado es `O(N^{-5})`. La masa central fuera del cubo es también
`O(N^{-5})`. Estos errores son menores que el resto `O(N^{-3})` de (3).
En consecuencia, para cada uno de los cuatro encoders originales,
\[
\boxed{q_N=\|Q(U_M-I)\phi_N\|^2
       =D N^{-5/2}\bigl(1+O(N^{-1/2})\bigr).}
\tag{4}
\]
La constante líder es la misma para los cuatro, no depende de Bob y no
afirma igualdad de las fugas a N finito.

### 3.3. Consecuencia para el error de atribución en norma

Combinando (1) y (4),
\[
\boxed{\|\Delta-P\Delta P\|_1
       =2\sqrt D\,N^{-5/4}\bigl(1+O(N^{-1/2})\bigr).}
\tag{5}
\]
Es una mejora del control superior original `O(N^{-1/2})` y además
identifica un coeficiente positivo. El denominador `||Delta||_1` de la
admisibilidad relativa está acotado por debajo en el protocolo original y
por arriba por 2; esa admisibilidad relativa tiene orden `Theta(N^{-5/4})`.

Una cota superior `epsilon=O(N^{-1/2})` **por sí sola no implica**
`epsilon/delta -> infinity`: epsilon podría ser exponencialmente menor.
La equivalencia positiva (5) sí permite concluir, usando la ley TOTAL ya
registrada y el coeficiente uniformemente no nulo,
\[
\frac{\|\Delta-P\Delta P\|_1}{\delta_N}
=\frac{2\sqrt D}{|C_{M,M_B}(\theta_N)|}
 N^{21/4}e^{K_*N}\bigl(1+O(N^{-1/2})\bigr)\longrightarrow\infty.
\tag{6}
\]
Esto rechaza el criterio suficiente de fidelidad en norma a escala de la
señal. **No** demuestra `|L-Lpp|/|L| -> infinity`: el observable concreto
puede cancelar partes de un operador grande en norma traza.

## 4. Proyectar y condicionar produce otro observable

Si se realiza una medición global `{P,Q}` y se retiene el resultado P,
las probabilidades de éxito son 1 para el bit cero y `1-q_N` para el bit uno.
Para N suficientemente grande, `q_N<1`. La diferencia entre los estados
condicionados es
\[
\Delta_{\rm cond}=\frac{|w\rangle\langle w|}{1-q}-|\phi\rangle\langle\phi|
=\frac{\Delta_{PP}+q|\phi\rangle\langle\phi|}{1-q}.
\]
Con `p0_N=<S^N phi,E S^N phi>` y el mismo efecto de Bob,
\[
\boxed{L_{\rm cond}=\frac{L_{PP}+q_Np0_N}{1-q_N},\qquad
L_{\rm cond}-L_{PP}=\frac{q_N(p0_N+L_{PP})}{1-q_N}.}
\tag{7}
\]
Lpp es la diferencia de probabilidades conjuntas de éxito P y detección;
no es la diferencia de probabilidades condicionadas. Su valor absoluto no
es, sin especificar ese protocolo global, la distinguibilidad del
experimento local original.

Para `M_B=I`, el límite del recurso libre del manuscrito da
\[
p0_N\longrightarrow p_\infty
=\int_{|w-u|<1/4}(1-16|w-u|^2)^2\|R_0(w)\|^2\,d^3w>0.
\]
La convergencia sigue de la expansión uniforme del recurso y sumas de
Riemann. La positividad no exige cálculos numéricos: R0 es la transformada
de Fourier de una función compacta no nula, luego es analítica y no puede
anularse en una bola abierta. El peso es positivo en el interior.

Además `|L-Lpp| <= ||Delta-PDeltaP||_1 -> 0` y `L -> 0`, de donde
`Lpp -> 0`. Por (4) y (7),
\[
\boxed{L_{\rm cond}-L_{PP}
       =D p_\infty N^{-5/2}(1+o(1)),\qquad M_B=I.}
\tag{8}
\]
La corrección por normalización es algebraica y positiva, muchísimo mayor
que la señal total exponencial. (8) no fija el término líder de Lcond ni
de Lpp por separado; podría haber cancelación entre ellos y la corrección.

## 5. El proyector ya introduce alcance espacial infinito

La bola del corte está dentro de la celda de Brillouin. Su núcleo escalar
exacto, multiplicado por la identidad interna, es, para `r=|x-y|>0`,
\[
P_N(x,y)=\frac{\sin(\lambda r)-\lambda r\cos(\lambda r)}{2\pi^2r^3}I,
\quad \lambda=N^{-1/2},\qquad
P_N(x,x)=\frac{\lambda^3}{6\pi^2}I.
\]
A distancia `r=sN`, con `s>0` fijo,
\[
P_N(x,y)=\left[-\frac{\cos(s\sqrt N)}{2\pi^2s^2N^{5/2}}
 +\frac{\sin(s\sqrt N)}{2\pi^2s^3N^3}\right]I.
\tag{9}
\]
Esto es una identidad oscilatoria, no una cota inferior uniforme ni una
asintótica demostrada para Lpp. La proyección deja de conservar el soporte
local de la perturbación. Una respuesta después de aplicarla no se puede
interpretar automáticamente como propagación desde la región original de
Alice. Sustituir P por un filtro suave también cambiaría el contrato y
requeriría un análisis propio.

## 6. Resultado y siguiente obligación matemática

| Afirmación | Alcance de esta continuación |
| --- | --- |
| Error real de compresión en norma | Derivación de `Theta(N^{-5/4})`, coeficiente explícito positivo; pendiente de revisión independiente |
| Fidelidad en norma a escala de la señal total | Criterio rechazado si se acepta la derivación (6) |
| Compresión = protocolo condicionado | Falso; identidad exacta (7) y corrección (8) |
| Asintótica de `Lpp` o de `abs(Lpp)` | OPEN |
| Predominio `L-Lpp=o(abs(L))` | OPEN; los dos diagnósticos finitos no lo deciden |
| Teorema plano del observable total | Conserva su alcance y estado previo |
| H1c y extensión E/AdS | Sin modificación |

El próximo cálculo pertinente a C es el elemento de matriz PP con el
corte móvil real, incluyendo sus términos lineal y cuadrático y el borde
`|p|=N^{-1/2}`. La norma ya no basta. Hay que distinguir una contribución
del borde del filtro de la saddle compleja del observable total. Esta nota
no asigna `K_IR`, una potencia, ni un coeficiente a ese elemento de matriz.

La hoja bibliográfica también exige dos precisiones: conservar el rango del
shift garantiza la **cota** de soporte, pero la igualdad del soporte estricto
requiere canales extremos no nulos; y el antecedente de la potencia 3/2
cerca del frente está ya en
[CJWW, resumen y sección 4.3](https://arxiv.org/html/2408.02108v1).
No se certifica aquí novedad bibliográfica, ni estabilidad inhomogénea.

## 7. Verificación reproducible

Ejecutar desde la raíz:

```sh
python3 -B scripts/verify_ir_projection_leakage.py
```

El certificado comprueba álgebra de rango dos, normalización, coeficientes
de borde para los cuatro encoders, constante radial y núcleo del corte.
Los argumentos analíticos de las secciones 3.1–3.2 y 4 son pruebas escritas,
no pruebas formalizadas ni resultados de un ajuste. No se reutilizan
cancelaciones de coma flotante para demostrar (4).

Ejecución local: **27/27 comprobaciones algebraicas exactas PASS**, Python
3.12.3 y SymPy 1.14.0. El control del transformado radial detectó inicialmente
coeficientes subdominantes mal transcritos en el valor esperado del test;
se corrigieron a partir de la integral exacta. El coeficiente líder, D y
las potencias de esta nota no cambiaron. Este PASS no sustituye la revisión
independiente pendiente de la derivación analítica.
