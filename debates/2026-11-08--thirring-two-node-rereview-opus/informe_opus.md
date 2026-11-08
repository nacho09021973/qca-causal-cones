<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.319 (Claude Code))
opus.json sha256 dc0988b1abbabf1bc8276f0fe908ad0c4de338d1a8da6dbfe6ec4af7f37d822e
inicio: 2026-11-08T16:39:41Z  fin: 2026-11-08T16:48:54Z
documento: /home/adnac/qca-causal-cones/theory/THIRRING_TWO_NODE_GATE.md ; último commit observado: fd1ef6c ; sha256 de la copia enviada 684290668d7e64f62e9aa1c75c55fc1e9103942ebff8729c63f01149bb8a27ac
documento: /home/adnac/qca-causal-cones/reports/2026-11-08--thirring-two-node.md ; último commit observado: cfeb548 ; sha256 de la copia enviada f773ff9633c2adc32b4678a1e36c1356d613fab590efbf23866274717c424904
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_two_node.py ; último commit observado: cfeb548 ; sha256 de la copia enviada 69fe66662358f9dec0087a7cd3c200387646272e883c26ca37860791c0c7a3a9
documento: /home/adnac/qca-causal-cones/reports/2026-11-08--thirring-two-node-verifier.txt ; último commit observado: cfeb548 ; sha256 de la copia enviada f23325f45e308f573b17b40f9a95af431a963cd2d9a8498f7b37d597e3cb3b55
documento: /home/adnac/qca-causal-cones/sources/1804.08508v1.pdf ; último commit observado: 58a345b ; sha256 de la copia enviada 495646b1a0c0a2822422c4d65536b8c4caa0d82c5efe7e48df878766af91f0d0
entrada_opus.txt sha256 9ef556a15aba2294dab6399c76611ef52f01be9fbc51019cfc7f2ade3efd25da
respuesta sha256 0422a29f59362d058c8d497b8499b034f2ba8fe20de1a0638d1291ee4e06a419
-->

# Revisión adversarial: código de dos nodos del QCA de Thirring sin masa (μ=0)

**Método.** No he ejecutado nada. Todo lo que sigue procede de tres fuentes:

- **Rederivación** a partir de U=FJ y de las definiciones del contrato.
- **Lectura** de `verify_thirring_two_node.py`.
- **Cotejo** con el texto extraído de arXiv:1804.08508v1.

Los números del registro son afirmaciones del autor. Solo los doy por confirmados cuando coinciden con una forma cerrada que he derivado: 0.46875, 1/2 y los recuentos 228, 222 y 6. El dictamen de Grok no se usa como evidencia.

---

## 0. Rederivaciones de control

**Orden, fase y signo de S_χ.** La regla de [1] es U_N = W_N V_int, con V = e^{iχ n↑n↓}. Aplica la interacción antes que el paso libre, igual que FJ. Con μ=0, W = diag(T†, T): ↑ se mueve a la izquierda y ↓ a la derecha, así que R=↓ y L=↑. La inversión de orientación está declarada.

- Un R en x y un L en y>x coinciden si y solo si y−x es par, en t=(y−x)/2. Como J actúa antes de F, el cruce completo exige T−1 ≥ max(y−x)/2.
- La fase acumulada es e^{iχ[x≡y]}. Como [x≡y] = (1+(−1)^x(−1)^y)/2 = (1+Π_RΠ_L)/2, se obtiene e^{iχ(1+Π_RΠ_L)/2} = aI + bΠ_RΠ_L.
- Coeficientes: a = e^{iχ/2}cos(χ/2) = (1+e^{iχ})/2 y b = e^{iχ/2}·i·sin(χ/2) = (e^{iχ}−1)/2. Correctos.
- Matriz 4×4 y forma e^{iχ/2}exp(iχX_RX_L/2): correctas.
- Concurrencia: 2|ab| = |sin χ|.
- En χ=π/2 se obtiene e^{iπ/4}(|00⟩+i|11⟩)/√2. En χ=π, a=0 y b=−1, es decir −XX. Correcto.

**Convención Z^T.** (TΠf)(x) = (−1)^{x−1}f(x−1), luego TΠ = −ΠT. En la base que se traslada aparece Z^T por paquete, y K = (Z⊗Z)^T S_χ. Coincide con el `expected` del test antisimétrico.

**Conservación de paridades.** Defino Γ_S(t) = (−1)^{Σ_{x∈S+t} x·n_R(x)} para la región móvil S del paquete de datos. Entonces:

  U† Γ_{S+t+1} U = Γ_{S+t} · (−1)^{N_R(S+t)},

porque F†n_R(x)F = n_R(x−1) y J es diagonal. Con μ=0, N_R(S+t) se conserva. Con un solo R en S, se cumple U^{−T}Γ U^{T} = (−1)^T Γ como **identidad de operadores en todo el Fock**. Esto vale para cualquier χ, cualquier tiempo y cualquier estado de las demás partículas, siempre que no haya otra R dentro de S.

