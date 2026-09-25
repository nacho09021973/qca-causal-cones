# INFORME DE REVISIÓN ADVERSARIAL — Punto (3), techo `c_0 <= c_strict^iso`

**Fecha:** 2026-09-16.
**Rama:** `research/b-infinity-post-s4-gate`.
**HEAD revisado:** `db083af` (demostración preliminar); contrato congelado en `4135625`.
**Objeto:** [`reports/2026-09-16--point-3-strict-cone-ceiling.md`](reports/2026-09-16--point-3-strict-cone-ceiling.md)
contra [`theory/STRICT_CONE_CEILING_N3_GATE.md`](theory/STRICT_CONE_CEILING_N3_GATE.md).
**Modo de la revisión:** sólo lectura; no se ejecutó ningún script científico,
búsqueda de modelos ni simulación. Todos los cálculos de contraste son
manuales.
**Naturaleza:** revisión adversarial independiente por un (1) revisor. **No** es
una ratificación de cinco miembros, **no** ratifica el gate C completo y **no**
es una auditoría de prior art.

**VERDICT = ACCEPT_AS_WRITTEN**
**THEOREM_STATUS = PROVED_UNDER_FROZEN_CONTRACT**

## Resumen (10 líneas)

1. Reconstruí de forma independiente las etapas (2)–(8); ninguna falla.
2. El lema (2) es correcto y no esconde hipótesis de grado exacto, invertibilidad ni conmutatividad.
3. `J_n = aI + F(1)†F'(1)` es correcta, pero el control de signo del informe es degenerado (`D=0`, `B=0`): lo verifiqué aparte con un control no degenerado.
4. La extensión a todas las direcciones es legítima: se hace a `n` fijo, sin intercambio con `n→∞` ni con el mínimo esférico.
5. Derivé por separado `J_n = Σ_j U_*^{-j} J U_*^j` y `P J_n P = n P J P`; sólo usan `[P,U_*]=0` y `U_*P=λ_*P`.
6. El paso pendiente→autovalor de `PJP` usa sólo compacidad y una subsucesión; no invoca Rellich, base propia continua, diferenciabilidad multivariable ni separación espectral.
7. Fekete, finitud, Lipschitz y existencia del mínimo están correctamente descargados; la positividad de `c_strict^iso` es consecuencia, no hipótesis.
8. No hay circularidad: `v_* ∈ Ran P` se **deriva**; no se presupone contención del cono en el cuerpo estricto.
9. Contrastes independientes pasan: Pavia (saturación) y s=4 (`PJP` tiene autovalores `±a/√3 = ±c_0`, calculado a mano).
10. No hallé defecto fatal ni laguna reparable; las objeciones son expositivas, de control y de alcance interpretativo.

## Tabla de auditoría A–G

