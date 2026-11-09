# Comité Decision 002 — rumbo-tras-cierre-aproximado-thirring

> Produced by `/comite` (shared engine, `~/herramientas/skills/comite`). The committee PROPOSES;
> the user AUTHORISES. The committee never executes a committing or outward-facing action, never
> loosens a frozen rule post-hoc, and never claims beyond the evidence.
> Guardrails: NO_UNQUALIFIED_VMAX — nunca v_max sin cualificar; C_micro, V_causal^max, V_grp^max y c_IR son distintos (§3); NO_EVIDENCE_PROMOTION — nada sube de PRELIMINARY a ESTABLISHED por encajar en la narrativa (§4); NO_RIGIDITY_FROM_FINITE_SCAN — una búsqueda fallida, un barrido finito o un aislamiento local no prueban rigidez (§7); NO_UNCHARTERED_GATE — sólo se trabaja en gates autorizados en state/CURRENT_STATE.md (§§2, 7); NO_SCOPE_BROADENING — nada de causal sets, redes aleatorias, QCA interactuantes ni nuevas clases de sustrato (§1); NO_NOVELTY_WITHOUT_PRIOR_ART — Bernstein y su teoría de igualdad son prior art; la novedad sigue OPEN (§6); KEEP_QUANTIFIERS — dimensión interna, grupo/acción, representación, nodo/sector e irreducibilidad se congelan antes y se conservan en toda conclusión (§7)

## 1. Decision question
Decisión de rumbo tras cerrar la recuperación aproximada del código M=1 Thirring (APPROXIMATE_RECOVERY_EXCLUDED, promocionado 2026-11-09). Pregunta del proyecto: ¿admite un mismo QCA de alcance finito con una regla fija computación cuántica universal y un régimen relativista de baja energía de la misma regla? ¿Qué siguiente contrato (si alguno) merece abrirse: (a) otro código con la misma regla (p. ej. usar el estado ligado de dos partículas como recurso), (b) más recursos (ancillas, medida intermedia, geometría), (c) el régimen de baja energía de la regla interactuante, (d) certificación Lean del cierre exacto T>=2, o (e) parar la línea?

## 2. Verified state
- HEAD `377ff55` en `research/schur-stability-audit`; `main` = `c58c22c`, mismo árbol (`git log --oneline -3`, `git rev-list --count origin/main..HEAD` = 0). Árbol limpio (`git status --short` vacío).
- Pregunta de coexistencia: `README.md` "Project question"; `PROJECT_INSTRUCTIONS.md` §1 (377ff55); `state/CURRENT_STATE.md` entrada "Project question reframed in README — 2026-11-09". QCA interactuantes en alcance, un modelo/código/recursos por contrato.
- `comite/contexto.md` y el guardarraíl NO_SCOPE_BROADENING de `comite/config.toml` siguen describiendo la pregunta antigua y excluyen "QCA interactuantes" (lectura directa de ambos ficheros). `CURRENT_STATE.md` prevalece.
- Promoción 2026-11-09 (`state/CURRENT_STATE.md`, "Bounded results promoted — 2026-11-09"): solo entrada 00, código M=1, U=FJ, mu=3/5, nu=4/5, z=i, marco F^T B.
- Recuperación exacta T>=2: autor Codex/OpenAI (`reports/2026-11-08--thirring-exact-recovery.md:3`), revisión Claude; PRELIMINARY.
- 1711.03920v1 pp.3–4 (Lema 2, Ec.(14), Prop. 1) leído por el presidente en esta sesión (Read del PDF, páginas 1–8).
- Contrato `61a8215` 2026-11-09 08:30:27; informe `ad01e20` 08:38:02 (`git log -1 --date=iso`).
- Roadmap: `state/ROADMAP_2026-11-09.md` (opciones aproximado o Lean; "No abrir estos frentes simultáneamente").

## 3. Dossier
- Dossier del presidente: hechos F1–F5 (copia en el scratchpad de la sesión; contenido resumido en §2).
- README.md; PROJECT_INSTRUCTIONS.md; state/CURRENT_STATE.md (primeras ~400 líneas); state/ROADMAP_2026-11-09.md.
- reports/2026-11-09--thirring-approximate-recovery.md; reports/2026-11-08--thirring-{two-node,massive-preflight,growing-time,two-contacts,exact-recovery}.md.
- theory/THIRRING_*_GATE.md; theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md; formal/README.md; formal/thirring-two-contact/README.md.
- sources/1711.03920v1.pdf; sources/1804.08508v1.pdf; biblioteca/entropy-27-00198.pdf; biblioteca/INDICE.md.

## 4. Expert briefs (wave 1 — blind, parallel)

### Matemático (análisis asintótico y geometría convexa)

- **Objetos matemáticos**
  - Se usan la regla U=FJ en Z, con W=[[νT, −iμ],[−iμ, νT⁻¹]] y J=∏ e^{iχ n_R n_L}; el código B (M=1, entradas 00, 01, 10, 11); el marco libre B_T=F^T B; K_T=B_T^†U^T B y E_T=(I−B_TB_T^†)U^T B (`reports/2026-11-09--thirring-approximate-recovery.md` §1; `reports/2026-11-08--thirring-exact-recovery.md` §2).
  - Descomposición en fibras: w=x1+x2, y=x1−x2, p∈(−π/2,π/2]. Se cumple U(p)=W_2(p)J(p) y U(p)−W_2(p) tiene rango 2. La proyección de Riesz P(p) va al valor propio aislado, y P_I es su integral directa sobre un intervalo I (informe aprox. §2, pasos 2–3).
  - La relación de dispersión libre es cos ω = ν cos q, con ω∈[0,π] (mismo §2, paso 2).
  - La pregunta de coexistencia exige que el mismo código, los mismos recursos y los mismos parámetros (μ=3/5, ν=4/5, z=i) sirvan para las dos mitades (`PROJECT_INSTRUCTIONS.md` §1).

- **Estado de cada afirmación**
  - **Recuperación exacta para T≥2 excluida.** Hay prueba escrita y una revisión de Claude. Es PRELIMINARY y no está promocionada (`state/CURRENT_STATE.md:88-105`). La prueba sólo usa 0<μ,ν<1, μ²+ν²=1 y z≠1 (informe exacto §1). Por tanto vale en una familia de parámetros, aunque sólo se ejecutó en los congelados.
  - **liminf_T ||E_T|00>||² ≥ c > 0.** Promocionado sólo en su alcance congelado (`CURRENT_STATE.md:23-28`). La prueba depende de z=i, que es lo que permite e^{2ip0}=z en p0=π/4, y de que ν²≠1. No da ningún valor de c.
  - **Lo que no está certificado.** El verificador no cubre el análisis de casos del paso 2, la continuidad de Riesz, la continuidad absoluta del espectro de W_2(p), el Riemann-Lebesgue espectral ni la propia descomposición en fibras (informe aprox. §4). He revisado el argumento y es correcto como esquema estándar: es una perturbación de rango finito (Weyl), el resolvente es continuo en norma y hay convergencia dominada. Faltan dos detalles por escribir: la medibilidad de p→P(p) y la constancia del rango de P(p) en I. Son rutinarios.
  - **Cota uniforme para 01 (derivable, no está en el repo).** La fuga de 01 es >0 en cada T≥2 finito, por la prueba exacta. Además, la nota §3 del informe aprox. afirma, sin desarrollarlo, que 01 tiene liminf>0. De ambas cosas sale inf_{T≥2} ||E_T|01>||²>0. Es una cota uniforme sin valor numérico. La entrada 11 sigue indeterminada.
  - **Extensión a otros χ: conjetural.** Con e^{iχ}∉{±1}, 1711.03920 da una banda ligada con un estado por p (pp.3-4, Lema 2, Prop. 1). Pero el vector compacto de la Ec.(14) sólo existe donde e^{iχ}=e^{±2ip}. Para χ≠π/2 se tiene cos 2p0 = cos χ ≠ 0, y la condición de aislamiento ν²(1+cos2p0 cos2k)=1 deja de ser imposible a priori. Sería un error de la comprobación 3 tratar la identidad z=i como ley de la regla.

- **Invariantes y estructura relevantes**
  - P_I conmuta con U. Ligado y libre son subespacios invariantes con espectros mutuamente singulares: uno puntual por fibra, el otro absolutamente continuo (informe aprox. §2, paso 4). **Consecuencia para (a):** la regla, sin ayuda, nunca hace interferir un estado ligado con un par libre. Un qubit codificado como «ligado frente a libre» sólo adquiere fases relativas dependientes de p, nunca rotaciones. Cualquier puerta entre dos qubits de banda ligada pasa por dispersión de cuatro partículas. 1711.03920 resuelve sólo el sector de dos partículas, así que la dispersión 4→4 no está disponible [UNVERIFIED que no exista en otra fuente; `biblioteca/entropy-27-00198.pdf` es perturbativo].
  - Los estados de la banda ligada son autovectores impropios en la red. Un paquete en esa banda dispersa con ω̃(p), que se obtiene de T±(k̃)=0 en 1711.03920 p.4. La curva ω̃(p) no está calculada en el repo; su curvatura decide si el recurso se mantiene localizado [UNVERIFIED].
  - En p=0, 1711.03920 p.4 da para U_2(χ,0) un autoespacio de dimensión infinita con valor propio 1 («stationary bound states»), incluso con χ=0. Es una fibra de medida cero, pero está justo en momento total nulo, es decir, en el sector de baja energía. Por continuidad de P_p^- → P_0^- (Kato IV 3.16, citado ahí), condiciona cualquier expansión de baja energía del sector de dos partículas.

- **Límite / objetivo continuo**
  - **Para (c).** De cos ω = ν cos q se deriva, cerca de q=0, ω ≈ ω0 + ν q²/(2μ) con ω0 = arccos ν = arcsin μ. Por tanto ω² ≈ ω0² + (ω0 ν/μ) q², lo que da c_{ω²}² = ω0ν/μ ≈ 0,858 con los parámetros congelados. Es un cálculo mío desde la fórmula del informe y no figura en el repo.
  - Con μ=3/5 la masa ω0 ≈ 0,64 es O(1) en unidades de red. No hay parámetro pequeño, así que «régimen relativista» sólo puede significar el coeficiente cuadrático de ω². Según §5 hay que distinguir c_H de c_{ω²} y no identificar c_IR con |∇ω(0)|.
  - Un límite relativista propiamente dicho requiere una escala μ→0 (y quizá χ→χ*). Entonces el código deja de estar en los parámetros congelados.
  - **Observación útil, pero sin verificar.** La exclusión exacta vale para todo μ∈(0,1), y la puerta T=1, D=diag(1,z,z,1), viene de JB=BD, que no parece depender de μ [UNVERIFIED para todo μ]. Si es así, la puerta de primer paso sobrevive a lo largo de la familia μ→0. Esto haría compatible en principio el escalado relativista con el recurso de puerta de T=1, pero no con una puerta componible.
  - El objetivo continuo natural es la teoría de Thirring masivo y sine-Gordon, cuya S-matriz de dos cuerpos y mesones ligados se compararían con la banda ω̃(p). Que 1711.03920 o 1804.08508 reproduzcan ese límite está [UNVERIFIED]; no lo he comprobado en los PDF.
  - En cualquier caso, comparar c_IR (longitud/tiempo) con una tasa de puertas (1/tiempo) exige dos escalas y un coeficiente adimensional (`state/ROADMAP_2026-11-09.md`, último apartado).

