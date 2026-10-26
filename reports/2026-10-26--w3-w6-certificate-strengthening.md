# Refuerzo de certificados W3–W6 — opción 2

Fecha: 2026-10-26. Autor: Codex. Base: `1ccf78d`, tras completar la opción 1.
Autorización directa: «1 y después 2». No se envió texto a terceros.

## Qué cambia

Las obligaciones de certificados de la revisión del 22 de octubre se han
implementado en los verificadores existentes. Se conserva el alcance reparado:
transporte semiclasico de primer orden, identidad local exacta de la fuente,
retroacción de campo medio y redundancia de frame cinemática.
Los nuevos bytes no heredan la revisión independiente de versiones anteriores.

El código compartido permanente está en `scripts/tetrad_transport.py`.
Desde el operador de salto orientado forma `i(T_d-T_d^dagger) sigma_a`, con
símbolo de T igual a `exp(-ip·d)`. La derivada de cada exponencial local en
g=0 es su generador. Como cada puerta vale identidad allí, la derivada de
cualquier producto de capas es la suma de esas derivadas. Las dos paridades
reúnen todos los enlaces de una familia, dando el símbolo uniforme al primer
orden aunque cada capa aislada tenga celda duplicada.

El código multiplica ese primer orden por `walk2()` de CJWW y extrae E con
la traza de Pauli de la derivada en momento. Ya no define E para después
comprobar solo propiedades de esa misma definición. El resultado se compara
con la fórmula contractual, incluida una prueba negativa de signo.
No se calcula el logaritmo de Floquet completo ni un cierre para estados
entrelazados; el producto de capas a orden finito no se sustituye por una
exponencial exacta del símbolo sumado.

## W3

`verify_w3_backreacting_tetrad.py` deriva la matriz E desde las tres corrientes
y el paso plano. Conserva la rotación exacta de Z y la pendiente para entrada
producto. La sustitución de las medias actualizadas en E comprueba solo el
término de campo medio de orden g²; las correlaciones del mismo orden no
quedan certificadas ni se omiten como si fueran cero. Cuatro bloques PASS.

## W5

`verify_w5_tetrad_source.py` comprueba las tres matrices de Pauli y sus tres
direcciones, las derivadas en cada momento y la variación del generador de
transporte respecto a cada media z. Se deriva `dH_transport/dz = g J`.
El signo contrario se rechaza como control negativo.

Para la identidad local se usan dos extremos y un sitio espectador. Así el
espectro de J incluye cero además de más y menos uno. Se comprueban
`J^2=A`, `J A=J`, la exponencial exacta del kick, unitariedad y su generador.
La conjugación de Z da la identidad operatorial completa con A y J.
Su derivada es `-2 X tensor J`. Trazarla contra factores independientes
recupera `-2 x <J>`; para estados correlacionados se conserva la expectativa
conjunta `-2 <X tensor J>`, sin factorizarla.

Cuatro bloques PASS: uno por familia y otro para la expectativa producto.
No se deriva aquí un tensor de estrés-energía conservado ni una identidad Ward.

## W6 F1, F5 y F6

- **F1:** todas las puertas R y T valen identidad en g=eta=0; las K de geometría
  pueden seguir siendo no triviales. El paso es entonces `K_total tensor U_CJWW`.
  El conjugado de cualquier observable de materia por una puerta K de geometría
  es el mismo observable: se comprueba en una base de coin, y la identidad
  tensorial vale para cualquier dimensión de materia. Al componer puertas K
  esto sigue siendo cierto. La traza parcial da por tanto el canal CJWW también
  cuando se conserva la evolución de geometría. Un kick con eta no nulo cambia
  un observable de posición en el control negativo: no basta apagar g.
- **F5:** se deriva la matriz tetrádica desde las nueve corrientes (a,r),
  y se varía el generador respecto a cada uno de los nueve z. La identidad
  exacta del kick se comprueba para las tres matrices locales distintas; r
  solo determina dónde se embebe el mismo operador de dos extremos y el
  símbolo espacial, comprobado para los nueve pares. La fórmula de producto
  de medias exige entrada separada o aproximación de campo medio.
- **F6:** la puerta K deja exactamente fijo cualquier par de estados idénticos
  y en kappa=pi/2 traslada un defecto completamente. Las nueve especies son
  factores distintos; la construcción se aplica a cada una. Es un testigo de
  transporte geométrico, no una demostración de onda del métrico, modo relativista
  o gravitón. Las precisiones del espectro W4 siguen vigentes.

