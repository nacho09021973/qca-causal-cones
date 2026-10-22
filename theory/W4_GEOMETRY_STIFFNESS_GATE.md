# W4_GEOMETRY_STIFFNESS_GATE

> **Typographic reconstruction — 2026-10-22.** The frozen text is commit `d4bcadf`.
> It lost its LaTeX backslashes through an escape layer
> (`reports/2026-10-22--escape-corruption-audit.md`). The delimiters and commands
> have been restored by hand. `scripts/check_reconstruction.py` certifies that only
> backslashes were added. The formulas were checked against
> `scripts/verify_w4_geometry_stiffness.py`. The contract remains the version
> frozen at `d4bcadf`.

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to:

```
W3_BACKREACTING_TETRAD_PASS / CURVATURE_DYNAMICS_OPEN
W3_CURVATURE_DYNAMICS_GATE =
COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL
```

The W3 failure C3 was specific: no geometry-only propagation/stiffness term
was present.

W4 may add a geometry-only local unitary, but must leave the W3 matter/tetrad
coupling unchanged.

## 1. Geometry lattice

Retain one geometry qubit on each declared W3 edge register. For a fixed W3
edge family \(a\), identify its parallel copies by the starting vertex
\(x\in\mathbb Z^3\).

For each coordinate direction \(j=1,2,3\), define neighboring geometry
registers

\[
e=(a,x),\qquad f=(a,x+\hat e_j).
\]

No vertex creation/destruction is introduced.

## 2. Geometry-only exchange gate

Let \(S_{ef}\) be the SWAP operator between geometry qubits \(e,f\). Define

\[
K_{ef}(\kappa)
=
\exp[-i\kappa(I-S_{ef})].
\]

Since \(S_{ef}=S_{ef}^\dagger=S_{ef}^{-1}\), each \(K_{ef}\) is exactly
unitary.

For each coordinate direction, split geometry-neighbor pairs by parity of
\(x_j\), giving two matchings. All W3 edge families can be updated in
parallel because they use distinct qubits.

Thus the geometry-only update has at most six matching layers.

Call their ordered product \(K_\kappa\).

## 3. Complete W4 step

Retain the W3 interaction \(V_g\) and the CJWW matter step \(U_0\). Define

\[
U_{g,\kappa}
=
K_\kappa\,V_g\,(I_g\otimes U_0).
\]

At \(g=0\), matter remains exactly CJWW regardless of \(\kappa\), because
\(K_\kappa\) acts on geometry only.

## 4. Obligations

### W4.1 exact local unitarity / bounded depth

Prove the geometry-only update is exactly unitary, bounded-range and
finite-depth independent of system size.

### W4.2 homogeneous background stability

For the W3 reference single-qubit state

\[
|n_0\rangle,\qquad
\langle X\rangle=\sin\theta,\;
\langle Y\rangle=0,\;
\langle Z\rangle=\cos\theta,
\]

prove

\[
K_\kappa |n_0\rangle^{\otimes E}
=
|n_0\rangle^{\otimes E}
\]

exactly (up to at most a global phase).

### W4.3 autonomous geometry propagation

With matter absent/decoupled, exhibit two geometry registers \(e,f\) and an
initial local defect for which \(K_{ef}\) changes the expectation of the
tetrad-control observable \(Z_f\).

This must not use any matter operator.

### W4.4 repeated propagation

Show that brickwork composition can move/spread a local geometry defect over
arbitrarily many geometry-neighbor steps with a finite maximum propagation
speed.

### W4.5 curvature linkage

Use the already established W3 coarse metric to show that a spatial texture
of \(z_e=\langle Z_e\rangle\) with nonzero coarse curvature can evolve under
\(K_\kappa\) even when the matter source is zero.

This is a curvature-dynamics statement only at the kinematic/coarse-field
level.

### W4.6 source remains separate

Do not repair W3 C4 inside this gate. Endpoint occupation is still not a
derived stress-energy tensor.

## 5. Terminal states

1. `W4_GEOMETRY_STIFFNESS_FAIL`.
2. `W4_AUTONOMOUS_GEOMETRY_DYNAMICS_PASS / GRAVITATIONAL_SOURCE_OPEN`.
3. `OPEN_AFTER_AUDIT`.

## 6. Claim ceiling

Passing W4 does not establish Einstein equations, a massless spin-2 mode,
diffeomorphism symmetry, an Einstein-Hilbert action, Newton's constant,
AdS/CFT, or an absolute scale.

The result would be only: the same microscopic variables that control the
matter tetrad have a local autonomous vacuum dynamics and can transport
coarse curvature information.
