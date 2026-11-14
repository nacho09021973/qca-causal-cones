<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.169.0)
inicio: 2026-11-14T18:24:11Z  fin: 2026-11-14T18:26:08Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-comoving-packet.md ; último commit observado: e81a719 ; sha256 de la copia enviada 979ecf49f8d31bffc921584c4ae01801ed80734deed00b1bb838b298c422fcf1
documento: /home/adnac/qca-causal-cones/theory/THIRRING_COMOVING_PACKET_GATE.md ; último commit observado: dca5ebc ; sha256 de la copia enviada 3db4cb5e00ff0146e9deae63533a996cea8a152cae16cba34fcdcebbfd1cc0f6
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_comoving_packet.py ; último commit observado: 2685635 ; sha256 de la copia enviada a72db65cf837921d2448315babce39ff93d9ac8077ab9f226abf77f039a9ac55
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-comoving-packet.txt ; último commit observado: e81a719 ; sha256 de la copia enviada 0861bf7273608a3c392eb3589b7d0357cf7326fc8dc80eae99190c7d2b5eff18
documento: /home/adnac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet.md ; último commit observado: 55f2b43 ; sha256 de la copia enviada d5d21b221fc3c70d15dfb6c57cbc40372a51a40c2bda59b14eb7c974546d2f2f
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-flavour-packet.md ; último commit observado: 918f7f4 ; sha256 de la copia enviada 39e595ce17ac1e5f2f0ad6fa3821f5e413e44ed2a0126aa39c4674e58eb8118e
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_low_energy_packet.py ; último commit observado: 8b41761 ; sha256 de la copia enviada a1900674990354db197e7daddfdefb46d0a23536ba3b5e0688c2b45250f4d517
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_flavour_packet.py ; último commit observado: 8d7e444 ; sha256 de la copia enviada 7e66c30ac95cb3b7f76f195831ec1d742e595dad52994361d44dcdcf8c0af6cd
documento: /home/adnac/qca-causal-cones/sources/1711.03920v1.pdf ; último commit observado: 45b933f ; sha256 de la copia enviada 3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca
entrada_astra.txt sha256 f1bd19bc96170687ffd5666a0a70319ea80bfda1f8f22f438bd38f1b4759d76c
respuesta sha256 f4903c7c9a11cd22b1c5a657005f0935979ba10f76ce3809ccb25809d3e50f58
-->

**Dictamen global: REPAIR_REQUIRED.** No encuentro un fallo que invalide la puerta co-móvil declarada. Sí encuentro dos reparaciones obligatorias: los «si y solo si» de A2/A5 omiten excepciones, y «52/52 exact» incluye dos comprobaciones numéricas de positividad. La simulabilidad física permanece **OPEN**.

Revisión basada únicamente en los documentos suministrados, mediante lectura del código y derivaciones manuales; no he ejecutado el verificador ni consultado el PDF original.

1. **Geometría co-móvil del puente: PASS.**

Con la convención \(e^{-i(qx+t\omega(q))}\), el centro sigue
\[
x(t)=x(0)-t\omega'(q).
\]
Por tanto, para la onda con \(q_f\) en la coordenada mayor,
\[
y_{\rm in}(t)=2L-t(v_f-v_s).
\]
Es entrante: el paquete rápido empieza a la derecha y alcanza al lento desplazándose ambos hacia la izquierda. La onda intercambiada tiene
\[
y_{\rm out}(t)=-2L+t(v_f-v_s).
\]
La identificación no depende de que las velocidades tengan signos opuestos.

Las cotas racionales bastan:
\[
v_f\ge\sqrt{0.87}>0.93,\qquad v_s\le0.8.
\]
Así, a \(T=20L\), los centros relativos quedan respectivamente por debajo de \(-0.6L\) y por encima de \(0.6L\). Estar en el semiespacio incorrecto exige que alguna coordenada individual se desvíe al menos \(0.3L\). No hace falta una separación absoluta respecto del origen, pues ambos paquetes pueden estar muy a la izquierda.

La extensión temporal conserva la estimación:
\[
t\delta^2/\mu\le20\lceil\mu^{-2}\rceil\mu^2=O(1).
\]
Con \(D=3L/10\), resulta \(\delta D\asymp\mu^{-1/2}\), masa de cola \(O(\mu^{3/2})\) y norma \(O(\mu^{3/4})\). También se conservan las estimaciones con \(T(q_1,q_2)\) no separable.

