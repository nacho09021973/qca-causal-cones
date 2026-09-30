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

Estado: revisión recibida; reparaciones no aplicadas. Decide el usuario.
