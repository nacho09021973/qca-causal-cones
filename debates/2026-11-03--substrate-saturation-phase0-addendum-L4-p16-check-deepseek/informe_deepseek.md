<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 b6454b30476687995ebcd28233377bf5199b62319b68031893a491c9b6790b63
inicio: 2026-11-03T18:23:10Z  fin: 2026-11-03T18:25:03Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0-addendum-L4.md ; último commit observado: 738b62c ; sha256 de la copia enviada b8b9ed87d5df373ea152c54252a5034bfbc30bebd4222ada0d2f387a896dd8b8
documento: /home/ignac/qca-causal-cones/debates/2026-11-03--substrate-saturation-phase0-addendum-L4-p16-check-deepseek/cjww_p16.txt ; último commit observado: sin versionar ; sha256 de la copia enviada e19e2c12ddc2f473f0c011224ecefa029bb7416611da303924261f94c74b3dfa
entrada_deepseek.txt sha256 2b876454fd52842a06e35cb4e86c89f54a0f69991b48dca486aa56716f94578a
respuesta sha256 51ea4ac4c2393c3a4f8fe0dc8676b61252631e1c700734ed2e2491d95b13f78e
-->

Dictamen: **PASS**.

Comparación punto por punto contra `cjww_p16.txt`:

1. **(5.12) y \(K=\mathbb{C}^2\)**  
   El extracto dice literalmente:  
   «We then have K = C2 , and  
   \(W (p1 , p2 , p3 ) = eip1 σ1 eip2 σ2 eip3 σ3 .\) (5.12)».  
   El addendum escribe \(K=C^2\) y  
   \(W(p_1,p_2,p_3)=e^{ip_1\sigma_1}e^{ip_2\sigma_2}e^{ip_3\sigma_3}\).  
   Salvo el aplanado de superíndices por `pdftotext` (`C2` por \(C^2\)), la correspondencia es exacta. No hay discrepancia.

2. **Frase sobre singularidades cónicas**  
   El extracto dice:  
   «A characteristic feature here are conical singularities at p = 0 and eight inequivalent points in the Brillouin zone, where p1 , p2 , p3 ∈ πZ».  
   El addendum la parafrasea como «conical singularities at \(p = 0\)» y «at the points with \(p_i\in\pi Z\)». Es una paráfrasis fiel; la omisión de «eight inequivalent points in the Brillouin zone» no contradice el texto. No hay discrepancia material.

3. **(5.14) y la presunta errata de subíndices**  
   El extracto imprime:  
   «ω(p∨ + p)2 = (p21 + p21 + p21 ) + O(p3 )».  
   El addendum interpreta:  
   \(\omega(p_\vee+p)^2=(p_1^2+p_1^2+p_1^2)+O(p^3)\),  
   con los tres subíndices repetidos como \(1\), y añade que lo pretendido debería ser \(p_1^2+p_2^2+p_3^2\).  
   Contra el texto extraído, esa lectura es consistente: los tres términos del extracto son idénticos (`p21 + p21 + p21`). La corrección \(p_1^2+p_2^2+p_3^2\) no está en el extracto, pero el addendum no la presenta como cita, sino como errata inferida y registrada.

Sobre la posible alteración de subíndices por `pdftotext`: sí, el extracto plano no permite certificar visualmente los sub/superíndices originales. Por ejemplo, `C2` representa \(C^2\) y `p1` representa \(p_1\). En (5.14), `p21` es compatible con \(p_1^2\). Además, en el propio extracto de (5.13) se distinguen `p1`, `p2`, `p3` en «cos p1 cos p2 cos p3 − sin p1 sin p2 sin p3», lo que sugiere que la conversión no tendió a igualar todos los subíndices. Por tanto, la lectura del addendum de que (5.14) está impreso con tres veces el subíndice \(1\) es plausible y no contradice el texto extraído. No obstante, la confirmación definitiva exigiría la imagen del PDF.

No encuentro discrepancias que exijan reparación.
