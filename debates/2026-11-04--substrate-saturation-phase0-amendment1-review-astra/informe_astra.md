<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.1-sol, esfuerzo: high, vía: codex exec sellado (codex-cli 0.166.0)
inicio: 2026-11-04T08:04:11Z  fin: 2026-11-04T08:08:04Z
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE_AMENDMENT_1.md ; último commit observado: cecf75a ; sha256 de la copia enviada b6598fa7de3ddec45cdd4408a2ba6e05500b0bf51d7ad3fd7a0c479a1db6a45d
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0.md ; último commit observado: 6aa42f9 ; sha256 de la copia enviada c64eb3228bf927710bad6e00d5fd026f4ce48721fe1553092ba40057b12a4ceb
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0-addendum-L4.md ; último commit observado: 738b62c ; sha256 de la copia enviada b8b9ed87d5df373ea152c54252a5034bfbc30bebd4222ada0d2f387a896dd8b8
documento: /home/ignac/qca-causal-cones/theory/C_ACROSS_LATTICES_GATE.md ; último commit observado: 30672ba ; sha256 de la copia enviada b58deeec91184fbf976a6cb857c8e935ec7d4a4e52d6608a62768452759e34e3
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-amendment1-review-astra/cjww_pp16-17.txt ; último commit observado: sin versionar ; sha256 de la copia enviada 68d4b9c97dedcc638ba1f55cc50e888497a3d1ce313d83a85c6ebe3399d70f5e
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-amendment1-review-astra/extractos.md ; último commit observado: sin versionar ; sha256 de la copia enviada e6560b2b4e73b973b2b232fe9d967515d9ca78ea21362880cd51d0b065d7b140
entrada_astra.txt sha256 a44fb543af082c43980380f254e250ae47ef66ef6efb01b4b689f79f15f8b104
respuesta sha256 2c7020f1c85b32103db4cb43d658617982ffb608c4c74dbc4d00fdb799e0d759
-->

**Dictamen global: PASS del borrador como propuesta condicional. No encuentro reparaciones obligatorias.** Hay aclaraciones útiles sobre la procedencia documental y una inconsistencia de signo en la fuente que conviene registrar.

Juzgo exclusivamente los textos adjuntos. Los PASS anteriores de DeepSeek no se usan como evidencia; tampoco doy por comprobados sus expedientes, hashes o commits.

1. **REGLA — PASS.**

   La Sec. 1 conserva los requisitos sustantivos: pertenencia a una clase congelada, nodo isotrópico sin tilt, dimensión interna y espacial, definición operacional del sustrato y fuente única para `(r_in,c_0)`. No modifica los contraejemplos de la Sec. 4 ni convierte la ausencia de contraejemplos en evidencia.

   Sí cambia una exigencia documental: permite establecer el nodo mediante una derivación revisada, en lugar de depender exclusivamente de la certificación citada en la Sec. 2.4 congelada. Esto es precisamente la excepción anunciada, no una certificación retroactiva del informe anterior.

   **Aclaración editorial:** «replaces nothing» es menos preciso que el contenido real. Mejor: «conserva las condiciones matemáticas y añade una excepción explícita a la procedencia documental del nodo». No considero que la formulación actual invalide la regla: la cabecera reconoce la prevalencia localizada de la enmienda y la Sec. 3 exige cumplir todo lo demás.

   La condición de clase basta para excluir la mera aparición en una tabla: exige una declaración congelada y su regla de admisión. No basta una fila incidental de un informe.

   Una revisión de una sola casa satisface la regla propuesta si esa casa pertenece a una familia distinta de la autora. Dos revisiones de DeepSeek no constituyen dos familias independientes, pero el borrador tampoco lo afirma. **INSUFFICIENT_EVIDENCE únicamente sobre el cumplimiento documental efectivo de Sec. 1.3:** no se adjuntan los expedientes que permitirían comprobar SHA-256, commit base y ausencia de reparaciones pendientes. Esto debe comprobarse antes de aplicar la regla; no refuta su diseño.

   La enmienda posterior al resultado es legítima dentro del alcance declarado: revisión transparente de una auditoría definicional, sin valor confirmatorio. No puede presentarse como criterio prerregistrado ni como validación independiente de (PH).

