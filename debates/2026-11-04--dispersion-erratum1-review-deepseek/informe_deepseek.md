<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 deda983fc03d55cc50a3824fdba18fa58dc582581fdccbb7b22f8e753cf2c0bb
inicio: 2026-11-04T11:14:52Z  fin: 2026-11-04T11:20:10Z
documento: /home/ignac/qca-causal-cones/theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_ERRATUM_1.md ; último commit observado: 648be9c ; sha256 de la copia enviada 00f83c25bcd45fce9d9a90429be4fa3d0b04f35b835a2c33a8b5baa9caae9ee3
documento: /home/ignac/qca-causal-cones/theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md ; último commit observado: a7ff5b7 ; sha256 de la copia enviada 6df09e81fae231ebbb00d19de546298559d333d33e965c95a1aa6027842231ea
documento: /home/ignac/qca-causal-cones/theory/C_ACROSS_LATTICES_GATE.md ; último commit observado: 30672ba ; sha256 de la copia enviada b58deeec91184fbf976a6cb857c8e935ec7d4a4e52d6608a62768452759e34e3
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices.md ; último commit observado: 70dd98c ; sha256 de la copia enviada 5aaaea6af9704abb2a1a16613f1ede7fc1639956800e66d2580824484b31bec9
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--dispersion-erratum1-review-deepseek/extractos.md ; último commit observado: sin versionar ; sha256 de la copia enviada 5c467c375f9d8fdae0dcce70ca81ce0ffb3fd7a90993c93c05130f4df36fd5dd
entrada_deepseek.txt sha256 43032889aca455eba9ac98e280fc176eb55b4e685a992274ff82c9f2b664ae44
respuesta sha256 e1c130e69ee43900eb628756b2c91e890f8effb0ce135a4a3ea1313481707a50
-->

## Dictamen 1 — INCOHERENCIA: PASS

La tabla de la Sec. 1 de la errata es exacta.

- El contrato padre (`C_ACROSS_LATTICES_GATE.md`, filas L3/L4) declara L3 como batería estándar BCC `N_3`, y L4 como CJWW (5.12) **y** (5.15), con etiqueta `Z^3` y `C_micro = [-1,1]^3`.
- El contrato de dispersión asigna a su fila L3 `walk2()` = CJWW (5.15), rotulada «BCC», y a su fila L4 `walk1()` = CJWW (5.12), rotulada «cube `[-1,1]^3`».
- El verificador l. 573–576 reproduce exactamente esa asignación: `DS.walk2()` para L3 y `DS.walk1()` para L4, ambos con `substrate="cubic"`.
- Las definiciones de `walk1`/`walk2` en `scripts/verify_directional_saturation.py` l. 64–65 y 72–73 confirman la correspondencia `walk1` = (5.12), `walk2` = (5.15).
- La Enmienda 1, Sec. 2, punto 4, da base suficiente: (5.12) tiene soporte `{±1}^3` y grupo generado BCC; (5.15) tiene pasos que generan `Z^3`; ambos tienen `C_micro` cúbico. La errata lo cita correctamente.

Es justo decir que el defecto está en la tabla del contrato de dispersión relativa a su contrato padre, no en el verificador como ejecución del contrato congelado. El verificador importa exactamente los símbolos que el contrato de dispersión le ordena importar.

Aclaración, no error: “no en la ejecución” debe leerse como “no en el verificador dado el contrato de dispersión congelado”; no significa que los rótulos del informe sean inmunes a la corrección.

## Dictamen 2 — LO QUE SE MANTIENE: PASS

Es correcto que la tabla del informe es una tabla de resultados para los símbolos efectivamente importados. La cadena verificador l. 573–576 → tabla del informe lo confirma.

La reasignación es correcta:

- La fila impresa «L3» (`O_h`, `alpha = -sigma2/18`, `alpha_0 = -1/90`) corresponde a `walk2()`, es decir, CJWW (5.15). Aunque su grupo generado sea `Z^3`, su dispersión puede tener simetría `O_h`; la errata no confunde grupo generado con grupo de simetría de la dispersión.
- La fila impresa «L4» (`T_d`, `beta = -(sqrt3/3) n1 n2 n3`, `alpha` como L5a) corresponde a `walk1()`, es decir, CJWW (5.12).

Los hallazgos listados como independientes de las etiquetas efectivamente lo son:

