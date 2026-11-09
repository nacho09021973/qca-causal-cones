# Moneda general U(4), desplazamiento tetraédrico fijo

2026-11-06. Codex. Usuario «adelante» a la ampliación mínima propuesta.
Nuevo contrato; no modifica el de la realización cíclica.

Conocido: G_i=sigma_i tensor tau_i conmutan y tienen cuatro proyectores
conjuntos E_h de rango uno, h en {±1}^3 con producto -1. El constructor
anterior realiza c=1/3. Fuente local: informe s4-cyclic-realization del
2026-11-06, evidencia de autor PRELIMINARY.

Pregunta: para U(k)=W product_i exp(-i k_i G_i/sqrt(3)), con W cualquier
U(4), ¿existe un doblete espectral en k=0, separado del resto del espectro,
con cono lineal isotrópico no degenerado, sin inclinación y c distinto de
1/3? El doblete tiene multiplicidad exactamente dos. No se exige nada
sobre la multiplicidad de los otros dos eigenvalores, salvo su separación
respecto al doblete. No se imponen D2, C, S ni una factorización de W.

Se fijan s=4, soporte tetraédrico F={h/sqrt(3): producto h_i=-1}, longitud
de paso uno, duración uno, nodo k=0. Todos los A_h=W E_h son no nulos
para W unitario. Se exigiría conmutante escalar para aceptar un testigo.
No se cambian desplazamientos, unidades, nodo ni dimensión.

Método primero algebraico: comprimir los E_h al doblete. La posible
exclusión por rango de esas compresiones se ha advertido en el razonamiento
previo; no se declara prerregistro de descubrimiento ni de Git. Registrar
hash antes de ejecutar un verificador permanente.

Para una isometría T:C²->C⁴ del doblete, H_i=T†G_i T/sqrt(3).
Sin inclinación significa tr H_i=0 para todo i. Isotropía significa
tr(H_i H_j)/2=c² delta_ij, con c>0, no solo igualdad de tres cortes.

Cierre: un testigo exacto verificable; una exclusión algebraica para toda
la clase; o una obligación concreta OPEN tras una sesión de hasta 90 min.
Abandono de esta vía si las restricciones fuerzan c=1/3. Una búsqueda
fallida no prueba exclusión. No acoplamiento s=8, barridos, interacción,
selección, revisión externa, promoción, commit ni push.
