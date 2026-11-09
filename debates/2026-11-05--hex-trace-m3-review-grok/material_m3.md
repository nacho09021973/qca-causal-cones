# Mathematical dossier: aligned hexagon, m=3

Author: Codex (OpenAI). Date: 2026-11-05.
This dossier contains the mathematical claim and arguments, with no
earlier review verdicts. It is a manually prepared exposition, not a new
calculation or a change to the source theorem. Source baseline:
ad842076a9e76c6ffccf31e7882438907ea46659.

Source mathematical report: reports/2026-11-05--hex-trace-m3.md,
SHA256 10549695289c4446532e1810c2b8a7fcb32ed7c76185594bdc9dfe56d6ca3c12.
Source residual argument: reports/2026-11-05--hex-trace-scalar-method.md,
SHA256 321b53d0dbc234724188b350a1ea050fc79747c5f7e038cdb17cd834b689423b.
Source rigidity argument: reports/2026-11-01--hex-ceiling.md Sec. 3 Step 1.
The attached verifier is unchanged from the baseline, SHA256
88a20b3d99b2164b91557d48b69fb113e3e3e5adf7662c088347a0146669998f.

## 1. Claim and frozen class

Let g1=(1,0), g2=(1/2,sqrt(3)/2), Lambda=Z*g1+Z*g2. Normalize the
radius-three lattice ball to maximum physical radius one. Its support
set is

    S = {(i*g1+j*g2)/3: i,j integers,
         max(|i|,|j|,|i+j|)<=3}.

It has 37 points and its convex hull H is the aligned regular hexagon
with vertices R^j*g1, j=0,...,5, R the counterclockwise 60-degree
rotation. Its inradius is r=sqrt(3)/2.

Scalar claim: there is no real finite Fourier polynomial supported in S
such that -1<=f<=1 globally, f(0)=1, and f(t*n)=cos(r*t) on every unit
facet normal n of H. No symmetry of f is initially required.

Walk consequence: let U(k) be any s=2 unitary Laurent symbol with F inside
S and exact hull conv(F)=H, scalar node U(0)=exp(-i*phi)I, and phase-
removed linear generator A(n) Hermitian, traceless and isotropic,
A(n)^2=c0^2*|n|^2 I, c0>0. Such a walk cannot saturate c0=r_in(H).
The existing ceiling then gives c0<r_in(H). No product factorization is
used. This claim keeps the exact hull, normalization, s and node
hypotheses; it is not a statement about all hexagons, other radii,
nonaligned orientations or a uniform quantitative gap.

## 2. Scalar averaging and residual reduction

Put p=k.g1/3, q=k.g2/3. Facet-normal lines are p=0, q=0 and p=q;
the required restrictions are cos(3q), cos(3p), cos(3p), respectively.
D6 preserves the lattice Lambda/3, S, H and its normal lines. Averaging
a candidate over D6 preserves realness, the bounds, value at zero,
support and these cosines (cos is even). Thus a candidate, if it exists,
has a D6-invariant average. It suffices to exclude such averages.

Define

    f0 = [cos(3p)+cos(3q)+cos(3(p-q))-1]/2,
    Delta = sin^2(p/2)*sin^2(q/2)*sin^2((p-q)/2),
    S1 = 2[cos p+cos q+cos(p-q)].

f0 is real, D6 invariant, supported in S and has the prescribed normal
restrictions and value at zero. Its bounds are not assumed. For a
symmetric candidate let d=f-f0. In the Laurent ring C[z^+/-1,w^+/-1],
z=exp(ip), w=exp(iq), d vanishes on z=1, w=1 and z=w. The real-torus
identities imply Laurent identities (multiply by a monomial to obtain
an ordinary polynomial with infinitely many roots).

The reflection fixing p=0 is (p,q)->(-p,q-p). Differentiating the
invariance of d at p=0 gives 2*partial_p d=-partial_q d=0 there.
Consequently (z-1)^2 divides d. The conjugate reflections give the double
factors (w-1)^2 and (z-w)^2. They are distinct nonassociated irreducibles
in the Laurent UFD, so their product divides d. The identity

    Delta = -(z-1)^2*(w-1)^2*(z-w)^2/(64*z^2*w^2)

therefore implies d=Delta*h with h Laurent. Delta is real and invariant,
so h is real and invariant on the dense set Delta!=0 and hence everywhere.

The Newton polygon of Delta is H2 in integer-frequency coordinates,
max(|i|,|j|,|i+j|)<=2. For nonzero h the Newton polygon of a product is
the Minkowski sum: exposed initial forms multiply and cannot vanish
in an integral domain. Since d has support inside H3, the six facet
support inequalities bound the support of h inside H1. If d=0 then
h=0. H1 has only the origin and one D6 orbit of six points, so

    f=f0+Delta*(alpha+beta*S1), alpha,beta real.

