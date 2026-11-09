<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.318 (Claude Code))
opus.json sha256 6382c644c75be1d393eb0f91d76cad626a846074021da21168796455a4ea2ef7
inicio: 2026-11-05T10:57:52Z  fin: 2026-11-05T11:03:02Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-m3.md ; último commit observado: sin versionar ; sha256 de la copia enviada b00a472770db7ebf67aff6a4b4619904a1e29d531b2b79e7fe4d47de1d5e711f
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_trace_m3.py ; último commit observado: sin versionar ; sha256 de la copia enviada 88a20b3d99b2164b91557d48b69fb113e3e3e5adf7662c088347a0146669998f
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-m3-verifier.txt ; último commit observado: sin versionar ; sha256 de la copia enviada bc884e888d0ce58d264f8f96ebd883988b852ce71a9c5b2f722b79edfe57a228
documento: /home/ignac/qca-causal-cones/theory/HEX_TRACE_M3_GATE.md ; último commit observado: sin versionar ; sha256 de la copia enviada e436cdb879e7b9e1ede963b4d170269d3d340c69f9c5b0a89bcbc6417de04b68
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-scalar-method.md ; último commit observado: c7c2dcb (con cambios sin commit) ; sha256 de la copia enviada 321b53d0dbc234724188b350a1ea050fc79747c5f7e038cdb17cd834b689423b
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
documento: /home/ignac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
entrada_opus.txt sha256 4a5ba08bd3204259f10d3998f6ac72bd5d3af091f0d406feb7d1a45cb1741e3d
respuesta sha256 f42c92604b1e83b1c071b89610c557d98e159898042c2a5d81f843e576061944
-->

# Revisión adversarial: «m=3: exact scalar incompatibility on the aligned 37-point hexagon»

Revisor: Claude (Opus 5.5). No ejecuté el verificador ni ningún código, y no comprobé los SHA256. Toda la aritmética siguiente está rederivada a mano a partir de las definiciones, sin tomar la salida del programa como dato. No heredo el PASS previo: rederivé la reducción (R) para m=3.

## Dictamen global

**REPAIR_REQUIRED, con una sola reparación obligatoria de carácter documental (R1, bloque 6).**

- El certificado matemático es **correcto**: excluye todo par real (α,β), no solo los puntos muestreados.
- El resultado escalar SCALAR_INFEASIBLE_M3 queda establecido.
- La consecuencia sobre los walks es matemáticamente válida (derivación abajo). Sin embargo, su paso de traza y eliminación de fase no está escrito en el informe ni en ningún insumo adjunto.
- No encontré errores de programa que afecten al certificado.

| Bloque | Dictamen |
|---|---|
| 1. Normalización, simetrías, reducción | PASS |
| 2. Fórmulas sobre p=2q | PASS |
| 3. Cuatro desigualdades | PASS |
| 4. Certificado | PASS |
| 5. Verificador | PASS (con mejoras opcionales) |
| 6. Puente a walks | REPAIR_REQUIRED (R1, documental) |

---

## 1. Soporte, simetrías y reducción — PASS

**Retícula y soporte.** Con h=(i g1+j g2)/3 se tiene k·h = ip+jq. Los vectores unitarios ±g1, ±g2, ±(g2−g1) son (±1,0), (0,±1), ±(−1,1), es decir, la bola max(|i|,|j|,|i+j|)≤1. Por tanto el hexágono de vértices R^j g1 (normalizado por 3) es {max(|i|,|j|,|i+j|)≤3}. Contiene 3m²+3m+1 = 37 puntos, su apotema es √3/2 y su circunradio 1.

**Cosenos normales.** Las normales de faceta están a 30°, 90° y 150°.
- n=(0,1): p=0 y q=t·(√3/2)/3, luego r·t=3q.
- n=(√3/2,1/2): p=q.
- n=(−√3/2,1/2): q=0.

Esto coincide con cos(3q) en p=0 y con cos(3p) en q=0 y en p=q.

