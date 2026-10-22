# W4_GEOMETRY_STIFFNESS_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W4_GEOMETRY_STIFFNESS_GATE](../theory/W4_GEOMETRY_STIFFNESS_GATE.md), frozen at commit `d4bcadf9e41ead03d3004607a48d46c1db5e6291`.  
**Certificado simbólico:** [verify_w4_geometry_stiffness.py](../scripts/verify_w4_geometry_stiffness.py), added at commit `3099bd5d06ea4395292489889f7324f79f48d405`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W4_GEOMETRY_STIFFNESS_GATE =
W4_AUTONOMOUS_GEOMETRY_DYNAMICS_PASS / GRAVITATIONAL_SOURCE_OPEN

COARSE_CURVATURE_PROPAGATION = PASS_IN_LINEARIZED_KINEMATIC_SENSE
EINSTEIN_STRUCTURE = OPEN
GRAVITATIONAL_NORMALIZATION_G1 = NOT_OPENED
```

W4 repairs the W3 C3 failure by adding a local geometry-only exchange
subdynamics acting on the same link variables whose (Z) expectations control
the W3 tetrad.

## 1. Exact geometry-only local unitary

For neighboring geometry registers (e,f), let (S_{ef}) be SWAP and define

[
K_{ef}(kappa)=e^{-ikappa(I-S_{ef})}.
]

Since (S_{ef}=S_{ef}^dagger=S_{ef}^{-1}), the generator is Hermitian and
(K_{ef}) is exactly unitary.

Using

[
S_{ef}
=
\frac12
left(
I+X_eX_f+Y_eY_f+Z_eZ_f
\right),
]

the generator is a standard exchange/stiffness operator,

[
I-S_{ef}
=
\frac12
left(
I-X_eX_f-Y_eY_f-Z_eZ_f
\right).
]

No matter operator appears.

## 2. Finite-depth implementation

For each W3 edge family (a) and each coordinate direction (j), pair
parallel edge registers based at (x) and (x+hat e_j).

Splitting each coordinate-direction pairing by parity of (x_j) gives two
matchings. Different W3 edge families act on disjoint geometry registers and
can be updated in parallel.

Thus the geometry-only brickwork has depth at most

[
\boxed{6}
]

independent of system size.

The complete W4 step is

[
U_{g,kappa}
=
K_kappa,V_g,(I_gotimes U_0).
]

At (g=0), matter remains exactly CJWW because (K_kappa) acts only on
geometry.

[
\boxed{\texttt{W4.1 = PASS}.}
]

## 3. Homogeneous W3 background is exactly stationary under K

Let every geometry qubit be in the same state (|n_0\rangle), including the
W3 reference state with Bloch vector
((sin\theta,0,cos\theta)).

For every neighboring pair,

[
S_{ef}|n_0,n_0\rangle=|n_0,n_0\rangle,
]

hence

[
(I-S_{ef})|n_0,n_0\rangle=0
]

and

[
K_{ef}(kappa)|n_0,n_0\rangle=|n_0,n_0\rangle.
]

Therefore

[
\boxed{
K_kappa|n_0\rangle^{otimes E}
=
|n_0\rangle^{otimes E}
}
]

exactly, with no background drift.

[
\boxed{\texttt{W4.2 = PASS}.}
]

## 4. Autonomous propagation of the tetrad-control variable

For one neighboring geometry pair start from

[
|1,0\rangle.
]

Because (S|1,0\rangle=|0,1\rangle),

[
K_{ef}(kappa)|1,0\rangle
=
e^{-ikappa}
left[
coskappa,|1,0\rangle
+
isinkappa,|0,1\rangle
\right].
]

Thus

[
langle Z_e\rangle=-cos2kappa,
qquad
langle Z_f\rangle=cos2kappa.
]

Initially these were ((-1,+1)). For generic nonzero (kappa), both change
without any matter present.

At

[
kappa=\frac{pi}{2},
]

the defect transfers completely from (e) to (f).

Therefore the same variable

[
z_e=langle Z_e\rangle
]

that controls the W3 principal symbol now has an autonomous local propagation
law.

[
\boxed{\texttt{W4.3 = PASS}.}
]

## 5. Repeated finite-speed geometry propagation

The geometry update is a bounded-depth nearest-neighbor brickwork on the
lattice of parallel edge registers.

After one matching layer, a local geometry disturbance can move by at most one
geometry-neighbor bond. After (m) layers it is supported only within graph
distance (m) of its initial geometry register.

Conversely, for any (0<|sinkappa|le1), successive partial-SWAP factors
give nonzero amplitudes along allowed brickwork paths. At
(kappa=pi/2), the update reduces locally to complete swaps, giving an
explicit deterministic transport witness along the scheduled matching path.

Hence W4 has a finite microscopic geometry-propagation speed and permits
arbitrarily long vacuum transport under repeated steps.

[
\boxed{\texttt{W4.4 = PASS}.}
]

## 6. Link to the W3 coarse curvature

W3 established, for example, that a texture

[
z_1=f(x_2),qquad z_2=z_3=0
]

has linearized spatial scalar curvature

[
R^{(1)}=-4g,partial_2^2 z_1.
]

Use the discrete second difference

[
Delta_2 z_n=z_{n+1}-2z_n+z_{n-1}
]

as the lattice linearized-curvature witness.

Take a one-link (Z)-defect along the (x_2) geometry chain:

[
z_n=
\begin{cases}
-1,&n=0,\\
+1,&n
e0.
end{cases}
]

Initially,

[
Delta_2 z_0=4.
]

After a geometry-only partial-SWAP between registers (0) and (1),

[
z_0=-cos2kappa,qquad
z_1=cos2kappa,
]

while the untouched neighbors remain (+1).

Thus the discrete curvature pattern changes. At
(kappa=pi/2), the (Z)-defect and its associated second-difference
curvature pattern move one geometry bond.

No matter operation is used in this evolution.

Therefore W4 supplies autonomous propagation of the coarse curvature
information already defined kinematically in W3.

[
\boxed{\texttt{W4.5 = PASS}}
]

within the explicitly limited linearized/coarse-field meaning.

## 7. Source remains open

W4 deliberately does not change the W3 matter source.

The backreaction kick still uses endpoint occupation

[
a_e=langle A_e\rangle,
]

and no derivation identifies this with the conserved stress-energy tensor of
the continuum Weyl theory.

Therefore:

[
\boxed{\texttt{GRAVITATIONAL_SOURCE = OPEN}.}
]

This preserves the earlier W3 C4 failure.

## 8. What W4 has achieved

The model now contains, at the declared perturbative/coarse level,

[
\text{matter}
longrightarrow
\text{tetrad control }z_e
longrightarrow
\text{matter cone},
]

together with

[
\text{tetrad control }z_e
longrightarrow
\text{geometry-only local propagation}
longrightarrow
\text{evolving coarse curvature}.
]

In particular, the geometry sector is no longer frozen in vacuum.

This repairs the specific W3 C3 obstruction.

## 9. What is still absent

W4 does **not** establish:

- a relativistic or spin-2 geometry mode;
- the Einstein constraint structure;
- a stress-energy source;
- local Lorentz or diffeomorphism gauge symmetry;
- an Einstein-Hilbert action;
- a Newton constant;
- a cosmological constant or AdS solution;
- an absolute physical scale.

The partial-SWAP/exchange dynamics is a deliberately minimal stiffness model,
not a derivation of general relativity.

## 10. Terminal decision

W4.1-W4.5 pass and W4.6 is retained as an explicit open condition.

Therefore

[
\boxed{
\texttt{W4\_AUTONOMOUS\_GEOMETRY\_DYNAMICS\_PASS /
GRAVITATIONAL\_SOURCE\_OPEN}
}
]

is the terminal state.

A successor should now audit the **source and symmetry structure**, not add
more arbitrary geometry propagation terms.
