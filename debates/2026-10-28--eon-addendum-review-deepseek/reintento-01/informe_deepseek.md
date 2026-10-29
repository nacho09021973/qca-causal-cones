<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 d3ac7954561a8be42431ed5601904840cd23cc93be2f2d6293ab3b9780fd524c
inicio: 2026-10-29T09:32:07Z  fin: 2026-10-29T09:41:18Z
documento: /home/ignac/qca-causal-cones/reports/2026-10-27--eon-projected-gaussian-reference.md ; último commit observado: 3395c1c ; sha256 de la copia enviada 9539e275b1438daab3ebe86c2b024a98420d047761a9562935e81e847d36400f
documento: /home/ignac/qca-causal-cones/debates/2026-10-28--eon-gaussian-review-deepseek/informe_deepseek.md ; último commit observado: f64d0c7 ; sha256 de la copia enviada 9f68cdc83a54266e62646b57b3f324f88706055314578210c7b6127a49671d24
documento: /home/ignac/qca-causal-cones/biblioteca/arXiv-2205.03148v4.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada c366b8a8482a762c93e534e43d6572323737df4677556b1a764e02a1389d2d02
documento: /home/ignac/qca-causal-cones/scripts/verify_eon_projected_gaussian_reference.py ; último commit observado: 5dbd843 ; sha256 de la copia enviada a12951dcfa7e61c0b5d5a13c9ef27c0ddac303b563e9af8b88bd74a2496274eb
entrada_deepseek.txt sha256 569c02cbf6ca4d1515cca00fad4f127fe85962632b0d05dfb821aad1c48f8886
respuesta sha256 7f270b7fc50a8f916c989ba5b450638bb249391f400369cd5747f14fbd67c6f4
-->

## Veredicto por reparación

### Reparación 1 — convención f/g, desigualdad y control inverse-kick

**Veredicto: PASS.**

En el texto original, *g* es “la serie de ψ” y *f* es la serie de la componente de  
`φ = D_E D_F ψ`. Con esa convención, la ecuación correcta es

\[
e^{i\theta B(z)} f(z)=\lambda g(z),
\]

o sea

\[
f(z)=\lambda e^{-i\theta B(z)}g(z).
\]

Con \(B(z)=az+b/z+c\) y \(r=|z|\), en un arco donde

\[
\operatorname{Re}(i\theta a z)\ge |\theta a|r/2,
\]

que ocupa \(1/3\) del círculo, se tiene

\[
|e^{-i\theta B(z)}|
=
\exp[\operatorname{Re}(-i\theta a z - i\theta b/z - i\theta c)]
\le
\exp[-|\theta a|r/2 + |\theta b| r^{-1}+|\theta c|].
\]

Para \(r\gg 1\), los términos \(b/z\) y \(c\) están absorbidos en el \(O(1)\). Por tanto

\[
|f(z)|\le \exp[-|\theta a|r/2+O(1)]\,|g(z)|.
\]

Es correcta.

El control inverse-kick

\[
f=e^{-i\theta(z+1/z)},\qquad g=1
\]

también es coherente:

\[
e^{i\theta(z+1/z)}f
=
e^{i\theta(z+1/z)}e^{-i\theta(z+1/z)}
=
1
=
g,
\]

con \(\lambda=1\).

**Sobre G-R1-01:** no era una refutación de la prueba. El revisor usó una convención invertida respecto a la del texto original. Bajo la convención ya fijada en el texto, la reparación es la correcta. La objeción era, como máximo, una ambigüedad/redacción.

---

## Reparaciones 2, 3 y 5

### Reparación 2 — convexidad/Jensen

**Veredicto: PASS.**

El enunciado corregido es correcto:

- Si \(f\) es holomorfa y no idénticamente nula en un anillo exterior \(R_0<|z|<\infty\), entonces \(\log|f|\) es subarmónica.
- La media circular

\[
M_f(r)=\frac1{2\pi}\int_0^{2\pi}\log|f(re^{it})|\,dt
\]

es finita, incluso si hay ceros sobre la circunferencia, porque las singularidades logarítmicas son integrables.

- \(M_f(r)\) es convexa en \(\log r\).
- Por convexidad admite una recta de apoyo

\[
M_f(r)\ge A+B\log r.
\]

Es exactamente lo que necesita la demostración.

---

### Reparación 3 — preservación de cotas gaussianas

**Veredicto: PASS.**

