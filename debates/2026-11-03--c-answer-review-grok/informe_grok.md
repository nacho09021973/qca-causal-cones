<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 e3383d45a55ce56e7d761208eede86f2fad4a6303fe2cd904413ca611ce7e109
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-03T10:07:33Z  fin: 2026-11-03T10:18:04Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--c-across-substrates-answer.md ; último commit observado: d3c6aae ; sha256 de la copia enviada 39ef1625d3780c3f4fd49504d0d54a9eea0bfd65e67d1c3b50b24c7d1ebad889
documento: /home/ignac/qca-causal-cones/state/CURRENT_STATE.md ; último commit observado: 56f6831 ; sha256 de la copia enviada b8e55e2b4aa0acc094c879b3feacbaba888a2fb6f286b097448d6a1c6d067edf
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--l6b-triangular-row.md ; último commit observado: a19e480 ; sha256 de la copia enviada 201a62e186976639dc351da55355820b8327dff971e0badd53a58ed9835afe4c
entrada_grok.txt sha256 109e8a4118acbe05cbcfee46fc8c2fcfbce0737d1503e53986cf42bfb6169c20
respuesta sha256 906a28b2f15625ca53d0ff9481fc2cc812855d49b67ac311186f20833e3cc149
-->

**Dictamen global: REPAIR_REQUIRED.** La síntesis no inventa un teorema ni sube de nivel las etiquetas de la Sec. 2, y la cadena del punto 0.2 no exporta la prueba de \(N_3\). Sí pierde cuantificadores, atribuye a un mismo sustrato filas que las fuentes separan, y añade frases que no están en `CURRENT_STATE.md` (CS), en el informe del techo hexagonal ni en la fila L6b.

## 1. Trazabilidad — REPAIR_REQUIRED

Cuadra con la fuente citada, entre otras cosas: \(c_0(a)=a/\sqrt{3}\) y \(c_{\mathrm{strict}}^{\mathrm{iso}}=1/\sqrt{3}\) en L3s4 (CS Sec. 4.1); \(c_0\le c_{\mathrm{strict}}^{\mathrm{iso}}\) con `PROVED_UNDER_FROZEN_CONTRACT` y una revisión, para conos admitidos y soporte exacto del símbolo completo en \(N_3\), nodos de Floquet degenerados incluidos (CS Sec. 7.2); Hc `CONFIRMED_IN_DECLARED_ROWS` tras L6b; el rechazo de la \(B_\infty^*\) fuerte en la clase declarada \(s=4\); L0, T1 y T2 con sus etiquetas (CS Sec. 12 y el informe hexagonal); la fila L6b normalizada \(r_{\mathrm{in}}=\sqrt{3}/2\), \(c_0=1/3\), \(c_0/r_{\mathrm{in}}=2\sqrt{3}/9\), \(c_{\mathrm{strict}}^{\mathrm{iso}}=1/\sqrt{3}\), cociente \(2/3\), vértices nilpotentes (informe L6b, Secs. 1 y 4, y la promoción en CS); las seis filas con término `beta` y el resto con `alpha` (CS Sec. 13); \(c_H\) y \(c_{\omega^2}\) distintos para \(0<m<1\) en la familia de Dirac estándar (CS Sec. 4 y Sec. 5); A y \(V_{\mathrm{grp}}^{\max}\) abiertos; `NO_ABSOLUTE_SCALE_DERIVABLE` en la clase plana congelada (CS Sec. 8.21).

No está en la fuente citada, o está en otra sección:

