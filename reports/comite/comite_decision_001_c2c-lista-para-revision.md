# Comité Decision 001 — c2c-lista-para-revision

> Produced by `/comite` (shared engine, `~/herramientas/skills/comite`). The committee PROPOSES;
> the user AUTHORISES. The committee never executes a committing or outward-facing action, never
> loosens a frozen rule post-hoc, and never claims beyond the evidence.
> Guardrails: NO_UNQUALIFIED_VMAX, NO_EVIDENCE_PROMOTION, NO_RIGIDITY_FROM_FINITE_SCAN,
> NO_UNCHARTERED_GATE, NO_SCOPE_BROADENING, NO_NOVELTY_WITHOUT_PRIOR_ART, KEEP_QUANTIFIERS
> (`comite/config.toml`).

## 1. Decision question
La ejecución C2c (`reports/2026-09-22--c2c-structural-scope.md`, estado PROOF_WRITTEN /
REVIEW_PENDING, sin versionar) ¿está en condiciones de pasar a revisión independiente tal como
está? Si lo está: ¿con qué alcance, qué revisor y qué criterios deben congelarse antes de la
revisión? Si no: ¿qué debe repararse, versionarse o congelarse antes?

## 2. Verified state
Facts checked **this session**, each with its command / file:line. Anything unchecked is marked
`[UNVERIFIED]`.
- HEAD `f4f937e102def05f8797a94e256a460d81b0cc33` ("Promote C2b PASS and open C2c
  structural-scope gate"), rama `research/b-infinity-post-s4-gate` (`git log --oneline -3`,
  `git rev-parse HEAD`, `git branch --show-current`; reconfirmado por el verificador de literatura).
- `git status --short`: sin versionar `reports/2026-09-22--c2c-structural-scope.md`,
  `reports/2026-09-22--front-resource-scaling.md`, `reports/2026-09-22--fr1-power-hypotheses.md`,
  `reports/2026-09-22--liu-chen-full-reading.md`, `reports/2026-09-21--roadmap-corona-causal-uv-ir.md`,
  `comite/`. Nada en el índice.
- `wc -l`: la nota C2c tiene 736 líneas; el contrato `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md`, 173.
- `sha256sum reports/2026-09-22--c2c-structural-scope.md` =
  `f6266e951d3f5ffed20aef9ef8a75fe189f56b90df2b2f2e9af0abf11d407fb5` (analista numérico;
  reproducido por el verificador de literatura y el guardián).
- Contrato C2c, versionado en `f4f937e`: estado UNBLOCKED / NOT_EXECUTED; obligaciones S1–S5;
  salidas `C2C_PASS` (alcance delimitado), `C2C_REPAIR_REQUIRED`, `C2C_FAIL`, `C2C_INCOMPLETE`
  (lectura del presidente de las líneas 1–173).
- Nota C2c §1, §10, §11, §12: autor "Codex, agente /root"; estado PROOF_WRITTEN / REVIEW_PENDING;
  §12 añadido después de la derivación (lectura del presidente de las líneas 1–60 y 652–736).
- `state/CURRENT_STATE.md` §10.1 (líneas 1582–1700): C1 PASS; C2a PASS (σ2/I); C2b PASS (σ2/I,
  POST-DISCOVERY, autor Claude Opus 5, revisor Codex /root); C2c UNBLOCKED / NOT_EXECUTED.
- Auditoría previa: no aplica. El repo no tiene `/auditor`.

## 3. Dossier
Files and references the chair supplied to the committee:
- `reports/2026-09-22--c2c-structural-scope.md` (objeto de la decisión)
- `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md`, `theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md`,
  `theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md`, `theory/IR_C2B_BLOCK_DECOMPOSITION_GATE.md`
- `reports/2026-09-22--c2a-oscillatory-transfer.md`, `reports/2026-09-22--c2a-independent-review.md`,
  `reports/2026-09-22--c2b-independent-review.md`
- `papers/ir-corona/ir-corona.md`, `formal/README.md`, `scripts/README.md`
- `state/CURRENT_STATE.md` (§10.1), `PROJECT_INSTRUCTIONS.md`
- Contexto y anclas del comité: `comite/contexto.md`, `comite/roles/*.md`

## 4. Expert briefs (wave 1 — blind, parallel)
### Matemático (análisis asintótico y geometría convexa)

**Veredicto.** No encontré ningún error bloqueante en la parte que se puede comprobar a mano. La nota C2c está lista para una revisión independiente una vez versionada tal cual. El alcance de esa revisión debe limitarse a dos cosas: (i) el criterio abstracto (C1) como teorema condicional y (ii) las 15 filas nuevas del protocolo congelado. El paso que menos está escrito, y por tanto el que más necesita revisión, es la adaptación de §5.2, que se argumenta con texto y no se vuelve a derivar.

- **Objetos matemáticos:**
  - Enunciado abstracto (`reports/2026-09-22--c2c-structural-scope.md:97-122`):
    - H_N es un espacio de Hilbert, con ‖φ_N‖=1 y V_N, U_N unitarios.
    - P_N es un proyector ortogonal con P_Nφ_N=φ_N, y Q=I−P.
    - El detector cumple 0≤E≤I y E=B E B.
    - La constante de propagación es T_N=‖B V A‖. Coincide con la del Teorema 4.1 (`papers/ir-corona/ir-corona.md:513-518`).
  - Protocolo: pesos de Alice y de Bob.
    - El peso de Bob es h_N=(1−16|y−Nu|²/N²)_+² (`ir-corona.md:426`). Es C¹, estrictamente positivo en el interior y se anula junto con su gradiente en la frontera. Es C¹ y no C^∞, a pesar de que en `ir-corona.md:134` se le llame "smooth bump".
    - Se usan b=1/4, K=√N y γ=√3−3/2.
  - Protocolo: fuentes.
    - Las fuentes son Â_M=ĉχ+iŝMχ (`reports/2026-09-22--c2-projected-response-representation.md:137-162`).
    - Da ζ_M∈{↓,↑,−i↑,−↓}; lo comprobé.
  - Protocolo: bandas y detector.
    - Los proyectores de banda son Π_σ(n)=(I+σJ(n))/2, con J(n)=n₁σ₁−n₂σ₂+n₃σ₃. Son distintos del corte P.
    - El detector es D∈{I,(I+σ_j)/2}; en los casos de rango uno, D^{1/2}=D.

- **Estado de cada afirmación:**
  - **(C3), constantes: comprobado a mano.**
    - L_PP=2Re c+𝒬 se obtiene de P(φ+a)=φ+Pa.
    - ρ_N=⟨d,Ed⟩−2Re⟨d_P,Ed⟩, luego |ρ|≤4T²+8T.
    - η=⟨d,E(r+d_P)⟩, luego |η|≤2T·3=6T.
    - Coinciden con la revisión de C2b (`reports/2026-09-22--c2b-independent-review.md:293,299-307`).
    - ‖E^{1/2}d‖≤2T_N se sigue de E^{1/2}=BE^{1/2}B y de a=Aa.
  - **(C1): probado, y es trivial una vez dada (C3).**
    - La suma de coherencias es −Lin−2𝒬+2Re η, y T²≤T porque T≤1.
    - Es sólo condición suficiente, y la nota lo declara (l.40).
  - **Contraejemplo de §4 (l.214-226): comprobado.**
    - Da a=−√2e₁, d_P=−φ, d_Q=(−e₁+e₂)/√2, 𝒬=1/2, c=−1/2, y bloques (−1/2, 1/2, 0).
    - Refuta de forma válida "A/B ⇒ patrón".
  - **(C9)–(C11), factor 64: correcto.**
    - Sale de 16²·½ =128 y de ½ al pasar el coseno a exponenciales.
    - Luego (C15) da 64·(4+4)=512.
    - Las frecuencias {0,1/2,3/2,2,5/2} son correctas para α∈{±5/4,±3/4}.
  - **(C12): correcto.**
    - Coincide con C2a (`reports/2026-09-22--c2a-oscillatory-transfer.md:230-260`, con B=β).
    - C₀>C₁>0 porque t₊≠t₋>0.
  - **§7, definitud positiva: probada.**
    - La nulidad en L² más la continuidad de √h·(racional) en el interior da nulidad puntual.
    - El segmento radial en la dirección n₀=u/√3 es el diámetro de Bob, donde h>0.
    - Los cuatro polos simples −α_i son distintos, así que la descomposición en fracciones parciales da a_i v_{σ(i)}=0.
    - (C14): la dirección de Bloch de J(n₀) es m₀=(1,−1,1)/√3, luego ‖DΠ_σζ‖²=¼(1+σs/√3)(1+σ(m₀)_j)>0. Lo comprobé, también para D₃ con ↓.
    - Por tanto G^{M,D}>0 y la cota inferior vale para todo K real.
  - **(C6)/(C7), §5.2–5.3: derivable pero no redemostrado.**
    - Todas las cotas de C2a que se importan son de norma: (16), (17)–(20), (21)–(23) y el lema angular (6) con g∈C⁶ (`c2a-oscillatory-transfer.md:103-112,296-400`).
    - Insertar un D constante con ‖D‖≤1, o cambiar ζ, no altera esas cotas.
    - La cota compleja proviene de C2b §8 (`c2b-independent-review.md:372-432`).
    - Clasificación: plausible, **no reverificado lema a lema** [UNVERIFIED en la nota].
  - **Hipótesis oculta:** Θ(N^{-3}) y (C16) valen sólo para N≥N₀, y N₀ no es explícito. Lo que vale "para todo N≥2" son únicamente (C3)/(C4) (l.178).

- **Invariantes y estructura:**
  - L_QP=conj(L_PQ) de forma exacta.
  - G^{M,D} es invariante bajo cambios de fase global de ζ_M. De ahí salen las ocho familias ({σ₁,σ₂} con ↑ y {I,σ₃} con ↓, por cuatro detectores; l.526-531), lo cual es correcto.
  - Frecuencias: con D=I, Π₊Π₋=0 deja sólo 0 y 1/2. Con detectores de rango uno pueden aparecer 3/2, 2 y 5/2.
  - Separación de denominadores: todos son ≥γ.

- **Límite o referencia de continuo:**
  - Para σ₂/I, (C12) debe reproducir exactamente 𝒞₀+𝒞₁cos(√N/2) de C2a (`c2a-oscillatory-transfer.md:25-38`). Lo hace.
  - Para D=I y M arbitrario debe salir la misma forma, cambiando sólo ν_σ.
  - La escala de referencia es K^{-6}=N^{-3}, con resto K^{-13/2}.

