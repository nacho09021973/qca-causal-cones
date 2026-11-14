<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.169.0)
inicio: 2026-11-14T21:51:08Z  fin: 2026-11-14T21:51:52Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-matchgate-a5.md ; último commit observado: 030e585 ; sha256 de la copia enviada f042b18d6492f938dcfbd8d375d796c474c5e06adad3acfec5545cbd3f4da1a5
documento: /home/adnac/qca-causal-cones/reports/reviews/2026-11-14-thirring-matchgate-a5-astra-rereview/informe_astra.md ; último commit observado: e3413e3 ; sha256 de la copia enviada 11f0c710c8e92768931423f6de4b28dfa79c272a9838e767a3a33d0477416f89
entrada_astra.txt sha256 890bb295412107a892b6bfc60f7f929ec59b6c3dac10a9316d7b148e9a0931bb
respuesta sha256 1805d779fdd6b181a05abe5d93784404d690bae50e629b5d4ddc834ff31a4666
-->

**Dictamen global: PASS para la reparación R2.** Revisión por lectura y derivación del material adjunto, sin herramientas. No reabro R1, R3, R4 ni R5. Commits, ejecuciones y atribuciones bibliográficas no comprobados aquí: **[UNVERIFIED]**.

1. **ORIENTACIÓN — PASS.**

   Para cada par que cruza, orientar con el paquete inicialmente derecho primero impone \(x_p-x_q>0\). El criterio de cruce implica entonces \(K_p>K_q\) y, por monotonía, \(v_p-v_q>0\). Ambos factores del denominador de la comparación son positivos, de modo que
   \[
   \operatorname{sign}(t_{pq}-t_{rs})=\operatorname{sign}(E).
   \]
   La convención también concuerda con el primer factor de la puerta en Sec. 2: mientras un par no se haya intercambiado, conserva su orden relativo, incluso durante la resolución de un empate.

2. **EMPATES — PASS.**

   La regla ahora restringe explícitamente la elección lexicográfica a los pares **pendientes y actualmente adyacentes**, y actualiza los slots después de cada intercambio.

   **Prueba de terminación y completitud.** En un bloque coincidente, las velocidades distintas hacen que el orden inmediatamente posterior sea el inverso del anterior. Respecto de ese orden objetivo, inicialmente todos los pares son inversiones. Un intercambio adyacente solo cambia el orden relativo del par intercambiado; por tanto, los pares pendientes son exactamente las inversiones restantes. Cada paso elimina una inversión y no introduce ninguna. Si queda alguna inversión, existe una inversión adyacente —de lo contrario, toda la lista estaría ordenada—, así que la regla no puede atascarse. Termina tras exactamente \(\binom{k}{2}\) intercambios, uno por par.

   **Ejemplo solicitado.** Para
   \[
   K=(3/4,-3/4,0),\qquad v=(3/5,-3/5,0)=x,
   \]
   los tres paquetes llegan a \(x=0\) en \(t=1\). El orden inicial, contado desde la derecha, es \((1,3,2)\). Con los pares orientados según Sec. 5:
   \[
   (1,3,2)\xrightarrow{(1,3)}(3,1,2)
   \xrightarrow{(1,2)}(3,2,1)
   \xrightarrow{(3,2)}(2,3,1).
   \]
   Cada elección es la menor disponible entre pares pendientes adyacentes. Se intercambian los tres pares una vez y se obtiene el orden inverso.

   Los encuentros en puntos distintos al mismo tiempo forman bloques disjuntos: ningún paquete puede pertenecer a dos puntos simultáneamente. Sus intercambios actúan sobre slots disjuntos y conmutan; intercalarlos mediante la regla global no altera esta prueba.

3. **CUERPO DE ALPHA — PASS.**

   El cuerpo
   \[
   F_{pq}=\mathbb Q(\sqrt{1+K_p^2},\sqrt{1+K_q^2})
   \]
   contiene \(a(K_p),a(K_q)\) y su cociente, pues \(a(K_q)>0\). Como \(1+r^2>0\), también contiene \(\beta\) y \(\alpha/i\). En consecuencia, \(\alpha\in F_{pq}(i)\). La nueva redacción corrige exactamente el defecto anterior.

4. **COSTES — PASS.**

   Se distingue correctamente \(N\), número de paquetes, de \(n\), longitud total de entrada. Ordenar los eventos y resolver empates cuesta \(\mathrm{poly}(n)\); incluso buscar candidatos mediante barridos completos sigue siendo polinómico. Cada parámetro admite una representación algebraica exacta de tamaño polinómico y aproximación en \(\mathrm{poly}(n,m)\).

   La formulación separa el modelo de acceso a puertas de Jozsa–Miyake del coste de generar esta instancia. Asimismo, mantiene las probabilidades de subconjuntos y el muestreo en el modelo aritmético exacto, sin atribuirles una cota de precisión finita no demostrada.

5. **EDICIONES — PASS.**

   El encabezado recoge las cuatro correcciones. La Sec. 3 remite a la regla que preserva adyacencia y mantiene explícita la resolución especificada para coincidencias múltiples. No detecto errores nuevos introducidos por estas ediciones.

**Reparaciones obligatorias: ninguna.** F, la unicidad en coincidencias de cuatro o más paquetes y la propagación de errores para salidas múltiples permanecen **OPEN**; este PASS no los cierra.