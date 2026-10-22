# Auditoría documental: embedding y hopping elástico

Fecha: 2026-10-08. Base inspeccionada: `0a4606c61a3f75e5516a245f3837ed009b0a56b4`,
rama `research/gravitational-normalization-gate`.

## Objetivo y cierre

Auditar únicamente la fila «Sucesor elástico F2–F4» del
[cruce de claims](2026-10-01--atlas-project-claim-crosswalk.md), contrastando
F1–F4 con F13–F17. Encargo documental autorizado por «adelante» tras el
balance del repositorio. Cierra al distinguir embedding, respuesta de hopping
y alcance transferible de las fuentes. Una ronda local; sin revisión externa,
ejecución de certificados, cambio de contratos ni promoción de evidencia.

## Evidencia local examinada

Se leyeron la cabecera autoritativa de `state/CURRENT_STATE.md`, las fichas
F1–F4 y F13–F17, los contratos F2/F4, el informe de ejecución F4 y el código
permanente `scripts/verify_elastic_hopping_hermitian_response.py`.
El código separa la corrección de hopping de `E*u`, elimina la fase escalar
antes de extraer el marco y contiene aserciones de corrección y tilt nulos
en los cuatro nodos +I. Esta es inspección de implementación, no una nueva
ejecución ni verificación independiente del resultado.

| Familia | Resultado registrado | Interpretación admisible |
|---|---|---|
| F1 / W12 | Subfamilia universal de rango 3/6; cierre contractual, revisión registrada | Negativo para controles W6/CJWW constantes; no contar el déficit como tres grados físicos ausentes |
| F2 | `h_*=a²ΛΛᵀ`, rango tangente 6/6 | Transformación común del embedding; bloques abstractos sin modificar; PRELIMINARY |
| F3 | Generador dependiente de la elección de semisoporte | Fallo de definición de ese ansatz; test métrico de cuatro especies no ejecutado |
| F4 | Corrección de marco por hopping cero a primer orden, fase nodal `tr(u)/3` | Rango 6/6 enteramente heredado de F2; PRELIMINARY, revisión independiente pendiente |

La exponencial de un generador de rango finito no certifica por sí misma un
tick de soporte estricto finito. Las fichas F3/F4 ya conservan esta limitación;
esta auditoría no demuestra soporte infinito ni modifica su clasificación.

## Contraste primario acotado

Se consultó primero `biblioteca/INDICE.md`. Los pasajes siguientes se leyeron
directamente con `pdftotext -f N -l M -layout <PDF> -`; las páginas son páginas
del PDF local. Las fichas orientaron la selección, no sustituyeron los originales.

| Comparador | Pasaje comprobado | Transferencia permitida |
|---|---|---|
| F13, Farrelly–Short | `biblioteca/1312.2852v1.pdf` p.3, Ecs.14–18: regla de desplazamientos, Hamiltoniano principal y rescalado/transformación de ejes | Separar normalización de un límite Weyl y elección de coordenadas de una respuesta física común de especies |
| F14, D’Ariano–Erba–Perinotti | `biblioteca/1708.00826v2.pdf` pp.1–4 y 7–8: regla Cayley, isotropía y clasificación, Proposición 5 | Comparar hipótesis de clasificación; no aplicar automáticamente su clase isotrópica a una deformación afín arbitraria |
| F15, D’Ariano–Perinotti | `biblioteca/Derivation of the Dirac Equation from Principles of Information Processing.pdf` pp.2–3, Ecs.5–14: regla, palabra-métrica, embedding y espacio de momentos | Distinguir grafo abstracto y embedding; la cuasi-isometría no es una ley constitutiva de hopping elástico |
| F16, Białynicki-Birula | `biblioteca/Dirac and Weyl Equations on a Lattice as Quantum Cellular Automata.pdf` pp.2–3, Ecs.1–18: ocho desplazamientos, condiciones de unitariedad y límite con `c=a/Δt` | Comparar actualización y expansión; sus ocho desplazamientos no identifican los 14 bloques CJWW usados en F3/F4 |
| F17, Bisio–D’Ariano–Perinotti | `biblioteca/Quantum Walks, Weyl equation and the Lorentz group.pdf` pp.2–3, Ecs.1–7: BCC, símbolo, rescalado y varios puntos Weyl | La presencia de varios puntos Weyl es antecedente; no identifica sus nodos con los cuatro +I del contrato CJWW |

[ABSENCE — búsqueda acotada] En estos pasajes no se especifica una ley
`W_h(u)` de hopping elástico CJWW con respuesta métrica no trivial común a
las cuatro especies contratadas. Esto no prueba ausencia en los artículos
completos ni en la literatura; no es un veredicto de novedad.

## Segunda vía de control del alcance

Como comprobación conceptual de la interpretación, mantener un strain
constante y los bloques `W_h` fijos deja la misma regla abstracta. El cambio
`p=aΛᵀq` explica la transformación del marco y, usando la identidad plana
registrada `E_*ᵀE_*=I`, da `h_*=a²ΛΛᵀ`. Este argumento condicional coincide
con el contrato F2 y explica por qué rango 6 no implica nuevo hopping.
No verifica aquí la identidad plana por especie ni aporta un certificado nuevo.

En el caso límite `Λ=I`, desaparece esa contribución de embedding.
El resultado registrado de F4 conserva solo la fase nodal y ninguna corrección
del marco por hopping al orden fijado. No se extrapola a segundo orden,
strain espacialmente variable, otros nodos o dinámica geométrica.

## Decisión

Auditoría documental completada. Se conserva la separación:

1. F2 aporta la referencia cinemática común.
2. F3 falla antes del test métrico.
3. F4 define una respuesta unitaria pero no añade respuesta métrica de hopping
   al orden contratado.
4. F13–F17 proporcionan comparadores de regla, embedding, isotropía y límite
   Weyl; los pasajes comprobados no cierran el puente elástico.

No se requieren cambios del estado canónico por este contraste. W1–W12
permanece cerrado en su clase, H1 permanece pausado y NOVELTY sigue OPEN.
Quedan pendientes la revisión independiente de F2/F4 y, para cualquier nueva
familia, una motivación física independiente previa y un contrato separado.
Este documento no selecciona una regla sucesora ni autoriza su cálculo.