| | Resultado | Justificación |
|---|---|---|
| **A** Lema polinómico | **CORRECTO** | Contracción en el disco: `a†F(z)b` escalar, módulo ≤1 en el círculo → máximo módulo → `‖F(z)‖ = sup_{a,b}\|a†F(z)b\| ≤ 1` en `\|z\|≤1`. Hermiticidad: derivando `F(e^{-it})†F(e^{-it})=I` en `t=0` sale `iF'(1)†F(1) − iF(1)†F'(1)=0`, i.e. `B†=B`. `B⪰0`: `g(r)=‖F(r)v‖²≤g(1)` para `r<1` porque `F(1)` es unitaria, y `g'(1)=2Re⟨v,Bv⟩=2⟨v,Bv⟩` (verificado por coeficientes: `g'(1)=Σ_{j,l}(j+l)v†C_j†C_l v`). Cota superior: `G(z)=Σ_j C_j z^{D−j}` es polinomio, `‖G(z)‖=‖F(z̄)‖=1` en el círculo, `G(1)=F(1)`, `G'(1)=DF(1)−F'(1)`, luego `G(1)†G'(1)=DI−B⪰0`. **No hay hipótesis oculta**: no se usa grado exacto (`G` sólo necesita grado nominal ≥ real), ni invertibilidad en el disco, ni conmutatividad. Controles: `F=z^d` → `B=d`; `F=diag(1,z^D)` → `B=diag(0,D)`; `D=0` → `B=0`. |
| **B** Soporte → cota operatorial | **CORRECTO** (con objeción O1 sobre el control, no sobre el paso) | Normalización: `N_3 ⊆ (1/√3)Z³` ⟹ `S_n ⊆ (1/√3)Z³` ⟹ para `q=√3m`, `q·x ∈ Z`. Esto es exactamente lo que hace que `U(tq)^n` sea función de `z=e^{-it}` (Laurent con exponentes enteros); sin ello no hay polinomio. `F(z)=z^{-a}L(z)` tiene exponentes en `[0,b−a]` y `F(e^{-it})=e^{iat}U(tq)^n` es unitaria en todo el círculo. Reconstruí la identidad omitida: `U(tq)^n = e^{-iat}F(e^{-it})`, `d/dt\|_0 = −i(aF(1)+F'(1))`, y multiplicando por `iF(1)†` (con `F(1)=U_*^n`) sale `J_n(q)=aI+B`. **Extracción del monomio y cancelaciones**: agrupar por `q·x` sólo puede anular coeficientes, nunca crear exponentes fuera de `[a,b]`; el lema se aplica con `D=b−a` como cota superior del grado, de modo que los extremos del soporte completo **siguen siendo cotas válidas aunque desaparezcan al restringir a la recta**. La cota resultante es entonces posiblemente no ajustada, lo cual es inocuo para una desigualdad `≤`. Signo de Fourier: coherente (`U(k)=e^{-ik·h}` desplaza por `+h`, `ω(k)=k·h`, `∇ω=h`). |
| **C** Todas las direcciones | **CORRECTO** | `J_n(λq)=λJ_n(q)` (real-lineal, `J_n(q)=U_*^{-n}Σ_x(q·x)A_{n,x}`), `H_n(λq)=λH_n(q)` para `λ>0`. `√3·Q³` es denso en `R³`. A `n` **fijo**: `J_n` lineal (continua), `H_n` máximo de finitas lineales (continua), cono PSD cerrado ⟹ (3) para todo `q` real. **No hay intercambio ilegítimo**: el orden es (i) `n` fijo → todas las direcciones; (ii) `q` fijo → `n→∞`; (iii) mínimo sobre la esfera al final. Como `c_0` es la misma constante en todas las direcciones (hipótesis de admisión), `c_0 ≤ inf_q inf_n H_n(q)/n` es inmediato. |
| **D** Compresión y potencias | **CORRECTO** | Derivación propia: `∂_q(U^n)\|_0 = Σ_{j=0}^{n-1} U_*^j(∂_qU(0))U_*^{n-1-j}`; con `∂_qU(0) = −iU_*J`, `J_n = Σ_j U_*^{-n+j+1}JU_*^{n-1-j} = Σ_{i=0}^{n-1}U_*^{-i}JU_*^{i}`. Compresión: `P` es proyector espectral de la **unitaria** `U_*`, luego `[P,U_*]=0` y `PU_*^{-i}JU_*^iP = λ_*^{-i}λ_*^i PJP = PJP` ⟹ `PJ_nP = nPJP`. **Colisiones Floquet**: no aparece ningún denominador de gap de `U_*^n`; verificado contra el control s=4 (`W^4 = −I`, cuyo proyector espectral tiene rango 4, mientras el `P` usado tiene rango 2 — la identidad no se altera). **Términos entre sectores**: la compresión de una desigualdad de operadores es válida sin conmutación; los bloques `P`–`Q` no necesitan anularse. **`P=I` (r=s)**: `J_n = nJ` y (3) da directamente la cota. |
| **E** Pendientes del cono | **CORRECTO**; distinción admisión/demostrado bien trazada | La hipótesis usada es mínima: existe, para cada `q` unitario y alguna sucesión `t_j↓0`, un autovalor `λ(t_j)` de `U(t_jq)` con `λ(t_j)=λ_*e^{-i(t_jc_0+o(t_j))}`. De ahí: compacidad de la esfera unidad en `C^s` da `v(t_j)→v_*`; el límite de `U(t_jq)v(t_j)=λ(t_j)v(t_j)` da `U_*v_*=λ_*v_*`, luego **`v_*∈Ran P` se deriva** (no se asume). La identidad proyectada `P[(U(tq)−U_*)/t]v(t) = [(λ(t)−λ_*)/t]Pv(t)` es exacta usando `PU_*=λ_*P`; ambos límites existen (`(U(t_jq)−U_*)/t_j → ∂_qU(0)` en norma, `(λ(t_j)−λ_*)/t_j → −iλ_*c_0`). Multiplicando por `i λ̄_*` y usando `PU_*† = λ̄_*P` sale `PJ(q)Pv_*=c_0v_*`. **No introduce** Rellich, ni elección continua de autovectores, ni diferenciabilidad multivariable, ni pureza cónica del cúmulo, ni separación espectral adicional. *Asumido*: la existencia del cono (admisión). *Demostrado*: que su pendiente es autovalor de `PJP\|_{Ran P}`. |
| **F** Límite asintótico | **CORRECTO** | `S_{n+m}⊆S_n+S_m` por convolución (si `x∉S_n+S_m` todos los sumandos se anulan) ⟹ `H_n` subaditiva. `‖x‖≤n` en `S_n` ⟹ `−n‖q‖≤H_n(q)≤n‖q‖` ⟹ el ínfimo de Fekete es **finito**; el argumento `n=am+r` con `H_0=0` es correcto y da `lim = inf`. Coincide con el limsup de `CAUSAL_BODY_GEOMETRY.md` §6. Lipschitz: `\|H_n(q)−H_n(q')\| ≤ n‖q−q'‖` ⟹ `H_n/n` y su límite `h_∞` son 1-Lipschitz ⟹ mínimo alcanzado en la esfera compacta. **Positividad no supuesta**: `c_strict^iso > 0` es *consecuencia* del teorema para símbolos admitidos, no premisa. (Nota adicional verificada: `h_∞` es sublineal, luego sí es función soporte de un cuerpo convexo `C_∞^strict`, de modo que la conclusión equivale a `B(c_0) ⊆ C_∞^strict` — pero esto se **deriva**, no se presupone.) |
| **G** Alcance | **CORRECTO; sin hipótesis añadidas tras congelar el contrato** | La prueba usa *menos* que el contrato: no usa covariancia D2 ni la representación `R`, ni `T_h≠0`, ni ausencia de modo on-site, ni `s≥2`, ni `r≥2`, ni irreducibilidad, ni minimalidad, ni no-nilpotencia de vértices, ni la pendiente `−c_0`. Es uniforme en `s` y `R`, como el contrato permite explícitamente. `s` y `R` quedan fijos pero arbitrarios; degeneraciones (`r` cualquiera, incl. `r=s`) y espectadores quedan cubiertos; el soporte usado es el del **símbolo completo**, tal como exige el contrato. Limitación metodológica real, no un defecto bajo el contrato: la reducción a polinomio usa la **conmensurabilidad** de `N_3` (ver O4). |

