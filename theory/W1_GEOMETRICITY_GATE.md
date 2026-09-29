# W1_GEOMETRICITY_GATE

**Fecha:** 2026-09-29.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to

```
W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE =
W1_CAUSAL_UNITARY_BRIDGE_PASS / FULL_QCGD_SYNTHESIS_OPEN
GEOMETRIC_INTERPRETATION = OPEN
```

The W1 ansatz attaches one qubit to each undirected edge of the certified
CJWW (5.15) support graph and uses

[
A_e=(|xanglelangle x|+|yanglelangle y|)otimes I_2,
]

[
V_e(g)=exp[-ig(Z_e+X_e)otimes A_e],
qquad
V_g=prod_eV_e(g),
]

[
U_g=V_g(I_gotimes U_0),
qquad U_0=U_{m CJWW}.
]

## 1. Single question

Does the W1 edge register define a genuine operational geometry, rather than
an internal link field?

For this gate, a necessary geometricity criterion is:

> changing the edge state must change at least one exact matter
> adjacency/causal-support statement.

Equivalent witnesses include:

- the one-step strict support set;
- an exact zero/nonzero transition amplitude between two sites;
- the asymptotic strict causal body;
- a graph distance defined by allowed matter propagation.

Changing only phases, internal spin rotations or reduced-state coherence while
leaving all exact support relations unchanged does **not** pass this gate.

## 2. Gm1 — one-step support dependence

For geometry states (|Gangle,|G'angle), define the joint transition
support from matter site (x) to matter site (y) by the existence of some
nonzero geometry matrix element

[
langle G_f,y|U_g|G,xangle
e0.
]

Gm1 PASS requires a pair (G,G') for which the set of reachable (y) differs.

## 3. Gm2 — finite-time causal support dependence

Let (mathcal R_t^G(x)) be the set of matter sites reachable with nonzero
joint amplitude after (t) steps from geometry state (G) and a matter
state localized at (x).

Gm2 PASS requires

[
mathcal R_t^G(x)
emathcal R_t^{G'}(x)
]

for some finite (t), or an equivalent difference in strict causal bodies.

## 4. Structural observation to test

Every (A_e) is diagonal in the matter position basis. Therefore every
(V_e(g)), and hence (V_g), is block diagonal in matter position:

[
V_g=sum_x |xanglelangle x|otimes R_x
]

for geometry/internal operators (R_x).

If this identity is exact, (V_g) cannot create a matter transition between
distinct lattice sites. The only position-changing factor in (U_g) is
(U_0).

The execution must determine whether this implies

[
mathcal R_t^G(x)=mathcal R_t^{U_0}(x)
]

for every geometry input (G) and every (t).

## 5. Terminal states

1. `W1_LINK_FIELD_NOT_GEOMETRY` — support/causal structure is exactly
   independent of the edge register.
2. `W1_OPERATIONAL_GEOMETRY_PASS` — an exact support/adjacency witness
   depends on geometry.
3. `OPEN_AFTER_AUDIT`.

## 6. Stop rule

If the current W1 ansatz fails, do not repair it inside this gate by replacing
(V_e) with a geometry-controlled hopping rule. Such a rule changes the model
class and requires a separate successor charter.

A negative result does not invalidate W1 as a reversible matter-link
interaction. It only rejects the geometric interpretation needed to reopen the
gravitational-normalization gate.
