# General infrared admissibility: Stage B on a fixed Bravais lattice

2026-11-13. Author: Codex (OpenAI). Branch:
`research/tetrahedral-support-rigidity-2026-11-09`.
Contract: `GENERAL_IR_ADMISSIBILITY_GATE.md` (`ecc5827`), Amendment 1
(`156657e`). Stage B authorized by user «adelante con ella», recorded
before execution at `20bc5b15ece6e8561b0cd0f87aad69336a3295f7`.
Base active-case proof: `reports/2026-11-13--general-ir-admissibility-active-encoders.md`
(`bb3592b`). **Author analytic derivation; PRELIMINARY; no independent
review, no promotion.** No computations or external transmissions.

**Exposition update, 2026-11-13:** optional O1, O2, O5 and O8 from the
[Claude review](reviews/2026-11-13-admissibility-opus/informe_opus.md)
are applied at the user's instruction «aplicalas». The original PASS
version is preserved at `6ddda97` and in the sealed review input. These
edits have not been re-reviewed; the original evidence and timing labels
describe the execution before review.

## 1. Question, scope and conclusion

Known: Stage A proves three `O(N^(-1/2))` leakage ratios on `Z^d` for
each fixed active encoder `M chi != 0` and non-zero detector projector.
Question: does the same statement hold on every fixed full-rank Bravais
lattice, with physical Euclidean balls and momentum cutoffs unchanged?
Stop: any required new hypothesis or loss of a denominator lower bound.

Fix `L=B Z^d`, real invertible B, `d in {2,3}`, and all of the finite
internal, profile and resource data of Stage A. Write
`v_L=|det B|`, `b_j=B e_j`, `beta=sigma_min(B)>0`,
`B_op=||B||_2`, `B_F=(sum_j |b_j|^2)^(1/2)`.
Here B denotes only the lattice matrix. Bob's physical ball is denoted
`B_reg` below; its radius is the charter's Bob radius. The reciprocal
cell's inscribed-ball radius is denoted `r_rec`, a different quantity.
All constants and thresholds may depend on this fixed lattice and data.
No uniformity over degenerating lattices or changing bases is asserted.

**Conclusion:** Stage A transfers. All three ratios for active encoders
and non-zero detectors are defined eventually and are `O(N^(-1/2))`.
No new hypothesis beyond fixed full rank is required. Null encoders and
zero detectors retain their zero signals and undefined relevant ratios.
Compatibility with the Bravais version of B1 is conditional on its
existing rate/non-vanishing derivation. No new proof of that derivation
or of the carrier dichotomy is supplied here.

## 2. Fourier conventions and small momentum balls

Dual lattice `L*=B^(-T) Z^d`; reciprocal torus
`T_L=R^d/(2 pi L*)`. Use normalized Haar measure

    dmu_L(p) = v_L dp/(2 pi)^d,
    f^(p) = sum_{x in L} exp(i p.x) f(x),
    f(x) = integral exp(-i p.x) f^(p) dmu_L(p).

This is an isometry: for `x=B n`, substitute `t=B^T p` and note
`dmu_L=dt/(2 pi)^d`, obtaining the standard orthogonality of the integer
characters. An explicit reciprocal fundamental cell is

    P_B = B^(-T)[-pi,pi)^d.

The Euclidean ball of radius `r_rec=pi/max_j |b_j|` lies inside its closure,
and every ball of strictly smaller radius lies in its interior: if
`|p|<r_rec`, then `|(B^T p)_j|<pi` for every j.
For sufficiently large N require `N^(-1/2)<r_rec`; both frozen cutoff
balls then lie inside this cell. The same small balls inject into the
reciprocal torus, irrespective of whether a parallelepiped or a Voronoi
cell is used to represent it. Pi and Pi' are multiplication by these
physical balls, with identity on the internal space. Changing the cell
for this proof does not change either projector.

## 3. Difference estimate with lattice constants

