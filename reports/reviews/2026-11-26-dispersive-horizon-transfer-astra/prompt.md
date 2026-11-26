# Revisión externa: matriz de transferencia 12×12 del paseo con horizonte dispersivo

Autorización: usuario «que la haga AStra» (2026-11-26). Autor de la derivación
revisada: no registrado en el informe (`8e5b540`). Autor de la auditoría y del
verificador: Claude (Opus 5.5), commit `d0114b2`. Revisor: GPT-6 Astra (OpenAI),
otra familia, mediante `revision-ciega astra` del PATH; generación comprobada
antes del envío. Herramientas: `~/herramientas` commit `4a4fcca`. Máximo: una
ronda. No se autoriza calcular transmisión ni promoción. Cierra el encargo: un
informe completo de esta ronda.

---
Revisa adversarialmente, de forma independiente, la matriz de transferencia
espacial 12×12 del paseo cuántico unitario

U = L₋ W²,   W = S C(θ) S C(θ) S C(−2θ),

y la auditoría de esa matriz hecha por otro modelo. Se adjuntan tres
documentos:

(A) el informe del autor (`2026-11-26--dispersive-horizon-three-step-transfer.md`),
    que define el operador (§2, §4) y la matriz (§6);
(B) la auditoría (`2026-11-26--dispersive-horizon-transfer-matrix-audit.md`),
    con veredicto PASS en alcance algebraico;
(C) el verificador SymPy exacto de la auditoría
    (`verify_dispersive_horizon_transfer_matrix.py`, 61 comprobaciones).

**Orden obligatorio:** deriva primero tú la matriz desde el operador de (A),
sin mirar (B) ni (C). No presupongas que la matriz publicada es correcta.
Solo después contrasta con (B) y (C). La auditoría (B) la escribió un modelo;
no es fuente.

Comprueba, informando para cada apartado PASS / REPAIR_REQUIRED / FAIL /
UNVERIFIED, con las derivaciones necesarias:

1. Convenciones: C(β) = [[cos β, −sin β], [sin β, cos β]] = exp(−iβσ_y);
   S|x,↑⟩ = |x+1,↑⟩, S|x,↓⟩ = |x−1,↓⟩; L₋|x,s⟩ = |x−1,s⟩. Determina tú el
   orden efectivo de las seis monedas y verifica q₇(x+1) = z q₁(x).
2. Matriz: relaciones entre a_j(x) y b_j(x); vector
   Y_x = (a₁(x)…a₆(x), b₁(x−1)…b₆(x−1)); las doce filas; los cuatro bloques
   6×6 P, Q, R, H; las 144 entradas frente a (A). Atención especial a las dos
   ecuaciones de cierre y a los coeficientes evaluados en x+1. Demuestra o
   refuta con un contraejemplo concreto que la recurrencia equivale a
   Uψ = zψ y que no introduce soluciones espurias.
3. Determinante: det M_x(z) = cot θ_x / cot θ_{x+1}, algebraicamente:
   independencia de z, signo, ausencia de factores extra, perfil variable,
   valor 1 en el caso homogéneo.
4. Dispersión homogénea: con t = cos²θ, A = t(2t−1), comprueba
   cos E = A cos 3k + (1−A) cos k desde el operador, y que con λ = e^{−ik}
   la condición de autovalor de M equivale a
   z²λ⁵ − zλ⁶[4f_t(λ)² − 2] + λ⁷ = 0. Grado, multiplicidades,
   correspondencia con los modos de Bloch y degeneraciones de Floquet
   (en particular (z, λ) = (i, −i)).
5. Adicionales: soporte microscópico [−7, 5]; ausencia de denominadores
   nulos para t ∈ [5/16, 7/16]; velocidades IR y UV del §5 de (A); la
   continuidad de la rama Ω₊ en (0, π/2] que (B) añade.
6. Auditoría y verificador: ¿cada afirmación de (B) está respaldada por una
   derivación o por una comprobación de (C) que de verdad la decide? Busca
   comprobaciones vacuas, tests de cero que puedan dar falso positivo,
   controles negativos insuficientes, o afirmaciones de (B) que excedan lo
   que (C) certifica. Distingue lo que (C) certifica de lo que solo se
   argumenta por escrito.

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que
derivas a mano de lo que solo inspeccionas. No calcules el coeficiente de
transmisión ni evalúes la originalidad. Separa reservas de interpretación
física de los resultados algebraicos.

Entrega en español: un veredicto por apartado, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas,
objeciones ordenadas por gravedad con sección y reparación concreta, y
respuesta expresa a: ¿se puede usar matemáticamente la matriz M_x(z)
publicada como punto de partida fiable para estudiar la transmisión
estacionaria a través del perfil tanh? Si no hay fallos, dilo sin inventar
objeciones.
---
