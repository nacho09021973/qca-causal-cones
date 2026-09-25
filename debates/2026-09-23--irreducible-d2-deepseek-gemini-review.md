---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-23 17:30
proyecto: /home/ignac/qca-causal-cones
tema: debates/2026-09-23--irreducible-d2-review-request.md
rondas: 2
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - ABNER — DeepSeek — api.deepseek.com/deepseek-v4-pro
  - GEMINI — Google — generativelanguage.googleapis.com/gemini-3.1-pro-preview
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

# Revisión independiente: irreducibilidad D2 y aplicación de P17

Solicitud del P.I.: revisión por Gemini y DeepSeek; si ambos aceptan sin
reparaciones obligatorias, commit y push acotados a esta evidencia.
No se solicita promoción de CURRENT_STATE ni ampliación del frente.

## Integridad y autoría

Autor de la prueba y del verificador: Codex /root. Revisores solicitados:
DeepSeek (ABNER) y Gemini, familias distintas del autor. El protocolo de
Sanedrín es una deliberación compartida, no dos revisiones ciegas.
Cada revisor debe reconstruir los pasos y emitir su propio veredicto.

Objeto primario, aún sin commit: `reports/2026-09-23--irreducible-d2-pavia-checks.md`.
SHA256: `2c2024c8de8b9ac7261bd761f25e34d787481dcb24cdae8bfe649aee6f4cd684`.
Verificador: `scripts/verify_irreducible_d2_pavia.py`.
SHA256: `878542f6999351ef6e229e4abe379245312520cdf21df0594825803890f8a27e`.
El registro de ejecución adjunto acredita 519 checks exactos en el entorno
del coordinador. Vosotros no tenéis herramientas y no debéis afirmar que
habéis reejecutado Python, leído un PDF binario o verificado Git/hashes.
El resultado del checker no demuestra por sí solo la completitud de P17
ni el argumento analítico de todos los tiempos: auditadlos por separado.

Baseline Git: `835d31a37c122560f685dd612e04771699b3c7df`.
Sanedrín: `8162508e3bd0e3d05770b4dd544fe7c962d0272c`.
Herramientas compartidas: `1ce73d26a5fc116c2ab83fa6f3b55d24f9110aa4`.

## Fuente primaria admitida

D'Ariano, Erba, Perinotti, arXiv:1708.00826v2, las 16 páginas completas.
PDF versionado: `sources/1708.00826v2.pdf`, SHA256
`dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81`.
El texto adjunto es su extracción íntegra mediante el comando reproducible:

```bash
pdftotext -layout sources/1708.00826v2.pdf debates/2026-09-23--irreducible-d2-p17-source.txt
```

La extracción conserva saltos de página y puede tener defectos de notación.
Extractor: pdftotext 24.02.0. SHA256 del texto extraído:
`24dd26aa918c329c4508c789d04f10b6f7eceb98ba3d816c2a43f241bb289327`.
Si una ambigüedad afecta al argumento, identificarla; no suplirla de memoria.
Paginación del arXiv: definición y (2), p.2; (6)-(9), pp.3-4;
normalización/Schur, pp.3-4; derivación d=3 y Proposición 5(c), pp.6-7.
La prueba sometida a revisión es objeto de crítica, no fuente autorizada
para sus propias conclusiones. La geometría y el checker histórico son
definiciones y código inspeccionables, no votos previos a favor del objeto.

## Obligaciones: PASS / INCOMPLETE / FAIL por separado

1. Alcance y representación. Para el D2 espacial fijado y su clase
   proyectiva no trivial de Pauli, demostrar s=2 al exigir R irreducible;
   comprobar Schur y la fase global, sin atribuirle una velocidad.
2. Condición (2). Rehacer desde los coeficientes de U Udag y Udag U los
   pasos (D1)-(D3), incluidos signo/orden de adjuntos, enumeración de pares,
   y contradicción cuando A_h=A_j. ¿Funciona realmente en dimensión
   arbitraria con este soporte, sin rank-one o clasificación circular?
3. Aplicabilidad de P17. Contrastar todas las hipótesis con la fuente
   primaria; comprobar que no se confunden irreducibilidad dinámica,
   homogeneidad, fiel representación proyectiva, grupo espacial o embedding.
   Se admite usar la clasificación publicada como teorema previo: no se
   exige redemostrar todo el artículo ni se reclama hacerlo.
4. Formas normales. Verificar la transcripción de Proposición 5(c), momentos
   lineales, signo Fourier, c0, determinantes y trazas de vértices, y la
   deducción para todo n de C_strict=C_micro. Auditar el código y su
   diccionario epsilon=+1 -> A-, epsilon=-1 -> A+; no tomar un PASS
   computacional como sustituto de la prueba analítica.
5. Equivalencias. Comprobar conjugación, fase, permutación tetraédrica,
   reflexión y normalización izquierda permitida. Distinguir traslados del
   nodo de afirmaciones en k=0. ¿Se preservan S_n y la comparación de
   velocidades para toda la clase declarada, no solo dos ejemplos?
6. Techo. La conclusión es suficiente solo para la clase de §1. No implica
   necesidad de irreducibilidad, otros grupos/soportes/nodos, novedad,
   universalidad entre especies, estado canónico o reapertura de E/AdS.

Emitid tabla de seis obligaciones y veredicto global en la primera
intervención, y confirmad/corregid el veredicto personal al cierre:
`D2_P17_REVIEW_ACCEPTED`, `D2_P17_REPAIR_REQUIRED`, `D2_P17_FAIL` o
`D2_P17_INCOMPLETE`. Ataques concretos con condición de concesión.
Distinguid reparaciones obligatorias de mejoras opcionales. La aceptación
del otro revisor no es prueba. No modificar archivos ni ampliar el alcance.
Una ausencia/fallo/cuota no cuenta como acuerdo; no publicar como aprobado
si la revisión queda incompleta o degradada.

## Contexto

### Contexto adjunto: reports/2026-09-23--irreducible-d2-pavia-checks.md
```
# Irreducible D2: P17 condition (2) and strict-support transport

Date: 2026-09-23.
Author: Codex, agent /root.
Repository baseline: `835d31a37c122560f685dd612e04771699b3c7df`.
Evidence level: **PROOF_WRITTEN / INDEPENDENT_REVIEW_PENDING**.
This is a scoped application of a published classification, not a novelty
claim, a canonical promotion, or an independent review of that classification.

## 1. Task and fixed class

The user authorized two checks: whether P17 condition (2) follows in the
current irreducible-representation setting, and whether the equivalences
needed to apply P17 preserve the strict asymptotic comparison. The class
below retains the geometry and symmetry discussed before this execution:

- Three spatial dimensions, homogeneous finite-range unitary symbol
  `U(k) = sum_h exp(-i k.h) A_h` on the lattice generated by `N`.
- `N = {(+/-1,+/-1,+/-1)/sqrt(3)}`, all eight coefficients nonzero;
  no other displacements or on-site coefficient.
- Euclidean Cartesian metric, unit-length neighbors, one full update per
  time unit. No physical stretching, moving frame, or time regrouping.
- `S+ = {h1,h2,h3,h4}` with integer numerators respectively
  `(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)`; `S- = -S+`.
- Spatial group `D2 = Z2 x Z2`, generated by coordinate-axis half-turns,
  acting transitively on `S+`. Covariance is
  `A_{g h} = R_g A_h R_g^dagger`.
- The internal representation is unitary, projective, **irreducible in
  the nontrivial Pauli projective class**. Its dimension is initially finite.
- Selected node `k=0`; subtract only its common quasienergy phase. The
  low-energy object is the whole resulting two-component sector.

No claim is made for arbitrary symmetry groups, support sets, projective
classes, other nodes, or irreducibility of dynamics in place of that of R.

## 2. Primary sources and provenance

The primary input is D'Ariano, Erba, Perinotti, *Isotropic quantum walks on
lattices and the Weyl equation*, arXiv:1708.00826v2 (2017), local
[`biblioteca/1708.00826v2.pdf`](../biblioteca/1708.00826v2.pdf).
SHA256: `dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81`.
The tracked copy [`sources/1708.00826v2.pdf`](../sources/1708.00826v2.pdf)
has the identical SHA256 and is the checker's reproducible input.
Page numbers here refer to this 16-page arXiv PDF, not the journal version.

- p. 2: Definition 1, covariance, active generators, condition (2).
- pp. 3-4: Fourier convention (6), unitarity equations (7)-(8), origin
  normalization (9), and restoration by a unitary in the symmetry commutant.
- pp. 6-7: d=3 derivation, equations (24)-(25), phase/sign equivalences,
  and Proposition 5(c), including the explicit eight coefficients.
- p. 4: change of lattice representation (11). This is separated below
  from physical isometries; it is not used to alter our fixed embedding.

The repository baseline supplies the definition of strict support in
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md), section 6.
The existing standard-family verifier is used only as a second check of
the representative dictionary, not as the source of P17 coefficients.
Those coefficients are transcribed directly from Proposition 5(c).

## 3. Irreducible Pauli-class D2 forces s=2

Rephase two projective generators to Hermitian involutions `X,Z` with
`X^2=Z^2=I` and `XZ=-ZX`. The anticommutation relation follows from the
fixed nontrivial projective class; it is not an extra property of U.
Z exchanges the +1 and -1 eigenspaces of X. They therefore have equal
dimension m. Choosing an orthonormal basis in one and its Z-image in the
other yields

`X = sigma_z tensor I_m`, `Z = sigma_x tensor I_m`.

The representation contains the invariant two-dimensional subspaces
associated with each multiplicity basis vector. It is irreducible iff
`m=1`. Equivalently, its commutant is `I_2 tensor M_m(C)`, scalar iff m=1.
Thus `s=2`. There is no irreducible `s=4` representation in this same
projective class of this same group.

At zero, covariance implies `[U(0),R_g]=0`. Schur and unitarity give
`U(0)=exp(i phi) I_2`. Set `W=exp(-i phi) U`, so W(0)=I. This changes no
Fourier support at any time and shifts all quasienergies by a constant.
Schur alone does **not** determine any spatial derivative of W.

## 4. Condition (2) follows from the fixed BCC geometry and unitarity

In fact this step works for arbitrary finite internal dimension, without
using representation irreducibility or rank-one transition matrices.

Write `d` for a displacement difference. Unitarity gives both identities

`sum_{p-q=d} A_p A_q^dagger = 0`,

`sum_{p-q=d} A_q^dagger A_p = 0` for d != 0.

For any corner h, the only pair with p-q=2h is (h,-h), hence

`A_{-h}^dagger A_h = 0`.                                      (D1)

For distinct h,j in the same tetrahedron, exactly two ordered pairs have
p-q=h-j: `(h,j)` and `(-j,-h)`. Indeed h and j agree in one coordinate
and differ in the other two; the two differing coordinates fix p and q,
and the equal coordinate has exactly two choices. Therefore

`A_h A_j^dagger + A_{-j} A_{-h}^dagger = 0`.                    (D2)

Right-multiply (D2) by A_h and apply (D1):

`A_h A_j^dagger A_h = 0`.                                     (D3)

If A_j=A_h, then `A_h A_h^dagger A_h=0`, which forces A_h=0: in an SVD
all singular values would obey `s_r^3=0`. This contradicts active support.
As a second formulation, left multiplication by A_h^dagger gives
`(A_h^dagger A_h)^2=0`; positivity implies A_h=0.

Thus distinct generators within S+ have distinct coefficient matrices.
By covariance, `[R_g,A_h]=0` would imply `A_{g h}=A_h`. Whenever g h != h
this is impossible. This is exactly P17 condition (2).

In particular this condition also follows for the existing active-support
s=4 counterexample. It does not distinguish that counterexample from the
minimal family; representation irreducibility is the added restriction here.

**Boundary:** this implication uses the two-pair difference geometry. It is
not a consequence of translation invariance or Schur in a general graph.
Allowing an on-site coefficient alone would not affect (D1)-(D2), since it
creates no additional pairs at these differences, but the task's class
continues to exclude it. Additional nonzero displacements could affect them.

## 5. P17 application and direct check of its normal forms

The preceding steps provide s=2, projective covariance, transitivity,
active generators and condition (2), on the connected rank-three lattice
generated by N. These meet the d=3 hypotheses used by P17. We use its
published completeness result; we do not independently re-prove the full
classification of graphs or coefficients here.

For epsilon in {+1,-1}, define `eta=(1+epsilon i)/4`, `mu=conj(eta)`.
P17 Proposition 5(c), with the tetrahedron labeling of section 1, gives:

| h | A_h | A_{-h} |
| --- | --- | --- |
| h1 | `eta [[1,0],[1,0]]` | `mu [[0,-1],[0,1]]` |
| h2 | `eta [[0,1],[0,1]]` | `mu [[1,0],[-1,0]]` |
| h3 | `eta [[0,-1],[0,1]]` | `mu [[1,0],[1,0]]` |
| h4 | `eta [[1,0],[-1,0]]` | `mu [[0,1],[0,1]]` |

Using these coefficients with our negative Fourier exponent gives W(0)=I
and the Hermitian first moments

`H_x = sigma_x/sqrt(3)`, `H_y = epsilon sigma_y/sqrt(3)`,
`H_z = sigma_z/sqrt(3)`.

Since `W(k)=I-i sum_i k_i H_i+O(|k|^2)`, the continuous logarithm at I has
these same linear terms. Their anticommutators are
`{H_i,H_j}=2 delta_ij I/3`, proving `c_0=1/sqrt(3)` at this node.
The exact determinant is one. As another check, the Hessian of
`tr W(k)/2` is `-delta_ij/3` and its first derivative vanishes.

Every vertex matrix has determinant zero and nonzero trace: eta on S+,
mu on S-. Cayley-Hamilton gives `A_h^n=(tr A_h)^(n-1) A_h != 0` for all
n>=1. Each h is an extreme point of the cube, so the only n-step path to
n h repeats h at every step. Its coefficient is exactly A_h^n. Hence

`conv(S_n/n)=[-1/sqrt(3),1/sqrt(3)]^3` for every n>=1,

and consequently `c_strict^iso=1/sqrt(3)`.

The representative dictionary, with the same negative-exponent convention,
is P17 epsilon=+1 -> repository A-, and epsilon=-1 -> repository A+.
This is checked coefficient by coefficient, not just through eigenvalues.
P17 itself uses a positive Fourier exponent in (6): evaluating its printed
symbol at -k implements our convention, an orthogonal spatial inversion.

## 6. Which equivalences preserve this comparison?

Let `U(k)^n = sum_x exp(-i k.x) C_n(x)`. The following formulas prove
support transport at every n, not merely at one step.

| Transformation | n-step coefficient/support | IR comparison |
| --- | --- | --- |
| Constant conjugation `V U V^dagger` | `V C_n(x) V^dagger`; same S_n | Same eigenphases at the same node |
| Global phase `exp(i phi) U` | `exp(i n phi) C_n(x)`; same S_n | Same slopes relative to shifted quasienergy |
| Orthogonal coordinates `U(Q^T k)` | coefficient at Qx is C_n(x); support Q S_n | Euclidean speeds and minimum support unchanged |
| Internal transpose `U(k)^T` | `C_n(x)^T`; same S_n because `(U^T)^n=(U^n)^T` | Same characteristic polynomial and eigenphases |
| Momentum shift `U(k+kappa)` | `exp(-i kappa.x) C_n(x)`; same S_n | Same local dispersion at the transported node `k0-kappa`, not necessarily at zero |

The d=3 coefficient reductions on P17 p. 7 use global phases, constant
unitary conjugations (sigma_z and `exp(+/-i pi sigma_z/4)`), and a
generator exchange h1 <-> h4. Every permutation of this **regular**
tetrahedron extends to an orthogonal linear transformation: its Gram
matrix has diagonal 1 and off-diagonal -1/3, and the only relation is
`sum_i h_i=0`. Thus the linear map sending each h_i to its permuted
partner is well-defined and preserves inner products on their span R^3.
It also sends -h_i to the corresponding -h_i. All 24 permutations are
checked explicitly by the verifier. Reflection is permitted here and
may change a chirality label, but preserves both scalar speeds.
Internal changes of basis and spatial relabelings transport the symmetry
representation and its group labels along with the symbol; they do not
hold a conflicting matrix realization of R fixed.

The uniform left multiplier restored after P17 (9) must commute with R.
In the present irreducible class it is only a global phase, already covered.
An arbitrary noncommuting left unitary is **not** an allowed equivalence.

No nonorthogonal embedding from P17 (11) is needed: our D2 action is already
orthogonal and our tetrahedron is fixed and regular. A change of abstract
lattice basis merely relabels sites if their physical positions are
transported unchanged. Actually stretching those positions in the fixed
Euclidean metric is a different problem and is not covered by this proof.
Likewise, an arbitrary generator permutation outside this tetrahedral
setting need not be an isometry. No momentum shift is needed for the P17
normal forms at zero; the table records its exact boundary so that a
future node relabeling cannot silently become an origin-node claim.

## 7. Result and evidence ceiling

**For the class in section 1**, irreducibility in the Pauli projective
class reduces the internal dimension to two; BCC unitarity supplies
P17 (2); P17 classifies the remaining symbols; its required d=3
equivalences preserve the strict-support and origin-speed comparison.
The resulting application yields

`c_0 = c_strict^iso = 1/sqrt(3)`.

This is a sufficient package, not a proof that representation
irreducibility is necessary for equality, nor a theorem that it suffices
for other groups/geometries. The speed value comes from unitarity plus
the classified forms, **not** from Schur alone. The known dynamically
irreducible s=4 counterexample remains outside this package because R is
reducible. No status in CURRENT_STATE, H1, C3 or E/AdS is changed.

The permanent checker is
[`scripts/verify_irreducible_d2_pavia.py`](../scripts/verify_irreducible_d2_pavia.py).
Its generated record is
[`2026-09-23--irreducible-d2-pavia-verification.md`](2026-09-23--irreducible-d2-pavia-verification.md).
The checker verifies the finite geometry used by (D1)-(D3), exact normal
forms, covariance, distinguishability, both-sided unitarity, dispersion,
vertex survival identities, and the explicit representative dictionary.
It does not turn the analytic all-n argument or P17 completeness into a
machine-checked theorem. All calculations and the analytic argument here
are by the same author: independent review remains pending.
```