This is a necessary interpolation/support reduction. It does not
certify boundedness. No candidate matrix symbol is being inferred.

## 3. Four rational point inequalities

On p=2q, let x=cos(q). Every x in [-1,1] is realizable. Then

    f0(x)=[T6(x)+2*T3(x)-1]/2,
    Delta(x)=(1-x^2)*(1-x)^2/4,
    S1(x)=4*x^2+4*x-2,

where Tj(cos q)=cos(jq). For -1<x<1, Delta>0. Thus the necessary upper
and lower inequalities are

    alpha+S1*beta <= (1-f0)/Delta,
    -alpha-S1*beta <= (1+f0)/Delta.

The proposed exact point values are:

| x | f0 | Delta | S1 |
|---|---|---|---|
| 5/16 | -1206391/1048576 | 27951/262144 | -23/64 |
| -1/2 | 1 | 27/64 | -3 |
| 3/8 | -17671/16384 | 1375/16384 | 1/16 |
| 13/16 | -1265351/1048576 | 783/262144 | 249/64 |

Taking respectively upper, lower, upper, lower gives

    alpha-(23/64)*beta <= 204997/10164,
    -alpha+3*beta <= 128/27,
    alpha+(1/16)*beta <= 6811/275,
    -alpha-(249/64)*beta <= -7475/108.

Multiply these by 64/169,64/169,64/245,64/245. All weights are positive.
The alpha coefficients cancel. The first pair contributes +beta and
the second contributes -beta. The right side is

    (64/169)*(204997/10164+128/27)
    +(64/245)*(6811/275-7475/108)
    = -7362262528/3381753375 < 0.

This would force 0<=a strictly negative rational. No real pair satisfies
even these four necessary inequalities. Hence no globally bounded scalar
candidate exists if the reduction and arithmetic above are correct.

## 4. Explicit bridge from a walk to the excluded scalar

Suppose a declared walk saturates c0=r=sqrt(3)/2. Remove the constant
phase by U_tilde=exp(i*phi)*U, so U_tilde(0)=I. F, unitarity and the
phase-removed generator are unchanged. Define

    f_U(k)=Re Tr U_tilde(k)/2.

Unit-modulus eigenvalues give -1<=f_U<=1 and f_U(0)=1. Real part adds
at most reflected frequencies: supp(f_U) is inside F union (-F),
which is inside the centrally symmetric set S.

Facet rigidity has this finite-degree argument (the case of equality of
the classical Bernstein bound). On a normal n the frequencies h.n are
integer multiples of delta=r/3, lying between -r and r. For a unit
eigenvector x of A(n) with eigenvalue +r, write
q(s)=<x,U_tilde(s*n/delta)x>, of degree N=3 in s. Unitarity gives |q|<=1,
q(0)=1, q'(0)=-i*N. Thus P(z)=z^N*q(s), z=exp(is), is an analytic
polynomial bounded by one on the disk, P(1)=1 and P'(1)=0. The classical
boundary fixed-point lemma (Julia--Caratheodory) forces P to be constant:
a nonconstant disk self-map with boundary fixed point 1 has positive
angular derivative there. Hence q(s)=exp(-i*N*s). Equality in Cauchy--
Schwarz forces U_tilde(t*n)x=exp(-i*r*t)x. Apply the conjugate-frequency
argument to the eigenvector with eigenvalue -r.

Since A(n) is Hermitian, traceless, s=2 and r>0, its two eigenspaces
have rank one. Therefore

    U_tilde(t*n)=exp(-i*r*t)*P_+(n)+exp(i*r*t)*P_-(n),
    f_U(t*n)=cos(r*t).

This argument uses the commensurate grid, unitarity, node and isotropy,
not minimal support. D6 averaging of f_U now produces a scalar candidate
of Sec. 2, excluded by Sec. 3. Together with the standard ceiling
c0<=r_in from the same normal-frequency Bernstein bound, this gives
strict non-attainment in the declared walk class.

## 5. Computational coverage and limits

The attached script retains its rational point schedule and exact
two-variable Fourier--Motzkin elimination. It generates 146 necessary
inequalities and discovers the displayed four-row certificate. The
script checks certificate point values again by Laurent substitution,
and explicitly checks nonnegative weights, vanishing coefficients and
a negative constant. Mathematical sampling is not used as a feasibility
certificate. Timings are operational diagnostics only.

The result does not depend on trusting the discovery algorithm: the
four-row certificate can be checked directly. The code does not
mechanize the analytic averaging/divisibility/rigidity proofs. A reviewer
with no tools must not claim execution. No novelty or uniform gap
statement is requested or inferred. No scientific promotion is made.