- **Comprobaciones del ancla del proyecto**
  1. *¿Uniformidad de los errores?* En el resultado aproximado la o(1) del paso 4 no es uniforme en la entrada ni tiene ritmo: es Riemann-Lebesgue sin tasa. Basta para el liminf, pero no da tiempos ni constantes. Cualquier contrato (a) o (c) que necesite tiempos de puerta debe pedir tasas, por ejemplo decaimiento por fase estacionaria (t^{-1/2} en 1D), y congelarlas antes.
  2. *¿La cota positiva es uniforme?* Para 00 sólo es asintótica (liminf). Para 01 es uniforme en T≥2 sólo combinando los dos resultados (véase arriba); el repo no lo registra.
  3. *¿Identidad de familia tratada como ley?* Sí hay riesgo: la cota usa z=i (Ec.(14) excepcional). No debe extenderse a otros χ ni a «la regla Thirring».
  4. *¿Hipótesis explícitas?* Lo están en el contrato y el informe. Lo implícito es la medibilidad de P(p), la constancia del rango y la representación antisimétrica (justificada en el informe exacto §2).

- **Valoración de las opciones (punto de vista matemático)**
  - **(a) Mejor definida matemáticamente.** Los objetos ya existen (fibras, Riesz, Ec.(14)), pero el obstáculo estructural está demostrado: los subespacios ligado y libre son invariantes y disjuntos. Las puertas de dos qubits requieren el sector de cuatro partículas, que no está resuelto.
  - **(c) Es la mitad intacta de la pregunta.** Choca con un hecho: a μ=3/5 y χ=π/2 no hay régimen perturbativo, y la cuestión real es si la puerta sobrevive al escalado.
  - **(b) Ampliar recursos (ancillas, medida, geometría).** Requiere antes congelar una clase de recursos admitida. Sin eso trivializa la pregunta, porque reintroduce el control externo excluido en §1.
  - **(d) Lean.** Sólo eleva el nivel de evidencia de un resultado de rayos combinatorio. No toca la coexistencia, y el resultado aproximado (integrales directas, Riesz) está fuera de alcance práctico [UNVERIFIED sobre Mathlib].
  - **Recomendación.** Si se abre algo, un contrato de una sola pregunta, exacto y con criterio de abandono escrito. Mi preferencia es un **preflight exacto de dos partículas que compartan (a) y (c)**: la curva ω̃(p) de la banda ligada a parámetros congelados, su comportamiento cerca de p→0 y si D=diag(1,z,z,1) se mantiene en la familia μ∈(0,1). Su cierre negativo sería «sin régimen de baja energía no trivial en el sector de 2 partículas a estos parámetros», y no abriría composición. Si no se quiere esto, **(e) parar** es matemáticamente legítimo: la línea M=1 está cerrada en sus tres variantes (T=1 sí; T≥2 exacta y aproximada no) y la coexistencia queda OPEN.

- **Salvedades**
  - Los ficheros del comité están desactualizados. `comite/contexto.md` describe la pregunta antigua (B_infty^*, rama `research/b-infinity-post-s4-gate`). El guardarraíl NO_SCOPE_BROADENING de `comite/config.toml` sigue excluyendo los «QCA interactuantes», lo que contradice `PROJECT_INSTRUCTIONS.md` §1 (commit 377ff55) y `CURRENT_STATE.md:13-16`. Gana CURRENT_STATE. He evaluado (a)–(c) como dentro del alcance según §1, pero hay que corregir esos ficheros antes de la ola 2.
  - No he leído la revisión de Grok (`reports/reviews/2026-11-09-thirring-approximate-recovery-grok/informe_grok.md`) ni la página 2 de 1711.03920; dependo de las citas del informe para Ec.(2)-(3).
  - Los valores c_{ω²} ≈ 0,926 y ω0 ≈ 0,644 son derivaciones mías no verificadas por script; tómense como orientativos [UNVERIFIED].
  - La «extensión a otros χ» y la «supervivencia de D para todo μ» son conjeturas o derivables, no resultados. No deben entrar en ninguna conclusión sin contrato propio (KEEP_QUANTIFIERS, NO_EVIDENCE_PROMOTION).
  - Ningún cierre negativo de este código es un no-go para el QCA de Thirring (NO_RIGIDITY_FROM_FINITE_SCAN; informe aprox. §1, «Scope»).

### Físico (QCA y límite relativista IR)

- **Magnitudes físicas en juego:**
  - Lo que se cerró es el código M=1 con U=FJ, mu=3/5, nu=4/5 y z=e^{i chi}=i, es decir chi=pi/2 (`reports/2026-11-09--thirring-approximate-recovery.md:22`). La magnitud cerrada es una fuga lógica adimensional, ||E_T|00>||^2 >= c > 0 (líneas 25-27). Es una probabilidad. No es una velocidad ni una energía, así que no compara ninguna de las cuatro velocidades de §3 (`PROJECT_INSTRUCTIONS.md` §3).
  - La dispersión libre que usa la prueba es cos omega = nu cos q (informe:69). omega es una cuasienergía por paso, en radianes por tau. q es un momento en unidades de 1/a.
  - Con mu=3/5, el gap libre es omega(0)=arccos(4/5)≈0,64 rad/paso. Es una fracción O(1) del corte pi. La longitud de Compton correspondiente es de O(1) sitios. Esta deducción es mía a partir de la dispersión citada [UNVERIFIED: no figura en el repositorio].
  - El acoplamiento chi=pi/2 es máximo y no perturbativo.
  - La escala física (a, tau) no aparece en ningún resultado de la línea Thirring. Además, c_IR (longitud/tiempo) y una frecuencia (1/tiempo) no se pueden comparar sin las dos escalas (`theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md:89-92`).

- **Régimen y límites:**
  - Todos los resultados de la línea computacional viven en la escala de la red: el gap es O(1), chi=pi/2 y las puertas son contactos en un mismo sitio. Ninguno vive en un límite IR.
  - Con mu=3/5 no existe la ventana relativista mu ≪ |q| ≪ 1. Por debajo del gap el régimen es no relativista, y por encima los efectos de red ya son O(1) [UNVERIFIED, deducción propia].
  - Consecuencia física para la pregunta de coexistencia (F1): ni una recuperación positiva con estos parámetros habría respondido a la segunda mitad de la pregunta. La regla fija tiene que tener también un régimen relativista.
  - El código sin masa (mu=0) sí tiene envolventes libres con c_IR=a/tau, pero su qubit nodal "no está establecido como qubit IR o de baja cuasienergía" (`state/CURRENT_STATE.md:224-226, 245-247`).
  - Para la regla Thirring interactuante no hay ningún límite relativista establecido. El intento de baja energía de 2026-11-06 fue sobre un modelo de Wilson 3D, no sobre Thirring (`theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md:12`). Su contaje de dimensión del contacto no se transfiere a 1+1 dimensiones.

- **Significado físico de la señal:**
  - El mecanismo del cierre es la banda ligada de dos partículas. 1711.03920 la describe en p.3-4 (Lema 2, Ec.(14), Prop.1) y en sus conclusiones de p.4: hay estados ligados para todo momento total, y "también en el caso libre".
  - Por tanto, la banda es un rasgo genérico de la regla en tiempo discreto y a escala de red, no un accidente de z=i. Eso pesa contra la opción (a): usar la banda ligada como recurso supone trabajar con un objeto de la UV que se mueve con el centro de masas (informe:48-49). Nada indica que sobreviva o sea relativista en el régimen IR.
  - 1804.08508 (resumen) describe dispersión con transferencia de momento entre regiones de la zona de Brillouin, interpretada como "partículas duplicadas de fermión" (fermion doubling). Físicamente, esto acopla el IR con los dobladores. Es el primer candidato concreto a obstrucción para que exista un régimen relativista interactuante. Nadie lo ha examinado en el repositorio.
  - Opino que la observable que de verdad sigue la mitad física pendiente no es otra fuga de código. Son dos cosas:
    1. la forma de la banda ligada y de las ramas libres cerca de sus mínimos, con c_{omega^2} explícita en cada caso;
    2. la supresión, o no, de la transferencia IR→doblador en función de (mu, chi).

  Las dos se pueden obtener de forma exacta a partir de las soluciones publicadas en 1711.03920 y 1804.08508.

- **Límite de lo que se afirma:**
  - El resultado afirma esto: para el código M=1, con U=FJ, mu=3/5, nu=4/5, z=i, la recta infinita y el marco de salida F^T B, ninguna subsucesión recupera el código, ni siquiera de forma aproximada (`state/CURRENT_STATE.md`, entrada de promoción del 2026-11-09).
  - No afirma:
    - un valor de c;
    - nada sobre la entrada 11;
    - nada sobre otros códigos, recursos o parámetros;
    - un no-go para la QCA de Thirring;
    - nada sobre el régimen relativista;
    - nada sobre física de laboratorio.
  - Que se cierre un código tampoco es un no-go del sustrato (`PROJECT_INSTRUCTIONS.md:11`). Por eso la opción (e), parar, no está justificada por la evidencia: solo hay dos códigos cerrados (el nodal sin masa y M=1), los dos fuera del IR.
  - Mi recomendación física es abrir **(c)** como único contrato, acotado y exacto primero. Se congela una familia declarada (mu, chi) que incluya mu ≪ 1, para que exista una ventana relativista. Se congelan también las observables: c_{omega^2} de las ramas libre y ligada, y la amplitud IR→doblador. Y se congela un criterio de abandono (§7).
    - Si sale negativo, la línea debe pararse por la mitad física, con más fundamento que con cualquier código nuevo.
    - Si sale positivo, fija en qué régimen de parámetros tiene que vivir cualquier código posterior de tipo (a) o (b).
  - Sobre las demás opciones:
    - (b) cambia el conjunto de recursos. Es legítimo según F1, pero prematuro mientras no exista un régimen IR que justifique la regla.
    - (d) añade rigor formal sin contenido físico nuevo. Es compatible como tarea de baja prioridad, pero el ROADMAP pide "No abrir estos frentes simultáneamente".

- **Comprobaciones propias del proyecto:**
  1. **¿Qué se compara y en qué límite?** Hoy, ninguna velocidad. La línea Thirring compara operaciones lógicas a escala de red y con chi finito. La única velocidad establecida es c_IR=a/tau, de las envolventes libres sin masa (`CURRENT_STATE.md:226`). Un contrato (c) debe fijar el límite: IR (|q| ≪ 1), mu ≪ 1, y si el acoplamiento chi se escala o se mantiene fijo.
  2. **Con masa, ¿c_H o c_{omega^2}, y no |∇omega(0)|?** En la línea Thirring todavía no aplica: no se ha calculado ninguna velocidad con masa. En la dispersión libre, |∇omega(0)|=0, así que identificarla con c_IR sería un error trivial. El contrato (c) debe exigir c_{omega^2} o c_H de forma explícita para cada rama (`theory/THREE_VELOCITIES.md:64-66`), también para la banda ligada.
  3. **¿Se restaura la escala física solo al final?** Sí, en todo lo hecho hasta ahora: todo es adimensional. Hay que mantenerlo así en (c) y no identificar c con una frecuencia (`LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md:89-92`).
  4. **¿Está autorizado decir algo del laboratorio o de la física real?** No. El gate §8.21 ya no está en NOT_EXECUTED, como dice el ancla. Se ejecutó y se cerró como `NO_ABSOLUTE_SCALE_DERIVABLE` (`CURRENT_STATE.md:854, 2238-2240`). El gate de implementación 4A no tiene contrato (`CURRENT_STATE.md:855`). Ninguna de las opciones (a)-(e) autoriza afirmaciones físicas reales.

