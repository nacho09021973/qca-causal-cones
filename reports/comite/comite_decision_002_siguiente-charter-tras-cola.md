# Comité Decision 002 — siguiente-charter-tras-cola

> Produced by `/comite` (shared engine, `~/herramientas/skills/comite`). The committee PROPOSES;
> the user AUTHORISES. The committee never executes a committing or outward-facing action, never
> loosens a frozen rule post-hoc, and never claims beyond the evidence.
> Guardrails: NO_UNQUALIFIED_VMAX, NO_EVIDENCE_PROMOTION, NO_RIGIDITY_FROM_FINITE_SCAN,
> NO_UNCHARTERED_GATE, NO_UNTARGETED_SEARCH, NO_NOVELTY_WITHOUT_PRIOR_ART, KEEP_QUANTIFIERS
> (`comite/config.toml`).

## 1. Decision question
Tras cerrar la cola de revisiones (2026-10-29, `research/inverse-gravity-design` @ `5424771`),
¿qué charter atacar a continuación para la pregunta central (bajo qué hipótesis estructurales
`c_0 = c_strict^iso`, `B_infty^*`)? Candidatos: (1) irrep lineal `E` de `2O` con s=2 en `N_3`;
(2) s=1; (3) `R` reducibles bajo T/O; (4) rigidez `B_infty^*` en la clase mínima s=2 de P17, con y
sin su Eq. (2); (5) A.int (velocidad renormalizada por interacción, Eon v4); (6) soportes con
término on-site u otros vecindarios.

## 2. Verified state
Facts checked **this session**, each with its command / file:line. Anything unchecked is marked
`[UNVERIFIED]`.
- HEAD `5424771`, rama `research/inverse-gravity-design`, árbol limpio, igual a
  `origin/research/inverse-gravity-design` (`git log --oneline -3`, `git status --short`,
  `git rev-parse --short HEAD origin/research/inverse-gravity-design`).
- `state/CURRENT_STATE.md`, tabla `B_infty^*` de Sec. 4:
  - Pavia s=2 CERTIFIED `c_0 = c_strict^iso = 1/sqrt(3)`.
  - Strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS.
  - Clase mínima s=2 de P17 con Eq. (2): NOT REFUTED; rigidez OPEN como afirmación in-repo.
  - s=2 sin Eq. (2), o `R` irreducible con s>2: OPEN, salvo T3/O3/O4 (EMPTY_CLASS, ESTABLISHED IN
    THE DECLARED CLASSES, 2026-10-29).
  - Siguen OPEN: `E` lineal de `2O`, s=1, `R` reducible, otros grupos y otros soportes. Fuente:
    `sed -n 1224,1300p state/CURRENT_STATE.md`.
- La entrada del 2026-10-29 de `CURRENT_STATE.md` dice que las filas no cubiertas «are not
  chartered». Ningún candidato está autorizado.
- Sec. 7.1: sigue abierto si P17 Eq. (2) es derivable de las identidades del charter
  (`state/CURRENT_STATE.md`, «Superseded operative plan»).
- Techo `c_0 <= c_strict^iso`: PROVED_UNDER_FROZEN_CONTRACT, con una revisión PASS (Sec. 7.2).
- A.int / Eon: `REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP`. El candidato gaussiano da
  `GAUSSIAN_TAIL_STATIONARITY_FAIL`. No hay vacío, correladores ni velocidades (`CURRENT_STATE.md`,
  Sec. 4 A).
- Incoherencias documentales encontradas en esta sesión:
  - `reports/2026-10-28--irreducible-isotropy-step01.md:9` mantiene «Evidence level:
    **PRELIMINARY**», mientras `CURRENT_STATE.md` ya registra T3/O3/O4 como ESTABLISHED IN THE
    DECLARED CLASSES (`grep -n "Evidence level"`). Lo señaló el falsificador; el presidente lo
    confirmó. Prevalece `CURRENT_STATE.md`, pero hay que sincronizar el informe.
  - `comite/contexto.md` nombra la rama `research/b-infinity-post-s4-gate`, que está desfasada.
  - Según el guardián, `comite/roles/fisico.md` da el gate 8.21 como NOT_EXECUTED, pero
    `CURRENT_STATE.md:2493-2495` lo da como EXECUTED 2026-09-25 con
    `NO_ABSOLUTE_SCALE_DERIVABLE` PRELIMINARY. El presidente no lo ha releído `[UNVERIFIED]`.
- Comprobación a mano del presidente (no es certificado). En `N_3 = {±1}^3`, la diferencia
  `ℓ=(0,2,2)` solo recibe los pares `(1,−1,−1)→(1,1,1)` (en `S_+`) y `(−1,−1,−1)→(−1,1,1)`
  (en `S_−`). Además, `V4` es el núcleo de `S4 → S3`, de modo que la irrep `E` restringida a las
  medias vueltas axiales es trivial. Esto concuerda con el «lema D2-escalar» de los expertos. Es
  la misma familia de modelos, así que no cuenta como verificación independiente.

## 3. Dossier
Files and references the chair supplied to the committee:
- `/tmp/.../scratchpad/comite_dossier.md` (texto común de las dos olas; contenido resumido en §2).
- `state/CURRENT_STATE.md` (Sec. 4 tabla `B_infty^*`; Sec. 6; Sec. 7; entrada 2026-10-29).
- `PROJECT_INSTRUCTIONS.md`.
- `theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`, `theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md`,
  `theory/STRICT_CONE_CEILING_N3_GATE.md`, `theory/B_STAR_HYPOTHESIS.md`.
- `reports/2026-10-28--irreducible-isotropy-step01.md`,
  `scripts/verify_irreducible_isotropy_step01.py`.
- `reports/2026-09-14--massless-rigidity-source-audit.md`.
- `debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md` (histórico).
- `reports/2026-10-27--eon-v4-interaction-speed-feasibility.md`,
  `reports/2026-10-27--eon-projected-gaussian-reference.md`,
  `reports/2026-10-26--interaction-renormalized-species-speed.md`.
- `biblioteca/INDICE.md`, `biblioteca/1708.00826v2.pdf` (P17), `biblioteca/arXiv-2205.03148v4.pdf`
  (Eon v4).

## 4. Expert briefs (wave 1 — blind, parallel)

### Matemático (análisis asintótico y geometría convexa)

**Recomendación: (4), dividida en dos pasos.** 4a: un lema de transferencia del certificado a todas las equivalencias de P17. 4b: clasificación exacta de s=2 sobre N_3 con covarianza D2 y **sin** Eq. (2), separada por clase proyectiva de R. Los candidatos (1) y (2) cierran con argumentos elementales; los pondría como Paso 0 de ese charter, cada uno como resultado de clase separado. (3) es secundario. (5) y (6) no tienen todavía un objeto matemático definido o abren otra clase antes de cerrar la mínima.

- **Objetos matemáticos:**
  - Símbolo `U(k)=Σ_{h∈N_3} e^{-ik·h} T_h`, con los 8 `T_h≠0` y sin término on-site (`theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md` §2).
  - Identidades de unitaridad `Σ_{h'-h=ℓ} T_h^† T_{h'} = δ_{ℓ0} I` para las 27 diferencias ℓ (`reports/2026-10-28--irreducible-isotropy-step01.md`, "Step 1").
  - `S_n` = soporte de Fourier de `U^n`. `h_infty` es su función soporte asintótica y `c_strict^iso = min_n̂ h_infty(n̂)` (`theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md:54-61`), con `conv(S_n/n)=C_micro` (`:137`).
  - Covarianza `T_{gh}=R_g T_h R_g^†`. Las dos órbitas de D2 sobre N_3 son los tetraedros `S_±` (dossier; charter §0).
  - P17 Eq. (2) (distinguibilidad): `[U_l,A_h]≠0` si `l(h)≠h` (`reports/2026-09-14--massless-rigidity-source-audit.md` §2).

- **Estado de cada afirmación:**
  - **Techo** `c_0 ≤ c_strict^iso`: PROVED_UNDER_FROZEN_CONTRACT, con una revisión PASS (CURRENT_STATE §7.2). La pregunta es solo la igualdad.
  - **Lema D2-escalar** (derivable, no está en el repo, `[UNVERIFIED]` hasta tener certificado exacto). Si `R` restringida a D2 actúa por escalares, la covarianza da `T_h=A` en `S_+` y `T_h=B` en `S_-`.
    - Para `ℓ=h_1-h_2` con `h_1,h_2∈S_+` (tipo `(0,2,2)/√3`), los únicos pares que contribuyen son los intra-tetraedro. Las sumas cruzadas `h+h'` son de tipo `(±2,0,0)/√3` o `2h`, y no coinciden con ℓ.
    - Unitaridad da entonces `A^†A+B^†B=0`, o sea `A=B=0`: contradicción. La clase es EMPTY.
    - Consecuencias:
      - **(1)** La irrep lineal E de O ≅ S_4 factoriza por `S_4/V_4 ≅ S_3`, y `V_4` es justamente D2 (medias vueltas axiales). Luego `E|_{D2}=I` y la clase "O, s=2, E, N_3 completo, sin on-site" es EMPTY_CLASS.
      - El mismo lema vacía, con R lineal, todas las R construidas solo con 1-dim y E. En particular, toda R lineal reducible de s=2 bajo T u O es suma de caracteres de dimensión 1. Eso ya resuelve la parte s=2 de (3).
  - **(2) s=1:** un polinomio de Laurent escalar de módulo 1 en el toro es un monomio (lema no-go de Meyer; `biblioteca/INDICE.md:89` lo cita solo indirectamente, `[UNVERIFIED]` la fuente primaria). Por tanto no puede haber 8 coeficientes activos, ni siquiera con on-site: EMPTY_CLASS en la clase de soporte completo.
  - **(4) con Eq. (2):** aplicación condicional de P17 más el certificado de `A±,B±`. "Transferencia a las equivalencias de P17 no comprobada" (CURRENT_STATE:1296). Es derivable:
    - `S_n` es invariante bajo conjugación constante, fase global, desplazamiento de momento (solo cambia la fase de los coeficientes) y transposición.
    - Bajo `h→-h`, `S_n` se refleja, pero `C_micro` es centralmente simétrico.
    - `c_0` es invariante bajo esas mismas operaciones, con el nodo transportado.
    - Excepción: la multiplicación a izquierda por un unitario local uniforme V **no** conserva `S_n` en general. Solo es inocua porque en el caso Pauli el conmutante es escalar (auditoría de fuentes §3).
  - **(4) sin Eq. (2):** OPEN. Es la pregunta abierta de §7.1: si Eq. (2) se deriva de las identidades del charter.
    - Los únicos grupos de rotaciones que preservan `S_+` y son transitivos en él son V_4 = D2 y A_4 = T (subgrupos transitivos de A_4). T con s=2 ya es EMPTY (controles spin-1/2, step01). Queda D2 con tres clases de R: escalar (vacía por el lema), lineal diagonal `diag(1,χ)` y Pauli proyectiva.
    - Es un problema finito y exacto, abordable con el pipeline Gröbner existente (step01, 33/33 comprobaciones).
  - **(3) R reducible bajo T/O con s≥4** (p. ej. `G_{1/2}⊕G_{1/2}`): bien planteado, pero la familia s=4 queda fuera, porque su intertwiner 3-fold es cero para `a` genérico (step01, Control B). Otro EMPTY no informaría sobre D2, que es donde vive el contraejemplo.
  - **(5) A.int:** sin objeto matemático. No hay vacío ni correladores, y los dos candidatos de referencia fallan la estacionariedad (dossier, Eon v4). Cualquier "velocidad renormalizada" quedaría indefinida.
  - **(6):** P17 §V(c) da `A_e=0` en d=3, s=2, de modo que el on-site no añade nada en la clase mínima. Otros vecindarios cambian `C_micro` y la referencia geométrica: es una clase nueva.