### Contexto adjunto: scripts/verify_irreducible_d2_pavia.py
```
"""Exact checks for the scoped irreducible-D2 application of P17.

Run from the repository root:
  python -B scripts/verify_irreducible_d2_pavia.py --output \
    reports/2026-09-23--irreducible-d2-pavia-verification.md

No sampling, fits, or numerical tolerances. The analytic completeness and
all-time support arguments live in the companion report, not in this script.
"""

import argparse
import hashlib
import itertools
from pathlib import Path
import platform

import sympy as sp

from verify_weyl_dirac_gate import fourier_support, published_symbol


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/1708.00826v2.pdf"
SOURCE_HASH = "dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81"
REPORT = ROOT / "reports/2026-09-23--irreducible-d2-pavia-checks.md"
BASELINE_SCRIPT = ROOT / "scripts/verify_weyl_dirac_gate.py"
I2 = sp.eye(2)
PAULI = (sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1))
POSITIVE = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
CORNERS = tuple(itertools.product((-1, 1), repeat=3))
CHECKS = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zero(label, expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    residuals = [sp.simplify(sp.expand(entry)) for entry in entries]
    if any(entry != 0 for entry in residuals):
        raise ValueError(f"{label}: nonzero or unresolved residual {residuals}")
    CHECKS.append(label)


def equal(label, actual, expected):
    if actual != expected:
        raise ValueError(f"{label}: {actual!r} != {expected!r}")
    CHECKS.append(label)


def neg(h):
    return tuple(-v for v in h)


def difference(h, j):
    return tuple(a - b for a, b in zip(h, j))


def pair_index():
    result = {}
    for h, j in itertools.product(CORNERS, repeat=2):
        result.setdefault(difference(h, j), []).append((h, j))
    return result


def verify_geometry(pairs):
    for h in CORNERS:
        equal(f"unique opposite difference {h}",
              set(pairs[tuple(2 * v for v in h)]), {(h, neg(h))})
        for j in CORNERS:
            if h == j or sp.prod(h) != sp.prod(j):
                continue
            equal(f"two-pair tetrahedral difference {h},{j}",
                  set(pairs[difference(h, j)]), {(h, j), (neg(j), neg(h))})
    for permutation in itertools.permutations(range(4)):
        # Integer tetrahedron has sum v_i v_i^T = 4 I_3.
        q = sum((sp.Matrix(POSITIVE[permutation[i]]) * sp.Matrix(POSITIVE[i]).T
                 for i in range(4)), sp.zeros(3)) / 4
        zero(f"tetrahedron permutation {permutation}: orthogonal", q.T * q - sp.eye(3))
        for i in range(4):
            zero(f"tetrahedron permutation {permutation}: image {i}",
                 q * sp.Matrix(POSITIVE[i]) - sp.Matrix(POSITIVE[permutation[i]]))


def p17_coefficients(epsilon):
    """Direct transcription of Proposition 5(c), arXiv PDF p. 7."""
    eta = (1 + epsilon * sp.I) / 4
    mu = sp.conjugate(eta)
    plus = (sp.Matrix([[1, 0], [1, 0]]), sp.Matrix([[0, 1], [0, 1]]),
            sp.Matrix([[0, -1], [0, 1]]), sp.Matrix([[1, 0], [-1, 0]]))
    minus = (sp.Matrix([[0, -1], [0, 1]]), sp.Matrix([[1, 0], [-1, 0]]),
             sp.Matrix([[1, 0], [1, 0]]), sp.Matrix([[0, 1], [0, 1]]))
    result = {h: eta * a for h, a in zip(POSITIVE, plus)}
    result.update({neg(h): mu * a for h, a in zip(POSITIVE, minus)})
    return result


def verify_form(epsilon, pairs):
    coefficients = p17_coefficients(epsilon)
    label = f"P17 epsilon={epsilon}"
    equal(f"{label}: full support", set(coefficients), set(CORNERS))
    zero(f"{label}: origin", sum(coefficients.values(), sp.zeros(2)) - I2)
    for d, decompositions in pairs.items():
        target = I2 if d == (0, 0, 0) else sp.zeros(2)
        zero(f"{label}: U Udag coefficient {d}",
             sum((coefficients[h] * coefficients[j].H for h, j in decompositions),
                 sp.zeros(2)) - target)
        zero(f"{label}: Udag U coefficient {d}",
             sum((coefficients[j].H * coefficients[h] for h, j in decompositions),
                 sp.zeros(2)) - target)
    for h, a in coefficients.items():
        equal(f"{label}: nonzero {h}", a == sp.zeros(2), False)
        for axis, r in enumerate(PAULI):
            gh = tuple(v if i == axis else -v for i, v in enumerate(h))
            zero(f"{label}: covariance axis {axis}, {h}", coefficients[gh] - r * a * r.H)
            commutator = (r * a - a * r).applyfunc(sp.simplify)
            equal(f"{label}: Eq2 axis {axis}, {h}", commutator == sp.zeros(2), False)
        alpha = (1 + epsilon * sp.I * sp.prod(h)) / 4
        zero(f"{label}: vertex determinant {h}", a.det())
        zero(f"{label}: vertex trace {h}", sp.trace(a) - alpha)
        zero(f"{label}: vertex square {h}", a * a - alpha * a)
        equal(f"{label}: nonzero vertex eigenvalue {h}", alpha == 0, False)
    moments = [sum((h[i] * a for h, a in coefficients.items()), sp.zeros(2)) / sp.sqrt(3)
               for i in range(3)]
    for i, moment in enumerate(moments):
        expected = PAULI[i] * (epsilon if i == 1 else 1) / sp.sqrt(3)
        zero(f"{label}: first moment {i}", moment - expected)
        zero(f"{label}: moment Hermitian {i}", moment - moment.H)
        zero(f"{label}: scalar first derivative {i}", sp.trace(moment))
        for j in range(3):
            delta = int(i == j)
            zero(f"{label}: Clifford {i},{j}",
                 moment * moments[j] + moments[j] * moment - 2 * delta * I2 / 3)
            hessian = -sum(h[i] * h[j] * sp.trace(a) for h, a in coefficients.items()) / 6
            zero(f"{label}: scalar Hessian {i},{j}", hessian + sp.Rational(delta, 3))
    z = sp.symbols("z0:3", nonzero=True)
    # z_i=exp(+i k_i/sqrt(3)); our negative Fourier exponent is z_i^(-h_i).
    matrix = sum((sp.prod(z[i] ** (-h[i]) for i in range(3)) * a
                  for h, a in coefficients.items()), sp.zeros(2))
    zero(f"{label}: determinant of full symbol", matrix.det() - 1)
    repo, _ = published_symbol(3, -epsilon, z)
    repo_coefficients = fourier_support(repo, z)
    equal(f"{label}: repository dictionary support", set(repo_coefficients), set(coefficients))
    for h in CORNERS:
        zero(f"{label}: repository dictionary coefficient {h}", repo_coefficients[h] - coefficients[h])
    zero(f"{label}: repository dictionary full symbol", repo - matrix)
    # Conventions cross-check: reversing all Fourier exponents inverts support.
    reflected = matrix.subs({v: 1 / v for v in z}, simultaneous=True)
    zero(f"{label}: Fourier convention inversion",
         reflected - sum((sp.prod(z[i] ** (-h[i]) for i in range(3)) * coefficients[neg(h)]
                          for h in CORNERS), sp.zeros(2)))


def run():
    CHECKS.clear()
    equal("primary source SHA256", digest(SOURCE), SOURCE_HASH)
    pairs = pair_index()
    verify_geometry(pairs)
    for epsilon in (1, -1):
        verify_form(epsilon, pairs)
    lines = ["# Irreducible D2 / P17: exact verification record", "",
             f"Result: PASS — {len(CHECKS)} exact checks; zero tolerance.", "",
             "Evidence: same-author computational checks; independent review pending.",
             "No canonical promotion. Published classification completeness is an input.", "",
             f"Python: {platform.python_version()}; SymPy: {sp.__version__}.", "",
             "Both P17 forms: c_0=1/sqrt(3); every vertex has a nonzero eigenvalue.",
             "The analytic all-n strict-support argument is in the companion report.",
             "The geometry checks verify the pair enumeration used to derive condition (2).", "",
             "## Provenance", "",
             f"- Source SHA256: `{digest(SOURCE)}`",
             f"- Checker SHA256: `{digest(Path(__file__))}`",
             f"- Analytic report SHA256: `{digest(REPORT)}`",
             f"- Imported baseline checker SHA256: `{digest(BASELINE_SCRIPT)}`", "",
             "## Checks", ""]
    lines.extend(f"- {label}" for label in CHECKS)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = run()
    if args.output:
        args.output.write_text(record, encoding="utf-8")
        print(f"PASS: {len(CHECKS)} exact checks; wrote {args.output}")
    else:
        print(record)


if __name__ == "__main__":
    main()
```

