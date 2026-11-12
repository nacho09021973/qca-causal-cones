# Lectura del autor (sesión Claude, claude-opus-5-5), 2026-11-12

Informe: `informe_grok.md` (grok-4.7, `COMPLETED`, herramientas `7d111a1`,
11:48–12:12 UTC), base `58885d4`. Copias enviadas sin el nombre interno del
régimen R2. Una ronda, sin herramientas.

**Dictamen del revisor: REPAIR_REQUIRED.** Cierran: reducción de fases a
`e^(iN psi_k)` (con la comprobación en `pi u`), sumas con decaimiento
complejo, herencia de las cotas, pérdida de positividad bajo H9(ii),
`mu_k != 0` como condición suficiente, media no nula bajo H9(i). No cierra
el segundo momento en todo el bloque de hipótesis.

## Objeciones

- **O1 (aceptada; no reparable sin cambiar el enunciado).** H6_k(ii) junto
  con H9(i): si `(psi_1 - psi_2)/(2 pi) = u.w_B`, ambas cláusulas valen y el
  término cruzado es función de `theta^B`, sin razón para anularse. La
  sección 8 sólo trata un desfase. **El veredicto de la sección 9 queda
  restringido**: probado para H6_k(i) con cualquier H9_k, y para H6_k(ii)
  con H9(ii); la celda H6_k(ii) + H9(i) queda `OPEN`. No se cambia la
  enmienda (aprobada): se restringe lo que el veredicto cubre.
- **O2 (aceptada, reparada sin hipótesis nueva).** El giro común del grupo:
  `M_B` hermítica con `u = M_B R~` recorre `{u : <R~, u> real}`; con
  `u_0 ⟂ R~`, `u_0^dagger e_k != 0` (H10_k), los vectores `u_0` y `-i u_0`
  dan `i` veces el mismo vector de coeficientes para todos los `j` a la
  vez. Añadido a la sección 10 del informe.
- **O3 (aceptada, reparada).** Media positiva de `|h|^2` no da densidad
  positiva por sí sola. Reparado con la medida de Haar del cierre de la
  órbita en el toro: la independencia por pares hace Haar las proyecciones
  bidimensionales, los cruces integran a cero en el cierre, `|h|` es
  continua en él, y la órbita equidistribuye respecto de esa medida.
- **O4 (aceptada en parte).** El revisor no tenía las pruebas de la red.
  En el repositorio: el diagnóstico (`lattice_isometric_to_Zd = false`
  para W2, W3, W6), el hallazgo registrado de que (5.12) genera el grupo
  BCC (enmienda 1 de la fase 0 de saturación, `5213d94`) y el retículo de
  paridad igual de índice cuatro del paseo s=4
  (`scripts/verify_s4_cyclic_realization.py`). Se mantiene «fuera de
  `Z^d`». Se acepta lo esencial: ninguno es un ejemplo verificado de R1
  (H6_k(i) falla; H6_k(ii) depende de una independencia racional no
  decidible en flotante; `mu` es numérico). Sección 9 reescrita.
- **O5 (aceptada).** Girar por `e^(-i arg mu)` antes de usar la parte real.
- **O6 (aceptada como nota).** `mu_k != 0` es suficiente, no necesaria;
  en el segundo momento basta `int |Gamma_j|^2 > 0`.
- **Obligación 3 (aceptada como lectura).** «No separable» se lee como
  álgebra lineal: `f_k` fuera del span de los `f_j` con `j` fuera de `G`,
  y cada punto fuera de `G` separable por la izquierda.

Reparaciones aplicadas tras la revisión y no re-revisadas.
