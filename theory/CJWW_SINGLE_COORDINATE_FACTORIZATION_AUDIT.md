# CJWW_SINGLE_COORDINATE_FACTORIZATION_AUDIT

Fecha: 2026-09-30. Autorización: instrucción del usuario de hacer commit/push
del atlas, elegir familias y seguir. Estado al escribir: contrato de
**verificación de un resultado ya alegado**, antes del nuevo certificado.
No se presenta como contrato anterior al descubrimiento: la lectura dirigida
en `3976026` ya anunció una obstrucción.

## Objetivo y cuantificadores

Certificar únicamente si el símbolo exacto `walk2()` (CJWW 5.15) admite

`W(p)=A(p_i) B(p_j) C(p_k)`

para alguna de las seis permutaciones de los tres ejes, con factores
invertibles diferenciables 2×2, cada uno dependiente de un único momento.
Un tick original, celda C² original, coordenadas originales. Se permite
conjugación constante on-site; constantes a izquierda/derecha también se
absorben en los factores y no cambian la obstrucción.

Se excluyen factores repetidos en una dirección, coordenadas mezcladas,
supercell, periodos espaciales adicionales, ancillas, dilaciones y `W^m`.
No es una clasificación de todos los paired QWs ni un test de universalidad
métrica, backreaction o gravedad. La correspondencia bibliográfica debe citar
`biblioteca/1609.00305v2.pdf` p.5, §IV, ec.36 y producto de substeps; no se
traslada este test automáticamente a sectores agrupados.

## Obligaciones y terminales

1. Confirmar símbolo, unitariedad y determinante exactamente, reutilizando
   `walk2()` y la normalización Laurent del repositorio.
2. Para cada posible primer eje i, formar `L_i=(∂_i W)W†` y dar un testigo
   exacto de dependencia en otro eje. Verificar las seis permutaciones.
3. Segunda vía: testigos de valores en puntos exactos, además de derivadas;
   comprobar la sección `W(π/2,p2,p3)=i σ1` y la variación no constante en
   p2 y p3 cuando p1=0. Con factores invertibles de un eje cada uno, esa
   sección constante obligaría a que los factores de p2 y p3 fueran constantes.
4. Control positivo: `walk1()` (CJWW 5.12) tiene su factorización publicada
   en el orden 1,2,3 y debe superar la condición del primer eje.
5. Explicar invariancia bajo conjugación constante, sin buscar cambios de
   coordenadas, soporte o celda.

`SINGLE_COORDINATE_FACTORIZATION_EXCLUDED`: obligaciones 1–5 satisfechas y
un testigo para cada primer eje. `OPEN_AFTER_AUDIT`: discrepancia o evidencia
insuficiente. `ALLEGED_OBSTRUCTION_NOT_CONFIRMED`: el certificado no reproduce
el resultado previo; detenerse y corregir la ficha antes de seguir.

Una sesión, sin búsqueda de familias ni ajustes del test. Evidencia máxima:
prueba y certificado del autor, **PRELIMINARY / INDEPENDENT_REVIEW_PENDING**.
Se conserva el código en `scripts/verify_cjww_coordinate_factorization.py`.
El informe debe declarar límites del puente; no se promueve la lectura
dirigida entera a gate PASS. Los contratos y cierres W6/W12, F2–F4 permanecen
con su alcance original.