- **Salvedades:**
  - Los ficheros del comité están desactualizados y eso es un hallazgo en sí:
    - `comite/contexto.md` describe la pregunta antigua (c_0 frente a c_strict^iso) y la rama `research/b-infinity-post-s4-gate`.
    - El guardarraíl NO_SCOPE_BROADENING de `comite/config.toml` todavía excluye las "QCA interactuantes".
    - Ambos contradicen `PROJECT_INSTRUCTIONS.md:18` (interactuantes dentro del alcance, un modelo/código/recurso por contrato) y `CURRENT_STATE.md`, que prevalece.
    - El ancla del físico también cita §8.21 como NOT_EXECUTED, y eso está superado.
    - Tal como están escritos, (a)-(d) violarían el guardarraíl literal. Según la autoridad canónica, no lo violan. Se deben corregir los ficheros del comité, con aprobación del usuario.
  - La afirmación de que con mu=3/5 no hay ventana relativista es aritmética propia sobre cos omega = nu cos q [UNVERIFIED en el repositorio]. Hay que verificarla dentro de cualquier contrato.
  - Que la transferencia a dobladores obstruya el régimen IR interactuante es una hipótesis física que saco del resumen de 1804.08508 [UNVERIFIED: no he leído las secciones de dispersión ni hay cálculo en el repositorio].
  - Que el acoplamiento de contacto sea marginal en 1+1 dimensiones (Thirring continuo) es conocimiento estándar no anclado [UNVERIFIED]. No debe usarse sin una cita de `biblioteca/`.
  - El estado de la entrada 11 sigue abierto (informe:124-126). No afecta al cierre, pero si se abre (a) con la banda ligada, la entrada 11 y el vector "−" de la Ec.(14) en p=−pi/4 son los primeros que hay que comprobar.
  - Ningún resultado de la línea está en Lean para todo T (F2). Todo lo promovido tiene una sola revisión de otra familia de modelos. No debe tratarse como ESTABLISHED (NO_EVIDENCE_PROMOTION).

### Lógico formal (cuantificadores y Lean)

- **Estado formal:**
  - *Definiciones:* la pregunta de coexistencia (`README.md:8-23`, `PROJECT_INSTRUCTIONS.md` §1). Fija el código, los recursos y los parámetros. Dentro del contrato aproximado también son definiciones K_T, E_T, ℓ_T y "entrelazante" (`theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md:33-50`).
  - *Teorema en papel, PROMOTED en su alcance congelado:* existe c>0 tal que liminf_T ‖E_T|00>‖² ≥ c (`reports/2026-11-09--thirring-approximate-recovery.md:25-31`; `state/CURRENT_STATE.md:23-28`). La promoción cubre solo la entrada 00. Para 01 y 10 el informe dice que la fuga persiste "by the same Steps 3-4" (`:122-125`). Eso es un corolario que no se escribió por separado, y CURRENT_STATE no lo lista como promovido. La entrada 11 está indeterminada. El verificador exacto certifica las identidades algebraicas. La continuidad de Riesz, la continuidad absoluta, Riemann-Lebesgue y la descomposición en fibras son "written proof only" (`:138-140`).
  - *Teorema en papel, PRELIMINARY:* la recuperación exacta queda excluida para todo T≥2 (`reports/2026-11-08--thirring-exact-recovery.md:23-26`). Tiene una revisión de Claude y no está en Lean.
  - *Lean:* `formal/thirring-two-contact` cubre solo nueve identidades finitas de dos pasos, en un anillo de 8 sitios y con parámetros fijos. El puente fermiónico, la fórmula genérica y la interpretación de normas quedan fuera expresamente (`formal/thirring-two-contact/README.md:23-37`). `formal/QcaFormal` no tiene relación con esta línea.
  - *Abiertas:* los otros códigos y recursos, y el régimen interactuante de baja energía (`PROJECT_INSTRUCTIONS.md` §7, l.79-80).
- **Orden de cuantificadores y dependencias:**
  1. *La conjunción misma no está congelada.* El README dice "per parameter choice" y "of the same rule", pero no fija el orden. Una lectura es ∃(μ,ν,χ) fijos con [∃código universal ∧ ∃régimen relativista]. Otra es ∃código en unos parámetros y ∃régimen en una familia o en un límite de escala. Los resultados del código usan μ=3/5 y χ=π/2, que no son pequeños. Un régimen de baja energía suele pedir familias (μ→0, o χ con escala). Si eso no se fija antes, la conjunción puede satisfacerse eligiendo parámetros a posteriori. Tampoco está fijado si el código y el régimen pueden vivir en sectores distintos de la misma regla. Sin esa restricción, el sector de una partícula, que es exactamente libre en el modelo de colisión de densidad (VACUUM_ONE_PARTICLE_ROUTE_CLOSED), daría un conjunto relativista "barato" separado del código [la transferencia a Thirring está UNVERIFIED].
  2. *En (a), el marco de salida debe congelarse antes y no puede depender de U sobre el código.* Si se toma el marco co-móvil B_T := U^T B, la recuperación es tautológica y la puerta queda absorbida en el marco. El cierre exacto se apoya justamente en que B_T no depende de U, V ni de la entrada (`exact-recovery.md:75-76`). Lo mismo vale para el tiempo T: debe ser independiente de la entrada.
  3. *En (b), la escalera de recursos debe congelarse antes de ver el resultado.* Añadir ancillas, medidas o geometría hasta que "funcione" es un grado de libertad a posteriori. La prealimentación adaptativa es control externo encubierto, y hay que declarar si se admite.
  4. Ninguno de los cierres actuales es un no-go para la línea. La única regla de abandono escrita cubre solo la recuperación aproximada con este código y esta regla (`THIRRING_APPROXIMATE_RECOVERY_GATE.md:108-112`). No hay un criterio de abandono registrado para la línea Thirring de coexistencia en su conjunto. Por eso la opción (e) solo puede ser una decisión del usuario, no una conclusión que se derive de los resultados.
- **Afirmaciones de equivalencia:**
  - La equivalencia del contrato, ‖U^{T_n}B − e^{iθ_n}B_T V‖→0 ⇔ (ℓ→0 ∧ K−e^{iθ}V→0), está probada por la cota de rangos ortogonales (`gate:36-47`). Es correcta.
  - El teorema aproximado implica la exclusión exacta solo para T≥T₀, con un T₀ no efectivo. No la implica para todo T≥2: el resultado exacto aporta un testigo explícito para cada T. En sentido inverso, el exacto no implica el aproximado, porque su cota decae (`gate:21-22`).
  - Por tanto, (d) certificaría un resultado PRELIMINARY que la parte promovida ya subsume asintóticamente. No certificaría el resultado promovido.
  - El exacto vale para 0<μ,ν<1 y z≠1 cualesquiera. El aproximado usa que exp(2ip₀)=z y que ν²≠1 en p₀=π/4 (`approx:57-78`). No hay, pues, equivalencia de alcance paramétrico entre los dos resultados.
  - D=diag(1,i,i,1)=(S⊗S)·CZ, comprobable a mano. D es localmente equivalente a CZ, pero eso no da universalidad: las puertas de un qubit generadas por la regla siguen sin existir.
- **Disciplina de tipos y objetos:**
  - El "estado ligado" es un autovector de la fibra U(p), no un vector normalizable de U en la red (`approx:48-49`). En (a), un qubit "en la banda ligada" sería un paquete ∫g(p)f_p dp que dispersa con la banda. Confundir el autovector de fibra con un estado lógico estacionario es un error de categoría.
  - La afirmación "un estado ligado por p para e^{iχ}∉{±1}" (1711.03920, Lema 2 y Prop. 1) no se usó ni se verificó en el informe (`approx:141-142`). Cualquier contrato (a) que se apoye en ella debe verificarla en el PDF.
  - c_IR (longitud/tiempo) y la frecuencia de actualización (1/tiempo) son objetos de tipos distintos (`README.md:31-33`).
- **Comprobaciones propias del proyecto:**
  1. *"Para todo" frente a lo declarado:* el promovido vale solo para el código M=1, U=FJ, μ=3/5, ν=4/5, z=i, recta infinita, marco F^T B y entrada 00. No es un no-go para Thirring. Las comillas del dossier F2 ("01, 10 también") exceden lo promovido.
  2. *Suficiente presentado como necesario:* que el peso ligado sea c>0 es suficiente para la fuga, no necesario. Que 11 tenga solapamiento nulo con este f no implica que no fugue (`approx:123-126`). Entrelazar una vez (D en T=1) es necesario para la universalidad, pero no suficiente.
  3. *Lean frente a papel:* Lean = dos pasos finitos. Nada del teorema exacto para todo T y nada del teorema aproximado. Formalizar el aproximado exigiría teoría espectral (proyecciones de Riesz, continuidad absoluta, Riemann-Lebesgue espectral). `formal/README.md` ya registra que Mathlib carece de teoría de perturbaciones analítica [UNVERIFIED que esa carencia se aplique aquí]. La opción (d) es viable porque el exacto es combinatorio, pero el puente fermiónico I_t tendría que entrar como hipótesis explícita en `Challenge.lean`, no como algo probado.
  4. *Implicaciones tratadas como equivalencias:* "cerrar el código" ≠ "cerrar la regla". "Banda ligada como fuga" ≠ "banda ligada como recurso", que es (a) y sigue abierta.
- **Recomendación formal (no física):**
  - (d) es la opción de menor valor para la pregunta de decisión. Solo es defendible como certificación, con el comparador de enunciados (`/lean-comparador`) y el puente explícito, y sin presentarla como avance de la coexistencia.
  - Antes de abrir (a), (b) o (c), el siguiente contrato debe congelar por escrito el orden de cuantificadores de la conjunción: mismos parámetros o familia, mismo sector o sectores distintos, marcos admisibles, recursos admitidos y criterio de abandono de la línea completa.
  - Con ese orden fijado, el conjunto (c) es el que puede refutar más barato toda la regla en los parámetros congelados. Si (c) falla con los parámetros fijos, (a) y (b) quedan moot para esa elección. Esto es una dependencia lógica, no una evaluación física.
  - (e) no se sigue de ningún resultado. Sería una decisión del usuario.
- **Salvedades:**
  - Hallazgo de proceso: `comite/contexto.md` (pregunta antigua, rama `research/b-infinity-post-s4-gate`) y el guardarraíl NO_SCOPE_BROADENING de `comite/config.toml` (que excluye los "QCA interactuantes") están obsoletos frente a `PROJECT_INSTRUCTIONS.md` §1 (commit 377ff55) y `CURRENT_STATE.md:13-16`. Prevalece CURRENT_STATE. Aplicar el guardarraíl literal vetaría (a), (b) y (c) por error. Hay que corregirlo antes de usarlo como filtro.
  - El resultado de dos nodos tiene abiertas las objeciones O1–O9 de Claude (`README.md`, tabla). Una opción (b) que componga puertas sobre ese código heredaría dependencias no resueltas.
  - La promoción descansa en una única revisión de otra familia (Grok) que inspeccionó el script sin ejecutarlo (`approx:10-13`). NO_EVIDENCE_PROMOTION: ningún corolario (01/10, o la exclusión exacta para T≥T₀) se promueve por arrastre.
  - No verifiqué los PDF fuente (1711.03920, 1804.08508). Todas las citas de página proceden de los informes del repositorio [UNVERIFIED en origen].

### Analista numérico (cálculo exacto frente a diagnóstico)

**Nota previa sobre ficheros desactualizados:** `comite/contexto.md` todavía describe la pregunta antigua (c_0 frente a c_strict^iso). El guardarraíl `NO_SCOPE_BROADENING` de `comite/config.toml` sigue excluyendo los "QCA interactuantes". Desde 377ff55, `PROJECT_INSTRUCTIONS.md` §1 los admite para la pregunta de coexistencia, con un modelo, código y conjunto de recursos declarados por contrato (DOSSIER F1). Prevalece `CURRENT_STATE.md`. Leo ese guardarraíl en su versión vigente y señalo el desfase como hallazgo: los ficheros del comité deben actualizarse antes del próximo contrato.

- **Cálculo proposed or relied on:**
  - El cierre aproximado descansa en un verificador simbólico exacto: `scripts/verify_thirring_approximate_recovery.py`, con 16/16 comprobaciones en SymPy 1.14.0 sobre Q(i,√2), sin coma flotante y sin evolución temporal (`reports/2026-11-09--thirring-approximate-recovery.md:132-135`).
  - El cierre exacto para T≥2 descansa en `scripts/verify_thirring_exact_recovery.py`: 80/80 comprobaciones con enteros gaussianos y denominador 25^T. Solo se evaluaron los tiempos 1, 2, 3, 4, 6, 8 y 12 (`reports/2026-11-08--thirring-exact-recovery.md:230-238`).
  - Lo que podría calcular cada opción:
    - (a) La banda ligada de 1711.03920 Ec.(14) tiene forma cerrada por fibra, así que sus magnitudes son exactas y simbólicas: relación de dispersión ligada, velocidad de grupo y solapamientos con un código nuevo.
    - (b) Ancillas, medida intermedia o geometría multiplican el espacio de diseño. El cálculo acaba siendo enumerativo y fácilmente degenera en barrido.
    - (c) En el sector de dos partículas, la fase de dispersión y la banda ligada cerca de p→0 son exactas. El régimen relativista de muchos cuerpos solo sería accesible numéricamente, con tamaño finito y coma flotante.
    - (d) Lean sería certificación formal, sin cálculo nuevo.
