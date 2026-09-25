# Revisión independiente: irreducibilidad D2 y aplicación de P17

Solicitud del P.I.: revisión por Gemini y DeepSeek; si ambos aceptan sin
reparaciones obligatorias, commit y push acotados a esta evidencia.
No se solicita promoción de CURRENT_STATE ni ampliación del frente.

## Integridad y autoría

Autor de la prueba y del verificador: Codex /root. Revisores solicitados:
DeepSeek (ABNER) y Gemini, familias distintas del autor. El protocolo de
Sanedrín es una deliberación compartida, no dos revisiones ciegas.
Cada revisor debe reconstruir los pasos y emitir su propio veredicto.

Objeto primario, aún sin commit: `reports/2026-09-23--irreducible-d2-pavia-checks.md`.
SHA256: `2c2024c8de8b9ac7261bd761f25e34d787481dcb24cdae8bfe649aee6f4cd684`.
Verificador: `scripts/verify_irreducible_d2_pavia.py`.
SHA256: `878542f6999351ef6e229e4abe379245312520cdf21df0594825803890f8a27e`.
El registro de ejecución adjunto acredita 519 checks exactos en el entorno
del coordinador. Vosotros no tenéis herramientas y no debéis afirmar que
habéis reejecutado Python, leído un PDF binario o verificado Git/hashes.
El resultado del checker no demuestra por sí solo la completitud de P17
ni el argumento analítico de todos los tiempos: auditadlos por separado.

Baseline Git: `835d31a37c122560f685dd612e04771699b3c7df`.
Sanedrín: `8162508e3bd0e3d05770b4dd544fe7c962d0272c`.
Herramientas compartidas: `1ce73d26a5fc116c2ab83fa6f3b55d24f9110aa4`.

## Fuente primaria admitida

D'Ariano, Erba, Perinotti, arXiv:1708.00826v2, las 16 páginas completas.
PDF versionado: `sources/1708.00826v2.pdf`, SHA256
`dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81`.
El texto adjunto es su extracción íntegra mediante el comando reproducible:

```bash
pdftotext -layout sources/1708.00826v2.pdf debates/2026-09-23--irreducible-d2-p17-source.txt
```

La extracción conserva saltos de página y puede tener defectos de notación.
Extractor: pdftotext 24.02.0. SHA256 del texto extraído:
`24dd26aa918c329c4508c789d04f10b6f7eceb98ba3d816c2a43f241bb289327`.
Si una ambigüedad afecta al argumento, identificarla; no suplirla de memoria.
Paginación del arXiv: definición y (2), p.2; (6)-(9), pp.3-4;
normalización/Schur, pp.3-4; derivación d=3 y Proposición 5(c), pp.6-7.
La prueba sometida a revisión es objeto de crítica, no fuente autorizada
para sus propias conclusiones. La geometría y el checker histórico son
definiciones y código inspeccionables, no votos previos a favor del objeto.

## Obligaciones: PASS / INCOMPLETE / FAIL por separado

1. Alcance y representación. Para el D2 espacial fijado y su clase
   proyectiva no trivial de Pauli, demostrar s=2 al exigir R irreducible;
   comprobar Schur y la fase global, sin atribuirle una velocidad.
2. Condición (2). Rehacer desde los coeficientes de U Udag y Udag U los
   pasos (D1)-(D3), incluidos signo/orden de adjuntos, enumeración de pares,
   y contradicción cuando A_h=A_j. ¿Funciona realmente en dimensión
   arbitraria con este soporte, sin rank-one o clasificación circular?
3. Aplicabilidad de P17. Contrastar todas las hipótesis con la fuente
   primaria; comprobar que no se confunden irreducibilidad dinámica,
   homogeneidad, fiel representación proyectiva, grupo espacial o embedding.
   Se admite usar la clasificación publicada como teorema previo: no se
   exige redemostrar todo el artículo ni se reclama hacerlo.
4. Formas normales. Verificar la transcripción de Proposición 5(c), momentos
   lineales, signo Fourier, c0, determinantes y trazas de vértices, y la
   deducción para todo n de C_strict=C_micro. Auditar el código y su
   diccionario epsilon=+1 -> A-, epsilon=-1 -> A+; no tomar un PASS
   computacional como sustituto de la prueba analítica.
5. Equivalencias. Comprobar conjugación, fase, permutación tetraédrica,
   reflexión y normalización izquierda permitida. Distinguir traslados del
   nodo de afirmaciones en k=0. ¿Se preservan S_n y la comparación de
   velocidades para toda la clase declarada, no solo dos ejemplos?
6. Techo. La conclusión es suficiente solo para la clase de §1. No implica
   necesidad de irreducibilidad, otros grupos/soportes/nodos, novedad,
   universalidad entre especies, estado canónico o reapertura de E/AdS.

Emitid tabla de seis obligaciones y veredicto global en la primera
intervención, y confirmad/corregid el veredicto personal al cierre:
`D2_P17_REVIEW_ACCEPTED`, `D2_P17_REPAIR_REQUIRED`, `D2_P17_FAIL` o
`D2_P17_INCOMPLETE`. Ataques concretos con condición de concesión.
Distinguid reparaciones obligatorias de mejoras opcionales. La aceptación
del otro revisor no es prueba. No modificar archivos ni ampliar el alcance.
Una ausencia/fallo/cuota no cuenta como acuerdo; no publicar como aprobado
si la revisión queda incompleta o degradada.
