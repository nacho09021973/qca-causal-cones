# Atlas de familias geométricas para QCA/QW

Primera edición documental: 2026-09-30. Base inspeccionada:
`research/gravitational-normalization-gate` @ `16850476a6320c55aaf6d25471d00454cdc15b41`.
Sincronización posterior: se recuperaron los expedientes remotos F2-F5 hasta
`3976026`, el atlas inicial se publicó en `f21af94`, y esta versión añade el
certificado restringido F5 y la selección/preflight F7.

El atlas registra clases, contratos, obstrucciones y puentes. No decide gates:
manda [CURRENT_STATE](../../state/CURRENT_STATE.md). No es una clasificación
exhaustiva, una afirmación de novedad ni una autorización para abrir modelos.
Los IDs F son del atlas; no sustituyen los IDs W del proyecto.

## Registro maestro

| ID / ficha | Clase y objeto geométrico | Resultado trazable en esta edición | Evidencia / decisión |
|---|---|---|---|
| [F1 — W6 Pauli-selective](families/F1_w6_pauli_selective.md) | Grafo fijo; nueve controles de transporte; métrica del símbolo principal | `UNIVERSAL_SUBFAMILY_DEFICIENT`: rango 3/6 sobre métricas constantes | Revisión W12 registrada; `CLOSED_BY_CONTRACT` para W6/CJWW |
| [F2 — Embedding común](families/F2_common_embedding.md) | Embedding afín común; métrica cinemática constante | `KINEMATIC_COMMON_EMBEDDING_UNIVERSAL / ELASTIC_HOPPING_RESPONSE_OPEN` | Certificado simbólico recuperado; preliminar, revisión independiente pendiente |
| [F3 — Hopping unitario elástico](families/F3_unitary_elastic.md) | Hopping con orientación de semisoporte | `UNITARY_ELASTIC_RESPONSE_INCONSISTENT` | Contraejemplo exacto de orientación; test de especies no ejecutado |
| [F4 — Hopping hermítico elástico](families/F4_hermitian_elastic.md) | Respuesta hermítica de hopping más embedding común | `HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY` | Certificado recuperado; hopping no aporta marco métrico nuevo a primer orden |
| [F5 — Puente paired-QW](families/F5_arrighi_facchini_bridge.md) | Antecedente publicado de QWs curvos mediante substeps direccionales | `SINGLE_COORDINATE_FACTORIZATION_EXCLUDED` para el puente restringido | Certificado autor-side nuevo; no-go solo para un factor por coordenada en celda C2 |
| [F6 — Arnault-Debbasch](families/F6_arnault_debbasch.md) | DTQW curvo publicado en (1+2)D | `PUBLISHED_2D_CURVED_DTQW / DIRECT_3D_CJWW_BRIDGE_NOT_PROVIDED` | Comparador bibliográfico; sin test algebraico |
| [F7 — QCGD](families/F7_qcgd.md) | Grafos cuánticos dinámicos; causalidad intrínseca | `NO_RULE_SPECIFIED` tras preflight `BRIDGE_QUANTIFIERS_OPEN` | Contrato de especificación congelado; no hay test métrico ejecutable |
| [F8 — Gu-Wen constraints](families/F8_gu_wen_constraints.md) | Sector tensorial con constraints escalares/vectoriales y helicidad +/-2 | `VACUUM_CONSTRAINT_ARCHITECTURE_PRIOR_ART / DIRECT_CJWW_SOURCE_BRIDGE_OPEN` | Fuente primaria y W10 reparado; no hay puente CJWW local |
| [F9 — Pretko tensor gauge](families/F9_pretko_tensor_gauge.md) | Teorías gauge tensoriales rank-2; Gauss laws, fractones y polarizaciones | `RANK2_GAUSS_LAW_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT` | Fuente primaria; diccionario estructural, no familia CJWW ejecutable |
| [F10 — Gauge-invariant CA](families/F10_gauge_invariant_ca.md) | Autómatas celulares con extensión gauge local; variables de enlace y sourcing matter/gauge | `GAUGE_EXTENSION_CA_ARCHITECTURE_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT` | Fuente primaria arXiv; arquitectura gauge discreta, no geometría CJWW |

## Mapa de navegación

