# MASSLESS INRADIUS RIGIDITY GATE

**Status: OPEN — charter fixed; an executable admissible-class contract is
the next step.** Authority: [CURRENT_STATE](../state/CURRENT_STATE.md).
Predecessor: STANDARD WEYL/DIRAC EXACT GATE, PASS on evidence at `2c7c2c9`.

This charter defines the sole next scientific front. It records no new
counterexample, search result or rigidity theorem.

## 1. Question and invariant comparison

For a selected standard baseline in d=1,2,3, can another admissible unitary
massless symbol have

\[
0<c_0<r_{\rm in}(C_{\rm micro})
\]

while keeping the same active one-step neighborhood, causal body, Euclidean
embedding, time normalization, homogeneity and discrete isotropy?

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
for a cone, or anisotropic linear metric before comparing c_0 with r_d.
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
   A failed condition makes a candidate inadmissible, not a falsifier of B*_0.
   Stop its certification at the first failed condition and record the reason.
4. Accept a counterexample only with exact support, unitary and covariance
   certificates, a massless isotropic linearization, and a proved strict
   inequality `0 < c_0 < r_d` in the same units. Numerical suggestions need
   exact certification; no finite scan or tolerance establishes the claim.
5. If no counterexample is obtained, retain OPEN unless an exhaustive analytic
   argument proves matching for every member of the declared class. Local
   absence of deformations does not exclude disconnected solutions.

The seven old symbols may serve as controls. Repeating related representatives
does not increase the number of independent geometries or establish coverage
of structural degrees of freedom.

## 5. Outcomes and claim ceilings

| Outcome | Meaning |
| --- | --- |
| COUNTEREXAMPLE_VERIFIED | B*_0 is false for the declared class and any broader claim including this admissible example |
| RIGIDITY_PROVED_FOR_FROZEN_CLASS | Matching is proved with every class restriction retained; wider classes remain open |
| INADMISSIBLE_CANDIDATE | At least one invariant or cone condition fails; B*_0 is not decided |
| INCONCLUSIVE / OPEN | No certified counterexample or exhaustive proof; a solver failure or unsuccessful search is not rigidity |

Even a rigidity result here would not establish inter-species universality A
or general continuum matching for other couplings. Novelty requires the
separate source comparison. No anisotropic-QCA detour, broad model search,
causal sets or new substrate class is authorized by this charter.
