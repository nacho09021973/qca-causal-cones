# IG-S2/M3 — compact tensor-probe commutator preflight

Date: 2026-10-08

Branch: `research/inverse-gravity-design`.
Authorization: user instruction "ok, primero el metodo tres".
Parent: `INVERSE_GRAVITY_DESIGN_CHARTER.md` and the five-method report.
Initial status: `OPEN`. This file fixes the questions before execution.

## 1. Domain and Hamiltonian

Use the full Gu–Wen N-type compact Hamiltonian, q=n_G=3, six qutrits per cell
on even periodic tori L>=4. Couplings \(\tilde U_1,\tilde U_2,\tilde J,\tilde g\)
are positive, fixed independently of L and comparable; no hierarchy is added.
Use the printed Eq.(39) on PDF p.14 and N-type expressions on p.18:
\[
 H_L=H_{U,S}+H_{U,V}+H_J+H_g,
\]
\[
 H_{U,S}=3\tilde U_2\sum_i(1-\operatorname{Re}S_i),\qquad
 H_{U,V}=3\tilde U_1\sum_{i,a}(1-\operatorname{Re}V_{i,a}),
\]
\[
 H_J=3\tilde J\left[
 \sum_{i,a}f(L^{aa}_i)+2\sum_{i,ab=xy,yz,zx}f(L^{ab}_i)
 -\tfrac12\sum_i f(L^{xx}_i+L^{yy}_i+L^{zz}_i)\right],
 \quad f(t)=1-\cos(2\pi t/3).
\]
H_g is the unchanged printed cosine/sine expression in rho, whose arguments
are sums of angle variables. Scalar/vector stencils, register offsets, signs
and clock orientation ZX=omega XZ are those of IG1a.
The true ground projector P_0 and ground energy E_0 refer to H_L on the full
Hilbert space, not the H_U kernel.

## 2. Frozen pair of microscopic probes

At each register define the bounded Hermitian operator
\[
 s^{ab}_i=(X^{ab}_i-(X^{ab}_i)^\dagger)/(2i).
\]
Indices i label the vertex for aa and the positive face at
\(i+(a+b)/2\) for ab. Set N=L^3, \(\kappa_L=2\pi/L\),
\(p_L=(0,0,\kappa_L)\), and \(k_L=(\pi,\pi,\pi)+p_L\).
Define the fixed pair
\[
 A_+(p)=\frac1{\sqrt{2N}}\sum_i(-1)^{i_x+i_y+i_z}
          e^{-ip\cdot i}(s^{xx}_i-s^{yy}_i),
\]
\[
 A_\times(p)=-\frac1{\sqrt{2N}}\sum_i(-1)^{i_x+i_y+i_z}
          e^{-ip\cdot(i+(x+y)/2)}s^{xy}_i.
\]
Along p||z the face-offset phase is one. Keep the displayed offset in the
definition rather than moving a face to a vertex. Even L makes staggering
periodic. If T_a translates local operators by +a,
\(T_a A_\alpha T_a^\dagger=e^{ik_L\cdot a}A_\alpha\).

Motivation, not exact physical admission: the source's continuum dictionary
on PDF p.20 is \(a_{aa}=(-1)^i\theta_{aa}\),
\(a_{ab}=-(-1)^i\theta_{ab}/2\) for a!=b.
Replacing sin(theta) by theta in its *formal small-angle tangent* makes the
two operators contractions with
\(e^+=\operatorname{diag}(1,-1,0)/\sqrt2\) and
\(e^\times_{xy}=e^\times_{yx}=1/\sqrt2\).
Both coefficient tensors are transverse and traceless for p||z.
No small-angle approximation is assumed at q=3. The exact probes can carry
constraint defects; tensor spectral weight, gauge separation and physical
TT interpretation must be demonstrated separately.

## 3. Exact matrix variational obligation

For a true ground vector Omega chosen as a simultaneous translation
eigenvector, let
\[
 b_\alpha=(I-P_0)A_\alpha\Omega,\quad
 G_{\alpha\beta}=\langle b_\alpha,b_\beta\rangle,\quad
 F_{\alpha\beta}=\langle b_\alpha,(H-E_0)b_\beta\rangle.
\]
Use all ground-space weight removal. Define the operator matrix
\[
 {\cal D}_{\alpha\beta}(p)
 =[A_\alpha(p)^\dagger,[H_L,A_\beta(p)]],\qquad
 D=\langle{\cal D}\rangle_\Omega.
\]
F<=D holds in matrix order in a true ground state. Test two sufficient routes:

1. Derive an L-uniform constant C_* with \(D\preceq C_*I_2\).
   If \(G\succeq g_*/\kappa_L I_2\) with g_*>0, this gives the target
   excitation bound \(C_*\kappa_L/g_*\).
2. Determine whether an operator bound
   \(\|\sum_{\alpha\beta}\bar z_\alpha{\cal D}_{\alpha\beta}(p)z_\beta\|
     \le C|p|^2\|z\|^2\)
   can hold uniformly. A counterexample to this state-independent bound
   does not refute a bound restricted to the true ground state or route 1.

No known Ward identity, vacuum correlations or exact ground state are assumed.
No scan or full-Hilbert-space diagonalization is admitted.

## 4. Permanent auxiliary certificate

After this contract is committed, add
`scripts/verify_inverse_gravity_sma_commutator.py` to check:

- the clock algebra and the general nested commutator for a diagonal Z-word
  against one/two local sine probes, by direct 3x3 and 9x9 matrices;
- the complete diagonal H_J vertex, including its trace cosine, using only
  the local three-register 27-dimensional matrix;
- single diagonal/face momentum shifts, their vector-link incidences and the
  exact zero-product-state matrix of the double commutator;
- the two coefficient tensors' TT algebra and the sufficient matrix
  variational implication, by the analytic proof recorded in the report.

The script checks local identities and witness coefficients only. Analytic
support counting proves all-volume statements. It does not evaluate any
true ground-state correlation, ground projector, or excitation spectrum.
Arithmetic is exact; tolerance zero. Output is retained in a named report
artifact only after all assertions pass. Failed attempts are retained.

## 5. Exit criteria

- `COMMUTATOR_PREFLIGHT_ANALYTIC_PASS_AUTHOR_SIDE`: exact identities and an
  L-uniform bound proved; finite auxiliary checks agree.
- `STATE_INDEPENDENT_QUADRATIC_BOUND_FAIL`: a state witness disproves that
  stronger operator-norm route for this pair.
- `SPECTRAL_UPPER_BOUND_CONDITIONAL_ON_GRAM`: route 1 is proved conditional on
  its true-ground-state Gram lower bound.
- `OPEN`: Gram, physical tensor identification, or other required estimates
  are missing. A failure concerns only this frozen pair and stated bound.

No R3/R4 promotion, independent review, continuum z=1 result, QCA tick or
Einstein result is obtained by these auxiliary identities.
