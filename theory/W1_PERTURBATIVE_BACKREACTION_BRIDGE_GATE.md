# W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE

> **Typographic reconstruction — 2026-10-26.** LaTeX backslashes restored
> by hand against the declared projector coupling and the execution report.
> The frozen contract remains `2631e31369a9598da044d00e37cbb54d7100cab6`.
> No words, coefficients or criteria changed. The related certificate
> `scripts/verify_w1_geometricity.py` does not certify every obligation here.
> Manual checks and their scope are recorded in
> `reports/2026-10-26--w1-typographic-reconstruction.md`.

**Fecha:** 2026-09-29.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to

```
EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE =
STRONG_EXACT_BRIDGE_IMPOSSIBLE
```

The no-go forces any matter-to-geometry backreaction to perturb the exact
reduced CJWW matter channel. This gate tests the conservative W1 escape:

\[
\Phi_g = \mathcal U_{\rm CJWW} + O(g)
\]

with exact CJWW recovered at \(g=0\), and nontrivial geometry response for
\(g\ne0\).

## 1. Frozen matter object

Matter Hilbert space:

\[
\mathcal H_m=\ell^2(\mathbb Z^3)\otimes\mathbb C^2.
\]

The target flat update is the certified CJWW Eq. (5.15) unitary
\(U_0=U_{\rm CJWW}\), whose exact Fourier support has 14 jumps,

\[
F=\{(\pm1,\pm1,\pm1),(\pm1,\pm1,0),(\pm1,0,0)\}
\]

with the actual seven undirected displacement families read from the certified
symbol.

No modification of \(U_0\) is allowed.

## 2. Geometry register

For each undirected edge \(e=\{x,x+d\}\) belonging to one of the seven
undirected CJWW displacement families, attach one qubit

\[
\mathcal H_e\simeq\mathbb C^2.
\]

The regular background is

\[
|G_0\rangle=\bigotimes_e |0\rangle_e.
\]

At this gate the edge qubit is a **candidate local geometry variable** only.
No metric interpretation, length assignment or Einstein dynamics is assumed.

## 3. Local interaction ansatz

For an edge \(e=\{x,y\}\), define a bounded local Hermitian matter operator
\(A_e\). The minimal declared choice is the endpoint occupation projector on
the one-particle sector,

\[
A_e=(|x\rangle\langle x|+|y\rangle\langle y|)\otimes I_2.
\]

Define

\[
H_e=(Z_e+X_e)\otimes A_e,
\qquad
V_e(g)=e^{-igH_e}.
\]

The \(Z_e\) term makes different geometry configurations act differently on
matter. The \(X_e\) term allows matter expectation values to change the
geometry state.

No coupling constant is identified with gravity; \(g\) is dimensionless.

## 4. Local layering

For each of the seven undirected displacement vectors choose the
representative with first coordinate \(+1\). For a fixed displacement \(d\),
split edges \(\{x,x+d\}\) according to the parity of \(x_1\).

Because \(d_1=1\), each parity class is a matching. Thus the declared
interaction can be implemented in at most

\[
7\times2=14
\]

layers of pairwise disjoint local edge gates \(V_e(g)\).

Let \(V_g\) denote their ordered product.

The candidate complete one-step update is

\[
U_g=V_g(I_g\otimes U_0).
\]

The gate distinguishes:

- `CAUSAL_UNITARY_LEVEL`: \(U_0\) is taken as the already-certified
  finite-range CJWW walk and the added interaction is a finite-depth local
  circuit;
- `FULL_QCGD_CIRCUIT_LEVEL`: an explicit finite-depth realization of the
  **entire** \(U_g\), including \(U_0\), is separately established.

Do not promote the first to the second without evidence.

## 5. W1 obligations

### W1.1 exact zero-coupling recovery

\[
U_{g=0}=I_g\otimes U_0.
\]

### W1.2 matter-to-geometry response

For some edge \(e\) and matter states \(\rho,\rho'\),

\[
\left.\frac{d}{dg}\rho_{g,e}^{\rm geom}\right|_{g=0}
\]

must differ.

### W1.3 geometry-to-matter response

Two local geometry states with different \(Z_e\) expectation must induce
different first-order matter channels.

### W1.4 controlled matter disturbance on the regular background

For \(|G_0\rangle\), derive the first nonzero correction to the reduced matter
channel. It may be \(O(g)\) or smaller, but it must be explicit and vanish at
\(g=0\).

### W1.5 finite-range/locality

The added interaction must have bounded range and finite layer depth
independent of system size.

### W1.6 no false gravitational promotion

Passing W1 does not imply that the edge qubits are physical geometry, that
\(g\) is Newton's constant, or that an Einstein-Hilbert term exists.

## 6. Terminal states

1. `W1_ANSATZ_INCONSISTENT`.
2. `W1_CAUSAL_UNITARY_BRIDGE_PASS / FULL_QCGD_SYNTHESIS_OPEN`.
3. `W1_FULL_QCGD_BRIDGE_PASS`.
4. `OPEN_AFTER_AUDIT`.

## 7. Stop rule

If W1.1-W1.5 pass at the causal-unitary level but no exact finite-depth
factorization of CJWW Eq. (5.15) is already established, stop at

`W1_CAUSAL_UNITARY_BRIDGE_PASS / FULL_QCGD_SYNTHESIS_OPEN`.

Do not invent a new factorization solely to upgrade the label.
