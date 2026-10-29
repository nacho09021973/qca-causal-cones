# Comprobación de las fuentes — referencias de la app «Cono IR»

Fecha: 2026-10-29. Autor: Claude. Este fichero contrasta con el original lo que localizó
`informe_gemini.md`. El informe de Gemini localiza referencias; no prueba nada.

## Ejecución

- `investigacion-gemini` @ `a32e189`, modelo `gemini-4-argon`, con búsqueda de Google.
- Dos vías, ambas `COMPLETED`: `informe_gemini.md` (referencias de la app) e
  `informe_gemini_abierto.md` (pregunta abierta).
- Autorización: «busca esos papers con investigacion-gemini». Descarga: «si, descárgalos tú».

## PDF descargados

- 14 PDF bajados de `arxiv.org/pdf/<id>` a una carpeta aislada.
- Antes de copiarlos se comprobó la identidad de cada uno por el texto de su p.1.
- Están en `biblioteca/` (git-ignored), catalogados en `scripts/biblioteca_catalog/curated.csv`
  con estado `proposed`.
- El índice se regeneró con `build_catalog.py`, y ahora hay 51 PDF.

| arXiv | Fichero | Corresponde a la referencia |
|---|---|---|
| gr-qc/0005091 | `arXiv-gr-qc_0005091.pdf` | Volovik, «Superfluid analogies of cosmological phenomena» (Phys. Rept. 2001) |
| 0901.3775 | `arXiv-0901.3775.pdf` | Hořava, «Quantum Gravity at a Lifshitz Point» |
| 0906.3477 | `arXiv-0906.3477.pdf` | Iengo, Russo y Serone, «Renormalization group in Lifshitz-type theories» |
| gr-qc/0505065 | `arXiv-gr-qc_0505065.pdf` | Barceló, Liberati y Visser, «Analogue gravity» |
| 1710.05834 | `arXiv-1710.05834.pdf` | LIGO/Virgo, Fermi-GBM e INTEGRAL, GW170817 / GRB 170817A |
| 0908.1832 | `arXiv-0908.1832.pdf` | Fermi, GRB 090510. **El título en arXiv** («Testing Einstein's special relativity with Fermi's short hard γ-ray burst GRB090510») **no coincide con el de Nature** que da Gemini |
| 1109.6562 | `arXiv-1109.6562.pdf` | Cohen y Glashow. **El título en arXiv** («New Constraints on Neutrino Velocities») **no coincide con el de PRL** que da Gemini |
| 1303.5843 | `arXiv-1303.5843.pdf` | Borriello, Chakraborty y Mirizzi, neutrinos PeV de IceCube |
| 1404.7025 | `arXiv-1404.7025.pdf` | Stecker y Scully, neutrinos PeV de IceCube |
| astro-ph/0212190 | `arXiv-astro-ph_0212190.pdf` | Jacobson, Liberati y Mattingly, Crab y Cherenkov en vacío |
| 1906.08221 | `arXiv-1906.08221.pdf` | Satunin, Crab por encima de 100 TeV |
| gr-qc/0502097 | `arXiv-gr-qc_0502097.pdf` | Mattingly, «Modern Tests of Lorentz Invariance» |
| 1304.5795 | `arXiv-1304.5795.pdf` | Liberati, «Tests of Lorentz invariance: a 2013 update» |
| 0801.0287 | `arXiv-0801.0287.pdf` | Kostelecký y Russell, Data Tables (versión de enero de 2026) |

Ya estaba antes en la biblioteca: Collins et al., `arXiv-gr-qc_0403053v4.pdf`.

**Sin copia abierta (no se descargan):**
- Chadha y Nielsen, Nucl. Phys. B 217 (1983) 125, según Gemini.
- Unruh, PRL 46 (1981) 1351.
- El libro de Volovik «The Universe in a Helium Droplet» (2003).

Lo que dependa de esas tres fuentes queda `[UNVERIFIED]`. El año 1983 de Chadha y Nielsen
coincide con lo que Claude recordaba, pero no se ha leído el original.

## Afirmaciones de la app contrastadas con el original

**Collins et al. (gr-qc/0403053v4).**
- La app dice que la corrección es ∝ `g²(Λ_UV/M_Pl)²`. **Es falso.** El resumen (p.1) habla de
  violación «at the percent level, some 20 orders of magnitude higher than earlier estimates,
  unless the bare parameters … are unnaturally strongly fine-tuned». La p.2 dice «without any
  suppression by powers of E/E_P».
- La cifra «1 parte en 10²³» **no se localiza**: `grep` del texto no encuentra «10^23». El
  artículo da «20 orders of magnitude» y una cota experimental «well below 10^-20» (p.2).
- «Teorema CPSUV» es una etiqueta de la app. El artículo es un argumento de estimación con un
  ejemplo explícito.

**GW170817 (1710.05834).**
- La app dice «1.7 s». El original da un retraso de (+1.74 ± 0.05) s (resumen, p.1). Es
  correcto, redondeado.
- La cota que da el original es `−3×10^-15 < Δv/c < +7×10^-16` (resumen, p.1).

**GRB 090510 (0908.1832).**
- Fotón de 31 GeV: correcto (texto de la sección de resultados).
- La app dice «menos de 0.82 s de desfase». El original sitúa el fotón dentro de los primeros
  0.829 s tras T0. La cifra de la app parece una lectura libre de ese valor; **no es una cota de
  desfase tal como la escribe la app**.
- Las cotas que da el original para `M_QG,1/M_Planck` (Tabla 2 y el texto que la acompaña):
  - (a), la más conservadora: `> 1.19`;
  - (e), la menos conservadora: `> 102`.

**Cherenkov en vacío y electrones de unos 100 TeV.**
- Jacobson, Liberati y Mattingly (astro-ph/0212190) usan la radiación de sincrotrón del Crab,
  con electrones de hasta unos 1500 TeV.
- Satunin (1906.08221) usa el espectro de fotones del Crab por encima de 100 TeV.
- La cifra «100 TeV» de la app no se atribuye a ninguno de los dos tal como la escribe.

**Iengo, Russo y Serone (0906.3477).** Resumen, p.1: en teorías escalares de tipo Lifshitz, a
un bucle, `c²` y `δc² = c²_φ1 − c²_φ2` fluyen logarítmicamente en el UV, y si `δc² ≠ 0` en el UV
la marcha persiste en el IR; la invariancia de Lorentz no se recupera con la precisión
experimental sin ajuste fino. Esto contradice la lectura optimista de la app («z: 3 → 1 recupera
Lorentz»). Es el resultado más directamente relevante para la pregunta A.

**Volovik (gr-qc/0005091).**
- La review habla de clases de universalidad y de la «velocidad de la luz» como parámetro
  material (líneas ~239 y ~444 del texto extraído).
- En esta pasada **no se localiza** ninguna afirmación de que la topología fije una velocidad
  común entre especies, ni de «rigidez absoluta» de `c`. La afirmación de la app queda **sin
  respaldo localizado** hasta una lectura completa.

**Hořava (0901.3775), Barceló, Liberati y Visser (gr-qc/0505065), Mattingly, Liberati,
Kostelecký y Russell, y los neutrinos de IceCube.** Solo se comprobó su identidad. Su contenido
no se ha contrastado todavía.

## Vía abierta

`informe_gemini_abierto.md` lista unas 25 referencias más sobre mecanismos de universalidad,
incluidos trabajos de QCA y quantum walks. **No se han descargado ni comprobado.** Hacerlo
quedaría para la nota preliminar de A, si el usuario lo pide.
