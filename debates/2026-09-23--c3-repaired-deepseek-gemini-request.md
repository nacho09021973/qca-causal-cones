# Encargo de revisión C3 reparado — DeepSeek y Gemini

Revisión solicitada por el P.I. después de la revisión interna de Astra.
Revisores: ABNER (DeepSeek) y GEMINI (Google). Autor del objeto: Codex.

## Integridad

- Objeto: `reports/2026-09-23--c3-conditioning-execution.md`.
- Commit del objeto: `479a25d6bb19c961abb386e53cbf3b7689811767`.
- SHA256 del objeto: `030e2396a1f209ac9f86f8392d1c634f8175c5dd605fc22de3f24c10869118de`.
- HEAD de preparación del corpus: `06629bd5478d074d803ee81b9c796e299faba1ac`.
- Herramientas compartidas: `1ce73d26a5fc116c2ab83fa6f3b55d24f9110aa4`.
- Sanedrín: `8162508e3bd0e3d05770b4dd544fe7c962d0272c`.

Estos identificadores han sido comprobados por el coordinador; los revisores
sellados no deben afirmar haber ejecutado git o sha256sum.

## Tarea

Auditar de nuevo las cinco obligaciones de `theory/IR_C3_CONDITIONING_GATE.md`:

1. Estados condicionados, probabilidades de éxito, identidad exacta de
   `Lcond` y su diferencia con `LPP`, incluida la asignación de los bits.
2. Identificación exacta de la fuga con C1, cuatro encoders y constante
   `B=Phi_0(1/4)`, `D=1024 pi^2 B^2/5>0`.
3. Definición de `h_N`, producto escalar de red, campo libre del Lema 7.2,
   paso de la suma a la integral, positividad de `p_infty`.
4. Aplicación de C2c a las cuatro filas `D_0=I` y derivación de (C3.7),
   distinguiendo cotas suficientes de las más fuertes disponibles.
5. Respeto del alcance: sólo los cuatro encoders originales, Bob `I`,
   protocolo congelado. No ampliar a otros detectores o QCA. El líder de
   `Lcond`, su valor absoluto y la comparación con L quedan fuera del
   dictamen; no confundir ese límite contractual con una cancelación posible.

C1 y C2c son entradas ya aceptadas en el estado canónico. Comprobad la
aplicabilidad y la trazabilidad de esas entradas; no es un encargo para
redemostrar íntegramente C2c ni ampliar sus requisitos. Se adjuntan tanto
las derivaciones como sus revisiones para que no falten las fuentes citadas.
La revisión interna de Astra es un argumento sometido a crítica, no una
autoridad ni una revisión independiente que debáis ratificar por defecto.

No usar datos N=24/40, simulaciones, cuadraturas, barridos, L-LPP o la
conclusión del Teorema 4.4. El Lema 7.2 y su prueba autónoma sobre el recurso
sí se someten a revisión: su ubicación en el manuscrito no implica importar
la ley de la señal total. No reabrir H1c, FR1–FR3 ni E/AdS.

Cada miembro debe emitir PASS/INCOMPLETE/FAIL para las cinco obligaciones
y su propio veredicto global, tanto en su primera intervención como en su
residuo final. Si hay reparación, citar la ecuación/pasaje preciso y qué
argumento falta. Distinguir mejoras opcionales de bloqueos matemáticos.

Veredictos globales: `C3_PROOF_WRITTEN_REVIEW_ACCEPTED`,
`C3_REPAIR_REQUIRED`, `C3_FAIL` o `C3_INCOMPLETE`. La aceptación se refiere
al objeto identificado, no autoriza una promoción canónica ni equivale a
verificación humana. Una ausencia, cuota o fallo no cuenta como acuerdo;
conservar `DEGRADED_NO_CONSENSUS` si ocurre. No modificar archivos.
