# Local audit of Fable's tetrahedral signal candidate

2026-11-10. Codex. User authorized checking the candidate locally.
Audit charter: `TETRAHEDRAL_IR_FABLE_AUDIT_GATE.md`, commit `269ada5`.
Candidate: `reviews/2026-11-10-tetrahedral-ir-signal-fable52/informe_opus.md`,
full-file SHA256 `1093e4f3d26f0ef50cc31be648ff20e96261b04af15e9f1b82fde0b865c87d06`.
The original output is preserved byte-for-byte. No new external calls.

## Verdict and evidence ceiling

**AUDIT_PASS_WITH_LOCAL_DERIVATION**, for the two-sided order bound and
eventual positivity under the exact protocol of `TETRAHEDRAL_IR_SIGNAL_GATE.md`.
The detailed local derivation below supplies the compressed analytic steps;
the exact verifier checks algebraic inputs only. This is a local, non-blind
cross-family audit with prior context, not a sealed new review. The protocol
analysis was itself written by Codex. All new conclusions remain
**PRELIMINARY**, with no automatic promotion or novelty finding.

The checked conclusion is: there exist c,C>0 and a finite, non-effective
N_0 such that c N^-5 <= L_N <= C N^-5 for every integer N>=N_0.
The remainder is qualitative little-o, not an effective error bar.
We do not assert the candidate's conditional exact leading coefficient
formula, an N^-13/2 interference order, or a numerical positivity threshold.
The leading response is supported away from a fixed small neighbourhood
of zero momentum. It is not exclusively IR spectral transport, although
the operations satisfy the declared asymptotic admissibility definition.

Known: fixed U(k), phases and protocol; Fable's text is a proof candidate,
not mathematical authority. Question: do its spectral and analytic inputs
exclude cancellation? Stop acceptance on a failed bound or a missing
uniformity/positivity argument. No new N samples or protocol changes.

## 1. Exact inputs checked independently

`scripts/verify_tetrahedral_fable_audit.py`: **55/55 exact SymPy checks**,
exit 0; stdout in `2026-11-10--tetrahedral-fable-audit-verifier.txt`.
No reviewed verifier was imported or modified. The fixed matrix definitions
are reconstructed directly, with the specified Fourier signs.

Checks cover channel projectors and colour increments, Laurent trace and
characteristic coefficients, determinant factors, both nodal compressions,
the diagonal-axis characteristic polynomial and invariant 2D block,
eigenvalue simplicity, the input/encoder overlap, the two target group
velocities, and source/detector boundary coefficients. A simple-spectrum
witness has characteristic polynomial lambda^4+(4/3)lambda^2+1 and nonzero
discriminant. Therefore the degeneracy discriminant of U(k) is not
identically zero; its zero set has measure zero.

On k=3s n, n=-v, the four phases are

    s±pi/4,   -s±alpha(s),   cos alpha=cos(2s)/sqrt(2),
    alpha'=2 sin(2s)/sqrt(1+sin(2s)^2).

