# Cono común: auditoría de premisas y corte de novedad

2026-11-06. Codex. Base: b434547, rama research/schur-stability-audit.
Continuación solicitada por el usuario el 6 de noviembre. Ejecuta las
etapas 1 y 2 del plan de hoy y su cierre documental. PRELIMINARY:
autocomprobación, sin revisión independiente ni promoción.

## Pregunta y regla de parada

Conocido: la forma local del informe del 5 de noviembre empareja las
dispersiones de dos dobletes con D2 y una antiunitaria fija, pero deja
libres tres coeficientes axiales. Sus contrato y verificador conservan
los SHA256 registrados, comprobados en esta sesión:

- theory/COMMON_CONE_LOCAL_SYMMETRY_NORMAL_FORM.md:
  5d463aea619d21f2c1e5f1e239126fa350bfa4d3e34ac5ae61150aae8e3c82b6.
- scripts/verify_common_cone_symmetry_normal_form.py:
  16639f7fd11d3e42dd9385db58a373d0b2bb3ca976ec876dc41e973ae35cbf4b.

Pregunta: ¿esa premisa es fiel y su extensión local hacia isotropía ofrece
algo distinto del emparejamiento PHS y la invariancia de una forma
cuadrática? Corte del plan: si solo ofrece esa consecuencia inmediata,
cerrar esa candidatura de novedad y no abrir constructores para salvarla.
No se ha congelado ni ejecutado una clase microscópica adicional.

## 1. Reentrada y auditoría manual

Leídos PROJECT_INSTRUCTIONS, entradas actuales de CURRENT_STATE, el plan,
los tres informes indicados y el intento previo de producto s=4. La carpeta
biblioteca/ no existe en esta copia; no se ha inventado un índice. Se han
usado los PDF primarios de sources/ y el PDF original de Asbóth en arXiv.
No se han repetido verificadores: no hay cambios de los hashes anteriores
ni una duda que justifique repetirlos. Los recuentos históricos no se
presentan como ejecuciones de hoy.

Para W=U(0), D_i=partial_i U(0), V=sigma_y tensor tau_y,
la hipótesis fija V W* V†=W y V D_i* V†=-D_i. Por tanto

    V (i W† D_i)* V† = (-i) W† (-D_i) = i W† D_i.

El signo de i es imprescindible. La identidad Pauli bajo conjugación
por sigma_y cambia el signo de cada Pauli conjugada. Así sigma_i tensor I
es impar y sigma_i tensor tau_j es par. Se conserva la restricción del
informe: J_i=sigma_i tensor (v_i.tau). No se detecta reparación necesaria.

La compresión en P,Q da H_P=sum_i u_i k_i sigma_i y H_Q=-H_P,
con u_i=v_i.n. Segunda vía manual: las relaciones de Pauli dan

    H_P(k)^2 = H_Q(k)^2 = (sum_i u_i^2 k_i^2) I_2.

Esto confirma igualdad de las dispersiones lineales en magnitud, incluso
si son anisótropas. No exige igualdad de los tres u_i^2.

Hay que separar tres obligaciones: las dos fases nodales deben ser
distintas; cada bloque debe tener rango dos; y u_x u_y u_z debe ser no
nulo para un cono tridimensional no degenerado. Con esas condiciones en
un punto, perturbaciones suficientemente pequeñas que mantengan las
simetrías fijas conservan separación y no degeneración por continuidad.
No es estabilidad para perturbaciones arbitrariamente grandes ni prueba
de aislamiento global de todos los nodos en la zona de Brillouin.

## 2. Comparación primaria acotada

Pasajes leídos en esta sesión, sin usar informes de IA como evidencia:

