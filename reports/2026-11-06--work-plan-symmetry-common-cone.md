# Plan de trabajo — 6 de noviembre de 2026

Redactado el 2026-11-05 por Codex, a petición del usuario.
Base de continuidad: 6f96b93616cd92e60d8484d54bdd4752e54bccff,
research/schur-stability-audit. Comprobar HEAD y CURRENT_STATE al reanudar.
Plan de investigación, no resultado, promoción ni ejecución anticipada.
No es una tarea programada ni un envío autorizado a modelos externos.

## Intuición que guía el trabajo

La isotropía y la universalidad observadas podrían proceder de una
selección dinámica de estructuras que protegen un cono común con poco
ajuste fino. La intuición del usuario es que la simetría puede ser una
estructura favorecida por el funcionamiento del sustrato.

Es una hipótesis de orientación. No se presupone que todo minimice energía,
que minimizar energía implique mayor simetría, o que exista una simulación
subyacente. Se mantienen separadas tres cuestiones:

1. Protección: qué simetrías obligan a compartir un cono y a ser isotrópico.
2. Selección: qué proceso, si existe, conduce hacia esas condiciones.
3. Escala: qué fija el valor común de c y las unidades físicas.

La sesión se centra en 1; solo localiza candidatos documentales para 2.
No promete resolver 3.

## Punto de partida comprobado en el repo

- CURRENT_STATE, entradas del 5 de noviembre: todos los resultados recientes
  siguientes son PRELIMINARY, sin revisión independiente ni novedad acreditada.
- reports/2026-11-05--common-cone-symmetry-normal-form.md: con s=4,
  R_j=sigma_j tensor I y C=(sigma_y tensor tau_y)K, D2+C elimina los
  términos d_i sigma_i tensor I. Los dobletes conjugados tienen la misma
  dispersión lineal en magnitud. No fuerza isotropía ni relaciona especies
  independientes. La forma local no prueba realización por un QW finito.
- reports/2026-11-05--local-particle-hole-two-cones.md: C existe en el
  constructor original y no en el de doble desplazamiento, para la clase
  local fijada y los puntos comprobados.
- reports/2026-11-05--two-cones-double-shift.md: dos conos de velocidades
  diferentes dentro de un modelo irreducible. No se necesita otra tabla
  para volver a mostrar que D2 y localidad no bastan.
- La tabla de cinco parámetros reproduce una fórmula del constructor:
  no es evidencia nueva de una ley. No continuar barridos de esa familia.

## Objetivo cerrado de la sesión

Decidir si una extensión microscópica precisa de las simetrías actuales
puede proteger simultáneamente emparejamiento e isotropía a primer orden,
sin fijar a mano las pendientes y sin reducirse a dos copias independientes.
Separar rigurosamente:

- condición algebraica local;
- existencia de al menos un QW unitario de alcance finito que la realice;
- robustez relativa a las perturbaciones que conservan la simetría;
- posible novedad respecto a clasificación y teoría de representaciones.

Presupuesto propuesto: una sesión de hasta cuatro horas. Los tiempos son
límites de trabajo, no promesas de hallar un resultado. Cada corte detiene
la etapa dependiente; el tiempo sobrante no abre otras líneas.

## Secuencia de trabajo

### 1. Reentrada y auditoría de la premisa — 30 minutos

Leer PROJECT_INSTRUCTIONS y CURRENT_STATE, los tres informes anteriores y
el índice de biblioteca. No repetir verificadores si los archivos y hashes
coinciden y no hay una duda nueva. Rehacer a mano los pasos delicados:
transformación antiunitaria de J_i, aislamiento nodal y significado de
"misma dispersión" frente a "misma c isotrópica".

Pregunta: ¿podemos usar la forma normal como premisa provisional fiel?
Corte: cualquier error sustantivo obliga a reparar antes de extenderla.
Salida: lista breve de premisas válidas y obligaciones pendientes. La
autocomprobación no sustituye revisión de otra familia o humana.

### 2. Novedad y comparación primaria — 45 minutos

Comenzar por biblioteca/INDICE.md. Leer pasajes pertinentes de:
Asboth 1208.2143 Sec. III (PHS y operador fijo), D'Ariano–Erba–Perinotti
1708.00826 (qué isotropía exige su clasificación), Arrighi–Facchini
1609.00305 (libertad de velocidades y compresión). Localizar originales
adicionales solo para resolver la comparación concreta, no un catálogo.

Pregunta: ¿el enunciado propuesto es ya un corolario inmediato conocido?
Corte: si solo reformula el emparejamiento por PHS más una aplicación
directa de irreducibilidad, cerrar su candidatura de novedad. Puede
conservarse como explicación pedagógica, sin abrir modelos para salvarla.
Salida: por afirmación, fuente, página/ecuación y diferencia restante;
"no localizado" no significa "nuevo". No usar informes de IA como fuentes.

### 3. Elegir y congelar UNA condición adicional — 30 minutos

