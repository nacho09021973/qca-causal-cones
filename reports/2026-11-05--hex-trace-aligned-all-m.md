# Aligned hexagons, all m >= 4: the vertex-slice route is closed

Date: 2026-11-05. Author: Claude Code (Claude Opus 5.5).
Contract: [`HEX_TRACE_ALIGNED_ALL_M_GATE.md`](../theory/HEX_TRACE_ALIGNED_ALL_M_GATE.md),
preregistration commit `689fd30`; execution authorized by the user
(«AÑADELO», recorded in CURRENT_STATE Sec. 16 at `302b616`).
Session: start 2026-11-05T13:01:50Z (first command), verifier final run
13:03:18Z, end 2026-11-05T13:04:19Z.
Timing note (repaired after review): the contract counts from the first
calculation, analytic included. The analytic route of Secs. 3–4 was worked
out by reasoning in the same session after the user's instruction and
before the first command; that start has no recorded timestamp. Compliance
with the 90-minute budget is therefore **[UNVERIFIED]**; only the
machine-recorded interval above is documented. No code was run before it.
**Outcome: `OPEN_AFTER_ALIGNED_ALL_M_ANALYSIS`.** Status: PRELIMINARY;
sealed OpenAI review (`gpt-6-astra`) REPAIR_REQUIRED on documentation only,
repairs applied (Sec. 7); bounded re-review by Grok `grok-4.7` PASS
(R1–R6 resolved); not promoted.

## 0. Pre-step check

Known: the m=3 certificate (CURRENT_STATE Sec. 16) uses four points on the
vertex-direction slice `p = 2q` only. Question: does that slice route, or
another argument, give scalar incompatibility for every m >= 4?
Abandonment: the contract's first named route is the slice; if it cannot
work for all m, record why and stop at OPEN.

## 1. Result in one paragraph

For every m >= 629 there is a D6-invariant real residual `h` supported in
`H_(m-2)` such that `f = f_m^0 + Delta*h` satisfies `-1 <= f <= 1` **on the
whole slice p = 2q** (hence, by invariance, on every vertex-direction line
through the origin). So no infeasibility certificate supported on those
lines, which includes every certificate of the m=3 type, can prove the
all-m statement. This does not produce a globally bounded candidate: the
bound off the slice is not examined. The all-m question stays OPEN; the
unresolved step is a certificate that uses points off the vertex-direction
lines, or a globally bounded candidate. Range 4 <= m <= 628 for the slice
is not decided here (no radius-by-radius computation was made).

## 2. General reduction, re-derived

Domain as in the contract: `Lambda/m`, `p = k.g1/m`, `q = k.g2/m`,
frequencies `(i,j)` with `max(|i|,|j|,|i+j|) <= m` (`H_m`). D6 acts on
frequencies by the rotation `(i,j) -> (-j, i+j)` and the reflection
`(i,j) -> (j,i)`; both preserve `H_m` for every m, so D6 averaging keeps
reality, support, `f(0)=1`, the bound and the normal cosines (the three
mirror lines p=0, q=0, p=q are permuted). It suffices to treat invariant f.

- `f_m^0 = [cos mp + cos mq + cos m(p-q) - 1]/2` is invariant, supported
  on `{0}` and the six vertices of `H_m`, and equals `cos mq` on p=0,
  `cos mp` on q=0 and on p=q (verifier A1, symbolic m).
- `d = f - f_m^0` vanishes on the three mirrors; invariance under the
  reflection fixing each mirror makes its normal derivative vanish there,
  so `(z-1)^2 (w-1)^2 (z-w)^2` divides d in the Laurent ring
  (z = e^{ip}, w = e^{iq}; distinct irreducibles). With
  `Delta = sin^2(p/2) sin^2(q/2) sin^2((p-q)/2) = -(z-1)^2(w-1)^2(z-w)^2/(64 z^2 w^2)`
  (A4), `d = Delta*h` with h invariant and real.
- Newton polygon of Delta is `H_2` (A2); Newton polytopes add under
  products, and `H_m` is homothetic to `H_2`, so supp h lies in `H_(m-2)`.
- Converse (used below, and independent of the divisibility step): if h is
  invariant and supported in `H_(m-2)`, then `f_m^0 + Delta*h` is invariant,
  supported in `H_2 + H_(m-2) = H_m` (the hex norm is subadditive), has
  `f(0)=1` and the normal cosines, because Delta and its gradient vanish
  on the mirrors (A3).

The divisibility direction is analytic (not mechanized); the closure in
Secs. 3–4 uses only the converse.

