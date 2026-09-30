# Revisión ciega, segunda ronda: reparaciones W9–W11 — 2026-09-30

Objeto: addenda de reparación de W9, W10 y W11 en `research/gravitational-normalization-gate`
@ `86fe771` (autor: Astra/GPT). Herramienta: `revision-ciega` (`~/herramientas` @ `b817ac0`),
sellada, una ronda, desde cero (sin los informes de la primera ronda).
Documentos: `documentos.txt` (+ `cjww_walk_definition.md`). Encargo: `prompt.md`.

| Revisor | W9 | W10 | W11 |
|---|---|---|---|
| DeepSeek `deepseek-v4-pro` (según la API) | ACCEPT_WITH_REPAIRS | ACCEPT | ACCEPT |
| Opus `claude-opus-5-5` | ACCEPT_WITH_REPAIRS | ACCEPT_WITH_REPAIRS | ACCEPT_WITH_REPAIRS |

Ambos: tabla de ocho nodos, marcos `E_* = diag(σ₂σ₃, −σ₃, 1)`, K (hermiticidad, `[K,U]=0`,
saltos, densidad), cotas de banda y dinámica, y la prueba de F3 son **correctas**. W10
`OPEN_AFTER_AUDIT` es coherente. La etiqueta terminal de W9 sobrevende su alcance.

## Comprobación (`verify_reviewer_claims.py`)

- CONFIRMADO: `‖K − H_IR‖ ≤ |p|³/2` (muestreo: sup del cociente 0.226; Opus decía ≈0.18); la
  cota `Λ³` del informe es válida pero holgada.
- CONFIRMADO: cotas de banda y dinámica (cociente máximo 0.998 ≤ 1 en los cuatro nodos +I).
- CONFIRMADO (Opus): en los nodos −I, `K = −H_*(k)` a primer orden (signo de energía opuesto).
- CONFIRMADO (Opus): en la forma lagrangiana, `h00` es lineal y `h0i` cuadrático; el shift solo
  es multiplicador en forma hamiltoniana.
- CONFIRMADO (Opus, por lectura y SymPy): en el certificado de W9, `after_ibp` repite el primer
  assert y `residual.subs(k0,0)==0` se cumple por construcción. DeepSeek lo daba por no vacío.
- SIN COMPROBAR: la prueba de F3 (aceptada por ambos), la afirmación de Opus sobre el grupo gauge
  residual síncrono completo.

## Reparaciones pedidas (segunda ronda)

Obligatorias (ambos o verificadas):
1. W9: cambiar la etiqueta terminal para que diga su alcance real, p. ej.
   `ON_SHELL_CONTINUUM_IDENTITY_PASS / CJWW_BRIDGE_OPEN`, o `OPEN_AFTER_AUDIT` con B2 como
   subresultado.
2. W9: certificado — sustituir los asserts de `after_ibp` y `subs(k0,0)` por uno real
   (variación espacial = iλΣξ_j(Tk)_j + residuo, usando la conservación), o describirlos como
   reformulación de convenciones.
3. W9, W10, W11: banner "superseded — see §9" junto al bloque de veredicto original (sin tocar el
   texto congelado; va como línea añadida o nota en CURRENT_STATE si no se quiere editar el
   prefijo).
4. W9/W10: el shift es multiplicador de Lagrange solo en forma hamiltoniana.
5. W11 F3: restringir a generadores de una partícula (cuadráticos) invariantes por todo ℤ³ con la
   celda de 2 componentes; los generadores con interacción o de supercelda quedan abiertos, así
   que la pregunta F3 del contrato no está cerrada.

Recomendadas (un revisor):
6. W11: registrar que K es −H_* en los nodos −I y dos-a-uno en θ ↔ π−θ.
7. W11: describir como entradas analíticas la completitud de nodos y la serie de H_eff, y que la
   tabla se imprime, no se asierta fila a fila.
8. W9: mencionar el término de frontera temporal en B1 y ampliar "static" a "al menos estático".
9. W10: T₍₀₎ en C2 debe ser el tensor total de las cuatro especies (no construido).
10. Opcional: afinar `‖K − H_IR‖ ≤ Λ³/2`.

Estado al recibir la revisión: reparaciones no aplicadas. La aplicación
autorizada posteriormente por el usuario se registra a continuación.

## Aplicación autorizada — 2026-09-30

Rama: `research/gravitational-normalization-gate`, tras incorporar `d6e74e6`
por avance rápido. Se conservan los informes de los revisores y los contratos.
Los tres informes científicos reciben una nota junto al veredicto histórico
y correcciones de alcance en §9. Estas correcciones responden a esta revisión;
no constituyen una tercera revisión independiente ni cierran los gates.

| Punto | Cambio aplicado |
| --- | --- |
| 1 | W9 pasa a `OPEN_AFTER_AUDIT`, con B2 `ON_SHELL_CONTINUUM_IDENTITY_PASS / O(lambda)` y puente CJWW abierto. Estado canónico y tabla de navegación sincronizados. |
| 2 | Se eliminan los asserts redundantes de W9. Se verifica la diferencia entre variación espacial calculada y residuo contra el término de conservación. Un tensor simétrico conservado polinómico comprueba variación completa nula, caso estático y un caso temporal no nulo, sin dividir por k. La integración por partes se describe como convención analítica. |
| 3 | Los tres bloques de veredicto originales llevan `SUPERSEDED — see §9` con el estado actual. Las secciones históricas 29–31 del estado también remiten a las reparaciones. |
| 4 | W9/W10 distinguen multiplicadores en forma hamiltoniana de dependencia cuadrática del shift en el lagrangiano h-only. |
| 5 | F3: una partícula (o segunda cuantización cuadrática que conserva número), todas las traslaciones ℤ³, celda original de dos componentes. Interacciones, superceldas y logaritmos discontinuos quedan fuera; F3 del contrato permanece abierto. |
| 6 | W11 explicita `K=s_* sin(H_*)`: signo opuesto a primer orden en −I y ambigüedad θ ↔ π−θ. |
| 7 | W11 identifica completitud de nodos y fórmula de H_eff como entradas analíticas; precisa qué comprueba el script y qué tabla imprime. |
| 8 | W9 conserva explícitamente el término de frontera temporal y dice «al menos estático», sin afirmar una clasificación del grupo residual. |
| 9 | W10 exige que T_(0) sea la suma de las cuatro especies; su correspondencia local microscópica sigue sin construirse. |
| 10 (opcional) | Se mantiene la cota Λ³ ya válida. No se añade un refinamiento de constante a esta reparación de alcance. |

Validación local:

- `python3 -B scripts/verify_w9_continuum_gauge_bridge.py`: PASS.
- `python3 -B scripts/verify_w10_linearized_constraints.py`: PASS, sin modificar el certificado.
- `python3 -B debates/2026-09-30--w9-w11-repair-review/verify_reviewer_claims.py`:
  PASS; cocientes máximos muestreados de banda y dinámica 0.998. Son muestras,
  no supremos demostrados. Su último chequeo reproduce la objeción al W9 de
  `86fe771`, no describe el certificado reparado actual.
- `git diff --check`: PASS.

SHA256 del certificado W9 actualizado:
`60254b382f634227f728d0622e8f9d79a540b0b891df0d5079bf15f909cbdc58`.

Los resultados aceptados de nodos, K, cotas y prueba F3 no se alteran. Siguen
abiertos el tensor local de Belinfante a q≠0, el emparejamiento local de las
cuatro especies y la backreaction. La aceptación de F3 en su clase no es una
prueba de novedad.
