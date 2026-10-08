# IG-S2 — exact information from the true ground space

Date: 2026-10-08

Branch: `research/inverse-gravity-design`.
Base: `d92a136`. Contract frozen at `f57b0e6`;
permanent auxiliary code frozen at `1bfa5a7` before execution.
Authorization: the user instructed continuation using the true ground space.

Results, author-side:

- `GROUND_SPACE_SUM_RULE_ANALYTIC_PASS_AUTHOR_SIDE`.
- `AVERAGED_RANK_TWO_MODE_INFERENCE_FAIL` without degeneracy control.
- `NTYPE_GROUND_MOMENTS_UNKNOWN / TENSOR_SPECTRAL_GATE_OPEN`.

These are exact consequences of the ground-space condition, not computed
N-type vacuum correlations. No actual value of a previously unknown ground
expectation, ground degeneracy, energy or spectral gap is supplied.

## 1. True-ground conditions and source

Use exactly the q=3 N-type Hamiltonian and fixed curvature probes of
`INVERSE_GRAVITY_CURVATURE_PROBE_GATE.md` on even L>=4, with unchanged positive
comparable couplings. Let
\[
 P_0=\mathbf1_{\{E_0\}}(H_L),\quad d_0=\operatorname{Tr}P_0,\quad
 \rho_0=P_0/d_0,\quad K=H_L-E_0I\ge0,\quad Q_0=I-P_0.
\]
These definitions refer to the entire finite-volume H_N Hilbert space.
Their existence does not provide their matrix elements. The available exact
information is
\[
 HP_0=E_0P_0,\quad \rho_0K=K\rho_0=0,\quad
 \operatorname{Tr}\rho_0[H,O]=0,\quad
 \operatorname{Tr}\rho_0 A^\dagger[H,A]\ge0.
\]
The last inequality follows from
\(\operatorname{Tr}\rho_0 A^\dagger[H,A]
=\operatorname{Tr}\rho_0 A^\dagger K A\).
It is a ground-state condition stronger than stationarity alone.