- **Comprobaciones específicas del proyecto:**
  1. **Uniformidad de los errores:**
     - Los errores son uniformes en la familia finita y en Bob.
     - La ganancia relativa sigue siendo sólo N^{-1/4}: O(N^{-13/4})/N^{-3}. Es la misma debilidad que la salvedad de C2a.
     - Con detectores de rango uno, λ_{M,D} puede ser bastante menor. Por ejemplo, en n₀ el factor de (C14) llega a ≈0.045 [indicativo, no es λ].
     - En consecuencia, el umbral efectivo podría ser aún más tardío que γ√N≈1.1 a N=24.
  2. **Cota inferior:**
     - (C15) es uniforme en K para la parte principal.
     - La positividad de 𝒬_N es sólo asintótica (N≥N₀ no explícito).
  3. **Identidad de una familia usada como ley general:** no ocurre. La nota rechaza expresamente extender el resultado a otros detectores (l.506-507) y a otras geometrías (§9.3).
  4. **Hipótesis operativas explícitas:** sí, y usadas donde se dice (tabla §3.2). La única salvedad es que la adaptación de §5.2 se afirma sin escribirla.

- **Salvedades y recomendación:**
  - **Antes de la revisión:**
    - Versionar la nota tal cual, con commit y SHA256.
    - Marcar el §12 (Liu–Chen) como addendum no científico, fuera del alcance revisado, o separarlo. No afecta a ninguna prueba (l.733-734).
  - **Revisor:** debe ser distinto de Codex `/root`, que es el autor aquí (l.3) y también fue el revisor de C2b (`theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:23-25`).
  - **Criterios a congelar antes de la revisión:**
    - (a) Veredicto por fila y por nivel de S3 (`theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:90-96`). Se admite un PASS parcial, por ejemplo A/B/patrón en PASS y coeficiente en REPAIR.
    - (b) Nueva derivación, lema por lema, de §5.2 con test hDR_N y espinor ζ_M: lema angular (6), cancelación (17), cola (18), resto (19), Poisson (23).
    - (c) Nueva comprobación de (C8)–(C11), incluidos todos los cruces Π₊DΠ₋, del factor 64/512 y de la prueba de §7.
    - (d) Declarar que (C2)/(C16) son eventuales, con N₀ no explícito, y ganancia relativa N^{-1/4}.
    - (e) (C1) se acepta sólo como teorema condicional; no se acepta como verificación en ningún otro modelo (KEEP_QUANTIFIERS, NO_SCOPE_BROADENING).
  - **Nivel de evidencia:** un C2C_PASS eventual sólo cubre los 16 pares originales del walk CJWW (5.15) y el nodo cero. No convierte en teorema nada de lo marcado OPEN (NO_EVIDENCE_PROMOTION).

### Físico (QCA y límite relativista IR)

**Veredicto desde la física:** el contenido físico de C2c está listo para una revisión independiente. El techo de interpretación de §9.4 es correcto y no encuentro ninguna afirmación física no autorizada. Aun así, no debe pasar a revisión **tal como está**, por tres motivos formales:
1. La nota no está versionada (dossier: sin versionar, sin SHA).
2. El addendum §12 es posterior al snapshot de entrada y está mezclado en el mismo artefacto.
3. Los criterios físicos de alcance, listados abajo, no están congelados.

Primero hay que reparar y congelar eso. Después, la revisión debe cubrir los cinco puntos de §10 y el argumento de §9.2.

- **Magnitudes físicas en juego:**
  - Todo está en unidades de red adimensionales: un paso de red (a) y un paso temporal (τ) valen 1, y c_IR = 1 (`papers/ir-corona/ir-corona.md:112`).
  - Y = y/N es la posición reescalada: Bob es la bola de centro u = (1,1,1) (|u| = √3) y radio b = 1/4; Alice es la bola de radio 1/4 en el origen (`ir-corona.md:125-130`, `:426`).
  - k = pN es el momento reescalado. El corte duro |p| ≤ N^{-1/2} equivale a K = √N en k. Está entre el ancho del recurso Λ = 1/N (`ir-corona.md:130`) y la escala de red.
  - ρ = |Y|. Los denominadores ρ + σ + εb (`c2c:263-270`) miden la distancia al frente del cono IR (ρ = 1) desde el borde de Alice. γ = √3 − 3/2 ≈ 0.23 es el margen de Bob fuera de ese cono, coherente con `ir-corona.md:383`.
  - Q_N, L_XY y Lin_N son contribuciones firmadas y adimensionales a un observable de Bob (`theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md`, objetos congelados). No son probabilidades ni flujos.
  - En ningún momento se restaura la escala física (a, Δt). Es correcto que sea así: el gate §8.21 está `NOT_EXECUTED` (`state/CURRENT_STATE.md:1368`).

- **Régimen y límites:**
  - Walk CJWW (5.15) homogéneo, nodo cero, Weyl sin masa, N entero → ∞, corte duro de Fourier fijo, perfiles y regiones originales.
  - El exponente 3 sale de K^{-6} con K = √N (`c2c:627`). Por tanto es un exponente **del protocolo de corte**, no de la dinámica: con otro exponente de corte cambiaría. La nota lo reconoce en §9.3 (`c2c:618-638`).
  - Fuera de los dieciséis pares, o con otro corte, perfil, geometría, dimensión o QCA, sólo queda el criterio condicional (C1), sin verificación de sus hipótesis.
  - El régimen asintótico llega despacio (γ√N ≈ 1.1 a N = 24; `CURRENT_STATE.md` §10.1, caveat 2). Con detectores de rango uno el autovalor mínimo λ_{M,D} de G no está evaluado (`c2c:493-507`, "constantes numéricas… abierto" en §11). El umbral efectivo de N podría ser todavía mayor [UNVERIFIED, no calculado por diseño].

- **Significado físico de la señal:**
  - (C5) es la cola de Gibbs del corte duro. La emite el borde de Alice (el perfil se anula cuadráticamente, de ahí la cola k^{-4}), se propaga a c_IR = 1 por el continuo de Weyl y llega a Bob fuera del cono con amplitud K^{-3}.
  - Los bloques PP y QQ llevan cada uno +Θ(N^{-3}) y las coherencias −2Θ(N^{-3}). La suma total sigue exponencialmente pequeña por el Teorema 4.1 (`ir-corona.md:513-517`).
  - Esto mide la **no localidad del proyector espectral** (§9.2, `c2c:600-616`: Pa no tiene soporte finito). No mide transporte físico por un sector ni señalización.
  - Por eso el patrón +1:+1:−2 describe una contabilidad espectral de un observable local. No dice nada sobre la velocidad IR, sobre C_micro, V_causal^max o V_grp^max, ni sobre c_0 frente a c_strict^iso.
  - Comprobé a mano, por mi cuenta, varios pasos que tocan la física:
    - el vector de Bloch m_0 = (1,−1,1)/√3 de J(n_0) y la positividad de (C14), que se cumple porque |(m_0)_j| = 1/√3 < 1;
    - el factor 256·½ = 128 = 64·2 en (C9) y (C11);
    - la cota 512β²λ de (C15) a partir de ‖z‖² = 4.

    Todo es consistente. No sustituye a la revisión independiente.

- **Límite de la afirmación:**
  - **Afirma, pendiente de revisión:**
    - para los dieciséis pares congelados, las expansiones de bloques (C16), con un coeficiente cuasi-periódico en √N acotado inferiormente de forma uniforme;
    - un criterio condicional abstracto (C1);
    - la refutación algebraica de "A/B bastan" (`c2c:212-228`).
  - **No afirma:**
    - que N^{-3} sea una ley física;
    - ningún origen UV ni IR exclusivo (`c2c:649`);
    - que P o Q sean preparaciones físicas locales;
    - ninguna predicción dimensional ni de laboratorio (§8.21 NOT_EXECUTED);
    - nada sobre C3, E/AdS, otras clases de QCA, ni novedad frente a Bernstein o Liu–Chen.
  - La tabla §8 con "D" no es promoción. Sólo σ2/I conserva su PASS (`c2c:703-705`).

- **Comprobaciones propias del proyecto:**
  1. **Qué se compara:** no se compara ninguna velocidad. Se comparan bloques espectrales de la respuesta de un detector local fuera del cono IR (c_IR = 1), en el límite de N grande con corte duro K = √N y Weyl sin masa. No aparece ningún v_max sin cualificar: la única mención es "velocidad emergente" como hipótesis no requerida (`c2c:207`).
  2. **Masa:** no aplica. Nodo cero, Weyl sin masa. No se usa |∇ω(0)| con masa, ni hace falta c_H o c_{ω²}.
  3. **Escala física:** no se restaura. Todo es adimensional y la geometría es fija. Correcto.
  4. **Régimen de laboratorio o física real:** no se dice nada sobre él, y §9.4 lo excluye expresamente. Conforme con §8.21.

- **Qué hacer antes de la revisión (físico):**
  - Versionar la nota en un commit propio y registrar su SHA256 como snapshot de revisión.
  - Separar el §12, o declararlo expresamente fuera del alcance de la revisión: es posterior al snapshot `f4f937e` (`c2c:720-736`).
  - Congelar por escrito estos criterios:
    - (a) el exponente 3 y las frecuencias {0, ½, 3/2, 2, 5/2} se aceptan sólo como propiedades del protocolo de corte en los dieciséis pares;
    - (b) cualquier PASS arrastra los caveats 1–3 de C2a a los quince pares nuevos (ganancia N^{-1/4}, asintótica lenta, una sola revisión de agente);
    - (c) el argumento §9.2 de colas no locales entra en el alcance, aunque §11 no lo incluye entre los ítems 1–4;
    - (d) el revisor no puede ser Codex `/root`, autor de C2c (`c2c:3`). Hay que registrar que Claude Opus 5 certificó los lemas de C2a que §5 adapta (`reports/2026-09-22--c2a-independent-review.md:8`). Eso no es autoría de C2c, pero conviene declararlo.
  - El veredicto posible queda en `C2C_PASS` con alcance "dieciséis pares originales y criterio condicional". O bien REPAIR, FAIL o INCOMPLETE, sin forzar ninguno.

- **Caveats:**
  - El alcance de la transferencia en §5.2 se justifica por "mismas cotas, D constante de norma ≤ 1" (`c2c:281-316`). Ahí está el riesgo físico-técnico principal: el test hDR_N con D de rango uno no conmuta con los proyectores de banda de Weyl. La uniformidad hay que comprobarla lema a lema. [UNVERIFIED por mí]
  - La cota inferior (C15) es asintótica y no numérica. No dice a partir de qué N el patrón es visible; los datos N = 24/40 siguen excluidos (contrato, "Método").
  - Normalizaciones de c: el contexto cita c_0 = 1/√3 para la familia estándar s = 2, mientras que el manuscrito de la corona usa c_IR = 1 (`ir-corona.md:112`). Ninguna conclusión de C2c depende de esa identificación. No hay que mezclarlas en ningún resumen.
  - La física del resultado es la de un artefacto espectral de un proyector no local. Cualquier redacción posterior que lo presente como "señal IR" o "transporte" violaría §9.4 y NO_EVIDENCE_PROMOTION.

### Lógico formal (cuantificadores y Lean)

