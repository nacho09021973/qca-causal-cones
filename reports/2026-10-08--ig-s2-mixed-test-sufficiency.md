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
