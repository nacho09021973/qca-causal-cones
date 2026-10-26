# W7 cinemática de espín 2 — reconstrucción tipográfica

Fecha: 2026-10-26. Autor: Codex. Base: `8194b17`.
Autorización: «ADELANTE» al bloque g de la hoja del 22 de octubre.
No es una revisión independiente ni una construcción de gravitón físico.

## Reconstrucción y certificado

Se restauraron manualmente las barras invertidas del contrato
`theory/W7_SPIN2_KINEMATICS_GATE.md` y del informe
`reports/2026-09-30--w7-spin2-kinematics.md`.
Ambos pasan `scripts/check_reconstruction.py` contra `2d144d9`:
fuera de las cabeceras solo cambian barras invertidas, sin alterar palabras,
coeficientes o criterios. No se modificó código.

Se leyó y ejecutó `scripts/verify_w7_spin2_kinematics.py`. Sus cuatro bloques
de comprobaciones pasan: descomposición, rangos de proyectores, visibilidad
métrica y cierre de las matrices simétricas sin traza bajo rotación infinitesimal.
No comprueba una dinámica microscópica, restricciones TT ni simetría rotacional
continua del QCA completo. La irreducibilidad no tiene una aserción específica
en ese certificado; se contrasta manualmente abajo.

## Segunda formulación por bases y núcleo

Una matriz antisimétrica tiene tres entradas libres por encima de la diagonal.
Una simétrica tiene seis; exigir traza cero elimina una y deja cinco.
La identidad da la dirección escalar restante. Una base explícita del sector
simétrico sin traza consta de las diagonales `(1,-1,0)` y `(1,1,-2)` y las
tres matrices con entradas uno en cada par simétrico 12, 13 y 23.
Esto reproduce `9 = 3 + 1 + 5` sin el algoritmo de rango del certificado.

Los proyectores `P_asym(A) = (A-A^T)/2`, `P_tr(A) = tr(A) I/3` y
`P_STF(A) = (A+A^T)/2 - tr(A) I/3` suman identidad y sus imágenes no se
intersectan salvo en cero. La ecuación `delta h = A + A^T` anula exactamente
la parte antisimétrica y recupera dos veces la parte simétrica. Por tanto
el núcleo métrico tiene dimensión tres y la imagen dimensión seis.
Esto es álgebra del mapa declarado; usar toda esa imagen como controles de
W6 conserva la condición g no nulo del mapa tetrádico. No se vuelve a derivar
E desde las puertas microscópicas en este bloque.

## Representación global y su alcance

El producto `R Q R^T` es simétrico y tiene la misma traza para R ortogonal.
Derivar esta transformación en identidad da el conmutador del informe:
su transpuesta coincide consigo mismo y su traza es cero.

Como contraste de la etiqueta espín 2, el polinomio `p_Q(x) = x^T Q x`
es homogéneo de grado dos y su laplaciano es `2 tr(Q)`. Las cinco matrices
anteriores corresponden a los polinomios armónicos de grado dos, con la
misma acción por rotaciones. Se puede comprobar también irreducibilidad
sin inferirla solo de la dimensión: cualquier subespacio invariante no nulo
contiene una Q diagonalizada por una rotación. Al ser no nula y sin traza,
dos de sus valores propios difieren. Restar su conjugada por una permutación
realizada con una rotación de permutación y signos produce una diagonal
proporcional a `(1,-1,0)`. Sus permutaciones generan las dos direcciones
diagonales; rotaciones de pi/4 en los planos generan las tres matrices
simétricas no diagonales. El subespacio contiene así las cinco direcciones.

Este contraste identifica la representación abstracta de SO(3). No prueba
que el conjunto de saltos, la familia de puertas o la dinámica del QCA tenga
esa simetría continua como simetría física. Tampoco convierte el núcleo
métrico lineal en una simetría gauge local de la evolución completa.

## Cierre dinámico: condición, no derivación microscópica

Si un mismo operador lineal K actúa sobre cada entrada de A, entonces
conmuta con transposición, traza y los tres proyectores anteriores. Como
los coeficientes del mapa lineal de controles a A son constantes, un operador
idéntico sobre los nueve controles también conmuta con ese cambio de variables.
Esto comprueba el enunciado condicional K4 del contrato.

Aplicar puertas idénticas a cada especie no deriva por sí solo una ecuación
cerrada y lineal para sus expectativas de Z en estados generales: la evolución
puede implicar otras componentes o correlaciones. El certificado W7 no contiene
ese paso. Por ello la sección 4 del informe se lee bajo la hipótesis explícita
de operador lineal común; no como prueba de cierre microscópico incondicional.
Siguen en vigor las precisiones sobre amplitudes de defecto frente a
expectativas del control registradas en `2026-10-26--w4-spectrum-reconstruction.md`.

## Dos polarizaciones: solo un control algebraico condicional

Para un momento no nulo orientado sobre el tercer eje, imponer transversalidad
a Q exige `Q13 = Q23 = Q33 = 0`. La traza cero deja `Q22 = -Q11`, y quedan
libres Q11 y Q12: las dos formas plus y cruz. En momento cero la condición
transversa no elimina componentes. Esto comprueba el recuento que se obtendría
si se derivaran las restricciones; no demuestra que el modelo las imponga,
elimine otros sectores o propague dos modos físicos. No se ejecuta el gate W8.

## Validación y cierre

```sh
python3 -B scripts/check_reconstruction.py theory/W7_SPIN2_KINEMATICS_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-30--w7-spin2-kinematics.md
python3 -B scripts/verify_w7_spin2_kinematics.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción 2/2 PASS y certificado cuatro PASS. Los contrastes manuales
quedan trazados arriba; no se ejecutó código científico temporal ni un nuevo
barrido completo de certificados, al no cambiar código.

Avisos globales: de 165 a 119, al retirar 46 delimitadores desnudos (14 + 32).
No quedan avisos en el par reconstruido ni en este registro; el detector
global sigue saliendo con código 1 por la cola restante. El diff pasa la
comprobación de espacios.

Permanece `SPIN2_KINEMATIC_SECTOR_PASS / TT_GAUGE_CONSTRAINTS_OPEN`, con
cierre dinámico condicionado como arriba. No se acredita gravitón físico,
no se promueve evidencia y W1–W12 sigue cerrado por contrato. El siguiente
bloque documental es el puente CJWW exacto de grafo dinámico (bloque h).
