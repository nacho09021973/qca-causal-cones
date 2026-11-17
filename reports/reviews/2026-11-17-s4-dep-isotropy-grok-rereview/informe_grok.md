<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 6f2e19a855dcfbabcda754dbbc5b6566ddb1ffca47855e10193d7c21eaa06029
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-17T10:21:39Z  fin: 2026-11-17T10:27:10Z
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-17-s4-dep-isotropy-astra/informe_astra.md ; último commit observado: ed63258 ; sha256 de la copia enviada 4113523d1874c4dd200ce3d8db99bb4ff354c6c0976d37a77f916cc644f466f2
documento: /home/ignac/qca-causal-cones/reports/2026-11-17--s4-dep-isotropy.md ; último commit observado: 6331fa5 ; sha256 de la copia enviada 15f5666f2b30d636abba16219e14a71a95ec4afe5d27015cf7b6dcf12d3ecb3a
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-17-s4-dep-isotropy-grok-rereview/verifier_fdae12c_to_36fb8fd.diff ; último commit observado: 5c4e723 ; sha256 de la copia enviada d228d293bdd4ed3a68ef747a8e29ab425af99dc4f664e5d09a37eda06edf2535
documento: /home/ignac/qca-causal-cones/scripts/verify_s4_dep_isotropy.py ; último commit observado: 36fb8fd ; sha256 de la copia enviada 03f8ffb7d9396d029d35fb693d21d09c38651644acc42510672d0de0d08523df
documento: /home/ignac/qca-causal-cones/scripts/README.md ; último commit observado: 929f7f7 ; sha256 de la copia enviada 7b14aad9f66a86752fca117eb19bde790928122715364bd9d84437ea83f764a9
entrada_grok.txt sha256 d1d4010dd977dcec90ae6b38a679a747f60d559ef0bbe57dbdebf4fa00d5c6af
respuesta sha256 b1c77c1fe012126af052c72ba147fd83d833414b0ce5e9d4fc05d03444be4c10
-->

**Dictamen global: PASS.** El diff cierra el bloque 5; R1 y R3 quedan bien registrados y no añaden ninguna afirmación matemática nueva que el material no sostenga.

### A. Bloque 5 — PASS

El cambio entre las dos versiones es un cambio de método del cálculo de ceros, más la guarda que hace válida esa sustitución. No cambia las tareas C1–C5, ni sus criterios, ni la lógica de veredicto.

El diff solo toca esto:

- Documenta la parada de la ejecución 1 y el método nuevo.
- Introduce el símbolo `t` y el factor intermedio `M_h`, con `A_h = W M_h`. El producto que define `A_h` es el mismo.
- Sustituye `sp.solve` por la parametrización racional del arco, el mcd de las partes real e imaginaria de los numeradores y `real_roots`.
- Evalúa los ceros de C1 en `M_h` y los de C4 en `[U_l, M_h]`.
- Añade tres comprobaciones de cordura, `U_l W = W U_l`, que cierran en fallo si no se cumplen.

C2, C3, C5 y el árbol de veredicto (`NOT_DEP_ISOTROPIC_IN_DECLARED_L`, `DEP_ISOTROPIC_IN_DECLARED_L`, `DEP_ISOTROPIC_EXCEPT_FINITE_SET`, `NONE_OF_THE_DECLARED`) no aparecen en el diff. La equivalencia usada es la correcta: `W` unitaria ya se comprobaba, así que `A_h = 0` si y solo si `M_h = 0`; con la conmutación nueva, `[U_l, A_h] = W[U_l, M_h]`, y la matriz se anula en los mismos `(a, b)`. Esas comprobaciones no alteran qué resultado exige cada tarea; solo pueden impedir emitir veredicto.

`zeros_in_domain` ya no devuelve `"UNDECIDED"`. La rama que imprime «C4 pairs undecided» sigue en el código y queda inalcanzable: es consecuencia del método, no una regla de veredicto reescrita. El comentario de esa función dice que la lista de valores de `a` va ordenada y el código no la ordena; C4 vuelve a ordenar el conjunto excepcional antes de usarlo, así que el veredicto no depende de ese orden.

### B. R1 — PASS

Sí es aceptable dejar los bytes del verificador como están y registrar la fe de erratas en el informe y en `scripts/README.md`. La línea falsa está en la cabecera de un fichero ya revisado; la corrección que pedía la revisión anterior es de redacción, no una prueba que faltara. La errata viaja junto a la orden de ejecución.

La redacción es correcta. La cabecera enumera «P projectors» y el código no comprueba ningún proyector: solo que cada `Gamma_i` es hermítica y que `Gamma_i² = I`. De ahí se deduce `P_i^± = (I ± Gamma_i)/2`: son hermíticos y cumplen `P² = P`. El informe y el README dicen exactamente eso, sin afirmar que el script imprima esa comprobación. La frase del README de que la rama `"UNDECIDED"` es inalcanzable coincide con el código de la ejecución 2.

### C. R3 — PASS

El párrafo del veredicto hace las tres cosas.

- Separa la isotropía certificada de la pendiente: «C1–C5 certify the declared isotropy only», y la pendiente «derived separately […] not recomputed here», con procedencia en `theory/S4_STRICT_CONE_COUNTEREXAMPLE.md`, `scripts/cert_Aa_s4_counterexample.py` y la sección 4.1 de `CURRENT_STATE.md`.
- Nombra el término de comparación: `c_strict^iso = 1/sqrt3` del cuerpo de soporte estricto, y dice que la comparación no es con un frente balístico definido por amplitudes.
- Restringe la homogeneidad a la condición (2) tal como está en arXiv:1708.00826v2, y excluye cualquier otra formulación, incluida la de su referencia [23].

Los valores `c_0 = a/sqrt3` en las cuasienergías `±pi/4`, dimensión interna cuatro, son los de la formulación que la revisión anterior ya dio por comprobada.

### D. Errores nuevos — PASS

No. Lo que añaden las reparaciones se sostiene con el verificador actual y el diff, o es la separación pedida en el bloque 6.

La deducción sobre los proyectores es la identidad anterior. La nota de que `"UNDECIDED"` no añade comprobación y de que `simplify` interviene en las identidades exactas, sin tolerancias, coincide con `red` y con `zeros_in_domain`. El informe no adopta como prueba los testigos de traza ni la derivación de la pendiente escritos por el otro modelo. El panel de seis puntos y el estado `COUNTEREXAMPLE_VERIFIED` de la sección 4.1 se citan como procedencia externa y este certificado dice que no los recalcula; no amplían lo que certifican C1–C5.

**Dictamen global: PASS.**
