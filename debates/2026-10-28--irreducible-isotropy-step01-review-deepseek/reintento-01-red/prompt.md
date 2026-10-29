# Revisión ciega — pasos 0–1 de la gate de isotropía irreducible (DeepSeek)

Fecha: 2026-10-28. Autorización directa del usuario: «mándalo a revisión ciega con DeepSeek».
Objetivo: revisión independiente que exige la carta (Sec. 6) antes de que el resultado
`EMPTY_CLASS` para T3, O3 y O4 pase de PRELIMINARY.
Resultado esperado: veredicto por afirmación y global (ACCEPT / ACCEPT_WITH_REPAIRS / REJECT), con
las reparaciones obligatorias numeradas.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: deepseek
(familia distinta de Claude, que escribió la carta, el certificado y el informe).
Cierre: informe del revisor y lectura crítica del autor en `verificacion_autor.md`. No promociona
nada ni cambia `state/CURRENT_STATE.md` por sí sola.
Documentos (commit `88b07ed`): `theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`,
`reports/2026-10-28--irreducible-isotropy-step01.md`,
`scripts/verify_irreducible_isotropy_step01.py` y los dos ayudantes que importa en modo lectura,
`scripts/cert_Aa_s4_counterexample.py` y `scripts/verify_weyl_dirac_gate.py`.
Herramienta: revision-ciega del PATH; ~/herramientas commit `83c04f9`.

---
Responde en español. Revisión matemática adversarial e independiente, una sola ronda. Tu sesión
está sellada: sólo tienes los cinco documentos adjuntos (la carta, el informe, el certificado y dos
módulos auxiliares que el certificado importa). No puedes ejecutar código; razona sobre él.

Contexto. Un paseo cuántico en d=3 con soporte en los ocho vértices del cubo N_3 tiene símbolo
U(k) = Σ_h e^{-ik·h} T_h, T_h ∈ C^{s×s}. La carta pregunta si exigir una representación interna
irreducible R de un grupo de rotaciones del cubo (T u O) fuerza que la velocidad de Weyl c_0 coincida
con la velocidad estricta asintótica. El informe concluye que las clases T3 (T, s=3, espín 1), O3
(O, s=3, espín 1) y O4 (O, s=4, espín 3/2) son vacías: no existe ningún símbolo unitario con soporte
en N_3, sin término en el sitio, covariante T_{gh} = R_g T_h R_g^† con esa R irreducible. Lo mismo
afirma para s=2 (espín 1/2) bajo T y O, como control. La prueba es una base de Gröbner exacta igual
a [1] para las identidades de unitariedad de los coeficientes.

Ataca, en este orden:

1. **Corrección del planteamiento.** ¿La covarianza T_{gh} = R_g T_h R_g^† con g actuando por
   rotaciones es la definición correcta y la misma que la de la carta? ¿Es correcto reducir a un
   coeficiente por órbita restringido al conmutante de R sobre el estabilizador del vértice
   (orden 3, levantado a orden 6)? ¿Falta alguna solución por haber exigido que el coeficiente
   conmute con R(estabilizador) en vez de hacerlo salvo una fase proyectiva? Comprueba
   expresamente ese punto para espín 1/2 y 3/2.
2. **Identidades de unitariedad.** ¿Son Σ_{h'−h=ℓ} T_h^† T_{h'} = δ_{ℓ0} I, para todas las
   diferencias ℓ, condiciones necesarias y suficientes de unitariedad del símbolo? ¿Basta imponer
   U^†U = I sin UU^† = I? ¿Partir en parte real e imaginaria y obtener [1] prueba que no hay
   solución real?
3. **Cobertura.** ¿Es correcta la afirmación de que, como las representaciones irreducibles de igual
   dimensión difieren en un carácter unidimensional, espín 1/2, 1 y 3/2 cubren todas las R
   irreducibles de dimensión 2, 3 y 4 de 2T y 2O? ¿Son correctas las dimensiones de las tablas de
   caracteres?
4. **Código.** Busca en `verify_irreducible_isotropy_step01.py` errores que invaliden la conclusión:
   convención de signos h ↔ −h entre los ayudantes y el certificado, emparejamiento rotación ↔
   matriz de espín (homomorfismo frente a antihomomorfismo), construcción del conmutante,
   asignación de vértices por covarianza, generador de ecuaciones, comparaciones estructurales `==`
   donde debería haber diferencias simplificadas. Di si los controles (anulación sobre paseos
   conocidos, homogeneidad sin normalización, control positivo D2/Q8 no vacío) bastan para
   descartar un generador que dé [1] siempre.
5. **Segunda vía.** Si puedes, da un argumento analítico independiente de la base de Gröbner para al
   menos una clase (por ejemplo O3 o T3), o señala por qué no es fácil.
6. **Alcance.** ¿Las conclusiones y los límites del informe (vacío, no refutación; s=1 marcado
   [UNVERIFIED]; nada sobre R reducibles, otros grupos u otros soportes) están bien dichos? Señala
   cualquier sobreafirmación.

Da un veredicto por punto y global: ACCEPT, ACCEPT_WITH_REPAIRS o REJECT, con las reparaciones
obligatorias numeradas y localizadas (fichero y línea o sección). Distingue error matemático,
error de código, laguna de justificación y cuestión de redacción. Marca como NO VERIFICADO lo que
no puedas comprobar sin ejecutar código.
---
