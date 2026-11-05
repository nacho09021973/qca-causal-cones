# HEX_TRACE_M3 — first nonconstant scalar residual

Date: 2026-11-05. Author: Codex (OpenAI).
Authorization: user chose option «2»: examine m=3 with two scalar
parameters, exact certification and no automatic continuation to other
radii. This file records the contract before any new calculation or
script execution. No preregistration Git commit is claimed. Parent:
HEX_TRACE_SCALAR_GATE, whose bounded analytic session has ended.

## Known, question, abandonment

Known: reports/2026-11-05--hex-trace-scalar-method.md Sec. 3 proves the
aligned residual form f=f_m^0+Delta*h. Claude Opus 5.5's sealed review
(debates/2026-11-05--hex-trace-scalar-review-opus-network) gives PASS,
no mandatory repairs; reduction not promoted. S19 (m=2) is excluded.

Question: at m=3, does any real pair (alpha,beta) give a globally bounded
candidate f=f_3^0+Delta*(alpha+beta*S1)?

An exact compatible polynomial ends the proposed universal obstruction
based only on these scalar conditions. It is NOT a unitary walk and does
not refute walk non-attainment. An exact incompatibility ends this test
for m=3 only. Failure to find either within the budget ends at OPEN,
with no inference from failed search.

## Frozen domain

Triangular g1=(1,0), g2=(1/2,sqrt(3)/2), lattice Lambda/3 after physical
radius-one normalization. Spectrum in the closed hexagon with vertices
R^j*g1; in p=k.g1/3, q=k.g2/3 variables, integer frequency pairs satisfy
max(|i|,|j|,|i+j|)<=3. Only real D6-invariant scalar polynomials, with
f(0)=1, normal cosines cos(3q) on p=0 and cos(3p) on q=0 and p=q.
The reviewed averaging argument makes this sufficient for scalar
existence. No matrix symbol or product factorization is sought.

    f_3^0 = [cos(3p)+cos(3q)+cos(3(p-q))-1]/2,
    Delta = sin^2(p/2)*sin^2(q/2)*sin^2((p-q)/2),
    S1 = 2[cos p+cos q+cos(p-q)],
    h = alpha+beta*S1, alpha,beta real.

## Method and budget

One bounded exact session. Permanent script scripts/verify_hex_trace_m3.py
retains every computational step used in the result. Start with analytic
restrictions and finite exact point inequalities (rational cosine slices
or rational multiples of pi). An infeasible finite subset must have an
explicit exact linear contradiction/certificate. Feasible point samples
do NOT certify global boundedness. A compatible candidate needs an exact
global proof, e.g. factorization/nonnegative polynomial certificate.

At most 256 point restrictions and 300 seconds cumulative solver time;
no floating-point search, nonlinear matrix solver, or support sweep. No
other m, orientation, lattice, s or physical interpretation. Stop at
the first exact certificate/witness, or OPEN_AFTER_M3_SCALAR_TEST.

## Outputs and levels

Permanent report, verifier and stdout; explicit finite certificate or
global bound if obtained. Outcomes SCALAR_INFEASIBLE_M3 /
SCALAR_COMPATIBLE_M3 / OPEN_AFTER_M3_SCALAR_TEST. PRELIMINARY, pending
independent review; no promotion, CURRENT_STATE change, commit or push
is implied. The previous Claude review does not cover this calculation.