Define `D_j f(x)=f(x+b_j)-f(x)`. Its Fourier multiplier has squared
modulus `|exp(i t_j)-1|^2`, where `t=B^T p`. For the representative in
P_B, `|t_j|<=pi`, so

    G(p) := sum_j |exp(i t_j)-1|^2
          >= (4/pi^2)|B^T p|^2
          >= (4 beta^2/pi^2)|p|^2.

On the complement of Pi', `|p|>=N^(-1/2)`, because the cutoff ball is
entirely inside P_B. Plancherel gives

    ||(I-Pi') f|| <= pi sqrt(N)/(2 beta)
                         (sum_j ||D_j f||^2)^(1/2).

On the input band, `G(p)<=|B^T p|^2<=B_op^2/N^2`, hence

    (sum_j ||D_j Pi f||^2)^(1/2) <= B_op N^(-1)||f||.

Let a_N be a matrix multiplier with `sup||a_N||<=A_0` and physical
Lipschitz constant at most `ell/N`. Then
`||D_j a_N||<=ell |b_j|/N`. Applying the discrete product rule and
Minkowski in the direct sum over j yields

    (sum_j ||D_j(a_N Pi f)||^2)^(1/2)
        <= (A_0 B_op + ell B_F) N^(-1)||f||,

    ||(I-Pi') a_N Pi||
        <= pi/(2 beta) (A_0 B_op + ell B_F) N^(-1/2).

For `a_N=U_M-I`, take `A_0=2`,
`ell=(pi/2)||M|| Lip(F)`. For `a_N=h_N tensor P` with non-zero
orthogonal P, take `A_0=1`, `ell=Lip(h)`.
The profiles have the same physical Lipschitz constants as in Stage A;
their spherical supports have not become coordinate ellipsoids.

The state-numerator rank-one identity is independent of the lattice.
It still bounds that trace norm by twice the encoder leakage numerator,
because `Pi' phi_N=phi_N`. Thus every required numerator has the same
power `N^(-1/2)`.
Explicitly, `Pi phi_N=phi_N` also gives
`r=(I-Pi')(U_M-I)Pi phi_N`, so its norm is bounded by the encoder
leakage operator norm in Sec. 3.

## 4. Resource normalization and positive local masses

Keep the Stage A notation `J_2=integral g^2` and Phi. For large N,

    Z_{N,L} = integral |g(Np)|^2 dmu_L(p)
            = v_L (2 pi)^(-d) N^(-d) J_2.

Fourier inversion with this exact normalization gives

    phi_{N,L}(x) = sqrt(v_L) N^(-d/2) Phi(x/N) chi,
    w_{N,L}(x) = v_L N^(-d) |Phi(x/N)|^2,
    sum_{x in L} w_{N,L}(x)=1.

In particular, Phi is the same entire non-zero function of the physical
coordinate as in Stage A. Every non-empty physical open set contains
a smaller closed parallelotope `Q=B product_j [a_j,a_j+l_j]` of positive
side lengths in lattice coordinates on which `|Phi|>=b>0`: choose a
non-zero point of Phi, then shrink the coordinate box inside its
neighbourhood. Coordinate counting gives

    #(NQ intersect L) >= N^d product_j(l_j/2)

for sufficiently large N, and hence

    sum_{x/N in Q} w_{N,L}(x)
        >= v_L b^2 product_j(l_j/2)
         = b^2 vol(Q)/2^d > 0.

This explicitly balances the resource factor v_L against the lattice
point density. It is a lower bound, not an asymptotic counting formula.
No numerical approximation or lattice-plane arithmetic is involved.

## 5. All denominator bounds and compatibility

For an active fixed M, the Stage A spectral argument produces a physical
open subset strictly inside A on which

    1-Re <chi,exp(i pi F(w) M/2)chi> >= epsilon > 0.

Choose a parallelotope Q_in there and another Q_out strictly outside A,
both with positive mass by Sec. 4. The outside encoder equals identity.
With `z_N=<phi_{N,L},U_M phi_{N,L}>`, the same absolutely convergent
double sum of non-negative terms gives

    1-|z_N|^2 >= 2 epsilon m_in m_out,
    ||Delta_M||_1 >= 2 sqrt(2 epsilon m_in m_out)>0.

For the operator denominator, use the same translated band-limited
test as in Stage A. The needed lattice point z_N near any physical
centre Nw_0 exists with a bound independent of N: round every coordinate
of `B^(-1)Nw_0` to an integer, giving
`|z_N-Nw_0| <= (1/2)sum_j |b_j|`. Thus `z_N/N -> w_0`.
On a smaller parallelotope, `Phi(x/N-z_N/N)` has a positive lower bound
by `Phi(0)>0` and continuity. The count of Sec. 4 applies to the
translated resource too. A non-zero eigenvalue of M gives a region
where `|exp(i pi F lambda/2)-1|` is bounded below, so
`||(U_M-I)Pi||` is bounded below. A unit vector in the range of non-zero
P and an interior region in `B_reg` where h is positive give the lower bound for
`||E Pi||`. Lattice translation preserves both norm and band support.

Dividing Sec. 3's numerators by these bounds proves all three
`O(N^(-1/2))` ratios. Finite families give a common threshold and
finite common constants by taking their maxima/minima as appropriate.

The active/null distinction is internal and unchanged by the lattice:
`M chi=0` fixes the resource exactly, so Delta and every signal vanish.
Zero detectors also give zero signal. Conditional on the Bravais B1
conclusion that a fixed basis pair has positive scaled limsup
`limsup e^(K_* N) N^(5+d/2) delta(N) > 0`, any such pair is therefore
active and has a non-zero detector, and satisfies this lemma. This is
an existence implication, not an explicit selection of a pair. It
inherits the B1 existence, per-pair remainder, witness and Bravais
transfer dependencies enumerated in Stage A Sec. 5. Bilinearity belongs
to B1's leading functional; the physical exponential signal need not
be bilinear.
No use is made of H3 or H9 to prove admissibility itself; such
hypotheses remain relevant to B1's conditional rate claim.

## 6. Independent formulation and limiting checks

Pull back to integer coordinates `x=B n`, `t=B^T p`. The physical
cutoffs become `|B^(-T)t|<=N^(-1)` and `<=N^(-1/2)` in the ordinary
integer torus. On their outer complement,

    |t| >= beta N^(-1/2),

while on the input band `|t|<=B_op/N`. The standard integer-torus
gradient bound then reproduces Sec. 3's constants. This checks the
estimate by unitary change of coordinates without replacing the
physical Euclidean balls by spherical coordinate cutoffs.

For `B=I`, `v_L=1`, `beta=B_op=1`, `B_F=sqrt(d)`: the multiplier
bound and exact resource reduce to Stage A. For `B=a I`, `a>0`,
`beta=B_op=a`, `B_F=a sqrt(d)`, so the multiplier constant is again
`(pi/2)(A_0+ell sqrt(d))`; the required threshold depends on a.
The normalization becomes `sqrt(v_L)=a^(d/2)` and point density scales
as `a^(-d)`, consistent with the squared resource mass in Sec. 4.
Neither check implies a uniform theorem when B varies with N.

## 7. Verdict and record

**Stage B: `PROVED_UNDER_FROZEN_CONTRACT` as amended by Amendment 1.**
The transfer changes constants and excludes finitely many N; it supplies
the active-protocol admissibility lemma on each fixed full-rank Bravais
lattice. Compatibility with B1 is a **conditional implication**, not
an unconditional rate proof; the dependencies are listed in Sec. 5
and the amended exposition of Stage A Sec. 5. The original author result
was PRELIMINARY and subsequently received one cross-family Claude PASS;
these exposition edits have not been re-reviewed. No promotion.

No new hypothesis, new walk, carrier computation, numerical diagnostic
or modified reviewed verifier. The local literature index was checked;
no external source theorem is invoked and novelty remains OPEN.
Execution began `2026-11-13T11:14:50Z`, after the authorization commit;
execution completed `2026-11-13T11:15:56Z` (66 seconds wall time,
including writing the derivation), within the 60-minute cap. Subsequent
status and Git checks are documentary only.
