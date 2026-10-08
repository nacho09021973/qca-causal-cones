# IG1c — dinámica física del tick completo, un paso

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Base: `e57802e1b2eca787cb02896f8400307bea3b0b6d`.
Autorización directa: «push y adelante con la dinamica fisica del tick completo».
Contrato congelado antes del cálculo; no modificar q, puertas, orden o ángulos.

## 1. Regla y pregunta

Se conserva el tick `U=U_T U_R` del
[contrato IG1b](INVERSE_GRAVITY_LOCAL_GATE_GATE.md): seis qutrits por celda,
constraints S/V, tres puertas R_aa y tres T_a^a por posición, θ=π/3.
Referencia estacionaria mixta y frontera IR del contrato padre permanecen.

Pregunta única: ¿el tick completo crea influencia algebraica espacial dentro
del sector S=V=1 entre operadores inicialmente de soporte disjunto?

No se calcula espectro, velocidad, crecimiento a muchos ticks ni modo físico.
Este test de un paso no requiere definir un vacío energético.

## 2. Operadores y estado testigo fijados

Toros de lado L≥6 múltiplo de 6, para evitar aliasing de los soportes usados.
Observador `O=T_x^x` en el cubo de origen i=(0,0,0), centro duplicado (1,1,1).
Perturbación `B=T_y^y` en i=(1,1,1), centro duplicado (3,3,3).
Stencils w de IG1b; sin elección posterior de otro par si falla.
O/B son unitarias físicas de tipo Z, con soportes disjuntos y `[O,B]=0`.
Sus partes hermítica y antihermítica son observables físicos.

Estado testigo algebraico ψ0: producto de estados X=1 en cada registro,
promediado sobre el grupo generado por los constraints V y normalizado.
Los V son permutaciones en la base X, sin fases en esa convención; el
promedio es no nulo. Conmutan con S y con todos los R, por lo que ψ0
satisface S=V=1 y todos los R_aa=1.
Este estado es una herramienta de prueba, no una preparación del vacío ni
una proyección intercalada en el tick. No sustituye a ρ_L en el contrato IR.

Bψ0 y OBψ0 siguen en el sector. Como los R conmutan, son estados con
eigenvalores conjuntos de R determinados por solapamientos de exponentes.

## 3. Cálculo exacto sin diagonalización de red

En Heisenberg `O(1)=U† O U=U_R† O U_R`, porque todo U_T conmuta con O.
Esta cancelación utiliza el tick completo y su orden fijado; no elimina
puertas que deberían intervenir.

Si C es una palabra física Z, sea M(C) el número de R de toda la red cuyo
eigenvalor en Cψ0 difiere de 1. Las demás puertas R aportan la misma fase
común. Cada puerta afectada tiene A_R=-1/2 en lugar de 1. Por ello

`O(1) Cψ0 = exp[-iπ(M(OC)-M(C))/2] OCψ0`.

Definir `f0=exp[-iπ M(O)/2]`,
`fB=exp[-iπ(M(OB)-M(B))/2]`.
Entonces `[O(1),B]ψ0=(fB-f0)OBψ0`.

Se construyen todas las incidencias finitas por solapamiento de stencils
locales, sin truncar artificialmente puertas influyentes. Se comparan con
una segunda formulación geométrica: las cargas de R producidas por un T_a^a
están en los ocho vértices de su cubo, con las dos componentes cíclicas de
signo opuesto derivadas de los stencils. Verificar la equivalencia exacta.

## 4. Umbrales y artefactos

Script permanente `scripts/verify_inverse_gravity_full_tick_dynamics.py`.
Tolerancia cero; phases exactas como potencias de -i. Código y contrato
versionados antes de ejecución; conservar salida íntegra en reports/.

Pruebas:

1. Soportes O/B disjuntos y preservación por las palabras de IG1b.
2. Incidencias por stencil coinciden con formulación geométrica independiente.
3. `|fB-f0|²>0` exactamente en el sector testigo. Si cero, terminal
   `FROZEN_WITNESS_NO_INFLUENCE`; no ajustar par, ángulo ni estado aquí.
4. Cota de consistencia `|fB-f0|²≤4`, porque O(1),B son unitarias.

PASS: `FULL_TICK_ONE_STEP_PHYSICAL_INFLUENCE_PASS_AUTHOR_SIDE`.
Un fallo algebraico da `INCIDENCE_OR_PHASE_CERTIFICATE_FAIL`.

## 5. Techo y parada

El PASS demuestra acción no escalar del tick en el sector y aparición de
influencia entre soportes inicialmente disjuntos. No demuestra crecimiento
sostenido, señalización con detector concreto, transporte hidrodinámico,
sector tensorial gapless, z=1, dos polarizaciones ni geometría gravitatoria.
No convierte un estado estacionario mixto en un vacío. No se generaliza a
otras puertas o tiempos sin contrato adicional. Revisión independiente pendiente.

El encargo se cierra al determinar este testigo y registrar la nueva frontera.
