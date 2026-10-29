# Re-revisión sellada de la adenda de reparación — informe Eon de referencia gaussiana proyectada

Fecha: 2026-10-28. Autorización directa del usuario: «revisa la adenda». La adenda la escribió Claude Opus 5.5, así que no puede autorrevisarse. Se envía al mismo revisor (DeepSeek), que en su ronda anterior planteó las objeciones G-R1-01 a 06. La sesión es sellada y no tiene memoria de esa ronda, por eso se adjunta su informe.
Objetivo: comprobar que la «Adenda de reparación — 2026-10-28» resuelve las objeciones y no introduce errores. Sobre todo, la reparación 4 (base |E>' y coeficiente a) y el rechazo de G-R1-01/06.
Documentos: el informe con la adenda al final (commit `3395c1c`), el informe previo de DeepSeek, el PDF primario arXiv:2205.03148v4 y `scripts/verify_eon_projected_gaussian_reference.py`.
Máximo: una ronda; un reintento operativo solo si falla el transporte. Herramienta: revision-ciega, ~/herramientas `1656820`. No promueve evidencia.

---
Responde en español. Revisión matemática adversarial, una sola ronda, sesión sellada: solo tienes los adjuntos.

Documento 1: informe sobre un candidato a estado de referencia materia–gauge en el QCA QED de Eon et al., con una prueba Fourier/Jensen de que no es estacionario. Al final lleva una «Adenda de reparación — 2026-10-28». Documento 2: un informe de revisión anterior (objeciones G-R1-01 a G-R1-06) que motivó la adenda. Documento 3: el artículo primario (texto extraído; las fórmulas pueden tener defectos). Documento 4: el verificador.

Revisa SOLO la adenda y su encaje con el texto que sustituye:

1. Reparación 1. La adenda rechaza G-R1-01/06 alegando que el revisor intercambió f y g. Comprueba en §3.C del texto original qué serie es f y cuál es g. Comprueba si, con la convención fijada (`exp[i theta B] f = lambda g`), la desigualdad del arco y la cota `abs(f) <= exp[-abs(theta a) r/2+O(1)] abs(g)` son correctas, incluidos los términos b/z y c. Comprueba también si el control inverse-kick es coherente. Si G-R1-01 era correcta, dilo.
2. Reparaciones 2, 3 y 5. ¿Son correctas y suficientes?
3. Reparación 4, la principal:
   a. ¿Basta la conmutación de los V (ec. (4) del PDF) para que `|E>' := V_1^{E_1}···V_M^{E_M}|0>` esté bien definido, sea ortonormal y convierta cada V_ℓ en un desplazamiento puro? Revisa si los V actúan de forma diagonal en las ocupaciones fermiónicas, si cambian otros registros, y qué ocurre con la estructura de dos campos gauge por enlace (rishons) del PDF. ¿Es legítimo reducirla a un entero E_ℓ por enlace?
   b. ¿Es exacto que, en esa base, D_M multiplica la serie por `exp[i theta B(z)]`, con signos ±1 fijos en los monomios de plaqueta? ¿Pueden aparecer fases que dependan de E y no sean constantes?
   c. ¿Son las cuatro plaquetas que contienen un enlace, para L>=3, monomios de Laurent distintos en los otros enlaces? ¿Es entonces a ≢ 0 para cualquier elección de signos?
   d. ¿Es correcto retirar «a=4» y decir que el recuento del certificado no certifica a?
4. ¿Queda alguna frase del texto original que contradiga la adenda?

Da un veredicto por reparación y global: PASS, PASS_WITH_REPAIRS o FAIL, con reparaciones obligatorias numeradas. Distingue error demostrado, laguna y redacción. Marca NO VERIFICADO lo que dependa de fórmulas ilegibles o de fuentes ausentes.
---