- **Estado formal:**
  - Definiciones: los objetos abstractos de §3.1 (`reports/2026-09-22--c2c-structural-scope.md:97-122`), la matriz de Gram (C8) (`:352-357`) y 𝒜_{M,D} (C9)/(C11) (`:387-409`). Coinciden con los objetos del contrato (`theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:44-60`).
  - Teoremas en papel, no revisados:
    - (C3): comprobé a mano las constantes 8T+4T² y 6T a partir de ‖E^{1/2}d_P‖≤2, ‖E^{1/2}r‖≤1 y ‖E^{1/2}d‖≤2T. También comprobé que L_PQ = −c̄ − 𝒬 + η, con el producto interno antilineal en la primera entrada. Son correctas.
    - (C1): es una implicación condicional. Presupone que 𝒬_N>0 a partir de cierto N (`:38`).
    - El contraejemplo en ℂ² (`:212-228`): comprobé a=−√2e₁, d_P=−φ, T=0, 𝒬=1/2, c=−1/2 y (−1/2, 1/2, 0). Es correcto.
    - (C11)/(C15): comprobé el factor 64 (256·½·½) y que 512β²λ sale de ‖z‖²=4 y de sumar dos términos. Son correctos.
    - Definitud positiva (§7): el argumento de polos simples distintos α∈{±5/4, ±3/4} es lógicamente válido, siempre que (C14) sea cierta. Con m₀=(1,−1,1)/√3 da factores (1±1/√3)/2>0. La bola de Bob tiene centro u y radio 1/4 (`papers/ir-corona/ir-corona.md:426`), así que el segmento radial por n₀ es un diámetro interior con h>0.
  - Delegado sin reprobar: la transferencia de §5 (C5)–(C7). Se afirma por referencia («la justificación del resto es la ya escrita», `:272`) a unos lemas de C2a revisados sólo para σ₂/I (`state/CURRENT_STATE.md:4`). Es el eslabón más débil y es exactamente lo que falta revisar.
  - Abierto: las constantes efectivas y el umbral N₀ (`:699-702`).

- **Orden de cuantificadores / dependencias:**
  - Ocurre de forma limpia: primero (M,D) de la lista congelada, luego G^{M,D} y λ_{M,D} (independientes de N), y después N→∞ con K=√N. La cota (C15) vale «para todo K real» (`:499`), así que no hay selección de fase ni de subsucesión.
  - Hay dos cuantificadores distintos que la revisión debe mantener separados:
    - (C4) vale ∀N≥2 con constantes explícitas (`:178`).
    - (C2)/(C16) son asintóticas, con N₀(M,D) no efectivo.
    - Por tanto, nada de (C16) se puede leer en N=24 o N=40. Esto es coherente con la salvedad de C2a γ√N≈1.1 [dossier].
  - Hay grados de libertad post-hoc:
    - El contrato se escribió conociendo ya el mecanismo de C2b, y lo admite (`IR_C2C…GATE.md:29-32`).
    - El informe objeto de revisión está sin versionar y recibió §12 después de la derivación (`:720-736`). El objeto que se revisaría no está fijado.
    - Los criterios de aceptación del revisor no están congelados más allá de las cuatro etiquetas (`IR_C2C…GATE.md:163-166`). No está definido cómo se expresa un PASS parcial, por ejemplo ítems 1–2 PASS e ítem 3 REPAIR.

- **Afirmaciones de equivalencia:**
  - (C1) se declara sólo suficiente (`:40`). Correcto.
  - La afirmación «Lin=o(𝒬) no es opcional» (`:212`) se queda corta. Dado que L_PP/𝒬 = 1 + Lin/𝒬 exactamente, la condición Lin=o(𝒬) es **necesaria y suficiente** para la componente PP del patrón. En cambio, T=o(𝒬) no es necesaria. Conviene enunciarlo así en lugar de apoyarse sólo en el contraejemplo.
  - La frase «se agrupan en ocho familias» (`:527`) sólo está probada en un sentido: igual ζζ† implica igual coeficiente líder. No se prueba que las ocho sean distintas, así que debe decir «a lo sumo ocho».
  - «Para σ₂/I son exactamente 𝒞₀, 𝒞₁» (`:436-437`) es una igualdad con las constantes de C2a que se afirma sin mostrar la comparación de normalizaciones. Es un punto a verificar.
  - L_PQ y L_QP: el informe separa bien la conjugación exacta de las expansiones separadas (`:570-571`).
  - «Refutado» (`:695`) refuta la implicación abstracta, no algo dentro del protocolo. Está bien delimitado.

- **Disciplina de tipos / objetos:**
  - No encontré errores de categoría. Hay colisiones de notación que un revisor debe desambiguar:
    - J (la constante de tasa, `:174`) frente a J(n) (la matriz de bandas, `:267`).
    - D (el detector) frente a D^W_{M,K} y D_{M,N} (campos) en la misma fórmula (C7) (`:333`).
    - Q (el proyector) frente a 𝒬_N.
    - ρ (el radio) frente a ρ_N (un resto); se aclara en `:156`.
    - A_N^{sp}, A_M y 𝒜_{M,D}.
    - R_N (el recurso) frente a R_N^{blocks} de C2a.
  - Los Π_σ (bandas de Weyl) se distinguen explícitamente de P (`:268-269`). Correcto.

- **Comprobaciones propias del proyecto:**
  1. **¿Todos los pares o sólo los declarados?** El resultado cuantitativo cubre sólo los 16 pares congelados. La no anulación (C14) se verifica sólo para la lista (`:506-507`). §9.1 dice «cualquier secuencia», pero de forma condicional y sin verificación en otros modelos (`:593-595`). Es aceptable.
  2. **¿Suficiente presentado como necesario u óptimo?** No, y el informe es explícito (`:40`). El matiz de necesidad de Lin=o(𝒬) está arriba.
  3. **¿Qué está en Lean y qué sólo en papel?** Lean sólo cubre `TN_bound`, T_N ≤ 4N⁴e^{−JN} (`formal/README.md`, tabla). Es más fuerte que el 9N⁴ que usa (C4), así que son compatibles. Todo lo demás de C2c es sólo papel: (C3), (C1), la transferencia, Gram y la definitud positiva. `delta_le_four_T` trata del observable total, no de los bloques. La revisión no debe citar Lean más allá de la tasa de T_N.
  4. **¿Implicaciones tratadas como equivalencias?** Sí, en «ocho familias» y en la identidad con 𝒞₀/𝒞₁. En la dirección contraria, (C1) PP se infravende como no bicondicional.

- **Salvedades:**
  - **Veredicto lógico: todavía no está listo para la revisión tal como está.** No encontré ningún error en los pasos que recomprobé. El bloqueo es de freeze: antes hay que (a) versionar la nota o registrar su SHA256; (b) separar o excluir expresamente §12 del objeto revisado (`:720-736`); y (c) congelar por escrito:
    - el alcance: ítems 1–4 de §11, sólo los 16 pares y sólo asintótico;
    - una lista de comprobación: los puntos de `:675-679`, más la necesidad de Lin=o(𝒬), «a lo sumo ocho», la verificación de 𝒞₀/𝒞₁ y la tabla de notación;
    - una regla de veredicto por ítem, para un PASS con alcance delimitado.
  - El revisor no puede ser Codex `/root`, que es el autor (`:3`). Si el revisor fue autor del candidato C2b, del que C2c hereda las identidades, tendría un conflicto parcial. La elección concreta del revisor corresponde al guardián [UNVERIFIED en cuanto a norma escrita].
  - `state/CURRENT_STATE.md` §10.1 aún dice NOT_EXECUTED. La revisión debe citar la nota por hash, no por el estado del registro.
  - Los lemas de C2a que se importan fueron revisados una sola vez (`state/CURRENT_STATE.md:4`). La adaptación de §5 es la dependencia no verificada de mayor riesgo; por ahora es [UNVERIFIED].

### Analista numérico (cálculo exacto frente a diagnóstico)

**Veredicto del rol:** la nota está en condiciones de pasar a revisión independiente en el aspecto computacional, porque toda su evidencia es analítica. Antes hay que reparar la procedencia (provenance): versionar o sellar con hash la nota y separar el §12. Los puntos se detallan abajo.

- **Cálculo propuesto o del que depende:** ninguno. La nota declara que no hay cálculo numérico, simulación, barrido ni ajuste (`reports/2026-09-22--c2c-structural-scope.md:60-63`). También dice que las entradas de G no se evalúan numéricamente (`:359-360`) y que no ejecuta código científico (`:716`). El nivel D del contrato (`theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:141-145`) se cumple: no usa N=24/40 ni los scripts `scripts/ir_precision_N24.py` o `ir_cancellation.py`.
  - Las conclusiones descansan en cuatro tipos de trabajo analítico:
    - álgebra exacta: (C3) y (C4);
    - transferencia asintótica importada de C2a y comprobada para cada familia (§5);
    - álgebra de una matriz de Gram 4×4 (C8)–(C11);
    - un argumento de independencia de funciones racionales (C13)–(C14).
  - Rehice a mano la aritmética que la nota marca como prioritaria:
    - (16β)²·½ = 128β² en (C9).
    - z†Gz + z̄†Gz̄ = 2 Σ G_ij cos((α_j−α_i)K), así que el factor 64 de (C11) es correcto.
    - ‖z‖² = 4 da 64·8 = 512 en (C15).
    - Las frecuencias {0, 1/2, 3/2, 2, 5/2} salen de α ∈ {±5/4, ±3/4}.
    - Con D=I sólo quedan cos(K/2) = cos(2bK), lo que concuerda con C2a (`reports/2026-09-22--c2a-oscillatory-transfer.md:226-250`).
    - (C14): el vector de Bloch es m0 = (1,−1,1)/√3, y los factores (1 ± 1/√3)/2 > 0 son correctos.
    - Denominadores: ρ − 5/4 ≥ √3 − 3/2 = γ en la bola de Bob, de radio 1/4 (`papers/ir-corona/ir-corona.md:426`).
    - Presupuesto de errores: O(K^{-13/2}) de (C7) domina a O(K^{-7}) de (C10) y a |c| = O(K^{-7}) de (C6). Eso da O(N^{-13/4}) en (C16).