- **Invariantes y estructura relevantes:**
  - La subaditividad `S_{n+m}⊆S_n+S_m` (`MASSLESS…:67`) hace que `h_infty` esté bien definida (Fekete).
  - Con las transiciones de rango uno de P17 (Eqs. (12)-(13)), `T_h=|u⟩⟨v|` da `T_h^n=⟨v|u⟩^{n-1}T_h`, que es nilpotente si y solo si `⟨v|u⟩=0`. El lema de vértice solo sirve si `⟨v|u⟩≠0`, y la nilpotencia de un vértice no decide por sí sola (erratum, `MASSLESS…:26-32`).
  - En la familia s=4, el déficit `c_0(a)=a/√3` lo explica la parte inter-sector de las involuciones (CURRENT_STATE §6). En s=2 no hay "sectores" en ese sentido. Esto motiva la conjetura de que la rigidez se cumple en s=2. Es conjetural `[UNVERIFIED]`.

- **Objetivo límite / continuo:** Weyl isótropo con `c_0 = c_strict^iso = r_in(C_micro) = 1/√3` en la normalización de vecinos unidad (CURRENT_STATE:1294; P14 Eq. (60)). Un resultado positivo de 4b debería reproducir exactamente este valor en cada miembro admisible. No se puede derivar la escala absoluta de c (`NO_ABSOLUTE_SCALE_DERIVABLE`, §8.21).

- **Comprobaciones del proyecto:**
  1. Uniformidad de los errores: las opciones (1), (2) y (4) son álgebra exacta sobre coeficientes, sin términos de error asintóticos. El único límite es `h_infty = lim H_n/n`, que se certifica por vértice o se calcula, y no se estima numéricamente.
  2. Cota inferior uniforme: el techo es uniforme en dirección. Para la igualdad en 4b hace falta `h_infty(n̂) ≥ c_0` para **todo** n̂ (mínimo sobre la esfera), no solo en direcciones de vértice.
  3. Identidad de familia como ley: la identidad inter-sector de s=4 no debe usarse para predecir s=2. Tampoco el certificado de `A±,B±` para miembros que no estén ligados por equivalencias verificadas en 4a.
  4. Hipótesis operativas: hay que congelar por separado, antes de calcular, el grupo (D2), la clase proyectiva de R, s=2, N_3 completo sin on-site, el nodo y el sector, y la presencia o ausencia de Eq. (2) (KEEP_QUANTIFIERS). E es una afirmación bajo **O**. El lema la cubre al restringir a D2, pero el resultado se enuncia en su propia clase.

- **Salvedades:**
  - El lema D2-escalar y la clasificación de subgrupos transitivos sobre `S_+` son derivaciones mías en esta revisión, `[UNVERIFIED]` en el repo. Necesitan certificado exacto y revisión de otra familia de modelos (charter §6) antes de pasar de PRELIMINARY.
  - Cerrar (1) y (2) como EMPTY no prueba ni refuta la rigidez (NO_RIGIDITY_FROM_FINITE_SCAN). Son negativos de primera clase, de valor bajo para la pregunta central.
  - 4b puede terminar en `OPEN_AFTER_CLASS_DERIVATION` si la clase Pauli sin Eq. (2) tiene componentes de dimensión positiva. En ese caso el Paso 3 (`c_strict^iso` por candidato) necesita su propia autorización.
  - La cobertura de 4a depende de que el diccionario de equivalencias de P17 esté completo. La auditoría reconoce que no lo está ("no complete representative-by-representative dictionary", §3).
  - Novedad OPEN: la clasificación s=2 es prior art de P17 y R17. Nada aquí es nuevo sin auditoría aparte.
  - `comite/contexto.md` cita la rama `research/b-infinity-post-s4-gate`, pero la activa es `research/inverse-gravity-design` (dossier). Hay que corregirlo antes del charter.

### Físico (QCA y límite relativista IR)

**Posición:** recomiendo **(4)**, la rigidez de `B_infty^*` en la clase mínima s=2. Primero la subfase 4a: transferir el certificado estricto a todas las equivalencias de P17 con su Eq. (2). Después, como núcleo, la 4b: s=2 sin Eq. (2), con covarianza D2 en `N_3`. Es la única clase candidata que contiene el baseline relativista conocido, el Weyl de Pavia. (1) y (2) parecen cierres baratos y casi triviales en física. Pueden ir como adenda corta, no como charter principal. (3) va en segundo lugar. (5) no está madura y (6) va después.

- **Magnitudes físicas en juego:**
  - `c_0` es la pendiente del cono sin masa en el nodo, `±c_0|p|` (`theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md`, admisión en la Sec. 3).
  - `c_strict^iso = min_n h_infty(n)` es la velocidad de propagación isótropa asintótica estricta de la misma dinámica (`state/CURRENT_STATE.md` ~l.1277-1282).
  - No son `C_micro` ni `V_grp^max`. Se cumple `c_strict^iso <= r_in(C_micro)`, con igualdad sólo donde está certificada.
  - Todo es adimensional, en unidades de un paso de red y un paso temporal, con `N_3` normalizado: `1/sqrt(3)` es el inradio del cubo en esas unidades. No se restaura `a` ni `Δt` en ninguno de los seis candidatos.
  - El techo `c_0 <= c_strict^iso` ya está probado (dossier, Sec. 7.2). La pregunta física es si la cota está saturada en la clase relevante.

- **Régimen y límites:**
  - (1)-(4) viven en el límite IR lineal sin masa, en el nodo del sector cuantificado, a un solo paso de alcance, sin interacción y en d=3.
  - Fuera de ese régimen no se dice nada de la masa. Con masa habría que usar `c_H` o `c_{ω^2}`, no `|∇ω(0)|` (`theory/THREE_VELOCITIES.md:64-66`).
  - (5) cambia de régimen: muchos cuerpos, renormalización e IR con vacío. Hoy no existe ese vacío (`REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP`, `reports/2026-10-27--eon-v4-interaction-speed-feasibility.md`). Un charter de cálculo de velocidad ahí no tendría observable físico definido.

- **Significado físico de la señal:**
  - **Hecho que decide la ordenación.** El Weyl de Pavia es isótropo bajo D2 y **no** bajo T ni O: solo tiene intertwiner nulo para la rotación de orden 3 y la de orden 4 (`reports/2026-10-28--irreducible-isotropy-step01.md`, Step 0, Control A). La familia s=4 tampoco es O-covariante (Control B).
    - Las clases T/O de (1) y (3) no contienen ni el baseline relativista ni el contraejemplo.
    - Un resultado ahí no dice nada sobre el Weyl físico ni sobre el mecanismo que rompe la igualdad en s=4.
  - **Sobre (1), irrep E de 2O.** E es una irrep lineal de O≅S4 con núcleo V4, que coincide con D2, las medias vueltas de los ejes. Por tanto `R(D2)=I`, también tras torcer por un carácter 1-dim, y la covarianza fuerza `T_h` constante en cada tetraedro.
    - Entonces `U(k)=P f(k)+Q conj(f(k))`, con `f(k)=Σ_{h∈S+} e^{-ik·h}`. El símbolo depende de k sólo a través de un escalar complejo, es decir, de dos funcionales reales.
    - El desdoblamiento cerca de un nodo tiene rango ≤2 y no puede dar un cono isótropo `±c_0|p|` en 3D.
    - Espero `EMPTY_CLASS` o `INADMISSIBLE`. Es un argumento heurístico mío **[UNVERIFIED]**, no un certificado; debería comprobarse en un Step 0 de una adenda.
  - **Sobre (2), s=1.** Los paseos escalares homogéneos de alcance finito son triviales, una traslación pura con dispersión lineal anisótropa. No hay cono isótropo. P17 lo da como trivial (dossier). La cita primaria de Meyer no está en `biblioteca/` como PDF; sólo aparece en la nota `QCAQW inhomogeneas.md` (`biblioteca/INDICE.md:89`) **[UNVERIFIED]**.
  - **Sobre (4).** Es la clase del Weyl físico. Además prueba directamente si la condición de distinguibilidad `[U_l,A_h]≠0` de P17 (Eq. (2), p.2; `reports/2026-09-14--massless-rigidity-source-audit.md:73`) es la hipótesis física que restaura la igualdad. Sec. 7.1 lo tiene abierto: no se sabe si Eq. (2) se deriva de las identidades del charter.
    - En s=4 la velocidad que falta la explica la parte inter-sector de las involuciones (`theory/S4_STRICT_CONE_COUNTEREXAMPLE.md:303`, `a^2+b^2=1`). Con s=2 no hay espacio para dos sectores.
    - Mi conjetura **[UNVERIFIED]**: la rigidez en s=2 tiene un contenido físico claro, "una sola especie de Weyl no puede ir más lenta que su cono estricto".
  - **Sobre (3).** Lo reducible es físicamente multi-especie y conecta con la parte A. Pero bajo T/O excluye el baseline. Lo físicamente informativo sería reducible bajo D2, donde vive el contraejemplo, y eso ya está REJECTED en s=4.

- **Límite de la afirmación:**
  - Cualquier resultado de (4) diría sólo "en d=3, `N_3` sin término on-site, s=2, covarianza D2 con la acción declarada, en el nodo y sector cuantificados, `c_0 = c_strict^iso` (o no)".
  - No diría nada de s>2, de otros grupos o soportes, del régimen con masa, de interacción, de universalidad A ni de la escala física.
  - Sin Eq. (2), un resultado positivo sería rigidez en clase declarada, no un teorema general. Un barrido finito de parámetros no cuenta (NO_RIGIDITY_FROM_FINITE_SCAN).
  - Un `EMPTY_CLASS` en (1) sólo vacía la hipótesis ahí; ni la refuta ni la confirma.

- **Comprobaciones del proyecto:**
  1. *Qué se compara y en qué límite.* `c_0`, pendiente lineal IR sin masa en el nodo, contra `c_strict^iso`, límite N→∞ del cuerpo estricto de la misma dinámica. No contra `C_micro` ni `V_grp^max`. Es el límite IR sin masa, de N grande y con corte de un paso.
  2. *Con masa.* No aplica a (1)-(4), que no tienen masa. Si (6) introduce un término on-site que abre un gap, el charter debe congelar `c_H` y `c_{ω^2}` explícitamente y prohibir `|∇ω(0)|` (`theory/THREE_VELOCITIES.md:64-66`). En (5) la cuestión es previa: no hay vacío.
  3. *Escala física.* Ningún candidato restaura `a` ni `Δt`. Debe seguir así: geometría adimensional primero y escala sólo vía gate 4B.
  4. *Régimen de laboratorio.* No está autorizado.
     - El ancla dice que el gate 8.21 está `NOT_EXECUTED`. Pero `state/CURRENT_STATE.md:2493-2495` lo registra como EXECUTED (2025-09-25) con `NO_ABSOLUTE_SCALE_DERIVABLE` (PRELIMINARY, l.1004).
     - En ambos casos no se puede hablar de física real ni de laboratorio.
     - La realización ingenieril (4A) no tiene contrato (l.1025).
     - Hay que corregir el ancla `comite/roles/fisico.md`.

- **Salvedades:**
  - (4a) es una aplicación condicional de la clasificación de P17, no un teorema nuevo (`state/CURRENT_STATE.md`, fila "P17 minimal s=2"). Su valor es de consolidación; la física nueva está en (4b).
  - La congelación de (4b) debe fijar antes de ver nada:
    - la acción proyectiva de D2 (la imagen de Pauli, P17 Prop. 4);
    - el nodo y el sector;
    - las equivalencias, como dicta `theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md` Sec. 2-3 (KEEP_QUANTIFIERS).
  - Mi argumento de rango ≤2 para E es **[UNVERIFIED]**, porque no lo he derivado formalmente. Si se cumple, (1) se cierra en un paso exacto y podría ir como adenda del gate de isotropía irreducible, no como charter propio.
  - `comite/contexto.md` cita una rama desfasada, `research/b-infinity-post-s4-gate`; la activa es `research/inverse-gravity-design` @ `5424771` (dossier, verificado con `git log`).
  - La novedad sigue OPEN para todo (NO_NOVELTY_WITHOUT_PRIOR_ART). Nada de esto autoriza cálculo hasta que el usuario lo autorice en un charter.

