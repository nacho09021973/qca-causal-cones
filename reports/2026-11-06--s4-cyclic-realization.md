# Realización s=4 con simetría cíclica y soporte tetraédrico

2026-11-06. Codex (OpenAI). **PRELIMINARY, comprobación de autor**.

[Revisión ciega de Grok](reviews/2026-11-09-s4-cyclic-realization-grok/informe_grok.md)
(2026-11-09, grok-4.7, herramientas 97292a9, texto en 170910b): «se sostiene»,
sin objeciones; rederiva unitariedad, simetrías (incluido el sentido del giro),
nodos, irreducibilidad, geometría y el argumento local; inspecciona el script
sin ejecutarlo; no leyó 1708.00826. Una ronda; informe sin editar.
Base Git `b434547432647ca72110d4f7b6c78583d70f27c9`; cambios documentales
anteriores conservados. Autorización: «realizamos s=4 a ver que ocurre?».
Contrato: `theory/S4_CYCLIC_REALIZATION_ATTEMPT.md`, SHA256
`c065cb8c91c0945e09aa6267d5933f47ab8cc5069d696fb89818826fb1734330`.
Registrado antes del verificador a las 07:42:25 UTC; ejecución terminada
antes de las 07:43:33 UTC. Candidata advertida durante el razonamiento
previo, como declara el contrato; sin prerregistro Git.

## 1. Resultado y alcance

**REALIZED_WITH_ACTUAL_SUPPORT.** Una realización exacta de dimensión
interna cuatro, unitaria de alcance finito, irreducible en el sentido de
conmutante común escalar, tiene dos dobletes nodales en k=0, con fases
±pi/4, y dos conos isotrópicos hasta primer orden con cP=cQ=1/3.
Satisface D2, C y una covariancia espacial cíclica exacta.

El soporte permitido se fijó en N3={±1}^3/sqrt(3), pero cuatro coeficientes
se anulan. El soporte REAL es

    F={(-1,-1,-1), (-1,1,1), (1,-1,1), (1,1,-1)}/sqrt(3).

Por tanto esto NO resuelve la variante que exige ocho coeficientes no
nulos o hull cúbico exacto. No se cambió la normalización después del
cálculo. La red generada sigue siendo la de triples enteros de igual
paridad, escalada por 1/sqrt(3): todos los pasos pertenecen a ella y tres
generadores tienen determinante de módulo cuatro, su índice en Z^3.

## 2. Constructor y unitariedad exacta

Sean sigma_i y tau_i las Pauli de los dos factores internos, y

    G_i = sigma_i tensor tau_i,
    n = (1,1,1)/sqrt(3),
    N = I tensor (n.tau),
    W = (I4-iN)/sqrt(2),
    U(k) = W product_i exp(-i k_i G_i/sqrt(3)).

Cada G_i es una involución hermítica. Para i distinto de j, las dos
anticomutaciones Pauli se compensan: los G_i conmutan. Además
G_x G_y G_z=-I4. Sus proyectores conjuntos son

    E_h = product_i (I4+h_i G_i)/2.

E_h=0 si h_x h_y h_z=+1. Los otros cuatro son proyectores ortogonales de
rango uno que suman I4. Así A_h=W E_h y

    U(k)=sum_{h_x h_y h_z=-1} A_h exp(-i k.h/sqrt(3)).

Esta descomposición prueba unitariedad para todo k por ortogonalidad de
los E_h y unitariedad de W. El verificador comprueba además las dos
convoluciones Laurent U†U y UU† en todos sus desplazamientos posibles.

## 3. Simetrías exactas

Se mantienen R_j=sigma_j tensor I y V=sigma_y tensor tau_y, C=VK.
R_j cambia el signo de los G_i con i distinto de j y conmuta con W;
por tanto implementa los semigiros cartesianos. C conserva G_i y W como
operadores antiunitarios, y coeficiente a coeficiente V A_h* V†=A_h.
Esto equivale a V U(k)* V†=U(-k), no a una identidad con adjuntos.

Sea t=(I-i(sigma_x+sigma_y+sigma_z))/2 y S=t tensor t.
La conjugación por t cicla las Pauli x->y->z->x; S conserva N y W y
cicla G_i. Como los tres factores conmutan, el cambio de orden no altera
el producto. Se obtiene exactamente

    S U(kx,ky,kz) S† = U(kz,kx,ky).

D2 y este giro generan el grupo tetraédrico propio, que actúa transitivamente
en F. S³=I4; las R_j constituyen la representación proyectiva fijada.
El verificador comprueba también S R_i S†=R_{i+1} y compatibilidad con C.

## 4. Nodos, conos y segunda vía

P=(I4+N)/2 y Q=(I4-N)/2 son de rango dos, con
WP=e^(-i*pi/4)P y WQ=e^(i*pi/4)Q. Las fases son distintas.
Para J_i=iW†partial_i U(0)=G_i/sqrt(3),

    P J_i P = (sigma_i tensor I)P/3,
    Q J_i Q = -(sigma_i tensor I)Q/3.

