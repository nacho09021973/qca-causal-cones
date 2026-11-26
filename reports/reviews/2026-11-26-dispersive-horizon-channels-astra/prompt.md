# Revisión externa: ejecución del contrato de canales C1–C5 (horizonte dispersivo)

Autorización: usuario «autorizo solo Astra» (2026-11-26). Modelo pedido por el usuario:
«quiero la version 6.2» → `gpt-6.2-astra` (OpenAI), vía `revision-ciega` del PATH
con `ASTRA_MODEL=gpt-6.2-astra`; generación comprobada antes del envío. Un primer
envío con `gpt-6-astra` (por defecto) se interrumpió sin respuesta; queda en
`intento-interrumpido-gpt-6-astra/`. Autor del contrato, del informe y de los verificadores: Claude
(Opus 5.5). Herramientas: `~/herramientas` commit `4a4fcca`. Revisado: commit
`526823f` (rama `research/dispersive-horizon-channels`). Máximo: una ronda. No se
autoriza calcular transmisión ni promoción. Cierra el encargo: un informe
completo de esta ronda.

---
Revisa adversarialmente la **ejecución del contrato de canales C1–C5** para el
paseo cuántico U = L₋W², W = S C(θ) S C(θ) S C(−2θ), con t = cos²θ,
A = t(2t−1), medio interior t = 5/16 (x → −∞) y exterior t = 7/16 (x → +∞).
La matriz de transferencia 12×12 M_x(z) y su verificador ya pasaron una
auditoría con revisiones externas; no las revises de nuevo salvo donde C1–C5
dependan de ellas. Se adjuntan:

(1) `DISPERSIVE_HORIZON_CHANNELS_GATE.md`: el contrato congelado (commit
    `7a63529`), con la regla de ventana I, los veredictos y las reglas de parada;
(2) `2026-11-26--dispersive-horizon-channels.md`: el informe de ejecución, con
    veredicto de autor CHANNELS_CLASSIFIED (PRELIMINARY);
(3) `verify_dispersive_horizon_channels.py`: el verificador (53 comprobaciones,
    SHA256 `08a38735…`, commit `a5b9be3`);
(4) `verify_dispersive_horizon_transfer_matrix.py`: el verificador de la matriz
    ya revisado, que (3) importa sin modificarlo (`M_report`, `hom_cs`, etc.);
(5) `2026-11-26--dispersive-horizon-channels-run.txt`: el registro de la
    ejecución (53/53, exit 0).

Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL /
UNVERIFIED, con las derivaciones necesarias:

1. **C1, forma de flujo.** ¿Es correcto G_x = M_x^H D M_x − E₇₇ con
   D = diag(0,1⁵,−1⁶) como flujo de probabilidad a través del corte entre x y
   x+1? ¿Decide el verificador M_x^H G_{x+1} M_x = G_x en general (ángulos
   independientes en x, x+1, x+2, |z| = 1, reducción módulo c²+s²=1)? ¿Es
   adecuada la segunda vía (flujo operativo leído de la palabra de U sobre
   soluciones exactas) y es correcto det G = −cot²θ en medio homogéneo?
2. **C2, estructura de raíces.** La simetría λ¹²P(1/λ,1/z) = z⁻²P(λ,z), la
   reducción P = zλ⁶Φ, Φ = −2h(k) en el círculo, y el argumento de enrollamiento
   Σ sign(v) = −2 a partir de det U(k) = e^{−2ik}.
3. **C3, umbrales y ventana.** La clasificación de colisiones (puntos z = ±1,
   ±i) frente a valores críticos (4f′² = 1 − f², f ≠ 0); la raíz interior
   u* = (5245 − √168025)/5250 y la ausencia de valores críticos exteriores;
   la aritmética de intervalos racionales que sitúa exactamente un valor crítico
   interior en el primer cuadrante abierto; el polinomio mínimo de Re z_c* y la
   desigualdad Re z_c* > 3/5. ¿Aplica la regla de ventana del contrato
   correctamente y es I = (arg z_c*, π/2) la componente correcta? ¿Importa la
   glosa de C_t que el informe señala?
4. **C4, clasificación en I.** Libertad de cuadrados, gcd(H, N) = 1, recuento de
   Sturm en τ = tan(k/2) (incluido el tratamiento de k = π), signo exacto de v
   en cada raíz, la tabla 4 propagantes (1 a la derecha, 3 a la izquierda) +
   4 + 4 evanescentes en cada medio, y el argumento escrito de constancia en
   todo I. ¿Es coherente con C2 (#der − #izq = −2)?
5. **C5, normalización.** Los intervalos sobre F = Y^H G Y, su signo y el
   cociente F/(v‖q₁‖²) ≈ 1; la identidad −iU^H ∂ₖU = Σ R_j^H σ_z R_j − I y el
   paso escrito (forma por etapas + Hellmann–Feynman) que da F = (∂ₖΩ)‖q₁‖²
   exactamente; el argumento de ortogonalidad de los modos evanescentes
   (Y_μ^H G Y_ν = 0 salvo μ̄ν = 1).
6. **Verificador (3).** ¿Deciden sus 53 comprobaciones lo que dicen? Atención a
   posibles falsos positivos, coma flotante en cantidades certificadas, anchura y
   corrección de los intervalos (RI/CI, isqrt), aislamiento de raíces, y que no
   se modifiquen los bytes de (4).
7. **Veredicto y alcance.** ¿Se sigue CHANNELS_CLASSIFIED de las reglas del
   contrato (exactamente un canal interior hacia la derecha; ninguna regla de
   parada)? ¿Separa el informe lo certificado de lo escrito y de lo numérico solo
   orientativo? ¿Es adecuada la sección «Not claimed»? ¿Afecta la desviación de
   proceso declarada (una ejecución de desarrollo antes del commit) a la validez?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que
derivas a mano de lo que solo inspeccionas. No calcules transmisión, matriz de
dispersión, asintóticas de Jost ni originalidad.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y
objeciones ordenadas por gravedad con sección y reparación concreta. Si no hay
fallos, dilo sin inventar objeciones.
---
