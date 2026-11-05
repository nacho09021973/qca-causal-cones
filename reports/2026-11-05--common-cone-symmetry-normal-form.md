# Qué protege la antiunitaria fuera del constructor particular

2026-11-05. Codex. PRELIMINARY, sin revisión independiente ni promoción.
Contrato: theory/COMMON_CONE_LOCAL_SYMMETRY_NORMAL_FORM.md,
SHA256 5d463aea619d21f2c1e5f1e239126fa350bfa4d3e34ac5ae61150aae8e3c82b6.
Forma candidata advertida antes del contrato de comprobación, declarado
allí; no prerregistro de descubrimiento ni de Git.

## Resultado local

Se obtiene una forma necesaria para C=(sigma_y tensor tau_y)K y
R_j=sigma_j tensor I, válida para cualquier símbolo unitario diferenciable
de dimensión cuatro con esas simetrías. No se supone factorización en
desplazamientos. Si conserva dos dobletes nodales distintos en k=0:

    J_i=i U(0)† partial_i U(0)=sigma_i tensor (v_i.tau),

con tres vectores reales v_i. Ambos dobletes tienen la misma dispersión
lineal en magnitud. La simetría no fuerza isotropía ni fija esa magnitud.
El emparejamiento por C ya era conocido: esto explicita sus restricciones
en la representación D2 elegida, sin reivindicar novedad.

## Derivación [autor]

1. Covariancia D2 en k=0 implica que W=U(0) conmuta con todas las Pauli
   del primer factor. Así W=I tensor w, con w unitario 2x2.
   PHS da tau_y w* tau_y=w. En U(2) esto selecciona SU(2): escribiendo
   w=e^(i phi) w0 con w0 en SU(2), la condición exige e^(2i phi)=1.
   Los dos eigenvalores distintos son conjugados, cada uno doble.

2. Unitariedad hace J_i hermítico. D2 exige que R_j J_i R_j† sea J_i
   para j=i y -J_i para j!=i. Expandiendo en las 16 matrices hermíticas
   sigma_mu tensor tau_nu, queda exactamente

       J_i=sigma_i tensor (d_i I+v_i.tau),

   con d_i y componentes de v_i reales. La parte proporcional a la
   identidad del primer factor queda excluida: no hay inclinación lineal.

3. Al derivar V U(k)* V†=U(-k) en el origen, se obtiene
   V (partial_i U)* V†=-partial_i U. La conjugación de i también cambia
   su signo, de modo que V J_i* V†=J_i. Ahora

       V (sigma_i tensor I)* V†=-(sigma_i tensor I),
       V (sigma_i tensor tau_j)* V†=sigma_i tensor tau_j.

   Por tanto d_i=0. Esta es la contribución lineal que la simetría prohíbe.

4. Escribamos los proyectores nodales como
   P=I tensor (I+n.tau)/2 y Q=I-P, con |n|=1. Sus compresiones son

       P J_i P=(v_i.n) sigma_i P,
       Q J_i Q=-(v_i.n) sigma_i Q.

   Si u_i=v_i.n, los dos Hamiltonianos nodales de primer orden tienen
   eigenvalores ±sqrt(sum_i u_i² k_i²). Esto proporciona un mismo cono
   lineal en ambos dobletes, con orientación de Pauli opuesta.
   Solo es isotrópico si u_x²=u_y²=u_z². Se identifica esta obligación;
   no se abre una búsqueda de modelos anisótropos.

## Robustez precisa y término de separación

Para perturbaciones exactas que mantengan C y D2 fijas, la forma anterior
vale en cada punto. Si los dobletes siguen separados, C los empareja.
En una vecindad de un punto con u_x u_y u_z!=0, la continuidad conserva
un cruce cónico no degenerado. No preserva por sí sola la isotropía.
Este argumento no demuestra que cualquier elección de v_i sea realizable
por un QW con un soporte Fourier fijado.

Sin exigir C, D2 permite los términos d_i. Entonces los espectros lineales
son ±sqrt(sum_i (d_i+u_i)² k_i²) y
±sqrt(sum_i (d_i-u_i)² k_i²). La diferencia entre sus coeficientes
cuadráticos por eje es 4 d_i u_i. Para u_i no nulos, igualar esos
coeficientes obliga a d_i=0. Esto es una necesidad LOCAL de primer orden,
no una demostración de PHS exacta en toda la zona de Brillouin.

En el modelo original, d_i=0 y u_i=a/sqrt3. En doble desplazamiento,
usando coordenadas crudas, d_i=1 y u_i=a; la división por 2sqrt3 da las
velocidades previamente verificadas. Se explica así la diferencia entre
los dos ejemplos sin recalcular tablas.

## Comprobación y antecedentes

python3 -B scripts/verify_common_cone_symmetry_normal_form.py
Salida 0, SymPy 1.14.0, 279/279 comprobaciones exactas PASS. Script SHA256:
16639f7fd11d3e42dd9385db58a373d0b2bb3ca976ec876dc41e973ae35cbf4b.
Registro en
reports/2026-11-05--common-cone-symmetry-normal-form-verifier.txt.
El script clasifica las 16 matrices de la base hermítica bajo D2 y C,
comprueba su completitud por ortogonalidad y los dos polinomios
característicos generales. Es verificación local auxiliar, no prueba
de existencia de una familia Laurent arbitraria ni revisión independiente.

Fuente primaria consultada: Asboth, arXiv:1208.2143v2, Sec. III.1,
Ecs.(10)–(11), https://arxiv.org/html/1208.2143v2 . PHS y emparejamiento
de quasienergías ya son conocidos. Sec. III.3 subraya que el operador de
simetría debe mantenerse fijo al variar el modelo; aquí se cumple eso.

## Conclusión física y cierre

Esta condición explica una igualdad entre sectores conjugados, no entre
especies independientes. Tampoco determina el valor de c. Si se añaden
otros pares conjugados, la simetría no contiene ninguna ecuación que
iguale sus pendientes a las del primer par; no se ha construido aquí
un nuevo ejemplo de más dimensión.

No basta tener la condición para obtener una explicación de la c universal
de la naturaleza. Haría falta justificar el emparejamiento físico y un
mecanismo adicional que relacione pares distintos. La forma normal es
álgebra de simetrías estándar y se termina esta derivación sin atribuirle
novedad ni abrir modelos adicionales.
