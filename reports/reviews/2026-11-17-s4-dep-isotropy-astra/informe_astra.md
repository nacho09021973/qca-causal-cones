<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.169.0)
inicio: 2026-11-17T10:13:39Z  fin: 2026-11-17T10:18:21Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-17--s4-dep-isotropy.md ; último commit observado: 251c163 ; sha256 de la copia enviada 1515bce1da3b18255b58e2d3f54bb08474533e2fdabf894d548b7dbf9f02eb8d
documento: /home/ignac/qca-causal-cones/theory/S4_DEP_ISOTROPY_GATE.md ; último commit observado: 9188755 ; sha256 de la copia enviada 656add33876586db29e8413e67e587543a029ff95f4022dc02d304920eace259
documento: /home/ignac/qca-causal-cones/theory/S4_STRICT_CONE_COUNTEREXAMPLE.md ; último commit observado: 1dae941 ; sha256 de la copia enviada bc15165e1acb426884018860a78388facc7b98647eefb914e4f2bb2449f47d7c
documento: /home/ignac/qca-causal-cones/scripts/verify_s4_dep_isotropy.py ; último commit observado: 36fb8fd ; sha256 de la copia enviada 03f8ffb7d9396d029d35fb693d21d09c38651644acc42510672d0de0d08523df
documento: /home/ignac/qca-causal-cones/reports/2026-11-17--s4-dep-isotropy-run1.txt ; último commit observado: 36fb8fd ; sha256 de la copia enviada 3dd0f133fff2074396309269e31078d62d9e5c5b0ecc7488fd45da0c60b69981
documento: /home/ignac/qca-causal-cones/reports/2026-11-17--s4-dep-isotropy-run2.txt ; último commit observado: 251c163 ; sha256 de la copia enviada 1ff336e3affa437eb96f8d9b717bbd1ee8d66f04c59f98db433844f9ae316385
documento: /home/ignac/qca-causal-cones/sources/1708.00826v2.pdf ; último commit observado: f74018f ; sha256 de la copia enviada dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81
entrada_astra.txt sha256 e4f0d590f7d4dc46b20fa1362ba9aa42223992c891da5bb44c8be743ad9c2ef2
respuesta sha256 c04ad1b0c580466e7ae6abe688e9fa9ff33df7391f2c73ea3fe30bde09b622ae
-->

La conclusión matemática de isotropía se sostiene: puede comprobarse algebraicamente con las definiciones adjuntas, sin depender del `PASS` del script. Hay una corrección documental menor y una limitación de trazabilidad entre ejecuciones.

Esta revisión usa exclusivamente el material pegado. Las referencias a páginas corresponden al texto extraído adjunto; no he consultado el PDF ni ejecutado el verificador.

1. **FIDELIDAD A LA FUENTE — PASS.**

   El contrato reproduce correctamente la Definición 1 y la condición (2), separadas en la fuente —documento 7, p. 2—. También incorpora la exigencia previa de coeficientes no nulos.

   Las condiciones que podrían quedar implícitas se cumplen aquí:

   - **Automorfismos del grafo:** las medias vueltas son aplicaciones lineales invertibles que preservan el retículo generado por los cuatro vectores de paridad positiva y permutan esos generadores. Por tanto, preservan las aristas dirigidas y su coloreado mediante una permutación global.
   - **Orden de los generadores:** todos tienen orden infinito. La transitividad exigida sobre cada \(S_+^n\) se reduce aquí a la transitividad sobre todo \(S_+\).
   - **Elección de \(S_+\):** es el tetraedro
     \[
     \{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}/\sqrt3,
     \]
     cuyos elementos suman cero. Coincide con la presentación tetraédrica admitida para el BCC —p. 6, figura 1; p. 14—. El retículo generado es abstractamente \(\mathbb Z^3\); no debe confundirse con las coordenadas cartesianas enteras estándar.
   - **Tratamiento de \(S_-\):** \(S_-=-S_+\), y \(l(-h)=-l(h)\). C2 verifica también sus coeficientes, cubriendo la covarianza completa de la ecuación (4). No se necesita imponer \(A_{-h}=A_h^\dagger\).
   - **Fidelidad proyectiva:** ningún \(U_x,U_y,U_z\) es escalar y sus clases módulo fases son distintas. La representación es fiel también en sentido proyectivo.
   - **Unitariedad del walk:** se obtiene del producto de exponenciales de involuciones hermíticas. La comprobación únicamente en \(k=0\) no bastaría, pero la construcción proporciona la prueba para todo \(k\).

   No falta una exigencia de irreducibilidad de \(U\): la Definición 1 no la impone. Tampoco constituye un incumplimiento que \(\sum_h A_h=W\neq I\): la fuente admite multiplicar por una unitaria que conmute con la representación —pp. 3–4—.

   El informe afirma satisfacer específicamente la condición (2). Eso es correcto; no debe ampliarse a una certificación de cualquier formulación adicional de homogeneidad mencionada en la referencia [23].

