# General infrared admissibility: active encoders on Z^d

2026-11-13. Author: Codex (OpenAI). Branch:
`research/tetrahedral-support-rigidity-2026-11-09`.
Charter `ecc5827a6aa1838f668326386d568a790417150d`; Amendment 1
preregistered at `156657e8a12282e39df9429095c6f58303d25d8a` before this
continuation. User «aprobado» authorizes the active/null treatment and
Stage A continuation only. Analytic derivation, no computational script,
no external transmission. **PRELIMINARY; not independently reviewed.**

**Exposition update, 2026-11-13:** Claude's optional O1–O4, O6 and O8
comments are applied at the user's instruction «aplicalas». The reviewed
version is preserved at `bb3592b` and in the sealed review input. The
[review](reviews/2026-11-13-admissibility-opus/informe_opus.md) gave PASS;
these edits have not been re-reviewed. Execution timing and the original
evidence label above are historical.

## 1. Statement and quantifiers

Fix `d in {2,3}`, finite `s >= 2`, positive-radius continuum balls A and B,
their frozen profiles F and h, a unit internal vector chi, and a fixed
finite Hermitian basis and fixed finite set of orthogonal detector
projectors. All these data are independent of N. Use precisely the
resource, projections and leakage ratios of the admissibility charter.

For every active basis member `M chi != 0` and every non-zero detector
projector P, all three required ratios are defined for sufficiently
large N and are `O(N^(-1/2))`. Constants depend on the fixed data and
can be chosen uniformly over their finite active/non-zero families;
no uniformity as the basis, chi, balls or lattice vary is claimed.

Null members `M chi = 0` have `Delta_M = 0` and zero signal exactly.
Their state ratio remains undefined, as required by Amendment 1.
For a non-zero null basis member, `eta_op(U_M-I)` is nevertheless
defined eventually and is `O(N^(-1/2))`: its operator denominator tests
all input-band vectors, not only the declared resource. Only its state
ratio `eta_enc(M)` is undefined.
Zero detector projectors, if present, likewise have zero signal and
an undefined operator ratio.

The lemma uses no tilted spectral hypothesis H1–H10 and no walk
dynamics. Those hypotheses enter only the conditional compatibility
with B1 in Sec. 5. No Bravais transfer is claimed here.

## 2. Resource mass on arbitrary open boxes

For sufficiently large N the support of `g(Np)` is contained in
`[-pi,pi]^d`. Put

    J_2 = integral g(q)^2 dq > 0,
    c_d = (2 pi)^(-d/2) J_2^(-1/2),
    Phi(w) = c_d integral g(q) exp(-i q.w) dq.

With Fourier measure `dp/(2pi)^d`, direct substitution in the normalized
resource gives exactly

    phi_N(x) = N^(-d/2) Phi(x/N) chi,
    w_x := ||phi_N(x)||^2 = N^(-d) |Phi(x/N)|^2,
    sum_x w_x = 1.

The compactly supported integrable g has an entire Fourier transform:
expand the exponential on any bounded complex set and integrate its
uniformly absolutely convergent power series. Thus Phi is real analytic
on `R^d`, and `Phi(0)=c_d integral g > 0`. Its zero set cannot contain a
non-empty real open set: vanishing on a ball annihilates every Taylor
coefficient there, and overlapping Taylor neighbourhoods along a path
would imply vanishing at zero. This contradicts `Phi(0)>0`.

Consequently any non-empty open set contains a point where Phi is
non-zero, and a smaller closed axis-aligned box Q of positive side
lengths on which `|Phi| >= b_Q > 0`. If the side lengths are l_j, then
for all sufficiently large N each coordinate interval of NQ contains
at least `N l_j/2` integers. Therefore

    sum_{x/N in Q} w_x >= b_Q^2 product_j(l_j/2) =: m_Q > 0.

This local mass bound avoids any assumption that A is near the origin,
and does not require a global Riemann-sum error estimate.

## 3. Positive lower bound for the active state denominator

