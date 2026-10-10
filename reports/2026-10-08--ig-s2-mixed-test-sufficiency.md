# IG-S2 — mixed stationarity is insufficient; coherent ground costs matter

Date: 2026-10-08. Branch: `research/inverse-gravity-design`.
Preregistration `cb25f19`; permanent auxiliary code `b6ed04b` before execution.
Evidence: author-side analytic proof and exact auxiliary controls, no review.

Verdicts: `ANGLE_TESTS_PLUS_MIXED_STATIONARITY_INSUFFICIENT_AUTHOR_SIDE`;
`COHERENT_MIXED_COST_EXCLUDES_TAU_AUTHOR_SIDE`; `TENSOR_SPECTRAL_GATE_OPEN`.

## 1. What is being tested

The user instructed checking whether the added mixed test yields a tensor
numerator bound. We keep the full q=3 N-type Hamiltonian and fixed probes,
unchanged positive comparable couplings, and even periodic L>=4.
The precise necessary conditions audited here are:

- a positive normalized density with translation and reality symmetry;
- stationarity for Hermitian polynomials in the commuting curvature angle
  words, and nonnegative ground costs for all such polynomials;
- stationarity for each translated mixed Y_i already fixed (and its cyclic
  central-species variants).

This is a specified relaxation, NOT the entire common commutant of H_U,H_g
and NOT every ground inequality or all local stationarity tests. The result
does not claim insufficiency of those larger, untested families.

Primary source inspected this session: `biblioteca/arXiv-0907.1203.pdf`,
Gu-Wen v3 p.14 Eq.(39), p.18 the full N-type H_J,H_g. Existing scalar and
curvature stencil helpers are reused read-only.

## 2. An explicit density passing the specified conditions

Consider the density

\[
 \tau_L=\bigotimes_{i,a=xx,yy,zz} I_{i,a}/3
 \ \otimes\bigotimes_{i,ab=xy,yz,zx}|0\rangle_{i,ab}\langle0|.
\]

It is real, translation invariant, positive and normalized. It is only a
false-positive witness for necessary conditions, never a trial vacuum or a
true-ground assumption. It need not lie in the constraint kernel; the full
N-type ground space is not known to lie there either.

Write any angle polynomial A as a finite sum of distinct pure-shift words
X^w, combining repetitions modulo 3 and the torus. For the curvature
algebra, [H_U,A]=[H_g,A]=0, so [H_N,A]=[H_J,A]. In tau the cross terms in
Tr(tau A^dagger[H_J,A]) vanish unless the full shift words agree: tau is
diagonal in momenta and the intervening H_J is diagonal too.
For an individual shift w, the diagonal-register contribution averages to
zero, since those registers are uniformly distributed and any shift is a
permutation of their configurations. The off-diagonal registers start at
zero and each nonzero shift costs 9 J. Thus

\[
 \operatorname{Tr}\tau A^\dagger[H_N,A]
 =9\widetilde J\sum_w |a_w|^2 n_{\rm face}(w)\ge0.
\]

This proves all the specified angle-polynomial ground inequalities, not
just individual unitary ones. Their Hermitian stationarity tests vanish
because [tau,H_J]=0.

For the mixed Y_i=i(P_i S_i^dagger-S_i P_i), diagonal H_J and vector
penalties have zero commutator expectation in any momentum-diagonal density.
Only the matching scalar word can cancel the shift of S_i. Its contribution
is 3 U2 Tr(tau(P_1-P_0))=0 because each central diagonal momentum is uniform.
No H_g word cancels S_i, which has all three diagonal species whereas
each H_g word has at most two. All translated and cyclic mixed stationarity
tests therefore vanish exactly. This argument uses the unchanged full H_N.

## 3. Its tensor numerator is constant, not quartic

The diagonal kinetic terms average out in tau. R_xx and R_yy each shift
four face registers, costing 36 J. R_xy shifts eleven, costing 99 J.
The signed translated curvature words are distinct on even L>=4 by their
species/support and central/end-point coefficient patterns. In a diagonal
trace a nonzero net shift has zero expectation, so only matching words
contribute to the double commutator. The sine and probe normalizations give

\[
 D_R^{\tau}(p)=\widetilde J\begin{pmatrix}36&0\\0&99/2\end{pmatrix}
\]