2. **FAMILIA — PASS.**

   La reconstrucción coincide con las secciones 2–4 del documento 3:

   \[
   T_x=b\tau_x+a\tau_z,\quad
   T_y=b\tau_y+a\tau_z,\quad
   T_z=-b\tau_x+a\tau_z.
   \]

   `TP(SIG[i], T[i])` mantiene el orden \(\sigma\otimes\tau\); `W` tiene las fases correctas para \(\theta=\pi/4\); y el producto de proyectores conserva el orden \(x,y,z\).

   Con la convención declarada,
   \[
   e^{-iq_i\Gamma_i}=\sum_{s_i=\pm1}e^{-is_iq_i}P_i^{s_i},
   \]
   el coeficiente de \(e^{-ik\cdot h_s}\) es exactamente \(WP_x^{s_x}P_y^{s_y}P_z^{s_z}\). No hay inversión accidental de signos. La ausencia del factor \(1/\sqrt3\) en las claves del diccionario es inocua para C1–C5: esas claves representan etiquetas de desplazamiento, no cálculos métricos.

   La acción utilizada en C2 también es correcta:
   \[
   U_l\Gamma_iU_l^\dagger=
   \begin{cases}
   \Gamma_i,&i=l,\\
   -\Gamma_i,&i\ne l.
   \end{cases}
   \]
   No se permutan los factores del producto. Además, estas rotaciones satisfacen \(l^{-1}=l=l^T\), por lo que aquí no hay discrepancia entre la acción sobre \(k\) y sobre los desplazamientos.

3. **MÉTODO EXACTO DE C1 Y C4 — PASS.**

   La sustitución por \(M_h\) es legítima:
   \[
   A_h=WM_h,\qquad [U_l,A_h]=W[U_l,M_h].
   \]
   Basta que \(W\) sea invertible y conmute con \(U_l\); el script comprueba ambas propiedades mediante su unitariedad y los tres conmutadores.

   La parametrización es biyectiva sobre el arco solicitado. Su inversa es
   \[
   t=\frac{b}{1+a}\in(0,1).
   \]
   No se pierde ninguna rama compatible con \(0<a<1,\ b>0\).

   Las entradas de \(M_h\) y de sus conmutadores son polinomios en \(a,b\) con coeficientes en \(\mathbb Q(i)\). Después de sustituir, puede usarse como denominador común
   \[
   8(1+t^2)^3,
   \]
   que no se anula en el intervalo real. Por tanto, pasar a numeradores no introduce ni elimina ceros allí.

   Para \(t\) real, un numerador complejo se anula exactamente cuando se anulan sus partes real e imaginaria. El mcd de todos esos polinomios tiene precisamente sus ceros comunes. Los casos de polinomios nulos y mcd constante están tratados correctamente.

   **Sobre `simplify` y las comparaciones:** sí se usa `simplify`, especialmente en `red` y `mzero`. No sería correcto describir todo el verificador como independiente de esa función. Sin embargo, las identidades se evalúan simbólicamente, sin tolerancias numéricas. El `float` aparece únicamente al ordenar resultados excepcionales, después de decidir su pertenencia al intervalo.

   Hay una limitación de diseño: `zeros_in_domain` nunca devuelve `"UNDECIDED"`, de modo que la línea que imprime «pairs undecided: none» no aporta una comprobación adicional. Tampoco existe una rama explícita para una comparación de raíces que quedase sin resolver. Esto no refuta el resultado de esta familia, que admite el siguiente certificado directo.

   **Segunda vía algebraica para C1 y C4.** Escribiendo \(J_i=\sigma_i\otimes I\), del producto definido se obtiene
   \[
   \operatorname{tr}(J_zM_h)=\frac{i}{2}s_xs_y a^2,\qquad
   \operatorname{tr}(J_xM_h)=\frac{i}{2}s_ys_z a^2.
   \]
   Basta usar \(\operatorname{tr}(T_xT_y)=\operatorname{tr}(T_yT_z)=2a^2\) y las identidades de Pauli.

   La primera expresión prueba \(M_h\neq0\). Por ciclicidad de la traza, además:
   
   | Conmutador | Testigo escalar |
   |---|---|
   | \([J_x,M_h]\) | \(\operatorname{tr}(J_y[J_x,M_h])=s_xs_y a^2\) |
   | \([J_y,M_h]\) | \(\operatorname{tr}(J_x[J_y,M_h])=-s_xs_y a^2\) |
   | \([J_z,M_h]\) | \(\operatorname{tr}(J_y[J_z,M_h])=-s_ys_z a^2\) |

   Todos son no nulos para \(0<a<1\). Así quedan comprobados C1 y los 24 casos de C4 por una vía distinta del cálculo de raíces, sin asumir que las salidas del programa son correctas.