Las aristas clasifican entradas; no representan implicaciones ni equivalencias.
El color expresa el estado documental de esta edición, no viabilidad física.
Rojo: cierre contractual o fallo terminal; gris: no ejecutado; azul:
antecedente bibliográfico; amarillo: cuestión abierta; verde: test acotado
superado, sin promoción a programa completo.

```mermaid
flowchart TB
  A["Atlas QCA/QW"] --> G["Grafo fijo / controles"]
  A --> P["Walks curvos publicados"]
  A --> D["Grafos dinámicos"]
  A --> C["Sectores con restricciones"]
  A --> L["Arquitecturas gauge / links"]
  G --> F1["F1 · W6/CJWW · cierre contractual"]
  G --> F2["F2 · embedding común · cinemática PASS"]
  G --> F3["F3 · hopping unitario · inconsistente"]
  G --> F4["F4 · hopping hermítico · embedding only"]
  P --> F5["F5 · paired-QW · puente restringido excluido"]
  P --> F6["F6 · Arnault-Debbasch · comparador 2D"]
  D --> F7["F7 · QCGD · NO_RULE_SPECIFIED"]
  C --> F8["F8 · Gu-Wen · constraint prior art"]
  C --> F9["F9 · Pretko · rank-2 gauge prior art"]
  L --> F10["F10 · gauge-invariant CA · link variables"]
  classDef closed fill:#fee2e2,stroke:#991b1b,color:#111827;
  classDef pending fill:#e5e7eb,stroke:#4b5563,color:#111827;
  classDef bibliography fill:#dbeafe,stroke:#1e40af,color:#111827;
  classDef open fill:#fef3c7,stroke:#92400e,color:#111827;
  classDef pass fill:#dcfce7,stroke:#166534,color:#111827;
  class F1,F3,F5 closed;
  class F2 pass;
  class F4,F7 open;
  class F6,F8,F9,F10 bibliography;
```

La secuencia W1–W11 puede incorporarse mediante nuevas fichas o antecedentes
de F1; este núcleo no la inventaría por completo.

## Reglas de incorporación

Objetivo operativo para la versión 1: unas 16 familias. El rango razonable
del atlas es 15-20 familias; por encima de 25-30 sólo se justifica si las
entradas aportan obstrucciones o puentes realmente distintos.

1. Registrar también las familias descartadas. Un resultado breve merece
   entrada si su clase y evidencia pueden identificarse.
2. Usar la [plantilla](FAMILY_TEMPLATE.md). Conservar por separado resultado
   matemático, nivel de evidencia, revisión y decisión canónica.
3. Congelar clase, soporte, especies, coordenadas, equivalencias y test antes
   de calcular. Si faltan, escribir «no localizado»; el atlas no los reconstruye.
4. Vincular contrato, código permanente, informe, revisión y commits. Para
   bibliografía, citar PDF y página leída. Texto generado no sustituye evidencia.
5. Un cambio de cuantificadores o de regla requiere expediente propio y relación
   explícita con su antecedente. No borrar el fallo ni rescatarlo a posteriori.
6. Mantener el mismo flujo visual por ficha: control → símbolo → términos
   no métricos → marco → métrica → test. Usar pasos pendientes cuando falte evidencia.
7. Los diagramas Mermaid son fuente editable permanente dentro de las fichas.
   Si se exportan figuras, conservar el generador y su correspondencia con la ficha.

Una entrada nueva debe cambiar al menos una de estas cosas: qué cuenta como
geometría, qué regla microscópica se permite, qué kill test aplica, qué modo
de fallo queda registrado o qué puente bibliográfico aporta. Si sólo cambia
un coeficiente, una orientación menor o una variante interna sin nuevo test,
debe ir como subcaso dentro de la ficha existente.

## Distinciones de lectura

El atlas separa embedding, métrica efectiva, soporte causal, transporte,
gauge y restricciones. Una rotación de marco que deja una métrica invariante
no acredita por sí sola una simetría gauge microscópica. Tampoco un coin,
un desplazamiento nodal, una fase escalar o una conexión de espín cuentan
automáticamente como deformación métrica: cada familia debe declarar el test
que los separa. No se impone una taxonomía universal antes de definir el modelo.