- **Control de errores:**
  - Las cotas son asintóticas sin constantes: O(·) y Θ(N^{-3}). La propia nota deja abiertas las "constantes numéricas y umbral efectivo de sus restos" (`:699-700`).
  - La única cota con constante explícita es T_N ≤ 9N⁴e^{-JN} (C4). El resto relativo gana sólo N^{-1/4}, igual que la salvedad 1 de C2a (`state/CURRENT_STATE.md:1654`), ahora en los dieciséis pares.
  - La cota inferior (C15) es cualitativa. λ_{M,D} > 0 se obtiene por independencia lineal, sin ningún valor.
  - Estimación propia, analítica y no calculada: G puede estar mal condicionada. Para σ=+1, las funciones 1/(ρ+5/4) y 1/(ρ+3/4) tienen el mismo espinor v_σ. Su cociente sólo varía entre ≈1.18 y ≈1.22 en ρ ∈ [√3−1/4, √3+1/4]. Además, con detectores de rango uno (C14) los pesos pueden bajar a ≈0.21·0.21 ≈ 0.045. En consecuencia λ_min puede ser pequeño y el N a partir del cual domina el líder, grande [UNVERIFIED cuantitativamente]. Esto no afecta a la validez asintótica, pero sí a cualquier lectura a N finito.
  - El único requisito de regularidad que usa la integración por partes de fases 2Kρ es h de clase C¹ con soporte compacto que se anula en el borde. h_N = (1−16|y−Nu|²/N²)_+² lo cumple (`papers/ir-corona/ir-corona.md:426`; C2a `:243-246`).
- **Peso evidencial:**
  - Lo que establece la nota, si la revisión la acepta: un límite asintótico N→∞ y una clasificación estructural en su clase congelada, que son los dieciséis pares originales, el walk CJWW (5.15), el nodo cero y el corte P = 1_{|p|≤N^{-1/2}}.
  - Lo que no establece: ningún valor, signo ni patrón +1:+1:−2 a N accesible. Con γ√N ≈ 1.1 en N=24 (`state/CURRENT_STATE.md:1655-1657`) y un λ posiblemente pequeño, el régimen asintótico no está alcanzado en los N disponibles.
  - Una verificación finita no podría confirmar (C1), (C2) ni (C15). Sólo podría falsar en dos casos: si una evaluación de G diera un autovalor ≤ 0, o si los factores exactos (128, 64, 512, C14) no se reprodujeran. Por tanto la revisión debe ser analítica, no numérica (NO_RIGIDITY_FROM_FINITE_SCAN).
- **Reproducibilidad:**
  - No hay script, semilla ni entorno que registrar. La reproducibilidad depende de fijar exactamente el texto revisado, y hoy no está fijado:
    - La nota está sin versionar (`git status`).
    - Su SHA256 actual es `f6266e951d3f5ffed20aef9ef8a75fe189f56b90df2b2f2e9af0abf11d407fb5` (`sha256sum` en esta sesión).
    - El §12 (`:720-736`) se añadió después de la derivación. Enlaza `reports/2026-09-22--front-resource-scaling.md`, que también está sin versionar (`git ls-files`: UNTRACKED).
  - Las fuentes importadas en §2 están versionadas: C1, la representación C2, C2a y su revisión, y la revisión C2b (`git ls-files` en esta sesión).
  - Lo que falta es un snapshot citable. El precedente es la revisión de C2b, que leyó sus entradas por `git show <commit>:<ruta>` con blob hashes (`reports/2026-09-22--c2b-independent-review.md:26-50`).
  - Antes de la revisión, recomiendo:
    1. Commit de la nota, con autorización del usuario.
    2. Excluir el §12 del alcance revisado, o moverlo a otro fichero.
    3. Registrar el commit y el blob o SHA256 como único snapshot de la revisión.
    4. Declarar que la revisión no ejecuta código.
- **Comprobaciones propias del proyecto** (`comite/roles/numerico.md`):
  1. **Qué depende de cálculo numérico:** nada. Todo es analítico. La transferencia de §5 depende de lemas de C2a revisados sólo para σ2/I. La adaptación uniforme de esos lemas a los quince pares restantes es el punto analítico más débil y debe ser el foco de la revisión (`:250-251`, `:676-677`).
  2. **Si se alcanza el régimen asintótico:** no en los N accesibles. γ√N ≈ 1.1 en N=24 y el resto relativo es O(N^{-1/4}), con constantes desconocidas y un λ posiblemente pequeño en los detectores de rango uno. Las salvedades 1 y 2 de C2a deben arrastrarse a cualquier PASS de C2c, fila por fila.
  3. **Tipo de cálculo propuesto:** la nota no propone ninguno. La aritmética exacta de (C9)–(C15) y (C14) es verificable a mano o simbólicamente, en aritmética racional más √3, sin coma flotante. Recomiendo que el revisor la rehaga a mano, como un criterio congelado.
  4. **Falsación barata sin barrido:**
     - Posible: evaluar G^{M,D} (8 familias × una matriz 4×4) con cuadratura certificada, por aritmética de intervalos, y comprobar λ_min > 0. Eso podría falsar (C15) o estimar el umbral efectivo. No es un barrido en N, pero la nota se declara libre de cálculo numérico, y el contrato no lo autoriza explícitamente.
     - Recomendación: no hacerlo dentro de la revisión de C2c. Si se quiere, debe ser un ítem aparte con autorización del usuario (NO_UNCHARTERED_GATE), y su resultado sólo podría falsar la afirmación o medir el umbral, nunca confirmar la asintótica.
     - Prohibido: usar N=24/40 (contrato `:141-142`).
- **Criterios que deben congelarse antes de la revisión (vertiente computacional):**
  - (a) El revisor rehace a mano, o con álgebra exacta, los factores 128, 64 y 512, las frecuencias y (C14) con m0 = (1,−1,1)/√3.
  - (b) Comprueba que O(K^{-13/2}) domina a todos los restos de (C16).
  - (c) Comprueba que (C15) se lea como cota cualitativa, no como constante.
  - (d) Ningún veredicto se apoya en valores a N finito ni en cálculo no autorizado.
  - (e) Cualquier C2C_PASS debe llevar las salvedades de N^{-1/4}, de γ√N y de constantes o umbrales abiertos.
- **Salvedades:**
  - La afirmación de mal condicionamiento de G y de un umbral grande en N es una estimación analítica mía, no calculada [UNVERIFIED].
  - No he auditado línea a línea los lemas (10)–(23) de C2a al cambiar M y D. Sólo he comprobado la consistencia de órdenes que cita la nota (`:299-327`). La uniformidad de esa adaptación queda para el revisor [UNVERIFIED por este rol].
  - La afirmación "C_{0,M} > C_{1,M} > 0" (`:434-436`) la comprobé: C_0 − C_1 ∝ ∫(h/ρ²) Σ ν (t₊ − t₋)² > 0 y t_{σ,+}·t_{σ,−} > 0 porque todos los denominadores son ≥ γ. Es correcta a nivel analítico.
  - El SHA256 citado corresponde al fichero en esta sesión. Cambiará si se edita, por ejemplo al separar el §12, y habrá que recalcularlo tras la reparación.

## 5. Controls (wave 2)
### Falsificador

**Veredicto:** no puede pasar a revisión tal como está. La matemática que se comprueba a mano resiste los ataques: el contraejemplo de §4, los factores 128, 64 y 512, la prueba de definitud positiva de §7 y el argumento de §9.2 los he vuelto a comprobar y aguantan. El problema está en tres sitios: el objeto que se revisaría, el revisor y las reglas de veredicto. Tal como están, un `C2C_PASS` sería trivial de obtener y difícil de falsar.

- **Modos de fallo concretos:**
  1. **El eslabón nuevo no está derivado.**
     - La nota adapta los lemas de C2a a D de rango uno y a ζ_M en §5.1–5.3, pero sólo con prosa: «La justificación del resto es la ya escrita» (`reports/2026-09-22--c2c-structural-scope.md:272`) y «se conservan porque D es una matriz constante» (`:283-287`).
     - La ganancia angular de C2a se aplicó a «funciones analíticas en la esfera: R_N(u+ηbn) y P_σH_3P_σ» (`reports/2026-09-22--c2a-independent-review.md:274-278`). Con D≠I, la amplitud del emparejamiento lineal pasa a ser hDR_N. Nadie ha comprobado que el conjunto de fases radiales «±ℓ+εb−ηb−σ» (`reports/2026-09-22--c2a-oscillatory-transfer.md:193-196`) siga completo y sin fases estacionarias.
     - Es plausible, pero no está verificado [UNVERIFIED]. De esta adaptación dependen las columnas «ley N⁻³» y «coherencias» de las 15 filas nuevas.
  2. **Una entrada es PRELIMINARY y no está revisada.**
     - §5.1 usa la «reducción C2 §4» y el «campo radial para los cuatro M» (`c2c:78,242-253`).
     - La nota C2 se declara `REPRESENTATION_DERIVED / PRELIMINARY` y «no tiene todavía revisión independiente» (`reports/2026-09-22--c2-projected-response-representation.md:5-10`). El PASS de C2a la cubre sólo para σ₂.
     - En la tabla de fuentes de §2, esa nota aparece sin su nivel de evidencia.
  3. **Hay igualdades afirmadas sin prueba.**
     - «Ocho familias» (`c2c:527`): sólo está probado «a lo sumo ocho».
     - «Para σ₂/I son exactamente 𝒞₀, 𝒞₁» (`c2c:436-437`): no se muestra la comparación de normalizaciones.
  4. **Hay un cuantificador oculto.**
     - (C2), (C15) y (C16) son eventuales, con un N₀(M,D) no efectivo.
     - λ_{M,D} puede ser pequeño con detectores de rango uno: pesos de (C14) de hasta ((1−1/√3)/2)² ≈ 0.045, según una estimación del numérico que no está calculada.
     - Además, la ganancia relativa es sólo N^{-1/4}. Nada de esto se puede leer a N finito.

- **Violaciones de freeze:**
  - **Objeto sin fijar.** El informe no está versionado (`git status`: `??`). Su SHA256 en esta sesión es `f6266e95…d407fb5`, pero cualquier reparación lo cambia. §12 se añadió después de la derivación (`c2c:720-736`) y enlaza a otro fichero también sin versionar, `front-resource-scaling.md`.
  - **Criterios fijados después de conocer el mecanismo.** El contrato C2c se escribió conociendo ya el mecanismo de C2b y lo reconoce (`theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:29-32`). Fuera de las cuatro etiquetas (`:163-166`) no hay criterios de aceptación congelados.
  - **El autor elige el foco de la revisión.** El único checklist existente son los «puntos prioritarios» de §10 (`c2c:675-679`), escritos por el propio autor. Si se adoptan como alcance de la revisión, el autor decide dónde mira el revisor. Esa lista deja fuera §5.1, la dependencia de la nota C2 PRELIMINARY y §9.2.

- **Coerción del resultado:**
  - Las 15 filas nuevas salen «D» en los cinco niveles. No hay ningún OPEN (`c2c:537-554`, «No quedan filas sin derivación», `:703-704`), aunque el contrato no exigía un resultado favorable (`GATE:103-104`). Una clasificación tan uniformemente favorable, obtenida en una sola pasada, sube la carga de prueba de la revisión.
  - El contrato no define veredictos por fila y por nivel. Sin esa regla, la revisión queda binaria:
    - o bien un PASS global arrastra las 15 filas junto con su eslabón más débil (§5.2);
    - o bien un REPAIR global tumba también A/B y (C1), que están probados.
  - Hay que congelar antes cómo se registran los resultados parciales, por ejemplo «A/B/(C1) PASS; ley N⁻³ en filas de rango uno REPAIR u OPEN». Un nivel inconcluso debe quedar OPEN, no absorberse en PASS ni en FAIL.