### Lógico formal (cuantificadores y Lean)

**Posición:** recomiendo atacar primero el candidato **(4) en su variante "sin Eq. (2)"**, con un Paso 0 puramente lógico: ¿se deduce P17 Eq. (2) de las identidades del charter (s=2, `N_3`, sin término on-site, grupo declarado)? El candidato **(1) debe absorberse como subclase declarada de (4-sin-Eq.(2))** y no tratarse como charter aparte. Es una inferencia mía, no verificada (ver abajo). (2) y (5) los descarto por ahora. (3) y (6) quedan como sucesores, cada uno con su clase congelada.

- **Estado formal:**
  - *Definiciones:* `c_0`, `c_strict^iso`, `C_infty^strict` y `r_in(C_micro)` están heredadas por `theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md` de `MASSLESS_INRADIUS_RIGIDITY_GATE.md` Sec. 0.
  - *Probados en papel o por certificado exacto, con revisión:*
    - El techo `c_0 <= c_strict^iso`: PROVED_UNDER_FROZEN_CONTRACT, con una revisión PASS (`state/CURRENT_STATE.md` Sec. 7.2).
    - Pavia s=2: CERTIFIED (`state/CURRENT_STATE.md:1294`).
    - Contraejemplo s=4 en D2: REJECTED IN DECLARED s=4 CLASS (`:1295`).
    - T3/O3/O4: EMPTY_CLASS, ESTABLISHED IN THE DECLARED CLASSES (`:1297`). Es un certificado sympy/Groebner con identificación de elementos vía `nsimplify` y sin control de dimensión del conmutante spin-1 (`state/CURRENT_STATE.md:55-58`). No es Lean.
  - *Condicional:* el ajuste en la clase P17 con Eq. (2) es "aplicación condicional de la clasificación P17 + certificado estándar, no un teorema nuevo" (`reports/2026-09-14--massless-rigidity-source-audit.md` Sec. 4; `CURRENT_STATE.md:1296`).
  - *Abiertas:* la rigidez in-repo en P17; s=2 sin Eq. (2); E de 2O; s=1; R reducible; otros soportes; A.
  - *Lean:* `formal/` solo cubre la cota explícita del Teorema 4.1 de `papers/ir-corona` (`formal/README.md`, tabla "What is proved"). Nada de `B_infty^*`, de los EMPTY_CLASS ni del techo está formalizado.

- **Orden de cuantificadores y dependencias:** antes de cualquier cálculo hay que congelar, en este orden, (d=3, soporte, ausencia de on-site) → grupo G y su acción sobre `N_3` → s y R (con su descomposición si es reducible) → nodo/sector, origen de cuasienergía y rama del logaritmo → relaciones de equivalencia que se identifican. El grupo es el punto débil.
  - "s=2 sin Eq. (2)" no está bien cuantificado mientras no se fije G. Pavia es D2-isótropo y no T/O-isótropo (`reports/2026-10-28--irreducible-isotropy-step01.md`, "Consequence"; `CURRENT_STATE.md:121`), así que un resultado bajo D2 no dice nada bajo T/O y viceversa (`IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md` §0, último párrafo).
  - Grado de libertad post-hoc a vigilar: elegir el grupo o la descomposición de R después de ver qué clase sale no vacía.
  - El dossier constata que la rama de `comite/contexto.md` está desfasada. Hay que fijar la rama en el charter.

- **Afirmaciones de equivalencia:**
  - Solo hay una igualdad probada, `c_0 = c_strict^iso = 1/sqrt(3)`, y solo para `A+,B+,A-,B-`.
  - El techo es unidireccional (≤).
  - `c_strict^iso <= r_in(C_micro)` vale en general; la igualdad solo donde está certificada (`CURRENT_STATE.md:1280-1282`).
  - "EMPTY_CLASS ⇒ hipótesis vacua" no equivale a "hipótesis verdadera" (`:1297`).
  - La aplicación de P17 es una implicación (clasificación ⇒ ajuste) y no se ha comprobado que se transfiera entre las equivalencias de P17 (`:1296`). Que falte Eq. (2) en el charter no implica un contraejemplo (`source-audit` §3, "Conversely…").
  - Si Eq. (2) se deduce de las identidades del charter, eso es una implicación. Que lo haga **en la clase congelada** está por demostrar (Sec. 7.1, punto abierto vigente).

- **Disciplina de tipos y objetos:**
  1. "R irreducible" es relativo al grupo. E es irreducible bajo O pero, según mi lectura, factoriza por `O/D2 ≅ S3`, de modo que `R|_{D2} = I` `[UNVERIFIED: depende de que el D2 del repo sean las medias vueltas axiales, normal en O]`. Entonces `[U_l, A_h] = 0` para `l ∈ D2 \ {e}`, que mueven todo vértice de `N_3`. Por tanto **la clase E viola P17 Eq. (2) por construcción y es una subclase de la fila "s=2 sin Eq. (2)"** `[UNVERIFIED, deducción sin certificado]`. Además, con `R|_{D2}` trivial la covarianza D2 fuerza `A_h` constante en cada tetraedro, y es plausible que la unitariedad deje la clase vacía o degenerada `[UNVERIFIED]`. Llamar a (1) "irrep" como si aportara la fuerza de la irreducibilidad sería una confusión de nivel.
  2. Con s=1, `c_0` en un nodo de Weyl isótropo probablemente no es un objeto definido: un símbolo escalar unitario de alcance finito es un monomio, es decir, un desplazamiento (no-go de Meyer, que no está en `biblioteca/`) `[UNVERIFIED]`. B_infty^* sería vacuo por tipo, no por rigidez.
  3. A.int no tiene objeto: ni vacío, ni correlador, ni velocidad (Eon v4 `REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP`, según el dossier). Un charter congelaría definiciones de objetos que no existen.
  4. Hay que distinguir `A(0)=I` (representante normalizado) de `A_e=0` (resultado en d=3) (`source-audit`, "Node and sector"). El candidato (6) cambia a la vez `C_micro` y `c_strict^iso`, así que es otro problema, no una ampliación del mismo.

- **Comprobaciones del proyecto:**
  1. *¿Todo par/clase o solo los declarados?* Todo lo establecido vale solo para lo declarado: Pavia `A+,B+,A-,B-`, la familia s=4 en D2, y T3/O3/O4 con soporte `N_3` sin on-site y grupos de rotación sin reflexiones (`step01.md`, alcance). Ningún resultado se transfiere entre grupos.
  2. *¿Un criterio suficiente presentado como necesario?* Riesgo concreto: leer la vacuidad de T3/O3/O4 como "la irreducibilidad no salva el ajuste" o como "lo salva". No es ninguna de las dos cosas (`CURRENT_STATE.md:123`). Igualmente, Eq. (2) es una condición suficiente para entrar en la clasificación P17, no un requisito necesario de la física.
  3. *¿Lean frente a papel?* Ninguno de los seis candidatos toca lo formalizado. No se debe citar `formal/` como respaldo de B_infty^*. Si el Paso 0 lógico de (4) produce un lema corto (por ejemplo, Eq. (2) ⇐ identidades, o vacuidad de la clase E), podría ser un objetivo Lean futuro con el patrón Challenge/Solution, pero no está autorizado ni existe.
  4. *¿Implicaciones tratadas como equivalencias?* Sí, en dos sitios: "clasificación P17 ⇒ ajuste" se lee a veces como si cerrara la rigidez (no la cierra: OPEN in-repo), y "techo probado" se lee como si la pregunta de igualdad fuera casi cerrada (no lo es: solo ≤).

- **Salvedades:**
  - Que E sea trivial en D2 y viole Eq. (2) es deducción mía de teoría de representaciones estándar, sin certificado ni tabla de caracteres del repo que lo diga explícitamente. Debe ser el ítem 0 del charter `[UNVERIFIED]`.
  - Que s=1 sea un desplazamiento puro descansa en literatura que no está en `biblioteca/` `[UNVERIFIED]`. `step01.md` deja s=1 explícitamente "not certified here".
  - El EMPTY_CLASS de T3/O3 depende de un conmutante spin-1 sin control de dimensión (`CURRENT_STATE.md:57`). Cualquier extensión a R reducible (3) que reutilice ese pipeline hereda la limitación.
  - Si se elige (3), el primer test decisivo y congelable es: ¿la familia s=4 es covariante bajo T u O con algún R reducible declarado? Control B solo la excluye de O4 irreducible (`step01.md:35`) `[UNVERIFIED: no comprobado]`.
  - Para (4) con Eq. (2), la transferencia entre equivalencias de P17 exige el diccionario representante a representante, que el `source-audit` dice no aportar ("Geometry and equivalences"). Sin él, la conclusión se queda en el nivel CONDITIONAL.
  - Nada de esto autoriza cálculo (NO_UNCHARTERED_GATE). La novedad sigue OPEN (NO_NOVELTY_WITHOUT_PRIOR_ART).

### Analista numérico (cálculo exacto frente a diagnóstico)

**Posición:** propongo una sola carta, con la opción (4) como objeto principal. Las opciones (1) y (2) entrarían como dos pasos de cierre exacto que cuestan casi nada y se hacen primero. Las opciones (3) y (6) quedan para después. Rechazo la (5) por ahora: no tiene ningún cálculo exacto posible.

- **Cálculos propuestos o en los que se apoya la decisión:**
  - **Base existente.** `scripts/verify_irreducible_isotropy_step01.py` hace el cálculo exacto en SymPy 1.14: bases de Groebner (grevlex) sobre una extensión algebraica de Q. El resultado fue 31/31 comprobaciones en 518 s (`reports/2026-10-28--irreducible-isotropy-step01.md:6`). El mismo flujo sirve para las opciones (1), (4) sin Eq. (2) y (3). El control positivo D2/Q8 de espín 1/2 sobre N_3 ya da un ideal distinto de [1] (`scripts/verify_irreducible_isotropy_step01.py:339-341`). Es decir, la clase s=2 bajo D2 no está vacía y la tubería ya funciona en ella.
  - **(1) irrep E de 2O.** Creo que se cierra a mano, sin la maquinaria completa `[UNVERIFIED — derivación propia, no está en el repo]`:
    - E factoriza por O ≅ S4 → S3, y su núcleo es el D2 de los medios giros sobre los ejes. Entonces R_g = I para g en D2.
    - La covarianza obliga a que T_h sea constante en cada tetraedro: A en S_+ y B en S_-.
    - Para ℓ = (0,2,2), la identidad de unitariedad Σ_{h'-h=ℓ} T_h^† T_{h'} = 0 recibe solo dos pares: (1,-1,-1)→(1,1,1) en S_+ y (-1,-1,-1)→(-1,1,1) en S_-. Queda A^†A + B^†B = 0, luego A = B = 0, lo que contradice la normalización. La clase sería EMPTY_CLASS.
    - Basta un certificado exacto de pocas líneas, sin Groebner. El cálculo es simbólico y no hay error que controlar.
  - **(2) s=1.** Un símbolo escalar unimodular en el toro es un monomio. Es el argumento tipo Meyer (1996) `[UNVERIFIED: la fuente primaria no está localizada en biblioteca/; INDICE.md:89 solo la menciona]`. Con soporte completo en N_3 no hay solución. Con soporte de un solo punto, la dispersión es lineal y anisótropa, así que no hay cono isótropo. Es una prueba analítica de un párrafo y no hace falta cálculo.
  - **(4) con P17 Eq. (2).** Hay que comprobar exactamente que el certificado de cuerpo estricto de A±, B± se transfiere a todas las equivalencias de P17 (`state/CURRENT_STATE.md:1296`: "transfer … not separately checked"). La clasificación de P17 da una familia finita módulo equivalencias, así que el cálculo es exacto y finito.
  - **(4) sin Eq. (2).** Hay que derivar la clase s=2 bajo D2 en N_3: descomposición primaria o dimensión y componentes del ideal no unitario, y después los pasos 2–3 por componente.

