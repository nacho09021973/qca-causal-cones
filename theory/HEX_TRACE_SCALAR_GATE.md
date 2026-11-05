# HEX_TRACE_SCALAR — bounded scalar-method audit

Date: 2026-11-05. Author: Codex (OpenAI).
Authorization: user «autorizado, adelante», following the three-step proposal
in this session: document the S19 trace proof, exact permanent verifier,
bounded independent review, then investigate the sufficiency of scalar
constraints under an explicit charter. This is a new contract, not an edit
of the frozen HEX_SUPREMUM gate. Recorded before the new verifier is run
and before investigating the general scalar question; no Git freeze commit
is claimed. The S19 derivation was supplied by the user before this charter.

## Known, question, abandonment

Known: HEX_CEILING report Sec. 3 Step 1 gives facet-normal rigidity under
saturation, for s=2, scalar node and traceless isotropic linear term.
HEX_SUPREMUM B19 is promoted in CURRENT_STATE Sec. 14. The user supplied
an alternative scalar derivation. S25 has a separate preliminary report;
it is neither rerun nor promoted here.

Question A: does the supplied scalar proof correctly reproduce S19?
Abandon A if the necessary scalar reduction or its exact contradiction
fails. A local verifier is not independent review.

Question B: can bounded real, even, hexagonally symmetric finite Fourier
polynomials satisfy all the normal-line cosines forced by saturation?
Abandon the proposed *universal scalar obstruction* at the first exact
compatible polynomial. This does not establish a unitary walk. An exact
incompatibility for a bounded support is not a universal obstruction.

## Domain and quantifiers

Walk input: W_hex^sym as in HEX_SUPREMUM Sec. 2: s=2 unitary Laurent
symbols on a triangular lattice, scalar node at zero (phase removed),
traceless isotropic A(n), c0>0, regular centred hexagonal exact hull,
maximum support radius 1. No product factorization is used for a gap.

Scalar relaxation: for every nonzero lattice vector v, H_v is the regular
hexagon with vertices R^j v, normalized by |v|. Frequencies belong to
(Lambda/|v|) intersect H_v. A candidate f is real, even, invariant under
the geometric dihedral group of H_v when that group preserves the
frequency lattice, satisfies -1<=f<=1 and f(0)=1, and
f(t n_j)=cos(sqrt(3)t/2) for all real t and all six unit facet normals.
For rotated lattice hexagons whose reflections do not preserve Lambda,
use C6 averaging only; do not silently enlarge the frequency lattice.
The S19 argument uses its actual D6-invariant frequency lattice.

## Method and finite budget

A: independent exact orbit enumeration, Laurent coefficient comparison,
trigonometric evaluations and a second contradiction point if available;
all code remains in scripts/verify_hex_trace_s19.py. No numerical verdict.
Write the analytic bridges explicitly. Review by revision-ciega from
another model family: one initial round, at most one repair re-review.
An operational failure is recorded and diagnosed, never counted as review.

B: one bounded analytic session, no support-by-support solver campaign.
First derive necessary consequences of scalar boundedness on saturated
normal lines. Test an explicit construction only if there is an analytic
reason to do so; exact checks in a permanent script. No nonlinear solver
or numerical search is authorized by this contract. Stop with either an
exact compatible polynomial, a general proof, or OPEN_AFTER_SCALAR_ANALYSIS
with the remaining obstruction identified. Further work needs a new scope.

## Outputs and evidence

S19 report plus permanent verifier; sealed review input/output and author
response. General report distinguishes analytic necessary conditions,
scalar feasibility and unitary realizability. PRELIMINARY until independent
review; promotion remains a separate user decision. No novelty claim,
literature absence claim, uniform gap, general QCA law or extension to s>2.
