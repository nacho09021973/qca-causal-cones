# HEX_TRACE_ALIGNED_ALL_M — aligned hexagons, all radii

Date: 2026-11-05. Author: Codex (OpenAI).
Status: OPEN. Frozen by user approval («haz los tres el texto está
bien», 2026-11-05) after three amendments by Claude Opus 5.5 (Secs. 1, 2,
3); the freezing commit is the preregistration commit. No calculation was
made before it. No review submission or promotion is supplied by this
contract. New contract; no frozen parent is amended.

## 1. Known, question, abandonment

Known: CURRENT_STATE Sec. 16 promotes scalar infeasibility at m=3 and
its walk-level trace bridge, on the aligned 37-point support only.
The general aligned residual reduction in
reports/2026-11-05--hex-trace-scalar-method.md Sec. 3 has one reviewing
house and remains PRELIMINARY. Earlier bounded exclusions do not prove
the all-m statement.

Earlier aligned radii, each in its own promoted class:
- m=1, support {0} U vert(H): T2 PROVED_FOR_MINIMAL_SUPPORT
  (CURRENT_STATE Sec. 12);
- m=2, S19: M1-B19 PROVED_FOR_S19, in W_hex^sym (Sec. 14);
- m=3, 37 points: SCALAR_INFEASIBLE_M3 with trace bridge (Sec. 16).
Their hypotheses are not identical. A statement about the whole aligned
family holds only in the intersection of the classes of m=1,2,3 with the
class of this contract, and the report must state that intersection
explicitly.

Question: for every integer m>=4, are the scalar conditions below
incompatible? Combined with the earlier bounded results, a proof would
exclude attainment throughout the aligned family. This would strengthen
the substrate comparison beyond a finite list, without deciding the
whole hexagonal class or (PH).

Abandon the universal scalar obstruction at the first exact compatible
polynomial with a global bound. That polynomial is not a unitary walk
and does not refute walk non-attainment. Stop this attempt if the bounded
session yields neither such a polynomial nor an all-m proof. Additional
finite-radius exclusions alone are not a successful outcome and do not
justify automatic continuation.

## 2. Domain and logical target

g1=(1,0), g2=(1/2,sqrt(3)/2), Lambda=Z*g1+Z*g2.
For integer m>=4 use Lambda/m and the closed radius-one regular hexagon
with vertices R^j*g1, R the 60-degree rotation. Set
p=k.g1/m, q=k.g2/m. Integer frequency pairs obey
max(|i|,|j|,|i+j|)<=m.

Candidates f are real D6-invariant finite Fourier polynomials with this
support, f(0)=1 and -1<=f<=1 everywhere. Their normal restrictions are
cos(m*q) on p=0, cos(m*p) on q=0 and on p=q.
The target is nonexistence for every m>=4, not just any bounded range.

The proposed equivalent residual formulation is

    f = [cos(m*p)+cos(m*q)+cos(m*(p-q))-1]/2 + Delta*h,
    Delta = sin^2(p/2)*sin^2(q/2)*sin^2((p-q)/2),

with h real D6-invariant Laurent and supported in H_(m-2).
Any proof relying on this formulation must explicitly re-establish its
general quantifiers; the m=3 promotion does not cover them.

Prior art: restricted to a line, the question becomes an extremal
problem for real polynomials of one variable (Markov/Bernstein type).
Bernstein's inequality and its equality theory are prior art; classical
extremal results may be used only as cited prior art, with the primary
source read and cited by page, never presented as new. NOVELTY = OPEN.

Walk consequence, only if proved and later reviewed and promoted:
s=2 unitary Laurent symbols, scalar node after phase removal, traceless
isotropic linear term, support in this aligned lattice hexagon and exact
radius-one hull cannot attain c0=r_in. No product assumption is needed
for this exclusion. The trace bridge must be stated and checked anew
for the general domain. No other orientation, lattice, s or node class.

## 3. Method and budget

One analytic session, at most 90 minutes from the first calculation,
with start/end and commands recorded in the report. First re-derive the
scalar relaxation and general residual reduction. Seek a structural
contradiction valid for arbitrary m, or a motivated exact compatible
candidate. Named first route: generalize the m=3 certificate on the slice
p=2q, x=cos(q). Caveat: allowing an arbitrary polynomial of the degree of
h on the slice is a relaxation strictly weaker than the actual problem
(the m=3 certificate used only the two-dimensional slice image of
alpha+beta*S1). A slice argument must either use the actual slice image of
the D6-invariant h supported in H_(m-2), or prove that the relaxation is
already infeasible. Failure of the relaxation route does not decide the
question. No sequential support sweep, floating-point search or
nonlinear solver. No calculations before approval and
the preregistration commit freezing the contract.

Every computational step retained as evidence belongs in a permanent
script scripts/verify_hex_trace_aligned_all_m.py, created before running
it. A proof must be analytic or an exact certificate with explicitly
universal quantifiers; checking selected m is not a universal certificate.
A compatible candidate requires an exact global bound, not point samples.
Check any claimed decisive argument by a second derivation or a relevant
limit/control, including consistency with the promoted m=3 result.

## 4. Outputs and closure

Permanent report reports/2026-11-05--hex-trace-aligned-all-m.md (use the
actual execution date if later), any verifier and its complete stdout.
Outcomes:

- SCALAR_INFEASIBLE_ALL_ALIGNED_M_GE4, with proof and trace consequence;
- SCALAR_COMPATIBLE_ALIGNED_M_<m>, with exact globally bounded candidate;
- OPEN_AFTER_ALIGNED_ALL_M_ANALYSIS, with the unresolved step identified.

All outcomes initially PRELIMINARY. Independent cross-family review
requires separate explicit authorization to send: one initial round and
at most one repair re-review per reviewer. The general reduction and
trace bridge must be within its scope. Promotion is a separate user
decision. No failed delivery counts as review.

No uniform gap, exact supremum, novelty, physical value of c, general
QCA law, proof of (PH), or closure of M1 is claimed. Non-aligned supports,
including S25, remain separate. No further stage follows automatically.
