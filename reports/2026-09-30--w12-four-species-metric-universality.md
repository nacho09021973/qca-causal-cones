# W12 — Four-species metric universality

**Contract:** [`W12_FOUR_SPECIES_METRIC_UNIVERSALITY_GATE.md`](../theory/W12_FOUR_SPECIES_METRIC_UNIVERSALITY_GATE.md), frozen at `2ff88b2`.
**Certificate:** [`verify_w12_four_species_metric_universality.py`](../scripts/verify_w12_four_species_metric_universality.py), SHA256 `dc17823a267a0085ec10f030e6e1bade738fbf91c95a3e119bf009fbbdbbcc73`.
**Execution:** 2026-09-30, branch `research/gravitational-normalization-gate`.
**Review:** not yet conducted; user will launch the contracted blind review. Evidence remains **PRELIMINARY / INDEPENDENT_REVIEW_PENDING**.

## Verdict

```
W12 = UNIVERSAL_SUBFAMILY_DEFICIENT
rank(Phi) = 6
 dim(U) = 3
rank(metric | U) = 3 / 6
common metric-null directions in U = 0
```

For the nine W6 controls, generic backgrounds do not give the same linear metric to the four `+I` species. The universal subspace consists only of the three diagonal control directions, and these span a three-dimensional part of the six-dimensional spatial-metric tangent space. Per the frozen contract, this is the negative outcome for this W6/CJWW control class; it does not authorize searching a replacement control family. The outcome is preliminary until independent review.

## U1 — nodes and frames

The certificate recomputes the frames from `walk2()` at all eight corners and checks
\(E_* = \operatorname{diag}(\sigma_2\sigma_3,-\sigma_3,1)\), with
\(s_*=(-1)^{b_1+b_2+b_3}\) at \(p_*=\pi(b_1,b_2,b_3)\).
The following table records `s*`, the diagonal of `E*`, and the direction signs \(\tau_r=(-1)^{b\cdot d_r}\). The four `−I` rows are diagnostics only.

| Node \(b=p_*/\pi\) | \(s_*\) | \(\operatorname{diag}E_*\) | \((\tau_1,\tau_2,\tau_3)\) |
|---|---:|---|---|
| (0,0,0) | +1 | (1,−1,1) | (+,+,+) |
| (0,0,1) | −1 | (−1,1,1) | (+,+,−) |
| (0,1,0) | −1 | (−1,−1,1) | (+,−,−) |
| (0,1,1) | +1 | (1,1,1) | (+,−,+) |
| (1,0,0) | −1 | (1,−1,1) | (−,−,−) |
| (1,0,1) | +1 | (−1,1,1) | (−,−,+) |
| (1,1,0) | +1 | (−1,−1,1) | (−,+,+) |
| (1,1,1) | −1 | (1,1,1) | (−,+,−) |

The `+I` node set matches the frozen contract. At zero coupling, all four have \(E_*^TE_*=I\).

## U2 — induced frames and product order

Use the W6 matrix with direction vectors as **rows**,
\[
D=\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix},\qquad
\tau_*=(\tau_1,\tau_2,\tau_3).
\]
Differentiating the frozen product \(W_g=W_0(I-igJ)\) gives, at every node,
\[
\frac{\delta E_*}{g}=-2Z\,\operatorname{diag}(\tau_*)D.
\]
The opposite product order \((I-igJ)W_0\) gives the same coefficient at order \(gk\). The exact comparison passes at all eight nodes. The flat check gives \(W_g|_{g=0}=W_0\).

The signs in the table arise directly from
\(\sin((p_*+k)\cdot d_r)=\tau_r(k\cdot d_r)+O(|k|^3)\). Both product orders have the same node value because \(J(p_*)=0\); their difference begins beyond the retained linear order in k.

## U3 — universality subspace

With control coordinates ordered
\((z_{11},z_{12},z_{13},z_{21},z_{22},z_{23},z_{31},z_{32},z_{33})\), the exact 18-by-9 matrix for \(\Phi\) has rank 6. Its kernel is
\[
\mathcal U=\operatorname{span}\{e_{11},e_{22},e_{33}\},\qquad\dim\mathcal U=3,
\]
where \(e_{ar}\) means the single control \(z_{ar}\) is nonzero. Thus the prior that generic controls are nonuniversal is confirmed. The calculation finds the universal subspace rather than assuming it.

