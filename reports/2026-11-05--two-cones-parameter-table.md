# Cinco pares en la arquitectura de doble desplazamiento

2026-11-05, Codex. PRELIMINARY, sin revisión independiente ni promoción.
Contrato: theory/TWO_CONES_PARAMETER_TABLE_ATTEMPT.md, hash anterior
al cálculo: 2d95baaa9823be44905b739bfd8605740a33053cadece8d112131719f0a5300b.
No prerregistro Git. Extensión expresamente autorizada de cinco puntos;
no se modifica el corte del contrato del primer punto.

## Fórmula y significado

El constructor anterior se conserva cambiando únicamente a y
b=sqrt(1-a²). Para 0<a<1, sus compresiones siguen siendo
P K_i P=(1+a) sigma_i P y Q K_i Q=(1-a) sigma_i Q.
Por tanto, con paso máximo 2sqrt3 y una actualización por unidad temporal:

    c_P=(1+a)/(2sqrt3), c_Q=(1-a)/(2sqrt3).

Esta derivación aplica a cualquier punto con el soporte y los conos
declarados; los controles de soporte de esta tabla son de cinco puntos,
no una clasificación universal del soporte en todo el intervalo.

| a | c_P | c_Q | c_P/c_Q |
| --- | --- | --- | --- |
| 1/5 | sqrt3/5 | 2sqrt3/15 | 3/2 |
| 1/3 | 2sqrt3/9 | sqrt3/9 | 2 |
| 1/2 | sqrt3/4 | sqrt3/12 | 3 |
| 3/5 | 4sqrt3/15 | sqrt3/15 | 4 |
| 4/5 | 3sqrt3/10 | sqrt3/30 | 9 |

La tabla exacta legible por máquina la genera el script permanente en
reports/2026-11-05--two-cones-parameter-table.csv. Es la misma familia de
constructores, no cinco arquitecturas independientes ni cinco especies
de un mismo modelo.

Se conservan en esta familia las relaciones

    c_P+c_Q=1/sqrt3,
    (c_P-c_Q)/(c_P+c_Q)=a,
    c_P/c_Q=(1+a)/(1-a).

La primera es una consecuencia de la suma de contribuciones 1±a, no
evidencia de una ley para todos los QCA. sqrt3/15 no es una unidad
universal: aparece al sustituir a=3/5. El factor sqrt3 común en las
expresiones procede de normalizar por el máximo paso euclídeo 2sqrt3.
La razón de velocidades es adimensional y cambia con a; no puede
eliminarse mediante un cambio común de unidades.

Segunda vía de lectura: las eigenfases axiales exactas del informe
anterior tienen semitraza (cos t-eps*a sin t)/sqrt2; al derivarlas en
t=0 dan eps*(1±a). La suma y el cociente de la tabla no proceden de un
ajuste a cinco observaciones, sino de esa fórmula.

## Verificación reproducible

Ejecutar python3 -B scripts/verify_two_cones_parameter_table.py.
Registro: reports/2026-11-05--two-cones-parameter-table-verifier.txt.
Ejecución: salida 0, SymPy 1.14.0, 415/415 comprobaciones exactas PASS.
SHA256 del script:
a56c94889668469df4398a8508cf328ec4d6c10dce22b38b49d86ab67eccbf2c.
El generador usa finales de línea LF en el CSV; ajuste de formato durante
la publicación, sin cambios en fórmulas ni valores.
Comprueba por punto involuciones y unitariedad Laurent por eje,
compresiones, relaciones Clifford de los conos, soporte de 27 elementos,
reconstrucción de momentos, D2 en los generadores y conmutante escalar.
El soporte genera 2Z^3 porque contiene todos los ejes ±2e_i y todos sus
vectores tienen coordenadas pares. Normalización igual en las cinco filas.

Resultado científico limitado: existen diferentes pares en esta estructura;
no todos tienen razón entera. Las verificaciones son del autor; no prueban
novedad, interpretación física de los sectores o protección frente a todas
las perturbaciones. El intento termina con esta tabla.
