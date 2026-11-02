# PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE — análisis 4B

**Fecha:** 2026-09-28
**Contrato:** `theory/PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md`
**Rama examinada:** `claude/endpoint-transfer-partial` (`a19c647`)
**Alcance:** análisis teórico referido a 4B en la clase congelada. No reabre §§8.15–8.20,
no recalcula la señal y no diseña 4A.

**Revisión documental:** 2026-09-28. Se comprobaron las tres fuentes
primarias enlazadas abajo y la consistencia dimensional de la conclusión.
Los resultados heredados de §§8.15–8.20 se toman como premisas del contrato;
esta revisión no vuelve a demostrar la ley operacional.

**Autorización y decisión posterior:** el contrato de 2026-09-17 autorizó
congelar el protocolo, no ejecutar 4B. La decisión explícita del usuario del
2026-09-28 acepta el diagnóstico revisado y cierra formalmente 4B con el alcance
de la clase congelada. Esta decisión no convierte retroactivamente el análisis
en una ejecución autorizada bajo el acto de 2026-09-17; adopta sus conclusiones
como base suficiente para el cierre terminal.

## Resultado

**Estado terminal aceptado para el modelo congelado: `NO_ABSOLUTE_SCALE_DERIVABLE`.**

La dinámica fija una relación de velocidades, pero deja una familia de escalas
absolutas. No encontré una relación física adicional que fije esas escalas **y
que esté derivada para el modelo y protocolo congelados**, junto con los modos,
operaciones y observable dimensional requeridos. Sí existe una propuesta de
gravedad discreta publicada en 2026 que postula un tiempo fundamental y relaciona
su escala con `G`; se evalúa abajo y no se puede injertar en CJWW sin una nueva
hipótesis de identificación entre dos dinámicas distintas.

La conclusión negativa se limita al modelo y al corpus revisado; no prueba que
ninguna teoría futura pueda aportar una escala física. El resultado de la corona
sigue siendo un resultado del modelo; no queda convertido en una afirmación
sobre la naturaleza.

## Criterios del contrato

| Criterio | Evaluación | Evidencia y límite |
|---|---|---|
| 1. Escala absoluta | **No derivada en el modelo congelado** | El diccionario da `c_IR^phys = a/τ`; fijar el valor físico de `c` fija el cociente, no `a` ni `τ` por separado. La familia `(a,τ)=(c_phys τ,τ)` conserva una escala libre. Una relación de otro modelo (Chrono-Grid Dynamics) requeriría justificar primero que sus variables y dinámica se identifican con CJWW. |
| 2. Diccionario físico | **Incompleto para este protocolo** | Hay interpretaciones QCA/Weyl de grados internos, pero no una realización natural identificada para los componentes, las intervenciones `M=σ_j`, el efecto `M_B` y la preparación `g(Np)` del contrato. Un simulador programado sería 4A y no llena el puente 4B. |
| 3. Observable dimensional | **Condicional, no establecido para naturaleza** | La salida del teorema es una diferencia adimensional de probabilidades. Formalmente, en `R` repeticiones ideales, la diferencia esperada de conteos sería `R δ(N)`. Falta una realización que implemente las operaciones congeladas y determine el ciclo físico de repetición; no hay una ley SI para un sistema natural candidato. |
| 4. Detectabilidad | **No puntuable sin mapa; Planck sólo condicional** | Si se impusiera `a=ℓ_P` y se asociara una distancia característica macroscópica `λ=1 m`, entonces `N≈λ/a≈6×10^34` y `K_*N≈1×10^34`; la señal sería inaccesible. Esto es un diagnóstico de la hipótesis Planck, no una predicción del QCA. |

## Restauración dimensional heredada

Se heredan, sin recalcular, la ley de §8.20 y el diccionario de §8.15:

\[
x=a n,\qquad t=N\tau,\qquad k=p/a,\qquad
c_{IR}^{phys}=a/\tau.
\]

Por tanto la ley operacional se escribe condicionalmente como

\[
\delta(T; a,\tau)=
\left|C\!\left(\left\{\frac{\sqrt3 T}{4\tau}\right\}\right)\right|
\left(\frac{T}{\tau}\right)^{-13/2}
\exp\!\left(-K_*\frac{T}{\tau}\right)
\left(1+O\!\left((T/\tau)^{-1/2}\right)\right),
\quad T=N\tau.
\]

