# Lectura del autor del cotejo de DeepSeek sobre la p. 16 de CJWW

DeepSeek (`deepseek-v4-pro`), COMPLETED: **PASS**. (5.12) con `K = C^2`,
la frase sobre los puntos cónicos y la lectura de (5.14) coinciden con el
texto extraído; señala que el texto de pdftotext no certifica los
subíndices y que la confirmación definitiva exigiría la imagen del PDF.

Segunda vía (autor, en esta sesión): página 16 del PDF
(`sources/2408.02108v1.pdf`) renderizada a imagen con `pdftoppm -r 150` e
inspeccionada visualmente. La imagen muestra `K = ℂ^2`,
`W(p_1,p_2,p_3) = e^{i p_1 σ_1} e^{i p_2 σ_2} e^{i p_3 σ_3}` (5.12), y
(5.14) impresa como `ω(p^∨ + p)^2 = (p_1^2 + p_1^2 + p_1^2) + O(p^3)`: la
errata está en el original, no en la extracción. Imagen no conservada
(inspección manual, sin resultado numérico).
