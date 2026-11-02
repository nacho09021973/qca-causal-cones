# Re-revisión acotada del gate HEX_CEILING tras reparaciones

Autorización explícita del usuario: «si, con ciro y gemini» (2026-11-02).
No autoriza publicación ni promoción. Autor: Claude (Anthropic).
Revisores: Grok grok-4.7 y Gemini gemini-4-argon, vía revision-ciega, en
paralelo. Snapshot revisado: 61232d7; reparado: bb4fcdb. Una revisión por
casa, 1800 s. Herramienta: ce09890a0d5f68a6634f358eff2e477ac5f15ec7.

---
Re-revisión acotada. Se adjuntan: el contrato congelado, el registro de
revisiones (resume las dos reparaciones obligatorias de Grok y las notas
sobre Gemini), el diff exacto entre el snapshot revisado y el reparado, y
el informe y el verificador reparados completos, con el módulo auxiliar
que importa. No tienes herramientas: no ejecutes, edites ni navegues; el
código se lee como texto y no confirmes recuentos.

No se reabre lo ya aceptado (T1 salvo el check del rango, el paso de
saturación, el certificado mínimo), salvo que el diff lo altere. Dictamen
PASS / REPAIR_REQUIRED por punto:
R1. Lema B: ¿es completa y correcta la prueba de la desigualdad de
    Bernstein escalar (reducción al caso real con R = Re(e^{iα}p),
    perturbación (1-ε)R, elección de β ∈ (-π,0), recuento de ceros: 2N
    arcos más dos ceros extra en el arco de s_0, frente a ≤ 2N ceros de un
    polinomio trigonométrico no nulo de grado N, caso simétrico)? ¿Cierra
    L0 como PROVED_IN_REPO según la sec. 2 del contrato?
R2. Rango: ¿el nuevo record afirma un menor 2×2 igual a la constante
    √3 l^4/2, independiente de θ_0, y eso certifica rango 2 para todo θ_0?
R3. Aclaraciones: hermiticidad de A en L0; módulo máximo en T2; el
    hexágono fija el denominador 2l; ξ como componente.
R4. Regresiones: ¿introduce el diff algún error o alguna afirmación que
    exceda el contrato?

Hasta 1200 palabras en español. Dictamen global y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
