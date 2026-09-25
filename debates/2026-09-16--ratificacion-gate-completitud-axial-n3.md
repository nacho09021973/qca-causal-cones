---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-16 09:11
proyecto: /home/ignac/qca-causal-cones
tema: /tmp/claude-1000/-home-ignac-qca-causal-cones/3558c24e-9fa0-4f52-9489-c67bf5cbe8d7/scratchpad/ratificacion-gate-completitud-axial-n3.md
rondas: 1
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - ASTRA — GPT (OpenAI) — codex exec -m gpt-6-astra (sellado)
  - CLAUDE OPUS — Claude (Anthropic) — claude -p --model claude-opus-5 --effort high (sellado)
  - CIRO — Grok (xAI) — grok --model grok-4.6 (sellado)
  - ABNER — DeepSeek — api.deepseek.com/deepseek-v4-pro
ausentes:
  - GEMINI — Google — backend no disponible
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

# SANEDRÍN — RATIFICACIÓN DE `GATE_COMPLETITUD_AXIAL_N3`

## Por qué existe esta sesión

La sesión anterior (acta adjunta: rondas 1–5, residuo y veredicto) terminó en estado
`DEGRADED_NO_CONSENSUS`. ASTRA falló dos turnos por límite de uso del backend, no por
el contenido, y quedó excluida. Los cuatro miembros restantes propusieron
`AUTHORIZE_C` con `GATE_COMPLETITUD_AXIAL_N3` y las enmiendas (a)–(e).

La preferencia registrada de ASTRA era A. Su objeción quedó sin respuesta: C sólo toca
`c_strict^iso` a través de una cota que todavía no está demostrada.

Estado registrado hoy:

`GATE_COMPLETITUD_AXIAL_N3 = CANDIDATE_FROM_DEGRADED_DEBATE` — **no autorizado**.
No se ha ejecutado ningún paso de su charter.

Esta sesión **no repite el debate general**. Es una ratificación o reparación corta.

## Tres cambios respecto del acta anterior

### 1. ASTRA está presente

ASTRA interviene primero y debe exponer su objeción a C. Debe responder también a la
afirmación de CLAUDE OPUS (ronda 5) de que el punto (3) de C incorpora A con su propio
FAIL.

### 2. Corrección de premisa: nilpotencia de vértices

La errata ya está registrada en el charter histórico y en `CURRENT_STATE`.

- Para un vértice extremo `h`, el coeficiente de `U^n` en `n·h` es exactamente
  `T_h^n`. Si `T_h` es nilpotente, `n·h ∉ S_n` para `n` grande.
- Por el lema de vértices: si los ocho coeficientes de vértice son no nilpotentes,
  entonces `C_∞^strict = C_micro` y hay saturación. Por tanto, un fallo de saturación
  `c_strict^iso < r_in` **requiere** al menos un vértice nilpotente.
- **La implicación recíproca no está establecida.** Perder el rayo exacto `n·h` no
  determina por sí solo `h_∞` ni `c_strict^iso`: palabras mixtas pueden seguir
  llegando cerca del vértice, y un cuerpo truncado cerca de un vértice no tiene por
  qué perder soporte mínimo. La saturación debe calcularse o demostrarse.

Todo argumento del acta anterior que use «vértice nilpotente ⇒ caída de saturación»
queda sin apoyo.

**Observación complementaria (no revisada; no es resultado de ningún gate).** En
`N_3`, sea `h` un vértice con `T_h^m = 0`. Ninguna palabra con producto no nulo
contiene `m` copias consecutivas de `h`, así que al menos `⌊n/m⌋` letras de cada
palabra son vértices distintos de `h`. La mayor proyección de un vértice BCC
distinto de `h` sobre `ĥ = h/‖h‖` es `1/3`. Por tanto

`h_∞(ĥ) ≤ ((m−1)·1 + 1/3)/m = 1 − 2/(3m) < 1 = h_{C_micro}(ĥ)`.

Esto es sólo una cota superior; el patrón `m−1` veces `h` más un vecino la alcanza
únicamente si esas palabras tienen coeficiente no nulo. Lectura correcta: **la
nilpotencia sí contrae estrictamente el cuerpo estricto en la dirección de ese vértice,
pero no implica que disminuya `min_n̂ h_∞(n̂) = c_strict^iso`.** Para todo `m ≥ 2` la
cota en `ĥ` es `≥ 2/3 > 1/√3`, de modo que no decide el inradio. Conviene recordar
además que la pérdida *completa* de un vértice del cuerpo sí bajaría el inradio del
cubo (conv de los 7 restantes está a distancia `1/3`). Lo que puede conservarlo es un
recorte poco profundo producido por palabras mixtas.

### 3. L1 tiene una derivación elemental candidata

Esta derivación **no está revisada ni registrada como resultado**. Para una dirección,
escríbase

`U(k_x, k_⊥) = e^{-ik_x/√3} X_+(k_⊥) + e^{+ik_x/√3} X_-(k_⊥)`.

- `U†U = I` no tiene modos de Fourier `±2/√3` en `k_x`, luego `X_+†X_- = X_-†X_+ = 0`.
- Análogamente, de `UU† = I` se obtiene `X_+X_-† = X_-X_+† = 0`.
- Entonces `P_± = X_±†X_±` son proyectores ortogonales complementarios.
- De ahí `J_x = iU†∂_xU = (P_+ − P_-)/√3`, y por tanto `J_x² = I/3`.

Insertando `I = P + Q` se obtiene

`(1/r)Tr[(PJ_xP)²] + (1/r)Tr[PJ_xQJ_xP] = 1/3`.

Si la hipótesis de cúmulo cónico garantiza `(1/r)Tr[(PJ_xP)²] = c_0²`, el punto (2)
sin la identificación métrica es completitud inmediata.

Consecuencias que debe considerar el Sanedrín:

- el primer paso autorizado de C casi no puede fallar;
- la capacidad de falsación de C reside en (3) y en la identificación métrica para
  degeneraciones arbitrarias;
- que L1 sea fácil **no es razón suficiente para elegir C**;
- L1 no debe presentarse como novedad: está muy cerca de un walk condicional/bipartito
  en esa dirección y del mecanismo de completitud de Arrighi–Facchini (AF16/17).

## Pregunta única

> Con estas dos correcciones y considerando que `c_0 ≤ c_strict^iso` sigue sin
> demostrarse, ¿ratificas `GATE_COMPLETITUD_AXIAL_N3`, prefieres A, o rechazas ambos?
> Señala específicamente si C estudia de forma suficientemente directa el cuerpo
> estricto o si sólo obtiene una identidad cinemática independiente de él.

Exigencia adicional, que no se puede sustituir por un voto:

> L1 y la identidad de defecto son locales/espectrales y esencialmente de un paso;
> `c_strict^iso` es un objeto asintótico de soporte. Si ratificas C, indica qué tipo
> de argumento podría conectar ambos niveles. Si no ves ningún puente plausible,
> explica por qué C sigue siendo un gate científicamente preferible a A.

## Advertencia sobre el nombre del gate

El nombre `GATE_COMPLETITUD_AXIAL_N3` puede inducir una falsa continuidad lógica. Las
partes (1) y (2) son **axiales**: usan la bipartición del cubo en una dirección
coordenada. En cambio, (3) necesita controlar **todas las direcciones**, porque

`c_strict^iso = min_n̂ h_∞(n̂)`,

y ese mínimo no tiene por qué alcanzarse en las normales de cara. Probar algo sólo
para `x, y, z` no basta para el techo isotrópico. Este salto debe reconocerse como
problema abierto del charter, no quedar escondido dentro del nombre.

## Formato — una sola ronda

Cada miembro debe dar, en este orden:

1. **Voto:** `RATIFY_C`, `PREFER_A` o `REJECT_BOTH`.
2. **Respuesta directa y puente:** ¿C estudia el cuerpo estricto, o sólo da una
   identidad cinemática independiente de él? Qué argumento podría conectar el nivel
   local/axial con `c_strict^iso` en todas las direcciones o, si no hay ninguno
   plausible, por qué C sigue siendo preferible a A.
3. **Si vota `RATIFY_C`:** como máximo tres enmiendas obligatorias al charter en vista
   de L1 y de la errata. En particular, decir si el primer paso autorizado debe ser
   (3), o una parte de (3), en lugar de L1.
4. **Si vota `PREFER_A`:** qué cambia, si algo, respecto de `GATE_A_N3` del acta.
5. **Condición de cambio:** qué resultado negativo de la primera prueba le haría
   cambiar de voto.

No se permiten propuestas de gates nuevos distintos de A y C.

## Restricciones (se mantienen)

1. No abrir nuevas clases de sustrato, causal sets, interacciones ni gravedad discreta.
2. No búsquedas numéricas amplias.
3. No asumir novedad bibliográfica.
4. No convertir una identidad de familia en ley general.
5. No añadir condiciones sólo porque excluyen el contraejemplo (restricción 8).
6. Mantener separados `C_micro`, `c_strict^iso`, velocidad de grupo y `c_0`.
7. Nadie debe presentar L1, (2) o (3) como resultado establecido.

Esta sesión no autoriza ciencia nueva por sí misma.

## Salida exigida en el veredicto

Exactamente una:

- `AUTHORIZE_C`, con el texto final del charter tras las enmiendas ratificadas y el
  primer paso autorizado;
- `AUTHORIZE_A`, con el charter final de A;
- `NO_GATE_YET`, con la razón.

Si alguna intervención falla, el veredicto no valida nada y debe decirlo.

## Contexto

