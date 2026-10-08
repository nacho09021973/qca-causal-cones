# IG-S2 — refutation of the first N-type ground-reference candidate

Date: 2026-10-08
Branch: `research/inverse-gravity-design`
Contract: `theory/INVERSE_GRAVITY_NTYPE_GROUND_REFERENCE_GATE.md`
Status: `ANALYTIC_PASS_AUTHOR_SIDE / REFUTED_AS_EXACT_GROUND_REFERENCE`

Correction, 2026-10-08: the version published at `edf54ff` incorrectly replaced
the cosine of the sum of diagonal momenta by separate cosines. That proof
must not be cited as written. Sections 2–3 below rederive the result with the
printed compact Hamiltonian. The conclusion survives for the frozen q=3
candidate; there is no independent review of this repaired derivation.
The candidate preregistration is `801bc0e`.

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

The N-type momentum term is diagonal in the \(L\)-basis. With
\(f_q(t)=1-\cos(2\pi t/q)\), the expression printed on PDF p.18 is

\[
H_J=q\tilde J\left[
 \sum_{i,a}f_q(L^{aa}(i))
 +2\sum_{i,ab=xy,yz,zx}f_q(L^{ab}(i))
 -\frac12\sum_i f_q\left(\sum_a L^{aa}(i)\right)
\right].
\]

The negative term couples the three diagonal registers at each vertex and
cannot be combined with the first sum. Here and below \(\tilde J>0\).
For the frozen q=3 only, \(f_3(t)=\frac32\mathbf1_{t\ne0\bmod3}\).
At a vertex with r nonzero diagonal registers the diagonal contribution,
divided by \(3\tilde J\), is
\(\frac32r-\frac34\mathbf1_{\sum_a L^{aa}\ne0\bmod3}\).
It vanishes if r=0 and is at least \(3/4\) if r>0.
The off-diagonal-register contributions are nonnegative. Thus \(H_J\ge0\)
for q=3 and \(\tilde J>0\), but this is not a general-q positivity theorem.

## 3. Non-constancy on the scalar orbit

Let \(|c_i\rangle=S(i)|0_L\rangle\). The frozen scalar stencil has a nonzero
coefficient modulo 3 (its central diagonal coefficient is \(4\equiv1\pmod3\));
therefore \(|c_i\rangle\ne|0_L\rangle\) on every declared torus \(L\ge3\).
At the two orbit points,

\[
\langle0_L|H_J|0_L\rangle=0,
\qquad
\langle c_i|H_J|c_i\rangle=162\tilde J>0.
\]

Here is a direct count using the printed scalar stencil, independently of the
preceding positivity argument. At the central vertex the diagonal momenta
are (1,1,1) modulo 3, contributing \(9/2\) inside the square bracket.
At each of the six distinct nearest-neighbour vertices, two diagonal
registers equal 1 and one equals 0, contributing \(3-3/4=9/4\).
There are twelve distinct face registers with value -1, each contributing 3.
The sum is \(9/2+6(9/4)+12(3)=54\), multiplied by \(3\tilde J\).
These supports remain distinct for all L>=3, including L=3. Both this direct
evaluation and the q=3 positivity argument prove non-constancy on the orbit.

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

Hence \(|\Omega_L\rangle\) is not an eigenvector of \(H_N(L)\) for \(\tilde J>0\).
It cannot be the exact finite-volume ground state, regardless of whether its
energy expectation is low.

## 5. Claim ceiling

`ANALYTIC_PASS_AUTHOR_SIDE / REFUTED_AS_EXACT_GROUND_REFERENCE` applies only
to this fixed q=3 projected reference and \(\tilde J>0\). It is not a no-go for the N-type
Hamiltonian, its spectrum, or alternative correlated ground references. It
also does not establish a lower bound on \(E_0(L)\), a gap, or the absence of
tensor excitations.

The next required action is to freeze a different reference or to formulate a
ground-energy method that does not require this candidate to be an eigenstate.
