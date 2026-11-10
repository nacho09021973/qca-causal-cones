<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.322 (Claude Code))
opus.json sha256 df670a0af0802ab170c3d3175abff9be40af362840e3177a86789d78d7964970
inicio: 2026-11-10T13:22:11Z  fin: 2026-11-10T13:35:52Z
documento: /home/ignac/qca-causal-cones/papers/ir-corona/ir-corona.tex ; último commit observado: 76d6b38 ; sha256 de la copia enviada 955bf3c14839aa9712c77f4e807c99b1bcf0852c50ebc835e7395d925eabea9f
documento: /home/ignac/qca-causal-cones/reports/2026-11-10--ir-corona-readiness.md ; último commit observado: 76d6b38 ; sha256 de la copia enviada 4df03db00730ff5712cf8dae1eef638039e08bb7d2f57c160ca54970ebb40e0d
entrada_opus.txt sha256 c3fe919541f358a18ed1f50aeeb3f60ff2b9e3fdae53c20b4f8900c647c6c2d8
respuesta sha256 26f3df3204c4e9e8de53d68764da68a3cf25c9a89344f1c2bf6d30f9828be527
-->

# Dictamen: «An infrared operational response outside the emergent light cone of a three-dimensional Weyl quantum walk»

**Alcance.** Este dictamen se basa solo en `ir-corona.tex`. El informe de *readiness* se ha usado únicamente como contexto. No he ejecutado código, no he compilado Lean, no he corrido los certificados y no he consultado literatura externa. Las comprobaciones propias son a mano y en coma flotante. No sustituyen a los certificados.

---

## 0. Veredicto resumido

**Corrección.** La asintótica del Teorema 4.4 me parece establecida en sustancia. Vale para los dieciséis pares, con coeficiente uniformemente no nulo en θ, y la inferencia δ(N)>0 para N≥N_* es válida. No he encontrado ningún error fatal.

Hay dos tipos de reparaciones pendientes:
- **Rigor y redacción:** un párrafo corrupto en §7.1, pruebas comprimidas en el Lema 7.4 y el Teorema 7.5, y un paso escueto en el Teorema 4.3(c).
- **Interpretación:** la lectura "infrarroja" es válida solo como enunciado de existencia dentro de la clase de la Definición 3.1. Además, la no anulación depende del par elegido: por linealidad existen generadores admisibles con coeficiente principal idénticamente nulo (objeción C-7).

**Originalidad.** La aportación es técnica, específica del modelo y de alcance modesto. La asintótica puntual del núcleo probablemente se sigue de teoremas generales de puntos críticos lisos y minimales (ACSV). Esto debe comprobarse en la fuente primaria; véase O-1.

La asintótica operacional ponderada no se sigue directamente de ningún resultado que pueda identificar. El paso adicional existe, pero usa técnicas estándar:
- suma tipo Laplace sobre capas frontera discretas, con Poisson en los planos;
- coherencia de paridad del punto πu;
- certificación de signo.

---

## 1. Qué está respaldado y por qué vía

| Componente | Vía | Comentario |
|---|---|---|
| Teorema 4.1: núcleo, geometría (ec. `eq:separation`), conteo, cota de T_N, δ≤4T_N | **Lean 4/Mathlib** (declarado; no verificado aquí) | La identificación protocolo↔paseo restringido y D_B no están formalizados. |
| Lema 5.1, parte de inclusión | **Lean** (declarado) | La caracterización de igualdad solo tiene prueba escrita. |
| Constantes t_*, K_*, Φ_*, q_t, q_n, P, 𝓘₀, 𝓘₁, φ_∂, 𝒦, Γ̄, ε_±, ℓ₀, ℓ_π, Tabla 1 | **Certificados** de aritmética de intervalos (mpmath.iv) | No ejecutados aquí. |
| Teorema 3.3, Teorema 4.3, Lemas 7.1–7.4, Teorema 7.5, Teorema 4.4 | **Argumento analítico** escrito | Constantes del resto no explícitas. Nada formalizado ni certificado. |
| Diagnósticos de N finito | Coma flotante | No son evidencia, como el propio manuscrito declara. |