- **Afirmaciones prematuras o demasiado amplias:**
  - En §9.2, «Este argumento se extiende a cortes escalares con esas propiedades de abiertos» (`c2c:611`) es una generalización que no está entre las afirmaciones 1–4 de §11. O entra de forma explícita en el alcance revisado o se retira (NO_SCOPE_BROADENING).
  - El recuadro de §1 anuncia una «cota inferior positiva uniforme» (`c2c:55`) antes de la revisión. Está bien etiquetado como pendiente, pero ningún resumen puede citarlo sin esa etiqueta (NO_EVIDENCE_PROMOTION).
  - §12 (Liu–Chen) presenta un «antecedente externo del mecanismo» dentro de un artefacto de prueba. Mezcla prior art con la prueba, y la novedad sigue OPEN (NO_NOVELTY_WITHOUT_PRIOR_ART).

- **Ataques propios del proyecto:**
  1. **Promoción encubierta.** Hoy no la hay: la nota dice que la tabla «no es una promoción canónica» (`c2c:704-705`). El riesgo es un PASS global sin regla por fila, que extendería σ₂/I a otros pares sin una prueba revisada de §5.2.
  2. **Contrato posterior al descubrimiento.** Sí. El contrato C2c es posterior a C2b, y los criterios de aceptación de la revisión aún no están escritos. Deben congelarse antes de nombrar al revisor y antes de que éste lea la nota.
  3. **Rigidez inferida de búsqueda fallida o barrido finito.** No aplica. No se usan N=24/40, barridos ni ajustes (`c2c:673`), y la no anulación (§7) es una prueba de independencia racional, no una búsqueda.
  4. **Revisor no independiente.** Es el ataque más grave:
     - El autor es Codex `/root` (`c2c:3`), que también fue el revisor de C2b. C2c importa como «entrada certificada» las constantes de esa revisión suya (`c2c:75`).
     - Astra corre sobre Codex (`state/CURRENT_STATE.md:426`, «ASTRA failed two turns (Codex usage limit)»). Es la misma casa que el autor y cuenta como una sola voz.
     - Claude Opus 5 es de otra casa, pero fue autor del candidato C2b y revisor de los lemas de C2a (`reports/2026-09-22--c2a-independent-review.md:8`). Esos lemas son exactamente los que §5 transfiere, así que revisaría la extensión de su propia certificación.
     - Este comité también es de la familia Claude. Su dictamen no es una revisión independiente.
  5. **v_max sin cualificar o c_IR con masa leído de |∇ω(0)|.** No ocurre. Nodo cero sin masa y c_IR=1 (`papers/ir-corona/ir-corona.md:112`). La única mención es «velocidad emergente», presentada como hipótesis no requerida (`c2c:207`).

- **Puerta de falsación independiente:** no se cumple.
  - Hoy el autor es el único verificador de §§5–7 y de §9.2. La nota lo admite (`c2c:708-709`).
  - Mínimo exigible:
    - un revisor que no sea de la casa Codex (lo que excluye a Codex `/root` y a Astra);
    - si es Claude Opus 5 o un modelo Claude, que el conflicto sobre los lemas de C2a quede declarado en el registro;
    - la re-derivación de §5.2 hecha desde el texto primario de C2a, no desde su revisión.
  - Si se busca una tercera casa (por ejemplo `sanedrin`), sólo sirve como segunda voz sobre §5.2, nunca como sustituto de la revisión.

- **Test mínimo de falsación:**
  - Qué es: una re-derivación ciega y escrita, sin cálculo numérico, del emparejamiento lineal c_{M,D,N} y de la forma cuadrática para la fila más adversa, M=I con D₃=(I+σ₃)/2, que es el detector que anula el espinor fuente ↓.
  - Cómo se hace: el revisor la deriva desde `f4f937e` y la nota C2 **antes de leer §5.2 de C2c**. Luego la compara con (C6), (C7) y (C14). Debe listar el conjunto completo de fases radiales y comprobar que todas tienen módulo ≥γ y que ninguna es estacionaria. También debe comprobar el peso 1/6 de (C14) en esa fila.
  - Qué falsaría: aparecer una fase estacionaria o un término cruzado Π₊DΠ₋ no controlado. Cualquiera de los dos refuta la columna «ley N⁻³ / coherencias» de las filas de rango uno, sin tocar A/B ni (C1).
  - Qué queda fuera: la cuadratura certificada de G no está autorizada por el contrato (`GATE:141-145`). Sólo podría falsar, nunca confirmar, y exigiría un ítem aparte autorizado por el usuario.
  - Requisitos previos:
    - Versionar la nota con commit y SHA256, con autorización del usuario.
    - Sacar §12 del objeto revisado.
    - Congelar por escrito:
      - la regla de veredicto por fila y por nivel;
      - el alcance: afirmaciones 1–4 de §11, más §9.2 o su retirada, y la dependencia de la nota C2 PRELIMINARY;
      - las salvedades obligatorias: N^{-1/4}, γ√N y un N₀ no efectivo;
      - el nombre del revisor, junto con sus conflictos declarados.

### Guardián de gates y alcance

- **Verdict: BLOCK** (bloqueo de reparación, no de contenido científico: el paso siguiente natural —revisión independiente— no puede autorizarse aún porque el artefacto que se enviaría a revisión no cumple el estándar de versionado que este mismo proyecto ha aplicado sin excepción a C1, C2a y C2b).

- **Authorization**: la ejecución de C2c en sí está chartered. `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md` (committed en `f4f937e`) define exactamente este entregable ("Una futura ejecución debe producir `reports/2026-09-22--c2c-structural-scope.md`… `PROOF_WRITTEN / REVIEW_PENDING` distingue la ejecución de su aceptación. Una revisión independiente puede emitir `C2C_PASS`…"), y `state/CURRENT_STATE.md` L4/§10.1 registra `C2c structural scope UNBLOCKED / NOT_EXECUTED` como línea activa. Por tanto pasar a revisión independiente es el paso previsto por el propio contrato, no una ampliación de mandato.

- **Freeze status — problema central**: el contrato (criterios de S1–S5, entregables 1–5, veredictos posibles) se congeló por escrito y se comprometió en `f4f937e` **antes** de que existiera el informe de ejecución (`reports/2026-09-22--c2c-structural-scope.md` está en `?? ` en `git status --short`, no versionado). Eso cumple la mitad "definir antes de ver evidencia". Pero el informe de ejecución mismo declara explícitamente: *"El informe C2c se deja sin commit… No hay push."* (`reports/2026-09-22--c2c-structural-scope.md` §11). Esto rompe el patrón de custodia que el propio proyecto ha seguido sin excepción hasta ahora:
  - La revisión de C2b identificó sus siete entradas obligatorias **por objeto Git** (blobs concretos) y las leyó con `git show <commit>:<ruta>` sobre el commit `19eb7a383cbb09464e91b64e89f724204e58cccb` (`reports/2026-09-22--c2b-independent-review.md` §2). El candidato C2b había sido comprometido en ese mismo commit antes de ser revisado (`git show 19eb7a3 --stat` lista `reports/2026-09-22--c2b-block-decomposition-candidate.md`).
  - El gate de techo del punto (3) se registra igual: *"the review at `bd44122` accepts the proof at `db083af`"* (`PROJECT_INSTRUCTIONS.md` §7) — prueba y revisión, ambas identificadas por commit.
  - `PROJECT_INSTRUCTIONS.md:18`: la autoridad canónica cambia sólo "by a new commit that records the reason" — el modelo de autoridad del proyecto es explícitamente basado en commits, no en hashes de archivo sueltos.
  - El único ancla de integridad que tiene hoy el informe C2c es un SHA256 citado en el DOSSIER (`f6266e9…`), que verifiqué y coincide con el archivo en disco (`sha256sum reports/2026-09-22--c2c-structural-scope.md`). Pero un hash de trabajo-en-curso, no comprometido y no citado dentro de ningún fichero versionado, no ofrece la misma trazabilidad que un blob Git referenciado desde un commit: es una atestación externa (del analista numérico en la ola 1), no una entrada del historial del repositorio. Ningún revisor independiente puede hoy hacer `git show <commit>:reports/2026-09-22--c2c-structural-scope.md` como hicieron los revisores de C1/C2a/C2b.
  - **Reparación exigida antes de abrir la revisión**: comprometer `reports/2026-09-22--c2c-structural-scope.md` en un commit dedicado (sin tocar contenido, para no invalidar el SHA256 ya verificado), de modo que la revisión pueda citar blob y commit exactos, igual que en C1/C2a/C2b.

- **Scope**: dentro de lo declarado. El informe cubre exactamente los dieciséis pares y los niveles S1–S5 fijados en el contrato (`reports/2026-09-22--c2c-structural-scope.md` §§3–9), sin sustituir perfiles, filtros o geometría, y su propia tabla de "failure search" (§10) declara no usar `L-L_{PP}`, Teorema 4.4, ley total ni `N=24/40` — confirmado por `grep` sin hallazgos contradictorios en el resto del texto. No hay ampliación hacia causal sets, redes aleatorias u otras clases de sustrato.

- **Forbidden moves present?**: ninguno detectado dentro del propio informe C2c (sin simulaciones, barridos, ajustes, suavizado de corte ni nueva saddle analysis — autoevaluado en L62-63 y L673, sin evidencia contraria tras grep completo del documento). Aparte del informe: el §12 "Addendum bibliográfico" (Liu–Chen) se añadió **después** de la derivación y el propio texto aclara que "no forma parte del snapshot de entrada ni cambia `PROOF_WRITTEN / REVIEW_PENDING`" — es contexto, no evidencia usada en la prueba; no viola el congelamiento pero debe seguir marcado como extra-snapshot en cualquier promoción futura.

- **Project-specific checks** (de `comite/roles/guardian.md`):
  1. ¿Autorizado en `CURRENT_STATE.md`? Sí — `C2c structural scope UNBLOCKED / NOT_EXECUTED` (L4, §10.1).
  2. ¿Contrato congelado con criterios de PASS/FAIL escritos antes de la evidencia? Sí, `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md`, comprometido en `f4f937e`, anterior al informe de ejecución.
  3. ¿Respeta el estado branch-local y no promueve a `main`? Sí — todo el trabajo vive en `research/b-infinity-post-s4-gate` (verificado con `git branch --show-current`); no hay push.
  4. ¿Mantiene separados C3, E/AdS (FROZEN) y H1c/E0? Sí — el informe reafirma "C3 sigue SEPARATE y E/AdS FROZEN" (§11) y no toca esos frentes.
  5. ¿Implica commit, push, publicación o barridos no autorizados? No hay push ni publicación; **pero el informe queda deliberadamente sin commit**, lo cual es precisamente el punto de fricción de este veredicto (ver Freeze status).