### Contexto adjunto: reports/2026-09-23--irreducible-d2-pavia-verification.md
```
# Irreducible D2 / P17: exact verification record

Result: PASS — 519 exact checks; zero tolerance.

Evidence: same-author computational checks; independent review pending.
No canonical promotion. Published classification completeness is an input.

Python: 3.12.3; SymPy: 1.14.0.

Both P17 forms: c_0=1/sqrt(3); every vertex has a nonzero eigenvalue.
The analytic all-n strict-support argument is in the companion report.
The geometry checks verify the pair enumeration used to derive condition (2).

## Provenance

- Source SHA256: `dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81`
- Checker SHA256: `878542f6999351ef6e229e4abe379245312520cdf21df0594825803890f8a27e`
- Analytic report SHA256: `2c2024c8de8b9ac7261bd761f25e34d787481dcb24cdae8bfe649aee6f4cd684`
- Imported baseline checker SHA256: `6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597`

## Checks

- primary source SHA256
- unique opposite difference (-1, -1, -1)
- two-pair tetrahedral difference (-1, -1, -1),(-1, 1, 1)
- two-pair tetrahedral difference (-1, -1, -1),(1, -1, 1)
- two-pair tetrahedral difference (-1, -1, -1),(1, 1, -1)
- unique opposite difference (-1, -1, 1)
- two-pair tetrahedral difference (-1, -1, 1),(-1, 1, -1)
- two-pair tetrahedral difference (-1, -1, 1),(1, -1, -1)
- two-pair tetrahedral difference (-1, -1, 1),(1, 1, 1)
- unique opposite difference (-1, 1, -1)
- two-pair tetrahedral difference (-1, 1, -1),(-1, -1, 1)
- two-pair tetrahedral difference (-1, 1, -1),(1, -1, -1)
- two-pair tetrahedral difference (-1, 1, -1),(1, 1, 1)
- unique opposite difference (-1, 1, 1)
- two-pair tetrahedral difference (-1, 1, 1),(-1, -1, -1)
- two-pair tetrahedral difference (-1, 1, 1),(1, -1, 1)
- two-pair tetrahedral difference (-1, 1, 1),(1, 1, -1)
- unique opposite difference (1, -1, -1)
- two-pair tetrahedral difference (1, -1, -1),(-1, -1, 1)
- two-pair tetrahedral difference (1, -1, -1),(-1, 1, -1)
- two-pair tetrahedral difference (1, -1, -1),(1, 1, 1)
- unique opposite difference (1, -1, 1)
- two-pair tetrahedral difference (1, -1, 1),(-1, -1, -1)
- two-pair tetrahedral difference (1, -1, 1),(-1, 1, 1)
- two-pair tetrahedral difference (1, -1, 1),(1, 1, -1)
- unique opposite difference (1, 1, -1)
- two-pair tetrahedral difference (1, 1, -1),(-1, -1, -1)
- two-pair tetrahedral difference (1, 1, -1),(-1, 1, 1)
- two-pair tetrahedral difference (1, 1, -1),(1, -1, 1)
- unique opposite difference (1, 1, 1)
- two-pair tetrahedral difference (1, 1, 1),(-1, -1, 1)
- two-pair tetrahedral difference (1, 1, 1),(-1, 1, -1)
- two-pair tetrahedral difference (1, 1, 1),(1, -1, -1)
- tetrahedron permutation (0, 1, 2, 3): orthogonal
- tetrahedron permutation (0, 1, 2, 3): image 0
- tetrahedron permutation (0, 1, 2, 3): image 1
- tetrahedron permutation (0, 1, 2, 3): image 2
- tetrahedron permutation (0, 1, 2, 3): image 3
- tetrahedron permutation (0, 1, 3, 2): orthogonal
- tetrahedron permutation (0, 1, 3, 2): image 0
- tetrahedron permutation (0, 1, 3, 2): image 1
- tetrahedron permutation (0, 1, 3, 2): image 2
- tetrahedron permutation (0, 1, 3, 2): image 3
- tetrahedron permutation (0, 2, 1, 3): orthogonal
- tetrahedron permutation (0, 2, 1, 3): image 0
- tetrahedron permutation (0, 2, 1, 3): image 1
- tetrahedron permutation (0, 2, 1, 3): image 2
- tetrahedron permutation (0, 2, 1, 3): image 3
- tetrahedron permutation (0, 2, 3, 1): orthogonal
- tetrahedron permutation (0, 2, 3, 1): image 0
- tetrahedron permutation (0, 2, 3, 1): image 1
- tetrahedron permutation (0, 2, 3, 1): image 2
- tetrahedron permutation (0, 2, 3, 1): image 3
- tetrahedron permutation (0, 3, 1, 2): orthogonal
- tetrahedron permutation (0, 3, 1, 2): image 0
- tetrahedron permutation (0, 3, 1, 2): image 1
- tetrahedron permutation (0, 3, 1, 2): image 2
- tetrahedron permutation (0, 3, 1, 2): image 3
- tetrahedron permutation (0, 3, 2, 1): orthogonal
- tetrahedron permutation (0, 3, 2, 1): image 0
- tetrahedron permutation (0, 3, 2, 1): image 1
- tetrahedron permutation (0, 3, 2, 1): image 2
- tetrahedron permutation (0, 3, 2, 1): image 3
- tetrahedron permutation (1, 0, 2, 3): orthogonal
- tetrahedron permutation (1, 0, 2, 3): image 0
- tetrahedron permutation (1, 0, 2, 3): image 1
- tetrahedron permutation (1, 0, 2, 3): image 2
- tetrahedron permutation (1, 0, 2, 3): image 3
- tetrahedron permutation (1, 0, 3, 2): orthogonal
- tetrahedron permutation (1, 0, 3, 2): image 0
- tetrahedron permutation (1, 0, 3, 2): image 1
- tetrahedron permutation (1, 0, 3, 2): image 2
- tetrahedron permutation (1, 0, 3, 2): image 3
- tetrahedron permutation (1, 2, 0, 3): orthogonal
- tetrahedron permutation (1, 2, 0, 3): image 0
- tetrahedron permutation (1, 2, 0, 3): image 1
- tetrahedron permutation (1, 2, 0, 3): image 2
- tetrahedron permutation (1, 2, 0, 3): image 3
- tetrahedron permutation (1, 2, 3, 0): orthogonal
- tetrahedron permutation (1, 2, 3, 0): image 0
- tetrahedron permutation (1, 2, 3, 0): image 1
- tetrahedron permutation (1, 2, 3, 0): image 2
- tetrahedron permutation (1, 2, 3, 0): image 3
- tetrahedron permutation (1, 3, 0, 2): orthogonal
- tetrahedron permutation (1, 3, 0, 2): image 0
- tetrahedron permutation (1, 3, 0, 2): image 1
- tetrahedron permutation (1, 3, 0, 2): image 2
- tetrahedron permutation (1, 3, 0, 2): image 3
- tetrahedron permutation (1, 3, 2, 0): orthogonal
- tetrahedron permutation (1, 3, 2, 0): image 0
- tetrahedron permutation (1, 3, 2, 0): image 1
- tetrahedron permutation (1, 3, 2, 0): image 2
- tetrahedron permutation (1, 3, 2, 0): image 3
- tetrahedron permutation (2, 0, 1, 3): orthogonal
- tetrahedron permutation (2, 0, 1, 3): image 0
- tetrahedron permutation (2, 0, 1, 3): image 1
- tetrahedron permutation (2, 0, 1, 3): image 2
- tetrahedron permutation (2, 0, 1, 3): image 3
- tetrahedron permutation (2, 0, 3, 1): orthogonal
- tetrahedron permutation (2, 0, 3, 1): image 0
- tetrahedron permutation (2, 0, 3, 1): image 1
- tetrahedron permutation (2, 0, 3, 1): image 2
- tetrahedron permutation (2, 0, 3, 1): image 3
- tetrahedron permutation (2, 1, 0, 3): orthogonal
- tetrahedron permutation (2, 1, 0, 3): image 0
- tetrahedron permutation (2, 1, 0, 3): image 1
- tetrahedron permutation (2, 1, 0, 3): image 2
- tetrahedron permutation (2, 1, 0, 3): image 3
- tetrahedron permutation (2, 1, 3, 0): orthogonal
- tetrahedron permutation (2, 1, 3, 0): image 0
- tetrahedron permutation (2, 1, 3, 0): image 1
- tetrahedron permutation (2, 1, 3, 0): image 2
- tetrahedron permutation (2, 1, 3, 0): image 3
- tetrahedron permutation (2, 3, 0, 1): orthogonal
- tetrahedron permutation (2, 3, 0, 1): image 0
- tetrahedron permutation (2, 3, 0, 1): image 1
- tetrahedron permutation (2, 3, 0, 1): image 2
- tetrahedron permutation (2, 3, 0, 1): image 3
- tetrahedron permutation (2, 3, 1, 0): orthogonal
- tetrahedron permutation (2, 3, 1, 0): image 0
- tetrahedron permutation (2, 3, 1, 0): image 1
- tetrahedron permutation (2, 3, 1, 0): image 2
- tetrahedron permutation (2, 3, 1, 0): image 3
- tetrahedron permutation (3, 0, 1, 2): orthogonal
- tetrahedron permutation (3, 0, 1, 2): image 0
- tetrahedron permutation (3, 0, 1, 2): image 1
- tetrahedron permutation (3, 0, 1, 2): image 2
- tetrahedron permutation (3, 0, 1, 2): image 3
- tetrahedron permutation (3, 0, 2, 1): orthogonal
- tetrahedron permutation (3, 0, 2, 1): image 0
- tetrahedron permutation (3, 0, 2, 1): image 1
- tetrahedron permutation (3, 0, 2, 1): image 2
- tetrahedron permutation (3, 0, 2, 1): image 3
- tetrahedron permutation (3, 1, 0, 2): orthogonal
- tetrahedron permutation (3, 1, 0, 2): image 0
- tetrahedron permutation (3, 1, 0, 2): image 1
- tetrahedron permutation (3, 1, 0, 2): image 2
- tetrahedron permutation (3, 1, 0, 2): image 3
- tetrahedron permutation (3, 1, 2, 0): orthogonal
- tetrahedron permutation (3, 1, 2, 0): image 0
- tetrahedron permutation (3, 1, 2, 0): image 1
- tetrahedron permutation (3, 1, 2, 0): image 2
- tetrahedron permutation (3, 1, 2, 0): image 3
- tetrahedron permutation (3, 2, 0, 1): orthogonal
- tetrahedron permutation (3, 2, 0, 1): image 0
- tetrahedron permutation (3, 2, 0, 1): image 1
- tetrahedron permutation (3, 2, 0, 1): image 2
- tetrahedron permutation (3, 2, 0, 1): image 3
- tetrahedron permutation (3, 2, 1, 0): orthogonal
- tetrahedron permutation (3, 2, 1, 0): image 0
- tetrahedron permutation (3, 2, 1, 0): image 1
- tetrahedron permutation (3, 2, 1, 0): image 2
- tetrahedron permutation (3, 2, 1, 0): image 3
- P17 epsilon=1: full support
- P17 epsilon=1: origin
- P17 epsilon=1: U Udag coefficient (0, 0, 0)
- P17 epsilon=1: Udag U coefficient (0, 0, 0)
- P17 epsilon=1: U Udag coefficient (0, 0, -2)
- P17 epsilon=1: Udag U coefficient (0, 0, -2)
- P17 epsilon=1: U Udag coefficient (0, -2, 0)
- P17 epsilon=1: Udag U coefficient (0, -2, 0)
- P17 epsilon=1: U Udag coefficient (0, -2, -2)
- P17 epsilon=1: Udag U coefficient (0, -2, -2)
- P17 epsilon=1: U Udag coefficient (-2, 0, 0)
- P17 epsilon=1: Udag U coefficient (-2, 0, 0)
- P17 epsilon=1: U Udag coefficient (-2, 0, -2)
- P17 epsilon=1: Udag U coefficient (-2, 0, -2)
- P17 epsilon=1: U Udag coefficient (-2, -2, 0)
- P17 epsilon=1: Udag U coefficient (-2, -2, 0)
- P17 epsilon=1: U Udag coefficient (-2, -2, -2)
- P17 epsilon=1: Udag U coefficient (-2, -2, -2)
- P17 epsilon=1: U Udag coefficient (0, 0, 2)
- P17 epsilon=1: Udag U coefficient (0, 0, 2)
- P17 epsilon=1: U Udag coefficient (0, -2, 2)
- P17 epsilon=1: Udag U coefficient (0, -2, 2)
- P17 epsilon=1: U Udag coefficient (-2, 0, 2)
- P17 epsilon=1: Udag U coefficient (-2, 0, 2)
- P17 epsilon=1: U Udag coefficient (-2, -2, 2)
- P17 epsilon=1: Udag U coefficient (-2, -2, 2)
- P17 epsilon=1: U Udag coefficient (0, 2, 0)
- P17 epsilon=1: Udag U coefficient (0, 2, 0)
- P17 epsilon=1: U Udag coefficient (0, 2, -2)
- P17 epsilon=1: Udag U coefficient (0, 2, -2)
- P17 epsilon=1: U Udag coefficient (-2, 2, 0)
- P17 epsilon=1: Udag U coefficient (-2, 2, 0)
- P17 epsilon=1: U Udag coefficient (-2, 2, -2)
- P17 epsilon=1: Udag U coefficient (-2, 2, -2)
- P17 epsilon=1: U Udag coefficient (0, 2, 2)
- P17 epsilon=1: Udag U coefficient (0, 2, 2)
- P17 epsilon=1: U Udag coefficient (-2, 2, 2)
- P17 epsilon=1: Udag U coefficient (-2, 2, 2)
- P17 epsilon=1: U Udag coefficient (2, 0, 0)
- P17 epsilon=1: Udag U coefficient (2, 0, 0)
- P17 epsilon=1: U Udag coefficient (2, 0, -2)
- P17 epsilon=1: Udag U coefficient (2, 0, -2)
- P17 epsilon=1: U Udag coefficient (2, -2, 0)
- P17 epsilon=1: Udag U coefficient (2, -2, 0)
- P17 epsilon=1: U Udag coefficient (2, -2, -2)
- P17 epsilon=1: Udag U coefficient (2, -2, -2)
- P17 epsilon=1: U Udag coefficient (2, 0, 2)
- P17 epsilon=1: Udag U coefficient (2, 0, 2)
- P17 epsilon=1: U Udag coefficient (2, -2, 2)
- P17 epsilon=1: Udag U coefficient (2, -2, 2)
- P17 epsilon=1: U Udag coefficient (2, 2, 0)
- P17 epsilon=1: Udag U coefficient (2, 2, 0)
- P17 epsilon=1: U Udag coefficient (2, 2, -2)
- P17 epsilon=1: Udag U coefficient (2, 2, -2)
- P17 epsilon=1: U Udag coefficient (2, 2, 2)
- P17 epsilon=1: Udag U coefficient (2, 2, 2)
- P17 epsilon=1: nonzero (1, 1, 1)
- P17 epsilon=1: covariance axis 0, (1, 1, 1)
- P17 epsilon=1: Eq2 axis 0, (1, 1, 1)
- P17 epsilon=1: covariance axis 1, (1, 1, 1)
- P17 epsilon=1: Eq2 axis 1, (1, 1, 1)
- P17 epsilon=1: covariance axis 2, (1, 1, 1)
- P17 epsilon=1: Eq2 axis 2, (1, 1, 1)
- P17 epsilon=1: vertex determinant (1, 1, 1)
- P17 epsilon=1: vertex trace (1, 1, 1)
- P17 epsilon=1: vertex square (1, 1, 1)
- P17 epsilon=1: nonzero vertex eigenvalue (1, 1, 1)
- P17 epsilon=1: nonzero (1, -1, -1)
- P17 epsilon=1: covariance axis 0, (1, -1, -1)
- P17 epsilon=1: Eq2 axis 0, (1, -1, -1)
- P17 epsilon=1: covariance axis 1, (1, -1, -1)
- P17 epsilon=1: Eq2 axis 1, (1, -1, -1)
- P17 epsilon=1: covariance axis 2, (1, -1, -1)
- P17 epsilon=1: Eq2 axis 2, (1, -1, -1)
- P17 epsilon=1: vertex determinant (1, -1, -1)
- P17 epsilon=1: vertex trace (1, -1, -1)
- P17 epsilon=1: vertex square (1, -1, -1)
- P17 epsilon=1: nonzero vertex eigenvalue (1, -1, -1)
- P17 epsilon=1: nonzero (-1, 1, -1)
- P17 epsilon=1: covariance axis 0, (-1, 1, -1)
- P17 epsilon=1: Eq2 axis 0, (-1, 1, -1)
- P17 epsilon=1: covariance axis 1, (-1, 1, -1)
- P17 epsilon=1: Eq2 axis 1, (-1, 1, -1)
- P17 epsilon=1: covariance axis 2, (-1, 1, -1)
- P17 epsilon=1: Eq2 axis 2, (-1, 1, -1)
- P17 epsilon=1: vertex determinant (-1, 1, -1)
- P17 epsilon=1: vertex trace (-1, 1, -1)
- P17 epsilon=1: vertex square (-1, 1, -1)
- P17 epsilon=1: nonzero vertex eigenvalue (-1, 1, -1)
- P17 epsilon=1: nonzero (-1, -1, 1)
- P17 epsilon=1: covariance axis 0, (-1, -1, 1)
- P17 epsilon=1: Eq2 axis 0, (-1, -1, 1)
- P17 epsilon=1: covariance axis 1, (-1, -1, 1)
- P17 epsilon=1: Eq2 axis 1, (-1, -1, 1)
- P17 epsilon=1: covariance axis 2, (-1, -1, 1)
- P17 epsilon=1: Eq2 axis 2, (-1, -1, 1)
- P17 epsilon=1: vertex determinant (-1, -1, 1)
- P17 epsilon=1: vertex trace (-1, -1, 1)
- P17 epsilon=1: vertex square (-1, -1, 1)
- P17 epsilon=1: nonzero vertex eigenvalue (-1, -1, 1)
- P17 epsilon=1: nonzero (-1, -1, -1)
- P17 epsilon=1: covariance axis 0, (-1, -1, -1)
- P17 epsilon=1: Eq2 axis 0, (-1, -1, -1)
- P17 epsilon=1: covariance axis 1, (-1, -1, -1)
- P17 epsilon=1: Eq2 axis 1, (-1, -1, -1)
- P17 epsilon=1: covariance axis 2, (-1, -1, -1)
- P17 epsilon=1: Eq2 axis 2, (-1, -1, -1)
- P17 epsilon=1: vertex determinant (-1, -1, -1)
- P17 epsilon=1: vertex trace (-1, -1, -1)
- P17 epsilon=1: vertex square (-1, -1, -1)
- P17 epsilon=1: nonzero vertex eigenvalue (-1, -1, -1)
- P17 epsilon=1: nonzero (-1, 1, 1)
- P17 epsilon=1: covariance axis 0, (-1, 1, 1)
- P17 epsilon=1: Eq2 axis 0, (-1, 1, 1)
- P17 epsilon=1: covariance axis 1, (-1, 1, 1)
- P17 epsilon=1: Eq2 axis 1, (-1, 1, 1)
- P17 epsilon=1: covariance axis 2, (-1, 1, 1)
- P17 epsilon=1: Eq2 axis 2, (-1, 1, 1)
- P17 epsilon=1: vertex determinant (-1, 1, 1)
- P17 epsilon=1: vertex trace (-1, 1, 1)
- P17 epsilon=1: vertex square (-1, 1, 1)
- P17 epsilon=1: nonzero vertex eigenvalue (-1, 1, 1)
- P17 epsilon=1: nonzero (1, -1, 1)
- P17 epsilon=1: covariance axis 0, (1, -1, 1)
- P17 epsilon=1: Eq2 axis 0, (1, -1, 1)
- P17 epsilon=1: covariance axis 1, (1, -1, 1)
- P17 epsilon=1: Eq2 axis 1, (1, -1, 1)
- P17 epsilon=1: covariance axis 2, (1, -1, 1)
- P17 epsilon=1: Eq2 axis 2, (1, -1, 1)
- P17 epsilon=1: vertex determinant (1, -1, 1)
- P17 epsilon=1: vertex trace (1, -1, 1)
- P17 epsilon=1: vertex square (1, -1, 1)
- P17 epsilon=1: nonzero vertex eigenvalue (1, -1, 1)
- P17 epsilon=1: nonzero (1, 1, -1)
- P17 epsilon=1: covariance axis 0, (1, 1, -1)
- P17 epsilon=1: Eq2 axis 0, (1, 1, -1)
- P17 epsilon=1: covariance axis 1, (1, 1, -1)
- P17 epsilon=1: Eq2 axis 1, (1, 1, -1)
- P17 epsilon=1: covariance axis 2, (1, 1, -1)
- P17 epsilon=1: Eq2 axis 2, (1, 1, -1)
- P17 epsilon=1: vertex determinant (1, 1, -1)
- P17 epsilon=1: vertex trace (1, 1, -1)
- P17 epsilon=1: vertex square (1, 1, -1)
- P17 epsilon=1: nonzero vertex eigenvalue (1, 1, -1)
- P17 epsilon=1: first moment 0
- P17 epsilon=1: moment Hermitian 0
- P17 epsilon=1: scalar first derivative 0
- P17 epsilon=1: Clifford 0,0
- P17 epsilon=1: scalar Hessian 0,0
- P17 epsilon=1: Clifford 0,1
- P17 epsilon=1: scalar Hessian 0,1
- P17 epsilon=1: Clifford 0,2
- P17 epsilon=1: scalar Hessian 0,2
- P17 epsilon=1: first moment 1
- P17 epsilon=1: moment Hermitian 1
- P17 epsilon=1: scalar first derivative 1
- P17 epsilon=1: Clifford 1,0
- P17 epsilon=1: scalar Hessian 1,0
- P17 epsilon=1: Clifford 1,1
- P17 epsilon=1: scalar Hessian 1,1
- P17 epsilon=1: Clifford 1,2
- P17 epsilon=1: scalar Hessian 1,2
- P17 epsilon=1: first moment 2
- P17 epsilon=1: moment Hermitian 2
- P17 epsilon=1: scalar first derivative 2
- P17 epsilon=1: Clifford 2,0
- P17 epsilon=1: scalar Hessian 2,0
- P17 epsilon=1: Clifford 2,1
- P17 epsilon=1: scalar Hessian 2,1
- P17 epsilon=1: Clifford 2,2
- P17 epsilon=1: scalar Hessian 2,2
- P17 epsilon=1: determinant of full symbol
- P17 epsilon=1: repository dictionary support
- P17 epsilon=1: repository dictionary coefficient (-1, -1, -1)
- P17 epsilon=1: repository dictionary coefficient (-1, -1, 1)
- P17 epsilon=1: repository dictionary coefficient (-1, 1, -1)
- P17 epsilon=1: repository dictionary coefficient (-1, 1, 1)
- P17 epsilon=1: repository dictionary coefficient (1, -1, -1)
- P17 epsilon=1: repository dictionary coefficient (1, -1, 1)
- P17 epsilon=1: repository dictionary coefficient (1, 1, -1)
- P17 epsilon=1: repository dictionary coefficient (1, 1, 1)
- P17 epsilon=1: repository dictionary full symbol
- P17 epsilon=1: Fourier convention inversion
- P17 epsilon=-1: full support
- P17 epsilon=-1: origin
- P17 epsilon=-1: U Udag coefficient (0, 0, 0)
- P17 epsilon=-1: Udag U coefficient (0, 0, 0)
- P17 epsilon=-1: U Udag coefficient (0, 0, -2)
- P17 epsilon=-1: Udag U coefficient (0, 0, -2)
- P17 epsilon=-1: U Udag coefficient (0, -2, 0)
- P17 epsilon=-1: Udag U coefficient (0, -2, 0)
- P17 epsilon=-1: U Udag coefficient (0, -2, -2)
- P17 epsilon=-1: Udag U coefficient (0, -2, -2)
- P17 epsilon=-1: U Udag coefficient (-2, 0, 0)
- P17 epsilon=-1: Udag U coefficient (-2, 0, 0)
- P17 epsilon=-1: U Udag coefficient (-2, 0, -2)
- P17 epsilon=-1: Udag U coefficient (-2, 0, -2)
- P17 epsilon=-1: U Udag coefficient (-2, -2, 0)
- P17 epsilon=-1: Udag U coefficient (-2, -2, 0)
- P17 epsilon=-1: U Udag coefficient (-2, -2, -2)
- P17 epsilon=-1: Udag U coefficient (-2, -2, -2)
- P17 epsilon=-1: U Udag coefficient (0, 0, 2)
- P17 epsilon=-1: Udag U coefficient (0, 0, 2)
- P17 epsilon=-1: U Udag coefficient (0, -2, 2)
- P17 epsilon=-1: Udag U coefficient (0, -2, 2)
- P17 epsilon=-1: U Udag coefficient (-2, 0, 2)
- P17 epsilon=-1: Udag U coefficient (-2, 0, 2)
- P17 epsilon=-1: U Udag coefficient (-2, -2, 2)
- P17 epsilon=-1: Udag U coefficient (-2, -2, 2)
- P17 epsilon=-1: U Udag coefficient (0, 2, 0)
- P17 epsilon=-1: Udag U coefficient (0, 2, 0)
- P17 epsilon=-1: U Udag coefficient (0, 2, -2)
- P17 epsilon=-1: Udag U coefficient (0, 2, -2)
- P17 epsilon=-1: U Udag coefficient (-2, 2, 0)
- P17 epsilon=-1: Udag U coefficient (-2, 2, 0)
- P17 epsilon=-1: U Udag coefficient (-2, 2, -2)
- P17 epsilon=-1: Udag U coefficient (-2, 2, -2)
- P17 epsilon=-1: U Udag coefficient (0, 2, 2)
- P17 epsilon=-1: Udag U coefficient (0, 2, 2)
- P17 epsilon=-1: U Udag coefficient (-2, 2, 2)
- P17 epsilon=-1: Udag U coefficient (-2, 2, 2)
- P17 epsilon=-1: U Udag coefficient (2, 0, 0)
- P17 epsilon=-1: Udag U coefficient (2, 0, 0)
- P17 epsilon=-1: U Udag coefficient (2, 0, -2)
- P17 epsilon=-1: Udag U coefficient (2, 0, -2)
- P17 epsilon=-1: U Udag coefficient (2, -2, 0)
- P17 epsilon=-1: Udag U coefficient (2, -2, 0)
- P17 epsilon=-1: U Udag coefficient (2, -2, -2)
- P17 epsilon=-1: Udag U coefficient (2, -2, -2)
- P17 epsilon=-1: U Udag coefficient (2, 0, 2)
- P17 epsilon=-1: Udag U coefficient (2, 0, 2)
- P17 epsilon=-1: U Udag coefficient (2, -2, 2)
- P17 epsilon=-1: Udag U coefficient (2, -2, 2)
- P17 epsilon=-1: U Udag coefficient (2, 2, 0)
- P17 epsilon=-1: Udag U coefficient (2, 2, 0)
- P17 epsilon=-1: U Udag coefficient (2, 2, -2)
- P17 epsilon=-1: Udag U coefficient (2, 2, -2)
- P17 epsilon=-1: U Udag coefficient (2, 2, 2)
- P17 epsilon=-1: Udag U coefficient (2, 2, 2)
- P17 epsilon=-1: nonzero (1, 1, 1)
- P17 epsilon=-1: covariance axis 0, (1, 1, 1)
- P17 epsilon=-1: Eq2 axis 0, (1, 1, 1)
- P17 epsilon=-1: covariance axis 1, (1, 1, 1)
- P17 epsilon=-1: Eq2 axis 1, (1, 1, 1)
- P17 epsilon=-1: covariance axis 2, (1, 1, 1)
- P17 epsilon=-1: Eq2 axis 2, (1, 1, 1)
- P17 epsilon=-1: vertex determinant (1, 1, 1)
- P17 epsilon=-1: vertex trace (1, 1, 1)
- P17 epsilon=-1: vertex square (1, 1, 1)
- P17 epsilon=-1: nonzero vertex eigenvalue (1, 1, 1)
- P17 epsilon=-1: nonzero (1, -1, -1)
- P17 epsilon=-1: covariance axis 0, (1, -1, -1)
- P17 epsilon=-1: Eq2 axis 0, (1, -1, -1)
- P17 epsilon=-1: covariance axis 1, (1, -1, -1)
- P17 epsilon=-1: Eq2 axis 1, (1, -1, -1)
- P17 epsilon=-1: covariance axis 2, (1, -1, -1)
- P17 epsilon=-1: Eq2 axis 2, (1, -1, -1)
- P17 epsilon=-1: vertex determinant (1, -1, -1)
- P17 epsilon=-1: vertex trace (1, -1, -1)
- P17 epsilon=-1: vertex square (1, -1, -1)
- P17 epsilon=-1: nonzero vertex eigenvalue (1, -1, -1)
- P17 epsilon=-1: nonzero (-1, 1, -1)
- P17 epsilon=-1: covariance axis 0, (-1, 1, -1)
- P17 epsilon=-1: Eq2 axis 0, (-1, 1, -1)
- P17 epsilon=-1: covariance axis 1, (-1, 1, -1)
- P17 epsilon=-1: Eq2 axis 1, (-1, 1, -1)
- P17 epsilon=-1: covariance axis 2, (-1, 1, -1)
- P17 epsilon=-1: Eq2 axis 2, (-1, 1, -1)
- P17 epsilon=-1: vertex determinant (-1, 1, -1)
- P17 epsilon=-1: vertex trace (-1, 1, -1)
- P17 epsilon=-1: vertex square (-1, 1, -1)
- P17 epsilon=-1: nonzero vertex eigenvalue (-1, 1, -1)
- P17 epsilon=-1: nonzero (-1, -1, 1)
- P17 epsilon=-1: covariance axis 0, (-1, -1, 1)
- P17 epsilon=-1: Eq2 axis 0, (-1, -1, 1)
- P17 epsilon=-1: covariance axis 1, (-1, -1, 1)
- P17 epsilon=-1: Eq2 axis 1, (-1, -1, 1)
- P17 epsilon=-1: covariance axis 2, (-1, -1, 1)
- P17 epsilon=-1: Eq2 axis 2, (-1, -1, 1)
- P17 epsilon=-1: vertex determinant (-1, -1, 1)
- P17 epsilon=-1: vertex trace (-1, -1, 1)
- P17 epsilon=-1: vertex square (-1, -1, 1)
- P17 epsilon=-1: nonzero vertex eigenvalue (-1, -1, 1)
- P17 epsilon=-1: nonzero (-1, -1, -1)
- P17 epsilon=-1: covariance axis 0, (-1, -1, -1)
- P17 epsilon=-1: Eq2 axis 0, (-1, -1, -1)
- P17 epsilon=-1: covariance axis 1, (-1, -1, -1)
- P17 epsilon=-1: Eq2 axis 1, (-1, -1, -1)
- P17 epsilon=-1: covariance axis 2, (-1, -1, -1)
- P17 epsilon=-1: Eq2 axis 2, (-1, -1, -1)
- P17 epsilon=-1: vertex determinant (-1, -1, -1)
- P17 epsilon=-1: vertex trace (-1, -1, -1)
- P17 epsilon=-1: vertex square (-1, -1, -1)
- P17 epsilon=-1: nonzero vertex eigenvalue (-1, -1, -1)
- P17 epsilon=-1: nonzero (-1, 1, 1)
- P17 epsilon=-1: covariance axis 0, (-1, 1, 1)
- P17 epsilon=-1: Eq2 axis 0, (-1, 1, 1)
- P17 epsilon=-1: covariance axis 1, (-1, 1, 1)
- P17 epsilon=-1: Eq2 axis 1, (-1, 1, 1)
- P17 epsilon=-1: covariance axis 2, (-1, 1, 1)
- P17 epsilon=-1: Eq2 axis 2, (-1, 1, 1)
- P17 epsilon=-1: vertex determinant (-1, 1, 1)
- P17 epsilon=-1: vertex trace (-1, 1, 1)
- P17 epsilon=-1: vertex square (-1, 1, 1)
- P17 epsilon=-1: nonzero vertex eigenvalue (-1, 1, 1)
- P17 epsilon=-1: nonzero (1, -1, 1)
- P17 epsilon=-1: covariance axis 0, (1, -1, 1)
- P17 epsilon=-1: Eq2 axis 0, (1, -1, 1)
- P17 epsilon=-1: covariance axis 1, (1, -1, 1)
- P17 epsilon=-1: Eq2 axis 1, (1, -1, 1)
- P17 epsilon=-1: covariance axis 2, (1, -1, 1)
- P17 epsilon=-1: Eq2 axis 2, (1, -1, 1)
- P17 epsilon=-1: vertex determinant (1, -1, 1)
- P17 epsilon=-1: vertex trace (1, -1, 1)
- P17 epsilon=-1: vertex square (1, -1, 1)
- P17 epsilon=-1: nonzero vertex eigenvalue (1, -1, 1)
- P17 epsilon=-1: nonzero (1, 1, -1)
- P17 epsilon=-1: covariance axis 0, (1, 1, -1)
- P17 epsilon=-1: Eq2 axis 0, (1, 1, -1)
- P17 epsilon=-1: covariance axis 1, (1, 1, -1)
- P17 epsilon=-1: Eq2 axis 1, (1, 1, -1)
- P17 epsilon=-1: covariance axis 2, (1, 1, -1)
- P17 epsilon=-1: Eq2 axis 2, (1, 1, -1)
- P17 epsilon=-1: vertex determinant (1, 1, -1)
- P17 epsilon=-1: vertex trace (1, 1, -1)
- P17 epsilon=-1: vertex square (1, 1, -1)
- P17 epsilon=-1: nonzero vertex eigenvalue (1, 1, -1)
- P17 epsilon=-1: first moment 0
- P17 epsilon=-1: moment Hermitian 0
- P17 epsilon=-1: scalar first derivative 0
- P17 epsilon=-1: Clifford 0,0
- P17 epsilon=-1: scalar Hessian 0,0
- P17 epsilon=-1: Clifford 0,1
- P17 epsilon=-1: scalar Hessian 0,1
- P17 epsilon=-1: Clifford 0,2
- P17 epsilon=-1: scalar Hessian 0,2
- P17 epsilon=-1: first moment 1
- P17 epsilon=-1: moment Hermitian 1
- P17 epsilon=-1: scalar first derivative 1
- P17 epsilon=-1: Clifford 1,0
- P17 epsilon=-1: scalar Hessian 1,0
- P17 epsilon=-1: Clifford 1,1
- P17 epsilon=-1: scalar Hessian 1,1
- P17 epsilon=-1: Clifford 1,2
- P17 epsilon=-1: scalar Hessian 1,2
- P17 epsilon=-1: first moment 2
- P17 epsilon=-1: moment Hermitian 2
- P17 epsilon=-1: scalar first derivative 2
- P17 epsilon=-1: Clifford 2,0
- P17 epsilon=-1: scalar Hessian 2,0
- P17 epsilon=-1: Clifford 2,1
- P17 epsilon=-1: scalar Hessian 2,1
- P17 epsilon=-1: Clifford 2,2
- P17 epsilon=-1: scalar Hessian 2,2
- P17 epsilon=-1: determinant of full symbol
- P17 epsilon=-1: repository dictionary support
- P17 epsilon=-1: repository dictionary coefficient (-1, -1, -1)
- P17 epsilon=-1: repository dictionary coefficient (-1, -1, 1)
- P17 epsilon=-1: repository dictionary coefficient (-1, 1, -1)
- P17 epsilon=-1: repository dictionary coefficient (-1, 1, 1)
- P17 epsilon=-1: repository dictionary coefficient (1, -1, -1)
- P17 epsilon=-1: repository dictionary coefficient (1, -1, 1)
- P17 epsilon=-1: repository dictionary coefficient (1, 1, -1)
- P17 epsilon=-1: repository dictionary coefficient (1, 1, 1)
- P17 epsilon=-1: repository dictionary full symbol
- P17 epsilon=-1: Fourier convention inversion
```