- La velocidad de grupo radial \(c_0(1+2\beta|k|+\cdots)\) y la consecuencia «\(c_0\) no es la mayor velocidad de grupo» no aparecen en CS Sec. 13. Esa sección deja \(V_{\mathrm{grp}}^{\max}\) abierto y no da el signo de `beta`.
- \(a^*\approx 0{,}412\) sustituye el valor promocionado \(a^*=\sqrt{3}\sqrt{17-\sqrt{154}}/9\) (CS Sec. 13). El decimal es un redondeo de esa expresión, no otra constante, pero no es el valor de la fuente.
- La masa finita nombra «moneda aparte», las filas L5b, L6c, L6d, L6f y la anisotropía del término lineal en L6e. CS Sec. 11 solo dice: \(c_H=c_0\,\theta/\sin\theta\) donde es isótropo, ninguna fila nueva calculada tiene \(c_{\omega^2}\) isótropo, y la fila masiva ADMP sigue `OPEN`.
- En la tabla, los absolutos de la línea (\(1\)) y del cuadrado (\(1/\sqrt{2}\)) están en CS Sec. 5; la Sec. 11 solo afirma \(c_0=r_{\mathrm{in}}\). Los absolutos hexagonales \(r_{\mathrm{in}}=\sqrt{3}/2\), \(c_0=1/2\) (ADMP) y \(c_0=3/4\) (JDW L6d) están en el informe hexagonal (T1), no en el resumen de la Sec. 11, que da los cocientes. La celda del cubo no está escrita así en CS: la Sec. 8 tiene \(C_{\mathrm{micro}}=[-1,1]^3\), \(c_{\mathrm{IR}}/r_{\mathrm{in}}=1\), luego \(r_{\mathrm{in}}=1\) y \(V_{\mathrm{causal}}^{\max}=\sqrt{3}\) en esas unidades.
- La Sec. 5 cita el informe de líneas, línea M1. Ese informe no es fuente de esta síntesis y CS no menciona M1 (el abandono que sí registra es H1).
- «Cualquier \(s\) fijo y cualquier representación» no está en CS Sec. 7.2.

## 2. Alcance — REPAIR_REQUIRED

La cadena del punto 0.2 **no** pasa de «filas declaradas» a «en general». La sintaxis deja `in general` solo en \(c_{\mathrm{strict}}^{\mathrm{iso}}\le r_{\mathrm{in}}(C_{\mathrm{micro}})\), que es lo que dicen CS Sec. 4 y la dirección 1 de la Sec. 7.2. El eslabón \(c_0\le c_{\mathrm{strict}}^{\mathrm{iso}}\) queda probado en \(N_3\) y, fuera, solo `CONFIRMED_IN_DECLARED_ROWS`. El «so» concluye \(c_0\le r_{\mathrm{in}}\) **en cada fila declarada**, no como teorema fuera de \(N_3\). Esa compositión hereda la confirmación fila a fila; no hereda el contrato congelado. En \(W_{\mathrm{hex}}\) hay además una prueba directa, distinta, \(c_0\le r_{\mathrm{in}}\) (Bernstein, CS Sec. 12). Conviene no leer «the relativistic speed» como \(c_{\mathrm{IR}}\): CS Sec. 7.2 solo tiene \(c_{\mathrm{IR}}\le r_{\mathrm{in}}\) bajo la contención isótropa de la Sec. 3.3.

Lo que sí pierde cuantificador:

- «On one hexagonal substrate the declared walks have \(c_0=1/3,1/2,3/4\)». CS Sec. 11 declara el sustrato por grupo de traslaciones y paso compuesto, y solo identifica como el mismo sustrato ADMP y JDW L6d (\(1/2\) y \(3/4\)). L6b es \(s=6\), \(0\notin F\), y la equivalencia con L6a es a tres actualizaciones, a media escala y rotada 60° (informe L6b, Secs. 1 y 5). L6c tiene soporte de 19 puntos, no el soporte mínimo (informe hexagonal, Sec. 3).
- «Whether the ceiling is reached depends on the substrate. On the line, square, BCC and cube substrates, declared walks reach it». En el mismo \(N_3\), L3 (y L5a, L5b) cumplen \(c_0=r_{\mathrm{in}}\) y L3s4 no: \(c_0=a/\sqrt{3}<1/\sqrt{3}\) (CS Sec. 4.1). En BCC depende del walk. El resumen de la Sec. 11 («BCC/cubic and line substrates have \(c_0=r_{\mathrm{in}}\)») no anula la Sec. 4.1.
- «No walk with minimal support reaches \(r_{\mathrm{in}}\)» y «whether any walk on the hexagonal substrate reaches it is OPEN». La fuente es: ningún walk de \(s=2\) con \(F\subseteq\{0\}\cup\mathrm{vert}(H)\) alcanza el techo; el resto de \(W_{\mathrm{hex}}\) queda `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS`; no hay enunciado para \(s>2\) (CS Sec. 12; informe hexagonal, Secs. 3 y 5).

