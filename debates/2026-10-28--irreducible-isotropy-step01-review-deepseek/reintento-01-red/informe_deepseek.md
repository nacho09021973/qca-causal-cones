<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 eb2449a02ea38c12b4aedae96ece00b1530034a1aee85f08fe872431076aff72
inicio: 2026-10-29T07:35:30Z  fin: 2026-10-29T07:52:14Z
documento: /home/ignac/qca-causal-cones/theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md ; último commit observado: 88b07ed ; sha256 de la copia enviada bb12375faff7b16fcd5e40c85995dc9fe8f374f6d26b51c60819fa94bba176a6
documento: /home/ignac/qca-causal-cones/reports/2026-10-28--irreducible-isotropy-step01.md ; último commit observado: 88b07ed ; sha256 de la copia enviada d251ba224f913085215bef4f0077701af51baf1a1e9b7384230c784f6177748c
documento: /home/ignac/qca-causal-cones/scripts/verify_irreducible_isotropy_step01.py ; último commit observado: 88b07ed ; sha256 de la copia enviada d414b446d476c646b1955c6c1260c2e818ffe95b5a7d302fd0ab0e4fefb03b94
documento: /home/ignac/qca-causal-cones/scripts/cert_Aa_s4_counterexample.py ; último commit observado: 1dae941 ; sha256 de la copia enviada 635a24706df763efda1458e6742a1c43763f6a7ff7c22ddc7c6637f78ea5787a
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
entrada_deepseek.txt sha256 36df225f56efae36b45556a6f232ac52642e982369cc56d5c21bd1fdeb24e910
respuesta sha256 86f0f5b21ae374c21dc9c662da4f3aae26ca1cc9ac56172d9c36c398a6195058
-->

## Veredicto global

**ACCEPT_WITH_REPAIRS.** El resultado principal —que las clases T3, O3 y O4 declaradas son vacías— es matemáticamente plausible y el diseño del certificado es, en lo esencial, correcto. No veo un error que invalide esa conclusión. Sí hay una **sobreafirmación de cobertura** que debe repararse: la representación lineal irreducible de dimensión 2 de \(2O\) (la `E` lineal) no está cubierta por el control de espín 1/2, y el informe la incluye implícitamente en su afirmación de cobertura total.

No he podido ejecutar el código ni verificar los 31/31 checks exactos; eso queda **NO VERIFICADO por ejecución**.

---

## 1. Corrección del planteamiento

**Veredicto: ACCEPT.**

La covarianza usada es la correcta y coincide con la carta:

\[
T_{gh}=R_g T_h R_g^\dagger
\]

es equivalente a

\[
U(gk)=R_g U(k)R_g^\dagger,
\]

pues

\[
U(gk)=\sum_h e^{-i(gk)\cdot h}T_h
=\sum_{\tilde h} e^{-ik\cdot \tilde h}T_{g\tilde h},
\]

mientras

\[
R_gU(k)R_g^\dagger
=\sum_{\tilde h} e^{-ik\cdot \tilde h} R_gT_{\tilde h}R_g^\dagger.
\]

La reducción a un coeficiente por órbita restringido al conmutante del estabilizador del vértice es correcta. Si \(g\) fija \(h\), entonces

\[
T_h=T_{gh}=R_g T_h R_g^\dagger,
\]

es decir

\[
[R_g,T_h]=0.
\]

La restricción al estabilizador es exacta y no hay una fase proyectiva adicional.

**Fase proyectiva explícita.**  
Si \(R\) es una representación proyectiva, la acción adjunta

\[
g\mapsto \operatorname{Ad}_{R_g}
\]

es un homomorfismo genuino: las fases de \(R_g\) se cancelan en \(R_g(\cdot)R_g^\dagger\). Por tanto, la covarianza exacta de la carta no deja libertad para pedir

\[
R_g T_h R_g^\dagger=\lambda_g T_h
\]

con \(\lambda_g\neq 1\). Para estabilizador, \(T_h=T_{gh}\) impone \(\lambda_g=1\).

Concretamente:

- En espín 1/2, un levantamiento de una rotación triple alrededor del vértice es conjugable a

\[
\operatorname{diag}(e^{i\pi/3}, e^{-i\pi/3}).
\]