Write the spectral resolution of the fixed Hermitian matrix as
`M = sum_lambda lambda P_lambda` and let
`p_lambda = ||P_lambda chi||^2`. These non-negative weights sum to one.
Activity is equivalent to `p_lambda > 0` for at least one `lambda != 0`.
At continuum position w set

    theta(w) = pi F(w)/2,
    t(w) = <chi, exp(i theta(w) M) chi>
         = sum_lambda p_lambda exp(i theta(w) lambda).

In particular `|t(w)| <= 1`, and outside A, `t(w)=1`.
Choose an eigenvalue `lambda_* != 0` with `p_lambda_* > 0`.
Inside a ball of positive radius, F takes every value in `(0,1)`.
Choose a value f in that interval such that
`(pi/2) f lambda_*` is not an integer multiple of `2 pi`.
Such a value exists since the exceptional values form a discrete set.
At a point attaining f,

    1-Re t(w) = sum_lambda p_lambda (1-cos(theta(w)lambda)) > 0.

By continuity this remains at least epsilon > 0 on a non-empty open
neighbourhood strictly inside A. By Sec. 2 select a box Q_in in that
neighbourhood carrying mass at least `m_in > 0` for all large N.
Also choose a box Q_out strictly outside A carrying mass at least
`m_out > 0`. Such an exterior box exists by the same analytic argument,
and `t=1` there. No lower bound on the resource at an entire sphere
or at a prescribed facing point is needed.

The overlap of the normalized encoded and unencoded states is

    z_N = <phi_N,U_M phi_N> = sum_x w_x t(x/N).

Absolute convergence follows from `sum w_x=1` and `|t|<=1`. Hence

    1-|z_N|^2
      = sum_{x,y} w_x w_y (1-Re[t(x/N) conjugate(t(y/N))]).

Every summand is non-negative. For one point in Q_in and one in Q_out,
the bracket is at least epsilon. Counting both orders gives

    1-|z_N|^2 >= 2 epsilon m_in m_out > 0,
    ||Delta_M||_1 = 2 sqrt(1-|z_N|^2)
                 >= 2 sqrt(2 epsilon m_in m_out) =: D_M > 0.

The pure-state trace-norm identity follows by restricting the difference
of the two rank-one projections to the span of their unit vectors:
its eigenvalues are `+sqrt(1-|z_N|^2)` and its negative (with zeros on
the orthogonal complement). This also checks that a spatially varying
scalar phase is not mistakenly treated as a global unobservable phase.

The bound proves eventual non-vanishing. It need not hold for all small
N; the admissibility definition only requires its asymptotic domain.

## 4. Completion of the three leakage estimates and cross-checks

