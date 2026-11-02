# Re-revisión acotada del gate DISPERSION_CORRECTIONS_ACROSS_LATTICES tras reparaciones

Autorización explícita del usuario: «adelante» (2026-11-02), en respuesta a
la petición de revisar las tres reparaciones con Gemini y Grok. No autoriza
publicación ni promoción. Autor: Claude (Anthropic). Revisores: Grok
grok-4.7 y Gemini gemini-4-argon, vía revision-ciega, en paralelo.
Snapshot revisado: 9557aa9; reparado: 4a45280. Una revisión por casa,
1800 s. Herramienta: ce09890a0d5f68a6634f358eff2e477ac5f15ec7.

---
Re-revisión acotada. Se adjuntan: el contrato congelado, el registro de
revisiones (resume las tres reparaciones obligatorias de Grok y las notas
de Gemini), el diff exacto entre el snapshot revisado y el reparado, y el
informe y el verificador reparados completos. Los cinco scripts de los que
el verificador importa símbolos no cambian y no se adjuntan. No tienes
herramientas: no ejecutes, edites ni navegues; el código se lee como texto
y no confirmes recuentos.

No se reabre lo ya aceptado por las dos casas (método de series, bloques,
simetría, valores tabulados, veredictos Hd/He/Hf), salvo que el diff lo
altere. Dictamen PASS / REPAIR_REQUIRED por punto:
R1. Signo de β en L3s4: con β = β0 + β3 n1 n2 n3, β0 = ±√3(1−a²)/(6a),
    β3 = ±√3(2a²−1)/(3a) y |n1 n2 n3| ≤ 1/(3√3), ¿es correcto que β
    conserva un signo en la esfera si y solo si a² < (19 − 6√3)/11? ¿Es
    correcto el nuevo texto de la Sec. 3.3 (incluida la dependencia del
    signo de β0 con el cúmulo y la rama)? ¿Certifica el nuevo record lo que
    dice (numerador 11a⁴ − 38a² + 23, una raíz en 0 < a < 1, evaluación en
    la frontera y signos a cada lado)?
R2. ¿Es correcta la nueva frase de la Sec. 1 sobre L5a y los bloques de
    L5b, y concuerda con lo que el verificador lista?
R3. ¿Tiene el record de Hd un predicado que puede fallar, y certifica que
    el signo de α0 está decidido en todas las filas (signo exacto de cada
    α0 numérico, tabla de Sturm completa y contigua en (0, 1) para L3s4)?
R4. Regresiones: ¿introduce el diff algún error, alguna afirmación que
    exceda el contrato, o algún cambio de valor o veredicto?

Hasta 1200 palabras en español. Dictamen global y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