### Contexto adjunto: /tmp/claude-1000/-home-ignac-qca-causal-cones/3558c24e-9fa0-4f52-9489-c67bf5cbe8d7/scratchpad/acta-degradada-rondas.md
```
# ACTA DEGRADADA — sesión 2026-09-15 11:00 (extracto: rondas 1–5, residuo, veredicto; sin adjuntos ni traducción)

## Ronda 1 — CLAUDE OPUS

**1. Qué demuestra el contraejemplo.** [SOURCE] Localidad, unitariedad, homogeneidad, covariancia D2 con `R_i=σ_i⊗I_2`, dinámica irreducible y cuerpo estricto `C_∞^strict=C_micro` fijos no fuerzan `c_0=c_strict^iso`: la pendiente Weyl varía como `a/√3`. [SOURCE] La clase se declaró después de construir el ejemplo y `R` es reducible. [INFERENCE] El contraejemplo no dice nada sobre la dirección opuesta, es decir, sobre si puede darse `c_0>c_strict^iso`. Tampoco muestra que la mezcla sea la única vía de desaturación: sólo muestra que en esta familia lo es.

**2. Qué sigue vivo.** La cota A, y probablemente con poco esfuerzo. [INFERENCE] El argumento sería este. Se restringe `U(k)^n` a la recta `k_0+t n̂`. Se obtiene una función matricial unitaria de tipo exponencial, con espectro en `{n̂·x : x∈S_n}`. Tras centrar con una fase, la desigualdad de Bernstein para funciones con valores operadoriales, junto con Hellmann–Feynman, pone cada velocidad de fase propia en `[min, max]` de ese conjunto dividido por `n`. Tomando el ínfimo en `n` (Fekete, [SOURCE] en el charter), `n̂·v_grp ≤ h_∞(n̂)`. En el cono isótropo, `v=c_0 n̂` como límite lateral, lo que da `c_0 ≤ c_strict^iso`. [UNVERIFIED] La versión de Bernstein para funciones con valores de Banach es la clásica. [SOURCE] El repositorio declara expresamente no usar la inclusión `V_grp ⊆ C_∞^strict`. **Condición de concesión:** que falle Bernstein operadorial en forma centrada, o que en nodos degenerados el coeficiente `c_0` del Hamiltoniano efectivo no sea límite de derivadas de ramas propias. Mientras no se dé ninguna de las dos, A es un lema de pocas líneas y no un gate. Esto confirma el riesgo de "casi tautológica" que ya señala el tema.

**3. Dirección inicial: C, reformulada.** No planteo C como generalización de la fórmula con métrica, sino a partir de un hecho que parece general en esta geometría.

- [INFERENCE] Tómese cualquier símbolo unitario con soporte `N_3`, cualquier `s`, a lo largo del eje `x`. Todos los vértices proyectan a `±1/√3`, así que `A = e^{-iq}X_+ + e^{iq}X_-`.
- Las dos identidades de unitariedad dan `X_+^†X_- = 0` y `X_+X_-^† = 0`. Entonces `Π_± = X_±^†X_±` son proyectores complementarios.
- En `k=0`, `J_x = iA^†∂_xA = (Π_+ − Π_-)/√3`, luego `J_x² = I/3` **para todo símbolo de la clase, no sólo para el ansatz**.
- Para cualquier sector `P` en el nodo, `P J_x² P = (PJ_xP)² + PJ_xQJ_xP`.
- Con cono no inclinado, el primer término vale `c_0²` sobre el sector.

Resultado candidato: `c_0² + ‖QJ_xP‖²_norm = r_in²`, con igualdad `c_0 = r_in` si y sólo si `[P, Π_+] = 0`. La identidad de la familia `A_{a,θ}` sería la especialización a dos sectores.

Si esto se sostiene, cambian tres cosas:
- **D queda reducida a un corolario.** Si el sector ocupa todo `C²`, entonces `Q=0` y `c_0 = 1/√3` sin Eq. (2) de P17. Con `Π_+` de rango 2 habría inclinación, que ya está excluida.
- **B cae sobre sí misma.** Toda condición de saturación debe implicar `[P, J_n̂] = 0`.
- **La saturación geométrica se separa de la de cono.** `c_strict^iso = r_in` es la no nilpotencia de vértices, ya certificada en ambos casos.

**Condición de concesión:** que falle la descomposición axial (por ejemplo, que `X_+^†X_- ≠ 0` sea compatible con unitariedad en `N_3`), o que el coeficiente de cono no coincida con el espectro de `PJ_xP` en sectores degenerados. El alcance tiene un límite que marco como [INFERENCE]: todo esto depende de que la dirección que minimiza `h_C` biparta el soporte en dos hiperplanos soporte. Eso ocurre en el cubo y no es general.

**4. Descartes.**
- **D como gate.** Es un lema, por lo anterior.
- **La hipótesis "R irreducible" dentro de B.** [INFERENCE] Las representaciones proyectivas irreducibles de `Z_2×Z_2` con cociclo no trivial son de dimensión 2 y únicas, porque el álgebra torcida es `M_2(C)`. En la clase de Pauli, "R irreducible" equivale entonces a `s=2` y no aporta una hipótesis independiente. Condición de concesión: admitir un grupo de isotropía mayor que D2, lo que la restricción 1 prohíbe cambiar dentro de la comparación.

**Objeción más fuerte, contra el objetivo del tema.** Si lo anterior es correcto, cualquier condición que "restaure" la igualdad es equivalente a `[P, J_n̂] = 0`: el sector relativista es invariante bajo la involución de velocidad microscópica. Esa condición es exactamente la de igualdad en Bernstein y reformula la conclusión. No es una hipótesis física independiente, y la restricción 8 la vetaría como post-hoc salvo que algo externo la implique. La única implicación independiente a la vista es "el sector agota el espacio interno", que es minimalidad pura y, [INFERENCE], no explica `c`: la elige. La afirmación fuerte buscada ("bajo condiciones físicamente justificables el sector debe saturar") quedaría entonces sustituida por una ley exacta de **presupuesto** (`c_0² = r_in² − mezcla`) más una elección de minimalidad. Esa ley sí es defendible, pero es una cota con defecto medido, no una derivación de `c`.

**Condición de concesión:** exhibir un principio con motivación independiente que implique `[P, J_n̂] = 0` sin equivaler a él, dentro de las restricciones 1 a 4. Candidatos serían la estabilidad del sector bajo iteración, o la compatibilidad de la separación del sector con la localidad finita en todo `k` y no sólo en el nodo. Si ninguno lo implica, el veredicto honesto es C como gate con el objetivo rebajado explícitamente.

## Ronda 1 — ASTRA

[SOURCE] Concuerdo con CLAUDE OPUS en el alcance del contraejemplo: la dinámica es irreducible, la representación interna de D2 es reducible y ambos sectores Weyl tienen velocidad ajustable con el mismo cuerpo causal estricto. Concuerdo también con su distinción entre una identidad de compresión interna y una explicación física de la saturación.

[INFERENCE] El contraejemplo elimina algo adicional: cualquier cota inferior universal positiva para el cociente `c_0/c_strict^iso` basada exclusivamente en las condiciones que conserva la familia. Ese cociente es `a` y puede acercarse arbitrariamente a cero dentro del intervalo admisible. No demuestra únicamente que falle la igualdad; demuestra que esas condiciones tampoco garantizan proximidad a ella. Esto no requiere incluir el extremo `a=0`.

[INFERENCE] Mi objeción principal a la preferencia de OPUS por C afecta al término que se pretende repartir. Reconstruyo su propuesta más fuerte: la geometría axial de `N_3` y la unitariedad podrían imponer una identidad exacta para cualquier símbolo admisible, y la compresión al sector Weyl convertiría esa identidad en una regla de velocidad más mezcla. Sería un avance respecto de una fórmula propia del ansatz. Pero su término total sería `1/3`, fijado por el soporte de un paso. Todavía no sería `(c_strict^iso)^2`.

[SOURCE] La revisión independiente distingue expresamente ambos pasos: la descomposición mediante proyectores no establece la igualdad del presupuesto con la velocidad estricta; en la familia, esa identificación necesita además el certificado de supervivencia de vértices. El estado declara abierta la saturación del cuerpo microscópico para otros símbolos.

[INFERENCE] Por tanto, el ascenso injustificado aparece en «toda condición de saturación debe implicar `[P,J_n̂]=0`». El argumento expuesto apunta a una condición de igualdad con `1/√3`. No establece esa necesidad para la igualdad buscada, `c_0=c_strict^iso`, cuando el segundo miembro pudiera ser menor que `1/√3`. Tampoco queda D resuelta como comparación estricta solamente por obtener su pendiente: falta justificar el puente entre pendiente espectral y soporte asintótico, o certificar directamente ese soporte. **Condición de concesión:** demostrar, para toda la clase pertinente, que `c_strict^iso=1/√3`, o reformular la identidad con el cuerpo estricto y probar esa reformulación sin asumir la saturación microscópica.

[INFERENCE] Mi preferencia inicial es A. La versión viva de «`c` viene del sustrato» debe distinguir dos contenidos: que el sustrato limita la velocidad del sector y que determina su valor. El segundo está refutado bajo las condiciones declaradas; el primero sigue pendiente como afirmación general. Resolverlo establece qué significa exactamente llamar «límite» al cuerpo estricto en esta discusión.

[INFERENCE] No acepto descartar A porque su demostración pudiera ser breve. Una implicación entre soporte exacto y pendientes espectrales no es una tautología definicional: relaciona objetos distintos. El esquema de OPUS constituye una razón para esperar un cierre exacto barato, no para contabilizarlo ya como resultado. **Condición de concesión:** si ese esquema queda convertido en prueba completa dentro de la clase congelada, A deja de necesitar un gate posterior; entonces reconsideraría C, conservando explícitamente su deuda con el cuerpo estricto.

[INFERENCE] No descartaría inmediatamente ninguno como candidato científico. B necesita una hipótesis independiente; C necesita identificar qué presupuesto mide; D necesita controlar sus equivalencias y su alcance. Sí descartaría presentar cualquiera de esos trabajos como recuperación de la igualdad antes de cerrar el paso específico que lo conecta con `c_strict^iso`.

## Ronda 1 — CIRO

Concuerdo con CLAUDE OPUS en el alcance del contraejemplo y en que no prueba que la mezcla sea la única vía de desaturación. Concuerdo con ASTRA en que el cociente `c_0/c_strict^iso` carece de cota inferior universal positiva bajo las condiciones que la familia conserva, y en que el presupuesto axial, si existe, iguala `r_in^2` y no automáticamente `(c_strict^iso)^2`.

**1.** [SOURCE] El contraejemplo demuestra el fallo de la casilla (i) del charter con éxito de (ii): `0<c_0(a)<c_strict^iso` para el cuerpo estricto *propio*, y a la vez `C_∞^strict=C_micro`. Eso es más preciso que «falla la igualdad»: desacopla el cono lineal local del soporte exacto global *sin* encoger el politopo de un paso. [SOURCE] La dinámica es irreducible y `R` es reducible; los nodos Weyl viven en cúmulos de Floquet `±θ`, no en una fase global. [SOURCE] Es un ansatz de producto, no una clasificación `s=4`; la clase se escribió después de construir, así que refuta toda clase que lo contenga, no una clase `s=4` predeclarada. [SOURCE] `c_strict^iso` es soporte exacto; no hay enunciado de frente balístico ni de Lieb–Robinson. [INFERENCE] El mecanismo operativo es que el sector relativista ocupa un subespacio espectral propio del espacio interno, con un bloque complementario a otra cuasienergía, aun sin suma directa constante.

**2.** [SOURCE] Sigue en pie `c_strict^iso≤r_in(C_micro)` y el certificado Pavia `s=2`. [INFERENCE] La tesis viva ya no es que el sector relevante *deba igualar* el límite del sustrato, sino que el sustrato fija un techo de soporte exacto y que el sector de baja energía puede ceder parte de la norma de los generadores a canales internos. [INFERENCE] Lo muerto es que localidad, unitariedad, homogeneidad y D2, con cuerpo estricto lleno, fuercen saturación. Lo que no está ni vivo ni muerto es si `c_0` puede superar `c_strict^iso` cuando (ii) falla.

**3.** Dirección inicial: **C**, con la deuda que marca ASTRA como parte del enunciado y no como un ascenso. [INFERENCE] Tras `s=4`, el contenido no tautológico de «`c` viene del sustrato» es una ley de defecto, no la desigualdad. A, si es verdadera, no explica el contraejemplo; sólo acota un objeto que ya queda por debajo. C pregunta si unitariedad y soporte `N_3` imponen una relación de completitud que parte una norma de generadores entre cono local y canales complementarios, y *por separado* si el total es `r_in^2` o `(c_strict^iso)^2`. [SOURCE] La identidad ponderada de `A_{a,θ}` está demostrada sólo para esa familia y no se promociona. [INFERENCE] El hecho axial `J_x^2=I/3` que esboza OPUS, si se sostiene, es independiente del ansatz y da a C un ancla que no viola la restricción 7. **Condición de concesión:** que la restricción axial no fuerce `X_+^†X_-=0`, o que `c_0` no coincida con el espectro de `PJP` en cúmulos degenerados, o que el total del presupuesto no se identifique con el cuerpo estricto sin un certificado de vértices.

No elijo A como gate. [INFERENCE] El esquema Bernstein–Hellmann–Feynman sobre `U^n` acota velocidades de grupo de *ramas del símbolo completo*. Eso no es definicionalmente `c_0`: `c_0` es la linealización de un cúmulo aislado, posiblemente Floquet-desplazado, cuya velocidad es una compresión `PJP`. Esa compresión da de inmediato `c_0≤‖J‖`, y con el corte de un paso `c_0≤r_in`, que es más débil que A. El único régimen donde A es no trivial respecto de esa compresión es el de vértices nilpotentes, `c_strict^iso<r_in`, con cono local aún del orden de `r_in`. [SOURCE] La familia `s=4` no explora ese régimen: allí (ii) se cumple. **Condición de concesión:** una prueba de que toda rama, incluido el Hamiltoniano efectivo de un cúmulo degenerado y con enrollamiento de rama de `U^n`, cumple `|∇ω|≤H_n/n`. Si esa prueba existe, A es un lema auxiliar de C, no el siguiente gate. No contabilizo esa prueba como hecha.

**4.** Descarto **B** de inmediato como gate autónomo. [INFERENCE] Toda hipótesis extra que restaure la igualdad, para no violar la restricción 8, necesita motivación independiente de excluir `s=4`. [INFERENCE] «`R` irreducible» en D2 proyectivo de clase Pauli colapsa a `s=2`, como dice OPUS; saturación de una desigualdad operadorial del tipo `[P,J]=0` reformula la conclusión. B se duplica entonces en D o es post-hoc. **Condición de concesión:** un principio independiente —estabilidad del sector bajo iteración, o localidad finita del proyector en todo `k`— que implique saturación sin equivaler a ella.

No descarto D como tarea de contrato: [SOURCE] el emparejamiento origen/`r_in` en la clase mínima publicada es aplicación condicional de P17 más el certificado estándar, y la transferencia del cuerpo estricto por equivalencias no está comprobada. [INFERENCE] Eso no es el gate de emergencia de `c`; un PASS dejaría intacta la pregunta que `s=4` acaba de abrir. No descarto A como lema; la descarto como *único* siguiente gate.

## Ronda 1 — ABNER

Concuerdo con ASTRA y con CIRO en que la identidad de presupuesto axial da contra `r_in`, no automáticamente contra `c_strict^iso`. Concuerdo con CIRO en descartar B como gate autónomo. Disiento de CLAUDE OPUS en tratar A como lema ya ganado: no lo está, y sin él C no toca el cuerpo estricto.

**1.** [SOURCE] El contraejemplo demuestra fallo de la casilla (i) con éxito de (ii): `0<c_0(a)<c_strict^iso` y `C_∞^strict=C_micro`. [INFERENCE] Lo específico es que la igualdad falla por un defecto puramente interno, sin encoger el soporte exacto. [SOURCE] La revisión independiente separa la descomposición en proyectores de la supervivencia de vértices. [INFERENCE] Por tanto conviene distinguir dos defectos: `D_sop = r_in² − c_strict²` y `D_esp = c_strict² − c_0²`. En el contraejemplo `D_sop=0` y `D_esp>0`; la familia no informa sobre `D_sop>0`.

**2.** [INFERENCE] La parte viva de “`c` viene del sustrato” es una ley de techo con doble defecto, no una igualdad. El sustrato fija `r_in`; el soporte estricto puede retener menos que `r_in`; el sector Weyl puede ceder además parte a mezcla interna. Eso mantiene al sustrato como límite, pero no como determinante del valor.

**3.** Dirección inicial: C, reformulada como separación de esos dos defectos. [RECONSTRUCTION] Si la descomposición axial de OPUS se sostiene, unitariedad sobre `N_3` da una relación del tipo `c_0² + Q_int = r_in²`, donde `Q_int` mide compresión interna. [SOURCE] En la familia `A_{a,θ}` la identidad se cierra contra `(c_strict^iso)²` en el punto certificado porque allí `c_strict^iso=r_in`. [INFERENCE] La versión defendible no es un presupuesto total contra el cuerpo estricto, sino `r_in² = c_0² + D_sop + D_esp`. [SOURCE] El acta declara abierta la saturación general del cuerpo estricto, así que no puede ascenderse la identidad de la familia a una ley con total estricto sin prueba.

**4.** A no es un lemma ya ganado. [INFERENCE] Para que C hable del límite real del sustrato hace falta probar `D_esp≥0`, es decir `c_0≤c_strict^iso`; eso no se sigue de `c_0≤r_in`. **Condición de concesión:** una prueba completa de la cota tipo Bernstein, válida para cúmulos Floquet degenerados y no sólo ramas regulares del símbolo completo, desactivaría esta objeción. Mientras esa prueba no exista, A es deuda interna de C, no un gate separado ni un resultado tácito.

**5.** D no debe ser el único siguiente gate. [SOURCE] El acta afirma que el emparejamiento en la clase `s=2` es aplicación condicional de P17 más el certificado estándar, no un teorema nuevo. [INFERENCE] Un PASS de D cerraría la clase mínima ya publicada y dejaría intacta la desaturación `s=4`. **Condición de concesión:** si el objetivo se rebajara a certificar rigurosamente la clase mínima, D sería correcto; para el objetivo declarado, es insuficiente.

No descarto B en abstracto, pero antes de identificar exactamente qué defecto anula una hipótesis extra, B corre riesgo de ser post-hoc. [INFERENCE] Si C deja la saturación espectral equivalente a una conmutación con el generador axial, B queda como búsqueda de una motivación independiente para esa conmutación; por eso es derivada, no primera.

## Ronda 1 — GEMINI

Concuerdo con ASTRA y ABNER en que la cota A no es un lema trivial ya ganado. Disiento frontalmente de CLAUDE OPUS, CIRO y ABNER en su preferencia por C: su versión del "presupuesto" destruye el avance conceptual del proyecto.

**1. Qué demuestra el contraejemplo.** [SOURCE] Demuestra que en la clase `s=4` declarada, el cono lineal local puede no saturar la propagación asintótica estricta de la propia dinámica, incluso cuando ésta alcanza el máximo geométrico posible (`c_strict^iso = r_in`). [INFERENCE] Esto prueba que el soporte global iterado no esclaviza incondicionalmente la pendiente de un sector de baja energía.

**2. Qué sigue vivo.** [INFERENCE] Únicamente la tesis de que el límite asintótico exacto del sustrato opera como un techo infranqueable: `c_0 ≤ c_strict^iso`. La saturación queda como un fenómeno contingente a explicar, pero su rol como límite absoluto es el núcleo remanente de la intuición original.

**3. Dirección inicial: A.** [INFERENCE] Es imperativo establecer A para justificar que `c_strict^iso` ejerce control físico sobre `c_0`. Ataco la preferencia mayoritaria por C. El "presupuesto axial" propuesto por OPUS (`J_x^2 = I/3`) es una identidad construida exclusivamente con los generadores de un paso. Su lado derecho siempre será `r_in^2`, sin importar el comportamiento asintótico. 
[SOURCE] El acta establece que un símbolo admisible puede tener vértices nilpotentes, lo que implica `c_strict^iso < r_in`. [INFERENCE] En ese escenario, el término de "mezcla interna" de la ecuación de OPUS absorbería ciegamente la deficiencia combinatoria del soporte asintótico (lo que ABNER llama `D_sop`) junto con la verdadera compresión inter-sectorial (`D_esp`). Al elegir C, el Sanedrín abandonaría el cuerpo asintótico `B_infty^*` para regresar furtivamente a la refutada comparación contra el inradio de un paso `B*`. El presupuesto de un paso no dice nada sobre el límite causal del sustrato iterado, a menos que ya sepamos que dicho límite es igual a `r_in`.
**Condición de concesión para retirar el ataque a C:** formular una relación de completitud que aísle matemáticamente el término `c_strict^iso` evaluando el comportamiento asintótico, sin presuponer el caso especial `c_strict^iso = r_in`. Mientras C sea una identidad de un paso, es un espejismo algebraico.

**4. Descartes.** 
- **C como gate autónomo.** Queda descartado por responder a la pregunta equivocada (inradio) en lugar del objetivo asintótico.
- **B.** [INFERENCE] Restringir la clase imponiendo conmutación `[P, J_n] = 0` o minimalidad `s=2` para forzar la saturación viola la restricción de no añadir condiciones ad-hoc (regla 8). Su motivación independiente está ausente. 
- **D.** [SOURCE] El emparejamiento en `s=2` es una aplicación condicional de P17. [INFERENCE] Limpiarlo es higiene bibliográfica, pero no extrae principios físicos generales sobre la emergencia de `c`. 

Señalo un ascenso injustificado de ABNER y CIRO: apoyan C con la esperanza de "separar los dos defectos", pero [INFERENCE] ningún operador local en el nodo `k=0` puede codificar si una matriz en la frontera de Brillouin (`A_h`) es nilpotente a potencias altas. El defecto de soporte asintótico es invisible para el álgebra local del presupuesto de C. Por tanto, el único gate científico genuino hacia el objetivo original es certificar el límite universal: A.

## Ronda 2 — ASTRA

[INFERENCE] Concedo a CIRO y ABNER que C puede formularse conservando explícitamente su deuda con el cuerpo estricto. Retiro cualquier lectura según la cual preferir C implique necesariamente confundir ambos cuerpos. Eso no convierte esa deuda en un resultado, pero tampoco justifica llamar «espejismo algebraico» a toda relación de compresión.

[INFERENCE] La versión más fuerte del ataque de GEMINI sostiene que los datos del presupuesto en el nodo no determinan el soporte iterado. Es una objeción pertinente como exigencia de prueba; su afirmación «ningún operador local […] puede codificar» ese soporte asciende injustificadamente de una conexión no demostrada a una imposibilidad universal. Para sostenerla haría falta precisar qué datos locales se permiten y demostrar su insuficiencia, por ejemplo mediante dos símbolos admisibles con esos mismos datos y distinto cuerpo estricto. **Condición de concesión:** una demostración de esa indistinguibilidad desactivaría mi ataque para los datos especificados.

[SOURCE] Además, `A_h` está definido en el acta como coeficiente de Fourier asociado al desplazamiento `h`, no como matriz evaluada en la frontera de Brillouin.

[INFERENCE] Tampoco acepto como cierre matemático que un vértice nilpotente implique automáticamente `c_strict^iso<r_in`. La versión fuerte del argumento sería que su desaparición produce una pérdida proporcional al tiempo en alguna dirección que determina el mínimo isotrópico. Pero perder el desplazamiento extremo exacto no demuestra por sí solo esa pérdida asintótica: faltaría controlar desplazamientos próximos; después faltaría establecer que cambia el mínimo, no solamente alguna función de soporte. **Condición de concesión:** aportar ambos controles para la clase discutida. Esta reserva alcanza también a las formulaciones categóricas del informe de referencia; figurar en el acta no completa un paso lógico.

[INFERENCE] Contra C, la dificultad nueva está en la reformulación de ABNER. Reconstruida favorablemente, pretende convertir dos mecanismos distintos en magnitudes comparables. Sin embargo, definir `D_sop=r_in²−c_strict²` y `D_esp=c_strict²−c_0²` hace que su suma propuesta sea una cancelación algebraica. No identifica dos mecanismos independientes ni permite atribuir cada diferencia a un canal. El resultado trivial que mataría **esa versión** de C sería obtener únicamente dicha recomposición, incluso acompañada de nombres físicos. **Condición de concesión:** caracterizar independientemente los defectos y demostrar su relación con soporte y mezcla, sin definirlos mediante las velocidades cuya relación se intenta explicar.

[SOURCE] Sobre B, el informe de fuentes registra que la dimensión dos se selecciona como mínima no trivial en P14.

[INFERENCE] Por eso el descarte de GEMINI es excesivo: minimalidad tiene una motivación matemática anterior al contraejemplo. La versión fuerte de B exige justificar además su pertinencia física; no exige que toda hipótesis estructural se derive de la igualdad. B podría fracasar rápidamente ante un símbolo que satisfaga la hipótesis congelada y desature. **Condición de concesión:** si la hipótesis finalmente elegida carece de motivación independiente o presupone la saturación, aceptaré descartarla como post-hoc.

[INFERENCE] D sigue teniendo una salida rigurosa pero estrecha: verificar que las equivalencias preservan exactamente los observables comparados. Su fracaso decisivo sería una excepción admisible a la igualdad; una equivalencia no comprobada sólo deja una laguna. Ni ese trabajo es automáticamente trivial ni su éxito demostraría que la minimalidad resulta físicamente obligatoria.

[INFERENCE] Mantengo A como preferencia. Concedo que no determina el valor de `c_0`; sí resolvería si el cuerpo estricto constituye su techo. Un cono admisible que lo superase mataría A directamente. Una prueba completa y breve cerraría favorablemente el gate: la brevedad sería una ventaja, no una razón para sustituirlo por C antes de tenerla.

## Ronda 2 — CIRO

Concedo a ASTRA el hueco lógico sobre vértices nilpotentes. [SOURCE] El lema de convexidad del certificado Pavia sólo dice que `n.h` exige la palabra `h+…+h` y que `A_h` no nilpotente pone ese vértice en `S_n/n`. La recíproca quita el extremo; no controla `min h_∞`. En el cubo ese mínimo se alcanza en las normales a las caras, y una cara conserva soporte `1/√3` mientras sobreviva un vértice suyo. [INFERENCE] «vértice nilpotente ⇒ `c_strict^iso<r_in`» es un ascenso. Condición de concesión: en la clase, la nilpotencia extrema baja el mínimo isotrópico, no una sola dirección. Esto alcanza el lenguaje categórico del charter sobre (ii).

Suscribo la objeción de ASTRA a GEMINI sobre la imposibilidad de que datos locales codifiquen el soporte iterado. Añado: [INFERENCE] esa indistinguibilidad, si se demostrara, mataría la identificación del total con `(c_strict^iso)^2` sin certificado de vértices, no una ley de completitud de generadores. Esa deuda ya era parte del enunciado.

**A.** Reconstruyo la versión fuerte de GEMINI y ASTRA: sin techo espectral, `c_strict^iso` no controla `c_0`; el esquema Bernstein no está cerrado para cúmulos degenerados. Concedo que A no es tautología y no está demostrada. [INFERENCE] Un PASS no produce la afirmación fuerte pedida. Tras `s=4` el sector ya puede alejarse arbitrariamente del techo bajo las hipótesis conservadas; demostrar el techo convierte `B_∞^*` en desigualdad: un repliegue. [SOURCE] La nota `s=4` niega frente balístico y Lieb–Robinson: el objeto es soporte exacto, con amplitudes que pueden decaer. [INFERENCE] A puede ser verdadera y físicamente inerte. Resultado trivial que la mata como gate de emergencia: acotar `∇ω` de ramas del símbolo completo y dejar sin control la compresión `PJP` de un cúmulo Floquet. Un cono con `c_0>c_strict^iso` la mata como teorema; eso no la hace la ruta hacia una ley precisa. Condición de concesión: mostrar por qué el techo, y no la ley de defecto, es ahora el contenido no tautológico de «`c` viene del sustrato».

**C.** Concedo a GEMINI que el esbozo de OPUS, al pie, es identidad de un paso contra `r_in^2` y, sin la deuda, regresa a `B*`. [INFERENCE] El riesgo propio es otro: definir `‖QJP‖^2` como resto pitagórico de `PJ^2P` es tautológico para cualquier corte ortogonal. El contenido no trivial es `J_x^2=I/3` para todo símbolo de soporte `N_3`, y que el coeficiente del cono coincida con el espectro de `PJP` en cúmulos degenerados. C muere si `X_+^†X_-≠0` es compatible con unitariedad, o si esa coincidencia espectral falla. Suscribo a ASTRA contra ABNER: definir `D_sop` y `D_esp` por las velocidades es cancelación algebraica, no dos canales. [INFERENCE] GEMINI trata «C usa generadores de un paso» como «C responde a la pregunta equivocada». El objetivo tras el contraejemplo es una ley que ligue el sector al sustrato; A no explica el defecto que `s=4` acaba de exhibir. Condición de concesión: si el término de mezcla no puede caracterizarse con independencia del resto, y el puente al cuerpo estricto no puede aislarse como lema, C es espejismo. Mientras el ancla axial sea comprobable en la clase congelada, C sigue siendo la dirección que explica el contraejemplo en lugar de acotarlo.

**B.** ASTRA rehabilita B porque [SOURCE] P14 selecciona `s=2` como mínima no trivial, motivación anterior al contraejemplo. [INFERENCE] Eso no salva B como gate autónomo: esa hipótesis *es* D. B no-D exigiría otra (estabilidad del sector bajo iteración, localidad finita del proyector en todo `k`) que nadie ha formulado sin equivaler a `[P,J]=0`. Condición de concesión: un enunciado cuya hipótesis no sea minimalidad ni la conmutación de saturación.

**D.** [SOURCE] El emparejamiento origen/`r_in` ya es aplicación condicional de P17 más el certificado. [INFERENCE] El residuo —transferir el cuerpo estricto por equivalencias— es higiene de contrato, no emergencia de `c`. OPUS reduce D a corolario de C si el sector agota `C^2`; esa reducción hereda el hueco (ii) que ASTRA acaba de agrandar. Un FAIL (`s=2` admisible con `0<c_0<c_strict^iso`) sería decisivo; incluir Eq. (2) lo hace improbable, y excluirla cambia de clase hacia una búsqueda, vedada por la restricción 5. Condición de concesión: rebajar el objetivo a certificar la clase mínima publicada.

## Ronda 2 — ABNER

Concedo a ASTRA y a CIRO la objeción a mi descomposición `D_sop/D_esp`. [INFERENCE] Tal como la formulé, es contabilidad algebraica, no identificación de dos canales. Si C se cerrara en esa resta, sería trivial. [ORIGINAL] La versión de C que mantengo exige dos lemas separables: (i) una completitud local de generadores sobre `N_3` cuyo término complementario esté caracterizado independientemente —en la familia `A_{a,θ}`, la métrica cuántica intersectorial, no definida como `c_strict^2 - c_0^2`—; (ii) un lema de supervivencia de vértices que fije el total contra `c_strict^2`. [SOURCE] La revisión independiente ya separa ambos pasos y declara que la descomposición en proyectores no iguala por sí sola al cuerpo estricto.

**A.** [INFERENCE] Sigo sin aceptar A como gate final. En la familia `s=4`, `c_strict^iso = r_in`; por tanto la cota A se reduce a `c_0 ≤ r_in`. Esa cota se obtiene ya de `P J_x P`, sin Bernstein. A no añade control precisamente en el caso que obligó a replantear el problema. Su contenido quedaría confinado a clases con `D_sop > 0`, no realizadas en este acta. Un PASS de A como gate de emergencia sería trivial en ese sentido relativo: probaría un techo que ya es visible en el ejemplo central, sin explicar su desaturación. [INFERENCE] El fracaso rápido que lo mataría no es un cono superlumínico, sino una prueba que cubra ramas regulares del símbolo completo y deje fuera cúmulos Floquet degenerados. Condición de concesión: una prueba que cubra la compresión `PJP` de cúmulos degenerados y muestre por qué la cota es la ley relevante tras `s=4`. No está.

**B.** [INFERENCE] Añado una objeción estructural a las ya formuladas. Si la condición de saturación es `[P,J_n̂]=0`, esa hipótesis fuerza `c_0 = r_in`, no `c_0 = c_strict^iso`, salvo que además se certifique `c_strict^iso = r_in`. [SOURCE] El acta admite vértices nilpotentes y tiene abierta la saturación general del cuerpo estricto. [INFERENCE] En una clase con `c_strict^iso < r_in`, un sector que cumpla `[P,J]=0` daría `c_0 > c_strict^iso`, es decir, no restauraría `B_∞^*`. Por tanto B, tal como se ha esbozado, sigue apuntando al inradio del cuerpo de un paso, no al límite asintótico propio. Condición de concesión: una hipótesis que implique saturación contra `c_strict^iso` sin pasar por `r_in`; no ha aparecido.

**D.** [INFERENCE] Un PASS seguiría siendo higiene de equivalencias sobre la clase publicada, no la ley buscada. Un FAIL requeriría un `s=2` admisible con desaturación estricta; incluyendo la Eq. (2) de P17 eso es poco probable, y excluyéndola se reabre una búsqueda amplia. No toca la diferencia `s=2`/`s=4`.

Contra GEMINI sobre C. [SOURCE] En la familia `s=4`, el cuerpo estricto se fija por `tr A_h ≠ 0` en los ocho vértices más el lema de convexidad, no por un operador local en `k=0`. [INFERENCE] La objeción “ningún operador local en el nodo codifica el soporte iterado” es correcta para `J(k=0)` y mata la versión de C como identidad de un solo paso; no alcanza a la versión corregida, que incorpora el lema de supervivencia de vértices como parte no local del gate. Condición de concesión: dos símbolos con idénticos datos de un paso y de vértice pero distinto `c_strict` refutarían el lema (ii); no se ha exhibido ninguno. [INFERENCE] Por eso mantengo C como marco, con A como lema interno pendiente, y con B/D no prioritarios.

## Ronda 2 — GEMINI

Concedo a ASTRA y CIRO mi propio ascenso injustificado del turno anterior. [INFERENCE] Afirmar que ningún operador local en el nodo puede codificar el soporte asintótico requiere exhibir dos símbolos admisibles con idénticos datos locales pero distinto $c_{strict}^{iso}$, lo cual no aporté. Concedo también a ASTRA su objeción geométrica: [INFERENCE] la nilpotencia de un vértice no fuerza obligatoriamente $c_{strict}^{iso} < r_{in}$, pues el mínimo del radio isotrópico en el cubo se mide en las normales a las caras, no en las diagonales extremas, y podría sostenerse mediante palabras formadas por otros desplazamientos.

Ataco la propuesta de ABNER para salvar el candidato C. [RECONSTRUCTION] ABNER propone acoplar una relación local de un paso ($c_0^2 + Q_{int} = r_{in}^2$) con un lema de supervivencia de vértices que certifique $r_{in} = c_{strict}^{iso}$, logrando así la igualdad contra el cuerpo asintótico. [INFERENCE] Esto no es una ley física unificada sobre el presupuesto causal, sino una yuxtaposición ad-hoc de una cota de un paso y un caso especial de saturación geométrica. Si aplicamos esta versión de C a un símbolo hipotético donde la supervivencia de vértices falle de forma que $c_{strict}^{iso} < r_{in}$, la relación puramente local seguiría sumando $r_{in}^2$. El supuesto "presupuesto" ignoraría el verdadero límite asintótico y quedaría anclado al inradio geométrico. Por tanto, C no establece una vinculación obligatoria entre el sector de baja energía y el límite de la dinámica iterada.
**Condición de concesión para este ataque:** exhibir una formulación del candidato C donde el término de mezcla $Q_{int}$ compense mecánicamente la caída del soporte asintótico estricto (lo que ABNER llama $D_{sop}$) sin requerir que esta sea cero.

Suscribo la objeción de CIRO contra el esquema axial de CLAUDE OPUS sobre C. [ABSENCE] Busqué en el acta la demostración de que $J_x^2 = I/3$ es una identidad general forzada para todo símbolo admisible de soporte $N_3$. No existe tal demostración. [SOURCE] La sección 8 de `S4_STRICT_CONE_COUNTEREXAMPLE.md` declara explícitamente que la identidad métrica está establecida "para esta familia solamente" y prohíbe promocionarla a teorema de QCA general sin prueba.
**Condición de concesión:** aportar el cálculo algebraico que demuestre que las identidades de unitariedad y localidad sobre los 8 modos BCC fuerzan inexorablemente $J_x^2 = I/3$ en $k=0$ para cualquier dimensión interna $s$, sin invocar la estructura específica de involuciones del ansatz.

Ataco a CIRO y ABNER por descartar el candidato A calificándolo de "físicamente inerte" o "trivial". [INFERENCE] Su rechazo asume que, dado que el límite $c_0 \le r_{in}$ ya se obtiene por la compresión local del generador $P J P$, A no aporta control nuevo en clases donde $c_{strict}^{iso} = r_{in}$ (como el contraejemplo actual). Esto es atacar una versión débil. La versión más fuerte de A —y la base del proyecto— pregunta si un cono relativista puede escapar del cono causal asintótico *cuando este último se contrae*. Si un símbolo admisible exhibe $c_{strict}^{iso} \ll r_{in}$, la cota local de un paso no impedirá en absoluto que $c_0 > c_{strict}^{iso}$, configurando una violación flagrante de la causalidad emergente frente al sustrato estricto. Renunciar a A es renunciar a probar que esto es imposible.
**Condición de concesión:** aportar la demostración rigurosa de que $c_0 \le c_{strict}^{iso}$ ya es un teorema cerrado que cubre el Hamiltoniano efectivo de cúmulos de Floquet degenerados, no solo ramas regulares del símbolo global. Mientras ese teorema no obre en el acta, el gate A es el único paso que fundamenta el concepto de límite causal del sustrato.

## Ronda 2 — CLAUDE OPUS

Concedo a ASTRA el ascenso que me señaló. [INFERENCE] Mi frase «toda condición de saturación debe implicar `[P,J_n̂]=0`» sólo vale para la igualdad con `r_in`, no para `c_0=c_strict^iso`. Concedo a GEMINI su [ABSENCE]: el acta no contiene prueba de `J_x²=I/3`. Aporto las dos pruebas que se me exigen. Si se sostienen, cambian qué puede ser gate.

**Presupuesto axial, para todo `s`.** [INFERENCE] Tómese un símbolo con soporte exactamente `N_3` y sin coeficiente on-site. Fijada `k_⊥`, se escribe `A=e^{-iq}X_+(k_⊥)+e^{iq}X_-(k_⊥)`. `A^†A=I` para todo `q` da `X_+^†X_-=0` y `X_+^†X_++X_-^†X_-=I`. `AA^†=I` da `X_+X_-^†=0`. Entonces `Π_±=X_±^†X_±` cumple `Π_+Π_-=X_+^†(X_+X_-^†)X_-=0`, y por tanto son proyectores complementarios. Los términos cruzados se anulan, luego `J_x=iA^†∂_xA=(Π_+−Π_-)/√3` y `J_x²=I/3` en **todo** `k`, no sólo en el nodo. No se usa ninguna involución del ansatz. **Condición de concesión:** un error en estas cuatro líneas, o que la clase admita on-site. Esto último la restricción de soporte lo excluye.

**El término de mezcla, caracterizado sin velocidades.** [INFERENCE] Sea `P` un cúmulo aislado de rango `r` a cuasienergía `ε`, y `P_μ` los demás cúmulos. La perturbación de un unitario normal da `‖P_μJ_xP‖²=4sin²((ε−ε_μ)/2)‖P_μ(∂_xP)P‖²`. Con cono isótropo sin inclinación, `(PJ_xP)²=c_0²P`. Resulta:

`c_0² + (4/r)Σ_μ sin²(Δε_μ/2) g^{(μ)}_{xx} = 1/3`.

`g^{(μ)}` es la métrica cuántica parcial hacia el cúmulo `μ`. Con `r=2` y un solo cúmulo complementario se recupera exactamente la identidad de `A_{a,θ}`. Esto responde a ASTRA y a CIRO: el defecto no es un resto definido por las velocidades, sino una métrica ponderada por separaciones de cuasienergía. No es la cancelación de ABNER.

**Cota A, incluidos cúmulos degenerados.** [INFERENCE] La cadena tiene cuatro pasos.
1. Se restringe a la recta `t↦U(k_*+tn̂)`. Por Rellich, aplicado vía transformada de Cayley, las ramas propias y los proyectores son analíticos a través del nodo degenerado. Las pendientes en `t=0` son los autovalores de `PJ_n̂P`. [UNVERIFIED] Aplicabilidad de Rellich a familias unitarias analíticas en un parámetro real.
2. `U^n` tiene frecuencias `{n̂·x : x∈S_n}` y ramas con fase multiplicada por `n`.
3. Tras centrar, Bernstein para funciones de tipo exponencial, aplicado a cada elemento de matriz `⟨u,V(t)w⟩`, da `‖V'‖≤` semiancho. [UNVERIFIED] Bernstein clásico, recordado.
4. Hellmann–Feynman da `n·ω'≤H_n(n̂)`. Por Fekete, `n̂·v≤h_∞(n̂)`. Un cono isótropo tiene rama `+c_0` en toda dirección, luego `c_0≤c_strict^iso`.