| Afirmación | Original comprobado | Alcance y diferencia restante |
| --- | --- | --- |
| PHS empareja quasienergías opuestas | Asbóth, arXiv:1208.2143v2.pdf p.3, Sec. III.A, Ecs. (10)–(11), https://arxiv.org/pdf/1208.2143v2 | El emparejamiento es antecedente explícito; su modelo es 1D, no nuestro constructor s=4. |
| El operador de simetría debe permanecer fijo en la familia comparada | Mismo PDF p.4, Sec. III.C | Se cumple en la forma local; no se permite reconstruir C desde eigenvectores para cada miembro. |
| Isotropía microscópica requiere covariancia de las matrices de transición | sources/1708.00826v2.pdf p.2, Definición 1 y Ec. (4) | La definición añade transitividad sobre los generadores; no equivale a que la envolvente del soporte sea simétrica. |
| La clasificación citada no clasifica nuestra clase s=4 | Mismo PDF p.3, comienzo de página | Declara s=2 y d=1,2,3. No se extrapola su unicidad a s=4. |
| Una compresión puede dejar libres las velocidades bajo un límite causal | sources/1609.00305v2.pdf p.4, Ecs. (27)–(29); p.6, Sec. V | Construcción de otra clase: no acredita nuestra realización con representación y soporte fijos. |

Las tres fuentes no contienen un teorema identificado aquí que resuelva
la existencia del modelo microscópico adicional. Tampoco se ha hecho una
búsqueda exhaustiva de prioridad.

La extensión LOCAL que motiva el plan tiene una lectura elemental:
la dispersión anterior define la forma cuadrática diagonal
q(k)=sum_i u_i^2 k_i^2. Si una covariancia exacta adicional conserva cada
sector nodal y permuta cíclicamente los tres ejes, su espectro exige
q(k_x,k_y,k_z)=q(k_z,k_x,k_y). Comparar coeficientes fuerza la igualdad
de los tres cuadrados. Es una inferencia algebraica de esta auditoría,
no un teorema atribuido a P17 ni una realización exacta comprobada.
Esta observación condicional no adopta representación nueva, no fija un
soporte y no permite saltar la etapa 3 del plan.

PHS aporta el emparejamiento; la covariancia espacial apropiada aportaría
isotropía. La combinación local es una consecuencia estándar de esas
hipótesis. No demuestra que una actualización ordenada por subpasos posea
esa covariancia: rotar los ejes puede cambiar el orden de factores.

## 3. Decisión y obligaciones

Se activa el corte de novedad de la etapa 2:
STANDARD_SYMMETRY_COROLLARY, referido SOLO al argumento local condicional
anterior. Se cierra su candidatura como resultado original por esa vía.
No es una refutación de la intuición de selección ni una decisión de
abandonar toda investigación de simetrías.

No se ejecutan las etapas 3 y 4 dependientes. No se ha demostrado
PROTECTION_IN_NONEMPTY_CLASS para una simetría ampliada. La obligación
precisa sigue siendo una realización Laurent unitaria de alcance finito,
irreducible, con soporte y representación congelados, que tenga la
covariancia exacta adicional y C fija. No se declara imposible ni cubierta
por la clasificación s=2. La robustez microscópica depende de ella.

Diagnóstico de selección: SELECTION_MECHANISM_NOT_SPECIFIED. En el
problema actual no hay regla de evolución para monedas, parámetros o
geometría ni criterio de selección definido. Los originales leídos no
aportan aquí ese mecanismo. No se introduce uno por analogía energética.

El valor común de c y la igualdad entre pares independientes permanecen
sin resolver. La línea hexagonal sigue aparcada. Los resultados previos
conservan su nivel y alcance. Este cierre no autoriza otra búsqueda,
revisión externa, promoción, commit o push.

Provenance: derivación manual conservada en este informe; inspección por
cat/sed/rg, sha256sum y pdftotext -f/-l -layout sobre los originales
indicados, y lectura del PDF de Asbóth en arXiv. Sin script científico
nuevo, barrido ni cálculo numérico. Verificación documental: git diff
--check; la autocomprobación no sustituye revisión independiente.
