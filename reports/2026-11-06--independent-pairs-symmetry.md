# Pares independientes: qué impone un intercambio interno

2026-11-06. Codex. PRELIMINARY, autocomprobación sin revisión externa
ni promoción. Usuario: «adelante» a opción 2. Base Git 74db229, con
los archivos del intento cíclico anterior todavía sin commit; no se
modifican. Contrato: theory/INDEPENDENT_PAIRS_SYMMETRY_PREFLIGHT.md,
SHA256 antes de ejecutar:
58372434ff9473275adc6e8968c560b058f6772bea92483c976eb90b4673fb0b.

## Resultado acotado

Un intercambio interno fijo no basta LOCALMENTE para igualar las
velocidades de los modos propios. Si se añade la segunda simetría
fijada, la igualdad procede de copias idénticas. Ninguna salida ofrece
la protección buscada en una nueva dinámica globalmente irreducible.

No se ha construido un QW finito ni demostrado que el término local
permitido pueda realizarse en un soporte dado. No es un contraejemplo
microscópico a una clase Laurent. Es un filtro de álgebra necesaria,
con tres condiciones fijadas de antemano y corte por resultado estándar.

## 1. Qué se entiende por independientes

Hay tres conceptos diferentes: etiquetas de una base; subespacios
conservados por U(k) para todo k; y modos propios de propagación del
problema nodal. Un intercambio de etiquetas solo implica igualdad de
dispersiones si relaciona subespacios dinámicos bien definidos. Cuando
hay mezcla, se debe diagonalizarla antes de comparar velocidades.

Usamos s=8, sigma tensor tau tensor rho: tau distingue conjugados PHS;
rho añade dos candidatos de especie. Esta ampliación de dimensión es
solo un filtro local autorizado, no un cambio de sustrato ni un nuevo
constructor. R_j=sigma_j tensor I tensor I y
C=(sigma_y tensor tau_y tensor I)K permanecen fijos.

## 2. Centros de fase distintos

Para una simetría unitaria F con F U(k) F†=U(k), necesariamente [F,W]=0,
W=U(0). Si W psi=lambda psi, entonces W F psi=lambda F psi.
F no puede intercambiar autoespacios de eigenvalores distintos. Esto
también vale para una covariancia espacial cuyo giro deje k=0 fijo.

Dos pares con conjuntos disjuntos {exp(±i theta_1)} y {exp(±i theta_2)}
no se relacionan mediante ese intercambio. No se comparan theta solo
como números reales: importan los conjuntos de fases módulo 2pi.
La antiunitaria PHS ya permite conjugación de fase, pero no relaciona
dos conjuntos disjuntos de ese modo.

El script comprueba además theta_1=pi/4, theta_2=pi/3. No se excluyen
simetrías que desplacen quasienergías, cambien marco temporal o relacionen
nodos en momentos diferentes; no pertenecen al contrato.

## 3. Centros coincidentes: intercambio insuficiente localmente

Con W=I_sigma tensor exp(-i theta tau_z) tensor I_rho, theta=pi/4,
se permite F=I_4 tensor rho_x. Las fases ±theta tienen rango cuatro:
no se presuponen dos dobletes separados antes de diagonalizar rho.

El álgebra de matrices de sabor que conmuta con rho_x es
span_C{I,rho_x}. Por ello es admisible a primer orden

    J_i=sigma_i tensor tau_z tensor B,
    B=c I+delta rho_x,  c>|delta|>0.

Son derivadas Hermíticas compatibles con D2, F y la condición PHS
V J_i* V†=J_i. En cada sector tau_z=eta, el Hamiltoniano nodal es
eta (k.sigma) tensor B. Los modos rho_x=±1 tienen velocidades
c+delta y c-delta, positivas y distintas. Ambas son isotrópicas y sin
inclinación, y cada modo tiene su conjugado PHS.

