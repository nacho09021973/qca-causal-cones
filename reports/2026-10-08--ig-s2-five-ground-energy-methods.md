# IG-S2 — five methods for ground-energy control or cancellation

Date: 2026-10-08

Base: `edf54ffa4ea23cafa2e60a3275e56201539e970a`,
branch `research/inverse-gravity-design`.

Authorization: user request to use five references or formulate five methods.
This report takes the second option. It formulates five methods for the same
N-type Hamiltonian; it does not execute five searches or open five architectures.

Evidence: the finite-dimensional implications below are proved here,
author-side (`ANALYTIC_PASS`). Their quantitative N-type hypotheses are
`OPEN`, so each proposed application is `CONDITIONAL`. No independent review,
numerical certificate, or tensor spectral PASS is claimed.

## 1. Corrected starting point

Primary source: Gu–Wen, arXiv:0907.1203v3,
[versioned source](https://arxiv.org/abs/0907.1203v3).
Local PDF `biblioteca/arXiv-0907.1203.pdf`, SHA256
`3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
The v3 identifier was checked on its first page. The compact algebra and
scalar stencil were reread on pp.13–14; the N-type Hamiltonian on p.18 was
checked both by text extraction and visual inspection of the rendered page.
The source supplies the microscopic model, not proofs of the five methods'
N-type admission hypotheses.

Two errors in the preceding session need correction before continuation:

1. The report at `edf54ff` replaced
   \(-\frac{n_G\tilde J}{2}\sum_i
   [1-\cos(\frac{2\pi}{n_G}\sum_aL^{aa}(i))]\)
   by a sum of independent diagonal-register terms. That is not the printed
   compact Hamiltonian. The refutation report now uses the full trace cosine.
   For the frozen q=3 candidate, the corrected energies of the two orbit
   configurations are 0 and \(162\tilde J\), so the author-side non-eigenstate
   conclusion survives. See the repaired report for both derivations.
2. A separate numerical value of E_0 is needed for an absolute-energy
   subtraction certificate, but not for every variational method. Exact
   ground-state commutator identities can cancel E_0. They require
   ground-state correlation bounds, not necessarily an explicit wavefunction.
   The earlier blanket prerequisite is withdrawn in the initial audit.

No previously rejected candidate is reinstated. These corrections preserve
the failed versions in Git and do not constitute independent certification.

## 2. Common target and precision

Let \(H_L=H_N(L)\) act on the full compact Hilbert space, and let
\(P_{0,L}\) denote its complete ground-space projector. Write
\(K_L=H_L-E_0(L)I\ge0\) and \(\kappa_L=2\pi/L\).
The frozen candidate had q=3, six registers per cell and all L>=3.
The methods below keep q=3; they do not import a large-q semiclassical result.
The positive couplings \(\tilde U_1,\tilde U_2,\tilde J,\tilde g\) are fixed
independently of L and comparable. Constants may depend on these fixed
couplings; no large-U limit or parameter fitting is allowed.

For a later momentum construction around \(k_*=(\pi,\pi,\pi)\) (source p.20),
even L>=4 admits \(k_*\) exactly; odd-L handling must be specified separately.
This compatibility note does not change the all-L>=3 refutation.
The momentum transfer of an operator is distinct from the total momentum of
the excited vector if the chosen ground vector has nonzero momentum.

The target is a two-dimensional \(T_L\perp\operatorname{ran}P_{0,L}\) with
\[
 \sup_{\psi\in T_L,\|\psi\|=1}\langle\psi,K_L\psi\rangle
 \le C\kappa_L.
\]
If an absolute variational estimate \(r_L\) is used, a certified \(b_L\le E_0\)
must satisfy \(r_L-b_L\le C\kappa_L\).
An error \(\delta_L\) per cell contributes \(L^3\delta_L\), hence this route
needs \(\delta_L=O(L^{-4})\), including finite-size corrections.
An exact thermodynamic energy density alone is insufficient.

All five methods additionally require two independent vectors and a justified
microscopic-to-IR tensor identification. Projecting two classical components
to TT is not that justification. Nonzero momentum alone does not remove the
whole ground space if other ground vectors carry that momentum.

## 3. Method 1 — local positive certificates and overlapping clusters

**Object.** Decompose the *same* full Hamiltonian into self-adjoint cluster
operators with exact covering weights, \(H_L=\sum_B K_B\). Prove
\(K_B\ge e_B I\), giving
\[
 b_L=\sum_B e_B\le E_0(L).
\]
Alternatively, seek the stronger explicit certificate
\[
 H_L-b_LI=\sum_\nu B_\nu^\dagger B_\nu+R_L,\qquad R_L\ge0.
\]
The B operators are finite combinations of compact Weyl words; the equality
must hold in the exact clock algebra, including phases and torus identifications.
Reduced-density-matrix relaxations may help propose bounds, but a retained
lower bound needs a verified feasible certificate, not a numerical optimum.
Cluster and sum-of-squares implementations are grouped as one method.

**Proof.** Taking an arbitrary normalized state's expectation of each positive
term gives \(\langle H_L\rangle\ge b_L\). Taking the infimum proves the bound;
subtracting it from r_L proves the excitation estimate if the target error holds.
Overlapping clusters require no simultaneous minimizing state for this lower
bound; they do require that every original term has the correct total weight.

**Admission test.** Exhibit the exact positive certificate and prove
\(r_L-b_L=O(L^{-1})\) uniformly, including boundary/overlap accounting.
No exact ground wavefunction is required.

**Concrete failure criterion.** A fixed-cluster certificate with a proved
nonvanishing energy-density discrepancy fails the precision requirement.
Dropping boundary bonds using norm bounds typically incurs a total estimate
of order \(L^3/\ell\) for cluster width \(\ell\); that estimate alone cannot
yield O(1/L) with \(\ell\le L\). This is a limitation of that bound, not a
theorem that all overlapping certificates fail.

**Cross-check.** For a commuting frustration-free parent the certificate can
give b=E_0 exactly; that does not imply it does so for this noncommuting H_N.
N-type certificate and required precision: **OPEN**.

## 4. Method 2 — residual/variance with a certified spectral separator

**Object.** For a normalized correlated trial vector \(\phi_L\), define
\[
 \mu_L=\langle H_L\rangle_{\phi_L},\qquad
 v_L=\|(H_L-\mu_L)\phi_L\|^2.
\]
Supply an independently proved \(\beta_L>\mu_L\) such that *all* spectrum
strictly above the complete ground eigenspace lies in \([\beta_L,\infty)\).
Then the Temple-type bound is
\[
 \mu_L-\frac{v_L}{\beta_L-\mu_L}\le E_0(L)\le\mu_L.
\]

**Proof.** The spectral assumption implies
\((H_L-E_0)(H_L-\beta_L)\ge0\): it vanishes on the ground space and is
nonnegative on its orthogonal complement. Its expectation is
\[
 v_L-(\mu_L-E_0)(\beta_L-\mu_L)\ge0,
\]
which gives the bound. A two-level spectrum \(\{E_0,\beta_L\}\) saturates this
inequality for any mixture with \(\mu_L<\beta_L\), checking its sign.

**Admission test.** Prove both the separator and
\[
 r_L-\mu_L+\frac{v_L}{\beta_L-\mu_L}\le C\kappa_L.
\]
If the certified denominator is of order 1/L, a variance O(L^-2) is needed
for an O(1/L) correction. A small *variance density* is insufficient.
Degenerate ground states are allowed; \(\beta_L\) is above their common
energy, not above an arbitrarily selected one-dimensional reference.

**Concrete failure criterion.** Without \(\beta_L>\mu_L\) the formula is
inapplicable. An excited exact eigenvector has v=0, so residual zero alone
cannot certify ground energy. A separator in one symmetry sector also needs
proof that no other sector contains a lower state.

**Assessment.** This route risks assuming the spectral information we seek.
No separator for H_N is supplied here. Application: **CONDITIONAL / OPEN**.

## 5. Method 3 — a two-probe ground-state commutator bound

**Object.** Let \(\Omega_L\) be a true normalized ground eigenvector, initially
unspecified, and choose two explicitly defined bounded compact operators
\(A_1(k),A_2(k)\) of the same momentum transfer. Ground-space existence is
automatic in finite dimension; useful estimates in that state are not.
For a momentum-sector claim choose \(\Omega_L\) to be a simultaneous
translation eigenvector, which exists because translations commute with H_L
and with each other. Its momentum need not be zero. Fix a selection rule or
prove the estimates uniformly in the admitted ground vectors.
Define
\[
 b_\alpha=(I-P_{0,L})A_\alpha\Omega_L,\quad
 G_{\alpha\beta}=\langle b_\alpha,b_\beta\rangle,\quad
 F_{\alpha\beta}=\langle b_\alpha,K_L b_\beta\rangle.
\]
Because \(K_LP_{0,L}=0\),
\[
 F_{\alpha\beta}
 =\langle\Omega_L,A_\alpha^\dagger[H_L,A_\beta]\Omega_L\rangle.
\]
For \(G>0\), the maximum excitation Rayleigh quotient in
\(T_L=\operatorname{span}\{b_1,b_2\}\) is exactly
\[
 \lambda_{\max}(G^{-1/2}FG^{-1/2}).
\]
Thus \(F\preceq C\kappa_L G\) proves the requested upper bound without
separately computing E_0 or writing \(\Omega_L\) in the microscopic basis.

**Proof.** For coefficients z, \(b(z)=\sum_\alpha z_\alpha b_\alpha\)
has norm squared \(z^\dagger Gz\) and excitation energy numerator
\(z^\dagger Fz\). The maximum of their quotient gives the displayed eigenvalue.
G>0 ensures dimension two and projection ensures full ground orthogonality.
The identity for F follows directly from \(H_L\Omega_L=E_0\Omega_L\).

**Double-commutator implementation.** Define
\[
 D_{\alpha\beta}
 =\langle[A_\alpha^\dagger,[H_L,A_\beta]]\rangle_{\Omega_L}.
\]
For every complex z,
\[
 z^\dagger Dz
 =\langle A(z)^\dagger K_L A(z)\rangle
  +\langle A(z)K_L A(z)^\dagger\rangle
 \ge z^\dagger Fz.
\]
Hence D is positive and \(F\preceq D\). No factor 1/2 is used without a
separate equality of the forward and reverse spectral weights. A Hermitian
single A gives D=2F, which checks the convention.

**Admission test.** One sufficient, but not necessary, scaling is
\[
 G_L\succeq s_0\kappa_L I_2,\qquad
 D_L\preceq f_0\kappa_L^2 I_2,\qquad s_0,f_0>0
\]
uniformly at the specified IR momenta. It yields C=f_0/s_0.
Other numerator/denominator scalings are allowed if the ratio is bounded.
The Fourier normalization and microscopic probes must be frozen before testing.
Two separate small diagonal quotients do not control arbitrary linear
combinations; the matrix inequality does.

**Concrete failure criterion.** G rank below two refutes this pair of probes.
A positive constant lower bound on the generalized quotient as L grows
refutes the desired scaling for these probes. Failure to bound correlations
leaves the method OPEN. Neither failure rejects N-type.

**N-type-specific missing hypotheses.** Locality alone gives no soft
double-commutator cancellation, and an emergent gauge description gives no
exact Ward identity. A connected correlator that subtracts only the chosen
ground vector is insufficient with ground degeneracy: one must subtract
\(\langle\Omega,A_\alpha^\dagger P_0 A_\beta\Omega\rangle\).
A nonzero-momentum shortcut requires absence of ground states at the target
momentum. Rotational/TT content and spectral weight must come from the
microscopic operators and controlled state estimates.

**Assessment.** Preferred first preflight: it eliminates the unnecessary
absolute-energy subtraction. Correlation estimates and tensor identification
remain **OPEN**; no N-type spectral claim follows from this general lemma.

## 6. Method 4 — certified low-temperature partition-function bounds

**Object.** Let \(Z_L(\beta)=\operatorname{Tr}e^{-\beta H_L}\), over the full
Hilbert space of dimension \(d_L=3^{6L^3}\), and
\(\mathcal F_L=-\beta^{-1}\log Z_L\). For \(\beta>0\),
\[
 \mathcal F_L\le E_0(L)
 \le\mathcal F_L+\frac{\log d_L}{\beta}.
\]

**Proof.** The ground eigenvalue contributes at least \(e^{-\beta E_0}\),
while each of d_L eigenvalues contributes at most that amount:
\(e^{-\beta E_0}\le Z_L\le d_Le^{-\beta E_0}\). Taking logarithms proves
both inequalities. Ground degeneracy causes no problem.

If a rigorously computed interval satisfies
\(|\log Z_L-\ell_L|\le\epsilon_L\), then
\[
 b_L=-\frac{\ell_L+\epsilon_L}{\beta},\qquad
 u_L=-\frac{\ell_L-\epsilon_L}{\beta}+\frac{\log d_L}{\beta}
\]
bracket E_0, with width
\((6L^3\log3+2\epsilon_L)/\beta\).

**Admission test.** Choose the analysis parameter \(\beta_L\), which does not
change H_N, so that this width is O(1/L), and obtain a certified trace interval.
The generic dimension-only estimate needs \(\beta_L\) of at least order L^4;
a proved low-energy entropy bound could improve it.
Still prove \(r_L-b_L\le C\kappa_L\) for the tensor trial subspace.

**Concrete failure criterion.** An approximate tensor-network contraction,
imaginary-time truncation, or sampled partition function without a rigorous
log-error interval is insufficient. No efficiency or favorable sign structure
of the compact N-type Hamiltonian is assumed.

**Cross-check.** H=cI saturates the entropy width:
\(\mathcal F=c-\log d/\beta\). A unique ground with fixed positive finite-volume
gap approaches \(\mathcal F\to E_0\) as \(\beta\to\infty\), but this supplies
no uniform L convergence rate beyond the displayed bound.
Application: **CONDITIONAL / OPEN**.

## 7. Method 5 — exact block elimination with a Schur complement

**Object.** Choose an orthogonal reference-space projector P, Q=I-P, and write
\[
 H_L=\begin{pmatrix}A&B^\dagger\\B&C\end{pmatrix},
 \quad A=PH_LP,\ B=QH_LP,\ C=QH_LQ.
\]
For a proposed b with \(C-bQ\ge\delta_L Q>0\), define on ran P
\[
 S_b=A-bP-B^\dagger(C-bQ)^{-1}B.
\]
Then
\[
 H_L-bI\ge0 \quad\Longleftrightarrow\quad S_b\ge0.
\]

**Proof.** For p in ran P and q in ran Q, complete the square:
\[
 \langle p+q,(H_L-b)(p+q)\rangle
 =\langle p,S_b p\rangle+
 \left\langle q+(C-b)^{-1}Bp,\,
 (C-b)\big[q+(C-b)^{-1}Bp\big]\right\rangle.
\]
Both implications follow, taking \(q=-(C-b)^{-1}Bp\) for necessity.
This is exact, with no expansion in J/U or g/U.

**Admission test.** Prove the block separator and a lower bound on S_b, then
establish \(r_L-b_L=O(1/L)\). P may contain many low-energy states; the
separator concerns the excluded block and need not assume a global gap.
If the old constraint projector is used, the H_U defect gap by itself does
not prove \(C-b>0\) for the full comparable-coupling Hamiltonian.

**Concrete failure criterion.** If \(C-b\) is not strictly positive, this
version of the certificate is unavailable. The crude correction bound
\(\|B^\dagger(C-b)^{-1}B\|\le\|B\|^2/\delta_L\) may be extensive or worse;
such an uncontrolled correction does not certify O(1/L).
Cancellation/locality estimates of the full self-energy would be required.

**Cross-check.** B=0 reduces to separate block positivity; if A and C are
scalars, the condition is the familiar exact two-by-two determinant test.
No assertion is made here about \(QH_gP\) from an isolated Weyl witness.
Application: **CONDITIONAL / OPEN**.

## 8. Decision and one next obligation

Continuation: the user selected method 3. Its preregistered contract and
author-side result are in
`theory/INVERSE_GRAVITY_SMA_TENSOR_PREFLIGHT_GATE.md` and
`reports/2026-10-08--ig-s2-method-three-commutator.md`.
The frozen angle-probe pair admits D=O(1); its missing sufficient condition
is G>=const/|p| in the true ground state. The historical recommendation below
is superseded only by that bounded preflight, not a spectral PASS.

The five formulations are: positive local certificates, residual bounds,
matrix commutator bounds, thermal trace bounds, and block elimination.
Methods 1, 2, 4 and 5 produce lower bounds on E_0; method 3 cancels E_0.
None currently has its full N-type hypotheses proved.

Recommend method 3 for the next bounded preflight. The single obligation is
to specify one pair of bounded microscopic tensor probes (including compact
Weyl words, offsets, momentum convention, normalization and tensor criterion)
and prove or refute its matrix estimate
\[
 G_L>0,\qquad F_L\preceq C(2\pi/L)G_L
\]
in a true ground state of the full H_N, with all ground-space weight removed.
The first computation, if later chartered, should derive the exact
double commutator for that frozen pair; the denominator must be controlled
analytically in the true ground state. No Ward identity or scalar-constraint
reference may be substituted for that control. This report does not yet
freeze such a microscopic probe pair or authorize a scan.

Even success gives only two low variational energies. It does not prove
exclusive helicity +/-2, a linear lower dispersion bound, or separation from
other excitations: an O(k^2) band also satisfies an O(|k|) upper bound.
The later separation obligation, QCA energy–tick bridge, and nonlinear
Einstein dynamics remain separate and OPEN.

No scientific script or diagonalization was executed. The source-rendering
command produces only a PDF inspection image; all retained derivations are
contained in this report and the repaired refutation.