The active block has off-diagonal entry
e^(-i pi/4)(e^(3is)-e^(-is))/2, nonzero when sin(2s)!=0.
Its eigenvalues cross a flat branch only when sin(2s)=0. The cyclic
symmetry fixes the axis, so the full gradient of a simple eigenphase
there is parallel to n. Hence the branch -s+alpha has velocity
(1-alpha')v/3, attaining (1+sqrt(2))v/3 on this axis. This is an axial
extremum, not a calculation of the global maximum group speed.

For sin(2s)=-5/sqrt(39), choosing s in (-pi/4,0), alpha'=-5/4 and
the velocity is 3v/4. For sin(2s)=-43/sqrt(2247), also with s in that
interval, alpha'=-43/32 and the velocity is 25v/32.

Let S be the singlet and e_±=sqrt(2)P_±S. The encoded spin M chi lies
in P_+, and |<S,M chi>|^2=(1+1/sqrt(3))/4>0. In the active basis
it consequently has nonzero first component and zero second component.
Nonzero off-diagonal coupling forces both components of each simple
active eigenvector to be nonzero. This proves the required overlap with
the selected fast branch; merely knowing <S,M chi>!=0 would not suffice.

## 2. Low-frequency estimate: filling Lemma A

Use zeta for the smooth momentum cutoff, avoiding the candidate's reuse
of chi for both a spinor and a function. Choose zeta=1 near zero, supported
in |k|<2kappa, with kappa fixed and sufficiently small. It will also be
small enough that zeta=0 on the fast spectral patch selected below.

The two eigenvalue clusters around exp(∓i pi/4) remain separated for
complex k in a neighbourhood of zero. Resolvent contour integrals give
bounded analytic projectors P_±(k). On each contour choose the local
logarithm of U/exp(∓i pi/4), setting the function to zero on the other
contour. The resulting full 4x4 analytic matrices H_±(k) are Hermitian on
real k, vanish at zero, and satisfy

    U(k)^N P_±(k)=exp(∓iNpi/4) exp(-iN H_±(k))P_±(k).

The zero value on both clusters eliminates off-diagonal divided-difference
terms in the derivative at zero. Thus

    dH_±(0)[eta]=P_±(eta.G)P_±/sqrt(3),
    ||dH_±(0)[eta]||=|eta|/3.

The two compressions are checked exactly. Analyticity and Hermiticity on
the real slice imply

    ||Im H_±(k+i eta)|| <= |eta|(1/3+C|k|+C|eta|).

For any matrix H, differentiating ||exp(-itH)u||^2 and integrating the
resulting differential inequality gives
||exp(-iNH)|| <= exp(N lambda_max(Im H)). This supplies the complex
growth estimate without assuming normality away from the real slice.

Here is a direct replacement for the candidate's compressed almost-analytic
Stokes step. For an integer m form

    zeta_m(k,t)=sum_{l=0}^m (it)^l/l! (v.grad)^l zeta(k).

It has the same compact real support, and
(partial_t-i v.grad)zeta_m=O(t^m). Differentiate the shifted integral
of exp(i(k+itv).z)U(k+itv)^N zeta_m(k,t), and integrate its real-direction
derivative by parts. For v.z>=11N/16, choose kappa,tau small so that
1/3+2Ckappa+Ctau<11/16. The endpoint is exponentially small and the
error is bounded by C_m integral_0^tau t^m exp(-cNt)dt=O(N^(-m-1)).
No boundary term occurs because the cutoff has compact real support.

Thus the cut-off kernel is O(N^-infinity) uniformly on all required
Alice--Bob differences. Since ||f_N||_1=O(N^(3/2)) and Bob has O(N^3)
sites, convolution and restriction preserve arbitrary inverse powers.
Writing a^<=U^N zeta(D)f_N and a^>=U^N(1-zeta(D))f_N yields

    L_N=Q_N+2 Re J_N+O(N^-infinity),
    Q_N=<a^>,E_N a^>>,  J_N=<E_N r_N,a^>>.

## 3. Fourier boundary expansion and lattice aliases: Lemma B

For a smooth vector amplitude inside |w|<=rho, vanishing with its first
normal derivative at the sphere, let c(theta) be its second outward
radial derivative. Rotate the Fourier direction to a coordinate axis
and integrate over transverse disks. The resulting marginal m(t) is
smooth on [-rho,rho] from each side and has endpoint expansions

    m(rho-epsilon) = pi rho c(theta) epsilon^3/3+O(epsilon^4),
    m(-rho+epsilon)= pi rho c(-theta)epsilon^3/3+O(epsilon^4).

Four integrations by parts extract the endpoint third derivatives; a
fifth controls the remainder. Uniform bounds on the interior amplitude's
derivatives give the uniform angular expansion

    g_tilde(xi)=2pi rho |xi|^-4 [c(xihat)e^(-i rho|xi|)
                 +c(-xihat)e^(i rho|xi|)] + O(|xi|^-5).

One can obtain endpoint smoothness by transverse angular averaging: odd
transverse Taylor terms vanish and even terms are smooth in the squared
transverse radius. This also supplies bounds uniform in direction and
for a bounded family of smooth interior amplitudes.

An independent exact check uses g(w)=(1-|w|^2)^2 on the unit ball.
Both radial integration and cross-section integration give

    g_tilde(t)=32pi[(15-6t^2)sin t+(t^3-15t)cos t]/t^7,

with leading term 32pi cos(t)/t^4. Both formulations are checked exactly.

For rho=1/32 the encoder's second normal derivative is
4pi Phi_0(rho)/rho^2 times i M chi; the cosine part vanishes to order four
and can be absorbed in the stated remainder. For the detector times
reference the derivative is 8 Psi_N(beta+rho theta)/rho^2.
The primitive-cell factors from the previous protocol report then give

    fhat_N(k)= i C_f N^(-5/2) sum_{G,sigma} |k+G|^-4
          exp(-iN sigma rho|k+G|)M chi + O(N^(-7/2)),
    C_f=256pi^2 Phi_0(rho)/sqrt(V),
    C_h=512pi/sqrt(V),

with the corresponding translated formula for (E_N r_N)^hat. These are
precisely the candidate's coefficients. The errors are uniform away from
the reciprocal lattice. For the reference, the exact representation

    Psi_N(w)=c_r integral_{|q|<=1} g(q)exp(iq.w)U(q/N)^N chi dq

has all spatial derivatives uniformly bounded, since U(q/N)^N is unitary
and |q|<=1. On compact w sets this family is precompact in every fixed
finite differentiability norm.

Poisson summation has measure factor N^3/V and translation phase
exp(-i(k+G).b_N). The |k+G|^-4 leading aliases and |k+G|^-5 errors are
absolutely summable in dimension three, uniformly on the cutoff complement.
Absolute Fourier convergence justifies this use of Poisson for the
compact, continuously differentiable profiles. The translation phases
have modulus one for every N, even when b_N is not a lattice point.
In particular ||a^>||=O(N^(-5/2)).

## 4. Interference: filling Lemma C

Inserting those expansions into J_N leaves an O(N^-6) error and N^-5
times oscillatory integrals with phases

    Phi(k)=beta.k+tau rho|k+G'|-sigma rho|k+G|-omega_j(k).

Reciprocal-translation constants can depend on N, but have unit modulus
and factor out of each integral. On compact simple-band charts, the
amplitudes form a precompact subset of L1 by the bounds on Psi_N.

The nonconstant-phase assertion needs proof, not just the assertion that
stationary points are isolated. Suppose Phi were constant on an open set.
Then exp(-i Omega(k)), with Omega=constant+beta.k plus the two radial
terms, would solve the characteristic polynomial there. That determinant
identity is real analytic on R^3 minus at most two points, a connected
domain, so it extends along it. Restrict to k=3s n on a simple-band interval
avoiding those points. Omega'(s) is algebraic over C(s) and lies in

    [-9/4-3/16, -9/4+3/16].

It cannot equal the flat-branch slope 1. If it equals -1±alpha', then
alpha' is algebraic in s. But

    (alpha')^2=4(1-cos 4s)/(3-cos 4s)

would make cos(4s) algebraic over C(s), which is impossible. To see this
directly, clear denominators in a putative polynomial identity in cos(4s)
and continue to s=it: its highest nonzero power grows exponentially faster
than all lower powers with polynomial coefficients. It cannot cancel.
Hence no such constant phase exists. An analytic nonconstant phase has
nonzero gradient almost everywhere: a nontrivial analytic derivative has
a zero set of measure zero.

On sets where one partial derivative is nonzero, use Phi as a local
coordinate and apply the ordinary L1 Fourier decay statement to its
pushforward density. The leftover set has arbitrarily small L1 mass.
This proves decay for each fixed amplitude. A finite epsilon-net gives
uniform decay over a precompact family of L1 amplitudes.

Finally truncate the absolutely convergent reciprocal sums and exclude
arbitrarily small neighbourhoods of the band-degeneracy set (whose
discriminant is nontrivial by section 1). Eigenprojectors have norm one,
so the uniform amplitude bound controls the removed volume. On the
remaining finite charts apply the preceding argument; then restore the
neighbourhoods and reciprocal tails by dominated convergence. This proves

    J_N=o(N^-5).

No nondegenerate Hessian or N^-13/2 rate is needed or claimed.

## 5. Positive localisation and transport: filling Lemma D

Choose smooth gamma with 0<=gamma<=h_0, positive near zero, and
gamma_N(x)=gamma(x/N-beta). Choose a simple-band patch away from the
cutoff and theta=sin^2(vartheta), where 0<=vartheta<=pi/2 is smooth and
compactly supported in that patch. Set Theta=theta(D)P_j(D) and
B=sqrt(Theta(1-Theta))=(sin vartheta cos vartheta)(D)P_j(D).
Both symbols extend smoothly by zero. Their lattice kernels have finite
absolute first moments. Because gamma_N has Lipschitz constant O(1/N),
the commutator kernels obey

    ||[Theta,gamma_N]||+||[B,gamma_N]||=O(1/N)

by summing |z| times the multiplier kernel. This is a direct Schur/Young
bound, uniform in the translate b_N. The exact identity

    Theta^2+(I-Theta)^2+2B^2=I

then gives

    gamma_N = Theta gamma_N Theta
           +(I-Theta)gamma_N(I-Theta)+2B gamma_N B+O_op(1/N).

All three quadratic forms on the right are nonnegative. Consequently

    Q_N >= <Theta a^>,gamma_N Theta a^>> - O(N^-1)||a^>||^2
         = <Theta a^>,gamma_N Theta a^>> - O(N^-6).

This is the needed approximate positive localisation; it is not obtained
by discarding interference between bands pointwise.

For a finite number of source aliases write the localised Fourier state
as N^(-5/2) sum_l A_l(k)exp(-iN H_l(k)) plus its smaller remainder, with

    H_l=omega_j+sigma rho|k+G|,
    A_l=i C_f theta P_j M chi |k+G|^-4.

To evaluate its gamma_N quadratic form, insert the Fourier kernel of
gamma_N and put k'=k-p/N. For equal aliases, the phase difference tends
to p.grad H_l and the translation contributes exp(-ip.beta). The inverse
Fourier integral in p is therefore gamma(grad H_l-beta). All measure
factors cancel: (N^3/V) from Poisson times V/((2pi)^3N^3) gives the
ordinary (2pi)^-3 inverse-transform factor.

This limit is controlled, rather than formal: first restrict p to a fixed
compact set and Taylor-expand the smooth phase and amplitude; the error
then tends uniformly to zero. The Fourier transform of gamma is rapidly
decaying and integrable, which controls the complementary p tail.
Nonzero lattice aliases in gamma's transform are rapidly small because
the momentum patch has diameter smaller than the nearest reciprocal
separation. For different source aliases the remaining phase is
rho(sigma|k+G|-tau|k+G'|). Its gradient cannot vanish identically on an
open set unless (G,sigma)=(G',tau); otherwise it would equate two different
unit radial fields on an open three-dimensional region. The same
oscillatory-integral argument as above eliminates these cross terms.

Restore infinitely many source aliases after this argument: their
uniform L2 tails are bounded by C sum_{|G|>R}|G|^-4, and multiplication
by gamma_N is bounded. Thus the tails can be made uniformly small before
taking N to infinity. It follows that

    lim N^5<Theta a^>,gamma_N Theta a^>>
      = C_f^2 sum_{G,sigma} integral theta^2 ||P_j M chi||^2 |k+G|^-8
          gamma(grad omega_j+sigma rho (k+G)/|k+G|-beta) dmu(k).

The source remainder and localisation error contribute O(N^-6) before
scaling and hence vanish in this limit.

For strict positivity take the branch -s+alpha at the verified point
sin(2s_1)=-43/sqrt(2247), s_1 in (-pi/4,0), and k_1=3s_1 n.
This point is inside the chosen primitive momentum cell, is simple,
and has k_1/|k_1|=v and velocity 25v/32. Choose G=0 and sigma=-1:

    grad omega_j(k_1)-rho v-beta=(25/32-1/32-3/4)v=0.

The overlap was proved nonzero in section 1. Choose theta positive at
k_1 and gamma positive near zero. Continuity then makes this integrand
strictly positive on an open three-dimensional patch, not just on the
axis. Its integral is positive. Therefore

    liminf N^5 Q_N >= c_*>0,   Q_N=O(N^-5).

## 6. Consequence and interpretation

Combining sections 2--5 gives L_N=Q_N+o(N^-5), and hence eventual positivity
and the two-sided N^-5 bounds. Every estimate is for all sufficiently
large integer N. No averaging over times or restriction to N divisible
by 16 was used: translated Riemann sums and Poisson phases keep the
actual b_N, and the positive smooth spatial detector averages the
microlocal cross terms. The exact small-N zeros remain valid and do not
contradict an unknown large-N threshold.

The declared definition of admissibility was checked directly against
`papers/ir-corona/ir-corona.tex` section 3: the protocol report uses the
same three relative ratios and nonzero-denominator requirement, with
the actual lattice measure. Fable lacked that manuscript as an attachment;
that input limitation does not by itself refute the protocol's derivation.
The earlier analytic admissibility proof remains PRELIMINARY and has
not been independently reviewed in a sealed round.

For the actual physical interpretation, the low fixed-neighbourhood
component a^< is superpolynomially small at Bob, whereas the fixed
nonzero-momentum component has a positive order-N^-5 quadratic response.
Thus Fable's warning is supported by this local derivation: an
IR-admissible operation may produce leakage which dominates this signal.
It does not establish exclusively IR-carried signalling or violate the
local Weyl approximation. The finite-range rule and its local cone are
the same throughout; the faster modes belong to its full spectrum.

## 7. Validation and what remains outside this audit

Reproduction: `python3 -B scripts/verify_tetrahedral_fable_audit.py`.
55/55 exact checks; no floating-point tests or additional evolution samples.
Verifier SHA256:
`6c9e29af3a53ad8d6eae42fdf445d6289a40715f8239c91dcb5c587b0322ac41`.
Stdout SHA256:
`f99be8fe18b9754bcd4963e2e31c1ca7169ac8d441ee62bcf59c7d7ad1a37aa7`.
Analytic sections 2--5 are written arguments, not machine certificates.
The contour, norm, Poisson and transport steps have been expanded here
instead of citing the model-generated candidate as an external theorem.
`git diff --check` passed. No fresh provider calls or changes to reviewed
verifiers; no scientific promotion or push.

Outstanding: independent scrutiny of this expanded local proof, an
effective N_0, quantitative remainder estimates, the exact limit coefficient
and any stronger interpretation of IR spectral origin. The candidate's
conditional full coefficient formula and the heuristic N^-13/2 interference
order have not been promoted by this audit. No claim about other walks,
other polyhedra, all protocols or substantive novelty follows.