- **Control de errores:**
  - El teorema aproximado no da cota: "c>0 pero sin valor numérico" (informe:33-34). El término o(1) del paso 4 viene de Riemann-Lebesgue y convergencia dominada, sin tasa.
  - Consecuencia: no hay presupuesto de error cuantitativo para ninguna puerta construida sobre este código. Una opción (a) que use el estado ligado como recurso necesita sus pesos y su dispersión de forma cuantitativa, no solo positivos.
  - Para (c), los precedentes del proyecto en N=24/40 están clasificados como FINITE_N_NUMERICAL_DIAGNOSTIC (`comite/roles/numerico.md`; `CURRENT_STATE.md` §10). No hay cotas certificadas de extrapolación.
- **Peso evidencial:**
  - Los pasos 2-4 del cierre aproximado (análisis de casos, continuidad de Riesz, espectro absolutamente continuo, Riemann-Lebesgue, descomposición en fibras) son solo prueba escrita (informe:136-140). El script certifica la aritmética, no el análisis.
  - El "para todo T≥2" del cierre exacto descansa en la prueba de autor con una revisión. El muestreo de siete tiempos solo contrasta la implementación, no el cuantificador (exact-recovery:236-238).
  - Observación propia, derivada del DOSSIER F2 y del informe:24-31 y no comprobada en el repositorio: liminf ‖E_T|00⟩‖² ≥ c > 0 ya implica que no existe ningún V para T≥T₀, con T₀ no cuantificado. Por tanto (d) solo añade de verdad la ventana finita 2≤T<T₀ y el paso de prueba de autor a prueba comprobada por máquina.
  - Ningún cálculo finito de (b) o (c) prueba imposibilidad ni rigidez (`NO_RIGIDITY_FROM_FINITE_SCAN`). Sí puede refutar con un contraejemplo exacto concreto.
- **Reproducibilidad:** todo contrato nuevo debe fijar antes de ejecutar:
  - un script permanente en `scripts/verify_*.py`;
  - el cuerpo exacto (Q(i,√2) o enteros gaussianos);
  - los parámetros congelados μ=3/5, ν=4/5, z=i y p₀;
  - los tiempos o ventanas fijados de antemano;
  - la versión de SymPy y los hashes de script, contrato y PDF en el JSON (precedente: exact-recovery:270-274);
  - un registro de ejecuciones fallidas como `...-failed-run-1` (informe:144-150).
  
  Sin semillas, porque no hay muestreo aleatorio. Si (c) usara coma flotante, debe registrar precisión, N, frontera y tolerancias como diagnóstico.
- **Comprobaciones del ancla del proyecto:**
  1. *Numérico frente a analítico:* ambos cierres (exacto T≥2 y aproximado) son analíticos con aritmética exacta auxiliar. Ninguna conclusión depende de coma flotante. La tabla p_01(T) es ilustrativa y no se usa (exact-recovery:258-261).
  2. *¿Se alcanza el régimen asintótico?* No aplica a los cierres, que no extrapolan. Sí aplica de lleno a (c): un régimen relativista de muchos cuerpos con N accesibles repetiría el problema γ√N≈1.1 en N=24 y no daría signos asintóticos.
  3. *¿Exacto o flotante?* (a) y (d) son exactos o formales. La parte de dos cuerpos de (c) es exacta, la de muchos cuerpos flotante. (b) es exacta por instancia pero combinatoria.
  4. *Falsadores baratos sin barrido:*
     - **(a), antes de contratar:** derivar en forma cerrada a partir de la Ec.(14) la dispersión ω_b(p) de la banda ligada. Si no es plana, un estado ligado localizado se dispersa y la codificación espacial finita queda en entredicho. Si lo es en algún intervalo, hay un candidato.
     - **(a):** comprobar el vector "−" en p=−π/4 para la entrada 11, que está sin decidir (informe:124-126). Es un cálculo exacto de una sola fibra.
     - **(c):** la velocidad de grupo exacta de la banda ligada para p→0, frente a c_IR=a/τ de las envolventes libres. Es un falsador simbólico directo de "un mismo cono para especie libre y especie ligada", conecta (a) con (c) sin barrido y respeta la distinción entre c_IR y frecuencia (ROADMAP:84-90).
- **Salvedades:**
  - c no está cuantificado y el o(1) no tiene tasa (informe:33-34, paso 4). Cualquier contrato de puerta sobre este código hereda un error sin acotar.
  - La continuidad de Riesz y la continuidad absoluta no están certificadas por máquina ni por script (informe:136-140). (d) tal como está en el ROADMAP:76-83 no las cubre: cubre el cierre exacto, no el aproximado.
  - Lean solo cubre las identidades de dos pasos (`formal/thirring-two-contact/`; exact-recovery:270-272). No confundirlo con el teorema para todo T.
  - Una cuantificación numérica de c o de las fugas sería diagnóstico finito, nunca prueba. [UNVERIFIED] si es alcanzable con cotas de intervalo rigurosas: el DOSSIER no lo trata.
  - (b) abre a la vez varios frentes que el ROADMAP:91-95 pide no abrir simultáneamente. Numéricamente es la opción con mayor riesgo de convertirse en un barrido no autorizado.
  - Mi preferencia como analista numérico es no ejecutar nada sin contrato. El orden coste/beneficio sería primero el par de falsadores exactos de (a)/(c), luego (d) acotado a la ventana T<T₀, y (b) al final. Que exista y se registre un criterio de abandono es condición previa, no opción (PROJECT_INSTRUCTIONS §7).

## 5. Controls (wave 2)

### Falsificador

- **Concrete failure modes:**
  1. **Ningún contrato candidato tiene una conjunción falsable.** La pregunta de coexistencia (`README.md:8-23`, `PROJECT_INSTRUCTIONS.md` §1) no fija el orden de cuantificadores. Puede leerse como "mismos (μ,χ) para el código y para el régimen" o como "código en unos parámetros y régimen en una familia o en un límite". Tampoco dice si el código y el régimen deben estar en el mismo sector. El Lógico lo señala (wave-1, punto 1). Aun así, el Físico recomienda (c) con una familia "que incluya μ ≪ 1", elegida después de ver que con μ=3/5 no hay ventana relativista. La única puerta conocida (T=1, D=diag(1,i,i,1)) vive en μ=3/5. Que D no dependa de μ está `[UNVERIFIED]` (Matemático). Si D depende de μ, (c) con μ≪1 queda desconectado del único recurso de puerta, y un "positivo" en (c) no respondería a la coexistencia.
  2. **(a) recibe su forma del fallo.** "Usar el estado ligado como recurso" es el mecanismo de la fuga reetiquetado. El propio Matemático demuestra el obstáculo: P_I conmuta con U, los espectros ligado y libre son mutuamente singulares, solo hay fases relativas y no hay rotaciones. Las puertas entre qubits ligados exigen el sector de 4 partículas, que no está resuelto en 1711.03920. Abrir (a) sin un criterio previo que diga qué contaría como recurso es buscar hasta encontrar.
  3. **(d) no aporta nada a la coexistencia y puede funcionar como promoción encubierta.** El aproximado ya implica el exacto para T ≥ T₀, con T₀ no efectivo (Lógico, Numérico). Lean certificaría un resultado PRELIMINARY (`reports/2026-11-08--thirring-exact-recovery.md`), y el puente fermiónico tendría que entrar como hipótesis. El riesgo es que "certificado en Lean" se lea como ESTABLISHED para la línea.
  4. **(b) trivializa la pregunta** si no se congela de antemano una escalera de recursos admitida. La retroalimentación adaptativa es el control externo que §1 excluye.
  5. **Las cifras de wave-1 no están ancladas.** Son derivaciones de autor sin script: ω0 ≈ 0,644, c_{ω²}² ≈ 0,858 (c_{ω²} ≈ 0,926), la "longitud Compton O(1)" y "sin ventana relativista con μ=3/5". Comprobé la aritmética a mano a partir de cos ω = ν cos q y es coherente, pero ninguna puede entrar en un criterio de contrato sin estar congelada y verificada.

- **Freeze violations:**
  1. **Preflights antes del contrato.** El Numérico ("(a), antes de contratar: derivar … ω_b(p)") y el Matemático (preflight de ω̃(p) y de D en la familia μ) proponen calcular la dispersión de la banda ligada y luego decidir si se abre (a) "si es plana en algún intervalo". Eso es mirar la evidencia antes de fijar el criterio, es decir, un contrato posterior al descubrimiento. Ese cálculo solo es legítimo dentro de un contrato que congele antes qué curvatura o planitud cuenta como candidato y qué la cierra.
  2. **Expectativas corregidas tras el fallo.** El verificador aproximado se comprometió en `dd4e547` (08:36:12) y se corrigió en `f5c0d16` (08:36:40), 28 s después. El primer run dio 14/16, con expectativas de solapamiento cero para 01/10 que resultaron erróneas. El fallo quedó retenido y eso es correcto. Pero la afirmación "01, 10 también solapan" (DOSSIER F2) nace precisamente de una corrección hecha después de mirar, y no está promocionada (`state/CURRENT_STATE.md:23-28` solo promociona 00).
  3. **Contrato y resultado demasiado juntos.** El contrato `61a8215` (08:30:27) ya escribía en R2(a) el criterio exacto que acabó siendo el resultado (peso en un estado ligado ⇒ liminf ℓ_T > 0; `theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md:65-67`). El informe `ad01e20` llegó a las 08:38, 8 minutos después. Que la derivación ya existiera en el contexto del autor antes de congelar el contrato es inferencia `[UNVERIFIED]`, pero la cronología no permite excluirlo. El próximo contrato debería registrar dónde se exploró antes de congelar.
  4. **Cota uniforme por combinación.** El Matemático deriva "inf_{T≥2} ||E_T|01⟩||² > 0" combinando un resultado PRELIMINARY (el exacto) con una nota no desarrollada del informe aproximado (§3). Es una cota nueva obtenida por arrastre (NO_EVIDENCE_PROMOTION).

- **Outcome coercion:**
  1. **Los negativos nunca cierran la línea.** El único criterio de abandono escrito cubre "approximate recovery with this code and rule" (`THIRRING_APPROXIMATE_RECOVERY_GATE.md:108-112`). No existe un criterio de abandono para la línea de coexistencia, aunque `PROJECT_INSTRUCTIONS.md:123-126` lo exige en cada contrato. Todo negativo se reduce a "solo este código", y todo positivo abriría el siguiente frente. Así la línea no puede fallar, porque no hay ningún resultado que la cierre.
  2. **El Físico es asimétrico.** Primero escribe que "(e) no está justificada por la evidencia", y después que "si (c) sale negativo, la línea debe pararse". El Lógico tiene razón: (e) no se deduce de ningún resultado, y continuar tampoco. Ambas son decisiones del usuario y deben presentarse con el mismo peso.
  3. **Falta el veredicto INCONCLUSIVE/OPEN** en las propuestas de (a) y (c). Solo hay ramas positiva y negativa. Debe congelarse, como ya hacía `OPEN_AFTER_BOUNDED_ANALYTIC_ATTEMPT` (gate:99).

