# Memoria de segundo orden: primeros ocho retardos

2026-11-06. PRELIMINARY, derivación y evaluación de autor, sin revisión
independiente ni promoción. Contrato OCCUPIED_MEMORY_KERNEL_GATE.md,
hash previo c6e5f522b1bd8a533fe33746a9f23f4819cd0b6d12f0cef7ea9ca0b2828cab1a.
Mismos walks s=4, a1=1/3,a2=2/3, theta=pi/4 y estado p1=p2=1/2.

## Reducción del núcleo

Quitando la fase Hartree, el operador de fuerza asociado a c_a(x) es
-i delta N_b(x)c_a(x), delta N_b=N_b-2. En el producto escalar de
traza normalizada las especies factorizaron y la dinámica libre conserva
el grado de cada operador. La correlación de dos fuerzas se reduce al
propagador de a multiplicado por la correlación conectada de densidad
de b. Si U_a(q)^r=sum_x u_a(r,x) exp(-i q.x), la contracción fermiónica
en el estado de ocupación uniforme da

    D_b(r,x)=<delta N_b(x,r) delta N_b(0,0)>
            =tr[u_b(r,x)†u_b(r,x)]/4,
    F_a,r(q)=sum_x u_a(r,x) D_b(r,x) exp(-i q.x).

La normalización del operador lineal cancela su ocupación 1/2. En r=0,
D_b(0,0)=1, de acuerdo con la varianza de los cuatro modos. Esta
reducción es a orden dos y usa evolución LIBRE entre las dos fuerzas;
no aproxima la dinámica interactuante completa por una dinámica libre.

En la notación abstracta L=L0 exp(chi H), H antihermítico,
B1 D0^j C1=P L0 H L0^(j+1) H P. La antihermiticidad da el signo
menos de la correlación de fuerzas. En matrices de respuesta, con
L c_j=sum_i U_ji c_i (traspuesta de la matriz que actúa sobre columnas
de coeficientes de operadores), el núcleo de retardo j=r-1 es

    K_a,j(q)=-F_a,r(q) U_a(q).

El orden matricial importa. El código utiliza esta convención; no se
identifica -U F con -F U. Las derivadas físicas son
partial/partial k_i=(1/sqrt3) partial/partial q_i.

## Evaluación realizada

Se calcularon u_a(r,x), F_a,r(0), K_a,r-1(0) y sus tres primeras
derivadas espaciales para r=1..8, mediante convolución Fourier de los
símbolos exactos del constructor. Aritmética numérica complex128.
Las matrices complejas completas se guardan como pares [real,imag] en
2026-11-06--occupied-memory-kernel.json; no se conservan solo normas.

| r | norma Frobenius F_1,r(0) | norma Frobenius F_2,r(0) |
|---|---:|---:|
|1|0.389439645274|0.373252673532|
|2|0.189362045772|0.122790422623|
|3|0.0821159309073|0.0484161319932|
|4|0.102707714537|0.115654425618|
|5|0.0423792293912|0.0444971167341|
|6|0.025432020370|0.00809012418848|
|7|0.0179482050501|0.00970040526394|
|8|0.00712105978025|0.00911379002927|

La memoria es no nula y no idéntica entre especies. Las normas no son
velocidades, anchuras ni signos de atracción. Tampoco decrecen de modo
monótono: no se ajusta una ley de cola a estos ocho valores.

## Controles y límites

Dos mallas de 24³ y 20³ dan diferencia máxima 2.633125101432526e-16
en F,K y sus derivadas. Para r<=8, el soporte de u está dentro de
[-8,8]³; ambos periodos exceden su anchura, sin alias espacial. Se usa
la representación BCC en coordenadas enteras con soporte de paridad
correcto, no una aproximación de una red distinta.

La normalización sum_x tr(u†u)=4 se comprueba en cada especie y retardo.
El primer retardo se calcula además directamente desde los ocho
coeficientes W producto_i(I+h_i G_i)/8, sin transformación Fourier,
y concuerda dentro de 1e-12. Estos controles validan la implementación
de la fórmula; no constituyen revisión independiente de la derivación.

La tabla y las matrices evalúan una ventana FINITA del núcleo, no lo
truncan físicamente. Falta una cota de la cola y/o convergencia controlada
de la transformada temporal, antes de evaluar una autoenergía sobre las
ramas nodales. No se extraen polos ni se afirma igualación. La
corrección de pendiente y la anchura siguen OPEN.

Salida: MEMORY_KERNEL_REDUCED_AND_EVALUATED_R1_R8 /
LONG_TIME_SELF_ENERGY_OPEN. El siguiente problema es controlar la suma
temporal del núcleo y su dependencia de frecuencia, conjuntamente con
sus derivadas; aumentar retardos por sí solo no demuestra convergencia.

Provenance: scripts/evaluate_occupied_memory_kernel.py; ejecución
/home/adnac/venvs/torch-gpu/bin/python scripts/evaluate_occupied_memory_kernel.py.
Registro completo en 2026-11-06--occupied-memory-kernel-run.txt.
Sin scripts científicos efímeros; git diff --check. No novedad acreditada.