**Comprobaciones propias (a mano):**
- Lema 2.1: catorce saltos, Σ‖S_d‖=4, det S=1.
- Identidad SOS (ec. `eq:SOS`), en las variables a_j=c_j².
- Ec. `eq:separation` y la normalización Z_N, c_r.
- J, t_*, K_* y la forma cerrada de cosh²t_*.
- El proyector P a partir de α=c_*²s_*/D_*; q_t, q_n y la convexidad de Φ vía Cauchy–Schwarz.
- La transformada de Laplace que da ĝ_τ, las constantes c_g, 1/720, 1/48, Γ̄≈49.44, ε₊≈0.0492, ε₋≈0.00289.
- La constante 𝒦 y el recuento 13/2; R₀(w_*).
- Las filas (I,I), (σ₁,I), (σ₁,P₃) y (σ₂,P₁) de la Tabla 1: coinciden con C̄=𝒦c_rΓ̄ℓ₀ hasta 4–5 cifras.
- Las constantes del Teorema 3.3.

No he rederivado el álgebra del determinante en el Lema 5.1.

---

## 2. Corrección

### P1. ¿Asintótica uniforme con coeficiente no nulo para los 16 pares? Restricción operacional a 12

**Sí, en sustancia.** La cadena lógica es completa:

1. La ec. `eq:Lexp` reduce L al funcional lineal ℓ(𝒯_χ) más dos piezas: 2Re⟨r,Ea_c⟩ y Q_M=O(N⁸e^{-2K_*N}).
2. La representación exacta (ec. `eq:exactrep`) es exacta: las sumas son finitas y el integrando es entero.
3. Lema 7.1:
   - la parte (a) da la proyección espectral de Perron;
   - la parte (b) da las identidades de semiperíodo, que transportan la cota gaussiana a los ocho puntos de Σ;
   - la parte (c) da caracteres no triviales en los planos para los seis puntos que no contribuyen;
   - la parte (e) da supresión exponencial fuera de Σ por el Lema 5.2.
4. El Lema 7.4 da las formas principales de capa, y el Teorema 7.5 hace el ensamblaje.

