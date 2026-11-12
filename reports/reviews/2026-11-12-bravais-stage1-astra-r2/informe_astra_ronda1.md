**Dictamen global: REPAIR_REQUIRED.**

No encuentro un obstáculo matemático específico de Bravais que invalide la adaptación. He rederivado los reemplazos geométricos, las normalizaciones y la transferencia de los argumentos analíticos indicados abajo. Sin embargo, **el inventario U1–U14 no es literalmente completo**, y U6 necesita precisar qué zona fundamental utiliza. El resultado (b) es defendible después de esas reparaciones, tomando B1 y la parte demostrada de B2 como base, conforme al encargo.

No identifico una hipótesis nueva necesaria para efectuar esos reemplazos. Tampoco identifico un contraejemplo a la adaptación. La celda abierta de B2 debe permanecer abierta.

**Objeciones al documento 2, «Etapa 1».**

1. **Falta un uso algebraico de la estructura de red. Reparación necesaria.**

   Referencias: documento 2, §§1–2 y §7; documento 8, «Stage 1 — upper bound», párrafo anterior al lema 1.1.

   S01 utiliza que el determinante de un símbolo unitario Laurent-polinómico es un monomio:
   \[
   \det S(p)=c\,e^{ip\cdot d_0}.
   \]
   Lo utiliza para asegurar que el radio espectral nunca se anula después del desplazamiento complejo y que \(\Phi\) es finita. Este uso de las coordenadas enteras y del álgebra de caracteres **no figura expresamente en U1–U14**. U1 enumera el toro y su medida, no esta propiedad algebraica.

   El paso se traslada, sin hipótesis adicional. Escribiendo \(a=Bn\), \(p=B^{-T}t\),
   \[
   S(B^{-T}t)=\sum_n S_{Bn}e^{it\cdot n}.
   \]
   Es un símbolo Laurent-polinómico en \(e^{it_j}\). Si \(P\) es su determinante, la unitariedad implica
   \[
   P(z)P^\sharp(z)=1
   \]
   como identidad de polinomios de Laurent; por tanto \(P\) es una unidad de ese anillo, es decir, un monomio. En las coordenadas originales:
   \[
   \det S(p)=c\,e^{ip\cdot a_0},\qquad a_0\in L,\quad |c|=1.
   \]

   Hay una segunda comprobación que evita incluso necesitar la clasificación de unidades. Defínase
   \[
   S^\sharp(p)=\sum_{a\in F}S_a^\dagger e^{-ip\cdot a}.
   \]
   La identidad \(SS^\sharp=I\) en el toro real, por unicidad de los coeficientes de Fourier, es una identidad de sumas exponenciales y vale también para \(p\) complejo. Así \(S(p)\) es invertible en todo el dominio complejo.

   **Obligación:** añadir este uso al inventario —o ampliar explícitamente U1— y recogerlo en §2. La afirmación actual «cada uso es uno de U1–U14» no está justificada tal como está escrita.

2. **U6 confunde una condición intrínseca de inyectividad con la inclusión en una zona fundamental no especificada. Cuestión de exposición que debe repararse.**

   Referencias: documento 2, §1, U6, y §3, «free tail».

   Para la celda de Voronoi de \(2\pi L^*\), centrada en cero, el inradio es
   \[
   r_{\mathrm{inj}}=\pi\lambda_1(L^*).
   \]
   Por ello
   \[
   \frac1N<\pi\lambda_1(L^*)
   \]
   garantiza que la bola cerrada de soporte queda estrictamente dentro de esa celda y constituye una sola carta del toro.

   **No es el criterio de inclusión en cualquier zona fundamental.** Incluso para \(L=\mathbb Z^2\), el paralelogramo fundamental centrado generado por
   \[
   2\pi(1,0),\qquad 2\pi(M,1)
   \]
   tiene inradio \(\pi/\sqrt{1+M^2}\), aunque \(\lambda_1(L^*)=1\). Con \(M=10\), \(N=1\) satisface el umbral de U6, pero la bola de radio uno no cabe en ese paralelogramo.

   **Obligación:** especificar «celda de Voronoi centrada en cero» o formular U6 como una condición de inyectividad de la bola en el toro. Conviene sustituir el «iff» por la formulación precisa de inclusión estricta; en el caso de igualdad hay además que distinguir soporte cerrado y región donde \(g\) es no nula.

   Si se explicita también la banda de salida de la definición de admisibilidad, de radio \(N^{-1/2}\), el umbral correspondiente es
   \[
   N>\bigl(\pi\lambda_1(L^*)\bigr)^{-2}.
   \]
   Esto tampoco exige una hipótesis nueva: para cada red fija solo elimina finitos \(N\). No constituye una demostración de admisibilidad.

