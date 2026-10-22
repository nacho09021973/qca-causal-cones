# W3_BACKREACTING_TETRAD_FLOQUET_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input and correction

Successor to the exact W2 audit

```
W2_PRINCIPAL_SYMBOL_CONTROL = PASS
W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL
```

W3 must make the observable that controls transport itself matter-dependent.

## 1. Frozen matter baseline and directions

Retain CJWW Eq. (5.15) as (U_0), and the three linearly independent support
directions

[
d_1=(1,0,0),quad d_2=(1,1,0),quad d_3=(1,1,1).
]

For (e=(x,x+d_a)), retain the Hermitian current

[
J_e^{(a)}
=
i(|x+d_a\ranglelangle x|-|x\ranglelangle x+d_a|)
otimessigma_a.
]

Define also the endpoint occupation projector

[
A_e=(|x\ranglelangle x|+|x+d_a\ranglelangle x+d_a|)
otimes I_2.
]

## 2. Geometry qubit and two noncommuting substeps

Each edge carries one qubit.

### Backreaction kick

[
R_e(g)=exp[-ig,Y_eotimes A_e].
]

### Transport/tetrad gate

[
T_e(g)=exp[-ig,Z_eotimes J_e^{(a)}].
]

One local W3 edge substep is

[
V_e(g)=T_e(g)R_e(g).
]

The full interaction uses the same parity/matching layering as W2. The complete
matter/geometry step is

[
U_g=V_g(I_gotimes U_0).
]

No full finite-depth synthesis claim for (U_0) is added.

## 3. Reference geometry state

Use a product edge state with Bloch vector

[
(x_0,y_0,z_0)=(sin\theta,0,cos\theta),
qquad 0<\theta<pi/2.
]

Thus both (x_0) and (z_0) are nonzero while (y_0=0).

This avoids a first-order scalar-potential mean from the kick and permits
first-order matter-dependent evolution of (z_e=langle Z_e\rangle).

## 4. Obligations

### W3.1 exact CJWW recovery

[
U_{g=0}=I_gotimes U_0.
]

### W3.2 exact local unitarity and finite interaction depth

Both (R_e) and (T_e) must be exact local unitaries. The interaction depth
must be bounded independently of volume.

### W3.3 tetrad control

For a slowly varying/separable geometry background with
(z_a=langle Z_e\rangle) on family (a), the transport gate must give

[
E(z)=E_0-2g,mathrm{diag}(z_1,z_2,z_3)D+O(g^2)
]

with (D) the W2 direction matrix.

### W3.4 matter changes the tetrad control

For initially uncorrelated edge/matter states, derive

[
z_e' - z_e
]

after (R_e(g)). PASS requires a matter-dependent leading term.

### W3.5 reciprocal closure at perturbative level

Combining W3.3 and W3.4 must give a nonzero matter-dependent change of the
next-step principal-symbol/tetrad coefficient.

### W3.6 no false Einstein claim

The backreaction source may be endpoint occupation at this gate. It is not
identified with the stress-energy tensor, and the resulting difference
equation is not called Einstein dynamics.

## 5. Terminal states

1. `W3_BACKREACTING_TETRAD_FAIL`.
2. `W3_BACKREACTING_TETRAD_PASS / CURVATURE_DYNAMICS_OPEN`.
3. `OPEN_AFTER_AUDIT`.

## 6. Stop rule

If W3.1-W3.5 pass, stop at
`W3_BACKREACTING_TETRAD_PASS / CURVATURE_DYNAMICS_OPEN`.

Do not infer curvature action, local Lorentz/diffeomorphism symmetry,
Einstein equations, (G_{\rm eff}), AdS, or an absolute scale.