The discrete product-rule proof in the first Stage A report, Sec. 2,
gives, for a matrix multiplier a with bounds A and L,

    ||(I-Pi')a Pi|| <= (pi/2)(A+sqrt(d)L) N^(-1/2).

It applies to `a=U_M-I` with `A=2`,
`L=(pi/2)||M|| Lip(F)`, and to `a=h_N tensor P` with `A=1`,
`L=Lip(h)`. The proof only uses the elementary torus inequality
`sum |exp(i p_j)-1|^2 >= 4|p|^2/pi^2`, the input-band bound
`|p|<=N^(-1)`, and the discrete product rule. Matrix size is irrelevant.
Write the resulting numerator constants as C_M and C_P.

For completeness, the operator denominators use test states that may
differ from the declared resource: an operator norm is a supremum over
all normalized input-band vectors. For non-zero M take an eigenvector
with non-zero eigenvalue and an interior box where
`|exp(i theta(w)lambda)-1| >= e > 0`. A scalar resource translated to
a nearest lattice point to the centre of that box has fixed positive
mass on a smaller box, since `Phi(0)>0`. Thus
`||(U_M-I)Pi|| >= e sqrt(m)`. For non-zero P use an internal vector in
its range and a box inside B where h is positive, obtaining the same
form of bound for `||E Pi||`. Translation preserves momentum support.
These are the first report's Sec. 3 arguments, and require no assumption
on M's action on the declared chi.

Explicitly, `Pi phi_N=Pi'phi_N=phi_N` implies

    r=(I-Pi')U_M phi_N=(I-Pi')(U_M-I)Pi phi_N,
    ||r|| <= C_M N^(-1/2).

Finally, the rank-one decomposition of the state numerator gives
`||Delta_M-Pi'Delta_M Pi'||_1 <= 2 C_M N^(-1/2)`.
Dividing by the positive bounds above proves

    eta_op(U_M-I) <= C'_M N^(-1/2),
    eta_enc(M) <= (2 C_M/D_M) N^(-1/2),
    eta_op(E) <= C'_P N^(-1/2).

Two checks of the boundary between active and null cases:

- If `M chi=0`, the exponential power series fixes chi at every site,
  independently of the overlap calculation: Delta and every signal
  vanish exactly. The positive spectral weight used in Sec. 3 is then
  absent, so no positive bound is asserted.
- If `M chi=lambda chi` with real `lambda != 0`, then
  `t(w)=exp(i lambda theta(w))`. Comparing an interior box with the
  unmodified exterior proves a positive state denominator even though
  M acts as a scalar on chi. For the manuscript Pauli matrices,
  the spectral expression instead reads
  `t=cos(theta)+i <chi,M chi> sin(theta)`; hence `Re t=cos(theta)`.
  With its choice `F>=1/2` and `F<=1`, epsilon can be
  `1-1/sqrt(2)`. The displayed bound becomes
  `1-|z_N|^2 >= (2-sqrt(2))m_in m_out`, recovering its denominator
  argument when the two mass bounds are the same m. This last comparison
  is a consistency check using the manuscript's stated profile choice;
  the general proof above does not depend on that comparison.

No uniform positive lower bound as `M chi -> 0` is claimed.

## 5. Compatibility with the existing B1 existence argument

This step is conditional on the B1 leading-term and non-vanishing
derivation already recorded in
`reports/2026-11-12--general-ir-rate-stage2-leading-term.md`, Secs. 5–7,
under the hypotheses as subsequently amended. It is not a re-review
of those asymptotics or of Amendments 5–6.

The inherited dependencies are explicit:

1. B1 asserts existence of a fixed basis pair for the physical signal
   with `limsup e^(K_* N) N^(5+d/2) delta(N) > 0`.
2. Its passage from the leading functional to that physical signal uses
   the per-pair expansion `L_N=-2 Im Z_1 + lower-order terms`.
3. Existence of the leading-functional witness uses B1's spectral,
   arithmetic and non-vanishing hypotheses as amended; that argument
   is not reproved by the admissibility lemma.
4. The analogous conclusion on a Bravais lattice requires the existing
   Bravais transfer of these statements, not established in this report.

Given dependency 1, any such pair must have `M chi != 0` and `M_B != 0`:
otherwise its physical signal is exactly zero for every N, contradicting
the positive **scaled** limsup. Secs. 2–4 therefore make that pair
admissible, with its actual nonlinear exponential encoder. No selection
algorithm or explicit pair is claimed. The signal itself is not
bilinear; B1 uses bilinearity only for its leading functional, before
passing to a basis pair through dependencies 2–3. No signed linear
combination is realized as a physical detector.

Accordingly the admissibility gap for B1's existence claim on `Z^d`
is closed at the level of this conditional author derivation. The
assertion that every member has defined ratios fails for some permitted
Hermitian bases, namely those containing a member annihilating chi.
It does not fail for bases consisting entirely of active members.
No statement about the open B2 cell,
Bravais lattices, interacting QCA or novelty follows.

## 6. Verdict and provenance

Active-family admissibility on `Z^d`:
`PROVED_UNDER_FROZEN_CONTRACT` as amended by Amendment 1.
Compatibility with B1: **conditional implication proved**, with the
inherited dependencies enumerated in Sec. 5; no unconditional B1 rate
proof is claimed here. The original author evidence was PRELIMINARY;
the original version subsequently received one cross-family Claude PASS.
These exposition edits have not been re-reviewed. No promotion.

The local literature index was checked before continuation; no external
theorem or bibliographic novelty claim is used. No retained computational
result was generated and no script or reviewed verifier was modified.
Execution began `2026-11-13T11:11:50Z`, after the amendment commit.
Execution completed `2026-11-13T11:13:08Z` (78 seconds wall time,
including writing the derivation), within the 90-minute cap. Subsequent
documentary status updates and Git checks do not extend the derivation.
