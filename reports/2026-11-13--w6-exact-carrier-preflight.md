# W6 exact R1 preflight: arithmetic obstruction

2026-11-13. Codex (OpenAI). Branch
`research/tetrahedral-support-rigidity-2026-11-09`.
Frozen contract `IR_CARRIER_W6_EXACT_EXAMPLE_GATE.md`, preregistration
`b8ece32257ee54a8d4c7dee3e2b031ab3c59a6a8`, charter SHA256
`519d579e9ff1d55be5e3303d256d74379b5ac147aa4ba9ca1de68c94ddbadc42`.
Stage 1 authorized by user «congela y ejecuta». **PRELIMINARY; exact
author derivation and algebra checks; no independent review or promotion.**

## 1. Verdict and scope

**`COUNTEREXAMPLE_VERIFIED` to membership in the declared carrier-group
hypothesis class, not to rate attainment.** The necessary H6_k(ii)
rational independence cannot hold for this fixed candidate if its
geometry satisfies H1. Every trivial-character carrier has distinct
scalar-shift copies with the same eigenvector spaces. Their phase
differences are rationally dependent on the depth offset. Thus H6_k(i)
cannot isolate one, and H6_k(ii) cannot handle their group.

This is a logical incompatibility of required hypotheses: if the
candidate fails H1 it is already outside the class; if it satisfies H1,
the exact symmetry forces the axis and then H6_k(ii) fails. It is not
necessary to assume or certify the remaining ledger to conclude that
the whole conjunction cannot hold. In particular this report does not
claim to have established H1 itself.

The first-stage geometry definition is well posed: the envelope
derivative defining s_0 exists, and the frozen radius satisfies
`0<r<1/6` (Sec. 3). The model, P-sector resource and lattice are checked.
The frozen abandonment rule is triggered; **Stage 2 is not executed**.
No parameters or resource vectors are changed. No exact R1 rate example
has been obtained. The possibility of a non-zero signal, or attainment
of the same exponential rate through resonant carrier interference,
remains OPEN and is not a continuation authorized by this contract.

## 2. Model, lattice and the scalar shift

Let Pi_h be the product of the three commuting projections in the
charter. The non-zero Pi_h are the four rank-one Bell projections with
`h_1 h_2 h_3=-1`, and sum to identity. Write

    W=(I-i N_0)/sqrt(2),
    D(p)=sum_h exp(i p.h/sqrt(3)) Pi_h,
    S(p)=W D(p).

Both factors are unitary for real p. The verifier also checks both
Laurent unitarity identities by coefficient convolution, the rank-two
P node, its phase, the isotropic compressed square `|q|^2 P/9` and
zero compressed traces. The P e_1 resource has squared normalizing
denominator `(1+1/sqrt(3))/2>0`, lies in P and has unit norm.

A basis of the step-generated lattice is B with columns

    b1=(1,1,1)/sqrt(3),
    b2=(2,0,0)/sqrt(3),
    b3=(0,2,0)/sqrt(3).

Every support vector has integer coordinates in this basis, while each
b_j is an integer combination of the support vectors. Hence it is
exactly the frozen lattice, of covolume `4/(3 sqrt(3))`, with reciprocal
lattice `B^(-T) Z^3`. No enlargement of the ambient lattice is used.

Set `V=n=(1,-1,1)/sqrt(3)` and

    u=3n=(sqrt(3),-sqrt(3),sqrt(3)).

The dual coordinates `B^T u=(1,2,-2)` show that u is primitive; in
particular `u.b1=1`. Its values on the four physical steps are 3 on V
and -1 on the other three. Define `q=(pi/2)u`. For every support step a,

    exp(i q.a)=-i,
    S(p+q)=-i S(p)                         for every complex p.       (1)

q has order exactly four on the reciprocal torus: `4q=2pi u`, while
`q.b1=pi/2` excludes lower positive orders. Thus if eta is dominant at
any fixed tilt, eta+jq, j=0,1,2,3, are distinct equally dominant points.
The whole matrices differ only by scalars; the corresponding right
and left eigenvector spaces coincide. This proves at least a four-point
dominant orbit, not that there are no other orbits. The old diagnostic's
list of two points is therefore incomplete on the declared torus.

## 3. Exact axial envelope and the frozen radius

This establishes the first required setup condition before applying
the arithmetic stop. For `xi=t n`, t>0, put

    a=exp(-t/3),  b=exp(t),  c=1/sqrt(2).

