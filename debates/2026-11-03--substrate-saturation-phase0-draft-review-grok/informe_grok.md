<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 0b50b52c7d28670f78e63e6802dfdfa4bf12f0551a9bc74fd31db2d7a7c0c720
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-03T16:52:07Z  fin: 2026-11-03T17:00:08Z
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: sin versionar ; sha256 de la copia enviada d6a8e9891c1baeeb3312145fdcc9bb91198443d2ed9eb9965de12b874f20c886
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--c-across-substrates-answer.md ; último commit observado: 98e9a69 ; sha256 de la copia enviada 4d35f826420fc84096af1ead8bf98366d3c6763c76c7de93b7d9faacbe2329df
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--c-across-lattices.md ; último commit observado: 8d0276e ; sha256 de la copia enviada 01a18c70a1b031e99ca4f944c9f6810f29b1327067138c8eb3ee089deca1ea3f
documento: /home/ignac/qca-causal-cones/theory/C_ACROSS_LATTICES_GATE.md ; último commit observado: 30672ba ; sha256 de la copia enviada b58deeec91184fbf976a6cb857c8e935ec7d4a4e52d6608a62768452759e34e3
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
entrada_grok.txt sha256 1c943dcabb99e49a447b74df9e32250f8d765f3d21924dc2df83cea2e526736b
respuesta sha256 3c33362daae5b5c668d24e9d676bcbf0b0b7a6913151a1a8ad0548e74bf63732
-->

**Dictamen global: REPAIR_REQUIRED.** La separación entre «existe un walk que satura» y «ninguno satura», la neutralidad de lo que cae fuera de las definiciones, y el tope `NOT_REFUTED` están bien armados. La conjetura, en cambio, no está bien definida: «paralelotopo» es más ancho que lo que las filas realmente separan, y la fase 0, sobre la tabla de la que salió la conjetura, no puede fallar. No hay en los documentos adjuntos un contraejemplo exacto a la letra de (PS).

## 1. Conjetura — REPAIR_REQUIRED

La bicondicional está parseada: (PS⇐) es existencial y (PS⇒) es universal, y el hexágono (6 vértices) no es un paralelotopo (en `d = 2`, 4 vértices). Entre las formas ya tabuladas, eso corta mejor que «zonotopo»: segmento, cuadrado, cubo y hexágono son zonotopos, y el hexágono no satura en los walks declarados. Tampoco es «simetría suficiente para un cono isótropo». L6a, L6c, L6d y L6f tienen cono isótropo sin inclinación y `c_0 < r_in`; el hexágono tiene más simetría que el cuadrado y no alcanza el techo.

El fallo es la frase de la Sec. 1, leída con la Sec. 2.3: el techo «se alcanza […] si y solo si su `C_micro` es un paralelotopo», y paralelotopo es «la suma de Minkowski de `d` segmentos linealmente independientes (un paralelogramo en `d = 2`)». Eso incluye un rombo de 60° y un paralelepípedo que no es cubo. `c_0` solo existe si hay nodo isótropo sin inclinación (`{T_a, T_b} = 2 c_0^2 δ_ab`). El grupo de simetría de un rombo de 60° deja dos ejes invariantes: no fuerza una única forma cuadrática. (PS⇐) afirma entonces un `c_0` que puede no estar definido. La cláusula `OUTSIDE_DEFINITIONS` de la Sec. 3.4 aparca una fila ya declarada; no arregla el enunciado general que la fase 1 heredaría («PS⇐ para paralelotopos generales»).

Las filas que sí saturan son hipercubos, salvo isometría: segmento, cuadrado (L2 y L6e) y cubo (BCC: la envolvente de `{±1}^3`; L4: `[-1,1]^3`). No hay en los adjuntos ningún paralelotopo que no sea hipercubo, así que nada distingue las dos nociones y nada contradice la letra de (PS). L3s4 no la contradice: es `s = 4` y, además, en ese sustrato L3 y L5a sí saturan.

