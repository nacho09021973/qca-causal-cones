# IG-S2 — a mixed local test excludes the product-state false positive

Date: 2026-10-08. Branch: `research/inverse-gravity-design`.
Contract frozen at `c15bde3`; permanent auxiliary code frozen at `47ddd26`
before execution. Evidence: author-side analytic derivation and auxiliary
finite checks; no independent review.

Verdict: `MIXED_STATIONARITY_TEST_ANALYTIC_PASS_AUTHOR_SIDE`.
The tensor spectral gate and the true-ground curvature cost remain OPEN.

## 1. Fixed test and hypotheses

Keep the complete q=3 N-type Hamiltonian, even periodic L>=4, and unchanged
positive comparable couplings. Use a fixed vertex i and its printed scalar
word S_i. Write Z_i=exp(2pi i Lxx(i)/3) and

\[
 P_i=(I+Z_i+Z_i^2)/3=\mathbf1_{L^{xx}(i)=0},\quad
 T_i=S_iP_i,\quad Y_i=i(T_i^\dagger-T_i).
\]

P_i is a *single-register* momentum projector, not a ground-space or full
constraint projector. The operator Y_i contains both angle shifts and
momentum projectors. Its support is precisely contained in the scalar
stencil: fifteen diagonal registers and twelve face registers, independent
of L. It is not assumed to preserve the full constraint kernel.

Primary equations inspected this session:
`biblioteca/arXiv-0907.1203.pdf`, Gu-Wen arXiv:0907.1203v3, p.14 Eq.(39)
and scalar shift convention, p.15 Eq.(46), and p.18 full N-type terms.
The scalar central coefficient is 4=1 modulo 3.

Since S_i maps central momentum 0 to 1, T_i is a partial isometry from the
central-0 subspace to the central-1 subspace, with the prescribed shifts of
other registers. Its two ranges are orthogonal. Thus T_i^2=0,
Y_i=Y_i^dagger, Y_i^2=P_i+S_iP_iS_i^dagger and ||Y_i||=1.

## 2. The exact off-diagonal matrix element of the full Hamiltonian

Let omega=|0_L> and c=S_i omega. They are orthogonal product configurations.
The scalar penalty is

\[
 H_{U,S}=3\widetilde U_2\sum_j
 \left[I-\tfrac12(S_j+S_j^\dagger)\right].
\]

There is precisely one word in this sum sending omega to c: S_i.
For all even L>=4 the diagonal supports of S_j have a unique common point
among the xx, yy and zz species, namely j. Equality of signed translated
words fixes that common centre. At that centre their coefficients are 1
for S_j and 2 for its inverse, so the sign is fixed as well. This proves
uniqueness without extrapolating finite collisions.

The vector penalties and H_J are diagonal, so their c/omega matrix element
vanishes. Every H_g cosine word has no diagonal-register species because
rho_aa contains only off-diagonal angles. Each rho_ab with a!=b has only
the bb diagonal species; its sine-product partner rho_ba has only aa.
Expanding the sines produces words containing at most two diagonal species.
In contrast, c has nonzero entries in all three diagonal species. No H_g
word can send omega to c, even after reduction modulo 3 or periodization.
Therefore, for the *complete unchanged* Hamiltonian,

\[
 h=\langle c,H_N\omega\rangle=-\frac32\widetilde U_2.
\]

Neither the comparable-coupling regime nor unknown ground correlations
affect this matrix element.

## 3. Nonzero stationarity residual

The chosen test obeys Y_i omega=-i c. Consequently

\[
 \langle\omega,i[H_N,Y_i]\omega\rangle
 =2\operatorname{Re}h=-3\widetilde U_2\ne0.
\]

Each individual contribution is resolved: the scalar penalty gives this
value, while H_J, vector penalties and H_g give zero in omega by Section 2.
In particular [H_U,Y_i]!=0, so Y_i is outside the common commutant whose
tests admitted omega in the preceding report.

Second derivation: define the normalized local unitary variation
omega(t)=exp(i t Y_i)omega. Its energy derivative at zero is

\[
 \frac{d}{dt}\langle\omega(t),H_N\omega(t)\rangle\big|_{t=0}
 =\langle\omega,i[H_N,Y_i]\omega\rangle=-3\widetilde U_2.
\]

Thus omega has an actual local energy-lowering direction for small positive
t. This confirms the sign and nonstationarity without knowing E0.
It does not introduce a new trial-vacuum architecture or claim an energy
error estimate for that variation.

Every density rho supported on the full ground space satisfies
Tr(rho i[H_N,Y_i])=0. The same is true of any stationary density, so this
test is a necessary ground condition, not a characterization of the vacuum.
It excludes omega but cannot distinguish all excited eigenstates from the
ground. Degeneracy of the ground space does not affect its validity.

## 4. A uniform local distinction from every true ground density

Let W_i=i[H_N,Y_i]. It is Hermitian and local. Only local Hamiltonian terms
h_a whose support meets that of Y_i enter the commutator. Let R be their
support union and C_loc=sum_a ||h_a|| over those terms. For all volumes
large enough to embed this fixed patch,

\[
 \|W_i\|\le2C_{\rm loc},\quad
 \|\rho_R-|0_R\rangle\langle0_R|\|_1
 \ge\frac{3\widetilde U_2}{\|W_i\|}
 \ge\frac{3\widetilde U_2}{2C_{\rm loc}}.
\]

Proof: the difference of the two W_i expectations is exactly 3 U2; apply
trace-norm/operator-norm duality to the reduced states. C_loc depends on
the fixed stencil and couplings, not on volume. On smaller declared tori
periodize all terms and use the actual finite-volume W_i norm. No explicit
numerical C_loc or optimal distance is claimed.

This gives genuine quantitative information about every full-H_N ground
density: its local reduced state differs from the momentum-zero product
state by a nonvanishing amount. It is not a bound on its curvature first
moment or long-range Gram correlator.

## 5. Permanent checks and limits

Command executed:

```sh
python3 -B scripts/verify_inverse_gravity_mixed_ground_test.py \
  --output reports/2026-10-08--ig-s2-mixed-ground-test-certificate.txt
```

Observed exit 0, exact arithmetic, SymPy 1.14.0. The local three-dimensional
matrix checks represent the central scalar orbit and projector algebra;
they are not a diagonalization of H_N. Fixed tori L=4,6 have respectively
128 and 432 distinct signed scalar translates, with one target match.
The diagonal-species check is structural, using the source property above;
it is not an independent transcription audit of all rho coordinates.
The analytic support argument supplies the all-volume conclusion.

No earlier verifier was modified. No unknown ground expectation, ground
energy, degeneracy, spectral gap or tensor excitation was computed.
No parameter changed, massive diagonalization or external review occurred.

## 6. One remaining obligation

The missing state-selection test has been supplied. Before any optimization,
the next obligation is to derive an explicit bound on the curvature first
moment from ground conditions that include this mixed test, or demonstrate
that those specified conditions still admit a false positive with a large
cost. Excluding omega alone is not a certificate that D_R(p_L) is small.
No automatic maturity increase or spectral promotion follows.
