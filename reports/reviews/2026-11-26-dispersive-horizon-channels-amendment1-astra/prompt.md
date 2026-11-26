# Revisión externa: Enmienda 1 del informe de canales C1–C5 (horizonte dispersivo)

Autorización: usuario «permiso concedido» (2026-11-26), a la propuesta de
revisar la Enmienda 1 con Astra 6.2 en una ronda. Modelo `gpt-6.2-astra`
(OpenAI) vía `revision-ciega` del PATH con `ASTRA_MODEL=gpt-6.2-astra`;
generación comprobada antes del envío. Autor de la enmienda, del informe y de
los verificadores: Claude (Opus 5.5). Herramientas: `~/herramientas` commit
`4a4fcca`. Revisado: commit `6d45537` (rama
`research/dispersive-horizon-channels`). Máximo: una ronda. No se autoriza
calcular transmisión ni promoción. Cierra el encargo: un informe completo de
esta ronda.

---
Revisa adversarialmente la **Enmienda 1** del informe de ejecución del contrato
de canales C1–C5 para el paseo cuántico U = L₋W², W = S C(θ) S C(θ) S C(−2θ),
t = cos²θ, medios t = 5/16 (interior, x → −∞) y t = 7/16 (exterior, x → +∞).
La Enmienda 1 responde a una revisión anterior (texto de un modelo, adjunto: no
es fuente) que dio REPAIR_REQUIRED por entregables del contrato que faltaban.
Se adjuntan:

(1) `amendment1.diff`: el diff exacto del informe introducido por la Enmienda 1;
(2) el informe completo con la Enmienda 1 (marcas [A1]);
(3) el informe de revisión al que responde;
(4) `verify_dispersive_horizon_channels_amendment1.py`: el verificador nuevo
    (63 comprobaciones, commit `ea3067a`, anterior a su única ejecución);
(5) `verify_dispersive_horizon_channels.py`: el verificador de canales ya
    revisado, que (4) importa sin modificarlo (y que importa el de la matriz,
    no adjunto);
(6) el registro de la ejecución de (4): 63/63 tras 61/61 y 53/53, exit 0.

El contrato congelado no se adjunta de nuevo; sus exigencias C2–C5 están citadas
en (3). Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL /
UNVERIFIED, con las derivaciones necesarias:

1. **Objeción mayor 1 (C2, recuento entre umbrales).** ¿Certifican las
   comprobaciones K el recuento en los ocho arcos de ambos medios? ¿Son
   correctos la elección de puntos racionales y su localización en cada arco
   (p₁ = (2499+100i)/2501 frente a arg z_c*; imágenes por conjugación y
   negación, con la simetría del conjunto crítico de Z)? ¿Es correcto el
   argumento escrito de constancia dentro de cada arco y a través de los puntos
   de colisión? ¿Queda bien acotada la sección «Not claimed»?
2. **Objeción mayor 2 (entregables C3–C5).**
   - C3: ¿son válidos los recintos impresos de los cuatro z_c?
   - C4 (E): ¿es correcto el método de aislamiento (norma
     N = P(·, z₀)P(·, z̄₀) ∈ ℚ[λ], gcd = 1, cajas de N asignadas a un factor
     por evaluación intervalar de Horner con exclusión del cero, decisión de
     |λ| ≶ 1 por abs2, emparejamiento por 1/λ̄, correspondencia con las raíces
     de Sturm)? ¿Hay falsos positivos posibles?
   - C5 (N): ¿registra lo que pide el contrato (vector normalizado por modo)?
     ¿Es correcta la comprobación N^H G N ∋ sign(v)?
3. **Objeción media 3 (verificador y procedencia).** Las aserciones de valores
   publicados (V) y de hashes (H, leídos antes de ejecutar la importación).
   ¿Siguen siendo débiles algunas condiciones de aceptación?
4. **det G_x = −cot²β₆(x) con perfil variable.** ¿Atribuye la enmienda
   correctamente la prueba escrita (de la revisión anterior) y la comprobación
   puntual G?
5. **Coherencia del texto.** ¿Son coherentes con el registro las tablas de la
   enmienda (raíces, valores de k orientativos, F y 1/√|F|)? ¿Separa lo
   certificado de lo escrito y de lo orientativo?
6. **Veredicto.** Con la Enmienda 1, ¿se cumplen las condiciones del contrato
   para `CHANNELS_CLASSIFIED` (C1–C5 completos; I no vacío; exactamente un canal
   interior hacia la derecha en I; al menos uno exterior), o queda alguna
   obligación abierta que obligue a `OPEN_AFTER_CHANNEL_ANALYSIS`?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que
derivas a mano de lo que solo inspeccionas. No revises de nuevo lo ya aprobado
en la revisión anterior salvo que la enmienda lo afecte. No calcules
transmisión, matriz de dispersión, asintóticas de Jost ni originalidad.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y
objeciones ordenadas por gravedad con sección y reparación concreta. Si no hay
fallos, dilo sin inventar objeciones.
---