## 2. Cuantificadores y dominio — REPAIR_REQUIRED

El existencial y el universal están bien separados, y un walk que no satura no refuta (PS⇐) si otro del mismo sustrato satura. «Sustrato» queda definido por la cita al contrato de retículos: grupo de traslaciones generado por el paso compuesto, más ese paso. L6a y L6d son el mismo sustrato; L6c es otro, porque el grupo es más fino, aunque la forma de `C_micro` coincida. Eso es correcto.

Hay dos errores de dominio. Primero, la Sec. 2.2: «L6b with `s = 6`» queda fuera. El contrato de retículos y el informe de ejecución ponen L6b en `s = 2` (en el informe, además, `OPEN`, no codificado). La síntesis, posterior, dice `s = 6` y da `c_0 = 1/3`. La fase 0 no puede excluir la fila por `s ≠ 2` mientras esas fuentes no digan lo mismo. Segundo, la Sec. 1 restringe (PS) a «the declared classes», y la Sec. 6 reutiliza el mismo nombre para «PS⇐ for general parallelotopes». Son dos enunciados. Un `NOT_REFUTED` sobre la lista finita no es la supervivencia del enunciado general.

## 3. Normalización — REPAIR_REQUIRED

`C_micro = conv(N)`, `r_in = min h_C`, cono isótropo sin inclinación y paso más largo 1 ponen en la misma escala a las filas cuyo par `(c_0, r_in)` se copie de una sola fuente ya normalizada. La igualdad `c_0 = r_in` no cambia si se reescalan los dos a la vez.

El agujero es L4. En CS Sec. 8, `C_micro = [-1,1]^3`, `r_in = 1` y `c_IR = 1`. El informe de retículos (Sec. 4) y la síntesis reescalan a paso más largo 1: `r_in = c_0 = 1/√3`. La Sec. 2.3 dice que un valor «taken in other units, is not a comparison», pero no dice que L4 tiene los dos sistemas promocionados. El método pide anotar los valores exactos: cruzar `c_0` de una fuente con `r_in` de la otra fabrica `c_0 ≠ r_in`.

El cero en `N` no rompe la comparación. En L6a, L6c y L6f está en el interior: no cambia la envolvente, los vértices, `r_in` ni el paso más largo. Aclaración, no error.

## 4. Criterio de fracaso — REPAIR_REQUIRED

Es correcto que un solo contraejemplo exacto tire el enunciado, que el máximo sea `NOT_REFUTED_IN_EXISTING_ROWS` (nunca `CONFIRMED`) y que `OUTSIDE_DEFINITIONS` no cuente a favor ni en contra. También es correcta la carta de la Sec. 2.4: (PS⇒) es puntual (`c_0(W) < r_in` para cada walk) y no da un hueco uniforme `sup c_0/r_in < 1`. T1, `√3/2`, es uniforme solo en la subclase antipodal `n = 3`; M1-B13 y M1-B19 son huecos cualitativos, sin cota bajo `r_in`.

Falla la Sec. 3.2: anotar «whether the row or its class has `c_0 = r_in`». «Su clase» mezcla el walk, una subclase con hueco demostrado y la clase hexagonal entera, que sigue `OPEN`. Un hueco en S13 o S19 no es «el sustrato cumple (PS⇒)».

## 5. Utilidad y sesgo — REPAIR_REQUIRED

Con esta lista la fase 0 no puede fallar de verdad. El patrón (satura en línea, cuadrado, BCC y cubo; en el hexágono los walks declarados no) es el mismo del que se leyó (PS). Ha ya fue `REFUTED_BY_ROW_L6a`. El único resultado científico posible es el que la síntesis ya tiene: no hay contraejemplo. `NOT_REFUTED` no añade evidencia.