## Objeciones, por gravedad

**O1 — Control de signo degenerado (laguna de verificación, no del argumento).**
*Lectura más fuerte:* §7 fila «Wrong Fourier sign» pretende validar la convención con el desplazamiento escalar `U(k)=e^{-ik·h}`.
*Por qué falla como control:* en ese ejemplo `S_n={nh}`, luego `a=b`, `D=0` y `B=0`. El control verifica únicamente el término `aI` de `J_n = aI + B` y es **vacío respecto del signo y la normalización del término derivada** `F(1)†F'(1)`, que es precisamente donde un error de regla de la cadena (`z=e^{-it}`, `dz/dt=−i`) produciría `aI − B`.
*Qué lo resolvería / reparación mínima:* un control con `D≠0`. Ejecutado a mano en esta revisión: `U(t)=e^{-it}P_+ + e^{it}P_-` da `a=−1`, `L(z)=zP_+ + z^{-1}P_-`, `F(z)=z²P_+ + P_-`, `F(1)=I`, `F'(1)=2P_+`, luego `J_1 = −I + 2P_+ = P_+ − P_-`; el cálculo directo `J = i·I·(−iP_+ + iP_-)` da lo mismo. **El signo del informe es correcto.**
*Clasificación:* aclaración expositiva / control incompleto. No afecta al veredicto.