### Contexto adjunto: debates/2026-09-23--irreducible-d2-p17-source.txt
```
                                                                   Isotropic quantum walks on lattices and the Weyl equation

                                                                           Giacomo Mauro D’Ariano,∗ Marco Erba,† and Paolo Perinotti‡
                                                                          Università degli Studi di Pavia, Dipartimento di Fisica, QUIT Group,
                                                                         and INFN Gruppo IV, Sezione di Pavia, via Bassi 6, 27100 Pavia, Italy

                                                             We present a thorough classification of the isotropic quantum walks on lattices of dimension
                                                          d = 1, 2, 3 with a coin system of dimension s = 2. For d = 3 there exist two isotropic walks, namely
                                                          the Weyl quantum walks presented in Ref. [1], resulting in the derivation of the Weyl equation from
                                                          informational principles. The present analysis, via a crucial use of isotropy, is significantly shorter
                                                          and avoids a superfluous technical assumption, making the result completely general.

                                                          PACS numbers: 03.67.-a, 03.67.Ac, 03.65.Ta
                                                          Keywords: Quantum walks, Cayley Graphs, Weyl Equation, Isotropy
arXiv:1708.00826v2 [quant-ph] 30 Nov 2017




                                                              I.    INTRODUCTION                               sphere of nearest neighbours. On the other hand, most of
                                                                                                               the derivation did not use the isotropy principle. In the
                                               Recently the possibility of implementing actual quan-           present paper, on the contrary, we exploit the isotropy
                                            tum simulations of quantum fields [2–5] has been ac-               principle from the very beginning of the derivation, thus
                                            companied by novel approaches to foundations of the                avoiding the above assumption and making the classifi-
                                            theory [6–9], including its derivation from informational          cation of the isotropic QWs on Zd completely general.
                                            principles [1, 10] and the recovery of its Lorentz covari-         In the present paper the derivation of the Weyl QWs is
                                            ance [11]. This has provided a progress in the research            included in a complete classification of isotropic QWs on
                                            based on the idea originally proposed by Feynman [12]              lattices of dimension d = 1, 2, 3 with a coin system of
                                            of recovering physics as pure quantum information pro-             dimension s = 2. The result exploits the isotropy no-
                                            cessing. Deriving quantum field theory from just denu-             tion of Ref. [1], which is extended in this paper in order
                                            merable quantum systems provides an emergent notion                to account for groups with generators of different orders.
                                            of space-time, with no prior background. This suggests             We will introduce a technique to construct the Cayley
                                            that the approach may be promising for a future devel-             graphs of a given group G supporting an isotropic QW.
                                            opment of quantum theories of gravity.                             Remarkably, the Cayley graph is unique for each dimen-
                                               The mathematical formalisation of the discrete quan-            sion d = 1, 2, 3.
                                            tum algorithm running a quantum field dynamics is pro-                The manuscript is organized as follows. In Sec. II we
                                            vided by the notion of quantum cellular automaton [13–             review the notion of Cayley graph of a group G, and
                                            15]. A quantum cellular automaton is a unitary homoge-             define QWs on Cayley graphs, introducing the definition
                                            neous evolution of the algebra of local observables that           of isotropy and its main properties. In Sec. III we review
                                            preserves locality. When the automaton is linear in the            the theory of QWs on free Abelian groups. In Sec. IV we
                                            local algebra generators, the cellular automaton is usu-           select the possible Cayley graphs according to a necessary
                                            ally referred to as a quantum walk (QW) [16–18], and               condition for a QW to be isotropic. In Sec. V we prove
                                            is suited for the description of the free field theory for a       a second necessary condition for isotropy that is used in
                                            fixed number of particles.                                         the appendix to refine the selection of Cayley graphs, and
                                               A quantum walk on a graph represents a coherent                 we solve the unitarity condition on the selected Cayley
                                            counterpart of a classical random walk on the same                 graphs for d = 1, 2, 3, finding the two Weyl QWs. Sec. VI
                                            graph. In the derivation of Ref. [1] it was proved that,           closes the paper with some concluding remarks, whereas
                                            if one assumes homogeneity of the evolution, the graph             in Appendix A we report technical proofs and details.
                                            must be the Cayley graph of a group G. When the graph
                                            corresponds to a free Abelian group G ∼ = Zd , one finds the
                                                                                                                  II.   ISOTROPIC QWS ON CAYLEY GRAPHS
                                            two Weyl QWs (one for the left- and one for the right-
                                            handed mode), recovering the Weyl equation in d + 1
                                            dimensions for d = 1, 2, 3. An alternative derivation of              We now define the QW on a Cayley graph Γ(G, S+ )
                                            the Weyl QWs for d = 3 on the BCC lattice has been re-             of a group G, with generating set S+ . A generating set
                                            cently presented in Ref. [19]. In Ref. [1] the derivation of       S+ ⊆ G is a set of elements of G such that all the elements
                                            the Weyl QWs exploited the technical assumption that               of the group can be expressed as words of elements of S+
                                            there is a quasi-isometry [20] of the Cayley graph in a Eu-        along with their inverses. The Cayley graph is a coloured
                                            clidean manifold such that no vertex can lie within the            directed graph with the elements of G as vertices and
                                                                                                               the elements of S+ as edges: a colour is associated to
                                                                                                               each generator h ∈ S+ , and two vertices g, g 0 ∈ G are
                                            ∗ dariano@unipv.it                                                 connected by the coloured edge h ∈ S+ if g 0 = gh, with
                                            † marco.erba01@ateneopv.it
                                                                                                               the arrow directed from g to g 0 . In the following we will
                                            ‡ paolo.perinotti@unipv.it
                                                                                                               take |S+ | < ∞, namely the group G is finitely generated.
                                                                                                                                      2

The Cayley graph of a group can be defined by giving                The previous definition guarantees that the group of
a presentation, namely choosing a set of generators (an          local changes of basis representing the isotropy group L—
alphabet) and a set of relators, i.e a set of words which        which is a group of automorphisms of the graph—acts
are equal to the identity of G. This completely specifies        just as a permutation of the transition matrices, implying
a unique group G. The cardinality of the group G can be          that all the directions are dynamically equivalent.
finite or infinite, depending on its relators, however the          To satisfy homogeneity, one has to demand also the
most interesting case in the present context is that of a        following condition [23]:
finitely presented infinite group.
   Let {|gi}g∈G be an orthonormal basis for `2 (G). The                  [Ul , Ah ] 6= 0 ∀h ∈ S+ , ∀l ∈ L : l(h) 6= h.               (2)
right-regular representation T of G is defined as
                                                                 Indeed, two transition matrices associated to different
                     Tg |g 0 i := |g 0 g −1 i.            (1)    generators must be distinct. In particular, this implies
                                                                 that if L does not contain nontrivial elements stabilizing
A QW on the Cayley graph Γ(G, S+ ) of the group G is a
                                                                 all the h ∈ S, then the representation U must be faithful
unitary operator A on `2 (G) ⊗ Cs , with 1 ≤ s < ∞, that
                                                                 (otherwise it would contain at least one nontrivial ele-
can be written as
                        X                                        ment represented as Is ).
                   A=       Th ⊗ Ah ,
                           h∈S
                                                                 Proposition 1. The automorphisms of the Cayley graph
                                                                 Γ(G, S+ ) are also automorphisms of G.
                               −1
where S = S+ ∪ S− , S− = S+        is the set of inverses of
S+ , and {Ah }h∈S ⊆ Ms (C) are the so-called transition          Proof. Consider the action of arbitrary elements l ∈ L on
matrices of the QW.                                              the graph vertices. We have
   It is worth mentioning that also other constructions of
QWs have been given in the literature, for example QWs                    λ(h) = l(h) = l(eh) = eλ(h),              ∀h ∈ S+ ,
such that the coin system is generated by the set of edges
                                                                 and since l(gh) = l(g)λ(h) ∀g ∈ G, then l(e) = e. The
of the underlying graph (see e.g. Ref [21], and Ref. [22]
                                                                 same holds ∀h ∈ S− . Moreover
for an overview).
   Generally we will consider also self-transitions, corre-
                                                                         l(hh0 ) = l(h)λ(h0 ) ≡ l(h)l(h0 ) ∀h, h0 ∈ S.
sponding to the inclusion of the identity e ∈ G in the
generating set which is then given by S ≡ S+ ∪ S− ∪ {e}.         Iterating, in general we obtain
In the following, for each group G considered, we will as-
sume Ah 6= 0 for all h ∈ S+ ∪ S− , whereas in general we            l(h1 · · · hp ) = l(h1 ) · · · l(hp ),   ∀h1 , . . . , hp ∈ S,   (3)
                                                     n
allow for the case Ae = 0. We also denote by S+          ⊆ S+
the set of generators of order n ≥ 2, i.e. n is the smallest     and, being S a set of generators for G, this amounts to
integer such that hn = e. Notice that the most common
case is that of n = +∞.                                                          l(gg 0 ) = l(g)l(g 0 ) ∀g, g 0 ∈ G.
   For the purpose of introducing the concept of isotropic
QWs, we remind that a graph automorphism is defined              Accordingly, L is a group automorphism of G. 
as a bijective map of the vertices that preserves the set of
edges. For a Cayley graph this means that the automor-             The isotropy conditions corresponds to the covariance
phism l is such that if g 0 = gh, then l(g 0 ) = l(g)h0 , with
                                                                                          Tl(h) ⊗ Ul Ah Ul† ∀l ∈ L. (4)
                                                                        X              X
g, g 0 ∈ G and h, h0 ∈ S+ . Then, an automorphism of the           A=       Th ⊗ Ah =
Cayley graph can be expressed as a permutation λ of the                  h∈S                 h∈S
set of colours S+ , where for every g ∈ G and h ∈ S+ one
has l(gh) = l(g)λ(h) for some permutation λ of S+ . Let          The covariance condition (4) and the transitivity of Λ on
                                                                         n
us denote by Λ a group of permutations of the elements           each S+    imply, by linear independence of the Th , that
                                                                          n
of S+ .                                                          every S+    is invariant under some subgroup Ln ≤ L. In
                                                                              n                                          (n)
Definition 1 (Isotropic QW). A QW on Γ(G, S+ ) is                fact, any S+    is the orbit of an arbitrary generator h1 ∈
                                                                   n                                     (n)
called isotropic with respect to S+ if there exists a group      S+  under Ln , denoted with OLn (h1 ).
L of automorphisms of Γ(G, S+ ) that can be expressed
as a permutation of the colours S+ , such that the evolu-        Proposition 2. The isotropy group L is a finite subgroup
tion operator of the QW is L-covariant, i.e. there exists        of Aut(G).
a projective unitary representation U over Cs of L such
                                                                 Proof. By Proposition 1 the isotropy group L is a group
that
                                                                 of automorphisms of G. By Eq. (3) L ∼  = Λ, hence L is
           Aλ(h) = Ul Ah Ul†       ∀l ∈ L, ∀h ∈ S+ ,             finite. 

where λ ∈ Λ, and such that the action of Λ is transitive         Corollary 1. Each subgroup Ln ≤ L is isomorphic to a
                n                                                                                                 n
on each subset S+ .                                              finite permutation group acting transitively on S+ .
                                                                                                                                  3

Corollary 2. If all generators have the same order, L         The unitary operator of the QW is given by
is isomorphic to a finite permutation group acting tran-                       XX
sitively on S+ .                                                          A=            |n + hihn| ⊗ Ah .                       (5)
                                                                                    n∈G h∈S
   By Eq. (4) one can always choose the projective uni-
tary representation U with unit determinant, namely           One has [A, Th ⊗ Is ] = 0. The unitary irreps are one-
Ul ∈ SU(s) ∀l ∈ L. Notice that, by definition of isotropy,    dimensional, and are classified by the joint eigenvectors
         n                                                    of Th
either S+   does not contain the inverse of any of its ele-
ments or it coincides with the whole set S n := S+ n    n
                                                     ∪ S− .
   In the following we will consider the isotropic QWs on                           Thi |ki =: e−ik·hi |ki,
Γ(G, S+ ) with s = 2 and G ∼   = Zd with d = 1, 2, 3. For
                                                              where
d = 3 we discover that there are two QWs (modulo dis-                                                            Z
crete symmetries) that for large-scales give the two Weyl             1 X ik·n                         1
                                                              |ki := p         e |ni,           |ni = p               dke−ik·n |ki.
equations, one for left- and one for right-handed mode.                |B| n∈G                          |B|       B
In Ref. [1] it is shown that, coupling two Weyl QWs in
the only possible way consistent with the above require-      Notice that
ments (specifically locality), the resulting QW is unique
                                                                                   1 X i(k−k0 )·n
(modulo discrete symmetries) and describes exactly the                hk|k0 i =       e           = δ2π (k − k0 ).
Dirac equation for large scales.                                                  |B|
                                                                                      n∈G

                                                              Translation invariance of the QW in Eq. (5) then implies
III.    QUANTUM WALKS ON CAYLEY GRAPHS                        the following form for the unitary evolution operator
                  OF Zd                                                             Z
                                                                               A=      dk|kihk| ⊗ Ak ,
   Since we are considering Abelian groups, we will de-                                  B
note the group elements as usual with the boldfaced vec-      where the the matrix
tor notation as n ∈ G, and the generators as h ∈ S.                                          X
Moreover, we will use the additive notation for the group                            Ak =          eih·k Ah                     (6)
composition, and 0 for the identity element. The space                                       h∈S
`2 (G) will be the span of {|ni}n∈G and the generators h
are represented by the operators                              is unitary for every k. Notice that Ak is a matrix poly-
                                                              nomial in eih·k . The unitarity conditions on Ak for all
                                                              k ∈ B then read
                         X
                   Th :=     |n + hihn|.
                                                                            Ah A†h =
                                                                        X            X †
                               n∈G
                                                                                        Ah Ah = Is ,               (7)
                                                                        h∈S             h∈S
We now treat the elements of G as vectors in Rd . Gen-
                                                                                    Ah A†h0 =               A†h0 Ah = 0.
                                                                            X                      X
erally the elements of S are linearly dependent. We in-                                                                         (8)
troduce all the sets Dn ⊆ S+ of linearly independent                    h−h0 =h00               h−h0 =h00
elements
                                                              The previous equations are a set of necessary and suffi-
                     Dn := {hi1 , . . . , hid },              cient conditions for the unitarity of the time evolution,
                                                              since they can be derived just imposing that the matrix
where n labels the specific subset. For every Dn we con-      Ak is unitary. As explained in Sec. II, the requirement of
struct the dual set D̃n defined by                            isotropy for the QW needs the existence of a group that
                                                              acts transitively over the generator set S+ with a faithful
                                (n)           (n)
                   D̃n := {h̃1 , . . . , h̃d },               projective unitary representation that satisfies Eq. (4).
                                                              Notice that one has the identity
where                                                                                 
                                                                              I ⊗ A†k=0 A =
                                                                                              X
                          (n)
                                                                                                 Th ⊗ A0 h ,
                        h̃l     · him = δlm .                                                      h∈S

                                                                           0
                                                                   P