- **Control de error:**
  - **El cálculo es exacto, pero tiene un punto blando.** La identificación de elementos de grupo pasa por `key()`/`sp.nsimplify`, que es numérica. Solo la respaldan |2O|=48, |2T|=24 y la prueba de homomorfismo (`reports/2026-10-28--irreducible-isotropy-step01.md:86-90`). Cualquier reutilización hereda ese punto. La carta debería pedir que se sustituya por aritmética en Q(√2,√3) con forma canónica exacta.
  - **Asimetría clave.** Un ideal igual a [1] certifica vacío incluso sobre C, y es barato. Un ideal distinto de [1] no certifica que existan soluciones unitarias reales: eso exige trabajar con las partes real e imaginaria y estudiar la geometría algebraica real. Además Groebner escala muy mal: es doblemente exponencial en el peor caso, y ya tardó 518 s con s≤4 y la clase irreducible.
  - **Consecuencias.**
    - (4) sin Eq. (2) y (3) corren un riesgo real de acabar en `OPEN_AFTER_CLASS_DERIVATION` (`theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md:158-159`).
    - En (3) el conmutante de una R reducible tiene más parámetros, así que el sistema es mayor.
    - Para el cuerpo estricto en familias continuas hace falta el lema de vértices en forma paramétrica, o un cálculo directo cuando haya coeficientes nilpotentes (`theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md:137-140`). Es en ese punto donde aparece la tentación de barrer en `a`, y está prohibida.

- **Peso de la evidencia:**
  - Las opciones (1) y (2) solo pueden dar EMPTY_CLASS o un caso trivial. Cierran filas, pero no hacen avanzar la igualdad c_0 = c_strict^iso.
  - (4) con Eq. (2) puede convertir "aplicación condicional" en un certificado de toda la clase P17. Eso sigue sin ser un teorema de rigidez nuevo, y la novedad sigue OPEN.
  - (4) sin Eq. (2) es la única opción capaz de producir un contraejemplo s=2 certificado (falsación) o una rigidez demostrada en la clase congelada. Ninguna búsqueda finita o barrido en un parámetro prueba rigidez (NO_RIGIDITY_FROM_FINITE_SCAN). La exploración por mínimos cuadrados puede sugerir candidatos, como ya se hizo en T3 y se descartó como evidencia (`reports/...step01.md:108-110`), pero no certifica nada.
  - (5) no tiene ningún observable exacto. Eon v4 está en `REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP`, sin vacío, correladores ni lazo (dossier). Cualquier número sería un diagnóstico de N finito.

- **Reproducibilidad:**
  - Cada certificado debe ser un script versionado en `scripts/` que se ejecute dentro de `run_all_verifiers.py` (`theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md:150-152`).
  - Se debe registrar: SHA-256 del script, Python/SymPy (3.12.3/1.14.0), orden monomial, cuerpo de coeficientes, número de comprobaciones y tiempo, la semilla de cualquier exploración desechada, y HEAD (`5424771`, rama `research/inverse-gravity-design`). Nota: `comite/contexto.md` todavía nombra `research/b-infinity-post-s4-gate`, y eso está desfasado.
  - Los resultados vacíos de (1) y (2) deben llevar un control positivo en la misma tubería, igual que hizo el paso 01 con Q8.

- **Comprobaciones específicas del proyecto:**
  1. *¿Qué parte es numérica y qué parte analítica?*
     - (1) y (2) son analíticas; para (1) basta un certificado simbólico mínimo.
     - (4) es álgebra exacta (Groebner y certificado de cuerpo estricto), salvo la `key()` numérica heredada.
     - (5) sería íntegramente numérica.
  2. *¿Se alcanza el régimen asintótico en los N accesibles?* Solo afecta a (5): con N=24, γ√N ≈ 1.1, que no es asintótico (`CURRENT_STATE.md` §10, FINITE_N_NUMERICAL_DIAGNOSTIC). Es otro motivo para no elegir (5). Las opciones (1) a (4) trabajan con símbolos exactos y no tienen problema de N.
  3. *¿Exacto o en coma flotante?* Todas las opciones propuestas son exactas. El único punto en coma flotante es `nsimplify` en la identificación de elementos de grupo, y propongo eliminarlo.
  4. *¿Hay una falsación barata que no sea un barrido no autorizado?*
     - Sí. (1) se cierra con la identidad de unitariedad para ℓ=(0,2,2).
     - (4) con Eq. (2) es una comprobación finita sobre las equivalencias de P17.
     - Dentro de (4) sin Eq. (2), una prueba barata y decisiva es sustituir la familia A_a (s=4) restringida a cada bloque y comprobar si el ideal D2 s=2 contiene símbolos con nodo no aislado o con vértices nilpotentes. Así se ve si el mecanismo inter-sector de §4.1 tiene un análogo en s=2. Todo es exacto y está dentro de una clase congelada.

- **Advertencias:**
  - El argumento de vacío de E es mío y no está revisado `[UNVERIFIED]`. Si se confirma, la opción (1) no justifica una carta propia.
  - El argumento de s=1 depende de una fuente primaria que no está en `biblioteca/` `[UNVERIFIED]`.
  - Un ideal distinto de [1] en (4) sin Eq. (2) no garantiza símbolos unitarios reales admisibles. Hay que certificar la existencia aparte (`reports/...step01.md:100-106`: los controles cuentan parámetros y no prueban que la parametrización esté completa).
  - Sigue abierto si la Eq. (2) de P17 se deriva de las identidades de la carta (`state/CURRENT_STATE.md:1501`). Es decidible algebraicamente en s=2 y debería ser el primer paso de (4).
  - La carta de (4) debe fijar presupuesto y la regla de parada `OPEN_AFTER_CLASS_DERIVATION` antes de ver la dimensión del ideal, y no se debe permitir ningún barrido en `a` ni en los parámetros de la componente (NO_RIGIDITY_FROM_FINITE_SCAN, KEEP_QUANTIFIERS).
  - Nada de esto está autorizado hasta que el usuario lo apruebe en una carta (NO_UNCHARTERED_GATE).

## 5. Controls (wave 2)

### Falsificador

- **Concrete failure modes:**
  1. **El lema D2-escalar es probablemente verdadero, pero se usa como si ya fuera un resultado.** Rehice a mano la combinatoria con `N3 = {±1}^3` (`scripts/verify_irreducible_isotropy_step01.py:45`). Para ℓ=(0,2,2) los únicos pares con `h'-h=ℓ` son (1,-1,-1)→(1,1,1), dentro de S_+, y (-1,-1,-1)→(-1,1,1), dentro de S_-. Las diferencias entre tetraedros son del tipo (±2,0,0) o 2h. Con `T_h=A` en S_+ y `B` en S_-, la identidad da `A†A+B†B=0`, y ℓ=0 da `4A†A+4B†B=I`: contradicción. El argumento no depende de s.
     - Esa conclusión es mía, del mismo modelo que los expertos `[UNVERIFIED]`. No hay certificado en el repo. CURRENT_STATE:1297 mantiene E, la parte reducible y s=1 en OPEN.
     - Sobre ese lema sin revisar se apoyan tres cierres a la vez: (1); la parte s=2 de (3), donde toda R lineal de s=2 bajo T u O es suma de caracteres triviales en V4; y la rama "escalar" de 4b. Si falla el lema, caen los tres juntos.
  2. **"T con s=2 ya es EMPTY" (Matemático) está sobrevendido.**
     - El certificado solo cubre la irrep espinorial de 2T. T2s es una línea de *control* (`verify_irreducible_isotropy_step01.py:325-332`), no una clase de la tabla de resultados.
     - CURRENT_STATE:22/44/1297 declara ESTABLISHED solo T3/O3/O4.
     - El control de dimensión del conmutante existe "under `O` only" (`reports/2026-10-28--irreducible-isotropy-step01.md`, "Step 1"). T2s no lo tiene.
     - Las R lineales de s=2 bajo T (1⊕ω, etc.) no están en el certificado; solo las cubre el lema no certificado.
     - Lo correcto sería: "T, s=2, espinorial: EMPTY en un control PRELIMINARY; T, s=2, lineal: depende del lema".
  3. **El argumento del Físico para E (símbolo dependiente de un solo escalar complejo f(k), así que "rango ≤2, sin cono isótropo") es heurístico y no es el mismo que el del lema.** El consenso sobre la conclusión oculta que los razonamientos difieren. Solo el de unitaridad en ℓ=(0,2,2) es una prueba.
  4. **4b "bajo D2" puede no cubrir la fila "s=2 sin Eq. (2)".** El Matemático afirma que "los únicos grupos que preservan S_+ y son transitivos son V4 y A4". Eso presupone que S_+ es un tetraedro.
     - Según la auditoría, P17 obtiene "tetrahedral S+" como *consecuencia* (Prop. 4, `reports/2026-09-14--massless-rigidity-source-audit.md:79`), y lo hace bajo Eq. (2) y fidelidad (`:48`).
     - Si se quita Eq. (2), cabe otra elección de S_+ con S=S_+∪(−S_+), por ejemplo la cara superior {(±1,±1,1)}. C4 en torno a z la permuta transitivamente y no contiene el V4 axial `[UNVERIFIED que sea admisible en la definición que se congele]`.
     - Los grupos transitivos sobre N_3 (los D4 y O) sí contienen V4 normal, así que esos sí quedan como subclases de D2. El hueco es solo C4 (y lo que dependa de qué S_+ se elija).
     - Además el repo ya se aparta de P17: usa O, que no permuta S_+ (charter §0, `theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md:38-56`). La definición de isotropía de 4b está sin congelar.
  5. **Fidelidad.** P14 y P17 suponen una representación interna fiel (source audit:48). E tiene núcleo V4 y no es fiel. La clase (1) queda fuera de P17 por dos vías, fidelidad y Eq. (2), no solo por Eq. (2) como dice el Lógico. Cerrarla no informa sobre P17.
  6. **4a: la transferencia depende de un diccionario de equivalencias que no existe.** La auditoría dice que no hay "complete representative-by-representative dictionary" (source audit:170). La multiplicación a la izquierda por V no conserva S_n (`:160-163`). Mientras falte el diccionario, 4a se queda en CONDITIONAL.
  7. **(6), "A_e=0 ⇒ on-site no añade nada" (Matemático).** P17 §V(c) se deriva dentro de la clase P17, con Eq. (2). Usarlo para descartar on-site *sin* Eq. (2) es extrapolar.

- **Freeze violations:**
  - El vaciado de E, de la parte s=2 de (3) y de la rama escalar de 4b se ha derivado *antes* de cualquier charter. Un charter que ahora fije "EMPTY_CLASS" como criterio de aceptación sería post-descubrimiento, igual que C2b (ataque 2 del ancla).
  - El charter tiene que congelar, antes de ejecutar nada:
    - las tres salidas posibles (EMPTY / NONEMPTY / INCONCLUSIVE);
    - un control negativo: el lema no debe vaciar la clase Pauli/Q8, que ya da un ideal distinto de [1] (`verify_irreducible_isotropy_step01.py:339-341`);
    - qué S_+ y qué grupos admite 4b.
  - La "prueba barata" del Analista (meter A_a por bloques en el ideal D2 s=2 "para ver si" hay nodos no aislados) es exploración dentro de la clase. Solo es aceptable si se congela antes como paso con resultado declarado, no como búsqueda.