**O2 — Identidad `J_n(q)=aI+F(1)†F'(1)` asertada sin derivación (expositiva).**
§3 pasa de «`U(tq)^n=L(e^{-it})`, `F(z)=z^{-a}L(z)`» directamente al resultado. Todo el edificio de signos descansa en ese paso. *Reparación mínima:* insertar la línea `U(tq)^n = e^{-iat}F(e^{-it})`, `d/dt|_{t=0} = −i(aF(1)+F'(1))`, `J_n = iF(1)†·(−i)(aF(1)+F'(1)) = aI+B`. Verificado correcto; conserva el contrato.

**O3 — Dos pasos del lema asertados sin cuenta (expositiva).**
`B†=B` y `g'(1)=2⟨v,Bv⟩` se enuncian sin cálculo. Ambos verificados aquí por coeficientes. Además, el esbozo del principio del máximo no separa explícitamente el caso «`p` constante» del caso «máximo interior con valor no nulo»; la frase siguiente («unless it is constant») lo cubre. Sin consecuencia.

**O4 — Dependencia no señalada de la conmensurabilidad del vecindario (alcance, no defecto).**
El paso a polinomio requiere `q·x ∈ Z` para un conjunto denso de `q`, lo cual usa `N_3 ⊆ (1/√3)Z³`. Para un `N` finito **no conmensurable** (p. ej. desplazamientos con emparejamientos racionalmente independientes) el conjunto de `q` con emparejamientos enteros puede reducirse a `{0}` y la densidad falla; `U(tq)^n` es entonces casi-periódica, no Laurent. El contrato fija `N_3`, así que **la prueba es válida tal como está**. *Obligación:* no citar (1) como «para todo QCA de rango finito» sin rehacer ese paso (es plausible hacerlo pasando al `p`-toro generado por `S_1`, pero eso no está hecho aquí ni autorizado).

**O5 — Límites interpretativos que deben permanecer explícitos (no es un defecto; el informe los reconoce).**
(a) `c_strict^iso` es del **símbolo completo**: en un símbolo reducible un bloque espectador rápido *infla* el miembro derecho, de modo que (1) **no** dice que el cono seleccionado quepa en el cuerpo de propagación del sector seleccionado. (b) «Estricto» es soporte exacto: no hay enunciado balístico, esencial ni Lieb-Robinson; las amplitudes pueden decaer exponencialmente. (c) `0<c_0` en (1) es hipótesis de admisión, no resultado.

**O6 — Fuente externa no verificada por el revisor (gobernanza).**
No se consultó Cedzich–Joye–A. H. Werner–R. F. Werner (modo sólo lectura; sin búsquedas externas). La cita **no es portante**: la prueba es autocontenida y no invoca ningún teorema externo. Esta revisión **no es** una auditoría de prior art: `NOVELTY` debe seguir `OPEN`.

## Reparaciones obligatorias

**Ninguna.** No se encontró defecto fatal ni laguna reparable que afecte a la validez bajo el contrato congelado. Las reparaciones de O1–O3 son mejoras de exposición/verificación recomendadas, no condiciones de aceptación; ninguna altera un cuantificador del contrato.

## Hipótesis efectivamente utilizadas

Usadas:

1. `U(k)` unitaria para **todo** `k` real (identidad exacta, no malla).
2. Soporte de Fourier finito contenido en `(1/√3)Z³` (finitud + conmensurabilidad). Para la última desigualdad de (1), además `S_n ⊆ n·conv(N_3)`.
3. Para cada `q` unitario, existencia de una sucesión `t_j↓0` y autovalores `λ(t_j)` de `U(t_jq)` con `λ(t_j)=λ_*e^{-i(t_jc_0+o(t_j))}`.
4. `c_0` independiente de la dirección (isotropía del cono seleccionado).
5. `P` = proyector espectral de `U(0)` en `λ_*` (normalidad ⟹ conmutación).
6. Dimensión interna finita `s` (compacidad de la esfera unidad).

No usadas: covariancia D2 / representación `R`; `T_h≠0`; ausencia de modo on-site; `s≥2`; `r≥2`; irreducibilidad, minimalidad o P17 Eq. (2); no-nilpotencia de vértices; la pendiente `−c_0`; L1; identidad métrica; cualquier hipótesis de brecha espectral, analiticidad multivariable o base propia continua.

## Qué puede registrarse legítimamente en `CURRENT_STATE.md` y qué debe seguir abierto