Se conservan además los rangos 9/6 y el núcleo de dimensión tres, para g no
nulo. El verificador W6 imprime once bloques PASS, incluidos los de calendario
y dos controles negativos. La identidad del paso completo no se reemplaza
por `I_geometry tensor U_CJWW` cuando K está activa.

## Calendario explícito de profundidad acotada

`scripts/w6_schedule.py` proporciona el siguiente testigo conservador. Todos
los índices a,r recorren 1,2,3 en orden lexicográfico; las paridades son 0 y 1.
El registro `(a,r,x)` corresponde al enlace con ancla x y dirección d_r.

| Bloque temporal | Capas | Puertas de una capa |
| --- | ---: | --- |
| R: recorrer a,r y paridad de x1 | 18 | Kick en todos los enlaces `(x,x+d_r)` de esa paridad y especie |
| T: mismo recorrido | 18 | Transporte en esos mismos enlaces |
| K: recorrer a,r, eje j y paridad de xj | 54 | Intercambio entre registros de la misma especie con anclas x y x+e_j |
| Total de interacción añadida | 90 | Profundidad independiente del volumen |

En cada capa de materia d_r tiene primera componente uno. Si dos enlaces
distintos de una familia comparten extremo, sus anclas difieren en más o menos
d_r y tienen paridad opuesta. Por tanto las anclas de una misma paridad dan
un matching. Cada enlace aparece una vez al reunir las dos paridades.
El mismo argumento, con el eje j, prueba los matchings de geometría.
Esto demuestra el resultado en la red infinita y en toros pares sin
identificaciones degeneradas de vecinos (lado al menos cuatro).

Como segunda vía, el verificador comprueba todos los soportes y la cobertura
en toros de lado cuatro y seis: 2880 y 9720 puertas etiquetadas, respectivamente,
repartidas en las 90 capas. Rechaza un calendario al que se quite una capa.
Las cajas son controles finitos del calendario; la prueba de todos los tamaños
es el argumento de paridad anterior, no una extrapolación de esas cajas.

Se serializan especies, aunque los factores geométricos distintos permiten
paralelismo. Es una cota conservadora, no una profundidad mínima. El orden R,
T, K da un testigo compatible con las puertas declaradas y completa un detalle
que el registro W6 no fijaba explícitamente. No demuestra independencia del
orden a acoplamiento finito ni identifica retrospectivamente una secuencia
única de la ejecución histórica. Los rangos y jets de primer orden comprobados
no dependen de ese orden cuando las demás puertas están apagadas.
Las puertas K de distintas especies conmutan, por lo que serializarlas no
cambia el producto geométrico que se podría aplicar en paralelo.

Las 90 capas son **solo la interacción añadida**. El paso CJWW se aplica antes;
su síntesis completa en el modelo de circuitos QCGD no se obtiene aquí.
No se cambia coeficiente, dirección, tipo de registro ni regla de acoplamiento.

## Reproducción y provenance del barrido

```sh
python3 -B scripts/verify_w3_backreacting_tetrad.py
python3 -B scripts/verify_w5_tetrad_source.py
python3 -B scripts/verify_w6_full_spatial_tetrad.py
python3 -B scripts/run_all_verifiers.py --output reports/2026-10-26--strengthened-verifier-sweep.tsv
sha256sum -c reports/2026-10-26--strengthened-verifier-inputs.sha256
python3 -B scripts/test_text_integrity.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

El barrido completo termina con **42 verificadores, cero fallos**. El TSV
registra Python, SymPy, NumPy, tiempos y últimas líneas. Su git_head es la base
`1ccf78d`, porque se ejecutó sobre los archivos reforzados antes de su commit;
el manifiesto SHA256 identifica exactamente los tres verificadores modificados
y sus dos módulos nuevos. El resto de código no cambió respecto a esa base.
El manifiesto se comprobó después del barrido. No se ejecutó código científico
temporal. Las entradas de los tres verificadores se añadieron a scripts/README.

## Cierre de la opción 2

Las obligaciones de implementación de certificados y calendario quedan
cubiertas al alcance anterior, con comprobación local del autor y sin nueva
revisión independiente de estos bytes. La ejecución correcta no certifica
gravedad física, novedad, conservación de estrés-energía, cierre después de
entrelazamiento ni síntesis completa del paso CJWW. No se adopta la reparación
espectral W4 como modelo ni se abre un contrato de investigación nuevo.
W1–W12 permanece cerrado por contrato.
