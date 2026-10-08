# IG-S1 — un par energía/tick exacto que falla el objetivo gravitatorio

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato y código congelados en `67fd3b1b0c6962d5d6f1b50ac114995bc03cbe6d`:
[especificación](../theory/INVERSE_GRAVITY_DRESSED_PARENT_GATE.md).

## 1. Resultado

`DRESSED_PARENT_ALGEBRA_PASS_AUTHOR_SIDE`.
`DRESSED_COMMUTING_PARENT_REJECTED_FOR_GAPLESS_PROPAGATING_TARGET`.

Se ha construido un par local `(K_E,U_E)` con energía exactamente conservada
y una referencia fundamental explícita en volumen finito. Su gap de energía
está uniformemente entre 2 y 16. La influencia espacial del tick permanece
en radio <=4 celdas para **todos** los tiempos enteros. Por tanto esta receta
no cumple el objetivo de un sector tensorial gapless con propagación z=1.

No se obtuvo el gap exacto, un vacío crítico ni gravedad. El resultado rechaza
la receta especificada, no toda energía conservada en QCA. No modifica el
tick R/T anterior, el negativo A ni el estado formal B. La ruta prioritaria
de energía conservada con referencia crítica permanece OPEN.

## 2. Fuentes y verificación ejecutada

