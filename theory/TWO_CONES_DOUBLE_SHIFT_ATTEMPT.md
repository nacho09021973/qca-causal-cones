# Segundo par de conos: arquitectura de doble desplazamiento

2026-11-05. Codex. Usuario: «podemos hacerlo con otro par y otra estructura».
Nuevo intento autorizado, distinto del contrato anterior que terminó sin
añadir factores. No se modifica aquel contrato. SHA256 antes del cálculo;
no se reivindica prerregistro Git.

Conocido: COMMON_SPEED_S4_PRODUCT_ATTEMPT obliga a igual velocidad en la
arquitectura de tres involuciones si ambos dobletes son isotrópicos y sin
inclinación. Pregunta: ¿ocurre lo mismo con dos desplazamientos por eje?

Clase fijada: d=3, s=4, coordenadas crudas enteras; un update por unidad de
tiempo. Pauli sigma en primer factor y tau en segundo. P=I tensor
(I+tau_z)/2, Q=I-P, W=(exp(-i pi/4)P+exp(i pi/4)Q).
Se toma a=3/5, b=4/5,
T_x=b tau_x+a tau_z, T_y=b tau_y+a tau_z, T_z=-b tau_x+a tau_z,
G_i=sigma_i tensor T_i, L_i=sigma_i tensor I.
U(k)=W prod_(i=x,y,z)[exp(-i k_i G_i) exp(-i k_i L_i)].
Representación D2 fija: R_j=sigma_j tensor I. Nodos k=0 en los dos
dobletes de W; espectros lineales exigidos ±c_P |k|, ±c_Q |k|.
El soporte candidato está en {-2,0,2}^3; se determina exactamente F.
Normalización final por la longitud máxima real del soporte, sin alterar
la unidad temporal. Grupo de traslación generado por F, no por subpasos.

Método: polinomios de Laurent exactos, compresiones nodales y segunda vía
mediante polinomio característico o caso axial. Comprobar unitariedad,
soporte, D2, isotropía, ausencia de inclinación y conmutante escalar de
todos los coeficientes. No basta comparar dos bloques desacoplados.

Salidas: TWO_UNEQUAL_CONES / TWO_EQUAL_CONES / OPEN_FAILED_OBLIGATION.
No buscar más parámetros tras decidir este punto racional. No reclamar
estabilidad alrededor del modelo anterior, universalidad, soporte
asintótico, identificación con especies físicas ni novedad. Detener la
línea en este testigo o fallo; cualquier ampliación se propone aparte.
