# Problema inverso de dispersión: comprobación documental acotada

Fecha: 2026-11-05. Autor: Codex. Autorización: usuario «adelante» tras
propuesta de la opción 10. PRELIMINARY; sin revisión independiente.
No es un gate ejecutado ni una demostración de identificabilidad general.

## Pregunta y criterio de corte

Sabido: las tablas promovidas de CURRENT_STATE Secs. 11 y 13, con Erratum 1
y la fila estándar L3, contienen velocidades y correcciones exactas.
Pregunta: ¿ofrecen ya una pareja de sustratos diferentes indistinguibles
por c y las primeras correcciones? Se descarta como testigo cualquier
pareja que sea el mismo sustrato bajo las equivalencias del contrato, o
que las correcciones ya distingan. No se construyen nuevos modelos para
rescatar esta candidatura durante esta comprobación.

Sustrato: grupo generado por el soporte y conjunto de pasos de una
actualización completa. Equivalencias: isometría y escala comunes a la
comparación, como en C_ACROSS_LATTICES_GATE Sec. 2. Unidades fijadas:
paso compuesto más largo 1; actualización completa 1. No se bloquea tiempo,
reagrupan celdas ni eliminan sectores para producir coincidencias.
Datos comparados: dimensión espacial, c_0 y las funciones angulares beta
y alpha, admitiendo una misma isometría para todas ellas. No solo medias.

## Contraste de las parejas inmediatas de las tablas existentes

Fuente: reports/2026-11-02--dispersion-corrections-across-lattices.md,
Sec. 2; etiquetas corregidas por el Erratum 1; fila estándar en
reports/2026-11-04--dispersion-L3-row.md, Sec. 2. Clasificación de grupos:
reports/2026-11-03--substrate-saturation-phase0.md, Sec. 7.3.

| Pareja | Lectura documental | Decisión como testigo |
| --- | --- | --- |
| L2 / L6e | Igual c, beta y alpha; mismo grupo y soporte cuadrado | Descartar: mismo sustrato |
| L6d / L6f | Igual c, beta y alpha; mismo sustrato salvo isometría y escala | Descartar: mismo sustrato |
| Estándar L3 o CJWW (5.12) / CJWW (5.15) | BCC frente a Z^3, igual c; beta no nula frente a beta cero | Descartar: distinguibles por beta |
| L6c / L6d o L6f | Grupo triangular fino frente al ordinario, igual c y beta cero; alpha=-1/512 frente a -1/128 | Descartar: distinguibles por alpha |

Estos contrastes no son una clasificación exhaustiva de todos los pares
de bloques ni de familias parametrizadas. Ninguna nueva expansión ni
verificador se ha ejecutado. No se infiere identificabilidad universal.

Comprobación primaria: sources/2408.02108v1.pdf pp.16–17, Ecs.(5.12)–(5.16),
imprime dos dispersiones diferentes: el producto de cosenos con un término
triple de senos y el producto sin él. Su igualdad al orden cónico no es
igualdad espectral. La distinción de grupos procede del soporte registrado
en la auditoría, no de la etiqueta «same lattice» del artículo.

## Antecedentes localizados, alcance de lectura

Búsqueda web 2026-11-05: «quantum walks inverse problem dispersion relation
isospectral different lattices» y «quantum walks dispersion relation
different graphs unitary equivalence coarse graining».

- Goyal, Konrad, Diósi, arXiv:1401.0196, abstract consultado: equivalencias
  unitarias de walks 1D. Localiza un riesgo; no demuestra equivalencia de
  las parejas anteriores.
- D'Ariano, Erba, Perinotti, Tosini, arXiv:1511.03992, abstract consultado:
  reducción de walks sobre grupos virtualmente abelianos a walks
  equivalentes sobre grupos abelianos con moneda mayor. Tampoco demuestra
  una equivalencia bajo nuestra incrustación y unidades fijadas.

No se han leído completos esos dos artículos: equivalencia con nuestro
problema y novedad siguen [UNVERIFIED]. Búsqueda orientativa, no exhaustiva.

## Decisión

No hay un testigo nuevo en las parejas inmediatas contrastadas. Conocer
solo c deja coincidencias ya conocidas; añadir beta y alpha separa las
parejas de sustratos distintos examinadas. Se cierra esta comprobación
documental sin abrir un cálculo ni reclamar novedad. El problema inverso
general queda OPEN. Continuar exigiría delimitar otra clase y revisar los
antecedentes completos; no es una consecuencia automática de esta nota.
