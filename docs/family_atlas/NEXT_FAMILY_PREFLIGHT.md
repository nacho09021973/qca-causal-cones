# Selección y preflight de la siguiente familia

Fecha: 2026-09-30. Base sincronizada: `3976026`, más atlas en `f21af94`.
Instrucción: «commit y push y luego a elegir familias y a seguir».
Este expediente separa la selección del atlas que registra resultados.

## Objetivo y criterios fijados antes de la nueva lectura

Mantener una partícula CJWW (5.15) exactamente en g=0, sobre ℤ³ con celda
C², cuatro especies +I y coordenadas comunes. Para una nueva regla de
geometría, exigir motivación publicada independiente y una definición
unitaria y causal precisa antes de calcular universalidad. No escoger una
modificación de F4 por el hecho de que su respuesta fue nula.

Seleccionar primero una **arquitectura para lectura de preflight**, no una
regla física por inventar. El resultado de esta etapa es elegibilidad o un
cuello de botella escrito; no presupone que exista una familia ejecutable.

## Lista corta al seleccionar

| Familia | Evidencia disponible | Decisión para esta ronda |
|---|---|---|
| F1 | W12 revisado, cierre contractual | Mantener cerrado |
| F2 | Contrato y certificado cinemático recuperados | Conservar como referencia; no suministra hopping dinámico |
| F3 | Testigo exacto de orientación recuperado | Mantener terminal inconsistente |
| F4 | Certificado recuperado: hopping métrico nulo | No cambiar prescripción para rescatarla |
| F5 | Lectura dirigida recuperada, sin certificado permanente de factorización | Verificar el negativo con el contrato acotado recién escrito |
| F6 | Arnault–Debbasch, PDF disponible | Comparador bibliográfico; comprobar dimensiones y regla antes de proponer extensión |
| F7 | QCGD seleccionada ya el 2026-09-29; original arXiv 1607.06700v2 localizado | **Elegida para la siguiente lectura de arquitectura** |
| F8 | Gu–Wen: sector de restricciones, no regla CJWW dada | Mantener como referencia para una etapa posterior |

## Por qué F7

La motivación de grafo cuántico y propagación sobre él ya consta en el
[contrato original](../../theory/DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE.md)
del 2026-09-29, anterior a W12 y F4. El original es
[Arrighi–Martiel, arXiv:1607.06700v2](https://arxiv.org/abs/1607.06700v2).
Su resumen confirma que estudia causalidad y localización sobre grafos
cuánticos variables. Falta comprobar las hipótesis completas y el puente;
no se infiere una regla CJWW del resumen.

## Preguntas de preflight y cierre

Leer las definiciones y el teorema, citando páginas del PDF:

1. ¿Qué grafos y qué Hilbert admite? ¿Se conserva el conjunto de vértices?
2. ¿La causalidad y la descomposición se miden en el grafo dinámico o en un
   grafo fijo externo? ¿Qué etiquetas, puertos y extensión auxiliar usan?
3. ¿El teorema cubre el grafo infinito ℤ³ del objetivo, o hace falta un puente
   finito/infinito? No sustituir ℤ³ por un toro sin declararlo y justificarlo.
4. ¿Da una regla concreta que recupere CJWW y una respuesta métrica, o solo
   representa causal unitaries ya definidas? ¿Qué límite tiene el no-go previo
   del fondo geométrico puro con canal reducido exacto?

Tiempo: una ronda de lectura acotada. Terminales:
`ARCHITECTURE_ELIGIBLE_RULE_SPECIFIED`, `ARCHITECTURE_ELIGIBLE_RULE_OPEN`,
`BRIDGE_QUANTIFIERS_OPEN` o `ARCHITECTURE_INCOMPATIBLE`.
Si falta la regla o una extensión requerida, registrar la carencia y detener
la síntesis: no inventar un edge flip ni empezar un test métrico sobre una
familia sin definición. El límite g=0 se mantiene; pedir backreaction a g≠0
no se sustituye por el canal exacto fuerte excluido en el no-go anterior.

No se convocan revisores externos en esta ronda. Una lectura o certificado
local no cuentan como revisión independiente. W3–W11 no se reabren.

## Ejecución de la lectura F7

PDF local: `biblioteca/arXiv-1607.06700v2.pdf`, sha256
`a8feaab0e3bf46680de45ae92b5c07aa514d27417b64c7ff8b6b4eeed8614dde`.

La lectura primaria acotada localizó:

- p.2, Def. 1: grafos finitos etiquetados, con vertices tomados de un
  universo contable, grado acotado, puertos finitos y etiquetas parciales.
- p.3, Defs. 6-7: espacio de Hilbert con base de grafos finitos etiquetados
  y propiedad de conservar vertices.
- pp.5-6: extension marcada y teorema de representacion localizada para una
  unitaria causal que conserva vertices.

Resultado:

```text
BRIDGE_QUANTIFIERS_OPEN / EXPLICIT_CJWW_RULE_NOT_SPECIFIED
PRIMARY_SOURCE_PREFLIGHT
```

La arquitectura QCGD sigue viva como candidata de grafo dinamico. La lectura
no proporciona todavia una regla CJWW exacta en `g=0` sobre Z3 infinito ni una
ley de backreaction. El siguiente movimiento admisible seria un contrato
nuevo que declare sector finito/infinito, regla unitaria concreta y el puente
exacto al tick CJWW plano antes de cualquier test de especies.