- **Premature or over-broad claims:**
  1. **Físico:** "la banda es un rasgo genérico de la regla, no un accidente de z=i". Esto contradice al Matemático: el vector compacto de la Ec.(14) solo existe cuando e^{iχ} = e^{±2ip}. Para χ ≠ π/2, el aislamiento ν²(1 + cos2p₀ cos2k) = 1 deja de ser imposible a priori. Los "stationary bound states" en p=0 (también en el caso libre) son una fibra de medida cero. No pueden sostener un argumento contra (a) ni a favor de él. `[UNVERIFIED]` en el PDF por ambos.
  2. **Físico:** el "fermion doubling" como obstrucción del régimen IR interactuante sale solo del resumen de 1804.08508. Es una hipótesis, no un dato.
  3. **DOSSIER F2:** "Inputs 01, 10 also overlap" excede lo promocionado, como ya dijo el Lógico.
  4. **Nivel de evidencia indefinido.** CURRENT_STATE dice "Promoted … in its frozen scope", pero no asigna ningún nivel de §4 (ESTABLISHED / SUPPORTED / …), y "PROMOTED" no es uno de ellos (`PROJECT_INSTRUCTIONS.md` §4). Esa ambigüedad invita a citar el cierre aproximado como ESTABLISHED. Debe quedar fijado por el usuario antes de que otro contrato lo use como premisa.
  5. **Ningún cierre es un no-go de Thirring.** Ningún experto lo afirma, y debe mantenerse así (NO_RIGIDITY_FROM_FINITE_SCAN). Dos códigos cerrados, ambos fuera del IR, no dicen nada de la regla.

- **Project-specific attacks:**
  1. **Promoción encubierta: sí hay riesgo.** Tres vías: 01/10 y la cota uniforme de 01 entran por arrastre; (d) puede convertir lo PRELIMINARY en "certificado"; y el resultado "promocionado" no tiene nivel de §4. Además, la extensión a otros χ o a toda μ ∈ (0,1) de D o de la banda está `[UNVERIFIED]` y no debe salir del par congelado (μ=3/5, z=i).
  2. **Contrato posterior al descubrimiento: sí, en dos sitios.** En lo ya hecho, por la cronología de 8 min entre contrato e informe y la corrección en 28 s tras el fallo. En lo propuesto, por los preflights "antes de contratar" de (a)/(c) y por la elección de μ≪1 tras ver que μ=3/5 no tiene ventana.
  3. **Rigidez inferida.** Ningún experto la infiere, pero la opción (e) tal como está formulada ("parar la línea") se leería así si no lleva la salvedad de que no es un no-go.
  4. **Revisor no independiente.** El exacto para T≥2 tiene una única revisión Claude, de la misma casa que el autor (Claude Opus 5.5). Cuenta como cero voces independientes. El aproximado tiene una sola revisión Grok que inspeccionó el script sin ejecutarlo (`reports/2026-11-09--thirring-approximate-recovery.md:10-13`). Este comité también es de la casa Claude: su recomendación cuenta como una sola voz.
  5. **v_max y c_IR.** No se usa v_max. Ninguna velocidad con masa está calculada en Thirring, y |∇ω(0)| = 0 en la rama libre con masa. Un contrato (c) debe exigir c_H o c_{ω²} por rama, también para la banda ligada, y no comparar c_IR (longitud/tiempo) con una tasa de puertas (1/tiempo) sin dos escalas (`state/ROADMAP_2026-11-09.md`, último apartado).
  6. **Guardarraíles desactualizados (hallazgo de proceso).** El guardarraíl literal NO_SCOPE_BROADENING (`comite/config.toml`) veta (a), (b) y (c), y `comite/contexto.md` describe la pregunta antigua (c_0 frente a c_strict^iso, rama `research/b-infinity-post-s4-gate`). Los cuatro expertos lo pasaron por alto basándose en el DOSSIER. Un guardarraíl que el comité ignora por consenso es decoración. Debe corregirse con aprobación del usuario antes de usar este brief como filtro.

- **Independent-falsification gate:** No se cumple para la base de la decisión.
  - El exacto T≥2 tiene autor y revisor de la misma casa.
  - El aproximado tiene una sola revisión cross-family, sin ejecución del script.
  - Ninguna de las pruebas analíticas (continuidad de Riesz, a.c., Riemann-Lebesgue, fibras) está verificada por máquina.
  - Las cifras y conjeturas de wave-1 tienen un único verificador: su propio autor.
  - Cualquier contrato nuevo debe nombrar de antemano un revisor de otra familia y congelar qué contaría como objeción bloqueante.

- **Minimal falsification test:** Comprobación previa a cualquier ejecución, sobre el próximo contrato `theory/*_GATE.md`. Debe cumplir dos condiciones:
  - Su commit debe ser anterior a cualquier commit de `scripts/verify_*.py` o a cualquier cálculo de ω_b(p), c_{ω²} o D(μ). Se comprueba con `git log --format='%h %ad %s' --date=iso -- <gate> <script>`.
  - Su texto debe contener literalmente: (i) el orden de cuantificadores de la conjunción (mismos (μ,χ) o familia declarada, mismo sector o no); (ii) el resultado que abandona la línea de coexistencia completa, no solo el contrato; (iii) un veredicto OPEN/INCONCLUSIVE con el mismo peso que los demás. Se comprueba con `grep -n -i "abandon\|cuantificador\|OPEN" <gate>`.

  Si falta cualquiera de las tres cosas, o si el cálculo precede al contrato, la opción elegida, sea (a), (b) o (c), queda falsada como contrato posterior al descubrimiento sin poder falsar la línea, y no debe ejecutarse.

### Guardián de gates y alcance
- Verdict: PASS (condicionado: sólo para recomendar al usuario UN contrato de (c) en forma de preflight exacto; BLOCK explícito sobre ejecutar cualquier cosa, abrir (a)/(b)/(d) o declarar (e) sin carta del usuario)
- Authorisation: ningún paso (a)-(e) figura hoy como chartered. CURRENT_STATE.md:3-16 registra sólo la reformulación de la pregunta y dice «No new gate authorized». Los tres resultados promovidos (CURRENT_STATE.md:18-28) cierran contratos ya ejecutados y no autorizan sucesores. ROADMAP_2026-11-09 (l.96-97) pedía decidir el contrato aproximado o Lean, no ambos; el aproximado ya está hecho. Sólo el usuario charterea (CLAUDE.md, dossier F5). Cualquier opción necesita una decisión explícita del usuario que todavía no existe. La salida del comité es una recomendación, no una autorización.
- Freeze status: no hay nada congelado para ninguna opción nueva. Existe contrato congelado sólo para la recuperación aproximada (theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md; criterio de abandono en :108-112), y está cerrado. No hay criterio de abandono registrado para la línea de coexistencia Thirring completa, ni orden de cuantificadores congelado (¿mismos parámetros o familia? ¿mismo sector? ¿marcos y recursos admitidos?). PROJECT_INSTRUCTIONS.md §7 (l.124-126) exige pregunta conocida y criterio de abandono por línea en cada carta. Todo contrato nuevo debe congelar antes de ejecutar: parámetros o familia (μ, χ), observables, tiempos o ventanas, cuerpo exacto, script permanente `scripts/verify_*.py` y criterio de abandono. Esto es condición previa y no una opción.
- Scope: DENTRO del alcance vigente. PROJECT_INSTRUCTIONS.md §1 (l.18, commit 377ff55) admite QCA interactuantes para la pregunta de coexistencia, con un modelo/código/recurso por carta. CURRENT_STATE.md:13-16 lo confirma. Ampliar a causal sets, redes aleatorias u otras clases de sustrato queda prohibido salvo carta sucesora. (b) rompe «un conjunto de recursos por carta» si abre ancillas, medida y geometría a la vez. Hallazgo de proceso: `comite/contexto.md` (pregunta antigua, rama `research/b-infinity-post-s4-gate`) y el guardarraíl NO_SCOPE_BROADENING de `comite/config.toml` («QCA interactuantes» fuera de alcance) están obsoletos. Prevalece CURRENT_STATE.md (autoridad canónica). Leído literalmente, el guardarraíl vetaría (a)-(c) por error. Hay que corregir esos ficheros con aprobación del usuario antes del próximo uso. La rama actual es `research/schur-stability-audit` (HEAD 377ff55, mismo árbol que main c58c22c) y no coincide con la que cita el contexto obsoleto.
- Forbidden moves present?: ninguno en la propuesta como se me presentó. Riesgos que bloqueo de antemano:
  - NO_UNCHARTERED_GATE: ejecutar un preflight, script o barrido antes de la carta y la autorización del usuario.
  - ROADMAP l.96, «No abrir estos frentes simultáneamente»: abrir a la vez (a)+(c), (b), o (d) junto a otro frente.
  - NO_EVIDENCE_PROMOTION: tratar como promovidos los corolarios 01/10 (el informe los atribuye «by the same Steps 3-4» sin escribirlos aparte, y CURRENT_STATE no los lista), la exclusión exacta T≥T₀ o la exclusión exacta T≥2 (sigue PRELIMINARY con una sola revisión, CURRENT_STATE.md:88-105). Tampoco se debe leer «se sostiene» de Grok como ESTABLISHED.
  - KEEP_QUANTIFIERS: generalizar z=i o χ=π/2 a «la regla Thirring» (la identidad e^{2ip0}=z es excepcional), o suponer que D=diag(1,z,z,1) sobrevive a todo μ (marcado [UNVERIFIED] por el matemático).
  - NO_RIGIDITY_FROM_FINITE_SCAN: usar el cierre de un código, o cualquier barrido finito de (b), como no-go del sustrato. PROJECT_INSTRUCTIONS.md:11 y el propio informe (§1 «Scope») lo prohíben.
  - Elegir (e) como si se siguiera de los resultados: no se sigue de ninguno, sería una decisión del usuario (lógico).
  - NO_SCOPE_BROADENING: ampliación de recursos de (b) sin congelar antes una escalera admitida (la prealimentación adaptativa es control externo encubierto, excluido por §1).
  - NO_NOVELTY_WITHOUT_PRIOR_ART: ninguna afirmación de novedad respecto de 1711.03920 / 1804.08508 / entropy-27-00198, que son prior art.
  - NO_UNQUALIFIED_VMAX: toda velocidad debe cualificarse (c_IR, c_{ω²}, c_H, velocidad de grupo de la banda ligada), sin identificar c_IR con |∇ω(0)| ni con una frecuencia 1/tiempo.
- Project-specific checks:
  1. ¿Autorizado (UNBLOCKED, chartered) en CURRENT_STATE? No. Requiere decisión explícita del usuario inexistente. Registro IR vigente: CURRENT_STATE §10.1, y autorizaciones generales §7 (sólo el punto (3) cartografiado por el usuario) y §8.21. El físico indica que §8.21 ya no está NOT_EXECUTED sino cerrado como `NO_ABSOLUTE_SCALE_DERIVABLE` (CURRENT_STATE.md:854, 2238-2240), así que ni siquiera esa autorización general ampara estas opciones. [No releí esas líneas; lo tomo de la sección del físico.]
  2. ¿Contrato congelado con PASS/FAIL previos? No para (a)-(e). Exige carta nueva con criterios escritos antes de la evidencia. Al ser un cierre «negativo válido» (CLAUDE.md, gate cycle), el criterio de abandono es obligatorio.
  3. ¿Respeta el estado branch-local y no promociona a main? Sí, si el trabajo sigue en `research/schur-stability-audit`. Ninguna opción requiere tocar main. No debe haber promoción a main sin decisión explícita.
  4. ¿C3, E/AdS (FROZEN) y H1c/E0 (sin cambios) separados? Ninguna opción los toca. Cabe una salvedad: el intento previo de baja energía (LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md, 2026-11-06) es un modelo Wilson 3D y no Thirring. Su cuenta de dimensión (-2) no debe transferirse a (c) sin un contrato propio.
  5. ¿Implica commit, push, publicación o barridos numéricos no autorizados? Un contrato escrito implicaría commit del contrato, y el commit exige instrucción del usuario. Un preflight de (c) sería simbólico y exacto (fórmulas cerradas de 1711.03920 / 1804.08508), sin barrido. Las partes de muchos cuerpos serían FINITE_N_NUMERICAL_DIAGNOSTIC y no están autorizadas. (b) es la opción con mayor riesgo de acabar en barrido enumerativo no autorizado.