**Aclaración:** el factor cinco corresponde al límite del parámetro temporal que controla las derivadas de fase. La constante final tras integrar por partes no tiene por qué ser exactamente cinco veces la anterior. El exponente y la uniformidad no cambian.

2. **Autofunciones y degeneraciones: PASS, con aclaración de las distancias.**

La ecuación local de contacto reutilizada,
\[
z(b-Tc)=Tb-c,
\]
no necesita momentos de signos opuestos. Las cuatro ondas comparten el autovalor y la extensión antisimétrica satisface las mismas ecuaciones locales. El argumento sirve en ambos sectores del soporte declarado.

La frase sobre degeneraciones es demasiado abreviada: el Lema 1 del texto suministrado, p. 3, también contiene la hipótesis \(p\ne n\pi/2\). No obstante, aquí puede comprobarse directamente. Escribiendo \(m=\sqrt\mu\),
\[
q_f-q_s\ge2\mu(1-m),\quad
p=\frac{q_f+q_s}{2}\in\mu[2-m,2+m],\quad
k=\frac{q_f-q_s}{2}\in\mu[1-m,1+m].
\]
Hay, pues, separación proporcional a \(\mu\) respecto de \(q_f=q_s\), de \(k=0\) y de \(p=0\); los restantes puntos periódicos quedan lejos.

