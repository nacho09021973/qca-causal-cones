# Lectura crítica del autor — revisión Grok de la etapa (a) del charter s=2

Fecha: 2026-10-29. Autor de esta lectura: Claude, autor del certificado y del informe. **No es
una revisión independiente.** La revisión independiente es la de Grok (familia xAI).

## Ejecución

- Un intento, `COMPLETED`, de 11:25:53Z a 11:46:55Z, con la autenticación del CLI de Grok.
- Antes del envío, `sha256sum -c inputs.sha256` dio OK.
- Documentos enviados: el charter (`657fa6d3…`), el informe (`f10fcfb3…`), el certificado
  (`d6bf4189…`) y `certificate_utils.py`, todos en el commit `dc4a6f7`.
- Herramienta: `revision_ciega.sh` @ `a32e189`.
- Autorización: «commit y push y que revise Gok».

## Veredicto del revisor

Matemáticamente correcto: los 30 subgrupos, las tres clases de P, F = `{D4, O}`, los recuentos
5/3/3/6/4, el lema del núcleo con dos certificados rehechos a mano, y A3/A8. Pero **no
promocionable tal cual**, por tres reparaciones:

- G-S0-01: laguna, bloquea.
- G-S0-02: laguna; bloquea la condición de exhaustividad, no el resultado.
- G-S0-03: redacción, no bloquea.

## Contraste

**G-S0-01 (identificación de `E`). Se acepta: es correcta.** El certificado vacía la clase de
`O` con núcleo el `V4` axial e imagen de orden 6, pero nunca construye `E`.
- El texto del `require` dice «e.g. E of 2O», y el informe marca A2/A7 como VERIFIED y da por
  cerrada la fila de `E`. Eso excede lo comprobado.
- La identificación es estándar. `O` permuta los tres ejes, lo que da `O → S3` con núcleo el
  `V4` axial. `E` es la representación estándar de `S3` compuesta con esa aplicación. Ninguna
  imagen de la estándar de `S3` es escalar salvo la identidad, así que el núcleo proyectivo de
  `E` es exactamente `V4` y su imagen en `SO(3)` tiene orden 6.
- Pero ese razonamiento no está en el certificado. La reparación es construir `E` en el
  certificado (permutación de ejes más carácter estándar de `S3`) y comprobar que su clase es la
  vaciada. Hay que añadir también la restricción a `D4`, con núcleo que contiene `V4`.
- Mientras tanto, A2/A7 pasan a «vaciado de la clase con núcleo `V4`, VERIFIED; identificación
  con `E`, pendiente», y la fila de `E` en CURRENT_STATE no se cierra.

**G-S0-02 (prueba de la 2-generación). Se acepta.** El informe afirma que todo subgrupo de `S4`
está generado por a lo sumo dos elementos y que «30 es el número conocido», sin prueba. Grok da la
prueba por órdenes:
- órdenes 1–4: cíclicos o `C2×C2`, y no hay `C2³` en `S4`;
- orden 6: `S3`;
- orden 8: un grupo de orden 8 que no sea `C2³`;
- orden 12: `A4`;
- orden 24: `S4`.

Se incorpora al informe.

**G-S0-03 (recuentos sin `require`). Se acepta.** Los recuentos 5/3/3/6/4 y la lista de
supervivientes se imprimen, pero no están entre las 16 comprobaciones. La observación de que los
recuentos son caracteres de un representante fijo, y no órbitas de tuplas, es correcta. En
`(V4, tetraedro)` los tres caracteres con núcleo de orden 2 forman una sola tupla bajo el
estabilizador `T`. No cambia los supervivientes.

**Otras observaciones:**
- La cita de la clasificación de subgrupos finitos de `SO(3)` sobra para estos cinco grupos: el
  desglose por órdenes y trazas cierra los recuentos sin ella. Se acepta sustituirla.
- El revisor no pudo recomprobar los símbolos de Pavia, porque `verify_irreducible_isotropy_step01.py`
  no iba en el paquete. Es una limitación del paquete, no un fallo del control.

## Conclusión del autor

- Ninguna objeción cambia el resultado: cinco supervivientes fieles y todas las demás clases
  vacías.
- G-S0-01 y G-S0-03 cambian los bytes del certificado; G-S0-02 solo cambia el informe. Cambiar
  el certificado exige una nueva revisión de ese fichero (charter, Sec. 6).
- El resultado sigue en PRELIMINARY. Aplicar las reparaciones y elegir quién revisa lo decide el
  usuario.
