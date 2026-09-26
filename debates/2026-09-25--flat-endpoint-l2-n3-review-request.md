# Revisión independiente estrecha: extremos planos en ℓ² inclinado

Fecha: 2026-09-25. Autor de la derivación: Claude (familia Anthropic).
Objeto: `2026-09-25--flat-endpoint-l2-n3-derivation-DRAFT.md` (adjunto).
Revisores solicitados: familias distintas de Anthropic. Una sola ronda. No
es un Sanedrín completo ni un comité.

## Pregunta y límite

¿Demuestra el borrador \(\|f_N\|,\|w_N\|_{\ell^2_{\rm tilt}}=O(N^{-3})\) para
los extremos planos heredados, en la norma que empareja con Schur (8)?
Intentad refutarlo. El estado declarado en el borrador no es evidencia.
Rehaced cada paso desde las definiciones del TeX y del informe regional.

## Cuatro criterios, puntuados por separado

1. **Cota puntual \(O(N^{-7/2})\):** ¿es uniforme en \(x\), \(u\) y \(N\)?
   ¿Oculta factores que crezcan en \(j\), en la dirección tangencial o en
   \(N\)? Comprobad (1a) \(\sup|b_N|=b_N(0)\) con \(g\ge0\); (1b)
   \(\sup|r|\le\int|\hat\phi_N|\) por unitariedad de \(S(p)\); (1c)
   \(F_N=64\varepsilon_\perp^2/N^2\) exacta y \(\varepsilon_\perp\le\delta\);
   (1d) el signo del peso.
2. **Conteo y suma:** ¿es correcto \(\#_j\le CN(1+j)\), con celda de diámetro
   \(\sqrt6\) y covolumen \(\sqrt3\)? ¿Da la suma cuadrática \(O(N^{-6})\) con
   el \(q(j)\) real?
3. **Norma de Schur:** ¿coinciden exactamente la inclinación \(\xi_*\), los
   centros, \(\Lambda=e^{\Phi_*}\), Parseval con \(d\mu=d^3p/(2\pi)^3\) y el
   embebido en \(\mathbb C^4\) con la norma P de Schur (6)–(8)? Señalad
   cualquier diferencia de peso, variable, medida o normalización.
4. **Alcance:** ¿queda limitado a los extremos planos, sin transferir nada al
   contrato de dos canales ni a \(r_c\)? ¿Se insinúa `N^{-7}`?

Para cada objeción: ecuación, contraejemplo y reparación. Clasificad cada una
como FATAL, REQUIRED_REPAIR u OPTIONAL. Si no hay objeción, decidlo sin
inventarla.

**Veredicto:** `PASS`, `PASS_WITH_REPAIRS` o `FAIL`.

No revisar Schur (8) en sí, ni H1c, Volterra, cancelaciones o las piezas
lineales. No proponer nuevos frentes.

## Snapshot

Base: `863fe8e86e2174a2b96fc38635d179e9114b2ce6`.

| Archivo | SHA256 |
| --- | --- |
| papers/ir-corona/ir-corona.tex | 05a2eb09d2f103608683978c292de939511359677727982de441970f2e655636 |
| reports/2026-09-17--regional-laplace-coefficient-gate.md | 8d0af529559887bdfa6cba125a23bc1629c19a96c7ba2adcb8c378f6a3294623 |
| reports/2026-09-17--scaled-ir-signaling-gate.md | 86a086dcc7e13f65dafc4f1003f7fe6d6801156a659b2b179f1fa8f2884fcf92 |
| reports/2026-09-24--h1c-return-kernel-schur-audit.md | ac92cb8c10fa49a94dd36387846e38ce3a8885bfbdc2b0c8001e407f046e4e9b |
| reports/2026-09-24--h1c-exact-dyson-decomposition.md | 0c911bea4176e6ed1a84eb21f95eae30d9957019d4b4ddcff0386a2d1252efd7 |
| reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md | ab06bb4136a4a96565670bc87d66eb6c8b13679abc7f9f3db31cfbe0b58dee9d |
| state/CURRENT_STATE.md | 99eb8024b4643bf319d69259fed2fd76efe61f0d674c5ad2fca9cdb18262931e |