for every allowed axial p, including p_L. This uses the actual double
commutator of H_N, not an excitation energy measured from tau.
Consequently the listed conditions, even after incorporating mixed
stationarity, cannot imply D_R(p_L)=O(p_L^4). A positive certificate relying
only on these conditions must also hold in tau and cannot yield a vanishing
upper bound. This refutes their sufficiency, not the true-ground estimate,
any possible spectral quotient, or N-type gaplessness.

## 4. A coherent mixed ground inequality excludes this false positive

For any actual complete-ground-space density rho and A_1=P_i, A_2=T_i=S_iP_i,
define the Hermitian ground-cost matrix

\[
 \mathcal M_{ab}(\rho)=\tfrac12\operatorname{Tr}\rho
 \{A_a^\dagger[H_N,A_b]+[A_a^\dagger,H_N]A_b\}.
\]

Using H_N rho=E0 rho gives
M_ab=Tr(rho A_a^dagger(H_N-E0)A_b), hence M(rho)>=0. This statement holds
for the complete degenerate ground space as well. The operator form on the
left does not require knowing E0. It implies
|M_12|^2<=M_11 M_22 with nonnegative diagonal costs.

In the explicit tau density the exact matrix is

\[
 \mathcal M(\tau)=\begin{pmatrix}
 0&-\widetilde U_2/2\\
 -\widetilde U_2/2&75\widetilde J/2
 \end{pmatrix}.
\]

Here M_11=0 because [tau,P_i]=0: cyclicity cancels its two costs for any H.
For M_12, P_i S_i P_i=0. In P_i H_N S_i P_i only the scalar S_i^dagger
term cancels the full shift, leaving -(3 U2/2)P_i. Since Tr(tau P_i)=1/3,
the matrix entry is -U2/2; the adjoint entry is the same. The diagonal
Hamiltonian terms and H_g cannot provide that transition.

For M_22 all off-diagonal words in H_U,H_g remain nontrivial shifts and
their diagonal traces vanish. Only H_J remains. Conditioning on central
Lxx=0 has probability 1/3. S_i raises the central xx momentum by one,
contributing 3 J/2 after this probability; yy,zz and the trace term retain
uniform averages. Every other diagonal vertex remains uniformly distributed
and contributes zero average change. Twelve shifted face registers each
cost 9 J, multiplied by 1/3, giving 36 J. Total: 75 J/2.

Therefore det M(tau)=-U2^2/4<0. More explicitly the fixed local coherent
variation

\[
 A=P_i+t S_iP_i,\qquad t=\frac{\widetilde U_2}{75\widetilde J}
\]

has symmetrized cost

\[
 \operatorname{Tr}\tau T_A
 =-\widetilde U_2 t+\tfrac{75}{2}\widetilde J t^2
 =-\frac{\widetilde U_2^2}{150\widetilde J}<0.
\]

The couplings have not changed: only the coefficient of a necessary test
depends on their fixed values. This excludes tau by a genuine ground-state
inequality, stronger than the mixed stationarity equation. The determinant
and this explicit quadratic direction give two formulations of the failure.

## 5. Exact auxiliary execution

```sh
python3 -B scripts/verify_inverse_gravity_mixed_test_sufficiency.py \
  --output reports/2026-10-08--ig-s2-mixed-test-sufficiency-certificate.txt
```

Observed exit 0, exact arithmetic, SymPy 1.14.0. The permanent code verifies
the 27-configuration central diagonal average, unchanged shifted diagonal
averages, scalar/curvature face counts, and the symbolic two-by-two determinant
and coherent cost. The full-H_N transition exclusion and all-volume state
admission proofs are analytic above, not independent transcription checks.
No many-body Hamiltonian, vacuum projector, SDP or provider review is used.

## 6. Limit and single remaining obligation

The added stationarity equation does not supply the desired bound. The
two-operator positive cost matrix supplies an additional genuine necessary
condition and eliminates the exhibited false positive, but no inequality
linking it to a small true-ground D_R(p_L) has been proved.
The remaining obligation is an explicit operator/ground-expectation
inequality connecting that admitted mixed-cost matrix to the fixed curvature
numerator, with volume-uniform constants. Its two local exclusions alone
are not a reason to claim such an inequality exists or to enlarge the test
family indefinitely. The spectral gate remains OPEN, without a maturity
increase or independent-review promotion.


## 7. Bounded mixed-cost transfer attempt — 2026-10-10