Now we define the set                                         with    h∈S A h = Is , namely modulo a uniform local
                                      [                       unitary we can always assume
                              D̃ :=       D̃n .                                     X
                                      n                                                Ah = Is ,               (9)
                                                                                        h∈S
The Brillouin zone B ⊆ Rd is defined as the polytope
            \                                                 as explained in the following. Indeed, the isotropy re-
     B=        {k ∈ Rd | −π|h̃|2 ≤ k · h̃ ≤ π|h̃|2 }.         quirement implies that Ak=0 commutes with the repre-
           h̃∈D̃                                              sentation of the isotropy group L, whence we can classify
                                                                                                                                4

the QW by requiring identity (9) and then multiplying                      • d = 2: Zn and Dn with n ∈ {1, 2, 3, 4, 6};
the QW operator A on the left by (I ⊗V ), with V unitary
                                                                           • d = 1: {e} and Z2 .
commuting with the representation of L. In the case that
the representation is irreducible, then by Schur lemma we             Accordingly, our cases of interest d = 1, 2, 3 can be
have only V = Is .                                                    treated together, considering just d = 3. We notice that
  From now on we will restrict to s = 2, which corre-                 for d = 1, 2 the finite subgroups of GL(d, Z) coincide with
sponds to the simplest nontrivial QW in the case of G                 those of O(d), while for d = 3 we restricted to those finite
Abelian. Indeed, in Ref. [24] it has been proved that if              subgroups of GL(3, Z) that are also subgroups of O(3).
G is an arbitrary Abelian group and s = 1 (scalar QW                     A given generating set for Zd satisfying the definition
case), then the evolution is trivial.                                 of isotropy can be constructed orbiting a vector in Rd
                                                                      under the aforementioned finite subgroups in O(d). Ac-
                                                                      cordingly, given a presentation for Zd , if the associated
   IV.    IMPOSING ISOTROPY: ADMISSIBLE                               Cayley graph satisfies isotropy then one can represent the
             CAYLEY GRAPHS OF Zd                                      generators having all the same Euclidean norm, namely
                                                                      they lie on a sphere centered at the origin: they form the
   In this Section we investigate how the isotropy as-                orbit—which we will denote as OL (v)—of an arbitrary
sumption restricts the possible presentations of G ∼= Zd .            d-dimensional real vector v under the action of a finite
By Prop. 2, the isotropy groups are finite subgroups                  subgroup L < GL(d, Z) represented in O(d).
L < Aut(Zd ) ∼= GL(d, Z): their action, by Cor. 2, is de-                In Appendix A we will consider the orbit of a vector
fined to be transitive on the generating set S+ and then              v ∈ R3 under the real, orthogonal and three-dimensional
is extended on all Zd by linearity. Indeed, the generating            faithful representations of L. Indeed, if we took into ac-
set S+ is the orbit of an arbitrary vector v ∈ Rd under               count also unfaithful representations, these would have
the action of a finite subgroup L < GL(d, Z).                         nontrivial kernel—which is a normal subgroup—and the
   Let M be a representation on integers of L (so that                effective action on v would be given by a faithful repre-
Ml MfP= Mlf for l, f ∈ L), and let us define the matrix               sentation of the quotient group. Inspecting the subgroup
P := l∈L MlT Ml . For every f ∈ L we have                             structure of the finite subgroups of GL(3, Z), one can
                                                                      check that all the possible quotients are themselves finite
                                                                      subgroups of GL(3, Z) [27]. Thus, the case of unfaithful
                 X                   X
      P Mf =           MlT Mlf =             MlT0 f −1 Ml0 =
                 l∈L                 l0 ∈L
                                                                      representations is already considered as long as we take
                 X                   T                        (10)   into account the faithful ones.
             =           Ml0 Mf −1        Ml0 = MfT−1 P.
                 l0 ∈L
                                                                      V.    THE QWS WITH MINIMAL COMPLEXITY:
Moreover, being a sum of positive operators, P is                             THE WEYL QUANTUM WALKS
P positive.
also                Then, for |ηi ∈ ker P , hη| P |ηi =
             T
   l∈L hη| M l M l |ηi = 0 implies that Ml |ηi = 0 ∀l ∈ L,              In the following X = V |X| will denote the√polar de-
namely |ηi = 0 since all Ml are invertible. Thus P has
trivial kernel and we can define the invertible change of             composition of the operator X, with |X| := X † X the
representation:                                                       modulus of X, and V unitary. Thus we will write the
                                                                      transition matrix as
                     M̃l := P 1/2 Ml P −1/2 .                  (11)                          Ah = Vh |Ah |.                  (12)
Using the definition of P and property (10), we obtain                From Eq. (8) with h00 = 2h it follows that Ah A†−h =
                                                                      0, namely, |Ah ||A−h | = 0. By definition the transition
            T
         M̃l M̃l = P −1/2 MlT P Ml P −1/2 =                           matrices are nonnull, hence |Ah | and |A−h | must have
                                                                      orthogonal supports, and for s = 2 they must then be
                    = P −1/2 MlT MlT−1 P P −1/2 = I.                  rank-one. Thus they can be written as follows
This means that, as long as one embeds the Cayley                        Ah =: αh Vh |ηh ihηh |,   A−h =: α−h V−h |η−h ihη−h |,
graphs in Rd , L can always be represented orthogonally.                                                                     (13)
Notice that the representation M̃ is in general on reals,             where {|η+h i, |η−h i} is an orthonormal basis and αh > 0.
namely {M̃l }l∈L ⊂ O(d, R) (from now on we denote it                  By the isotropy requirement we have that for all h, h0
just as O(d)).                                                        α±h = α±h0 =: α± . Furthermore, it is easy to see that
  As one can find in Refs. [25, 26], the finite subgroups of          we can choose Vh = V−h for every h [28].
GL(d, Z) which are also subgroups of O(d) are isomorphic                 Denoting the elements of S± as ±hi , suppose that
to:                                                                   there exists a subgroup K ≤ L such that, for some
                                                                      h1 ∈ S+ , ∀hi , hj ∈ OK (h1 ) with hi 6= hj , and for
   • d = 3: Zn , Dn with n ∈ {1, 2, 3, 4, 6}, A4 , S4 , and           hl , hm ∈ {0, OL (h1 )}, one has
     the direct products of all the previous groups with
     Z2 ;                                                             hi − hj = hl − hm ⇐⇒ (hi = hl ) ∨ (hi = −hm ). (14)
                                                                                                                                5

Then, a second set of equations from conditions (8) is                       The isotropic QWs on Zd for d = 1, 2, 3

                 Ah1 A†hj + A−hj A†−h1 = 0,                   (15)      In Appendix A we make use of Prop. 3 along with the
                                                                     unitarity constraints to exclude an infinite set of Cayley
                 A†h1 Ahj + A†−hj A−h1 = 0.                   (16)
                                                                     graphs arising from the aforementioned finite subgroups
                                                                     of O(3). We then proved the following.
Multiplying Eq. (15) by A†hj on the left or by Ah1 on the
right, we obtain                                                     Proposition 4. The primitive cells associated to the
                                                                     unique graphs admitting isotropic QWs in dimensions
                                                                     d = 1, 2, 3 are those shown in Fig. 1.
              A†hj Ah1 A†hj = Ah1 A†hj Ah1 = 0.
                                                                        Throughout the present section, we solve the unitarity
Using the isotropy requirement and posing Ahj                   =    conditions in dimension d = 1, 2, 3 for the Cayley graphs
Uk Ahi Uk† , we have                                                 associated to the primitive cells shown in Fig. 1, and
                                                                     for all the possible isotropy groups. We remind that in
     Uk A†h1 Uk† Ah1 Uk A†h1 Uk† = Ah1 Uk A†h1 Uk† Ah1 = 0.          general each isotropy group gives rise to a distinct pre-
                                                                     sentation for Zd , possibly with the same first-neighbours
                                                                     structure. As discussed in Fig. 1, different presentations
By exploiting Eq. (13) both the previous equations be-
                                                                     can be in general associated to the same primitive cell
come
                                                                     (one can include in S+ the inverses or not). We will now
                                                                     prove our main result, which is stated in Prop. 5 after
           hηh1 |Vh†1 Uk† Vh1 |ηh1 ihηh1 |Uk |ηh1 i = 0.             the following derivation.
                                                                        Before starting the derivation, we remind that in each
Then, at least one of the two following conditions must              case we can choose |η±h1 i to be the eigenstates of σZ .
be satisfied                                                         Moreover, we will make use of Eq. (13) to represent the
                                                                     transition matrices, reminding that Vh = V−h . Finally,
                  hηh1 |Vh†1 Uk† Vh1 |ηh1 i = 0,              (17)   we recall that in Sec. III we showed that one can always
                  hηh1 |Uk |ηh1 i = 0.                        (18)   impose condition (9) and then multiply the transition
                                                                     matrices on the left by an arbitrary unitary commuting
Furthermore, we remind that the representation U can                 with the elements of the representation UL .
be chosen with unit determinant, and for s = 2 one has                  Case d = 1. We can write the transition matrices
Uk = cos θI + i sin θ nk · σ. Then, from Eqs. (17) and               associated to ±h1 as
(18) one has Uk = ink · σ. Using the identity
                                                                       Ah1 = α+ V |ηh1 ihηh1 |,   A−h1 = α− V |η−h1 ihη−h1 |.
          Uk Uk0 = −nk · nk0 I − i(nk × nk0 ) · σ,            (19)
                                                                     Multiplying on the right respectively by Ah1 and A†−h1
it follows that all the nk must be mutually orthogonal               the unitarity conditions
and then |K| ≤ 4. The case K ∼        = Z3 is not consistent
with Eqs. (17) and (18). Accordingly, we end up with                                  Ah1 A†e + Ae A†−h1 = 0,
                                                                                                                           (20)
K ∈ {I, Z2 , Z2 × Z2 , Z4 }. Notice that, up to a change of                           A†e Ah1 + A†−h1 Ae = 0,
basis, one can always choose |η±h1 i to be the eigenstates
of σZ without loss of generality. Then, by Eqs. (17),(18)            one obtains
and imposing Uk ∈ SU(2) ∀k ∈ K, up to a change of
basis it must be: either i) UK := RngK (U ) = H, where                                  A±h1 A†e A±h1 = 0,
H := {I, iσX , iσY , iσZ } is the Heisenberg group, or ii)
UK = J where J ∈ {Ji }4i=1 , where J1 := {I, iσX },                  which implies Ae = V W , where W has vanishing diago-
J2 := {I, −Vh1 (iσX )Vh†1 }, J3 := {I, iσX , −I, −iσX }, and         nal elements in the basis {|η+h1 i, |η−h1 i}. Substituting
J4 := {I, −Vh1 (iσX )Vh†1 , −I, Vh1 (iσX )Vh†1 }, or finally iii)    into Eqs. (20), one derives α+ = α− =: n and, up to
UK = {I}. We remark that H is a projective faithful                  a change of basis, Ae = imV σX with m ≥ 0. Imposing
representation of Z2 × Z2 in SU(2), while {Ji }2i=1 are              the normalization condition (7) amounts to the relation
projective faithful representations of Z2 , while {Ji }4i=3          n2 + m2 = 1. The admissible isotropy groups are I and,
are unitary faithful representations of Z4 in SU(2). We              up to a change of basis, J1 . Then, for UL = {I}, the
have thus proved the following result.                               transition matrices are given by:
                                                                                                                 
Proposition 3. If the isotropy group L contains a sub-                                   n 0                    0 0
                                                                              Ah1 = V          , A−h1 = V             ,
group K such that all the hk ∈ OK (h1 ) (for h1 ∈ S+ )                                   0 0                    0 n
                                                                                              
satisfy condition (14), then either UK = H or UK = J                                     0 im
                                                                              Ae = V             ,
or UK = I.                                                                              im 0
                                                                                                                                   6



                                                             h1                                            h1
                           h1                                             h2                                          h2

                                                                                                      h4
                                                                                                                      h3



                                                                                                              (c)
                    (a)                                           (b)

 FIG. 1: We report here the primitive cells of the unique graphs admitting isotropic QWs in dimensions d = 1, 2, 3. Integer
     lattice (a): the isotropy groups can be UL = {I} and UL = {I, iσX }, corresponding respectively to S+ = {h1 } and
          S+ ≡ S− = {h1 , −h1 }. Simple square lattice (b): the isotropy groups can be UL = {I, iσX }, {I, iσZ } and
  UL = {I, iσX , iσY , iσZ }, corresponding respectively to S+ = {h1 , h2 } and S+ ≡ S− = {h1 , h2 , −h1 , −h2 }. Body-centered
 cubic (BCC) lattice (c): the only possible isotropy group is UL = {I, iσX , iσY , iσZ }, corresponding to S+ = {h1 , h2 , h3 , h4 }
       with the nontrivial relator h1 + h2 + h3 + h4 = 0. We notice that the case d = 1 is the only one supporting the
                                            self-interaction, namely such that Ae 6= 0.


where V is an arbitrary unitary. For UL = {I, iσX },                    and then multiply the transition matrices by a unitary
we impose condition (9) and then V can be taken as an                   commuting with the representation UL . The isotropy
arbitrary unitary commuting with σX .                                   group can be either J2 ≡ {I, iσZ } or H for the first family
  Case d = 2. The form of the transition matrices is:                   of walks, while either J1 = {I, iσX } or H for the second
                                                                        one. Thus the first family is given by
               A±h1 = α± Vh1 |η±h1 ihη±h1 |,
                                                                                                                       
               A±h2 = α± Vh2 |η±h2 ihη±h2 |.                                          1     1 0               1     0 −1
                                                                              Ah1 = V             , A−h1 = V                 ,
                                                                                      2     1 0               2     0 1
Multiplying on the right by Ah1 the unitarity conditions                                                               
                                                                                      1      1 0                1     0 1
                                                                              Ah2 = V               , A−h2 = V               ,
                                                                                      2     −1  0               2     0 1
                Ah1 A†±h2 + A∓h2 A†−h1 = 0,                (21)

one obtains                                                             where V is either an arbitrary unitary commuting with
                                                                        σZ or V = I, while the second family of transition ma-
                     Ah1 A†±h2 Ah1 = 0.                                 trices is obtained exchanging h2 ↔ −h2 and taking V as
                                                                        either an arbitrary unitary commuting with σX or V = I.
The latter implies either i) |η±h1 i = |η±h2 i or ii)                      Case d = 3. The isotropy requirement can be fulfilled
|η±h1 i = |η∓h2 i and that, in both cases, one can choose               with UL = H. At least one of the two conditions of
Vh1 = Vh2 (iσY ) up to a change of basis. In either cases,              Eqs. (17) or (18) must be fulfilled for any nontrivial l ∈ L.
substituting into Eqs. (21) one derives α+ = α− =: α                    Since Eq. (18) cannot be satisfied for Ul = iσZ , then it
and, from the normalization condition (7), α = √12 . Re-                must be hηh1 |Vh†1 σZ Vh1 |ηh1 i = 0. This implies
defining V := Vh2 , in case i) one obtains the following
family of transition matrices:                                                             Tr[Vh†1 σZ Vh1 σZ ] = 0.             (23)

                A±h1 = ±αV |η∓h1 ihη±h1 |,                              Writing Vh1 in the general unitary form
                                                           (22)
                 A±h2 = αV |η±h1 ihη±h1 |.
                                                                                                    µ −ν ∗
                                                                                                          
                                                                                          Vh1 = θ            ,
The second family, namely case ii), is connected to the                                             ν µ∗
first one via the exchange h2 ↔ −h2 . One can check that
the self-interaction term Te ⊗ Ae is not supported by the               where |θ|2 = |µ|2 + |ν|2 = 1, the condition in Eq. (23)
unitarity conditions                                                    implies |µ| = |ν| = 2−1/2 , and using the polar decompo-
                                                                        sition (13) of A±h1 we obtain
    Ah A†e + Ae A†−h = A†h Ae + A†e A−h = 0 ∀h ∈ S,
                                                                                                           α− 0 −ψ ∗
                                                                                                                    
                                                                                   α+ φ 0
                                                                            Ah1 = √            , A−h1 = √            ∗   , (24)
namely Ae = 0. Imposing Eq. (9), one can choose                                      2 ψ 0                   2 0 φ
                                
                       1    1 1                                         with φ, ψ phase factors. Using isotropy, namely consid-
                 V =  √
                        2 −1 1                                          ering the orbit of the above matrices under conjugation
                                                                                                                                7

with H, we obtain                                                        b) Case d = 2: one has Ae = 0 and
                                                                                                              
                                ∗                                              1     1 0             1   0 −1
         α+ 0 ψ               α−   φ 0                                      Ah1 = V           , A−h1 = V           ,
   Ah2 = √          , A−h2 = √       ∗    ,                                        2     1 0             2   0 1
           2 0 φ               2 −ψ 0                                                                         
                                                                                   1     0 1             1    1 0
                               α− φ∗ 0
                                     
         α+ 0 −ψ                                                            Ah2 = V           , A−h2 = V           ,
   Ah3 = √            , A−h3 = √     ∗    ,                    (25)                2     0 1             2   −1 0
           2 0 φ                 2 ψ 0
         α+
             
                φ 0
                    
                               α− 0 ψ ∗
                                                                          where V is a unitary commuting with σX if S+ =
   Ah4 = √            , A−h4 = √       ∗ .                                  {h1 , h2 } or V = I if S+ = {h1 , h2 , −h1 , −h2 }.
           2 −ψ 0                2 0 φ
                                                                         c) Case d = 3: one has Ae = 0 and
Also in this case, the self-interaction term is not sup-                              ± 
                                                                                                          0 −η ∓
                                                                                                                
ported by the unitarity conditions. Finally, we can write                              η 0
                                                                              Ah1 =            , A−h1 =            ,
the matrix Ak in Eq. (6) as                                                            η± 0               0 η∓
                                                                                       0 η±                η∓ 0
                                                                                                              
                      4                                                       Ah2 =        ± ,   A−h2 =            ,
                      X                                                                0 η                −η ∓ 0
             Ak =           (Ahi eiki + A−hi e−iki )
                                                                                       0 −η ±               η∓ 0
                                                                                                              
                      i=1                                                     Ah3 =             , A−h3 =           ,
                                                                                            ±
                                                                                       0 η                  η∓ 0
and imposing unitarity of Ak for every k, one obtains the                             ±
                                                                                        η    0
                                                                                                         
                                                                                                            0 η∓
                                                                                                                 
following conditions                                                          Ah4 =       ±     , A−h4 =           .
                                                                                       −η 0                 0 η∓
                          1 ∗2                                              where η ± = 1±i
          2
         α+    2
            = α− =          , φ + φ2 = ψ ∗2 + ψ 2 = 0,                                    4 and S+ = {h1 , h2 , h3 , h4 } with the
                          4                                                 nontrivial relator h1 + h2 + h3 + h4 = 0.
namely
                                                                                     VI.   CONCLUSIONS
                             1+i           1−i
       φ, ψ ∈       ±ζ + := ± √ , ±ζ − := ± √              .
                               2              2                          In this paper we presented a complete classification
                                                                      of the isotropic quantum walks on lattices of dimension
The different choices of the overall signs for φ, ψ are con-
                                                                      d = 1, 2, 3 with coin dimension s = 2. We have extended
nected to each other by an overall phase factor and by
                                                                      the isotropy definition of Ref. [1], to account for groups
unitary conjugation by σZ . Then we can fix then choos-
                                                                      with generators of different orders. We introduced a tech-
ing the plus signs. The choices φ = ζ ± , ψ = ζ ∓ are
                                                                      nique to construct the Cayley graphs of a given group
equivalent to φ = ψ = ζ ± via conjugation of the former
       π                                                              G satisfying a relevant necessary condition for isotropy.
by e±i 4 σZ and an exchange h1 ↔ h4 . Accordingly, the                This allowed us to exclude an infinite class of Cayley
QWs found are given by the transition matrices of Eqs.                graphs of Zd . The technique is sufficiently flexible to be
(24) and (25) with ψ = ϕ = ζ ± , namely the two Weyl                  used in the future for other generally non Abelian groups.
QWs presented in Ref. [1].                                            Remarkably, the Cayley graph is unique for each dimen-
  We have thus proved the following main result.                      sion d = 1, 2, 3 and for d = 3 the only admissible QWs
                                                                      are the two Weyl QWs presented in Ref. [1]. The use of
Proposition 5 (Classification of the isotropic QWs on                 isotropy since the very beginning has made the solution of
lattices of dimension d = 1, 2, 3 with a coin system of               the unitarity equations significantly shorter. Moreover,
dimension s = 2). Let S = S+ ∪ S− ∪ {e} denote a set                  we eliminated the superfluous technical assumption used
of generators for Zd and let {Ah }h∈S denote the set of               in Ref. [1] mentioned in the Introduction. In consider-
transition matrices of a QW on Zd with a coin system                  ation of the length of the derivation from informational
of dimension s = 2 and isotropic on S+ . Then for each                principles of the Weyl equation in Ref. [1], the present
d = 1, 2, 3 the admissible graphs are unique (see Fig. 1)             derivation constitutes a thoroughly independent check.
and one has the following:                                            Finally, this result represents the extension of the classi-
                                                                      fication of Ref. [24].
  a) Case d = 1:
                      
                                      
                  n 0               0 0                                               ACKNOLEDGMENTS
         Ah1 = V        , A−h1 = V        ,
                  0 0               0 n
                       
                  0 im                                                  This publication was made possible through the sup-
         Ae = V           ,
                 im 0                                                 port of a grant from the John Templeton Foundation, ID
                                                                      # 60609 “Quantum Causal Structures”. The opinions
      where n, m are real such that n2 +m2 = 1, and V is              expressed in this publication are those of the authors and
      an arbitrary unitary if S+ = {h1 } or V is a unitary            do not necessarily reflect the views of the John Temple-
      commuting with σX if S+ = {h1 , −h1 }.                          ton Foundation.
                                                                                                                           8

         Appendix A: Excluding Cayley graphs                    (s, t signs). Our strategy is now to solve the necessary
                                                                conditions for the violation of (A1), consisting in systems
  In Secs. A 1–A 4 we will exclude the infinite family of       of the form
graphs arising from the following finite isotropy groups
L < O(3):                                                             ∀A, B ∈ L0 , (I − D − s(A + tB))v = 0.           (A2)

     1. A4 , S4 and their direct product with Z2 (except for    These will produce some solutions v0 . Then we can
        the cases in item 2);                                   choose another vector in OL (v0 ), impose again Eq. (A2),
                                                                and iterate until we end up either with the trivial solu-
     2. the special instances of item 1 where the orbits con-   tion, or with a system of linear equations for α, β, γ. By
        tain the vertices of a truncated tetrahedron;           Prop. 6, the only A4 - or S4 -symmetric Cayley graphs
                                                                of Z3 for which the unitarity conditions may be satis-
     3. Zn , Dn for n = 3, 4, 6 and their direct product with
                                                                fied must then be found among the non-trivial solutions
        Z2 ;
                                                                of the above systems. Since the condition (A2) is only
     4. one special instance arising from D2 , D2 × Z2 .        necessary, we need to check whether the solutions actu-
                                                                ally violate condition (A1). The remaining differences
                                                                (D − D2 )v and (D2 − I)v are the orbit of (I − D)v under
1.     Excluding A4 - and S4 -symmetric Cayley graphs           D, then we can just solve (A2) and check (A1).
                                                                   In the following we will show that (A1) has only trivial
   In this subsection we use the convention that unwrit-        solutions for A, B ∈ L, except for the special case where
ten matrix elements are zero. In Secs. A 1 a and A 1 b we       v = α(3, 1, 1)T , that will be treated separately in Sub-
will consider the orbit of an arbitrary three-dimensional       sec. A 2. At the end of Subsec. A 1 b we will then prove
vector v = (α, β, γ)T under the action of the finite groups     the same result in the case of B = 0.
L ∼ = A4 , S4 in O(3). To this purpose, as discussed               It is useful to notice the following:
in Sec. IV, we will use the real, orthogonal and three-
                                                                Remark 1. v1 ∈ R3 solves
dimensional faithful representations of L, identifying its
representation with the group itself. In the present case                      (I − D − s(A + tB))v1 = 0
of L ∼= A4 , S4 , such representations coincide with the ir-
reducible ones, since the reducible ones cannot be faithful     iff v2 := F2−1 v1 solves
(otherwise they would have orthogonal blocks of dimen-
sion at most 2, but A4 , S4 are not subgroups of O(2)).                     F1 (I − D − s(A + tB))F2 v2 = 0,
   We denote with OL (v) the family of orbits of v un-