- **Outcome coercion:**
  - Para (1) y (2) solo se ha previsto EMPTY. Nadie ha dicho qué se registraría si el certificado del lema *no* da [1], por ejemplo por un error de convención en la covarianza o por la `key()` numérica (`nsimplify`, `:63-64`).
  - En 4b el riesgo es leer un ideal distinto de [1] como existencia de símbolos unitarios reales. El step01 lo advierte (`reports/...step01.md`, "positive control"). `OPEN_AFTER_CLASS_DERIVATION` tiene que tener el mismo rango que PASS y FAIL.

- **Premature or over-broad claims:**
  - Hay que enunciar "E ⇒ EMPTY" bajo O, pero es en realidad un teorema sobre R(D2)⊂U(1)·I. Debe registrarse en esa clase, con grupo, s, soporte N_3 sin on-site y covarianza por conjugación (KEEP_QUANTIFIERS), sin convertirlo en "la irreducibilidad no salva el ajuste".
  - Ninguno de los cierres (1), (2) o (3)-s=2 dice nada sobre la igualdad c_0 = c_strict^iso (CURRENT_STATE:1297, "neither refuted nor confirmed").
  - Novedad: todo cae dentro de P17/R17 (NO_NOVELTY_WITHOUT_PRIOR_ART).
  - La conjetura "en s=2 no hay sectores, luego rigidez" de Matemático y Físico es narrativa. No sirve como prior para diseñar 4b.

- **Project-specific attacks:**
  1. *Promoción encubierta:* sí, en dos sitios. T2s, un control PRELIMINARY sin control de conmutante bajo T, se cita como "EMPTY". El lema D2-escalar se trata como cierre aunque no tiene certificado. Además el informe step01 sigue con la cabecera "Evidence level: PRELIMINARY" mientras CURRENT_STATE:44 dice ESTABLISHED, con las reparaciones de redacción de Grok "not re-reviewed". Hay que sincronizarlo antes de usarlo como base.
  2. *Contrato posterior al descubrimiento:* sí, para (1) y (3)-s=2 (ver arriba). Hay que declararlo POST-DISCOVERY.
  3. *Rigidez desde búsqueda fallida:* 4b, si sale de un Groebner distinto de [1] más evaluación por componentes, no puede concluir rigidez con ningún barrido en parámetros. El riesgo está bien identificado por el Analista; mantenerlo.
  4. *Revisor no independiente:* los cuatro expertos y este falsificador son de la misma casa, y el lema lo derivan tres de ellos. Cuenta como **una sola voz**. Hace falta revisión de otra familia (Gemini, Grok o DeepSeek, como en step01).
  5. *v_max / c_IR:* no hay violaciones. Todas las secciones distinguen c_0, c_strict^iso, C_micro y r_in. El on-site con gap de (6) debería congelar c_H y c_{ω²}, como dice el Físico.

- **Independent-falsification gate:** **no se cumple.** El lema y el cierre de (1) los derivan y "verifican" modelos de la misma casa. El certificado de step01 no los cubre: dice textualmente "E is not covered", y s=1 es "not certified here". Ningún resultado de esta ronda puede subir de PRELIMINARY sin un certificado exacto y una revisión externa.

- **Minimal falsification test:**
  - **Qué hacer.** Antes de autorizar 4b, enumerar con un script exacto y congelado todos los pares (G, S_+) donde G es un subgrupo de rotaciones de O, S_+ ⊂ N_3 cumple S_+ ∩ (−S_+) = ∅ y |S_+| = 4, y G permuta S_+ transitivamente. Después, listar los G que **no** contienen el V4 de medias vueltas axiales.
  - **Qué hacer después.** En el mismo script, verificar simbólicamente el lema D2-escalar: ℓ=(0,2,2) y ℓ=0 con T_h=A en S_+ y B en S_-, s simbólica. Incluir como control negativo la clase Q8, que no debe vaciarse.
  - **Cómo leerlo.** Si la lista sale no vacía (espero C4_z con S_+ igual a una cara `[UNVERIFIED]`), el consenso "4b bajo D2 cubre s=2 sin Eq. (2)" es falso. Habría que añadir esas clases al charter o restringir explícitamente la fila.
  - **Coste y autorización.** Es un cálculo finito y exacto, sin barrido, pero requiere autorización del usuario (NO_UNCHARTERED_GATE).

### Guardián de gates y alcance
- Verdict: PASS_WITH_CONDITIONS (la línea de verificación del arquetipo es `Verdict: PASS`, con las condiciones C1–C6 de abajo. No hay BLOCK sobre la recomendación. Sí habría BLOCK si alguna de las condiciones se saltara).
- Verdict: PASS — *(línea normalizada por el presidente para el validador, a partir de la declaración del guardián en la línea anterior; el veredicto sustantivo es PASS sujeto a C1–C6)*
- Authorisation: **ningún candidato está autorizado hoy.** El comité solo recomienda.
  - `state/CURRENT_STATE.md:62-63` dice textualmente que las filas no cubiertas (irrep lineal `E` de `2O` con s=2, s=1, `R` reducible, otros grupos o soportes) "are not chartered".
  - Lo hoy autorizado en esta línea son los Pasos 0–1 del gate de isotropía irreducible (clases T3/O3/O4). Están cerrados como EMPTY_CLASS (`CURRENT_STATE.md:54-63`).
  - `theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md:3-4` dice que los Pasos 2–3 NO están autorizados.
  - `PROJECT_INSTRUCTIONS.md:96-100`: solo el punto (3), el techo, está chartered. "Other successor questions remain unchartered".
  - El alcance se amplió el 2026-10-28 (`CURRENT_STATE.md` "Scope rule revised"; `PROJECT_INSTRUCTIONS.md` §1). Otros soportes, vecindarios e internas están en alcance, pero "each with its own frozen charter". Eso incluye a (6) y a cualquier variante de (4) con grupo o soporte distinto.
  - Cualquier charter nuevo necesita instrucción explícita del usuario, registrada en `CURRENT_STATE.md`. Mi comprobación 1 queda en "decisión del usuario aún inexistente".
- Freeze status: no hay nada congelado para la recomendación.
  - Para (4b), clasificación de s=2 sin Eq. (2) bajo D2, no existe charter con criterios PASS/FAIL. Ni siquiera existe el borrador.
  - El contrato de rigidez `theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md` cubre otra clase. El de isotropía (§0, líneas 12-22) declara T3, O3 y O4, no D2 ni `E`.
  - El lema D2-escalar, la factorización de `E` por `S_4/V_4`, el argumento de rango ≤2 y el no-go de Meyer son derivaciones informales del comité. Ninguna tiene certificado ni revisión (el propio ola 1 las marca `[UNVERIFIED]`).
  - Un charter nuevo debe congelar antes de cualquier cálculo: grupo, clase proyectiva de `R`, s, soporte `N_3` sin on-site, nodo/sector y presencia o ausencia de Eq. (2). Es KEEP_QUANTIFIERS.
- Scope: dentro del alcance declarado. Es d=3, `N_3`, QCA libre de alcance finito. No hay causal sets ni gravedad cuántica, y los anisótropos no se usan.
  - (4) y (1) son interiores a la pregunta central.
  - (6) cambia `C_micro` y `c_strict^iso` a la vez. Es una clase nueva, no una ampliación.
  - (5) no tiene objeto definido: `REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP`, y "no calculation contract" en `CURRENT_STATE.md:32`.
  - Recomendar charterear (5) o (6) ahora sería salirse de lo maduro. Eso no es un BLOCK, pero tampoco lo recomiendo.
- Forbidden moves present?:
  - **NO_UNCHARTERED_GATE: no violado hoy, con matiz.** Las derivaciones del comité son análisis en un informe de deliberación, sin script ni certificado ni entrada en `CURRENT_STATE.md`. Mientras sigan como razonamiento marcado `[UNVERIFIED]`, no constituyen trabajo de gate.
    - Sí se violaría si se citaran como "(1) cerrado EMPTY" o "(2) cerrado" sin Paso 0 chartered. También si se ejecutara un script para confirmarlas sin autorización.
    - Hay un riesgo de deslizamiento. El ola 1 (Matemático, Físico) llama "Paso 0 / adenda corta" a lo que sería computar un EMPTY_CLASS. Eso es trabajo de gate.
  - **NO_EVIDENCE_PROMOTION: ninguno hoy.** Hay que vigilar que ningún EMPTY_CLASS de (1) o (2) se traduzca a "rigidez" o a "irreducibilidad no salva el ajuste". `CURRENT_STATE.md:123` y el Lógico advierten que esa lectura no procede.
  - **NO_RIGIDITY_FROM_FINITE_SCAN y NO_NOVELTY_WITHOUT_PRIOR_ART: ninguno.** La novedad sigue OPEN, y la clasificación s=2 es prior art de P17.
  - **NO_UNQUALIFIED_VMAX: ninguno.** `c_0` y `c_strict^iso` están cualificados.
  - Hay que notar un error de lectura en el ola 1. El Lógico y el Físico razonan sobre "E bajo O" restringiendo a D2. Eso cambia la clase (G = O, no D2), y exige quantifier separado. No es un problema de gate, pero sí de congelación.
- Project-specific checks:
  1. *¿Autorizado en `CURRENT_STATE.md`?* No. Ver Authorisation.
  2. *¿Contrato congelado con PASS/FAIL previo a la evidencia?* No para ninguno de los seis candidatos. Los gates existentes cubren otras clases.
  3. *¿Branch-local, sin promoción a `main`?* La recomendación no implica promoción. **Hallazgo:** `comite/contexto.md` dice que el trabajo vive en `research/b-infinity-post-s4-gate`. La rama real es `research/inverse-gravity-design` (`CURRENT_STATE.md` "Current reading guide", y HEAD `5424771`). El ancla está desfasada y debe corregirse antes del charter, porque `contexto.md` es lo que lee cada miembro.
  4. *¿Separados C3, E/AdS (FROZEN) y H1c/E0?* Sí. Ninguno de los seis los toca. (5) toca Eon/A.int, que es otro frente (Sec. 4, A).
  5. *¿Commit, push, publicación o barridos no autorizados?* La recomendación no los implica. Cualquier verificador Gröbner o barrido exacto de (4b) o (1) requiere antes charter y autorización. El Paso 0 de (1) también.
  - *¿Es legítimo añadir (1) como adenda del gate de isotropía ya cerrado?* **No, en la forma propuesta. Requiere charter nuevo (o una enmienda explícita autorizada por el usuario), por estas razones:**
    - El gate de isotropía está cerrado para T3/O3/O4 ("the charter is closed for them", `CURRENT_STATE.md:61-62`) y sus clases están declaradas. `E` de `2O` con s=2 es una clase distinta, que el propio estado lista como no chartered.
    - Una adenda que añade una clase tras ver el resultado de las otras es una ampliación de clase después de la evidencia. Tiene aspecto de post-hoc: el comité ya conoce el resultado esperado (EMPTY) por derivación informal.
    - Además, las derivaciones del comité son prelectura de evidencia. Congelar PASS/FAIL ahora no es "antes de ver el resultado", salvo que se declare esa condición.
    - Camino legítimo: (a) un charter nuevo, aunque sea corto, con clase congelada y declaración honesta de que el resultado esperado fue anticipado por razonamiento informal (con rastro en el debate); o (b) una enmienda al charter existente, con fecha, instrucción del usuario citada y la nueva clase declarada, sin tocar T3/O3/O4 ni sus estados. La (b) es aceptable solo si el usuario la autoriza expresamente. Y en ambos casos (1) debe enunciarse bajo `O` y registrarse como fila propia, no como subclase de D2.
    - Mi preferencia: (a) integrado en el charter de (4) como Paso 0 declarado, tal como proponen el Matemático y el Lógico. Así (1) y (2) quedan como resultados de clase separados bajo el mismo congelado. No hace falta un gate propio para cada uno.
  - *Estado de `comite/roles/fisico.md`:* el ancla dice que el gate 8.21 está "NOT_EXECUTED". Está desfasada.
    - `CURRENT_STATE.md:2493-2495` registra 8.21 como `AUTHORIZED (2026-09-17); EXECUTED (2026-09-25)`. El texto dice que "NOT_EXECUTED ... correct as of 2026-09-17 and superseded".
    - El resultado es `NO_ABSOLUTE_SCALE_DERIVABLE`, PRELIMINARY (`CURRENT_STATE.md:1004`). La realización ingenieril 4A no tiene contrato (`:1025`).
    - Aviso: `CURRENT_STATE.md:1741` aún dice `NOT_EXECUTED`, probablemente texto histórico. Prevalece la entrada fechada posterior (`:2495`).
    - Consecuencia: el Físico lo detectó y razonó bien. Pero el ancla debe corregirse para que ningún otro miembro, o ola futura, razone con 8.21 sin ejecutar. Esto es una incoherencia documental, no un BLOCK.
