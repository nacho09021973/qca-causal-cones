# Re-revisión acotada del gate C_ACROSS_LATTICES tras reparaciones

Autorización explícita del usuario: «si, autorizado» (2026-11-01), a la
propuesta de reparar y hacer una re-revisión acotada con ciro y,
opcionalmente, gemini. No autoriza publicación ni promoción.
Autor: Claude (Anthropic). Revisores: Grok grok-4.7 y Gemini
gemini-4-argon, vía revision-ciega, en paralelo. Base revisada: aab5e7b;
snapshot reparado: 8d0276e. Una revisión por casa, 1800 s.
Herramienta: ce09890a0d5f68a6634f358eff2e477ac5f15ec7.

---
Re-revisión acotada. Se adjuntan: el contrato congelado, el registro de
la primera revisión (que resume las tres reparaciones obligatorias de
Grok y las aclaraciones de ambas casas), el diff exacto entre el
snapshot revisado y el reparado, y el informe y el verificador reparados
completos. No tienes herramientas: no ejecutes, edites ni navegues; el
código se lee como texto y no confirmes recuentos.

El alcance es acotado: no se reabre la física ya aceptada por ambas casas
en los bloques 1–5, salvo que el diff la altere. Dictamen
PASS / REPAIR_REQUIRED por punto:
R1. Asertos de tabla: ¿cada valor tabulado del informe (conjuntos de
    pasos, índices, r_in, c_0, número de vértices, matrices de Gram, K)
    queda ahora cerrado por un record exacto que falla el proceso si
    cambia? ¿Coinciden los valores esperados del código con las tablas
    del informe? ¿Algún aserto nuevo es tautológico?
R2. Orden del producto: ¿el informe ya no presenta el acuerdo con la
    velocidad continua como test del orden de Π en JDW (2) y (8), y
    declara que K y coeficientes de vértice pueden depender de él?
R3. Tokens Hb/Hc: ¿el informe y el código evitan
    CONFIRMED_IN_DECLARED_ROWS con L6b OPEN y usan formulación correcta?
R4. Aclaraciones: identidad de Duhamel con el factor e^{iθQ} y su
    consecuencia (Gram de B igual a la de dH cuando X_par = 0); distinción
    del grupo fino de L6c; signo de Fourier k → −k; docstring.
R5. Regresiones: ¿introduce el diff algún error nuevo o alguna afirmación
    que exceda el contrato?

Hasta 1200 palabras en español. Dictamen global y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
