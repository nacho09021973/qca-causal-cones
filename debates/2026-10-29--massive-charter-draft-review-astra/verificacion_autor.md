# Lectura del autor — revisión Astra del borrador v1 del charter con masa

Fecha: 2026-10-29. Autor: Claude, autor del borrador. **No es una revisión independiente.**
Bytes revisados: `afc2b64`. Herramienta: `revision_ciega.sh` @ `a32e189`. Autorización: «manda la
revision de masa, ya tengo datos en astra, asi que se lo puedes lanzar a ella».

## Veredicto del revisor

**NO LISTO PARA CONGELAR**, con trece reparaciones A-M-01..13. Además aporta una construcción
explícita (derivación manual del revisor, `[UNVERIFIED]` hasta certificarla) en la clase M4:

`U_{η,t}(k) = (e^{itτ_x} ⊗ I_2) D_η(k)`, con `D_η` el acoplamiento de Dirac estándar de ángulo `η`,
`η + t = M`.

- `cos ω(k) = cos η cos t · u(k) − sin η sin t`.
- `c_{ω^2}^2 = (1/3) M cos η cos t / sin M` y `c_H = (1/√3) M cos η / sin M`.
- `c_strict^iso = 1/√3` en toda la familia (todos los vértices con traza no nula).

## Contraste

**`c_{ω^2}`, rehecho a mano: correcto.** Con `u ≈ 1 − |k|^2/6`:
- `cos ω(0) = cos(η + t) = cos M`;
- `ω ≈ M + cos η cos t |k|^2 / (6 sin M)`, luego `c_{ω^2}^2 = M cos η cos t / (3 sin M)`;
- con `(η, t) = (M, 0)` reproduce el valor establecido de la familia estándar, `(1/3) M cot M`;
- con `(M/2, M/2)` da `(1/3)(M/2) cot(M/2)`, distinto porque `x cot x` es estrictamente decreciente
  en `(0, π/2)`.

**`c_H`, la unitariedad, la covarianza y la traza de los vértices:** plausibles, no rehechos. La
covarianza es inmediata: `e^{itτ_x} ⊗ I` conmuta con `I ⊗ σ_i`.

**Consecuencias, si se certifican:**
- QM-0: existen sectores con masa en M4, incluso con `T_0 = 0` (contra la necesidad de C1).
- QM-1 para `c_H`: violación, `c_H = M/(√3 sin M) > 1/√3`. Lectura del autor: `c_H` no es una
  velocidad de señal, así que una cota causal para `c_H` no tenía por qué valer.
- QM-2: `MASS_DEFICIT_ADJUSTABLE_WITNESS` para ambas extracciones, a igual `M` e igual cuerpo
  estricto.
- C4 era correcta en la conclusión pero no en el argumento: los dobletes del contraejemplo s=4
  tienen pendiente lineal y no forman un sector con masa.

## Reparaciones

| ID | Lectura del autor |
| --- | --- |
| A-M-01 (proyectores completos, rango par, tuplas) | Se acepta. |
| A-M-02 (identificación de fibras para `c_H`) | Se acepta. Bloqueante: una base móvil cambia el término lineal. |
| A-M-03 (la traza no es Clifford) | Se acepta: error demostrado; contraejemplo comprobado (`{α_x, α_y} = −2σ_z ⊗ τ_z`). |
| A-M-04 (C1 no es necesidad) | Se acepta. |
| A-M-05 (alcance de Schur) | Se acepta. |
| A-M-06 (C3 demostrable) | Se acepta; se incorpora como paso de la etapa (a). |
| A-M-07 (C4 por continuidad) | Se acepta. |
| A-M-08 (soporte permitido/efectivo, `T_0` en el conmutante) | Se acepta. |
| A-M-09 (QM-1 falla para `c_H`) | Se acepta como candidato a certificar. |
| A-M-10 (QM-2: denominadores, dos variantes) | Se acepta. |
| A-M-11 (QM-3 sin definición ni etapa) | Se acepta. Bloqueante. |
| A-M-12 (límites de Gröbner) | Se acepta. |
| A-M-13 (alcance; A fuera) | Se acepta. |

## Conclusión del autor

El borrador no se puede congelar tal como está. La revisión adelanta resultados: si la
construcción se certifica, QM-0, QM-1 (para `H`) y QM-2 quedan decididos en M4 por testigos
explícitos. Un v2 debería reformular el charter alrededor de esos testigos y dejar abiertas QM-1
para `ω^2` y QM-3. Lo decide el usuario.