**Registrable** (contenido; el registro material es decisión del usuario — esta revisión no modifica `CURRENT_STATE.md`):

- `c_0 <= c_strict^iso` queda **demostrado bajo el contrato congelado `4135625`**, con una revisión adversarial independiente que no halló defecto fatal ni laguna reparable y **sin reparaciones obligatorias**. Nivel de evidencia propuesto: `PROOF_COMPLETE_ONE_INDEPENDENT_ADVERSARIAL_REVIEW_PASS`. No se propone `ESTABLISHED` por decisión propia: `PROJECT_INSTRUCTIONS` §4 lo permitiría («proved in-repo»), pero la norma de ratificación de cinco miembros sigue incumplida y una revisión no es un Sanedrín.
- Resultados **más fuertes** que (1), realmente demostrados y que conviene registrar: (i) la cota vale a todo tiempo finito, `c_0 ≤ H_n(q)/n` para todo `n≥1` y todo `q`; (ii) **toda** pendiente direccional que emerge del nodo está en `[−h_∞(−q), h_∞(q)]`, no sólo `±c_0`; (iii) equivalentemente `B(c_0) ⊆ C_∞^strict`; (iv) todo símbolo admitido tiene `c_strict^iso > 0`.
- Las **hipótesis efectivamente usadas** (lista anterior), para que ninguna puerta futura suponga que D2, `T_h≠0` o `r≥2` son necesarias.
- La fila 1 de «Research directions» §7.2 («`c_0 <= c_strict^iso` tiene prueba preliminar; revisión pendiente») puede actualizarse a «revisión adversarial realizada, PASS».

**Debe seguir abierto / sin cambio:**

- `NOVELTY = OPEN` (no se hizo auditoría de prior art; la cita de §8 no está verificada aquí).
- Ratificación de cinco miembros: sigue `ABORTED_OR_INCOMPLETE`. Esta revisión **no** la sustituye ni ratifica `C` completo.
- Strong `B_infty^*`: sigue `REJECTED` en la clase s=4; el mecanismo que seleccionaría la igualdad sigue abierto. El techo **no** implica igualdad, saturación, universalidad entre especies ni frente balístico.
- Versión **intrínseca al sector** del techo: abierta (O5a). Versión con frente balístico/amplitudes: abierta (O5b).
- Saturación (ii), `c_strict^iso = ρ_micro`: abierta.
- Extensión a vecindarios no conmensurables: no demostrada por este método (O4).
- L1, identidad métrica-defecto y el gate C completo: no autorizados, sin cambio. `main` y las ramas congeladas, fuera de alcance.

## Ataques que la prueba superó

Grado exacto / invertibilidad / conmutatividad en el lema; `D=0` y `F(0)` singular; signo del término derivada (verificado con control no degenerado propio); cancelación de los extremos al agrupar sobre la recta; exponentes no enteros; intercambio `min_q ↔ lim_n` (no existe: (3) es a `n` fijo); colisiones de fase Floquet en `U_*^n` (verificado contra `W^4=−I` del control s=4); ausencia de brecha espectral y de denominadores; `P=I`; espectadores y ramas no cónicas en `Ran P`; introducción subrepticia de Rellich, autovectores continuos o diferenciabilidad multivariable (ninguna); circularidad por presuponer `B(c_0) ⊆ C_∞^strict` (no la hay: `v_*∈Ran P` se deriva); Fekete con `H_n` posiblemente negativo (acotado por `−n‖q‖`); positividad encubierta de `c_strict^iso` (es consecuencia); caso degenerado `U(k)^n ≡ const` (fuerza `c_0=0` por continuidad de autovalores en el toro conexo — consistente); y dos contrastes cuantitativos independientes: Pavia (igualdad saturada) y s=4, donde se calculó a mano `P_+ J(ê_x) P_+ = (a/√3)σ_x P_+`, cuyos autovalores `±a/√3` son exactamente `±c_0`, confirmando (6) en un caso con fase Floquet no nula, `P` de rango 2 y colisión de potencias.

Ausencia de objeciones fatales aquí significa que **un** revisor adversarial no rompió la prueba en los siete frentes exigidos; no equivale a revisión exhaustiva ni a certificación independiente múltiple.
