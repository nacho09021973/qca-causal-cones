# Revisión ciega, ronda 2 — reparaciones de la etapa (a) del charter s=2

Fecha: 2026-10-29. Autorización del usuario: «si» a aplicar G-S0-01..03 y devolverlo a Grok, y
después «adelante».
Objetivo: comprobar que el certificado y el informe reparados (commit `3bcf7b6`; certificado
`a2abbe32…`, informe `3f1b9e4b…`) resuelven G-S0-01..03 sin introducir errores. Hace falta porque
el certificado cambió después de la ronda 1 (charter, Sec. 6).
Resultado esperado: un veredicto por reparación (RESUELTA / PARCIAL / NO RESUELTA), los errores
nuevos G-S0-R2-NN y un veredicto global ACCEPT / ACCEPT_WITH_REPAIRS / REJECT.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI), en sesión sellada y sin memoria de la ronda 1, por eso se adjunta su informe.
Cierre: informe y lectura del autor en `verificacion_autor.md`. No promociona nada ni autoriza
las etapas 4a o 4b.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH; ~/herramientas `a32e189`.

---
Responde en español. Eres un revisor independiente de física matemática (grupos finitos,
representaciones proyectivas, QCA en red). Solo tienes los documentos adjuntos; no tienes
herramientas y no puedes ejecutar código. El script es un argumento que inspeccionas. No supongas
que nada es correcto.

Documento 1: el informe reparado de la etapa (a). Documento 2: el certificado reparado. Documento
3: tu informe de la ronda 1 sobre la versión anterior, con las reparaciones G-S0-01..03. Documento
4: el charter. Documento 5: utilidades simbólicas.

Comprueba:
1. G-S0-01. El certificado construye ahora `E` así:
   - Toma la permutación de ejes `sigma`, que con su convención es un antihomomorfismo
     `sigma(AB) = sigma(B) ∘ sigma(A)`.
   - Prueba que `ker sigma` es el `V4` axial.
   - Toma la representación estándar de `S3` sobre el plano de suma cero y comprueba en qué
     elementos es escalar.
   - Comprueba que hay una única clase de `O` con núcleo `V4`.
   - Comprueba que la multiplicidad trivial de `E` restringida a `D4` es 1.

   ¿Basta con esto para identificar la clase vaciada con `E`? ¿Afecta en algo que `sigma` sea un
   antihomomorfismo? ¿Es correcto calcular el carácter de `E` como «número de puntos fijos − 1»?
2. G-S0-02. ¿Es correcta y completa la prueba por órdenes de que todo subgrupo de `S4` está
   generado por a lo sumo dos elementos, tal como figura en el informe?
3. G-S0-03. ¿Fijan correctamente los nuevos `require` los recuentos 5/3/3/6/4 y los cinco
   supervivientes? ¿Es correcta la nota de que son caracteres y no órbitas de tuplas?
4. ¿Hay algún error nuevo o alguna afirmación que siga excediendo lo certificado? Revisa en
   especial la fila A2/A7 y la sección de método sobre la clasificación de los subgrupos finitos
   de `SO(3)`.

Salida: una tabla de G-S0-01..03 con su veredicto; una sección por punto; los errores nuevos con
ubicación y gravedad; un veredicto global. Si señalas un error, da el cálculo. Una sola ronda:
declara tus supuestos en vez de preguntar.
---
