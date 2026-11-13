# General infrared admissibility: Stage A denominator audit

2026-11-13. Author: Codex (OpenAI). Branch:
`research/tetrahedral-support-rigidity-2026-11-09`.
Preregistration: `ecc5827a6aa1838f668326386d568a790417150d`,
`theory/GENERAL_IR_ADMISSIBILITY_GATE.md`. User authorized Stage A only.
Evidence: analytic author derivation, **PRELIMINARY; not independently
reviewed**. No numerical or symbolic computation, no verifier run.

## 1. Scope and outcome

The frozen family permits a Hermitian basis containing a non-zero M
with `M chi = 0`. For that member `Delta_M = 0` for every N and
`eta_enc(M)` is undefined. Thus the whole unrestricted family cannot
be asserted to satisfy Definition 3.1, which requires `Delta_M != 0`.
This is a denominator obstruction, **not** a counterexample to convergence
of a defined ratio, and **not** a counterexample to existence of an
admissible pair attaining the B1 rate.

Per-target records:

- Leakage numerator estimate: `PROVED_UNDER_FROZEN_CONTRACT` (author).
- Operator denominators for non-zero M and non-zero detector projectors:
  `PROVED_UNDER_FROZEN_CONTRACT` for all sufficiently large N (author).
- State denominator for every member of an arbitrary Hermitian basis:
  undefined in an allowed case, as proved below. No convergence verdict
  is assigned to that ratio.
- Overall: `OPEN_AFTER_ADMISSIBILITY_ANALYSIS`; stopped at the charter's
  class-change rule, not at budget exhaustion. A revised treatment of
  null encoders needs a user decision before continuing. No amendment
  has been applied, and Stage B has not been executed.

The following arguments concern the inherited positive-radius balls
and fixed finite matrix families on `Z^d`, `d in {2,3}`. All constants
may depend on that fixed data; none depend on N. No walk hypothesis is
used in these estimates. The nodal condition only locates chi in the
declared resource space.

## 2. Numerators: arbitrary internal dimension

On the torus represented by `[-pi,pi]^d`, define
`D_j f(x) = f(x+e_j)-f(x)`. For `|p| >= N^(-1/2)`,

    sum_j |exp(i p_j)-1|^2 >= (4/pi^2)|p|^2 >= (4/pi^2)/N.

