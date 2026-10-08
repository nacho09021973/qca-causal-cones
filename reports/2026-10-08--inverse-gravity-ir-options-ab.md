# IG1e — opción A y alternativa B para la referencia IR

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato y controles congelados en `2bee60512fb88fd012284eaa846787fad4047e19`:
[opciones A/B](../theory/INVERSE_GRAVITY_IR_OPTIONS_AB.md),
[script](../scripts/verify_inverse_gravity_ir_options_ab.py).

## 1. Selección realizada

| Opción | Estado definido | Criterio físico buscado | Primer descarte |
|---|---|---|---|
| A, prioritaria | Gibbs restringido de H_A local, β=1 como control; mínimo de H_A como receta posterior si conserva energía | Selección por energía local conservada, sin ordenar quasifases | Un testigo exacto de `[U,H_A]|H_P≠0` |
| B, contingencia | Promedio Cesàro de la semilla Gibbs β=1 bajo el mismo tick U | Estado estacionario seleccionado por la dinámica real | Respuesta local nula o falta de método/límite local controlado |

H_A es la suma local de los generadores hermíticos de las puertas, con signo
negativo y pesos iguales congelados. Su uso como semilla no identifica su
energía con quasienergía ni asume que U conserve H_A.
Ni A ni B está aprobada científicamente como referencia gravitatoria.

El contrato fija estados, batería de fuentes/observables, orden de límites,
activación B y qué hacer ante un límite de método. No se escoge otro peso,
β, ángulo o observable tras un fallo. Si A queda sin resolver, B puede
activarse con A OPEN, dejando el límite escrito; no convertir coste en refutación.

## 2. Control matemático de A

En volumen finito restringido a H_P, σ_A=e^-H_A/Z es positiva y de rango
completo. Si `[U,H_A]=0`, entonces Uσ_AU†=σ_A.
Recíprocamente, si Uσ_AU†=σ_A, aplicar el logaritmo hermítico único da
`U(-H_A-log Z)U†=-H_A-log Z`; por tanto `[U,H_A]=0`.

La equivalencia es exacta a β=1; no exige diagonalizar para ordenar eigenfases.
Si H_A se conserva, también se conserva su proyector de mínima energía.
Una Gibbs local no es por eso automáticamente una fase IR o un vacío Einstein.

El control qutrit del script usa una pareja Weyl y el mismo ángulo de puerta
para exhibir `[U_control,H_control]≠0`. Muestra que no existe una implicación
automática de conservación al formar puertas con términos de H. **No es un
testigo contra A en la red espacial ni en su sector físico. A0 sigue NOT_TESTED.**

## 3. Control matemático de B

En cada volumen finito, escribir U|H_P mediante proyectores de eigenfase Π_φ.
En el promedio temporal, cada bloque Π_φ σ Π_φ' se multiplica por
`M^-1 sum_n exp[i n(φ-φ')]`. El factor converge a cero si las fases difieren
módulo 2π y a 1 si coinciden. Por ello el promedio existe y es

`ρ_B=sum_φ Π_φ σ Π_φ`.

Es positivo, normalizado, físico y estacionario. Las coherencias dentro de
un bloque degenerado se conservan; no se depende de una base de eigenvectores.
No hay garantía de memoria local, respuesta no nula ni vacío de baja energía.

Segunda vía: para el promedio truncado ρ_M, telescopar da

`Uρ_MU†-ρ_M=(U^M σ U^-M-σ)/M`,
`||Uρ_MU†-ρ_M||_1≤2/M`.

Es una cota uniforme de defecto de estacionariedad, **no** una cota de
`||ρ_M-ρ_B||_1` ni de error de sus respuestas respecto al ensemble límite.
No permite elegir M por esa sola fórmula y declarar el estado IR convergido.

El script verifica dos controles 3×3: promedio de un periodo completo con
estado estacionario no tracial y respuesta a n=1 de -2/3; y conservación de
coherencia en un bloque degenerado. Esos valores pertenecen al control,
no al autómata. No se aplican a la red por analogía.

## 4. Fuentes y límite de transferencia

Se consultó `biblioteca/INDICE.md` antes de buscar. Lectura local primaria:
Gu–Wen `biblioteca/arXiv-0907.1203.pdf` pp.15–16 para los operadores
auxiliares y restricciones; `biblioteca/arXiv-1701.01440.pdf` pp.1–2 para
distinguir modelos Floquet con gauge conservado y estrategias de evitar
calentamiento. No se importa su fase quiral ni disorder a nuestra clase.

Lectura acotada adicional, en abstracts originales de arXiv:

- [Lazarides–Das–Moessner, 1403.2946](https://arxiv.org/abs/1403.2946):
  estudia pérdida de memoria local en sistemas periódicos genéricos no
  integrables. Motiva vigilar ese fallo en B, pero no prueba ergodicidad ni
  calentamiento del tick q=3 con constraints. No se usó como no-go.
- [Shirai–Mori–Miyashita, 1410.0464v3](https://arxiv.org/abs/1410.0464v3):
  las condiciones declaradas para un Floquet-Gibbs se refieren a sistemas
  abiertos con baño y acoplamiento débil. No justifican importar un Gibbs
  a nuestro QCA cerrado. A usa una prueba de conservación propia; B no añade baño.

No se descargaron esos dos PDFs ni se añadieron al catálogo. Solo se afirma
lo comprobado en los abstracts originales; sus hipótesis completas siguen
fuera de esta lectura acotada. Las derivaciones A/B anteriores son directas.
No se hace búsqueda exhaustiva ni claim de novedad.

## 5. Ejecución, estado y siguiente paso

Comando `python3 -B scripts/verify_inverse_gravity_ir_options_ab.py`.
SymPy 1.14.0, código 0, exacto; salida íntegra en
[certificado](2026-10-08--inverse-gravity-ir-options-ab-certificate.txt).
Resultado `AB_ALGEBRA_CONTROLS_PASS / SPATIAL_A_AND_B_OPEN`.
Contrato y script no cambiaron después de ejecutar.

Se completó la selección de dos opciones y sus mecanismos de descarte.
**El siguiente paso operativo es A0:** probar o romper la conservación de
H_A por el tick completo en H_P mediante un test algebraico localizado.
No construir una matriz de dimensión 729^(L³) para luego llamarla viable.
Antes de cualquier código que produzca ese testigo, congelar su alcance,
procedimiento y criterio, con artefacto permanente.

Si A0 falla, activar B0 con la semilla ya fijada, sin pedir una nueva elección
de ruta. Su estacionariedad formal ya está demostrada; su acceso computacional,
memoria local, respuesta y control IR aún deben justificarse.
