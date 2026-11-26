# Revisión externa: Enmienda 1 de la auditoría de la matriz de transferencia

Autorización: usuario «pide a Grok que revise la enmienda 1» (2026-11-26).
Autor de la enmienda, de la auditoría y de los verificadores: Claude (Opus 5.5).
Revisor: Grok (xAI), otra familia, mediante `revision-ciega grok` del PATH;
generación comprobada antes del envío. Herramientas: `~/herramientas` commit
`4a4fcca`. Revisado: commit `63db34b` (enmienda), sobre la auditoría `d0114b2`
y la revisión previa de Astra. Máximo: una ronda. No se autoriza calcular
transmisión ni promoción. Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la **Enmienda 1** de una auditoría matemática. La
auditoría (B) comprobó una matriz de transferencia espacial 12×12 del paseo
cuántico U = L₋W², W = S C(θ) S C(θ) S C(−2θ), con perfil
t = cos²θ ∈ [5/16, 7/16]. Una revisión previa de otro modelo (Astra) dio PASS
a la matriz y REPAIR_REQUIRED a tres afirmaciones de (B). La Enmienda 1
pretende repararlas. Se adjuntan:

(1) `amendment1.diff`: el diff exacto de (B) introducido por la enmienda;
(2) (B) completa, ya enmendada;
(3) el informe de Astra, con las tres objeciones (texto de un modelo: no es
    fuente);
(4) `verify_dispersive_horizon_transfer_repairs.py`: el verificador nuevo
    (8 comprobaciones) que respalda la enmienda;
(5) `verify_dispersive_horizon_transfer_matrix.py`: el verificador ya revisado
    que (4) importa sin modificarlo (61 comprobaciones).

Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL /
UNVERIFIED, con las derivaciones necesarias:

1. **Multiplicidad en velocidad nula.** En el horizonte t = 3/8, con A = t(2t−1),
   la velocidad infrarroja saliente es nula. Deriva tú, desde
   cos E = A cos 3k + (1−A) cos k y Ω± = −k ± 2E, la multiplicidad algebraica
   de λ = 1 (λ = e^{−ik}) como raíz de det(λ − M_hom) en z = 1, y la
   geométrica. ¿Es 4 y 2, como afirma la enmienda? ¿Y 2 en t = 5/16 y 7/16?
   Comprueba si el coeficiente cúbico de Ω₊ que da Astra (35/32) es correcto;
   la enmienda lo deja sin verificar.
2. **¿Es correcta y suficiente la nueva formulación** sobre raíces en puntos de
   velocidad de grupo nula? ¿Queda alguna otra degeneración del perfil (en
   z = i, en bordes de banda, o en otros valores de t) que la enmienda debiera
   mencionar y no menciona?
3. **Recuento de T3.** En (5), con `NS = 34`, seis pasos `S` y un paso `L`, ¿son
   exactamente 21 los sitios interiores (6..26)?
4. **«Para todo θ admisible, z ≠ 0».** ¿Es la restricción correcta y completa
   para la identidad del polinomio característico y para la matriz?
5. **Verificador (4).** ¿Deciden sus comprobaciones lo que dicen? En particular:
   el bucle que extrae factores (λ − 1) y la comprobación de que el cociente
   no se anula en 1; los dos vectores propios de Bloch en k = 0 (construcción
   de Y con S(0) = I); el menor 10×10 no nulo como cota de rango; posibles
   tests de cero o de no-cero que den falsos positivos; si importar (5) puede
   enmascarar un fallo.
6. **Alcance.** ¿Excede la enmienda, o el registro de la revisión de Astra, lo
   que (4) certifica? ¿Se presentan como verificadas afirmaciones que solo
   argumenta Astra?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que
derivas a mano de lo que solo inspeccionas. No revises de nuevo las 144
entradas salvo que la enmienda las afecte. No calcules transmisión ni evalúes
originalidad.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y
objeciones ordenadas por gravedad con sección y reparación concreta. Si no hay
fallos, dilo sin inventar objeciones.
---
