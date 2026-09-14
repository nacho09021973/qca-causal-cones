# Strict asymptotic propagation body: exact Pavia d=3 baseline certificate

Date: 2026-09-14. Baseline: `5845eda` plus this commit's extension of
`scripts/verify_weyl_dirac_gate.py` (new checks only; the seven original
cases, their 247 checks, and the frozen
[verification record](2026-09-14--weyl-dirac-verification.md) are untouched).
New machine record:
[`2026-09-14--vertex-idempotency-verification.md`](2026-09-14--vertex-idempotency-verification.md),
375 exact checks, zero tolerance.

**Purpose of this report.** `B*` has so far been stated in terms of
`r_in(C_micro)`, the inradius of the *one-step* microscopic causal body. That
object need not coincide with the speed actually achievable by *strict*
ballistic propagation after coarse-graining in time. This report (a) defines
the correct strict asymptotic object, (b) shows why calling it "inradius" in
general is wrong, and (c) certifies that for the standard Pavia Weyl family in
d=3 the two objects coincide exactly. It does not touch the massive-sector
results, does not decide the open rigidity question for other admissible
symbols, and does not attribute anything to Ahlbrecht–Vogts–Werner–Werner or
any ballistic-limit theorem — no such attribution is used or needed here.

## 1. The strict asymptotic support function

Fix a homogeneous finite-range QCA step `U(k) = sum_{h in N} e^{-i k.h} T_h`
with the frozen unit-neighbor, unit-time coordinates of the standard battery.
For `n >= 1`, let

`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`.

Define the strict asymptotic support function

`h_infty(q_hat) = limsup_{n->infty} (1/n) max_{x in S_n} q_hat . x`,

and the isotropic scalar, with the origin fixed at `v = 0` (the physically
privileged rest point, not a free normalization choice),

`c_strict^iso = min_{||q_hat||=1} h_infty(q_hat)`.

**B_infty^*** (replaces the inradius-only statement of `B*` for the massless/
continuum sector): `c_0 = c_strict^iso`, for the declared gapless sector and
the same embedding/time convention used to define `c_0`.

### 1.1 Trivial inclusion and the general inequality

`S_n subseteq n.N-fold sumset subseteq n.C_micro` for every `n`, since each
one-step displacement lies in `C_micro = conv(N)` by definition. Hence
`S_n/n subseteq C_micro` for every `n`, so for every direction `q_hat`,
`(1/n) max_{x in S_n} q_hat.x <= h_{C_micro}(q_hat)`, and therefore

`h_infty(q_hat) <= h_{C_micro}(q_hat)` for every `q_hat`, hence
`c_strict^iso <= r_in(C_micro)`.

This inequality is general and requires no computation. It is the reason
`r_in(C_micro)` was ever a reasonable candidate: it is a provable *upper
bound* on the strict asymptotic isotropic speed, not a definition of it.
Equality is a separate, checkable fact, established below only for the
Pavia baseline.

### 1.2 Why "inradius" is the wrong general name: the pure-shift sanity check

Take `U` to be a pure shift by `h_0 != 0` (one-element support,
`N = {h_0}`). Then `S_n = {n h_0}` for every `n`, so

`h_infty(q_hat) = q_hat . h_0` exactly (no limsup is needed; the sequence is
constant), and therefore

`min_{q_hat} h_infty(q_hat) = -||h_0|| < 0`.

There is no bidirectional isotropic cone centered at `v = 0` here at all: the
"cone" is a single ray. A name built on "inradius of a centered body" silently
assumes centering that a pure shift violates. `c_strict^iso` remains
well-defined and negative in this case, which is the correct statement that
no such isotropic ball exists; `r_in` of a one-point body is not comparably
meaningful, and conflating the two is exactly the terminology error this
report removes from the charter. (This example is a sanity check on the
*definition*, not a claim about any QCA in this repository's battery: no
one-step support here is a singleton.)

