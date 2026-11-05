# Dos velocidades en la arquitectura s=4: obstrucción exacta

2026-11-05. Autor: Codex. PRELIMINARY, sin revisión independiente,
sin promoción y sin reivindicación de novedad.
Contrato: theory/COMMON_SPEED_S4_PRODUCT_ATTEMPT.md, SHA256 registrado
antes de calcular: 263600afd4de23e22b5602a4daf0d93877efd30b509eb2277101047fa1e2e987.
No prerregistro Git: contrato y resultado están inicialmente sin commit.

## Resultado y alcance

En la arquitectura del contrato, si sobreviven dos conos isotrópicos sin
inclinación en los dobletes nodales complementarios, sus velocidades son
iguales. No existe un testigo de separación dentro de esta clase.
La conclusión admite matrices de desplazamiento generales, no solo las
tensoriales de la familia original. No demuestra que las perturbaciones
conserven los conos, ni que todo QCA de soporte BCC admita esta arquitectura.
Es una obstrucción algebraica condicional, no una ley de universalidad.

## Derivación universal [autor]

Sea G cualquiera de las tres involuciones hermíticas de desplazamiento,
escrita en los dos autoespacios nodales de W:

    G = [ A    B  ] ,  A=A†, D=D†, todos los bloques de tamaño 2.
        [ B†   D  ]

G²=I implica

    A² + BB† = I_2,     D² + B†B = I_2.

Tomando trazas y usando tr(BB†)=tr(B†B):

    tr(A²) = tr(D²).                                      (1)

No se requiere que B sea invertible. Tampoco se usa la simetría D2 ni
la forma particular de las monedas del constructor base.

Para U(k)=W exp(-i k_x G_x/sqrt3) exp(-i k_y G_y/sqrt3)
exp(-i k_z G_z/sqrt3), se tiene

    i W† partial_i U(0) = G_i/sqrt3.

La perturbación degenerada de primer orden dentro de cada autoespacio
aislado de W da las pendientes como eigenvalores de A_i/sqrt3 y
D_i/sqrt3. Esto puede verse directamente expandiendo
U(t e_i)=W(I-i t G_i/sqrt3)+O(t²): al proyectar en un autoespacio,
el desplazamiento de la eigenfase es el espectro de esa compresión.
Los términos entre autoespacios no contribuyen a primer orden porque
las dos fases de W son distintas.

Si ambos conos son sin inclinación e isotrópicos, para cualquier eje i:

    spec A_i = {+sqrt3 c_P, -sqrt3 c_P},
    spec D_i = {+sqrt3 c_Q, -sqrt3 c_Q}.

Sustituyendo en (1), 6 c_P²=6 c_Q². Al ser velocidades positivas,
c_P=c_Q. Basta un eje para esta conclusión; la isotropía convierte esa
igualdad axial en igualdad de las velocidades de los conos.

Es una igualdad exacta en cualquier miembro admisible de esta clase, no
una derivada nula en el parámetro de una familia. No compara directamente
pendientes de direcciones oblicuas si se retira la isotropía.

## Segunda vía y límites de las hipótesis

Para matrices 2x2 sin traza, Cayley–Hamilton da
tr(A²)=-2 det A. Así, (1) equivale a det A=det D y, con traza cero,
a igualdad de sus polinomios característicos. Se recupera la igualdad de
pendientes axiales sin elegir bases de Pauli.

La hipótesis sin inclinación importa: G=diag(1,-1,1,1) es una involución,
pero su bloque A tiene espectro {1,-1} y D espectro {1,1}. La identidad
(1) sigue cierta, aunque las semianchuras espectrales sean distintas.
Este es un caso límite algebraico, no un contraejemplo QCA con dos conos
admisibles.

La clase no es vacía: el constructor original con a=3/5, b=4/5 y
theta=pi/4 conserva los dos conos; su unitariedad, covariancia D2,
compresiones y ocho coeficientes no nulos se comprueban exactamente.
No se ha añadido un nuevo cálculo de irreducibilidad: se usa la
demostración de la familia original en S4_STRICT_CONE_COUNTEREXAMPLE Sec. 6.

## Verificación y antecedentes

Comando: python3 -B scripts/verify_common_speed_s4_product.py
Python con SymPy 1.14.0, salida 0, 34/34 checks exactos. Registro:
reports/2026-11-05--common-speed-s4-product-verifier.txt.
Script SHA256: 8806ef78c28c4db8e367a83f79986325e3153c2f606a2df179dacf110309b745.
Comprueba las identidades simbólicas para bloques generales, la formulación
por determinantes, el límite con inclinación y un punto base admisible.
El argumento universal está en la derivación, no en contar esos checks.

Antecedente primario leído: sources/1609.00305v2.pdf p.4, Ecs.(27)–(29),
Arrighi–Facchini. Ya emplea la identidad de compresión de una involución
y construye bloques D y -D. No afirma aquí nuestro enunciado exacto para
dos conos Floquet, pero el mecanismo algebraico utilizado es elemental
y próximo a ese antecedente. No se presenta esta aplicación como novedosa.
La búsqueda orientativa de compresiones de involuciones y descomposición
coseno-seno no es una auditoría exhaustiva de prioridad.

## Cierre

Resultado del intento: EQUAL_SPEEDS_IN_DECLARED_PRODUCT_ARCHITECTURE,
PRELIMINARY. Se activa el corte: la obstrucción es una consecuencia breve
de la involución y los rangos iguales, y se termina aquí. Quedan abiertas
las perturbaciones del símbolo Laurent completo que no preserven esta
factorización. No se amplía a ellas el contrato para salvar una candidatura.
No se determina el valor común de c: el parámetro a sigue permitiendo
variarlo, como ya establece la familia original.
