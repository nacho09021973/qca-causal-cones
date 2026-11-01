# Revisión independiente del gate C_ACROSS_LATTICES

Autorización explícita del usuario: «si, con ciro y gemini» (2026-11-01).
Autoriza este envío externo a xAI y Google; no autoriza publicación ni
promoción. Autor: Claude Code (Claude Opus 5.5, Anthropic). Revisores:
Grok grok-4.7 (xAI) y Gemini gemini-4-argon (Google), cada uno vía
revision-ciega, en paralelo y sin ver la otra revisión.
Máximo: una revisión por casa, 1800 segundos; sin cambio silencioso de modelo.
Base: aab5e7b. Herramienta: ce09890a0d5f68a6634f358eff2e477ac5f15ec7.

---
Revisa de forma adversarial e independiente la ejecución del gate
C_ACROSS_LATTICES: el informe 2026-11-01--c-across-lattices.md y su
verificador verify_c_across_lattices_gate.py, escritos por Claude
(Anthropic), contra el contrato congelado C_ACROSS_LATTICES_GATE.md
adjunto. Reconstruye las afirmaciones desde las fuentes primarias adjuntas
(texto extraído de los PDF; el PDF es la autoridad, las fórmulas pueden
venir desordenadas). El informe no es premisa. No tienes herramientas: no
ejecutes, edites, navegues ni delegues. El código se lee como texto; no
afirmes haberlo ejecutado ni confirmes el recuento 103/103.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. SOURCE_READING: ¿los símbolos codificados son fieles a las ecuaciones?
   Convención de fase, orden de los productos (incluido el producto Π de JDW
   Eqs. (2) y (8)), lectura "toma el valor en N_j", parametrización U(·) de
   JDW Eq. (1), elección de representación de Clifford para Mlodinow–Brun,
   uso de las τ_i de ADMP Eq. (5), y las dos incidencias de signo de ADMP
   (α y S). ¿Está justificada la exclusión de Arrighi–Facchini y de L6b?
2. STEP_SETS: conjuntos de pasos compuestos y grupos de traslación; ¿son
   correctas las identificaciones "mismo sustrato" (L6a = L6d, L6e = L2,
   L5a/L5b = BCC, L6f = L6a salvo rotación y escala, L6c hexágono con grupo
   más fino)?
3. MASSLESS_SPEEDS: nodo en k=0, extracción de c_0 desde i dU/dk(0),
   isotropía y ausencia de tilt, normalización (paso más largo = 1), r_in,
   y el contraste con la velocidad continua que da cada fuente.
4. STRICT_BODY: el argumento de vértices (coeficiente de n·v en U^n igual a
   A_v^n; no nilpotente implica C_infty^strict = C_micro).
5. MASSIVE: la identidad i dU U(0)^† = X_par + (sin θ/θ) X_perp, la
   consistencia de c_H con la definición del gate Weyl/Dirac, el argumento
   de la Hessiana de G = (U+U^†)/2 (perturbación degenerada), el control
   Dirac 1D, y las lecturas c_H > c_0 y ausencia de c_{ω²} isótropo.
6. SCOPE_AND_CODE: veredictos Ha REFUTED_BY_ROW_L6a, Hb y Hc
   CONFIRMED_IN_DECLARED_ROWS, TABLE_PARTIAL; ¿hay checks tautológicos o
   que no prueban lo que dicen?; ¿alguna afirmación excede la lista
   declarada (ley general, rigidez, novedad)?

Entrega hasta 2400 palabras en español, con ecuaciones y contraargumentos
precisos. Cada reparación obligatoria debe identificar la ecuación o línea
afectada, qué falla y qué cerraría la objeción. Distingue aclaración de
fallo matemático. Da dictamen global y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente. No exijas filas, fuentes ni cálculos
que el contrato no declara.
---
