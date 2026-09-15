# S4 strict-cone counterexample — branch freeze

**Date:** 2026-09-15  
**Base:** `main` at `5845eda92d7a5ee07c2e8eb26183eb5b2770cf79`  
**Branch:** `research/s4-strict-cone-counterexample`  
**Status:** BRANCH-LOCAL FREEZE; canonical state intentionally unchanged.

## Purpose

Archive the `s=4` construction derived after the current `main` state so that it can be independently reviewed before any promotion to `state/CURRENT_STATE.md`.

## Minimal claim archived

Within the declared BCC `s=4` class, there is an explicit irreducible family with

- full eight-generator BCC Fourier support and no on-site term;
- exact unitarity and homogeneous `D2` covariance in the non-trivial Pauli projective class;
- exact strict asymptotic body equal to the microscopic BCC cube;
- a rank-two Weyl sector at `k=0` with tunable low-energy speed.

For the one-parameter subfamily `theta=pi/4`,

\[
c_{\rm strict}^{\rm iso}=1/\sqrt3,
\qquad
c_0(a)=a/\sqrt3,
\qquad 0<a<1.
\]

If the analytic proof and executable certificate survive independent review, the strong statement that the strict BCC asymptotic causal body alone fixes the Weyl speed is falsified in this enlarged internal class.

## Files

- `theory/S4_STRICT_CONE_COUNTEREXAMPLE.md` — definitions and analytic proofs.
- `scripts/cert_Aa_s4_counterexample.py` — SymPy exact reproducibility certificate.

Local reconstruction check before upload:

```text
S4_STRICT_CONE_COUNTEREXAMPLE_CERTIFICATE: PASS
a_panel=1/5,2/5,1/2,1/sqrt(2),4/5,99/100
theta_panel=pi/6,pi/4,pi/3 at a=1/2
backend=sympy_exact
tolerance=0
```

The repository already pins `sympy==1.14.0`; no dependency change is required.

## Two-parameter extension

The branch also records

\[
A_{a,\theta}(k)=W_\theta e^{-iq_x\Gamma_x}e^{-iq_y\Gamma_y}e^{-iq_z\Gamma_z},
\qquad W_\theta=I\otimes e^{-i\theta\tau_z}.
\]

For `0<theta<pi/2`, the two doublets at `k=0` have quasienergy separation

\[
\Delta\varepsilon=2\theta,
\]

while the Weyl speed remains

\[
c_0=a/\sqrt3.
\]

With the spectral-projector normalization

\[
g_{ij}(0)=\frac12\operatorname{Tr}[(\partial_iP_+)(\partial_jP_+)],
\]

the family obeys

\[
g_{ij}(0)=\frac{1-a^2}{6\sin^2\theta}\delta_{ij}
\]

and therefore

\[
\boxed{c_0^2+2\sin^2(\Delta\varepsilon/2)g_{ii}(0)=1/3}.
\]

This identity is archived as a **family identity only**, not as a general QCA theorem.

## Mandatory interpretation cautions

1. **`s=2` remains alive.** This is not a counterexample inside the P17 minimal `s=2` classification.
2. **The node is Floquet-shifted.** `A_{a,theta}(0)=W_theta` is not a global phase; the two rank-two Weyl crossings sit at nonzero quasienergy.
3. **Strict means exact support.** The vertex coefficients remain nonzero under iteration, but their norms may decay exponentially. A ballistic/essential/Lieb-Robinson front is a different observable and has not been substituted post hoc.
4. **Irreducibility is joint-commutant irreducibility.** The certificate tests the scalar joint commutant; non-scalar multiplicity matrices alone would not suffice.
5. **No novelty claim yet.** Prior-art comparison must remain adversarial and separate from correctness.
6. **No canonical promotion yet.** `state/CURRENT_STATE.md` is deliberately untouched until this branch receives independent review.

## Promotion gate

Do not merge or update canonical state until at least these checks are independently repeated:

- reproduce the exact certificate from a fresh checkout;
- recheck the all-`a` trace/non-nilpotency proof;
- recheck the irreducibility argument independently of the script;
- recheck the Weyl projection and the quantum-metric normalization;
- record prior-art status separately.