In the Bell basis, `D(eta-i xi)` has modulus b on Pi_V and a on its
orthogonal complement. Thus `S(eta-i xi)=U diag(b,a,a,a)` with a unitary
U. For a unit vector v in Pi_V, `Pi_V N_0 Pi_V=0`, so
`|<v,Uv>|=c`; its off-diagonal row has norm `sqrt(1-c^2)`.

Let z be the modulus of any eigenvalue, with eigenvector `x v+y`,
`y perpendicular v`. The operator norm bounds z<=b. If z>a, its
eigenvector has x non-zero and unitarity gives

    ||y||^2/|x|^2 = (b^2-z^2)/(z^2-a^2).

The v component of the eigen-equation gives

    z <= bc + a sqrt(1-c^2) sqrt((b^2-z^2)/(z^2-a^2)).

If z>bc, squaring and multiplying by `z^2-a^2` yields

    (z^2-c(b-a)z-ab)(z^2-c(b+a)z+ab) <= 0.                 (2)

The second factor is positive for z>=bc: its value at bc is
`ab(1-c^2)>0` and its derivative there and to the right is positive
since b>a. Hence z is at most the positive root R of
`R^2-c(b-a)R-ab=0`. The cases z<=a or z<=bc obey the same bound,
since that quadratic is negative at both a and bc. This proves a
**global torus** bound on the spectral radius, not a local saddle check.

Equality is attained at `eta=-(pi/4)u`. After removing its common phase
`exp(i pi/4)`, D has entries -b on Pi_V and a elsewhere. The orthonormal
plane spanned by v and N_0 v is invariant, with block

    (1/sqrt(2)) [[-b, -i a], [i b, a]].

Its characteristic polynomial is `lambda^2+c(b-a)lambda-ab`;
its negative root has modulus R. This independently supplies the
attainment side of the global bound. Therefore, for every t>0,

    Phi(t n)=log R=t/3+asinh(sinh(2t/3)/sqrt(2)),
    s(t)=d/dt Phi(t n)
        =1/3+(2/3) cosh(2t/3)/sqrt(1+cosh(2t/3)^2).

It follows directly that `1/3<s(t)<1`. At the frozen `t_0=1/1000`,
the derivative exists and `r=(1-s(t_0))/4` satisfies `0<r<1/6`.
No floating-point radius, numerical maximization or limiting replacement
of t_0 was used. The verifier checks the block polynomial and the
factorization in (2); the inequalities and attainment argument are the
written analytic proof above.

## 4. Necessary geometry if H1 holds

The exact coefficient covariance in the verifier uses the order-three
rotation `T=F T0 F`, where F=diag(-1,1,-1) and T0 cyclically permutes
the coordinate axes. Its fixed space is the axis Rn. A corresponding
unitary is `R2 (t tensor t) R2^dagger`, where
`R2=sigma_2 tensor I` and `t=(I-i sum sigma_j)/2`. It maps each
coefficient A_h to A_{Th}; thus `S(Tp)` is unitarily conjugate to S(p).
Consequently Phi, its Legendre transform I, and both frozen balls are
T-invariant.

Suppose the unique minimizer and differentiability required by H1 hold.
Uniqueness forces `v_*=beta n`. Since `v_*` lies in
`closed_ball(n,2r)` and `r<1/6`, beta>0. Differentiability and symmetry
force `xi_*=grad I(v_*)` to lie on the same axis.

To fix its sign, note that `det S(p)=1`: det W=1 and the four raw
support vectors sum to zero, so det D(p)=1, also for complex p.
Hence every tilted spectral radius is at least 1, Phi>=0, and
`I(0)=0` since Phi(0)=0. The subgradient inequality for the convex I
then gives `xi_*.v_* >= I(v_*)=K_*>0`. Thus xi_* is a positive
multiple of n. The non-zero gradient minimizing I over the regional
ball must expose its unique facing point:

    v_*=(1-2r)n,   w_A=r n,   w_B=(1-r)n,
    alpha:=u.w_A=3r,   u.v_*=3-2alpha.                       (3)

The primitive dual normal in the positive n direction is precisely
u from Sec. 2: if c n belongs to L*, testing b1 gives c/3 integer.
This uses H1 as a necessary premise; it is not an independent proof
that the regional minimizer or its differentiability exists.

## 5. Exact failure of H6_k(ii), with branch corrections

