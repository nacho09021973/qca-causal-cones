# IG1a — módulo de restricciones y condición para dar dinámica

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato y script congelados en `1798644f5af8a8d4f4f2458547bb09248337d7d6`:
[preflight](../theory/INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md),
[certificado](../scripts/verify_inverse_gravity_constraint_module.py).

## 1. Resultado ejecutado y procedencia

Comando: `python3 scripts/verify_inverse_gravity_constraint_module.py`.
Python con SymPy 1.14.0, código de salida 0. Salida íntegra conservada en
[constraint-certificate.txt](2026-10-08--inverse-gravity-constraint-certificate.txt).
Tolerancia cero. No se escribió código temporal para producir este resultado.

`IG1a = FINITE_CONSTRAINT_ALGEBRA_PASS_AUTHOR_SIDE`.
Evidencia: certificado algebraico exacto propio, sin revisión independiente.
Es una reproducción de una estructura de Gu–Wen, no una novedad propuesta.

Se verificaron matrices de un qutrit, las tres identidades de Laurent y, por
segunda vía, todos los solapamientos de los stencils introducidos directamente
en espacio real, tanto enteros como reducidos módulo 3. La correlación incluye
todas las traslaciones: no se limita a constraints en el mismo centro.

Fuente primaria: `biblioteca/arXiv-0907.1203.pdf`, pp.13–15, Ecs.38–46;
discusión dinámica releída en pp.18–21, especialmente §§VII.D–E.
SHA256 del PDF local:
`3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
Original: [Gu–Wen v3](https://arxiv.org/abs/0907.1203v3).

## 2. Qué concreta el módulo

Seis qutrits por celda Z³, dimensión 729; constraints escalares de tipo X y
vectoriales de tipo Z, con soporte local explicitado en el preflight. El
algebra de reloj evita postular una relación canónica continua imposible en
dimensión finita: si matrices d×d obedecieran `[A,B]=iI`, tomar trazas daría
`0=id`. Esta observación es elemental y no es una obstrucción a variables
continuas efectivas en un sector colectivo.

En un toro finito, el sector S=V=1 es no vacío. Partir de `|0>` en cada
registro satisface todos los V. El promedio finito sobre el grupo abeliano
generado por los S conserva V=1 y produce un vector no nulo: los S son
permutaciones de la base, por lo que la amplitud de la configuración cero
recibe contribuciones positivas, incluida la identidad. Normalizar ese vector
da un estado del sector. Esta es una construcción algebraica de estado,
análoga a Gu–Wen p.15; no es preparación dinámica ni selección de vacío.
No se exige unicidad, no se calcula degeneración y no se extrapola sin prueba
a un estado infinito con propiedades IR.

Denotar P el proyector de este sector es una herramienta de análisis.
No se aplicará P en cada tick para eliminar excitaciones.

## 3. Requisito exacto para puertas que preserven el sector

Para una puerta local unitaria G, la condición suficiente
`[G,S_r]=[G,V_r,a]=0` para todos los constraints implica `[G,P]=0`.
Si un tick es un número fijo de capas con puertas así y soporte acotado,
también preserva el sector. Su inversa invierte orden de capas y adjunta
puertas; ambas evoluciones tienen alcance finito independiente del volumen.
Esto deriva R0 y la invariancia condicional para esa construcción, pero no
prueba R1: invariancia no es un orden energético ni un sector relativista.

La conmutación de cada puerta es suficiente, no necesaria. Se permite
demostrar conservación exacta por un ciclo completo en una futura regla.
Tampoco se exige aquí que toda emergencia gauge futura sea exacta por tick:
una alternativa con fugas acotadas necesita su propio control IR.

**Descartado: usar solo funciones de los constraints como dinámica física.**
En S=V=1, cada puerta `exp[-iθ(S+S†)]`, o su análoga vectorial, actúa como
`exp[-2iθ]I`. Un producto de ellas es una fase común en el sector. No puede
dar transporte tensorial dentro de ese sector. El argumento se limita a
puertas que sean funciones de los constraints; no excluye su conmutante local.

Gu–Wen p.15, Ecs.47–48, ofrece operadores R_ab que conmutan con las
restricciones y actúan sobre el sector; el problema de introducir dinámica
no se resuelve con las puertas de penalización solas. No se adoptaron aquí
ángulos, capas ni una actualización basada en R_ab.

## 4. Por qué la penalización Hamiltoniana no basta para un QCA

Considerar únicamente un projector local de defecto Q, con eigenvalores 0,1,
y `UΔ=exp[-iτΔQ]`. Sus eigenfases son 1 y `exp[-iτΔ]`.
Para `τΔ=2πm` coinciden exactamente: un coste Hamiltoniano Δ grande no
implica separación de quasienergía. Esto es una identidad de un kick aislado,
no el espectro de un candidato gravitatorio ni un no-go para penalizaciones.

Además, al añadir una puerta B con `[B,P]≠0`, la unitariedad del tick no
demuestra `P U (I-P)=0`. Un producto local aproxima una evolución auxiliar
solo bajo sus controles de error; no hereda sin prueba su estado fundamental,
gap, constraints o fase a tiempos arbitrarios.

Se puede buscar una separación de fases en una ventana fija, un sector exacto
o un régimen aproximado con fugas controladas. Cada ruta debe declarar τ,
escalas, límites y el criterio IR antes del cálculo. No se tomará `Δ→∞`
con τ fijo como prueba de congelación de defectos.

## 5. Límite de la ruta Gu–Wen N

[SOURCE] Gu–Wen p.19 registra `[HU,HJ]≠0`, `[HU,Hg]≠0`, y que HJ/Hg no
actúan dentro del subespacio de energía cero de HU. Pp.20–21 explican por qué
el acoplamiento más allá del orden cuadrático impide controlar la dispersión
lineal por la aproximación usada. La fuente contrasta esto con el modelo L,
con control mejor y dispersión cúbica.

[INFERENCE] Convertir el N-model en puertas locales no elimina por sí mismo
esa dificultad. Para usarlo habría que probar control del sector y de los
errores cuánticos/Floquet adicionales. No se declara imposible construir una
variante ni se traslada su dispersión semiclasica al módulo q=3 comprobado.

Un q fijo finito acredita álgebra finita; no acredita el régimen grande-nG
usado por la fuente. Variar q para buscar un resultado deseado violaría este
preflight. La viabilidad tensorial, incluso a q=3, queda OPEN.

## 6. Estado y siguiente paso concreto

| Elemento | Estado |
|---|---|
| Álgebra de constraints finitos | PASS del certificado propio |
| Existencia de sector en volumen finito | Argumento escrito, sin revisión independiente |
| Tick solo de constraints | Excluido como dinámica no trivial en ese sector |
| Familia de puertas locales en el conmutante | Ruta condicional, puertas dinámicas no seleccionadas |
| Tick completo, referencia IR y espectro | NO_RULE_SPECIFIED / NOT_EXECUTED |
| Dos polarizaciones con z=1, cono común, Einstein | OPEN |

Siguiente pregunta: **¿qué generadores locales del conmutante de S/V producen
dinámica física no trivial y qué mecanismo puede permitir z=1 con control?**
Antes de un espectro hay que especificar ese tick y su sector de referencia.
No basta una identidad de modo continuo o una copia del N-model. Si esa
especificación no puede completarse, se registra el límite en IG1 sin rescatar
W6/CJWW, sin barrido de parámetros y sin proyección TT manual.