Primary source checked: `biblioteca/arXiv-0907.1203.pdf`,
Gu–Wen arXiv:0907.1203v3, Eqs.(39), (47)–(48) on pp.14–15 and the complete
N-type terms on p.18. PDF SHA256:
`3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
The source fixes H_L and probe stencils; the identities below are derived here.

## 2. Exact reality and D=2F in the canonical ground density

H_L is real symmetric in the momentum basis. H_J and the vector penalties are
real diagonal cosine functions. The scalar penalties are sums of real
permutation matrices and their transposes. Each sine of a rho word is purely
imaginary in this basis, so the product of the two commuting sines in H_g is
real; its cosine terms are real as well. Thus complex conjugation leaves H_L,
K, P_0 and rho_0 invariant.

Each curvature density \(o_\alpha(i)\) is purely imaginary and Hermitian.
Consequently the fixed Fourier probes satisfy
\(B_\alpha(p)^*=-B_\alpha(p)^\dagger\).
Define
\[
 F_{\alpha\beta}=\operatorname{Tr}\rho_0 B_\alpha^\dagger K B_\beta,\quad
 D_{\alpha\beta}=\operatorname{Tr}\rho_0
 [B_\alpha^\dagger,[H,B_\beta]].
\]
Ground stationarity gives
\[
 D_{\alpha\beta}=F_{\alpha\beta}
 +\operatorname{Tr}\rho_0 B_\beta K B_\alpha^\dagger.
\]
Reality identifies the second term with \(F_{\beta\alpha}^*\), which equals
F_alpha,beta because F is Hermitian. Therefore
\[
 D=2F,\qquad F\succeq0.
\]
This relation uses the actual full ground projector, including degeneracy.
It holds at allowed Fourier momenta and needs no spatial inversion symmetry.
It also holds in a conjugation-invariant pure ground state. It is not asserted
for an arbitrary complex pure member of a degenerate ground space.

The ground-subtracted averaged Gram is
\[
 G_{\alpha\beta}=\operatorname{Tr}\rho_0
 B_\alpha^\dagger Q_0 B_\beta.
\]
An averaged matrix bound F<=C|p|G has a meaning, but its rank is not automatically
the number of distinct excited vectors in the physical Hilbert space.

## 3. Locality reduces the axial first moment to five coefficients

Write the fixed probes as
\[
 B_\alpha(p)=N^{-1/2}\sum_i(-1)^i e^{-ip i_z}o_\alpha(i),
\]
with \(o_+=(b_{xx}-b_{yy})/\sqrt2\),
\(o_\times=-b_{xy}/\sqrt2\), and the cross density on the actual xy face.
Along z the face-offset phase is one. rho_0 is translation invariant because
P_0 is a spectral function of the translation-invariant H_L.

The exact preceding reduction gives [H,B]=[H_J,B].
Since all curvature densities commute with each other, a nested commutator
\([o_\alpha(i),[h,o_\beta(j)]]\) can be nonzero only when both densities touch
the support of the same H_J term h.
H_J has single-register terms and diagonal-register trace terms on one vertex.
Each curvature density uses cell anchors with z-displacement at most one.
Hence their relative axial displacement satisfies |j_z-i_z|<=2.
For a mixed +/cross pair it is at most one.

Define the finite local matrices
\[
 C_n(L)_{\alpha\beta}=
 \sum_{d:\,d_z=n}(-1)^{d_x+d_y+d_z}
 \operatorname{Tr}\rho_0
 [o_\alpha(0),[H_J,o_\beta(d)]],\qquad -2\le n\le2.
\]
Only a fixed finite set of d contributes, independent of L. On the smaller
torus periodize the same local terms; unwrapped displacements still reproduce
the formula at every allowed momentum, with aliases included.
Translation invariance yields
\[
 D_L(p)=\sum_{n=-2}^{2}e^{-inp}C_n(L).
\]
Thus its energy numerator depends on five 2x2 matrices of *local ground
expectations*, rather than the entire long-range Gram correlator.
The matrices are unknown, not supplied by the tangent symbol.
They obey C_-n=C_n^dagger in expectation; mixed entries of C_+/-2 vanish by
support. Norms are uniformly bounded by finite support and fixed J.

## 4. What a fourth-order cancellation would require

For the fixed degree-two Fourier polynomial to have an exact fourth-order
zero at p=0, its four moments must vanish:
\[
 M_j(L)=\sum_{n=-2}^{2}n^j C_n(L)=0,\qquad j=0,1,2,3.
\]
The four-by-five scalar moment matrix has one-dimensional kernel
\((1,-4,6,-4,1)\), so this is equivalent entrywise to
\[
 C_{-2}=C_2=T_L,\quad C_{-1}=C_1=-4T_L,\quad C_0=6T_L.
\]
Then
\[
 D_L(p)=16\sin^4(p/2)T_L=a(p)^2T_L.
\]
If ||T_L||<=tau uniformly and T_L>=0, this provides D<=tau p^4 I.
The mixed-degree support forces T_L to be diagonal for this exact factorization.

This is a characterization of an exact cancellation of the polynomial,
not a necessity theorem for the original bound only at p_L=2pi/L.
A bound on that discrete sequence can hold with finite-size moment errors.
One sufficient quantitative alternative is
\[
 \|M_j(L)\|\le c_j p_L^{4-j},\qquad j=0,1,2,3.
\]
Taylor's formula gives
\[
 D_L(p_L)=M_0-ip_LM_1-\tfrac12p_L^2M_2
          +\tfrac{i}{6}p_L^3M_3+R_4,
\quad
 \|R_4\|\le\frac{p_L^4}{24}\sum_n|n|^4\|C_n(L)\|.
\]
The uniform local bound controls the last sum, proving sufficiency of the
quantitative moment estimates. An unquantified thermodynamic cancellation
M_j(L)->0 is insufficient for these finite-size rates.
None of these cancellations or rates is currently proved for H_N.

## 5. The first missing quantity is a true-ground-space energy cost

At p=0 the probe B(z,0)=z_+ B_+(0)+z_cross B_cross(0) is Hermitian for real z.
More generally the matrix identity from Section 2 gives
\[
 z^\dagger M_0(L)z=
 \frac{2}{d_0}\|K^{1/2}B(z,0)P_0\|_{\mathrm{HS}}^2\ge0.
\]
For both directions to have M_0=0 is equivalent to
\[
 Q_0 B_\alpha(0)P_0=0,\qquad \alpha=+,\times.
\]
The equivalence uses the positive excitation eigenvalues at each finite
volume, without assuming a volume-independent gap.
This is preservation of the *energy ground space* by the zero-envelope-
momentum probes, stronger than preservation of scalar/vector constraints.

The energy along a unitary variation generated by a Hermitian B(0) is
\[
 {\cal E}(t)=\operatorname{Tr}\rho_0 e^{-itB(0)}H e^{itB(0)}.
\]
It satisfies E'(0)=0 and E''(0)=D(0)>=0 because rho_0 is a ground density.
It need not satisfy E''(0)=0. Stationarity supplies a minimum, not flatness.
Likewise each constraint-preserving unitary R gives the exact inequality
\[
 \operatorname{Tr}\rho_0(R^\dagger H_J R-H_J)\ge0
\]
since the other terms commute with R. These are genuine ground-state
constraints on local kinetic expectations, but do not set M_0 to zero.

If liminf_L lambda_max M_0(L)>0, uniform local derivative bounds imply
lambda_max D_L(p_L)>c>0 for large L. That would refute the proposed p^4
*vacuum numerator* route. It would not alone refute every possible F/G
scaling or prove a spectral gap.
The needed finite-size bounds on M_0 remain unknown. The product-state
operator witness from the previous report cannot evaluate this ground cost.

## 6. Degeneracy: an exact counterexample to an averaged-rank shortcut

As an auxiliary logical example, take H=diag(0,0,1), P_0=diag(1,1,0) and
rho_0=P_0/2. The excited subspace has dimension one, spanned by e.
Choose imaginary Hermitian probes
\[
 B_1=i(|e\rangle\langle g_1|-|g_1\rangle\langle e|),\quad
 B_2=i(|e\rangle\langle g_2|-|g_2\rangle\langle e|).
\]
Then the ground-averaged matrices are G=F=I_2/2 and D=I_2=2F.
G has rank two, yet there is only one physical excited state.
For the pure ground vector (g_1+g_2)/sqrt2, G is instead the rank-one matrix
with every entry 1/2. Both created vectors are collinear.

The example refutes only a general inference from averaged rank to two
physical states. It is not an alternative N-type architecture or a
counterexample to N-type gaplessness.
For the desired two-dimensional trial subspace, one must either prove
nondegeneracy and use its pure ground vector, or control the Gram and energy
in an admitted pure ground vector (including momentum selection), or provide
a separate excited-range dimension argument. Purification of rho_0 alone
would count states in an enlarged Hilbert space and is insufficient.

## 7. Reproducible auxiliary checks

Command:

```sh
python3 -B scripts/verify_inverse_gravity_ground_sum_rules.py \
  --output reports/2026-10-08--ig-s2-true-ground-sum-rule-certificate.txt
