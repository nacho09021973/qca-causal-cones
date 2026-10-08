# IG1b — puertas locales no triviales y tick de control

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Padre: [charter](INVERSE_GRAVITY_DESIGN_CHARTER.md).
Base: `058133a0bf92acf7d243bf73e08a0be19cab827e`.
Contrato congelado antes de ejecutar el certificado de IG1b.

## 1. Pregunta y motivo

¿Existen puertas locales del módulo q=3 de IG1a que preserven exactamente
S=V=1 y actúen allí de forma no escalar? Si pasan, definir un tick de control,
su inversa y su alcance. No calcular espectro many-body ni dispersión IR.

Motivo independiente: las puertas que solo son funciones de S/V actúan como
fase en el sector. La fuente Gu–Wen `biblioteca/arXiv-0907.1203.pdf` pp.15–16,
Ecs.48–49, ofrece operadores invariantes R y T con acción conjugada. Este
contrato prueba esa alternativa; no ajusta coeficientes para obtener z=1.

## 2. Datos fijos

Red, registro, constraints y convención ZX=ωXZ de
[IG1a](INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md), q=3 y seis registros por celda.
Orden xx,yy,zz,xy,yz,zx; `t_a=a+a^-1` en coordenadas duplicadas.

R_aa son palabras X centradas en vértices con stencils

```
r_xx=(0,t_z²,t_y²,0,-t_y*t_z,0)
r_yy=(t_z²,0,t_x²,0,0,-t_z*t_x)
r_zz=(t_y²,t_x²,0,-t_x*t_y,0,0)
```

T_a^a son palabras Z centradas en el centro de cubo i+(1/2,1/2,1/2):

```
w_x=(0,0,0,t_z,0,-t_y)
w_y=(0,0,0,-t_z,t_x,0)
w_z=(0,0,0,0,-t_x,t_y)
```

El centrado de T_x^x expresa Eq.49 como +Lxy en dos caras y -Lzx en otras
dos; no se identifica este operador diagonal de Cotton con todos los T_a^b.
No se completa el modelo L ni se traslada su dispersión a este subconjunto.

Solo simetría cíclica C3 de permutación x→y→z→x se adopta para ordenar
las familias. No se afirma isotropía SO(3), simetría cúbica completa ni Lorentz.

## 3. Puerta local fijada

Para cada palabra W=R_aa o T_a^a:

`A_W=(W+W†)/2`, `G_W=exp[-iθ A_W]`, `θ=π/3`.

Cada A_W es hermítico. Como W³=I,

`Π_W=(I+W+W²)/3`,
`A_W=(3Π_W-I)/2`,
`G_W=e^(iθ/2)[I+(e^(-3iθ/2)-1)Π_W]`.

Esta fórmula permite verificar unitariedad y acción sin una exponencial
global. θ es un ángulo de control elegido antes del test, no una velocidad.
No se variará para rescatar resultados. Ventana de perturbación declarada
para el claim de puerta no escalar: θ∈[π/4,5π/12], sin ejecutarla como scan.

## 4. Pruebas predeclaradas

Certificado: `scripts/verify_inverse_gravity_local_gates.py`, aritmética exacta.

1. Cada r_aa conmuta con cada vector por toda traslación: correlación cero.
   Cada w_a conmuta con el escalar: correlación cero. Las otras conmutaciones
   son automáticas por tipos X/X o Z/Z.
2. Segunda vía con stencils enteros de espacio real, introducidos desde las
   Ecs.48–49. Comparar también sus polinomios con las fórmulas anteriores.
3. Testigo fijado: Rzz en i=0 y T_x^x en centro duplicado (1,1,1).
   Solapamiento de exponentes -1, fase no trivial módulo 3.
4. En representación de una pareja qutrit R=X, T=Z^-1, comprobar relación
   TR=ω^-1 RT, unitariedad de G_R y `[G_R,T]≠0` a θ=π/3.
   Es test local de puerta, no el espectro de un autómata gravitatorio.
5. Identidades `r_xx+r_yy+r_zz=c`, `w_x+w_y+w_z=0`; informar redundancias.

PASS local: `LOCAL_CONSTRAINT_PRESERVING_NONSCALAR_GATE_PASS_AUTHOR_SIDE`.
Primer FAIL detiene el contrato; no cambiar palabra, q ni ángulo para rescatar.
Un PASS no cuenta dos modos físicos por tener dos palabras independientes.

## 5. Tick fijado y alcance

`U=U_T U_R` donde cada bloque aplica G_W en todas las posiciones y en
los tres tipos, primero R y después T. Todas las puertas R conmutan entre sí;
todas las T conmutan entre sí. No se exige conmutación entre bloques.

Implementación en capas disjuntas: ordenar aa=(xx,yy,zz), colores de centros
R=i mod 3 en orden lexicográfico, 27 por tipo; después a=(x,y,z), colores
T=i mod 2, 8 por tipo. Total 81+24=105 capas independientes del volumen.
Los soportes de R están dentro de las celdas i+[-1,1]³ y los de T dentro de
i+[0,1]³. Esta coloración es suficiente; no es una profundidad óptima.
Para toros de control: L≥6 múltiplo de 6 en cada dirección.

La inversa es `U_R† U_T†` con orden de capas invertido. Cota por tick e
inversa: 3 celdas en norma ℓ∞. Cada bloque conmutante solo puede añadir
soportes de puertas que tocan el soporte inicial de ese bloque: diámetro
R≤2, T≤1. No se deduce esta cota del número de puertas por volumen.
Aunque la coloración tiene periodo 6, cada bloque completo es invariante por
traslación de una celda por conmutación interna y coeficientes uniformes.

## 6. Referencia de control y frontera IR

En cada toro, P proyecta al sector no vacío S=V=1 de IG1a.
Referencia fijada: `ρ_L=P/Tr(P)`. Es estacionaria si todas las puertas
preservan P. No es un vacío energético ni un sector de baja temperatura.
No se aplican mediciones ni proyecciones durante el tick.

Este control fija una regla sin materia y una referencia algebraica. IG1
del charter sigue incompleto respecto al criterio IR: antes de dispersión
hay que especificar estado/sector IR, observables, ramas y límites con error.
El criterio deseado sigue siendo dos polarizaciones físicas con z=1 en un
régimen controlado; no se presupone para ρ_L ni se usa para seleccionar puertas.

No se calcula conteo de modos, espectro, dinámica de materia o métrica.
No se afirma transporte ni no trivialidad del tick completo a partir de
la no trivialidad de una puerta: posibles cancelaciones colectivas requieren
un test aparte. El testigo de este contrato acredita la puerta local.
