# Pares independientes: filtro algebraico de simetrías

2026-11-06. Codex. Autorización: opción 2, usuario «adelante».
Contrato antes de ejecutar cálculos. No prerregistro Git ni búsqueda
ciega: las posibles consecuencias de Schur y de la conmutación nodal
motivan expresamente este filtro.

Conocido: PHS relaciona sectores conjugados, no pares arbitrarios;
la covariancia espacial puede proteger isotropía condicionalmente.
Fuentes leídas: auditoría de hoy y Asboth 1208.2143v2 Sec. III;
P17 1708.00826v2 p.2. La realización cíclica anterior ha fallado
y no se modifica ni se continúa aquí.

Pregunta: ¿un intercambio interno fijo entre dos pares prohíbe una
diferencia de velocidades sin reducir el problema a copias idénticas?
Corte: si la conclusión es álgebra estándar o requiere copias idénticas,
terminar sin construir QW para rescatar una candidatura de novedad.

## Clase y límites

Filtro LOCAL, no constructor Laurent. d=3, k=0; dimensión s=8,
C²_sigma tensor C²_tau tensor C²_rho, necesaria aquí para representar
dos pares de dobletes. rho distingue candidatos de especie, tau el par
conjugado. No se asigna significado físico a esas etiquetas.

R_j=sigma_j tensor I tensor I (D2),
C=(sigma_y tensor tau_y tensor I)K, fijos. Unidad temporal y
coordenadas comunes. Sin soporte nuevo: no se afirma existencia de
un QW de alcance finito, geometría causal ni velocidades normalizadas
al inradio. La ausencia de una restricción LOCAL es necesaria, no
suficiente, para una perturbación Laurent admisible.

Se comparan SOLO tres condiciones anidadas y fijadas ahora:
1. Mismos R_j,C en ambos candidatos, sin intercambio.
2. Intercambio F=I_4 tensor rho_x, [F,U(k)]=0.
3. Además Z=I_4 tensor rho_z, [Z,U(k)]=0. Ambas conjugaciones
   generan una acción proyectiva de Z2 x Z2 en el factor rho y
   el álgebra completa M2(C). No se elige otro grupo tras el resultado.

Dos situaciones nodales: fases ±theta_1 y ±theta_2 distintas, o
centros coincidentes ±theta, 0<theta<pi. En la primera se comprueba
la restricción espectral al intercambio. En la segunda se permite
mezclar rho; no se conserva rho_z como etiqueta dinámica salvo que
se imponga explícitamente Z. Se exige distinguir etiquetas y modos
propios de propagación.

Perturbaciones del filtro: derivadas Hermíticas J_i=i W† partial_i U
compatibles con las representaciones fijadas y nodos separados de
sus conjugados. Para probar insuficiencia LOCAL del intercambio se
examina un único término permitido proporcional a rho_x en un cono
isótropo no inclinado. No se construye su exponencial como QW finito.

Excluidos: cambios de marco temporal, desplazamientos de quasienergía,
simetrías dependientes de k, nodos en momentos diferentes, interacción,
selección dinámica, masa física, búsqueda de modelos o promoción.
Una simetría espacial que deje k=0 fijo debe conservar sus autoespacios
de fase; esto no excluye acciones que intercambien nodos distintos.

## Salida y comprobación

Derivación por bloques y segunda vía por espectros/conmutantes.
Script permanente scripts/verify_independent_pairs_symmetry.py;
informe reports/2026-11-06--independent-pairs-symmetry.md.
Antecedente de Schur: original docente del autor, Peter Woit,
Quantum Theory, Groups and Representations, Sec. 2.1, leído antes
de atribuir la conclusión. Sin novedad salvo diferencia concreta
acreditada, sin revisión externa. Una sesión acotada; terminar al
resolver estas tres condiciones, sin añadir grupos sucesores.