Esto desactiva la condición de GEMINI y la de ABNER, siempre que 1–4 se sostengan. **Condición de concesión:** que en un cúmulo Floquet degenerado `c_0` no sea pendiente de ninguna rama analítica, o que Bernstein falle para frecuencias reales no enteras.

**Consecuencias, con ambos lemas.**

- **Contra GEMINI.** [INFERENCE] `c_0≤c_strict^iso≤r_in` y el presupuesto dan `mezcla ≥ r_in²−(c_strict^iso)²`. Es exactamente lo que pedía su condición de concesión: el término interno debe cubrir al menos toda caída del soporte asintótico, sin exigir que ésta sea cero. C deja entonces de estar anclado sólo al inradio.
- **Contra ASTRA, sobre D.** [INFERENCE] Si el nodo es escalar (`A(k_*)∝I`, cúmulo de rango `s`), entonces `Q=0` y `c_0=r_in`. Por A, `r_in=c_0≤c_strict^iso≤r_in`. Luego `c_0=c_strict^iso=r_in` para todo `s`, sin Eq. (2) de P17 y **sin certificado de vértices**. El puente con el cuerpo estricto que ASTRA juzgaba ausente lo proporciona A. D pasa a ser un corolario de pocas líneas, no un gate.
- **Contra CIRO.** [INFERENCE] Llamar a A «físicamente inerte» se sostiene sólo mientras A esté aislado. Combinado con el presupuesto, A es lo único que convierte la ley de defecto en una afirmación sobre el cuerpo iterado.
- **Contra ASTRA, sobre elegir A como gate.** [INFERENCE] Mi objeción de ronda 1 queda reforzada: si la prueba anterior resiste revisión, autorizar A como gate consume el turno científico en una verificación.

**Lo que queda débil, empezando por lo mío.**
- [INFERENCE] Todo lo anterior depende de que la dirección que minimiza `h_C` biparta `N_3` en dos planos soporte. Es un hecho del cubo, no de la localidad en general. Además, `min h_∞` no tiene por qué alcanzarse en normales de cara si `C_∞^strict` no es un cubo. Para la igualdad basta la cadena de desigualdades, pero la cota inferior sobre la mezcla usa `r_in` en la dirección `x`.
- [INFERENCE] La hipótesis «nodo escalar» es, a la vista, la frontera exacta entre Pavia y `s=4` (`A(0)=W` no escalar). Precisamente por eso corre el riesgo de ser post-hoc según la restricción 8. Su motivación independiente sería que no haya grados internos espectadores en la cuasienergía del nodo. Eso es minimalidad espectral, no minimalidad dimensional, y está por justificar. Además es suficiente y no necesaria: la condición necesaria y suficiente para `c_0=r_in` es `QJ_x P=0`.

**Condición de concesión global:** si alguno de los dos lemas cae, retiro las consecuencias y D y A recuperan su estatus de gate.

## Ronda 3 — CIRO

Concedo a CLAUDE OPUS el esbozo axial. [RECONSTRUCTION] Con soporte exacto `N_3` y sin on-site, a `k_⊥` fijo se tiene `A=e^{-iq}X_++e^{iq}X_-`; `A^†A=AA^†=I` para todo `q` fuerza `X_+^†X_-=0=X_+X_-^†`, luego `Π_±=X_±^†X_±` son proyectores complementarios, `J_x=(Π_+-Π_-)/√3` y `J_x^2=I/3` en todo `k`, sin involuciones del ansatz. Condición de concesión: on-site, o fallo de la anulación de cruzados.

Concedo que el defecto se caracteriza por métrica cuántica ponderada por `Δε`, no por la resta de ABNER. [SOURCE] En `A_{a,θ}` coincide. [INFERENCE] `(PJP)^2=c_0^2 P` y el prefactor `4/r` no están en el acta fuera de un Weyl de rango 2. Condición de concesión: esa identidad espectral para todo cúmulo admisible.

No concedo que eso cumpla la condición de GEMINI. [INFERENCE] `mezcla ≥ r_in^2-(c_strict^iso)^2` acota el resto pitagórico; no aísla un término que rastree `h_∞`. El total sigue siendo `r_in^2`. GEMINI pedía compensación mecánica de la caída asintótica dentro de la identidad.

No concedo A cerrado. [UNVERIFIED] Rellich para familias unitarias y Bernstein operadorial. [INFERENCE] Bernstein sobre elementos de matriz de `U^n(t)` acota por la semianchura de `{n̂·x:x∈S_n}`, no por la función de soporte desde el origen; en el cubo centrado coinciden en los ejes, no por definición de `c_strict^iso`. Condición de concesión: `|∇ω|≤H_n/n` para el cúmulo de Floquet degenerado. Sin eso, nodo escalar más presupuesto da `c_0=r_in`, que es `B*_0`, no el puente al cuerpo estricto que ASTRA exigía. D no es corolario.

La versión fuerte de A que defiende GEMINI no nombra la condición que distingue los dos especímenes certificados. [INFERENCE] Diseñar el único gate siguiente alrededor de un régimen con `C_∞` contraído, no realizado en el acta, invierte la prioridad evidencial. Condición de concesión: un símbolo certificado en la clase congelada con `c_strict^iso<r_in` y cono Weyl.

Diferencias invariantes entre Pavia `s=2`, que satura, y la familia `s=4`, que no:

Dimensión interna 2 frente a 4. [SOURCE] HECHO de especímenes. [INFERENCE] IRRELEVANTE como condición de saturación: si el presupuesto vale, cualquier `s` con sector de rango `s` da `c_0=r_in`.

Representación `R`. [SOURCE] `R_i=σ_i⊗I_2` es reducible; en Pavia la imagen de Pauli no lo es. HECHO. Como hipótesis extra, POST-HOC: en este D2 proyectivo colapsa a `s=2`, ya argumentado.

Dinámica irreducible. [SOURCE] Conmutante conjunto escalar en `s=4`; imagen de Pauli sin recta invariante en `s=2`. IRRELEVANTE: no distingue.

Número de sectores de cuasienergía. [SOURCE] Pavia: `A(0)` es fase global y un cúmulo de rango `2=s`. `s=4`: `A(0)=W` no escalar, dos cúmulos de rango 2 a `±θ`. HECHO. CANDIDATA: completez espectral del sector (rango `s`). [INFERENCE] Un Weyl de rango 2 en `s=2` agota la fibra por aritmética; en `s=4` no. Esa completez, no el entero `s`, cierra `Q=0`. Riesgo POST-HOC si se axiomatiza sólo para excluir el ejemplo.

Mezcla intersectorial. [SOURCE] `a^2+b^2=1` en `s=4`; `Q=0` en Pavia. HECHO como mecanismo. POST-HOC como hipótesis restauradora: «sin mezcla» es `QJP=0`, la igualdad.

Generadores. [INFERENCE] `J_x^2=I/3` sería común a ambos. Las `Γ_i` son del ansatz. IRRELEVANTE a nivel de clase.

Proyectores internos constantes. [SOURCE] `W` define proyectores de `τ_z` constantes que no reducen los ocho coeficientes. En `s=2` no hay escisión espectral de `A(0)`. CANDIDATA de vehículo del ansatz, no de clase.

`N_3`, D2, `C_∞^strict=C_micro` y supervivencia de vértices. [SOURCE] Comunes. IRRELEVANTE para la desaturación.

[INFERENCE] La diferencia invariante que no reformula la conclusión es si el sector Weyl agota el espacio interno en su cuasienergía. `s`, `R` irreducible y mezcla nula son equivalentes a eso o más débiles. Condición de concesión: un `s=2` con cono Weyl isótropo y `Q≠0`, o un sector de rango `s` con `0<c_0<c_strict^iso`.

## Ronda 3 — ABNER

Sin impugnar el lema axial de OPUS en sus condiciones. Concedo que, si la identidad espectral con prefactor `4/r` y métrica parcial se verifica, el defecto queda caracterizado por geometría cuántica ponderada por cuasienergía y no por resta algebraica; retiro condicionalmente mi objeción de cancelación.

No concedo A cerrado. [UNVERIFIED] Rellich y Bernstein no figuran en el acta. [INFERENCE] La cadena de OPUS necesita además simetría de `S_n` en la recta elegida: Bernstein acota por semianchura de frecuencias, que coincide con `H_n(n̂)` sólo si `min_{x∈S_n} n̂·x = -max_{x∈S_n} n̂·x`. En el cubo centrado es cierto para los ejes en los casos certificados, pero A pretende cubrir el régimen `c_strict<r_in`, donde `S_n` no está certificado simétrico. Condición de concesión: probar la simetría o sustituir Bernstein por una cota desde origen. Sin eso, D no es corolario.

Rechazo el paso “nodo escalar ⇒ Q=0”. [INFERENCE] `A(0)∝I` produce un único cúmulo de rango `s`, pero no obliga a que el sector Weyl agote ese cúmulo; puede ser un subespacio degenerado de rango 2 dentro de él. La anulación de Q requiere que `P` sea el cúmulo completo, no que no haya cúmulos separados. Condición de concesión: demostrar que un sector Weyl subpropio dentro de un cúmulo degenerado es inadmisible o no isotrópico.

Diferencias invariantes entre Pavia `s=2` y la familia `s=4`. Suscribo la lista de CIRO y corrijo tres entradas.

Dimensión interna: [SOURCE] HECHO de especímenes. [INFERENCE] No es irrelevante sin asumir el lema axial, porque `s=2` es lo que hace a `A(0)` escalar y al cúmulo completo. Como condición restauradora, CANDIDATA sólo en la forma “el sector Weyl agota su cúmulo”, no como entero dimensional.

Representación `R`: [SOURCE] HECHO: `R_i=σ_i⊗I_2` reducible en `s=4`; imagen de Pauli irreducible en `s=2`. POST-HOC si se propone como hipótesis restauradora.

Dinámica irreducible: [SOURCE] Conmutante conjunto escalar en ambos especímenes. IRRELEVANTE.

Número de cúmulos de cuasienergía: [SOURCE] HECHO: uno de rango 2 en Pavia; dos de rango 2 en `s=4`. CANDIDATA la completez espectral del cúmulo Wel, no el número de cúmulos.

A(0) escalar frente a no escalar: [SOURCE] HECHO. CANDIDATA sólo reformulada como “el sector Wel es todo el cúmulo”; la escalaridad sola no basta, según el rechazo anterior.

Mezcla intersectorial: [SOURCE] HECHO como mecanismo en `s=4`; POST-HOC si se erige en hipótesis restauradora.

Proyectores internos constantes: [SOURCE] HECHO en `s=4` vía `W`; [INFERENCE] ausentes en `s=2` por dimensionalidad. POST-HOC como restauradora.

Cuerpo estricto, `N_3`, D2, supervivencia de vértices: [SOURCE] HECHO comunes. IRRELEVANTE para la desaturación.

La única diferencia no post-hoc que sobrevive es que el sector Weyl agota su cúmulo de cuasienergía: en Pavia rango del sector = rango del cúmulo = `s`; en `s=4` rango del sector = 2 < 4 y convive con otro cúmulo separado. Condición de concesión: un `s=2` con sector propio, o un sector de rango completo que desature.

## Ronda 3 — GEMINI

La única diferencia estructural invariante con potencial causal explicativo, no tautológica ni puramente clasificatoria, es la completeza espectral del sector Weyl dentro de su cúmulo de cuasienergía.

La evaluación de las variables estructurales propuestas por CIRO y ABNER (dimensión, irreducibilidad, mezcla y proyectores) queda validada en su diagnóstico básico como contexto establecido. Los esquemas locales del presupuesto axial de CLAUDE OPUS y las cotas tipo Bernstein asumen simetrías no demostradas del soporte iterado y se procesan internamente como restricciones estándar sin alterar el aislamiento de las diferencias.

Diferencias invariables entre Pavia `s=2` y la familia irreducible `s=4`:

**1. Dimensión interna (2 frente a 4):**
[SOURCE] HECHO.
[INFERENCE] POST-HOC. Como imposición bruta, la minimalidad dimensional restringe el espacio de búsqueda pero carece de motivación física para explicar el acoplamiento asintótico.

**2. Reducibilidad de la representación de simetría (`R`):**
[SOURCE] HECHO. `R` es reducible en el espécimen `s=4` e irreducible en Pavia.
[INFERENCE] POST-HOC. En la clase D2 proyectiva de Pauli, imponer irreducibilidad colapsa matemáticamente a exigir `s=2`. No aporta un principio físico independiente de la dimensión.

**3. Irreducibilidad de la dinámica:**
[SOURCE] HECHO. Ambas dinámicas poseen un conmutante conjunto escalar.
[INFERENCE] IRRELEVANTE. Al ser compartida, no discrimina el mecanismo de desaturación.

**4. Mezcla intersectorial (`Q`):**
[SOURCE] HECHO. Existe en `s=4` y es nula en Pavia.
[INFERENCE] POST-HOC. Utilizar "ausencia de mezcla" como hipótesis restauradora es tautológico frente al objetivo de explicar la emergencia de `c`. Exigir `Q=0` fuerza algebraicamente la saturación local sin revelar por qué el sustrato asintótico lo demandaría.

**5. Existencia de proyectores internos constantes (`W`):**
[SOURCE] HECHO. Presentes en el ansatz `s=4`, ausentes en `s=2`.
[INFERENCE] POST-HOC. Son una particularidad de diseño del circuito de este contraejemplo específico, no un invariante topológico o causal fundamental de los autómatas.

**6. Completeza espectral del sector en el nodo (Número y rango de sectores de cuasienergía):**
[SOURCE] HECHO. En Pavia, el sector Weyl tiene rango 2 sobre un espacio total `s=2`, agotando su cuasienergía. En `s=4`, existen dos cúmulos aislados a `±θ`; el sector relativista evaluado es un subespacio de rango 2 dentro del espacio total.
[ORIGINAL] CANDIDATA. 

