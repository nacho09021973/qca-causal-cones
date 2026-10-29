# Lectura del autor — revisión Grok de la etapa 4b-2 del charter s=2

Fecha: 2026-10-29. Autor: Claude, autor del certificado y del informe. **No es una revisión
independiente.**

## Ejecución

- `COMPLETED`, `grok-4.7`. Bytes revisados: `7c741df`, certificado `8849e87a…`.
- Herramienta: `revision_ciega.sh` @ `a32e189`.
- Autorización: «permiso concedido, y si, lanza a GRok».

## Veredicto del revisor

**Sostenido, con reparaciones obligatorias antes de promocionar.** Rehace a mano:
- la parametrización y la biyección;
- la independencia de las funciones y el sistema `R` (27 ecuaciones);
- la deducción completa de las 48 familias, sin caso nulo omitido;
- los 16 puntos escalares y los cuatro nodos (con un recuento de covolumen: `4 · 4 = 16`);
- `H_j`, `c_0 = 1/√3`, el lema del vértice, `h_∞` y `rho_micro`.

No reejecuta Gröbner: la igualdad de ideales queda como afirmación del certificado. Para el
conjunto de soluciones no hace falta.

## Contraste

| ID | Lectura del autor |
| --- | --- |
| G-4B2-01 (laguna en el argumento a mano de Q-a (ii)) | **Se acepta: error demostrado del paso.** La suma del desplazamiento `gh − h` es `T_h^†T_{gh} + T_{−gh}^†T_{−h}`; yo había usado `T_{−gh} = T_{−h}` sin probarlo (el mismo atajo estaba en mi lectura del argumento de Astra en 4b-1). Reparado: `T_{−h} = μ(I − P)` conmuta con `R_g`, y la covarianza da `T_{−gh} = T_{−h}`. Comprobado a mano. La conclusión no dependía de él: la ruta (i) y los ideales unidad del certificado cierran Q-a. |
| G-4B2-02 (dominio de la Eq. (2)) | Se acepta. El informe dice ahora que la comprobación en `N_3` implica la Eq. (2) sobre `S_+`, que es más fuerte que el enunciado literal. |
| G-4B2-03 (`h_∞` y la letra `h`) | Se acepta. Se escribe `h_∞(q̂) = |q̂|_1/√3` con `h = ε/√3`. |
| G-4B2-04 («Consecuencia») | Se acepta. Se limita a lo demostrado; se dice que no se impone la normalización de P17 ni se identifican las 48 familias con sus paseos. |
| G-4B2-05 (procedencia) | Se acepta. 4b-1 ya está revisada y promocionada (`014753e`). |

## Conclusión del autor

Las cinco reparaciones son de texto; los bytes del certificado no cambian. No queda ninguna
objeción obligatoria abierta en el contenido. Las reparaciones no se han vuelto a revisar. Se
promociona como ESTABLISHED IN THE DECLARED CLASS, con la instrucción del usuario de promocionar
tras la revisión.