2. **CLASE — PASS.**

   C_ACROSS_LATTICES no contiene una tabla incidental: su Sec. 0 declara como objeto los pares de red y familia; la Sec. 2 enumera las filas admitidas; L4 identifica dos ecuaciones concretas; y l. 100–104 prescribe cómo admitir sus símbolos y prohíbe construir otros walks.

   Por tanto, la clase pertinente puede ser el conjunto finito
   \[
   \mathcal C_{L4}=\{W_{(5.12)},W_{(5.15)}\}.
   \]
   Una clase no necesita parámetros libres. La frase «The declared class of L4 is therefore the two printed walks» está justificada por la combinación de declaración y admisión, no por la fila aislada.

   El alcance termina ahí: no declara todos los walks cúbicos, toda una familia de Bialynicki-Birula ni variantes arbitrarias. La corrección operacional del sustrato de uno de sus miembros no añade un modelo: aplica la definición congelada de «substrate».

3. **FUENTE Y NODO — PASS, con una inconsistencia de la fuente que conviene explicitar.**

   Frente al extracto suministrado, las transcripciones de (5.12) y (5.15) son correctas. Este cotejo no acredita por sí mismo la inspección del PDF que exige el expediente de revisión.

   Tomo matrices de Pauli convencionales y
   \[
   W(p)=I-i\sum_a p_aT_a+O(|p|^2),\qquad T_a=i\partial_aW(0).
   \]

   Para **(5.12)**:

   - (i) Cada factor vale \(I\) en cero: \(W(0)=I\).
   - (ii) \(\partial_aW(0)=i\sigma_a\), luego \(T_a=-\sigma_a\), Hermitiano.
   - (iii) \(\operatorname{tr}T_a=0\).
   - (iv) \(\{T_a,T_b\}=2\delta_{ab}I\), por tanto \(c_0=1\) en estas coordenadas.
   - (v) \(A(n)=-n\cdot\sigma\) satisface \(A(n)^2=|n|^2I\), con autovalores \(\pm|n|\). Su centro lineal es cero: no hay tilt.

   Para **(5.15)**, escribiendo \(a=c_1c_2e^{ip_3}\) y \(b=-c_1s_2+is_1\), la matriz es
   \[
   \begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix},
   \qquad |a|^2+|b|^2=1.
   \]
   Esto comprueba directamente su unitariedad para momentos reales. Además:

   - (i) \(W(0)=I\).
   - (ii) Las derivadas son \((i\sigma_1,-i\sigma_2,i\sigma_3)\), de modo que \(T=(-\sigma_1,\sigma_2,-\sigma_3)\), Hermitiano.
   - (iii) Los tres generadores son traceless.
   - (iv) Satisfacen la misma relación de Clifford: \(c_0=1\).
   - (v) \(A(n)^2=|n|^2I\), con espectro \(\pm|n|\) y sin componente identidad.

   **Segunda comprobación del término dominante:** ambas semitrazas tienen expansión \(1-|p|^2/2+O(|p|^3)\); producen el mismo cono lineal.

   **Signo de (5.13).** Usando \(\sigma_1\sigma_2\sigma_3=iI\), el término triple del producto (5.12) es
   \[
   i^3s_1s_2s_3\,\sigma_1\sigma_2\sigma_3
   =+s_1s_2s_3I.
   \]
   Por ello
   \[
   \tfrac12\operatorname{tr}W=c_1c_2c_3+s_1s_2s_3,
   \]
   como declara el verificador l. 81 y reproduce la enmienda. El **menos** impreso en (5.13) es inconsistente con (5.12) bajo esta convención.

   No falla la transcripción del borrador: éste sigue la ecuación matricial. Conviene añadir una nota que registre la discrepancia, sin corregir silenciosamente el artículo. No afecta a (i)–(v), al soporte ni al radio; sí afecta a términos superiores de dispersión: alrededor de cero, el producto da
   \[
   \omega^2=|p|^2-2p_1p_2p_3+O(|p|^4),
   \]
   mientras que el signo impreso en (5.13) da el signo cúbico contrario. No debe extenderse la irrelevancia del signo a otros cálculos.

