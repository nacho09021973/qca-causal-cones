<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.169.0)
inicio: 2026-11-14T20:25:24Z  fin: 2026-11-14T20:26:43Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-matchgate-a5.md ; último commit observado: b8f0483 ; sha256 de la copia enviada c81dc1fb210459d41fb72028885919f857c9350aea22e9cb8ad08f3c0537f592
documento: /home/adnac/qca-causal-cones/reports/reviews/2026-11-14-thirring-matchgate-a5-astra/informe_astra.md ; último commit observado: 47ea467 ; sha256 de la copia enviada e403960502f7e352ec6af00a1d958a9c4dfe7dc8bee719d9b39d118e50b678c9
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_matchgate_a5.py ; último commit observado: eae7876 ; sha256 de la copia enviada 8a5de947de8627d81f641ef7cbe1c21be599dae5c59ff99c06597cea50f0cb1a
documento: /home/adnac/qca-causal-cones/sources/valiant-stoc2001.pdf ; último commit observado: a1cfd20 ; sha256 de la copia enviada ff54395f2a04bcffcb8f483bca409d9328aceed2545312d7a35479beb9958572
entrada_astra.txt sha256 a1a6ddecac327d3fdedba79ac6932a4c24d51bfd574ce284a49a6c7d1bff32ee
respuesta sha256 bddf862d52a5ece876b6a0772b72ea0273a342c032c0779b6ffe03bd02d07996
-->

**Dictamen global: REPAIR_REQUIRED.** R1, R3, R4 y R5 quedan reparadas. R2 necesita precisar dos convenciones del algoritmo y corregir una afirmación sobre el cuerpo algebraico. No reabro los bloques algebraicos anteriormente aprobados.

Revisión por lectura y derivación sobre los documentos suministrados, sin ejecutar herramientas. Commits, hashes y ejecuciones declaradas: **[UNVERIFIED]** en esta revisión.

1. **R1 — PASS.**

   La frase pertinente es:

   > “acts, on the logical sector with exactly one fermion per packet, as the restriction of the even operator”

   Se completa correctamente con:

   > “The formula is not a unitary on the whole Fock space […] no extension outside the code is defined or assumed.”

   Esto corrige el dominio sin exigir ninguna extensión física adicional. El comentario antiguo del verificador conservado no invalida la restricción explícita del informe reparado.