**Promedio D6.** Las 12 isometrías del hexágono alineado preservan Λ/3, el conjunto de 37 frecuencias y el conjunto de las tres rectas normales. Sea f̄ = (1/12)Σ f∘g. Entonces:
- la cota |f̄|≤1 se conserva por convexidad;
- f̄(0)=1;
- f̄ es real;
- el soporte sigue dentro del conjunto de 37 frecuencias;
- en cada recta normal, f(g·tn) = cos(±rt) = cos(rt).

Por tanto, cualquier candidato real, simétrico o no, produce un candidato D6-invariante, y excluir estos últimos basta. ✔

**Reducción (R) para m=3, rederivada.**
- f0 es D6-invariante. Bajo (p,q)→(−p,q−p) y (p,q)→(q,q−p), los tres cosenos se permutan.
- f0 cumple las condiciones: f0(0)=1, cos(3q) en p=0 y cos(3p) en q=0 y en p=q.
- d=f̄−f0 se anula en z=1, |w|=1, luego d(1,w)≡0 y (z−1) divide a d.
- La reflexión que fija p=0 es σ: g1→−g1, g2→g2−g1, es decir (p,q)→(−p,q−p). Al derivar la invariancia en p=0, donde ∂_q d=0, se obtiene 2∂_p d=0. Por tanto e(1,w)=0 y (z−1)² divide a d.
- Las conjugadas dan (w−1)² y (z−w)². Son irreducibles no asociados en el anillo de Laurent, que es un DFU.
- La identidad sin²(θ/2) = −(e^{iθ}−1)²/(4e^{iθ}) da Δ = −(z−1)²(w−1)²(z−w)²/(64z²w²). ✔
- Newt(Δ) es la suma de Minkowski de los segmentos ±e1, ±e2, ±(e1−e2), que es H_2. Las funciones soporte en las seis direcciones de faceta son 3 para H_3 y 2 para H_2, luego Newt(h)⊂H_1.
- H_1 consta del origen y de una sola órbita de 6 puntos. La invariancia por rotación de 180° junto con la realidad hacen reales los coeficientes. Por tanto h=α+βS1 con α,β∈ℝ. ✔

## 2. Fórmulas sobre p=2q — PASS

- cos3p = T6(x), y cos3q = cos3(p−q) = T3(x). Por tanto f0=[T6+2T3−1]/2.
- Con T6=2T3²−1, esto da una forma más cómoda: **f0 = T3²+T3−1**.
- sin²(p/2)=1−x² y sin²(q/2)=sin²((p−q)/2)=(1−x)/2. Por tanto Δ=(1−x²)(1−x)²/4, que es >0 en (−1,1).
- S1 = 2(2x²−1+2x) = 4x²+4x−2.

**Realizabilidad.** q=arccos x, p=2q, y (p,q)↦k es una biyección lineal de ℝ². Los cuatro x están en (−1,1), luego Δ>0.

Valores rederivados:

| x | T3 | f0 | Δ | S1 |
|---|---|---|---|---|
| 5/16 | −835/1024 | −1206391/1048576 | 27951/262144 | −23/64 |
| −1/2 | 1 | 1 | 27/64 | −3 |
| 3/8 | −117/128 | −17671/16384 | 1375/16384 | 1/16 |
| 13/16 | −299/1024 | −1265351/1048576 | 783/262144 | 249/64 |

Todos coinciden con el stdout.

Un control de plausibilidad confirma el mecanismo: f0 baja hasta −5/4 en T3=−1/2 (x≈0,766), donde Δ es pequeño. Eso fuerza h grande cerca del borde del vértice.

## 3. Desigualdades — PASS

Como Δ>0:
- f≤1 ⟺ h≤(1−f0)/Δ;
- f≥−1 ⟺ −h≤(1+f0)/Δ.

Ambos sentidos son correctos.

Las constantes son:
- (1−f0)/Δ en 5/16: 2254967/111804, y como 2254967=11·204997, queda **204997/10164**.
- 2·64/27 = **128/27**.
- 34055/1375 = **6811/275**.
- −216775/3132, y como 216775=29·7475, queda **−7475/108**.

Las cuatro fracciones están reducidas.

## 4. Certificado — PASS

**Cancelación de α y β.**
- Primer par: coeficientes B −23/64 y +3, cuya suma es 169/64. Con peso 64/169 se obtiene +β, y la α se cancela (1−1).
- Segundo par: 1/16−249/64 = −245/64. Con peso 64/245 se obtiene −β.