**Authorization and baseline.** The user instructed "Intentalo" after a
bounded proposal to obtain a quantitative upper energy estimate or a
rigorously scoped obstruction. The dated continuation in the existing
contract was committed before this derivation at
`2a9c1b9d533b02ef82186ce9cd466a5571c49f11`, based on
`dfe2241a596289c718e9dc54d12c43c10cc2a33b`.
The October 8 Sections 1–6 above are retained verbatim.

**Outcome.** No true-ground numerator upper bound or Rayleigh bound was
obtained. Two restricted routes can be audited exactly:

- positivity of the joint mixed/curvature energy matrix gives a *lower*
  bound on the curvature block and an uncontrolled positive residual;
- the fixed mixed operators, even the associative algebra they generate,
  cannot reconstruct the curvature probes as full operators. Two global
  qutrit charge differences separate them, with a nonvanishing normalized
  Hilbert–Schmidt approximation error at every admitted volume.

These are author-side analytic statements, not an independent review.
The second statement does not exclude reconstruction *on the unknown
ground space*. Neither statement proves that all the original angle
ground inequalities plus the mixed conditions are insufficient for the
actual N-type Hamiltonian.

Verdicts:
`SCHUR_PSD_UPPER_TRANSFER_NOT_OBTAINED`;
`NEUTRAL_OPERATOR_RECONSTRUCTION_EXCLUDED_AUTHOR_SIDE`;
`BOUNDED_TRANSFER_ATTEMPT_STOPPED_OPEN`.
`TENSOR_SPECTRAL_GATE_OPEN` remains unchanged.

### 7.1 Source checks and unchanged objects

Use exactly the full H_N, q=3, even periodic L>=4, fixed positive comparable
couplings independent of L, and B_+(p), B_cross(p) from the curvature-probe
contract. Write N=L^3 and p_L=2pi/L along the fixed axis.

