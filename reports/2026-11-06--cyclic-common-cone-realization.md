# Intento de realización: fallo de la covariancia cíclica exacta

2026-11-06. Codex. Base de entrada: 74db229, research/schur-stability-audit.
Autorización: «autorizada opcion 1». PRELIMINARY, comprobación de autor,
sin revisión independiente, promoción ni reivindicación de novedad.

Contrato escrito y SHA256 medido antes de ejecutar:
theory/CYCLIC_COMMON_CONE_REALIZATION_ATTEMPT.md,
c73f93576e6b811e7b0e00a9ec881e23a7457b23c3a38e0cdf7193a50f37fd54.
No prerregistro Git. El riesgo del orden de factores estaba advertido.

## Resultado

**CANDIDATE_FAILS_CYCLIC_COVARIANCE.** La única candidata congelada tiene
unitariedad para todo k, soporte BCC completo, PHS fija, D2 exacta y
conmutante escalar. Sus dos dobletes tienen conos isotrópicos de igual
velocidad sqrt3/5. Sin embargo, la actualización completa NO tiene la
covariancia cíclica añadida. No se obtiene PROTECTION_IN_NONEMPTY_CLASS
para el grupo ampliado. Se activa el corte y termina este constructor.

## Candidata y controles positivos

En C²_sigma tensor C²_tau, a=3/5, b=4/5:

    T=b tau_x+a tau_z,  G_i=sigma_i tensor T,
    W=I tensor exp(-i pi tau_z/4),
    U(k)=W E_x(q_x) E_y(q_y) E_z(q_z),
    E_i(q)=cos(q)I-i sin(q)G_i,  q_i=k_i/sqrt3.

Los T_i distintos de la familia original se sustituyen aquí por UN T
común, como fija este contrato separado; no es una modificación de sus
resultados ni un barrido de sus parámetros. Las coordenadas y unidad
temporal se conservan.

G_i²=I y G_i†=G_i. Cada factor es unitario; la convolución da exactamente
los ocho coeficientes no nulos

    A_h=W (I+h_x G_x)(I+h_y G_y)(I+h_z G_z)/8,
    h=(±1,±1,±1), desplazamiento físico h/sqrt3.

La comprobación Laurent de ambos productos U†U y UU† cubre los 27
desplazamientos diferencia posibles. No se deduce unitariedad de una malla.
C_micro=[-1/sqrt3,1/sqrt3]³ y r_in=1/sqrt3. El grupo de traslaciones
es el BCC generado por esos pasos, no todo Z³ en coordenadas crudas.
No se calcula el cuerpo asintótico ni V_grp^max.

Con R_j=sigma_j tensor I, los coeficientes son D2-covariantes.
Con V=sigma_y tensor tau_y satisfacen V A_h* V†=A_h, de donde
V U(k)* V†=U(-k), C²=I. El asterisco conjuga entradas.

W tiene fases ±pi/4 separadas y proyectores P,Q de rango dos.
Las compresiones son P G_i P=a R_i P y Q G_i Q=-a R_i Q.
Por perturbación nodal degenerada:

    H_P(k)=a k.sigma/sqrt3,  H_Q(k)=-H_P(k),
    H_P²=H_Q²=(a²/3)|k|² I_2.

No hay inclinación; c_P=c_Q=a/sqrt3=sqrt3/5>0. Segunda comprobación
axial: en el sector sigma_i=eps, la semitraza del bloque SU(2) es
f_eps(q)=(cos q-eps*a sin q)/sqrt2. La derivada en q=0 de
acos(f_eps) es eps*a; restaurar q=k_i/sqrt3 reproduce la pendiente.

Irreducibilidad global: todo X que conmute con los A_h conmuta con
su suma W y sus primeros momentos W G_i; por tanto conmuta con G_i.
Conmutar con W fuerza X=diag(X_P,X_Q) en los sectores tau_z. Como
a!=0, las partes diagonales de G_i fuerzan X_P=lambda_P I_2 y
X_Q=lambda_Q I_2. Como b!=0, la parte entre sectores fuerza
lambda_P=lambda_Q. El conmutante es C I. El sistema exacto de
[X,W]=[X,G_i]=0 tiene rango 15 sobre 16 incógnitas complejas.
No es una suma directa por un cambio de base constante.

