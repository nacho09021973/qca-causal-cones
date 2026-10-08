# IG-S2/M3 — exact compact-probe commutator and remaining Gram obligation

Date: 2026-10-08

Branch: `research/inverse-gravity-design`.
Preregistered contract: `737e2a6`,
`theory/INVERSE_GRAVITY_SMA_TENSOR_PREFLIGHT_GATE.md`.
Permanent auxiliary code: `d402af8`,
`scripts/verify_inverse_gravity_sma_commutator.py`.
User authorization: "ok, primero el metodo tres".

Results, author-side:

- `COMMUTATOR_PREFLIGHT_ANALYTIC_PASS_AUTHOR_SIDE`.
- `STATE_INDEPENDENT_QUADRATIC_BOUND_FAIL` for the frozen pair.
- `SPECTRAL_UPPER_BOUND_CONDITIONAL_ON_GRAM`.
- `TRUE_GROUND_GRAM_OPEN / PHYSICAL_TENSOR_ADMISSION_OPEN`.

The general method is not closed as a tensor spectral result.

## 1. Source and conventions

Primary source: Gu–Wen,
[arXiv:0907.1203v3](https://arxiv.org/abs/0907.1203v3).
Read the local PDF's compact algebra/stencils on pp.13–14, the complete
N-type Hamiltonian on p.18, and staggered field dictionary/IR node on p.20.
Local PDF SHA256:
`3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
The paper's small-angle construction motivates the probes but is not assumed
as a controlled expansion at q=3.

All parameters, the two probes, and torus family are fixed by the contract.
Use q=3, N=L^3, even L>=4 and comparable positive couplings independent of L.
X shifts momenta by +1 and ZX=omega XZ. Scalars and rho are products or
functions of X; vectors and H_J are functions of Z.
The trace cosine is retained as a three-register Z product.

Writing \(s_i^{ab}=(X_i^{ab}-X_i^{ab\dagger})/(2i)\) and
\(\chi_i(p)=(-1)^{i_x+i_y+i_z}e^{-ip\cdot i}\), the frozen probes along p||z are
\[
 A_+(p)=\frac1{\sqrt{2N}}\sum_i\chi_i(p)(s_i^{xx}-s_i^{yy}),
 \qquad
 A_\times(p)=-\frac1{\sqrt{2N}}\sum_i\chi_i(p)s_i^{xy}.
\]
The xy register lies at \(i+(x+y)/2\); its additional Fourier phase is exactly
one along z and remains specified in the contract. The momentum transfer is
\((\pi,\pi,\pi)+p\), with translation convention fixed there.

The coefficient tensors are \(e^+=\operatorname{diag}(1,-1,0)/\sqrt2\) and
\(e^\times_{xy}=e^\times_{yx}=1/\sqrt2\).
The negative cross coefficient includes the source's a_xy=-(-1)^i theta_xy/2
and the two off-diagonal terms in the tensor contraction.
These are transverse/traceless coefficient tensors at p||z. Identifying
their compact probes as physical helicity +/-2 modes still requires control
of the state and constraints. A single X has nonzero vector-constraint charge,
so the probes are not exact constraint-preserving observables.

## 2. Exact microscopic double commutator

Define \({\cal D}_{\alpha\beta}(p)
=[A_\alpha^\dagger,[H_L,A_\beta]]\).
Since both probes are sums of commuting X operators,
\[
 [H_{U,S},A_\alpha]=[H_g,A_\alpha]=0.
\]
Thus the *full* double commutator reduces exactly to H_{U,V}+H_J:
\[
 {\cal D}_{\alpha\beta}
 =[A_\alpha^\dagger,[H_{U,V}+H_J,A_\beta]].
\]
This reduction does not discard an interaction or project H_N to the
constraint kernel.

For a diagonal Weyl word \(Z^d=\prod_r Z_r^{d_r}\), clock algebra gives
\[
 [X_r^{-\epsilon},[Z^d,X_s^\eta]]
 =(\omega^{\eta d_s}-1)(1-\omega^{-\epsilon d_r})
    X_s^\eta X_r^{-\epsilon} Z^d.
\]
Here epsilon,eta are +/-1; r=s is allowed. The first bracket follows from
\(Z^dX_s^\eta=\omega^{\eta d_s}X_s^\eta Z^d\); commuting X_r through Z^d gives
the second factor. This proves the identity at every volume.

Let \(A_\alpha=\sum_r a_{\alpha r}s_r\) with the frozen coefficients.
If \(H_{U,V}+H_J=h_0I+\sum_d h_dZ^d\), the exact expression is
\[
 {\cal D}_{\alpha\beta}
 =\sum_{d,r,s}h_d\bar a_{\alpha r}a_{\beta s}
   \sum_{\epsilon,\eta=\pm1}\frac{\epsilon\eta}{4}
   (\omega^{\eta d_s}-1)(1-\omega^{-\epsilon d_r})
   X_s^\eta X_r^{-\epsilon}Z^d.
\]
The coefficients h_d are fixed by the printed Hamiltonian:
each vector link has +/- words with coefficient \(-3\tilde U_1/2\);
each diagonal-register cosine has coefficient \(-3\tilde J/2\);
each face-register cosine has coefficient \(-3\tilde J\);
each vertex trace-cosine has coefficient \(+3\tilde J/4\).
Constant terms give zero. All phases and register coincidences are retained.
The independent local matrix checks verify this exact expression, including
the r=s sign.

## 3. Analytic bound uniform in momentum and volume

Take \(A(z)=z_+A_++z_\times A_\times\).
At any local diagonal term h, only its supported registers contribute:
\[
 [h,A(z)]=[h,A_{\operatorname{supp}h}(z)],\qquad
 \|[A(z)^\dagger,[h,A(z)]]\|
 \le4\|h\|\left(\sum_{r\in\operatorname{supp}h}|a_r(z)|\right)^2.
\]
The compact sine has norm <=1. Coefficients at xx, yy and xy have absolute
values \(|z_+|/\sqrt{2N}, |z_+|/\sqrt{2N},
|z_\times|/\sqrt{2N}\), respectively.

For q=3 the local norms are:

- diagonal-register kinetic term: \(9\tilde J/2\);
- face-register kinetic term: \(9\tilde J\);
- negative vertex trace term: \(9\tilde J/4\);
- vector-link penalty: \(9\tilde U_1/2\).

Summing the diagonal-register and vertex-trace terms gives respectively
\(18\tilde J|z_+|^2\) and \(18\tilde J|z_+|^2\).
Face terms give \(18\tilde J|z_\times|^2\).
Each vector-link stencil has six registers. Cauchy–Schwarz gives
\((\sum_{\text{link}}|a_r|)^2\le6\sum_{\text{link}}|a_r|^2\).
A diagonal register meets two links and a face register meets four.
Summing all links therefore gives
\[
 \sum_{\text{links}}\sum_{r\in\text{link}}|a_r(z)|^2
 =2(|z_+|^2+|z_\times|^2).
\]
The total vector contribution is at most
\(4(9\tilde U_1/2)6(2)\|z\|^2=216\tilde U_1\|z\|^2\).
Consequently
\[
 \left\|\sum_{\alpha,\beta}\bar z_\alpha
 {\cal D}_{\alpha\beta}(p)z_\beta\right\|
 \le C_*\|z\|^2,\qquad C_*=216\tilde U_1+36\tilde J,
\]
for all the frozen tori and axial momenta. C_* is deliberately conservative.
It depends only on the fixed microscopic couplings.
All N factors cancel by the 1/sqrt(N) probe normalization.
No ground-state assumption was needed for this operator-norm bound.

## 4. Exact obstruction to a state-independent O(p^2) bound

Use the product vector \(|0_L\rangle\) with every momentum zero solely as an
operator witness. It is not the ground state reference used in the
variational argument.
The diagonal Hamiltonian H_{U,V}+H_J has energy zero on this vector.
A shift of one diagonal register has H_J energy \(9\tilde J/4\) and changes
two vector links, each of energy \(9\tilde U_1/2\).
A shift of one xy register has H_J energy \(9\tilde J\) and changes four links.
Positive and negative shifts have equal costs at q=3.
The normalized sine creates them with squared amplitudes 1/4 each.

Different single-register shifts are distinct orthogonal basis vectors.
Their Fourier phases cancel in each diagonal expectation, and mixed +/cross
matrix elements vanish. The general double-commutator formula and,
independently, these shifted-state costs give
\[
 \langle0_L|{\cal D}(p)|0_L\rangle=
 \begin{pmatrix}
 9\tilde U_1+\frac94\tilde J&0\\
 0&9\tilde U_1+\frac92\tilde J
 \end{pmatrix}.
\]
This holds at every admissible axial p and frozen volume.
For example, the + entry gives
\(\|{\cal D}_{++}(p_L)\|\ge9\tilde U_1+9\tilde J/4>0\).
Since p_L=2pi/L ->0, no L-independent bound
\(\|{\cal D}_{++}(p_L)\|\le C|p_L|^2\) can hold.

Verdict: `STATE_INDEPENDENT_QUADRATIC_BOUND_FAIL`.
This refutes the stronger operator bound only. It provides no lower bound on
the true-ground-state D and does not refute the spectral ansatz or N-type.

## 5. Conditional excitation bound and remaining denominator

Let Omega be a true ground vector, P_0 the complete ground projector and
\(K=H_L-E_0\ge0\). Define
\[
 b_\alpha=(I-P_0)A_\alpha\Omega,\quad
 G_{\alpha\beta}=\langle b_\alpha,b_\beta\rangle,\quad
 F_{\alpha\beta}=\langle b_\alpha,Kb_\beta\rangle.
\]
Then \(F_{\alpha\beta}=\langle A_\alpha^\dagger[H_L,A_\beta]\rangle_\Omega\).
For any coefficients z,
\[
 z^\dagger Dz
 =\langle A(z)^\dagger K A(z)\rangle_\Omega
  +\langle A(z)K A(z)^\dagger\rangle_\Omega
 \ge z^\dagger Fz\ge0.
\]
Thus the proved operator bound implies
\[
 0\preceq F\preceq D\preceq C_*I_2
\]
in every true ground vector.
If for the frozen pair one can additionally prove
\[
 G_L(p_L)\succeq \frac{g_*}{|p_L|}I_2,\qquad g_*>0
\]
uniformly in L in the declared ground-state selection, then
\[
 F_L\preceq(C_*/g_*)|p_L|G_L,\qquad
 \sup_{\psi\in\operatorname{span}\{b_+,b_\times\},\|\psi\|=1}
 \langle\psi,K\psi\rangle\le(C_*/g_*)\,2\pi/L.
\]
G>0 supplies dimension two; P_0 supplies complete ground-space orthogonality.
E_0 cancels exactly. This proves the conditional variational implication.
It does not supply or verify the hypothesis.

The missing Gram matrix is
\[
 G_{\alpha\beta}
 =\langle A_\alpha^\dagger A_\beta\rangle_\Omega
  -\langle A_\alpha^\dagger P_0 A_\beta\rangle_\Omega.
\]
The operator product is a staggered two-point structure factor, with the
full ground-space contribution removed. Its lower bound must hold in the
minimum-eigenvalue direction of the matrix, not just on its diagonal.
Translation symmetry alone proves neither the infrared divergence nor the
absence of ground weight at the target momentum. A constraint-kernel or
tracial expectation cannot substitute for the true ground expectation.

Verdict: `SPECTRAL_UPPER_BOUND_CONDITIONAL_ON_GRAM / TRUE_GROUND_GRAM_OPEN`.
The old suggested D=O(p^2), G>=const*|p| route is not required for these angle
probes; the frozen alternative D=O(1), G>=const/|p| is sufficient.

## 6. Reproducible local verification

The script was added permanently and committed before its first execution.
Command from repository root:

```sh
python3 -B scripts/verify_inverse_gravity_sma_commutator.py \
  --output reports/2026-10-08--ig-s2-method-three-certificate.txt
```

Observed: exit 0, SymPy 1.14.0, exact arithmetic, no tolerances.
The retained record contains 120 nested-Weyl/sine checks plus the clock,
27-state local H_J, vector incidences, witness coefficients, norm constants
and coefficient-tensor checks. It reports `LOCAL_SMA_COMMUTATOR_CONTROLS_PASS`.
The largest matrix is 27x27, for one vertex's three diagonal registers.
No matrix of dimension 3^(6L^3) is built.
The finite checks do not prove the all-L result by extrapolation: Sections 2–4
give the analytic identities and support counts that prove it.

## 7. Attempt to control the Gram matrix from exact symmetries

There are discrete symmetries that can be derived from the printed operators,
without assuming the continuum gauge transformations. On the frozen even
torus, define one operator per register species:
\[
 C_{ab}=\prod_{i\in\Lambda_L}(Z_i^{ab})^{(-1)^{i_x+i_y+i_z}}.
\]
Each has order 3. They commute with H_{U,V} and H_J because those terms are
functions of Z. For H_{U,S}, a diagonal scalar stencil has signed sum
4-4=0; an off-diagonal scalar stencil has four anchors with alternating sum
\(-(1-1-1+1)=0\). Thus every S_i commutes with every C_ab.
For H_g, inspect the three printed rho examples on p.18:
the zx and xy pairs in rho_x^x have neighbouring anchors, the yz pair in
rho_y^x has anchors i and i-y, and its yy pair has anchors i and i+z.
The zz and yz pairs in rho_z^x have the same cancellation. Every species
therefore has signed exponent sum zero; cyclic permutation proves the other
six rho stencils. Hence
\[
 [C_{ab},H_L]=0
\]
exactly, with an abelian \((\mathbb Z_3)^6\) symmetry. This is finite order and
does not generate an exact continuous conserved charge or a Goldstone bound.
Translation by a primitive axis conjugates C_ab to its inverse, so an
arbitrary charge eigenvector cannot also be assumed to have definite
translation momentum. A ground state in a nonneutral charge sector would
have symmetry-related partners; the full P_0 remains essential.

In a state invariant under all C_ab, \(\langle X_i^{ab}\rangle=0\).
At q=3 this implies
\(\langle(s_i^{ab})^2\rangle=1/2\), since
\(s^2=(2I-X-X^\dagger)/4\).
For the normalized Fourier transform of a single species, the exact discrete
Parseval sum rule is
\[
 \frac1N\sum_{p\in(2\pi/L)\mathbb Z_L^3}
 \langle A_{ab}(p)^\dagger A_{ab}(p)\rangle
 =\frac1N\sum_i\langle(s_i^{ab})^2\rangle=\frac12,
\]
where this single-species A_ab has normalization 1/sqrt(N).
It controls the average over all momenta, not a lower bound at p_L.
The ground projector subtraction may further reduce the particular Gram.
No proof that the true ground space is neutral is supplied.

As a second formulation of the missing information, the translation-invariant
product vector |0_L> is neutral under every C_ab and has exactly
\[
 \langle0_L|A_\alpha(p)^\dagger A_\beta(p)|0_L\rangle
 =\operatorname{diag}(1/2,1/4)_{\alpha\beta}
\]
at every momentum: distinct single-register shifts are orthogonal.
It satisfies the discrete symmetry and local-variance identities but has no
1/|p| structure-factor divergence. This is a counterexample to deriving the
desired Gram lower bound from those symmetry/variance premises alone.
It is not a counterexample in the class of true N-type ground states:
the eigenstate assumption is not met. To get the lower bound one needs new
information that uses the ground-state condition and controls long-distance
correlations, rather than merely imposing the exact discrete symmetries.

## 8. Single next obligation and claim ceiling

The immediate remaining mathematical obligation for this pair is to prove or
refute the true-ground-state, ground-space-subtracted matrix lower bound
\[
 \lambda_{\min}G_L((0,0,2\pi/L))\ge g_* L/(2\pi)
\]
with g_*>0 independent of even L>=4 and with a fixed ground-state selection.
A proved uniform upper bound on that eigenvalue would refute this sufficient
route; it would not by itself prove a gap or reject every possible quotient
scaling. If no correlation control is available, the result remains OPEN.

The physical TT admission is a separate unresolved condition: these probes
have a TT small-angle motivation but carry microscopic constraint charge.
Their coupling to defects cannot be silently excluded.
Even a future variational PASS would establish only the stated upper bound,
not a linear lower dispersion, uniqueness of two soft modes, rest-sector gap,
QCA energy–tick bridge, matter coupling or nonlinear Einstein dynamics.
No independent review was requested or performed.

## 9. Author assessment of the user-supplied Grok recommendation

During this preflight the user pasted a Grok recommendation based on the
five-method formulations. The pasted text explicitly says the report was
not accessible and the demonstrations were not audited. Its model/run identity,
complete input and provider artifacts are not available here. It is retained
as user-supplied discussion, not as independent closure of this report.

Accept the recommendation to prioritize M3 as an upper-bound method and to
keep rank-two Gram control, physical tensor admission and later rest-sector
separation as distinct obligations. Its concern about extensive subtraction
errors is precisely why the ground-state identity is useful.

Reject the final proposed shortcut: an explicit state in the joint H_U kernel
does not substitute for a true H_N ground state. Its Rayleigh quotient gives
\(\langle H_N\rangle_\psi\); the needed quantity is
\(\langle H_N\rangle_\psi-E_0(H_N)\).
The commutator equality relies on \(H_N\Omega=E_0\Omega\), so using a different
reference introduces an uncontrolled residual term. With \(\mu=\langle H\rangle_\phi\),
\[
 \langle A\phi,H A\phi\rangle-\mu\langle A\phi,A\phi\rangle
 =\langle\phi,A^\dagger[H,A]\phi\rangle
  +\langle\phi,A^\dagger A(H-\mu)\phi\rangle.
\]
Subtracting E_0 instead of mu additionally changes the left-hand side by
\((\mu-E_0)\|A\phi\|^2\). Neither error is controlled by belonging to the H_U
kernel. Also, an exact microscopic helicity +/-2 condition cannot simply be
assigned to two classical TT components.

A limiting-case check makes the absolute-energy issue explicit:
H=diag(-1,0) and the second basis vector have Rayleigh quotient zero for every
L but excitation energy one. Energy shifts H->H+c_L I change absolute
Rayleigh values while leaving the required excitation quotient unchanged.
Thus no absolute Rayleigh calculation alone implements M3's cancellation.

Several broader claims in the pasted recommendation require qualification:

- A positive local certificate can be exactly sharp; a mandatory error of
  order L or L^2 is not a general theorem. No sharp N-type certificate exists
  in the present evidence.
- Variance is not always extensive (an eigenstate has variance zero).
  Temple's missing separator is the relevant unproved hypothesis here.
- The dimension-only thermal bracket needs beta of order L^4 for error O(1/L);
  beta much larger is required for the bracket error to be o(1/L).
- Schur elimination needs positivity of the excluded block relative to b,
  not necessarily the later rest-sector gap or a gap above the full ground
  space. Its block positivity and self-energy error are still unproved.
- Only M3 directly cancels E_0 among these five formulations; that does not
  prove that the other methods cannot yield controlled thermodynamic bounds.

The immediate obligation remains the frozen probes' true-ground Gram bound,
with physical tensor admission still OPEN. The pasted discussion does not
authorize replacing the ground state, changing q or modifying the couplings.
