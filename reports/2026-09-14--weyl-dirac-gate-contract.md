# Weyl/Dirac exact gate — execution contract

Date: 2026-09-14. Baseline: `44ad178`.

This contract is written before implementation or execution of the verifier.
It specifies a local calculation under the initial freeze; it does not change
the canonical status in `state/CURRENT_STATE.md` or authorize scope expansion.

## Cases and conventions

- Standard zero-node Pavia symbols: d=1 A; d=2 A and its transpose;
  d=3 A+, A- and their transposes. The additional d=2 on-site rotation
  parameter is fixed to zero. No exhaustive classification of that deformation
  or of all isotropic QCAs is claimed.
- Momentum coordinates are Cartesian, Euclidean, and dual to unit-length
  one-step neighbors. One complete automaton update is one time unit.
  Define `q_j = k_j/sqrt(d)`; d=1 uses `q=k`.
- Weyl matrices are equations (15)-(17) of arXiv:1601.04832v1, PDF p.6.
  The scalar part of each matrix fixes `cos(theta)=tr(W)/2`.
  Do not copy the inconsistent opposite sign in the sentence after (15).
- Dirac coupling is `D=[[n W,i m I],[i m I,n W^dagger]]`, equation (9)
  of arXiv:1601.04842v1. Take `0<m<1`, `n=sqrt(1-m^2)>0`.
  The dagger is mandatory; equation (23) of 1601.04832v1 omits it.
- Use `D=exp(-i H)`, the logarithm continuous from the identity near the
  massless zero node, and massive phases `+/-omega`,
  `omega=acos(n u)`, `M=omega(0)=asin(m)` in `(0,pi/2)`.
- Compare actual nonzero one-step Fourier support. At `m=0` and `m=1`
  recompute support separately. Distinguish active support from an unchanged
  declared substrate neighborhood at the decoupled endpoint.

## Required verification, frozen before execution

1. Reconstruct each published Weyl matrix independently as an ordered product
   of Pauli rotations; extract its nonzero Laurent coefficients.
2. Verify unitarity and the characteristic quadratic as exact identities.
3. Enumerate supporting facets of the extracted neighbor hull exactly;
   obtain inradius and maximum support. Establish the directional support
   formula analytically from the complete corner set.
4. Compute all first spatial derivatives and the full Hessian of the scalar
   Weyl symbol at zero; check isotropy including mixed entries.
5. Check Dirac unitarity, its characteristic quadratic and the square of its
   Hermitian sine part. Derive the logarithm from this algebra.
6. Independently differentiate the exact eigenphase and logarithm prefactor
   to compare `c_H`, `c_{omega^2}` and the quadratic mass-term correction.
7. Treat the open mass interval analytically, with separate massless and
   decoupled endpoints. Derive the small-mass series and a joint continuum
   scaling; finite samples cannot establish an interval assertion or limit.
8. Negative controls must detect a missing Dirac dagger, a reversed 3D
   phase sign, and the omission of the quadratic mass correction.

## Acceptance and output

All machine checks use exact symbolic arithmetic: tolerance is zero. A
nonzero or unresolved residual stops the verifier with a nonzero exit code.
No numerical tolerance, fitting, scan, or post-output change of acceptance
is allowed. A checker failure is distinguished from a false hypothesis.

Equality labels are `EXACT`, `ASYMPTOTIC`, `FALSE`, and
`CONVENTION_DEPENDENT`; a degenerate endpoint is explicitly qualified.
The analytic report must explain any interval inequality and limit, rather
than inferring it from machine samples.

The permanent verifier lives in `scripts/verify_weyl_dirac_gate.py`.
It emits a deterministic Markdown record, including source/script/contract
hashes and dependency versions, only after every check passes. Its default
is stdout; `--output` explicitly writes the retained record.

Completion of this battery supplies evidence for the seven declared symbols
and their block couplings. It does not prove A, general B*_0, general B*_cont,
novelty, or any theorem for a new substrate. Canonical promotion requires the
separate reason-recording commit specified by PROJECT_INSTRUCTIONS.
