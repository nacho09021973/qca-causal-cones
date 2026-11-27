# Revisión externa: Enmienda 2 de la auditoría de la matriz de transferencia

Autorización: usuario «astra» (2026-11-26), como encargo separado del contrato
de canales. Autor de la enmienda, de la auditoría y de los verificadores:
Claude (Opus 5.5). Revisor: GPT-6 Astra (OpenAI), mediante `revision-ciega
astra` del PATH; generación comprobada antes del envío. Herramientas:
`~/herramientas` commit `4a4fcca`. Revisado: commit `b1c6d75` (Enmienda 2).
Astra ya revisó la auditoría original (`d0114b2`); Grok revisó la Enmienda 1
(`63db34b`). Máximo: una ronda. No se autoriza calcular transmisión ni
promoción. Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la **Enmienda 2** de una auditoría matemática de la
matriz de transferencia espacial 12×12 del paseo cuántico U = L₋W²,
W = S C(θ) S C(θ) S C(−2θ), con t = cos²θ, A = t(2t−1), perfil
t ∈ [5/16, 7/16] y horizonte t = 3/8. La Enmienda 2 responde a la revisión de
Grok de la Enmienda 1. Se adjuntan:

(1) `amendment2.diff`: el diff exacto de la auditoría introducido por la
    Enmienda 2;
(2) la auditoría completa, con las Enmiendas 1 y 2;
(3) el informe de Grok sobre la Enmienda 1 (texto de un modelo: no es fuente);
(4) `verify_dispersive_horizon_transfer_amendment2.py`: el verificador nuevo
    (39 comprobaciones);
(5) `verify_dispersive_horizon_transfer_repairs.py` (8 comprobaciones), que
    (4) importa sin modificarlo;
(6) `verify_dispersive_horizon_transfer_matrix.py` (61 comprobaciones), que
    (5) importa sin modificarlo.

Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL /
UNVERIFIED, con las derivaciones necesarias:

1. **Gemelo (z, λ) = (−1, −1) en t = 3/8.** Deriva a mano, desde
   cos E = A cos 3k + (1−A) cos k y Ω± = −k ± 2E, que la multiplicidad
   algebraica es 4 y la geométrica 2 (vectores de Bloch en k = π, con
   S(π) = −I e Y = (a_j, b_j/λ)).
2. **Extremos t = 5/16, 7/16.** ¿Es (±1, ±1) doble y semisimple en ambos?
3. **Coeficiente cúbico.** ¿Es E = k/2 + (35/64)k³ + O(k⁵) en t = 3/8, y por
   tanto Ω₊ = (35/32)k³ + O(k⁵)? ¿Decide G3 eso?
4. **Borde de banda interior.** Sobre (0, π/2), ¿equivale v₊ = 0 a
   4(1−u)g′(C)² = 1 − g(C)² (u = cos²k, C = cos k, g(C) = 4AC³ + (1−4A)C),
   incluida la reversibilidad del paso al cuadrado? ¿Es correcto el polinomio
   en t = 5/16, proporcional a (u−1)(2625w² + 5w − 16) con w = u − 1, con una
   sola raíz u ∈ (0,1)? ¿Y el factor (u−1)² en t = 3/8 y la ausencia de raíces
   en [0,1] en t = 7/16? ¿Cuenta bien la función de Sturm las raíces,
   incluidos los extremos?
5. **Los dos puntos que la Enmienda 2 deja [UNVERIFIED].** Intenta decidirlos
   a mano o di qué falta:
   (a) partición de Jordan en (z, λ) = (±1, ±1), t = 3/8: 3+1 frente a 2+2;
       el criterio son las nulidades de (M − λI)^j (para 3+1: 2, 3, 4; para
       2+2: 2, 4) o un argumento de Puiseux sobre λ(z) cerca de z = ±1;
   (b) en el borde de t = 5/16: Ω″ ≠ 0 en el punto de velocidad nula y, por
       tanto, raíz doble no semisimple (autoespacio de dimensión 1).
6. **Verificador (4).** ¿Deciden sus 39 comprobaciones lo que dicen? En
   particular: el bucle de multiplicidad y la comprobación de no anulación del
   cociente; la construcción de los vectores de Bloch para λ = −1; el menor
   10×10 como cota de rango; `roots_in_open_unit` y el tratamiento de las
   raíces en los extremos; posibles falsos positivos; si importar (5) y (6)
   puede enmascarar un fallo.
7. **Alcance y atribución.** ¿Atribuye la Enmienda 2 a cada verificador
   exactamente lo que certifica? ¿Presenta como verificado algo que solo
   argumentan Astra o Grok?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que
derivas a mano de lo que solo inspeccionas. No revises de nuevo las 144
entradas ni la Enmienda 1 salvo que la Enmienda 2 las afecte. No calcules
transmisión, canales asintóticos ni originalidad.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y
objeciones ordenadas por gravedad con sección y reparación concreta. Si no hay
fallos, dilo sin inventar objeciones.
---