Su conmutante exacto es diagonal. Si se permitiera fase, habría soluciones con entradas no diagonales y \(\lambda=e^{2\pi i/3}\), pero eso correspondería a otra convención de covarianza, no a la de la carta.

- En espín 3/2, la restricción al levantamiento del estabilizador es conjugable a

\[
\operatorname{diag}(e^{i\pi/3}, e^{-i\pi/3}, -1, -1).
\]

El conmutante exacto es por bloques, no diagonal genérico. También aquí podrían aparecer soluciones “salvo carácter” si se modificara la ecuación de covarianza, pero no son admisibles bajo la covarianza declarada.

Por tanto, no falta ninguna solución por no permitir fases proyectivas extra.

---

## 2. Identidades de unitariedad

**Veredicto: ACCEPT.**

Las identidades usadas son correctas. Para

\[
U(k)=\sum_h e^{-ik\cdot h}T_h,
\]

se tiene

\[
U(k)^\dagger U(k)
=\sum_{h,h'} e^{ik\cdot(h-h')} T_h^\dagger T_{h'}
=\sum_{\ell} e^{-ik\cdot \ell}
\left(\sum_{h'-h=\ell} T_h^\dagger T_{h'}\right).
\]

Las exponenciales \(e^{-ik\cdot \ell}\) con \(\ell\in\{-2,0,2\}^3\) son caracteres linealmente independientes sobre \(k\). Por tanto,

\[
\sum_{h'-h=\ell} T_h^\dagger T_{h'}=\delta_{\ell 0}I
\]

es una condición necesaria y suficiente para \(U^\dagger U=I\).

No hace falta imponer por separado \(UU^\dagger=I\), porque para matrices cuadradas finitas \(U^\dagger U=I\) ya implica que \(U^\dagger\) es inversa por ambos lados.

La división en parte real e imaginaria y una base de Gröbner igual a \([1]\) demuestra, si SymPy simplifica bien los coeficientes algebraicos, que no hay solución real; como los parámetros reales son exactamente las partes real e imaginaria de los coeficientes complejos, tampoco hay solución compleja.

No veo error aquí. Lo que no puedo verificar sin ejecutar es que SymPy no haya producido ceros espurios por simplificación de expresiones algebraicas.

---

## 3. Cobertura de representaciones irreducibles

**Veredicto: REJECT en la afirmación de cobertura; las dimensiones de las tablas son correctas.**

Las dimensiones listadas son correctas:

\[
2T:\quad 1,1,1,2,2,2,3 \qquad \sum d^2=24,
\]

\[
2O:\quad 1,1,2,2,2,3,3,4 \qquad \sum d^2=48.
\]

También es cierto que, dentro de una misma **clase central**, representaciones de igual dimensión suelen diferir en un carácter unidimensional, y la conjugación \(R_g T_h R_g^\dagger\) ve ese carácter solo como una fase que se cancela.

Pero la afirmación

> “spin 1/2, 1 y 3/2 cubren todas las \(R\) irreducibles de dimensión 2, 3 y 4 de \(2T\) y \(2O\)”

es **falsa para dimensión 2 de \(2O\)**.

En \(2O\) hay:

- dos representaciones espinoriales de dimensión 2: \(E_{1/2}\) y \(E_{5/2}\);
- una representación **lineal** de dimensión 2: \(E\), que proviene de la representación irreducible bidimensional de \(O\) y tiene carácter central \(+1\) sobre \(-I\in 2O\).

La representación de espín 1/2 restringida a \(2O\) es \(E_{1/2}\), con carácter central \(-1\) sobre \(-I\). Multiplicar por un carácter unidimensional de \(2O\) no cambia ese carácter central, porque los caracteres unidimensionales de \(2O\) son triviales sobre \(-I\). Por tanto, la \(E\) lineal **no** es equivalente a espín 1/2 multiplicado por un carácter.

El control `O2s (control)` del código usa `n=1`, es decir, espín 1/2. Por tanto cubre \(E_{1/2}\) y \(E_{5/2}\), pero no la \(E\) lineal de \(O\).

La afirmación final del informe:

> “every irreducible-\(R\) class with \(s\ge 2\) under \(T\) or \(O\) on \(N_3\) is covered by T3, O3, O4 and the two \(s=2\) controls”

es, por tanto, incorrecta. Debe corregirse para excluir, o tratar explícitamente, la clase \(O\), \(s=2\), \(R=E\) lineal.

