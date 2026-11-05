# Scalar method beyond S19: bounded analytic audit

Date: 2026-11-05. Author: Codex (OpenAI).
Contract: theory/HEX_TRACE_SCALAR_GATE.md, written before this analysis.
Status: PRELIMINARY, not independently reviewed, not promoted.
Outcome: OPEN_AFTER_SCALAR_ANALYSIS. No general incompatibility theorem
and no compatible scalar polynomial have been obtained in this session.

## 1. The exact question

The S19 scalar obstruction is support-specific: D6 invariance leaves four
orbit coefficients, normal rigidity leaves one, two point bounds fix it,
and a third point contradicts the remaining bound. Larger supports have
more orbits; the uniqueness step is not inherited.

For H_v with v=a*g1+b*g2 nonzero, let L=|v|, normalize the frequency
lattice to Lambda/L, and write r=sqrt(3)/2. Does a real finite Fourier
polynomial f with spectrum inside H_v/L satisfy

    -1<=f(k)<=1, f(0)=1,
    f(t*n_j)=cos(r*t) on all six facet normals?

One may impose evenness and C6 invariance by averaging. D6 averaging
inside the same lattice is available for S19; for a general oriented
lattice hexagon a geometric reflection need not preserve Lambda.
Do not assume that stronger average in the universal question.

If no such polynomial exists for every v, the trace argument excludes
saturation for the declared walks. If one exists, these scalar conditions
are insufficient. It would not yet produce a unitary 2x2 symbol, a product
walk, or a counterexample to the saturation claim itself.

## 2. Hessian and transverse derivative: necessary conditions

These statements require only real boundedness, normal cosines and the
finite frequency support; not the full amplitude matrices.

First, the Hessian of f at zero is fixed. On three distinct facet-normal
lines its quadratic form is -r^2. A symmetric 2x2 matrix whose quadratic
form agrees with -r^2 I on three distinct unoriented lines equals -r^2 I:
their difference is a homogeneous quadratic vanishing on three lines,
so it is zero. Thus D^2 f(0)=-r^2 I. This does not require a separate
scalar isotropy assumption.

Fix a facet normal n and its unit tangent e. Put
g(t)=partial_e f(t*n). Then

    g(t)=0 for every real t.                                      (T)

Here is a finite-degree proof that applies to all lattice H_v. For the
facet joining v to Rv, set D=a^2+ab+b^2 and d=gcd(|a|,|b|). In lattice
coordinates its edge vector is (-a-b,a). A frequency h=(m*g1+l*g2)/L
has normalized projection

    (h.n)/r = [a*m+(a+b)*l]/D.

Therefore all normal frequencies are integer multiples of
delta=r*d/D, with maximal degree N=D/d (a positive integer). Rotation
gives the same property on the other facets. The proof needs only a
commensurate grid, not that every layer is populated.

Use theta=delta*t and write G(theta)=g(theta/delta), a real trigonometric
polynomial of degree at most N. At theta_j=j*pi/N, j=0,...,2N-1,
f((theta_j/delta)*n)=(-1)^j. Boundedness makes each such point a global
maximum or minimum in the full k-plane, so its transverse derivative is
zero: G(theta_j)=0. Multiplying G by z^N, z=exp(i*theta), gives an
ordinary polynomial of degree <=2N vanishing at all 2N-th roots of unity.
It is a constant multiple of z^(2N)-1, so reality implies
G(theta)=b*sin(N*theta) with b real. But

    G'(0)=partial_n partial_e f(0)/delta=0

by the Hessian identity above. Hence b=0 and (T) follows.

Equivalently, in Fourier coefficients b_h,

    sum_{h.n=lambda} (h.e)*b_h = 0

for every normal layer lambda, in addition to the usual layer sums
(1/2 on each extreme layer, zero on intermediate layers). These are
necessary first-moment constraints on the scalar coefficients.

## 3. Exact residual form for the aligned hexagon family

This section concerns v=m*g1, m a positive integer; it does not silently
identify all oriented lattice hexagons with this family. Set
p=k.g1/m, q=k.g2/m. Frequencies in these variables have integer pairs
(i,j) with max(|i|,|j|,|i+j|)<=m. Averaging over D6 is valid here.
The prescribed normal restrictions become cos(m*q) on p=0, cos(m*p)
on q=0 and on p=q. A particular interpolant is

    f_m^0 = [cos(m*p)+cos(m*q)+cos(m*(p-q))-1]/2.