```

Observed exit 0, SymPy 1.14.0, exact arithmetic.
The permanent code checks axial support degree, the polynomial identity and
its moment-kernel uniqueness, D=2F for the auxiliary real ground density,
the rank counterexample and the Hilbert-Schmidt identity.
It computes no N-type P_0, ground expectation or spectrum. Analytic proofs
in this report establish the implications; finite checks are auxiliary.
No earlier completed verifier was modified.

## 8. Outcome and one next obligation

The full ground condition supplied D=2F and reduced the numerator to five
local ground-moment matrices. It also identified a degeneracy issue that a
trace-only computation cannot bypass. These are exact reductions, not
certification of the missing correlations.

The single immediate obligation is to bound
\[
 M_0(L)_{\alpha\beta}
 =\frac{2}{d_0}\operatorname{Tr}
 P_0 B_\alpha(0)^\dagger (H_L-E_0)B_\beta(0)P_0
\]
in the true N-type ground space. The sufficient moment route needs
||M_0(L)||=O(L^-4); a proved positive lower limit would reject that route.
Success on this first cost still requires the remaining moment rates, a
ground-subtracted Gram estimate and physical tensor admission.

At present no controlled N-type ground representation or inequality
determines this quantity. A further step must add genuine ground-state
information with a concrete error bound; more tangent symbols or reference
states in ker H_U cannot supply it. Status remains OPEN, with no increase
of the spectral or gravity evidence level and no independent audit.
