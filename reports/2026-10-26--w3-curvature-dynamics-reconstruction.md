# W3 curvatura y dinámica — reconstrucción tipográfica

Fecha: 2026-10-26. Autor: Codex. Base: `9d27245`.
Autorización: «adelante» al bloque d de la hoja del 22 de octubre.
No es una revisión independiente ni una nueva ejecución del programa físico.

## Alcance y comprobador

Se restauraron manualmente las barras invertidas del contrato
`theory/W3_CURVATURE_DYNAMICS_GATE.md` y del informe
`reports/2026-09-30--w3-curvature-dynamics.md`.
Los dos pasan `scripts/check_reconstruction.py` contra `2d144d9`:
fuera de las cabeceras solo cambian barras invertidas, sin alterar palabras,
coeficientes, criterios o conclusiones. No se modificó código.

Se leyó y ejecutó `scripts/verify_w3_backreacting_tetrad.py`: sus cuatro
comprobaciones pasan. Ese script verifica la rotación de Z y álgebra de la
matriz tetrad declarada; no deriva E desde el walk ni calcula curvatura.
Su término de retroacción de segundo orden conserva la limitación de campo
medio de la revisión W3 del 22 de octubre, no el coeficiente completo de
un estado que ya se ha entrelazado.

## Contraste manual del métrico

Con las matrices E0, Z y D declaradas, el producto E0 transpuesta por ZD es

\[
E_0^TZD=
\begin{pmatrix}
z_1&0&0\\
-z_2&-z_2&0\\
z_3&z_3&z_3
\end{pmatrix}.
\]

Sumar su transpuesta reproduce exactamente la matriz simétrica que aparece
multiplicada por -2g en h. Esto comprueba cada entrada y sus signos.
Una segunda formulación parte de la identidad de Pauli: el cuadrado del
símbolo lineal es la norma al cuadrado de Ep por la identidad de coin;
la parte antisimétrica se cancela. El coeficiente cuadrático es por tanto
E transpuesta por E. En g = 0 se recupera el métrico euclídeo.

Estos son cálculos manuales sobre el tetrad ya declarado, no una nueva prueba
de que ese tetrad sea el generador efectivo completo del modelo microscópico.

## Curvatura: dos vías sobre el ejemplo

Para z1 = f(x2) y z2 = z3 = 0, el único componente contravariante perturbado
es q11 = -4g f. Invertir el métrico a primer orden da k11 = 4g f.
En la fórmula linealizada de la sección 2, el término de doble divergencia
es cero porque el componente 11 no depende de x1. El laplaciano de la traza
de k es 4g f'', y se obtiene `R^(1) = -4g f''`.

Por otra vía, una familia covariante que realiza ese mismo primer orden es

\[
ds^2=a(y)^2dx^2+dy^2+dz^2,
\qquad a(y)=\sqrt{1+4g f(y)},\qquad y=x_2,
\]

en una región con acoplamiento suficientemente pequeño para mantener el
métrico positivo. Los únicos símbolos de conexión no nulos son
`Gamma^x_xy = Gamma^x_yx = a'/a` y `Gamma^y_xx = -a a'`.
La contracción de Ricci da `R = -2 a''/a`. Expandir a como
`1 + 2g f + O(g^2)` reproduce `R = -4g f'' + O(g^2)`.
Esta familia sirve para comprobar el primer orden: no fija los términos
desconocidos de orden g al cuadrado del métrico microscópico.
Como casos límite, f constante o afín anula esta curvatura linealizada;
no se afirma que eso anule toda curvatura de órdenes superiores.

La sección 6 de `reports/2026-09-30--w4-geometry-stiffness.md` cita precisamente
esta textura y esta fórmula. Queda contrastada localmente su procedencia W3,
sin convertir el transporte del testigo discreto de W4 en una dinámica de
curvatura con límite continuo controlado. No se modificó el informe W4 ni
el registro histórico de su revisión.

## C3, C4 y límites de la retroacción

Se contrastaron los generadores declarados de W3: tanto el kick como el
transporte llevan un factor de materia. En el sector en que A y J anulan
el estado, las puertas respectivas son identidad. No hay en ese modelo
un generador adicional que actúe solo entre registros geométricos.
Esto sostiene el FAIL contractual C3; no es un no-go sobre todos los QCA.

La identidad del kick da en general la pendiente de Z como
`-2 <X_e tensor A_e>`. Escribirla como `-2 x_e a_e`, como hace el informe,
requiere separación inicial o la aproximación de campo medio indicada.
La revisión posterior de W3 ya restringe su alcance. No se interpreta el
producto de medias como una identidad para estados correlacionados.
Ninguna de estas identidades deriva una fuente conservada de estrés-energía:
el C4 FAIL se conserva. No se construye una interacción sucesora.

## Validación ejecutada y cierre

```sh
python3 -B scripts/check_reconstruction.py theory/W3_CURVATURE_DYNAMICS_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-30--w3-curvature-dynamics.md
python3 -B scripts/verify_w3_backreacting_tetrad.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción 2/2 PASS y certificado relacionado cuatro PASS. Los cálculos
de métrico y curvatura anteriores son manuales y quedan trazados aquí;
no se ejecutó código científico temporal. No se hizo un nuevo barrido completo
de certificados porque no se cambió código.

Avisos globales: de 301 a 249, al retirar los 52 delimitadores desnudos del
par (6 + 46). No quedan avisos en estos dos documentos ni en este registro.
El detector global sigue saliendo con código 1 por la cola restante;
`git diff --check` pasa.

Se mantiene `COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL`:
C1 y C2 PASS, C3 y C4 FAIL bajo el contrato declarado. No se promueve evidencia,
no se abre normalización gravitatoria y W1–W12 continúa cerrado por contrato.
El siguiente bloque documental es W4 espectro de onda larga (bloque e).