**Walk-to-scalar relaxation for general m (added after review).** This is
the bridge that makes the scalar problem relevant to walks; it is stated
here for the general aligned domain, with the same hypotheses as the m=3
bridge (`reports/2026-11-05--hex-trace-m3.md` Sec. 4, R1). Let U be an s=2
walk with support F in `H_m` (in `Lambda/m` coordinates), exact hull the
radius-one hexagon, `U(0) = e^{-i phi} I`, traceless isotropic linear term,
and suppose `c_0 = r = sqrt3/2`. Put `U~ = e^{i phi} U` and
`f_U = Re Tr U~ / 2`. Then `-1 <= f_U <= 1` (two unimodular eigenvalues),
`f_U(0) = 1`, and supp `f_U` lies in `F ∪ (-F)`, inside the centrally
symmetric `H_m`. By HEX_CEILING report (`reports/2026-11-01--hex-ceiling.md`)
Sec. 3 Step 1, saturation gives on each facet normal
`U~(t n) = e^{-irt} P_+(n) + e^{irt} P_-(n)`; that step uses the
commensurate frequency grid (here of degree N = m along each normal),
unitarity, the scalar node and the traceless isotropic generator, not
minimal support. With s = 2 and `c_0 > 0` both projectors have rank one, so
`f_U(t n) = cos(r t)`: in p, q these are the normal cosines of Sec. 2. The
D6 average of `f_U` keeps all these properties and support in `H_m`.
Hence a walk saturating `c_0 = r_in` in this class gives a scalar candidate
of Sec. 2; scalar infeasibility for some m would exclude such walks at
that m. This bridge was not used in Secs. 3–4 and no walk statement is made
here; its general-N rigidity input is the cited HEX_CEILING step, read, not
re-proved.

## 3. The slice p = 2q and the image of the residuals

On `p = 2q`, `x = cos q` (B1, B2):

    f_m^0 = T_m(x)^2 + T_m(x) - 1 = G(mq),  G(t) = cos^2 t + cos t - 1,
    Delta = (1-x)^3 (1+x) / 4.

A frequency `(i,j)` restricts to `e^{i(2i+j)q}`, so `h|slice` is an even
cosine polynomial of degree <= `2(m-2)`, i.e. a polynomial `g(x)` of degree
<= `2n`, `n = m-2`.