## 3. Niveles — REPAIR_REQUIRED

Las etiquetas de la Sec. 2 coinciden con la fuente y no suben de nivel: `PROVED_UNDER_FROZEN_CONTRACT` (una revisión, no una ratificación de cinco), `CONFIRMED_IN_DECLARED_ROWS`, `REJECTED IN THE DECLARED s=4 CLASS`, `PROVED_IN_REPO`, `GAP_PROVED_IN_CLASS`, `PROVED_FOR_MINIMAL_SUPPORT`, `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS`. El preámbulo deja la síntesis en preliminar. L6b se trata como promocionada, que es el registro de CS, no la línea «nothing is promoted» del propio informe de ejecución.

El fallo de nivel está en presentar como hallazgo de la Sec. 13 la comparación de velocidad de grupo, que esa sección no promociona, y en cambiar el \(a^*\) exacto por un decimal bajo un texto que dice «All values exact». El cubo mezcla el cuerpo de la Sec. 8, donde \(r_{\mathrm{in}}=1\), con el número \(1/\sqrt{3}\) de otra unidad. El cociente \(c_0/r_{\mathrm{in}}=1\) sí coincide con la Sec. 8 y con «cubic … \(c_0=r_{\mathrm{in}}\)» de la Sec. 11. El resto de la tabla es aritméticamente coherente con las unidades declaradas: \((1/2)/(\sqrt{3}/2)=1/\sqrt{3}\), \((3/4)/(\sqrt{3}/2)=\sqrt{3}/2\), \((1/3)/(\sqrt{3}/2)=2\sqrt{3}/9\), y \((a/\sqrt{3})/(1/\sqrt{3})=a\).

## 4. Lecturas y límites — REPAIR_REQUIRED

Se siguen de las filas, sin extrapolar: L6a y L6d, mismo sustrato, \(c_0\) distinto, ambos con \(s=2\); el continuo de L3s4 y el valor \(a=\sqrt{3}/2\), que da \(c_0=1/2\), frente al cociente \(1/\sqrt{3}\) de L6a, con A abierto; \(c_{0,\mathrm{raw}}^2=(3/2)l^2(1-g)\) y el máximo \(\sqrt{3}/2\) en \(g=-1/2\), solo en la subclase \(n=3\) (informe hexagonal, T1). Evaluar \(g=0\) da \(1/\sqrt{2}\) por esa fórmula. La palabra «anticommute» no está en T1: es glosa, no otro número.

No se sigue de las filas: «even the long-run propagation speed is not fixed by the substrate». El hecho de fila sí: salvo L6b, \(c_{\mathrm{strict}}^{\mathrm{iso}}=r_{\mathrm{in}}\); en L6b el cuerpo asintótico está a escala \(2/3\). L6a y L6d comparten sustrato y comparten \(c_{\mathrm{strict}}^{\mathrm{iso}}\). Ninguna fuente pone a L6b en ese mismo paso compuesto. Lo que muestra L6b es que \(r_{\mathrm{in}}\) no obliga a la igualdad, no que un mismo sustrato deje libre \(c_{\mathrm{strict}}^{\mathrm{iso}}\).

