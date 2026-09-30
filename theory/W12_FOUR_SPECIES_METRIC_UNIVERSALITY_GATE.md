# W12_FOUR_SPECIES_METRIC_UNIVERSALITY_GATE

**Fecha:** 2026-09-30.
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`
(«sí, congélalo y súbelo», 2026-09-30). Precisiones de Astra incorporadas antes de congelar:
coordenadas comunes, U5 solo en nodos `+I`, rangos sobre el coeficiente de g.
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input and purpose

W11 (repair addendum §9, A1) established that the zero-quasienergy sector of CJWW (5.15) consists
of **four** Weyl species, at the `+I` nodes

\[
p_*\in\{(0,0,0),(\pi,\pi,0),(\pi,0,\pi),(0,\pi,\pi)\},
\]

with frames \(E_*=\operatorname{diag}(\sigma_2\sigma_3,-\sigma_3,1)\), \(\sigma_i=(-1)^{p_{*i}/\pi}\),
and that any continuum coupling must use all four (option A1(i)). Both second-round reviewers
confirmed the node table. In the flat walk all four species see the same metric,
\(E_*^{T}E_*=I\).

W6 introduced nine geometry controls \(z_{ar}\) acting through transport gates

\[
T_e^{(a,r)}(g)=e^{-igZ_{ar,e}\otimes J_e^{(a,r)}},\qquad
J^{(a,r)}(p)=2\sin(p\cdot d_r)\,\sigma_a,
\]

with \(d_1=(1,0,0)\), \(d_2=(1,1,0)\), \(d_3=(1,1,1)\), and derived the induced frame
\(E=E_0-2gZD+O(g^2)\) **only at the node \(p=0\)**.

A geometry that couples to matter as gravity must give the **same metric to every species**
(species universality, the equivalence principle at this linear level). This gate asks whether
the W6 controls do so. It is a kill test for the gravity line: a negative outcome closes it for
this control class.

## 1. Single question

For a translation-invariant semiclassical background \(Z=(z_{ar})\), to first order in \(g\) and
in the species momentum \(k\), are the induced spatial metric perturbations
\(\delta h_*=E_*^{T}\delta E_*+\delta E_*^{T}E_*\) **identical at the four `+I` nodes**?

If not for all \(Z\): does a subspace \(\mathcal U\) of the nine controls exist on which they are
identical, and what metric perturbations does \(\mathcal U\) span?

## 2. Frozen setting

- Matter: one-particle CJWW (5.15) symbol \(W_0(p)\), exactly as `walk2()` in
  `scripts/verify_directional_saturation.py`.
- Deformed walk to first order: \(W_g(p)=W_0(p)\,\big(I-ig\sum_{a,r}z_{ar}J^{(a,r)}(p)\big)+O(g^2)\).
  The certificate must also check that the opposite order of the product gives the same result at
  \(O(g\,k)\); if it does not, both orders are reported and the gate is `OPEN_AFTER_AUDIT`.
- At each node define \(\delta E_*\) by
  \(s_*W_g(p_*+k)=I+i\sigma^a\big(E_*+\delta E_*\big)_a{}^{i}k_i+O(|k|^2)+O(g^2)\).
- Metric convention as in W6: \(h=E^{T}E\), so \(\delta h_*=E_*^{T}\delta E_*+\delta E_*^{T}E_*\).
- **Common coordinates.** All \(\delta h_*\) are compared as tensors in the same lattice
  coordinates \(k_i\) (the species momentum measured from its node along the fixed lattice axes).
  No species-dependent spatial redefinition, relabelling or reflection of coordinates is allowed.
- **Ranks on the coefficient of g.** Every rank and kernel in U3–U5 is computed on the linear
  coefficient \(\partial_g\delta h_*|_{g=0}\), with the nine real controls \(z_{ar}\) as independent
  variables. The \(g=0\) limit itself is only the flat-recovery check U6.
- Only the four `+I` nodes enter the universality condition. The four `−I` nodes are computed and
  reported but do not decide the gate (they are outside the A1(i) low-quasienergy contract).
- No other control family, lattice, or matter model may be introduced in this gate.

## 3. Obligations (all exact, symbolic; no numerics)

**U1 — node frames.** Recompute \(E_*\) at all eight nodes from `walk2()` and check the W11 table.

**U2 — induced frames.** Derive \(\delta E_*\) at each node as an explicit linear function of
\(Z\). Record in particular the node-dependent sign of \(\sin((p_*+k)\cdot d_r)\) to first order in
\(k\).

**U3 — universality map.** Form the linear map
\(\Phi: Z\mapsto(\delta h_{*2}-\delta h_{*1},\ \delta h_{*3}-\delta h_{*1},\ \delta h_{*4}-\delta h_{*1})\)
and compute \(\mathcal U=\ker\Phi\) and \(\dim\mathcal U\).

**U4 — universal span.** Compute the rank of \(Z\mapsto\delta h_{*1}\) restricted to \(\mathcal U\)
(maximum 6), and identify which metric components are missing if the rank is below 6.

**U5 — frame-rotation redundancy.** Separate from \(\mathcal U\) the directions that only rotate
frames (\(\delta h_*=0\) at all four `+I` nodes); they carry no metric content and do not count
towards U4. The `−I` nodes remain auxiliary here too and add no constraint.

**U6 — flat recovery.** At \(g=0\) the deformed walk is exactly CJWW (5.15).

## 4. Terminal states

1. `METRIC_UNIVERSAL_FULL`: \(\Phi=0\) (every control gives the same metric to all four species)
   and U4 has rank 6.
2. `UNIVERSAL_SUBFAMILY_FULL_RANK`: \(\Phi\neq0\) but U4 has rank 6 on \(\mathcal U\). The gravity
   line may continue with the geometry restricted to \(\mathcal U\); that restriction must be stated
   in any successor.
3. `UNIVERSAL_SUBFAMILY_DEFICIENT`: U4 has rank 1–5 on \(\mathcal U\); record the missing
   components.
4. `NON_UNIVERSAL`: U4 has rank 0 on \(\mathcal U\) (only frame rotations are universal).
5. `OPEN_AFTER_AUDIT`: the product-order check of §2 or U1 fails.

**Consequence fixed in advance.** States 3 and 4 close the gravity line for the W6/CJWW control
class as a negative result. Reopening it requires a new control family with an independent
physical justification written before any calculation; searching for a control family after the
fact to rescue universality is not allowed. State 2 allows a separate decision to continue; it
does not by itself authorize a successor gate. State 1 or 2 is not evidence of emergent gravity:
dynamics, sources, backreaction and constraints remain as recorded in W9–W11.

## 5. Certificate and review

- Certificate: `scripts/verify_w12_four_species_metric_universality.py`, SymPy, exact. It builds
  \(W_g\) from `walk2()` and the W6 symbols, extracts \(\delta E_*\) by differentiation at each
  node, and prints \(\dim\mathcal U\), the U4 rank and, if deficient, the missing components.
- Report: `reports/<fecha>--w12-four-species-metric-universality.md`, with the verdict and the
  author's prior (below) compared to the outcome.
- Independent review with `revision-ciega` (DeepSeek and Opus) before the result is used; the
  gate stays PRELIMINARY until then.

## 6. Author prior (recorded before calculation)

Claude's expectation, written before any calculation: because \(\sin((p_*+k)\cdot d_r)\) changes
sign between nodes for some \(r\) and the frames \(E_*\) differ by sign flips, generic \(Z\) will
**not** give a universal metric, so \(\Phi\neq0\). Whether a rank-6 universal subfamily exists is
not anticipated. This prior is recorded so that the outcome can be compared with it; it does not
decide anything.

## 7. Time box and claim ceiling

- Time box: one working session for certificate and report. If U1–U5 are not settled in that
  time, record `OPEN_AFTER_AUDIT` with what was done.
- Claim ceiling: first order in \(g\) and \(k\), one-particle free walk, W6 controls only. No claim
  about higher orders, interacting QCAs, the `−I` sector, dynamics of \(Z\), gravitational
  normalization, or nature.
