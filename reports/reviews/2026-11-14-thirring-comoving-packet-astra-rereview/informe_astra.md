<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.169.0)
inicio: 2026-11-14T18:29:33Z  fin: 2026-11-14T18:30:07Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-comoving-packet.md ; último commit observado: 583868e ; sha256 de la copia enviada 79cb3cfff5a464b40b1f67dc6d9495afdb258b05da920adf01754c5e5a2c9cf4
documento: /home/adnac/qca-causal-cones/reports/reviews/2026-11-14-thirring-comoving-packet-astra/informe_astra.md ; último commit observado: 091f3b8 ; sha256 de la copia enviada 905bb830f6f8b74ef2695781d296563de5c57eaf093c14f9cbc12c263376703a
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_comoving_packet.py ; último commit observado: 2685635 ; sha256 de la copia enviada a72db65cf837921d2448315babce39ff93d9ac8077ab9f226abf77f039a9ac55
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-comoving-packet.txt ; último commit observado: e81a719 ; sha256 de la copia enviada 0861bf7273608a3c392eb3589b7d0357cf7326fc8dc80eae99190c7d2b5eff18
entrada_astra.txt sha256 923d856bc719a21e5840eb0290456b92a71f1a9fbc468793c93093bd429f0d11
respuesta sha256 fa3204953e66e368723eafbe33c793afd65e4a713e16c52b8ecebfe0a77e7c16
-->

**Dictamen global: PASS para esta re-revisión acotada. R1 y R2 quedan resueltas. No hay reparaciones obligatorias.**

Revisión mediante lectura de los documentos suministrados y derivación manual, sin ejecutar el verificador ni consultar fuentes externas. Mantengo los bloques previamente aprobados fuera del alcance, salvo las aclaraciones incorporadas.

1. **R1 — PASS.**

   A2 distingue correctamente los tres niveles. Cita la identidad como «rational identity, where \(z^2r^2\ne1\)»; restringe \(\Delta=\cos\chi\) a «wherever the quotient is defined»; y separa:
   > «Pointwise […] iff \(z^2=-1\) or \(r=1\); it vanishes for the whole family iff \(z^2=-1\).»

   Esto se sigue directamente del numerador \((z^2+1)(r^2-1)\), excluidos los polos. El paréntesis «alpha != 0, i.e. r != 1» es correcto en el dominio físico utilizado: \(r>0\) y \(z=e^{-i\chi}\ne0\). No debe interpretarse como una equivalencia para cualquier \(z\) complejo, incluido cero; la identidad racional sí tiene ese alcance algebraico más amplio.

   A5 recoge ambas excepciones y el dominio:
   > «for r != 1 […] iff […] chi = pi/2 mod pi; at r = 1, V = P and P V = I for every chi with defined denominators».

   Además, concreta «The declared code has r_co != 1 and chi = pi/2». Como comprobación directa, sustituir \(r=1\), con \(z^2\ne1\), da \(\alpha=0,\beta=1\): \(V=P\), \(PV=I\), mientras que el cociente original de \(\Delta\) queda indeterminado. La reparación es coherente.

2. **R2 — PASS.**

   «50 exact, 2 numerical positivity checks» describe correctamente el recuento suministrado. Las dos pruebas identificadas en `check_C` aplican explícitamente `sp.N(..., 30) > 0`; llamarlas mediante una función denominada `exact` no cambia su naturaleza. Las conversiones numéricas adicionales de `DIAG` son valores informativos, no nuevas pruebas del recuento.

   El argumento manual de la Sec. 6 es exacto y suficiente:
   \[
   r_{\rm co}=\frac{\sqrt{10}+3}{\sqrt2+1}>1,
   \quad \beta=\frac{2r_{\rm co}}{1+r_{\rm co}^2}>0,
   \quad \operatorname{Im}\alpha=\frac{r_{\rm co}^2-1}{r_{\rm co}^2+1}>0.
   \]
   Por tanto, ambos coeficientes son no nulos y \(2|\alpha\beta|>0\). Directamente, esa concurrencia también es
   \[
   \frac{4r_{\rm co}(r_{\rm co}^2-1)}{(1+r_{\rm co}^2)^2}>0.
   \]

   La salida histórica y el generador conservan «52/52 exact». El informe corregido rectifica expresamente esa etiqueta y declara que el verificador no cambió; conservar ese registro no deja pendiente R2.

3. **ACLARACIONES Y EDICIONES — PASS.**

   El encabezado reproduce fielmente las cuatro aclaraciones: el factor cinco afecta al parámetro temporal; incorpora \(p\ne n\pi/2\); vincula \(r_{\rm co}\) con geometría entrante **y** orden declarado; y reconoce el signo común de las cuatro columnas al ordenar por posición.

   Las distancias proporcionales a \(\mu\) se entienden como separación mínima de ese orden respecto del conjunto degenerado; los demás puntos periódicos permanecen lejos. La cota de denominadores escalados \(\ge\sqrt2\) coincide con la aclaración anterior. No detecto errores nuevos introducidos por estas ediciones.

**OPEN:** siguen abiertas las cuestiones físicas y bibliográficas previamente delimitadas, incluida la simulabilidad física. Este PASS cierra las reparaciones textuales revisadas; no constituye una promoción del resultado.