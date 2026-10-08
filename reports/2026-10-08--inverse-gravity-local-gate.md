# IG1b — puerta física local y tick de control

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato/código congelados en `601463bc851d7b87cf149637ddcb8000a629fb3f`:
[contrato](../theory/INVERSE_GRAVITY_LOCAL_GATE_GATE.md),
[script](../scripts/verify_inverse_gravity_local_gates.py).

## 1. Resultado y procedencia

Comando: `python3 scripts/verify_inverse_gravity_local_gates.py`.
Salida íntegra: [certificado](2026-10-08--inverse-gravity-local-gate-certificate.txt).
SymPy 1.14.0, aritmética exacta, tolerancia cero, código de salida 0.
No se cambió el contrato, stencil, dimensión ni ángulo tras ejecutar.

`IG1b = LOCAL_CONSTRAINT_PRESERVING_NONSCALAR_GATE_PASS_AUTHOR_SIDE`.
Evidencia: certificado algebraico y demostraciones propias; revisión
independiente pendiente. Reproduce operadores de Gu–Wen; NOVELTY OPEN.

Lectura primaria previa: `biblioteca/arXiv-0907.1203.pdf` pp.15–17,
Ecs.48–55, especialmente Rzz Eq.48 y T_x^x Ecs.49,53.
Es el mismo PDF con SHA256 registrado en
[IG1a](2026-10-08--inverse-gravity-constraint-mechanism.md).
La fuente incluye otros operadores y otra dinámica: este tick no se presenta
como realización completa del modelo L ni de su límite semiclasico.

## 2. Puerta no trivial dentro del sector

El certificado reproduce por Laurent y por stencils de espacio real que los
tres R_aa y los tres T_a^a preservan todos los S/V por toda traslación.
Rzz(0) y T_x^x centrado en (1,1,1) de coordenadas duplicadas tienen
solapamiento entero -1. Por ZX=ωXZ:

`T R = ω^-1 R T`, `R³=T³=I`.

No se ha obtenido esa relación tras eliminar modos; es una relación de
palabras locales en el álgebra de registros completa. Ambas palabras
preservan el sector no vacío de IG1a, por lo que sus restricciones siguen
siendo unitarias y satisfacen la misma relación.

Si R fuese escalar en ese sector, esta identidad implicaría ω=1, contradicción.
Más precisamente, T permuta cíclicamente los tres eigensectores de R; al
menos uno existe y por tanto existen los tres. Para

`G_R=exp[-iθ(R+R†)/2]`, `θ=π/3`,

el valor de `(R+R†)/2` es 1 en R=1 y -1/2 en R=ω,ω².
Las fases de G_R son `e^-iπ/3` y `e^iπ/6`, distintas. Por tanto G_R es
una puerta física no escalar y unitaria, exactamente preservadora del sector.
La representación 3×3 del certificado comprueba la misma relación y
`[G_R,T]≠0`; no sustituye ni simula la red completa.

En la ventana congelada θ∈[π/4,5π/12], la diferencia angular 3θ/2 permanece
en [3π/8,5π/8], sin alcanzar 2πm. La no trivialidad de esta puerta persiste.
Esto no demuestra robustez del espectro ni una fase gravitatoria.

## 3. Tick, inversa y soporte

El contrato fija `U=U_T U_R`, usando las tres permutaciones cíclicas de cada
familia, q=3 y ángulo π/3. Los bloques contienen palabras X o Z respectivamente;
conmutan internamente. Se implementan con 81 capas R y 24 capas T, cada
una de puertas de soporte disjunto, para una profundidad fija 105.

Cada soporte R cabe en celdas i+[-1,1]³ y cada T en i+[0,1]³. Separar los
centros R por color mod 3 y T por color mod 2 asegura disjunción dentro de
una capa. La profundidad es suficiente y no pretende ser mínima.

La inversa invierte bloques y capas y toma puertas adjuntas. La conmutación
interna permite cancelar las puertas que no tocaban el operador inicial
de cada bloque antes de conjugación; no hay cadena de expansión entre
puertas del mismo bloque. En ℓ∞, R añade como máximo 2 celdas y T 1.
U y U^-1 tienen por tanto alcance ≤3 celdas por tick. Las capas son una
representación de la actualización, no una exponencial Hamiltoniana global.

Estas son demostraciones estructurales a partir de soportes y álgebra, no
tests numéricos de sistemas grandes. Acreditan un QCA de control y conservación
exacta de constraints; no se evaluó el tick completo en el sector para excluir
cancelaciones colectivas ni para demostrar transporte.

## 4. Referencia y criterio IR

En toros L≥6 múltiplo de 6 se fija `ρ_L=P/Tr(P)`. Como cada puerta conmuta
con P, `Uρ_LU†=ρ_L` exactamente. El sector es no vacío por la construcción
de IG1a. La referencia y el tick están definidos sin postselección ni ancillas.

Esta referencia es máximamente mixta en el sector, no un vacío energético.
No se identifica estacionariedad con baja energía. La dinámica de
correlaciones podría ser una pregunta válida, pero todavía no se ha definido
una ventana IR ni un régimen de excitaciones que justifique el objetivo z=1.
No se calcula un espectro aprovechando esta referencia como sustituto de ese
control ausente.

**Frontera actual:** `CONTROL_TICK_SPECIFIED / IR_UNDEFINED`.
IG1 del charter permanece incompleto para R1 y para el cálculo de modos:
faltan la selección justificada de un estado/sector IR y el procedimiento
controlado de extracción de excitaciones. Materia y geometría operacional
R2/R5 tampoco están construidas. Dos familias con una redundancia no son
evidencia de dos polarizaciones físicas.

## 5. Siguiente filtro y cierre del encargo

Se completó el encargo algebraico: puerta no escalar, preservación exacta,
tick de control, inversa, alcance y referencia de control explícitos.
El criterio IR sigue abierto y es ahora el primer problema científico.

Antes de dispersión, el siguiente expediente debe comprobar si la regla
produce dinámica física colectiva no trivial y qué estado/sector permite
interpretar sus excitaciones. Fijar observables y errores antes de ejecutarlo.
Un fracaso del tick de control se registrará para este tick; no se rescatará
con parámetros ni se extrapolará a imposibilidad de toda gravedad en QCA.

No se promociona el target Einstein, no se reabre W1–W12 y no hay claim de
Lorentz, spin-2, cono común, fuente o escala física absoluta.
