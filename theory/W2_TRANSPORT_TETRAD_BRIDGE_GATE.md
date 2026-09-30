# W2_TRANSPORT_TETRAD_BRIDGE_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to

```
W1_COARSE_METRIC_GATE =
W1_SCALAR_POTENTIAL_ONLY / NO_METRIC_DEFORMATION
```

W1 failed at metric level because its matter operator was diagonal in position.
W2 is allowed to change the transport operator itself, while retaining exact
CJWW Eq. (5.15) at zero coupling.

## 1. Frozen matter baseline

Matter Hilbert space:

[
mathcal H_m=ell^2(mathbb Z^3)otimesmathbb C^2.
]

Flat update:

[
U_0=U_{m CJWW(5.15)}.
]

Near (p=0), the exact symbol satisfies

[
W_0(p)
=
I+ileft(p_1sigma_1-p_2sigma_2+p_3sigma_3ight)
+O(|p|^2),
]

equivalently (W_0=e^{-iH_0}) with the corresponding convention-dependent
Weyl tetrad. Only changes relative to this fixed convention matter below.

Choose three linearly independent displacement vectors already contained in
the exact CJWW support:

[
d_1=(1,0,0),qquad
d_2=(1,1,0),qquad
d_3=(1,1,1).
]

Their displacement matrix has determinant one.

## 2. Geometry/link registers

For each oriented edge (e=(x,x+d_a)), (a=1,2,3), attach one qubit with

[
B_e=Z_e+X_e.
]

No metric meaning is assumed at freeze time.

## 3. Transport coupling

Define the Hermitian matter current on edge (e=(x,x+d_a)),

[
J_e^{(a)}
=
ileft(
|x+d_aanglelangle x|
-
|xanglelangle x+d_a|
ight)otimessigma_a.
]

Define the exact local unitary

[
V_e^{(a)}(g)
=
exp[-ig,B_eotimes J_e^{(a)}].
]

For each displacement family, split edges by parity of (x_1). Since
((d_a)_1=1), each parity class is a matching. The added interaction therefore
has at most six disjoint-edge layers.

Let (V_g) be the ordered product of these six layers and

[
U_g=V_g(I_gotimes U_0).
]

No finite-depth synthesis claim for (U_0) itself is added.

## 4. Obligations

### W2.1 exact flat recovery

[
U_{g=0}=I_gotimes U_0.
]

### W2.2 exact local unitarity and bounded causal range

Each (V_e^{(a)}(g)) must be unitary and supported only on one link register
and the two endpoint matter sites. Layer depth must be independent of volume.

### W2.3 matter-to-link backreaction

For some local matter states (ho,ho'), the first derivative of the edge
state at (g=0) must differ. The response must depend on a matter current
observable, not merely total occupation.

### W2.4 link-to-matter transport response

Two edge backgrounds with different (langle B_eangle) must alter the
first-order matter transport generator.

### W2.5 principal-symbol/tetrad deformation

For a translation-invariant semiclassical link background with family means

[
b_a=langle B_eangle,qquad eparallel d_a,
]

derive the uniform first-order matter symbol. PASS requires a nonzero
momentum-linear correction

[
delta H(p)
=
sum_{a,i}delta e_a{}^i,sigma_a p_i
+O(|p|^2)
]

with at least one (delta e_a{}^i
e0).

A scalar potential or quasienergy shift does not pass.

### W2.6 reciprocal perturbative consistency

The same coupling that changes the principal symbol must also permit
matter-dependent link evolution. A geometry-controlled transport term with no
backreaction is insufficient.

## 5. Full-rank directional check

For the declared three families, the linear current symbols are expected to
contain

[
2sin(pcdot d_a)sigma_a
=
2(d_acdot p)sigma_a+O(|p|^3).
]

Because

[
D=
egin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
end{pmatrix},
qquad det D=1,
]

the three chosen directions span three-dimensional momentum space. This does
not provide all nine tetrad components, but it is enough to test a genuine
cone deformation.

## 6. Mandatory ceiling

Passing W2 establishes only a **dynamical principal-symbol / tetrad-like
degree of freedom** at perturbative level.

It does not establish:

- Einstein dynamics;
- diffeomorphism or local Lorentz gauge symmetry;
- a curvature tensor;
- a Newton constant;
- an AdS radius;
- an absolute scale;
- that the link qubits are nature.

## 7. Terminal states

1. `W2_TRANSPORT_COUPLING_FAIL`.
2. `W2_DYNAMIC_PRINCIPAL_SYMBOL_PASS / CURVATURE_OPEN`.
3. `OPEN_AFTER_AUDIT`.

## 8. Stop rule

If W2.1-W2.6 pass, stop at
`W2_DYNAMIC_PRINCIPAL_SYMBOL_PASS / CURVATURE_OPEN`.

Do not infer Einstein equations or reopen gravitational normalization G1 until
a separate curvature/dynamics gate defines a coarse geometric field and its
equation of motion.