Candidata inicial: una simetría espacial que relacione las tres direcciones,
con representación interna fija, además de C. Un giro cíclico de ejes
es una posibilidad que debe estudiarse, no una condición ya adoptada.
No confundir simetría de C_micro, isotropía del término lineal y covariancia
exacta de U. El orden de los subpasos puede romper la última.

Antes de calcular, redactar un charter separado: dimensión s=4, soporte
finito, grupo generado, unidad temporal, representación de cada generador,
nodos y perturbaciones permitidas. No cambiar estos datos después de ver
la respuesta. Usar un soporte ya declarado; cambiarlo requiere registrar
por qué y una nueva decisión, no otra normalización silenciosa.

Pregunta: ¿la nueva simetría tiene significado microscópico independiente
y admite una representación compatible con C y los dobletes?
Corte: si equivale a postular c_x=c_y=c_z o exige dos copias desacopladas,
no aceptarla como explicación. Si la representación es incompatible,
registrar el fallo sin pasar a una cadena de grupos alternativos.

### 4. Prueba y realización exacta — hasta 90 minutos

Solo si sobreviven las etapas anteriores. Derivar qué términos lineales
prohíbe la simetría completa. Después comprobar UNA realización de alcance
finito: unitariedad para todo k, soporte real con cancelaciones, nodo,
covariancia, C e irreducibilidad. Un Hamiltoniano efectivo admisible no
garantiza por sí mismo un símbolo Laurent unitario con el soporte fijado.

La robustez buscada es relativa a perturbaciones que preservan las
simetrías microscópicas. Conservar la isotropía como condición de admisión
no cuenta como demostrar que una simetría la protege.

Comprobación por segunda vía: eigenfases axiales y relaciones cuadráticas
del término lineal, o caso límite exacto; sin barridos ni ajustes.
Todo script científico debe quedar permanente en scripts/ y su registro
en reports/. No crear código científico efímero.

Cortes: (a) hay un término permitido que rompe el objetivo; (b) la prueba
requiere una hipótesis extra no fijada; (c) falta realización exacta al
agotar el presupuesto. Distinguir fallo lógico, obstrucción demostrada e
inconclusión. No inferir imposibilidad por una búsqueda fallida.

### 5. Selección dinámica: solo diagnóstico — 20 minutos

Preguntar qué variable cambiaría: estado, parámetros de actualización,
geometría o descripción efectiva al cambiar escala. Son problemas distintos.
Identificar, si hay fuente primaria pertinente, UN mecanismo y su objeto:
relajación, flujo efectivo o adaptación con regla propia.

No basta promediar monedas o estados hasta hacerlos simétricos: hay que
comprobar qué dinámica resulta y si sigue siendo el QCA de la clase.
La evolución unitaria microscópica por sí sola no suministra un argumento
de atracción de sus propios parámetros hacia una regla más simétrica.

Corte: si no hay ley de evolución de esa variable y cantidad o criterio
de selección definido, dejar SELECTION_MECHANISM_NOT_SPECIFIED. No
inventar una energía de la simetría o un coste para obtener el resultado.
Abrir interacción, entorno o geometría dinámica requeriría un sucesor
charter: esta etapa no los autoriza ni los calcula.

### 6. Cierre documental — 25 minutos

Un informe breve: resultado exacto, hipótesis completas, antecedente más
cercano, prueba o gap y decisión. Actualizar CURRENT_STATE solo con lo
hecho. Separar: protección de un par conjugado, isotropía, universalidad
entre pares y selección dinámica. Las dos últimas no se heredan de las
primeras. No promoción por un PASS local; revisión externa solo con
permiso explícito y por los lanzadores canónicos.

## Qué constituiría un buen cierre mañana

- PROTECTION_IN_NONEMPTY_CLASS: condición independiente, argumento y
  realización exacta; novedad evaluada por separado.
- STANDARD_SYMMETRY_COROLLARY: explicación correcta ya contenida en
  teoría conocida; cerrar candidatura de artículo original por esa vía.
- LOCAL_CONDITION_WITHOUT_REALIZATION: forma local, sin modelo exacto;
  obligación abierta, no resultado físico completo.
- OPEN_WITH_NAMED_OBLIGATION: presupuesto agotado con el obstáculo preciso.
- SELECTION_MECHANISM_NOT_SPECIFIED puede acompañar cualquiera de los
  anteriores: no invalida una protección, pero impide afirmar selección.

Abandono de la hipótesis fuerte como ruta de trabajo: si solo se obtiene
simetría imponiéndola, o todos los enunciados restantes son aplicaciones
inmediatas conocidas y no hay mecanismo independiente de selección,
terminar esta ruta. No implica refutar todas las ideas de emergencia.

## Instrucción de reanudación

«Lee reports/2026-11-06--work-plan-symmetry-common-cone.md y el estado
canónico. Empieza por las etapas 1 y 2. No abras cálculos nuevos antes
del charter de la etapa 3. Mantén aparcada la línea hexagonal y conserva
la distinción entre protección, selección y valor de c.»