**Fermiones idénticos (L₁, L₂).** F es un automorfismo de modos que lleva un producto ordenado de c† a otro producto ordenado, sin reordenar. J es diagonal. L₁ y L₂ tienen la misma velocidad y soportes disjuntos, así que nunca ocupan el mismo sitio. Por tanto no aparece signo de intercambio y el orden de etiqueta es legítimo. **Correcto, pero solo por álgebra** (véase O6).

**Recuentos, por lectura del código.**

| Bloque | Comprobaciones |
|---|---:|
| Dos paquetes | 80 |
| Cruce parcial | 4 |
| Antisimétrico | 36 |
| Composición | 96 |
| Ilustraciones | 6 |
| Físicas | 6 |
| **Total** | **228** |

Son 222 de categoría `finite_numerical_contrast` y 6 ilustraciones, por prefijo de nombre. Coincide con el registro.

---

## 1. Tabla R1–R4

| | Estado | Razón |
|---|---|---|
| **R1** | **RESOLVED** | §1 y §6 separan las envolventes libres (velocidad a/τ tras retirar el portador) del qubit 0/π. Declaran que este usa coherencia a momento π y que no se ha aislado como grado de baja cuasienergía. Queda un residuo en la definición de c_IR y de α (O7). Además hay un defecto físico nuevo y más fuerte que el original (O1). |
| **R2** | **RESOLVED** | El reparto 222/6 es correcto por lectura del código. La Hadamard no se ejecuta: `H@plus` es aritmética de referencia. El no-go se atribuye al álgebra (`algebra_only_conclusions`). Residuo: la etiqueta «contraste finito» incluye comprobaciones que no pueden fallar y duplicados, y la frase «pueden detectar discrepancias» es falsa para ellas (O5). |
| **R3** | **RESOLVED** | §7 y el registro dicen explícitamente «TWO fermions» y «three labeled trajectories». El argumento de orden de etiqueta es correcto (§0). Residuo: el test de dos cuerpos R+L no tiene contenido estadístico (O6). |
| **R4** | **RESOLVED** | Lo he verificado en forma cerrada (abajo). 0.46875 es exactamente el cuadrado de la norma de operador de (1−P)DP sobre el código, para M=4, T=17, χ=π/2. No es un máximo sobre parámetros: en χ=π el valor es 15/16. |

**Derivación de R4.** Tomo x = −16+i e y = 16+j, con i,j ∈ {0,…,7}.

- Hay contacto antes de T=17 si y solo si j ≤ i y j ≡ i (mod 2).
- Los bloques e·o y o·e no reciben fase.
- En el bloque e·e, 10 de los 16 pares han recibido fase. La amplitud de retorno es c = (10e^{iχ}+6)/16, y la fuga es

  1 − |c|² = **(15/32)(1 − cos χ)**.

- El bloque o·o da lo mismo, y las fugas de ambos bloques tienen soportes ortogonales.
- El máximo 15/32 se alcanza en todo el subespacio XX=+1, es decir span{|00⟩+|11⟩, |01⟩+|10⟩}. Para |00⟩ la fuga es 15/64.
- La compresión es K = (1+c)/2·I + (c−1)/2·XX, con |c|<1. Conmuta con cada X_i, lo que concuerda con `partial-crossing-still-preserves-parity`.

---

## 2. Veredictos separados

**Núcleo algebraico: correcto, con reparación menor obligatoria (O3, O4).** Son correctos:

- S_χ, con su fase, su signo y el orden FJ.
- El cierre exacto para todo M tras un cruce completo.
- La composición conmutativa.
- La conservación de Π_i.
- La obstrucción a la universalidad del código de nodos.

La obstrucción es incluso más fuerte de lo escrito: la identidad de Γ_S cubre ancillas arbitrarias independientes y tiempos intermedios. Faltan dos cosas: la hipótesis geométrica del cierre y la definición de la clase de ancillas sobre la que se cuantifica.

**Alcance físico: REPAIR_REQUIRED (O1, O2, O7, O8).** La cinemática libre es correcta y está bien acotada. Pero el informe:

- no declara que la colisión saca a los paquetes del sector infrarrojo con probabilidad O(1) independiente de M;
- presenta como «computación universal: No» lo que es solo no-densidad unitaria;
- define c_IR de forma ambigua.

