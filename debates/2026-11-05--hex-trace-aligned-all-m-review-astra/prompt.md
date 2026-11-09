# Revisión sellada (casa OpenAI, gpt-6-astra) del gate HEX_TRACE_ALIGNED_ALL_M

Autorización explícita del usuario (2026-11-05): «MEJOR CODEX», en respuesta
a la propuesta de revisión de otra familia. Autoriza el envío a OpenAI
(`gpt-6-astra` vía `revision-ciega astra`); no autoriza promover. Autor del
resultado: Claude Code (Claude Opus 5.5). Base: `8204822` (pushed).
Herramienta: `~/herramientas` `ce09890`. Generación comprobada antes del envío
(`gpt-6-astra` y `gpt-6.1-sol` responden «OK»). Una ronda inicial y como máximo
una re-revisión acotada de reparaciones obligatorias. Hashes en
`inputs.sha256`. No hay dictámenes previos sobre este resultado.

Comprobación previa. Sabido: contrato congelado 689fd30; verificador 20/20;
resultado del autor OPEN_AFTER_ALIGNED_ALL_M_ANALYSIS con cierre de la vía de
la recta p=2q para m>=629. Pregunta: ¿es correcta esa cadena y no afirma más
de lo que prueba? Cierre: PASS → el usuario decide; REPAIR_REQUIRED → se
repara; un fallo de fondo retira el cierre de la vía. Un fallo operativo o un
`tool_call_as_text` no es revisión.

---
Revisa de forma adversarial e independiente el informe
reports/2026-11-05--hex-trace-aligned-all-m.md, escrito por Claude
(Anthropic), contra su contrato theory/HEX_TRACE_ALIGNED_ALL_M_GATE.md, con el
verificador scripts/verify_hex_trace_aligned_all_m.py y su salida completa.
Se adjuntan como contexto el informe de m=3 (certificado en la recta p=2q,
ya revisado) y el informe del método escalar (reducción general, Sec. 3).
Nada de lo escrito por Claude es premisa: rederiva. No tienes herramientas:
no ejecutes ni navegues y no afirmes haber ejecutado código. No propongas
ampliar la investigación.

Dictámenes separados PASS / REPAIR_REQUIRED / FAIL:
1. REDUCCIÓN Y RECÍPROCO (Sec. 2). ¿Es correcto que todo h D6-invariante con
   soporte en H_(m-2) da un f = f_m^0 + Delta*h admisible (soporte en H_m,
   f(0)=1, cosenos normales), sin usar la divisibilidad? ¿Es correcta la
   divisibilidad re-derivada para m general?
2. RECTA p=2q (Sec. 3). ¿Son correctas f_m^0 = T_m^2+T_m-1 y
   Delta=(1-x)^3(1+x)/4? ¿Es exactamente la imagen de las restricciones
   V_n = {g: grado <= 2n, g'(-1/2)=0}: inclusión por el punto fijo del giro de
   120° y dimensión por las frecuencias máximas {0,2,3,...,2n}? Comprueba en
   particular las órbitas de (a,0) y (a,1) y que el coeficiente superior no se
   anula. ¿Es correcta la equivalencia con el problema en una variable
   (F(0)=1, F''(0)=-3m^2, F''''(0)=9m^4, F(pi)=(-1)^m, F'(2pi/3)=0)?
3. CONSTRUCCIÓN (Sec. 4). ¿Está F=A*B acotada por 1? ¿Son correctos los
   momentos, la positividad del exceso E=(K2^2-s^2)(s^2-K1^2), la cota
   E<36(s+3)^2, 3L^4>=243m^2, y la condición de grado para todo m>=629?
   ¿Se cumplen F(pi)=(-1)^m y F'(2pi/3)=0 por las congruencias de K y L?
   ¿De g=(P-f_m^0)/Delta sale un polinomio de grado <= 2m-4 en V_n?
4. VERIFICADOR. ¿Certifica lo que el informe dice que certifica, y declara
   bien lo que no (divisibilidad, cotas fuera de la recta, la pregunta para
   todo m)? ¿Hay alguna comprobación vacía o que pase por construcción?
5. ALCANCE Y DICTAMEN. ¿Es correcto que esto cierra solo los certificados
   apoyados en las rectas de dirección de vértice, que no es un candidato
   compatible, que 4<=m<=628 queda sin decidir y que el resultado correcto es
   OPEN_AFTER_ALIGNED_ALL_M_ANALYSIS? ¿Afirma el informe algo más fuerte de lo
   que prueba? ¿Respeta el contrato (sin barrido de radios, sin búsqueda en
   coma flotante, presupuesto, nota de tiempos)?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global PASS,
REPAIR_REQUIRED o FAIL y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente.
---
