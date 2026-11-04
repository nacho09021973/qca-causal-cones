# Lectura del autor de la revisión de gpt-6.1-sol del borrador de la Enmienda 1

Autor: Claude (Anthropic). Objeto: `theory/SUBSTRATE_SATURATION_PHASE0_GATE_AMENDMENT_1.md`
en `cecf75a`. Revisor: `gpt-6.1-sol` (OpenAI, `codex exec`, miembro astra),
COMPLETED, 2026-11-04. **PASS**, sin reparaciones obligatorias. Puntos 1–5
PASS; un INSUFFICIENT_EVIDENCE parcial sobre el cumplimiento documental de
Sec. 1.3 (no recibió los expedientes de DeepSeek).

## Comprobaciones del autor

- **Sec. 1.3, expedientes.** Revisión DeepSeek 1: addendum en `3e20c70`,
  sha256 `39a6d17a…`, PASS. Comprobación literal de p. 16: addendum en
  `738b62c`, sha256 `b8b9ed87…`, PASS. El addendum actual tiene sha256
  `b8b9ed87…` (`sha256sum`, 2026-11-04): es el texto de la segunda revisión.
  Entre ambas cambió la cita de página y la redacción de (v). Además, el
  propio gpt-6.1-sol rehízo (i)–(v) de ambos walks desde el texto de la
  fuente (punto 3, PASS): la derivación tiene ahora PASS de dos familias
  distintas de la del autor.
- **Signo de (5.13).** Con `σ1σ2σ3 = iI`, el término triple de (5.12) es
  `i^3 s1 s2 s3 · iI = +s1 s2 s3 I`; la semitraza es `c c c + s s s`, como
  `F1` (`verify_directional_saturation.py` l. 81). El revisor llega a lo
  mismo. Su expansión `ω^2 = |p|^2 − 2 p1 p2 p3 + O(|p|^4)` cerca de 0: de
  `cos ω = 1 − |p|^2/2 + p1p2p3 + O(|p|^4)` y `ω^2 = 2(1 − cos ω) + O(|p|^4)`.
  Coincide. No afecta a (i)–(v), al soporte ni al radio; sí al término
  cúbico de la dispersión. Ya estaba registrado en el repo:
  `verify_directional_saturation.py` l. 106–111 certifica `ccc + sss` frente
  al `ccc − sss` impreso, y `scripts/README.md` l. 98 dice que ambos difieren
  por `p -> -p`; `reports/2026-09-16--directional-causal-saturation.md` l. 20
  lo anota. No es un hallazgo nuevo.
- **Recuento F3.** Cuatro sustratos más el hexágono de grupo fino = 5;
  con el `Z^3` de (5.15), 6. Coincide con el revisor.

## Aclaraciones no bloqueantes (no aplicadas; decide el usuario)

1. Sec. 1, título «replaces nothing»: mejor «conserva las condiciones
   matemáticas y añade una excepción explícita a la procedencia documental
   del nodo».
2. Registrar la discrepancia de signo de (5.13) frente a (5.12), sin
   corregir el artículo, y no extender su irrelevancia a cálculos de
   dispersión.
3. Sec. 2.4: «not for (5.12)» se refiere al grupo generado; (5.12) puede
   formularse sobre `Z^3` con sus cuatro cosets BCC.
4. Que la Sec. 1.3 conste con los SHA y commits de los expedientes (arriba).

Búsqueda de secretos en la carpeta: sin coincidencias.
