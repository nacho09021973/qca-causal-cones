# Revisión externa: Enmienda 3 de la auditoría de la matriz de transferencia

Autorización: usuario «SI, HAZ LA enmienda tres y pasala a Astra» y «si quieres
la envias tambien a Grok y asi tenemos dos opiniones» (2026-11-26). Mismo
encargo, enviado por separado a GPT-6 Astra (OpenAI) y a Grok (xAI) mediante
`revision-ciega` del PATH; generación comprobada antes del envío. Autor de la
enmienda, de la auditoría y de los verificadores: Claude (Opus 5.5).
Herramientas: `~/herramientas` commit `4a4fcca`. Revisado: commit `f9dce97`.
Máximo: una ronda. No se autoriza calcular transmisión ni promoción. Cierra el
encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la **Enmienda 3** de una auditoría matemática de la
matriz de transferencia espacial 12×12 del paseo cuántico U = L₋W²,
W = S C(θ) S C(θ) S C(−2θ), con t = cos²θ, A = t(2t−1), perfil
t ∈ [5/16, 7/16] y horizonte t = 3/8. La Enmienda 3 responde a una revisión
de la Enmienda 2 (texto de un modelo, adjunto: no es fuente). Se adjuntan:

(1) `amendment3.diff`: el diff exacto de la auditoría introducido por la
    Enmienda 3;
(2) la auditoría completa, con las Enmiendas 1–3;
(3) el informe de revisión de la Enmienda 2 al que responde;
(4) `verify_dispersive_horizon_transfer_amendment3.py`: el verificador nuevo
    (10 comprobaciones);
(5) `verify_dispersive_horizon_transfer_amendment2.py`, que (4) importa sin
    modificarlo (y que a su vez importa los verificadores anteriores, no
    adjuntos: 61 + 8 comprobaciones ya revisadas).

Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL /
UNVERIFIED, con las derivaciones necesarias:

1. **Jordan 3+1 en t = 3/8, (z, λ) = (±1, ±1).** ¿Prueban las nulidades
   dim ker (M − λI)^j = 2, 3, 4, 4 (j = 1..4) la partición 3+1? ¿Es fiable el
   cálculo de rango exacto con `DomainMatrix` sobre ℚ(√6, √10), incluida la
   conversión de las entradas (con √6/4, √10/4 y productos) a ese cuerpo?
   Si puedes, confírmalo a mano por otra vía.
2. **Contacto exacto (u−1)² (J2).** ¿Decide la comprobación que (u−1)³ no
   divide?
3. **Borde interior en t = 5/16.** Comprueba la identidad
   P_t(u(k)) = sin²E · v(v+2), v = 2E′ − 1 en la rama saliente; la
   derivación P_t′(u*)u′(k*) = 2 sin²E(k*) Ω₊″(k*) en el cero de v; los
   signos P_t′(u*) = −(3/1024)(1−u*)√168025 < 0, u′(k*) < 0, sin E > 0; y la
   conclusión Ω₊″(k*) > 0 (mínimo), multiplicidad algebraica 2, geométrica 1,
   un bloque de Jordan 2. ¿Separa la enmienda correctamente lo certificado
   (B1–B3) de los pasos escritos?
4. **Redacción t = 7/16.** ¿Queda correcta la afirmación sobre el cociente
   P_t/(u−1) y el tratamiento del extremo u = 1 (k = 0)?
5. **Verificador (4).** ¿Deciden sus 10 comprobaciones lo que dicen? Atención
   a: conversiones al cuerpo algebraico; la comprobación B2 de 0 < u* < 1 por
   comparación entera; la cadena lógica de B3 (g(0) = 0, g(1) = 1,
   g′ ≥ g′(1) = 1/16 por ser A < 0); posibles falsos positivos; la aserción
   final de recuentos.
6. **Alcance y atribución.** ¿Atribuye la Enmienda 3 a cada verificador
   exactamente lo que certifica? ¿Presenta como verificado algo que solo es
   un argumento escrito? ¿Queda algún punto [UNVERIFIED] mal etiquetado?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que
derivas a mano de lo que solo inspeccionas. No revises de nuevo las 144
entradas ni las Enmiendas 1–2 salvo que la Enmienda 3 las afecte. No calcules
transmisión, canales asintóticos ni originalidad.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y
objeciones ordenadas por gravedad con sección y reparación concreta. Si no hay
fallos, dilo sin inventar objeciones.
---
