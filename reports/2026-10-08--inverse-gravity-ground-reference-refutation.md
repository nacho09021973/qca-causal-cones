# IG-S2 — refutation of the first N-type ground-reference candidate

Date: 2026-10-08
Branch: `research/inverse-gravity-design`
Contract: `theory/INVERSE_GRAVITY_NTYPE_GROUND_REFERENCE_GATE.md`
Status: `ANALYTIC_PASS / REFUTED_AS_EXACT_GROUND_REFERENCE`

## 1. Candidate

The frozen candidate was

\[
|\Omega_L\rangle=\frac{P_S|0_L\rangle}{\|P_S|0_L\rangle\|},
\qquad
P_S=\prod_i\frac13\sum_{m=0}^{2}S(i)^m,
\]

with the fixed \(n_G=3\) Gu–Wen scalar stencils and six qutrit registers per
cell. The state is invariant under every scalar constraint \(S(i)\) and lies
in the vector sector \(V=1\).

## 2. Exact separation of the Hamiltonian terms

From Gu–Wen's printed compact N-type Hamiltonian (PDF pp. 18–20),

\[
H_N=H_U+H_J+H_g.
\]

The scalar constraints \(S(i)\) are products of angle shifts \(W_\theta\).
The operator \(H_U\) is a function of the commuting scalar and vector
constraint operators, so it commutes with every \(S(i)\). The N-type \(H_g\)
term is a function of the commuting angle Weyl operators entering the printed
\(\rho^{ab}\), so it also commutes with every \(S(i)\). Consequently,

\[
H_U|\Omega_L\rangle=0,
\qquad
H_g|\Omega_L\rangle\in\mathcal H_{S=1},
\]

where \(\mathcal H_{S=1}\) denotes the simultaneous scalar-invariant sector.

The N-type momentum term is diagonal in the \(L\)-basis. Combining the two
diagonal contributions in the printed expression gives, for \(J>0\),

\[
H_J=n_GJ\left[
 \frac12\sum_{i,a}(1-\cos(2\pi L^{aa}(i)/n_G))
 +2\sum_{i,ab=xy,yz,zx}(1-\cos(2\pi L^{ab}(i)/n_G))
\right].
\]

Thus every basis configuration has a nonnegative diagonal energy, and the
zero configuration has energy zero.

## 3. Non-constancy on the scalar orbit

Let \(|c_i\rangle=S(i)|0_L\rangle\). The frozen scalar stencil has a nonzero
coefficient modulo 3 (its central diagonal coefficient is \(4\equiv1\pmod3\));
therefore \(|c_i\rangle\ne|0_L\rangle\) on every declared torus \(L\ge3\).
At the two orbit points,

\[
\langle0_L|H_J|0_L\rangle=0,
\qquad
\langle c_i|H_J|c_i\rangle>0,
\]

because at least one qutrit has a nonzero \(L^{ab}\pmod3\), and all displayed
coefficients of \(H_J\) are positive.

The vector \(|\Omega_L\rangle\) is the uniform group-orbit sum, up to the
common multiplicity caused by any scalar-stencil stabilizer. Therefore
\(H_J|\Omega_L\rangle\) is not invariant under the scalar group: its
coefficients at \(|0_L\rangle\) and \(|c_i\rangle\) differ. Equivalently,

\[
Q_S H_J|\Omega_L\rangle\ne0,
\qquad Q_S=I-P_{S=1}.
\]

## 4. Refutation

Since \(H_U|\Omega_L\rangle=0\) and \(H_g|\Omega_L\rangle\) is scalar
invariant, while \(Q_SH_J|\Omega_L\rangle\ne0\),

\[
Q_SH_N|\Omega_L\rangle
=Q_SH_J|\Omega_L\rangle\ne0.
\]

Hence \(|\Omega_L\rangle\) is not an eigenvector of \(H_N(L)\) for \(J>0\).
It cannot be the exact finite-volume ground state, regardless of whether its
energy expectation is low.

## 5. Claim ceiling

`ANALYTIC_PASS / REFUTED_AS_EXACT_GROUND_REFERENCE` applies only to this fixed
projected constraint reference and \(J>0\). It is not a no-go for the N-type
Hamiltonian, its spectrum, or alternative correlated ground references. It
also does not establish a lower bound on \(E_0(L)\), a gap, or the absence of
tensor excitations.

The next required action is to freeze a different reference or to formulate a
ground-energy method that does not require this candidate to be an eigenstate.
