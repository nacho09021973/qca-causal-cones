# A.int — candidato materia–gauge con proyección de Gauss

Fecha: 2026-10-27. Autorización nueva: «hazlo», al requisito de un estado
explícito con Gauss, estacionariedad y criterio de selección física.
No sustituye ni reescribe los rechazos de candidatos anteriores.
Especificación escrita antes de ejecutar el certificado de esta ronda.

## Regla microscópica que se conserva

Eon arXiv:2205.03148v4, ecuaciones (34)–(37). Toro cúbico L=3,
epsilon=1, m=pi/4, g_E=g_M=1; rotores enteros sin truncar.
Magnetismo exponencial exacto (21), orden de (36), seguido en la fórmula
`U=D_M D_E D_F`. Sector `G_x=div E_x+N_x-2=0`.
No se reemplaza U por la exponencial de un Hamiltoniano auxiliar.

## Candidato fijado

Se introduce explícitamente un **criterio auxiliar de preparación**, no
una energía conservada derivada del QCA:

`h_D(k)=m gamma_0 - sum_a sin(k_a) gamma_a`;
`P_-(k)=[I-h_D(k)/sqrt(m²+sum_a sin²(k_a))]/2`.

Los gamma son los de p.24 del PDF. El Slater |FS_D> ocupa las dos bandas
negativas en cada momento del toro. Es el mínimo de la energía fermiónica
aditiva de ese h_D a número total 2V. El criterio coincide con Dirac a
primer orden en momento; su extensión ultravioleta es una hipótesis
auxiliar explícita, no la energía exacta del paso ni un resultado de Lorentz.

Se fija beta=log(2). En cada enlace, el vector de rotor normalizado es
`|g_beta> = [sum_l exp(-2 beta l²)]^(-1/2) sum_E exp(-beta E²)|E>`.
Los V de las ecuaciones (4)–(6) fijan la base de traslaciones de rotor;
las posibles fases de su implementación JW se mantienen mediante esa
elección de base. No se presume un producto de fases incorrecto en otra
representación. La regla de evolución sigue siendo la original.

Sea P_G el proyector ortogonal conjunto sobre todos los G_x=0. El estado es

`|Omega_beta> = P_G (|FS_D> tensor tensor_links |g_beta>) / sqrt(Z)`;
`Z=||P_G (|FS_D> tensor tensor_links |g_beta>)||²`.

Equivalente en la base de ocupaciones y flujos: el coeficiente es
proporcional a `det(FS_D[n]) exp(-beta sum_links E²)` si
`div E=2-N[n]`, y cero en caso contrario. Los determinantes del subespacio
ocupado definen el Slater salvo una fase global. El orden de sitios es
lexicográfico y el de modos es 0,1,2,3.

La proyección entrelaza materia y flujo, conserva el número total y no
identifica medias locales con autovalores de Gauss. El peso gaussiano es
una preparación por amortiguamiento eléctrico; **no se afirma que sea
el fundamental del QCA ni de su logaritmo principal**.

## Comprobaciones y criterio de cierre

1. Demostrar Z>0 y normalización, existencia de soluciones enteras de
   Gauss para cada configuración neutral y energía eléctrica esperada finita.
2. Contrastar por segunda vía el criterio de bandas auxiliares y un
   control explícito de dos configuraciones de carga con bucles de flujo
   infinitos. Cualquier corte para verificar ese control necesita cota de
   cola y no se convierte en una truncación del modelo.
3. Comprobar estacionariedad para U completo. Puede usarse una obstrucción
   analítica de clases de colas eléctricas si se demuestran sus hipótesis:
   tras D_F y D_E una cota gaussiana sigue siendo gaussiana; D_M se
   diagonaliza con los V conmutativos como una exponencial de cosenos de
   plaqueta. No confundir la prueba analítica con verificaciones finitas.
4. Si falla, declarar que el objetivo de construir un vacío aceptado no
   se ha logrado. No adoptar la preparación auxiliar como cambio de modelo
   ni sustituir el candidato por una mezcla estacionaria.

Código permanente: `scripts/verify_eon_projected_gaussian_reference.py`.
Se conservarán JSON, demostración, manifiesto y barrido de verificadores.
No se calculan velocidades o lazos, ni se reclama novedad o revisión
independiente. La selección auxiliar solo sería un candidato de vacío;
la estacionariedad es un requisito imprescindible adicional.