Esto no afecta a las clases principales T3, O3, O4, porque dimensión 3 y 4 sí están cubiertas.

---

## 4. Revisión del código

**Veredicto: ACCEPT_WITH_REPAIRS.**  
No veo un error que invalide la conclusión principal, pero hay una laguna de control y una afirmación impresa falsa.

### Convención de signos \(h\leftrightarrow -h\)

No invalida. En los controles se usa

```python
T4 = {tuple(-x for x in k): v ...}
T2[tuple(-x for x in v)] = ...
```

Eso es un reetiquetado global \(T'_h=T_{-h}\). Si \(T_h\) produce un símbolo unitario, también lo produce \(T'_h\), porque corresponde a \(U(-k)\). La covarianza no se pierde, ya que \(T'_{gh}=T_{-gh}=T_{g(-h)}\). Por tanto, los controles siguen siendo válidos.

En la derivación principal de Step 1, `covariant_class` no usa esa inversión; usa directamente

\[
T_{R(u)h_0}=D(u) A D(u)^\dagger.
\]

Eso es correcto.

### Homomorfismo / antihomomorfismo

Correcto. `rotation(u)` es la representación adjunta estándar:

\[
R_{ij}(u)=\frac12 \operatorname{Tr}(\sigma_i u\sigma_j u^\dagger).
\]

Esto da

\[
R(uv)=R(u)R(v),
\]

y el código comprueba homomorfismo. La matriz `spin(u,n)` construida por potencias simétricas también es un homomorfismo. La comprobación de espín 3/2 solo se hace para \(12\times 48\) productos, no todos, pero la construcción es polinomial y define un homomorfismo global de \(SU(2)\); no es un bug.

### Construcción del conmutante

Correcta. Se resuelve

\[
D(u)X-XD(u)=0
\]

para todos los levantamientos \(u\) del estabilizador del vértice. Como \(D(u)\) es unitario, no hace falta añadir \(D(u)^\dagger X-XD(u)^\dagger\).

El uso de `sp.linsolve` sobre variables complejas y luego sustituir cada variable libre compleja por \(q_{2i}+i q_{2i+1}\) con \(q\) reales cubre todas las soluciones complejas. No veo error.

**Laguna de control:** el control positivo Q8/D2 usa `commutant=False`, por lo que no ejercita el solucionador del conmutante. Es decir, si `covariant_class(..., commutant=True)` tuviera un error que restringiera de más, el control positivo no lo detectaría. No es evidencia de error, pero es una laguna de justificación.

### Asignación de vértices por covarianza

Correcta. Para cada `v` se buscan los `u` con `R(u)*base=v` y se define

\[
T_v=D(u)AD(u)^\dagger.
\]

La comprobación

```python
assert all(is_zero(c - cands[0]) for c in cands)
```

garantiza que la asignación no depende del representante de coset. Eso es exactamente lo que se necesita.

### Generador de ecuaciones

Correcto. `unitarity_equations` agrupa por \(\ell=h'-h\) y construye

\[
\sum_{h'-h=\ell} T_h^\dagger T_{h'},
\]

restando \(I\) solo para \(\ell=0\). Eso es el sistema correcto.

### Comparaciones estructurales `==`

Hay comparaciones estructurales como

```python
R_1 * R_2 == R_3
x == 0
exprs == [1]
```

En este contexto, con matrices algebraicas exactas, es probablemente suficiente. Para robustez sería mejor comparar diferencias simplificadas con cero. No creo que invalide el certificado, pero es una mejora recomendable.

### ¿Los controles descartan un generador que dé \([1]\) siempre?

No completamente. El control positivo Q8/D2 descarta un fallo absolutamente universal “todo da \([1]\)”. La anulación sobre los paseos conocidos muestra que el generador no impone ecuaciones espurias para esos paseos. La homogeneidad sin normalización muestra que el sistema relajado es homogéneo y no unitario.

Pero no descartan un error que afecte específicamente a las clases con `commutant=True`, ni un error de Gröbner que produzca \([1]\) solo para estos sistemas algebraicos de dimensión mayor. Son controles buenos, pero no son una prueba de que el generador es correcto para T3/O3/O4.

---

## 5. Segunda vía analítica independiente

**Veredicto: NO VERIFICADO; observación parcial.**

Puedo dar una observación útil, pero no una prueba analítica completa sin hacer cálculos largos.

Para \(O\) u \(T\) con \(R\) irreducible, en \(k=0\):

\[
U(0)=R_g U(0) R_g^\dagger
\]

para todo \(g\), luego por Schur

\[
U(0)=\lambda I,\qquad |\lambda|=1.
\]

Para O3, con un coeficiente \(A=T_{h_0}\) en el conmutante del estabilizador, la suma sobre la órbita da

\[
\sum_h T_h=\frac{8}{3}(\operatorname{Tr} A)I,
\]

y la normalización da

\[
\sum_h T_h^\dagger T_h
=\frac{8}{3}\operatorname{Tr}(A^\dagger A)I
=I,
\]

por lo que

\[
\operatorname{Tr}(A^\dagger A)=\frac38.
\]

Además, de \(U(0)=\lambda I\),

\[
|\operatorname{Tr}A|=\frac38.
\]

Estas condiciones no son contradictorias por Cauchy.

Para T3 hay condiciones análogas con dos coeficientes y una traza total.

Una prueba analítica completa requeriría imponer las identidades \(\ell\neq 0\), probablemente evaluando \(U(k)\) en direcciones invariantes por el estabilizador del vértice. No es imposible, pero no es un argumento corto. No he verificado una demostración de ese tipo.

---

## 6. Alcance y conclusiones del informe

**Veredicto: ACCEPT_WITH_REPAIRS.**

Las limitaciones principales están bien declaradas:

- `EMPTY_CLASS` es vacío, no refutación ni confirmación de la hipótesis;
- \(s=1\) queda `[UNVERIFIED]`;
- no se cubren representaciones reducibles, otros grupos u otros soportes;
- no hay objeciones de Steps 2–3.

La redacción es cuidadosa en general.

El problema es la **sobreafirmación de cobertura** ya señalada. El informe dice que todas las clases \(s\ge 2\) bajo \(T\) u \(O\) están cubiertas por T3, O3, O4 y los dos controles \(s=2\). Eso es falso para la representación lineal \(E\) de dimensión 2 de \(O\). Hay que corregirlo.

---

## Reparaciones obligatorias

1. **[Error matemático / cobertura]**  
   Documento `2026-10-28--irreducible-isotropy-step01.md`, sección “Scope and limits”.  
   Corregir o matizar la frase:

   > “Since 2T and 2O have no irreducible representation of dimension above 4, every irreducible-\(R\) class with \(s\ge 2\) under \(T\) or \(O\) on \(N_3\) is covered by T3, O3, O4 and the two \(s=2\) controls.”

   Debe excluirse explícitamente la representación lineal bidimensional \(E\) de \(2O\), o añadirse un control/derivación para \(O\), \(s=2\), \(R=E\) lineal.

2. **[Error de código / redacción]**  
   `verify_irreducible_isotropy_step01.py`, cerca del mensaje:

   ```python
   print("NOTE  irreps of equal dimension above are built as (spin rep) x (1-dim "
         "character); T -> R T R^dagger sees R only up to that scalar, so spin 1/2, 1, "
         "3/2 cover every irreducible R of dimension 2, 3, 4.")
   ```

   Ese mensaje es falso para dimensión 2 de \(2O\). Debe corregirse.

3. **[Laguna de justificación]**  
   Documento `2026-10-28--irreducible-isotropy-step01.md`, sección “Controls in the certificate”.  
   Indicar que el control positivo Q8/D2 usa `commutant=False` y por tanto no valida el solucionador del conmutante. Conviene añadir un control que ejercite `commutant=True` con estabilizador no trivial, o justificar por qué la solución del conmutante es completa por inspección analítica.

4. **[Redacción / robustez]**  
   En el código, reemplazar comparaciones estructurales `==` por diferencias simplificadas iguales a cero en puntos críticos: homomorfismo de rotaciones, intertwiners y base de Gröbner. No cambia la conclusión si SymPy ya simplifica, pero evita falsos fallos o falsos positivos ante cambios de versión.

5. **[NO VERIFICADO por ejecución]**  
   Los hashes, los 31/31 checks, el tiempo de ejecución y la base de Gröbner exacta no pueden ser verificados sin ejecutar el certificado. El resultado principal queda como altamente plausible, pero no verificado por mí en esta sesión.