der the action of L, parametrized by α, β, γ. Each orbit        for some arbitrary F1 , F2 ∈ GL(3, R). In particular, this
satisfies a necessary condition to give rise to an isotropic    is relevant in the case F2 ∈ L, because it means that the
presentation for Zd for d = 1, 2, 3.                            orbits generated by the two solutions v1 , v2 coincide.
Proposition 6. If L contains a ternary subgroup K ∼       =       This remark will allow us to considerably reduce the
Z3 such that for hi , hj ∈ OK (v) and hl , hm ∈ OL (v), the     number of systems we have to solve. In the following we
condition in Eq. (14) is satisfied, then the set of vertices    will refer to a particular solution for (A2) indifferently
OL (v) cannot satisfy the necessary conditions (16),(15)        with: 1) the solution vector v0 , or 2) the lattice which
for unitarity.                                                  v0 gives rise to, or 3) the polyhedron whose vertices are
                                                                the elements of OL (v0 ), or 4) any other vector in OL (v0 ),
Proof. By Prop. 3, K has to be a subgroup of the                or finally 5) the orbit OL (v0 ). The cases we will end up
Heisenberg group H. However H does not contain                  with are the following:
ternary subgroups. 
   We will make use of Prop. 6 to exclude an infinite fam-         1. The simple cubic lattice, generated orbiting vs =
ily of presentations arising from L ∼
                                    = A4 , S4 . Since by Eq.          α(1, 0, 0)T under A4 : its vertices are all the signed
(14) we are interested in sums or differences of generators,          permutations of the coordinates of vs .
the cases L ∼ = A4 × Z2 , S4 × Z2 are already accounted:           2. The BCC lattice, generated orbiting vb =
their irreducible representations just add the inversion to           α(1, −1, −1)T under S4 : its vertices are all the
the irreducible ones of A4 , S4 .                                     signed permutations of the coordinates of vb .
   The groups L contain four isomorphic copies of Z3 (see
Subsecs. A 1 a,A 1 b). Let us denote with D the genera-            3. The cuboctahedron, whose vertices are all the
tor of one of this cyclic subgroups. The content of Eqs.              signed permutations of the coordinates of vc =
(14) for a fixed choice of i, j translates to the following.          α(1, −1, 0)T and are generated by orbiting vc under
Suppose that for all A, B ∈ L0 := {0 ∈ M3 (R)} ∪ L one                A4 .
has:
                                                                   4. The truncated tetrahedron, whose vertices are all
 (I−D)v = s(A+tB)v ⇔ (sAv = v)∨(stBv = v), (A1)                       the permutations with an even number of minus
                                                                                                                          9
                                                                                                
      signs of the coordinates of vtt = α(3, 1, 1)T and are                            2s
      generated by orbiting vtt under A4 ; in addition,             1. s(Xi + tXj ) =    ±ξ          , modulo permutations
      one can also find the solution including the inverses,                                         0
      which is given by OS4 (vtt ).                                    of the diagonal elements, with arbitrary sign s and
                                                                       for ξ := 0, 2.
   5. The truncated octahedron, whose vertices are all                                                 
      the signed permutations of the coordinates of vto =                                     s1 0 t1
      α(1, −2, 0)T and are generated by orbiting vto un-            2. s(Xi + tXj R) =  t2 s2 0 , with s1 s2 + s1 s3 +
      der S4 .                                                                                 0 t3 s3
                                                                       s2 s3 = t1 t2 + t1 t3 + t2 t3 = −1.
One can easily check that OL (v0 ) for the five cases above
actually are generating sets for some presentation of Z3 .
                                                                                                       
                                                                                              s1 t1 0
  In the following, we will choose D = R with                       3. s(Xi +tXj R2 ) =  0 s2 t2 , with arbitrary signs
R(x, y, z)T = (z, x, y)T (R is contained in the represen-                                     t3 0 s3
tation of both A4 and S4 ). As a consequence, we can                   tk , and s1 s2 + s1 s3 + s2 s3 = −1.
consider A 6= B, since otherwise there are two possible                                                 
cases:                                                                                                 2s
                                                                    4. s(Xi + tXj )R = ±ξ                and permutations
   1. (I − R)v = ±2Av, implying (A−1 − A−1 R)v =                                                     0
      ±2v. Since A, R ∈ O(3), by the triangle inequality               of the written elements, with arbitrary sign s and
      it must be                                                       ξ = 0, 2.
               A−1 v = ±v, A−1 Rv = ∓v,                                                         
                                                                                                   0 t1 s1
                                                                                                            

      and in particular v = −Rv holds. This implies                 5. s(Xi + tXj R)R = s2 0 t2 , with arbitrary
      v = (0, 0, 0)T .                                                                             t3 s3 0
                                                                       signs tk , and s1 s2 + s1 s3 + s2 s3 = −1.
   2. (I − R)v = 0, implying v = α(1, 1, 1)T .                                                           
                                                                                                   2s
   Finally, the reader can check that for v0 ∈                      6. s(Xi + tXj )R2 =               ±ξ  and permutations
{vs , vb , vc , vto } condition (A1) is not violated, thus ex-                                  0
cluding the cases of S+ = OL (v0 ) by virtue of Prop. 6.               of the written elements, with arbitrary sign s and
                                                                       ξ = 0, 2.
        a.   Excluding A4 -symmetric Cayley graphs                 All the above mentioned permutations of elements and
                                                                 those between the si and ti are performed by conjugation
  A4 has a unique three-dimensional real irreducible rep-        with R±1 . Since
resentation, generated by the matrices:
                                                             (I − R − sR(A + tB)R−1 ) = R(I − R − s(A + tB))R−1 ,
               1 0 0               0 0 1
       X1 = 0 −1 0  , R = 1 0 0 .               (A3)         by Remark 1 we can just choose one permutation in each
               0 0 −1              0 1 0                         of the six cases to find the orbits of the solutions.
                                                                    Accordingly, explicitly computing the expression
We define                                                                                                
                                                                                              1 0 −1
       X0 = I, X2 = RX1 R−1 , X3 = R2 X1 R−2 .                      I − R − s(A + tB) = −1 1 0  − s(A + tB),
The group contains four isomorphic copies of Z3 ,                                             0 −1 1
generated respectively by the elements of the set
                                                                 we end up with the following cases:
{R, X1 R, X2 R, X3 R} (these are cyclic signed permuta-
tions of the coordinates).
                                                                                           
                                                                         1 + 2s 0 −1
   We now choose the subgroup generated by R and con-               1.  −1 1 ± ξ 0 , for s arbitrary sign.
sider the difference (I − R)v, setting the condition (A2)                   0       −1 1
for any A, B ∈ A4 . Each of these define linear systems                                                     
of three equations for v. If A equals I or R, then it is                  2        −2       2     0      0     −2
easy to see that ∃G ∈ A4 such that Gv = sv (s a sign):              2. −ξ 0 ξ         , −2 ξ     , −ξ 0 2   ,
this implies that either v = (0, β, γ)T up to signed per-                     0 0               0
                                                                                              −ξ 0           0 ξ
mutations, or OA4 (v) = OA4 (vb ). The latter case was                 with ξ, ξ 0 = 0, 2.
excluded in Subsec. A 1. The remaining cases are then i)                              
A, B 6∈ {I, R} or ii) v = (0, β, γ)T and signed permuta-                  2 s1 −1
tions. Case (ii), however, will appear as a special instance        3. −1 ξ s2 , with si arbitrary.
of (i). In case (i), we have six cases for s(A + tB):                    s3 −1 0
                                                                                                                        10
                     
       1   0    2s − 1                                       orbiting the elements generated by (A3) under the left
   4. −1  1       0 , with s arbitrary.                    action of {I, C} with
       0 ±ξ − 1    1                                                                        
                                                                                       0 0 1
                                                                                 C = 0 1 0 ,
              
       1 s1 0
   5. −2 1 s2 , with s arbitrary.                                                    1 0 0
       s3 −ξ 1
                                                             whose effect is just an exchange of the first and third row.
                                                             Let us now define Xi0 := CXi . In order to perform the
       1 2s −1
                                                             computation of s(A + tB), we proceed as follows. We
   6. −1 1 0 , with s arbitrary.
                                                             have to compute
       ±ξ −1 1
                                                                                     s(Xi + tXj ), s(Xi0 + tXj0 ),
The only solution to cases 1 and 4 is OA4 (vb ). Cases
3, 5 and 6 can be treated together since they exhibit a                          s(Xi + tXj R), s(Xi0 + tXj0 R),      (A6)
common structure: their solutions are OA4 (vb ) (which          s(Xi0 + tXj ),   s(Xi0 + tXj R),   s(Xi0 + tXj R2 )
has been already excluded by Prop. 6) and OA4 (vtt )
(which is excluded in Sec. A 2). The only relevant case is   and then recover all the remaining combinations by right
2, since all the other cases have been already excluded.     multiplication of these by R±1 . For (A6), we obtain the
   In case 2, the most general orbits of solutions are       following cases:
OA4 (vi ) for i = 1, 2, 3, where                                    
                                                                      ±2
                                                                               
                                                                                         ±2
                                                                                            
                                                             1.      ξ , ξ            , considering all the per-
                   α             0                                          0      0
           v1 = β  , v2 = β  , v3 = R2 v2 .      (A4)           mutations of elements and ξ = 0, ±2.
                   α             γ                                                                      
                                                                      s1    t1           t1 s1     s1     s2
Nevertheless, for v ∈ {v2 , v3 } the condition (A1) is not       2.  t2 s2     ,  t2 s2      ,    ξ     ,
violated. Indeed, v2 was found as a solution of                          t3 s3       s3      t3    s3     s4
                                                                                          
                                                                            ξ          t1 s1
                (I − R + X1 − RX1 )v2 = 0,            (A5)           t2 s2  ,  s2 t2  , for ξ = 0, ±2.
                                                                      s3 t3         ξ
however X1 v2 = −v2 , and thus Eq. (A1) is satisfied. A
similar argument holds for v3 . By virtue of Prop. 6 the     As mentioned above, one has to add to these cases the
corresponding orbits OA4 (v2 ) and OA4 (v3 ) are excluded.   matrices resulting from a right multiplication of the pre-
   From the above analysis we already know that the only     vious ones by R±1 , whose action is a cyclic permutation
relevant solution is v1 for case 2, modulo cyclic permu-     of the columns. Let us now consider
tations. We now impose that X1 v1 , which is in OA4 (v1 ),                                        
                                                                                         1 0 −1
is itself a solution of Eq. (A2). Thus we impose
                                                                             I − R = −1 1 0  ,
                                                                                 0 −1 1
                         α0       α0     β0 
           X1 v1 = w ∈ β  , α  , α0  .
                              0     0
                                                             and derive the following matrices
                         α0       β0     α0 
                                                                         I − R + s(A + tB)Ri ,       i = 0, ±1        (A7)
The solutions are OA4 (vs ) and OA4 (vb ): we can exclude
also this last case.                                         for all the mentioned cases.
                                                                1. It’s easy to verify that, in this case, either the ma-
                                                                   trices in Eq. (A7) have trivial solution or their solu-
         b.   Excluding S4 -symmetric Cayley graphs                tions are OS4 (vb ) (already excluded) and OS4 (vtt )
                                                                   (which will be treated in Sec. A 2).
   The group S4 contains A4 as a subgroup of index                                                                  
                                                                     1 + s1           t1 − 1         1            ξ−1
2. The element connecting the two cosets is an involu-
                                                                2.  t2 − 1 1 + s2            , t2 − 1 1 + s2        ,
tion, which we will denote with C. S4 has two three-
                                                                              t3 − 1 1 + s3         s3    t3 − 1    1
dimensional irreducible representatons: their elements                                                             
are signed permutations matrices of three elements and                   1      t1    s1 − 1         1     ξ     −1
the two representations coincide up to a minus sign on the         s2 − 1       1      t2  , s2 − 1 1         t2  ,
elements in the coset CA4 . Nevertheless, in our case the               t     s3 − 1     1           t3   −1 1 + s3
                                                                    3                                               
sign is irrelevant, since we are considering combinations            1 + t1 s1         −1         1+ξ             −1
s(A + tB) of A, B ∈ S4 with s, t arbitrary signs. Ac-               −1 1 + t2 s2  ,  −1 1 + t2                 s2 ,
cordingly, we consider the representation resulting from                s3     −1 1 + t3                s3 − 1 1 + t3
                                                                                                                           11
                                                     
          1      t1    s1 − 1      1 + t1    s1      −1            • For M3 one has OS4 (vs ), OS4 (vb ), OS4 (vc ),
      t2 − 1 1 + s2          , s2 − 1 1 + t2                     OS4 (vt o), OS4 (v1 ) and OS4 (v4 ), with
          s3     −1 1 + t3                   −1 ξ + 1                                           
                                                                                               α
                                                     
        1 + t1   s1      −1        1 + s1         t1 − 1
      s2 − 1     1      t2  ,  t2 − 1      1      s2                              v4 =  β  .
                                                                                              α+β
               t3 − 1 1 + s3               ξ−1       1                                         2
                                                    
       1 + s1          t1 − 1       1     t1    s1 − 1
       −1 1 + t2        s2  , −1 1 + s2        t2 ,              The systems in the same equivalence class are con-
          t3   s3 − 1     1         ξ     −1       1                 nected by the permutations F ∈ {R2 , C}.
                                                     
       1 + s1         s2 − 1        1      s2    s1 − 1        We notice that v2 is a particular case of v4 , then we can
       −1 1 + ξ              , ξ − 1     1           ,     just treat the latter. On the other hand, the vectors in
          s3    −1 1 + s4                s4 − 1 1 + s3         OS4 (v3 ) cannot be solutions for Mi with i 6= 2, otherwise
                          
       1 + s2    s1    −1                                      the orbit is reduced to OS4 (vs ), or OS4 (vc ), or OS4 (vto ),
       −1        1     ξ .                                   which are ruled out. The remaining case of OS4 (v3 ) can
          s4   s3 − 1 1                                        be then excluded via the same analysis of case 2 in the
                                                               previous section.
   The above set can be partitioned into equivalence
                                                                  We end up with OS4 (v1 ), OS4 (v4 ). We observe that
classes according to the relation:
                                                               imposing that X2 v1 is a solutions for M1 , M2 , M3 gives
   N ∼ M ⇔ ∃F ∈ S4 , F 0 ∈ GL(3, R) : N = F 0 M F.             rise to OS4 (vs ), OS4 (vb ), OS4 (vc ). As for OS4 (v4 ),
                                                       (A8)    imposing that X2 v4 is a solution leads to OS4 (vtt ),
By Remark 1 the above equivalence relation preserves           OS4 (vto ), and OS4 (v5 ) with v5 = α(5, 3, 1)T . However,
the orbits of solutions of the linear systems. It is easy to   it’s easy to verify that (I − X2 R)v5 is uniquely deter-
check that there are five equivalence classes represented      mined as sum of elements of {0, OS4 (±v5 )}, leading us
by thefollowing matrices:                                    to exclude this last case by virtue of Prop. 6.
         1 + s1         s2 − 1                                    Finally, as anticipated at the beginning of Sec. A 1, we
M1 =  −1 1 + ξ                ,                              can exclude (I − R)v = ±Av for A ∈ L and L ∼        = A4 , S4 :
           s      −1 1 + s4                                    by direct inspection of the representation matrices of S4 ,
       3                                                     it turns out that this condition leads to OS4 (vc ).
         1 + s1          t1 − 1
M2 =  t2 − 1 1 + s2            ,
                 t3 − 1 1 + s3
                                                                  2.   Exclusion of the truncated tetrahedron
           1       t1    s1 − 1
M3 = t2 − 1 1 + s2            ,
           s3     −1 1 + t3                                       In this section we make use of the three-dimensional ir-
                                                             reducible representation of A4 provided in Subsec. A 1 a
            1       t1   s1 − 1
                                                               in order to exclude, by means of the unitarity condi-
M4 = s2 − 1        1       t2  ,
                                                               tions, the graph whose primitive cell is the set of ver-
           t3    s3 − 1     1
                                                             tices of the truncated tetrahedron. This also excludes
            1     ξ    −1                                      the case where the inverses are contained in S+ . For
M5 = s2 − 1 1          t2  .                                 notation convenience, we will use the Pauli matrices no-
           t3    −1 1 + s3                                     tation X := X1 , Y := X2 , and Z := X3 , and use the
The solutions for M4 , M5 are OS4 (vs ), OS4 (vb ) (that       vector wtt = α(1, 1, 3)T instead of vtt as a representative
have been already excluded) and OS4 (vtt ), that will be       of the orbit OA4 (vtt ). In the following we will also denote
treated in Sec. A 2.                                           the elements Gwtt (for G ∈ A4 ) with the shorthand G.
  The three remaining cases are given in the following:           Let U be a faithful unitary and (generally projective)
   • For M1 one has OS4 (vs ), OS4 (vb ), OS4 (vc ),           representation of A4 in SU(2). We will denote the tran-
     OS4 (vtt ), and OS4 (v1 ), OS4 (v2 ), with                sition matrices as
                                                                                                  †
                                     
                      α                 3                                          A±G := UG A±I UG ,                   (A9)
                v1 = α , v2 = α 1 ;
                      β                 2                      with G ∈ A4 . From the unitarity conditions (8), choosing
                                                               h00 = 2wtt , one derives the form
      The systems in the same equivalence class are con-
      nected by the permutations F ∈ {R±1 , C, CR±1 }.                            A±I := α± V |±i h±| ,                (A10)
   • For M2 one has OS4 (v1 ) and OS4 (v3 ), with
                                                             with {|+i , |−i} orthonormal basis, α± > 0 and V uni-
                            0                                  tary. Consider the following unitarity conditions:
                    v3 = α ;
                            β                                            AI A†W + A−W A†−I = 0,        W = X, Y.
                                                                                                                          12

By multiplication on the right by AI we obtain                   Now, substituting Eq. (A10), and using definition (A9),
                                                                 the nonvanishing matrix element of the previous identity
                       AI A†W AI = 0,                            in the basis {|+i , |−i} is
                                                                                                  †
implying that UW must be antidiagonal in the {|+i , |−i}                   h−| V † URX V |−i h−| URX |−i =
basis or in {V |+i , V |−i}. On the other hand, from
                                                                           = −ei h−| V † UY V |−i h−| UY† UR |−i .
                  AI A†−R + AR A†−I = 0,
                                                                 Recalling the form of V given above and using the fact
                                                                 that URX = t0 UR UX (t0 a sign) and that UR cannot have
one gets
                                                                 vanishing elements in the basis {|+i , |−i}, for the previ-
                                                                 ous equation we finally obtain
                     A−I A†R A−I = 0,                  (A11)
                                                                            cos(θ1 + ϕ1 ) = −i sin(θ1 + ϕ1 )e2i ,
meaning that UR must be diagonal in {|+i , |−i} or
{V |+i , V |−i}.                                                 which has no solution.
  Let us now suppose that UX is antidiagonal in
{|+i , |−i} and UY antidiagonal in {V |+i , V |−i} (or
viceversa): then, since                                           3.   Exclusion of Zn , Dn , Zn × Z2 and Dn × Z2 , with
                                                                                         n = 3, 4, 6
       UR UX UR† = s1 UY , UR UY UR† = s2 UZ ,         (A12)

(s1 , s2 arbitrary signs) all of the UG for G = X, Y, Z             The aim of the present section is: 1) to construct the
would be antidiagonal in one of the two bases, but this          real, orthogonal and three-dimensional faithful represen-
violates the algebra of D2 ≡ {I, X, Y, Z} in A4 . Accord-        tations of the groups L ∈ {Zn , Dn , Zn ×Z2 , Dn ×Z2 | n =
ingly, choosing the {|+i , |−i} basis and imposing               3, 4, 6}, and 2) to exclude all the graphs arising from L
                                                                 by means of the unitarity conditions.
                                   2
       UX UY = t1 UY UX = t2 UZ , UG = t3 I            (A13)        By the classification theorem for real matrices of finite
                                                                 order given in Ref. [29], any matrix in O(3) of order n is
(for G = X, Y, Z and t1 , t2 , t3 arbitrary signs), it is easy   similar to one of the form
to see that up to a change of basis we can always take:
                                                                                                        
                  UG = iσG , G = X, Y, Z                                                 cos θ − sin θ 0
                                                                                Rθ,s :=  sin θ cos θ 0 ,
with |+i , |−i eigenvectors of σZ . This implies that, in or-                               0     0    s
der to satisfy (A12), UR cannot have vanishing elements
in {|+i , |−i} and then by Eq.(A11) it must be diagonal          with θ = 2zπ  n , z integer and s a sign. The matrices
in {V |+i , V |−i}. Consequently we must have:                   Rθ,s represent the generators for the subgroups of order
                                                                 n = 3, 4, 6 in L. We can generate the orbits of L starting
                       UR := V DV † ,                  (A14)     from the generic vector (up to a rotation around the z-
                                                                 axis) given by v1 = (1, 0, h)T . It is easy to show that
