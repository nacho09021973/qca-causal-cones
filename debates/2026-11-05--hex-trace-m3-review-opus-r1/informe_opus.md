<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.318 (Claude Code))
opus.json sha256 4f10ed152e0cc00c61d8bc51d7cb72179567b37aeed2b3dd0cc0b4a70b85bba6
inicio: 2026-11-05T11:08:09Z  fin: 2026-11-05T11:10:09Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-m3.md ; último commit observado: sin versionar ; sha256 de la copia enviada 42aa2faba84ac09bc0bc25f167dbfc5e4e9ea80fff0f5cb6c16815756d329b31
documento: /home/ignac/qca-causal-cones/debates/2026-11-05--hex-trace-m3-review-opus/informe_opus.md ; último commit observado: sin versionar ; sha256 de la copia enviada 4c0167710715b0513f0afa69d78e362da8cc691769344e4396b1c8cddc2d1776
documento: /home/ignac/qca-causal-cones/debates/2026-11-05--hex-trace-m3-review-opus/verificacion_autor.md ; último commit observado: sin versionar ; sha256 de la copia enviada d7350574262ec5448c4523cf72fe7e7dd2e214aefe06ec13c664b957364c2b97
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
entrada_opus.txt sha256 9bdbeede157eecc9b45f244a29d4d831161a2f1ce3a8b796f78f85109cc8fa22
respuesta sha256 c4dee527ed8c9596bd654abb7aaa84029b5c0a6cabeada20209e276dbba45f57
-->

# Re-revisión acotada de R1: puente de traza en «m=3: exact scalar incompatibility on the aligned 37-point hexagon»

Revisor: Claude (Opus 5.5). No he ejecutado código ni comprobado hashes. He rederivado cada paso a mano a partir de los documentos adjuntos, sin aceptar ninguno por la autoridad del texto. El alcance se limita al párrafo «Explicit trace bridge (R1 repair)» de la Sec. 4. No reabro los bloques 1–5, el certificado, el código, otros radios ni otros cascos, ni la cuestión del gap uniforme.

## Dictamen

- **R1: RESUELTA.**
- **Dictamen sobre la reparación: PASS.**
- **Obligaciones obligatorias restantes para el resultado (dentro de esta cadena de revisión): ninguna.** Quedan observaciones opcionales y salvedades heredadas, detalladas abajo.

## Verificación paso a paso

### 1. Eliminación de fase — correcta

U(0)=e^{−iφ}I y Ũ=e^{iφ}U, luego Ũ(0)=I.

- Multiplicar por un escalar constante de módulo 1 no cambia el soporte de Fourier compuesto F, ni la unitariedad.
- Tampoco cambia el generador lineal: A(k)=i·dŨ/dk(0)·k es por definición el término con la fase global quitada.
- Ũ(0)=I es exactamente lo que necesitan las dos referencias: el Sec. 1 de HEX_CEILING («take U(0)=I») y su Step 1, para tener p(0)=1.

### 2. Traza escalar: cotas, valor en cero y soporte — correcto

Sea f_U=Re Tr Ũ/2.

- **Cotas.** Los autovalores de Ũ(k) son unimodulares, así que |Tr Ũ|≤2 y −1≤f_U≤1 en todo k.
- **Valor en cero.** f_U(0)=Re(2)/2=1.
- **Soporte.** Si Tr Ũ(k)=Σ_{h∈F} c_h e^{−ik·h}, su conjugado tiene soporte en −F, luego supp f_U ⊂ F∪(−F).
  - El casco exacto es el hexágono alineado, cuyos vértices en Λ original son 3R^j g1. Como Λ∩hexágono es la bola max(|i|,|j|,|i+j|)≤3, se tiene F⊂{37 puntos}.
  - Ese conjunto tiene simetría central, así que F∪(−F) también está contenido en él.
- **Realidad.** f_U es un polinomio trigonométrico real, de coeficientes hermíticos. Es el tipo de objeto que exige la Sec. 4.

### 3. Rigidez y puntero a HEX_CEILING Sec. 3 Step 1 — correcto y aplicable

El puntero existe y es exacto: `reports/2026-11-01--hex-ceiling.md`, Sec. 3, «Step 1: saturation along a facet normal is rigid».

**El Step 1 no usa soporte mínimo.** Aunque está dentro de la sección T2 de soporte mínimo, solo usa:
- la notación del Sec. 1 (rejilla h·n_f=m_hδ con m_h∈ℤ y |m_h|≤N);
- |p|≤1, por unitariedad;
- p(0)=1, por el nodo escalar;
- un autovector de A(n_f) con autovalor +c0=r_in.

La hipótesis de soporte mínimo solo entra en el Step 3. Así lo afirma el propio informe («uses only F, unitarity, the node and isotropy»). La frase del R1 «does not require minimal support» es correcta.

**Derivación rehecha.** Sea p(s)=⟨x,Ũ(s n_f/δ)x⟩ con A(n_f)x=c0x y c0=Nδ.
- Entonces p′(0)=(1/δ)⟨x,−iAx⟩=−iN.
- P(z)=z^N p es un polinomio analítico con |P|≤1 en el disco cerrado, P(1)=1 y P′(1)=0.
- Por Julia–Carathéodory, un P no constante con |P(0)|<1 tiene derivada angular P′(1)≥(1−|P(0)|)/(1+|P(0)|)>0. Si |P(0)|=1, P es constante por el máximo módulo. Luego P≡1 y p=e^{−iNs}.
- Por la igualdad en Cauchy–Schwarz, Ũ(tn_f)x=e^{−ir t}x. Análogamente para −c0, lo que da la fórmula citada.