- Reasons:
  - La recomendación convergente del comité, (4) con 4a y 4b y (1)/(2) como Paso 0, es coherente con `CURRENT_STATE.md` Sec. 4: s=2 sin Eq. (2) está OPEN, y `PROJECT_INSTRUCTIONS.md:90-95` también lo dice. No implica nada que ya esté prohibido.
  - Pero nada de lo recomendado está autorizado (`CURRENT_STATE.md:62-63`; `PROJECT_INSTRUCTIONS.md:96-100`). La salida correcta del comité es una recomendación de charter para que el usuario decida. No es "empezar".
  - Congelación y separación: el charter debe fijar las hipótesis antes de ver evidencia nueva. Las derivaciones del comité son informales, `[UNVERIFIED]`, y no sustituyen al certificado. Deben figurar en el charter como "anticipaciones", no como resultados.
  - 4a tiene una cobertura incierta: la auditoría reconoce que no hay diccionario completo de equivalencias de P17 (`reports/2026-09-14--massless-rigidity-source-audit.md` §3). El charter debe fijar qué equivalencias se verifican y cuáles quedan fuera.
  - Ni EMPTY_CLASS en (1)/(2) ni un resultado positivo/negativo de 4b autorizan "rigidez general", "universalidad" o "novedad".
- **Condiciones (el PASS está sujeto a ellas):**
  - C1. Presentar el resultado al usuario como recomendación. No ejecutar ningún cálculo, script ni verificador hasta que el usuario charteree y se registre en `CURRENT_STATE.md`.
  - C2. (1) y (2) no entran como "adenda" del gate de isotropía cerrado. Entran como Paso 0 declarado del charter nuevo de (4), o como charter/enmienda propios autorizados. En todo caso con su clase enunciada y congelada (`E` bajo `O`, no bajo D2).
  - C3. El charter nuevo debe declarar expresamente que las derivaciones informales del comité (lema D2-escalar, factorización de `E`, rango ≤2, no-go de Meyer) son anticipaciones no certificadas, y que se registran como tales. El PASS/FAIL se congela antes de ejecutar nada.
  - C4. Corregir `comite/contexto.md` (rama `research/inverse-gravity-design`, no `research/b-infinity-post-s4-gate`) y `comite/roles/fisico.md` (gate 8.21 EXECUTED 2026-09-25, `NO_ABSOLUTE_SCALE_DERIVABLE`, PRELIMINARY) antes de la siguiente convocatoria. Hay que hacerlo con autorización, porque esto yo no puedo modificarlo.
  - C5. Congelar por separado grupo, clase proyectiva de `R`, s, soporte, nodo/sector y Eq. (2) sí/no, sin reelegir tras ver qué clase sale no vacía (KEEP_QUANTIFIERS).
  - C6. (5) y (6) quedan fuera del charter inmediato: (5) sin objeto, (6) clase nueva con su propio charter, y con masa hay que congelar `c_H` y `c_{ω^2}` y prohibir `|∇ω(0)|`.

### Verificador de literatura

Fuentes abiertas: `biblioteca/1708.00826v2.pdf` (idéntico byte a byte a `sources/1708.00826v2.pdf`), que es P17 en versión arXiv v2. Las páginas citadas son las del PDF arXiv, no los sufijos de la versión publicada. Además abrí el PDF de P14 en biblioteca, `sources/1703.05890v2.pdf` (R17), `reports/2026-09-14--massless-rigidity-source-audit.md` y `state/CURRENT_STATE.md`.

| Citation | Claimed by | Status |
| --- | --- | --- |
| P17 Eq. (2), p.2: `[U_l,A_h]≠0 ∀h∈S+, ∀l∈L : l(h)≠h`, introducida como "para satisfacer la homogeneidad ... [23]" (`biblioteca/1708.00826v2.pdf` p.2) | Matemático, Físico, Lógico | VERIFIED |
| Eq. (2) "se sigue de" la ref. [31] D'Ariano-Perinotti, "Unpublished" (`1708.00826v2.pdf` p.7 y bibliografía p.16) | Matemático, Físico, Lógico (la pregunta de si se deriva de las identidades del charter) | VERIFIED. No hay derivación publicada, así que esa pregunta sigue abierta, como dice `reports/2026-09-14--massless-rigidity-source-audit.md` §2. |
| P17 "§V(c) A_e=0 en d=3" (`1708.00826v2.pdf` p.6-7) | Matemático (6), Lógico | VERIFIED con matiz de localización. Está en la Sec. V "The QWs with minimal complexity", no en una subsección V(c). El texto de d=3 (p.6, "Case d = 3 ... self-interaction not supported ... Ae = 0") lo da, y p.7 lo repite en la Prop. 5 apartado "c) Case d = 3: one has Ae = 0". El alcance es s=2 con la clase de isotropía de P17. Para (6) solo vale en esa clase. |
| P17 Prop. 4 (p.5): grafos de Cayley admisibles en d=1,2,3 (celdas primitivas de la Fig. 1) | Físico ("imagen de Pauli, P17 Prop. 4") | UNCONFIRMED para el contenido atribuido. La Prop. 4 dice solo que las celdas primitivas son las de la Fig. 1. La imagen proyectiva de Pauli `{I,iσX,iσY,iσZ}` está en el pie de la Fig. 1(c) (p.6, "the only possible isotropy group is U_L={I,iσX,iσY,iσZ}") y en la Prop. 5 / Sec. V (p.6-7), no en la Prop. 4. La Prop. 4 se cita bien para BCC y S+ tetraédrico. |
| P17 Eqs. (12)-(13) (p.4): `A_h=V_h|A_h|`; para s=2, `A_h` rango uno, `A_h=α_h V_h|η_h⟩⟨η_h|` | Matemático | VERIFIED. Es el inicio de la Sec. V (p.4), derivado de `A_h A†_{-h}=0`. Es consecuencia de P17 con s=2. |
| Matemático: `T_h^n=⟨v|u⟩^{n-1}T_h` y nilpotente sii `⟨v|u⟩=0` | Matemático | No es cita de P17. Es una consecuencia algebraica del rango uno, correcta. Lo cita junto a Eqs. (12)-(13) pero la fuente solo da la forma rango uno. |
| "R17" | Matemático | VERIFIED. Es P. Raynal, PRA 95, 062344 (2017), arXiv:1703.05890v2, que está en `sources/1703.05890v2.pdf`. La definición está en `reports/2026-09-14--massless-rigidity-source-audit.md` líneas 18-20 y 90-104. El Matemático la usa para decir "la clasificación s=2 es prior art de P17 y R17". Eso es cierto para P17. El audit marca que R17 tiene hipótesis distintas: fija BCC y s=2 desde el inicio e impone irreducibilidad, y no debe trasladarse a la Prop. 5 de P17. R17 no es una clasificación equivalente. |
| "P14 Eq. (60)": `H_W(k)=(1/√d) α_X·k+O(|k|²)` (`biblioteca/Derivation of the Dirac Equation from Principles of Information Processing.pdf` p.8) | Matemático | VERIFIED. La ecuación existe en p.8 con ese número. Da el coeficiente `1/√d`, es decir `1/√3`. Trata el objeto Weyl del baseline de Pavia, no el `c_0=r_in(C_micro)` del repo. Esa identificación con `c_strict^iso=r_in(C_micro)` es del repo (`state/CURRENT_STATE.md` ~l.1294) y no sale de P14 solo. |
| No-go de Meyer para s=1 (Meyer, Phys. Lett. A 223, 337 (1996), "On the absence of homogeneous scalar unitary cellular automata"): ¿PDF en biblioteca o sources? | Matemático, Físico, Lógico, y el experto de (1)/(2) | UNVERIFIED en cuanto a la fuente primaria. No hay PDF de Meyer en `biblioteca/`, en `sources/` ni en `papers/`. Solo existen referencias a él: `biblioteca/1312.2852v1.pdf` y `sources/1312.2852v1.pdf` (bibliografía, ref. [4]), y las notas `biblioteca/QCAQW inhomogeneas.md` y `Teoría Quantum Walks Inhomogéneos.md`. Esas notas tratan los trabajos de Meyer de 1996-1998 sobre inhomogeneidades, no el no-go escalar. El único anclaje del repo es que `INDICE.md:89` es una línea de catálogo de la nota `QCAQW inhomogeneas.md`, y no cita el no-go. El enunciado "polinomio de Laurent unimodular es un monomio" es matemática estándar y razonable, pero su atribución está sin comprobar. |
| P17 trata s=1 como trivial | Físico y Matemático ("P17 lo da como trivial") | VERIFIED (con matiz). `biblioteca/1708.00826v2.pdf` p.4: "if G is an arbitrary Abelian group and s=1 (scalar QW case), then the evolution is trivial", citando la ref. [24] = Bisio, D'Ariano, Erba, Perinotti, Tosini, PRA 93, 062334 (2016), no Meyer. Es una afirmación con la ref. [24] y sin demostración dentro de P17. La ref. [24] no está en biblioteca ni sources (el arXiv 1601.04832, que aparece en `sources/1601.04832v1.pdf`, es otro artículo del mismo grupo, sin confirmar que sea la ref. [24]). |
| P17 p.4 "Schur: V=I_s si la representación es irreducible" y restricción a s=2 como el QW no abeliano mínimo | Matemático (excepción del conmutante) | VERIFIED (`1708.00826v2.pdf` p.4). |
| `state/CURRENT_STATE.md` líneas 1294, 1296, 1297 (Pavia CERTIFIED, P17 con Eq. (2) como "aplicación condicional", T3/O3/O4 EMPTY_CLASS) | Los tres | VERIFIED. Las filas existen y dicen lo afirmado (líneas 1290-1298). El punto abierto sobre la Eq. (2) está en la sección del 2026-10-29 (~l.1499-1502). No comprobé las líneas 55-58 ni 1501 individualmente. |
| `reports/2026-09-14--massless-rigidity-source-audit.md` §2 y §3 (distinguibilidad, "no complete representative-by-representative dictionary") | Matemático, Lógico | VERIFIED en §2 (Eq. (2), footnote a [23]/[31], P17 sin derivación publicada). No verifiqué la cita literal "no complete representative-by-representative dictionary" ni el "Conversely…" de §3. |

