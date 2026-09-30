# F3 — Ansatz unitario de hopping elástico

[Atlas](../FAMILY_BIBLE.md)

## 1. Identidad

Nombre recibido: «First unitary elastic hopping ansatz, half-support orientation».
Alta documental: 2026-09-30. Apertura científica, fuente y motivación previa:
no localizadas. La relación de sucesión con F2 procede de la propuesta.

## 2. Cuantificadores congelados

Contrato no localizado. Pendientes: Hilbert, walk, especies, lattice,
semisoporte y criterio de orientación, coordenadas, grouping/supercell/ancillas,
controles, orden y observable. No asumir que son los de F1 o F2.

## 3. Qué es geometría

La propuesta relaciona deformación elástica y hopping. Falta la definición
que permita separar respuesta métrica de elecciones de orientación.

## 4. Qué no se cuenta como geometría

No identificar una elección de representante de enlace con un efecto físico
sin comprobar las equivalencias permitidas por el contrato ausente.

## 5. Regla microscópica

No localizada; no se inventa una regla unitaria que produzca el fallo descrito.

## 6. Kill tests

Test de orientación mencionado por el usuario, sin contraejemplo ni umbral
localizado. Un expediente recuperado deberá especificar qué inversión de
orientación deja invariantes los datos físicos y qué salida cambia.

## 7. Resultado

**Pendiente de trazabilidad, `[UNVERIFIED]`.** Literal recibido:
`UNITARY_ELASTIC_RESPONSE_INCONSISTENT`. No incorporado como fallo verificado.
Contrato, código, reporte, revisión y commit: pendientes.

## 8. Modo de fallo

Dependencia de orientación, según la propuesta. No se ha reproducido ni
se generaliza a otras reglas de hopping unitario.

## 9. Qué deja vivo

La pregunta de si la orientación es convención o dato físico. Próximo
movimiento documental: recuperar la regla y el test original.

## 10. Qué queda prohibido después

No etiquetar toda la clase de hopping unitario como inconsistente; no
corregir orientación a posteriori bajo el mismo contrato. No certificar F4
por llamarla sucesora de F3.

## Flujo visual

```mermaid
flowchart LR
  A["Hopping propuesto"] -.-> B["Símbolo no localizado"]
  B -.-> C["Orientación física o convencional: pendiente"]
  C -.-> D["Marco pendiente"] -.-> E["Métrica pendiente"]
  E -.-> F["Fallo de orientación alegado: UNVERIFIED"]
```
