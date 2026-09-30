# W3_CURVATURE_DYNAMICS_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to

```
W3_BACKREACTING_TETRAD_PASS / CURVATURE_DYNAMICS_OPEN
```

The W3 coarse principal symbol is

[
H_{m Weyl}(x,p)sim sigma^a E_a{}^i(x)p_i,
]

with

[
E(z)=E_0-2g,mathrm{diag}(z_1,z_2,z_3)D+O(g^2),
]

and the same (z_e=langle Z_eangle) is changed by matter through the
noncommuting Y-kick.

## 1. Single question

Does W3 already contain enough structure for **curvature dynamics**, rather
than only a matter-dependent tetrad field?

The gate separates:

1. metric kinematics;
2. possible nonzero curvature of an inhomogeneous tetrad;
3. autonomous geometry dynamics/stiffness;
4. source structure.

## 2. C1 — coarse metric kinematics

For a slowly varying real tetrad (E_a{}^i(x)), define the spatial
contravariant metric from the Weyl principal symbol,

[
h^{ij}(x)=sum_a E_a{}^i(x)E_a{}^j(x).
]

PASS requires that W3 give an explicit geometry-state-dependent (h^{ij}).

## 3. C2 — curvature can be nonzero kinematically

For spatially varying (z_a(x)), determine whether the induced metric can
have nonzero derivatives and hence nonzero linearized spatial curvature.

This is only a kinematic statement. It does not count as a gravitational
equation.

## 4. C3 — autonomous geometry dynamics

A gravity-like field must have dynamics not reducible to an external or
instantaneous matter register.

PASS requires at least one geometry-only or geometry-geometry local unitary
that changes (z_e) (or the coarse tetrad) even when the relevant matter
source operators vanish.

Equivalently, the microscopic update must contain a spatial stiffness /
neighbor coupling / plaquette-type term from which propagation of geometric
disturbances could arise.

Indirect future mediation through matter is not counted as an intrinsic
geometry kinetic term at this gate.

## 5. C4 — gravitational source structure

The W3 source is currently endpoint occupation (a_e=langle A_eangle).

PASS requires either:

- a derived conserved stress-energy-like source appropriate to the continuum
  matter theory; or
- a proof that the declared source reduces to the required component under a
  controlled limit.

Merely calling occupation “energy density” does not pass.

## 6. Terminal states

1. `NO_COARSE_METRIC`.
2. `COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL`.
3. `CURVATURE_DYNAMICS_PASS / EINSTEIN_STRUCTURE_OPEN`.
4. `OPEN_AFTER_AUDIT`.

## 7. Stop rule

If C1-C2 pass but C3 or C4 fails, stop at
`COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL`.

Do not invent a geometry self-interaction or relabel endpoint occupation as
stress-energy inside this gate.
