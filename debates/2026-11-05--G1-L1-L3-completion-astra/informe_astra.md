<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.1-sol, esfuerzo: high, vía: codex exec sellado (codex-cli 0.166.0)
inicio: 2026-11-05T16:00:45Z  fin: 2026-11-05T16:02:17Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--substrate-saturation-phase0-G1-trace.md ; último commit observado: d60eaba ; sha256 de la copia enviada 33826163fba95df8aed75724594ebea680b425c868dc670e5d77c54bee87276c
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
entrada_astra.txt sha256 fab5ccbed7db2730eb1f2107b56e3221950ebcad68b14655245b4edd6e229f5a
respuesta sha256 bdd1c30fb04e1a9873214aa88bfe64853bb1db0a4e25b4b5aa89ed4b7dc2d16f
-->

**PASS — para las identidades, la pertenencia literal y los generadores de L1–L3, mediante revisión estática.** No he ejecutado el programa. Este dictamen no ratifica un PASS histórico de ejecución, no evalúa toda la fase 0 y no cierra G1-a/b/c.

La derivación siguiente usa las definiciones originales de `published_symbol`, `rotation_product`, `fourier_support` y `hull_geometry`, junto con el contrato; no presupone las conclusiones de la traza.

### 1. Correspondencia entre símbolos

Escribamos, como en el constructor,
\[
c_j=(z_j+z_j^{-1})/2,\qquad s_j=(z_j-z_j^{-1})/(2i).
\]
Cada factor de `rotation_product` satisface exactamente
\[
z_j\frac{I-r_j\sigma_j}{2}
+z_j^{-1}\frac{I+r_j\sigma_j}{2}
=c_jI-i r_js_j\sigma_j.
\]

Usando \(\sigma_a\sigma_b=\delta_{ab}I+i\epsilon_{abc}\sigma_c\):

- **L1, \(d=1\):** el eje de moneda es \(\sigma_z\), y el único factor es
  \[
  c_xI-is_x\sigma_z,
  \]
  exactamente `published_symbol(1,…)`. El eje de moneda no cambia que exista una sola dirección espacial.

- **L2, \(d=2\):**
  \[
  (c_xI-is_x\sigma_x)(c_yI-is_y\sigma_y)
  =c_xc_yI-i\bigl(
  s_xc_y\sigma_x+c_xs_y\sigma_y+s_xs_y\sigma_z
  \bigr),
  \]
  que coincide con las tres componentes publicadas en el código.

- **L3, \(d=3\), \(\chi=\pm1\):** el producto original es
  \[
  (c_xI-is_x\sigma_x)
  (c_yI+i\chi s_y\sigma_y)
  (c_zI-is_z\sigma_z).
  \]
  Su parte escalar es
  \[
  c_xc_yc_z+\chi s_xs_ys_z,
  \]
  y el vector que multiplica a \(-i\boldsymbol{\sigma}\) es
  \[
  \begin{pmatrix}
  s_xc_yc_z-\chi c_xs_ys_z\\
  -\chi c_xs_yc_z-s_xc_ys_z\\
  c_xc_ys_z-\chi s_xs_yc_z
  \end{pmatrix}.
  \]
  Coincide componente por componente con `published_symbol(3,chi,…)`.

En dimensiones 1 y 2, `chirality` no interviene en ninguna de las dos funciones. Por tanto, emplear \(1\), como afirma la traza para L1/L2, o \(0\), como hace `run()`, produce los mismos símbolos.

**Variantes B.** La transposición exige invertir el orden:
\[
(R_xR_y)^T=R_y^TR_x^T,\qquad
(R_xR_yR_z)^T=R_z^TR_y^TR_x^T.
\]
Además, \(\sigma_x^T=\sigma_x\), \(\sigma_z^T=\sigma_z\) y
\(\sigma_y^T=-\sigma_y\). Así, B sigue siendo literalmente un producto de los factores transpuestos, con el signo de moneda de \(y\) invertido y el orden revertido. No basta con invertir ese signo manteniendo el orden original.

El bucle de `run()` especifica exactamente siete casos: uno en \(d=1\), dos en \(d=2\) y cuatro en \(d=3\). Las identidades anteriores cubren todos ellos.

### 2. Clase producto, desplazamientos y soporte

Los coeficientes
\[
P_j^\pm=(I\mp r_j\sigma_j)/2
\]
son proyectores hermíticos complementarios de rango uno. Cada factor contiene exactamente dos monomios, \(z_j\) y \(z_j^{-1}\), por lo que cumple literalmente la cláusula de desplazamientos antipodales del contrato.

Hay una precisión de convención: `fourier_support` asigna al monomio
\(z_1^{\varepsilon_1}\cdots z_d^{\varepsilon_d}\) el desplazamiento
\(-(\varepsilon_1,\ldots,\varepsilon_d)\). Por tanto, el coeficiente de \(z_j\) corresponde a \(-e_j\). Esto no altera el par \(\{\pm e_j\}\) ni los generadores reducidos, definidos salvo signo.

La ausencia de patrones nulos puede demostrarse sin usar la aserción `active support`. El coeficiente de cada patrón es un producto de proyectores de rango uno sobre ejes de Bloch consecutivos ortogonales. Para dos estados de esos ejes,
\[
|\langle u_j,u_{j+1}\rangle|^2
=\frac{1+\boldsymbol q_j\cdot\boldsymbol q_{j+1}}2
=\frac12.
\]
En consecuencia, para cualquier coeficiente de patrón \(A\),
\[
\operatorname{tr}(A^\dagger A)=2^{-(d-1)}>0.
\]
En \(d=1\) vale \(1\). La transposición conserva esta norma y la no nulidad.

Cada patrón tiene un vector de exponentes distinto. No existen coincidencias ni cancelaciones entre patrones. Queda derivado, independientemente de la comprobación programada,
\[
F=\{-1,1\}^{d},\qquad
\operatorname{conv}F=\sum_{j=1}^{d}[-e_j,e_j].
\]

### 3. Generadores y alcance documental

`hull_geometry` normaliza los desplazamientos dividiéndolos por \(\sqrt d\). Así, los generadores son:

| Fila | Generadores normalizados |
|---|---|
| L1 | \(e_1\) |
| L2 | \(e_1/\sqrt2,\ e_2/\sqrt2\) |
| L3 | \(e_1/\sqrt3,\ e_2/\sqrt3,\ e_3/\sqrt3\) |

Son \(d\) direcciones ortogonales, linealmente independientes y de igual longitud; no hay direcciones paralelas que fusionar. Esto respalda las afirmaciones matemáticas de L1–L3 y su resumen.

**Reparaciones obligatorias: ninguna para este alcance matemático.** La llamada externa citada a `verify_c_across_lattices_gate.py` y el PASS histórico de CS no quedan comprobados con los adjuntos. No los he utilizado como premisas ni presento esta revisión estática como evidencia de ejecución.