- Qué filas tienen término `beta` depende del símbolo importado, no del rótulo L3/L4.
- El contenido armónico se refiere a `G_walk` calculado para cada símbolo.
- `Hd` está refutado por L1 y por el rango de L3s4; eso no depende de las etiquetas L3/L4.
- La refutación de `Hf` por `L2 = L6e` en el sustrato cuadrado queda intacta.

No hay error aquí.

## Dictamen 3 — LO QUE CAMBIA: PASS

(a) Las líneas 560 y 562 del verificador importan `published_symbol` solo para `d = 1` y `d = 2`. No hay importación de `published_symbol(3, ·, ·)`. Por tanto, la fila L3 del padre —batería estándar `d = 3`— no tiene entrada de dispersión computada. La afirmación de que “the thirteen massless rows” sobrestima la cobertura en una fila es materialmente correcta: hay 13 filas/entradas computadas, pero cubren 12 filas distintas del padre; L4 del padre recibe dos entradas y L3 del padre queda sin entrada.

Aclaración de trazabilidad: la frase exacta «the thirteen massless rows of Sec. 11» no aparece en el extracto entregado de `CURRENT_STATE.md` l. 2424–2456. La conclusión numérica es correcta por l. 560/562 y por la tabla parental; no lo considero error.

(b) Es correcto restringir `He`. La línea promovida `L3 K4` es evidencia para CJWW (5.15), no para la batería estándar L3 del padre. El veredicto `CONFIRMED_IN_DECLARED_ROWS` vale para las filas efectivamente declaradas/calculadas, excluyendo la batería estándar L3 del padre. La errata lo formula bien.

(c) La nueva pertenencia al sustrato es correcta:

- BCC: L5a, los dos bloques de L5b y CJWW (5.12).
- `Z^3`: CJWW (5.15), y es la única fila computada en ese grupo generado.
- El par compartido es correcto. De la tabla: L5a tiene `beta = +(sqrt3/3) n1 n2 n3`; L5b tiene bloques con `±`; CJWW (5.12), impresa L4, tiene `beta = -(sqrt3/3) n1 n2 n3` y `alpha` como L5a. Por tanto, CJWW (5.12) coincide con el bloque de L5b de signo opuesto a L5a, a los órdenes tabulados.
- Las líneas 81 y 263 del informe siguen siendo ciertas: en el sustrato BCC corregido no todas las correcciones son iguales, ya que L5a y (5.12) difieren en el signo de `beta`.
- `REFUTED_BY_ROW_L6e` queda intacto.

Precisión menor no bloqueante: en el verificador l. 811 la comparación BCC usa `L5b[+i]`, no todos los bloques de L5b. La errata habla de “L5b” como fila, lo cual es sustancialmente correcto, pero citar `L5b[+i]` sería más exacto.

## Dictamen 4 — ALCANCE: PASS

La errata respeta lo que dice no hacer:

- No cambia bytes del contrato, informe ni verificador.
- No recalcula valores; lee la tabla del informe y los grupos ya derivados en la Enmienda 1.
- No decide si CJWW (5.12) o (5.15) coincide con un símbolo L3 de la batería estándar; explícitamente lo deja sin comprobar.

No se le escapa ningún enunciado promovido relevante de `CURRENT_STATE.md` Sec. 13 que dependa de las etiquetas L3/L4:

- La afirmación de `He` con `L3 K4` está expresamente corregida/reinterpretada.
- `Hf` no depende de L3/L4 para su refutación; las parejas adicionales mencionadas siguen siendo válidas.
- La frase sobre L4 con `T_d` sigue siendo cierta para la fila impresa L4, que es CJWW (5.12).
- La mención “alpha elsewhere” y las filas `D_6` no dependen de las etiquetas L3/L4.

La única salvedad es la trazabilidad ya señalada: convendría indicar la línea exacta de CS donde aparece “the thirteen massless rows of Sec. 11” si se promueve la errata, pero no es una reparación obligatoria.

## Dictamen global: PASS

No hay errores materiales que obliguen a reparar la errata. Las imprecisiones detectadas son de trazabilidad o de redacción menores:

1. La frase literal «the thirteen massless rows of Sec. 11» no es visible en el extracto entregado; si se cita, convendría añadir la línea exacta.
2. Al citar el verificador l. 811, sería más preciso decir `L5b[+i]` que “L5b” sin calificar.

**Reparaciones obligatorias: ninguna.**