## 2. The vertex/convexity lemma

**Lemma.** Let `C` be convex, `h` an extreme point of `C`, and
`x_1, ..., x_n in C` with `(1/n) sum x_i = h`. Then `x_i = h` for every `i`.

*Proof.* For `n = 1` this is trivial. For `n >= 2`, write
`h = (1/n) x_1 + (1 - 1/n) y`, where `y = (1/(n-1)) sum_{i=2}^n x_i` is a
convex combination of points of `C`, hence `y in C`. Since `1/n in (0,1)` and
`h` is extreme, `h = t.a + (1-t).b` with `a, b in C`, `t in (0,1)` forces
`a = b = h`; here `a = x_1`, `b = y`. So `x_1 = h` and `y = h`. Repeat the
argument on `y = h` with the remaining `n-1` points. Induction on `n` gives
`x_i = h` for every `i`. QED.

**Consequence for `S_n`.** Let `h` be a vertex of `C_micro = conv(N)` (so
`h in N`, since `N`'s convex hull vertices are themselves elements of `N` in
every case in this battery — the neighbor set already consists of cube
corners). Then `n.h` can be written as a sum of `n` elements of `N` in exactly
one way: `h_1 = ... = h_n = h`. Since the Fourier coefficient of `U^n` at
displacement `x = sum h_i` is `sum_{h_1+...+h_n=x} T_{h_1} T_{h_2} ... T_{h_n}`
(ordered matrix product, summed over all decompositions — a direct consequence
of expanding `U(k)^n` as a product of `n` copies of the same Laurent series),
the sum at `x = n.h` collapses to the single term

`[U^n]_{n.h} = T_h^n = A_h^n`.

So: **`A_h` not nilpotent implies `n.h in S_n` for every `n >= 1`.**

## 3. Exact d=3 Pavia certificate: every vertex survives

The d=3 standard Weyl symbols and their transposes are, in the frozen
factorization,

`A^+ = R_x(q_x) R_y(-q_y) R_z(q_z)`, `A^- = R_x(q_x) R_y(q_y) R_z(q_z)`,
`B^+ = (A^+)^T`, `B^- = (A^-)^T`, `q_j = k_j/sqrt(3)`,

as already frozen by the exact-gate
[contract](2026-09-14--weyl-dirac-gate-contract.md) and reconstructed by
`published_symbol`/`rotation_product` in the verifier (`d=3 A/B` check,
`published vs product`). The one-step support of each is exactly the 8 cube
corners `N_3 = {(eps_1,eps_2,eps_3)/sqrt(3) : eps_j = +-1}`
(already certified: `active support` check, `2026-09-14--weyl-dirac-exact-gate.md`
Sec. 3). All 8 corners are vertices of `C_micro = [-1/sqrt(3), 1/sqrt(3)]^3` in
the elementary sense required by the Sec. 2 lemma.

The new checks in `scripts/verify_weyl_dirac_gate.py`
(`verify_vertex_idempotency`, function added this commit; reuses
`published_symbol` and `fourier_support`, no new script) extract each corner's
Fourier coefficient `A_h` directly from the same matrices and establish, for
all four cases `A+, B+, A-, B-` and all 8 corners `h`, exactly:

`det(A_h) = 0`,

`A_h^2 = alpha_h . A_h`, `alpha_h in {alpha_+ , alpha_-}`,
`alpha_+ = (1-i)/4`, `alpha_- = (1+i)/4`.

Concretely, writing `P = {(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)}` for the four
positive BCC generators (product of signs `= +1`): for `A+`, `alpha_h =
alpha_+` on `P` and `alpha_h = alpha_-` on the complementary four corners; for
`A-` the two roles swap. `B+`/`B-` reproduce the same table as `A+`/`A-`
exactly (transposition preserves both `det` and `trace` of each corner
coefficient, and the identity `A_h^2 = alpha_h A_h` transposes to
`(A_h^T)^2 = alpha_h A_h^T`), which the checker verifies directly rather than
asserting by a symmetry sentence. All 32 `(case, vertex)` combinations are
checked exactly (zero tolerance); see the 375-check record for the full table.