Every D6-invariant real candidate with those restrictions has the form

    f = f_m^0 + Delta*h,
    Delta = sin^2(p/2)*sin^2(q/2)*sin^2((p-q)/2),                 (R)

where h is a real D6-invariant Laurent polynomial supported inside the
radius-(m-2) lattice hexagon. For m=1 the residual must be zero; for m=2
it is a constant. The assertion concerns interpolation and support, not
boundedness: that still has to be imposed on the full expression.

Proof: write d=f-f_m^0, z=exp(i*p), w=exp(i*q). Vanishing on p=0, q=0
and p=q gives the factors z-1, w-1 and z-w in the Laurent ring. The
reflection fixing p=0 sends (p,q) to (-p,q-p). Differentiating invariance
at p=0, where d and partial_q d vanish, gives partial_p d=0. Thus the
factor z-1 has multiplicity at least two. The conjugate reflections give
the other double factors. They are distinct irreducibles in the Laurent
UFD, so their product divides d. Since

    Delta = -(z-1)^2*(w-1)^2*(z-w)^2/(64*z^2*w^2),

the quotient h is Laurent. Delta is D6 invariant and real, hence so is
h (first on the dense set Delta!=0 and then identically). If h is nonzero,
the Newton polytope of a product is the Minkowski sum: each exposed leading
face is a product of nonzero face polynomials in an integral domain.
Delta has Newton polygon H_2. Since Delta*h=d has support inside H_m,
the six facet inequalities bound the support of h by H_(m-2). If m=1,
their intersection is empty; h must be zero. Conversely such an h gives
the stated support and normal restrictions, though not necessarily bounds.

For m=2, f_m^0=-1/2+S3/4 and the S19 one-parameter family satisfies

    fbar = f_2^0 - 32*a1*Delta.

Thus the supplied S19 argument forces h=16/3 and disproves boundedness
of that unique candidate. For m>=3 the quotient can be nonconstant;
its exclusion cannot be inferred from the constant case.

The permanent checker `scripts/verify_hex_trace_scalar_structure.py`
checks the Laurent factorization, double zeros, D6 invariance, exact
Newton polygon and the S19 residual identity. The proof of universal
divisibility in this aligned family is the analytic argument above,
not something certified by testing a finite set of radii.

## 4. What this does not solve

The first-moment constraints are already consequences of the scalar
conditions, not extra assumptions or a new witness. On reflection axes
they also follow immediately from reflection symmetry. For S19, whose
average is D6 invariant, adding them cannot improve the scalar reduction.
For general oriented lattice hexagons the derivative argument supplies
them without an illicit reflection average.

The zero-count argument does not apply to partial_e^2 f: at the extremal
points only an alternating sign is forced for that derivative, not zero.
It therefore cannot be iterated here to conclude that all transverse
dependence vanishes. That would be an unsupported generalization.

No exact compatible polynomial or general contradiction is provided.
No larger-support solver, numerical scan, or new walk construction was
run. The bounded analysis ends here under the contract. Any further
attempt should address scalar feasibility itself, rather than treating
these necessary constraints or additional bounded cases as a proof for
all supports. The universal walk saturation question remains OPEN.

## 5. Provenance and review boundary

This is an analytic derivation written in the permanent report; the
explicit Laurent checks have their permanent script, and no temporary
script generated the conclusions. The normal projection formula
is derived from the determinant with edge (-a-b,a); at v=2*g1 it gives
N=2, and at v=2*g1+g2 it gives N=7, matching the respective existing
layer descriptions. These are consistency checks, not independent review.
The sealed S19 review has a separate scope and does not review this
general-method report. No literature novelty claim is made.

Local algebra execution: `python3 -B scripts/verify_hex_trace_scalar_structure.py`,
exit 0, 6/6 exact checks, Python 3.12.3 / SymPy 1.14.0. Permanent stdout:
`reports/2026-11-05--hex-trace-scalar-structure-verifier.txt`.
Script SHA256:
`a00574f90b6c2191dbb92d20f75b260c3a6f4987b683e97a96c7585717647ce3`.
