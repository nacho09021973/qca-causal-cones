# Revisión independiente del gate HEX_CEILING

Autorización explícita del usuario: «si, con gemini» (2026-11-02). Autoriza
este envío externo a Google; no autoriza publicación ni promoción.
Autor: Claude Code (Claude Opus 5.5, Anthropic). Revisor: Gemini
gemini-4-argon (Google), vía revision-ciega. Grok no participa (saldo
agotado en la última prueba). Base: 61232d7. Una revisión, 1800 s.
Herramienta: ce09890a0d5f68a6634f358eff2e477ac5f15ec7.

---
Revisa de forma adversarial e independiente la ejecución del gate
HEX_CEILING: el informe 2026-11-01--hex-ceiling.md y el verificador
verify_hex_ceiling_gate.py (que importa sin modificarlas funciones de
verify_c_across_lattices_gate.py, adjunto), escritos por Claude
(Anthropic), contra el contrato congelado HEX_CEILING_GATE.md adjunto.
También se adjunta un script exploratorio que el informe declara sin valor
probatorio. Reconstruye las afirmaciones; el informe no es premisa. No
tienes herramientas: no ejecutes, edites ni navegues; el código se lee como
texto y no confirmes el recuento 24/24.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. L0: reducción a rejilla de frecuencias a lo largo de la normal de
   faceta (h·Rot90(d) ∈ (√3/2)Z), simetría del hexágono, aplicación de la
   desigualdad de Bernstein escalar a ⟨y, U x⟩ y paso ||A(n_f)|| = c_0.
2. T1: reducción de un walk n=3 antipodal con nodo a la forma producto
   ∏ exp(-i(k·a_j)τ_j); isotropía ⇔ solapes iguales; c_0^2 = (3/2)l^2(1-g);
   g ≥ -1/2; normalización por 2l; supremo √3/2 y su alcance; lectura
   ADMP (g=1/3) frente a JDW (g=-1/2).
3. T2_SATURATION_STEP: si c_0 = r_in, ¿se sigue U(t n_f) = e^{-irt}P_+ +
   e^{irt}P_- exactamente? Comprueba el argumento con P(z)=z^N p, el lema
   de Julia / caso de igualdad de Bernstein, y la deducción de las sumas
   por capas.
4. T2_MINIMAL_CERTIFICATE: forma normal (rotaciones de Bloch y espaciales,
   escala), estructura de capas, A_0 = -I/2, que el sistema de unitariedad
   esté completo (UU† y U†U para todo d), y que el polinomio de la base lex
   con discriminante -1/12 implique ausencia de solución real. ¿Es correcto
   el control positivo del cuadrado y prueba algo?
5. SCOPE_AND_CODE: veredictos (L0 PROVED_IN_REPO, T1 GAP_PROVED_IN_CLASS,
   T2 PROVED_FOR_MINIMAL_SUPPORT y OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS);
   ¿checks tautológicos?; ¿afirmaciones que exceden la clase W_hex, s=2 o
   la subclase probada?; ¿se trata bien el script exploratorio?

Hasta 2400 palabras en español, con ecuaciones y contraargumentos precisos.
Cada reparación obligatoria debe identificar la ecuación o línea afectada,
qué falla y qué cerraría la objeción. Distingue aclaración de fallo
matemático. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente. No exijas resultados que el contrato no pide.
---
