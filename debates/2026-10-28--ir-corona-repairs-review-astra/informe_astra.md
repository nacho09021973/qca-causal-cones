<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 0c150e808db4471d10c743a325433605980d8c82; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 f363e072101d7766d1075b6f4a24e3fc84dc92e541016af9ccd448a5e2108db4; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.165.0)
inicio: 2026-10-28T15:28:19Z  fin: 2026-10-28T15:35:40Z
documento: /home/ignac/qca-causal-cones/papers/ir-corona/ir-corona.tex ; último commit observado: cd8ff54 ; sha256 de la copia enviada 90fb2c8ec712463c553770ebf676dd9277dd0ea823b0528b87143c1077375f00
documento: /home/ignac/qca-causal-cones/debates/2026-10-28--ir-corona-repairs-review-astra/reparaciones.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 730794567607b268bb601176bdbf5201b980b55fb72e6669a96780cdba7f438c
entrada_astra.txt sha256 95f839e5b8e68a6bef8358321d83d70fab770ab3708dbb6e144f6880eb530cc5
respuesta sha256 cd2787aec6fd7ab33c492002f6dfbab0e50a077d0677184eb6dbd96ab1b60298
-->

**Veredicto global: CERRADA_CON_ARREGLOS.** Las nuevas estimaciones conservan las potencias \(N^{-7}\) y \(N^{-8}\). Quedan dos arreglos locales: justificar uniformemente el recuento de sitios y escribir las fases que faltan en las expansiones individuales cerca de \(\pi u\). Este último defecto ya estaba en el texto anterior; la reparación no lo introduce, pero tampoco lo resuelve.

| Reparación | Veredicto |
|---|---|
| Fila residual de Bob y propagación en «Assembly» | **CERRADA_CON_ARREGLOS** |
| Frecuencias desplazadas y estimación de «Layers»(d) | **CERRADA** |
| Leyenda de la Tabla 1 | **CERRADA** |

La revisión se limita a los dos documentos suministrados. Los certificados informáticos y sus resultados externos quedan **NO VERIFICADOS**.

**1. Reparación de «Layers»(b) y segundo reemplazo de «Assembly».**

La sustitución del error escalar por una fila residual es correcta y necesaria. Rehago la estimación.

Por las definiciones,
\[
y_*=Nu-\frac N4\hat u=Nw_*.
\]
Además, \(y/N\) pertenece al compacto \(\overline B(u,1/4)\). La representación integral del lema «Free tail» muestra que \(R_0\) es suave y tiene derivadas acotadas en ese compacto; no hace falta suponer regularidad adicional.