- Reasons:
  - Orden y secuenciación de las opciones (recomendación al usuario, no autorización): (c) como único candidato, en forma de preflight exacto de dos partículas. Lo apoyan tres expertos de la ola 1, el matemático, el físico y el lógico, mientras que el numérico prefiere primero un par de falsadores exactos de (a)/(c). Es la mitad intacta de la pregunta (README.md:8-23; PROJECT_INSTRUCTIONS §1). Es la que refuta más barato: si falla con parámetros fijos, (a) y (b) quedan moot para esa elección (dependencia lógica). Un cierre negativo en (c) no se presenta como no-go del sustrato.
  - (c) como carta de una sola pregunta debe congelar de antemano:
    - el orden de cuantificadores;
    - la familia (μ, χ), incluyendo μ≪1, porque a μ=3/5 el gap ω₀≈0,64 es O(1) y no hay ventana relativista (esta deducción es [UNVERIFIED], y los valores c_{ω²}≈0,858 y ≈0,926 que los dos expertos citan para este caso no coinciden entre sí, así que hay que recalcularlos en el contrato);
    - las observables: c_{ω²} o c_H por rama, la velocidad de grupo y la curvatura de la banda ligada ω̃(p) cerca de p→0, y la amplitud IR→doblador (1804.08508);
    - el cuerpo exacto y el script permanente;
    - el criterio de abandono (§7).
    El estado ligado de dimensión infinita en p=0 de 1711.03920 p.4 condiciona la expansión de baja energía y hay que tratarlo explícitamente.
  - Justificación de rechazar las demás opciones por ahora:
    - (a) no puede abrirse antes: los subespacios ligado y libre son invariantes y de espectros singulares entre sí, así que las puertas de dos qubits requieren dispersión 4→4 que no está resuelta (matemático; [UNVERIFIED] que no exista otra fuente). Además, la banda ligada es un rasgo UV a escala de red cuyo comportamiento IR es desconocido (físico). Es un error de categoría tratar el autovector de fibra como estado lógico estacionario (lógico). El marco de salida debe congelarse independiente de U, pues B_T=U^T B volvería tautológica la recuperación (exact-recovery:75-76).
    - (b) cambia el conjunto de recursos, y eso es legítimo según README, pero abrirlo de entrada es ampliación a posteriori mientras no se fije una escalera. Rompe además «un conjunto de recursos por carta» y reintroduce el control externo excluido en §1. El resultado de dos nodos conserva abiertas las objeciones O1-O9 de Claude (README, tabla), que una (b) sobre ese código heredaría.
    - (d) no avanza la coexistencia. Sólo certificaría un resultado PRELIMINARY que el promovido ya subsume asintóticamente (T≥T₀ no efectivo, y la ventana 2≤T<T₀ es lo único nuevo). El cierre aproximado, que es el promovido, queda fuera del alcance práctico de Lean (Riesz, continuidad absoluta, Riemann-Lebesgue). Lean actual cubre sólo nueve identidades de dos pasos (`formal/thirring-two-contact/README.md:23-37`). Si alguna vez se abre, requiere `/lean-comparador` y el puente fermiónico como hipótesis explícita en `Challenge.lean`. Es compatible sólo como tarea de baja prioridad y no simultánea (ROADMAP:96).
    - (e) no es una conclusión de las pruebas: sólo hay dos códigos cerrados (el nodal sin masa y M=1), ambos fuera del IR, y el cierre de un código no es no-go (PROJECT_INSTRUCTIONS.md:11). Es legítima únicamente como decisión del usuario, y podría tomarse si (c) cierra negativamente. Hasta entonces la coexistencia queda OPEN. Parar ahora sin criterio de abandono registrado sería una conclusión sin base.
  - Recomendación operativa para el usuario: (1) autorizar la corrección de `comite/contexto.md` y del guardarraíl NO_SCOPE_BROADENING; (2) si lo desea, chartear (c) como contrato único exacto con criterio de abandono; (3) no abrir otros frentes en paralelo; (4) no ejecutar ni hacer commit hasta su autorización explícita. Todo cierre posterior se redacta con la salvedad «para este código/regla/parámetros, no es un no-go del sustrato».

### Verificador de literatura
| Citation | Claimed by | Status |
| --- | --- | --- |
| sources/1711.03920v1.pdf, Lema 2 (p.3): para p≠zπ/2 y e^{iχ}∉{e^{±2ip},1,−1} hay un único k con T±=0 (estado ligado propio) | Matemático, Lógico, Físico | CONFIRMED con matiz (ver Notas 1) |
| 1711.03920, Ec.(14) (p.4): f_±∞ es autovector de U2(χ,p) con valor propio e^{±2ip} cuando e^{iχ}=e^{±2ip}; el vector tiene f(0)=(0,μ/ν,−μ/ν,0) | Matemático, Físico | CONFIRMED |
| 1711.03920, Prop. 1 (p.4): resolución espectral de U2(χ,p) con proyector de rango uno P_{p,χ}=\|ϕ⟩⟨ϕ\| | Matemático, Físico | CONFIRMED (el enunciado se corta en la extracción; solo se ve la definición del proyector) |
| 1711.03920 p.4: en p=0, autovalor 1 de U2(χ,0) con autoespacio de dimensión infinita separable ("stationary bound states"), "incluso con χ=0"; continuidad ‖P_p^−−P_0^−‖→0 por Kato Teor. IV 3.16 (Ref. [33]) | Matemático | CONFIRMED |
| 1711.03920, resumen y conclusiones (p.1 y p.4): estados ligados para todo momento total y también en el caso libre | Físico, Matemático | CONFIRMED como cita textual. Ver Notas 1 sobre la tensión con el Lema 2 |
| 1711.03920 p.4: ω̃(p) se obtiene de T±(k̃)=0 | Matemático | UNCONFIRMED. Solo se trata k̃ en p=0. La ecuación general T±=0 está en Ec.(12) (p.3), y la curva ω̃(p) no está calculada |
| sources/1804.08508v1.pdf, resumen: dispersión con transferencia de momento entre regiones de la zona de Brillouin ("Fermion-doubled particles"), y estados ligados para todo momento total, incluso con acoplamiento nulo | Físico | CONFIRMED (solo el resumen. Que esto obstruya el régimen IR es hipótesis del Físico y no figura en la fuente) |
| 1804.08508 describe U2 como interacción en el mismo sitio seguida de dos Dirac walks libres | Lógico (implícito) | CONFIRMED (resumen) |
| biblioteca/entropy-27-00198.pdf: "A Perturbative Approach to the Solution of the Thirring QCA", enfoque perturbativo (vértices y masa) | Matemático | CONFIRMED. El PDF existe y el resumen es perturbativo. No se revisó si trae dispersión 4→4, así que "no existe en otra fuente" sigue UNVERIFIED |
| reports/2026-11-09--thirring-approximate-recovery.md: Teorema liminf‖E_T\|00⟩‖²≥c>0, sin valor de c (§1, líneas 20-34) | Matemático, Físico, Lógico, Numérico | CONFIRMED |
| Mismo informe, líneas 48-49: la banda ligada viaja con el centro de masas y no es normalizable en la red | Matemático, Físico, Lógico | CONFIRMED |
| Mismo informe, línea 61 y §2 paso 2: f(0)=(0,μ/ν,−μ/ν,0), cos ω=ν cos q | Físico, Matemático | CONFIRMED (el paso 2 está en torno a las líneas 66-69; no se cotejó el número de línea exacto) |
| Mismo informe, líneas 118-127: solapamientos para 01 (3√2/4) y 10 (−3i√2/4), 11 con solapamiento nulo e indeterminado, vector "−" en p=−π/4 sin comprobar | Matemático, Físico, Lógico, Numérico | CONFIRMED. El informe dice 01/10 "por los mismos pasos 3-4", sin corolario aparte. Esto respalda al Lógico y matiza al Matemático (ver Notas 2) |
| Mismo informe, líneas 132-142: 16/16 con SymPy 1.14.0 en Q(i,√2), sin coma flotante. Certificado: Paso 1, antisimetría, identidades del paso 2, solapamientos y peso 16/25. No certificado: análisis de casos, Riesz, continuidad absoluta, Riemann-Lebesgue, descomposición en fibras. Lema 2 y Prop. 1 "no se usan" | Numérico, Lógico, Matemático | CONFIRMED |
| Mismo informe, §5: primera ejecución fallida 14/16, registro `...-failed-run-1` | Numérico | CONFIRMED |
| reports/2026-11-08--thirring-exact-recovery.md: teorema ∄V con U^T B=F^T B V para todo T≥2 (líneas 21-27); la prueba usa solo 0<μ,ν<1, μ²+ν²=1 y z≠1 (línea 35) | Matemático, Lógico | CONFIRMED. El teorema recuadrado se enuncia en los parámetros congelados, y la afirmación de familia es del texto de la prueba |
| Mismo informe, líneas 75-76: B_T=F^T B no depende de U, V ni de la entrada | Lógico | CONFIRMED |
| Mismo informe, §6 (líneas ~228-238): 80/80 controles, enteros gaussianos, denominador 25^T, tiempos 1,2,3,4,6,8,12 que no prueban el cuantificador | Numérico | CONFIRMED |
| Mismo informe, tabla de p_01(T) (líneas ~256-262) ilustrativa; §7 (~268-275) Lean cubre solo dos pasos, sin promoción | Numérico, Lógico | CONFIRMED |
| state/CURRENT_STATE.md:13-16 (PROJECT_INSTRUCTIONS §1 alineado, QCA interactuantes en alcance) | Matemático, Lógico, Físico | CONFIRMED |
| state/CURRENT_STATE.md:23-28 (promoción APPROXIMATE_RECOVERY_EXCLUDED, Grok `grok-4.7`, "se sostiene"; no promovido: valor de c, entrada 11, otros códigos, no-go) | Matemático, Físico, Lógico | CONFIRMED |
| state/CURRENT_STATE.md:88-105 (recuperación exacta, 80/80, PRELIMINARY, sin Lean, sin promoción) | Matemático | CONFIRMED (el rango real es aproximadamente 86-106) |
| state/CURRENT_STATE.md:224-226 y 245-247 (qubit nodal no establecido como IR; c_IR=a/τ por envolvente tras quitar la portadora) | Físico | CONFIRMED (líneas 225-226 y 246) |
| state/CURRENT_STATE.md:854, 2238-2240 (§8.21 ejecutado, NO_ABSOLUTE_SCALE_DERIVABLE); :855 (4A sin contrato) | Físico | CONFIRMED. La corrección del Físico al ancla es válida: el ancla dice NOT_EXECUTED, pero la línea 2240 lo declara superado. Ojo: las líneas 1486 y 1970 aún dicen NOT_EXECUTED |
| state/CURRENT_STATE.md:323 y reports/2026-11-06--low-energy-circuit-verifier.txt:3: dimensión canónica del contacto −2 (du/dℓ=−2u) | dossier F2 (respalda al Físico) | CONFIRMED |
| theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md:12 (modelo de Wilson de dos especies, red Z³, no Thirring) | Físico | CONFIRMED (líneas 5-12: red cúbica Z³, Hamiltoniano Wilson) |
| theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md:89-92 (c_IR frente a frecuencia, dos escalas) | Físico, Matemático (vía ROADMAP) | UNCONFIRMED. El fichero tiene solo 37 líneas y no menciona frecuencia ni inverso de tiempo. El contenido sí está en README.md:31-33 y state/ROADMAP_2026-11-09.md (último apartado) |
| theory/THREE_VELOCITIES.md:64-66 (c_H<c_{ω²}<r_in; c_H²+2Mb=c_{ω²}²; F=arcsin(m)√(1−m²)/m) | Físico | CONFIRMED. El texto trata el Dirac estándar. La fórmula F coincide con el c_{ω²}²=ω0ν/μ≈0,858 del Matemático para m=μ=3/5 (comprobado a mano; la cifra 0,926 es su raíz) |
| theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md:36-47 (equivalencia por rangos ortogonales), 33-50 (definiciones), ~19-22 (cota p_01 que tiende a 0), 108-112 (criterio de abandono solo de esta línea) | Lógico | CONFIRMED |
| PROJECT_INSTRUCTIONS.md §1 (líneas 9-19) y ~77-81: pregunta de coexistencia, QCA interactuantes en alcance (un modelo, código y recursos por contrato), frentes OPEN | Todos | CONFIRMED (las líneas 11 y 18 que citan el Físico y el Lógico caen en el rango; el desfase de uno o dos números no cambia el contenido) |
| README.md:8-23 y 31-33 (pregunta de coexistencia, "per parameter choice", c_IR frente a frecuencia) | Lógico, Físico | CONFIRMED |
| state/ROADMAP_2026-11-09.md (opción Lean, "No abrir estos frentes simultáneamente", c_IR frente a frecuencia, cerrar sin presentarlo como imposibilidad general) | Lógico, Matemático, Numérico, Físico | CONFIRMED (el número de línea 76-95 es aproximado; el texto coincide) |
| formal/thirring-two-contact/README.md:23-37 (anillo de 8 sitios, nueve identidades, puente fermiónico y fórmula genérica fuera de alcance) | Lógico, Numérico | CONFIRMED |
| formal/README.md:47-48 (Mathlib carece de Laplace multidimensional, Poisson en red y teoría de perturbaciones analítica) | Lógico | CONFIRMED con matiz: el texto está escrito para el "Theorem 4.3" de otro frente, no para el cierre Thirring. El propio Lógico lo marca UNVERIFIED en su aplicación |
| comite/roles/numerico.md y state/CURRENT_STATE.md:2830-2831 (N=24/40 como FINITE_N_NUMERICAL_DIAGNOSTIC, γ√N≈1,1) | Numérico | CONFIRMED (el §10 está en torno a la línea 2830; la cifra γ√N≈1,1 está en comite/roles/numerico.md) |
| reports/reviews/2026-11-09-thirring-approximate-recovery-grok/ (revisión Grok, sin objeciones) | dossier F2 | CONFIRMED que el directorio existe. No se leyó su contenido; la promoción "sin objeciones" se apoya en CURRENT_STATE:23-28 |
| comite/contexto.md y guardarraíl NO_SCOPE_BROADENING de comite/config.toml obsoletos frente a PROJECT_INSTRUCTIONS §1 | los cuatro expertos | CONFIRMED. config.toml línea 16 aún dice "nada de … QCA interactuantes". Prevalece CURRENT_STATE.md:13-16 |