Se descartan las transiciones procedimentales relativas al puente métrico intersectorial para saltar directamente a la transformación final. [INFERENCE] La desaturación causal no emerge simplemente porque el autómata posea "más dimensiones" o representaciones reducibles, sino porque el cono relativista constituye un subespacio propio e incompleto del operador de evolución local en ese nodo. Cuando un sector agota por completo la multiplicidad de su cúmulo, la invariancia de la dinámica fuerza a sus generadores efectivos a saturar los extremos del politopo de un paso, anclando obligatoriamente la pendiente espectral al avance del soporte asintótico. Por el contrario, la incompletitud espectral permite que los grados de libertad latentes en el mismo nodo (o en nodos complementarios) operen como sumideros de norma, desconectando la velocidad de fase (el sector de baja energía) de la velocidad de propagación de la frontera estricta (el límite causal del sustrato iterado).

**Condición de concesión:** Exhibir un espécimen admisible donde el sector Weyl agote por completo su cúmulo de cuasienergía (rango del sector igual al rango del cúmulo, sin espectadores degenerados) y que, a pesar de esa completeza espectral, desature el límite asintótico con `0 < c_0 < c_{strict}^{iso}`. Mientras no exista tal contraejemplo, la completeza espectral es la única hipótesis independiente que conecta rígidamente la propagación relativista con el soporte geométrico del sustrato.

## Ronda 3 — CLAUDE OPUS

Concedo a ABNER un error de formulación. «Nodo escalar ⇒ `Q=0`» identificaba sector y cúmulo. [INFERENCE] Si `A(k_*)∝I`, el cúmulo es la fibra entera. La conclusión se mantiene por otra vía. En un autovalor degenerado, las pendientes de las ramas analíticas son los autovalores de la compresión de `J` al cúmulo completo, que aquí es el propio `J_x=(Π_+−Π_-)/√3`. Toda rama que sale del nodo, incluida la de un sector Weyl subpropio, tiene entonces pendiente axial `±1/√3`. Un cono isótropo exige esa pendiente en el eje, luego `c_0=1/√3`. **Condición de concesión:** que la teoría de perturbación degenerada para familias unitarias analíticas no dé esas pendientes. [UNVERIFIED] Esa teoría es la de Rellich, recordada y no leída.

Concedo a CIRO dos cosas. Primera: `(PJP)²=c_0²P` exige que el cúmulo esté formado sólo por ramas cónicas `±c_0`, sin bandas planas ni conos de otra pendiente. Es una hipótesis que hay que declarar y no un dato. La normalización `4/r` fuera de `r=2` es [INFERENCE] sin comprobar. Segunda: `mezcla ≥ r_in²−(c_strict^iso)²` es una desigualdad, no una compensación exacta que siga a `h_∞`. No retiro más.

Contra ABNER y CIRO sobre Bernstein, la objeción de semianchura no se sostiene. [INFERENCE] Sea `[α,β]` la envolvente de `{n̂·x : x∈S_n}` y `m=(α+β)/2`. Defino `V=e^{itm}U^n`. Bernstein da `‖V'‖≤(β−α)/2`, y `iV^†V'=iU^{n†}(U^n)'−m`. Los autovalores de la velocidad caen entonces en `[α,β]`, y la cota superior es `β=H_n(n̂)`, medida desde el origen. No hace falta simetría de `S_n`. **Condición de concesión:** que falle Bernstein para funciones con valores de Banach de tipo exponencial acotadas en la recta real. [UNVERIFIED] La reducción escalar por funcionales es clásica. Sigue siendo deuda de verificación, pero ya no es un hueco estructural.

GEMINI no argumenta su turno. Descarta mis dos lemas porque «asumen simetrías no demostradas» sin decir cuáles ni dar condición de concesión, lo que por la regla 3 no cuenta como ataque. Además, su paso central («la invariancia fuerza a los generadores efectivos a saturar los extremos del politopo, anclando la pendiente al soporte asintótico») es exactamente la cadena presupuesto + A que acaba de descartar, afirmada sin prueba.

Hay algo más grave. [INFERENCE] La candidata de GEMINI y ABNER, «el sector Weyl agota su cúmulo», **ya está refutada por el contraejemplo `s=4`**. [SOURCE] Allí cada cúmulo a `±θ` tiene rango dos y el sector Weyl es el cúmulo completo, sin espectadores degenerados, y aun así `0<c_0<c_strict^iso`. Es literalmente la condición de concesión que GEMINI declara. ABNER confunde «agota su cúmulo» con «agota la fibra».

Diferencias invariantes, frente a conjugación constante y fase global (no frente a multiplicación por una moneda no escalar, que [SOURCE] es dinámica nueva):

**Multiplicidad espectral de `U(k_*)`.** [SOURCE] En `s=4`, `A(0)=W` no es fase global; Pavia tiene un único cúmulo. HECHO. [INFERENCE] CANDIDATA, y la más débil de las suficientes: basta «un solo autovalor en el nodo». No es POST-HOC, porque [SOURCE] R17 impone `A(0)=I` en su Eq. (15) antes de conocer esta familia. [INFERENCE] Con `s=2` e `R` irreducible esa imposición era una normalización; con `s>2` es restrictiva. La motivación física a defender es un límite continuo en el que el paso tiende a la identidad en toda la fibra, sin gaps internos del orden de `1/Δt`. Con el lema axial y A, daría `c_0=c_strict^iso=r_in` para todo `s`, lo que es más que D. Es suficiente y no necesaria: la condición exacta es `QJ_n̂P=0`. **Condición de fallo:** un símbolo con nodo escalar y cono isótropo con `c_0<1/√3`, que sólo puede existir si cae el lema axial.

**Dimensión interna.** HECHO. [INFERENCE] Subsumida: con un cúmulo Weyl de rango dos, `s=2` implica nodo escalar. Es más fuerte que la anterior sin ganar nada.

**`R` reducible.** HECHO. [INFERENCE] Subsumida: en la clase proyectiva de Pauli equivale a `s=2`.

**Mezcla intersectorial.** HECHO como mecanismo, POST-HOC como hipótesis restauradora, porque reformula la igualdad.

**Proyectores `τ_z` constantes.** HECHO. [INFERENCE] IRRELEVANTE a nivel de clase: son el vehículo concreto de la multiplicidad del nodo en este ansatz.

**Rango del sector respecto de su cúmulo.** IRRELEVANTE, por el contraejemplo.

**Dinámica irreducible, `N_3`, D2 y supervivencia de vértices.** Comunes a ambos especímenes. IRRELEVANTES.

Límite propio que mantengo. [INFERENCE] Todo lo anterior usa la bipartición axial del cubo. Un gate construido sobre «nodo escalar» debe congelar `N_3` y declarar que su alcance es geométrico y no general.

## Ronda 3 — ASTRA

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
   A failed condition makes a candidate inadmissible, not a falsifier of
   B_infty^*. Stop its certification at the first failed condition and
   concesión explícita y bien delimitada es un turno válido.
  limits which classes the example speaks to; it does not affect the
## 4. Search coverage and limitations
```

## Ronda 4 — ABNER

[ORIGINAL] Propongo como único siguiente gate el GATE_A_N3: cota universal `c_0≤c_strict^iso`.

[SOURCE] El acta define `S_n`, `h_∞` y `c_strict^iso`, y registra que `c_strict^iso≤r_in` es la única desigualdad general ya establecida. [INFERENCE] Ni la identidad de presupuesto de OPUS ni la candidata nodo escalar tocan el cuerpo estricto sin una cota espectral universal; por eso este gate es el pago de esa deuda, no un lema auxiliar prescindible.

[ORIGINAL] Enunciado exacto: sea `U(k)=∑_{h∈N_3}e^{-ik·h}T_h` unitaria para todo `k`, con los ocho `T_h≠0` y sin término on-site; sea `P` un cúmulo espectral aislado en `k=0`, de rango finito `r≥2`, cuyo primer orden da un cono isótropo no inclinado con velocidad `c_0>0` en toda dirección. Entonces `c_0≤c_strict^iso`.

[ORIGINAL] Clase admisible congelada: `d=3`, `N_3={±1,±1,±1}/√3`, una actualización completa por unidad de tiempo, convenio `exp(-ik·h)`, nodo `k=0`. No congelo `s`, representación `R`, covariancia D2, irreducibilidad de la dinámica, escalaridad de `A(0)` ni rango del cúmulo. [INFERENCE] Congelar sólo soporte y unitariedad evita introducir una hipótesis que excluya el contraejemplo por diseño.

[ORIGINAL] PASS: prueba analítica exacta, sin búsqueda numérica, de la cota para todo símbolo admisible, con cobertura explícita de cúmulos degenerados y Floquet-desplazados. [INFERENCE] Una prueba que cubra sólo ramas regulares del símbolo completo no constituye PASS.

[ORIGINAL] FAIL: un único símbolo admisible, certificado exactamente como en el acta, con `0<c_strict^iso<c_0`. [INFERENCE] No exige que `C_∞^strict=C_micro`; el fallo más letal sería un símbolo con cuerpo estricto contraído que el cono local supere.

[ORIGINAL] Stop rule: primer FAIL certificado cierra el gate en contra y obliga a abandonar la línea de “límite del sustrato” como tesis defendible. Un PASS cierra el gate en favor y deja abierta la saturación como pregunta subsidiaria. [INFERENCE] Una demostración parcial o dependiente de supuestos no verificados produce INCONCLUSIVE, no un gate cerrado.

[ORIGINAL] Cálculo mínimo necesario: (i) verificación exacta de unitariedad de los coeficientes; (ii) teoría espectral para familias unitarias analíticas: las pendientes del cúmulo degenerado son los autovalores de `PJ_n̂P`, para todo `n̂`; (iii) cota de velocidad de `U^n` a partir de la envolvente de `{n̂·x:x∈S_n}`; (iv) Fekete para `h_∞`. [UNVERIFIED] Los pasos (ii) y (iii) no figuran como teoremas leídos en el acta; deben probarse, no asumirse. [SOURCE] El acta contiene la subaditividad de `H_n` y la definición de `h_∞`.

[INFERENCE] Por qué acerca al objetivo: si A es verdadera, el sustrato estricto queda restaurado como techo universal del sector Weyl; la afirmación fuerte defendible se convierte en `c_0≤c_strict^iso`, y la saturación pasa a ser una cuestión medible de cuándo se agota el presupuesto axial. Si A es falsa, no hay nada que salvar: el sector relativista puede escapar del soporte exacto iterado. [INFERENCE] Concedo a CIRO que A no explica por qué `s=4` desatura; no lo necesita: convierte la desaturación en acotada y es exactamente el suelo que la ley de defecto requiere antes de cualquier candidato B o C.

## Ronda 4 — GEMINI

Concedo explícitamente a CLAUDE OPUS dos puntos que destruyen mi posición anterior.
Primero: [SOURCE] En el contraejemplo `s=4`, el sector Weyl agota por completo su cúmulo de cuasienergía de rango 2, sin espectadores degenerados. [INFERENCE] Por tanto, mi candidata "el sector agota su cúmulo" es FALSA y ya está refutada. Condición de concesión cumplida. Retiro la candidata.
Segundo: [INFERENCE] Su derivación algebraica para `J_x^2 = I/3` es impecable. Al aislar las frecuencias espaciales en el eje `x` sobre el soporte `N_3` sin on-site, la unitariedad fuerza `X_+^\dagger X_- = 0`. Esto hace que `J_x` sea proporcional a una diferencia de proyectores complementarios. Es una verdad estructural, independiente del ansatz. Condición de concesión cumplida.

Ataco el GATE_A_N3 propuesto por ABNER. [INFERENCE] Un PASS en su cota de Bernstein probaría que el soporte asintótico es un techo (`c_0 \le c_{strict}^{iso}`), pero dejaría ciego el mecanismo físico de desaturación de `s=4`. A es una desigualdad matemática; no nos diría *por qué* cae la velocidad ni calcularía el déficit. **Condición de concesión:** que GATE A pueda reformularse como una igualdad exacta que compute la velocidad en función exclusiva del soporte asintótico, sin invocar operadores locales. Dado que Bernstein acota un supremo, esto es inviable. A es un lema necesario, pero el gate científico rector debe gobernar la partición exacta de la norma.

Suscribo los rechazos de CIRO y ABNER a B y D por ser soluciones post-hoc e higiene de equivalencias.

[INFERENCE] El hallazgo de OPUS cambia el paradigma: la física del cono Weyl local no reacciona al soporte iterado asintótico, sino exclusivamente a la geometría de un paso (`r_{in}`). La intuición viva del proyecto no es una saturación flotante, sino una **ley exacta de conservación** donde el sustrato provee un presupuesto máximo que la unitariedad reparte.

Propongo como único gate:

**NOMBRE:** GATE_C_PRESUPUESTO_EXACTO_N3

**ENUNCIADO EXACTO:** Para todo símbolo unitario admisible con soporte exacto `N_3` y sin término on-site, se cumple la identidad de generadores `J_x^2 = I/3`. En cualquier nodo escalar o degenerado donde emerja un cono isótropo de pendiente `c_0 > 0`, opera la ley exacta de presupuesto local `c_0^2 + Q_{int} = r_{in}^2 = 1/3`, siendo `Q_{int}` una norma intersectorial invariablemente positiva si existe mezcla.

**CLASE ADMISIBLE:** `d=3`, soporte `N_3`, sin coeficiente on-site, nodo `k=0` con un sector Weyl isótropo. 

**QUÉ SE CONGELA ANTES DE CALCULAR:** La geometría BCC y la ausencia de on-site. NO se congela la dimensión interna `s`, la representación `R`, ni el número de cúmulos (asegurando validez general).

**PASS:** Prueba analítica rigurosa, sin búsqueda numérica, que formalice la descomposición axial para todo `s`, demostrando que `c_0^2 + Q_{int} = 1/3` es universal en la clase, y caracterizando `Q_{int}` de forma independiente a las velocidades (usando la métrica cuántica ponderada).

**FAIL:** Un símbolo admisible en la clase congelada donde `c_0^2 + Q_{int} \neq 1/3`, o donde `X_+^\dagger X_- = 0` resulte incompatible con la unitariedad global.

**STOP RULE:** Un FAIL destruye la conjetura de conservación intersectorial y nos devuelve a A como única cota. Un PASS establece la ley fundamental de desaturación, confirmando que `c` está determinada de manera rígida por el inradio de un paso menos la compresibilidad interna.

**CÁLCULO MÍNIMO NECESARIO:**
1. Formalizar analíticamente el teorema `J_x^2 = I/3` desde las identidades de Fourier en `N_3`.
2. Aplicar teoría de perturbaciones degeneradas al bloque `P` del cono para aislar el espectro de `(P J_x P)^2` y el término complementario `P J_x Q J_x P`.
3. Vincular algebraicamente el término complementario con la métrica del proyector y la separación de cuasienergías.

**POR QUÉ ACERCA AL OBJETIVO:** Abandona la expectativa ingenua de igualdad incondicional por una **relación de completitud determinista**. Rescata al sustrato como fijador exacto del límite causal (`r_{in}`), explicando toda desaturación relativista como una redistribución geométrica interna exigida por los axiomas de la QCA, y confinando la relación espectral con `c_{strict}^{iso}` a un problema derivado de supervivencia de vértices.

## Ronda 4 — CLAUDE OPUS

Concedo a ABNER que A no puede darse por cerrada mientras sus pasos (ii) y (iii) sigan siendo [UNVERIFIED], y que cualquier gate que la use debe pagar esa deuda. A GEMINI le concedo la retirada de su candidata y nada más. [INFERENCE] No he sostenido que el cono «no reaccione» al soporte iterado: combinado con A, el presupuesto dice justo lo contrario.

**Contra ABNER.** Su paso (ii) tiene un hueco que el enunciado no contempla. [INFERENCE] Cúmulos distintos de `U` pueden fundirse en `U^n`. En `s=4` con `θ=π/4`, `e^{∓4iθ}=−1` coinciden para `n=4`, de modo que la perturbación degenerada de `U^n` no es la de `U`. El hueco se cierra sin coste. Una rama analítica `ψ(t)` de `U` es autovector de `U^n`, y por normalidad `⟨ψ,(U^n)'ψ⟩=(λ^n)'`. Basta aplicar Bernstein a `U^n` y Hellmann–Feynman a la rama de `U`. **Condición de concesión:** que en un nodo degenerado de una familia unitaria analítica no existan ramas analíticas ([UNVERIFIED], Kato–Rellich). La objeción de fondo es otra. [INFERENCE] GATE_A_N3 cumple el criterio 3 de la regla de decisión, pero sólo produce una cota. Un gate que contenga A como lema obligatorio hereda su falsabilidad y además puede dar una igualdad.

**Contra GEMINI.** [INFERENCE] Su FAIL «`X_+^†X_-=0` incompatible con unitariedad» no puede ocurrir, porque esa identidad se deriva de la unitariedad; no es un falsador. Su ley `c_0²+Q_int=1/3` es falsa tal como está escrita para cúmulos con bandas planas o conos de otra pendiente (concedido a CIRO en la ronda 3). Además, en el nodo escalar `Q_int=0` y la ley no dice nada. Sin A, su enunciado «`c` fijada por `r_in` menos compresibilidad» vuelve a `B*`, que es exactamente lo que GEMINI denunciaba en la ronda 1. **Condición de concesión:** hipótesis de cúmulo puramente cónico declarada, `4/r` probado y un puente a `c_strict^iso`.

**Propuesta: GATE_NODO_ESCALAR_N3.**

*Enunciado.* [ORIGINAL] Sea `U(k)=Σ_{h∈N_3}e^{-ik·h}T_h`, unitario para todo `k`, con `s` finito arbitrario, `T_h≠0` en los ocho vértices y sin coeficiente on-site. Supongamos `U(0)=e^{-iε}I` y que en `k=0` emerge un cono isótropo no inclinado de velocidad `c_0>0`. Entonces `c_0=c_strict^iso=r_in=1/√3`. En particular, `min h_∞=r_in` queda probado sin certificado de vértices.

*Clase.* `d=3`, `N_3`, una actualización por unidad de tiempo, fase `exp(-ik·h)`, nodo `k=0`. No se congelan `s`, `R`, la covariancia D2 ni la irreducibilidad.

*Qué se congela antes de calcular.* El enunciado y tres lemas:
- L1: `J_x²=I/3` en todo `k`.
- L2: las pendientes de las ramas analíticas en el nodo son los autovalores de `PJ_n̂P`.
- L3: `c_0≤c_strict^iso` para toda la clase, sin la hipótesis de nodo escalar.

Se congelan también la definición de cono (rama `±c_0` en toda dirección) y la motivación escrita de la hipótesis.

*PASS.* L1–L3 probados analíticamente. L2 y L3 deben demostrarse o citarse de una fuente leída, no recordada. [INFERENCE] Con nodo escalar, `P=I`, y en el eje `x` toda rama tiene pendiente `±1/√3`, luego `c_0=1/√3`. L3 cierra entonces la cadena `r_in=c_0≤c_strict^iso≤r_in`.

*FAIL.* Hay dos formas:
- un símbolo admisible con nodo escalar y cono isótropo con `c_0≠1/√3`, que refuta L1 o L2;
- un símbolo de la clase con `c_0>c_strict^iso`, que refuta L3 y con ello la tesis de techo.

*Stop rule.* El primer FAIL cierra el gate. Si cae L3, el sanedrín reabre con A falso. Si L2 sólo se prueba para ramas simples, el resultado es INCONCLUSIVE, sin extensión. No se autoriza búsqueda numérica ni familia nueva.

*Primera prueba (control negativo sin búsqueda).* En la familia ya certificada `A_{a,0}` (`θ=0`, nodo escalar), calcular exactamente el espectro de `k·Γ/√3` en los ejes y en `(1,1,1)/√3`. [INFERENCE] La predicción es que en los ejes las pendientes son `±1/√3`, porque los `Γ_i` son involuciones, y que el cono isótropo `a/√3` no sobrevive. [SOURCE] La revisión ya advierte que no hay límite uniforme a través de `θ=0`. Si sobreviviera un cono isótropo `a/√3`, L1 o L2 caen.

*Motivación y riesgo de la restricción 8.* [SOURCE] R17 impone `A(0)=I` en su Eq. (15), antes de conocerse esta familia. [INFERENCE] La lectura física es que un nodo no escalar deja grados internos del mismo `k` separados por una cuasienergía `O(1)` por paso, es decir, a escala de corte `1/Δt`. En `s=4` el sector Weyl está a `2θ/Δt` de su compañero. La hipótesis es entonces «sin gap interno a escala de corte en el nodo», no minimalidad dimensional. Admito dos límites:
- la hipótesis coincide con la frontera entre los dos especímenes; si el sanedrín juzga insuficiente esa motivación, el resultado debe rotularse como condición suficiente clasificatoria y no como explicación;
- [INFERENCE] el alcance se limita a la bipartición axial del cubo.

*Por qué acerca al objetivo.* [INFERENCE] Es el único candidato en la mesa que ofrece una igualdad `c_0=c_strict^iso` para todo `s` bajo una hipótesis espectral enunciable y ajena a la conclusión.
- Contiene A como lema falsable.
- Absorbe D como caso `s=2`, donde un cúmulo Weyl de rango 2 fuerza el nodo escalar.
- Sitúa la desaturación de `s=4` exactamente en el gap interno del nodo.
- Deja la ley de presupuesto de GEMINI como corolario cuantitativo fuera del nodo escalar, condicionado a cúmulos cónicos.

**Condición de concesión global:** si L2 o L3 no admiten prueba completa, retiro esta propuesta y apoyo GATE_A_N3 tal como lo formula ABNER.

## Ronda 4 — ASTRA

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
   A failed condition makes a candidate inadmissible, not a falsifier of
   B_infty^*. Stop its certification at the first failed condition and
   concesión explícita y bien delimitada es un turno válido.
  limits which classes the example speaks to; it does not affect the
## 4. Search coverage and limitations
```

> ASTRA queda fuera del resto de la sesión tras 2 fallos; no se interpreta su ausencia como acuerdo.

## Ronda 4 — CIRO

