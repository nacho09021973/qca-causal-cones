# Intento s=4 con giro cíclico: contrato de comprobación

2026-11-06, Codex. Usuario: «realizamos s=4 a ver que ocurre?».
Autorización de un intento matemático separado de selección y novedad.
La candidata se identificó en el razonamiento previo: no se declara
prerregistro de descubrimiento ni prerregistro Git. Se fija antes de
ejecutar su verificador; hash y hora se conservarán en el informe.

Conocido: forma local provisional D2+C en el informe del 2026-11-05;
la realización con covariancia espacial adicional sigue abierta.
Pregunta: ¿el candidato siguiente realiza dos conos isotrópicos conjugados
en un walk exacto irreducible con simetría espacial cíclica?

## Datos fijos

- s=4, d=3, una actualización de duración 1; longitudes en las mismas
  unidades que el soporte previo N3={±1}^3/sqrt(3).
- N3 es soporte PERMITIDO; se calculan todos los coeficientes y su soporte
  real. No se exige que los ocho sean no nulos. Si hay cancelaciones, no
  se afirma realización con hull cúbico exacto ni pertenencia a una clase
  que exija los ocho saltos. No se renormalizan las longitudes después.
- Red generada por los pasos: coordenadas enteras de igual paridad,
  escaladas por 1/sqrt(3). Se comprobará con el soporte real.
- R_j=sigma_j tensor I; V=sigma_y tensor tau_y, C=VK.
- t=(I-i(sigma_x+sigma_y+sigma_z))/2, S=t tensor t; giro espacial
  rho:(kx,ky,kz)->(kz,kx,ky). Grupo espacial generado por D2 y rho
  (tetraédrico propio). Representaciones fijas, independientes de k.
- G_i=sigma_i tensor tau_i; n=(1,1,1)/sqrt(3);
  W=I tensor exp(-i*pi*(n.tau)/4).
- U(k)=W product_{i=x,y,z}[cos(ki/sqrt(3)) I4
  -i sin(ki/sqrt(3)) G_i], orden xyz fijo.
- Nodos en k=0: fases ±pi/4, cada una con multiplicidad dos.
  Irreducibilidad: conmutante común de todos los coeficientes escalar.

## Obligaciones y corte

Comprobar unitariedad Laurent exacta, soporte tras cancelaciones, C,
covariancia D2 y S coeficiente a coeficiente, nodos y pendientes,
irreducibilidad. Segunda vía para pendientes: eigenfases axiales frente
a compresión del término lineal. Computar cuerpo causal, soporte e
inradio reales, sin inferir cuerpo estricto asintótico.

Robustez solo relativa a perturbaciones unitarias de soporte permitido que
preserven las representaciones, la separación nodal y pendientes no nulas;
no se exige isotropía como condición independiente. No se promete que haya
deformaciones arbitrarias con ese soporte.

Una sola candidata; hasta 90 minutos desde el registro previo al cálculo.
Abandono de esta realización si falla una identidad exacta, hay conos
degenerados o reducibilidad. No cambiar moneda, grupo, soporte permitido
ni dimensión para salvarla. Un fallo de candidata no prueba imposibilidad
de la clase. Salidas: REALIZED_WITH_ACTUAL_SUPPORT / CANDIDATE_FAIL /
OPEN_WITH_NAMED_OBLIGATION. Todo resultado queda PRELIMINARY, sin revisión
externa, promoción, novedad, selección, commit o push.
