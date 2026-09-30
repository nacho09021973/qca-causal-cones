# W2_TETRAD_BACKREACTION_AUDIT — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W2_TETRAD_BACKREACTION_AUDIT](../theory/W2_TETRAD_BACKREACTION_AUDIT.md), frozen at commit `1fc383fd62607ab118f3d6305c8e445ca10caab9`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL
```

This supersedes only the interpretation of the W2 control variable as a
dynamical tetrad. It does not invalidate the previously derived
geometry-state-dependent principal symbol.

## Exact conservation

The declared W2 local Hamiltonian is

[
H_e=B_eotimes J_e,
qquad B_e=Z_e+X_e.
]

The observable that controls the matter principal-symbol coefficient is
(B_eotimes I). Exactly,

[
[H_e,B_eotimes I]
=
[B_e,B_e]otimes J_e
=
0.
]

Therefore for

[
V_e(g)=e^{-igH_e},
]

[
V_e(g)^dagger(B_eotimes I)V_e(g)=B_eotimes I
]

for every real (g).

Thus, for every joint initial state,

[
oxed{
langle B_eangle_{m out}
=
langle B_eangle_{m in}.
}
]

No perturbative qualification is needed.

## What still changes

The link density matrix can change because components not commuting with
(B_e) evolve conditionally on the matter current. This is the response
identified in W2.3.

However, the principal-symbol deformation depends on

[
b_e=langle B_eangle,
]

and this quantity is exactly conserved.

So the declared W2 coupling provides:

[
	ext{link background} 	o 	ext{matter principal symbol}
]

but not

[
	ext{matter} 	o b_e 	o 	ext{principal symbol}.
]

## Corrected scientific state

Retain:

```
W2_PRINCIPAL_SYMBOL_CONTROL = PASS
```

Withdraw/supersede:

```
W2_DYNAMIC_TETRAD_LIKE_VARIABLE
```

Replace by:

```
W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL
```

The correct statement is that W2 constructs a link-controlled Weyl tetrad
deformation, not yet a backreacting tetrad.

## Required repair

A successor must separate the geometry operator that controls transport from
a noncommuting geometry operator through which matter updates that control.

For example, a transport substep may depend on (Z_e), while a distinct
backreaction substep uses (X_e) (or another operator not commuting with
(Z_e)). Only then can matter change the next-step transport coefficient.

No repaired model is constructed in this audit.
