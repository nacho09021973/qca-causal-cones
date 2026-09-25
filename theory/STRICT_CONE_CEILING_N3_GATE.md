# Point (3): strict asymptotic cone ceiling on N3

**Date:** 2026-09-16. **Scope:** branch-local,
`research/b-infinity-post-s4-gate`.
**Authorization:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION`.
The user's instruction was: "pues adelante, punto (3)".
This authorizes investigating point (3) only; it is not a five-member
ratification of `GATE_COMPLETITUD_AXIAL_N3`. The attempted ratification
remains `ABORTED_OR_INCOMPLETE` (Gemini absent; no final verdict).

**Initial evidence status:** OPEN. This contract is frozen before the new
derivation. No claim of a proof, counterexample or novelty is recorded here.

## 1. Frozen question

Does every admitted symbol and selected isotropic, untilted cone satisfy

`c_0 <= c_strict^iso`,

where the right-hand side uses the exact Fourier support of the **full same
symbol** at arbitrarily many complete updates? The claim is an upper bound,
not equality or saturation of the microscopic body.

## 2. Quantifiers and admission

Fix the following data before considering coefficients:

| Item | Frozen declaration |
| --- | --- |
| Geometry | d=3, `N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`, Cartesian Euclidean coordinates, one complete update per unit time |
| Symbol | `U(k)=sum_{h in N_3} exp(-i k.h) T_h`, every `T_h != 0`, no other Fourier modes, no on-site mode |
| Internal space | Any prescribed finite integer `s >= 2`, held fixed in each quantified class; no scan or change of s in a calculation |
| Unitarity | `U(k)` unitary for every real k; exact coefficient identities, not a mesh condition |
| Symmetry | D2 acts by Cartesian half-turns; any prescribed unitary/projective representation R on `C^s`, fixed within the class; `T_{g h}=R_g T_h R_g^dagger` |
| Node and phase | `k_star=0`; any fixed eigenphase `omega_star` of U(0), including nonzero Floquet phases; a local unwrapped phase is used |
| Eigenspace | P is the full spectral projector of U(0) at `exp(-i omega_star)`, any fixed rank `2 <= r <= s`; isolated from distinct eigenvalues at the node; r=s is allowed |
| Selected cone | In every unit direction q, eigenphases emerging from P include slopes `+c_0` and `-c_0`, with the same `c_0>0`; equivalently the selected cone is isotropic and untilted to first order |
| Other slopes | Other branches in the same eigenspace may have other slopes; the whole eigenspace need not be purely conical |
| Reducibility | No dynamical irreducibility, minimality, irreducibility of R, scalar-node or vertex-survival assumption is imposed |
| Coverage | Full coefficient class satisfying these conditions, for every fixed s and R, including disconnected components; no product ansatz |
| Equivalences | Constant unitary basis changes and simultaneous D2 relabelings preserve the question; no change of embedding, origin, time unit or support is used to compare speeds |

The quantified statement is for every fixed choice of these data and every
admitted symbol. A proof uniform in s and R is permitted; no classification
or search in larger internal spaces is authorized. The full-symbol support
is intentional: no claim about support intrinsic to a selected sector is
made, and spectator sectors are not silently removed.

## 3. Exact output and convergence

For integer `n >= 1`, define `S_n` from the nonzero matrix Fourier
coefficients of `U(k)^n`, including all cancellations. For every real q,

`H_n(q)=max_{x in S_n} q.x`,

`h_infty(q)=lim_{n -> infinity} H_n(q)/n`,

`c_strict^iso=min_{||q||=1} h_infty(q)`.

The limit, originally defined as a limsup, must be justified using exact
support subadditivity. Existence of the minimum must also be justified.
No assumption of positivity of `c_strict^iso` is made in advance.

The desired intermediate bound is directional: every selected positive
cone slope is at most `H_n(q)/n` for every n and every unit q. A sufficient
route is a finite-time operator bound for
`J_n(q)=i (U^n)^dagger partial_q(U^n)` and its compression to P.
Any argument must remain valid when distinct eigenvalues of U(0) coincide
after taking the n-th power. No global smooth eigenbasis over the sphere
may be assumed at a conical node.

## 4. Frozen acceptance and stop rules

- **PASS_ANALYTIC:** a complete analytic proof under all the quantified
  conditions, with the directional, degeneracy, Floquet, power-collision
  and support-limit obligations discharged. Any invoked spectral or
  derivative theorem needs a checked source or a supplied proof.
- **FAIL_COUNTEREXAMPLE:** an exact admitted symbol with a certified
  `c_strict^iso < c_0`. This includes a zero or negative strict isotropic
  value; positivity of that value is not an extra FAIL requirement.
- **INCONCLUSIVE:** a missing lemma, unverified external theorem, proof
  restricted to the coordinate axes, extra undeclared hypothesis, or only
  a finite numerical check. Failure of a proof strategy is not a falsifier.
- **Review level:** a completed author derivation remains PRELIMINARY until
  independently reviewed. Record proof completeness and independent review
  separately; do not call a self-check independent certification.

Stop at a genuine failure or unclosed obligation. Do not replace a missing
ceiling proof with L1 or a metric identity. Do not begin those other steps.

## 5. Verification obligations fixed before derivation

Inspect the sign convention with a scalar shift; treat rational and
irrational directions; do not exchange a direction minimum and a time
limit without proof; retain exact cancellations in S_n; handle r=s and
spectator slopes; handle eigenvalue collisions of U^n using the original
P; compare the final inequality with the already certified Pavia equality
and strict s=4 inequality without rerunning their scientific scripts.

These are mathematical checks, not numerical tolerances. No solver,
simulation, new family search or ephemeral scientific script is needed.

## 6. Claim ceiling

Only point (3) is authorized. L1 remains a manual candidate derivation;
the defect identity remains established only in its previously certified
family. The s=4 example refutes the strong equality, not this ceiling.
Vertex nilpotency alone still does not imply a decrease of `c_strict^iso`.
`NOVELTY = OPEN`. A proof of this bound would establish neither equality,
microscopic saturation, inter-species universality nor a ballistic-front
claim. `main` and the frozen branches are outside the scope of this work.