4. **C2, C3 Y C5 — PASS.**

   Las 24 identidades de C2 cubren los tres elementos no triviales y los ocho desplazamientos. Los ocho casos de la identidad son tautológicos.

   En C3, comprobar una órbita por conjunto es suficiente: cada órbita calculada coincide con el conjunto completo. Las medias vueltas preservan la paridad y ningún elemento no trivial fija una terna con todas sus coordenadas iguales a \(\pm1\).

   En C5 se comprueban los seis productos ordenados de elementos no triviales distintos y los tres cuadrados. Los productos con la identidad son inmediatos. Las fases son \(\pm i\) para ejes distintos y \(1\) para los cuadrados. La condición de cociclo se sigue de la asociatividad de las matrices; no hace falta una comprobación separada.

   La unitariedad y fidelidad de los \(U_l\), y la extensión de las permutaciones a automorfismos del grafo, no aparecen como pruebas explícitas separadas en el código, pero quedan establecidas por las matrices y aplicaciones concretas anteriores.

   La segunda lectura de C4 también es correcta:
   \[
   [U_l,M_h]=0\iff M_{l(h)}=M_h.
   \]
   Como reconoce el informe, esta equivalencia por sí sola no constituye una segunda comprobación.

5. **EJECUCIONES — OPEN para la comparación histórica; PASS para su coherencia matemática.**

   La primera salida registra una excepción durante la resolución simbólica y no contiene un veredicto final. No demuestra un fallo de isotropía.

   El método de la segunda versión conserva exactamente la pregunta matemática: quitar el factor invertible \(W\) y parametrizar biyectivamente el dominio no cambia los conjuntos de ceros buscados. Las expectativas del código adjunto coinciden con C1–C5 del contrato.

   Sin embargo, **no se adjunta el código de la ejecución 1 ni el diff entre versiones**. Por tanto, no puede certificarse que esos fueran los únicos cambios. La afirmación histórica «no expectation changed», los commits y su orden temporal permanecen **[UNVERIFIED]** en esta revisión.

   Para cerrar este punto bastaría adjuntar el diff entre las dos versiones comprometidas. No encuentro ninguna contradicción entre las dos salidas y el resultado matemático comprobado arriba.

6. **ALCANCE — REPAIR_REQUIRED menor, documental.**

   El informe distingue los resultados C1–C5 de la pendiente tomada de un trabajo anterior. No afirma novedad, isotropía cúbica, otros grupos ni otros valores de \(\theta\).

   Además, la pendiente **sí puede comprobarse con el material adjunto**, aunque no la calcula este verificador. En el doblete \(\tau_z=+1\),
   \[
   P_+\Gamma_iP_+=a\sigma_iP_+,
   \]
   y la expansión alrededor de \(k=0\) da
   \[
   P_+A(k)P_+
   =e^{-i\theta}\left(I_2-\frac{ia}{\sqrt3}\,k\cdot\sigma\right)
   +O(|k|^2).
   \]
   La separación espectral en \(\theta=\pi/4\) permite obtener así la pendiente \(a/\sqrt3\). No hace falta aceptar como prueba la supuesta promoción en `CURRENT_STATE.md`.

   La afirmación sobre la pérdida de rigidez es defendible para estos dobletes de Floquet y con la normalización espacial declarada. Conviene explicitar que compara esa pendiente con el cuerpo de soporte estricto; no demuestra una afirmación sobre un frente balístico definido por amplitudes.

   **La discrepancia documental concreta** está en la cabecera del verificador: anuncia comprobaciones de proyectores `P`, pero no las ejecuta explícitamente. Su propiedad de proyector se deduce de las comprobaciones de hermiticidad e involución de \(\Gamma_i\).

   **Reparación mínima:** sustituir esa descripción por «se comprueba que \(\Gamma_i\) son involuciones hermíticas; de ello se deduce que \(P_i^\pm\) son proyectores». No hace falta añadir pruebas redundantes.

   Para precisar también la conclusión física, recomiendo esta formulación:

   > C1–C5 certifican la isotropía declarada. La expansión espectral de la familia, calculada separadamente, da pendientes Weyl \(c_0=a/\sqrt3\) alrededor de las cuasienergías \(\pm\pi/4\). Con \(c_{\rm strict}^{\rm iso}=1/\sqrt3\), esta noción de isotropía no fija esa pendiente al pasar a dimensión interna cuatro.

**Dictamen global: REPAIR_REQUIRED, limitado a documentación.** La conclusión matemática `DEP_ISOTROPIC_IN_DECLARED_L` recibe **PASS** para todo \(0<a<1\). La comparación histórica íntegra entre las ejecuciones permanece **OPEN** hasta disponer del diff.