- Notas:
  1. **Lema 2 y banda ligada "para todo p y e^{iχ}∉{±1}".** El Lema 2 (p.3) exige p≠zπ/2 y e^{iχ}∉{e^{±2ip},1,−1}. Para e^{iχ}∈{1,−1} afirma que T±≠0 en todo k, es decir, que no hay estado ligado de ese tipo. Sin embargo, el resumen y las conclusiones dicen que hay estados ligados "también en el caso libre". La reconciliación pasa por el autoespacio estacionario de p=0, ±π/2 (p.4) y por la Prop. 1, que no pude leer entera en la extracción. Por eso "un estado ligado por p para e^{iχ}∉{±1}" (dossier F2 y Matemático) es una paráfrasis más fuerte que el texto del Lema 2. Para la rama exacta e^{iχ}=e^{±2ip} la Ec.(14) cubre el hueco. Para los puntos p=0, ±π/2 el Lema 2 no se aplica, y ahí el resultado es el autoespacio de dimensión infinita. El informe aproximado no usa ni verifica el Lema 2 ni la Prop. 1 (líneas 141-142). El Lógico lo señala bien. Cualquier contrato (a) debe leer la Prop. 1 completa.
  2. **Entradas 01 y 10.** El Matemático dice que la nota §3 "afirma, sin desarrollarlo, que 01 tiene liminf>0", y de ahí deduce inf_{T≥2}‖E_T\|01⟩‖²>0. Esto es una derivación suya que une el resultado exacto y el aproximado, y no está en el repo. El informe solo da el solapamiento no nulo y remite a los "pasos 3-4". CURRENT_STATE:23-28 promueve únicamente la entrada 00. El dossier F2 dice "Inputs 01, 10 also overlap", lo cual sí está en el informe, pero no equivale a una promoción. El Lógico lo señala correctamente.
  3. **Cita rota.** `theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md:89-92` no existe (fichero de 37 líneas). La cita del Físico y la del Matemático sobre c_IR frente a frecuencia debe reemplazarse por README.md:31-33 y state/ROADMAP_2026-11-09.md.
  4. **Cálculos propios, no anclados.** Quedan sin cita en el repo ω0≈0,644, c_{ω²}²≈0,858 (≈0,926 como c_{ω²}), la ausencia de ventana relativista a μ=3/5, la supervivencia de D=diag(1,i,i,1) para todo μ, la curvatura de ω̃(p), la 4→4 y la obstrucción por fermion doubling. El único respaldo parcial es THREE_VELOCITIES.md:64-66, que contiene la misma F para el Dirac libre. El resto sigue [UNVERIFIED], como los propios autores marcan.
  5. **Citas de página del Matemático y del Físico a 1711.03920** (pp.3-4, Lema 2, Ec.(14), Prop. 1, estacionarios, Kato) coinciden con el PDF. El Lógico y el Numérico dicen no haber abierto los PDF y citan por los informes. Esas citas indirectas coinciden con lo que verifiqué, salvo lo indicado.
  6. **Citas numéricas de líneas.** Varios números de línea de los expertos (informe aproximado :69, :132-135; exacto :230-238, :258-261, :270-274; ROADMAP :76-95; PROJECT_INSTRUCTIONS :11, :18, :79-80) son aproximados, con desfases de uno a pocas líneas. El contenido coincide en todos los casos.
  7. **Alcance.** No se abrieron las secciones de dispersión de 1804.08508 ni el cuerpo de entropy-27-00198.pdf. Tampoco el informe_grok.md. Lo que dependa de ellos queda UNVERIFIED.

### Auditor de novedad
- Claims examined:
  1. APPROXIMATE_RECOVERY_EXCLUDED para el código M=1, U=FJ, μ=3/5, ν=4/5, z=i, entrada 00, marco F^T B. Es la liminf ‖E_T|00⟩‖² ≥ c > 0, sin valor de c (`reports/2026-11-09--thirring-approximate-recovery.md:25-34`; `state/CURRENT_STATE.md:23-28`). Su mecanismo es el estado ligado compacto de 1711.03920 Ec.(14) (pp.3-4, Lema 2, Prop. 1), aislado en la fibra p=π/4, más Riesz y Riemann-Lebesgue.
  2. Cierre exacto para T≥2 (EXACT_RECOVERY_EXCLUDED_FOR_ALL_FINITE_T_GE2, PRELIMINARY).
  3. Cierres de contactos: puerta T=1 D=diag(1,z,z,1) y no componibilidad del segundo contacto (fuga 288/625). También el código nodal sin masa, con la tesis MASSLESS_NODE_CODE_NOT_UNITARILY_UNIVERSAL.
  4. Posibles palabras de novedad en la opción (a): "el estado ligado como recurso", "coexistencia de computación universal y régimen relativista en una misma regla QCA", "primer no-go de recuperación para Thirring".
  5. Opciones (c) y (d): la banda ligada ω̃(p), c_{ω²} y la amplitud IR→doblador son derivaciones, no resultados. La opción (d) certifica un resultado combinatorio, sin contenido físico nuevo.
- Prior art found:
  - **Bernstein escalar/trigonométrico y su teoría de igualdad:** identical, es prior art por `PROJECT_INSTRUCTIONS.md` §6. Ninguna de las opciones (a)-(e) lo toca, pero no debe reaparecer como mérito de la línea Thirring.
  - **Banda ligada de dos partículas del QCA de Thirring:** identical. Es de `biblioteca/arXiv-1711.03920v1.pdf` y `sources/1711.03920v1.pdf` (Lema 2, Ec.(14), Prop. 1, pp.3-4): un estado ligado por momento total p, que "también existe en el caso libre", con p=0 degenerado de dimensión infinita. Todo uso de la banda como fuga o como recurso parte de ese resultado. La indexación local (`biblioteca/INDICE.md:73`) solo registra pp.1-2 y "interacción Thirring conserva número", y el dossier admite que las citas de página vienen de los informes del repo. Por eso el contenido de pp.3-4 queda [UNVERIFIED en origen].
  - **Solución perturbativa del Thirring QCA:** partial. `biblioteca/entropy-27-00198.pdf` (`INDICE.md:104`, pp.3-4, 8, 12-13, 21-22) da amplitudes perturbativas. No trata recuperación de código ni puertas. No es prior art de la exclusión, pero sí de cualquier cálculo de baja energía perturbativo en (c).
  - **Dispersión con transferencia de momento y "doblado" de fermiones:** identical en lo descriptivo, `sources/1804.08508v1.pdf` (solo el resumen). La obstrucción IR→doblador que propone el físico es una hipótesis suya; no hay prior art local sobre su supresión.
  - **Análisis de fibras, proyecciones de Riesz y Riemann-Lebesgue espectral:** técnica estándar de teoría de perturbación de rango finito (el matemático cita Weyl y Kato IV 3.16). Es prior art de método, no de resultado. Kato figura solo como cita de 1711.03920, y no hay copia local que lo anclé [UNVERIFIED].
  - **Universalidad computacional de QCA, o de redes con interacción, y no componibilidad de puertas:** none located en `biblioteca/` ni `sources/`. Hay QCA/walks de Dirac, Lorentz discreto (`arXiv-1404.4499v1.pdf`, `1312.2852v1.pdf`) y Lieb-Robinson, pero nada sobre computación universal en una regla fija. Por memoria sé que existe literatura de QCA universales y de computación con quantum walks interactuantes [UNVERIFIED, sin fuente local]. Es muy probable que haya prior art parcial sobre "una misma regla fija con universalidad", y no se debe asumir ausencia.
  - **Régimen relativista de baja energía de un QCA interactuante:** partial. `biblioteca/` tiene Lorentz emergente (`arXiv-1305.0011.pdf`, `arXiv-1505.04130.pdf`, `arXiv-1102.0789.pdf`) y QCA de Dirac/Weyl. Ninguno cubre Thirring en tiempo discreto. Los precedentes del propio repo (`theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md`) son de un modelo de Wilson 3D, no de Thirring.
  - **Auditorías previas:** `reports/2026-09-15--s4-family-prior-art-audit.md` y `reports/2026-09-17--physical-realization-literature-scan.md` son sobre la familia S4 y la realización física. Los grep de "thirring" y "interact" no devolvieron nada en esas auditorías, así que no cubren la línea de coexistencia ni Thirring.