**Proyectores de rango 1.** Como s=2, A es hermítica (Sec. 1 de HEX_CEILING), traceless y cumple A(n)²=c0²I con c0>0. Su espectro es {+c0,−c0} con multiplicidad 1 cada uno, así que Tr P_±=1. El texto dice «since s=2 and c0>0», pero el rango 1 también requiere que A sea traceless; esa hipótesis está enumerada en la frase anterior del mismo párrafo.

**Aplicabilidad a N=3.** En Λ original, con el vector de arista primitivo d=g2−g1, se obtiene h·Rot90(d)=−(√3/2)(a+b). Entonces:
- δ=√3/2 y m_h=−(a+b)∈[−3,3];
- h_C=3√3/2=3δ, luego N=3.

Esto coincide con el N=D/d=9/3 de la primera ronda. El Step 1 vale para cualquier N entero, pues solo usa Bernstein y su caso de igualdad. Si se tomara d como la arista completa 3(g2−g1), resultaría N=9 con solo frecuencias múltiplos de 3, y la conclusión sería idéntica.

**Cosenos normales.** Tr Ũ(tn_f)=e^{−irt}+e^{irt}, luego f_U(tn_f)=cos(rt). En coordenadas (p,q):
- n=(0,1): p=0 y rt=3q;
- n=(√3/2,1/2): p=q y rt=3p;
- n=(−√3/2,1/2): q=0 y rt=−3p.

Son cos 3q y cos 3p, que coinciden con f0 y con las condiciones de la reducción revisada. La paridad del coseno cubre las normales opuestas.

### 4. Promedio D6 — correcto

f_U ya satisface las condiciones normales en las tres rectas sin promediar. El promedio sirve para reducir a la forma simétrica.

El promedio D6 conserva:
- las cotas, por convexidad;
- f(0)=1;
- la realidad;
- el soporte en los 37 puntos;
- los cosenos en las rectas normales, porque D6 las permuta y cos es par.

Por la reducción ya revisada (PASS), el resultado tiene la forma f0+Δ(α+βS1) con α,β reales. Las Secs. 2–4 lo excluyen. El razonamiento es exactamente el contrapositivo que se necesita.

### 5. Techo y conclusión estricta — correcto

- **El techo se aplica.** La prueba de L0 (HEX_CEILING Sec. 1) usa solo:
  - nodo escalar;
  - rejilla entera en la normal de faceta;
  - F⊂casco;
  - unitariedad;
  - A hermítica, traceless e isótropa con s=2.

  Todo esto se cumple en la clase declarada, así que c0≤r_in.
- **La saturación está excluida.** El puente da c0≠r_in.
- **Conclusión.** Por tanto c0<r_in. Es una no-alcanzabilidad puntual, sin cota cuantitativa, como dice el texto.

### 6. Hipótesis conservadas — correcto

El párrafo y la frase anterior mantienen todas las hipótesis:
- s=2;
- nodo escalar;
- generador traceless e isótropo;
- soporte dentro de los 37 puntos;
- casco exacto igual al hexágono alineado de radio 1;
- su normalización r=√3/2.

El casco exacto se usa en tres sitios: para fijar r=√3/2, para las rectas normales concretas y para el techo. No hay extrapolación a otros cascos, radios u orientaciones.

## Observaciones no bloqueantes (opcionales)

1. Añadir «traceless» a la frase «Since s=2 and c0>0, the projectors have rank one».
2. Precisar que N=3 corresponde a tomar d=g2−g1, primitivo en Λ original. Con d=3(g2−g1) sale N=9 y la conclusión no cambia.
3. La Sec. 1 del informe m=3 no escribe explícitamente las tres rectas (cos 3q en p=0; cos 3p en q=0 y en p=q), aunque el R1 remite a ellas como «the normal cosines of Sec. 1». Podrían escribirse en una línea.
4. Actualizar la línea de estado de la cabecera («bounded re-review pending») para registrar este resultado, sin promoción.

## Salvedades heredadas (no reabiertas, no obligatorias aquí)

- El informe HEX_CEILING, que contiene el Step 1 y L0, está marcado como PRELIMINARY y no promocionado.
- En ese informe, la cita de Julia y del caso de igualdad de Bernstein figura con página [UNVERIFIED]. He rederivado la rigidez arriba, así que el puente no descansa en esa autoridad. La promoción del resultado m=3 dependerá del estado de esas dependencias según la política del proyecto.
- El certificado, el verificador y las limitaciones operativas (a)–(d) de la primera ronda no han cambiado y no se han reevaluado.

## Cierre

- R1 queda resuelta. La reparación pasa y no queda ninguna obligación obligatoria derivada de esta cadena de dos rondas.
- No hay problemas matemáticos abiertos en el puente.
- Los puntos abiertos son solo los opcionales y heredados listados arriba, y el alcance declarado: sin ley escalar universal, sin otros radios u orientaciones y sin gap uniforme.
- Este dictamen no promociona el resultado ni modifica CURRENT_STATE.
