# Segundo par de conos: velocidades diferentes en una dinámica irreducible

2026-11-05. Codex. PRELIMINARY, author checks only, sin revisión externa,
sin promoción y sin reivindicación de novedad.
Contrato: theory/TWO_CONES_DOUBLE_SHIFT_ATTEMPT.md, hash antes de calcular
942384106f36cb44aafbe30290efd6885f378f76ffab5be7de99a238482f7122.
Sin prerregistro Git. Nueva estructura autorizada por el usuario; no
extensión silenciosa del intento anterior, cuyo corte se mantiene.

## Constructor y resultado

Se emplean los G_i y W del contrato, con a=3/5, b=4/5, theta=pi/4,
y L_i=sigma_i tensor I. Una actualización es

    U(k)=W [exp(-i k_x G_x) exp(-i k_x L_x)]
           [exp(-i k_y G_y) exp(-i k_y L_y)]
           [exp(-i k_z G_z) exp(-i k_z L_z)].

Cada G_i y L_i es hermítico e involutivo, luego cada factor es unitario.
La convolución exacta da 27 coeficientes no nulos, F={-2,0,2}^3, incluido
el origen. Grupo generado: 2Z^3 (están los tres 2e_i). C_micro=[-2,2]^3,
paso más largo 2sqrt3. Normalizando por esa longitud, sin cambiar la unidad
temporal, F={-1,0,1}^3/sqrt3 y r_in=1/sqrt3. No se calcula el cuerpo
asintótico estricto.

El espectro de U(0)=W consta de fases +pi/4 y -pi/4, ambas de rango dos.
P=I tensor (I+tau_z)/2, Q=I-P. Para K_i=G_i+L_i:

    P K_i P = (1+a)(sigma_i tensor I) P,
    Q K_i Q = (1-a)(sigma_i tensor I) Q.

La perturbación nodal de primer orden, como en el intento anterior,
proporciona H_P(k)=(1+a) k.sigma y H_Q(k)=(1-a) k.sigma en unidades
crudas, además de sus fases centrales. Las trazas son cero y sus
polinomios característicos son lambda²-(1±a)²|k|²: dos conos isotrópicos
sin inclinación. Velocidades normalizadas:

    c_P = (1+a)/(2sqrt3) = 4sqrt3/15,
    c_Q = (1-a)/(2sqrt3) = sqrt3/15,
    c_P/c_Q = 4.

Son dobletes locales en fases Floquet diferentes, no una identificación
de dos especies físicas a una misma energía. Resultado: TWO_UNEQUAL_CONES.

## Comprobación por eigenfases axiales

Sobre k=t e_i, sigma_i tiene eigenvalor eps=±1. El bloque tau de U es

    exp(-i eps t) exp(-i theta tau_z) exp(-i eps t T_i).

Retirando la fase escalar, su determinante es 1 y su semitraza

    f_eps(t)=cos(theta) cos(t)-eps*a sin(theta) sin(t).

Las eigenfases son eps*t ± acos(f_eps(t)), con ramas locales alrededor
de t=0. Como theta=pi/4 y d acos(f_eps)/dt en 0 = eps*a, las pendientes
son eps*(1+a) y eps*(1-a). Esta segunda vía axial coincide exactamente
con las compresiones; la isotropía en todas las direcciones se comprueba
por los polinomios característicos de H_P y H_Q.

## Simetría e irreducibilidad

R_j=sigma_j tensor I invierte G_i y L_i si i!=j y los conserva si i=j;
conmuta con W. Se verifica R_j A_h R_j†=A_(g_j h) en los 27 coeficientes,
para los tres generadores D2. No se postula covariancia cúbica completa.

No es una suma directa constante de dos walks. La suma de los coeficientes
da W y su momento en h_i da W K_i. Todo X que conmute con cada A_h
conmuta por tanto con W y K_i. La matriz exacta de las restricciones
[X,W]=[X,K_x]=[X,K_y]=[X,K_z]=0 tiene rango 15 sobre las 16 entradas
complejas de X. Su núcleo contiene I y tiene dimensión 1; el conmutante
de todos los A_h es así exactamente C I. El script realiza este cálculo
con aritmética racional compleja, retirando solo el factor escalar sqrt2
de W, que no cambia las restricciones.

Interpretación analítica del rango: conmutar con W fuerza bloques X_P,
X_Q. Las partes diagonales de K_i fuerzan que cada bloque conmute con
las tres Pauli, porque 1±a son no nulos. Son escalares. Las partes entre
sectores son no nulas (b!=0), por lo que ambos escalares deben coincidir.
Irreducibilidad global no niega los autoespacios nodales locales.

## Verificación, significado y cierre

python3 -B scripts/verify_two_cones_double_shift.py
salida 0, SymPy 1.14.0, 165/165 comprobaciones exactas. Registro:
reports/2026-11-05--two-cones-double-shift-verifier.txt.
Script SHA256:
07bdcfbb2a9ffbdbaa9b798a0f3e99f9d91a3991fb40abb1c5b1ab9acdcfa2f6.
Incluye involuciones, unitariedad Laurent de cada factor por eje,
convolución completa del soporte, nodo, D2, compresiones, dos vías de
pendientes, isotropía, conmutante y normalización. La unitariedad global
resulta del producto de factores unitarios; no se infiere de una malla.

El resultado difiere del anterior porque ahora la pendiente axial es una
compresión de K_i=G_i+L_i, que no es una involución: no le aplica la
identidad de trazas del cuadrado usada allí. No hay contradicción.
Al cambiar el soporte y la arquitectura, esto tampoco es una perturbación
en el contrato anterior ni refuta protección a soporte BCC fijo.

El intento termina en este punto racional, sin más búsqueda. No prueba
una ley sobre todos los sustratos, universalidad IR ni novedad. Antes de
promoverlo haría falta revisión independiente y comparación primaria con
construcciones de múltiples conos. No se envía a terceros en este intento.
