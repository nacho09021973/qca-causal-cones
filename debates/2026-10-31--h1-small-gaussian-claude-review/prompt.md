# Revisión independiente de la prueba para un perfil gaussiano pequeño

Autorización explícita del usuario: «que lo revise claude», posterior al
informe candidato y a su estado pendiente de revisión. Esta instrucción
autoriza el envío y supera para este encargo la prohibición previa de envío
externo del contrato congelado; no autoriza publicación ni promoción.
Autor: Codex (OpenAI). Revisor: Claude Opus (Anthropic), vía revision-ciega.
Máximo: una revisión, 900 segundos; sin cambio silencioso de modelo.
Cierre: dictamen completo o fallo operativo registrado. Sin abrir otro gate.
Herramienta: ce09890a0d5f68a6634f358eff2e477ac5f15ec7.

---
Revisa de forma adversarial e independiente la prueba candidata
2026-10-31--h1-small-gaussian-profile.md de Codex (OpenAI), en el contrato
H1_SMALL_GAUSSIAN_PROFILE_GATE adjunto. Reconstruye sus desigualdades desde
las definiciones; ni el informe ni un PASS previo son premisas matemáticas.
No tienes herramientas: no edites, ejecutes, navegues ni delegues. El código
adjunto se examina como texto; no afirmes haberlo ejecutado.

El puente Schur promovido y el teorema plano sigma_2/I son resultados de
entrada con alcance congelado; comprueba sus hipótesis y su aplicación.
No se pide revalidar toda la investigación previa. Se adjuntan T1, el puente,
el manuscrito de definiciones y pruebas, y ambos verificadores relevantes.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. PROFILE_AND_PARITY: normalización Fourier y momentos gaussianos, norma
Wiener, paridad de los canales y del funcional físico actual.
2. FIRST_CORRECTION: fórmula general-N del coeficiente cuadrático, términos
dentro de una sola moneda y entre dos tiempos, orden S^{-(k-j)}, factores
de dos al derivar, y resto uniforme en N del producto entero.
3. INTEGRATED_KERNEL: integral_T ||Lambda^-N S(p-i xi_*)^N|| <= C N^-3/2.
Comprueba todos los ocho máximos, proyectores no normales, Hessiano positivo,
complemento compacto y si se confunde integral de norma con norma de integral.
4. SCALE_BOUND: masas l1 inclinadas de las capas, fuente completa de Alice,
Bob físico inhomogéneo, signos del tilt, factores del efecto E, representación
exacta de contorno y paso a C epsilon^2 N^-13/2 exp(-K_*N), incluido el resto
de orden epsilon^4 en esa escala.
5. FULL_SIGNAL_SURVIVAL: uniformidad real de las constantes del puente para
|epsilon|<=1, y existencia de epsilon_0>0, N_0<infinito con cuantificadores
uniformes que dan L_+<0 y |L_+|=Theta(N^-13/2 exp(-K_*N)), y cota para L_-.
Ataca especialmente cualquier continuidad en epsilon que sólo valga a N fijo.
6. SCOPE_AND_CODE: alcance del verificador frente a la prueba analítica,
preservación del observable y distinción entre supervivencia de signo/escala,
coeficiente asintótico calculado, Q_N no nulo y H1 general.

Entrega hasta 2400 palabras en español, con ecuaciones y contraargumentos
precisos. Cada reparación obligatoria debe identificar la ecuación afectada,
qué falla y qué cerraría la objeción. Si sólo falta una aclaración, distingue
ese caso de un fallo matemático. Da dictamen global y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente. No exijas un epsilon_0
numérico ni uniformidad en W que el contrato no promete. No atribuyas novedad,
general H1/H1c, E0, estabilidad general de la potencia ni AdS a este gate.
---