3. **La primera observación de §6 necesita el calificativo «en general». Cuestión de exposición.**

   Referencia: documento 2, §6.1.

   Un cambio lineal general convierte las bolas en elipsoides y puede convertir el cono isotrópico en anisotrópico. Pero no ocurre para toda red de Bravais ni para toda matriz \(B\). Si
   \[
   L=aQ\mathbb Z^d,\qquad Q^TQ=I,
   \]
   el cambio es una similitud: las bolas siguen siendo bolas y el nodo sigue siendo isotrópico, con la velocidad reescalada.

   La conclusión pertinente es correcta: **la extensión a todas las redes de Bravais no se deduce mediante un cambio de coordenadas que preserve la clase de B1**. La afirmación categórica sobre lo que sucede con cualquier \(B\) es demasiado fuerte.

4. **El alcance literal de «cada uso» debe separar la prueba general de las comprobaciones del ejemplo. Cuestión de exposición.**

   Referencias: documento 2, preámbulo, §§1 y 7; documento 10, §8; documento 8, comprobación de K3 al final de la etapa 1.

   LT §8 utiliza propiedades particulares del paseo original: hermiticidad de \(S(-i\xi_*)\), relación entre proyectores en cero y \(\pi u\), y fórmulas explícitas de sus autovectores. No son reemplazos universales de geometría de redes.

   Esto **no perjudica la prueba general**, porque allí esas propiedades se sustituyen por las hipótesis H6 y H10. Pero la frase «cada uso en los textos recorridos» es más amplia que lo efectivamente inventariado.

   **Obligación:** delimitar el inventario a los usos de la red en las demostraciones generales, identificando aparte las verificaciones específicas de K3. No he encontrado que la adaptación use subrepticiamente una simetría cúbica para demostrar el resultado general.

**Lo que sí he rederivado.**

1. **Geometría de §0, incluidos los dos ejemplos.**

   Para \(u=B^{-T}n\ne0\),
   \[
   u\cdot L=n\cdot\mathbb Z^d
   =\gcd(n_1,\ldots,n_d)\mathbb Z.
   \]
   Por tanto, primitividad equivale exactamente a \(u\cdot L=\mathbb Z\).

   Elíjase \(b\in L\) con \(u\cdot b=1\). Entonces
   \[
   L=\Lambda_0\oplus\mathbb Zb,\qquad
   L\cap\{u\cdot x=k\}=kb+\Lambda_0.
   \]
   La altura de \(b\) respecto a \(u^\perp\) es \(1/|u|\). Calculando el volumen del paralelepípedo con una base de \(\Lambda_0\) y \(b\):
   \[
   \operatorname{covol}(L)
   =\frac{\operatorname{covol}(\Lambda_0)}{|u|}.
   \]
   No hace falta que \(b\) sea perpendicular al plano.

   Todo carácter trivial en \(\Lambda_0\) está determinado por su valor \(\omega\) en \(b\), de donde
   \[
   \chi(x)=\omega^{u\cdot x}.
   \]
   Además,
   \[
   e^{i\eta\cdot \ell}=1\quad(\ell\in\Lambda_0)
   \iff \eta_t\in2\pi\Lambda_0^*.
   \]

   Los ejemplos son correctos:

   - Triangular: \(u=(1,-1/\sqrt3)\), \(\Lambda_0=\mathbb Zb_2\), covolumen uno y separación \(\sqrt3/2\).
   - BCC de igual paridad: índice cuatro en \(\mathbb Z^3\); los productos \(3\) y \(2\) garantizan primitividad de \(u=(1,1,1)\). En el plano de suma cero no hay puntos de coordenadas todas impares, por lo que
     \[
     \Lambda_0=2(\mathbb Z^3\cap u^\perp),
     \qquad \operatorname{covol}(\Lambda_0)=4\sqrt3.
     \]

   U9 debe entenderse como existencia de puntos en cada **plano afín completo**. No garantiza que cada sección de ese plano con la bola contenga sitios, ni necesita hacerlo: las sumas admiten secciones vacías.