Concedo a CLAUDE OPUS el cierre del hueco de semianchura que marqué en la ronda 3: [INFERENCE] centrar `V=e^{itm}U^n` coloca las velocidades en `[α,β]` y la cota superior es `H_n(n̂)`. Queda [UNVERIFIED] Bernstein operadorial y Rellich. Concedo su respuesta a ABNER: [INFERENCE] si `U(0)` es escalar, el espectro de `J_x` es `±1/√3` y un Weyl subpropio no desatura al primer orden. Condición de concesión: que la perturbación degenerada de familias unitarias no dé esas pendientes. Suscribo la retirada de GEMINI de la completez del cúmulo.

Suscribo las tres objeciones de OPUS al GATE_C de GEMINI. Añado una: [INFERENCE] el stop rule que confina `c_strict^iso` a un «problema derivado de vértices» cambia de pregunta. La restricción 10 exige la relación con el límite iterado, no una identidad de un paso como fin. Eso rehabilita el `B*` que GEMINI denunció en la ronda 1.

Contra GATE_A_N3. [INFERENCE] El charter no declara cúmulo puramente cónico: `c_0` del cono isótropo y el radio espectral de `PJP` pueden disociarse, y un PASS que acote el segundo no acota el primero. Autorizar A como único gate responde sólo al techo de la pregunta del sanedrín y aplaza la ley precisa a un sucesor no charteado. El único turno autorizado no debe gastarse en el suelo de la afirmación fuerte.

Contra GATE_NODO_ESCALAR. [SOURCE] El audit registra que R17 impone `A(0)=I` tras Schur, como normalización del `s=2` irreducible. [INFERENCE] Trasladar esa normalización a principio físico para `s` arbitrario es un ascenso. La lectura de «gap interno a escala de corte» presupone un límite hamiltoniano continuo; en un sustrato discreto el nodo Floquet a `θ=π/4` es un sector de baja energía admisible. Congelar nodo escalar como hipótesis de clase viola la restricción 8: coincide con la frontera de los dos especímenes. Si L1–L3 valen, la igualdad en nodo escalar es un corolario, no una restricción.

[ORIGINAL] Único gate: GATE_COMPLETITUD_AXIAL_N3.

Enunciado. Sea `U(k)=∑_{h∈N_3}e^{-ik·h}T_h` unitario para todo `k`, con los ocho `T_h≠0` y sin on-site. Entonces: (1) `J_x^2=I/3` en todo `k`. (2) Si `P` es un cúmulo aislado en `k=0`, de rango `r`, formado únicamente por ramas de un cono isótropo no inclinado de velocidad `c_0>0`, entonces `c_0^2+Q_x(P)=1/3`, donde `Q_x(P):=(1/r)Tr[P J_x(I-P)J_x P]` coincide con la suma de métricas cuánticas parciales ponderadas por separaciones de cuasienergía, sin definir `Q` por velocidades. (3) En la misma clase y el mismo cúmulo, `c_0≤c_strict^iso`. Corolario, no hipótesis de clase: si `U(0)∝I`, entonces `Q_x=0` y `c_0=c_strict^iso=r_in=1/√3`.

Clase admisible. `d=3`, `N_3`, una actualización por unidad de tiempo, `exp(-ik·h)`, nodo `k=0`. No se congelan `s`, `R`, covariancia D2 ni irreducibilidad.

Qué se congela antes de calcular. El enunciado (1)–(3), la definición de cúmulo cónico, la de `Q`, y que el corolario no restringe la clase.

PASS. Prueba analítica de (1)–(3). El (2) exige la identidad métrica, no el resto pitagórico. El (3) cubre cúmulos degenerados y Floquet, incluidas fusiones en `U^n`, vía ramas analíticas de `U`.

FAIL. Cruzados no nulos o fallo de (1): cae la completitud. Cúmulo cónico con `c_0^2+Q_{\rm métrica}≠1/3`: cae (2). Un símbolo admisible con `0<c_strict^iso<c_0`: cae (3) y la tesis de techo.

Stop rule. El primer FAIL certificado cierra el gate. Si cae sólo (3), (1)–(2) no se promocionan como ley de `B_∞^*`. Si (2) sólo se prueba para `r=2` o un único complemento, el resultado es INCONCLUSIVE, sin extensión. Sin búsqueda numérica ni familia nueva.

Cálculo mínimo. Identidades de Fourier en `N_3` para (1); perturbación degenerada de unitarios para el espectro de `PJP` y el resto; identificación con la métrica ponderada; Bernstein centrado, Hellmann–Feynman y Fekete para (3). [UNVERIFIED] Rellich y Bernstein no figuran como teoremas leídos en el acta.

Por qué acerca al objetivo. Produce la afirmación fuerte como techo más defecto medido, cubre Pavia (`Q=0`) y `s=4` (`Q>0`) sin hipótesis que excluya el contraejemplo, y convierte la saturación en el caso `Q=0` del mismo teorema. A y el nodo escalar quedan como lema y corolario, no como gates autónomos.

Condición de concesión: si (3) no admite prueba completa, el gate se degrada a (1)–(2) y dejo de afirmar que habla de `B_∞^*`; si (2) no identifica `Q` con la métrica, retiro C y apoyo GATE_A_N3.

## Ronda 5 — GEMINI

Concedo a CLAUDE OPUS y CIRO que mi propuesta de la ronda 4 fracasa: al anclar la ley a $r_{in}^2$ sin exigir la prueba de $c_0 \le c_{strict}^{iso}$, mi gate recaía en el refutado $B^*$ y abandonaba el límite iterado. Concedo a CIRO que la propuesta de OPUS (GATE_NODO_ESCALAR) viola la restricción 8 al elevar a hipótesis de clase la frontera exacta que separa los especímenes conocidos (Pavia y $s=4$), lo cual es una maniobra post-hoc. Concedo a ABNER que la cota A es indispensable, pero suscribo el ataque de CIRO: un gate exclusivo para A prueba el techo pero ignora el defecto geométrico inter-sectorial que causa la desaturación en $s=4$.

La propuesta de CIRO (GATE_COMPLETITUD_AXIAL_N3) resuelve el debate integrando los tres requerimientos matemáticos sin hipótesis espurias. La adopto como veredicto.

SANEDRIN_NEXT_GATE_VERDICT

**Diagnóstico:** El contraejemplo $s=4$ demuestra que el límite asintótico estricto no esclaviza incondicionalmente la velocidad del sector Weyl; el cono puede ceder norma a canales intersectoriales si no agota su cúmulo de cuasienergía.
**Argumentos ganadores:** La intuición original se salva mediante una relación exacta de completitud de generadores más un lema universal de acotación asintótica. La métrica cuántica debe caracterizar el defecto independientemente de las velocidades.
**Argumentos perdedores:** Buscar condiciones puramente clasificatorias (como $s=2$ o representaciones irreducibles) es post-hoc; acotar sin explicar el defecto (sólo A) es insuficiente; igualar contra el inradio (C de un paso) abandona la pregunta asintótica.

**Decisión:** `AUTHORIZE_C`

**Charter exacto:** GATE_COMPLETITUD_AXIAL_N3
**Enunciado:** Sea $U(k)$ unitario para todo $k$, generado en $N_3$, con los 8 coeficientes no nulos y sin término on-site. (1) $J_x^2 = I/3$ en todo $k$. (2) Para todo cúmulo aislado $P$ en $k=0$ de rango $r$, formado exclusivamente por ramas de un cono isótropo de velocidad $c_0 > 0$, se cumple $c_0^2 + Q_x(P) = 1/3$, donde $Q_x(P) := (1/r)\text{Tr}[P J_x (I-P) J_x P]$ se identifica analíticamente con la suma de métricas cuánticas ponderadas por cuasienergía. (3) $c_0 \le c_{strict}^{iso}$ para dicho cúmulo. 
Corolario (no hipótesis): Si $U(0) \propto I$, entonces $Q_x = 0$ y $c_0 = c_{strict}^{iso} = 1/\sqrt{3}$.
**Clase admisible:** $d=3$, $N_3$, actualización completa, convención $\exp(-i k \cdot h)$, nodo $k=0$. No se congelan $s$, $R$, D2, irreducibilidad ni escalaridad.
**PASS:** Prueba analítica de (1), (2) y (3). (3) debe cubrir cúmulos degenerados Floquet vía ramas analíticas de $U$ y límite de Bernstein centrado. (2) debe probarse para $r$ arbitrario.
**FAIL:** Cruzados no nulos incompatibles con unitariedad; un cúmulo cónico donde $c_0^2 + Q_{\text{métrica}} \neq 1/3$; o un símbolo admisible con $0 < c_{strict}^{iso} < c_0$.
**Stop rule:** Un FAIL certificado cierra el gate y la línea de investigación. Si cae (3), el esquema asintótico fracasa. Si (2) sólo se logra para $r=2$, el resultado es INCONCLUSIVE.
**Primera prueba autorizada:** Formalizar las identidades algebraicas de Fourier para (1); derivar el espectro del generador y la métrica ponderada para (2); demostrar Rellich, Bernstein centrado y Fekete para (3).

**Respuestas explícitas:**

1. **¿Cuál es la versión más fuerte defendible?** El sustrato impone un límite asintótico absoluto ($c_0 \le c_{strict}^{iso}$) y una ley de conservación estricta de generadores ($c_0^2 + Q_x = 1/3$). El sector satura el límite salvo que exista mezcla inter-sectorial medible por la métrica cuántica.
2. **¿Qué tendría que demostrarse para recuperar la igualdad?** Que el sector Weyl constituye la totalidad de la fibra en su nodo (ej. nodo escalar $A(0) \propto I$). Esto anula obligatoriamente la mezcla ($Q_x=0$), forzando $c_0 = 1/\sqrt{3}$. Si además se certifica la supervivencia de vértices ($c_{strict}^{iso} = 1/\sqrt{3}$), la igualdad se recupera.
3. **¿Obstáculo principal en s=4?** La multiplicidad espectral en el nodo. El sector relativista no agota el espacio interno de su cúmulo, dejando grados de libertad que actúan como sumideros de norma ($Q_x > 0$) y deprimen la velocidad efectiva por debajo del frente balístico.
4. **¿Qué descubrimiento obligaría a abandonar la línea?** Un símbolo admisible certificado con $c_0 > c_{strict}^{iso}$ (violación supralumínica del cuerpo iterado) o la demostración de que los teoremas de Bernstein/Rellich no aplican a cúmulos Floquet degenerados.

## Ronda 5 — CLAUDE OPUS

Retiro GATE_NODO_ESCALAR como gate y concedo a CIRO lo que pedía. [INFERENCE] Convertir `U(0)∝I` en hipótesis de clase coincide con la frontera entre los dos especímenes. Como corolario de un teorema sin esa restricción, en cambio, no viola la restricción 8. Suscribo GATE_COMPLETITUD_AXIAL_N3 y la salida `AUTHORIZE_C`. [SOURCE] ASTRA falló dos turnos; su ausencia no cuenta como acuerdo, y su preferencia registrada era A. [INFERENCE] El charter de CIRO contiene A como punto (3) con FAIL propio, así que no la deja sin prueba.

Lo que sigue en pie es el texto de veredicto de GEMINI. Lo ataco sólo donde altera el charter o las respuestas obligatorias.

**Diagnóstico y respuesta 3.** GEMINI atribuye la desaturación a que el sector «no agota su cúmulo». Es la candidata que retiró en la ronda 4. [SOURCE] En `s=4` cada cúmulo a `±θ` tiene rango dos y es entero el sector Weyl. [INFERENCE] El obstáculo es la multiplicidad espectral de `U(k_*)`: hay más de un cúmulo en el nodo y `J_x` acopla entre ellos. **Condición de concesión:** un sector Weyl de rango menor que su cúmulo en `A_{a,π/4}`. No existe.

**Respuesta 2.** GEMINI añade «si además se certifica la supervivencia de vértices». Es un paso de más. [INFERENCE] Con (3) probado y nodo escalar, se tiene `r_in = c_0 ≤ c_strict^iso ≤ r_in`, y la igualdad sale sin certificado de vértices. Exigir la fibra entera es también excesivo: basta un único autovalor en el nodo. Hay que decir además lo que la versión de GEMINI oculta. La condición necesaria y suficiente de igualdad es `QJ_n̂P=0`, que reformula la conclusión. La suficiente independiente, nodo escalar, carece por ahora de motivación física aceptada. [INFERENCE] Por tanto el gate no entrega «debe saturar bajo condiciones físicamente justificables». Entrega techo, defecto medido y una condición suficiente de carácter clasificatorio. **Condición de concesión:** un principio independiente que implique `U(k_*)∝I`.

**Respuesta 1.** «Ley de conservación estricta» es un ascenso. [INFERENCE] (2) es una identidad en el nodo, restringida a cúmulos puramente cónicos, y sólo en el eje de la bipartición del cubo. La tesis defendible es más modesta. En `N_3` sin on-site, el sector Weyl no supera el cuerpo estricto, y su déficit respecto de `r_in` se mide por mezcla intercúmulo. «Frente balístico», en la respuesta 3, contradice el acta: [SOURCE] `c_strict^iso` es soporte exacto y no afirma nada balístico.

**Stop rule y respuesta 4.** «Un FAIL cierra la línea» mezcla niveles. [INFERENCE] Caer (1) o (2) mata la ley de defecto pero no el techo. Sólo un símbolo certificado con `c_0 > c_strict^iso` obliga a abandonar la línea. Que Rellich o Bernstein no se puedan verificar da INCONCLUSIVE, no refutación. Mantengo la redacción de CIRO: si cae (3), (1)–(2) no se promocionan como enunciado sobre `B_∞^*`.

**Enmiendas al charter.**

- (a) **Direcciones.** (3) se prueba para toda dirección `n̂` y no sólo para los ejes, ya que `min h_∞` puede no alcanzarse en normales de cara. [INFERENCE] El argumento Bernstein centrado no usa bipartición.
- (b) **Fusión de cúmulos.** (3) debe cubrir cúmulos que se funden en `U^n`, por ejemplo `e^{∓4iθ}=−1` en `n=4`. Se hace aplicando Hellmann–Feynman a ramas de `U` y Bernstein a `U^n`.
- (c) **Rango.** (2) se congela con `r` arbitrario y cúmulo cónico declarado. El prefactor métrico es [INFERENCE] sin comprobar fuera de `r=2`.
- (d) **Atribución.** [SOURCE] La completitud de involuciones `B_1²+B_2^†B_2=I` de AF16/17 es antecedente, y (1)–(2) deben atribuirse. NOVELTY sigue OPEN.
- (e) **Exclusiones.** No hay búsqueda numérica ni familia nueva. Rellich y Bernstein deben citarse desde una fuente leída o probarse; [UNVERIFIED] mientras tanto.

**Primera prueba autorizada, en orden.**

1. **L1.** Derivación exacta de `X_+^†X_-=0=X_+X_-^†` y `J_x²=I/3` a partir de las identidades de Fourier del charter del gate anterior, Sec. 3.
2. **Control positivo.** Evaluar (2) en `A_{a,π/4}`. Debe reproducir la identidad ya revisada: `r=2`, un complemento, total `1/3`. Si no la reproduce, se detiene.
3. **(3) con ramas analíticas.** Sólo después, y con los incisos (a) y (b).

**Condición de concesión global.** Si el paso 1 falla, retiro `AUTHORIZE_C` y apoyo GATE_A_N3 tal como lo formuló ABNER.

## Ronda 5 — CIRO

Concedo a CLAUDE OPUS las cuatro correcciones al texto de GEMINI. [SOURCE] En `s=4` cada cúmulo a `±θ` tiene rango dos y es el sector Weyl entero. [INFERENCE] El diagnóstico que atribuye la desaturación a un sector que «no agota su cúmulo» reintroduce la candidata que GEMINI retiró. El obstáculo es la multiplicidad espectral de `U(k_*)`: dos cúmulos y acoplamiento de `J` entre ellos. Concedo que exigir además supervivencia de vértices para recuperar la igualdad es un paso de más: con (3) y un único autovalor en el nodo, `r_in=c_0≤c_strict^iso≤r_in`. Concedo que «ley de conservación estricta» asciende: (2) es identidad nodal, en cúmulos puramente cónicos y en la bipartición axial del cubo. [SOURCE] `c_strict^iso` es soporte exacto, no frente balístico. Concedo el stop rule de mi ronda 4: un FAIL de (1) o (2) mata la ley de defecto, no la línea; sólo `c_0>c_strict^iso` obliga a abandonarla; Rellich o Bernstein no verificados dan INCONCLUSIVE.

Suscribo las enmiendas (a)–(e) de OPUS al charter. Acepto el orden de la primera prueba. ASTRA no cuenta. [INFERENCE] El punto (3) conserva el FAIL de ABNER; no se gasta el techo. El nodo escalar queda como corolario, no como hipótesis de clase: la restricción 8 queda satisfecha.

SANEDRIN_NEXT_GATE_VERDICT

**Diagnóstico.** [SOURCE] El contraejemplo `s=4` refuta `B_∞^*` fuerte en su clase: `0<c_0(a)<c_strict^iso` con `C_∞^strict=C_micro`. Localidad, unitariedad, homogeneidad y D2 con cuerpo estricto lleno no fuerzan saturación. [INFERENCE] El sustrato sigue como techo de soporte exacto más un defecto interno medible; no como determinante incondicional de `c`.

**Ganadores.** Completitud axial de generadores en `N_3` más cota espectral al cuerpo iterado; defecto por métrica cuántica ponderada, no por resta de velocidades; nodo escalar como corolario.

**Perdedores.** B y D: post-hoc o higiene de equivalencias. A sola: techo sin el mecanismo que `s=4` exhibe. C anclado sólo a `r_in`: regreso a `B*`. Nodo escalar como hipótesis de clase: frontera de los especímenes.

**Decisión:** `AUTHORIZE_C`

**Charter: GATE_COMPLETITUD_AXIAL_N3**

*Enunciado.* Sea `U(k)=∑_{h∈N_3}e^{-ik·h}T_h` unitario para todo `k`, ocho `T_h≠0`, sin on-site. (1) `J_x^2=I/3` en todo `k`. (2) Si `P` es un cúmulo aislado en `k=0`, rango `r` arbitrario, formado sólo por ramas de un cono isótropo no inclinado de velocidad `c_0>0`, entonces `c_0^2+Q_x(P)=1/3`, con `Q_x(P):=(1/r)Tr[P J_x(I-P)J_x P]` identificado con la suma de métricas cuánticas parciales ponderadas por `Δε`, no definido por velocidades. (3) En la misma clase y el mismo cúmulo, `c_0≤c_strict^iso` para toda dirección `n̂`, cubriendo cúmulos degenerados, Floquet y fusiones en `U^n` (Hellmann–Feynman en ramas de `U`, Bernstein en `U^n`). Corolario, no hipótesis: si `U(0)∝I`, entonces `Q_x=0` y `c_0=c_strict^iso=r_in=1/√3`.

*Clase.* `d=3`, `N_3`, una actualización, `exp(-ik·h)`, nodo `k=0`. No se congelan `s`, `R`, D2, irreducibilidad ni escalaridad.

*Congelado antes de calcular.* (1)–(3), cúmulo cónico, definición de `Q`, el corolario no restringe la clase. [SOURCE] AF16/17 (`B_1^2+B_2^†B_2=I`) es antecedente; NOVELTY=OPEN. Sin búsqueda numérica ni familia nueva.

*PASS.* Prueba analítica de (1)–(3). (2) exige la identidad métrica para `r` arbitrario. (3) exige fuente leída o demostración de Rellich y Bernstein; [UNVERIFIED] mientras tanto.

*FAIL.* Cruzados no nulos o fallo de (1). Cúmulo cónico con `c_0^2+Q_métrica≠1/3`. Símbolo admisible con `0<c_strict^iso<c_0`.

*Stop rule.* Primer FAIL certificado cierra el gate. Si cae (3), (1)–(2) no se promocionan como enunciado sobre `B_∞^*`. Si (2) sólo se prueba para `r=2` o un complemento, INCONCLUSIVE, sin extensión. Caer (1) o (2) no abandona la tesis de techo.

*Primera prueba.* (i) Identidades de Fourier: `X_+^†X_-=0=X_+X_-^†` y `J_x^2=I/3`. Si (i) falla, el gate se degrada a GATE_A_N3. (ii) Control positivo: (2) en `A_{a,π/4}` debe reproducir la identidad revisada; si no, se detiene. (iii) (3) con ramas analíticas, todas las direcciones y fusiones.

**Respuestas.**

1. [INFERENCE] En `N_3` sin on-site, el sector Weyl no supera el cuerpo estricto, y su déficit respecto de `r_in` se mide por mezcla intercúmulo. No se ha derivado que deba saturar bajo hipótesis físicamente justificadas.

2. [INFERENCE] `QJ_n̂P=0` es necesaria y suficiente, y reformula la conclusión. Suficiente independiente: un único autovalor en el nodo. Con (3), eso da la igualdad sin certificado de vértices. Falta un principio que implique `U(k_*)∝I`.

3. [SOURCE] Multiplicidad espectral de `U(0)=W`: dos cúmulos de rango 2 a `±θ`, con `J` acoplándolos. No es incompletitud dentro del cúmulo.

4. [INFERENCE] Un símbolo certificado con `c_0>c_strict^iso`.

## Ronda 5 — ABNER

[ORIGINAL] Voto `AUTHORIZE_C`, con el charter `GATE_COMPLETITUD_AXIAL_N3` enmendado por CLAUDE OPUS y CIRO. No autorizo A como gate único.

