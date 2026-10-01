# Uso del atlas para el proyecto QCA-Causal-Cones

Fecha: 2026-10-01. Esta guía traduce F1–F20 a decisiones de trabajo del
proyecto. No es un contrato científico y no modifica `state/CURRENT_STATE.md`.

## Regla de uso

Una familia del atlas puede servir para:

1. localizar un antecedente primario;
2. comparar cuantificadores y claim ceilings;
3. identificar una obstrucción o un test de muerte;
4. justificar que una nueva regla es realmente distinta;
5. decidir qué cuestión merece un contrato posterior.

No puede, por sí sola:

- convertir una arquitectura bibliográfica en una regla CJWW;
- transferir una prueba de una celda, coin, soporte o dimensión a otra;
- reabrir W12 o la línea gravitatoria cerrada;
- promover una afirmación preliminar a establecida;
- sustituir una revisión primaria o un certificado permanente.

## Mapa por frentes del proyecto

| Frente del proyecto | Familias útiles | Uso permitido | Límite vigente |
|---|---|---|---|
| `C_micro`, `V_causal`, `V_grp`, `c_IR` | F13, F14, F16, F17 | Separar soporte, dispersión, límite Weyl y simetría de momentos | No inferir una métrica física ni una escala absoluta |
| Universalidad de especies | F1, F2, F3, F4 | Comparar controles Pauli-selective, embedding común y hopping | F1/W12 está cerrado en su clase; F2–F4 no reabren W12 |
| Puentes a walks curvos | F5, F6 | Contrastar operator splitting, agrupación y dimensión | El certificado F5 solo tiene alcance restringido; no mata F6 globalmente |
| Geometría dinámica | F7, F10, F11 | Identificar requisitos para links, grafos dinámicos, acción y corriente | No existe todavía una regla CJWW completa en F7/F10/F11 |
| Constraints y helicidad | F8, F9, F18 | Comparar constraints tensoriales, Gauss laws, fractones y helicidad | No hay puente local CJWW–fuente/backreaction |
| Gravedad emergente | F19, F20 | Auditar antecedentes de gauge/difeomorfismos efectivos y fases IR | Son marcos no-QCA o de red distinta; no validan W9–W11 |
| Claim de novedad | F8–F20, especialmente F12–F20 | Construir el techo de prior art antes de cualquier promoción | La novedad sigue `OPEN` |

## Cómo usarlo en una tarea concreta

### 1. Si la tarea es sobre velocidad causal

Comenzar por F13–F17 y escribir explícitamente qué objeto se compara:
`C_micro`, soporte estricto, velocidad de grupo, velocidad Weyl o simetría en
espacio de momentos. No mezclar la dispersión de F17 con la métrica de F2.

### 2. Si la tarea es sobre universalidad entre especies

Comenzar por F1–F4. El contrato debe declarar de antemano soporte, especies,
nodos, controles, orden perturbativo, rango y tolerancia. F2 solo certifica el
embedding cinemático; la respuesta de hopping sigue abierta.

### 3. Si la tarea es sobre curvatura o backreaction

Usar F5–F11 como auditoría de arquitectura y cuantificadores. Antes de
calcular debe existir una regla unitaria concreta, una observable geométrica y
una recuperación plana exacta. Si falta cualquiera, el resultado correcto es
`OPEN` o `NO_RULE_SPECIFIED`.

### 4. Si la tarea es sobre gravedad o gauge

Usar F8–F20 para separar cuatro niveles: constraint, gauge, métrica efectiva y
fuente/backreaction. Una coincidencia en helicidad, Gauss law o difeomorfismo
no demuestra una realización CJWW.

## Orden recomendado de trabajo

1. Revisar el claim que se quiere hacer y reducirlo a sus cuantificadores.
2. Consultar `relations.csv` para localizar antecedentes y obstrucciones.
3. Leer el PDF primario de la arista elegida y registrar páginas.
4. Comparar la regla microscópica antes de comparar la ecuación IR.
5. Escribir contrato solo si queda una diferencia de arquitectura ejecutable.
6. Ejecutar el kill test más barato antes de cualquier cálculo de backreaction.
7. Mantener el resultado en el claim ceiling de la familia y del estado canónico.

## Decisión actual

El atlas se usa ahora como capa de selección y auditoría. La línea W1–W12
permanece cerrada por contrato en la clase W6/CJWW; el sucesor elástico F2–F4
solo puede avanzar dentro de sus propios contratos; y las familias F5–F20 no
abren por sí mismas un nuevo programa gravitatorio.
