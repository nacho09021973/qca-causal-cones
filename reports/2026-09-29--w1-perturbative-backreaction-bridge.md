# W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE — execution

**Fecha:** 2026-09-29.  
**Contrato:** [W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE](../theory/W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE.md), frozen at commit `2631e31369a9598da044d00e37cbb54d7100cab6`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE =
W1_CAUSAL_UNITARY_BRIDGE_PASS / FULL_QCGD_SYNTHESIS_OPEN
```

Additional ceiling:

```
GEOMETRIC_INTERPRETATION = OPEN
GRAVITATIONAL_NORMALIZATION_G0 = NOT_REOPENED
```

The construction is an explicit local **link-register** backreaction bridge.
It proves algebraic compatibility of reversible local backreaction with exact
CJWW recovery at zero coupling. It does not yet prove that the link qubits are
physical geometry or adjacency.

## 1. Exact CJWW support used

The certified support of Eq. (5.15) is

[
F={
(-1,-1,-1),(-1,-1,0),(-1,-1,1),(-1,0,0),
(-1,1,-1),(-1,1,0),(-1,1,1),
]
[
(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,0),
(1,1,-1),(1,1,0),(1,1,1)
}.
]

Thus the seven undirected representatives can be taken as

[
D_+={
(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,0),
(1,1,-1),(1,1,0),(1,1,1)
}.
]

Every site has degree (14) in this undirected support graph.

For rigor of the global circuit, work first on an even periodic cubic box.
All formulas below are local and uniform in the box size.

## 2. Local gate

For each undirected edge (e={x,y}), let

[
A_e=(|xanglelangle x|+|yanglelangle y|)otimes I_2,
qquad A_e^2=A_e.
]

Let the edge register be a qubit and define

[
B_e=Z_e+X_e,
qquad B_e^2=2I_e,
]

[
H_e=B_eotimes A_e,
qquad
V_e(g)=e^{-igH_e}.
]

Because (A_e) is a projector,

[
V_e(g)
=
I_eotimes(I-A_e)
+
e^{-igB_e}otimes A_e.
]

So the gate is exactly unitary for every real (g), with no perturbative
unitarity claim.

## 3. W1.1 — exact zero-coupling recovery

Let (V_g) be the product of all edge gates and

[
U_g=V_g(I_gotimes U_0).
]

At (g=0),

[
V_e(0)=I,qquad V_0=I,
]

hence

[
oxed{
U_{g=0}=I_gotimes U_{m CJWW}.
}
]

**W1.1 = PASS.**

## 4. W1.5 — bounded locality and 14-layer interaction circuit

Fix (din D_+). Orient each edge from (x) to (x+d). Since (d_1=1),
split these edges according to the parity of (x_1).

For fixed (d) and fixed parity, two distinct edges cannot share a vertex:
if ({x,x+d}) and ({y,y+d}) share one, then
(y-xin{0,pm d}); the nonzero cases flip the parity of the first
coordinate.

Therefore each parity class is a matching.

There are seven displacement classes and two parities:

[
oxed{	ext{interaction depth}le 14.}
]

Each gate acts on one edge qubit and the two endpoint matter sites, with
(ell^infty) range one. The depth is independent of system size.

Moreover all (A_e) commute, and (B_e) acts on distinct edge registers, so
all (H_e) commute algebraically; the 14 layers are an implementation
constraint, not an ordering ambiguity.

**W1.5 = PASS for the added interaction.**

No explicit finite-depth factorization of the frozen CJWW (5.15) step itself
is established in the repository by this gate. Hence
`FULL_QCGD_SYNTHESIS` remains OPEN.

## 5. W1.2 — matter-to-link response at first order

Let the regular edge state be

[
ho_{e,0}=|0anglelangle0|.
]

For a matter state (sigma) entering the interaction layer, define

[
a_e=operatorname{tr}(A_esigma).
]

To first order,

[
ho_e(g)
=
ho_{e,0}
-ig,a_e[B_e,ho_{e,0}]
+O(g^2).
]

Since (Z_e) commutes with (ho_{e,0}) and
([X_e,ho_{e,0}]
e0),

[
left.rac{d}{dg}ho_e(g)ight|_{0}
=
-i a_e[X_e,ho_{e,0}].
]

Equivalently,

[
left.rac{d}{dg}langle Y_eangleight|_{0}=-2a_e
]

with the standard Pauli convention.

Because (U_0) is unitary, choose two pre-interaction matter states whose
post-(U_0) endpoint occupations on (e) differ. Then their edge-state
derivatives differ.

Thus the link register acquires matter-dependent information at order (g).

**W1.2 = PASS.**

## 6. W1.3 — link state affects matter at first order

For a general initial edge state (eta_e), the first-order reduced matter
generator contributed by edge (e) is

[
langle B_eangle_{eta_e}A_e.
]

In particular,

[
langle0|B_e|0angle=+1,
qquad
langle1|B_e|1angle=-1.
]

Two backgrounds identical except for (e) therefore differ at first order by

[
2A_e
]

in the reduced matter generator. For a matter state not commuting with
(A_e), the two reduced matter channels differ.

**W1.3 = PASS.**

This establishes reciprocal coupling of the declared link register and
matter. It does not yet prove that the register is adjacency or metric.

## 7. W1.4 — regular background: first order cancels to a global phase

Let every edge start in (|0angle). The environment mean of each local
operator is

[
langle B_eangle=1.
]

The first-order effective matter Hamiltonian is therefore

[
H_{m eff}^{(1)}=sum_e A_e.
]

Every matter site belongs to exactly fourteen undirected support edges, so on
the one-particle Hilbert space

[
sum_e A_e=14I_m.
]

Hence

[
-i g[H_{m eff}^{(1)},sigma]
=
-i14g[I_m,sigma]
=0.
]

Thus, on the perfectly regular background,

[
oxed{
Phi_g(ho)
=
U_0ho U_0^dagger + O(g^2).
}
]

This is stronger than the (O(g)) control required by the charter.

It is also consistent with the preceding no-go: geometry can begin to acquire
matter information at order (g), but the reduced matter density matrix
cannot remain exactly CJWW for finite nonzero (g).

## 8. Explicit second-order matter correction

Let

[
sigma=U_0ho U_0^dagger.
]

For distinct edges the regular product background gives factorized moments.
With

[
langle B_eangle=1,qquad
langle B_e^2angle=2,
]

the centered covariance is

[
langle(B_e-1)(B_f-1)angle=delta_{ef}.
]

The mean contribution is generated by (14I_m) and therefore drops out.
The first nonzero reduced correction is

[
oxed{
Phi_g(ho)
=
sigma
+
g^2sum_e
left(
A_esigma A_e
-rac12{A_e,sigma}
ight)
+O(g^3).
}
]

Since (A_e^2=A_e), this is a local dephasing-type correction.

For a position coherence
(|xanglelangle y|otimes M), (x
e y), the coefficient is

[
-rac{g^2}{2}
#{e: e	ext{ is incident to exactly one of }x,y}.
]

Therefore:

- if (x,y) are joined by one support edge, the symmetric difference of
  their incident-edge sets has size (26), giving coefficient
  (-13g^2);
- otherwise it has size (28), giving coefficient (-14g^2).

Diagonal position populations have zero (g^2) correction from this
dephasing term.

The power counting is therefore explicit:

[
	ext{link backreaction}=O(g),
qquad
	ext{regular-background matter disturbance}=O(g^2).
]

**W1.4 = PASS.**

## 9. What has and has not been constructed

Established here:

[
oxed{
	ext{exact CJWW at }g=0
+
	ext{unitary local link backreaction for }g
e0
+
	ext{controlled reduced-matter correction}.
}
]

Not established:

- that the edge qubit is literally adjacency, distance, tetrad or metric;
- that (|1angle_e) means an absent edge;
- that the full CJWW step has been synthesized inside the specific QCGD
  finite-depth gate model used for the interaction;
- any Einstein-Hilbert term;
- any (G_{m eff});
- any absolute scale.

Thus the gravitational-normalization G0 stop is **not** lifted by this report.
The construction first needs a separate geometricity test showing that the
link register changes operational causal/metric structure rather than acting
as an internal link field.

## 10. Terminal-state decision

W1.1-W1.5 pass at the declared causal-unitary level. By the frozen stop rule,

[
oxed{
	exttt{W1\_CAUSAL\_UNITARY\_BRIDGE\_PASS /
FULL\_QCGD\_SYNTHESIS\_OPEN}
}
]

with the additional ceiling

[
oxed{	exttt{GEOMETRIC\_INTERPRETATION = OPEN}.}
]

A natural successor is a **GEOMETRICITY GATE**: require the link register to
change a genuine operational notion of adjacency, causal distance or
propagation support while retaining the (g	o0) CJWW limit.
