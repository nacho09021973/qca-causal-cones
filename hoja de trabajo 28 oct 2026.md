# Hoja de trabajo — 28 de octubre de 2026

Rama: `research/inverse-gravity-design`. Sustituye a la [hoja del 22 de octubre](hoja%20de%20trabajo%2022%20oct%202026.md).
La fuente de verdad sigue siendo `state/CURRENT_STATE.md`, con una guía de lectura vigente al principio
(«Current reading guide — 2026-10-28»). Esta hoja ordena los próximos pasos, pero no autoriza nada por sí misma.

## Qué se hizo desde el 22 de octubre

Los cinco puntos de la hoja anterior:

1. **Reconstrucción documental:** terminada el 26-10 (`1ccf78d`). `text_integrity.py --check` da cero problemas.
2. **Certificados que derivan:** W3, W5 y W6 reforzados el 26-10 (`800cafd`). Estado:
   `IMPLEMENTED_AUTHOR_CHECKED / NEW_INDEPENDENT_REVIEW_PENDING`.
3. **Documentar verificadores en `scripts/README.md`:** sin hacer (ver punto 4 abajo).
4. **Revisiones pendientes:**
   - W4 (espectro de longitud de onda larga): auditado y revisado por DeepSeek, ACCEPT_WITH_REPAIRS. Las
     cinco objeciones se trataron en `reports/2026-10-27--w4-review-objections.md`, pero no se han vuelto a
     revisar.
   - Coste de discriminación: Grok revisó la versión reparada y dio PASS (28-10, `c88be82`, `06a0335`).
5. **Comité sobre la línea de gravedad inversa:** no convocado.

Además:

- **4B:** los commits `16c4f0f`/`13d398a` quedaron reconciliados el 22-10 (`94071db`). El 28-10 se corrigió
  una frase que todavía los daba por pendientes.
- **A.int, velocidades renormalizadas por interacción:** pregunta importada el 26-10 desde `~/simulacion-red`
  y revisión preliminar de fuentes primarias el 27-10 (`01fd957`).
- **Eon v4 (27-10, sin commit en el working tree):**
  - auditoría de viabilidad: `REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP`;
  - primer candidato a vacío (producto de ocupaciones): `GAUSS_PASS / OCCUPATION_REFERENCE_STATIONARITY_FAIL /
    STOP_THIS_CANDIDATE`;
  - auditoría de una respuesta recibida;
  - segundo candidato (gaussiano proyectado): `EXPLICIT_NORMALIZABLE_GAUSS_STATE_CONSTRUCTED /
    GAUSSIAN_TAIL_STATIONARITY_FAIL`.

  La revisión con Gemini no llegó a completarse (fallo de DNS). El 28-10 se envió el mismo encargo a DeepSeek:
  `debates/2026-10-28--eon-gaussian-review-deepseek/`.

## Próximos pasos, por orden

### 1. Cerrar la revisión de Eon con DeepSeek — hecho el 28-10

Hecho:
- **`5dbd843`:** commit del bloque de Eon con los bytes revisados.
- **`f64d0c7`:** DeepSeek da ACCEPT_WITH_REPAIRS. G-R1-01 y G-R1-06 se rechazan como errores, porque el
  revisor intercambió f y g. G-R1-04 tiene contenido.
- **Commit siguiente:** adenda de reparación del informe, que nadie ha vuelto a revisar.

Queda abierto que el argumento del autor para G-R1-04 (base `|E>'` y coeficiente `a` con signos) no lo ha visto
ningún revisor. Si interesa, se puede certificar el signo real de las plaquetas con el orden JW de Eon. Eso
exigiría un contrato nuevo o una ampliación del existente, con un verificador aparte. El plan original era:

1. Leer el informe sin editarlo.
2. Contrastar cada objeción contra el PDF primario y los certificados.
3. Escribir `verificacion_autor.md`.
4. Hacer commit, solo de ficheros con nombre, del trabajo de Eon que sigue en el working tree:
   - `theory/A_INT_EON_*.md`;
   - los informes, certificados y barridos del 27-10;
   - los tres `verify_eon_*.py`;
   - la carpeta de Gemini;
   - el fragmento de Eon de `CURRENT_STATE.md`.

   Antes, pasar `run_all_verifiers.py` y `text_integrity.py --check`.

### 2. Decisión de rumbo de A.int (la toma el usuario)

Hay dos candidatos a vacío descartados. Antes de un tercero, conviene decidir si se sigue buscando un estado de
referencia estacionario o si la ruta se detiene con su registro de obstrucciones. Encaja para `/comite`.

### 3. Revisiones independientes pendientes

Por orden de uso:

- certificados reforzados de W3/W5/W6;
- comprobación de primer candidato de Eon (`STOP_THIS_CANDIDATE`);
- reparaciones de W4;
- W1, W2, W7 y los puentes CJWW (texto ya reconstruido);
- F2/F4 de la familia elástica.

Ninguna promueve evidencia por sí sola.

### 4. Deuda documental de verificadores — hecho el 28-10, salvo Eon

- Los 24 verificadores con commit que faltaban ya tienen entrada en `scripts/README.md` («Previously
  undocumented verifiers»). Faltan los tres `verify_eon_*.py`, que se documentan al hacer su commit (punto 1).
- `.claude/settings.json` permite ya los 43 verificadores con commit en sus dos formas exactas. Los de Eon se
  añaden con su commit.
- Barrido completo el 28-10 en `233a553`: 46/46 pasan.

### 5. Comité sobre la línea de gravedad inversa

Sigue pendiente desde el 22-10. Pregunta única: ¿hay un objetivo alcanzable o se cierra como registro de
obstrucciones? IG-S2 terminó en `BOUNDED_TRANSFER_ATTEMPT_STOPPED_OPEN`, con la transferencia directa en pausa.

### 6. Mantenimiento

- Push de la rama: hay commits locales por delante de `origin`.
- `CLAUDE.md`: corregidas el 28-10 las notas sobre `biblioteca/`, el generador del índice y el censo de
  `sanedrin`.

## Comprobaciones antes de cada sesión

```sh
python3 -B scripts/run_all_verifiers.py --output reports/<fecha>--verifier-sweep.tsv
python3 -B scripts/text_integrity.py --check        # 0 problemas el 28-10
sanedrin --listar
```