2. **R2 — REPAIR_REQUIRED.**

   **Criterio de cruce: correcto**, para evolución futura \(t>0\). Como \(v(K)\) es estrictamente creciente y las posiciones iniciales son distintas, \(t_{pq}>0\) equivale a
   \[
   (x_p-x_q)(K_p-K_q)>0.
   \]

   **Comparación temporal: falta explicitar la orientación.** Definiendo
   \[
   E=(x_p-x_q)(v_r-v_s)-(x_r-x_s)(v_p-v_q),
   \]
   se tiene
   \[
   t_{pq}-t_{rs}=\frac{E}{(v_p-v_q)(v_r-v_s)}.
   \]
   Por tanto, el signo de \(E\) proporciona directamente el orden solo si el producto de denominadores es positivo. Basta declarar que cada par se orienta con el paquete inicialmente derecho primero; para pares que cruzan, ambos denominadores serán positivos. Alternativamente, debe incorporarse su signo. Como comprobación independiente: intercambiar los nombres \(p,q\) deja \(t_{pq}\) intacto, pero invierte \(E\). La igualdad \(E=0\) sí detecta empates sin esa convención.

   **Cuatro raíces: correcto.** La expresión contiene como máximo cuatro raíces cuadradas de racionales. Al ser un número fijo, el grado algebraico está acotado por 16 y las alturas tienen longitud polinómica en la entrada; la decisión exacta del signo admite coste polinómico. No aparece aquí el problema de sumar un número variable de radicales.

   **Resolución lexicográfica: insuficientemente especificada.** Ordenar lexicográficamente todos los pares empatados puede seleccionar un par no adyacente. Por ejemplo, en un bloque cuyo orden inicial es \((1,3,2)\), el par lexicográficamente primero \((1,2)\) ocupa los extremos. Esto puede ocurrir con datos racionales admitidos: \(K=(3/4,-3/4,0)\), \(x=(3/5,-3/5,0)\); los tres coinciden en \(t=1\).

   Una reparación concreta es escoger repetidamente el menor par lexicográfico **entre los pares actualmente adyacentes pendientes de cruzar**, actualizando los slots. Equivale a ordenar el bloque hacia su orden final mediante intercambios adyacentes; cada par se intercambia una vez. Debe declararse esa regla u otra igualmente explícita y válida.

   **Parámetros:** \(a(K)=\sqrt{1+K^2}+K\) y \(r_{pq}=a(K_p)/a(K_q)\) son correctos, respetando la orientación de Sec. 2. Pero es falsa literalmente la inclusión conjunta de \(\alpha,\beta\) en
   \(\mathbb Q(\sqrt{1+K_p^2},\sqrt{1+K_q^2})\): ese cuerpo es real y \(\alpha\) es imaginaria no nula. Debe añadirse \(i\), o afirmar que pertenecen al cuerpo real \(\beta\) y \(\alpha/i\).

   **Precisión y salida:** la separación entre aritmética exacta y aproximación queda bien declarada. Limitar marginales y muestreo al modelo aritmético exacto, dejando explícitamente sin rederivar sus errores finitos, es suficiente para ese alcance reducido. “Una asignación consultada” elimina correctamente la interpretación de una tabla exponencial. Al aplicar la cota de J–M al modelo de entrada propio, debe escribirse \(\mathrm{poly}(n,m)\); \(\mathrm{poly}(N,m)\) puede conservarse como formulación del teorema con su modelo de acceso a puertas.

3. **R3 — PASS.**

   El texto primario adjunto confirma, mediante los pies de página:

   - **Main Theorem:** p. **120**, incluido el apartado (b) de vecinos.
   - **Theorem 4:** p. **120**, sobre asignaciones parciales.
   - **Measurement Theorem:** p. **121**, con generación aleatoria de salidas.

   La modificación declarada de `sources/README.md` no está adjunta: **[UNVERIFIED]**.

4. **R4 — PASS, como conclusión condicional.**

   Las Secs. 1 y 8 ya afirman simulabilidad y la implicación «universalidad eficiente ⇒ \(BQP\subseteq P\)», sin separación incondicional. La Sec. 1 delimita correctamente la decisión a aceptación en una línea con brecha acotada. Su aplicación al modelo concreto queda pendiente de cerrar R2; no requiere otro cambio conceptual.

5. **R5 — PASS.**

   La sustitución por \(\chi\not\equiv\pi/2\pmod\pi\) realiza la reparación solicitada. La mención de \(3\pi/2\) recoge correctamente la otra representante pertinente. Este PASS cierra la corrección literal; no constituye una nueva verificación de la familia general no adjunta.

6. **ACLARACIONES Y EDICIONES — REPAIR_REQUIRED, limitada a R2.**

   El encabezado recoge fielmente las aclaraciones sobre espectadores, resoluciones especificadas, convenciones de Valiant, adaptatividad restringida y fermiones del registro. Sin embargo, anticipa que el orden y los empates están completamente resueltos, cuando falta concretar lo anterior. La inclusión de \(\alpha\) en un cuerpo real es una afirmación nueva incorrecta.

**Reparaciones obligatorias:** explicitar la orientación o el signo de denominadores; definir una resolución lexicográfica que preserve adyacencia; corregir el cuerpo algebraico de \(\alpha\); expresar el coste de la instancia en función de \(n\). Después, sincronizar el encabezado con esas correcciones. F y la propagación de errores para salidas múltiples permanecen **OPEN**, como declara el informe.