**Lado derecho.**
- (64/169)·2278637/91476 = 36458192/3864861.
- (64/245)·(−1320037/29700) = −21120592/1819125.
- El mínimo común denominador es 3³·5³·7²·11²·13² = 3381753375.
- 31900918000 − 39263180528 = **−7362262528**, que es ≈ −2,177 < 0. ✔

**Lectura equivalente.** De las cuatro restricciones se obtienen dos cotas opuestas sobre β:
- de las filas 1 y 2: β ≤ 9,434;
- de las filas 3 y 4: β ≥ 11,610.

**Alcance.** Es una combinación lineal no negativa de desigualdades lineales en (α,β) que da 0 ≤ c < 0. Por tanto excluye **todo** (α,β)∈ℝ² que cumpla esas cuatro restricciones necesarias. A fortiori excluye cualquier candidato globalmente acotado. No depende del muestreo ni del programa.

## 5. Verificador — PASS

Leído, no ejecutado.

- **`point_values`.** zw = z·w̄ = e^{i(p−q)}; δ=∏(1−cos)/8; las fórmulas son correctas.
- **Recuento de filas.** El toro da 64 pares. Se descartan los que tienen t=0 o u=0 (z=1 o w=1), lo que deja 49, y luego la diagonal z=w, lo que deja 42 puntos y 84 filas. La rebanada da 33 valores menos x=±1, es decir 31 puntos y 62 filas. **Total: 146**, que coincide con el informe.
- **`eliminate`.** Es Fourier–Motzkin exacto, y completo para dos variables.
  - Las filas superiores α+Bβ≤C se emparejan con las inferiores −α+Bβ≤C.
  - Si B<0, el sentido se invierte correctamente: β≥C/B.
  - Los pesos 1/B_hi y −1/B_lo son positivos. Reproducen exactamente 64/169 y 64/245.
- **`recheck_point`.** Es una segunda evaluación por sustitución en caracteres de Laurent. Vale como cruce de fórmulas, y el informe ya admite que no es revisión independiente.
  - Sobre z=w², verifica las fórmulas de Chebyshev de la rebanada en los cuatro puntos.
  - No recomprueba C=(1∓f0)/δ, aunque esa fórmula se lee directamente en `restrictions()`.
  - Un fallo de `simplify` daría un falso negativo, que cierra con fallo, no un falso positivo.
- **Comprobación final.** Recalcula A, B y C a partir de las filas. Exige pesos ≥0, A=B=0 y C<0, lo cual basta: si todos los pesos fueran 0, C sería 0.
- **Salida.** Devuelve 0 solo con 5/5 comprobaciones en la rama de certificado.

**Distinción entre certificado y procedimiento.** El procedimiento (rejilla y eliminación) descubre el certificado. Pero el certificado de cuatro filas es comprobable a mano, como hice arriba, y su validez no depende del programa.

**Limitaciones operativas que no afectan a la validez:**
- **(a)** La comprobación 1 solo cuenta puntos (37 y 7). Su etiqueta dice «origin plus six-point orbit», pero no verifica la estructura de órbitas D6 ni ningún paso de la reducción. La reducción es analítica (§1).
- **(b)** El tope de 300 s es de reloj y no determinista. En una máquina lenta podría fallar con un certificado válido.
- **(c)** `F(base_poly.eval(...))` depende de que SymPy registre su `Rational` como `numbers.Rational`. Si no lo hiciera, el programa abortaría (falla cerrado). No podría producir un certificado falso.
- **(d)** El verificador redescubre el certificado en lugar de comprobar uno fijado. Un cambio futuro de rejilla podría cambiar las filas sin que el informe lo refleje.

## 6. Puente a los walks — REPAIR_REQUIRED (R1)

### Derivación que verifico

Sea U del tipo declarado, con casco exacto igual al hexágono alineado de radio 1 y c0=r_in.