**Cierre de una codificación frente a imposibilidad del modelo completo.** El informe cierra correctamente solo la codificación de nodos con los recursos declarados, y no afirma un no-go del modelo. Una observación para encuadrarlo: con μ=0, cualquier ejecución autónoma es, en coordenadas de trayectoria, *una única* unitaria diagonal en la base de ocupaciones. Este rasgo vale para todas las codificaciones y para toda interacción local diagonal, no solo e^{iχn_Rn_L}. Lo que depende del código es cómo se ve esa diagonal tras codificar. Esto no convierte el resultado en un no-go del modelo, pero indica que la obstrucción es cinemática y no específica del acoplamiento de Thirring.

---

## 3. Objeciones nuevas

**O1. La colisión no cierra el sector infrarrojo (físico; obligatoria).**
Sea |00⟩ = f_R⊗f_L, concentrado en el nodo 0 para M grande según la cota de cola de §6. Tras el cruce queda a|00⟩ + b|11⟩. Ambos paquetes saltan al nodo π (cuasienergía π/τ) con probabilidad **sin²(χ/2), independiente de M**: vale 1/2 en χ=π/2 y 1 en χ=π. Es la transferencia a «Fermion-doubled particles» que describe el resumen de [1].

Consecuencias:
- (i) No existe una descripción efectiva cerrada en las envolventes de k≈0 con colisiones.
- (ii) El entrelazamiento que se publicita reside enteramente en la coherencia con el nodo duplicado, a escala reticular.
- (iii) Un χ que se escalara a cero para tener límite continuo anularía también el entrelazamiento.

*Reparación:* añadir esto en §1 y §6. Debe quedar claro que «colisión entrelazante» y «sector relativista» son sectores distintos, no un único sector IR que haga ambas cosas. La frase «la fase de colisión finita persiste al crecer M» debe sustituirse por la probabilidad de salto entre nodos.

**O2. «Computación universal: No» sobrepasa lo demostrado (alcance; obligatoria).**
Lo que se demuestra es que el conjunto de mapas codificados normaliza cada X_i, y por tanto no es denso en U(2ⁿ). Hay tres puntos sin cerrar:

- **Bases de preparación y lectura.** El informe concede la preparación |±⟩ y una «lectura final ideal en el código» sin fijar la base. Con lectura en Z, el modelo resultante son circuitos conmutantes diagonales en X entre preparación y medida de producto, del tipo IQP. Su potencia de decisión no está acotada incondicionalmente frente a BQP. Con lectura solo en X, el modelo es trivialmente clásico.
- **Qué es un programa.** Un programa es una geometría inicial más un T. No hay secuenciación libre de puertas: las «Z_i independientes» son una sobreconcesión, cosa que el informe sí dice.

*Reparación:* (a) fijar las bases de preparación y lectura admitidas; (b) sustituir la fila de la tabla y la frase de §1 por «no genera un conjunto unitario universal en el código»; (c) declarar no acotada la potencia computacional del modelo conmutante resultante.

**O3. Clase de ancillas no definida (núcleo; obligatoria, documental).**
§7 afirma una obstrucción «para todos los protocolos y ancillas admitidos». Sin embargo, la «primera vía» de §5, con su unitaria diagonal en paridades conjuntas, solo cubre ancillas que sean ellas mismas qubits del código.

La segunda vía, enunciada como la identidad de Γ_S de §0, cubre bastante más:
- cualquier estado de Fock de L;
- cualquier estado de R fuera de S;
- tiempos parciales;
- cualquier interacción diagonal.

*Reparación:* enunciar el teorema con esa identidad y sus cuantificadores:
- para todo M ≥ 1, todo χ, todo n y todo T ≥ 0;
- para toda geometría con componentes fijas y soportes de misma componente disjuntos;
- para toda ancilla producto con el dato y sin partículas R en S(0).

Excluir o tratar aparte el caso de una R ancilla dentro de S en modos ortogonales. En ese caso se conservan por separado N_par(S) y N_impar(S), y la coherencia de paridad del dato sigue sin poder crearse.

**O4. Falta la hipótesis geométrica del cierre (núcleo; obligatoria).**
El contrato solo exige que los paquetes de la misma componente sean disjuntos. Considérese R y L con el mismo soporte de 2M sitios: los pares con y<x no se cruzan nunca. Para M=4, la fuga es (15/32)(1−cos χ) **para todo T**, permanente. Es un contraejemplo, dentro del contrato, a «código cerrado» sin calificar. El no-go no se ve afectado, porque el mapa sigue conmutando con Π_i.

*Reparación:* exigir max supp(R) < min supp(L) para cada par que interactúa. Incluir esta condición en §3, §4 y en `algebra_only_conclusions`.

**O5. Taxonomía del verificador (residuo de R2; obligatoria, documental).**
De las 222 comprobaciones:

- **49 son gramianos**, pero solo hay 9 configuraciones distintas: 40 son duplicados.
- **18 no pueden fallar por construcción:**
  - las 12 de `fermionic-antisymmetry`, porque la fase y `dest` son simétricas en ambos índices;
  - las 5 de `Fourier-node-shift`, que es una identidad exacta de la DFT con N par;
  - `two-node-quasienergy-shift`, que es la aritmética e^{−i(k+π)} = −e^{−ik}.
