# Comprobación focalizada: E5 escrito y estabilidad `||t_j||_2 = O_{W,Theta}(1)`

## Contexto de esta petición

En una revisión anterior (acta `2026-09-25--schur-repair-deepseek-review.md`)
el miembro ABNER señaló que E5 estaba redactado como "se propone obtener" y no
como lema ejecutado: faltaban (i) separación espectral uniforme
`sup rho(M(p)) < 1` dentro y fuera de `W`, y (ii) la cota de Cauchy
`||M^h|| <= C_0 rho_1^h` con `C_0(W)` uniforme sin diagonalizabilidad ni número
de condición. ABNER escribió que, sin esa ejecución, la conclusión "debe
permanecer abierta". Ninguno de los otros miembros de esa acta reprodujo
esa ejecución; se ha escrito después, en la nota adjunta
`reports/2026-09-25--schur-block-stability-repaired.md`.

## Decisión solicitada

Revisar **únicamente** si la nota adjunta (§§2–4) ejecuta E5 y cierra
la conclusión

`sup_{0<=j<=N} ||t_j||_2 <= C(W,Theta) ||s||_2`,

con `W` admisible fijo, `||vartheta||_inf <= Theta` y `N>=2`. No es una
revisión general. No revisar Schur (7)–(8), `||M_N||`, las cotas físicas,
las diez piezas, ni H1/H1c. No proponer rutas nuevas (en particular no la
vía Dyson).

Puntos que deben atacarse:

1. §3, dentro de `W`: `M(p) = (lambda Lambda)^-1 Q(p)`, `rho(M) <= Lambda^-1`.
   ¿Se sigue de `D_xi Q = lambda^-1 Q` y `Q^2 = Q`? ¿Es suficiente
   `|lambda| > 1` en el cierre de `W`?
2. §3, fuera de `W`: `r_ext < 1` por `lem:specrad` (igualdad sólo en `Sigma`,
   todas las componentes de `xi_*` no nulas), compacidad de `T^3\W` y
   continuidad de `rho`. ¿Queda `partial W` bien cubierto?
3. §3, resolvente: `|det(zI-M)| >= (rho_1-rho_0)^4` y
   `||adj(A)|| <= ||A||^3` para `A` `4x4` en norma de operador. ¿Correcto? ¿La
   constante `R` y `C_0` son independientes de `p`, `N`, `j`, `vartheta`?
4. §3, norma `||.||_*`: equivalencia `||y||_2 <= ||y||_* <= C_0||y||_2` y
   `||My||_* <= rho_1||y||_*`.
5. §4, las cuatro identidades de bloque y sus cotas, en particular que
   `P M = 0`-type cancelaciones (`P D_xi Q = Q D_xi P = 0`) son las únicas
   desapariciones y que los productos `P(p')Q(p)` con `p' != p` se pagan con
   `||E|| <= Theta/N`.
6. §4, recurrencia: `nu_{j+1} <= (1+kappa/N) nu_j` sin factor constante `> 1`
   por paso, y `nu_0 <= (C_P + C_0 C_Q)||s||_2`.
7. Rotulado: ¿`O_{W,Theta}(1)` es la dependencia correcta?

## Criterio de veredicto

`PASS`, `PASS_WITH_REPAIRS` o `REPAIR_REQUIRED` para esa conclusión, con el
primer paso que falla (si lo hay), la condición exacta que lo desactiva y el
alcance. Indicar expresamente si la objeción original de ABNER sobre E5
queda cerrada. No convertir esta comprobación en un PASS de Schur (7)–(8) ni
de las transferencias físicas.