where D = diag(ei , e−i ) in {|+i , |−i} and e3i is a         the only matrices in O(3) of order 2 commuting with
sign. As a consequence, using conditions (A13) one sees          Rθ,s for all θ and s are R0,t and Rπ,t : they represent
that the UX , UY , UZ cannot have vanishing elements in          the generators of L/Zn for L ∼   = Zn × Z2 or L/Dn for
{V |+i , V |−i}. This in turn implies, by Eq. (A12), that        L∼ = Dn × Z2 . On the other hand, the involutions
V cannot have vanishing elements in {|+i , |−i}.                                                          
   Let us now pose                                                                         cos ϕ sin ϕ 0
                                                                               Sϕ,r :=  sin ϕ − cos ϕ 0
             ρeiθ    τ eiϕ                                                                   0      0    r
     V =                     : ρ, τ > 0, ρ2 + τ 2 = 1.
            −τ e−iϕ ρe−iθ
                                                                                                                    −1
                                                                 are the only ones such that Sϕ,r Rθ,s Sϕ,r               =
Multiplying on the left by A†−I     the following unitarity                           −1
                                                                 Sϕ,r Rθ,s Sϕ,r = Rθ,s .     This implies that the Sϕ,r
condition                                                        represent the generators for the subgroups of reflections
                                                                 when L is a dihedral group. Therefore, in general, the
     AI A†RX + A−RX A†−I + AR A†Y + A−Y A†−R = 0,                elements of OL (v1 ) lie on the two circumferences which
                                                                 are parallel to the xy-plane at heights z = ±h.
and reminding that A†−I AR A†Y = 0 by Eq. (A14), one                In order to solve the unitarity conditions, it is neces-
has                                                              sary to determine the paths with length 2 constructed
                                                                 by elements in {0} ∪ OL (v1 ): by the above analysis, the
            A†−I A−RX A†−I + A†−I A−Y A†−R = 0.                  problem is reduced to a two-dimensional problem, since
                                                                                                                             13

the form of the vectors in OL (v1 ) is vi = (xi , yi , ±h)T :=    Multiplying the last equation by Av1 on the right and
(cos χi , sin χi , ±h)T . Accordingly, it is easy to see that     taking the adjoint we get [30]

  vi ± vj = svl + tvp ,    vi , vj , vl , vp 6= 0, (s, t signs)
                                                                               A†v1 Av2 A†v1 + A†v1 A−v4 A†−v3 = 0,
implies (xi , yi ) = s(xl , yl ) or (xi , yi ) = t(xp , yp ).
   Case n = 4. There are at least two inequivalent or-            which amounts to
thogonal representations of L ∈ {Z4 , D4 , Z4 × Z2 , D4 ×                     2
                                                                             α+      †         †
Z2 }, since the element of order 4 can be either repre-                       2 h+| R |+i h+| V RV |+i =
                                                                             α−                                          (A18)
sented by R π2 ,− or R π2 ,+ . We shall now analyse the two
                                                                                  ∗        †             †   3
different cases.                                                           = − ν h−| R |−i h+| V R V |−i .
   R π2 ,− generates the four vectors
                                                                  Posing now
                                        
        1            0           −1             0
                                                                                                            
                                                                                       †               a b
 v1 =  0  , v2 =  1  , v3 =  0  , v4 =  −1  .                                 V RV =                   ,
                                                                                                      −b∗ a∗
       h            −h            h           −h
                                                                  with a, b 6= 0 since otherwise V † R2 V cannot be anti-
The differences vi −vj 6= 0 ∀i, j ∈ {1, 2, 3, 4} are uniquely     diagonal (see (A17)), we have that
determined as sums of elements of {0, OL (±v1 )}. Ac-                                                              
cordingly, there is a cyclic subgroup of order 4 (i.e. Z4 )                                            a b      0 ν
                                                                   V † R3 V = (V † RV )(V † R2 V ) =                    .
whose orbit satisfies Eq. (14) and thus, invoking Prop. 3                                             −b∗ a∗   −ν ∗ 0
(we remind that the representation U must be faithful),
we exclude the representation containing R π2 ,− .                Accordingly, Eq. (A18) leads to
  Taking now R π2 ,+ , the orbit is                                                             2
                                                                                               α+
                                                                                                2 = −µ2 ,
                                                                                       α−
         1            0           −1           0
  v1 =  0  , v2 =  1  , v3 =  0  , v4 = −1 .              which is impossible, since µ2 6= µ∗ 2 .
        h            h             h           h                     Cases n = 3, 6.          The representations of L ∈
                                                                  {Zn , Dn , Zn ×Z2 , Dn ×Z2 | n = 3, 6} must contain R 2π
                                                                                                                         3 ,+
                                                                                                                              ,
We have that the vectors
                                                                  which generates a subgroup K isomorphic to Z3 : OK (v1 )
                    v1 + v2 ,   v1 − v3                   (A15)   is given by the following vectors:
                                                                                   
                                                                                      cos 2π
                                                                                                    
are uniquely determined as sum of elements of                                              3 (l − 1)
{0, OL (±v1 )}. Let us denote with R the matrix repre-                        vl =  sin 2π
                                                                                          3 (l − 1)
                                                                                                     , l ∈ {1, 2, 3}.
senting R π2 ,+ in SU(2) and proceed as in Sec. A 2. From                                   h
now on in the present section we use the notation of Eq.          We denote the representation matrix of R 2π           in SU(2)
(A9) and perform calculations in the {|+i , |−i} basis.                                                            3 ,+
                                                                  with U 2π  .
Multiplying on the right by Av1 the unitarity conditions                   3

associated to the vectors in (A15), we obtain                        If v1 − v2 is uniquely determined as sum of elements of
                                                                  {0, OL (±v1 )} (a particular case is given by the condition
                                           †                      h = 0), we can exclude this case by Prop. 6. Let us then
  Av1 RA†−v1 R† Av1 = 0, Av1 R2 A†v1 R2 Av1 = 0. (A16)
                                                                  suppose that v1 −v2 is not uniquely determined as sum of
By the first of conditions (A16), up to a change of basis         elements of {0, OL (±v1 )} (in particular h 6= 0) . Then,
we can impose                                                     by the above analysis, OL (v1 ) must contain
                                                                                   
                                                                                     − cos 2π
                                                                                                      
                                                                                            3 (l − 1)
                            
                        µ 0
                 R=            , R4 = sI                                      vl =  − sin 2π
                                                                                            3 (l − 1)
                                                                                                       , l ∈ {4, 5, 6}
                        0 µ∗
                                                                                            h
(s arbitrary sign); using the second condition, it follows        (such that v1 − v2 = v5 − v4 ). Again, via the above
that                                                              arguments on the representations of L, is easy to see
               2
                µ    0
                             
                                 0 ν
                                                                 that v1 + v2 is uniquely determined as sum of elements
          2
        R =              =V              V †,       (A17)         of {0, OL (±v1 )}. Then, from condition
                0 µ∗ 2          −ν ∗ 0
                                                                                   Av1 A†−v2 + Av2 A†−v1 = 0,
and thus necessarily µ2 6= µ∗ 2 . Consider now the unitar-
ity condition                                                     by multiplying on the right by Av1 , we get

   Av1 A†v2 + A−v2 A†−v1 + Av4 A†v3 + A−v3 A†−v4 = 0.                                  Av1 A†−v2 Av1 = 0.
                                                                                                                         14

Up to a change of basis U 2π3
                              = diag(ei , e−i ) holds with    which cannot be satisfied neither in case 1 nor in case 2.
e3i = ±1, and  6∈ {0, π}. Let Uπ represent the element        On the other hand in case b), from (A22) one has
of L mapping v1 to v4 . This element is an involution                    2
                                                                        α+
and there are only two cases (by inspection of the groups                   ∗ i
                                                                         2 a e = −e
                                                                                    −i
                                                                                        h−| V † Uπ† U †2π Uπ V |−i ,
L here considered)                                                      α−                              3


                                                               and being Uπ anti-diagonal, one has
                                   
                                      sU 2π
                                           3

                   Uπ U 2π Uπ† =                      (A19)               2
                                                                         α+
                         3             0    †                            2 a∗ e2i = − h−| V † U 2π V |−i = −a∗ ,
                                      s U 2π ,                          α−                        3
                                             3


(s, s0 signs). Recalling that the representation U ⊂ SU(2)      which is impossible, since e3i = ±1, for  6∈ {0, π}.
is faithful and U 32π = tI (t a sign), it is easy to verify
                    3
that the previous two conditions on U 2π 3
                                           , Uπ are satisfied   4.   Remaining presentations arising from Z2 , D2 and
respectively only if                                                                  D2 × Z2

   1. Uπ is diagonal;
                                                                  By the argument of Sec. A 3, any matrix of order 2 in
   2. Uπ is anti-diagonal.                                      O(3) is similar to
                                                                                                  
Multiplying by Av1 on the right the unitarity condition                                      s 0 0
associated to the difference v1 − v4                                               Ms,t := 0 s 0 ,
                                                                                             0 0 t
                  Av1 A†v4 + A−v4 A†−v1 = 0,
                                                                with s, t signs. Accordingly, up to conjugation, any three-
one also gets                                                   dimensional orthogonal representation of a group L ∈
                                                                {Z2 , D2 , D2 × Z2 } contains Ms,t . If s 6= t, any matrix N
                         Av1 A†v4 Av1 = 0,                      of order 2 in O(3) commuting with Ms,t is either Ms0 ,t0 ,
                                                                or of the form:
namely either A†v4 Av1 = 0 or Av1 A†v4 = 0. This implies                                                  
                                                                                        cos ϕ sin ϕ 0
that a) V † Uπ V is anti-diagonal or b) Uπ is anti-diagonal.
                                                                                 N =  sin ϕ − cos ϕ 0 ,
In case a), multiplying by Av1 on the right the unitarity
                                                                                          0       0      r
condition
                                                                with r a sign. Being the two dimensional block a re-
   Av1 A†v2 + A−v2 A†−v1 + Av5 A†v4 + A−v4 A†−v5 = 0,           flection matrix, there exists a similarity transformation
                                                                which maps it to ±σz (and leaving Ms,t invariant). Thus
it follows that
                                                                the real, orthogonal and three-dimensional faithful rep-
                                                                resentations of the groups here considered contain just
         Av1 A†v2 Av1 + A−v4 A†−v5 Av1 = 0;           (A20)
                                                                Ms,t and
in case b) multiplying by A†v1 on the right the unitarity                                  
                                                                                             r1 0 0
                                                                                                       
condition                                                                       Nr1 ,r2 :=  0 −r1 0  .
                                                                                             0 0 r2
 A†v1 Av2 + A†−v2 A−v1 + A†v5 Av4 + A†−v4 A−v5 = 0, (A21)
                                                                The problem reduces to combine signs in Ms,t , Nr1 ,r2 to
and taking the adjoint, it follows that                         give rise to faithful representations of L. It is easy to
                                                                check that they give rise to the integer lattice, the square
            Av1 A†v2 Av1 + A1 A†−v5 A−v4 = 0.         (A22)     lattice or the BCC lattice (one can include the inverses
                                                                or not). Nevertheless, there are two ways of providing a
Let us now pose
                                                                minimal generating set (namely such that S+ 6= S− ) for
                                                              Z3 and whose Cayley graph is associated with the BCC
                     †              a b
                   V U 2π V =               ,                   lattice. Such presentations are both generated by D2 :
                        3          −b∗ a∗
                                                                one is made with the vertices of a tetrahedron; the second
                                                                one corresponds to the vertices given by the following
where a 6= 0 since U 32π = tI. In case a), from (A20) one
                       3                                        vectors
then has                                                                                                      
                                                                          1            −1            −1               1
                 2
                α+                                                v0 =  1  , v1 = −1 , v2 =  1  , v3 = −1 .
                 2 ei = − h−| Uπ† U 2π Uπ |−i ,
                α−                    3                                   h            h              h               h
                                                                                                                                      15

We notice that excluding this solution allows us to ex-               to respect the D2 algebra, while the case A†−v3 Av0 =
clude the case including the inverses, namely S+ = S− .               Av0 A†−v2 = 0 is accounted by the symmetry of the uni-
   From the unitarity conditions one has:                             tarity conditions under the exchange 2 ↔ 3. In case 1,
                                                                      the condition is incompatible with a faithful representa-
    Av0 A†v1 Av0 = 0,                                       (A23)     tion of D2 in SU(2). In case 2, we have UG = iσG and
    Av0 A†−vi Av0 = 0, i = 2, 3,               (A24)                  U2 = V DV † with D diagonal, implying U2 = sV (iσ3 )V †
          †           †          †        †                           (s a sign). Then, up to a global sign, one has
    Av0 A−v1 + Av1 A−v0 + Av2 A−v3 + Av3 A−v2 = 0.
                                                            (A25)                                             
                                                                                               1           i s
                                                                                           V =√                  ,
From (A23) and the form of Eqs. (A9),(A10) for the                                              2         −s −i
transition matrices, we get U1 = iσ1 (we use the equiv-
alent notation for Pauli matrices: σ0 := I, σ1 := σX ,
                                                                      and from (A25) we obtain
σ2 := σY , σ3 := σZ ), up to a change of basis; from (A24)
we end up with the two cases:
                                                                                   Av0 A†−v1 Av0 + Av2 A†−v3 Av0 = 0,
   1. A†−v2 Av0 = A†−v3 Av0 = 0,

   2. A†−v2 Av0 = Av0 A†−v3 = 0,                                      which, using the form of Eqs. (A9),(A10) for the tran-
                                                                      sition matrices along with the previous results, leads to
since Av0 A†−v2 = Av0 A†−v3 = 0 is forbidden in order                 −2α+ 2
                                                                             α− = 0, contradicting the assumption α± 6= 0.




 [1] G. M. D’Ariano and P. Perinotti, Phys. Rev. A 90,                [17] A. Ambainis, E. Bach, A. Nayak, A. Vishwanath, and
     062106 (2014).                                                        J. Watrous, in Proceedings of the Thirty-third Annual
 [2] A. Ahlbrecht, A. Alberti, D. Meschede, V. B. Scholz,                  ACM Symposium on Theory of Computing, STOC ’01
     A. H. Werner, and R. F. Werner, New Journal of Physics                (ACM, New York, NY, USA, 2001) pp. 37–49.
     14, 073050 (2012).                                               [18] S. Severini, SIAM Journal on Matrix Analysis and Ap-
 [3] E. Zohar, J. I. Cirac, and B. Reznik, Phys. Rev. A 88,                plications 25, 295 (2003).
     023617 (2013).                                                   [19] P. Raynal, Phys. Rev. A 95, 062344 (2017).
 [4] D. González-Cuadra, E. Zohar, and J. I. Cirac, New              [20] J. Meier, Groups, Graphs and Trees (Cambridge Univer-
     Journal of Physics 19, 063038 (2017).                                 sity Press, 2008) Cambridge Books Online.
 [5] K. Stannigel, P. Hauke, D. Marcos, M. Hafezi, S. Diehl,          [21] A. Montanaro, Quantum Information and Computation
     M. Dalmonte, and P. Zoller, Phys. Rev. Lett. 112,                     7, 093 (2007).
     120406 (2014).                                                   [22] J. Kempe, Contemporary Physics 44, 307 (2003).
 [6] P. Arnault, G. Di Molfetta, M. Brachet, and F. Deb-              [23] The homogeneity requirement defined in Ref. [1] should
     basch, Phys. Rev. A 94, 012335 (2016).                                be completed upon requiring that any two nodes remain
 [7] P. Arrighi, S. Facchini, and M. Forets, New Journal of                “distinguishable” from the point of view of a third node.
     Physics 16, 093007 (2014).                                            For details we will refer to Ref. [31]. Eq. (2) follows from
 [8] P. Arrighi, S. Facchini, and M. Forets, Quantum Infor-                this definition.
     mation Processing 15, 3467 (2016).                               [24] A. Bisio, G. M. D’Ariano, M. Erba, P. Perinotti, and
 [9] I. Siloi, C. Benedetti, E. Piccinini, J. Piilo, S. Maniscalco,        A. Tosini, Phys. Rev. A 93, 062334 (2016).
     M. G. A. Paris, and P. Bordone, Phys. Rev. A 95, 022106          [25] G. Mackiw, Mathematics Magazine 69, 356 (1996).
     (2017).                                                          [26] K.-I. Tahara, Nagoya Mathematical Journal 41, 169
[10] A. Bisio, G. M. D’Ariano, and P. Perinotti, Annals of                 (1971).
     Physics 368, 177 (2016).                                         [27] This is straightforward as far as Zn and Dn are con-
[11] A. Bisio, G. M. D’Ariano, and P. Perinotti, Phys. Rev.                cerned; as for A4 and S4 , one can verify it in a direct
     A 94, 042120 (2016).                                                  way considering their faithful representations given in
[12] R. P. Feynman, International Journal of Theoretical                   Secs. A 1 a and A 1 b.
     Physics 21, 467 (1982).                                          [28] We follow the argument of Ref. [32]. The condition
[13] J. Watrous, in Foundations of Computer Science, 1995.                 A†h A−h = 0 implies that Vh V−h        †
                                                                                                                      is diagonal in the
     Proceedings., 36th Annual Symposium on (IEEE, 1995)                   basis {|η+h i, |η−h i}. Since the transition matrices are
     pp. 528–537.                                                          not full rank, their polar decomposition is not unique:
[14] B. Schumacher and R. F. Werner, arXiv preprint quant-                 Vh (|η+h ihη+h | + eiθh |η−h ihη−h |) gives the same polar de-
     ph/0405174 (2004).                                                    composition as Vh ∀h ∈ S. Accordingly, one can tune the
                                                                                                          †
[15] P. Arrighi, V. Nesme, and R. Werner, Journal of Com-                  phases θ±h to choose Vh V−h      = I ∀h ∈ S.
     puter and System Sciences 77, 372 (2011), adaptivity in          [29] R. Koo, Mathematics magazine 76, 143 (2003).
     Heterogeneous Environments.                                      [30] One has A−v2 A†−v1 Av1 = 0 since A†−v1 Av1 = 0, and
[16] Y. Aharonov, L. Davidovich, and N. Zagury, Phys. Rev.                 Av4 A†v3 Av1 = 0, since A†v3 Av1 = R2 A†v1 R2† Av1 and
     A 48, 1687 (1993).
                                                                           A†v1 R2 Av1 = α+    2
                                                                                                 |+i h+| V † R2 V |+i h+|, and by Eq.
                                                                                                                16

     (A17) h+| V † R2 V |+i = 0.                             Journal of Physics A: Mathematical and Theoretical 50,
[31] G. M. D’Ariano and P. Perinotti, Unpublished.           035301 (2017).
[32] G. M. D’Ariano, M. Erba, P. Perinotti, and A. Tosini,

```

### Contexto adjunto: scripts/verify_weyl_dirac_gate.py
```
"""Exact, fail-closed checks for the frozen standard Pavia Weyl/Dirac gate."""

import argparse
import hashlib
import itertools
from pathlib import Path
import platform
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "reports/2026-09-14--weyl-dirac-gate-contract.md"
SOURCE = ROOT / "sources/1601.04832v1.pdf"
SOURCE_SHA256 = "0dbf0a0bea497701e0408ce410d62ca0183a4aa14b4116254d029ff6602f1367"
IDENTITY = sp.eye(2)
PAULI = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.diag(1, -1),
)
MASS, HOP = sp.symbols("m n", positive=True)
CHECKS = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def residual(expression):
    return sp.cancel(sp.expand(expression).subs(HOP**2, 1 - MASS**2))