- **Reasons**:
  - El paso "abrir revisión independiente de C2c" está chartered por `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md` y `CURRENT_STATE.md` §10.1 — no es un problema de autorización.
  - El paso falla el estándar de custodia/versionado que el propio proyecto ha aplicado sin excepción en C1, C2a, C2b y el gate del punto (3) (`bd44122`/`db083af`): siempre el candidato bajo revisión estuvo comprometido a un commit citable por blob antes de que el revisor lo auditara. `reports/2026-09-22--c2c-structural-scope.md` no lo está.
  - Reparación mínima antes de autorizar la revisión: (a) comprometer el informe C2c tal cual (para preservar el SHA256 ya atestiguado por el analista numérico y verificado aquí); (b) asignar como revisor a un agente distinto del autor — el informe es de "Codex, agente `/root`" (L3), y el propio documento reconoce que "la autoría de esta derivación no constituye revisión independiente de ella misma" (§11); siguiendo el patrón de independencia autor/revisor usado en C1→C2a→C2b, el revisor de C2c debe ser explícitamente otro agente (p. ej. Claude Opus 5, u otro distinto de Codex/root), y esa asignación debe registrarse por escrito antes de empezar; (c) mantener fuera del paquete a comprometer los documentos FR1–FR3 / Liu–Chen y el roadmap del 21-09, que son trabajo no chartered (no hay `theory/FR*_GATE.md` ni entrada en `CURRENT_STATE.md` para "FR1/FR2/FR3/front-resource" — verificado por grep) y no deben mezclarse en el mismo commit que fija la evidencia para la revisión de C2c, para no contaminar el snapshot de entrada del revisor.
  - Una vez cumplidas (a) y (b), el alcance de la revisión debe limitarse exactamente a lo que el contrato define como salida posible: `C2C_PASS` (para un alcance explícitamente delimitado, sin convertir los niveles marcados OPEN en S3/§8 en teoremas), `C2C_REPAIR_REQUIRED`, `C2C_FAIL` o `C2C_INCOMPLETE` — ninguna otra promoción de estado está autorizada por este contrato.

### Verificador de literatura

| Citation | Claimed by | Status |
| --- | --- | --- |
| `papers/ir-corona/ir-corona.md:112` — c_IR = 1 | Físico | CONFIRMED — línea 112 dice "the closed infrared light cone... $c_{\mathrm{IR}}=1$" |
| `papers/ir-corona/ir-corona.md:426` — h_N(y)=(1−16\|y−Nu\|²/N²)_+², C¹ | Matemático, Lógico, Numérico | CONFIRMED — fórmula literal en :426; centro u=(1,1,1), soporte en bola de Bob |
| `papers/ir-corona/ir-corona.md:134` — "smooth bump" | Matemático | CONFIRMED — "profiles F_N,h_N are smooth bumps of width N/4" (línea 134). Nota: la nota C2c en ningún punto verificado afirma C^∞; la observación del matemático de que es C¹ y no C^∞ es una lectura propia, no una cita textual falsa |
| `papers/ir-corona/ir-corona.md:513-518` — Teorema 4.1, T_N ≤ 9N⁴e^{-JN} | Matemático, Físico | CONFIRMED — enunciado textual exacto en :513-518 |
| `papers/ir-corona/ir-corona.md:383` — γ=√3−3/2, margen de Bob | Físico | CONFIRMED — línea 383: "$|y-x|-N\ge(\sqrt3-\tfrac32)N$" |
| `formal/README.md` — `TN_bound`, T_N ≤ 4N⁴e^{−JN} (más fuerte que 9N⁴) | Lógico, Numérico | CONFIRMED — fila de tabla en README (línea 31) dice literalmente "stronger than the paper's 9N⁴e^{−JN}"; `delta_le_four_T` (línea 32) trata el observable total, tal como afirma el lógico |
| `state/CURRENT_STATE.md:1368` — gate §8.21 NOT_EXECUTED | Físico | CONFIRMED — línea 1368: "8.21 PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE — AUTHORIZED, NOT_EXECUTED" |
| `state/CURRENT_STATE.md:4` — lemas de C2a revisados una sola vez (sigma2/I) | Físico, Lógico | CONFIRMED — línea 4: "C2a PASS for sigma2/I (one independent agent review)" |
| `state/CURRENT_STATE.md:1654-1657` (numérico cita :1655-1657) — γ√N≈1.1 en N=24 | Numérico | CONFIRMED (offset menor) — el texto exacto está en :1649-1651, no exactamente en :1655-1657; mismo párrafo, error de línea de ±5-6. Contenido correcto: "gamma sqrt(N)... about 1.1 at N=24 and 1.5 at N=40" |
| `reports/2026-09-22--c2c-structural-scope.md:3` — autor Codex `/root` | Matemático, Físico, Lógico | CONFIRMED — línea 3: "Fecha: 2026-09-22. Autor: Codex, agente `/root`." |
| `reports/2026-09-22--c2c-structural-scope.md:97-122` — enunciado abstracto §3.1 | Matemático, Lógico | CONFIRMED — objetos H_N, φ_N, V_N, U_N, P_N, Q_N, E_N, T_N definidos exactamente ahí |
| `reports/2026-09-22--c2c-structural-scope.md:40` — (C1) sólo suficiente | Matemático, Lógico | CONFIRMED — línea ~40: "El criterio es suficiente, no se afirma que sea necesario ni óptimo" |
| `reports/2026-09-22--c2c-structural-scope.md:212-228` — contraejemplo ℂ² | Matemático, Lógico | CONFIRMED — valores a=−√2e₁, d_P=−φ, T=0, 𝒬=1/2, c=−1/2, bloques (−1/2,1/2,0) coinciden exactamente con el texto en esa franja |
| `reports/2026-09-22--c2c-structural-scope.md:352-360` — matriz de Gram (C8) | Lógico | CONFIRMED — fórmula G^{M,D}_{ij}=∫f_i†f_j en :352-357 |
| `reports/2026-09-22--c2c-structural-scope.md:493-499` — (C15), 512β²λ | Matemático, Numérico | CONFIRMED — fórmula "0<512β²λ_{M,D}≤𝒜_{M,D}(K)≤512β²Λ_{M,D}<∞ para todo K real" en :493-499 |
| `reports/2026-09-22--c2c-structural-scope.md:598-616` — §9.2, Pa sin soporte finito | Físico, Lógico | CONFIRMED — argumento de no-localidad del proyector espectral textual en :600-608 |
| `reports/2026-09-22--c2c-structural-scope.md:622-630` — exponente 3 del protocolo de corte | Físico | CONFIRMED — línea ~627: "el corte K=√N: el campo líder de orden K^{-3} produce una forma cuadrática de orden K^{-6}=N^{-3}" |
| `reports/2026-09-22--c2c-structural-scope.md:715-736` — §12 Liu–Chen, addendum posterior | Todos los cuatro roles | CONFIRMED — §12 en :720-731 cita explícitamente K. Liu y D. Chen, Phys. Rev. A 114, 032434 (2026), arXiv:2609.01970v2, §§V.B–VI.B, (40)–(47), (66)–(67); el propio texto dice "se añade después de la derivación y no forma parte del snapshot de entrada" (línea ~733-734), tal como citan los roles. **No verificado**: el contenido real del artículo Liu–Chen (no está en `biblioteca/` ni se pidió acceso arXiv en esta verificación) — la nota FR-referenciada (`reports/2026-09-22--front-resource-scaling.md`) tampoco se auditó línea a línea |
| `reports/2026-09-22--c2-projected-response-representation.md:137-162` — fuentes Â_M | Matemático | CONFIRMED — fórmula (8) y velocidad de soporte uno de Weyl sin corte, cola en cos(bk)/k⁴, presentes tal cual en ese rango |
| `reports/2026-09-22--c2a-oscillatory-transfer.md:230-260` — 𝒞₀, 𝒞₁, factor 128/256 | Matemático, Numérico | CONFIRMED — 𝒞₀=128B²∫..., 𝒞₁=256B²∫... aparecen exactamente en ese rango |
| `reports/2026-09-22--c2b-independent-review.md:293,299-307` — \|ρ\|≤8T+4T², \|η\|≤6T | Matemático | CONFIRMED — "8T_N+4T_N^2" y "≤2T_N(1+2)=6T_N" aparecen literalmente en ese rango |
| `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:23-25` — Codex `/root` revisor de C2b | Matemático | CONFIRMED — línea 23-25: "Su revisión es de Codex, agente `/root`, independiente del autor Claude Opus 5" |
| `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:90-96` — tabla S3, veredicto por fila/nivel | Matemático | CONFIRMED — tabla de 5 niveles (identidades exactas … coherencias individuales) presente en ese rango |
| `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:141-145` — nivel D, prohibición N=24/40 | Numérico | CONFIRMED — "No usar L-Lpp, Teorema 4.4... No se autorizan... simulaciones, nuevos barridos" en esa zona |
| `theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md:163-166` — cuatro etiquetas C2C_PASS/REPAIR/FAIL/INCOMPLETE | Lógico | CONFIRMED — enumeración textual exacta al final del fichero |
| `reports/2026-09-22--c2a-independent-review.md:8` — Claude Opus 5 revisor de C2a | Físico | CONFIRMED — línea 8: "Revisor: Claude Opus 5 (`claude-opus-5`) en Claude Code" |
| `git ls-files` / `git status` — nota C2c y front-resource-scaling.md sin versionar | Numérico, Físico, Lógico | CONFIRMED — ambos ficheros ausentes de `git ls-files`; aparecen como `??` en `git status --short`. Las fuentes importadas (C1, C2, C2a, revisión C2a, C2b) sí están trackeadas |
| SHA256 `f6266e9…7fb5` de `c2c-structural-scope.md` | Numérico | CONFIRMED — `sha256sum` reproducido en esta sesión da exactamente `f6266e951d3f5ffed20aef9ef8a75fe189f56b90df2b2f2e9af0abf11d407fb5` |
| HEAD `f4f937e`, branch `research/b-infinity-post-s4-gate` (dossier) | Chair | CONFIRMED — `git rev-parse HEAD` = `f4f937e102def05f8797a94e256a460d81b0cc33`; `git branch --show-current` = `research/b-infinity-post-s4-gate` |