2. **Fourier, convexidad, contorno y Schur de §§0 y 2.**

   Con \(p=B^{-T}t\),
   \[
   \frac{\operatorname{covol}(L)\,dp}{(2\pi)^d}
   =\frac{dt}{(2\pi)^d}.
   \]
   Esto verifica la medida normalizada, la inversión y Parseval.

   Toda traslación real del toro preserva esa medida. En consecuencia, la conjugación del operador multiplicación utilizada en S01, lema 1.1, y la igualdad
   \[
   \|F(a+ib)\|=\|F(a)\|
   \]
   se mantienen.

   Para desplazar el contorno se puede trabajar en \(t\), donde la periodicidad es coordenada a coordenada. El desplazamiento requerido es
   \[
   t\longmapsto t-iB^T\xi.
   \]
   El integrando completo es periódico porque \(y-x\in L\); los términos de las caras opuestas se cancelan. El factor exterior es \(e^{-\xi\cdot(y-x)}\), con el signo indicado en el informe.

   Finalmente, si \(V_L\) es una celda de Voronoi, las celdas asociadas a los sitios de \(NA\) tienen interiores disjuntos y están contenidas en \(NA+V_L\). Así,
   \[
   |NA\cap L|\operatorname{covol}(L)
   \le \operatorname{vol}(NA+V_L)=O_L(N^d).
   \]
   El test de Schur conserva el exponente \(d+s-1\). La dependencia adicional de la constante de conteo es geométrica; las constantes espectrales siguen dependiendo del paseo, como en B1.

3. **U6 y la forma limsup.**

   La menor longitud de un período no nulo es \(2\pi\lambda_1(L^*)\). Dos puntos de una bola de radio \(r<\pi\lambda_1(L^*)\) no pueden diferir en un período no nulo. Esta es una comprobación independiente del cálculo mediante la celda de Voronoi.

   Para \(L\) fijo, los umbrales anteriores son finitos. Eliminar finitos términos no cambia
   \[
   \limsup_{N\to\infty}N^{-1}\log\delta(N).
   \]
   Esto no proporciona uniformidad cuando \(L\) varía o degenera; el informe tampoco necesita esa uniformidad.

4. **Cola libre, Poisson en clases y ensamblaje de §3.**

   El factor que aparece después de \(p=q/N\) es
   \[
   Z_N(L)^{-1/2}\,
   \frac{\operatorname{covol}(L)}{(2\pi)^d}N^{-d}
   =N^{-d/2}c_r(L).
   \]
   La estimación uniforme en \(y\) del resto usa que
   \(|e^{-iq\cdot y/N}|=1\); no depende de coordenadas enteras. Los argumentos locales sobre el símbolo son los de B1, aceptados aquí como base.

   Para una clase \(t+\Lambda_0\), Poisson tiene la forma
   \[
   \sum_{\ell\in\Lambda_0}F(t+\ell)
   =\frac1{\operatorname{covol}(\Lambda_0)}
     \sum_{\nu\in\Lambda_0^*}
       e^{2\pi i\nu\cdot t}\widehat F(2\pi\nu),
   \]
   con la convención \(\widehat F(k)=\int e^{-ik\cdot x}F(x)\,dx\).
   El modo cero es independiente del desplazamiento de la clase y lleva exactamente
   \[
   \frac1{\operatorname{covol}(L)|u|}.
   \]
   Los desplazamientos de las clases, que pueden depender de \(N\) y de la profundidad, solo introducen fases de módulo uno en los otros modos.

   Las cotas de terceras derivadas de B1 son euclídeas. La única suma discreta adicional es del tipo
   \[
   \sum_{\nu\ne0}|\nu|^{-3},
   \]
   convergente en rango \(m=1,2\). Por anillos diádicos, su cola queda acotada por una serie \(\sum_j2^{j(m-3)}\).

   Para un carácter no trivial,
   \[
   d_0=\operatorname{dist}(\eta_{k,t},2\pi\Lambda_0^*)>0.
   \]
   Reduciendo \(r_0<d_0/2\), todos los términos —incluido el índice cero— quedan separados de frecuencia cero. La cota uniforme sobre la suma desplazada se obtiene separando finitos índices de la cola anterior. Para el carácter trivial, \(r_0\le\pi\lambda_1(\Lambda_0^*)\) basta para controlar los modos no nulos.

   También debe escogerse \(r_0\) dentro de las cartas locales del toro y separando los puntos dominantes. Esto es una elección de constante, no una hipótesis.

   El conteo de sitios de cada disco sigue siendo
   \[
   O_L\!\left((N\delta)^{m/2}+1\right).
   \]
   Con los factores de recurso y perfil produce \(N^{-5/2}\) por lado. El ensamblaje añade \(N^{-d/2}\) y la medida \(d\mu_L\), conservando \(N^{-5-d/2}\).