Los términos efectivos nodales son por tanto ±(q.sigma)/3, sin inclinación.
Su polinomio característico es lambda²-|q|²/9. Son dos cruces cónicos
tridimensionales no degenerados, con igual magnitud de velocidad 1/3;
no se afirma isotropía a todos los órdenes en k.

Segunda vía exacta: en cada eje, diagonalizando sigma_i con signo eps,
queda un bloque SU(2) de determinante uno, cuya semitraza es

    f(x)=[cos(x)-eps sin(x)/sqrt(3)]/sqrt(2), x=k_i/sqrt(3).

Sus eigenfases son ±acos(f). Sus derivadas físicas en el origen son
±eps/3, coincidentes con las compresiones. Se comprobaron por separado
los tres ejes y ambos signos. No se usa un ajuste numérico.

## 5. Irreducibilidad y geometría

Si X conmuta con todos los A_h, conmuta con W=sum A_h y, por tanto,
con E_h=W†A_h. En la base conjunta de G_i, X es diagonal. Cada tau_i
lleva un estado conjunto a otro cambiando los dos signos G_j con j!=i;
los tres tau_i conectan los otros tres estados. Todos sus coeficientes en
n.tau son no nulos. Conmutar además con W obliga a que las cuatro
entradas diagonales de X sean iguales. No son dos bloques independientes
en una base interna fija. El sistema lineal directo de conmutación con
los cuatro A_h tiene rango 15 sobre las 16 entradas complejas de X.

C_micro=conv(F) es un tetraedro regular centrado en el origen. Sus vértices
v tienen norma uno y los productos entre vértices distintos valen -1/3.
La faceta opuesta a v tiene normal exterior -v y distancia 1/3 al origen.
Así r_in=1/3 y la función soporte es h_C(u)=max_{v en F} u.v.
La máxima longitud de paso es uno. La coincidencia cP=cQ=r_in pertenece
solo a esta realización; no se ha calculado el cuerpo estricto asintótico,
la máxima velocidad de grupo ni una ley universal de saturación.

## 6. Protección relativa, no selección

Para una perturbación que conserve exactamente R_j, C y S, D2 obliga
a W'=I tensor w'. Conservar S hace que w' conmute con t; mientras sus
dos eigenvalores sigan separados, su eje es n (hasta intercambio de etiquetas).
La forma local D2+C es J_i=sigma_i tensor(v_i.tau). La covariancia
cíclica exige v_{i+1}=rho v_i. Como rho n=n, los tres productos v_i.n
coinciden. Las compresiones en P y Q son opuestas y su métrica es
isotrópica. Este es un argumento local de autor, no una clasificación de
todas las perturbaciones Laurent admisibles.

En el punto construido esos productos físicos son no nulos; por continuidad
la propiedad persiste en una vecindad dentro de esa clase de simetrías con
dobletes separados. La igualdad no se impuso como condición de admisión
de las pendientes. No se demuestra selección de esas simetrías ni
universalidad entre pares independientes. El valor 1/3 es del constructor
y de las unidades fijadas, no una predicción del valor físico de c.

## 7. Evidencia y cierre

Comando: `python3 -B scripts/verify_s4_cyclic_realization.py`.
SymPy 1.14.0, salida 0, **143/143 comprobaciones exactas PASS**.
Registro: `reports/2026-11-06--s4-cyclic-realization-verifier.txt`.
Script SHA256:
`9a13907240311d26e8db7bc356b9826efd63f0a65190182404a819461ba19224`.

Fuente primaria de comparación leída: `biblioteca/1708.00826v2.pdf` p.2,
Def.1 y Ec.(4), covariancia por representación. Su convención exige
coeficientes no nulos en S+ y sus inversos. Aquí F no contiene sus
inversos: no se declara pertenencia a esa clase por usar la palabra
isotropía. Nuestra afirmación es la identidad explícita de covariancia
y la isotropía del término lineal verificadas arriba. No se hizo una
búsqueda de novedad de este constructor.

El intento termina con esta realización de soporte real tetraédrico.
La variante de ocho saltos no nulos queda OPEN, no excluida. La línea
de selección permanece aparcada. Sin revisión externa, promoción,
commit ni push; los controles de autor no son revisión independiente.

## Visualización posterior autorizada

A petición del usuario, `scripts/plot_s4_cyclic_realization.py` genera
el soporte real y cortes de las bandas mediante diagonalización numérica
del constructor. Figuras, datos y procedencia en
[`figures/s4_cyclic/README.md`](figures/s4_cyclic/README.md).
Se muestran dos cruces con pendiente local 1/3 y diferencias direccionales
a momento finito; no se interpreta la semiseparación/r como velocidad de
grupo. Sin nuevo modelo, promoción ni afirmación sobre propagación temporal.