El sesgo de lectura es real, y la Sec. 6 lo institucionaliza: la fase 2 solo sigue si la fase 0 termina en `NOT_REFUTED_IN_EXISTING_ROWS`. El token de «no había contraejemplo en la tabla de ajuste» queda como luz verde. El aviso «Never `CONFIRMED`» no lo desactiva.

Además, «four parallelotope substrates» cuenta sustratos, no formas. Las formas de `C_micro` son tres hipercubos y un hexágono. BCC y L4 son el mismo cubo en distinto grupo; L2 y L6e son el mismo cuadrado. No hay cuatro geometrías independientes, ni una sola que sea paralelotopo sin ser hipercubo.

## Reparaciones obligatorias

1. **Sec. 1 y Sec. 2.3.** La frase «iff its `C_micro` is a parallelotope», con paralelotopo = suma de `d` segmentos, mete en (PS⇐) cuerpos sin nodo isótropo (rombo de 60°) y llama «paralelotopo» a lo que en las filas es solo un hipercubo. Cierre: en esta carta, el predicado es «`C_micro` es un hipercubo salvo isometría». Un paralelotopo que no lo sea no está a ningún lado de la bicondicional. No es objetivo de una fase 1 llamada igual. Si no hay nodo isótropo, el objeto está fuera del enunciado, no en el lado «se alcanza».

2. **Sec. 2.2, «L6b with `s = 6`».** Los adjuntos no fijan `s`. Cierre: citar los dos textos; si siguen en desacuerdo, L6b queda sin clasificar (`OPEN_AFTER_ROW_SURVEY`), no fuera por `s ≠ 2`.

3. **Sec. 1, «within the declared classes», frente a Sec. 6, «PS⇐ for general parallelotopes».** Mismo nombre, dos cuantificadores. Cierre: esta carta solo contiene el enunciado sobre filas promocionadas. El enunciado general no se escribe aquí.

4. **Sec. 2.3 y el método de la Sec. 3, aplicados a L4.** Hay dos pares promocionados, `(1, 1)` y `(1/√3, 1/√3)`. Cierre: por fila, una sola cita del par en unidades de paso más largo 1, y la prohibición explícita de cruzar CS Sec. 8 con la tabla reescalada.

5. **Sec. 3.2, «the row or its class».** Convierte un hueco de subclase en hecho de sustrato. Cierre: tres campos separados —este walk, el enunciado promocionado con su propio cuantificador y alcance, y el existencial por sustrato— sin pasar de uno a otro.

6. **Sec. 5, `NOT_REFUTED_IN_EXISTING_ROWS`, y Sec. 6, la fase 2 solo después de ese veredicto.** Sobre el conjunto de ajuste ese veredicto no puede no salir, y aun así abre la fase siguiente. Cierre: si no hay contraejemplo, el resultado se llama como auditoría de la tabla que sugirió la frase, no como supervivencia; se dice en la misma frase que no es evidencia y que no autoriza la fase 2. El informe debe decir que las filas no distinguen hipercubo de paralelotopo. Un fallo de verdad exige, en otra carta, una forma que no esté en esta tabla. Esta fase, documental, no la calcula.

## Aclaraciones, no errores

- El ejemplo «L3s4 on BCC» (Sec. 2.1) es `s = 4`, fuera del dominio. La lógica es cierta: no refuta el existencial. Conviene etiquetarlo `s = 4`. Dentro de `s = 2`, en los paralelotopos de la tabla no hay ningún walk promocionado que no sature.
- `N` del borrador es `F` del contrato de retículos. Conviene escribir `N := F` una vez. «Composite one-step» debe leerse como un update completo: en L5a el paso compuesto son los 8 vértices; los shifts parciales darían otro cuerpo.
- `0 ∈ N` no altera la comparación.
- Un `c_0 > r_in` no sería un contraejemplo a (PS): chocaría con la cota de fondo `c_0 ≤ r_in`. No hay tal fila.
- Nada de lo adjunto contradice la letra actual de (PS). Eso no es apoyo.