5. **Todas las constantes explícitas de §4.**

   Escribiendo \(v_L=\operatorname{covol}(L)\), obtengo
   \[
   Z_N(L)=v_LN^{-d}(2\pi)^{-d}\|g\|_2^2,
   \qquad
   c_r(L)=\frac{\sqrt{v_L}}{(2\pi)^{d/2}\|g\|_2}.
   \]
   La sustitución tangencial y el modo cero de Poisson dan
   \[
   k_A(L)=\frac{2\pi(2\rho_A)^{m/2}}
                  {\rho_A^2v_L|u|},
   \qquad
   k_B(L)=\frac{4(2\rho_B)^{m/2}}
                  {\rho_B^2v_L|u|}.
   \]
   La integración gaussiana normal aporta
   \(\sqrt{2\pi/C_{nn}}\), con la rama de B1, y la medida aporta
   \(v_L(2\pi)^{-d}\). Por tanto el \(c(L)\) escrito en el informe tiene la normalización correcta.

   La cancelación explícita de covolúmenes es
   \[
   v_L^{1/2}v_L^{1/2}v_L^{-1}v_L^{-1}v_L=1.
   \]
   Esto no significa que el coeficiente sea independiente de la red: permanecen \(|u|\), los parámetros del paseo y los factores de profundidad.

   La comprobación contra \(\mathbb Z^3\) también coincide:
   \[
   \begin{aligned}
   \|g\|_2^2
   &=4\pi\left(\frac13-\frac45+\frac67-\frac49+\frac1{11}\right)
     =\frac{512\pi}{3465},\\
   c_r&=\frac{\sqrt{3465}}{64\pi^2},\qquad
   Z_N=\frac{64}{3465\pi^2N^3},\\
   k_A&=\frac{16\pi}{\sqrt3},\qquad
   k_B=\frac{32}{\sqrt3}
   \quad(\rho_A=\rho_B=1/4).
   \end{aligned}
   \]
   Son comprobaciones algebraicas contra las fórmulas adjuntas; no dependen de certificados externos.