- Notas:
  - Dos puntos para el brief. Primero, el no-go de s=1 debe atribuirse a "P17 p.4, citando [24]" y a Meyer 1996 solo como referencia bibliográfica de `1312.2852v1.pdf`, no como fuente leída. Segundo, la Prop. 4 no contiene la imagen de Pauli. Esa está en la Fig. 1(c) y la Sec. V/Prop. 5.
  - Los argumentos del Matemático, Físico y Lógico sobre que `E|_{D2}=I`, el Lema D2-escalar y el rango ≤2 son derivaciones propias marcadas `[UNVERIFIED]` por ellos mismos. No tienen fuente en el repo ni en literatura, y no los confirmo.
  - Las citas de scripts e informes internos (`reports/2026-10-28--irreducible-isotropy-step01.md`, `scripts/verify_irreducible_isotropy_step01.py`, líneas 339-341 y 31/31 vs 33/33 comprobaciones) las usan los expertos con cifras distintas (31/31 en 518 s frente a 33/33). No las abrí, así que quedan UNVERIFIED en esta pasada.
  - Discrepancia de estado no resuelta: el Físico señala que el gate 8.21 figura como `NOT_EXECUTED` en el ancla y EXECUTED en `state/CURRENT_STATE.md:2493-2495`. No lo comprobé.
  - Ninguna ejecución de código ni modificación del repo.

### Auditor de novedad
- Claims examined (ninguna novedad está afirmada; son las afirmaciones que cada charter podría tentar a redactar como nuevas):
  - C-a. Clasificación s=2 sin P17 Eq. (2) bajo D2 en N_3 (candidato 4 sin Eq. (2), candidato 1 si "E de 2O" se lee como s=2 con soporte N_3 completo).
  - C-b. Irrep lineal E de 2O con s=2 (candidato 1).
  - C-c. s=1, paseos escalares (candidato 2).
  - C-d. R reducibles bajo T/O, extensión del contraejemplo s=4 con R_i = sigma_i ⊗ I_2 (candidato 3).
  - C-e. Rigidez B_infty^* en la clase mínima s=2 de P17 con Eq. (2) (candidato 4 con Eq. (2)). Es una aplicación condicional de P17 más el certificado estándar.
  - C-f. Velocidad por especie renormalizada por interacción, A.int (candidato 5).
  - C-g. Soportes con término on-site u otros vecindarios (candidato 6).
  - C-h. Teorema c_0 <= c_strict^iso (punto 3, PROVED_UNDER_FROZEN_CONTRACT). Es la desigualdad, no la igualdad.