En el sector mixto, tomando \(q_s'=q_s+\pi\),
\[
p'=p+\pi/2,\qquad k'=k-\pi/2.
\]
Las distancias a las degeneraciones correspondientes son precisamente \(p\) y \(k\). No son distancias uniformemente positivas sin reescalar, pero sí respecto de la anchura \(\delta=\mu^{3/2}\).

Tampoco se alcanzan los autovalores excepcionales \(e^{\pm i2p}\): para estos momentos pequeños positivos, \(\omega(q)>q\), de modo que
\[
\omega(q_f)+\omega(q_s)>q_f+q_s,
\]
sin posibilidad de identificación por periodicidad. El desplazamiento del sector mixto multiplica por \(-1\) tanto el autovalor como los valores excepcionales.

Los denominadores admiten una comprobación más fuerte que la mera positividad del límite. Definiendo
\[
A_\mu(q)=\frac{\sin\omega(q)+\nu\sin q}{\mu}
=\sqrt{1+\nu^2(\sin q/\mu)^2}+\nu\sin q/\mu,
\]
se tiene \(A_\mu(q)\ge1\) en ambos soportes. Los dos denominadores escalados tienen módulo
\[
\sqrt{A_\mu(q_f)^2+A_\mu(q_s)^2}\ge\sqrt2.
\]
Esto sostiene las cotas de derivadas, incluidas las segundas utilizadas en las colas.

E1/E2 son ejemplos válidos y no degenerados. Su \(\mu=3/5\) queda fuera del régimen de paquetes, pero eso es admisible como comprobación ilustrativa de la identidad local. La ventana finita comprueba los casos de contacto y los de propagación libre; su extensión a toda la red depende de esa estructura local, no del recuento.

3. **Orden, \(r_{\rm co}\) y ensamblaje: PASS.**

La elección está fijada por **la geometría entrante junto con el orden declarado**: el primer factor de creación es el rápido y ocupa inicialmente la coordenada mayor. Por ello,
\[
r_{\rm co}=a(3)/a(1).
\]
El orden de creación, aislado de la identificación entrante, no sería una regla universal para escoger entre \(r\) y \(1/r\).

Una comprobación independiente usa \(\Delta\theta=\operatorname{asinh}3-\operatorname{asinh}1\):
\[
\cosh\Delta\theta=2\sqrt5-3,\qquad
\beta=\operatorname{sech}\Delta\theta=\frac{3+2\sqrt5}{11}.
\]
Además, \(\alpha=i\tanh\Delta\theta\), con parte imaginaria positiva, da
\[
\alpha=\frac{i\sqrt{92-12\sqrt5}}{11}.
\]
Los valores son correctos.

AA y BB evolucionan exactamente como sus columnas de \(B_{\rm out}\); esto fija la fase común a \(1\). El signo antisimétrico de la onda intercambiada aparece también en la comparación libre y no introduce otra fase.

Para sentidos opuestos,
\[
a(1)/a(-2)=a(1)a(2)
=e^{\operatorname{asinh}1-\operatorname{asinh}(-2)},
\]
coherente con la misma convención.

4. **Parte A, A1–A4: REPAIR_REQUIRED por el alcance de A2.**

A1 y la identidad racional de A2 son correctas. El código de A3 construye las matrices \(8\times8\), implementa \(V_{13}\) mediante permutación y recorre las 64 entradas. A4 comprueba la relación parametrizada escrita para \(PV\). No hay una reducción oculta a un único sector.

La separación respecto de factorización física y estructura graduada está bien expresada.

**Reparación obligatoria R1, primera parte.** Frase afectada: «zero iff \(z^2=-1\)».

La propia identidad muestra
\[
1+\alpha^2-\beta^2
=\frac{(z^2+1)(r^2-1)}{z^2r^2-1}.
\]
También se anula en \(r=1\), cuando el denominador está definido. Allí \(\alpha=0,\beta=1\), y la definición cociente de \(\Delta\) es \(0/0\).

Lo cierra distinguir entre:

- igualdad puntual, con la excepción \(r=1\);
- identidad nula para toda la familia, que sí exige \(z^2=-1\);
- \(\Delta=\cos\chi\) donde su cociente está definido, o mediante extensión racional explícita.

5. **A5 y su lectura: REPAIR_REQUIRED por R1; simulabilidad física OPEN.**

Los determinantes calculados son correctos:
\[
V:(1,-1),\qquad \mathrm{fSWAP}\,V:(-1,1),\qquad PV:(1,1)
\]
a \(z=-i\).

El cambio a orden de posición produce \(PV\) **hasta una fase global convencional**. Si ambas bases se construyen literalmente ordenando los operadores fermiónicos por posición, intercambiar los dos paquetes introduce un signo común y puede escribirse \(-PV\). Cada paquete contiene exactamente un fermión para ambos sabores: ese signo es igual para AA, AB, BA y BB. No es el signo selectivo de fSWAP sobre \(|11\rangle\), y no altera la condición de determinantes.

**R1, segunda parte.** Frase afectada: «\(PV\) meets the determinant condition exactly at \(\chi=\pi/2\)».

En \(r=1\), \(V=P\) y \(PV=I\) para cualquier acoplamiento con denominador definido. Para \(r\ne1\), la condición es \(z^2=-1\), es decir, \(\chi=\pi/2\pmod\pi\). Lo cierra introducir esas condiciones o restringir explícitamente la afirmación al acoplamiento declarado.

La lectura de simulabilidad está marcada como no verificada y condicionada; no constituye un veredicto. La igualdad de determinantes sí identifica una matchgate abstracta en la base escrita. La naturaleza fermiónica del sabor no la refuta automáticamente. Lo pendiente es demostrar que una evolución física con muchos paquetes se representa por el circuito correspondiente y precisar preparaciones y medidas admitidas. La condición local de determinantes, sola, no demuestra ninguna de esas cosas.

6. **Alcance y certificación: REPAIR_REQUIRED por una calificación incorrecta.**

La separación entre puente escrito, álgebra comprobada y cuestiones abiertas es sustancialmente correcta. No se afirma factorización física, universalidad ni un no-go general.

**Reparación obligatoria R2.** Frases afectadas: «52/52 exact» y «Certified exactly (52/52)».

En `check_C`, `C-beta>0` y `C-concurrence(V|AB>)>0` usan `sp.N(..., 30) > 0`. Son evaluaciones numéricas, aunque las expresiones originales sean exactas. El informe anterior ya reconocía esta misma distinción.

Lo cierra calificar el recuento o sustituir esas dos comprobaciones por pruebas exactas. La prueba manual es inmediata: \(r_{\rm co}>1\) implica \(\beta>0\) y \(\operatorname{Im}\alpha>0\), luego la concurrencia es positiva.

**Reparaciones obligatorias: R1 y R2, únicamente.** Las aclaraciones sobre degeneraciones, constantes y fase al ordenar por posición no cambian la puerta ni las cotas del puente.