6. **Fases, profundidad compleja y promedios de §5.**

   Los factores globales de CA §2 satisfacen
   \[
   \alpha_A\alpha_B
   =e^{-i\phi N u\cdot v_*}e^{iN\eta_k\cdot v_*}.
   \]
   Multiplicando por el factor del kernel se cancela la segunda exponencial. Queda exactamente
   \[
   \psi_k=\phi_k+\omega_0-\phi\,u\cdot v_*.
   \]
   El cálculo solo utiliza las identidades de caracteres sobre sitios de \(L\); no requiere que \(x_*\) o \(y_*\) sean sitios.

   La transformada de profundidad resulta de integrar primero en \(\delta\) y después en las coordenadas tangenciales:
   \[
   \widehat g_\tau(\omega;\sigma)
   =2\pi^{m/2}|u|\,
     \bigl(|u|(\sigma+i\omega)\bigr)^{-3-m/2}
     e^{-|\tau|^2/[4|u|(\sigma+i\omega)]}.
   \]
   Como \(\Re\sigma=\kappa>0\), las integrales convergen. La serie de Fourier converge absolutamente; la periodicidad continua en el desplazamiento se conserva porque el sumando de profundidad cero se anula.

   Las condiciones aritméticas siguen concerniendo a los números reales
   \(u\cdot w_A\), \(u\cdot w_B\) y las diferencias de fases. Su interpretación no depende de que \(u\) tenga coordenadas enteras en la base euclídea.

   En particular:

   - H6\(_k\)(i) conserva los dos casos demostrados de H9.
   - H6\(_k\)(ii) con H9(ii) conserva la anulación de los términos cruzados por equidistribución.
   - H6\(_k\)(ii) con H9(i) sigue abierta: trasladar la red no proporciona la independencia respecto del segundo desplazamiento que falta en B2.

   No he encontrado un factor de covolumen o una fase adicional omitidos en esta transferencia.

7. **Las observaciones restantes de §6.**

   La periodicidad adicional debida a \(L'\subsetneq L\) es correcta:
   \[
   S(p+2\pi h)=S(p),\qquad h\in L'^*.
   \]
   Una copia distinta en \(T_L\), cuya diferencia de carácter sea trivial sobre \(\Lambda_0\), reproduce los autovectores del punto seleccionado. Por ello impide su aislamiento mediante H6 o H6\(_k\)(i). Conviene explicitar «copia distinta» y la referencia al punto seleccionado.

   Pasar a \(L'\) cambia el toro, el normal primitivo y las condiciones aritméticas. Las condiciones verificadas en una elección de red no se heredan automáticamente en otra.

   La observación sobre admisibilidad también describe correctamente los textos adjuntos: S01, SP y LT no contienen una demostración general de los cocientes exigidos por la definición 3.1 del manuscrito. Probar que los denominadores no son cero no prueba que los cocientes tiendan a cero.

**Cuestiones de B1/B2 anotadas aparte; no deciden este dictamen.**

- **Admisibilidad general: NO_VERIFICADO.** Es la carencia reconocida por el documento 2, §6.3. La prueba del manuscrito usa diferencias en direcciones de una base de \(\mathbb Z^3\), desigualdades para sus multiplicadores y cotas inferiores de masa. Si se pretende completar esa parte sobre \(L\), habrá que tratar esos usos de la red. Quedan fuera del inventario de las etapas demostradas que se adapta aquí. La expresión «no involucra la red» solo es aceptable para decir que la carencia ya existía, no para afirmar que su eventual solución carecerá de ingredientes de red.

- **Lectura literal de H2: NO_VERIFICADO.** Documento 3, H2; documento 9, §3.1; documento 10, §5. La no degeneración de la Hessiana *compleja* de \(\log\lambda\) no implica por sí sola positividad definida de su parte real. Por ejemplo, el germen
  \[
  f(t)=f(0)+ivt-it^2-t^4
  \]
  tiene máximo estricto de su parte real en cero y \(f''(0)=-2i\ne0\), pero no tiene decaimiento gaussiano real cuadrático. Esto señala una insuficiencia de la inferencia escrita bajo esa lectura de H2; no es un contraejemplo construido dentro de la clase de paseos. Conforme al encargo, acepto el argumento gaussiano de B1 como base y no uso esta cuestión para rechazar su transferencia.

**Obligaciones para cerrar esta revisión.**

- Completar el inventario con el paso algebraico del determinante o su sustituto mediante \(S^\sharp\).
- Precisar U6 mediante una celda de Voronoi o el radio de inyectividad.
- Corregir la formulación universal de §6.1 y delimitar el inventario frente a las comprobaciones particulares de K3.
- Reformular §7 como corolario relativo a B1 y a las celdas demostradas de B2, conservando expresamente sus límites y la celda abierta.

Estas reparaciones no requieren cambiar las hipótesis. Con ellas, los reemplazos rederivados sostienen el resultado (b); **el informe actual requiere reparación antes de afirmar la completitud de U1–U14**.