[INFERENCE] Retiro la preferencia de mi ronda 4. `GATE_A_N3` sólo fija el techo; el contraejemplo `s=4` pide además el defecto medido, y [SOURCE] la restricción 10 exige mantener la relación con el límite iterado, no una acotación en el inradio de un paso. Como el punto (3) del charter de CIRO conserva mi enunciado y su FAIL, no se pierde: queda subsumido como lema falsable dentro de C. Concedo también a CLAUDE OPUS: el nodo escalar no puede ser hipótesis de clase, pero es corolario legítimo y no viola la restricción 8.

[INFERENCE] Lo único sustantivo que sigue en pie es el texto de GEMINI, no ese charter. [SOURCE] El acta certifica que en `A_{a,θ}` cada cúmulo a `±θ` tiene rango dos y es el sector Weyl completo. [INFERENCE] Por tanto, es falso que el obstáculo sea que el sector “no agota su cúmulo”. La desaturación procede de la multiplicidad espectral de `U(0)=W`: dos cúmulos separados y `J_x` los acopla. Retiro mi formulación de ronda 3 sobre completez dentro del cúmulo; era incompatible con el acta.

[INFERENCE] Condición al charter: Rellich y Bernstein no figuran como teoremas leídos. [UNVERIFIED] La cadena espectral que sostiene (3) debe probarse o citarse de fuente leída. Si no se logra, el resultado es INCONCLUSIVE, no FAIL. Si (1) falla, la autorización se degrada a `GATE_A_N3` sin nuevo sanedrín, como prevé la primera prueba. Un PASS no puede dar por verificada esa cadena sin fuente o demonstración completa.

1. [INFERENCE] En `N_3` sin on-site, el sector Weyl no supera el cuerpo estricto y su déficit respecto de `r_in` se mide por mezcla intercúmulo; no se ha derivado que deba saturar.
2. [INFERENCE] `QJ_n̂P=0` es necesaria y suficiente; un único autovalor en el nodo da la igualdad vía (3). Falta un principio independiente que implique `U(k*)∝I`.
3. [SOURCE] Multiplicidad espectral de `U(0)=W`: dos cúmulos de rango dos a `±θ` acoplados por `J`.
4. [INFERENCE] Un símbolo certificado con `c_0>c_strict^iso`.

## Ronda Residuo — CLAUDE OPUS

Queda en pie `AUTHORIZE_C` con GATE_COMPLETITUD_AXIAL_N3 y las enmiendas (a)–(e). [SOURCE] Cuatro miembros lo suscriben. ASTRA falló y su preferencia registrada era A, así que no hay unanimidad. [INFERENCE] El nodo escalar entra como corolario y no como hipótesis de clase.

Se abandonan cuatro cosas:
- B y D como gates.
- La candidata «el sector no agota su cúmulo».
- «Ley de conservación» y «frente balístico».
- El stop rule de GEMINI que cierra la línea por no poder verificar Rellich o Bernstein. Eso da INCONCLUSIVE, no refutación.

Discrepo del residuo de CIRO y ABNER en la respuesta 1. Presentan «el sector Weyl no supera el cuerpo estricto» como tesis defendible, pero es exactamente el punto (3) todavía sin probar. [INFERENCE] Hoy lo defendible es sólo esto: el contraejemplo s=4 refuta la igualdad, y la cota `c_0≤c_strict^iso` es una conjetura con un esbozo que se apoya en teoremas [UNVERIFIED].

Nada de lo siguiente está justificado todavía:
- L1 (`J_x²=I/3` para todo `s`). Es inferencia mía y ningún texto la ha verificado.
- El prefactor métrico para `r>2`.
- Que la multiplicidad espectral en el nodo sea el único mecanismo de desaturación.
- Cualquier motivación física de `U(k_*)∝I`. Sin ella, la igualdad recuperada es clasificatoria y no explica `c`.

## Ronda Residuo — CIRO

Queda en pie `AUTHORIZE_C` con GATE_COMPLETITUD_AXIAL_N3 y las enmiendas (a)–(e). [SOURCE] Lo suscriben cuatro miembros; ASTRA no cuenta. El nodo escalar entra como corolario. Si (1) falla, degradación a GATE_A_N3. Sólo un símbolo con `c_0>c_strict^iso` cierra la línea.

Se abandona B, D, A como gate único, la candidata de completez del cúmulo, «conservación» y «frente balístico», y el stop rule de GEMINI que trata INCONCLUSIVE como refutación.

Concedo a OPUS la objeción a mi respuesta 1. [INFERENCE] Presenté el techo como tesis defendible; es el punto (3), aún [UNVERIFIED] en Rellich y Bernstein. [SOURCE] Lo que está en pie es el rechazo de `B_∞^*` fuerte en s=4 y `c_strict^iso≤r_in`. El techo es conjetura del charter, no resultado.

No justificado: L1 para todo `s`; la identidad métrica fuera de `r=2`; que la multiplicidad espectral sea el único mecanismo; un principio que implique `U(0)∝I`.

Discrepo de OPUS en el peso de L1. [INFERENCE] No justificado no reabre A ahora. L1 es el primer cálculo autorizado; su fallo ya tiene ruta de degradación. Tratarlo como vacío previo invertiría el orden del charter.

## Ronda Residuo — ABNER

[INFERENCE] Suscribo el residuo de CLAUDE OPUS, incluida la corrección a mi respuesta 1: presentar `c_0≤c_strict^iso` como defendible era ascender el punto (3), aún [UNVERIFIED] en Rellich y Bernstein. [SOURCE] Queda en pie `AUTHORIZE_C` con `GATE_COMPLETITUD_AXIAL_N3` y enmiendas (a)–(e); el nodo escalar queda como corolario, no como hipótesis. [INFERENCE] Abandono B, D, A único, la candidata de completez del cúmulo, «conservación» y «frente balístico»; Rellich/Bernstein no verificados dan INCONCLUSIVE, no cierre de línea.

No justificado todavía: L1 para todo `s`; la identidad métrica fuera de `r=2`; que la multiplicidad espectral sea el único mecanismo; y un principio independiente que implique `U(0)∝I`. [INFERENCE] Discrepo del matiz de CIRO: que L1 no esté justificado no reabre A, pero tampoco puede presentarse como verdad de la clase antes de su prueba. El orden del charter es correcto: si L1 falla, degradación a GATE_A_N3.

## Ronda Residuo — GEMINI

Suscribo el residuo de CLAUDE OPUS, CIRO y ABNER.

**Queda en pie:** `AUTHORIZE_C` con GATE_COMPLETITUD_AXIAL_N3 y sus enmiendas (a)–(e). El nodo escalar entra exclusivamente como corolario. La ruta de degradación a GATE_A_N3 está activa si falla el primer cálculo.

**Debe abandonarse:** Las direcciones B y D, el gate A como paso único, y mi hipótesis previa sobre la completez espectral del cúmulo. [SOURCE] Se abandona la retórica de "frente balístico" o "conservación estricta". Retiro mi stop rule: la incapacidad técnica de verificar los teoremas clásicos produce INCONCLUSIVE, no la refutación de la línea.

**NO está justificado todavía:**
1. La desigualdad $c_0 \le c_{strict}^{iso}$. [INFERENCE] Asumirla como hecho ya defendible era un error; depende de probar (3), sustentado en [UNVERIFIED] Rellich y Bernstein.
2. La identidad $J_x^2 = I/3$ para todo $s$ (L1 exige demostración formal).
3. La fórmula del prefactor métrico para $r>2$.
4. Que la multiplicidad espectral sea la *única* causa posible de desaturación.
5. Un principio físico independiente que obligue a $U(0) \propto I$.

No discrepo del residuo consolidado: el techo asintótico es el objetivo mismo a demostrar, no un resultado adquirido.

## Ronda Veredicto — CLAUDE OPUS

**1. ACUERDO**

[SOURCE] Los cuatro miembros activos suscriben `AUTHORIZE_C` con GATE_COMPLETITUD_AXIAL_N3 y las enmiendas (a)–(e). ASTRA quedó fuera tras dos turnos fallidos. Su preferencia registrada era A y su silencio no se computa como adhesión, de modo que el acuerdo es de cuatro y no unánime.

Dentro de ese perímetro hay acuerdo en los siguientes puntos, todos [SOURCE]:

- El contraejemplo `s=4` refuta la forma fuerte de `B_∞^*` en su clase: falla (i) con (ii) intacto. La desigualdad `c_strict^iso ≤ r_in` es la única general establecida.
- B y D no son gates. "R irreducible" en la clase proyectiva de Pauli no aporta una hipótesis independiente de `s=2`.
- El nodo escalar entra como corolario, no como hipótesis de clase.
- El obstáculo en `s=4` es la multiplicidad espectral de `U(0)=W`, con dos cúmulos acoplados por `J`. No es la incompletitud del sector dentro de su cúmulo.
- La cota `c_0 ≤ c_strict^iso` es conjetura, no resultado.
- Si Rellich o Bernstein no pueden verificarse, el resultado es INCONCLUSIVE, no FAIL.
- Si falla L1, el gate se degrada a GATE_A_N3.
- Sólo un símbolo certificado con `c_0 > c_strict^iso` obliga a abandonar la línea.

[SOURCE] También hay acuerdo en que el gate no entrega "debe saturar bajo condiciones físicamente justificables". Entrega, si pasa, un techo, un defecto medido y una condición suficiente de carácter clasificatorio.

**2. DESACUERDO VIVO**

[SOURCE] Queda sin resolver la objeción de ASTRA de que C sólo toca el cuerpo estricto a través de una cota aún no probada, lo que la llevaba a preferir A. [INFERENCE] El punto (3) del charter incorpora A con su FAIL, pero nadie puede afirmar que eso satisfaga a ASTRA.

[SOURCE] Hay una discrepancia menor sobre el estatus previo de L1. CIRO sostiene que su falta de prueba no afecta al orden del charter. OPUS y ABNER sostienen que no puede presentarse como propiedad de la clase antes de probarse. [INFERENCE] Es una discrepancia sobre la redacción de los informes, no sobre el orden de cálculo.

[SOURCE] Queda abierta la objeción de ASTRA de que un vértice nilpotente no implica `c_strict^iso < r_in`. CIRO y GEMINI la concedieron. [INFERENCE] El texto del charter anterior (Sec. 0(ii), INADMISSIBLE_SATURATION) sigue formulándolo categóricamente y nadie ha propuesto enmendarlo.

**3. ABANDONADO**

De mi propia posición se registran estas pérdidas, todas [SOURCE]:

- "Toda condición de saturación implica `[P,J_n̂]=0`" vale sólo para la igualdad con `r_in`, como me señaló ASTRA.
- "Nodo escalar ⇒ `Q=0`" confundía sector y cúmulo, como me señaló ABNER. Lo reformulé vía el espectro de la compresión al cúmulo completo, que sigue [UNVERIFIED].
- GATE_NODO_ESCALAR como hipótesis de clase cae por la restricción 8, como me señaló CIRO.
- La afirmación de que D es "corolario de pocas líneas" no se sostiene sin (3).
- La afirmación de que A es "lema de pocas líneas" tampoco se sostiene: A no está cerrada.

Del resto de miembros, también [SOURCE]:

- La descomposición `D_sop/D_esp` de ABNER, por ser cancelación algebraica.
- "Ningún operador local codifica el soporte iterado" de GEMINI, por ascenso sin testigo.
- La candidata "el sector agota su cúmulo", refutada por el propio `s=4`.
- La objeción de semianchura contra Bernstein, cerrada mediante centrado.
- El GATE_C de GEMINI anclado sólo a `r_in`, incluido su FAIL imposible sobre `X_+^†X_-`.
- A como gate único.
- "Ley de conservación estricta" y "frente balístico".
- El stop rule de GEMINI que cerraba la línea por no poder verificar teoremas.
- La presentación del techo como tesis ya defendible en las respuestas 1 de CIRO y ABNER, retirada por ambos.

**4. PENDIENTE**

(i) Una demostración escrita y revisada de L1: `X_+^†X_- = 0 = X_+X_-^†` y `J_x² = I/3` para todo `s`, a partir de las identidades de Fourier de la Sec. 3 del charter previo. [INFERENCE] Hoy sólo existe mi esbozo.

(ii) El control positivo de (2) sobre `A_{a,π/4}`, que debe reproducir la identidad ya revisada.

(iii) Una fuente leída o una prueba completa de estos tres elementos:
- perturbación degenerada analítica para familias unitarias en un parámetro real, con las pendientes dadas por los autovalores de `PJ_n̂P`;
- la desigualdad de Bernstein para funciones con valores operadoriales de tipo exponencial con frecuencias reales;
- el tratamiento de cúmulos que se funden en `U^n`.

Hoy los tres son [UNVERIFIED].

(iv) La identidad métrica con prefactor para `r > 2` y varios complementos, bajo la hipótesis declarada de cúmulo puramente cónico. [INFERENCE] Sólo está comprobada para `r=2` y un complemento.

(v) La prueba de (3) en toda dirección `n̂`, no sólo en los ejes.

(vi) Un análisis que decida si la nilpotencia de un vértice baja `min h_∞`.

(vii) Un argumento de que la multiplicidad espectral en el nodo es el único mecanismo de desaturación, o un testigo de que no lo es.

(viii) Un principio con motivación independiente que implique `U(k_*) ∝ I`. [INFERENCE] Sin él, la igualdad recuperada clasifica pero no explica `c`.

(ix) La comparación de equivalencia con la especialización homogénea de AF16/17, necesaria para atribuir (1)–(2). [SOURCE] NOVELTY = OPEN.

(x) [INFERENCE] El alcance fuera de la bipartición axial del cubo no está tratado: todo el esquema depende de `N_3`.

## Resultado operativo

- Estado: `DEGRADED_NO_CONSENSUS`
- Turnos con fallo, cuota, ausencia o respuesta corta: 2
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.
```

### Contexto adjunto: state/CURRENT_STATE.md
```
# CURRENT_STATE

**Date:** 2026-09-15  
**Status:** STANDARD WEYL/DIRAC EXACT GATE: PASS; strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS (branch-local)

**Branch-local state.** This file is reconciled on
`research/b-infinity-post-s4-gate` only, so that it agrees with all evidence
merged on this branch. It is **not** a canonical promotion: `main` is
unchanged, and promotion requires a separate explicit decision.

**Repository:** `nacho09021973/qca-causal-cones`

**Evidence baseline:** `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.
Canonical promotion is recorded in
[`2026-09-14--standard-gate-promotion.md`](../reports/2026-09-14--standard-gate-promotion.md).
**No successor scientific gate is currently chartered** (Sec. 7).

**Correction (2026-09-14):** `B*` as a comparison against the one-step
inradius `r_in(C_micro)` is superseded by `B_infty^*`, a comparison against
the strict asymptotic isotropic speed `c_strict^iso`. See
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) and
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0. New baseline-specific certificate: for the
standard Pavia Weyl family in d=3, `C_infty^strict = C_micro` exactly, so
`c_strict^iso = r_in(C_micro) = 1/sqrt(3)`; see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
This baseline-specific certificate did not by itself close the gate; the
later s=4 counterexample completed it for the declared s=4 class.

**Integration (2026-09-15, branch-local):** an explicit irreducible `s=4`
family on the same `N_3`, with the same `D2` action, has
`C_infty^strict = C_micro` and `c_strict^iso = 1/sqrt(3)`, but
`c_0(a) = a/sqrt(3)` for every `0 < a < 1`. This is `COUNTEREXAMPLE_VERIFIED`
in the sense of the
[gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) Sec. 5 for the
declared `s=4` class (Sec. 4.1 below). It does not refute the standard Pavia
`s=2` certificate above. Evidence:
[analytic note](../theory/S4_STRICT_CONE_COUNTEREXAMPLE.md) and
[freeze record](../reports/2026-09-15--s4-strict-cone-counterexample-freeze.md)
(`1dae941`), [independent review](../reports/2026-09-15--s4-independent-review.md)
(`aeec462`), [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md)
(`f74018f`). **NOVELTY = OPEN.**

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.
- In the verified standard Dirac couplings they differ for every `0 < m < 1`.
  Name the extraction `c_H` or `c_{ω^2}`; do not use an unspecified finite-lattice
  `c_IR` as though those coefficients were interchangeable.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Canonical hypothesis status

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

### B_infty^* — strict asymptotic matching (supersedes B* / inradius matching)

Candidate:

`c_0 = c_strict^iso`, `c_strict^iso = min_{n̂} h_infty(n̂)`,

with `h_infty` the strict asymptotic support function of
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md) Sec. 6.
Interpretation: `c` would match the exact long-run isotropic propagation
speed of the same dynamics, not necessarily the inradius of the one-step
body `C_micro` — the two satisfy `c_strict^iso <= r_in(C_micro)` in general,
with equality only where separately certified (see the d=3 row below).

| Claim | Status and scope |
| --- | --- |
| A — IR universality | **OPEN** |
| B_max | **REJECTED** under isotropic containment in an anisotropic causal body, d >= 2 |
| B_full | **REJECTED / GEOMETRICALLY IMPOSSIBLE** for a nondegenerate isotropic ball equaling a finite lattice polytope, d >= 2 |
| Exact finite-mass B* | **REJECTED IN STANDARD DIRAC FAMILY**, for both specified extractions, every 0 < m < 1 (comparison against `r_in(C_micro)`, unaffected by the B_infty^* correction) |
| B*_0 (linear order, `c_0=r_in`) | **VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN** |
| B*_cont | **VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN** |
| B_infty^*, d=3 Pavia baseline (`C_infty^strict=C_micro`, full nonlinear order) | **CERTIFIED for the standard Weyl family `A+,B+,A-,B-`** (`s=2`): `c_0 = c_strict^iso = 1/sqrt(3)`; d=1,2 not checked; unaffected by the s=4 result |
| Strong B_infty^* (`c_0 = c_strict^iso` forced by locality, unitarity, homogeneity and D2 covariance at fixed `N_3`) | **REJECTED IN DECLARED s=4 CLASS** — explicit counterexample, Sec. 4.1; false for any class containing that family |
| B_infty^* in the published minimal `s=2` class (P17, including its Eq. (2)) | **NOT REFUTED by the s=4 result; rigidity OPEN as an in-repo claim.** Origin-node inradius matching there is a conditional application of P17's classification plus the standard certificate, not a new theorem. The strict-body certificate is recorded for `A+,B+,A-,B-`; its transfer across all of P17's equivalences is not separately checked |
| B_infty^* for `s=2` without P17 Eq. (2), or with an irreducible internal symmetry representation `R` for `s>2` | **OPEN** |
| Novelty of the s=4 family and its strict-support statement | **OPEN** — no equivalent found in eleven checked primary sources; not a novelty certificate |

The restricted statements are established for the declared cases below.
There is no general rigidity theorem, proof of A, or novelty claim.

### 4.1 Declared s=4 counterexample class

**Status: COUNTEREXAMPLE_VERIFIED for this class; independent review PASS;
NOVELTY = OPEN.**

| Item | Declaration |
| --- | --- |
| Geometry | d=3, `N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`, all eight modes active, no on-site coefficient, one complete update per time unit, phase `exp(-i k.h)` |
| Internal space | `s=4 = C^2_sigma (x) C^2_tau`; parameter `0<a<1`, `b=sqrt(1-a^2)` |
| Symbol | `A_a(k) = W exp(-i q_x Gamma_x) exp(-i q_y Gamma_y) exp(-i q_z Gamma_z)`, `q_i=k_i/sqrt(3)`, `W = I (x) exp(-i pi tau_z/4)` |
| Isotropy | D2 half-turns acting on `N_3`; `R_i = sigma_i (x) I_2` — two copies of the Pauli projective class, hence a **reducible** representation; full cubic symmetry not assumed |
| Irreducibility | Dynamics irreducible: scalar joint commutant of all eight Fourier coefficients |
| Gapless sector | `k=0`; two isolated rank-two clusters at quasienergies `+/-theta`, `theta=pi/4`; isotropic, untilted cones measured from each cluster's node |
| Result | `C_infty^strict = C_micro` exactly (all vertex traces nonzero, so no vertex coefficient is nilpotent); `c_strict^iso = 1/sqrt(3)`; `c_0(a) = a/sqrt(3)` |
| Coverage | One particular product ansatz, not a classification of four-component walks |

Scope limits, all retained:

- **Procedure.** The class table above was written at the freeze and review,
  after the construction, not before solving as charter Sec. 2 requires. This
  limits which classes the example speaks to; it does not affect the
  mathematical validity of the certified inequality.
- **Strict means exact support.** Vertex amplitudes may decay exponentially.
  No ballistic, essential or Lieb-Robinson front statement is made.
- **Floquet-shifted nodes.** `A(0) = W` is not a global phase.
- **Family identity only.** For `0<theta<pi/2`,
  `c_0^2 + 2 sin^2(Delta eps/2) g_ii(0) = 1/3`, where `Delta eps = 2 theta`
  and `g` is the projector quantum metric. It comes from the
  intra/inter-sector split `a^2 + b^2 = 1` of the involutions `Gamma_i`.
  Equating `1/3` with `(c_strict^iso)^2` additionally needs vertex survival,
  which is certified at `theta=pi/4`, or, for fixed `a`, on an open
  neighbourhood where all vertex traces remain nonzero. This is not a
  general QCA theorem.
- **Prior art.** Product-of-projector walks (MB18, BM25), four-component Weyl
  mixing (BB94), shifted Floquet Weyl nodes, adjustable continuum velocity,
  and involution block completion (AF16/17) are antecedents and must be
  attributed. Raynal's explicit s=4 Dirac family is excluded as an
  identification. The most useful open equivalence check is AF16/17's
  homogeneous paired-walk specialization.
- **Certificates.** `scripts/cert_Aa_s4_counterexample.py` and
  `scripts/review_Aa_s4_exact.py` both return PASS (SymPy 1.14.0, zero
  tolerance), and `scripts/verify_weyl_dirac_gate.py` still returns PASS
  (375 checks), on this branch.

## 5. Completed standard Weyl/Dirac exact gate

**Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**

Evidence is the committed
[contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
[analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
[verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
[permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
Source provenance and the published sign/dagger issues are recorded there.
The analytic proof establishes the open mass interval and continuum scaling;
the check count alone is not their justification or a formal proof certificate.

### Declared family and coordinates

The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
the minimal two-component blocks. The seven symbols are not seven independent
geometries: transposes/chiralities within a dimension share support, inradius
and linear speed. There are three dimension-specific geometries in this battery.

Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
complete update per time unit:

`N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,