4. **SUSTRATO — PASS.**

   Para **(5.12)**,
   \[
   e^{ip_a\sigma_a}=\sum_{\varepsilon=\pm1}
   e^{i\varepsilon p_a}P_a^\varepsilon,\qquad
   P_a^\varepsilon=(I+\varepsilon\sigma_a)/2.
   \]
   El coeficiente de cada esquina es
   \(P_1^{\varepsilon_1}P_2^{\varepsilon_2}P_3^{\varepsilon_3}\).
   Ninguno se anula: los autoestados de ejes consecutivos tienen solapamiento de módulo \(1/\sqrt2\). Así,
   \[
   F_{12}=\{\pm1\}^3.
   \]
   Su grupo generado es
   \[
   G_{12}=\{x\in\mathbb Z^3:x_1\equiv x_2\equiv x_3\pmod2\}.
   \]
   La inclusión directa es inmediata; la inversa resulta de una esquina y las diferencias que generan \(2e_a\). Es BCC en esta escala.

   Para **(5.15)**, las distintas entradas dan exactamente
   \[
   F_{15}=
   \{(\pm1,\pm1,\pm1)\}
   \cup\{(\pm1,\pm1,0)\}
   \cup\{(\pm1,0,0)\}.
   \]
   No hay cancelación entre esos conjuntos, que ocupan exponentes distintos. Generan \(\mathbb Z^3\): están \(e_1\), la diferencia \((1,1,0)-e_1=e_2\), y \((1,1,1)-(1,1,0)=e_3\).

   Ambos soportes contienen las ocho esquinas y están dentro del cubo: sus envolventes son exactamente \([-1,1]^3\). El máximo desplazamiento mide \(\sqrt3\); normalizarlo a uno da \(r_{\rm in}=c_0=1/\sqrt3\), coherente con l. 147, sin sustituirla como fuente del par.

   **Aclaración:** (5.12) también puede definirse sobre el espacio ambiente \(\mathbb Z^3\), conservando sus cuatro cosets BCC. La afirmación «not for (5.12)» es correcta respecto del *grupo generado* exigido por el contrato, no como imposibilidad de formularlo sobre \(\mathbb Z^3\).

   Con las agrupaciones de F3, se añade un sustrato admisible: el de (5.15). (5.12) comparte grupo y soporte normalizados con el BCC ya contado. El total pasa de cinco a seis, contando separadamente el hexágono de grupo más fino. No aparece ninguna forma nueva.

   La inconsistencia de DISPERSION_CORRECTIONS está bien identificada: l. 63 atribuye a BCC el constructor cuyo soporte genera \(\mathbb Z^3\), y l. 67 usa para «cube» el walk BCC. Registrar esto no determina qué resultados ejecutados están afectados. El borrador mantiene correctamente esa separación.

5. **EFECTO Y ALCANCE — PASS.**

   La clasificación corregida elimina una incertidumbre de admisibilidad y actualiza F3. No modifica los criterios de contraejemplo. Ambos `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE` permanecen: ninguno de estos walks aporta un cuerpo no hipercúbico saturante ni una imposibilidad de saturación sobre un hipercubo.

   `DEFINITIONS_CLOSED` queda correctamente condicionado a **todos** los requisitos restantes, incluido el origen promovido de los campos exigidos. La derivación revisada no autoriza completar otros datos faltantes.

   F1 permanece porque no cambia el repertorio de formas. F2 también: probar aquí que las ocho amplitudes de (5.12) son no nulas no establece esa propiedad para todas las filas ni valida generalmente (PS′).

   La enmienda conserva expresamente la ausencia de evidencia para (PH), la ausencia de promoción y la prohibición de inferir autorización para fases posteriores.

**Reparaciones obligatorias: ninguna.** Las aclaraciones propuestas precisan el alcance documental y registran el signo inconsistente de (5.13); no cambian la derivación ni los dictámenes.