- Notes: no se encontró ninguna cita que contradiga la afirmación para la que se usó. Todas las anclas priorizadas por el chair (c_IR=1, bola de Bob, TN_bound, CURRENT_STATE.md, rangos de revisión C2a/C2b, referencias internas de la propia nota, y el §12 Liu–Chen) fueron localizadas y coinciden en contenido con lo que cada rol afirma. Único desajuste menor: el numérico cita `CURRENT_STATE.md:1655-1657` para "γ√N≈1.1 en N=24"; el texto real está en `:1649-1651` (mismo párrafo, desplazamiento de línea de ~5-6, contenido correcto).
- No verificado en esta pasada (fuera del subconjunto priorizado, declarado explícitamente sin comprobar): el contenido íntegro del artículo Liu–Chen (Phys. Rev. A 114, 032434) citado en §12 — solo se confirmó que la cita bibliográfica y el DOI/arXiv existen en el texto de la nota, no que describan correctamente el mecanismo que la nota les atribuye, por no tener acceso al PDF fuente en `biblioteca/` dentro de este mandato de solo lectura; `reports/2026-09-22--front-resource-scaling.md` (solo se confirmó que existe y está sin versionar, no su contenido); rangos de línea secundarios citados por el lógico en `c2c:526-531`, `:570-571`, `:593-595`, `:675-679`, `:699-702`; y los rangos internos de `c2a-oscillatory-transfer.md:103-112,296-400` y `c2b-independent-review.md:372-432` más allá del fragmento puntual ya confirmado (293,299-307). Ninguno de estos no-verificados afectó a un anclaje de una afirmación central (c_IR=1, T_N, factor 64/512, γ, versionado/SHA256), que sí quedaron todos CONFIRMED.

### Auditor de novedad

- **Claims examined:**
  1. El patrón de bloques `(L_PP,L_QQ,L_PQ+L_QP)/Q_N → (1,1,−2)` (C2c, (C1)/(C2), `reports/2026-09-22--c2c-structural-scope.md:14-38`), incluida cualquier redacción que lo llame "patrón +1:+1:−2".
  2. El criterio abstracto suficiente (C1): `T_N=o(Q_N), Lin_N=o(Q_N) ⇒` el patrón (`c2c:14-23`).
  3. El mecanismo de "cola de Gibbs" producida por el corte espectral duro P (`c2c:594-609`, §9.2), y su lectura física en el rol físico de ola 1 ("cola de Gibbs del corte duro", `.../ola1.md:114`).
  4. La no-localidad del proyector espectral P/Q sobre fuentes de soporte finito, usada como argumento de analiticidad/Paley–Wiener (`c2c:596-608`, §9.2).
  5. El addendum bibliográfico §12 de C2c, que cita a Liu–Chen como "antecedente externo" de (3)–(4) (`c2c:720-731`).
  6. Cualquier redacción que la revisión pudiera adoptar sobre "novedad" del resultado C2c en conjunto, dado que `NOVELTY = OPEN` es el estado canónico del proyecto (`state/CURRENT_STATE.md:43,181,410,494`) y que el guardarraíl `NO_NOVELTY_WITHOUT_PRIOR_ART` (`comite/config.toml`) y `PROJECT_INSTRUCTIONS.md` §6 obligan a toda sección, no sólo a S4.

- **Prior art found:**
  1. **Patrón +1:+1:−2** — Ningún documento local lo contiene tal cual; es una contabilidad de bloques de un observable espectral específico del protocolo congelado (16 pares, walk CJWW (5.15), nodo cero, corte K=√N). **Grado: ninguno localizado.** Es, sin embargo, una consecuencia casi inmediata de una identidad de álgebra lineal trivial (L=L_PP+L_QQ+(L_PQ+L_QP), L=o(Q_N) por el Teorema 4.1 exponencial, L_PP/Q→1 y L_QQ/Q→1 fuerzan el cruzado a −2); la propia nota lo reconoce como "trivial una vez dada (C3)" (rol Matemático, ola 1: "(C1): probado, y es trivial una vez dada (C3)"). El propio C2c excluye explícitamente "novedad" de su alcance declarado (`c2c:700-703`: "...atribución física exclusivamente IR/UV, novedad y cualquier aplicación inhomogénea/AdS" quedan fuera). El rol Físico de ola 1 confirma que no se afirma "novedad frente a Bernstein o Liu-Chen" (`.../ola1.md:135`).
  2. **Criterio abstracto (C1)** — No es una ley física ni una proposición con antecedentes bibliográficos que buscar: es aritmética de límites bajo hipótesis de dominancia declaradas por la propia nota como suficientes, no necesarias ni óptimas (`c2c:20`). **Grado: no aplica prior-art (hecho matemático elemental, no un teorema con historia bibliográfica propia)**; no debe presentarse como descubrimiento.
  3. **Cola de Gibbs / cola inducida por corte espectral duro** — Prior art parcial concreta, ya identificada dentro del propio proyecto:
     - K. Liu, D. Chen, *Maximal-velocity deficit...*, Phys. Rev. A 114, 032434 (2026), arXiv:2609.01970v2, §§V.B–VI.B, (40)–(47), (66)–(67) (`biblioteca/Maximal-velocity deficit under a finite-support_cn.pdf`; leído en `reports/2026-09-22--liu-chen-full-reading.md` §4). Da el mecanismo general "traza no nula en el borde ⇒ cola lenta" para un corte de Fourier duro, en un problema de CTQW en semirrecta 1D, variable conjugada distinta de la del corte IR del proyecto (`c2c:730`: "no se identifica con nuestro corte IR"; `2026-09-22--front-resource-scaling.md`§2: "no demuestra su compensación localizada ni el patrón +1:+1:−2"). **Grado: antecedente parcial/estructural del mecanismo de cola, no del resultado cuantitativo ni del patrón de bloques.**
     - C. Cedzich, A. Joye, A. H. Werner, R. F. Werner, *Exponential Tail Estimates for Quantum Lattice Dynamics*, arXiv:2408.02108v1 (`biblioteca/EXPONENTIAL_TAIL_ESTIMATES_FOR_QUANTUM_LATTICE_DYNAMICS.pdf` = `sources/2408.02108v1.pdf`). Mismo grupo de autores que el walk congelado CJWW (5.15) del proyecto. Demuestra que la probabilidad total fuera del cono balístico decae **exponencialmente** en t, con tasa ∝(distancia al borde)^(3/2) — mecanismo **dinámico** de Lieb–Robinson, no un corte espectral impuesto sobre un recurso. Es plausible que sea la fuente (o análoga a la fuente) del "Teorema 4.1" que C2c invoca para la pequeñez exponencial del total L (`c2c:614-615`: "sigue exponencialmente pequeña por el Teorema 4.1") [UNVERIFIED — no confirmé en esta sesión que el Teorema 4.1 del manuscrito cite exactamente este paper; el dossier no lo especifica]. **Grado: antecedente directo para "el total es exponencialmente pequeño"; no cubre la descomposición algebraica interna en bloques P/Q ni su cociente −2.**
     - S. Bravyi, M. B. Hastings, F. Verstraete, *Lieb-Robinson bounds...* (`biblioteca/Lieb-Robinson bounds and the generation of correlations.pdf`). Antecedente general del "cono efectivo con colas exponenciales" para dinámica local; mecanismo dinámico, no espectral. **Grado: relacionado/contexto, no específico al mecanismo de corte duro (C2c §9.2).**
  4. **No-localidad de un proyector espectral duro sobre fuentes de soporte finito (§9.2)** — El argumento de C2c es una versión concreta del teorema de Paley–Wiener / principio de incertidumbre (una función de soporte compacto no nulo no puede tener transformada de soporte compacto, salvo la nula). Es un hecho **clásico de análisis armónico**, no localizado como texto citado en `biblioteca/` ni `sources/` en esta sesión. **Grado: prior art clásico, casi con certeza (Paley–Wiener 1934 / teoría de funciones enteras de tipo exponencial), pero sin fuente local verificable** → [UNVERIFIED: no hay documento en `biblioteca/`/`sources/` que lo contenga explícitamente; es hueco de búsqueda, ver abajo]. Ningún documento local reclama esto como propio; tampoco C2c lo hace — lo presenta como argumento auxiliar, no como resultado.
  5. **Estado de novedad general del proyecto** — `PROJECT_INSTRUCTIONS.md` §6 y `state/CURRENT_STATE.md` fijan que la cota de Bernstein escalar/trigonométrica y su teoría de igualdad son prior art para la familia S4/B*, y que `NOVELTY = OPEN`. Las auditorías previas (`reports/2026-09-15--s4-family-prior-art-audit.md`, `reports/2026-09-17--physical-realization-literature-scan.md`) son sobre la familia S4 y la realización física absoluta, **no** sobre C2c; no cubren el patrón de bloques, (C1) ni el mecanismo de cola de §9.2. **Grado: no aplicable directamente a los objetos de C2c**; no puede invocarse esa auditoría previa como si cerrara la novedad de C2c.

- **Novelty wording allowed:**
  - Se puede decir: "bajo las hipótesis congeladas del protocolo (16 pares, walk CJWW (5.15), nodo cero, corte espectral duro K=√N), se demuestra —pendiente de revisión independiente— una descomposición estructural específica de este observable en bloques P/Q con razón asintótica (1,1,−2)", presentándolo como **resultado condicional dentro de la clase declarada**, no como fenómeno general.
  - Se puede decir que el mecanismo de cola de §9.2 (corte duro ⇒ fuente proyectada sin soporte finito) **usa un argumento de tipo Paley–Wiener/analiticidad** y que **tiene un antecedente externo parcial** en Liu–Chen (mecanismo de cola por trazas no nulas en el borde, en un problema distinto: CTQW en semirrecta 1D frente a QCA 3D con recurso IR fijo) y una relación de contexto con Cedzich–Joye–Werner–Werner (decaimiento exponencial del total, mecanismo dinámico distinto del corte espectral).
  - **No se puede decir**: que el patrón +1:+1:−2, el criterio (C1) o el argumento de no-localidad espectral son "nuevos" en sentido general, "primeros en demostrarse", ni que generalizan o resuelven algo dejado abierto por Liu–Chen o por Cedzich–Joye–Werner–Werner. Tampoco se puede decir que Liu–Chen "confirma" o "prueba" el patrón de C2c: el propio §12 y `2026-09-22--front-resource-scaling.md` lo excluyen expresamente (`c2c:729-731`).
  - **No se puede** usar la ausencia local de un texto sobre Paley–Wiener/uncertainty principle como si autorizara reclamar novedad sobre el argumento de §9.2: es prior art casi seguro por conocimiento matemático estándar, aunque no esté en `biblioteca/`; debe tratarse como "clásico, no re-demostrado aquí como descubrimiento", nunca como "hueco de prior art que favorece novedad".
  - Cualquier frase de novedad sobre C2c en conjunto debe llevar la cualificación de alcance de `KEEP_QUANTIFIERS`/`NO_SCOPE_BROADENING`: sólo dentro de los 16 pares originales, del corte concreto y del walk congelado; y debe respetar que `NOVELTY = OPEN` sigue siendo el estado canónico del proyecto — C2c no lo cierra ni lo reabre (`NO_NOVELTY_WITHOUT_PRIOR_ART`, `comite/config.toml`).
  - El §12 debe tratarse en la redacción de la revisión como lo que es: un addendum bibliográfico posterior al snapshot de entrada `f4f937e`, no parte de la prueba ni evidencia que certifique novedad o su ausencia; si se versiona junto con C2c debe marcarse fuera del alcance revisado, como ya piden los roles Matemático y Físico de ola 1 (`.../ola1.md:80,94,146`).