`C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,

`r_in = 1/sqrt(d)`, `V_causal^max = 1`.

### Massless equality

For d=1,2,3 in this family, at the declared zero node,

`m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.

This is equality of the linear IR coefficient, not exact finite-momentum
relativistic dispersion or a theorem about every admissible symbol.

### Fixed nonzero lattice mass

For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
`0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
continuous from the identity near the massless zero node. Then

`cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,

`F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.

Exact finite-mass B* is refuted in the standard family under either extraction.
This result is no longer PRELIMINARY.

The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
expansions: `b = r_in^2 n (1-F)/(2m)` and
`c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
not a failure of the exact spectrum or an inconsistent calculation.

The endpoint m=1 is separate: actual hopping vanishes, active support becomes
`{0}`, and its inradius and spatial coefficients are zero. It is not covered
by the strict inequalities for `0 < m < 1`.

### Small-mass / continuum matching

For each standard coupling in d=1,2,3,

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
the equality of the limits is established analytically. The joint scaling
of momentum, dimensionless mass, neighbor length and time step is specified
in the report. Its continuum statement is local at fixed rescaled momentum
and mass, not a full propagator convergence theorem on arbitrary states.

## 6. Current scientific interpretation

The live idea is no longer:

`c = maximum microscopic speed`,

nor, unqualified, `c_massless = r_in(C_micro)`. The corrected comparison is
`B_infty^*`: `c_0 = c_strict^iso`, the exact strict asymptotic isotropic
speed of the same dynamics (Sec. 4). Its strong form is rejected in the
declared s=4 class (update below). `r_in(C_micro)` remains a provable
upper bound (`c_strict^iso <= r_in(C_micro)`), and is known to be exactly
attained — `c_strict^iso = r_in(C_micro)` — for the standard Pavia Weyl
family in d=3, by an explicit vertex non-nilpotency certificate, not merely
by the linear-order Taylor coefficient.

**Update (2026-09-15, branch-local).** Locality, unitarity, homogeneity and
D2 covariance at fixed `N_3` do **not** force `c_0 = c_strict^iso` once the
internal dimension is enlarged. The s=4 family (Sec. 4.1) keeps the whole
strict body, `C_infty^strict = C_micro`, while its Weyl slope varies
continuously below `1/sqrt(3)`. The strict causal body alone therefore does
not fix the Weyl speed. In this family the missing speed is exactly
accounted for by the inter-sector part of the involutions (the family
identity in Sec. 4.1). Whether that is a structural principle or a feature of
this ansatz is **OPEN**.

What remains unknown is which additional hypotheses restore matching: `s=2`
minimality with or without P17 Eq. (2), irreducibility of the internal
symmetry representation, a whole-symbol common cone, or something else.
Whether `c_strict^iso` saturates `r_in(C_micro)` for every admissible symbol
(saturation, charter Sec. 0(ii)) is a separate question and also remains
open.

At finite mass the two natural extraction procedures differ exactly. A common
relativistic coefficient is recovered in the specified continuum limit.
Additional equivalent representatives cannot resolve the open generality issue;
any successor gate must examine structural freedom under fixed causal geometry
and discrete isotropy.

## 7. GATE STATUS — no calculation currently authorized

**MASSLESS INRADIUS RIGIDITY GATE — COUNTEREXAMPLE_VERIFIED IN DECLARED s=4
CLASS (branch-local); s=2 and irreducible-R classes OPEN; successor gate NOT
YET CHARTERED.**
(Charter name kept for continuity; its comparison target is corrected, see
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0.) Where the charter or
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) still describe the
gate as having no counterexample, this section overrides them
(`PROJECT_INSTRUCTIONS.md` Sec. 2).

### 7.1 Superseded operative plan

The 2026-09-14 deliberation
([`debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md`](../debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md))
predates the s=4 result. It recommended freezing an `s=2` contract on `N_3`,
filtering candidates by non-nilpotent vertices, and escalating to `s>2` only
after exhausting that class. That order was not followed, and its
"rigidity vs saturation" framing cannot continue as written. It is kept as
historical decision material, not as a current plan. Its open point about
whether P17 Eq. (2) is derivable from the charter's identities still matters
for the `s=2` question.

### 7.2 Successor gate — to be chartered before any calculation

No successor calculation is authorized until a charter is committed. Its
question should be narrower than the refuted strong form.

**Candidate from a degraded debate (2026-09-15):**
`GATE_COMPLETITUD_AXIAL_N3 = CANDIDATE_FROM_DEGRADED_DEBATE`, **not
authorized.** In the
[deliberation](../debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.md),
four members proposed `AUTHORIZE_C`. The tool classified the run as
`DEGRADED_NO_CONSENSUS`: ASTRA failed two turns (Codex usage limit) and was
excluded. ASTRA's recorded preference was A, and its objection that C reaches
`c_strict^iso` only through the still unproven bound `c_0 <= c_strict^iso`
was left unanswered. Before any part of that charter, including its first
test, is executed, a short ratification with all five members must run,
using the nilpotency erratum in Sec. 7.3. Until then, none of its steps is
authorized.

Candidate directions, none of them frozen yet:

1. **Surviving bounds.** Which inequalities between `c_0`, `c_strict^iso`
   and `r_in(C_micro)` hold for every admissible symbol? Currently
   `c_strict^iso <= r_in(C_micro)` is established. `c_IR <= r_in(C_micro)`
   is established only under the isotropic-containment premise of Sec. 3.3.
   `c_0 <= c_strict^iso` is not established in general.
2. **Restoring hypotheses.** Which explicitly stated extra assumptions (for
   example `s=2` minimality with or without Eq. (2), or an irreducible `R`)
   give `c_0 = c_strict^iso` for a whole declared class?
3. **Intra/inter rule.** Does the s=4 family identity reflect a general
   structure that accounts for the missing speed, or is it specific to this
   ansatz?

Every class must keep the quantifiers of charter Sec. 2 and be declared
**before** solving.

### 7.3 Original gate question (answered for the declared s=4 class)

The original question was whether another admissible massless symbol can have
`0 < c_0 < c_strict^iso` for its own strict asymptotic body, while preserving
the same `N`, `C_micro`, embedding, unitarity, homogeneity and discrete
isotropy as its selected standard baseline. A candidate whose `c_0 < r_in(C_micro)`
only because its own strict body already falls short of `r_in(C_micro)` is not
this counterexample; see the charter's Sec. 0 for the (i)/(ii) split.

**Erratum (2026-09-15).** Earlier wording here attributed such a shortfall to
a nilpotent one-step coefficient. What is established is only this: a
saturation failure `c_strict^iso < r_in(C_micro)` requires at least one
nilpotent vertex coefficient (contrapositive of the vertex lemma). The
converse is not established. A nilpotent vertex removes the exact ray `n.h`
from `S_n`, but it does not by itself determine `c_strict^iso`, which must be
computed. See the charter's erratum.

The [gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) requires the
internal dimension, isotropy group/action and representation, node/sector,
and any irreducibility assumptions to be explicit before solving. Do not
silently introduce minimality or weaken the symmetry when interpreting a result.

- One exact admissible counterexample refutes B_infty^* for a class containing
  it (realized for the declared s=4 class, Sec. 4.1).
- A rigidity claim requires an exhaustive analytic argument for an explicitly
  quantified class; failure to find a deformation is not such an argument.
- The absence of a continuous deformation alone does not exclude disconnected
  admissible symbols. A restricted proof leaves wider generality open.
- Prior-art classification assumptions must be checked before any novelty claim.

### Stop rule

Until a successor gate is chartered and closed:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO anisotropic-QCA detour**;
- **NO change of support, embedding, time normalization or discrete isotropy
  within a declared rigidity comparison**;
- **NO novelty claim for B*, B_infty^* or the s=4 family (NOVELTY = OPEN)**;
- **NO use of a scalar `v_max` without definition**;
- **NO promotion of the s=4 family identity to a general QCA law**.

A certified falsification within the frozen admissible class is a successful
gate outcome. The s=4 counterexample is such an outcome for its declared
class only. This branch-local reconciliation does not promote anything to
`main` and does not charter the successor gate.
```

### Contexto adjunto: theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md
```
# MASSLESS INRADIUS RIGIDITY GATE