En un plano de profundidad \(\delta'\),
\[
y-y_*=\delta'\hat u+u'_\perp,\qquad
|u'_\perp|^2\le 2R\delta'-\delta'^2.
\]
Por tanto, incluso se dispone de la cota más precisa
\[
|y/N-w_*|^2\le \frac{2R\delta'}{N^2}
=\frac{\delta'}{2N}.
\]
El lema del recurso libre da entonces
\[
\begin{aligned}
\|r(y)-N^{-3/2}R_0(w_*)\|
&\le CN^{-3/2}|y/N-w_*|+CN^{-5/2}\\
&\le CN^{-2}\sqrt{\delta'}+CN^{-5/2}\\
&\le CN^{-2}(1+\delta').
\end{aligned}
\]
La cota propuesta para \(\rho\) es válida, uniformemente en todos los planos que intersectan \(\mathcal B_N\).

El punto que necesita explicitarse es el recuento. Para un disco en una traslación de una red bidimensional, la estimación general es
\[
\#\{\text{sitios del plano en el disco}\}\le C(1+N\delta'),
\]
no directamente \(CN\delta'\) cuando la profundidad puede acercarse a cero.

Con esta estimación general, el argumento funciona sin ninguna pérdida:
\[
\begin{aligned}
\sum_{y\text{ en el plano}}h_N(y)\|\rho(y)\|
&\le C(1+N\delta')\frac{\delta'^2}{N^2}
                 N^{-2}(1+\delta')\\
&\le CN^{-3}(1+\delta')^4.
\end{aligned}
\]
Y, poniendo \(a=\sqrt3t_*>0\),
\[
\sup_{0\le\theta<1}
\sum_{j\ge0}e^{-t_*(\theta+j)}
\left(1+\frac{\theta+j}{\sqrt3}\right)^4<\infty.
\]
Así, la fila residual sin normalizar tiene norma \(O(N^{-3})\), uniformemente en \(\theta\) y en todas las frecuencias reales: sólo se han usado módulos de fases.

Hay una comprobación adicional favorable al manuscrito: para la secuencia efectiva \(\theta_N\), el recuento escrito \(O(N\delta')\) también puede justificarse. Si \(k=\lfloor\sqrt3N/4\rfloor\),
\[
\theta_N
=\frac{3N^2-16k^2}{16(\sqrt3N/4+k)}
\ge\frac1{8\sqrt3N},
\]
pues el numerador es un entero positivo. En consecuencia,
\[
N\delta'\ge N\theta_N/\sqrt3\ge1/24.
\]
Esto permite absorber el \(1\), pero el manuscrito no da este argumento. Usar \(1+N\delta'\) evita introducirlo.

Sea \(B_\rho(\eta)\) la **fila**, con sus fases, obtenida al sumar \(\rho(y)^\dagger M_Bh_N(y)\). La definición correcta es
\[
\mathbf E_B
=\mathcal E\,R_0(w_*)^\dagger M_B
+\frac{B_\rho(\eta)}{N^{-5/2}(32/\sqrt3)}.
\]
Como \(\|M_B\|\le1\),
\[
\|\mathbf E_B\|
\le C(N^{-1/2}+|\eta_n|).
\]
No se impone ninguna dirección artificial al error. Los factores \(32/\sqrt3\) y \(N^{-5/2}\) son correctos.

**La salvedad cerca de \(\pi u\) es algebraica.** Con las definiciones exactas de \(\mathfrak A,\mathfrak B\), «the same holds with \(\mathcal S_-\)» no es literalmente cierto para cada capa por separado. En efecto,
\[
u\cdot(x-x_*)=-(\theta_N+j),\qquad
u\cdot(y-y_*)=\theta_N+j',
\]
de donde
\[
e^{i\pi u\cdot(x-x_*)}=e^{-i\pi\theta_N}(-1)^j,
\qquad
e^{-i\pi u\cdot(y-y_*)}=e^{-i\pi\theta_N}(-1)^{j'}.
\]
Las dos expansiones deben llevar el factor global \(e^{-i\pi\theta_N}\):
\[
\mathfrak A_f(\pi u+\eta)
=e^{-i\pi\theta_N}N^{-5/2}\frac{16\pi}{\sqrt3}
\varphi_\partial[\mathcal S_-+\mathcal E_{A,-}]\chi,
\]
\[
\mathfrak B_w(\pi u+\eta)
=e^{-i\pi\theta_N}N^{-5/2}\frac{32}{\sqrt3}
[R_0(w_*)^\dagger M_B\mathcal S_-+\mathbf E_{B,-}].
\]
Los errores satisfacen las mismas cotas. Esas fases tienen módulo uno, pero **no pueden omitirse dentro de una identidad con error pequeño**.

La fórmula final de «Assembly» se conserva, porque las fases se cancelan exactamente:
\[
e^{-2\pi i\theta_N}(-1)^N
e^{-iN\pi u\cdot v_*}
=e^{-2\pi i\theta_N}
e^{2\pi i(\sqrt3N/4)}
=1.
\]
La identidad de paridad citada en el manuscrito expresa esta cancelación en el producto completo; no elimina las fases de cada factor individual.

La nueva desigualdad en norma de «Assembly» es correcta:
\[
|BTA-B_0TA_0|
\le\|B-B_0\|\|T\||A|
+\|B_0\|\|T\||A-A_0|.
\]
Incluye también el producto de errores, porque el primer término conserva \(A\) completo. Usando las capas corregidas y la cota gaussiana local,
\[
N^{-5}\int
(N^{-1/2}+|\eta_n|)e^{-cN|\eta|^2}\,d^3\eta
=O(N^{-7}).
\]
En efecto, ambos términos de la integral son \(O(N^{-2})\). No se pierde ninguna potencia.

Como cuestión de exposición, esa desigualdad utiliza el símbolo original, aunque el párrafo dice haberlo reemplazado antes. Basta efectuar primero el reemplazo de capas y después el del símbolo, o escribir la desigualdad con el símbolo gaussiano. No es un defecto matemático de la estimación.

**2. Reparación de «Layers»(d).**

La reducción a frecuencias tangenciales desplazadas es correcta. En un plano afín, las traslaciones por \(\Lambda_0\) sólo ven
\[
\eta_{0,t}+\eta_t.
\]
Las fases procedentes de elegir un origen en el plano tienen módulo uno y no afectan a las cotas.

Con la convención
\[
\Lambda_0^*=\{m\in\hat u^\perp:m\cdot z\in\mathbb Z
\text{ para todo }z\in\Lambda_0\},
\]
la trivialidad del carácter equivale exactamente a
\[
\eta_{0,t}\in2\pi\Lambda_0^*.
\]
Por «symbol»(c), esto falla en los seis puntos considerados. Cada distancia a la red cerrada es positiva y el conjunto de puntos es finito; por tanto \(d_0>0\).

Reducir \(r_0\) a \(r_0\le d_0/2\) es compatible con «symbol»(d). También lo es con (e), **permitiendo que cambie su constante de separación espectral**: el nuevo complemento sigue siendo compacto y no contiene puntos de \(\Sigma\). No se necesita conservar el valor anterior de \(c\).

Para todas las frecuencias de Poisson,
\[
|2\pi m-\eta_{0,t}-\eta_t|\ge d_0/2.
\]
La suma de sus inversos cúbicos converge uniformemente: un número finito de términos queda controlado por \(d_0/2\), y para \(|m|\) grande los denominadores son comparables a \(|m|\). En dimensión dos,
\[
\sum_{m\ne0}|m|^{-3}<\infty.
\]
El término \(m=0\) está correctamente incluido.

La estimación de las derivadas también es correcta, con una precisión de interpretación: las cotas ordinarias de \(S',S'',S'''\) corresponden a \(e>0\); la parte singular de la tercera derivada se contabiliza separadamente en el borde.

Para \(e>0\),
\[
\begin{aligned}
S'(e)&=2\kappa e\cos(\kappa e^2),\\
S''(e)&=2\kappa\cos(\kappa e^2)
       -4\kappa^2e^2\sin(\kappa e^2),\\
S'''(e)&=-12\kappa^2e\sin(\kappa e^2)
         -8\kappa^3e^3\cos(\kappa e^2).
\end{aligned}
\]
Como \(e\le\delta\le R/2=N/8\),
\[
\kappa e^2\le\pi/2.
\]
Esto justifica uniformemente
\[
|S'|\le C\kappa e,\quad
|S''|\le C\kappa,\quad
|S'''|\le C\kappa^2e.
\]

En el borde, \(S(0)=S'(0)=0\) y \(S''(0+)=2\kappa\). Por tanto, la segunda derivada de \(s_N\) tiene salto tensorial
\[
2\kappa\,\nabla\varepsilon_\perp
\otimes\nabla\varepsilon_\perp.
\]
Su contribución a la variación total de la tercera derivada queda acotada por
\[
C\kappa\frac{\delta}{R}\sqrt{R\delta}
=C\kappa\delta^{3/2}R^{-1/2}.
\]

En el interior, la regla de la cadena sólo produce
\[
S'''(\varepsilon_\perp)(D\varepsilon_\perp)^3,
\qquad
3S''(\varepsilon_\perp)
D\varepsilon_\perp D^2\varepsilon_\perp,
\]
pues \(D^3\varepsilon_\perp=0\). Sus cotas puntuales son, respectivamente,
\[
C\kappa^2\delta^{5/2}R^{-3/2},
\qquad
C\kappa\delta^{1/2}R^{-3/2}.
\]
Multiplicando por el área \(O(R\delta)\), y añadiendo el borde,
\[
\|D^3s_N\|_{\mathcal M}
\le C\left(
\kappa\delta^{3/2}R^{-1/2}
+\kappa^2\delta^{7/2}R^{-1/2}
\right).
\]
El cociente del segundo término respecto al primero es \(\kappa\delta^2=O(1)\). Así,
\[
\|D^3s_N\|_{\mathcal M}
\le CN^{-5/2}\delta^{3/2}.
\]
La versión con \((1+\delta)^{3/2}\) del diff es válida.

Para comprobar todas las potencias de Leibniz, las cuatro contribuciones a \(D^3(s_N\varphi_N)\) son:

| Derivadas sobre \(s_N\) | Cota de la contribución |
|---|---|
| 3 | \(CN^{-4}\delta^{3/2}\) |
| 2 | \(CN^{-9/2}\delta^2\) |
| 1 | \(CN^{-5}\delta^{5/2}\) |
| 0 | \(CN^{-11/2}\delta^3\) |

Aquí se usan exactamente las cotas \(L^1\) del diff y
\(\|D^b\varphi_N\|_\infty\le CN^{-3/2-b}\). Todas quedan acotadas por
\[
CN^{-4}(1+\delta)^3.
\]
El argumento vale para derivadas direccionales unitarias, uniformemente en la dirección de la frecuencia; por ello sirve para la integración por partes de Poisson.

La suma ponderada en profundidad converge uniformemente en \(\theta\). Para \(\delta>R/2\), los pesos proporcionan \(e^{-cN}\); el número de sitios y las amplitudes sólo añaden factores polinómicos, absorbibles reduciendo \(c\). Se obtiene, por tanto,
\[
|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}
\]
con los cuantificadores declarados.

Finalmente, las simetrías de «symbol»(b) transportan la cota gaussiana a esos seis puntos. Su contribución es
\[
N^{-4}N^{-5/2}\int e^{-cN|\eta|^2}\,d^3\eta
=O(N^{-8}).
\]
Esta reparación queda cerrada sin cambios matemáticos obligatorios.

**3. Leyenda de la Tabla 1.**

Las afirmaciones sobre los promedios de \(\Gamma_\pm\) son correctas. No basta, sin embargo, con invocar informalmente que son cuadrados: se puede calcular el promedio exactamente.

Sea
\[
a_\omega(\tau)=\hat g_\tau(\omega).
\]
Como \(a_{-\omega}=\overline{a_\omega}\), la ortogonalidad de las series de Fourier da
\[
\langle\Gamma_+\rangle
=\overline\Gamma+
\sum_{n\ne0}\int_{\mathbb R^2}
e^{-q_t|\tau|^2}|a_{2\pi n}(\tau)|^2\,d^2\tau
>\overline\Gamma,
\]
y
\[
\langle\Gamma_-\rangle
=\sum_{n\in\mathbb Z}\int_{\mathbb R^2}
e^{-q_t|\tau|^2}|a_{\pi(2n+1)}(\tau)|^2\,d^2\tau
>0.
\]
La convergencia absoluta y las cotas gaussianas del lema permiten intercambiar sumas e integrales. Para \(\mathcal S_-\), las frecuencias son impares; al elevar al cuadrado, la integración en \([0,1]\) selecciona precisamente las parejas opuestas.

Hay una sutileza lógica: esas dos desigualdades, por sí solas, no excluyen que sus contribuciones a un \(C\) concreto se cancelen cuando \(\ell_0\ell_\pi<0\). También comprobé ese punto.

Definiendo
\[
W(\omega)=
\frac{\pi c_g^2}
{(t_*^2+\omega^2)^3
 \left[q_t(t_*^2+\omega^2)+t_*/(2\sqrt3)\right]},
\]
se tiene
\[
a:=\langle\Gamma_+\rangle-\overline\Gamma
=2\sum_{n\ge1}W(2\pi n),\qquad
b:=\langle\Gamma_-\rangle
=2\sum_{n\ge0}W(\pi(2n+1)).
\]
Como \(t_*<1\),
\[
W(2\pi n)\le\frac{W(\pi)}{27n^6},
\qquad
\frac ba\ge\frac{27}{\zeta(6)}>13.5.
\]
Por otro lado, las fórmulas del apéndice dan
\[
|\ell_0/\ell_\pi|<3
\]
en todas las filas con signos opuestos. Para comprobar esta desigualdad basta usar las cotas amplias
\[
0.71<\alpha<0.72,\quad 1.28<c_*<1.29,\quad
0.70<\mathcal I_0<0.73,\quad 0.12<\mathcal I_1<0.14.
\]
Las dos últimas se obtienen directamente acotando los integrandos con los polinomios alternantes de seno, coseno y las funciones esféricas; no requieren los certificados externos.

Por tanto, tampoco hay cancelación accidental:
\[
\langle C\rangle-\overline C
=\mathcal Kc_r(a\ell_0+b\ell_\pi)\ne0
\]
para las dieciséis filas. La nueva leyenda es correcta incluso en su lectura individual por pareja.

No queda en el documento suministrado otra identificación explícita de \(\overline C\) con el promedio de \(C\). Las restantes apariciones lo usan como coeficiente de referencia y denominador de la desviación relativa. La notación con barra puede sugerir un promedio, pero la definición y la nueva leyenda eliminan esa ambigüedad.

**Arreglos obligatorios, localizados.**

1. **«Layers»(b), párrafo nuevo del recuento de sitios** —hunk que comienza en `+1161`—. **Laguna de justificación de uniformidad.** Cambiar \(O(N\delta')\) por \(O(1+N\delta')\) y conservar la estimación demostrada arriba, o añadir la cota aritmética \(N\delta'\ge1/24\) para la secuencia efectiva. La primera opción es más directa y mantiene la uniformidad sin argumentos adicionales.

2. **«Layers»(c) y tratamiento de \(\pi u\) en «Assembly».** **Error matemático del enunciado literal, heredado del texto anterior.** Incluir \(e^{-i\pi\theta_N}\) en ambas expansiones individuales, o definir explícitamente capas renormalizadas por esa fase. Mostrar después su cancelación con \((-1)^N e^{-iN\pi u\cdot v_*}\). Las cotas de los residuos, \(\Gamma_-\), el coeficiente final y el \(O(N^{-7})\) permanecen iguales.

No encuentro un error nuevo de constantes o potencias introducido por el diff. La certificación numérica de las tablas, los scripts, Lean y las referencias externas permanece **NO VERIFICADA** en esta sesión sellada.