La Sec. 4 sí tapa ley QCA, universo, fotón, escala absoluta, universalidad IR (A queda `OPEN`) y el no-alcance del techo hexagonal más allá de la subclase y del soporte mínimo. No tapa dos lecturas que la Sec. 0 deja abiertas: que todo walk declarado en BCC alcance el techo, y que la pregunta abierta sea «cualquier walk» del sustrato hexagonal, incluidos \(s>2\). «No novelty» no excede: atribuye arte previo a Bernstein y a las construcciones, que es lo que dicen CS Sec. 3.1 y el informe hexagonal, Sec. 5. No cierra el `NOVELTY=OPEN` del techo hexagonal que CS deja abierto en el control de arte previo; tampoco lo refuta. «Five sources» no está en CS.

## 5. Contenido propio — PASS

Con las reparaciones sigue habiendo respuesta. El sustrato no fija \(c_0\): en \(N_3\), L3s4 recorre \((0,1/\sqrt{3})\); en el sustrato común de L6a y L6d los valores son \(1/2\) y \(3/4\). El sustrato sí fija el techo \(r_{\mathrm{in}}\), con \(c_{\mathrm{strict}}^{\mathrm{iso}}\le r_{\mathrm{in}}\) en general y \(c_0\le c_{\mathrm{strict}}^{\mathrm{iso}}\) probado solo en el contrato de \(N_3\) y confirmado en el resto de filas declaradas. La igualdad se alcanza en filas declaradas de la línea, el cuadrado, el BCC estándar y el cubo, y no en L3s4 ni en las cinco filas hexagonales declaradas. En la subclase antipodal de tres pasos el supremo es \(\sqrt{3}/2\); el soporte mínimo de \(s=2\) no llega a \(r_{\mathrm{in}}\); el resto de \(W_{\mathrm{hex}}\) está abierto. No hay escala absoluta en la clase plana congelada. L6b es la fila donde también el cuerpo a largo plazo queda estrictamente dentro de \(C_{\mathrm{micro}}\). Eso no es una lista de fuentes.

## Reparaciones obligatorias

1. **Frase:** «on one hexagonal substrate the declared walks have \(c_0=1/3,1/2,3/4\)». **Choca con** CS Sec. 11 (mismo sustrato solo ADMP y L6d) y con el informe L6b, Secs. 1 y 5 (otro \(s\), otro \(F\), equivalencia solo a tres pasos). **Cierra:** dejar \(1/2\) y \(3/4\) en L6a y L6d; dar \(1/3\) como fila L6b, no como ese sustrato.

2. **Frase:** «Whether the ceiling is reached depends on the substrate. On the line, square, BCC and cube substrates, declared walks reach it (\(c_0=r_{\mathrm{in}}\))». **Choca con** CS Sec. 4.1, mismo \(N_3\), \(c_0=a/\sqrt{3}\) para \(0<a<1\). **Cierra:** decir que hay filas declaradas que alcanzan la igualdad en línea, cuadrado, BCC estándar y cubo, y que L3s4, en ese mismo paso BCC, no la alcanza.

3. **Frase:** «no walk with minimal support reaches \(r_{\mathrm{in}}\)» y «Whether any walk on the hexagonal substrate reaches it is OPEN» (punto 0.3 y el resumen de la Sec. 2). **Choca con** CS Sec. 12 y el informe hexagonal, Secs. 3 y 5: cuantificador \(s=2\) y \(F\subseteq\{0\}\cup\mathrm{vert}(H)\); abierto el resto de \(W_{\mathrm{hex}}\); nada para \(s>2\). **Cierra:** reponer \(s=2\) y el predicado de soporte, y limitar el `OPEN` a lo que queda de \(W_{\mathrm{hex}}\). La Sec. 4 debería repetir ese límite.

4. **Frase:** «any fixed \(s\) and representation» y, en el punto 0.2, «proved for the class on \(N_3\)». **Choca con** CS Sec. 7.2, cuyo alcance escrito es conos admitidos y soporte exacto del símbolo completo en \(N_3\), incluidos nodos de Floquet degenerados, sin extensión a desplazamientos inconmensurables. **Cierra:** usar solo ese cuantificador.