**Image.** Let V_n = { g : deg g <= 2n, g'(-1/2) = 0 }, of dimension 2n.

- Image ⊂ V_n: the 60° rotation acts on `(p,q)` as `(p,q) -> (p-q,p)`; its
  square fixes `(4π/3, 2π/3)` mod 2π, the slice point at q = 2π/3 (C1a).
  A 120° rotation fixes no nonzero vector, so every invariant function has
  zero gradient there; along the slice, `-sin q * g'(x) = 0` at q = 2π/3,
  so `g'(-1/2) = 0`.
- dim image >= 2n: the orbit of `(a,0)`, a >= 1, has top slice frequency
  2a, and the orbit of `(a,1)`, a >= 1, has top 2a+1 (C2a, C2b, symbolic
  in a, with positive top coefficient); `(a,1)` lies in `H_n` iff a <= n-1.
  With the origin, the tops are `{0, 2, 3, ..., 2n}`: 2n distinct values,
  hence 2n independent restrictions.

So the image is exactly V_n for every m >= 3. Diagnostics m = 3..8 (C3:
rank 2(m-2), all elements with g'(-1/2)=0) and the m = 3 control (C4: image
= span{1, 4x^2+4x-2}, the promoted two-parameter form) agree; they are
consistency checks, not the proof.

**Slice problem.** Writing `P = f_m^0 + Delta*g` and `F(q) = P(cos q)`, a
residual exists with `|f| <= 1` on the slice iff there is an even cosine
polynomial F of degree <= 2m with `|F| <= 1` and

    F(0)=1, F''(0) = -3m^2, F''''(0) = 9m^4,  F(π) = (-1)^m,  F'(2π/3) = 0.

The first three say `F - G(mq) = O(q^6)` (the triple zero of Delta at x=1);
`F(π) = f_m^0(-1) = (-1)^m` is the simple zero at x = -1; the last is
`g'(-1/2) = 0`, because `f_m^0` and Delta both have zero x-derivative at
x = -1/2 and `Delta(-1/2) != 0` (C1b). Then `g = (P - f_m^0)/Delta` is a
polynomial of degree <= 2m-4 in V_n, i.e. the restriction of an admissible h.

## 4. Explicit slice solution for every m >= 629

Let `s^2 = 3m^2` (s = sqrt3 m is never an integer). Take K ≡ 0 mod 3 and
K ≡ m mod 2 (K ≡ 0 or 3 mod 6), `K1` the largest such with `K1^2 < s^2`,
`K2 = K1 + 6`; `L = 6*ceil(sqrt(m)/2)`. Put

    A(q) = λ cos(K1 q) + (1-λ) cos(K2 q),  λ = (K2^2 - s^2)/(K2^2 - K1^2),
    H(q) = 1 - (1/2)(1 - cos Lq)^2,
    B(q) = α + (1-α) H(q),  1-α = (λK1^4 + (1-λ)K2^4 - s^4) / (3 L^4),
    F = A*B.

- Bound: |A| <= 1 (convex combination of cosines), H takes values in
  [-1, 1], |B| <= 1 if α ∈ [0,1]; so |F| <= 1 everywhere.
- Taylor: A has `μ2 = s^2`, `μ4 = λK1^4 + (1-λ)K2^4`; B has `μ2 = 0`,
  `μ4 = -3(1-α)L^4`. So F has `μ2 = 3m^2`, `μ4 = 9m^4`, matching G(mq)
  (D2 by series, D3a by closed form).
- α ∈ [0,1]: the excess `E = λK1^4 + (1-λ)K2^4 - s^4 = (K2^2 - s^2)(s^2 - K1^2)`
  is positive (strict convexity) and at most `(3(K1+K2))^2 < 36(s+3)^2`;
  `3L^4 >= 243 m^2` exceeds this whenever `135m^2 - 216 sqrt3 m - 324 > 0`,
  true for m >= 4 (D1b).
- Degree: `K2 + 2L < sqrt3 m + 6 + 6 sqrt m + 12 <= 2m` whenever
  `(2 - sqrt3) y^2 - 6y - 18 >= 0`, y = sqrt m, true for m >= 629 (D1a).
- `F(π) = (-1)^m` (K ≡ m mod 2, L even) and `F'(2π/3) = 0` (K, L ≡ 0 mod 3).

Instances m = 629, 630, 1000 are checked exactly: D2 by series (the
independent Taylor test); D3a is the closed-form moment algebra, which
cancels by the definition of α and is therefore partly by construction; a negative
control without B fails the q^4 condition (D3b). At m = 3 the construction
does not apply (D3c), consistent with the promoted m=3 certificate; the
check only says the construction is unavailable there, not that the slice
is infeasible for 4 <= m <= 628.

Local control (repaired after review; not a second derivation of all
conditions): in the scaled variable t = mq the three conditions at q = 0
become those of `cos(sqrt3 t)`, a bounded function of exponential type
sqrt3 < 2 that meets them. The conditions at q = π and q = 2π/3 move to
infinity under this scaling and are not tested by the limit; they are
checked by the congruences of Sec. 4 and by D2. The control only shows the
local conditions are not an obstruction in the limit.

## 5. What is and is not established

- Established here (PRELIMINARY, unreviewed): for m >= 629 the
  vertex-direction lines carry no infeasibility certificate; in particular
  the m=3 certificate pattern cannot be extended to all m.
- Not established: global boundedness of any candidate (off-slice values of
  `f_m^0 + Delta*h` are not controlled), so this is **not**
  `SCALAR_COMPATIBLE_ALIGNED_M_<m>`; nothing about walks; nothing for
  4 <= m <= 628; nothing about other lines or 2D certificates.
- Unresolved step for the all-m question: a certificate using points off
  the vertex-direction lines, or an
  exact globally bounded candidate. The contract allows no automatic
  continuation; either needs a new decision.
- Prior art: the slice problem is a one-variable extremal problem of
  Markov/Bernstein type; the construction uses only elementary facts
  (convex combinations and products of bounded functions). No novelty
  claim; `NOVELTY = OPEN`. No classical theorem was cited, so none needed
  a page reference.

## 6. Provenance

Verifier `scripts/verify_hex_trace_aligned_all_m.py`, created before its
first run; 21 exact checks after the review repair (20 at `1154fad`, SHA-256
`f8da0f94…`); current SHA-256
`1c31653c4decbe7027b9644e155618ece7150b6a64f9d11cf0cb5fbea794f4e0`.
Command: `python3 -B scripts/verify_hex_trace_aligned_all_m.py` (about 2 s,
sympy 1.14.0). Stdout: `reports/2026-11-05--hex-trace-aligned-all-m-verifier.txt`.
Commands run in the session: the verifier, three times (first run 17/17
before the second-route checks D3 were added; then 20/20, saved; a rerun
after registering the script, 20/20, bytes unchanged); after the review
repair R1, one more run, 21/21, saved as the current stdout. No
floating-point search, no nonlinear solver, no radius sweep. Not
mechanized: the divisibility step of Sec. 2 and the interpretation of the
inequalities D1 as valid for all m >= 629 (monotonicity beyond the vertex
is checked, the algebra from the construction to D1 is in Sec. 4).
Session end: 2026-11-05T13:04:19Z.

## 7. Review and repairs

Sealed review by OpenAI `gpt-6-astra` via `revision-ciega astra`
(`~/herramientas` `ce09890`), base `8204822`
([report](../debates/2026-11-05--hex-trace-aligned-all-m-review-astra/informe_astra.md)):
blocks 1–3 (reduction and converse, slice image and one-variable
equivalence, construction) PASS; blocks 4–5 REPAIR_REQUIRED, documentary.
Repairs, none changing the construction or the outcome:

- R1 verifier label C2b claimed a membership check it did not make: label
  narrowed; new check C2c (hex norm of (a,1) is a+1) added. 21/21.
- R2 D3a partly by construction: stated in the label and in Sec. 4; D2 is
  the independent Taylor test.
- R3 timing: budget compliance marked [UNVERIFIED] (analytic start not
  timestamped).
- R4 walk-to-scalar bridge for general m added to Sec. 2, with hypotheses,
  reflected support, averaging and the cited rigidity step with N = m.
- R5 the `cos(sqrt3 t)` paragraph restated as a local control only.
- R6 "a genuinely two-dimensional measure" removed: points off the vertex
  lines could lie on other lines.