## Condición decisiva, comprobada por dos vías

S=s tensor I, s=(I-i(sigma_x+sigma_y+sigma_z))/2, es unitario,
S³=-I y S G_i S†=G_(i+1). También conserva W y es compatible con
C fija. El giro espacial es r(k_x,k_y,k_z)=(k_z,k_x,k_y).
Por tanto transforma correctamente las primeras derivadas, pero

    S U(k) S† = W E_y(q_x) E_z(q_y) E_x(q_z),
    U(rk)     = W E_x(q_z) E_y(q_x) E_z(q_y).

Los órdenes difieren. Sobre q=(t,0,t), la diferencia exacta es

    D(t)=W[E_y(t)E_x(t)-E_x(t)E_y(t)]
        =2i sin²(t) W (sigma_z tensor I).

Aquí se usa T²=I y [G_x,G_y]=2i sigma_z tensor I. D(pi/2) es
no nula: la condición falla exactamente, sin tolerancia ni ajuste.
Además D(t)=2i t² W(sigma_z tensor I)+O(t⁴): explica por qué el
término lineal satisface la simetría que la actualización rompe.

La vía independiente compara S A_h S† con A_(r h): falla en los ocho
coeficientes. El testigo en momentos se calcula además directamente
desde el producto, no se reconstruye a partir de esas diferencias.

## Alcance, robustez y cierre

La candidata no pertenece a la clase con D2, C y S exactas, por lo que
no se ejecuta la obligación dependiente de robustez dentro de esa clase.
La igualdad e isotropía de sus conos en este punto no constituye prueba
de protección por S. No se sustituye covariancia de U por la de su término
lineal ni por la simetría geométrica del soporte.

El fallo descarta este constructor xyz con los datos fijados. No descarta
otros símbolos Laurent con N3, otras representaciones ni otras
arquitecturas. No se cambia ninguna de ellas en este intento. La
existencia general sigue OPEN; la obstrucción aquí es el orden de
factores no conmutativos. No se proclama un no-go general.

La covariancia microscópica exigida sigue la distinción ya comprobada en
sources/1708.00826v2.pdf p.2, Definición 1 y Ec. (4), releídas hoy:
equivalencia dinámica de direcciones, además de geometría. Esa fuente
no se cita como demostración de este fallo ni se extiende su clasificación
s=2 a s=4. La carpeta biblioteca/ sigue ausente; no se creó un índice.

SELECTION_MECHANISM_NOT_SPECIFIED. No resultado sobre valor físico de c,
universalidad entre pares independientes o novedad. Hexagonal aparcado.

## Ejecución y provenance

Código permanente: scripts/verify_cyclic_common_cone_realization.py.
SHA256: 134fe097b9c2a82e2d09e992bb8cbd56852b192f3ceab6ed757c7e68a0539c69.
Comando desde la raíz:

    /home/adnac/venvs/torch-gpu/bin/python -B scripts/verify_cyclic_common_cone_realization.py

Python 3.12.3, SymPy 1.14.0, salida 0, **139/139 checks exactos PASS**;
incluyen afirmar el defecto, no aprobar la candidata. Registro completo:
reports/2026-11-06--cyclic-common-cone-realization-verifier.txt.

Incidencias de ejecución: python3 del sistema no tiene SymPy; se usó el
entorno existente indicado. La primera ejecución allí se detuvo al comparar
las fases exponenciales con radicales: se hizo explícita su expansión
compleja y se repitió el mismo verificador. Ningún parámetro ni condición
científica cambió. El registro conserva la ejecución final completa.

No código científico temporal, barridos ni revisión por terceros.
La derivación y la segunda vía son autocomprobación, no revisión
independiente. Cierre documental con git diff --check; sin promoción.