5. **Frase:** «So even the long-run propagation speed is not fixed by the substrate». **Choca con** la promoción de L6b y el informe L6b, Sec. 6 (una fila de una lista; no es el paso compuesto de L6a/L6d). **Cierra:** conservar la excepción, la nilpotencia y el cociente \(2/3\); sustituir el «so» por: \(r_{\mathrm{in}}\) no fuerza \(c_{\mathrm{strict}}^{\mathrm{iso}}=r_{\mathrm{in}}\) (fila L6b).

6. **Frase:** la velocidad de grupo radial \(c_0(1+2\beta|k|+\cdots)\) y «so \(c_0\) is not the largest group speed of those walks». **Choca con** CS Sec. 13, que no contiene esa fórmula ni ese signo y deja \(V_{\mathrm{grp}}^{\max}\) abierto. **Cierra:** borrarla. No hace falta un corolario nuevo.

7. **Frase:** «\(a<a^*\approx 0{,}412\)». **Choca con** CS Sec. 13, \(a^*=\sqrt{3}\sqrt{17-\sqrt{154}}/9\). **Cierra:** restituir la expresión exacta. El intervalo \(0<a<a^*\) y el hecho de que en las demás filas \(\alpha_0<0\), y en L1 la dispersión es exactamente lineal, se quedan.

8. **Frase:** «rows where the mass is a separate coin (L5b, L6c, L6d, L6f), \(c_H=c_0\theta/\sin\theta>c_0\)…; in L6e the linear term itself becomes anisotropic». **Choca con** CS Sec. 11, que no nombra esas filas ni esa anisotropía de L6e, y con CS Sec. 5, donde en la familia estándar \(c_H<c_{\omega^2}<r_{\mathrm{in}}\). **Cierra:** dejar solo lo escrito: las dos extracciones difieren para \(0<m<1\) en la familia estándar; \(c_H=c_0\theta/\sin\theta\) donde es isótropo; ninguna fila nueva calculada tiene \(c_{\omega^2}\) isótropo; la fila masiva ADMP está `OPEN`.

9. **Frase de la tabla:** cubo \([-1,1]^3\) con \(r_{\mathrm{in}}=c_0=c_{\mathrm{strict}}^{\mathrm{iso}}=1/\sqrt{3}\) y, en el encabezado, \(V_{\mathrm{causal}}^{\max}=1\). **Choca con** CS Sec. 8: ese cubo tiene \(r_{\mathrm{in}}=1\) y radio de vértice \(\sqrt{3}\). **Cierra:** o se reescala de forma explícita y el cuerpo pasa a \([-1/\sqrt{3},1/\sqrt{3}]^3\), o se da \(r_{\mathrm{in}}=1\) en las unidades de la Sec. 8. El cociente 1 se conserva. La cita de L1 y L2 debe apuntar a la Sec. 5 para el valor absoluto; la de L6a y L6d, al informe hexagonal para \(1/2\), \(3/4\) y \(r_{\mathrm{in}}=\sqrt{3}/2\).

10. **Frase:** «The line review (… line M1) records the result that would end it». **Choca con** el corpus permitido: no está en CS ni en los dos informes. **Cierra:** suprimirla. El carácter abierto del supremo en toda la clase ya está en CS Sec. 12.

## Aclaraciones, no errores

El «so» del punto 0.2 no es una prueba fuera de \(N_3\); su fuerza es la de Hc más la desigualdad general de \(c_{\mathrm{strict}}^{\mathrm{iso}}\). «The class» del punto 0.2 hay que leerlo con el cuantificador de la reparación 4. «The whole class is OPEN» no degrada T1 ni el soporte mínimo: es el T2 general. «Anticommute» y «five sources» son vocabulario añadido; los números de T1 no cambian. «No novelty» no debe leerse como cierre del `NOVELTY=OPEN` del techo hexagonal.