- Las de concurrencia y unitariedad se derivan del error de mapa y de la fuga.
- En cambio, el único diagnóstico físico no trivial, la cola FFT frente a la cota, se registra pero no se comprueba.
- La línea «H witness maximum fidelity» informa un único solapamiento, no un máximo.

*Reparación:* reclasificar en cinco grupos: propagador independiente frente a fórmula, fuga, derivadas, tautologías estructurales e ilustraciones. Retirar «pueden detectar discrepancias» para las tautologías.

**O6. El test «fermiónico» no prueba estadística (residuo de R3; obligatoria, documental).**
Con una R y una L, que son modos distintos, el sector antisimétrico es isomorfo al producto de partículas distinguibles. El test tiene valor como propagador reticular independiente: mueve espacialmente y no usa la fórmula de trayectorias. No contrasta ningún signo de intercambio. El único caso donde la estadística podría importar, L₁ y L₂, descansa solo en el argumento algebraico de §0, que es correcto.

*Reparación:* renombrar la fila «espacio antisimétrico fermiónico» y declarar que la afirmación sobre fermiones idénticos es exclusivamente algebraica.

**O7. Definición de c_IR y de α (residuo de R1; obligatoria, documental).**
«c_IR = a/τ para las dos envolventes libres identificadas» puede leerse como si incluyera las envolventes del nodo π en el marco rotante. Llamar IR a esas envolventes reintroduce la confusión que R1 quería eliminar, aunque la velocidad sea la misma porque ω=±k exactamente. Además, «α=1» no está definido en ningún documento. El contrato pedía V_grp^max, y el informe solo da V_grp^{max,1p}; lo declara, pero debe figurar como incumplimiento parcial del contrato.

*Reparación:* definir c_IR sobre las envolventes en k≈0, definir α y marcar V_grp^max de muchos cuerpos como no calculado.

**O8. Dominio de la fuente primaria y extrapolación masiva (documental; obligatoria la primera parte).**

(a) La Ec. (1) de [1] exige ν, μ > 0. μ=0 queda fuera del dominio declarado: es una extensión o un límite, y debe decirse así.

(b) [1] define el operador de N partículas solo de forma esquemática: V_int = e^{iχn↑(x)n↓(x)}, sin producto sobre x. El autómata fermiónico de segunda cuantización está en su Ref. [1] (PRA 97, 032132), que no se consultó. Las afirmaciones de tres cuerpos dependen de esa definición.

(c) *Observación, no obligatoria.* La simetría de la Ec. (7) de [1] equivale a que Γ = σ_z(−1)^x anticommuta con W **para todo μ**, mientras V conmuta con cada Γ de partícula. Por tanto N_A = Σ_{x par} n↑ + Σ_{x impar} n↓ satisface U†N_AU = N_B en el modelo masivo. Para este código, Σ_iX_i se conserva salvo inversión global incluso con μ>0. La versión por paquete se pierde porque hay reflexión. Ancillas con coherencia en N_A podrían, en principio, sortear esta restricción. El informe no extrapola al caso masivo, y hace bien; un contrato masivo futuro no debería suponer que la obstrucción desaparece sin más.

**O9. Procedencia y redondeo (documental; obligatoria).**

- La tabla de §7 redondea hacia arriba sin decirlo:

  | Magnitud | Registro | Informe |
  |---|---|---|
  | Error de mapa, dos paquetes | 1.3615e−15 | 1.37e−15 |
  | Error de mapa, antisimétrico | 6.593e−16 | 6.60e−16 |
  | Error de mapa, tres paquetes | 1.5223e−15 | 1.53e−15 |
  | Fuga máxima al cerrar los cruces | 2.2508e−30 | 2.26e−30 |

- «Versionado antes de ejecutar (`578f27c`)» y «ejecución original con `20a78c4`» son commits distintos, y no se explica qué cambió entre ellos.
- `contract_commit="fd1ef6c"` es una cadena fija en el código, no comprobada en tiempo de ejecución.

*Reparación:* indicar el criterio de redondeo o citar los valores del registro; explicar la diferencia entre los dos commits.

---

**Conclusión.** R1–R4 están resueltas en lo que pedían. El núcleo algebraico es correcto y su obstrucción es robusta. Antes de considerar estable el alcance hay que reparar:

- **O1–O4**, que son sustantivas;
- **O5–O9**, que son documentales.

Ninguna de estas reparaciones cambia el veredicto `MASSLESS_NODE_CODE_NOT_UNITARILY_UNIVERSAL`. O2 sí obliga a no leerlo como un no-go de la computación cuántica universal. Revisión de una sola ronda, sin ejecución ni experimentos nuevos.
