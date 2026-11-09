# Realización cíclica: un único intento

2026-11-06. Codex. Autorización directa: «autorizada opcion 1».
Contrato escrito antes de ejecutar el verificador. Sin prerregistro Git.
El posible fallo por orden de factores ya está advertido en el plan y en
la auditoría de hoy; no se presenta como descubrimiento ciego.

Conocido: la forma D2+C permite un cono común anisótropo; una covariancia
que permute los ejes y conserve los dobletes forzaría isotropía lineal.
Fuentes: informes 2026-11-05--common-cone-symmetry-normal-form y
2026-11-06--symmetry-common-cone-premise-audit; antecedentes primarios
indicados allí. El argumento local es estándar, sin candidatura de novedad.

Pregunta única: ¿la candidata siguiente realiza EXACTAMENTE las dos
simetrías y dos conos isotrópicos en una dinámica irreducible?

## Datos congelados

- d=3, s=4, base sigma tensor tau, una actualización por unidad temporal.
- Soporte permitido N3={(±1,±1,±1)/sqrt3}; grupo generado por N3,
  isomorfo a Z³ (BCC), mismas coordenadas y normalización del repo.
- a=3/5, b=4/5, T=b tau_x+a tau_z, G_i=sigma_i tensor T.
- W=I tensor exp(-i pi tau_z/4), P=I tensor (I+tau_z)/2, Q=I-P.
- U(k)=W E_x(q_x) E_y(q_y) E_z(q_z), E_i(q)=cos(q)I-i sin(q)G_i,
  q_i=k_i/sqrt3. Orden xyz fijo. Es la única candidata del intento.
- R_j=sigma_j tensor I para semigiros D2; C=V K,
  V=sigma_y tensor tau_y, C²=I, V U(k)* V†=U(-k).
- Nueva representación fija S=s tensor I,
  s=(I-i(sigma_x+sigma_y+sigma_z))/2; r e_x=e_y, r e_y=e_z,
  r e_z=e_x. Objetivo S U(k) S†=U(r k). Grupo espacial generado
  por D2 y r: tetraédrico propio A4; representación interna proyectiva.
  No se confunde con una rotación continua ni con la simetría del cuerpo.
- Nodos locales en k=0: fases ±pi/4, rango dos cada una. Se exige
  cono no inclinado, isotrópico y no degenerado en ambos sectores.
- Irreducibilidad: conmutante constante de todos los coeficientes
  Laurent exactamente C I. No se exige irreducibilidad del nodo local.
- Robustez buscada, SOLO si pasa: perturbaciones pequeñas de los
  coeficientes en N3, unitarias para todo k, con R_j,S,C fijos. No
  se impone isotropía como condición de admisión. Se mantienen fases
  separadas y se comprueba supervivencia de los nodos por las simetrías.

## Método y cierre

Álgebra exacta; sin barridos. Convolución de proyectores (I±G_i)/2:
soporte efectivo, unitariedad Laurent, simetrías por coeficientes,
nodos, compresiones y conmutante. Segunda vía para la condición decisiva:
una sección bidimensional exacta o derivada mixta, además de coeficientes.
Código permanente en scripts/verify_cyclic_common_cone_realization.py;
resultado y provenance en reports/2026-11-06--cyclic-common-cone-realization.md.

Salidas: PROTECTION_IN_NONEMPTY_CLASS para esta candidata si pasa todo;
CANDIDATE_FAILS_<condición> con obstrucción exacta; o
OPEN_WITH_NAMED_OBLIGATION si no se completa la comprobación.

Abandono de esta ruta de construcción: si falla una simetría exacta o la
irreducibilidad, terminar con ese fallo; no cambiar orden, soporte,
representación, dimensión o factores para eludirlo. Un fallo de esta
candidata no demuestra imposibilidad para todos los símbolos Laurent de
N3. No búsqueda sucesora, selección dinámica, escala física, novedad,
revisión externa ni promoción implícita. Límite: una sesión, hasta 90 min.