- Prior art found:
  - P17 (D'Ariano–Erba–Perinotti, PRA 96, 062101; `biblioteca/1708.00826v2.pdf`). Según `reports/2026-09-14--massless-rigidity-source-audit.md` §2 y §4:
    - Clasifica el símbolo mínimo d=3 con s=2: BCC, S+ tetraédrico, imagen proyectiva de Pauli, A_e=0, dos formas normales de Weyl (Prop. 4–5, pp. 5–7).
    - Admite término on-site de partida (p. 2) y prueba A_e=0 como resultado. Esto solapa parcialmente con C-g para s=2.
    - Su clase exige la Eq. (2) de distinguibilidad `[U_l, A_h] != 0` si `l(h) != h` (Def. 1, p. 2). La nota al pie 1 la remite a un trabajo no publicado [23], y ninguna derivación publicada de la Eq. (2) desde homogeneidad está certificada.
    - Grado para C-e: identidad en la clasificación y parcial en la rigidez. La igualdad velocidad/inradio es aplicación propia de ingredientes existentes, no un teorema de P17 en lenguaje de cuerpo causal (audit §4).
  - Respuesta a la pregunta explícita (¿está C-a en la literatura?). No localizada. P17 clasifica con la Eq. (2) y s=2. El audit dice que "omission of the condition is not evidence that a counterexample exists", y que la clasificación fuera de la Eq. (2) no es un teorema publicado localizado (grado: none located, no ausencia probada). Las dos líneas de dos pasos que conviene separar son:
    - (i) Lo que P17 prueba con la Eq. (2): prior art, identidad.
    - (ii) Lo que ocurre sin la Eq. (2): no hay fuente local que lo clasifique. Su estado in-repo es OPEN, salvo T3/O3/O4 con R irreducible de dim 3 o 4 (EMPTY_CLASS) y el contraejemplo s=4.
    - Matiz importante. Si la clasificación sin la Eq. (2) resultara coincidir con la de P17, sería un resultado de redundancia (la Eq. (2) derivable), pertinente para el punto abierto de CURRENT_STATE §7.1 "si P17 Eq. (2) es derivable de las identidades del charter". Si difiere, sería un contraejemplo a la extensión del teorema. Ambos desenlaces dependen de que no exista el trabajo no publicado [23] ni uno posterior. Eso no se puede afirmar localmente.
  - P14 (D'Ariano–Perinotti, PRA 90, 062106, arXiv:1306.1934). Construcción original: BCC, s=2 tomado como mínimo no trivial (no derivado), Weyl coeficiente 1/sqrt(d) (Sec. VII, Eq. (60)). Prior art identidad para el caso base Pavia (la línea CERTIFIED c_0 = c_strict^iso = 1/sqrt(3)) en cuanto al símbolo, no en lenguaje de cuerpo causal.
  - R17 (Raynal, PRA 95, 062344, arXiv:1703.05890v2; auditoría de fuente 2026-09-14, no en `biblioteca/` según `ls`, sí con SHA en el reporte).
    - Deriva Weyl y Dirac con BCC y s=2 fijados, A(0)=I (Eq. (15)) e irreducibilidad asumida explícitamente (fin de Sec. III.E). Permite término on-site antes de derivar.
    - Su Sec. IV trata s=4 en forma restringida, no exhaustiva.
    - Grado: parcial para C-a y C-g (s=2 con irreducibilidad, no sin ella), identidad para el caso base. El audit prohíbe transferir su irreducibilidad a la Prop. 5 de P17.
  - Meyer / Bisio–D'Ariano–Perinotti (Meyer: QCA y no-go de QW escalares, citado en `biblioteca/QCAQW inhomogeneas.md`; BDP: descripción de QCA de Dirac/Weyl).
    - No he abierto estas fuentes en esta sesión. El INDICE local sólo las menciona vía `QCAQW inhomogeneas.md` y no localicé un PDF por nombre (grep de `biblioteca` por "meyer|bisio" sólo devolvió 1708.00826v2.pdf).
    - Para C-c (s=1): P17 lo cita como trivial, y el resultado clásico de que un QW/QCA escalar homogéneo con vecindad finita y unitario sólo traslada (QW escalar, Meyer 1996) es conocimiento estándar, pero [UNVERIFIED] localmente. Grado: parcial/probable, por confirmar.
  - Familia s=4 y mecanismo de compresión (audit `reports/2026-09-15--s4-family-prior-art-audit.md` §2–§5): velocidad efectiva ajustable por compresión con cuadrado complementario que completa una involución ya está presente en la literatura (limita novedad amplia del "presupuesto causal"). Wang–Zhou–Chong (arXiv:1512.00111, Eq. (4), (A5), (A10)): traslación de cuasienergía de Weyl y red sintonizable, prior art. Farrelly–Short (arXiv:1312.2852, Sec. IV, Eq. (19)): límite sin masa genérico de dos componentes con reescalado de coordenadas, prior art. Cedzich–Joye–Werner–Werner (arXiv:2408.02108, Sec. 5.3): separación entre velocidad de Weyl a momento pequeño y propagación más rápida a momento finito, prior art parcial para la idea c_0 < velocidad estricta. Higashikawa–Nakagawa–Ueda, Sun et al.: antecedentes de Floquet Weyl, parciales. Esto afecta a C-d (R reducible) y a la interpretación de la brecha c_0 < C_infty^strict.
  - Bernstein escalar/trigonométrico y su teoría de igualdad: prior art declarado (`comite/contexto.md`, `PROJECT_INSTRUCTIONS.md` §6). Cubre en parte C-h y el certificado estándar de igualdad. La parte vectorial/de múltiples nodos del techo c_0 <= c_strict^iso no la he localizado cubierta, pero no hay reporte ad hoc de ese punto en la lista leída. Grado: parcial.
  - Eon–Di Molfetta–Magnifico–Arrighi, arXiv:2205.03148v4 (`biblioteca/arXiv-2205.03148v4.pdf`; `reports/2026-10-27--eon-v4-interaction-speed-feasibility.md`). Para C-f es la fuente central, no un obstáculo de novedad: el reporte propio concluye REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP, sin vacío, correladores ni velocidades. Hasta que existan, no hay resultado que comparar. Grado: sin resultado propio que auditar. La literatura general de renormalización de velocidad en QCA/Thirring queda sin buscar (ver huecos).
  - Para C-b (E de 2O s=2) y C-g con otros vecindarios: ninguna fuente local clasifica ni descarta, salvo T3/O3/O4 en el repo (ESTABLISHED en clases declaradas, hipótesis vacía) y la clasificación de grupos de isotropía de P17 Prop. 1–2 (grupo finito de Aut(Z^d), orbitas). P17 trabaja con la imagen proyectiva de Pauli (D2 → Z2 x Z2); la lectura de "E de 2O" como representación lineal de dim 2 del doble octaedral no corresponde directamente a su clase, y el límite de cobertura es el que fija el audit: la clasificación P17 es de coeficientes en s=2 con su transitividad sobre S+, no de otras vecindades ni de cobertura de 2O. Grado: none located.

- Novelty wording allowed:
  - Permitido (siempre con nivel de evidencia y cuantificadores congelados):
    - "En la clase declarada X (grupo, s, R, soporte, nodo), el repo establece/rechaza/vacía Y". Por ejemplo, que T3/O3/O4 son EMPTY_CLASS (T u O, R irreducible dim 3 o 4, soporte N_3 completo sin on-site) y el contraejemplo s=4 con c_0(a)=a/sqrt(3) (C_infty^strict = C_micro), ambos con "novedad OPEN".
    - Para C-e: "aplicación condicional de la clasificación P17 más el certificado estándar", literalmente como en el audit. Rigidez como afirmación in-repo sigue OPEN.
    - Para C-a, si se hiciera y saliera algo: "no se localizó en las fuentes revisadas una clasificación s=2 sin la Eq. (2)", nunca "no existe".
  - Prohibido:
    - Cualquier "nuevo", "primero", "universal" o "rigidez" para C-a…C-g sin búsqueda externa y revisión de prior art separada (NO_NOVELTY_WITHOUT_PRIOR_ART).
    - Atribuir a P17 la igualdad velocidad = inradio (es nuestra aplicación).
    - Trasladar la irreducibilidad de R17 a la Prop. 5 de P17.
    - Presentar el barrido finito o un contraejemplo aislado como rigidez (NO_RIGIDITY_FROM_FINITE_SCAN).
    - Usar "v_max" sin cualificar al hablar de C_infty^strict, C_micro y c_0 (NO_UNQUALIFIED_VMAX).
    - Presentar un resultado de redundancia de la Eq. (2) como descubrimiento sin comprobar [23] y la literatura posterior.
  - Observación de priorización desde novedad (no vinculante, la decisión es del usuario): el candidato con más espacio de aportación local y menos solapamiento visible es el de la Eq. (2) (candidato 4 sin ella) por ser el punto que P17 deja sin derivación publicada y el repo mantiene explícitamente abierto. Pero esa misma razón obliga a buscar [23] primero. Los candidatos 1 y 6 hoy no tienen una fuente que los cubra ni los excluya, por lo que su novedad sólo se podría evaluar tras fijar la clase. El candidato 2 (s=1) probablemente es conocimiento estándar y es un resultado de baja novedad. El candidato 3 queda enmarcado por el mecanismo de compresión ya conocido. El candidato 5 está bloqueado por falta de referencia, no por prior art.

- Search gaps:
  - Referencia [23] de P17 (nota al pie 1, trabajo no publicado sobre la Eq. (2)) y cualquier publicación posterior que derive la Eq. (2) de homogeneidad o clasifique sin ella. Es el hueco decisivo para C-a. Se necesita búsqueda externa (arXiv/Google Scholar, citas hacia delante de P17, página de autores en qubit.it).
  - Citas hacia delante de P17 y P14 (censo no hecho; el audit del 2026-09-15 dice explícitamente que no es exhaustivo).
  - Meyer 1996 y Bisio–D'Ariano–Perinotti (y Arrighi y colaboradores sobre QCA de Dirac/Weyl): no abiertos en esta sesión. Confirmar con fuente el resultado de s=1 (QW escalar homogéneo) y cualquier clasificación de QCA con representación de rotaciones tipo 2O.
  - Clasificaciones de QW/QCA con simetría octaedral o cúbica (P17 es BCC con tetraédrico, 2O distinto) y en otras redes d<=3 (candidato 6): sin buscar.
  - Renormalización de velocidad por interacción en QCA (Thirring, Bisio et al. QCA interactivos, Eon v4): sin búsqueda fuera del PDF de Eon v4.
  - Teoría vectorial/de múltiples nodos para c_0 <= c_strict^iso y la igualdad en símbolos matriciales (Bernstein matricial, análisis microlocal de velocidades de grupo máximas, Lax–Wendroff/Trotter–Kato en QW): la parte escalar es prior art declarado, la matricial no está auditada localmente.
  - Los huecos que estas fuentes no cubren no se resuelven por la ausencia de resultados en la búsqueda local; ninguna ausencia aquí es evidencia de novedad.
  - Nota de estado: `comite/contexto.md` nombra la rama `research/b-infinity-post-s4-gate`, desfasada respecto de `research/inverse-gravity-design` (según el dossier). No afecta a esta auditoría.

## 6. Synthesis
Recommended direction, ranked alternatives, and **open disagreements (never hidden)**. A guardian
BLOCK or an unresolved falsification forbids a PROCEED verdict.

**Dirección recomendada.** Un solo charter nuevo centrado en (4), la rigidez de `B_infty^*` en la
clase mínima s=2. El objeto científico es la fila «s=2 sin P17 Eq. (2)». Es el único candidato
que contiene el baseline de Pavia y donde puede salir algo informativo: un contraejemplo s=2
certificado, rigidez en una clase congelada, o la redundancia de Eq. (2). Coinciden los cuatro
expertos, y el auditor de novedad lo ve como el candidato con más espacio no cubierto. El charter
llevaría esta estructura:

- **Paso 0 (cierres declarados como anticipados).**
  - Certificado exacto del lema «`R(V4) ⊂ U(1)·I` ⇒ `EMPTY_CLASS` en `N_3` sin on-site», con el
    control negativo Q8, que no debe vaciarse.
  - A partir del lema, la clase (1) (`E` de `2O`, enunciada bajo `O`) y la parte s=2 lineal de (3).
  - (2), s=1, como argumento analítico, atribuido a P17 p.4 citando [24]; Meyer 1996 queda como
    referencia no leída.
  - El charter debe declarar que estos resultados se anticiparon informalmente en este comité
    (POST-DISCOVERY).
- **Paso 0′ (test mínimo del falsificador).** Antes de congelar la clase de 4b, enumerar
  exactamente los pares `(G, S_+)` con `G ⊂ O` y `S_+ ⊂ N_3` disjunto de `−S_+` y transitivo bajo
  `G`. La clase de 4b se congela según el resultado: o incluye los grupos que no contienen `V4`
  (por ejemplo, `C4` sobre una cara `[UNVERIFIED]`), o restringe explícitamente la fila.
- **4a.** Transferir el certificado de cuerpo estricto a las equivalencias de P17 que se enumeren
  en el charter. Las que no se enumeren quedan fuera y el resultado se queda en CONDITIONAL.
- **4b.** Clasificación exacta de s=2 sin Eq. (2) en las clases congeladas en 0′.
  - Tiene tres salidas congeladas: EMPTY, NONEMPTY con evaluación de `c_0` y `c_strict^iso`, u
    `OPEN_AFTER_CLASS_DERIVATION`.
  - Un ideal distinto de `[1]` no prueba que existan símbolos unitarios reales.
  - Ningún barrido de parámetros cuenta como prueba.

**Alternativas, por orden.**
1. Un charter mínimo solo con el Paso 0 y el 0′. Es barato y cierra filas, pero no avanza la
   igualdad.
2. (3) con s≥4 bajo `T`/`O`. Está bien planteado, pero excluye el baseline y el contraejemplo.
3. (6). Es una clase nueva que cambia `C_micro`. Con masa exigiría congelar `c_H` y `c_{ω^2}`.
4. (5). Hoy no tiene objeto matemático. Queda bloqueado hasta que exista un vacío de referencia.

**Desacuerdos abiertos.**
- *Cobertura de 4b bajo D2.* El matemático afirma que solo `V4` y `A4` son transitivos sobre
  `S_+`. El falsificador replica que eso presupone un `S_+` tetraédrico, que en P17 es consecuencia
  de Eq. (2) y de la fidelidad; sin Eq. (2) podría haber, por ejemplo, `C4` sobre una cara. **No
  está resuelto.** Por eso la recomendación ya no depende de esa afirmación: el Paso 0′ la decide
  antes de congelar 4b.
- *Dónde va (1).*
  - El matemático y el analista la ponen como Paso 0 del charter.
  - El físico la ponía como adenda del gate de isotropía.
  - El lógico la absorbía como subclase de «sin Eq. (2)» bajo D2.
  - El guardián rechaza la adenda al gate cerrado (C2) y exige enunciarla bajo `O`. El falsificador
    añade que `E` no es fiel, así que queda fuera de P17 por dos vías.
  - La síntesis sigue al guardián.
- *«T con s=2 ya es EMPTY».* Lo afirma el matemático. El falsificador responde que solo el caso
  espinorial está cubierto, y solo como control PRELIMINARY sin control de conmutante; el caso
  lineal depende del lema. Se acepta la corrección del falsificador.
- *Argumento para (1).* El físico usa un argumento heurístico de rango ≤2. El matemático, el
  analista y el falsificador usan la identidad de unitariedad en `ℓ=(0,2,2)`. Solo esta última es
  una prueba.
- *Conjetura «en s=2 no hay sectores, luego rigidez».* La proponen el matemático y el físico. El
  falsificador la tacha de narrativa. No debe orientar el diseño de 4b.
- *On-site en (6).* El matemático dice que `A_e=0` (P17) lo hace irrelevante. El falsificador y el
  verificador de literatura restringen eso a la clase P17 con Eq. (2).

**Falsificación.** El falsificador no refuta la recomendación de charterear (4). Refuta dos
afirmaciones de apoyo: la cobertura de 4b y «T s=2 EMPTY». Las dos se han retirado de la
recomendación, y la primera pasa a ser el Paso 0′. Su condición de falsificación independiente
(«no se cumple») se aplica a los resultados futuros, no a la decisión de charterear: ningún cierre
del Paso 0 sube de PRELIMINARY sin un certificado exacto y una revisión de otra familia.

**Literatura.** Citas que corregir en el charter:
- La imagen de Pauli no está en la Prop. 4 de P17, sino en la Fig. 1(c) y en la Sec. V/Prop. 5.
- `A_e=0` está en la Sec. V/Prop. 5(c), no en una «§V(c)».
- s=1 trivial: P17 p.4, que cita [24]. No hay ningún PDF de Meyer en el repo.
- Eq. (2) remite a la ref. [31], no publicada.

**Novedad.** La búsqueda de la ref. [23]/[31] de P17 y de sus citas posteriores es el hueco
decisivo antes de dar valor a un resultado de 4b. Cualquier frase de novedad sigue prohibida.

## 7. Next-step spec
Sequenced plan separating **reversible** steps (may run now if the user asks) from **committing**
steps (only on explicit user authorisation), with the binding rules pre-committed and the
falsifier's minimal falsification test included:

**Reversibles (solo documentación; pueden hacerse ahora si el usuario lo pide):**
- R1. Sincronizar la cabecera de `reports/2026-10-28--irreducible-isotropy-step01.md` con
  `CURRENT_STATE.md` (ESTABLISHED IN THE DECLARED CLASSES, revisiones citadas).
- R2. Corregir `comite/contexto.md` (rama activa `research/inverse-gravity-design`) y
  `comite/roles/fisico.md` (gate 8.21 EXECUTED 2026-09-25, `NO_ABSOLUTE_SCALE_DERIVABLE`
  PRELIMINARY), tras releer `CURRENT_STATE.md:2493-2495`. Es la condición C4 del guardián.
- R3. Redactar sin commit un borrador del charter `theory/<NOMBRE>_GATE.md` con:
  - **Clases congeladas:** grupo, `S_+`, clase proyectiva de `R`, s, `N_3` sin on-site, nodo y
    sector, y Eq. (2) sí/no (KEEP_QUANTIFIERS).
  - **Pasos:** 0, 0′, 4a y 4b como en §6.
  - **Salidas:** EMPTY / NONEMPTY / `OPEN_AFTER_CLASS_DERIVATION`, todas con el mismo rango.
  - **Declaración POST-DISCOVERY** de los cierres anticipados, con sus controles negativos (Q8).
  - **Presupuesto y regla de parada** antes de ver la dimensión de ningún ideal.
  - **Prohibiciones:** ningún barrido en parámetros; ningún «rigidez», «universal» ni «nuevo».
  - **Identificación de grupo exacta:** canonización exacta en lugar de `nsimplify`.
  - **Revisión:** de otra familia de modelos antes de pasar de PRELIMINARY.

**Comprometidos (solo con autorización explícita del usuario):**
- C1. Commit del charter con estado OPEN y registro de la autorización en `CURRENT_STATE.md`.
- C2. Ejecutar el Paso 0′, el test mínimo del falsificador, con un script exacto versionado:
  enumerar los pares `(G, S_+)` y listar los `G` sin `V4`. Del resultado depende el congelado de
  la clase de 4b.
- C3. Ejecutar el Paso 0: certificado del lema con control Q8, más las clases (1), (3)-s=2 y (2).
- C4. Ejecutar 4a y luego 4b, cada uno con su verificador en `scripts/` y su barrido completo de
  `run_all_verifiers.py`.
- C5. Revisión sellada por otra familia (`revision-ciega`) de cada resultado terminal.
- C6. Búsqueda externa de la ref. [23]/[31] de P17 y de sus citas posteriores (por ejemplo, con
  `investigacion-gemini`). Envía texto a terceros, así que necesita permiso expreso.

**Reglas vinculantes precomprometidas:** NO_UNCHARTERED_GATE (nada se calcula antes de C1),
KEEP_QUANTIFIERS, NO_RIGIDITY_FROM_FINITE_SCAN, NO_EVIDENCE_PROMOTION y
NO_NOVELTY_WITHOUT_PRIOR_ART.

## 8. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS

Salvedades:
- El guardián da PASS sujeto a C1–C6.
- La recomendación ya no se apoya en las dos afirmaciones que refutó el falsificador.
- El Paso 0′ va antes de congelar 4b.
- Ningún cálculo sin charter autorizado.

## 9. Provenance
HERRAMIENTAS_COMMIT=a32e189
REPO_COMMIT=5424771
- Presidente: Claude Opus 5.5 (sesión principal).
- Matemático, Físico, Lógico formal y Analista numérico (ola 1): opus, subagentes Explore.
- Falsificador (ola 2): fable, subagente Explore.
- Guardián, Verificador de literatura y Auditor de novedad (ola 2): sonnet, subagentes Explore.
- Todos los miembros son de la familia Claude; esto no es una revisión independiente.

## 10. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