## U4 — metric span on \(\mathcal U\)

Order metric components as \((h_{11},h_{22},h_{33},h_{12},h_{13},h_{23})\). In the displayed control basis, the reference-species map restricted to \(\mathcal U\) is
\[
\begin{pmatrix}
-4&0&0\\
0&4&0\\
0&0&-4\\
0&2&0\\
0&0&-2\\
0&0&-2
\end{pmatrix},
\qquad \operatorname{rank}=3.
\]
Equivalently, writing the three universal controls as \(a=z_{11}, b=z_{22}, c=z_{33}\),
\[
\frac{\delta h_*}{g}=
\begin{pmatrix}
-4a&2b&-2c\\
2b&4b&-2c\\
-2c&-2c&-4c
\end{pmatrix}
\quad\text{at every `+I` node.}
\]
No individual coordinate component is identically zero throughout this span. Its three missing directions in the space of \(\delta h/g\) are expressed by the independent relations
\[
(\delta h/g)_{12}=\tfrac12(\delta h/g)_{22},\qquad
(\delta h/g)_{13}=\tfrac12(\delta h/g)_{33},\qquad
(\delta h/g)_{23}=\tfrac12(\delta h/g)_{33}.
\]
Therefore U4 is rank-deficient, not full-rank.

## U5 — frame rotations

The common metric map on the four `+I` species has a zero-dimensional kernel in the nine control variables. Hence no nonzero direction in \(\mathcal U\) is a pure common frame rotation with zero metric at every decisive node. These results are only about the linearized metric map; they do not establish a microscopic frame gauge symmetry.

## U6 — flat recovery and claim ceiling

At \(g=0\), the deformation reduces exactly to `walk2()`, as required. The whole calculation is exact and symbolic in the first-order coefficient of \(g\) and first-order species momentum \(k\), for the one-particle CJWW (5.15) symbol and the frozen nine W6 controls. Coordinates are held common across species. The `−I` nodes do not enter \(\Phi\), \(\mathcal U\), or the verdict.

This outcome does not establish or refute gravity outside the declared W6/CJWW control class. It says nothing about higher orders, interacting walks, metric dynamics, local stress at nonzero transfer, backreaction, constraints, or gravitational normalization. A positive subfamily decision would have required a separate authorization; none is implied here.

**Verification command:** `python3 -B scripts/verify_w12_four_species_metric_universality.py` — PASS for U1–U6 and the stated verdict.

## Addendum — review and closure, 2026-09-30

- **Blind review** ([record](../debates/2026-09-30--w12-blind-review/README.md), `4b0797d`):
  DeepSeek ACCEPT; Opus ACCEPT_WITH_REPAIRS. Both recompute U1–U5 by hand and confirm the verdict;
  both find it invariant under the conventions the contract allows. An independent re-derivation by
  Claude (`verify_w12_independent.py`) gives the same result, also with `h = E Eᵀ`.
- **Opus's additional facts, confirmed** (`verify_reviewer_claims.py`): on 𝒰,
  `δh(−I) = −δh(+I)`, so an eight-node test would be `NON_UNIVERSAL`; each `+I` node alone has
  metric rank 6 and node-dependent rotation kernels; read as a gauge condition on
  `δh = ∂ᵢξⱼ + ∂ⱼξᵢ`, the three missing relations have symbol determinant
  `−q₃(2q₁q₂ − q₁q₃ − q₂²)`.
- **Citation scope.** The rank `3/6` refers to constant δh, which is gauge-trivial. The result is a
  contract outcome for constant W6 controls, not a proof that three physical metric degrees of
  freedom are missing; the gauge-aware deficit is `q₃ = 0` and a cone.
- **Closure.** By direct user decision («cierra la línea como dice el contrato»), the contract's
  §4 consequence applies: the gravity line is **closed** for the W6/CJWW control class as a
  negative result. No joint Einstein–Weyl gate is opened. Opus's presentation repairs (−I δh
  reporting, U6 "by construction", extra asserts) are recorded in the review README and do not
  change the verdict; they are not applied here.