If there is no non-zero trivial-character carrier, the R1 target already
fails. Otherwise take one, eta, with layer character `exp(i phi u.x)`.
Under the q shift (1), its character becomes `exp(i(phi+pi/2)u.x)` and
its dominant eigenvalue is multiplied by -i. The shifted point is
distinct and has the same eigenvector spaces; its character is still
trivial on `L intersect u^perp`. It cannot be excluded from the
inseparable group by H6_k(i).

Use the full phase definition of carrier Stage A,
`psi=arg(lambda)+omega_0-phi u.v_*`. For principal character phases
and arbitrary eigenphase branches write

    phi' - phi = pi/2-2pi k,
    arg(lambda')-arg(lambda) = -pi/2+2pi m,

with integers k,m. With (3), the normalized phase difference is exactly

    delta:=(psi'-psi)/(2pi)
          =-1/4-(1/4-k)(3-2alpha)+m
          =(m+3k-1)+(1/2-2k)alpha.

Therefore

    2 delta -(1-4k)alpha-2(m+3k-1)=0.                        (4)

This is a non-trivial integer relation among `1`, `u.w_A` and the
required phase difference. It contradicts H6_k(ii), whether alpha is
rational or irrational. Changes of torus representatives leave the
character modulo 2pi and only change the integers above; all branches
retain a relation. In a no-wrap branch it reads simply
`delta=-1+alpha/2`.

Any additional carriers do not restore the failed pairwise independence
inside this inseparable orbit. H9(ii), depth-average magnitudes and
rotation cannot repair this necessary H6 condition. The frozen stop
rule applies here; they are not evaluated.

## 6. Second route and ledger

An independent formulation of (1) is real-space support arithmetic.
Every one-step displacement has `u.a == -1 (mod 4)`, so every non-zero
N-step kernel coefficient is on `u.(y-x) == -N (mod 4)`.
Taking its Fourier character gives
`S(p+q)^N=(-i)^N S(p)^N`, exactly as obtained by the direct coefficient
calculation. This explains the carrier copies without asserting that
their contributions cancel the full signal. The phase relation (4) is
also checked both in its general branch form and its no-wrap form by
the permanent certificate.

| Ledger row | Execution status |
| --- | --- |
| Model/node/resource normalization | Exact identities checked; analytic unitary/nodal interpretation above. |
| Frozen derivative/radius | Global axial envelope derived; derivative exists and radius positive. |
| Ambient lattice/dual normal | Basis and primitive vector checked; identification with the tilt normal is conditional on H1. |
| H1 | Not fully established; its symmetry consequences suffice for the incompatibility proof. |
| H2 double-prime/H8 | Full global dominant inventory and Hessians not evaluated; at least four scalar copies exist at any tilt. |
| H6_k(i) | No isolation of a trivial carrier from its scalar copies, conditional on the required geometry. |
| H6_k(ii) | Contradicted by (4) under H1; necessary-condition failure closes the gate. |
| H9(ii), depth mu, H5/H7/H10_k | Not executed after the stop. |
| Operational rate example | Not obtained; no rate-attainment counterexample claimed. |

## 7. Reproduction and provenance

Permanent script committed **before** its first run at `27d8ba3`:

    python3 -B scripts/verify_w6_exact_carrier_preflight.py

86/86 exact algebra checks, exit 0; Python 3.12.3, SymPy 1.14.0.
Stdout: `reports/2026-11-13--w6-exact-carrier-preflight-verifier.txt`.
Script SHA256:
`1cfc3b717ab46ffbe425f645399baf927f16e3092d1490ce4bb41dd55341b73b`.
No project imports, no float comparisons, no scans, no ephemeral script,
no old-verifier modification. Passing these checks alone does not
certify the written inequalities or the global hypothesis ledger.

Execution began after freeze at `2026-11-13T13:13:31Z`. The verifier
was observed completed by `13:17:31Z`; writing and analytic audit of
this record are part of the Stage 1 session. The terminal outcome is a
structural hypothesis obstruction, not budget exhaustion. The local
literature index was inspected before work; no primary literature claim
or novelty verdict was inferred from it. No external review was sent.

Stage 1 execution, including the written proof audit, ended at
`2026-11-13T13:20:07Z` (6 minutes 36 seconds after the recorded start),
within the 90-minute cap. Subsequent status, README and Git updates
are documentary. Stage 2 is closed without execution by the stop rule.
