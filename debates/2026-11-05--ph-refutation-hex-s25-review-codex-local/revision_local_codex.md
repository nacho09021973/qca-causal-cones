# Revisión local de S25

2026-11-05. Revisor: Codex (OpenAI). Autor del resultado revisado:
Claude Code (Claude Opus 5.5), según el informe. Solicitada por el usuario:
«puedes revisar tu S25». Revisión con acceso al repo y ejecución local;
no es la entrega del intento sellado anterior, ni una revisión ciega.
No se ha enviado texto a terceros ni se ha consultado otro modelo.

**Dictamen: PASS sobre la no saturación acotada, con una carencia de
cobertura del verificador original subsanada por un chequeo suplementario.**
No propongo ninguna reparación matemática obligatoria. La promoción
queda pendiente de decisión del usuario; CURRENT_STATE no se modifica.

## Entrada y ejecución

HEAD comprobado al cerrar la revisión: 5512a96. Informe:
`reports/2026-11-04--ph-refutation-hex-s25.md`, SHA256
`d3c9a92c9d5b7545945ed940c7da83ca58380e2754bf11a00dfc455acc95f464`.
Leídos el contrato S25, las pruebas Stage A y hex-ceiling, y los
enumeradores y el código T2 importados. El commit `6eb50c1` introduce
solo el contrato; `7e7bf7d` introduce su ejecución posterior.

Antes del cálculo: conocido el lema de rigidez de hex-ceiling §3;
pregunta: si la geometría y las capas de H25 justifican la reducción
a T2; criterio de rechazo: punto omitido, superviviente interior no
anulado o fallo del certificado T2.

Comandos ejecutados, ambos con exit 0:

```
python3 -B scripts/verify_ph_refutation_hex_s25_gate.py
python3 -B scripts/verify_hex_s25_review.py
```

Salidas completas en `review_original_stdout.txt` (14/14) y
`review_geometry_stdout.txt` (13/13), en esta carpeta. El primero incluye
T2 4/4 y controles cuadrados 5/5. No se ejecutó un solver nuevo para S25;
la repetición original sí recalcula la base de Gröbner del caso T2.

Hashes comprobados de los cuatro módulos originales: S25 `ddf85386…`,
Stage A `ef4b0114…`, B19 `244bb106…`, ceiling `8f3b7a10…`, coincidentes
con el informe. Su contenido no se modificó. Nuevo chequeo permanente:
`scripts/verify_hex_s25_review.py`, SHA256
`010fa7fb805710baa80932a2538195c28041de741434a2e0cf05877d6ac09b7a`.

## 1. Soporte — PASS con complemento de cobertura

Recalculado sin importar el enumerador original. En coordenadas enteras
`h=a*g1+b*g2`, el hexágono no normalizado es

    |2a+3b|<=7, |-a+2b|<=7, |3a+b|<=7.

Las tres formas son las proyecciones normales divididas por
`delta=sqrt3/14` después de normalizar por sqrt7. El radio circunscrito
sqrt7 implica |a|,|b|<=2*sqrt(7/3)<4, así que enumerar [-3,3]^2 es
exhaustivo. Resultan 25 puntos y seis vértices; las capas extremas
contienen solo los dos vértices de cada arista. No hay punto de red
interior a una arista. Esto también justifica que la caja [-5,5]^2 del
enumerador original no omite puntos en este caso.

La reflexión y->-y es (a,b)->(a+b,-b); lleva la órbita de (2,1) a la
de (1,2). No se presupone una simetría especular de H25 consigo mismo.

**Carencia original:** el contrato §2 pide certificar que los únicos
hexágonos centrados menores contenidos son S7, S13 y S19.
`check_support()` del verificador original no comprueba esa lista.
El nuevo chequeo enumera todas las órbitas de vértices posibles, comprueba
contención por convexidad y cuenta los puntos de cada hull por productos
cruzados: exactamente 7, 13 y 19. La carencia queda cubierta en el
expediente de revisión, sin cambiar el archivo congelado ni el verificador
original. Esta lista no es necesaria para la exclusión con hull exacto H25.

## 2. Capas y A1 — PASS

Por cada normal se obtiene exactamente

    2,1,1,2,1,2,2,3,2,2,1,2,1,1,2.

Las seis capas intermedias unitarias por normal cubren, entre las tres
normales, los 18 puntos que no son origen ni vértices. La rigidez exige
suma matricial cero en cada capa intermedia: en una capa unitaria anula
la matriz entera, sin asumir simetría de sus coeficientes. Por tanto el
soporte superviviente está contenido en origen más seis vértices.
La resolución lineal original confirma lo mismo; no constituye una
premisa independiente de A1, como declara correctamente el informe.
Expandir las normales a radicales solo cambia su representación exacta.

## 3. Paso a T2 — PASS

La orientación del vértice (2,1) es atan(sqrt3/5). El giro espacial inverso
lleva los vértices normalizados al hexágono estándar. Un giro simultáneo
en el plano de Bloch conserva la forma isotrópica A(n)=r*n.sigma.
Es un cambio de coordenadas para aplicar la prueba geométrica, no una
afirmación de que ese giro preserve la red triangular original.

Inspeccionado `check_T2_minimal()`: usa siete puntos abstractos, matrices
complejas genéricas, ecuaciones de capa y las dos identidades de
unitariedad por diferencias de puntos. No usa factorización del walk
ni otros puntos de la red. El giro conserva las coincidencias entre
diferencias, así que permite transportar el argumento a H25 y H25'.
Las capas fuerzan A0=-I/2. El recálculo obtiene la ecuación real
`x^2-x/2+1/12=0`, de discriminante -1/12: imposible sobre los reales.

La rigidez analítica se apoya en el argumento de Julia de hex-ceiling
§3, leído como argumento matemático y no aceptado por su autoría.
No se ha subsanado la ausencia de referencia primaria paginada para
ese resultado clásico que el informe padre declara; no se reclama
una comprobación bibliográfica ni novedad.

## 4. Controles — PASS

Los cinco controles cuadrados pasan, incluido detectar un coeficiente
perturbado no unitario. Conservan el ejemplo saturante conocido. No
verifican un caso no trivial de A1 porque en ese soporte no hay capas
unitarias intermedias; el informe lo delimita correctamente.

## 5. Alcance — PASS

La conclusión es no alcanzamiento para s=2, nodo escalar y término lineal
isótropo sin traza, con hull exacto H25 o H25', en W_hex^sym y por
inclusión W_hex. No da separación uniforme del techo, supremo, prueba
de (PH), ni cierre de la clase hexagonal. `NOT_REFUTED_ON_H25` es adecuado;
`CONFIRMED_FOR_S25` pertenece a HX2 y no debe atribuirse a (PH).

Este documento registra una revisión técnica de otra familia que la
autora de S25, con herramientas y contexto previo. No equivale a revisión
humana ni a una segunda casa revisora adicional. El intento sellado
anterior permanece sin dictamen; esta revisión tiene procedencia distinta.