def check_zero(label, expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    for entry in entries:
        remaining = residual(entry)
        if remaining != 0:
            raise ValueError(f"{label}: nonzero or unresolved residual {remaining}")
    CHECKS.append(label)


def check_equal(label, actual, expected):
    if actual != expected:
        raise ValueError(f"{label}: {actual!r} != {expected!r}")
    CHECKS.append(label)


def laurent_adjoint(matrix, variables):
    return matrix.H.subs({variable: 1 / variable for variable in variables}, simultaneous=True)


def published_symbol(dimension, chirality, variables):
    cosines = [(variable + 1 / variable) / 2 for variable in variables]
    sines = [(variable - 1 / variable) / (2 * sp.I) for variable in variables]
    if dimension == 1:
        scalar = cosines[0]
        vector = (0, 0, sines[0])
    elif dimension == 2:
        cos_x, cos_y = cosines
        sin_x, sin_y = sines
        scalar = cos_x * cos_y
        vector = (sin_x * cos_y, cos_x * sin_y, sin_x * sin_y)
    else:
        cos_x, cos_y, cos_z = cosines
        sin_x, sin_y, sin_z = sines
        scalar = cos_x * cos_y * cos_z + chirality * sin_x * sin_y * sin_z
        vector = (
            sin_x * cos_y * cos_z - chirality * cos_x * sin_y * sin_z,
            -chirality * cos_x * sin_y * cos_z - sin_x * cos_y * sin_z,
            cos_x * cos_y * sin_z - chirality * sin_x * sin_y * cos_z,
        )
    matrix = scalar * IDENTITY
    for component, pauli in zip(vector, PAULI):
        matrix -= sp.I * component * pauli
    return matrix.applyfunc(sp.expand), sp.expand(scalar)


def rotation_product(dimension, chirality, variables):
    axes = (2,) if dimension == 1 else tuple(range(dimension))
    signs = (1, -chirality, 1) if dimension == 3 else (1,) * dimension
    matrix = IDENTITY
    for variable, axis, sign in zip(variables, axes, signs):
        positive = (IDENTITY - sign * PAULI[axis]) / 2
        negative = (IDENTITY + sign * PAULI[axis]) / 2
        matrix = matrix * (variable * positive + negative / variable)
    return matrix.applyfunc(sp.expand)


def fourier_support(matrix, variables):
    shift = sp.prod(variables)
    coefficients = {}
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            polynomial = sp.Poly(sp.expand(shift * matrix[row, column]), *variables)
            for powers, coefficient in polynomial.terms():
                displacement = tuple(1 - power for power in powers)
                coefficients.setdefault(displacement, sp.zeros(matrix.rows, matrix.cols))
                coefficients[displacement][row, column] += coefficient
    return {
        displacement: coefficient
        for displacement, coefficient in coefficients.items()
        if any(sp.expand(entry) != 0 for entry in coefficient)
    }


def hull_geometry(support, dimension):
    vertices = [sp.Matrix(displacement) / sp.sqrt(dimension) for displacement in support]
    facets = set()
    for selected in itertools.combinations(vertices, dimension):
        differences = sp.Matrix(dimension - 1, dimension, lambda row, column:
                                selected[row + 1][column] - selected[0][column])
        normals = differences.nullspace()
        if len(normals) != 1:
            continue
        normal = normals[0]
        offset = normal.dot(selected[0])
        if offset == 0:
            continue
        normalized = normal / offset
        distances = [sp.simplify(normalized.dot(vertex) - 1) for vertex in vertices]
        if all(distance <= 0 for distance in distances):
            facets.add(tuple(normalized))
    if not facets:
        raise ValueError("Hull has no certified facets")
    inradius = min(sp.simplify(1 / sp.sqrt(sum(value**2 for value in facet)))
                   for facet in facets)
    maximum = max(sp.sqrt(vertex.dot(vertex)) for vertex in vertices)
    return inradius, maximum, len(facets)


def spatial_derivative(expression, variable, dimension):
    return sp.I * variable * sp.diff(expression, variable) / sp.sqrt(dimension)


def verify_case(dimension, chirality, transpose):
    suffix = ("+" if chirality == 1 else "-") if dimension == 3 else ""
    name = f"d={dimension} {'B' if transpose else 'A'}{suffix}"
    variables = sp.symbols(f"z0:{dimension}", real=True, nonzero=True)
    matrix, scalar = published_symbol(dimension, chirality, variables)
    product = rotation_product(dimension, chirality, variables)
    if transpose:
        matrix, product = matrix.T, product.T
    check_zero(f"{name}: published vs product", matrix - product)
    adjoint = laurent_adjoint(matrix, variables)
    check_zero(f"{name}: Weyl unitarity", matrix * adjoint - IDENTITY)
    check_zero(f"{name}: Weyl quadratic", matrix**2 - 2 * scalar * matrix + IDENTITY)
    check_zero(f"{name}: scalar trace", sp.trace(matrix) - 2 * scalar)
    support = fourier_support(matrix, variables)
    corners = set(itertools.product((-1, 1), repeat=dimension))
    check_equal(f"{name}: active support", set(support), corners)
    inradius, maximum, facets = hull_geometry(support, dimension)
    check_zero(f"{name}: inradius", inradius - 1 / sp.sqrt(dimension))
    check_zero(f"{name}: maximum support", maximum - 1)
    check_equal(f"{name}: facets", facets, 2 * dimension)
    origin = dict.fromkeys(variables, 1)
    check_zero(f"{name}: zero node", matrix.subs(origin) - IDENTITY)
    spatial = [sp.I * spatial_derivative(matrix, variable, dimension).subs(origin)
               for variable in variables]
    for first, first_variable in enumerate(variables):
        check_zero(f"{name}: scalar gradient {first}",
                   spatial_derivative(scalar, first_variable, dimension).subs(origin))
        for second, second_variable in enumerate(variables):
            expected = sp.Rational(int(first == second), dimension)
            check_zero(f"{name}: Clifford {first},{second}",
                       spatial[first] * spatial[second] + spatial[second] * spatial[first]
                       - 2 * expected * IDENTITY)
            hessian = spatial_derivative(
                spatial_derivative(scalar, first_variable, dimension), second_variable, dimension)
            check_zero(f"{name}: Hessian {first},{second}", hessian.subs(origin) + expected)
    speed = sp.sqrt(sp.simplify(sp.trace(spatial[0]**2) / 2))
    check_zero(f"{name}: massless matching", speed - inradius)
    dirac = sp.BlockMatrix([[HOP * matrix, sp.I * MASS * IDENTITY],
                           [sp.I * MASS * IDENTITY, HOP * adjoint]]).as_explicit()
    if dimension == 1:
        permutation = (0, 2, 3, 1)
        reduced = sp.Matrix([[HOP / variables[0], sp.I * MASS],
                             [sp.I * MASS, HOP * variables[0]]])
        check_zero(f"{name}: minimal Dirac blocks",
                   dirac.extract(permutation, permutation) - sp.diag(reduced, reduced))
    dirac_adjoint = laurent_adjoint(dirac, variables)
    check_zero(f"{name}: Dirac unitarity", dirac * dirac_adjoint - sp.eye(4))
    check_zero(f"{name}: Dirac quadratic", dirac**2 - 2 * HOP * scalar * dirac + sp.eye(4))
    check_zero(f"{name}: Dirac trace", sp.trace(dirac) - 4 * HOP * scalar)
    sine_part = sp.I * (dirac - dirac_adjoint) / 2
    check_zero(f"{name}: logarithm algebra",
               sine_part**2 - (1 - HOP**2 * scalar**2) * sp.eye(4))
    check_equal(f"{name}: massive support", set(fourier_support(dirac, variables)),
                corners | {(0,) * dimension})
    check_equal(f"{name}: massless Dirac support",
                set(fourier_support(dirac.subs({MASS: 0, HOP: 1}), variables)), corners)
    check_equal(f"{name}: decoupled support",
                set(fourier_support(dirac.subs({MASS: 1, HOP: 0}), variables)), {(0,) * dimension})
    return name, len(support), facets, sp.sstr(inradius), sp.sstr(maximum), sp.sstr(speed)


def verify_mass_coefficients():
    scalar_argument = sp.Symbol("u", real=True)
    gap = sp.Symbol("M", positive=True)
    phase = sp.acos(HOP * scalar_argument)
    prefactor = phase / sp.sqrt(1 - HOP**2 * scalar_argument**2)

    def at_origin(expression):
        expression = expression.subs(scalar_argument, 1).subs(HOP, sp.sqrt(1 - MASS**2))
        expression = sp.simplify(expression)
        return expression.subs(sp.acos(sp.sqrt(1 - MASS**2)), gap)

    hopping = sp.sqrt(1 - MASS**2)
    ratio = gap * hopping / MASS
    check_zero("fixed-mass logarithm prefactor", at_origin(prefactor) - gap / MASS)
    for dimension in (1, 2, 3):
        speed_squared = sp.Rational(1, dimension)
        phase_coefficient = at_origin(sp.diff(phase**2, scalar_argument)) * (-speed_squared / 2)
        check_zero(f"d={dimension}: phase curvature", phase_coefficient - speed_squared * ratio)
        mass_curvature = MASS * at_origin(sp.diff(prefactor, scalar_argument)) * (-speed_squared / 2)
        expected_curvature = speed_squared * hopping * (1 - ratio) / (2 * MASS)
        check_zero(f"d={dimension}: quadratic mass term", mass_curvature - expected_curvature)
        check_zero(f"d={dimension}: independent H-squared curvature",
                   speed_squared * ratio**2 + 2 * gap * mass_curvature - phase_coefficient)
    mass_ratio = ratio.subs(gap, sp.asin(MASS))
    check_zero("c_H small-mass series", sp.series(mass_ratio, MASS, 0, 6).removeO()
               - (1 - MASS**2 / 3 - 2 * MASS**4 / 15))
    check_zero("c_omega2 small-mass series", sp.series(sp.sqrt(mass_ratio), MASS, 0, 6).removeO()
               - (1 - MASS**2 / 6 - 29 * MASS**4 / 360))
    check_zero("small-mass ratio limit", sp.limit(mass_ratio, MASS, 0, dir="+") - 1)
    angle = sp.Symbol("angle", real=True)
    check_zero("strict-bound derivative identity",
               sp.diff(sp.sin(angle) - angle * sp.cos(angle), angle) - angle * sp.sin(angle))
    check_zero("strict-bound zero endpoint", (sp.sin(angle) - angle * sp.cos(angle)).subs(angle, 0))


def verify_negative_controls():
    weyl = sp.diag(-sp.I, sp.I)
    bad_dirac = sp.BlockMatrix([[sp.Rational(4, 5) * weyl, sp.I * sp.Rational(3, 5) * IDENTITY],
                               [sp.I * sp.Rational(3, 5) * IDENTITY, sp.Rational(4, 5) * weyl]]).as_explicit()
    check_equal("negative control: missing dagger detected",
                bad_dirac * bad_dirac.H != sp.eye(4), True)
    variables = sp.symbols("z0:3", real=True, nonzero=True)
    matrix, scalar = published_symbol(3, 1, variables)
    wrong_scalar = published_symbol(3, -1, variables)[1]
    check_equal("negative control: reversed phase sign detected",
                residual(sp.trace(matrix) / 2 - wrong_scalar) != 0, True)
    momentum = sp.Symbol("momentum", real=True)
    phase = sp.acos(sp.cos(momentum) / sp.sqrt(2))
    dispersion_coefficient = sp.simplify(sp.diff(phase**2, momentum, 2).subs(momentum, 0) / 2)
    hamiltonian_coefficient = sp.simplify((phase / sp.sin(phase)).subs(momentum, 0) / sp.sqrt(2))
    discrepancy = sp.simplify(dispersion_coefficient - hamiltonian_coefficient**2)
    check_zero("negative control: exact finite-mass discrepancy",
               discrepancy - sp.pi * (4 - sp.pi) / 16)
    check_equal("negative control: missing quadratic mass term detected", discrepancy != 0, True)


def verify_vertex_idempotency():
    """Addendum (2026-09-14): exact non-nilpotency certificate for every
    d=3 corner coefficient A_h, reusing published_symbol/fourier_support.
    This is the algebraic input for the strict-asymptotic-body baseline
    certificate; see reports/2026-09-14--strict-asymptotic-pavia-baseline.md.
    Governed by no separate contract; it only extracts and checks exact
    identities already reachable from the frozen d=3 factorization."""
    positive_generators = {(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)}
    alpha_plus = sp.Rational(1, 4) * (1 - sp.I)
    alpha_minus = sp.Rational(1, 4) * (1 + sp.I)
    rows = []
    for chirality in (1, -1):
        own, other = (alpha_plus, alpha_minus) if chirality == 1 else (alpha_minus, alpha_plus)
        for transpose in (False, True):
            suffix = "+" if chirality == 1 else "-"
            name = f"d=3 {'B' if transpose else 'A'}{suffix}"
            variables = sp.symbols("z0:3", real=True, nonzero=True)
            matrix, _ = published_symbol(3, chirality, variables)
            if transpose:
                matrix = matrix.T
            support = fourier_support(matrix, variables)
            for h in sorted(support):
                coefficient = support[h]
                expected = own if h in positive_generators else other
                check_zero(f"{name}: vertex {h} rank-one (det A_h=0)", coefficient.det())
                check_zero(f"{name}: vertex {h} trace A_h={sp.nsimplify(expected)}",
                           sp.trace(coefficient) - expected)
                check_zero(f"{name}: vertex {h} A_h^2=alpha*A_h",
                           coefficient * coefficient - expected * coefficient)
                check_equal(f"{name}: vertex {h} nonzero eigenvalue alpha", expected != 0, True)
                rows.append((name, str(h), sp.sstr(expected)))
    return rows


def run():
    CHECKS.clear()
    check_equal("source PDF SHA256", digest(SOURCE), SOURCE_SHA256)
    rows = []
    for dimension in (1, 2, 3):
        chiralities = (1, -1) if dimension == 3 else (0,)
        transposes = (False,) if dimension == 1 else (False, True)
        for chirality, transpose in itertools.product(chiralities, transposes):
            rows.append(verify_case(dimension, chirality, transpose))
    verify_mass_coefficients()
    verify_negative_controls()
    vertex_rows = verify_vertex_idempotency()
    lines = [
        "# Weyl/Dirac exact verification record", "",
        f"Result: PASS — {len(CHECKS)} exact checks; zero tolerance; seven Weyl symbols and their Dirac couplings.",
        "", "This is a local verification record, not a canonical status update.", "",
        f"Python: {platform.python_version()}; SymPy: {sp.__version__}.", "",
        "| Case | Weyl neighbors | Facets | r_in | V_causal^max | c_0 |",
        "| --- | ---: | ---: | --- | --- | --- |",
    ]
    lines.extend("| " + " | ".join(map(str, row)) + " |" for row in rows)
    lines.extend([
        "", "For each row and 0<m<1: M=asin(m), F=M*sqrt(1-m^2)/m;",
        "c_H=c_0*F and c_omega2=c_0*sqrt(F). Analytically 0<F<1.",
        "At m=0 both equal r_in (EXACT); at fixed 0<m<1 both equalities",
        "with r_in are FALSE; matching as m tends to zero is ASYMPTOTIC.",
        "", "At m=1 active support is {0}; all spatial coefficients and its inradius",
        "are zero. The limiting ratio to the nonzero-mass substrate inradius is not",
        "an inradius ratio for that collapsed active body.", "",
        "Negative controls: missing dagger, reversed phase sign, omitted quadratic mass term detected.",
        "Interval proof, continuum scaling and convention limits: see the analytic report.", "",
        "## Addendum: d=3 vertex non-nilpotency certificate (2026-09-14)", "",
        "For every one-step corner h in {-1,1}^3/sqrt(3) and every d=3 case,",
        "det(A_h)=0 and A_h^2=alpha*A_h with alpha in {(1-i)/4,(1+i)/4}, alpha!=0",
        "(exact). Hence each A_h is rank-one and not nilpotent, so",
        "A_h^n=alpha^(n-1)*A_h != 0 for every n>=1. See",
        "reports/2026-09-14--strict-asymptotic-pavia-baseline.md for the",
        "convexity argument that turns this into C_infty^strict=C_micro for this",
        "baseline. Baseline-specific; not a claim about other admissible symbols.",
        "", "| Case | Vertex h | alpha |", "| --- | --- | ---: |",
    ])
    lines.extend(f"| {name} | {h} | {alpha} |" for name, h, alpha in vertex_rows)
    lines.extend([
        "",
        "## Provenance", "",
        f"- Script SHA256: `{digest(Path(__file__))}`",
        f"- Contract SHA256: `{digest(CONTRACT)}`",
        f"- 1601.04832v1 PDF SHA256: `{digest(SOURCE)}`",
        "- Weyl input: https://arxiv.org/abs/1601.04832v1, equations (15)-(17).",
        "- Dirac dagger cross-check: https://arxiv.org/html/1601.04842v1#S2.E9.",
        "- Baseline: 44ad178; fixed cases and semantics are specified by the contract.",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the record only after all checks pass.")
    arguments = parser.parse_args()
    try:
        record = run()
    except (ValueError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if arguments.output:
        arguments.output.write_text(record, encoding="utf-8")
        print(f"PASS: {len(CHECKS)} exact checks; wrote {arguments.output}")
    else:
        print(record, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### Contexto adjunto: theory/CAUSAL_BODY_GEOMETRY.md
```
# CAUSAL_BODY_GEOMETRY

## 1. Finite-range lattice locality

Let `N = {n_1, ..., n_m}` be the finite set of one-step lattice displacements allowed by locality. Ignoring internal amplitudes, repeated paths after `Nstep` steps lie in the Minkowski sum of the one-step support. After dividing by the number of steps, the asymptotic geometric velocity body is the convex hull

`C_micro = conv(N)`

up to the physical scale `a/Δt` (or the appropriate anisotropic coordinate scales).

For finite `N`, `C_micro` is a polytope.

## 2. Support function

For a unit direction `n̂`,

`h_C(n̂) = sup_{v in C_micro} n̂·v`.

The convex body can be recovered as

`C_micro = intersection over n̂ of {v : n̂·v <= h_C(n̂)}`.

Define

`r_in(C_micro) = min_{||n̂||=1} h_C(n̂)`

when the origin and Euclidean norm are fixed by the same velocity coordinates used for the proposed isotropic IR cone.

Also define

`V_causal^max = max_{||n̂||=1} h_C(n̂)`.

## 3. Isotropic IR containment lemma

Suppose an isotropic low-energy causal ball

`B(c_IR) = {v : ||v||_2 <= c_IR}`

must be contained in `C_micro`.

Then for every unit `n̂`,

`c_IR <= h_C(n̂)`.

Hence

`c_IR <= min h_C = r_in(C_micro)`.

If `C_micro` is anisotropic, then

`min h_C < max h_C`,

so

`c_IR < V_causal^max`.

This rules out identifying an isotropic `c_IR` with the largest directional microscopic speed in an anisotropic causal body.

## 4. Three old saturation statements

- `B_max`: `c_IR = V_causal^max`.
- `B_full`: `B(c_IR) = C_micro`.
- `B_touch`: `∂B(c_IR)` intersects `∂C_micro`.

For an anisotropic `C_micro`, `B_max` is impossible under isotropic containment.

For finite-range lattice QCA in `d >= 2`, exact `B_full` is impossible because `C_micro` is a finite polytope whereas a nondegenerate Euclidean ball is not.

`B_touch` can still hold and, for a centered isotropic ball, corresponds to

`c_IR = r_in(C_micro)`.

Tangency is therefore much weaker than “`c` is the fastest speed of the substrate.”

## 5. Scope of the lemma

The statement is geometric. It assumes:

- a fixed embedding/velocity coordinate system;
- a Euclidean isotropic IR cone in those coordinates;
- containment of the IR velocity ball inside the microscopic causal body.

Changing coordinates or the norm changes the numerical inradius. Therefore every comparison must freeze the physical embedding before computing `r_in`.

## 6. Strict asymptotic support and `c_strict^iso` (added 2026-09-14)

`C_micro = conv(N)` is the *one-step* body: it only records which average velocities are compatible with a single update. It says nothing about whether a given direction is actually reachable arbitrarily far after repeated coarse-graining in time — that depends on whether the relevant Fourier coefficients survive under repeated multiplication, not on `N` alone.

For a homogeneous step `U(k) = sum_h e^{-ik.h} T_h` and `n >= 1`, let

`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`.

Define the **strict asymptotic support function**

`h_infty(n̂) = limsup_{n->infty} (1/n) max_{x in S_n} n̂.x`,

and, with the origin fixed at the physically privileged rest point `v = 0`,

`c_strict^iso = min_{||n̂||=1} h_infty(n̂)`.

Since `S_n/n subseteq C_micro` for every `n` (each one-step displacement lies in `C_micro` by definition), `h_infty(n̂) <= h_C(n̂)` for every `n̂`, hence

`c_strict^iso <= r_in(C_micro)`.

This is the exact and general relation between the two objects: `r_in(C_micro)` is a provable *upper bound* on the strict asymptotic isotropic speed, not a definition of it, and the two need not coincide. A pure one-step shift by `h_0 != 0` (`S_n = {n h_0}`) gives `h_infty(n̂) = n̂.h_0` and `min_{n̂} h_infty(n̂) = -||h_0|| < 0`: there is no bidirectional isotropic cone centered at `v=0` at all, which "inradius" language silently assumes. Do not call `c_strict^iso` an inradius except where a separate argument shows the relevant body is centered and `c_strict^iso = r_in(C_micro)` exactly.

The live hypothesis built on this object, `B_infty^*`, and the exact d=3 Pavia baseline in which `c_strict^iso = r_in(C_micro) = 1/sqrt(3)` is certified (not merely bounded), are in [`B_STAR_HYPOTHESIS.md`](B_STAR_HYPOTHESIS.md) and
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
```