En volumen finito, \(D_F\) consta de un número finito de gates. Los transportes desplazan los campos eléctricos por vectores de un conjunto finito \(S\), y las monedas/mezclas fermiónicas son finitas. Para \(0<\beta'<\beta\),

\[
e^{-\beta |E+\delta|^2}
\le
C_{\delta,\beta'}
e^{-\beta'|E|^2}.
\]

Como \(S\) es finito, la cota gaussiana sobrevive. \(D_E\) solo añade fases. La versión con \(\beta/2\) del texto original es un caso particular. La reparación es suficiente.

---

### Reparación 5 — elección genérica de componente no nula y \(a\neq 0\)

**Veredicto: PASS.**

Si \(f\) no es idénticamente nula como función holomorfa en \((\mathbb C^*)^M\), el conjunto de variables \(z_{\neq e}\) para las cuales la restricción a \(z_e\) desaparece idénticamente es un conjunto analítico propio. Análogamente, \(a(z_{\neq e})\) es una suma finita de monomios de Laurent no idénticamente nula. Por tanto, existen \(z_{\neq e}\) en el toro unidad fuera de ambos ceros. La reparación es correcta y suficiente.

---

## Reparación 4 — operadores \(V\), base \(|E\rangle'\), y coeficiente \(a\)

### 4.a — ¿Basta la conmutación de los \(V\)?

**Veredicto: PASS, con reparación obligatoria de redacción/formalización.**

La conmutación de los \(V_\ell\), por sí sola, da que la órbita

\[
|E\rangle'
:=
V_1^{E_1}\cdots V_M^{E_M}|0\rangle
\]

está bien definida como acción de un grupo abeliano. Pero la ortonormalidad y la interpretación como desplazamientos puros requieren un paso adicional: el estabilizador debe ser trivial.

Ese paso se obtiene así:

- Para una configuración fermiónica fija, \(V_\ell\) no cambia la ocupación fermiónica, porque los \(V_\ell\) conmutan con los fermiones, ec. (5) del PDF.
- En el subsector gauge físico, la restricción

\[
E_{x:\eta}=-E_{x+\eta:-\eta}
\]

permite reducir los dos campos gauge por enlace a un solo entero \(E_\ell\).
- En la base eléctrica estándar, \(V_\ell\) actúa como desplazamiento de ese único entero por \(\pm 1\), multiplicado por una fase diagonal JW.
- Por tanto, \(V_\ell^{E_\ell}|0\rangle\) tiene soporte en una única configuración eléctrica estándar. Eso elimina dependencias lineales y da ortonormalidad, salvo fases.

Así, la reducción a un entero \(E_\ell\) por enlace es legítima dentro del sector físico gauge-invariante. La adenda se limita a remitir a §1; convendría que explicitara este argumento.

**Reparación obligatoria:** añadir una línea explícita que justifique la reducción de los dos campos gauge por enlace y la ausencia de estabilizador no trivial.

---

### 4.b — \(D_M\) multiplica por \(e^{i\theta B(z)}\) y fases ±1

**Veredicto: PASS.**

En la base nueva \(|E\rangle'\), cada \(V_\ell\) es exactamente un desplazamiento puro. Por tanto:

- cada plaqueta es un monomio de Laurent en los \(z_\ell\);
- la exponencial magnética exacta \(D_M\) es multiplicación por

\[
\exp[i\theta B(z)],
\]

donde \(B(z)\) es suma de monomios de plaqueta y sus inversos.

Las fases JW que dependen de \(E\) no aparecen en esta base; quedan absorbidas en la definición de \(|E\rangle'\). Por eso no rompen la multiplicación por \(B(z)\). Solo pueden aparecer signos globales ±1 fijos en cada monomio de plaqueta, provenientes de la orientación o del signo global del operador plaqueta, no fases dependientes de \(E\).

La afirmación es exacta, con la salvedad de que conviene fijar explícitamente la convención de signo de la etiqueta \(E\) frente a la base eléctrica estándar.

---

### 4.c — Las cuatro plaquetas como monomios distintos y \(a\neq 0\)

**Veredicto: PASS.**

Para \(L\ge 3\), un enlace fijo pertenece a cuatro plaquetas. En cada una de ellas, el coeficiente de \(z_e\) es un monomio de Laurent en los otros tres enlaces. Las cuatro plaquetas usan desplazamientos distintos:

- dos en el plano \(e\)-\(\nu\), una a cada lado del enlace;
- dos en el plano \(e\)-\(\kappa\), una a cada lado del enlace.

Para \(L\ge 3\), los conjuntos de enlaces “otros” son distintos. Por tanto, los monomios de Laurent son distintos y linealmente independientes como funciones en \((\mathbb C^*)^M\).

Cada monomio tiene coeficiente ±1 no nulo. La suma

\[
a(z_{\neq e})
=
\sum_{p\ni e} s_p M_p(z_{\neq e})
\]

no puede ser idénticamente nula, porque los monomios \(M_p\) son linealmente independientes y los coeficientes \(s_p\in\{\pm 1\}\) son no nulos.

Resultado: \(a\not\equiv 0\) para cualquier elección de signos fijos.

**Reparación recomendada:** incluir esta breve prueba geométrica en el texto, ya que la adenda lo afirma sin desarrollarla.

---

### 4.d — Retirar «a=4» y el recuento del certificado

**Veredicto: PASS.**

Es correcto retirar la afirmación de que las cuatro plaquetas dan \(a=4\). El certificado, tal como está visible en el Documento 4, cuenta flujos geométricos mediante `plaquette_flow` sin incorporar los signos JW/plaqueta. Por tanto, no certifica el valor real de \(a\).

La conclusión de la prueba solo necesita \(a\neq 0\), no el valor concreto \(a=4\). Así que la retirada no daña el argumento.

**NO VERIFICADO:** el detalle exacto de `plaquette_flow` está en `verify_eon_reference_state.py`, que no se incluye en esta sesión. Sin embargo, el punto central no depende de ese código: la adenda correctamente deja de apoyarse en su recuento sin signos.

---

## ¿Quedan frases del texto original que contradigan la adenda?

Sí. Aunque la adenda declara que reemplaza el texto anterior donde lo contradiga, el Documento 1 todavía conserva afirmaciones contradictorias o ambiguas:

1. **§3.B original:**  
   > «las cuatro plaquetas adyacentes dan coeficiente a=4»  
   contradice la Reparación 4, que retira ese valor.

2. **§3.B original:**  
   > «El código comprueba ese recuento en L=3,4»  
   contradice la nueva afirmación de que el certificado no certifica \(a\).

3. **§3.C original:**  
   La igualdad escrita
   \[
   g(z)=e^{i\theta B(z)} f(z)
   \]
   con “absorbiendo en g la fase lambda” es ambigua y no coincide literalmente con la convención reparada
   \[
   e^{i\theta B(z)} f(z)=\lambda g(z).
   \]

Estas frases deben editarse, no solo declararse sustituidas.

---

## Reparaciones obligatorias numeradas

1. **Editar §3.B original:** eliminar/reemplazar la frase «las cuatro plaquetas adyacentes dan a=4» por una afirmación del tipo:  
   “\(a\) es suma de cuatro monomios de Laurent distintos con coeficientes ±1, luego no idénticamente nulo para \(L\ge 3\).”

2. **Editar §3.B original:** corregir la frase que dice que el código certifica ese recuento. El certificado solo comprueba un conteo geométrico sin signos; no certifica el valor físico de \(a\).

3. **Editar §3.C original:** escribir explícitamente
   \[
   e^{i\theta B(z)} f(z)=\lambda g(z).
   \]
   y definir sin ambigüedad:
   - \(f\) = serie de Fourier de \(\varphi=D_E D_F\psi\);
   - \(g\) = serie de Fourier de \(\psi\).

4. **Formalizar la reducción de dos campos gauge por enlace a un entero \(E_\ell\):** indicar que se usa el sector físico con
   \[
   E_{x:\eta}=-E_{x+\eta:-\eta}
   \]
   y que \(V_\ell\) preserva esa restricción.

5. **Formalizar la ortonormalidad de \(|E\rangle'\):** añadir que \(V_\ell^{E_\ell}|0\rangle\) tiene soporte en una única configuración eléctrica estándar, lo que da estabilizador trivial y ortonormalidad.

6. **Añadir la breve prueba geométrica** de que las cuatro plaquetas producen monomios de Laurent distintos para \(L\ge 3\).

7. **Aclarar la convención de signo/etiqueta** entre \(|E\rangle'\) y la base eléctrica estándar, para evitar invertir \(E\) o fases globales.

---

## Veredicto global

**PASS_WITH_REPAIRS**

La adenda es matemáticamente correcta en lo esencial y las reparaciones propuestas salvan la prueba de Fourier/Jensen. No veo un error fatal demostrado en la adenda. Los problemas restantes son de redacción, formalización y de que el texto original aún contiene frases que la propia adenda contradice. Las reparaciones obligatorias numeradas deben aplicarse al texto del Documento 1.