Segunda vía: la transformación de Hadamard diagonaliza B con entradas
c+delta,c-delta. Cada bloque satisface
H_±²=(c±delta)² |k|² I_2 y tiene polinomio característico
lambda²-(c±delta)²|k|². El punto racional c=1/3, delta=1/12 da
5/12 y 1/4, SOLO en las unidades locales del filtro. No son velocidades
de un QW acreditado ni se comparan con un inradio.

Así, un término de separación infinitesimal puede conservar el
intercambio en el álgebra local. Falta demostrar realizabilidad Laurent
antes de llamarlo perturbación microscópica admisible.

## 4. Añadir Z: igualdad mediante copias idénticas

La condición adicional es Z=I_4 tensor rho_z, [Z,U(k)]=0, además de F.
Expandir cualquier matriz U(k) en las cuatro Pauli de rho muestra:
conmutar con rho_x permite I,rho_x; conmutar también con rho_z
deja solo I. Por tanto U(k)=A(k) tensor I_rho, exactamente, no solo
en su término lineal. Si U es unitario y Laurent, A también lo es.
En una base agrupada por rho son dos copias idénticas de A.

Segunda lectura: conservar las etiquetas rho_z ya fuerza bloques
diag(A,D); intercambiarlos con F exige A=D. La igualdad resultante
no aporta un mecanismo entre dinámicas independientes.

Además, incluso F por sí sola, si es una simetría interna exacta para
todo k, hace que los proyectores constantes (I±F)/2 conserven U(k).
Por independencia de los modos Fourier conservan cada coeficiente
Laurent. F no escalar pertenece al conmutante: no hay irreducibilidad
global en el sentido usado en este repo. Esto no contradice los modelos
s=4 previos: allí R_j actúa también sobre k y C es antiunitaria, no
son una F unitaria interna que conmute con U(k) a k fijo.

La irreducibilidad de la representación del grupo de simetría y la
irreducibilidad del álgebra de coeficientes del QW son cuestiones
distintas. No se infiere una de la otra.

## 5. Antecedente y decisión

Leído el original docente del autor: Peter Woit, *Quantum Theory, Groups
and Representations*, versión fechada 20 octubre 2025,
[qmbook-latest.pdf](https://www.math.columbia.edu/~woit/QMbook/qmbook-latest.pdf),
página PDF 33 (numeración impresa 16), Sec. 2.1: enunciado y prueba del
lema de Schur. El conmutante escalar y las copias que aparecen aquí son
aplicaciones elementales; la derivación anterior explicita la aplicación
y sus hipótesis. No se atribuye al libro un resultado QCA nuevo.
También releída sources/1708.00826v2.pdf p.2 para distinguir simetría
interna de covariancia espacial. Biblioteca local ausente, sin índice nuevo.

Salida: LOCAL_EXCHANGE_INSUFFICIENT /
TWO_GENERATORS_FORCE_IDENTICAL_COPIES; STANDARD_REPRESENTATION_COROLLARY.
Se activa el corte. No se abre un constructor ni otro grupo para salvar
la candidatura. No es un no-go para toda universalidad entre especies:
acciones espaciales que relacionen nodos diferentes y mecanismos fuera
del contrato quedan sin estudiar. No se propone uno como resultado.

La selección dinámica y la escala física siguen sin mecanismo definido;
no se reabre la línea hexagonal. Todo permanece PRELIMINARY.

## Provenance y comprobación

Código permanente scripts/verify_independent_pairs_symmetry.py,
SHA256 186f9b787c8685bcad9a319b3ea3b34770f4345f9feff4f28a798b6485d0c34b.
Comando desde la raíz:

    /home/adnac/venvs/torch-gpu/bin/python -B scripts/verify_independent_pairs_symmetry.py

Python 3.12.3, SymPy 1.14.0. Salida 0, 37/37 checks exactos PASS.
Registro: reports/2026-11-06--independent-pairs-symmetry-verifier.txt.
Conmutantes comprobados por base completa de Pauli y, separadamente,
por rangos de ecuaciones en entradas complejas arbitrarias; espectros
por cuadrados, polinomios característicos y cambio explícito de base.
Sin script temporal, barrido ni revisión externa. git diff --check.
