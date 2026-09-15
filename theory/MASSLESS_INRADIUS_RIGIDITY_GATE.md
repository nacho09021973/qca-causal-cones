# MASSLESS INRADIUS RIGIDITY GATE

> **Status: HISTORICAL / COMPLETED BY COUNTEREXAMPLE FOR THE DECLARED s=4
> CLASS** (2026-09-15, branch-local). This file is kept as the charter under
> which the counterexample was judged, and it is no longer the sole authorized
> next front. The outcome is `COUNTEREXAMPLE_VERIFIED` (Sec. 5) for the class
> declared in
> [`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md),
> with an [independent review](../reports/2026-09-15--s4-independent-review.md)
> and a [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md).
> The standard Pavia `s=2`, d=3 certificate (Sec. 0) is not affected. Rigidity
> in the published minimal `s=2` class, and in stronger classes with
> additional representation assumptions, remains OPEN, and NOVELTY remains
> OPEN. No successor gate is chartered; current status is in
> [CURRENT_STATE](../state/CURRENT_STATE.md) Sec. 7. The body below is
> unchanged from the pre-counterexample charter, except for the erratum
> below.

> **ERRATUM 2026-09-15 — vertex nilpotency does not decide saturation.**
> Earlier wording in Sec. 0(ii) and in the Sec. 5 `INADMISSIBLE_SATURATION`
> row presented a nilpotent one-step vertex coefficient as the reason for
> `c_strict^iso < \rho_{\rm micro}`. That causal reading is withdrawn. What is
> established:
>
> - For an extreme vertex `h`, the coefficient of `U^n` at `n.h` is exactly
>   `T_h^n`. If `T_h` is nilpotent, `n.h` is not in `S_n` for large `n`.
> - By the vertex lemma, if every vertex coefficient is non-nilpotent, then
>   `C_infty^strict = C_micro` and (ii) holds. So a saturation failure
>   requires at least one nilpotent vertex coefficient.
>
> The converse is **not established**. Losing the exact ray `n.h` does not
> by itself determine `h_infty` or `c_strict^iso`: mixed words can still
> reach near the vertex, and a body truncated near a vertex need not have a
> smaller minimal support. Saturation (ii) must be computed or proved for
> each candidate. Vertex nilpotency alone is neither a certificate of
> `c_strict^iso < \rho_{\rm micro}` nor an admissible explanation of one.

**Original status: OPEN — charter fixed; an executable admissible-class contract is
the next step.** Authority: [CURRENT_STATE](../state/CURRENT_STATE.md).
Predecessor: STANDARD WEYL/DIRAC EXACT GATE, PASS on evidence at `2c7c2c9`.

This charter defines the sole next scientific front. It records no new
counterexample, search result or rigidity theorem. The file name is kept for
continuity of cross-references; the object it is written against has been
corrected (Sec. 0-1 below, 2026-09-14).

## 0. Correction and baseline certificate (2026-09-14)

The gate was originally written as a comparison against the inradius of the
*one-step* microscopic causal body. That object is only an upper bound on the
speed actually reachable by strict propagation after repeated updates, and
the inradius notation is not the right general comparison for a long-run
support body. The correct comparison target is the **strict asymptotic
isotropic speed** `c_strict^iso = min_{n̂} h_infty(n̂)`, defined in
[`CAUSAL_BODY_GEOMETRY.md`](CAUSAL_BODY_GEOMETRY.md) Sec. 6 from
`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`.

For every direction `q`, define

\[
H_n(q)=\max_{x\in S_n}q\cdot x.
\]

The convolution formula for the Fourier coefficients gives

\[
S_{n+m}\subseteq S_n+S_m
\quad\Longrightarrow\quad
H_{n+m}(q)\le H_n(q)+H_m(q).
\]

Thus `(H_n(q))_n` is subadditive, and Fekete's lemma gives

\[
h_\infty(q)
=\lim_{n\to\infty}\frac{H_n(q)}n
=\inf_n\frac{H_n(q)}n.
\]

In particular, grouping `m` updates into one coarse-grained temporal step
does not change the normalized asymptotic support function:

\[
\lim_{r\to\infty}\frac{H_{mr}(q)}{mr}=h_\infty(q).
\]

This proves the coarse-graining invariance of `c_strict^iso` and is the
mathematical reason for using the `B_\infty^*` observable. Since
`S_n/n\subseteq C_{\rm micro}`, the general comparison is instead

\[
h_\infty(\hat q)\le h_{C_{\rm micro}}(\hat q),
\qquad
\rho_{\rm micro}:=
\min_{\|\hat q\|=1}h_{C_{\rm micro}}(\hat q),
\qquad
\boxed{
c_{\rm strict}^{\rm iso}
\le
\rho_{\rm micro}
}.
\]

Only when the relevant `C_micro` is centered does this last number coincide
with its usual inradius. For the centered cubic baseline used below it is
`1/\sqrt d`.

This gate's admissible class already fixes one shared `N_d` for every
candidate symbol, so `\rho_{\rm micro}` is the same fixed number for all of
them; correcting the target does not change that number. What the
correction changes is which question is actually being asked, by splitting
what used to be a single comparison into two logically independent ones for
any candidate symbol with linear massless slope `c_0`:

- **(i) genuine rigidity:** does `c_0 = c_strict^iso` for *that symbol's own*
  strict asymptotic body — does the linear IR slope match the full nonlinear
  strict propagation speed of the same dynamics?
- **(ii) saturation:** does `c_strict^iso = \rho_{\rm micro}` for that symbol —
  does its strict asymptotic body fill the entire shared one-step polytope,
  or does it fall short? (An admissible symbol only needs `T_h != 0`, not
  non-nilpotent powers of `T_h`. A nilpotent vertex coefficient is necessary
  for falling short but does not by itself imply it; see the erratum above.)

A candidate with `c_0 < \rho_{\rm micro}` that fails only (ii) — its own
`c_strict^iso` is already below `\rho_{\rm micro}` — is **not** a counterexample to `B_infty^*` and is not the kind of
result this gate is looking for; it would only have refuted the old,
superseded comparison against the one-step body. Only a failure of (i) is a
genuine rigidity counterexample. See
[`B_STAR_HYPOTHESIS.md`](B_STAR_HYPOTHESIS.md) Sec. 9.

**Established baseline fact (certified, not open):** for the standard Pavia
Weyl family in d=3 (`A+, B+, A-, B-`), both (i) and (ii) hold exactly:
`c_0 = \rho_{\rm micro} = r_{\rm in}(C_{\rm micro}) = 1/\sqrt3`
(because this is the centered cubic case; linear slope, prior exact gate) and
`C_infty^strict = C_micro` exactly, hence
`c_strict^iso = \rho_{\rm micro}`
(indeed, `\operatorname{conv}(S_n/n)=C_{\rm micro}` for every `n\ge1`)
(new vertex certificate: every one-step corner's Fourier coefficient is
rank-one and not nilpotent, so it survives at `n.h` for every `n`). Full
derivation:
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md);
machine record:
[`2026-09-14--vertex-idempotency-verification.md`](../reports/2026-09-14--vertex-idempotency-verification.md),
375 exact checks. **This is a fact about the standard baseline itself, not
an answer to Sec. 1's question about *other* admissible symbols**, and it
covers d=3 only — d=1, d=2 are not checked by this certificate.

## 1. Question and invariant comparison

For a selected standard baseline in d=1,2,3, can another admissible unitary
massless symbol have, in the sense of (i) above,

\[
0<c_0<c_{\rm strict}^{\rm iso}
\]

for its own strict asymptotic body — while keeping the same active one-step
neighborhood, causal body, Euclidean embedding, time normalization,
homogeneity and discrete isotropy as the selected standard baseline? (A
candidate additionally failing saturation (ii) is a separate, weaker
observation; see Sec. 0.)

The baseline geometries are

\[
N_d=\{(\epsilon_1,\ldots,\epsilon_d)/\sqrt d:\epsilon_j=\pm1\},
\quad C_d=[-1/\sqrt d,1/\sqrt d]^d,\quad r_d=1/\sqrt d.
\]

Choose the baseline before solving. Comparisons are within that fixed
geometry, not between dimensions. Every h in N_d must retain a nonzero
Fourier coefficient matrix, with none outside N_d. Merely retaining a
declared allowed neighborhood while actual support shrinks is insufficient.
Adding an on-site Fourier term changes N_d even if its hull would not change.

A common change of units, a different number of updates per time unit, or a
different spatial embedding cannot be used to manufacture a smaller ratio.

## 2. Mandatory class declaration before solving

Each calculation must freeze a permanent case contract containing:

| Item | Required declaration |
| --- | --- |
| Geometry | d, explicit N_d, embedding, one complete time step and Fourier convention |
| Internal degrees of freedom | Fixed finite dimension s and coefficient parameter domain |
| Discrete isotropy | The same baseline group/action L on N_d, its positive generating set if relevant, and exact covariance requirements |
| Internal symmetry | A specified unitary/projective representation R of L, fixed within the calculation |
| Gapless sector | Node k_star, quasienergy origin, branch convention, sector dimension and isolation from other bands |
| Relativistic cone | Nonzero, untilted, isotropic linear speed in the fixed Euclidean coordinates; an axis slope alone is insufficient |
| Reducibility/minimality | Whether assumed; sector support and the role of any spectator blocks |
| Coverage | Full coefficient class versus a particular ansatz, including any disconnected components not covered |
| Equivalences | Constant basis conjugations, symmetry relabelings, transposes/chiralities and node relabelings identified explicitly |

Fixing the causal body and saying "discrete isotropy" does not specify s,
the symmetry representation or the relevant massless sector. A trivial or
weaker symmetry group cannot replace the baseline's isotropy. Discrete
covariance and an isotropic IR cone are separate admission requirements.

Begin with source and class-definition work, not a solver run. Minimal s=2
and enlarged internal spaces are different quantified classes. No result
proved only with minimality may be presented as following from locality,
unitarity, homogeneity and discrete isotropy alone. A change of s or R needs
its own declared class before calculation, with the same geometric and group
action constraints; it cannot silently alter an existing comparison.

For a selected sector, document how its support relates to the full active
support. A reducible/direct-sum example must be identified as such and judged
against the declared quantifiers. Do not silently rule it out or present
spectator-supported geometry as intrinsic to the selected sector. If one
instead requires irreducibility or a common cone for the whole symbol, that
is an additional hypothesis and limits any rigidity conclusion.

## 3. Exact admission checks

Write the homogeneous finite-range symbol as

\[
U(\mathbf k)=\sum_{h\in N_d}e^{-i\mathbf k\cdot h}T_h,
\qquad T_h\in\mathbb C^{s\times s},\quad T_h\ne0.
\]

For every displacement difference ell, verify the coefficient identities

\[
\sum_{h'-h=\ell}T_h^\dagger T_{h'}=\delta_{\ell0}I_s,
\qquad
\sum_{h-h'=\ell}T_h T_{h'}^\dagger=\delta_{\ell0}I_s.
\]

These certify unitarity for every momentum rather than on a finite mesh.
For every group element g, verify

\[
T_{gh}=R_gT_hR_g^\dagger,
\qquad U(g\mathbf k)=R_gU(\mathbf k)R_g^\dagger.
\]

Check the declared representation, active support and node exactly. In the
specified gapless sector derive the full linearized spectrum, requiring

\[
\omega_\pm(\mathbf k_\star+\mathbf p)-\omega_\star
=\pm c_0|\mathbf p|+O(|\mathbf p|^2),\qquad c_0>0,
\]

in every direction. Rule out a residual mass gap, tilt, flat band mistaken
for a cone, or anisotropic linear metric before comparing c_0 with the
candidate's own `c_strict^iso` (Sec. 0); comparing only against r_d checks
saturation (ii), not genuine rigidity (i), and the two must not be conflated.
If there are multiple cone sectors, identify exactly which are quantified.

These are admission criteria, not assertions that a new admissible symbol
exists. Any scientific code implementing them must be retained in the repo.

## 4. Adversarial sequence and acceptance

1. Read the primary classification results and list their actual assumptions:
   support, s, isotropy action/representation, minimality, node and equivalences.
   The prior battery did not establish an exhaustive classification. Check
   whether a proposed rigidity statement is already covered by existing work.
2. Freeze one admissible-class contract and its quantified target. Derive the
   coefficient constraints before choosing a special product/coin ansatz;
   if an ansatz is used, state its coverage ceiling.
3. Seek a structural counterexample while retaining all admission conditions.
   A failed condition makes a candidate inadmissible, not a falsifier of
   B_infty^*. Stop its certification at the first failed condition and
   record the reason.
4. Accept a counterexample only with exact support, unitary and covariance
   certificates, a massless isotropic linearization, and a proved strict
   inequality `0 < c_0 < c_strict^iso` for that candidate's own strict
   asymptotic body, in the same units (Sec. 0(i)). A candidate satisfying
   only `0 < c_0 < r_d` while `c_strict^iso < r_d` for the same candidate
   (saturation failure, Sec. 0(ii)) is not this counterexample; record it
   separately as INADMISSIBLE_SATURATION (Sec. 5). Numerical suggestions
   need exact certification; no finite scan or tolerance establishes the
   claim.
5. If no counterexample is obtained, retain OPEN unless an exhaustive analytic
   argument proves matching for every member of the declared class. Local
   absence of deformations does not exclude disconnected solutions.

The seven old symbols may serve as controls. Repeating related representatives
does not increase the number of independent geometries or establish coverage
of structural degrees of freedom.

## 5. Outcomes and claim ceilings

| Outcome | Meaning |
| --- | --- |
| COUNTEREXAMPLE_VERIFIED | `0 < c_0 < c_strict^iso` proved for that candidate's own strict body (Sec. 0(i)): B_infty^* is false for the declared class and any broader claim including this admissible example |
| RIGIDITY_PROVED_FOR_FROZEN_CLASS | `c_0 = c_strict^iso` is proved for every member with every class restriction retained; wider classes remain open |
| INADMISSIBLE_SATURATION | Candidate is admissible and `c_0 = c_strict^iso` (i) holds, but `c_strict^iso < r_d` (ii) fails — a saturation failure, certified by computing `c_strict^iso` and not inferred from vertex nilpotency (erratum above); not a rigidity counterexample; B_infty^* is not decided by this candidate |
| INADMISSIBLE_CANDIDATE | At least one invariant or cone condition fails; B_infty^* is not decided |
| INCONCLUSIVE / OPEN | No certified counterexample or exhaustive proof; a solver failure or unsuccessful search is not rigidity |

Even a rigidity result here would not establish inter-species universality A
or general continuum matching for other couplings. Novelty requires the
separate source comparison. No anisotropic-QCA detour, broad model search,
causal sets or new substrate class is authorized by this charter.