He comprobado varios puntos concretos:
- El mismo θ_N aparece en Alice y en Bob.
- La paridad (−1)^{N+u·(y−x)}=(−1)^{j+j'} es correcta. Las fases constantes de x_*, y_* se cancelan al desplazar η→πu+η, porque y_*−x_*=Nv_*.
- El proyector en πu es P^T=P̄.
- 𝒮₋ es antiperiódica en θ, de modo que Γ₋=∫e^{-q_t|τ|²}𝒮₋² es 1-periódica. 𝒮₊ es periódica porque Ψ₀≡0. Por tanto C(θ) es continua y 1-periódica, como se afirma.

**No anulación.** Es robusta y depende poco del certificado. Basta que |ℓ_π/ℓ₀|<(Γ̄−ε₊)/ε₋≈1.7·10⁴. La cota de oscilación de la Tabla 1 (≤1.47·10⁻³) implica |ℓ_π/ℓ₀|≤8.1 en todas las filas.

En varias filas el signo de ℓ₀ es analítico. Por ejemplo, para (I,I) se tiene ℓ₀=−(√3/3)Bα(c−1)/c², con B>0 y c>1. El certificado solo tiene que asegurar ℓ₀≠0 con un margen enorme.

**Restricción a 12 pares.** El Teorema 4.4 cubre los 16, así que la conclusión operacional para los 12 de Pauli se sigue a fortiori. El manuscrito no justifica por qué M=I es un "control de referencia". U_I=e^{iπF_N/2} es una fase local no trivial, segundo-cuantizable igual que las demás. Conviene explicar el criterio o eliminar la etiqueta. Es una cuestión menor.

### P2. Restos de capas/Poisson, uniformidad en θ_N y la inferencia δ>0

**Suficientes en sustancia; la exposición necesita completarse.**

- **Poisson en el plano (Lema 7.4(b)).** La cota de variación total de ∂³G₀ es O(δ^{3/2}R^{-1/2}): interior O(|u|/R²), y una medida en el borde de densidad O(δ/R) sobre una longitud O(√(Rδ)). Lo he comprobado.
  - La cota |Ĝ₀(k)|≲‖∂³G₀‖_𝓜|k|^{-3} es sumable en el retículo dual bidimensional, lo que justifica la fórmula de Poisson.
  - El resto relativo es O(N^{-3/2}), y la cota es absoluta y no se degenera cuando δ→0.
- **Lado de Bob.** El uso de la interpolación de banda limitada de r̃, con ‖∂^βr̃‖_∞≤C_βN^{-3/2-|β|} por la cota L¹ de Fourier, es correcto.
- **Uniformidad cuando θ_N→0 o θ_N��1.** Se cumple, aunque el texto no lo dice explícitamente.
  - Todas las cotas son absolutas y suman contra Σ_j e^{-t_*(θ+j)}poly(θ+j)≤Σ_j e^{-t_* j}poly(1+j), uniformemente en θ∈(0,1).
  - θ_N nunca vale 0, porque √3N/4∉ℤ.
  - Cuando θ→0 el plano j=0 contribuye O(θ³). La continuidad periódica de 𝒮₊ y de 𝒮₋² enlaza los dos extremos.
- **δ(N)>0 para N≥N_*.** Está justificada. inf_θ|C|≥(1−1.5·10⁻³)|C̄|>0 y el resto O(N^{-1/2}) es uniforme en θ, por el punto anterior.

### P3. Validez de la lectura operacional bajo la Definición 3.1

La lectura es válida **como enunciado de existencia**: las ocho operaciones satisfacen la Definición 3.1 (Teorema 3.3, comprobado) y la señal no se anula. No presupone dominancia espectral. De hecho, **la prueba del Teorema 4.4 no usa la admisibilidad en ningún paso**; es una propiedad independiente de las operaciones elegidas.

Formulaciones como "survives infrared control" o "infrared operational response" sugieren más de lo que se prueba. Véanse I-1 e I-2.

### Objeciones de corrección

| ID | Lugar | Objeción | Clase |
|---|---|---|---|
| **C-1** | §7.1, párrafo tras la definición de 𝒯_χ ("by the same argument, For completeness…") | El texto está corrupto: frase truncada, y mezcla capas, modos de Poisson y "O(δ^{7/2}R^{-1/2})" sin hilo. La cota O(N^{-17/2}) se obtiene directamente: \|𝔄_{c_Nφ}\|≤CN^{-9/2} (por \|c_N\|≲N^{-4}ε_⊥⁴, misma suma de capas que en el Lema 7.4(a)), ‖𝔅_w‖≤CN^{-5/2} y ∫‖S̃_N‖dμ≤CN^{-3/2}. No hace falta Poisson. Además, el teorema solo necesita o(N^{-13/2}). | Reparable |
| **C-2** | Lema 7.4 (Layers) y Teorema 7.5 | Las pruebas son esquemáticas. Falta explicitar: (i) que r₀ debe quedar también por debajo de la distancia de la proyección en el plano de η₀∈Σ\\{0,πu} a 2πΛ₀\* (esto lo requiere el apartado (d), no solo "half the shortest reciprocal vector"); (ii) el truncamiento δ≤R/2 y la validez de la aproximación parabólica de ε_⊥; (iii) una frase sobre uniformidad en θ, incluidos los extremos. Las tres cosas son correctas en sustancia. | Reparable |
| **C-3** | Teorema 4.3(c) | La identidad I(u)=log4 solo se muestra a lo largo de la diagonal. La cota superior sobre todo ξ se sigue de la cota inclinada (ec. `eq:tilt` con el Lema 5.3) frente a la amplitud exacta 4^{-N} de la Proposición 2.2(c), pero el texto no lo dice. | Reparable (menor) |
| **C-4** | Proposición 2.2(b), prueba | En los nodos con f=−1 se tiene ω=π−\|p−p_∨\|+…, no \|p−p_∨\|. La conclusión no cambia. | Reparable (trivial) |
| **C-5** | Teorema 4.4, Apéndice A | Resto y N_* no explícitos. Los diagnósticos indican que el término principal no es preciso en N≤56: el semianalítico da una corrección relativa ≈−100/N. El cociente pieza-a_c/pieza-a_↓ por N da 365, 376 y 358, prácticamente constante. Esto es coherente con que la pieza a_↓ esté dominada por su corrección O(N^{-1}) en ese rango, y no contradice la cota N^{-17/2}. Además, los términos impares en η y en u_⊥ (cúbico, P(η)−P, variación de R₀) se anulan por simetría al integrar contra funciones radiales, lo que sugiere un resto efectivo O(N^{-1}). Mejora opcional. | Limitación |
| **C-6** | Observación 4.6, "first feature" | C(σ₃,·)=−C(I,·) es inmediato a partir de la ec. `eq:Lexp`: como σ₃↓=−↓, las partes lineales tienen signo opuesto y la parte en c_N es común. No es un resultado del cálculo. | Reparable (redacción) |
| **C-7** | Observación 4.7 (Methodology), problema abierto (1), Corolario 4.5 | En la capa frontera F_N=O(N^{-2}), de modo que el término e^{-K_*N}N^{-13/2} solo ve el primer orden iπF_NM/2. Por tanto, para M=aI+b·σ, el coeficiente principal es aC_I+Σb_kC_{σ_k}, lineal en (a,b). Hay direcciones donde se anula idénticamente en θ, a saber (a,b)⊥ℓ₀ y (a,b)⊥ℓ_π. Un ejemplo trivial es M=I+σ₃=2\|↑⟩⟨↑\|, que deja φ_N invariante. Uno no trivial, con M_B=I, es b∝ℓ��×ℓ_π≈(0.096,−0.096,0.991), por mis números. La afirmación "general generators not covered" es demasiado pesimista: el primer orden está resuelto por linealidad. Y la no anulación es específica del par, no genérica. | Limitación (y reparación de texto) |
| **C-8** | §8.1 (cita de `state/CURRENT_STATE.md`, Sec. 10.1) | Un manuscrito no puede apoyarse en un archivo interno de estado ni en "scoped review records". Hay que probarlo, citarlo como trabajo publicado o eliminarlo. | Reparable |
| **C-9** | Teorema 3.3 | Las constantes explícitas solo hacen no trivial la cota para N≳1.4·10¹¹ (η_op) y N≳2.4·10¹⁸ (η_enc), porque m≈6·10⁻⁸ es muy pesimista. La afirmación asintótica es correcta, pero "explicit constants" no tiene contenido práctico. Se podría acotar directamente el peso del recurso en 𝒜_N. | Limitación |
| **C-10** | §1 y §7.1 ("free tail only polynomially small") | El orden N^{-3/2} es puntual. ‖r‖_{ℓ²(ℬ_N)} es O(1) e independiente de N. La tasa K_*, y no 2K_*, procede de interferir con una amplitud de referencia de norma O(1) que ya está en ℬ_N. Conviene decirlo explícitamente; esto también aclara la estructura lineal en T_N del Teorema 4.1. | Reparable (claridad) |

### Objeciones de interpretación (P3)

| ID | Lugar | Objeción | Clase |
|---|---|---|---|
| **I-1** | Resumen, Corolario 4.5 | La admisibilidad no interviene en la prueba de la asintótica. "Survives infrared control" debe leerse como "existe una respuesta no nula para operaciones que cumplen la Definición 3.1". | Limitación; redacción reparable |
| **I-2** | Definición 3.1 frente al Teorema 4.4 | La tolerancia de admisibilidad es N^{-1/2}, mucho mayor que e^{-K_*N}. La clase es estable bajo perturbaciones de norma o(1) de cualquier carácter UV. **Estimación heurística, no probada:** componer U_M con una puerta de un solo sitio de ángulo ε_N en la capa frontal de 𝒜_N preserva la admisibilidad para todo ε_N→0, y añade una contribución de orden ε_N N^{-11/2}e^{-K_*N}. Con ε_N=N^{-1/2} esa contribución supera al término principal. Por tanto, la admisibilidad no controla el mecanismo de la respuesta. A esto se suman otros rasgos de escala reticular: la contribución del punto πu, la paridad de los planos, y la dependencia del exponente 13/2 del orden de anulación de los perfiles (el manuscrito reconoce esto último). | Limitación conceptual |
| **I-3** | §8.1 | El manuscrito ya descarta el origen espectral. Recomiendo que el resumen y la introducción sean igual de prudentes. | Reparable (redacción) |

---

## 3. Originalidad (P4)

### O-1. ¿Qué resultado previo podría implicar la asintótica del núcleo?

El candidato principal es la teoría de puntos críticos **lisos y minimales, en número finito y no degenerados** de Pemantle–Wilson–Melczer [ACSV]. Se aplicaría a la función generatriz Σ_N S(z)^N w^N, o a z^{Nu}S(z)^N tras reducir a serie de potencias.

**Hipótesis que coinciden con lemas del manuscrito:**
- **Finitud y minimalidad en el toro inclinado.** El Lema 5.2 da igualdad del radio espectral solo en Σ, que tiene 8 puntos.
- **Lisura.** El autovalor dominante es simple, con brecha e^{2Φ_*}≈15.8 (Lema 7.1(a),(d)).
- **No degeneración.** Q=HessΦ(ξ_*)>0.
- **Dirección.** ∇Φ(ξ_*)=v_* corresponde a la dirección crítica (v_*,1), y la dependencia en la dirección es analítica en un entorno compacto de v_* dentro de la corona.

**Qué falta verificar en la fuente:**
- si los teoremas generales, y no solo los ejemplos de paseos cuánticos, admiten puntos minimales fuera del toro unitario (componentes del complemento de la ameba, o serie de Laurent reducida a serie de potencias);
- si dan uniformidad en direcciones.

El párrafo de literatura del manuscrito solo trata los ejemplos de paseos cuánticos de [ACSVms], [BBBP], [BGPP] y [BP3], fuera de la región factible. No trata el teorema general. Si este se aplica, la asintótica puntual del núcleo no es nueva.

Hay vías alternativas: el punto de silla multivariante para potencias de una matriz de polinomios de Laurent (análogo d-dimensional de Sunada–Tate) y los métodos de cuasi-potencias de Nagaev–Guivarc'h, Bender–Richmond y Hwang.

### O-2. ¿Implica alguno la asintótica operacional ponderada directamente?

**No, que yo identifique.** Aun disponiendo de la asintótica del núcleo uniforme en direcciones, falta un paso adicional sustantivo:

1. Reducir el observable al funcional de interferencia con la cola libre (ec. `eq:Lexp` y Lema 7.2).
2. Sumar contra perfiles que se anulan cuadráticamente, en capas de profundidad O(1) con dirección tangencial plana confinada por los perfiles. Esto requiere Poisson en planos reticulares inconmensurables con las esferas, de ahí el coeficiente cuasi-periódico en θ_N.
3. Cancelar los seis puntos de Σ mediante caracteres no triviales sobre Λ₀.
4. Establecer la coherencia de paridad en πu, que produce 𝒮₋.
5. Certificar que el coeficiente no se anula.

**Relevancia.** El paso está bien ejecutado, pero es metodológicamente estándar: método de Laplace discreto más Poisson.

Un prefactor que depende de la parte fraccionaria es el fenómeno conocido de corrección reticular en grandes desviaciones locales (Bahadur–Rao, caso reticular). Por eso "leading coefficient that is oscillatory" no es un fenómeno conceptualmente nuevo.

La certificación de no anulación tiene un margen enorme (véase P1), así que su contenido es modesto. Y por C-7, la no anulación no es genérica en el generador.

El valor principal es mostrar, para un protocolo concreto, que la tasa K_* se alcanza: una cota inferior fina que acompaña a la cota superior. La respuesta a la pregunta (I) es la esperable genéricamente.

### O-3. Componentes ya reconocidos como previos

- El **valor de K_*** se deduce de CJWW, ec. (5.21), como el propio manuscrito admite. La identificación del minimizador regional es elemental (convexidad e hiperplano soporte).
- La **cota superior** usa el desplazamiento de contorno de CJWW con lemas elementales. La formalización en Lean añade valor de verificación, no novedad matemática.

### O-4. Sobre la reivindicación de novedad

La frase de prioridad acumula calificativos ("first … prefactor-level … oscillatory … certified … infrared-controlled … operational … strictly outside … three-dimensional multi-component"). Es novedad por conjunción. Recomiendo reformularla en términos del paso adicional (O-2), condicionada al resultado de O-1.

### Fuentes primarias que habría que comprobar

1. **Pemantle–Wilson–Melczer, *ACSV*, 2.ª ed. (2024)** y el manuscrito expandido:
   - teoremas de puntos lisos con puntos críticos minimales finitos y no degenerados;
   - tratamiento de series de Laurent y componentes de la ameba;
   - uniformidad en direcciones;
   - las afirmaciones concretas atribuidas a los Teoremas 12.12 y 12.14.
2. **CJWW, arXiv:2408.02108:**
   - ec. (5.15), ec. (5.21), Lema 4.1 y Sec. 5.1;
   - si afirman la optimalidad de las tasas o solo cotas superiores.
3. **Sunada–Tate (2012):** si su método de punto de silla es independiente de la dimensión.
4. **BBBP (2011), BGPP (arXiv:0903.2967), Baryshnikov–Pemantle III (arXiv:0810.4898):** las afirmaciones citadas con número de teorema.
5. **Bahadur–Rao (1960), caso reticular:** el prefactor dependiente de la parte fraccionaria.
6. **Bender–Richmond (1983) y teoría de cuasi-potencias:** teoremas locales de "large powers" multivariantes.

---

## 4. Cierre

**Corrección.** Aceptable en sustancia, sin objeción fatal. Antes de considerarla cerrada hacen falta:
- reparaciones de redacción y rigor: C-1, C-2, C-3, C-6, C-8 y C-10;
- una reformulación interpretativa: C-7, I-1, I-2 e I-3;
- reconocer explícitamente las limitaciones C-5 y C-9.

**Originalidad.** Contribución técnica modesta y específica del modelo. El juicio final depende de **O-1**: comprobar si la teoría general ACSV de puntos minimales lisos da directamente la asintótica del núcleo en la corona. Si la da, la novedad se reduce al paso de suma ponderada y certificación (O-2), que es correcto pero estándar.

**Objeciones pendientes:** C-1, C-2, C-3, C-7, C-8, I-2 y O-1. Las demás son menores o ya están reconocidas en el manuscrito.