Índice local consultado. Se releen directamente Gu–Wen,
`biblioteca/arXiv-0907.1203.pdf`, pp.15–16, ecs.48–49 y 53, para Rzz y Tx.
SHA256 `3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
Los stencils se comprueban de nuevo por solapamientos reales y Laurent.
La construcción de K_E/U_E y las pruebas siguientes son derivaciones propias;
no se atribuyen a Gu–Wen ni se trasladan sus modos L/N a este circuito.

Se ejecutó `python3 -B scripts/verify_inverse_gravity_dressed_parent.py`,
SymPy 1.14.0, aritmética exacta, salida 0. Salida íntegra en
[certificado](2026-10-08--inverse-gravity-dressed-parent-certificate.txt).
El bloque qutrit verifica identidades locales, no simula la red. La prueba
espacial usa la regla completa y los argumentos de este informe.
No hay revisión independiente ni claim de novedad.

## 3. Energía y circuito construidos conjuntamente

En el sector S=V=1 de seis qutrits por celda, fijar

`h_alpha=I-Pi_Ralpha`, `Pi_R=(I+R+R²)/3`,
`K_0=sum_alpha h_alpha`.

Los R son palabras X físicas; cada h es un proyector y todos conmutan.
D es el bloque físico de puertas T a ángulo pi/3. La regla nueva es

`F=prod_alpha [Pi_Ralpha+exp(-i) h_alpha]`,
`U_E=D F D†`, `K_E=D K_0 D†`.

Cada factor de F es unitario porque Pi y h son proyectores complementarios.
Por la conmutación, `F=exp(-iK_0)`; conjugando,

`U_E=exp(-iK_E)` y `U_E† K_E U_E=K_E`.

Esta exponencial es una identidad de un circuito finito ya especificado,
no una suposición de causalidad para una exponencial global genérica.
La inversa `D F† D†` es explícita. El bloque auxiliar verifica conservación
con un símbolo unimodular, independientemente de aproximaciones numéricas.

Los términos `D h_alpha D†` continúan siendo proyectores conmutantes.
Por eso el dressing no introduce una frustración o una interacción espectral
nueva: cambia la representación local y el estado, pero conserva el espectro.
La receta pertenece a la alternativa de núcleo común de IG-S0; no constituye
la realización crítica de su ruta E prioritaria.

## 4. Referencia fundamental y alcance del acceso

Definir

`G_0=prod_alpha Pi_Ralpha prod_(i,a) Pi_Va(i)`.

Las conmutaciones R/V permiten formar este proyector. Es no nulo: partir
del producto con X=1 en cada registro y aplicar los promedios de V. En la
base X, los V actúan como permutaciones con coeficientes positivos; el término
identidad garantiza que el promedio no es cero. R=1 se mantiene porque R
conmuta con V. La redundancia `Rxx Ryy Rzz=S` impone también S=1.

Positividad de cada h implica que el kernel de K_0 es exactamente su núcleo
común. Dentro del sector físico, G_0 es por tanto **todo** su proyector
fundamental. No se utiliza el vector de la demostración como elección de
vacío entre estados degenerados. La referencia fijada es

`G_E=D G_0 D†`, `rho_E,L=G_E/Tr G_E`.

Se tiene `K_E G_E=0`, `U_E G_E=G_E` y estacionariedad de rho_E,L.
Un excitado físico construido abajo demuestra que G_E no es todo el sector;
esta referencia no es P/Tr P.

Acceso finito por una segunda formulación: R/V generan un grupo estabilizador
abeliano de qutrits sin fases escalares no triviales, como también garantiza
su núcleo común no vacío. Su promedio es G_0. La ortogonalidad de traza de
las palabras Pauli reduce cada expectativa a pertenencia a ese grupo y su
fase. Se resuelve mediante álgebra lineal sobre F3, sin la matriz Hilbert
de dimensión 729^(L³). Una conjugación local por D añade solo las puertas
que tocan el soporte inicial y puede expandirse en una base Pauli finita.

Esto es una receta exacta de acceso a volumen finito, no una prueba del
límite termodinámico local ni de preparación eficiente del estado. No se
ejecuta una batería extensa de expectativas: los filtros siguientes ya
rechazan el candidato. R1 como referencia IR crítica no queda aprobado.

## 5. Gap: prueba entera y testigo espacial independiente

En una base simultánea de R, cada término h vale 0 o 1. Por ello K_0 tiene
energías enteras `M`, el número de R distintos de 1. No se supone que todas
las asignaciones de caracteres sean realizables en la red.

En cada vértice del sector físico, los caracteres `r_x,r_y,r_z` satisfacen
`r_x+r_y+r_z=0 mod 3`. Una única entrada no nula viola esa identidad.
Si un estado tiene energía positiva, tiene al menos un vértice con dos R
violados. Luego

`gap(K_0|physical) >=2`.

El script comprueba los 27 triples locales; el argumento global solo utiliza
la condición necesaria, sin inferir independencia entre vértices.

Por otra vía, aplicar T_x del cubo origen a cualquier estado físico con
R=1. El stencil de solapamientos da ocho vértices, cada uno con caracteres
`(0,-1,+1)`. La geometría del cubo introducida independientemente coincide
con los stencils. Son 16 R violados y T_x preserva el sector físico. Como
T_x es unitario, produce un eigenestado no nulo de energía 16. No hay alias
en los toros admitidos L>=6 múltiplo de 6. Conjugando el estado por D,

`2 <= gap(K_E|physical) <=16`, uniformemente en L.

La conjugación conserva todo el espectro, así que no puede cerrar ese gap.
Para Lambda<2, el proyector de baja energía de IG-S0 solo contiene el vacío:
la igualdad energía–tick es exacta pero su test en esa ventana es vacío de
excitaciones. No acredita modos sin masa. Este es un gap de **energía**;
no se deduce un gap uniforme de quasifases, que viven módulo 2pi.

## 6. Localidad para cualquier número de ticks

Un bloque de puertas mutuamente conmutantes solo necesita, al conjugar un
observable O, las puertas que no conmutan con O inicialmente. Las otras
pueden moverse junto a O y cancelarse por su conmutación con todo el bloque.
Así, la extensión de soporte está acotada por el diámetro de esas puertas,
independientemente del número de factores o de su ángulo.

Las puertas R tienen diámetro <=2 celdas y las T <=1 en norma infinito.
Por ello F y todas sus potencias tienen alcance <=2; D y D† <=1.
Cada término D h_R D† queda en las celdas i+[-2,2]³: K_E es local con
soporte y norma uniformes. El circuito admite las 129 capas disjuntas
declaradas, independientemente del volumen.

Además, para **todo** entero n,

`U_E^n = D F^n D†`.

La cancelación entre ticks es exacta. En consecuencia,

`supp(U_E^-n O_A U_E^n) subset A+[-4,4]³`.

Si un detector B_C está a distancia >4 celdas de A, el conmutador con el
observable evolucionado es cero para todos los tiempos. Esto vale también
en el sector físico, cualquier estado y n negativo. No es una extrapolación
desde tiempos cortos ni una estimación que crezca como 4|n|.

Puede haber influencia próxima y dinámica no escalar, pero no transporte
balístico a distancias crecientes para esta regla. El testigo de energía 16
recibe fase exp(-16i), distinta de 1, mientras el vacío queda fijo: el tick
no es escalar. No se necesita confundir falta de propagación con trivialidad.

## 7. Cierre de la receta y obligación pendiente

La construcción resuelve algebraicamente conservación, localidad estricta
y selección de referencia finita. Falla la condición de excitaciones sin
gap y de propagación del objetivo tensorial. Se cierra este intento sin
variar el ángulo, los pesos o el dressing.

El argumento de soporte se aplica a toda la receta `D F D†` con D de alcance
fijo y F un bloque de puertas locales mutuamente conmutantes: las potencias
siguen teniendo soporte fijo. No se aplica a cualquier QCA que conserve un
Hamiltoniano conmutante; un tick diferente podría, por ejemplo, transportar
sus términos. La prueba del gap depende de los proyectores y pesos fijados.

El siguiente candidato necesita un mecanismo que permita excitaciones de
energía arbitrariamente pequeña y transporte sostenido, conservando a la vez
una energía local y una referencia controlada. Conjugar este parent por más
capas de profundidad fija no resuelve ninguno de los dos fallos.
No se ha especificado todavía esa construcción crítica; permanece
`CRITICAL_CONSERVED_ENERGY_CONSTRUCTION_OPEN`. El resultado actual no autoriza
una batería IR ni un nuevo rescate del control q=3 anterior.
