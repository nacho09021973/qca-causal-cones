# Lectura del autor: revisiones de Grok y Gemini de M1, etapa A y M1-B13

**Fecha:** 2026-11-03. **Autor del informe y de esta lectura:** Claude Code
(Claude Opus 5.5). **Revisiones:** `informe_grok.md` (grok-4.7, sellado,
COMPLETED) y `../2026-11-03--hex-supremum-stageA-review-gemini/informe_gemini.md`
(gemini-4-argon, COMPLETED, STOP); herramienta `ce09890`; entrada idéntica
(`inputs.sha256`, informe `8a4c4eec…`, verificador `ef4b0114…`). Base:
`8abca3c`. Esta lectura vale para las dos carpetas.

**Dictámenes:** Grok PASS en los cinco puntos; Gemini PASS en los cinco.
**Ninguna reparación obligatoria** en ninguna de las dos casas.

Los informes no son fuente. Sus afirmaciones comprobables:

| Afirmación | Comprobación | Resultado |
| --- | --- | --- |
| S13 = `{|h|^2 <= 3}`: 1 + 6 + 6 puntos (Grok); misma cuenta por coordenadas `(2a+b, b-a, a+2b)` (Gemini) | verificador: 13 puntos | Coincide |
| Normal a 60°, nivel `m = a+2b`: vértices `(1,1)`, `(-1,2)` en `m = 3`; singleton `(0,1)` en `m = 2` | `(2,0)` y `(-2,2)` tienen norma 4, fuera de S13 | Cierto |
| En S19, `d = 2(g2-g1)` tiene gcd 2: el `delta` de L0 es la mitad del ocupado, `N = 2` es correcto (Grok) | el verificador usa `N = 2` y exige niveles enteros `-2..2` | Cierto; el informe ya usa `N = 2` |
| Giro conjunto `V = e^{i pi/12 sigma_z}` conserva `A(n) = r n.sigma` y las ecuaciones de T2 (Gemini; Grok equivalente) | las diferencias `h - h'` giran en bloque; conjugación común | Cierto |
| A2 vale para todo convexo centralmente simétrico en un punto extremo | prueba del informe Sec. 1; segunda vía de Grok por soporte | Cierto |

**Aclaraciones aceptadas, sin cambio de veredicto:**
- **Grok: la segunda vía no es independiente.** Las ecuaciones de capa ya
  contienen `A_h = 0` en cada singleton; el `solve` lineal reencuentra ese
  subsistema. Es la misma geometría escrita en álgebra, no una derivación
  distinta. La frase del informe «Second route (rule 4) ... Both routes
  agree» exagera su independencia: queda anotado en el informe, en el
  párrafo de revisión, sin editar el cuerpo revisado.
- Gemini: la escala de la semejanza es 1 (el verificador ya normaliza
  `|v| = 1`); «rotation by -30 deg, scale» sobra la palabra «scale».
- Grok: «encodes the vertices abstractly» significa geometría sin red, no
  cuantificación sobre semejanzas; el giro concreto está comprobado aparte.
- Grok no ejecutó el verificador; rehízo la geometría a mano. Gemini
  tampoco lo ejecutó (sin herramientas). El 12/12 es de esta sesión.

**Estado:** M1-B13 `PROVED_FOR_S13`, HX2 `CONFIRMED_FOR_S13`, M1-A
`OPEN_AFTER_SINGLETON_LAYER_ANALYSIS`: PRELIMINARY,
INDEPENDENT_REVIEW_PASS_TWO_HOUSES, PROMOTION_PENDING. La promoción es un
commit aparte, por decisión del usuario.
