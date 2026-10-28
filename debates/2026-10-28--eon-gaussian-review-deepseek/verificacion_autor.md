# Lectura crítica del autor (Claude Opus 5.5), 2026-10-28

Revisión sellada de `reports/2026-10-27--eon-projected-gaussian-reference.md`
(sha256 `ce267c5b…`, sin versionar; autor del informe: Codex) y sus adjuntos
(`inputs.sha256`). DeepSeek (deepseek-v4-pro, thinking, reasoning_effort=high,
max_tokens=65536), una ronda, `COMPLETED`/`stop`: **ACCEPT_WITH_REPAIRS**.
Bloques: construcción ACCEPT; hipótesis y alcance ACCEPT; prueba de obstrucción
ACCEPT_WITH_REPAIRS; ningún error fatal señalado.

## Tratamiento de las objeciones

| Objeción | Comprobación del autor | Decisión |
|---|---|---|
| G-R1-01, signo en la igualdad de autoestado | En el informe (§3.C), f es la serie de φ = D_E D_F ψ y g la de ψ («la misma estimación vale para la serie g de psi»). Entonces Uψ = D_M φ = λψ da e^{iθB} f = λ g, que es la igualdad escrita con λ absorbido en g. En el arco con Re(iθaz) ≥ abs(θa) r/2, abs(f) = abs(λ) abs(e^{−iθB}) abs(g) ≤ e^{−abs(θa) r/2 + O(1)} abs(g): justo la cota que usa el informe. El revisor tomó f como la serie de ψ y g como la de φ. Arco de 2π/3 y media −abs(θa) r/6, comprobados. | **Rechazada como error.** Se acepta como reparación de redacción: definir f y g de forma explícita y escribir λ. |
| G-R1-02, Jensen/convexidad subenunciado | La media circular de log abs(f), con log abs(f) subarmónica en el anillo exterior, es convexa en log r. Una recta de apoyo da la cota afín inferior. El enunciado del informe es correcto. | Aceptada como redacción: escribir el enunciado preciso. |
| G-R1-03, cotas gaussianas bajo D_F, D_E | El informe ya da β/2 con constante mayor; la reparación propuesta (β' < β, conjunto finito de desplazamientos) es la misma idea. | Aceptada como redacción. |
| G-R1-04, V con cadenas JW | **Tiene contenido.** En Eon v4 los V_{x:η} son no locales: llevan cadenas JW y la paridad del campo gauge se trata como fermión (PDF p.7, §§2.2–2.3; conmutan por la ec. (4)). En la base eléctrica, cada V_ℓ es un desplazamiento por una fase diagonal ±1 que depende de las paridades. Como conmutan, en cada componente fermiónica fija (D_M no cambia n) forman una representación de Z^M equivalente a los desplazamientos puros mediante una unitaria diagonal W. Este argumento es del autor y no tiene revisión externa. W conserva los módulos, así que las cotas gaussianas pasan. Consecuencia que no señaló el revisor: tras W, cada monomio de plaqueta puede llevar un signo ±1. Entonces el valor a = 4 «con los demás ángulos a cero» no está garantizado. `verify_eon_projected_gaussian_reference.py` (l.166–172) cuenta flujos de plaqueta sin signos JW. La prueba solo necesita a ≢ 0. Esto sigue valiendo porque a(z_{≠e}) es una suma de cuatro monomios de Laurent distintos (las cuatro plaquetas que contienen e usan conjuntos distintos de enlaces para L ≥ 3), y los signos no pueden anularla idénticamente. | **Aceptada; reparación obligatoria** en el informe: (i) escribir la equivalencia diagonal de los V; (ii) sustituir «a = 4» por el argumento de monomios distintos, o certificar los signos de plaqueta con el orden JW de Eon. |
| G-R1-05, componente no nula y a ≠ 0 | El argumento de conjuntos de ceros propios es el del informe, más detallado. | Aceptada como redacción. |
| G-R1-06, signo del control inverse-kick | Con la convención del informe, g = e^{iθB} f y B = z + 1/z dan, para f = e^{−iθ(z+1/z)}, g = 1. Es consistente. | Rechazada: depende de la misma inversión f/g de G-R1-01. |

## Estado

- Construcción del candidato: ACCEPT, sin reparaciones.
- Obstrucción Fourier/Jensen: estructuralmente correcta según el revisor y según esta lectura. Hay una
  reparación con contenido (G-R1-04: equivalencia diagonal de los V y signo del coeficiente a) y cuatro de
  redacción.
- Las reparaciones **no se han aplicado**: el informe y el certificado siguen con los bytes revisados.
  Aplicarlas, y en su caso certificar los signos de plaqueta, es un paso aparte que decide el usuario.
- No se promueve evidencia: `EXPLICIT_NORMALIZABLE_GAUSS_STATE_CONSTRUCTED / GAUSSIAN_TAIL_STATIONARITY_FAIL`
  pasa de «revisión independiente pendiente» a «ACCEPT_WITH_REPAIRS, reparaciones pendientes». Sigue sin vacío
  físico, sin correladores y sin lazo.
