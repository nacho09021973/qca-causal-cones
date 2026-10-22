# W1_COARSE_METRIC_GATE

**Fecha:** 2026-09-29.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to

```
W1_GEOMETRICITY_GATE = W1_OPERATIONAL_GEOMETRY_PASS
SCOPE = FINITE_TIME_EXACT_SUPPORT_ONLY
```

The W1 interaction is

[
V_e(g)=exp[-ig B_eotimes A_e],
qquad
B_e=Z_e+X_e,
]

[
A_e=(|x\ranglelangle x|+|y\ranglelangle y|)otimes I_2,
]

followed after the frozen CJWW (5.15) matter update.

## 1. Single question

Does a smooth/semiclassical state of the W1 link register change the
**principal matter propagation symbol** in a way that can be interpreted as a
local tetrad/light-cone deformation?

A finite-time interference-support change is not sufficient.

## 2. Metric-level criterion

For a slowly varying classical/semiclassical link background, derive the
first-order effective matter operator.

PASS requires a correction to the coefficient of the momentum-dependent
Weyl term,

[
H_W(p)=sigma^a e_a^{ i}p_i+cdots,
]

so that the link state changes (e_a^{ i}), the local characteristic cone,
or an equivalent principal-symbol object.

The following do **not** count as a metric deformation:

- a scalar on-site potential;
- a position-dependent overall phase;
- a mass term with unchanged principal symbol;
- dephasing/noise after tracing out links;
- lifting exact path cancellations while the one-step causal neighborhood and
  principal symbol remain fixed.

## 3. First-order mean-field reduction

For a product/separable link background with

[
b_e=operatorname{tr}(eta_e B_e),
]

the first-order reduced matter generator contributed by W1 is

[
H_{\rm link}^{(1)}=sum_e b_e A_e.
]

Because each (A_e) is diagonal in matter position and proportional to the
coin identity,

[
H_{\rm link}^{(1)}
=
sum_x v(x)|x\ranglelangle x|otimes I_2,
]

where

[
v(x)=sum_{e
i x}b_e.
]

The execution must determine whether such a term can alter the Weyl principal
symbol or only supply a scalar potential.

## 4. Exact eigen-background test

If every edge is in an eigenstate of (B_e), then W1 acts on the matter
sector as a position-dependent on-site phase,

[
V_g^{\rm eff}
=
sum_x e^{-ig v(x)}|x\ranglelangle x|otimes I_2.
]

For locally constant (v(x)), the Bloch symbol is

[
W_g(x,p)=e^{-igv(x)}W_0(p).
]

The gate must compare the (p)-derivative/principal symbol of (W_g) with
that of (W_0).

## 5. Traced-link test

For non-eigenstate link backgrounds, the W1 report found the first
regular-background matter correction at (O(g^2)) to be a local
dephasing-type channel.

The gate must state whether that nonunitary correction defines a metric
principal symbol. It may not be relabeled as curvature by analogy.

## 6. Terminal states

1. `W1_PRINCIPAL_SYMBOL_METRIC_PASS`.
2. `W1_SCALAR_POTENTIAL_ONLY / NO_METRIC_DEFORMATION`.
3. `OPEN_AFTER_AUDIT`.

## 7. Stop rule

If the present (A_e) coupling only generates an order-zero scalar potential
plus decoherence, stop. Do not repair it inside this gate by replacing
(A_e) with geometry-controlled hopping matrices.

Such a replacement would be a new model and requires a separate successor
charter.