1. **Eliminación de fase.** U(0)=e^{−iφ}I. Se define Ũ=e^{iφ}U, que tiene el mismo soporte F⊂Λ/3∩H, es decir, dentro de los 37 puntos.
2. **Rigidez** (Doc 6, Sec. 3, Paso 1). El paso usa solo el entramado entero de L0, no el soporte mínimo.
   - Para m=3, N=D/d=9/3=3.
   - Con s=2 y A sin traza e isótropa, A(n_f) es hermítica con espectro {±c0}, c0=r_in=Nδ, y proyectores P_± de rango 1.
   - Por la igualdad de Bernstein / Julia, Ũ(tn_f)=e^{−ir t}P_+ + e^{ir t}P_−.
   - Comprobé que P'(1) = N + (−N) = 0 con P=z^N p.
3. **Traza escalar.** Se define f := Re tr Ũ /2. Entonces:
   - f es real y |f| ≤ |tr Ũ|/2 ≤ 1, porque los autovalores son unimodulares;
   - f(0)=1;
   - el soporte está en F∪(−F)⊂H, porque H tiene simetría central;
   - en cada normal, tr P_±=1 da f(tn_f)=cos(r t), que en coordenadas son las rectas de §1.
4. **Cierre.** Los §§1–4 excluyen tal f. Por tanto no hay saturación.

Las hipótesis s=2, nodo escalar y término lineal traceless e isótropo son todas necesarias: dan los proyectores de rango 1 y la normalización /2.

**Casco exacto.** Es esencial y está bien declarado. Dentro de los 37 puntos caben walks con casco S7, S13 (v=g1+g2), S19 (v=2g1) o el hexágono no alineado v=2g1+g2 (|v|=√7, (2,1) cumple max=3). Esos walks tienen otra normalización y otro r_in, y no quedan cubiertos.

**Ausencia de afirmaciones excesivas.** El informe no afirma gap uniforme, otros radios u orientaciones, ni una ley universal. ✔

### R1 (obligatoria, documental)

**Brecha.** El informe invoca «the existing s=2 trace/averaging/rigidity bridge». Los insumos adjuntos contienen la rigidez (Doc 6) y el promedio (Docs 1 y 5). Ninguno define el escalar f=Re(e^{iφ}tr U)/2 ni demuestra los cuatro hechos del paso 3. El Doc 5 solo dice «the trace argument excludes saturation». La conclusión a nivel de walks descansa así sobre un paso no escrito en el material de este resultado.

**Reparación.** Hay dos opciones:
- añadir al §4 la derivación de los pasos 1–3 (unas cinco líneas, válidas tal como están arriba); o
- dar un puntero exacto, con fichero y sección, a donde ese paso está escrito y revisado.

No afecta a los bloques 1–5 ni a la etiqueta SCALAR_INFEASIBLE_M3.

---

## Mejoras opcionales (no bloquean)

1. Añadir una función que compruebe el certificado de cuatro filas fijado en el código, separada del descubrimiento (ver §5 d). La validez es independiente del programa, como se muestra arriba.
2. Corregir la etiqueta de la comprobación 1 para que diga «solo recuentos», o comprobar de verdad la descomposición en órbitas.
3. Enumerar explícitamente los cascos contenidos en los 37 puntos que **no** quedan cubiertos (S7, S13, S19, v=2g1+g2).
4. Indicar que el argumento usa solo unitariedad, F, nodo e isotropía. Por tanto vale también en W_hex^sym con este casco (convención del Doc 7). Es opcional: este gate no lo exige.
5. **Observación, no verificada como afirmación del informe.** Con soporte fijo de 37 puntos y la normalización de este hexágono, el conjunto de símbolos unitarios con nodo y A traceless e isótropa es compacto, y c0 es continuo. El argumento escalar excluye c0=√3/2 en todo ese conjunto, porque Bernstein con N=3 no usa el casco exacto. Eso implicaría un gap uniforme **no cuantitativo**: existiría ε>0 con c0≤√3/2−ε. La frase «not a uniform gap estimate» sigue siendo exacta, porque no se da ninguna estimación. Si se quisiera afirmar el gap, haría falta una revisión aparte. No recomiendo añadirlo a este resultado.

## Cierre

- No hay objeciones matemáticas.
- La única obligación pendiente es R1 (documental). Requiere una re-revisión acotada a ese punto.
- Ni este dictamen ni una futura reparación promocionan el resultado.