- Novelty wording allowed:
  - Permitido: "resultado negativo acotado y registrado": para ese código, esos parámetros, la recta infinita, el marco F^T B y la entrada 00, ninguna subsucesión recupera el código, ni aproximadamente. Se admite también "la exclusión es PRELIMINARY o promovida con una revisión de otra familia, y no es un no-go de Thirring". Puede decirse que el mecanismo es el estado ligado de 1711.03920 usado como fuga.
  - Prohibido:
    - "nuevo", "primero", "descubierto" o "novedoso", en cualquier opción. NOVELTY = OPEN (`CURRENT_STATE.md`) y `NO_NOVELTY_WITHOUT_PRIOR_ART`.
    - Atribuir al repo la existencia de la banda ligada o de las fibras. Eso es de 1711.03920.
    - Atribuir novedad a la técnica de Riesz o Riemann-Lebesgue.
    - "no-go para Thirring", "imposibilidad de computación universal en QCA interactuantes" o "coexistencia imposible" (`NO_RIGIDITY_FROM_FINITE_SCAN`).
    - Presentar (a), (b) o (c) como "primera exploración de computación en el QCA de Thirring", porque no se ha buscado.
    - Llamar novedad a la conjunción "universalidad + régimen relativista". Es la pregunta del proyecto, no un resultado.
    - Presentar c_{ω²} ≈ 0,858 o 0,926 (valores dispares del matemático) o ω0 ≈ 0,64 como resultados. Son derivaciones propias no verificadas y no pueden figurar en ninguna conclusión sin contrato.
  - Si se abre (c) o (a): cualquier candidato a novedad solo puede ser "resultado exacto concreto sobre la banda ligada o la amplitud IR→doblador a parámetros declarados", y requiere una auditoría separada de prior art antes de usar la palabra. Puede quedar como PRELIMINARY OPEN.
  - Sobre (d): la certificación Lean no crea novedad. Puede decirse "verificado en Lean bajo el puente fermiónico declarado como hipótesis", no "demostrado" ni "nuevo".
  - Sobre (e): parar no tiene consecuencias de novedad. Un cierre negativo sin búsqueda externa no permite afirmar ausencia de prior art.
- Search gaps (requieren búsqueda externa, no hecha):
  1. Universalidad computacional en QCA y en walks interactuantes (autómatas de rango finito, QCA universales, walks multi-partícula, rutas de computación con estados ligados). No hay fuente local.
  2. Puertas de dos qubits basadas en dispersión o estados ligados en el modelo de Thirring discreto, incluida la dispersión 4→4. El matemático lo marca [UNVERIFIED] fuera de 1711.03920.
  3. Límite del continuo de Thirring discreto: Thirring masivo, sine-Gordon y su S-matriz. ¿Lo reproducen 1711.03920 o 1804.08508? Está [UNVERIFIED]; no se verificó el cuerpo de 1804.08508 más allá del resumen.
  4. Fermion doubling y restauración de simetría (Lorentz) en QCA interactuantes con transferencia de momento.
  5. Resultados de no-go de recuperación o de "fuga por estados ligados" en QCA, y cotas de error de código en rangos finitos.
  6. Lean y Mathlib: la teoría espectral (Riesz, continuidad absoluta) es [UNVERIFIED] como ausente, y es un punto de precedente para (d).
  7. Verificar en `sources/1711.03920v1.pdf` (pp.3-4) el Lema 2 y la Prop. 1, que el repo cita pero el propio informe aproximado no verificó (`approx:141-142`, según el lógico).
- Salvedad de proceso: `comite/contexto.md` y el guardarraíl `NO_SCOPE_BROADENING` de `comite/config.toml` están desactualizados (pregunta antigua, y excluyen "QCA interactuantes"). `PROJECT_INSTRUCTIONS.md` §1 (commit 377ff55) y `CURRENT_STATE.md` los admiten para la coexistencia, y `CURRENT_STATE.md` prevalece. Evalué (a)-(c) como dentro del alcance. Los ficheros del comité deben corregirse, con aprobación del usuario, antes de usarse como filtro.
- Valoración para la decisión (solo desde novedad): ninguna opción habilita palabras de novedad hoy. (c) tiene menos solapamiento local y más exposición a prior art externo (Lorentz emergente, Thirring continuo). (a) se apoya enteramente en la banda de 1711.03920, que es prior art identical. (d) no añade novedad. (e) solo es decisión del usuario; el cierre no la implica. Si se abre cualquier contrato, debe incluir una búsqueda externa de los huecos 1-3 antes de formular la novedad.

## 6. Synthesis

**Dirección recomendada.** Ningún contrato científico todavía. Primero, dos decisiones del usuario que son condición previa para cualquier opción (a)–(c):
1. corregir `comite/contexto.md` y el guardarraíl NO_SCOPE_BROADENING para que reflejen la pregunta de coexistencia (los ocho miembros lo señalan);
2. fijar por escrito, para la línea entera, el orden de cuantificadores de la conjunción (mismos (mu, chi) para código y régimen, o familia declarada; mismo sector o no; marcos de salida admitidos, independientes de U) y el resultado que abandonaría la línea de coexistencia completa, no solo un contrato (lógico, falsificador, guardián; PROJECT_INSTRUCTIONS §7).

Después, si el usuario lo autoriza, **un único contrato de (c)**: preflight exacto del sector de dos partículas de la regla Thirring, congelado antes de cualquier cálculo, con observables por rama (c_{omega^2} o c_H, nunca |grad omega(0)|), la banda ligada cerca de p=0 (incluido el autoespacio de dimensión infinita en p=0, 1711.03920 p.4) y un veredicto OPEN con el mismo peso que los demás.

**Alternativas, por orden.**
1. (c) como contrato único (físico, lógico, guardián; matemático y numérico la aceptan combinada con (a)).
2. Preflight combinado (a)+(c) sobre la banda ligada (matemático, numérico). Rechazado como primer paso por el guardián (ROADMAP: "No abrir estos frentes simultáneamente") y por el falsificador (forma sacada del fallo).
3. (d) Lean: baja prioridad, nunca en paralelo; solo certificaría el resultado exacto PRELIMINARY, no el promovido (todos).
4. (b) más recursos: solo con una escalera de recursos congelada de antemano (matemático, lógico, falsificador, guardián).
5. (e) parar: legítimo como decisión del usuario, no se deduce de ningún resultado (lógico, falsificador, guardián, matemático).

**Desacuerdos abiertos (no se ocultan).**
- (c) solo frente a (a)+(c) combinado: físico/lógico/guardián frente a matemático/numérico.
- Elección de mu: el físico propone una familia con mu << 1 porque a mu=3/5 no habría ventana relativista; el falsificador lo califica de elección posterior a ver el resultado y señala que la única puerta conocida (D, T=1) vive en mu=3/5 y que su independencia de mu está [UNVERIFIED]. Debe resolverse en la decisión de cuantificadores, antes de cualquier cálculo.
- ¿La banda ligada es genérica o accidente de z=i? Físico ("genérica") frente a matemático y falsificador (el vector compacto de la Ec.(14) exige e^{i chi}=e^{+-2ip}). Literatura: el Lema 2 cubre p != z pi/2 y e^{i chi} fuera de {e^{+-2ip},1,-1}; la paráfrasis "un estado ligado por p" es más fuerte que el lema.
- Preflights "antes de contratar" (numérico, matemático) frente al falsificador: cualquier cálculo de omega_b(p), c_{omega^2} o D(mu) va dentro de un contrato ya congelado.
- Nivel de evidencia de lo "promovido": el falsificador pide que el usuario asigne un nivel de §4, porque "PROMOTED" no es uno de ellos.

**Correcciones del presidente a afirmaciones de los controles** (verificadas en esta sesión):
- Falsificador, "el exacto T>=2 tiene autor y revisor de la misma casa": falso. El autor es Codex/OpenAI (`reports/2026-11-08--thirring-exact-recovery.md:3`) y el revisor Claude. Es una revisión de otra familia.
- Falsificador, "los cuatro expertos pasaron por alto el guardarraíl": falso. Los cuatro lo señalan en sus salvedades.
- Falsificador, contrato e informe con 8 min de diferencia: la cronología es correcta (08:30:27 → 08:38:02). Lo que hay que declarar: el criterio R2(a) del contrato era una idea del autor anterior a la congelación, escrita en el propio contrato como candidata no probada; la vía de la Ec.(14) surgió al leer el PDF después de congelar, y el informe §2 registra que R2(a) tal como estaba escrito era incorrecto (bandas, no estados localizados). La recomendación del falsificador (registrar en el próximo contrato qué se exploró antes de congelar) se acepta.
- Matemático, c_{omega^2}^2 ≈ 0,858 y c_{omega^2} ≈ 0,926: no son valores contradictorios (uno es el cuadrado del otro), como confirma literatura. Siguen siendo cálculos no verificados por script.
- Novedad y lógico marcan [UNVERIFIED] el Lema 2 y la Prop. 1: el presidente leyó 1711.03920 pp.1–8 en esta sesión; literatura confirma las citas con el matiz anotado.
- Literatura: la cita `theory/LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md:89-92` (físico, matemático) está rota; el contenido está en `README.md` y `state/ROADMAP_2026-11-09.md`.

**Guardián:** PASS condicionado, solo para recomendar un único contrato de (c) en forma de preflight exacto; BLOCK sobre ejecutar cualquier cosa, abrir (a)/(b)/(d) o declarar (e) sin autorización del usuario. **Falsificador:** no falsa la recomendación; impone la prueba mínima de §7 como condición previa. Ninguna falsificación queda sin resolver para el paso recomendado, que es solo de decisión.

## 7. Next-step spec

**Reversibles** (no tocan resultados; pueden hacerse si el usuario lo pide):
- R1. Redactar, sin commit, la corrección de `comite/contexto.md` y del guardarraíl NO_SCOPE_BROADENING para que digan lo mismo que PROJECT_INSTRUCTIONS §1.
- R2. Redactar, sin commit, una nota de una página con el orden de cuantificadores de la conjunción y el criterio de abandono de la línea completa, con opciones explícitas para que el usuario elija (mismos parámetros o familia; mismo sector o no; marcos admitidos).
- R3. Búsqueda externa de prior art sobre los huecos 1–3 del auditor de novedad (universalidad en QCA y walks interactuantes; puertas por dispersión o estados ligados en Thirring discreto; límite continuo Thirring masivo/sine-Gordon). Envía texto a terceros (`investigacion-gemini`): solo con permiso explícito.

**Comprometidos** (solo con autorización explícita del usuario):
- C1. Commit de las correcciones R1 y de la nota R2, registradas en `CURRENT_STATE.md`.
- C2. Contrato `theory/<NOMBRE>_GATE.md` para (c), congelado y commiteado antes de cualquier script o cálculo, que contenga: orden de cuantificadores; familia (mu, chi) declarada antes de calcular; observables (c_{omega^2} o c_H por rama, banda ligada cerca de p=0, autoespacio en p=0); cuerpo exacto y script permanente; veredictos positivo, negativo y OPEN con el mismo peso; criterio de abandono de la línea; qué se exploró antes de congelar; revisor de otra familia nombrado de antemano.
- C3. Asignación por el usuario del nivel de §4 a los tres resultados promovidos el 2026-11-09.

**Reglas vinculantes precomprometidas:** NO_UNCHARTERED_GATE; un solo frente abierto (ROADMAP); KEEP_QUANTIFIERS (z=i y chi=pi/2 no se generalizan); NO_EVIDENCE_PROMOTION (01/10, cota uniforme de 01, exclusión T>=T0 no se promueven por arrastre); NO_UNQUALIFIED_VMAX; ningún cierre se presenta como no-go del sustrato.

**Prueba mínima de falsificación (falsificador):** antes de ejecutar nada bajo C2, comprobar con `git log --format='%h %ad %s' --date=iso -- <gate> <script>` que el commit del contrato precede a cualquier script o cálculo, y con `grep -n -i "abandon\|cuantificador\|OPEN" <gate>` que el contrato contiene (i) el orden de cuantificadores, (ii) el resultado que abandona la línea completa y (iii) un veredicto OPEN. Si falta algo, el contrato no se ejecuta.

## 8. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS

## 9. Provenance
HERRAMIENTAS_COMMIT=97292a9
REPO_COMMIT=377ff55
- Matemático (análisis asintótico y geometría convexa): opus
- Físico (QCA y límite relativista IR): opus
- Lógico formal (cuantificadores y Lean): opus
- Analista numérico (cálculo exacto frente a diagnóstico): opus
- Falsificador: opus (el modelo por defecto del arquetipo, fable, falló por falta de créditos, HTTP 429; se relanzó con opus)
- Guardián de gates y alcance: sonnet
- Verificador de literatura: sonnet
- Auditor de novedad: sonnet
- Presidente: Claude Opus 5.5. Todos los miembros son de la familia Claude: el comité cuenta como una sola voz.

## 10. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