The local, git-ignored bibliography index is not present in this workspace.
The versioned curated catalog identifies Gu–Wen arXiv:0907.1203. Its primary
[v3 HTML](https://arxiv.org/html/0907.1203v3) was read in this session:
Sections V.1–V.3 for the scalar word, clock convention and curvature
stencils, and VII.1–VII.3 for the full Hamiltonian. The PDF fetch failed;
no new PDF-page verification or PDF hash computation is claimed.

Existing code was read without execution or modification:
`verify_inverse_gravity_constraint_module.py`,
`verify_inverse_gravity_local_gates.py`,
`verify_inverse_gravity_curvature_probes.py`,
`verify_inverse_gravity_mixed_ground_test.py`, and
`verify_inverse_gravity_mixed_test_sufficiency.py`, all in scripts/
at the baseline above. Their explicit stencils agree with the diagonal
species sums used below. The new results are proved analytically here;
previous certificates are not relabelled as tests of this addition.
No new scientific code, numerical output or external reviewer was used.

### 7.2 The full positive block and the direction of the bound

Let P_0 be the complete finite-volume ground projector, d_0=Tr P_0,
rho_0=P_0/d_0 and K=H_N-E_0 I>=0. Define the positive energy form
\[
 \langle A,B\rangle_K
 =\operatorname{Tr}\rho_0 A^\dagger K B
 =\operatorname{Tr}\rho_0 A^\dagger[H_N,B].
\]
The second identity uses H_N P_0=E_0 P_0. It does not require a numerical
estimate of E_0. It is valid for non-Hermitian A and B.

Take any finite list A_a of the existing mixed operators; it may include
all their translates and adjoints. Set
\[
 \mathcal M_{ab}=\langle A_a,A_b\rangle_K,\qquad
 X_{a\alpha}=\langle A_a,B_\alpha\rangle_K,\qquad
 F_{\alpha\beta}=\langle B_\alpha,B_\beta\rangle_K.
\]
The two-by-two local matrices in Section 4 are principal blocks of
mathcal M when the list contains P_i,S_iP_i. Knowing their positivity
does not supply the other entries of mathcal M or X.

For every true ground density,
\[
 \Gamma=\begin{pmatrix}\mathcal M&X\\X^\dagger&F\end{pmatrix}\succeq0.
\]
Indeed, its quadratic form is
\(\langle A(u)+B(z),A(u)+B(z)\rangle_K\).
Because [H_U,B]=[H_g,B]=0, the cross block can equivalently be written
\[
 X_{a\alpha}=\operatorname{Tr}\rho_0 A_a^\dagger[H_J,B_\alpha].
\]
Its ground expectations are still unknown.

Let mathcal M^+ be the Moore–Penrose inverse. Positivity first implies
\[
 (I-\mathcal M\mathcal M^+)X=0.
\]
To see this, take w in ker mathcal M and vary the real and imaginary
coefficient of w in the joint quadratic form; an uncancelled cross term
would make it negative. Completion of the square then gives
\[
 \boxed{F\succeq X^\dagger\mathcal M^+X.}
\]
More explicitly, for arbitrary u,z,
\[
 \begin{pmatrix}u\\z\end{pmatrix}^\dagger\Gamma
 \begin{pmatrix}u\\z\end{pmatrix}
 =(u+\mathcal M^+Xz)^\dagger\mathcal M(u+\mathcal M^+Xz)
 +z^\dagger(F-X^\dagger\mathcal M^+X)z.
\]
This also handles singular mathcal M. It is a standard Schur-complement
fact, not a novelty claim. Reversing this inequality would be an error.

There is an exact description of what remains uncontrolled. Regard
\[
 V_a=d_0^{-1/2}K^{1/2}A_aP_0,\qquad
 W_\alpha=d_0^{-1/2}K^{1/2}B_\alpha P_0
\]
as vectors in Hilbert–Schmidt space. If Pi_A is the orthogonal projection
onto span{V_a}, then
\[
 F=X^\dagger\mathcal M^+X+\mathcal R,\qquad
 \mathcal R_{\alpha\beta}
 =\langle(I-\Pi_A)W_\alpha,(I-\Pi_A)W_\beta\rangle_{\rm HS}\succeq0.
\]
This follows by orthogonally projecting W and using
Pi_A=V mathcal M^+ V^\dagger. Neither positivity nor the exclusion of tau
bounds mathcal R from above. The desired spectral inequality would require
control of the *sum* on the right relative to the actual ground-subtracted
Gram G. No such control has been obtained.

For clarity, even exact abstract knowledge of mathcal M and X would not
make joint PSD sufficient: mathcal M=J I, X=0, F=J I_2 and G=I_2 obey it
for every L but violate F<=C p_L G for sufficiently large L and fixed C.
They also admit D=2F with only the constant Fourier coefficient nonzero.
This is a countermodel to inference from these matrix constraints alone,
NOT a constructed N-type state, not a counterexample to the full set of
ground conditions, and not evidence for a physical spectral gap.

### 7.3 A full-operator reconstruction is blocked by qutrit charges

The natural way to remove mathcal R would be an identity expressing B
through the mixed operators. For the current operators a state-independent
identity of that kind is excluded.

Use the clock convention ZX=omega XZ, omega^3=1. Define
\[
 Q_1=\prod_i Z_{xx}(i)Z_{zz}(i)^\dagger,\qquad
 Q_2=\prod_i Z_{yy}(i)Z_{zz}(i)^\dagger.
\]
They commute and have order three. Here Q_1,Q_2 are algebraic charge
operators, unrelated to the excited-space projector I-P_0.

For an X word with diagonal-species total shifts (u_x,u_y,u_z) modulo 3,
conjugation by Q_1,Q_2 gives charges
\((u_x-u_z,u_y-u_z)\).
The unchanged stencils give:

| Word | Total diagonal shifts modulo 3 | (Q_1,Q_2) charges |
| --- | --- | --- |
| S_i | (2,2,2) | (0,0) |
| R_xx(i) | (0,1,1) | (2,0) |
| R_yy(i) | (1,0,1) | (0,2) |
| R_xy(i+(x+y)/2) | (0,0,2) | (1,1) |

For S_i each diagonal species has coefficients 4+1+1+1+1=8.
For R_xx and R_yy each nonzero diagonal species has 2+1+1=4.
For R_xy the four zz entries each have coefficient 2, totaling 8.
Reduction modulo 3 gives the table; signs reverse the charges for adjoints.
Translations and periodic identification preserve these sums.

Every P_i and its cyclic central-species variants are momentum-diagonal.
Thus they commute with both Q's, as do S_iP_i, their adjoints and Y_i.
The unital associative star algebra generated by these mixed operators is
contained in the neutral algebra
\[
 \mathfrak N=\{A:[A,Q_1]=[A,Q_2]=0\}.
\]
This remains true after arbitrary sums, products, translations and
L-dependent scalar coefficients of those generators.

Each signed curvature word has one of six nonzero charges
\((2,0),(1,0),(0,2),(0,1),(1,1),(2,2)\).
Consequently the charge twirl
\[
 {\cal E}(O)=\frac19\sum_{a,b=0}^2
 Q_1^aQ_2^b\,O\,Q_2^{-b}Q_1^{-a}
\]
satisfies E(B_alpha(p))=0 while E(A)=A for A in mathfrak N. The twirl is
orthogonal projection for the normalized full trace
tr_L=3^{-6N}Tr. Therefore
\[
 \operatorname{tr}_L A^\dagger B_\alpha(p)=0
 \quad\text{for every }A\in\mathfrak N.
\]
No nonzero B combination lies in that neutral algebra.

This does not assume that Q_1,Q_2 are symmetries of H_N. In particular
H_g need not commute with them. It gives no charge-selection rule for
rho_0 or for the energy form; using it as one would be an unjustified step.

The algebra above concerns the *mixed generators*. The original necessary
conditions also include curvature-angle polynomials, and B itself belongs
to that other algebra. Adding B as an input generator makes its reconstruction
tautological and leaves its unknown energy block as input. Thus the argument
does not exclude every possible use of the full frozen test family.

### 7.4 Quantitative full-trace residual, with a strict scope limit

The signed translated curvature words are distinct for even L>=4.
For a diagonal curvature word, in either active diagonal species the unique
coefficient-2 centre and two coefficient-1 endpoints fix its translate;
the inverse interchanges their multiplicities. The missing diagonal species
distinguishes R_xx from R_yy. R_xy uses only zz, on an xy square with
coefficient 2 at all four vertices (1 in its inverse); its square fixes
its centre on L>=4. It cannot equal either diagonal word.
This is an all-volume support argument, not extrapolation from L=4,6.

Distinct Weyl words are orthonormal for tr_L. Each B_+ has 4N signed
words, each with squared coefficient 1/(8N). B_cross has 2N such words.
The families do not overlap and Fourier phases have unit magnitude. Hence
\[
 \operatorname{tr}_L B_\alpha^\dagger B_\beta
 =\begin{pmatrix}1/2&0\\0&1/4\end{pmatrix}_{\alpha\beta}
 \quad\text{at every allowed axial momentum.}
\]
For B(z)=z_+ B_+ + z_cross B_cross and every A in mathfrak N,
\[
 \operatorname{tr}_L(B(z)-A)^\dagger(B(z)-A)
 =\frac{|z_+|^2}{2}+\frac{|z_\times|^2}{4}
  +\operatorname{tr}_L A^\dagger A.
\]
In particular, for unit z,
\[
 \inf_{A\in\mathfrak N}\|B(z)-A\|_{\rm op}
 \ \ge\ \sqrt{|z_+|^2/2+|z_\times|^2/4}\ \ge\ 1/2.
\]
The inequality uses normalized Hilbert–Schmidt norm <= operator norm.
Thus a vanishing full-operator remainder cannot be obtained from the
current mixed-generator algebra, even allowing all its products.

**This is not a lower bound on the true-ground residual mathcal R.**
The full trace is not rho_0; K^{1/2} and P_0 can annihilate directions
that have large full-trace norm. The estimate neither proves nor disproves
a small ground-projected error, a small curvature numerator, or gaplessness.

### 7.5 Decision and exact remaining information

The bounded attempt stops with no upper spectral estimate:

1. Direct PSD/Schur transfer has the wrong inequality direction for the
   required upper bound; the exact positive remainder is not controlled.
2. Full-operator reconstruction within the mixed algebra is excluded by
   the charge argument and its quantitative norm bound.
3. Ground-specific reconstruction or a different inequality using all
   the already admitted ground conditions remains logically possible,
   but has not been supplied. No physical feasible-state counterexample
   to that full family has been constructed here.

A useful continuation would need actual information on the vectors
K^{1/2}B_alpha P_0 (or directly on the quotient), sufficient to control
X^dagger mathcal M^+ X + mathcal R relative to G with constants independent
of L. Listing another positive local matrix does not supply that control.
The present attempt does not authorize an enlarged test hierarchy.

The use of rho_0 above also retains the existing degeneracy caveat: rank
two of an averaged G alone does not prove two independent physical excited
states. Pure-ground-vector control or a separate excited-range dimension
argument is still needed, along with tensor-sector admission and separation
from the remaining spectrum.

No E0, ground correlation, ground degeneracy, N-type gap, two-mode count,
QCA energy–tick bridge or Einstein result was calculated or promoted.
Recommendation: pause this direct transfer route pending a concrete,
ground-sensitive estimate or an independently justified different method.
This is a limit of the attempted argument, not a refutation of the model.