For a matrix multiplier a with `sup ||a|| <= A` and
`sup ||D_j a|| <= L/N`, the product rule and Plancherel therefore give

    ||(I-Pi') a Pi|| <= (pi/2)(A + sqrt(d)L) N^(-1/2).

Indeed `||(D_j Pi f)_j|| <= N^(-1)||f||`; applying the product rule
gives the upper bound `(A+sqrt(d)L)N^(-1)||f||` for the discrete gradient
of `a Pi f`. The displayed high-momentum lower bound then yields the
claim. These are operator norms and vector-valued Plancherel identities;
the proof does not depend on matrix size.

For the fixed profiles F and h, put `L_F = Lip(F)`, `L_h = Lip(h)`
in continuum coordinates. They are finite, including at their spherical
boundaries. For `a_M = U_M-I`, spectral calculus for a fixed Hermitian M
gives

    A <= 2,  L <= (pi/2)||M|| L_F.

For `E = h_N tensor P`, with P a non-zero orthogonal projector,
`A <= 1`, `L <= L_h`. Thus both leakage numerators are `O(N^(-1/2))`.

For the state numerator, let `v=U_M phi_N`, `w=Pi'v`, `r=v-w`.
Since `Pi'phi_N=phi_N`,

    Delta_M-Pi'Delta_M Pi' = |r><v| + |w><r|,
    ||Delta_M-Pi'Delta_M Pi'||_1 <= 2||r|| = O(N^(-1/2)).

The rank-one identity uses `v=w+r` and is valid even when Delta is zero.
It supplies no lower bound for its denominator.

## 3. Operator denominators

For sufficiently large N the momentum ball lies inside the chosen
torus cell. With normalized measure `dp/(2pi)^d`, write the exact
normalized scalar resource as

    phi_N(x) = N^(-d/2) Phi(x/N) chi,
    Phi(w) = c_d integral g(q) exp(-i q.w) dq,

where `c_d > 0` is fixed by normalization. The scalar Phi is continuous
and `Phi(0)>0`: `g >= 0` is integrable, supported on the unit ball and
not zero. Hence `|Phi|` has a positive lower bound on a neighbourhood
of zero. A fixed open box in continuum coordinates contains at least
`c N^d` points of `N^(-1)Z^d` for all sufficiently large N, by counting
each coordinate interval.

For a non-zero Hermitian M choose a unit eigenvector v of eigenvalue
`lambda != 0`. Inside Alice's ball the scalar F takes all values in
`(0,1)`. Choose an interior point w_0 where
`exp(i pi lambda F(w_0)/2) != 1`; such points exist because a nonconstant
interval of phases cannot all lie in `2 pi Z`. By continuity there is
an open box around w_0 on which this modulus is at least epsilon > 0.

Test `a_M Pi` on the normalized band-limited scalar resource translated
by a lattice point z_N nearest to `N w_0`, with internal vector v.
Translation preserves its band support. Shrink the box so that
`Phi(x/N-z_N/N)` is bounded below there for all large N. Site counting
then gives a resource mass at least m > 0 on that box, and

    ||a_M Pi|| >= epsilon sqrt(m) > 0.

For a non-zero detector projector choose a unit v in its range, a box
inside Bob's ball where h >= epsilon, and the same translated-resource
test. It gives `||E Pi|| >= epsilon sqrt(m) > 0`.

Consequently both operator leakage ratios are `O(N^(-1/2))` for these
non-zero matrices. A Hermitian basis has no zero member. If a declared
spanning projector set includes the zero projector, that member has an
undefined ratio and must also be recorded, not silently discarded.
Only eventual non-vanishing is proved here; no assertion for all small N.

## 4. Exact state-denominator obstruction; stop

Take an internal orthonormal pair `(chi,v)`. It exists since `s >= 2`.
The non-zero Hermitian matrix

    M = |v><v|

satisfies `M chi = 0`. It can be a member of a real Hermitian basis:
any non-zero vector of the finite-dimensional real space of Hermitian
matrices extends to a basis. For every site and every N, the power
series of the exponential gives

    exp(i pi F_N(x) M/2) chi = chi.

Since the resource at each site is a scalar multiple of chi,
`U_M phi_N = phi_N` exactly. Thus `Delta_M = 0` and its trace norm is
zero. This construction changes only the basis permitted by the
protocol definition, not the walk, regions or spectral hypotheses.
It is not a construction or search for a new walk.

Independent formulation of the same check: in coordinates
`chi=(1,0)` and `v=(0,1)`, take

    M = diag(0,1),
    U_M(x) = diag(1, exp(i pi F_N(x)/2)).

The first component of the resource is unchanged. In this `s=2` case,
`{I, sigma_x, sigma_y, diag(0,1)}` is a real Hermitian basis since
`sigma_z = I-2 diag(0,1)`. This supplies an explicit basis, not merely
the basis-extension argument. For larger s, the same null action is
checked on chi in the displayed rank-one construction.

The manuscript's four Pauli generators instead obey `M^2=I`, so none
annihilates a unit chi. The numerator calculation above reduces to its
`d=3`, `||M||=1` estimate. Its special state-denominator argument does
not address the allowed projector generator just exhibited.

This triggers the frozen stop rule. No general lower bound on the
state denominator for the remaining non-null generators is claimed in
this execution, and no altered family is used to finish the theorem.

## 5. Decision required before further execution

A candidate continuation would distinguish null encoders `M chi=0`
(which encode no bit on this resource) from active encoders, then prove
the state-denominator bound for active encoders and check that B1's
non-vanishing pair can be chosen among them. This is a proposed change
of statement, not an amendment in force or an admissibility proof.

There is a useful documentary compatibility check, without completing
that argument: B1's recorded leading coefficient contains
`f_0^dagger M chi`
(`reports/2026-11-12--general-ir-rate-stage2-leading-term.md`, Sec. 5,
and its bilinearity conclusion in Sec. 7). It vanishes for the null
generators above. That observation does not independently verify B1,
its existence argument, or admissibility of the remaining pairs.

No evidence here requires dropping the word admissible from every
possible B1 existence statement. The unsupported assertion is that
every member of its unrestricted Hermitian family has defined ratios
and is admissible. No claim about Bravais lattices, carrier Stage B,
interactions or novelty follows.

## 6. Timing and provenance

Execution began at `2026-11-13T10:44:41Z`, after the charter commit.
Execution ended at `2026-11-13T10:45:47Z` (66 seconds of wall time,
including writing the analytic record). The final documentary status
update and Git checks follow this endpoint; no further derivation.
The terminal outcome is the structural denominator obstruction, reached
within the 90-minute Stage A cap. This report is a written derivation;
it does not rely on an ephemeral computational script or external model.
