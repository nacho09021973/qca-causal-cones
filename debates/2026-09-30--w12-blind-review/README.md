# Revisión ciega de W12 — 2026-09-30

Objeto: W12 (universalidad del métrico entre las cuatro especies) en
`research/gravitational-normalization-gate` @ `5485cb0`. Contrato de Claude (`2ff88b2`), ejecución
de Astra/GPT. Herramienta: `revision-ciega` (`~/herramientas` @ `b817ac0`), sellada, una ronda.

| Revisor | Veredicto |
|---|---|
| DeepSeek `deepseek-v4-pro` (según la API) | ACCEPT, sin reparaciones obligatorias |
| Opus `claude-opus-5-5` | ACCEPT_WITH_REPAIRS (6) |

Ambos recalculan a mano y confirman: marcos, `δE_*/g = −2Z diag(τ)D`, `𝒰 = span{e11,e22,e33}`,
rango de Φ = 6, rango 3/6 en 𝒰, las tres relaciones y núcleo común nulo. Ambos: el negativo no
depende de convenciones permitidas por el contrato.

## Comprobaciones

- `verify_w12_independent.py` (Claude, antes de la revisión): rederivación independiente; mismo
  resultado; también con la convención `h = E Eᵀ`.
- `verify_reviewer_claims.py` (afirmaciones adicionales de Opus), todas CONFIRMADAS:
  - la fórmula de `δE_*` vale también en los nodos −I;
  - en 𝒰, `δh(−I) = −δh(+I)`; con los ocho nodos, `dim 𝒰₈ = 0` → sería `NON_UNIVERSAL`;
  - cada nodo +I por separado tiene rango métrico 6; los núcleos de rotación dependen del nodo;
  - leídas como condición gauge sobre `δh = ∂ᵢξⱼ + ∂ⱼξᵢ`, las tres relaciones que faltan tienen
    símbolo de determinante `−q₃(2q₁q₂ − q₁q₃ − q₂²)`: se pueden alcanzar por gauge para vectores
    de onda genéricos y fallan en `q₃ = 0` y en un cono.

## Consecuencia para la interpretación

El veredicto contractual `UNIVERSAL_SUBFAMILY_DEFICIENT` se sostiene y el contrato lo clasifica
como negativo para la clase W6/CJWW. Pero la frase "a los controles universales les faltan tres
componentes físicas del métrico" es demasiado fuerte: el rango 3/6 se mide sobre `δh` constante,
que es un cambio de coordenadas trivial. Con perturbaciones que varían en el espacio, el déficit es
el conjunto `q₃ = 0` más un cono, no tres componentes. Esto no reabre la línea (el contrato
prohíbe el rescate a posteriori), pero limita cómo se cita el negativo.

## Reparaciones de Opus (a aplicar por el autor)

1. Informar de `δE`, `δh` en los nodos −I (lo exige el contrato), con `δh(−I) = −δh(+I)` en 𝒰.
2. U6 es cierta por construcción; decirlo, o comprobar el símbolo real de `J_e`.
3. Asertar `J(p_*) = 0` y la ausencia de término identidad; quitar o anotar los asserts vacíos de U5.
4. Distinguir obligaciones asertadas de solo impresas; el acuerdo de órdenes del producto está
   garantizado por estructura.
5. Frase de alcance sobre la lectura gauge (arriba).
6. Registrar el rango 6 por nodo y los núcleos de rotación dependientes del nodo.

Estado: revisión recibida y comprobada; reparaciones no aplicadas. Decide el usuario.