`det(A_h) = 0` and `A_h^2 = alpha_h A_h` are consequences of the
Cayley–Hamilton identity for the `2x2` matrix `A_h` (`A_h^2 -
tr(A_h) A_h + det(A_h) I = 0`) together with the exact vanishing determinant;
`alpha_h = tr(A_h) != 0` in every case. Since a nilpotent `2x2` matrix must
have zero trace, `alpha_h != 0` alone already rules out nilpotency. The
idempotent-square identity gives the sharper, exact statement used in Sec. 2:

`A_h^n = alpha_h^{n-1} . A_h != 0` for every `n >= 1`

(by induction from `A_h^2 = alpha_h A_h`; `alpha_h != 0` and `A_h != 0`, the
latter already certified by the `active support` check of the base battery).

## 4. Conclusion for this baseline

By Sec. 2-3, for every one of the 8 vertices `h` of `C_micro` and every
`n >= 1`, `n.h in S_n`. Combined with the trivial inclusion `S_n/n subseteq
C_micro` (Sec. 1.1),

`conv(S_n/n) = C_micro` for every `n >= 1`

in this baseline (not only in the limit: the full vertex set is already
present at every `n`). Consequently, for every direction `q_hat`,
`(1/n) max_{x in S_n} q_hat.x = h_{C_micro}(q_hat)` exactly for every `n`, so
the limsup is trivial and

`h_infty = h_{C_micro}` exactly, hence

`C_infty^strict := ` the strict asymptotic body ` = C_micro`, and

`c_strict^iso = r_in(C_micro) = 1/sqrt(3) = c_0`.

**This closes the Sec. 1.1 inequality to equality for this baseline only.**
It is a certificate about the standard Pavia Weyl family in d=3 (`A+, B+, A-,
B-`), established by an exact algebraic vertex check plus an elementary
convexity lemma — not a rigidity theorem for other admissible massless
symbols, not a statement about d=1 or d=2 (not checked here), and not a
resolution of the [rigidity gate](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md).
In particular, an admissible alternative symbol satisfying the same one-step
`N_3`, unitarity, homogeneity and discrete isotropy could in principle have a
nilpotent corner coefficient (the admissibility class only requires each
`T_h != 0`, not non-nilpotency of its powers); such a symbol's own
`C_infty^strict` would then be a strict subset of `C_micro`, and its own
`c_strict^iso` a strict lower bound below `1/sqrt(3)` — a purely combinatorial
fact with no bearing on whether that symbol's `c_0` matches its *own*
`c_strict^iso`. Distinguishing these two questions is the point of replacing
`B*` with `B_infty^*`; see `theory/B_STAR_HYPOTHESIS.md` and
`theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md`.

## 5. Bibliographic caution (explicitly not used)

No claim in this report or in the updated charter relies on, or cites, a
ballistic-limit theorem of Ahlbrecht–Vogts–Werner–Werner, nor on the general
inclusion `V_grp^max subseteq C_infty^strict` (or any scalar form of it).
Neither appeared anywhere in this repository before this report, and neither
is introduced now. If a future report wants either, it must be added as an
explicit **UNVERIFIED / NOT USED** claim with its own source check, per
`PROJECT_INSTRUCTIONS.md` Sec. 4-6; the certificate above needs neither.

## 6. Reproduction

```sh
python3 scripts/verify_weyl_dirac_gate.py \
  --output reports/2026-09-14--vertex-idempotency-verification.md
```

This reruns the full accumulating check list (the original 247 checks plus
the 128 new vertex checks = 375) and rewrites only the new file above; the
historical `2026-09-14--weyl-dirac-verification.md` (247 checks) is a
separate, untouched record of the pre-extension verifier.
