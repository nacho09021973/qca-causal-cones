# Simetría local que empareja los dos conos

2026-11-05. Autor: Codex. PRELIMINARY, sin revisión independiente,
sin promoción ni atribución de carga física o novedad.
Contrato: theory/LOCAL_PARTICLE_HOLE_TWO_CONES_ATTEMPT.md, SHA256 previo
00fe971ec73d0b3c5e988150b2da2eb16b23e129a55f1e947d38795db242d2df.
Sin prerregistro Git. Punto exacto a=3/5, b=4/5, theta=pi/4.

## Convención y resultado

Para una antiunitaria local C=V K, la condición de Bloch es

    V U(k)* V† = U(-k).

El asterisco conjuga entradas, no transpone. Con la convención Fourier
U(k)=sum_h A_h exp(-i k.h), esto equivale a

    V A_h* = A_h V  para todo h,

si V es unitario. Es un sistema lineal complejo en las 16 entradas de V.

| Modelo | Rango del sistema | Dimensión del núcleo | Resultado |
| --- | --- | --- | --- |
| Tres desplazamientos, 8 coeficientes | 15 | 1 | LOCAL_PHS_FOUND |
| Doble desplazamiento, 27 coeficientes | 16 | 0 | NO_LOCAL_PHS |

En el primero, un representante es V=sigma_y tensor tau_y. Es unitario,
V V*=I (C²=+I), y V P* V†=Q. El núcleo unidimensional y la existencia
de este V implican unicidad salvo fase para esta condición local en el
punto comprobado. En el segundo, núcleo cero excluye cualquier V local
unitario, no solo el producto de Pauli probado inicialmente.

## Comprobación analítica del candidato

La identidad Pauli sigma_y sigma_i* sigma_y=-sigma_i, y su análoga en
tau, hacen que V G_i* V†=G_i: los dos signos se cancelan. También
V W* V†=W, pues tau_y invierte tau_z y la conjugación compleja invierte
la fase. En consecuencia, al conjugar

    U(k)=W prod_i exp(-i k_i G_i/sqrt3),

se obtiene U(-k), con el mismo orden de factores. El argumento no requiere
diagonalizar U(k) ni construir V a partir de sus eigenvectores. Las
identidades valen con coeficientes a,b reales del constructor; el control
lineal exhaustivo se ha realizado solo en el punto fijado.

La matriz V actúa en la base sigma tensor tau como

    [ 0  0  0 -1 ]
    [ 0  0  1  0 ]
    [ 0  1  0  0 ]
    [-1  0  0  0 ].

Es local y no depende de k ni de una velocidad medida.

## Consecuencia para las pendientes

Si U(k) psi=exp(-i omega) psi, la antiunitariedad y la identidad anterior
dan U(-k) C psi=exp(+i omega) C psi. Por tanto, el espectro se empareja
como (k,omega) con (-k,-omega). En k=0 el operador intercambia los
dobletes de fases +theta y -theta. Para conos isotrópicos sin inclinación,
sus pendientes en magnitud son iguales. La afirmación es condicional a
que esos conos sobrevivan: PHS por sí sola no demuestra su existencia,
isotropía o estabilidad frente a toda perturbación.

Perturbaciones que conserven el mismo C y esos nodos/conos mantienen su
emparejamiento. Esto es una condición suficiente; no se demuestra necesaria
para toda posible igualdad de velocidades. No se fija su valor común.

## Por qué falla el segundo modelo

En el constructor con factores adicionales L_i=sigma_i tensor I,
V L_i* V†=-L_i. Su conjunción no produce la transformación requerida de
los factores completos. Este fallo del candidato no sería una prueba de
ausencia; la prueba adicional es el rango 16 del sistema de TODOS los
coeficientes del segundo modelo.

Otra obstrucción, desde los resultados previos: una antiunitaria de esta
forma intercambiaría necesariamente los dos dobletes de W y emparejaría
sus conos isotrópicos; las pendientes exactas distintas 4sqrt3/15 y
sqrt3/15 impiden tal emparejamiento. Esta lectura espectral concuerda con
el cálculo independiente por coeficientes.

## Verificador, fuente y límite físico

python3 -B scripts/verify_local_particle_hole_two_cones.py
Salida 0, SymPy 1.14.0, 22/22 comprobaciones exactas PASS; incluye las dos
matrices completas de restricciones. Registro en
reports/2026-11-05--local-particle-hole-two-cones-verifier.txt.
Script SHA256:
b4bfffacf6a0629276d7427be16a5ea9225cce2e3b1b0631734e4c0fe90da75a.
Se retira el factor escalar REAL sqrt2 de W para el cálculo racional;
no cambia las ecuaciones de entrelazamiento.

Antecedente primario localizado: Asboth, arXiv:1208.2143v2,
https://arxiv.org/html/1208.2143v2 , Sec. III.1, simetría partícula–hueco
en quantum walks. El emparejamiento espectral por una antiunitaria es
estándar. La derivación aquí es autocontenida; no se reivindica que la
aplicación concreta o la matriz V sean nuevas.

Significado físico limitado: se ha encontrado una simetría exacta del
modelo de una partícula. No se ha identificado una carga conservada ni
una teoría de campo cuyos operadores de creación y aniquilación realicen
conjugación de carga. No permite llamar fotón/electrón a los dobletes,
ni explicar igualdad entre especies no emparejadas por C. Tampoco se
excluyen otras simetrías del segundo modelo: transformaciones espaciales,
dependientes de k o en otro marco temporal quedan fuera del contrato.
El intento termina con estos dos veredictos.