- **Search gaps:**
  - No se buscó externamente literatura específica sobre "cancelación de bloques de un observable proyectado en razón −2" ni sobre "criterios de suficiencia para patrones de razón fija en descomposiciones P/Q" — es plausible que exista literatura de teoría de operadores/perturbaciones sobre este tipo de identidad algebraica genérica, pero no se buscó.
  - No se localizó en `biblioteca/`/`sources/` un texto que contenga explícitamente el teorema de Paley–Wiener o el principio de incertidumbre posición-momento en la forma usada en §9.2; sería el hueco más relevante a cerrar con una búsqueda externa antes de que cualquier revisión describa ese argumento como algo distinto de "estándar".
  - No verifiqué si el "Teorema 4.1" que C2c invoca para la pequeñez exponencial del total (`c2c:614-615`) cita efectivamente a Cedzich–Joye–Werner–Werner arXiv:2408.02108 o a otra fuente del manuscrito `papers/ir-corona/ir-corona.md`; el dossier no lo trae y no lo comprobé línea a línea en el manuscrito. [UNVERIFIED]
  - No se hizo una búsqueda bibliográfica dedicada sobre "spectral-projector non-locality" fuera de lo ya presente en `biblioteca/`/`sources/`; el hallazgo de Liu–Chen y Cedzich–Joye–Werner–Werner proviene de que ya estaban acopiados por trabajo previo del proyecto (auditorías FR1–FR3), no de una búsqueda nueva en esta sesión.
  - Las auditorías previas de novedad (`reports/2026-09-15--s4-family-prior-art-audit.md`, `reports/2026-09-17--physical-realization-literature-scan.md`) son de dominio distinto (familia S4, realización física absoluta) y no se puede extrapolar su cobertura a los objetos de C2c; sería necesaria una auditoría de novedad dedicada a C2c si en algún momento se quisiera afirmar algo más fuerte que "resultado condicional dentro de la clase declarada".

## 6. Synthesis

**Consenso de los ocho miembros:** la nota C2c no debe pasar a revisión independiente **tal como
está**. El motivo no es el contenido: nadie encontró un error en los pasos que se pueden comprobar
a mano. Cuatro miembros rehicieron por su cuenta los factores 128, 64 y 512, el contraejemplo de
§4 y la no anulación (C14) (matemático, lógico, numérico y falsificador), y la física del §9.4 se
considera bien acotada. El bloqueo es de custodia y de congelación. El guardián emite
**Verdict: BLOCK** y ese veredicto prohíbe un PROCEED.

Problemas que todos señalan:
1. **Objeto sin fijar.** La nota no está versionada. Todos los precedentes del proyecto (C1, C2a,
   C2b y el punto (3)) revisaron un candidato ya comprometido y citable por commit y blob
   (guardián, citando `reports/2026-09-22--c2b-independent-review.md` §2).
2. **§12 posterior al snapshot.** El addendum Liu–Chen se añadió tras la derivación y enlaza a un
   fichero sin versionar.
3. **Criterios de aceptación no congelados.** Más allá de las cuatro etiquetas del contrato, no
   hay regla de veredicto por fila y por nivel. Sin ella, la revisión es binaria: o un PASS que
   arrastra las 15 filas nuevas, o un REPAIR que tumba también A/B y (C1), que ya están probados.
4. **El eslabón más débil es §5.2.** La adaptación de los lemas de C2a a D de rango uno y a ζ_M
   se afirma por referencia y no se vuelve a derivar. Lo dicen los cuatro expertos y el
   falsificador.

**Dirección recomendada:** reparar la custodia y congelar la revisión *antes* de abrirla (§7).
Después, la revisión puede proceder sin reconvocar el comité completo; basta con que el guardián
confirme que se han cumplido los requisitos.

**Alternativas, por orden:**
1. (Recomendada) Commit dedicado de la nota sin tocarla, §12 excluido del alcance por escrito,
   criterios congelados, revisor nombrado con sus conflictos declarados, y revisión.
2. Separar §12 en otro fichero y después hacer commit. Deja el objeto más limpio, pero cambia el
   SHA256 atestiguado en esta sesión.
3. Revisar ya con el SHA256 como única ancla. Se descarta: rompe el estándar de custodia del
   proyecto y el guardián lo bloquea.

**Desacuerdos abiertos (no se ocultan):**
- **Gravedad del bloqueo.** El matemático y el analista numérico ven la nota lista para revisión
  "una vez versionada". El falsificador y el lógico exigen además congelar criterios por fila y
  una rederivación ciega de §5.2. El presidente se queda con la posición más exigente, porque la
  nota clasifica las 15 filas nuevas como «D» sin un solo OPEN y eso sube la carga de prueba.
- **Qué hacer con §12.** El guardián pide el commit *tal cual*, para conservar el SHA256. El
  físico y el falsificador piden sacar §12 del objeto revisado. Se pueden reconciliar: commit tal
  cual y exclusión de §12 escrita en los criterios de la revisión (alternativa 1).
- **Quién revisa.** El guardián admite a Claude Opus 5 (otra casa que el autor, Codex /root). El
  falsificador objeta que Claude Opus 5 revisó los lemas de C2a que §5 transfiere y fue autor del
  candidato C2b, y que Astra es de la casa Codex. Ningún revisor disponible carece de conflictos.
  **Es una decisión del usuario.**
- **Alcance ampliado.** Solo el falsificador pide incluir en el alcance dos cosas más: la
  dependencia de la nota C2 (`REPRESENTATION_DERIVED / PRELIMINARY`, sin revisión propia) y la
  frase de §9.2 que extiende el argumento a «cortes escalares» (`c2c:611`), que habría que
  revisar o retirar. Nadie lo contradice. El presidente lo incorpora.
- **Formulación.** El lógico propone decir que Lin=o(𝒬) es necesaria *y* suficiente para la
  componente PP, y escribir «a lo sumo ocho familias». Son cambios de redacción. Si se aplican
  antes del commit, cambian el SHA256; si no, quedan como puntos de revisión.

**Notas del verificador y del auditor de novedad:** todas las anclas prioritarias quedan
CONFIRMED. Hay un solo desplazamiento de línea (`CURRENT_STATE.md` :1649-1651, no :1655-1657), y
el contenido de Liu–Chen no se verificó. En cuanto a la novedad: el patrón +1:+1:−2 solo puede
presentarse como resultado condicional dentro de la clase declarada. (C1) es elemental. El
argumento de §9.2 es de tipo Paley–Wiener clásico. NOVELTY sigue OPEN.

**Límite de este dictamen:** los ocho miembros son de la familia Claude. Este informe no es, ni
sustituye, la revisión independiente que exige el contrato (falsificador, ataque 4).

## 7. Next-step spec

**Pasos reversibles**, que se pueden hacer ahora si el usuario lo pide y no cambian ningún estado
científico:
1. Redactar un borrador de *criterios de revisión C2c* (por ejemplo
   `theory/IR_C2C_REVIEW_CRITERIA.md`) con:
   - Objeto: la nota por commit y blob; §12 fuera de alcance.
   - Alcance: afirmaciones 1–4 de §11, el argumento de §9.2 (incluida la frase de `c2c:611`, que
     se revisa o se retira) y la dependencia de la nota C2 PRELIMINARY.
   - Regla de veredicto por fila y por nivel de S3. Se admite un PASS parcial. Un nivel sin
     resolver queda OPEN y nunca se absorbe en PASS ni en FAIL.
   - Lista de comprobación mínima:
     - rederivación lema a lema de §5.2 (lema angular (6), (17), (18), (19), (23)) con hDR_N y ζ_M;
     - todos los cruces Π₊DΠ₋ en (C8)–(C11);
     - los factores 64 y 512;
     - la definitud positiva de §7;
     - las igualdades «a lo sumo ocho» y 𝒞₀/𝒞₁;
     - la tabla de notación;
     - que Lin=o(𝒬) es necesaria y suficiente para PP.
   - Salvedades obligatorias en cualquier PASS: ganancia relativa N^{-1/4}, γ√N≈1.1 a N=24 y un
     N₀(M,D) no efectivo. Nada se lee a N finito.
   - Prohibiciones: ningún cálculo numérico; ni N=24/40, ni L−L_PP, ni Teorema 4.4.
2. Test mínimo de falsación (falsificador), incluido en los criterios. El revisor rederiva a
   ciegas, sin cálculo numérico, el emparejamiento lineal y la forma cuadrática de la fila más
   adversa (M=I, D₃=(I+σ₃)/2), partiendo de `f4f937e` y de la nota C2, **antes de leer §5.2**:
   - Luego compara con (C6), (C7) y (C14).
   - Tiene que listar todas las fases radiales y comprobar que todas son ≥γ y que ninguna es
     estacionaria.
   - Una fase estacionaria o un cruce sin controlar refutaría la ley N⁻³ en las filas de rango
     uno, sin afectar a A/B ni a (C1).

**Pasos comprometidos** (solo con autorización explícita del usuario):
3. Commit dedicado que contenga *solo* `reports/2026-09-22--c2c-structural-scope.md`, sin editarlo
   (SHA256 `f6266e95…d407fb5`). Los documentos FR1–FR3, Liu–Chen y el roadmap quedan fuera de ese
   commit, porque no están autorizados.
4. Congelar los criterios del paso 1, en un commit posterior al paso 3 y anterior a que el revisor
   lea la nota.
5. Nombrar al revisor y declarar sus conflictos por escrito (ver el desacuerdo sobre quién revisa).
   Opcional: el sanedrín como segunda voz de otra casa solo sobre §5.2, nunca como sustituto.
6. La revisión emite solo `C2C_PASS` (con alcance delimitado y por fila), `C2C_REPAIR_REQUIRED`,
   `C2C_FAIL` o `C2C_INCOMPLETE`. No se promociona nada en `CURRENT_STATE.md` sin una decisión
   posterior del usuario. No hay push.

Fuera de este plan queda la cuadratura certificada de G (λ_min>0). Podría falsar, pero no está
autorizada por el contrato y exigiría un ítem aparte.

## 8. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 9. Provenance
HERRAMIENTAS_COMMIT=ad16560
REPO_COMMIT=f4f937e
- Los miembros leyeron el motor en `ad16560`. El informe se validó con `e18a48a`, que solo fija
  en inglés las etiquetas que comprueba el validador y acepta su forma española; los prompts de
  los roles no cambian de fondo.
- Modelos por rol:
  - ola 1, en modo Explore: matemático, físico, lógico formal y analista numérico con `opus`;
  - ola 2, en modo Explore: falsificador con `fable`; guardián, verificador de literatura y
    auditor de novedad con `sonnet`.
- Presidente: Claude Opus 5.5.
- Composición de los prompts: por referencia (`SKILL.md`, paso 3).

## 10. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