> **Status: HISTORICAL / COMPLETED BY COUNTEREXAMPLE FOR THE DECLARED s=4
> CLASS** (2026-09-15, branch-local). This file is kept as the charter under
> which the counterexample was judged, and it is no longer the sole authorized
> next front. The outcome is `COUNTEREXAMPLE_VERIFIED` (Sec. 5) for the class
> declared in
> [`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md),
> with an [independent review](../reports/2026-09-15--s4-independent-review.md)
> and a [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md).
> The standard Pavia `s=2`, d=3 certificate (Sec. 0) is not affected. Rigidity
> in the published minimal `s=2` class, and in stronger classes with
> additional representation assumptions, remains OPEN, and NOVELTY remains
> OPEN. No successor gate is chartered; current status is in
> [CURRENT_STATE](../state/CURRENT_STATE.md) Sec. 7. The body below is
> unchanged from the pre-counterexample charter, except for the erratum
> below.

> **ERRATUM 2026-09-15 — vertex nilpotency does not decide saturation.**
> Earlier wording in Sec. 0(ii) and in the Sec. 5 `INADMISSIBLE_SATURATION`
> row presented a nilpotent one-step vertex coefficient as the reason for
> `c_strict^iso < \rho_{\rm micro}`. That causal reading is withdrawn. What is
> established:
>
> - For an extreme vertex `h`, the coefficient of `U^n` at `n.h` is exactly
>   `T_h^n`. If `T_h` is nilpotent, `n.h` is not in `S_n` for large `n`.
> - By the vertex lemma, if every vertex coefficient is non-nilpotent, then
>   `C_infty^strict = C_micro` and (ii) holds. So a saturation failure
>   requires at least one nilpotent vertex coefficient.
>
> The converse is **not established**. Losing the exact ray `n.h` does not
> by itself determine `h_infty` or `c_strict^iso`: mixed words can still
> reach near the vertex, and a body truncated near a vertex need not have a
> smaller minimal support. Saturation (ii) must be computed or proved for
> each candidate. Vertex nilpotency alone is neither a certificate of
> `c_strict^iso < \rho_{\rm micro}` nor an admissible explanation of one.

**Original status: OPEN — charter fixed; an executable admissible-class contract is
the next step.** Authority: [CURRENT_STATE](../state/CURRENT_STATE.md).
Predecessor: STANDARD WEYL/DIRAC EXACT GATE, PASS on evidence at `2c7c2c9`.

This charter defines the sole next scientific front. It records no new
counterexample, search result or rigidity theorem. The file name is kept for
continuity of cross-references; the object it is written against has been
corrected (Sec. 0-1 below, 2026-09-14).

## 0. Correction and baseline certificate (2026-09-14)

The gate was originally written as a comparison against the inradius of the
*one-step* microscopic causal body. That object is only an upper bound on the
speed actually reachable by strict propagation after repeated updates, and
the inradius notation is not the right general comparison for a long-run
support body. The correct comparison target is the **strict asymptotic
isotropic speed** `c_strict^iso = min_{n̂} h_infty(n̂)`, defined in
[`CAUSAL_BODY_GEOMETRY.md`](CAUSAL_BODY_GEOMETRY.md) Sec. 6 from
`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`.

For every direction `q`, define

\[
H_n(q)=\max_{x\in S_n}q\cdot x.
\]

The convolution formula for the Fourier coefficients gives

\[
S_{n+m}\subseteq S_n+S_m
\quad\Longrightarrow\quad
H_{n+m}(q)\le H_n(q)+H_m(q).
\]

Thus `(H_n(q))_n` is subadditive, and Fekete's lemma gives

\[
h_\infty(q)
=\lim_{n\to\infty}\frac{H_n(q)}n
=\inf_n\frac{H_n(q)}n.
\]

In particular, grouping `m` updates into one coarse-grained temporal step
does not change the normalized asymptotic support function:

\[
\lim_{r\to\infty}\frac{H_{mr}(q)}{mr}=h_\infty(q).
\]

This proves the coarse-graining invariance of `c_strict^iso` and is the
mathematical reason for using the `B_\infty^*` observable. Since
`S_n/n\subseteq C_{\rm micro}`, the general comparison is instead

\[
h_\infty(\hat q)\le h_{C_{\rm micro}}(\hat q),
\qquad
\rho_{\rm micro}:=
\min_{\|\hat q\|=1}h_{C_{\rm micro}}(\hat q),
\qquad
\boxed{
c_{\rm strict}^{\rm iso}
\le
\rho_{\rm micro}
}.
\]

Only when the relevant `C_micro` is centered does this last number coincide
with its usual inradius. For the centered cubic baseline used below it is
`1/\sqrt d`.

This gate's admissible class already fixes one shared `N_d` for every
candidate symbol, so `\rho_{\rm micro}` is the same fixed number for all of
them; correcting the target does not change that number. What the
correction changes is which question is actually being asked, by splitting
what used to be a single comparison into two logically independent ones for
any candidate symbol with linear massless slope `c_0`:

- **(i) genuine rigidity:** does `c_0 = c_strict^iso` for *that symbol's own*
  strict asymptotic body — does the linear IR slope match the full nonlinear
  strict propagation speed of the same dynamics?
- **(ii) saturation:** does `c_strict^iso = \rho_{\rm micro}` for that symbol —
  does its strict asymptotic body fill the entire shared one-step polytope,
  or does it fall short? (An admissible symbol only needs `T_h != 0`, not
  non-nilpotent powers of `T_h`. A nilpotent vertex coefficient is necessary
  for falling short but does not by itself imply it; see the erratum above.)

A candidate with `c_0 < \rho_{\rm micro}` that fails only (ii) — its own
`c_strict^iso` is already below `\rho_{\rm micro}` — is **not** a counterexample to `B_infty^*` and is not the kind of
result this gate is looking for; it would only have refuted the old,
superseded comparison against the one-step body. Only a failure of (i) is a
genuine rigidity counterexample. See
[`B_STAR_HYPOTHESIS.md`](B_STAR_HYPOTHESIS.md) Sec. 9.

**Established baseline fact (certified, not open):** for the standard Pavia
Weyl family in d=3 (`A+, B+, A-, B-`), both (i) and (ii) hold exactly:
`c_0 = \rho_{\rm micro} = r_{\rm in}(C_{\rm micro}) = 1/\sqrt3`
(because this is the centered cubic case; linear slope, prior exact gate) and
`C_infty^strict = C_micro` exactly, hence
`c_strict^iso = \rho_{\rm micro}`
(indeed, `\operatorname{conv}(S_n/n)=C_{\rm micro}` for every `n\ge1`)
(new vertex certificate: every one-step corner's Fourier coefficient is
rank-one and not nilpotent, so it survives at `n.h` for every `n`). Full
derivation:
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md);
machine record:
[`2026-09-14--vertex-idempotency-verification.md`](../reports/2026-09-14--vertex-idempotency-verification.md),
375 exact checks. **This is a fact about the standard baseline itself, not
an answer to Sec. 1's question about *other* admissible symbols**, and it
covers d=3 only — d=1, d=2 are not checked by this certificate.

## 1. Question and invariant comparison

For a selected standard baseline in d=1,2,3, can another admissible unitary
massless symbol have, in the sense of (i) above,

\[
0<c_0<c_{\rm strict}^{\rm iso}
\]

for its own strict asymptotic body — while keeping the same active one-step
neighborhood, causal body, Euclidean embedding, time normalization,
homogeneity and discrete isotropy as the selected standard baseline? (A
candidate additionally failing saturation (ii) is a separate, weaker
observation; see Sec. 0.)

The baseline geometries are

\[
N_d=\{(\epsilon_1,\ldots,\epsilon_d)/\sqrt d:\epsilon_j=\pm1\},
\quad C_d=[-1/\sqrt d,1/\sqrt d]^d,\quad r_d=1/\sqrt d.
\]

Choose the baseline before solving. Comparisons are within that fixed
geometry, not between dimensions. Every h in N_d must retain a nonzero
Fourier coefficient matrix, with none outside N_d. Merely retaining a
declared allowed neighborhood while actual support shrinks is insufficient.
Adding an on-site Fourier term changes N_d even if its hull would not change.

A common change of units, a different number of updates per time unit, or a
different spatial embedding cannot be used to manufacture a smaller ratio.

## 2. Mandatory class declaration before solving

Each calculation must freeze a permanent case contract containing:

| Item | Required declaration |
| --- | --- |
| Geometry | d, explicit N_d, embedding, one complete time step and Fourier convention |
| Internal degrees of freedom | Fixed finite dimension s and coefficient parameter domain |
| Discrete isotropy | The same baseline group/action L on N_d, its positive generating set if relevant, and exact covariance requirements |
| Internal symmetry | A specified unitary/projective representation R of L, fixed within the calculation |
| Gapless sector | Node k_star, quasienergy origin, branch convention, sector dimension and isolation from other bands |
| Relativistic cone | Nonzero, untilted, isotropic linear speed in the fixed Euclidean coordinates; an axis slope alone is insufficient |
| Reducibility/minimality | Whether assumed; sector support and the role of any spectator blocks |
| Coverage | Full coefficient class versus a particular ansatz, including any disconnected components not covered |
| Equivalences | Constant basis conjugations, symmetry relabelings, transposes/chiralities and node relabelings identified explicitly |

Fixing the causal body and saying "discrete isotropy" does not specify s,
the symmetry representation or the relevant massless sector. A trivial or
weaker symmetry group cannot replace the baseline's isotropy. Discrete
covariance and an isotropic IR cone are separate admission requirements.

Begin with source and class-definition work, not a solver run. Minimal s=2
and enlarged internal spaces are different quantified classes. No result
proved only with minimality may be presented as following from locality,
unitarity, homogeneity and discrete isotropy alone. A change of s or R needs
its own declared class before calculation, with the same geometric and group
action constraints; it cannot silently alter an existing comparison.

For a selected sector, document how its support relates to the full active
support. A reducible/direct-sum example must be identified as such and judged
against the declared quantifiers. Do not silently rule it out or present
spectator-supported geometry as intrinsic to the selected sector. If one
instead requires irreducibility or a common cone for the whole symbol, that
is an additional hypothesis and limits any rigidity conclusion.

## 3. Exact admission checks

Write the homogeneous finite-range symbol as

\[
U(\mathbf k)=\sum_{h\in N_d}e^{-i\mathbf k\cdot h}T_h,
\qquad T_h\in\mathbb C^{s\times s},\quad T_h\ne0.
\]

For every displacement difference ell, verify the coefficient identities

\[
\sum_{h'-h=\ell}T_h^\dagger T_{h'}=\delta_{\ell0}I_s,
\qquad
\sum_{h-h'=\ell}T_h T_{h'}^\dagger=\delta_{\ell0}I_s.
\]

These certify unitarity for every momentum rather than on a finite mesh.
For every group element g, verify

\[
T_{gh}=R_gT_hR_g^\dagger,
\qquad U(g\mathbf k)=R_gU(\mathbf k)R_g^\dagger.
\]

Check the declared representation, active support and node exactly. In the
specified gapless sector derive the full linearized spectrum, requiring

\[
\omega_\pm(\mathbf k_\star+\mathbf p)-\omega_\star
=\pm c_0|\mathbf p|+O(|\mathbf p|^2),\qquad c_0>0,
\]

in every direction. Rule out a residual mass gap, tilt, flat band mistaken
for a cone, or anisotropic linear metric before comparing c_0 with the
candidate's own `c_strict^iso` (Sec. 0); comparing only against r_d checks
saturation (ii), not genuine rigidity (i), and the two must not be conflated.
If there are multiple cone sectors, identify exactly which are quantified.

These are admission criteria, not assertions that a new admissible symbol
exists. Any scientific code implementing them must be retained in the repo.

## 4. Adversarial sequence and acceptance

1. Read the primary classification results and list their actual assumptions:
   support, s, isotropy action/representation, minimality, node and equivalences.
   The prior battery did not establish an exhaustive classification. Check
   whether a proposed rigidity statement is already covered by existing work.
2. Freeze one admissible-class contract and its quantified target. Derive the
   coefficient constraints before choosing a special product/coin ansatz;
   if an ansatz is used, state its coverage ceiling.
3. Seek a structural counterexample while retaining all admission conditions.
   A failed condition makes a candidate inadmissible, not a falsifier of
   B_infty^*. Stop its certification at the first failed condition and
   record the reason.
4. Accept a counterexample only with exact support, unitary and covariance
   certificates, a massless isotropic linearization, and a proved strict
   inequality `0 < c_0 < c_strict^iso` for that candidate's own strict
   asymptotic body, in the same units (Sec. 0(i)). A candidate satisfying
   only `0 < c_0 < r_d` while `c_strict^iso < r_d` for the same candidate
   (saturation failure, Sec. 0(ii)) is not this counterexample; record it
   separately as INADMISSIBLE_SATURATION (Sec. 5). Numerical suggestions
   need exact certification; no finite scan or tolerance establishes the
   claim.
5. If no counterexample is obtained, retain OPEN unless an exhaustive analytic
   argument proves matching for every member of the declared class. Local
   absence of deformations does not exclude disconnected solutions.

The seven old symbols may serve as controls. Repeating related representatives
does not increase the number of independent geometries or establish coverage
of structural degrees of freedom.

## 5. Outcomes and claim ceilings

| Outcome | Meaning |
| --- | --- |
| COUNTEREXAMPLE_VERIFIED | `0 < c_0 < c_strict^iso` proved for that candidate's own strict body (Sec. 0(i)): B_infty^* is false for the declared class and any broader claim including this admissible example |
| RIGIDITY_PROVED_FOR_FROZEN_CLASS | `c_0 = c_strict^iso` is proved for every member with every class restriction retained; wider classes remain open |
| INADMISSIBLE_SATURATION | Candidate is admissible and `c_0 = c_strict^iso` (i) holds, but `c_strict^iso < r_d` (ii) fails — a saturation failure, certified by computing `c_strict^iso` and not inferred from vertex nilpotency (erratum above); not a rigidity counterexample; B_infty^* is not decided by this candidate |
| INADMISSIBLE_CANDIDATE | At least one invariant or cone condition fails; B_infty^* is not decided |
| INCONCLUSIVE / OPEN | No certified counterexample or exhaustive proof; a solver failure or unsuccessful search is not rigidity |

Even a rigidity result here would not establish inter-species universality A
or general continuum matching for other couplings. Novelty requires the
separate source comparison. No anisotropic-QCA detour, broad model search,
causal sets or new substrate class is authorized by this charter.
```

### Contexto adjunto: theory/S4_STRICT_CONE_COUNTEREXAMPLE.md
```
# S4 strict-cone counterexample family

**Branch-local status:** analytic freeze for independent review.  
**Canonical state:** unchanged; `state/CURRENT_STATE.md` remains authoritative until a later explicit promotion commit.

## 1. Claim under test

The strong form of the working hypothesis was

\[
B_\infty^*:\qquad c_0=c_{\rm strict}^{\rm iso},
\]

with the strict asymptotic body defined from exact Fourier support under iteration.

This note gives an explicit `s=4` family on the same BCC neighborhood and the same non-trivial Pauli projective `D_2` symmetry class for which

\[
C_\infty^{\rm strict}=C_{\rm micro},\qquad
c_{\rm strict}^{\rm iso}=\frac1{\sqrt3},
\]

but

\[
c_0(a)=\frac{a}{\sqrt3},\qquad 0<a<1.
\]

Thus the strict causal body alone does not fix the Weyl slope once the internal multiplicity is enlarged from `s=2` to `s=4`.

This does **not** refute the classified `s=2` Pavia result.

## 2. Definition of the family

Let `sigma_i` act on the Pauli factor and `tau_i` on a two-dimensional multiplicity factor,

\[
\mathbb C^4=\mathbb C^2_\sigma\otimes\mathbb C^2_\tau.
\]

For

\[
0<a<1,\qquad b=\sqrt{1-a^2},
\]

define

\[
T_x=b\tau_x+a\tau_z,\qquad
T_y=b\tau_y+a\tau_z,\qquad
T_z=-b\tau_x+a\tau_z,
\]

and

\[
\Gamma_x=\sigma_x\otimes T_x,\qquad
\Gamma_y=\sigma_y\otimes T_y,\qquad
\Gamma_z=\sigma_z\otimes T_z.
\]

Each `T_i` is Hermitian and satisfies `T_i^2=I`, hence each `Gamma_i` is Hermitian and involutory.

The original one-parameter counterexample uses

\[
W=I\otimes e^{-i\pi\tau_z/4}
\]

and

\[
A_a(\mathbf k)
=W e^{-iq_x\Gamma_x}e^{-iq_y\Gamma_y}e^{-iq_z\Gamma_z},
\qquad q_i=k_i/\sqrt3.
\]

A useful two-parameter deformation is

\[
A_{a,\theta}(\mathbf k)
=W_\theta e^{-iq_x\Gamma_x}e^{-iq_y\Gamma_y}e^{-iq_z\Gamma_z},
\qquad
W_\theta=I\otimes e^{-i\theta\tau_z}.
\]

The counterexample itself requires only `theta=pi/4`.

## 3. Exact unitarity and BCC Fourier support

Because `Gamma_i^2=I`,

\[
e^{-iq_i\Gamma_i}=e^{-iq_i}P_i^+ + e^{iq_i}P_i^-,
\qquad
P_i^\pm=\frac{I\pm\Gamma_i}{2}.
\]

Therefore, with

\[
h_s=\frac{(s_x,s_y,s_z)}{\sqrt3},\qquad s_i\in\{\pm1\},
\]

and the repository Fourier convention `exp(-i k.h)`, the only Fourier coefficients are

\[
A_{h_s}^{(a,\theta)}
=W_\theta P_x^{s_x}P_y^{s_y}P_z^{s_z}.
\]

There are exactly eight BCC modes and no on-site coefficient `A_e`.

Unitarity is exact for every `k`, since the four factors in `A_{a,theta}(k)` are unitary.

## 4. Exact D2 covariance

Use

\[
R_x=\sigma_x\otimes I,\qquad
R_y=\sigma_y\otimes I,\qquad
R_z=\sigma_z\otimes I.
\]

These realize the same non-trivial Pauli projective class used by the minimal Weyl walk. They commute with `W_theta`. Conjugation by `R_x` fixes `Gamma_x` and flips `Gamma_y,Gamma_z`; cyclically for `R_y,R_z`. Hence

\[
R_l A_{a,\theta}(\mathbf k)R_l^\dagger
=A_{a,\theta}(l\mathbf k)
\]

for the binary rotations of the BCC tetrahedral generators.

## 5. Vertex survival and the strict asymptotic body

For a BCC vertex coefficient,

\[
\operatorname{tr}A_{h_s}^{(a,\theta)}
=
\frac12\left[
\cos\theta
+s_xs_ys_z\,a\left(\sin\theta-2(1-a^2)\cos\theta\right)
\right].
\]

At the counterexample point `theta=pi/4`, this becomes

\[
\operatorname{tr}A_{h_s}^{(a)}
=
\frac{\sqrt2}{4}
\left[1+s_xs_ys_z\,a(2a^2-1)\right].
\]

For `0<a<1`,

\[
|a(2a^2-1)|<1,
\]

so every trace is nonzero. Therefore no vertex coefficient is nilpotent.

Let `S_n` be the exact Fourier support of `A_a^n`. Since each `h_s` is an extreme vertex of

\[
C_{\rm micro}=\operatorname{conv}\{h_s\}
=[-1/\sqrt3,1/\sqrt3]^3,
\]

the displacement `n h_s` can arise from only the word `h_s+...+h_s`. Its coefficient is therefore exactly

\[
(A_{h_s}^{(a)})^n\neq0.
\]

Hence every vertex of `C_micro` lies in `S_n/n` for every `n`, while every `n`-step average lies in `C_micro`. Thus

\[
\boxed{\operatorname{conv}(S_n/n)=C_{\rm micro}\quad\forall n\ge1}
\]

and consequently

\[
\boxed{C_\infty^{\rm strict}=C_{\rm micro}},\qquad
\boxed{c_{\rm strict}^{\rm iso}=1/\sqrt3}.
\]

For fixed `a`, the same vertex-survival conclusion persists on an open interval of `theta` around `pi/4` by continuity of the nonzero trace condition. No global all-`theta` strict-cone claim is made here.

## 6. Irreducibility

Suppose `X` commutes with all eight Fourier coefficients. Summing the coefficients gives

\[
W_\theta=\sum_s A_{h_s}^{(a,\theta)},
\]

and sign-weighted sums give

\[
W_\theta\Gamma_i=\sum_s s_i A_{h_s}^{(a,\theta)}.
\]

Therefore `X` commutes with `W_theta` and all three `Gamma_i`.

For `sin(theta) != 0`, the two eigenvalues of `W_theta` on the `tau_z` factor are distinct, so `[X,W_theta]=0` makes `X` block diagonal in the `tau_z` decomposition. Because `a!=0` and `b!=0`, commuting with `Gamma_x` forces the two blocks to coincide and to commute with `sigma_x`. Commuting with `Gamma_y` then forces that common block also to commute with `sigma_y`. The only such `2x2` matrix is scalar. Hence

\[
\boxed{\{X:[X,A_{h_s}]=0\ \forall s\}=\mathbb C I_4}.
\]

The family is not a direct sum of two decoupled `s=2` Weyl walks.

## 7. Weyl sectors and tunable velocity

At `k=0`,

\[
A_{a,\theta}(0)=W_\theta
\]

has two rank-two eigenspaces with eigenvalues `exp(-i theta)` and `exp(+i theta)`. For `0<theta<pi/2` they are spectrally separated by quasienergy

\[
\Delta\varepsilon=2\theta.
\]

On the `tau_z=+1` doublet,

\[
P_+\Gamma_iP_+=a\,\sigma_iP_+,
\]

so the first-order effective Hamiltonian is

\[
H_{\rm eff,+}
=\theta I_2
+\frac{a}{\sqrt3}\,\mathbf k\cdot\boldsymbol\sigma
+O(|\mathbf k|^2).
\]

The other doublet has the opposite linear orientation and the same speed magnitude. Therefore

\[
\boxed{c_0(a)=a/\sqrt3}.
\]

At `theta=pi/4`, for every `0<a<1`,

\[
0<c_0(a)<c_{\rm strict}^{\rm iso}=1/\sqrt3.
\]

This is the explicit counterexample to the strong `B_infty*` claim in the declared `s=4` class.

## 8. Two-parameter deformation and projector quantum metric

Let `P_+(k)` denote the rank-two spectral projector continuing the `exp(-i theta)` doublet near `k=0`, and define

\[
g_{ij}(0)=\frac12\operatorname{Tr}[(\partial_iP_+)(\partial_jP_+)].
\]

For a normal unitary,

\[
Q(\partial_iP_+)P_+
=
\frac{Q(\partial_iA)P_+}
{e^{-i\theta}-e^{+i\theta}},
\qquad Q=I-P_+.
\]

At `k=0`,

\[
\partial_{k_i}A=-\frac{i}{\sqrt3}W_\theta\Gamma_i,
\]

and the off-doublet part of `T_i` has magnitude `b=sqrt(1-a^2)`. Since `Tr(sigma_i^2)=2`,

\[
\boxed{g_{ij}(0)=\frac{1-a^2}{6\sin^2\theta}\,\delta_{ij}}.
\]

Thus

\[
\boxed{
 c_0^2+2\sin^2(\Delta\varepsilon/2)\,g_{ii}(0)
 =\frac13
 =(c_{\rm strict}^{\rm iso})^2
}
\]

(no sum on `i`). At `theta=pi/4`, the prefactor is one and this reduces to `c0^2+g_ii=1/3`.

This weighted identity is **established for this family only**. It is not promoted here to a general QCA theorem. The more primitive structural fact is the intra/inter-sector decomposition `a^2+b^2=1` of the microscopic involutions `Gamma_i`.

## 9. Scope and interpretation limits

1. The `s=2` Pavia classification and its fixed `c0=1/sqrt(3)` remain intact.
2. `A_{a,theta}(0)=W_theta` is not a global phase. The Weyl doublets live at nonzero Floquet quasienergy.
3. `C_infty^strict` is an exact-support body. Vertex amplitudes may decay exponentially with iteration even though they remain nonzero. No claim is made here about an essential/ballistic/Lieb-Robinson front defined by amplitude decay.
4. The weighted quantum-metric rule is a family identity, not yet a substrate principle.
5. No novelty claim is made by this note. Prior-art comparison is a separate gate.
```


## Ronda 1 — ASTRA

[INFERENCE] Voto: `PREFER_A`. La prioridad es resolver si el soporte estricto asintótico limita el cono local; la identidad axial, incluso acompañada de una interpretación métrica, no resuelve esa comparación por sí sola.

[RECONSTRUCTION] La versión más fuerte de C combina tres obligaciones independientes: completitud axial, identificación geométrica del defecto y techo asintótico en todas las direcciones. Concedo a CLAUDE OPUS que incorporar (3) con FAIL propio impide declarar PASS de C dejando pendiente el techo. Mi objeción no puede ser que C necesariamente omita A.

[INFERENCE] Pero esa incorporación tampoco demuestra que convenga empezar por L1. Además, la subsunción necesita precisar sus cuantificadores: C formula (3) para un cúmulo exclusivamente cónico; A debe poder acotar un cono identificado dentro de un cúmulo con otras pendientes. La pureza del cúmulo puede ser necesaria para convertir una traza normalizada en `c_0²`; no queda justificado trasladarla al techo de cada rama. Presentar ambos alcances como idénticos exige ese paso.

[INFERENCE] La objeción más fuerte al orden propuesto es que sus primeras pruebas pueden completar todo el presupuesto local y dejar intacta la única obligación que compara con el objeto central. El éxito del control sobre la familia certificada tampoco discrimina ese problema: allí el cuerpo estricto ya coincide con el microscópico. **Condición de concesión:** que C empiece por (3), conserve el alcance de A para los sectores cónicos identificados y registre separadamente su resultado, aunque después falle la identificación métrica. Eso desactivaría mi objeción de prioridad y permitiría ratificar C como programa compuesto.

[UNVERIFIED] Hay un puente plausible, pendiente de revisión, que podría simplificar la primera prueba. Para cada dirección y cada entero `n`, definir `J_n=i(U^n)†∂_{\hat q}(U^n)`. Si `P` proyecta sobre un autovalor de `U(0)`, la regla del producto sugiere `PJ_nP=nPJ_{\hat q}P`, incluso cuando otros autovalores se fusionen al elevar a `n`. Bernstein centrado aplicado a `U^n` debería situar `J_n` entre los extremos proyectados de su soporte exacto. La compresión daría entonces `c_0≤H_n(\hat q)/n`; Fekete y la cuantificación sobre todas las direcciones cerrarían la comparación. Esta ruta exige verificar tanto Bernstein como la identificación de las pendientes; no constituye aquí una prueba de (3).

[INFERENCE] Respecto de `GATE_A_N3`, mantengo geometría, unidades, unitariedad y ausencia de búsquedas. Precisaría que el cono seleccionado tiene pendientes `±c_0` en toda dirección, sin exigir que todas las demás ramas del cúmulo compartan esa pendiente. Corregiría también FAIL a `c_strict^iso<c_0`: exigir adicionalmente `c_strict^iso>0` dejaría fuera una posible refutación con soporte isotrópico nulo. La nilpotencia no sustituye ningún certificado de esa desigualdad.

[INFERENCE] Condición de cambio: un símbolo admisible certificado con `c_strict^iso<c_0` me haría pasar a `REJECT_BOTH`, porque refutaría A y el punto obligatorio (3) de C. El fracaso de la ruta técnica propuesta produciría solamente `INCONCLUSIVE`; no convertiría la identidad axial en una respuesta sobre el cuerpo estricto.

## Ronda 1 — CLAUDE OPUS

**1. Voto:** `RATIFY_C`, condicionado a la enmienda (i) de abajo.

Concuerdo con ASTRA en tres puntos y los doy por incorporados: que el FAIL de (3) debe ser `c_strict^iso < c_0` sin exigir `c_strict^iso > 0`; que el alcance de (3) no puede heredar la hipótesis de cúmulo puramente cónico que (2) sí necesita; y que ratificar C sin tocar (3) sería ratificar un programa que puede completarse sin pronunciarse sobre el objeto central. Concuerdo con la errata: «vértice nilpotente ⇒ caída de saturación» queda sin apoyo.

**2. Puente.** Ataco la premisa compartida por ASTRA y por el propio tema —que L1 es «local/espectral de un paso» y `c_strict^iso` «asintótico de soporte», niveles sin contacto—. [ORIGINAL] L1 no es una identidad sobre `J_x`: es una factorización de la dinámica. Con la notación del tema, `M := X_+ + X_-` cumple `M†M = I` (los cruzados se anulan), y `MΠ_+ = X_+X_+†X_+ + X_-X_+†X_+ = X_+` porque `X_-X_+† = 0`; análogamente `MΠ_- = X_-`. Luego

`U(k) = M(k_⊥)·exp[−i k_x (Π_+−Π_-)/√3]`,

con `M` y `Π_±` independientes de `k_x`. [INFERENCE] Esto es exactamente un shift condicional en `x` compuesto con un unitario de rebanada: confirma y agrava la advertencia del tema sobre novedad —L1 *es* la forma bipartita, no está «cerca» de ella.

[ORIGINAL] La consecuencia es el puente pedido. El desplazamiento axial máximo en `n` pasos, `n/√3`, sólo lo produce la palabra de signos `+`, cuyo coeficiente es exactamente `(X_+)^n`. Por tanto `H_n(x̂) = n/√3` si y sólo si `X_+(k_⊥)^n ≢ 0`, y si `X_+^m = 0` cada bloque de `m` pasos consecutivos contiene un `−`, luego

`h_∞(x̂) ≤ (1 − 2/m)/√3 < 1/√3`.

[INFERENCE] El objeto correcto para el soporte axial no es la nilpotencia de vértice —necesaria y no suficiente, como establece la errata— sino la nilpotencia de **cara** de `X_±`, que sí decide en ambas direcciones y que L1 entrega gratis, porque `Π_+` es el proyector espectral de `√3 J_x`. La misma álgebra que fija el presupuesto controla el extremo axial de `S_n`. **Condición de concesión:** que el coeficiente del desplazamiento extremo no sea `(X_+)^n`, o que falle el álgebra de L1.

Límite estricto: esto da `h_∞` en `±x̂, ±ŷ, ±ẑ`. No da `min_n̂ h_∞`: un cuerpo contenido en el cubo puede tocar las seis caras y tener inradio menor. El salto axial→isótropo sigue siendo el problema abierto que el tema exige no esconder en el nombre.

**3. Enmiendas (tres).**

(i) **El primer paso autorizado no es L1 sola, sino L1 más su corolario axial**: probar la factorización, `h_∞(x̂) = 1/√3 ⟺ X_+` no nilpotente, y la cota `(1−2/m)/√3`. Así el primer paso ya toca el cuerpo estricto y la objeción de prioridad de ASTRA queda desactivada sin reordenar el charter. Si el corolario falla, degradación a `GATE_A_N3`.

(ii) **Sustituir en todo el charter «certificado de vértices» por «certificado de cara»**, registrando que el de vértice es sólo suficiente.

(iii) **Declarar el salto axial→isótropo como FAIL parcial explícito**: probar (1)–(3) en los ejes y no en toda `n̂` es `INCONCLUSIVE` sobre `c_strict^iso`, no PASS.

**5. Condición de cambio.** Si el corolario axial de (i) resulta falso —esto es, si `h_∞(x̂)` no queda determinado por la nilpotencia de `X_+`—, L1 vuelve a ser cinemática pura, el puente desaparece y paso a `PREFER_A`.

## Ronda 1 — CIRO

1. Voto: `RATIFY_C`.

2. Concuerdo con ASTRA en que el FAIL propio de (3) no omite A, y en que un programa que agote L1 y la métrica puede cerrarse sin pronunciarse sobre el objeto central. Concuerdo con CLAUDE OPUS en la errata, en no trasladar a (3) la hipótesis de cúmulo puramente cónico, en el FAIL `c_strict^iso<c_0` sin exigir positividad, y en no esconder el salto axial→isótropo. Ataco su tesis de que el corolario de cara desactiva la objeción de prioridad.

C, en (1)–(2), no estudia el cuerpo estricto: da una identidad cinemática contra `r_in²`. [SOURCE] El tema separa ambos niveles y advierte que L1 fácil no justifica elegir C, y que la falsación vive en (3) y en la identificación métrica. [SOURCE] En `s=4`, `C_∞^strict=C_micro` y `0<c_0<c_strict^iso`.

El puente de OPUS conecta L1 con la saturación (ii) en los ejes, no con la rigidez (i). [SOURCE] Errata: vértice nilpotente no decide `min h_∞`; la cota complementaria en `ĥ` queda `≥2/3>1/√3`. [INFERENCE] Si `X_+^m=0`, entonces `H_n(x̂)<n/√3`, luego `c_strict^iso≤h_∞(x̂)<r_in`: la cara sí decide (ii) axial. [SOURCE] El contraejemplo tiene los ocho coeficientes de vértice no nilpotentes, luego `X_+` no es idénticamente nilpotente. [INFERENCE] Un primer paso centrado en esa nilpotencia pasa en `s=4` y deja intacta la desaturación que abrió el problema. Condición de concesión: que la factorización axial determine `min_n̂ h_∞` o acote `c_0`. [ABSENCE] Ninguno de esos dos pasos figura en el acta.

El único puente plausible hacia `c_strict^iso` en todas las direcciones es espectral: ramas analíticas de `U`, Hellmann–Feynman sobre la compresión del cono identificado, Bernstein centrado en `U^n`, Fekete. [UNVERIFIED] Rellich y Bernstein. Eso es (3), no un corolario de L1. C es preferible a A como charter compuesto porque (2) formula el defecto que `s=4` exhibe y (3) conserva el techo con FAIL propio; no lo es si la primera prueba es el paso que casi no puede fallar.

3. Enmiendas. (i) El primer paso autorizado es (3), no L1. Alcance: cono con `±c_0` en toda dirección, sin exigir que el resto del cúmulo sea cónico. FAIL: `c_strict^iso<c_0`. El resultado se registra aunque falle la identificación métrica. Si (3) queda INCONCLUSIVE, no se continúa con L1 como enunciado sobre `B_∞^*`. (ii) Probar (1)–(2) o `h_∞` axial no es PASS de `c_strict^iso`. Sustituir el certificado de vértices por la distinción vértice/cara; la cara no sustituye (3). (iii) L1 y (2) quedan posteriores. Atribuir AF16/17; NOVELTY=OPEN.

5. Un símbolo certificado con `c_strict^iso<c_0` me pasa a `REJECT_BOTH`. Si la primera prueba de (3) queda INCONCLUSIVE, paso a `PREFER_A`.