La fase conserva la convención congelada y la fórmula se entiende en el régimen
asintótico del teorema. Si se nombra una longitud característica del protocolo
`λ=aN`, el exponente es `exp(-K_* λ/a)`. Ninguna de estas sustituciones determina
`a` o `τ`; `N→∞` tampoco equivale a un límite continuo `a,τ→0`.

Para un detector ideal que repitiese exactamente el protocolo, la diferencia
esperada de conteos sería `ΔE[n_B]=R δ(N)` para `R` ensayos independientes. Esta
identidad de conteo no aporta por sí misma la realización física, la tasa de
repetición, la eficiencia ni el ruido, y por eso no satisface el criterio 3 para
la naturaleza.

## Contraste con fuentes primarias

1. D’Ariano y Perinotti describen su hipótesis QCA como una derivación de la
   dinámica de Weyl/Dirac/Maxwell desde principios informacionales. En la p. 1
   dicen que la escala de Planck se fija mediante un **argumento heurístico**, y
   explican que el programa pretende recuperar constantes físicas como `c` y
   `ħ`; eso no es una derivación de una escala absoluta para el QCA CJWW
   congelado. [PDF primario, p. 1](https://arxiv.org/pdf/1608.02004).
2. Mlodinow y Brun calculan límites superiores para el tamaño de retículo a
   partir de dispersión y anisotropía: `Δx < 5.8×10^-36 m` con datos de GRB y
   `Δx < 6.5×10^-26 m` con resonadores (PDF pp. 18, 20). Son cotas sobre los
   parámetros de su modelo y esos observables, no una determinación de `a` o
   `τ` para nuestro protocolo ni una medición de `δ(N)`. [PDF primario,
   pp. 18, 20](https://arxiv.org/pdf/2506.20136).
3. Su conclusión mantiene abierta la alternativa entre un sustrato discreto
   fundamental y una red como herramienta de cálculo; sus resultados no
   deciden cuál describe la naturaleza (PDF p. 20).
4. Jovanović, *Chrono-Grid Dynamics* (publicado el 3 de julio de 2026), es un
   candidato nuevo y cercano que no figuraba en el rastreo local previo. El
   artículo **postula** un cuanto universal de tiempo propio `τ`; dentro de ese
   modelo obtiene `8πGβ=τ²` y, en unidades `c=1`, `a=τ`, de modo que su escala
   espacial resulta del orden de Planck (secciones 2.2 y 7.1–7.2). El propio
   texto califica `τ` como postulado fundamental. No identifica su dinámica de
   red de espines y enlaces SU(2) con el walk CJWW (5.15), ni deriva el protocolo
   `M,M_B,g(Np)` o su respuesta operacional. Por tanto ofrece una **hipótesis
   externa de escala para otra teoría**, no el mapa físico requerido aquí.
   [Artículo primario, secciones 2.2 y 7.1–7.2](https://link.springer.com/article/10.1140/epjc/s10052-026-16018-y).
5. El informe local de rastreo 4B clasifica simuladores, análogos materiales y
   propuestas fundamentales por separado y no encuentra una fuente que cubra
   las cuatro casillas para la corona congelada:
   [`2026-09-17--physical-realization-literature-scan.md`](2026-09-17--physical-realization-literature-scan.md).
   Ese rastreo se reutiliza como cobertura bibliográfica previa, no como prueba
   exhaustiva de ausencia; en particular, no incluía la propuesta Chrono-Grid
   publicada después.

## Techo y estado de repositorio

El análisis no afirma que `c` no pueda emerger de un sustrato. Indica que, en el
modelo congelado y la evidencia examinada, sólo se obtiene `a/τ=c`, sin escala
absoluta ni mapa físico para la señal operacional. La diferencia geométrica
entre soporte microscópico y cono IR sigue establecida dentro de la clase del
modelo; su traducción a la naturaleza permanece abierta.

`state/CURRENT_STATE.md` registra esta decisión como cierre branch-local en
`claude/endpoint-transfer-partial`; ese fichero sigue reconciliado con
`research/b-infinity-post-s4-gate` y `main` no se modifica. El cierre se limita
al gate 4B para CJWW (5.15) congelado. La cuestión distinta de realización física
en la extensión H1 de Sec. 9 sigue OPEN. Chrono-Grid queda como candidato sin
identificación demostrada con CJWW y no abre otra línea de trabajo.
