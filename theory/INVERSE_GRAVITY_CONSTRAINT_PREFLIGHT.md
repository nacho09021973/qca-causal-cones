# IG1a — preflight del módulo finito de restricciones tensoriales

Fecha: 2026-10-08. Contrato padre:
[INVERSE_GRAVITY_DESIGN_CHARTER](INVERSE_GRAVITY_DESIGN_CHARTER.md).
Este preflight se congela antes de ejecutar el certificado. Es un módulo
algebraico previo a IG1, no un candidato completo ni cálculo de espectro.

## Objeto, motivación y alcance

Fuente: Gu–Wen, `biblioteca/arXiv-0907.1203.pdf`, pp.13–15, Ecs.38–46.
Se examina la realización de constraints mediante relojes finitos y operadores
locales conmutantes. Motivo: resolver primero la compatibilidad de constraints
con una celda finita; no seleccionar parámetros desde una dispersión buscada.

Red Z³; tres registros diagonales xx,yy,zz en cada vértice y un registro
xy,yz,zx en cada cara positiva correspondiente. Agrupados por celda primitiva:
seis qutrits, dimensión local 3⁶=729. Aquí nG=3 es fijo, sin límite nG→∞.
No se identifica esta celda con una fase semiclasica o un autómata gravitatorio.

En cada registro: `X|n>=|n+1 mod 3>`, `Z|n>=ω^n|n>`,
`ω=exp(2πi/3)`, de modo que `ZX=ωXZ`. No se postula una pareja
canónica continua exacta en dimensión finita.

## Stencils congelados

Coordenadas duplicadas: vértices en (2i,2j,2k), caras xy en
(2i+1,2j+1,2k), y análogamente. Variables de Laurent x,y,z para esas
coordenadas; `t_a=a+a^-1`. Orden de registros: xx,yy,zz,xy,yz,zx.

El escalar S en cada vértice es un producto de X con exponentes del stencil

`c=(t_y²+t_z², t_x²+t_z², t_x²+t_y²,
    -t_x*t_y, -t_y*t_z, -t_z*t_x)`.

Los vectores V_a, centrados en los enlaces de cada dirección, son productos
de Z con stencils relativos a esos centros:

`v_x=(t_x,0,0,t_y,0,t_z)`;
`v_y=(0,t_y,0,t_x,t_z,0)`;
`v_z=(0,0,t_z,0,t_y,t_x)`.

Esta notación incluye offsets geométricos y los factores 2 del cambio a
variables compactas de la fuente; no reemplazarla por diferencias continuas.
Al expandir, un diagonal c contiene coeficiente 4 en su centro y 1 en
cuatro vecinos; cada componente fuera de la diagonal tiene cuatro -1.

## Pruebas y umbrales previos

Certificado permanente: `scripts/verify_inverse_gravity_constraint_module.py`.
Álgebra exacta, tolerancia cero, sin fitting ni diagonalización de candidato.

1. Comprobar X³=Z³=I y ZX=ωXZ en matrices de un qutrit.
2. Comprobar `c·v_a=0` como identidades de Laurent, las tres direcciones.
   Los stencils son pares: `v_a(x^-1,y^-1,z^-1)=v_a(x,y,z)`.
   Por ello es también la identidad de correlación necesaria para todas
   las traslaciones de S/V, no solo para un par coincidente.
3. Segunda vía: construir los stencils enteros directamente en espacio real,
   enumerar todos sus solapamientos por traslación y exigir fase entera cero.
4. Repetir la vía real después de reducir exponentes módulo 3.

PASS significa únicamente `FINITE_CONSTRAINT_ALGEBRA_PASS_AUTHOR_SIDE`.
FAIL detiene este módulo como `CONSTRAINT_STENCIL_OR_CONVENTION_FAIL`;
no cambiar stencils o q para rescatar el test bajo este contrato.

## Qué queda fuera

S/S y V/V conmutan por ser, respectivamente, productos exclusivamente de X
y de Z. El sector físico propuesto es el eigensector S=V=1; su selección
no se realiza mediante medición ni proyección TT durante la evolución.
La existencia de estados que lo satisfacen se argumentará en el informe,
pero no se calculará su dimensión ni el conteo de excitaciones.

No hay tick, materia, estado estacionario de una dinámica, energía o rama IR
especificados. No hay modo tensorial certificado, gauge continuo emergente,
dispersión, métrica, backreaction ni resultado de gravedad.
La prueba algebraica no promueve R1/R3/R4 del contrato padre.
